# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1 **你的审查侧重：方法严谨性 + 实验设计** ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via 

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 92
- **Recorded user turns:** 3
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/c90336b9-14fd-4019-93e1-2d9dae199ea7.jsonl`
- **Structured JSON:** [`570b22dc580ed3db7ebb.json`](../../sessions/57/570b22dc580ed3db7ebb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T07:07:36.945Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T07:07:36.945Z",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### Venue 信息\n- 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 长文 8 页正文（Limitations/Ethics/References/Appendix 不计入）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: double-blind\n\n### 论文路径\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各章节在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex\n- Appendix: `docs/paper/sections/appendix.tex`\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **方法论严谨性**\n   - 5 个 confidence signal 的定义是否数学上严密？有无遗漏或错误？\n   - \"instance-level vs per-sample\" 的区分是否清晰且正确？\n   - MBR / consensus-proximity selection 的形式化是否完整？\n   - Soft Jaccard 的分母选择 (max 而非 union) 是否合理？论文声称差异 <0.01 但未给出证据\n\n2. **实验设计与统计分析**\n   - 4 个 NER benchmark 的选择是否合理？是否存在 cherry-picking？\n   - seed 数量（primary 1 seed, selection 2 seeds）是否足够？3-seed stability claim 是否可靠？\n   - bootstrap / sign test / TOST 等统计检验的使用是否恰当？\n   - p 值报告是否一致？多重比较校正是否充分？\n   - 论文声称 \"correlation-selection gap\" 时的统计基础是否牢固？\n   - degeneracy 与 LP selection 的 n=3 datasets 梯度关系是否过度解读？\n   - LoRA rank=8 ablation: 7.2% vs 21% degeneracy 但 selection 仍失败——这是否足以支撑 \"necessary but not sufficient\" 的 claim？\n\n3. **Claim 与 Evidence 对应**\n   - 每个 Contribution 是否有充分的实验支撑？\n   - 负面结果的解读是否过度？（e.g., \"fails\" vs \"not statistically significant\"）\n   - Oracle headroom 的计算方式是否合理？\n   - 自由格式解码 ablation 的结论（\"compression is model-intrinsic\"）是否过强？\n\n4. **实验可复现性**\n   - 训练细节是否充分（LoRA 参数、学习率、batch size、epoch、data split）？\n   - 推理设置是否完整（vLLM 版本、constrained decoding 细节）？\n   - 评估 protocol 是否清晰（gold-filtered vs full-set 的切换）？\n\n请按以下格式输出审稿报告：\n```\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n## Questions (需要作者澄清)\n## Missing References\n## Detailed Comments (逐节)\n## Overall Score (strong reject / weak reject / borderline / weak accept / strong accept)\n## Confidence (1-5)\n```"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T07:07:36.948Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T07:07:36.948Z",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

## Round 1

82 recorded events

### User

_source line 3 · 2026-05-17T07:07:36.979Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计**

### Venue 信息
- 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- 截止日期: 2026-05-25
- 页数限制: 长文 8 页正文（Limitations/Ethics/References/Appendix 不计入）
- 模板: ACL style (`\usepackage[review]{acl}`)
- 匿名规则: double-blind

### 论文路径
- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`
- 各章节在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex
- Appendix: `docs/paper/sections/appendix.tex`

### 你的审查重点

请从以下维度严格评审：

1. **方法论严谨性**
   - 5 个 confidence signal 的定义是否数学上严密？有无遗漏或错误？
   - "instance-level vs per-sample" 的区分是否清晰且正确？
   - MBR / consensus-proximity selection 的形式化是否完整？
   - Soft Jaccard 的分母选择 (max 而非 union) 是否合理？论文声称差异 <0.01 但未给出证据

2. **实验设计与统计分析**
   - 4 个 NER benchmark 的选择是否合理？是否存在 cherry-picking？
   - seed 数量（primary 1 seed, selection 2 seeds）是否足够？3-seed stability claim 是否可靠？
   - bootstrap / sign test / TOST 等统计检验的使用是否恰当？
   - p 值报告是否一致？多重比较校正是否充分？
   - 论文声称 "correlation-selection gap" 时的统计基础是否牢固？
   - degeneracy 与 LP selection 的 n=3 datasets 梯度关系是否过度解读？
   - LoRA rank=8 ablation: 7.2% vs 21% degeneracy 但 selection 仍失败——这是否足以支撑 "necessary but not sufficient" 的 claim？

3. **Claim 与 Evidence 对应**
   - 每个 Contribution 是否有充分的实验支撑？
   - 负面结果的解读是否过度？（e.g., "fails" vs "not statistically significant"）
   - Oracle headroom 的计算方式是否合理？
   - 自由格式解码 ablation 的结论（"compression is model-intrinsic"）是否过强？

4. **实验可复现性**
   - 训练细节是否充分（LoRA 参数、学习率、batch size、epoch、data split）？
   - 推理设置是否完整（vLLM 版本、constrained decoding 细节）？
   - 评估 protocol 是否清晰（gold-filtered vs full-set 的切换）？

请按以下格式输出审稿报告：
```
## Summary (2-3 句)
## Strengths (逐条)
## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])
## Questions (需要作者澄清)
## Missing References
## Detailed Comments (逐节)
## Overall Score (strong reject / weak reject / borderline / weak accept / strong accept)
## Confidence (1-5)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "9378ad67-c52f-496b-9a0a-4058750fa47e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T07:07:36.978Z_

```json
{
  "parentUuid": "9378ad67-c52f-496b-9a0a-4058750fa47e",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "14f3013d-349a-4943-9893-585cdac937fb",
  "timestamp": "2026-05-17T07:07:36.978Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T07:07:36.978Z_

```json
{
  "parentUuid": "14f3013d-349a-4943-9893-585cdac937fb",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "32c223a9-7192-409e-b72d-868127e62eca",
  "timestamp": "2026-05-17T07:07:36.978Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T07:07:36.978Z_

```json
{
  "parentUuid": "32c223a9-7192-409e-b72d-868127e62eca",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bb6a800e-6e0d-46db-9d66-4a67d5fd56c2",
  "timestamp": "2026-05-17T07:07:36.978Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Assistant

_source line 8 · 2026-05-17T07:07:45.109Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform a Round 1 review of a paper for EMNLP 2026. I need to:

1. First, follow the "审查前必做（Step 0）" - search for EMNLP 2026 / ACL ARR reviewer guidelines
2. Read the paper (main.tex and all section files)
3. Provide a detailed review focusing on methodology rigor and experimental design

Let me start by searching for the reviewer guidelines and reading the paper simultaneously.

Let me first load the tools I need (WebSearch for reviewer guidelines, and pdf_to_images for the paper). 

I realize the paper is in .tex format so I can read it directly without conversion. Let me search for the reviewer guidelines while loading the paper files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb6a800e-6e0d-46db-9d66-4a67d5fd56c2",
  "isSidechain": false,
  "requestId": "req_011Cb7ifyT7NvYxu6uf2c8pm",
  "type": "assistant",
  "uuid": "7f2f186e-3c14-468e-9985-a6dcbae6fc22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7L73uvf2my98jtjPKDeaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15287,
      "cache_read_input_tokens": 11841,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 538,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15287
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-17T07:07:45.423Z_

我开始执行 Round 1 审稿。首先搜索 ACL ARR 官方 reviewer guidelines，同时读取论文各章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f2f186e-3c14-468e-9985-a6dcbae6fc22",
  "isSidechain": false,
  "requestId": "req_011Cb7ifyT7NvYxu6uf2c8pm",
  "type": "assistant",
  "uuid": "deeff103-89d3-496d-b727-816d3da5db01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7L73uvf2my98jtjPKDeaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15287,
      "cache_read_input_tokens": 11841,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 538,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15287
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T07:07:46.381Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ah2US7efRhzbCxH2v9XihZ`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "deeff103-89d3-496d-b727-816d3da5db01",
  "isSidechain": false,
  "requestId": "req_011Cb7ifyT7NvYxu6uf2c8pm",
  "type": "assistant",
  "uuid": "a16730da-15bc-4771-b8bf-24340156309c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7L73uvf2my98jtjPKDeaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15287,
      "cache_read_input_tokens": 11841,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 538,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15287
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T07:07:47.790Z_

<details><summary>↩ Tool result · `toolu_01TPTFevcEXL7fLqGqnzudDv`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	These signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
12	Yet quality estimation does not translate to structural selection---the \textbf{correlation-selection gap} (the disparity between a signal's ability to rank instances reliably and its failure to select the best output within a single instance): structural best-of-$N$ selection matches or degrades greedy decoding ($T{=}0$) despite 12--14~pp oracle headroom.
13	The gap has two empirical causes: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 10--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{LP compression}---median within-instance range of 0.041 nats (\S\ref{sec:discussion}).
14	LP selection is degeneracy-gated: significant at 10\% degeneracy ($+1.36$~pp, $p{<}0.001$), sub-significant at 21\% ($+0.42$~pp), and absent at 58\%.
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=\textwidth]{fig_overview}
19	\caption{The correlation-selection gap. \textbf{Left}: consistency signals reliably predict instance-level quality ($\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82). \textbf{Right}: quality estimation does not translate to selection---all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\S\ref{sec:discussion}).}
20	\label{fig:overview}
21	\end{figure*}
22	
23	We evaluate five signals from three families---structural, surface, and model-internal---on SciERC \cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).
24	We vary candidate pool size ($N{\in}\{2,\ldots,32\}$), signal sophistication, and model capacity within the 4B--8B range; behavior at 70B+ scales remains an open question.
25	An exploratory extension to relation extraction is reported in Appendix~\ref{app:re_extension}.
26	Our contributions:
27	\begin{enumerate}
28	    \item \textbf{Quality estimation framework.}
29	    We systematically evaluate five confidence signals from three families (structural, surface, model-internal) for LLM-based NER across four benchmarks spanning a difficulty gradient, two model families, and a 4B scale ablation.
30	    Structural signals reliably predict output quality (VC $\rho{=}0.38$ on the primary test bed; EM AUROC${=}0.82$ on CoNLL), with difficulty-dependent but model-stable rankings that support selective prediction and error flagging.
31	
32	    \item \textbf{Diagnosis of the correlation-selection gap.}
33	    We identify a three-layer failure:
34	    (a)~four instance-level signals cannot rank candidates within an instance \textit{by construction};
35	    (b)~MBR selection with well-aligned utility (within-instance $\rho{=}0.52$) fails because instance degeneracy (10--58\% of instances yield identical outputs) collapses the candidate pool;
36	    (c)~LP, the sole per-sample signal, carries genuine ranking information but suffers from extreme compression (median range 0.041 nats).
37	    A diagnostic chain (LoRA-rank ablation, free-form decoding, entity-token LP, supervised signal combination) confirms the bottleneck lies in the feature space, not signal aggregation.
38	
39	    \item \textbf{Degeneracy as a regime boundary.}
40	    LP selection effectiveness is inversely associated with degeneracy rate across three datasets (58\% $\to$ fail, 21\% $\to$ $+0.42$~pp, 10\% $\to$ $+1.36$~pp at $p{<}0.001$); entity-type-level analysis provides stronger statistical grounding ($\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$).
41	    In the low-degeneracy regime, LP selection scales with $N$ ($+0.52$~pp from $N{=}8$ to $N{=}16$, paired $p{=}0.003$).
42	\end{enumerate}
43	
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f94ad0a-b76e-4e1c-9eed-98694d939536",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "cf258d36-4614-48f9-b49c-dbcc72b7b3f8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \\citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \\cite{snell2025scaling, brown2024monkeys}.\nBut named entity recognition (NER) poses a structurally different challenge: the output is a \\textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.\n\nPrior work on confidence estimation for LLM-based IE has conflated \\textit{quality estimation} (which inputs does the model handle reliably?) with \\textit{sample selection} (which of $N$ outputs is best?).\nExisting self-consistency methods \\cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\n\\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.\n\nA methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.\nThese signals achieve reliable quality estimation ($\\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82; Figure~\\ref{fig:overview}), supporting selective prediction and error flagging.\nYet quality estimation does not translate to structural selection---the \\textbf{correlation-selection gap} (the disparity between a signal's ability to rank instances reliably and its failure to select the best output within a single instance): structural best-of-$N$ selection matches or degrades greedy decoding ($T{=}0$) despite 12--14~pp oracle headroom.\nThe gap has two empirical causes: (a)~\\textit{instance degeneracy}---fine-tuned models produce identical outputs for 10--58\\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\\rho{=}0.52$); and (b)~\\textit{LP compression}---median within-instance range of 0.041 nats (\\S\\ref{sec:discussion}).\nLP selection is degeneracy-gated: significant at 10\\% degeneracy ($+1.36$~pp, $p{<}0.001$), sub-significant at 21\\% ($+0.42$~pp), and absent at 58\\%.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: consistency signals reliably predict instance-level quality ($\\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82). \\textbf{Right}: quality estimation does not translate to selection---all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\\S\\ref{sec:discussion}).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe evaluate five signals from three families---structural, surface, and model-internal---on SciERC \\cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \\cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \\cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \\cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).\nWe vary candidate pool size ($N{\\in}\\{2,\\ldots,32\\}$), signal sophistication, and model capacity within the 4B--8B range; behavior at 70B+ scales remains an open question.\nAn exploratory extension to relation extraction is reported in Appendix~\\ref{app:re_extension}.\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Quality estimation framework.}\n    We systematically evaluate five confidence signals from three families (structural, surface, model-internal) for LLM-based NER across four benchmarks spanning a difficulty gradient, two model families, and a 4B scale ablation.\n    Structural signals reliably predict output quality (VC $\\rho{=}0.38$ on the primary test bed; EM AUROC${=}0.82$ on CoNLL), with difficulty-dependent but model-stable rankings that support selective prediction and error flagging.\n\n    \\item \\textbf{Diagnosis of the correlation-selection gap.}\n    We identify a three-layer failure:\n    (a)~four instance-level signals cannot rank candidates within an instance \\textit{by construction};\n    (b)~MBR selection with well-aligned utility (within-instance $\\rho{=}0.52$) fails because instance degeneracy (10--58\\% of instances yield identical outputs) collapses the candidate pool;\n    (c)~LP, the sole per-sample signal, carries genuine ranking information but suffers from extreme compression (median range 0.041 nats).\n    A diagnostic chain (LoRA-rank ablation, free-form decoding, entity-token LP, supervised signal combination) confirms the bottleneck lies in the feature space, not signal aggregation.\n\n    \\item \\textbf{Degeneracy as a regime boundary.}\n    LP selection effectiveness is inversely associated with degeneracy rate across three datasets (58\\% $\\to$ fail, 21\\% $\\to$ $+0.42$~pp, 10\\% $\\to$ $+1.36$~pp at $p{<}0.001$); entity-type-level analysis provides stronger statistical grounding ($\\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$).\n    In the low-degeneracy regime, LP selection scales with $N$ ($+0.52$~pp from $N{=}8$ to $N{=}16$, paired $p{=}0.003$).\n\\end{enumerate}\n\n",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  },
  "sourceToolAssistantUUID": "1f94ad0a-b76e-4e1c-9eed-98694d939536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T07:07:46.387Z_

<details><summary>↩ Tool result · `toolu_01Ah2US7efRhzbCxH2v9XihZ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a16730da-15bc-4771-b8bf-24340156309c",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "9e36f40a-4c8a-41e8-b60b-f5f897d5b742",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "a16730da-15bc-4771-b8bf-24340156309c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T07:07:46.879Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T6nwAyJppMy86N4UXnMxgG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e36f40a-4c8a-41e8-b60b-f5f897d5b742",
  "isSidechain": false,
  "requestId": "req_011Cb7ifyT7NvYxu6uf2c8pm",
  "type": "assistant",
  "uuid": "8bd1af5b-ccd0-4f6e-b70b-d6e4e414b16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7L73uvf2my98jtjPKDeaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15287,
      "cache_read_input_tokens": 11841,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 538,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15287
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T07:07:46.894Z_

<details><summary>↩ Tool result · `toolu_01T6nwAyJppMy86N4UXnMxgG`</summary>

```text
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
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
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
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bd1af5b-ccd0-4f6e-b70b-d6e4e414b16c",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "6f7dcc7f-bf41-4293-aab5-7412fe1fc811",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ Why Confidence Signals Fail to Scale Structured Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).\nCoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\nCode and data will be released upon acceptance at [anonymized URL].\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "8bd1af5b-ccd0-4f6e-b70b-d6e4e414b16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T07:07:47.404Z_

<details open><summary>🔧 Tool call — Read · `toolu_012uDNLqCJnyXTY9X9Ktu1JA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f7dcc7f-bf41-4293-aab5-7412fe1fc811",
  "isSidechain": false,
  "requestId": "req_011Cb7ifyT7NvYxu6uf2c8pm",
  "type": "assistant",
  "uuid": "8bab8fe3-7c95-4255-8069-8c14c27a2d03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7L73uvf2my98jtjPKDeaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15287,
      "cache_read_input_tokens": 11841,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 538,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15287
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T07:07:47.409Z_

<details><summary>↩ Tool result · `toolu_012uDNLqCJnyXTY9X9Ktu1JA`</summary>

```text
1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability, LP)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient, using 4B--8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction.
5	However, quality estimation does not translate to sample selection---the \textit{correlation-selection gap}: despite ${\sim}$13~pp oracle headroom, no signal consistently outperforms greedy decoding.
6	The gap has a three-layer structure: four instance-level signals cannot rank candidates within an instance by construction; MBR selection with well-aligned utility ($\rho{=}0.52$) fails because instance degeneracy (10--58\% identical outputs) eliminates headroom; and LP carries genuine per-sample information but is compressed to near-ineffectiveness (median range 0.041 nats).
7	LP selection is inversely associated with degeneracy: at 10\% (Few-NERD), $+1.36$~pp ($p{<}0.001$); at 58\% (CoNLL), LP fails.
8	In the low-degeneracy regime, LP scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
9	Closing the gap for structural signals likely requires learned per-sample scoring.
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bab8fe3-7c95-4255-8069-8c14c27a2d03",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "9e326d38-4b41-4bbe-8adc-7fdeef44c599",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nSelf-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \\textit{sets} of entities with partial overlap, where no majority vote analog exists.\nWe evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability, LP)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient, using 4B--8B models.\nAll signals achieve reliable quality estimation ($\\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction.\nHowever, quality estimation does not translate to sample selection---the \\textit{correlation-selection gap}: despite ${\\sim}$13~pp oracle headroom, no signal consistently outperforms greedy decoding.\nThe gap has a three-layer structure: four instance-level signals cannot rank candidates within an instance by construction; MBR selection with well-aligned utility ($\\rho{=}0.52$) fails because instance degeneracy (10--58\\% identical outputs) eliminates headroom; and LP carries genuine per-sample information but is compressed to near-ineffectiveness (median range 0.041 nats).\nLP selection is inversely associated with degeneracy: at 10\\% (Few-NERD), $+1.36$~pp ($p{<}0.001$); at 58\\% (CoNLL), LP fails.\nIn the low-degeneracy regime, LP scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).\nClosing the gap for structural signals likely requires learned per-sample scoring.\n\\end{abstract}\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "8bab8fe3-7c95-4255-8069-8c14c27a2d03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T07:07:47.780Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TPTFevcEXL7fLqGqnzudDv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e326d38-4b41-4bbe-8adc-7fdeef44c599",
  "isSidechain": false,
  "requestId": "req_011Cb7ifyT7NvYxu6uf2c8pm",
  "type": "assistant",
  "uuid": "1f94ad0a-b76e-4e1c-9eed-98694d939536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7L73uvf2my98jtjPKDeaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15287,
      "cache_read_input_tokens": 11841,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 538,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15287
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验设计**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics/Ref…",
  "leafUuid": "cf258d36-4614-48f9-b49c-dbcc72b7b3f8",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Assistant

_source line 20 · 2026-05-17T07:07:51.496Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the remaining sections of the paper and search for ACL ARR reviewer guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf258d36-4614-48f9-b49c-dbcc72b7b3f8",
  "isSidechain": false,
  "requestId": "req_011Cb7igmkveLTfWBtFMC7o7",
  "type": "assistant",
  "uuid": "15b91b94-9459-4d85-b568-e7b9b8f10297",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118ipYWiM9Yz31Pm9yNtLsT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3916,
      "cache_read_input_tokens": 27128,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 325,
          "cache_read_input_tokens": 27128,
          "cache_creation_input_tokens": 3916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3916
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T07:07:52.166Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013RGbSui4mtGLbUuu8K61Uj`</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15b91b94-9459-4d85-b568-e7b9b8f10297",
  "isSidechain": false,
  "requestId": "req_011Cb7igmkveLTfWBtFMC7o7",
  "type": "assistant",
  "uuid": "4efa4c87-c71c-4aef-b25d-92b1b0eab2bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118ipYWiM9Yz31Pm9yNtLsT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3916,
      "cache_read_input_tokens": 27128,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 325,
          "cache_read_input_tokens": 27128,
          "cache_creation_input_tokens": 3916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3916
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T07:07:52.483Z_

<details open><summary>🔧 Tool call — Read · `toolu_019t5dwNa4f6gCHS3ePpveHe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4efa4c87-c71c-4aef-b25d-92b1b0eab2bd",
  "isSidechain": false,
  "requestId": "req_011Cb7igmkveLTfWBtFMC7o7",
  "type": "assistant",
  "uuid": "4219b049-6ee3-4f95-9bfe-835a0a3d0e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118ipYWiM9Yz31Pm9yNtLsT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3916,
      "cache_read_input_tokens": 27128,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 325,
          "cache_read_input_tokens": 27128,
          "cache_creation_input_tokens": 3916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3916
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T07:07:53.654Z_

