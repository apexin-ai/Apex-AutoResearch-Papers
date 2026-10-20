# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/c6c5af12-c569-4559-ba51-4daf898d5084.jsonl`
- **Structured JSON:** [`887c7a0d1b1872cd0423.json`](../../sessions/88/887c7a0d1b1872cd0423.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:16:17.729Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:16:17.729Z",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：核心 reframe：从 'cross-lingual calibration method' 转为 'cross-lingual probing viability boundary + methodological warning'。 Headline: 'Stress-testing probe-based calibration beyond English: viability boundaries, capacity artifacts, and when cross-lingual transfer breaks down.' 大模型（235B MoE / Scout MoE）的 correctness signal 比 7B dense 更分散——MoE routing 将信息分散到更多 expert，导致 probe AUROC 提升有限且 noisy。 Pareto frontier 在两个 MoE 架构上均 noisy（rho 接近零），无法支撑 clean architecture contrast。 CaCLR 失败且 linear projection 在低/中资源语言不稳定。CKA partial correlation 控制 depth 后 n.s.。 Control task 揭示 >30% 的 lang-layer 组合是 capacity artifacts，低资源语言几乎全部受影响。 贡献重构为：(1) viability boundary 刻画；(2) capacity artifact 问题揭露（Hewitt & Liang 多语言扩展）；(3) 方法论框架。 目标 venue 不降级（EACL）——需增加 discussion 篇幅，补充 few-shot escalation 实验作为 constructive path forward。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T04:16:17.733Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:16:17.733Z",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-21T04:16:17.765Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：核心 reframe：从 'cross-lingual calibration method' 转为 'cross-lingual probing viability boundary + methodological warning'。 Headline: 'Stress-testing probe-based calibration beyond English: viability boundaries, capacity artifacts, and when cross-lingual transfer breaks down.' 大模型（235B MoE / Scout MoE）的 correctness signal 比 7B dense 更分散——MoE routing 将信息分散到更多 expert，导致 probe AUROC 提升有限且 noisy。 Pareto frontier 在两个 MoE 架构上均 noisy（rho 接近零），无法支撑 clean architecture contrast。 CaCLR 失败且 linear projection 在低/中资源语言不稳定。CKA partial correlation 控制 depth 后 n.s.。 Control task 揭示 >30% 的 lang-layer 组合是 capacity artifacts，低资源语言几乎全部受影响。 贡献重构为：(1) viability boundary 刻画；(2) capacity artifact 问题揭露（Hewitt & Liang 多语言扩展）；(3) 方法论框架。 目标 venue 不降级（EACL）——需增加 discussion 篇幅，补充 few-shot escalation 实验作为 constructive path forward。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "a68b1ff4-8e39-4ef3-85b0-f05a15345cd5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:16:17.765Z_

```json
{
  "parentUuid": "a68b1ff4-8e39-4ef3-85b0-f05a15345cd5",
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c21643f4-5fc0-4362-b335-310138af63f5",
  "timestamp": "2026-05-21T04:16:17.765Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:16:17.765Z_

```json
{
  "parentUuid": "c21643f4-5fc0-4362-b335-310138af63f5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ade93d5c-2112-4b14-a7d4-1576590c9449",
  "timestamp": "2026-05-21T04:16:17.765Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration viability boundaries",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084"
}
```

---

### Assistant

_source line 7 · 2026-05-21T04:16:20.923Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ade93d5c-2112-4b14-a7d4-1576590c9449",
  "isSidechain": false,
  "requestId": "req_011CbF4qusCEXCqJrDWjhJBH",
  "type": "assistant",
  "uuid": "36ce26da-88f2-4da0-aad1-30949ded09e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018n2XHHZcmarg2HqPfusRP2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11675,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11675
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

_source line 8 · 2026-05-21T04:16:21.506Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fd9GZVQVT83MWTDRkXXXfG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36ce26da-88f2-4da0-aad1-30949ded09e5",
  "isSidechain": false,
  "requestId": "req_011CbF4qusCEXCqJrDWjhJBH",
  "type": "assistant",
  "uuid": "f3aa0a7f-d3fa-49dc-abd9-64a1c4ea47bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018n2XHHZcmarg2HqPfusRP2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11675,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11675
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

_source line 9 · 2026-05-21T04:16:21.753Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DGqrXryAAQKzyWChA5ZrnH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3aa0a7f-d3fa-49dc-abd9-64a1c4ea47bb",
  "isSidechain": false,
  "requestId": "req_011CbF4qusCEXCqJrDWjhJBH",
  "type": "assistant",
  "uuid": "ba931b5e-05c4-4b2b-8ac4-1fa1e45a7159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018n2XHHZcmarg2HqPfusRP2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11675,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11675
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

_source line 10 · 2026-05-21T04:16:21.760Z_

<details><summary>↩ Tool result · `toolu_01DGqrXryAAQKzyWChA5ZrnH`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff varies across architectures (strong on Qwen, weak on Llama); CKA geometric analysis (not mechanistic explanation — correlational, must control for depth) suggests architecture-specific representation divergence rates as a factor. CaCLR tests whether distributional matching can shift this frontier without target-language labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).
15	- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).
16	- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method / Diagnostic)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.
24	- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
25	- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.
26	- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.
27	- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.
28	- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
29	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.
30	
31	### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
32	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
33	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
34	
35	## Story Spine
36	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
37	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
38	- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. A methodological warning: control task analysis reveals that ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold), challenging uncritical use of cross-lingual probing. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.
39	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
40	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines."
41	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
42	
43	## Field-Level Significance
44	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
45	
46	## Anticipated Reviewer Concerns & Responses
47	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
48	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
49	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
50	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
51	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
52	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
53	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
54	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
55	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
56	10. **"No mechanistic explanation"** → CKA geometric analysis (framed as correlational, NOT mechanistic) provides two levels of insight: (a) between-language: languages with higher CKA show less transfer degradation; (b) between-architecture: CKA cliff steepness differs. **MUST report partial correlation controlling for normalized depth** — if CKA adds no explanatory power beyond depth, downgrade to "suggestive correlational analysis." Subspace angle analysis (quantitative, not just prose) strengthens geometric narrative.
57	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
58	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
59	13. **"CaCLR is your own method — self-debunking is less impactful"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.
60	14. **"CKA is correlational, not mechanistic"** → We agree and frame CKA analysis as geometric/correlational, not mechanistic. We report partial correlation controlling for depth to test whether CKA adds explanatory power beyond the trivial "deeper = worse transfer." If partial correlation is weak, we explicitly state CKA is suggestive only.
61	
62	## Additional Related Work Coverage (Dream-identified gaps)
63	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) "On learning invariant representations for domain adaptation" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.
64	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.
65	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.
66	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.
67	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
68	- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.
69	- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.
70	
71	## Differentiation from Closest Prior Work
72	| Paper | Their Focus | Our Difference |
73	|-------|-------------|----------------|
74	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
75	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
76	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
77	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
78	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
79	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba931b5e-05c4-4b2b-8ac4-1fa1e45a7159",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "a0910a74-32e0-4b79-8d79-5d162f4421cc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff varies across architectures (strong on Qwen, weak on Llama); CKA geometric analysis (not mechanistic explanation — correlational, must control for depth) suggests architecture-specific representation divergence rates as a factor. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. A methodological warning: control task analysis reveals that ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold), challenging uncritical use of cross-lingual probing. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis (framed as correlational, NOT mechanistic) provides two levels of insight: (a) between-language: languages with higher CKA show less transfer degradation; (b) between-architecture: CKA cliff steepness differs. **MUST report partial correlation controlling for normalized depth** — if CKA adds no explanatory power beyond depth, downgrade to \"suggestive correlational analysis.\" Subspace angle analysis (quantitative, not just prose) strengthens geometric narrative.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame CKA analysis as geometric/correlational, not mechanistic. We report partial correlation controlling for depth to test whether CKA adds explanatory power beyond the trivial \"deeper = worse transfer.\" If partial correlation is weak, we explicitly state CKA is suggestive only.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 79,
      "startLine": 1,
      "totalLines": 79
    }
  },
  "sourceToolAssistantUUID": "ba931b5e-05c4-4b2b-8ac4-1fa1e45a7159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T04:16:21.818Z_

<details><summary>↩ Tool result · `toolu_01Fd9GZVQVT83MWTDRkXXXfG`</summary>

```text
1	[
2	  {
3	    "name": "Qwen3-235B-A22B Full Pareto Frontier (20 langs × 24 layers × 5 transfer conditions)",
4	    "description": "在 Qwen3-235B-A22B（94 层 MoE, INT4）上提取每隔 4 层的激活（24 个 probed layers）， 20 种语言训练英语 correctness probes（LR + MLP），评估 5 种 transfer 条件。 报告 per-language Spearman rho（depth vs transfer AUROC）和 global rho。\n",
5	    "results": {
6	      "en_best_auroc": 0.76,
7	      "en_best_layer": "L72 (约 77% depth)",
8	      "en_auroc_range": [
9	        0.58,
10	        0.76
11	      ],
12	      "en_best_ece_raw": 0.175,
13	      "zs_transfer_auroc_avg_20lang": 0.59,
14	      "zs_transfer_auroc_high_resource_avg": 0.65,
15	      "zs_transfer_auroc_mid_resource_avg": 0.59,
16	      "zs_transfer_auroc_low_resource_avg": 0.53,
17	      "zs_transfer_success_rate_above_060": "11/20 (55%)",
18	      "pareto_global_spearman_rho": -0.18,
19	      "pareto_global_spearman_p": 0.12,
20	      "pareto_per_lang_rho_median": -0.14,
21	      "pareto_per_lang_significant_count": "3/19 (zh, es, fr — 仅高资源)",
22	      "pareto_per_lang_positive_rho_count": "6/19 (ar, ko, bn, sw, te, vi — 方向反转)",
23	      "mean_shift_delta_auroc_avg": 0.0,
24	      "linear_proj_50pairs_delta_auroc_avg": 0.015,
25	      "linear_proj_50pairs_delta_auroc_high": 0.025,
26	      "linear_proj_50pairs_delta_auroc_low": -0.005,
27	      "fewshot_25_delta_auroc_avg": 0.035,
28	      "fewshot_100_delta_auroc_avg": 0.065,
29	      "linear_proj_std_across_seeds_low_resource": 0.028,
30	      "zs_auroc_std_across_layers_top10": 0.04
31	    },
32	    "tables": [
33	      {
34	        "title": "Table 1: Qwen3-235B Zero-Shot Transfer AUROC by Language (EN-optimal layer L72)",
35	        "columns": [
36	          "Language",
37	          "Family",
38	          "Resource_Tier",
39	          "ZS_AUROC",
40	          "95% CI",
41	          "vs EN Δ"
42	        ],
43	        "rows": [
44	          [
45	            "en",
46	            "Germanic",
47	            "source",
48	            0.76,
49	            "[0.74, 0.78]",
50	            "—"
51	          ],
52	          [
53	            "zh",
54	            "Sinitic",
55	            "HIGH",
56	            0.672,
57	            "[0.65, 0.69]",
58	            -0.088
59	          ],
60	          [
61	            "es",
62	            "Romance",
63	            "HIGH",
64	            0.668,
65	            "[0.64, 0.69]",
66	            -0.092
67	          ],
68	          [
69	            "fr",
70	            "Romance",
71	            "HIGH",
72	            0.662,
73	            "[0.64, 0.68]",
74	            -0.098
75	          ],
76	          [
77	            "de",
78	            "Germanic",
79	            "HIGH",
80	            0.653,
81	            "[0.63, 0.68]",
82	            -0.107
83	          ],
84	          [
85	            "ja",
86	            "Japonic",
87	            "MID",
88	            0.631,
89	            "[0.60, 0.66]",
90	            -0.129
91	          ],
92	          [
93	            "pt",
94	            "Romance",
95	            "MID",
96	            0.624,
97	            "[0.60, 0.65]",
98	            -0.136
99	          ],
100	          [
101	            "ru",
102	            "Slavic",
103	            "MID",
104	            0.608,
105	            "[0.58, 0.64]",
106	            -0.152
107	          ],
108	          [
109	            "ko",
110	            "Koreanic",
111	            "MID",
112	            0.602,
113	            "[0.57, 0.63]",
114	            -0.158
115	          ],
116	          [
117	            "nl",
118	            "Germanic",
119	            "MID",
120	            0.598,
121	            "[0.57, 0.63]",
122	            -0.162
123	          ],
124	          [
125	            "hi",
126	            "Indo-Aryan",
127	            "MID",
128	            0.588,
129	            "[0.56, 0.62]",
130	            -0.172
131	          ],
132	          [
133	            "pl",
134	            "Slavic",
135	            "MID",
136	            0.582,
137	            "[0.55, 0.61]",
138	            -0.178
139	          ],
140	          [
141	            "id",
142	            "Austronesian",
143	            "MID",
144	            0.577,
145	            "[0.55, 0.61]",
146	            -0.183
147	          ],
148	          [
149	            "tr",
150	            "Turkic",
151	            "MID",
152	            0.571,
153	            "[0.54, 0.60]",
154	            -0.189
155	          ],
156	          [
157	            "vi",
158	            "Austroasiatic",
159	            "MID",
160	            0.563,
161	            "[0.53, 0.60]",
162	            -0.197
163	          ],
164	          [
165	            "uk",
166	            "Slavic",
167	            "MID",
168	            0.558,
169	            "[0.53, 0.59]",
170	            -0.202
171	          ],
172	          [
173	            "ar",
174	            "Semitic",
175	            "MID",
176	            0.555,
177	            "[0.52, 0.59]",
178	            -0.205
179	          ],
180	          [
181	            "bn",
182	            "Indo-Aryan",
183	            "LOW",
184	            0.538,
185	            "[0.50, 0.57]",
186	            -0.222
187	          ],
188	          [
189	            "te",
190	            "Dravidian",
191	            "LOW",
192	            0.521,
193	            "[0.49, 0.55]",
194	            -0.239
195	          ],
196	          [
197	            "sw",
198	            "Niger-Congo",
199	            "LOW",
200	            0.508,
201	            "[0.48, 0.54]",
202	            -0.252
203	          ]
204	        ]
205	      },
206	      {
207	        "title": "Table 2: Qwen3-235B Pareto Spearman ρ (depth vs ZS AUROC) per Language",
208	        "columns": [
209	          "Language",
210	          "Spearman_rho",
211	          "p_value",
212	          "Direction",
213	          "Significant"
214	        ],
215	        "rows": [
216	          [
217	            "zh",
218	            -0.52,
219	            0.009,
220	            "expected",
221	            "✓"
222	          ],
223	          [
224	            "es",
225	            -0.44,
226	            0.031,
227	            "expected",
228	            "✓"
229	          ],
230	          [
231	            "fr",
232	            -0.41,
233	            0.046,
234	            "expected",
235	            "✓"
236	          ],
237	          [
238	            "de",
239	            -0.33,
240	            0.11,
241	            "expected",
242	            "✗"
243	          ],
244	          [
245	            "ja",
246	            -0.25,
247	            0.24,
248	            "expected",
249	            "✗"
250	          ],
251	          [
252	            "ru",
253	            -0.18,
254	            0.4,
255	            "expected",
256	            "✗"
257	          ],
258	          [
259	            "ko",
260	            -0.06,
261	            0.79,
262	            "flat",
263	            "✗"
264	          ],
265	          [
266	            "hi",
267	            -0.03,
268	            0.89,
269	            "flat",
270	            "✗"
271	          ],
272	          [
273	            "tr",
274	            0.02,
275	            0.93,
276	            "flat",
277	            "✗"
278	          ],
279	          [
280	            "id",
281	            -0.11,
282	            0.61,
283	            "expected",
284	            "✗"
285	          ],
286	          [
287	            "pt",
288	            -0.28,
289	            0.19,
290	            "expected",
291	            "✗"
292	          ],
293	          [
294	            "nl",
295	            -0.22,
296	            0.3,
297	            "expected",
298	            "✗"
299	          ],
300	          [
301	            "pl",
302	            -0.08,
303	            0.71,
304	            "flat",
305	            "✗"
306	          ],
307	          [
308	            "vi",
309	            0.12,
310	            0.58,
311	            "reversed",
312	            "✗"
313	          ],
314	          [
315	            "uk",
316	            -0.15,
317	            0.48,
318	            "expected",
319	            "✗"
320	          ],
321	          [
322	            "ar",
323	            0.09,
324	            0.67,
325	            "reversed",
326	            "✗"
327	          ],
328	          [
329	            "bn",
330	            0.18,
331	            0.4,
332	            "reversed",
333	            "✗"
334	          ],
335	          [
336	            "te",
337	            0.22,
338	            0.3,
339	            "reversed",
340	            "✗"
341	          ],
342	          [
343	            "sw",
344	            0.15,
345	            0.48,
346	            "reversed",
347	            "✗"
348	          ],
349	          [
350	            "global",
351	            -0.18,
352	            0.12,
353	            "—",
354	            "✗"
355	          ]
356	        ]
357	      }
358	    ],
359	    "figures": [],
360	    "analysis": "Qwen3-235B 的 Pareto frontier 远弱于 7B dense MVP 预期。Global rho=-0.18 不显著， 仅 3/19 target 语言有显著负相关（均为高资源）。6/19 语言出现方向反转（正 rho）， 集中在低资源。MoE routing 的 input-dependent expert selection 使得不同语言在不同深度 激活完全不同的子网络，破坏了 \"更深=更好英语但更差 transfer\" 的简单叙事。 这意味着 Pareto frontier 在 MoE 架构上不是稳定的 architecture-level property， 而是 language-specific 的。对 worst tier 叙事：这直接支持 \"viability boundary\" reframe—— Pareto analysis 仅在高资源+特定架构上有清晰信号。\n\n\n235B MoE 架构有 94 层但仅 22B 激活参数——expert routing 机制将 correctness 信息分散到不同 expert 子网络中， probe 在 shared representation 上只能捕获部分信号，因此 AUROC 相比 7B dense（0.754）提升极有限（→0.76）。 MoE 的 expert 选择是 input-dependent 的，不同语言激活不同 expert 子集，导致跨语言激活空间异质性更高。 这直接破坏了 Pareto frontier 的一致性：不同语言的 \"最优 transfer 层\" 受 expert routing pattern 影响而高度分散， global rho 被拉向零。高资源语言（zh/es/fr）与英语共享更多 expert 激活模式，仍显示弱 Pareto； 低资源语言与英语 expert overlap 极低，transfer AUROC 在深层反而因 expert divergence 而改善（正 rho）。 Linear projection 在低资源上不稳定，因为 50 parallel pairs 不足以学习 MoE 碎片化空间的旋转矩阵。\n"
361	  },
362	  {
363	    "name": "Llama 4 Scout Full Pareto Frontier (20 langs × 12 layers × 5 transfer conditions)",
364	    "description": "在 Llama 4 Scout（48 层 MoE, W4A16）上提取激活（12 probed layers）， 20 种语言，5 种 transfer 条件。报告 per-language Spearman rho。\n",
365	    "results": {
366	      "en_best_auroc": 0.74,
367	      "en_best_layer": "L40 (约 83% depth)",
368	      "en_auroc_range": [
369	        0.6,
370	        0.74
371	      ],
372	      "en_best_ece_raw": 0.185,
373	      "zs_transfer_auroc_avg_20lang": 0.57,
374	      "zs_transfer_auroc_high_resource_avg": 0.63,
375	      "zs_transfer_auroc_mid_resource_avg": 0.57,
376	      "zs_transfer_auroc_low_resource_avg": 0.51,
377	      "zs_transfer_success_rate_above_060": "8/20 (40%)",
378	      "pareto_global_spearman_rho": -0.05,
379	      "pareto_global_spearman_p": 0.62,
380	      "pareto_per_lang_rho_median": -0.02,
381	      "pareto_per_lang_significant_count": "1/19 (仅 zh)",
382	      "pareto_per_lang_positive_rho_count": "8/19",
383	      "mean_shift_delta_auroc_avg": 0.0,
384	      "linear_proj_50pairs_delta_auroc_avg": 0.008,
385	      "linear_proj_50pairs_delta_auroc_low": -0.01,
386	      "fewshot_25_delta_auroc_avg": 0.028,
387	      "fewshot_100_delta_auroc_avg": 0.055,
388	      "linear_proj_std_across_seeds_low_resource": 0.035
389	    },
390	    "tables": [
391	      {
392	        "title": "Table 3: Llama 4 Scout Zero-Shot Transfer AUROC (EN-optimal L40)",
393	        "columns": [
394	          "Language",
395	          "Resource_Tier",
396	          "ZS_AUROC",
397	          "95% CI"
398	        ],
399	        "rows": [
400	          [
401	            "en",
402	            "source",
403	            0.74,
404	            "[0.72, 0.76]"
405	          ],
406	          [
407	            "zh",
408	            "HIGH",
409	            0.648,
410	            "[0.62, 0.67]"
411	          ],
412	          [
413	            "es",
414	            "HIGH",
415	            0.643,
416	            "[0.62, 0.67]"
417	          ],
418	          [
419	            "fr",
420	            "HIGH",
421	            0.635,
422	            "[0.61, 0.66]"
423	          ],
424	          [
425	            "de",
426	            "HIGH",
427	            0.628,
428	            "[0.60, 0.65]"
429	          ],
430	          [
431	            "ja",
432	            "MID",
433	            0.601,
434	            "[0.57, 0.63]"
435	          ],
436	          [
437	            "ru",
438	            "MID",
439	            0.588,
440	            "[0.56, 0.62]"
441	          ],
442	          [
443	            "ko",
444	            "MID",
445	            0.583,
446	            "[0.55, 0.61]"
447	          ],
448	          [
449	            "pt",
450	            "MID",
451	            0.595,
452	            "[0.57, 0.62]"
453	          ],
454	          [
455	            "hi",
456	            "MID",
457	            0.568,
458	            "[0.54, 0.60]"
459	          ],
460	          [
461	            "nl",
462	            "MID",
463	            0.575,
464	            "[0.54, 0.61]"
465	          ],
466	          [
467	            "pl",
468	            "MID",
469	            0.562,
470	            "[0.53, 0.59]"
471	          ],
472	          [
473	            "id",
474	            "MID",
475	            0.555,
476	            "[0.52, 0.59]"
477	          ],
478	          [
479	            "tr",
480	            "MID",
481	            0.548,
482	            "[0.52, 0.58]"
483	          ],
484	          [
485	            "vi",
486	            "MID",
487	            0.541,
488	            "[0.51, 0.57]"
489	          ],
490	          [
491	            "uk",
492	            "MID",
493	            0.545,
494	            "[0.51, 0.58]"
495	          ],
496	          [
497	            "ar",
498	            "MID",
499	            0.538,
500	            "[0.51, 0.57]"
501	          ],
502	          [
503	            "bn",
504	            "LOW",
505	            0.518,
506	            "[0.49, 0.55]"
507	          ],
508	          [
509	            "te",
510	            "LOW",
511	            0.505,
512	            "[0.47, 0.54]"
513	          ],
514	          [
515	            "sw",
516	            "LOW",
517	            0.495,
518	            "[0.46, 0.53]"
519	          ]
520	        ]
521	      },
522	      {
523	        "title": "Table 4: Llama 4 Scout Pareto ρ per Language",
524	        "columns": [
525	          "Language",
526	          "Spearman_rho",
527	          "p_value",
528	          "Significant"
529	        ],
530	        "rows": [
531	          [
532	            "zh",
533	            -0.62,
534	            0.031,
535	            "✓"
536	          ],
537	          [
538	            "es",
539	            -0.38,
540	            0.22,
541	            "✗"
542	          ],
543	          [
544	            "fr",
545	            -0.29,
546	            0.36,
547	            "✗"
548	          ],
549	          [
550	            "de",
551	            -0.15,
552	            0.64,
553	            "✗"
554	          ],
555	          [
556	            "ja",
557	            -0.08,
558	            0.8,
559	            "✗"
560	          ],
561	          [
562	            "ru",
563	            0.05,
564	            0.88,
565	            "✗"
566	          ],
567	          [
568	            "ko",
569	            0.22,
570	            0.49,
571	            "✗"
572	          ],
573	          [
574	            "hi",
575	            0.11,
576	            0.73,
577	            "✗"
578	          ],
579	          [
580	            "tr",
581	            0.08,
582	            0.8,
583	            "✗"
584	          ],
585	          [
586	            "id",
587	            -0.03,
588	            0.93,
589	            "✗"
590	          ],
591	          [
592	            "pt",
593	            -0.18,
594	            0.58,
595	            "✗"
596	          ],
597	          [
598	            "nl",
599	            -0.12,
600	            0.71,
601	            "✗"
602	          ],
603	          [
604	            "pl",
605	            0.15,
606	            0.64,
607	            "✗"
608	          ],
609	          [
610	            "vi",
611	            0.25,
612	            0.43,
613	            "✗"
614	          ],
615	          [
616	            "uk",
617	            0.03,
618	            0.93,
619	            "✗"
620	          ],
621	          [
622	            "ar",
623	            0.18,
624	            0.58,
625	            "✗"
626	          ],
627	          [
628	            "bn",
629	            0.28,
630	            0.38,
631	            "✗"
632	          ],
633	          [
634	            "te",
635	            0.35,
636	            0.26,
637	            "✗"
638	          ],
639	          [
640	            "sw",
641	            0.31,
642	            0.33,
643	            "✗"
644	          ],
645	          [
646	            "global",
647	            -0.05,
648	            0.62,
649	            "✗"
650	          ]
651	        ]
652	      }
653	    ],
654	    "figures": [],
655	    "analysis": "Scout 上 Pareto 完全崩溃——global rho=-0.05 (p=0.62)，仅 zh 显著。n=12 的采样密度 使得统计检验力不足以检测中等效应。与 Qwen3 对比：两个 MoE 架构都无法支撑 \"clean architecture contrast\"， 因为 rho 都不显著（Qwen -0.18 p=0.12, Scout -0.05 p=0.62）。MVP 阶段观察到的 Qwen(strong)/Llama(weak) 对比在大模型上被 MoE noise 冲刷。这强化了 worst tier 叙事：Pareto frontier 作为分析工具 仅在 7B dense + 高资源语言上有效——对 MoE 架构的泛化失败是方法论局限性的核心发现。\n\n\nLlama 4 Scout 是 17B-16E MoE（272B total, 17B active），48 层比 Qwen3 的 94 层少得多， probed layers 仅 12 个，Spearman rho 的统计检验力极低（n=12 时需要 |rho|>0.58 才显著）。 MVP 阶段 Llama-3.1-8B dense 已经是 weak Pareto（仅 2/5 显著），Scout MoE 继承了 Llama 家族 的弱 depth-transfer tradeoff 特征（可能因为 Llama 训练数据中多语言比例高于 Qwen， 导致深层 representation 已经部分语言对齐），加上 MoE routing 碎片化效应， global rho 被进一步推向零。W4A16 量化可能引入额外 noise（权重 4-bit 但激活 16-bit， correctness probe 依赖的微弱方向性信号可能在权重量化中丢失部分精度）。 12 个 probed layers 的粗糙采样使得 per-language rho 高度不稳定， 微小的 AUROC 波动就能翻转 rho 方向。\n"
656	  },
657	  {
658	    "name": "CaCLR Comparative Evaluation (2 models × 20 langs × Pareto frontier)",
659	    "description": "CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) 与 zero-shot/mean-shift/linear projection/few-shot 在两个模型全 Pareto frontier 上的对比。α sweep (0.01-10.0), β sweep 3 OOM (0.001-1.0)。\n",
660	    "results": {
661	      "caclr_best_beta_auroc_delta_vs_zeroshot_avg": 0.002,
662	      "caclr_best_beta_auroc_delta_high_resource": 0.005,
663	      "caclr_best_beta_auroc_delta_low_resource": -0.008,
664	      "caclr_best_beta_auroc_delta_range": [
665	        -0.01,
666	        0.005
667	      ],
668	      "beta_0001_delta_auroc": 0.001,
669	      "beta_001_delta_auroc": 0.002,
670	      "beta_01_delta_auroc": 0.001,
671	      "beta_1_delta_auroc": -0.003,
672	      "beta_sweep_variance_across_seeds": 0.006,
673	      "caclr_delta_ece_vs_tempscaling_avg": 0.008,
674	      "caclr_delta_ece_vs_tempscaling_range": [
675	        -0.005,
676	        0.02
677	      ],
678	      "bce_only_auroc_delta": 0.0,
679	      "bce_sbece_auroc_delta": 0.001,
680	      "bce_mmd_auroc_delta": 0.002,
681	      "bce_sbece_mmd_auroc_delta": 0.002,
682	      "linear_proj_50pairs_delta_auroc_avg": 0.015,
683	      "linear_proj_50pairs_wins_over_caclr": "14/19 languages",
684	      "fewshot_25_delta_auroc_avg": 0.032,
685	      "fewshot_100_delta_auroc_avg": 0.061,
686	      "alpha_optimal": 0.1,
687	      "alpha_sensitivity": "robust in [0.01, 1.0], degrades at α=10"
688	    },
689	    "tables": [
690	      {
691	        "title": "Table 5: Transfer Method Comparison — Δ AUROC vs Zero-Shot (Qwen3-235B, EN-optimal layer)",
692	        "columns": [
693	          "Method",
694	          "HIGH_avg",
695	          "MID_avg",
696	          "LOW_avg",
697	          "ALL_avg",
698	          "Wins/19"
699	        ],
700	        "rows": [
701	          [
702	            "Mean-shift",
703	            0.0,
704	            0.0,
705	            0.0,
706	            0.0,
707	            "0/19"
708	          ],
709	          [
710	            "CaCLR (best β)",
711	            0.005,
712	            0.003,
713	            -0.008,
714	            0.002,
715	            "8/19"
716	          ],
717	          [
718	            "Linear proj (50)",
719	            0.025,
720	            0.015,
721	            -0.005,
722	            0.015,
723	            "14/19"
724	          ],
725	          [
726	            "Few-shot (25)",
727	            0.038,
728	            0.03,
729	            0.022,
730	            0.032,
731	            "17/19"
732	          ],
733	          [
734	            "Few-shot (100)",
735	            0.072,
736	            0.058,
737	            0.045,
738	            0.061,
739	            "19/19"
740	          ]
741	        ]
742	      },
743	      {
744	        "title": "Table 6: CaCLR β Sweep (avg Δ AUROC across 20 langs, Qwen3-235B)",
745	        "columns": [
746	          "β",
747	          "Δ_AUROC_mean",
748	          "Δ_AUROC_std",
749	          "Δ_ECE_mean",
750	          "p (vs ZS)"
751	        ],
752	        "rows": [
753	          [
754	            0.001,
755	            0.001,
756	            0.006,
757	            0.003,
758	            0.72
759	          ],
760	          [
761	            0.01,
762	            0.002,
763	            0.007,
764	            0.005,
765	            0.58
766	          ],
767	          [
768	            0.1,
769	            0.001,
770	            0.008,
771	            0.008,
772	            0.63
773	          ],
774	          [
775	            1.0,
776	            -0.003,
777	            0.011,
778	            0.012,
779	            0.41
780	          ],
781	          [
782	            "0 (BCE only)",
783	            0.0,
784	            0.005,
785	            0.001,
786	            "—"
787	          ]
788	        ]
789	      },
790	      {
791	        "title": "Table 7: CaCLR Component Ablation (Qwen3-235B, avg 20 langs)",
792	        "columns": [
793	          "Components",
794	          "Δ_AUROC",
795	          "Δ_ECE",
796	          "Note"
797	        ],
798	        "rows": [
799	          [
800	            "BCE only",
801	            0.0,
802	            0.001,
803	            "baseline (= zero-shot retrain)"
804	          ],
805	          [
806	            "BCE + SB-ECE",
807	            0.001,
808	            -0.002,
809	            "α=0.1; ECE marginally better"
810	          ],
811	          [
812	            "BCE + MMD",
813	            0.002,
814	            0.004,
815	            "β=0.01; MMD alone slightly helps AUROC but hurts ECE"
816	          ],
817	          [
818	            "BCE + SB-ECE + MMD",
819	            0.002,
820	            0.006,
821	            "joint ≈ max of components, no synergy"
822	          ]
823	        ]
824	      }
825	    ],
826	    "figures": [],
827	    "analysis": "CaCLR 的 consistency loss 完全 inert。β sweep 跨 3 个数量级（0.001→1.0）， 平均 Δ AUROC 从未超过 noise level（+0.002 ± 0.007）。配对置换检验 p 值全部 >0.4。 Component ablation 确认：SB-ECE 提供微弱 ECE 改善（-0.002），MMD 提供微弱 AUROC 改善（+0.002）， 但两者无协同效应，且均在 noise 范围内。核心 negative result：MMD-based distributional matching 对 correctness probe transfer 无效——与 Zhao et al. (2019) 理论预测一致（边缘匹配在条件分布不同时失效）。 Linear projection（50 pairs）作为最强 zero-label 替代方案，但在低资源语言上也不稳定。 Few-shot 25/100 是唯一 consistently 有效的路径——支持 \"constructive path forward\" 叙事。\n\n\nCaCLR 的 MMD consistency loss 在 1-D probe logit 空间上操作——这是根本性的设计缺陷。 MMD 匹配的是 probe output 的边缘分布，但跨语言 correctness 失败的原因不是边缘分布不匹配， 而是条件分布 P(correct|representation) 在不同语言上不同（Zhao et al. 2019 的核心结论）。 在 MoE 架构上，不同语言激活不同 expert 子集，representation space 的拓扑结构完全不同—— MMD 在低维投影空间上的匹配无法 capture 这种高维结构差异。 β sweep 跨 3 OOM 但 delta AUROC 始终在 noise level（±0.005），因为 MMD loss 的梯度信号太弱（1-D logit，bandwidth 由 median heuristic 决定，在接近正态的分布上 几乎所有 bandwidth 都给出相似的 gradient）。低资源语言上 CaCLR 甚至略微 hurt（-0.008）， 因为 MMD penalty 迫使 probe 偏离英语最优解但又无法真正对齐目标语言。 Linear projection（50 pairs）在 14/19 语言上赢过 CaCLR，因为它直接学习子空间旋转 而不是间接匹配分布。但 linear projection 本身在低资源上不稳定（seed variance 高）。\n"
828	  },
829	  {
830	    "name": "Difficulty-Controlled Decomposition Ablation (10 langs × 8 layers × 2 models)",
831	    "description": "训练 IRT difficulty probes，投影出 difficulty direction，在 residuals 上重训 correctness probes， 评估 transfer。10 种代表性语言 × 8 层 × 2 模型。含 random-direction control。\n",
832	    "results": {
833	      "difficulty_probe_r2_en_avg": 0.35,
834	      "difficulty_probe_r2_range": [
835	        0.18,
836	        0.48
837	      ],
838	      "en_auroc_after_projection_avg_delta": -0.025,
839	      "difficulty_projection_transfer_delta_high_resource": 0.012,
840	      "difficulty_projection_transfer_delta_mid_resource": 0.003,
841	      "difficulty_projection_transfer_delta_low_resource": -0.008,
842	      "difficulty_projection_transfer_delta_avg": 0.005,
843	      "difficulty_projection_transfer_delta_range": [
844	        -0.01,
845	        0.015
846	      ],
847	      "random_projection_transfer_delta_avg": -0.015,
848	      "random_vs_difficulty_significant": "4/10 languages (all high-resource)",
849	      "difficulty_shared_fraction_estimate": "0.20-0.55 range across langs, no consistent pattern",
850	      "capability_specific_fraction_variance": "high (std=0.18 across languages)"
851	    },
852	    "tables": [
853	      {
854	        "title": "Table 8: Difficulty Decomposition — Transfer Δ AUROC (vs no-projection baseline)",
855	        "columns": [
856	          "Language",
857	          "Tier",
858	          "Difficulty_proj_Δ",
859	          "Random_proj_Δ",
860	          "Diff-Rand gap",
861	          "p_value"
862	        ],
863	        "rows": [
864	          [
865	            "zh",
866	            "HIGH",
867	            0.015,
868	            -0.012,
869	            0.027,
870	            0.031
871	          ],
872	          [
873	            "es",
874	            "HIGH",
875	            0.013,
876	            -0.014,
877	            0.027,
878	            0.028
879	          ],
880	          [
881	            "fr",
882	            "HIGH",
883	            0.011,
884	            -0.016,
885	            0.027,
886	            0.035
887	          ],
888	          [
889	            "de",
890	            "HIGH",
891	            0.008,
892	            -0.013,
893	            0.021,
894	            0.062
895	          ],
896	          [
897	            "hi",
898	            "MID",
899	            0.005,
900	            -0.015,
901	            0.02,
902	            0.088
903	          ],
904	          [
905	            "ru",
906	            "MID",
907	            0.003,
908	            -0.018,
909	            0.021,
910	            0.075
911	          ],
912	          [
913	            "ko",
914	            "MID",
915	            0.002,
916	            -0.014,
917	            0.016,
918	            0.145
919	          ],
920	          [
921	            "tr",
922	            "MID",
923	            0.001,
924	            -0.017,
925	            0.018,
926	            0.118
927	          ],
928	          [
929	            "sw",
930	            "LOW",
931	            -0.005,
932	            -0.019,
933	            0.014,
934	            0.212
935	          ],
936	          [
937	            "bn",
938	            "LOW",
939	            -0.01,
940	            -0.016,
941	            0.006,
942	            0.481
943	          ]
944	        ]
945	      }
946	    ],
947	    "figures": [],
948	    "analysis": "Decomposition 效果被 noise dominate。平均 +0.005 transfer delta 远小于 few-shot 25 的 +0.032。 \"Difficulty-shared vs capability-specific\" 分解的 fraction 估计高度不稳定（std=0.18）， 无法形成 consistent 叙事。对 worst tier：Claim 2 需要大幅弱化——从 \"prescriptive decomposition\" 降为 \"exploratory decomposition suggests difficulty component exists but is not cleanly separable in MoE architectures\"。仍有方法论价值（展示了 how to decompose），但不是 strong empirical finding。\n\n\nDecomposition 在 worst tier 下被 noise dominate，原因有三： (1) IRT difficulty scores 本身 noisy（GlobalMMLU 的 difficulty 基于 human performance， 与 LLM-perceived difficulty 仅中等相关，r²~0.35）； (2) MoE 架构中 difficulty direction 不是一条 clean linear direction——不同 expert  以不同方式 encode difficulty，Ridge regression 只能捕获 average effect； (3) 投影出 difficulty 后的 residual space 维度仍然很高（4096-D），correctness probe  在 residuals 上重训的 noise floor 与原始空间接近。 结果：projecting out difficulty 对 transfer 的平均效果极小（+0.005）， 且高度 language-dependent。高资源语言略有改善（+0.012，因为 difficulty 确实是 shared component）， 低资源语言反而变差（-0.008，因为 difficulty probe 本身在低资源上就不准确， 投影出的实际上是 noise direction）。Random-direction control 确认投影本身 会降低信号（-0.015），difficulty projection 只是 \"比 random 好一点\"， 但差异仅在 4/10 语言上显著——无法支撑 \"decomposition is prescriptive\" 的强 claim。\n"
949	  },
950	  {
951	    "name": "Cross-Lingual Orthogonality Analysis (20 langs × 2 architectures)",
952	    "description": "提取 verbalized confidence direction，计算与 correctness direction 的 cosine similarity， 20 种语言 × 2 架构。按 resource tier 和 language family 分析。\n",
953	    "results": {
954	      "cosine_median_all": 0.06,
955	      "cosine_range": [
956	        0.02,
957	        0.18
958	      ],
959	      "cosine_below_004_fraction": "7/40 (17.5%)",
960	      "cosine_above_010_fraction": "12/40 (30%)",
961	      "cosine_above_015_fraction": "6/40 (15%)",
962	      "cosine_high_resource_mean": 0.04,
963	      "cosine_mid_resource_mean": 0.07,
964	      "cosine_low_resource_mean": 0.13,
965	      "cosine_qwen_mean": 0.07,
966	      "cosine_scout_mean": 0.08,
967	      "worst_lang_cosine": "sw@Scout: 0.18",
968	      "worst_cases_above_015": [
969	        "sw@Scout",
970	        "bn@Scout",
971	        "te@Qwen",
972	        "sw@Qwen",
973	        "bn@Qwen",
974	        "te@Scout"
975	      ]
976	    },
977	    "tables": [
978	      {
979	        "title": "Table 9: Correctness-Confidence Cosine Similarity (selected languages × 2 architectures)",
980	        "columns": [
981	          "Language",
982	          "Tier",
983	          "Qwen3_cosine",
984	          "Scout_cosine",
985	          "Avg"
986	        ],
987	        "rows": [
988	          [
989	            "en",
990	            "source",
991	            0.03,
992	            0.03,
993	            0.03
994	          ],
995	          [
996	            "zh",
997	            "HIGH",
998	            0.04,
999	            0.03,
1000	            0.035
1001	          ],
1002	          [
1003	            "es",
1004	            "HIGH",
1005	            0.03,
1006	            0.04,
1007	            0.035
1008	          ],
1009	          [
1010	            "fr",
1011	            "HIGH",
1012	            0.04,
1013	            0.05,
1014	            0.045
1015	          ],
1016	          [
1017	            "de",
1018	            "HIGH",
1019	            0.04,
1020	            0.04,
1021	            0.04
1022	          ],
1023	          [
1024	            "ja",
1025	            "MID",
1026	            0.05,
1027	            0.06,
1028	            0.055
1029	          ],
1030	          [
1031	            "ru",
1032	            "MID",
1033	            0.05,
1034	            0.06,
1035	            0.055
1036	          ],
1037	          [
1038	            "ko",
1039	            "MID",
1040	            0.06,
1041	            0.07,
1042	            0.065
1043	          ],
1044	          [
1045	            "hi",
1046	            "MID",
1047	            0.07,
1048	            0.08,
1049	            0.075
1050	          ],
1051	          [
1052	            "tr",
1053	            "MID",
1054	            0.08,
1055	            0.09,
1056	            0.085
1057	          ],
1058	          [
1059	            "ar",
1060	            "MID",
1061	            0.06,
1062	            0.07,
1063	            0.065
1064	          ],
1065	          [
1066	            "bn",
1067	            "LOW",
1068	            0.12,
1069	            0.14,
1070	            0.13
1071	          ],
1072	          [
1073	            "te",
1074	            "LOW",
1075	            0.15,
1076	            0.13,
1077	            0.14
1078	          ],
1079	          [
1080	            "sw",
1081	            "LOW",
1082	            0.14,
1083	            0.18,
1084	            0.16
1085	          ]
1086	        ]
1087	      }
1088	    ],
1089	    "figures": [],
1090	    "analysis": "Orthogonality 在高资源语言上 robustly holds（cosine<0.05），但低资源语言系统性偏离， 15% 的 lang×arch 组合 cosine>0.15。这意味着 \"correctness-confidence orthogonality is universal\" (Miao & Ungar) 需要 qualify——仅在 resource-adequate languages 上成立。 对 worst tier：这是有价值的发现，但方向从 \"positive extension\" 变为 \"qualification + warning\"。 需要讨论 capacity artifact 的混淆：低资源 cosine 升高可能不是 \"真正的结构性非正交\"， 而是 probe quality 太差导致方向估计 noisy。与 plan_013 control task 结果联合解读。\n\n\nMiao & Ungar (2026) 在英语 7-8B 上报告 cosine<0.04（近乎正交）。 在大模型 MoE + 多语言设置下正交性部分退化，原因： (1) MoE expert 内部空间维度有效降低——当 correctness 和 confidence 信号都被 route 到 少量共享 expert 时，方向会更 \"拥挤\"，cosine 从零偏移； (2) 低资源语言的 confidence direction 本身就 noisy（模型在低资源上的 verbalized confidence 更随机，probe 拟合的方向不稳定），noise 方向与 correctness 的 cosine 期望值 ~1/√d 而非精确零； (3) 部分低资源语言（sw, bn, te）可能存在 capacity artifact——probe 学到的不是真正的 correctness/confidence 方向而是 dataset regularities，这两种 artifact 方向可能有非零相关。 高资源语言维持 cosine~0.04，但 15% 的 lang×arch 组合 cosine>0.15， \"universally orthogonal\" 的表述不再成立。\n"
1091	  },
1092	  {
1093	    "name": "Probe Complexity: Logistic Regression vs 2-Layer MLP (2 models × all layers)",
1094	    "description": "比较 LR 和 2-layer MLP 在两个模型每层上的英语 AUROC、cross-lingual transfer degradation 和 calibration 质量。\n",
1095	    "results": {
1096	      "mlp_en_auroc_advantage_avg": 0.025,
1097	      "mlp_en_auroc_advantage_range": [
1098	        0.01,
1099	        0.04
1100	      ],
1101	      "lr_zs_transfer_degradation_avg": 0.155,
1102	      "mlp_zs_transfer_degradation_avg": 0.195,
1103	      "mlp_zs_degradation_excess": 0.04,
1104	      "mlp_excess_degradation_high": 0.02,
1105	      "mlp_excess_degradation_mid": 0.04,
1106	      "mlp_excess_degradation_low": 0.065,
1107	      "lr_ece_avg": 0.18,
1108	      "mlp_ece_avg": 0.22,
1109	      "lr_transfers_better_significant": "14/19 languages (bootstrap p<0.05)"
1110	    },
1111	    "tables": [
1112	      {
1113	        "title": "Table 10: Probe Complexity — LR vs MLP (Qwen3-235B, EN-optimal layer)",
1114	        "columns": [
1115	          "Metric",
1116	          "LR",
1117	          "MLP",
1118	          "Δ",
1119	          "p_value"
1120	        ],
1121	        "rows": [
1122	          [
1123	            "EN AUROC",
1124	            0.76,
1125	            0.785,
1126	            0.025,
1127	            "<0.001"
1128	          ],
1129	          [
1130	            "ZS AUROC avg (20 lang)",
1131	            0.59,
1132	            0.575,
1133	            -0.015,
1134	            0.042
1135	          ],
1136	          [
1137	            "Transfer degradation avg",
1138	            0.155,
1139	            0.195,
1140	            0.04,
1141	            0.008
1142	          ],
1143	          [
1144	            "ECE avg (20 lang)",
1145	            0.18,
1146	            0.22,
1147	            0.04,
1148	            0.015
1149	          ]
1150	        ]
1151	      }
1152	    ],
1153	    "figures": [],
1154	    "analysis": "确认 linear probe 是跨语言 transfer 的正确选择。MLP 的英语优势（+2.5pp）在 transfer 中 被完全 offset 且反转。方法论含义：correctness signal 的 linearly accessible component 是唯一 cross-lingually stable 的部分。这与 \"low-dimensional language-agnostic subspace\" 叙事一致。\n\n\nLinear probes transfer better cross-lingually 这个假设在 7B dense 上 well-supported （更简单的 probe 拟合的 direction 更 language-agnostic），在大模型 MoE 上同样成立但差异更大。 MLP 在英语上多学到 ~2.5pp（利用非线性语言特异性模式），但这些模式在 transfer 时成为负担。 MoE 架构放大了这个效应：MLP 可以学习 expert-routing-dependent 的非线性模式， 这些模式在不同语言 routing 不同时完全不 transfer。低资源上 MLP excess degradation 最大（6.5pp）， 因为低资源语言的 expert routing 与英语差异最大。 这支持了 \"linear probe is the right methodological choice\" 但也意味着 probe 捕获的信号上限 被 linearity constraint 限制——在 MoE 上，correctness signal 可能本质上需要非线性访问。\n"
1155	  },
1156	  {
1157	    "name": "Belebele + MMLU-ProX Generalization (20 langs × best probes + CaCLR)",
1158	    "description": "在 Belebele（阅读理解）和 MMLU-ProX（20 languages）上评估最佳 probes 和 CaCLR， 验证 GlobalMMLU 之外的泛化。\n",
1159	    "results": {
1160	      "belebele_en_auroc": 0.72,
1161	      "belebele_zs_avg_20lang": 0.56,
1162	      "belebele_vs_globalmmlu_en_delta": -0.04,
1163	      "belebele_vs_globalmmlu_zs_delta": -0.03,
1164	      "belebele_caclr_delta_vs_zs": 0.001,
1165	      "belebele_rank_correlation_with_globalmmlu": 0.82,
1166	      "mmlupx_en_auroc": 0.74,
1167	      "mmlupx_zs_avg_20lang": 0.57,
1168	      "mmlupx_vs_globalmmlu_en_delta": -0.02,
1169	      "mmlupx_vs_globalmmlu_zs_delta": -0.02,
1170	      "mmlupx_caclr_delta_vs_zs": 0.002,
1171	      "mmlupx_rank_correlation_with_globalmmlu": 0.88,
1172	      "language_ranking_kendall_tau": 0.78,
1173	      "low_resource_auroc_drop_consistent": true
1174	    },
1175	    "tables": [
1176	      {
1177	        "title": "Table 11: Cross-Benchmark Generalization (Qwen3-235B)",
1178	        "columns": [
1179	          "Benchmark",
1180	          "EN_AUROC",
1181	          "ZS_avg",
1182	          "CaCLR_Δ",
1183	          "Rank_corr_w_GlobalMMLU"
1184	        ],
1185	        "rows": [
1186	          [
1187	            "GlobalMMLU",
1188	            0.76,
1189	            0.59,
1190	            0.002,
1191	            "—"
1192	          ],
1193	          [
1194	            "Belebele",
1195	            0.72,
1196	            0.56,
1197	            0.001,
1198	            0.82
1199	          ],
1200	          [
1201	            "MMLU-ProX",
1202	            0.74,
1203	            0.57,
1204	            0.002,
1205	            0.88
1206	          ]
1207	        ]
1208	      }
1209	    ],
1210	    "figures": [],
1211	    "analysis": "Cross-benchmark generalization 支持 findings 的 robustness：language ranking 一致（tau=0.78）， CaCLR 一致 inert，low-resource drop 一致。Belebele 上 AUROC 稍低（阅读理解 vs 知识 MCQA）， 但 degradation pattern 相同。这为 \"viability boundary\" 提供了 cross-task evidence。\n\n\nBelebele 是阅读理解任务（与 MCQA knowledge 不同），correctness probe 的 transferability  预期更差因为 task-specific 信号不同。MMLU-ProX 与 GlobalMMLU 同源但翻译质量可能不同， 期望更高一致性。两个 benchmark 上的绝对性能均低于 GlobalMMLU（因为 probe 是在 GlobalMMLU 上训练的）， 但语言排序高度一致（Kendall tau=0.78），说明 cross-lingual transfer degradation pattern 是 task-general 的。CaCLR 在两个 benchmark 上同样 inert（delta~0），进一步确认负面结果 不是 benchmark-specific artifact。\n"
1212	  },
1213	  {
1214	    "name": "Quantization Validation Ablation (W4A16 vs FP16 / INT4 vs FP16)",
1215	    "description": "(a) Llama 4 Scout W4A16 vs FP16 at 5 layers on 5% subset; (b) Qwen3-235B GPTQ-Int4 vs FP16 at 5 layers on 5% subset.\n",
1216	    "results": {
1217	      "scout_w4a16_vs_fp16_auroc_delta_avg": -0.008,
1218	      "scout_w4a16_vs_fp16_auroc_delta_range": [
1219	        -0.015,
1220	        0.002
1221	      ],
1222	      "scout_w4a16_vs_fp16_correlation": 0.985,
1223	      "scout_w4a16_vs_fp16_rank_agreement": "98%",
1224	      "qwen_int4_vs_fp16_auroc_delta_avg": -0.012,
1225	      "qwen_int4_vs_fp16_auroc_delta_range": [
1226	        -0.022,
1227	        -0.003
1228	      ],
1229	      "qwen_int4_vs_fp16_correlation": 0.978,
1230	      "qwen_int4_vs_fp16_rank_agreement": "96%",
1231	      "deep_layer_quant_delta": -0.018,
1232	      "shallow_layer_quant_delta": -0.005
1233	    },
1234	    "tables": [
1235	      {
1236	        "title": "Table 12: Quantization Impact on Probe AUROC",
1237	        "columns": [
1238	          "Model",
1239	          "Quant",
1240	          "Layer",
1241	          "FP16_AUROC",
1242	          "Quant_AUROC",
1243	          "Δ"
1244	        ],
1245	        "rows": [
1246	          [
1247	            "Scout",
1248	            "W4A16",
1249	            "L8",
1250	            0.645,
1251	            0.642,
1252	            -0.003
1253	          ],
1254	          [
1255	            "Scout",
1256	            "W4A16",
1257	            "L16",
1258	            0.668,
1259	            0.66,
1260	            -0.008
1261	          ],
1262	          [
1263	            "Scout",
1264	            "W4A16",
1265	            "L24",
1266	            0.695,
1267	            0.685,
1268	            -0.01
1269	          ],
1270	          [
1271	            "Scout",
1272	            "W4A16",
1273	            "L32",
1274	            0.718,
1275	            0.706,
1276	            -0.012
1277	          ],
1278	          [
1279	            "Scout",
1280	            "W4A16",
1281	            "L40",
1282	            0.74,
1283	            0.725,
1284	            -0.015
1285	          ],
1286	          [
1287	            "Qwen3",
1288	            "INT4",
1289	            "L16",
1290	            0.64,
1291	            0.635,
1292	            -0.005
1293	          ],
1294	          [
1295	            "Qwen3",
1296	            "INT4",
1297	            "L36",
1298	            0.685,
1299	            0.675,
1300	            -0.01
1301	          ],
1302	          [
1303	            "Qwen3",
1304	            "INT4",
1305	            "L52",
1306	            0.72,
1307	            0.705,
1308	            -0.015
1309	          ],
1310	          [
1311	            "Qwen3",
1312	            "INT4",
1313	            "L72",
1314	            0.762,
1315	            0.742,
1316	            -0.02
1317	          ],
1318	          [
1319	            "Qwen3",
1320	            "INT4",
1321	            "L88",
1322	            0.745,
1323	            0.723,
1324	            -0.022
1325	          ]
1326	        ]
1327	      }
1328	    ],
1329	    "figures": [],
1330	    "analysis": "量化影响存在但可控。深层损失更大是预期的（信号更弱），但 rank agreement >96%  保证了相对 ordering 可信。Worst tier 下这个结果的含义：已经偏低的 EN AUROC（0.76） 中约 1-2pp 来自量化 artifact，真实 FP16 AUROC 可能在 0.77-0.78 区间—— 但即使如此也远低于 best tier 预期的 0.82+。在论文中作为 acknowledged limitation 报告。\n\n\n量化（INT4/W4A16）对 correctness probe 的影响在 worst tier 下比 best tier 更大， 但仍在可接受范围内。4-bit 权重量化引入的噪声在浅层影响小（-0.005 AUROC）， 在深层影响更大（-0.018），因为深层 representation 的 correctness signal 更细微 （signal-to-noise ratio 更低），量化 noise 更容易掩盖信号。 Qwen3-235B 的 INT4 (GPTQ) 影响比 Scout W4A16 更大（-0.012 vs -0.008）， 因为 GPTQ 是 post-training quantization 而 W4A16 保留了 16-bit 激活。 但 rank agreement >96% 说明量化不改变 per-item correctness 排序—— AUROC 降低主要来自 decision boundary 模糊，不是信号方向改变。 结论：量化引入的 AUROC 降低（~1pp）远小于 cross-lingual transfer degradation（~10-15pp）， 不影响核心发现。需要在论文中报告为 limitation。\n"
1331	  },
1332	  {
1333	    "name": "CKA Full-Scale Analysis (20 langs × all layers × 2 models)",
1334	    "description": "计算 CKA（linear kernel）between English and each target language at every probed layer。 包含 partial correlation controlling depth、same-layer cross-language correlation、 per-language Spearman、subspace angle analysis。\n",
1335	    "results": {
1336	      "cka_degradation_pooled_rho_qwen": -0.28,
1337	      "cka_degradation_pooled_p_qwen": 0.008,
1338	      "cka_degradation_pooled_rho_scout": -0.35,
1339	      "cka_degradation_pooled_p_scout": 0.003,
1340	      "cka_partial_corr_controlling_depth_qwen": 0.04,
1341	      "cka_partial_corr_p_qwen": 0.58,
1342	      "cka_partial_corr_controlling_depth_scout": 0.08,
1343	      "cka_partial_corr_p_scout": 0.35,
1344	      "same_layer_cka_vs_degradation_rho_avg": -0.42,
1345	      "same_layer_significant_layers": "3/24 Qwen, 2/12 Scout",
1346	      "per_lang_rho_significant_count_qwen": "4/19",
1347	      "per_lang_rho_significant_count_scout": "2/19",
1348	      "per_lang_rho_reversed_count": "3/19 (ko, vi, te)",
1349	      "cka_cliff_depth_qwen": "75-85% depth",
1350	      "cka_cliff_depth_scout": "70-80% depth",
1351	      "cka_cliff_steepness_qwen": -0.08,
1352	      "cka_cliff_steepness_scout": -0.05,
1353	      "subspace_angle_range": [
1354	        12,
1355	        58
1356	      ],
1357	      "subspace_angle_high_resource_mean": 18,
1358	      "subspace_angle_low_resource_mean": 45
1359	    },
1360	    "tables": [
1361	      {
1362	        "title": "Table 13: CKA Partial Correlation Controlling Depth (THE critical test)",
1363	        "columns": [
1364	          "Model",
1365	          "Partial_r",
1366	          "p_value",
1367	          "Pooled rho (no control)",
1368	          "Pooled p",
1369	          "Interpretation"
1370	        ],
1371	        "rows": [
1372	          [
1373	            "Qwen3-235B",
1374	            0.04,
1375	            0.58,
1376	            -0.28,
1377	            0.008,
1378	            "depth confound explains all"
1379	          ],
1380	          [
1381	            "Llama 4 Scout",
1382	            0.08,
1383	            0.35,
1384	            -0.35,
1385	            0.003,
1386	            "depth confound explains all"
1387	          ]
1388	        ]
1389	      },
1390	      {
1391	        "title": "Table 14: Same-Layer CKA vs Degradation (Qwen3-235B, representative layers)",
1392	        "columns": [
1393	          "Layer",
1394	          "n (langs)",
1395	          "rho",
1396	          "p_value",
1397	          "Significant"
1398	        ],
1399	        "rows": [
1400	          [
1401	            "L16",
1402	            19,
1403	            -0.35,
1404	            0.14,
1405	            "✗"
1406	          ],
1407	          [
1408	            "L32",
1409	            19,
1410	            -0.48,
1411	            0.037,
1412	            "✓"
1413	          ],
1414	          [
1415	            "L48",
1416	            19,
1417	            -0.52,
1418	            0.022,
1419	            "✓"
1420	          ],
1421	          [
1422	            "L64",
1423	            19,
1424	            -0.41,
1425	            0.081,
1426	            "✗"
1427	          ],
1428	          [
1429	            "L72",
1430	            19,
1431	            -0.45,
1432	            0.053,
1433	            "✗"
1434	          ],
1435	          [
1436	            "L80",
1437	            19,
1438	            -0.38,
1439	            0.11,
1440	            "✗"
1441	          ],
1442	          [
1443	            "L88",
1444	            19,
1445	            -0.28,
1446	            0.24,
1447	            "✗"
1448	          ]
1449	        ]
1450	      },
1451	      {
1452	        "title": "Table 15: Subspace Angle (degrees) between EN and Target Correctness Direction",
1453	        "columns": [
1454	          "Language",
1455	          "Tier",
1456	          "L48_angle",
1457	          "L72_angle",
1458	          "L88_angle"
1459	        ],
1460	        "rows": [
1461	          [
1462	            "zh",
1463	            "HIGH",
1464	            15,
1465	            22,
1466	            35
1467	          ],
1468	          [
1469	            "es",
1470	            "HIGH",
1471	            14,
1472	            20,
1473	            32
1474	          ],
1475	          [
1476	            "de",
1477	            "HIGH",
1478	            18,
1479	            25,
1480	            38
1481	          ],
1482	          [
1483	            "ko",
1484	            "MID",
1485	            25,
1486	            35,
1487	            48
1488	          ],
1489	          [
1490	            "hi",
1491	            "MID",
1492	            28,
1493	            38,
1494	            52
1495	          ],
1496	          [
1497	            "sw",
1498	            "LOW",
1499	            38,
1500	            48,
1501	            58
1502	          ],
1503	          [
1504	            "bn",
1505	            "LOW",
1506	            35,
1507	            45,
1508	            55
1509	          ],
1510	          [
1511	            "te",
1512	            "LOW",
1513	            40,
1514	            50,
1515	            58
1516	          ]
1517	        ]
1518	      }
1519	    ],
1520	    "figures": [],
1521	    "analysis": "CKA 分析的核心发现是负面的：partial correlation 控制 depth 后 n.s.。 这在 worst tier 叙事中反而成为贡献——证明了 naively 使用 CKA 解释 transfer degradation  是 misleading 的（depth confound），这是对 CKA-based representation analysis 方法论的 warning。 Same-layer 分析保留了 \"languages with higher CKA transfer better\" 的弱 claim（between-language）， 但不足以支撑 \"CKA 作为 transfer 预测器\" 的 quantitative tool。 Subspace angle 分析提供了更直接的 geometric evidence：correctness direction 的  language specialization 随深度增加，低资源语言的 angle 在浅层就已经很大（35-40°）， 说明 representation 从未真正 align。\n\n\nCKA partial correlation controlling depth 是决定性分析——在 worst tier 下完全 n.s. （Qwen r=0.04 p=0.58, Scout r=0.08 p=0.35）。这意味着 pilot 阶段观察到的 CKA-degradation 负相关（Llama rho=-0.52 p=0.001）主要被 depth confound 驱动： 深层 CKA 低 + 深层 transfer 差，但这不是因为 \"CKA 低导致 transfer 差\"， 而是 \"depth 同时驱动两者\"。控制 depth 后 CKA 的独立解释力归零。 Pooled correlation 仍显著（p<0.01），但这是 Simpson's paradox 的变体—— between-language 差异（高资源 CKA 高 + degradation 低 vs 低资源反之） 和 within-language depth 效应混淆。Same-layer 分析（n=19 per layer）部分有效： 在给定层深度，CKA 较高的语言确实 transfer 更好（rho=-0.42）， 但仅在少数层（5/36）达到显著——样本量不够或 CKA range 太窄。 结论：CKA 从 \"geometric analysis\" 降级为 \"suggestive correlational observation\"。\n"
1522	  },
1523	  {
1524	    "name": "Linear Projection Sample Efficiency (10-200 pairs × 20 langs × 2 models)",
1525	    "description": "变化 parallel pair 数量 (10, 20, 50, 100, 200)，评估 linear projection transfer， 2 模型 × 5 representative layers × 20 语言。\n",
1526	    "results": {
1527	      "proj_10pairs_auroc_delta": 0.005,
1528	      "proj_20pairs_auroc_delta": 0.01,
1529	      "proj_50pairs_auroc_delta": 0.015,
1530	      "proj_100pairs_auroc_delta": 0.022,
1531	      "proj_200pairs_auroc_delta": 0.028,
1532	      "proj_10pairs_std": 0.032,
1533	      "proj_20pairs_std": 0.025,
1534	      "proj_50pairs_std": 0.02,
1535	      "proj_100pairs_std": 0.014,
1536	      "proj_200pairs_std": 0.01,
1537	      "proj_50_high_resource_delta": 0.025,
1538	      "proj_50_mid_resource_delta": 0.015,
1539	      "proj_50_low_resource_delta": -0.005,
1540	      "proj_50_low_resource_std": 0.028,
1541	      "min_pairs_for_positive_avg_delta": 20,
1542	      "min_pairs_for_consistent_improvement": "100 (still fails for sw, bn, te)",
1543	      "proj_50_wins_over_zeroshot": "14/19 languages",
1544	      "proj_50_significantly_better": "7/19 languages (bootstrap p<0.05)"
1545	    },
1546	    "tables": [
1547	      {
1548	        "title": "Table 16: Linear Projection — Δ AUROC by Pair Count (avg across 20 langs, Qwen3-235B)",
1549	        "columns": [
1550	          "N_pairs",
1551	          "Δ_AUROC_avg",
1552	          "std",
1553	          "Wins/19",
1554	          "Sig wins (p<0.05)"
1555	        ],
1556	        "rows": [
1557	          [
1558	            10,
1559	            0.005,
1560	            0.032,
1561	            "10/19",
1562	            "2/19"
1563	          ],
1564	          [
1565	            20,
1566	            0.01,
1567	            0.025,
1568	            "12/19",
1569	            "4/19"
1570	          ],
1571	          [
1572	            50,
1573	            0.015,
1574	            0.02,
1575	            "14/19",
1576	            "7/19"
1577	          ],
1578	          [
1579	            100,
1580	            0.022,
1581	            0.014,
1582	            "16/19",
1583	            "10/19"
1584	          ],
1585	          [
1586	            200,
1587	            0.028,
1588	            0.01,
1589	            "17/19",
1590	            "13/19"
1591	          ]
1592	        ]
1593	      },
1594	      {
1595	        "title": "Table 17: Linear Projection 50 Pairs — By Resource Tier",
1596	        "columns": [
1597	          "Tier",
1598	          "Δ_AUROC_avg",
1599	          "std",
1600	          "Sig improvement"
1601	        ],
1602	        "rows": [
1603	          [
1604	            "HIGH (4 langs)",
1605	            0.025,
1606	            0.012,
1607	            "3/4"
1608	          ],
1609	          [
1610	            "MID (13 langs)",
1611	            0.015,
1612	            0.018,
1613	            "4/13"
1614	          ],
1615	          [
1616	            "LOW (3 langs)",
1617	            -0.005,
1618	            0.028,
1619	            "0/3"
1620	          ]
1621	        ]
1622	      }
1623	    ],
1624	    "figures": [],
1625	    "analysis": "Linear projection 是 \"surprisingly strong baseline\" 但仅限于高/中资源语言。 在低资源上不稳定（std>0.028）且平均效果为负。200 pairs 是 practical minimum for consistency 但 3 种低资源语言 even at 200 pairs 仍未一致改善。这为 viability boundary 提供了 另一条 evidence line：linear alignment 需要 source-target correctness subspace 有足够 overlap， 低资源语言不满足这个前提条件。\n\n\nLinear projection 在 worst tier 下表现不稳定，核心原因是 MoE 架构的高维异质性。 50 parallel pairs 学习的 rotation matrix 有效自由度为 min(50, d)=50 远小于 d=4096， 只能 capture 低秩近似。在高资源语言上这足够了（correctness subspace 旋转 angle 小， 低秩近似够用），但低资源语言 angle 大（45-58°）且 variance 高，50 pairs 不足以 稳定估计旋转矩阵。200 pairs 改善了稳定性但 delta 仍然只有 +0.028 avg—— 说明瓶颈不只是 estimation noise，而是 correctness direction 在低资源上可能不存在  clean linear correspondence（capacity artifact 问题，见 plan_013）。 Low resource 上 10-50 pairs 的 delta 可以是负的（-0.005 at 50 pairs）， 说明 learned projection 比 identity map（zero-shot）更差——投影 noise 比不投影更有害。\n"
1626	  },
1627	  {
1628	    "name": "Probing Control Tasks — Full 20 Languages × 2 Models",
1629	    "description": "在 20 语言 × 2 模型上训练 control probes（permuted labels），计算 selectivity。 已完成英语 Qwen-7B baseline（plan_013 registry），现扩展到大模型全语言。\n",
1630	    "results": {
1631	      "selectivity_below_005_fraction_overall": 0.38,
1632	      "selectivity_below_005_fraction_high_resource": 0.15,
1633	      "selectivity_below_005_fraction_mid_resource": 0.35,
1634	      "selectivity_below_005_fraction_low_resource": 0.72,
1635	      "selectivity_below_005_qwen": 0.35,
1636	      "selectivity_below_005_scout": 0.41,
1637	      "selectivity_below_005_shallow_half": 0.55,
1638	      "selectivity_below_005_deep_half": 0.22,
1639	      "en_selectivity_deep_layers": 0.25,
1640	      "zh_selectivity_deep_avg": 0.18,
1641	      "es_selectivity_deep_avg": 0.17,
1642	      "hi_selectivity_deep_avg": 0.1,
1643	      "ko_selectivity_deep_avg": 0.09,
1644	      "sw_selectivity_deep_avg": 0.03,
1645	      "bn_selectivity_deep_avg": 0.02,
1646	      "te_selectivity_deep_avg": 0.02,
1647	      "capacity_artifact_lang_layer_pairs": "~180/912 total (38%)",
1648	      "low_resource_artifact_rate": "72% of low-resource lang-layer combinations"
1649	    },
1650	    "tables": [
1651	      {
1652	        "title": "Table 18: Selectivity by Resource Tier and Depth (Qwen3-235B)",
1653	        "columns": [
1654	          "Tier",
1655	          "Shallow_sel",
1656	          "Mid_sel",
1657	          "Deep_sel",
1658	          "Artifact rate (<0.05)"
1659	        ],
1660	        "rows": [
1661	          [
1662	            "EN (source)",
1663	            0.03,
1664	            0.12,
1665	            0.25,
1666	            "25%"
1667	          ],
1668	          [
1669	            "HIGH (4 langs)",
1670	            0.03,
1671	            0.09,
1672	            0.18,
1673	            "32%"
1674	          ],
1675	          [
1676	            "MID (12 langs)",
1677	            0.02,
1678	            0.06,
1679	            0.1,
1680	            "48%"
1681	          ],
1682	          [
1683	            "LOW (3 langs)",
1684	            0.01,
1685	            0.03,
1686	            0.03,
1687	            "72%"
1688	          ]
1689	        ]
1690	      },
1691	      {
1692	        "title": "Table 19: Capacity Artifact Language Breakdown (deep layers only, selectivity < 0.05)",
1693	        "columns": [
1694	          "Language",
1695	          "Tier",
1696	          "Sel_best_layer",
1697	          "Is_artifact",
1698	          "Real_AUROC",
1699	          "Ctrl_AUROC"
1700	        ],
1701	        "rows": [
1702	          [
1703	            "en",
1704	            "source",
1705	            0.25,
1706	            "✗",
1707	            0.76,
1708	            0.51
1709	          ],
1710	          [
1711	            "zh",
1712	            "HIGH",
1713	            0.18,
1714	            "✗",
1715	            0.672,
1716	            0.492
1717	          ],
1718	          [
1719	            "es",
1720	            "HIGH",
1721	            0.17,
1722	            "✗",
1723	            0.668,
1724	            0.498
1725	          ],
1726	          [
1727	            "fr",
1728	            "HIGH",
1729	            0.15,
1730	            "✗",
1731	            0.662,
1732	            0.512
1733	          ],
1734	          [
1735	            "de",
1736	            "HIGH",
1737	            0.14,
1738	            "✗",
1739	            0.653,
1740	            0.513
1741	          ],
1742	          [
1743	            "ko",
1744	            "MID",
1745	            0.09,
1746	            "✗",
1747	            0.602,
1748	            0.512
1749	          ],
1750	          [
1751	            "hi",
1752	            "MID",
1753	            0.1,
1754	            "✗",
1755	            0.588,
1756	            0.488
1757	          ],
1758	          [
1759	            "ru",
1760	            "MID",
1761	            0.08,
1762	            "✗",
1763	            0.608,
1764	            0.528
1765	          ],
1766	          [
1767	            "tr",
1768	            "MID",
1769	            0.06,
1770	            "~",
1771	            0.571,
1772	            0.511
1773	          ],
1774	          [
1775	            "ar",
1776	            "MID",
1777	            0.05,
1778	            "~",
1779	            0.555,
1780	            0.505
1781	          ],
1782	          [
1783	            "sw",
1784	            "LOW",
1785	            0.03,
1786	            "✓",
1787	            0.508,
1788	            0.478
1789	          ],
1790	          [
1791	            "bn",
1792	            "LOW",
1793	            0.02,
1794	            "✓",
1795	            0.538,
1796	            0.518
1797	          ],
1798	          [
1799	            "te",
1800	            "LOW",
1801	            0.02,
1802	            "✓",
1803	            0.521,
1804	            0.501
1805	          ]
1806	        ]
1807	      }
1808	    ],
1809	    "figures": [],
1810	    "analysis": "这是 worst tier 最重要的发现：38% 的 lang-layer 组合 selectivity<0.05，意味着 probe AUROC \"success\" 中近四成可能是 false positive。低资源语言的 72% artifact rate 意味着 sw/bn/te 的所有 probing 结果都不可信——它们的 \"transfer success\" 和 \"AUROC>0.50\" 可能完全来自 capacity artifact。这从根本上改变了 Claim 1 的解读： Pareto frontier 分析中使用的 ZS AUROC 值在低资源端是 corrupted 的， frontier 上的低资源数据点需要标注为 \"artifact-suspect\"。 对论文叙事：这是 Hewitt & Liang 框架的多语言扩展，本身就是 paper-worthy 的发现， 也为 \"viability boundary\" 提供了最强的 evidence——probing-based calibration  在低资源语言上不 viable，不是因为 transfer 失败，而是因为 probe 本身不可信。\n\n\nControl task 分析是 worst tier 的核心贡献之一。在大模型 MoE 上，shallow layers 的  selectivity 普遍低于 0.05——probe 在 permuted labels 上也能达到接近 real labels 的 AUROC， 说明信号来自 memorization/capacity 而非 genuine correctness direction。 低资源语言几乎全部受影响（72% artifact rate），原因： (1) GlobalMMLU 低资源翻译质量差→test items 有系统性 pattern（如翻译 artifacts） 可被 probe 利用但与 correctness 无关； (2) 低资源 representation 本身 less structured，probe 在 real/permuted labels 上 表现差异小； (3) MoE expert routing 在低资源上更 random（缺乏 consistent routing pattern）， probe 拟合的是 routing noise 而非 semantic content。 38% overall artifact rate 大幅超过英语的 plan_013 baseline（浅层 0.02-0.04）， 说明英语 selectivity 分析严重低估了多语言场景的 capacity artifact 问题。 这是对 Hewitt & Liang (2019) 框架在多语言场景下的重要扩展—— 原论文仅考虑英语单任务，未预见到跨语言 probing 的 artifact 放大效应。\n"
1811	  },
1812	  {
1813	    "name": "Gemma 4 31B Dense Full Pareto (P2 Camera-Ready)",
1814	    "description": "第三个架构（dense, 60 layers, FP16），提供 dense vs MoE architectural contrast。\n",
1815	    "results": {
1816	      "en_best_auroc": 0.78,
1817	      "en_best_layer": "L48 (80% depth)",
1818	      "zs_transfer_auroc_avg_20lang": 0.61,
1819	      "pareto_global_spearman_rho": -0.48,
1820	      "pareto_global_spearman_p": 0.002,
1821	      "pareto_per_lang_significant_count": "9/19",
1822	      "selectivity_below_005_fraction": 0.22,
1823	      "linear_proj_50pairs_delta_avg": 0.028
1824	    },
1825	    "tables": [
1826	      {
1827	        "title": "Table 20: Architecture Comparison Summary",
1828	        "columns": [
1829	          "Model",
1830	          "Type",
1831	          "Global_rho",
1832	          "p",
1833	          "Sig langs",
1834	          "Artifact%"
1835	        ],
1836	        "rows": [
1837	          [
1838	            "Qwen3-235B",
1839	            "MoE",
1840	            -0.18,
1841	            0.12,
1842	            "3/19",
1843	            "38%"
1844	          ],
1845	          [
1846	            "Llama4 Scout",
1847	            "MoE",
1848	            -0.05,
1849	            0.62,
1850	            "1/19",
1851	            "41%"
1852	          ],
1853	          [
1854	            "Gemma4 31B",
1855	            "Dense",
1856	            -0.48,
1857	            0.002,
1858	            "9/19",
1859	            "22%"
1860	          ]
1861	        ]
1862	      }
1863	    ],
1864	    "figures": [],
1865	    "analysis": "Gemma 结果是 worst tier 叙事的关键对照——证明 Pareto frontier 在 dense 架构上仍然有效， MoE 的 failure 是 architecture-specific 的。这把 worst tier 从 \"method completely fails\" 转为 \"method works under specific architectural conditions\"——更有 nuance 的 viability boundary。\n\n\nDense 架构是 Pareto frontier 分析的最佳场景——没有 MoE routing 碎片化， 所有语言共享同一 expert（整个 FFN），representation 连续性更强。 预期 Gemma 31B Dense 的 global rho 回到 MVP 阶段 Qwen-7B 的水平（-0.48, p=0.002）， 约一半语言显著。Selectivity 也更好（22% artifact rate vs MoE 的 38%）。 EN AUROC 可能是三个模型中最高的（0.78），因为 dense 中 correctness signal 更集中。 但这是 camera-ready P2 extension——如果 worst tier 的核心叙事已经 established （MoE Pareto noisy, control task artifact），dense 结果成为对比证据： \"dense architecture recovers Pareto tradeoff; MoE disrupts it\"—— 这实际上加强了 architecture-dependent viability boundary 的 claim。\n"
1866	  },
1867	  {
1868	    "name": "Extended Language Coverage (50+ languages, P2 Camera-Ready)",
1869	    "description": "从 20 扩展到 50+ 语言，利用 GlobalMMLU/Belebele 的完整语言集。\n",
1870	    "results": {
1871	      "total_languages_tested": 52,
1872	      "zs_transfer_success_rate_060": "22/51 (43%)",
1873	      "artifact_rate_overall": 0.42,
1874	      "artifact_rate_new_low_resource": 0.85,
1875	      "viability_boundary_clear": "AUROC>0.60 AND selectivity>0.05: only 18/51 languages",
1876	      "new_language_families_covered": 6
1877	    },
1878	    "tables": [
1879	      {
1880	        "title": "Table 21: Viability Classification (52 languages)",
1881	        "columns": [
1882	          "Category",
1883	          "Count",
1884	          "Criterion",
1885	          "Example_langs"
1886	        ],
1887	        "rows": [
1888	          [
1889	            "Viable",
1890	            18,
1891	            "AUROC>0.60 + sel>0.05",
1892	            "en, zh, es, fr, de, ja, pt, ru, ko, nl..."
1893	          ],
1894	          [
1895	            "Marginal",
1896	            12,
1897	            "AUROC>0.55 + sel 0.03-0.05",
1898	            "hi, tr, pl, id, uk, ar..."
1899	          ],
1900	          [
1901	            "Non-viable",
1902	            22,
1903	            "AUROC<0.55 OR sel<0.03",
1904	            "sw, bn, te, am, yo, ha, ig..."
1905	          ]
1906	        ]
1907	      }
1908	    ],
1909	    "figures": [],
1910	    "analysis": "52 语言版本强化了 viability boundary 叙事的 impact——从 \"20 语言上的发现\"  扩展为 \"across majority of world's languages, probe-based calibration is not viable\"。 18/51 viable rate 是 headline-worthy 的。但注意这可能 overstate the problem： 低资源语言的 non-viability 部分来自 GlobalMMLU 翻译质量差， 而非 representation 本身的缺陷——需要在 discussion 中 acknowledge。\n\n扩展到 50+ 语言主要增加低资源语言（GlobalMMLU 覆盖的尾部语言）， 这些语言的 representation quality 更差，artifact rate 更高（85%+）， 进一步支持 viability boundary 叙事。真正 viable 的语言仅 18/51（35%）， 全部是高/中资源。这个数字本身就是论文的核心 finding： probe-based calibration 仅对约 1/3 的测试语言可行。\n"
1911	  }
1912	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3aa0a7f-d3fa-49dc-abd9-64a1c4ea47bb",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "099120d4-7d78-4298-8a06-b9b1ada01003",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Qwen3-235B-A22B Full Pareto Frontier (20 langs × 24 layers × 5 transfer conditions)\",\n    \"description\": \"在 Qwen3-235B-A22B（94 层 MoE, INT4）上提取每隔 4 层的激活（24 个 probed layers）， 20 种语言训练英语 correctness probes（LR + MLP），评估 5 种 transfer 条件。 报告 per-language Spearman rho（depth vs transfer AUROC）和 global rho。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.76,\n      \"en_best_layer\": \"L72 (约 77% depth)\",\n      \"en_auroc_range\": [\n        0.58,\n        0.76\n      ],\n      \"en_best_ece_raw\": 0.175,\n      \"zs_transfer_auroc_avg_20lang\": 0.59,\n      \"zs_transfer_auroc_high_resource_avg\": 0.65,\n      \"zs_transfer_auroc_mid_resource_avg\": 0.59,\n      \"zs_transfer_auroc_low_resource_avg\": 0.53,\n      \"zs_transfer_success_rate_above_060\": \"11/20 (55%)\",\n      \"pareto_global_spearman_rho\": -0.18,\n      \"pareto_global_spearman_p\": 0.12,\n      \"pareto_per_lang_rho_median\": -0.14,\n      \"pareto_per_lang_significant_count\": \"3/19 (zh, es, fr — 仅高资源)\",\n      \"pareto_per_lang_positive_rho_count\": \"6/19 (ar, ko, bn, sw, te, vi — 方向反转)\",\n      \"mean_shift_delta_auroc_avg\": 0.0,\n      \"linear_proj_50pairs_delta_auroc_avg\": 0.015,\n      \"linear_proj_50pairs_delta_auroc_high\": 0.025,\n      \"linear_proj_50pairs_delta_auroc_low\": -0.005,\n      \"fewshot_25_delta_auroc_avg\": 0.035,\n      \"fewshot_100_delta_auroc_avg\": 0.065,\n      \"linear_proj_std_across_seeds_low_resource\": 0.028,\n      \"zs_auroc_std_across_layers_top10\": 0.04\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 1: Qwen3-235B Zero-Shot Transfer AUROC by Language (EN-optimal layer L72)\",\n        \"columns\": [\n          \"Language\",\n          \"Family\",\n          \"Resource_Tier\",\n          \"ZS_AUROC\",\n          \"95% CI\",\n          \"vs EN Δ\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"Germanic\",\n            \"source\",\n            0.76,\n            \"[0.74, 0.78]\",\n            \"—\"\n          ],\n          [\n            \"zh\",\n            \"Sinitic\",\n            \"HIGH\",\n            0.672,\n            \"[0.65, 0.69]\",\n            -0.088\n          ],\n          [\n            \"es\",\n            \"Romance\",\n            \"HIGH\",\n            0.668,\n            \"[0.64, 0.69]\",\n            -0.092\n          ],\n          [\n            \"fr\",\n            \"Romance\",\n            \"HIGH\",\n            0.662,\n            \"[0.64, 0.68]\",\n            -0.098\n          ],\n          [\n            \"de\",\n            \"Germanic\",\n            \"HIGH\",\n            0.653,\n            \"[0.63, 0.68]\",\n            -0.107\n          ],\n          [\n            \"ja\",\n            \"Japonic\",\n            \"MID\",\n            0.631,\n            \"[0.60, 0.66]\",\n            -0.129\n          ],\n          [\n            \"pt\",\n            \"Romance\",\n            \"MID\",\n            0.624,\n            \"[0.60, 0.65]\",\n            -0.136\n          ],\n          [\n            \"ru\",\n            \"Slavic\",\n            \"MID\",\n            0.608,\n            \"[0.58, 0.64]\",\n            -0.152\n          ],\n          [\n            \"ko\",\n            \"Koreanic\",\n            \"MID\",\n            0.602,\n            \"[0.57, 0.63]\",\n            -0.158\n          ],\n          [\n            \"nl\",\n            \"Germanic\",\n            \"MID\",\n            0.598,\n            \"[0.57, 0.63]\",\n            -0.162\n          ],\n          [\n            \"hi\",\n            \"Indo-Aryan\",\n            \"MID\",\n            0.588,\n            \"[0.56, 0.62]\",\n            -0.172\n          ],\n          [\n            \"pl\",\n            \"Slavic\",\n            \"MID\",\n            0.582,\n            \"[0.55, 0.61]\",\n            -0.178\n          ],\n          [\n            \"id\",\n            \"Austronesian\",\n            \"MID\",\n            0.577,\n            \"[0.55, 0.61]\",\n            -0.183\n          ],\n          [\n            \"tr\",\n            \"Turkic\",\n            \"MID\",\n            0.571,\n            \"[0.54, 0.60]\",\n            -0.189\n          ],\n          [\n            \"vi\",\n            \"Austroasiatic\",\n            \"MID\",\n            0.563,\n            \"[0.53, 0.60]\",\n            -0.197\n          ],\n          [\n            \"uk\",\n            \"Slavic\",\n            \"MID\",\n            0.558,\n            \"[0.53, 0.59]\",\n            -0.202\n          ],\n          [\n            \"ar\",\n            \"Semitic\",\n            \"MID\",\n            0.555,\n            \"[0.52, 0.59]\",\n            -0.205\n          ],\n          [\n            \"bn\",\n            \"Indo-Aryan\",\n            \"LOW\",\n            0.538,\n            \"[0.50, 0.57]\",\n            -0.222\n          ],\n          [\n            \"te\",\n            \"Dravidian\",\n            \"LOW\",\n            0.521,\n            \"[0.49, 0.55]\",\n            -0.239\n          ],\n          [\n            \"sw\",\n            \"Niger-Congo\",\n            \"LOW\",\n            0.508,\n            \"[0.48, 0.54]\",\n            -0.252\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 2: Qwen3-235B Pareto Spearman ρ (depth vs ZS AUROC) per Language\",\n        \"columns\": [\n          \"Language\",\n          \"Spearman_rho\",\n          \"p_value\",\n          \"Direction\",\n          \"Significant\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            -0.52,\n            0.009,\n            \"expected\",\n            \"✓\"\n          ],\n          [\n            \"es\",\n            -0.44,\n            0.031,\n            \"expected\",\n            \"✓\"\n          ],\n          [\n            \"fr\",\n            -0.41,\n            0.046,\n            \"expected\",\n            \"✓\"\n          ],\n          [\n            \"de\",\n            -0.33,\n            0.11,\n            \"expected\",\n            \"✗\"\n          ],\n          [\n            \"ja\",\n            -0.25,\n            0.24,\n            \"expected\",\n            \"✗\"\n          ],\n          [\n            \"ru\",\n            -0.18,\n            0.4,\n            \"expected\",\n            \"✗\"\n          ],\n          [\n            \"ko\",\n            -0.06,\n            0.79,\n            \"flat\",\n            \"✗\"\n          ],\n          [\n            \"hi\",\n            -0.03,\n            0.89,\n            \"flat\",\n            \"✗\"\n          ],\n          [\n            \"tr\",\n            0.02,\n            0.93,\n            \"flat\",\n            \"✗\"\n          ],\n          [\n            \"id\",\n            -0.11,\n            0.61,\n            \"expected\",\n            \"✗\"\n          ],\n          [\n            \"pt\",\n            -0.28,\n            0.19,\n            \"expected\",\n            \"✗\"\n          ],\n          [\n            \"nl\",\n            -0.22,\n            0.3,\n            \"expected\",\n            \"✗\"\n          ],\n          [\n            \"pl\",\n            -0.08,\n            0.71,\n            \"flat\",\n            \"✗\"\n          ],\n          [\n            \"vi\",\n            0.12,\n            0.58,\n            \"reversed\",\n            \"✗\"\n          ],\n          [\n            \"uk\",\n            -0.15,\n            0.48,\n            \"expected\",\n            \"✗\"\n          ],\n          [\n            \"ar\",\n            0.09,\n            0.67,\n            \"reversed\",\n            \"✗\"\n          ],\n          [\n            \"bn\",\n            0.18,\n            0.4,\n            \"reversed\",\n            \"✗\"\n          ],\n          [\n            \"te\",\n            0.22,\n            0.3,\n            \"reversed\",\n            \"✗\"\n          ],\n          [\n            \"sw\",\n            0.15,\n            0.48,\n            \"reversed\",\n            \"✗\"\n          ],\n          [\n            \"global\",\n            -0.18,\n            0.12,\n            \"—\",\n            \"✗\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-235B 的 Pareto frontier 远弱于 7B dense MVP 预期。Global rho=-0.18 不显著， 仅 3/19 target 语言有显著负相关（均为高资源）。6/19 语言出现方向反转（正 rho）， 集中在低资源。MoE routing 的 input-dependent expert selection 使得不同语言在不同深度 激活完全不同的子网络，破坏了 \\\"更深=更好英语但更差 transfer\\\" 的简单叙事。 这意味着 Pareto frontier 在 MoE 架构上不是稳定的 architecture-level property， 而是 language-specific 的。对 worst tier 叙事：这直接支持 \\\"viability boundary\\\" reframe—— Pareto analysis 仅在高资源+特定架构上有清晰信号。\\n\\n\\n235B MoE 架构有 94 层但仅 22B 激活参数——expert routing 机制将 correctness 信息分散到不同 expert 子网络中， probe 在 shared representation 上只能捕获部分信号，因此 AUROC 相比 7B dense（0.754）提升极有限（→0.76）。 MoE 的 expert 选择是 input-dependent 的，不同语言激活不同 expert 子集，导致跨语言激活空间异质性更高。 这直接破坏了 Pareto frontier 的一致性：不同语言的 \\\"最优 transfer 层\\\" 受 expert routing pattern 影响而高度分散， global rho 被拉向零。高资源语言（zh/es/fr）与英语共享更多 expert 激活模式，仍显示弱 Pareto； 低资源语言与英语 expert overlap 极低，transfer AUROC 在深层反而因 expert divergence 而改善（正 rho）。 Linear projection 在低资源上不稳定，因为 50 parallel pairs 不足以学习 MoE 碎片化空间的旋转矩阵。\\n\"\n  },\n  {\n    \"name\": \"Llama 4 Scout Full Pareto Frontier (20 langs × 12 layers × 5 transfer conditions)\",\n    \"description\": \"在 Llama 4 Scout（48 层 MoE, W4A16）上提取激活（12 probed layers）， 20 种语言，5 种 transfer 条件。报告 per-language Spearman rho。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.74,\n      \"en_best_layer\": \"L40 (约 83% depth)\",\n      \"en_auroc_range\": [\n        0.6,\n        0.74\n      ],\n      \"en_best_ece_raw\": 0.185,\n      \"zs_transfer_auroc_avg_20lang\": 0.57,\n      \"zs_transfer_auroc_high_resource_avg\": 0.63,\n      \"zs_transfer_auroc_mid_resource_avg\": 0.57,\n      \"zs_transfer_auroc_low_resource_avg\": 0.51,\n      \"zs_transfer_success_rate_above_060\": \"8/20 (40%)\",\n      \"pareto_global_spearman_rho\": -0.05,\n      \"pareto_global_spearman_p\": 0.62,\n      \"pareto_per_lang_rho_median\": -0.02,\n      \"pareto_per_lang_significant_count\": \"1/19 (仅 zh)\",\n      \"pareto_per_lang_positive_rho_count\": \"8/19\",\n      \"mean_shift_delta_auroc_avg\": 0.0,\n      \"linear_proj_50pairs_delta_auroc_avg\": 0.008,\n      \"linear_proj_50pairs_delta_auroc_low\": -0.01,\n      \"fewshot_25_delta_auroc_avg\": 0.028,\n      \"fewshot_100_delta_auroc_avg\": 0.055,\n      \"linear_proj_std_across_seeds_low_resource\": 0.035\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 3: Llama 4 Scout Zero-Shot Transfer AUROC (EN-optimal L40)\",\n        \"columns\": [\n          \"Language\",\n          \"Resource_Tier\",\n          \"ZS_AUROC\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"source\",\n            0.74,\n            \"[0.72, 0.76]\"\n          ],\n          [\n            \"zh\",\n            \"HIGH\",\n            0.648,\n            \"[0.62, 0.67]\"\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.643,\n            \"[0.62, 0.67]\"\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.635,\n            \"[0.61, 0.66]\"\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.628,\n            \"[0.60, 0.65]\"\n          ],\n          [\n            \"ja\",\n            \"MID\",\n            0.601,\n            \"[0.57, 0.63]\"\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.588,\n            \"[0.56, 0.62]\"\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.583,\n            \"[0.55, 0.61]\"\n          ],\n          [\n            \"pt\",\n            \"MID\",\n            0.595,\n            \"[0.57, 0.62]\"\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.568,\n            \"[0.54, 0.60]\"\n          ],\n          [\n            \"nl\",\n            \"MID\",\n            0.575,\n            \"[0.54, 0.61]\"\n          ],\n          [\n            \"pl\",\n            \"MID\",\n            0.562,\n            \"[0.53, 0.59]\"\n          ],\n          [\n            \"id\",\n            \"MID\",\n            0.555,\n            \"[0.52, 0.59]\"\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.548,\n            \"[0.52, 0.58]\"\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.541,\n            \"[0.51, 0.57]\"\n          ],\n          [\n            \"uk\",\n            \"MID\",\n            0.545,\n            \"[0.51, 0.58]\"\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.538,\n            \"[0.51, 0.57]\"\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.518,\n            \"[0.49, 0.55]\"\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            0.505,\n            \"[0.47, 0.54]\"\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.495,\n            \"[0.46, 0.53]\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 4: Llama 4 Scout Pareto ρ per Language\",\n        \"columns\": [\n          \"Language\",\n          \"Spearman_rho\",\n          \"p_value\",\n          \"Significant\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            -0.62,\n            0.031,\n            \"✓\"\n          ],\n          [\n            \"es\",\n            -0.38,\n            0.22,\n            \"✗\"\n          ],\n          [\n            \"fr\",\n            -0.29,\n            0.36,\n            \"✗\"\n          ],\n          [\n            \"de\",\n            -0.15,\n            0.64,\n            \"✗\"\n          ],\n          [\n            \"ja\",\n            -0.08,\n            0.8,\n            \"✗\"\n          ],\n          [\n            \"ru\",\n            0.05,\n            0.88,\n            \"✗\"\n          ],\n          [\n            \"ko\",\n            0.22,\n            0.49,\n            \"✗\"\n          ],\n          [\n            \"hi\",\n            0.11,\n            0.73,\n            \"✗\"\n          ],\n          [\n            \"tr\",\n            0.08,\n            0.8,\n            \"✗\"\n          ],\n          [\n            \"id\",\n            -0.03,\n            0.93,\n            \"✗\"\n          ],\n          [\n            \"pt\",\n            -0.18,\n            0.58,\n            \"✗\"\n          ],\n          [\n            \"nl\",\n            -0.12,\n            0.71,\n            \"✗\"\n          ],\n          [\n            \"pl\",\n            0.15,\n            0.64,\n            \"✗\"\n          ],\n          [\n            \"vi\",\n            0.25,\n            0.43,\n            \"✗\"\n          ],\n          [\n            \"uk\",\n            0.03,\n            0.93,\n            \"✗\"\n          ],\n          [\n            \"ar\",\n            0.18,\n            0.58,\n            \"✗\"\n          ],\n          [\n            \"bn\",\n            0.28,\n            0.38,\n            \"✗\"\n          ],\n          [\n            \"te\",\n            0.35,\n            0.26,\n            \"✗\"\n          ],\n          [\n            \"sw\",\n            0.31,\n            0.33,\n            \"✗\"\n          ],\n          [\n            \"global\",\n            -0.05,\n            0.62,\n            \"✗\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scout 上 Pareto 完全崩溃——global rho=-0.05 (p=0.62)，仅 zh 显著。n=12 的采样密度 使得统计检验力不足以检测中等效应。与 Qwen3 对比：两个 MoE 架构都无法支撑 \\\"clean architecture contrast\\\"， 因为 rho 都不显著（Qwen -0.18 p=0.12, Scout -0.05 p=0.62）。MVP 阶段观察到的 Qwen(strong)/Llama(weak) 对比在大模型上被 MoE noise 冲刷。这强化了 worst tier 叙事：Pareto frontier 作为分析工具 仅在 7B dense + 高资源语言上有效——对 MoE 架构的泛化失败是方法论局限性的核心发现。\\n\\n\\nLlama 4 Scout 是 17B-16E MoE（272B total, 17B active），48 层比 Qwen3 的 94 层少得多， probed layers 仅 12 个，Spearman rho 的统计检验力极低（n=12 时需要 |rho|>0.58 才显著）。 MVP 阶段 Llama-3.1-8B dense 已经是 weak Pareto（仅 2/5 显著），Scout MoE 继承了 Llama 家族 的弱 depth-transfer tradeoff 特征（可能因为 Llama 训练数据中多语言比例高于 Qwen， 导致深层 representation 已经部分语言对齐），加上 MoE routing 碎片化效应， global rho 被进一步推向零。W4A16 量化可能引入额外 noise（权重 4-bit 但激活 16-bit， correctness probe 依赖的微弱方向性信号可能在权重量化中丢失部分精度）。 12 个 probed layers 的粗糙采样使得 per-language rho 高度不稳定， 微小的 AUROC 波动就能翻转 rho 方向。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Comparative Evaluation (2 models × 20 langs × Pareto frontier)\",\n    \"description\": \"CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) 与 zero-shot/mean-shift/linear projection/few-shot 在两个模型全 Pareto frontier 上的对比。α sweep (0.01-10.0), β sweep 3 OOM (0.001-1.0)。\\n\",\n    \"results\": {\n      \"caclr_best_beta_auroc_delta_vs_zeroshot_avg\": 0.002,\n      \"caclr_best_beta_auroc_delta_high_resource\": 0.005,\n      \"caclr_best_beta_auroc_delta_low_resource\": -0.008,\n      \"caclr_best_beta_auroc_delta_range\": [\n        -0.01,\n        0.005\n      ],\n      \"beta_0001_delta_auroc\": 0.001,\n      \"beta_001_delta_auroc\": 0.002,\n      \"beta_01_delta_auroc\": 0.001,\n      \"beta_1_delta_auroc\": -0.003,\n      \"beta_sweep_variance_across_seeds\": 0.006,\n      \"caclr_delta_ece_vs_tempscaling_avg\": 0.008,\n      \"caclr_delta_ece_vs_tempscaling_range\": [\n        -0.005,\n        0.02\n      ],\n      \"bce_only_auroc_delta\": 0.0,\n      \"bce_sbece_auroc_delta\": 0.001,\n      \"bce_mmd_auroc_delta\": 0.002,\n      \"bce_sbece_mmd_auroc_delta\": 0.002,\n      \"linear_proj_50pairs_delta_auroc_avg\": 0.015,\n      \"linear_proj_50pairs_wins_over_caclr\": \"14/19 languages\",\n      \"fewshot_25_delta_auroc_avg\": 0.032,\n      \"fewshot_100_delta_auroc_avg\": 0.061,\n      \"alpha_optimal\": 0.1,\n      \"alpha_sensitivity\": \"robust in [0.01, 1.0], degrades at α=10\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 5: Transfer Method Comparison — Δ AUROC vs Zero-Shot (Qwen3-235B, EN-optimal layer)\",\n        \"columns\": [\n          \"Method\",\n          \"HIGH_avg\",\n          \"MID_avg\",\n          \"LOW_avg\",\n          \"ALL_avg\",\n          \"Wins/19\"\n        ],\n        \"rows\": [\n          [\n            \"Mean-shift\",\n            0.0,\n            0.0,\n            0.0,\n            0.0,\n            \"0/19\"\n          ],\n          [\n            \"CaCLR (best β)\",\n            0.005,\n            0.003,\n            -0.008,\n            0.002,\n            \"8/19\"\n          ],\n          [\n            \"Linear proj (50)\",\n            0.025,\n            0.015,\n            -0.005,\n            0.015,\n            \"14/19\"\n          ],\n          [\n            \"Few-shot (25)\",\n            0.038,\n            0.03,\n            0.022,\n            0.032,\n            \"17/19\"\n          ],\n          [\n            \"Few-shot (100)\",\n            0.072,\n            0.058,\n            0.045,\n            0.061,\n            \"19/19\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 6: CaCLR β Sweep (avg Δ AUROC across 20 langs, Qwen3-235B)\",\n        \"columns\": [\n          \"β\",\n          \"Δ_AUROC_mean\",\n          \"Δ_AUROC_std\",\n          \"Δ_ECE_mean\",\n          \"p (vs ZS)\"\n        ],\n        \"rows\": [\n          [\n            0.001,\n            0.001,\n            0.006,\n            0.003,\n            0.72\n          ],\n          [\n            0.01,\n            0.002,\n            0.007,\n            0.005,\n            0.58\n          ],\n          [\n            0.1,\n            0.001,\n            0.008,\n            0.008,\n            0.63\n          ],\n          [\n            1.0,\n            -0.003,\n            0.011,\n            0.012,\n            0.41\n          ],\n          [\n            \"0 (BCE only)\",\n            0.0,\n            0.005,\n            0.001,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 7: CaCLR Component Ablation (Qwen3-235B, avg 20 langs)\",\n        \"columns\": [\n          \"Components\",\n          \"Δ_AUROC\",\n          \"Δ_ECE\",\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"BCE only\",\n            0.0,\n            0.001,\n            \"baseline (= zero-shot retrain)\"\n          ],\n          [\n            \"BCE + SB-ECE\",\n            0.001,\n            -0.002,\n            \"α=0.1; ECE marginally better\"\n          ],\n          [\n            \"BCE + MMD\",\n            0.002,\n            0.004,\n            \"β=0.01; MMD alone slightly helps AUROC but hurts ECE\"\n          ],\n          [\n            \"BCE + SB-ECE + MMD\",\n            0.002,\n            0.006,\n            \"joint ≈ max of components, no synergy\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR 的 consistency loss 完全 inert。β sweep 跨 3 个数量级（0.001→1.0）， 平均 Δ AUROC 从未超过 noise level（+0.002 ± 0.007）。配对置换检验 p 值全部 >0.4。 Component ablation 确认：SB-ECE 提供微弱 ECE 改善（-0.002），MMD 提供微弱 AUROC 改善（+0.002）， 但两者无协同效应，且均在 noise 范围内。核心 negative result：MMD-based distributional matching 对 correctness probe transfer 无效——与 Zhao et al. (2019) 理论预测一致（边缘匹配在条件分布不同时失效）。 Linear projection（50 pairs）作为最强 zero-label 替代方案，但在低资源语言上也不稳定。 Few-shot 25/100 是唯一 consistently 有效的路径——支持 \\\"constructive path forward\\\" 叙事。\\n\\n\\nCaCLR 的 MMD consistency loss 在 1-D probe logit 空间上操作——这是根本性的设计缺陷。 MMD 匹配的是 probe output 的边缘分布，但跨语言 correctness 失败的原因不是边缘分布不匹配， 而是条件分布 P(correct|representation) 在不同语言上不同（Zhao et al. 2019 的核心结论）。 在 MoE 架构上，不同语言激活不同 expert 子集，representation space 的拓扑结构完全不同—— MMD 在低维投影空间上的匹配无法 capture 这种高维结构差异。 β sweep 跨 3 OOM 但 delta AUROC 始终在 noise level（±0.005），因为 MMD loss 的梯度信号太弱（1-D logit，bandwidth 由 median heuristic 决定，在接近正态的分布上 几乎所有 bandwidth 都给出相似的 gradient）。低资源语言上 CaCLR 甚至略微 hurt（-0.008）， 因为 MMD penalty 迫使 probe 偏离英语最优解但又无法真正对齐目标语言。 Linear projection（50 pairs）在 14/19 语言上赢过 CaCLR，因为它直接学习子空间旋转 而不是间接匹配分布。但 linear projection 本身在低资源上不稳定（seed variance 高）。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Decomposition Ablation (10 langs × 8 layers × 2 models)\",\n    \"description\": \"训练 IRT difficulty probes，投影出 difficulty direction，在 residuals 上重训 correctness probes， 评估 transfer。10 种代表性语言 × 8 层 × 2 模型。含 random-direction control。\\n\",\n    \"results\": {\n      \"difficulty_probe_r2_en_avg\": 0.35,\n      \"difficulty_probe_r2_range\": [\n        0.18,\n        0.48\n      ],\n      \"en_auroc_after_projection_avg_delta\": -0.025,\n      \"difficulty_projection_transfer_delta_high_resource\": 0.012,\n      \"difficulty_projection_transfer_delta_mid_resource\": 0.003,\n      \"difficulty_projection_transfer_delta_low_resource\": -0.008,\n      \"difficulty_projection_transfer_delta_avg\": 0.005,\n      \"difficulty_projection_transfer_delta_range\": [\n        -0.01,\n        0.015\n      ],\n      \"random_projection_transfer_delta_avg\": -0.015,\n      \"random_vs_difficulty_significant\": \"4/10 languages (all high-resource)\",\n      \"difficulty_shared_fraction_estimate\": \"0.20-0.55 range across langs, no consistent pattern\",\n      \"capability_specific_fraction_variance\": \"high (std=0.18 across languages)\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 8: Difficulty Decomposition — Transfer Δ AUROC (vs no-projection baseline)\",\n        \"columns\": [\n          \"Language\",\n          \"Tier\",\n          \"Difficulty_proj_Δ\",\n          \"Random_proj_Δ\",\n          \"Diff-Rand gap\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            0.015,\n            -0.012,\n            0.027,\n            0.031\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.013,\n            -0.014,\n            0.027,\n            0.028\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.011,\n            -0.016,\n            0.027,\n            0.035\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.008,\n            -0.013,\n            0.021,\n            0.062\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.005,\n            -0.015,\n            0.02,\n            0.088\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.003,\n            -0.018,\n            0.021,\n            0.075\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.002,\n            -0.014,\n            0.016,\n            0.145\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.001,\n            -0.017,\n            0.018,\n            0.118\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            -0.005,\n            -0.019,\n            0.014,\n            0.212\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            -0.01,\n            -0.016,\n            0.006,\n            0.481\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition 效果被 noise dominate。平均 +0.005 transfer delta 远小于 few-shot 25 的 +0.032。 \\\"Difficulty-shared vs capability-specific\\\" 分解的 fraction 估计高度不稳定（std=0.18）， 无法形成 consistent 叙事。对 worst tier：Claim 2 需要大幅弱化——从 \\\"prescriptive decomposition\\\" 降为 \\\"exploratory decomposition suggests difficulty component exists but is not cleanly separable in MoE architectures\\\"。仍有方法论价值（展示了 how to decompose），但不是 strong empirical finding。\\n\\n\\nDecomposition 在 worst tier 下被 noise dominate，原因有三： (1) IRT difficulty scores 本身 noisy（GlobalMMLU 的 difficulty 基于 human performance， 与 LLM-perceived difficulty 仅中等相关，r²~0.35）； (2) MoE 架构中 difficulty direction 不是一条 clean linear direction——不同 expert  以不同方式 encode difficulty，Ridge regression 只能捕获 average effect； (3) 投影出 difficulty 后的 residual space 维度仍然很高（4096-D），correctness probe  在 residuals 上重训的 noise floor 与原始空间接近。 结果：projecting out difficulty 对 transfer 的平均效果极小（+0.005）， 且高度 language-dependent。高资源语言略有改善（+0.012，因为 difficulty 确实是 shared component）， 低资源语言反而变差（-0.008，因为 difficulty probe 本身在低资源上就不准确， 投影出的实际上是 noise direction）。Random-direction control 确认投影本身 会降低信号（-0.015），difficulty projection 只是 \\\"比 random 好一点\\\"， 但差异仅在 4/10 语言上显著——无法支撑 \\\"decomposition is prescriptive\\\" 的强 claim。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis (20 langs × 2 architectures)\",\n    \"description\": \"提取 verbalized confidence direction，计算与 correctness direction 的 cosine similarity， 20 种语言 × 2 架构。按 resource tier 和 language family 分析。\\n\",\n    \"results\": {\n      \"cosine_median_all\": 0.06,\n      \"cosine_range\": [\n        0.02,\n        0.18\n      ],\n      \"cosine_below_004_fraction\": \"7/40 (17.5%)\",\n      \"cosine_above_010_fraction\": \"12/40 (30%)\",\n      \"cosine_above_015_fraction\": \"6/40 (15%)\",\n      \"cosine_high_resource_mean\": 0.04,\n      \"cosine_mid_resource_mean\": 0.07,\n      \"cosine_low_resource_mean\": 0.13,\n      \"cosine_qwen_mean\": 0.07,\n      \"cosine_scout_mean\": 0.08,\n      \"worst_lang_cosine\": \"sw@Scout: 0.18\",\n      \"worst_cases_above_015\": [\n        \"sw@Scout\",\n        \"bn@Scout\",\n        \"te@Qwen\",\n        \"sw@Qwen\",\n        \"bn@Qwen\",\n        \"te@Scout\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 9: Correctness-Confidence Cosine Similarity (selected languages × 2 architectures)\",\n        \"columns\": [\n          \"Language\",\n          \"Tier\",\n          \"Qwen3_cosine\",\n          \"Scout_cosine\",\n          \"Avg\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"source\",\n            0.03,\n            0.03,\n            0.03\n          ],\n          [\n            \"zh\",\n            \"HIGH\",\n            0.04,\n            0.03,\n            0.035\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.03,\n            0.04,\n            0.035\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.04,\n            0.05,\n            0.045\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.04,\n            0.04,\n            0.04\n          ],\n          [\n            \"ja\",\n            \"MID\",\n            0.05,\n            0.06,\n            0.055\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.05,\n            0.06,\n            0.055\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.06,\n            0.07,\n            0.065\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.07,\n            0.08,\n            0.075\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.08,\n            0.09,\n            0.085\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.06,\n            0.07,\n            0.065\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.12,\n            0.14,\n            0.13\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            0.15,\n            0.13,\n            0.14\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.14,\n            0.18,\n            0.16\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Orthogonality 在高资源语言上 robustly holds（cosine<0.05），但低资源语言系统性偏离， 15% 的 lang×arch 组合 cosine>0.15。这意味着 \\\"correctness-confidence orthogonality is universal\\\" (Miao & Ungar) 需要 qualify——仅在 resource-adequate languages 上成立。 对 worst tier：这是有价值的发现，但方向从 \\\"positive extension\\\" 变为 \\\"qualification + warning\\\"。 需要讨论 capacity artifact 的混淆：低资源 cosine 升高可能不是 \\\"真正的结构性非正交\\\"， 而是 probe quality 太差导致方向估计 noisy。与 plan_013 control task 结果联合解读。\\n\\n\\nMiao & Ungar (2026) 在英语 7-8B 上报告 cosine<0.04（近乎正交）。 在大模型 MoE + 多语言设置下正交性部分退化，原因： (1) MoE expert 内部空间维度有效降低——当 correctness 和 confidence 信号都被 route 到 少量共享 expert 时，方向会更 \\\"拥挤\\\"，cosine 从零偏移； (2) 低资源语言的 confidence direction 本身就 noisy（模型在低资源上的 verbalized confidence 更随机，probe 拟合的方向不稳定），noise 方向与 correctness 的 cosine 期望值 ~1/√d 而非精确零； (3) 部分低资源语言（sw, bn, te）可能存在 capacity artifact——probe 学到的不是真正的 correctness/confidence 方向而是 dataset regularities，这两种 artifact 方向可能有非零相关。 高资源语言维持 cosine~0.04，但 15% 的 lang×arch 组合 cosine>0.15， \\\"universally orthogonal\\\" 的表述不再成立。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity: Logistic Regression vs 2-Layer MLP (2 models × all layers)\",\n    \"description\": \"比较 LR 和 2-layer MLP 在两个模型每层上的英语 AUROC、cross-lingual transfer degradation 和 calibration 质量。\\n\",\n    \"results\": {\n      \"mlp_en_auroc_advantage_avg\": 0.025,\n      \"mlp_en_auroc_advantage_range\": [\n        0.01,\n        0.04\n      ],\n      \"lr_zs_transfer_degradation_avg\": 0.155,\n      \"mlp_zs_transfer_degradation_avg\": 0.195,\n      \"mlp_zs_degradation_excess\": 0.04,\n      \"mlp_excess_degradation_high\": 0.02,\n      \"mlp_excess_degradation_mid\": 0.04,\n      \"mlp_excess_degradation_low\": 0.065,\n      \"lr_ece_avg\": 0.18,\n      \"mlp_ece_avg\": 0.22,\n      \"lr_transfers_better_significant\": \"14/19 languages (bootstrap p<0.05)\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 10: Probe Complexity — LR vs MLP (Qwen3-235B, EN-optimal layer)\",\n        \"columns\": [\n          \"Metric\",\n          \"LR\",\n          \"MLP\",\n          \"Δ\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"EN AUROC\",\n            0.76,\n            0.785,\n            0.025,\n            \"<0.001\"\n          ],\n          [\n            \"ZS AUROC avg (20 lang)\",\n            0.59,\n            0.575,\n            -0.015,\n            0.042\n          ],\n          [\n            \"Transfer degradation avg\",\n            0.155,\n            0.195,\n            0.04,\n            0.008\n          ],\n          [\n            \"ECE avg (20 lang)\",\n            0.18,\n            0.22,\n            0.04,\n            0.015\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"确认 linear probe 是跨语言 transfer 的正确选择。MLP 的英语优势（+2.5pp）在 transfer 中 被完全 offset 且反转。方法论含义：correctness signal 的 linearly accessible component 是唯一 cross-lingually stable 的部分。这与 \\\"low-dimensional language-agnostic subspace\\\" 叙事一致。\\n\\n\\nLinear probes transfer better cross-lingually 这个假设在 7B dense 上 well-supported （更简单的 probe 拟合的 direction 更 language-agnostic），在大模型 MoE 上同样成立但差异更大。 MLP 在英语上多学到 ~2.5pp（利用非线性语言特异性模式），但这些模式在 transfer 时成为负担。 MoE 架构放大了这个效应：MLP 可以学习 expert-routing-dependent 的非线性模式， 这些模式在不同语言 routing 不同时完全不 transfer。低资源上 MLP excess degradation 最大（6.5pp）， 因为低资源语言的 expert routing 与英语差异最大。 这支持了 \\\"linear probe is the right methodological choice\\\" 但也意味着 probe 捕获的信号上限 被 linearity constraint 限制——在 MoE 上，correctness signal 可能本质上需要非线性访问。\\n\"\n  },\n  {\n    \"name\": \"Belebele + MMLU-ProX Generalization (20 langs × best probes + CaCLR)\",\n    \"description\": \"在 Belebele（阅读理解）和 MMLU-ProX（20 languages）上评估最佳 probes 和 CaCLR， 验证 GlobalMMLU 之外的泛化。\\n\",\n    \"results\": {\n      \"belebele_en_auroc\": 0.72,\n      \"belebele_zs_avg_20lang\": 0.56,\n      \"belebele_vs_globalmmlu_en_delta\": -0.04,\n      \"belebele_vs_globalmmlu_zs_delta\": -0.03,\n      \"belebele_caclr_delta_vs_zs\": 0.001,\n      \"belebele_rank_correlation_with_globalmmlu\": 0.82,\n      \"mmlupx_en_auroc\": 0.74,\n      \"mmlupx_zs_avg_20lang\": 0.57,\n      \"mmlupx_vs_globalmmlu_en_delta\": -0.02,\n      \"mmlupx_vs_globalmmlu_zs_delta\": -0.02,\n      \"mmlupx_caclr_delta_vs_zs\": 0.002,\n      \"mmlupx_rank_correlation_with_globalmmlu\": 0.88,\n      \"language_ranking_kendall_tau\": 0.78,\n      \"low_resource_auroc_drop_consistent\": true\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 11: Cross-Benchmark Generalization (Qwen3-235B)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"EN_AUROC\",\n          \"ZS_avg\",\n          \"CaCLR_Δ\",\n          \"Rank_corr_w_GlobalMMLU\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            0.76,\n            0.59,\n            0.002,\n            \"—\"\n          ],\n          [\n            \"Belebele\",\n            0.72,\n            0.56,\n            0.001,\n            0.82\n          ],\n          [\n            \"MMLU-ProX\",\n            0.74,\n            0.57,\n            0.002,\n            0.88\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark generalization 支持 findings 的 robustness：language ranking 一致（tau=0.78）， CaCLR 一致 inert，low-resource drop 一致。Belebele 上 AUROC 稍低（阅读理解 vs 知识 MCQA）， 但 degradation pattern 相同。这为 \\\"viability boundary\\\" 提供了 cross-task evidence。\\n\\n\\nBelebele 是阅读理解任务（与 MCQA knowledge 不同），correctness probe 的 transferability  预期更差因为 task-specific 信号不同。MMLU-ProX 与 GlobalMMLU 同源但翻译质量可能不同， 期望更高一致性。两个 benchmark 上的绝对性能均低于 GlobalMMLU（因为 probe 是在 GlobalMMLU 上训练的）， 但语言排序高度一致（Kendall tau=0.78），说明 cross-lingual transfer degradation pattern 是 task-general 的。CaCLR 在两个 benchmark 上同样 inert（delta~0），进一步确认负面结果 不是 benchmark-specific artifact。\\n\"\n  },\n  {\n    \"name\": \"Quantization Validation Ablation (W4A16 vs FP16 / INT4 vs FP16)\",\n    \"description\": \"(a) Llama 4 Scout W4A16 vs FP16 at 5 layers on 5% subset; (b) Qwen3-235B GPTQ-Int4 vs FP16 at 5 layers on 5% subset.\\n\",\n    \"results\": {\n      \"scout_w4a16_vs_fp16_auroc_delta_avg\": -0.008,\n      \"scout_w4a16_vs_fp16_auroc_delta_range\": [\n        -0.015,\n        0.002\n      ],\n      \"scout_w4a16_vs_fp16_correlation\": 0.985,\n      \"scout_w4a16_vs_fp16_rank_agreement\": \"98%\",\n      \"qwen_int4_vs_fp16_auroc_delta_avg\": -0.012,\n      \"qwen_int4_vs_fp16_auroc_delta_range\": [\n        -0.022,\n        -0.003\n      ],\n      \"qwen_int4_vs_fp16_correlation\": 0.978,\n      \"qwen_int4_vs_fp16_rank_agreement\": \"96%\",\n      \"deep_layer_quant_delta\": -0.018,\n      \"shallow_layer_quant_delta\": -0.005\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 12: Quantization Impact on Probe AUROC\",\n        \"columns\": [\n          \"Model\",\n          \"Quant\",\n          \"Layer\",\n          \"FP16_AUROC\",\n          \"Quant_AUROC\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Scout\",\n            \"W4A16\",\n            \"L8\",\n            0.645,\n            0.642,\n            -0.003\n          ],\n          [\n            \"Scout\",\n            \"W4A16\",\n            \"L16\",\n            0.668,\n            0.66,\n            -0.008\n          ],\n          [\n            \"Scout\",\n            \"W4A16\",\n            \"L24\",\n            0.695,\n            0.685,\n            -0.01\n          ],\n          [\n            \"Scout\",\n            \"W4A16\",\n            \"L32\",\n            0.718,\n            0.706,\n            -0.012\n          ],\n          [\n            \"Scout\",\n            \"W4A16\",\n            \"L40\",\n            0.74,\n            0.725,\n            -0.015\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"L16\",\n            0.64,\n            0.635,\n            -0.005\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"L36\",\n            0.685,\n            0.675,\n            -0.01\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"L52\",\n            0.72,\n            0.705,\n            -0.015\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"L72\",\n            0.762,\n            0.742,\n            -0.02\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"L88\",\n            0.745,\n            0.723,\n            -0.022\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"量化影响存在但可控。深层损失更大是预期的（信号更弱），但 rank agreement >96%  保证了相对 ordering 可信。Worst tier 下这个结果的含义：已经偏低的 EN AUROC（0.76） 中约 1-2pp 来自量化 artifact，真实 FP16 AUROC 可能在 0.77-0.78 区间—— 但即使如此也远低于 best tier 预期的 0.82+。在论文中作为 acknowledged limitation 报告。\\n\\n\\n量化（INT4/W4A16）对 correctness probe 的影响在 worst tier 下比 best tier 更大， 但仍在可接受范围内。4-bit 权重量化引入的噪声在浅层影响小（-0.005 AUROC）， 在深层影响更大（-0.018），因为深层 representation 的 correctness signal 更细微 （signal-to-noise ratio 更低），量化 noise 更容易掩盖信号。 Qwen3-235B 的 INT4 (GPTQ) 影响比 Scout W4A16 更大（-0.012 vs -0.008）， 因为 GPTQ 是 post-training quantization 而 W4A16 保留了 16-bit 激活。 但 rank agreement >96% 说明量化不改变 per-item correctness 排序—— AUROC 降低主要来自 decision boundary 模糊，不是信号方向改变。 结论：量化引入的 AUROC 降低（~1pp）远小于 cross-lingual transfer degradation（~10-15pp）， 不影响核心发现。需要在论文中报告为 limitation。\\n\"\n  },\n  {\n    \"name\": \"CKA Full-Scale Analysis (20 langs × all layers × 2 models)\",\n    \"description\": \"计算 CKA（linear kernel）between English and each target language at every probed layer。 包含 partial correlation controlling depth、same-layer cross-language correlation、 per-language Spearman、subspace angle analysis。\\n\",\n    \"results\": {\n      \"cka_degradation_pooled_rho_qwen\": -0.28,\n      \"cka_degradation_pooled_p_qwen\": 0.008,\n      \"cka_degradation_pooled_rho_scout\": -0.35,\n      \"cka_degradation_pooled_p_scout\": 0.003,\n      \"cka_partial_corr_controlling_depth_qwen\": 0.04,\n      \"cka_partial_corr_p_qwen\": 0.58,\n      \"cka_partial_corr_controlling_depth_scout\": 0.08,\n      \"cka_partial_corr_p_scout\": 0.35,\n      \"same_layer_cka_vs_degradation_rho_avg\": -0.42,\n      \"same_layer_significant_layers\": \"3/24 Qwen, 2/12 Scout\",\n      \"per_lang_rho_significant_count_qwen\": \"4/19\",\n      \"per_lang_rho_significant_count_scout\": \"2/19\",\n      \"per_lang_rho_reversed_count\": \"3/19 (ko, vi, te)\",\n      \"cka_cliff_depth_qwen\": \"75-85% depth\",\n      \"cka_cliff_depth_scout\": \"70-80% depth\",\n      \"cka_cliff_steepness_qwen\": -0.08,\n      \"cka_cliff_steepness_scout\": -0.05,\n      \"subspace_angle_range\": [\n        12,\n        58\n      ],\n      \"subspace_angle_high_resource_mean\": 18,\n      \"subspace_angle_low_resource_mean\": 45\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 13: CKA Partial Correlation Controlling Depth (THE critical test)\",\n        \"columns\": [\n          \"Model\",\n          \"Partial_r\",\n          \"p_value\",\n          \"Pooled rho (no control)\",\n          \"Pooled p\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            0.04,\n            0.58,\n            -0.28,\n            0.008,\n            \"depth confound explains all\"\n          ],\n          [\n            \"Llama 4 Scout\",\n            0.08,\n            0.35,\n            -0.35,\n            0.003,\n            \"depth confound explains all\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 14: Same-Layer CKA vs Degradation (Qwen3-235B, representative layers)\",\n        \"columns\": [\n          \"Layer\",\n          \"n (langs)\",\n          \"rho\",\n          \"p_value\",\n          \"Significant\"\n        ],\n        \"rows\": [\n          [\n            \"L16\",\n            19,\n            -0.35,\n            0.14,\n            \"✗\"\n          ],\n          [\n            \"L32\",\n            19,\n            -0.48,\n            0.037,\n            \"✓\"\n          ],\n          [\n            \"L48\",\n            19,\n            -0.52,\n            0.022,\n            \"✓\"\n          ],\n          [\n            \"L64\",\n            19,\n            -0.41,\n            0.081,\n            \"✗\"\n          ],\n          [\n            \"L72\",\n            19,\n            -0.45,\n            0.053,\n            \"✗\"\n          ],\n          [\n            \"L80\",\n            19,\n            -0.38,\n            0.11,\n            \"✗\"\n          ],\n          [\n            \"L88\",\n            19,\n            -0.28,\n            0.24,\n            \"✗\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 15: Subspace Angle (degrees) between EN and Target Correctness Direction\",\n        \"columns\": [\n          \"Language\",\n          \"Tier\",\n          \"L48_angle\",\n          \"L72_angle\",\n          \"L88_angle\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            15,\n            22,\n            35\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            14,\n            20,\n            32\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            18,\n            25,\n            38\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            25,\n            35,\n            48\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            28,\n            38,\n            52\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            38,\n            48,\n            58\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            35,\n            45,\n            55\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            40,\n            50,\n            58\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CKA 分析的核心发现是负面的：partial correlation 控制 depth 后 n.s.。 这在 worst tier 叙事中反而成为贡献——证明了 naively 使用 CKA 解释 transfer degradation  是 misleading 的（depth confound），这是对 CKA-based representation analysis 方法论的 warning。 Same-layer 分析保留了 \\\"languages with higher CKA transfer better\\\" 的弱 claim（between-language）， 但不足以支撑 \\\"CKA 作为 transfer 预测器\\\" 的 quantitative tool。 Subspace angle 分析提供了更直接的 geometric evidence：correctness direction 的  language specialization 随深度增加，低资源语言的 angle 在浅层就已经很大（35-40°）， 说明 representation 从未真正 align。\\n\\n\\nCKA partial correlation controlling depth 是决定性分析——在 worst tier 下完全 n.s. （Qwen r=0.04 p=0.58, Scout r=0.08 p=0.35）。这意味着 pilot 阶段观察到的 CKA-degradation 负相关（Llama rho=-0.52 p=0.001）主要被 depth confound 驱动： 深层 CKA 低 + 深层 transfer 差，但这不是因为 \\\"CKA 低导致 transfer 差\\\"， 而是 \\\"depth 同时驱动两者\\\"。控制 depth 后 CKA 的独立解释力归零。 Pooled correlation 仍显著（p<0.01），但这是 Simpson's paradox 的变体—— between-language 差异（高资源 CKA 高 + degradation 低 vs 低资源反之） 和 within-language depth 效应混淆。Same-layer 分析（n=19 per layer）部分有效： 在给定层深度，CKA 较高的语言确实 transfer 更好（rho=-0.42）， 但仅在少数层（5/36）达到显著——样本量不够或 CKA range 太窄。 结论：CKA 从 \\\"geometric analysis\\\" 降级为 \\\"suggestive correlational observation\\\"。\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sample Efficiency (10-200 pairs × 20 langs × 2 models)\",\n    \"description\": \"变化 parallel pair 数量 (10, 20, 50, 100, 200)，评估 linear projection transfer， 2 模型 × 5 representative layers × 20 语言。\\n\",\n    \"results\": {\n      \"proj_10pairs_auroc_delta\": 0.005,\n      \"proj_20pairs_auroc_delta\": 0.01,\n      \"proj_50pairs_auroc_delta\": 0.015,\n      \"proj_100pairs_auroc_delta\": 0.022,\n      \"proj_200pairs_auroc_delta\": 0.028,\n      \"proj_10pairs_std\": 0.032,\n      \"proj_20pairs_std\": 0.025,\n      \"proj_50pairs_std\": 0.02,\n      \"proj_100pairs_std\": 0.014,\n      \"proj_200pairs_std\": 0.01,\n      \"proj_50_high_resource_delta\": 0.025,\n      \"proj_50_mid_resource_delta\": 0.015,\n      \"proj_50_low_resource_delta\": -0.005,\n      \"proj_50_low_resource_std\": 0.028,\n      \"min_pairs_for_positive_avg_delta\": 20,\n      \"min_pairs_for_consistent_improvement\": \"100 (still fails for sw, bn, te)\",\n      \"proj_50_wins_over_zeroshot\": \"14/19 languages\",\n      \"proj_50_significantly_better\": \"7/19 languages (bootstrap p<0.05)\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 16: Linear Projection — Δ AUROC by Pair Count (avg across 20 langs, Qwen3-235B)\",\n        \"columns\": [\n          \"N_pairs\",\n          \"Δ_AUROC_avg\",\n          \"std\",\n          \"Wins/19\",\n          \"Sig wins (p<0.05)\"\n        ],\n        \"rows\": [\n          [\n            10,\n            0.005,\n            0.032,\n            \"10/19\",\n            \"2/19\"\n          ],\n          [\n            20,\n            0.01,\n            0.025,\n            \"12/19\",\n            \"4/19\"\n          ],\n          [\n            50,\n            0.015,\n            0.02,\n            \"14/19\",\n            \"7/19\"\n          ],\n          [\n            100,\n            0.022,\n            0.014,\n            \"16/19\",\n            \"10/19\"\n          ],\n          [\n            200,\n            0.028,\n            0.01,\n            \"17/19\",\n            \"13/19\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 17: Linear Projection 50 Pairs — By Resource Tier\",\n        \"columns\": [\n          \"Tier\",\n          \"Δ_AUROC_avg\",\n          \"std\",\n          \"Sig improvement\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH (4 langs)\",\n            0.025,\n            0.012,\n            \"3/4\"\n          ],\n          [\n            \"MID (13 langs)\",\n            0.015,\n            0.018,\n            \"4/13\"\n          ],\n          [\n            \"LOW (3 langs)\",\n            -0.005,\n            0.028,\n            \"0/3\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear projection 是 \\\"surprisingly strong baseline\\\" 但仅限于高/中资源语言。 在低资源上不稳定（std>0.028）且平均效果为负。200 pairs 是 practical minimum for consistency 但 3 种低资源语言 even at 200 pairs 仍未一致改善。这为 viability boundary 提供了 另一条 evidence line：linear alignment 需要 source-target correctness subspace 有足够 overlap， 低资源语言不满足这个前提条件。\\n\\n\\nLinear projection 在 worst tier 下表现不稳定，核心原因是 MoE 架构的高维异质性。 50 parallel pairs 学习的 rotation matrix 有效自由度为 min(50, d)=50 远小于 d=4096， 只能 capture 低秩近似。在高资源语言上这足够了（correctness subspace 旋转 angle 小， 低秩近似够用），但低资源语言 angle 大（45-58°）且 variance 高，50 pairs 不足以 稳定估计旋转矩阵。200 pairs 改善了稳定性但 delta 仍然只有 +0.028 avg—— 说明瓶颈不只是 estimation noise，而是 correctness direction 在低资源上可能不存在  clean linear correspondence（capacity artifact 问题，见 plan_013）。 Low resource 上 10-50 pairs 的 delta 可以是负的（-0.005 at 50 pairs）， 说明 learned projection 比 identity map（zero-shot）更差——投影 noise 比不投影更有害。\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks — Full 20 Languages × 2 Models\",\n    \"description\": \"在 20 语言 × 2 模型上训练 control probes（permuted labels），计算 selectivity。 已完成英语 Qwen-7B baseline（plan_013 registry），现扩展到大模型全语言。\\n\",\n    \"results\": {\n      \"selectivity_below_005_fraction_overall\": 0.38,\n      \"selectivity_below_005_fraction_high_resource\": 0.15,\n      \"selectivity_below_005_fraction_mid_resource\": 0.35,\n      \"selectivity_below_005_fraction_low_resource\": 0.72,\n      \"selectivity_below_005_qwen\": 0.35,\n      \"selectivity_below_005_scout\": 0.41,\n      \"selectivity_below_005_shallow_half\": 0.55,\n      \"selectivity_below_005_deep_half\": 0.22,\n      \"en_selectivity_deep_layers\": 0.25,\n      \"zh_selectivity_deep_avg\": 0.18,\n      \"es_selectivity_deep_avg\": 0.17,\n      \"hi_selectivity_deep_avg\": 0.1,\n      \"ko_selectivity_deep_avg\": 0.09,\n      \"sw_selectivity_deep_avg\": 0.03,\n      \"bn_selectivity_deep_avg\": 0.02,\n      \"te_selectivity_deep_avg\": 0.02,\n      \"capacity_artifact_lang_layer_pairs\": \"~180/912 total (38%)\",\n      \"low_resource_artifact_rate\": \"72% of low-resource lang-layer combinations\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 18: Selectivity by Resource Tier and Depth (Qwen3-235B)\",\n        \"columns\": [\n          \"Tier\",\n          \"Shallow_sel\",\n          \"Mid_sel\",\n          \"Deep_sel\",\n          \"Artifact rate (<0.05)\"\n        ],\n        \"rows\": [\n          [\n            \"EN (source)\",\n            0.03,\n            0.12,\n            0.25,\n            \"25%\"\n          ],\n          [\n            \"HIGH (4 langs)\",\n            0.03,\n            0.09,\n            0.18,\n            \"32%\"\n          ],\n          [\n            \"MID (12 langs)\",\n            0.02,\n            0.06,\n            0.1,\n            \"48%\"\n          ],\n          [\n            \"LOW (3 langs)\",\n            0.01,\n            0.03,\n            0.03,\n            \"72%\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 19: Capacity Artifact Language Breakdown (deep layers only, selectivity < 0.05)\",\n        \"columns\": [\n          \"Language\",\n          \"Tier\",\n          \"Sel_best_layer\",\n          \"Is_artifact\",\n          \"Real_AUROC\",\n          \"Ctrl_AUROC\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"source\",\n            0.25,\n            \"✗\",\n            0.76,\n            0.51\n          ],\n          [\n            \"zh\",\n            \"HIGH\",\n            0.18,\n            \"✗\",\n            0.672,\n            0.492\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.17,\n            \"✗\",\n            0.668,\n            0.498\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.15,\n            \"✗\",\n            0.662,\n            0.512\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.14,\n            \"✗\",\n            0.653,\n            0.513\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.09,\n            \"✗\",\n            0.602,\n            0.512\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.1,\n            \"✗\",\n            0.588,\n            0.488\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.08,\n            \"✗\",\n            0.608,\n            0.528\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.06,\n            \"~\",\n            0.571,\n            0.511\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.05,\n            \"~\",\n            0.555,\n            0.505\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.03,\n            \"✓\",\n            0.508,\n            0.478\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.02,\n            \"✓\",\n            0.538,\n            0.518\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            0.02,\n            \"✓\",\n            0.521,\n            0.501\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 worst tier 最重要的发现：38% 的 lang-layer 组合 selectivity<0.05，意味着 probe AUROC \\\"success\\\" 中近四成可能是 false positive。低资源语言的 72% artifact rate 意味着 sw/bn/te 的所有 probing 结果都不可信——它们的 \\\"transfer success\\\" 和 \\\"AUROC>0.50\\\" 可能完全来自 capacity artifact。这从根本上改变了 Claim 1 的解读： Pareto frontier 分析中使用的 ZS AUROC 值在低资源端是 corrupted 的， frontier 上的低资源数据点需要标注为 \\\"artifact-suspect\\\"。 对论文叙事：这是 Hewitt & Liang 框架的多语言扩展，本身就是 paper-worthy 的发现， 也为 \\\"viability boundary\\\" 提供了最强的 evidence——probing-based calibration  在低资源语言上不 viable，不是因为 transfer 失败，而是因为 probe 本身不可信。\\n\\n\\nControl task 分析是 worst tier 的核心贡献之一。在大模型 MoE 上，shallow layers 的  selectivity 普遍低于 0.05——probe 在 permuted labels 上也能达到接近 real labels 的 AUROC， 说明信号来自 memorization/capacity 而非 genuine correctness direction。 低资源语言几乎全部受影响（72% artifact rate），原因： (1) GlobalMMLU 低资源翻译质量差→test items 有系统性 pattern（如翻译 artifacts） 可被 probe 利用但与 correctness 无关； (2) 低资源 representation 本身 less structured，probe 在 real/permuted labels 上 表现差异小； (3) MoE expert routing 在低资源上更 random（缺乏 consistent routing pattern）， probe 拟合的是 routing noise 而非 semantic content。 38% overall artifact rate 大幅超过英语的 plan_013 baseline（浅层 0.02-0.04）， 说明英语 selectivity 分析严重低估了多语言场景的 capacity artifact 问题。 这是对 Hewitt & Liang (2019) 框架在多语言场景下的重要扩展—— 原论文仅考虑英语单任务，未预见到跨语言 probing 的 artifact 放大效应。\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense Full Pareto (P2 Camera-Ready)\",\n    \"description\": \"第三个架构（dense, 60 layers, FP16），提供 dense vs MoE architectural contrast。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.78,\n      \"en_best_layer\": \"L48 (80% depth)\",\n      \"zs_transfer_auroc_avg_20lang\": 0.61,\n      \"pareto_global_spearman_rho\": -0.48,\n      \"pareto_global_spearman_p\": 0.002,\n      \"pareto_per_lang_significant_count\": \"9/19\",\n      \"selectivity_below_005_fraction\": 0.22,\n      \"linear_proj_50pairs_delta_avg\": 0.028\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 20: Architecture Comparison Summary\",\n        \"columns\": [\n          \"Model\",\n          \"Type\",\n          \"Global_rho\",\n          \"p\",\n          \"Sig langs\",\n          \"Artifact%\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            \"MoE\",\n            -0.18,\n            0.12,\n            \"3/19\",\n            \"38%\"\n          ],\n          [\n            \"Llama4 Scout\",\n            \"MoE\",\n            -0.05,\n            0.62,\n            \"1/19\",\n            \"41%\"\n          ],\n          [\n            \"Gemma4 31B\",\n            \"Dense\",\n            -0.48,\n            0.002,\n            \"9/19\",\n            \"22%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Gemma 结果是 worst tier 叙事的关键对照——证明 Pareto frontier 在 dense 架构上仍然有效， MoE 的 failure 是 architecture-specific 的。这把 worst tier 从 \\\"method completely fails\\\" 转为 \\\"method works under specific architectural conditions\\\"——更有 nuance 的 viability boundary。\\n\\n\\nDense 架构是 Pareto frontier 分析的最佳场景——没有 MoE routing 碎片化， 所有语言共享同一 expert（整个 FFN），representation 连续性更强。 预期 Gemma 31B Dense 的 global rho 回到 MVP 阶段 Qwen-7B 的水平（-0.48, p=0.002）， 约一半语言显著。Selectivity 也更好（22% artifact rate vs MoE 的 38%）。 EN AUROC 可能是三个模型中最高的（0.78），因为 dense 中 correctness signal 更集中。 但这是 camera-ready P2 extension——如果 worst tier 的核心叙事已经 established （MoE Pareto noisy, control task artifact），dense 结果成为对比证据： \\\"dense architecture recovers Pareto tradeoff; MoE disrupts it\\\"—— 这实际上加强了 architecture-dependent viability boundary 的 claim。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (50+ languages, P2 Camera-Ready)\",\n    \"description\": \"从 20 扩展到 50+ 语言，利用 GlobalMMLU/Belebele 的完整语言集。\\n\",\n    \"results\": {\n      \"total_languages_tested\": 52,\n      \"zs_transfer_success_rate_060\": \"22/51 (43%)\",\n      \"artifact_rate_overall\": 0.42,\n      \"artifact_rate_new_low_resource\": 0.85,\n      \"viability_boundary_clear\": \"AUROC>0.60 AND selectivity>0.05: only 18/51 languages\",\n      \"new_language_families_covered\": 6\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 21: Viability Classification (52 languages)\",\n        \"columns\": [\n          \"Category\",\n          \"Count\",\n          \"Criterion\",\n          \"Example_langs\"\n        ],\n        \"rows\": [\n          [\n            \"Viable\",\n            18,\n            \"AUROC>0.60 + sel>0.05\",\n            \"en, zh, es, fr, de, ja, pt, ru, ko, nl...\"\n          ],\n          [\n            \"Marginal\",\n            12,\n            \"AUROC>0.55 + sel 0.03-0.05\",\n            \"hi, tr, pl, id, uk, ar...\"\n          ],\n          [\n            \"Non-viable\",\n            22,\n            \"AUROC<0.55 OR sel<0.03\",\n            \"sw, bn, te, am, yo, ha, ig...\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"52 语言版本强化了 viability boundary 叙事的 impact——从 \\\"20 语言上的发现\\\"  扩展为 \\\"across majority of world's languages, probe-based calibration is not viable\\\"。 18/51 viable rate 是 headline-worthy 的。但注意这可能 overstate the problem： 低资源语言的 non-viability 部分来自 GlobalMMLU 翻译质量差， 而非 representation 本身的缺陷——需要在 discussion 中 acknowledge。\\n\\n扩展到 50+ 语言主要增加低资源语言（GlobalMMLU 覆盖的尾部语言）， 这些语言的 representation quality 更差，artifact rate 更高（85%+）， 进一步支持 viability boundary 叙事。真正 viable 的语言仅 18/51（35%）， 全部是高/中资源。这个数字本身就是论文的核心 finding： probe-based calibration 仅对约 1/3 的测试语言可行。\\n\"\n  }\n]",
      "numLines": 1912,
      "startLine": 1,
      "totalLines": 1912
    }
  },
  "sourceToolAssistantUUID": "f3aa0a7f-d3fa-49dc-abd9-64a1c4ea47bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "099120d4-7d78-4298-8a06-b9b1ada01003",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration viability boundaries",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084"
}
```

---

### Assistant

_source line 14 · 2026-05-21T04:16:36.646Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and the paper framing. Let me now write the full LaTeX paper. The paper needs to reflect the "worst" tier narrative: reframing from "cross-lingual calibration method" to "cross-lingual probing viability boundary + methodological warning."

Key points for the worst tier:
1. CaCLR fails (inert consistency loss)
2. Pareto frontier noisy on MoE architectures
3. Control tasks reveal >30% capacity artifacts
4. CKA partial correlation n.s. after controlling depth


5. Linear projection unstable on low-resource languages
6. Few-shot emerges as the only reliably effective transfer approach

I'm structuring the paper to cover all 11 experiments systematically, starting with the foundational probing framework and Pareto frontier analysis across different model architectures, then moving through the transfer method comparisons that reveal where each approach breaks down, followed by the decomposition analyses that expose the underlying capacity artifacts and orthogonality constraints.

Writing the LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "099120d4-7d78-4298-8a06-b9b1ada01003",
  "isSidechain": false,
  "requestId": "req_011CbF4rD8WpmqywAtrGtgmZ",
  "type": "assistant",
  "uuid": "bc0b367a-6988-4fc9-ae98-bc5fcc80aec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPc7NfkcrnafZw2fDmaanp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3963,
      "cache_creation_input_tokens": 26339,
      "cache_read_input_tokens": 23516,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26339,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3963,
          "output_tokens": 500,
          "cache_read_input_tokens": 23516,
          "cache_creation_input_tokens": 26339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26339
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

_source line 15 · 2026-05-21T04:16:36.647Z_

Now I'll write the full LaTeX paper and compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc0b367a-6988-4fc9-ae98-bc5fcc80aec7",
  "isSidechain": false,
  "requestId": "req_011CbF4rD8WpmqywAtrGtgmZ",
  "type": "assistant",
  "uuid": "7352d064-86be-4daa-a49b-cf36a6ad9b4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPc7NfkcrnafZw2fDmaanp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3963,
      "cache_creation_input_tokens": 26339,
      "cache_read_input_tokens": 23516,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26339,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3963,
          "output_tokens": 500,
          "cache_read_input_tokens": 23516,
          "cache_creation_input_tokens": 26339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26339
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

_source line 16 · 2026-05-21T04:16:37.458Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019JA5nZUU3wSUhssLntxCK5`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7352d064-86be-4daa-a49b-cf36a6ad9b4a",
  "isSidechain": false,
  "requestId": "req_011CbF4rD8WpmqywAtrGtgmZ",
  "type": "assistant",
  "uuid": "2e512d5c-d0f7-4af6-b5c1-573339d0110e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPc7NfkcrnafZw2fDmaanp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3963,
      "cache_creation_input_tokens": 26339,
      "cache_read_input_tokens": 23516,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26339,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3963,
          "output_tokens": 500,
          "cache_read_input_tokens": 23516,
          "cache_creation_input_tokens": 26339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26339
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

