# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/67525fd2-9679-4e46-9b3e-5dfdbacf9928.jsonl`
- **Structured JSON:** [`bafd2b681ec79c35b0e4.json`](../../sessions/ba/bafd2b681ec79c35b0e4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:09:06.277Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:09:06.277Z",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Discovery + principled negative result + practical recommendation 三段叙事。 (1) Pareto frontier 在 Qwen3-235B 上清晰（rho ~ -0.50），在 Llama 4 Scout 上 language-specific（global rho ~ -0.12）：部分语言随 depth 改善（ar/ko/hi）， 部分退化（zh/sw），验证 architecture-dependent tradeoff shape。 (2) CaCLR β sweep 3 OOM 证明 MMD consistency loss inert（d=0.07, p=0.38）。 CKA 几何分析提供 suggestive 解释——MMD matches marginals but not low-dim directional structure——但 partial correlation controlling depth 仅 r=0.18, p=0.11，降级为 suggestive correlational analysis。Between-language correlation 成立（same-layer r=0.52, p<0.01）。 (3) Linear projection ~50 pairs 是实际方案（+3.5pp over zero-shot），surpasses CaCLR at ~20 pairs。 Decomposition 定性成立（65% combos improved, d=0.25），orthogonality 跨语言持续 但 low-resource variance 增大（cosine max 0.11）。 Control task artifact warning 升级为独立贡献：~27% lang-layer combos selectivity < 0.05，集中在 low-resource + shallow layers。 Target: EACL borderline accept，以 discovery + systematic negative result 发表。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T04:09:06.280Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:09:06.280Z",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

## Round 1

77 recorded events

### User

_source line 3 · 2026-05-21T04:09:06.314Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Discovery + principled negative result + practical recommendation 三段叙事。 (1) Pareto frontier 在 Qwen3-235B 上清晰（rho ~ -0.50），在 Llama 4 Scout 上 language-specific（global rho ~ -0.12）：部分语言随 depth 改善（ar/ko/hi）， 部分退化（zh/sw），验证 architecture-dependent tradeoff shape。 (2) CaCLR β sweep 3 OOM 证明 MMD consistency loss inert（d=0.07, p=0.38）。 CKA 几何分析提供 suggestive 解释——MMD matches marginals but not low-dim directional structure——但 partial correlation controlling depth 仅 r=0.18, p=0.11，降级为 suggestive correlational analysis。Between-language correlation 成立（same-layer r=0.52, p<0.01）。 (3) Linear projection ~50 pairs 是实际方案（+3.5pp over zero-shot），surpasses CaCLR at ~20 pairs。 Decomposition 定性成立（65% combos improved, d=0.25），orthogonality 跨语言持续 但 low-resource variance 增大（cosine max 0.11）。 Control task artifact warning 升级为独立贡献：~27% lang-layer combos selectivity < 0.05，集中在 low-resource + shallow layers。 Target: EACL borderline accept，以 discovery + systematic negative result 发表。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "a0929d6f-bf7b-43d8-b180-f2fb7807a157",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:09:06.314Z_

```json
{
  "parentUuid": "a0929d6f-bf7b-43d8-b180-f2fb7807a157",
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
  "uuid": "d9bcb2ab-adb6-4780-b63b-7745282c6cc6",
  "timestamp": "2026-05-21T04:09:06.314Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:09:06.314Z_

```json
{
  "parentUuid": "d9bcb2ab-adb6-4780-b63b-7745282c6cc6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8bf923e6-9a1a-45ab-9ae8-d4cef3ef0465",
  "timestamp": "2026-05-21T04:09:06.314Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
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
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

### Assistant

_source line 7 · 2026-05-21T04:09:09.408Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bf923e6-9a1a-45ab-9ae8-d4cef3ef0465",
  "isSidechain": false,
  "requestId": "req_011CbF4J7AwY8Eu9zLwoBvoY",
  "type": "assistant",
  "uuid": "e56d3c28-ecda-42a1-a891-7da03f337295",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjskSzkyoqYBpQ1ZkQh2pM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11710,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11710
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

_source line 8 · 2026-05-21T04:09:10.378Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MeM17WNH1HPesrthb7DqtC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e56d3c28-ecda-42a1-a891-7da03f337295",
  "isSidechain": false,
  "requestId": "req_011CbF4J7AwY8Eu9zLwoBvoY",
  "type": "assistant",
  "uuid": "0169291f-bed1-424b-84ca-5d07e34df71f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjskSzkyoqYBpQ1ZkQh2pM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11710,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11710
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

_source line 9 · 2026-05-21T04:09:10.673Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PsPxR9wFfoa3EnNZyCbnUx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0169291f-bed1-424b-84ca-5d07e34df71f",
  "isSidechain": false,
  "requestId": "req_011CbF4J7AwY8Eu9zLwoBvoY",
  "type": "assistant",
  "uuid": "d1d198f6-8488-47d2-8924-13c2e461c3f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjskSzkyoqYBpQ1ZkQh2pM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11710,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11710
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

_source line 10 · 2026-05-21T04:09:10.681Z_

<details><summary>↩ Tool result · `toolu_01PsPxR9wFfoa3EnNZyCbnUx`</summary>

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
  "parentUuid": "d1d198f6-8488-47d2-8924-13c2e461c3f1",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "a80cd3c8-e40f-4c75-9db4-af405e57728e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff varies across architectures (strong on Qwen, weak on Llama); CKA geometric analysis (not mechanistic explanation — correlational, must control for depth) suggests architecture-specific representation divergence rates as a factor. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. A methodological warning: control task analysis reveals that ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold), challenging uncritical use of cross-lingual probing. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis (framed as correlational, NOT mechanistic) provides two levels of insight: (a) between-language: languages with higher CKA show less transfer degradation; (b) between-architecture: CKA cliff steepness differs. **MUST report partial correlation controlling for normalized depth** — if CKA adds no explanatory power beyond depth, downgrade to \"suggestive correlational analysis.\" Subspace angle analysis (quantitative, not just prose) strengthens geometric narrative.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame CKA analysis as geometric/correlational, not mechanistic. We report partial correlation controlling for depth to test whether CKA adds explanatory power beyond the trivial \"deeper = worse transfer.\" If partial correlation is weak, we explicitly state CKA is suggestive only.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 79,
      "startLine": 1,
      "totalLines": 79
    }
  },
  "sourceToolAssistantUUID": "d1d198f6-8488-47d2-8924-13c2e461c3f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T04:09:10.728Z_

<details><summary>↩ Tool result · `toolu_01MeM17WNH1HPesrthb7DqtC`</summary>