<details><summary>↩ Tool result · `toolu_01W3ib2pRXQxe6BQzcgqgAhR`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	For quality estimation, all signals achieve positive $\rho$ across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	For selection, LP is the only signal achieving significant gains, and only at low degeneracy: $+1.36$~pp on Few-NERD (10\% degeneracy, $p{<}0.001$), $+0.42$~pp on SciERC (21\%, $p{=}0.091$), failure on CoNLL (58\%).
7	Structural signals uniformly degrade selection regardless of dataset.
8	RE signal rankings are reported in Appendix~\ref{app:re_extension}.
9	
10	\paragraph{Why the gap exists.}
11	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
12	
13	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
14	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
15	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
16	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; Few-NERD (75\%) shows 10\%; SciERC (66\%) shows 21\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero---the tension between model quality and selection utility is inherent, though Few-NERD's low degeneracy despite high performance suggests that dataset-specific factors (number of entity types, semantic overlap) also modulate the rate.
17	Scale ablation confirms this tension: Qwen3-8B shows 21\% instance degeneracy on SciERC vs.\ 10.4\% for the weaker Qwen3-4B, despite comparable within-instance utility correlation ($\rho{=}0.52$ vs.\ $0.55$; Table~\ref{tab:degeneracy}).
18	Despite MBR's success in machine translation \cite{freitag2022high}, all consensus-proximity variants consistently fail because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Appendix~\ref{app:mbr_discussion}).
19	On SciERC, LP selection approximately matches greedy decoding ($T{=}0$; $\Delta{=}{+}0.2$~pp, $p{=}0.29$; Table~\ref{tab:selection}); on Few-NERD, where degeneracy drops to 10\%, LP achieves significant gains ($+1.36$~pp, $p{<}0.001$; Table~\ref{tab:fewnerd}), confirming that degeneracy is the gating factor for LP selection.
20	
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
25	\label{tab:degeneracy}
26	\begin{tabular}{lccc}
27	\toprule
28	& \shortstack{SciERC 8B\\($N{=}8$)} & \shortstack{SciERC 4B\\($N{=}8$)} & \shortstack{CoNLL 8B\\($N{=}16$)} \\
29	\midrule
30	Constant F1 & 21\% & 10.4\% & 58\% \\
31	Constant utility & 13\% & 7.0\% & 49\% \\
32	Oracle gap closed (non-deg.) & 23\% & 25.2\% & 41\% \\
33	Within-inst.\ SJ $\rho$ (median) & 0.524 & 0.550 & 0.994 \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ confirming weak but positive signal.
39	
40	\paragraph{Non-tied subset analysis.}
41	Where compression is mitigated, LP selection works.
42	Restricting to instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total; Table~\ref{tab:nontied_main}), within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied), and LP selection outperforms greedy by $+2.9$~pp ($p{=}0.004$).
43	The effect grows monotonically with $\varepsilon$ (full sweep in Appendix~\ref{app:logprob_ties}), and the $\varepsilon{=}0.05$ result survives Bonferroni correction over 5 comparisons.
44	This demonstrates that LP \textit{does} carry per-sample discriminative information; compression---not signal absence---is the bottleneck.
45	However, the effect size is sensitive to subset definition, and the non-tied subset constitutes only 40\% of instances, limiting practical impact.
46	
47	\begin{table}[t]
48	\centering
49	\small
50	\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\varepsilon{=}0.05$. Within-instance $\rho$ and selection gain both concentrate in the non-tied subset. Full $\varepsilon$ sweep in Appendix~\ref{app:logprob_ties}.}
51	\label{tab:nontied_main}
52	\begin{tabular}{lccc}
53	\toprule
54	Subset & $n$ & $\rho$(LP,F1) & LP $\Delta$ vs.\ greedy \\
55	\midrule
56	Tied (range ${<}0.05$) & 319 & 0.08 & ${\approx}0$ \\
57	Non-tied (range ${\geq}0.05$) & 210 & 0.39 & $+$2.9~pp ($p{=}0.004$) \\
58	\midrule
59	All instances & 529 & 0.248 & $+$0.2~pp ($p{=}0.29$) \\
60	\bottomrule
61	\end{tabular}
62	\end{table}
63	Stratifying by voting confidence reveals a complementary pattern: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\ref{app:vc_quartile}).
64	\paragraph{Effect of sample count.}
65	Increasing $N$ from 2 to 32 expands oracle headroom more than fourfold ($+4.4$ to $+19.2$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom reaches ${\sim}19$~pp---the best signal captures less than 5\% of the available improvement (Table~\ref{tab:n_scaling_selection}).
66	VC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.
67	Bootstrap significance testing at $N{=}32$ ($B{=}10{,}000$) confirms that LP shows a consistent positive trend ($+0.95$~pp, $p{=}0.091$) but does not reach significance at $\alpha{=}0.05$, while all signals except VC significantly outperform random selection ($p{<}0.001$; Table~\ref{tab:bootstrap_n32})---the gap is not a statistical artifact but a persistent, regime-dependent limitation.
68	
69	\paragraph{Effect of sampling temperature.}
70	Oracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing beyond $T{=}1.0$ ($+13.0$~pp at $T{=}1.2$; Table~\ref{tab:t_ablation} in Appendix), confirming that higher temperature produces more diverse candidate pools.
71	Structural QE signals (SJ $\rho$) improve with temperature ($0.297 \to 0.377$), while LP $\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades---consistent with LP compression being model-intrinsic rather than temperature-dependent.
72	Despite expanded headroom and improved QE signals at higher temperatures, selection gains remain negligible, further isolating the bottleneck at the within-instance ranking mechanism rather than signal quality or output diversity.
73	
74	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\rho$ than LP (Appendix~\ref{app:verbalized_confidence}; \citealp{bhattacharyya2026beyond}).
75	This intrinsic compression extends beyond logprobs: when explicitly prompted to verbalize confidence on a 1--10 scale, models cluster at 8--9 (CoNLL mean 9.24, std 1.32), exhibiting the same top-biased pattern regardless of output format.
76	
77	\paragraph{Signal combinations.}
78	We test three LP${\times}$VC combination strategies: VC-stratified LP selection, LP${\times}$VC product ranking, and LP tiebreaking within VC-equivalent groups.
79	All three fail to improve over greedy (best: $+0.2$~pp, $p{>}0.3$), consistent with VC's collapse on degenerate instances and LP's compression on the remainder.
80	An oracle tiebreaker---selecting the highest-F1 sample among VC-equivalent candidates---recovers $+7.9$~pp, confirming that per-sample signal \textit{exists} within VC-equivalent groups but current signals cannot extract it.
81	
82	\paragraph{Hypotheses for LP compression.}
83	We identify four (non-mutually-exclusive) mechanisms that may explain within-instance LP compression, though we do not isolate their individual contributions.
84	Two are \textit{constraint-imposed}:
85	(b) \textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance;
86	(c) \textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation.
87	Two are \textit{model-learned}:
88	(a) \textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;
89	(d) \textit{format-token dilution}---fine-tuned models assign extremely high LP to schema tokens (\texttt{\{"entities": [}~etc.) that carry no extraction information, diluting the signal from entity-name tokens; free-form parse rates of 99.95\% confirm that format tokens dominate the sequence.
90	The constraint-imposed mechanisms (b)--(c) predict that free-form decoding should reduce compression; our NER ablation finds negligible change (std ratio 0.97; Appendix~\ref{app:freeform_ablation}), suggesting the model-learned mechanisms (a) and (d) are the primary drivers for NER.
91	
92	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
93	Removing grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.
94	Removing format constraints restores LP selection for RE: bootstrap mean $+2.35$~pp (95\% CI [$+0.24$, $+4.50$], $p{=}0.025$, $n{=}397$), though driven by magnitude asymmetry rather than instance-level win rate (sign test: 45W/45L/307T; Appendix~\ref{app:re_extension}).
95	More generally, LP selection failures show cross-seed stability (Jaccard${=}0.42$; Appendix~\ref{app:lp_failure_stability}), indicating a systematic rather than stochastic failure mode.
96	VC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \cite{eikema2022sampling, deguchi2024centroid}.
97	More broadly, all consensus-proximity strategies fail because instance degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Table~\ref{tab:degeneracy}; Appendix~\ref{app:mbr_discussion}).
98	
99	\paragraph{Ablation: entity-token LP.}
100	We directly test hypothesis (d) by isolating entity-mention tokens from the log-probability computation.
101	On SciERC, entity-token LP exhibits $4{\times}$ higher within-instance variance than full-sequence LP, confirming that format tokens do compress the signal.
102	However, entity-token LP selection performs strictly \textit{worse} than full-sequence LP on both datasets ($-2.0$~pp on SciERC, $-3.3$~pp on CoNLL).
103	Entity tokens are either too sparse (5.3\% of sequence tokens on SciERC) for stable estimation, or nearly saturated (79.4\% of instances tied on CoNLL)---consistent with CoNLL's limited entity vocabulary (4 types, high-frequency names) that fine-tuning drives to near-deterministic prediction.
104	This rules out format-token dilution as the primary cause of LP's selection failure and instead points to an intrinsic pattern: fine-tuned models assign near-deterministic probabilities to entity-name tokens themselves, leaving minimal discriminative signal regardless of aggregation scope.
105	Even disaggregating to entity-token logprobs fails to break compression: on CoNLL, 79.4\% of sample pairs share identical entity-token LP, confirming that compression operates at the representation level rather than being diluted by non-entity tokens.
106	
107	\paragraph{Pilot remedy.}
108	Entity-token LP represents a natural pilot remedy: if format-token dilution caused compression, restricting LP to entity tokens should recover selection ability.
109	Its failure---particularly the near-zero entity-token variance on CoNLL---suggests that effective remedies must address the underlying model confidence calibration rather than signal aggregation.
110	
111	\paragraph{Practical considerations.}
112	Multi-sample inference incurs $N{\times}$ compute cost.
113	For quality estimation---where signals are already reliable ($\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82)---$N{=}8$ samples suffice (Appendix~\ref{app:n_scaling}), making the cost acceptable for selective prediction or error flagging in high-stakes IE.
114	For selection, the cost-benefit is unfavorable: $8{\times}$ inference yields at most $+0.2$~pp over greedy ($p{>}0.05$).
115	Whether the trade-off shifts in low-convergence regimes (e.g., under-parameterized models where degeneracy drops below 10\%) remains an open question.
116	
117	\paragraph{Regime boundaries.}
118	The correlation-selection gap for structural signals is persistent across all four datasets, but LP selection is degeneracy-gated.
119	At the \textit{low-resource boundary} (WNUT-17, macro F1${\approx}$42\%), QE signals themselves become unreliable: full-set correlations are dominated by the zero/non-zero boundary (VC conditional $\rho{=}0.038$; Table~\ref{tab:wnut}), so selection is moot.
120	At the \textit{ceiling boundary} (CoNLL, F1${\approx}$91\%, 58\% degeneracy), selection shows only a marginal structural exception: VC achieves $+0.28$~pp ($p{<}0.03$) at $N{=}16$, capturing ${\sim}$10\% of the 2.5~pp oracle headroom (Appendix~\ref{app:n_scaling}); LP fails entirely.
121	In the \textit{moderate regime}, instance degeneracy determines LP effectiveness: at 21\% degeneracy (SciERC), LP gains are positive but sub-significant ($+0.42$~pp, $p{=}0.091$); at 10\% degeneracy (Few-NERD), LP achieves highly significant gains ($+1.36$~pp, $p{<}0.001$; Table~\ref{tab:fewnerd}).
122	The cross-dataset gradient (58\% $\to$ fail, 21\% $\to$ weak, 10\% $\to$ strong; $n{=}3$ datasets) is consistent with degeneracy below ${\sim}$15\% being a necessary condition for LP selection; entity-type-level evidence provides stronger statistical grounding (Spearman $\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$; Appendix~\ref{app:per_type_lp}).
123	When candidates differ sufficiently in quality, LP's per-sample signal can exploit the headroom.
124	The pattern persists at finer granularity: per-entity-type analysis on Few-NERD shows 7/8 types with positive LP gains, the sole exception being the highest-degeneracy type (Spearman $\rho(\text{degen}, \text{headroom}){=}{-}0.881$, $p{=}0.004$; Appendix~\ref{app:per_type_lp}).
125	Structural signals fail uniformly regardless of degeneracy because they rank candidates by typicality, not quality.
126	Whether these patterns persist on larger models (70B+) remains open.
127	
128	\paragraph{Methodological implications.}
129	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.
130	Even supervised combination of all five signals (logistic regression, MLP, random forest) fails to close the oracle gap (\S\ref{sec:robustness_main}), confirming the information bottleneck is in the features themselves, not the aggregation method.
131	Effective selection thus requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers, venktesh2025trust}, not confidence signal aggregation; $N{=}8$ captures most quality estimation benefit (Appendix~\ref{app:n_scaling}).
132	Structural signals are robust to domain shift when the training schema subsumes the target (Appendix~\ref{app:ood}).
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76570da8-d27f-44d2-80fc-d3813fac75cd",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "a85e9fc2-c365-488a-b0ed-db713fe6f53a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Implications for practitioners.}\nFor quality estimation, all signals achieve positive $\\rho$ across non-collapsed datasets (LP $\\rho{=}0.42$ on Few-NERD, VC $\\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL).\nRankings hold across model families and a 4B ablation (Table~\\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.\nFor selection, LP is the only signal achieving significant gains, and only at low degeneracy: $+1.36$~pp on Few-NERD (10\\% degeneracy, $p{<}0.001$), $+0.42$~pp on SciERC (21\\%, $p{=}0.091$), failure on CoNLL (58\\%).\nStructural signals uniformly degrade selection regardless of dataset.\nRE signal rankings are reported in Appendix~\\ref{app:re_extension}.\n\n\\paragraph{Why the gap exists.}\nWe identify two mechanisms: \\textit{instance degeneracy} (affecting consensus-proximity selection) and \\textit{LP compression} (affecting per-sample selection).\n\nWithin-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \\cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\\% (SciERC) to 41\\% (CoNLL) of the oracle gap.\nHowever, fine-tuned models exhibit pervasive \\textit{instance degeneracy}: 21\\% of SciERC instances (58\\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\\% (49\\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\\ref{tab:degeneracy}).\nInstance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.\nCoNLL (91\\% single-sample F1) exhibits 58\\% degeneracy; Few-NERD (75\\%) shows 10\\%; SciERC (66\\%) shows 21\\%; WNUT-17 (${\\approx}$42\\%, macro) shows near-zero---the tension between model quality and selection utility is inherent, though Few-NERD's low degeneracy despite high performance suggests that dataset-specific factors (number of entity types, semantic overlap) also modulate the rate.\nScale ablation confirms this tension: Qwen3-8B shows 21\\% instance degeneracy on SciERC vs.\\ 10.4\\% for the weaker Qwen3-4B, despite comparable within-instance utility correlation ($\\rho{=}0.52$ vs.\\ $0.55$; Table~\\ref{tab:degeneracy}).\nDespite MBR's success in machine translation \\cite{freitag2022high}, all consensus-proximity variants consistently fail because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Appendix~\\ref{app:mbr_discussion}).\nOn SciERC, LP selection approximately matches greedy decoding ($T{=}0$; $\\Delta{=}{+}0.2$~pp, $p{=}0.29$; Table~\\ref{tab:selection}); on Few-NERD, where degeneracy drops to 10\\%, LP achieves significant gains ($+1.36$~pp, $p{<}0.001$; Table~\\ref{tab:fewnerd}), confirming that degeneracy is the gating factor for LP selection.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\n\\label{tab:degeneracy}\n\\begin{tabular}{lccc}\n\\toprule\n& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}16$)} \\\\\n\\midrule\nConstant F1 & 21\\% & 10.4\\% & 58\\% \\\\\nConstant utility & 13\\% & 7.0\\% & 49\\% \\\\\nOracle gap closed (non-deg.) & 23\\% & 25.2\\% & 41\\% \\\\\nWithin-inst.\\ SJ $\\rho$ (median) & 0.524 & 0.550 & 0.994 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLog-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\\ref{tab:logprob_ties}), with pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ confirming weak but positive signal.\n\n\\paragraph{Non-tied subset analysis.}\nWhere compression is mitigated, LP selection works.\nRestricting to instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total; Table~\\ref{tab:nontied_main}), within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied), and LP selection outperforms greedy by $+2.9$~pp ($p{=}0.004$).\nThe effect grows monotonically with $\\varepsilon$ (full sweep in Appendix~\\ref{app:logprob_ties}), and the $\\varepsilon{=}0.05$ result survives Bonferroni correction over 5 comparisons.\nThis demonstrates that LP \\textit{does} carry per-sample discriminative information; compression---not signal absence---is the bottleneck.\nHowever, the effect size is sensitive to subset definition, and the non-tied subset constitutes only 40\\% of instances, limiting practical impact.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\\varepsilon{=}0.05$. Within-instance $\\rho$ and selection gain both concentrate in the non-tied subset. Full $\\varepsilon$ sweep in Appendix~\\ref{app:logprob_ties}.}\n\\label{tab:nontied_main}\n\\begin{tabular}{lccc}\n\\toprule\nSubset & $n$ & $\\rho$(LP,F1) & LP $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nTied (range ${<}0.05$) & 319 & 0.08 & ${\\approx}0$ \\\\\nNon-tied (range ${\\geq}0.05$) & 210 & 0.39 & $+$2.9~pp ($p{=}0.004$) \\\\\n\\midrule\nAll instances & 529 & 0.248 & $+$0.2~pp ($p{=}0.29$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\nStratifying by voting confidence reveals a complementary pattern: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\\ref{app:vc_quartile}).\n\\paragraph{Effect of sample count.}\nIncreasing $N$ from 2 to 32 expands oracle headroom more than fourfold ($+4.4$ to $+19.2$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}19$~pp---the best signal captures less than 5\\% of the available improvement (Table~\\ref{tab:n_scaling_selection}).\nVC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.\nBootstrap significance testing at $N{=}32$ ($B{=}10{,}000$) confirms that LP shows a consistent positive trend ($+0.95$~pp, $p{=}0.091$) but does not reach significance at $\\alpha{=}0.05$, while all signals except VC significantly outperform random selection ($p{<}0.001$; Table~\\ref{tab:bootstrap_n32})---the gap is not a statistical artifact but a persistent, regime-dependent limitation.\n\n\\paragraph{Effect of sampling temperature.}\nOracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing beyond $T{=}1.0$ ($+13.0$~pp at $T{=}1.2$; Table~\\ref{tab:t_ablation} in Appendix), confirming that higher temperature produces more diverse candidate pools.\nStructural QE signals (SJ $\\rho$) improve with temperature ($0.297 \\to 0.377$), while LP $\\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades---consistent with LP compression being model-intrinsic rather than temperature-dependent.\nDespite expanded headroom and improved QE signals at higher temperatures, selection gains remain negligible, further isolating the bottleneck at the within-instance ranking mechanism rather than signal quality or output diversity.\n\nA verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\\rho$ than LP (Appendix~\\ref{app:verbalized_confidence}; \\citealp{bhattacharyya2026beyond}).\nThis intrinsic compression extends beyond logprobs: when explicitly prompted to verbalize confidence on a 1--10 scale, models cluster at 8--9 (CoNLL mean 9.24, std 1.32), exhibiting the same top-biased pattern regardless of output format.\n\n\\paragraph{Signal combinations.}\nWe test three LP${\\times}$VC combination strategies: VC-stratified LP selection, LP${\\times}$VC product ranking, and LP tiebreaking within VC-equivalent groups.\nAll three fail to improve over greedy (best: $+0.2$~pp, $p{>}0.3$), consistent with VC's collapse on degenerate instances and LP's compression on the remainder.\nAn oracle tiebreaker---selecting the highest-F1 sample among VC-equivalent candidates---recovers $+7.9$~pp, confirming that per-sample signal \\textit{exists} within VC-equivalent groups but current signals cannot extract it.\n\n\\paragraph{Hypotheses for LP compression.}\nWe identify four (non-mutually-exclusive) mechanisms that may explain within-instance LP compression, though we do not isolate their individual contributions.\nTwo are \\textit{constraint-imposed}:\n(b) \\textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance;\n(c) \\textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation.\nTwo are \\textit{model-learned}:\n(a) \\textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;\n(d) \\textit{format-token dilution}---fine-tuned models assign extremely high LP to schema tokens (\\texttt{\\{\"entities\": [}~etc.) that carry no extraction information, diluting the signal from entity-name tokens; free-form parse rates of 99.95\\% confirm that format tokens dominate the sequence.\nThe constraint-imposed mechanisms (b)--(c) predict that free-form decoding should reduce compression; our NER ablation finds negligible change (std ratio 0.97; Appendix~\\ref{app:freeform_ablation}), suggesting the model-learned mechanisms (a) and (d) are the primary drivers for NER.\n\n\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nRemoving grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.\nRemoving format constraints restores LP selection for RE: bootstrap mean $+2.35$~pp (95\\% CI [$+0.24$, $+4.50$], $p{=}0.025$, $n{=}397$), though driven by magnitude asymmetry rather than instance-level win rate (sign test: 45W/45L/307T; Appendix~\\ref{app:re_extension}).\nMore generally, LP selection failures show cross-seed stability (Jaccard${=}0.42$; Appendix~\\ref{app:lp_failure_stability}), indicating a systematic rather than stochastic failure mode.\nVC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \\cite{eikema2022sampling, deguchi2024centroid}.\nMore broadly, all consensus-proximity strategies fail because instance degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Table~\\ref{tab:degeneracy}; Appendix~\\ref{app:mbr_discussion}).\n\n\\paragraph{Ablation: entity-token LP.}\nWe directly test hypothesis (d) by isolating entity-mention tokens from the log-probability computation.\nOn SciERC, entity-token LP exhibits $4{\\times}$ higher within-instance variance than full-sequence LP, confirming that format tokens do compress the signal.\nHowever, entity-token LP selection performs strictly \\textit{worse} than full-sequence LP on both datasets ($-2.0$~pp on SciERC, $-3.3$~pp on CoNLL).\nEntity tokens are either too sparse (5.3\\% of sequence tokens on SciERC) for stable estimation, or nearly saturated (79.4\\% of instances tied on CoNLL)---consistent with CoNLL's limited entity vocabulary (4 types, high-frequency names) that fine-tuning drives to near-deterministic prediction.\nThis rules out format-token dilution as the primary cause of LP's selection failure and instead points to an intrinsic pattern: fine-tuned models assign near-deterministic probabilities to entity-name tokens themselves, leaving minimal discriminative signal regardless of aggregation scope.\nEven disaggregating to entity-token logprobs fails to break compression: on CoNLL, 79.4\\% of sample pairs share identical entity-token LP, confirming that compression operates at the representation level rather than being diluted by non-entity tokens.\n\n\\paragraph{Pilot remedy.}\nEntity-token LP represents a natural pilot remedy: if format-token dilution caused compression, restricting LP to entity tokens should recover selection ability.\nIts failure---particularly the near-zero entity-token variance on CoNLL---suggests that effective remedies must address the underlying model confidence calibration rather than signal aggregation.\n\n\\paragraph{Practical considerations.}\nMulti-sample inference incurs $N{\\times}$ compute cost.\nFor quality estimation---where signals are already reliable ($\\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82)---$N{=}8$ samples suffice (Appendix~\\ref{app:n_scaling}), making the cost acceptable for selective prediction or error flagging in high-stakes IE.\nFor selection, the cost-benefit is unfavorable: $8{\\times}$ inference yields at most $+0.2$~pp over greedy ($p{>}0.05$).\nWhether the trade-off shifts in low-convergence regimes (e.g., under-parameterized models where degeneracy drops below 10\\%) remains an open question.\n\n\\paragraph{Regime boundaries.}\nThe correlation-selection gap for structural signals is persistent across all four datasets, but LP selection is degeneracy-gated.\nAt the \\textit{low-resource boundary} (WNUT-17, macro F1${\\approx}$42\\%), QE signals themselves become unreliable: full-set correlations are dominated by the zero/non-zero boundary (VC conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}), so selection is moot.\nAt the \\textit{ceiling boundary} (CoNLL, F1${\\approx}$91\\%, 58\\% degeneracy), selection shows only a marginal structural exception: VC achieves $+0.28$~pp ($p{<}0.03$) at $N{=}16$, capturing ${\\sim}$10\\% of the 2.5~pp oracle headroom (Appendix~\\ref{app:n_scaling}); LP fails entirely.\nIn the \\textit{moderate regime}, instance degeneracy determines LP effectiveness: at 21\\% degeneracy (SciERC), LP gains are positive but sub-significant ($+0.42$~pp, $p{=}0.091$); at 10\\% degeneracy (Few-NERD), LP achieves highly significant gains ($+1.36$~pp, $p{<}0.001$; Table~\\ref{tab:fewnerd}).\nThe cross-dataset gradient (58\\% $\\to$ fail, 21\\% $\\to$ weak, 10\\% $\\to$ strong; $n{=}3$ datasets) is consistent with degeneracy below ${\\sim}$15\\% being a necessary condition for LP selection; entity-type-level evidence provides stronger statistical grounding (Spearman $\\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$; Appendix~\\ref{app:per_type_lp}).\nWhen candidates differ sufficiently in quality, LP's per-sample signal can exploit the headroom.\nThe pattern persists at finer granularity: per-entity-type analysis on Few-NERD shows 7/8 types with positive LP gains, the sole exception being the highest-degeneracy type (Spearman $\\rho(\\text{degen}, \\text{headroom}){=}{-}0.881$, $p{=}0.004$; Appendix~\\ref{app:per_type_lp}).\nStructural signals fail uniformly regardless of degeneracy because they rank candidates by typicality, not quality.\nWhether these patterns persist on larger models (70B+) remains open.\n\n\\paragraph{Methodological implications.}\nThe decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.\nEven supervised combination of all five signals (logistic regression, MLP, random forest) fails to close the oracle gap (\\S\\ref{sec:robustness_main}), confirming the information bottleneck is in the features themselves, not the aggregation method.\nEffective selection thus requires content-aware verifiers that examine output semantics \\cite{cobbe2021verifiers, venktesh2025trust}, not confidence signal aggregation; $N{=}8$ captures most quality estimation benefit (Appendix~\\ref{app:n_scaling}).\nStructural signals are robust to domain shift when the training schema subsumes the target (Appendix~\\ref{app:ood}).\n",
      "numLines": 133,
      "startLine": 1,
      "totalLines": 133
    }
  },
  "sourceToolAssistantUUID": "76570da8-d27f-44d2-80fc-d3813fac75cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T07:07:52.488Z_

<details><summary>↩ Tool result · `toolu_019t5dwNa4f6gCHS3ePpveHe`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
27	\begin{equation}\label{eq:fk}
28	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
29	\end{equation}
30	where $\bar{P}$ is mean observed and $\bar{P}_e$ expected agreement.
31	Temperature-based sampling introduces mild negative dependence ($-$0.4\% to $-$4.0\%; Appendix~\ref{app:fk_independence}), which does not inflate FK.
32	Unlike structural signals, FK relies on exact string matching.
33	
34	\paragraph{Soft Jaccard (structural, instance-level).}
35	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:
36	\begin{equation}\label{eq:sj}
37	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
38	\end{equation}
39	where $M$ is the matched set, $\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\max(|g_i|, |g_j|)$ penalizes length asymmetry.\footnote{The denominator uses $\max(|g_i|, |g_j|)$ per type group rather than $|A \cup B|$, penalizing cardinality mismatches more heavily than standard Jaccard; the two variants produce nearly identical rankings ($\Delta\rho{<}0.01$; Table~\ref{tab:sj_normalizer}).}
40	The instance-level QE signal averages over all pairs:
41	\begin{equation}\label{eq:sj_instance}
42	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
43	\end{equation}
44	For selection, $c_{\text{sj}}(x)$ cannot rank individual candidates (it assigns one score per input).
45	Consensus-proximity converts it to a per-sample utility $u_{\text{sj}}(y_i) = \frac{1}{N-1} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, selecting the candidate most consistent with the sample pool---equivalent to minimum Bayes risk (MBR) decoding \cite{eikema2022sampling} with SJ as the utility function.
46	The same construction applies to FK, EM, and VC.
47	
48	\paragraph{Entity voting confidence (structural, instance-level).}
49	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
50	The instance-level confidence is the mean frequency:
51	\begin{equation}\label{eq:voting}
52	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
53	\end{equation}
54	When $E_\cup = \emptyset$, we set $c_{\mathrm{vc}}(x) = 0$.\footnote{Equation~\ref{eq:voting} defines the continuous QE signal; for voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}
55	
56	\subsection{Evaluation Framework}\label{sec:evaluation}
57	
58	\paragraph{Quality estimation.}
59	Spearman $\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.
60	Both quality estimation and selection exclude instances with no gold annotations: $n{=}529$ on SciERC (from 551), $n{=}2{,}756$ on CoNLL (from 3{,}453).\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\ref{app:additional}.}
61	
62	\paragraph{Sample selection.}
63	Best-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals rank via consensus-proximity (MBR utility; see SJ definition above).
64	Baselines: \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$ argmax decoding).
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4219b049-6ee3-4f95-9bfe-835a0a3d0e0c",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "ceac959f-9ccd-413b-8afd-5696f203eed3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven model $\\mathcal{M}$ and input $x$, we sample $N$ outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}, where each $y_i$ is an entity set.\nA \\textbf{per-sample signal} $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$ scores each output independently; an \\textbf{instance-level signal} $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$ produces a single score per input (notation in Appendix~\\ref{app:notation}).\nThis distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\\S\\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nFour are \\textit{consistency signals}: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]); log-probability [LP] is the sole \\textit{model-internal}, per-sample signal.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed and $\\bar{P}_e$ expected agreement.\nTemperature-based sampling introduces mild negative dependence ($-$0.4\\% to $-$4.0\\%; Appendix~\\ref{app:fk_independence}), which does not inflate FK.\nUnlike structural signals, FK relies on exact string matching.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set, $\\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\\max(|g_i|, |g_j|)$ penalizes length asymmetry.\\footnote{The denominator uses $\\max(|g_i|, |g_j|)$ per type group rather than $|A \\cup B|$, penalizing cardinality mismatches more heavily than standard Jaccard; the two variants produce nearly identical rankings ($\\Delta\\rho{<}0.01$; Table~\\ref{tab:sj_normalizer}).}\nThe instance-level QE signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\nFor selection, $c_{\\text{sj}}(x)$ cannot rank individual candidates (it assigns one score per input).\nConsensus-proximity converts it to a per-sample utility $u_{\\text{sj}}(y_i) = \\frac{1}{N-1} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, selecting the candidate most consistent with the sample pool---equivalent to minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling} with SJ as the utility function.\nThe same construction applies to FK, EM, and VC.\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$, we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{Equation~\\ref{eq:voting} defines the continuous QE signal; for voted-output \\textit{selection} (Table~\\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nSpearman $\\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.\nBoth quality estimation and selection exclude instances with no gold annotations: $n{=}529$ on SciERC (from 551), $n{=}2{,}756$ on CoNLL (from 3{,}453).\\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\\ref{app:additional}.}\n\n\\paragraph{Sample selection.}\nBest-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals rank via consensus-proximity (MBR utility; see SJ definition above).\nBaselines: \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$ argmax decoding).\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  },
  "sourceToolAssistantUUID": "4219b049-6ee3-4f95-9bfe-835a0a3d0e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T07:07:53.419Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QBZctthb2FzBFK4XoUPxgD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceac959f-9ccd-413b-8afd-5696f203eed3",
  "isSidechain": false,
  "requestId": "req_011Cb7igmkveLTfWBtFMC7o7",
  "type": "assistant",
  "uuid": "489e4591-4f5a-4c44-868d-7a36349a1ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118ipYWiM9Yz31Pm9yNtLsT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3916,
      "cache_read_input_tokens": 27128,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 325,
          "cache_read_input_tokens": 27128,
          "cache_creation_input_tokens": 3916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3916
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T07:07:53.445Z_