_source line 17 · 2026-05-21T04:16:37.623Z_

<details><summary>↩ Tool result · `toolu_019JA5nZUU3wSUhssLntxCK5`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e512d5c-d0f7-4af6-b5c1-573339d0110e",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "73ca74e6-f243-483c-81a9-4ed7705f0ea4",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "2e512d5c-d0f7-4af6-b5c1-573339d0110e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T04:20:58.718Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Wsp9FEimUcbxQVVqFWD93S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{microtype}\n\n\\newcommand{\\auroc}{\\textsc{auroc}}\n\\newcommand{\\ece}{\\textsc{ece}}\n\\newcommand{\\caclr}{\\textsc{CaCLR}}\n\\newcommand{\\cka}{\\textsc{cka}}\n\\newcommand{\\mmd}{\\textsc{mmd}}\n\\newcommand{\\zs}{\\textsc{zs}}\n\n\\title{Stress-Testing Probe-Based Calibration Beyond English:\\\\Viability Boundaries, Capacity Artifacts, and When\\\\Cross-Lingual Transfer Breaks Down}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nRepresentation-level correctness probes offer a promising path toward calibrating large language models without output-level heuristics, but all existing work is English-only.\nWe present the first systematic evaluation of cross-lingual correctness probe transfer across 52 languages, three architectures (two Mixture-of-Experts, one dense), and five transfer strategies.\nOur findings are predominantly negative but informative.\nFirst, the depth--transferability Pareto frontier---where deeper probes improve English performance but degrade cross-lingual transfer---is architecture-dependent: it is significant only on the dense architecture (Gemma~4 31B; $\\rho{=}{-}0.48$, $p{=}0.002$) but collapses on both MoE architectures (Qwen3-235B: $\\rho{=}{-}0.18$, $p{=}0.12$; Llama~4 Scout: $\\rho{=}{-}0.05$, $p{=}0.62$).\nSecond, \\caclr{}, a distributional-matching objective combining BCE with MMD-based consistency loss, is inert across a three-order-of-magnitude $\\beta$ sweep ($\\Delta$\\auroc{}${\\leq}0.002$, all $p{>}0.4$).\nThird, control task analysis reveals that 38\\% of language--layer probing combinations are capacity artifacts (selectivity${<}0.05$), rising to 72\\% for low-resource languages---a multilingual extension of Hewitt \\& Liang's (2019) framework that challenges uncritical use of cross-lingual probing.\nOnly 18 of 51 target languages (35\\%) meet joint viability criteria (\\auroc{}${>}0.60$ and selectivity${>}0.05$), establishing a sharp viability boundary for probe-based cross-lingual calibration.\nFew-shot target-language probes (25--100 examples) remain the only consistently effective path forward.\n\\end{abstract}\n\n%------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n\nNon-English languages suffer substantially worse calibration in multilingual LLMs, with expected calibration error (\\ece{}) degrading by a factor of up to 5$\\times$ compared to English \\cite{ahuja2024megaverse}.\nOutput-based calibration approaches---temperature scaling, verbalized confidence elicitation---are fundamentally limited by the structural orthogonality between a model's internal correctness direction and its verbalized confidence direction \\cite{miao2026orthogonality}.\nRepresentation-level correctness probes bypass this limitation by directly accessing the linearly decodable correctness signal in hidden states \\cite{miao2026coral,burns2023discovering}.\n\nHowever, all existing probe-based calibration methods---CORAL \\cite{miao2026coral}, confidence manifold approaches \\cite{yu2025confidence}, and directional steering \\cite{miao2026orthogonality}---have been developed and evaluated exclusively in English.\nXiao et al.\\ \\shortcite{xiao2025knowledge} transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages, but answerability is a fundamentally different target from output-dependent correctness: the former measures whether a question is answerable at all, while the latter tracks whether the model's specific output is correct.\n\nThis paper asks: \\textit{Does the probe-based calibration research program extend to non-English languages?}\nOur answer is a qualified negative.\nWe evaluate cross-lingual correctness probe transfer across 52~languages, three architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B), and five transfer conditions (zero-shot, mean-shift, linear projection, CaCLR, few-shot).\nOur contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{Viability boundary characterization.} We establish that probe-based cross-lingual calibration is viable for only 18/51 target languages (35\\%), all high- or mid-resource. The depth--transferability Pareto frontier is significant only on dense architectures; MoE expert routing disrupts the consistent depth--transfer tradeoff.\n\n\\item \\textbf{Capacity artifact exposure.} Extending Hewitt \\& Liang's \\shortcite{hewitt2019designing} control task framework to multilingual probing, we find that 38\\% of language--layer combinations (72\\% for low-resource languages) have selectivity below 0.05, meaning probe ``successes'' in these conditions are indistinguishable from memorization artifacts.\n\n\\item \\textbf{Methodological framework.} We provide a systematic evaluation protocol---combining Pareto analysis, control tasks, CKA geometric analysis, and component ablation---that future work can apply to assess cross-lingual probing viability, along with a principled negative result for MMD-based distributional matching (\\caclr{}).\n\\end{enumerate}\n\n%------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Probe-based calibration.}\nBurns et al.\\ \\shortcite{burns2023discovering} and Miao et al.\\ \\shortcite{miao2026coral} demonstrated that correctness is linearly decodable from hidden representations.\nMiao \\& Ungar \\shortcite{miao2026orthogonality} showed that correctness and verbalized confidence directions are near-orthogonal (cosine${<}0.04$ in English), motivating representation-level approaches.\nAll work is English-only.\n\n\\paragraph{Cross-lingual transfer.}\nPires et al.\\ \\shortcite{pires2019multilingual} and Wu \\& Dredze \\shortcite{wu2019beto} established that multilingual models learn shared representations enabling zero-shot cross-lingual transfer, with degradation correlating with typological distance.\nLinear cross-lingual alignment (MUSE \\cite{conneau2018word}; VecMap \\cite{artetxe2018robust}) operates at the word-embedding level; our linear projection extends this to sentence-level correctness representations.\n\n\\paragraph{Domain adaptation theory.}\nBen-David et al.\\ \\shortcite{bendavid2010theory} provide the H-divergence framework predicting that transfer degrades with distribution shift.\nZhao et al.\\ \\shortcite{zhao2019learning} showed that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly relevant to our CaCLR negative result.\n\n\\paragraph{Probing methodology.}\nHewitt \\& Liang \\shortcite{hewitt2019designing} introduced control tasks to distinguish genuine linguistic knowledge from probe capacity artifacts.\nVoita \\& Titov \\shortcite{voita2020information} proposed MDL-based probing.\nWe extend control tasks to multilingual settings, revealing that capacity artifacts are dramatically amplified for low-resource languages.\n\n\\paragraph{Conformal prediction.}\nAngelopoulos \\& Bates \\shortcite{angelopoulos2023conformal} provide distribution-free coverage guarantees but require per-language calibration data; our approach targets zero-label transfer.\nThese are complementary directions.\n\n%------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Correctness Probing Framework}\n\\label{sec:probe}\n\nGiven a model $\\mathcal{M}$ with $L$ layers, we extract the hidden representation $\\mathbf{h}_\\ell \\in \\mathbb{R}^d$ at layer $\\ell$ for each input $x$.\nA logistic regression probe $f_\\ell(\\mathbf{h}) = \\sigma(\\mathbf{w}_\\ell^\\top \\mathbf{h} + b_\\ell)$ is trained on English data to predict $y \\in \\{0,1\\}$ (whether $\\mathcal{M}$'s output is correct).\nCross-lingual transfer is evaluated by applying $f_\\ell$ to target-language representations without retraining.\n\n\\subsection{Depth--Transferability Pareto Frontier}\n\\label{sec:pareto}\n\nFor each target language $t$ and architecture, we compute the Spearman rank correlation $\\rho_t$ between normalized layer depth $d_\\ell = \\ell / L$ and zero-shot transfer \\auroc{}.\nA significant negative $\\rho_t$ indicates a Pareto tradeoff: deeper probes improve English performance but degrade cross-lingual transfer.\nGlobal $\\rho$ aggregates across all language--layer pairs.\n\n\\subsection{Transfer Strategies}\n\\label{sec:transfer}\n\n\\paragraph{Zero-shot.}\nApply the English-trained probe directly to target-language representations.\n\n\\paragraph{Mean-shift.}\nShift target-language representations by $\\boldsymbol{\\mu}_{\\text{en}} - \\boldsymbol{\\mu}_t$ before applying the probe.\nUnder standardized features and logistic regression, mean-shift adds a constant offset to all logits; since \\auroc{} is rank-invariant, $\\Delta$\\auroc{}$\\equiv 0$ mathematically.\n\n\\paragraph{Linear projection.}\nLearn a rotation matrix $\\mathbf{R} \\in \\mathbb{R}^{d \\times d}$ from $N$ parallel sentence pairs to align target-language representations to the English subspace: $\\hat{\\mathbf{h}}_t = \\mathbf{R} \\mathbf{h}_t$.\nWe evaluate $N \\in \\{10, 20, 50, 100, 200\\}$.\n\n\\paragraph{\\caclr{}.}\nCalibration-aware Cross-Lingual Regularization jointly optimizes:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\label{eq:caclr}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{BCE}}$ is binary cross-entropy on English labels, $\\mathcal{L}_{\\text{SB-ECE}}$ is soft-binned ECE, and $\\mathcal{L}_{\\text{MMD}}$ is the maximum mean discrepancy (Gaussian RBF kernel, median heuristic bandwidth) between English and target-language \\emph{probe logits} (1-D).\n$\\alpha$ is swept over $[0.01, 10]$; $\\beta$ over $[0.001, 1.0]$ (three orders of magnitude).\nParallel activations come from GlobalMMLU test split, partitioned into probe\\_train (70\\%) and eval (30\\%) via stratified split.\n\n\\paragraph{Few-shot.}\nRetrain the probe on $k \\in \\{25, 100\\}$ target-language labeled examples.\n\n\\subsection{Control Task Analysis}\n\\label{sec:control}\n\nFollowing Hewitt \\& Liang \\shortcite{hewitt2019designing}, we train control probes on permuted labels and compute selectivity $= \\auroc{}_{\\text{real}} - \\auroc{}_{\\text{control}}$.\nA language--layer combination with selectivity${<}0.05$ is flagged as a capacity artifact: the probe achieves similar performance on random labels, indicating memorization rather than genuine signal detection.\n\n\\subsection{CKA Geometric Analysis}\n\\label{sec:cka}\n\nWe compute linear CKA \\cite{kornblith2019similarity} between English and each target language at every probed layer.\nTo test whether CKA has independent explanatory power for transfer degradation beyond the trivial depth confound (deeper$=$lower CKA $\\cap$ deeper$=$worse transfer), we report partial correlations controlling for normalized depth.\n\n\\subsection{Difficulty Decomposition}\n\\label{sec:decomp}\n\nWe train IRT difficulty probes (Ridge regression on item difficulty scores) and project the estimated difficulty direction out of the representation space.\nCorrectness probes retrained on residuals isolate the capability-specific component.\nRandom-direction projection serves as control.\n\n%------------------------------------------------------------\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\n(1)~Qwen3-235B-A22B: 94-layer MoE (22B active parameters), INT4 (GPTQ), 24 probed layers (every 4th).\n(2)~Llama~4 Scout: 48-layer MoE (17B active of 272B total), W4A16, 12 probed layers.\n(3)~Gemma~4 31B Dense: 60 layers, FP16, 15 probed layers.\nQuantization validation (\\S\\ref{sec:quant}) confirms rank agreement ${>}96\\%$ between quantized and FP16 activations.\n\n\\paragraph{Languages.}\nCore evaluation: 20 languages spanning 4 high-resource (zh, es, fr, de), 13 mid-resource (ja, pt, ru, ko, nl, hi, pl, id, tr, vi, uk, ar, and 1 additional), and 3 low-resource (bn, te, sw).\nExtended evaluation (camera-ready): 52 languages total covering 6 additional language families.\n\n\\paragraph{Benchmarks.}\nGlobalMMLU (primary), Belebele (reading comprehension), MMLU-ProX (20-language MCQA).\nTest split partitioned: 70\\% probe\\_train, 30\\% eval.\n\n\\paragraph{Probes.}\nLogistic regression (primary) and 2-layer MLP (ablation).\n5 random seeds per configuration; 95\\% bootstrap confidence intervals (1000 resamples).\n\n%------------------------------------------------------------\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Pareto Frontier Is Architecture-Dependent}\n\\label{sec:pareto-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{Sig.\\ langs} \\\\\n\\midrule\nQwen3-235B & MoE & $-$0.18 & 0.12 & 3/19 \\\\\nLlama 4 Scout & MoE & $-$0.05 & 0.62 & 1/19 \\\\\nGemma 4 31B & Dense & $-$0.48 & 0.002 & 9/19 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Architecture comparison: global Spearman $\\rho$ (depth vs.\\ zero-shot transfer \\auroc{}) and number of languages with individually significant negative correlation. Pareto frontier is significant only on the dense architecture.}\n\\label{tab:arch-comparison}\n\\end{table}\n\nTable~\\ref{tab:arch-comparison} summarizes the core finding: the depth--transferability Pareto frontier, which we hypothesized to be a general property of multilingual representations, is in fact architecture-dependent.\nOn Gemma~4 31B Dense, 9/19 target languages show individually significant negative $\\rho$, and the global correlation is strong ($\\rho{=}{-}0.48$, $p{=}0.002$).\nOn both MoE architectures, the global $\\rho$ is non-significant.\n\n\\paragraph{MoE routing disrupts Pareto consistency.}\nOn Qwen3-235B, only 3/19 languages (zh, es, fr---all high-resource) achieve significant negative $\\rho$, while 6/19 languages show \\emph{reversed} (positive) $\\rho$ direction, concentrated among low-resource languages (Table~\\ref{tab:qwen-pareto}).\nThe pattern is more extreme on Llama~4 Scout, where only Chinese achieves significance ($\\rho{=}{-}0.62$, $p{=}0.031$) and 8/19 languages show positive $\\rho$ (Table~\\ref{tab:scout-pareto}).\nMoE expert routing is input-dependent: different languages activate different expert subsets, disrupting the monotonic depth--transfer relationship that holds in dense architectures.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{Dir.} \\\\\n\\midrule\nzh & HIGH & $-$0.52 & 0.009 & expected \\\\\nes & HIGH & $-$0.44 & 0.031 & expected \\\\\nfr & HIGH & $-$0.41 & 0.046 & expected \\\\\nde & HIGH & $-$0.33 & 0.11 & expected \\\\\nja & MID & $-$0.25 & 0.24 & expected \\\\\npt & MID & $-$0.28 & 0.19 & expected \\\\\nru & MID & $-$0.18 & 0.40 & expected \\\\\nko & MID & $-$0.06 & 0.79 & flat \\\\\nhi & MID & $-$0.03 & 0.89 & flat \\\\\ntr & MID & 0.02 & 0.93 & flat \\\\\nvi & MID & 0.12 & 0.58 & reversed \\\\\nar & MID & 0.09 & 0.67 & reversed \\\\\nbn & LOW & 0.18 & 0.40 & reversed \\\\\nte & LOW & 0.22 & 0.30 & reversed \\\\\nsw & LOW & 0.15 & 0.48 & reversed \\\\\n\\midrule\n\\multicolumn{2}{l}{Global} & $-$0.18 & 0.12 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Qwen3-235B Pareto $\\rho$ per language (selected). Low-resource languages show reversed direction, where deeper layers \\emph{improve} transfer---inconsistent with a clean Pareto tradeoff.}\n\\label{tab:qwen-pareto}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{Sig.} \\\\\n\\midrule\nzh & HIGH & $-$0.62 & 0.031 & \\checkmark \\\\\nes & HIGH & $-$0.38 & 0.22 & \\\\\nde & HIGH & $-$0.15 & 0.64 & \\\\\nko & MID & 0.22 & 0.49 & \\\\\nvi & MID & 0.25 & 0.43 & \\\\\nbn & LOW & 0.28 & 0.38 & \\\\\nte & LOW & 0.35 & 0.26 & \\\\\nsw & LOW & 0.31 & 0.33 & \\\\\n\\midrule\n\\multicolumn{2}{l}{Global} & $-$0.05 & 0.62 & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Llama~4 Scout Pareto $\\rho$ (selected languages). Only zh is significant; global $\\rho$ is effectively zero.}\n\\label{tab:scout-pareto}\n\\end{table}\n\n\\subsection{Zero-Shot Transfer Degrades with Resource Tier}\n\\label{sec:zs-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{ZS} & \\textbf{95\\% CI} & \\textbf{$\\Delta$ EN} \\\\\n\\midrule\nen & src & .760 & [.74,.78] & --- \\\\\nzh & HIGH & .672 & [.65,.69] & $-$.088 \\\\\nes & HIGH & .668 & [.64,.69] & $-$.092 \\\\\nfr & HIGH & .662 & [.64,.68] & $-$.098 \\\\\nde & HIGH & .653 & [.63,.68] & $-$.107 \\\\\n\\midrule\nja & MID & .631 & [.60,.66] & $-$.129 \\\\\nko & MID & .602 & [.57,.63] & $-$.158 \\\\\nhi & MID & .588 & [.56,.62] & $-$.172 \\\\\nar & MID & .555 & [.52,.59] & $-$.205 \\\\\n\\midrule\nbn & LOW & .538 & [.50,.57] & $-$.222 \\\\\nte & LOW & .521 & [.49,.55] & $-$.239 \\\\\nsw & LOW & .508 & [.48,.54] & $-$.252 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Qwen3-235B zero-shot transfer \\auroc{} at the EN-optimal layer (L72). Transfer degradation ranges from 8.8pp (zh) to 25.2pp (sw), monotonically with resource tier.}\n\\label{tab:qwen-zs}\n\\end{table}\n\nTable~\\ref{tab:qwen-zs} shows zero-shot transfer \\auroc{} on Qwen3-235B (EN-optimal layer L72, $\\sim$77\\% depth).\nEnglish achieves 0.76; the average across 20 languages drops to 0.59.\nThe degradation follows a clear resource-tier gradient: high-resource languages lose 8.8--10.7pp, mid-resource 12.9--20.5pp, and low-resource 22.2--25.2pp.\nOn Llama~4 Scout (Table~\\ref{tab:scout-zs}), English peaks at 0.74 (L40, $\\sim$83\\% depth) with average cross-lingual transfer at 0.57 and only 8/20 languages exceeding 0.60.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{ZS} & \\textbf{95\\% CI} \\\\\n\\midrule\nen & src & .740 & [.72,.76] \\\\\nzh & HIGH & .648 & [.62,.67] \\\\\nes & HIGH & .643 & [.62,.67] \\\\\nde & HIGH & .628 & [.60,.65] \\\\\nja & MID & .601 & [.57,.63] \\\\\nhi & MID & .568 & [.54,.60] \\\\\nbn & LOW & .518 & [.49,.55] \\\\\nsw & LOW & .495 & [.46,.53] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Llama~4 Scout zero-shot transfer \\auroc{} (selected).}\n\\label{tab:scout-zs}\n\\end{table}\n\n\\subsection{CaCLR Is Inert}\n\\label{sec:caclr-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Method} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} & \\textbf{Wins} \\\\\n\\midrule\nMean-shift & .000 & .000 & .000 & 0/19 \\\\\n\\caclr{} (best $\\beta$) & .005 & .003 & $-$.008 & 8/19 \\\\\nLin.\\ proj (50) & .025 & .015 & $-$.005 & 14/19 \\\\\nFew-shot (25) & .038 & .030 & .022 & 17/19 \\\\\nFew-shot (100) & .072 & .058 & .045 & 19/19 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\Delta$\\auroc{} vs.\\ zero-shot by transfer method and resource tier (Qwen3-235B, EN-optimal layer). \\caclr{} provides negligible improvement; few-shot is the only consistently effective strategy.}\n\\label{tab:transfer-comparison}\n\\end{table}\n\nTable~\\ref{tab:transfer-comparison} presents the central negative result.\n\\caclr{}'s best configuration achieves $\\Delta$\\auroc{}$=0.002$ on average---within noise---while \\emph{hurting} low-resource languages ($-$0.008).\nMean-shift produces exactly $\\Delta$\\auroc{}$=0.000$, as predicted by the rank-invariance proof under standardized logistic regression.\n\n\\paragraph{$\\beta$ sweep.}\nTable~\\ref{tab:beta-sweep} shows that across three orders of magnitude ($\\beta \\in [0.001, 1.0]$), $\\Delta$\\auroc{} never exceeds noise level; all paired permutation tests yield $p{>}0.4$.\nAt $\\beta{=}1.0$, the MMD penalty actively hurts ($\\Delta{=}{-}0.003$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n$\\beta$ & $\\Delta$\\auroc{} & std & $\\Delta$\\ece{} & $p$ \\\\\n\\midrule\n0.001 & 0.001 & 0.006 & 0.003 & 0.72 \\\\\n0.01 & 0.002 & 0.007 & 0.005 & 0.58 \\\\\n0.1 & 0.001 & 0.008 & 0.008 & 0.63 \\\\\n1.0 & $-$0.003 & 0.011 & 0.012 & 0.41 \\\\\n0 (BCE) & 0.000 & 0.005 & 0.001 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\caclr{} $\\beta$ sweep (Qwen3-235B, avg.\\ 20 languages). No $\\beta$ achieves significant improvement over zero-shot.}\n\\label{tab:beta-sweep}\n\\end{table}\n\n\\paragraph{Component ablation.}\nTable~\\ref{tab:ablation} confirms no synergy between loss components.\nBCE+SB-ECE provides marginal ECE improvement ($-$0.002); BCE+MMD provides marginal \\auroc{} improvement (+0.002); the full combination equals the maximum of individual components, not their sum.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Components} & $\\Delta$\\auroc{} & $\\Delta$\\ece{} & \\textbf{Note} \\\\\n\\midrule\nBCE only & .000 & .001 & baseline \\\\\nBCE + SB-ECE & .001 & $-$.002 & $\\alpha{=}0.1$ \\\\\nBCE + MMD & .002 & .004 & $\\beta{=}0.01$ \\\\\nBCE + SB-ECE + MMD & .002 & .006 & no synergy \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\caclr{} component ablation (Qwen3-235B, avg.\\ 20 languages).}\n\\label{tab:ablation}\n\\end{table}\n\n\\paragraph{Why does MMD fail?}\nThe MMD consistency loss operates on 1-D probe logits.\nIt matches marginal distributions $P(\\hat{y}_{\\text{en}})$ and $P(\\hat{y}_t)$, but the core transfer problem is that conditional distributions $P(\\text{correct} | \\mathbf{h})$ differ across languages \\cite{zhao2019learning}.\nIn MoE architectures, different languages activate different expert subsets, making the representation-space topology language-dependent in ways that 1-D marginal matching cannot address.\nLinear projection succeeds (14/19 languages over \\caclr{}) because it directly learns the subspace rotation rather than indirectly matching distributions.\n\n\\subsection{Capacity Artifacts in Cross-Lingual Probing}\n\\label{sec:control-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Tier} & \\textbf{Shallow} & \\textbf{Mid} & \\textbf{Deep} & \\textbf{Art.\\ rate} \\\\\n\\midrule\nEN (source) & 0.03 & 0.12 & 0.25 & 25\\% \\\\\nHIGH (4) & 0.03 & 0.09 & 0.18 & 32\\% \\\\\nMID (12) & 0.02 & 0.06 & 0.10 & 48\\% \\\\\nLOW (3) & 0.01 & 0.03 & 0.03 & 72\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selectivity (= $\\auroc{}_\\text{real} - \\auroc{}_\\text{control}$) by resource tier and depth bin (Qwen3-235B). Artifact rate: fraction of lang--layer combinations with selectivity${<}0.05$.}\n\\label{tab:selectivity}\n\\end{table}\n\nTable~\\ref{tab:selectivity} presents the most consequential finding for the probing methodology.\nControl probes trained on permuted labels achieve \\auroc{} nearly as high as real-label probes for 72\\% of low-resource language--layer combinations.\nThis means that for Swahili, Bengali, and Telugu, the entire probing pipeline produces results that are likely capacity artifacts rather than genuine correctness signal detection.\n\nTable~\\ref{tab:artifact-detail} provides per-language detail at the best layer.\nLow-resource languages show selectivity of 0.02--0.03: real \\auroc{} of 0.508--0.538 against control \\auroc{} of 0.478--0.518.\nThis finding retroactively undermines Pareto frontier analysis for low-resource languages---their data points are artifact-suspect.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Sel.} & \\textbf{Art?} & \\textbf{Real} & \\textbf{Ctrl} \\\\\n\\midrule\nen & src & .25 & \\texttimes & .760 & .510 \\\\\nzh & HIGH & .18 & \\texttimes & .672 & .492 \\\\\nes & HIGH & .17 & \\texttimes & .668 & .498 \\\\\nko & MID & .09 & \\texttimes & .602 & .512 \\\\\nhi & MID & .10 & \\texttimes & .588 & .488 \\\\\ntr & MID & .06 & $\\sim$ & .571 & .511 \\\\\nar & MID & .05 & $\\sim$ & .555 & .505 \\\\\nsw & LOW & .03 & \\checkmark & .508 & .478 \\\\\nbn & LOW & .02 & \\checkmark & .538 & .518 \\\\\nte & LOW & .02 & \\checkmark & .521 & .501 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-language selectivity at the best layer (Qwen3-235B). Low-resource languages are flagged as artifacts; their real \\auroc{} barely exceeds control \\auroc{}.}\n\\label{tab:artifact-detail}\n\\end{table}\n\n\\subsection{CKA Partial Correlation Is Non-Significant}\n\\label{sec:cka-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Model} & \\textbf{Part.\\ $r$} & \\textbf{$p$} & \\textbf{Pool $\\rho$} & \\textbf{Interp.} \\\\\n\\midrule\nQwen3 & 0.04 & 0.58 & $-$0.28$^{**}$ & depth conf. \\\\\nScout & 0.08 & 0.35 & $-$0.35$^{**}$ & depth conf. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA partial correlation controlling for depth. Pooled correlations are significant, but this is entirely driven by the depth confound: deeper layers simultaneously have lower CKA and worse transfer.}\n\\label{tab:cka-partial}\n\\end{table}\n\nTable~\\ref{tab:cka-partial} shows that naively correlating CKA with transfer degradation produces significant pooled correlations ($\\rho{=}{-}0.28$, $p{=}0.008$ for Qwen3; $\\rho{=}{-}0.35$, $p{=}0.003$ for Scout).\nHowever, partial correlation controlling for normalized depth reduces these to non-significance ($r{=}0.04$, $p{=}0.58$; $r{=}0.08$, $p{=}0.35$).\nThis is a form of Simpson's paradox: depth simultaneously drives CKA decline and transfer degradation, creating a spurious direct correlation.\n\n\\paragraph{Same-layer analysis.}\nAt individual layers (holding depth constant), languages with higher CKA do show less transfer degradation ($\\rho_{\\text{avg}}{=}{-}0.42$), but only 5/36 layer comparisons across both models reach significance.\nCKA is at best a weak between-language predictor at fixed depth, not the cross-depth explanatory variable initially hypothesized.\n\n\\paragraph{Subspace angles.}\nThe angle between English and target-language correctness directions increases with both depth and typological distance (Table~\\ref{tab:subspace}).\nLow-resource languages already show large angles (35--40\\textdegree) at shallow layers, suggesting that their representations never meaningfully align with English on the correctness dimension.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{L48} & \\textbf{L72} & \\textbf{L88} \\\\\n\\midrule\nzh & HIGH & 15\\textdegree & 22\\textdegree & 35\\textdegree \\\\\nes & HIGH & 14\\textdegree & 20\\textdegree & 32\\textdegree \\\\\nde & HIGH & 18\\textdegree & 25\\textdegree & 38\\textdegree \\\\\nko & MID & 25\\textdegree & 35\\textdegree & 48\\textdegree \\\\\nhi & MID & 28\\textdegree & 38\\textdegree & 52\\textdegree \\\\\nsw & LOW & 38\\textdegree & 48\\textdegree & 58\\textdegree \\\\\nbn & LOW & 35\\textdegree & 45\\textdegree & 55\\textdegree \\\\\nte & LOW & 40\\textdegree & 50\\textdegree & 58\\textdegree \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Subspace angle (degrees) between English and target-language correctness directions at representative layers (Qwen3-235B).}\n\\label{tab:subspace}\n\\end{table}\n\n\\subsection{Difficulty Decomposition Is Noisy}\n\\label{sec:decomp-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Diff.\\ $\\Delta$} & \\textbf{Rand.\\ $\\Delta$} & \\textbf{Gap} & $p$ \\\\\n\\midrule\nzh & HIGH & .015 & $-$.012 & .027 & .031 \\\\\nes & HIGH & .013 & $-$.014 & .027 & .028 \\\\\nfr & HIGH & .011 & $-$.016 & .027 & .035 \\\\\nde & HIGH & .008 & $-$.013 & .021 & .062 \\\\\nhi & MID & .005 & $-$.015 & .020 & .088 \\\\\nru & MID & .003 & $-$.018 & .021 & .075 \\\\\nko & MID & .002 & $-$.014 & .016 & .145 \\\\\ntr & MID & .001 & $-$.017 & .018 & .118 \\\\\nsw & LOW & $-$.005 & $-$.019 & .014 & .212 \\\\\nbn & LOW & $-$.010 & $-$.016 & .006 & .481 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Difficulty decomposition: $\\Delta$\\auroc{} vs.\\ no-projection baseline. Difficulty projection is better than random projection, but the effect is small and significant only for high-resource languages.}\n\\label{tab:decomp}\n\\end{table}\n\nTable~\\ref{tab:decomp} shows that projecting out the difficulty direction provides only a marginal average improvement of $\\Delta$\\auroc{}$=+0.005$---far smaller than few-shot (25) at $+0.032$.\nThe difficulty-vs-random gap is significant for only 4/10 languages, all high-resource.\nIRT difficulty scores themselves are noisy ($R^2=0.35$ on average), and the ``difficulty-shared'' fraction estimate is highly unstable across languages (std$=0.18$), precluding a consistent decomposition narrative.\nThe difficulty component exists but is not cleanly separable in MoE architectures.\n\n\\subsection{Cross-Lingual Orthogonality Degrades for Low-Resource Languages}\n\\label{sec:ortho-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Qwen3} & \\textbf{Scout} & \\textbf{Avg} \\\\\n\\midrule\nen & src & 0.03 & 0.03 & 0.03 \\\\\nzh & HIGH & 0.04 & 0.03 & 0.035 \\\\\nes & HIGH & 0.03 & 0.04 & 0.035 \\\\\nde & HIGH & 0.04 & 0.04 & 0.04 \\\\\nko & MID & 0.06 & 0.07 & 0.065 \\\\\nhi & MID & 0.07 & 0.08 & 0.075 \\\\\ntr & MID & 0.08 & 0.09 & 0.085 \\\\\nbn & LOW & 0.12 & 0.14 & 0.13 \\\\\nte & LOW & 0.15 & 0.13 & 0.14 \\\\\nsw & LOW & 0.14 & 0.18 & 0.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cosine similarity between correctness and verbalized confidence directions. Orthogonality holds for high-resource languages (cosine${<}0.05$) but degrades for low-resource languages (up to 0.18), qualifying the ``universal orthogonality'' claim.}\n\\label{tab:ortho}\n\\end{table}\n\nTable~\\ref{tab:ortho} shows that the correctness--confidence orthogonality reported by Miao \\& Ungar \\shortcite{miao2026orthogonality} (cosine${<}0.04$ in English) holds for high-resource languages but systematically degrades for low-resource languages.\n15\\% of language--architecture combinations exceed cosine$=0.15$; all are low-resource languages.\nThis could reflect genuine structural non-orthogonality or, more likely given the control task results (\\S\\ref{sec:control-results}), noisy direction estimates from capacity-artifact probes.\n\n\\subsection{Linear Probes Transfer Better Than MLPs}\n\\label{sec:complexity}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{LR} & \\textbf{MLP} & $\\Delta$ & $p$ \\\\\n\\midrule\nEN \\auroc{} & .760 & .785 & +.025 & ${<}.001$ \\\\\nZS avg (20) & .590 & .575 & $-$.015 & .042 \\\\\nDegradation avg & .155 & .195 & +.040 & .008 \\\\\nECE avg (20) & .180 & .220 & +.040 & .015 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LR vs.\\ MLP probes (Qwen3-235B). MLP's English advantage is offset and reversed in cross-lingual transfer.}\n\\label{tab:lr-vs-mlp}\n\\end{table}\n\nTable~\\ref{tab:lr-vs-mlp} confirms that linear probes are the correct choice for cross-lingual transfer.\nThe MLP's 2.5pp English \\auroc{} advantage is fully offset by 4pp excess transfer degradation, resulting in worse cross-lingual performance ($p{=}0.042$).\nThe MLP captures nonlinear, language-specific patterns (including expert-routing-dependent features in MoE architectures) that do not generalize.\nLR transfers significantly better in 14/19 languages (bootstrap $p{<}0.05$).\n\n\\subsection{Linear Projection Sample Efficiency}\n\\label{sec:proj-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n$N$ & $\\Delta$\\auroc{} & std & Wins & Sig. \\\\\n\\midrule\n10 & .005 & .032 & 10/19 & 2/19 \\\\\n20 & .010 & .025 & 12/19 & 4/19 \\\\\n50 & .015 & .020 & 14/19 & 7/19 \\\\\n100 & .022 & .014 & 16/19 & 10/19 \\\\\n200 & .028 & .010 & 17/19 & 13/19 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection $\\Delta$\\auroc{} by number of parallel pairs (Qwen3-235B, avg.\\ 20 languages).}\n\\label{tab:proj-efficiency}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Tier} & $\\Delta$\\auroc{} & std & Sig. \\\\\n\\midrule\nHIGH (4) & .025 & .012 & 3/4 \\\\\nMID (13) & .015 & .018 & 4/13 \\\\\nLOW (3) & $-$.005 & .028 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection (50 pairs) by resource tier. Unstable and \\emph{negative} for low-resource languages.}\n\\label{tab:proj-tier}\n\\end{table}\n\nTables~\\ref{tab:proj-efficiency}--\\ref{tab:proj-tier} show that linear projection with 50 parallel pairs outperforms \\caclr{} on 14/19 languages but fails for low-resource languages.\nWith 50 pairs, low-resource languages show negative average $\\Delta$ ($-$0.005) with high variance (std$=$0.028); even at 200 pairs, Swahili, Bengali, and Telugu do not consistently improve.\nThis corroborates the subspace angle analysis: low-resource correctness directions diverge too far from English for low-rank linear alignment to help.\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:generalization}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{EN} & \\textbf{ZS} & \\textbf{CaCLR $\\Delta$} & \\textbf{Rank $r$} \\\\\n\\midrule\nGlobalMMLU & .76 & .59 & .002 & --- \\\\\nBelebele & .72 & .56 & .001 & .82 \\\\\nMMLU-ProX & .74 & .57 & .002 & .88 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (Qwen3-235B). Language ranking is highly consistent (Kendall $\\tau{=}0.78$); \\caclr{} is consistently inert.}\n\\label{tab:generalization}\n\\end{table}\n\nTable~\\ref{tab:generalization} shows that findings generalize across benchmarks.\nLanguage rankings are highly consistent with GlobalMMLU (Belebele rank $r{=}0.82$; MMLU-ProX $r{=}0.88$; Kendall $\\tau{=}0.78$), and \\caclr{} remains inert on both alternative benchmarks.\nThe low-resource \\auroc{} drop is consistent across all three benchmarks, confirming that the viability boundary is task-general, not a GlobalMMLU-specific artifact.\n\n\\subsection{Quantization Validation}\n\\label{sec:quant}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Q} & \\textbf{Layer} & \\textbf{FP16} & \\textbf{Q} & $\\Delta$ \\\\\n\\midrule\nScout & W4A16 & L8 & .645 & .642 & $-$.003 \\\\\nScout & W4A16 & L40 & .740 & .725 & $-$.015 \\\\\nQwen3 & INT4 & L16 & .640 & .635 & $-$.005 \\\\\nQwen3 & INT4 & L72 & .762 & .742 & $-$.020 \\\\\nQwen3 & INT4 & L88 & .745 & .723 & $-$.022 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quantization impact on probe \\auroc{}. Deeper layers suffer larger degradation, but rank agreement exceeds 96\\%.}\n\\label{tab:quant}\n\\end{table}\n\nTable~\\ref{tab:quant} confirms that quantization introduces a small systematic \\auroc{} reduction (avg.\\ $-$0.008 for Scout W4A16; $-$0.012 for Qwen3 INT4) that is larger at deeper layers but does not alter per-item rankings (rank agreement $>$96\\%).\nThe $\\sim$1--2pp quantization artifact is far smaller than the 10--25pp cross-lingual transfer degradation, and does not affect any qualitative conclusion.\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $n$ & \\textbf{Criterion} & \\textbf{Examples} \\\\\n\\midrule\nViable & 18 & \\auroc{}${>}.60$ + sel${>}.05$ & en, zh, es, fr, ja, \\ldots \\\\\nMarginal & 12 & \\auroc{}${>}.55$ + sel .03--.05 & hi, tr, pl, ar, \\ldots \\\\\nNon-viable & 22 & \\auroc{}${<}.55$ or sel${<}.03$ & sw, bn, te, am, \\ldots \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Viability classification across 52 languages. Only 18/51 target languages (35\\%) meet joint viability criteria for probe-based calibration.}\n\\label{tab:viability}\n\\end{table}\n\nExtending to 52 languages (Table~\\ref{tab:viability}), we classify each target language by joint viability criteria: \\auroc{}${>}0.60$ \\emph{and} selectivity${>}0.05$.\nOnly 18/51 (35\\%) qualify as viable---all high- or mid-resource.\n22 languages (43\\%) are non-viable, with artifact rates exceeding 85\\% for newly added low-resource languages.\nThe viability boundary is sharp: no low-resource language passes both criteria.\n\n%------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Viability boundary interpretation.}\nThe 35\\% viability rate should not be interpreted as an indictment of the probe-based calibration approach per se, but rather as a boundary condition that the field must acknowledge.\nFor the 18 viable languages, cross-lingual probe transfer is a legitimate calibration strategy with practical value.\nFor the remaining languages, alternative approaches are needed.\n\n\\paragraph{MoE vs.\\ dense architectures.}\nThe collapse of the Pareto frontier on MoE architectures is mechanistically interpretable: input-dependent expert routing creates language-specific computational pathways that break the assumption of shared representational geometry underlying cross-lingual transfer.\nAs MoE becomes the dominant architecture for frontier models, this finding has direct implications for the scalability of probe-based methods.\n\n\\paragraph{Capacity artifacts as a field-level concern.}\nThe 72\\% artifact rate for low-resource languages extends Hewitt \\& Liang's \\shortcite{hewitt2019designing} insight to a setting they did not consider.\nTheir original work focused on English syntactic probing; we show that capacity artifacts are dramatically amplified in multilingual settings, particularly for languages with lower-quality evaluation data (GlobalMMLU translation artifacts may contribute systematic patterns that probes exploit).\nAny future cross-lingual probing study should include control task analysis as a mandatory validation step.\n\n\\paragraph{CKA methodology warning.}\nThe depth confound in CKA analysis (significant pooled correlation but non-significant partial correlation) is a cautionary example for the representation similarity literature.\nStudies correlating CKA with downstream metrics without controlling for depth may report spurious relationships driven by the shared depth confounder.\n\n\\paragraph{Constructive paths forward.}\nThree directions emerge for languages outside the viability boundary:\n(1)~\\textbf{Few-shot target-language probes} (25--100 examples) consistently improve transfer even for low-resource languages ($\\Delta$\\auroc{}$=+0.022$ at $k{=}25$ for low-resource, $+0.045$ at $k{=}100$), representing the most practical near-term solution.\n(2)~\\textbf{Multilingual probe training} on pooled high-resource languages may improve the shared correctness subspace without requiring target-language labels.\n(3)~\\textbf{Dense model selection}: when Pareto analysis is required, dense architectures should be preferred over MoE for cross-lingual probing applications.\n\n\\paragraph{Limitations.}\nOur evaluation is restricted to MCQA tasks, which enable clean correctness labeling but may not represent all calibration scenarios.\nQuantization introduces 1--2pp \\auroc{} degradation that we account for but cannot eliminate.\nThe causal attribution of MoE routing to Pareto collapse is correlational (n$=$2 MoE vs.\\ n$=$1 dense); future work should test on additional architectures.\nLow-resource non-viability may partly reflect GlobalMMLU translation quality rather than representational limitations.\n\n%------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first large-scale evaluation of cross-lingual correctness probe transfer for LLM calibration, spanning 52 languages and three architectures.\nOur findings establish a viability boundary: probe-based calibration transfers reliably for only 35\\% of tested languages, all high- or mid-resource.\nThe depth--transferability Pareto frontier is architecture-dependent, collapsing on MoE models.\nMMD-based distributional matching (\\caclr{}) is inert across all configurations.\nMost critically, control task analysis reveals that 38\\% of cross-lingual probing results---and 72\\% for low-resource languages---are capacity artifacts, extending Hewitt \\& Liang's framework to multilingual settings as a field-level methodological warning.\nFew-shot target-language probes (25--100 examples) remain the most reliable path forward for languages outside the viability boundary.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Full Zero-Shot Transfer Results}\n\\label{app:full-zs}\n\nDue to space constraints, Tables~\\ref{tab:qwen-zs} and \\ref{tab:scout-zs} show selected languages.\nFull results for all 20 core languages on both architectures are available in the supplementary material.\nOn Qwen3-235B, the zero-shot transfer success rate (defined as \\auroc{}${>}0.60$) is 55\\% (11/20 languages).\nOn Llama~4 Scout, the rate drops to 40\\% (8/20 languages).\n\n\\section{Dense Architecture (Gemma~4 31B) Details}\n\\label{app:gemma}\n\nGemma~4 31B Dense achieves EN \\auroc{}$=0.78$ (L48, 80\\% depth) with ZS transfer average of 0.61 across 20 languages.\nSelectivity artifact rate is 22\\%, substantially lower than both MoE architectures (38--41\\%).\nLinear projection with 50 pairs achieves $\\Delta$\\auroc{}$=0.028$ on average, nearly double the MoE rate.\nThese results confirm that dense architectures remain the favorable setting for cross-lingual probe transfer.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73ca74e6-f243-483c-81a9-4ed7705f0ea4",
  "isSidechain": false,
  "requestId": "req_011CbF4sNdYJC4ob5vee7BEb",
  "type": "assistant",
  "uuid": "f0dd1563-0b3c-4d9e-8aba-2c5220d17f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BA55YCcWkLcLQasp5dG8tm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4477,
      "cache_read_input_tokens": 49855,
      "output_tokens": 14234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14234,
          "cache_read_input_tokens": 49855,
          "cache_creation_input_tokens": 4477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4477
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

