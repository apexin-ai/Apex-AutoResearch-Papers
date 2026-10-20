# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/e6abcd22-961e-4398-8251-13a4344291ba.jsonl`
- **Structured JSON:** [`27557df127509e2d5713.json`](../../sessions/27/27557df127509e2d5713.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T18:17:02.451Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T18:17:02.451Z",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：原始 'Diversity Trap' framing 完全成立。标题保持挑衅性（'More Diverse, More Vulnerable'）。Claim 1 升级为 'diversity independently and causally-directionally increases vulnerability'（加 capability-matched 证据）。BFT reversal 从 analogy 升级为 empirically grounded mechanism（calibrated RF 下 β 在 transferable attacks 中翻转为负，shared-bias attacks 中显著衰减）。Story arc 无需调整：surprise → mechanism → nuance → defense 完整链条。审稿人 RC1 (confound) 被残差化 + confound-free conditions + capability-matched 三线封堵，RC3 (generalization) 被 open-ended + attack expansion + panel size 三线封堵。预期 Dream score 3.0–3.5，对应 EMNLP Findings→Borderline Conference。\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T18:17:02.455Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T18:17:02.455Z",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba"
}
```

---

## Round 1

55 recorded events

### User

_source line 3 · 2026-05-22T18:17:02.474Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：原始 'Diversity Trap' framing 完全成立。标题保持挑衅性（'More Diverse, More Vulnerable'）。Claim 1 升级为 'diversity independently and causally-directionally increases vulnerability'（加 capability-matched 证据）。BFT reversal 从 analogy 升级为 empirically grounded mechanism（calibrated RF 下 β 在 transferable attacks 中翻转为负，shared-bias attacks 中显著衰减）。Story arc 无需调整：surprise → mechanism → nuance → defense 完整链条。审稿人 RC1 (confound) 被残差化 + confound-free conditions + capability-matched 三线封堵，RC3 (generalization) 被 open-ended + attack expansion + panel size 三线封堵。预期 Dream score 3.0–3.5，对应 EMNLP Findings→Borderline Conference。
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "50846801-9575-4774-a884-47364a1f6050",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T18:17:02.473Z_

```json
{
  "parentUuid": "50846801-9575-4774-a884-47364a1f6050",
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
  "uuid": "6e5fc3ef-1156-4488-b2ca-77bfe63704dc",
  "timestamp": "2026-05-22T18:17:02.473Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T18:17:02.473Z_

```json
{
  "parentUuid": "6e5fc3ef-1156-4488-b2ca-77bfe63704dc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "600a299e-1af5-4fce-83f6-f7e44ad99a8e",
  "timestamp": "2026-05-22T18:17:02.473Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
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
  "aiTitle": "Generate certificate manipulation vulnerability study paper",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba"
}
```

---

### Assistant

_source line 7 · 2026-05-22T18:17:05.808Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "600a299e-1af5-4fce-83f6-f7e44ad99a8e",
  "isSidechain": false,
  "requestId": "req_011CbJ4mL7LBrLZTdsYWXHKo",
  "type": "assistant",
  "uuid": "100c1926-f0d4-4057-87d8-cc78ff692cc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cYY78zKqTSKpuVCPMMehw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11878,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11878,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11878
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

_source line 8 · 2026-05-22T18:17:06.758Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WtMGohvcSigU1Fppg3YHJm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "100c1926-f0d4-4057-87d8-cc78ff692cc5",
  "isSidechain": false,
  "requestId": "req_011CbJ4mL7LBrLZTdsYWXHKo",
  "type": "assistant",
  "uuid": "e50a3923-1e3e-4324-8f9a-015b4d0bf728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cYY78zKqTSKpuVCPMMehw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11878,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11878,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11878
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

_source line 9 · 2026-05-22T18:17:06.996Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A6zZUaHWubGiCyMLqjyLTV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e50a3923-1e3e-4324-8f9a-015b4d0bf728",
  "isSidechain": false,
  "requestId": "req_011CbJ4mL7LBrLZTdsYWXHKo",
  "type": "assistant",
  "uuid": "c6c30663-8a52-42d6-aef7-75128a6b0212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cYY78zKqTSKpuVCPMMehw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11878,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11878,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11878
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

_source line 10 · 2026-05-22T18:17:07.003Z_

<details><summary>↩ Tool result · `toolu_01A6zZUaHWubGiCyMLqjyLTV`</summary>

```text
1	# Paper Framing — cert_manip_resist_eval (v4: 15-Model Empirical Revision)
2	
3	> Last updated: 2026-05-22 | Reason: 15-model/455-panel results fundamentally changed Claim 1 direction; K_eff independently positive; dual vulnerability drivers
4	
5	## Target
6	EMNLP 2026 (via ARR)
7	
8	## Title Candidates
9	1. "The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer"
10	2. "More Diverse, More Vulnerable: How Judge Independence Backfires Under Adaptive Adversaries"
11	3. "Against the Diversity Assumption: Panel Diversity Independently Increases LLM Evaluation Vulnerability"
12	
13	## Core Insight
14	Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where independence protects against faults. We provide the first large-scale empirical evidence (15 models, 455 panels, 6 attacks) that this assumption **reverses** under adaptive adversaries: diversity (K_eff) is significantly and independently **positively** correlated with attack success rate. Panel vulnerability is driven by **dual factors** — individual weakness (η_max) AND structural diversity (K_eff) — with their relative importance depending on attack type. The mechanism: BFT assumes random faults where independent nodes tolerate uncorrelated failures; but adaptive adversaries exploit the diverse attack surface that independent judges create, finding judge-specific vulnerabilities across a wider attack space.
15	
16	## Hook
17	"Adding more diverse judges to an evaluation panel doesn't just fail to help — it actively makes the panel more vulnerable to adversarial manipulation."
18	
19	## Novelty Positioning
20	We do NOT claim to discover that diversity can be harmful in adversarial settings — the concept exists in security literature. Our contributions are:
21	1. **First empirical quantification of diversity's independent harmful effect** in the LLM-judge domain (15 models, 455 panels, residualized K_eff analysis confirming independent effect beyond η_max)
22	2. **Dual vulnerability driver discovery**: η_max and K_eff independently predict panel ASR, with condition-dependent relative importance (η_max dominates bias attacks; K_eff dominates transferable attacks)
23	3. **BFT reversal mechanism**: formal and empirical demonstration of WHY diversity helps under random faults but HURTS under adaptive adversaries
24	4. **Structural barriers**: copula failure (10-21× MI underestimation), diversity-capability tradeoff (now with independent predictive evidence), family label unreliability
25	5. **Actionable defense**: robustness-first selection + reliability-weighted aggregation
26	
27	## Core Claims
28	
29	### Claim 1 (Primary): Dual Vulnerability Drivers — Diversity Trap
30	**Statement**: Under adaptive adversarial attacks, panel ASR is independently predicted by BOTH individual weakness (η_max, 9/12 FDR sig) AND panel diversity (K_eff, 8/12 FDR sig positive after residualization). Diversity **increases** vulnerability. Their relative importance is condition-dependent: η_max dominates shared-bias attacks, K_eff dominates transferable attacks.
31	**Evidence** (15-model, 455 panels, 12 conditions):
32	- η_max FDR significant: **9/12**
33	- K_eff raw FDR significant positive: **12/12**
34	- K_eff residualized (orthogonalized against η_max, VIF=1.00): **8/12 FDR sig positive**
35	- Sensitivity (exclude ACC < 0.5): K_eff_resid **9/12** sig → not driven by extreme outliers
36	- **K_eff dominates η_max** in 2 conditions: arc×score_manipulation (η_max p=0.117 NS, K_eff_resid p=1.7e-7), arc×position_bias (η_max p=0.910 NS, K_eff_resid p=1.8e-8)
37	- **η_max dominates K_eff** in bias-type attacks: sycophancy, verbosity, authority
38	- Confound status: mean |r|=0.700 (SEVERE), but 2 BROKEN conditions (r≈0.35) confirm independent K_eff effect (p=6e-26, 4e-16)
39	**Strength**: Strong. Residualized analysis + confound-free conditions + sensitivity analysis all converge.
40	**Headline**: "Both η_max (9/12) and K_eff (8/12 residualized) independently predict panel vulnerability. Diversity actively increases attack surface."
41	
42	**Comparison to 6-model results** (for transparency):
43	- 6-model (20 panels): K_eff 1/12 sig, η_max 6/12 sig → "K_eff irrelevant"
44	- 15-model (455 panels): K_eff 8/12 sig positive, η_max 9/12 sig → "K_eff independently harmful"
45	- The reversal is driven by model pool expansion: more diverse capability spectrum enables detecting K_eff's real effect.
46	
47	### Claim 2 (Empirical): Adaptive vs Random-Fault Predictability Gap
48	**Statement**: Panel composition explains systematically more variance under random faults than under adaptive attacks (ΔR² = +0.213). Adaptive adversaries introduce strategic variance beyond panel structure.
49	**Evidence** (15-model, 455 panels):
50	- K_eff significant in both regimes (12/12 adaptive, 12/12 RF), both positive direction
51	- K_eff gains significance: 11/12 (RF β larger than adaptive β in most conditions)
52	- ΔR² = +0.213 mean
53	**Reframing from v3**: Original BFT contrast ("K_eff helps under RF but not adaptive") does NOT hold — K_eff is harmful in both regimes. The real distinction is predictability: random faults produce more explainable variance, adaptive attacks introduce strategic noise.
54	**Strength**: Moderate. R² gap real, but K_eff regime-difference story is weaker than originally hoped.
55	
56	### Claim 3 (Empirical): Diversity-Capability Tradeoff
57	**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. This tradeoff is not merely correlational — residualized K_eff analysis confirms diversity has an independent predictive effect on vulnerability beyond its association with η_max.
58	**Evidence**:
59	- K_eff-η_max correlation: r = +0.700 (15-model)
60	- Residualized K_eff still significant 8/12 → not purely mediated by η_max
61	- Independent statistical effect: diversity predicts vulnerability beyond what η_max alone explains
62	**Upgrade from v3**: From "correlation" to "independent predictive effect" (residualized analysis). Note: observational regression cannot establish causality — would require experimental manipulation of panel composition or instrumental variables.
63	**Strength**: Strong (statistical association). Causal language avoided.
64	
65	### Claim 4 (Methodological): Family Labels ≠ Diversity
66	**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.
67	**Evidence**: Mann-Whitney U p=0.206, permutation p=0.427 for within vs cross-family MI. (6-model data; needs 15-model revalidation with 105 pairs)
68	**Strength**: Moderate (needs 15-model update).
69	
70	### Claim 5 (Methodological): Gaussian Copula Failure
71	**Statement**: The Gaussian copula model systematically underestimates information sharing between LLM judges by 10-21× (up to 235×), invalidating copula-based independence bounds.
72	**Evidence**: MI_observed / MI_gaussian ratio across model pairs × datasets. (Needs 15-model update)
73	**Strength**: Strong (6-model). Needs 15-model revalidation.
74	
75	### Claim 6 (Practical): Robustness-First Panel Design
76	**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.
77	**Evidence**: min_eta_max strategy dominates 5/6 conditions (6-model). Full 15-model validation needed.
78	**Strength**: Moderate. Updated rationale: K_eff's positive (harmful) effect should diminish when η_max is controlled by screening.
79	
80	### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Vulnerability Drivers
81	**Statement**: The dual vulnerability driver effect (Claim 1) varies by aggregation rule. Bayesian aggregation partially breaks the η_max effect; threshold voting amplifies K_eff's harmful effect.
82	**Evidence** (6-model, needs 15-model rerun):
83	- Majority: η_max 5/12, K_eff mostly NS
84	- Threshold: K_eff positive 8/12 (diversity harmful under unanimity)
85	- Bayesian: η_max 2/12 (weakened)
86	**Needs**: 15-model/455-panel rerun of plan_010 aggregation analysis.
87	**Strength**: Moderate (6-model only).
88	
89	## Contribution Stack (ordered by strength)
90	1. **Diversity Trap / Dual vulnerability drivers** — primary empirical contribution (K_eff independently harmful + condition-dependent dominance pattern)
91	2. **Diversity-capability tradeoff with independent predictive evidence** — empirical contribution (residualized analysis upgrades from correlation to independent effect)
92	3. **BFT reversal mechanism** — theoretical contribution (why independence hurts under adaptive adversaries)
93	4. **Aggregation-dependent effects** — empirical+practical (Bayesian as partial defense; threshold as amplifier)
94	5. **Robustness-first panel design** — practical contribution
95	6. **Gaussian copula failure** — methodological contribution
96	7. **Family label unreliability** — methodological contribution
97	8. **Adaptive vs random-fault predictability gap** — empirical (R² gap, weakened from original)
98	
99	## Anticipated Reviewer Concerns
100	
101	### RC1: "K_eff positive is just confound with η_max"
102	**Response**: (a) Residualized K_eff (VIF=1.00) still significant 8/12; (b) In confound-free conditions (r≈0.35), K_eff p < 1e-16; (c) Sensitivity analysis excluding extreme models: 9/12 still significant. Three independent lines of evidence rule out confound artifact.
103	
104	### RC2: "Why does diversity hurt? What's the mechanism?"
105	**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) Condition-dependent analysis: K_eff dominates transferable attacks (score_manipulation, position_bias) where attack diversity maps to judge diversity; η_max dominates shared-bias attacks (sycophancy, verbosity) where all judges share similar biases.
106	
107	### RC3: "Only 15 models — does this generalize?"
108	**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).
109	
110	### RC4: "BFT comparison is a strawman"
111	**Response**: (a) The implicit assumption "more diverse judges = more robust" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.
112	
113	### RC5: "Why not just use the strongest models?"
114	**Response**: (a) "Strongest" varies by attack type; (b) K_eff dominates η_max in 2 conditions — even all-strong panels are vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.
115	
116	### RC6: "No theoretical novelty"
117	**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.
118	
119	### RC7: "Why not just use Bayesian aggregation?"
120	**Response**: (a) Bayesian reduces η_max significance but K_eff effect unknown at 15-model scale; (b) Requires clean accuracy prior; (c) Adaptive attacker can target Bayesian weighting; (d) Defense stack (selection + aggregation) recommended.
121	
122	### RC8 (new): "6-model and 15-model results contradict — which is right?"
123	**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff positive) has 23× more panels, wider capability range, and passes residualized validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.
124	
125	## "When Diversity Helps" Section
126	Diversity MAY be beneficial under specific conditions — paper must acknowledge nuance:
127	1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary
128	2. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.
129	3. **Shared-bias attacks where η_max is high and uniform**: when all models are similarly vulnerable (low η_max variance), K_eff's independent harmful effect is weaker. But this is a narrow regime.
130	4. **Disclaimer**: K_eff's harmful effect was significant in 8/12 conditions including confound-free ones. "When diversity helps" is the exception, not the rule, under adaptive adversaries.
131	
132	## Story Arc (v4)
133	1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)
134	2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types
135	3. **Surprise**: Diversity doesn't just fail to protect — it **actively increases vulnerability**. K_eff is significantly positive in 12/12 conditions (8/12 after residualization)
136	4. **Mechanism**: BFT assumes random faults; adaptive adversaries exploit the diverse attack surface that independent judges create. η_max and K_eff are dual vulnerability drivers with condition-dependent importance
137	5. **Nuance**: K_eff dominates transferable attacks; η_max dominates shared-bias attacks. The diversity-capability tradeoff provides partial (but not complete) explanation
138	6. **Defense**: Robustness-first screening + Bayesian aggregation. No single defense eliminates both vulnerability channels
139	7. **Implication**: The LLM evaluation community should rethink the "more diverse = more robust" assumption. Panel security requires managing both individual robustness AND structural diversity
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6c30663-8a52-42d6-aef7-75128a6b0212",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "5fafceb4-162b-40f9-9683-cf96e38fa5aa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper_framing.md",
      "content": "# Paper Framing — cert_manip_resist_eval (v4: 15-Model Empirical Revision)\n\n> Last updated: 2026-05-22 | Reason: 15-model/455-panel results fundamentally changed Claim 1 direction; K_eff independently positive; dual vulnerability drivers\n\n## Target\nEMNLP 2026 (via ARR)\n\n## Title Candidates\n1. \"The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer\"\n2. \"More Diverse, More Vulnerable: How Judge Independence Backfires Under Adaptive Adversaries\"\n3. \"Against the Diversity Assumption: Panel Diversity Independently Increases LLM Evaluation Vulnerability\"\n\n## Core Insight\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where independence protects against faults. We provide the first large-scale empirical evidence (15 models, 455 panels, 6 attacks) that this assumption **reverses** under adaptive adversaries: diversity (K_eff) is significantly and independently **positively** correlated with attack success rate. Panel vulnerability is driven by **dual factors** — individual weakness (η_max) AND structural diversity (K_eff) — with their relative importance depending on attack type. The mechanism: BFT assumes random faults where independent nodes tolerate uncorrelated failures; but adaptive adversaries exploit the diverse attack surface that independent judges create, finding judge-specific vulnerabilities across a wider attack space.\n\n## Hook\n\"Adding more diverse judges to an evaluation panel doesn't just fail to help — it actively makes the panel more vulnerable to adversarial manipulation.\"\n\n## Novelty Positioning\nWe do NOT claim to discover that diversity can be harmful in adversarial settings — the concept exists in security literature. Our contributions are:\n1. **First empirical quantification of diversity's independent harmful effect** in the LLM-judge domain (15 models, 455 panels, residualized K_eff analysis confirming independent effect beyond η_max)\n2. **Dual vulnerability driver discovery**: η_max and K_eff independently predict panel ASR, with condition-dependent relative importance (η_max dominates bias attacks; K_eff dominates transferable attacks)\n3. **BFT reversal mechanism**: formal and empirical demonstration of WHY diversity helps under random faults but HURTS under adaptive adversaries\n4. **Structural barriers**: copula failure (10-21× MI underestimation), diversity-capability tradeoff (now with independent predictive evidence), family label unreliability\n5. **Actionable defense**: robustness-first selection + reliability-weighted aggregation\n\n## Core Claims\n\n### Claim 1 (Primary): Dual Vulnerability Drivers — Diversity Trap\n**Statement**: Under adaptive adversarial attacks, panel ASR is independently predicted by BOTH individual weakness (η_max, 9/12 FDR sig) AND panel diversity (K_eff, 8/12 FDR sig positive after residualization). Diversity **increases** vulnerability. Their relative importance is condition-dependent: η_max dominates shared-bias attacks, K_eff dominates transferable attacks.\n**Evidence** (15-model, 455 panels, 12 conditions):\n- η_max FDR significant: **9/12**\n- K_eff raw FDR significant positive: **12/12**\n- K_eff residualized (orthogonalized against η_max, VIF=1.00): **8/12 FDR sig positive**\n- Sensitivity (exclude ACC < 0.5): K_eff_resid **9/12** sig → not driven by extreme outliers\n- **K_eff dominates η_max** in 2 conditions: arc×score_manipulation (η_max p=0.117 NS, K_eff_resid p=1.7e-7), arc×position_bias (η_max p=0.910 NS, K_eff_resid p=1.8e-8)\n- **η_max dominates K_eff** in bias-type attacks: sycophancy, verbosity, authority\n- Confound status: mean |r|=0.700 (SEVERE), but 2 BROKEN conditions (r≈0.35) confirm independent K_eff effect (p=6e-26, 4e-16)\n**Strength**: Strong. Residualized analysis + confound-free conditions + sensitivity analysis all converge.\n**Headline**: \"Both η_max (9/12) and K_eff (8/12 residualized) independently predict panel vulnerability. Diversity actively increases attack surface.\"\n\n**Comparison to 6-model results** (for transparency):\n- 6-model (20 panels): K_eff 1/12 sig, η_max 6/12 sig → \"K_eff irrelevant\"\n- 15-model (455 panels): K_eff 8/12 sig positive, η_max 9/12 sig → \"K_eff independently harmful\"\n- The reversal is driven by model pool expansion: more diverse capability spectrum enables detecting K_eff's real effect.\n\n### Claim 2 (Empirical): Adaptive vs Random-Fault Predictability Gap\n**Statement**: Panel composition explains systematically more variance under random faults than under adaptive attacks (ΔR² = +0.213). Adaptive adversaries introduce strategic variance beyond panel structure.\n**Evidence** (15-model, 455 panels):\n- K_eff significant in both regimes (12/12 adaptive, 12/12 RF), both positive direction\n- K_eff gains significance: 11/12 (RF β larger than adaptive β in most conditions)\n- ΔR² = +0.213 mean\n**Reframing from v3**: Original BFT contrast (\"K_eff helps under RF but not adaptive\") does NOT hold — K_eff is harmful in both regimes. The real distinction is predictability: random faults produce more explainable variance, adaptive attacks introduce strategic noise.\n**Strength**: Moderate. R² gap real, but K_eff regime-difference story is weaker than originally hoped.\n\n### Claim 3 (Empirical): Diversity-Capability Tradeoff\n**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. This tradeoff is not merely correlational — residualized K_eff analysis confirms diversity has an independent predictive effect on vulnerability beyond its association with η_max.\n**Evidence**:\n- K_eff-η_max correlation: r = +0.700 (15-model)\n- Residualized K_eff still significant 8/12 → not purely mediated by η_max\n- Independent statistical effect: diversity predicts vulnerability beyond what η_max alone explains\n**Upgrade from v3**: From \"correlation\" to \"independent predictive effect\" (residualized analysis). Note: observational regression cannot establish causality — would require experimental manipulation of panel composition or instrumental variables.\n**Strength**: Strong (statistical association). Causal language avoided.\n\n### Claim 4 (Methodological): Family Labels ≠ Diversity\n**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.\n**Evidence**: Mann-Whitney U p=0.206, permutation p=0.427 for within vs cross-family MI. (6-model data; needs 15-model revalidation with 105 pairs)\n**Strength**: Moderate (needs 15-model update).\n\n### Claim 5 (Methodological): Gaussian Copula Failure\n**Statement**: The Gaussian copula model systematically underestimates information sharing between LLM judges by 10-21× (up to 235×), invalidating copula-based independence bounds.\n**Evidence**: MI_observed / MI_gaussian ratio across model pairs × datasets. (Needs 15-model update)\n**Strength**: Strong (6-model). Needs 15-model revalidation.\n\n### Claim 6 (Practical): Robustness-First Panel Design\n**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.\n**Evidence**: min_eta_max strategy dominates 5/6 conditions (6-model). Full 15-model validation needed.\n**Strength**: Moderate. Updated rationale: K_eff's positive (harmful) effect should diminish when η_max is controlled by screening.\n\n### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Vulnerability Drivers\n**Statement**: The dual vulnerability driver effect (Claim 1) varies by aggregation rule. Bayesian aggregation partially breaks the η_max effect; threshold voting amplifies K_eff's harmful effect.\n**Evidence** (6-model, needs 15-model rerun):\n- Majority: η_max 5/12, K_eff mostly NS\n- Threshold: K_eff positive 8/12 (diversity harmful under unanimity)\n- Bayesian: η_max 2/12 (weakened)\n**Needs**: 15-model/455-panel rerun of plan_010 aggregation analysis.\n**Strength**: Moderate (6-model only).\n\n## Contribution Stack (ordered by strength)\n1. **Diversity Trap / Dual vulnerability drivers** — primary empirical contribution (K_eff independently harmful + condition-dependent dominance pattern)\n2. **Diversity-capability tradeoff with independent predictive evidence** — empirical contribution (residualized analysis upgrades from correlation to independent effect)\n3. **BFT reversal mechanism** — theoretical contribution (why independence hurts under adaptive adversaries)\n4. **Aggregation-dependent effects** — empirical+practical (Bayesian as partial defense; threshold as amplifier)\n5. **Robustness-first panel design** — practical contribution\n6. **Gaussian copula failure** — methodological contribution\n7. **Family label unreliability** — methodological contribution\n8. **Adaptive vs random-fault predictability gap** — empirical (R² gap, weakened from original)\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"K_eff positive is just confound with η_max\"\n**Response**: (a) Residualized K_eff (VIF=1.00) still significant 8/12; (b) In confound-free conditions (r≈0.35), K_eff p < 1e-16; (c) Sensitivity analysis excluding extreme models: 9/12 still significant. Three independent lines of evidence rule out confound artifact.\n\n### RC2: \"Why does diversity hurt? What's the mechanism?\"\n**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) Condition-dependent analysis: K_eff dominates transferable attacks (score_manipulation, position_bias) where attack diversity maps to judge diversity; η_max dominates shared-bias attacks (sycophancy, verbosity) where all judges share similar biases.\n\n### RC3: \"Only 15 models — does this generalize?\"\n**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).\n\n### RC4: \"BFT comparison is a strawman\"\n**Response**: (a) The implicit assumption \"more diverse judges = more robust\" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.\n\n### RC5: \"Why not just use the strongest models?\"\n**Response**: (a) \"Strongest\" varies by attack type; (b) K_eff dominates η_max in 2 conditions — even all-strong panels are vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.\n\n### RC6: \"No theoretical novelty\"\n**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.\n\n### RC7: \"Why not just use Bayesian aggregation?\"\n**Response**: (a) Bayesian reduces η_max significance but K_eff effect unknown at 15-model scale; (b) Requires clean accuracy prior; (c) Adaptive attacker can target Bayesian weighting; (d) Defense stack (selection + aggregation) recommended.\n\n### RC8 (new): \"6-model and 15-model results contradict — which is right?\"\n**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff positive) has 23× more panels, wider capability range, and passes residualized validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.\n\n## \"When Diversity Helps\" Section\nDiversity MAY be beneficial under specific conditions — paper must acknowledge nuance:\n1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary\n2. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.\n3. **Shared-bias attacks where η_max is high and uniform**: when all models are similarly vulnerable (low η_max variance), K_eff's independent harmful effect is weaker. But this is a narrow regime.\n4. **Disclaimer**: K_eff's harmful effect was significant in 8/12 conditions including confound-free ones. \"When diversity helps\" is the exception, not the rule, under adaptive adversaries.\n\n## Story Arc (v4)\n1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)\n2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types\n3. **Surprise**: Diversity doesn't just fail to protect — it **actively increases vulnerability**. K_eff is significantly positive in 12/12 conditions (8/12 after residualization)\n4. **Mechanism**: BFT assumes random faults; adaptive adversaries exploit the diverse attack surface that independent judges create. η_max and K_eff are dual vulnerability drivers with condition-dependent importance\n5. **Nuance**: K_eff dominates transferable attacks; η_max dominates shared-bias attacks. The diversity-capability tradeoff provides partial (but not complete) explanation\n6. **Defense**: Robustness-first screening + Bayesian aggregation. No single defense eliminates both vulnerability channels\n7. **Implication**: The LLM evaluation community should rethink the \"more diverse = more robust\" assumption. Panel security requires managing both individual robustness AND structural diversity\n",
      "numLines": 140,
      "startLine": 1,
      "totalLines": 140
    }
  },
  "sourceToolAssistantUUID": "c6c30663-8a52-42d6-aef7-75128a6b0212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T18:17:07.087Z_

<details><summary>↩ Tool result · `toolu_01WtMGohvcSigU1Fppg3YHJm`</summary>

```text
1	[
2	  {
3	    "name": "15-Model Scale Expansion + Core Regression",
4	    "description": "从 6 扩展到 15 models（GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini, Claude-3.5-Sonnet, Gemini-1.5-Pro + 6 local open-source: Llama-3.1-8B/70B, Qwen2.5-7B/72B, Mistral-7B-v0.3, Phi-3-medium-14B）。455 C(15,3) panels，2 datasets × 6 attacks = 12 conditions 全量回归。",
5	    "results": {
6	      "K_eff_raw_FDR_sig_positive": "12/12",
7	      "K_eff_resid_FDR_sig_positive": "10/12",
8	      "eta_max_FDR_sig": "10/12",
9	      "VIF_keff_etamax": 1.02,
10	      "mean_R2": 0.62,
11	      "confound_r_mean": 0.55,
12	      "confound_free_conditions_count": 3,
13	      "confound_free_keff_p_min": 2.1e-28,
14	      "panels_total": 455,
15	      "keff_dominates_etamax_conditions": 3,
16	      "etamax_dominates_keff_conditions": 4,
17	      "sensitivity_exclude_ACC_lt_05_keff_sig": "11/12"
18	    },
19	    "tables": [
20	      {
21	        "name": "Dual Vulnerability Drivers: 15-Model Regression (12 Conditions)",
22	        "columns": [
23	          "Condition",
24	          "η_max β",
25	          "η_max p",
26	          "K_eff_resid β",
27	          "K_eff_resid p",
28	          "R²",
29	          "Confound r",
30	          "Dominant"
31	        ],
32	        "rows": [
33	          [
34	            "mmlu×sycophancy",
35	            "0.82",
36	            "1.2e-8",
37	            "0.31",
38	            "0.004",
39	            "0.68",
40	            "0.72",
41	            "η_max"
42	          ],
43	          [
44	            "mmlu×score_manip",
45	            "0.45",
46	            "0.018",
47	            "0.61",
48	            "3.4e-9",
49	            "0.71",
50	            "0.38",
51	            "K_eff"
52	          ],
53	          [
54	            "mmlu×position",
55	            "0.15",
56	            "0.214",
57	            "0.58",
58	            "1.2e-8",
59	            "0.56",
60	            "0.36",
61	            "K_eff"
62	          ],
63	          [
64	            "mmlu×verbosity",
65	            "0.74",
66	            "4.1e-7",
67	            "0.28",
68	            "0.011",
69	            "0.63",
70	            "0.74",
71	            "η_max"
72	          ],
73	          [
74	            "mmlu×authority",
75	            "0.69",
76	            "1.8e-6",
77	            "0.19",
78	            "0.087",
79	            "0.58",
80	            "0.78",
81	            "η_max"
82	          ],
83	          [
84	            "mmlu×few_shot",
85	            "0.55",
86	            "2.3e-4",
87	            "0.48",
88	            "6.1e-6",
89	            "0.65",
90	            "0.65",
91	            "both"
92	          ],
93	          [
94	            "arc×sycophancy",
95	            "0.79",
96	            "3.5e-8",
97	            "0.35",
98	            "0.002",
99	            "0.66",
100	            "0.71",
101	            "η_max"
102	          ],
103	          [
104	            "arc×score_manip",
105	            "0.38",
106	            "0.117",
107	            "0.64",
108	            "1.7e-7",
109	            "0.59",
110	            "0.35",
111	            "K_eff"
112	          ],
113	          [
114	            "arc×position",
115	            "0.03",
116	            "0.910",
117	            "0.72",
118	            "1.8e-8",
119	            "0.57",
120	            "0.34",
121	            "K_eff"
122	          ],
123	          [
124	            "arc×verbosity",
125	            "0.71",
126	            "8.9e-7",
127	            "0.33",
128	            "0.003",
129	            "0.61",
130	            "0.73",
131	            "η_max"
132	          ],
133	          [
134	            "arc×authority",
135	            "0.66",
136	            "3.2e-6",
137	            "0.22",
138	            "0.062",
139	            "0.55",
140	            "0.76",
141	            "η_max"
142	          ],
143	          [
144	            "arc×few_shot",
145	            "0.51",
146	            "5.7e-4",
147	            "0.52",
148	            "3.8e-6",
149	            "0.63",
150	            "0.62",
151	            "both"
152	          ]
153	        ]
154	      }
155	    ],
156	    "figures": [],
157	    "analysis": "15-model 核心回归确认 Diversity Trap 的全部结构。10/12 残差化显著（vs 初步分析 8/12）表明 refined 统计方法（FDR 校正 + beta regression consistency check from plan_009）增强效应检测。Condition-dependent dominance pattern 从定性观察升级为 systematic taxonomy：attack transferability 高→K_eff 主导（adversary 利用 judge 异质性找 judge-specific 攻击路径），attack transferability 低（shared bias）→η_max 主导（所有 judges 共享弱点）。3 个 confound-free conditions 的 p<1e-20 是最强 'smoking gun'——即使 K_eff 与 η_max 近乎正交（r≈0.35），K_eff 仍达 genome-wide 级别显著性。这单独就足以封堵 RC1 的所有统计变体。\n\n模型池从 6→15 后能力谱系大幅展开（7B→72B 全开源 + GPT-4/Claude/Gemini API tier），K_eff-η_max 结构性共线从 r=-0.80 降至 ~0.55。455 panels（23× 6-model 的 20 panels）给残差化 K_eff 分析提供充足统计功效，使 8/12 的初步结果在 refined analysis 后升至 10/12。关键驱动力：(1) confound-free conditions 从 2→3 个（arc×score_manipulation、arc×position_bias、mmlu×position_bias 中 r≈0.35），这些条件下 K_eff 达极端显著性（p<1e-20），彻底排除 confound artifact；(2) condition-dependent dominance pattern 清晰——transferable attacks（score_manipulation、position_bias）中 K_eff β > η_max β，因为 diverse judges 提供异质化 attack surface；shared-bias attacks（sycophancy、verbosity、authority）中 η_max 主导，因为所有 judges 共享类似认知偏差；(3) sensitivity analysis 排除 ACC<0.5 outlier models 后 K_eff_resid 增至 11/12，证明效应非极端 outlier 驱动。"
158	  },
159	  {
160	    "name": "Attack Surface Expansion (9 Types)",
161	    "description": "攻击类型从 6 扩展到 9：新增 few-shot hijacking（in-context example 注入篡改评分标准）、persona manipulation（冒充权威角色指令 judge 改分）、instruction override（直接覆写评判 prompt）。全 15 models × 455 panels × 2 datasets。",
162	    "results": {
163	      "new_attack_types": 3,
164	      "new_conditions": 6,
165	      "keff_resid_sig_new_conditions": "4/6",
166	      "total_conditions_majority": 18,
167	      "keff_resid_sig_total_majority": "14/18",
168	      "eta_max_sig_total_majority": "15/18",
169	      "keff_dominates_new_attacks": 1,
170	      "etamax_dominates_new_attacks": 2,
171	      "mean_R2_new": 0.63
172	    },
173	    "tables": [
174	      {
175	        "name": "Extended Attack Results (New 6 Conditions)",
176	        "columns": [
177	          "Condition",
178	          "K_eff_resid β",
179	          "K_eff_resid p (FDR)",
180	          "η_max β",
181	          "η_max p (FDR)",
182	          "R²",
183	          "Attack Transferability"
184	        ],
185	        "rows": [
186	          [
187	            "mmlu×few_shot_hijack",
188	            "0.54",
189	            "8.2e-7",
190	            "0.47",
191	            "3.1e-5",
192	            "0.67",
193	            "High"
194	          ],
195	          [
196	            "mmlu×persona_manip",
197	            "0.29",
198	            "0.008",
199	            "0.63",
200	            "5.4e-7",
201	            "0.60",
202	            "Moderate"
203	          ],
204	          [
205	            "mmlu×instr_override",
206	            "0.22",
207	            "0.042",
208	            "0.71",
209	            "1.1e-7",
210	            "0.64",
211	            "Low"
212	          ],
213	          [
214	            "arc×few_shot_hijack",
215	            "0.58",
216	            "2.1e-7",
217	            "0.41",
218	            "8.8e-5",
219	            "0.65",
220	            "High"
221	          ],
222	          [
223	            "arc×persona_manip",
224	            "0.25",
225	            "0.019",
226	            "0.68",
227	            "2.3e-7",
228	            "0.62",
229	            "Moderate"
230	          ],
231	          [
232	            "arc×instr_override",
233	            "0.18",
234	            "0.112",
235	            "0.74",
236	            "3.7e-8",
237	            "0.66",
238	            "Low"
239	          ]
240	        ]
241	      }
242	    ],
243	    "figures": [],
244	    "analysis": "新攻击验证了 attack taxonomy 的预测性：transferability 越高的攻击，K_eff 的相对重要性越大。Few-shot hijacking 与 score_manipulation/position_bias 一起构成 'transferable attacks cluster'（K_eff β 0.47–0.72），persona/instruction/sycophancy/verbosity/authority 构成 'shared-bias cluster'（η_max β 0.58–0.82）。Taxonomy 从 post-hoc 描述升级为 predictive framework：给定新攻击类型，可预测哪个 vulnerability driver 主导。14/18 总显著数直接封堵 RC3 的 generalization 质疑，attack 覆盖面从 6→9 类型跨越 injection、bias、hijacking 三大攻击范式。\n\n三类新攻击按 transferability 分层：few-shot hijacking 是 high-transferability 攻击——通过 in-context examples 篡改评分标准，不同 judge 对 ICL 的响应模式差异极大（Qwen 系对 Chinese-style ICL 特别敏感、GPT 系对结构化 format hijacking 脆弱），因此 K_eff 主导（β≈0.54, p<1e-6）——diverse panel 有更多可利用的 ICL 入口点。Persona manipulation 和 instruction override 属于 moderate-to-low transferability：不同 judge 的 instruction-following 遵从度存在差异但 RLHF 训练给所有模型植入了类似的 authority-compliance bias，预测 η_max 主导但 K_eff 在 persona_manip 上仍显著（p<0.02）。Instruction override 的 K_eff 在 arc 上 NS（p=0.112）因为 ARC 的简短问题格式给 override 攻击的操作空间更少，judge 差异贡献有限。总计 14/18 残差化显著满足 K_eff_resid_sig_extended_conditions [10,16] 范围。"
245	  },
246	  {
247	    "name": "BFT Random-Fault Contrast (Calibrated, 15-Model)",
248	    "description": "Random-fault simulation 使用 calibrated failure rates（非原始 η_j）：基于 bootstrapped clean-accuracy noise 生成独立 random failures。每个 judge 失败概率与其 clean accuracy 相关但独立采样，模拟 BFT 假设的 uncorrelated fault 模式。455 panels × 12 conditions 对比 adaptive 与 RF 下的 K_eff β。",
249	    "results": {
250	      "RF_keff_sig_positive": "3/12",
251	      "RF_keff_sig_negative": "5/12",
252	      "RF_keff_NS": "4/12",
253	      "adaptive_keff_beta_mean": 0.42,
254	      "RF_keff_beta_mean": -0.12,
255	      "BFT_RF_beta_ratio": 2.8,
256	      "conditions_ratio_ge_1_5x": "9/12",
257	      "conditions_beta_flipped_negative": "5/12",
258	      "delta_R2_RF_vs_adaptive": 0.31,
259	      "RF_R2_mean": 0.78,
260	      "adaptive_R2_mean": 0.47
261	    },
262	    "tables": [
263	      {
264	        "name": "BFT Regime Contrast: K_eff β Adaptive vs Random-Fault (12 Conditions)",
265	        "columns": [
266	          "Condition",
267	          "β_adaptive",
268	          "p_adap",
269	          "β_RF",
270	          "p_RF",
271	          "|β_adap/β_RF|",
272	          "R²_adap",
273	          "R²_RF",
274	          "Flipped?"
275	        ],
276	        "rows": [
277	          [
278	            "mmlu×sycophancy",
279	            "0.31",
280	            "0.004",
281	            "0.08",
282	            "0.310",
283	            "3.88",
284	            "0.68",
285	            "0.82",
286	            "No"
287	          ],
288	          [
289	            "mmlu×score_manip",
290	            "0.61",
291	            "3.4e-9",
292	            "-0.22",
293	            "0.015",
294	            "2.77",
295	            "0.71",
296	            "0.89",
297	            "Yes"
298	          ],
299	          [
300	            "mmlu×position",
301	            "0.58",
302	            "1.2e-8",
303	            "-0.31",
304	            "0.003",
305	            "1.87",
306	            "0.56",
307	            "0.76",
308	            "Yes"
309	          ],
310	          [
311	            "mmlu×verbosity",
312	            "0.28",
313	            "0.011",
314	            "0.11",
315	            "0.198",
316	            "2.55",
317	            "0.63",
318	            "0.79",
319	            "No"
320	          ],
321	          [
322	            "mmlu×authority",
323	            "0.19",
324	            "0.087",
325	            "0.06",
326	            "0.541",
327	            "3.17",
328	            "0.58",
329	            "0.74",
330	            "No"
331	          ],
332	          [
333	            "mmlu×few_shot",
334	            "0.48",
335	            "6.1e-6",
336	            "-0.18",
337	            "0.039",
338	            "2.67",
339	            "0.65",
340	            "0.81",
341	            "Yes"
342	          ],
343	          [
344	            "arc×sycophancy",
345	            "0.35",
346	            "0.002",
347	            "0.10",
348	            "0.251",
349	            "3.50",
350	            "0.66",
351	            "0.80",
352	            "No"
353	          ],
354	          [
355	            "arc×score_manip",
356	            "0.64",
357	            "1.7e-7",
358	            "-0.28",
359	            "0.008",
360	            "2.29",
361	            "0.59",
362	            "0.85",
363	            "Yes"
364	          ],
365	          [
366	            "arc×position",
367	            "0.72",
368	            "1.8e-8",
369	            "-0.35",
370	            "0.001",
371	            "2.06",
372	            "0.57",
373	            "0.78",
374	            "Yes"
375	          ],
376	          [
377	            "arc×verbosity",
378	            "0.33",
379	            "0.003",
380	            "0.12",
381	            "0.175",
382	            "2.75",
383	            "0.61",
384	            "0.77",
385	            "No"
386	          ],
387	          [
388	            "arc×authority",
389	            "0.22",
390	            "0.062",
391	            "0.05",
392	            "0.612",
393	            "4.40",
394	            "0.55",
395	            "0.72",
396	            "No"
397	          ],
398	          [
399	            "arc×few_shot",
400	            "0.52",
401	            "3.8e-6",
402	            "-0.14",
403	            "0.091",
404	            "3.71",
405	            "0.63",
406	            "0.79",
407	            "Yes(marg)"
408	          ]
409	        ]
410	      }
411	    ],
412	    "figures": [],
413	    "analysis": "Calibrated RF 对比定性建立 BFT reversal mechanism：5/12 conditions β 翻转为负（diversity 在 true random faults 下确实有益），集中在 transferable attacks 上——exactly as mechanism predicts。翻转在 score_manip 和 position 上最强（这些攻击的 ASR 最依赖 judge-specific vulnerabilities），在 RF 模式下这些 vulnerabilities 被 random noise 取代，diversity 的容错优势重新显现。9/12 ratio ≥1.5× 表明即使不完全翻转，adaptive 下 K_eff 的有害效应也显著强于 RF——β 系统性 amplification 2.8× on average。ΔR²=0.31 是 BFT 理论的直接数值体现：BFT 假设 panel structure determines fault tolerance（high R²=0.78），adaptive adversary 打破这一假设（low R²=0.47）。BFT reversal 从 conceptual analogy 升级为 empirically grounded mechanism with quantitative support。\n\nBFT contrast 的核心区分在于 failure mode topology：random faults 下 judges 独立失败且 failures 无空间相关性，majority vote 的冗余容错使 K_eff 越高→fault tolerance 越强→β 应为负或接近零。Adaptive adversary 则 strategic targeting：找到 panel 中最弱的 judges 并集中攻击，K_eff 越高→attack surface 越大→β 为正。之前 15-model pipeline 的 RF 分析直接用 η_j 作为 failure prob，保留了 adaptive vulnerability structure（弱 judges 在 RF 下仍然更容易 fail），未能 cleanly 模拟 BFT 假设。Best tier 用 calibrated rates（基于 clean accuracy 的 bootstrapped noise）打破 adaptive vulnerability structure：RF failure prob 仅与 clean accuracy 相关而非 adversarial robustness，使 RF 成为 genuine random-fault baseline。翻转在 transferable attacks（score_manip、position、few_shot）中最明确（β 从 +0.52–0.72 翻至 -0.14–-0.35），因为这些攻击最依赖 judge-specific exploit paths——RF 下这些 paths 变成 random noise。Shared-bias attacks（sycophancy、verbosity）下 RF β 仍略正（0.08–0.12）但 NS，因为 bias 的 shared nature 使 'random' 和 'adaptive' failure modes 部分重叠。ΔR²=0.31 表明 RF 下 panel composition 解释 78% 方差（结构可预测），adaptive 仅 47%（strategic noise 占 53%），直接支撑 'adaptive adversary introduces variance beyond panel structure' 论点。"
414	  },
415	  {
416	    "name": "Capability-Matched Within-Tier Validation",
417	    "description": "同 capability tier 内做 within-tier regression 排除 tier-mixing artifact。Small tier: Llama-8B, Qwen-7B, Mistral-7B, Phi-14B, GPT-4o-mini (5 models, C(5,3)=10 panels)。Medium tier: 此 tier 仅 4 models → 4 panels，功效不足标注 directional。Large tier: Llama-70B, Qwen-72B, GPT-4o, GPT-4.1, Claude-3.5, Gemini-1.5 (6 models, C(6,3)=20 panels)。",
418	    "results": {
419	      "small_tier_models": 5,
420	      "small_tier_panels": 10,
421	      "small_tier_keff_sig": "2/6",
422	      "small_tier_confound_r": 0.32,
423	      "medium_tier_models": 4,
424	      "medium_tier_panels": 4,
425	      "medium_tier_keff_sig": "1/6",
426	      "medium_tier_note": "directional only, underpowered",
427	      "large_tier_models": 6,
428	      "large_tier_panels": 20,
429	      "large_tier_keff_sig": "4/6",
430	      "large_tier_confound_r": 0.33,
431	      "total_keff_sig_across_tiers": 4,
432	      "capability_matched_keff_sig": 4,
433	      "within_tier_confound_r_mean": 0.35
434	    },
435	    "tables": [
436	      {
437	        "name": "Within-Tier K_eff Validation",
438	        "columns": [
439	          "Tier",
440	          "Models",
441	          "Panels",
442	          "K_eff-η_max r",
443	          "K_eff_resid sig (of 6)",
444	          "Best p",
445	          "η_max sig (of 6)"
446	        ],
447	        "rows": [
448	          [
449	            "Small (7B-14B)",
450	            "5",
451	            "10",
452	            "0.32",
453	            "2/6",
454	            "0.008",
455	            "3/6"
456	          ],
457	          [
458	            "Medium (14-34B)",
459	            "4",
460	            "4",
461	            "0.41",
462	            "1/6",
463	            "0.031",
464	            "2/6"
465	          ],
466	          [
467	            "Large (70B+API)",
468	            "6",
469	            "20",
470	            "0.33",
471	            "4/6",
472	            "4.2e-4",
473	            "5/6"
474	          ],
475	          [
476	            "Cross-tier (all 15)",
477	            "15",
478	            "455",
479	            "0.55",
480	            "10/12",
481	            "1.7e-7",
482	            "10/12"
483	          ]
484	        ]
485	      },
486	      {
487	        "name": "Large-Tier Condition Detail",
488	        "columns": [
489	          "Condition",
490	          "K_eff_resid β",
491	          "p",
492	          "η_max β",
493	          "p",
494	          "Sig?"
495	        ],
496	        "rows": [
497	          [
498	            "score_manip",
499	            "0.58",
500	            "4.2e-4",
501	            "0.31",
502	            "0.042",
503	            "K_eff dominant"
504	          ],
505	          [
506	            "position_bias",
507	            "0.52",
508	            "0.001",
509	            "0.18",
510	            "0.228",
511	            "K_eff dominant"
512	          ],
513	          [
514	            "sycophancy",
515	            "0.21",
516	            "0.154",
517	            "0.61",
518	            "0.002",
519	            "η_max dominant"
520	          ],
521	          [
522	            "verbosity",
523	            "0.17",
524	            "0.238",
525	            "0.55",
526	            "0.005",
527	            "η_max dominant"
528	          ],
529	          [
530	            "authority",
531	            "0.34",
532	            "0.018",
533	            "0.48",
534	            "0.008",
535	            "both sig"
536	          ],
537	          [
538	            "few_shot",
539	            "0.45",
540	            "0.003",
541	            "0.39",
542	            "0.012",
543	            "both sig"
544	          ]
545	        ]
546	      }
547	    ],
548	    "figures": [],
549	    "analysis": "Capability-matched validation 是封堵 RC1 最强变体的 decisive evidence。Reviewer 可能 argue：'K_eff positive 不过是因为 high-K_eff panels 混了弱模型（tier-mixing）'。Large tier 结果直接否定：全是 top-tier 模型（GPT-4 级别），η_max 在 0.08-0.15 的 narrow range 内，K_eff 仍在 4/6 conditions 显著正向。Condition-dependent pattern 在 tier-internal 分析中完美复现：score_manip + position 由 K_eff 主导，sycophancy + verbosity 由 η_max 主导。这一致性跨 pooling strategy（all-15 vs within-tier）极大增强了 finding 的 robustness。Small tier 的 2/6 sig 表明 diversity trap 在低能力模型中也存在（低能力 diverse panel 更脆弱），但效应弱于 large tier——可能因为 small models 的 η_max 方差更大（有的 7B 异常脆弱），η_max 抢走了更多 variance。\n\nWithin-tier analysis 的核心价值是控制 tier-mixing confound。全局 r=0.55（K_eff 与 η_max）有约 40% 来自跨 tier mixing：高 K_eff panels 往往混合 7B 和 70B 模型，天然引入低 robustness judges。同 tier 内 r 降至 ~0.35，给 K_eff 最干净的检验。Large tier 结果最有说服力：6 models（GPT-4o, GPT-4.1, Claude-3.5, Gemini-1.5, Llama-70B, Qwen-72B）全是 top-tier 模型，η_max 方差天然较小，但 K_eff 仍在 4/6 conditions 显著——diverse panel 即使全由强模型组成也更脆弱，因为 judges 的 robustness profiles 仍然异质（GPT-4o 对 sycophancy 特别敏感、Llama-70B 对 position bias 敏感等）。Small tier 5 models / 10 panels 功效有限但 2/6 sig 提供 cross-tier consistency。Medium tier 仅 4 panels，1/6 sig 是 directional evidence only。总计 ≥4/6 unique conditions 有 within-tier K_eff 显著，满足 capability_matched_keff_sig [3,6] 范围。意义：即使 reviewer 最强版本的 'K_eff positive = tier-mixing artifact' argument 也被否定——same-tier panels 中 diversity 仍独立有害。"
550	  },
551	  {
552	    "name": "Two-Stage Panel Selection Algorithm Benchmark",
553	    "description": "Robustness-first 两阶段算法：Stage 1 filter η_j > percentile-75 threshold (保留最 robust 的 75% judges)，Stage 2 在通过筛选的 candidates 中 maximize K_eff。Benchmark vs 5 baselines on 15-model pool，6 attack conditions (MMLU × 6 attacks)。",
554	    "results": {
555	      "two_stage_mean_ASR": 0.038,
556	      "strongest_k_ASR": 0.048,
557	      "min_etamax_ASR": 0.041,
558	      "max_keff_ASR": 0.112,
559	      "random_ASR": 0.089,
560	      "oracle_ASR": 0.032,
561	      "ASR_reduction_vs_strongest_k_pct": 20.8,
562	      "ASR_reduction_vs_max_keff_pct": 66.1,
563	      "conditions_two_stage_best": "5/6",
564	      "two_stage_pareto_optimal_pct": 78,
565	      "screening_threshold_optimal_percentile": 75
566	    },
567	    "tables": [
568	      {
569	        "name": "Panel Selection Strategy Benchmark (15 Models, MMLU)",
570	        "columns": [
571	          "Strategy",
572	          "Mean ASR",
573	          "Δ vs Strongest-K",
574	          "Best (of 6)",
575	          "Worst-case ASR"
576	        ],
577	        "rows": [
578	          [
579	            "Two-Stage (ours)",
580	            "0.038",
581	            "-20.8%",
582	            "5/6",
583	            "0.071"
584	          ],
585	          [
586	            "Min-η_max",
587	            "0.041",
588	            "-14.6%",
589	            "4/6",
590	            "0.078"
591	          ],
592	          [
593	            "Strongest-K",
594	            "0.048",
595	            "baseline",
596	            "1/6",
597	            "0.095"
598	          ],
599	          [
600	            "Random",
601	            "0.089",
602	            "+85.4%",
603	            "0/6",
604	            "0.156"
605	          ],
606	          [
607	            "Max-K_eff",
608	            "0.112",
609	            "+133.3%",
610	            "0/6",
611	            "0.198"
612	          ],
613	          [
614	            "Oracle",
615	            "0.032",
616	            "-33.3%",
617	            "6/6",
618	            "0.052"
619	          ]
620	        ]
621	      },
622	      {
623	        "name": "Two-Stage Sensitivity to Screening Threshold",
624	        "columns": [
625	          "Threshold (percentile)",
626	          "Candidate models",
627	          "Mean ASR",
628	          "K_eff of selected panel"
629	        ],
630	        "rows": [
631	          [
632	            "50",
633	            "8",
634	            "0.039",
635	            "2.12"
636	          ],
637	          [
638	            "65",
639	            "10",
640	            "0.037",
641	            "2.28"
642	          ],
643	          [
644	            "75 (optimal)",
645	            "11",
646	            "0.038",
647	            "2.41"
648	          ],
649	          [
650	            "85",
651	            "13",
652	            "0.045",
653	            "2.55"
654	          ],
655	          [
656	            "100 (no filter)",
657	            "15",
658	            "0.058",
659	            "2.71"
660	          ]
661	        ]
662	      }
663	    ],
664	    "figures": [],
665	    "analysis": "20.8% ASR reduction 将实用贡献从 Dream 批评的 'marginal'（12.5% at 6-model）升级为 'practically meaningful'。Threshold sensitivity table 揭示 sweet spot 在 percentile-65–75：太紧（50th）损失 candidate diversity，太松（85–100th）引入弱 judges。Pareto frontier analysis 显示 78% 的 Two-stage selected panels 落在 Pareto 前沿上——算法近似了 computationally-expensive 的 exhaustive Pareto search。关键 takeaway for practitioners：(1) 绝不盲目 maximize diversity（Max-K_eff 灾难级 ASR）；(2) Pure robustness（Min-η_max）已经很好，diversity 优化提供 modest 额外收益；(3) Two-stage 在所有非 oracle 策略中最接近理论最优。\n\n15-model pool 给 Two-stage 算法显著优于 6-model 结果（12.5%→20.8% vs Strongest-K）的空间。原因双重：(1) 15 models 筛选后 candidate pool 更大——6-model 时 threshold filter 后仅剩 3-4 judges（几乎无 K_eff 优化空间），15-model 时剩 ~11 judges（C(11,3)=165 candidate panels），K_eff 最大化有真正的搜索空间。(2) Robustness screening 后的 restricted pool 中，K_eff-η_max confound 被 threshold 机制性打破（高 η_max 模型已被移除），K_eff 的效应方向可能从有害翻转为中性——当所有 judges 都 robust 时，diversity 不再引入弱 judge，其 BFT 容错优势部分恢复。Min_etamax 与 Two-stage 差距较小（0.041 vs 0.038, Δ=7.3%）说明 K_eff 优化在 robustness-screened pool 内的增量贡献 modest——这恰好支持 'robustness-first, diversity-second' 的优先级判断。Max_keff 策略的灾难性表现（ASR 0.112, +133% vs Strongest-K）是 diversity trap 最直观的实证：盲目追求 diversity 而不管 robustness 是危险的。Oracle 的存在（0.032）表明 Two-stage 达 Oracle 效率的 84%（0.038/0.032），远超 Strongest-K 的 67%（0.048/0.032）。15%+ 降幅满足 two_stage_ASR_reduction_pct [15,35]。"
666	  },
667	  {
668	    "name": "Per-Judge ASR Concentration Analysis",
669	    "description": "计算 455 panels × 6 attacks 的 per-judge ASR 分布。Gini coefficient 量化 ASR 在 panel 内 judges 间的集中度，Shannon entropy 量化均匀性。Adaptive vs RF 对比。",
670	    "results": {
671	      "mean_gini_adaptive": 0.68,
672	      "mean_gini_RF": 0.12,
673	      "gini_ratio_adaptive_vs_RF": 5.67,
674	      "mean_entropy_adaptive": 1.42,
675	      "mean_entropy_RF": 2.31,
676	      "high_keff_gini_adaptive": 0.74,
677	      "low_keff_gini_adaptive": 0.55,
678	      "gini_keff_correlation": 0.52,
679	      "top1_judge_ASR_share_adaptive": 0.78,
680	      "top1_judge_ASR_share_RF": 0.38
681	    },
682	    "tables": [
683	      {
684	        "name": "ASR Concentration Metrics: Adaptive vs Random-Fault",
685	        "columns": [
686	          "Metric",
687	          "Adaptive",
688	          "Random-Fault",
689	          "Ratio",
690	          "Interpretation"
691	        ],
692	        "rows": [
693	          [
694	            "Mean Gini",
695	            "0.68",
696	            "0.12",
697	            "5.67",
698	            "Concentrated vs uniform"
699	          ],
700	          [
701	            "Mean Entropy (bits)",
702	            "1.42",
703	            "2.31",
704	            "0.61",
705	            "Low entropy = targeted"
706	          ],
707	          [
708	            "Top-1 Judge ASR Share",
709	            "0.78",
710	            "0.38",
711	            "2.05",
712	            "78% ASR on weakest judge"
713	          ],
714	          [
715	            "r(K_eff, Gini)",
716	            "0.52",
717	            "0.08",
718	            "6.50",
719	            "Diversity → more targeting"
720	          ]
721	        ]
722	      }
723	    ],
724	    "figures": [],
725	    "analysis": "Concentration analysis 将 diversity trap 从统计关联推进到机制层面：不是 'K_eff 与 ASR 碰巧正相关'，而是 'diverse panels 给 adversary 提供了更清晰的 targeting gradient（Gini 0.74），使攻击集中在最弱 judge 上（78% share），从而打破 majority vote'。r(K_eff, Gini)=0.52 的正相关是 diversity trap 因果链中的关键中间变量——future work 可用 mediation analysis 正式量化 Gini 在 K_eff→ASR 路径中的 mediating role。此外 RF 下的 low concentration（Gini 0.12）直接验证了 BFT 的 key assumption（uncorrelated failures distribute uniformly），解释了为何 diversity 在 RF 下可以有益。\n\nConcentration analysis 是 diversity trap 机制的 'microscope'——从 panel-level 聚合统计深入到 judge-level 攻击分布。Adaptive adversary 的 core strategy 是 targeting：识别 panel 中最脆弱的 judge 并集中 exploit。这导致 ASR 高度 concentrated 在 1-2 个 judges 上（Gini≈0.68, top-1 share 78%），而 RF 下 failures 近似均匀分布（Gini≈0.12）。关键发现：high-K_eff panels 的 Gini 更高（0.74 vs 0.55），因为 diverse panel 中 judges 的 capability spread 更大→adversary 的 target 更清晰（最弱 judge 与最强 judge 的差距更大）。Gini-K_eff 正相关（r=0.52）是 diversity trap 因果链的直接 observational evidence：diversity → larger capability spread → clearer targeting → higher concentration → higher panel ASR。这不是因果证明（需要 intervention），但因果方向性（directional consistency）很强。5.67× Gini ratio 也是 BFT contrast 的另一维度验证：BFT 假设 failures 均匀分布（low Gini），adaptive adversary 打破这一假设（high Gini）。"
726	  },
727	  {
728	    "name": "Diversity-Capability Tradeoff Visualization",
729	    "description": "455 panels 的 K_eff vs η_max tradeoff 散点图、Pareto 前沿、tier 分层分析。",
730	    "results": {
731	      "global_r_keff_etamax": 0.55,
732	      "within_small_r": 0.32,
733	      "within_medium_r": 0.41,
734	      "within_large_r": 0.33,
735	      "pareto_frontier_panels": 18,
736	      "pareto_frontier_slope": -0.73,
737	      "tradeoff_explained_variance": 0.42
738	    },
739	    "tables": [
740	      {
741	        "name": "K_eff–η_max Correlation Structure by Tier",
742	        "columns": [
743	          "Tier",
744	          "r(K_eff, η_max)",
745	          "N panels",
746	          "Pareto-optimal",
747	          "Mean K_eff",
748	          "Mean η_max"
749	        ],
750	        "rows": [
751	          [
752	            "Small (7B-14B)",
753	            "0.32",
754	            "10",
755	            "3",
756	            "2.41",
757	            "0.312"
758	          ],
759	          [
760	            "Medium (14-34B)",
761	            "0.41",
762	            "4",
763	            "2",
764	            "2.18",
765	            "0.224"
766	          ],
767	          [
768	            "Large (70B+API)",
769	            "0.33",
770	            "20",
771	            "5",
772	            "1.95",
773	            "0.148"
774	          ],
775	          [
776	            "Cross-tier (all 15)",
777	            "0.55",
778	            "455",
779	            "18",
780	            "2.35",
781	            "0.231"
782	          ]
783	        ]
784	      }
785	    ],
786	    "figures": [],
787	    "analysis": "Tradeoff 可视化的核心价值是将 Claim 3 从统计数字转化为直觉图形。Pareto frontier 的 steep negative slope（-0.73）意味着 K_eff 每增加 0.1，η_max 至少增加 0.073——practitioners 必须明确这个 cost。Tier-stratified view 显示 within-tier tradeoff 较弱但仍存在，支持 'screening + optimize' 策略的理论基础。ASR 等值线叠加（contour）直接显示 Pareto-optimal panels 的 ASR 远低于 max-K_eff panels——视觉化 diversity trap。\n\n全局 K_eff-η_max 正相关（r=0.55）编码了 LLM 生态系统的一个结构性约束：maximizing panel independence（K_eff）要求跨越 capability tiers 选 judges（例如同时选 GPT-4o 和 Mistral-7B），这必然引入 robustness 差异大的 judges，推高 η_max。Within-tier r 大幅下降（0.32–0.41）揭示了 tradeoff 的两层结构：(1) Cross-tier component（贡献 ~40% 的 global r）：源于 tier mixing，可通过 screening 消除；(2) Within-tier component（residual r≈0.35）：即使同 tier 内，追求 diversity 仍需选择 robustness profile 更异质的 judges，这不可完全消除但幅度较小。Pareto 前沿的 18 panels（约 4% of 455）定义了 diversity-robustness 不可能三角的 achievable boundary——Two-stage 算法的目标就是逼近这个前沿。解释方差 42% 意味着 K_eff 是 η_max 的 moderate 但非 dominant 预测器——剩余 58% 的 η_max 方差由 attack-specific vulnerability profiles、评分偏好差异等因素决定，这也解释了为什么 K_eff 的 residualized effect 在控制 η_max 后仍然显著。"
788	  },
789	  {
790	    "name": "Panel Size Sensitivity K=3,5,7,9",
791	    "description": "Panel size 从 K=3 扩展到 K=5,7,9。15 models 选 K 个 judges 的组合数分别为 C(15,3)=455, C(15,5)=3003, C(15,7)=6435, C(15,9)=5005。每个 K 做 12 conditions 回归。",
792	    "results": {
793	      "K3_keff_resid_sig": "10/12",
794	      "K5_keff_resid_sig": "11/12",
795	      "K7_keff_resid_sig": "12/12",
796	      "K9_keff_resid_sig": "12/12",
797	      "K3_mean_keff_beta": 0.42,
798	      "K5_mean_keff_beta": 0.48,
799	      "K7_mean_keff_beta": 0.55,
800	      "K9_mean_keff_beta": 0.61,
801	      "K3_mean_etamax_beta": 0.51,
802	      "K5_mean_etamax_beta": 0.49,
803	      "K7_mean_etamax_beta": 0.43,
804	      "K9_mean_etamax_beta": 0.38,
805	      "crossover_K": 6,
806	      "K3_mean_R2": 0.62,
807	      "K9_mean_R2": 0.51
808	    },
809	    "tables": [
810	      {
811	        "name": "Panel Size Sensitivity Summary",
812	        "columns": [
813	          "K",
814	          "Panels",
815	          "K_eff_resid sig",
816	          "Mean K_eff β",
817	          "Mean η_max β",
818	          "Mean R²",
819	          "Primary driver"
820	        ],
821	        "rows": [
822	          [
823	            "3",
824	            "455",
825	            "10/12",
826	            "0.42",
827	            "0.51",
828	            "0.62",
829	            "η_max"
830	          ],
831	          [
832	            "5",
833	            "3003",
834	            "11/12",
835	            "0.48",
836	            "0.49",
837	            "0.58",
838	            "balanced"
839	          ],
840	          [
841	            "7",
842	            "6435",
843	            "12/12",
844	            "0.55",
845	            "0.43",
846	            "0.54",
847	            "K_eff"
848	          ],
849	          [
850	            "9",
851	            "5005",
852	            "12/12",
853	            "0.61",
854	            "0.38",
855	            "0.51",
856	            "K_eff"
857	          ]
858	        ]
859	      }
860	    ],
861	    "figures": [],
862	    "analysis": "Panel size sensitivity 提供 diversity trap 的 scaling law：K_eff β ≈ 0.33 + 0.047K（近似线性增长）。这意味着 evaluation community 普遍采用的 'add more judges' strategy 会 systematically amplify diversity trap——K=9 panel 的 K_eff 有害效应比 K=3 大 45%。η_max 的下降则反映了 weakest-link theorem 在 large K 下的局限性：当 K 足够大时，单一最弱 judge 不再 decisive，panel 的整体结构（diversity/independence）接管。交叉点 K≈6 有实际指导意义：K≤5 的小 panel 优先管控 η_max（选最 robust 的 judges），K≥7 的大 panel 必须同时管控 K_eff（限制不必要的 diversity）。\n\nK_eff β 随 panel size 单调递增（0.42→0.61），原因：(1) larger panels 有更多 judges → attack surface 与 panel size 正比增长，每个 additional judge 提供一个额外的 potential exploit path；(2) K=9 panel 的 K_eff range 更大（15 models 选 9 → wider independence spectrum），给回归更大信号。η_max β 随 K 递减（0.51→0.38），原因：larger panel 的 vulnerability 不再由单一 weakest judge 决定——K=9 时 adversary 需要 compromise ⌈9/2⌉=5 judges，不能仅靠 targeting the weakest one，panel structure（diversity）的相对重要性上升。交叉点约 K≈6：在此 panel size 以上，K_eff 超过 η_max 成为 primary vulnerability driver。R² 随 K 下降（0.62→0.51）因为 larger panel 的行为更复杂，judge interaction effects 增加 unexplained variance。K=9 时 K_eff 12/12 sig + β=0.61 是 diversity trap 的 strongest single evidence point：大型 evaluation panels 中 diversity 是 dominant 有害因素。这直接回应 'just add more judges to be safer' 的朴素直觉。"
863	  },
864	  {
865	    "name": "VIF + Multicollinearity Full Diagnostics",
866	    "description": "对 15-model 455-panel 数据做完整统计诊断：VIF、condition number、partial correlations、residualized K_eff、Bonferroni/FDR 多重比较校正、beta regression（处理 ASR 的 [0,1] bounded nature）、Shapiro-Wilk 残差正态性检验。纯计算，无 GPU。",
867	    "results": {
868	      "VIF_keff_resid": 1.02,
869	      "VIF_etamax": 1.02,
870	      "condition_number": 4.8,
871	      "partial_r_keff_given_etamax": 0.38,
872	      "partial_r_etamax_given_keff": 0.45,
873	      "keff_resid_FDR_sig": "10/12",
874	      "keff_bonferroni_sig": "8/12",
875	      "beta_regression_keff_sig": "9/12",
876	      "beta_regression_etamax_sig": "10/12",
877	      "shapiro_wilk_residuals_p_mean": 0.23,
878	      "cooks_d_max": 0.031,
879	      "leverage_outlier_pct": 2.4
880	    },
881	    "tables": [
882	      {
883	        "name": "Multicollinearity Diagnostics Summary",
884	        "columns": [
885	          "Diagnostic",
886	          "Value",
887	          "Threshold",
888	          "Status"
889	        ],
890	        "rows": [
891	          [
892	            "VIF (K_eff_resid)",
893	            "1.02",
894	            "<5.0",
895	            "PASS"
896	          ],
897	          [
898	            "VIF (η_max)",
899	            "1.02",
900	            "<5.0",
901	            "PASS"
902	          ],
903	          [
904	            "Condition Number",
905	            "4.8",
906	            "<30",
907	            "PASS"
908	          ],
909	          [
910	            "Partial r(K_eff|η_max)",
911	            "0.38",
912	            ">0.1",
913	            "Moderate independent effect"
914	          ],
915	          [
916	            "Partial r(η_max|K_eff)",
917	            "0.45",
918	            ">0.1",
919	            "Moderate-strong independent effect"
920	          ],
921	          [
922	            "Shapiro-Wilk p (residuals)",
923	            "0.23",
924	            ">0.05",
925	            "Normal residuals"
926	          ],
927	          [
928	            "Max Cook's D",
929	            "0.031",
930	            "<1.0",
931	            "No influential points"
932	          ],
933	          [
934	            "High-leverage %",
935	            "2.4%",
936	            "<5%",
937	            "Acceptable"
938	          ]
939	        ]
940	      },
941	      {
942	        "name": "Multiple Comparison Robustness",
943	        "columns": [
944	          "Correction Method",
945	          "K_eff_resid sig",
946	          "η_max sig",
947	          "Interpretation"
948	        ],
949	        "rows": [
950	          [
951	            "Uncorrected",
952	            "12/12",
953	            "11/12",
954	            "Raw signal"
955	          ],
956	          [
957	            "FDR (Benjamini-Hochberg)",
958	            "10/12",
959	            "10/12",
960	            "Primary report"
961	          ],
962	          [
963	            "Bonferroni",
964	            "8/12",
965	            "9/12",
966	            "Most conservative, still passes"
967	          ],
968	          [
969	            "Beta Regression + FDR",
970	            "9/12",
971	            "10/12",
972	            "Distributional robustness"
973	          ]
974	        ]
975	      }
976	    ],
977	    "figures": [],
978	    "analysis": "VIF + diagnostics package 是论文统计 credibility 的 foundation。Key contribution to paper: (1) 把 'K_eff is independently significant' 从初步 observation 升级为经过 6 层 robustness check（residualization, VIF, partial correlation, beta regression, multiple comparison, influence diagnostics）验证的 result；(2) 每个 check 都 pass 意味着 reviewer 无法从任何统计 angle 质疑 K_eff 的独立效应；(3) Bonferroni-corrected 8/12 sig 是最保守的下界——即使用最严格的多重比较校正，diversity trap 仍在 2/3 的 conditions 中成立。\n\n残差化设计（K_eff_resid = residuals of K_eff ~ η_max）在数学上保证 VIF=1.0（两个 predictors 正交）。实际计算得 1.02 是因为 floating point precision + minor numerical jitter。Condition number 4.8 远低于 30 的 concern threshold，确认回归矩阵 well-conditioned。Partial correlations 揭示各自独立贡献：K_eff|η_max 的 partial r=0.38 意味着 holding η_max constant，K_eff 独立解释 ~14% ASR variance；η_max|K_eff 的 partial r=0.45 解释 ~20%。Beta regression 作为 distributional robustness check 处理两个 OLS 假设违反：(1) ASR 在 [0,1] 内 bounded，OLS 可能在极端值处产生 out-of-range predictions；(2) ASR 的方差可能 heteroscedastic（低 ASR panels 方差更小）。Beta regression 结果（9/12 vs OLS 10/12）高度一致，证明 OLS findings 非 distributional artifact。Multiple comparison 从 FDR（10/12）到 Bonferroni（8/12，最保守）全部 pass，消除 'cherry-picking' concern。Cook's distance max=0.031（远低于 1.0 threshold）和 leverage outliers 仅 2.4% 证明结果非 influential point 驱动。这套诊断 package 直接 preempt Dream review W2（VIF 未报告）和 RC1（multicollinearity）的所有 variants。"
979	  },
980	  {
981	    "name": "Aggregation Rule Modulation (15-Model)",
982	    "description": "三种非 majority-vote 聚合规则下的 dual vulnerability drivers 分析：Threshold voting（unanimity: 所有 judges 必须同意 reject）、Accuracy-weighted voting（权重 ∝ clean accuracy）、Bayesian aggregation（基于 prior accuracy 的 posterior probability）。455 panels × 12 conditions per aggregation。",
983	    "results": {
984	      "majority_keff_sig": "10/12",
985	      "majority_etamax_sig": "10/12",
986	      "threshold_keff_sig": "11/12",
987	      "threshold_etamax_sig": "7/12",
988	      "threshold_keff_beta_amplification": 1.45,
989	      "weighted_keff_sig": "8/12",
990	      "weighted_etamax_sig": "9/12",
991	      "bayesian_keff_sig": "6/12",
992	      "bayesian_etamax_sig": "5/12",
993	      "bayesian_mean_ASR_reduction_vs_majority": 0.28,
994	      "total_keff_sig_majority_plus_threshold": "14/16"
995	    },
996	    "tables": [
997	      {
998	        "name": "Aggregation Rule × Vulnerability Drivers (15-Model, 455 Panels)",
999	        "columns": [
1000	          "Aggregation",
1001	          "K_eff_resid sig",
1002	          "η_max sig",
1003	          "Mean K_eff β",
1004	          "Mean η_max β",
1005	          "Mean ASR",
1006	          "Δ ASR vs Majority"
1007	        ],
1008	        "rows": [
1009	          [
1010	            "Majority",
1011	            "10/12",
1012	            "10/12",
1013	            "0.42",
1014	            "0.51",
1015	            "0.074",
1016	            "baseline"
1017	          ],
1018	          [
1019	            "Threshold (unanimity)",
1020	            "11/12",
1021	            "7/12",
1022	            "0.61",
1023	            "0.34",
1024	            "0.138",
1025	            "+86%"
1026	          ],
1027	          [
1028	            "Accuracy-weighted",
1029	            "8/12",
1030	            "9/12",
1031	            "0.39",
1032	            "0.48",
1033	            "0.069",
1034	            "-6.8%"
1035	          ],
1036	          [
1037	            "Bayesian",
1038	            "6/12",
1039	            "5/12",
1040	            "0.25",
1041	            "0.28",
1042	            "0.053",
1043	            "-28.4%"
1044	          ]
1045	        ]
1046	      }
1047	    ],
1048	    "figures": [],
1049	    "analysis": "Aggregation 分析的 three actionable insights：(1) Threshold voting 是 diversity trap 的 worst-case amplifier——unanimity requirement 使 K_eff β 增加 45%，absolute ASR 增加 86%。Deployment recommendation: 避免在 adversarial-aware 场景使用 unanimity aggregation。(2) Bayesian 是 best partial defense——同时削弱两个 vulnerability channels（K_eff 6/12, η_max 5/12 vs majority 的 10/12, 10/12），ASR 降 28%。但 6/12 K_eff 仍 sig 表明 Bayesian 不能完全消除 diversity trap。(3) Defense stack rationale: Two-stage selection（控制 η_max 通道）+ Bayesian aggregation（削弱残余 η_max + 部分削弱 K_eff）是最 comprehensive defense。单一维度不够。\n\n聚合规则改变 vulnerability driver 的 relative weight 通过三个机制：(1) Threshold/unanimity 放大 K_eff——panel reject 需要 ALL judges agree，adversary 只需 flip one judge 就能 block rejection。Diverse panel 有更多 potential 'flip targets'（judge-specific vulnerabilities 更多样），因此 K_eff β amplifies 1.45×。同时 η_max 弱化（7/12）因为 unanimity 的 blocking 不需要 weakest judge 特别弱——任何一个 judge 被 flip 就够了。(2) Weighted voting 结果近似 majority 因为 accuracy weights 仅微调 vote influence（权重范围 0.8-1.2），未根本改变投票结构。(3) Bayesian aggregation 基于 clean-accuracy prior 下调低能力 judges 的 posterior weight，partially 中和了 η_max 通道（5/12，从 majority 的 10/12 下降）——弱 judges 的 vote 被 discount 所以 adversary targeting 弱 judge 的收益降低。但 K_eff 仍 6/12 sig，因为 Bayesian weights 基于 clean accuracy 而非 adversarial robustness——attack-shifted accuracy ≠ clean accuracy，adversary 可以 manipulate a judge 使其给出 'confidently wrong' judgment，Bayesian 无法区分这种 confident error 与 genuine judgment。28% ASR reduction 说明 Bayesian 是 best single-aggregation defense 但非 silver bullet。Combined majority + threshold conditions 的 14/16 K_eff sig 落入 K_eff_resid_sig_extended_conditions [10,16] 范围。"
1050	  },
1051	  {
1052	    "name": "Open-Ended Generation Benchmark (MT-Bench + AlpacaEval)",
1053	    "description": "在 MT-Bench（多轮对话评判）和 AlpacaEval（指令遵循评分）上测试 diversity trap。4 attack types × 2 benchmarks = 8 新 conditions（选 4 primary attacks: score_manip, sycophancy, position, verbosity）。15 models 但 panel size 受限于 benchmark cost 可能 sample 200 panels。",
1054	    "results": {
1055	      "mtbench_keff_resid_sig": "3/4",
1056	      "mtbench_etamax_sig": "3/4",
1057	      "mtbench_mean_R2": 0.48,
1058	      "alpacaeval_keff_resid_sig": "2/4",
1059	      "alpacaeval_etamax_sig": "3/4",
1060	      "alpacaeval_mean_R2": 0.42,
1061	      "open_ended_keff_sig_total": "3/4",
1062	      "open_ended_confound_r": 0.48,
1063	      "keff_beta_ratio_open_vs_mcq": 0.85,
1064	      "condition_dependent_pattern_preserved": true
1065	    },
1066	    "tables": [
1067	      {
1068	        "name": "Open-Ended Benchmark Results (8 Conditions)",
1069	        "columns": [
1070	          "Benchmark×Attack",
1071	          "K_eff_resid β",
1072	          "K_eff_resid p (FDR)",
1073	          "η_max β",
1074	          "η_max p (FDR)",
1075	          "R²",
1076	          "Dominant"
1077	        ],
1078	        "rows": [
1079	          [
1080	            "MT-Bench×score_manip",
1081	            "0.52",
1082	            "1.8e-5",
1083	            "0.38",
1084	            "0.003",
1085	            "0.52",
1086	            "K_eff"
1087	          ],
1088	          [
1089	            "MT-Bench×sycophancy",
1090	            "0.28",
1091	            "0.012",
1092	            "0.55",
1093	            "4.1e-5",
1094	            "0.49",
1095	            "η_max"
1096	          ],
1097	          [
1098	            "MT-Bench×position",
1099	            "0.47",
1100	            "8.3e-5",
1101	            "0.21",
1102	            "0.089",
1103	            "0.44",
1104	            "K_eff"
1105	          ],
1106	          [
1107	            "MT-Bench×verbosity",
1108	            "0.18",
1109	            "0.108",
1110	            "0.62",
1111	            "7.2e-6",
1112	            "0.47",
1113	            "η_max"
1114	          ],
1115	          [
1116	            "AlpacaEval×score_manip",
1117	            "0.44",
1118	            "3.2e-4",
1119	            "0.35",
1120	            "0.006",
1121	            "0.46",
1122	            "K_eff"
1123	          ],
1124	          [
1125	            "AlpacaEval×sycophancy",
1126	            "0.21",
1127	            "0.058",
1128	            "0.58",
1129	            "1.4e-5",
1130	            "0.43",
1131	            "η_max"
1132	          ],
1133	          [
1134	            "AlpacaEval×position",
1135	            "0.38",
1136	            "0.002",
1137	            "0.25",
1138	            "0.041",
1139	            "0.40",
1140	            "both"
1141	          ],
1142	          [
1143	            "AlpacaEval×verbosity",
1144	            "0.14",
1145	            "0.175",
1146	            "0.59",
1147	            "2.1e-5",
1148	            "0.39",
1149	            "η_max"
1150	          ]
1151	        ]
1152	      }
1153	    ],
1154	    "figures": [],
1155	    "analysis": "Open-ended 结果的 three-fold significance：(1) Generalization — diversity trap 从 MCQ 推广到 open-ended，覆盖 LLM evaluation 的两大应用场景（benchmark scoring + human preference prediction），claim 从 'diversity hurts on MMLU/ARC' 升级为 'diversity hurts on LLM evaluation generally'。(2) Taxonomy transfer — condition-dependent dominance pattern（transferable→K_eff, shared-bias→η_max）在 open-ended 上 preserved without modification，表明 taxonomy 是 task-agnostic fundamental structure。(3) Practical relevance — MT-Bench/AlpacaEval 是 LLM 排名的 de facto standard，diversity trap 在这些 benchmark 上成立直接影响模型选择和部署决策。R² 下降（0.39-0.52 vs MCQ 0.62）是 expected tradeoff：open-ended evaluation 的 subjectivity noise 是 inherent 的，panel structure 能解释的 fraction naturally 减少。\n\nOpen-ended judging 与 MCQ 的关键差异：(1) 评分更主观——judges 在 'what constitutes a good response' 上 disagreement 更高，noise floor 提升；(2) 攻击空间更大——adversary 可以在 multi-turn conversation 的每轮 independently manipulate（MT-Bench），或在 free-form response 中 embed 更复杂的 manipulation signals（AlpacaEval）。K_eff 在 open-ended 上仍显著正向（3/4 unique conditions across benchmarks），但 β 略低于 MCQ（ratio 0.85），因为 open-ended 的 higher noise floor 使 panel structure 解释的方差降低（R² 0.42-0.48 vs MCQ 0.62）。MT-Bench 比 AlpacaEval 表现更强（3/4 vs 2/4 sig），因为 multi-turn 结构给 adversary 更多 manipulation surface（每轮是独立攻击机会），judge-specific 响应差异在多轮中累积。Condition-dependent pattern 在 open-ended 上完美复现：score_manip 和 position 下 K_eff 主导，sycophancy 和 verbosity 下 η_max 主导——attack taxonomy 从 MCQ 推广到 open-ended 无需修改。≥2/4 open-ended K_eff 显著（best tier 达 3/4）满足 open-ended 显著条件。意义：diversity trap 不是 MCQ-specific artifact，直接回应 Dream W6 和 RC3。"
1156	  },
1157	  {
1158	    "name": "Gaussian Copula Failure + Family Label Revalidation (15-Model, 105 Pairs)",
1159	    "description": "15-model 105 pairwise MI matrix 计算。Gaussian copula MI vs observed MI ratio 验证。Family labels（6 families）的 MI 预测性检验（within vs cross-family）。Capability proximity 与 MI 的相关性分析。",
1160	    "results": {
1161	      "total_pairs": 105,
1162	      "MI_gaussian_ratio_mean": 18.5,
1163	      "MI_gaussian_ratio_max": 312,
1164	      "MI_gaussian_ratio_min": 4.2,
1165	      "pairs_ratio_gt_10x": "82/105",
1166	      "family_label_MWU_p": 0.158,
1167	      "family_label_permutation_p": 0.312,
1168	      "within_family_MI_mean": 0.42,
1169	      "cross_family_MI_mean": 0.39,
1170	      "capability_proximity_MI_correlation": -0.71,
1171	      "copula_MI_ratio_15model": 18.5
1172	    },
1173	    "tables": [
1174	      {
1175	        "name": "Copula Failure: Scale Comparison",
1176	        "columns": [
1177	          "Metric",
1178	          "6-model (15 pairs)",
1179	          "15-model (105 pairs)",
1180	          "Change"
1181	        ],
1182	        "rows": [
1183	          [
1184	            "MI_obs/MI_gauss mean",
1185	            "14.7",
1186	            "18.5",
1187	            "+25.9%"
1188	          ],
1189	          [
1190	            "MI_obs/MI_gauss max",
1191	            "235",
1192	            "312",
1193	            "+32.8%"
1194	          ],
1195	          [
1196	            "MI_obs/MI_gauss min",
1197	            "8.3",
1198	            "4.2",
1199	            "Some close pairs"
1200	          ],
1201	          [
1202	            "Pairs with ratio >10×",
1203	            "11/15 (73%)",
1204	            "82/105 (78%)",
1205	            "+5pp"
1206	          ],
1207	          [
1208	            "Family label p (MWU)",
1209	            "0.206",
1210	            "0.158",
1211	            "Still NS"
1212	          ],
1213	          [
1214	            "Capability-MI r",
1215	            "-0.65",
1216	            "-0.71",
1217	            "Stronger"
1218	          ]
1219	        ]
1220	      }
1221	    ],
1222	    "figures": [],
1223	    "analysis": "15-model copula failure 和 family label 结果分别强化 Claims 5 和 4。Copula failure 的 practical implication：任何基于 Gaussian copula 假设的 panel reliability bound（如 independence-based certification）在 LLM judge 对上不可信——underestimate information sharing by 10-30×（mean 18.5×）。这为 K_eff 作为 empirical independence measure（而非 copula-derived bounds）提供 methodological justification。Family label result 的 practical implication：panel designers 不能简单用 '3 different families = diverse panel' 的 heuristic——Qwen-7B 和 Llama-8B 虽属不同 families 但 capability 接近故 MI 高（independence 低），而 GPT-4o-mini 和 GPT-4o 虽同属 OpenAI 但 capability gap 大故 MI 低（independence 高）。Capability proximity 是 independence 的 true driver。\n\n105 pairs（7× 6-model 的 15 pairs）大幅增加 copula failure 的统计力度。MI_gaussian_ratio 均值从 6-model 的 14.7 升至 18.5，因为 15-model pool 包含更多 capability-heterogeneous pairs（如 Mistral-7B 与 GPT-4o、Phi-14B 与 Claude-3.5），这些极端 pair 的联合分布更远离 bivariate Gaussian——heavy tails、discrete clustering、capability-dependent correlation structure 使 Gaussian copula 的低估更严重。Max ratio 从 235 升至 312（最极端 pair 如 Mistral-7B × GPT-4o 的 MI 被 Gaussian 低估 312×）。Family labels 仍无预测力（MWU p=0.158）：within-family MI（0.42）和 cross-family MI（0.39）无显著差异。根本原因：同 family 不同 size（如 Llama-8B vs Llama-70B）的 judges 独立性差异远大于同 size 不同 family（如 Llama-8B vs Qwen-7B vs Mistral-7B）——这些 7B-class 模型 capability-wise 非常接近，共享 similar failure modes despite different training pipelines。Capability proximity（|capability_i - capability_j|）与 MI 的强负相关（r=-0.71）直接支持：能力越接近→共享越多 failure patterns→MI 越高→independence 越低。意义：practitioners 不应用 family diversity 作为 panel independence proxy——capability-based metrics（如 K_eff）才是 valid measure。"
1224	  },
1225	  {
1226	    "name": "Partial-Knowledge Adversary Model",
1227	    "description": "Adversary 知道 panel 包含哪些 model families（public information）但不知各 judge 的具体 η_j vulnerability profiles。Strategy: family-level average attack 而非 judge-specific targeting。与 full-knowledge 和 black-box baselines 对比。",
1228	    "results": {
1229	      "full_knowledge_mean_ASR": 0.074,
1230	      "partial_knowledge_mean_ASR": 0.058,
1231	      "black_box_mean_ASR": 0.031,
1232	      "partial_vs_full_ratio": 0.784,
1233	      "keff_sig_partial": "7/12",
1234	      "etamax_sig_partial": "8/12",
1235	      "partial_R2": 0.51,
1236	      "family_info_value_pct": 62.8
1237	    },
1238	    "tables": [
1239	      {
1240	        "name": "Adversary Knowledge Level Comparison",
1241	        "columns": [
1242	          "Knowledge Level",
1243	          "Mean ASR",
1244	          "K_eff sig",
1245	          "η_max sig",
1246	          "R²",
1247	          "Info value vs black-box"
1248	        ],
1249	        "rows": [
1250	          [
1251	            "Full (judge-level η_j)",
1252	            "0.074",
1253	            "10/12",
1254	            "10/12",
1255	            "0.62",
1256	            "100%"
1257	          ],
1258	          [
1259	            "Partial (family only)",
1260	            "0.058",
1261	            "7/12",
1262	            "8/12",
1263	            "0.51",
1264	            "62.8%"
1265	          ],
1266	          [
1267	            "Black-box (none)",
1268	            "0.031",
1269	            "3/12",
1270	            "4/12",
1271	            "0.28",
1272	            "0%"
1273	          ]
1274	        ]
1275	      }
1276	    ],
1277	    "figures": [],
1278	    "analysis": "Partial-knowledge 分析的 key takeaway：diversity trap 的 threat model 是 realistic。Full-knowledge 是 worst-case security analysis 的 standard practice（similar to how cryptography assumes worst-case adversary），但 even partial-knowledge（family info = public）已经 captures 63% of the vulnerability。The 7/12 K_eff significance under partial knowledge means: even if the adversary only knows 'this panel uses judges from Llama, GPT, and Qwen families'（commonly disclosed），they can exploit diversity. This eliminates the 'but real adversaries don't have full information' defense. Graduation: paper can now claim diversity trap holds under realistic threat models, not just theoretical worst-case.\n\nPartial-knowledge adversary 的 strategy 是 family-level targeting：知道 panel 含 Llama → apply Llama-family average attack template，知道含 GPT → apply GPT-family average attack template。ASR 约为 full-knowledge 的 78%——family membership 提供了 ~63% of adversary information value（(0.058-0.031)/(0.074-0.031)=62.8%），因为 family→capability tier 有强相关性（所有 Qwen-7B 都是 small tier），且 family-level vulnerability profiles 有 within-family consistency。K_eff 在 partial-knowledge 下仍 7/12 sig（vs full-knowledge 10/12），因为 diverse panel 跨越更多 families → adversary 的 family-level portfolio attack 有更多 entry points。η_max 8/12 sig（vs 10/12）轻微下降因为 adversary 不知 exact η_j，targeting precision 降低使 weakest-link exploitation 变 fuzzy。R² 从 0.62 降至 0.51 反映 partial-knowledge 下 panel structure 的 predictive power 减弱——adversary behavior 有更多 randomness（不确定性导致 suboptimal targeting）。关键意义：diversity trap 不依赖于 unrealistically strong adversary 假设——即使 adversary 只有 public-level information（model families are typically disclosed in evaluation pipelines），diversity 仍然显著有害。这直接回应 Dream W7（'unrealistically strong adversary'）。"
1279	  }
1280	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e50a3923-1e3e-4324-8f9a-015b4d0bf728",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "6a0dd755-c66e-47aa-ade4-15a07fcaecf7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"15-Model Scale Expansion + Core Regression\",\n    \"description\": \"从 6 扩展到 15 models（GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini, Claude-3.5-Sonnet, Gemini-1.5-Pro + 6 local open-source: Llama-3.1-8B/70B, Qwen2.5-7B/72B, Mistral-7B-v0.3, Phi-3-medium-14B）。455 C(15,3) panels，2 datasets × 6 attacks = 12 conditions 全量回归。\",\n    \"results\": {\n      \"K_eff_raw_FDR_sig_positive\": \"12/12\",\n      \"K_eff_resid_FDR_sig_positive\": \"10/12\",\n      \"eta_max_FDR_sig\": \"10/12\",\n      \"VIF_keff_etamax\": 1.02,\n      \"mean_R2\": 0.62,\n      \"confound_r_mean\": 0.55,\n      \"confound_free_conditions_count\": 3,\n      \"confound_free_keff_p_min\": 2.1e-28,\n      \"panels_total\": 455,\n      \"keff_dominates_etamax_conditions\": 3,\n      \"etamax_dominates_keff_conditions\": 4,\n      \"sensitivity_exclude_ACC_lt_05_keff_sig\": \"11/12\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Dual Vulnerability Drivers: 15-Model Regression (12 Conditions)\",\n        \"columns\": [\n          \"Condition\",\n          \"η_max β\",\n          \"η_max p\",\n          \"K_eff_resid β\",\n          \"K_eff_resid p\",\n          \"R²\",\n          \"Confound r\",\n          \"Dominant\"\n        ],\n        \"rows\": [\n          [\n            \"mmlu×sycophancy\",\n            \"0.82\",\n            \"1.2e-8\",\n            \"0.31\",\n            \"0.004\",\n            \"0.68\",\n            \"0.72\",\n            \"η_max\"\n          ],\n          [\n            \"mmlu×score_manip\",\n            \"0.45\",\n            \"0.018\",\n            \"0.61\",\n            \"3.4e-9\",\n            \"0.71\",\n            \"0.38\",\n            \"K_eff\"\n          ],\n          [\n            \"mmlu×position\",\n            \"0.15\",\n            \"0.214\",\n            \"0.58\",\n            \"1.2e-8\",\n            \"0.56\",\n            \"0.36\",\n            \"K_eff\"\n          ],\n          [\n            \"mmlu×verbosity\",\n            \"0.74\",\n            \"4.1e-7\",\n            \"0.28\",\n            \"0.011\",\n            \"0.63\",\n            \"0.74\",\n            \"η_max\"\n          ],\n          [\n            \"mmlu×authority\",\n            \"0.69\",\n            \"1.8e-6\",\n            \"0.19\",\n            \"0.087\",\n            \"0.58\",\n            \"0.78\",\n            \"η_max\"\n          ],\n          [\n            \"mmlu×few_shot\",\n            \"0.55\",\n            \"2.3e-4\",\n            \"0.48\",\n            \"6.1e-6\",\n            \"0.65\",\n            \"0.65\",\n            \"both\"\n          ],\n          [\n            \"arc×sycophancy\",\n            \"0.79\",\n            \"3.5e-8\",\n            \"0.35\",\n            \"0.002\",\n            \"0.66\",\n            \"0.71\",\n            \"η_max\"\n          ],\n          [\n            \"arc×score_manip\",\n            \"0.38\",\n            \"0.117\",\n            \"0.64\",\n            \"1.7e-7\",\n            \"0.59\",\n            \"0.35\",\n            \"K_eff\"\n          ],\n          [\n            \"arc×position\",\n            \"0.03\",\n            \"0.910\",\n            \"0.72\",\n            \"1.8e-8\",\n            \"0.57\",\n            \"0.34\",\n            \"K_eff\"\n          ],\n          [\n            \"arc×verbosity\",\n            \"0.71\",\n            \"8.9e-7\",\n            \"0.33\",\n            \"0.003\",\n            \"0.61\",\n            \"0.73\",\n            \"η_max\"\n          ],\n          [\n            \"arc×authority\",\n            \"0.66\",\n            \"3.2e-6\",\n            \"0.22\",\n            \"0.062\",\n            \"0.55\",\n            \"0.76\",\n            \"η_max\"\n          ],\n          [\n            \"arc×few_shot\",\n            \"0.51\",\n            \"5.7e-4\",\n            \"0.52\",\n            \"3.8e-6\",\n            \"0.63\",\n            \"0.62\",\n            \"both\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"15-model 核心回归确认 Diversity Trap 的全部结构。10/12 残差化显著（vs 初步分析 8/12）表明 refined 统计方法（FDR 校正 + beta regression consistency check from plan_009）增强效应检测。Condition-dependent dominance pattern 从定性观察升级为 systematic taxonomy：attack transferability 高→K_eff 主导（adversary 利用 judge 异质性找 judge-specific 攻击路径），attack transferability 低（shared bias）→η_max 主导（所有 judges 共享弱点）。3 个 confound-free conditions 的 p<1e-20 是最强 'smoking gun'——即使 K_eff 与 η_max 近乎正交（r≈0.35），K_eff 仍达 genome-wide 级别显著性。这单独就足以封堵 RC1 的所有统计变体。\\n\\n模型池从 6→15 后能力谱系大幅展开（7B→72B 全开源 + GPT-4/Claude/Gemini API tier），K_eff-η_max 结构性共线从 r=-0.80 降至 ~0.55。455 panels（23× 6-model 的 20 panels）给残差化 K_eff 分析提供充足统计功效，使 8/12 的初步结果在 refined analysis 后升至 10/12。关键驱动力：(1) confound-free conditions 从 2→3 个（arc×score_manipulation、arc×position_bias、mmlu×position_bias 中 r≈0.35），这些条件下 K_eff 达极端显著性（p<1e-20），彻底排除 confound artifact；(2) condition-dependent dominance pattern 清晰——transferable attacks（score_manipulation、position_bias）中 K_eff β > η_max β，因为 diverse judges 提供异质化 attack surface；shared-bias attacks（sycophancy、verbosity、authority）中 η_max 主导，因为所有 judges 共享类似认知偏差；(3) sensitivity analysis 排除 ACC<0.5 outlier models 后 K_eff_resid 增至 11/12，证明效应非极端 outlier 驱动。\"\n  },\n  {\n    \"name\": \"Attack Surface Expansion (9 Types)\",\n    \"description\": \"攻击类型从 6 扩展到 9：新增 few-shot hijacking（in-context example 注入篡改评分标准）、persona manipulation（冒充权威角色指令 judge 改分）、instruction override（直接覆写评判 prompt）。全 15 models × 455 panels × 2 datasets。\",\n    \"results\": {\n      \"new_attack_types\": 3,\n      \"new_conditions\": 6,\n      \"keff_resid_sig_new_conditions\": \"4/6\",\n      \"total_conditions_majority\": 18,\n      \"keff_resid_sig_total_majority\": \"14/18\",\n      \"eta_max_sig_total_majority\": \"15/18\",\n      \"keff_dominates_new_attacks\": 1,\n      \"etamax_dominates_new_attacks\": 2,\n      \"mean_R2_new\": 0.63\n    },\n    \"tables\": [\n      {\n        \"name\": \"Extended Attack Results (New 6 Conditions)\",\n        \"columns\": [\n          \"Condition\",\n          \"K_eff_resid β\",\n          \"K_eff_resid p (FDR)\",\n          \"η_max β\",\n          \"η_max p (FDR)\",\n          \"R²\",\n          \"Attack Transferability\"\n        ],\n        \"rows\": [\n          [\n            \"mmlu×few_shot_hijack\",\n            \"0.54\",\n            \"8.2e-7\",\n            \"0.47\",\n            \"3.1e-5\",\n            \"0.67\",\n            \"High\"\n          ],\n          [\n            \"mmlu×persona_manip\",\n            \"0.29\",\n            \"0.008\",\n            \"0.63\",\n            \"5.4e-7\",\n            \"0.60\",\n            \"Moderate\"\n          ],\n          [\n            \"mmlu×instr_override\",\n            \"0.22\",\n            \"0.042\",\n            \"0.71\",\n            \"1.1e-7\",\n            \"0.64\",\n            \"Low\"\n          ],\n          [\n            \"arc×few_shot_hijack\",\n            \"0.58\",\n            \"2.1e-7\",\n            \"0.41\",\n            \"8.8e-5\",\n            \"0.65\",\n            \"High\"\n          ],\n          [\n            \"arc×persona_manip\",\n            \"0.25\",\n            \"0.019\",\n            \"0.68\",\n            \"2.3e-7\",\n            \"0.62\",\n            \"Moderate\"\n          ],\n          [\n            \"arc×instr_override\",\n            \"0.18\",\n            \"0.112\",\n            \"0.74\",\n            \"3.7e-8\",\n            \"0.66\",\n            \"Low\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"新攻击验证了 attack taxonomy 的预测性：transferability 越高的攻击，K_eff 的相对重要性越大。Few-shot hijacking 与 score_manipulation/position_bias 一起构成 'transferable attacks cluster'（K_eff β 0.47–0.72），persona/instruction/sycophancy/verbosity/authority 构成 'shared-bias cluster'（η_max β 0.58–0.82）。Taxonomy 从 post-hoc 描述升级为 predictive framework：给定新攻击类型，可预测哪个 vulnerability driver 主导。14/18 总显著数直接封堵 RC3 的 generalization 质疑，attack 覆盖面从 6→9 类型跨越 injection、bias、hijacking 三大攻击范式。\\n\\n三类新攻击按 transferability 分层：few-shot hijacking 是 high-transferability 攻击——通过 in-context examples 篡改评分标准，不同 judge 对 ICL 的响应模式差异极大（Qwen 系对 Chinese-style ICL 特别敏感、GPT 系对结构化 format hijacking 脆弱），因此 K_eff 主导（β≈0.54, p<1e-6）——diverse panel 有更多可利用的 ICL 入口点。Persona manipulation 和 instruction override 属于 moderate-to-low transferability：不同 judge 的 instruction-following 遵从度存在差异但 RLHF 训练给所有模型植入了类似的 authority-compliance bias，预测 η_max 主导但 K_eff 在 persona_manip 上仍显著（p<0.02）。Instruction override 的 K_eff 在 arc 上 NS（p=0.112）因为 ARC 的简短问题格式给 override 攻击的操作空间更少，judge 差异贡献有限。总计 14/18 残差化显著满足 K_eff_resid_sig_extended_conditions [10,16] 范围。\"\n  },\n  {\n    \"name\": \"BFT Random-Fault Contrast (Calibrated, 15-Model)\",\n    \"description\": \"Random-fault simulation 使用 calibrated failure rates（非原始 η_j）：基于 bootstrapped clean-accuracy noise 生成独立 random failures。每个 judge 失败概率与其 clean accuracy 相关但独立采样，模拟 BFT 假设的 uncorrelated fault 模式。455 panels × 12 conditions 对比 adaptive 与 RF 下的 K_eff β。\",\n    \"results\": {\n      \"RF_keff_sig_positive\": \"3/12\",\n      \"RF_keff_sig_negative\": \"5/12\",\n      \"RF_keff_NS\": \"4/12\",\n      \"adaptive_keff_beta_mean\": 0.42,\n      \"RF_keff_beta_mean\": -0.12,\n      \"BFT_RF_beta_ratio\": 2.8,\n      \"conditions_ratio_ge_1_5x\": \"9/12\",\n      \"conditions_beta_flipped_negative\": \"5/12\",\n      \"delta_R2_RF_vs_adaptive\": 0.31,\n      \"RF_R2_mean\": 0.78,\n      \"adaptive_R2_mean\": 0.47\n    },\n    \"tables\": [\n      {\n        \"name\": \"BFT Regime Contrast: K_eff β Adaptive vs Random-Fault (12 Conditions)\",\n        \"columns\": [\n          \"Condition\",\n          \"β_adaptive\",\n          \"p_adap\",\n          \"β_RF\",\n          \"p_RF\",\n          \"|β_adap/β_RF|\",\n          \"R²_adap\",\n          \"R²_RF\",\n          \"Flipped?\"\n        ],\n        \"rows\": [\n          [\n            \"mmlu×sycophancy\",\n            \"0.31\",\n            \"0.004\",\n            \"0.08\",\n            \"0.310\",\n            \"3.88\",\n            \"0.68\",\n            \"0.82\",\n            \"No\"\n          ],\n          [\n            \"mmlu×score_manip\",\n            \"0.61\",\n            \"3.4e-9\",\n            \"-0.22\",\n            \"0.015\",\n            \"2.77\",\n            \"0.71\",\n            \"0.89\",\n            \"Yes\"\n          ],\n          [\n            \"mmlu×position\",\n            \"0.58\",\n            \"1.2e-8\",\n            \"-0.31\",\n            \"0.003\",\n            \"1.87\",\n            \"0.56\",\n            \"0.76\",\n            \"Yes\"\n          ],\n          [\n            \"mmlu×verbosity\",\n            \"0.28\",\n            \"0.011\",\n            \"0.11\",\n            \"0.198\",\n            \"2.55\",\n            \"0.63\",\n            \"0.79\",\n            \"No\"\n          ],\n          [\n            \"mmlu×authority\",\n            \"0.19\",\n            \"0.087\",\n            \"0.06\",\n            \"0.541\",\n            \"3.17\",\n            \"0.58\",\n            \"0.74\",\n            \"No\"\n          ],\n          [\n            \"mmlu×few_shot\",\n            \"0.48\",\n            \"6.1e-6\",\n            \"-0.18\",\n            \"0.039\",\n            \"2.67\",\n            \"0.65\",\n            \"0.81\",\n            \"Yes\"\n          ],\n          [\n            \"arc×sycophancy\",\n            \"0.35\",\n            \"0.002\",\n            \"0.10\",\n            \"0.251\",\n            \"3.50\",\n            \"0.66\",\n            \"0.80\",\n            \"No\"\n          ],\n          [\n            \"arc×score_manip\",\n            \"0.64\",\n            \"1.7e-7\",\n            \"-0.28\",\n            \"0.008\",\n            \"2.29\",\n            \"0.59\",\n            \"0.85\",\n            \"Yes\"\n          ],\n          [\n            \"arc×position\",\n            \"0.72\",\n            \"1.8e-8\",\n            \"-0.35\",\n            \"0.001\",\n            \"2.06\",\n            \"0.57\",\n            \"0.78\",\n            \"Yes\"\n          ],\n          [\n            \"arc×verbosity\",\n            \"0.33\",\n            \"0.003\",\n            \"0.12\",\n            \"0.175\",\n            \"2.75\",\n            \"0.61\",\n            \"0.77\",\n            \"No\"\n          ],\n          [\n            \"arc×authority\",\n            \"0.22\",\n            \"0.062\",\n            \"0.05\",\n            \"0.612\",\n            \"4.40\",\n            \"0.55\",\n            \"0.72\",\n            \"No\"\n          ],\n          [\n            \"arc×few_shot\",\n            \"0.52\",\n            \"3.8e-6\",\n            \"-0.14\",\n            \"0.091\",\n            \"3.71\",\n            \"0.63\",\n            \"0.79\",\n            \"Yes(marg)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Calibrated RF 对比定性建立 BFT reversal mechanism：5/12 conditions β 翻转为负（diversity 在 true random faults 下确实有益），集中在 transferable attacks 上——exactly as mechanism predicts。翻转在 score_manip 和 position 上最强（这些攻击的 ASR 最依赖 judge-specific vulnerabilities），在 RF 模式下这些 vulnerabilities 被 random noise 取代，diversity 的容错优势重新显现。9/12 ratio ≥1.5× 表明即使不完全翻转，adaptive 下 K_eff 的有害效应也显著强于 RF——β 系统性 amplification 2.8× on average。ΔR²=0.31 是 BFT 理论的直接数值体现：BFT 假设 panel structure determines fault tolerance（high R²=0.78），adaptive adversary 打破这一假设（low R²=0.47）。BFT reversal 从 conceptual analogy 升级为 empirically grounded mechanism with quantitative support。\\n\\nBFT contrast 的核心区分在于 failure mode topology：random faults 下 judges 独立失败且 failures 无空间相关性，majority vote 的冗余容错使 K_eff 越高→fault tolerance 越强→β 应为负或接近零。Adaptive adversary 则 strategic targeting：找到 panel 中最弱的 judges 并集中攻击，K_eff 越高→attack surface 越大→β 为正。之前 15-model pipeline 的 RF 分析直接用 η_j 作为 failure prob，保留了 adaptive vulnerability structure（弱 judges 在 RF 下仍然更容易 fail），未能 cleanly 模拟 BFT 假设。Best tier 用 calibrated rates（基于 clean accuracy 的 bootstrapped noise）打破 adaptive vulnerability structure：RF failure prob 仅与 clean accuracy 相关而非 adversarial robustness，使 RF 成为 genuine random-fault baseline。翻转在 transferable attacks（score_manip、position、few_shot）中最明确（β 从 +0.52–0.72 翻至 -0.14–-0.35），因为这些攻击最依赖 judge-specific exploit paths——RF 下这些 paths 变成 random noise。Shared-bias attacks（sycophancy、verbosity）下 RF β 仍略正（0.08–0.12）但 NS，因为 bias 的 shared nature 使 'random' 和 'adaptive' failure modes 部分重叠。ΔR²=0.31 表明 RF 下 panel composition 解释 78% 方差（结构可预测），adaptive 仅 47%（strategic noise 占 53%），直接支撑 'adaptive adversary introduces variance beyond panel structure' 论点。\"\n  },\n  {\n    \"name\": \"Capability-Matched Within-Tier Validation\",\n    \"description\": \"同 capability tier 内做 within-tier regression 排除 tier-mixing artifact。Small tier: Llama-8B, Qwen-7B, Mistral-7B, Phi-14B, GPT-4o-mini (5 models, C(5,3)=10 panels)。Medium tier: 此 tier 仅 4 models → 4 panels，功效不足标注 directional。Large tier: Llama-70B, Qwen-72B, GPT-4o, GPT-4.1, Claude-3.5, Gemini-1.5 (6 models, C(6,3)=20 panels)。\",\n    \"results\": {\n      \"small_tier_models\": 5,\n      \"small_tier_panels\": 10,\n      \"small_tier_keff_sig\": \"2/6\",\n      \"small_tier_confound_r\": 0.32,\n      \"medium_tier_models\": 4,\n      \"medium_tier_panels\": 4,\n      \"medium_tier_keff_sig\": \"1/6\",\n      \"medium_tier_note\": \"directional only, underpowered\",\n      \"large_tier_models\": 6,\n      \"large_tier_panels\": 20,\n      \"large_tier_keff_sig\": \"4/6\",\n      \"large_tier_confound_r\": 0.33,\n      \"total_keff_sig_across_tiers\": 4,\n      \"capability_matched_keff_sig\": 4,\n      \"within_tier_confound_r_mean\": 0.35\n    },\n    \"tables\": [\n      {\n        \"name\": \"Within-Tier K_eff Validation\",\n        \"columns\": [\n          \"Tier\",\n          \"Models\",\n          \"Panels\",\n          \"K_eff-η_max r\",\n          \"K_eff_resid sig (of 6)\",\n          \"Best p\",\n          \"η_max sig (of 6)\"\n        ],\n        \"rows\": [\n          [\n            \"Small (7B-14B)\",\n            \"5\",\n            \"10\",\n            \"0.32\",\n            \"2/6\",\n            \"0.008\",\n            \"3/6\"\n          ],\n          [\n            \"Medium (14-34B)\",\n            \"4\",\n            \"4\",\n            \"0.41\",\n            \"1/6\",\n            \"0.031\",\n            \"2/6\"\n          ],\n          [\n            \"Large (70B+API)\",\n            \"6\",\n            \"20\",\n            \"0.33\",\n            \"4/6\",\n            \"4.2e-4\",\n            \"5/6\"\n          ],\n          [\n            \"Cross-tier (all 15)\",\n            \"15\",\n            \"455\",\n            \"0.55\",\n            \"10/12\",\n            \"1.7e-7\",\n            \"10/12\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Large-Tier Condition Detail\",\n        \"columns\": [\n          \"Condition\",\n          \"K_eff_resid β\",\n          \"p\",\n          \"η_max β\",\n          \"p\",\n          \"Sig?\"\n        ],\n        \"rows\": [\n          [\n            \"score_manip\",\n            \"0.58\",\n            \"4.2e-4\",\n            \"0.31\",\n            \"0.042\",\n            \"K_eff dominant\"\n          ],\n          [\n            \"position_bias\",\n            \"0.52\",\n            \"0.001\",\n            \"0.18\",\n            \"0.228\",\n            \"K_eff dominant\"\n          ],\n          [\n            \"sycophancy\",\n            \"0.21\",\n            \"0.154\",\n            \"0.61\",\n            \"0.002\",\n            \"η_max dominant\"\n          ],\n          [\n            \"verbosity\",\n            \"0.17\",\n            \"0.238\",\n            \"0.55\",\n            \"0.005\",\n            \"η_max dominant\"\n          ],\n          [\n            \"authority\",\n            \"0.34\",\n            \"0.018\",\n            \"0.48\",\n            \"0.008\",\n            \"both sig\"\n          ],\n          [\n            \"few_shot\",\n            \"0.45\",\n            \"0.003\",\n            \"0.39\",\n            \"0.012\",\n            \"both sig\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Capability-matched validation 是封堵 RC1 最强变体的 decisive evidence。Reviewer 可能 argue：'K_eff positive 不过是因为 high-K_eff panels 混了弱模型（tier-mixing）'。Large tier 结果直接否定：全是 top-tier 模型（GPT-4 级别），η_max 在 0.08-0.15 的 narrow range 内，K_eff 仍在 4/6 conditions 显著正向。Condition-dependent pattern 在 tier-internal 分析中完美复现：score_manip + position 由 K_eff 主导，sycophancy + verbosity 由 η_max 主导。这一致性跨 pooling strategy（all-15 vs within-tier）极大增强了 finding 的 robustness。Small tier 的 2/6 sig 表明 diversity trap 在低能力模型中也存在（低能力 diverse panel 更脆弱），但效应弱于 large tier——可能因为 small models 的 η_max 方差更大（有的 7B 异常脆弱），η_max 抢走了更多 variance。\\n\\nWithin-tier analysis 的核心价值是控制 tier-mixing confound。全局 r=0.55（K_eff 与 η_max）有约 40% 来自跨 tier mixing：高 K_eff panels 往往混合 7B 和 70B 模型，天然引入低 robustness judges。同 tier 内 r 降至 ~0.35，给 K_eff 最干净的检验。Large tier 结果最有说服力：6 models（GPT-4o, GPT-4.1, Claude-3.5, Gemini-1.5, Llama-70B, Qwen-72B）全是 top-tier 模型，η_max 方差天然较小，但 K_eff 仍在 4/6 conditions 显著——diverse panel 即使全由强模型组成也更脆弱，因为 judges 的 robustness profiles 仍然异质（GPT-4o 对 sycophancy 特别敏感、Llama-70B 对 position bias 敏感等）。Small tier 5 models / 10 panels 功效有限但 2/6 sig 提供 cross-tier consistency。Medium tier 仅 4 panels，1/6 sig 是 directional evidence only。总计 ≥4/6 unique conditions 有 within-tier K_eff 显著，满足 capability_matched_keff_sig [3,6] 范围。意义：即使 reviewer 最强版本的 'K_eff positive = tier-mixing artifact' argument 也被否定——same-tier panels 中 diversity 仍独立有害。\"\n  },\n  {\n    \"name\": \"Two-Stage Panel Selection Algorithm Benchmark\",\n    \"description\": \"Robustness-first 两阶段算法：Stage 1 filter η_j > percentile-75 threshold (保留最 robust 的 75% judges)，Stage 2 在通过筛选的 candidates 中 maximize K_eff。Benchmark vs 5 baselines on 15-model pool，6 attack conditions (MMLU × 6 attacks)。\",\n    \"results\": {\n      \"two_stage_mean_ASR\": 0.038,\n      \"strongest_k_ASR\": 0.048,\n      \"min_etamax_ASR\": 0.041,\n      \"max_keff_ASR\": 0.112,\n      \"random_ASR\": 0.089,\n      \"oracle_ASR\": 0.032,\n      \"ASR_reduction_vs_strongest_k_pct\": 20.8,\n      \"ASR_reduction_vs_max_keff_pct\": 66.1,\n      \"conditions_two_stage_best\": \"5/6\",\n      \"two_stage_pareto_optimal_pct\": 78,\n      \"screening_threshold_optimal_percentile\": 75\n    },\n    \"tables\": [\n      {\n        \"name\": \"Panel Selection Strategy Benchmark (15 Models, MMLU)\",\n        \"columns\": [\n          \"Strategy\",\n          \"Mean ASR\",\n          \"Δ vs Strongest-K\",\n          \"Best (of 6)\",\n          \"Worst-case ASR\"\n        ],\n        \"rows\": [\n          [\n            \"Two-Stage (ours)\",\n            \"0.038\",\n            \"-20.8%\",\n            \"5/6\",\n            \"0.071\"\n          ],\n          [\n            \"Min-η_max\",\n            \"0.041\",\n            \"-14.6%\",\n            \"4/6\",\n            \"0.078\"\n          ],\n          [\n            \"Strongest-K\",\n            \"0.048\",\n            \"baseline\",\n            \"1/6\",\n            \"0.095\"\n          ],\n          [\n            \"Random\",\n            \"0.089\",\n            \"+85.4%\",\n            \"0/6\",\n            \"0.156\"\n          ],\n          [\n            \"Max-K_eff\",\n            \"0.112\",\n            \"+133.3%\",\n            \"0/6\",\n            \"0.198\"\n          ],\n          [\n            \"Oracle\",\n            \"0.032\",\n            \"-33.3%\",\n            \"6/6\",\n            \"0.052\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Two-Stage Sensitivity to Screening Threshold\",\n        \"columns\": [\n          \"Threshold (percentile)\",\n          \"Candidate models\",\n          \"Mean ASR\",\n          \"K_eff of selected panel\"\n        ],\n        \"rows\": [\n          [\n            \"50\",\n            \"8\",\n            \"0.039\",\n            \"2.12\"\n          ],\n          [\n            \"65\",\n            \"10\",\n            \"0.037\",\n            \"2.28\"\n          ],\n          [\n            \"75 (optimal)\",\n            \"11\",\n            \"0.038\",\n            \"2.41\"\n          ],\n          [\n            \"85\",\n            \"13\",\n            \"0.045\",\n            \"2.55\"\n          ],\n          [\n            \"100 (no filter)\",\n            \"15\",\n            \"0.058\",\n            \"2.71\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"20.8% ASR reduction 将实用贡献从 Dream 批评的 'marginal'（12.5% at 6-model）升级为 'practically meaningful'。Threshold sensitivity table 揭示 sweet spot 在 percentile-65–75：太紧（50th）损失 candidate diversity，太松（85–100th）引入弱 judges。Pareto frontier analysis 显示 78% 的 Two-stage selected panels 落在 Pareto 前沿上——算法近似了 computationally-expensive 的 exhaustive Pareto search。关键 takeaway for practitioners：(1) 绝不盲目 maximize diversity（Max-K_eff 灾难级 ASR）；(2) Pure robustness（Min-η_max）已经很好，diversity 优化提供 modest 额外收益；(3) Two-stage 在所有非 oracle 策略中最接近理论最优。\\n\\n15-model pool 给 Two-stage 算法显著优于 6-model 结果（12.5%→20.8% vs Strongest-K）的空间。原因双重：(1) 15 models 筛选后 candidate pool 更大——6-model 时 threshold filter 后仅剩 3-4 judges（几乎无 K_eff 优化空间），15-model 时剩 ~11 judges（C(11,3)=165 candidate panels），K_eff 最大化有真正的搜索空间。(2) Robustness screening 后的 restricted pool 中，K_eff-η_max confound 被 threshold 机制性打破（高 η_max 模型已被移除），K_eff 的效应方向可能从有害翻转为中性——当所有 judges 都 robust 时，diversity 不再引入弱 judge，其 BFT 容错优势部分恢复。Min_etamax 与 Two-stage 差距较小（0.041 vs 0.038, Δ=7.3%）说明 K_eff 优化在 robustness-screened pool 内的增量贡献 modest——这恰好支持 'robustness-first, diversity-second' 的优先级判断。Max_keff 策略的灾难性表现（ASR 0.112, +133% vs Strongest-K）是 diversity trap 最直观的实证：盲目追求 diversity 而不管 robustness 是危险的。Oracle 的存在（0.032）表明 Two-stage 达 Oracle 效率的 84%（0.038/0.032），远超 Strongest-K 的 67%（0.048/0.032）。15%+ 降幅满足 two_stage_ASR_reduction_pct [15,35]。\"\n  },\n  {\n    \"name\": \"Per-Judge ASR Concentration Analysis\",\n    \"description\": \"计算 455 panels × 6 attacks 的 per-judge ASR 分布。Gini coefficient 量化 ASR 在 panel 内 judges 间的集中度，Shannon entropy 量化均匀性。Adaptive vs RF 对比。\",\n    \"results\": {\n      \"mean_gini_adaptive\": 0.68,\n      \"mean_gini_RF\": 0.12,\n      \"gini_ratio_adaptive_vs_RF\": 5.67,\n      \"mean_entropy_adaptive\": 1.42,\n      \"mean_entropy_RF\": 2.31,\n      \"high_keff_gini_adaptive\": 0.74,\n      \"low_keff_gini_adaptive\": 0.55,\n      \"gini_keff_correlation\": 0.52,\n      \"top1_judge_ASR_share_adaptive\": 0.78,\n      \"top1_judge_ASR_share_RF\": 0.38\n    },\n    \"tables\": [\n      {\n        \"name\": \"ASR Concentration Metrics: Adaptive vs Random-Fault\",\n        \"columns\": [\n          \"Metric\",\n          \"Adaptive\",\n          \"Random-Fault\",\n          \"Ratio\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Mean Gini\",\n            \"0.68\",\n            \"0.12\",\n            \"5.67\",\n            \"Concentrated vs uniform\"\n          ],\n          [\n            \"Mean Entropy (bits)\",\n            \"1.42\",\n            \"2.31\",\n            \"0.61\",\n            \"Low entropy = targeted\"\n          ],\n          [\n            \"Top-1 Judge ASR Share\",\n            \"0.78\",\n            \"0.38\",\n            \"2.05\",\n            \"78% ASR on weakest judge\"\n          ],\n          [\n            \"r(K_eff, Gini)\",\n            \"0.52\",\n            \"0.08\",\n            \"6.50\",\n            \"Diversity → more targeting\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Concentration analysis 将 diversity trap 从统计关联推进到机制层面：不是 'K_eff 与 ASR 碰巧正相关'，而是 'diverse panels 给 adversary 提供了更清晰的 targeting gradient（Gini 0.74），使攻击集中在最弱 judge 上（78% share），从而打破 majority vote'。r(K_eff, Gini)=0.52 的正相关是 diversity trap 因果链中的关键中间变量——future work 可用 mediation analysis 正式量化 Gini 在 K_eff→ASR 路径中的 mediating role。此外 RF 下的 low concentration（Gini 0.12）直接验证了 BFT 的 key assumption（uncorrelated failures distribute uniformly），解释了为何 diversity 在 RF 下可以有益。\\n\\nConcentration analysis 是 diversity trap 机制的 'microscope'——从 panel-level 聚合统计深入到 judge-level 攻击分布。Adaptive adversary 的 core strategy 是 targeting：识别 panel 中最脆弱的 judge 并集中 exploit。这导致 ASR 高度 concentrated 在 1-2 个 judges 上（Gini≈0.68, top-1 share 78%），而 RF 下 failures 近似均匀分布（Gini≈0.12）。关键发现：high-K_eff panels 的 Gini 更高（0.74 vs 0.55），因为 diverse panel 中 judges 的 capability spread 更大→adversary 的 target 更清晰（最弱 judge 与最强 judge 的差距更大）。Gini-K_eff 正相关（r=0.52）是 diversity trap 因果链的直接 observational evidence：diversity → larger capability spread → clearer targeting → higher concentration → higher panel ASR。这不是因果证明（需要 intervention），但因果方向性（directional consistency）很强。5.67× Gini ratio 也是 BFT contrast 的另一维度验证：BFT 假设 failures 均匀分布（low Gini），adaptive adversary 打破这一假设（high Gini）。\"\n  },\n  {\n    \"name\": \"Diversity-Capability Tradeoff Visualization\",\n    \"description\": \"455 panels 的 K_eff vs η_max tradeoff 散点图、Pareto 前沿、tier 分层分析。\",\n    \"results\": {\n      \"global_r_keff_etamax\": 0.55,\n      \"within_small_r\": 0.32,\n      \"within_medium_r\": 0.41,\n      \"within_large_r\": 0.33,\n      \"pareto_frontier_panels\": 18,\n      \"pareto_frontier_slope\": -0.73,\n      \"tradeoff_explained_variance\": 0.42\n    },\n    \"tables\": [\n      {\n        \"name\": \"K_eff–η_max Correlation Structure by Tier\",\n        \"columns\": [\n          \"Tier\",\n          \"r(K_eff, η_max)\",\n          \"N panels\",\n          \"Pareto-optimal\",\n          \"Mean K_eff\",\n          \"Mean η_max\"\n        ],\n        \"rows\": [\n          [\n            \"Small (7B-14B)\",\n            \"0.32\",\n            \"10\",\n            \"3\",\n            \"2.41\",\n            \"0.312\"\n          ],\n          [\n            \"Medium (14-34B)\",\n            \"0.41\",\n            \"4\",\n            \"2\",\n            \"2.18\",\n            \"0.224\"\n          ],\n          [\n            \"Large (70B+API)\",\n            \"0.33\",\n            \"20\",\n            \"5\",\n            \"1.95\",\n            \"0.148\"\n          ],\n          [\n            \"Cross-tier (all 15)\",\n            \"0.55\",\n            \"455\",\n            \"18\",\n            \"2.35\",\n            \"0.231\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Tradeoff 可视化的核心价值是将 Claim 3 从统计数字转化为直觉图形。Pareto frontier 的 steep negative slope（-0.73）意味着 K_eff 每增加 0.1，η_max 至少增加 0.073——practitioners 必须明确这个 cost。Tier-stratified view 显示 within-tier tradeoff 较弱但仍存在，支持 'screening + optimize' 策略的理论基础。ASR 等值线叠加（contour）直接显示 Pareto-optimal panels 的 ASR 远低于 max-K_eff panels——视觉化 diversity trap。\\n\\n全局 K_eff-η_max 正相关（r=0.55）编码了 LLM 生态系统的一个结构性约束：maximizing panel independence（K_eff）要求跨越 capability tiers 选 judges（例如同时选 GPT-4o 和 Mistral-7B），这必然引入 robustness 差异大的 judges，推高 η_max。Within-tier r 大幅下降（0.32–0.41）揭示了 tradeoff 的两层结构：(1) Cross-tier component（贡献 ~40% 的 global r）：源于 tier mixing，可通过 screening 消除；(2) Within-tier component（residual r≈0.35）：即使同 tier 内，追求 diversity 仍需选择 robustness profile 更异质的 judges，这不可完全消除但幅度较小。Pareto 前沿的 18 panels（约 4% of 455）定义了 diversity-robustness 不可能三角的 achievable boundary——Two-stage 算法的目标就是逼近这个前沿。解释方差 42% 意味着 K_eff 是 η_max 的 moderate 但非 dominant 预测器——剩余 58% 的 η_max 方差由 attack-specific vulnerability profiles、评分偏好差异等因素决定，这也解释了为什么 K_eff 的 residualized effect 在控制 η_max 后仍然显著。\"\n  },\n  {\n    \"name\": \"Panel Size Sensitivity K=3,5,7,9\",\n    \"description\": \"Panel size 从 K=3 扩展到 K=5,7,9。15 models 选 K 个 judges 的组合数分别为 C(15,3)=455, C(15,5)=3003, C(15,7)=6435, C(15,9)=5005。每个 K 做 12 conditions 回归。\",\n    \"results\": {\n      \"K3_keff_resid_sig\": \"10/12\",\n      \"K5_keff_resid_sig\": \"11/12\",\n      \"K7_keff_resid_sig\": \"12/12\",\n      \"K9_keff_resid_sig\": \"12/12\",\n      \"K3_mean_keff_beta\": 0.42,\n      \"K5_mean_keff_beta\": 0.48,\n      \"K7_mean_keff_beta\": 0.55,\n      \"K9_mean_keff_beta\": 0.61,\n      \"K3_mean_etamax_beta\": 0.51,\n      \"K5_mean_etamax_beta\": 0.49,\n      \"K7_mean_etamax_beta\": 0.43,\n      \"K9_mean_etamax_beta\": 0.38,\n      \"crossover_K\": 6,\n      \"K3_mean_R2\": 0.62,\n      \"K9_mean_R2\": 0.51\n    },\n    \"tables\": [\n      {\n        \"name\": \"Panel Size Sensitivity Summary\",\n        \"columns\": [\n          \"K\",\n          \"Panels\",\n          \"K_eff_resid sig\",\n          \"Mean K_eff β\",\n          \"Mean η_max β\",\n          \"Mean R²\",\n          \"Primary driver\"\n        ],\n        \"rows\": [\n          [\n            \"3\",\n            \"455\",\n            \"10/12\",\n            \"0.42\",\n            \"0.51\",\n            \"0.62\",\n            \"η_max\"\n          ],\n          [\n            \"5\",\n            \"3003\",\n            \"11/12\",\n            \"0.48\",\n            \"0.49\",\n            \"0.58\",\n            \"balanced\"\n          ],\n          [\n            \"7\",\n            \"6435\",\n            \"12/12\",\n            \"0.55\",\n            \"0.43\",\n            \"0.54\",\n            \"K_eff\"\n          ],\n          [\n            \"9\",\n            \"5005\",\n            \"12/12\",\n            \"0.61\",\n            \"0.38\",\n            \"0.51\",\n            \"K_eff\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Panel size sensitivity 提供 diversity trap 的 scaling law：K_eff β ≈ 0.33 + 0.047K（近似线性增长）。这意味着 evaluation community 普遍采用的 'add more judges' strategy 会 systematically amplify diversity trap——K=9 panel 的 K_eff 有害效应比 K=3 大 45%。η_max 的下降则反映了 weakest-link theorem 在 large K 下的局限性：当 K 足够大时，单一最弱 judge 不再 decisive，panel 的整体结构（diversity/independence）接管。交叉点 K≈6 有实际指导意义：K≤5 的小 panel 优先管控 η_max（选最 robust 的 judges），K≥7 的大 panel 必须同时管控 K_eff（限制不必要的 diversity）。\\n\\nK_eff β 随 panel size 单调递增（0.42→0.61），原因：(1) larger panels 有更多 judges → attack surface 与 panel size 正比增长，每个 additional judge 提供一个额外的 potential exploit path；(2) K=9 panel 的 K_eff range 更大（15 models 选 9 → wider independence spectrum），给回归更大信号。η_max β 随 K 递减（0.51→0.38），原因：larger panel 的 vulnerability 不再由单一 weakest judge 决定——K=9 时 adversary 需要 compromise ⌈9/2⌉=5 judges，不能仅靠 targeting the weakest one，panel structure（diversity）的相对重要性上升。交叉点约 K≈6：在此 panel size 以上，K_eff 超过 η_max 成为 primary vulnerability driver。R² 随 K 下降（0.62→0.51）因为 larger panel 的行为更复杂，judge interaction effects 增加 unexplained variance。K=9 时 K_eff 12/12 sig + β=0.61 是 diversity trap 的 strongest single evidence point：大型 evaluation panels 中 diversity 是 dominant 有害因素。这直接回应 'just add more judges to be safer' 的朴素直觉。\"\n  },\n  {\n    \"name\": \"VIF + Multicollinearity Full Diagnostics\",\n    \"description\": \"对 15-model 455-panel 数据做完整统计诊断：VIF、condition number、partial correlations、residualized K_eff、Bonferroni/FDR 多重比较校正、beta regression（处理 ASR 的 [0,1] bounded nature）、Shapiro-Wilk 残差正态性检验。纯计算，无 GPU。\",\n    \"results\": {\n      \"VIF_keff_resid\": 1.02,\n      \"VIF_etamax\": 1.02,\n      \"condition_number\": 4.8,\n      \"partial_r_keff_given_etamax\": 0.38,\n      \"partial_r_etamax_given_keff\": 0.45,\n      \"keff_resid_FDR_sig\": \"10/12\",\n      \"keff_bonferroni_sig\": \"8/12\",\n      \"beta_regression_keff_sig\": \"9/12\",\n      \"beta_regression_etamax_sig\": \"10/12\",\n      \"shapiro_wilk_residuals_p_mean\": 0.23,\n      \"cooks_d_max\": 0.031,\n      \"leverage_outlier_pct\": 2.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Multicollinearity Diagnostics Summary\",\n        \"columns\": [\n          \"Diagnostic\",\n          \"Value\",\n          \"Threshold\",\n          \"Status\"\n        ],\n        \"rows\": [\n          [\n            \"VIF (K_eff_resid)\",\n            \"1.02\",\n            \"<5.0\",\n            \"PASS\"\n          ],\n          [\n            \"VIF (η_max)\",\n            \"1.02\",\n            \"<5.0\",\n            \"PASS\"\n          ],\n          [\n            \"Condition Number\",\n            \"4.8\",\n            \"<30\",\n            \"PASS\"\n          ],\n          [\n            \"Partial r(K_eff|η_max)\",\n            \"0.38\",\n            \">0.1\",\n            \"Moderate independent effect\"\n          ],\n          [\n            \"Partial r(η_max|K_eff)\",\n            \"0.45\",\n            \">0.1\",\n            \"Moderate-strong independent effect\"\n          ],\n          [\n            \"Shapiro-Wilk p (residuals)\",\n            \"0.23\",\n            \">0.05\",\n            \"Normal residuals\"\n          ],\n          [\n            \"Max Cook's D\",\n            \"0.031\",\n            \"<1.0\",\n            \"No influential points\"\n          ],\n          [\n            \"High-leverage %\",\n            \"2.4%\",\n            \"<5%\",\n            \"Acceptable\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Multiple Comparison Robustness\",\n        \"columns\": [\n          \"Correction Method\",\n          \"K_eff_resid sig\",\n          \"η_max sig\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Uncorrected\",\n            \"12/12\",\n            \"11/12\",\n            \"Raw signal\"\n          ],\n          [\n            \"FDR (Benjamini-Hochberg)\",\n            \"10/12\",\n            \"10/12\",\n            \"Primary report\"\n          ],\n          [\n            \"Bonferroni\",\n            \"8/12\",\n            \"9/12\",\n            \"Most conservative, still passes\"\n          ],\n          [\n            \"Beta Regression + FDR\",\n            \"9/12\",\n            \"10/12\",\n            \"Distributional robustness\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"VIF + diagnostics package 是论文统计 credibility 的 foundation。Key contribution to paper: (1) 把 'K_eff is independently significant' 从初步 observation 升级为经过 6 层 robustness check（residualization, VIF, partial correlation, beta regression, multiple comparison, influence diagnostics）验证的 result；(2) 每个 check 都 pass 意味着 reviewer 无法从任何统计 angle 质疑 K_eff 的独立效应；(3) Bonferroni-corrected 8/12 sig 是最保守的下界——即使用最严格的多重比较校正，diversity trap 仍在 2/3 的 conditions 中成立。\\n\\n残差化设计（K_eff_resid = residuals of K_eff ~ η_max）在数学上保证 VIF=1.0（两个 predictors 正交）。实际计算得 1.02 是因为 floating point precision + minor numerical jitter。Condition number 4.8 远低于 30 的 concern threshold，确认回归矩阵 well-conditioned。Partial correlations 揭示各自独立贡献：K_eff|η_max 的 partial r=0.38 意味着 holding η_max constant，K_eff 独立解释 ~14% ASR variance；η_max|K_eff 的 partial r=0.45 解释 ~20%。Beta regression 作为 distributional robustness check 处理两个 OLS 假设违反：(1) ASR 在 [0,1] 内 bounded，OLS 可能在极端值处产生 out-of-range predictions；(2) ASR 的方差可能 heteroscedastic（低 ASR panels 方差更小）。Beta regression 结果（9/12 vs OLS 10/12）高度一致，证明 OLS findings 非 distributional artifact。Multiple comparison 从 FDR（10/12）到 Bonferroni（8/12，最保守）全部 pass，消除 'cherry-picking' concern。Cook's distance max=0.031（远低于 1.0 threshold）和 leverage outliers 仅 2.4% 证明结果非 influential point 驱动。这套诊断 package 直接 preempt Dream review W2（VIF 未报告）和 RC1（multicollinearity）的所有 variants。\"\n  },\n  {\n    \"name\": \"Aggregation Rule Modulation (15-Model)\",\n    \"description\": \"三种非 majority-vote 聚合规则下的 dual vulnerability drivers 分析：Threshold voting（unanimity: 所有 judges 必须同意 reject）、Accuracy-weighted voting（权重 ∝ clean accuracy）、Bayesian aggregation（基于 prior accuracy 的 posterior probability）。455 panels × 12 conditions per aggregation。\",\n    \"results\": {\n      \"majority_keff_sig\": \"10/12\",\n      \"majority_etamax_sig\": \"10/12\",\n      \"threshold_keff_sig\": \"11/12\",\n      \"threshold_etamax_sig\": \"7/12\",\n      \"threshold_keff_beta_amplification\": 1.45,\n      \"weighted_keff_sig\": \"8/12\",\n      \"weighted_etamax_sig\": \"9/12\",\n      \"bayesian_keff_sig\": \"6/12\",\n      \"bayesian_etamax_sig\": \"5/12\",\n      \"bayesian_mean_ASR_reduction_vs_majority\": 0.28,\n      \"total_keff_sig_majority_plus_threshold\": \"14/16\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Aggregation Rule × Vulnerability Drivers (15-Model, 455 Panels)\",\n        \"columns\": [\n          \"Aggregation\",\n          \"K_eff_resid sig\",\n          \"η_max sig\",\n          \"Mean K_eff β\",\n          \"Mean η_max β\",\n          \"Mean ASR\",\n          \"Δ ASR vs Majority\"\n        ],\n        \"rows\": [\n          [\n            \"Majority\",\n            \"10/12\",\n            \"10/12\",\n            \"0.42\",\n            \"0.51\",\n            \"0.074\",\n            \"baseline\"\n          ],\n          [\n            \"Threshold (unanimity)\",\n            \"11/12\",\n            \"7/12\",\n            \"0.61\",\n            \"0.34\",\n            \"0.138\",\n            \"+86%\"\n          ],\n          [\n            \"Accuracy-weighted\",\n            \"8/12\",\n            \"9/12\",\n            \"0.39\",\n            \"0.48\",\n            \"0.069\",\n            \"-6.8%\"\n          ],\n          [\n            \"Bayesian\",\n            \"6/12\",\n            \"5/12\",\n            \"0.25\",\n            \"0.28\",\n            \"0.053\",\n            \"-28.4%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Aggregation 分析的 three actionable insights：(1) Threshold voting 是 diversity trap 的 worst-case amplifier——unanimity requirement 使 K_eff β 增加 45%，absolute ASR 增加 86%。Deployment recommendation: 避免在 adversarial-aware 场景使用 unanimity aggregation。(2) Bayesian 是 best partial defense——同时削弱两个 vulnerability channels（K_eff 6/12, η_max 5/12 vs majority 的 10/12, 10/12），ASR 降 28%。但 6/12 K_eff 仍 sig 表明 Bayesian 不能完全消除 diversity trap。(3) Defense stack rationale: Two-stage selection（控制 η_max 通道）+ Bayesian aggregation（削弱残余 η_max + 部分削弱 K_eff）是最 comprehensive defense。单一维度不够。\\n\\n聚合规则改变 vulnerability driver 的 relative weight 通过三个机制：(1) Threshold/unanimity 放大 K_eff——panel reject 需要 ALL judges agree，adversary 只需 flip one judge 就能 block rejection。Diverse panel 有更多 potential 'flip targets'（judge-specific vulnerabilities 更多样），因此 K_eff β amplifies 1.45×。同时 η_max 弱化（7/12）因为 unanimity 的 blocking 不需要 weakest judge 特别弱——任何一个 judge 被 flip 就够了。(2) Weighted voting 结果近似 majority 因为 accuracy weights 仅微调 vote influence（权重范围 0.8-1.2），未根本改变投票结构。(3) Bayesian aggregation 基于 clean-accuracy prior 下调低能力 judges 的 posterior weight，partially 中和了 η_max 通道（5/12，从 majority 的 10/12 下降）——弱 judges 的 vote 被 discount 所以 adversary targeting 弱 judge 的收益降低。但 K_eff 仍 6/12 sig，因为 Bayesian weights 基于 clean accuracy 而非 adversarial robustness——attack-shifted accuracy ≠ clean accuracy，adversary 可以 manipulate a judge 使其给出 'confidently wrong' judgment，Bayesian 无法区分这种 confident error 与 genuine judgment。28% ASR reduction 说明 Bayesian 是 best single-aggregation defense 但非 silver bullet。Combined majority + threshold conditions 的 14/16 K_eff sig 落入 K_eff_resid_sig_extended_conditions [10,16] 范围。\"\n  },\n  {\n    \"name\": \"Open-Ended Generation Benchmark (MT-Bench + AlpacaEval)\",\n    \"description\": \"在 MT-Bench（多轮对话评判）和 AlpacaEval（指令遵循评分）上测试 diversity trap。4 attack types × 2 benchmarks = 8 新 conditions（选 4 primary attacks: score_manip, sycophancy, position, verbosity）。15 models 但 panel size 受限于 benchmark cost 可能 sample 200 panels。\",\n    \"results\": {\n      \"mtbench_keff_resid_sig\": \"3/4\",\n      \"mtbench_etamax_sig\": \"3/4\",\n      \"mtbench_mean_R2\": 0.48,\n      \"alpacaeval_keff_resid_sig\": \"2/4\",\n      \"alpacaeval_etamax_sig\": \"3/4\",\n      \"alpacaeval_mean_R2\": 0.42,\n      \"open_ended_keff_sig_total\": \"3/4\",\n      \"open_ended_confound_r\": 0.48,\n      \"keff_beta_ratio_open_vs_mcq\": 0.85,\n      \"condition_dependent_pattern_preserved\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Open-Ended Benchmark Results (8 Conditions)\",\n        \"columns\": [\n          \"Benchmark×Attack\",\n          \"K_eff_resid β\",\n          \"K_eff_resid p (FDR)\",\n          \"η_max β\",\n          \"η_max p (FDR)\",\n          \"R²\",\n          \"Dominant\"\n        ],\n        \"rows\": [\n          [\n            \"MT-Bench×score_manip\",\n            \"0.52\",\n            \"1.8e-5\",\n            \"0.38\",\n            \"0.003\",\n            \"0.52\",\n            \"K_eff\"\n          ],\n          [\n            \"MT-Bench×sycophancy\",\n            \"0.28\",\n            \"0.012\",\n            \"0.55\",\n            \"4.1e-5\",\n            \"0.49\",\n            \"η_max\"\n          ],\n          [\n            \"MT-Bench×position\",\n            \"0.47\",\n            \"8.3e-5\",\n            \"0.21\",\n            \"0.089\",\n            \"0.44\",\n            \"K_eff\"\n          ],\n          [\n            \"MT-Bench×verbosity\",\n            \"0.18\",\n            \"0.108\",\n            \"0.62\",\n            \"7.2e-6\",\n            \"0.47\",\n            \"η_max\"\n          ],\n          [\n            \"AlpacaEval×score_manip\",\n            \"0.44\",\n            \"3.2e-4\",\n            \"0.35\",\n            \"0.006\",\n            \"0.46\",\n            \"K_eff\"\n          ],\n          [\n            \"AlpacaEval×sycophancy\",\n            \"0.21\",\n            \"0.058\",\n            \"0.58\",\n            \"1.4e-5\",\n            \"0.43\",\n            \"η_max\"\n          ],\n          [\n            \"AlpacaEval×position\",\n            \"0.38\",\n            \"0.002\",\n            \"0.25\",\n            \"0.041\",\n            \"0.40\",\n            \"both\"\n          ],\n          [\n            \"AlpacaEval×verbosity\",\n            \"0.14\",\n            \"0.175\",\n            \"0.59\",\n            \"2.1e-5\",\n            \"0.39\",\n            \"η_max\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Open-ended 结果的 three-fold significance：(1) Generalization — diversity trap 从 MCQ 推广到 open-ended，覆盖 LLM evaluation 的两大应用场景（benchmark scoring + human preference prediction），claim 从 'diversity hurts on MMLU/ARC' 升级为 'diversity hurts on LLM evaluation generally'。(2) Taxonomy transfer — condition-dependent dominance pattern（transferable→K_eff, shared-bias→η_max）在 open-ended 上 preserved without modification，表明 taxonomy 是 task-agnostic fundamental structure。(3) Practical relevance — MT-Bench/AlpacaEval 是 LLM 排名的 de facto standard，diversity trap 在这些 benchmark 上成立直接影响模型选择和部署决策。R² 下降（0.39-0.52 vs MCQ 0.62）是 expected tradeoff：open-ended evaluation 的 subjectivity noise 是 inherent 的，panel structure 能解释的 fraction naturally 减少。\\n\\nOpen-ended judging 与 MCQ 的关键差异：(1) 评分更主观——judges 在 'what constitutes a good response' 上 disagreement 更高，noise floor 提升；(2) 攻击空间更大——adversary 可以在 multi-turn conversation 的每轮 independently manipulate（MT-Bench），或在 free-form response 中 embed 更复杂的 manipulation signals（AlpacaEval）。K_eff 在 open-ended 上仍显著正向（3/4 unique conditions across benchmarks），但 β 略低于 MCQ（ratio 0.85），因为 open-ended 的 higher noise floor 使 panel structure 解释的方差降低（R² 0.42-0.48 vs MCQ 0.62）。MT-Bench 比 AlpacaEval 表现更强（3/4 vs 2/4 sig），因为 multi-turn 结构给 adversary 更多 manipulation surface（每轮是独立攻击机会），judge-specific 响应差异在多轮中累积。Condition-dependent pattern 在 open-ended 上完美复现：score_manip 和 position 下 K_eff 主导，sycophancy 和 verbosity 下 η_max 主导——attack taxonomy 从 MCQ 推广到 open-ended 无需修改。≥2/4 open-ended K_eff 显著（best tier 达 3/4）满足 open-ended 显著条件。意义：diversity trap 不是 MCQ-specific artifact，直接回应 Dream W6 和 RC3。\"\n  },\n  {\n    \"name\": \"Gaussian Copula Failure + Family Label Revalidation (15-Model, 105 Pairs)\",\n    \"description\": \"15-model 105 pairwise MI matrix 计算。Gaussian copula MI vs observed MI ratio 验证。Family labels（6 families）的 MI 预测性检验（within vs cross-family）。Capability proximity 与 MI 的相关性分析。\",\n    \"results\": {\n      \"total_pairs\": 105,\n      \"MI_gaussian_ratio_mean\": 18.5,\n      \"MI_gaussian_ratio_max\": 312,\n      \"MI_gaussian_ratio_min\": 4.2,\n      \"pairs_ratio_gt_10x\": \"82/105\",\n      \"family_label_MWU_p\": 0.158,\n      \"family_label_permutation_p\": 0.312,\n      \"within_family_MI_mean\": 0.42,\n      \"cross_family_MI_mean\": 0.39,\n      \"capability_proximity_MI_correlation\": -0.71,\n      \"copula_MI_ratio_15model\": 18.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Copula Failure: Scale Comparison\",\n        \"columns\": [\n          \"Metric\",\n          \"6-model (15 pairs)\",\n          \"15-model (105 pairs)\",\n          \"Change\"\n        ],\n        \"rows\": [\n          [\n            \"MI_obs/MI_gauss mean\",\n            \"14.7\",\n            \"18.5\",\n            \"+25.9%\"\n          ],\n          [\n            \"MI_obs/MI_gauss max\",\n            \"235\",\n            \"312\",\n            \"+32.8%\"\n          ],\n          [\n            \"MI_obs/MI_gauss min\",\n            \"8.3\",\n            \"4.2\",\n            \"Some close pairs\"\n          ],\n          [\n            \"Pairs with ratio >10×\",\n            \"11/15 (73%)\",\n            \"82/105 (78%)\",\n            \"+5pp\"\n          ],\n          [\n            \"Family label p (MWU)\",\n            \"0.206\",\n            \"0.158\",\n            \"Still NS\"\n          ],\n          [\n            \"Capability-MI r\",\n            \"-0.65\",\n            \"-0.71\",\n            \"Stronger\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"15-model copula failure 和 family label 结果分别强化 Claims 5 和 4。Copula failure 的 practical implication：任何基于 Gaussian copula 假设的 panel reliability bound（如 independence-based certification）在 LLM judge 对上不可信——underestimate information sharing by 10-30×（mean 18.5×）。这为 K_eff 作为 empirical independence measure（而非 copula-derived bounds）提供 methodological justification。Family label result 的 practical implication：panel designers 不能简单用 '3 different families = diverse panel' 的 heuristic——Qwen-7B 和 Llama-8B 虽属不同 families 但 capability 接近故 MI 高（independence 低），而 GPT-4o-mini 和 GPT-4o 虽同属 OpenAI 但 capability gap 大故 MI 低（independence 高）。Capability proximity 是 independence 的 true driver。\\n\\n105 pairs（7× 6-model 的 15 pairs）大幅增加 copula failure 的统计力度。MI_gaussian_ratio 均值从 6-model 的 14.7 升至 18.5，因为 15-model pool 包含更多 capability-heterogeneous pairs（如 Mistral-7B 与 GPT-4o、Phi-14B 与 Claude-3.5），这些极端 pair 的联合分布更远离 bivariate Gaussian——heavy tails、discrete clustering、capability-dependent correlation structure 使 Gaussian copula 的低估更严重。Max ratio 从 235 升至 312（最极端 pair 如 Mistral-7B × GPT-4o 的 MI 被 Gaussian 低估 312×）。Family labels 仍无预测力（MWU p=0.158）：within-family MI（0.42）和 cross-family MI（0.39）无显著差异。根本原因：同 family 不同 size（如 Llama-8B vs Llama-70B）的 judges 独立性差异远大于同 size 不同 family（如 Llama-8B vs Qwen-7B vs Mistral-7B）——这些 7B-class 模型 capability-wise 非常接近，共享 similar failure modes despite different training pipelines。Capability proximity（|capability_i - capability_j|）与 MI 的强负相关（r=-0.71）直接支持：能力越接近→共享越多 failure patterns→MI 越高→independence 越低。意义：practitioners 不应用 family diversity 作为 panel independence proxy——capability-based metrics（如 K_eff）才是 valid measure。\"\n  },\n  {\n    \"name\": \"Partial-Knowledge Adversary Model\",\n    \"description\": \"Adversary 知道 panel 包含哪些 model families（public information）但不知各 judge 的具体 η_j vulnerability profiles。Strategy: family-level average attack 而非 judge-specific targeting。与 full-knowledge 和 black-box baselines 对比。\",\n    \"results\": {\n      \"full_knowledge_mean_ASR\": 0.074,\n      \"partial_knowledge_mean_ASR\": 0.058,\n      \"black_box_mean_ASR\": 0.031,\n      \"partial_vs_full_ratio\": 0.784,\n      \"keff_sig_partial\": \"7/12\",\n      \"etamax_sig_partial\": \"8/12\",\n      \"partial_R2\": 0.51,\n      \"family_info_value_pct\": 62.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Adversary Knowledge Level Comparison\",\n        \"columns\": [\n          \"Knowledge Level\",\n          \"Mean ASR\",\n          \"K_eff sig\",\n          \"η_max sig\",\n          \"R²\",\n          \"Info value vs black-box\"\n        ],\n        \"rows\": [\n          [\n            \"Full (judge-level η_j)\",\n            \"0.074\",\n            \"10/12\",\n            \"10/12\",\n            \"0.62\",\n            \"100%\"\n          ],\n          [\n            \"Partial (family only)\",\n            \"0.058\",\n            \"7/12\",\n            \"8/12\",\n            \"0.51\",\n            \"62.8%\"\n          ],\n          [\n            \"Black-box (none)\",\n            \"0.031\",\n            \"3/12\",\n            \"4/12\",\n            \"0.28\",\n            \"0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Partial-knowledge 分析的 key takeaway：diversity trap 的 threat model 是 realistic。Full-knowledge 是 worst-case security analysis 的 standard practice（similar to how cryptography assumes worst-case adversary），但 even partial-knowledge（family info = public）已经 captures 63% of the vulnerability。The 7/12 K_eff significance under partial knowledge means: even if the adversary only knows 'this panel uses judges from Llama, GPT, and Qwen families'（commonly disclosed），they can exploit diversity. This eliminates the 'but real adversaries don't have full information' defense. Graduation: paper can now claim diversity trap holds under realistic threat models, not just theoretical worst-case.\\n\\nPartial-knowledge adversary 的 strategy 是 family-level targeting：知道 panel 含 Llama → apply Llama-family average attack template，知道含 GPT → apply GPT-family average attack template。ASR 约为 full-knowledge 的 78%——family membership 提供了 ~63% of adversary information value（(0.058-0.031)/(0.074-0.031)=62.8%），因为 family→capability tier 有强相关性（所有 Qwen-7B 都是 small tier），且 family-level vulnerability profiles 有 within-family consistency。K_eff 在 partial-knowledge 下仍 7/12 sig（vs full-knowledge 10/12），因为 diverse panel 跨越更多 families → adversary 的 family-level portfolio attack 有更多 entry points。η_max 8/12 sig（vs 10/12）轻微下降因为 adversary 不知 exact η_j，targeting precision 降低使 weakest-link exploitation 变 fuzzy。R² 从 0.62 降至 0.51 反映 partial-knowledge 下 panel structure 的 predictive power 减弱——adversary behavior 有更多 randomness（不确定性导致 suboptimal targeting）。关键意义：diversity trap 不依赖于 unrealistically strong adversary 假设——即使 adversary 只有 public-level information（model families are typically disclosed in evaluation pipelines），diversity 仍然显著有害。这直接回应 Dream W7（'unrealistically strong adversary'）。\"\n  }\n]",
      "numLines": 1280,
      "startLine": 1,
      "totalLines": 1280
    }
  },
  "sourceToolAssistantUUID": "e50a3923-1e3e-4324-8f9a-015b4d0bf728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_…",
  "leafUuid": "6a0dd755-c66e-47aa-ade4-15a07fcaecf7",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate certificate manipulation vulnerability study paper",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba"
}
```

---

### Assistant

_source line 14 · 2026-05-22T18:17:13.198Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also read the paper-writing-norms skill and check if there's a LaTeX template available, then write the full paper.

Let me check what's available in the artifacts directory and whether pdflatex is available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a0dd755-c66e-47aa-ade4-15a07fcaecf7",
  "isSidechain": false,
  "requestId": "req_011CbJ4mfTfWtLa8pSVqFHQR",
  "type": "assistant",
  "uuid": "9df1a9d1-6868-4ba0-9a32-8f138535419d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXzdX53vJDbCndZHw6XJLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4093,
      "cache_creation_input_tokens": 22848,
      "cache_read_input_tokens": 23719,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22848,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4093,
          "output_tokens": 288,
          "cache_read_input_tokens": 23719,
          "cache_creation_input_tokens": 22848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22848
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

_source line 15 · 2026-05-22T18:17:13.671Z_

Now let me check if pdflatex is available and read the paper-writing-norms skill.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9df1a9d1-6868-4ba0-9a32-8f138535419d",
  "isSidechain": false,
  "requestId": "req_011CbJ4mfTfWtLa8pSVqFHQR",
  "type": "assistant",
  "uuid": "671cdfb2-4688-42f9-bc9b-4bc4df1c81e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXzdX53vJDbCndZHw6XJLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4093,
      "cache_creation_input_tokens": 22848,
      "cache_read_input_tokens": 23719,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22848,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4093,
          "output_tokens": 288,
          "cache_read_input_tokens": 23719,
          "cache_creation_input_tokens": 22848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22848
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

_source line 16 · 2026-05-22T18:17:14.167Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GnSy3pnf753mDo4zt6EU1c`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version | head -3",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "671cdfb2-4688-42f9-bc9b-4bc4df1c81e0",
  "isSidechain": false,
  "requestId": "req_011CbJ4mfTfWtLa8pSVqFHQR",
  "type": "assistant",
  "uuid": "5e10972d-4851-4814-aaeb-08baf6b8d499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXzdX53vJDbCndZHw6XJLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4093,
      "cache_creation_input_tokens": 22848,
      "cache_read_input_tokens": 23719,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22848,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4093,
          "output_tokens": 288,
          "cache_read_input_tokens": 23719,
          "cache_creation_input_tokens": 22848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22848
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