<details><summary>↩ Tool result · `toolu_01QBZctthb2FzBFK4XoUPxgD`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}
19	
20	%% ============================================================
21	\subsection{Quality Estimation Results}
22	\label{sec:qe_results}
23	
24	\begin{table*}[t]
25	\centering
26	\small
27	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
28	\label{tab:quality_estimation}
29	\begin{tabular}{ll cc cc cc}
30	\toprule
31	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
32	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
33	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
34	\midrule
35	VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
36	SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
37	FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
38	EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
39	\midrule
40	LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
41	\bottomrule
42	\end{tabular}
43	\end{table*}
44	
45	Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models.\footnote{$\varepsilon{=}0.05$ applies only to selection (\S\ref{sec:selection_gap}); quality estimation is $\varepsilon$-free. Selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}).}
46	
47	\paragraph{Signal rankings are difficulty-dependent.}
48	On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over surface ($\rho{\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
49	On CoNLL (ceiling-effect control, single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$); the $\rho$--AUROC dissociation across datasets reflects use-case alignment.
50	At the signal-collapse boundary---WNUT-17 (macro F1${\approx}$42\%, 52\% zero-F1 instances)---full-set correlations are dominated by the zero/non-zero boundary: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) but conditional $\rho$ drops to 0.038 (Table~\ref{tab:wnut}).
51	LP shows the reverse pattern (full-set $\rho{=}{-}0.410$, conditional $\rho{=}0.350$), confirming that full-set correlations conflate binary success prediction with quality gradation.
52	Restricting to non-zero instances reshuffles rankings, with EM strongest ($\rho{=}0.360$; Figure~\ref{fig:signal_heatmap}).
53	
54	\begin{table}[t]
55	\centering
56	\small
57	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
58	\label{tab:wnut}
59	\begin{tabular}{lcccc}
60	\toprule
61	Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
62	\midrule
63	VC      & .724 & .913 & .038 & .487 \\
64	FK      & .125 & .555 & .169 & .002 \\
65	SJ      & .089 & .517 & .288 & ${<}$1e-7 \\
66	EM      & .050 & .487 & .333 & ${<}$1e-9 \\
67	LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	%% ============================================================
73	\subsection{The Correlation-Selection Gap}
74	\label{sec:selection_gap}
75	
76	We define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.
77	
78	Our argument proceeds in three layers.
79	First, four of five signals (SJ, FK, EM, VC) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; they \textit{cannot} rank candidates within an instance by construction, and consensus-proximity (MBR) conversion does not reliably recover per-sample ranking.
80	Second, MBR selection with well-aligned utility (within-instance SJ--F1 $\rho{=}0.52$) should in principle select better outputs, but instance degeneracy collapses the candidate pool, eliminating the headroom MBR would otherwise exploit.
81	Third, LP, the sole natively per-sample signal, provides genuine ranking information but suffers from extreme compression (median within-instance range 0.041 nats), limiting its discriminative power except in low-degeneracy regimes.
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$, $p$ vs.\ greedy baseline from paired sign tests). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Random: uniform random selection from $N$ candidates. Non-tied LP subset analysis in \S\ref{sec:discussion}; RE selection in Appendix~\ref{app:re_extension}.}
87	\label{tab:selection}
88	\begin{tabular}{lcc}
89	\toprule
90	Method & NER F1 & $p$ \\
91	\midrule
92	Oracle & $0.778 \pm 0.003$ & --- \\
93	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
94	\midrule
95	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
96	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
97	\midrule
98	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
99	SJ           & $0.646 \pm 0.002$ & .67 \\
100	FK           & $0.646 \pm 0.001$ & .79 \\
101	EM           & $0.637 \pm 0.001$ & --- \\
102	VC           & $0.623 \pm 0.004$ & --- \\
103	\midrule
104	Random           & $0.610 \pm 0.003$ & --- \\
105	\bottomrule
106	\end{tabular}
107	\end{table}
108	
109	Despite moderate quality estimation, confidence signals yield limited selection gains (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
110	The 3.5~pp gap between greedy (0.645) and random selection (0.610) reflects the difference between deterministic decoding ($T{=}0$) and uniformly sampling one of $N$ stochastic candidates ($T{=}1.0$); greedy is not drawn from the candidate pool.
111	Instance-level signals (SJ, FK, EM, VC) assign identical QE scores to all candidates per input; consensus-proximity (MBR) converts these to per-sample rankings (Table~\ref{tab:selection}: SJ 0.646, FK 0.646, EM 0.637, VC 0.623), but none consistently improves over the greedy baseline on the primary test bed.
112	The key question is whether LP---the only natively per-sample signal---can exploit the oracle headroom.
113	
114	\paragraph{No significant improvement over greedy.}
115	On SciERC NER (2-seed sign tests\footnote{Multi-seed NER experiments confirm seed variation is small ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}).}, $n{=}529$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\Delta{=}{+}0.2$~pp, $d{=}0.038$, $p{=}0.29$); the observed LP advantage is small and not reliably detected at $N{=}8$ (absence of evidence should not be equated with evidence of absence; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\ref{app:tost}).
116	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); RE selection results are consistent (Appendix~\ref{app:re_extension}).
117	With $N{=}16$, LP selection on SciERC yields a paired improvement of $+0.52$~pp (bootstrap $p{=}0.003$), suggesting the signal becomes actionable at larger candidate pools where degeneracy drops and headroom expands.
118	Few-NERD provides a stronger demonstration: LP achieves significant gains ($+1.36$~pp, $p{<}0.001$) at low degeneracy, while structural signals still fail (\S\ref{sec:fewnerd}).
119	CoNLL's near-ceiling single-sample F1 (0.91) with only ${\sim}$4~pp oracle headroom functions primarily as a ceiling-effect control.
120	Under stringent external TOST anchors ($\delta_0{=}1.0$~pp), some configurations (e.g., Qwen CoNLL) show statistically significant degradation (0.9--1.5~pp below greedy), indicating that signal-based selection can be actively harmful rather than merely ineffective (Appendix~\ref{app:tost}).
121	LP approximately matches greedy decoding ($T{=}0$; $\Delta{=}{+}0.2$~pp, not significant); neither significantly outperforms the other, yet both fall far short of the oracle (0.778, 13.3~pp gap).
122	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021verifiers}.\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}
123	
124	%% ============================================================
125	\subsection{Cross-Dataset Contrast: Few-NERD}
126	\label{sec:fewnerd}
127	
128	\begin{table}[t]
129	\centering
130	\small
131	\caption{Cross-dataset comparison of LP selection effectiveness (Qwen3-8B, $N{=}8$, $T{=}1.0$). LP selection gains are inversely associated with instance degeneracy across three datasets. Few-NERD uses gold-filtered evaluation ($n{=}32{,}565$); SciERC uses full test set ($n{=}551$) for protocol consistency.\protect\footnotemark}
132	\label{tab:fewnerd}
133	\begin{tabular}{lcccccc}
134	\toprule
135	Dataset & $n$ & Greedy & Headroom & Degen\% & LP $\rho$ & LP $\Delta$ \\
136	\midrule
137	CoNLL & 2{,}756 & .908 & 4.0\,pp & 58\% & .316 & fail \\
138	SciERC & 551 & .614 & 13.8\,pp & 21\% & .205 & $+$0.42\,pp \\
139	Few-NERD & 32{,}565 & .748 & 12.4\,pp & 10.1\% & .421 & $\mathbf{+1.36}$\,pp \\
140	\bottomrule
141	\end{tabular}
142	\end{table}
143	\footnotetext{SciERC greedy (0.614) and headroom (13.8~pp) differ from Table~\ref{tab:selection} (gold-filtered $n{=}529$, greedy${=}0.645$) due to full-set evaluation; the ranking and significance are unchanged.}
144	
145	Few-NERD (Table~\ref{tab:fewnerd}) reveals that LP selection effectiveness is inversely associated with instance degeneracy across datasets.
146	At 10.1\% degeneracy (vs.\ SciERC's 21\%, CoNLL's 58\%), LP achieves highly significant selection gains ($+1.36$~pp, 95\% CI $[+1.18, +1.53]$, $p{<}0.001$), while all other signals degrade selection (VC $-1.79$, SJ $-2.14$, FK $-2.26$, EM $-3.85$~pp).
147	
148	\paragraph{Degeneracy as a necessary condition.}
149	Low degeneracy is necessary for LP selection: the cross-dataset gradient is monotonic (58\% $\to$ fail, 21\% $\to$ $+0.42$~pp, 10\% $\to$ $+1.36$~pp), and degeneracy below ${\sim}$15\% consistently enables positive LP gains (Figure~\ref{fig:degeneracy_scatter}).
150	However, within a dataset, LP signal quality ($\rho$) provides an additional prerequisite: per-type analysis shows that low degeneracy alone does not guarantee gains (Appendix~\ref{app:per_type_lp}).
151	The LoRA-rank ablation (\S\ref{sec:robustness_main}) corroborates this interaction: reducing rank lowers SciERC degeneracy from 21\% to 7\% and increases oracle headroom, though LP selection still fails there, confirming that degeneracy is necessary but not sufficient.
152	
153	\paragraph{The correlation-selection gap persists for structural signals.}
154	All five signals achieve positive quality estimation on Few-NERD (LP $\rho{=}0.42$, VC $0.39$, FK $0.31$, SJ $0.30$, EM $0.29$), yet only LP translates QE into selection.
155	The gap between VC's quality estimation ($\rho{=}0.39$) and its selection outcome ($-1.79$~pp) confirms that the gap is not an artifact of weak QE: even strong instance-level QE signals cannot rank candidates within an instance.
156	Within Few-NERD, the degeneracy-gating pattern holds at entity-type granularity: 7 of 8 types show positive LP selection gains ($+0.23$ to $+4.73$~pp), while the highest-degeneracy type (Art, 19.8\%) is the sole exception (Appendix~\ref{app:per_type_lp}).
157	
158	\begin{figure}[t]
159	\centering
160	\includegraphics[width=\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}
161	\caption{Instance degeneracy vs.\ LP selection gain. Blue circles: cross-dataset aggregates (CoNLL, SciERC, Few-NERD); orange triangles: per-entity-type within Few-NERD. The dashed line at ${\sim}$15\% separates a regime where LP selection improves over greedy (left) from one where it fails (right). Cross-dataset ordering is monotonic; 7/8 Few-NERD entity types below 20\% degeneracy show positive gains. Degeneracy below ${\sim}$15\% appears necessary for LP selection to succeed (Spearman $\rho{=}{-}0.57$, $p{=}0.066$, $n{=}11$).}
162	\label{fig:degeneracy_scatter}
163	\end{figure}
164	
165	Figure~\ref{fig:degeneracy_scatter} visualizes the relationship across both dataset-level and entity-type-level granularity: degeneracy below ${\sim}$15\% appears necessary for LP selection gains.
166	The pooled Spearman correlation ($\rho{=}{-}0.57$, $p{=}0.066$, $n{=}11$) treats dataset-level and entity-type-level points as independent; the entity-type-level evidence alone provides stronger grounding ($\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$).
167	
168	\paragraph{LP selection scales with sample budget in the low-degeneracy regime.}
169	On the same 4{,}351 Few-NERD instances, doubling $N$ from 8 to 16 yields a significant additional $+0.52$~pp (paired bootstrap $p{=}0.003$, 95\% CI $[+0.17, +0.87]$): LP selection improves from $+1.37$~pp to $+1.88$~pp (both $p{<}0.001$).
170	The gain is driven by reduced degeneracy (11.1\% $\to$ 4.5\%) expanding oracle headroom (12.1 $\to$ 15.4~pp), while LP ranking quality remains stable ($\rho{\approx}0.62$), confirming that signal quality is model-intrinsic rather than $N$-dependent.
171	At $N{=}16$, all 8 entity types show positive LP gains, including types that were negative at $N{=}8$.
172	Structural signals remain uniformly negative at $N{=}16$ (SJ $-1.36$, FK $-1.47$~pp), reinforcing that the correlation-selection gap for consensus-based methods persists regardless of sample budget.
173	
174	%% ============================================================
175	\subsection{Robustness}
176	\label{sec:robustness_main}
177	
178	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$).
179	Signal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$, though statistical precision is limited with $m{=}3$ raters, exact $p{\approx}0.028$; Table~\ref{tab:ranking-stability}).
180	NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
181	
182	\begin{table}[t]
183	\centering
184	\small
185	\caption{Scale ablation: Qwen3-8B vs.\ 4B NER quality estimation ($\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\ref{app:re_extension}.}
186	\label{tab:scale_ablation}
187	\begin{tabular}{@{}ll cc r@{}}
188	\toprule
189	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
190	\midrule
191	CoNLL & SJ & .436 & .422 & $-$.014 \\
192	      & FK & .400 & .418 & $+$.018 \\
193	SciERC & SJ & .360 & .422 & $+$.062 \\
194	       & FK & .267 & .326 & $+$.059 \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\paragraph{Scale robustness.}
200	Repeating with Qwen3-4B (Table~\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy on SciERC ($\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty is a stronger predictor of the gap than model scale; results hold at smaller scale (LLaMA-3.2-3B, 13.6~pp headroom; Appendix~\ref{app:llama3b}).
201	Instance degeneracy also scales with model capability: 8B shows twice the degeneracy of 4B on SciERC (21\% vs.\ 10.4\%) despite comparable within-instance utility correlation (Table~\ref{tab:degeneracy}).
202	
203	\paragraph{LoRA-rank ablation.}
204	To disentangle model capacity from degeneracy, we train Qwen3-8B on SciERC with LoRA rank${=}8$ (vs.\ rank${=}32$ in all other experiments).
205	Reducing rank lowers degeneracy from 21\% to 7.2\% and increases oracle headroom from 13.3~pp to 16.0~pp, confirming that fine-tuning capacity drives output convergence.
206	However, selection still fails: the best signal (LP, 0.635) falls short of greedy (0.640), and all consensus-proximity signals perform worse (SJ 0.631, VC 0.592).
207	Quality estimation remains comparable (VC $\rho{=}0.394$ vs.\ $0.379$; SJ $\rho{=}0.365$ vs.\ $0.360$).
208	Low degeneracy is thus a necessary but not sufficient condition for selection---LP compression persists regardless of LoRA rank, indicating that both mechanisms must be addressed simultaneously.
209	
210	\paragraph{Supervised verifier baseline.}
211	To test whether the information bottleneck lies in the aggregation method or the features themselves, we train a logistic regression verifier on all five signals (3-fold cross-validation on SciERC, $N{=}16$---giving the verifier access to twice as many samples as the main results).
212	The supervised selector achieves F1${=}0.641$, below both LP (0.647) and greedy (0.644),\footnote{Greedy F1 is 0.644 (3-seed mean in the verifier experiment), consistent with Table~\ref{tab:selection} (0.645, 2-seed mean on the gold-filtered subset).} closing none of the oracle gap despite the additional samples.
213	Its AUROC (0.652) is lower than single-signal VC (0.706), and feature importance is dominated by VC (coefficient 0.65--0.92) with SJ receiving a negative coefficient.
214	A 2-layer MLP and random forest on the same five features achieve comparable or slightly worse performance (MLP AUROC: 0.639; RF: 0.604), confirming that the bottleneck lies in the feature space rather than the aggregation model.
215	The failure of supervised signal combination confirms that the bottleneck is not in how signals are aggregated but in what information they encode: these features lack per-sample discriminative content sufficient for selection.
216	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "489e4591-4f5a-4c44-868d-7a36349a1ae5",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "c3071cfe-5974-4e39-98db-a26acb788a28",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures.\nQwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\\ref{app:n_scaling}).}\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models.\\footnote{$\\varepsilon{=}0.05$ applies only to selection (\\S\\ref{sec:selection_gap}); quality estimation is $\\varepsilon$-free. Selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}).}\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over surface ($\\rho{\\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (ceiling-effect control, single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$); the $\\rho$--AUROC dissociation across datasets reflects use-case alignment.\nAt the signal-collapse boundary---WNUT-17 (macro F1${\\approx}$42\\%, 52\\% zero-F1 instances)---full-set correlations are dominated by the zero/non-zero boundary: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) but conditional $\\rho$ drops to 0.038 (Table~\\ref{tab:wnut}).\nLP shows the reverse pattern (full-set $\\rho{=}{-}0.410$, conditional $\\rho{=}0.350$), confirming that full-set correlations conflate binary success prediction with quality gradation.\nRestricting to non-zero instances reshuffles rankings, with EM strongest ($\\rho{=}0.360$; Figure~\\ref{fig:signal_heatmap}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\n\\label{tab:wnut}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & .913 & .038 & .487 \\\\\nFK      & .125 & .555 & .169 & .002 \\\\\nSJ      & .089 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nWe define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.\n\nOur argument proceeds in three layers.\nFirst, four of five signals (SJ, FK, EM, VC) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; they \\textit{cannot} rank candidates within an instance by construction, and consensus-proximity (MBR) conversion does not reliably recover per-sample ranking.\nSecond, MBR selection with well-aligned utility (within-instance SJ--F1 $\\rho{=}0.52$) should in principle select better outputs, but instance degeneracy collapses the candidate pool, eliminating the headroom MBR would otherwise exploit.\nThird, LP, the sole natively per-sample signal, provides genuine ranking information but suffers from extreme compression (median within-instance range 0.041 nats), limiting its discriminative power except in low-degeneracy regimes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$, $p$ vs.\\ greedy baseline from paired sign tests). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Random: uniform random selection from $N$ candidates. Non-tied LP subset analysis in \\S\\ref{sec:discussion}; RE selection in Appendix~\\ref{app:re_extension}.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.778 \\pm 0.003$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & --- \\\\\nVC           & $0.623 \\pm 0.004$ & --- \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite moderate quality estimation, confidence signals yield limited selection gains (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nThe 3.5~pp gap between greedy (0.645) and random selection (0.610) reflects the difference between deterministic decoding ($T{=}0$) and uniformly sampling one of $N$ stochastic candidates ($T{=}1.0$); greedy is not drawn from the candidate pool.\nInstance-level signals (SJ, FK, EM, VC) assign identical QE scores to all candidates per input; consensus-proximity (MBR) converts these to per-sample rankings (Table~\\ref{tab:selection}: SJ 0.646, FK 0.646, EM 0.637, VC 0.623), but none consistently improves over the greedy baseline on the primary test bed.\nThe key question is whether LP---the only natively per-sample signal---can exploit the oracle headroom.\n\n\\paragraph{No significant improvement over greedy.}\nOn SciERC NER (2-seed sign tests\\footnote{Multi-seed NER experiments confirm seed variation is small ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}).}, $n{=}529$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\\Delta{=}{+}0.2$~pp, $d{=}0.038$, $p{=}0.29$); the observed LP advantage is small and not reliably detected at $N{=}8$ (absence of evidence should not be equated with evidence of absence; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\\ref{app:tost}).\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); RE selection results are consistent (Appendix~\\ref{app:re_extension}).\nWith $N{=}16$, LP selection on SciERC yields a paired improvement of $+0.52$~pp (bootstrap $p{=}0.003$), suggesting the signal becomes actionable at larger candidate pools where degeneracy drops and headroom expands.\nFew-NERD provides a stronger demonstration: LP achieves significant gains ($+1.36$~pp, $p{<}0.001$) at low degeneracy, while structural signals still fail (\\S\\ref{sec:fewnerd}).\nCoNLL's near-ceiling single-sample F1 (0.91) with only ${\\sim}$4~pp oracle headroom functions primarily as a ceiling-effect control.\nUnder stringent external TOST anchors ($\\delta_0{=}1.0$~pp), some configurations (e.g., Qwen CoNLL) show statistically significant degradation (0.9--1.5~pp below greedy), indicating that signal-based selection can be actively harmful rather than merely ineffective (Appendix~\\ref{app:tost}).\nLP approximately matches greedy decoding ($T{=}0$; $\\Delta{=}{+}0.2$~pp, not significant); neither significantly outperforms the other, yet both fall far short of the oracle (0.778, 13.3~pp gap).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; closing this gap likely requires trained verifiers \\cite{cobbe2021verifiers}.\\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset comparison of LP selection effectiveness (Qwen3-8B, $N{=}8$, $T{=}1.0$). LP selection gains are inversely associated with instance degeneracy across three datasets. Few-NERD uses gold-filtered evaluation ($n{=}32{,}565$); SciERC uses full test set ($n{=}551$) for protocol consistency.\\protect\\footnotemark}\n\\label{tab:fewnerd}\n\\begin{tabular}{lcccccc}\n\\toprule\nDataset & $n$ & Greedy & Headroom & Degen\\% & LP $\\rho$ & LP $\\Delta$ \\\\\n\\midrule\nCoNLL & 2{,}756 & .908 & 4.0\\,pp & 58\\% & .316 & fail \\\\\nSciERC & 551 & .614 & 13.8\\,pp & 21\\% & .205 & $+$0.42\\,pp \\\\\nFew-NERD & 32{,}565 & .748 & 12.4\\,pp & 10.1\\% & .421 & $\\mathbf{+1.36}$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\footnotetext{SciERC greedy (0.614) and headroom (13.8~pp) differ from Table~\\ref{tab:selection} (gold-filtered $n{=}529$, greedy${=}0.645$) due to full-set evaluation; the ranking and significance are unchanged.}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) reveals that LP selection effectiveness is inversely associated with instance degeneracy across datasets.\nAt 10.1\\% degeneracy (vs.\\ SciERC's 21\\%, CoNLL's 58\\%), LP achieves highly significant selection gains ($+1.36$~pp, 95\\% CI $[+1.18, +1.53]$, $p{<}0.001$), while all other signals degrade selection (VC $-1.79$, SJ $-2.14$, FK $-2.26$, EM $-3.85$~pp).\n\n\\paragraph{Degeneracy as a necessary condition.}\nLow degeneracy is necessary for LP selection: the cross-dataset gradient is monotonic (58\\% $\\to$ fail, 21\\% $\\to$ $+0.42$~pp, 10\\% $\\to$ $+1.36$~pp), and degeneracy below ${\\sim}$15\\% consistently enables positive LP gains (Figure~\\ref{fig:degeneracy_scatter}).\nHowever, within a dataset, LP signal quality ($\\rho$) provides an additional prerequisite: per-type analysis shows that low degeneracy alone does not guarantee gains (Appendix~\\ref{app:per_type_lp}).\nThe LoRA-rank ablation (\\S\\ref{sec:robustness_main}) corroborates this interaction: reducing rank lowers SciERC degeneracy from 21\\% to 7\\% and increases oracle headroom, though LP selection still fails there, confirming that degeneracy is necessary but not sufficient.\n\n\\paragraph{The correlation-selection gap persists for structural signals.}\nAll five signals achieve positive quality estimation on Few-NERD (LP $\\rho{=}0.42$, VC $0.39$, FK $0.31$, SJ $0.30$, EM $0.29$), yet only LP translates QE into selection.\nThe gap between VC's quality estimation ($\\rho{=}0.39$) and its selection outcome ($-1.79$~pp) confirms that the gap is not an artifact of weak QE: even strong instance-level QE signals cannot rank candidates within an instance.\nWithin Few-NERD, the degeneracy-gating pattern holds at entity-type granularity: 7 of 8 types show positive LP selection gains ($+0.23$ to $+4.73$~pp), while the highest-degeneracy type (Art, 19.8\\%) is the sole exception (Appendix~\\ref{app:per_type_lp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain. Blue circles: cross-dataset aggregates (CoNLL, SciERC, Few-NERD); orange triangles: per-entity-type within Few-NERD. The dashed line at ${\\sim}$15\\% separates a regime where LP selection improves over greedy (left) from one where it fails (right). Cross-dataset ordering is monotonic; 7/8 Few-NERD entity types below 20\\% degeneracy show positive gains. Degeneracy below ${\\sim}$15\\% appears necessary for LP selection to succeed (Spearman $\\rho{=}{-}0.57$, $p{=}0.066$, $n{=}11$).}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nFigure~\\ref{fig:degeneracy_scatter} visualizes the relationship across both dataset-level and entity-type-level granularity: degeneracy below ${\\sim}$15\\% appears necessary for LP selection gains.\nThe pooled Spearman correlation ($\\rho{=}{-}0.57$, $p{=}0.066$, $n{=}11$) treats dataset-level and entity-type-level points as independent; the entity-type-level evidence alone provides stronger grounding ($\\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$).\n\n\\paragraph{LP selection scales with sample budget in the low-degeneracy regime.}\nOn the same 4{,}351 Few-NERD instances, doubling $N$ from 8 to 16 yields a significant additional $+0.52$~pp (paired bootstrap $p{=}0.003$, 95\\% CI $[+0.17, +0.87]$): LP selection improves from $+1.37$~pp to $+1.88$~pp (both $p{<}0.001$).\nThe gain is driven by reduced degeneracy (11.1\\% $\\to$ 4.5\\%) expanding oracle headroom (12.1 $\\to$ 15.4~pp), while LP ranking quality remains stable ($\\rho{\\approx}0.62$), confirming that signal quality is model-intrinsic rather than $N$-dependent.\nAt $N{=}16$, all 8 entity types show positive LP gains, including types that were negative at $N{=}8$.\nStructural signals remain uniformly negative at $N{=}16$ (SJ $-1.36$, FK $-1.47$~pp), reinforcing that the correlation-selection gap for consensus-based methods persists regardless of sample budget.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\\Delta\\rho{=}{+}0.044$).\nSignal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$, though statistical precision is limited with $m{=}3$ raters, exact $p{\\approx}0.028$; Table~\\ref{tab:ranking-stability}).\nNER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3-8B vs.\\ 4B NER quality estimation ($\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nRepeating with Qwen3-4B (Table~\\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy on SciERC ($\\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty is a stronger predictor of the gap than model scale; results hold at smaller scale (LLaMA-3.2-3B, 13.6~pp headroom; Appendix~\\ref{app:llama3b}).\nInstance degeneracy also scales with model capability: 8B shows twice the degeneracy of 4B on SciERC (21\\% vs.\\ 10.4\\%) despite comparable within-instance utility correlation (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nTo disentangle model capacity from degeneracy, we train Qwen3-8B on SciERC with LoRA rank${=}8$ (vs.\\ rank${=}32$ in all other experiments).\nReducing rank lowers degeneracy from 21\\% to 7.2\\% and increases oracle headroom from 13.3~pp to 16.0~pp, confirming that fine-tuning capacity drives output convergence.\nHowever, selection still fails: the best signal (LP, 0.635) falls short of greedy (0.640), and all consensus-proximity signals perform worse (SJ 0.631, VC 0.592).\nQuality estimation remains comparable (VC $\\rho{=}0.394$ vs.\\ $0.379$; SJ $\\rho{=}0.365$ vs.\\ $0.360$).\nLow degeneracy is thus a necessary but not sufficient condition for selection---LP compression persists regardless of LoRA rank, indicating that both mechanisms must be addressed simultaneously.\n\n\\paragraph{Supervised verifier baseline.}\nTo test whether the information bottleneck lies in the aggregation method or the features themselves, we train a logistic regression verifier on all five signals (3-fold cross-validation on SciERC, $N{=}16$---giving the verifier access to twice as many samples as the main results).\nThe supervised selector achieves F1${=}0.641$, below both LP (0.647) and greedy (0.644),\\footnote{Greedy F1 is 0.644 (3-seed mean in the verifier experiment), consistent with Table~\\ref{tab:selection} (0.645, 2-seed mean on the gold-filtered subset).} closing none of the oracle gap despite the additional samples.\nIts AUROC (0.652) is lower than single-signal VC (0.706), and feature importance is dominated by VC (coefficient 0.65--0.92) with SJ receiving a negative coefficient.\nA 2-layer MLP and random forest on the same five features achieve comparable or slightly worse performance (MLP AUROC: 0.639; RF: 0.604), confirming that the bottleneck lies in the feature space rather than the aggregation model.\nThe failure of supervised signal combination confirms that the bottleneck is not in how signals are aggregated but in what information they encode: these features lack per-sample discriminative content sufficient for selection.\n",
      "numLines": 216,
      "startLine": 1,
      "totalLines": 216
    }
  },
  "sourceToolAssistantUUID": "489e4591-4f5a-4c44-868d-7a36349a1ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T07:07:53.645Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W3ib2pRXQxe6BQzcgqgAhR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3071cfe-5974-4e39-98db-a26acb788a28",
  "isSidechain": false,
  "requestId": "req_011Cb7igmkveLTfWBtFMC7o7",
  "type": "assistant",
  "uuid": "76570da8-d27f-44d2-80fc-d3813fac75cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118ipYWiM9Yz31Pm9yNtLsT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3916,
      "cache_read_input_tokens": 27128,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 325,
          "cache_read_input_tokens": 27128,
          "cache_creation_input_tokens": 3916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3916
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验设计**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics/Ref…",
  "leafUuid": "a85e9fc2-c365-488a-b0ed-db713fe6f53a",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Tool result

_source line 30 · 2026-05-17T07:08:00.030Z_

<details><summary>↩ Tool result · `toolu_013RGbSui4mtGLbUuu8K61Uj`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's what I found regarding ACL ARR 2025/2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Scores

For the overall recommendation score, the options are: 5 = Consider for Award (for papers that could be considered for an outstanding paper award at an *ACL conference, up to top 2.5% papers); 2 = Resubmit next cycle (for papers needing substantial revisions that can be completed by the next ARR cycle); 1.5 = Resubmit after next cycle (for papers needing substantial revisions that cannot be completed by the next ARR cycle); and 1 = Do not resubmit (for papers that have to be fully redone or are not relevant to the *ACL community).

## Review Form Questions

The review form includes evaluation of several key aspects:
- Whether authors have adequately discussed limitations and potential positive and negative societal impacts of their work, with constructive suggestions for improvement if not.
- Whether there is enough information in the paper for readers to reproduce main results or build upon the work.
- Ethical concerns in accordance with the ACL code of ethics

## General Review Guidance

ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference, and low scores may indicate the submission is not a good fit for ACL, even if it may be a good fit for other/more specialized venues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4efa4c87-c71c-4aef-b25d-92b1b0eab2bd",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "8939dc50-767b-467b-ab9b-abe027435e7c",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FFkZvCHJd4HCWNSmmXgTom",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "ACLRollingReview (@ReviewAcl) / X",
            "url": "https://x.com/reviewacl"
          },
          {
            "title": "aclrollingreview/reviewing.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"
          }
        ]
      },
      "Based on the search results, here's what I found regarding ACL ARR 2025/2026 reviewer guidelines, review form criteria, and scoring:\n\n## Review Scoring Criteria\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Scores\n\nFor the overall recommendation score, the options are: 5 = Consider for Award (for papers that could be considered for an outstanding paper award at an *ACL conference, up to top 2.5% papers); 2 = Resubmit next cycle (for papers needing substantial revisions that can be completed by the next ARR cycle); 1.5 = Resubmit after next cycle (for papers needing substantial revisions that cannot be completed by the next ARR cycle); and 1 = Do not resubmit (for papers that have to be fully redone or are not relevant to the *ACL community).\n\n## Review Form Questions\n\nThe review form includes evaluation of several key aspects:\n- Whether authors have adequately discussed limitations and potential positive and negative societal impacts of their work, with constructive suggestions for improvement if not.\n- Whether there is enough information in the paper for readers to reproduce main results or build upon the work.\n- Ethical concerns in accordance with the ACL code of ethics\n\n## General Review Guidance\n\nARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference, and low scores may indicate the submission is not a good fit for ACL, even if it may be a good fit for other/more specialized venues."
    ],
    "durationSeconds": 7.857051974000002
  },
  "sourceToolAssistantUUID": "4efa4c87-c71c-4aef-b25d-92b1b0eab2bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T07:08:05.345Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the remaining sections and also get the full ARR review form details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8939dc50-767b-467b-ab9b-abe027435e7c",
  "isSidechain": false,
  "requestId": "req_011Cb7ihg1vMujYmfrdqRJtG",
  "type": "assistant",
  "uuid": "6895570e-6311-4e91-be5c-f50973e986cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196GSEsN4gfffy6h1ChwDup",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 14730,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 31044,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 14730,
          "output_tokens": 369,
          "cache_read_input_tokens": 31044,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-17T07:08:05.863Z_