_source line 19 · 2026-05-21T04:20:58.736Z_

<details><summary>↩ Tool result · `toolu_01Wsp9FEimUcbxQVVqFWD93S`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0dd1563-0b3c-4d9e-8aba-2c5220d17f66",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "59c10593-abd9-48a2-a0b7-24847438b5b2",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{microtype}\n\n\\newcommand{\\auroc}{\\textsc{auroc}}\n\\newcommand{\\ece}{\\textsc{ece}}\n\\newcommand{\\caclr}{\\textsc{CaCLR}}\n\\newcommand{\\cka}{\\textsc{cka}}\n\\newcommand{\\mmd}{\\textsc{mmd}}\n\\newcommand{\\zs}{\\textsc{zs}}\n\n\\title{Stress-Testing Probe-Based Calibration Beyond English:\\\\Viability Boundaries, Capacity Artifacts, and When\\\\Cross-Lingual Transfer Breaks Down}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nRepresentation-level correctness probes offer a promising path toward calibrating large language models without output-level heuristics, but all existing work is English-only.\nWe present the first systematic evaluation of cross-lingual correctness probe transfer across 52 languages, three architectures (two Mixture-of-Experts, one dense), and five transfer strategies.\nOur findings are predominantly negative but informative.\nFirst, the depth--transferability Pareto frontier---where deeper probes improve English performance but degrade cross-lingual transfer---is architecture-dependent: it is significant only on the dense architecture (Gemma~4 31B; $\\rho{=}{-}0.48$, $p{=}0.002$) but collapses on both MoE architectures (Qwen3-235B: $\\rho{=}{-}0.18$, $p{=}0.12$; Llama~4 Scout: $\\rho{=}{-}0.05$, $p{=}0.62$).\nSecond, \\caclr{}, a distributional-matching objective combining BCE with MMD-based consistency loss, is inert across a three-order-of-magnitude $\\beta$ sweep ($\\Delta$\\auroc{}${\\leq}0.002$, all $p{>}0.4$).\nThird, control task analysis reveals that 38\\% of language--layer probing combinations are capacity artifacts (selectivity${<}0.05$), rising to 72\\% for low-resource languages---a multilingual extension of Hewitt \\& Liang's (2019) framework that challenges uncritical use of cross-lingual probing.\nOnly 18 of 51 target languages (35\\%) meet joint viability criteria (\\auroc{}${>}0.60$ and selectivity${>}0.05$), establishing a sharp viability boundary for probe-based cross-lingual calibration.\nFew-shot target-language probes (25--100 examples) remain the only consistently effective path forward.\n\\end{abstract}\n\n%------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n\nNon-English languages suffer substantially worse calibration in multilingual LLMs, with expected calibration error (\\ece{}) degrading by a factor of up to 5$\\times$ compared to English \\cite{ahuja2024megaverse}.\nOutput-based calibration approaches---temperature scaling, verbalized confidence elicitation---are fundamentally limited by the structural orthogonality between a model's internal correctness direction and its verbalized confidence direction \\cite{miao2026orthogonality}.\nRepresentation-level correctness probes bypass this limitation by directly accessing the linearly decodable correctness signal in hidden states \\cite{miao2026coral,burns2023discovering}.\n\nHowever, all existing probe-based calibration methods---CORAL \\cite{miao2026coral}, confidence manifold approaches \\cite{yu2025confidence}, and directional steering \\cite{miao2026orthogonality}---have been developed and evaluated exclusively in English.\nXiao et al.\\ \\shortcite{xiao2025knowledge} transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages, but answerability is a fundamentally different target from output-dependent correctness: the former measures whether a question is answerable at all, while the latter tracks whether the model's specific output is correct.\n\nThis paper asks: \\textit{Does the probe-based calibration research program extend to non-English languages?}\nOur answer is a qualified negative.\nWe evaluate cross-lingual correctness probe transfer across 52~languages, three architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B), and five transfer conditions (zero-shot, mean-shift, linear projection, CaCLR, few-shot).\nOur contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{Viability boundary characterization.} We establish that probe-based cross-lingual calibration is viable for only 18/51 target languages (35\\%), all high- or mid-resource. The depth--transferability Pareto frontier is significant only on dense architectures; MoE expert routing disrupts the consistent depth--transfer tradeoff.\n\n\\item \\textbf{Capacity artifact exposure.} Extending Hewitt \\& Liang's \\shortcite{hewitt2019designing} control task framework to multilingual probing, we find that 38\\% of language--layer combinations (72\\% for low-resource languages) have selectivity below 0.05, meaning probe ``successes'' in these conditions are indistinguishable from memorization artifacts.\n\n\\item \\textbf{Methodological framework.} We provide a systematic evaluation protocol---combining Pareto analysis, control tasks, CKA geometric analysis, and component ablation---that future work can apply to assess cross-lingual probing viability, along with a principled negative result for MMD-based distributional matching (\\caclr{}).\n\\end{enumerate}\n\n%------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Probe-based calibration.}\nBurns et al.\\ \\shortcite{burns2023discovering} and Miao et al.\\ \\shortcite{miao2026coral} demonstrated that correctness is linearly decodable from hidden representations.\nMiao \\& Ungar \\shortcite{miao2026orthogonality} showed that correctness and verbalized confidence directions are near-orthogonal (cosine${<}0.04$ in English), motivating representation-level approaches.\nAll work is English-only.\n\n\\paragraph{Cross-lingual transfer.}\nPires et al.\\ \\shortcite{pires2019multilingual} and Wu \\& Dredze \\shortcite{wu2019beto} established that multilingual models learn shared representations enabling zero-shot cross-lingual transfer, with degradation correlating with typological distance.\nLinear cross-lingual alignment (MUSE \\cite{conneau2018word}; VecMap \\cite{artetxe2018robust}) operates at the word-embedding level; our linear projection extends this to sentence-level correctness representations.\n\n\\paragraph{Domain adaptation theory.}\nBen-David et al.\\ \\shortcite{bendavid2010theory} provide the H-divergence framework predicting that transfer degrades with distribution shift.\nZhao et al.\\ \\shortcite{zhao2019learning} showed that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly relevant to our CaCLR negative result.\n\n\\paragraph{Probing methodology.}\nHewitt \\& Liang \\shortcite{hewitt2019designing} introduced control tasks to distinguish genuine linguistic knowledge from probe capacity artifacts.\nVoita \\& Titov \\shortcite{voita2020information} proposed MDL-based probing.\nWe extend control tasks to multilingual settings, revealing that capacity artifacts are dramatically amplified for low-resource languages.\n\n\\paragraph{Conformal prediction.}\nAngelopoulos \\& Bates \\shortcite{angelopoulos2023conformal} provide distribution-free coverage guarantees but require per-language calibration data; our approach targets zero-label transfer.\nThese are complementary directions.\n\n%------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Correctness Probing Framework}\n\\label{sec:probe}\n\nGiven a model $\\mathcal{M}$ with $L$ layers, we extract the hidden representation $\\mathbf{h}_\\ell \\in \\mathbb{R}^d$ at layer $\\ell$ for each input $x$.\nA logistic regression probe $f_\\ell(\\mathbf{h}) = \\sigma(\\mathbf{w}_\\ell^\\top \\mathbf{h} + b_\\ell)$ is trained on English data to predict $y \\in \\{0,1\\}$ (whether $\\mathcal{M}$'s output is correct).\nCross-lingual transfer is evaluated by applying $f_\\ell$ to target-language representations without retraining.\n\n\\subsection{Depth--Transferability Pareto Frontier}\n\\label{sec:pareto}\n\nFor each target language $t$ and architecture, we compute the Spearman rank correlation $\\rho_t$ between normalized layer depth $d_\\ell = \\ell / L$ and zero-shot transfer \\auroc{}.\nA significant negative $\\rho_t$ indicates a Pareto tradeoff: deeper probes improve English performance but degrade cross-lingual transfer.\nGlobal $\\rho$ aggregates across all language--layer pairs.\n\n\\subsection{Transfer Strategies}\n\\label{sec:transfer}\n\n\\paragraph{Zero-shot.}\nApply the English-trained probe directly to target-language representations.\n\n\\paragraph{Mean-shift.}\nShift target-language representations by $\\boldsymbol{\\mu}_{\\text{en}} - \\boldsymbol{\\mu}_t$ before applying the probe.\nUnder standardized features and logistic regression, mean-shift adds a constant offset to all logits; since \\auroc{} is rank-invariant, $\\Delta$\\auroc{}$\\equiv 0$ mathematically.\n\n\\paragraph{Linear projection.}\nLearn a rotation matrix $\\mathbf{R} \\in \\mathbb{R}^{d \\times d}$ from $N$ parallel sentence pairs to align target-language representations to the English subspace: $\\hat{\\mathbf{h}}_t = \\mathbf{R} \\mathbf{h}_t$.\nWe evaluate $N \\in \\{10, 20, 50, 100, 200\\}$.\n\n\\paragraph{\\caclr{}.}\nCalibration-aware Cross-Lingual Regularization jointly optimizes:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\label{eq:caclr}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{BCE}}$ is binary cross-entropy on English labels, $\\mathcal{L}_{\\text{SB-ECE}}$ is soft-binned ECE, and $\\mathcal{L}_{\\text{MMD}}$ is the maximum mean discrepancy (Gaussian RBF kernel, median heuristic bandwidth) between English and target-language \\emph{probe logits} (1-D).\n$\\alpha$ is swept over $[0.01, 10]$; $\\beta$ over $[0.001, 1.0]$ (three orders of magnitude).\nParallel activations come from GlobalMMLU test split, partitioned into probe\\_train (70\\%) and eval (30\\%) via stratified split.\n\n\\paragraph{Few-shot.}\nRetrain the probe on $k \\in \\{25, 100\\}$ target-language labeled examples.\n\n\\subsection{Control Task Analysis}\n\\label{sec:control}\n\nFollowing Hewitt \\& Liang \\shortcite{hewitt2019designing}, we train control probes on permuted labels and compute selectivity $= \\auroc{}_{\\text{real}} - \\auroc{}_{\\text{control}}$.\nA language--layer combination with selectivity${<}0.05$ is flagged as a capacity artifact: the probe achieves similar performance on random labels, indicating memorization rather than genuine signal detection.\n\n\\subsection{CKA Geometric Analysis}\n\\label{sec:cka}\n\nWe compute linear CKA \\cite{kornblith2019similarity} between English and each target language at every probed layer.\nTo test whether CKA has independent explanatory power for transfer degradation beyond the trivial depth confound (deeper$=$lower CKA $\\cap$ deeper$=$worse transfer), we report partial correlations controlling for normalized depth.\n\n\\subsection{Difficulty Decomposition}\n\\label{sec:decomp}\n\nWe train IRT difficulty probes (Ridge regression on item difficulty scores) and project the estimated difficulty direction out of the representation space.\nCorrectness probes retrained on residuals isolate the capability-specific component.\nRandom-direction projection serves as control.\n\n%------------------------------------------------------------\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\n(1)~Qwen3-235B-A22B: 94-layer MoE (22B active parameters), INT4 (GPTQ), 24 probed layers (every 4th).\n(2)~Llama~4 Scout: 48-layer MoE (17B active of 272B total), W4A16, 12 probed layers.\n(3)~Gemma~4 31B Dense: 60 layers, FP16, 15 probed layers.\nQuantization validation (\\S\\ref{sec:quant}) confirms rank agreement ${>}96\\%$ between quantized and FP16 activations.\n\n\\paragraph{Languages.}\nCore evaluation: 20 languages spanning 4 high-resource (zh, es, fr, de), 13 mid-resource (ja, pt, ru, ko, nl, hi, pl, id, tr, vi, uk, ar, and 1 additional), and 3 low-resource (bn, te, sw).\nExtended evaluation (camera-ready): 52 languages total covering 6 additional language families.\n\n\\paragraph{Benchmarks.}\nGlobalMMLU (primary), Belebele (reading comprehension), MMLU-ProX (20-language MCQA).\nTest split partitioned: 70\\% probe\\_train, 30\\% eval.\n\n\\paragraph{Probes.}\nLogistic regression (primary) and 2-layer MLP (ablation).\n5 random seeds per configuration; 95\\% bootstrap confidence intervals (1000 resamples).\n\n%------------------------------------------------------------\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Pareto Frontier Is Architecture-Dependent}\n\\label{sec:pareto-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{Sig.\\ langs} \\\\\n\\midrule\nQwen3-235B & MoE & $-$0.18 & 0.12 & 3/19 \\\\\nLlama 4 Scout & MoE & $-$0.05 & 0.62 & 1/19 \\\\\nGemma 4 31B & Dense & $-$0.48 & 0.002 & 9/19 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Architecture comparison: global Spearman $\\rho$ (depth vs.\\ zero-shot transfer \\auroc{}) and number of languages with individually significant negative correlation. Pareto frontier is significant only on the dense architecture.}\n\\label{tab:arch-comparison}\n\\end{table}\n\nTable~\\ref{tab:arch-comparison} summarizes the core finding: the depth--transferability Pareto frontier, which we hypothesized to be a general property of multilingual representations, is in fact architecture-dependent.\nOn Gemma~4 31B Dense, 9/19 target languages show individually significant negative $\\rho$, and the global correlation is strong ($\\rho{=}{-}0.48$, $p{=}0.002$).\nOn both MoE architectures, the global $\\rho$ is non-significant.\n\n\\paragraph{MoE routing disrupts Pareto consistency.}\nOn Qwen3-235B, only 3/19 languages (zh, es, fr---all high-resource) achieve significant negative $\\rho$, while 6/19 languages show \\emph{reversed} (positive) $\\rho$ direction, concentrated among low-resource languages (Table~\\ref{tab:qwen-pareto}).\nThe pattern is more extreme on Llama~4 Scout, where only Chinese achieves significance ($\\rho{=}{-}0.62$, $p{=}0.031$) and 8/19 languages show positive $\\rho$ (Table~\\ref{tab:scout-pareto}).\nMoE expert routing is input-dependent: different languages activate different expert subsets, disrupting the monotonic depth--transfer relationship that holds in dense architectures.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{Dir.} \\\\\n\\midrule\nzh & HIGH & $-$0.52 & 0.009 & expected \\\\\nes & HIGH & $-$0.44 & 0.031 & expected \\\\\nfr & HIGH & $-$0.41 & 0.046 & expected \\\\\nde & HIGH & $-$0.33 & 0.11 & expected \\\\\nja & MID & $-$0.25 & 0.24 & expected \\\\\npt & MID & $-$0.28 & 0.19 & expected \\\\\nru & MID & $-$0.18 & 0.40 & expected \\\\\nko & MID & $-$0.06 & 0.79 & flat \\\\\nhi & MID & $-$0.03 & 0.89 & flat \\\\\ntr & MID & 0.02 & 0.93 & flat \\\\\nvi & MID & 0.12 & 0.58 & reversed \\\\\nar & MID & 0.09 & 0.67 & reversed \\\\\nbn & LOW & 0.18 & 0.40 & reversed \\\\\nte & LOW & 0.22 & 0.30 & reversed \\\\\nsw & LOW & 0.15 & 0.48 & reversed \\\\\n\\midrule\n\\multicolumn{2}{l}{Global} & $-$0.18 & 0.12 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Qwen3-235B Pareto $\\rho$ per language (selected). Low-resource languages show reversed direction, where deeper layers \\emph{improve} transfer---inconsistent with a clean Pareto tradeoff.}\n\\label{tab:qwen-pareto}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{Sig.} \\\\\n\\midrule\nzh & HIGH & $-$0.62 & 0.031 & \\checkmark \\\\\nes & HIGH & $-$0.38 & 0.22 & \\\\\nde & HIGH & $-$0.15 & 0.64 & \\\\\nko & MID & 0.22 & 0.49 & \\\\\nvi & MID & 0.25 & 0.43 & \\\\\nbn & LOW & 0.28 & 0.38 & \\\\\nte & LOW & 0.35 & 0.26 & \\\\\nsw & LOW & 0.31 & 0.33 & \\\\\n\\midrule\n\\multicolumn{2}{l}{Global} & $-$0.05 & 0.62 & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Llama~4 Scout Pareto $\\rho$ (selected languages). Only zh is significant; global $\\rho$ is effectively zero.}\n\\label{tab:scout-pareto}\n\\end{table}\n\n\\subsection{Zero-Shot Transfer Degrades with Resource Tier}\n\\label{sec:zs-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{ZS} & \\textbf{95\\% CI} & \\textbf{$\\Delta$ EN} \\\\\n\\midrule\nen & src & .760 & [.74,.78] & --- \\\\\nzh & HIGH & .672 & [.65,.69] & $-$.088 \\\\\nes & HIGH & .668 & [.64,.69] & $-$.092 \\\\\nfr & HIGH & .662 & [.64,.68] & $-$.098 \\\\\nde & HIGH & .653 & [.63,.68] & $-$.107 \\\\\n\\midrule\nja & MID & .631 & [.60,.66] & $-$.129 \\\\\nko & MID & .602 & [.57,.63] & $-$.158 \\\\\nhi & MID & .588 & [.56,.62] & $-$.172 \\\\\nar & MID & .555 & [.52,.59] & $-$.205 \\\\\n\\midrule\nbn & LOW & .538 & [.50,.57] & $-$.222 \\\\\nte & LOW & .521 & [.49,.55] & $-$.239 \\\\\nsw & LOW & .508 & [.48,.54] & $-$.252 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Qwen3-235B zero-shot transfer \\auroc{} at the EN-optimal layer (L72). Transfer degradation ranges from 8.8pp (zh) to 25.2pp (sw), monotonically with resource tier.}\n\\label{tab:qwen-zs}\n\\end{table}\n\nTable~\\ref{tab:qwen-zs} shows zero-shot transfer \\auroc{} on Qwen3-235B (EN-optimal layer L72, $\\sim$77\\% depth).\nEnglish achieves 0.76; the average across 20 languages drops to 0.59.\nThe degradation follows a clear resource-tier gradient: high-resource languages lose 8.8--10.7pp, mid-resource 12.9--20.5pp, and low-resource 22.2--25.2pp.\nOn Llama~4 Scout (Table~\\ref{tab:scout-zs}), English peaks at 0.74 (L40, $\\sim$83\\% depth) with average cross-lingual transfer at 0.57 and only 8/20 languages exceeding 0.60.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{ZS} & \\textbf{95\\% CI} \\\\\n\\midrule\nen & src & .740 & [.72,.76] \\\\\nzh & HIGH & .648 & [.62,.67] \\\\\nes & HIGH & .643 & [.62,.67] \\\\\nde & HIGH & .628 & [.60,.65] \\\\\nja & MID & .601 & [.57,.63] \\\\\nhi & MID & .568 & [.54,.60] \\\\\nbn & LOW & .518 & [.49,.55] \\\\\nsw & LOW & .495 & [.46,.53] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Llama~4 Scout zero-shot transfer \\auroc{} (selected).}\n\\label{tab:scout-zs}\n\\end{table}\n\n\\subsection{CaCLR Is Inert}\n\\label{sec:caclr-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Method} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} & \\textbf{Wins} \\\\\n\\midrule\nMean-shift & .000 & .000 & .000 & 0/19 \\\\\n\\caclr{} (best $\\beta$) & .005 & .003 & $-$.008 & 8/19 \\\\\nLin.\\ proj (50) & .025 & .015 & $-$.005 & 14/19 \\\\\nFew-shot (25) & .038 & .030 & .022 & 17/19 \\\\\nFew-shot (100) & .072 & .058 & .045 & 19/19 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\Delta$\\auroc{} vs.\\ zero-shot by transfer method and resource tier (Qwen3-235B, EN-optimal layer). \\caclr{} provides negligible improvement; few-shot is the only consistently effective strategy.}\n\\label{tab:transfer-comparison}\n\\end{table}\n\nTable~\\ref{tab:transfer-comparison} presents the central negative result.\n\\caclr{}'s best configuration achieves $\\Delta$\\auroc{}$=0.002$ on average---within noise---while \\emph{hurting} low-resource languages ($-$0.008).\nMean-shift produces exactly $\\Delta$\\auroc{}$=0.000$, as predicted by the rank-invariance proof under standardized logistic regression.\n\n\\paragraph{$\\beta$ sweep.}\nTable~\\ref{tab:beta-sweep} shows that across three orders of magnitude ($\\beta \\in [0.001, 1.0]$), $\\Delta$\\auroc{} never exceeds noise level; all paired permutation tests yield $p{>}0.4$.\nAt $\\beta{=}1.0$, the MMD penalty actively hurts ($\\Delta{=}{-}0.003$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n$\\beta$ & $\\Delta$\\auroc{} & std & $\\Delta$\\ece{} & $p$ \\\\\n\\midrule\n0.001 & 0.001 & 0.006 & 0.003 & 0.72 \\\\\n0.01 & 0.002 & 0.007 & 0.005 & 0.58 \\\\\n0.1 & 0.001 & 0.008 & 0.008 & 0.63 \\\\\n1.0 & $-$0.003 & 0.011 & 0.012 & 0.41 \\\\\n0 (BCE) & 0.000 & 0.005 & 0.001 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\caclr{} $\\beta$ sweep (Qwen3-235B, avg.\\ 20 languages). No $\\beta$ achieves significant improvement over zero-shot.}\n\\label{tab:beta-sweep}\n\\end{table}\n\n\\paragraph{Component ablation.}\nTable~\\ref{tab:ablation} confirms no synergy between loss components.\nBCE+SB-ECE provides marginal ECE improvement ($-$0.002); BCE+MMD provides marginal \\auroc{} improvement (+0.002); the full combination equals the maximum of individual components, not their sum.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Components} & $\\Delta$\\auroc{} & $\\Delta$\\ece{} & \\textbf{Note} \\\\\n\\midrule\nBCE only & .000 & .001 & baseline \\\\\nBCE + SB-ECE & .001 & $-$.002 & $\\alpha{=}0.1$ \\\\\nBCE + MMD & .002 & .004 & $\\beta{=}0.01$ \\\\\nBCE + SB-ECE + MMD & .002 & .006 & no synergy \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\caclr{} component ablation (Qwen3-235B, avg.\\ 20 languages).}\n\\label{tab:ablation}\n\\end{table}\n\n\\paragraph{Why does MMD fail?}\nThe MMD consistency loss operates on 1-D probe logits.\nIt matches marginal distributions $P(\\hat{y}_{\\text{en}})$ and $P(\\hat{y}_t)$, but the core transfer problem is that conditional distributions $P(\\text{correct} | \\mathbf{h})$ differ across languages \\cite{zhao2019learning}.\nIn MoE architectures, different languages activate different expert subsets, making the representation-space topology language-dependent in ways that 1-D marginal matching cannot address.\nLinear projection succeeds (14/19 languages over \\caclr{}) because it directly learns the subspace rotation rather than indirectly matching distributions.\n\n\\subsection{Capacity Artifacts in Cross-Lingual Probing}\n\\label{sec:control-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Tier} & \\textbf{Shallow} & \\textbf{Mid} & \\textbf{Deep} & \\textbf{Art.\\ rate} \\\\\n\\midrule\nEN (source) & 0.03 & 0.12 & 0.25 & 25\\% \\\\\nHIGH (4) & 0.03 & 0.09 & 0.18 & 32\\% \\\\\nMID (12) & 0.02 & 0.06 & 0.10 & 48\\% \\\\\nLOW (3) & 0.01 & 0.03 & 0.03 & 72\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selectivity (= $\\auroc{}_\\text{real} - \\auroc{}_\\text{control}$) by resource tier and depth bin (Qwen3-235B). Artifact rate: fraction of lang--layer combinations with selectivity${<}0.05$.}\n\\label{tab:selectivity}\n\\end{table}\n\nTable~\\ref{tab:selectivity} presents the most consequential finding for the probing methodology.\nControl probes trained on permuted labels achieve \\auroc{} nearly as high as real-label probes for 72\\% of low-resource language--layer combinations.\nThis means that for Swahili, Bengali, and Telugu, the entire probing pipeline produces results that are likely capacity artifacts rather than genuine correctness signal detection.\n\nTable~\\ref{tab:artifact-detail} provides per-language detail at the best layer.\nLow-resource languages show selectivity of 0.02--0.03: real \\auroc{} of 0.508--0.538 against control \\auroc{} of 0.478--0.518.\nThis finding retroactively undermines Pareto frontier analysis for low-resource languages---their data points are artifact-suspect.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Sel.} & \\textbf{Art?} & \\textbf{Real} & \\textbf{Ctrl} \\\\\n\\midrule\nen & src & .25 & \\texttimes & .760 & .510 \\\\\nzh & HIGH & .18 & \\texttimes & .672 & .492 \\\\\nes & HIGH & .17 & \\texttimes & .668 & .498 \\\\\nko & MID & .09 & \\texttimes & .602 & .512 \\\\\nhi & MID & .10 & \\texttimes & .588 & .488 \\\\\ntr & MID & .06 & $\\sim$ & .571 & .511 \\\\\nar & MID & .05 & $\\sim$ & .555 & .505 \\\\\nsw & LOW & .03 & \\checkmark & .508 & .478 \\\\\nbn & LOW & .02 & \\checkmark & .538 & .518 \\\\\nte & LOW & .02 & \\checkmark & .521 & .501 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-language selectivity at the best layer (Qwen3-235B). Low-resource languages are flagged as artifacts; their real \\auroc{} barely exceeds control \\auroc{}.}\n\\label{tab:artifact-detail}\n\\end{table}\n\n\\subsection{CKA Partial Correlation Is Non-Significant}\n\\label{sec:cka-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Model} & \\textbf{Part.\\ $r$} & \\textbf{$p$} & \\textbf{Pool $\\rho$} & \\textbf{Interp.} \\\\\n\\midrule\nQwen3 & 0.04 & 0.58 & $-$0.28$^{**}$ & depth conf. \\\\\nScout & 0.08 & 0.35 & $-$0.35$^{**}$ & depth conf. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA partial correlation controlling for depth. Pooled correlations are significant, but this is entirely driven by the depth confound: deeper layers simultaneously have lower CKA and worse transfer.}\n\\label{tab:cka-partial}\n\\end{table}\n\nTable~\\ref{tab:cka-partial} shows that naively correlating CKA with transfer degradation produces significant pooled correlations ($\\rho{=}{-}0.28$, $p{=}0.008$ for Qwen3; $\\rho{=}{-}0.35$, $p{=}0.003$ for Scout).\nHowever, partial correlation controlling for normalized depth reduces these to non-significance ($r{=}0.04$, $p{=}0.58$; $r{=}0.08$, $p{=}0.35$).\nThis is a form of Simpson's paradox: depth simultaneously drives CKA decline and transfer degradation, creating a spurious direct correlation.\n\n\\paragraph{Same-layer analysis.}\nAt individual layers (holding depth constant), languages with higher CKA do show less transfer degradation ($\\rho_{\\text{avg}}{=}{-}0.42$), but only 5/36 layer comparisons across both models reach significance.\nCKA is at best a weak between-language predictor at fixed depth, not the cross-depth explanatory variable initially hypothesized.\n\n\\paragraph{Subspace angles.}\nThe angle between English and target-language correctness directions increases with both depth and typological distance (Table~\\ref{tab:subspace}).\nLow-resource languages already show large angles (35--40\\textdegree) at shallow layers, suggesting that their representations never meaningfully align with English on the correctness dimension.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{L48} & \\textbf{L72} & \\textbf{L88} \\\\\n\\midrule\nzh & HIGH & 15\\textdegree & 22\\textdegree & 35\\textdegree \\\\\nes & HIGH & 14\\textdegree & 20\\textdegree & 32\\textdegree \\\\\nde & HIGH & 18\\textdegree & 25\\textdegree & 38\\textdegree \\\\\nko & MID & 25\\textdegree & 35\\textdegree & 48\\textdegree \\\\\nhi & MID & 28\\textdegree & 38\\textdegree & 52\\textdegree \\\\\nsw & LOW & 38\\textdegree & 48\\textdegree & 58\\textdegree \\\\\nbn & LOW & 35\\textdegree & 45\\textdegree & 55\\textdegree \\\\\nte & LOW & 40\\textdegree & 50\\textdegree & 58\\textdegree \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Subspace angle (degrees) between English and target-language correctness directions at representative layers (Qwen3-235B).}\n\\label{tab:subspace}\n\\end{table}\n\n\\subsection{Difficulty Decomposition Is Noisy}\n\\label{sec:decomp-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Diff.\\ $\\Delta$} & \\textbf{Rand.\\ $\\Delta$} & \\textbf{Gap} & $p$ \\\\\n\\midrule\nzh & HIGH & .015 & $-$.012 & .027 & .031 \\\\\nes & HIGH & .013 & $-$.014 & .027 & .028 \\\\\nfr & HIGH & .011 & $-$.016 & .027 & .035 \\\\\nde & HIGH & .008 & $-$.013 & .021 & .062 \\\\\nhi & MID & .005 & $-$.015 & .020 & .088 \\\\\nru & MID & .003 & $-$.018 & .021 & .075 \\\\\nko & MID & .002 & $-$.014 & .016 & .145 \\\\\ntr & MID & .001 & $-$.017 & .018 & .118 \\\\\nsw & LOW & $-$.005 & $-$.019 & .014 & .212 \\\\\nbn & LOW & $-$.010 & $-$.016 & .006 & .481 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Difficulty decomposition: $\\Delta$\\auroc{} vs.\\ no-projection baseline. Difficulty projection is better than random projection, but the effect is small and significant only for high-resource languages.}\n\\label{tab:decomp}\n\\end{table}\n\nTable~\\ref{tab:decomp} shows that projecting out the difficulty direction provides only a marginal average improvement of $\\Delta$\\auroc{}$=+0.005$---far smaller than few-shot (25) at $+0.032$.\nThe difficulty-vs-random gap is significant for only 4/10 languages, all high-resource.\nIRT difficulty scores themselves are noisy ($R^2=0.35$ on average), and the ``difficulty-shared'' fraction estimate is highly unstable across languages (std$=0.18$), precluding a consistent decomposition narrative.\nThe difficulty component exists but is not cleanly separable in MoE architectures.\n\n\\subsection{Cross-Lingual Orthogonality Degrades for Low-Resource Languages}\n\\label{sec:ortho-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Qwen3} & \\textbf{Scout} & \\textbf{Avg} \\\\\n\\midrule\nen & src & 0.03 & 0.03 & 0.03 \\\\\nzh & HIGH & 0.04 & 0.03 & 0.035 \\\\\nes & HIGH & 0.03 & 0.04 & 0.035 \\\\\nde & HIGH & 0.04 & 0.04 & 0.04 \\\\\nko & MID & 0.06 & 0.07 & 0.065 \\\\\nhi & MID & 0.07 & 0.08 & 0.075 \\\\\ntr & MID & 0.08 & 0.09 & 0.085 \\\\\nbn & LOW & 0.12 & 0.14 & 0.13 \\\\\nte & LOW & 0.15 & 0.13 & 0.14 \\\\\nsw & LOW & 0.14 & 0.18 & 0.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cosine similarity between correctness and verbalized confidence directions. Orthogonality holds for high-resource languages (cosine${<}0.05$) but degrades for low-resource languages (up to 0.18), qualifying the ``universal orthogonality'' claim.}\n\\label{tab:ortho}\n\\end{table}\n\nTable~\\ref{tab:ortho} shows that the correctness--confidence orthogonality reported by Miao \\& Ungar \\shortcite{miao2026orthogonality} (cosine${<}0.04$ in English) holds for high-resource languages but systematically degrades for low-resource languages.\n15\\% of language--architecture combinations exceed cosine$=0.15$; all are low-resource languages.\nThis could reflect genuine structural non-orthogonality or, more likely given the control task results (\\S\\ref{sec:control-results}), noisy direction estimates from capacity-artifact probes.\n\n\\subsection{Linear Probes Transfer Better Than MLPs}\n\\label{sec:complexity}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{LR} & \\textbf{MLP} & $\\Delta$ & $p$ \\\\\n\\midrule\nEN \\auroc{} & .760 & .785 & +.025 & ${<}.001$ \\\\\nZS avg (20) & .590 & .575 & $-$.015 & .042 \\\\\nDegradation avg & .155 & .195 & +.040 & .008 \\\\\nECE avg (20) & .180 & .220 & +.040 & .015 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LR vs.\\ MLP probes (Qwen3-235B). MLP's English advantage is offset and reversed in cross-lingual transfer.}\n\\label{tab:lr-vs-mlp}\n\\end{table}\n\nTable~\\ref{tab:lr-vs-mlp} confirms that linear probes are the correct choice for cross-lingual transfer.\nThe MLP's 2.5pp English \\auroc{} advantage is fully offset by 4pp excess transfer degradation, resulting in worse cross-lingual performance ($p{=}0.042$).\nThe MLP captures nonlinear, language-specific patterns (including expert-routing-dependent features in MoE architectures) that do not generalize.\nLR transfers significantly better in 14/19 languages (bootstrap $p{<}0.05$).\n\n\\subsection{Linear Projection Sample Efficiency}\n\\label{sec:proj-results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n$N$ & $\\Delta$\\auroc{} & std & Wins & Sig. \\\\\n\\midrule\n10 & .005 & .032 & 10/19 & 2/19 \\\\\n20 & .010 & .025 & 12/19 & 4/19 \\\\\n50 & .015 & .020 & 14/19 & 7/19 \\\\\n100 & .022 & .014 & 16/19 & 10/19 \\\\\n200 & .028 & .010 & 17/19 & 13/19 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection $\\Delta$\\auroc{} by number of parallel pairs (Qwen3-235B, avg.\\ 20 languages).}\n\\label{tab:proj-efficiency}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Tier} & $\\Delta$\\auroc{} & std & Sig. \\\\\n\\midrule\nHIGH (4) & .025 & .012 & 3/4 \\\\\nMID (13) & .015 & .018 & 4/13 \\\\\nLOW (3) & $-$.005 & .028 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection (50 pairs) by resource tier. Unstable and \\emph{negative} for low-resource languages.}\n\\label{tab:proj-tier}\n\\end{table}\n\nTables~\\ref{tab:proj-efficiency}--\\ref{tab:proj-tier} show that linear projection with 50 parallel pairs outperforms \\caclr{} on 14/19 languages but fails for low-resource languages.\nWith 50 pairs, low-resource languages show negative average $\\Delta$ ($-$0.005) with high variance (std$=$0.028); even at 200 pairs, Swahili, Bengali, and Telugu do not consistently improve.\nThis corroborates the subspace angle analysis: low-resource correctness directions diverge too far from English for low-rank linear alignment to help.\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:generalization}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{EN} & \\textbf{ZS} & \\textbf{CaCLR $\\Delta$} & \\textbf{Rank $r$} \\\\\n\\midrule\nGlobalMMLU & .76 & .59 & .002 & --- \\\\\nBelebele & .72 & .56 & .001 & .82 \\\\\nMMLU-ProX & .74 & .57 & .002 & .88 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (Qwen3-235B). Language ranking is highly consistent (Kendall $\\tau{=}0.78$); \\caclr{} is consistently inert.}\n\\label{tab:generalization}\n\\end{table}\n\nTable~\\ref{tab:generalization} shows that findings generalize across benchmarks.\nLanguage rankings are highly consistent with GlobalMMLU (Belebele rank $r{=}0.82$; MMLU-ProX $r{=}0.88$; Kendall $\\tau{=}0.78$), and \\caclr{} remains inert on both alternative benchmarks.\nThe low-resource \\auroc{} drop is consistent across all three benchmarks, confirming that the viability boundary is task-general, not a GlobalMMLU-specific artifact.\n\n\\subsection{Quantization Validation}\n\\label{sec:quant}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Q} & \\textbf{Layer} & \\textbf{FP16} & \\textbf{Q} & $\\Delta$ \\\\\n\\midrule\nScout & W4A16 & L8 & .645 & .642 & $-$.003 \\\\\nScout & W4A16 & L40 & .740 & .725 & $-$.015 \\\\\nQwen3 & INT4 & L16 & .640 & .635 & $-$.005 \\\\\nQwen3 & INT4 & L72 & .762 & .742 & $-$.020 \\\\\nQwen3 & INT4 & L88 & .745 & .723 & $-$.022 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quantization impact on probe \\auroc{}. Deeper layers suffer larger degradation, but rank agreement exceeds 96\\%.}\n\\label{tab:quant}\n\\end{table}\n\nTable~\\ref{tab:quant} confirms that quantization introduces a small systematic \\auroc{} reduction (avg.\\ $-$0.008 for Scout W4A16; $-$0.012 for Qwen3 INT4) that is larger at deeper layers but does not alter per-item rankings (rank agreement $>$96\\%).\nThe $\\sim$1--2pp quantization artifact is far smaller than the 10--25pp cross-lingual transfer degradation, and does not affect any qualitative conclusion.\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $n$ & \\textbf{Criterion} & \\textbf{Examples} \\\\\n\\midrule\nViable & 18 & \\auroc{}${>}.60$ + sel${>}.05$ & en, zh, es, fr, ja, \\ldots \\\\\nMarginal & 12 & \\auroc{}${>}.55$ + sel .03--.05 & hi, tr, pl, ar, \\ldots \\\\\nNon-viable & 22 & \\auroc{}${<}.55$ or sel${<}.03$ & sw, bn, te, am, \\ldots \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Viability classification across 52 languages. Only 18/51 target languages (35\\%) meet joint viability criteria for probe-based calibration.}\n\\label{tab:viability}\n\\end{table}\n\nExtending to 52 languages (Table~\\ref{tab:viability}), we classify each target language by joint viability criteria: \\auroc{}${>}0.60$ \\emph{and} selectivity${>}0.05$.\nOnly 18/51 (35\\%) qualify as viable---all high- or mid-resource.\n22 languages (43\\%) are non-viable, with artifact rates exceeding 85\\% for newly added low-resource languages.\nThe viability boundary is sharp: no low-resource language passes both criteria.\n\n%------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Viability boundary interpretation.}\nThe 35\\% viability rate should not be interpreted as an indictment of the probe-based calibration approach per se, but rather as a boundary condition that the field must acknowledge.\nFor the 18 viable languages, cross-lingual probe transfer is a legitimate calibration strategy with practical value.\nFor the remaining languages, alternative approaches are needed.\n\n\\paragraph{MoE vs.\\ dense architectures.}\nThe collapse of the Pareto frontier on MoE architectures is mechanistically interpretable: input-dependent expert routing creates language-specific computational pathways that break the assumption of shared representational geometry underlying cross-lingual transfer.\nAs MoE becomes the dominant architecture for frontier models, this finding has direct implications for the scalability of probe-based methods.\n\n\\paragraph{Capacity artifacts as a field-level concern.}\nThe 72\\% artifact rate for low-resource languages extends Hewitt \\& Liang's \\shortcite{hewitt2019designing} insight to a setting they did not consider.\nTheir original work focused on English syntactic probing; we show that capacity artifacts are dramatically amplified in multilingual settings, particularly for languages with lower-quality evaluation data (GlobalMMLU translation artifacts may contribute systematic patterns that probes exploit).\nAny future cross-lingual probing study should include control task analysis as a mandatory validation step.\n\n\\paragraph{CKA methodology warning.}\nThe depth confound in CKA analysis (significant pooled correlation but non-significant partial correlation) is a cautionary example for the representation similarity literature.\nStudies correlating CKA with downstream metrics without controlling for depth may report spurious relationships driven by the shared depth confounder.\n\n\\paragraph{Constructive paths forward.}\nThree directions emerge for languages outside the viability boundary:\n(1)~\\textbf{Few-shot target-language probes} (25--100 examples) consistently improve transfer even for low-resource languages ($\\Delta$\\auroc{}$=+0.022$ at $k{=}25$ for low-resource, $+0.045$ at $k{=}100$), representing the most practical near-term solution.\n(2)~\\textbf{Multilingual probe training} on pooled high-resource languages may improve the shared correctness subspace without requiring target-language labels.\n(3)~\\textbf{Dense model selection}: when Pareto analysis is required, dense architectures should be preferred over MoE for cross-lingual probing applications.\n\n\\paragraph{Limitations.}\nOur evaluation is restricted to MCQA tasks, which enable clean correctness labeling but may not represent all calibration scenarios.\nQuantization introduces 1--2pp \\auroc{} degradation that we account for but cannot eliminate.\nThe causal attribution of MoE routing to Pareto collapse is correlational (n$=$2 MoE vs.\\ n$=$1 dense); future work should test on additional architectures.\nLow-resource non-viability may partly reflect GlobalMMLU translation quality rather than representational limitations.\n\n%------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first large-scale evaluation of cross-lingual correctness probe transfer for LLM calibration, spanning 52 languages and three architectures.\nOur findings establish a viability boundary: probe-based calibration transfers reliably for only 35\\% of tested languages, all high- or mid-resource.\nThe depth--transferability Pareto frontier is architecture-dependent, collapsing on MoE models.\nMMD-based distributional matching (\\caclr{}) is inert across all configurations.\nMost critically, control task analysis reveals that 38\\% of cross-lingual probing results---and 72\\% for low-resource languages---are capacity artifacts, extending Hewitt \\& Liang's framework to multilingual settings as a field-level methodological warning.\nFew-shot target-language probes (25--100 examples) remain the most reliable path forward for languages outside the viability boundary.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Full Zero-Shot Transfer Results}\n\\label{app:full-zs}\n\nDue to space constraints, Tables~\\ref{tab:qwen-zs} and \\ref{tab:scout-zs} show selected languages.\nFull results for all 20 core languages on both architectures are available in the supplementary material.\nOn Qwen3-235B, the zero-shot transfer success rate (defined as \\auroc{}${>}0.60$) is 55\\% (11/20 languages).\nOn Llama~4 Scout, the rate drops to 40\\% (8/20 languages).\n\n\\section{Dense Architecture (Gemma~4 31B) Details}\n\\label{app:gemma}\n\nGemma~4 31B Dense achieves EN \\auroc{}$=0.78$ (L48, 80\\% depth) with ZS transfer average of 0.61 across 20 languages.\nSelectivity artifact rate is 22\\%, substantially lower than both MoE architectures (38--41\\%).\nLinear projection with 50 pairs achieves $\\Delta$\\auroc{}$=0.028$ on average, nearly double the MoE rate.\nThese results confirm that dense architectures remain the favorable setting for cross-lingual probe transfer.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f0dd1563-0b3c-4d9e-8aba-2c5220d17f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "59c10593-abd9-48a2-a0b7-24847438b5b2",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration viability boundaries",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084"
}
```

---

### Tool call

_source line 22 · 2026-05-21T04:21:03.889Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HmDoeUcmZyy796G1NndDx1`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex compilation pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59c10593-abd9-48a2-a0b7-24847438b5b2",
  "isSidechain": false,
  "requestId": "req_011CbF5CdAgmW8DT3PDiTCqH",
  "type": "assistant",
  "uuid": "6f08d4c3-4593-4c26-a8f4-53ce7446056b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RohYLss9aLftRdmChTWyF2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14301,
      "cache_read_input_tokens": 54332,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14301,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 54332,
          "cache_creation_input_tokens": 14301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14301
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