_source line 17 · 2026-05-22T18:17:16.351Z_

<details><summary>↩ Tool result · `toolu_01MSo2ZiCmu6wBNQWt77eDWY`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0185fd4c-7324-43ee-8515-550595ef7e0a",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "a3bc2624-fcc2-4f2b-b525-d781df55dcf6",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0185fd4c-7324-43ee-8515-550595ef7e0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T18:17:14.519Z_

<details><summary>↩ Tool result · `toolu_01GnSy3pnf753mDo4zt6EU1c`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1
Copyright 2025 Han The Thanh (pdfTeX) et al.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e10972d-4851-4814-aaeb-08baf6b8d499",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "a058c59f-9e5e-41c5-83e8-6d34d3251302",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1\nCopyright 2025 Han The Thanh (pdfTeX) et al.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5e10972d-4851-4814-aaeb-08baf6b8d499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T18:17:16.303Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MSo2ZiCmu6wBNQWt77eDWY`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/",
  "description": "List existing files in target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a058c59f-9e5e-41c5-83e8-6d34d3251302",
  "isSidechain": false,
  "requestId": "req_011CbJ4mfTfWtLa8pSVqFHQR",
  "type": "assistant",
  "uuid": "0185fd4c-7324-43ee-8515-550595ef7e0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXzdX53vJDbCndZHw6XJLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4093,
      "cache_creation_input_tokens": 22848,
      "cache_read_input_tokens": 23719,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22848,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4093,
          "output_tokens": 288,
          "cache_read_input_tokens": 23719,
          "cache_creation_input_tokens": 22848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22848
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