```text
1	[
2	  {
3	    "name": "Qwen3-235B-A22B Full Pareto Frontier",
4	    "description": "Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): 24 probed layers (every 4th), 20 languages, EN correctness probes (LogReg + MLP), 5 transfer conditions. Per-language Spearman rho.\n",
5	    "results": {
6	      "en_best_auroc": 0.8,
7	      "en_best_layer": 72,
8	      "en_best_ece_raw": 0.175,
9	      "en_auroc_range": [
10	        0.54,
11	        0.8
12	      ],
13	      "en_auroc_at_50pct_depth_L48": 0.77,
14	      "en_auroc_profile_summary": "L0-L20: 0.54-0.67 (early buildup); L24-L44: 0.70-0.76 (mid layers); L48-L68: 0.77-0.80 (approaching peak); L72: 0.80 (peak); L76-L92: 0.79-0.75 (slight decline)\n",
15	      "zs_at_en_optimal_L72": {
16	        "zh": 0.71,
17	        "es": 0.7,
18	        "fr": 0.7,
19	        "de": 0.69,
20	        "ja": 0.67,
21	        "pt": 0.69,
22	        "nl": 0.68,
23	        "ru": 0.67,
24	        "ar": 0.65,
25	        "hi": 0.64,
26	        "ko": 0.66,
27	        "vi": 0.64,
28	        "tr": 0.63,
29	        "id": 0.65,
30	        "pl": 0.66,
31	        "uk": 0.65,
32	        "sw": 0.55,
33	        "bn": 0.54,
34	        "te": 0.56,
35	        "avg": 0.647
36	      },
37	      "zs_at_best_transfer_L48": {
38	        "zh": 0.73,
39	        "es": 0.72,
40	        "fr": 0.71,
41	        "de": 0.7,
42	        "ja": 0.69,
43	        "pt": 0.7,
44	        "nl": 0.69,
45	        "ru": 0.69,
46	        "ar": 0.67,
47	        "hi": 0.66,
48	        "ko": 0.68,
49	        "vi": 0.66,
50	        "tr": 0.65,
51	        "id": 0.67,
52	        "pl": 0.68,
53	        "uk": 0.67,
54	        "sw": 0.58,
55	        "bn": 0.57,
56	        "te": 0.59,
57	        "avg": 0.669
58	      },
59	      "pareto_rho_global": -0.5,
60	      "pareto_rho_per_lang_median": -0.48,
61	      "pareto_rho_per_lang": {
62	        "zh": -0.45,
63	        "es": -0.42,
64	        "fr": -0.43,
65	        "de": -0.44,
66	        "ja": -0.47,
67	        "pt": -0.43,
68	        "nl": -0.44,
69	        "ru": -0.46,
70	        "ar": -0.5,
71	        "hi": -0.52,
72	        "ko": -0.48,
73	        "vi": -0.51,
74	        "tr": -0.53,
75	        "id": -0.49,
76	        "pl": -0.46,
77	        "uk": -0.47,
78	        "sw": -0.58,
79	        "bn": -0.56,
80	        "te": -0.55
81	      },
82	      "pareto_rho_range": [
83	        -0.58,
84	        -0.42
85	      ],
86	      "zs_langs_above_060": 16,
87	      "zs_langs_above_065": 13,
88	      "transfer_methods_at_L48": {
89	        "zero_shot_avg": 0.669,
90	        "mean_shift_avg": 0.669,
91	        "mean_shift_delta": 0.0,
92	        "linear_proj_50_avg": 0.704,
93	        "linear_proj_50_delta": 0.035,
94	        "fewshot_25_avg": 0.695,
95	        "fewshot_25_delta": 0.026,
96	        "fewshot_100_avg": 0.715,
97	        "fewshot_100_delta": 0.046,
98	        "caclr_best_avg": 0.677,
99	        "caclr_best_delta": 0.008
100	      },
101	      "bootstrap_ci_linear_proj_delta": [
102	        0.025,
103	        0.045
104	      ],
105	      "bootstrap_ci_fewshot100_delta": [
106	        0.035,
107	        0.057
108	      ],
109	      "bootstrap_ci_caclr_delta": [
110	        -0.003,
111	        0.019
112	      ]
113	    },
114	    "tables": [
115	      {
116	        "name": "Table 1: Qwen3-235B Zero-Shot Transfer AUROC (Language × Layer)",
117	        "description": "24 probed layers (rows) × 20 languages + EN (columns)。 Cells: AUROC。Bold: per-language best layer。Gray: within 1pp of best。 Bottom: per-language Spearman rho ± bootstrap 95% CI。 Key pattern: EN-optimal L72 ≠ transfer-optimal L48 for all languages。 Resource-tier banding visible: HIGH langs (zh/es/fr/de) show flatter profiles; LOW langs (sw/bn/te) show steeper drop-off at deep layers。\n"
118	      },
119	      {
120	        "name": "Table 2: Qwen3-235B Transfer Method Comparison",
121	        "description": "5 methods (columns) × 20 langs (rows), at two fixed layers (L48 = 50% depth, L72 = EN-optimal) + per-lang oracle。AUROC, ΔAUROC vs zero-shot, bootstrap 95% CI, paired permutation p, Cohen's d。\n"
122	      }
123	    ],
124	    "figures": [],
125	    "analysis": "Qwen3-235B 作为 \"strong Pareto architecture\" 的角色得到验证：所有 20 语言 都展现一致的 depth-transfer tradeoff（全部 rho 负值），没有例外。 Architecture-specific 特征是 MoE routing 引入的层间异质性使 frontier 不如 dense model 平滑（per-layer variance 较高），但总趋势清晰。 16/20 语言在最优 transfer layer 达到 >0.60 AUROC，13/20 达到 >0.65， 验证 zero-shot probe transfer 对 majority languages 可行。 sw/bn/te 的失败是 pretraining representation 的基础限制，非 architecture-specific。\n\n\nQwen3-235B-A22B 是 94 层 MoE 架构，显著深于 MVP 的 7B 模型。EN best AUROC 从 MVP 的 0.754 提升到 0.80，因为更大模型编码更强的 correctness signal。 Peak 在 ~77% depth (L72)，与 MVP pattern 一致——correctness 在 deep-but-not-final 层达到峰值。\nPareto frontier 清晰（median per-lang rho = -0.48）因为：(a) 94 层提供足够 depth gradient 让 language specialization 逐渐显现；(b) 所有 20 语言在更深层 的 transfer 都退化，只是退化速度不同。Low-resource 语言（sw/bn/te）rho 更强 负（-0.55 ~ -0.58）因为它们的跨语言表征从一开始就弱，depth-induced specialization 影响更大。High-resource 语言 rho 较温和（-0.42 ~ -0.45）因为 丰富的预训练数据使深层仍保持合理的跨语言对齐。\nBest transfer layer (L48, ~51% depth) vs EN-optimal (L72, ~77% depth) 的 gap 是 Pareto tradeoff 的直接体现：L48 平均 ZS AUROC 0.669 vs L72 的 0.647， 差 2.2pp。\nMean-shift ΔAUROC ≡ 0 符合数学证明（rank-invariance under StandardScaler + logistic regression）。Linear projection +3.5pp 因为直接学习 rotation correction。CaCLR +0.8pp 几乎全来自 α (SB-ECE) 项而非 β (MMD) 项。\n"
126	  },
127	  {
128	    "name": "Llama 4 Scout Full Pareto Frontier",
129	    "description": "Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): 12 probed layers (every 4th), 20 languages, 5 transfer conditions. Per-language Spearman rho. Architecture contrast with Qwen3-235B.\n",
130	    "results": {
131	      "en_best_auroc": 0.78,
132	      "en_best_layer": 40,
133	      "en_best_ece_raw": 0.185,
134	      "en_auroc_range": [
135	        0.55,
136	        0.78
137	      ],
138	      "en_auroc_at_50pct_depth_L24": 0.73,
139	      "zs_at_en_optimal_L40": {
140	        "zh": 0.67,
141	        "es": 0.66,
142	        "fr": 0.66,
143	        "de": 0.65,
144	        "ja": 0.64,
145	        "pt": 0.65,
146	        "nl": 0.64,
147	        "ru": 0.64,
148	        "ar": 0.65,
149	        "hi": 0.63,
150	        "ko": 0.66,
151	        "vi": 0.62,
152	        "tr": 0.61,
153	        "id": 0.63,
154	        "pl": 0.64,
155	        "uk": 0.63,
156	        "sw": 0.54,
157	        "bn": 0.53,
158	        "te": 0.55,
159	        "avg": 0.627
160	      },
161	      "zs_at_per_lang_best": {
162	        "zh": {
163	          "auroc": 0.69,
164	          "best_layer": 24
165	        },
166	        "es": {
167	          "auroc": 0.68,
168	          "best_layer": 24
169	        },
170	        "fr": {
171	          "auroc": 0.68,
172	          "best_layer": 28
173	        },
174	        "de": {
175	          "auroc": 0.67,
176	          "best_layer": 24
177	        },
178	        "ja": {
179	          "auroc": 0.66,
180	          "best_layer": 28
181	        },
182	        "pt": {
183	          "auroc": 0.67,
184	          "best_layer": 24
185	        },
186	        "nl": {
187	          "auroc": 0.66,
188	          "best_layer": 28
189	        },
190	        "ru": {
191	          "auroc": 0.66,
192	          "best_layer": 28
193	        },
194	        "ar": {
195	          "auroc": 0.66,
196	          "best_layer": 40
197	        },
198	        "hi": {
199	          "auroc": 0.64,
200	          "best_layer": 36
201	        },
202	        "ko": {
203	          "auroc": 0.67,
204	          "best_layer": 40
205	        },
206	        "vi": {
207	          "auroc": 0.64,
208	          "best_layer": 32
209	        },
210	        "tr": {
211	          "auroc": 0.63,
212	          "best_layer": 32
213	        },
214	        "id": {
215	          "auroc": 0.65,
216	          "best_layer": 32
217	        },
218	        "pl": {
219	          "auroc": 0.66,
220	          "best_layer": 32
221	        },
222	        "uk": {
223	          "auroc": 0.65,
224	          "best_layer": 32
225	        },
226	        "sw": {
227	          "auroc": 0.57,
228	          "best_layer": 20
229	        },
230	        "bn": {
231	          "auroc": 0.56,
232	          "best_layer": 20
233	        },
234	        "te": {
235	          "auroc": 0.57,
236	          "best_layer": 24
237	        },
238	        "avg": 0.649
239	      },
240	      "pareto_rho_global": -0.12,
241	      "pareto_rho_per_lang_median": -0.1,
242	      "pareto_rho_per_lang": {
243	        "zh": -0.35,
244	        "es": -0.3,
245	        "fr": -0.28,
246	        "de": -0.32,
247	        "ja": -0.25,
248	        "pt": -0.27,
249	        "nl": -0.22,
250	        "ru": -0.18,
251	        "ar": 0.15,
252	        "hi": 0.08,
253	        "ko": 0.12,
254	        "vi": -0.05,
255	        "tr": -0.08,
256	        "id": 0.02,
257	        "pl": -0.1,
258	        "uk": -0.05,
259	        "sw": -0.42,
260	        "bn": -0.38,
261	        "te": -0.3
262	      },
263	      "pareto_rho_range": [
264	        -0.42,
265	        0.15
266	      ],
267	      "n_langs_positive_rho": 4,
268	      "n_langs_negative_rho_sig": 8,
269	      "n_langs_near_zero": 8,
270	      "transfer_methods_at_L28": {
271	        "zero_shot_avg": 0.638,
272	        "mean_shift_avg": 0.638,
273	        "mean_shift_delta": 0.0,
274	        "linear_proj_50_avg": 0.67,
275	        "linear_proj_50_delta": 0.032,
276	        "fewshot_25_avg": 0.662,
277	        "fewshot_25_delta": 0.024,
278	        "fewshot_100_avg": 0.682,
279	        "fewshot_100_delta": 0.044,
280	        "caclr_best_avg": 0.644,
281	        "caclr_best_delta": 0.006
282	      },
283	      "zs_langs_above_060": 15,
284	      "zs_langs_above_065": 10
285	    },
286	    "tables": [
287	      {
288	        "name": "Table 3: Llama 4 Scout Zero-Shot Transfer AUROC (Language × Layer)",
289	        "description": "12 probed layers × 20 languages。Same format as Table 1。 KEY CONTRAST: per-language Spearman rho 有 4 个正值（ar/ko/hi/id）， 与 Qwen3 全负形成对比。用 ↑↓ arrows 标注 rho 方向。\n"
290	      },
291	      {
292	        "name": "Table 4: Architecture Contrast — Per-Language Spearman rho",
293	        "description": "20 languages (rows) × 2 architectures (columns: Qwen3 rho, Llama4 rho)。 Sorted by rho difference。Highlighted: languages where rho sign flips between architectures (ar, ko, hi)。Bootstrap 95% CI for each。 Bottom: architecture-level summary (median, IQR, % negative)。\n"
294	      }
295	    ],
296	    "figures": [],
297	    "analysis": "Llama 4 Scout 的 language-specific Pareto 是 paper 最重要的 architecture contrast finding。Global rho -0.12 不是 \"weak version of same trend\" 而是 \"qualitatively different pattern\"——4/20 语言的 rho 为正（deeper layers transfer BETTER），8/20 near zero，仅 8/20 显著负。 这与 Qwen3 的 20/20 负值形成 stark contrast。\n实际含义：在 Llama 4 Scout 上不存在单一 \"best transfer layer\"—— practitioner 需要 per-language layer selection（或 per-language oracle）， 而 Qwen3 上可以用 50% depth 的 universal rule。这是 architecture-dependent 的 practical recommendation。\n\n\nLlama 4 Scout 是 median 档的 \"weak/language-specific Pareto\" 架构。 MVP 已展示此 pattern：Llama-3.1-8B 上 ar/hi/ko 的 best transfer layer 在最深层 (L31)，而 zh 在 L20, sw 在 L16——不同语言的最优层方向不一致。\n全量实验中此 pattern 放大：ar (rho=+0.15)、ko (+0.12)、hi (+0.08) 在更深层 transfer 更好，因为 Llama 4 的 MoE routing 对这些语言在深层 保持了更好的跨语言对齐（可能与 Llama 4 training data 中 ar/ko/hi 的分布有关）。同时 zh (-0.35)、sw (-0.42) 展示传统的 depth-degradation pattern。\nGlobal rho = -0.12 因为正负 rho 相互抵消——这不是 noise，而是 genuinely language-specific behavior。与 Qwen3 的 uniform negative rho 形成 sharp architectural contrast：同一组语言在两个架构上展现 qualitatively different Pareto shapes。\n这直接支持 Claim 1 的 \"architecture-dependent tradeoff shape\" 结论。 Important caveat: n=2 architectures 无法归因于具体 architectural feature （MoE routing scheme、training data composition、layer count 都不同）， 仅能报告 observational finding。\n"
298	  },
299	  {
300	    "name": "CaCLR Implementation and Comparative Evaluation",
301	    "description": "CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) implementation。 β sweep 3 OOM (0.001–1.0), α sweep (0.01–10.0)。 Full comparison vs zero-shot, mean-shift, linear projection, few-shot on both models × 20 languages。\n",
302	    "results": {
303	      "implementation": {
304	        "mmd_kernel": "gaussian_rbf",
305	        "bandwidth": "median_heuristic",
306	        "optimizer": "adam",
307	        "lr": 0.001,
308	        "lr_schedule": "cosine_decay",
309	        "epochs": 50,
310	        "early_stopping": "patience_10_on_val_bce",
311	        "init": "from_standard_lr_solution",
312	        "batch_size": 256,
313	        "mmd_items": "same_as_bce",
314	        "parallel_set_sizes": {
315	          "avg_per_lang": 9800,
316	          "min_lang_te": 4200,
317	          "max_lang_en": 14042
318	        }
319	      },
320	      "alpha_sweep": {
321	        "alpha_0p01": {
322	          "en_auroc": 0.8,
323	          "en_ece": 0.17,
324	          "zs_avg_auroc": 0.647
325	        },
326	        "alpha_0p1": {
327	          "en_auroc": 0.798,
328	          "en_ece": 0.145,
329	          "zs_avg_auroc": 0.648
330	        },
331	        "alpha_0p5": {
332	          "en_auroc": 0.795,
333	          "en_ece": 0.125,
334	          "zs_avg_auroc": 0.65
335	        },
336	        "alpha_1p0": {
337	          "en_auroc": 0.79,
338	          "en_ece": 0.118,
339	          "zs_avg_auroc": 0.651
340	        },
341	        "alpha_3p0": {
342	          "en_auroc": 0.78,
343	          "en_ece": 0.112,
344	          "zs_avg_auroc": 0.648
345	        },
346	        "alpha_10p0": {
347	          "en_auroc": 0.755,
348	          "en_ece": 0.108,
349	          "zs_avg_auroc": 0.635
350	        },
351	        "alpha_optimal": 0.5
352	      },
353	      "beta_sweep": {
354	        "beta_0": {
355	          "delta_auroc_vs_beta0": 0.0,
356	          "delta_ece": 0.0
357	        },
358	        "beta_0p001": {
359	          "delta_auroc_vs_beta0": 0.002,
360	          "delta_ece": -0.001
361	        },
362	        "beta_0p003": {
363	          "delta_auroc_vs_beta0": 0.001,
364	          "delta_ece": -0.001
365	        },
366	        "beta_0p01": {
367	          "delta_auroc_vs_beta0": 0.001,
368	          "delta_ece": 0.0
369	        },
370	        "beta_0p03": {
371	          "delta_auroc_vs_beta0": -0.001,
372	          "delta_ece": 0.001
373	        },
374	        "beta_0p1": {
375	          "delta_auroc_vs_beta0": -0.002,
376	          "delta_ece": 0.002
377	        },
378	        "beta_0p3": {
379	          "delta_auroc_vs_beta0": -0.005,
380	          "delta_ece": 0.003
381	        },
382	        "beta_1p0": {
383	          "delta_auroc_vs_beta0": -0.01,
384	          "delta_ece": 0.005
385	        }
386	      },
387	      "beta_sweep_stats": {
388	        "max_delta_auroc": 0.002,
389	        "min_delta_auroc": -0.01,
390	        "paired_permutation_p": 0.38,
391	        "cohens_d": 0.07,
392	        "any_beta_significant_at_005": false
393	      },
394	      "component_ablation": {
395	        "bce_only": {
396	          "zs_avg_auroc": 0.647,
397	          "ece": 0.175
398	        },
399	        "bce_plus_alpha": {
400	          "zs_avg_auroc": 0.651,
401	          "ece": 0.125
402	        },
403	        "bce_plus_beta": {
404	          "zs_avg_auroc": 0.649,
405	          "ece": 0.173
406	        },
407	        "bce_plus_alpha_plus_beta": {
408	          "zs_avg_auroc": 0.652,
409	          "ece": 0.124
410	        },
411	        "alpha_contribution": "+0.004_auroc_and_-0.050_ece",
412	        "beta_contribution": "+0.001_auroc_and_-0.001_ece"
413	      },
414	      "method_comparison_qwen_L48": {
415	        "zero_shot": {
416	          "auroc": 0.669,
417	          "ece": 0.165
418	        },
419	        "mean_shift": {
420	          "auroc": 0.669,
421	          "ece": 0.168
422	        },
423	        "caclr_alpha_only": {
424	          "auroc": 0.673,
425	          "ece": 0.135
426	        },
427	        "caclr_full": {
428	          "auroc": 0.677,
429	          "ece": 0.133
430	        },
431	        "linear_proj_50": {
432	          "auroc": 0.704,
433	          "ece": 0.148
434	        },
435	        "fewshot_25": {
436	          "auroc": 0.695,
437	          "ece": 0.14
438	        },
439	        "fewshot_100": {
440	          "auroc": 0.715,
441	          "ece": 0.128
442	        }
443	      },
444	      "method_comparison_llama_L28": {
445	        "zero_shot": {
446	          "auroc": 0.638,
447	          "ece": 0.172
448	        },
449	        "mean_shift": {
450	          "auroc": 0.638,
451	          "ece": 0.175
452	        },
453	        "caclr_alpha_only": {
454	          "auroc": 0.642,
455	          "ece": 0.142
456	        },
457	        "caclr_full": {
458	          "auroc": 0.644,
459	          "ece": 0.14
460	        },
461	        "linear_proj_50": {
462	          "auroc": 0.67,
463	          "ece": 0.155
464	        },
465	        "fewshot_25": {
466	          "auroc": 0.662,
467	          "ece": 0.148
468	        },
469	        "fewshot_100": {
470	          "auroc": 0.682,
471	          "ece": 0.135
472	        }
473	      },
474	      "beta_effect_by_tier": {
475	        "high_resource": {
476	          "delta_auroc": 0.003,
477	          "n_langs": 8
478	        },
479	        "mid_resource": {
480	          "delta_auroc": 0.001,
481	          "n_langs": 8
482	        },
483	        "low_resource": {
484	          "delta_auroc": -0.004,
485	          "n_langs": 3
486	        }
487	      },
488	      "caclr_delta_auroc_vs_zeroshot": 0.008,
489	      "caclr_delta_ece_vs_tempscaling": -0.003,
490	      "linear_proj_50_delta_auroc_vs_zeroshot": 0.035,
491	      "linear_proj_50_vs_caclr_delta": 0.027
492	    },
493	    "tables": [
494	      {
495	        "name": "Table 5: β Sweep — ΔAUROC over α-only Baseline",
496	        "description": "β values (rows: 0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0) × summary stats (columns: median ΔAUROC, mean, std, # langs improved, paired permutation p, Cohen's d)。Both models side-by-side。 Key: NO β achieves p < 0.05 or d > 0.2。 Shaded gray: β = 0 row (reference)。\n"
497	      },
498	      {
499	        "name": "Table 6: Transfer Method Comparison — Full Ranking",
500	        "description": "7 methods (rows) × 2 models × 2 fixed layers。 Columns: AUROC, ΔAUROC vs ZS, bootstrap 95% CI, p-value, Cohen's d。 Clear visual separation: linear-proj/few-shot cluster significantly above zero-shot; CaCLR-full/CaCLR-α-only marginally above; mean-shift identical to zero-shot。\n"
501	      },
502	      {
503	        "name": "Table 7: Component Ablation",
504	        "description": "4 configurations (BCE-only, +α, +β, +α+β) × AUROC, ECE, ΔAUROC。 Demonstrates α contributes ECE reduction, β contributes nothing。 Clean decomposition of CaCLR components。\n"
505	      }
506	    ],
507	    "figures": [],
508	    "analysis": "CaCLR β inertness 是 paper 的 centerpiece negative result。论证三步： (1) Empirically: β across 3 OOM, d=0.07, p=0.38, both architectures; (2) Theoretically: Zhao et al. (2019) predicts MMD failure when P(Y|X) differs across domains; (3) Constructively: linear projection succeeds (+3.5pp) because it addresses the actual misalignment type (geometric rotation)。\n这关闭了 MMD distributional matching 这条路。Paper framing: \"CaCLR is the natural baseline testing whether distributional matching works; the systematic negative result + geometric explanation saves the community from pursuing this path.\" CaCLR 不是 novel method contribution，而是 systematic test of an obvious-seeming approach。\nPositive takeaway: α-only CaCLR（即 SB-ECE regularized probes） provides marginal ECE improvement，可作为 calibration regularizer standalone recommendation。\n\n\nβ (MMD consistency loss) inert 的根本原因：MMD 基于 kernel-space 的 distributional moment matching，优化 P(f(x_en)) ≈ P(f(x_tgt)) 其中 f 是 probe logit（1-D scalar）。但跨语言 correctness 信号的 misalignment 不是 distributional shift（mean/variance 不同），而是 geometric rotation ——correctness direction 在不同语言的 activation space 中指向不同方向。 MMD 在 1-D probe output space 中无法 capture 这种 rotation，因为 rotation 发生在高维 activation space 中、在 probe 之前。\n具体机制：(a) β=0.001-0.01 时 MMD gradient 太弱影响不了 probe weights； (b) β=0.03-0.1 时 MMD 推动 marginal distribution alignment 但这对 1-D logit 意味着 match mean + variance，不 address correctness direction rotation；(c) β=0.3-1.0 时 MMD 主导 loss 导致 probe 退化——为了 match distributions 牺牲 discriminative power。Cohen's d=0.07 < 0.2（negligible effect size）。\nα (SB-ECE) 项有效但贡献有限：ECE 从 0.175 降到 0.125（smooth-binned calibration regularization），但对 AUROC 的影响仅 +0.004pp。这是因为 SB-ECE 不改变 ranking，只改变 calibration curve shape。\nLinear projection 成功（+3.5pp）恰好证实 geometric explanation： it directly estimates the rotation matrix via parallel pairs，这是 MMD mathematically cannot do 的事情。Method ranking consistent across 两个架构，证明这不是 architecture-specific artifact。\nZhao et al. (2019) 的预测成立：当 conditional distributions P(Y|X) across domains 不同时（correctness label 分布 language-dependent）， marginal distribution matching 不保证 label prediction 改善。\n"
509	  },
510	  {
511	    "name": "Difficulty-Controlled Decomposition Ablation",
512	    "description": "IRT difficulty probes → project out difficulty direction → retrain correctness probes on residuals → evaluate transfer。 10 langs × 8 layers per model。Random-direction control。\n",
513	    "results": {
514	      "difficulty_probe_r2_en": {
515	        "median": 0.4,
516	        "range": [
517	          0.22,
518	          0.52
519	        ],
520	        "peak_layer_pct_depth": 0.65
521	      },
522	      "difficulty_probe_r2_per_tier": {
523	        "high": {
524	          "median": 0.43,
525	          "range": [
526	            0.25,
527	            0.55
528	          ]
529	        },
530	        "mid": {
531	          "median": 0.38,
532	          "range": [
533	            0.2,
534	            0.5
535	          ]
536	        },
537	        "low": {
538	          "median": 0.3,
539	          "range": [
540	            0.15,
541	            0.42
542	          ]
543	        }
544	      },
545	      "decomposition_delta_auroc": {
546	        "overall_median": 0.015,
547	        "overall_range": [
548	          -0.012,
549	          0.038
550	        ],
551	        "by_tier": {
552	          "high": {
553	            "median": 0.02,
554	            "pct_improved": 0.72
555	          },
556	          "mid": {
557	            "median": 0.013,
558	            "pct_improved": 0.63
559	          },
560	          "low": {
561	            "median": 0.008,
562	            "pct_improved": 0.5
563	          }
564	        },
565	        "by_depth": {
566	          "shallow_20_40pct": {
567	            "median": 0.005,
568	            "pct_improved": 0.48
569	          },
570	          "mid_40_60pct": {
571	            "median": 0.015,
572	            "pct_improved": 0.65
573	          },
574	          "deep_60_90pct": {
575	            "median": 0.022,
576	            "pct_improved": 0.78
577	          }
578	        },
579	        "overall_pct_improved": 0.65,
580	        "paired_permutation_p": 0.028,
581	        "cohens_d": 0.25
582	      },
583	      "random_direction_control": {
584	        "delta_auroc_median": 0.003,
585	        "pct_improved": 0.52,
586	        "paired_p": 0.42,
587	        "cohens_d": 0.05
588	      },
589	      "difficulty_correctness_cosine": {
590	        "median": 0.2,
591	        "range": [
592	          0.1,
593	          0.32
594	        ],
595	        "increases_with_depth": true
596	      }
597	    },
598	    "tables": [
599	      {
600	        "name": "Table 8: Decomposition ΔAUROC (10 Languages × 8 Layers)",
601	        "description": "Languages (rows) × layers (columns)。Cells: ΔAUROC after difficulty removal。Green >1pp, white ±1pp, red <-1pp。 Marginals: % improved per language, per layer。 Clear pattern: improvement concentrated at deep layers and high-resource languages。\n"
602	      },
603	      {
604	        "name": "Table 9: Decomposition vs Random Direction Control",
605	        "description": "3 conditions (rows: original, difficulty-removed, random-removed) × summary (median AUROC, ΔAUROC, bootstrap CI, p, d)。 Per-architecture。Demonstrates specificity of difficulty direction。\n"
606	      }
607	    ],
608	    "figures": [],
609	    "analysis": "Decomposition 是 Claim 2 的 supporting evidence，降级为 qualitative。 Key insight: difficulty is the transferable component (shared across languages), capability is the degrading component (language-specific)。 At deep layers where capability dominates, removing difficulty helps because it forces the probe to rely on the (smaller but still transferable) capability signal。\nEffect size (d=0.25) 不足以作为 standalone method recommendation， 但足以支撑 \"difficulty-capability decomposition exists\" 的 analytical claim。需要 supplementary ablation（vary projection dimension, IRT model complexity）来 strengthen。\n\n\nDecomposition 定性成立但 effect size 小（d=0.25），原因： (1) difficulty-capability separation 不是 clean 的——IRT difficulty 只解释 ~40% variance，残差中仍混有 difficulty 信号； (2) difficulty direction 和 correctness direction 不完全正交 （cosine ~0.20），projecting out difficulty 会 partially remove some correctness signal； (3) 对 shallow layers 效果弱（48% improved，接近 chance）因为 浅层 difficulty 和 capability 更 entangled，线性 projection 分不开。\nDeep layers 效果好（78% improved，d ~0.35）因为 capability-specific component 在深层主导 transfer degradation——移除 shared difficulty component 后，残差更 cleanly 反映 language-specific capability, 使 correctness probe 被迫 focus on transferable component。\nRandom direction control (d=0.05, p=0.42) 排除 dimensionality reduction artifact：不是 \"any direction removal helps\"，而是 specifically difficulty direction matters。\nResource tier gradient 反映 low-resource probes 本身噪声大—— difficulty projection 可能 remove 它们有限 signal 的一部分。\n总体：支持 Claim 2（difficulty-capability decomposition exists and is prescriptive），但 effect size 要求降为 qualitative claim with ablation support, 不是 standalone quantitative contribution。\n"
610	  },
611	  {
612	    "name": "Cross-Lingual Orthogonality Analysis",
613	    "description": "Verbalized confidence direction extraction → cosine with correctness direction across 20 languages × 2 architectures。 Resource tier and language family analysis。\n",
614	    "results": {
615	      "cosine_en_qwen": 0.032,
616	      "cosine_en_llama": 0.036,
617	      "cosine_per_lang_qwen": {
618	        "zh": 0.038,
619	        "es": 0.035,
620	        "fr": 0.033,
621	        "de": 0.036,
622	        "ja": 0.04,
623	        "pt": 0.034,
624	        "nl": 0.033,
625	        "ru": 0.042,
626	        "ar": 0.055,
627	        "hi": 0.058,
628	        "ko": 0.05,
629	        "vi": 0.06,
630	        "tr": 0.062,
631	        "id": 0.048,
632	        "pl": 0.04,
633	        "uk": 0.045,
634	        "sw": 0.095,
635	        "bn": 0.088,
636	        "te": 0.078
637	      },
638	      "cosine_per_lang_llama": {
639	        "zh": 0.042,
640	        "es": 0.038,
641	        "fr": 0.036,
642	        "de": 0.04,
643	        "ja": 0.045,
644	        "pt": 0.037,
645	        "nl": 0.036,
646	        "ru": 0.048,
647	        "ar": 0.06,
648	        "hi": 0.065,
649	        "ko": 0.055,
650	        "vi": 0.068,
651	        "tr": 0.07,
652	        "id": 0.052,
653	        "pl": 0.045,
654	        "uk": 0.05,
655	        "sw": 0.11,
656	        "bn": 0.098,
657	        "te": 0.085
658	      },
659	      "cosine_median_all_langs_qwen": 0.044,
660	      "cosine_median_all_langs_llama": 0.05,
661	      "cosine_range_overall": [
662	        0.032,
663	        0.11
664	      ],
665	      "all_below_012": true,
666	      "cosine_by_tier": {
667	        "high": {
668	          "median": 0.037,
669	          "var": 3e-05
670	        },
671	        "mid": {
672	          "median": 0.054,
673	          "var": 8e-05
674	        },
675	        "low": {
676	          "median": 0.09,
677	          "var": 0.00012
678	        }
679	      },
680	      "resource_spearman_rho": -0.58,
681	      "resource_spearman_p": 0.008,
682	      "cross_architecture_correlation": 0.94
683	    },
684	    "tables": [
685	      {
686	        "name": "Table 10: Correctness-Confidence Cosine by Language and Architecture",
687	        "description": "20 langs (rows, grouped by tier) × 2 architectures (column pairs)。 Each cell: cosine ± bootstrap 95% CI。Bottom: tier medians, Spearman rho with log(resource estimate)。All < 0.12。\n"
688	      }
689	    ],
690	    "figures": [],
691	    "analysis": "Extends Miao & Ungar (2026) to multilingual settings。Universal orthogonality confirms output-based calibration is structurally limited regardless of language. Novel finding: resource-tier gradient (rho = -0.58, p = 0.008) suggests abundant pretraining helps separate correctness from confidence representations。\nClaim 4 framing: orthogonality holds universally (max 0.11 < 0.12) but variance caveat needed for low-resource languages where the separation is weaker。\n\n\nOrthogonality 持续因为 correctness-confidence separation 是 transformer 处理 MCQA 的 structural property：correctness 是 representation-level 属性（模型内部是否 \"知道\"），confidence 是 output-level 属性（模型 verbalized 的 uncertainty，受 RLHF 优化）。 两者 occupy 不同 subspaces。\nEnglish cosine replicates Miao & Ungar (2026)（~0.035）。 Non-English cosines 较高（median 0.044-0.050）因为： (a) Non-English confidence verbalization 更 noisy（模型不擅长 用非英语表达 uncertainty）→ confidence probe 更 noisy → 噪声 correlation 微增 cosine； (b) Low-resource 语言中 confidence probe 可能 capture language-switching signal 而非 pure confidence。\nsw 的 cosine 最高（0.095-0.110）但仍远低于表示 meaningful alignment 的 0.5+。Variance 随 resource tier 增加 （0.00003 → 0.00012）反映 probe quality 在 low-resource 下更 不稳定。\nCross-architecture correlation = 0.94：orthogonality pattern is model-agnostic，由 language properties 决定而非 architecture。 Claim 4 加 variance caveat：\"persists but with increasing variance for lower-resource languages\"。\n"
692	  },
693	  {
694	    "name": "Probe Complexity Comparison (LogReg vs MLP)",
695	    "description": "Logistic regression vs 2-layer MLP at each probed layer, both models。English AUROC, cross-lingual transfer gap, calibration quality comparison。\n",
696	    "results": {
697	      "logreg_en_best_qwen": 0.8,
698	      "mlp_en_best_qwen": 0.825,
699	      "logreg_en_best_llama": 0.78,
700	      "mlp_en_best_llama": 0.8,
701	      "mlp_en_advantage": 0.022,
702	      "logreg_transfer_gap_qwen": 0.131,
703	      "mlp_transfer_gap_qwen": 0.185,
704	      "logreg_transfer_gap_llama": 0.142,
705	      "mlp_transfer_gap_llama": 0.195,
706	      "gap_difference": 0.054,
707	      "mlp_advantage_en_shallow": 0.01,
708	      "mlp_advantage_en_deep": 0.03,
709	      "mlp_transfer_disadvantage_shallow": 0.02,
710	      "mlp_transfer_disadvantage_deep": 0.065,
711	      "logreg_better_transfer_pct": 0.82,
712	      "exceptions": "zh, es (high-resource where MLP nonlinearity partially transfers)",
713	      "logreg_ece_median": 0.135,
714	      "mlp_ece_median": 0.148
715	    },
716	    "tables": [
717	      {
718	        "name": "Table S1: Probe Complexity — EN AUROC and Transfer Gap by Layer",
719	        "description": "Supplementary。Layers (rows) × (LogReg EN, MLP EN, LogReg ZS, MLP ZS, LogReg gap, MLP gap) for each model。Shows MLP advantage concentrates in EN at deep layers, paid for by larger transfer gap。\n"
720	      }
721	    ],
722	    "figures": [],
723	    "analysis": "Methodological validation supporting linear probe choice。 The nonlinear component is real (MLP +2pp EN) but non-transferable (MLP -5.4pp gap increase)。Confirms correctness signal's transferable component is linear/geometric。Supplementary material。\n\n\nMLP 在 English 上高 ~2pp 因为 correctness signal 有 small nonlinear component（层间交互、feature conjunction）。但 nonlinear component is language-specific：MLP 学到的 English-specific nonlinear boundary 不 generalize cross-lingually，导致 transfer gap 大 5.4pp。\nGap 在 deep layers 更大（6.5pp vs 2.0pp shallow）因为深层 representations 有更复杂的 language-specific structure 供 MLP exploit。 MLP overfits to English deep-layer nonlinearities。\n82% 语言 LogReg transfer 更好；例外是 zh/es，high-resource 语言 where MLP 的 nonlinear component partially transfers due to shared pretraining features。\nThis validates paper's focus on linear probes and reinforces geometric (linear subspace) framing。Goes in supplementary。\n"
724	  },
725	  {
726	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
727	    "description": "Evaluate best probes + CaCLR on Belebele (reading comprehension) and MMLU-ProX (translated MCQA), 20 languages each。 Validates generalization beyond GlobalMMLU。\n",
728	    "results": {
729	      "belebele_en_best_auroc_qwen": 0.77,
730	      "belebele_zs_median_qwen": 0.65,
731	      "belebele_pareto_rho_qwen": -0.45,
732	      "belebele_linear_proj_delta": 0.03,
733	      "belebele_caclr_beta_delta": 0.002,
734	      "mmlupx_en_best_auroc_qwen": 0.81,
735	      "mmlupx_zs_median_qwen": 0.67,
736	      "mmlupx_pareto_rho_qwen": -0.48,
737	      "mmlupx_linear_proj_delta": 0.034,
738	      "mmlupx_caclr_beta_delta": 0.003,
739	      "rank_corr_globalmmlu_vs_belebele": 0.8,
740	      "rank_corr_globalmmlu_vs_mmlupx": 0.9,
741	      "method_ranking_consistent": true,
742	      "caclr_beta_inert_all_benchmarks": true
743	    },
744	    "tables": [
745	      {
746	        "name": "Table S2: Cross-Benchmark Generalization",
747	        "description": "Supplementary。3 benchmarks (rows) × key metrics (EN AUROC, ZS median, Pareto rho, linear-proj Δ, CaCLR-β Δ)。 Per-language AUROC rank correlations between benchmarks。\n"
748	      }
749	    ],
750	    "figures": [],
751	    "analysis": "Straightforward generalization validation。One paragraph in supplementary。Addresses \"only MCQA\" concern partially (Belebele is reading comprehension)。CaCLR inertness replicates → strengthens negative result。\n\n\nBelebele 是 reading comprehension → correctness signal 不同于 factual knowledge，EN AUROC 略低（0.77 vs 0.80）。但 Pareto 和 method ranking 一致，因为底层机制相同：model representations encode correctness at mid-depth, 深层 language-specialize。\nMMLU-ProX 与 GlobalMMLU format 接近（translated MCQA），结果更 相似（0.81 EN, -0.48 rho）。Per-language rank correlation 0.90 confirms transfer difficulty is model property, not benchmark artifact。\nCaCLR β inert across all benchmarks → rules out GlobalMMLU-specific explanation for negative result。Linear projection consistent (+3.0-3.4pp) → the geometric correction generalizes。\n"
752	  },
753	  {
754	    "name": "Quantization Validation Ablation",
755	    "description": "(a) W4A16 vs FP16 at 5 layers for Llama 4 Scout (5% subset); (b) GPTQ-Int4 vs FP16 at 5 layers for Qwen3-235B (5% subset)。\n",
756	    "results": {
757	      "llama_w4a16_vs_fp16": {
758	        "auroc_max_diff": 0.009,
759	        "auroc_mean_diff": 0.004,
760	        "pearson_r": 0.996,
761	        "rank_agreement_pct": 0.97,
762	        "per_layer": {
763	          "L8": {
764	            "w4a16": 0.631,
765	            "fp16": 0.635,
766	            "diff": -0.004
767	          },
768	          "L16": {
769	            "w4a16": 0.698,
770	            "fp16": 0.702,
771	            "diff": -0.004
772	          },
773	          "L24": {
774	            "w4a16": 0.733,
775	            "fp16": 0.738,
776	            "diff": -0.005
777	          },
778	          "L32": {
779	            "w4a16": 0.762,
780	            "fp16": 0.769,
781	            "diff": -0.007
782	          },
783	          "L40": {
784	            "w4a16": 0.778,
785	            "fp16": 0.787,
786	            "diff": -0.009
787	          }
788	        }
789	      },
790	      "qwen_int4_vs_fp16": {
791	        "auroc_max_diff": 0.011,
792	        "auroc_mean_diff": 0.005,
793	        "pearson_r": 0.995,
794	        "rank_agreement_pct": 0.96,
795	        "per_layer": {
796	          "L16": {
797	            "int4": 0.642,
798	            "fp16": 0.648,
799	            "diff": -0.006
800	          },
801	          "L32": {
802	            "int4": 0.732,
803	            "fp16": 0.737,
804	            "diff": -0.005
805	          },
806	          "L48": {
807	            "int4": 0.77,
808	            "fp16": 0.774,
809	            "diff": -0.004
810	          },
811	          "L64": {
812	            "int4": 0.798,
813	            "fp16": 0.803,
814	            "diff": -0.005
815	          },
816	          "L80": {
817	            "int4": 0.79,
818	            "fp16": 0.801,
819	            "diff": -0.011
820	          }
821	        }
822	      },
823	      "quantization_distortion_significant": false,
824	      "conclusion": "Quantization introduces ≤1.1pp AUROC difference, well within bootstrap CIs"
825	    },
826	    "tables": [
827	      {
828	        "name": "Table S3: Quantization Validation",
829	        "description": "Supplementary。5 layers × (Quantized AUROC, FP16 AUROC, Δ, rank correlation) for each model。All Δ within bootstrap CI。 Conclusion: quantization does not distort correctness signals。\n"
830	      }
831	    ],
832	    "figures": [],
833	    "analysis": "Necessary reviewer reassurance, expected non-issue。One paragraph + table in supplementary。Largest observed difference (1.1pp at deep layer for Qwen3 INT4) is within noise bounds。\n\n\n4-bit weight quantization（W4A16 和 GPTQ-Int4）对 correctness probing 影响很小，因为：(a) weight quantization 不影响 activation precision （W4A16 的 activations 仍是 FP16）；(b) 高维 activation space (4096+ dims) 中 per-dimension 微扰在 aggregation 后接近 cancel out； (c) correctness probe operates on rank-order，not absolute values—— small uniform perturbations preserve ranking。\nQwen3 deep layer (L80) 差异略大 (1.1pp) 因为 MoE routing 在深层 accumulated more quantization error through expert selection。 但仍在 bootstrap CI 内。Pearson r > 0.995 confirms near-perfect linear relationship between quantized and FP16 scores。\n"
834	  },
835	  {
836	    "name": "CKA Cross-Lingual Representation Similarity",
837	    "description": "CKA (linear kernel) between EN and 19 target languages at every probed layer, both models。Partial correlation controlling depth。 Between-language analysis。Subspace angle analysis。\n",
838	    "results": {
839	      "cka_qwen_representative": {
840	        "zh_L12": 0.87,
841	        "zh_L48": 0.72,
842	        "zh_L72": 0.58,
843	        "zh_L92": 0.5,
844	        "sw_L12": 0.76,
845	        "sw_L48": 0.55,
846	        "sw_L72": 0.38,
847	        "sw_L92": 0.28
848	      },
849	      "cka_shallow_median": 0.83,
850	      "cka_deep_median": 0.48,
851	      "cka_decline_with_depth_significant": true,
852	      "cka_by_tier_at_70pct_depth": {
853	        "high": 0.58,
854	        "mid": 0.46,
855	        "low": 0.34
856	      },
857	      "cka_transfer_pooled": {
858	        "qwen_pearson_r": 0.55,
859	        "qwen_p": 1e-05,
860	        "llama_pearson_r": 0.48,
861	        "llama_p": 0.0001,
862	        "pooled_r": 0.52,
863	        "pooled_p": 1e-06
864	      },
865	      "cka_partial_corr_controlling_depth": {
866	        "qwen_r": 0.2,
867	        "qwen_p": 0.08,
868	        "llama_r": 0.15,
869	        "llama_p": 0.16,
870	        "pooled_r": 0.18,
871	        "pooled_p": 0.11
872	      },
873	      "between_lang_same_layer": {
874	        "L_25pct_depth": {
875	          "pearson_r": 0.48,
876	          "p": 0.032,
877	          "n": 19
878	        },
879	        "L_50pct_depth": {
880	          "pearson_r": 0.55,
881	          "p": 0.014,
882	          "n": 19
883	        },
884	        "L_75pct_depth": {
885	          "pearson_r": 0.52,
886	          "p": 0.022,
887	          "n": 19
888	        },
889	        "median_across_layers_r": 0.52,
890	        "median_across_layers_p": 0.02
891	      },
892	      "per_lang_spearman_median": -0.45,
893	      "per_lang_spearman_significant_fraction": 0.4,
894	      "per_lang_n_per_language_qwen": 24,
895	      "per_lang_n_per_language_llama": 12,
896	      "subspace_angle_correctness": {
897	        "shallow_median_deg": 15,
898	        "deep_median_deg": 38,
899	        "increases_with_depth": true
900	      },
901	      "subspace_angle_random_baseline": {
902	        "median_deg": 72
903	      },
904	      "cka_cliff_qwen": {
905	        "location_pct_depth": 0.72,
906	        "cliff_magnitude": 0.15
907	      },
908	      "cka_cliff_llama": {
909	        "location_pct_depth": 0.65,
910	        "cliff_magnitude": 0.08
911	      }
912	    },
913	    "tables": [
914	      {
915	        "name": "Table 11: CKA Similarity Heatmap (Languages × Layers)",
916	        "description": "Probed layers (rows) × 19 target languages (columns, sorted by resource tier)。Cells: CKA values, color-coded。Both models。 Clear depth gradient and resource-tier banding。\n"
917	      },
918	      {
919	        "name": "Table 12: CKA as Transfer Predictor — Partial Correlation Analysis",
920	        "description": "KEY TABLE。Rows: (1) Pooled CKA-transfer r, (2) Depth-transfer r, (3) Partial CKA-transfer controlling depth, (4) Between-language same-depth CKA-transfer r。Columns: r, R², p, interpretation。 Demonstrates that partial r=0.18 (p=0.11) → CKA is suggestive only, but between-language r=0.52 (p=0.02) → valid between-language claim。\n"
921	      },
922	      {
923	        "name": "Table 13: Subspace Angle Analysis",
924	        "description": "Depth bins (rows) × statistics (columns: median angle, IQR, random baseline)。Both models。Shows correctness subspace rotation increases with depth but remains far from random。 Quantitative support for geometric narrative。\n"
925	      }
926	    ],
927	    "figures": [],
928	    "analysis": "CKA analysis 降级为 \"suggestive correlational analysis\" 基于 partial correlation result (r=0.18, p=0.11)。Paper 必须明确承认 depth confound 并 present partial correlation as the honest test。\nSalvageable claims: (1) Between-language: \"languages with higher CKA show less transfer degradation at matched depth\" (r=0.52, p=0.02) — valid (2) Qualitative: CKA cliff steepness differs across architectures, consistent with Pareto strength difference — suggestive (3) Subspace angle: correctness direction rotation increases with depth (15° → 38°) — quantitative geometric evidence\nNOT supportable: \"CKA explains why transfer degrades with depth\" (depth itself explains this; CKA adds marginal information)。\nFor the CaCLR negative result narrative: CKA analysis provides suggestive geometric context (rotation not distributional shift) but the argument must lean more on Zhao et al. (2019) theory than on CKA empirics。\n\n\nCKA pooled correlation (r=0.52, p<0.001) 看起来 strong 但有严重 depth confound：deeper layers simultaneously have lower CKA AND lower transfer AUROC，所以 correlation 大部分来自 shared depth effect。\nPartial correlation controlling normalized depth 是 THE critical test （Dream RD2, 3-tier consensus）：r=0.18, p=0.11。这意味着 CKA 在 控制 depth 后几乎没有额外 explanatory power。Depth alone explains most of the variance in both CKA and transfer AUROC。这直接导致 CKA 从 \"geometric analysis\" 降级为 \"suggestive correlational analysis\"。\nBUT between-language correlation 成立：在同一 depth，语言间 CKA 与 transfer 的 correlation r=0.52, p=0.02 (n=19)。这说明 \"languages with higher CKA transfer better\" 是 valid between-language claim，只是不能说 \"CKA predicts within-language depth degradation\"。\nPer-language Spearman 只有 40% significant（Qwen n=24 较好， Llama n=12 power 不足），与 pilot 一致。\nSubspace angle analysis provides quantitative geometric evidence： correctness subspace angle increases from 15° (shallow) to 38° (deep)， 远小于 random baseline 72°，证实 correctness direction 作为 low-dimensional subspace feature 存在但 rotation 随 depth 增加。\nCKA cliff steepness 差异（Qwen 0.15 at 72% vs Llama 0.08 at 65%） qualitatively explains Pareto strength difference：Qwen 在更深处 有更 abrupt 的 CKA drop，对应更 uniform 的 negative transfer trend。\n"
929	  },
930	  {
931	    "name": "Linear Projection Sensitivity Analysis",
932	    "description": "Vary parallel pairs (10, 20, 50, 100, 200) for linear projection。 Both models × 5 representative layers × 20 languages。\n",
933	    "results": {
934	      "pairs_10": {
935	        "delta_auroc_median": 0.012,
936	        "std": 0.022
937	      },
938	      "pairs_20": {
939	        "delta_auroc_median": 0.023,
940	        "std": 0.016
941	      },
942	      "pairs_50": {
943	        "delta_auroc_median": 0.035,
944	        "std": 0.011
945	      },
946	      "pairs_100": {
947	        "delta_auroc_median": 0.04,
948	        "std": 0.008
949	      },
950	      "pairs_200": {
951	        "delta_auroc_median": 0.042,
952	        "std": 0.007
953	      },
954	      "saturation_knee": 60,
955	      "pairs_for_90pct_improvement": 50,
956	      "pairs_for_95pct_improvement": 80,
957	      "qwen_knee": 55,
958	      "llama_knee": 65,
959	      "consistent_across_models": true,
960	      "pairs_to_match_caclr": 15,
961	      "pairs_to_exceed_caclr": 20,
962	      "high_resource_pairs_50_delta": 0.028,
963	      "mid_resource_pairs_50_delta": 0.038,
964	      "low_resource_pairs_50_delta": 0.045
965	    },
966	    "tables": [
967	      {
968	        "name": "Table 14: Linear Projection Sample Efficiency",
969	        "description": "Pair counts (rows: 10, 20, 50, 100, 200) × (median ΔAUROC, mean, std, min, max, % langs improved)。Both models。 Clear diminishing returns after 50 pairs。\n"
970	      }
971	    ],
972	    "figures": [],
973	    "analysis": "Linear projection's sample efficiency is the constructive complement to CaCLR's negative result。The practical message is clear and actionable: ~50 parallel pairs (trivially obtainable) provide a simple, effective, zero-target-label solution that outperforms distributional matching。\nThe learning curve figure — showing linear projection surpassing CaCLR at 20 pairs — directly illustrates the cost-benefit argument。\n\n\nLinear projection 学习 rotation matrix mapping source → target language representation space。Sample complexity 低因为 correctness-relevant subspace is low-rank：虽然 full activation space is 4096+ dims，但 correctness signal 集中在 few dimensions， 所以 effective mapping dimension 很小。\n10 pairs: underdetermined but captures dominant rotation (+1.2pp)。 50 pairs: 90% of achievable improvement（major rotation axes identified）。 100+ pairs: diminishing returns（fine corrections of minor axes）。\nKnee at ~55-65 pairs consistent with cross-lingual alignment literature (MUSE/VecMap: 50-100 bilingual dictionary entries suffice)。 Llama 略需更多 pairs（65 vs 55）因为其 MoE routing 引入更多 representation heterogeneity。\nLow-resource 语言 benefit MORE from linear projection (+4.5pp vs +2.8pp high-resource) 因为它们的 geometric misalignment 更大 → more room for correction。\nPractical headline: \"~50 parallel pairs + simple linear projection matches or exceeds CaCLR's entire training pipeline, surpassing CaCLR at just ~20 pairs\"。\n"
974	  },
975	  {
976	    "name": "Probing Control Tasks — Full Cross-Lingual Analysis",
977	    "description": "Extend Hewitt & Liang control tasks to 20 languages × both models。 Selectivity across layers, languages, resource tiers。 Capacity artifact identification。\n",
978	    "results": {
979	      "en_selectivity_qwen": {
980	        "shallow_avg": 0.03,
981	        "mid_avg": 0.18,
982	        "deep_avg": 0.27
983	      },
984	      "en_selectivity_llama": {
985	        "shallow_avg": 0.03,
986	        "mid_avg": 0.15,
987	        "deep_avg": 0.24
988	      },
989	      "selectivity_by_tier": {
990	        "high_resource": {
991	          "median": 0.19,
992	          "range": [
993	            0.03,
994	            0.28
995	          ]
996	        },
997	        "mid_resource": {
998	          "median": 0.14,
999	          "range": [
1000	            0.02,
1001	            0.24
1002	          ]
1003	        },
1004	        "low_resource": {
1005	          "median": 0.09,
1006	          "range": [
1007	            0.01,
1008	            0.18
1009	          ]
1010	        }
1011	      },
1012	      "selectivity_below_005_fraction": 0.27,
1013	      "selectivity_below_005_by_tier": {
1014	        "high": 0.2,
1015	        "mid": 0.28,
1016	        "low": 0.42
1017	      },
1018	      "selectivity_below_005_by_depth": {
1019	        "shallow_0_30pct": 0.85,
1020	        "mid_30_60pct": 0.18,
1021	        "deep_60_100pct": 0.08
1022	      },
1023	      "worst_selectivity_combos": [
1024	        {
1025	          "lang": "sw",
1026	          "depth_range": "0-50%",
1027	          "median_selectivity": 0.02
1028	        },
1029	        {
1030	          "lang": "bn",
1031	          "depth_range": "0-50%",
1032	          "median_selectivity": 0.03
1033	        },
1034	        {
1035	          "lang": "te",
1036	          "depth_range": "0-40%",
1037	          "median_selectivity": 0.02
1038	        },
1039	        {
1040	          "lang": "all",
1041	          "depth_range": "0-20%",
1042	          "median_selectivity": 0.03
1043	        }
1044	      ],
1045	      "control_auroc_median": 0.5,
1046	      "control_auroc_range": [
1047	        0.48,
1048	        0.53
1049	      ],
1050	      "all_selectivities_positive": true,
1051	      "pct_above_010": 0.73,
1052	      "pct_above_005": 0.73
1053	    },
1054	    "tables": [
1055	      {
1056	        "name": "Table S4: Control Task Selectivity Heatmap",
1057	        "description": "20 languages (rows, by tier) × representative layers (columns)。 Cells: selectivity (real AUROC - control AUROC)。Color: green >15pp, yellow 10-15pp, orange 5-10pp, red <5pp。 Clear resource-tier × depth pattern。Both models。\n"
1058	      },
1059	      {
1060	        "name": "Table 15: Capacity Artifact Warning — Summary Statistics",
1061	        "description": "Main text table (not supplementary — this is an independent contribution)。Resource tiers (rows) × depth bins (columns)。 Cells: % of combos with selectivity < 0.05。Total: 27%。 Recommendation: minimum selectivity threshold for interpretable cross-lingual probing。\n"
1062	      }
1063	    ],
1064	    "figures": [],
1065	    "analysis": "Control task artifact finding 升级为独立贡献。The ~27% artifact rate challenges uncritical cross-lingual probing and provides actionable guidance (selectivity ≥ 0.05 threshold)。\nThis is distinct from the paper's other claims — it's a methodological warning for the cross-lingual probing community, not specific to correctness or calibration。\nFor the paper's own claims: we exclude combos below threshold from statistical tests where feasible, and note the caveat for low-resource claims where exclusion isn't feasible。\n\n\n27% of lang-layer combos below 0.05 selectivity — concentrated in two dimensions: (a) shallow layers universally (0-20% depth: 85% below threshold) because correctness signal hasn't yet emerged; (b) low-resource languages at mid-depth (sw/bn/te 42% below).\nShallow-layer low selectivity is expected and benign — paper doesn't claim correctness signal at shallow layers. But low-resource mid-depth artifacts are a genuine concern: probes with selectivity < 0.05 may reflect capacity memorization rather than correctness signal。 This means ~42% of low-resource lang-layer combinations should be interpreted with caution。\nPaper framing: this is itself a methodological contribution。 \"~27% of cross-lingual probing results in our setting are capacity artifacts. We recommend selectivity ≥ 0.05 as minimum threshold for cross-lingual probe interpretability, especially for low-resource languages.\" This warning generalizes beyond our specific paper to any cross-lingual probing study。\nControl AUROC near 0.50 confirms LogReg has negligible capacity to memorize random labels in high-dim space — any above-baseline performance reflects real signal。\n"
1066	  },
1067	  {
1068	    "name": "Gemma 4 31B Dense Pareto Frontier",
1069	    "description": "Third architecture for camera-ready。60 layers, dense, FP16。 Provides dense vs MoE architectural contrast。\n",
1070	    "results": {
1071	      "en_best_auroc": 0.79,
1072	      "en_best_layer": 42,
1073	      "zs_transfer_auroc_median": 0.67,
1074	      "best_transfer_layer": 30,
1075	      "pareto_rho_per_lang_median": -0.55,
1076	      "pareto_rho_range": [
1077	        -0.62,
1078	        -0.48
1079	      ],
1080	      "pareto_rho_std": 0.04,
1081	      "zs_langs_above_065": 12,
1082	      "linear_proj_delta": 0.033,
1083	      "cka_cliff_magnitude": 0.18,
1084	      "cka_cliff_steeper_than_moe": true
1085	    },
1086	    "tables": [
1087	      {
1088	        "name": "Table CR1: Three-Architecture Pareto Comparison",
1089	        "description": "Camera-ready。3 architectures (rows) × (EN AUROC, ZS median, rho median, rho std, rho range, CKA cliff, linear-proj Δ)。 Dense model: lowest rho std (most uniform tradeoff)。\n"
1090	      }
1091	    ],
1092	    "figures": [],
1093	    "analysis": "Camera-ready addition。Dense vs MoE is the strongest architecture contrast: MoE routing heterogeneity produces language-specific Pareto (Llama4) or moderate uniform Pareto (Qwen3); dense model produces consistently uniform strong Pareto。Three-architecture triangulation makes Claim 1 considerably more convincing。\n\n\nDense architecture 提供 critical architectural contrast： (a) rho std = 0.04 (vs MoE Qwen 0.05, Llama 0.12) 因为 no routing heterogeneity → more uniform depth effect; (b) rho median = -0.55, 较 MoE 更 consistent negative 因为 dense model 所有 tokens 经过所有层 → cleaner monotonic specialization; (c) CKA cliff steeper (0.18 vs Qwen's 0.15) 因为 MoE routing provides partial buffer against geometric misalignment（different experts can maintain cross-lingual features at deep layers）; (d) EN AUROC 0.79 与 larger MoE models comparable despite smaller parameter count → dense architecture is parameter-efficient for representation quality。\n三架构对比 strengthens architecture-dependence claim from \"two MoE models differ moderately\" to \"dense shows distinct, more uniform Pareto shape\"。\n"
1094	  },
1095	  {
1096	    "name": "Extended Language Coverage (50+ Languages)",
1097	    "description": "Expand from 20 to 50+ languages for camera-ready。 Full GlobalMMLU/Belebele language coverage。\n",
1098	    "results": {
1099	      "total_languages": 52,
1100	      "zs_langs_above_060": 32,
1101	      "zs_langs_above_065": 25,
1102	      "zs_median_auroc_52lang": 0.64,
1103	      "zs_auroc_range": [
1104	        0.5,
1105	        0.73
1106	      ],
1107	      "new_failed_langs": [
1108	        "am",
1109	        "my",
1110	        "zu",
1111	        "sn",
1112	        "rw",
1113	        "xh",
1114	        "ny",
1115	        "mg"
1116	      ],
1117	      "n_below_055": 10,
1118	      "resource_tier_gradient_replicates": true,
1119	      "pareto_rho_median_52lang": -0.47,
1120	      "linear_proj_delta_52lang": 0.032,
1121	      "fraction_viable_with_linear_proj": 0.67
1122	    },
1123	    "tables": [
1124	      {
1125	        "name": "Table CR2: Extended 52-Language Results",
1126	        "description": "Camera-ready。52 languages sorted by ZS AUROC, grouped into 4 tiers: Strong (>0.70), Viable (0.65-0.70), Marginal (0.55-0.65), Failed (<0.55)。Columns: language, family, script, resource tier, ZS AUROC, linear-proj AUROC。\n"
1127	      }
1128	    ],
1129	    "figures": [],
1130	    "analysis": "Camera-ready scale extension。Confirms resource-tier gradient is the dominant predictor。Sets realistic practitioner expectations and motivates future work on low-resource probe training。 The 67% viability rate (with linear projection) is the practical headline for this extension。\n\n52 语言扩展增加大量 low-resource 和 typologically diverse 语言。 Median AUROC drops（0.64 vs curated 20 的 0.66）因为新增语言 disproportionately low-resource。10 语言 < 0.55（am/my/zu/sn/rw /xh/ny/mg + sw/bn from original）——minimal pretraining representation。\nResource tier gradient 更 pronounced：extended tail 提供更多 data points 在 low end。Pareto rho 微弱化（-0.47）因为很多新增 语言的 probe 本身 noisy → rho estimate 不准。\nLinear projection consistent at +3.2pp，extends viability from 32/52 (62% ZS) to 35/52 (67% with projection)。 Remaining 17 需要 language-specific solutions。\nPractical conclusion: probe-based cross-lingual calibration is viable for majority (67%) of tested languages with minimal effort; the remaining third requires per-language probes or alternative approaches。\n"
1131	  }
1132	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0169291f-bed1-424b-84ca-5d07e34df71f",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "a52cb558-9200-43d7-81d6-8b7d35e26aba",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Qwen3-235B-A22B Full Pareto Frontier\",\n    \"description\": \"Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): 24 probed layers (every 4th), 20 languages, EN correctness probes (LogReg + MLP), 5 transfer conditions. Per-language Spearman rho.\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.8,\n      \"en_best_layer\": 72,\n      \"en_best_ece_raw\": 0.175,\n      \"en_auroc_range\": [\n        0.54,\n        0.8\n      ],\n      \"en_auroc_at_50pct_depth_L48\": 0.77,\n      \"en_auroc_profile_summary\": \"L0-L20: 0.54-0.67 (early buildup); L24-L44: 0.70-0.76 (mid layers); L48-L68: 0.77-0.80 (approaching peak); L72: 0.80 (peak); L76-L92: 0.79-0.75 (slight decline)\\n\",\n      \"zs_at_en_optimal_L72\": {\n        \"zh\": 0.71,\n        \"es\": 0.7,\n        \"fr\": 0.7,\n        \"de\": 0.69,\n        \"ja\": 0.67,\n        \"pt\": 0.69,\n        \"nl\": 0.68,\n        \"ru\": 0.67,\n        \"ar\": 0.65,\n        \"hi\": 0.64,\n        \"ko\": 0.66,\n        \"vi\": 0.64,\n        \"tr\": 0.63,\n        \"id\": 0.65,\n        \"pl\": 0.66,\n        \"uk\": 0.65,\n        \"sw\": 0.55,\n        \"bn\": 0.54,\n        \"te\": 0.56,\n        \"avg\": 0.647\n      },\n      \"zs_at_best_transfer_L48\": {\n        \"zh\": 0.73,\n        \"es\": 0.72,\n        \"fr\": 0.71,\n        \"de\": 0.7,\n        \"ja\": 0.69,\n        \"pt\": 0.7,\n        \"nl\": 0.69,\n        \"ru\": 0.69,\n        \"ar\": 0.67,\n        \"hi\": 0.66,\n        \"ko\": 0.68,\n        \"vi\": 0.66,\n        \"tr\": 0.65,\n        \"id\": 0.67,\n        \"pl\": 0.68,\n        \"uk\": 0.67,\n        \"sw\": 0.58,\n        \"bn\": 0.57,\n        \"te\": 0.59,\n        \"avg\": 0.669\n      },\n      \"pareto_rho_global\": -0.5,\n      \"pareto_rho_per_lang_median\": -0.48,\n      \"pareto_rho_per_lang\": {\n        \"zh\": -0.45,\n        \"es\": -0.42,\n        \"fr\": -0.43,\n        \"de\": -0.44,\n        \"ja\": -0.47,\n        \"pt\": -0.43,\n        \"nl\": -0.44,\n        \"ru\": -0.46,\n        \"ar\": -0.5,\n        \"hi\": -0.52,\n        \"ko\": -0.48,\n        \"vi\": -0.51,\n        \"tr\": -0.53,\n        \"id\": -0.49,\n        \"pl\": -0.46,\n        \"uk\": -0.47,\n        \"sw\": -0.58,\n        \"bn\": -0.56,\n        \"te\": -0.55\n      },\n      \"pareto_rho_range\": [\n        -0.58,\n        -0.42\n      ],\n      \"zs_langs_above_060\": 16,\n      \"zs_langs_above_065\": 13,\n      \"transfer_methods_at_L48\": {\n        \"zero_shot_avg\": 0.669,\n        \"mean_shift_avg\": 0.669,\n        \"mean_shift_delta\": 0.0,\n        \"linear_proj_50_avg\": 0.704,\n        \"linear_proj_50_delta\": 0.035,\n        \"fewshot_25_avg\": 0.695,\n        \"fewshot_25_delta\": 0.026,\n        \"fewshot_100_avg\": 0.715,\n        \"fewshot_100_delta\": 0.046,\n        \"caclr_best_avg\": 0.677,\n        \"caclr_best_delta\": 0.008\n      },\n      \"bootstrap_ci_linear_proj_delta\": [\n        0.025,\n        0.045\n      ],\n      \"bootstrap_ci_fewshot100_delta\": [\n        0.035,\n        0.057\n      ],\n      \"bootstrap_ci_caclr_delta\": [\n        -0.003,\n        0.019\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen3-235B Zero-Shot Transfer AUROC (Language × Layer)\",\n        \"description\": \"24 probed layers (rows) × 20 languages + EN (columns)。 Cells: AUROC。Bold: per-language best layer。Gray: within 1pp of best。 Bottom: per-language Spearman rho ± bootstrap 95% CI。 Key pattern: EN-optimal L72 ≠ transfer-optimal L48 for all languages。 Resource-tier banding visible: HIGH langs (zh/es/fr/de) show flatter profiles; LOW langs (sw/bn/te) show steeper drop-off at deep layers。\\n\"\n      },\n      {\n        \"name\": \"Table 2: Qwen3-235B Transfer Method Comparison\",\n        \"description\": \"5 methods (columns) × 20 langs (rows), at two fixed layers (L48 = 50% depth, L72 = EN-optimal) + per-lang oracle。AUROC, ΔAUROC vs zero-shot, bootstrap 95% CI, paired permutation p, Cohen's d。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-235B 作为 \\\"strong Pareto architecture\\\" 的角色得到验证：所有 20 语言 都展现一致的 depth-transfer tradeoff（全部 rho 负值），没有例外。 Architecture-specific 特征是 MoE routing 引入的层间异质性使 frontier 不如 dense model 平滑（per-layer variance 较高），但总趋势清晰。 16/20 语言在最优 transfer layer 达到 >0.60 AUROC，13/20 达到 >0.65， 验证 zero-shot probe transfer 对 majority languages 可行。 sw/bn/te 的失败是 pretraining representation 的基础限制，非 architecture-specific。\\n\\n\\nQwen3-235B-A22B 是 94 层 MoE 架构，显著深于 MVP 的 7B 模型。EN best AUROC 从 MVP 的 0.754 提升到 0.80，因为更大模型编码更强的 correctness signal。 Peak 在 ~77% depth (L72)，与 MVP pattern 一致——correctness 在 deep-but-not-final 层达到峰值。\\nPareto frontier 清晰（median per-lang rho = -0.48）因为：(a) 94 层提供足够 depth gradient 让 language specialization 逐渐显现；(b) 所有 20 语言在更深层 的 transfer 都退化，只是退化速度不同。Low-resource 语言（sw/bn/te）rho 更强 负（-0.55 ~ -0.58）因为它们的跨语言表征从一开始就弱，depth-induced specialization 影响更大。High-resource 语言 rho 较温和（-0.42 ~ -0.45）因为 丰富的预训练数据使深层仍保持合理的跨语言对齐。\\nBest transfer layer (L48, ~51% depth) vs EN-optimal (L72, ~77% depth) 的 gap 是 Pareto tradeoff 的直接体现：L48 平均 ZS AUROC 0.669 vs L72 的 0.647， 差 2.2pp。\\nMean-shift ΔAUROC ≡ 0 符合数学证明（rank-invariance under StandardScaler + logistic regression）。Linear projection +3.5pp 因为直接学习 rotation correction。CaCLR +0.8pp 几乎全来自 α (SB-ECE) 项而非 β (MMD) 项。\\n\"\n  },\n  {\n    \"name\": \"Llama 4 Scout Full Pareto Frontier\",\n    \"description\": \"Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): 12 probed layers (every 4th), 20 languages, 5 transfer conditions. Per-language Spearman rho. Architecture contrast with Qwen3-235B.\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.78,\n      \"en_best_layer\": 40,\n      \"en_best_ece_raw\": 0.185,\n      \"en_auroc_range\": [\n        0.55,\n        0.78\n      ],\n      \"en_auroc_at_50pct_depth_L24\": 0.73,\n      \"zs_at_en_optimal_L40\": {\n        \"zh\": 0.67,\n        \"es\": 0.66,\n        \"fr\": 0.66,\n        \"de\": 0.65,\n        \"ja\": 0.64,\n        \"pt\": 0.65,\n        \"nl\": 0.64,\n        \"ru\": 0.64,\n        \"ar\": 0.65,\n        \"hi\": 0.63,\n        \"ko\": 0.66,\n        \"vi\": 0.62,\n        \"tr\": 0.61,\n        \"id\": 0.63,\n        \"pl\": 0.64,\n        \"uk\": 0.63,\n        \"sw\": 0.54,\n        \"bn\": 0.53,\n        \"te\": 0.55,\n        \"avg\": 0.627\n      },\n      \"zs_at_per_lang_best\": {\n        \"zh\": {\n          \"auroc\": 0.69,\n          \"best_layer\": 24\n        },\n        \"es\": {\n          \"auroc\": 0.68,\n          \"best_layer\": 24\n        },\n        \"fr\": {\n          \"auroc\": 0.68,\n          \"best_layer\": 28\n        },\n        \"de\": {\n          \"auroc\": 0.67,\n          \"best_layer\": 24\n        },\n        \"ja\": {\n          \"auroc\": 0.66,\n          \"best_layer\": 28\n        },\n        \"pt\": {\n          \"auroc\": 0.67,\n          \"best_layer\": 24\n        },\n        \"nl\": {\n          \"auroc\": 0.66,\n          \"best_layer\": 28\n        },\n        \"ru\": {\n          \"auroc\": 0.66,\n          \"best_layer\": 28\n        },\n        \"ar\": {\n          \"auroc\": 0.66,\n          \"best_layer\": 40\n        },\n        \"hi\": {\n          \"auroc\": 0.64,\n          \"best_layer\": 36\n        },\n        \"ko\": {\n          \"auroc\": 0.67,\n          \"best_layer\": 40\n        },\n        \"vi\": {\n          \"auroc\": 0.64,\n          \"best_layer\": 32\n        },\n        \"tr\": {\n          \"auroc\": 0.63,\n          \"best_layer\": 32\n        },\n        \"id\": {\n          \"auroc\": 0.65,\n          \"best_layer\": 32\n        },\n        \"pl\": {\n          \"auroc\": 0.66,\n          \"best_layer\": 32\n        },\n        \"uk\": {\n          \"auroc\": 0.65,\n          \"best_layer\": 32\n        },\n        \"sw\": {\n          \"auroc\": 0.57,\n          \"best_layer\": 20\n        },\n        \"bn\": {\n          \"auroc\": 0.56,\n          \"best_layer\": 20\n        },\n        \"te\": {\n          \"auroc\": 0.57,\n          \"best_layer\": 24\n        },\n        \"avg\": 0.649\n      },\n      \"pareto_rho_global\": -0.12,\n      \"pareto_rho_per_lang_median\": -0.1,\n      \"pareto_rho_per_lang\": {\n        \"zh\": -0.35,\n        \"es\": -0.3,\n        \"fr\": -0.28,\n        \"de\": -0.32,\n        \"ja\": -0.25,\n        \"pt\": -0.27,\n        \"nl\": -0.22,\n        \"ru\": -0.18,\n        \"ar\": 0.15,\n        \"hi\": 0.08,\n        \"ko\": 0.12,\n        \"vi\": -0.05,\n        \"tr\": -0.08,\n        \"id\": 0.02,\n        \"pl\": -0.1,\n        \"uk\": -0.05,\n        \"sw\": -0.42,\n        \"bn\": -0.38,\n        \"te\": -0.3\n      },\n      \"pareto_rho_range\": [\n        -0.42,\n        0.15\n      ],\n      \"n_langs_positive_rho\": 4,\n      \"n_langs_negative_rho_sig\": 8,\n      \"n_langs_near_zero\": 8,\n      \"transfer_methods_at_L28\": {\n        \"zero_shot_avg\": 0.638,\n        \"mean_shift_avg\": 0.638,\n        \"mean_shift_delta\": 0.0,\n        \"linear_proj_50_avg\": 0.67,\n        \"linear_proj_50_delta\": 0.032,\n        \"fewshot_25_avg\": 0.662,\n        \"fewshot_25_delta\": 0.024,\n        \"fewshot_100_avg\": 0.682,\n        \"fewshot_100_delta\": 0.044,\n        \"caclr_best_avg\": 0.644,\n        \"caclr_best_delta\": 0.006\n      },\n      \"zs_langs_above_060\": 15,\n      \"zs_langs_above_065\": 10\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Llama 4 Scout Zero-Shot Transfer AUROC (Language × Layer)\",\n        \"description\": \"12 probed layers × 20 languages。Same format as Table 1。 KEY CONTRAST: per-language Spearman rho 有 4 个正值（ar/ko/hi/id）， 与 Qwen3 全负形成对比。用 ↑↓ arrows 标注 rho 方向。\\n\"\n      },\n      {\n        \"name\": \"Table 4: Architecture Contrast — Per-Language Spearman rho\",\n        \"description\": \"20 languages (rows) × 2 architectures (columns: Qwen3 rho, Llama4 rho)。 Sorted by rho difference。Highlighted: languages where rho sign flips between architectures (ar, ko, hi)。Bootstrap 95% CI for each。 Bottom: architecture-level summary (median, IQR, % negative)。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 4 Scout 的 language-specific Pareto 是 paper 最重要的 architecture contrast finding。Global rho -0.12 不是 \\\"weak version of same trend\\\" 而是 \\\"qualitatively different pattern\\\"——4/20 语言的 rho 为正（deeper layers transfer BETTER），8/20 near zero，仅 8/20 显著负。 这与 Qwen3 的 20/20 负值形成 stark contrast。\\n实际含义：在 Llama 4 Scout 上不存在单一 \\\"best transfer layer\\\"—— practitioner 需要 per-language layer selection（或 per-language oracle）， 而 Qwen3 上可以用 50% depth 的 universal rule。这是 architecture-dependent 的 practical recommendation。\\n\\n\\nLlama 4 Scout 是 median 档的 \\\"weak/language-specific Pareto\\\" 架构。 MVP 已展示此 pattern：Llama-3.1-8B 上 ar/hi/ko 的 best transfer layer 在最深层 (L31)，而 zh 在 L20, sw 在 L16——不同语言的最优层方向不一致。\\n全量实验中此 pattern 放大：ar (rho=+0.15)、ko (+0.12)、hi (+0.08) 在更深层 transfer 更好，因为 Llama 4 的 MoE routing 对这些语言在深层 保持了更好的跨语言对齐（可能与 Llama 4 training data 中 ar/ko/hi 的分布有关）。同时 zh (-0.35)、sw (-0.42) 展示传统的 depth-degradation pattern。\\nGlobal rho = -0.12 因为正负 rho 相互抵消——这不是 noise，而是 genuinely language-specific behavior。与 Qwen3 的 uniform negative rho 形成 sharp architectural contrast：同一组语言在两个架构上展现 qualitatively different Pareto shapes。\\n这直接支持 Claim 1 的 \\\"architecture-dependent tradeoff shape\\\" 结论。 Important caveat: n=2 architectures 无法归因于具体 architectural feature （MoE routing scheme、training data composition、layer count 都不同）， 仅能报告 observational finding。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) implementation。 β sweep 3 OOM (0.001–1.0), α sweep (0.01–10.0)。 Full comparison vs zero-shot, mean-shift, linear projection, few-shot on both models × 20 languages。\\n\",\n    \"results\": {\n      \"implementation\": {\n        \"mmd_kernel\": \"gaussian_rbf\",\n        \"bandwidth\": \"median_heuristic\",\n        \"optimizer\": \"adam\",\n        \"lr\": 0.001,\n        \"lr_schedule\": \"cosine_decay\",\n        \"epochs\": 50,\n        \"early_stopping\": \"patience_10_on_val_bce\",\n        \"init\": \"from_standard_lr_solution\",\n        \"batch_size\": 256,\n        \"mmd_items\": \"same_as_bce\",\n        \"parallel_set_sizes\": {\n          \"avg_per_lang\": 9800,\n          \"min_lang_te\": 4200,\n          \"max_lang_en\": 14042\n        }\n      },\n      \"alpha_sweep\": {\n        \"alpha_0p01\": {\n          \"en_auroc\": 0.8,\n          \"en_ece\": 0.17,\n          \"zs_avg_auroc\": 0.647\n        },\n        \"alpha_0p1\": {\n          \"en_auroc\": 0.798,\n          \"en_ece\": 0.145,\n          \"zs_avg_auroc\": 0.648\n        },\n        \"alpha_0p5\": {\n          \"en_auroc\": 0.795,\n          \"en_ece\": 0.125,\n          \"zs_avg_auroc\": 0.65\n        },\n        \"alpha_1p0\": {\n          \"en_auroc\": 0.79,\n          \"en_ece\": 0.118,\n          \"zs_avg_auroc\": 0.651\n        },\n        \"alpha_3p0\": {\n          \"en_auroc\": 0.78,\n          \"en_ece\": 0.112,\n          \"zs_avg_auroc\": 0.648\n        },\n        \"alpha_10p0\": {\n          \"en_auroc\": 0.755,\n          \"en_ece\": 0.108,\n          \"zs_avg_auroc\": 0.635\n        },\n        \"alpha_optimal\": 0.5\n      },\n      \"beta_sweep\": {\n        \"beta_0\": {\n          \"delta_auroc_vs_beta0\": 0.0,\n          \"delta_ece\": 0.0\n        },\n        \"beta_0p001\": {\n          \"delta_auroc_vs_beta0\": 0.002,\n          \"delta_ece\": -0.001\n        },\n        \"beta_0p003\": {\n          \"delta_auroc_vs_beta0\": 0.001,\n          \"delta_ece\": -0.001\n        },\n        \"beta_0p01\": {\n          \"delta_auroc_vs_beta0\": 0.001,\n          \"delta_ece\": 0.0\n        },\n        \"beta_0p03\": {\n          \"delta_auroc_vs_beta0\": -0.001,\n          \"delta_ece\": 0.001\n        },\n        \"beta_0p1\": {\n          \"delta_auroc_vs_beta0\": -0.002,\n          \"delta_ece\": 0.002\n        },\n        \"beta_0p3\": {\n          \"delta_auroc_vs_beta0\": -0.005,\n          \"delta_ece\": 0.003\n        },\n        \"beta_1p0\": {\n          \"delta_auroc_vs_beta0\": -0.01,\n          \"delta_ece\": 0.005\n        }\n      },\n      \"beta_sweep_stats\": {\n        \"max_delta_auroc\": 0.002,\n        \"min_delta_auroc\": -0.01,\n        \"paired_permutation_p\": 0.38,\n        \"cohens_d\": 0.07,\n        \"any_beta_significant_at_005\": false\n      },\n      \"component_ablation\": {\n        \"bce_only\": {\n          \"zs_avg_auroc\": 0.647,\n          \"ece\": 0.175\n        },\n        \"bce_plus_alpha\": {\n          \"zs_avg_auroc\": 0.651,\n          \"ece\": 0.125\n        },\n        \"bce_plus_beta\": {\n          \"zs_avg_auroc\": 0.649,\n          \"ece\": 0.173\n        },\n        \"bce_plus_alpha_plus_beta\": {\n          \"zs_avg_auroc\": 0.652,\n          \"ece\": 0.124\n        },\n        \"alpha_contribution\": \"+0.004_auroc_and_-0.050_ece\",\n        \"beta_contribution\": \"+0.001_auroc_and_-0.001_ece\"\n      },\n      \"method_comparison_qwen_L48\": {\n        \"zero_shot\": {\n          \"auroc\": 0.669,\n          \"ece\": 0.165\n        },\n        \"mean_shift\": {\n          \"auroc\": 0.669,\n          \"ece\": 0.168\n        },\n        \"caclr_alpha_only\": {\n          \"auroc\": 0.673,\n          \"ece\": 0.135\n        },\n        \"caclr_full\": {\n          \"auroc\": 0.677,\n          \"ece\": 0.133\n        },\n        \"linear_proj_50\": {\n          \"auroc\": 0.704,\n          \"ece\": 0.148\n        },\n        \"fewshot_25\": {\n          \"auroc\": 0.695,\n          \"ece\": 0.14\n        },\n        \"fewshot_100\": {\n          \"auroc\": 0.715,\n          \"ece\": 0.128\n        }\n      },\n      \"method_comparison_llama_L28\": {\n        \"zero_shot\": {\n          \"auroc\": 0.638,\n          \"ece\": 0.172\n        },\n        \"mean_shift\": {\n          \"auroc\": 0.638,\n          \"ece\": 0.175\n        },\n        \"caclr_alpha_only\": {\n          \"auroc\": 0.642,\n          \"ece\": 0.142\n        },\n        \"caclr_full\": {\n          \"auroc\": 0.644,\n          \"ece\": 0.14\n        },\n        \"linear_proj_50\": {\n          \"auroc\": 0.67,\n          \"ece\": 0.155\n        },\n        \"fewshot_25\": {\n          \"auroc\": 0.662,\n          \"ece\": 0.148\n        },\n        \"fewshot_100\": {\n          \"auroc\": 0.682,\n          \"ece\": 0.135\n        }\n      },\n      \"beta_effect_by_tier\": {\n        \"high_resource\": {\n          \"delta_auroc\": 0.003,\n          \"n_langs\": 8\n        },\n        \"mid_resource\": {\n          \"delta_auroc\": 0.001,\n          \"n_langs\": 8\n        },\n        \"low_resource\": {\n          \"delta_auroc\": -0.004,\n          \"n_langs\": 3\n        }\n      },\n      \"caclr_delta_auroc_vs_zeroshot\": 0.008,\n      \"caclr_delta_ece_vs_tempscaling\": -0.003,\n      \"linear_proj_50_delta_auroc_vs_zeroshot\": 0.035,\n      \"linear_proj_50_vs_caclr_delta\": 0.027\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: β Sweep — ΔAUROC over α-only Baseline\",\n        \"description\": \"β values (rows: 0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0) × summary stats (columns: median ΔAUROC, mean, std, # langs improved, paired permutation p, Cohen's d)。Both models side-by-side。 Key: NO β achieves p < 0.05 or d > 0.2。 Shaded gray: β = 0 row (reference)。\\n\"\n      },\n      {\n        \"name\": \"Table 6: Transfer Method Comparison — Full Ranking\",\n        \"description\": \"7 methods (rows) × 2 models × 2 fixed layers。 Columns: AUROC, ΔAUROC vs ZS, bootstrap 95% CI, p-value, Cohen's d。 Clear visual separation: linear-proj/few-shot cluster significantly above zero-shot; CaCLR-full/CaCLR-α-only marginally above; mean-shift identical to zero-shot。\\n\"\n      },\n      {\n        \"name\": \"Table 7: Component Ablation\",\n        \"description\": \"4 configurations (BCE-only, +α, +β, +α+β) × AUROC, ECE, ΔAUROC。 Demonstrates α contributes ECE reduction, β contributes nothing。 Clean decomposition of CaCLR components。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR β inertness 是 paper 的 centerpiece negative result。论证三步： (1) Empirically: β across 3 OOM, d=0.07, p=0.38, both architectures; (2) Theoretically: Zhao et al. (2019) predicts MMD failure when P(Y|X) differs across domains; (3) Constructively: linear projection succeeds (+3.5pp) because it addresses the actual misalignment type (geometric rotation)。\\n这关闭了 MMD distributional matching 这条路。Paper framing: \\\"CaCLR is the natural baseline testing whether distributional matching works; the systematic negative result + geometric explanation saves the community from pursuing this path.\\\" CaCLR 不是 novel method contribution，而是 systematic test of an obvious-seeming approach。\\nPositive takeaway: α-only CaCLR（即 SB-ECE regularized probes） provides marginal ECE improvement，可作为 calibration regularizer standalone recommendation。\\n\\n\\nβ (MMD consistency loss) inert 的根本原因：MMD 基于 kernel-space 的 distributional moment matching，优化 P(f(x_en)) ≈ P(f(x_tgt)) 其中 f 是 probe logit（1-D scalar）。但跨语言 correctness 信号的 misalignment 不是 distributional shift（mean/variance 不同），而是 geometric rotation ——correctness direction 在不同语言的 activation space 中指向不同方向。 MMD 在 1-D probe output space 中无法 capture 这种 rotation，因为 rotation 发生在高维 activation space 中、在 probe 之前。\\n具体机制：(a) β=0.001-0.01 时 MMD gradient 太弱影响不了 probe weights； (b) β=0.03-0.1 时 MMD 推动 marginal distribution alignment 但这对 1-D logit 意味着 match mean + variance，不 address correctness direction rotation；(c) β=0.3-1.0 时 MMD 主导 loss 导致 probe 退化——为了 match distributions 牺牲 discriminative power。Cohen's d=0.07 < 0.2（negligible effect size）。\\nα (SB-ECE) 项有效但贡献有限：ECE 从 0.175 降到 0.125（smooth-binned calibration regularization），但对 AUROC 的影响仅 +0.004pp。这是因为 SB-ECE 不改变 ranking，只改变 calibration curve shape。\\nLinear projection 成功（+3.5pp）恰好证实 geometric explanation： it directly estimates the rotation matrix via parallel pairs，这是 MMD mathematically cannot do 的事情。Method ranking consistent across 两个架构，证明这不是 architecture-specific artifact。\\nZhao et al. (2019) 的预测成立：当 conditional distributions P(Y|X) across domains 不同时（correctness label 分布 language-dependent）， marginal distribution matching 不保证 label prediction 改善。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Decomposition Ablation\",\n    \"description\": \"IRT difficulty probes → project out difficulty direction → retrain correctness probes on residuals → evaluate transfer。 10 langs × 8 layers per model。Random-direction control。\\n\",\n    \"results\": {\n      \"difficulty_probe_r2_en\": {\n        \"median\": 0.4,\n        \"range\": [\n          0.22,\n          0.52\n        ],\n        \"peak_layer_pct_depth\": 0.65\n      },\n      \"difficulty_probe_r2_per_tier\": {\n        \"high\": {\n          \"median\": 0.43,\n          \"range\": [\n            0.25,\n            0.55\n          ]\n        },\n        \"mid\": {\n          \"median\": 0.38,\n          \"range\": [\n            0.2,\n            0.5\n          ]\n        },\n        \"low\": {\n          \"median\": 0.3,\n          \"range\": [\n            0.15,\n            0.42\n          ]\n        }\n      },\n      \"decomposition_delta_auroc\": {\n        \"overall_median\": 0.015,\n        \"overall_range\": [\n          -0.012,\n          0.038\n        ],\n        \"by_tier\": {\n          \"high\": {\n            \"median\": 0.02,\n            \"pct_improved\": 0.72\n          },\n          \"mid\": {\n            \"median\": 0.013,\n            \"pct_improved\": 0.63\n          },\n          \"low\": {\n            \"median\": 0.008,\n            \"pct_improved\": 0.5\n          }\n        },\n        \"by_depth\": {\n          \"shallow_20_40pct\": {\n            \"median\": 0.005,\n            \"pct_improved\": 0.48\n          },\n          \"mid_40_60pct\": {\n            \"median\": 0.015,\n            \"pct_improved\": 0.65\n          },\n          \"deep_60_90pct\": {\n            \"median\": 0.022,\n            \"pct_improved\": 0.78\n          }\n        },\n        \"overall_pct_improved\": 0.65,\n        \"paired_permutation_p\": 0.028,\n        \"cohens_d\": 0.25\n      },\n      \"random_direction_control\": {\n        \"delta_auroc_median\": 0.003,\n        \"pct_improved\": 0.52,\n        \"paired_p\": 0.42,\n        \"cohens_d\": 0.05\n      },\n      \"difficulty_correctness_cosine\": {\n        \"median\": 0.2,\n        \"range\": [\n          0.1,\n          0.32\n        ],\n        \"increases_with_depth\": true\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Decomposition ΔAUROC (10 Languages × 8 Layers)\",\n        \"description\": \"Languages (rows) × layers (columns)。Cells: ΔAUROC after difficulty removal。Green >1pp, white ±1pp, red <-1pp。 Marginals: % improved per language, per layer。 Clear pattern: improvement concentrated at deep layers and high-resource languages。\\n\"\n      },\n      {\n        \"name\": \"Table 9: Decomposition vs Random Direction Control\",\n        \"description\": \"3 conditions (rows: original, difficulty-removed, random-removed) × summary (median AUROC, ΔAUROC, bootstrap CI, p, d)。 Per-architecture。Demonstrates specificity of difficulty direction。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition 是 Claim 2 的 supporting evidence，降级为 qualitative。 Key insight: difficulty is the transferable component (shared across languages), capability is the degrading component (language-specific)。 At deep layers where capability dominates, removing difficulty helps because it forces the probe to rely on the (smaller but still transferable) capability signal。\\nEffect size (d=0.25) 不足以作为 standalone method recommendation， 但足以支撑 \\\"difficulty-capability decomposition exists\\\" 的 analytical claim。需要 supplementary ablation（vary projection dimension, IRT model complexity）来 strengthen。\\n\\n\\nDecomposition 定性成立但 effect size 小（d=0.25），原因： (1) difficulty-capability separation 不是 clean 的——IRT difficulty 只解释 ~40% variance，残差中仍混有 difficulty 信号； (2) difficulty direction 和 correctness direction 不完全正交 （cosine ~0.20），projecting out difficulty 会 partially remove some correctness signal； (3) 对 shallow layers 效果弱（48% improved，接近 chance）因为 浅层 difficulty 和 capability 更 entangled，线性 projection 分不开。\\nDeep layers 效果好（78% improved，d ~0.35）因为 capability-specific component 在深层主导 transfer degradation——移除 shared difficulty component 后，残差更 cleanly 反映 language-specific capability, 使 correctness probe 被迫 focus on transferable component。\\nRandom direction control (d=0.05, p=0.42) 排除 dimensionality reduction artifact：不是 \\\"any direction removal helps\\\"，而是 specifically difficulty direction matters。\\nResource tier gradient 反映 low-resource probes 本身噪声大—— difficulty projection 可能 remove 它们有限 signal 的一部分。\\n总体：支持 Claim 2（difficulty-capability decomposition exists and is prescriptive），但 effect size 要求降为 qualitative claim with ablation support, 不是 standalone quantitative contribution。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"Verbalized confidence direction extraction → cosine with correctness direction across 20 languages × 2 architectures。 Resource tier and language family analysis。\\n\",\n    \"results\": {\n      \"cosine_en_qwen\": 0.032,\n      \"cosine_en_llama\": 0.036,\n      \"cosine_per_lang_qwen\": {\n        \"zh\": 0.038,\n        \"es\": 0.035,\n        \"fr\": 0.033,\n        \"de\": 0.036,\n        \"ja\": 0.04,\n        \"pt\": 0.034,\n        \"nl\": 0.033,\n        \"ru\": 0.042,\n        \"ar\": 0.055,\n        \"hi\": 0.058,\n        \"ko\": 0.05,\n        \"vi\": 0.06,\n        \"tr\": 0.062,\n        \"id\": 0.048,\n        \"pl\": 0.04,\n        \"uk\": 0.045,\n        \"sw\": 0.095,\n        \"bn\": 0.088,\n        \"te\": 0.078\n      },\n      \"cosine_per_lang_llama\": {\n        \"zh\": 0.042,\n        \"es\": 0.038,\n        \"fr\": 0.036,\n        \"de\": 0.04,\n        \"ja\": 0.045,\n        \"pt\": 0.037,\n        \"nl\": 0.036,\n        \"ru\": 0.048,\n        \"ar\": 0.06,\n        \"hi\": 0.065,\n        \"ko\": 0.055,\n        \"vi\": 0.068,\n        \"tr\": 0.07,\n        \"id\": 0.052,\n        \"pl\": 0.045,\n        \"uk\": 0.05,\n        \"sw\": 0.11,\n        \"bn\": 0.098,\n        \"te\": 0.085\n      },\n      \"cosine_median_all_langs_qwen\": 0.044,\n      \"cosine_median_all_langs_llama\": 0.05,\n      \"cosine_range_overall\": [\n        0.032,\n        0.11\n      ],\n      \"all_below_012\": true,\n      \"cosine_by_tier\": {\n        \"high\": {\n          \"median\": 0.037,\n          \"var\": 3e-05\n        },\n        \"mid\": {\n          \"median\": 0.054,\n          \"var\": 8e-05\n        },\n        \"low\": {\n          \"median\": 0.09,\n          \"var\": 0.00012\n        }\n      },\n      \"resource_spearman_rho\": -0.58,\n      \"resource_spearman_p\": 0.008,\n      \"cross_architecture_correlation\": 0.94\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Correctness-Confidence Cosine by Language and Architecture\",\n        \"description\": \"20 langs (rows, grouped by tier) × 2 architectures (column pairs)。 Each cell: cosine ± bootstrap 95% CI。Bottom: tier medians, Spearman rho with log(resource estimate)。All < 0.12。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Extends Miao & Ungar (2026) to multilingual settings。Universal orthogonality confirms output-based calibration is structurally limited regardless of language. Novel finding: resource-tier gradient (rho = -0.58, p = 0.008) suggests abundant pretraining helps separate correctness from confidence representations。\\nClaim 4 framing: orthogonality holds universally (max 0.11 < 0.12) but variance caveat needed for low-resource languages where the separation is weaker。\\n\\n\\nOrthogonality 持续因为 correctness-confidence separation 是 transformer 处理 MCQA 的 structural property：correctness 是 representation-level 属性（模型内部是否 \\\"知道\\\"），confidence 是 output-level 属性（模型 verbalized 的 uncertainty，受 RLHF 优化）。 两者 occupy 不同 subspaces。\\nEnglish cosine replicates Miao & Ungar (2026)（~0.035）。 Non-English cosines 较高（median 0.044-0.050）因为： (a) Non-English confidence verbalization 更 noisy（模型不擅长 用非英语表达 uncertainty）→ confidence probe 更 noisy → 噪声 correlation 微增 cosine； (b) Low-resource 语言中 confidence probe 可能 capture language-switching signal 而非 pure confidence。\\nsw 的 cosine 最高（0.095-0.110）但仍远低于表示 meaningful alignment 的 0.5+。Variance 随 resource tier 增加 （0.00003 → 0.00012）反映 probe quality 在 low-resource 下更 不稳定。\\nCross-architecture correlation = 0.94：orthogonality pattern is model-agnostic，由 language properties 决定而非 architecture。 Claim 4 加 variance caveat：\\\"persists but with increasing variance for lower-resource languages\\\"。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison (LogReg vs MLP)\",\n    \"description\": \"Logistic regression vs 2-layer MLP at each probed layer, both models。English AUROC, cross-lingual transfer gap, calibration quality comparison。\\n\",\n    \"results\": {\n      \"logreg_en_best_qwen\": 0.8,\n      \"mlp_en_best_qwen\": 0.825,\n      \"logreg_en_best_llama\": 0.78,\n      \"mlp_en_best_llama\": 0.8,\n      \"mlp_en_advantage\": 0.022,\n      \"logreg_transfer_gap_qwen\": 0.131,\n      \"mlp_transfer_gap_qwen\": 0.185,\n      \"logreg_transfer_gap_llama\": 0.142,\n      \"mlp_transfer_gap_llama\": 0.195,\n      \"gap_difference\": 0.054,\n      \"mlp_advantage_en_shallow\": 0.01,\n      \"mlp_advantage_en_deep\": 0.03,\n      \"mlp_transfer_disadvantage_shallow\": 0.02,\n      \"mlp_transfer_disadvantage_deep\": 0.065,\n      \"logreg_better_transfer_pct\": 0.82,\n      \"exceptions\": \"zh, es (high-resource where MLP nonlinearity partially transfers)\",\n      \"logreg_ece_median\": 0.135,\n      \"mlp_ece_median\": 0.148\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: Probe Complexity — EN AUROC and Transfer Gap by Layer\",\n        \"description\": \"Supplementary。Layers (rows) × (LogReg EN, MLP EN, LogReg ZS, MLP ZS, LogReg gap, MLP gap) for each model。Shows MLP advantage concentrates in EN at deep layers, paid for by larger transfer gap。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Methodological validation supporting linear probe choice。 The nonlinear component is real (MLP +2pp EN) but non-transferable (MLP -5.4pp gap increase)。Confirms correctness signal's transferable component is linear/geometric。Supplementary material。\\n\\n\\nMLP 在 English 上高 ~2pp 因为 correctness signal 有 small nonlinear component（层间交互、feature conjunction）。但 nonlinear component is language-specific：MLP 学到的 English-specific nonlinear boundary 不 generalize cross-lingually，导致 transfer gap 大 5.4pp。\\nGap 在 deep layers 更大（6.5pp vs 2.0pp shallow）因为深层 representations 有更复杂的 language-specific structure 供 MLP exploit。 MLP overfits to English deep-layer nonlinearities。\\n82% 语言 LogReg transfer 更好；例外是 zh/es，high-resource 语言 where MLP 的 nonlinear component partially transfers due to shared pretraining features。\\nThis validates paper's focus on linear probes and reinforces geometric (linear subspace) framing。Goes in supplementary。\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"Evaluate best probes + CaCLR on Belebele (reading comprehension) and MMLU-ProX (translated MCQA), 20 languages each。 Validates generalization beyond GlobalMMLU。\\n\",\n    \"results\": {\n      \"belebele_en_best_auroc_qwen\": 0.77,\n      \"belebele_zs_median_qwen\": 0.65,\n      \"belebele_pareto_rho_qwen\": -0.45,\n      \"belebele_linear_proj_delta\": 0.03,\n      \"belebele_caclr_beta_delta\": 0.002,\n      \"mmlupx_en_best_auroc_qwen\": 0.81,\n      \"mmlupx_zs_median_qwen\": 0.67,\n      \"mmlupx_pareto_rho_qwen\": -0.48,\n      \"mmlupx_linear_proj_delta\": 0.034,\n      \"mmlupx_caclr_beta_delta\": 0.003,\n      \"rank_corr_globalmmlu_vs_belebele\": 0.8,\n      \"rank_corr_globalmmlu_vs_mmlupx\": 0.9,\n      \"method_ranking_consistent\": true,\n      \"caclr_beta_inert_all_benchmarks\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Cross-Benchmark Generalization\",\n        \"description\": \"Supplementary。3 benchmarks (rows) × key metrics (EN AUROC, ZS median, Pareto rho, linear-proj Δ, CaCLR-β Δ)。 Per-language AUROC rank correlations between benchmarks。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Straightforward generalization validation。One paragraph in supplementary。Addresses \\\"only MCQA\\\" concern partially (Belebele is reading comprehension)。CaCLR inertness replicates → strengthens negative result。\\n\\n\\nBelebele 是 reading comprehension → correctness signal 不同于 factual knowledge，EN AUROC 略低（0.77 vs 0.80）。但 Pareto 和 method ranking 一致，因为底层机制相同：model representations encode correctness at mid-depth, 深层 language-specialize。\\nMMLU-ProX 与 GlobalMMLU format 接近（translated MCQA），结果更 相似（0.81 EN, -0.48 rho）。Per-language rank correlation 0.90 confirms transfer difficulty is model property, not benchmark artifact。\\nCaCLR β inert across all benchmarks → rules out GlobalMMLU-specific explanation for negative result。Linear projection consistent (+3.0-3.4pp) → the geometric correction generalizes。\\n\"\n  },\n  {\n    \"name\": \"Quantization Validation Ablation\",\n    \"description\": \"(a) W4A16 vs FP16 at 5 layers for Llama 4 Scout (5% subset); (b) GPTQ-Int4 vs FP16 at 5 layers for Qwen3-235B (5% subset)。\\n\",\n    \"results\": {\n      \"llama_w4a16_vs_fp16\": {\n        \"auroc_max_diff\": 0.009,\n        \"auroc_mean_diff\": 0.004,\n        \"pearson_r\": 0.996,\n        \"rank_agreement_pct\": 0.97,\n        \"per_layer\": {\n          \"L8\": {\n            \"w4a16\": 0.631,\n            \"fp16\": 0.635,\n            \"diff\": -0.004\n          },\n          \"L16\": {\n            \"w4a16\": 0.698,\n            \"fp16\": 0.702,\n            \"diff\": -0.004\n          },\n          \"L24\": {\n            \"w4a16\": 0.733,\n            \"fp16\": 0.738,\n            \"diff\": -0.005\n          },\n          \"L32\": {\n            \"w4a16\": 0.762,\n            \"fp16\": 0.769,\n            \"diff\": -0.007\n          },\n          \"L40\": {\n            \"w4a16\": 0.778,\n            \"fp16\": 0.787,\n            \"diff\": -0.009\n          }\n        }\n      },\n      \"qwen_int4_vs_fp16\": {\n        \"auroc_max_diff\": 0.011,\n        \"auroc_mean_diff\": 0.005,\n        \"pearson_r\": 0.995,\n        \"rank_agreement_pct\": 0.96,\n        \"per_layer\": {\n          \"L16\": {\n            \"int4\": 0.642,\n            \"fp16\": 0.648,\n            \"diff\": -0.006\n          },\n          \"L32\": {\n            \"int4\": 0.732,\n            \"fp16\": 0.737,\n            \"diff\": -0.005\n          },\n          \"L48\": {\n            \"int4\": 0.77,\n            \"fp16\": 0.774,\n            \"diff\": -0.004\n          },\n          \"L64\": {\n            \"int4\": 0.798,\n            \"fp16\": 0.803,\n            \"diff\": -0.005\n          },\n          \"L80\": {\n            \"int4\": 0.79,\n            \"fp16\": 0.801,\n            \"diff\": -0.011\n          }\n        }\n      },\n      \"quantization_distortion_significant\": false,\n      \"conclusion\": \"Quantization introduces ≤1.1pp AUROC difference, well within bootstrap CIs\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: Quantization Validation\",\n        \"description\": \"Supplementary。5 layers × (Quantized AUROC, FP16 AUROC, Δ, rank correlation) for each model。All Δ within bootstrap CI。 Conclusion: quantization does not distort correctness signals。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Necessary reviewer reassurance, expected non-issue。One paragraph + table in supplementary。Largest observed difference (1.1pp at deep layer for Qwen3 INT4) is within noise bounds。\\n\\n\\n4-bit weight quantization（W4A16 和 GPTQ-Int4）对 correctness probing 影响很小，因为：(a) weight quantization 不影响 activation precision （W4A16 的 activations 仍是 FP16）；(b) 高维 activation space (4096+ dims) 中 per-dimension 微扰在 aggregation 后接近 cancel out； (c) correctness probe operates on rank-order，not absolute values—— small uniform perturbations preserve ranking。\\nQwen3 deep layer (L80) 差异略大 (1.1pp) 因为 MoE routing 在深层 accumulated more quantization error through expert selection。 但仍在 bootstrap CI 内。Pearson r > 0.995 confirms near-perfect linear relationship between quantized and FP16 scores。\\n\"\n  },\n  {\n    \"name\": \"CKA Cross-Lingual Representation Similarity\",\n    \"description\": \"CKA (linear kernel) between EN and 19 target languages at every probed layer, both models。Partial correlation controlling depth。 Between-language analysis。Subspace angle analysis。\\n\",\n    \"results\": {\n      \"cka_qwen_representative\": {\n        \"zh_L12\": 0.87,\n        \"zh_L48\": 0.72,\n        \"zh_L72\": 0.58,\n        \"zh_L92\": 0.5,\n        \"sw_L12\": 0.76,\n        \"sw_L48\": 0.55,\n        \"sw_L72\": 0.38,\n        \"sw_L92\": 0.28\n      },\n      \"cka_shallow_median\": 0.83,\n      \"cka_deep_median\": 0.48,\n      \"cka_decline_with_depth_significant\": true,\n      \"cka_by_tier_at_70pct_depth\": {\n        \"high\": 0.58,\n        \"mid\": 0.46,\n        \"low\": 0.34\n      },\n      \"cka_transfer_pooled\": {\n        \"qwen_pearson_r\": 0.55,\n        \"qwen_p\": 1e-05,\n        \"llama_pearson_r\": 0.48,\n        \"llama_p\": 0.0001,\n        \"pooled_r\": 0.52,\n        \"pooled_p\": 1e-06\n      },\n      \"cka_partial_corr_controlling_depth\": {\n        \"qwen_r\": 0.2,\n        \"qwen_p\": 0.08,\n        \"llama_r\": 0.15,\n        \"llama_p\": 0.16,\n        \"pooled_r\": 0.18,\n        \"pooled_p\": 0.11\n      },\n      \"between_lang_same_layer\": {\n        \"L_25pct_depth\": {\n          \"pearson_r\": 0.48,\n          \"p\": 0.032,\n          \"n\": 19\n        },\n        \"L_50pct_depth\": {\n          \"pearson_r\": 0.55,\n          \"p\": 0.014,\n          \"n\": 19\n        },\n        \"L_75pct_depth\": {\n          \"pearson_r\": 0.52,\n          \"p\": 0.022,\n          \"n\": 19\n        },\n        \"median_across_layers_r\": 0.52,\n        \"median_across_layers_p\": 0.02\n      },\n      \"per_lang_spearman_median\": -0.45,\n      \"per_lang_spearman_significant_fraction\": 0.4,\n      \"per_lang_n_per_language_qwen\": 24,\n      \"per_lang_n_per_language_llama\": 12,\n      \"subspace_angle_correctness\": {\n        \"shallow_median_deg\": 15,\n        \"deep_median_deg\": 38,\n        \"increases_with_depth\": true\n      },\n      \"subspace_angle_random_baseline\": {\n        \"median_deg\": 72\n      },\n      \"cka_cliff_qwen\": {\n        \"location_pct_depth\": 0.72,\n        \"cliff_magnitude\": 0.15\n      },\n      \"cka_cliff_llama\": {\n        \"location_pct_depth\": 0.65,\n        \"cliff_magnitude\": 0.08\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: CKA Similarity Heatmap (Languages × Layers)\",\n        \"description\": \"Probed layers (rows) × 19 target languages (columns, sorted by resource tier)。Cells: CKA values, color-coded。Both models。 Clear depth gradient and resource-tier banding。\\n\"\n      },\n      {\n        \"name\": \"Table 12: CKA as Transfer Predictor — Partial Correlation Analysis\",\n        \"description\": \"KEY TABLE。Rows: (1) Pooled CKA-transfer r, (2) Depth-transfer r, (3) Partial CKA-transfer controlling depth, (4) Between-language same-depth CKA-transfer r。Columns: r, R², p, interpretation。 Demonstrates that partial r=0.18 (p=0.11) → CKA is suggestive only, but between-language r=0.52 (p=0.02) → valid between-language claim。\\n\"\n      },\n      {\n        \"name\": \"Table 13: Subspace Angle Analysis\",\n        \"description\": \"Depth bins (rows) × statistics (columns: median angle, IQR, random baseline)。Both models。Shows correctness subspace rotation increases with depth but remains far from random。 Quantitative support for geometric narrative。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CKA analysis 降级为 \\\"suggestive correlational analysis\\\" 基于 partial correlation result (r=0.18, p=0.11)。Paper 必须明确承认 depth confound 并 present partial correlation as the honest test。\\nSalvageable claims: (1) Between-language: \\\"languages with higher CKA show less transfer degradation at matched depth\\\" (r=0.52, p=0.02) — valid (2) Qualitative: CKA cliff steepness differs across architectures, consistent with Pareto strength difference — suggestive (3) Subspace angle: correctness direction rotation increases with depth (15° → 38°) — quantitative geometric evidence\\nNOT supportable: \\\"CKA explains why transfer degrades with depth\\\" (depth itself explains this; CKA adds marginal information)。\\nFor the CaCLR negative result narrative: CKA analysis provides suggestive geometric context (rotation not distributional shift) but the argument must lean more on Zhao et al. (2019) theory than on CKA empirics。\\n\\n\\nCKA pooled correlation (r=0.52, p<0.001) 看起来 strong 但有严重 depth confound：deeper layers simultaneously have lower CKA AND lower transfer AUROC，所以 correlation 大部分来自 shared depth effect。\\nPartial correlation controlling normalized depth 是 THE critical test （Dream RD2, 3-tier consensus）：r=0.18, p=0.11。这意味着 CKA 在 控制 depth 后几乎没有额外 explanatory power。Depth alone explains most of the variance in both CKA and transfer AUROC。这直接导致 CKA 从 \\\"geometric analysis\\\" 降级为 \\\"suggestive correlational analysis\\\"。\\nBUT between-language correlation 成立：在同一 depth，语言间 CKA 与 transfer 的 correlation r=0.52, p=0.02 (n=19)。这说明 \\\"languages with higher CKA transfer better\\\" 是 valid between-language claim，只是不能说 \\\"CKA predicts within-language depth degradation\\\"。\\nPer-language Spearman 只有 40% significant（Qwen n=24 较好， Llama n=12 power 不足），与 pilot 一致。\\nSubspace angle analysis provides quantitative geometric evidence： correctness subspace angle increases from 15° (shallow) to 38° (deep)， 远小于 random baseline 72°，证实 correctness direction 作为 low-dimensional subspace feature 存在但 rotation 随 depth 增加。\\nCKA cliff steepness 差异（Qwen 0.15 at 72% vs Llama 0.08 at 65%） qualitatively explains Pareto strength difference：Qwen 在更深处 有更 abrupt 的 CKA drop，对应更 uniform 的 negative transfer trend。\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sensitivity Analysis\",\n    \"description\": \"Vary parallel pairs (10, 20, 50, 100, 200) for linear projection。 Both models × 5 representative layers × 20 languages。\\n\",\n    \"results\": {\n      \"pairs_10\": {\n        \"delta_auroc_median\": 0.012,\n        \"std\": 0.022\n      },\n      \"pairs_20\": {\n        \"delta_auroc_median\": 0.023,\n        \"std\": 0.016\n      },\n      \"pairs_50\": {\n        \"delta_auroc_median\": 0.035,\n        \"std\": 0.011\n      },\n      \"pairs_100\": {\n        \"delta_auroc_median\": 0.04,\n        \"std\": 0.008\n      },\n      \"pairs_200\": {\n        \"delta_auroc_median\": 0.042,\n        \"std\": 0.007\n      },\n      \"saturation_knee\": 60,\n      \"pairs_for_90pct_improvement\": 50,\n      \"pairs_for_95pct_improvement\": 80,\n      \"qwen_knee\": 55,\n      \"llama_knee\": 65,\n      \"consistent_across_models\": true,\n      \"pairs_to_match_caclr\": 15,\n      \"pairs_to_exceed_caclr\": 20,\n      \"high_resource_pairs_50_delta\": 0.028,\n      \"mid_resource_pairs_50_delta\": 0.038,\n      \"low_resource_pairs_50_delta\": 0.045\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Linear Projection Sample Efficiency\",\n        \"description\": \"Pair counts (rows: 10, 20, 50, 100, 200) × (median ΔAUROC, mean, std, min, max, % langs improved)。Both models。 Clear diminishing returns after 50 pairs。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear projection's sample efficiency is the constructive complement to CaCLR's negative result。The practical message is clear and actionable: ~50 parallel pairs (trivially obtainable) provide a simple, effective, zero-target-label solution that outperforms distributional matching。\\nThe learning curve figure — showing linear projection surpassing CaCLR at 20 pairs — directly illustrates the cost-benefit argument。\\n\\n\\nLinear projection 学习 rotation matrix mapping source → target language representation space。Sample complexity 低因为 correctness-relevant subspace is low-rank：虽然 full activation space is 4096+ dims，但 correctness signal 集中在 few dimensions， 所以 effective mapping dimension 很小。\\n10 pairs: underdetermined but captures dominant rotation (+1.2pp)。 50 pairs: 90% of achievable improvement（major rotation axes identified）。 100+ pairs: diminishing returns（fine corrections of minor axes）。\\nKnee at ~55-65 pairs consistent with cross-lingual alignment literature (MUSE/VecMap: 50-100 bilingual dictionary entries suffice)。 Llama 略需更多 pairs（65 vs 55）因为其 MoE routing 引入更多 representation heterogeneity。\\nLow-resource 语言 benefit MORE from linear projection (+4.5pp vs +2.8pp high-resource) 因为它们的 geometric misalignment 更大 → more room for correction。\\nPractical headline: \\\"~50 parallel pairs + simple linear projection matches or exceeds CaCLR's entire training pipeline, surpassing CaCLR at just ~20 pairs\\\"。\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks — Full Cross-Lingual Analysis\",\n    \"description\": \"Extend Hewitt & Liang control tasks to 20 languages × both models。 Selectivity across layers, languages, resource tiers。 Capacity artifact identification。\\n\",\n    \"results\": {\n      \"en_selectivity_qwen\": {\n        \"shallow_avg\": 0.03,\n        \"mid_avg\": 0.18,\n        \"deep_avg\": 0.27\n      },\n      \"en_selectivity_llama\": {\n        \"shallow_avg\": 0.03,\n        \"mid_avg\": 0.15,\n        \"deep_avg\": 0.24\n      },\n      \"selectivity_by_tier\": {\n        \"high_resource\": {\n          \"median\": 0.19,\n          \"range\": [\n            0.03,\n            0.28\n          ]\n        },\n        \"mid_resource\": {\n          \"median\": 0.14,\n          \"range\": [\n            0.02,\n            0.24\n          ]\n        },\n        \"low_resource\": {\n          \"median\": 0.09,\n          \"range\": [\n            0.01,\n            0.18\n          ]\n        }\n      },\n      \"selectivity_below_005_fraction\": 0.27,\n      \"selectivity_below_005_by_tier\": {\n        \"high\": 0.2,\n        \"mid\": 0.28,\n        \"low\": 0.42\n      },\n      \"selectivity_below_005_by_depth\": {\n        \"shallow_0_30pct\": 0.85,\n        \"mid_30_60pct\": 0.18,\n        \"deep_60_100pct\": 0.08\n      },\n      \"worst_selectivity_combos\": [\n        {\n          \"lang\": \"sw\",\n          \"depth_range\": \"0-50%\",\n          \"median_selectivity\": 0.02\n        },\n        {\n          \"lang\": \"bn\",\n          \"depth_range\": \"0-50%\",\n          \"median_selectivity\": 0.03\n        },\n        {\n          \"lang\": \"te\",\n          \"depth_range\": \"0-40%\",\n          \"median_selectivity\": 0.02\n        },\n        {\n          \"lang\": \"all\",\n          \"depth_range\": \"0-20%\",\n          \"median_selectivity\": 0.03\n        }\n      ],\n      \"control_auroc_median\": 0.5,\n      \"control_auroc_range\": [\n        0.48,\n        0.53\n      ],\n      \"all_selectivities_positive\": true,\n      \"pct_above_010\": 0.73,\n      \"pct_above_005\": 0.73\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S4: Control Task Selectivity Heatmap\",\n        \"description\": \"20 languages (rows, by tier) × representative layers (columns)。 Cells: selectivity (real AUROC - control AUROC)。Color: green >15pp, yellow 10-15pp, orange 5-10pp, red <5pp。 Clear resource-tier × depth pattern。Both models。\\n\"\n      },\n      {\n        \"name\": \"Table 15: Capacity Artifact Warning — Summary Statistics\",\n        \"description\": \"Main text table (not supplementary — this is an independent contribution)。Resource tiers (rows) × depth bins (columns)。 Cells: % of combos with selectivity < 0.05。Total: 27%。 Recommendation: minimum selectivity threshold for interpretable cross-lingual probing。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Control task artifact finding 升级为独立贡献。The ~27% artifact rate challenges uncritical cross-lingual probing and provides actionable guidance (selectivity ≥ 0.05 threshold)。\\nThis is distinct from the paper's other claims — it's a methodological warning for the cross-lingual probing community, not specific to correctness or calibration。\\nFor the paper's own claims: we exclude combos below threshold from statistical tests where feasible, and note the caveat for low-resource claims where exclusion isn't feasible。\\n\\n\\n27% of lang-layer combos below 0.05 selectivity — concentrated in two dimensions: (a) shallow layers universally (0-20% depth: 85% below threshold) because correctness signal hasn't yet emerged; (b) low-resource languages at mid-depth (sw/bn/te 42% below).\\nShallow-layer low selectivity is expected and benign — paper doesn't claim correctness signal at shallow layers. But low-resource mid-depth artifacts are a genuine concern: probes with selectivity < 0.05 may reflect capacity memorization rather than correctness signal。 This means ~42% of low-resource lang-layer combinations should be interpreted with caution。\\nPaper framing: this is itself a methodological contribution。 \\\"~27% of cross-lingual probing results in our setting are capacity artifacts. We recommend selectivity ≥ 0.05 as minimum threshold for cross-lingual probe interpretability, especially for low-resource languages.\\\" This warning generalizes beyond our specific paper to any cross-lingual probing study。\\nControl AUROC near 0.50 confirms LogReg has negligible capacity to memorize random labels in high-dim space — any above-baseline performance reflects real signal。\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense Pareto Frontier\",\n    \"description\": \"Third architecture for camera-ready。60 layers, dense, FP16。 Provides dense vs MoE architectural contrast。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.79,\n      \"en_best_layer\": 42,\n      \"zs_transfer_auroc_median\": 0.67,\n      \"best_transfer_layer\": 30,\n      \"pareto_rho_per_lang_median\": -0.55,\n      \"pareto_rho_range\": [\n        -0.62,\n        -0.48\n      ],\n      \"pareto_rho_std\": 0.04,\n      \"zs_langs_above_065\": 12,\n      \"linear_proj_delta\": 0.033,\n      \"cka_cliff_magnitude\": 0.18,\n      \"cka_cliff_steeper_than_moe\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table CR1: Three-Architecture Pareto Comparison\",\n        \"description\": \"Camera-ready。3 architectures (rows) × (EN AUROC, ZS median, rho median, rho std, rho range, CKA cliff, linear-proj Δ)。 Dense model: lowest rho std (most uniform tradeoff)。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Camera-ready addition。Dense vs MoE is the strongest architecture contrast: MoE routing heterogeneity produces language-specific Pareto (Llama4) or moderate uniform Pareto (Qwen3); dense model produces consistently uniform strong Pareto。Three-architecture triangulation makes Claim 1 considerably more convincing。\\n\\n\\nDense architecture 提供 critical architectural contrast： (a) rho std = 0.04 (vs MoE Qwen 0.05, Llama 0.12) 因为 no routing heterogeneity → more uniform depth effect; (b) rho median = -0.55, 较 MoE 更 consistent negative 因为 dense model 所有 tokens 经过所有层 → cleaner monotonic specialization; (c) CKA cliff steeper (0.18 vs Qwen's 0.15) 因为 MoE routing provides partial buffer against geometric misalignment（different experts can maintain cross-lingual features at deep layers）; (d) EN AUROC 0.79 与 larger MoE models comparable despite smaller parameter count → dense architecture is parameter-efficient for representation quality。\\n三架构对比 strengthens architecture-dependence claim from \\\"two MoE models differ moderately\\\" to \\\"dense shows distinct, more uniform Pareto shape\\\"。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (50+ Languages)\",\n    \"description\": \"Expand from 20 to 50+ languages for camera-ready。 Full GlobalMMLU/Belebele language coverage。\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"zs_langs_above_060\": 32,\n      \"zs_langs_above_065\": 25,\n      \"zs_median_auroc_52lang\": 0.64,\n      \"zs_auroc_range\": [\n        0.5,\n        0.73\n      ],\n      \"new_failed_langs\": [\n        \"am\",\n        \"my\",\n        \"zu\",\n        \"sn\",\n        \"rw\",\n        \"xh\",\n        \"ny\",\n        \"mg\"\n      ],\n      \"n_below_055\": 10,\n      \"resource_tier_gradient_replicates\": true,\n      \"pareto_rho_median_52lang\": -0.47,\n      \"linear_proj_delta_52lang\": 0.032,\n      \"fraction_viable_with_linear_proj\": 0.67\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table CR2: Extended 52-Language Results\",\n        \"description\": \"Camera-ready。52 languages sorted by ZS AUROC, grouped into 4 tiers: Strong (>0.70), Viable (0.65-0.70), Marginal (0.55-0.65), Failed (<0.55)。Columns: language, family, script, resource tier, ZS AUROC, linear-proj AUROC。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Camera-ready scale extension。Confirms resource-tier gradient is the dominant predictor。Sets realistic practitioner expectations and motivates future work on low-resource probe training。 The 67% viability rate (with linear projection) is the practical headline for this extension。\\n\\n52 语言扩展增加大量 low-resource 和 typologically diverse 语言。 Median AUROC drops（0.64 vs curated 20 的 0.66）因为新增语言 disproportionately low-resource。10 语言 < 0.55（am/my/zu/sn/rw /xh/ny/mg + sw/bn from original）——minimal pretraining representation。\\nResource tier gradient 更 pronounced：extended tail 提供更多 data points 在 low end。Pareto rho 微弱化（-0.47）因为很多新增 语言的 probe 本身 noisy → rho estimate 不准。\\nLinear projection consistent at +3.2pp，extends viability from 32/52 (62% ZS) to 35/52 (67% with projection)。 Remaining 17 需要 language-specific solutions。\\nPractical conclusion: probe-based cross-lingual calibration is viable for majority (67%) of tested languages with minimal effort; the remaining third requires per-language probes or alternative approaches。\\n\"\n  }\n]",
      "numLines": 1132,
      "startLine": 1,
      "totalLines": 1132
    }
  },
  "sourceToolAssistantUUID": "0169291f-bed1-424b-84ca-5d07e34df71f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "a52cb558-9200-43d7-81d6-8b7d35e26aba",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

### Assistant

_source line 14 · 2026-05-21T04:09:19.947Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me also load the research and writing skills for this project to inform my paper writing style.

Let me now compose a comprehensive LaTeX paper. I need to create tables for all experiments and write all sections. Let me first check what directory structure exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a52cb558-9200-43d7-81d6-8b7d35e26aba",
  "isSidechain": false,
  "requestId": "req_011CbF4JRynakLG8fNbwQinq",
  "type": "assistant",
  "uuid": "3f44effc-06c2-41a0-b968-bc13ac47294c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVGQ1GamVf7Q1rc16bBus1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3963,
      "cache_creation_input_tokens": 21934,
      "cache_read_input_tokens": 23551,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21934,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3963,
          "output_tokens": 293,
          "cache_read_input_tokens": 23551,
          "cache_creation_input_tokens": 21934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21934
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

_source line 15 · 2026-05-21T04:09:20.929Z_

Now let me check the output directory and load the writing skill for style guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f44effc-06c2-41a0-b968-bc13ac47294c",
  "isSidechain": false,
  "requestId": "req_011CbF4JRynakLG8fNbwQinq",
  "type": "assistant",
  "uuid": "d84cf77c-048a-414e-9e1c-ea6011fe825c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVGQ1GamVf7Q1rc16bBus1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3963,
      "cache_creation_input_tokens": 21934,
      "cache_read_input_tokens": 23551,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21934,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3963,
          "output_tokens": 293,
          "cache_read_input_tokens": 23551,
          "cache_creation_input_tokens": 21934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21934
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

_source line 16 · 2026-05-21T04:09:23.315Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MsxT5aTGhUmna36U3DP6UB`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d84cf77c-048a-414e-9e1c-ea6011fe825c",
  "isSidechain": false,
  "requestId": "req_011CbF4JRynakLG8fNbwQinq",
  "type": "assistant",
  "uuid": "bc888a2b-9c56-459d-94dd-5bf29d5a7107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVGQ1GamVf7Q1rc16bBus1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3963,
      "cache_creation_input_tokens": 21934,
      "cache_read_input_tokens": 23551,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21934,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3963,
          "output_tokens": 293,
          "cache_read_input_tokens": 23551,
          "cache_creation_input_tokens": 21934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21934
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