继续读取剩余章节和 ARR review form 详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6895570e-6311-4e91-be5c-f50973e986cd",
  "isSidechain": false,
  "requestId": "req_011Cb7ihg1vMujYmfrdqRJtG",
  "type": "assistant",
  "uuid": "1c3bd1d2-e87c-44c4-a5ef-2fe948eb18fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196GSEsN4gfffy6h1ChwDup",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 14730,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 31044,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 14730,
          "output_tokens": 369,
          "cache_read_input_tokens": 31044,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T07:08:08.289Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FyAASgcvm3EkW7rZEuyTrU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c3bd1d2-e87c-44c4-a5ef-2fe948eb18fc",
  "isSidechain": false,
  "requestId": "req_011Cb7ihg1vMujYmfrdqRJtG",
  "type": "assistant",
  "uuid": "e1b00e1c-048d-40a1-ab02-57ffcebcfe88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196GSEsN4gfffy6h1ChwDup",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 14730,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 31044,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 14730,
          "output_tokens": 369,
          "cache_read_input_tokens": 31044,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T07:08:08.296Z_

<details><summary>↩ Tool result · `toolu_01FyAASgcvm3EkW7rZEuyTrU`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement signals that assume equivalence can be determined via exact match or semantic similarity.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} demonstrate that consistency correlates with accuracy for LLM-based NER/RE under hard-prompting.
11	We show this correlation is necessary but not sufficient for sample selection, and diagnose two specific failure mechanisms (degeneracy, compression) that explain why correlation does not translate to selection gains.
12	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, where instance degeneracy is most pronounced.
13	Degeneracy varies across datasets: CoNLL (91\% single-sample F1) exhibits 58\%; SciERC (66\%) shows 21\%; Few-NERD (75\%) shows 10\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero (\S\ref{sec:discussion}).
14	Few-NERD's low degeneracy despite high performance reveals that dataset-specific factors modulate degeneracy beyond model capability alone.
15	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction; our supervised verifier baseline (logistic regression on all five signals, no oracle gap closure; \S\ref{sec:robustness_main}) suggests that the combination strategy itself is not the bottleneck.
16	\citet{culotta2004confidence} and \citet{mejer2010confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; \citet{fomicheva2020unsupervised} systematically apply model-internal signals (MC Dropout, D-Lex) for unsupervised quality estimation in NMT, establishing the paradigm we extend from sequence-level to set-valued structured outputs.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, park2024grammar}; recent work highlights hidden costs of constrained generation for log-probability estimation \cite{schall2025hidden} and inference efficiency \cite{yun2025price}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} study predictive uncertainty for autoregressive structured prediction.
22	Our structural signals instead measure agreement over output \textit{structure}, requiring no model modification.
23	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid} with structural utility functions.
24	Unlike machine translation where MBR yields consistent gains \cite{freitag2022high}, we find that utility \textit{is} aligned with quality (within-instance SJ--F1 $\rho{=}0.52$) but instance degeneracy eliminates the headroom MBR would otherwise exploit.
25	\citet{eikema2025structured} find that standard MBR utilities degrade on structured outputs due to bag-of-unit mismatches.
26	Our diagnosis is complementary but distinct: even when utility \textit{is} well-aligned with quality (within-instance $\rho{=}0.52$), output degeneracy eliminates the headroom MBR needs to improve over greedy.
27	NER's discrete label space produces more extreme degeneracy (up to 58\%) than the partial-overlap regime typical in MT and summarization (\S\ref{sec:discussion}).
28	\citet{xie2024selfevaluation} show self-evaluation improves selective generation for discrete tasks; our results suggest this does not transfer to structured extraction without learned scoring.
29	Our quality estimation results connect to selective prediction \cite{kuleshov2015calibrated}: signals with $\rho$ up to 0.45 on CoNLL (0.38 on the primary test bed, 0.42 on Few-NERD) and AUROC up to 0.82 can support abstention policies that flag low-quality extractions, providing practical value independent of sample selection.
30	Conformal prediction constructs prediction sets with coverage guarantees \cite{zhang2025conformal}; while complementary, its set-valued output differs from best-of-$N$ selection.
31	
32	\paragraph{Best-of-$N$ with learned verifiers.}
33	\citet{gao2023scaling} establish scaling laws for best-of-$N$ selection with learned reward models, showing that BoN performance scales log-linearly with $N$ but eventually degrades due to reward overoptimization.
34	Our unsupervised signals face a more fundamental limitation: they cannot rank candidates at all (instance-level signals) or rank them too weakly (LP compression), making the overoptimization regime irrelevant.
35	Trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and quality-aware decoding \cite{fernandes2022quality} learn per-sample scoring that may bridge this gap; our LoRA-rank ablation (degeneracy 7\% vs.\ 21\%, selection still fails) suggests that verifier training is necessary beyond merely increasing output diversity.
36	Fine-tuning itself contributes to the problem: \citet{kirk2024understanding} document diversity collapse in RLHF-trained models; our instance degeneracy is an analogous phenomenon in supervised fine-tuning, where stronger models converge to more uniform outputs.
37	Nucleus sampling \cite{holtzman2020curious} improves diversity in open-ended generation, but our constrained structured outputs limit the diversity that temperature scaling alone can recover.
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1b00e1c-048d-40a1-ab02-57ffcebcfe88",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "59488069-8ee8-4c66-b0db-d03fd226aab5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency \\cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \\cite{chen2024usc}, sub-claim decomposition \\cite{thirukovalluru2024atomic}, or hallucination detection \\cite{manakul2023selfcheckgpt}.\nTest-time scaling studies \\cite{snell2025scaling, brown2024monkeys} and reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement signals that assume equivalence can be determined via exact match or semantic similarity.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings; \\citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} demonstrate that consistency correlates with accuracy for LLM-based NER/RE under hard-prompting.\nWe show this correlation is necessary but not sufficient for sample selection, and diagnose two specific failure mechanisms (degeneracy, compression) that explain why correlation does not translate to selection gains.\nOur experiments use fine-tuned models, the dominant deployment paradigm for production NER, where instance degeneracy is most pronounced.\nDegeneracy varies across datasets: CoNLL (91\\% single-sample F1) exhibits 58\\%; SciERC (66\\%) shows 21\\%; Few-NERD (75\\%) shows 10\\%; WNUT-17 (${\\approx}$42\\%, macro) shows near-zero (\\S\\ref{sec:discussion}).\nFew-NERD's low degeneracy despite high performance reveals that dataset-specific factors modulate degeneracy beyond model capability alone.\nCoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction; our supervised verifier baseline (logistic regression on all five signals, no oracle gap closure; \\S\\ref{sec:robustness_main}) suggests that the combination strategy itself is not the bottleneck.\n\\citet{culotta2004confidence} and \\citet{mejer2010confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; \\citet{fomicheva2020unsupervised} systematically apply model-internal signals (MC Dropout, D-Lex) for unsupervised quality estimation in NMT, establishing the paradigm we extend from sequence-level to set-valued structured outputs.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \\cite{willard2023guided, park2024grammar}; recent work highlights hidden costs of constrained generation for log-probability estimation \\cite{schall2025hidden} and inference efficiency \\cite{yun2025price}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} study predictive uncertainty for autoregressive structured prediction.\nOur structural signals instead measure agreement over output \\textit{structure}, requiring no model modification.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid} with structural utility functions.\nUnlike machine translation where MBR yields consistent gains \\cite{freitag2022high}, we find that utility \\textit{is} aligned with quality (within-instance SJ--F1 $\\rho{=}0.52$) but instance degeneracy eliminates the headroom MBR would otherwise exploit.\n\\citet{eikema2025structured} find that standard MBR utilities degrade on structured outputs due to bag-of-unit mismatches.\nOur diagnosis is complementary but distinct: even when utility \\textit{is} well-aligned with quality (within-instance $\\rho{=}0.52$), output degeneracy eliminates the headroom MBR needs to improve over greedy.\nNER's discrete label space produces more extreme degeneracy (up to 58\\%) than the partial-overlap regime typical in MT and summarization (\\S\\ref{sec:discussion}).\n\\citet{xie2024selfevaluation} show self-evaluation improves selective generation for discrete tasks; our results suggest this does not transfer to structured extraction without learned scoring.\nOur quality estimation results connect to selective prediction \\cite{kuleshov2015calibrated}: signals with $\\rho$ up to 0.45 on CoNLL (0.38 on the primary test bed, 0.42 on Few-NERD) and AUROC up to 0.82 can support abstention policies that flag low-quality extractions, providing practical value independent of sample selection.\nConformal prediction constructs prediction sets with coverage guarantees \\cite{zhang2025conformal}; while complementary, its set-valued output differs from best-of-$N$ selection.\n\n\\paragraph{Best-of-$N$ with learned verifiers.}\n\\citet{gao2023scaling} establish scaling laws for best-of-$N$ selection with learned reward models, showing that BoN performance scales log-linearly with $N$ but eventually degrades due to reward overoptimization.\nOur unsupervised signals face a more fundamental limitation: they cannot rank candidates at all (instance-level signals) or rank them too weakly (LP compression), making the overoptimization regime irrelevant.\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and quality-aware decoding \\cite{fernandes2022quality} learn per-sample scoring that may bridge this gap; our LoRA-rank ablation (degeneracy 7\\% vs.\\ 21\\%, selection still fails) suggests that verifier training is necessary beyond merely increasing output diversity.\nFine-tuning itself contributes to the problem: \\citet{kirk2024understanding} document diversity collapse in RLHF-trained models; our instance degeneracy is an analogous phenomenon in supervised fine-tuning, where stronger models converge to more uniform outputs.\nNucleus sampling \\cite{holtzman2020curious} improves diversity in open-ended generation, but our constrained structured outputs limit the diversity that temperature scaling alone can recover.\n",
      "numLines": 38,
      "startLine": 1,
      "totalLines": 38
    }
  },
  "sourceToolAssistantUUID": "e1b00e1c-048d-40a1-ab02-57ffcebcfe88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T07:08:08.816Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Psr3MPQ5K7ZzT8SjQaEKkC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59488069-8ee8-4c66-b0db-d03fd226aab5",
  "isSidechain": false,
  "requestId": "req_011Cb7ihg1vMujYmfrdqRJtG",
  "type": "assistant",
  "uuid": "4619ba68-ab2b-42d1-a1a6-c6bac5930291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196GSEsN4gfffy6h1ChwDup",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 14730,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 31044,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 14730,
          "output_tokens": 369,
          "cache_read_input_tokens": 31044,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T07:08:08.821Z_

<details><summary>↩ Tool result · `toolu_01Psr3MPQ5K7ZzT8SjQaEKkC`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to sample selection, and the gap has a three-layer structure: four instance-level signals cannot rank candidates by construction; MBR selection with well-aligned utility ($\rho{=}0.52$) fails because instance degeneracy (10--58\%) collapses the candidate pool; and LP, the sole per-sample signal, is compressed to near-ineffectiveness (median range 0.041 nats).
6	LP selection effectiveness is inversely associated with instance degeneracy: at 10\% (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\% (CoNLL), LP fails.
7	In the low-degeneracy regime, LP selection scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
8	Structural signals fail uniformly regardless of degeneracy, and supervised combination of all five signals cannot close the oracle gap, confirming the bottleneck is in the feature space.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the gap for structural signals requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers}; LP provides a lightweight baseline when degeneracy is low.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4619ba68-ab2b-42d1-a1a6-c6bac5930291",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "2abc4dbe-bb75-4ae8-a98c-c51f86e4f536",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.\nAll signals achieve reliable quality estimation ($\\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction and error flagging.\nHowever, quality estimation does not translate to sample selection, and the gap has a three-layer structure: four instance-level signals cannot rank candidates by construction; MBR selection with well-aligned utility ($\\rho{=}0.52$) fails because instance degeneracy (10--58\\%) collapses the candidate pool; and LP, the sole per-sample signal, is compressed to near-ineffectiveness (median range 0.041 nats).\nLP selection effectiveness is inversely associated with instance degeneracy: at 10\\% (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\\% (CoNLL), LP fails.\nIn the low-degeneracy regime, LP selection scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).\nStructural signals fail uniformly regardless of degeneracy, and supervised combination of all five signals cannot close the oracle gap, confirming the bottleneck is in the feature space.\nWhether these patterns persist at 70B+ scales remains open.\nClosing the gap for structural signals requires content-aware verifiers that examine output semantics \\cite{cobbe2021verifiers}; LP provides a lightweight baseline when degeneracy is low.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "4619ba68-ab2b-42d1-a1a6-c6bac5930291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T07:08:09.359Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MTyntGyGNXaaxsQ9pdARGL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2abc4dbe-bb75-4ae8-a98c-c51f86e4f536",
  "isSidechain": false,
  "requestId": "req_011Cb7ihg1vMujYmfrdqRJtG",
  "type": "assistant",
  "uuid": "872ee2a3-e3a1-4588-b56a-866e45939371",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196GSEsN4gfffy6h1ChwDup",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 14730,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 31044,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 14730,
          "output_tokens": 369,
          "cache_read_input_tokens": 31044,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T07:08:09.367Z_

<details><summary>↩ Tool result · `toolu_01MTyntGyGNXaaxsQ9pdARGL`</summary>

```text
1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing within-instance variance on SciERC ($4{\times}$); LP${\times}$VC combinations also fail to recover selection (\S\ref{sec:discussion}); calibration-based approaches remain unexplored.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "872ee2a3-e3a1-4588-b56a-866e45939371",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "c80c6b51-d9c4-44a6-8b99-3a6875bdce07",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.\nWe cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.\nWe do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\\ref{app:n_scaling}).\nThe free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\\ref{app:re_extension}.\nQwen3-8B's SciERC checkpoint used empty \\texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nLP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.\nWe tested verbalized confidence \\cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\\ref{app:verbalized_confidence}).\nAd-hoc LP${\\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \\S\\ref{sec:discussion}); whether \\textit{learned} combinations could close the gap remains open.\nThe $\\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.\nWe tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing within-instance variance on SciERC ($4{\\times}$); LP${\\times}$VC combinations also fail to recover selection (\\S\\ref{sec:discussion}); calibration-based approaches remain unexplored.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  },
  "sourceToolAssistantUUID": "872ee2a3-e3a1-4588-b56a-866e45939371",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T07:08:09.814Z_

<details open><summary>🔧 Tool call — Read · `toolu_016NhBpiGcyVVVp8UKAX5HWr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c80c6b51-d9c4-44a6-8b99-3a6875bdce07",
  "isSidechain": false,
  "requestId": "req_011Cb7ihg1vMujYmfrdqRJtG",
  "type": "assistant",
  "uuid": "276e3448-5502-45a7-b46c-918019a57a9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196GSEsN4gfffy6h1ChwDup",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 14730,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 31044,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 14730,
          "output_tokens": 369,
          "cache_read_input_tokens": 31044,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验设计**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics/Ref…",
  "leafUuid": "276e3448-5502-45a7-b46c-918019a57a9f",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Tool result

_source line 42 · 2026-05-17T07:08:10.063Z_

<details><summary>↩ Tool result · reported error · `toolu_016NhBpiGcyVVVp8UKAX5HWr`</summary>

```text
File content (30903 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "276e3448-5502-45a7-b46c-918019a57a9f",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "cab1f55a-2072-42e8-bcec-901e322180ef",
  "toolUseResult": "Error: File content (30903 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "276e3448-5502-45a7-b46c-918019a57a9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43 · 2026-05-17T07:08:10.066Z_

```json
{
  "parentUuid": "cab1f55a-2072-42e8-bcec-901e322180ef",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "dfffd5b5-6eac-4374-b634-55f5a13baf48",
  "timestamp": "2026-05-17T07:08:10.066Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 44 · 2026-05-17T07:08:14.935Z_

<details><summary>Logged reasoning block</summary>

```text
The appendix is too long. Let me read it in parts, focusing on the most critical sections for my review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfffd5b5-6eac-4374-b634-55f5a13baf48",
  "isSidechain": false,
  "requestId": "req_011Cb7iiQqtaLFceSKcvFJxf",
  "type": "assistant",
  "uuid": "4b208aa0-e8f1-463f-8b1b-c709743f9573",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ouvwck6m6XJaf9KB5Zcmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18166,
      "cache_read_input_tokens": 32262,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 32262,
          "cache_creation_input_tokens": 18166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18166
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T07:08:15.462Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XsD9QJtj6bTifjRTmLr9Er`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b208aa0-e8f1-463f-8b1b-c709743f9573",
  "isSidechain": false,
  "requestId": "req_011Cb7iiQqtaLFceSKcvFJxf",
  "type": "assistant",
  "uuid": "3505c096-5856-45bc-83af-9fc68ccbaded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ouvwck6m6XJaf9KB5Zcmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18166,
      "cache_read_input_tokens": 32262,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 32262,
          "cache_creation_input_tokens": 18166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18166
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T07:08:15.472Z_

<details><summary>↩ Tool result · `toolu_01XsD9QJtj6bTifjRTmLr9Er`</summary>

```text
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
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
48	\quad LP & $T{=}0.7$ & 0.249 & --- \\
49	\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\
50	\midrule
51	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
52	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
53	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
54	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
55	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
56	\midrule
57	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
58	\quad SJ &  & $0.474{\pm}0.009$ & --- \\
59	\quad FK &  & $0.467{\pm}0.009$ & --- \\
60	\quad EM &  & $0.473{\pm}0.010$ & --- \\
61	\quad VC &  & $0.470{\pm}0.006$ & --- \\
62	\quad LP &  & $0.311{\pm}0.003$ & --- \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
70	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
71	\label{fig:temperature_robustness}
72	\end{figure}
73	
74	\paragraph{Temperature sensitivity.}
75	SJ NER $\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.
76	FK NER $\rho$ drops by 0.022, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
77	LP exhibits the largest temperature effect on NER ($\rho{=}0.249$ at $T{=}0.7$ vs.\ $0.205$ at $T{=}1.0$, $\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.
78	Across all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).
79	
80	\paragraph{Sample size scaling.}
81	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
82	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.
87	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
88	
89	\paragraph{Transfer across model families.}
90	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
91	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
92	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$),\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.474{\pm}0.009$ vs.\ LP $0.311{\pm}0.003$, $\Delta{=}{+}0.163$).
93	
94	\paragraph{FK independence: instance-level permutation test.}\label{app:fk_independence}
95	
96	To verify that Fleiss' $\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.
97	For each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}
103	\label{tab:fk_independence}
104	\begin{tabular}{lrcccc}
105	\toprule
106	Config & $n$ & FK mean & 95\% CI & $t$ & Split-half $r$ \\
107	\midrule
108	SciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\
109	CoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\
110	CoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	Table~\ref{tab:fk_independence} reports the results.
116	All configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), confirming that FK captures genuine inter-sample agreement rather than chance label co-occurrence.
117	Split-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), indicating moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.
118	The higher FK means on CoNLL ($0.720$--$0.927$) vs.\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.
119	
120	\section{Calibration Analysis}\label{app:calibration}
121	
122	\begin{figure*}[t]
123	\centering
124	\includegraphics[width=\textwidth]{fig_reliability}
125	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
126	\label{fig:reliability}
127	\end{figure*}
128	
129	Reliability diagrams use 10 equal-width bins.
130	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
131	
132	\section{Additional Analyses}\label{app:additional}
133	
134	\begin{figure*}[t]
135	\centering
136	\includegraphics[width=\textwidth]{fig_signal_heatmap}
137	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
138	\label{fig:signal_heatmap}
139	\end{figure*}
140	
141	\paragraph{Per-relation diagnostic.}
142	RE signal degradation is relation-specific.
143	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
144	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
145	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
146	
147	\paragraph{Capability stratification.}
148	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
149	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
150	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
151	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
152	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
153	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
154	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
155	
156	\paragraph{Length vs.\ log-probability.}
157	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
158	
159	\begin{figure}[t]
160	\centering
161	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
162	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
163	\label{fig:length_logprob_scatter}
164	\end{figure}
165	
166	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
167	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
168	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
169	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
170	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
171	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
172	Evaluation circularity is negligible.
173	
174	\paragraph{SJ normalizer robustness.}
175	Equation~\ref{eq:sj} uses $\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \cup g_j|$.
176	Table~\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\Delta\rho|{<}0.01$ in every case, confirming that the choice between max and union normalization does not affect conclusions.
177	
178	\begin{table}[h]
179	\centering
180	\small
181	\caption{SJ normalizer comparison (Spearman $\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\max(|g_i|,|g_j|)$; Union: $|g_i \cup g_j|$.}
182	\label{tab:sj_normalizer}
183	\begin{tabular}{@{}ll ccc@{}}
184	\toprule
185	Dataset & Model & $\rho$(max) & $\rho$(union) & $\Delta\rho$ \\
186	\midrule
187	CoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\
188	CoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\
189	CoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\
190	SciERC & Qwen3-8B & .360 & .365 & $-$.005 \\
191	SciERC & Qwen3-4B & .422 & .423 & $-$.001 \\
192	SciERC & LLaMA-8B & .363 & .372 & $-$.009 \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	\paragraph{Conditional filtering details.}
198	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
199	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
200	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3505c096-5856-45bc-83af-9fc68ccbaded",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "9d9d3453-35fb-41a2-b881-de144b6d7679",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\nWe exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\\%; SciERC: 22/551, 4.0\\%).\nFor these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\\rho$ depending on signal behavior at the boundary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\quad LP & $T{=}0.7$ & 0.249 & --- \\\\\n\\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.474{\\pm}0.009$ & --- \\\\\n\\quad FK &  & $0.467{\\pm}0.009$ & --- \\\\\n\\quad EM &  & $0.473{\\pm}0.010$ & --- \\\\\n\\quad VC &  & $0.470{\\pm}0.006$ & --- \\\\\n\\quad LP &  & $0.311{\\pm}0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.\nFK NER $\\rho$ drops by 0.022, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nLP exhibits the largest temperature effect on NER ($\\rho{=}0.249$ at $T{=}0.7$ vs.\\ $0.205$ at $T{=}1.0$, $\\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.\nAcross all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), making it a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$),\\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.474{\\pm}0.009$ vs.\\ LP $0.311{\\pm}0.003$, $\\Delta{=}{+}0.163$).\n\n\\paragraph{FK independence: instance-level permutation test.}\\label{app:fk_independence}\n\nTo verify that Fleiss' $\\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.\nFor each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\n\\label{tab:fk_independence}\n\\begin{tabular}{lrcccc}\n\\toprule\nConfig & $n$ & FK mean & 95\\% CI & $t$ & Split-half $r$ \\\\\n\\midrule\nSciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\\\\nCoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\\\\nCoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fk_independence} reports the results.\nAll configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), confirming that FK captures genuine inter-sample agreement rather than chance label co-occurrence.\nSplit-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), indicating moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.\nThe higher FK means on CoNLL ($0.720$--$0.927$) vs.\\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{SJ normalizer robustness.}\nEquation~\\ref{eq:sj} uses $\\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \\cup g_j|$.\nTable~\\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\\Delta\\rho|{<}0.01$ in every case, confirming that the choice between max and union normalization does not affect conclusions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\n\\label{tab:sj_normalizer}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\nDataset & Model & $\\rho$(max) & $\\rho$(union) & $\\Delta\\rho$ \\\\\n\\midrule\nCoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\\\\nCoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\\\\nCoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\\\\nSciERC & Qwen3-8B & .360 & .365 & $-$.005 \\\\\nSciERC & Qwen3-4B & .422 & .423 & $-$.001 \\\\\nSciERC & LLaMA-8B & .363 & .372 & $-$.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 1183
    }
  },
  "sourceToolAssistantUUID": "3505c096-5856-45bc-83af-9fc68ccbaded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T07:08:16.260Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016dsvWNAHnV3W16go1tz6ce`</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d9d3453-35fb-41a2-b881-de144b6d7679",
  "isSidechain": false,
  "requestId": "req_011Cb7iiQqtaLFceSKcvFJxf",
  "type": "assistant",
  "uuid": "db6a12a9-0f30-4e8d-bea3-4116ccdba43d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ouvwck6m6XJaf9KB5Zcmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18166,
      "cache_read_input_tokens": 32262,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 32262,
          "cache_creation_input_tokens": 18166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18166
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验设计**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics/Ref…",
  "leafUuid": "db6a12a9-0f30-4e8d-bea3-4116ccdba43d",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Tool result

_source line 50 · 2026-05-17T07:08:21.701Z_

<details><summary>↩ Tool result · `toolu_016dsvWNAHnV3W16go1tz6ce`</summary>

```text
Web search results for query: "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"Surviving ARR May Meta-Review & Deciding on EMNLP 2025: A Tactical and Honest Guide | CSPaper Forum","url":"https://forum.cspaper.org/topic/113/surviving-arr-may-meta-review-deciding-on-emnlp-2025-a-tactical-and-honest-guide"},{"title":"Conference Decisions · GitHub","url":"https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper","url":"https://cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"}]

Based on the search results, I found information about the ACL Rolling Review (ARR) scoring system for 2025. Here's what I found regarding the soundness and excitement scoring scales:

## Soundness Scoring Scale

The soundness scoring uses a 1-5 scale: 5 = Excellent (one of the most thorough papers), 4 = Strong (provides sufficient support for claims), 3 = Acceptable (provides sufficient support for main claims), and 1 = Major Issues (not sufficiently thorough for publication).

## Excitement Scoring Scale

The excitement scoring also uses a 1-5 scale: 5 = Highly Exciting (would recommend to others/attend presentation), and 1 = Not Exciting (doesn't resonate and isn't relevant to the ACL community).

## Key Principles

Soundness scores must be justified by the text of the review, while excitement scores reflect personal taste and don't necessarily come with explicit reasons.

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

The review form on the official ACL Rolling Review website provides detailed rubrics for each score level to guide reviewers in their assessments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db6a12a9-0f30-4e8d-bea3-4116ccdba43d",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "711d3825-34f1-4ce1-813f-6c3d050229bf",
  "toolUseResult": {
    "query": "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DoqUCkXezNhrFGJmDZyixA",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"
          },
          {
            "title": "ACL 2023 Acceptance Recommendations - ACL 2023",
            "url": "https://2023.aclweb.org/blog/overall-recommendation/"
          },
          {
            "title": "ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X",
            "url": "https://x.com/aclmeeting/status/1637827267173953540"
          },
          {
            "title": "Surviving ARR May Meta-Review & Deciding on EMNLP 2025: A Tactical and Honest Guide | CSPaper Forum",
            "url": "https://forum.cspaper.org/topic/113/surviving-arr-may-meta-review-deciding-on-emnlp-2025-a-tactical-and-honest-guide"
          },
          {
            "title": "Conference Decisions · GitHub",
            "url": "https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper",
            "url": "https://cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"
          }
        ]
      },
      "Based on the search results, I found information about the ACL Rolling Review (ARR) scoring system for 2025. Here's what I found regarding the soundness and excitement scoring scales:\n\n## Soundness Scoring Scale\n\nThe soundness scoring uses a 1-5 scale: 5 = Excellent (one of the most thorough papers), 4 = Strong (provides sufficient support for claims), 3 = Acceptable (provides sufficient support for main claims), and 1 = Major Issues (not sufficiently thorough for publication).\n\n## Excitement Scoring Scale\n\nThe excitement scoring also uses a 1-5 scale: 5 = Highly Exciting (would recommend to others/attend presentation), and 1 = Not Exciting (doesn't resonate and isn't relevant to the ACL community).\n\n## Key Principles\n\nSoundness scores must be justified by the text of the review, while excitement scores reflect personal taste and don't necessarily come with explicit reasons.\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\nThe review form on the official ACL Rolling Review website provides detailed rubrics for each score level to guide reviewers in their assessments."
    ],
    "durationSeconds": 5.437487850000005
  },
  "sourceToolAssistantUUID": "db6a12a9-0f30-4e8d-bea3-4116ccdba43d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-17T07:08:27.567Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read more of the appendix to fully understand the paper, specifically the sections about:
1. Multi-seed stability
2. TOST equivalence tests
3. Free-form ablation
4. N-scaling selection
5. Per-type LP analysis

These are critical for my review of method rigor and experimental design.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "711d3825-34f1-4ce1-813f-6c3d050229bf",
  "isSidechain": false,
  "requestId": "req_011Cb7ijGc4iUDaJzL8wWGyY",
  "type": "assistant",
  "uuid": "e3489153-59c5-4581-9eaa-38ebbaec5f18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JxpXgyXLD5CDLcwPgSWHJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7236,
      "cache_read_input_tokens": 50428,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 50428,
          "cache_creation_input_tokens": 7236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7236
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-17T07:08:29.612Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LMhhzFRnpcSLE1phM45uSf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 200,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3489153-59c5-4581-9eaa-38ebbaec5f18",
  "isSidechain": false,
  "requestId": "req_011Cb7ijGc4iUDaJzL8wWGyY",
  "type": "assistant",
  "uuid": "735033b6-d334-4810-84f8-cd7abc528226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JxpXgyXLD5CDLcwPgSWHJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7236,
      "cache_read_input_tokens": 50428,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 50428,
          "cache_creation_input_tokens": 7236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7236
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-17T07:08:29.620Z_

<details><summary>↩ Tool result · `toolu_01LMhhzFRnpcSLE1phM45uSf`</summary>

```text
200	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} (\S\ref{sec:qe_results}) reports all five signals on WNUT-17 with full-set and conditional $\rho$.
207	The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
208	VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\rho{=}0.350$ is the highest among all signals on the non-zero subset, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
209	
210	\paragraph{Cross-configuration selection analysis.}
211	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
212	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
213	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
214	
215	\begin{table*}[t]
216	\centering
217	\small
218	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
219	\label{tab:cross_selection}
220	\begin{tabular}{llccccccc}
221	\toprule
222	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
223	\midrule
224	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
225	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
226	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
227	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
228	\bottomrule
229	\end{tabular}
230	\end{table*}
231	
232	\paragraph{Diminishing returns of $N$-scaling.}
233	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
234	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
235	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
236	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
237	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
238	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
239	
240	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
241	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
242	VC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
243	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
244	This reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
245	
246	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
247	
248	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
249	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
250	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
251	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
252	
253	\begin{table}[t]
254	\centering
255	\small
256	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
257	\label{tab:bootstrap_signal_ci}
258	\begin{tabular}{lcc}
259	\toprule
260	Signal & $\rho$ & 95\% CI \\
261	\midrule
262	VC & +0.379 & [+0.299, +0.456] \\
263	SJ & +0.360 & [+0.277, +0.437] \\
264	EM & +0.295 & [+0.212, +0.371] \\
265	FK & +0.267 & [+0.176, +0.354] \\
266	LP & +0.205 & [+0.119, +0.291] \\
267	\bottomrule
268	\end{tabular}
269	
270	\vspace{0.5em}
271	
272	\begin{tabular}{lccc}
273	\toprule
274	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
275	\midrule
276	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
277	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
278	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
279	\bottomrule
280	\end{tabular}
281	
282	\smallskip
283	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
284	\end{table}
285	
286	At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.
287	On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
288	On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
289	
290	\section{Diversity and Selection Analysis}\label{app:diversity}
291	
292	\begin{figure*}[t]
293	\centering
294	\includegraphics[width=\textwidth]{fig_selection_gap}
295	\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.40, no signal significantly outperforms single-sample (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\ref{tab:selection}.}
296	\label{fig:selection_gap}
297	\end{figure*}
298	
299	\paragraph{Output diversity quantification.}
300	Table~\ref{tab:diversity} summarizes output diversity across configurations.
301	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
302	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
303	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where single-sample F1 already exceeds 0.90.
304	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
305	
306	\begin{table}[t]
307	\centering
308	\small
309	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
310	\label{tab:diversity}
311	\begin{tabular}{lcc}
312	\toprule
313	Config & Identical & Unique \\
314	\midrule
315	Qwen/SciERC & 11\% & 43\% \\
316	LLaMA/SciERC & 18\% & 39\% \\
317	Qwen/CoNLL & 57\% & --- \\
318	LLaMA/CoNLL & 88\% & --- \\
319	WNUT-17 & 55\% & --- \\
320	\bottomrule
321	\end{tabular}
322	\end{table}
323	
324	\paragraph{Oracle-improvable fraction.}
325	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding single-sample\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \S\ref{sec:evaluation}); the diversity quantification in Table~\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
326	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
327	
328	\paragraph{Diversity-stratified selection gap.}
329	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
330	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.
331	This rules out insufficient diversity as an explanation for the correlation-selection gap.
332	
333	\paragraph{TOST equivalence testing.}\label{app:tost}
334	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
335	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
336	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
337	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
338	We address this below with externally anchored equivalence margins.
339	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
340	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
341	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
342	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
343	
344	\begin{table}[t]
345	\centering
346	\small
347	\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).}
348	\label{tab:tost}
349	\begin{tabular}{l cccc cccc}
350	\toprule
351	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
352	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
353	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
354	\midrule
355	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
356	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
357	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
358	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
359	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
360	\bottomrule
361	\end{tabular}
362	\end{table}
363	
364	\paragraph{External equivalence margins.}
365	The oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\delta$ is calibrated against the very quantity it contextualizes.
366	To resolve this, we supplement with three externally grounded margins:
367	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), representing measurement noise;
368	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \cite{ratinov2009design};
369	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
370	
371	Results under these external anchors diverge sharply by configuration.
372	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
373	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, exceeding even $\delta_{\mathrm{literature}}$.
374	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
375	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
376	
377	\paragraph{Multiple comparison considerations.}\label{app:multiple_comparisons}
378	Our primary selection analysis involves ${\sim}$20 comparisons (5 signals $\times$ 3--4 configurations).
379	Since all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.
380	The sole positive finding---non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion})---survives Bonferroni correction over 5 signal comparisons ($p_{\mathrm{adj}}{=}0.020 < 0.05$), as noted in the main text footnote.
381	For quality estimation signal rankings, differences between the top signals (e.g., VC vs.\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.
382	
383	\section{Multi-Seed Stability}\label{app:multiseed}
384	
385	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
386	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).
387	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
388	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
389	
390	\begin{table}[t]
391	\centering
392	\small
393	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
394	\label{tab:multiseed}
395	\begin{tabular}{lccccc}
396	\toprule
397	& LP & FK & SJ & VC & EM \\
398	\midrule
399	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
400	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
401	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
402	\midrule
403	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
404	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
405	\midrule
406	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
407	Qwen & .579${\pm}$.008 & .600${\pm}$.016 & .659${\pm}$.016 & .677${\pm}$.011 & .631${\pm}$.013 \\
408	LLaMA & .565${\pm}$.008 & .593${\pm}$.006 & .632${\pm}$.012 & .673${\pm}$.009 & .606${\pm}$.005 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	\section{Training Configuration}\label{app:training}
414	
415	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
416	
417	\begin{table}[t]
418	\centering
419	\small
420	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
421	\label{tab:training}
422	\begin{tabular}{ll}
423	\toprule
424	Parameter & Value \\
425	\midrule
426	LoRA rank / $\alpha$ & 32 / 64 \\
427	LoRA target & All linear modules \\
428	LoRA dropout & 0 \\
429	Optimizer & AdamW \\
430	Learning rate & 2e-4, cosine schedule \\
431	Warmup ratio & 0.1 \\
432	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
433	Epochs & 5 \\
434	Max sequence length & 2048 \\
435	Precision & bf16 \\
436	Gradient checkpointing & Enabled \\
437	Max gradient norm & 1.0 \\
438	Training seed & 42 \\
439	Framework & LLaMA Factory \\
440	\midrule
441	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
442	SciERC split & 1861 / 275 / 551 \\
443	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
444	& eval\_steps${=}$200, save\_limit${=}$5 \\
445	\bottomrule
446	\end{tabular}
447	\end{table}
448	
449	\paragraph{Prompt template.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "735033b6-d334-4810-84f8-cd7abc528226",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "9b3abb9d-858b-4318-9b6b-66b3edaeb57b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "EM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} (\\S\\ref{sec:qe_results}) reports all five signals on WNUT-17 with full-set and conditional $\\rho$.\nThe full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.\nVC's high full-set $\\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\\rho{=}0.350$ is the highest among all signals on the non-zero subset, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (single-sample F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\nAt $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.\nOn SciERC NER ($n{=}529$), SJ--FK ($\\Delta\\rho{=}0.147$--$0.160$, all $p{\\leq}0.002$) and VC--FK ($\\Delta\\rho{=}0.138$--$0.188$, all $p{\\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\\Delta\\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).\nOn CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\\Delta\\rho{=}0.071$ ($p{<}0.001$), SJ $\\Delta\\rho{=}0.056$ ($p{<}0.001$), VC $\\Delta\\rho{=}0.022$ ($p{=}0.040$).\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.40, no signal significantly outperforms single-sample (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\\ref{tab:selection}.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where single-sample F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding single-sample\\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \\S\\ref{sec:evaluation}); the diversity quantification in Table~\\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\\label{app:tost}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\\delta$.\nThe $\\delta$ values are contextualized against oracle headroom (12--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThese proportions use the same test data that defines the headroom, introducing circularity: $\\delta$ is anchored to the very quantity it contextualizes.\nWe address this below with externally anchored equivalence margins.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{External equivalence margins.}\nThe oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\\delta$ is calibrated against the very quantity it contextualizes.\nTo resolve this, we supplement with three externally grounded margins:\n(1) $\\delta_{\\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), representing measurement noise;\n(2) $\\delta_{\\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \\cite{ratinov2009design};\n(3) $\\delta_{\\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \\cite{bergkirkpatrick2012empirical}.\n\nResults under these external anchors diverge sharply by configuration.\nOn LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\\Delta|{\\leq}0.1$~pp) and tight CIs at this sample size.\nOn Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, exceeding even $\\delta_{\\mathrm{literature}}$.\nOn SciERC NER ($n{=}529$), only SJ passes at $\\delta_{\\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.\nThese external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.\n\n\\paragraph{Multiple comparison considerations.}\\label{app:multiple_comparisons}\nOur primary selection analysis involves ${\\sim}$20 comparisons (5 signals $\\times$ 3--4 configurations).\nSince all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.\nThe sole positive finding---non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion})---survives Bonferroni correction over 5 signal comparisons ($p_{\\mathrm{adj}}{=}0.020 < 0.05$), as noted in the main text footnote.\nFor quality estimation signal rankings, differences between the top signals (e.g., VC vs.\\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .579${\\pm}$.008 & .600${\\pm}$.016 & .659${\\pm}$.016 & .677${\\pm}$.011 & .631${\\pm}$.013 \\\\\nLLaMA & .565${\\pm}$.008 & .593${\\pm}$.006 & .632${\\pm}$.012 & .673${\\pm}$.009 & .606${\\pm}$.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}",
      "numLines": 250,
      "startLine": 200,
      "totalLines": 1183
    }
  },
  "sourceToolAssistantUUID": "735033b6-d334-4810-84f8-cd7abc528226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验设计**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics/Ref…",
  "leafUuid": "9b3abb9d-858b-4318-9b6b-66b3edaeb57b",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Tool call