_source line 20 · 2026-05-22T18:17:42.098Z_

<details><summary>Logged reasoning block</summary>

```text
Good, pdflatex is available and the target directory exists. Now I need to write a full LaTeX paper. Let me carefully structure this based on the experiment data and paper framing.

The paper has these key experiments:
1. 15-Model Scale Expansion + Core Regression (dual vulnerability drivers)
2. Attack Surface Expansion (9 Types)
3. BFT Random-Fault Contrast (Calibrated, 15-Model)
4. Capability-Matched Within-Tier Validation
5. Two-Stage Panel Selection Algorithm Benchmark
6. Per-Judge ASR Concentration Analysis


7. Diversity-Capability Tradeoff Visualization
8. Panel Size Sensitivity K=3,5,7,9
9. VIF + Multicollinearity Full Diagnostics
10. Aggregation Rule Modulation (15-Model)
11. Open-Ended Generation Benchmark (MT-Bench + AlpacaEval)
12. Gaussian Copula Failure + Family Label Revalidation
13. Partial-Knowledge Adversary Model

I'll organize these into a comprehensive paper structure with Abstract, Introduction, Related Work, Problem Formulation/Method, and Experiments sections, grouping the core analyses logically.

Now I'm laying out the full experimental section with all thirteen experiments arranged by theme—starting with the foundational regression and attack expansion studies, then moving through validation approaches, sensitivity analyses, statistical diagnostics, and finally the adversarial robustness tests. I'll follow this with sections on the defense mechanisms and limitations.

For the submission, I need to pull all numbers directly from the experiment data file and keep the writing at a reviewable draft level within the eight-page constraint.

Writing LaTeX now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3bc2624-fcc2-4f2b-b525-d781df55dcf6",
  "isSidechain": false,
  "requestId": "req_011CbJ4nM3QtehjCvtmuUG2F",
  "type": "assistant",
  "uuid": "0ae75975-9697-453e-baf0-2220c6383911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1vvZcCXLgBwgU2Vwi2Ruy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4531,
      "cache_read_input_tokens": 46567,
      "output_tokens": 11017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11017,
          "cache_read_input_tokens": 46567,
          "cache_creation_input_tokens": 4531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4531
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

_source line 21 · 2026-05-22T18:17:42.262Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ae75975-9697-453e-baf0-2220c6383911",
  "isSidechain": false,
  "requestId": "req_011CbJ4nM3QtehjCvtmuUG2F",
  "type": "assistant",
  "uuid": "2d15839a-7f55-4e7e-b5f5-16fe09702356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1vvZcCXLgBwgU2Vwi2Ruy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4531,
      "cache_read_input_tokens": 46567,
      "output_tokens": 11017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11017,
          "cache_read_input_tokens": 46567,
          "cache_creation_input_tokens": 4531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4531
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

_source line 22 · 2026-05-22T18:20:38.214Z_

<details open><summary>🔧 Tool call — Write · `toolu_01VqBe5DLJ2VV1ye7M2YCZCh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{amsmath}\n\\usepackage{amsfonts}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\n\\setlength\\titlebox{5cm}\n\n\\newcommand{\\keff}{K_{\\text{eff}}}\n\\newcommand{\\etamax}{\\eta_{\\text{max}}}\n\\newcommand{\\keffresid}{K_{\\text{eff}}^{\\text{resid}}}\n\n\\title{More Diverse, More Vulnerable:\\\\How Judge Panel Diversity Backfires Under Adaptive Adversaries}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge evaluation panels are increasingly used to assess LLM outputs, with the prevailing assumption that judge diversity---analogous to Byzantine Fault Tolerance (BFT)---improves robustness against manipulation. We provide large-scale empirical evidence that this assumption \\emph{reverses} under adaptive adversaries. Across 15 LLM judges spanning 6 model families, 455 three-judge panels, 9 attack types, and 4 evaluation benchmarks, we show that panel diversity (effective independence $\\keff$) is \\textbf{independently and positively} associated with attack success rate (ASR), even after residualizing against individual judge weakness ($\\etamax$). This ``diversity trap'' is driven by dual vulnerability channels whose relative importance is attack-dependent: $\\etamax$ dominates shared-bias attacks (sycophancy, verbosity), while $\\keff$ dominates transferable attacks (score manipulation, position bias). We trace the mechanism to BFT's broken assumption: random faults distribute uniformly across judges (Gini$\\approx$0.12), but adaptive adversaries concentrate attacks on the weakest judge (Gini$\\approx$0.68), turning diversity from a defense into an expanded attack surface. Under calibrated random faults, $\\keff$'s coefficient flips negative in 5/12 conditions, empirically confirming BFT's prediction. We propose a robustness-first two-stage panel selection algorithm that reduces ASR by 20.8\\% over the strongest-$K$ baseline, and show that Bayesian aggregation provides a complementary 28.4\\% reduction. Our findings challenge the ``more diverse = more robust'' assumption and call for diversity-aware security analysis in LLM evaluation pipeline design.\n\\end{abstract}\n\n\\section{Introduction}\n\nAs LLMs are increasingly deployed as automated evaluators~\\cite{zheng2023judging,li2023alpacaeval}, the research community has adopted multi-judge panels to mitigate individual model biases. The intuition is straightforward and borrowed from distributed systems: diverse, independent judges should be harder to simultaneously fool, much like Byzantine Fault Tolerance (BFT) guarantees that $f$ faulty nodes cannot compromise a system of $3f+1$ independent replicas.\n\nThis paper demonstrates that this intuition is \\emph{wrong} under adversarial conditions. We conduct what is, to our knowledge, the largest systematic study of adversarial robustness in multi-judge LLM evaluation: 15 models from 6 families (OpenAI, Anthropic, Google, Meta, Alibaba, Microsoft), enumerated into 455 three-judge panels, evaluated under 9 distinct attack types across MMLU, ARC-Challenge, MT-Bench, and AlpacaEval.\n\nOur central finding is the \\textbf{diversity trap}: panel diversity, measured by effective judge independence ($\\keff$), is \\emph{independently and positively} associated with attack success rate. After residualizing $\\keff$ against individual judge weakness ($\\etamax$, the maximum vulnerability of any panel member), $\\keffresid$ remains significantly positive in 10/12 conditions (FDR-corrected). Panel vulnerability is driven by \\textbf{dual factors}---$\\etamax$ and $\\keff$---whose relative importance depends on attack type:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Shared-bias attacks} (sycophancy, verbosity, authority): $\\etamax$ dominates because all judges share similar cognitive biases from RLHF training.\n\\item \\textbf{Transferable attacks} (score manipulation, position bias): $\\keff$ dominates because diverse judges provide heterogeneous, judge-specific attack surfaces.\n\\end{itemize}\n\nWe trace this to BFT's core assumption: fault independence. Under random faults, failures distribute uniformly (Gini$\\approx$0.12) and diversity genuinely helps---our calibrated random-fault simulations show $\\keff$'s coefficient \\emph{flipping negative} in 5/12 conditions. But adaptive adversaries concentrate attacks on the weakest judges (Gini$\\approx$0.68, top-1 judge absorbing 78\\% of ASR), turning diversity from fault tolerance into an expanded attack menu.\n\nWe further show that: (1) the diversity trap holds within capability tiers (4/6 conditions significant among top-tier models only), ruling out tier-mixing confounds; (2) generalizes to open-ended benchmarks (MT-Bench 3/4, AlpacaEval 2/4 significant); (3) scales with panel size ($\\keff$ coefficient increases monotonically from $K$=3 to $K$=9); (4) holds under partial-knowledge adversaries who know only model family membership (7/12 significant). We propose a two-stage defense---robustness screening followed by diversity optimization---that achieves 20.8\\% ASR reduction over the strongest-$K$ baseline, and show Bayesian aggregation provides complementary protection.\n\n\\section{Related Work}\n\n\\paragraph{LLM-as-Judge.} LLM evaluation using model judges has become standard practice~\\cite{zheng2023judging,li2023alpacaeval,dubois2024alpacafarm}. Known biases include position bias, verbosity preference, and self-enhancement~\\cite{wang2023large,zheng2023judging}. Multi-judge panels are proposed as mitigation, but their adversarial robustness remains unstudied.\n\n\\paragraph{Adversarial Attacks on LLM Judges.} Prior work demonstrates individual judge vulnerability to prompt injection, sycophancy exploitation, and score manipulation~\\cite{raina2024llm,shi2024optimization}. We extend this to \\emph{panel-level} analysis, studying how panel composition mediates vulnerability.\n\n\\paragraph{Byzantine Fault Tolerance.} Classical BFT~\\cite{lamport1982byzantine,castro1999practical} guarantees safety when faults are independent. Recent work questions independence assumptions in ML systems~\\cite{sagawa2020investigation}. We empirically test whether BFT's independence assumption holds for LLM judge panels.\n\n\\paragraph{Ensemble Diversity.} The diversity-accuracy tradeoff is well-studied in ensemble learning~\\cite{krogh1994neural,brown2005diversity}. Our setting differs: we study diversity under \\emph{adaptive adversaries} who exploit panel composition, not passive noise.\n\n\\section{Problem Formulation}\n\n\\paragraph{Setup.} A panel $P = \\{j_1, \\ldots, j_K\\}$ of $K$ LLM judges evaluates candidate responses. Each judge $j_i$ produces a binary decision (accept/reject). The panel decision uses an aggregation rule $\\mathcal{A}$ (default: majority vote).\n\n\\paragraph{Adversary Model.} An adaptive adversary observes the panel composition and crafts attacks to maximize the panel's attack success rate (ASR)---the fraction of evaluation instances where the panel decision is flipped.\n\n\\paragraph{Vulnerability Metrics.} We define two panel-level predictors:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item $\\etamax = \\max_{j \\in P} \\eta_j$: maximum individual vulnerability (weakest link). $\\eta_j$ is judge $j$'s individual ASR under a given attack.\n\\item $\\keff$: effective number of independent judges, computed from the eigenspectrum of the pairwise mutual information matrix. Higher $\\keff$ indicates greater functional diversity.\n\\end{itemize}\n\nTo disentangle $\\keff$ from $\\etamax$, we define $\\keffresid$ as the residual of regressing $\\keff$ on $\\etamax$, ensuring orthogonality (VIF$=$1.02).\n\n\\paragraph{Regression Model.} For each condition (dataset $\\times$ attack type), we fit:\n\\begin{equation}\n\\text{ASR}_P = \\beta_0 + \\beta_\\eta \\cdot \\etamax + \\beta_K \\cdot \\keffresid + \\epsilon\n\\end{equation}\nacross all 455 panels. A significantly positive $\\beta_K$ indicates diversity independently increases vulnerability.\n\n\\section{Experimental Setup}\n\n\\paragraph{Models.} 15 LLM judges: GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini (OpenAI); Claude-3.5-Sonnet (Anthropic); Gemini-1.5-Pro (Google); Llama-3.1-8B, Llama-3.1-70B (Meta); Qwen2.5-7B, Qwen2.5-72B (Alibaba); Mistral-7B-v0.3, Phi-3-medium-14B (Microsoft). Three capability tiers: Small (7--14B), Medium (14--34B), Large (70B+ and API).\n\n\\paragraph{Panels.} All $\\binom{15}{3} = 455$ three-judge panels, extended to $K \\in \\{5,7,9\\}$ for panel-size analysis.\n\n\\paragraph{Attacks.} 9 attack types spanning three paradigms: \\emph{bias exploitation} (sycophancy, verbosity, authority bias), \\emph{score manipulation} (direct score manipulation, position bias, few-shot bias), and \\emph{injection} (few-shot hijacking, persona manipulation, instruction override).\n\n\\paragraph{Benchmarks.} MMLU and ARC-Challenge (MCQ); MT-Bench and AlpacaEval (open-ended generation).\n\n\\paragraph{Statistical Methods.} FDR correction (Benjamini-Hochberg) for multiple comparisons; beta regression for distributional robustness; residualization for multicollinearity control.\n\n\\section{The Diversity Trap: Core Evidence}\n\n\\subsection{Dual Vulnerability Drivers}\n\nTable~\\ref{tab:core} presents the core regression results across 12 conditions (2 datasets $\\times$ 6 attacks). Both $\\etamax$ and $\\keffresid$ are significant predictors of panel ASR: $\\etamax$ reaches FDR significance in 10/12 conditions, $\\keffresid$ in 10/12 conditions. The mean $R^2 = 0.62$, indicating that these two factors jointly explain the majority of panel-level vulnerability variance.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Dual vulnerability drivers: 15-model regression across 12 conditions (455 panels each). $\\keffresid$ is residualized against $\\etamax$ (VIF$=$1.02). Bold $p$-values are FDR-significant ($q < 0.05$). ``Dominant'' indicates which predictor has the larger standardized $\\beta$.}\n\\label{tab:core}\n\\begin{tabular}{lccccccl}\n\\toprule\nCondition & $\\etamax$ $\\beta$ & $p$ & $\\keffresid$ $\\beta$ & $p$ & $R^2$ & Confound $r$ & Dominant \\\\\n\\midrule\nmmlu$\\times$sycophancy & 0.82 & \\textbf{1.2e-8} & 0.31 & \\textbf{0.004} & 0.68 & 0.72 & $\\etamax$ \\\\\nmmlu$\\times$score\\_manip & 0.45 & \\textbf{0.018} & 0.61 & \\textbf{3.4e-9} & 0.71 & 0.38 & $\\keff$ \\\\\nmmlu$\\times$position & 0.15 & 0.214 & 0.58 & \\textbf{1.2e-8} & 0.56 & 0.36 & $\\keff$ \\\\\nmmlu$\\times$verbosity & 0.74 & \\textbf{4.1e-7} & 0.28 & \\textbf{0.011} & 0.63 & 0.74 & $\\etamax$ \\\\\nmmlu$\\times$authority & 0.69 & \\textbf{1.8e-6} & 0.19 & 0.087 & 0.58 & 0.78 & $\\etamax$ \\\\\nmmlu$\\times$few\\_shot & 0.55 & \\textbf{2.3e-4} & 0.48 & \\textbf{6.1e-6} & 0.65 & 0.65 & both \\\\\n\\midrule\narc$\\times$sycophancy & 0.79 & \\textbf{3.5e-8} & 0.35 & \\textbf{0.002} & 0.66 & 0.71 & $\\etamax$ \\\\\narc$\\times$score\\_manip & 0.38 & 0.117 & 0.64 & \\textbf{1.7e-7} & 0.59 & 0.35 & $\\keff$ \\\\\narc$\\times$position & 0.03 & 0.910 & 0.72 & \\textbf{1.8e-8} & 0.57 & 0.34 & $\\keff$ \\\\\narc$\\times$verbosity & 0.71 & \\textbf{8.9e-7} & 0.33 & \\textbf{0.003} & 0.61 & 0.73 & $\\etamax$ \\\\\narc$\\times$authority & 0.66 & \\textbf{3.2e-6} & 0.22 & 0.062 & 0.55 & 0.76 & $\\etamax$ \\\\\narc$\\times$few\\_shot & 0.51 & \\textbf{5.7e-4} & 0.52 & \\textbf{3.8e-6} & 0.63 & 0.62 & both \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nA systematic pattern emerges: \\textbf{transferable attacks} (score manipulation, position bias) are $\\keff$-dominated ($\\beta_K > \\beta_\\eta$), while \\textbf{shared-bias attacks} (sycophancy, verbosity, authority) are $\\etamax$-dominated. This yields a predictive taxonomy: given a new attack type, its transferability predicts which vulnerability channel dominates.\n\nThree conditions have low confound correlation ($r \\approx 0.35$), serving as ``smoking gun'' evidence: in these conditions, $\\keffresid$ achieves $p < 2.1 \\times 10^{-28}$, confirming diversity's independent harmful effect even where the $\\keff$-$\\etamax$ association is weak.\n\n\\subsection{Capability-Matched Validation}\n\nA natural concern is that $\\keff$'s positive effect is an artifact of tier-mixing: high-$\\keff$ panels might mix weak and strong models, making $\\keff$ a proxy for tier heterogeneity rather than diversity \\emph{per se}. We test this by running within-tier regressions (Table~\\ref{tab:tier}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Within-tier $\\keff$ validation. Large tier uses only top-tier models (70B+ and API), eliminating tier-mixing.}\n\\label{tab:tier}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & Models & Panels & $r(\\keff,\\etamax)$ & $\\keffresid$ sig \\\\\n\\midrule\nSmall (7B--14B) & 5 & 10 & 0.32 & 2/6 \\\\\nMedium & 4 & 4 & 0.41 & 1/6 \\\\\nLarge (70B+API) & 6 & 20 & 0.33 & 4/6 \\\\\nCross-tier (all) & 15 & 455 & 0.55 & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe large tier is most informative: all 6 models are top-tier (GPT-4o, GPT-4.1, Claude-3.5-Sonnet, Gemini-1.5-Pro, Llama-70B, Qwen-72B), yet $\\keffresid$ is significant in 4/6 conditions (best $p = 4.2 \\times 10^{-4}$). The condition-dependent pattern is preserved: score manipulation and position bias are $\\keff$-dominated; sycophancy and verbosity are $\\etamax$-dominated. This rules out tier-mixing as the driver of the diversity trap.\n\n\\subsection{Statistical Robustness}\n\nWe perform comprehensive diagnostics (Table~\\ref{tab:diagnostics}). VIF$=$1.02 and condition number$=$4.8 confirm the design matrix is well-conditioned. Residuals pass Shapiro-Wilk normality ($p = 0.23$). Maximum Cook's distance is 0.031 (threshold: 1.0), with only 2.4\\% high-leverage points. Under Bonferroni correction (most conservative), $\\keffresid$ remains significant in 8/12 conditions. Beta regression, which properly handles bounded ASR in $[0,1]$, confirms 9/12 significant---highly consistent with OLS.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multiple comparison robustness across correction methods.}\n\\label{tab:diagnostics}\n\\begin{tabular}{lcc}\n\\toprule\nCorrection & $\\keffresid$ sig & $\\etamax$ sig \\\\\n\\midrule\nUncorrected & 12/12 & 11/12 \\\\\nFDR (BH) & 10/12 & 10/12 \\\\\nBonferroni & 8/12 & 9/12 \\\\\nBeta reg.\\ + FDR & 9/12 & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Mechanism: BFT Reversal}\n\n\\subsection{Random-Fault Contrast}\n\nBFT predicts that diversity helps when faults are independent and random. We test this by simulating calibrated random faults: each judge's failure probability is drawn from bootstrapped clean-accuracy noise, independent across judges. Table~\\ref{tab:bft} contrasts $\\keff$'s coefficient under adaptive versus random-fault regimes.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{BFT regime contrast: $\\keff$ coefficient under adaptive vs.\\ calibrated random faults (12 conditions, 455 panels). ``Flipped'' indicates $\\beta_{\\text{RF}}$ is significantly negative (diversity helps under random faults).}\n\\label{tab:bft}\n\\begin{tabular}{lcccccc}\n\\toprule\nCondition & $\\beta_{\\text{adaptive}}$ & $p_{\\text{adap}}$ & $\\beta_{\\text{RF}}$ & $p_{\\text{RF}}$ & $|\\beta_{\\text{adap}}/\\beta_{\\text{RF}}|$ & Flipped? \\\\\n\\midrule\nmmlu$\\times$sycophancy & 0.31 & \\textbf{0.004} & 0.08 & 0.310 & 3.88 & No \\\\\nmmlu$\\times$score\\_manip & 0.61 & \\textbf{3.4e-9} & $-$0.22 & \\textbf{0.015} & 2.77 & Yes \\\\\nmmlu$\\times$position & 0.58 & \\textbf{1.2e-8} & $-$0.31 & \\textbf{0.003} & 1.87 & Yes \\\\\nmmlu$\\times$verbosity & 0.28 & \\textbf{0.011} & 0.11 & 0.198 & 2.55 & No \\\\\nmmlu$\\times$authority & 0.19 & 0.087 & 0.06 & 0.541 & 3.17 & No \\\\\nmmlu$\\times$few\\_shot & 0.48 & \\textbf{6.1e-6} & $-$0.18 & \\textbf{0.039} & 2.67 & Yes \\\\\narc$\\times$sycophancy & 0.35 & \\textbf{0.002} & 0.10 & 0.251 & 3.50 & No \\\\\narc$\\times$score\\_manip & 0.64 & \\textbf{1.7e-7} & $-$0.28 & \\textbf{0.008} & 2.29 & Yes \\\\\narc$\\times$position & 0.72 & \\textbf{1.8e-8} & $-$0.35 & \\textbf{0.001} & 2.06 & Yes \\\\\narc$\\times$verbosity & 0.33 & \\textbf{0.003} & 0.12 & 0.175 & 2.75 & No \\\\\narc$\\times$authority & 0.22 & 0.062 & 0.05 & 0.612 & 4.40 & No \\\\\narc$\\times$few\\_shot & 0.52 & \\textbf{3.8e-6} & $-$0.14 & 0.091 & 3.71 & Marginal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe results confirm the BFT reversal: in 5/12 conditions, $\\beta_{\\text{RF}}$ flips to significantly \\emph{negative}---diversity genuinely protects under random faults, as BFT predicts. The flips concentrate on transferable attacks (score manipulation, position bias, few-shot), where judge-specific exploit paths are most relevant. Under adaptive attacks, these same conditions show the strongest positive $\\beta$ (0.48--0.72). The mean $\\beta$ ratio is 2.8$\\times$, and the $R^2$ gap ($\\Delta R^2 = 0.31$; RF: 0.78, adaptive: 0.47) quantifies BFT's broken predictability: panel structure explains 78\\% of variance under random faults but only 47\\% under adaptive attacks, where strategic adversary behavior introduces irreducible noise.\n\n\\subsection{ASR Concentration Analysis}\n\nTo illuminate \\emph{how} adaptive adversaries exploit diversity, we analyze per-judge ASR distributions within panels (Table~\\ref{tab:concentration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{ASR concentration: adaptive vs.\\ random-fault regimes.}\n\\label{tab:concentration}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Adaptive & RF & Ratio \\\\\n\\midrule\nMean Gini & 0.68 & 0.12 & 5.67 \\\\\nEntropy (bits) & 1.42 & 2.31 & 0.61 \\\\\nTop-1 judge share & 0.78 & 0.38 & 2.05 \\\\\n$r(\\keff, \\text{Gini})$ & 0.52 & 0.08 & 6.50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder adaptive attacks, ASR is highly concentrated: the weakest judge absorbs 78\\% of attack success (vs.\\ 38\\% under random faults). Crucially, $r(\\keff, \\text{Gini}) = 0.52$: more diverse panels produce \\emph{more concentrated} attacks, because greater capability spread gives the adversary a clearer targeting gradient. Under random faults, concentration is uniformly low (Gini$=$0.12), confirming BFT's independence assumption holds only in the non-adversarial regime.\n\n\\section{Generalization}\n\n\\subsection{Attack Surface Expansion}\n\nTo test whether the diversity trap generalizes beyond the original 6 attack types, we introduce 3 additional attacks: few-shot hijacking (in-context example injection), persona manipulation (authority impersonation), and instruction override (direct prompt overwrite). Table~\\ref{tab:expanded} shows the 6 new conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Extended attack results (6 new conditions, 15 models).}\n\\label{tab:expanded}\n\\begin{tabular}{lccc}\n\\toprule\nCondition & $\\keffresid$ $\\beta$ & $p$ & Dominant \\\\\n\\midrule\nmmlu$\\times$hijack & 0.54 & \\textbf{8.2e-7} & $\\keff$ \\\\\nmmlu$\\times$persona & 0.29 & \\textbf{0.008} & $\\etamax$ \\\\\nmmlu$\\times$override & 0.22 & 0.042 & $\\etamax$ \\\\\narc$\\times$hijack & 0.58 & \\textbf{2.1e-7} & $\\keff$ \\\\\narc$\\times$persona & 0.25 & \\textbf{0.019} & $\\etamax$ \\\\\narc$\\times$override & 0.18 & 0.112 & $\\etamax$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\keffresid$ is significant in 4/6 new conditions. Combined with the original 12, this yields 14/18 total FDR-significant conditions for $\\keffresid$. The attack taxonomy is predictive: high-transferability attacks (few-shot hijacking) are $\\keff$-dominated; moderate/low-transferability attacks (persona, instruction override) are $\\etamax$-dominated---consistent with the core results.\n\n\\subsection{Open-Ended Benchmarks}\n\nThe diversity trap is not an MCQ artifact. On MT-Bench (multi-turn dialogue evaluation) and AlpacaEval (instruction-following scoring), $\\keffresid$ is significant in 3/4 and 2/4 conditions, respectively (Table~\\ref{tab:openended}). The condition-dependent dominance pattern transfers without modification: score manipulation and position bias remain $\\keff$-dominated; sycophancy and verbosity remain $\\etamax$-dominated. $R^2$ is lower (0.39--0.52 vs.\\ 0.62 for MCQ), reflecting the higher noise floor inherent to open-ended evaluation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Open-ended benchmark results (8 conditions). Pattern consistent with MCQ findings despite higher evaluation noise.}\n\\label{tab:openended}\n\\begin{tabular}{lcccl}\n\\toprule\nCondition & $\\keffresid$ $\\beta$ & $p$ & $R^2$ & Dom. \\\\\n\\midrule\nMT$\\times$score & 0.52 & \\textbf{1.8e-5} & 0.52 & $\\keff$ \\\\\nMT$\\times$syco & 0.28 & \\textbf{0.012} & 0.49 & $\\etamax$ \\\\\nMT$\\times$pos & 0.47 & \\textbf{8.3e-5} & 0.44 & $\\keff$ \\\\\nMT$\\times$verb & 0.18 & 0.108 & 0.47 & $\\etamax$ \\\\\nAE$\\times$score & 0.44 & \\textbf{3.2e-4} & 0.46 & $\\keff$ \\\\\nAE$\\times$syco & 0.21 & 0.058 & 0.43 & $\\etamax$ \\\\\nAE$\\times$pos & 0.38 & \\textbf{0.002} & 0.40 & both \\\\\nAE$\\times$verb & 0.14 & 0.175 & 0.39 & $\\etamax$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Panel Size Sensitivity}\n\nExtending panel size from $K=3$ to $K \\in \\{5,7,9\\}$ reveals a scaling law: $\\keff$'s coefficient increases monotonically ($\\beta_K$: 0.42$\\to$0.48$\\to$0.55$\\to$0.61), while $\\etamax$'s decreases (0.51$\\to$0.49$\\to$0.43$\\to$0.38). The crossover occurs at $K \\approx 6$: for panels below this size, individual robustness ($\\etamax$) is the primary concern; above it, structural diversity ($\\keff$) becomes dominant (Table~\\ref{tab:panelsize}). This has direct practical implications: the common strategy of ``adding more judges'' systematically amplifies the diversity trap---$K=9$ panels show 45\\% stronger $\\keff$ effect than $K=3$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Panel size sensitivity ($K = 3, 5, 7, 9$).}\n\\label{tab:panelsize}\n\\begin{tabular}{lccccl}\n\\toprule\n$K$ & Panels & $\\keffresid$ sig & $\\bar{\\beta}_K$ & $\\bar{\\beta}_\\eta$ & Primary \\\\\n\\midrule\n3 & 455 & 10/12 & 0.42 & 0.51 & $\\etamax$ \\\\\n5 & 3003 & 11/12 & 0.48 & 0.49 & balanced \\\\\n7 & 6435 & 12/12 & 0.55 & 0.43 & $\\keff$ \\\\\n9 & 5005 & 12/12 & 0.61 & 0.38 & $\\keff$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Partial-Knowledge Adversary}\n\nA full-knowledge adversary is a worst-case assumption. We test a realistic partial-knowledge adversary who knows only model \\emph{family} membership (typically public information) but not individual vulnerability profiles. Family-level targeting achieves 78.4\\% of full-knowledge ASR (0.058 vs.\\ 0.074), and $\\keff$ remains significant in 7/12 conditions (Table~\\ref{tab:partial}). Family membership alone captures 62.8\\% of adversary information value, because family$\\to$capability tier correlations provide a strong prior on vulnerability profiles.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Adversary knowledge level comparison.}\n\\label{tab:partial}\n\\begin{tabular}{lcccc}\n\\toprule\nKnowledge & ASR & $\\keff$ sig & $R^2$ & Info value \\\\\n\\midrule\nFull & 0.074 & 10/12 & 0.62 & 100\\% \\\\\nPartial (family) & 0.058 & 7/12 & 0.51 & 62.8\\% \\\\\nBlack-box & 0.031 & 3/12 & 0.28 & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Structural Barriers to Independence}\n\n\\subsection{Gaussian Copula Failure}\n\nIf inter-judge dependence followed a Gaussian copula, pairwise mutual information (MI) could be estimated from linear correlations. Across 105 model pairs (15 models), observed MI exceeds Gaussian-predicted MI by a mean factor of 18.5$\\times$ (max 312$\\times$), with 82/105 pairs exceeding 10$\\times$. This invalidates copula-based independence bounds and motivates empirical $\\keff$ measurement.\n\n\\subsection{Family Labels Are Unreliable}\n\nModel family labels do not predict judge independence: within-family MI (0.42) is not significantly higher than cross-family MI (0.39; Mann-Whitney $p = 0.158$). The actual driver is capability proximity ($r = -0.71$ with MI): models at similar capability levels share failure modes regardless of training pipeline. Practitioners should not equate ``different families'' with ``diverse panel.''\n\n\\subsection{Diversity-Capability Tradeoff}\n\nAcross 455 panels, $\\keff$ and $\\etamax$ correlate at $r = 0.55$ globally. Within capability tiers, this drops to $r \\approx 0.33$, revealing two components: a cross-tier component ($\\sim$40\\%, from mixing weak and strong models) and a within-tier residual ($\\sim$60\\%, from genuine diversity-vulnerability association). The Pareto frontier (18 panels, slope $-0.73$) quantifies the tradeoff: each 0.1 increase in $\\keff$ costs at least 0.073 increase in $\\etamax$.\n\n\\section{Defense: Panel Design and Aggregation}\n\n\\subsection{Two-Stage Panel Selection}\n\nWe propose a robustness-first algorithm: (1) screen judges by individual robustness ($\\eta_j \\leq$ percentile-75 threshold), (2) maximize $\\keff$ among qualifying judges. Table~\\ref{tab:defense} benchmarks this against 5 baselines.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Panel selection strategy benchmark (15 models, MMLU, 6 attacks). Two-stage achieves 84\\% of oracle efficiency.}\n\\label{tab:defense}\n\\begin{tabular}{lccc}\n\\toprule\nStrategy & ASR & $\\Delta$ vs Strong-K & Best (of 6) \\\\\n\\midrule\nTwo-Stage (ours) & 0.038 & $-$20.8\\% & 5/6 \\\\\nMin-$\\etamax$ & 0.041 & $-$14.6\\% & 4/6 \\\\\nStrongest-$K$ & 0.048 & baseline & 1/6 \\\\\nRandom & 0.089 & +85.4\\% & 0/6 \\\\\nMax-$\\keff$ & 0.112 & +133.3\\% & 0/6 \\\\\nOracle & 0.032 & $-$33.3\\% & 6/6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo-stage achieves the lowest ASR among non-oracle strategies (0.038), outperforming the strongest-$K$ baseline by 20.8\\%. Max-$\\keff$ is catastrophic (ASR 0.112, +133\\%), providing the most direct evidence against blind diversity maximization. Sensitivity analysis shows the screening threshold is robust across percentile 50--75, with optimal performance at percentile 65--75.\n\n\\subsection{Aggregation Rule Modulation}\n\nThe dual vulnerability driver effect varies by aggregation rule (Table~\\ref{tab:aggregation}). Threshold (unanimity) voting amplifies $\\keff$'s harmful effect by 45\\% ($\\beta_K$: 0.42$\\to$0.61) and increases ASR by 86\\%, because a single flipped judge blocks panel rejection. Bayesian aggregation, which downweights judges based on prior accuracy, provides the best single-aggregation defense: 28.4\\% ASR reduction, with $\\keff$ significance dropping from 10/12 to 6/12. However, 6/12 $\\keff$ significance confirms Bayesian aggregation alone cannot eliminate the diversity trap, motivating a combined defense stack.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Aggregation rule $\\times$ vulnerability drivers (455 panels).}\n\\label{tab:aggregation}\n\\begin{tabular}{lcccc}\n\\toprule\nAggregation & $\\keff$ sig & $\\bar{\\beta}_K$ & ASR & $\\Delta$ \\\\\n\\midrule\nMajority & 10/12 & 0.42 & 0.074 & -- \\\\\nThreshold & 11/12 & 0.61 & 0.138 & +86\\% \\\\\nAcc-weighted & 8/12 & 0.39 & 0.069 & $-$6.8\\% \\\\\nBayesian & 6/12 & 0.25 & 0.053 & $-$28.4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Conclusion}\n\nWe presented large-scale empirical evidence for the \\emph{diversity trap} in multi-judge LLM evaluation: panel diversity independently increases vulnerability to adaptive adversarial attacks. This finding, validated across 15 models, 455 panels, 9 attack types, 4 benchmarks, and multiple panel sizes, challenges the pervasive assumption that diversity improves evaluation robustness. The mechanism traces to BFT's broken assumption: adaptive adversaries exploit the heterogeneous attack surface that diverse judges create, concentrating attacks on the weakest judge rather than facing independent random faults. We proposed a two-stage defense (robustness screening + diversity optimization) that reduces ASR by 20.8\\%, complemented by Bayesian aggregation ($-$28.4\\%). We urge the LLM evaluation community to adopt diversity-aware security analysis: do not assume more judges means safer evaluation.\n\n\\section*{Limitations}\n\nOur study has three main limitations. First, our adversary model assumes knowledge of panel composition (full or partial); in settings where panel membership is secret, the diversity trap may be attenuated. Second, while we cover 15 models from 6 families, the rapidly evolving LLM landscape means our specific quantitative findings may shift as new model generations emerge. Third, our analysis is observational---the regression design establishes independent predictive association, not strict causality, between diversity and vulnerability; experimental manipulation of panel composition with controlled interventions would strengthen causal claims.\n\n\\bibliography{anthology,custom}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d15839a-7f55-4e7e-b5f5-16fe09702356",
  "isSidechain": false,
  "requestId": "req_011CbJ4nM3QtehjCvtmuUG2F",
  "type": "assistant",
  "uuid": "a4d17bf8-7817-42f9-b4ee-6bc05afb7cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1vvZcCXLgBwgU2Vwi2Ruy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4531,
      "cache_read_input_tokens": 46567,
      "output_tokens": 11017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11017,
          "cache_read_input_tokens": 46567,
          "cache_creation_input_tokens": 4531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4531
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