_source line 17 · 2026-05-21T04:09:24.232Z_

<details><summary>↩ Tool result · `toolu_019YhSTqRivyzB7G7ppVdhcq`</summary>

```text
1	---
2	name: xling-calib-direction-writing
3	description: Writing and visual presentation patterns from 8 papers on cross-lingual calibration and representations
4	type: skill
5	---
6	
7	# Cross-Lingual Calibration — Writing Patterns (8 papers)
8	
9	## Narrative
10	
11	**Story type**: "突破局限型" (7/8). Blind spot → reveal → fill. High conf.
12	
13	**Intro**: 4 paragraphs (5/8). P1 motivation → P2 prior work → P3 gap+approach → P4 three contributions [(1) discovery, (2) method, (3) generalization]. High conf.
14	
15	**Hooks** (pick one):
16	- English-centric gap: "Prior work focuses on English, leaving X unexplored" (xiao, zhou). 2/8.
17	- Name the meta-problem: "Square One Bias" (zhou) — forces acknowledgment.
18	- Cognitive dissonance: "LLMs are surprisingly well-calibrated" (joshi) — contradicts expectation.
19	- Pain narrowing: "most dangerous hallucination — confident wrong answers" (ji).
20	
21	**Tension**: Show standard practice actively fails, not just untried. "Fine-tuning doesn't change alignment" (liu). "Final layer overwrites multilingual signals" (zhou). "Aggregate correlation masks instance-level failure" (ravisankar). 3/8. High conf.
22	
23	## Insight Delivery
24	
25	**Layer-wise revelation** (3/8): Probe all layers → phase transition → motivates method. Signature move of this subfield.
26	
27	**Negative-as-evidence** (2/8): "X doesn't work" proves your design. SAE failure → distributed signal → justifies probe (miao2026coral). SFT doesn't align → explicit alignment needed (liu).
28	
29	**"Finding the knob"** (ji): Abstract concept → manipulable direction. Provides understanding + intervention.
30	
31	## Figures
32	
33	**Figure 1**: 50/50 motivation (analytical) vs method overview (method papers). High conf.
34	
35	**Layer analysis → line plots** (universal). Overlay conditions on same axes. Never tables for continuous layer data. High conf.
36	
37	**Xling transfer → heatmaps**. Side-by-side at contrasting layers (xiao: layer 3 vs 19). 3/8.
38	
39	**Gain highlighting**: Dashed baseline line (miao2026coral), before/after panels (xiao), curve gaps (ji). 4/8.
40	
41	**Progression**: motivation → method → finding → ablation → surprise. 14+ figures: front-load key results, appendix for per-language. 6/8.
42	
43	## Tables
44	
45	**Main result**: rows=methods, cols=datasets×metrics, grouped by dataset. Bold best. 3-4 baselines main, full in appendix. 5/8. High conf.
46	
47	**Ablations**: full numbers (8/8). No checkmark grids. Delta-from-base rare. High conf.
48	
49	**Division**: Continuous → figures. Discrete comparisons → tables. Per-language → appendix. Mechanistic = figure-heavy; benchmarking = table-heavy. High conf.
50	
51	**Appendix**: Main 1-2 models + key langs. Appendix exhaustive. zhou: 15 main, 122 appendix. 6/8.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83350e50-bbdc-47dd-9e33-d4095c505311",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "c13f1a05-9cb3-4a49-a742-95dc85591b86",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md",
      "content": "---\nname: xling-calib-direction-writing\ndescription: Writing and visual presentation patterns from 8 papers on cross-lingual calibration and representations\ntype: skill\n---\n\n# Cross-Lingual Calibration — Writing Patterns (8 papers)\n\n## Narrative\n\n**Story type**: \"突破局限型\" (7/8). Blind spot → reveal → fill. High conf.\n\n**Intro**: 4 paragraphs (5/8). P1 motivation → P2 prior work → P3 gap+approach → P4 three contributions [(1) discovery, (2) method, (3) generalization]. High conf.\n\n**Hooks** (pick one):\n- English-centric gap: \"Prior work focuses on English, leaving X unexplored\" (xiao, zhou). 2/8.\n- Name the meta-problem: \"Square One Bias\" (zhou) — forces acknowledgment.\n- Cognitive dissonance: \"LLMs are surprisingly well-calibrated\" (joshi) — contradicts expectation.\n- Pain narrowing: \"most dangerous hallucination — confident wrong answers\" (ji).\n\n**Tension**: Show standard practice actively fails, not just untried. \"Fine-tuning doesn't change alignment\" (liu). \"Final layer overwrites multilingual signals\" (zhou). \"Aggregate correlation masks instance-level failure\" (ravisankar). 3/8. High conf.\n\n## Insight Delivery\n\n**Layer-wise revelation** (3/8): Probe all layers → phase transition → motivates method. Signature move of this subfield.\n\n**Negative-as-evidence** (2/8): \"X doesn't work\" proves your design. SAE failure → distributed signal → justifies probe (miao2026coral). SFT doesn't align → explicit alignment needed (liu).\n\n**\"Finding the knob\"** (ji): Abstract concept → manipulable direction. Provides understanding + intervention.\n\n## Figures\n\n**Figure 1**: 50/50 motivation (analytical) vs method overview (method papers). High conf.\n\n**Layer analysis → line plots** (universal). Overlay conditions on same axes. Never tables for continuous layer data. High conf.\n\n**Xling transfer → heatmaps**. Side-by-side at contrasting layers (xiao: layer 3 vs 19). 3/8.\n\n**Gain highlighting**: Dashed baseline line (miao2026coral), before/after panels (xiao), curve gaps (ji). 4/8.\n\n**Progression**: motivation → method → finding → ablation → surprise. 14+ figures: front-load key results, appendix for per-language. 6/8.\n\n## Tables\n\n**Main result**: rows=methods, cols=datasets×metrics, grouped by dataset. Bold best. 3-4 baselines main, full in appendix. 5/8. High conf.\n\n**Ablations**: full numbers (8/8). No checkmark grids. Delta-from-base rare. High conf.\n\n**Division**: Continuous → figures. Discrete comparisons → tables. Per-language → appendix. Mechanistic = figure-heavy; benchmarking = table-heavy. High conf.\n\n**Appendix**: Main 1-2 models + key langs. Appendix exhaustive. zhou: 15 main, 122 appendix. 6/8.\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "83350e50-bbdc-47dd-9e33-d4095c505311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T04:09:23.461Z_

<details><summary>↩ Tool result · `toolu_01MsxT5aTGhUmna36U3DP6UB`</summary>

```text
total 136
drwxr-xr-x 2 ubuntu ubuntu  4096 May 21 04:09 .
drwxr-xr-x 5 ubuntu ubuntu  4096 May 21 04:09 ..
-rw-r--r-- 1 ubuntu ubuntu 54703 May 21 04:09 experiment_data.json
-rw-r--r-- 1 ubuntu ubuntu 56485 May 21 04:09 imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 15805 May 21 04:09 paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc888a2b-9c56-459d-94dd-5bf29d5a7107",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "61046756-7a97-447d-851e-1320e62a08c7",
  "toolUseResult": {
    "stdout": "total 136\ndrwxr-xr-x 2 ubuntu ubuntu  4096 May 21 04:09 .\ndrwxr-xr-x 5 ubuntu ubuntu  4096 May 21 04:09 ..\n-rw-r--r-- 1 ubuntu ubuntu 54703 May 21 04:09 experiment_data.json\n-rw-r--r-- 1 ubuntu ubuntu 56485 May 21 04:09 imagined_experiments.yaml\n-rw-r--r-- 1 ubuntu ubuntu 15805 May 21 04:09 paper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bc888a2b-9c56-459d-94dd-5bf29d5a7107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T04:09:24.226Z_

<details open><summary>🔧 Tool call — Read · `toolu_019YhSTqRivyzB7G7ppVdhcq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61046756-7a97-447d-851e-1320e62a08c7",
  "isSidechain": false,
  "requestId": "req_011CbF4JRynakLG8fNbwQinq",
  "type": "assistant",
  "uuid": "83350e50-bbdc-47dd-9e33-d4095c505311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVGQ1GamVf7Q1rc16bBus1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3963,
      "cache_creation_input_tokens": 21934,
      "cache_read_input_tokens": 23551,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21934,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3963,
          "output_tokens": 293,
          "cache_read_input_tokens": 23551,
          "cache_creation_input_tokens": 21934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21934
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

_source line 20 · 2026-05-21T04:09:44.538Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the complete LaTeX paper. This is a substantial paper with multiple experiments, tables, and sections. Let me compose it carefully.

Key structure:
1. Abstract
2. Introduction
3. Related Work
4. Method
5. Experiments (multiple subsections for each experiment)
6. Conclusion

Tables needed (from experiment data):
- Table 1: Qwen3-235B Zero-Shot Transfer AUROC (Language × Layer) - too large, summarize
- Table 2: Qwen3-235B Transfer Method Comparison
- Table 3: Llama 4 Scout Zero-Shot Transfer AUROC


- Tables 4-15: Architecture contrasts, ablations, decomposition analyses, similarity metrics, and capacity comparisons across different experimental conditions

Generating LaTeX tables... I'm mapping out the full paper structure with all the key results sections, then I'll need to draft the complete LaTeX while being careful to pull exact numbers from the experiment data and keep the larger tables in summarized form since the full matrices would be too unwieldy for publication.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c13f1a05-9cb3-4a49-a742-95dc85591b86",
  "isSidechain": false,
  "requestId": "req_011CbF4KRw63BDq5Qn7d4DPg",
  "type": "assistant",
  "uuid": "41f6ca66-fb61-4a98-be44-6db7ed44b2b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkWUUmr7BRdeZSTgoWfGqF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5370,
      "cache_read_input_tokens": 45485,
      "output_tokens": 15976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15976,
          "cache_read_input_tokens": 45485,
          "cache_creation_input_tokens": 5370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5370
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

_source line 21 · 2026-05-21T04:09:44.542Z_

Writing the full LaTeX paper now. This covers all 10 experiments with corresponding tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41f6ca66-fb61-4a98-be44-6db7ed44b2b6",
  "isSidechain": false,
  "requestId": "req_011CbF4KRw63BDq5Qn7d4DPg",
  "type": "assistant",
  "uuid": "e129ffcc-bafd-48f3-bd98-ac3f79447fce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkWUUmr7BRdeZSTgoWfGqF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5370,
      "cache_read_input_tokens": 45485,
      "output_tokens": 15976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15976,
          "cache_read_input_tokens": 45485,
          "cache_creation_input_tokens": 5370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5370
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

_source line 22 · 2026-05-21T04:14:14.963Z_

<details open><summary>🔧 Tool call — Write · `toolu_01DByaGEnUqKLbPrrfj8Qrtu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{adjustbox}\n\\usepackage{subcaption}\n\n\\definecolor{lightgreen}{rgb}{0.85,0.95,0.85}\n\\definecolor{lightyellow}{rgb}{1.0,1.0,0.85}\n\\definecolor{lightred}{rgb}{1.0,0.85,0.85}\n\\definecolor{lightgray}{rgb}{0.92,0.92,0.92}\n\n\\newcommand{\\caclr}{CaCLR}\n\\newcommand{\\dauroc}{$\\Delta$AUROC}\n\n\\title{Cross-Lingual Correctness Probe Transfer Reveals\\\\Architecture-Dependent Pareto Frontiers:\\\\Discovery, Negative Result, and Practical Recommendation}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nProbe-based calibration methods exploit internal correctness directions to assess LLM confidence, but remain English-only.\nWe present the first systematic evaluation of cross-lingual correctness probe transfer across 20 languages, two MoE architectures (Qwen3-235B-A22B, Llama~4 Scout), and one dense architecture (Gemma~4 31B), revealing three findings.\n\\textbf{(1)~Discovery:} A depth-transferability Pareto frontier emerges whose shape is architecture-dependent---Qwen3 shows a uniformly negative tradeoff (per-language Spearman $\\rho \\approx -0.50$) while Llama~4 Scout shows language-specific behavior (global $\\rho = -0.12$; 4/20 languages exhibit \\emph{positive} $\\rho$).\n\\textbf{(2)~Principled negative result:} CaCLR, a calibration-aware probe training objective combining BCE, smooth-binned ECE, and MMD consistency loss, fails to shift this frontier: a $\\beta$ sweep across three orders of magnitude yields negligible effect ($d = 0.07$, $p = 0.38$). CKA analysis suggests MMD matches marginals but cannot align the low-dimensional correctness subspace that rotates with depth.\n\\textbf{(3)~Practical recommendation:} Simple linear projection with ${\\sim}50$ parallel pairs provides +3.5pp AUROC over zero-shot transfer, surpassing CaCLR at only 20 pairs.\nA methodological warning accompanies these findings: control task analysis reveals that ${\\sim}27\\%$ of language-layer probing combinations exhibit selectivity below 0.05, concentrated in low-resource languages and shallow layers.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nNon-English languages suffer substantially worse calibration in multilingual LLMs: expected calibration error (ECE) can be 5$\\times$ higher than English.\nRecent work has shown that internal \\emph{correctness directions}---linearly accessible from intermediate representations---are orthogonal to verbalized confidence \\cite{miao2026steering}, implying that output-based calibration is structurally limited.\nProbe-based methods such as CORAL \\cite{miao2026coral} and correctness-confidence steering \\cite{miao2026steering} exploit this finding, but operate exclusively in English.\nWhether this entire research line generalizes beyond English is an open question.\n\nWe provide the first systematic test.\nProbing 20 languages across two large-scale MoE architectures (Qwen3-235B-A22B, 94 layers; Llama~4 Scout, 48 layers) and one dense architecture (Gemma~4 31B, 60 layers), we discover that cross-lingual correctness probe transfer is governed by a \\emph{depth-transferability Pareto frontier} whose shape is architecture-dependent (Section~\\ref{sec:pareto}).\nOn Qwen3, all 20 languages exhibit a consistent negative tradeoff between probe depth (and thus English AUROC) and cross-lingual transfer quality ($\\rho_{\\text{median}} = -0.48$).\nOn Llama~4 Scout, the tradeoff is language-specific: Arabic, Korean, and Hindi improve with depth while Chinese and Swahili degrade, producing a near-zero global correlation ($\\rho = -0.12$).\n\nTo test whether distributional matching can shift this frontier, we design CaCLR---a calibration-aware cross-lingual regularization objective combining BCE with smooth-binned ECE ($\\alpha$) and MMD consistency ($\\beta$) losses.\nA systematic $\\beta$ sweep across three orders of magnitude yields a principled negative result: the MMD component is inert (Cohen's $d = 0.07$, $p = 0.38$; Section~\\ref{sec:caclr}).\nCKA geometric analysis provides a suggestive explanation: MMD matches marginal distributions but cannot align the low-dimensional directional structure of correctness representations, which rotates as a function of depth (Section~\\ref{sec:cka}).\n\nThe constructive outcome is a practical recommendation: simple linear projection with ${\\sim}50$ parallel pairs yields +3.5pp AUROC over zero-shot transfer, surpassing CaCLR at only 20 pairs (Section~\\ref{sec:linproj}).\nDifficulty-controlled decomposition reveals that the transferable component of correctness signal is difficulty-shared and language-agnostic, while the degrading component is capability-specific (Section~\\ref{sec:decomp}).\nCross-lingual orthogonality between correctness and verbalized confidence persists across all 20 languages (max cosine 0.11), extending prior English-only findings (Section~\\ref{sec:ortho}).\n\nA methodological warning accompanies our findings: Hewitt \\& Liang control task analysis reveals that ${\\sim}27\\%$ of language-layer probing combinations exhibit selectivity below 0.05, concentrated in low-resource languages and shallow layers (Section~\\ref{sec:control}).\nWe recommend a minimum selectivity threshold for interpretable cross-lingual probing.\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Probe-Based Calibration.}\nCORAL \\cite{miao2026coral} trains cross-task correctness probes showing that correctness signals transfer across benchmarks but not across languages.\nMiao \\& Ungar (\\citeyear{miao2026steering}) demonstrate correctness-confidence orthogonality in English, establishing that output-based calibration is structurally limited.\nJi et al.\\ identify internal confidence directions as a ``manipulable knob'' for calibration.\nWe extend these English-only findings to 20 languages.\n\n\\paragraph{Cross-Lingual Probing.}\nXiao et al.\\ (\\citeyear{xiao2025}) transfer \\emph{knowledge boundary} probes (input-level answerability) across 8 languages.\nOur work targets \\emph{correctness} probes (output-dependent accuracy)---a fundamentally different signal---across 20 languages, with calibration rather than probing accuracy as the downstream metric.\nLACE \\cite{zhou2024lace} ensembles per-language layers but requires target-language labels.\nWe target zero-label transfer.\n\n\\paragraph{Cross-Lingual Alignment.}\nLinear projection for cross-lingual alignment is well-established in word embeddings (MUSE, \\citealp{conneau2018muse}; VecMap, \\citealp{artetxe2018vecmap}).\nOur linear projection is conceptually similar but operates on sentence-level correctness representations; the contribution is demonstrating effectiveness for probe transfer and characterizing sample efficiency.\n\n\\paragraph{Domain Adaptation Theory.}\nBen-David et al.\\ (\\citeyear{bendavid2010}) provide H-divergence bounds for domain adaptation; Zhao et al.\\ (\\citeyear{zhao2019}) show that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains.\nThis directly predicts CaCLR's MMD failure.\n\n\\paragraph{Representation Similarity.}\nCKA \\cite{kornblith2019cka} and SVCCA \\cite{raghu2017svcca} measure representational alignment.\nWe use CKA as a correlational (not mechanistic) analysis tool, reporting partial correlations controlling for depth.\n\n\\paragraph{Probing Methodology.}\nHewitt \\& Liang (\\citeyear{hewitt2019control}) introduce control tasks for probe validation.\nWe extend their framework cross-lingually and identify systematic capacity artifacts.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Correctness Probes}\n\\label{sec:probes}\n\nGiven a multilingual LLM with $L$ layers and an English MCQA dataset with items $\\{(x_i, y_i)\\}$ where $y_i \\in \\{0, 1\\}$ indicates correctness of the model's predicted answer, we train a logistic regression probe at each layer $\\ell$:\n\\begin{equation}\np_\\ell(y=1 \\mid \\mathbf{h}_\\ell) = \\sigma(\\mathbf{w}_\\ell^\\top \\mathbf{h}_\\ell + b_\\ell)\n\\end{equation}\nwhere $\\mathbf{h}_\\ell \\in \\mathbb{R}^d$ is the hidden representation at layer $\\ell$.\nWe evaluate with AUROC (discrimination) and ECE (calibration).\n\n\\paragraph{Zero-Shot Cross-Lingual Transfer.}\nThe English-trained probe is applied directly to target-language representations $\\mathbf{h}_\\ell^{(\\text{tgt})}$ without adaptation.\n\n\\paragraph{Transfer Conditions.}\nWe evaluate five transfer methods: (1)~zero-shot, (2)~mean-shift (center target representations to English mean), (3)~linear projection with $n$ parallel pairs, (4)~few-shot with $k$ target-language labels, (5)~CaCLR.\n\n\\paragraph{Mean-Shift Invariance.}\nUnder StandardScaler preprocessing and logistic regression, mean-shift adds a constant offset to all logits.\nSince AUROC depends only on rank ordering, $\\Delta\\text{AUROC} \\equiv 0$ mathematically.\n\n\\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}\n\\label{sec:caclr_method}\n\nCaCLR jointly optimizes English probe quality and cross-lingual consistency:\n\\begin{equation}\n\\mathcal{L}_{\\text{CaCLR}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{SB-ECE}}$ is smooth-binned ECE (differentiable calibration regularizer) and $\\mathcal{L}_{\\text{MMD}}$ is maximum mean discrepancy between English and target-language probe logits computed from parallel inputs:\n\\begin{equation}\n\\mathcal{L}_{\\text{MMD}} = \\text{MMD}^2_k\\big(f(\\mathbf{h}_\\ell^{(\\text{en})}), f(\\mathbf{h}_\\ell^{(\\text{tgt})})\\big)\n\\end{equation}\nusing Gaussian RBF kernel with median heuristic bandwidth.\nNote that MMD operates on 1-D probe logits $f(\\mathbf{h}) = \\mathbf{w}^\\top \\mathbf{h} + b$, a design limitation: it can only match marginal distributions of scalar outputs, not the high-dimensional geometric structure of representations.\n\n\\subsection{Difficulty-Capability Decomposition}\n\\label{sec:decomp_method}\n\nWe decompose the correctness signal into difficulty-shared (language-agnostic) and capability-specific (language-dependent) components.\nAn IRT difficulty probe $\\mathbf{w}_{\\text{diff}}$ is trained to predict item difficulty from English representations.\nThe difficulty direction is projected out:\n\\begin{equation}\n\\tilde{\\mathbf{h}}_\\ell = \\mathbf{h}_\\ell - \\frac{\\mathbf{h}_\\ell \\cdot \\mathbf{w}_{\\text{diff}}}{\\|\\mathbf{w}_{\\text{diff}}\\|^2} \\mathbf{w}_{\\text{diff}}\n\\end{equation}\nA correctness probe retrained on residuals $\\tilde{\\mathbf{h}}_\\ell$ should transfer better if difficulty is the shared component and capability is the language-specific component driving degradation.\n\n\\subsection{Linear Projection}\n\\label{sec:linproj_method}\n\nGiven $n$ parallel pairs $\\{(\\mathbf{h}_\\ell^{(\\text{en})}_i, \\mathbf{h}_\\ell^{(\\text{tgt})}_i)\\}$, we learn a linear mapping $\\mathbf{W}$ minimizing:\n\\begin{equation}\n\\min_{\\mathbf{W}} \\sum_i \\|\\mathbf{W} \\mathbf{h}_\\ell^{(\\text{tgt})}_i - \\mathbf{h}_\\ell^{(\\text{en})}_i\\|^2\n\\end{equation}\nThis directly estimates the rotation correction between source and target representation spaces.\n\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nQwen3-235B-A22B (94 layers, MoE, INT4 quantization), Llama~4 Scout (48 layers, MoE, W4A16), and Gemma~4 31B Dense (60 layers, FP16).\nQuantization validation (Section~\\ref{sec:quant}) confirms $\\leq$1.1pp AUROC difference vs.\\ FP16.\n\n\\paragraph{Languages.}\n20 languages spanning 3 resource tiers: \\textbf{High} (zh, es, fr, de, ja, pt, nl, ru), \\textbf{Mid} (ar, hi, ko, vi, tr, id, pl, uk), \\textbf{Low} (sw, bn, te).\nCamera-ready extension covers 52 languages.\n\n\\paragraph{Benchmark.}\nGlobalMMLU test split, partitioned into probe\\_train (70\\%) and eval (30\\%) via stratified split.\nEnglish BCE labels and parallel activations for MMD come from probe\\_train only.\nValidation on Belebele and MMLU-ProX.\n\n\\paragraph{Probed Layers.}\nQwen3: 24 layers (every 4th); Llama~4 Scout: 12 layers (every 4th); Gemma~4: 15 layers (every 4th).\n\n\\paragraph{CaCLR Implementation.}\nGaussian RBF kernel with median heuristic bandwidth; Adam optimizer ($\\text{lr} = 0.001$, cosine decay); 50 epochs with early stopping (patience 10 on val BCE); initialized from standard LR solution; batch size 256.\nAverage parallel set size per language: 9,800 items (min: 4,200 for Telugu, max: 14,042 for English).\n\n\\paragraph{Statistical Testing.}\nAll comparisons use bootstrap 95\\% CIs (1,000 resamples), paired permutation tests, and Cohen's $d$.\n\n% ============================================================\n\\section{Results}\n\n\\subsection{Pareto Frontier Discovery}\n\\label{sec:pareto}\n\n\\paragraph{Qwen3-235B: Uniform Strong Tradeoff.}\nTable~\\ref{tab:qwen_transfer} summarizes the depth-transferability tradeoff on Qwen3.\nEnglish AUROC peaks at layer 72 ($\\approx$77\\% depth) with AUROC = 0.80.\nHowever, the best \\emph{transfer} layer is L48 ($\\approx$51\\% depth), where average zero-shot AUROC across 19 languages is 0.669 vs.\\ 0.647 at L72---a 2.2pp gap.\nAll 20 languages exhibit negative Spearman $\\rho$ between depth and transfer AUROC ($\\rho_{\\text{median}} = -0.48$, range $[-0.58, -0.42]$), confirming a universal tradeoff on this architecture.\nLow-resource languages show stronger negative correlation (sw: $-0.58$, bn: $-0.56$, te: $-0.55$) due to weaker cross-lingual representations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{adjustbox}{max width=\\columnwidth}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{ZS AUROC}} & \\multirow{2}{*}{\\textbf{$\\rho$}} \\\\\n\\cmidrule(lr){2-3}\n\\textbf{Language} & \\textbf{L48} & \\textbf{L72} & \\\\\n\\midrule\nzh & 0.73 & 0.71 & $-0.45$ \\\\\nes & 0.72 & 0.70 & $-0.42$ \\\\\nfr & 0.71 & 0.70 & $-0.43$ \\\\\nde & 0.70 & 0.69 & $-0.44$ \\\\\nja & 0.69 & 0.67 & $-0.47$ \\\\\npt & 0.70 & 0.69 & $-0.43$ \\\\\nnl & 0.69 & 0.68 & $-0.44$ \\\\\nru & 0.69 & 0.67 & $-0.46$ \\\\\n\\midrule\nar & 0.67 & 0.65 & $-0.50$ \\\\\nhi & 0.66 & 0.64 & $-0.52$ \\\\\nko & 0.68 & 0.66 & $-0.48$ \\\\\nvi & 0.66 & 0.64 & $-0.51$ \\\\\ntr & 0.65 & 0.63 & $-0.53$ \\\\\nid & 0.67 & 0.65 & $-0.49$ \\\\\npl & 0.68 & 0.66 & $-0.46$ \\\\\nuk & 0.67 & 0.65 & $-0.47$ \\\\\n\\midrule\nsw & 0.58 & 0.55 & $-0.58$ \\\\\nbn & 0.57 & 0.54 & $-0.56$ \\\\\nte & 0.59 & 0.56 & $-0.55$ \\\\\n\\midrule\n\\textbf{Avg} & \\textbf{0.669} & \\textbf{0.647} & $-0.48$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\caption{Qwen3-235B zero-shot transfer AUROC at best transfer layer (L48, 51\\% depth) vs.\\ EN-optimal layer (L72, 77\\% depth), with per-language Spearman $\\rho$ (depth vs.\\ transfer AUROC). All $\\rho$ values are negative. Languages grouped by resource tier (High/Mid/Low).}\n\\label{tab:qwen_transfer}\n\\end{table}\n\n\\paragraph{Llama 4 Scout: Language-Specific Tradeoff.}\nTable~\\ref{tab:arch_contrast} contrasts per-language $\\rho$ across architectures.\nLlama~4 Scout shows a qualitatively different pattern: global $\\rho = -0.12$, with 4 languages exhibiting \\emph{positive} $\\rho$ (ar: $+0.15$, ko: $+0.12$, hi: $+0.08$, id: $+0.02$), 8 near zero, and only 8 significantly negative.\nThis means deeper layers improve transfer for some languages while degrading it for others---there is no single ``best transfer layer'' on this architecture.\nPer-language best layers vary from L20 (sw, bn) to L40 (ar, ko), whereas on Qwen3 all languages converge near L48.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{adjustbox}{max width=\\columnwidth}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Language} & \\textbf{Qwen3 $\\rho$} & \\textbf{Llama4 $\\rho$} \\\\\n\\midrule\nzh & $-0.45$ & $-0.35$ \\\\\nes & $-0.42$ & $-0.30$ \\\\\nfr & $-0.43$ & $-0.28$ \\\\\nde & $-0.44$ & $-0.32$ \\\\\nja & $-0.47$ & $-0.25$ \\\\\npt & $-0.43$ & $-0.27$ \\\\\nnl & $-0.44$ & $-0.22$ \\\\\nru & $-0.46$ & $-0.18$ \\\\\n\\midrule\nar & $-0.50$ & $\\mathbf{+0.15}$ \\\\\nhi & $-0.52$ & $\\mathbf{+0.08}$ \\\\\nko & $-0.48$ & $\\mathbf{+0.12}$ \\\\\nvi & $-0.51$ & $-0.05$ \\\\\ntr & $-0.53$ & $-0.08$ \\\\\nid & $-0.49$ & $\\mathbf{+0.02}$ \\\\\npl & $-0.46$ & $-0.10$ \\\\\nuk & $-0.47$ & $-0.05$ \\\\\n\\midrule\nsw & $-0.58$ & $-0.42$ \\\\\nbn & $-0.56$ & $-0.38$ \\\\\nte & $-0.55$ & $-0.30$ \\\\\n\\midrule\n\\textbf{Median} & $-0.48$ & $-0.10$ \\\\\n\\textbf{Range} & [$-0.58$, $-0.42$] & [$-0.42$, $+0.15$] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\caption{Architecture contrast: per-language Spearman $\\rho$ (depth vs.\\ zero-shot transfer AUROC). Qwen3 shows uniformly negative $\\rho$; Llama~4 Scout shows language-specific behavior with 4 positive values (\\textbf{bold}).}\n\\label{tab:arch_contrast}\n\\end{table}\n\n\\paragraph{Gemma 4 31B Dense.}\nThe dense architecture exhibits the strongest and most uniform tradeoff ($\\rho_{\\text{median}} = -0.55$, range $[-0.62, -0.48]$, $\\sigma = 0.04$), consistent with the absence of MoE routing heterogeneity.\nEN best AUROC is 0.79 at layer 42 (70\\% depth); best transfer layer is L30 (50\\% depth) with median zero-shot AUROC 0.67.\nThe CKA cliff is steeper (magnitude 0.18) than both MoE models, providing the strongest architecture contrast.\n\n\\subsection{CaCLR: A Principled Negative Result}\n\\label{sec:caclr}\n\n\\paragraph{$\\beta$ Sweep.}\nTable~\\ref{tab:beta_sweep} presents the MMD consistency loss $\\beta$ sweep across three orders of magnitude.\nNo value of $\\beta$ achieves $p < 0.05$ or $d > 0.2$.\nAt low $\\beta$ (0.001--0.01), MMD gradients are too weak to influence probe weights.\nAt moderate $\\beta$ (0.03--0.1), MMD pushes toward marginal distribution alignment of 1-D logits without addressing correctness direction rotation.\nAt high $\\beta$ (0.3--1.0), MMD dominates the loss, degrading discriminative power ($\\Delta$AUROC $= -0.010$ at $\\beta = 1.0$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n$\\beta$ & $\\Delta$AUROC & $\\Delta$ECE \\\\\n\\midrule\n\\rowcolor{lightgray}\n0 (ref.) & 0.000 & 0.000 \\\\\n0.001 & +0.002 & $-0.001$ \\\\\n0.003 & +0.001 & $-0.001$ \\\\\n0.01 & +0.001 & 0.000 \\\\\n0.03 & $-0.001$ & +0.001 \\\\\n0.1 & $-0.002$ & +0.002 \\\\\n0.3 & $-0.005$ & +0.003 \\\\\n1.0 & $-0.010$ & +0.005 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\small Paired perm.\\ $p = 0.38$, Cohen's $d = 0.07$} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\beta$ sweep (MMD consistency weight). $\\Delta$AUROC and $\\Delta$ECE are relative to $\\beta = 0$ (i.e., $\\alpha$-only baseline with $\\alpha = 0.5$). No $\\beta$ value produces a significant effect.}\n\\label{tab:beta_sweep}\n\\end{table}\n\n\\paragraph{Component Ablation.}\nTable~\\ref{tab:ablation} decomposes CaCLR into its components.\nThe $\\alpha$ (SB-ECE) term reduces ECE from 0.175 to 0.125 ($-$5.0pp) with minimal AUROC impact (+0.004pp).\nThe $\\beta$ (MMD) term contributes $+$0.001pp AUROC and $-$0.001pp ECE---functionally zero.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{ZS AUROC} & \\textbf{ECE} \\\\\n\\midrule\nBCE only & 0.647 & 0.175 \\\\\n$+\\alpha$ (SB-ECE) & 0.651 & 0.125 \\\\\n$+\\beta$ (MMD) & 0.649 & 0.173 \\\\\n$+\\alpha + \\beta$ (Full) & 0.652 & 0.124 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CaCLR component ablation (Qwen3, L48). The $\\alpha$ term drives ECE improvement; $\\beta$ contributes nothing.}\n\\label{tab:ablation}\n\\end{table}\n\n\\paragraph{Full Method Comparison.}\nTable~\\ref{tab:method_comparison} ranks all transfer methods.\nLinear projection with 50 pairs (+3.5pp on Qwen3, +3.2pp on Llama~4) and few-shot with 100 labels (+4.6pp, +4.4pp) significantly outperform zero-shot transfer.\nCaCLR achieves only +0.8pp on Qwen3 and +0.6pp on Llama~4, almost entirely from the $\\alpha$ component.\nMean-shift produces $\\Delta$AUROC $\\equiv 0$ as predicted by the rank-invariance proof.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{adjustbox}{max width=\\columnwidth}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Qwen3 (L48)}} & \\multicolumn{2}{c}{\\textbf{Llama4 (L28)}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Method} & AUROC & $\\Delta$ & AUROC & $\\Delta$ \\\\\n\\midrule\nZero-shot & 0.669 & --- & 0.638 & --- \\\\\nMean-shift & 0.669 & 0.000 & 0.638 & 0.000 \\\\\nCaCLR ($\\alpha$ only) & 0.673 & +0.004 & 0.642 & +0.004 \\\\\nCaCLR (full) & 0.677 & +0.008 & 0.644 & +0.006 \\\\\n\\midrule\nLinear proj.\\ (50) & 0.704 & +0.035 & 0.670 & +0.032 \\\\\nFew-shot (25) & 0.695 & +0.026 & 0.662 & +0.024 \\\\\nFew-shot (100) & 0.715 & +0.046 & 0.682 & +0.044 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\caption{Transfer method comparison. Linear projection and few-shot methods significantly outperform zero-shot and CaCLR. $\\Delta$ is vs.\\ zero-shot. Bootstrap 95\\% CI for linear proj.\\ $\\Delta$: $[0.025, 0.045]$ (Qwen3).}\n\\label{tab:method_comparison}\n\\end{table}\n\n\\subsection{CKA Geometric Analysis}\n\\label{sec:cka}\n\nCKA (linear kernel) between English and 19 target languages declines monotonically with depth: median CKA drops from 0.83 at shallow layers to 0.48 at deep layers.\nAt 70\\% depth, resource-tier banding is clear (High: 0.58, Mid: 0.46, Low: 0.34).\nQwen3 exhibits a steeper CKA cliff at 72\\% depth (magnitude 0.15) than Llama~4 at 65\\% depth (0.08), consistent with the stronger Pareto tradeoff.\n\n\\paragraph{Partial Correlation Analysis.}\nTable~\\ref{tab:cka_partial} presents the key statistical test.\nPooled CKA--transfer correlation is $r = 0.52$ ($p < 10^{-6}$), but this is confounded by depth.\nPartial correlation controlling for normalized depth drops to $r = 0.18$ ($p = 0.11$)---CKA adds marginal information beyond depth itself.\nWe therefore frame CKA as \\emph{suggestive correlational analysis}, not geometric explanation.\n\nThe between-language claim remains valid: at matched depth, languages with higher CKA show less transfer degradation ($r = 0.52$, $p = 0.02$, $n = 19$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Analysis} & $r$ & $p$ & \\textbf{Interpretation} \\\\\n\\midrule\nCKA--transfer (pooled) & 0.52 & $<10^{-6}$ & Strong but confounded \\\\\nDepth--transfer & --- & --- & Primary driver \\\\\nCKA $|$ depth (partial) & 0.18 & 0.11 & Suggestive only \\\\\n\\midrule\nBetween-lang (same depth) & 0.52 & 0.02 & Valid cross-lang claim \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA as transfer predictor. Partial correlation controlling depth reduces $r$ from 0.52 to 0.18, indicating CKA's predictive power is largely driven by depth. Between-language correlation at matched depth remains significant.}\n\\label{tab:cka_partial}\n\\end{table}\n\n\\paragraph{Subspace Angle Analysis.}\nCorrectness subspace angles between English and target languages increase from median 15\\textdegree{} at shallow layers to 38\\textdegree{} at deep layers, far below the random baseline of 72\\textdegree.\nThis quantifies the rotation of correctness directions with depth: the subspace persists but rotates, consistent with the Pareto frontier---deeper layers encode stronger English correctness but rotate away from cross-lingual alignment.\n\n\\subsection{Difficulty-Capability Decomposition}\n\\label{sec:decomp}\n\nTable~\\ref{tab:decomp} summarizes the decomposition ablation.\nRemoving the difficulty direction before retraining correctness probes improves transfer in 65\\% of language-layer combinations (paired permutation $p = 0.028$, Cohen's $d = 0.25$).\nThe effect is concentrated at deep layers (78\\% improved, $d \\approx 0.35$) and high-resource languages (72\\% improved), with diminishing returns for low-resource languages (50\\% improved) where probes are noisier.\nA random-direction control confirms specificity: random removal yields $d = 0.05$ ($p = 0.42$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Med.\\ $\\Delta$AUC} & \\textbf{\\% Impr.} & $d$ \\\\\n\\midrule\nDifficulty removed & +0.015 & 65\\% & 0.25 \\\\\nRandom direction & +0.003 & 52\\% & 0.05 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\small \\textit{Difficulty removed, by depth:}} \\\\\n\\quad Shallow (20--40\\%) & +0.005 & 48\\% & --- \\\\\n\\quad Mid (40--60\\%) & +0.015 & 65\\% & --- \\\\\n\\quad Deep (60--90\\%) & +0.022 & 78\\% & --- \\\\\n\\midrule\n\\multicolumn{4}{l}{\\small \\textit{Difficulty removed, by resource tier:}} \\\\\n\\quad High & +0.020 & 72\\% & --- \\\\\n\\quad Mid & +0.013 & 63\\% & --- \\\\\n\\quad Low & +0.008 & 50\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition ablation. Removing the difficulty direction improves transfer, concentrated at deep layers and high-resource languages. Random-direction control confirms specificity ($p = 0.42$). Effect size is small ($d = 0.25$), supporting a qualitative rather than quantitative claim.}\n\\label{tab:decomp}\n\\end{table}\n\nThe IRT difficulty probe achieves median $R^2 = 0.40$ (range $[0.22, 0.52]$), peaking at 65\\% depth.\nThe difficulty--correctness cosine of 0.20 (range $[0.10, 0.32]$) indicates incomplete separation---the decomposition is informative but not clean.\n\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:ortho}\n\nTable~\\ref{tab:ortho} extends the correctness-confidence orthogonality finding to 20 languages.\nAll cosine values remain below 0.12 (English: 0.032 on Qwen3, 0.036 on Llama~4), confirming that output-based calibration is structurally limited regardless of language.\nA resource-tier gradient emerges: high-resource median 0.037, mid 0.054, low 0.090 (Spearman $\\rho = -0.58$, $p = 0.008$ with log resource estimate).\nCross-architecture correlation is 0.94, indicating the pattern is model-agnostic.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{adjustbox}{max width=\\columnwidth}\n\\begin{tabular}{lcc|lcc}\n\\toprule\n\\textbf{Lang} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Lang} & \\textbf{Qwen3} & \\textbf{Llama4} \\\\\n\\midrule\nen & .032 & .036 & ar & .055 & .060 \\\\\nzh & .038 & .042 & hi & .058 & .065 \\\\\nes & .035 & .038 & ko & .050 & .055 \\\\\nfr & .033 & .036 & vi & .060 & .068 \\\\\nde & .036 & .040 & tr & .062 & .070 \\\\\nja & .040 & .045 & id & .048 & .052 \\\\\npt & .034 & .037 & pl & .040 & .045 \\\\\nnl & .033 & .036 & uk & .045 & .050 \\\\\nru & .042 & .048 & sw & .095 & .110 \\\\\n &  &  & bn & .088 & .098 \\\\\n &  &  & te & .078 & .085 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Tier medians:}} & \\multicolumn{3}{l}{High: .037, Mid: .054, Low: .090} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\caption{Correctness-confidence cosine similarity across 20 languages and 2 architectures. All values $< 0.12$. Resource-tier gradient: $\\rho = -0.58$, $p = 0.008$.}\n\\label{tab:ortho}\n\\end{table}\n\n\\subsection{Linear Projection Sample Efficiency}\n\\label{sec:linproj}\n\nTable~\\ref{tab:linproj} presents the linear projection learning curve.\nWith only 10 parallel pairs, median $\\Delta$AUROC is +1.2pp; at 50 pairs, it reaches +3.5pp (90\\% of achievable improvement).\nDiminishing returns set in around 60 pairs (knee), consistent with cross-lingual alignment literature.\nLinear projection surpasses CaCLR at only 20 pairs.\nLow-resource languages benefit most (+4.5pp at 50 pairs vs.\\ +2.8pp for high-resource), as their larger geometric misalignment provides more room for correction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{rccl}\n\\toprule\n\\textbf{Pairs} & \\textbf{Med.\\ $\\Delta$AUC} & \\textbf{Std} & \\textbf{Note} \\\\\n\\midrule\n10 & +0.012 & 0.022 & Below CaCLR \\\\\n20 & +0.023 & 0.016 & Matches CaCLR \\\\\n50 & +0.035 & 0.011 & 90\\% of max \\\\\n100 & +0.040 & 0.008 & Near saturation \\\\\n200 & +0.042 & 0.007 & Saturated \\\\\n\\midrule\n\\multicolumn{4}{l}{\\small CaCLR surpassed at ${\\sim}$20 pairs; knee at ${\\sim}$60} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection sample efficiency. $\\sim$50 parallel pairs achieve 90\\% of maximum improvement. CaCLR is surpassed at $\\sim$20 pairs.}\n\\label{tab:linproj}\n\\end{table}\n\n\\subsection{Control Task Analysis}\n\\label{sec:control}\n\nTable~\\ref{tab:control} presents the Hewitt \\& Liang control task analysis extended to 20 languages.\nApproximately 27\\% of language-layer combinations exhibit selectivity $< 0.05$, concentrated along two dimensions: shallow layers universally (85\\% below threshold at 0--20\\% depth) and low-resource languages at mid-depth (42\\% below for sw/bn/te).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Shallow} & \\textbf{Mid} & \\textbf{Deep} \\\\\n& (0--30\\%) & (30--60\\%) & (60--100\\%) \\\\\n\\midrule\nHigh resource & 80\\% & 12\\% & 5\\% \\\\\nMid resource & 88\\% & 22\\% & 8\\% \\\\\nLow resource & 92\\% & 38\\% & 15\\% \\\\\n\\midrule\n\\textbf{All} & 85\\% & 18\\% & 8\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Fraction of language-layer combinations with selectivity $< 0.05$ (capacity artifact risk). Total: ${\\sim}$27\\%. Shallow layers and low-resource languages are most affected.}\n\\label{tab:control}\n\\end{table}\n\nThis has two implications.\nFirst, shallow-layer low selectivity is expected and benign---the paper does not claim correctness signal at shallow layers.\nSecond, low-resource mid-depth artifacts are a genuine concern: probes with selectivity $< 0.05$ may reflect capacity memorization rather than correctness signal.\nWe recommend selectivity $\\geq 0.05$ as a minimum threshold for interpretable cross-lingual probing.\nOur own statistical tests exclude combinations below this threshold where feasible.\n\n\\subsection{Probe Complexity Validation}\n\\label{sec:probe_complexity}\n\nMLP probes (2-layer) achieve +2.2pp English AUROC over logistic regression (0.825 vs.\\ 0.80 on Qwen3; 0.80 vs.\\ 0.78 on Llama~4) but suffer a 5.4pp larger transfer gap (18.5\\% vs.\\ 13.1\\% on Qwen3).\nLogistic regression transfers better for 82\\% of languages; exceptions are zh and es where MLP nonlinearity partially transfers.\nThis validates the focus on linear probes: the transferable component of correctness signal is geometric (linear subspace), and nonlinear components are language-specific.\n\n\\subsection{Additional Validation}\n\\label{sec:quant}\n\n\\paragraph{Quantization.}\nComparing W4A16 vs.\\ FP16 on Llama~4 Scout (5 layers, 5\\% subset) yields max $\\Delta$AUROC of 0.009 with Pearson $r = 0.996$.\nGPTQ-Int4 vs.\\ FP16 on Qwen3 yields max $\\Delta$AUROC of 0.011 ($r = 0.995$).\nAll differences are within bootstrap CIs.\n\n\\paragraph{Cross-Benchmark Generalization.}\nOn Belebele (reading comprehension), Pareto $\\rho = -0.45$ and linear projection $\\Delta = +3.0$pp.\nOn MMLU-ProX (translated MCQA), $\\rho = -0.48$ and $\\Delta = +3.4$pp.\nMethod ranking is consistent across all three benchmarks (rank correlation with GlobalMMLU: 0.80 for Belebele, 0.90 for MMLU-ProX).\nCaCLR $\\beta$ remains inert on all benchmarks.\n\n\\paragraph{Extended Language Coverage.}\nExpanding to 52 languages, median zero-shot AUROC is 0.64 (range $[0.50, 0.73]$).\n10 languages fall below 0.55 (am, my, zu, sn, rw, xh, ny, mg), reflecting minimal pretraining representation.\nWith linear projection, 67\\% of languages (35/52) achieve viable calibration ($\\text{AUROC} > 0.60$).\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why Does MMD Fail?}\nMMD operates on 1-D probe logits and can only match marginal distributions (mean and variance of scalar outputs).\nCross-lingual correctness misalignment is \\emph{geometric rotation}---the correctness direction points differently in different languages' activation spaces.\nThis rotation occurs in high-dimensional space \\emph{before} the probe, where MMD on post-probe logits cannot reach.\nZhao et al.\\ (\\citeyear{zhao2019}) predict exactly this: marginal matching fails when $P(Y|X)$ differs across domains, as correctness label distributions are language-dependent.\nLinear projection succeeds because it directly estimates the rotation matrix via parallel pairs.\n\n\\paragraph{Architecture Dependence.}\nWith $n = 3$ architectures differing in type (MoE vs.\\ dense), scale, layer count, and training data, we cannot attribute tradeoff shape to specific architectural features.\nThe finding is observational: practitioners must empirically characterize the Pareto frontier for their target architecture rather than assuming a universal depth rule.\n\n\\paragraph{Limitations.}\n(1)~MCQA only: clean correctness labeling requires closed-form evaluation; open-ended generation requires different signal types.\n(2)~$n = 3$ architectures: insufficient for causal attribution.\n(3)~Decomposition effect size ($d = 0.25$) supports a qualitative claim only.\n(4)~CKA is correlational after controlling for depth.\n(5)~27\\% of probing combinations are potential capacity artifacts, particularly for low-resource languages.\n\n% ============================================================\n\\section{Conclusion}\n\nWe present the first systematic study of cross-lingual correctness probe transfer, revealing an architecture-dependent depth-transferability Pareto frontier.\nThe natural distributional-matching approach (CaCLR with MMD consistency) fails---a principled negative result explained by the geometric nature of cross-lingual misalignment.\nThe practical recommendation is simple: linear projection with ${\\sim}50$ parallel pairs provides +3.5pp AUROC, surpassing CaCLR at 20 pairs and achieving 90\\% of the maximum achievable improvement.\nCross-lingual orthogonality between correctness and confidence persists across all 20 tested languages (max cosine 0.11), establishing output-based calibration as structurally limited regardless of language.\nWe further contribute a methodological warning: approximately 27\\% of cross-lingual probing results are capacity artifacts, and recommend selectivity $\\geq 0.05$ as a minimum interpretability threshold.\n\n% ============================================================\n% References\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018vecmap}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proceedings of ACL}, pages 789--798.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79(1):151--175.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018muse}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019control}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proceedings of EMNLP}, pages 2733--2743.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019cka}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proceedings of ICML}, pages 3519--3529.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nQingyi Miao, Mingxuan Ju, and Lyle Ungar. 2026a.\n\\newblock {CORAL}: Cross-task correctness probes for LLM calibration.\n\\newblock In {\\em Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026steering}\nQingyi Miao and Lyle Ungar. 2026.\n\\newblock Steering LLM confidence via orthogonal correctness directions.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Pires et~al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proceedings of ACL}, pages 4996--5001.\n\n\\bibitem[\\protect\\citename{Raghu et~al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In {\\em Proceedings of NeurIPS}, pages 6076--6085.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020mdl}\nElena Voita and Ivan Titov. 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proceedings of EMNLP}, pages 183--196.\n\n\\bibitem[\\protect\\citename{Wu and Dredze}2019]{wu2019beto}\nShijie Wu and Mark Dredze. 2019.\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proceedings of EMNLP}, pages 833--844.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025}\nShuyue Xiao, Zhiwei Zhang, and Linyi Yang. 2025.\n\\newblock Cross-lingual knowledge boundary probing in large language models.\n\\newblock In {\\em Proceedings of ACL}, pages 1204--1218.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019}\nHan Zhao, Remi Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proceedings of ICML}, pages 7523--7532.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2024]{zhou2024lace}\nKaitlyn Zhou, Dan Jurafsky, and Tatsunori Hashimoto. 2024.\n\\newblock {LACE}: Language-aware cross-lingual calibration.\n\\newblock In {\\em Proceedings of EMNLP}, pages 2891--2906.\n\n\\end{thebibliography}\n\n% ============================================================\n\\appendix\n\\section{Supplementary Results}\n\n\\subsection{Probe Complexity (Table S1)}\n\nTable~\\ref{tab:probe_complexity_supp} compares logistic regression and MLP probes.\nMLP achieves higher English AUROC but larger transfer gap at all layers, with the gap widening at deeper layers (6.5pp at deep vs.\\ 2.0pp at shallow).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{EN AUROC}} & \\multicolumn{2}{c}{\\textbf{Transfer Gap}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Model} & LogReg & MLP & LogReg & MLP \\\\\n\\midrule\nQwen3 & 0.800 & 0.825 & 13.1\\% & 18.5\\% \\\\\nLlama4 & 0.780 & 0.800 & 14.2\\% & 19.5\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\small LogReg better transfer: 82\\% of langs} \\\\\n\\multicolumn{5}{l}{\\small LogReg ECE: 0.135; MLP ECE: 0.148} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Probe complexity comparison. MLP gains English AUROC at the cost of larger transfer gap.}\n\\label{tab:probe_complexity_supp}\n\\end{table}\n\n\\subsection{Cross-Benchmark Generalization (Table S2)}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{EN} & \\textbf{ZS} & $\\rho$ & \\textbf{LP $\\Delta$} & $\\beta$ $\\Delta$ \\\\\n\\midrule\nGlobalMMLU & 0.80 & 0.669 & $-0.50$ & +.035 & +.002 \\\\\nBelebele & 0.77 & 0.650 & $-0.45$ & +.030 & +.002 \\\\\nMMLU-ProX & 0.81 & 0.670 & $-0.48$ & +.034 & +.003 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\small Rank corr.\\ with GlobalMMLU: Belebele 0.80, MMLU-ProX 0.90} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (Qwen3). EN = EN best AUROC; ZS = zero-shot median; LP = linear projection 50 pairs. CaCLR $\\beta$ inert across all benchmarks.}\n\\label{tab:benchmark_supp}\n\\end{table}\n\n\\subsection{Quantization Validation (Table S3)}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Llama4 (W4A16)}} & \\multicolumn{2}{c}{\\textbf{Qwen3 (INT4)}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Layer} & $\\Delta$AUC & & $\\Delta$AUC & \\\\\n\\midrule\nL8 / L16 & $-0.004$ & & $-0.006$ & \\\\\nL16 / L32 & $-0.004$ & & $-0.005$ & \\\\\nL24 / L48 & $-0.005$ & & $-0.004$ & \\\\\nL32 / L64 & $-0.007$ & & $-0.005$ & \\\\\nL40 / L80 & $-0.009$ & & $-0.011$ & \\\\\n\\midrule\n\\textbf{Mean} & $-0.004$ & $r{=}.996$ & $-0.005$ & $r{=}.995$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quantization validation. All $\\Delta$AUROC within bootstrap CIs. Quantization does not distort correctness signals.}\n\\label{tab:quant_supp}\n\\end{table}\n\n\\subsection{Control Task Details (Table S4)}\n\nEnglish selectivity increases with depth on both architectures: shallow average 0.03, mid 0.15--0.18, deep 0.24--0.27.\nLow-resource languages show lower selectivity at matched depth (median 0.09 vs.\\ 0.19 for high-resource), with the worst combinations being sw at 0--50\\% depth (median selectivity 0.02) and te at 0--40\\% depth (0.02).\nAll control task AUROCs remain near chance (median 0.50, range $[0.48, 0.53]$), confirming negligible probe capacity for memorizing random labels.\n\n\\subsection{Three-Architecture Summary (Table CR1)}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{adjustbox}{max width=\\columnwidth}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{EN} & \\textbf{ZS} & $\\rho_{\\text{med}}$ & $\\rho_{\\sigma}$ & \\textbf{CKA cliff} & \\textbf{LP $\\Delta$} \\\\\n\\midrule\nQwen3-235B & MoE & .80 & .669 & $-.48$ & .05 & .15 & +.035 \\\\\nLlama4 Scout & MoE & .78 & .638 & $-.10$ & .12 & .08 & +.032 \\\\\nGemma4 31B & Dense & .79 & .670 & $-.55$ & .04 & .18 & +.033 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\caption{Three-architecture comparison. Dense model shows strongest, most uniform Pareto ($\\rho_\\sigma = 0.04$). MoE models vary: Qwen3 moderate uniform, Llama4 language-specific.}\n\\label{tab:three_arch}\n\\end{table}\n\n\\subsection{Extended 52-Language Coverage (Table CR2)}\n\nOf 52 languages tested, 32 achieve zero-shot AUROC $> 0.60$ and 25 exceed 0.65.\nWith linear projection (+3.2pp median), 35/52 (67\\%) reach viable calibration.\n8 new languages fall below 0.55 (am, my, zu, sn, rw, xh, ny, mg), reflecting minimal pretraining representation.\nThe resource-tier gradient replicates at scale ($\\rho_{\\text{median}} = -0.47$ across 52 languages).\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e129ffcc-bafd-48f3-bd98-ac3f79447fce",
  "isSidechain": false,
  "requestId": "req_011CbF4KRw63BDq5Qn7d4DPg",
  "type": "assistant",
  "uuid": "2e72f5f9-61d8-4db9-85b0-7aae1f3bfb01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkWUUmr7BRdeZSTgoWfGqF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5370,
      "cache_read_input_tokens": 45485,
      "output_tokens": 15976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15976,
          "cache_read_input_tokens": 45485,
          "cache_creation_input_tokens": 5370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5370
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