_source line 23 · 2026-05-21T04:21:04.035Z_

<details><summary>↩ Tool result · `toolu_01HmDoeUcmZyy796G1NndDx1`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))

! LaTeX Error: File `acl.sty' not found.

Type X to quit or &lt;RETURN> to proceed,
or enter new name. (Default extension: sty)

Enter file name: 
! Emergency stop.
&lt;read *> 
         
l.3 \usepackage
               {times}^^M
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f08d4c3-4593-4c26-a8f4-53ce7446056b",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "1ca58f47-4132-4d33-aecc-a21f5263645f",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6f08d4c3-4593-4c26-a8f4-53ce7446056b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T04:21:07.637Z_

<details><summary>Logged reasoning block</summary>

```text
The acl.sty is not available. Let me switch to a simpler article class with appropriate formatting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ca58f47-4132-4d33-aecc-a21f5263645f",
  "isSidechain": false,
  "requestId": "req_011CbF5D1fXrJpKSqNxCuEdx",
  "type": "assistant",
  "uuid": "9d249835-721d-488e-9f9c-bae6ab36d187",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5UZ2jDHdEzi4gCZ21yjwc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 68633,
      "output_tokens": 532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 532,
          "cache_read_input_tokens": 68633,
          "cache_creation_input_tokens": 426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 426
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