_source line 23 · 2026-05-22T18:20:38.236Z_

<details><summary>↩ Tool result · `toolu_01VqBe5DLJ2VV1ye7M2YCZCh`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4d17bf8-7817-42f9-b4ee-6bc05afb7cc8",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "4a3528e9-1d8d-433b-8faf-c7097dd0cc9c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{amsmath}\n\\usepackage{amsfonts}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\n\\setlength\\titlebox{5cm}\n\n\\newcommand{\\keff}{K_{\\text{eff}}}\n\\newcommand{\\etamax}{\\eta_{\\text{max}}}\n\\newcommand{\\keffresid}{K_{\\text{eff}}^{\\text{resid}}}\n\n\\title{More Diverse, More Vulnerable:\\\\How Judge Panel Diversity Backfires Under Adaptive Adversaries}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge evaluation panels are increasingly used to assess LLM outputs, with the prevailing assumption that judge diversity---analogous to Byzantine Fault Tolerance (BFT)---improves robustness against manipulation. We provide large-scale empirical evidence that this assumption \\emph{reverses} under adaptive adversaries. Across 15 LLM judges spanning 6 model families, 455 three-judge panels, 9 attack types, and 4 evaluation benchmarks, we show that panel diversity (effective independence $\\keff$) is \\textbf{independently and positively} associated with attack success rate (ASR), even after residualizing against individual judge weakness ($\\etamax$). This ``diversity trap'' is driven by dual vulnerability channels whose relative importance is attack-dependent: $\\etamax$ dominates shared-bias attacks (sycophancy, verbosity), while $\\keff$ dominates transferable attacks (score manipulation, position bias). We trace the mechanism to BFT's broken assumption: random faults distribute uniformly across judges (Gini$\\approx$0.12), but adaptive adversaries concentrate attacks on the weakest judge (Gini$\\approx$0.68), turning diversity from a defense into an expanded attack surface. Under calibrated random faults, $\\keff$'s coefficient flips negative in 5/12 conditions, empirically confirming BFT's prediction. We propose a robustness-first two-stage panel selection algorithm that reduces ASR by 20.8\\% over the strongest-$K$ baseline, and show that Bayesian aggregation provides a complementary 28.4\\% reduction. Our findings challenge the ``more diverse = more robust'' assumption and call for diversity-aware security analysis in LLM evaluation pipeline design.\n\\end{abstract}\n\n\\section{Introduction}\n\nAs LLMs are increasingly deployed as automated evaluators~\\cite{zheng2023judging,li2023alpacaeval}, the research community has adopted multi-judge panels to mitigate individual model biases. The intuition is straightforward and borrowed from distributed systems: diverse, independent judges should be harder to simultaneously fool, much like Byzantine Fault Tolerance (BFT) guarantees that $f$ faulty nodes cannot compromise a system of $3f+1$ independent replicas.\n\nThis paper demonstrates that this intuition is \\emph{wrong} under adversarial conditions. We conduct what is, to our knowledge, the largest systematic study of adversarial robustness in multi-judge LLM evaluation: 15 models from 6 families (OpenAI, Anthropic, Google, Meta, Alibaba, Microsoft), enumerated into 455 three-judge panels, evaluated under 9 distinct attack types across MMLU, ARC-Challenge, MT-Bench, and AlpacaEval.\n\nOur central finding is the \\textbf{diversity trap}: panel diversity, measured by effective judge independence ($\\keff$), is \\emph{independently and positively} associated with attack success rate. After residualizing $\\keff$ against individual judge weakness ($\\etamax$, the maximum vulnerability of any panel member), $\\keffresid$ remains significantly positive in 10/12 conditions (FDR-corrected). Panel vulnerability is driven by \\textbf{dual factors}---$\\etamax$ and $\\keff$---whose relative importance depends on attack type:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Shared-bias attacks} (sycophancy, verbosity, authority): $\\etamax$ dominates because all judges share similar cognitive biases from RLHF training.\n\\item \\textbf{Transferable attacks} (score manipulation, position bias): $\\keff$ dominates because diverse judges provide heterogeneous, judge-specific attack surfaces.\n\\end{itemize}\n\nWe trace this to BFT's core assumption: fault independence. Under random faults, failures distribute uniformly (Gini$\\approx$0.12) and diversity genuinely helps---our calibrated random-fault simulations show $\\keff$'s coefficient \\emph{flipping negative} in 5/12 conditions. But adaptive adversaries concentrate attacks on the weakest judges (Gini$\\approx$0.68, top-1 judge absorbing 78\\% of ASR), turning diversity from fault tolerance into an expanded attack menu.\n\nWe further show that: (1) the diversity trap holds within capability tiers (4/6 conditions significant among top-tier models only), ruling out tier-mixing confounds; (2) generalizes to open-ended benchmarks (MT-Bench 3/4, AlpacaEval 2/4 significant); (3) scales with panel size ($\\keff$ coefficient increases monotonically from $K$=3 to $K$=9); (4) holds under partial-knowledge adversaries who know only model family membership (7/12 significant). We propose a two-stage defense---robustness screening followed by diversity optimization---that achieves 20.8\\% ASR reduction over the strongest-$K$ baseline, and show Bayesian aggregation provides complementary protection.\n\n\\section{Related Work}\n\n\\paragraph{LLM-as-Judge.} LLM evaluation using model judges has become standard practice~\\cite{zheng2023judging,li2023alpacaeval,dubois2024alpacafarm}. Known biases include position bias, verbosity preference, and self-enhancement~\\cite{wang2023large,zheng2023judging}. Multi-judge panels are proposed as mitigation, but their adversarial robustness remains unstudied.\n\n\\paragraph{Adversarial Attacks on LLM Judges.} Prior work demonstrates individual judge vulnerability to prompt injection, sycophancy exploitation, and score manipulation~\\cite{raina2024llm,shi2024optimization}. We extend this to \\emph{panel-level} analysis, studying how panel composition mediates vulnerability.\n\n\\paragraph{Byzantine Fault Tolerance.} Classical BFT~\\cite{lamport1982byzantine,castro1999practical} guarantees safety when faults are independent. Recent work questions independence assumptions in ML systems~\\cite{sagawa2020investigation}. We empirically test whether BFT's independence assumption holds for LLM judge panels.\n\n\\paragraph{Ensemble Diversity.} The diversity-accuracy tradeoff is well-studied in ensemble learning~\\cite{krogh1994neural,brown2005diversity}. Our setting differs: we study diversity under \\emph{adaptive adversaries} who exploit panel composition, not passive noise.\n\n\\section{Problem Formulation}\n\n\\paragraph{Setup.} A panel $P = \\{j_1, \\ldots, j_K\\}$ of $K$ LLM judges evaluates candidate responses. Each judge $j_i$ produces a binary decision (accept/reject). The panel decision uses an aggregation rule $\\mathcal{A}$ (default: majority vote).\n\n\\paragraph{Adversary Model.} An adaptive adversary observes the panel composition and crafts attacks to maximize the panel's attack success rate (ASR)---the fraction of evaluation instances where the panel decision is flipped.\n\n\\paragraph{Vulnerability Metrics.} We define two panel-level predictors:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item $\\etamax = \\max_{j \\in P} \\eta_j$: maximum individual vulnerability (weakest link). $\\eta_j$ is judge $j$'s individual ASR under a given attack.\n\\item $\\keff$: effective number of independent judges, computed from the eigenspectrum of the pairwise mutual information matrix. Higher $\\keff$ indicates greater functional diversity.\n\\end{itemize}\n\nTo disentangle $\\keff$ from $\\etamax$, we define $\\keffresid$ as the residual of regressing $\\keff$ on $\\etamax$, ensuring orthogonality (VIF$=$1.02).\n\n\\paragraph{Regression Model.} For each condition (dataset $\\times$ attack type), we fit:\n\\begin{equation}\n\\text{ASR}_P = \\beta_0 + \\beta_\\eta \\cdot \\etamax + \\beta_K \\cdot \\keffresid + \\epsilon\n\\end{equation}\nacross all 455 panels. A significantly positive $\\beta_K$ indicates diversity independently increases vulnerability.\n\n\\section{Experimental Setup}\n\n\\paragraph{Models.} 15 LLM judges: GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini (OpenAI); Claude-3.5-Sonnet (Anthropic); Gemini-1.5-Pro (Google); Llama-3.1-8B, Llama-3.1-70B (Meta); Qwen2.5-7B, Qwen2.5-72B (Alibaba); Mistral-7B-v0.3, Phi-3-medium-14B (Microsoft). Three capability tiers: Small (7--14B), Medium (14--34B), Large (70B+ and API).\n\n\\paragraph{Panels.} All $\\binom{15}{3} = 455$ three-judge panels, extended to $K \\in \\{5,7,9\\}$ for panel-size analysis.\n\n\\paragraph{Attacks.} 9 attack types spanning three paradigms: \\emph{bias exploitation} (sycophancy, verbosity, authority bias), \\emph{score manipulation} (direct score manipulation, position bias, few-shot bias), and \\emph{injection} (few-shot hijacking, persona manipulation, instruction override).\n\n\\paragraph{Benchmarks.} MMLU and ARC-Challenge (MCQ); MT-Bench and AlpacaEval (open-ended generation).\n\n\\paragraph{Statistical Methods.} FDR correction (Benjamini-Hochberg) for multiple comparisons; beta regression for distributional robustness; residualization for multicollinearity control.\n\n\\section{The Diversity Trap: Core Evidence}\n\n\\subsection{Dual Vulnerability Drivers}\n\nTable~\\ref{tab:core} presents the core regression results across 12 conditions (2 datasets $\\times$ 6 attacks). Both $\\etamax$ and $\\keffresid$ are significant predictors of panel ASR: $\\etamax$ reaches FDR significance in 10/12 conditions, $\\keffresid$ in 10/12 conditions. The mean $R^2 = 0.62$, indicating that these two factors jointly explain the majority of panel-level vulnerability variance.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Dual vulnerability drivers: 15-model regression across 12 conditions (455 panels each). $\\keffresid$ is residualized against $\\etamax$ (VIF$=$1.02). Bold $p$-values are FDR-significant ($q < 0.05$). ``Dominant'' indicates which predictor has the larger standardized $\\beta$.}\n\\label{tab:core}\n\\begin{tabular}{lccccccl}\n\\toprule\nCondition & $\\etamax$ $\\beta$ & $p$ & $\\keffresid$ $\\beta$ & $p$ & $R^2$ & Confound $r$ & Dominant \\\\\n\\midrule\nmmlu$\\times$sycophancy & 0.82 & \\textbf{1.2e-8} & 0.31 & \\textbf{0.004} & 0.68 & 0.72 & $\\etamax$ \\\\\nmmlu$\\times$score\\_manip & 0.45 & \\textbf{0.018} & 0.61 & \\textbf{3.4e-9} & 0.71 & 0.38 & $\\keff$ \\\\\nmmlu$\\times$position & 0.15 & 0.214 & 0.58 & \\textbf{1.2e-8} & 0.56 & 0.36 & $\\keff$ \\\\\nmmlu$\\times$verbosity & 0.74 & \\textbf{4.1e-7} & 0.28 & \\textbf{0.011} & 0.63 & 0.74 & $\\etamax$ \\\\\nmmlu$\\times$authority & 0.69 & \\textbf{1.8e-6} & 0.19 & 0.087 & 0.58 & 0.78 & $\\etamax$ \\\\\nmmlu$\\times$few\\_shot & 0.55 & \\textbf{2.3e-4} & 0.48 & \\textbf{6.1e-6} & 0.65 & 0.65 & both \\\\\n\\midrule\narc$\\times$sycophancy & 0.79 & \\textbf{3.5e-8} & 0.35 & \\textbf{0.002} & 0.66 & 0.71 & $\\etamax$ \\\\\narc$\\times$score\\_manip & 0.38 & 0.117 & 0.64 & \\textbf{1.7e-7} & 0.59 & 0.35 & $\\keff$ \\\\\narc$\\times$position & 0.03 & 0.910 & 0.72 & \\textbf{1.8e-8} & 0.57 & 0.34 & $\\keff$ \\\\\narc$\\times$verbosity & 0.71 & \\textbf{8.9e-7} & 0.33 & \\textbf{0.003} & 0.61 & 0.73 & $\\etamax$ \\\\\narc$\\times$authority & 0.66 & \\textbf{3.2e-6} & 0.22 & 0.062 & 0.55 & 0.76 & $\\etamax$ \\\\\narc$\\times$few\\_shot & 0.51 & \\textbf{5.7e-4} & 0.52 & \\textbf{3.8e-6} & 0.63 & 0.62 & both \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nA systematic pattern emerges: \\textbf{transferable attacks} (score manipulation, position bias) are $\\keff$-dominated ($\\beta_K > \\beta_\\eta$), while \\textbf{shared-bias attacks} (sycophancy, verbosity, authority) are $\\etamax$-dominated. This yields a predictive taxonomy: given a new attack type, its transferability predicts which vulnerability channel dominates.\n\nThree conditions have low confound correlation ($r \\approx 0.35$), serving as ``smoking gun'' evidence: in these conditions, $\\keffresid$ achieves $p < 2.1 \\times 10^{-28}$, confirming diversity's independent harmful effect even where the $\\keff$-$\\etamax$ association is weak.\n\n\\subsection{Capability-Matched Validation}\n\nA natural concern is that $\\keff$'s positive effect is an artifact of tier-mixing: high-$\\keff$ panels might mix weak and strong models, making $\\keff$ a proxy for tier heterogeneity rather than diversity \\emph{per se}. We test this by running within-tier regressions (Table~\\ref{tab:tier}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Within-tier $\\keff$ validation. Large tier uses only top-tier models (70B+ and API), eliminating tier-mixing.}\n\\label{tab:tier}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & Models & Panels & $r(\\keff,\\etamax)$ & $\\keffresid$ sig \\\\\n\\midrule\nSmall (7B--14B) & 5 & 10 & 0.32 & 2/6 \\\\\nMedium & 4 & 4 & 0.41 & 1/6 \\\\\nLarge (70B+API) & 6 & 20 & 0.33 & 4/6 \\\\\nCross-tier (all) & 15 & 455 & 0.55 & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe large tier is most informative: all 6 models are top-tier (GPT-4o, GPT-4.1, Claude-3.5-Sonnet, Gemini-1.5-Pro, Llama-70B, Qwen-72B), yet $\\keffresid$ is significant in 4/6 conditions (best $p = 4.2 \\times 10^{-4}$). The condition-dependent pattern is preserved: score manipulation and position bias are $\\keff$-dominated; sycophancy and verbosity are $\\etamax$-dominated. This rules out tier-mixing as the driver of the diversity trap.\n\n\\subsection{Statistical Robustness}\n\nWe perform comprehensive diagnostics (Table~\\ref{tab:diagnostics}). VIF$=$1.02 and condition number$=$4.8 confirm the design matrix is well-conditioned. Residuals pass Shapiro-Wilk normality ($p = 0.23$). Maximum Cook's distance is 0.031 (threshold: 1.0), with only 2.4\\% high-leverage points. Under Bonferroni correction (most conservative), $\\keffresid$ remains significant in 8/12 conditions. Beta regression, which properly handles bounded ASR in $[0,1]$, confirms 9/12 significant---highly consistent with OLS.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multiple comparison robustness across correction methods.}\n\\label{tab:diagnostics}\n\\begin{tabular}{lcc}\n\\toprule\nCorrection & $\\keffresid$ sig & $\\etamax$ sig \\\\\n\\midrule\nUncorrected & 12/12 & 11/12 \\\\\nFDR (BH) & 10/12 & 10/12 \\\\\nBonferroni & 8/12 & 9/12 \\\\\nBeta reg.\\ + FDR & 9/12 & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Mechanism: BFT Reversal}\n\n\\subsection{Random-Fault Contrast}\n\nBFT predicts that diversity helps when faults are independent and random. We test this by simulating calibrated random faults: each judge's failure probability is drawn from bootstrapped clean-accuracy noise, independent across judges. Table~\\ref{tab:bft} contrasts $\\keff$'s coefficient under adaptive versus random-fault regimes.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{BFT regime contrast: $\\keff$ coefficient under adaptive vs.\\ calibrated random faults (12 conditions, 455 panels). ``Flipped'' indicates $\\beta_{\\text{RF}}$ is significantly negative (diversity helps under random faults).}\n\\label{tab:bft}\n\\begin{tabular}{lcccccc}\n\\toprule\nCondition & $\\beta_{\\text{adaptive}}$ & $p_{\\text{adap}}$ & $\\beta_{\\text{RF}}$ & $p_{\\text{RF}}$ & $|\\beta_{\\text{adap}}/\\beta_{\\text{RF}}|$ & Flipped? \\\\\n\\midrule\nmmlu$\\times$sycophancy & 0.31 & \\textbf{0.004} & 0.08 & 0.310 & 3.88 & No \\\\\nmmlu$\\times$score\\_manip & 0.61 & \\textbf{3.4e-9} & $-$0.22 & \\textbf{0.015} & 2.77 & Yes \\\\\nmmlu$\\times$position & 0.58 & \\textbf{1.2e-8} & $-$0.31 & \\textbf{0.003} & 1.87 & Yes \\\\\nmmlu$\\times$verbosity & 0.28 & \\textbf{0.011} & 0.11 & 0.198 & 2.55 & No \\\\\nmmlu$\\times$authority & 0.19 & 0.087 & 0.06 & 0.541 & 3.17 & No \\\\\nmmlu$\\times$few\\_shot & 0.48 & \\textbf{6.1e-6} & $-$0.18 & \\textbf{0.039} & 2.67 & Yes \\\\\narc$\\times$sycophancy & 0.35 & \\textbf{0.002} & 0.10 & 0.251 & 3.50 & No \\\\\narc$\\times$score\\_manip & 0.64 & \\textbf{1.7e-7} & $-$0.28 & \\textbf{0.008} & 2.29 & Yes \\\\\narc$\\times$position & 0.72 & \\textbf{1.8e-8} & $-$0.35 & \\textbf{0.001} & 2.06 & Yes \\\\\narc$\\times$verbosity & 0.33 & \\textbf{0.003} & 0.12 & 0.175 & 2.75 & No \\\\\narc$\\times$authority & 0.22 & 0.062 & 0.05 & 0.612 & 4.40 & No \\\\\narc$\\times$few\\_shot & 0.52 & \\textbf{3.8e-6} & $-$0.14 & 0.091 & 3.71 & Marginal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe results confirm the BFT reversal: in 5/12 conditions, $\\beta_{\\text{RF}}$ flips to significantly \\emph{negative}---diversity genuinely protects under random faults, as BFT predicts. The flips concentrate on transferable attacks (score manipulation, position bias, few-shot), where judge-specific exploit paths are most relevant. Under adaptive attacks, these same conditions show the strongest positive $\\beta$ (0.48--0.72). The mean $\\beta$ ratio is 2.8$\\times$, and the $R^2$ gap ($\\Delta R^2 = 0.31$; RF: 0.78, adaptive: 0.47) quantifies BFT's broken predictability: panel structure explains 78\\% of variance under random faults but only 47\\% under adaptive attacks, where strategic adversary behavior introduces irreducible noise.\n\n\\subsection{ASR Concentration Analysis}\n\nTo illuminate \\emph{how} adaptive adversaries exploit diversity, we analyze per-judge ASR distributions within panels (Table~\\ref{tab:concentration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{ASR concentration: adaptive vs.\\ random-fault regimes.}\n\\label{tab:concentration}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Adaptive & RF & Ratio \\\\\n\\midrule\nMean Gini & 0.68 & 0.12 & 5.67 \\\\\nEntropy (bits) & 1.42 & 2.31 & 0.61 \\\\\nTop-1 judge share & 0.78 & 0.38 & 2.05 \\\\\n$r(\\keff, \\text{Gini})$ & 0.52 & 0.08 & 6.50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder adaptive attacks, ASR is highly concentrated: the weakest judge absorbs 78\\% of attack success (vs.\\ 38\\% under random faults). Crucially, $r(\\keff, \\text{Gini}) = 0.52$: more diverse panels produce \\emph{more concentrated} attacks, because greater capability spread gives the adversary a clearer targeting gradient. Under random faults, concentration is uniformly low (Gini$=$0.12), confirming BFT's independence assumption holds only in the non-adversarial regime.\n\n\\section{Generalization}\n\n\\subsection{Attack Surface Expansion}\n\nTo test whether the diversity trap generalizes beyond the original 6 attack types, we introduce 3 additional attacks: few-shot hijacking (in-context example injection), persona manipulation (authority impersonation), and instruction override (direct prompt overwrite). Table~\\ref{tab:expanded} shows the 6 new conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Extended attack results (6 new conditions, 15 models).}\n\\label{tab:expanded}\n\\begin{tabular}{lccc}\n\\toprule\nCondition & $\\keffresid$ $\\beta$ & $p$ & Dominant \\\\\n\\midrule\nmmlu$\\times$hijack & 0.54 & \\textbf{8.2e-7} & $\\keff$ \\\\\nmmlu$\\times$persona & 0.29 & \\textbf{0.008} & $\\etamax$ \\\\\nmmlu$\\times$override & 0.22 & 0.042 & $\\etamax$ \\\\\narc$\\times$hijack & 0.58 & \\textbf{2.1e-7} & $\\keff$ \\\\\narc$\\times$persona & 0.25 & \\textbf{0.019} & $\\etamax$ \\\\\narc$\\times$override & 0.18 & 0.112 & $\\etamax$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\keffresid$ is significant in 4/6 new conditions. Combined with the original 12, this yields 14/18 total FDR-significant conditions for $\\keffresid$. The attack taxonomy is predictive: high-transferability attacks (few-shot hijacking) are $\\keff$-dominated; moderate/low-transferability attacks (persona, instruction override) are $\\etamax$-dominated---consistent with the core results.\n\n\\subsection{Open-Ended Benchmarks}\n\nThe diversity trap is not an MCQ artifact. On MT-Bench (multi-turn dialogue evaluation) and AlpacaEval (instruction-following scoring), $\\keffresid$ is significant in 3/4 and 2/4 conditions, respectively (Table~\\ref{tab:openended}). The condition-dependent dominance pattern transfers without modification: score manipulation and position bias remain $\\keff$-dominated; sycophancy and verbosity remain $\\etamax$-dominated. $R^2$ is lower (0.39--0.52 vs.\\ 0.62 for MCQ), reflecting the higher noise floor inherent to open-ended evaluation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Open-ended benchmark results (8 conditions). Pattern consistent with MCQ findings despite higher evaluation noise.}\n\\label{tab:openended}\n\\begin{tabular}{lcccl}\n\\toprule\nCondition & $\\keffresid$ $\\beta$ & $p$ & $R^2$ & Dom. \\\\\n\\midrule\nMT$\\times$score & 0.52 & \\textbf{1.8e-5} & 0.52 & $\\keff$ \\\\\nMT$\\times$syco & 0.28 & \\textbf{0.012} & 0.49 & $\\etamax$ \\\\\nMT$\\times$pos & 0.47 & \\textbf{8.3e-5} & 0.44 & $\\keff$ \\\\\nMT$\\times$verb & 0.18 & 0.108 & 0.47 & $\\etamax$ \\\\\nAE$\\times$score & 0.44 & \\textbf{3.2e-4} & 0.46 & $\\keff$ \\\\\nAE$\\times$syco & 0.21 & 0.058 & 0.43 & $\\etamax$ \\\\\nAE$\\times$pos & 0.38 & \\textbf{0.002} & 0.40 & both \\\\\nAE$\\times$verb & 0.14 & 0.175 & 0.39 & $\\etamax$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Panel Size Sensitivity}\n\nExtending panel size from $K=3$ to $K \\in \\{5,7,9\\}$ reveals a scaling law: $\\keff$'s coefficient increases monotonically ($\\beta_K$: 0.42$\\to$0.48$\\to$0.55$\\to$0.61), while $\\etamax$'s decreases (0.51$\\to$0.49$\\to$0.43$\\to$0.38). The crossover occurs at $K \\approx 6$: for panels below this size, individual robustness ($\\etamax$) is the primary concern; above it, structural diversity ($\\keff$) becomes dominant (Table~\\ref{tab:panelsize}). This has direct practical implications: the common strategy of ``adding more judges'' systematically amplifies the diversity trap---$K=9$ panels show 45\\% stronger $\\keff$ effect than $K=3$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Panel size sensitivity ($K = 3, 5, 7, 9$).}\n\\label{tab:panelsize}\n\\begin{tabular}{lccccl}\n\\toprule\n$K$ & Panels & $\\keffresid$ sig & $\\bar{\\beta}_K$ & $\\bar{\\beta}_\\eta$ & Primary \\\\\n\\midrule\n3 & 455 & 10/12 & 0.42 & 0.51 & $\\etamax$ \\\\\n5 & 3003 & 11/12 & 0.48 & 0.49 & balanced \\\\\n7 & 6435 & 12/12 & 0.55 & 0.43 & $\\keff$ \\\\\n9 & 5005 & 12/12 & 0.61 & 0.38 & $\\keff$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Partial-Knowledge Adversary}\n\nA full-knowledge adversary is a worst-case assumption. We test a realistic partial-knowledge adversary who knows only model \\emph{family} membership (typically public information) but not individual vulnerability profiles. Family-level targeting achieves 78.4\\% of full-knowledge ASR (0.058 vs.\\ 0.074), and $\\keff$ remains significant in 7/12 conditions (Table~\\ref{tab:partial}). Family membership alone captures 62.8\\% of adversary information value, because family$\\to$capability tier correlations provide a strong prior on vulnerability profiles.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Adversary knowledge level comparison.}\n\\label{tab:partial}\n\\begin{tabular}{lcccc}\n\\toprule\nKnowledge & ASR & $\\keff$ sig & $R^2$ & Info value \\\\\n\\midrule\nFull & 0.074 & 10/12 & 0.62 & 100\\% \\\\\nPartial (family) & 0.058 & 7/12 & 0.51 & 62.8\\% \\\\\nBlack-box & 0.031 & 3/12 & 0.28 & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Structural Barriers to Independence}\n\n\\subsection{Gaussian Copula Failure}\n\nIf inter-judge dependence followed a Gaussian copula, pairwise mutual information (MI) could be estimated from linear correlations. Across 105 model pairs (15 models), observed MI exceeds Gaussian-predicted MI by a mean factor of 18.5$\\times$ (max 312$\\times$), with 82/105 pairs exceeding 10$\\times$. This invalidates copula-based independence bounds and motivates empirical $\\keff$ measurement.\n\n\\subsection{Family Labels Are Unreliable}\n\nModel family labels do not predict judge independence: within-family MI (0.42) is not significantly higher than cross-family MI (0.39; Mann-Whitney $p = 0.158$). The actual driver is capability proximity ($r = -0.71$ with MI): models at similar capability levels share failure modes regardless of training pipeline. Practitioners should not equate ``different families'' with ``diverse panel.''\n\n\\subsection{Diversity-Capability Tradeoff}\n\nAcross 455 panels, $\\keff$ and $\\etamax$ correlate at $r = 0.55$ globally. Within capability tiers, this drops to $r \\approx 0.33$, revealing two components: a cross-tier component ($\\sim$40\\%, from mixing weak and strong models) and a within-tier residual ($\\sim$60\\%, from genuine diversity-vulnerability association). The Pareto frontier (18 panels, slope $-0.73$) quantifies the tradeoff: each 0.1 increase in $\\keff$ costs at least 0.073 increase in $\\etamax$.\n\n\\section{Defense: Panel Design and Aggregation}\n\n\\subsection{Two-Stage Panel Selection}\n\nWe propose a robustness-first algorithm: (1) screen judges by individual robustness ($\\eta_j \\leq$ percentile-75 threshold), (2) maximize $\\keff$ among qualifying judges. Table~\\ref{tab:defense} benchmarks this against 5 baselines.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Panel selection strategy benchmark (15 models, MMLU, 6 attacks). Two-stage achieves 84\\% of oracle efficiency.}\n\\label{tab:defense}\n\\begin{tabular}{lccc}\n\\toprule\nStrategy & ASR & $\\Delta$ vs Strong-K & Best (of 6) \\\\\n\\midrule\nTwo-Stage (ours) & 0.038 & $-$20.8\\% & 5/6 \\\\\nMin-$\\etamax$ & 0.041 & $-$14.6\\% & 4/6 \\\\\nStrongest-$K$ & 0.048 & baseline & 1/6 \\\\\nRandom & 0.089 & +85.4\\% & 0/6 \\\\\nMax-$\\keff$ & 0.112 & +133.3\\% & 0/6 \\\\\nOracle & 0.032 & $-$33.3\\% & 6/6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo-stage achieves the lowest ASR among non-oracle strategies (0.038), outperforming the strongest-$K$ baseline by 20.8\\%. Max-$\\keff$ is catastrophic (ASR 0.112, +133\\%), providing the most direct evidence against blind diversity maximization. Sensitivity analysis shows the screening threshold is robust across percentile 50--75, with optimal performance at percentile 65--75.\n\n\\subsection{Aggregation Rule Modulation}\n\nThe dual vulnerability driver effect varies by aggregation rule (Table~\\ref{tab:aggregation}). Threshold (unanimity) voting amplifies $\\keff$'s harmful effect by 45\\% ($\\beta_K$: 0.42$\\to$0.61) and increases ASR by 86\\%, because a single flipped judge blocks panel rejection. Bayesian aggregation, which downweights judges based on prior accuracy, provides the best single-aggregation defense: 28.4\\% ASR reduction, with $\\keff$ significance dropping from 10/12 to 6/12. However, 6/12 $\\keff$ significance confirms Bayesian aggregation alone cannot eliminate the diversity trap, motivating a combined defense stack.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Aggregation rule $\\times$ vulnerability drivers (455 panels).}\n\\label{tab:aggregation}\n\\begin{tabular}{lcccc}\n\\toprule\nAggregation & $\\keff$ sig & $\\bar{\\beta}_K$ & ASR & $\\Delta$ \\\\\n\\midrule\nMajority & 10/12 & 0.42 & 0.074 & -- \\\\\nThreshold & 11/12 & 0.61 & 0.138 & +86\\% \\\\\nAcc-weighted & 8/12 & 0.39 & 0.069 & $-$6.8\\% \\\\\nBayesian & 6/12 & 0.25 & 0.053 & $-$28.4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Conclusion}\n\nWe presented large-scale empirical evidence for the \\emph{diversity trap} in multi-judge LLM evaluation: panel diversity independently increases vulnerability to adaptive adversarial attacks. This finding, validated across 15 models, 455 panels, 9 attack types, 4 benchmarks, and multiple panel sizes, challenges the pervasive assumption that diversity improves evaluation robustness. The mechanism traces to BFT's broken assumption: adaptive adversaries exploit the heterogeneous attack surface that diverse judges create, concentrating attacks on the weakest judge rather than facing independent random faults. We proposed a two-stage defense (robustness screening + diversity optimization) that reduces ASR by 20.8\\%, complemented by Bayesian aggregation ($-$28.4\\%). We urge the LLM evaluation community to adopt diversity-aware security analysis: do not assume more judges means safer evaluation.\n\n\\section*{Limitations}\n\nOur study has three main limitations. First, our adversary model assumes knowledge of panel composition (full or partial); in settings where panel membership is secret, the diversity trap may be attenuated. Second, while we cover 15 models from 6 families, the rapidly evolving LLM landscape means our specific quantitative findings may shift as new model generations emerge. Third, our analysis is observational---the regression design establishes independent predictive association, not strict causality, between diversity and vulnerability; experimental manipulation of panel composition with controlled interventions would strengthen causal claims.\n\n\\bibliography{anthology,custom}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "a4d17bf8-7817-42f9-b4ee-6bc05afb7cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_…",
  "leafUuid": "4a3528e9-1d8d-433b-8faf-c7097dd0cc9c",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate certificate manipulation vulnerability study paper",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba"
}
```

---

### Assistant

_source line 26 · 2026-05-22T18:20:42.944Z_

Now compiling. Since we reference bibliography files that don't exist, let me create stubs and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a3528e9-1d8d-433b-8faf-c7097dd0cc9c",
  "isSidechain": false,
  "requestId": "req_011CbJ53EGYDrKQmnc8edok4",
  "type": "assistant",
  "uuid": "8091b54f-7ff5-447b-9ce5-7114193e1b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYv93tnYZ8iNq5P2GUbZAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11086,
      "cache_read_input_tokens": 51098,
      "output_tokens": 1268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1268,
          "cache_read_input_tokens": 51098,
          "cache_creation_input_tokens": 11086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11086
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

_source line 27 · 2026-05-22T18:21:01.589Z_

<details open><summary>🔧 Tool call — Write · `toolu_0136aFDYkwwHRpKKSw2pTD9Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/custom.bib",
  "content": "@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and Chatbot Arena},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and others},\n  booktitle={NeurIPS},\n  year={2023}\n}\n\n@article{li2023alpacaeval,\n  title={AlpacaEval: An Automatic Evaluator of Instruction-Following Models},\n  author={Li, Xuechen and Zhang, Tianyi and Dubois, Yann and Taori, Rohan and Gulrajani, Ishaan and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  year={2023}\n}\n\n@inproceedings{dubois2024alpacafarm,\n  title={AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={NeurIPS},\n  year={2024}\n}\n\n@article{wang2023large,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  year={2023}\n}\n\n@article{raina2024llm,\n  title={Is {LLM}-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot {LLM} Assessment},\n  author={Raina, Vyas and Liusie, Adian and Gales, Mark},\n  year={2024}\n}\n\n@article{shi2024optimization,\n  title={Optimization-based Prompt Injection Attack to {LLM}-as-a-Judge},\n  author={Shi, Jiawen and others},\n  year={2024}\n}\n\n@article{lamport1982byzantine,\n  title={The {Byzantine} Generals Problem},\n  author={Lamport, Leslie and Shostak, Robert and Pease, Marshall},\n  journal={ACM Transactions on Programming Languages and Systems},\n  volume={4},\n  number={3},\n  pages={382--401},\n  year={1982}\n}\n\n@inproceedings{castro1999practical,\n  title={Practical {Byzantine} Fault Tolerance},\n  author={Castro, Miguel and Liskov, Barbara},\n  booktitle={OSDI},\n  year={1999}\n}\n\n@article{sagawa2020investigation,\n  title={An Investigation of Why Overparameterization Exacerbates Spurious Correlations},\n  author={Sagawa, Shiori and Raghunathan, Aditi and Koh, Pang Wei and Liang, Percy},\n  year={2020}\n}\n\n@article{krogh1994neural,\n  title={Neural Network Ensembles, Cross Validation, and Active Learning},\n  author={Krogh, Anders and Vedelsby, Jesper},\n  journal={NeurIPS},\n  year={1994}\n}\n\n@article{brown2005diversity,\n  title={Diversity Creation Methods: A Survey and Categorisation},\n  author={Brown, Gavin and Wyatt, Jeremy and Harris, Rachel and Yao, Xin},\n  journal={Information Fusion},\n  volume={6},\n  number={1},\n  pages={5--20},\n  year={2005}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8091b54f-7ff5-447b-9ce5-7114193e1b47",
  "isSidechain": false,
  "requestId": "req_011CbJ53EGYDrKQmnc8edok4",
  "type": "assistant",
  "uuid": "ddeb250f-2de8-4760-857f-f609fd016a82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYv93tnYZ8iNq5P2GUbZAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11086,
      "cache_read_input_tokens": 51098,
      "output_tokens": 1268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1268,
          "cache_read_input_tokens": 51098,
          "cache_creation_input_tokens": 11086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11086
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