_source line 23 · 2026-05-21T04:14:14.981Z_

<details><summary>↩ Tool result · `toolu_01DByaGEnUqKLbPrrfj8Qrtu`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e72f5f9-61d8-4db9-85b0-7aae1f3bfb01",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "f5e90016-3444-4d2c-b895-2f98abe5212d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{adjustbox}\n\\usepackage{subcaption}\n\n\\definecolor{lightgreen}{rgb}{0.85,0.95,0.85}\n\\definecolor{lightyellow}{rgb}{1.0,1.0,0.85}\n\\definecolor{lightred}{rgb}{1.0,0.85,0.85}\n\\definecolor{lightgray}{rgb}{0.92,0.92,0.92}\n\n\\newcommand{\\caclr}{CaCLR}\n\\newcommand{\\dauroc}{$\\Delta$AUROC}\n\n\\title{Cross-Lingual Correctness Probe Transfer Reveals\\\\Architecture-Dependent Pareto Frontiers:\\\\Discovery, Negative Result, and Practical Recommendation}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nProbe-based calibration methods exploit internal correctness directions to assess LLM confidence, but remain English-only.\nWe present the first systematic evaluation of cross-lingual correctness probe transfer across 20 languages, two MoE architectures (Qwen3-235B-A22B, Llama~4 Scout), and one dense architecture (Gemma~4 31B), revealing three findings.\n\\textbf{(1)~Discovery:} A depth-transferability Pareto frontier emerges whose shape is architecture-dependent---Qwen3 shows a uniformly negative tradeoff (per-language Spearman $\\rho \\approx -0.50$) while Llama~4 Scout shows language-specific behavior (global $\\rho = -0.12$; 4/20 languages exhibit \\emph{positive} $\\rho$).\n\\textbf{(2)~Principled negative result:} CaCLR, a calibration-aware probe training objective combining BCE, smooth-binned ECE, and MMD consistency loss, fails to shift this frontier: a $\\beta$ sweep across three orders of magnitude yields negligible effect ($d = 0.07$, $p = 0.38$). CKA analysis suggests MMD matches marginals but cannot align the low-dimensional correctness subspace that rotates with depth.\n\\textbf{(3)~Practical recommendation:} Simple linear projection with ${\\sim}50$ parallel pairs provides +3.5pp AUROC over zero-shot transfer, surpassing CaCLR at only 20 pairs.\nA methodological warning accompanies these findings: control task analysis reveals that ${\\sim}27\\%$ of language-layer probing combinations exhibit selectivity below 0.05, concentrated in low-resource languages and shallow layers.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nNon-English languages suffer substantially worse calibration in multilingual LLMs: expected calibration error (ECE) can be 5$\\times$ higher than English.\nRecent work has shown that internal \\emph{correctness directions}---linearly accessible from intermediate representations---are orthogonal to verbalized confidence \\cite{miao2026steering}, implying that output-based calibration is structurally limited.\nProbe-based methods such as CORAL \\cite{miao2026coral} and correctness-confidence steering \\cite{miao2026steering} exploit this finding, but operate exclusively in English.\nWhether this entire research line generalizes beyond English is an open question.\n\nWe provide the first systematic test.\nProbing 20 languages across two large-scale MoE architectures (Qwen3-235B-A22B, 94 layers; Llama~4 Scout, 48 layers) and one dense architecture (Gemma~4 31B, 60 layers), we discover that cross-lingual correctness probe transfer is governed by a \\emph{depth-transferability Pareto frontier} whose shape is architecture-dependent (Section~\\ref{sec:pareto}).\nOn Qwen3, all 20 languages exhibit a consistent negative tradeoff between probe depth (and thus English AUROC) and cross-lingual transfer quality ($\\rho_{\\text{median}} = -0.48$).\nOn Llama~4 Scout, the tradeoff is language-specific: Arabic, Korean, and Hindi improve with depth while Chinese and Swahili degrade, producing a near-zero global correlation ($\\rho = -0.12$).\n\nTo test whether distributional matching can shift this frontier, we design CaCLR---a calibration-aware cross-lingual regularization objective combining BCE with smooth-binned ECE ($\\alpha$) and MMD consistency ($\\beta$) losses.\nA systematic $\\beta$ sweep across three orders of magnitude yields a principled negative result: the MMD component is inert (Cohen's $d = 0.07$, $p = 0.38$; Section~\\ref{sec:caclr}).\nCKA geometric analysis provides a suggestive explanation: MMD matches marginal distributions but cannot align the low-dimensional directional structure of correctness representations, which rotates as a function of depth (Section~\\ref{sec:cka}).\n\nThe constructive outcome is a practical recommendation: simple linear projection with ${\\sim}50$ parallel pairs yields +3.5pp AUROC over zero-shot transfer, surpassing CaCLR at only 20 pairs (Section~\\ref{sec:linproj}).\nDifficulty-controlled decomposition reveals that the transferable component of correctness signal is difficulty-shared and language-agnostic, while the degrading component is capability-specific (Section~\\ref{sec:decomp}).\nCross-lingual orthogonality between correctness and verbalized confidence persists across all 20 languages (max cosine 0.11), extending prior English-only findings (Section~\\ref{sec:ortho}).\n\nA methodological warning accompanies our findings: Hewitt \\& Liang control task analysis reveals that ${\\sim}27\\%$ of language-layer probing combinations exhibit selectivity below 0.05, concentrated in low-resource languages and shallow layers (Section~\\ref{sec:control}).\nWe recommend a minimum selectivity threshold for interpretable cross-lingual probing.\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Probe-Based Calibration.}\nCORAL \\cite{miao2026coral} trains cross-task correctness probes showing that correctness signals transfer across benchmarks but not across languages.\nMiao \\& Ungar (\\citeyear{miao2026steering}) demonstrate correctness-confidence orthogonality in English, establishing that output-based calibration is structurally limited.\nJi et al.\\ identify internal confidence directions as a ``manipulable knob'' for calibration.\nWe extend these English-only findings to 20 languages.\n\n\\paragraph{Cross-Lingual Probing.}\nXiao et al.\\ (\\citeyear{xiao2025}) transfer \\emph{knowledge boundary} probes (input-level answerability) across 8 languages.\nOur work targets \\emph{correctness} probes (output-dependent accuracy)---a fundamentally different signal---across 20 languages, with calibration rather than probing accuracy as the downstream metric.\nLACE \\cite{zhou2024lace} ensembles per-language layers but requires target-language labels.\nWe target zero-label transfer.\n\n\\paragraph{Cross-Lingual Alignment.}\nLinear projection for cross-lingual alignment is well-established in word embeddings (MUSE, \\citealp{conneau2018muse}; VecMap, \\citealp{artetxe2018vecmap}).\nOur linear projection is conceptually similar but operates on sentence-level correctness representations; the contribution is demonstrating effectiveness for probe transfer and characterizing sample efficiency.\n\n\\paragraph{Domain Adaptation Theory.}\nBen-David et al.\\ (\\citeyear{bendavid2010}) provide H-divergence bounds for domain adaptation; Zhao et al.\\ (\\citeyear{zhao2019}) show that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains.\nThis directly predicts CaCLR's MMD failure.\n\n\\paragraph{Representation Similarity.}\nCKA \\cite{kornblith2019cka} and SVCCA \\cite{raghu2017svcca} measure representational alignment.\nWe use CKA as a correlational (not mechanistic) analysis tool, reporting partial correlations controlling for depth.\n\n\\paragraph{Probing Methodology.}\nHewitt \\& Liang (\\citeyear{hewitt2019control}) introduce control tasks for probe validation.\nWe extend their framework cross-lingually and identify systematic capacity artifacts.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Correctness Probes}\n\\label{sec:probes}\n\nGiven a multilingual LLM with $L$ layers and an English MCQA dataset with items $\\{(x_i, y_i)\\}$ where $y_i \\in \\{0, 1\\}$ indicates correctness of the model's predicted answer, we train a logistic regression probe at each layer $\\ell$:\n\\begin{equation}\np_\\ell(y=1 \\mid \\mathbf{h}_\\ell) = \\sigma(\\mathbf{w}_\\ell^\\top \\mathbf{h}_\\ell + b_\\ell)\n\\end{equation}\nwhere $\\mathbf{h}_\\ell \\in \\mathbb{R}^d$ is the hidden representation at layer $\\ell$.\nWe evaluate with AUROC (discrimination) and ECE (calibration).\n\n\\paragraph{Zero-Shot Cross-Lingual Transfer.}\nThe English-trained probe is applied directly to target-language representations $\\mathbf{h}_\\ell^{(\\text{tgt})}$ without adaptation.\n\n\\paragraph{Transfer Conditions.}\nWe evaluate five transfer methods: (1)~zero-shot, (2)~mean-shift (center target representations to English mean), (3)~linear projection with $n$ parallel pairs, (4)~few-shot with $k$ target-language labels, (5)~CaCLR.\n\n\\paragraph{Mean-Shift Invariance.}\nUnder StandardScaler preprocessing and logistic regression, mean-shift adds a constant offset to all logits.\nSince AUROC depends only on rank ordering, $\\Delta\\text{AUROC} \\equiv 0$ mathematically.\n\n\\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}\n\\label{sec:caclr_method}\n\nCaCLR jointly optimizes English probe quality and cross-lingual consistency:\n\\begin{equation}\n\\mathcal{L}_{\\text{CaCLR}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{SB-ECE}}$ is smooth-binned ECE (differentiable calibration regularizer) and $\\mathcal{L}_{\\text{MMD}}$ is maximum mean discrepancy between English and target-language probe logits computed from parallel inputs:\n\\begin{equation}\n\\mathcal{L}_{\\text{MMD}} = \\text{MMD}^2_k\\big(f(\\mathbf{h}_\\ell^{(\\text{en})}), f(\\mathbf{h}_\\ell^{(\\text{tgt})})\\big)\n\\end{equation}\nusing Gaussian RBF kernel with median heuristic bandwidth.\nNote that MMD operates on 1-D probe logits $f(\\mathbf{h}) = \\mathbf{w}^\\top \\mathbf{h} + b$, a design limitation: it can only match marginal distributions of scalar outputs, not the high-dimensional geometric structure of representations.\n\n\\subsection{Difficulty-Capability Decomposition}\n\\label{sec:decomp_method}\n\nWe decompose the correctness signal into difficulty-shared (language-agnostic) and capability-specific (language-dependent) components.\nAn IRT difficulty probe $\\mathbf{w}_{\\text{diff}}$ is trained to predict item difficulty from English representations.\nThe difficulty direction is projected out:\n\\begin{equation}\n\\tilde{\\mathbf{h}}_\\ell = \\mathbf{h}_\\ell - \\frac{\\mathbf{h}_\\ell \\cdot \\mathbf{w}_{\\text{diff}}}{\\|\\mathbf{w}_{\\text{diff}}\\|^2} \\mathbf{w}_{\\text{diff}}\n\\end{equation}\nA correctness probe retrained on residuals $\\tilde{\\mathbf{h}}_\\ell$ should transfer better if difficulty is the shared component and capability is the language-specific component driving degradation.\n\n\\subsection{Linear Projection}\n\\label{sec:linproj_method}\n\nGiven $n$ parallel pairs $\\{(\\mathbf{h}_\\ell^{(\\text{en})}_i, \\mathbf{h}_\\ell^{(\\text{tgt})}_i)\\}$, we learn a linear mapping $\\mathbf{W}$ minimizing:\n\\begin{equation}\n\\min_{\\mathbf{W}} \\sum_i \\|\\mathbf{W} \\mathbf{h}_\\ell^{(\\text{tgt})}_i - \\mathbf{h}_\\ell^{(\\text{en})}_i\\|^2\n\\end{equation}\nThis directly estimates the rotation correction between source and target representation spaces.\n\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nQwen3-235B-A22B (94 layers, MoE, INT4 quantization), Llama~4 Scout (48 layers, MoE, W4A16), and Gemma~4 31B Dense (60 layers, FP16).\nQuantization validation (Section~\\ref{sec:quant}) confirms $\\leq$1.1pp AUROC difference vs.\\ FP16.\n\n\\paragraph{Languages.}\n20 languages spanning 3 resource tiers: \\textbf{High} (zh, es, fr, de, ja, pt, nl, ru), \\textbf{Mid} (ar, hi, ko, vi, tr, id, pl, uk), \\textbf{Low} (sw, bn, te).\nCamera-ready extension covers 52 languages.\n\n\\paragraph{Benchmark.}\nGlobalMMLU test split, partitioned into probe\\_train (70\\%) and eval (30\\%) via stratified split.\nEnglish BCE labels and parallel activations for MMD come from probe\\_train only.\nValidation on Belebele and MMLU-ProX.\n\n\\paragraph{Probed Layers.}\nQwen3: 24 layers (every 4th); Llama~4 Scout: 12 layers (every 4th); Gemma~4: 15 layers (every 4th).\n\n\\paragraph{CaCLR Implementation.}\nGaussian RBF kernel with median heuristic bandwidth; Adam optimizer ($\\text{lr} = 0.001$, cosine decay); 50 epochs with early stopping (patience 10 on val BCE); initialized from standard LR solution; batch size 256.\nAverage parallel set size per language: 9,800 items (min: 4,200 for Telugu, max: 14,042 for English).\n\n\\paragraph{Statistical Testing.}\nAll comparisons use bootstrap 95\\% CIs (1,000 resamples), paired permutation tests, and Cohen's $d$.\n\n% ============================================================\n\\section{Results}\n\n\\subsection{Pareto Frontier Discovery}\n\\label{sec:pareto}\n\n\\paragraph{Qwen3-235B: Uniform Strong Tradeoff.}\nTable~\\ref{tab:qwen_transfer} summarizes the depth-transferability tradeoff on Qwen3.\nEnglish AUROC peaks at layer 72 ($\\approx$77\\% depth) with AUROC = 0.80.\nHowever, the best \\emph{transfer} layer is L48 ($\\approx$51\\% depth), where average zero-shot AUROC across 19 languages is 0.669 vs.\\ 0.647 at L72---a 2.2pp gap.\nAll 20 languages exhibit negative Spearman $\\rho$ between depth and transfer AUROC ($\\rho_{\\text{median}} = -0.48$, range $[-0.58, -0.42]$), confirming a universal tradeoff on this architecture.\nLow-resource languages show stronger negative correlation (sw: $-0.58$, bn: $-0.56$, te: $-0.55$) due to weaker cross-lingual representations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{adjustbox}{max width=\\columnwidth}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{ZS AUROC}} & \\multirow{2}{*}{\\textbf{$\\rho$}} \\\\\n\\cmidrule(lr){2-3}\n\\textbf{Language} & \\textbf{L48} & \\textbf{L72} & \\\\\n\\midrule\nzh & 0.73 & 0.71 & $-0.45$ \\\\\nes & 0.72 & 0.70 & $-0.42$ \\\\\nfr & 0.71 & 0.70 & $-0.43$ \\\\\nde & 0.70 & 0.69 & $-0.44$ \\\\\nja & 0.69 & 0.67 & $-0.47$ \\\\\npt & 0.70 & 0.69 & $-0.43$ \\\\\nnl & 0.69 & 0.68 & $-0.44$ \\\\\nru & 0.69 & 0.67 & $-0.46$ \\\\\n\\midrule\nar & 0.67 & 0.65 & $-0.50$ \\\\\nhi & 0.66 & 0.64 & $-0.52$ \\\\\nko & 0.68 & 0.66 & $-0.48$ \\\\\nvi & 0.66 & 0.64 & $-0.51$ \\\\\ntr & 0.65 & 0.63 & $-0.53$ \\\\\nid & 0.67 & 0.65 & $-0.49$ \\\\\npl & 0.68 & 0.66 & $-0.46$ \\\\\nuk & 0.67 & 0.65 & $-0.47$ \\\\\n\\midrule\nsw & 0.58 & 0.55 & $-0.58$ \\\\\nbn & 0.57 & 0.54 & $-0.56$ \\\\\nte & 0.59 & 0.56 & $-0.55$ \\\\\n\\midrule\n\\textbf{Avg} & \\textbf{0.669} & \\textbf{0.647} & $-0.48$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\caption{Qwen3-235B zero-shot transfer AUROC at best transfer layer (L48, 51\\% depth) vs.\\ EN-optimal layer (L72, 77\\% depth), with per-language Spearman $\\rho$ (depth vs.\\ transfer AUROC). All $\\rho$ values are negative. Languages grouped by resource tier (High/Mid/Low).}\n\\label{tab:qwen_transfer}\n\\end{table}\n\n\\paragraph{Llama 4 Scout: Language-Specific Tradeoff.}\nTable~\\ref{tab:arch_contrast} contrasts per-language $\\rho$ across architectures.\nLlama~4 Scout shows a qualitatively different pattern: global $\\rho = -0.12$, with 4 languages exhibiting \\emph{positive} $\\rho$ (ar: $+0.15$, ko: $+0.12$, hi: $+0.08$, id: $+0.02$), 8 near zero, and only 8 significantly negative.\nThis means deeper layers improve transfer for some languages while degrading it for others---there is no single ``best transfer layer'' on this architecture.\nPer-language best layers vary from L20 (sw, bn) to L40 (ar, ko), whereas on Qwen3 all languages converge near L48.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{adjustbox}{max width=\\columnwidth}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Language} & \\textbf{Qwen3 $\\rho$} & \\textbf{Llama4 $\\rho$} \\\\\n\\midrule\nzh & $-0.45$ & $-0.35$ \\\\\nes & $-0.42$ & $-0.30$ \\\\\nfr & $-0.43$ & $-0.28$ \\\\\nde & $-0.44$ & $-0.32$ \\\\\nja & $-0.47$ & $-0.25$ \\\\\npt & $-0.43$ & $-0.27$ \\\\\nnl & $-0.44$ & $-0.22$ \\\\\nru & $-0.46$ & $-0.18$ \\\\\n\\midrule\nar & $-0.50$ & $\\mathbf{+0.15}$ \\\\\nhi & $-0.52$ & $\\mathbf{+0.08}$ \\\\\nko & $-0.48$ & $\\mathbf{+0.12}$ \\\\\nvi & $-0.51$ & $-0.05$ \\\\\ntr & $-0.53$ & $-0.08$ \\\\\nid & $-0.49$ & $\\mathbf{+0.02}$ \\\\\npl & $-0.46$ & $-0.10$ \\\\\nuk & $-0.47$ & $-0.05$ \\\\\n\\midrule\nsw & $-0.58$ & $-0.42$ \\\\\nbn & $-0.56$ & $-0.38$ \\\\\nte & $-0.55$ & $-0.30$ \\\\\n\\midrule\n\\textbf{Median} & $-0.48$ & $-0.10$ \\\\\n\\textbf{Range} & [$-0.58$, $-0.42$] & [$-0.42$, $+0.15$] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\caption{Architecture contrast: per-language Spearman $\\rho$ (depth vs.\\ zero-shot transfer AUROC). Qwen3 shows uniformly negative $\\rho$; Llama~4 Scout shows language-specific behavior with 4 positive values (\\textbf{bold}).}\n\\label{tab:arch_contrast}\n\\end{table}\n\n\\paragraph{Gemma 4 31B Dense.}\nThe dense architecture exhibits the strongest and most uniform tradeoff ($\\rho_{\\text{median}} = -0.55$, range $[-0.62, -0.48]$, $\\sigma = 0.04$), consistent with the absence of MoE routing heterogeneity.\nEN best AUROC is 0.79 at layer 42 (70\\% depth); best transfer layer is L30 (50\\% depth) with median zero-shot AUROC 0.67.\nThe CKA cliff is steeper (magnitude 0.18) than both MoE models, providing the strongest architecture contrast.\n\n\\subsection{CaCLR: A Principled Negative Result}\n\\label{sec:caclr}\n\n\\paragraph{$\\beta$ Sweep.}\nTable~\\ref{tab:beta_sweep} presents the MMD consistency loss $\\beta$ sweep across three orders of magnitude.\nNo value of $\\beta$ achieves $p < 0.05$ or $d > 0.2$.\nAt low $\\beta$ (0.001--0.01), MMD gradients are too weak to influence probe weights.\nAt moderate $\\beta$ (0.03--0.1), MMD pushes toward marginal distribution alignment of 1-D logits without addressing correctness direction rotation.\nAt high $\\beta$ (0.3--1.0), MMD dominates the loss, degrading discriminative power ($\\Delta$AUROC $= -0.010$ at $\\beta = 1.0$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n$\\beta$ & $\\Delta$AUROC & $\\Delta$ECE \\\\\n\\midrule\n\\rowcolor{lightgray}\n0 (ref.) & 0.000 & 0.000 \\\\\n0.001 & +0.002 & $-0.001$ \\\\\n0.003 & +0.001 & $-0.001$ \\\\\n0.01 & +0.001 & 0.000 \\\\\n0.03 & $-0.001$ & +0.001 \\\\\n0.1 & $-0.002$ & +0.002 \\\\\n0.3 & $-0.005$ & +0.003 \\\\\n1.0 & $-0.010$ & +0.005 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\small Paired perm.\\ $p = 0.38$, Cohen's $d = 0.07$} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\beta$ sweep (MMD consistency weight). $\\Delta$AUROC and $\\Delta$ECE are relative to $\\beta = 0$ (i.e., $\\alpha$-only baseline with $\\alpha = 0.5$). No $\\beta$ value produces a significant effect.}\n\\label{tab:beta_sweep}\n\\end{table}\n\n\\paragraph{Component Ablation.}\nTable~\\ref{tab:ablation} decomposes CaCLR into its components.\nThe $\\alpha$ (SB-ECE) term reduces ECE from 0.175 to 0.125 ($-$5.0pp) with minimal AUROC impact (+0.004pp).\nThe $\\beta$ (MMD) term contributes $+$0.001pp AUROC and $-$0.001pp ECE---functionally zero.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{ZS AUROC} & \\textbf{ECE} \\\\\n\\midrule\nBCE only & 0.647 & 0.175 \\\\\n$+\\alpha$ (SB-ECE) & 0.651 & 0.125 \\\\\n$+\\beta$ (MMD) & 0.649 & 0.173 \\\\\n$+\\alpha + \\beta$ (Full) & 0.652 & 0.124 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CaCLR component ablation (Qwen3, L48). The $\\alpha$ term drives ECE improvement; $\\beta$ contributes nothing.}\n\\label{tab:ablation}\n\\end{table}\n\n\\paragraph{Full Method Comparison.}\nTable~\\ref{tab:method_comparison} ranks all transfer methods.\nLinear projection with 50 pairs (+3.5pp on Qwen3, +3.2pp on Llama~4) and few-shot with 100 labels (+4.6pp, +4.4pp) significantly outperform zero-shot transfer.\nCaCLR achieves only +0.8pp on Qwen3 and +0.6pp on Llama~4, almost entirely from the $\\alpha$ component.\nMean-shift produces $\\Delta$AUROC $\\equiv 0$ as predicted by the rank-invariance proof.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{adjustbox}{max width=\\columnwidth}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Qwen3 (L48)}} & \\multicolumn{2}{c}{\\textbf{Llama4 (L28)}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Method} & AUROC & $\\Delta$ & AUROC & $\\Delta$ \\\\\n\\midrule\nZero-shot & 0.669 & --- & 0.638 & --- \\\\\nMean-shift & 0.669 & 0.000 & 0.638 & 0.000 \\\\\nCaCLR ($\\alpha$ only) & 0.673 & +0.004 & 0.642 & +0.004 \\\\\nCaCLR (full) & 0.677 & +0.008 & 0.644 & +0.006 \\\\\n\\midrule\nLinear proj.\\ (50) & 0.704 & +0.035 & 0.670 & +0.032 \\\\\nFew-shot (25) & 0.695 & +0.026 & 0.662 & +0.024 \\\\\nFew-shot (100) & 0.715 & +0.046 & 0.682 & +0.044 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\caption{Transfer method comparison. Linear projection and few-shot methods significantly outperform zero-shot and CaCLR. $\\Delta$ is vs.\\ zero-shot. Bootstrap 95\\% CI for linear proj.\\ $\\Delta$: $[0.025, 0.045]$ (Qwen3).}\n\\label{tab:method_comparison}\n\\end{table}\n\n\\subsection{CKA Geometric Analysis}\n\\label{sec:cka}\n\nCKA (linear kernel) between English and 19 target languages declines monotonically with depth: median CKA drops from 0.83 at shallow layers to 0.48 at deep layers.\nAt 70\\% depth, resource-tier banding is clear (High: 0.58, Mid: 0.46, Low: 0.34).\nQwen3 exhibits a steeper CKA cliff at 72\\% depth (magnitude 0.15) than Llama~4 at 65\\% depth (0.08), consistent with the stronger Pareto tradeoff.\n\n\\paragraph{Partial Correlation Analysis.}\nTable~\\ref{tab:cka_partial} presents the key statistical test.\nPooled CKA--transfer correlation is $r = 0.52$ ($p < 10^{-6}$), but this is confounded by depth.\nPartial correlation controlling for normalized depth drops to $r = 0.18$ ($p = 0.11$)---CKA adds marginal information beyond depth itself.\nWe therefore frame CKA as \\emph{suggestive correlational analysis}, not geometric explanation.\n\nThe between-language claim remains valid: at matched depth, languages with higher CKA show less transfer degradation ($r = 0.52$, $p = 0.02$, $n = 19$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Analysis} & $r$ & $p$ & \\textbf{Interpretation} \\\\\n\\midrule\nCKA--transfer (pooled) & 0.52 & $<10^{-6}$ & Strong but confounded \\\\\nDepth--transfer & --- & --- & Primary driver \\\\\nCKA $|$ depth (partial) & 0.18 & 0.11 & Suggestive only \\\\\n\\midrule\nBetween-lang (same depth) & 0.52 & 0.02 & Valid cross-lang claim \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA as transfer predictor. Partial correlation controlling depth reduces $r$ from 0.52 to 0.18, indicating CKA's predictive power is largely driven by depth. Between-language correlation at matched depth remains significant.}\n\\label{tab:cka_partial}\n\\end{table}\n\n\\paragraph{Subspace Angle Analysis.}\nCorrectness subspace angles between English and target languages increase from median 15\\textdegree{} at shallow layers to 38\\textdegree{} at deep layers, far below the random baseline of 72\\textdegree.\nThis quantifies the rotation of correctness directions with depth: the subspace persists but rotates, consistent with the Pareto frontier---deeper layers encode stronger English correctness but rotate away from cross-lingual alignment.\n\n\\subsection{Difficulty-Capability Decomposition}\n\\label{sec:decomp}\n\nTable~\\ref{tab:decomp} summarizes the decomposition ablation.\nRemoving the difficulty direction before retraining correctness probes improves transfer in 65\\% of language-layer combinations (paired permutation $p = 0.028$, Cohen's $d = 0.25$).\nThe effect is concentrated at deep layers (78\\% improved, $d \\approx 0.35$) and high-resource languages (72\\% improved), with diminishing returns for low-resource languages (50\\% improved) where probes are noisier.\nA random-direction control confirms specificity: random removal yields $d = 0.05$ ($p = 0.42$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Med.\\ $\\Delta$AUC} & \\textbf{\\% Impr.} & $d$ \\\\\n\\midrule\nDifficulty removed & +0.015 & 65\\% & 0.25 \\\\\nRandom direction & +0.003 & 52\\% & 0.05 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\small \\textit{Difficulty removed, by depth:}} \\\\\n\\quad Shallow (20--40\\%) & +0.005 & 48\\% & --- \\\\\n\\quad Mid (40--60\\%) & +0.015 & 65\\% & --- \\\\\n\\quad Deep (60--90\\%) & +0.022 & 78\\% & --- \\\\\n\\midrule\n\\multicolumn{4}{l}{\\small \\textit{Difficulty removed, by resource tier:}} \\\\\n\\quad High & +0.020 & 72\\% & --- \\\\\n\\quad Mid & +0.013 & 63\\% & --- \\\\\n\\quad Low & +0.008 & 50\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition ablation. Removing the difficulty direction improves transfer, concentrated at deep layers and high-resource languages. Random-direction control confirms specificity ($p = 0.42$). Effect size is small ($d = 0.25$), supporting a qualitative rather than quantitative claim.}\n\\label{tab:decomp}\n\\end{table}\n\nThe IRT difficulty probe achieves median $R^2 = 0.40$ (range $[0.22, 0.52]$), peaking at 65\\% depth.\nThe difficulty--correctness cosine of 0.20 (range $[0.10, 0.32]$) indicates incomplete separation---the decomposition is informative but not clean.\n\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:ortho}\n\nTable~\\ref{tab:ortho} extends the correctness-confidence orthogonality finding to 20 languages.\nAll cosine values remain below 0.12 (English: 0.032 on Qwen3, 0.036 on Llama~4), confirming that output-based calibration is structurally limited regardless of language.\nA resource-tier gradient emerges: high-resource median 0.037, mid 0.054, low 0.090 (Spearman $\\rho = -0.58$, $p = 0.008$ with log resource estimate).\nCross-architecture correlation is 0.94, indicating the pattern is model-agnostic.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{adjustbox}{max width=\\columnwidth}\n\\begin{tabular}{lcc|lcc}\n\\toprule\n\\textbf{Lang} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Lang} & \\textbf{Qwen3} & \\textbf{Llama4} \\\\\n\\midrule\nen & .032 & .036 & ar & .055 & .060 \\\\\nzh & .038 & .042 & hi & .058 & .065 \\\\\nes & .035 & .038 & ko & .050 & .055 \\\\\nfr & .033 & .036 & vi & .060 & .068 \\\\\nde & .036 & .040 & tr & .062 & .070 \\\\\nja & .040 & .045 & id & .048 & .052 \\\\\npt & .034 & .037 & pl & .040 & .045 \\\\\nnl & .033 & .036 & uk & .045 & .050 \\\\\nru & .042 & .048 & sw & .095 & .110 \\\\\n &  &  & bn & .088 & .098 \\\\\n &  &  & te & .078 & .085 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Tier medians:}} & \\multicolumn{3}{l}{High: .037, Mid: .054, Low: .090} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\caption{Correctness-confidence cosine similarity across 20 languages and 2 architectures. All values $< 0.12$. Resource-tier gradient: $\\rho = -0.58$, $p = 0.008$.}\n\\label{tab:ortho}\n\\end{table}\n\n\\subsection{Linear Projection Sample Efficiency}\n\\label{sec:linproj}\n\nTable~\\ref{tab:linproj} presents the linear projection learning curve.\nWith only 10 parallel pairs, median $\\Delta$AUROC is +1.2pp; at 50 pairs, it reaches +3.5pp (90\\% of achievable improvement).\nDiminishing returns set in around 60 pairs (knee), consistent with cross-lingual alignment literature.\nLinear projection surpasses CaCLR at only 20 pairs.\nLow-resource languages benefit most (+4.5pp at 50 pairs vs.\\ +2.8pp for high-resource), as their larger geometric misalignment provides more room for correction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{rccl}\n\\toprule\n\\textbf{Pairs} & \\textbf{Med.\\ $\\Delta$AUC} & \\textbf{Std} & \\textbf{Note} \\\\\n\\midrule\n10 & +0.012 & 0.022 & Below CaCLR \\\\\n20 & +0.023 & 0.016 & Matches CaCLR \\\\\n50 & +0.035 & 0.011 & 90\\% of max \\\\\n100 & +0.040 & 0.008 & Near saturation \\\\\n200 & +0.042 & 0.007 & Saturated \\\\\n\\midrule\n\\multicolumn{4}{l}{\\small CaCLR surpassed at ${\\sim}$20 pairs; knee at ${\\sim}$60} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection sample efficiency. $\\sim$50 parallel pairs achieve 90\\% of maximum improvement. CaCLR is surpassed at $\\sim$20 pairs.}\n\\label{tab:linproj}\n\\end{table}\n\n\\subsection{Control Task Analysis}\n\\label{sec:control}\n\nTable~\\ref{tab:control} presents the Hewitt \\& Liang control task analysis extended to 20 languages.\nApproximately 27\\% of language-layer combinations exhibit selectivity $< 0.05$, concentrated along two dimensions: shallow layers universally (85\\% below threshold at 0--20\\% depth) and low-resource languages at mid-depth (42\\% below for sw/bn/te).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Shallow} & \\textbf{Mid} & \\textbf{Deep} \\\\\n& (0--30\\%) & (30--60\\%) & (60--100\\%) \\\\\n\\midrule\nHigh resource & 80\\% & 12\\% & 5\\% \\\\\nMid resource & 88\\% & 22\\% & 8\\% \\\\\nLow resource & 92\\% & 38\\% & 15\\% \\\\\n\\midrule\n\\textbf{All} & 85\\% & 18\\% & 8\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Fraction of language-layer combinations with selectivity $< 0.05$ (capacity artifact risk). Total: ${\\sim}$27\\%. Shallow layers and low-resource languages are most affected.}\n\\label{tab:control}\n\\end{table}\n\nThis has two implications.\nFirst, shallow-layer low selectivity is expected and benign---the paper does not claim correctness signal at shallow layers.\nSecond, low-resource mid-depth artifacts are a genuine concern: probes with selectivity $< 0.05$ may reflect capacity memorization rather than correctness signal.\nWe recommend selectivity $\\geq 0.05$ as a minimum threshold for interpretable cross-lingual probing.\nOur own statistical tests exclude combinations below this threshold where feasible.\n\n\\subsection{Probe Complexity Validation}\n\\label{sec:probe_complexity}\n\nMLP probes (2-layer) achieve +2.2pp English AUROC over logistic regression (0.825 vs.\\ 0.80 on Qwen3; 0.80 vs.\\ 0.78 on Llama~4) but suffer a 5.4pp larger transfer gap (18.5\\% vs.\\ 13.1\\% on Qwen3).\nLogistic regression transfers better for 82\\% of languages; exceptions are zh and es where MLP nonlinearity partially transfers.\nThis validates the focus on linear probes: the transferable component of correctness signal is geometric (linear subspace), and nonlinear components are language-specific.\n\n\\subsection{Additional Validation}\n\\label{sec:quant}\n\n\\paragraph{Quantization.}\nComparing W4A16 vs.\\ FP16 on Llama~4 Scout (5 layers, 5\\% subset) yields max $\\Delta$AUROC of 0.009 with Pearson $r = 0.996$.\nGPTQ-Int4 vs.\\ FP16 on Qwen3 yields max $\\Delta$AUROC of 0.011 ($r = 0.995$).\nAll differences are within bootstrap CIs.\n\n\\paragraph{Cross-Benchmark Generalization.}\nOn Belebele (reading comprehension), Pareto $\\rho = -0.45$ and linear projection $\\Delta = +3.0$pp.\nOn MMLU-ProX (translated MCQA), $\\rho = -0.48$ and $\\Delta = +3.4$pp.\nMethod ranking is consistent across all three benchmarks (rank correlation with GlobalMMLU: 0.80 for Belebele, 0.90 for MMLU-ProX).\nCaCLR $\\beta$ remains inert on all benchmarks.\n\n\\paragraph{Extended Language Coverage.}\nExpanding to 52 languages, median zero-shot AUROC is 0.64 (range $[0.50, 0.73]$).\n10 languages fall below 0.55 (am, my, zu, sn, rw, xh, ny, mg), reflecting minimal pretraining representation.\nWith linear projection, 67\\% of languages (35/52) achieve viable calibration ($\\text{AUROC} > 0.60$).\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why Does MMD Fail?}\nMMD operates on 1-D probe logits and can only match marginal distributions (mean and variance of scalar outputs).\nCross-lingual correctness misalignment is \\emph{geometric rotation}---the correctness direction points differently in different languages' activation spaces.\nThis rotation occurs in high-dimensional space \\emph{before} the probe, where MMD on post-probe logits cannot reach.\nZhao et al.\\ (\\citeyear{zhao2019}) predict exactly this: marginal matching fails when $P(Y|X)$ differs across domains, as correctness label distributions are language-dependent.\nLinear projection succeeds because it directly estimates the rotation matrix via parallel pairs.\n\n\\paragraph{Architecture Dependence.}\nWith $n = 3$ architectures differing in type (MoE vs.\\ dense), scale, layer count, and training data, we cannot attribute tradeoff shape to specific architectural features.\nThe finding is observational: practitioners must empirically characterize the Pareto frontier for their target architecture rather than assuming a universal depth rule.\n\n\\paragraph{Limitations.}\n(1)~MCQA only: clean correctness labeling requires closed-form evaluation; open-ended generation requires different signal types.\n(2)~$n = 3$ architectures: insufficient for causal attribution.\n(3)~Decomposition effect size ($d = 0.25$) supports a qualitative claim only.\n(4)~CKA is correlational after controlling for depth.\n(5)~27\\% of probing combinations are potential capacity artifacts, particularly for low-resource languages.\n\n% ============================================================\n\\section{Conclusion}\n\nWe present the first systematic study of cross-lingual correctness probe transfer, revealing an architecture-dependent depth-transferability Pareto frontier.\nThe natural distributional-matching approach (CaCLR with MMD consistency) fails---a principled negative result explained by the geometric nature of cross-lingual misalignment.\nThe practical recommendation is simple: linear projection with ${\\sim}50$ parallel pairs provides +3.5pp AUROC, surpassing CaCLR at 20 pairs and achieving 90\\% of the maximum achievable improvement.\nCross-lingual orthogonality between correctness and confidence persists across all 20 tested languages (max cosine 0.11), establishing output-based calibration as structurally limited regardless of language.\nWe further contribute a methodological warning: approximately 27\\% of cross-lingual probing results are capacity artifacts, and recommend selectivity $\\geq 0.05$ as a minimum interpretability threshold.\n\n% ============================================================\n% References\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018vecmap}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proceedings of ACL}, pages 789--798.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79(1):151--175.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018muse}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019control}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proceedings of EMNLP}, pages 2733--2743.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019cka}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proceedings of ICML}, pages 3519--3529.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nQingyi Miao, Mingxuan Ju, and Lyle Ungar. 2026a.\n\\newblock {CORAL}: Cross-task correctness probes for LLM calibration.\n\\newblock In {\\em Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026steering}\nQingyi Miao and Lyle Ungar. 2026.\n\\newblock Steering LLM confidence via orthogonal correctness directions.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Pires et~al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proceedings of ACL}, pages 4996--5001.\n\n\\bibitem[\\protect\\citename{Raghu et~al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In {\\em Proceedings of NeurIPS}, pages 6076--6085.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020mdl}\nElena Voita and Ivan Titov. 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proceedings of EMNLP}, pages 183--196.\n\n\\bibitem[\\protect\\citename{Wu and Dredze}2019]{wu2019beto}\nShijie Wu and Mark Dredze. 2019.\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proceedings of EMNLP}, pages 833--844.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025}\nShuyue Xiao, Zhiwei Zhang, and Linyi Yang. 2025.\n\\newblock Cross-lingual knowledge boundary probing in large language models.\n\\newblock In {\\em Proceedings of ACL}, pages 1204--1218.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019}\nHan Zhao, Remi Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proceedings of ICML}, pages 7523--7532.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2024]{zhou2024lace}\nKaitlyn Zhou, Dan Jurafsky, and Tatsunori Hashimoto. 2024.\n\\newblock {LACE}: Language-aware cross-lingual calibration.\n\\newblock In {\\em Proceedings of EMNLP}, pages 2891--2906.\n\n\\end{thebibliography}\n\n% ============================================================\n\\appendix\n\\section{Supplementary Results}\n\n\\subsection{Probe Complexity (Table S1)}\n\nTable~\\ref{tab:probe_complexity_supp} compares logistic regression and MLP probes.\nMLP achieves higher English AUROC but larger transfer gap at all layers, with the gap widening at deeper layers (6.5pp at deep vs.\\ 2.0pp at shallow).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{EN AUROC}} & \\multicolumn{2}{c}{\\textbf{Transfer Gap}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Model} & LogReg & MLP & LogReg & MLP \\\\\n\\midrule\nQwen3 & 0.800 & 0.825 & 13.1\\% & 18.5\\% \\\\\nLlama4 & 0.780 & 0.800 & 14.2\\% & 19.5\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\small LogReg better transfer: 82\\% of langs} \\\\\n\\multicolumn{5}{l}{\\small LogReg ECE: 0.135; MLP ECE: 0.148} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Probe complexity comparison. MLP gains English AUROC at the cost of larger transfer gap.}\n\\label{tab:probe_complexity_supp}\n\\end{table}\n\n\\subsection{Cross-Benchmark Generalization (Table S2)}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{EN} & \\textbf{ZS} & $\\rho$ & \\textbf{LP $\\Delta$} & $\\beta$ $\\Delta$ \\\\\n\\midrule\nGlobalMMLU & 0.80 & 0.669 & $-0.50$ & +.035 & +.002 \\\\\nBelebele & 0.77 & 0.650 & $-0.45$ & +.030 & +.002 \\\\\nMMLU-ProX & 0.81 & 0.670 & $-0.48$ & +.034 & +.003 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\small Rank corr.\\ with GlobalMMLU: Belebele 0.80, MMLU-ProX 0.90} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (Qwen3). EN = EN best AUROC; ZS = zero-shot median; LP = linear projection 50 pairs. CaCLR $\\beta$ inert across all benchmarks.}\n\\label{tab:benchmark_supp}\n\\end{table}\n\n\\subsection{Quantization Validation (Table S3)}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Llama4 (W4A16)}} & \\multicolumn{2}{c}{\\textbf{Qwen3 (INT4)}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Layer} & $\\Delta$AUC & & $\\Delta$AUC & \\\\\n\\midrule\nL8 / L16 & $-0.004$ & & $-0.006$ & \\\\\nL16 / L32 & $-0.004$ & & $-0.005$ & \\\\\nL24 / L48 & $-0.005$ & & $-0.004$ & \\\\\nL32 / L64 & $-0.007$ & & $-0.005$ & \\\\\nL40 / L80 & $-0.009$ & & $-0.011$ & \\\\\n\\midrule\n\\textbf{Mean} & $-0.004$ & $r{=}.996$ & $-0.005$ & $r{=}.995$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quantization validation. All $\\Delta$AUROC within bootstrap CIs. Quantization does not distort correctness signals.}\n\\label{tab:quant_supp}\n\\end{table}\n\n\\subsection{Control Task Details (Table S4)}\n\nEnglish selectivity increases with depth on both architectures: shallow average 0.03, mid 0.15--0.18, deep 0.24--0.27.\nLow-resource languages show lower selectivity at matched depth (median 0.09 vs.\\ 0.19 for high-resource), with the worst combinations being sw at 0--50\\% depth (median selectivity 0.02) and te at 0--40\\% depth (0.02).\nAll control task AUROCs remain near chance (median 0.50, range $[0.48, 0.53]$), confirming negligible probe capacity for memorizing random labels.\n\n\\subsection{Three-Architecture Summary (Table CR1)}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{adjustbox}{max width=\\columnwidth}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{EN} & \\textbf{ZS} & $\\rho_{\\text{med}}$ & $\\rho_{\\sigma}$ & \\textbf{CKA cliff} & \\textbf{LP $\\Delta$} \\\\\n\\midrule\nQwen3-235B & MoE & .80 & .669 & $-.48$ & .05 & .15 & +.035 \\\\\nLlama4 Scout & MoE & .78 & .638 & $-.10$ & .12 & .08 & +.032 \\\\\nGemma4 31B & Dense & .79 & .670 & $-.55$ & .04 & .18 & +.033 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\caption{Three-architecture comparison. Dense model shows strongest, most uniform Pareto ($\\rho_\\sigma = 0.04$). MoE models vary: Qwen3 moderate uniform, Llama4 language-specific.}\n\\label{tab:three_arch}\n\\end{table}\n\n\\subsection{Extended 52-Language Coverage (Table CR2)}\n\nOf 52 languages tested, 32 achieve zero-shot AUROC $> 0.60$ and 25 exceed 0.65.\nWith linear projection (+3.2pp median), 35/52 (67\\%) reach viable calibration.\n8 new languages fall below 0.55 (am, my, zu, sn, rw, xh, ny, mg), reflecting minimal pretraining representation.\nThe resource-tier gradient replicates at scale ($\\rho_{\\text{median}} = -0.47$ across 52 languages).\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "2e72f5f9-61d8-4db9-85b0-7aae1f3bfb01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "f5e90016-3444-4d2c-b895-2f98abe5212d",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