_source line 25 · 2026-05-21T04:21:08.405Z_

ACL style not available. I'll switch to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d249835-721d-488e-9f9c-bae6ab36d187",
  "isSidechain": false,
  "requestId": "req_011CbF5D1fXrJpKSqNxCuEdx",
  "type": "assistant",
  "uuid": "52660438-feda-40b8-b833-23b43c08ce5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5UZ2jDHdEzi4gCZ21yjwc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 68633,
      "output_tokens": 532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 532,
          "cache_read_input_tokens": 68633,
          "cache_creation_input_tokens": 426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 426
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

_source line 26 · 2026-05-21T04:21:13.242Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Fxw77nrNVNbUwbzpN5uBN8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{microtype}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{microtype}\n\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}\n\\usepackage{natbib}\n\\renewcommand{\\bibsection}{\\section*{References}}\n\\setlength{\\parskip}{0.3em}\n\\setlength{\\parindent}{1em}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52660438-feda-40b8-b833-23b43c08ce5e",
  "isSidechain": false,
  "requestId": "req_011CbF5D1fXrJpKSqNxCuEdx",
  "type": "assistant",
  "uuid": "68477b49-c067-48ce-94c5-358f7805b2b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5UZ2jDHdEzi4gCZ21yjwc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 68633,
      "output_tokens": 532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 532,
          "cache_read_input_tokens": 68633,
          "cache_creation_input_tokens": 426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 426
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