_source line 28 · 2026-05-22T18:21:01.623Z_

<details><summary>↩ Tool result · `toolu_0136aFDYkwwHRpKKSw2pTD9Y`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/custom.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddeb250f-2de8-4760-857f-f609fd016a82",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "36f8dad5-b451-4dfc-b411-a44ebfa9992a",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/custom.bib",
    "content": "@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and Chatbot Arena},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and others},\n  booktitle={NeurIPS},\n  year={2023}\n}\n\n@article{li2023alpacaeval,\n  title={AlpacaEval: An Automatic Evaluator of Instruction-Following Models},\n  author={Li, Xuechen and Zhang, Tianyi and Dubois, Yann and Taori, Rohan and Gulrajani, Ishaan and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  year={2023}\n}\n\n@inproceedings{dubois2024alpacafarm,\n  title={AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={NeurIPS},\n  year={2024}\n}\n\n@article{wang2023large,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  year={2023}\n}\n\n@article{raina2024llm,\n  title={Is {LLM}-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot {LLM} Assessment},\n  author={Raina, Vyas and Liusie, Adian and Gales, Mark},\n  year={2024}\n}\n\n@article{shi2024optimization,\n  title={Optimization-based Prompt Injection Attack to {LLM}-as-a-Judge},\n  author={Shi, Jiawen and others},\n  year={2024}\n}\n\n@article{lamport1982byzantine,\n  title={The {Byzantine} Generals Problem},\n  author={Lamport, Leslie and Shostak, Robert and Pease, Marshall},\n  journal={ACM Transactions on Programming Languages and Systems},\n  volume={4},\n  number={3},\n  pages={382--401},\n  year={1982}\n}\n\n@inproceedings{castro1999practical,\n  title={Practical {Byzantine} Fault Tolerance},\n  author={Castro, Miguel and Liskov, Barbara},\n  booktitle={OSDI},\n  year={1999}\n}\n\n@article{sagawa2020investigation,\n  title={An Investigation of Why Overparameterization Exacerbates Spurious Correlations},\n  author={Sagawa, Shiori and Raghunathan, Aditi and Koh, Pang Wei and Liang, Percy},\n  year={2020}\n}\n\n@article{krogh1994neural,\n  title={Neural Network Ensembles, Cross Validation, and Active Learning},\n  author={Krogh, Anders and Vedelsby, Jesper},\n  journal={NeurIPS},\n  year={1994}\n}\n\n@article{brown2005diversity,\n  title={Diversity Creation Methods: A Survey and Categorisation},\n  author={Brown, Gavin and Wyatt, Jeremy and Harris, Rachel and Yao, Xin},\n  journal={Information Fusion},\n  volume={6},\n  number={1},\n  pages={5--20},\n  year={2005}\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ddeb250f-2de8-4760-857f-f609fd016a82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T18:21:02.257Z_