### Tool call

_source line 26 · 2026-05-21T04:14:18.859Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ga1gLPAdCPss4eBGRdCdab`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5e90016-3444-4d2c-b895-2f98abe5212d",
  "isSidechain": false,
  "requestId": "req_011CbF4gs7zNyXAcoqjidpsW",
  "type": "assistant",
  "uuid": "ce99b764-6db5-49c8-bf9b-890f7e79c399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUhtJjdVvy8EXndpmYDb16",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16046,
      "cache_read_input_tokens": 50855,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16046,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 50855,
          "cache_creation_input_tokens": 16046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16046
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

_source line 27 · 2026-05-21T04:14:19.013Z_

<details><summary>↩ Tool result · `toolu_01Ga1gLPAdCPss4eBGRdCdab`</summary>

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
  "parentUuid": "ce99b764-6db5-49c8-bf9b-890f7e79c399",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "6179fcf6-a2bf-4fca-b419-b0a8d87896c4",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ce99b764-6db5-49c8-bf9b-890f7e79c399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T04:14:23.902Z_

<details><summary>Logged reasoning block</summary>

```text
The acl.sty is not available. Let me switch to a standard article class with appropriate formatting, or find what style files are available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6179fcf6-a2bf-4fca-b419-b0a8d87896c4",
  "isSidechain": false,
  "requestId": "req_011CbF4hA2UvcLKCVXMc16yq",
  "type": "assistant",
  "uuid": "df804e40-30d4-4db2-893c-937dd91db8d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7MCbnz38f2CDntYxiKJvJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 66901,
      "output_tokens": 497,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 497,
          "cache_read_input_tokens": 66901,
          "cache_creation_input_tokens": 421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 421
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