_source line 56 · 2026-05-17T07:08:35.486Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YH9CN4QNcY3XAABVF6sZst`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 449,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b3abb9d-858b-4318-9b6b-66b3edaeb57b",
  "isSidechain": false,
  "requestId": "req_011Cb7ijriAKwZ1XdWCkVR6o",
  "type": "assistant",
  "uuid": "93909477-5b9b-4168-aa3c-0d22d0a1326f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJdwmSTjZWKx6DkLiBMguT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7816,
      "cache_read_input_tokens": 57664,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 57664,
          "cache_creation_input_tokens": 7816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7816
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-17T07:08:35.496Z_

<details><summary>↩ Tool result · `toolu_01YH9CN4QNcY3XAABVF6sZst`</summary>

```text
449	\paragraph{Prompt template.}
450	For NER, we use a structured prompt:
451	\begin{quote}
452	\small
453	\texttt{System:} You are an expert in Named Entity Recognition.\\
454	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
455	Text: \texttt{\{input\_text\}}\\
456	Entity types: \texttt{\{schema\_types\}}
457	\end{quote}
458	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
459	
460	\paragraph{Constrained decoding.}
461	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
462	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
463	
464	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
465	
466	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
467	We quantify the potential impact on LP scores through three complementary arguments.
468	
469	\paragraph{LP shift magnitude.}
470	Empty thinking tokens (mean 4.5 per sample) constitute 2.1\% of tokens on SciERC.
471	The estimated LP shift is 0.001 nats per token (2.68\% of the median within-instance LP range of 0.041 nats).
472	Because all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\%$ of instances.
473	
474	\paragraph{Constant prefix cancellation.}
475	All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
476	Any LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \textit{rankings} unchanged.
477	
478	\paragraph{CoNLL control group.}
479	CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
480	If thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.
481	Instead, CoNLL shows \textit{higher} tied fractions at both temperatures (86.8\% at $T{=}1.0$, 95.8\% at $T{=}0.7$) than SciERC (60.3\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.
482	
483	\section{Log-Probability Score Compression}\label{app:logprob_ties}
484	
485	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
486	The median within-instance LP range is only 0.041 nats; we use $\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.
487	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
488	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
489	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
490	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.
491	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
492	
493	\begin{figure}[t]
494	\centering
495	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
496	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
497	\label{fig:lp_range_cdf}
498	\end{figure}
499	
500	\begin{table}[t]
501	\centering
502	\small
503	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
504	\label{tab:logprob_ties}
505	\begin{tabular}{lc}
506	\toprule
507	$\varepsilon$ threshold & Tied instances (\%) \\
508	\midrule
509	0.01 & 1.1\% \\
510	0.05 & 60.3\% \\
511	0.1  & ${\sim}$84\% \\
512	0.5  & ${\sim}$99\% \\
513	\bottomrule
514	\end{tabular}
515	\end{table}
516	
517	\paragraph{Non-tied subset.}
518	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
519	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
520	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
521	
522	\paragraph{$\varepsilon$ sensitivity sweep (post-hoc exploratory).}
523	Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.
524	The tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.
525	$\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\varepsilon{\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\leq}36$).
526	
527	\begin{table}[t]
528	\centering
529	\small
530	\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\varepsilon{=}0.05$ yields the strongest statistical separation.}
531	\label{tab:epsilon_sweep}
532	\begin{tabular}{ccccc}
533	\toprule
534	$\varepsilon$ & Tied\% & Non-tied $n$ & $\Delta$ (pp) & $p$ \\
535	\midrule
536	0.01 & 1.1\% & 523 & $+$0.58 & .21 \\
537	0.02 & 13.6\% & 457 & $+$0.83 & .15 \\
538	0.03 & 31.8\% & 361 & $+$1.31 & .079 \\
539	\textbf{0.05} & \textbf{60.3\%} & \textbf{210} & \textbf{$+$2.86} & \textbf{.004} \\
540	0.10 & 83.9\% & 85 & $+$3.69 & .034 \\
541	0.15 & 93.2\% & 36 & $+$4.15 & .11 \\
542	0.20 & 96.4\% & 19 & $+$4.59 & .13 \\
543	\bottomrule
544	\end{tabular}
545	\end{table}
546	
547	\paragraph{$\varepsilon$ robustness of selection F1.}\label{app:epsilon_robustness}
548	The preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\varepsilon$ to define MBR-style proximity in selection.
549	Table~\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\varepsilon \in [0, 0.2]$ for all signals and configurations.
550	At $\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.
551	Spearman $\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\varepsilon$ parameter affects only the selection analysis.
552	
553	\begin{table}[t]
554	\centering
555	\small
556	\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
557	\label{tab:epsilon_robustness}
558	\begin{tabular}{lcccc}
559	\toprule
560	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL}} \\
561	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
562	Signal & Qwen & LLaMA & Qwen & LLaMA \\
563	\midrule
564	SJ & 0.92 & 1.45 & 0.99 & 0.18 \\
565	FK & 1.03 & 0.93 & 0.60 & 0.15 \\
566	VC & 2.33 & 0.53 & 0.72 & 0.18 \\
567	EM & 0.00 & 0.00 & 0.00 & 0.00 \\
568	LP & 3.65 & 2.58 & 3.00 & 0.31 \\
569	\bottomrule
570	\end{tabular}
571	\end{table}
572	
573	\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
574	
575	Table~\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\Delta$ (gain over single-sample) for LP and SJ.
576	
577	\begin{table}[t]
578	\centering
579	\small
580	\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
581	\label{tab:vc_quartile}
582	\begin{tabular}{lcccc}
583	\toprule
584	Quartile & Mean VC & LP $\Delta$ & SJ $\Delta$ & Oracle (pp) \\
585	\midrule
586	\multicolumn{5}{l}{\textit{NER}} \\
587	Q1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\
588	Q2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\
589	Q3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\
590	Q4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\
591	\midrule
592	\multicolumn{5}{l}{\textit{$^\dagger$RE}} \\
593	Q1 (low) & --- & $-$3.56 & --- & --- \\
594	Q4 (high) & --- & $+$4.01 & --- & --- \\
595	\bottomrule
596	\end{tabular}
597	\end{table}
598	
599	The NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:
600	\begin{itemize}
601	\item \textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp---samples have already converged, leaving little room for any signal to improve selection.
602	\item \textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, yielding inconsistent $\Delta$ signs across quartiles.
603	\end{itemize}
604	
605	On $^\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp, suggesting LP can recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.
606	
607	On CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), yielding $\Delta{=}0$ universally---a ceiling effect even more extreme than SciERC Q4.
608	
609	\section{Exploratory Extension to Relation Extraction}\label{app:re_extension}
610	
611	We extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.
612	RE produces sets of (head, relation, tail) triples with partial overlap; 40\% of RE instances receive zero F1, and entity span errors account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect (\S\ref{app:additional}).
613	All RE results use Qwen3-8B unless noted; single-seed ($\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.
614	
615	\paragraph{Quality estimation.}
616	RE quality estimation is reported in Table~\ref{tab:multiseed} (3-seed means).
617	The signal ranking differs from NER: VC leads ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal reflecting RE's higher sensitivity to per-sample scoring.
618	RE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\ref{fig:reliability}).
619	
620	\paragraph{Selection.}
621	Table~\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.
622	At $N{=}16$ (Qwen3-4B, Table~\ref{tab:re_n16_selection}), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.
623	
624	\paragraph{Scale ablation.}
625	At 4B scale (Qwen3-4B, $N{=}8$, $\text{seed}{=}42$), RE quality estimation shows FK $\rho{=}0.359$ and LP $\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\ $0.250$).
626	Selection remains below single-sample on RE ($\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.
627	
628	\paragraph{Free-form decoding.}
629	RE LP selection consistently reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp across 4 seeds vs.\ $-0.9$~pp under constrained decoding at 8B; \S\ref{app:freeform_ablation}), suggesting constrained decoding's fixed template obscures LP signal in RE (\S\ref{app:mbr_discussion}).
630	
631	\section{RE Conditional Selection}\label{app:re_conditional_selection}
632	
633	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
634	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
635	All five signals underperform single-sample on both subsets.
636	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
637	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
638	
639	\begin{table}[t]
640	\centering
641	\small
642	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
643	\label{tab:re_cond_selection}
644	\begin{tabular}{lcc}
645	\toprule
646	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
647	\midrule
648	Oracle & 0.585 & 0.757 \\
649	\midrule
650	LP & 0.395 & 0.600 \\
651	SJ & 0.386 & 0.604 \\
652	EM & 0.372 & 0.583 \\
653	VC & 0.359 & 0.574 \\
654	\midrule
655	Greedy & 0.404 & 0.674 \\
656	\bottomrule
657	\end{tabular}
658	\end{table}
659	
660	\section{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
661	
662	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
663	All four consistency signals underperform single-sample, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
664	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
665	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
666	This cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the persistent limitation of instance-level signals for candidate ranking across tested regimes.
667	
668	\begin{table}[t]
669	\centering
670	\small
671	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
672	\label{tab:re_n16_selection}
673	\begin{tabular}{lccc}
674	\toprule
675	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
676	\midrule
677	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
678	\midrule
679	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
680	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
681	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
682	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
683	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
684	\midrule
685	Greedy & $.291{\pm}.000$ & --- & --- \\
686	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
687	\bottomrule
688	\end{tabular}
689	\end{table}
690	
691	\section{MBR Decoding and Task-Specific Interactions}\label{app:mbr_discussion}
692	
693	\paragraph{Connection to MBR decoding.}
694	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
695	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy---the core of the correlation-selection gap.
696	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
697	
698	\paragraph{Task-specific decoding interactions.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93909477-5b9b-4168-aa3c-0d22d0a1326f",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "69d222eb-236c-4d2a-87aa-65128fec9d78",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Thinking Token Impact Analysis}\\label{app:thinking_token}\n\nQwen3-8B's SciERC checkpoint was trained with empty \\texttt{&lt;think>&lt;/think>} blocks prepended to each response (\\S\\ref{sec:setup}).\nWe quantify the potential impact on LP scores through three complementary arguments.\n\n\\paragraph{LP shift magnitude.}\nEmpty thinking tokens (mean 4.5 per sample) constitute 2.1\\% of tokens on SciERC.\nThe estimated LP shift is 0.001 nats per token (2.68\\% of the median within-instance LP range of 0.041 nats).\nBecause all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\\%$ of instances.\n\n\\paragraph{Constant prefix cancellation.}\nAll $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.\nAny LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \\textit{rankings} unchanged.\n\n\\paragraph{CoNLL control group.}\nCoNLL and WNUT-17 checkpoints were trained without thinking tokens (\\texttt{enable\\_thinking=False}).\nIf thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.\nInstead, CoNLL shows \\textit{higher} tied fractions at both temperatures (86.8\\% at $T{=}1.0$, 95.8\\% at $T{=}0.7$) than SciERC (60.3\\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats; we use $\\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.\nAt this cutpoint, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\\varepsilon$, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\nThis compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\\%$ (vs.\\ seed${=}42$: $0.041$ nats, $60.3\\%$).\nSeed~456 uses a different subtask flag (joint vs.\\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\paragraph{$\\varepsilon$ sensitivity sweep (post-hoc exploratory).}\nTable~\\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.\nThe tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.\n$\\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\\varepsilon{\\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\\leq}36$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\n\\label{tab:epsilon_sweep}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\varepsilon$ & Tied\\% & Non-tied $n$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n0.01 & 1.1\\% & 523 & $+$0.58 & .21 \\\\\n0.02 & 13.6\\% & 457 & $+$0.83 & .15 \\\\\n0.03 & 31.8\\% & 361 & $+$1.31 & .079 \\\\\n\\textbf{0.05} & \\textbf{60.3\\%} & \\textbf{210} & \\textbf{$+$2.86} & \\textbf{.004} \\\\\n0.10 & 83.9\\% & 85 & $+$3.69 & .034 \\\\\n0.15 & 93.2\\% & 36 & $+$4.15 & .11 \\\\\n0.20 & 96.4\\% & 19 & $+$4.59 & .13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\varepsilon$ robustness of selection F1.}\\label{app:epsilon_robustness}\nThe preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\\varepsilon$ to define MBR-style proximity in selection.\nTable~\\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\\varepsilon \\in [0, 0.2]$ for all signals and configurations.\nAt $\\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.\nSpearman $\\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\\varepsilon$ parameter affects only the selection analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\n\\label{tab:epsilon_robustness}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & Qwen & LLaMA & Qwen & LLaMA \\\\\n\\midrule\nSJ & 0.92 & 1.45 & 0.99 & 0.18 \\\\\nFK & 1.03 & 0.93 & 0.60 & 0.15 \\\\\nVC & 2.33 & 0.53 & 0.72 & 0.18 \\\\\nEM & 0.00 & 0.00 & 0.00 & 0.00 \\\\\nLP & 3.65 & 2.58 & 3.00 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Consistency-Stratified Selection Analysis}\\label{app:vc_quartile}\n\nTable~\\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\\Delta$ (gain over single-sample) for LP and SJ.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Selection $\\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}\n\\label{tab:vc_quartile}\n\\begin{tabular}{lcccc}\n\\toprule\nQuartile & Mean VC & LP $\\Delta$ & SJ $\\Delta$ & Oracle (pp) \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{NER}} \\\\\nQ1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\\\\nQ2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\\\\nQ3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\\\\nQ4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$^\\dagger$RE}} \\\\\nQ1 (low) & --- & $-$3.56 & --- & --- \\\\\nQ4 (high) & --- & $+$4.01 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:\n\\begin{itemize}\n\\item \\textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp---samples have already converged, leaving little room for any signal to improve selection.\n\\item \\textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, yielding inconsistent $\\Delta$ signs across quartiles.\n\\end{itemize}\n\nOn $^\\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp, suggesting LP can recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.\n\nOn CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), yielding $\\Delta{=}0$ universally---a ceiling effect even more extreme than SciERC Q4.\n\n\\section{Exploratory Extension to Relation Extraction}\\label{app:re_extension}\n\nWe extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.\nRE produces sets of (head, relation, tail) triples with partial overlap; 40\\% of RE instances receive zero F1, and entity span errors account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect (\\S\\ref{app:additional}).\nAll RE results use Qwen3-8B unless noted; single-seed ($\\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.\n\n\\paragraph{Quality estimation.}\nRE quality estimation is reported in Table~\\ref{tab:multiseed} (3-seed means).\nThe signal ranking differs from NER: VC leads ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal reflecting RE's higher sensitivity to per-sample scoring.\nRE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\\ref{fig:reliability}).\n\n\\paragraph{Selection.}\nTable~\\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.\nAt $N{=}16$ (Qwen3-4B, Table~\\ref{tab:re_n16_selection}), LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.\n\n\\paragraph{Scale ablation.}\nAt 4B scale (Qwen3-4B, $N{=}8$, $\\text{seed}{=}42$), RE quality estimation shows FK $\\rho{=}0.359$ and LP $\\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\\ $0.250$).\nSelection remains below single-sample on RE ($\\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.\n\n\\paragraph{Free-form decoding.}\nRE LP selection consistently reverses direction under free-form decoding ($+1.8{\\pm}0.1$~pp across 4 seeds vs.\\ $-0.9$~pp under constrained decoding at 8B; \\S\\ref{app:freeform_ablation}), suggesting constrained decoding's fixed template obscures LP signal in RE (\\S\\ref{app:mbr_discussion}).\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform single-sample on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{RE $N{=}16$ Selection Analysis}\\label{app:re_n16_selection}\n\nTable~\\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.\nAll four consistency signals underperform single-sample, with EM showing the largest deficit ($\\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).\nLP is the only positive signal ($\\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).\nEven the most favorable seed captures only ${\\sim}9\\%$ of the 17.1~pp oracle headroom.\nThis cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the persistent limitation of instance-level signals for candidate ranking across tested regimes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ greedy. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:re_n16_selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & F1 & $\\Delta$ (pp) & $p$(Fisher) \\\\\n\\midrule\nOracle & $.463{\\pm}.006$ & $+$17.1 & --- \\\\\n\\midrule\nLP & $\\mathbf{.299}{\\pm}.007$ & $+$0.7 & .058 \\\\\nVC & $.284{\\pm}.002$ & $-$0.8 & .973 \\\\\nFK & $.283{\\pm}.005$ & $-$0.9 & .985 \\\\\nSJ & $.281{\\pm}.005$ & $-$1.0 & .993 \\\\\nEM & $.277{\\pm}.007$ & $-$1.5 & .999 \\\\\n\\midrule\nGreedy & $.291{\\pm}.000$ & --- & --- \\\\\nRandom & $.262{\\pm}.001$ & $-$2.9 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{MBR Decoding and Task-Specific Interactions}\\label{app:mbr_discussion}\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy---the core of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Task-specific decoding interactions.}",
      "numLines": 250,
      "startLine": 449,
      "totalLines": 1183
    }
  },
  "sourceToolAssistantUUID": "93909477-5b9b-4168-aa3c-0d22d0a1326f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验设计**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics/Ref…",
  "leafUuid": "69d222eb-236c-4d2a-87aa-65128fec9d78",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Assistant

_source line 60 · 2026-05-17T07:08:41.816Z_

<details><summary>Logged reasoning block</summary>

```text
I've read most of the paper now. Let me also read the remaining parts of the appendix to see the free-form ablation results and the N-scaling selection data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69d222eb-236c-4d2a-87aa-65128fec9d78",
  "isSidechain": false,
  "requestId": "req_011Cb7ikHo2qTRjEhVM3KphD",
  "type": "assistant",
  "uuid": "c210fc2d-c625-4e4c-a314-bba49bfbc72b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo5Uqij7p92dpVF4LrZmfV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6701,
      "cache_read_input_tokens": 65480,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 65480,
          "cache_creation_input_tokens": 6701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6701
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T07:08:43.872Z_

<details open><summary>🔧 Tool call — Read · `toolu_01McQhekfnnBRJzwHoCvMMoM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 698,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c210fc2d-c625-4e4c-a314-bba49bfbc72b",
  "isSidechain": false,
  "requestId": "req_011Cb7ikHo2qTRjEhVM3KphD",
  "type": "assistant",
  "uuid": "9cba6972-0299-47cb-b754-262283bb1eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo5Uqij7p92dpVF4LrZmfV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6701,
      "cache_read_input_tokens": 65480,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 65480,
          "cache_creation_input_tokens": 6701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6701
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T07:08:43.878Z_