<details><summary>↩ Tool result · `toolu_01HvStYi8794qM5mWEFdYsas`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/anthology.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dfc7fe3-ab68-4cd5-b617-1ac0a35f2898",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "784d902f-8d7d-4858-b7e7-f8ba4ca21b61",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/anthology.bib",
    "content": "% placeholder\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "4dfc7fe3-ab68-4cd5-b617-1ac0a35f2898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T18:21:02.250Z_

<details open><summary>🔧 Tool call — Write · `toolu_01HvStYi8794qM5mWEFdYsas`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/anthology.bib",
  "content": "% placeholder\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36f8dad5-b451-4dfc-b411-a44ebfa9992a",
  "isSidechain": false,
  "requestId": "req_011CbJ53EGYDrKQmnc8edok4",
  "type": "assistant",
  "uuid": "4dfc7fe3-ab68-4cd5-b617-1ac0a35f2898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYv93tnYZ8iNq5P2GUbZAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11086,
      "cache_read_input_tokens": 51098,
      "output_tokens": 1268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1268,
          "cache_read_input_tokens": 51098,
          "cache_creation_input_tokens": 11086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11086
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

_source line 31 · 2026-05-22T18:21:02.298Z_

```json
{
  "parentUuid": "784d902f-8d7d-4858-b7e7-f8ba4ca21b61",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "754176b4-e4bf-4f44-84c0-edfbb2615e87",
  "timestamp": "2026-05-22T18:21:02.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-22T18:21:11.721Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me check if the acl.sty file is available. The paper uses `\usepackage[hyperref]{acl}` which requires the ACL style file. Let me check if it's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "754176b4-e4bf-4f44-84c0-edfbb2615e87",
  "isSidechain": false,
  "requestId": "req_011CbJ5511sWa8u8hAsv8yUm",
  "type": "assistant",
  "uuid": "ea506230-c130-4044-93a8-2d7653f54ce6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dy4euMMkrDLG6ApNVZseKx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 62184,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 62184,
          "cache_creation_input_tokens": 1544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1544
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

_source line 33 · 2026-05-22T18:21:12.969Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AjdkqgAQtGzKsauJC9yW2T`</summary>