_source line 29 · 2026-05-21T04:14:24.440Z_

ACL style not available. Switching to standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df804e40-30d4-4db2-893c-937dd91db8d6",
  "isSidechain": false,
  "requestId": "req_011CbF4hA2UvcLKCVXMc16yq",
  "type": "assistant",
  "uuid": "b2a193a4-0c57-4bf9-acd7-d391e5e0f58d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7MCbnz38f2CDntYxiKJvJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 66901,
      "output_tokens": 497,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 497,
          "cache_read_input_tokens": 66901,
          "cache_creation_input_tokens": 421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 421
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

_source line 30 · 2026-05-21T04:14:28.418Z_

<details open><summary>🔧 Tool call — Edit · `toolu_013cfZ7kjWMox49zC9PB8oB6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{adjustbox}\n\\usepackage{subcaption}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{adjustbox}\n\\usepackage{subcaption}\n\\usepackage{natbib}\n\\usepackage{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2a193a4-0c57-4bf9-acd7-d391e5e0f58d",
  "isSidechain": false,
  "requestId": "req_011CbF4hA2UvcLKCVXMc16yq",
  "type": "assistant",
  "uuid": "ab32c758-f7b2-4d23-92b1-4fd4157268f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7MCbnz38f2CDntYxiKJvJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 66901,
      "output_tokens": 497,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 497,
          "cache_read_input_tokens": 66901,
          "cache_creation_input_tokens": 421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 421
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

_source line 31 · 2026-05-21T04:14:28.444Z_

<details><summary>↩ Tool result · `toolu_013cfZ7kjWMox49zC9PB8oB6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab32c758-f7b2-4d23-92b1-4fd4157268f2",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "9a1fbc45-b830-40bd-ab58-0a29fe66a8ac",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{adjustbox}\n\\usepackage{subcaption}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{adjustbox}\n\\usepackage{subcaption}\n\\usepackage{natbib}\n\\usepackage{hyperref}",
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
          " \\usepackage{graphicx}"
        ]
      },
      {
        "oldStart": 12,
        "oldLines": 6,
        "newStart": 12,
        "newLines": 8,
        "lines": [
          " \\usepackage{array}",
          " \\usepackage{adjustbox}",
          " \\usepackage{subcaption}",
          "+\\usepackage{natbib}",
          "+\\usepackage{hyperref}",
          " ",
          " \\definecolor{lightgreen}{rgb}{0.85,0.95,0.85}",
          " \\definecolor{lightyellow}{rgb}{1.0,1.0,0.85}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ab32c758-f7b2-4d23-92b1-4fd4157268f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-21T04:14:28.525Z_

```json
{
  "parentUuid": "9a1fbc45-b830-40bd-ab58-0a29fe66a8ac",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "57189fae-4cd7-4438-b0d7-53e7e80710ea",
  "timestamp": "2026-05-21T04:14:28.525Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-21T04:14:32.467Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BWViomZ4qprT8UXmYmCsPy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57189fae-4cd7-4438-b0d7-53e7e80710ea",
  "isSidechain": false,
  "requestId": "req_011CbF4hrhiMNj39kRD7yswP",
  "type": "assistant",
  "uuid": "9371e8a3-1886-4374-a5a4-496d9521800e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GUomGseLv4Do3kURWFpxu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 67322,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 688,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 67322,
          "cache_creation_input_tokens": 688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 688
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

_source line 34 · 2026-05-21T04:14:32.485Z_

<details><summary>↩ Tool result · `toolu_01BWViomZ4qprT8UXmYmCsPy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9371e8a3-1886-4374-a5a4-496d9521800e",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "466e800a-e34f-4f74-b045-3dfb5fa4e78a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 596,
        "oldLines": 7,
        "newStart": 596,
        "newLines": 7,
        "lines": [
          " ",
          " % ============================================================",
          " % References",
          "-\\bibliographystyle{acl_natbib}",
          "+\\bibliographystyle{plainnat}",
          " ",
          " \\begin{thebibliography}{30}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9371e8a3-1886-4374-a5a4-496d9521800e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T04:14:38.489Z_

Now also fix the `\citename` commands which are ACL-specific — replace them with standard natbib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "466e800a-e34f-4f74-b045-3dfb5fa4e78a",
  "isSidechain": false,
  "requestId": "req_011CbF4i9p7ZFRvu7U15av8S",
  "type": "assistant",
  "uuid": "ee88420a-ddc3-4b98-8c66-371ae209ef3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mtxu1RYkkCQVkuL59121i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 245,
      "cache_read_input_tokens": 68010,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 68010,
          "cache_creation_input_tokens": 245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 245
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

_source line 36 · 2026-05-21T04:14:38.937Z_

<details open><summary>🔧 Tool call — Edit · `toolu_016VByWQD8iad9DJDwFzgBRS`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Angelopoulos and Bates}",
  "new_string": "Angelopoulos and Bates,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee88420a-ddc3-4b98-8c66-371ae209ef3c",
  "isSidechain": false,
  "requestId": "req_011CbF4i9p7ZFRvu7U15av8S",
  "type": "assistant",
  "uuid": "ee20a206-ecd5-411a-9c09-e056c2e4f84f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mtxu1RYkkCQVkuL59121i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 245,
      "cache_read_input_tokens": 68010,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 68010,
          "cache_creation_input_tokens": 245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 245
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

_source line 37 · 2026-05-21T04:14:38.954Z_

<details><summary>↩ Tool result · `toolu_016VByWQD8iad9DJDwFzgBRS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee20a206-ecd5-411a-9c09-e056c2e4f84f",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "a11d672b-1e95-43b9-b19f-36c7d37366dd",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Angelopoulos and Bates}",
    "newString": "Angelopoulos and Bates,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 600,
        "oldLines": 7,
        "newStart": 600,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{thebibliography}{30}",
          " ",
          "-\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}",
          "+\\bibitem[Angelopoulos and Bates,2023]{angelopoulos2023conformal}",
          " Anastasios Angelopoulos and Stephen Bates. 2023.",
          " \\newblock Conformal prediction: A gentle introduction.",
          " \\newblock {\\em Foundations and Trends in Machine Learning}, 16(4):494--591."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "ee20a206-ecd5-411a-9c09-e056c2e4f84f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T04:14:47.049Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0113JY9CNi4yskr7pReL7PWD`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Artetxe et~al.}",
  "new_string": "Artetxe et~al.,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a11d672b-1e95-43b9-b19f-36c7d37366dd",
  "isSidechain": false,
  "requestId": "req_011CbF4idfvGJgbSfPsGn7bA",
  "type": "assistant",
  "uuid": "da764d6d-bce0-4100-9c92-4a0dec08abab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RYFJ9gZpqJf6HCUkefBB2V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 68255,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 68255,
          "cache_creation_input_tokens": 283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 283
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

_source line 39 · 2026-05-21T04:14:47.060Z_

<details><summary>↩ Tool result · `toolu_0113JY9CNi4yskr7pReL7PWD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da764d6d-bce0-4100-9c92-4a0dec08abab",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "45f673d6-bf9c-4df8-898a-522e29d030f5",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Artetxe et~al.}",
    "newString": "Artetxe et~al.,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 605,
        "oldLines": 7,
        "newStart": 605,
        "newLines": 7,
        "lines": [
          " \\newblock Conformal prediction: A gentle introduction.",
          " \\newblock {\\em Foundations and Trends in Machine Learning}, 16(4):494--591.",
          " ",
          "-\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018vecmap}",
          "+\\bibitem[Artetxe et~al.,2018]{artetxe2018vecmap}",
          " Mikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.",
          " \\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.",
          " \\newblock In {\\em Proceedings of ACL}, pages 789--798."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "da764d6d-bce0-4100-9c92-4a0dec08abab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T04:14:50.313Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FfUim8zwCpyL3FTRdXPhoW`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Ben-David et~al.}",
  "new_string": "Ben-David et~al.,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45f673d6-bf9c-4df8-898a-522e29d030f5",
  "isSidechain": false,
  "requestId": "req_011CbF4jEfbGFBDiny7E5A9p",
  "type": "assistant",
  "uuid": "31c80ac3-d0cf-4bae-b882-c450b9063acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LuTnmubqcrf78ZGM9A9fBk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 68538,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 68538,
          "cache_creation_input_tokens": 256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 256
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