<details><summary>↩ Tool result · `toolu_01McQhekfnnBRJzwHoCvMMoM`</summary>

```text
698	\paragraph{Task-specific decoding interactions.}
699	The free-form ablation reveals divergent behavior across tasks.
700	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
701	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
702	This interaction does not generalize to NER, where selection remains negligible under both regimes.
703	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
704	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
705	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
706	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
707	
708	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
709	
710	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).
711	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
712	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
713	RE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\ $-0.68$~pp constrained.
714	The constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.
715	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
716	
717	\begin{table*}[t]
718	\centering
719	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
720	\label{tab:freeform_ablation}
721	
722	\vspace{2pt}
723	{\small\textsc{Panel A: Logprob Distribution}}
724	\vspace{2pt}
725	
726	\begin{tabular}{lccc}
727	\toprule
728	Metric & Constrained & Free-form & $\Delta$ \\
729	\midrule
730	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
731	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
732	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
733	\bottomrule
734	\end{tabular}
735	
736	\vspace{8pt}
737	
738	{\small\textsc{Panel B: Selection F1}}
739	\vspace{2pt}
740	
741	\begin{tabular}{llccc}
742	\toprule
743	Task & Method & Constrained & Free-form & $\Delta$ \\
744	\midrule
745	\multirow{3}{*}{NER}
746	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
747	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
748	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
749	\midrule
750	\multirow{3}{*}{RE}
751	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
752	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
753	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
754	\bottomrule
755	\end{tabular}
756	
757	\vspace{8pt}
758	
759	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
760	\vspace{2pt}
761	
762	\begin{tabular}{l ccc ccc}
763	\toprule
764	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
765	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
766	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
767	\midrule
768	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
769	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
770	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
771	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
772	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
773	\bottomrule
774	\end{tabular}
775	
776	\vspace{8pt}
777	
778	{\small\textsc{Panel D: Parse Rate (Free-form)}}
779	\vspace{2pt}
780	
781	\begin{tabular}{lc}
782	\toprule
783	Metric & Value \\
784	\midrule
785	Total samples          & 4408 \\
786	Parse rate             & 99.95\% \\
787	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
788	\bottomrule
789	\end{tabular}
790	
791	\end{table*}
792	
793	\paragraph{CoNLL NER free-form results.}
794	Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\pm}0.007$ across seeds---higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\% tied fraction under constrained decoding.
795	Free-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\ single-sample $0.904$ ($\Delta{=}{-}0.77$~pp).
796	Quality estimation under free-form decoding yields SJ $\rho{=}0.461$, EM $\rho{=}0.471$, LP $\rho{=}0.326$---comparable to constrained results (Table~\ref{tab:quality_estimation}).
797	The failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.25~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.
798	
799	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
800	
801	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
802	
803	\paragraph{Pairwise overlap.}
804	LP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
805	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
806	
807	\paragraph{Instance complexity drives failure.}
808	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
809	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher single-sample F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
810	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
811	
812	\begin{table}[t]
813	\centering
814	\small
815	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}
816	\label{tab:stable_failures}
817	\begin{tabular}{lcccc}
818	\toprule
819	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
820	\midrule
821	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
822	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
823	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
824	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
825	\bottomrule
826	\end{tabular}
827	\end{table}
828	
829	\paragraph{Flip instances.}
830	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
831	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
832	
833	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
834	
835	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
836	
837	\begin{table}[t]
838	\centering
839	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
840	\label{tab:n-scaling}
841	\small
842	\begin{tabular}{l ccc ccc}
843	\toprule
844	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
845	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
846	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
847	\midrule
848	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
849	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
850	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
851	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
852	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
853	\midrule
854	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
855	\bottomrule
856	\end{tabular}
857	\end{table}
858	
859	\begin{table}[t]
860	\centering
861	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
862	\label{tab:ranking-stability}
863	\small
864	\begin{tabular}{ll cc l}
865	\toprule
866	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
867	\midrule
868	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
869	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
870	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
871	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
872	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
873	\bottomrule
874	\end{tabular}
875	\end{table}
876	
877	\begin{table}[t]
878	\centering
879	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
880	\label{tab:sigma-comparison}
881	\small
882	\begin{tabular}{l cc cc}
883	\toprule
884	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
885	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
886	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
887	\midrule
888	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
889	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
890	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
891	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
892	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
893	\midrule
894	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
895	\bottomrule
896	\end{tabular}
897	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cba6972-0299-47cb-b754-262283bb1eb8",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "05a69c3b-64fa-4817-94f7-c98f564fdd75",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\paragraph{Task-specific decoding interactions.}\nThe free-form ablation reveals divergent behavior across tasks.\nOn RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.\nThe non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\\ $-0.68$~pp constrained.\nThe constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\paragraph{CoNLL NER free-form results.}\nExtending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\\pm}0.007$ across seeds---higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\\% tied fraction under constrained decoding.\nFree-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\\ single-sample $0.904$ ($\\Delta{=}{-}0.77$~pp).\nQuality estimation under free-form decoding yields SJ $\\rho{=}0.461$, EM $\\rho{=}0.471$, LP $\\rho{=}0.326$---comparable to constrained results (Table~\\ref{tab:quality_estimation}).\nThe failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.25~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), confirming a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher single-sample F1 (0.688 vs.\\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Greedy F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n\n\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
      "numLines": 200,
      "startLine": 698,
      "totalLines": 1183
    }
  },
  "sourceToolAssistantUUID": "9cba6972-0299-47cb-b754-262283bb1eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T07:08:50.200Z_

<details open><summary>🔧 Tool call — Read · `toolu_018hWnZ9zvNarqFnd52xDAjE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 897,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05a69c3b-64fa-4817-94f7-c98f564fdd75",
  "isSidechain": false,
  "requestId": "req_011Cb7ikuwAZGasMx9tJRMKD",
  "type": "assistant",
  "uuid": "0127378f-69a4-41ca-804c-7d435de2fdb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqwfb9ghLXLYj7JvpbhZVi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4966,
      "cache_read_input_tokens": 72181,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 72181,
          "cache_creation_input_tokens": 4966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4966
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T07:08:50.205Z_

<details><summary>↩ Tool result · `toolu_018hWnZ9zvNarqFnd52xDAjE`</summary>

```text
897	\end{table}
898	
899	Signal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.
900	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
901	
902	\paragraph{$N$-scaling: selection headroom vs.\ selection gain.}
903	Table~\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.
904	Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+19.2$~pp at $N{=}32$).
905	LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom reaches ${\sim}19$~pp---the best signal captures less than 5\% of the available improvement.
906	Degeneracy drops monotonically (44\% at $N{=}2$ to 4\% at $N{=}32$), yet reduced degeneracy does not unlock selection---consistent with the LoRA-rank ablation finding (\S\ref{sec:robustness_main}).
907	VC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.
908	
909	\begin{table}[t]
910	\centering
911	\small
912	\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, seed${=}42$).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
913	\label{tab:n_scaling_selection}
914	\begin{tabular}{ccccccccc}
915	\toprule
916	$N$ & Degen.\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\Delta$ \\
917	\midrule
918	2 & 44.1\% & $+$4.4 & $-$0.75 & $-$2.54 & $-$2.54 & $-$2.54 & $-$2.27 & $-$0.75 \\
919	4 & 22.4\% & $+$9.8 & $-$0.01 & $-$0.61 & $-$0.50 & $-$1.27 & $-$1.30 & $-$0.01 \\
920	8 & 12.4\% & $+$13.8 & $+$0.42 & $+$0.03 & $+$0.11 & $-$0.33 & $-$1.82 & $+$0.42 \\
921	16 & 6.8\% & $+$16.7 & $+$0.63 & $+$0.26 & $+$0.43 & $-$0.15 & $-$2.91 & $+$0.63 \\
922	32 & 4.0\% & $+$19.2 & $+$0.91 & $+$0.33 & $+$0.62 & $+$0.21 & $-$4.18 & $+$0.91 \\
923	\bottomrule
924	\end{tabular}
925	\end{table}
926	\footnotetext{$N$-scaling analysis uses subsampled evaluation on the full 551-instance test set. Absolute greedy F1 (0.614) differs from Table~\ref{tab:selection} (0.645) due to the subsampling procedure and instance weighting; relative trends are consistent.}
927	
928	\paragraph{Bootstrap significance at $N{=}32$.}
929	Table~\ref{tab:bootstrap_n32} reports bootstrap confidence intervals and $p$-values for selection at $N{=}32$ ($B{=}10{,}000$, $n{=}529$).
930	No signal achieves significant improvement over greedy at $\alpha{=}0.05$ (LP: $p{=}0.091$; FK: $p{=}0.101$), while VC is significantly \textit{worse} ($-4.36$~pp, $p{=}1.0$).
931	However, all signals except VC significantly outperform random selection ($p{<}0.001$, permutation test), confirming that the signals carry meaningful quality information yet fail to translate it into reliable selection gains.
932	The oracle gap ($+20.0$~pp, $p{<}0.001$) confirms substantial unrealized headroom.
933	
934	\begin{table}[t]
935	\centering
936	\small
937	\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\Delta$: selection gain vs.\ greedy. CI: 95\% bootstrap percentile interval. $p_{\text{greedy}}$: one-sided $p$-value vs.\ greedy; $p_{\text{rand}}$: permutation test vs.\ random selection.}
938	\label{tab:bootstrap_n32}
939	\begin{tabular}{lcccc}
940	\toprule
941	Signal & $\Delta$ (pp) & 95\% CI & $p_{\text{greedy}}$ & $p_{\text{rand}}$ \\
942	\midrule
943	LP & $+$0.95 & [$-$0.41, $+$2.34] & 0.091 & ${<}$0.001 \\
944	FK & $+$0.66 & [$-$0.36, $+$1.67] & 0.101 & ${<}$0.001 \\
945	SJ & $+$0.36 & [$-$0.66, $+$1.38] & 0.244 & ${<}$0.001 \\
946	EM & $+$0.22 & [$-$0.99, $+$1.44] & 0.355 & ${<}$0.001 \\
947	VC & $-$4.36 & [$-$6.26, $-$2.37] & 1.000 & 0.741 \\
948	\midrule
949	Oracle & $+$20.00 & [$+$17.98, $+$22.10] & ${<}$0.001 & --- \\
950	\bottomrule
951	\end{tabular}
952	\end{table}
953	
954	\section{Temperature Ablation}\label{app:t_ablation}
955	
956	Table~\ref{tab:t_ablation} reports the effect of sampling temperature on QE signals, oracle headroom, and output quality across four temperatures on SciERC NER.
957	
958	\begin{table}[t]
959	\centering
960	\small
961	\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\rho$ across four temperatures. $\kappa$: Fleiss' $\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}
962	\label{tab:t_ablation}
963	\begin{tabular}{ccccccc}
964	\toprule
965	$T$ & Oracle gap (pp) & SJ $\rho$ & LP $\rho$ & $\kappa$ & Sample F1 \\
966	\midrule
967	0.5 & $+$7.8 & 0.297 & 0.218 & 0.577 & 0.636 \\
968	0.8 & $+$10.5 & 0.359 & 0.253 & 0.451 & 0.622 \\
969	1.0 & $+$13.3 & 0.360 & 0.205 & ${\approx}$0.39 & ${\approx}$0.612 \\
970	1.2 & $+$13.0 & 0.377 & 0.196 & 0.356 & 0.594 \\
971	\bottomrule
972	\end{tabular}
973	\end{table}
974	
975	Oracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing at $T{=}1.2$ ($+13.0$~pp); the plateau suggests $T{=}1.0$ already approaches the diversity ceiling for constrained structured decoding.
976	Structural QE signals improve with temperature: SJ $\rho$ rises from $0.297$ ($T{=}0.5$) to $0.377$ ($T{=}1.2$), consistent with more diverse outputs providing richer pairwise evidence.
977	LP $\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades to $0.196$ at $T{=}1.2$.
978	This divergence confirms that LP compression is model-intrinsic: higher temperature increases between-instance LP variance (benefiting structural signals) but does not resolve within-instance compression, degrading LP's discriminative power.
979	Inter-sample agreement ($\kappa$) decreases monotonically ($0.577$ to $0.356$), confirming that higher temperature generates more diverse outputs; mean sample F1 also decreases ($0.636$ to $0.594$), reflecting the quality--diversity trade-off.
980	The $T{=}0.7$ and $T{=}1.0$ comparison in Table~\ref{tab:robustness} is consistent with the trends reported here.
981	
982	\section{Cross-Dataset OOD Analysis}\label{app:ood}
983	
984	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
985	
986	\begin{table}[t]
987	\centering
988	\small
989	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
990	\label{tab:ood}
991	\begin{tabular}{l ccc ccc}
992	\toprule
993	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
994	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
995	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
996	\midrule
997	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
998	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
999	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
1000	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
1001	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
1002	\bottomrule
1003	\end{tabular}
1004	\end{table}
1005	
1006	\paragraph{Wider-to-narrower schema transfer.}
1007	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
1008	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
1009	
1010	\paragraph{Narrower-to-wider schema transfer (excluded).}
1011	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
1012	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (single-sample NER F1${=}0.009$, RE F1${=}0.001$).
1013	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
1014	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
1015	
1016	\paragraph{Asymmetry interpretation.}
1017	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
1018	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
1019	
1020	\section{Verbalized Confidence}\label{app:verbalized_confidence}
1021	
1022	We evaluate verbalized confidence (VerbConf) as a second per-sample signal following \citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.
1023	Table~\ref{tab:verbconf} reports quality estimation and selection results.
1024	
1025	\begin{table}[t]
1026	\centering
1027	\small
1028	\caption{Verbalized confidence (VerbConf) vs.\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}
1029	\label{tab:verbconf}
1030	\begin{tabular}{l cc cc}
1031	\toprule
1032	 & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{CoNLL NER}} \\
1033	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
1034	Metric & VerbConf & LP & VerbConf & LP \\
1035	\midrule
1036	$\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\
1037	AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\
1038	Selection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\
1039	$\Delta$ vs.\ greedy & $-$2.45\,pp & $+$0.2\,pp & $-$1.93\,pp & $-$0.77\,pp \\
1040	\midrule
1041	Mean score & 8.58\,/\,10 & --- & 9.24\,/\,10 & --- \\
1042	Parse fail rate & 0.26\% & --- & 0\% & --- \\
1043	\bottomrule
1044	\end{tabular}
1045	\end{table}
1046	
1047	\paragraph{Severe overconfidence.}
1048	VerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.
1049	This compression is more severe than LP (which spans a 0.041-nat median range), confirming that score compression is a general property of model self-assessment, not an artifact of log-probability computation.
1050	
1051	\paragraph{QE--selection decoupling.}
1052	VerbConf achieves higher $\rho$ than LP on both datasets (SciERC: 0.297 vs.\ 0.205; CoNLL: 0.337 vs.\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\ 0.578; CoNLL: 0.747 vs.\ 0.753), yet yields the worst selection among all signals ($\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).
1053	This dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.
1054	The AUROC--$\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\rho$ at 0.337) reflects differing sensitivity to binary vs.\ ordinal discrimination.
1055	
1056	\section{LLaMA-3.2-3B Scale Ablation}\label{app:llama3b}
1057	
1058	To extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\ref{tab:llama3b}).
1059	
1060	\begin{table}[t]
1061	\centering
1062	\small
1063	\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}
1064	\label{tab:llama3b}
1065	\begin{tabular}{l cc cc}
1066	\toprule
1067	Signal & $\rho$ & AUROC & Sel.\ F1 & $\Delta$ vs.\ greedy \\
1068	\midrule
1069	VC & \textbf{.460} & .743 & 0.611 & $-$1.54\,pp \\
1070	SJ & .375 & .738 & \textbf{0.633} & $+$0.61\,pp \\
1071	EM & .334 & \textbf{.776} & --- & --- \\
1072	FK & .268 & .671 & 0.630 & $+$0.28\,pp \\
1073	LP & .266 & .633 & 0.628 & $+$0.12\,pp \\
1074	\midrule
1075	Greedy & --- & --- & 0.627 & --- \\
1076	Oracle & --- & --- & 0.763 & --- \\
1077	\bottomrule
1078	\end{tabular}
1079	\end{table}
1080	
1081	The $\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.
1082	AUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\rho$--AUROC dissociation noted in the main text.
1083	Despite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.
1084	
1085	\section{Few-NERD Full Results}\label{app:fewnerd}
1086	
1087	Table~\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).
1088	After gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\% receive zero F1 under greedy decoding.
1089	Instance degeneracy is 10.1\% (vs.\ 21\% on SciERC, 58\% on CoNLL).
1090	
1091	\begin{table}[t]
1092	\centering
1093	\small
1094	\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\ $\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\% confidence interval.}
1095	\label{tab:fewnerd_full}
1096	\begin{tabular}{lcccc}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0127378f-69a4-41ca-804c-7d435de2fdb8",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "30998d01-c8ab-4442-872a-8d6d2b645fb3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\end{table}\n\nSignal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER), confirming that additional samples stabilize structural signals more than LP.\n\n\\paragraph{$N$-scaling: selection headroom vs.\\ selection gain.}\nTable~\\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.\nOracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+19.2$~pp at $N{=}32$).\nLP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}19$~pp---the best signal captures less than 5\\% of the available improvement.\nDegeneracy drops monotonically (44\\% at $N{=}2$ to 4\\% at $N{=}32$), yet reduced degeneracy does not unlock selection---consistent with the LoRA-rank ablation finding (\\S\\ref{sec:robustness_main}).\nVC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, seed${=}42$).\\protect\\footnotemark\\ ``Best $\\Delta$'': highest selection gain across all 5 signals. Per-signal $\\Delta$ in pp vs.~greedy.}\n\\label{tab:n_scaling_selection}\n\\begin{tabular}{ccccccccc}\n\\toprule\n$N$ & Degen.\\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\\Delta$ \\\\\n\\midrule\n2 & 44.1\\% & $+$4.4 & $-$0.75 & $-$2.54 & $-$2.54 & $-$2.54 & $-$2.27 & $-$0.75 \\\\\n4 & 22.4\\% & $+$9.8 & $-$0.01 & $-$0.61 & $-$0.50 & $-$1.27 & $-$1.30 & $-$0.01 \\\\\n8 & 12.4\\% & $+$13.8 & $+$0.42 & $+$0.03 & $+$0.11 & $-$0.33 & $-$1.82 & $+$0.42 \\\\\n16 & 6.8\\% & $+$16.7 & $+$0.63 & $+$0.26 & $+$0.43 & $-$0.15 & $-$2.91 & $+$0.63 \\\\\n32 & 4.0\\% & $+$19.2 & $+$0.91 & $+$0.33 & $+$0.62 & $+$0.21 & $-$4.18 & $+$0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\footnotetext{$N$-scaling analysis uses subsampled evaluation on the full 551-instance test set. Absolute greedy F1 (0.614) differs from Table~\\ref{tab:selection} (0.645) due to the subsampling procedure and instance weighting; relative trends are consistent.}\n\n\\paragraph{Bootstrap significance at $N{=}32$.}\nTable~\\ref{tab:bootstrap_n32} reports bootstrap confidence intervals and $p$-values for selection at $N{=}32$ ($B{=}10{,}000$, $n{=}529$).\nNo signal achieves significant improvement over greedy at $\\alpha{=}0.05$ (LP: $p{=}0.091$; FK: $p{=}0.101$), while VC is significantly \\textit{worse} ($-4.36$~pp, $p{=}1.0$).\nHowever, all signals except VC significantly outperform random selection ($p{<}0.001$, permutation test), confirming that the signals carry meaningful quality information yet fail to translate it into reliable selection gains.\nThe oracle gap ($+20.0$~pp, $p{<}0.001$) confirms substantial unrealized headroom.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\\Delta$: selection gain vs.\\ greedy. CI: 95\\% bootstrap percentile interval. $p_{\\text{greedy}}$: one-sided $p$-value vs.\\ greedy; $p_{\\text{rand}}$: permutation test vs.\\ random selection.}\n\\label{tab:bootstrap_n32}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\Delta$ (pp) & 95\\% CI & $p_{\\text{greedy}}$ & $p_{\\text{rand}}$ \\\\\n\\midrule\nLP & $+$0.95 & [$-$0.41, $+$2.34] & 0.091 & ${<}$0.001 \\\\\nFK & $+$0.66 & [$-$0.36, $+$1.67] & 0.101 & ${<}$0.001 \\\\\nSJ & $+$0.36 & [$-$0.66, $+$1.38] & 0.244 & ${<}$0.001 \\\\\nEM & $+$0.22 & [$-$0.99, $+$1.44] & 0.355 & ${<}$0.001 \\\\\nVC & $-$4.36 & [$-$6.26, $-$2.37] & 1.000 & 0.741 \\\\\n\\midrule\nOracle & $+$20.00 & [$+$17.98, $+$22.10] & ${<}$0.001 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Temperature Ablation}\\label{app:t_ablation}\n\nTable~\\ref{tab:t_ablation} reports the effect of sampling temperature on QE signals, oracle headroom, and output quality across four temperatures on SciERC NER.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\\rho$ across four temperatures. $\\kappa$: Fleiss' $\\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}\n\\label{tab:t_ablation}\n\\begin{tabular}{ccccccc}\n\\toprule\n$T$ & Oracle gap (pp) & SJ $\\rho$ & LP $\\rho$ & $\\kappa$ & Sample F1 \\\\\n\\midrule\n0.5 & $+$7.8 & 0.297 & 0.218 & 0.577 & 0.636 \\\\\n0.8 & $+$10.5 & 0.359 & 0.253 & 0.451 & 0.622 \\\\\n1.0 & $+$13.3 & 0.360 & 0.205 & ${\\approx}$0.39 & ${\\approx}$0.612 \\\\\n1.2 & $+$13.0 & 0.377 & 0.196 & 0.356 & 0.594 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing at $T{=}1.2$ ($+13.0$~pp); the plateau suggests $T{=}1.0$ already approaches the diversity ceiling for constrained structured decoding.\nStructural QE signals improve with temperature: SJ $\\rho$ rises from $0.297$ ($T{=}0.5$) to $0.377$ ($T{=}1.2$), consistent with more diverse outputs providing richer pairwise evidence.\nLP $\\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades to $0.196$ at $T{=}1.2$.\nThis divergence confirms that LP compression is model-intrinsic: higher temperature increases between-instance LP variance (benefiting structural signals) but does not resolve within-instance compression, degrading LP's discriminative power.\nInter-sample agreement ($\\kappa$) decreases monotonically ($0.577$ to $0.356$), confirming that higher temperature generates more diverse outputs; mean sample F1 also decreases ($0.636$ to $0.594$), reflecting the quality--diversity trade-off.\nThe $T{=}0.7$ and $T{=}1.0$ comparison in Table~\\ref{tab:robustness} is consistent with the trends reported here.\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n\\label{tab:ood}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{SciERC$\\to$CoNLL}} & \\multicolumn{3}{c}{\\textbf{CoNLL$\\to$SciERC}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & In-dom. & $\\Delta$ & $\\rho$ & In-dom. & $\\Delta$ \\\\\n\\midrule\nVC & .469\\textsuperscript{***} & .379 & +.090 & +.105\\textsuperscript{*} & .379 & $-$.274 \\\\\nSJ & .378\\textsuperscript{***} & .360 & +.018 & $-$.186\\textsuperscript{***} & .360 & $-$.546 \\\\\nEM & .300\\textsuperscript{***} & .295 & +.005 & $-$.202\\textsuperscript{***} & .295 & $-$.497 \\\\\nFK & .285\\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\\\\nLP & .246\\textsuperscript{***} & .205 & +.041 & $-$.152\\textsuperscript{***} & .205 & $-$.357 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Wider-to-narrower schema transfer.}\nWhen the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\nThe wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.\n\n\\paragraph{Narrower-to-wider schema transfer (excluded).}\nThe reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.\nThe CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (single-sample NER F1${=}0.009$, RE F1${=}0.001$).\nUnder this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\nThese negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}), not evidence against signal utility.\n\n\\paragraph{Asymmetry interpretation.}\nThe directional asymmetry is driven by schema coverage: wider$\\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.\nThis extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\n\n\\section{Verbalized Confidence}\\label{app:verbalized_confidence}\n\nWe evaluate verbalized confidence (VerbConf) as a second per-sample signal following \\citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.\nTable~\\ref{tab:verbconf} reports quality estimation and selection results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\n\\label{tab:verbconf}\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{CoNLL NER}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & VerbConf & LP & VerbConf & LP \\\\\n\\midrule\n$\\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\\\\nAUROC & 0.681 & 0.578 & 0.747 & 0.753 \\\\\nSelection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\\\\n$\\Delta$ vs.\\ greedy & $-$2.45\\,pp & $+$0.2\\,pp & $-$1.93\\,pp & $-$0.77\\,pp \\\\\n\\midrule\nMean score & 8.58\\,/\\,10 & --- & 9.24\\,/\\,10 & --- \\\\\nParse fail rate & 0.26\\% & --- & 0\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Severe overconfidence.}\nVerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.\nThis compression is more severe than LP (which spans a 0.041-nat median range), confirming that score compression is a general property of model self-assessment, not an artifact of log-probability computation.\n\n\\paragraph{QE--selection decoupling.}\nVerbConf achieves higher $\\rho$ than LP on both datasets (SciERC: 0.297 vs.\\ 0.205; CoNLL: 0.337 vs.\\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\\ 0.578; CoNLL: 0.747 vs.\\ 0.753), yet yields the worst selection among all signals ($\\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).\nThis dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.\nThe AUROC--$\\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\\rho$ at 0.337) reflects differing sensitivity to binary vs.\\ ordinal discrimination.\n\n\\section{LLaMA-3.2-3B Scale Ablation}\\label{app:llama3b}\n\nTo extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\\ref{tab:llama3b}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\n\\label{tab:llama3b}\n\\begin{tabular}{l cc cc}\n\\toprule\nSignal & $\\rho$ & AUROC & Sel.\\ F1 & $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nVC & \\textbf{.460} & .743 & 0.611 & $-$1.54\\,pp \\\\\nSJ & .375 & .738 & \\textbf{0.633} & $+$0.61\\,pp \\\\\nEM & .334 & \\textbf{.776} & --- & --- \\\\\nFK & .268 & .671 & 0.630 & $+$0.28\\,pp \\\\\nLP & .266 & .633 & 0.628 & $+$0.12\\,pp \\\\\n\\midrule\nGreedy & --- & --- & 0.627 & --- \\\\\nOracle & --- & --- & 0.763 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.\nAUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\\rho$--AUROC dissociation noted in the main text.\nDespite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.\n\n\\section{Few-NERD Full Results}\\label{app:fewnerd}\n\nTable~\\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).\nAfter gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\\% receive zero F1 under greedy decoding.\nInstance degeneracy is 10.1\\% (vs.\\ 21\\% on SciERC, 58\\% on CoNLL).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\n\\label{tab:fewnerd_full}\n\\begin{tabular}{lcccc}",
      "numLines": 200,
      "startLine": 897,
      "totalLines": 1183
    }
  },
  "sourceToolAssistantUUID": "0127378f-69a4-41ca-804c-7d435de2fdb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验设计**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics/Ref…",
  "leafUuid": "30998d01-c8ab-4442-872a-8d6d2b645fb3",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Assistant

_source line 67 · 2026-05-17T07:08:55.604Z_

<details><summary>Logged reasoning block</summary>

```text
I've read enough of the paper to form a thorough review. Let me now also quickly look at what the ARR review form looks like for the official dimensions, and then I'll produce my review. Let me fetch the official review form page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30998d01-c8ab-4442-872a-8d6d2b645fb3",
  "isSidechain": false,
  "requestId": "req_011Cb7imNcHMhvvYarZgfav6",
  "type": "assistant",
  "uuid": "3294bb84-6e45-4a00-a401-b6b2cd09a799",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdHnxFFcWnGEANcK2VZwKD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6629,
      "cache_read_input_tokens": 77147,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 77147,
          "cache_creation_input_tokens": 6629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6629
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-17T07:08:56.610Z_