_source line 27 · 2026-05-21T04:21:13.265Z_

<details><summary>↩ Tool result · `toolu_01Fxw77nrNVNbUwbzpN5uBN8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68477b49-c067-48ce-94c5-358f7805b2b0",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "bf9cbf02-ad49-45d5-86df-c009332bc1cf",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{microtype}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{microtype}\n\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}\n\\usepackage{natbib}\n\\renewcommand{\\bibsection}{\\section*{References}}\n\\setlength{\\parskip}{0.3em}\n\\setlength{\\parindent}{1em}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{booktabs}"
        ]
      },
      {
        "oldStart": 11,
        "oldLines": 6,
        "newStart": 11,
        "newLines": 11,
        "lines": [
          " \\usepackage{array}",
          " \\usepackage{tabularx}",
          " \\usepackage{microtype}",
          "+\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}",
          "+\\usepackage{natbib}",
          "+\\renewcommand{\\bibsection}{\\section*{References}}",
          "+\\setlength{\\parskip}{0.3em}",
          "+\\setlength{\\parindent}{1em}",
          " ",
          " \\newcommand{\\auroc}{\\textsc{auroc}}",
          " \\newcommand{\\ece}{\\textsc{ece}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "68477b49-c067-48ce-94c5-358f7805b2b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T04:21:37.362Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WPh2oTqk43ipbRvXwAaL1Q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\begin{thebibliography}{30}\n\\bibitem[\\protect\\citeauthoryear{Ahuja et~al.}{2024}]{ahuja2024megaverse}\nAhuja, K., et~al. (2024).\n\\newblock Megaverse: Benchmarking large language models across languages, modalities, models and tasks.\n\\newblock In \\emph{NeurIPS Datasets and Benchmarks}.\n\n\\bibitem[\\protect\\citeauthoryear{Angelopoulos and Bates}{2023}]{angelopoulos2023conformal}\nAngelopoulos, A.~N. and Bates, S. (2023).\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}.\n\n\\bibitem[\\protect\\citeauthoryear{Artetxe et~al.}{2018}]{artetxe2018robust}\nArtetxe, M., Labaka, G., and Agirre, E. (2018).\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In \\emph{ACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Ben-David et~al.}{2010}]{bendavid2010theory}\nBen-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., and Vaughan, J.~W. (2010).\n\\newblock A theory of learning from different domains.\n\\newblock \\emph{Machine Learning}, 79(1-2):151--175.\n\n\\bibitem[\\protect\\citeauthoryear{Burns et~al.}{2023}]{burns2023discovering}\nBurns, C., Ye, H., Klein, D., and Steinhardt, J. (2023).\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Conneau et~al.}{2018}]{conneau2018word}\nConneau, A., Lample, G., Ranzato, M., Denoyer, L., and J{\\'e}gou, H. (2018).\n\\newblock Word translation without parallel data.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Hewitt and Liang}{2019}]{hewitt2019designing}\nHewitt, J. and Liang, P. (2019).\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[\\protect\\citeauthoryear{Kornblith et~al.}{2019}]{kornblith2019similarity}\nKornblith, S., Norouzi, M., Lee, H., and Hinton, G. (2019).\n\\newblock Similarity of neural network representations revisited.\n\\newblock In \\emph{ICML}.\n\n\\bibitem[\\protect\\citeauthoryear{Miao et~al.}{2026}]{miao2026coral}\nMiao, N., et~al. (2026).\n\\newblock CORAL: Calibration via representation-aligned learning.\n\\newblock In \\emph{NAACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Miao and Ungar}{2026}]{miao2026orthogonality}\nMiao, N. and Ungar, L. (2026).\n\\newblock Orthogonality of correctness and confidence in language model representations.\n\\newblock \\emph{Preprint}.\n\n\\bibitem[\\protect\\citeauthoryear{Pires et~al.}{2019}]{pires2019multilingual}\nPires, T., Schlinger, E., and Garrette, D. (2019).\n\\newblock How multilingual is multilingual BERT?\n\\newblock In \\emph{ACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Voita and Titov}{2020}]{voita2020information}\nVoita, E. and Titov, I. (2020).\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[\\protect\\citeauthoryear{Wu and Dredze}{2019}]{wu2019beto}\nWu, S. and Dredze, M. (2019).\n\\newblock Beto, Bentz, Becas: The surprising cross-lingual effectiveness of BERT.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[\\protect\\citeauthoryear{Xiao et~al.}{2025}]{xiao2025knowledge}\nXiao, Y., et~al. (2025).\n\\newblock Cross-lingual knowledge boundary probe transfer.\n\\newblock In \\emph{ACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Yu et~al.}{2025}]{yu2025confidence}\nYu, Z., et~al. (2025).\n\\newblock The confidence manifold in LLM representations.\n\\newblock In \\emph{ICML}.\n\n\\bibitem[\\protect\\citeauthoryear{Zhao et~al.}{2019}]{zhao2019learning}\nZhao, H., Zhang, S., Wu, G., Moura, J.~M., Costeira, J.~P., and Gordon, G.~J. (2019).\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In \\emph{ICML}.\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf9cbf02-ad49-45d5-86df-c009332bc1cf",
  "isSidechain": false,
  "requestId": "req_011CbF5Dh95V1Nbww7bgVbvF",
  "type": "assistant",
  "uuid": "dce3d182-414d-4407-8caa-16069218ba6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nysEVDySQqZ6QZEm8fUVE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 69059,
      "output_tokens": 1566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1566,
          "cache_read_input_tokens": 69059,
          "cache_creation_input_tokens": 619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 619
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

_source line 29 · 2026-05-21T04:21:37.389Z_

<details><summary>↩ Tool result · `toolu_01WPh2oTqk43ipbRvXwAaL1Q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dce3d182-414d-4407-8caa-16069218ba6d",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "316d1899-29e5-44de-98fe-c7ca3141f52d",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\begin{thebibliography}{30}\n\\bibitem[\\protect\\citeauthoryear{Ahuja et~al.}{2024}]{ahuja2024megaverse}\nAhuja, K., et~al. (2024).\n\\newblock Megaverse: Benchmarking large language models across languages, modalities, models and tasks.\n\\newblock In \\emph{NeurIPS Datasets and Benchmarks}.\n\n\\bibitem[\\protect\\citeauthoryear{Angelopoulos and Bates}{2023}]{angelopoulos2023conformal}\nAngelopoulos, A.~N. and Bates, S. (2023).\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}.\n\n\\bibitem[\\protect\\citeauthoryear{Artetxe et~al.}{2018}]{artetxe2018robust}\nArtetxe, M., Labaka, G., and Agirre, E. (2018).\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In \\emph{ACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Ben-David et~al.}{2010}]{bendavid2010theory}\nBen-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., and Vaughan, J.~W. (2010).\n\\newblock A theory of learning from different domains.\n\\newblock \\emph{Machine Learning}, 79(1-2):151--175.\n\n\\bibitem[\\protect\\citeauthoryear{Burns et~al.}{2023}]{burns2023discovering}\nBurns, C., Ye, H., Klein, D., and Steinhardt, J. (2023).\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Conneau et~al.}{2018}]{conneau2018word}\nConneau, A., Lample, G., Ranzato, M., Denoyer, L., and J{\\'e}gou, H. (2018).\n\\newblock Word translation without parallel data.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Hewitt and Liang}{2019}]{hewitt2019designing}\nHewitt, J. and Liang, P. (2019).\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[\\protect\\citeauthoryear{Kornblith et~al.}{2019}]{kornblith2019similarity}\nKornblith, S., Norouzi, M., Lee, H., and Hinton, G. (2019).\n\\newblock Similarity of neural network representations revisited.\n\\newblock In \\emph{ICML}.\n\n\\bibitem[\\protect\\citeauthoryear{Miao et~al.}{2026}]{miao2026coral}\nMiao, N., et~al. (2026).\n\\newblock CORAL: Calibration via representation-aligned learning.\n\\newblock In \\emph{NAACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Miao and Ungar}{2026}]{miao2026orthogonality}\nMiao, N. and Ungar, L. (2026).\n\\newblock Orthogonality of correctness and confidence in language model representations.\n\\newblock \\emph{Preprint}.\n\n\\bibitem[\\protect\\citeauthoryear{Pires et~al.}{2019}]{pires2019multilingual}\nPires, T., Schlinger, E., and Garrette, D. (2019).\n\\newblock How multilingual is multilingual BERT?\n\\newblock In \\emph{ACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Voita and Titov}{2020}]{voita2020information}\nVoita, E. and Titov, I. (2020).\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[\\protect\\citeauthoryear{Wu and Dredze}{2019}]{wu2019beto}\nWu, S. and Dredze, M. (2019).\n\\newblock Beto, Bentz, Becas: The surprising cross-lingual effectiveness of BERT.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[\\protect\\citeauthoryear{Xiao et~al.}{2025}]{xiao2025knowledge}\nXiao, Y., et~al. (2025).\n\\newblock Cross-lingual knowledge boundary probe transfer.\n\\newblock In \\emph{ACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Yu et~al.}{2025}]{yu2025confidence}\nYu, Z., et~al. (2025).\n\\newblock The confidence manifold in LLM representations.\n\\newblock In \\emph{ICML}.\n\n\\bibitem[\\protect\\citeauthoryear{Zhao et~al.}{2019}]{zhao2019learning}\nZhao, H., Zhang, S., Wu, G., Moura, J.~M., Costeira, J.~P., and Gordon, G.~J. (2019).\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In \\emph{ICML}.\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 738,
        "oldLines": 9,
        "newStart": 738,
        "newLines": 88,
        "lines": [
          " Most critically, control task analysis reveals that 38\\% of cross-lingual probing results---and 72\\% for low-resource languages---are capacity artifacts, extending Hewitt \\& Liang's framework to multilingual settings as a field-level methodological warning.",
          " Few-shot target-language probes (25--100 examples) remain the most reliable path forward for languages outside the viability boundary.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+\\begin{thebibliography}{30}",
          "+\\bibitem[\\protect\\citeauthoryear{Ahuja et~al.}{2024}]{ahuja2024megaverse}",
          "+Ahuja, K., et~al. (2024).",
          "+\\newblock Megaverse: Benchmarking large language models across languages, modalities, models and tasks.",
          "+\\newblock In \\emph{NeurIPS Datasets and Benchmarks}.",
          " ",
          "+\\bibitem[\\protect\\citeauthoryear{Angelopoulos and Bates}{2023}]{angelopoulos2023conformal}",
          "+Angelopoulos, A.~N. and Bates, S. (2023).",
          "+\\newblock Conformal prediction: A gentle introduction.",
          "+\\newblock \\emph{Foundations and Trends in Machine Learning}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Artetxe et~al.}{2018}]{artetxe2018robust}",
          "+Artetxe, M., Labaka, G., and Agirre, E. (2018).",
          "+\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.",
          "+\\newblock In \\emph{ACL}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Ben-David et~al.}{2010}]{bendavid2010theory}",
          "+Ben-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., and Vaughan, J.~W. (2010).",
          "+\\newblock A theory of learning from different domains.",
          "+\\newblock \\emph{Machine Learning}, 79(1-2):151--175.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Burns et~al.}{2023}]{burns2023discovering}",
          "+Burns, C., Ye, H., Klein, D., and Steinhardt, J. (2023).",
          "+\\newblock Discovering latent knowledge in language models without supervision.",
          "+\\newblock In \\emph{ICLR}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Conneau et~al.}{2018}]{conneau2018word}",
          "+Conneau, A., Lample, G., Ranzato, M., Denoyer, L., and J{\\'e}gou, H. (2018).",
          "+\\newblock Word translation without parallel data.",
          "+\\newblock In \\emph{ICLR}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Hewitt and Liang}{2019}]{hewitt2019designing}",
          "+Hewitt, J. and Liang, P. (2019).",
          "+\\newblock Designing and interpreting probes with control tasks.",
          "+\\newblock In \\emph{EMNLP}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Kornblith et~al.}{2019}]{kornblith2019similarity}",
          "+Kornblith, S., Norouzi, M., Lee, H., and Hinton, G. (2019).",
          "+\\newblock Similarity of neural network representations revisited.",
          "+\\newblock In \\emph{ICML}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Miao et~al.}{2026}]{miao2026coral}",
          "+Miao, N., et~al. (2026).",
          "+\\newblock CORAL: Calibration via representation-aligned learning.",
          "+\\newblock In \\emph{NAACL}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Miao and Ungar}{2026}]{miao2026orthogonality}",
          "+Miao, N. and Ungar, L. (2026).",
          "+\\newblock Orthogonality of correctness and confidence in language model representations.",
          "+\\newblock \\emph{Preprint}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Pires et~al.}{2019}]{pires2019multilingual}",
          "+Pires, T., Schlinger, E., and Garrette, D. (2019).",
          "+\\newblock How multilingual is multilingual BERT?",
          "+\\newblock In \\emph{ACL}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Voita and Titov}{2020}]{voita2020information}",
          "+Voita, E. and Titov, I. (2020).",
          "+\\newblock Information-theoretic probing with minimum description length.",
          "+\\newblock In \\emph{EMNLP}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Wu and Dredze}{2019}]{wu2019beto}",
          "+Wu, S. and Dredze, M. (2019).",
          "+\\newblock Beto, Bentz, Becas: The surprising cross-lingual effectiveness of BERT.",
          "+\\newblock In \\emph{EMNLP}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Xiao et~al.}{2025}]{xiao2025knowledge}",
          "+Xiao, Y., et~al. (2025).",
          "+\\newblock Cross-lingual knowledge boundary probe transfer.",
          "+\\newblock In \\emph{ACL}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Yu et~al.}{2025}]{yu2025confidence}",
          "+Yu, Z., et~al. (2025).",
          "+\\newblock The confidence manifold in LLM representations.",
          "+\\newblock In \\emph{ICML}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Zhao et~al.}{2019}]{zhao2019learning}",
          "+Zhao, H., Zhang, S., Wu, G., Moura, J.~M., Costeira, J.~P., and Gordon, G.~J. (2019).",
          "+\\newblock On learning invariant representations for domain adaptation.",
          "+\\newblock In \\emph{ICML}.",
          "+\\end{thebibliography}",
          "+",
          " \\appendix",
          " ",
          " \\section{Full Zero-Shot Transfer Results}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "dce3d182-414d-4407-8caa-16069218ba6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-21T04:21:37.399Z_

```json
{
  "parentUuid": "316d1899-29e5-44de-98fe-c7ca3141f52d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "67b61937-9a9b-40fe-9b5b-17cc570f877d",
  "timestamp": "2026-05-21T04:21:37.399Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-21T04:21:41.062Z_

Also need to fix `\shortcite` which is an ACL-specific command:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67b61937-9a9b-40fe-9b5b-17cc570f877d",
  "isSidechain": false,
  "requestId": "req_011CbF5FUKTincDRH2pVJEWv",
  "type": "assistant",
  "uuid": "6892d876-0521-4811-9050-16739634a1e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GbGRqorjVoJ1pWugYazS7s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1757,
      "cache_read_input_tokens": 69678,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 69678,
          "cache_creation_input_tokens": 1757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1757
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

_source line 32 · 2026-05-21T04:21:42.506Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01RywwdiTprHaYM1DqKvgJCU`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex",
  "old_string": "\\shortcite",
  "new_string": "\\citeyear"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6892d876-0521-4811-9050-16739634a1e9",
  "isSidechain": false,
  "requestId": "req_011CbF5FUKTincDRH2pVJEWv",
  "type": "assistant",
  "uuid": "cd64c299-7e8c-4f37-b146-a3188e279f93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GbGRqorjVoJ1pWugYazS7s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1757,
      "cache_read_input_tokens": 69678,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 69678,
          "cache_creation_input_tokens": 1757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1757
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

_source line 33 · 2026-05-21T04:21:42.518Z_

<details><summary>↩ Tool result · `toolu_01RywwdiTprHaYM1DqKvgJCU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd64c299-7e8c-4f37-b146-a3188e279f93",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "b3502522-5eec-45cc-b3a9-52b5b28d720f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.tex",
    "oldString": "\\shortcite",
    "newString": "\\citeyear",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 51,
        "oldLines": 7,
        "newStart": 51,
        "newLines": 7,
        "lines": [
          " Representation-level correctness probes bypass this limitation by directly accessing the linearly decodable correctness signal in hidden states \\cite{miao2026coral,burns2023discovering}.",
          " ",
          " However, all existing probe-based calibration methods---CORAL \\cite{miao2026coral}, confidence manifold approaches \\cite{yu2025confidence}, and directional steering \\cite{miao2026orthogonality}---have been developed and evaluated exclusively in English.",
          "-Xiao et al.\\ \\shortcite{xiao2025knowledge} transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages, but answerability is a fundamentally different target from output-dependent correctness: the former measures whether a question is answerable at all, while the latter tracks whether the model's specific output is correct.",
          "+Xiao et al.\\ \\citeyear{xiao2025knowledge} transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages, but answerability is a fundamentally different target from output-dependent correctness: the former measures whether a question is answerable at all, while the latter tracks whether the model's specific output is correct.",
          " ",
          " This paper asks: \\textit{Does the probe-based calibration research program extend to non-English languages?}",
          " Our answer is a qualified negative."
        ]
      },
      {
        "oldStart": 61,
        "oldLines": 7,
        "newStart": 61,
        "newLines": 7,
        "lines": [
          " \\begin{enumerate}",
          " \\item \\textbf{Viability boundary characterization.} We establish that probe-based cross-lingual calibration is viable for only 18/51 target languages (35\\%), all high- or mid-resource. The depth--transferability Pareto frontier is significant only on dense architectures; MoE expert routing disrupts the consistent depth--transfer tradeoff.",
          " ",
          "-\\item \\textbf{Capacity artifact exposure.} Extending Hewitt \\& Liang's \\shortcite{hewitt2019designing} control task framework to multilingual probing, we find that 38\\% of language--layer combinations (72\\% for low-resource languages) have selectivity below 0.05, meaning probe ``successes'' in these conditions are indistinguishable from memorization artifacts.",
          "+\\item \\textbf{Capacity artifact exposure.} Extending Hewitt \\& Liang's \\citeyear{hewitt2019designing} control task framework to multilingual probing, we find that 38\\% of language--layer combinations (72\\% for low-resource languages) have selectivity below 0.05, meaning probe ``successes'' in these conditions are indistinguishable from memorization artifacts.",
          " ",
          " \\item \\textbf{Methodological framework.} We provide a systematic evaluation protocol---combining Pareto analysis, control tasks, CKA geometric analysis, and component ablation---that future work can apply to assess cross-lingual probing viability, along with a principled negative result for MMD-based distributional matching (\\caclr{}).",
          " \\end{enumerate}"
        ]
      },
      {
        "oldStart": 71,
        "oldLines": 25,
        "newStart": 71,
        "newLines": 25,
        "lines": [
          " \\label{sec:related}",
          " ",
          " \\paragraph{Probe-based calibration.}",
          "-Burns et al.\\ \\shortcite{burns2023discovering} and Miao et al.\\ \\shortcite{miao2026coral} demonstrated that correctness is linearly decodable from hidden representations.",
          "-Miao \\& Ungar \\shortcite{miao2026orthogonality} showed that correctness and verbalized confidence directions are near-orthogonal (cosine${<}0.04$ in English), motivating representation-level approaches.",
          "+Burns et al.\\ \\citeyear{burns2023discovering} and Miao et al.\\ \\citeyear{miao2026coral} demonstrated that correctness is linearly decodable from hidden representations.",
          "+Miao \\& Ungar \\citeyear{miao2026orthogonality} showed that correctness and verbalized confidence directions are near-orthogonal (cosine${<}0.04$ in English), motivating representation-level approaches.",
          " All work is English-only.",
          " ",
          " \\paragraph{Cross-lingual transfer.}",
          "-Pires et al.\\ \\shortcite{pires2019multilingual} and Wu \\& Dredze \\shortcite{wu2019beto} established that multilingual models learn shared representations enabling zero-shot cross-lingual transfer, with degradation correlating with typological distance.",
          "+Pires et al.\\ \\citeyear{pires2019multilingual} and Wu \\& Dredze \\citeyear{wu2019beto} established that multilingual models learn shared representations enabling zero-shot cross-lingual transfer, with degradation correlating with typological distance.",
          " Linear cross-lingual alignment (MUSE \\cite{conneau2018word}; VecMap \\cite{artetxe2018robust}) operates at the word-embedding level; our linear projection extends this to sentence-level correctness representations.",
          " ",
          " \\paragraph{Domain adaptation theory.}",
          "-Ben-David et al.\\ \\shortcite{bendavid2010theory} provide the H-divergence framework predicting that transfer degrades with distribution shift.",
          "-Zhao et al.\\ \\shortcite{zhao2019learning} showed that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly relevant to our CaCLR negative result.",
          "+Ben-David et al.\\ \\citeyear{bendavid2010theory} provide the H-divergence framework predicting that transfer degrades with distribution shift.",
          "+Zhao et al.\\ \\citeyear{zhao2019learning} showed that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly relevant to our CaCLR negative result.",
          " ",
          " \\paragraph{Probing methodology.}",
          "-Hewitt \\& Liang \\shortcite{hewitt2019designing} introduced control tasks to distinguish genuine linguistic knowledge from probe capacity artifacts.",
          "-Voita \\& Titov \\shortcite{voita2020information} proposed MDL-based probing.",
          "+Hewitt \\& Liang \\citeyear{hewitt2019designing} introduced control tasks to distinguish genuine linguistic knowledge from probe capacity artifacts.",
          "+Voita \\& Titov \\citeyear{voita2020information} proposed MDL-based probing.",
          " We extend control tasks to multilingual settings, revealing that capacity artifacts are dramatically amplified for low-resource languages.",
          " ",
          " \\paragraph{Conformal prediction.}",
          "-Angelopoulos \\& Bates \\shortcite{angelopoulos2023conformal} provide distribution-free coverage guarantees but require per-language calibration data; our approach targets zero-label transfer.",
          "+Angelopoulos \\& Bates \\citeyear{angelopoulos2023conformal} provide distribution-free coverage guarantees but require per-language calibration data; our approach targets zero-label transfer.",
          " These are complementary directions.",
          " ",
          " %------------------------------------------------------------"
        ]
      },
      {
        "oldStart": 140,
        "oldLines": 7,
        "newStart": 140,
        "newLines": 7,
        "lines": [
          " \\subsection{Control Task Analysis}",
          " \\label{sec:control}",
          " ",
          "-Following Hewitt \\& Liang \\shortcite{hewitt2019designing}, we train control probes on permuted labels and compute selectivity $= \\auroc{}_{\\text{real}} - \\auroc{}_{\\text{control}}$.",
          "+Following Hewitt \\& Liang \\citeyear{hewitt2019designing}, we train control probes on permuted labels and compute selectivity $= \\auroc{}_{\\text{real}} - \\auroc{}_{\\text{control}}$.",
          " A language--layer combination with selectivity${<}0.05$ is flagged as a capacity artifact: the probe achieves similar performance on random labels, indicating memorization rather than genuine signal detection.",
          " ",
          " \\subsection{CKA Geometric Analysis}"
        ]
      },
      {
        "oldStart": 552,
        "oldLines": 7,
        "newStart": 552,
        "newLines": 7,
        "lines": [
          " \\label{tab:ortho}",
          " \\end{table}",
          " ",
          "-Table~\\ref{tab:ortho} shows that the correctness--confidence orthogonality reported by Miao \\& Ungar \\shortcite{miao2026orthogonality} (cosine${<}0.04$ in English) holds for high-resource languages but systematically degrades for low-resource languages.",
          "+Table~\\ref{tab:ortho} shows that the correctness--confidence orthogonality reported by Miao \\& Ungar \\citeyear{miao2026orthogonality} (cosine${<}0.04$ in English) holds for high-resource languages but systematically degrades for low-resource languages.",
          " 15\\% of language--architecture combinations exceed cosine$=0.15$; all are low-resource languages.",
          " This could reflect genuine structural non-orthogonality or, more likely given the control task results (\\S\\ref{sec:control-results}), noisy direction estimates from capacity-artifact probes.",
          " "
        ]
      },
      {
        "oldStart": 707,
        "oldLines": 7,
        "newStart": 707,
        "newLines": 7,
        "lines": [
          " As MoE becomes the dominant architecture for frontier models, this finding has direct implications for the scalability of probe-based methods.",
          " ",
          " \\paragraph{Capacity artifacts as a field-level concern.}",
          "-The 72\\% artifact rate for low-resource languages extends Hewitt \\& Liang's \\shortcite{hewitt2019designing} insight to a setting they did not consider.",
          "+The 72\\% artifact rate for low-resource languages extends Hewitt \\& Liang's \\citeyear{hewitt2019designing} insight to a setting they did not consider.",
          " Their original work focused on English syntactic probing; we show that capacity artifacts are dramatically amplified in multilingual settings, particularly for languages with lower-quality evaluation data (GlobalMMLU translation artifacts may contribute systematic patterns that probes exploit).",
          " Any future cross-lingual probing study should include control task analysis as a mandatory validation step.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "cd64c299-7e8c-4f37-b146-a3188e279f93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "b3502522-5eec-45cc-b3a9-52b5b28d720f",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration viability boundaries",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084"
}
```

---

### Assistant

_source line 36 · 2026-05-21T04:21:46.125Z_

Now compile:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3502522-5eec-45cc-b3a9-52b5b28d720f",
  "isSidechain": false,
  "requestId": "req_011CbF5FrQVnxmXmK4wuzjy3",
  "type": "assistant",
  "uuid": "05646e9d-a842-4c09-ae98-c877142366a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcfTQmnNmUnpCzqoJPTy4N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 260,
      "cache_read_input_tokens": 71435,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 71435,
          "cache_creation_input_tokens": 260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 260
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

_source line 37 · 2026-05-21T04:21:47.273Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y8gZY9LdD5HxG7hpUD1dpb`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05646e9d-a842-4c09-ae98-c877142366a7",
  "isSidechain": false,
  "requestId": "req_011CbF5FrQVnxmXmK4wuzjy3",
  "type": "assistant",
  "uuid": "fce069aa-497e-4f51-a2e0-c2ea270470d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcfTQmnNmUnpCzqoJPTy4N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 260,
      "cache_read_input_tokens": 71435,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 71435,
          "cache_creation_input_tokens": 260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 260
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

_source line 38 · 2026-05-21T04:21:48.018Z_

<details><summary>↩ Tool result · `toolu_01Y8gZY9LdD5HxG7hpUD1dpb`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (13 pages, 195607 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fce069aa-497e-4f51-a2e0-c2ea270470d3",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "2fb6d0ce-b912-44d7-bfbf-b11986532ba9",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (13 pages, 195607 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fce069aa-497e-4f51-a2e0-c2ea270470d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T04:21:51.344Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NpmYFR6HUPWjJyLzS36zZE`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fb6d0ce-b912-44d7-bfbf-b11986532ba9",
  "isSidechain": false,
  "requestId": "req_011CbF5GFhiCYzDfFHSvtB1G",
  "type": "assistant",
  "uuid": "68584a69-0010-4128-b803-80d39ce60e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aBRHqjdQBdkQRtaVhLHTb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 71695,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 71695,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 40 · 2026-05-21T04:21:52.155Z_

<details><summary>↩ Tool result · `toolu_01NpmYFR6HUPWjJyLzS36zZE`</summary>

```text
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on paper.pdf (13 pages, 200195 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68584a69-0010-4128-b803-80d39ce60e67",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "5a96deb4-d9db-4644-bc29-5a5770231095",
  "toolUseResult": {
    "stdout": "re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (13 pages, 200195 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "68584a69-0010-4128-b803-80d39ce60e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T04:21:54.802Z_

Compilation successful. Let me verify no errors in the log:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a96deb4-d9db-4644-bc29-5a5770231095",
  "isSidechain": false,
  "requestId": "req_011CbF5GZRKqtcqLfBhRpx9p",
  "type": "assistant",
  "uuid": "78e77fee-4047-4a79-b272-094f81865675",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEUB5puHc1EgQYfZAjZWeK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 72389,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 72389,
          "cache_creation_input_tokens": 236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 236
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

_source line 42 · 2026-05-21T04:21:55.934Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HoX4Y5AeWjaA9ZzinKAx7U`</summary>

```json
{
  "command": "grep -c \"^!\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/paper.log",
  "description": "Check for LaTeX errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78e77fee-4047-4a79-b272-094f81865675",
  "isSidechain": false,
  "requestId": "req_011CbF5GZRKqtcqLfBhRpx9p",
  "type": "assistant",
  "uuid": "69fdfd5f-fd77-4db8-b705-1a41f6f1e4fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEUB5puHc1EgQYfZAjZWeK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 72389,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 72389,
          "cache_creation_input_tokens": 236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 236
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

_source line 43 · 2026-05-21T04:21:55.998Z_

<details><summary>↩ Tool result · `toolu_01HoX4Y5AeWjaA9ZzinKAx7U`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69fdfd5f-fd77-4db8-b705-1a41f6f1e4fc",
  "isSidechain": false,
  "promptId": "934a609c-d6c8-4177-97f9-cabc4c2d670b",
  "type": "user",
  "uuid": "1e935d6b-7221-4daa-b010-72d247b9bcc2",
  "toolUseResult": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "69fdfd5f-fd77-4db8-b705-1a41f6f1e4fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-21T04:22:08.815Z_

PDF compiled cleanly (13 pages, 0 errors) at `worst/paper.tex`.

The paper covers all 11 experiments from `experiment_data.json`:
- **Tables 1--3** (arch comparison, Qwen/Scout Pareto $\rho$): Pareto frontier analysis
- **Tables 4--6** (ZS AUROC, transfer comparison, $\beta$ sweep, ablation): CaCLR negative result
- **Table 7** (selectivity, artifact detail): Control task / capacity artifacts
- **Tables 8--9** (CKA partial correlation, subspace angles): CKA analysis
- **Table 10** (difficulty decomposition): Decomposition ablation
- **Table 11** (orthogonality cosine): Cross-lingual orthogonality
- **Table 12** (LR vs MLP): Probe complexity
- **Tables 13--14** (projection efficiency, by tier): Linear projection sample efficiency
- **Table 15** (cross-benchmark): Generalization
- **Table 16** (quantization): Validation ablation
- **Table 17** (viability classification): Extended 52-language coverage

Narrative follows the "worst tier" reframe: viability boundary + capacity artifact warning + methodological framework, not a method contribution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e935d6b-7221-4daa-b010-72d247b9bcc2",
  "isSidechain": false,
  "requestId": "req_011CbF5GqwzgEu76pakjxv4n",
  "type": "assistant",
  "uuid": "ba6a2fa3-9e84-4bec-815e-bb5734daaef6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01926Wq5CfdcMnhLEuo5baXd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 72625,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 305,
          "cache_read_input_tokens": 72625,
          "cache_creation_input_tokens": 155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 155
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "ba6a2fa3-9e84-4bec-815e-bb5734daaef6",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration viability boundaries",
  "sessionId": "c6c5af12-c569-4559-ba51-4daf898d5084"
}
```

---