_source line 41 · 2026-05-21T04:14:50.328Z_

<details><summary>↩ Tool result · `toolu_01FfUim8zwCpyL3FTRdXPhoW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31c80ac3-d0cf-4bae-b882-c450b9063acd",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "8d800c3d-589b-4f28-a2b8-d126148bd9cd",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Ben-David et~al.}",
    "newString": "Ben-David et~al.,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 610,
        "oldLines": 7,
        "newStart": 610,
        "newLines": 7,
        "lines": [
          " \\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.",
          " \\newblock In {\\em Proceedings of ACL}, pages 789--798.",
          " ",
          "-\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010}",
          "+\\bibitem[Ben-David et~al.,2010]{bendavid2010}",
          " Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.",
          " \\newblock A theory of learning from different domains.",
          " \\newblock {\\em Machine Learning}, 79(1):151--175."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "31c80ac3-d0cf-4bae-b882-c450b9063acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T04:15:00.042Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01HxTvsc2rN6rFGGX3ebE4e5`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Conneau et~al.}",
  "new_string": "Conneau et~al.,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d800c3d-589b-4f28-a2b8-d126148bd9cd",
  "isSidechain": false,
  "requestId": "req_011CbF4jUASpYXnvSdAktHV3",
  "type": "assistant",
  "uuid": "acb7c8bc-9694-4d06-8492-2823032f5dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNeGJ76FuvENgopkkYjKu4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 68794,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 68794,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 252
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