I've now read the full paper. Let me fetch the official ARR review form for the exact scoring rubric.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3294bb84-6e45-4a00-a401-b6b2cd09a799",
  "isSidechain": false,
  "requestId": "req_011Cb7imNcHMhvvYarZgfav6",
  "type": "assistant",
  "uuid": "7a469ad2-0240-4c1c-b1b7-14343129a5a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdHnxFFcWnGEANcK2VZwKD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6629,
      "cache_read_input_tokens": 77147,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 77147,
          "cache_creation_input_tokens": 6629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6629
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-17T07:08:57.255Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012AcN9yq4zfLdGtoCKc16Q9`</summary>

```json
{
  "query": "\"aclrollingreview.org/reviewform\" soundness excitement overall recommendation scale detailed rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a469ad2-0240-4c1c-b1b7-14343129a5a3",
  "isSidechain": false,
  "requestId": "req_011Cb7imNcHMhvvYarZgfav6",
  "type": "assistant",
  "uuid": "ca33ce92-e4cc-43b3-a9f0-9025d56df8bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdHnxFFcWnGEANcK2VZwKD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6629,
      "cache_read_input_tokens": 77147,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 77147,
          "cache_creation_input_tokens": 6629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6629
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-17T07:09:04.529Z_

<details><summary>↩ Tool result · `toolu_012AcN9yq4zfLdGtoCKc16Q9`</summary>

```text
Web search results for query: ""aclrollingreview.org/reviewform" soundness excitement overall recommendation scale detailed rubric"

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ARR Area Chair Guidelines","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"aclrollingreview/acguidelines.md at main · yoshitomo-matsubara/aclrollingreview","url":"https://github.com/yoshitomo-matsubara/aclrollingreview/blob/main/acguidelines.md"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"Program Chairs' Report on Peer Review at ACL 2023","url":"http://www.cs.umd.edu/~jbg/docs/2023_acl_peer_review_report.pdf"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"}]

Based on the search results from aclrollingreview.org, here's information about the review form's scoring rubric:

## Three Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Scale

The soundness score evaluates whether the paper is sufficiently sound and thorough, and whether it clearly states scientific claims and provides adequate support for them. The rubric includes the following scale points:

- 5 = Excellent: This study is one of the most thorough I have seen, given its type.
- 4 = Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.
- 3 = Acceptable: This study provides sufficient support for its main claims.

### Excitement Scale

Excitement is subjective and does not necessarily follow what is popular in the field. Papers may be perceived as transformational/innovative/surprising because they present conceptual breakthroughs or evidence challenging common assumptions/methods/datasets/metrics. The scale includes:

- 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference.
- 4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference.

### Overall Recommendation

The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca33ce92-e4cc-43b3-a9f0-9025d56df8bb",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "80fa56be-a2ee-40c5-b8a1-b37a0faed8f0",
  "toolUseResult": {
    "query": "\"aclrollingreview.org/reviewform\" soundness excitement overall recommendation scale detailed rubric",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LrY5iNC3cu8hFBkaRsYZFh",
        "content": [
          {
            "title": "ARR Reviewer Guidelines",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "Review Form",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "ACL 2023 Acceptance Recommendations - ACL 2023",
            "url": "https://2023.aclweb.org/blog/overall-recommendation/"
          },
          {
            "title": "ARR Area Chair Guidelines",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"
          },
          {
            "title": "Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}",
            "url": "https://aclanthology.org/2023.acl-long.report.pdf"
          },
          {
            "title": "aclrollingreview/acguidelines.md at main · yoshitomo-matsubara/aclrollingreview",
            "url": "https://github.com/yoshitomo-matsubara/aclrollingreview/blob/main/acguidelines.md"
          },
          {
            "title": "ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X",
            "url": "https://x.com/aclmeeting/status/1637827267173953540"
          },
          {
            "title": "Program Chairs' Report on Peer Review at ACL 2023",
            "url": "http://www.cs.umd.edu/~jbg/docs/2023_acl_peer_review_report.pdf"
          },
          {
            "title": "ACL’23 Peer Review Policies - ACL 2023",
            "url": "https://2023.aclweb.org/blog/review-acl23/"
          }
        ]
      },
      "Based on the search results from aclrollingreview.org, here's information about the review form's scoring rubric:\n\n## Three Scoring Dimensions\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n### Soundness Scale\n\nThe soundness score evaluates whether the paper is sufficiently sound and thorough, and whether it clearly states scientific claims and provides adequate support for them. The rubric includes the following scale points:\n\n- 5 = Excellent: This study is one of the most thorough I have seen, given its type.\n- 4 = Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.\n- 3 = Acceptable: This study provides sufficient support for its main claims.\n\n### Excitement Scale\n\nExcitement is subjective and does not necessarily follow what is popular in the field. Papers may be perceived as transformational/innovative/surprising because they present conceptual breakthroughs or evidence challenging common assumptions/methods/datasets/metrics. The scale includes:\n\n- 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference.\n- 4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference.\n\n### Overall Recommendation\n\nThe Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."
    ],
    "durationSeconds": 7.269991383000001
  },
  "sourceToolAssistantUUID": "ca33ce92-e4cc-43b3-a9f0-9025d56df8bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-17T07:09:44.563Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me compile my review. Based on the ARR review form, I need to score on:
- Soundness (1-5)
- Excitement (1-5)
- Overall Recommendation (1-5, where 5 = Consider for Award, 3.5/4 = Accept, 3 = Borderline, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit)

Let me write a thorough review focused on method rigor and experimental design as instructed.


The paper demonstrates strong experimental rigor with comprehensive testing across multiple datasets, model sizes, and random seeds, supported by solid statistical methods including bootstrap confidence intervals and equivalence testing. The core contribution—the correlation-selection gap and its three-layer diagnostic framework—is well-articulated and systematically validated, with honest acknowledgment of limitations like the low seed count. The authors present negative results carefully with appropriate caveats, and their degeneracy analysis provides genuine insight into the phenomenon.

On methodological grounds, the soft Jaccard denominator choice is well-justified by the data, the instance-level versus per-sample distinction is cleanly formalized, and the MBR/consensus-proximity equivalence is properly established. The reported within-instance correlation of ρ = 0.52 for MBR utility is compelling, though showing the full distribution rather than just the median would be more convincing. The primary analysis relies on a single seed, which they acknowledge, but the three-seed stability check with σ ≤ 0.026 provides reasonable reassurance about ranking consistency.

However, the correlation-selection gap phenomenon is demonstrated on only three datasets with a monotonic degeneracy gradient, which is a limited sample size for making cross-dataset claims—though the entity-type analysis within Few-NERD does expand this to eight cases. The LoRA rank ablation is more problematic: at rank 8, degeneracy drops to 7.2% with 16 percentage points of headroom, yet selection still fails. The paper argues this shows degeneracy is necessary but not sufficient, but the ablation actually conflates two variables—low degeneracy and LP compression both change together. To properly support the "not sufficient" claim, they'd need to show a case where degeneracy is low and LP compression isn't present, yet selection still fails. The Few-NERD results actually point in the opposite direction, suggesting that when degeneracy is genuinely low, the dynamics shift.

The free-form decoding ablation further complicates the "model-intrinsic compression" narrative: on NER it holds (std ratio 0.97), but on RE, free-form decoding recovers selection performance by 2.35 percentage points, indicating the phenomenon is task-dependent rather than universally intrinsic to the model. The non-tied subset analysis with ε=0.05 relies on post-hoc threshold selection, though the monotonic trends and Bonferroni correction provide some rigor despite the data-snooping concerns the authors acknowledge. The oracle headroom calculation using max F1 across samples is standard and unproblematic, while the sign test at n=529 across two seeds forms the core of the selection stability assessment.

However, there's a missing power analysis—with p=0.29 and effect size d=0.038, I need to determine what power this test actually has to detect a 1 percentage point improvement, which is crucial for interpreting the negative result. Additionally, Few-NERD uses only 3 training epochs versus 5 for SciERC, which could confound the degeneracy comparison between datasets. The evaluation protocols also vary across datasets (gold-filtered versus full-set, different N values) without always being transparent about these differences in the main text.

I'm working through several specific concerns: the "necessary but not sufficient" claim about LoRA rank=8 conflates two simultaneous changes—degeneracy drops while model quality also degrades from lower rank. The cross-dataset degeneracy gradient relies on just 3 datasets, which is too limited for the causal claims being made, though the entity-type analysis within Few-NERD (n=8) is more granular but still confounds entity difficulty with degeneracy. There's also an internal contradiction where the free-form decoding conclusion that "compression is model-intrinsic" conflicts with the RE results showing free-form actually does recover selection. Now I need to structure these critiques into a coherent review.

The statistical power issue is significant here—the paper doesn't report power analyses, and for the main SciERC selection result with such a small effect size and sample, the ability to detect even a 1 percentage point effect is probably insufficient. This is particularly problematic since the paper's core argument hinges on a negative result.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80fa56be-a2ee-40c5-b8a1-b37a0faed8f0",
  "isSidechain": false,
  "requestId": "req_011Cb7inRiLgVUdqBEoaNxsH",
  "type": "assistant",
  "uuid": "f2aa15ca-28c3-4254-8a85-30945c44913e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uns7kiEkcMVpebKXQfTPvP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 83776,
      "output_tokens": 1560,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1560,
          "cache_read_input_tokens": 83776,
          "cache_creation_input_tokens": 1085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1085
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-17T07:09:44.568Z_

我已通读全文和附录。现在撰写审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2aa15ca-28c3-4254-8a85-30945c44913e",
  "isSidechain": false,
  "requestId": "req_011Cb7inRiLgVUdqBEoaNxsH",
  "type": "assistant",
  "uuid": "5225c048-9498-4a98-b500-5026082562da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uns7kiEkcMVpebKXQfTPvP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 83776,
      "output_tokens": 1560,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1560,
          "cache_read_input_tokens": 83776,
          "cache_creation_input_tokens": 1085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1085
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-17T07:09:45.947Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UVGgGnyKbTU8UAkFjEAdiB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5225c048-9498-4a98-b500-5026082562da",
  "isSidechain": false,
  "requestId": "req_011Cb7inRiLgVUdqBEoaNxsH",
  "type": "assistant",
  "uuid": "0c10fdce-5d86-4920-9efd-cd4b4f9a0c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uns7kiEkcMVpebKXQfTPvP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 83776,
      "output_tokens": 1560,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1560,
          "cache_read_input_tokens": 83776,
          "cache_creation_input_tokens": 1085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1085
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-17T07:09:45.953Z_

<details><summary>↩ Tool result · `toolu_01UVGgGnyKbTU8UAkFjEAdiB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__review_reviewer_post_to_director"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c10fdce-5d86-4920-9efd-cd4b4f9a0c08",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "28cfa4e3-d8e6-4982-bd64-fac62d8f45e2",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__review_reviewer_post_to_director"
    ],
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "0c10fdce-5d86-4920-9efd-cd4b4f9a0c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 75 · 2026-05-17T07:09:45.974Z_

```json
{
  "parentUuid": "28cfa4e3-d8e6-4982-bd64-fac62d8f45e2",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7292c75c-fd52-4eb3-b02c-b6616c0c9bab",
  "timestamp": "2026-05-17T07:09:45.974Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 76 · 2026-05-17T07:09:50.417Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to write a comprehensive review. Let me compile my detailed review focused on method rigor and experimental design, and then post it to the director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7292c75c-fd52-4eb3-b02c-b6616c0c9bab",
  "isSidechain": false,
  "requestId": "req_011Cb7iqVLTDBzUXEGEUjJ7R",
  "type": "assistant",
  "uuid": "0271944e-c36b-4019-ad70-821641a49cbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRAUB21bNZ5DZSqZu2mwHc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1975,
      "cache_read_input_tokens": 84861,
      "output_tokens": 6167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6167,
          "cache_read_input_tokens": 84861,
          "cache_creation_input_tokens": 1975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1975
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-17T07:09:51.409Z_

审稿完成，正在提交报告给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0271944e-c36b-4019-ad70-821641a49cbd",
  "isSidechain": false,
  "requestId": "req_011Cb7iqVLTDBzUXEGEUjJ7R",
  "type": "assistant",
  "uuid": "606aae63-3554-4f59-8604-b82016edf78f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRAUB21bNZ5DZSqZu2mwHc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1975,
      "cache_read_input_tokens": 84861,
      "output_tokens": 6167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6167,
          "cache_read_input_tokens": 84861,
          "cache_creation_input_tokens": 1975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1975
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-17T07:12:13.906Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01F1hzPTnubcwXVSPe7bmF3S`</summary>

```json
{
  "text": "\n# Round 1 Review — Reviewer 1 (方法严谨性 + 实验设计)\n\n**Paper**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n\n---\n\n## Summary (2-3 句)\n\n本文系统评估了 5 种 confidence signals 在 LLM-based NER 中的 quality estimation 和 sample selection 能力，发现 QE 成功但 selection 失败（correlation-selection gap），并通过 instance degeneracy 和 LP compression 两个机制给出诊断。实验设计严谨度高于平均水准（多数据集、多模型、多 seed、bootstrap/TOST 统计检验），但部分核心 claim 的因果推断证据不足，跨数据集梯度 n=3 支撑的泛化结论需要审慎对待。\n\n---\n\n## Strengths\n\n1. **问题定义清晰且有贡献** (Section 1, 3.3): \"correlation-selection gap\" 的概念化有价值——将 QE 和 selection 明确解耦，指出一个被 prior work 忽略的 confound。instance-level vs per-sample 的形式化区分（Section 3.1）简洁且数��上正确。\n\n2. **实验设计的系统性** (Section 4): 4 个 NER benchmark 构成 difficulty gradient（WNUT-17 collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），每个数据集的角色清晰。两个模型族（Qwen3-8B, LLaMA-3.1-8B）加 4B/3B ablation 排除模型特异性。\n\n3. **统计方法论上佳** (Section 4.3, Appendix): Bootstrap CI（B=10,000）、paired sign test、TOST 等效性检验、Bonferroni 校正、Kendall's W 排名稳定性、Fisher 合并 p 值——统计工具选择恰当，且在负面结果中使用 TOST 避免了\"absence of evidence = evidence of absence\"的谬误。\n\n4. **三层诊断结构有说服力** (Section 4.3): (a) instance-level 信号 by construction 不能排名候选 → (b) MBR with aligned utility 因 degeneracy 失败 → (c) LP 有 per-sample 信息但被 compression 限制。逻辑递进清晰。\n\n5. **负面结果的审慎表达**: 论文多处使用\"inversely associated with\"而非\"causes\"，使用\"necessary but not sufficient\"限定 claim，Limitations 节详尽列举未覆盖条件。\n\n6. **Appendix 丰富且组织有序**: 涵盖 FK independence test、SJ normalizer robustness、ε robustness、thinking token impact、OOD analysis 等，大多数潜在反驳都有对应的 ablation 或 control。\n\n---\n\n## Weaknesses\n\n### [Must-Fix] W1: 跨数据集 degeneracy 梯度的因果推断基础薄弱 (n=3)\n\n- **位置**: Section 4.4 (Table 4), Section 5 \"Regime boundaries\", Figure 3\n- **问题**: 论文的核心 claim 之一是 \"LP selection effectiveness is inversely associated with degeneracy rate across datasets\"，但这一梯度仅基于 n=3 数据集（CoNLL 58% → SciERC 21% → Few-NERD 10%）。任何三个数据点的单调排列概率为 1/3!= 1/6，即使在随机条件下也有 16.7% 的概率出现单调趋势。\n- **补充**: 论文试图用 entity-type-level analysis（n=8, ρ=-0.881, p=0.004）加强论证，但 entity type 之间共享同一模型、同一 checkpoint、同一 inference pipeline，违反独立性假设。不同 entity type 的 degeneracy 差异可能源自 type frequency、schema complexity 等混淆变量，而非 degeneracy 本身直接导致 LP selection 差异。\n- **Figure 3 的 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合了两个粒度的观测**，统计上有问题：cross-dataset aggregates 和 per-entity-type points 的方差结构完全不同，不应直接 pool。\n- **为什么影响接收**: 如果 degeneracy 梯度的因果解释不成立，Contribution 3 的基础动摇。\n- **建议**: (a) 增加至少 2-3 个数据集的实验（如 OntoNotes、ACE05）扩大 n；(b) 用 Few-NERD 内 entity-type analysis 时，控制 type frequency 和 entity boundary difficulty 等混淆变量；(c) 不要 pool 不同粒度的观测到同一 correlation。\n\n### [Must-Fix] W2: \"Necessary but not sufficient\" claim 的 LoRA-rank ablation 存在混淆变量\n\n- **位置**: Section 4.5 \"LoRA-rank ablation\" (line: \"Low degeneracy is thus a necessary but not sufficient condition for selection\")\n- **问题**: LoRA rank=8 ablation 降低了 degeneracy (21% → 7.2%) 且增加了 oracle headroom (13.3 → 16.0 pp)，但 LP selection 仍失败。论文据此声称 degeneracy 是 \"necessary but not sufficient\"。但 LoRA rank=8 同时降低了模型能力（greedy F1: 0.645 → 0.640），改变了学到的 representation space。LP compression 在 rank=8 下可能因模型能力下降而加剧，而非因为 degeneracy 本身不充分。\n- **矛盾**: Few-NERD 在 10% degeneracy 下 LP selection 成功 (+1.36 pp)，而 rank=8 SciERC 在 7.2% degeneracy 下仍失败。如果 degeneracy 是唯一 gating factor，Few-NERD 的成功和 rank=8 SciERC 的失败之间的差异需要更好的解释。论文在 Section 4.4 简要提到 \"LP signal quality (ρ) provides an additional prerequisite\"，但这实质上是在说 degeneracy + LP quality 联���决定 selection，而非 degeneracy alone is necessary。\n- **为什么影响接收**: \"Necessary but not sufficient\" 是一个精确的逻辑声明；当前实验设计无法将 degeneracy 从 LP compression 中独立隔离。\n- **建议**: (a) 明确指出 LoRA rank ablation 同时改变了多个变量（degeneracy、model quality、LP compression degree），不能做 clean causal attribution；(b) 将 claim 弱化为 \"low degeneracy co-occurs with LP selection success, but rank-8 ablation shows it is not alone sufficient\"；(c) 最好提供 rank=8 下的 LP compression 统计（median LP range、tied fraction），以量化 compression 在两种 rank 下的变化。\n\n### [Should-Fix] W3: 负面结果的统计功效 (power) 未报告\n\n- **位置**: Section 4.3 (Table 3, \"LP achieves only 0.647, Δ=+0.2 pp, d=0.038, p=0.29\")\n- **问题**: 论文的中心论点是负面结果（selection 不显著优于 greedy）。对于负面结果，需要报告 power analysis：在当前样本量 (n=529) 和 seed 数量 (2) 下，检测 1 pp 效应（一个实际有意义的改进）的统计功效是多少？如果 power 很低（如 <50%），则 p=0.29 无法区分 \"真的没效果\" 和 \"效果存在但检测不到\"。\n- **TOST 部分缓解了这个问题** (Appendix D)，但 TOST 使用的 δ=2pp (internal anchor) 是否过宽？externally anchored δ=1.0pp 下，SciERC 未通过 TOST。\n- **为什么影响评分**: 虽然 TOST 是好的补充，但主文没有明确讨论 power，可能误导读者认为 \"p>0.05\" 等同于 \"确认无效果\"。\n- **建议**: 在 main text 或 appendix 中加入 post-hoc power analysis，报告当前设计检测 Δ=1pp 的 power；或者明确指出 Few-NERD (n=32,565) 的结果 (LP +1.36 pp, p<0.001) 才是 definitive evidence，SciERC 的 non-significance 可能受限于 power。\n\n### [Should-Fix] W4: \"Compression is model-intrinsic\" 的结论与 RE 结果矛盾\n\n- **位置**: Section 5 \"Ablation: free-form decoding\" + Appendix H (Table 8)\n- **问题**: 论文 NER free-form ablation 发现 LP 分布几乎不变 (std ratio 0.97)，据此声称 \"compression is model-intrinsic rather than constraint-imposed\"。但 RE 的 free-form decoding 显著恢复了 LP selection (+2.35 pp, p=0.025)，直接证明 constraints DO compress LP for RE。\n- **论文在 Section 5 最后简要提到这一分歧**，但 Abstract 和 Introduction 中 \"compression is model-intrinsic\" 的 framing 没有 qualification。读者如果只看主文可能误以为这是普适结论。\n- **为什么影响评分**: 论文的诊断框架混淆了 task-specific behavior 和 universal mechanism。\n- **建议**: (a) 将主文 claim 限定为 \"for NER, compression is model-intrinsic; for RE, constraint-imposed mechanisms contribute significantly\"；(b) 在 Abstract 或 Introduction 的 diagnostic chain 描述中加入 task qualifier。\n\n### [Should-Fix] W5: Primary seed (seed=42) 的代表性与 selection 实验的 2-seed 限制\n\n- **位置**: Section 4.1 footnote 4 (\"Quality estimation uses a single primary seed; selection uses 2-seed averages\")\n- **问题**: QE 主结果仅 1 seed，selection 仅 2 seeds。虽然 Table 6 的 3-seed stability test 显示 σ≤0.026 for ρ rankings，但 selection F1 的 seed variance 未被同样充分量化。Table 3 报告的 selection F1 σ（如 LP: ±0.005）基于仅 2 seeds 的极差，这不是可靠的 variance estimate。\n- **Few-NERD 是 1-seed result** (Table 4)，尽管 n=32,565 提供了足够 statistical power，但 systematic bias（如训练 seed 影响 degeneracy rate）仍可能存在。\n- **建议**: 至少为 Few-NERD 的核心 selection 结果 (LP +1.36 pp) 添加 2-3 seed replication；或者在 Limitations 中更明确指出 selection 结果的 seed coverage 比 QE 更有限。\n\n### [Should-Fix] W6: Few-NERD 训练配置差异未充分讨论\n\n- **位置**: Appendix L (\"3 epochs\" for Few-NERD vs. 5 epochs for SciERC/CoNLL)\n- **问题**: Few-NERD 仅训练 3 epochs（vs. 其他数据集的 5 epochs），这可能直接导致 lower degeneracy（更少训练 → 更弱模型 → 更多 diversity）。如果 Few-NERD 的低 degeneracy 部分源自 under-training 而非数据集固有特性，则 degeneracy-selection 关系的因果方向被混淆。\n- **论文在 Discussion 中提到** \"dataset-specific factors (number of entity types, semantic overlap) also modulate the rate\"，但没有排除 training epoch 差异这一 confound。\n- **建议**: 在 appendix 中添加 epoch sensitivity 分析（如 Few-NERD 5 epoch 的 degeneracy rate），或明确讨论为何使用 3 epochs（early stopping? 收敛?）。\n\n### [Minor] W7: Soft Jaccard 分母选择的 claim 缺乏完整表达\n\n- **位置**: Section 3.2, Equation 4, footnote\n- **问题**: 论文声称 max vs union normalizer 差异 Δρ<0.01，并在 Appendix (Table 5) 给出了 6 个 model-dataset combinations 的证据。这实际上是充分的。但 footnote 的表述 \"nearly identical rankings (Δρ<0.01; Table X)\" 暗示这是所有条件下的 bound，而表中最大差异是 0.009——距 0.01 仅一个量级，更准确的表述是 \"|Δρ| ��� 0.009\"。\n- **建议**: 微调措辞精度即可。\n\n### [Minor] W8: Table 3 与 Table 4 的 greedy F1 不一致可能困惑读者\n\n- **位置**: Table 3 (SciERC greedy=0.645), Table 4 (SciERC greedy=0.614)\n- **问题**: 两表使用不同 evaluation protocol (gold-filtered n=529 vs. full-set n=551)，导致同一模型的 greedy F1 差 3.1 pp。虽然 Table 4 有脚注解释，但读者在主文中连续看到两个不同的 baseline 数字时容易困惑。\n- **建议**: 统一 evaluation protocol，或在 Table 4 同时报告 gold-filtered 数字。\n\n---\n\n## Questions (需要作者澄清)\n\n**Q1**: Section 4.5 LoRA rank=8 ablation 中，LP 的 median within-instance range 是多少？如果 rank=8 下 LP range 显著小于 rank=32 下的 0.041 nats，则 selection failure 可归因于更严重的 compression 而非 degeneracy 本身不充分���\n\n**Q2**: Few-NERD 训练为何仅 3 epochs？是否有 early stopping 或 validation loss plateau 的证据？5 epochs 下的 degeneracy rate 是多少？\n\n**Q3**: Table 3 的 sign test 使用的是 instance-level 配对（对每个 instance 比较 LP-selected F1 vs greedy F1），还是 corpus-level 比较？如果是 instance-level，n=529 × 2 seeds = 1058 paired observations 应该有更强的 power。\n\n**Q4**: Within-instance SJ-F1 ρ=0.52 (Section 5) 报告为 median；distribution 如何？有多少比例的 non-degenerate instances 有 ρ<0？如果大量 instances 的 within-instance correlation 为负或接近零，则 \"well-aligned utility\" 的 claim 需要 qualify。\n\n**Q5**: Entity-type-level degeneracy-LP gain 分析（Appendix, ρ=-0.881, p=0.004, n=8）中，是否考虑过 entity type frequency 或 average entity count per sentence 作为 confound？高频类型可能同时有 higher degeneracy 和 lower selection gain，但因果机制可能是 frequency → model confidence → degeneracy + LP compression，而非 degeneracy → LP failure。\n\n---\n\n## Missing References\n\n1. **Best-of-N with process reward models**: Lightman et al. (2024) \"Let's Verify Step by Step\" 在 math reasoning 中展示了 verifier-based BoN 的 scaling law——与本文\"需要 learned verifier\"的结论直接相关，已引用但可更深入对比。\n2. **Self-consistency for structured prediction beyond NER**: Yoran et al. (2023) \"Answering Questions by Meta-Reasoning over Multiple Chains of Thought\" 和 Li et al. (2023) \"Making Language Models Better Reasoners with Step-Aware Verifier\" 在 structured reasoning 中有类似 gap 的发现。\n3. **Diversity in fine-tuned models**: Zhang et al. (2024) \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters\" (DeepMind) 讨论了 fine-tuned model 的 diversity collapse 与 test-time compute 的关系——直接相关。\n4. **MBR for structured prediction**: Eikema et al. (2025) \"Structured MBR\" 已引用但可更详细讨论为何 IE 的 bag-of-unit mismatch 比 MT 更严重。\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- 信息密度高，四个必答问题都有覆盖。\n- \"correlation-selection gap\" 概念在 Abstract 中引入但未定义（主文 Section 4.3 才定义），建议用一句简短释义。\n- 数字选择合理（ρ, AUROC, pp gains, p values）。\n\n### Introduction\n- 叙事线清晰：从 self-consistency 的成功切入 NER 的结构性挑战。\n- Contribution 3 \"Degeneracy as a regime boundary\" 的 claim 在 Introduction 中比实际证据更强（写作是 \"inversely associated\" 但 structure 暗示因果）。\n\n### Method (Section 3)\n- 形式化清晰。5 个 signal 的数学定义完整且正确。\n- Fleiss' κ 的 adaptation 有 independence concern（已在 Appendix B 用 permutation test 验证，充分）。\n- MBR/consensus-proximity 的等价性证明 (Appendix C, LOO-SJ) 是好的补充。\n\n### Experiments (Section 4)\n- 数据集选择合理且角色分工清晰。\n- 训练细节 (Appendix E, Table 7) 充分：LoRA config、optimizer、batch size、epoch 均报告。\n- vLLM + XGrammar constrained decoding 描述清楚；但 vLLM 版本号未报告（影响 reproducibility）。\n\n### Discussion (Section 5)\n- 这一节承载了大量 ablation 和 diagnostic 结果，密度极高。\n- Entity-token LP ablation 的 negative result 是好的：排除了 format-token dilution 作为 primary cause。\n- Signal combination 失败（logistic regression、MLP、RF）有力支撑了 \"feature space bottleneck\" 的结论。\n- \"Practical considerations\" 段落实用价值高（N=8 suffices for QE, cost-benefit for selection is unfavorable）。\n\n### Limitations\n- 全面且诚实（scale limitation、seed coverage、untested verifier、ε post-hoc choice）。\n- 建议补充: power analysis limitation、Few-NERD epoch confound。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claims 有充分支撑（QE works, selection fails），但核心因果诊断（degeneracy gates LP selection）的证据基础偏薄（cross-dataset n=3, entity-type confounds, LoRA ablation 混淆变量）。统计方法使用恰当。 |\n| Excitement | 3.5/5 | \"Correlation-selection gap\" 是 useful conceptual contribution，对 test-time compute scaling 社区有 immediate practical value（告诉 practitioner 何时 BoN 不工作）。但核心发现是 negative result + diagnostic，novelty 在于 framing 而非 new method。 |\n| Reproducibility | 4/5 | 训练 config 完整 (Table 7)，prompt template 提供，constrained decoding 细节清楚。缺 vLLM 版本号，缺部分配置的 exact random seeds for selection experiments。Code release upon acceptance 声明。 |\n\n---\n\n## Overall Score\n\n**Borderline Accept (3.5/5)**\n\n论文的实验工作量大、统计处理严谨、negative results 的报告方式远超平均水平。\"Correlation-selection gap\" 的概念化和三层诊断对社区有价值。主要扣分来自：(1) 核心因果 claim（degeneracy as regime boundary）的证据基础偏弱（n=3 datasets, confounded ablation）；(2) \"model-intrinsic compression\" claim 与 RE 结果矛盾但主文未充分 qualify。如果作者能在 rebuttal 中：(a) 提供 LoRA rank=8 下的 LP compression statistics，(b) 澄清 Few-NERD epoch confound，(c) 弱化/qualify 因果语言，我倾向接收。\n\n---\n\n## Confidence\n\n**4/5** — 我对方法论和统计分析的评估有信心；对 NER/IE 领域的 related work coverage 有较好把握，但未验证所有 appendix 中的数值计算。\n",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "606aae63-3554-4f59-8604-b82016edf78f",
  "isSidechain": false,
  "requestId": "req_011Cb7iqVLTDBzUXEGEUjJ7R",
  "type": "assistant",
  "uuid": "b8620e4c-fea0-48f7-b1bb-a66fb46ca018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRAUB21bNZ5DZSqZu2mwHc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1975,
      "cache_read_input_tokens": 84861,
      "output_tokens": 6167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6167,
          "cache_read_input_tokens": 84861,
          "cache_creation_input_tokens": 1975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1975
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 79_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验设计**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics/Ref…",
  "leafUuid": "b8620e4c-fea0-48f7-b1bb-a66fb46ca018",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Runtime record

_source line 80_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Tool result

_source line 81 · 2026-05-17T07:12:17.847Z_

<details><summary>↩ Tool result · `toolu_01F1hzPTnubcwXVSPe7bmF3S`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8620e4c-fea0-48f7-b1bb-a66fb46ca018",
  "isSidechain": false,
  "promptId": "9cc30cd1-ffce-43b6-84df-cabae5e505ee",
  "type": "user",
  "uuid": "7eb5c9f0-c703-477a-a97a-e75b9d060a1c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "b8620e4c-fea0-48f7-b1bb-a66fb46ca018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 82_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Runtime record

_source line 83 · 2026-05-17T07:14:40.207Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T07:14:40.207Z",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "content": "[Round 1 审稿请求]:\n## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Overall Score**: Borderline reject (leaning Findings), 3/5\n**Confidence**: 4/5\n\n**Strengths**:\nS1. 问题 framing 清晰且有价值\nS2. 实验设计全面且系统\nS3. 统计严谨性高\nS4. Negative result 的论证逻辑完整\nS5. Related work 覆盖面广（59 篇引用）\n\n**Weaknesses**:\n\n**W1 [Must-Fix]** 核心概念 \"correlation-selection gap\" 的新颖性有限。本质上是已知 observation 的 repackaging：(1) instance-level signals 不能做 per-sample ranking 是 trivial by definition；(2) fine-tuned models 的 diversity collapse 是已知现象 (Kirk et al., 2024)；(3) LP compression 是 specific but minor。三者组合的诊断价值有余，但是否构成 EMNLP 主会议长文的贡献量存疑。\n\n**W2 [Must-Fix]** \"Instance degeneracy\" 作为概念贡献的独立性不足。degeneracy 不是 \"failure mechanism\" 而是 model success 的 natural consequence。CoNLL 58% degeneracy = 91% F1（模型很好当然一致）；Few-NERD 10% = 75% F1（模型 underfit）。\"degeneracy gates LP selection\" 本质等价于 \"LP selection only works when the model is bad enough to produce diverse wrong answers\"。\n\n**W3 [Must-Fix]** 缺乏任何可操作的 positive contribution。全部 takeaway 是 \"需要 trained verifiers\"，但不训练 verifier、不提出新 signal、唯一 remedy (entity-token LP) 失败。纯诊断性论文需要极强 insight novelty 来补偿。\n\n**W4 [Should-Fix]** em-dash 过度使用（约 90 处），AI 写作风格痕迹。\n\n**W5 [Should-Fix]** Abstract 和 Introduction 过度堆砌数字（Abstract 10 行含 15+ 个数字），报告风格重于故事风格。\n\n**W6 [Should-Fix]** 与 Yao et al. (2026) 的增量贡献需更明确差异化。\n\n**W7 [Should-Fix]** Missing reference: Byerly & Khashabi (2024) \"Self-Consistency Falls Short\"。\n\n**W8 [Should-Fix]** Discussion section 过长（2+ 页），部分内容适合移入 Appendix。\n\n**M1-M5**: \"leverage\" 用词、Abstract 缩写未定义 (NER/MBR)、Table 3 EM/VC 无 p 值未解释、Figure 2 \"~15%\" 不精确、em-dash vs en-dash 区分。\n\n**Questions**:\nQ1. Few-NERD 低 degeneracy (10%) 和高 F1 (75%) 是否因 8 entity types（vs CoNLL 4 types）导致 output space 更大？如果是，degeneracy 主要是 output space size 的函数。\nQ2. LoRA rank=8 degeneracy 7% 但 selection 失败——degeneracy 是否不是 \"gating factor\"？\nQ3. 70B+ 模型是否 degeneracy 更高？如果是，整个 research direction 是否无望？\nQ4. Supervised verifier 只用 5 个 signal 做 features，加入 token-level features 能否 close gap？\n\n**Missing References**: Byerly & Khashabi (2024)、CRF-based calibration (Lafferty et al.)、Diverse Beam Search (Vijayakumar et al., 2016)\n\n**官方维度打分**: Soundness 4/5, Excitement 2.5/5, Reproducibility 4/5\n\n---\n\n请对 W1-W8、M1-M5、Q1-Q4 逐条回应。"
}
```