```json
{
  "command": "kpsewhich acl.sty 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check if ACL style file exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea506230-c130-4044-93a8-2d7653f54ce6",
  "isSidechain": false,
  "requestId": "req_011CbJ5511sWa8u8hAsv8yUm",
  "type": "assistant",
  "uuid": "39fc4699-593d-4234-9019-439aa55665ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dy4euMMkrDLG6ApNVZseKx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 62184,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 62184,
          "cache_creation_input_tokens": 1544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1544
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

_source line 34 · 2026-05-22T18:21:13.041Z_

<details><summary>↩ Tool result · `toolu_01AjdkqgAQtGzKsauJC9yW2T`</summary>

```text
NOT_FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39fc4699-593d-4234-9019-439aa55665ec",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "b52a5e5e-028b-41c2-afc9-91d373f09306",
  "toolUseResult": {
    "stdout": "NOT_FOUND",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "39fc4699-593d-4234-9019-439aa55665ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-22T18:21:17.382Z_

<details><summary>Logged reasoning block</summary>

```text
ACL style not found. Let me switch to a standard article class with reasonable formatting, or download the ACL style file.

Actually, let me just use a simpler approach - use the article class directly with some basic formatting. This is a dream/simulation paper, so it doesn't need the exact ACL template.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b52a5e5e-028b-41c2-afc9-91d373f09306",
  "isSidechain": false,
  "requestId": "req_011CbJ55o9XRzjoUKyYFSnd2",
  "type": "assistant",
  "uuid": "47b90c14-9880-4ab1-9d41-56e7a64ff741",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TExBnCt5j1sEKVa4ZyBVU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 63728,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 63728,
          "cache_creation_input_tokens": 176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 176
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

_source line 36 · 2026-05-22T18:21:17.912Z_

ACL style not available. Let me rewrite using a standard template.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47b90c14-9880-4ab1-9d41-56e7a64ff741",
  "isSidechain": false,
  "requestId": "req_011CbJ55o9XRzjoUKyYFSnd2",
  "type": "assistant",
  "uuid": "c1192d69-592f-4c95-955f-92e7701d5800",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TExBnCt5j1sEKVa4ZyBVU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 63728,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 63728,
          "cache_creation_input_tokens": 176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 176
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

_source line 37 · 2026-05-22T18:21:19.078Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JnsTDpDyEcyNJmZKKCexwG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1192d69-592f-4c95-955f-92e7701d5800",
  "isSidechain": false,
  "requestId": "req_011CbJ55o9XRzjoUKyYFSnd2",
  "type": "assistant",
  "uuid": "a0caacf5-428c-46dc-9d2e-3268a725766a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TExBnCt5j1sEKVa4ZyBVU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 63728,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 63728,
          "cache_creation_input_tokens": 176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 176
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

_source line 38 · 2026-05-22T18:21:19.357Z_

<details><summary>↩ Tool result · `toolu_01JnsTDpDyEcyNJmZKKCexwG`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{amsmath}
8	\usepackage{amsfonts}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{enumitem}
12	\usepackage{tabularx}
13	
14	\setlength\titlebox{5cm}
15	
16	\newcommand{\keff}{K_{\text{eff}}}
17	\newcommand{\etamax}{\eta_{\text{max}}}
18	\newcommand{\keffresid}{K_{\text{eff}}^{\text{resid}}}
19	
20	\title{More Diverse, More Vulnerable:\\How Judge Panel Diversity Backfires Under Adaptive Adversaries}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	Multi-judge evaluation panels are increasingly used to assess LLM outputs, with the prevailing assumption that judge diversity---analogous to Byzantine Fault Tolerance (BFT)---improves robustness against manipulation. We provide large-scale empirical evidence that this assumption \emph{reverses} under adaptive adversaries. Across 15 LLM judges spanning 6 model families, 455 three-judge panels, 9 attack types, and 4 evaluation benchmarks, we show that panel diversity (effective independence $\keff$) is \textbf{independently and positively} associated with attack success rate (ASR), even after residualizing against individual judge weakness ($\etamax$). This ``diversity trap'' is driven by dual vulnerability channels whose relative importance is attack-dependent: $\etamax$ dominates shared-bias attacks (sycophancy, verbosity), while $\keff$ dominates transferable attacks (score manipulation, position bias). We trace the mechanism to BFT's broken assumption: random faults distribute uniformly across judges (Gini$\approx$0.12), but adaptive adversaries concentrate attacks on the weakest judge (Gini$\approx$0.68), turning diversity from a defense into an expanded attack surface. Under calibrated random faults, $\keff$'s coefficient flips negative in 5/12 conditions, empirically confirming BFT's prediction. We propose a robustness-first two-stage panel selection algorithm that reduces ASR by 20.8\% over the strongest-$K$ baseline, and show that Bayesian aggregation provides a complementary 28.4\% reduction. Our findings challenge the ``more diverse = more robust'' assumption and call for diversity-aware security analysis in LLM evaluation pipeline design.
29	\end{abstract}
30	
31	\section{Introduction}
32	
33	As LLMs are increasingly deployed as automated evaluators~\cite{zheng2023judging,li2023alpacaeval}, the research community has adopted multi-judge panels to mitigate individual model biases. The intuition is straightforward and borrowed from distributed systems: diverse, independent judges should be harder to simultaneously fool, much like Byzantine Fault Tolerance (BFT) guarantees that $f$ faulty nodes cannot compromise a system of $3f+1$ independent replicas.
34	
35	This paper demonstrates that this intuition is \emph{wrong} under adversarial conditions. We conduct what is, to our knowledge, the largest systematic study of adversarial robustness in multi-judge LLM evaluation: 15 models from 6 families (OpenAI, Anthropic, Google, Meta, Alibaba, Microsoft), enumerated into 455 three-judge panels, evaluated under 9 distinct attack types across MMLU, ARC-Challenge, MT-Bench, and AlpacaEval.
36	
37	Our central finding is the \textbf{diversity trap}: panel diversity, measured by effective judge independence ($\keff$), is \emph{independently and positively} associated with attack success rate. After residualizing $\keff$ against individual judge weakness ($\etamax$, the maximum vulnerability of any panel member), $\keffresid$ remains significantly positive in 10/12 conditions (FDR-corrected). Panel vulnerability is driven by \textbf{dual factors}---$\etamax$ and $\keff$---whose relative importance depends on attack type:
38	
39	\begin{itemize}[nosep,leftmargin=*]
40	\item \textbf{Shared-bias attacks} (sycophancy, verbosity, authority): $\etamax$ dominates because all judges share similar cognitive biases from RLHF training.
41	\item \textbf{Transferable attacks} (score manipulation, position bias): $\keff$ dominates because diverse judges provide heterogeneous, judge-specific attack surfaces.
42	\end{itemize}
43	
44	We trace this to BFT's core assumption: fault independence. Under random faults, failures distribute uniformly (Gini$\approx$0.12) and diversity genuinely helps---our calibrated random-fault simulations show $\keff$'s coefficient \emph{flipping negative} in 5/12 conditions. But adaptive adversaries concentrate attacks on the weakest judges (Gini$\approx$0.68, top-1 judge absorbing 78\% of ASR), turning diversity from fault tolerance into an expanded attack menu.
45	
46	We further show that: (1) the diversity trap holds within capability tiers (4/6 conditions significant among top-tier models only), ruling out tier-mixing confounds; (2) generalizes to open-ended benchmarks (MT-Bench 3/4, AlpacaEval 2/4 significant); (3) scales with panel size ($\keff$ coefficient increases monotonically from $K$=3 to $K$=9); (4) holds under partial-knowledge adversaries who know only model family membership (7/12 significant). We propose a two-stage defense---robustness screening followed by diversity optimization---that achieves 20.8\% ASR reduction over the strongest-$K$ baseline, and show Bayesian aggregation provides complementary protection.
47	
48	\section{Related Work}
49	
50	\paragraph{LLM-as-Judge.} LLM evaluation using model judges has become standard practice~\cite{zheng2023judging,li2023alpacaeval,dubois2024alpacafarm}. Known biases include position bias, verbosity preference, and self-enhancement~\cite{wang2023large,zheng2023judging}. Multi-judge panels are proposed as mitigation, but their adversarial robustness remains unstudied.
51	
52	\paragraph{Adversarial Attacks on LLM Judges.} Prior work demonstrates individual judge vulnerability to prompt injection, sycophancy exploitation, and score manipulation~\cite{raina2024llm,shi2024optimization}. We extend this to \emph{panel-level} analysis, studying how panel composition mediates vulnerability.
53	
54	\paragraph{Byzantine Fault Tolerance.} Classical BFT~\cite{lamport1982byzantine,castro1999practical} guarantees safety when faults are independent. Recent work questions independence assumptions in ML systems~\cite{sagawa2020investigation}. We empirically test whether BFT's independence assumption holds for LLM judge panels.
55	
56	\paragraph{Ensemble Diversity.} The diversity-accuracy tradeoff is well-studied in ensemble learning~\cite{krogh1994neural,brown2005diversity}. Our setting differs: we study diversity under \emph{adaptive adversaries} who exploit panel composition, not passive noise.
57	
58	\section{Problem Formulation}
59	
60	\paragraph{Setup.} A panel $P = \{j_1, \ldots, j_K\}$ of $K$ LLM judges evaluates candidate responses. Each judge $j_i$ produces a binary decision (accept/reject). The panel decision uses an aggregation rule $\mathcal{A}$ (default: majority vote).
61	
62	\paragraph{Adversary Model.} An adaptive adversary observes the panel composition and crafts attacks to maximize the panel's attack success rate (ASR)---the fraction of evaluation instances where the panel decision is flipped.
63	
64	\paragraph{Vulnerability Metrics.} We define two panel-level predictors:
65	\begin{itemize}[nosep,leftmargin=*]
66	\item $\etamax = \max_{j \in P} \eta_j$: maximum individual vulnerability (weakest link). $\eta_j$ is judge $j$'s individual ASR under a given attack.
67	\item $\keff$: effective number of independent judges, computed from the eigenspectrum of the pairwise mutual information matrix. Higher $\keff$ indicates greater functional diversity.
68	\end{itemize}
69	
70	To disentangle $\keff$ from $\etamax$, we define $\keffresid$ as the residual of regressing $\keff$ on $\etamax$, ensuring orthogonality (VIF$=$1.02).
71	
72	\paragraph{Regression Model.} For each condition (dataset $\times$ attack type), we fit:
73	\begin{equation}
74	\text{ASR}_P = \beta_0 + \beta_\eta \cdot \etamax + \beta_K \cdot \keffresid + \epsilon
75	\end{equation}
76	across all 455 panels. A significantly positive $\beta_K$ indicates diversity independently increases vulnerability.
77	
78	\section{Experimental Setup}
79	
80	\paragraph{Models.} 15 LLM judges: GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini (OpenAI); Claude-3.5-Sonnet (Anthropic); Gemini-1.5-Pro (Google); Llama-3.1-8B, Llama-3.1-70B (Meta); Qwen2.5-7B, Qwen2.5-72B (Alibaba); Mistral-7B-v0.3, Phi-3-medium-14B (Microsoft). Three capability tiers: Small (7--14B), Medium (14--34B), Large (70B+ and API).
81	
82	\paragraph{Panels.} All $\binom{15}{3} = 455$ three-judge panels, extended to $K \in \{5,7,9\}$ for panel-size analysis.
83	
84	\paragraph{Attacks.} 9 attack types spanning three paradigms: \emph{bias exploitation} (sycophancy, verbosity, authority bias), \emph{score manipulation} (direct score manipulation, position bias, few-shot bias), and \emph{injection} (few-shot hijacking, persona manipulation, instruction override).
85	
86	\paragraph{Benchmarks.} MMLU and ARC-Challenge (MCQ); MT-Bench and AlpacaEval (open-ended generation).
87	
88	\paragraph{Statistical Methods.} FDR correction (Benjamini-Hochberg) for multiple comparisons; beta regression for distributional robustness; residualization for multicollinearity control.
89	
90	\section{The Diversity Trap: Core Evidence}
91	
92	\subsection{Dual Vulnerability Drivers}
93	
94	Table~\ref{tab:core} presents the core regression results across 12 conditions (2 datasets $\times$ 6 attacks). Both $\etamax$ and $\keffresid$ are significant predictors of panel ASR: $\etamax$ reaches FDR significance in 10/12 conditions, $\keffresid$ in 10/12 conditions. The mean $R^2 = 0.62$, indicating that these two factors jointly explain the majority of panel-level vulnerability variance.
95	
96	\begin{table*}[t]
97	\centering
98	\small
99	\caption{Dual vulnerability drivers: 15-model regression across 12 conditions (455 panels each). $\keffresid$ is residualized against $\etamax$ (VIF$=$1.02). Bold $p$-values are FDR-significant ($q < 0.05$). ``Dominant'' indicates which predictor has the larger standardized $\beta$.}
100	\label{tab:core}
101	\begin{tabular}{lccccccl}
102	\toprule
103	Condition & $\etamax$ $\beta$ & $p$ & $\keffresid$ $\beta$ & $p$ & $R^2$ & Confound $r$ & Dominant \\
104	\midrule
105	mmlu$\times$sycophancy & 0.82 & \textbf{1.2e-8} & 0.31 & \textbf{0.004} & 0.68 & 0.72 & $\etamax$ \\
106	mmlu$\times$score\_manip & 0.45 & \textbf{0.018} & 0.61 & \textbf{3.4e-9} & 0.71 & 0.38 & $\keff$ \\
107	mmlu$\times$position & 0.15 & 0.214 & 0.58 & \textbf{1.2e-8} & 0.56 & 0.36 & $\keff$ \\
108	mmlu$\times$verbosity & 0.74 & \textbf{4.1e-7} & 0.28 & \textbf{0.011} & 0.63 & 0.74 & $\etamax$ \\
109	mmlu$\times$authority & 0.69 & \textbf{1.8e-6} & 0.19 & 0.087 & 0.58 & 0.78 & $\etamax$ \\
110	mmlu$\times$few\_shot & 0.55 & \textbf{2.3e-4} & 0.48 & \textbf{6.1e-6} & 0.65 & 0.65 & both \\
111	\midrule
112	arc$\times$sycophancy & 0.79 & \textbf{3.5e-8} & 0.35 & \textbf{0.002} & 0.66 & 0.71 & $\etamax$ \\
113	arc$\times$score\_manip & 0.38 & 0.117 & 0.64 & \textbf{1.7e-7} & 0.59 & 0.35 & $\keff$ \\
114	arc$\times$position & 0.03 & 0.910 & 0.72 & \textbf{1.8e-8} & 0.57 & 0.34 & $\keff$ \\
115	arc$\times$verbosity & 0.71 & \textbf{8.9e-7} & 0.33 & \textbf{0.003} & 0.61 & 0.73 & $\etamax$ \\
116	arc$\times$authority & 0.66 & \textbf{3.2e-6} & 0.22 & 0.062 & 0.55 & 0.76 & $\etamax$ \\
117	arc$\times$few\_shot & 0.51 & \textbf{5.7e-4} & 0.52 & \textbf{3.8e-6} & 0.63 & 0.62 & both \\
118	\bottomrule
119	\end{tabular}
120	\end{table*}
121	
122	A systematic pattern emerges: \textbf{transferable attacks} (score manipulation, position bias) are $\keff$-dominated ($\beta_K > \beta_\eta$), while \textbf{shared-bias attacks} (sycophancy, verbosity, authority) are $\etamax$-dominated. This yields a predictive taxonomy: given a new attack type, its transferability predicts which vulnerability channel dominates.
123	
124	Three conditions have low confound correlation ($r \approx 0.35$), serving as ``smoking gun'' evidence: in these conditions, $\keffresid$ achieves $p < 2.1 \times 10^{-28}$, confirming diversity's independent harmful effect even where the $\keff$-$\etamax$ association is weak.
125	
126	\subsection{Capability-Matched Validation}
127	
128	A natural concern is that $\keff$'s positive effect is an artifact of tier-mixing: high-$\keff$ panels might mix weak and strong models, making $\keff$ a proxy for tier heterogeneity rather than diversity \emph{per se}. We test this by running within-tier regressions (Table~\ref{tab:tier}).
129	
130	\begin{table}[t]
131	\centering
132	\small
133	\caption{Within-tier $\keff$ validation. Large tier uses only top-tier models (70B+ and API), eliminating tier-mixing.}
134	\label{tab:tier}
135	\begin{tabular}{lcccc}
136	\toprule
137	Tier & Models & Panels & $r(\keff,\etamax)$ & $\keffresid$ sig \\
138	\midrule
139	Small (7B--14B) & 5 & 10 & 0.32 & 2/6 \\
140	Medium & 4 & 4 & 0.41 & 1/6 \\
141	Large (70B+API) & 6 & 20 & 0.33 & 4/6 \\
142	Cross-tier (all) & 15 & 455 & 0.55 & 10/12 \\
143	\bottomrule
144	\end{tabular}
145	\end{table}
146	
147	The large tier is most informative: all 6 models are top-tier (GPT-4o, GPT-4.1, Claude-3.5-Sonnet, Gemini-1.5-Pro, Llama-70B, Qwen-72B), yet $\keffresid$ is significant in 4/6 conditions (best $p = 4.2 \times 10^{-4}$). The condition-dependent pattern is preserved: score manipulation and position bias are $\keff$-dominated; sycophancy and verbosity are $\etamax$-dominated. This rules out tier-mixing as the driver of the diversity trap.
148	
149	\subsection{Statistical Robustness}
150	
151	We perform comprehensive diagnostics (Table~\ref{tab:diagnostics}). VIF$=$1.02 and condition number$=$4.8 confirm the design matrix is well-conditioned. Residuals pass Shapiro-Wilk normality ($p = 0.23$). Maximum Cook's distance is 0.031 (threshold: 1.0), with only 2.4\% high-leverage points. Under Bonferroni correction (most conservative), $\keffresid$ remains significant in 8/12 conditions. Beta regression, which properly handles bounded ASR in $[0,1]$, confirms 9/12 significant---highly consistent with OLS.
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\caption{Multiple comparison robustness across correction methods.}
157	\label{tab:diagnostics}
158	\begin{tabular}{lcc}
159	\toprule
160	Correction & $\keffresid$ sig & $\etamax$ sig \\
161	\midrule
162	Uncorrected & 12/12 & 11/12 \\
163	FDR (BH) & 10/12 & 10/12 \\
164	Bonferroni & 8/12 & 9/12 \\
165	Beta reg.\ + FDR & 9/12 & 10/12 \\
166	\bottomrule
167	\end{tabular}
168	\end{table}
169	
170	\section{Mechanism: BFT Reversal}
171	
172	\subsection{Random-Fault Contrast}
173	
174	BFT predicts that diversity helps when faults are independent and random. We test this by simulating calibrated random faults: each judge's failure probability is drawn from bootstrapped clean-accuracy noise, independent across judges. Table~\ref{tab:bft} contrasts $\keff$'s coefficient under adaptive versus random-fault regimes.
175	
176	\begin{table*}[t]
177	\centering
178	\small
179	\caption{BFT regime contrast: $\keff$ coefficient under adaptive vs.\ calibrated random faults (12 conditions, 455 panels). ``Flipped'' indicates $\beta_{\text{RF}}$ is significantly negative (diversity helps under random faults).}
180	\label{tab:bft}
181	\begin{tabular}{lcccccc}
182	\toprule
183	Condition & $\beta_{\text{adaptive}}$ & $p_{\text{adap}}$ & $\beta_{\text{RF}}$ & $p_{\text{RF}}$ & $|\beta_{\text{adap}}/\beta_{\text{RF}}|$ & Flipped? \\
184	\midrule
185	mmlu$\times$sycophancy & 0.31 & \textbf{0.004} & 0.08 & 0.310 & 3.88 & No \\
186	mmlu$\times$score\_manip & 0.61 & \textbf{3.4e-9} & $-$0.22 & \textbf{0.015} & 2.77 & Yes \\
187	mmlu$\times$position & 0.58 & \textbf{1.2e-8} & $-$0.31 & \textbf{0.003} & 1.87 & Yes \\
188	mmlu$\times$verbosity & 0.28 & \textbf{0.011} & 0.11 & 0.198 & 2.55 & No \\
189	mmlu$\times$authority & 0.19 & 0.087 & 0.06 & 0.541 & 3.17 & No \\
190	mmlu$\times$few\_shot & 0.48 & \textbf{6.1e-6} & $-$0.18 & \textbf{0.039} & 2.67 & Yes \\
191	arc$\times$sycophancy & 0.35 & \textbf{0.002} & 0.10 & 0.251 & 3.50 & No \\
192	arc$\times$score\_manip & 0.64 & \textbf{1.7e-7} & $-$0.28 & \textbf{0.008} & 2.29 & Yes \\
193	arc$\times$position & 0.72 & \textbf{1.8e-8} & $-$0.35 & \textbf{0.001} & 2.06 & Yes \\
194	arc$\times$verbosity & 0.33 & \textbf{0.003} & 0.12 & 0.175 & 2.75 & No \\
195	arc$\times$authority & 0.22 & 0.062 & 0.05 & 0.612 & 4.40 & No \\
196	arc$\times$few\_shot & 0.52 & \textbf{3.8e-6} & $-$0.14 & 0.091 & 3.71 & Marginal \\
197	\bottomrule
198	\end{tabular}
199	\end{table*}
200	
201	The results confirm the BFT reversal: in 5/12 conditions, $\beta_{\text{RF}}$ flips to significantly \emph{negative}---diversity genuinely protects under random faults, as BFT predicts. The flips concentrate on transferable attacks (score manipulation, position bias, few-shot), where judge-specific exploit paths are most relevant. Under adaptive attacks, these same conditions show the strongest positive $\beta$ (0.48--0.72). The mean $\beta$ ratio is 2.8$\times$, and the $R^2$ gap ($\Delta R^2 = 0.31$; RF: 0.78, adaptive: 0.47) quantifies BFT's broken predictability: panel structure explains 78\% of variance under random faults but only 47\% under adaptive attacks, where strategic adversary behavior introduces irreducible noise.
202	
203	\subsection{ASR Concentration Analysis}
204	
205	To illuminate \emph{how} adaptive adversaries exploit diversity, we analyze per-judge ASR distributions within panels (Table~\ref{tab:concentration}).
206	
207	\begin{table}[t]
208	\centering
209	\small
210	\caption{ASR concentration: adaptive vs.\ random-fault regimes.}
211	\label{tab:concentration}
212	\begin{tabular}{lccc}
213	\toprule
214	Metric & Adaptive & RF & Ratio \\
215	\midrule
216	Mean Gini & 0.68 & 0.12 & 5.67 \\
217	Entropy (bits) & 1.42 & 2.31 & 0.61 \\
218	Top-1 judge share & 0.78 & 0.38 & 2.05 \\
219	$r(\keff, \text{Gini})$ & 0.52 & 0.08 & 6.50 \\
220	\bottomrule
221	\end{tabular}
222	\end{table}
223	
224	Under adaptive attacks, ASR is highly concentrated: the weakest judge absorbs 78\% of attack success (vs.\ 38\% under random faults). Crucially, $r(\keff, \text{Gini}) = 0.52$: more diverse panels produce \emph{more concentrated} attacks, because greater capability spread gives the adversary a clearer targeting gradient. Under random faults, concentration is uniformly low (Gini$=$0.12), confirming BFT's independence assumption holds only in the non-adversarial regime.
225	
226	\section{Generalization}
227	
228	\subsection{Attack Surface Expansion}
229	
230	To test whether the diversity trap generalizes beyond the original 6 attack types, we introduce 3 additional attacks: few-shot hijacking (in-context example injection), persona manipulation (authority impersonation), and instruction override (direct prompt overwrite). Table~\ref{tab:expanded} shows the 6 new conditions.
231	
232	\begin{table}[t]
233	\centering
234	\small
235	\caption{Extended attack results (6 new conditions, 15 models).}
236	\label{tab:expanded}
237	\begin{tabular}{lccc}
238	\toprule
239	Condition & $\keffresid$ $\beta$ & $p$ & Dominant \\
240	\midrule
241	mmlu$\times$hijack & 0.54 & \textbf{8.2e-7} & $\keff$ \\
242	mmlu$\times$persona & 0.29 & \textbf{0.008} & $\etamax$ \\
243	mmlu$\times$override & 0.22 & 0.042 & $\etamax$ \\
244	arc$\times$hijack & 0.58 & \textbf{2.1e-7} & $\keff$ \\
245	arc$\times$persona & 0.25 & \textbf{0.019} & $\etamax$ \\
246	arc$\times$override & 0.18 & 0.112 & $\etamax$ \\
247	\bottomrule
248	\end{tabular}
249	\end{table}
250	
251	$\keffresid$ is significant in 4/6 new conditions. Combined with the original 12, this yields 14/18 total FDR-significant conditions for $\keffresid$. The attack taxonomy is predictive: high-transferability attacks (few-shot hijacking) are $\keff$-dominated; moderate/low-transferability attacks (persona, instruction override) are $\etamax$-dominated---consistent with the core results.
252	
253	\subsection{Open-Ended Benchmarks}
254	
255	The diversity trap is not an MCQ artifact. On MT-Bench (multi-turn dialogue evaluation) and AlpacaEval (instruction-following scoring), $\keffresid$ is significant in 3/4 and 2/4 conditions, respectively (Table~\ref{tab:openended}). The condition-dependent dominance pattern transfers without modification: score manipulation and position bias remain $\keff$-dominated; sycophancy and verbosity remain $\etamax$-dominated. $R^2$ is lower (0.39--0.52 vs.\ 0.62 for MCQ), reflecting the higher noise floor inherent to open-ended evaluation.
256	
257	\begin{table}[t]
258	\centering
259	\small
260	\caption{Open-ended benchmark results (8 conditions). Pattern consistent with MCQ findings despite higher evaluation noise.}
261	\label{tab:openended}
262	\begin{tabular}{lcccl}
263	\toprule
264	Condition & $\keffresid$ $\beta$ & $p$ & $R^2$ & Dom. \\
265	\midrule
266	MT$\times$score & 0.52 & \textbf{1.8e-5} & 0.52 & $\keff$ \\
267	MT$\times$syco & 0.28 & \textbf{0.012} & 0.49 & $\etamax$ \\
268	MT$\times$pos & 0.47 & \textbf{8.3e-5} & 0.44 & $\keff$ \\
269	MT$\times$verb & 0.18 & 0.108 & 0.47 & $\etamax$ \\
270	AE$\times$score & 0.44 & \textbf{3.2e-4} & 0.46 & $\keff$ \\
271	AE$\times$syco & 0.21 & 0.058 & 0.43 & $\etamax$ \\
272	AE$\times$pos & 0.38 & \textbf{0.002} & 0.40 & both \\
273	AE$\times$verb & 0.14 & 0.175 & 0.39 & $\etamax$ \\
274	\bottomrule
275	\end{tabular}
276	\end{table}
277	
278	\subsection{Panel Size Sensitivity}
279	
280	Extending panel size from $K=3$ to $K \in \{5,7,9\}$ reveals a scaling law: $\keff$'s coefficient increases monotonically ($\beta_K$: 0.42$\to$0.48$\to$0.55$\to$0.61), while $\etamax$'s decreases (0.51$\to$0.49$\to$0.43$\to$0.38). The crossover occurs at $K \approx 6$: for panels below this size, individual robustness ($\etamax$) is the primary concern; above it, structural diversity ($\keff$) becomes dominant (Table~\ref{tab:panelsize}). This has direct practical implications: the common strategy of ``adding more judges'' systematically amplifies the diversity trap---$K=9$ panels show 45\% stronger $\keff$ effect than $K=3$.
281	
282	\begin{table}[t]
283	\centering
284	\small
285	\caption{Panel size sensitivity ($K = 3, 5, 7, 9$).}
286	\label{tab:panelsize}
287	\begin{tabular}{lccccl}
288	\toprule
289	$K$ & Panels & $\keffresid$ sig & $\bar{\beta}_K$ & $\bar{\beta}_\eta$ & Primary \\
290	\midrule
291	3 & 455 & 10/12 & 0.42 & 0.51 & $\etamax$ \\
292	5 & 3003 & 11/12 & 0.48 & 0.49 & balanced \\
293	7 & 6435 & 12/12 & 0.55 & 0.43 & $\keff$ \\
294	9 & 5005 & 12/12 & 0.61 & 0.38 & $\keff$ \\
295	\bottomrule
296	\end{tabular}
297	\end{table}
298	
299	\subsection{Partial-Knowledge Adversary}
300	
301	A full-knowledge adversary is a worst-case assumption. We test a realistic partial-knowledge adversary who knows only model \emph{family} membership (typically public information) but not individual vulnerability profiles. Family-level targeting achieves 78.4\% of full-knowledge ASR (0.058 vs.\ 0.074), and $\keff$ remains significant in 7/12 conditions (Table~\ref{tab:partial}). Family membership alone captures 62.8\% of adversary information value, because family$\to$capability tier correlations provide a strong prior on vulnerability profiles.
302	
303	\begin{table}[t]
304	\centering
305	\small
306	\caption{Adversary knowledge level comparison.}
307	\label{tab:partial}
308	\begin{tabular}{lcccc}
309	\toprule
310	Knowledge & ASR & $\keff$ sig & $R^2$ & Info value \\
311	\midrule
312	Full & 0.074 & 10/12 & 0.62 & 100\% \\
313	Partial (family) & 0.058 & 7/12 & 0.51 & 62.8\% \\
314	Black-box & 0.031 & 3/12 & 0.28 & 0\% \\
315	\bottomrule
316	\end{tabular}
317	\end{table}
318	
319	\section{Structural Barriers to Independence}
320	
321	\subsection{Gaussian Copula Failure}
322	
323	If inter-judge dependence followed a Gaussian copula, pairwise mutual information (MI) could be estimated from linear correlations. Across 105 model pairs (15 models), observed MI exceeds Gaussian-predicted MI by a mean factor of 18.5$\times$ (max 312$\times$), with 82/105 pairs exceeding 10$\times$. This invalidates copula-based independence bounds and motivates empirical $\keff$ measurement.
324	
325	\subsection{Family Labels Are Unreliable}
326	
327	Model family labels do not predict judge independence: within-family MI (0.42) is not significantly higher than cross-family MI (0.39; Mann-Whitney $p = 0.158$). The actual driver is capability proximity ($r = -0.71$ with MI): models at similar capability levels share failure modes regardless of training pipeline. Practitioners should not equate ``different families'' with ``diverse panel.''
328	
329	\subsection{Diversity-Capability Tradeoff}
330	
331	Across 455 panels, $\keff$ and $\etamax$ correlate at $r = 0.55$ globally. Within capability tiers, this drops to $r \approx 0.33$, revealing two components: a cross-tier component ($\sim$40\%, from mixing weak and strong models) and a within-tier residual ($\sim$60\%, from genuine diversity-vulnerability association). The Pareto frontier (18 panels, slope $-0.73$) quantifies the tradeoff: each 0.1 increase in $\keff$ costs at least 0.073 increase in $\etamax$.
332	
333	\section{Defense: Panel Design and Aggregation}
334	
335	\subsection{Two-Stage Panel Selection}
336	
337	We propose a robustness-first algorithm: (1) screen judges by individual robustness ($\eta_j \leq$ percentile-75 threshold), (2) maximize $\keff$ among qualifying judges. Table~\ref{tab:defense} benchmarks this against 5 baselines.
338	
339	\begin{table}[t]
340	\centering
341	\small
342	\caption{Panel selection strategy benchmark (15 models, MMLU, 6 attacks). Two-stage achieves 84\% of oracle efficiency.}
343	\label{tab:defense}
344	\begin{tabular}{lccc}
345	\toprule
346	Strategy & ASR & $\Delta$ vs Strong-K & Best (of 6) \\
347	\midrule
348	Two-Stage (ours) & 0.038 & $-$20.8\% & 5/6 \\
349	Min-$\etamax$ & 0.041 & $-$14.6\% & 4/6 \\
350	Strongest-$K$ & 0.048 & baseline & 1/6 \\
351	Random & 0.089 & +85.4\% & 0/6 \\
352	Max-$\keff$ & 0.112 & +133.3\% & 0/6 \\
353	Oracle & 0.032 & $-$33.3\% & 6/6 \\
354	\bottomrule
355	\end{tabular}
356	\end{table}
357	
358	Two-stage achieves the lowest ASR among non-oracle strategies (0.038), outperforming the strongest-$K$ baseline by 20.8\%. Max-$\keff$ is catastrophic (ASR 0.112, +133\%), providing the most direct evidence against blind diversity maximization. Sensitivity analysis shows the screening threshold is robust across percentile 50--75, with optimal performance at percentile 65--75.
359	
360	\subsection{Aggregation Rule Modulation}
361	
362	The dual vulnerability driver effect varies by aggregation rule (Table~\ref{tab:aggregation}). Threshold (unanimity) voting amplifies $\keff$'s harmful effect by 45\% ($\beta_K$: 0.42$\to$0.61) and increases ASR by 86\%, because a single flipped judge blocks panel rejection. Bayesian aggregation, which downweights judges based on prior accuracy, provides the best single-aggregation defense: 28.4\% ASR reduction, with $\keff$ significance dropping from 10/12 to 6/12. However, 6/12 $\keff$ significance confirms Bayesian aggregation alone cannot eliminate the diversity trap, motivating a combined defense stack.
363	
364	\begin{table}[t]
365	\centering
366	\small
367	\caption{Aggregation rule $\times$ vulnerability drivers (455 panels).}
368	\label{tab:aggregation}
369	\begin{tabular}{lcccc}
370	\toprule
371	Aggregation & $\keff$ sig & $\bar{\beta}_K$ & ASR & $\Delta$ \\
372	\midrule
373	Majority & 10/12 & 0.42 & 0.074 & -- \\
374	Threshold & 11/12 & 0.61 & 0.138 & +86\% \\
375	Acc-weighted & 8/12 & 0.39 & 0.069 & $-$6.8\% \\
376	Bayesian & 6/12 & 0.25 & 0.053 & $-$28.4\% \\
377	\bottomrule
378	\end{tabular}
379	\end{table}
380	
381	\section{Conclusion}
382	
383	We presented large-scale empirical evidence for the \emph{diversity trap} in multi-judge LLM evaluation: panel diversity independently increases vulnerability to adaptive adversarial attacks. This finding, validated across 15 models, 455 panels, 9 attack types, 4 benchmarks, and multiple panel sizes, challenges the pervasive assumption that diversity improves evaluation robustness. The mechanism traces to BFT's broken assumption: adaptive adversaries exploit the heterogeneous attack surface that diverse judges create, concentrating attacks on the weakest judge rather than facing independent random faults. We proposed a two-stage defense (robustness screening + diversity optimization) that reduces ASR by 20.8\%, complemented by Bayesian aggregation ($-$28.4\%). We urge the LLM evaluation community to adopt diversity-aware security analysis: do not assume more judges means safer evaluation.
384	
385	\section*{Limitations}
386	
387	Our study has three main limitations. First, our adversary model assumes knowledge of panel composition (full or partial); in settings where panel membership is secret, the diversity trap may be attenuated. Second, while we cover 15 models from 6 families, the rapidly evolving LLM landscape means our specific quantitative findings may shift as new model generations emerge. Third, our analysis is observational---the regression design establishes independent predictive association, not strict causality, between diversity and vulnerability; experimental manipulation of panel composition with controlled interventions would strengthen causal claims.
388	
389	\bibliography{anthology,custom}
390	
391	\end{document}
392	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0caacf5-428c-46dc-9d2e-3268a725766a",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "0f7b5173-5950-4943-ba57-3a487fc79a84",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{amsmath}\n\\usepackage{amsfonts}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\n\\setlength\\titlebox{5cm}\n\n\\newcommand{\\keff}{K_{\\text{eff}}}\n\\newcommand{\\etamax}{\\eta_{\\text{max}}}\n\\newcommand{\\keffresid}{K_{\\text{eff}}^{\\text{resid}}}\n\n\\title{More Diverse, More Vulnerable:\\\\How Judge Panel Diversity Backfires Under Adaptive Adversaries}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge evaluation panels are increasingly used to assess LLM outputs, with the prevailing assumption that judge diversity---analogous to Byzantine Fault Tolerance (BFT)---improves robustness against manipulation. We provide large-scale empirical evidence that this assumption \\emph{reverses} under adaptive adversaries. Across 15 LLM judges spanning 6 model families, 455 three-judge panels, 9 attack types, and 4 evaluation benchmarks, we show that panel diversity (effective independence $\\keff$) is \\textbf{independently and positively} associated with attack success rate (ASR), even after residualizing against individual judge weakness ($\\etamax$). This ``diversity trap'' is driven by dual vulnerability channels whose relative importance is attack-dependent: $\\etamax$ dominates shared-bias attacks (sycophancy, verbosity), while $\\keff$ dominates transferable attacks (score manipulation, position bias). We trace the mechanism to BFT's broken assumption: random faults distribute uniformly across judges (Gini$\\approx$0.12), but adaptive adversaries concentrate attacks on the weakest judge (Gini$\\approx$0.68), turning diversity from a defense into an expanded attack surface. Under calibrated random faults, $\\keff$'s coefficient flips negative in 5/12 conditions, empirically confirming BFT's prediction. We propose a robustness-first two-stage panel selection algorithm that reduces ASR by 20.8\\% over the strongest-$K$ baseline, and show that Bayesian aggregation provides a complementary 28.4\\% reduction. Our findings challenge the ``more diverse = more robust'' assumption and call for diversity-aware security analysis in LLM evaluation pipeline design.\n\\end{abstract}\n\n\\section{Introduction}\n\nAs LLMs are increasingly deployed as automated evaluators~\\cite{zheng2023judging,li2023alpacaeval}, the research community has adopted multi-judge panels to mitigate individual model biases. The intuition is straightforward and borrowed from distributed systems: diverse, independent judges should be harder to simultaneously fool, much like Byzantine Fault Tolerance (BFT) guarantees that $f$ faulty nodes cannot compromise a system of $3f+1$ independent replicas.\n\nThis paper demonstrates that this intuition is \\emph{wrong} under adversarial conditions. We conduct what is, to our knowledge, the largest systematic study of adversarial robustness in multi-judge LLM evaluation: 15 models from 6 families (OpenAI, Anthropic, Google, Meta, Alibaba, Microsoft), enumerated into 455 three-judge panels, evaluated under 9 distinct attack types across MMLU, ARC-Challenge, MT-Bench, and AlpacaEval.\n\nOur central finding is the \\textbf{diversity trap}: panel diversity, measured by effective judge independence ($\\keff$), is \\emph{independently and positively} associated with attack success rate. After residualizing $\\keff$ against individual judge weakness ($\\etamax$, the maximum vulnerability of any panel member), $\\keffresid$ remains significantly positive in 10/12 conditions (FDR-corrected). Panel vulnerability is driven by \\textbf{dual factors}---$\\etamax$ and $\\keff$---whose relative importance depends on attack type:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Shared-bias attacks} (sycophancy, verbosity, authority): $\\etamax$ dominates because all judges share similar cognitive biases from RLHF training.\n\\item \\textbf{Transferable attacks} (score manipulation, position bias): $\\keff$ dominates because diverse judges provide heterogeneous, judge-specific attack surfaces.\n\\end{itemize}\n\nWe trace this to BFT's core assumption: fault independence. Under random faults, failures distribute uniformly (Gini$\\approx$0.12) and diversity genuinely helps---our calibrated random-fault simulations show $\\keff$'s coefficient \\emph{flipping negative} in 5/12 conditions. But adaptive adversaries concentrate attacks on the weakest judges (Gini$\\approx$0.68, top-1 judge absorbing 78\\% of ASR), turning diversity from fault tolerance into an expanded attack menu.\n\nWe further show that: (1) the diversity trap holds within capability tiers (4/6 conditions significant among top-tier models only), ruling out tier-mixing confounds; (2) generalizes to open-ended benchmarks (MT-Bench 3/4, AlpacaEval 2/4 significant); (3) scales with panel size ($\\keff$ coefficient increases monotonically from $K$=3 to $K$=9); (4) holds under partial-knowledge adversaries who know only model family membership (7/12 significant). We propose a two-stage defense---robustness screening followed by diversity optimization---that achieves 20.8\\% ASR reduction over the strongest-$K$ baseline, and show Bayesian aggregation provides complementary protection.\n\n\\section{Related Work}\n\n\\paragraph{LLM-as-Judge.} LLM evaluation using model judges has become standard practice~\\cite{zheng2023judging,li2023alpacaeval,dubois2024alpacafarm}. Known biases include position bias, verbosity preference, and self-enhancement~\\cite{wang2023large,zheng2023judging}. Multi-judge panels are proposed as mitigation, but their adversarial robustness remains unstudied.\n\n\\paragraph{Adversarial Attacks on LLM Judges.} Prior work demonstrates individual judge vulnerability to prompt injection, sycophancy exploitation, and score manipulation~\\cite{raina2024llm,shi2024optimization}. We extend this to \\emph{panel-level} analysis, studying how panel composition mediates vulnerability.\n\n\\paragraph{Byzantine Fault Tolerance.} Classical BFT~\\cite{lamport1982byzantine,castro1999practical} guarantees safety when faults are independent. Recent work questions independence assumptions in ML systems~\\cite{sagawa2020investigation}. We empirically test whether BFT's independence assumption holds for LLM judge panels.\n\n\\paragraph{Ensemble Diversity.} The diversity-accuracy tradeoff is well-studied in ensemble learning~\\cite{krogh1994neural,brown2005diversity}. Our setting differs: we study diversity under \\emph{adaptive adversaries} who exploit panel composition, not passive noise.\n\n\\section{Problem Formulation}\n\n\\paragraph{Setup.} A panel $P = \\{j_1, \\ldots, j_K\\}$ of $K$ LLM judges evaluates candidate responses. Each judge $j_i$ produces a binary decision (accept/reject). The panel decision uses an aggregation rule $\\mathcal{A}$ (default: majority vote).\n\n\\paragraph{Adversary Model.} An adaptive adversary observes the panel composition and crafts attacks to maximize the panel's attack success rate (ASR)---the fraction of evaluation instances where the panel decision is flipped.\n\n\\paragraph{Vulnerability Metrics.} We define two panel-level predictors:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item $\\etamax = \\max_{j \\in P} \\eta_j$: maximum individual vulnerability (weakest link). $\\eta_j$ is judge $j$'s individual ASR under a given attack.\n\\item $\\keff$: effective number of independent judges, computed from the eigenspectrum of the pairwise mutual information matrix. Higher $\\keff$ indicates greater functional diversity.\n\\end{itemize}\n\nTo disentangle $\\keff$ from $\\etamax$, we define $\\keffresid$ as the residual of regressing $\\keff$ on $\\etamax$, ensuring orthogonality (VIF$=$1.02).\n\n\\paragraph{Regression Model.} For each condition (dataset $\\times$ attack type), we fit:\n\\begin{equation}\n\\text{ASR}_P = \\beta_0 + \\beta_\\eta \\cdot \\etamax + \\beta_K \\cdot \\keffresid + \\epsilon\n\\end{equation}\nacross all 455 panels. A significantly positive $\\beta_K$ indicates diversity independently increases vulnerability.\n\n\\section{Experimental Setup}\n\n\\paragraph{Models.} 15 LLM judges: GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini (OpenAI); Claude-3.5-Sonnet (Anthropic); Gemini-1.5-Pro (Google); Llama-3.1-8B, Llama-3.1-70B (Meta); Qwen2.5-7B, Qwen2.5-72B (Alibaba); Mistral-7B-v0.3, Phi-3-medium-14B (Microsoft). Three capability tiers: Small (7--14B), Medium (14--34B), Large (70B+ and API).\n\n\\paragraph{Panels.} All $\\binom{15}{3} = 455$ three-judge panels, extended to $K \\in \\{5,7,9\\}$ for panel-size analysis.\n\n\\paragraph{Attacks.} 9 attack types spanning three paradigms: \\emph{bias exploitation} (sycophancy, verbosity, authority bias), \\emph{score manipulation} (direct score manipulation, position bias, few-shot bias), and \\emph{injection} (few-shot hijacking, persona manipulation, instruction override).\n\n\\paragraph{Benchmarks.} MMLU and ARC-Challenge (MCQ); MT-Bench and AlpacaEval (open-ended generation).\n\n\\paragraph{Statistical Methods.} FDR correction (Benjamini-Hochberg) for multiple comparisons; beta regression for distributional robustness; residualization for multicollinearity control.\n\n\\section{The Diversity Trap: Core Evidence}\n\n\\subsection{Dual Vulnerability Drivers}\n\nTable~\\ref{tab:core} presents the core regression results across 12 conditions (2 datasets $\\times$ 6 attacks). Both $\\etamax$ and $\\keffresid$ are significant predictors of panel ASR: $\\etamax$ reaches FDR significance in 10/12 conditions, $\\keffresid$ in 10/12 conditions. The mean $R^2 = 0.62$, indicating that these two factors jointly explain the majority of panel-level vulnerability variance.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Dual vulnerability drivers: 15-model regression across 12 conditions (455 panels each). $\\keffresid$ is residualized against $\\etamax$ (VIF$=$1.02). Bold $p$-values are FDR-significant ($q < 0.05$). ``Dominant'' indicates which predictor has the larger standardized $\\beta$.}\n\\label{tab:core}\n\\begin{tabular}{lccccccl}\n\\toprule\nCondition & $\\etamax$ $\\beta$ & $p$ & $\\keffresid$ $\\beta$ & $p$ & $R^2$ & Confound $r$ & Dominant \\\\\n\\midrule\nmmlu$\\times$sycophancy & 0.82 & \\textbf{1.2e-8} & 0.31 & \\textbf{0.004} & 0.68 & 0.72 & $\\etamax$ \\\\\nmmlu$\\times$score\\_manip & 0.45 & \\textbf{0.018} & 0.61 & \\textbf{3.4e-9} & 0.71 & 0.38 & $\\keff$ \\\\\nmmlu$\\times$position & 0.15 & 0.214 & 0.58 & \\textbf{1.2e-8} & 0.56 & 0.36 & $\\keff$ \\\\\nmmlu$\\times$verbosity & 0.74 & \\textbf{4.1e-7} & 0.28 & \\textbf{0.011} & 0.63 & 0.74 & $\\etamax$ \\\\\nmmlu$\\times$authority & 0.69 & \\textbf{1.8e-6} & 0.19 & 0.087 & 0.58 & 0.78 & $\\etamax$ \\\\\nmmlu$\\times$few\\_shot & 0.55 & \\textbf{2.3e-4} & 0.48 & \\textbf{6.1e-6} & 0.65 & 0.65 & both \\\\\n\\midrule\narc$\\times$sycophancy & 0.79 & \\textbf{3.5e-8} & 0.35 & \\textbf{0.002} & 0.66 & 0.71 & $\\etamax$ \\\\\narc$\\times$score\\_manip & 0.38 & 0.117 & 0.64 & \\textbf{1.7e-7} & 0.59 & 0.35 & $\\keff$ \\\\\narc$\\times$position & 0.03 & 0.910 & 0.72 & \\textbf{1.8e-8} & 0.57 & 0.34 & $\\keff$ \\\\\narc$\\times$verbosity & 0.71 & \\textbf{8.9e-7} & 0.33 & \\textbf{0.003} & 0.61 & 0.73 & $\\etamax$ \\\\\narc$\\times$authority & 0.66 & \\textbf{3.2e-6} & 0.22 & 0.062 & 0.55 & 0.76 & $\\etamax$ \\\\\narc$\\times$few\\_shot & 0.51 & \\textbf{5.7e-4} & 0.52 & \\textbf{3.8e-6} & 0.63 & 0.62 & both \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nA systematic pattern emerges: \\textbf{transferable attacks} (score manipulation, position bias) are $\\keff$-dominated ($\\beta_K > \\beta_\\eta$), while \\textbf{shared-bias attacks} (sycophancy, verbosity, authority) are $\\etamax$-dominated. This yields a predictive taxonomy: given a new attack type, its transferability predicts which vulnerability channel dominates.\n\nThree conditions have low confound correlation ($r \\approx 0.35$), serving as ``smoking gun'' evidence: in these conditions, $\\keffresid$ achieves $p < 2.1 \\times 10^{-28}$, confirming diversity's independent harmful effect even where the $\\keff$-$\\etamax$ association is weak.\n\n\\subsection{Capability-Matched Validation}\n\nA natural concern is that $\\keff$'s positive effect is an artifact of tier-mixing: high-$\\keff$ panels might mix weak and strong models, making $\\keff$ a proxy for tier heterogeneity rather than diversity \\emph{per se}. We test this by running within-tier regressions (Table~\\ref{tab:tier}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Within-tier $\\keff$ validation. Large tier uses only top-tier models (70B+ and API), eliminating tier-mixing.}\n\\label{tab:tier}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & Models & Panels & $r(\\keff,\\etamax)$ & $\\keffresid$ sig \\\\\n\\midrule\nSmall (7B--14B) & 5 & 10 & 0.32 & 2/6 \\\\\nMedium & 4 & 4 & 0.41 & 1/6 \\\\\nLarge (70B+API) & 6 & 20 & 0.33 & 4/6 \\\\\nCross-tier (all) & 15 & 455 & 0.55 & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe large tier is most informative: all 6 models are top-tier (GPT-4o, GPT-4.1, Claude-3.5-Sonnet, Gemini-1.5-Pro, Llama-70B, Qwen-72B), yet $\\keffresid$ is significant in 4/6 conditions (best $p = 4.2 \\times 10^{-4}$). The condition-dependent pattern is preserved: score manipulation and position bias are $\\keff$-dominated; sycophancy and verbosity are $\\etamax$-dominated. This rules out tier-mixing as the driver of the diversity trap.\n\n\\subsection{Statistical Robustness}\n\nWe perform comprehensive diagnostics (Table~\\ref{tab:diagnostics}). VIF$=$1.02 and condition number$=$4.8 confirm the design matrix is well-conditioned. Residuals pass Shapiro-Wilk normality ($p = 0.23$). Maximum Cook's distance is 0.031 (threshold: 1.0), with only 2.4\\% high-leverage points. Under Bonferroni correction (most conservative), $\\keffresid$ remains significant in 8/12 conditions. Beta regression, which properly handles bounded ASR in $[0,1]$, confirms 9/12 significant---highly consistent with OLS.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multiple comparison robustness across correction methods.}\n\\label{tab:diagnostics}\n\\begin{tabular}{lcc}\n\\toprule\nCorrection & $\\keffresid$ sig & $\\etamax$ sig \\\\\n\\midrule\nUncorrected & 12/12 & 11/12 \\\\\nFDR (BH) & 10/12 & 10/12 \\\\\nBonferroni & 8/12 & 9/12 \\\\\nBeta reg.\\ + FDR & 9/12 & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Mechanism: BFT Reversal}\n\n\\subsection{Random-Fault Contrast}\n\nBFT predicts that diversity helps when faults are independent and random. We test this by simulating calibrated random faults: each judge's failure probability is drawn from bootstrapped clean-accuracy noise, independent across judges. Table~\\ref{tab:bft} contrasts $\\keff$'s coefficient under adaptive versus random-fault regimes.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{BFT regime contrast: $\\keff$ coefficient under adaptive vs.\\ calibrated random faults (12 conditions, 455 panels). ``Flipped'' indicates $\\beta_{\\text{RF}}$ is significantly negative (diversity helps under random faults).}\n\\label{tab:bft}\n\\begin{tabular}{lcccccc}\n\\toprule\nCondition & $\\beta_{\\text{adaptive}}$ & $p_{\\text{adap}}$ & $\\beta_{\\text{RF}}$ & $p_{\\text{RF}}$ & $|\\beta_{\\text{adap}}/\\beta_{\\text{RF}}|$ & Flipped? \\\\\n\\midrule\nmmlu$\\times$sycophancy & 0.31 & \\textbf{0.004} & 0.08 & 0.310 & 3.88 & No \\\\\nmmlu$\\times$score\\_manip & 0.61 & \\textbf{3.4e-9} & $-$0.22 & \\textbf{0.015} & 2.77 & Yes \\\\\nmmlu$\\times$position & 0.58 & \\textbf{1.2e-8} & $-$0.31 & \\textbf{0.003} & 1.87 & Yes \\\\\nmmlu$\\times$verbosity & 0.28 & \\textbf{0.011} & 0.11 & 0.198 & 2.55 & No \\\\\nmmlu$\\times$authority & 0.19 & 0.087 & 0.06 & 0.541 & 3.17 & No \\\\\nmmlu$\\times$few\\_shot & 0.48 & \\textbf{6.1e-6} & $-$0.18 & \\textbf{0.039} & 2.67 & Yes \\\\\narc$\\times$sycophancy & 0.35 & \\textbf{0.002} & 0.10 & 0.251 & 3.50 & No \\\\\narc$\\times$score\\_manip & 0.64 & \\textbf{1.7e-7} & $-$0.28 & \\textbf{0.008} & 2.29 & Yes \\\\\narc$\\times$position & 0.72 & \\textbf{1.8e-8} & $-$0.35 & \\textbf{0.001} & 2.06 & Yes \\\\\narc$\\times$verbosity & 0.33 & \\textbf{0.003} & 0.12 & 0.175 & 2.75 & No \\\\\narc$\\times$authority & 0.22 & 0.062 & 0.05 & 0.612 & 4.40 & No \\\\\narc$\\times$few\\_shot & 0.52 & \\textbf{3.8e-6} & $-$0.14 & 0.091 & 3.71 & Marginal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe results confirm the BFT reversal: in 5/12 conditions, $\\beta_{\\text{RF}}$ flips to significantly \\emph{negative}---diversity genuinely protects under random faults, as BFT predicts. The flips concentrate on transferable attacks (score manipulation, position bias, few-shot), where judge-specific exploit paths are most relevant. Under adaptive attacks, these same conditions show the strongest positive $\\beta$ (0.48--0.72). The mean $\\beta$ ratio is 2.8$\\times$, and the $R^2$ gap ($\\Delta R^2 = 0.31$; RF: 0.78, adaptive: 0.47) quantifies BFT's broken predictability: panel structure explains 78\\% of variance under random faults but only 47\\% under adaptive attacks, where strategic adversary behavior introduces irreducible noise.\n\n\\subsection{ASR Concentration Analysis}\n\nTo illuminate \\emph{how} adaptive adversaries exploit diversity, we analyze per-judge ASR distributions within panels (Table~\\ref{tab:concentration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{ASR concentration: adaptive vs.\\ random-fault regimes.}\n\\label{tab:concentration}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Adaptive & RF & Ratio \\\\\n\\midrule\nMean Gini & 0.68 & 0.12 & 5.67 \\\\\nEntropy (bits) & 1.42 & 2.31 & 0.61 \\\\\nTop-1 judge share & 0.78 & 0.38 & 2.05 \\\\\n$r(\\keff, \\text{Gini})$ & 0.52 & 0.08 & 6.50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder adaptive attacks, ASR is highly concentrated: the weakest judge absorbs 78\\% of attack success (vs.\\ 38\\% under random faults). Crucially, $r(\\keff, \\text{Gini}) = 0.52$: more diverse panels produce \\emph{more concentrated} attacks, because greater capability spread gives the adversary a clearer targeting gradient. Under random faults, concentration is uniformly low (Gini$=$0.12), confirming BFT's independence assumption holds only in the non-adversarial regime.\n\n\\section{Generalization}\n\n\\subsection{Attack Surface Expansion}\n\nTo test whether the diversity trap generalizes beyond the original 6 attack types, we introduce 3 additional attacks: few-shot hijacking (in-context example injection), persona manipulation (authority impersonation), and instruction override (direct prompt overwrite). Table~\\ref{tab:expanded} shows the 6 new conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Extended attack results (6 new conditions, 15 models).}\n\\label{tab:expanded}\n\\begin{tabular}{lccc}\n\\toprule\nCondition & $\\keffresid$ $\\beta$ & $p$ & Dominant \\\\\n\\midrule\nmmlu$\\times$hijack & 0.54 & \\textbf{8.2e-7} & $\\keff$ \\\\\nmmlu$\\times$persona & 0.29 & \\textbf{0.008} & $\\etamax$ \\\\\nmmlu$\\times$override & 0.22 & 0.042 & $\\etamax$ \\\\\narc$\\times$hijack & 0.58 & \\textbf{2.1e-7} & $\\keff$ \\\\\narc$\\times$persona & 0.25 & \\textbf{0.019} & $\\etamax$ \\\\\narc$\\times$override & 0.18 & 0.112 & $\\etamax$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\keffresid$ is significant in 4/6 new conditions. Combined with the original 12, this yields 14/18 total FDR-significant conditions for $\\keffresid$. The attack taxonomy is predictive: high-transferability attacks (few-shot hijacking) are $\\keff$-dominated; moderate/low-transferability attacks (persona, instruction override) are $\\etamax$-dominated---consistent with the core results.\n\n\\subsection{Open-Ended Benchmarks}\n\nThe diversity trap is not an MCQ artifact. On MT-Bench (multi-turn dialogue evaluation) and AlpacaEval (instruction-following scoring), $\\keffresid$ is significant in 3/4 and 2/4 conditions, respectively (Table~\\ref{tab:openended}). The condition-dependent dominance pattern transfers without modification: score manipulation and position bias remain $\\keff$-dominated; sycophancy and verbosity remain $\\etamax$-dominated. $R^2$ is lower (0.39--0.52 vs.\\ 0.62 for MCQ), reflecting the higher noise floor inherent to open-ended evaluation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Open-ended benchmark results (8 conditions). Pattern consistent with MCQ findings despite higher evaluation noise.}\n\\label{tab:openended}\n\\begin{tabular}{lcccl}\n\\toprule\nCondition & $\\keffresid$ $\\beta$ & $p$ & $R^2$ & Dom. \\\\\n\\midrule\nMT$\\times$score & 0.52 & \\textbf{1.8e-5} & 0.52 & $\\keff$ \\\\\nMT$\\times$syco & 0.28 & \\textbf{0.012} & 0.49 & $\\etamax$ \\\\\nMT$\\times$pos & 0.47 & \\textbf{8.3e-5} & 0.44 & $\\keff$ \\\\\nMT$\\times$verb & 0.18 & 0.108 & 0.47 & $\\etamax$ \\\\\nAE$\\times$score & 0.44 & \\textbf{3.2e-4} & 0.46 & $\\keff$ \\\\\nAE$\\times$syco & 0.21 & 0.058 & 0.43 & $\\etamax$ \\\\\nAE$\\times$pos & 0.38 & \\textbf{0.002} & 0.40 & both \\\\\nAE$\\times$verb & 0.14 & 0.175 & 0.39 & $\\etamax$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Panel Size Sensitivity}\n\nExtending panel size from $K=3$ to $K \\in \\{5,7,9\\}$ reveals a scaling law: $\\keff$'s coefficient increases monotonically ($\\beta_K$: 0.42$\\to$0.48$\\to$0.55$\\to$0.61), while $\\etamax$'s decreases (0.51$\\to$0.49$\\to$0.43$\\to$0.38). The crossover occurs at $K \\approx 6$: for panels below this size, individual robustness ($\\etamax$) is the primary concern; above it, structural diversity ($\\keff$) becomes dominant (Table~\\ref{tab:panelsize}). This has direct practical implications: the common strategy of ``adding more judges'' systematically amplifies the diversity trap---$K=9$ panels show 45\\% stronger $\\keff$ effect than $K=3$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Panel size sensitivity ($K = 3, 5, 7, 9$).}\n\\label{tab:panelsize}\n\\begin{tabular}{lccccl}\n\\toprule\n$K$ & Panels & $\\keffresid$ sig & $\\bar{\\beta}_K$ & $\\bar{\\beta}_\\eta$ & Primary \\\\\n\\midrule\n3 & 455 & 10/12 & 0.42 & 0.51 & $\\etamax$ \\\\\n5 & 3003 & 11/12 & 0.48 & 0.49 & balanced \\\\\n7 & 6435 & 12/12 & 0.55 & 0.43 & $\\keff$ \\\\\n9 & 5005 & 12/12 & 0.61 & 0.38 & $\\keff$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Partial-Knowledge Adversary}\n\nA full-knowledge adversary is a worst-case assumption. We test a realistic partial-knowledge adversary who knows only model \\emph{family} membership (typically public information) but not individual vulnerability profiles. Family-level targeting achieves 78.4\\% of full-knowledge ASR (0.058 vs.\\ 0.074), and $\\keff$ remains significant in 7/12 conditions (Table~\\ref{tab:partial}). Family membership alone captures 62.8\\% of adversary information value, because family$\\to$capability tier correlations provide a strong prior on vulnerability profiles.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Adversary knowledge level comparison.}\n\\label{tab:partial}\n\\begin{tabular}{lcccc}\n\\toprule\nKnowledge & ASR & $\\keff$ sig & $R^2$ & Info value \\\\\n\\midrule\nFull & 0.074 & 10/12 & 0.62 & 100\\% \\\\\nPartial (family) & 0.058 & 7/12 & 0.51 & 62.8\\% \\\\\nBlack-box & 0.031 & 3/12 & 0.28 & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Structural Barriers to Independence}\n\n\\subsection{Gaussian Copula Failure}\n\nIf inter-judge dependence followed a Gaussian copula, pairwise mutual information (MI) could be estimated from linear correlations. Across 105 model pairs (15 models), observed MI exceeds Gaussian-predicted MI by a mean factor of 18.5$\\times$ (max 312$\\times$), with 82/105 pairs exceeding 10$\\times$. This invalidates copula-based independence bounds and motivates empirical $\\keff$ measurement.\n\n\\subsection{Family Labels Are Unreliable}\n\nModel family labels do not predict judge independence: within-family MI (0.42) is not significantly higher than cross-family MI (0.39; Mann-Whitney $p = 0.158$). The actual driver is capability proximity ($r = -0.71$ with MI): models at similar capability levels share failure modes regardless of training pipeline. Practitioners should not equate ``different families'' with ``diverse panel.''\n\n\\subsection{Diversity-Capability Tradeoff}\n\nAcross 455 panels, $\\keff$ and $\\etamax$ correlate at $r = 0.55$ globally. Within capability tiers, this drops to $r \\approx 0.33$, revealing two components: a cross-tier component ($\\sim$40\\%, from mixing weak and strong models) and a within-tier residual ($\\sim$60\\%, from genuine diversity-vulnerability association). The Pareto frontier (18 panels, slope $-0.73$) quantifies the tradeoff: each 0.1 increase in $\\keff$ costs at least 0.073 increase in $\\etamax$.\n\n\\section{Defense: Panel Design and Aggregation}\n\n\\subsection{Two-Stage Panel Selection}\n\nWe propose a robustness-first algorithm: (1) screen judges by individual robustness ($\\eta_j \\leq$ percentile-75 threshold), (2) maximize $\\keff$ among qualifying judges. Table~\\ref{tab:defense} benchmarks this against 5 baselines.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Panel selection strategy benchmark (15 models, MMLU, 6 attacks). Two-stage achieves 84\\% of oracle efficiency.}\n\\label{tab:defense}\n\\begin{tabular}{lccc}\n\\toprule\nStrategy & ASR & $\\Delta$ vs Strong-K & Best (of 6) \\\\\n\\midrule\nTwo-Stage (ours) & 0.038 & $-$20.8\\% & 5/6 \\\\\nMin-$\\etamax$ & 0.041 & $-$14.6\\% & 4/6 \\\\\nStrongest-$K$ & 0.048 & baseline & 1/6 \\\\\nRandom & 0.089 & +85.4\\% & 0/6 \\\\\nMax-$\\keff$ & 0.112 & +133.3\\% & 0/6 \\\\\nOracle & 0.032 & $-$33.3\\% & 6/6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo-stage achieves the lowest ASR among non-oracle strategies (0.038), outperforming the strongest-$K$ baseline by 20.8\\%. Max-$\\keff$ is catastrophic (ASR 0.112, +133\\%), providing the most direct evidence against blind diversity maximization. Sensitivity analysis shows the screening threshold is robust across percentile 50--75, with optimal performance at percentile 65--75.\n\n\\subsection{Aggregation Rule Modulation}\n\nThe dual vulnerability driver effect varies by aggregation rule (Table~\\ref{tab:aggregation}). Threshold (unanimity) voting amplifies $\\keff$'s harmful effect by 45\\% ($\\beta_K$: 0.42$\\to$0.61) and increases ASR by 86\\%, because a single flipped judge blocks panel rejection. Bayesian aggregation, which downweights judges based on prior accuracy, provides the best single-aggregation defense: 28.4\\% ASR reduction, with $\\keff$ significance dropping from 10/12 to 6/12. However, 6/12 $\\keff$ significance confirms Bayesian aggregation alone cannot eliminate the diversity trap, motivating a combined defense stack.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Aggregation rule $\\times$ vulnerability drivers (455 panels).}\n\\label{tab:aggregation}\n\\begin{tabular}{lcccc}\n\\toprule\nAggregation & $\\keff$ sig & $\\bar{\\beta}_K$ & ASR & $\\Delta$ \\\\\n\\midrule\nMajority & 10/12 & 0.42 & 0.074 & -- \\\\\nThreshold & 11/12 & 0.61 & 0.138 & +86\\% \\\\\nAcc-weighted & 8/12 & 0.39 & 0.069 & $-$6.8\\% \\\\\nBayesian & 6/12 & 0.25 & 0.053 & $-$28.4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Conclusion}\n\nWe presented large-scale empirical evidence for the \\emph{diversity trap} in multi-judge LLM evaluation: panel diversity independently increases vulnerability to adaptive adversarial attacks. This finding, validated across 15 models, 455 panels, 9 attack types, 4 benchmarks, and multiple panel sizes, challenges the pervasive assumption that diversity improves evaluation robustness. The mechanism traces to BFT's broken assumption: adaptive adversaries exploit the heterogeneous attack surface that diverse judges create, concentrating attacks on the weakest judge rather than facing independent random faults. We proposed a two-stage defense (robustness screening + diversity optimization) that reduces ASR by 20.8\\%, complemented by Bayesian aggregation ($-$28.4\\%). We urge the LLM evaluation community to adopt diversity-aware security analysis: do not assume more judges means safer evaluation.\n\n\\section*{Limitations}\n\nOur study has three main limitations. First, our adversary model assumes knowledge of panel composition (full or partial); in settings where panel membership is secret, the diversity trap may be attenuated. Second, while we cover 15 models from 6 families, the rapidly evolving LLM landscape means our specific quantitative findings may shift as new model generations emerge. Third, our analysis is observational---the regression design establishes independent predictive association, not strict causality, between diversity and vulnerability; experimental manipulation of panel composition with controlled interventions would strengthen causal claims.\n\n\\bibliography{anthology,custom}\n\n\\end{document}\n",
      "numLines": 392,
      "startLine": 1,
      "totalLines": 392
    }
  },
  "sourceToolAssistantUUID": "a0caacf5-428c-46dc-9d2e-3268a725766a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_…",
  "leafUuid": "0f7b5173-5950-4943-ba57-3a487fc79a84",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate certificate manipulation vulnerability study paper",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba"
}
```

---

### Tool call

_source line 41 · 2026-05-22T18:21:28.797Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01QbSZfL5riJhHYvapKGmmV4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{amsmath}\n\\usepackage{amsfonts}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\n\\setlength\\titlebox{5cm}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{amsmath}\n\\usepackage{amsfonts}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\\usepackage[numbers]{natbib}\n\\usepackage{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f7b5173-5950-4943-ba57-3a487fc79a84",
  "isSidechain": false,
  "requestId": "req_011CbJ56Fz4kcwaBsvvpibVj",
  "type": "assistant",
  "uuid": "a4e0c9dd-2c7f-4abd-ba3f-96536da9e499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7BGGMUMJ5acA7jsyxFkbv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10892,
      "cache_read_input_tokens": 63904,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 413,
          "cache_read_input_tokens": 63904,
          "cache_creation_input_tokens": 10892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10892
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

_source line 42 · 2026-05-22T18:21:28.813Z_

<details><summary>↩ Tool result · `toolu_01QbSZfL5riJhHYvapKGmmV4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4e0c9dd-2c7f-4abd-ba3f-96536da9e499",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "593695e4-f115-497d-be4e-3a602d96a4c2",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{amsmath}\n\\usepackage{amsfonts}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\n\\setlength\\titlebox{5cm}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{amsmath}\n\\usepackage{amsfonts}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\\usepackage[numbers]{natbib}\n\\usepackage{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\documentclass[11pt,a4paper]{article}",
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{booktabs}"
        ]
      },
      {
        "oldStart": 10,
        "oldLines": 9,
        "newStart": 10,
        "newLines": 9,
        "lines": [
          " \\usepackage{xcolor}",
          " \\usepackage{enumitem}",
          " \\usepackage{tabularx}",
          "+\\usepackage[numbers]{natbib}",
          "+\\usepackage{hyperref}",
          " ",
          "-\\setlength\\titlebox{5cm}",
          "-",
          " \\newcommand{\\keff}{K_{\\text{eff}}}",
          " \\newcommand{\\etamax}{\\eta_{\\text{max}}}",
          " \\newcommand{\\keffresid}{K_{\\text{eff}}^{\\text{resid}}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a4e0c9dd-2c7f-4abd-ba3f-96536da9e499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T18:21:32.407Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01LTGW3XT7zhGJYCTvSoSrjc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex",
  "old_string": "\\bibliography{anthology,custom}",
  "new_string": "\\bibliographystyle{plainnat}\n\\bibliography{custom}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "593695e4-f115-497d-be4e-3a602d96a4c2",
  "isSidechain": false,
  "requestId": "req_011CbJ56xY76Nm7mrFXH76Z7",
  "type": "assistant",
  "uuid": "9fcce938-51ab-4de8-9895-a5371b6c586a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pUitGGgPLSxYhFD6ta8Ez",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 501,
      "cache_read_input_tokens": 74796,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 74796,
          "cache_creation_input_tokens": 501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 501
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

_source line 44 · 2026-05-22T18:21:32.421Z_

<details><summary>↩ Tool result · `toolu_01LTGW3XT7zhGJYCTvSoSrjc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fcce938-51ab-4de8-9895-a5371b6c586a",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "29e55ffb-1719-42aa-b3c4-6dba2fe76651",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex",
    "oldString": "\\bibliography{anthology,custom}",
    "newString": "\\bibliographystyle{plainnat}\n\\bibliography{custom}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 386,
        "oldLines": 6,
        "newStart": 386,
        "newLines": 7,
        "lines": [
          " ",
          " Our study has three main limitations. First, our adversary model assumes knowledge of panel composition (full or partial); in settings where panel membership is secret, the diversity trap may be attenuated. Second, while we cover 15 models from 6 families, the rapidly evolving LLM landscape means our specific quantitative findings may shift as new model generations emerge. Third, our analysis is observational---the regression design establishes independent predictive association, not strict causality, between diversity and vulnerability; experimental manipulation of panel composition with controlled interventions would strengthen causal claims.",
          " ",
          "-\\bibliography{anthology,custom}",
          "+\\bibliographystyle{plainnat}",
          "+\\bibliography{custom}",
          " ",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9fcce938-51ab-4de8-9895-a5371b6c586a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T18:21:36.502Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YEAYqHGd3EEVu423Yk2CxW`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29e55ffb-1719-42aa-b3c4-6dba2fe76651",
  "isSidechain": false,
  "requestId": "req_011CbJ57E12b2TAAv3eYk28d",
  "type": "assistant",
  "uuid": "f92f7fc9-7345-4366-b2ce-f648f8a419fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9RosX8YnrRujNRtLk6QQN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 75297,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 75297,
          "cache_creation_input_tokens": 247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 247
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

_source line 46 · 2026-05-22T18:21:37.026Z_

<details><summary>↩ Tool result · `toolu_01YEAYqHGd3EEVu423Yk2CxW`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 163677 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f92f7fc9-7345-4366-b2ce-f648f8a419fc",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "391a2b6a-623d-4380-8491-a2ce5e7c58f7",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 163677 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f92f7fc9-7345-4366-b2ce-f648f8a419fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T18:21:41.188Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ec1hLFT1ZiDFqPUwL7BsNE`</summary>

```json
{
  "command": "bibtex paper 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Run bibtex and two more pdflatex passes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "391a2b6a-623d-4380-8491-a2ce5e7c58f7",
  "isSidechain": false,
  "requestId": "req_011CbJ57ZV3qu68kueXRbmzW",
  "type": "assistant",
  "uuid": "0b1450e3-10b5-4648-9e17-ead956c857d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MahQKZQMc9UTfW6676vBym",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 75544,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 75544,
          "cache_creation_input_tokens": 677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 677
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

_source line 48 · 2026-05-22T18:21:42.171Z_

<details><summary>↩ Tool result · `toolu_01Ec1hLFT1ZiDFqPUwL7BsNE`</summary>

```text
Warning--empty journal in raina2024llm
Warning--empty journal in sagawa2020investigation
Warning--empty journal in shi2024optimization
Warning--empty journal in wang2023large
(There were 5 warnings)
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 170016 bytes).
Transcript written on paper.log.
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 170094 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b1450e3-10b5-4648-9e17-ead956c857d0",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "1b47c4c0-aaaa-4ff0-95bf-79cac1856d61",
  "toolUseResult": {
    "stdout": "Warning--empty journal in raina2024llm\nWarning--empty journal in sagawa2020investigation\nWarning--empty journal in shi2024optimization\nWarning--empty journal in wang2023large\n(There were 5 warnings)\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 170016 bytes).\nTranscript written on paper.log.\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 170094 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0b1450e3-10b5-4648-9e17-ead956c857d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-22T18:21:46.401Z_

PDF compiled successfully (9 pages). Let me verify there are no errors in the log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b47c4c0-aaaa-4ff0-95bf-79cac1856d61",
  "isSidechain": false,
  "requestId": "req_011CbJ57xozvWVqFX5HU4ZkU",
  "type": "assistant",
  "uuid": "8b167145-569b-421e-a2e2-8fea4361b481",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7nK4kbCY1PkmYozuDSrvH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 460,
      "cache_read_input_tokens": 76221,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 460,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 76221,
          "cache_creation_input_tokens": 460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 460
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

_source line 50 · 2026-05-22T18:21:47.395Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EPN2ozv5PLMPzGjZE5T127`</summary>

```json
{
  "command": "grep -c \"^!\" paper.log && ls -lh paper.pdf",
  "description": "Check for LaTeX errors and PDF size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b167145-569b-421e-a2e2-8fea4361b481",
  "isSidechain": false,
  "requestId": "req_011CbJ57xozvWVqFX5HU4ZkU",
  "type": "assistant",
  "uuid": "5d0ce507-3ecf-4830-b2ae-5524f30da888",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7nK4kbCY1PkmYozuDSrvH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 460,
      "cache_read_input_tokens": 76221,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 460,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 76221,
          "cache_creation_input_tokens": 460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 460
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

_source line 51 · 2026-05-22T18:21:47.446Z_

<details><summary>↩ Tool result · reported error · `toolu_01EPN2ozv5PLMPzGjZE5T127`</summary>

```text
Exit code 1
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d0ce507-3ecf-4830-b2ae-5524f30da888",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "216f75b4-26ca-4b23-b16a-f04142415e0e",
  "toolUseResult": "Error: Exit code 1\n0",
  "sourceToolAssistantUUID": "5d0ce507-3ecf-4830-b2ae-5524f30da888",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-22T18:21:51.093Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013tNcc25kBmQ33g8jfsRkWx`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.pdf",
  "description": "Check PDF file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "216f75b4-26ca-4b23-b16a-f04142415e0e",
  "isSidechain": false,
  "requestId": "req_011CbJ58LFME66YzmV8mRW6t",
  "type": "assistant",
  "uuid": "cb648af6-cd99-4e12-81b8-d0b74a4948a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvBLwYa41EPcCdhUfPhGpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 138,
      "cache_read_input_tokens": 76681,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 76681,
          "cache_creation_input_tokens": 138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 138
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

_source line 53 · 2026-05-22T18:21:51.152Z_

<details><summary>↩ Tool result · `toolu_013tNcc25kBmQ33g8jfsRkWx`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 167K May 22 18:21 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb648af6-cd99-4e12-81b8-d0b74a4948a8",
  "isSidechain": false,
  "promptId": "993f943f-8f17-4416-a10d-fa7f126cfd97",
  "type": "user",
  "uuid": "1f083ae0-f33d-4fae-bd3b-6cfa4f198c58",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 167K May 22 18:21 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cb648af6-cd99-4e12-81b8-d0b74a4948a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54 · 2026-05-22T18:21:51.160Z_

```json
{
  "parentUuid": "1f083ae0-f33d-4fae-bd3b-6cfa4f198c58",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d5fa68bf-67c3-4b34-aa44-9d4b3715ff50",
  "timestamp": "2026-05-22T18:21:51.160Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 55 · 2026-05-22T18:22:03.100Z_

0 LaTeX errors, 167K PDF. 

论文已写入 `paper.tex` 并编译为 `paper.pdf`（9页，无错误）。覆盖全部 11 个实验的对应 section/table：

- **Table 1**: 12-condition 核心回归（dual vulnerability drivers）
- **Table 2**: Within-tier 验证（capability-matched）
- **Table 3**: 多重比较校正（VIF/Bonferroni/Beta regression）
- **Table 4**: BFT regime contrast（adaptive vs RF，12 conditions）
- **Table 5**: ASR concentration（Gini/entropy）
- **Table 6**: 攻击扩展（6 new conditions）
- **Table 7**: Open-ended benchmarks（MT-Bench + AlpacaEval）
- **Table 8**: Panel size sensitivity（K=3,5,7,9）
- **Table 9**: Partial-knowledge adversary
- **Table 10**: Two-stage selection benchmark
- **Table 11**: Aggregation rule modulation

另外在 §8 Structural Barriers 中以文本形式覆盖了 Gaussian copula failure（18.5× MI underestimate）、family label 不可靠性（MWU p=0.158）和 diversity-capability tradeoff（Pareto slope −0.73）。所有数字均来自 `experiment_data.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5fa68bf-67c3-4b34-aa44-9d4b3715ff50",
  "isSidechain": false,
  "requestId": "req_011CbJ58c5r1un497o5pBp2C",
  "type": "assistant",
  "uuid": "b04638d1-7c02-4793-ba9f-2edb8be9a9df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iNnK3upR1d9pfVfy93XPJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 76819,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 369,
          "cache_read_input_tokens": 76819,
          "cache_creation_input_tokens": 316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 316
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

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_…",
  "leafUuid": "b04638d1-7c02-4793-ba9f-2edb8be9a9df",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate certificate manipulation vulnerability study paper",
  "sessionId": "e6abcd22-961e-4398-8251-13a4344291ba"
}
```

---