_source line 43 · 2026-05-21T04:15:00.090Z_

<details><summary>↩ Tool result · `toolu_01HxTvsc2rN6rFGGX3ebE4e5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acb7c8bc-9694-4d06-8492-2823032f5dcf",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "6b44c58c-01fd-43c2-a14b-4bf25d5248c2",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Conneau et~al.}",
    "newString": "Conneau et~al.,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 615,
        "oldLines": 7,
        "newStart": 615,
        "newLines": 7,
        "lines": [
          " \\newblock A theory of learning from different domains.",
          " \\newblock {\\em Machine Learning}, 79(1):151--175.",
          " ",
          "-\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018muse}",
          "+\\bibitem[Conneau et~al.,2018]{conneau2018muse}",
          " Alexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.",
          " \\newblock Word translation without parallel data.",
          " \\newblock In {\\em Proceedings of ICLR}."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "acb7c8bc-9694-4d06-8492-2823032f5dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T04:15:04.379Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01W7KTpZRz4SQR9Lt4TPvEXq`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Hewitt and Liang}",
  "new_string": "Hewitt and Liang,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b44c58c-01fd-43c2-a14b-4bf25d5248c2",
  "isSidechain": false,
  "requestId": "req_011CbF4kC4r6fXBBumEAFVUz",
  "type": "assistant",
  "uuid": "cee37b1d-880a-4c19-a1dd-ebbb342279c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMNi1uG2ZEigpRvvZb8nB4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 69046,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 69046,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 252
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

_source line 45 · 2026-05-21T04:15:04.393Z_

<details><summary>↩ Tool result · `toolu_01W7KTpZRz4SQR9Lt4TPvEXq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cee37b1d-880a-4c19-a1dd-ebbb342279c0",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "3356120b-342f-4248-8e51-be680a229080",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Hewitt and Liang}",
    "newString": "Hewitt and Liang,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 620,
        "oldLines": 7,
        "newStart": 620,
        "newLines": 7,
        "lines": [
          " \\newblock Word translation without parallel data.",
          " \\newblock In {\\em Proceedings of ICLR}.",
          " ",
          "-\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019control}",
          "+\\bibitem[Hewitt and Liang,2019]{hewitt2019control}",
          " John Hewitt and Percy Liang. 2019.",
          " \\newblock Designing and interpreting probes with control tasks.",
          " \\newblock In {\\em Proceedings of EMNLP}, pages 2733--2743."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "cee37b1d-880a-4c19-a1dd-ebbb342279c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "3356120b-342f-4248-8e51-be680a229080",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

### Tool call

_source line 48 · 2026-05-21T04:15:10.443Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01PFy28yfJHGL8ZAJHYvAeKc`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Kornblith et~al.}",
  "new_string": "Kornblith et~al.,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3356120b-342f-4248-8e51-be680a229080",
  "isSidechain": false,
  "requestId": "req_011CbF4kWHE4fhxhHo2qEH6R",
  "type": "assistant",
  "uuid": "23409e1d-d43d-4e88-9507-9e43f3135f09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MK6NXr7MpWNqrHyyRCTAJX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 69298,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 69298,
          "cache_creation_input_tokens": 253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 253
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

_source line 49 · 2026-05-21T04:15:10.453Z_

<details><summary>↩ Tool result · `toolu_01PFy28yfJHGL8ZAJHYvAeKc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23409e1d-d43d-4e88-9507-9e43f3135f09",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "23584447-8839-4996-be5d-187f8034807b",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Kornblith et~al.}",
    "newString": "Kornblith et~al.,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 625,
        "oldLines": 7,
        "newStart": 625,
        "newLines": 7,
        "lines": [
          " \\newblock Designing and interpreting probes with control tasks.",
          " \\newblock In {\\em Proceedings of EMNLP}, pages 2733--2743.",
          " ",
          "-\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019cka}",
          "+\\bibitem[Kornblith et~al.,2019]{kornblith2019cka}",
          " Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.",
          " \\newblock Similarity of neural network representations revisited.",
          " \\newblock In {\\em Proceedings of ICML}, pages 3519--3529."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "23409e1d-d43d-4e88-9507-9e43f3135f09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T04:15:16.134Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01HcrrteWtomjyaycWYKY7pc`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Miao et~al.}2026a",
  "new_string": "Miao et~al., 2026a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23584447-8839-4996-be5d-187f8034807b",
  "isSidechain": false,
  "requestId": "req_011CbF4kxnv1LwKiJGcsaym6",
  "type": "assistant",
  "uuid": "a0edbc24-3b41-4cdf-b0d0-bede7a03151a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xuJ7U7zEFKmGN7LvqPqMH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 254,
      "cache_read_input_tokens": 69551,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 69551,
          "cache_creation_input_tokens": 254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 254
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

_source line 51 · 2026-05-21T04:15:16.147Z_

<details><summary>↩ Tool result · `toolu_01HcrrteWtomjyaycWYKY7pc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0edbc24-3b41-4cdf-b0d0-bede7a03151a",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "d9f26a5c-daa0-46ce-aa06-88c9327bd4b7",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Miao et~al.}2026a",
    "newString": "Miao et~al., 2026a",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 630,
        "oldLines": 7,
        "newStart": 630,
        "newLines": 7,
        "lines": [
          " \\newblock Similarity of neural network representations revisited.",
          " \\newblock In {\\em Proceedings of ICML}, pages 3519--3529.",
          " ",
          "-\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}",
          "+\\bibitem[Miao et~al., 2026a]{miao2026coral}",
          " Qingyi Miao, Mingxuan Ju, and Lyle Ungar. 2026a.",
          " \\newblock {CORAL}: Cross-task correctness probes for LLM calibration.",
          " \\newblock In {\\em Proceedings of NAACL}."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "a0edbc24-3b41-4cdf-b0d0-bede7a03151a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-21T04:15:19.501Z_

<details open><summary>🔧 Tool call — Edit · `toolu_014AXXBrM19zwiNPUfkBydNN`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Miao and Ungar}",
  "new_string": "Miao and Ungar,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9f26a5c-daa0-46ce-aa06-88c9327bd4b7",
  "isSidechain": false,
  "requestId": "req_011CbF4mNr2GCQqcj6wzWgbs",
  "type": "assistant",
  "uuid": "55e0fddd-de44-4b91-b18e-e90942138687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ae4EmTzLtKeQLxQsDSGuLz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 260,
      "cache_read_input_tokens": 69805,
      "output_tokens": 178,
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
          "output_tokens": 178,
          "cache_read_input_tokens": 69805,
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

_source line 53 · 2026-05-21T04:15:19.513Z_

<details><summary>↩ Tool result · `toolu_014AXXBrM19zwiNPUfkBydNN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55e0fddd-de44-4b91-b18e-e90942138687",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "c720b6c8-8e33-4bb6-ae55-6dbd51f23e12",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Miao and Ungar}",
    "newString": "Miao and Ungar,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 635,
        "oldLines": 7,
        "newStart": 635,
        "newLines": 7,
        "lines": [
          " \\newblock {CORAL}: Cross-task correctness probes for LLM calibration.",
          " \\newblock In {\\em Proceedings of NAACL}.",
          " ",
          "-\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026steering}",
          "+\\bibitem[Miao and Ungar,2026]{miao2026steering}",
          " Qingyi Miao and Lyle Ungar. 2026.",
          " \\newblock Steering LLM confidence via orthogonal correctness directions.",
          " \\newblock In {\\em Proceedings of ACL}."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "55e0fddd-de44-4b91-b18e-e90942138687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54 · 2026-05-21T04:15:19.565Z_

```json
{
  "parentUuid": "c720b6c8-8e33-4bb6-ae55-6dbd51f23e12",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fcb75921-feba-4d14-8047-19ef51a80508",
  "timestamp": "2026-05-21T04:15:19.565Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 55 · 2026-05-21T04:15:23.447Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01YXwTrNk5fDBRfrAXAKDY34`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Pires et~al.}",
  "new_string": "Pires et~al.,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcb75921-feba-4d14-8047-19ef51a80508",
  "isSidechain": false,
  "requestId": "req_011CbF4mcvr9ximmHciJULrt",
  "type": "assistant",
  "uuid": "cd8004a8-e386-4ea3-8d52-c07af2c56e60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZ3umCEudW2ky4oETSD34d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 357,
      "cache_read_input_tokens": 70065,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 357,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 70065,
          "cache_creation_input_tokens": 357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 357
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

_source line 56 · 2026-05-21T04:15:23.458Z_

<details><summary>↩ Tool result · `toolu_01YXwTrNk5fDBRfrAXAKDY34`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd8004a8-e386-4ea3-8d52-c07af2c56e60",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "80082cd6-6b61-4e35-abd1-6091b0ada987",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Pires et~al.}",
    "newString": "Pires et~al.,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 640,
        "oldLines": 7,
        "newStart": 640,
        "newLines": 7,
        "lines": [
          " \\newblock Steering LLM confidence via orthogonal correctness directions.",
          " \\newblock In {\\em Proceedings of ACL}.",
          " ",
          "-\\bibitem[\\protect\\citename{Pires et~al.}2019]{pires2019multilingual}",
          "+\\bibitem[Pires et~al.,2019]{pires2019multilingual}",
          " Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.",
          " \\newblock How multilingual is multilingual {BERT}?",
          " \\newblock In {\\em Proceedings of ACL}, pages 4996--5001."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "cd8004a8-e386-4ea3-8d52-c07af2c56e60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T04:15:26.782Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01GpJo7Zz5FYpaPvPWEiJFmL`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Raghu et~al.}",
  "new_string": "Raghu et~al.,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80082cd6-6b61-4e35-abd1-6091b0ada987",
  "isSidechain": false,
  "requestId": "req_011CbF4mujdyfv6f6uGgQZg6",
  "type": "assistant",
  "uuid": "6240d8c7-c8e4-4e12-8328-976db398dca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TuStZMz8Fjc4C263jyEAr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 70422,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 70422,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 252
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

_source line 58 · 2026-05-21T04:15:26.793Z_

<details><summary>↩ Tool result · `toolu_01GpJo7Zz5FYpaPvPWEiJFmL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6240d8c7-c8e4-4e12-8328-976db398dca8",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "3f81cf0e-0b18-451e-9c8c-fed71e0ae97b",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Raghu et~al.}",
    "newString": "Raghu et~al.,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 645,
        "oldLines": 7,
        "newStart": 645,
        "newLines": 7,
        "lines": [
          " \\newblock How multilingual is multilingual {BERT}?",
          " \\newblock In {\\em Proceedings of ACL}, pages 4996--5001.",
          " ",
          "-\\bibitem[\\protect\\citename{Raghu et~al.}2017]{raghu2017svcca}",
          "+\\bibitem[Raghu et~al.,2017]{raghu2017svcca}",
          " Maithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.",
          " \\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.",
          " \\newblock In {\\em Proceedings of NeurIPS}, pages 6076--6085."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "6240d8c7-c8e4-4e12-8328-976db398dca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T04:15:31.358Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BsiQDshWGPi6GsoBfRAGJn`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Voita and Titov}",
  "new_string": "Voita and Titov,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f81cf0e-0b18-451e-9c8c-fed71e0ae97b",
  "isSidechain": false,
  "requestId": "req_011CbF4nA1sbt7b4eBuCnLQa",
  "type": "assistant",
  "uuid": "67e287aa-85b9-4d14-a0cc-90603929ca2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMGQjwHi2HhfhcqkpyiKPU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 70674,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 70674,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 252
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

_source line 60 · 2026-05-21T04:15:31.378Z_

<details><summary>↩ Tool result · `toolu_01BsiQDshWGPi6GsoBfRAGJn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67e287aa-85b9-4d14-a0cc-90603929ca2b",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "d625597e-562b-454b-9c5c-bf69a240826f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Voita and Titov}",
    "newString": "Voita and Titov,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 650,
        "oldLines": 7,
        "newStart": 650,
        "newLines": 7,
        "lines": [
          " \\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.",
          " \\newblock In {\\em Proceedings of NeurIPS}, pages 6076--6085.",
          " ",
          "-\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020mdl}",
          "+\\bibitem[Voita and Titov,2020]{voita2020mdl}",
          " Elena Voita and Ivan Titov. 2020.",
          " \\newblock Information-theoretic probing with minimum description length.",
          " \\newblock In {\\em Proceedings of EMNLP}, pages 183--196."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "67e287aa-85b9-4d14-a0cc-90603929ca2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T04:15:34.557Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01XzYc7C8Dt45WsZzEk8dQUg`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Wu and Dredze}",
  "new_string": "Wu and Dredze,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d625597e-562b-454b-9c5c-bf69a240826f",
  "isSidechain": false,
  "requestId": "req_011CbF4nVcbHHwkbdtAniZao",
  "type": "assistant",
  "uuid": "e26f9941-052f-4bc6-ba89-02cf39866cb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFPvJBkXBQtXvwSzHZrYgk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 70926,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 70926,
          "cache_creation_input_tokens": 253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 253
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

_source line 62 · 2026-05-21T04:15:34.568Z_

<details><summary>↩ Tool result · `toolu_01XzYc7C8Dt45WsZzEk8dQUg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e26f9941-052f-4bc6-ba89-02cf39866cb6",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "3ec611a9-0613-43ba-86a8-58e48b3fcf23",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Wu and Dredze}",
    "newString": "Wu and Dredze,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 655,
        "oldLines": 7,
        "newStart": 655,
        "newLines": 7,
        "lines": [
          " \\newblock Information-theoretic probing with minimum description length.",
          " \\newblock In {\\em Proceedings of EMNLP}, pages 183--196.",
          " ",
          "-\\bibitem[\\protect\\citename{Wu and Dredze}2019]{wu2019beto}",
          "+\\bibitem[Wu and Dredze,2019]{wu2019beto}",
          " Shijie Wu and Mark Dredze. 2019.",
          " \\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.",
          " \\newblock In {\\em Proceedings of EMNLP}, pages 833--844."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "e26f9941-052f-4bc6-ba89-02cf39866cb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T04:15:37.873Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WL3GkLpPmASYPV1khkAsko`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Xiao et~al.}",
  "new_string": "Xiao et~al.,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ec611a9-0613-43ba-86a8-58e48b3fcf23",
  "isSidechain": false,
  "requestId": "req_011CbF4njG8VPxD8gBv3wHwJ",
  "type": "assistant",
  "uuid": "cd5188de-b500-4232-b9b0-cfe9d8a68eea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8vHAmz3aTv8A2DP9VRUbZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 71179,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 71179,
          "cache_creation_input_tokens": 251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 251
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

_source line 64 · 2026-05-21T04:15:37.883Z_

<details><summary>↩ Tool result · `toolu_01WL3GkLpPmASYPV1khkAsko`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd5188de-b500-4232-b9b0-cfe9d8a68eea",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "37804a21-3439-409d-8e2d-9835ca048d7f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Xiao et~al.}",
    "newString": "Xiao et~al.,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 660,
        "oldLines": 7,
        "newStart": 660,
        "newLines": 7,
        "lines": [
          " \\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.",
          " \\newblock In {\\em Proceedings of EMNLP}, pages 833--844.",
          " ",
          "-\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025}",
          "+\\bibitem[Xiao et~al.,2025]{xiao2025}",
          " Shuyue Xiao, Zhiwei Zhang, and Linyi Yang. 2025.",
          " \\newblock Cross-lingual knowledge boundary probing in large language models.",
          " \\newblock In {\\em Proceedings of ACL}, pages 1204--1218."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "cd5188de-b500-4232-b9b0-cfe9d8a68eea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T04:15:41.812Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ep5Dg12RxWVPHikq9iNJre`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Zhao et~al.}",
  "new_string": "Zhao et~al.,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37804a21-3439-409d-8e2d-9835ca048d7f",
  "isSidechain": false,
  "requestId": "req_011CbF4nyW8ZJyGcCiogGB2y",
  "type": "assistant",
  "uuid": "94435112-8880-409d-98ef-4724217c12d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2KkoMqfa6AzFJZEq91Dwe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 71430,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 71430,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 252
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

_source line 66 · 2026-05-21T04:15:41.828Z_

<details><summary>↩ Tool result · `toolu_01Ep5Dg12RxWVPHikq9iNJre`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94435112-8880-409d-98ef-4724217c12d0",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "4e6ea3c2-9196-44ab-9486-616cb7773098",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Zhao et~al.}",
    "newString": "Zhao et~al.,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 665,
        "oldLines": 7,
        "newStart": 665,
        "newLines": 7,
        "lines": [
          " \\newblock Cross-lingual knowledge boundary probing in large language models.",
          " \\newblock In {\\em Proceedings of ACL}, pages 1204--1218.",
          " ",
          "-\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019}",
          "+\\bibitem[Zhao et~al.,2019]{zhao2019}",
          " Han Zhao, Remi Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019.",
          " \\newblock On learning invariant representations for domain adaptation.",
          " \\newblock In {\\em Proceedings of ICML}, pages 7523--7532."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "94435112-8880-409d-98ef-4724217c12d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-21T04:15:45.044Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01PcQyumMXjpCFhGb13hAt5s`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
  "old_string": "\\protect\\citename{Zhou et~al.}",
  "new_string": "Zhou et~al.,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e6ea3c2-9196-44ab-9486-616cb7773098",
  "isSidechain": false,
  "requestId": "req_011CbF4oGLQujwbZ2Pwv2XKk",
  "type": "assistant",
  "uuid": "416c3da2-c6ee-4ae1-99d8-3c795ffc7331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1UjszbERkajF225Top6vz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 250,
      "cache_read_input_tokens": 71682,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 71682,
          "cache_creation_input_tokens": 250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 250
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

_source line 68 · 2026-05-21T04:15:45.059Z_

<details><summary>↩ Tool result · `toolu_01PcQyumMXjpCFhGb13hAt5s`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "416c3da2-c6ee-4ae1-99d8-3c795ffc7331",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "b023de7d-ea51-4c14-870a-de2c6772ea4d",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.tex",
    "oldString": "\\protect\\citename{Zhou et~al.}",
    "newString": "Zhou et~al.,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 670,
        "oldLines": 7,
        "newStart": 670,
        "newLines": 7,
        "lines": [
          " \\newblock On learning invariant representations for domain adaptation.",
          " \\newblock In {\\em Proceedings of ICML}, pages 7523--7532.",
          " ",
          "-\\bibitem[\\protect\\citename{Zhou et~al.}2024]{zhou2024lace}",
          "+\\bibitem[Zhou et~al.,2024]{zhou2024lace}",
          " Kaitlyn Zhou, Dan Jurafsky, and Tatsunori Hashimoto. 2024.",
          " \\newblock {LACE}: Language-aware cross-lingual calibration.",
          " \\newblock In {\\em Proceedings of EMNLP}, pages 2891--2906."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "416c3da2-c6ee-4ae1-99d8-3c795ffc7331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 69_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "b023de7d-ea51-4c14-870a-de2c6772ea4d",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

### Assistant

_source line 71 · 2026-05-21T04:15:47.995Z_

Now compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b023de7d-ea51-4c14-870a-de2c6772ea4d",
  "isSidechain": false,
  "requestId": "req_011CbF4oWRjgFnMV6CnP9FGW",
  "type": "assistant",
  "uuid": "fb992b41-4284-4a20-8d04-6cae0e09fc5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4yPsCq3rR6DM6bY1zscbw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 71932,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 248,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 71932,
          "cache_creation_input_tokens": 248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 248
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

_source line 72 · 2026-05-21T04:15:49.128Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NZiMwzCZ8TcYjYKddWmNjB`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb992b41-4284-4a20-8d04-6cae0e09fc5b",
  "isSidechain": false,
  "requestId": "req_011CbF4oWRjgFnMV6CnP9FGW",
  "type": "assistant",
  "uuid": "70828f5e-2f65-4544-a3af-273cfe6acbd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4yPsCq3rR6DM6bY1zscbw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 71932,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 248,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 71932,
          "cache_creation_input_tokens": 248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 248
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

_source line 73 · 2026-05-21T04:15:49.866Z_

<details><summary>↩ Tool result · `toolu_01NZiMwzCZ8TcYjYKddWmNjB`</summary>

```text
 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.
pfb>
Output written on paper.pdf (12 pages, 208734 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70828f5e-2f65-4544-a3af-273cfe6acbd2",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "2e24d60b-a5d9-47ce-a8cf-61bbe7f3f403",
  "toolUseResult": {
    "stdout": " )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.\npfb>\nOutput written on paper.pdf (12 pages, 208734 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "70828f5e-2f65-4544-a3af-273cfe6acbd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-21T04:16:07.235Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ezw4B1fJZmhxbXB342HC4M`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e24d60b-a5d9-47ce-a8cf-61bbe7f3f403",
  "isSidechain": false,
  "requestId": "req_011CbF4orVETXomJ3R4YFs1N",
  "type": "assistant",
  "uuid": "0b92ff1a-bdb8-4a79-8522-07d1c5ba4cf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkhpxMNGdCXYbRBYk51AFs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 72180,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 72180,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 75 · 2026-05-21T04:16:07.944Z_

<details><summary>↩ Tool result · `toolu_01Ezw4B1fJZmhxbXB342HC4M`</summary>

```text
fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.
pfb>
Output written on paper.pdf (13 pages, 212373 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b92ff1a-bdb8-4a79-8522-07d1c5ba4cf3",
  "isSidechain": false,
  "promptId": "d9d34b12-ba9b-4c4d-94dc-1e840146dcd0",
  "type": "user",
  "uuid": "75de6436-20f8-4a79-88ab-c592ba4f20a9",
  "toolUseResult": {
    "stdout": "fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.\npfb>\nOutput written on paper.pdf (13 pages, 212373 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0b92ff1a-bdb8-4a79-8522-07d1c5ba4cf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 76 · 2026-05-21T04:16:07.946Z_

```json
{
  "parentUuid": "75de6436-20f8-4a79-88ab-c592ba4f20a9",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ae199aff-3898-4861-ae80-1f91a03af42a",
  "timestamp": "2026-05-21T04:16:07.946Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 77 · 2026-05-21T04:16:15.859Z_

编译成功，生成 13 页 PDF。

`paper.pdf` 写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/paper.pdf`。

论文结构：Abstract → Introduction → Related Work → Method（4 subsections）→ Experimental Setup → Results（8 subsections，覆盖全部 10 个实验）→ Discussion → Conclusion → Appendix（6 supplementary tables）。所有定量 claim 均引用 experiment_data.json 中的数据，包含 15 个表格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae199aff-3898-4861-ae80-1f91a03af42a",
  "isSidechain": false,
  "requestId": "req_011CbF4qBmt1pq3szsPmwNTc",
  "type": "assistant",
  "uuid": "fe532f84-35f5-4435-9546-0d36a2335082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcJZ7gtb31NNZTd9dKm5Fo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 72907,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 72907,
          "cache_creation_input_tokens": 321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 321
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

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "fe532f84-35f5-4435-9546-0d36a2335082",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "67525fd2-9679-4e46-9b3e-5dfdbacf9928"
}
```

---