---

### Runtime record

_source line 84 · 2026-05-17T07:14:40.208Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T07:14:40.208Z",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

## Round 2

2 recorded events

### User

_source line 85 · 2026-05-17T07:14:40.199Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eb5c9f0-c703-477a-a97a-e75b9d060a1c",
  "isSidechain": false,
  "promptId": "e569eff4-e4f3-4bac-baec-9c1df028af05",
  "type": "user",
  "isMeta": true,
  "uuid": "2cf36455-a937-4388-8580-8b1a03fc9f3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-17T07:14:40.199Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cf36455-a937-4388-8580-8b1a03fc9f3f",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "28f4d272-b4b2-4051-acf2-53a6cc1fedb3",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "ef38711f-8af4-4f7e-aefb-48a53ac79710",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

## Round 3

6 recorded events

### User

_source line 87 · 2026-05-17T07:14:40.282Z_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。

---

### Reviewer 2 完整审稿意见

**Overall Score**: Borderline reject (leaning Findings), 3/5
**Confidence**: 4/5

**Strengths**:
S1. 问题 framing 清晰且有价值
S2. 实验设计全面且系统
S3. 统计严谨性高
S4. Negative result 的论证逻辑完整
S5. Related work 覆盖面广（59 篇引用）

**Weaknesses**:

**W1 [Must-Fix]** 核心概念 "correlation-selection gap" 的新颖性有限。本质上是已知 observation 的 repackaging：(1) instance-level signals 不能做 per-sample ranking 是 trivial by definition；(2) fine-tuned models 的 diversity collapse 是已知现象 (Kirk et al., 2024)；(3) LP compression 是 specific but minor。三者组合的诊断价值有余，但是否构成 EMNLP 主会议长文的贡献量存疑。

**W2 [Must-Fix]** "Instance degeneracy" 作为概念贡献的独立性不足。degeneracy 不是 "failure mechanism" 而是 model success 的 natural consequence。CoNLL 58% degeneracy = 91% F1（模型很好当然一致）；Few-NERD 10% = 75% F1（模型 underfit）。"degeneracy gates LP selection" 本质等价于 "LP selection only works when the model is bad enough to produce diverse wrong answers"。

**W3 [Must-Fix]** 缺乏任何可操作的 positive contribution。全部 takeaway 是 "需要 trained verifiers"，但不训练 verifier、不提出新 signal、唯一 remedy (entity-token LP) 失败。纯诊断性论文需要极强 insight novelty 来补偿。

**W4 [Should-Fix]** em-dash 过度使用（约 90 处），AI 写作风格痕迹。

**W5 [Should-Fix]** Abstract 和 Introduction 过度堆砌数字（Abstract 10 行含 15+ 个数字），报告风格重于故事风格。

**W6 [Should-Fix]** 与 Yao et al. (2026) 的增量贡献需更明确差异化。

**W7 [Should-Fix]** Missing reference: Byerly & Khashabi (2024) "Self-Consistency Falls Short"。

**W8 [Should-Fix]** Discussion section 过长（2+ 页），部分内容适合移入 Appendix。

**M1-M5**: "leverage" 用词、Abstract 缩写未定义 (NER/MBR)、Table 3 EM/VC 无 p 值未解释、Figure 2 "~15%" 不精确、em-dash vs en-dash 区分。

**Questions**:
Q1. Few-NERD 低 degeneracy (10%) 和高 F1 (75%) 是否因 8 entity types（vs CoNLL 4 types）导致 output space 更大？如果是，degeneracy 主要是 output space size 的函数。
Q2. LoRA rank=8 degeneracy 7% 但 selection 失败——degeneracy 是否不是 "gating factor"？
Q3. 70B+ 模型是否 degeneracy 更高？如果是，整个 research direction 是否无望？
Q4. Supervised verifier 只用 5 个 signal 做 features，加入 token-level features 能否 close gap？

**Missing References**: Byerly & Khashabi (2024)、CRF-based calibration (Lafferty et al.)、Diverse Beam Search (Vijayakumar et al., 2016)

**官方维度打分**: Soundness 4/5, Excitement 2.5/5, Reproducibility 4/5

---

请对 W1-W8、M1-M5、Q1-Q4 逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28f4d272-b4b2-4051-acf2-53a6cc1fedb3",
  "isSidechain": false,
  "promptId": "e569eff4-e4f3-4bac-baec-9c1df028af05",
  "type": "user",
  "uuid": "43805a85-3d20-4f6a-8705-2974ff31fe2e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 88 · 2026-05-17T07:15:14.010Z_

<details><summary>Logged reasoning block</summary>

```text
Reviewer 2 raises several interesting points. Let me go through each one systematically, comparing against what I found in the paper during my own review. I need to provide [AGREE] or [REBUT] for each weakness and question, citing specific evidence from the paper.

Let me think through each:

**W1**: "correlation-selection gap" novelty is limited - repackaging of known observations.
- The claim that instance-level signals can't rank per-sample is indeed trivial by definition. The paper acknowledges this.
- Diversity collapse is known (Kirk et al. 2024 is cited).
- But the COMBINATION and the systematic empirical demonstration across a difficulty gradient IS new. 

The paper's real contribution is synthesizing these known pieces into a unified framework specifically for structured IE, supported by empirical evidence across different difficulty levels. I partially agree the novelty lies in the demonstration and framing rather than individual observations, but I'd push back on calling it pure repackaging.

**W2**: Degeneracy as model success, not failure mechanism.
- This is a sharp observation. CoNLL's 58% degeneracy with 91% F1 suggests the model is simply performing well. Few-NERD's 10% degeneracy with 75% F1 indicates less convergence.
- The Few-NERD results actually support the paper's point here—the lower degeneracy correlates with lower performance, which contradicts the idea that degeneracy is just a sign of success.
- The 4B vs 8B comparison on SciERC is particularly telling: both models achieve similar performance (~65% F1) but show very different degeneracy rates (10.4% vs 21%), suggesting model size and dataset characteristics matter independently of performance.
- I think the paper has stronger evidence here than R2's framing acknowledges.

**W3**: No positive contribution.
- Fair criticism for a top-tier venue, since the paper is purely diagnostic. That said, negative or diagnostic results do get accepted at *ACL conferences when they reveal something meaningful about how methods fail or behave.
- The paper does offer some actionable takeaways—using quality estimation signals rather than selection, and recognizing that loss-based pruning works better in low-degeneracy settings—though I'd agree it's borderline for main conference standards.

**W4**: Excessive em-dashes and AI-like writing style.
- This is a presentation issue rather than a scientific one, but if there really are ~90 em-dashes throughout, it does affect readability and professionalism.

**W5**: Abstract is too number-dense.
- Valid stylistic concern; the Abstract packs in too many metrics and makes it harder to extract the main message.

**W6**: Differentiation from Yao et al. (2026).
- The Related Work does address this—Yao et al. focus on consistency-accuracy tradeoffs in hard-prompting, while this paper extends to fine-tuned models, separates quality estimation from selection, and diagnoses failure modes. The distinction exists but could be articulated more clearly.

**W7**: Missing Byerly & Khashabi (2024) reference.
- I'm not familiar with this paper, so I can't verify if it's real or hallucinated. I'll be cautious about taking a strong stance here.

**W8**: Discussion section is overstuffed.
- I see the density—it covers many ablations—but most of the content feels necessary. Some material on signal combinations and practical considerations could shift to the appendix.

**Q1**: Output space size as a driver of degeneracy.
- That's a compelling hypothesis. Few-NERD has 8 entity types while CoNLL has 4, so larger type inventories create more possible entity configurations and make identical outputs less likely. The paper does touch on this in Section 5 when mentioning entity types and semantic overlap as modulators.

**Q2**: The LoRA rank=8 case shows 7% degeneracy but selection still fails.
- This points to the same underlying tension.

The paper's "necessary but not sufficient" framing holds up with this data, though the confounds I flagged earlier—LP compression persisting across conditions—mean the ablation doesn't cleanly isolate degeneracy as the sole factor.

**Q3**: Larger models show higher degeneracy.
- That's a legitimate concern, but the paper acknowledges it as an open question rather than claiming their findings scale universally.

**Q4**: A supervised verifier with richer token-level features would be more powerful.
- True, the current verifier relies on just five scalar signals, which is a real limitation of the diagnostic approach. Though the paper frames this as testing whether information exists in those specific signals rather than building an optimal verifier.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43805a85-3d20-4f6a-8705-2974ff31fe2e",
  "isSidechain": false,
  "requestId": "req_011Cb7jDBD9tGuaRQ6HGSMNX",
  "type": "assistant",
  "uuid": "d013713b-4e84-463d-9184-6d21ea80a59e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjKx9FNxe864f4ZZaXWHf9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1255,
      "cache_read_input_tokens": 93076,
      "output_tokens": 5331,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5331,
          "cache_read_input_tokens": 93076,
          "cache_creation_input_tokens": 1255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1255
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-17T07:16:44.290Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01Wox6YPFPzGVTpLCnAfaigV`</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见逐条回应\n\n---\n\n## Weaknesses 回应\n\n**[REBUT] R2-W1: \"Correlation-selection gap\" 新颖性有限**\n\nR2 称三层诊断是已知 observation 的 repackaging。我部分不同意：\n\n(1) \"Instance-level signals 不能做 per-sample ranking 是 trivial by definition\" — 表面上 trivial，但 prior work（Yao et al. 2026; Vashurin et al. 2025 CoCoA; Taubenfeld et al. 2025 CISC）直接用 consistency signals 做 selection，说明社区并未普遍认识到这一区分。论文 Section 1 第二段明确指出 \"Prior work on confidence estimation for LLM-based IE has conflated quality estimation with sample selection\"。如果是 trivial，这些 prior work 不应该存在。\n\n(2) \"Diversity collapse 是已知现象\" — Kirk et al. (2024) 讨论的是 RLHF 下的 diversity collapse 作为 alignment tax；本文的 instance degeneracy 是 supervised fine-tuning 下的量化现象，且关键贡献不在于发现 degeneracy 存在，而在于量化其与 selection headroom 的具体关系（Table 5: 21% constant F1 + 13% constant utility = 34% instances 完全没有 selection room）。\n\n(3) 但我同意 R2 关于 \"是否构成 EMNLP 主会议长文贡献量\" 的质疑。纯诊断性 negative result 论文需要很强的 insight density。论文在 diagnostic depth 上做到了，但缺乏 constructive output 确实限制了贡献的完整性。\n\n**结论**: 不同意 \"repackaging\" 的定性，但同意 contribution 量对 main conference 偏弱，可能更适合 Findings。\n\n---\n\n**[REBUT] R2-W2: Degeneracy = model success 的 natural consequence**\n\nR2 的逻辑是：CoNLL 58% degeneracy ← 91% F1（好模型），Few-NERD 10% ← 75% F1（弱模型），因此 degeneracy 仅反映 model quality。\n\n但论文有两个直接反驳：\n\n(a) **Few-NERD 75% F1 + 10% degeneracy vs. SciERC 66% F1 + 21% degeneracy** (Table 4, Section 5): Few-NERD 性能更高但 degeneracy 更低。如果 degeneracy 纯粹是 model quality 的函数，这一反转不应出现。论文在 Section 5 明确讨论：\"Few-NERD's low degeneracy despite high performance suggests that dataset-specific factors (number of entity types, semantic overlap) also modulate the rate。\"\n\n(b) **4B vs 8B on SciERC** (Table 5): 8B degeneracy 21% vs 4B degeneracy 10.4%，但 within-instance utility correlation 可比 (ρ=0.52 vs 0.55)。这证明 degeneracy 不仅是 accuracy 的 proxy——更高能力的模型在相同任务上产生更多 degeneracy，即使 within-instance 的 quality 分布仍有结构。\n\nR2 的简化 (\"LP selection only works when the model is bad enough\") 与 Few-NERD 数据矛盾：Few-NERD 是 75% F1（不差），LP 仍然 work (+1.36 pp)。\n\n**但我同意** R2 的 deeper point：论文需要更清楚地 disentangle degeneracy 的多个 driver（model quality, output space size, schema complexity, training epochs），而非将其作为一个 monolithic \"mechanism\"。这与我在 W1 中提出的 concern 一致。\n\n---\n\n**[AGREE] R2-W3: 缺乏可操作的 positive contribution**\n\n同意。论文唯一的 constructive suggestion 是 \"需要 trained verifiers\"（Section 5 最后段, Conclusion 最后句），但自己没有实现。Entity-token LP remedy 失败（Section 5 entity-token LP ablation），supervised verifier baseline 也失败 (Section 4.5)。LP + VC 组合全部失败 (Section 5 \"Signal combinations\")。\n\n对于 EMNLP main conference，我认为至少需要以下之一来补偿：\n- 一个 working (哪怕 partial) verifier baseline 展示 oracle gap 可以被 partially closed\n- 或者一个 clear actionable framework 告诉 practitioner exactly when to use BoN（例如基于 degeneracy rate 的 decision rule）\n\n论文在 practical considerations 段落有一些 guidance，但不够 concrete to be actionable。\n\n不过我注意到：Few-NERD 的 LP selection 成功 (+1.36 pp, p<0.001) 本身就是 positive result，只是论文将其 framing 为 diagnostic evidence 而非 practical method。如果 reframe 为 \"LP selection works in the low-degeneracy regime, and we characterize when that regime occurs\"，practical value 会更明显。\n\n---\n\n**[AGREE] R2-W4: em-dash 过度使用**\n\n同意这是一个 presentation quality 问题。我没有专门计数，但通读全文时确实注意到频繁的 em-dash 使用（特别是在 Discussion section）。按照 ACL 写作规范和审稿人期望，减少 em-dash 使用是低成本高收益的修改。\n\n---\n\n**[AGREE] R2-W5: Abstract 和 Introduction 数字堆��**\n\n同意。我重新检查 Abstract：在约 180 words 中有 \"ρ up to 0.38\", \"0.42\", \"AUROC up to 0.82\", \"~13 pp\", \"ρ=0.52\", \"10-58%\", \"0.041 nats\", \"+1.36 pp\", \"p<0.001\", \"58%\", \"+0.42 pp\", \"$N=8$ to 16\", \"p=0.003\" — 密度过高。这是 experimental report 风格而非 story-driven 叙事。每个数字单独看是 justified，但整体上牺牲了可读性。\n\n---\n\n**[REBUT] R2-W6: 与 Yao et al. (2026) 差异化不足**\n\n论文在 Section 1 第二段（Introduction）和 Section 2 \"Consistency for structured IE\" 段落中明确列出差异：(1) Yao et al. 使用 hard-prompting，本文使用 fine-tuned models（degeneracy 更严重）；(2) Yao et al. 仅报告 correlation，未区分 QE vs selection；(3) 本文诊断了两个具体 failure mechanisms。\n\n差异化实际上是充分的——Table 4 的 Few-NERD 结果和 Section 4.5 的 LoRA ablation 都是 Yao et al. 不覆盖的实验。但 Introduction 中差异化的叙述方式可以更 upfront（目前在第二段中间，容易被跳过）。\n\n---\n\n**[REBUT] R2-W7: Missing reference Byerly & Khashabi (2024) \"Self-Consistency Falls Short\"**\n\n我无法确认这篇论文存在。在我的知识范围内，没有 Byerly & Khashabi (2024) 以这个确切标题发表的论文。如果 R2 能提供确切 venue 或 arXiv ID，我可以重新评估。建议作者在 rebuttal 中 verify 这一引用的存在性。\n\n---\n\n**[AGREE] R2-W8: Discussion 过长**\n\n同意。Discussion (Section 5) 承载了：(1) practical implications, (2) why the gap exists (degeneracy + LP compression analysis), (3) non-tied subset analysis, (4) N-scaling effect, (5) temperature effect, (6) verbalized confidence, (7) signal combinations, (8) LP compression hypotheses, (9) free-form ablation, (10) entity-token LP, (11) pilot remedy, (12) practical considerations, (13) regime boundaries, (14) methodological implications. 这是 14 个 distinct sub-topics 在一个 section 中。\n\n建议：将 (3) non-tied subset, (4) N-scaling, (5) temperature, (6) verbalized confidence, (7) signal combinations 移入 Appendix，仅在 Discussion 保留引用。这可释放 ~1 page 空间用于 constructive contribution。\n\n---\n\n## Minor Issues 回应\n\n**[AGREE] R2-M1**: \"leverage\" 用词问题——Minor，容易修复。\n\n**[REBUT] R2-M2**: Abstract 中 NER 需定义——NER (Named Entity Recognition) 是 NLP 社区的标准缩写，ARR 审稿人不需要定义。MBR 可能确实需要定义或避免在 Abstract 中使��（Abstract 中首次出现 \"MBR / consensus-proximity selection\" 在 line 6，未展开）。\n\n**[AGREE] R2-M3**: Table 3 EM/VC 无 p 值——同意需要解释。查看 Table 3，EM (0.637) 和 VC (0.623) 明显低于 greedy (0.645)，因此方向为负，paired test 不会给 \"improvement\" p 值。但论文应标注 \"—\" 并注释 \"below greedy, test not applicable\"。\n\n**[AGREE] R2-M4**: Figure 3 \"~15%\" 的定义——确实不精确。Dashed line 位置应有 explicit justification（如来自 ROC 分析或 breakpoint detection），而非视觉近似。\n\n**[REBUT] R2-M5**: em-dash vs en-dash 区分——这是排版规范问题，不影响科学内容。论文使用 LaTeX `---` (em-dash) 用于解释性插入。按 ACL style guide，em-dash 本身不违规，只是频率过高（同意 W4）。\n\n---\n\n## Questions 回应\n\n**[AGREE] R2-Q1: Output space size 驱动 degeneracy**\n\n这是一个重要的 alternative explanation。Few-NERD 8 types vs CoNLL 4 types 意味着可能的 entity set configurations 指数级更多，自然降低 exact match degeneracy。论文在 Section 5 提到 \"number of entity types\" 作为 modulating factor，但未做 controlled analysis。\n\n这与我在 W1 中的 concern 一致：degeneracy 可能主要是 output space size 的函数，而非独立的 \"mechanism\"。如果在 CoNLL 上增加 entity types（如 fine-grained NER），degeneracy 可能也会下降——那么 \"degeneracy gates selection\" 本质上就是 \"output space diversity gates selection\"，这个 framing 更准确但也更 trivial。\n\n---\n\n**[AGREE] R2-Q2: LoRA rank=8 证据对 degeneracy-as-gating-factor 的挑战**\n\n完全同意。这与我在 W2 中的分析一致：rank=8 下 degeneracy 7.2% 但 LP selection 仍失败，直接挑战了 \"degeneracy is the gating factor\" 的 framing。论文的 \"necessary but not sufficient\" 回应在逻辑上成立，但实验设计上混淆了 degeneracy 下降和模型能力下降这两个变量。\n\n---\n\n**[REBUT] R2-Q3: 70B+ 模型是否使 research direction 无望**\n\n不同意 \"无望\" 的暗示。两个理由：\n\n(a) 70B+ 模型可能有更强的 LP signal quality（representation space 更丰富），即使 degeneracy 更高。LP compression 可能在 larger models 中有不同 pattern——论文未测试不代表方向无望。\n\n(b) 更重要的是，论文的 QE contribution 不受 degeneracy 影响——即使 70B 模型 degeneracy 更高，QE signals 仍然有用（selective prediction, error flagging）。只是 selection 方向可能确实在 highly capable models 上受限。\n\n论文在 Limitations 中诚实承认这一未知：\"Whether the gap holds for 70B+ models is untested—larger models may produce more diverse samples.\" 这是合理的 scope limitation 而非 fatal flaw。\n\n---\n\n**[AGREE] R2-Q4: Supervised verifier 仅用 5 scalar features**\n\n同意这是 verifier experiment 的主要局限。5 个 scalar features（all are instance-level aggregates except LP）本身就 encode 不了 per-sample discriminative information——这几乎是 set up to fail。\n\n如果加入 token-level features（如 per-entity log-prob, attention entropy, hidden state uncertainty），verifier 可能表现完全不同。Section 4.5 的 supervised verifier 结论 (\"bottleneck lies in the feature space\") 实际上只能说 \"bottleneck lies in THESE specific 5 features\"，不能泛化为 \"no feature combination can close the gap\"。\n\n但我也注意到��论文 frame 这个实验的目的是 \"test whether the information bottleneck lies in the aggregation method or the features themselves\"——在这个 narrow claim 下，实验设计是合理的（固定 features，变 aggregation method）。只是 broader conclusion 需要 qualify。\n\n---\n\n## 总结性评价\n\nR2 的核心 concern（novelty/contribution 量不足 for main conference）是合理的，但部分 technical criticisms（W2 的 degeneracy = model success 简化）在论文数据面前不完全成立。我认为论文的贡献介于 Main Conference 和 Findings 之间：\n\n- **支撑 Main Conference 的因素**: 实验系统性、统计严谨性、三层诊断的清晰度、Few-NERD positive result\n- **支撑 Findings 的因素**: 缺乏 constructive contribution (W3)、核心因果 claim 证据偏薄 (与我的 W1-W2 一致)、novelty 主要在 framing 而非 new method\n\n我维持 **Borderline Accept (3.5/5)** 的评分，但认为 R2 的 **Borderline Reject (3/5)** 也在合���范围内。关键分歧在于 \"purely diagnostic paper with strong execution\" 是否 sufficient for main conference。\n",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d013713b-4e84-463d-9184-6d21ea80a59e",
  "isSidechain": false,
  "requestId": "req_011Cb7jDBD9tGuaRQ6HGSMNX",
  "type": "assistant",
  "uuid": "fe944bf5-ad4b-412f-a0a6-1205eefcea96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjKx9FNxe864f4ZZaXWHf9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1255,
      "cache_read_input_tokens": 93076,
      "output_tokens": 5331,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5331,
          "cache_read_input_tokens": 93076,
          "cache_creation_input_tokens": 1255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1255
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 90_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见  以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。  ---  ### Reviewe…",
  "leafUuid": "fe944bf5-ad4b-412f-a0a6-1205eefcea96",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Runtime record

_source line 91_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structural self-consistency information extraction paper",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7"
}
```

---

### Tool result

_source line 92 · 2026-05-17T07:16:47.986Z_

<details><summary>↩ Tool result · `toolu_01Wox6YPFPzGVTpLCnAfaigV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe944bf5-ad4b-412f-a0a6-1205eefcea96",
  "isSidechain": false,
  "promptId": "e569eff4-e4f3-4bac-baec-9c1df028af05",
  "type": "user",
  "uuid": "ca783527-bbb8-4185-977c-d5bb7c56d509",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "fe944bf5-ad4b-412f-a0a6-1205eefcea96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "c90336b9-14fd-4019-93e1-2d9dae199ea7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
