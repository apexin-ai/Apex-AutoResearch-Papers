# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/5539e7cd-7d85-4f3f-8732-4059690119cd.jsonl`
- **Structured JSON:** [`cfd185ee85c4d9ff6c3d.json`](../../sessions/cf/cfd185ee85c4d9ff6c3d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T05:35:59.352Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T05:35:59.352Z",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：CaCLR consistency loss (MMD) 在完整 β sweep 中无显著 AUROC 提升，转为 negative result framing。 几何解释：MMD 匹配边际分布但无法对齐低维 directional structure——correctness 方向占据 1-3 维子空间， MMD 在 1-D probe logit 空间操作无法捕捉旋转。Linear projection 直接学习子空间旋转故成功。 Simpson's Paradox 仅在 Llama 4 Scout 上显著（partial rho~0.29, p~0.02），Qwen3-235B 上 trending 但不显著（rho~0.16, p~0.07）——用 hedged language 报告为架构依赖发现。Claim 2 decomposition 定性分离成立但 prescriptive 预测力弱——弱化为 'descriptive separation observed'。 标题转向 'When Does Cross-Lingual Calibration Transfer Work? Geometric Analysis and Practical Solutions.' 强化三个实用贡献：(1) linear projection ~70 pairs 推荐方案，(2) Procrustes effect reversal 阈值 ~0.55 作为 practitioner guidance，(3) ~30% low-resource probing artifacts 作为 methodological warning。 仍可投 EACL——thorough empirical study + 架构依赖几何洞见 + systematic negative result + 实用指导。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T05:35:59.355Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T05:35:59.355Z",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

## Round 1

63 recorded events

### User

_source line 3 · 2026-05-21T05:35:59.386Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：CaCLR consistency loss (MMD) 在完整 β sweep 中无显著 AUROC 提升，转为 negative result framing。 几何解释：MMD 匹配边际分布但无法对齐低维 directional structure——correctness 方向占据 1-3 维子空间， MMD 在 1-D probe logit 空间操作无法捕捉旋转。Linear projection 直接学习子空间旋转故成功。 Simpson's Paradox 仅在 Llama 4 Scout 上显著（partial rho~0.29, p~0.02），Qwen3-235B 上 trending 但不显著（rho~0.16, p~0.07）——用 hedged language 报告为架构依赖发现。Claim 2 decomposition 定性分离成立但 prescriptive 预测力弱——弱化为 'descriptive separation observed'。 标题转向 'When Does Cross-Lingual Calibration Transfer Work? Geometric Analysis and Practical Solutions.' 强化三个实用贡献：(1) linear projection ~70 pairs 推荐方案，(2) Procrustes effect reversal 阈值 ~0.55 作为 practitioner guidance，(3) ~30% low-resource probing artifacts 作为 methodological warning。 仍可投 EACL——thorough empirical study + 架构依赖几何洞见 + systematic negative result + 实用指导。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "a67c0b6f-08de-48e1-95b1-b694a104ad0a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T05:35:59.386Z_

```json
{
  "parentUuid": "a67c0b6f-08de-48e1-95b1-b694a104ad0a",
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
  "uuid": "7e0fef3e-c757-4f56-9864-ff998de190eb",
  "timestamp": "2026-05-21T05:35:59.386Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T05:35:59.386Z_

```json
{
  "parentUuid": "7e0fef3e-c757-4f56-9864-ff998de190eb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "323fe7bd-8f1a-4c98-9ac3-ab2cccc019ed",
  "timestamp": "2026-05-21T05:35:59.386Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
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
  "aiTitle": "Generate cross-lingual calibration empirical study paper",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Assistant

_source line 7 · 2026-05-21T05:36:01.637Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "323fe7bd-8f1a-4c98-9ac3-ab2cccc019ed",
  "isSidechain": false,
  "requestId": "req_011CbFAvPPTvHxJ7oEpwiYEe",
  "type": "assistant",
  "uuid": "ce8d9bc9-4620-443f-a8a2-7012c406130e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pn3CG3BF8rJYUkk9gho8Ar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11703,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11703
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

_source line 8 · 2026-05-21T05:36:02.756Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PDEjpeJNHUqYFxSsjBz4Ts`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce8d9bc9-4620-443f-a8a2-7012c406130e",
  "isSidechain": false,
  "requestId": "req_011CbFAvPPTvHxJ7oEpwiYEe",
  "type": "assistant",
  "uuid": "30a886d9-f46c-4c25-b921-5b8a3cf50ee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pn3CG3BF8rJYUkk9gho8Ar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11703,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11703
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

_source line 9 · 2026-05-21T05:36:02.835Z_

<details open><summary>🔧 Tool call — Read · `toolu_01882eZNT13ugpX9KmjecdNA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30a886d9-f46c-4c25-b921-5b8a3cf50ee6",
  "isSidechain": false,
  "requestId": "req_011CbFAvPPTvHxJ7oEpwiYEe",
  "type": "assistant",
  "uuid": "10f5b826-8c3c-49a1-b523-20ffafc89f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pn3CG3BF8rJYUkk9gho8Ar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11703,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11703
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

_source line 10 · 2026-05-21T05:36:02.842Z_

<details><summary>↩ Tool result · `toolu_01882eZNT13ugpX9KmjecdNA`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.
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
31	### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)
32	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty ("method replication to more languages"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).
33	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
34	
35	### Key Empirical Contributions (elevated from appendix to main body, D012)
36	- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.
37	- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.
38	- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.
39	
40	## Story Spine
41	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
42	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
43	- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.
44	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
45	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines."
46	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
47	
48	## Field-Level Significance
49	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
50	
51	## Anticipated Reviewer Concerns & Responses
52	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
53	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
54	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
55	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
56	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
57	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
58	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
59	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
60	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
61	10. **"No mechanistic explanation"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as "geometric analysis" not "mechanistic explanation." **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.
62	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
63	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
64	13. **"CaCLR is your own method — self-debunking is less impactful"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.
65	14. **"CKA is correlational, not mechanistic"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.
66	
67	## Additional Related Work Coverage (Dream-identified gaps)
68	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) "On learning invariant representations for domain adaptation" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.
69	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.
70	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.
71	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.
72	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
73	- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.
74	- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.
75	
76	## Differentiation from Closest Prior Work
77	| Paper | Their Focus | Our Difference |
78	|-------|-------------|----------------|
79	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
80	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
81	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
82	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
83	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10f5b826-8c3c-49a1-b523-20ffafc89f06",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "a9b80b97-d285-469d-8a50-eefbbc4ae48e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  },
  "sourceToolAssistantUUID": "10f5b826-8c3c-49a1-b523-20ffafc89f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T05:36:03.009Z_

<details><summary>↩ Tool result · `toolu_01PDEjpeJNHUqYFxSsjBz4Ts`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B (MoE, INT4)",
4	    "description": "94 层 MoE 模型，每 4 层取一层（24 probed layers），20 种语言，5 种 transfer 条件。 MoE 路由机制在深层创建更强的语言特异化，产生比 7B pilot 更清晰的 Pareto tradeoff。\n",
5	    "results": {
6	      "en_best_auroc": 0.78,
7	      "en_best_layer": 80,
8	      "en_best_layer_depth_pct": 0.851,
9	      "en_auroc_range": [
10	        0.58,
11	        0.78
12	      ],
13	      "en_best_ece_raw": 0.185,
14	      "transfer_optimal_layer_mean": 68,
15	      "transfer_optimal_depth_pct": 0.723,
16	      "en_transfer_layer_gap_pp": 2.8,
17	      "zs_pass_rate": 0.75,
18	      "zs_pass_count": 15,
19	      "zs_mean_auroc_en_optimal": 0.66,
20	      "zs_mean_auroc_transfer_optimal": 0.682,
21	      "pareto_significant_langs": 15,
22	      "pareto_spearman_rho_median": -0.42,
23	      "pareto_spearman_rho_range": [
24	        -0.68,
25	        0.15
26	      ],
27	      "pareto_langs_negative_rho": 16,
28	      "best_zs_auroc_by_tier": {
29	        "HIGH_mean": 0.725,
30	        "MID_mean": 0.672,
31	        "LOW_mean": 0.575
32	      },
33	      "linear_proj_200_mean_auroc": 0.692,
34	      "few_shot_25_mean_auroc": 0.678,
35	      "few_shot_100_mean_auroc": 0.712,
36	      "mean_shift_delta_auroc": 0.0
37	    },
38	    "tables": [
39	      {
40	        "name": "Per-Language ZS AUROC at EN-Optimal Layer (L80)",
41	        "data": "| Tier | Language | ZS AUROC | Best ZS Layer | Pareto rho | Pareto p |\n|------|----------|----------|---------------|------------|----------|\n| HIGH | zh       | 0.732    | L68           | -0.52      | 0.009   |\n| HIGH | es       | 0.741    | L72           | -0.48      | 0.017   |\n| HIGH | fr       | 0.738    | L72           | -0.45      | 0.027   |\n| HIGH | de       | 0.720    | L68           | -0.55      | 0.005   |\n| HIGH | pt       | 0.730    | L72           | -0.41      | 0.046   |\n| HIGH | ja       | 0.710    | L64           | -0.58      | 0.003   |\n| MID  | ar       | 0.690    | L64           | -0.50      | 0.013   |\n| MID  | ru       | 0.700    | L68           | -0.44      | 0.031   |\n| MID  | ko       | 0.685    | L64           | -0.47      | 0.021   |\n| MID  | hi       | 0.665    | L60           | -0.38      | 0.068   |\n| MID  | vi       | 0.678    | L64           | -0.42      | 0.041   |\n| MID  | tr       | 0.655    | L60           | -0.35      | 0.093   |\n| LOW  | sw       | 0.592    | L56           | -0.30      | 0.153   |\n| LOW  | bn       | 0.608    | L60           | -0.32      | 0.126   |\n| LOW  | th       | 0.620    | L60           | -0.37      | 0.075   |\n| LOW  | te       | 0.568    | L56           | -0.22      | 0.301   |\n| LOW  | yo       | 0.542    | L52           | -0.18      | 0.398   |\n| LOW  | am       | 0.530    | L48           | 0.05       | 0.815   |\n"
42	      },
43	      {
44	        "name": "Transfer Method Comparison (mean across 20 languages, L80)",
45	        "data": "| Method              | Mean AUROC | ΔAUROC vs ZS | Sig (paired perm) |\n|---------------------|------------|--------------|-------------------|\n| Zero-shot           | 0.660      | —            | —                 |\n| Mean-shift          | 0.660      | 0.000        | n/a               |\n| CaCLR (best β=0.01) | 0.662      | +0.002       | p=0.42            |\n| Linear proj (50)    | 0.678      | +0.018       | p=0.008           |\n| Linear proj (200)   | 0.692      | +0.032       | p<0.001           |\n| Few-shot 25         | 0.678      | +0.018       | p=0.006           |\n| Few-shot 100        | 0.712      | +0.052       | p<0.001           |\n"
46	      }
47	    ],
48	    "figures": [],
49	    "analysis": "Qwen3-235B 的 MoE 架构产生了比 7B pilot 更清晰的 Pareto frontier：16/20 语言的 depth-transfer rho 为负值，其中 15 个在 p<0.10 显著。Pareto 强度与资源 tier 强相关 （HIGH rho median=-0.49, MID=-0.43, LOW=-0.27），因为低资源语言整体 AUROC 低、 depth variation 也小。MoE 路由机制加速了深层表征的语言特异化——L64-L80 的 expert 激活 模式在不同语言间差异显著增大，解释了 transfer cliff 为何比 dense 7B 更陡。 EN-optimal（L80）vs transfer-optimal（L68）的 gap 为实际部署提供了明确的 layer selection guidance。\n\n\nQwen3-235B 的 MoE 路由在深层为不同语言激活不同 expert，加剧表征语言特异化。 EN best AUROC 从 7B 的 0.754 提升至 ~0.78（+2.6pp），符合模型规模 scaling 预期（22B active params vs 7B, correctness signal 在更大模型中更强但非线性增长）。EN-optimal 在 L80（85% depth）， 而非最终层——MoE 最终层 expert 过度特化导致 probe 质量微降。Pareto tradeoff 比 7B 更清晰： MoE 架构下 CKA cliff 更陡（L64-L80 急剧下降），transfer-optimal 在 L68（72% depth）， EN-optimal 与 transfer-optimal 相差 ~12 层（~3pp AUROC gap），远大于 7B pilot 的 L24 vs L27（~2pp）。 ZS pass rate 75%（15/20）: HIGH 6/6 全通过（共享训练数据充分），MID 6/6 通过（>0.60）， LOW 仅 3/6 通过（yo/am/my 低于 0.55）。Mean-shift 仍然恒等于 0（数学不变性）。 Linear projection 在低资源语言上提升 +0.04-0.08 但在高资源语言上可能微损。\n"
50	  },
51	  {
52	    "name": "Full Pareto Frontier — Llama 4 Scout (MoE, W4A16)",
53	    "description": "48 层 17B-16E MoE，每 4 层取一层（12 probed layers），20 语言，5 transfer 条件。 Llama 架构族在 pilot 中显示弱 Pareto，full-scale 预期延续此模式但 MoE 可能略增 Pareto 强度。\n",
54	    "results": {
55	      "en_best_auroc": 0.76,
56	      "en_best_layer": 44,
57	      "en_best_layer_depth_pct": 0.917,
58	      "en_auroc_range": [
59	        0.6,
60	        0.76
61	      ],
62	      "en_best_ece_raw": 0.195,
63	      "transfer_optimal_layer_mean": 36,
64	      "transfer_optimal_depth_pct": 0.75,
65	      "en_transfer_layer_gap_pp": 1.5,
66	      "zs_pass_rate": 0.7,
67	      "zs_pass_count": 14,
68	      "zs_mean_auroc_en_optimal": 0.643,
69	      "zs_mean_auroc_transfer_optimal": 0.655,
70	      "pareto_significant_langs": 11,
71	      "pareto_spearman_rho_median": -0.28,
72	      "pareto_spearman_rho_range": [
73	        -0.55,
74	        0.35
75	      ],
76	      "pareto_langs_negative_rho": 13,
77	      "best_zs_auroc_by_tier": {
78	        "HIGH_mean": 0.705,
79	        "MID_mean": 0.652,
80	        "LOW_mean": 0.558
81	      },
82	      "linear_proj_200_mean_auroc": 0.673,
83	      "few_shot_25_mean_auroc": 0.662,
84	      "few_shot_100_mean_auroc": 0.693,
85	      "mean_shift_delta_auroc": 0.0
86	    },
87	    "tables": [
88	      {
89	        "name": "Per-Language Pareto Strength Comparison (Qwen3 vs Llama 4)",
90	        "data": "| Tier | Language | Qwen3 rho | Qwen3 p | Llama4 rho | Llama4 p | Pattern       |\n|------|----------|-----------|---------|------------|----------|---------------|\n| HIGH | zh       | -0.52     | 0.009   | -0.40      | 0.198    | Both negative |\n| HIGH | es       | -0.48     | 0.017   | -0.35      | 0.265    | Both negative |\n| HIGH | ja       | -0.58     | 0.003   | -0.48      | 0.115    | Both negative |\n| MID  | ar       | -0.50     | 0.013   | +0.15      | 0.641    | DIVERGENT     |\n| MID  | ko       | -0.47     | 0.021   | +0.22      | 0.489    | DIVERGENT     |\n| MID  | hi       | -0.38     | 0.068   | -0.55      | 0.065    | Both negative |\n| LOW  | sw       | -0.30     | 0.153   | -0.25      | 0.432    | Weak both     |\n| LOW  | yo       | -0.18     | 0.398   | +0.10      | 0.758    | Neither sig   |\n"
91	      },
92	      {
93	        "name": "Architecture Comparison Summary",
94	        "data": "| Metric                        | Qwen3-235B | Llama 4 Scout |\n|-------------------------------|------------|---------------|\n| EN best AUROC                 | 0.78       | 0.76          |\n| Mean ZS AUROC (EN-opt layer)  | 0.660      | 0.643         |\n| Pareto significant langs (/20)| 15         | 11            |\n| Median per-lang Pareto rho    | -0.42      | -0.28         |\n| CKA cliff onset (% depth)    | ~68%       | ~55%          |\n| CKA slope (cliff region)      | -0.025/L   | -0.015/L      |\n"
95	      }
96	    ],
97	    "figures": [],
98	    "analysis": "两个 MoE 架构的 Pareto 差异确认了 pilot 的架构依赖性发现。关键差异不在 MoE vs dense， 而在 CKA depth gradient 的斜率：Qwen3 的急剧 CKA cliff 创建清晰 tradeoff， Llama 4 的渐进下降使 tradeoff 分散。ar/ko 在 Llama 4 上随深度改善的异常模式扩展到 full-scale——这些语言在 Llama tokenizer 中有较好的 subword coverage，深层 expert specialization 反而增强了 correctness signal。此架构依赖性是 observational（n=2 架构， 混杂 scale/layer count/training data），不做因果归因。\n\n\nLlama 4 Scout 延续 Llama-3.1-8B pilot 的弱 Pareto 模式：pilot 中仅 2/5 语言显示 depth-transfer tradeoff（ar/ko 随深度改善），full-scale 中约 7/20 语言不显示 tradeoff 或方向相反。EN AUROC 从 pilot 的 0.728 提升至 0.76（Llama 4 Scout 更大），但提升幅度 小于 Qwen3 的 scaling，因为 Llama 4 的 16-expert MoE 在浅层就开始 expert specialization， correctness signal 在中层已经 plateau。Pareto 弱于 Qwen3 的根本原因：Llama CKA decline 更渐进（slope -0.015/layer vs Qwen 的 -0.025/layer），导致 transfer 不出现急剧 cliff， tradeoff 分散在更宽的层范围内。EN-optimal（L44）vs transfer-optimal（L36）gap 仅 ~1.5pp， 相比 Qwen3 的 ~2.8pp 更小。一些语言（ar, ko, vi）在全深度范围 AUROC 单调增加， 无 tradeoff——pilot 中 ar/ko 的异常模式在 full-scale 中得到确认和扩展。\n"
99	  },
100	  {
101	    "name": "CaCLR Implementation and Negative Result",
102	    "description": "CaCLR (BCE + α·SB-ECE + β·MMD) 完整实现与评估。β sweep 横跨 3 OOM (0.001-1.0)。 Median tier 预期：consistency loss 无效，转为 negative result + geometric explanation。\n",
103	    "results": {
104	      "caclr_mean_delta_auroc_vs_zs": 0.002,
105	      "caclr_best_beta": 0.01,
106	      "caclr_best_alpha": 0.3,
107	      "beta_sweep": {
108	        "beta_0.001": {
109	          "mean_delta_auroc": 0.001,
110	          "p_vs_zs": 0.71
111	        },
112	        "beta_0.01": {
113	          "mean_delta_auroc": 0.003,
114	          "p_vs_zs": 0.42
115	        },
116	        "beta_0.1": {
117	          "mean_delta_auroc": -0.002,
118	          "p_vs_zs": 0.58
119	        },
120	        "beta_1.0": {
121	          "mean_delta_auroc": -0.008,
122	          "p_vs_zs": 0.12
123	        }
124	      },
125	      "alpha_sweep": {
126	        "alpha_0.01": {
127	          "mean_delta_ece": -0.2,
128	          "mean_delta_auroc": 0.0
129	        },
130	        "alpha_0.1": {
131	          "mean_delta_ece": -0.5,
132	          "mean_delta_auroc": -0.001
133	        },
134	        "alpha_1.0": {
135	          "mean_delta_ece": -1.5,
136	          "mean_delta_auroc": -0.004
137	        },
138	        "alpha_10.0": {
139	          "mean_delta_ece": -2.1,
140	          "mean_delta_auroc": -0.012
141	        }
142	      },
143	      "component_ablation": {
144	        "bce_only": {
145	          "auroc": 0.66,
146	          "ece": 0.192
147	        },
148	        "bce_sbece": {
149	          "auroc": 0.658,
150	          "ece": 0.178
151	        },
152	        "bce_mmd": {
153	          "auroc": 0.662,
154	          "ece": 0.19
155	        },
156	        "bce_sbece_mmd": {
157	          "auroc": 0.661,
158	          "ece": 0.176
159	        }
160	      },
161	      "method_comparison_mean_20lang": {
162	        "zero_shot": 0.66,
163	        "mean_shift": 0.66,
164	        "caclr_best": 0.662,
165	        "linear_proj_50": 0.678,
166	        "linear_proj_200": 0.692,
167	        "few_shot_25": 0.678,
168	        "few_shot_100": 0.712
169	      },
170	      "caclr_per_tier_delta": {
171	        "HIGH": 0.001,
172	        "MID": 0.003,
173	        "LOW": 0.002
174	      },
175	      "implementation_spec": {
176	        "mmd_kernel": "Gaussian RBF, median heuristic bandwidth",
177	        "optimizer": "Adam, lr=1e-3, cosine schedule",
178	        "epochs": 50,
179	        "early_stopping": "patience=10 on val BCE loss",
180	        "initialization": "from standard LR solution",
181	        "batch_size": 256,
182	        "mmd_items": "same as BCE (probe_train split)",
183	        "parallel_set_size_range": [
184	          8200,
185	          12800
186	        ]
187	      }
188	    },
189	    "tables": [
190	      {
191	        "name": "β Sweep Results (Qwen3-235B, L80, mean across 20 languages)",
192	        "data": "| β     | Mean AUROC | ΔAUROC vs ZS | 95% Bootstrap CI    | Cohen's d | Interpretation     |\n|-------|------------|--------------|---------------------|-----------|--------------------|\n| 0     | 0.660      | —            | —                   | —         | ZS baseline        |\n| 0.001 | 0.661      | +0.001       | [-0.004, +0.006]    | 0.03      | Negligible         |\n| 0.01  | 0.663      | +0.003       | [-0.003, +0.009]    | 0.07      | Negligible         |\n| 0.1   | 0.658      | -0.002       | [-0.008, +0.004]    | 0.05      | Negligible         |\n| 1.0   | 0.652      | -0.008       | [-0.015, -0.001]    | 0.19      | Slight degradation |\n"
193	      },
194	      {
195	        "name": "CaCLR vs All Methods (mean 20 languages, both models)",
196	        "data": "| Method            | Qwen3 AUROC | Llama4 AUROC | Mean  | Req. labels | Req. parallel |\n|-------------------|-------------|--------------|-------|-------------|---------------|\n| Zero-shot         | 0.660       | 0.643        | 0.652 | 0           | 0             |\n| Mean-shift        | 0.660       | 0.643        | 0.652 | 0           | N (mean only) |\n| CaCLR (best)      | 0.662       | 0.645        | 0.654 | 0           | ~10K parallel |\n| Linear proj (50)  | 0.678       | 0.660        | 0.669 | 0           | 50 pairs      |\n| Linear proj (200) | 0.692       | 0.673        | 0.683 | 0           | 200 pairs     |\n| Few-shot 25       | 0.678       | 0.662        | 0.670 | 25          | 0             |\n| Few-shot 100      | 0.712       | 0.693        | 0.703 | 100         | 0             |\n"
197	      },
198	      {
199	        "name": "CKA Subspace Analysis — Why MMD Fails",
200	        "data": "| Language Tier | Mean subspace angle (EN-target) | MMD after CaCLR | Angle after CaCLR | Interpretation            |\n|--------------|----------------------------------|-----------------|--------------------|-----------------------------|\n| HIGH         | 12°                              | 0.02 → 0.01     | 12° → 11°         | MMD reduces, angle unchanged |\n| MID          | 24°                              | 0.05 → 0.02     | 24° → 23°         | MMD reduces, angle unchanged |\n| LOW          | 42°                              | 0.12 → 0.05     | 42° → 40°         | MMD reduces, angle unchanged |\n"
201	      }
202	    ],
203	    "figures": [],
204	    "analysis": "CaCLR negative result 的核心贡献不是 method 本身，而是 (1) systematic β sweep 关闭 MMD distributional-matching 路径（3 OOM, component ablation, 两个架构 × 20 语言）， (2) CKA subspace analysis 提供几何解释——MMD 成功减小了 marginal distance 但完全 无法对齐 correctness subspace 的方向（subspace angle 几乎不变）。这验证了 Zhao et al. (2019) 的理论预测：当 conditional distributions P(Y|X) 在域间不同时， marginal matching 必然失败。在 correctness probing 中，P(correct|activation) 的 条件结构在不同语言间确实不同（语言特异的 capability 成分），因此 MMD 注定无效。 Constructive path: linear projection 以 50-80 parallel pairs 的极低成本解决了 subspace alignment 问题，是明确的 practical recommendation。\n\n\nCaCLR 的 MMD consistency loss 在 1-D probe logit 空间操作——这是设计层面的根本局限。 Correctness direction 是高维 activation 空间中的低维子空间特征（~1-3 维），MMD 匹配 probe logit 的边际分布（均值和方差）但无法对齐子空间内的方向结构。具体地：两种语言的 probe logit 分布可能有相似的均值和方差（MMD 小），但 correctness direction 在 activation 空间中的朝向不同——MMD 无法检测或纠正这种旋转。β=0.001-0.01 时 consistency loss 太弱， 无实质效果；β=0.1-1.0 时 consistency loss 开始干扰 BCE 训练（AUROC 下降），因为 强制匹配边际分布反而破坏了 EN probe 已经学到的 correctness direction。这不是 hyperparameter 问题——是根本的 architectural mismatch。α (SB-ECE) 对 ECE 有轻微改善 是预期的（ECE loss 直接优化 calibration），但与 cross-lingual transfer 无关。 Linear projection 成功因为它直接学习子空间旋转矩阵（Procrustes alignment）， 绕过了 distributional matching 的局限。这一对比（MMD 失败 vs linear projection 成功） 提供了对 Zhao et al. (2019) conditional-marginal mismatch theory 的实证验证。\n"
205	  },
206	  {
207	    "name": "Difficulty-Controlled Decomposition Ablation",
208	    "description": "IRT difficulty probes → project out difficulty direction → retrain correctness probes → evaluate transfer。 10 代表语言 × 8 代表层 × 两个模型。含 random-direction control。 Median tier: 定性分离成立但 prescriptive 预测能力不可靠。\n",
209	    "results": {
210	      "mean_delta_auroc_difficulty_projected": 0.012,
211	      "delta_auroc_range": [
212	        -0.008,
213	        0.025
214	      ],
215	      "langs_with_positive_delta": 7,
216	      "langs_with_negative_delta": 3,
217	      "random_direction_mean_delta": 0.005,
218	      "difficulty_vs_random_ratio": 2.4,
219	      "difficulty_probe_r2": 0.35,
220	      "per_lang_results": {
221	        "zh": {
222	          "delta": 0.008,
223	          "sig": false
224	        },
225	        "es": {
226	          "delta": 0.01,
227	          "sig": false
228	        },
229	        "fr": {
230	          "delta": 0.012,
231	          "sig": true
232	        },
233	        "de": {
234	          "delta": 0.015,
235	          "sig": true
236	        },
237	        "hi": {
238	          "delta": 0.022,
239	          "sig": true
240	        },
241	        "ru": {
242	          "delta": 0.018,
243	          "sig": true
244	        },
245	        "ko": {
246	          "delta": -0.005,
247	          "sig": false
248	        },
249	        "tr": {
250	          "delta": 0.02,
251	          "sig": true
252	        },
253	        "sw": {
254	          "delta": -0.008,
255	          "sig": false
256	        },
257	        "bn": {
258	          "delta": 0.025,
259	          "sig": true
260	        }
261	      },
262	      "prescriptive_accuracy": 0.58
263	    },
264	    "tables": [
265	      {
266	        "name": "Decomposition Results by Language (Qwen3-235B, 8-layer mean)",
267	        "data": "| Language | Tier | Full AUROC | Diff-projected AUROC | ΔAUROC  | Random-proj AUROC | Rand ΔAUROC |\n|----------|------|------------|----------------------|---------|-------------------|-------------|\n| zh       | HIGH | 0.725      | 0.733                | +0.008  | 0.729             | +0.004      |\n| es       | HIGH | 0.735      | 0.745                | +0.010  | 0.740             | +0.005      |\n| fr       | HIGH | 0.732      | 0.744                | +0.012  | 0.737             | +0.005      |\n| de       | HIGH | 0.715      | 0.730                | +0.015  | 0.721             | +0.006      |\n| hi       | MID  | 0.658      | 0.680                | +0.022  | 0.665             | +0.007      |\n| ru       | MID  | 0.695      | 0.713                | +0.018  | 0.702             | +0.007      |\n| ko       | MID  | 0.680      | 0.675                | -0.005  | 0.683             | +0.003      |\n| tr       | MID  | 0.650      | 0.670                | +0.020  | 0.656             | +0.006      |\n| sw       | LOW  | 0.585      | 0.577                | -0.008  | 0.588             | +0.003      |\n| bn       | LOW  | 0.602      | 0.627                | +0.025  | 0.608             | +0.006      |\n"
268	      }
269	    ],
270	    "figures": [],
271	    "analysis": "Decomposition 分析支持 \"correctness transfer 确实包含 difficulty-shared 和 capability-specific 两个成分\" 的定性结论，但 prescriptive accuracy (58%) 与随机猜测差距过小（chance=50%）， 无法作为实际策略选择工具。弱化 Claim 2 为 \"descriptive separation observed in most language-architecture combinations; however, the decomposition does not reliably predict optimal alignment strategy.\" 纸面贡献仍在：这是首次在跨语言 probing 中尝试 difficulty- capability 分解，定性结果与 Civelli et al. 的 difficulty transfer 文献一致。 ko/sw 的反常模式（projection 损害 AUROC）值得单独分析——可能是因为这些语言的 difficulty ordering 与英语差异较大（文化特异的知识题目分布不同）。\n\n\nDifficulty decomposition 的定性逻辑成立：difficulty 成分确实是跨语言共享的（IRT difficulty 与语言无关），project out 后 residual 应该更 capability-specific。但 prescriptive 力弱 的原因有三：(1) IRT difficulty probe 的 R²=0.35 意味着 difficulty direction 只解释了 35% 的方差，projection 不完全；(2) difficulty 和 capability 在 activation 空间中不正交—— projection 同时移除了部分 capability 信息（ko/sw 中 AUROC 下降）；(3) 不同语言中 difficulty-capability 纠缠程度不同——高资源语言 capability 独立于 difficulty（projection 帮助），低资源语言两者纠缠更深（projection 效果不确定）。Random-direction control 显示 ~40% 的效果来自纯维度缩减（从高维投影到低维本身就降噪），只有 ~60% 是 difficulty-specific。这足以支持 \"descriptive separation observed\" 但不足以支持 \"prescriptive decomposition predicts optimal strategy\"。Prescriptive accuracy 仅 58% （随机猜 50%），几乎无实际预测价值。\n"
272	  },
273	  {
274	    "name": "Cross-Lingual Orthogonality Analysis",
275	    "description": "提取 verbalized confidence direction，计算与 correctness direction 的 cosine similarity， 20 语言 × 2 架构。作为 Claim 4 的 supporting evidence（subsection）。\n",
276	    "results": {
277	      "mean_cosine_all": 0.038,
278	      "cosine_range": [
279	        0.008,
280	        0.142
281	      ],
282	      "langs_below_0.05": 14,
283	      "langs_below_0.10": 18,
284	      "langs_above_0.10": 2,
285	      "per_tier_mean_cosine": {
286	        "HIGH": 0.028,
287	        "MID": 0.042,
288	        "LOW": 0.072
289	      },
290	      "architecture_comparison": {
291	        "qwen3_mean": 0.035,
292	        "llama4_mean": 0.041
293	      },
294	      "outlier_langs": [
295	        "am",
296	        "yo"
297	      ],
298	      "outlier_cosine": [
299	        0.142,
300	        0.118
301	      ]
302	    },
303	    "tables": [
304	      {
305	        "name": "Cosine Similarity by Resource Tier",
306	        "data": "| Tier | n  | Mean cosine | Std  | Min   | Max   | < 0.05 | < 0.10 |\n|------|----|-------------|------|-------|-------|--------|--------|\n| HIGH | 6  | 0.028       | 0.012| 0.012 | 0.045 | 5      | 6      |\n| MID  | 8  | 0.042       | 0.018| 0.018 | 0.075 | 5      | 8      |\n| LOW  | 6  | 0.072       | 0.042| 0.025 | 0.142 | 2      | 4      |\n"
307	      }
308	    ],
309	    "figures": [],
310	    "analysis": "Orthogonality 作为 subsection supporting evidence 充分：18/20 语言 cosine < 0.10， 14/20 < 0.05。结论简洁：\"output-based calibration 的结构性局限（correctness-confidence orthogonality）跨语言稳健，强化了 probe-based 方法的必要性。\" am/yo 的高 cosine 值须与 plan_013 control task 结果交叉验证，确认是 probe artifact 而非真实 alignment。\n\n\nMiao & Ungar (2026) 在 English 7-8B 模型上发现 cosine < 0.04。跨语言扩展时， HIGH 资源语言复现此结果（模型在这些语言上有足够训练数据，correctness 和 confidence direction 分化清晰）。MID 语言 cosine 略高（0.04-0.06）因为 confidence direction 在 中资源语言上更嘈杂（模型对这些语言的 verbalized confidence 不够稳定）。LOW 语言中 am/yo 出现较高 cosine（>0.10）——这不是真正的 correctness-confidence alignment， 而是 probe capacity artifact：在低资源语言上两个 direction 都很弱，cosine 被噪声主导。 plan_013 control task 将确认这些语言的 selectivity 低于阈值。整体结论不变： orthogonality 是跨语言稳健的结构性质，output-based calibration 的局限性与语言无关。 两个架构差异微小（0.035 vs 0.041），不具有统计显著性。\n"
311	  },
312	  {
313	    "name": "Probe Complexity Comparison (LR vs 2-layer MLP)",
314	    "description": "每层每模型对比 logistic regression 和 2-layer MLP 的 EN accuracy、cross-lingual transfer degradation 和 calibration quality。CPU-bound，使用缓存 activations。\n",
315	    "results": {
316	      "lr_en_best_auroc_qwen3": 0.78,
317	      "mlp_en_best_auroc_qwen3": 0.802,
318	      "lr_mean_zs_auroc_qwen3": 0.66,
319	      "mlp_mean_zs_auroc_qwen3": 0.632,
320	      "lr_transfer_gap_qwen3": 0.12,
321	      "mlp_transfer_gap_qwen3": 0.17,
322	      "lr_en_best_auroc_llama4": 0.76,
323	      "mlp_en_best_auroc_llama4": 0.778,
324	      "lr_mean_zs_auroc_llama4": 0.643,
325	      "mlp_mean_zs_auroc_llama4": 0.618,
326	      "mlp_en_advantage_pp": 2.0,
327	      "lr_transfer_advantage_pp": 2.8,
328	      "lr_preferred_for_transfer": true
329	    },
330	    "tables": [
331	      {
332	        "name": "LR vs MLP Transfer Comparison (mean across 20 languages)",
333	        "data": "| Metric                    | Qwen3 LR | Qwen3 MLP | Llama4 LR | Llama4 MLP |\n|---------------------------|----------|-----------|-----------|------------|\n| EN best AUROC             | 0.780    | 0.802     | 0.760     | 0.778      |\n| Mean ZS AUROC             | 0.660    | 0.632     | 0.643     | 0.618      |\n| Transfer gap (EN - ZS)    | 0.120    | 0.170     | 0.117     | 0.160      |\n| EN ECE                    | 0.185    | 0.172     | 0.195     | 0.182      |\n| Mean ZS ECE               | 0.225    | 0.252     | 0.232     | 0.260      |\n| ZS pass rate (>0.60)      | 75%      | 60%       | 70%       | 55%        |\n"
334	      }
335	    ],
336	    "figures": [],
337	    "analysis": "LR vs MLP 对比验证了 linear probe 是 cross-lingual transfer 的正确选择。 MLP 的额外容量在 EN 上有用但在迁移中有害——这与 Hewitt & Liang (2019) 关于 probe complexity 的讨论一致。Paper 方法论选择（LR）有实证支持。\n\n\nMLP（2 层, ~256 hidden units）有更多参数来拟合 EN correctness signal，EN AUROC 提升 ~2pp。但额外容量同时学到了 EN-specific 的 activation pattern（如 English 特有的 token position bias, subject-verb agreement cues），这些 pattern 不跨语言迁移。 LR 被迫学习更简洁的 direction（1 个超平面），这个 direction 更可能对应语言无关的 correctness subspace。Transfer gap（EN - mean ZS）: LR 12pp vs MLP 17pp——MLP 多出的 5pp gap 恰好对应其 EN advantage 的 2pp + 额外 3pp 的 EN-specific overfitting。 这为 paper 的方法论选择（使用 LR probe）提供了实证支持。\n"
338	  },
339	  {
340	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
341	    "description": "在 Belebele（阅读理解）和 MMLU-ProX（翻译 MMLU）上评估 best probes + 所有 transfer 方法，验证 generalization beyond GlobalMMLU。20 语言 × 2 模型。\n",
342	    "results": {
343	      "belebele": {
344	        "en_best_auroc": 0.74,
345	        "mean_zs_auroc": 0.625,
346	        "zs_pass_rate": 0.6,
347	        "pareto_preserved": true,
348	        "pareto_strength": "weaker than GlobalMMLU",
349	        "rank_correlation_with_globalmmlu": 0.82
350	      },
351	      "mmlu_prox": {
352	        "en_best_auroc": 0.77,
353	        "mean_zs_auroc": 0.648,
354	        "zs_pass_rate": 0.7,
355	        "pareto_preserved": true,
356	        "pareto_strength": "comparable to GlobalMMLU",
357	        "rank_correlation_with_globalmmlu": 0.91
358	      },
359	      "linear_proj_generalizes": true,
360	      "caclr_still_inert": true,
361	      "cross_benchmark_lang_ranking_rho": 0.88
362	    },
363	    "tables": [
364	      {
365	        "name": "Cross-Benchmark Comparison (mean across 20 languages, Qwen3-235B)",
366	        "data": "| Metric             | GlobalMMLU | Belebele | MMLU-ProX |\n|--------------------|------------|----------|-----------|\n| EN best AUROC      | 0.78       | 0.74     | 0.77      |\n| Mean ZS AUROC      | 0.660      | 0.625    | 0.648     |\n| ZS pass rate       | 75%        | 60%      | 70%       |\n| Pareto langs (/20) | 15         | 12       | 14        |\n| Linear proj Δ      | +0.032     | +0.028   | +0.030    |\n| CaCLR Δ            | +0.002     | +0.001   | +0.002    |\n"
367	      }
368	    ],
369	    "figures": [],
370	    "analysis": "Cross-benchmark 泛化确认了主要发现的稳健性。Belebele 上 Pareto 更弱是预期的 （RC task 的 correctness signal 与 knowledge MCQA 不同），但关键模式（架构差异、 resource tier 梯度、CaCLR 无效、linear projection 有效）在所有 benchmark 上一致。 这为 paper 的 claim 提供了必要的泛化验证。\n\n\nBelebele 是阅读理解任务，与 GlobalMMLU 的知识型 MCQA 不同——correctness signal 的性质不完全相同（RC 依赖 passage comprehension, MCQA 依赖 parametric knowledge）， 所以 EN AUROC 略低（0.74 vs 0.78）且 transfer 更差。但 Pareto 结构保留，因为 depth-transferability tradeoff 是 representation geometry 的性质，不依赖特定任务。 MMLU-ProX 与 GlobalMMLU 高度相关（同源翻译数据），所以模式几乎一致。 Language ranking 在 benchmarks 间高度相关（rho=0.88）——确认结果不是 benchmark-specific。 CaCLR 在两个 benchmark 上仍无效，linear projection 仍有效——泛化性确认。\n"
371	  },
372	  {
373	    "name": "Quantization Validation Ablation",
374	    "description": "(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4 vs FP16 for Qwen3-235B at 5 layers, 5% subset. 验证量化不扭曲 correctness signal。\n",
375	    "results": {
376	      "llama4_w4a16_vs_fp16": {
377	        "mean_abs_delta_auroc": 0.005,
378	        "max_abs_delta_auroc": 0.009,
379	        "direction": "mixed (2 positive, 3 negative)",
380	        "cka_fp16_vs_quant": 0.985
381	      },
382	      "qwen3_int4_vs_fp16": {
383	        "mean_abs_delta_auroc": 0.006,
384	        "max_abs_delta_auroc": 0.011,
385	        "direction": "mixed (3 positive, 2 negative)",
386	        "cka_fp16_vs_quant": 0.978
387	      },
388	      "quantization_safe": true
389	    },
390	    "tables": [
391	      {
392	        "name": "Quantization Validation (per-layer ΔAUROC)",
393	        "data": "| Model      | Layer (% depth) | FP16 AUROC | Quant AUROC | ΔAUROC  |\n|------------|-----------------|------------|-------------|---------|\n| Llama4     | L8 (17%)        | 0.632      | 0.629       | -0.003  |\n| Llama4     | L16 (33%)       | 0.685      | 0.688       | +0.003  |\n| Llama4     | L24 (50%)       | 0.720      | 0.715       | -0.005  |\n| Llama4     | L36 (75%)       | 0.748      | 0.741       | -0.007  |\n| Llama4     | L44 (92%)       | 0.760      | 0.762       | +0.002  |\n| Qwen3      | L16 (17%)       | 0.628      | 0.622       | -0.006  |\n| Qwen3      | L36 (38%)       | 0.702      | 0.705       | +0.003  |\n| Qwen3      | L52 (55%)       | 0.738      | 0.734       | -0.004  |\n| Qwen3      | L68 (72%)       | 0.768      | 0.772       | +0.004  |\n| Qwen3      | L80 (85%)       | 0.780      | 0.769       | -0.011  |\n"
394	      }
395	    ],
396	    "figures": [],
397	    "analysis": "Quantization validation 通过——所有 ΔAUROC < 0.012，CKA > 0.97。 Qwen3 L80 的 ΔAUROC=-0.011 是最大偏差，但仍在 bootstrap CI 范围内 且不影响 EN-optimal layer 的选择。Paper 中报告为 \"quantization artifacts are negligible for correctness probing (max |ΔAUROC| < 0.012 across all validated layers)\"。\n\n\n4-bit weight quantization 保留了 activation 空间的大部分结构——correctness signal 是高维 activation 空间中的低维子空间特征，quantization noise 主要分布在与 correctness direction 正交的维度上（根据 random projection 理论，低维结构 在高维 noise 下稳健）。ΔAUROC < 0.01 在 bootstrap CI 内，不影响任何结论。 Qwen3 的 MoE 量化略有更大 delta（expert routing 决策在 INT4 下可能微变）， 但仍在可接受范围。CKA(FP16, quant) > 0.97 确认 activation 空间整体结构保留。\n"
398	  },
399	  {
400	    "name": "Full CKA Cross-Lingual Similarity & Simpson's Paradox Analysis",
401	    "description": "Linear CKA between EN and 20 target languages at every probed layer, both models. 核心分析：partial correlation controlling for depth（Simpson's Paradox 验证）。 Median tier: 仅 Llama 4 Scout 上显著，Qwen3 上 trending but not significant。\n",
402	    "results": {
403	      "qwen3": {
404	        "raw_spearman_cka_auroc": -0.22,
405	        "raw_p": 0.001,
406	        "partial_spearman_ctrl_depth": 0.16,
407	        "partial_p": 0.072,
408	        "significant": false,
409	        "per_layer_positive_rho_count": 17,
410	        "per_layer_total": 24,
411	        "per_layer_significant_count": 5,
412	        "cka_cliff_onset_layer": 64,
413	        "cka_cliff_onset_depth_pct": 0.68,
414	        "cka_final_layer_mean": 0.1,
415	        "cka_peak_layer": 36,
416	        "cka_peak_mean": 0.81
417	      },
418	      "llama4": {
419	        "raw_spearman_cka_auroc": -0.28,
420	        "raw_p": 0.001,
421	        "partial_spearman_ctrl_depth": 0.29,
422	        "partial_p": 0.018,
423	        "significant": true,
424	        "per_layer_positive_rho_count": 10,
425	        "per_layer_total": 12,
426	        "per_layer_significant_count": 4,
427	        "cka_cliff_onset_layer": 24,
428	        "cka_cliff_onset_depth_pct": 0.5,
429	        "cka_final_layer_mean": 0.22,
430	        "cka_peak_layer": 12,
431	        "cka_peak_mean": 0.82
432	      },
433	      "simpson_paradox_confirmed": "partial (1/2 architectures)",
434	      "subspace_angle_analysis": {
435	        "qwen3_mean_angle_HIGH": 10,
436	        "qwen3_mean_angle_MID": 22,
437	        "qwen3_mean_angle_LOW": 45,
438	        "llama4_mean_angle_HIGH": 12,
439	        "llama4_mean_angle_MID": 25,
440	        "llama4_mean_angle_LOW": 40
441	      },
442	      "cka_transfer_collapse_threshold": 0.32,
443	      "bootstrap_ci_partial_rho_qwen3": [
444	        -0.02,
445	        0.34
446	      ],
447	      "bootstrap_ci_partial_rho_llama4": [
448	        0.06,
449	        0.5
450	      ]
451	    },
452	    "tables": [
453	      {
454	        "name": "Simpson's Paradox — Raw vs Partial Correlation",
455	        "data": "| Model       | n   | Raw rho | Raw p   | Partial rho | Partial p | Boot 95% CI      | Sig?   |\n|-------------|-----|---------|---------|-------------|-----------|------------------|--------|\n| Qwen3-235B  | 480 | -0.22   | <0.001  | +0.16       | 0.072     | [-0.02, +0.34]   | No     |\n| Llama4 Scout| 240 | -0.28   | <0.001  | +0.29       | 0.018     | [+0.06, +0.50]   | Yes    |\n| Pilot Llama | 45  | -0.16   | 0.294   | +0.41       | 0.006     | [+0.12, +0.65]   | Yes    |\n| Pilot Qwen  | 40  | -0.16   | 0.310   | +0.18       | 0.274     | [-0.15, +0.48]   | No     |\n"
456	      },
457	      {
458	        "name": "Per-Layer Cross-Language Spearman (CKA vs AUROC, n=20 per layer)",
459	        "data": "| Layer group        | Qwen3 median rho | Qwen3 sig layers | Llama4 median rho | Llama4 sig layers |\n|--------------------|------------------|------------------|-------------------|-------------------|\n| 0-25% depth        | +0.15            | 0/6              | +0.22             | 1/3               |\n| 25-50% depth       | +0.38            | 2/6              | +0.45             | 2/3               |\n| 50-75% depth       | +0.42            | 2/6              | +0.52             | 2/3               |\n| 75-100% depth      | +0.28            | 1/6              | +0.35             | 1/3               |\n"
460	      },
461	      {
462	        "name": "CKA Depth Profile (mean across 20 languages)",
463	        "data": "| Depth % | Qwen3 Layer | Qwen3 CKA | Llama4 Layer | Llama4 CKA |\n|---------|-------------|-----------|--------------|------------|\n| 0%      | 0           | 0.72      | 0            | 0.60       |\n| 17%     | 16          | 0.75      | 8            | 0.80       |\n| 34%     | 32          | 0.80      | 16           | 0.76       |\n| 51%     | 48          | 0.78      | 24           | 0.58       |\n| 68%     | 64          | 0.62      | 32           | 0.42       |\n| 77%     | 72          | 0.40      | 36           | 0.35       |\n| 85%     | 80          | 0.25      | 40           | 0.30       |\n| 94%     | 88          | 0.14      | 44           | 0.25       |\n| 100%    | 92          | 0.10      | 48           | 0.22       |\n"
464	      },
465	      {
466	        "name": "Subspace Angle Analysis (correctness direction EN vs target)",
467	        "data": "| Tier | Qwen3 mean angle | Llama4 mean angle | Mean ZS AUROC | Interpretation         |\n|------|------------------|-------------------|---------------|------------------------|\n| HIGH | 10°              | 12°               | 0.715         | Near-aligned           |\n| MID  | 22°              | 25°               | 0.662         | Modest rotation        |\n| LOW  | 45°              | 40°               | 0.567         | Substantial misalignment|\n"
468	      }
469	    ],
470	    "figures": [],
471	    "analysis": "Simpson's Paradox 在 full-scale 上部分确认：Llama 4 Scout 上统计显著（partial rho=0.29, p=0.018），Qwen3-235B 上 trending 但不显著（partial rho=0.16, p=0.072）。 这一架构依赖性本身是有意义的发现。Paper 中用 hedged language 报告： \"In architectures where the CKA-depth gradient is steep (Llama 4 Scout), partial correlation controlling for depth reveals a significant positive relationship between CKA and transfer AUROC (rho=0.29, p=0.018), indicating that CKA provides genuine explanatory power beyond depth. In architectures with a delayed, step-function-like CKA decline (Qwen3-235B), the linear partial correlation is trending but not significant (rho=0.16, p=0.072), possibly because the non-linear depth-CKA relationship reduces the effectiveness of linear depth control.\" Subspace angle analysis 提供了 CKA 分析的定量补充——HIGH 语言角度小（zero-shot 可行）， LOW 语言角度大（需要 alignment）——这与 Procrustes reversal 发现互洽。\n\n\nSimpson's Paradox 的架构依赖性源于 CKA-depth gradient 的形状差异。 Llama 4 Scout 的 CKA depth gradient 更陡峭（从 peak 0.82 at L12 到 final 0.22 at L48, slope ~ -0.017/layer），这使得 depth confound 更强——controlling for depth 释放了更多 CKA 的独立解释力（partial rho=0.29, p=0.018）。Qwen3 的 CKA decline 起始更晚 （L64 才开始急降）且更集中在最深层，depth confound 的影响不均匀——前 60% 层几乎 无 CKA 变化，后 30% 急降——这种非线性使得 linear partial correlation 效果较差 （partial rho=0.16, p=0.072）。这不意味 CKA 在 Qwen3 上无解释力，而是 linear depth control 不够——可能需要 non-linear depth control（如 depth²）才能捕捉 Qwen3 的 step-function-like CKA profile。但 paper 应诚实报告：standard partial correlation 仅在 Llama 上显著。Per-layer analysis: 两个模型 70-83% 的 per-layer rho 为正（Qwen 17/24, Llama 10/12），但因每层仅 n=20 语言，个别层的 significance 有限。Full-scale 的 n=20 per layer 比 pilot 的 n=5 有更多 power，但仍不足以让所有 per-layer rho 显著。 Subspace angle 分析提供定量补充：HIGH 语言角度小（10-12°）→ 零样本迁移好， LOW 语言角度大（40-45°）→ 需要 alignment。CKA collapse threshold ~0.32 是 transfer 从 \"reasonable\" 骤降到 \"chance-level\" 的拐点。\n"
472	  },
473	  {
474	    "name": "Linear Projection Sensitivity & Procrustes Effect Reversal",
475	    "description": "Vary parallel pairs (10, 20, 50, 100, 200) for linear projection。 两模型 × 5 代表层 × 20 语言。Resource-tier stratified saturation curves。 含 Procrustes effect reversal 分析。\n",
476	    "results": {
477	      "overall_pairs_to_95pct": 70,
478	      "per_tier_pairs_to_95pct": {
479	        "HIGH": 35,
480	        "MID": 55,
481	        "LOW": 75
482	      },
483	      "saturation_curve": {
484	        "pairs_10": {
485	          "pct_of_max": 0.42,
486	          "mean_delta_auroc": 0.013
487	        },
488	        "pairs_20": {
489	          "pct_of_max": 0.62,
490	          "mean_delta_auroc": 0.02
491	        },
492	        "pairs_50": {
493	          "pct_of_max": 0.84,
494	          "mean_delta_auroc": 0.027
495	        },
496	        "pairs_100": {
497	          "pct_of_max": 0.95,
498	          "mean_delta_auroc": 0.03
499	        },
500	        "pairs_200": {
501	          "pct_of_max": 1.0,
502	          "mean_delta_auroc": 0.032
503	        }
504	      },
505	      "procrustes_reversal": {
506	        "threshold_estimate": 0.55,
507	        "threshold_ci_95": [
508	          0.46,
509	          0.63
510	        ],
511	        "benefit_below_0.50": {
512	          "mean_delta": 0.058,
513	          "n_langs": 4
514	        },
515	        "ambiguous_0.50_0.62": {
516	          "mean_delta": 0.012,
517	          "n_langs": 8
518	        },
519	        "harm_above_0.62": {
520	          "mean_delta": -0.018,
521	          "n_langs": 8
522	        }
523	      },
524	      "curve_cleanness": "noisy, especially LOW tier (R² of saturation fit: HIGH=0.96, MID=0.91, LOW=0.78)"
525	    },
526	    "tables": [
527	      {
528	        "name": "Saturation Curves by Resource Tier (Qwen3-235B, L68)",
529	        "data": "| Pairs | HIGH ΔAUROC | MID ΔAUROC | LOW ΔAUROC | Overall ΔAUROC |\n|-------|-------------|------------|------------|----------------|\n| 10    | +0.002      | +0.010     | +0.028     | +0.013         |\n| 20    | +0.005      | +0.018     | +0.042     | +0.020         |\n| 50    | +0.007      | +0.026     | +0.054     | +0.027         |\n| 100   | +0.008      | +0.029     | +0.060     | +0.030         |\n| 200   | +0.008      | +0.030     | +0.063     | +0.032         |\n"
530	      },
531	      {
532	        "name": "Procrustes Effect Reversal by ZS AUROC Band",
533	        "data": "| ZS AUROC band | n langs | Mean Δ from proj | Std   | % positive | Example langs |\n|---------------|---------|------------------|-------|------------|---------------|\n| < 0.50        | 4       | +0.058           | 0.022 | 100%       | am, yo, my, te|\n| 0.50 - 0.55   | 2       | +0.035           | 0.018 | 100%       | sw, bn        |\n| 0.55 - 0.60   | 2       | +0.012           | 0.015 | 75%        | th, tr        |\n| 0.60 - 0.65   | 4       | +0.003           | 0.012 | 50%        | hi, vi, ko, ar|\n| 0.65 - 0.70   | 4       | -0.008           | 0.010 | 25%        | ru, ja, de, pt|\n| > 0.70        | 4       | -0.018           | 0.008 | 0%         | zh, es, fr, ...  |\n"
534	      }
535	    ],
536	    "figures": [],
537	    "analysis": "Linear projection 的 sample efficiency 是最直接的 practical contribution： 70 parallel pairs（约 2-3 小时标注工作）达到 95% of maximum improvement。 Resource-tier stratification 为 practitioners 提供指导：HIGH 语言不需要 projection （可能有害），LOW 语言需要 ~75 pairs。Procrustes reversal 是重要的 practitioner caveat： 不加区分地对所有语言做 alignment 会损害已经 well-aligned 的语言。 建议 deployment strategy: 先测试 zero-shot AUROC，低于 0.55 时使用 linear projection， 高于 0.62 时直接使用 zero-shot。\n\n\nLinear projection（Procrustes alignment）通过学习 EN→target 的旋转矩阵对齐 correctness subspace。Saturation 速度取决于子空间旋转的复杂度：HIGH 语言的 EN-target subspace 角度小（~10°），10-20 pairs 就足以估计一个简单旋转，35 pairs 达到 95%；LOW 语言角度大 （~40-45°），需要更多 pairs 来稳定估计更复杂的旋转，75 pairs 才达到 95%。 Overall 70 pairs（而非 pilot 预估的 ~50 pairs）因为 (1) 20 语言比 5 语言引入更多方差， (2) 部分低资源语言的 parallel data 翻译质量低（机翻 artifacts），增加了 noise。 Curves 在 LOW tier 不够干净（R²=0.78）——个别语言的饱和曲线不单调（20 pairs 时偶然 好于 50 pairs），因为 parallel pair 的质量方差大。 Procrustes reversal 的机制：当 ZS AUROC 已高（>0.62），EN probe 的 correctness direction 与 target 语言已经 well-aligned（subspace angle <15°），Procrustes 旋转引入的估计噪声 反而大于 alignment gain→净效果为负。当 ZS AUROC 低（<0.50），严重 misalignment （angle >40°）使得 Procrustes 的 alignment gain 远大于估计噪声→净效果明显为正。 阈值 ~0.55 对应 subspace angle ~20-25° 的平衡点。\n"
538	  },
539	  {
540	    "name": "Probing Control Tasks (Hewitt & Liang 2019) — Full Scale",
541	    "description": "随机排列标签训练 control probes，计算 selectivity (real - control AUROC)， 2 模型 × 20 语言 × 所有 probed 层。验证 AUROC 反映 genuine correctness direction。\n",
542	    "results": {
543	      "artifact_rate_low_resource": 0.3,
544	      "artifact_rate_mid_resource": 0.28,
545	      "artifact_rate_high_resource": 0.06,
546	      "artifact_threshold_selectivity": 0.05,
547	      "overall_artifact_rate": 0.18,
548	      "en_selectivity_profile": {
549	        "shallow": 0.03,
550	        "mid": 0.12,
551	        "deep": 0.25
552	      },
553	      "per_tier_selectivity_deep_layers": {
554	        "HIGH": 0.22,
555	        "MID": 0.14,
556	        "LOW": 0.06
557	      },
558	      "control_auroc_range": [
559	        0.48,
560	        0.52
561	      ],
562	      "affected_layer_range": "primarily layers 0-40% depth"
563	    },
564	    "tables": [
565	      {
566	        "name": "Artifact Rate by Resource Tier and Depth (Qwen3-235B)",
567	        "data": "| Depth zone     | HIGH artifact % | MID artifact % | LOW artifact % |\n|----------------|-----------------|----------------|----------------|\n| 0-25% depth    | 17%             | 58%            | 83%            |\n| 25-50% depth   | 4%              | 33%            | 67%            |\n| 50-75% depth   | 0%              | 17%            | 17%            |\n| 75-100% depth  | 0%              | 4%             | 0%             |\n| Overall        | 6%              | 28%            | 30%            |\n"
568	      },
569	      {
570	        "name": "Selectivity at EN-Optimal Layer by Language",
571	        "data": "| Tier | Language | Real AUROC | Control AUROC | Selectivity | Artifact? |\n|------|----------|------------|---------------|-------------|-----------|\n| HIGH | zh       | 0.732      | 0.498         | 0.234       | No        |\n| HIGH | es       | 0.741      | 0.495         | 0.246       | No        |\n| MID  | hi       | 0.665      | 0.502         | 0.163       | No        |\n| MID  | tr       | 0.655      | 0.508         | 0.147       | No        |\n| LOW  | sw       | 0.592      | 0.505         | 0.087       | No        |\n| LOW  | bn       | 0.608      | 0.501         | 0.107       | No        |\n| LOW  | yo       | 0.542      | 0.510         | 0.032       | YES       |\n| LOW  | am       | 0.530      | 0.512         | 0.018       | YES       |\n"
572	      }
573	    ],
574	    "figures": [],
575	    "analysis": "Control task 发现是独立的 methodological contribution：首次在 cross-lingual probing 中 系统性应用 Hewitt & Liang selectivity analysis，发现 ~30% low-resource 和 ~28% mid-resource language-layer 组合的 probing results 不可靠。Field-level implication: 所有 cross-lingual probing 研究（包括 Xiao et al.）应包含 selectivity checks。 在 paper 中：(1) 用 selectivity threshold 过滤不可靠结果后重新报告 main results （确认过滤后结论不变），(2) 将过滤信息作为 methodological recommendation 在 main body 报告（不只是 appendix），(3) 讨论与 Voita & Titov MDL probes 的关系。\n\n\nPilot（Qwen2.5-7B, EN）显示 selectivity 在浅层低（L0-L12: 0.02-0.04）、深层高 （L20-L27: 0.24-0.26）。跨语言扩展时，LOW 资源语言的 selectivity 全面下降： (1) 这些语言的 activations 中 correctness signal 更弱（模型对这些语言\"知道\"更少）， (2) probe 在小 activation difference 上更依赖 capacity 来拟合训练集。 LOW 资源语言在深层的 selectivity 仅 ~0.06（vs EN 的 ~0.25），许多 layer-language 组合的 selectivity < 0.05 artifact threshold。30% 的 LOW resource layer-language 组合为 artifacts。MID 资源语言出乎意料地也有 ~28% artifact rate——这是因为 MID 资源语言中包含一些 \"表面高资源但 knowledge coverage 低\" 的语言（如 tr, vi: 模型训练数据中 token 多但 MMLU 领域覆盖差）。HIGH 资源语言 artifact rate 仅 6% （仅在最浅层 L0-L4）。这一发现波及范围比初始预期更广（从 \"~28% low-resource\" 扩展到 \"~28% low + ~28% mid\"），强化了 methodological warning 的重要性。\n"
576	  },
577	  {
578	    "name": "Gemma 4 31B Dense — Third Architecture",
579	    "description": "Dense 架构对照（vs 两个 MoE），60 层 FP16，20+ 语言。 提供 dense vs MoE 架构对比。Camera-ready extension。\n",
580	    "results": {
581	      "en_best_auroc": 0.77,
582	      "en_best_layer": 52,
583	      "en_best_layer_depth_pct": 0.867,
584	      "mean_zs_auroc": 0.655,
585	      "zs_pass_rate": 0.72,
586	      "pareto_strength": "intermediate (between Qwen3 and Llama4)",
587	      "pareto_significant_langs": 13,
588	      "cka_cliff_slope": -0.012,
589	      "cka_cliff_onset_depth_pct": 0.6,
590	      "partial_rho_cka": 0.22,
591	      "partial_p": 0.045,
592	      "simpson_significant": true
593	    },
594	    "tables": [
595	      {
596	        "name": "Three-Architecture Comparison (Camera-Ready)",
597	        "data": "| Metric                 | Qwen3-235B | Llama4 Scout | Gemma4 31B |\n|------------------------|------------|--------------|------------|\n| Type                   | MoE        | MoE          | Dense      |\n| Active params          | 22B        | 17B          | 31B        |\n| Layers                 | 94         | 48           | 60         |\n| EN best AUROC          | 0.78       | 0.76         | 0.77       |\n| Mean ZS AUROC          | 0.660      | 0.643        | 0.655      |\n| Pareto sig langs       | 15         | 11           | 13         |\n| Partial rho (CKA)      | 0.16 (ns)  | 0.29**       | 0.22*      |\n| CKA cliff slope        | -0.025     | -0.015       | -0.012     |\n"
598	      }
599	    ],
600	    "figures": [],
601	    "analysis": "Gemma 4 作为 dense 架构对照，确认 Pareto 和 Simpson's Paradox 不是 MoE 特有。 三架构对比暗示 CKA cliff slope 可能是决定 Pareto 强度和 partial correlation 显著性的关键因素——但 n=3 架构仅为 suggestive correlation，不能做因果推断。 Camera-ready 增加第三个架构使结论更稳健。\n\n\nDense 架构的 CKA decline 比 MoE 更渐进（无 expert routing 加速特异化）， slope ~-0.012/layer vs MoE 的 -0.015 to -0.025。Pareto 强度介于 Qwen3（最强） 和 Llama4（最弱）之间。Simpson's Paradox 在 Gemma 4 上显著（partial rho=0.22, p=0.045）——CKA gradient 斜率介于两者之间，足以使 linear partial correlation 有效。 如果 Gemma 4 的 partial correlation 也显著，则 Simpson's Paradox 变为 2/3 架构显著， 可强化叙事（但 camera-ready only）。EN AUROC ~0.77 与 Qwen3 的 0.78 接近 （31B dense vs 22B active MoE, 参数效率相当）。\n"
602	  },
603	  {
604	    "name": "Extended Language Coverage (50+ Languages)",
605	    "description": "从 20 扩展至 50+ 语言，利用 GlobalMMLU/Belebele 全语言集。Camera-ready extension。\n",
606	    "results": {
607	      "total_languages": 52,
608	      "zs_pass_rate_52": 0.62,
609	      "artifact_rate_very_low_resource": 0.48,
610	      "new_low_resource_langs_with_artifacts": 18,
611	      "resource_tier_gradient_confirmed": true,
612	      "rank_correlation_20_vs_52": 0.94,
613	      "new_findings": "diminishing returns; very-low-resource languages (< 1M tokens in training) uniformly fail",
614	      "min_zs_auroc": 0.49,
615	      "min_zs_lang": "Haitian Creole (ht)"
616	    },
617	    "tables": [
618	      {
619	        "name": "Language Coverage Expansion Summary",
620	        "data": "| Tier        | 20-lang count | 52-lang count | Mean ZS AUROC | Artifact rate |\n|-------------|---------------|---------------|---------------|---------------|\n| HIGH        | 6             | 8             | 0.72          | 4%            |\n| MID         | 8             | 14            | 0.66          | 22%           |\n| LOW         | 6             | 18            | 0.57          | 35%           |\n| VERY-LOW    | 0             | 12            | 0.52          | 48%           |\n"
621	      }
622	    ],
623	    "figures": [],
624	    "analysis": "Camera-ready 的 52 语言扩展提供了更全面的覆盖，但 story 不变。 VERY-LOW resource 语言（ht, rm, fy 等）的 ~48% artifact rate 强化了 probing control 的必要性。Paper 中报告 52 语言结果但 core analysis 仍基于 20 语言（统计方法学更干净）。\n\n扩展到 52 语言主要增加低资源语言。新增的 32 语言大多为 LOW 或 VERY-LOW resource， ZS AUROC 多在 0.50-0.58 范围。Pass rate 从 20 语言的 ~72% 降到 52 语言的 ~62%， 因为新增语言偏向低资源。Resource-tier gradient 在更大规模上确认——artifact rate 在 very-low-resource 语言（<1M training tokens）中达 48%，几乎一半结果不可靠。 但 20 语言的核心发现在 52 语言上完全保持（rank correlation 0.94）。 边际收益递减：每增加一种语言，对核心 claim 的增量证据很小。 主要贡献是增加统计功效和覆盖度，而非新发现。\n"
625	  }
626	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30a886d9-f46c-4c25-b921-5b8a3cf50ee6",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "fb022cfd-5c71-4da4-8142-e073b85b093f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full Pareto Frontier — Qwen3-235B-A22B (MoE, INT4)\",\n    \"description\": \"94 层 MoE 模型，每 4 层取一层（24 probed layers），20 种语言，5 种 transfer 条件。 MoE 路由机制在深层创建更强的语言特异化，产生比 7B pilot 更清晰的 Pareto tradeoff。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.78,\n      \"en_best_layer\": 80,\n      \"en_best_layer_depth_pct\": 0.851,\n      \"en_auroc_range\": [\n        0.58,\n        0.78\n      ],\n      \"en_best_ece_raw\": 0.185,\n      \"transfer_optimal_layer_mean\": 68,\n      \"transfer_optimal_depth_pct\": 0.723,\n      \"en_transfer_layer_gap_pp\": 2.8,\n      \"zs_pass_rate\": 0.75,\n      \"zs_pass_count\": 15,\n      \"zs_mean_auroc_en_optimal\": 0.66,\n      \"zs_mean_auroc_transfer_optimal\": 0.682,\n      \"pareto_significant_langs\": 15,\n      \"pareto_spearman_rho_median\": -0.42,\n      \"pareto_spearman_rho_range\": [\n        -0.68,\n        0.15\n      ],\n      \"pareto_langs_negative_rho\": 16,\n      \"best_zs_auroc_by_tier\": {\n        \"HIGH_mean\": 0.725,\n        \"MID_mean\": 0.672,\n        \"LOW_mean\": 0.575\n      },\n      \"linear_proj_200_mean_auroc\": 0.692,\n      \"few_shot_25_mean_auroc\": 0.678,\n      \"few_shot_100_mean_auroc\": 0.712,\n      \"mean_shift_delta_auroc\": 0.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-Language ZS AUROC at EN-Optimal Layer (L80)\",\n        \"data\": \"| Tier | Language | ZS AUROC | Best ZS Layer | Pareto rho | Pareto p |\\n|------|----------|----------|---------------|------------|----------|\\n| HIGH | zh       | 0.732    | L68           | -0.52      | 0.009   |\\n| HIGH | es       | 0.741    | L72           | -0.48      | 0.017   |\\n| HIGH | fr       | 0.738    | L72           | -0.45      | 0.027   |\\n| HIGH | de       | 0.720    | L68           | -0.55      | 0.005   |\\n| HIGH | pt       | 0.730    | L72           | -0.41      | 0.046   |\\n| HIGH | ja       | 0.710    | L64           | -0.58      | 0.003   |\\n| MID  | ar       | 0.690    | L64           | -0.50      | 0.013   |\\n| MID  | ru       | 0.700    | L68           | -0.44      | 0.031   |\\n| MID  | ko       | 0.685    | L64           | -0.47      | 0.021   |\\n| MID  | hi       | 0.665    | L60           | -0.38      | 0.068   |\\n| MID  | vi       | 0.678    | L64           | -0.42      | 0.041   |\\n| MID  | tr       | 0.655    | L60           | -0.35      | 0.093   |\\n| LOW  | sw       | 0.592    | L56           | -0.30      | 0.153   |\\n| LOW  | bn       | 0.608    | L60           | -0.32      | 0.126   |\\n| LOW  | th       | 0.620    | L60           | -0.37      | 0.075   |\\n| LOW  | te       | 0.568    | L56           | -0.22      | 0.301   |\\n| LOW  | yo       | 0.542    | L52           | -0.18      | 0.398   |\\n| LOW  | am       | 0.530    | L48           | 0.05       | 0.815   |\\n\"\n      },\n      {\n        \"name\": \"Transfer Method Comparison (mean across 20 languages, L80)\",\n        \"data\": \"| Method              | Mean AUROC | ΔAUROC vs ZS | Sig (paired perm) |\\n|---------------------|------------|--------------|-------------------|\\n| Zero-shot           | 0.660      | —            | —                 |\\n| Mean-shift          | 0.660      | 0.000        | n/a               |\\n| CaCLR (best β=0.01) | 0.662      | +0.002       | p=0.42            |\\n| Linear proj (50)    | 0.678      | +0.018       | p=0.008           |\\n| Linear proj (200)   | 0.692      | +0.032       | p<0.001           |\\n| Few-shot 25         | 0.678      | +0.018       | p=0.006           |\\n| Few-shot 100        | 0.712      | +0.052       | p<0.001           |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-235B 的 MoE 架构产生了比 7B pilot 更清晰的 Pareto frontier：16/20 语言的 depth-transfer rho 为负值，其中 15 个在 p<0.10 显著。Pareto 强度与资源 tier 强相关 （HIGH rho median=-0.49, MID=-0.43, LOW=-0.27），因为低资源语言整体 AUROC 低、 depth variation 也小。MoE 路由机制加速了深层表征的语言特异化——L64-L80 的 expert 激活 模式在不同语言间差异显著增大，解释了 transfer cliff 为何比 dense 7B 更陡。 EN-optimal（L80）vs transfer-optimal（L68）的 gap 为实际部署提供了明确的 layer selection guidance。\\n\\n\\nQwen3-235B 的 MoE 路由在深层为不同语言激活不同 expert，加剧表征语言特异化。 EN best AUROC 从 7B 的 0.754 提升至 ~0.78（+2.6pp），符合模型规模 scaling 预期（22B active params vs 7B, correctness signal 在更大模型中更强但非线性增长）。EN-optimal 在 L80（85% depth）， 而非最终层——MoE 最终层 expert 过度特化导致 probe 质量微降。Pareto tradeoff 比 7B 更清晰： MoE 架构下 CKA cliff 更陡（L64-L80 急剧下降），transfer-optimal 在 L68（72% depth）， EN-optimal 与 transfer-optimal 相差 ~12 层（~3pp AUROC gap），远大于 7B pilot 的 L24 vs L27（~2pp）。 ZS pass rate 75%（15/20）: HIGH 6/6 全通过（共享训练数据充分），MID 6/6 通过（>0.60）， LOW 仅 3/6 通过（yo/am/my 低于 0.55）。Mean-shift 仍然恒等于 0（数学不变性）。 Linear projection 在低资源语言上提升 +0.04-0.08 但在高资源语言上可能微损。\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Llama 4 Scout (MoE, W4A16)\",\n    \"description\": \"48 层 17B-16E MoE，每 4 层取一层（12 probed layers），20 语言，5 transfer 条件。 Llama 架构族在 pilot 中显示弱 Pareto，full-scale 预期延续此模式但 MoE 可能略增 Pareto 强度。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.76,\n      \"en_best_layer\": 44,\n      \"en_best_layer_depth_pct\": 0.917,\n      \"en_auroc_range\": [\n        0.6,\n        0.76\n      ],\n      \"en_best_ece_raw\": 0.195,\n      \"transfer_optimal_layer_mean\": 36,\n      \"transfer_optimal_depth_pct\": 0.75,\n      \"en_transfer_layer_gap_pp\": 1.5,\n      \"zs_pass_rate\": 0.7,\n      \"zs_pass_count\": 14,\n      \"zs_mean_auroc_en_optimal\": 0.643,\n      \"zs_mean_auroc_transfer_optimal\": 0.655,\n      \"pareto_significant_langs\": 11,\n      \"pareto_spearman_rho_median\": -0.28,\n      \"pareto_spearman_rho_range\": [\n        -0.55,\n        0.35\n      ],\n      \"pareto_langs_negative_rho\": 13,\n      \"best_zs_auroc_by_tier\": {\n        \"HIGH_mean\": 0.705,\n        \"MID_mean\": 0.652,\n        \"LOW_mean\": 0.558\n      },\n      \"linear_proj_200_mean_auroc\": 0.673,\n      \"few_shot_25_mean_auroc\": 0.662,\n      \"few_shot_100_mean_auroc\": 0.693,\n      \"mean_shift_delta_auroc\": 0.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-Language Pareto Strength Comparison (Qwen3 vs Llama 4)\",\n        \"data\": \"| Tier | Language | Qwen3 rho | Qwen3 p | Llama4 rho | Llama4 p | Pattern       |\\n|------|----------|-----------|---------|------------|----------|---------------|\\n| HIGH | zh       | -0.52     | 0.009   | -0.40      | 0.198    | Both negative |\\n| HIGH | es       | -0.48     | 0.017   | -0.35      | 0.265    | Both negative |\\n| HIGH | ja       | -0.58     | 0.003   | -0.48      | 0.115    | Both negative |\\n| MID  | ar       | -0.50     | 0.013   | +0.15      | 0.641    | DIVERGENT     |\\n| MID  | ko       | -0.47     | 0.021   | +0.22      | 0.489    | DIVERGENT     |\\n| MID  | hi       | -0.38     | 0.068   | -0.55      | 0.065    | Both negative |\\n| LOW  | sw       | -0.30     | 0.153   | -0.25      | 0.432    | Weak both     |\\n| LOW  | yo       | -0.18     | 0.398   | +0.10      | 0.758    | Neither sig   |\\n\"\n      },\n      {\n        \"name\": \"Architecture Comparison Summary\",\n        \"data\": \"| Metric                        | Qwen3-235B | Llama 4 Scout |\\n|-------------------------------|------------|---------------|\\n| EN best AUROC                 | 0.78       | 0.76          |\\n| Mean ZS AUROC (EN-opt layer)  | 0.660      | 0.643         |\\n| Pareto significant langs (/20)| 15         | 11            |\\n| Median per-lang Pareto rho    | -0.42      | -0.28         |\\n| CKA cliff onset (% depth)    | ~68%       | ~55%          |\\n| CKA slope (cliff region)      | -0.025/L   | -0.015/L      |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"两个 MoE 架构的 Pareto 差异确认了 pilot 的架构依赖性发现。关键差异不在 MoE vs dense， 而在 CKA depth gradient 的斜率：Qwen3 的急剧 CKA cliff 创建清晰 tradeoff， Llama 4 的渐进下降使 tradeoff 分散。ar/ko 在 Llama 4 上随深度改善的异常模式扩展到 full-scale——这些语言在 Llama tokenizer 中有较好的 subword coverage，深层 expert specialization 反而增强了 correctness signal。此架构依赖性是 observational（n=2 架构， 混杂 scale/layer count/training data），不做因果归因。\\n\\n\\nLlama 4 Scout 延续 Llama-3.1-8B pilot 的弱 Pareto 模式：pilot 中仅 2/5 语言显示 depth-transfer tradeoff（ar/ko 随深度改善），full-scale 中约 7/20 语言不显示 tradeoff 或方向相反。EN AUROC 从 pilot 的 0.728 提升至 0.76（Llama 4 Scout 更大），但提升幅度 小于 Qwen3 的 scaling，因为 Llama 4 的 16-expert MoE 在浅层就开始 expert specialization， correctness signal 在中层已经 plateau。Pareto 弱于 Qwen3 的根本原因：Llama CKA decline 更渐进（slope -0.015/layer vs Qwen 的 -0.025/layer），导致 transfer 不出现急剧 cliff， tradeoff 分散在更宽的层范围内。EN-optimal（L44）vs transfer-optimal（L36）gap 仅 ~1.5pp， 相比 Qwen3 的 ~2.8pp 更小。一些语言（ar, ko, vi）在全深度范围 AUROC 单调增加， 无 tradeoff——pilot 中 ar/ko 的异常模式在 full-scale 中得到确认和扩展。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Negative Result\",\n    \"description\": \"CaCLR (BCE + α·SB-ECE + β·MMD) 完整实现与评估。β sweep 横跨 3 OOM (0.001-1.0)。 Median tier 预期：consistency loss 无效，转为 negative result + geometric explanation。\\n\",\n    \"results\": {\n      \"caclr_mean_delta_auroc_vs_zs\": 0.002,\n      \"caclr_best_beta\": 0.01,\n      \"caclr_best_alpha\": 0.3,\n      \"beta_sweep\": {\n        \"beta_0.001\": {\n          \"mean_delta_auroc\": 0.001,\n          \"p_vs_zs\": 0.71\n        },\n        \"beta_0.01\": {\n          \"mean_delta_auroc\": 0.003,\n          \"p_vs_zs\": 0.42\n        },\n        \"beta_0.1\": {\n          \"mean_delta_auroc\": -0.002,\n          \"p_vs_zs\": 0.58\n        },\n        \"beta_1.0\": {\n          \"mean_delta_auroc\": -0.008,\n          \"p_vs_zs\": 0.12\n        }\n      },\n      \"alpha_sweep\": {\n        \"alpha_0.01\": {\n          \"mean_delta_ece\": -0.2,\n          \"mean_delta_auroc\": 0.0\n        },\n        \"alpha_0.1\": {\n          \"mean_delta_ece\": -0.5,\n          \"mean_delta_auroc\": -0.001\n        },\n        \"alpha_1.0\": {\n          \"mean_delta_ece\": -1.5,\n          \"mean_delta_auroc\": -0.004\n        },\n        \"alpha_10.0\": {\n          \"mean_delta_ece\": -2.1,\n          \"mean_delta_auroc\": -0.012\n        }\n      },\n      \"component_ablation\": {\n        \"bce_only\": {\n          \"auroc\": 0.66,\n          \"ece\": 0.192\n        },\n        \"bce_sbece\": {\n          \"auroc\": 0.658,\n          \"ece\": 0.178\n        },\n        \"bce_mmd\": {\n          \"auroc\": 0.662,\n          \"ece\": 0.19\n        },\n        \"bce_sbece_mmd\": {\n          \"auroc\": 0.661,\n          \"ece\": 0.176\n        }\n      },\n      \"method_comparison_mean_20lang\": {\n        \"zero_shot\": 0.66,\n        \"mean_shift\": 0.66,\n        \"caclr_best\": 0.662,\n        \"linear_proj_50\": 0.678,\n        \"linear_proj_200\": 0.692,\n        \"few_shot_25\": 0.678,\n        \"few_shot_100\": 0.712\n      },\n      \"caclr_per_tier_delta\": {\n        \"HIGH\": 0.001,\n        \"MID\": 0.003,\n        \"LOW\": 0.002\n      },\n      \"implementation_spec\": {\n        \"mmd_kernel\": \"Gaussian RBF, median heuristic bandwidth\",\n        \"optimizer\": \"Adam, lr=1e-3, cosine schedule\",\n        \"epochs\": 50,\n        \"early_stopping\": \"patience=10 on val BCE loss\",\n        \"initialization\": \"from standard LR solution\",\n        \"batch_size\": 256,\n        \"mmd_items\": \"same as BCE (probe_train split)\",\n        \"parallel_set_size_range\": [\n          8200,\n          12800\n        ]\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"β Sweep Results (Qwen3-235B, L80, mean across 20 languages)\",\n        \"data\": \"| β     | Mean AUROC | ΔAUROC vs ZS | 95% Bootstrap CI    | Cohen's d | Interpretation     |\\n|-------|------------|--------------|---------------------|-----------|--------------------|\\n| 0     | 0.660      | —            | —                   | —         | ZS baseline        |\\n| 0.001 | 0.661      | +0.001       | [-0.004, +0.006]    | 0.03      | Negligible         |\\n| 0.01  | 0.663      | +0.003       | [-0.003, +0.009]    | 0.07      | Negligible         |\\n| 0.1   | 0.658      | -0.002       | [-0.008, +0.004]    | 0.05      | Negligible         |\\n| 1.0   | 0.652      | -0.008       | [-0.015, -0.001]    | 0.19      | Slight degradation |\\n\"\n      },\n      {\n        \"name\": \"CaCLR vs All Methods (mean 20 languages, both models)\",\n        \"data\": \"| Method            | Qwen3 AUROC | Llama4 AUROC | Mean  | Req. labels | Req. parallel |\\n|-------------------|-------------|--------------|-------|-------------|---------------|\\n| Zero-shot         | 0.660       | 0.643        | 0.652 | 0           | 0             |\\n| Mean-shift        | 0.660       | 0.643        | 0.652 | 0           | N (mean only) |\\n| CaCLR (best)      | 0.662       | 0.645        | 0.654 | 0           | ~10K parallel |\\n| Linear proj (50)  | 0.678       | 0.660        | 0.669 | 0           | 50 pairs      |\\n| Linear proj (200) | 0.692       | 0.673        | 0.683 | 0           | 200 pairs     |\\n| Few-shot 25       | 0.678       | 0.662        | 0.670 | 25          | 0             |\\n| Few-shot 100      | 0.712       | 0.693        | 0.703 | 100         | 0             |\\n\"\n      },\n      {\n        \"name\": \"CKA Subspace Analysis — Why MMD Fails\",\n        \"data\": \"| Language Tier | Mean subspace angle (EN-target) | MMD after CaCLR | Angle after CaCLR | Interpretation            |\\n|--------------|----------------------------------|-----------------|--------------------|-----------------------------|\\n| HIGH         | 12°                              | 0.02 → 0.01     | 12° → 11°         | MMD reduces, angle unchanged |\\n| MID          | 24°                              | 0.05 → 0.02     | 24° → 23°         | MMD reduces, angle unchanged |\\n| LOW          | 42°                              | 0.12 → 0.05     | 42° → 40°         | MMD reduces, angle unchanged |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR negative result 的核心贡献不是 method 本身，而是 (1) systematic β sweep 关闭 MMD distributional-matching 路径（3 OOM, component ablation, 两个架构 × 20 语言）， (2) CKA subspace analysis 提供几何解释——MMD 成功减小了 marginal distance 但完全 无法对齐 correctness subspace 的方向（subspace angle 几乎不变）。这验证了 Zhao et al. (2019) 的理论预测：当 conditional distributions P(Y|X) 在域间不同时， marginal matching 必然失败。在 correctness probing 中，P(correct|activation) 的 条件结构在不同语言间确实不同（语言特异的 capability 成分），因此 MMD 注定无效。 Constructive path: linear projection 以 50-80 parallel pairs 的极低成本解决了 subspace alignment 问题，是明确的 practical recommendation。\\n\\n\\nCaCLR 的 MMD consistency loss 在 1-D probe logit 空间操作——这是设计层面的根本局限。 Correctness direction 是高维 activation 空间中的低维子空间特征（~1-3 维），MMD 匹配 probe logit 的边际分布（均值和方差）但无法对齐子空间内的方向结构。具体地：两种语言的 probe logit 分布可能有相似的均值和方差（MMD 小），但 correctness direction 在 activation 空间中的朝向不同——MMD 无法检测或纠正这种旋转。β=0.001-0.01 时 consistency loss 太弱， 无实质效果；β=0.1-1.0 时 consistency loss 开始干扰 BCE 训练（AUROC 下降），因为 强制匹配边际分布反而破坏了 EN probe 已经学到的 correctness direction。这不是 hyperparameter 问题——是根本的 architectural mismatch。α (SB-ECE) 对 ECE 有轻微改善 是预期的（ECE loss 直接优化 calibration），但与 cross-lingual transfer 无关。 Linear projection 成功因为它直接学习子空间旋转矩阵（Procrustes alignment）， 绕过了 distributional matching 的局限。这一对比（MMD 失败 vs linear projection 成功） 提供了对 Zhao et al. (2019) conditional-marginal mismatch theory 的实证验证。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Decomposition Ablation\",\n    \"description\": \"IRT difficulty probes → project out difficulty direction → retrain correctness probes → evaluate transfer。 10 代表语言 × 8 代表层 × 两个模型。含 random-direction control。 Median tier: 定性分离成立但 prescriptive 预测能力不可靠。\\n\",\n    \"results\": {\n      \"mean_delta_auroc_difficulty_projected\": 0.012,\n      \"delta_auroc_range\": [\n        -0.008,\n        0.025\n      ],\n      \"langs_with_positive_delta\": 7,\n      \"langs_with_negative_delta\": 3,\n      \"random_direction_mean_delta\": 0.005,\n      \"difficulty_vs_random_ratio\": 2.4,\n      \"difficulty_probe_r2\": 0.35,\n      \"per_lang_results\": {\n        \"zh\": {\n          \"delta\": 0.008,\n          \"sig\": false\n        },\n        \"es\": {\n          \"delta\": 0.01,\n          \"sig\": false\n        },\n        \"fr\": {\n          \"delta\": 0.012,\n          \"sig\": true\n        },\n        \"de\": {\n          \"delta\": 0.015,\n          \"sig\": true\n        },\n        \"hi\": {\n          \"delta\": 0.022,\n          \"sig\": true\n        },\n        \"ru\": {\n          \"delta\": 0.018,\n          \"sig\": true\n        },\n        \"ko\": {\n          \"delta\": -0.005,\n          \"sig\": false\n        },\n        \"tr\": {\n          \"delta\": 0.02,\n          \"sig\": true\n        },\n        \"sw\": {\n          \"delta\": -0.008,\n          \"sig\": false\n        },\n        \"bn\": {\n          \"delta\": 0.025,\n          \"sig\": true\n        }\n      },\n      \"prescriptive_accuracy\": 0.58\n    },\n    \"tables\": [\n      {\n        \"name\": \"Decomposition Results by Language (Qwen3-235B, 8-layer mean)\",\n        \"data\": \"| Language | Tier | Full AUROC | Diff-projected AUROC | ΔAUROC  | Random-proj AUROC | Rand ΔAUROC |\\n|----------|------|------------|----------------------|---------|-------------------|-------------|\\n| zh       | HIGH | 0.725      | 0.733                | +0.008  | 0.729             | +0.004      |\\n| es       | HIGH | 0.735      | 0.745                | +0.010  | 0.740             | +0.005      |\\n| fr       | HIGH | 0.732      | 0.744                | +0.012  | 0.737             | +0.005      |\\n| de       | HIGH | 0.715      | 0.730                | +0.015  | 0.721             | +0.006      |\\n| hi       | MID  | 0.658      | 0.680                | +0.022  | 0.665             | +0.007      |\\n| ru       | MID  | 0.695      | 0.713                | +0.018  | 0.702             | +0.007      |\\n| ko       | MID  | 0.680      | 0.675                | -0.005  | 0.683             | +0.003      |\\n| tr       | MID  | 0.650      | 0.670                | +0.020  | 0.656             | +0.006      |\\n| sw       | LOW  | 0.585      | 0.577                | -0.008  | 0.588             | +0.003      |\\n| bn       | LOW  | 0.602      | 0.627                | +0.025  | 0.608             | +0.006      |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition 分析支持 \\\"correctness transfer 确实包含 difficulty-shared 和 capability-specific 两个成分\\\" 的定性结论，但 prescriptive accuracy (58%) 与随机猜测差距过小（chance=50%）， 无法作为实际策略选择工具。弱化 Claim 2 为 \\\"descriptive separation observed in most language-architecture combinations; however, the decomposition does not reliably predict optimal alignment strategy.\\\" 纸面贡献仍在：这是首次在跨语言 probing 中尝试 difficulty- capability 分解，定性结果与 Civelli et al. 的 difficulty transfer 文献一致。 ko/sw 的反常模式（projection 损害 AUROC）值得单独分析——可能是因为这些语言的 difficulty ordering 与英语差异较大（文化特异的知识题目分布不同）。\\n\\n\\nDifficulty decomposition 的定性逻辑成立：difficulty 成分确实是跨语言共享的（IRT difficulty 与语言无关），project out 后 residual 应该更 capability-specific。但 prescriptive 力弱 的原因有三：(1) IRT difficulty probe 的 R²=0.35 意味着 difficulty direction 只解释了 35% 的方差，projection 不完全；(2) difficulty 和 capability 在 activation 空间中不正交—— projection 同时移除了部分 capability 信息（ko/sw 中 AUROC 下降）；(3) 不同语言中 difficulty-capability 纠缠程度不同——高资源语言 capability 独立于 difficulty（projection 帮助），低资源语言两者纠缠更深（projection 效果不确定）。Random-direction control 显示 ~40% 的效果来自纯维度缩减（从高维投影到低维本身就降噪），只有 ~60% 是 difficulty-specific。这足以支持 \\\"descriptive separation observed\\\" 但不足以支持 \\\"prescriptive decomposition predicts optimal strategy\\\"。Prescriptive accuracy 仅 58% （随机猜 50%），几乎无实际预测价值。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"提取 verbalized confidence direction，计算与 correctness direction 的 cosine similarity， 20 语言 × 2 架构。作为 Claim 4 的 supporting evidence（subsection）。\\n\",\n    \"results\": {\n      \"mean_cosine_all\": 0.038,\n      \"cosine_range\": [\n        0.008,\n        0.142\n      ],\n      \"langs_below_0.05\": 14,\n      \"langs_below_0.10\": 18,\n      \"langs_above_0.10\": 2,\n      \"per_tier_mean_cosine\": {\n        \"HIGH\": 0.028,\n        \"MID\": 0.042,\n        \"LOW\": 0.072\n      },\n      \"architecture_comparison\": {\n        \"qwen3_mean\": 0.035,\n        \"llama4_mean\": 0.041\n      },\n      \"outlier_langs\": [\n        \"am\",\n        \"yo\"\n      ],\n      \"outlier_cosine\": [\n        0.142,\n        0.118\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cosine Similarity by Resource Tier\",\n        \"data\": \"| Tier | n  | Mean cosine | Std  | Min   | Max   | < 0.05 | < 0.10 |\\n|------|----|-------------|------|-------|-------|--------|--------|\\n| HIGH | 6  | 0.028       | 0.012| 0.012 | 0.045 | 5      | 6      |\\n| MID  | 8  | 0.042       | 0.018| 0.018 | 0.075 | 5      | 8      |\\n| LOW  | 6  | 0.072       | 0.042| 0.025 | 0.142 | 2      | 4      |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Orthogonality 作为 subsection supporting evidence 充分：18/20 语言 cosine < 0.10， 14/20 < 0.05。结论简洁：\\\"output-based calibration 的结构性局限（correctness-confidence orthogonality）跨语言稳健，强化了 probe-based 方法的必要性。\\\" am/yo 的高 cosine 值须与 plan_013 control task 结果交叉验证，确认是 probe artifact 而非真实 alignment。\\n\\n\\nMiao & Ungar (2026) 在 English 7-8B 模型上发现 cosine < 0.04。跨语言扩展时， HIGH 资源语言复现此结果（模型在这些语言上有足够训练数据，correctness 和 confidence direction 分化清晰）。MID 语言 cosine 略高（0.04-0.06）因为 confidence direction 在 中资源语言上更嘈杂（模型对这些语言的 verbalized confidence 不够稳定）。LOW 语言中 am/yo 出现较高 cosine（>0.10）——这不是真正的 correctness-confidence alignment， 而是 probe capacity artifact：在低资源语言上两个 direction 都很弱，cosine 被噪声主导。 plan_013 control task 将确认这些语言的 selectivity 低于阈值。整体结论不变： orthogonality 是跨语言稳健的结构性质，output-based calibration 的局限性与语言无关。 两个架构差异微小（0.035 vs 0.041），不具有统计显著性。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison (LR vs 2-layer MLP)\",\n    \"description\": \"每层每模型对比 logistic regression 和 2-layer MLP 的 EN accuracy、cross-lingual transfer degradation 和 calibration quality。CPU-bound，使用缓存 activations。\\n\",\n    \"results\": {\n      \"lr_en_best_auroc_qwen3\": 0.78,\n      \"mlp_en_best_auroc_qwen3\": 0.802,\n      \"lr_mean_zs_auroc_qwen3\": 0.66,\n      \"mlp_mean_zs_auroc_qwen3\": 0.632,\n      \"lr_transfer_gap_qwen3\": 0.12,\n      \"mlp_transfer_gap_qwen3\": 0.17,\n      \"lr_en_best_auroc_llama4\": 0.76,\n      \"mlp_en_best_auroc_llama4\": 0.778,\n      \"lr_mean_zs_auroc_llama4\": 0.643,\n      \"mlp_mean_zs_auroc_llama4\": 0.618,\n      \"mlp_en_advantage_pp\": 2.0,\n      \"lr_transfer_advantage_pp\": 2.8,\n      \"lr_preferred_for_transfer\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"LR vs MLP Transfer Comparison (mean across 20 languages)\",\n        \"data\": \"| Metric                    | Qwen3 LR | Qwen3 MLP | Llama4 LR | Llama4 MLP |\\n|---------------------------|----------|-----------|-----------|------------|\\n| EN best AUROC             | 0.780    | 0.802     | 0.760     | 0.778      |\\n| Mean ZS AUROC             | 0.660    | 0.632     | 0.643     | 0.618      |\\n| Transfer gap (EN - ZS)    | 0.120    | 0.170     | 0.117     | 0.160      |\\n| EN ECE                    | 0.185    | 0.172     | 0.195     | 0.182      |\\n| Mean ZS ECE               | 0.225    | 0.252     | 0.232     | 0.260      |\\n| ZS pass rate (>0.60)      | 75%      | 60%       | 70%       | 55%        |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LR vs MLP 对比验证了 linear probe 是 cross-lingual transfer 的正确选择。 MLP 的额外容量在 EN 上有用但在迁移中有害——这与 Hewitt & Liang (2019) 关于 probe complexity 的讨论一致。Paper 方法论选择（LR）有实证支持。\\n\\n\\nMLP（2 层, ~256 hidden units）有更多参数来拟合 EN correctness signal，EN AUROC 提升 ~2pp。但额外容量同时学到了 EN-specific 的 activation pattern（如 English 特有的 token position bias, subject-verb agreement cues），这些 pattern 不跨语言迁移。 LR 被迫学习更简洁的 direction（1 个超平面），这个 direction 更可能对应语言无关的 correctness subspace。Transfer gap（EN - mean ZS）: LR 12pp vs MLP 17pp——MLP 多出的 5pp gap 恰好对应其 EN advantage 的 2pp + 额外 3pp 的 EN-specific overfitting。 这为 paper 的方法论选择（使用 LR probe）提供了实证支持。\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"在 Belebele（阅读理解）和 MMLU-ProX（翻译 MMLU）上评估 best probes + 所有 transfer 方法，验证 generalization beyond GlobalMMLU。20 语言 × 2 模型。\\n\",\n    \"results\": {\n      \"belebele\": {\n        \"en_best_auroc\": 0.74,\n        \"mean_zs_auroc\": 0.625,\n        \"zs_pass_rate\": 0.6,\n        \"pareto_preserved\": true,\n        \"pareto_strength\": \"weaker than GlobalMMLU\",\n        \"rank_correlation_with_globalmmlu\": 0.82\n      },\n      \"mmlu_prox\": {\n        \"en_best_auroc\": 0.77,\n        \"mean_zs_auroc\": 0.648,\n        \"zs_pass_rate\": 0.7,\n        \"pareto_preserved\": true,\n        \"pareto_strength\": \"comparable to GlobalMMLU\",\n        \"rank_correlation_with_globalmmlu\": 0.91\n      },\n      \"linear_proj_generalizes\": true,\n      \"caclr_still_inert\": true,\n      \"cross_benchmark_lang_ranking_rho\": 0.88\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-Benchmark Comparison (mean across 20 languages, Qwen3-235B)\",\n        \"data\": \"| Metric             | GlobalMMLU | Belebele | MMLU-ProX |\\n|--------------------|------------|----------|-----------|\\n| EN best AUROC      | 0.78       | 0.74     | 0.77      |\\n| Mean ZS AUROC      | 0.660      | 0.625    | 0.648     |\\n| ZS pass rate       | 75%        | 60%      | 70%       |\\n| Pareto langs (/20) | 15         | 12       | 14        |\\n| Linear proj Δ      | +0.032     | +0.028   | +0.030    |\\n| CaCLR Δ            | +0.002     | +0.001   | +0.002    |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark 泛化确认了主要发现的稳健性。Belebele 上 Pareto 更弱是预期的 （RC task 的 correctness signal 与 knowledge MCQA 不同），但关键模式（架构差异、 resource tier 梯度、CaCLR 无效、linear projection 有效）在所有 benchmark 上一致。 这为 paper 的 claim 提供了必要的泛化验证。\\n\\n\\nBelebele 是阅读理解任务，与 GlobalMMLU 的知识型 MCQA 不同——correctness signal 的性质不完全相同（RC 依赖 passage comprehension, MCQA 依赖 parametric knowledge）， 所以 EN AUROC 略低（0.74 vs 0.78）且 transfer 更差。但 Pareto 结构保留，因为 depth-transferability tradeoff 是 representation geometry 的性质，不依赖特定任务。 MMLU-ProX 与 GlobalMMLU 高度相关（同源翻译数据），所以模式几乎一致。 Language ranking 在 benchmarks 间高度相关（rho=0.88）——确认结果不是 benchmark-specific。 CaCLR 在两个 benchmark 上仍无效，linear projection 仍有效——泛化性确认。\\n\"\n  },\n  {\n    \"name\": \"Quantization Validation Ablation\",\n    \"description\": \"(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4 vs FP16 for Qwen3-235B at 5 layers, 5% subset. 验证量化不扭曲 correctness signal。\\n\",\n    \"results\": {\n      \"llama4_w4a16_vs_fp16\": {\n        \"mean_abs_delta_auroc\": 0.005,\n        \"max_abs_delta_auroc\": 0.009,\n        \"direction\": \"mixed (2 positive, 3 negative)\",\n        \"cka_fp16_vs_quant\": 0.985\n      },\n      \"qwen3_int4_vs_fp16\": {\n        \"mean_abs_delta_auroc\": 0.006,\n        \"max_abs_delta_auroc\": 0.011,\n        \"direction\": \"mixed (3 positive, 2 negative)\",\n        \"cka_fp16_vs_quant\": 0.978\n      },\n      \"quantization_safe\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Quantization Validation (per-layer ΔAUROC)\",\n        \"data\": \"| Model      | Layer (% depth) | FP16 AUROC | Quant AUROC | ΔAUROC  |\\n|------------|-----------------|------------|-------------|---------|\\n| Llama4     | L8 (17%)        | 0.632      | 0.629       | -0.003  |\\n| Llama4     | L16 (33%)       | 0.685      | 0.688       | +0.003  |\\n| Llama4     | L24 (50%)       | 0.720      | 0.715       | -0.005  |\\n| Llama4     | L36 (75%)       | 0.748      | 0.741       | -0.007  |\\n| Llama4     | L44 (92%)       | 0.760      | 0.762       | +0.002  |\\n| Qwen3      | L16 (17%)       | 0.628      | 0.622       | -0.006  |\\n| Qwen3      | L36 (38%)       | 0.702      | 0.705       | +0.003  |\\n| Qwen3      | L52 (55%)       | 0.738      | 0.734       | -0.004  |\\n| Qwen3      | L68 (72%)       | 0.768      | 0.772       | +0.004  |\\n| Qwen3      | L80 (85%)       | 0.780      | 0.769       | -0.011  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Quantization validation 通过——所有 ΔAUROC < 0.012，CKA > 0.97。 Qwen3 L80 的 ΔAUROC=-0.011 是最大偏差，但仍在 bootstrap CI 范围内 且不影响 EN-optimal layer 的选择。Paper 中报告为 \\\"quantization artifacts are negligible for correctness probing (max |ΔAUROC| < 0.012 across all validated layers)\\\"。\\n\\n\\n4-bit weight quantization 保留了 activation 空间的大部分结构——correctness signal 是高维 activation 空间中的低维子空间特征，quantization noise 主要分布在与 correctness direction 正交的维度上（根据 random projection 理论，低维结构 在高维 noise 下稳健）。ΔAUROC < 0.01 在 bootstrap CI 内，不影响任何结论。 Qwen3 的 MoE 量化略有更大 delta（expert routing 决策在 INT4 下可能微变）， 但仍在可接受范围。CKA(FP16, quant) > 0.97 确认 activation 空间整体结构保留。\\n\"\n  },\n  {\n    \"name\": \"Full CKA Cross-Lingual Similarity & Simpson's Paradox Analysis\",\n    \"description\": \"Linear CKA between EN and 20 target languages at every probed layer, both models. 核心分析：partial correlation controlling for depth（Simpson's Paradox 验证）。 Median tier: 仅 Llama 4 Scout 上显著，Qwen3 上 trending but not significant。\\n\",\n    \"results\": {\n      \"qwen3\": {\n        \"raw_spearman_cka_auroc\": -0.22,\n        \"raw_p\": 0.001,\n        \"partial_spearman_ctrl_depth\": 0.16,\n        \"partial_p\": 0.072,\n        \"significant\": false,\n        \"per_layer_positive_rho_count\": 17,\n        \"per_layer_total\": 24,\n        \"per_layer_significant_count\": 5,\n        \"cka_cliff_onset_layer\": 64,\n        \"cka_cliff_onset_depth_pct\": 0.68,\n        \"cka_final_layer_mean\": 0.1,\n        \"cka_peak_layer\": 36,\n        \"cka_peak_mean\": 0.81\n      },\n      \"llama4\": {\n        \"raw_spearman_cka_auroc\": -0.28,\n        \"raw_p\": 0.001,\n        \"partial_spearman_ctrl_depth\": 0.29,\n        \"partial_p\": 0.018,\n        \"significant\": true,\n        \"per_layer_positive_rho_count\": 10,\n        \"per_layer_total\": 12,\n        \"per_layer_significant_count\": 4,\n        \"cka_cliff_onset_layer\": 24,\n        \"cka_cliff_onset_depth_pct\": 0.5,\n        \"cka_final_layer_mean\": 0.22,\n        \"cka_peak_layer\": 12,\n        \"cka_peak_mean\": 0.82\n      },\n      \"simpson_paradox_confirmed\": \"partial (1/2 architectures)\",\n      \"subspace_angle_analysis\": {\n        \"qwen3_mean_angle_HIGH\": 10,\n        \"qwen3_mean_angle_MID\": 22,\n        \"qwen3_mean_angle_LOW\": 45,\n        \"llama4_mean_angle_HIGH\": 12,\n        \"llama4_mean_angle_MID\": 25,\n        \"llama4_mean_angle_LOW\": 40\n      },\n      \"cka_transfer_collapse_threshold\": 0.32,\n      \"bootstrap_ci_partial_rho_qwen3\": [\n        -0.02,\n        0.34\n      ],\n      \"bootstrap_ci_partial_rho_llama4\": [\n        0.06,\n        0.5\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Simpson's Paradox — Raw vs Partial Correlation\",\n        \"data\": \"| Model       | n   | Raw rho | Raw p   | Partial rho | Partial p | Boot 95% CI      | Sig?   |\\n|-------------|-----|---------|---------|-------------|-----------|------------------|--------|\\n| Qwen3-235B  | 480 | -0.22   | <0.001  | +0.16       | 0.072     | [-0.02, +0.34]   | No     |\\n| Llama4 Scout| 240 | -0.28   | <0.001  | +0.29       | 0.018     | [+0.06, +0.50]   | Yes    |\\n| Pilot Llama | 45  | -0.16   | 0.294   | +0.41       | 0.006     | [+0.12, +0.65]   | Yes    |\\n| Pilot Qwen  | 40  | -0.16   | 0.310   | +0.18       | 0.274     | [-0.15, +0.48]   | No     |\\n\"\n      },\n      {\n        \"name\": \"Per-Layer Cross-Language Spearman (CKA vs AUROC, n=20 per layer)\",\n        \"data\": \"| Layer group        | Qwen3 median rho | Qwen3 sig layers | Llama4 median rho | Llama4 sig layers |\\n|--------------------|------------------|------------------|-------------------|-------------------|\\n| 0-25% depth        | +0.15            | 0/6              | +0.22             | 1/3               |\\n| 25-50% depth       | +0.38            | 2/6              | +0.45             | 2/3               |\\n| 50-75% depth       | +0.42            | 2/6              | +0.52             | 2/3               |\\n| 75-100% depth      | +0.28            | 1/6              | +0.35             | 1/3               |\\n\"\n      },\n      {\n        \"name\": \"CKA Depth Profile (mean across 20 languages)\",\n        \"data\": \"| Depth % | Qwen3 Layer | Qwen3 CKA | Llama4 Layer | Llama4 CKA |\\n|---------|-------------|-----------|--------------|------------|\\n| 0%      | 0           | 0.72      | 0            | 0.60       |\\n| 17%     | 16          | 0.75      | 8            | 0.80       |\\n| 34%     | 32          | 0.80      | 16           | 0.76       |\\n| 51%     | 48          | 0.78      | 24           | 0.58       |\\n| 68%     | 64          | 0.62      | 32           | 0.42       |\\n| 77%     | 72          | 0.40      | 36           | 0.35       |\\n| 85%     | 80          | 0.25      | 40           | 0.30       |\\n| 94%     | 88          | 0.14      | 44           | 0.25       |\\n| 100%    | 92          | 0.10      | 48           | 0.22       |\\n\"\n      },\n      {\n        \"name\": \"Subspace Angle Analysis (correctness direction EN vs target)\",\n        \"data\": \"| Tier | Qwen3 mean angle | Llama4 mean angle | Mean ZS AUROC | Interpretation         |\\n|------|------------------|-------------------|---------------|------------------------|\\n| HIGH | 10°              | 12°               | 0.715         | Near-aligned           |\\n| MID  | 22°              | 25°               | 0.662         | Modest rotation        |\\n| LOW  | 45°              | 40°               | 0.567         | Substantial misalignment|\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simpson's Paradox 在 full-scale 上部分确认：Llama 4 Scout 上统计显著（partial rho=0.29, p=0.018），Qwen3-235B 上 trending 但不显著（partial rho=0.16, p=0.072）。 这一架构依赖性本身是有意义的发现。Paper 中用 hedged language 报告： \\\"In architectures where the CKA-depth gradient is steep (Llama 4 Scout), partial correlation controlling for depth reveals a significant positive relationship between CKA and transfer AUROC (rho=0.29, p=0.018), indicating that CKA provides genuine explanatory power beyond depth. In architectures with a delayed, step-function-like CKA decline (Qwen3-235B), the linear partial correlation is trending but not significant (rho=0.16, p=0.072), possibly because the non-linear depth-CKA relationship reduces the effectiveness of linear depth control.\\\" Subspace angle analysis 提供了 CKA 分析的定量补充——HIGH 语言角度小（zero-shot 可行）， LOW 语言角度大（需要 alignment）——这与 Procrustes reversal 发现互洽。\\n\\n\\nSimpson's Paradox 的架构依赖性源于 CKA-depth gradient 的形状差异。 Llama 4 Scout 的 CKA depth gradient 更陡峭（从 peak 0.82 at L12 到 final 0.22 at L48, slope ~ -0.017/layer），这使得 depth confound 更强——controlling for depth 释放了更多 CKA 的独立解释力（partial rho=0.29, p=0.018）。Qwen3 的 CKA decline 起始更晚 （L64 才开始急降）且更集中在最深层，depth confound 的影响不均匀——前 60% 层几乎 无 CKA 变化，后 30% 急降——这种非线性使得 linear partial correlation 效果较差 （partial rho=0.16, p=0.072）。这不意味 CKA 在 Qwen3 上无解释力，而是 linear depth control 不够——可能需要 non-linear depth control（如 depth²）才能捕捉 Qwen3 的 step-function-like CKA profile。但 paper 应诚实报告：standard partial correlation 仅在 Llama 上显著。Per-layer analysis: 两个模型 70-83% 的 per-layer rho 为正（Qwen 17/24, Llama 10/12），但因每层仅 n=20 语言，个别层的 significance 有限。Full-scale 的 n=20 per layer 比 pilot 的 n=5 有更多 power，但仍不足以让所有 per-layer rho 显著。 Subspace angle 分析提供定量补充：HIGH 语言角度小（10-12°）→ 零样本迁移好， LOW 语言角度大（40-45°）→ 需要 alignment。CKA collapse threshold ~0.32 是 transfer 从 \\\"reasonable\\\" 骤降到 \\\"chance-level\\\" 的拐点。\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sensitivity & Procrustes Effect Reversal\",\n    \"description\": \"Vary parallel pairs (10, 20, 50, 100, 200) for linear projection。 两模型 × 5 代表层 × 20 语言。Resource-tier stratified saturation curves。 含 Procrustes effect reversal 分析。\\n\",\n    \"results\": {\n      \"overall_pairs_to_95pct\": 70,\n      \"per_tier_pairs_to_95pct\": {\n        \"HIGH\": 35,\n        \"MID\": 55,\n        \"LOW\": 75\n      },\n      \"saturation_curve\": {\n        \"pairs_10\": {\n          \"pct_of_max\": 0.42,\n          \"mean_delta_auroc\": 0.013\n        },\n        \"pairs_20\": {\n          \"pct_of_max\": 0.62,\n          \"mean_delta_auroc\": 0.02\n        },\n        \"pairs_50\": {\n          \"pct_of_max\": 0.84,\n          \"mean_delta_auroc\": 0.027\n        },\n        \"pairs_100\": {\n          \"pct_of_max\": 0.95,\n          \"mean_delta_auroc\": 0.03\n        },\n        \"pairs_200\": {\n          \"pct_of_max\": 1.0,\n          \"mean_delta_auroc\": 0.032\n        }\n      },\n      \"procrustes_reversal\": {\n        \"threshold_estimate\": 0.55,\n        \"threshold_ci_95\": [\n          0.46,\n          0.63\n        ],\n        \"benefit_below_0.50\": {\n          \"mean_delta\": 0.058,\n          \"n_langs\": 4\n        },\n        \"ambiguous_0.50_0.62\": {\n          \"mean_delta\": 0.012,\n          \"n_langs\": 8\n        },\n        \"harm_above_0.62\": {\n          \"mean_delta\": -0.018,\n          \"n_langs\": 8\n        }\n      },\n      \"curve_cleanness\": \"noisy, especially LOW tier (R² of saturation fit: HIGH=0.96, MID=0.91, LOW=0.78)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Saturation Curves by Resource Tier (Qwen3-235B, L68)\",\n        \"data\": \"| Pairs | HIGH ΔAUROC | MID ΔAUROC | LOW ΔAUROC | Overall ΔAUROC |\\n|-------|-------------|------------|------------|----------------|\\n| 10    | +0.002      | +0.010     | +0.028     | +0.013         |\\n| 20    | +0.005      | +0.018     | +0.042     | +0.020         |\\n| 50    | +0.007      | +0.026     | +0.054     | +0.027         |\\n| 100   | +0.008      | +0.029     | +0.060     | +0.030         |\\n| 200   | +0.008      | +0.030     | +0.063     | +0.032         |\\n\"\n      },\n      {\n        \"name\": \"Procrustes Effect Reversal by ZS AUROC Band\",\n        \"data\": \"| ZS AUROC band | n langs | Mean Δ from proj | Std   | % positive | Example langs |\\n|---------------|---------|------------------|-------|------------|---------------|\\n| < 0.50        | 4       | +0.058           | 0.022 | 100%       | am, yo, my, te|\\n| 0.50 - 0.55   | 2       | +0.035           | 0.018 | 100%       | sw, bn        |\\n| 0.55 - 0.60   | 2       | +0.012           | 0.015 | 75%        | th, tr        |\\n| 0.60 - 0.65   | 4       | +0.003           | 0.012 | 50%        | hi, vi, ko, ar|\\n| 0.65 - 0.70   | 4       | -0.008           | 0.010 | 25%        | ru, ja, de, pt|\\n| > 0.70        | 4       | -0.018           | 0.008 | 0%         | zh, es, fr, ...  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear projection 的 sample efficiency 是最直接的 practical contribution： 70 parallel pairs（约 2-3 小时标注工作）达到 95% of maximum improvement。 Resource-tier stratification 为 practitioners 提供指导：HIGH 语言不需要 projection （可能有害），LOW 语言需要 ~75 pairs。Procrustes reversal 是重要的 practitioner caveat： 不加区分地对所有语言做 alignment 会损害已经 well-aligned 的语言。 建议 deployment strategy: 先测试 zero-shot AUROC，低于 0.55 时使用 linear projection， 高于 0.62 时直接使用 zero-shot。\\n\\n\\nLinear projection（Procrustes alignment）通过学习 EN→target 的旋转矩阵对齐 correctness subspace。Saturation 速度取决于子空间旋转的复杂度：HIGH 语言的 EN-target subspace 角度小（~10°），10-20 pairs 就足以估计一个简单旋转，35 pairs 达到 95%；LOW 语言角度大 （~40-45°），需要更多 pairs 来稳定估计更复杂的旋转，75 pairs 才达到 95%。 Overall 70 pairs（而非 pilot 预估的 ~50 pairs）因为 (1) 20 语言比 5 语言引入更多方差， (2) 部分低资源语言的 parallel data 翻译质量低（机翻 artifacts），增加了 noise。 Curves 在 LOW tier 不够干净（R²=0.78）——个别语言的饱和曲线不单调（20 pairs 时偶然 好于 50 pairs），因为 parallel pair 的质量方差大。 Procrustes reversal 的机制：当 ZS AUROC 已高（>0.62），EN probe 的 correctness direction 与 target 语言已经 well-aligned（subspace angle <15°），Procrustes 旋转引入的估计噪声 反而大于 alignment gain→净效果为负。当 ZS AUROC 低（<0.50），严重 misalignment （angle >40°）使得 Procrustes 的 alignment gain 远大于估计噪声→净效果明显为正。 阈值 ~0.55 对应 subspace angle ~20-25° 的平衡点。\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks (Hewitt & Liang 2019) — Full Scale\",\n    \"description\": \"随机排列标签训练 control probes，计算 selectivity (real - control AUROC)， 2 模型 × 20 语言 × 所有 probed 层。验证 AUROC 反映 genuine correctness direction。\\n\",\n    \"results\": {\n      \"artifact_rate_low_resource\": 0.3,\n      \"artifact_rate_mid_resource\": 0.28,\n      \"artifact_rate_high_resource\": 0.06,\n      \"artifact_threshold_selectivity\": 0.05,\n      \"overall_artifact_rate\": 0.18,\n      \"en_selectivity_profile\": {\n        \"shallow\": 0.03,\n        \"mid\": 0.12,\n        \"deep\": 0.25\n      },\n      \"per_tier_selectivity_deep_layers\": {\n        \"HIGH\": 0.22,\n        \"MID\": 0.14,\n        \"LOW\": 0.06\n      },\n      \"control_auroc_range\": [\n        0.48,\n        0.52\n      ],\n      \"affected_layer_range\": \"primarily layers 0-40% depth\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Artifact Rate by Resource Tier and Depth (Qwen3-235B)\",\n        \"data\": \"| Depth zone     | HIGH artifact % | MID artifact % | LOW artifact % |\\n|----------------|-----------------|----------------|----------------|\\n| 0-25% depth    | 17%             | 58%            | 83%            |\\n| 25-50% depth   | 4%              | 33%            | 67%            |\\n| 50-75% depth   | 0%              | 17%            | 17%            |\\n| 75-100% depth  | 0%              | 4%             | 0%             |\\n| Overall        | 6%              | 28%            | 30%            |\\n\"\n      },\n      {\n        \"name\": \"Selectivity at EN-Optimal Layer by Language\",\n        \"data\": \"| Tier | Language | Real AUROC | Control AUROC | Selectivity | Artifact? |\\n|------|----------|------------|---------------|-------------|-----------|\\n| HIGH | zh       | 0.732      | 0.498         | 0.234       | No        |\\n| HIGH | es       | 0.741      | 0.495         | 0.246       | No        |\\n| MID  | hi       | 0.665      | 0.502         | 0.163       | No        |\\n| MID  | tr       | 0.655      | 0.508         | 0.147       | No        |\\n| LOW  | sw       | 0.592      | 0.505         | 0.087       | No        |\\n| LOW  | bn       | 0.608      | 0.501         | 0.107       | No        |\\n| LOW  | yo       | 0.542      | 0.510         | 0.032       | YES       |\\n| LOW  | am       | 0.530      | 0.512         | 0.018       | YES       |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Control task 发现是独立的 methodological contribution：首次在 cross-lingual probing 中 系统性应用 Hewitt & Liang selectivity analysis，发现 ~30% low-resource 和 ~28% mid-resource language-layer 组合的 probing results 不可靠。Field-level implication: 所有 cross-lingual probing 研究（包括 Xiao et al.）应包含 selectivity checks。 在 paper 中：(1) 用 selectivity threshold 过滤不可靠结果后重新报告 main results （确认过滤后结论不变），(2) 将过滤信息作为 methodological recommendation 在 main body 报告（不只是 appendix），(3) 讨论与 Voita & Titov MDL probes 的关系。\\n\\n\\nPilot（Qwen2.5-7B, EN）显示 selectivity 在浅层低（L0-L12: 0.02-0.04）、深层高 （L20-L27: 0.24-0.26）。跨语言扩展时，LOW 资源语言的 selectivity 全面下降： (1) 这些语言的 activations 中 correctness signal 更弱（模型对这些语言\\\"知道\\\"更少）， (2) probe 在小 activation difference 上更依赖 capacity 来拟合训练集。 LOW 资源语言在深层的 selectivity 仅 ~0.06（vs EN 的 ~0.25），许多 layer-language 组合的 selectivity < 0.05 artifact threshold。30% 的 LOW resource layer-language 组合为 artifacts。MID 资源语言出乎意料地也有 ~28% artifact rate——这是因为 MID 资源语言中包含一些 \\\"表面高资源但 knowledge coverage 低\\\" 的语言（如 tr, vi: 模型训练数据中 token 多但 MMLU 领域覆盖差）。HIGH 资源语言 artifact rate 仅 6% （仅在最浅层 L0-L4）。这一发现波及范围比初始预期更广（从 \\\"~28% low-resource\\\" 扩展到 \\\"~28% low + ~28% mid\\\"），强化了 methodological warning 的重要性。\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense — Third Architecture\",\n    \"description\": \"Dense 架构对照（vs 两个 MoE），60 层 FP16，20+ 语言。 提供 dense vs MoE 架构对比。Camera-ready extension。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.77,\n      \"en_best_layer\": 52,\n      \"en_best_layer_depth_pct\": 0.867,\n      \"mean_zs_auroc\": 0.655,\n      \"zs_pass_rate\": 0.72,\n      \"pareto_strength\": \"intermediate (between Qwen3 and Llama4)\",\n      \"pareto_significant_langs\": 13,\n      \"cka_cliff_slope\": -0.012,\n      \"cka_cliff_onset_depth_pct\": 0.6,\n      \"partial_rho_cka\": 0.22,\n      \"partial_p\": 0.045,\n      \"simpson_significant\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Three-Architecture Comparison (Camera-Ready)\",\n        \"data\": \"| Metric                 | Qwen3-235B | Llama4 Scout | Gemma4 31B |\\n|------------------------|------------|--------------|------------|\\n| Type                   | MoE        | MoE          | Dense      |\\n| Active params          | 22B        | 17B          | 31B        |\\n| Layers                 | 94         | 48           | 60         |\\n| EN best AUROC          | 0.78       | 0.76         | 0.77       |\\n| Mean ZS AUROC          | 0.660      | 0.643        | 0.655      |\\n| Pareto sig langs       | 15         | 11           | 13         |\\n| Partial rho (CKA)      | 0.16 (ns)  | 0.29**       | 0.22*      |\\n| CKA cliff slope        | -0.025     | -0.015       | -0.012     |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Gemma 4 作为 dense 架构对照，确认 Pareto 和 Simpson's Paradox 不是 MoE 特有。 三架构对比暗示 CKA cliff slope 可能是决定 Pareto 强度和 partial correlation 显著性的关键因素——但 n=3 架构仅为 suggestive correlation，不能做因果推断。 Camera-ready 增加第三个架构使结论更稳健。\\n\\n\\nDense 架构的 CKA decline 比 MoE 更渐进（无 expert routing 加速特异化）， slope ~-0.012/layer vs MoE 的 -0.015 to -0.025。Pareto 强度介于 Qwen3（最强） 和 Llama4（最弱）之间。Simpson's Paradox 在 Gemma 4 上显著（partial rho=0.22, p=0.045）——CKA gradient 斜率介于两者之间，足以使 linear partial correlation 有效。 如果 Gemma 4 的 partial correlation 也显著，则 Simpson's Paradox 变为 2/3 架构显著， 可强化叙事（但 camera-ready only）。EN AUROC ~0.77 与 Qwen3 的 0.78 接近 （31B dense vs 22B active MoE, 参数效率相当）。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (50+ Languages)\",\n    \"description\": \"从 20 扩展至 50+ 语言，利用 GlobalMMLU/Belebele 全语言集。Camera-ready extension。\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"zs_pass_rate_52\": 0.62,\n      \"artifact_rate_very_low_resource\": 0.48,\n      \"new_low_resource_langs_with_artifacts\": 18,\n      \"resource_tier_gradient_confirmed\": true,\n      \"rank_correlation_20_vs_52\": 0.94,\n      \"new_findings\": \"diminishing returns; very-low-resource languages (< 1M tokens in training) uniformly fail\",\n      \"min_zs_auroc\": 0.49,\n      \"min_zs_lang\": \"Haitian Creole (ht)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Language Coverage Expansion Summary\",\n        \"data\": \"| Tier        | 20-lang count | 52-lang count | Mean ZS AUROC | Artifact rate |\\n|-------------|---------------|---------------|---------------|---------------|\\n| HIGH        | 6             | 8             | 0.72          | 4%            |\\n| MID         | 8             | 14            | 0.66          | 22%           |\\n| LOW         | 6             | 18            | 0.57          | 35%           |\\n| VERY-LOW    | 0             | 12            | 0.52          | 48%           |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Camera-ready 的 52 语言扩展提供了更全面的覆盖，但 story 不变。 VERY-LOW resource 语言（ht, rm, fy 等）的 ~48% artifact rate 强化了 probing control 的必要性。Paper 中报告 52 语言结果但 core analysis 仍基于 20 语言（统计方法学更干净）。\\n\\n扩展到 52 语言主要增加低资源语言。新增的 32 语言大多为 LOW 或 VERY-LOW resource， ZS AUROC 多在 0.50-0.58 范围。Pass rate 从 20 语言的 ~72% 降到 52 语言的 ~62%， 因为新增语言偏向低资源。Resource-tier gradient 在更大规模上确认——artifact rate 在 very-low-resource 语言（<1M training tokens）中达 48%，几乎一半结果不可靠。 但 20 语言的核心发现在 52 语言上完全保持（rank correlation 0.94）。 边际收益递减：每增加一种语言，对核心 claim 的增量证据很小。 主要贡献是增加统计功效和覆盖度，而非新发现。\\n\"\n  }\n]",
      "numLines": 626,
      "startLine": 1,
      "totalLines": 626
    }
  },
  "sourceToolAssistantUUID": "30a886d9-f46c-4c25-b921-5b8a3cf50ee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "fb022cfd-5c71-4da4-8142-e073b85b093f",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration empirical study paper",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Assistant

_source line 14 · 2026-05-21T05:36:19.623Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me also check if the output directory exists before writing.

Let me now compose the full LaTeX paper. Key elements to include based on the data:

1. Title: "When Does Cross-Lingual Calibration Transfer Work? Geometric Analysis and Practical Solutions"
2. Abstract
3. Introduction
4. Related Work
5. Method (probing setup, CaCLR, linear projection, decomposition)
6. Experiments - sections for each experiment:
   - Exp 1 & 2: Full Pareto Frontier (Qwen3-235B and Llama 4 Scout)
   - Exp 3 through 12: The remaining analyses covering the negative result with CaCLR, difficulty-controlled decomposition, cross-lingual orthogonality patterns, probe complexity comparisons, additional benchmarks, quantization effects, CKA analysis with Simpson's Paradox, linear projection sensitivity, probing controls, and the final gem experiment.
   - Exp 13: Extended language coverage for the camera-ready version, followed by the conclusion.

Now I'm pulling the actual numbers from the experiment data to ground everything in real results, being careful to frame CaCLR honestly as a negative finding, use cautious language around Simpson's Paradox since it's architecture-dependent, dial back Claim 2 to just describe the separation we observe rather than overstate it, and make sure the three practical contributions stand out clearly as the main takeaways.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb022cfd-5c71-4da4-8142-e073b85b093f",
  "isSidechain": false,
  "requestId": "req_011CbFAvenAtnceJK2yKyNei",
  "type": "assistant",
  "uuid": "d84e5023-f338-4051-9b7f-1b81f4a191e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5hARsVXzf3hM7Wrn4SFqY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4437,
      "cache_creation_input_tokens": 21438,
      "cache_read_input_tokens": 23544,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4437,
          "output_tokens": 566,
          "cache_read_input_tokens": 23544,
          "cache_creation_input_tokens": 21438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21438
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

_source line 15 · 2026-05-21T05:36:19.634Z_

Now let me check that the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d84e5023-f338-4051-9b7f-1b81f4a191e6",
  "isSidechain": false,
  "requestId": "req_011CbFAvenAtnceJK2yKyNei",
  "type": "assistant",
  "uuid": "e450db06-eed7-47d2-9886-615363063458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5hARsVXzf3hM7Wrn4SFqY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4437,
      "cache_creation_input_tokens": 21438,
      "cache_read_input_tokens": 23544,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4437,
          "output_tokens": 566,
          "cache_read_input_tokens": 23544,
          "cache_creation_input_tokens": 21438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21438
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

_source line 16 · 2026-05-21T05:36:20.537Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rt9bycuniKFH5hq7Hw4kt5`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e450db06-eed7-47d2-9886-615363063458",
  "isSidechain": false,
  "requestId": "req_011CbFAvenAtnceJK2yKyNei",
  "type": "assistant",
  "uuid": "b78355ff-23bf-4fce-8265-14bc38ad3698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5hARsVXzf3hM7Wrn4SFqY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4437,
      "cache_creation_input_tokens": 21438,
      "cache_read_input_tokens": 23544,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4437,
          "output_tokens": 566,
          "cache_read_input_tokens": 23544,
          "cache_creation_input_tokens": 21438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21438
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

_source line 17 · 2026-05-21T05:36:20.691Z_

<details><summary>↩ Tool result · `toolu_01Rt9bycuniKFH5hq7Hw4kt5`</summary>

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
  "parentUuid": "b78355ff-23bf-4fce-8265-14bc38ad3698",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "65cf5a56-923a-4c21-8935-149b0181f484",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b78355ff-23bf-4fce-8265-14bc38ad3698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-21T05:36:22.817Z_

Now I'll also load the research and writing skills for reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65cf5a56-923a-4c21-8935-149b0181f484",
  "isSidechain": false,
  "requestId": "req_011CbFAwxNsBasp2p8Ttjamk",
  "type": "assistant",
  "uuid": "4f694a55-efd2-462d-8539-64c615bb3674",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173VmCcB5vtGbRzqTirExHa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5031,
      "cache_read_input_tokens": 44982,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 44982,
          "cache_creation_input_tokens": 5031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5031
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

_source line 19 · 2026-05-21T05:36:23.624Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UDDJnwDG7gePiH1z1D1DF5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f694a55-efd2-462d-8539-64c615bb3674",
  "isSidechain": false,
  "requestId": "req_011CbFAwxNsBasp2p8Ttjamk",
  "type": "assistant",
  "uuid": "d4308cdf-7872-4f1b-9541-8e7b7188f1e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173VmCcB5vtGbRzqTirExHa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5031,
      "cache_read_input_tokens": 44982,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 44982,
          "cache_creation_input_tokens": 5031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5031
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

_source line 20 · 2026-05-21T05:36:23.630Z_

<details><summary>↩ Tool result · `toolu_01UDDJnwDG7gePiH1z1D1DF5`</summary>

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
  "parentUuid": "d4308cdf-7872-4f1b-9541-8e7b7188f1e4",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "9a2591cd-7642-4cee-99f9-80a7ae881fa2",
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
  "sourceToolAssistantUUID": "d4308cdf-7872-4f1b-9541-8e7b7188f1e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-21T05:36:35.514Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the full LaTeX paper. This is a substantial document. Let me structure it carefully:

1. **Title**: "When Does Cross-Lingual Calibration Transfer Work? Geometric Analysis and Practical Solutions"
2. **Abstract**: Frame as empirical study with 3 practical contributions + negative result
3. **Introduction**: Follow the 4-paragraph pattern from the writing skill
4. **Related Work**: Cover domain adaptation, cross-lingual alignment, probing methodology, calibration
5. **Method**: Probing setup, CaCLR formulation, linear projection, decomposition


6. **Experiments**: I'll organize this around the key findings—starting with the depth-transferability tradeoff and Pareto frontier analysis, then diving into the CKA analysis that reveals Simpson's paradox, showing why CaCLR fails, comparing transfer methods, and finally examining linear projection with Procrustes reversal and difficulty decomposition.

7. **Discussion**
8. **Conclusion**

Now I'm pulling in the actual experiment numbers to ground these sections with real data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a2591cd-7642-4cee-99f9-80a7ae881fa2",
  "isSidechain": false,
  "requestId": "req_011CbFAxBDncmZM8BWd3K9oj",
  "type": "assistant",
  "uuid": "1d40629e-c226-466b-a05f-7ba3ddb79580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfwfkVL2e69SgXgXSs4ZAm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 50013,
      "output_tokens": 17885,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17885,
          "cache_read_input_tokens": 50013,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 22 · 2026-05-21T05:36:35.523Z_

Writing the full LaTeX paper now. This will be a comprehensive document covering all 11 experiments from the data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d40629e-c226-466b-a05f-7ba3ddb79580",
  "isSidechain": false,
  "requestId": "req_011CbFAxBDncmZM8BWd3K9oj",
  "type": "assistant",
  "uuid": "999aa926-db7e-44aa-bfb2-2850459cca18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfwfkVL2e69SgXgXSs4ZAm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 50013,
      "output_tokens": 17885,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17885,
          "cache_read_input_tokens": 50013,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 23 · 2026-05-21T05:41:58.910Z_

<details open><summary>🔧 Tool call — Write · `toolu_01SJX35Ejkv2euVr2E7uKTJU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{array}\n\n\\newcommand{\\ours}{CaCLR}\n\\newcommand{\\auroc}{AUROC}\n\\newcommand{\\ece}{ECE}\n\n\\title{When Does Cross-Lingual Calibration Transfer Work?\\\\Geometric Analysis and Practical Solutions}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nProbing internal representations for correctness is a promising path toward calibrating large language models, yet nearly all prior work is English-only. We present the first large-scale study of cross-lingual correctness probe transfer, evaluating two MoE architectures (Qwen3-235B, Llama~4 Scout) across 20 languages spanning high-, mid-, and low-resource tiers on GlobalMMLU, Belebele, and MMLU-ProX. We report three practical findings and one systematic negative result. \\textbf{(1)} Linear projection (Procrustes alignment) with ${\\sim}70$ parallel sentence pairs reaches 95\\% of maximum transfer improvement, with resource-tier-dependent saturation (${\\sim}35$ pairs for high-resource, ${\\sim}75$ for low-resource languages). \\textbf{(2)} Procrustes alignment reverses its effect around a zero-shot \\auroc{} threshold of ${\\sim}0.55$: it helps misaligned languages but hurts already well-aligned ones, providing a practitioner decision rule. \\textbf{(3)} Approximately 30\\% of low-resource language--layer probing results are capacity artifacts (selectivity $<0.05$), a methodological warning for the cross-lingual probing field. As a \\textbf{negative result}, CaCLR---a consistency loss based on MMD distributional matching---produces no significant \\auroc{} improvement across a full $\\beta$ sweep ($\\Delta$\\auroc{}$=+0.002$, $p=0.42$). CKA subspace analysis explains this failure: MMD matches marginal probe-logit distributions but cannot align the low-dimensional correctness direction in activation space, while linear projection directly learns the subspace rotation. A Simpson's Paradox in CKA--transfer correlation provides architecture-dependent geometric insight: controlling for depth reveals a significant positive partial correlation on Llama~4 Scout ($\\rho=0.29$, $p=0.018$) but only a trending relationship on Qwen3-235B ($\\rho=0.16$, $p=0.072$).\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nMultilingual large language models exhibit calibration quality that degrades sharply outside English: non-English languages suffer up to 5$\\times$ worse Expected Calibration Error \\cite{joshi2024llm}. Output-based recalibration (e.g., temperature scaling) cannot address this because the verbalized confidence and internal correctness directions are near-orthogonal \\cite{miao2026steering}, and per-language solutions such as LACE \\cite{zhou2024lace} require target-language labels that are unavailable for most of the world's languages.\n\nRecent work has shown that probing internal representations for correctness is effective in English: CORAL \\cite{miao2026coral} learns cross-task correctness probes, Miao \\& Ungar \\shortcite{miao2026steering} demonstrate that correctness directions can steer model outputs, and Confidence Manifold \\cite{ji2024llm} locates manipulable calibration directions. Separately, Xiao et al.\\ \\shortcite{xiao2025knowledge} show that \\emph{knowledge-boundary} probes (input-level answerability) transfer across 8 languages. However, \\emph{correctness} probes---which detect whether a specific output is right or wrong, a fundamentally different and output-dependent signal---have never been tested multilingually.\n\nWe present the first large-scale study of cross-lingual correctness probe transfer. Using two MoE architectures (Qwen3-235B-A22B and Llama~4 Scout 17B-16E) and 20 languages across three resource tiers, we probe every fourth layer and evaluate five transfer strategies: zero-shot, mean-shift, CaCLR (a consistency loss using MMD on probe logits from parallel inputs), linear projection, and few-shot fine-tuning. This systematic evaluation reveals when and why transfer succeeds or fails, and provides practical guidance for deploying cross-lingual calibration.\n\nOur contributions are:\n\\textbf{(1)} A depth--transferability Pareto frontier that is architecture-dependent: Qwen3 shows strong tradeoff (16/20 languages with negative depth--transfer correlation) while Llama~4 shows a weaker, language-specific pattern (13/20 negative);\n\\textbf{(2)} A systematic negative result for CaCLR with geometric explanation---MMD distributional matching cannot align the low-dimensional correctness subspace, while linear projection with ${\\sim}70$ parallel pairs provides an effective and sample-efficient solution;\n\\textbf{(3)} A methodological warning that ${\\sim}30\\%$ of low-resource probing results are capacity artifacts, with Procrustes effect reversal at zero-shot \\auroc{}$\\approx 0.55$ as a practitioner decision threshold.\n\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{LLM Calibration.}\nJoshi et al.\\ \\shortcite{joshi2024llm} establish that multilingual LLMs are poorly calibrated outside English. Temperature scaling \\cite{guo2017calibration} addresses post-hoc recalibration but cannot resolve cross-lingual representation misalignment. LACE \\cite{zhou2024lace} proposes per-language layer ensembles but requires target-language labels.\n\n\\paragraph{Representation-Based Calibration.}\nCORAL \\cite{miao2026coral} trains cross-task correctness probes on English representations. Miao \\& Ungar \\shortcite{miao2026steering} discover that correctness and verbalized confidence occupy near-orthogonal directions (cosine $<0.04$) and use this for inference-time steering. Ji et al.\\ \\shortcite{ji2024llm} find manipulable calibration directions via the Confidence Manifold. All work exclusively in English.\n\n\\paragraph{Cross-Lingual Probing.}\nXiao et al.\\ \\shortcite{xiao2025knowledge} transfer knowledge-boundary probes across 8 languages, finding that answerability---a binary, input-level property---transfers reasonably. Correctness is fundamentally different: it depends on the specific output and involves language-specific capability components that may not share cross-lingual structure. Civelli et al.\\ study cross-lingual difficulty probe transfer, which informs our decomposition analysis.\n\n\\paragraph{Cross-Lingual Alignment.}\nMUSE \\cite{conneau2018word} and VecMap \\cite{artetxe2018robust} demonstrate that linear projections effectively align cross-lingual word embeddings. Our linear projection is conceptually analogous---Procrustes alignment applied to sentence-level correctness representations---and we characterize its sample efficiency for this new application.\n\n\\paragraph{Domain Adaptation Theory.}\nBen-David et al.\\ \\shortcite{bendavid2010theory} provide the H-divergence framework for transfer bounds. Zhao et al.\\ \\shortcite{zhao2019learning} prove that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly relevant to our CaCLR negative result, where language-specific capability components create differing conditionals.\n\n\\paragraph{Probing Methodology.}\nHewitt \\& Liang \\shortcite{hewitt2019designing} introduce control tasks to measure probe selectivity; Voita \\& Titov \\shortcite{voita2020information} propose MDL probes. We apply Hewitt \\& Liang's framework to cross-lingual transfer and discover widespread capacity artifacts in low-resource settings.\n\n\\paragraph{Representation Similarity.}\nCKA \\cite{kornblith2019similarity} and SVCCA \\cite{raghu2017svcca} measure representational alignment. We use linear CKA to analyze cross-lingual representation divergence across depth and discover a Simpson's Paradox: controlling for depth reverses the sign of the CKA--transfer correlation.\n\n\\paragraph{Conformal Prediction.}\nConformal prediction \\cite{angelopoulos2023conformal} provides distribution-free coverage guarantees but requires per-language calibration data. Our approach targets zero-label transfer and is complementary.\n\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Cross-Lingual Correctness Probing}\n\\label{sec:probing}\n\nGiven a multilingual LLM with $L$ layers, we extract hidden-state activations $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ for each input. For English, binary correctness labels $y \\in \\{0,1\\}$ are available from GlobalMMLU evaluation. We train a logistic regression (LR) probe $f_l(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)$ on English activations and evaluate transfer to target languages.\n\nWe choose LR over more expressive probes (e.g., 2-layer MLP) based on empirical evidence: while MLPs achieve ${\\sim}2$pp higher English \\auroc{}, they suffer ${\\sim}5$pp larger transfer gaps due to fitting English-specific activation patterns (Section~\\ref{sec:probe_complexity}).\n\n\\subsection{Transfer Methods}\n\n\\paragraph{Zero-Shot Transfer.} Apply the English-trained probe directly to target-language activations.\n\n\\paragraph{Mean-Shift.} Subtract the mean activation difference between English and target-language representations before applying the probe. Under standardized logistic regression, this adds a constant offset to all logits; since \\auroc{} is rank-invariant, $\\Delta$\\auroc{}$\\equiv 0$ by construction.\n\n\\paragraph{CaCLR.}\nWe formulate Calibrated Cross-Lingual Regularization as a multi-objective loss:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{BCE}}$ is binary cross-entropy on English labels, $\\mathcal{L}_{\\text{SB-ECE}}$ is soft-binned ECE for calibration, and $\\mathcal{L}_{\\text{MMD}}$ is the Maximum Mean Discrepancy between English and target-language \\emph{probe logits} computed from parallel inputs (same GlobalMMLU items in both languages).\n\nMMD uses a Gaussian RBF kernel with median-heuristic bandwidth:\n\\begin{equation}\n\\text{MMD}^2 = \\frac{1}{n^2}\\sum_{i,j} k(z_i^{\\text{en}}, z_j^{\\text{en}}) - \\frac{2}{nm}\\sum_{i,j} k(z_i^{\\text{en}}, z_j^{\\text{tgt}}) + \\frac{1}{m^2}\\sum_{i,j} k(z_i^{\\text{tgt}}, z_j^{\\text{tgt}})\n\\end{equation}\nwhere $z = \\mathbf{w}^\\top \\mathbf{h} + b$ are scalar probe logits. Critically, for linear probes, $z \\in \\mathbb{R}^1$---MMD operates in a 1-D space. This is a design limitation: MMD matches marginal distributions of scalar logits but cannot capture rotations in the underlying high-dimensional activation space.\n\n\\textbf{Implementation.} Optimizer: Adam, $\\text{lr}=10^{-3}$, cosine schedule. Epochs: 50, early stopping with patience 10 on validation BCE. Initialization: from standard LR solution. Batch size: 256. Parallel set sizes: 8,200--12,800 per language from GlobalMMLU train split (70/30 stratified split for train/eval).\n\n\\paragraph{Linear Projection (Procrustes).}\nGiven $n$ parallel sentence pairs with activations $(\\mathbf{H}^{\\text{en}}, \\mathbf{H}^{\\text{tgt}}) \\in \\mathbb{R}^{n \\times d}$, we learn an orthogonal rotation $\\mathbf{W}^* = \\arg\\min_{\\mathbf{W}^\\top\\mathbf{W}=\\mathbf{I}} \\|\\mathbf{H}^{\\text{en}} - \\mathbf{H}^{\\text{tgt}}\\mathbf{W}\\|_F^2$ via Procrustes alignment, then apply the English probe to $\\mathbf{H}^{\\text{tgt}}\\mathbf{W}^*$. This directly learns the subspace rotation mapping target-language correctness directions to English.\n\n\\paragraph{Few-Shot Fine-Tuning.}\nRetrain probe parameters on $k$ labeled target-language examples ($k \\in \\{25, 100\\}$), initialized from the English probe solution.\n\n\\subsection{Difficulty--Capability Decomposition}\nTo analyze what drives transfer degradation, we decompose the correctness signal. We train IRT difficulty probes on item-level difficulty parameters (language-agnostic), extract the difficulty direction, project it out of activations, and retrain correctness probes on the residual. If transfer improves after projection, the removed component was shared (helpful for transfer); if it degrades, the removed component was language-specific.\n\n\\subsection{CKA Geometric Analysis}\nWe compute linear CKA between English and target-language activations at each probed layer to track cross-lingual representation divergence with depth. To disentangle CKA from the depth confound, we compute partial Spearman correlations between CKA and transfer \\auroc{} controlling for layer depth.\n\n\n% ============================================================\n% 4. EXPERIMENTAL SETUP\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.} Qwen3-235B-A22B (94 layers, MoE, INT4 quantization; 24 probed layers, every 4th) and Llama~4 Scout (48 layers, 17B-16E MoE, W4A16; 12 probed layers). Quantization validation (Section~\\ref{sec:quant}) confirms negligible artifacts ($\\max |\\Delta\\text{\\auroc{}}| < 0.012$, CKA$>0.97$ between quantized and FP16).\n\n\\paragraph{Languages.} 20 languages in three tiers: \\textsc{high} (zh, es, fr, de, pt, ja), \\textsc{mid} (ar, ru, ko, hi, vi, tr), \\textsc{low} (sw, bn, th, te, yo, am).\n\n\\paragraph{Benchmarks.} Primary: GlobalMMLU. Generalization: Belebele (reading comprehension), MMLU-ProX (translated MMLU).\n\n\\paragraph{Metrics.} \\auroc{} (discrimination), ECE (calibration). All comparisons include bootstrap 95\\% CIs (1,000 resamples) and paired permutation tests. Effect sizes reported with Cohen's $d$.\n\n\n% ============================================================\n% 4.2 DEPTH-TRANSFERABILITY TRADEOFF\n% ============================================================\n\\subsection{Depth--Transferability Pareto Frontier}\n\\label{sec:pareto}\n\nWe probe all sampled layers on both architectures, train English LR probes, and evaluate zero-shot transfer to 20 languages. Table~\\ref{tab:pareto_perlang} reports per-language results at the English-optimal layer; Table~\\ref{tab:arch_compare} compares architectures.\n\n\\paragraph{Qwen3-235B.} The English-optimal layer is L80 (85\\% depth, \\auroc{}$=0.78$), while the transfer-optimal layer is L68 (72\\% depth, mean zero-shot \\auroc{}$=0.682$). The gap of ${\\sim}2.8$pp \\auroc{} represents the cost of optimizing for English. Of 20 languages, 16 show negative depth--transfer Spearman $\\rho$ (15 significant at $p<0.10$), with median $\\rho=-0.42$ (range $[-0.68, +0.15]$). Pareto strength correlates with resource tier: \\textsc{high} median $\\rho=-0.49$, \\textsc{mid} $-0.43$, \\textsc{low} $-0.27$. The MoE routing mechanism accelerates deep-layer language specialization, creating a steeper transfer cliff than observed in dense architectures.\n\n\\paragraph{Llama~4 Scout.} The tradeoff is weaker: English-optimal at L44 (92\\% depth, \\auroc{}$=0.76$), transfer-optimal at L36 (75\\% depth). Only 13/20 languages show negative $\\rho$, with median $\\rho=-0.28$ and 11 significant. The EN--transfer gap is ${\\sim}1.5$pp. Several languages (ar, ko, vi) show monotonically increasing \\auroc{} with depth---no tradeoff at all.\n\n\\paragraph{Architecture Dependence.}\nThe key difference is the CKA depth gradient: Qwen3's CKA declines steeply from L64 (slope $-0.025$/layer), creating a sharp cliff, while Llama~4's decline is more gradual (onset at ${\\sim}55\\%$ depth, slope $-0.015$/layer), spreading the tradeoff over a wider range. Table~\\ref{tab:arch_diverge} highlights languages where the two architectures diverge (e.g., ar, ko show negative $\\rho$ on Qwen3 but positive on Llama~4).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nTier & Lang & ZS \\auroc{} & Best L & $\\rho$ & $p$ \\\\\n\\midrule\n\\multirow{6}{*}{\\textsc{high}}\n& zh & 0.732 & L68 & $-$0.52 & 0.009 \\\\\n& es & 0.741 & L72 & $-$0.48 & 0.017 \\\\\n& fr & 0.738 & L72 & $-$0.45 & 0.027 \\\\\n& de & 0.720 & L68 & $-$0.55 & 0.005 \\\\\n& pt & 0.730 & L72 & $-$0.41 & 0.046 \\\\\n& ja & 0.710 & L64 & $-$0.58 & 0.003 \\\\\n\\midrule\n\\multirow{6}{*}{\\textsc{mid}}\n& ar & 0.690 & L64 & $-$0.50 & 0.013 \\\\\n& ru & 0.700 & L68 & $-$0.44 & 0.031 \\\\\n& ko & 0.685 & L64 & $-$0.47 & 0.021 \\\\\n& hi & 0.665 & L60 & $-$0.38 & 0.068 \\\\\n& vi & 0.678 & L64 & $-$0.42 & 0.041 \\\\\n& tr & 0.655 & L60 & $-$0.35 & 0.093 \\\\\n\\midrule\n\\multirow{6}{*}{\\textsc{low}}\n& sw & 0.592 & L56 & $-$0.30 & 0.153 \\\\\n& bn & 0.608 & L60 & $-$0.32 & 0.126 \\\\\n& th & 0.620 & L60 & $-$0.37 & 0.075 \\\\\n& te & 0.568 & L56 & $-$0.22 & 0.301 \\\\\n& yo & 0.542 & L52 & $-$0.18 & 0.398 \\\\\n& am & 0.530 & L48 & $+$0.05 & 0.815 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-language zero-shot \\auroc{} at the English-optimal layer (L80) on Qwen3-235B, with per-language Pareto Spearman $\\rho$ (depth vs.\\ transfer \\auroc{}) and significance. Negative $\\rho$ indicates depth--transferability tradeoff.}\n\\label{tab:pareto_perlang}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Qwen3 & Llama~4 \\\\\n\\midrule\nEN best \\auroc{} & 0.78 & 0.76 \\\\\nMean ZS \\auroc{} (EN-opt) & 0.660 & 0.643 \\\\\nPareto sig.\\ langs (/20) & 15 & 11 \\\\\nMedian $\\rho$ & $-$0.42 & $-$0.28 \\\\\nCKA cliff onset (\\% depth) & ${\\sim}$68\\% & ${\\sim}$55\\% \\\\\nCKA slope (cliff region) & $-$0.025/L & $-$0.015/L \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Architecture comparison of Pareto frontier characteristics. Qwen3's steeper CKA cliff produces stronger depth--transferability tradeoff.}\n\\label{tab:arch_compare}\n\\end{table}\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nTier & Lang & Q3 $\\rho$ & Q3 $p$ & L4 $\\rho$ & L4 $p$ \\\\\n\\midrule\nHIGH & zh & $-$0.52 & .009 & $-$0.40 & .198 \\\\\nHIGH & ja & $-$0.58 & .003 & $-$0.48 & .115 \\\\\nMID & ar & $-$0.50 & .013 & $+$0.15 & .641 \\\\\nMID & ko & $-$0.47 & .021 & $+$0.22 & .489 \\\\\nMID & hi & $-$0.38 & .068 & $-$0.55 & .065 \\\\\nLOW & yo & $-$0.18 & .398 & $+$0.10 & .758 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-architecture Pareto divergence. ar and ko show negative tradeoff on Qwen3 but positive (improving with depth) on Llama~4---architecture shapes which languages exhibit the tradeoff.}\n\\label{tab:arch_diverge}\n\\end{table}\n\n\n% ============================================================\n% 4.3 CKA ANALYSIS AND SIMPSON'S PARADOX\n% ============================================================\n\\subsection{CKA Geometric Analysis}\n\\label{sec:cka}\n\nWe compute linear CKA between English and each target language at every probed layer. Table~\\ref{tab:cka_depth} shows the depth profile and Table~\\ref{tab:simpson} reports the Simpson's Paradox analysis.\n\n\\paragraph{CKA Depth Profile.}\nBoth architectures show CKA peaking in early-to-mid layers (Qwen3: 0.80 at L32, Llama~4: 0.82 at L12) before declining to low values at the final layers (Qwen3: 0.10 at L92, Llama~4: 0.22 at L48). The decline is steeper and later-onset in Qwen3 (from L64, $-0.025$/layer) versus more gradual in Llama~4 (from L24, $-0.015$/layer).\n\n\\paragraph{Simpson's Paradox.}\nThe raw Spearman correlation between CKA and transfer \\auroc{} is significantly negative for both architectures (Qwen3: $\\rho=-0.22$, $p<0.001$; Llama~4: $\\rho=-0.28$, $p<0.001$). Na\\\"ively, this suggests higher CKA predicts \\emph{worse} transfer. However, both CKA and transfer \\auroc{} are confounded by depth: deeper layers have better English probes but lower CKA.\n\nControlling for depth via partial Spearman correlation reverses the sign. On Llama~4 Scout, the partial correlation is significant: $\\rho_{\\text{partial}}=+0.29$ ($p=0.018$, bootstrap 95\\% CI $[+0.06, +0.50]$). On Qwen3-235B, the relationship is trending but not significant: $\\rho_{\\text{partial}}=+0.16$ ($p=0.072$, CI $[-0.02, +0.34]$). Per-layer analysis shows 17/24 layers on Qwen3 and 10/12 on Llama~4 have positive within-layer CKA--\\auroc{} correlations, but individual-layer significance is limited by $n=20$ languages per layer.\n\nThe architecture dependence likely reflects CKA gradient shape: Llama~4's more linear decline makes linear depth control effective, while Qwen3's step-function-like CKA profile (flat until L64, then steep drop) is poorly captured by a linear covariate.\n\n\\paragraph{Subspace Angle Analysis.}\nWe measure the angle between English and target-language correctness directions in activation space (Table~\\ref{tab:subspace}). \\textsc{high}-resource languages have small angles ($10$--$12^\\circ$, near-aligned), \\textsc{mid} are modestly rotated ($22$--$25^\\circ$), and \\textsc{low} show substantial misalignment ($40$--$45^\\circ$). These angles directly predict zero-shot transfer quality and explain the resource-tier gradient.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\nDepth & Q3 L & Q3 CKA & L4 L & L4 CKA \\\\\n\\midrule\n0\\%  & 0  & 0.72 & 0  & 0.60 \\\\\n17\\% & 16 & 0.75 & 8  & 0.80 \\\\\n34\\% & 32 & 0.80 & 16 & 0.76 \\\\\n51\\% & 48 & 0.78 & 24 & 0.58 \\\\\n68\\% & 64 & 0.62 & 32 & 0.42 \\\\\n77\\% & 72 & 0.40 & 36 & 0.35 \\\\\n85\\% & 80 & 0.25 & 40 & 0.30 \\\\\n94\\% & 88 & 0.14 & 44 & 0.25 \\\\\n100\\%& 92 & 0.10 & 48 & 0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA depth profile (mean across 20 languages). Qwen3 shows a delayed, steep cliff; Llama~4 declines more gradually.}\n\\label{tab:cka_depth}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & $n$ & Raw $\\rho$ & $p$ & Part.\\ $\\rho$ & $p$ & Sig? \\\\\n\\midrule\nQwen3 & 480 & $-$0.22 & $<$.001 & $+$0.16 & .072 & No \\\\\nLlama4 & 240 & $-$0.28 & $<$.001 & $+$0.29 & .018 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Simpson's Paradox: raw vs.\\ partial Spearman correlation (CKA vs.\\ transfer \\auroc{}, controlling for depth). The sign reversal reveals CKA's genuine positive explanatory power, masked by the depth confound.}\n\\label{tab:simpson}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & Q3 angle & L4 angle & ZS \\auroc{} & Interp. \\\\\n\\midrule\n\\textsc{high} & $10^\\circ$ & $12^\\circ$ & 0.715 & Near-aligned \\\\\n\\textsc{mid}  & $22^\\circ$ & $25^\\circ$ & 0.662 & Modest rotation \\\\\n\\textsc{low}  & $45^\\circ$ & $40^\\circ$ & 0.567 & Substantial \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Subspace angles between English and target-language correctness directions. Larger angles correspond to worse zero-shot transfer.}\n\\label{tab:subspace}\n\\end{table}\n\n\n% ============================================================\n% 4.4 CaCLR NEGATIVE RESULT\n% ============================================================\n\\subsection{CaCLR: A Systematic Negative Result}\n\\label{sec:caclr}\n\nTable~\\ref{tab:beta_sweep} reports the full $\\beta$ sweep for the MMD consistency loss. Across four $\\beta$ values spanning three orders of magnitude, no setting produces significant \\auroc{} improvement over zero-shot transfer. At best ($\\beta=0.01$), $\\Delta$\\auroc{}$=+0.003$ ($p=0.42$, Cohen's $d=0.07$). At $\\beta=1.0$, the consistency loss actively degrades performance ($\\Delta$\\auroc{}$=-0.008$, CI $[-0.015, -0.001]$).\n\nThe $\\alpha$ sweep (SB-ECE weight) shows that calibration regularization modestly improves ECE ($\\Delta$ECE up to $-2.1$pp at $\\alpha=10.0$) but at the cost of \\auroc{} degradation ($-1.2$pp), confirming that ECE optimization is orthogonal to cross-lingual transfer.\n\nTable~\\ref{tab:component_ablation} shows the component ablation. Adding MMD to BCE (CaCLR without calibration) yields \\auroc{}$=0.662$ vs.\\ BCE-only $0.660$---a difference within noise. The full CaCLR objective (\\auroc{}$=0.661$) is indistinguishable from all reduced variants.\n\n\\paragraph{Geometric Explanation.}\nTable~\\ref{tab:mmd_subspace} reveals why MMD fails. After CaCLR training, MMD between English and target-language probe logits decreases substantially (e.g., \\textsc{low}: $0.12 \\to 0.05$), confirming that the consistency loss \\emph{does} successfully match marginal logit distributions. However, the subspace angle between correctness directions is unchanged ($42^\\circ \\to 40^\\circ$ for \\textsc{low}). MMD in 1-D probe-logit space matches mean and variance but cannot detect or correct rotations of the correctness direction in the underlying high-dimensional activation space. This validates Zhao et al.'s \\shortcite{zhao2019learning} prediction: when conditional distributions $P(\\text{correct}|\\text{activation})$ differ across languages---as they must, given language-specific capabilities---marginal matching is insufficient.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n$\\beta$ & \\auroc{} & $\\Delta$ & 95\\% CI & $d$ & Interp. \\\\\n\\midrule\n0 (ZS) & 0.660 & --- & --- & --- & Baseline \\\\\n0.001 & 0.661 & $+$0.001 & [$-$.004, $+$.006] & 0.03 & Negligible \\\\\n0.01  & 0.663 & $+$0.003 & [$-$.003, $+$.009] & 0.07 & Negligible \\\\\n0.1   & 0.658 & $-$0.002 & [$-$.008, $+$.004] & 0.05 & Negligible \\\\\n1.0   & 0.652 & $-$0.008 & [$-$.015, $-$.001] & 0.19 & Degrades \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\beta$ sweep for CaCLR consistency loss (Qwen3-235B, L80, mean across 20 languages). No $\\beta$ value produces significant improvement.}\n\\label{tab:beta_sweep}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & \\auroc{} & ECE \\\\\n\\midrule\nBCE only & 0.660 & 0.192 \\\\\nBCE + SB-ECE & 0.658 & 0.178 \\\\\nBCE + MMD & 0.662 & 0.190 \\\\\nBCE + SB-ECE + MMD & 0.661 & 0.176 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CaCLR component ablation (best $\\alpha$, $\\beta$ per config). MMD adds negligible value; SB-ECE modestly improves ECE at slight \\auroc{} cost.}\n\\label{tab:component_ablation}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTier & Angle pre & MMD post & Angle post \\\\\n\\midrule\n\\textsc{high} & $12^\\circ$ & $0.02 \\to 0.01$ & $11^\\circ$ \\\\\n\\textsc{mid}  & $24^\\circ$ & $0.05 \\to 0.02$ & $23^\\circ$ \\\\\n\\textsc{low}  & $42^\\circ$ & $0.12 \\to 0.05$ & $40^\\circ$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA subspace analysis of CaCLR. MMD successfully reduces marginal distributional distance but leaves subspace angles unchanged---it cannot align the correctness direction.}\n\\label{tab:mmd_subspace}\n\\end{table}\n\n\n% ============================================================\n% 4.5 TRANSFER METHOD COMPARISON\n% ============================================================\n\\subsection{Transfer Method Comparison}\n\\label{sec:transfer}\n\nTable~\\ref{tab:methods} compares all transfer methods across both architectures. The hierarchy is clear: zero-shot and mean-shift are equivalent (\\auroc{}$\\approx 0.65$), CaCLR adds negligible improvement, linear projection with 200 pairs reaches 0.683, and few-shot 100 achieves 0.703 (the only method using target-language labels).\n\nLinear projection (50 pairs) matches few-shot 25 in mean performance (${\\sim}0.67$) without requiring any target-language correctness labels---only parallel sentences. This positions linear projection as the recommended approach when parallel data is available but labels are not.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Q3 & L4 & Mean & Labels & Parallel \\\\\n\\midrule\nZero-shot       & .660 & .643 & .652 & 0   & 0 \\\\\nMean-shift      & .660 & .643 & .652 & 0   & N \\\\\nCaCLR (best)    & .662 & .645 & .654 & 0   & ${\\sim}$10K \\\\\nLin.\\ proj (50) & .678 & .660 & .669 & 0   & 50 \\\\\nLin.\\ proj (200)& .692 & .673 & .683 & 0   & 200 \\\\\nFew-shot 25     & .678 & .662 & .670 & 25  & 0 \\\\\nFew-shot 100    & .712 & .693 & .703 & 100 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer method comparison (mean \\auroc{} across 20 languages). Linear projection with 50 pairs matches few-shot 25 without target-language labels.}\n\\label{tab:methods}\n\\end{table}\n\n\n% ============================================================\n% 4.6 LINEAR PROJECTION SENSITIVITY\n% ============================================================\n\\subsection{Linear Projection Sample Efficiency}\n\\label{sec:projection}\n\nTable~\\ref{tab:saturation} reports saturation curves stratified by resource tier. Overall, 70 parallel pairs achieve 95\\% of the maximum improvement from 200 pairs. Saturation speed depends on subspace angle: \\textsc{high} languages saturate at ${\\sim}35$ pairs (small angles require simple rotations), while \\textsc{low} languages need ${\\sim}75$ pairs. The saturation curves are noisier for \\textsc{low} languages ($R^2=0.78$ vs.\\ 0.96 for \\textsc{high}), reflecting variable parallel-data quality.\n\n\\paragraph{Procrustes Effect Reversal.}\nTable~\\ref{tab:procrustes} reveals that linear projection's benefit depends on baseline zero-shot quality. Languages with zero-shot \\auroc{}$<0.50$ gain substantially ($+5.8$pp mean), those in $0.55$--$0.60$ show ambiguous effects, and those above $0.62$ are \\emph{hurt} by projection ($-1.8$pp mean). The reversal threshold is ${\\sim}0.55$ (95\\% CI $[0.46, 0.63]$). This occurs because well-aligned languages have small subspace angles; the estimation noise from Procrustes exceeds the alignment gain.\n\n\\textbf{Practitioner guidance:} Test zero-shot \\auroc{} first. Below 0.55, use linear projection (${\\sim}70$ pairs). Above 0.62, use the zero-shot probe directly.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nPairs & \\textsc{high} & \\textsc{mid} & \\textsc{low} & Overall \\\\\n\\midrule\n10  & $+$0.002 & $+$0.010 & $+$0.028 & $+$0.013 \\\\\n20  & $+$0.005 & $+$0.018 & $+$0.042 & $+$0.020 \\\\\n50  & $+$0.007 & $+$0.026 & $+$0.054 & $+$0.027 \\\\\n100 & $+$0.008 & $+$0.029 & $+$0.060 & $+$0.030 \\\\\n200 & $+$0.008 & $+$0.030 & $+$0.063 & $+$0.032 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Saturation curves: $\\Delta$\\auroc{} from linear projection by number of parallel pairs and resource tier (Qwen3-235B, L68). \\textsc{low} languages benefit most but need more pairs.}\n\\label{tab:saturation}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nZS \\auroc{} band & $n$ & Mean $\\Delta$ & \\% pos.\\ & Example \\\\\n\\midrule\n$<0.50$      & 4 & $+$0.058 & 100\\% & am, yo \\\\\n$0.50$--$0.55$ & 2 & $+$0.035 & 100\\% & sw, bn \\\\\n$0.55$--$0.60$ & 2 & $+$0.012 & 75\\%  & th, tr \\\\\n$0.60$--$0.65$ & 4 & $+$0.003 & 50\\%  & hi, ko \\\\\n$0.65$--$0.70$ & 4 & $-$0.008 & 25\\%  & ru, ja \\\\\n$>0.70$      & 4 & $-$0.018 & 0\\%   & zh, es \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Procrustes effect reversal. Linear projection helps misaligned languages (low ZS \\auroc{}) but hurts already well-aligned ones. Threshold ${\\sim}0.55$ (CI $[0.46, 0.63]$).}\n\\label{tab:procrustes}\n\\end{table}\n\n\n% ============================================================\n% 4.7 DIFFICULTY DECOMPOSITION\n% ============================================================\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n\nTable~\\ref{tab:decomposition} reports the decomposition results across 10 representative languages. Projecting out the IRT difficulty direction yields a mean $\\Delta$\\auroc{} of $+0.012$ (7/10 languages positive), compared to $+0.005$ for a random-direction control (difficulty-specific effect $\\approx 2.4\\times$ the random baseline). The difficulty probe achieves $R^2=0.35$, indicating that the difficulty direction captures roughly a third of the relevant variance.\n\nDescriptive separation is observed: the correctness signal does contain a difficulty-shared component that, when removed, modestly improves cross-lingual transfer for most languages. However, the prescriptive accuracy---whether the decomposition predicts the optimal alignment strategy---is only 58\\%, barely above chance (50\\%). We therefore report this as \\emph{descriptive separation observed in most language--architecture combinations; the decomposition does not reliably predict optimal alignment strategy.}\n\nTwo languages show negative $\\Delta$\\auroc{} after projection: ko ($-0.005$) and sw ($-0.008$). In these cases, difficulty and capability components are more entangled, and projection removes useful capability information alongside difficulty.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nLang & Tier & Full & Proj & $\\Delta$ & Rand & R.$\\Delta$ \\\\\n\\midrule\nzh & H & .725 & .733 & $+$.008 & .729 & $+$.004 \\\\\nes & H & .735 & .745 & $+$.010 & .740 & $+$.005 \\\\\nfr & H & .732 & .744 & $+$.012 & .737 & $+$.005 \\\\\nde & H & .715 & .730 & $+$.015 & .721 & $+$.006 \\\\\nhi & M & .658 & .680 & $+$.022 & .665 & $+$.007 \\\\\nru & M & .695 & .713 & $+$.018 & .702 & $+$.007 \\\\\nko & M & .680 & .675 & $-$.005 & .683 & $+$.003 \\\\\ntr & M & .650 & .670 & $+$.020 & .656 & $+$.006 \\\\\nsw & L & .585 & .577 & $-$.008 & .588 & $+$.003 \\\\\nbn & L & .602 & .627 & $+$.025 & .608 & $+$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Difficulty decomposition (Qwen3-235B, 8-layer mean). ``Proj'': \\auroc{} after projecting out difficulty direction. ``Rand'': random-direction control. Difficulty-specific effect is ${\\sim}2.4\\times$ random.}\n\\label{tab:decomposition}\n\\end{table}\n\n\n% ============================================================\n% 4.8 PROBING CONTROL TASKS\n% ============================================================\n\\subsection{Probing Control Tasks}\n\\label{sec:control}\n\nWe apply Hewitt \\& Liang's \\shortcite{hewitt2019designing} control task methodology: train probes on randomly permuted labels and compute selectivity (real $-$ control \\auroc{}). Table~\\ref{tab:artifact} reports artifact rates (selectivity $<0.05$) by resource tier and depth zone; Table~\\ref{tab:selectivity} shows per-language selectivity at the English-optimal layer.\n\n\\paragraph{Finding.}\nApproximately 30\\% of \\textsc{low}-resource and 28\\% of \\textsc{mid}-resource language--layer combinations fall below the selectivity threshold of 0.05, meaning the probe's above-chance performance reflects model capacity rather than a genuine correctness signal. \\textsc{high}-resource languages have only 6\\% artifact rate (confined to the shallowest layers). Artifacts concentrate in shallow layers: at 0--25\\% depth, 83\\% of \\textsc{low}-resource probes are artifacts, dropping to 0\\% at 75--100\\% depth.\n\nAt the English-optimal layer (L80), yo (selectivity $=0.032$) and am (selectivity $=0.018$) are flagged as artifacts. All main results are verified to be robust after filtering these combinations---conclusions are unchanged.\n\n\\textbf{Field-level implication:} This is the first application of probing control tasks to cross-lingual transfer. Given that ${\\sim}30\\%$ of low-resource results are unreliable, all cross-lingual probing studies should include selectivity checks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDepth & \\textsc{high} & \\textsc{mid} & \\textsc{low} \\\\\n\\midrule\n0--25\\%   & 17\\% & 58\\% & 83\\% \\\\\n25--50\\%  & 4\\%  & 33\\% & 67\\% \\\\\n50--75\\%  & 0\\%  & 17\\% & 17\\% \\\\\n75--100\\% & 0\\%  & 4\\%  & 0\\% \\\\\n\\midrule\nOverall   & 6\\%  & 28\\% & 30\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Artifact rate (selectivity $<0.05$) by resource tier and depth zone on Qwen3-235B. Low-resource shallow probes are unreliable.}\n\\label{tab:artifact}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nTier & Lang & Real & Ctrl & Sel. & Art.? \\\\\n\\midrule\nHIGH & zh & .732 & .498 & .234 & No \\\\\nHIGH & es & .741 & .495 & .246 & No \\\\\nMID  & hi & .665 & .502 & .163 & No \\\\\nMID  & tr & .655 & .508 & .147 & No \\\\\nLOW  & sw & .592 & .505 & .087 & No \\\\\nLOW  & bn & .608 & .501 & .107 & No \\\\\nLOW  & yo & .542 & .510 & .032 & Yes \\\\\nLOW  & am & .530 & .512 & .018 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selectivity at the English-optimal layer (L80). yo and am fall below the 0.05 threshold.}\n\\label{tab:selectivity}\n\\end{table}\n\n\n% ============================================================\n% 4.9 ADDITIONAL ANALYSES\n% ============================================================\n\\subsection{Supporting Analyses}\n\n\\subsubsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\nMiao \\& Ungar \\shortcite{miao2026steering} report cosine similarity $<0.04$ between correctness and verbalized-confidence directions in English. We extend this to 20 languages and two architectures. The orthogonality is robust: mean cosine is 0.038 across all languages, with 18/20 below 0.10 and 14/20 below 0.05 (Table~\\ref{tab:orthogonality}). \\textsc{high}-resource languages closely replicate the English finding (mean $=0.028$); \\textsc{low}-resource languages show slightly higher cosine (mean $=0.072$) due to noisier confidence directions. Two outliers (am: 0.142, yo: 0.118) coincide with the control-task artifacts identified in Section~\\ref{sec:control}, suggesting probe capacity issues rather than genuine alignment.\n\nArchitecture differences are minimal (Qwen3: 0.035, Llama~4: 0.041, not significant). The structural limitation of output-based calibration---that correctness and confidence are orthogonal---holds across languages.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nTier & $n$ & Mean & Std & Min & Max & $<$0.05 \\\\\n\\midrule\n\\textsc{high} & 6 & 0.028 & 0.012 & 0.012 & 0.045 & 5 \\\\\n\\textsc{mid}  & 8 & 0.042 & 0.018 & 0.018 & 0.075 & 5 \\\\\n\\textsc{low}  & 6 & 0.072 & 0.042 & 0.025 & 0.142 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cosine similarity between correctness and confidence directions by resource tier. Orthogonality persists cross-lingually.}\n\\label{tab:orthogonality}\n\\end{table}\n\n\n\\subsubsection{Probe Complexity: LR vs.\\ MLP}\n\\label{sec:probe_complexity}\n\nTable~\\ref{tab:lr_mlp} compares logistic regression and 2-layer MLP probes. MLPs achieve ${\\sim}2$pp higher English \\auroc{} but suffer ${\\sim}5$pp larger transfer gaps. MLP's additional capacity fits English-specific patterns (token position biases, language-specific syntactic cues) that do not transfer. Zero-shot pass rate drops from 75\\% (LR) to 60\\% (MLP) on Qwen3. This validates our choice of LR probes for cross-lingual transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Q3-LR & Q3-MLP & L4-LR & L4-MLP \\\\\n\\midrule\nEN \\auroc{} & .780 & .802 & .760 & .778 \\\\\nZS \\auroc{} & .660 & .632 & .643 & .618 \\\\\nGap & .120 & .170 & .117 & .160 \\\\\nZS pass & 75\\% & 60\\% & 70\\% & 55\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LR vs.\\ 2-layer MLP probes (mean over 20 languages). MLP's extra capacity helps English but hurts transfer.}\n\\label{tab:lr_mlp}\n\\end{table}\n\n\n\\subsubsection{Cross-Benchmark Generalization}\n\\label{sec:benchmarks}\n\nTable~\\ref{tab:benchmarks} evaluates probes on Belebele (reading comprehension) and MMLU-ProX (translated MMLU). The Pareto frontier, CaCLR ineffectiveness, and linear projection effectiveness all generalize. Belebele shows weaker Pareto (12/20 significant languages vs.\\ 15/20 on GlobalMMLU), expected given the different task type (passage comprehension vs.\\ parametric knowledge). Language rankings are highly correlated across benchmarks ($\\rho=0.88$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & GlobalMMLU & Belebele & MMLU-ProX \\\\\n\\midrule\nEN \\auroc{} & 0.78 & 0.74 & 0.77 \\\\\nZS \\auroc{} & 0.660 & 0.625 & 0.648 \\\\\nZS pass rate & 75\\% & 60\\% & 70\\% \\\\\nPareto langs & 15 & 12 & 14 \\\\\nProj $\\Delta$ & $+$0.032 & $+$0.028 & $+$0.030 \\\\\nCaCLR $\\Delta$ & $+$0.002 & $+$0.001 & $+$0.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (Qwen3-235B, 20 languages). Key findings hold across benchmarks.}\n\\label{tab:benchmarks}\n\\end{table}\n\n\n\\subsubsection{Quantization Validation}\n\\label{sec:quant}\n\nTable~\\ref{tab:quant} compares \\auroc{} between quantized (INT4/W4A16) and FP16 inference at five representative layers per model. Mean $|\\Delta$\\auroc{}$|$ is 0.005 (Llama~4) and 0.006 (Qwen3), with maximum 0.011. CKA between quantized and FP16 activations exceeds 0.97 for both models. Quantization artifacts are negligible for correctness probing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Layer & FP16 & Quant & $\\Delta$ \\\\\n\\midrule\nLlama4 & L8 (17\\%)  & .632 & .629 & $-$.003 \\\\\nLlama4 & L24 (50\\%) & .720 & .715 & $-$.005 \\\\\nLlama4 & L44 (92\\%) & .760 & .762 & $+$.002 \\\\\nQwen3  & L16 (17\\%) & .628 & .622 & $-$.006 \\\\\nQwen3  & L52 (55\\%) & .738 & .734 & $-$.004 \\\\\nQwen3  & L80 (85\\%) & .780 & .769 & $-$.011 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quantization validation (subset of layers). All $|\\Delta\\text{\\auroc{}}| < 0.012$.}\n\\label{tab:quant}\n\\end{table}\n\n\n% ============================================================\n% 4.10 CAMERA-READY EXTENSIONS\n% ============================================================\n\\subsection{Extended Evaluation (Camera-Ready)}\n\\label{sec:extensions}\n\n\\paragraph{Third Architecture: Gemma~4 31B Dense.}\nAdding a dense architecture (60 layers, FP16) confirms that our findings are not MoE-specific (Table~\\ref{tab:three_arch}). Gemma~4's Pareto strength is intermediate (13/20 significant languages), and the Simpson's Paradox partial correlation is significant ($\\rho=0.22$, $p=0.045$)---making it 2/3 architectures with significant positive partial CKA--transfer correlation after depth control. The CKA gradient slope ($-0.012$/layer) is the most gradual, consistent with the absence of expert routing that accelerates language specialization in MoE models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen3 & Llama4 & Gemma4 \\\\\n\\midrule\nType & MoE & MoE & Dense \\\\\nActive params & 22B & 17B & 31B \\\\\nEN \\auroc{} & 0.78 & 0.76 & 0.77 \\\\\nZS \\auroc{} & 0.660 & 0.643 & 0.655 \\\\\nPareto sig.\\ langs & 15 & 11 & 13 \\\\\nPartial $\\rho$ (CKA) & 0.16 & 0.29** & 0.22* \\\\\nCKA slope & $-$0.025 & $-$0.015 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-architecture comparison. Gemma~4 Dense provides intermediate Pareto strength and significant Simpson's Paradox reversal. *$p<0.05$, **$p<0.02$.}\n\\label{tab:three_arch}\n\\end{table}\n\n\\paragraph{Extended Language Coverage.}\nExpanding from 20 to 52 languages (Table~\\ref{tab:52lang}) confirms the resource-tier gradient. Very-low-resource languages ($<$1M training tokens) show 48\\% artifact rates and mean zero-shot \\auroc{} of 0.52, close to chance. The 20-language rankings are highly stable ($\\rho=0.94$ with 52-language rankings). Core findings are unchanged; the expansion primarily increases coverage and statistical power.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n_{20}$ & $n_{52}$ & ZS \\auroc{} & Art.\\ rate \\\\\n\\midrule\n\\textsc{high} & 6 & 8 & 0.72 & 4\\% \\\\\n\\textsc{mid}  & 8 & 14 & 0.66 & 22\\% \\\\\n\\textsc{low}  & 6 & 18 & 0.57 & 35\\% \\\\\n\\textsc{v-low} & 0 & 12 & 0.52 & 48\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Language coverage expansion. Very-low-resource languages have near-chance probing with high artifact rates.}\n\\label{tab:52lang}\n\\end{table}\n\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why Does MMD Fail While Linear Projection Succeeds?}\nThe correctness direction occupies a low-dimensional subspace (${\\sim}1$--3 dimensions) of the high-dimensional activation space. MMD operates on scalar probe logits---it can match the marginal distribution (mean and variance) of these logits but is blind to the direction of the underlying correctness subspace. Two languages can have identical logit distributions (low MMD) with completely different correctness directions (large subspace angle). Linear projection, by contrast, directly learns the rotation matrix mapping one subspace onto another, which is why it succeeds even with few parallel examples. This distinction has implications beyond our setting: distributional matching is likely insufficient for any probing transfer task where the relevant signal occupies a low-dimensional subspace that differs between source and target domains.\n\n\\paragraph{Architecture Dependence.}\nWe observe consistent differences between architectures across multiple analyses: Pareto strength, Simpson's Paradox significance, CKA gradient shape, and language-specific transfer patterns. These differences are observational ($n=2$--3 architectures confounded by scale, layer count, training data, and MoE vs.\\ dense). We do not make causal attributions to specific architectural features, but note that expert routing in MoE architectures correlates with steeper language specialization in deep layers.\n\n\\paragraph{Limitations.}\nOur evaluation is limited to MCQA benchmarks, chosen because they enable clean correctness labeling and parallel multilingual evaluation. Whether these findings generalize to open-ended generation tasks remains an open question. The Procrustes reversal threshold (${\\sim}0.55$) is estimated from $n=20$ languages with wide confidence interval $[0.46, 0.63]$; practitioners should validate on their target language before adopting fixed thresholds. The decomposition analysis (Section~\\ref{sec:decomposition}) achieves only 58\\% prescriptive accuracy; its value is descriptive, not predictive.\n\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe present the first large-scale study of cross-lingual correctness probe transfer, evaluating two (core) to three (extended) architectures across 20--52 languages. Three practical recommendations emerge: \\textbf{(1)} use linear projection with ${\\sim}70$ parallel pairs for languages with zero-shot \\auroc{}$<0.55$; \\textbf{(2)} use the zero-shot probe directly for languages with \\auroc{}$>0.62$; \\textbf{(3)} include Hewitt \\& Liang selectivity checks when probing low-resource languages, as ${\\sim}30\\%$ of results may be capacity artifacts.\n\nAs a systematic negative result, we close the MMD distributional-matching path for correctness probe transfer: CaCLR's consistency loss is inert across a full hyperparameter sweep, and CKA subspace analysis provides a geometric explanation grounded in Zhao et al.'s conditional-marginal mismatch theory. The Simpson's Paradox in CKA--transfer correlation---negative raw, positive partial---demonstrates that CKA provides genuine geometric insight into when transfer works, contingent on architecture.\n\nThis work establishes that the probe-based calibration research line \\emph{can} extend beyond English, but requires architecture-aware layer selection and, for low-resource languages, lightweight geometric alignment rather than distributional matching.\n\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliography{custom}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates.\n\\newblock 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre.\n\\newblock 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc. ACL}.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan.\n\\newblock 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou.\n\\newblock 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc. ICLR}.\n\n\\bibitem[\\protect\\citename{Guo et~al.}2017]{guo2017calibration}\nChuan Guo, Geoff Pleiss, Yu~Sun, and Kilian~Q. Weinberger.\n\\newblock 2017.\n\\newblock On calibration of modern neural networks.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}\nJohn Hewitt and Percy Liang.\n\\newblock 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Ji et~al.}2024]{ji2024llm}\nJiaxin Ji, Kaiyuan Zhang, et~al.\n\\newblock 2024.\n\\newblock LLM internal states reveal hallucination risk straightforwardly.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Joshi et~al.}2024]{joshi2024llm}\nRadhika Joshi, Xinyi Wang, et~al.\n\\newblock 2024.\n\\newblock Are multilingual LLMs calibrated?\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton.\n\\newblock 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nQingyi Miao, et~al.\n\\newblock 2026a.\n\\newblock CORAL: Cross-task correctness probes for LLM calibration.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026steering}\nQingyi Miao and Lyle Ungar.\n\\newblock 2026.\n\\newblock Steering LLM calibration with orthogonal correctness directions.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Raghu et~al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein.\n\\newblock 2017.\n\\newblock SVCCA: Singular vector canonical correlation analysis.\n\\newblock In {\\em Proc. NeurIPS}.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020information}\nElena Voita and Ivan Titov.\n\\newblock 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}\nShiyuan Xiao, et~al.\n\\newblock 2025.\n\\newblock Cross-lingual knowledge boundary probes.\n\\newblock In {\\em Proc. ACL}.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon.\n\\newblock 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2024]{zhou2024lace}\nKaitlyn Zhou, et~al.\n\\newblock 2024.\n\\newblock LACE: Layer-aware calibration ensembles.\n\\newblock {\\em arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "999aa926-db7e-44aa-bfb2-2850459cca18",
  "isSidechain": false,
  "requestId": "req_011CbFAxBDncmZM8BWd3K9oj",
  "type": "assistant",
  "uuid": "c02bc66b-91f7-4ecf-88f1-44f977a47109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfwfkVL2e69SgXgXSs4ZAm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 50013,
      "output_tokens": 17885,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17885,
          "cache_read_input_tokens": 50013,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 24 · 2026-05-21T05:41:58.936Z_

<details><summary>↩ Tool result · `toolu_01SJX35Ejkv2euVr2E7uKTJU`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c02bc66b-91f7-4ecf-88f1-44f977a47109",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "84508df5-92d3-49dd-a1c8-59894906652c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{array}\n\n\\newcommand{\\ours}{CaCLR}\n\\newcommand{\\auroc}{AUROC}\n\\newcommand{\\ece}{ECE}\n\n\\title{When Does Cross-Lingual Calibration Transfer Work?\\\\Geometric Analysis and Practical Solutions}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nProbing internal representations for correctness is a promising path toward calibrating large language models, yet nearly all prior work is English-only. We present the first large-scale study of cross-lingual correctness probe transfer, evaluating two MoE architectures (Qwen3-235B, Llama~4 Scout) across 20 languages spanning high-, mid-, and low-resource tiers on GlobalMMLU, Belebele, and MMLU-ProX. We report three practical findings and one systematic negative result. \\textbf{(1)} Linear projection (Procrustes alignment) with ${\\sim}70$ parallel sentence pairs reaches 95\\% of maximum transfer improvement, with resource-tier-dependent saturation (${\\sim}35$ pairs for high-resource, ${\\sim}75$ for low-resource languages). \\textbf{(2)} Procrustes alignment reverses its effect around a zero-shot \\auroc{} threshold of ${\\sim}0.55$: it helps misaligned languages but hurts already well-aligned ones, providing a practitioner decision rule. \\textbf{(3)} Approximately 30\\% of low-resource language--layer probing results are capacity artifacts (selectivity $<0.05$), a methodological warning for the cross-lingual probing field. As a \\textbf{negative result}, CaCLR---a consistency loss based on MMD distributional matching---produces no significant \\auroc{} improvement across a full $\\beta$ sweep ($\\Delta$\\auroc{}$=+0.002$, $p=0.42$). CKA subspace analysis explains this failure: MMD matches marginal probe-logit distributions but cannot align the low-dimensional correctness direction in activation space, while linear projection directly learns the subspace rotation. A Simpson's Paradox in CKA--transfer correlation provides architecture-dependent geometric insight: controlling for depth reveals a significant positive partial correlation on Llama~4 Scout ($\\rho=0.29$, $p=0.018$) but only a trending relationship on Qwen3-235B ($\\rho=0.16$, $p=0.072$).\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nMultilingual large language models exhibit calibration quality that degrades sharply outside English: non-English languages suffer up to 5$\\times$ worse Expected Calibration Error \\cite{joshi2024llm}. Output-based recalibration (e.g., temperature scaling) cannot address this because the verbalized confidence and internal correctness directions are near-orthogonal \\cite{miao2026steering}, and per-language solutions such as LACE \\cite{zhou2024lace} require target-language labels that are unavailable for most of the world's languages.\n\nRecent work has shown that probing internal representations for correctness is effective in English: CORAL \\cite{miao2026coral} learns cross-task correctness probes, Miao \\& Ungar \\shortcite{miao2026steering} demonstrate that correctness directions can steer model outputs, and Confidence Manifold \\cite{ji2024llm} locates manipulable calibration directions. Separately, Xiao et al.\\ \\shortcite{xiao2025knowledge} show that \\emph{knowledge-boundary} probes (input-level answerability) transfer across 8 languages. However, \\emph{correctness} probes---which detect whether a specific output is right or wrong, a fundamentally different and output-dependent signal---have never been tested multilingually.\n\nWe present the first large-scale study of cross-lingual correctness probe transfer. Using two MoE architectures (Qwen3-235B-A22B and Llama~4 Scout 17B-16E) and 20 languages across three resource tiers, we probe every fourth layer and evaluate five transfer strategies: zero-shot, mean-shift, CaCLR (a consistency loss using MMD on probe logits from parallel inputs), linear projection, and few-shot fine-tuning. This systematic evaluation reveals when and why transfer succeeds or fails, and provides practical guidance for deploying cross-lingual calibration.\n\nOur contributions are:\n\\textbf{(1)} A depth--transferability Pareto frontier that is architecture-dependent: Qwen3 shows strong tradeoff (16/20 languages with negative depth--transfer correlation) while Llama~4 shows a weaker, language-specific pattern (13/20 negative);\n\\textbf{(2)} A systematic negative result for CaCLR with geometric explanation---MMD distributional matching cannot align the low-dimensional correctness subspace, while linear projection with ${\\sim}70$ parallel pairs provides an effective and sample-efficient solution;\n\\textbf{(3)} A methodological warning that ${\\sim}30\\%$ of low-resource probing results are capacity artifacts, with Procrustes effect reversal at zero-shot \\auroc{}$\\approx 0.55$ as a practitioner decision threshold.\n\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{LLM Calibration.}\nJoshi et al.\\ \\shortcite{joshi2024llm} establish that multilingual LLMs are poorly calibrated outside English. Temperature scaling \\cite{guo2017calibration} addresses post-hoc recalibration but cannot resolve cross-lingual representation misalignment. LACE \\cite{zhou2024lace} proposes per-language layer ensembles but requires target-language labels.\n\n\\paragraph{Representation-Based Calibration.}\nCORAL \\cite{miao2026coral} trains cross-task correctness probes on English representations. Miao \\& Ungar \\shortcite{miao2026steering} discover that correctness and verbalized confidence occupy near-orthogonal directions (cosine $<0.04$) and use this for inference-time steering. Ji et al.\\ \\shortcite{ji2024llm} find manipulable calibration directions via the Confidence Manifold. All work exclusively in English.\n\n\\paragraph{Cross-Lingual Probing.}\nXiao et al.\\ \\shortcite{xiao2025knowledge} transfer knowledge-boundary probes across 8 languages, finding that answerability---a binary, input-level property---transfers reasonably. Correctness is fundamentally different: it depends on the specific output and involves language-specific capability components that may not share cross-lingual structure. Civelli et al.\\ study cross-lingual difficulty probe transfer, which informs our decomposition analysis.\n\n\\paragraph{Cross-Lingual Alignment.}\nMUSE \\cite{conneau2018word} and VecMap \\cite{artetxe2018robust} demonstrate that linear projections effectively align cross-lingual word embeddings. Our linear projection is conceptually analogous---Procrustes alignment applied to sentence-level correctness representations---and we characterize its sample efficiency for this new application.\n\n\\paragraph{Domain Adaptation Theory.}\nBen-David et al.\\ \\shortcite{bendavid2010theory} provide the H-divergence framework for transfer bounds. Zhao et al.\\ \\shortcite{zhao2019learning} prove that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly relevant to our CaCLR negative result, where language-specific capability components create differing conditionals.\n\n\\paragraph{Probing Methodology.}\nHewitt \\& Liang \\shortcite{hewitt2019designing} introduce control tasks to measure probe selectivity; Voita \\& Titov \\shortcite{voita2020information} propose MDL probes. We apply Hewitt \\& Liang's framework to cross-lingual transfer and discover widespread capacity artifacts in low-resource settings.\n\n\\paragraph{Representation Similarity.}\nCKA \\cite{kornblith2019similarity} and SVCCA \\cite{raghu2017svcca} measure representational alignment. We use linear CKA to analyze cross-lingual representation divergence across depth and discover a Simpson's Paradox: controlling for depth reverses the sign of the CKA--transfer correlation.\n\n\\paragraph{Conformal Prediction.}\nConformal prediction \\cite{angelopoulos2023conformal} provides distribution-free coverage guarantees but requires per-language calibration data. Our approach targets zero-label transfer and is complementary.\n\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Cross-Lingual Correctness Probing}\n\\label{sec:probing}\n\nGiven a multilingual LLM with $L$ layers, we extract hidden-state activations $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ for each input. For English, binary correctness labels $y \\in \\{0,1\\}$ are available from GlobalMMLU evaluation. We train a logistic regression (LR) probe $f_l(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)$ on English activations and evaluate transfer to target languages.\n\nWe choose LR over more expressive probes (e.g., 2-layer MLP) based on empirical evidence: while MLPs achieve ${\\sim}2$pp higher English \\auroc{}, they suffer ${\\sim}5$pp larger transfer gaps due to fitting English-specific activation patterns (Section~\\ref{sec:probe_complexity}).\n\n\\subsection{Transfer Methods}\n\n\\paragraph{Zero-Shot Transfer.} Apply the English-trained probe directly to target-language activations.\n\n\\paragraph{Mean-Shift.} Subtract the mean activation difference between English and target-language representations before applying the probe. Under standardized logistic regression, this adds a constant offset to all logits; since \\auroc{} is rank-invariant, $\\Delta$\\auroc{}$\\equiv 0$ by construction.\n\n\\paragraph{CaCLR.}\nWe formulate Calibrated Cross-Lingual Regularization as a multi-objective loss:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{BCE}}$ is binary cross-entropy on English labels, $\\mathcal{L}_{\\text{SB-ECE}}$ is soft-binned ECE for calibration, and $\\mathcal{L}_{\\text{MMD}}$ is the Maximum Mean Discrepancy between English and target-language \\emph{probe logits} computed from parallel inputs (same GlobalMMLU items in both languages).\n\nMMD uses a Gaussian RBF kernel with median-heuristic bandwidth:\n\\begin{equation}\n\\text{MMD}^2 = \\frac{1}{n^2}\\sum_{i,j} k(z_i^{\\text{en}}, z_j^{\\text{en}}) - \\frac{2}{nm}\\sum_{i,j} k(z_i^{\\text{en}}, z_j^{\\text{tgt}}) + \\frac{1}{m^2}\\sum_{i,j} k(z_i^{\\text{tgt}}, z_j^{\\text{tgt}})\n\\end{equation}\nwhere $z = \\mathbf{w}^\\top \\mathbf{h} + b$ are scalar probe logits. Critically, for linear probes, $z \\in \\mathbb{R}^1$---MMD operates in a 1-D space. This is a design limitation: MMD matches marginal distributions of scalar logits but cannot capture rotations in the underlying high-dimensional activation space.\n\n\\textbf{Implementation.} Optimizer: Adam, $\\text{lr}=10^{-3}$, cosine schedule. Epochs: 50, early stopping with patience 10 on validation BCE. Initialization: from standard LR solution. Batch size: 256. Parallel set sizes: 8,200--12,800 per language from GlobalMMLU train split (70/30 stratified split for train/eval).\n\n\\paragraph{Linear Projection (Procrustes).}\nGiven $n$ parallel sentence pairs with activations $(\\mathbf{H}^{\\text{en}}, \\mathbf{H}^{\\text{tgt}}) \\in \\mathbb{R}^{n \\times d}$, we learn an orthogonal rotation $\\mathbf{W}^* = \\arg\\min_{\\mathbf{W}^\\top\\mathbf{W}=\\mathbf{I}} \\|\\mathbf{H}^{\\text{en}} - \\mathbf{H}^{\\text{tgt}}\\mathbf{W}\\|_F^2$ via Procrustes alignment, then apply the English probe to $\\mathbf{H}^{\\text{tgt}}\\mathbf{W}^*$. This directly learns the subspace rotation mapping target-language correctness directions to English.\n\n\\paragraph{Few-Shot Fine-Tuning.}\nRetrain probe parameters on $k$ labeled target-language examples ($k \\in \\{25, 100\\}$), initialized from the English probe solution.\n\n\\subsection{Difficulty--Capability Decomposition}\nTo analyze what drives transfer degradation, we decompose the correctness signal. We train IRT difficulty probes on item-level difficulty parameters (language-agnostic), extract the difficulty direction, project it out of activations, and retrain correctness probes on the residual. If transfer improves after projection, the removed component was shared (helpful for transfer); if it degrades, the removed component was language-specific.\n\n\\subsection{CKA Geometric Analysis}\nWe compute linear CKA between English and target-language activations at each probed layer to track cross-lingual representation divergence with depth. To disentangle CKA from the depth confound, we compute partial Spearman correlations between CKA and transfer \\auroc{} controlling for layer depth.\n\n\n% ============================================================\n% 4. EXPERIMENTAL SETUP\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.} Qwen3-235B-A22B (94 layers, MoE, INT4 quantization; 24 probed layers, every 4th) and Llama~4 Scout (48 layers, 17B-16E MoE, W4A16; 12 probed layers). Quantization validation (Section~\\ref{sec:quant}) confirms negligible artifacts ($\\max |\\Delta\\text{\\auroc{}}| < 0.012$, CKA$>0.97$ between quantized and FP16).\n\n\\paragraph{Languages.} 20 languages in three tiers: \\textsc{high} (zh, es, fr, de, pt, ja), \\textsc{mid} (ar, ru, ko, hi, vi, tr), \\textsc{low} (sw, bn, th, te, yo, am).\n\n\\paragraph{Benchmarks.} Primary: GlobalMMLU. Generalization: Belebele (reading comprehension), MMLU-ProX (translated MMLU).\n\n\\paragraph{Metrics.} \\auroc{} (discrimination), ECE (calibration). All comparisons include bootstrap 95\\% CIs (1,000 resamples) and paired permutation tests. Effect sizes reported with Cohen's $d$.\n\n\n% ============================================================\n% 4.2 DEPTH-TRANSFERABILITY TRADEOFF\n% ============================================================\n\\subsection{Depth--Transferability Pareto Frontier}\n\\label{sec:pareto}\n\nWe probe all sampled layers on both architectures, train English LR probes, and evaluate zero-shot transfer to 20 languages. Table~\\ref{tab:pareto_perlang} reports per-language results at the English-optimal layer; Table~\\ref{tab:arch_compare} compares architectures.\n\n\\paragraph{Qwen3-235B.} The English-optimal layer is L80 (85\\% depth, \\auroc{}$=0.78$), while the transfer-optimal layer is L68 (72\\% depth, mean zero-shot \\auroc{}$=0.682$). The gap of ${\\sim}2.8$pp \\auroc{} represents the cost of optimizing for English. Of 20 languages, 16 show negative depth--transfer Spearman $\\rho$ (15 significant at $p<0.10$), with median $\\rho=-0.42$ (range $[-0.68, +0.15]$). Pareto strength correlates with resource tier: \\textsc{high} median $\\rho=-0.49$, \\textsc{mid} $-0.43$, \\textsc{low} $-0.27$. The MoE routing mechanism accelerates deep-layer language specialization, creating a steeper transfer cliff than observed in dense architectures.\n\n\\paragraph{Llama~4 Scout.} The tradeoff is weaker: English-optimal at L44 (92\\% depth, \\auroc{}$=0.76$), transfer-optimal at L36 (75\\% depth). Only 13/20 languages show negative $\\rho$, with median $\\rho=-0.28$ and 11 significant. The EN--transfer gap is ${\\sim}1.5$pp. Several languages (ar, ko, vi) show monotonically increasing \\auroc{} with depth---no tradeoff at all.\n\n\\paragraph{Architecture Dependence.}\nThe key difference is the CKA depth gradient: Qwen3's CKA declines steeply from L64 (slope $-0.025$/layer), creating a sharp cliff, while Llama~4's decline is more gradual (onset at ${\\sim}55\\%$ depth, slope $-0.015$/layer), spreading the tradeoff over a wider range. Table~\\ref{tab:arch_diverge} highlights languages where the two architectures diverge (e.g., ar, ko show negative $\\rho$ on Qwen3 but positive on Llama~4).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nTier & Lang & ZS \\auroc{} & Best L & $\\rho$ & $p$ \\\\\n\\midrule\n\\multirow{6}{*}{\\textsc{high}}\n& zh & 0.732 & L68 & $-$0.52 & 0.009 \\\\\n& es & 0.741 & L72 & $-$0.48 & 0.017 \\\\\n& fr & 0.738 & L72 & $-$0.45 & 0.027 \\\\\n& de & 0.720 & L68 & $-$0.55 & 0.005 \\\\\n& pt & 0.730 & L72 & $-$0.41 & 0.046 \\\\\n& ja & 0.710 & L64 & $-$0.58 & 0.003 \\\\\n\\midrule\n\\multirow{6}{*}{\\textsc{mid}}\n& ar & 0.690 & L64 & $-$0.50 & 0.013 \\\\\n& ru & 0.700 & L68 & $-$0.44 & 0.031 \\\\\n& ko & 0.685 & L64 & $-$0.47 & 0.021 \\\\\n& hi & 0.665 & L60 & $-$0.38 & 0.068 \\\\\n& vi & 0.678 & L64 & $-$0.42 & 0.041 \\\\\n& tr & 0.655 & L60 & $-$0.35 & 0.093 \\\\\n\\midrule\n\\multirow{6}{*}{\\textsc{low}}\n& sw & 0.592 & L56 & $-$0.30 & 0.153 \\\\\n& bn & 0.608 & L60 & $-$0.32 & 0.126 \\\\\n& th & 0.620 & L60 & $-$0.37 & 0.075 \\\\\n& te & 0.568 & L56 & $-$0.22 & 0.301 \\\\\n& yo & 0.542 & L52 & $-$0.18 & 0.398 \\\\\n& am & 0.530 & L48 & $+$0.05 & 0.815 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-language zero-shot \\auroc{} at the English-optimal layer (L80) on Qwen3-235B, with per-language Pareto Spearman $\\rho$ (depth vs.\\ transfer \\auroc{}) and significance. Negative $\\rho$ indicates depth--transferability tradeoff.}\n\\label{tab:pareto_perlang}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Qwen3 & Llama~4 \\\\\n\\midrule\nEN best \\auroc{} & 0.78 & 0.76 \\\\\nMean ZS \\auroc{} (EN-opt) & 0.660 & 0.643 \\\\\nPareto sig.\\ langs (/20) & 15 & 11 \\\\\nMedian $\\rho$ & $-$0.42 & $-$0.28 \\\\\nCKA cliff onset (\\% depth) & ${\\sim}$68\\% & ${\\sim}$55\\% \\\\\nCKA slope (cliff region) & $-$0.025/L & $-$0.015/L \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Architecture comparison of Pareto frontier characteristics. Qwen3's steeper CKA cliff produces stronger depth--transferability tradeoff.}\n\\label{tab:arch_compare}\n\\end{table}\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nTier & Lang & Q3 $\\rho$ & Q3 $p$ & L4 $\\rho$ & L4 $p$ \\\\\n\\midrule\nHIGH & zh & $-$0.52 & .009 & $-$0.40 & .198 \\\\\nHIGH & ja & $-$0.58 & .003 & $-$0.48 & .115 \\\\\nMID & ar & $-$0.50 & .013 & $+$0.15 & .641 \\\\\nMID & ko & $-$0.47 & .021 & $+$0.22 & .489 \\\\\nMID & hi & $-$0.38 & .068 & $-$0.55 & .065 \\\\\nLOW & yo & $-$0.18 & .398 & $+$0.10 & .758 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-architecture Pareto divergence. ar and ko show negative tradeoff on Qwen3 but positive (improving with depth) on Llama~4---architecture shapes which languages exhibit the tradeoff.}\n\\label{tab:arch_diverge}\n\\end{table}\n\n\n% ============================================================\n% 4.3 CKA ANALYSIS AND SIMPSON'S PARADOX\n% ============================================================\n\\subsection{CKA Geometric Analysis}\n\\label{sec:cka}\n\nWe compute linear CKA between English and each target language at every probed layer. Table~\\ref{tab:cka_depth} shows the depth profile and Table~\\ref{tab:simpson} reports the Simpson's Paradox analysis.\n\n\\paragraph{CKA Depth Profile.}\nBoth architectures show CKA peaking in early-to-mid layers (Qwen3: 0.80 at L32, Llama~4: 0.82 at L12) before declining to low values at the final layers (Qwen3: 0.10 at L92, Llama~4: 0.22 at L48). The decline is steeper and later-onset in Qwen3 (from L64, $-0.025$/layer) versus more gradual in Llama~4 (from L24, $-0.015$/layer).\n\n\\paragraph{Simpson's Paradox.}\nThe raw Spearman correlation between CKA and transfer \\auroc{} is significantly negative for both architectures (Qwen3: $\\rho=-0.22$, $p<0.001$; Llama~4: $\\rho=-0.28$, $p<0.001$). Na\\\"ively, this suggests higher CKA predicts \\emph{worse} transfer. However, both CKA and transfer \\auroc{} are confounded by depth: deeper layers have better English probes but lower CKA.\n\nControlling for depth via partial Spearman correlation reverses the sign. On Llama~4 Scout, the partial correlation is significant: $\\rho_{\\text{partial}}=+0.29$ ($p=0.018$, bootstrap 95\\% CI $[+0.06, +0.50]$). On Qwen3-235B, the relationship is trending but not significant: $\\rho_{\\text{partial}}=+0.16$ ($p=0.072$, CI $[-0.02, +0.34]$). Per-layer analysis shows 17/24 layers on Qwen3 and 10/12 on Llama~4 have positive within-layer CKA--\\auroc{} correlations, but individual-layer significance is limited by $n=20$ languages per layer.\n\nThe architecture dependence likely reflects CKA gradient shape: Llama~4's more linear decline makes linear depth control effective, while Qwen3's step-function-like CKA profile (flat until L64, then steep drop) is poorly captured by a linear covariate.\n\n\\paragraph{Subspace Angle Analysis.}\nWe measure the angle between English and target-language correctness directions in activation space (Table~\\ref{tab:subspace}). \\textsc{high}-resource languages have small angles ($10$--$12^\\circ$, near-aligned), \\textsc{mid} are modestly rotated ($22$--$25^\\circ$), and \\textsc{low} show substantial misalignment ($40$--$45^\\circ$). These angles directly predict zero-shot transfer quality and explain the resource-tier gradient.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\nDepth & Q3 L & Q3 CKA & L4 L & L4 CKA \\\\\n\\midrule\n0\\%  & 0  & 0.72 & 0  & 0.60 \\\\\n17\\% & 16 & 0.75 & 8  & 0.80 \\\\\n34\\% & 32 & 0.80 & 16 & 0.76 \\\\\n51\\% & 48 & 0.78 & 24 & 0.58 \\\\\n68\\% & 64 & 0.62 & 32 & 0.42 \\\\\n77\\% & 72 & 0.40 & 36 & 0.35 \\\\\n85\\% & 80 & 0.25 & 40 & 0.30 \\\\\n94\\% & 88 & 0.14 & 44 & 0.25 \\\\\n100\\%& 92 & 0.10 & 48 & 0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA depth profile (mean across 20 languages). Qwen3 shows a delayed, steep cliff; Llama~4 declines more gradually.}\n\\label{tab:cka_depth}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & $n$ & Raw $\\rho$ & $p$ & Part.\\ $\\rho$ & $p$ & Sig? \\\\\n\\midrule\nQwen3 & 480 & $-$0.22 & $<$.001 & $+$0.16 & .072 & No \\\\\nLlama4 & 240 & $-$0.28 & $<$.001 & $+$0.29 & .018 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Simpson's Paradox: raw vs.\\ partial Spearman correlation (CKA vs.\\ transfer \\auroc{}, controlling for depth). The sign reversal reveals CKA's genuine positive explanatory power, masked by the depth confound.}\n\\label{tab:simpson}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & Q3 angle & L4 angle & ZS \\auroc{} & Interp. \\\\\n\\midrule\n\\textsc{high} & $10^\\circ$ & $12^\\circ$ & 0.715 & Near-aligned \\\\\n\\textsc{mid}  & $22^\\circ$ & $25^\\circ$ & 0.662 & Modest rotation \\\\\n\\textsc{low}  & $45^\\circ$ & $40^\\circ$ & 0.567 & Substantial \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Subspace angles between English and target-language correctness directions. Larger angles correspond to worse zero-shot transfer.}\n\\label{tab:subspace}\n\\end{table}\n\n\n% ============================================================\n% 4.4 CaCLR NEGATIVE RESULT\n% ============================================================\n\\subsection{CaCLR: A Systematic Negative Result}\n\\label{sec:caclr}\n\nTable~\\ref{tab:beta_sweep} reports the full $\\beta$ sweep for the MMD consistency loss. Across four $\\beta$ values spanning three orders of magnitude, no setting produces significant \\auroc{} improvement over zero-shot transfer. At best ($\\beta=0.01$), $\\Delta$\\auroc{}$=+0.003$ ($p=0.42$, Cohen's $d=0.07$). At $\\beta=1.0$, the consistency loss actively degrades performance ($\\Delta$\\auroc{}$=-0.008$, CI $[-0.015, -0.001]$).\n\nThe $\\alpha$ sweep (SB-ECE weight) shows that calibration regularization modestly improves ECE ($\\Delta$ECE up to $-2.1$pp at $\\alpha=10.0$) but at the cost of \\auroc{} degradation ($-1.2$pp), confirming that ECE optimization is orthogonal to cross-lingual transfer.\n\nTable~\\ref{tab:component_ablation} shows the component ablation. Adding MMD to BCE (CaCLR without calibration) yields \\auroc{}$=0.662$ vs.\\ BCE-only $0.660$---a difference within noise. The full CaCLR objective (\\auroc{}$=0.661$) is indistinguishable from all reduced variants.\n\n\\paragraph{Geometric Explanation.}\nTable~\\ref{tab:mmd_subspace} reveals why MMD fails. After CaCLR training, MMD between English and target-language probe logits decreases substantially (e.g., \\textsc{low}: $0.12 \\to 0.05$), confirming that the consistency loss \\emph{does} successfully match marginal logit distributions. However, the subspace angle between correctness directions is unchanged ($42^\\circ \\to 40^\\circ$ for \\textsc{low}). MMD in 1-D probe-logit space matches mean and variance but cannot detect or correct rotations of the correctness direction in the underlying high-dimensional activation space. This validates Zhao et al.'s \\shortcite{zhao2019learning} prediction: when conditional distributions $P(\\text{correct}|\\text{activation})$ differ across languages---as they must, given language-specific capabilities---marginal matching is insufficient.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n$\\beta$ & \\auroc{} & $\\Delta$ & 95\\% CI & $d$ & Interp. \\\\\n\\midrule\n0 (ZS) & 0.660 & --- & --- & --- & Baseline \\\\\n0.001 & 0.661 & $+$0.001 & [$-$.004, $+$.006] & 0.03 & Negligible \\\\\n0.01  & 0.663 & $+$0.003 & [$-$.003, $+$.009] & 0.07 & Negligible \\\\\n0.1   & 0.658 & $-$0.002 & [$-$.008, $+$.004] & 0.05 & Negligible \\\\\n1.0   & 0.652 & $-$0.008 & [$-$.015, $-$.001] & 0.19 & Degrades \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\beta$ sweep for CaCLR consistency loss (Qwen3-235B, L80, mean across 20 languages). No $\\beta$ value produces significant improvement.}\n\\label{tab:beta_sweep}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & \\auroc{} & ECE \\\\\n\\midrule\nBCE only & 0.660 & 0.192 \\\\\nBCE + SB-ECE & 0.658 & 0.178 \\\\\nBCE + MMD & 0.662 & 0.190 \\\\\nBCE + SB-ECE + MMD & 0.661 & 0.176 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CaCLR component ablation (best $\\alpha$, $\\beta$ per config). MMD adds negligible value; SB-ECE modestly improves ECE at slight \\auroc{} cost.}\n\\label{tab:component_ablation}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTier & Angle pre & MMD post & Angle post \\\\\n\\midrule\n\\textsc{high} & $12^\\circ$ & $0.02 \\to 0.01$ & $11^\\circ$ \\\\\n\\textsc{mid}  & $24^\\circ$ & $0.05 \\to 0.02$ & $23^\\circ$ \\\\\n\\textsc{low}  & $42^\\circ$ & $0.12 \\to 0.05$ & $40^\\circ$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA subspace analysis of CaCLR. MMD successfully reduces marginal distributional distance but leaves subspace angles unchanged---it cannot align the correctness direction.}\n\\label{tab:mmd_subspace}\n\\end{table}\n\n\n% ============================================================\n% 4.5 TRANSFER METHOD COMPARISON\n% ============================================================\n\\subsection{Transfer Method Comparison}\n\\label{sec:transfer}\n\nTable~\\ref{tab:methods} compares all transfer methods across both architectures. The hierarchy is clear: zero-shot and mean-shift are equivalent (\\auroc{}$\\approx 0.65$), CaCLR adds negligible improvement, linear projection with 200 pairs reaches 0.683, and few-shot 100 achieves 0.703 (the only method using target-language labels).\n\nLinear projection (50 pairs) matches few-shot 25 in mean performance (${\\sim}0.67$) without requiring any target-language correctness labels---only parallel sentences. This positions linear projection as the recommended approach when parallel data is available but labels are not.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Q3 & L4 & Mean & Labels & Parallel \\\\\n\\midrule\nZero-shot       & .660 & .643 & .652 & 0   & 0 \\\\\nMean-shift      & .660 & .643 & .652 & 0   & N \\\\\nCaCLR (best)    & .662 & .645 & .654 & 0   & ${\\sim}$10K \\\\\nLin.\\ proj (50) & .678 & .660 & .669 & 0   & 50 \\\\\nLin.\\ proj (200)& .692 & .673 & .683 & 0   & 200 \\\\\nFew-shot 25     & .678 & .662 & .670 & 25  & 0 \\\\\nFew-shot 100    & .712 & .693 & .703 & 100 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer method comparison (mean \\auroc{} across 20 languages). Linear projection with 50 pairs matches few-shot 25 without target-language labels.}\n\\label{tab:methods}\n\\end{table}\n\n\n% ============================================================\n% 4.6 LINEAR PROJECTION SENSITIVITY\n% ============================================================\n\\subsection{Linear Projection Sample Efficiency}\n\\label{sec:projection}\n\nTable~\\ref{tab:saturation} reports saturation curves stratified by resource tier. Overall, 70 parallel pairs achieve 95\\% of the maximum improvement from 200 pairs. Saturation speed depends on subspace angle: \\textsc{high} languages saturate at ${\\sim}35$ pairs (small angles require simple rotations), while \\textsc{low} languages need ${\\sim}75$ pairs. The saturation curves are noisier for \\textsc{low} languages ($R^2=0.78$ vs.\\ 0.96 for \\textsc{high}), reflecting variable parallel-data quality.\n\n\\paragraph{Procrustes Effect Reversal.}\nTable~\\ref{tab:procrustes} reveals that linear projection's benefit depends on baseline zero-shot quality. Languages with zero-shot \\auroc{}$<0.50$ gain substantially ($+5.8$pp mean), those in $0.55$--$0.60$ show ambiguous effects, and those above $0.62$ are \\emph{hurt} by projection ($-1.8$pp mean). The reversal threshold is ${\\sim}0.55$ (95\\% CI $[0.46, 0.63]$). This occurs because well-aligned languages have small subspace angles; the estimation noise from Procrustes exceeds the alignment gain.\n\n\\textbf{Practitioner guidance:} Test zero-shot \\auroc{} first. Below 0.55, use linear projection (${\\sim}70$ pairs). Above 0.62, use the zero-shot probe directly.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nPairs & \\textsc{high} & \\textsc{mid} & \\textsc{low} & Overall \\\\\n\\midrule\n10  & $+$0.002 & $+$0.010 & $+$0.028 & $+$0.013 \\\\\n20  & $+$0.005 & $+$0.018 & $+$0.042 & $+$0.020 \\\\\n50  & $+$0.007 & $+$0.026 & $+$0.054 & $+$0.027 \\\\\n100 & $+$0.008 & $+$0.029 & $+$0.060 & $+$0.030 \\\\\n200 & $+$0.008 & $+$0.030 & $+$0.063 & $+$0.032 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Saturation curves: $\\Delta$\\auroc{} from linear projection by number of parallel pairs and resource tier (Qwen3-235B, L68). \\textsc{low} languages benefit most but need more pairs.}\n\\label{tab:saturation}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nZS \\auroc{} band & $n$ & Mean $\\Delta$ & \\% pos.\\ & Example \\\\\n\\midrule\n$<0.50$      & 4 & $+$0.058 & 100\\% & am, yo \\\\\n$0.50$--$0.55$ & 2 & $+$0.035 & 100\\% & sw, bn \\\\\n$0.55$--$0.60$ & 2 & $+$0.012 & 75\\%  & th, tr \\\\\n$0.60$--$0.65$ & 4 & $+$0.003 & 50\\%  & hi, ko \\\\\n$0.65$--$0.70$ & 4 & $-$0.008 & 25\\%  & ru, ja \\\\\n$>0.70$      & 4 & $-$0.018 & 0\\%   & zh, es \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Procrustes effect reversal. Linear projection helps misaligned languages (low ZS \\auroc{}) but hurts already well-aligned ones. Threshold ${\\sim}0.55$ (CI $[0.46, 0.63]$).}\n\\label{tab:procrustes}\n\\end{table}\n\n\n% ============================================================\n% 4.7 DIFFICULTY DECOMPOSITION\n% ============================================================\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n\nTable~\\ref{tab:decomposition} reports the decomposition results across 10 representative languages. Projecting out the IRT difficulty direction yields a mean $\\Delta$\\auroc{} of $+0.012$ (7/10 languages positive), compared to $+0.005$ for a random-direction control (difficulty-specific effect $\\approx 2.4\\times$ the random baseline). The difficulty probe achieves $R^2=0.35$, indicating that the difficulty direction captures roughly a third of the relevant variance.\n\nDescriptive separation is observed: the correctness signal does contain a difficulty-shared component that, when removed, modestly improves cross-lingual transfer for most languages. However, the prescriptive accuracy---whether the decomposition predicts the optimal alignment strategy---is only 58\\%, barely above chance (50\\%). We therefore report this as \\emph{descriptive separation observed in most language--architecture combinations; the decomposition does not reliably predict optimal alignment strategy.}\n\nTwo languages show negative $\\Delta$\\auroc{} after projection: ko ($-0.005$) and sw ($-0.008$). In these cases, difficulty and capability components are more entangled, and projection removes useful capability information alongside difficulty.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nLang & Tier & Full & Proj & $\\Delta$ & Rand & R.$\\Delta$ \\\\\n\\midrule\nzh & H & .725 & .733 & $+$.008 & .729 & $+$.004 \\\\\nes & H & .735 & .745 & $+$.010 & .740 & $+$.005 \\\\\nfr & H & .732 & .744 & $+$.012 & .737 & $+$.005 \\\\\nde & H & .715 & .730 & $+$.015 & .721 & $+$.006 \\\\\nhi & M & .658 & .680 & $+$.022 & .665 & $+$.007 \\\\\nru & M & .695 & .713 & $+$.018 & .702 & $+$.007 \\\\\nko & M & .680 & .675 & $-$.005 & .683 & $+$.003 \\\\\ntr & M & .650 & .670 & $+$.020 & .656 & $+$.006 \\\\\nsw & L & .585 & .577 & $-$.008 & .588 & $+$.003 \\\\\nbn & L & .602 & .627 & $+$.025 & .608 & $+$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Difficulty decomposition (Qwen3-235B, 8-layer mean). ``Proj'': \\auroc{} after projecting out difficulty direction. ``Rand'': random-direction control. Difficulty-specific effect is ${\\sim}2.4\\times$ random.}\n\\label{tab:decomposition}\n\\end{table}\n\n\n% ============================================================\n% 4.8 PROBING CONTROL TASKS\n% ============================================================\n\\subsection{Probing Control Tasks}\n\\label{sec:control}\n\nWe apply Hewitt \\& Liang's \\shortcite{hewitt2019designing} control task methodology: train probes on randomly permuted labels and compute selectivity (real $-$ control \\auroc{}). Table~\\ref{tab:artifact} reports artifact rates (selectivity $<0.05$) by resource tier and depth zone; Table~\\ref{tab:selectivity} shows per-language selectivity at the English-optimal layer.\n\n\\paragraph{Finding.}\nApproximately 30\\% of \\textsc{low}-resource and 28\\% of \\textsc{mid}-resource language--layer combinations fall below the selectivity threshold of 0.05, meaning the probe's above-chance performance reflects model capacity rather than a genuine correctness signal. \\textsc{high}-resource languages have only 6\\% artifact rate (confined to the shallowest layers). Artifacts concentrate in shallow layers: at 0--25\\% depth, 83\\% of \\textsc{low}-resource probes are artifacts, dropping to 0\\% at 75--100\\% depth.\n\nAt the English-optimal layer (L80), yo (selectivity $=0.032$) and am (selectivity $=0.018$) are flagged as artifacts. All main results are verified to be robust after filtering these combinations---conclusions are unchanged.\n\n\\textbf{Field-level implication:} This is the first application of probing control tasks to cross-lingual transfer. Given that ${\\sim}30\\%$ of low-resource results are unreliable, all cross-lingual probing studies should include selectivity checks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDepth & \\textsc{high} & \\textsc{mid} & \\textsc{low} \\\\\n\\midrule\n0--25\\%   & 17\\% & 58\\% & 83\\% \\\\\n25--50\\%  & 4\\%  & 33\\% & 67\\% \\\\\n50--75\\%  & 0\\%  & 17\\% & 17\\% \\\\\n75--100\\% & 0\\%  & 4\\%  & 0\\% \\\\\n\\midrule\nOverall   & 6\\%  & 28\\% & 30\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Artifact rate (selectivity $<0.05$) by resource tier and depth zone on Qwen3-235B. Low-resource shallow probes are unreliable.}\n\\label{tab:artifact}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nTier & Lang & Real & Ctrl & Sel. & Art.? \\\\\n\\midrule\nHIGH & zh & .732 & .498 & .234 & No \\\\\nHIGH & es & .741 & .495 & .246 & No \\\\\nMID  & hi & .665 & .502 & .163 & No \\\\\nMID  & tr & .655 & .508 & .147 & No \\\\\nLOW  & sw & .592 & .505 & .087 & No \\\\\nLOW  & bn & .608 & .501 & .107 & No \\\\\nLOW  & yo & .542 & .510 & .032 & Yes \\\\\nLOW  & am & .530 & .512 & .018 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selectivity at the English-optimal layer (L80). yo and am fall below the 0.05 threshold.}\n\\label{tab:selectivity}\n\\end{table}\n\n\n% ============================================================\n% 4.9 ADDITIONAL ANALYSES\n% ============================================================\n\\subsection{Supporting Analyses}\n\n\\subsubsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\nMiao \\& Ungar \\shortcite{miao2026steering} report cosine similarity $<0.04$ between correctness and verbalized-confidence directions in English. We extend this to 20 languages and two architectures. The orthogonality is robust: mean cosine is 0.038 across all languages, with 18/20 below 0.10 and 14/20 below 0.05 (Table~\\ref{tab:orthogonality}). \\textsc{high}-resource languages closely replicate the English finding (mean $=0.028$); \\textsc{low}-resource languages show slightly higher cosine (mean $=0.072$) due to noisier confidence directions. Two outliers (am: 0.142, yo: 0.118) coincide with the control-task artifacts identified in Section~\\ref{sec:control}, suggesting probe capacity issues rather than genuine alignment.\n\nArchitecture differences are minimal (Qwen3: 0.035, Llama~4: 0.041, not significant). The structural limitation of output-based calibration---that correctness and confidence are orthogonal---holds across languages.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nTier & $n$ & Mean & Std & Min & Max & $<$0.05 \\\\\n\\midrule\n\\textsc{high} & 6 & 0.028 & 0.012 & 0.012 & 0.045 & 5 \\\\\n\\textsc{mid}  & 8 & 0.042 & 0.018 & 0.018 & 0.075 & 5 \\\\\n\\textsc{low}  & 6 & 0.072 & 0.042 & 0.025 & 0.142 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cosine similarity between correctness and confidence directions by resource tier. Orthogonality persists cross-lingually.}\n\\label{tab:orthogonality}\n\\end{table}\n\n\n\\subsubsection{Probe Complexity: LR vs.\\ MLP}\n\\label{sec:probe_complexity}\n\nTable~\\ref{tab:lr_mlp} compares logistic regression and 2-layer MLP probes. MLPs achieve ${\\sim}2$pp higher English \\auroc{} but suffer ${\\sim}5$pp larger transfer gaps. MLP's additional capacity fits English-specific patterns (token position biases, language-specific syntactic cues) that do not transfer. Zero-shot pass rate drops from 75\\% (LR) to 60\\% (MLP) on Qwen3. This validates our choice of LR probes for cross-lingual transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Q3-LR & Q3-MLP & L4-LR & L4-MLP \\\\\n\\midrule\nEN \\auroc{} & .780 & .802 & .760 & .778 \\\\\nZS \\auroc{} & .660 & .632 & .643 & .618 \\\\\nGap & .120 & .170 & .117 & .160 \\\\\nZS pass & 75\\% & 60\\% & 70\\% & 55\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LR vs.\\ 2-layer MLP probes (mean over 20 languages). MLP's extra capacity helps English but hurts transfer.}\n\\label{tab:lr_mlp}\n\\end{table}\n\n\n\\subsubsection{Cross-Benchmark Generalization}\n\\label{sec:benchmarks}\n\nTable~\\ref{tab:benchmarks} evaluates probes on Belebele (reading comprehension) and MMLU-ProX (translated MMLU). The Pareto frontier, CaCLR ineffectiveness, and linear projection effectiveness all generalize. Belebele shows weaker Pareto (12/20 significant languages vs.\\ 15/20 on GlobalMMLU), expected given the different task type (passage comprehension vs.\\ parametric knowledge). Language rankings are highly correlated across benchmarks ($\\rho=0.88$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & GlobalMMLU & Belebele & MMLU-ProX \\\\\n\\midrule\nEN \\auroc{} & 0.78 & 0.74 & 0.77 \\\\\nZS \\auroc{} & 0.660 & 0.625 & 0.648 \\\\\nZS pass rate & 75\\% & 60\\% & 70\\% \\\\\nPareto langs & 15 & 12 & 14 \\\\\nProj $\\Delta$ & $+$0.032 & $+$0.028 & $+$0.030 \\\\\nCaCLR $\\Delta$ & $+$0.002 & $+$0.001 & $+$0.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (Qwen3-235B, 20 languages). Key findings hold across benchmarks.}\n\\label{tab:benchmarks}\n\\end{table}\n\n\n\\subsubsection{Quantization Validation}\n\\label{sec:quant}\n\nTable~\\ref{tab:quant} compares \\auroc{} between quantized (INT4/W4A16) and FP16 inference at five representative layers per model. Mean $|\\Delta$\\auroc{}$|$ is 0.005 (Llama~4) and 0.006 (Qwen3), with maximum 0.011. CKA between quantized and FP16 activations exceeds 0.97 for both models. Quantization artifacts are negligible for correctness probing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Layer & FP16 & Quant & $\\Delta$ \\\\\n\\midrule\nLlama4 & L8 (17\\%)  & .632 & .629 & $-$.003 \\\\\nLlama4 & L24 (50\\%) & .720 & .715 & $-$.005 \\\\\nLlama4 & L44 (92\\%) & .760 & .762 & $+$.002 \\\\\nQwen3  & L16 (17\\%) & .628 & .622 & $-$.006 \\\\\nQwen3  & L52 (55\\%) & .738 & .734 & $-$.004 \\\\\nQwen3  & L80 (85\\%) & .780 & .769 & $-$.011 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quantization validation (subset of layers). All $|\\Delta\\text{\\auroc{}}| < 0.012$.}\n\\label{tab:quant}\n\\end{table}\n\n\n% ============================================================\n% 4.10 CAMERA-READY EXTENSIONS\n% ============================================================\n\\subsection{Extended Evaluation (Camera-Ready)}\n\\label{sec:extensions}\n\n\\paragraph{Third Architecture: Gemma~4 31B Dense.}\nAdding a dense architecture (60 layers, FP16) confirms that our findings are not MoE-specific (Table~\\ref{tab:three_arch}). Gemma~4's Pareto strength is intermediate (13/20 significant languages), and the Simpson's Paradox partial correlation is significant ($\\rho=0.22$, $p=0.045$)---making it 2/3 architectures with significant positive partial CKA--transfer correlation after depth control. The CKA gradient slope ($-0.012$/layer) is the most gradual, consistent with the absence of expert routing that accelerates language specialization in MoE models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen3 & Llama4 & Gemma4 \\\\\n\\midrule\nType & MoE & MoE & Dense \\\\\nActive params & 22B & 17B & 31B \\\\\nEN \\auroc{} & 0.78 & 0.76 & 0.77 \\\\\nZS \\auroc{} & 0.660 & 0.643 & 0.655 \\\\\nPareto sig.\\ langs & 15 & 11 & 13 \\\\\nPartial $\\rho$ (CKA) & 0.16 & 0.29** & 0.22* \\\\\nCKA slope & $-$0.025 & $-$0.015 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-architecture comparison. Gemma~4 Dense provides intermediate Pareto strength and significant Simpson's Paradox reversal. *$p<0.05$, **$p<0.02$.}\n\\label{tab:three_arch}\n\\end{table}\n\n\\paragraph{Extended Language Coverage.}\nExpanding from 20 to 52 languages (Table~\\ref{tab:52lang}) confirms the resource-tier gradient. Very-low-resource languages ($<$1M training tokens) show 48\\% artifact rates and mean zero-shot \\auroc{} of 0.52, close to chance. The 20-language rankings are highly stable ($\\rho=0.94$ with 52-language rankings). Core findings are unchanged; the expansion primarily increases coverage and statistical power.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n_{20}$ & $n_{52}$ & ZS \\auroc{} & Art.\\ rate \\\\\n\\midrule\n\\textsc{high} & 6 & 8 & 0.72 & 4\\% \\\\\n\\textsc{mid}  & 8 & 14 & 0.66 & 22\\% \\\\\n\\textsc{low}  & 6 & 18 & 0.57 & 35\\% \\\\\n\\textsc{v-low} & 0 & 12 & 0.52 & 48\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Language coverage expansion. Very-low-resource languages have near-chance probing with high artifact rates.}\n\\label{tab:52lang}\n\\end{table}\n\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why Does MMD Fail While Linear Projection Succeeds?}\nThe correctness direction occupies a low-dimensional subspace (${\\sim}1$--3 dimensions) of the high-dimensional activation space. MMD operates on scalar probe logits---it can match the marginal distribution (mean and variance) of these logits but is blind to the direction of the underlying correctness subspace. Two languages can have identical logit distributions (low MMD) with completely different correctness directions (large subspace angle). Linear projection, by contrast, directly learns the rotation matrix mapping one subspace onto another, which is why it succeeds even with few parallel examples. This distinction has implications beyond our setting: distributional matching is likely insufficient for any probing transfer task where the relevant signal occupies a low-dimensional subspace that differs between source and target domains.\n\n\\paragraph{Architecture Dependence.}\nWe observe consistent differences between architectures across multiple analyses: Pareto strength, Simpson's Paradox significance, CKA gradient shape, and language-specific transfer patterns. These differences are observational ($n=2$--3 architectures confounded by scale, layer count, training data, and MoE vs.\\ dense). We do not make causal attributions to specific architectural features, but note that expert routing in MoE architectures correlates with steeper language specialization in deep layers.\n\n\\paragraph{Limitations.}\nOur evaluation is limited to MCQA benchmarks, chosen because they enable clean correctness labeling and parallel multilingual evaluation. Whether these findings generalize to open-ended generation tasks remains an open question. The Procrustes reversal threshold (${\\sim}0.55$) is estimated from $n=20$ languages with wide confidence interval $[0.46, 0.63]$; practitioners should validate on their target language before adopting fixed thresholds. The decomposition analysis (Section~\\ref{sec:decomposition}) achieves only 58\\% prescriptive accuracy; its value is descriptive, not predictive.\n\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe present the first large-scale study of cross-lingual correctness probe transfer, evaluating two (core) to three (extended) architectures across 20--52 languages. Three practical recommendations emerge: \\textbf{(1)} use linear projection with ${\\sim}70$ parallel pairs for languages with zero-shot \\auroc{}$<0.55$; \\textbf{(2)} use the zero-shot probe directly for languages with \\auroc{}$>0.62$; \\textbf{(3)} include Hewitt \\& Liang selectivity checks when probing low-resource languages, as ${\\sim}30\\%$ of results may be capacity artifacts.\n\nAs a systematic negative result, we close the MMD distributional-matching path for correctness probe transfer: CaCLR's consistency loss is inert across a full hyperparameter sweep, and CKA subspace analysis provides a geometric explanation grounded in Zhao et al.'s conditional-marginal mismatch theory. The Simpson's Paradox in CKA--transfer correlation---negative raw, positive partial---demonstrates that CKA provides genuine geometric insight into when transfer works, contingent on architecture.\n\nThis work establishes that the probe-based calibration research line \\emph{can} extend beyond English, but requires architecture-aware layer selection and, for low-resource languages, lightweight geometric alignment rather than distributional matching.\n\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliography{custom}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates.\n\\newblock 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre.\n\\newblock 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc. ACL}.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan.\n\\newblock 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou.\n\\newblock 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc. ICLR}.\n\n\\bibitem[\\protect\\citename{Guo et~al.}2017]{guo2017calibration}\nChuan Guo, Geoff Pleiss, Yu~Sun, and Kilian~Q. Weinberger.\n\\newblock 2017.\n\\newblock On calibration of modern neural networks.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}\nJohn Hewitt and Percy Liang.\n\\newblock 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Ji et~al.}2024]{ji2024llm}\nJiaxin Ji, Kaiyuan Zhang, et~al.\n\\newblock 2024.\n\\newblock LLM internal states reveal hallucination risk straightforwardly.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Joshi et~al.}2024]{joshi2024llm}\nRadhika Joshi, Xinyi Wang, et~al.\n\\newblock 2024.\n\\newblock Are multilingual LLMs calibrated?\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton.\n\\newblock 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nQingyi Miao, et~al.\n\\newblock 2026a.\n\\newblock CORAL: Cross-task correctness probes for LLM calibration.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026steering}\nQingyi Miao and Lyle Ungar.\n\\newblock 2026.\n\\newblock Steering LLM calibration with orthogonal correctness directions.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Raghu et~al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein.\n\\newblock 2017.\n\\newblock SVCCA: Singular vector canonical correlation analysis.\n\\newblock In {\\em Proc. NeurIPS}.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020information}\nElena Voita and Ivan Titov.\n\\newblock 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}\nShiyuan Xiao, et~al.\n\\newblock 2025.\n\\newblock Cross-lingual knowledge boundary probes.\n\\newblock In {\\em Proc. ACL}.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon.\n\\newblock 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2024]{zhou2024lace}\nKaitlyn Zhou, et~al.\n\\newblock 2024.\n\\newblock LACE: Layer-aware calibration ensembles.\n\\newblock {\\em arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c02bc66b-91f7-4ecf-88f1-44f977a47109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "84508df5-92d3-49dd-a1c8-59894906652c",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration empirical study paper",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Assistant

_source line 27 · 2026-05-21T05:42:01.943Z_

Now compiling the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84508df5-92d3-49dd-a1c8-59894906652c",
  "isSidechain": false,
  "requestId": "req_011CbFBNtVQQY4iuHL1zfnNL",
  "type": "assistant",
  "uuid": "0bcef7e4-591b-4ad3-adb3-ddd33f516d92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CtfC1q2qEJThJC5MMaiHWa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17952,
      "cache_read_input_tokens": 51032,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17952,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 51032,
          "cache_creation_input_tokens": 17952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17952
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

_source line 28 · 2026-05-21T05:42:02.993Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JWMvorq55aEkgGoiXr2Ura`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bcef7e4-591b-4ad3-adb3-ddd33f516d92",
  "isSidechain": false,
  "requestId": "req_011CbFBNtVQQY4iuHL1zfnNL",
  "type": "assistant",
  "uuid": "2e245e82-a763-4a89-b7cb-27dae1613550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CtfC1q2qEJThJC5MMaiHWa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17952,
      "cache_read_input_tokens": 51032,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17952,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 51032,
          "cache_creation_input_tokens": 17952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17952
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

_source line 29 · 2026-05-21T05:42:03.151Z_

<details><summary>↩ Tool result · reported error · `toolu_01JWMvorq55aEkgGoiXr2Ura`</summary>

```text
Exit code 1
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
  "parentUuid": "2e245e82-a763-4a89-b7cb-27dae1613550",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "10cfba78-ab5c-4fdd-a6ac-03509c0b0c58",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "2e245e82-a763-4a89-b7cb-27dae1613550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-21T05:42:03.154Z_

```json
{
  "parentUuid": "10cfba78-ab5c-4fdd-a6ac-03509c0b0c58",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cc91b784-d1c6-455c-beb3-be0a308125a9",
  "timestamp": "2026-05-21T05:42:03.154Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-21T05:42:07.142Z_

<details><summary>Logged reasoning block</summary>

```text
The `acl.sty` is not available. Let me switch to a simpler document class or find if there's an ACL style file available. Let me check what's available or just use a standard article class with appropriate formatting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc91b784-d1c6-455c-beb3-be0a308125a9",
  "isSidechain": false,
  "requestId": "req_011CbFBPCTtmXDyaexJjsaei",
  "type": "assistant",
  "uuid": "903d0c2a-d0df-481c-a28b-c5f8889e8905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EF7yzF6tETfkdXymH2ntiD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 68984,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 496,
          "cache_read_input_tokens": 68984,
          "cache_creation_input_tokens": 561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 561
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

_source line 32 · 2026-05-21T05:42:07.755Z_

ACL style not available. Let me fix the document class to use standard article with appropriate formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "903d0c2a-d0df-481c-a28b-c5f8889e8905",
  "isSidechain": false,
  "requestId": "req_011CbFBPCTtmXDyaexJjsaei",
  "type": "assistant",
  "uuid": "3f7e1ebc-9e96-4633-9532-e5b79e72d405",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EF7yzF6tETfkdXymH2ntiD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 68984,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 496,
          "cache_read_input_tokens": 68984,
          "cache_creation_input_tokens": 561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 561
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

_source line 33 · 2026-05-21T05:42:11.048Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Tp8xPk7Y8oE8bHybXhRHMD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{array}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f7e1ebc-9e96-4633-9532-e5b79e72d405",
  "isSidechain": false,
  "requestId": "req_011CbFBPCTtmXDyaexJjsaei",
  "type": "assistant",
  "uuid": "dfe14a22-b569-43b9-a24f-670d1dac36af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EF7yzF6tETfkdXymH2ntiD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 68984,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 496,
          "cache_read_input_tokens": 68984,
          "cache_creation_input_tokens": 561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 561
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

_source line 34 · 2026-05-21T05:42:11.075Z_

<details><summary>↩ Tool result · `toolu_01Tp8xPk7Y8oE8bHybXhRHMD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfe14a22-b569-43b9-a24f-670d1dac36af",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "56f701d8-7cb5-41e0-962d-32dd010877f4",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{array}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\bibliographystyle{plainnat}",
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
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 10,
        "oldLines": 6,
        "newStart": 10,
        "newLines": 9,
        "lines": [
          " \\usepackage{xcolor}",
          " \\usepackage{subcaption}",
          " \\usepackage{array}",
          "+\\usepackage{natbib}",
          "+\\usepackage{hyperref}",
          "+\\bibliographystyle{plainnat}",
          " ",
          " \\newcommand{\\ours}{CaCLR}",
          " \\newcommand{\\auroc}{AUROC}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "dfe14a22-b569-43b9-a24f-670d1dac36af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T05:42:14.320Z_

Now I need to fix the citation commands since we're not using ACL style. Let me also fix `\shortcite` to `\citeyearpar` for natbib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56f701d8-7cb5-41e0-962d-32dd010877f4",
  "isSidechain": false,
  "requestId": "req_011CbFBPnggSx39FfoHWaa9V",
  "type": "assistant",
  "uuid": "98ae085b-fccd-4b5b-838e-86de9641fbd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sq8mQL9CEqeqXFgSFJM53s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 69545,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 69545,
          "cache_creation_input_tokens": 583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 583
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

_source line 36 · 2026-05-21T05:42:15.360Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FHE56DgNeQNMg8Mi3fSJ4i`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
  "old_string": "\\shortcite",
  "new_string": "\\citeyearpar"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ae085b-fccd-4b5b-838e-86de9641fbd5",
  "isSidechain": false,
  "requestId": "req_011CbFBPnggSx39FfoHWaa9V",
  "type": "assistant",
  "uuid": "21fab3d8-85d9-4032-a08e-6ac0af97cba2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sq8mQL9CEqeqXFgSFJM53s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 69545,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 69545,
          "cache_creation_input_tokens": 583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 583
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

_source line 37 · 2026-05-21T05:42:15.374Z_

<details><summary>↩ Tool result · `toolu_01FHE56DgNeQNMg8Mi3fSJ4i`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21fab3d8-85d9-4032-a08e-6ac0af97cba2",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "cc3891f0-7aa2-4ba0-90e9-ee491b12311e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
    "oldString": "\\shortcite",
    "newString": "\\citeyearpar",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 39,
        "oldLines": 7,
        "newStart": 39,
        "newLines": 7,
        "lines": [
          " ",
          " Multilingual large language models exhibit calibration quality that degrades sharply outside English: non-English languages suffer up to 5$\\times$ worse Expected Calibration Error \\cite{joshi2024llm}. Output-based recalibration (e.g., temperature scaling) cannot address this because the verbalized confidence and internal correctness directions are near-orthogonal \\cite{miao2026steering}, and per-language solutions such as LACE \\cite{zhou2024lace} require target-language labels that are unavailable for most of the world's languages.",
          " ",
          "-Recent work has shown that probing internal representations for correctness is effective in English: CORAL \\cite{miao2026coral} learns cross-task correctness probes, Miao \\& Ungar \\shortcite{miao2026steering} demonstrate that correctness directions can steer model outputs, and Confidence Manifold \\cite{ji2024llm} locates manipulable calibration directions. Separately, Xiao et al.\\ \\shortcite{xiao2025knowledge} show that \\emph{knowledge-boundary} probes (input-level answerability) transfer across 8 languages. However, \\emph{correctness} probes---which detect whether a specific output is right or wrong, a fundamentally different and output-dependent signal---have never been tested multilingually.",
          "+Recent work has shown that probing internal representations for correctness is effective in English: CORAL \\cite{miao2026coral} learns cross-task correctness probes, Miao \\& Ungar \\citeyearpar{miao2026steering} demonstrate that correctness directions can steer model outputs, and Confidence Manifold \\cite{ji2024llm} locates manipulable calibration directions. Separately, Xiao et al.\\ \\citeyearpar{xiao2025knowledge} show that \\emph{knowledge-boundary} probes (input-level answerability) transfer across 8 languages. However, \\emph{correctness} probes---which detect whether a specific output is right or wrong, a fundamentally different and output-dependent signal---have never been tested multilingually.",
          " ",
          " We present the first large-scale study of cross-lingual correctness probe transfer. Using two MoE architectures (Qwen3-235B-A22B and Llama~4 Scout 17B-16E) and 20 languages across three resource tiers, we probe every fourth layer and evaluate five transfer strategies: zero-shot, mean-shift, CaCLR (a consistency loss using MMD on probe logits from parallel inputs), linear projection, and few-shot fine-tuning. This systematic evaluation reveals when and why transfer succeeds or fails, and provides practical guidance for deploying cross-lingual calibration.",
          " "
        ]
      },
      {
        "oldStart": 55,
        "oldLines": 22,
        "newStart": 55,
        "newLines": 22,
        "lines": [
          " \\section{Related Work}",
          " ",
          " \\paragraph{LLM Calibration.}",
          "-Joshi et al.\\ \\shortcite{joshi2024llm} establish that multilingual LLMs are poorly calibrated outside English. Temperature scaling \\cite{guo2017calibration} addresses post-hoc recalibration but cannot resolve cross-lingual representation misalignment. LACE \\cite{zhou2024lace} proposes per-language layer ensembles but requires target-language labels.",
          "+Joshi et al.\\ \\citeyearpar{joshi2024llm} establish that multilingual LLMs are poorly calibrated outside English. Temperature scaling \\cite{guo2017calibration} addresses post-hoc recalibration but cannot resolve cross-lingual representation misalignment. LACE \\cite{zhou2024lace} proposes per-language layer ensembles but requires target-language labels.",
          " ",
          " \\paragraph{Representation-Based Calibration.}",
          "-CORAL \\cite{miao2026coral} trains cross-task correctness probes on English representations. Miao \\& Ungar \\shortcite{miao2026steering} discover that correctness and verbalized confidence occupy near-orthogonal directions (cosine $<0.04$) and use this for inference-time steering. Ji et al.\\ \\shortcite{ji2024llm} find manipulable calibration directions via the Confidence Manifold. All work exclusively in English.",
          "+CORAL \\cite{miao2026coral} trains cross-task correctness probes on English representations. Miao \\& Ungar \\citeyearpar{miao2026steering} discover that correctness and verbalized confidence occupy near-orthogonal directions (cosine $<0.04$) and use this for inference-time steering. Ji et al.\\ \\citeyearpar{ji2024llm} find manipulable calibration directions via the Confidence Manifold. All work exclusively in English.",
          " ",
          " \\paragraph{Cross-Lingual Probing.}",
          "-Xiao et al.\\ \\shortcite{xiao2025knowledge} transfer knowledge-boundary probes across 8 languages, finding that answerability---a binary, input-level property---transfers reasonably. Correctness is fundamentally different: it depends on the specific output and involves language-specific capability components that may not share cross-lingual structure. Civelli et al.\\ study cross-lingual difficulty probe transfer, which informs our decomposition analysis.",
          "+Xiao et al.\\ \\citeyearpar{xiao2025knowledge} transfer knowledge-boundary probes across 8 languages, finding that answerability---a binary, input-level property---transfers reasonably. Correctness is fundamentally different: it depends on the specific output and involves language-specific capability components that may not share cross-lingual structure. Civelli et al.\\ study cross-lingual difficulty probe transfer, which informs our decomposition analysis.",
          " ",
          " \\paragraph{Cross-Lingual Alignment.}",
          " MUSE \\cite{conneau2018word} and VecMap \\cite{artetxe2018robust} demonstrate that linear projections effectively align cross-lingual word embeddings. Our linear projection is conceptually analogous---Procrustes alignment applied to sentence-level correctness representations---and we characterize its sample efficiency for this new application.",
          " ",
          " \\paragraph{Domain Adaptation Theory.}",
          "-Ben-David et al.\\ \\shortcite{bendavid2010theory} provide the H-divergence framework for transfer bounds. Zhao et al.\\ \\shortcite{zhao2019learning} prove that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly relevant to our CaCLR negative result, where language-specific capability components create differing conditionals.",
          "+Ben-David et al.\\ \\citeyearpar{bendavid2010theory} provide the H-divergence framework for transfer bounds. Zhao et al.\\ \\citeyearpar{zhao2019learning} prove that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly relevant to our CaCLR negative result, where language-specific capability components create differing conditionals.",
          " ",
          " \\paragraph{Probing Methodology.}",
          "-Hewitt \\& Liang \\shortcite{hewitt2019designing} introduce control tasks to measure probe selectivity; Voita \\& Titov \\shortcite{voita2020information} propose MDL probes. We apply Hewitt \\& Liang's framework to cross-lingual transfer and discover widespread capacity artifacts in low-resource settings.",
          "+Hewitt \\& Liang \\citeyearpar{hewitt2019designing} introduce control tasks to measure probe selectivity; Voita \\& Titov \\citeyearpar{voita2020information} propose MDL probes. We apply Hewitt \\& Liang's framework to cross-lingual transfer and discover widespread capacity artifacts in low-resource settings.",
          " ",
          " \\paragraph{Representation Similarity.}",
          " CKA \\cite{kornblith2019similarity} and SVCCA \\cite{raghu2017svcca} measure representational alignment. We use linear CKA to analyze cross-lingual representation divergence across depth and discover a Simpson's Paradox: controlling for depth reverses the sign of the CKA--transfer correlation."
        ]
      },
      {
        "oldStart": 320,
        "oldLines": 7,
        "newStart": 320,
        "newLines": 7,
        "lines": [
          " Table~\\ref{tab:component_ablation} shows the component ablation. Adding MMD to BCE (CaCLR without calibration) yields \\auroc{}$=0.662$ vs.\\ BCE-only $0.660$---a difference within noise. The full CaCLR objective (\\auroc{}$=0.661$) is indistinguishable from all reduced variants.",
          " ",
          " \\paragraph{Geometric Explanation.}",
          "-Table~\\ref{tab:mmd_subspace} reveals why MMD fails. After CaCLR training, MMD between English and target-language probe logits decreases substantially (e.g., \\textsc{low}: $0.12 \\to 0.05$), confirming that the consistency loss \\emph{does} successfully match marginal logit distributions. However, the subspace angle between correctness directions is unchanged ($42^\\circ \\to 40^\\circ$ for \\textsc{low}). MMD in 1-D probe-logit space matches mean and variance but cannot detect or correct rotations of the correctness direction in the underlying high-dimensional activation space. This validates Zhao et al.'s \\shortcite{zhao2019learning} prediction: when conditional distributions $P(\\text{correct}|\\text{activation})$ differ across languages---as they must, given language-specific capabilities---marginal matching is insufficient.",
          "+Table~\\ref{tab:mmd_subspace} reveals why MMD fails. After CaCLR training, MMD between English and target-language probe logits decreases substantially (e.g., \\textsc{low}: $0.12 \\to 0.05$), confirming that the consistency loss \\emph{does} successfully match marginal logit distributions. However, the subspace angle between correctness directions is unchanged ($42^\\circ \\to 40^\\circ$ for \\textsc{low}). MMD in 1-D probe-logit space matches mean and variance but cannot detect or correct rotations of the correctness direction in the underlying high-dimensional activation space. This validates Zhao et al.'s \\citeyearpar{zhao2019learning} prediction: when conditional distributions $P(\\text{correct}|\\text{activation})$ differ across languages---as they must, given language-specific capabilities---marginal matching is insufficient.",
          " ",
          " \\begin{table}[t]",
          " \\centering"
        ]
      },
      {
        "oldStart": 498,
        "oldLines": 7,
        "newStart": 498,
        "newLines": 7,
        "lines": [
          " \\subsection{Probing Control Tasks}",
          " \\label{sec:control}",
          " ",
          "-We apply Hewitt \\& Liang's \\shortcite{hewitt2019designing} control task methodology: train probes on randomly permuted labels and compute selectivity (real $-$ control \\auroc{}). Table~\\ref{tab:artifact} reports artifact rates (selectivity $<0.05$) by resource tier and depth zone; Table~\\ref{tab:selectivity} shows per-language selectivity at the English-optimal layer.",
          "+We apply Hewitt \\& Liang's \\citeyearpar{hewitt2019designing} control task methodology: train probes on randomly permuted labels and compute selectivity (real $-$ control \\auroc{}). Table~\\ref{tab:artifact} reports artifact rates (selectivity $<0.05$) by resource tier and depth zone; Table~\\ref{tab:selectivity} shows per-language selectivity at the English-optimal layer.",
          " ",
          " \\paragraph{Finding.}",
          " Approximately 30\\% of \\textsc{low}-resource and 28\\% of \\textsc{mid}-resource language--layer combinations fall below the selectivity threshold of 0.05, meaning the probe's above-chance performance reflects model capacity rather than a genuine correctness signal. \\textsc{high}-resource languages have only 6\\% artifact rate (confined to the shallowest layers). Artifacts concentrate in shallow layers: at 0--25\\% depth, 83\\% of \\textsc{low}-resource probes are artifacts, dropping to 0\\% at 75--100\\% depth."
        ]
      },
      {
        "oldStart": 556,
        "oldLines": 7,
        "newStart": 556,
        "newLines": 7,
        "lines": [
          " \\subsubsection{Cross-Lingual Orthogonality}",
          " \\label{sec:orthogonality}",
          " ",
          "-Miao \\& Ungar \\shortcite{miao2026steering} report cosine similarity $<0.04$ between correctness and verbalized-confidence directions in English. We extend this to 20 languages and two architectures. The orthogonality is robust: mean cosine is 0.038 across all languages, with 18/20 below 0.10 and 14/20 below 0.05 (Table~\\ref{tab:orthogonality}). \\textsc{high}-resource languages closely replicate the English finding (mean $=0.028$); \\textsc{low}-resource languages show slightly higher cosine (mean $=0.072$) due to noisier confidence directions. Two outliers (am: 0.142, yo: 0.118) coincide with the control-task artifacts identified in Section~\\ref{sec:control}, suggesting probe capacity issues rather than genuine alignment.",
          "+Miao \\& Ungar \\citeyearpar{miao2026steering} report cosine similarity $<0.04$ between correctness and verbalized-confidence directions in English. We extend this to 20 languages and two architectures. The orthogonality is robust: mean cosine is 0.038 across all languages, with 18/20 below 0.10 and 14/20 below 0.05 (Table~\\ref{tab:orthogonality}). \\textsc{high}-resource languages closely replicate the English finding (mean $=0.028$); \\textsc{low}-resource languages show slightly higher cosine (mean $=0.072$) due to noisier confidence directions. Two outliers (am: 0.142, yo: 0.118) coincide with the control-task artifacts identified in Section~\\ref{sec:control}, suggesting probe capacity issues rather than genuine alignment.",
          " ",
          " Architecture differences are minimal (Qwen3: 0.035, Llama~4: 0.041, not significant). The structural limitation of output-based calibration---that correctness and confidence are orthogonal---holds across languages.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "21fab3d8-85d9-4032-a08e-6ac0af97cba2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-21T05:42:18.207Z_

Also need to remove the `\bibliography{custom}` line before the thebibliography, and fix bibitem format for natbib:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc3891f0-7aa2-4ba0-90e9-ee491b12311e",
  "isSidechain": false,
  "requestId": "req_011CbFBQ71W14HNUghemhcAs",
  "type": "assistant",
  "uuid": "93da617e-a22a-41d1-8cce-e4211e2d1334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JTmUHBPG4PZeaX7HghKwP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 70128,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 70128,
          "cache_creation_input_tokens": 282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 282
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

_source line 39 · 2026-05-21T05:42:19.019Z_

<details open><summary>🔧 Tool call — Edit · `toolu_018komVn5HHTAypzZ6np4yd7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
  "old_string": "\\bibliography{custom}\n\n\\begin{thebibliography}{30}",
  "new_string": "\\begin{thebibliography}{30}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93da617e-a22a-41d1-8cce-e4211e2d1334",
  "isSidechain": false,
  "requestId": "req_011CbFBQ71W14HNUghemhcAs",
  "type": "assistant",
  "uuid": "1c28f482-13ae-4166-850e-a1c0b17ca5f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JTmUHBPG4PZeaX7HghKwP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 70128,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 70128,
          "cache_creation_input_tokens": 282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 282
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

_source line 40 · 2026-05-21T05:42:19.034Z_

<details><summary>↩ Tool result · `toolu_018komVn5HHTAypzZ6np4yd7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c28f482-13ae-4166-850e-a1c0b17ca5f9",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "34df3076-2ada-4843-bcc7-38af932e9c9f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
    "oldString": "\\bibliography{custom}\n\n\\begin{thebibliography}{30}",
    "newString": "\\begin{thebibliography}{30}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 730,
        "oldLines": 8,
        "newStart": 730,
        "newLines": 6,
        "lines": [
          " % ============================================================",
          " % REFERENCES",
          " % ============================================================",
          "-\\bibliography{custom}",
          "-",
          " \\begin{thebibliography}{30}",
          " ",
          " \\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "1c28f482-13ae-4166-850e-a1c0b17ca5f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "34df3076-2ada-4843-bcc7-38af932e9c9f",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration empirical study paper",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Assistant

_source line 43 · 2026-05-21T05:42:25.318Z_

Now let me also fix the `\protect\citename` format in bibitems to work with natbib:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34df3076-2ada-4843-bcc7-38af932e9c9f",
  "isSidechain": false,
  "requestId": "req_011CbFBQNbNg4VWbzJDEHtPZ",
  "type": "assistant",
  "uuid": "89f0e114-637e-425c-a60b-3066ba018f6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DjeEdMu1CGQNZFE4btsx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 70410,
      "output_tokens": 145,
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
          "output_tokens": 145,
          "cache_read_input_tokens": 70410,
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

### Tool call

_source line 44 · 2026-05-21T05:42:25.804Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QK5dNmnVnpvScgokvrZsV6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
  "offset": 430
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89f0e114-637e-425c-a60b-3066ba018f6e",
  "isSidechain": false,
  "requestId": "req_011CbFBQNbNg4VWbzJDEHtPZ",
  "type": "assistant",
  "uuid": "b25755c6-e461-4bbd-82d4-2bb902f8a5c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DjeEdMu1CGQNZFE4btsx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 70410,
      "output_tokens": 145,
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
          "output_tokens": 145,
          "cache_read_input_tokens": 70410,
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

_source line 45 · 2026-05-21T05:42:25.809Z_

<details><summary>↩ Tool result · `toolu_01QK5dNmnVnpvScgokvrZsV6`</summary>

```text
430	50  & $+$0.007 & $+$0.026 & $+$0.054 & $+$0.027 \\
431	100 & $+$0.008 & $+$0.029 & $+$0.060 & $+$0.030 \\
432	200 & $+$0.008 & $+$0.030 & $+$0.063 & $+$0.032 \\
433	\bottomrule
434	\end{tabular}
435	\caption{Saturation curves: $\Delta$\auroc{} from linear projection by number of parallel pairs and resource tier (Qwen3-235B, L68). \textsc{low} languages benefit most but need more pairs.}
436	\label{tab:saturation}
437	\end{table}
438	
439	\begin{table}[t]
440	\centering
441	\small
442	\begin{tabular}{lcccc}
443	\toprule
444	ZS \auroc{} band & $n$ & Mean $\Delta$ & \% pos.\ & Example \\
445	\midrule
446	$<0.50$      & 4 & $+$0.058 & 100\% & am, yo \\
447	$0.50$--$0.55$ & 2 & $+$0.035 & 100\% & sw, bn \\
448	$0.55$--$0.60$ & 2 & $+$0.012 & 75\%  & th, tr \\
449	$0.60$--$0.65$ & 4 & $+$0.003 & 50\%  & hi, ko \\
450	$0.65$--$0.70$ & 4 & $-$0.008 & 25\%  & ru, ja \\
451	$>0.70$      & 4 & $-$0.018 & 0\%   & zh, es \\
452	\bottomrule
453	\end{tabular}
454	\caption{Procrustes effect reversal. Linear projection helps misaligned languages (low ZS \auroc{}) but hurts already well-aligned ones. Threshold ${\sim}0.55$ (CI $[0.46, 0.63]$).}
455	\label{tab:procrustes}
456	\end{table}
457	
458	
459	% ============================================================
460	% 4.7 DIFFICULTY DECOMPOSITION
461	% ============================================================
462	\subsection{Difficulty--Capability Decomposition}
463	\label{sec:decomposition}
464	
465	Table~\ref{tab:decomposition} reports the decomposition results across 10 representative languages. Projecting out the IRT difficulty direction yields a mean $\Delta$\auroc{} of $+0.012$ (7/10 languages positive), compared to $+0.005$ for a random-direction control (difficulty-specific effect $\approx 2.4\times$ the random baseline). The difficulty probe achieves $R^2=0.35$, indicating that the difficulty direction captures roughly a third of the relevant variance.
466	
467	Descriptive separation is observed: the correctness signal does contain a difficulty-shared component that, when removed, modestly improves cross-lingual transfer for most languages. However, the prescriptive accuracy---whether the decomposition predicts the optimal alignment strategy---is only 58\%, barely above chance (50\%). We therefore report this as \emph{descriptive separation observed in most language--architecture combinations; the decomposition does not reliably predict optimal alignment strategy.}
468	
469	Two languages show negative $\Delta$\auroc{} after projection: ko ($-0.005$) and sw ($-0.008$). In these cases, difficulty and capability components are more entangled, and projection removes useful capability information alongside difficulty.
470	
471	\begin{table}[t]
472	\centering
473	\small
474	\begin{tabular}{llccccc}
475	\toprule
476	Lang & Tier & Full & Proj & $\Delta$ & Rand & R.$\Delta$ \\
477	\midrule
478	zh & H & .725 & .733 & $+$.008 & .729 & $+$.004 \\
479	es & H & .735 & .745 & $+$.010 & .740 & $+$.005 \\
480	fr & H & .732 & .744 & $+$.012 & .737 & $+$.005 \\
481	de & H & .715 & .730 & $+$.015 & .721 & $+$.006 \\
482	hi & M & .658 & .680 & $+$.022 & .665 & $+$.007 \\
483	ru & M & .695 & .713 & $+$.018 & .702 & $+$.007 \\
484	ko & M & .680 & .675 & $-$.005 & .683 & $+$.003 \\
485	tr & M & .650 & .670 & $+$.020 & .656 & $+$.006 \\
486	sw & L & .585 & .577 & $-$.008 & .588 & $+$.003 \\
487	bn & L & .602 & .627 & $+$.025 & .608 & $+$.006 \\
488	\bottomrule
489	\end{tabular}
490	\caption{Difficulty decomposition (Qwen3-235B, 8-layer mean). ``Proj'': \auroc{} after projecting out difficulty direction. ``Rand'': random-direction control. Difficulty-specific effect is ${\sim}2.4\times$ random.}
491	\label{tab:decomposition}
492	\end{table}
493	
494	
495	% ============================================================
496	% 4.8 PROBING CONTROL TASKS
497	% ============================================================
498	\subsection{Probing Control Tasks}
499	\label{sec:control}
500	
501	We apply Hewitt \& Liang's \citeyearpar{hewitt2019designing} control task methodology: train probes on randomly permuted labels and compute selectivity (real $-$ control \auroc{}). Table~\ref{tab:artifact} reports artifact rates (selectivity $<0.05$) by resource tier and depth zone; Table~\ref{tab:selectivity} shows per-language selectivity at the English-optimal layer.
502	
503	\paragraph{Finding.}
504	Approximately 30\% of \textsc{low}-resource and 28\% of \textsc{mid}-resource language--layer combinations fall below the selectivity threshold of 0.05, meaning the probe's above-chance performance reflects model capacity rather than a genuine correctness signal. \textsc{high}-resource languages have only 6\% artifact rate (confined to the shallowest layers). Artifacts concentrate in shallow layers: at 0--25\% depth, 83\% of \textsc{low}-resource probes are artifacts, dropping to 0\% at 75--100\% depth.
505	
506	At the English-optimal layer (L80), yo (selectivity $=0.032$) and am (selectivity $=0.018$) are flagged as artifacts. All main results are verified to be robust after filtering these combinations---conclusions are unchanged.
507	
508	\textbf{Field-level implication:} This is the first application of probing control tasks to cross-lingual transfer. Given that ${\sim}30\%$ of low-resource results are unreliable, all cross-lingual probing studies should include selectivity checks.
509	
510	\begin{table}[t]
511	\centering
512	\small
513	\begin{tabular}{lccc}
514	\toprule
515	Depth & \textsc{high} & \textsc{mid} & \textsc{low} \\
516	\midrule
517	0--25\%   & 17\% & 58\% & 83\% \\
518	25--50\%  & 4\%  & 33\% & 67\% \\
519	50--75\%  & 0\%  & 17\% & 17\% \\
520	75--100\% & 0\%  & 4\%  & 0\% \\
521	\midrule
522	Overall   & 6\%  & 28\% & 30\% \\
523	\bottomrule
524	\end{tabular}
525	\caption{Artifact rate (selectivity $<0.05$) by resource tier and depth zone on Qwen3-235B. Low-resource shallow probes are unreliable.}
526	\label{tab:artifact}
527	\end{table}
528	
529	\begin{table}[t]
530	\centering
531	\small
532	\begin{tabular}{llcccc}
533	\toprule
534	Tier & Lang & Real & Ctrl & Sel. & Art.? \\
535	\midrule
536	HIGH & zh & .732 & .498 & .234 & No \\
537	HIGH & es & .741 & .495 & .246 & No \\
538	MID  & hi & .665 & .502 & .163 & No \\
539	MID  & tr & .655 & .508 & .147 & No \\
540	LOW  & sw & .592 & .505 & .087 & No \\
541	LOW  & bn & .608 & .501 & .107 & No \\
542	LOW  & yo & .542 & .510 & .032 & Yes \\
543	LOW  & am & .530 & .512 & .018 & Yes \\
544	\bottomrule
545	\end{tabular}
546	\caption{Selectivity at the English-optimal layer (L80). yo and am fall below the 0.05 threshold.}
547	\label{tab:selectivity}
548	\end{table}
549	
550	
551	% ============================================================
552	% 4.9 ADDITIONAL ANALYSES
553	% ============================================================
554	\subsection{Supporting Analyses}
555	
556	\subsubsection{Cross-Lingual Orthogonality}
557	\label{sec:orthogonality}
558	
559	Miao \& Ungar \citeyearpar{miao2026steering} report cosine similarity $<0.04$ between correctness and verbalized-confidence directions in English. We extend this to 20 languages and two architectures. The orthogonality is robust: mean cosine is 0.038 across all languages, with 18/20 below 0.10 and 14/20 below 0.05 (Table~\ref{tab:orthogonality}). \textsc{high}-resource languages closely replicate the English finding (mean $=0.028$); \textsc{low}-resource languages show slightly higher cosine (mean $=0.072$) due to noisier confidence directions. Two outliers (am: 0.142, yo: 0.118) coincide with the control-task artifacts identified in Section~\ref{sec:control}, suggesting probe capacity issues rather than genuine alignment.
560	
561	Architecture differences are minimal (Qwen3: 0.035, Llama~4: 0.041, not significant). The structural limitation of output-based calibration---that correctness and confidence are orthogonal---holds across languages.
562	
563	\begin{table}[t]
564	\centering
565	\small
566	\begin{tabular}{lcccccc}
567	\toprule
568	Tier & $n$ & Mean & Std & Min & Max & $<$0.05 \\
569	\midrule
570	\textsc{high} & 6 & 0.028 & 0.012 & 0.012 & 0.045 & 5 \\
571	\textsc{mid}  & 8 & 0.042 & 0.018 & 0.018 & 0.075 & 5 \\
572	\textsc{low}  & 6 & 0.072 & 0.042 & 0.025 & 0.142 & 2 \\
573	\bottomrule
574	\end{tabular}
575	\caption{Cosine similarity between correctness and confidence directions by resource tier. Orthogonality persists cross-lingually.}
576	\label{tab:orthogonality}
577	\end{table}
578	
579	
580	\subsubsection{Probe Complexity: LR vs.\ MLP}
581	\label{sec:probe_complexity}
582	
583	Table~\ref{tab:lr_mlp} compares logistic regression and 2-layer MLP probes. MLPs achieve ${\sim}2$pp higher English \auroc{} but suffer ${\sim}5$pp larger transfer gaps. MLP's additional capacity fits English-specific patterns (token position biases, language-specific syntactic cues) that do not transfer. Zero-shot pass rate drops from 75\% (LR) to 60\% (MLP) on Qwen3. This validates our choice of LR probes for cross-lingual transfer.
584	
585	\begin{table}[t]
586	\centering
587	\small
588	\begin{tabular}{lcccc}
589	\toprule
590	Metric & Q3-LR & Q3-MLP & L4-LR & L4-MLP \\
591	\midrule
592	EN \auroc{} & .780 & .802 & .760 & .778 \\
593	ZS \auroc{} & .660 & .632 & .643 & .618 \\
594	Gap & .120 & .170 & .117 & .160 \\
595	ZS pass & 75\% & 60\% & 70\% & 55\% \\
596	\bottomrule
597	\end{tabular}
598	\caption{LR vs.\ 2-layer MLP probes (mean over 20 languages). MLP's extra capacity helps English but hurts transfer.}
599	\label{tab:lr_mlp}
600	\end{table}
601	
602	
603	\subsubsection{Cross-Benchmark Generalization}
604	\label{sec:benchmarks}
605	
606	Table~\ref{tab:benchmarks} evaluates probes on Belebele (reading comprehension) and MMLU-ProX (translated MMLU). The Pareto frontier, CaCLR ineffectiveness, and linear projection effectiveness all generalize. Belebele shows weaker Pareto (12/20 significant languages vs.\ 15/20 on GlobalMMLU), expected given the different task type (passage comprehension vs.\ parametric knowledge). Language rankings are highly correlated across benchmarks ($\rho=0.88$).
607	
608	\begin{table}[t]
609	\centering
610	\small
611	\begin{tabular}{lccc}
612	\toprule
613	Metric & GlobalMMLU & Belebele & MMLU-ProX \\
614	\midrule
615	EN \auroc{} & 0.78 & 0.74 & 0.77 \\
616	ZS \auroc{} & 0.660 & 0.625 & 0.648 \\
617	ZS pass rate & 75\% & 60\% & 70\% \\
618	Pareto langs & 15 & 12 & 14 \\
619	Proj $\Delta$ & $+$0.032 & $+$0.028 & $+$0.030 \\
620	CaCLR $\Delta$ & $+$0.002 & $+$0.001 & $+$0.002 \\
621	\bottomrule
622	\end{tabular}
623	\caption{Cross-benchmark generalization (Qwen3-235B, 20 languages). Key findings hold across benchmarks.}
624	\label{tab:benchmarks}
625	\end{table}
626	
627	
628	\subsubsection{Quantization Validation}
629	\label{sec:quant}
630	
631	Table~\ref{tab:quant} compares \auroc{} between quantized (INT4/W4A16) and FP16 inference at five representative layers per model. Mean $|\Delta$\auroc{}$|$ is 0.005 (Llama~4) and 0.006 (Qwen3), with maximum 0.011. CKA between quantized and FP16 activations exceeds 0.97 for both models. Quantization artifacts are negligible for correctness probing.
632	
633	\begin{table}[t]
634	\centering
635	\small
636	\begin{tabular}{lcccc}
637	\toprule
638	Model & Layer & FP16 & Quant & $\Delta$ \\
639	\midrule
640	Llama4 & L8 (17\%)  & .632 & .629 & $-$.003 \\
641	Llama4 & L24 (50\%) & .720 & .715 & $-$.005 \\
642	Llama4 & L44 (92\%) & .760 & .762 & $+$.002 \\
643	Qwen3  & L16 (17\%) & .628 & .622 & $-$.006 \\
644	Qwen3  & L52 (55\%) & .738 & .734 & $-$.004 \\
645	Qwen3  & L80 (85\%) & .780 & .769 & $-$.011 \\
646	\bottomrule
647	\end{tabular}
648	\caption{Quantization validation (subset of layers). All $|\Delta\text{\auroc{}}| < 0.012$.}
649	\label{tab:quant}
650	\end{table}
651	
652	
653	% ============================================================
654	% 4.10 CAMERA-READY EXTENSIONS
655	% ============================================================
656	\subsection{Extended Evaluation (Camera-Ready)}
657	\label{sec:extensions}
658	
659	\paragraph{Third Architecture: Gemma~4 31B Dense.}
660	Adding a dense architecture (60 layers, FP16) confirms that our findings are not MoE-specific (Table~\ref{tab:three_arch}). Gemma~4's Pareto strength is intermediate (13/20 significant languages), and the Simpson's Paradox partial correlation is significant ($\rho=0.22$, $p=0.045$)---making it 2/3 architectures with significant positive partial CKA--transfer correlation after depth control. The CKA gradient slope ($-0.012$/layer) is the most gradual, consistent with the absence of expert routing that accelerates language specialization in MoE models.
661	
662	\begin{table}[t]
663	\centering
664	\small
665	\begin{tabular}{lccc}
666	\toprule
667	Metric & Qwen3 & Llama4 & Gemma4 \\
668	\midrule
669	Type & MoE & MoE & Dense \\
670	Active params & 22B & 17B & 31B \\
671	EN \auroc{} & 0.78 & 0.76 & 0.77 \\
672	ZS \auroc{} & 0.660 & 0.643 & 0.655 \\
673	Pareto sig.\ langs & 15 & 11 & 13 \\
674	Partial $\rho$ (CKA) & 0.16 & 0.29** & 0.22* \\
675	CKA slope & $-$0.025 & $-$0.015 & $-$0.012 \\
676	\bottomrule
677	\end{tabular}
678	\caption{Three-architecture comparison. Gemma~4 Dense provides intermediate Pareto strength and significant Simpson's Paradox reversal. *$p<0.05$, **$p<0.02$.}
679	\label{tab:three_arch}
680	\end{table}
681	
682	\paragraph{Extended Language Coverage.}
683	Expanding from 20 to 52 languages (Table~\ref{tab:52lang}) confirms the resource-tier gradient. Very-low-resource languages ($<$1M training tokens) show 48\% artifact rates and mean zero-shot \auroc{} of 0.52, close to chance. The 20-language rankings are highly stable ($\rho=0.94$ with 52-language rankings). Core findings are unchanged; the expansion primarily increases coverage and statistical power.
684	
685	\begin{table}[t]
686	\centering
687	\small
688	\begin{tabular}{lcccc}
689	\toprule
690	Tier & $n_{20}$ & $n_{52}$ & ZS \auroc{} & Art.\ rate \\
691	\midrule
692	\textsc{high} & 6 & 8 & 0.72 & 4\% \\
693	\textsc{mid}  & 8 & 14 & 0.66 & 22\% \\
694	\textsc{low}  & 6 & 18 & 0.57 & 35\% \\
695	\textsc{v-low} & 0 & 12 & 0.52 & 48\% \\
696	\bottomrule
697	\end{tabular}
698	\caption{Language coverage expansion. Very-low-resource languages have near-chance probing with high artifact rates.}
699	\label{tab:52lang}
700	\end{table}
701	
702	
703	% ============================================================
704	% 5. DISCUSSION
705	% ============================================================
706	\section{Discussion}
707	
708	\paragraph{Why Does MMD Fail While Linear Projection Succeeds?}
709	The correctness direction occupies a low-dimensional subspace (${\sim}1$--3 dimensions) of the high-dimensional activation space. MMD operates on scalar probe logits---it can match the marginal distribution (mean and variance) of these logits but is blind to the direction of the underlying correctness subspace. Two languages can have identical logit distributions (low MMD) with completely different correctness directions (large subspace angle). Linear projection, by contrast, directly learns the rotation matrix mapping one subspace onto another, which is why it succeeds even with few parallel examples. This distinction has implications beyond our setting: distributional matching is likely insufficient for any probing transfer task where the relevant signal occupies a low-dimensional subspace that differs between source and target domains.
710	
711	\paragraph{Architecture Dependence.}
712	We observe consistent differences between architectures across multiple analyses: Pareto strength, Simpson's Paradox significance, CKA gradient shape, and language-specific transfer patterns. These differences are observational ($n=2$--3 architectures confounded by scale, layer count, training data, and MoE vs.\ dense). We do not make causal attributions to specific architectural features, but note that expert routing in MoE architectures correlates with steeper language specialization in deep layers.
713	
714	\paragraph{Limitations.}
715	Our evaluation is limited to MCQA benchmarks, chosen because they enable clean correctness labeling and parallel multilingual evaluation. Whether these findings generalize to open-ended generation tasks remains an open question. The Procrustes reversal threshold (${\sim}0.55$) is estimated from $n=20$ languages with wide confidence interval $[0.46, 0.63]$; practitioners should validate on their target language before adopting fixed thresholds. The decomposition analysis (Section~\ref{sec:decomposition}) achieves only 58\% prescriptive accuracy; its value is descriptive, not predictive.
716	
717	
718	% ============================================================
719	% 6. CONCLUSION
720	% ============================================================
721	\section{Conclusion}
722	
723	We present the first large-scale study of cross-lingual correctness probe transfer, evaluating two (core) to three (extended) architectures across 20--52 languages. Three practical recommendations emerge: \textbf{(1)} use linear projection with ${\sim}70$ parallel pairs for languages with zero-shot \auroc{}$<0.55$; \textbf{(2)} use the zero-shot probe directly for languages with \auroc{}$>0.62$; \textbf{(3)} include Hewitt \& Liang selectivity checks when probing low-resource languages, as ${\sim}30\%$ of results may be capacity artifacts.
724	
725	As a systematic negative result, we close the MMD distributional-matching path for correctness probe transfer: CaCLR's consistency loss is inert across a full hyperparameter sweep, and CKA subspace analysis provides a geometric explanation grounded in Zhao et al.'s conditional-marginal mismatch theory. The Simpson's Paradox in CKA--transfer correlation---negative raw, positive partial---demonstrates that CKA provides genuine geometric insight into when transfer works, contingent on architecture.
726	
727	This work establishes that the probe-based calibration research line \emph{can} extend beyond English, but requires architecture-aware layer selection and, for low-resource languages, lightweight geometric alignment rather than distributional matching.
728	
729	
730	% ============================================================
731	% REFERENCES
732	% ============================================================
733	\begin{thebibliography}{30}
734	
735	\bibitem[\protect\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}
736	Anastasios~N. Angelopoulos and Stephen Bates.
737	\newblock 2023.
738	\newblock Conformal prediction: A gentle introduction.
739	\newblock {\em Foundations and Trends in Machine Learning}.
740	
741	\bibitem[\protect\citename{Artetxe et~al.}2018]{artetxe2018robust}
742	Mikel Artetxe, Gorka Labaka, and Eneko Agirre.
743	\newblock 2018.
744	\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.
745	\newblock In {\em Proc. ACL}.
746	
747	\bibitem[\protect\citename{Ben-David et~al.}2010]{bendavid2010theory}
748	Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan.
749	\newblock 2010.
750	\newblock A theory of learning from different domains.
751	\newblock {\em Machine Learning}, 79:151--175.
752	
753	\bibitem[\protect\citename{Conneau et~al.}2018]{conneau2018word}
754	Alexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\'e} J{\'e}gou.
755	\newblock 2018.
756	\newblock Word translation without parallel data.
757	\newblock In {\em Proc. ICLR}.
758	
759	\bibitem[\protect\citename{Guo et~al.}2017]{guo2017calibration}
760	Chuan Guo, Geoff Pleiss, Yu~Sun, and Kilian~Q. Weinberger.
761	\newblock 2017.
762	\newblock On calibration of modern neural networks.
763	\newblock In {\em Proc. ICML}.
764	
765	\bibitem[\protect\citename{Hewitt and Liang}2019]{hewitt2019designing}
766	John Hewitt and Percy Liang.
767	\newblock 2019.
768	\newblock Designing and interpreting probes with control tasks.
769	\newblock In {\em Proc. EMNLP}.
770	
771	\bibitem[\protect\citename{Ji et~al.}2024]{ji2024llm}
772	Jiaxin Ji, Kaiyuan Zhang, et~al.
773	\newblock 2024.
774	\newblock LLM internal states reveal hallucination risk straightforwardly.
775	\newblock {\em arXiv preprint}.
776	
777	\bibitem[\protect\citename{Joshi et~al.}2024]{joshi2024llm}
778	Radhika Joshi, Xinyi Wang, et~al.
779	\newblock 2024.
780	\newblock Are multilingual LLMs calibrated?
781	\newblock In {\em Proc. EMNLP}.
782	
783	\bibitem[\protect\citename{Kornblith et~al.}2019]{kornblith2019similarity}
784	Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton.
785	\newblock 2019.
786	\newblock Similarity of neural network representations revisited.
787	\newblock In {\em Proc. ICML}.
788	
789	\bibitem[\protect\citename{Miao et~al.}2026a]{miao2026coral}
790	Qingyi Miao, et~al.
791	\newblock 2026a.
792	\newblock CORAL: Cross-task correctness probes for LLM calibration.
793	\newblock {\em arXiv preprint}.
794	
795	\bibitem[\protect\citename{Miao and Ungar}2026]{miao2026steering}
796	Qingyi Miao and Lyle Ungar.
797	\newblock 2026.
798	\newblock Steering LLM calibration with orthogonal correctness directions.
799	\newblock {\em arXiv preprint}.
800	
801	\bibitem[\protect\citename{Raghu et~al.}2017]{raghu2017svcca}
802	Maithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein.
803	\newblock 2017.
804	\newblock SVCCA: Singular vector canonical correlation analysis.
805	\newblock In {\em Proc. NeurIPS}.
806	
807	\bibitem[\protect\citename{Voita and Titov}2020]{voita2020information}
808	Elena Voita and Ivan Titov.
809	\newblock 2020.
810	\newblock Information-theoretic probing with minimum description length.
811	\newblock In {\em Proc. EMNLP}.
812	
813	\bibitem[\protect\citename{Xiao et~al.}2025]{xiao2025knowledge}
814	Shiyuan Xiao, et~al.
815	\newblock 2025.
816	\newblock Cross-lingual knowledge boundary probes.
817	\newblock In {\em Proc. ACL}.
818	
819	\bibitem[\protect\citename{Zhao et~al.}2019]{zhao2019learning}
820	Han Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon.
821	\newblock 2019.
822	\newblock On learning invariant representations for domain adaptation.
823	\newblock In {\em Proc. ICML}.
824	
825	\bibitem[\protect\citename{Zhou et~al.}2024]{zhou2024lace}
826	Kaitlyn Zhou, et~al.
827	\newblock 2024.
828	\newblock LACE: Layer-aware calibration ensembles.
829	\newblock {\em arXiv preprint}.
830	
831	\end{thebibliography}
832	
833	\end{document}
834	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b25755c6-e461-4bbd-82d4-2bb902f8a5c7",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "c84c5e22-6283-49f9-b2e1-7ee71874f3e0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
      "content": "50  & $+$0.007 & $+$0.026 & $+$0.054 & $+$0.027 \\\\\n100 & $+$0.008 & $+$0.029 & $+$0.060 & $+$0.030 \\\\\n200 & $+$0.008 & $+$0.030 & $+$0.063 & $+$0.032 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Saturation curves: $\\Delta$\\auroc{} from linear projection by number of parallel pairs and resource tier (Qwen3-235B, L68). \\textsc{low} languages benefit most but need more pairs.}\n\\label{tab:saturation}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nZS \\auroc{} band & $n$ & Mean $\\Delta$ & \\% pos.\\ & Example \\\\\n\\midrule\n$<0.50$      & 4 & $+$0.058 & 100\\% & am, yo \\\\\n$0.50$--$0.55$ & 2 & $+$0.035 & 100\\% & sw, bn \\\\\n$0.55$--$0.60$ & 2 & $+$0.012 & 75\\%  & th, tr \\\\\n$0.60$--$0.65$ & 4 & $+$0.003 & 50\\%  & hi, ko \\\\\n$0.65$--$0.70$ & 4 & $-$0.008 & 25\\%  & ru, ja \\\\\n$>0.70$      & 4 & $-$0.018 & 0\\%   & zh, es \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Procrustes effect reversal. Linear projection helps misaligned languages (low ZS \\auroc{}) but hurts already well-aligned ones. Threshold ${\\sim}0.55$ (CI $[0.46, 0.63]$).}\n\\label{tab:procrustes}\n\\end{table}\n\n\n% ============================================================\n% 4.7 DIFFICULTY DECOMPOSITION\n% ============================================================\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n\nTable~\\ref{tab:decomposition} reports the decomposition results across 10 representative languages. Projecting out the IRT difficulty direction yields a mean $\\Delta$\\auroc{} of $+0.012$ (7/10 languages positive), compared to $+0.005$ for a random-direction control (difficulty-specific effect $\\approx 2.4\\times$ the random baseline). The difficulty probe achieves $R^2=0.35$, indicating that the difficulty direction captures roughly a third of the relevant variance.\n\nDescriptive separation is observed: the correctness signal does contain a difficulty-shared component that, when removed, modestly improves cross-lingual transfer for most languages. However, the prescriptive accuracy---whether the decomposition predicts the optimal alignment strategy---is only 58\\%, barely above chance (50\\%). We therefore report this as \\emph{descriptive separation observed in most language--architecture combinations; the decomposition does not reliably predict optimal alignment strategy.}\n\nTwo languages show negative $\\Delta$\\auroc{} after projection: ko ($-0.005$) and sw ($-0.008$). In these cases, difficulty and capability components are more entangled, and projection removes useful capability information alongside difficulty.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nLang & Tier & Full & Proj & $\\Delta$ & Rand & R.$\\Delta$ \\\\\n\\midrule\nzh & H & .725 & .733 & $+$.008 & .729 & $+$.004 \\\\\nes & H & .735 & .745 & $+$.010 & .740 & $+$.005 \\\\\nfr & H & .732 & .744 & $+$.012 & .737 & $+$.005 \\\\\nde & H & .715 & .730 & $+$.015 & .721 & $+$.006 \\\\\nhi & M & .658 & .680 & $+$.022 & .665 & $+$.007 \\\\\nru & M & .695 & .713 & $+$.018 & .702 & $+$.007 \\\\\nko & M & .680 & .675 & $-$.005 & .683 & $+$.003 \\\\\ntr & M & .650 & .670 & $+$.020 & .656 & $+$.006 \\\\\nsw & L & .585 & .577 & $-$.008 & .588 & $+$.003 \\\\\nbn & L & .602 & .627 & $+$.025 & .608 & $+$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Difficulty decomposition (Qwen3-235B, 8-layer mean). ``Proj'': \\auroc{} after projecting out difficulty direction. ``Rand'': random-direction control. Difficulty-specific effect is ${\\sim}2.4\\times$ random.}\n\\label{tab:decomposition}\n\\end{table}\n\n\n% ============================================================\n% 4.8 PROBING CONTROL TASKS\n% ============================================================\n\\subsection{Probing Control Tasks}\n\\label{sec:control}\n\nWe apply Hewitt \\& Liang's \\citeyearpar{hewitt2019designing} control task methodology: train probes on randomly permuted labels and compute selectivity (real $-$ control \\auroc{}). Table~\\ref{tab:artifact} reports artifact rates (selectivity $<0.05$) by resource tier and depth zone; Table~\\ref{tab:selectivity} shows per-language selectivity at the English-optimal layer.\n\n\\paragraph{Finding.}\nApproximately 30\\% of \\textsc{low}-resource and 28\\% of \\textsc{mid}-resource language--layer combinations fall below the selectivity threshold of 0.05, meaning the probe's above-chance performance reflects model capacity rather than a genuine correctness signal. \\textsc{high}-resource languages have only 6\\% artifact rate (confined to the shallowest layers). Artifacts concentrate in shallow layers: at 0--25\\% depth, 83\\% of \\textsc{low}-resource probes are artifacts, dropping to 0\\% at 75--100\\% depth.\n\nAt the English-optimal layer (L80), yo (selectivity $=0.032$) and am (selectivity $=0.018$) are flagged as artifacts. All main results are verified to be robust after filtering these combinations---conclusions are unchanged.\n\n\\textbf{Field-level implication:} This is the first application of probing control tasks to cross-lingual transfer. Given that ${\\sim}30\\%$ of low-resource results are unreliable, all cross-lingual probing studies should include selectivity checks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDepth & \\textsc{high} & \\textsc{mid} & \\textsc{low} \\\\\n\\midrule\n0--25\\%   & 17\\% & 58\\% & 83\\% \\\\\n25--50\\%  & 4\\%  & 33\\% & 67\\% \\\\\n50--75\\%  & 0\\%  & 17\\% & 17\\% \\\\\n75--100\\% & 0\\%  & 4\\%  & 0\\% \\\\\n\\midrule\nOverall   & 6\\%  & 28\\% & 30\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Artifact rate (selectivity $<0.05$) by resource tier and depth zone on Qwen3-235B. Low-resource shallow probes are unreliable.}\n\\label{tab:artifact}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nTier & Lang & Real & Ctrl & Sel. & Art.? \\\\\n\\midrule\nHIGH & zh & .732 & .498 & .234 & No \\\\\nHIGH & es & .741 & .495 & .246 & No \\\\\nMID  & hi & .665 & .502 & .163 & No \\\\\nMID  & tr & .655 & .508 & .147 & No \\\\\nLOW  & sw & .592 & .505 & .087 & No \\\\\nLOW  & bn & .608 & .501 & .107 & No \\\\\nLOW  & yo & .542 & .510 & .032 & Yes \\\\\nLOW  & am & .530 & .512 & .018 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selectivity at the English-optimal layer (L80). yo and am fall below the 0.05 threshold.}\n\\label{tab:selectivity}\n\\end{table}\n\n\n% ============================================================\n% 4.9 ADDITIONAL ANALYSES\n% ============================================================\n\\subsection{Supporting Analyses}\n\n\\subsubsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\nMiao \\& Ungar \\citeyearpar{miao2026steering} report cosine similarity $<0.04$ between correctness and verbalized-confidence directions in English. We extend this to 20 languages and two architectures. The orthogonality is robust: mean cosine is 0.038 across all languages, with 18/20 below 0.10 and 14/20 below 0.05 (Table~\\ref{tab:orthogonality}). \\textsc{high}-resource languages closely replicate the English finding (mean $=0.028$); \\textsc{low}-resource languages show slightly higher cosine (mean $=0.072$) due to noisier confidence directions. Two outliers (am: 0.142, yo: 0.118) coincide with the control-task artifacts identified in Section~\\ref{sec:control}, suggesting probe capacity issues rather than genuine alignment.\n\nArchitecture differences are minimal (Qwen3: 0.035, Llama~4: 0.041, not significant). The structural limitation of output-based calibration---that correctness and confidence are orthogonal---holds across languages.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nTier & $n$ & Mean & Std & Min & Max & $<$0.05 \\\\\n\\midrule\n\\textsc{high} & 6 & 0.028 & 0.012 & 0.012 & 0.045 & 5 \\\\\n\\textsc{mid}  & 8 & 0.042 & 0.018 & 0.018 & 0.075 & 5 \\\\\n\\textsc{low}  & 6 & 0.072 & 0.042 & 0.025 & 0.142 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cosine similarity between correctness and confidence directions by resource tier. Orthogonality persists cross-lingually.}\n\\label{tab:orthogonality}\n\\end{table}\n\n\n\\subsubsection{Probe Complexity: LR vs.\\ MLP}\n\\label{sec:probe_complexity}\n\nTable~\\ref{tab:lr_mlp} compares logistic regression and 2-layer MLP probes. MLPs achieve ${\\sim}2$pp higher English \\auroc{} but suffer ${\\sim}5$pp larger transfer gaps. MLP's additional capacity fits English-specific patterns (token position biases, language-specific syntactic cues) that do not transfer. Zero-shot pass rate drops from 75\\% (LR) to 60\\% (MLP) on Qwen3. This validates our choice of LR probes for cross-lingual transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Q3-LR & Q3-MLP & L4-LR & L4-MLP \\\\\n\\midrule\nEN \\auroc{} & .780 & .802 & .760 & .778 \\\\\nZS \\auroc{} & .660 & .632 & .643 & .618 \\\\\nGap & .120 & .170 & .117 & .160 \\\\\nZS pass & 75\\% & 60\\% & 70\\% & 55\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LR vs.\\ 2-layer MLP probes (mean over 20 languages). MLP's extra capacity helps English but hurts transfer.}\n\\label{tab:lr_mlp}\n\\end{table}\n\n\n\\subsubsection{Cross-Benchmark Generalization}\n\\label{sec:benchmarks}\n\nTable~\\ref{tab:benchmarks} evaluates probes on Belebele (reading comprehension) and MMLU-ProX (translated MMLU). The Pareto frontier, CaCLR ineffectiveness, and linear projection effectiveness all generalize. Belebele shows weaker Pareto (12/20 significant languages vs.\\ 15/20 on GlobalMMLU), expected given the different task type (passage comprehension vs.\\ parametric knowledge). Language rankings are highly correlated across benchmarks ($\\rho=0.88$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & GlobalMMLU & Belebele & MMLU-ProX \\\\\n\\midrule\nEN \\auroc{} & 0.78 & 0.74 & 0.77 \\\\\nZS \\auroc{} & 0.660 & 0.625 & 0.648 \\\\\nZS pass rate & 75\\% & 60\\% & 70\\% \\\\\nPareto langs & 15 & 12 & 14 \\\\\nProj $\\Delta$ & $+$0.032 & $+$0.028 & $+$0.030 \\\\\nCaCLR $\\Delta$ & $+$0.002 & $+$0.001 & $+$0.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (Qwen3-235B, 20 languages). Key findings hold across benchmarks.}\n\\label{tab:benchmarks}\n\\end{table}\n\n\n\\subsubsection{Quantization Validation}\n\\label{sec:quant}\n\nTable~\\ref{tab:quant} compares \\auroc{} between quantized (INT4/W4A16) and FP16 inference at five representative layers per model. Mean $|\\Delta$\\auroc{}$|$ is 0.005 (Llama~4) and 0.006 (Qwen3), with maximum 0.011. CKA between quantized and FP16 activations exceeds 0.97 for both models. Quantization artifacts are negligible for correctness probing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Layer & FP16 & Quant & $\\Delta$ \\\\\n\\midrule\nLlama4 & L8 (17\\%)  & .632 & .629 & $-$.003 \\\\\nLlama4 & L24 (50\\%) & .720 & .715 & $-$.005 \\\\\nLlama4 & L44 (92\\%) & .760 & .762 & $+$.002 \\\\\nQwen3  & L16 (17\\%) & .628 & .622 & $-$.006 \\\\\nQwen3  & L52 (55\\%) & .738 & .734 & $-$.004 \\\\\nQwen3  & L80 (85\\%) & .780 & .769 & $-$.011 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quantization validation (subset of layers). All $|\\Delta\\text{\\auroc{}}| < 0.012$.}\n\\label{tab:quant}\n\\end{table}\n\n\n% ============================================================\n% 4.10 CAMERA-READY EXTENSIONS\n% ============================================================\n\\subsection{Extended Evaluation (Camera-Ready)}\n\\label{sec:extensions}\n\n\\paragraph{Third Architecture: Gemma~4 31B Dense.}\nAdding a dense architecture (60 layers, FP16) confirms that our findings are not MoE-specific (Table~\\ref{tab:three_arch}). Gemma~4's Pareto strength is intermediate (13/20 significant languages), and the Simpson's Paradox partial correlation is significant ($\\rho=0.22$, $p=0.045$)---making it 2/3 architectures with significant positive partial CKA--transfer correlation after depth control. The CKA gradient slope ($-0.012$/layer) is the most gradual, consistent with the absence of expert routing that accelerates language specialization in MoE models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen3 & Llama4 & Gemma4 \\\\\n\\midrule\nType & MoE & MoE & Dense \\\\\nActive params & 22B & 17B & 31B \\\\\nEN \\auroc{} & 0.78 & 0.76 & 0.77 \\\\\nZS \\auroc{} & 0.660 & 0.643 & 0.655 \\\\\nPareto sig.\\ langs & 15 & 11 & 13 \\\\\nPartial $\\rho$ (CKA) & 0.16 & 0.29** & 0.22* \\\\\nCKA slope & $-$0.025 & $-$0.015 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-architecture comparison. Gemma~4 Dense provides intermediate Pareto strength and significant Simpson's Paradox reversal. *$p<0.05$, **$p<0.02$.}\n\\label{tab:three_arch}\n\\end{table}\n\n\\paragraph{Extended Language Coverage.}\nExpanding from 20 to 52 languages (Table~\\ref{tab:52lang}) confirms the resource-tier gradient. Very-low-resource languages ($<$1M training tokens) show 48\\% artifact rates and mean zero-shot \\auroc{} of 0.52, close to chance. The 20-language rankings are highly stable ($\\rho=0.94$ with 52-language rankings). Core findings are unchanged; the expansion primarily increases coverage and statistical power.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n_{20}$ & $n_{52}$ & ZS \\auroc{} & Art.\\ rate \\\\\n\\midrule\n\\textsc{high} & 6 & 8 & 0.72 & 4\\% \\\\\n\\textsc{mid}  & 8 & 14 & 0.66 & 22\\% \\\\\n\\textsc{low}  & 6 & 18 & 0.57 & 35\\% \\\\\n\\textsc{v-low} & 0 & 12 & 0.52 & 48\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Language coverage expansion. Very-low-resource languages have near-chance probing with high artifact rates.}\n\\label{tab:52lang}\n\\end{table}\n\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why Does MMD Fail While Linear Projection Succeeds?}\nThe correctness direction occupies a low-dimensional subspace (${\\sim}1$--3 dimensions) of the high-dimensional activation space. MMD operates on scalar probe logits---it can match the marginal distribution (mean and variance) of these logits but is blind to the direction of the underlying correctness subspace. Two languages can have identical logit distributions (low MMD) with completely different correctness directions (large subspace angle). Linear projection, by contrast, directly learns the rotation matrix mapping one subspace onto another, which is why it succeeds even with few parallel examples. This distinction has implications beyond our setting: distributional matching is likely insufficient for any probing transfer task where the relevant signal occupies a low-dimensional subspace that differs between source and target domains.\n\n\\paragraph{Architecture Dependence.}\nWe observe consistent differences between architectures across multiple analyses: Pareto strength, Simpson's Paradox significance, CKA gradient shape, and language-specific transfer patterns. These differences are observational ($n=2$--3 architectures confounded by scale, layer count, training data, and MoE vs.\\ dense). We do not make causal attributions to specific architectural features, but note that expert routing in MoE architectures correlates with steeper language specialization in deep layers.\n\n\\paragraph{Limitations.}\nOur evaluation is limited to MCQA benchmarks, chosen because they enable clean correctness labeling and parallel multilingual evaluation. Whether these findings generalize to open-ended generation tasks remains an open question. The Procrustes reversal threshold (${\\sim}0.55$) is estimated from $n=20$ languages with wide confidence interval $[0.46, 0.63]$; practitioners should validate on their target language before adopting fixed thresholds. The decomposition analysis (Section~\\ref{sec:decomposition}) achieves only 58\\% prescriptive accuracy; its value is descriptive, not predictive.\n\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe present the first large-scale study of cross-lingual correctness probe transfer, evaluating two (core) to three (extended) architectures across 20--52 languages. Three practical recommendations emerge: \\textbf{(1)} use linear projection with ${\\sim}70$ parallel pairs for languages with zero-shot \\auroc{}$<0.55$; \\textbf{(2)} use the zero-shot probe directly for languages with \\auroc{}$>0.62$; \\textbf{(3)} include Hewitt \\& Liang selectivity checks when probing low-resource languages, as ${\\sim}30\\%$ of results may be capacity artifacts.\n\nAs a systematic negative result, we close the MMD distributional-matching path for correctness probe transfer: CaCLR's consistency loss is inert across a full hyperparameter sweep, and CKA subspace analysis provides a geometric explanation grounded in Zhao et al.'s conditional-marginal mismatch theory. The Simpson's Paradox in CKA--transfer correlation---negative raw, positive partial---demonstrates that CKA provides genuine geometric insight into when transfer works, contingent on architecture.\n\nThis work establishes that the probe-based calibration research line \\emph{can} extend beyond English, but requires architecture-aware layer selection and, for low-resource languages, lightweight geometric alignment rather than distributional matching.\n\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates.\n\\newblock 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre.\n\\newblock 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc. ACL}.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan.\n\\newblock 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou.\n\\newblock 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc. ICLR}.\n\n\\bibitem[\\protect\\citename{Guo et~al.}2017]{guo2017calibration}\nChuan Guo, Geoff Pleiss, Yu~Sun, and Kilian~Q. Weinberger.\n\\newblock 2017.\n\\newblock On calibration of modern neural networks.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}\nJohn Hewitt and Percy Liang.\n\\newblock 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Ji et~al.}2024]{ji2024llm}\nJiaxin Ji, Kaiyuan Zhang, et~al.\n\\newblock 2024.\n\\newblock LLM internal states reveal hallucination risk straightforwardly.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Joshi et~al.}2024]{joshi2024llm}\nRadhika Joshi, Xinyi Wang, et~al.\n\\newblock 2024.\n\\newblock Are multilingual LLMs calibrated?\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton.\n\\newblock 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nQingyi Miao, et~al.\n\\newblock 2026a.\n\\newblock CORAL: Cross-task correctness probes for LLM calibration.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026steering}\nQingyi Miao and Lyle Ungar.\n\\newblock 2026.\n\\newblock Steering LLM calibration with orthogonal correctness directions.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Raghu et~al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein.\n\\newblock 2017.\n\\newblock SVCCA: Singular vector canonical correlation analysis.\n\\newblock In {\\em Proc. NeurIPS}.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020information}\nElena Voita and Ivan Titov.\n\\newblock 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}\nShiyuan Xiao, et~al.\n\\newblock 2025.\n\\newblock Cross-lingual knowledge boundary probes.\n\\newblock In {\\em Proc. ACL}.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon.\n\\newblock 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2024]{zhou2024lace}\nKaitlyn Zhou, et~al.\n\\newblock 2024.\n\\newblock LACE: Layer-aware calibration ensembles.\n\\newblock {\\em arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
      "numLines": 405,
      "startLine": 430,
      "totalLines": 834
    }
  },
  "sourceToolAssistantUUID": "b25755c6-e461-4bbd-82d4-2bb902f8a5c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "c84c5e22-6283-49f9-b2e1-7ee71874f3e0",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration empirical study paper",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Assistant

_source line 48 · 2026-05-21T05:42:29.749Z_

<details><summary>Logged reasoning block</summary>

```text
The `\protect\citename` is an ACL-specific command. With natbib, I need to change the bibitem format. Let me replace all the bibitems to use natbib-compatible format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c84c5e22-6283-49f9-b2e1-7ee71874f3e0",
  "isSidechain": false,
  "requestId": "req_011CbFBQsk4sqaM1cCWs6UTE",
  "type": "assistant",
  "uuid": "23622ace-3b25-437b-b6c1-8da16d3d2220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoVNU18ye7uWXp2v7pbCsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8320,
      "cache_read_input_tokens": 70693,
      "output_tokens": 2995,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2995,
          "cache_read_input_tokens": 70693,
          "cache_creation_input_tokens": 8320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8320
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

_source line 49 · 2026-05-21T05:42:30.312Z_

The `\protect\citename` format is ACL-specific. Let me replace the bibliography section with natbib-compatible format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23622ace-3b25-437b-b6c1-8da16d3d2220",
  "isSidechain": false,
  "requestId": "req_011CbFBQsk4sqaM1cCWs6UTE",
  "type": "assistant",
  "uuid": "20e58109-39f3-4b27-8ccb-a815b14a803a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoVNU18ye7uWXp2v7pbCsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8320,
      "cache_read_input_tokens": 70693,
      "output_tokens": 2995,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2995,
          "cache_read_input_tokens": 70693,
          "cache_creation_input_tokens": 8320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8320
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

_source line 50 · 2026-05-21T05:42:53.936Z_

<details open><summary>🔧 Tool call — Edit · `toolu_018mWenXNHVPUkFUb2HBioCm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
  "old_string": "\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates.\n\\newblock 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre.\n\\newblock 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc. ACL}.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan.\n\\newblock 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou.\n\\newblock 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc. ICLR}.\n\n\\bibitem[\\protect\\citename{Guo et~al.}2017]{guo2017calibration}\nChuan Guo, Geoff Pleiss, Yu~Sun, and Kilian~Q. Weinberger.\n\\newblock 2017.\n\\newblock On calibration of modern neural networks.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}\nJohn Hewitt and Percy Liang.\n\\newblock 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Ji et~al.}2024]{ji2024llm}\nJiaxin Ji, Kaiyuan Zhang, et~al.\n\\newblock 2024.\n\\newblock LLM internal states reveal hallucination risk straightforwardly.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Joshi et~al.}2024]{joshi2024llm}\nRadhika Joshi, Xinyi Wang, et~al.\n\\newblock 2024.\n\\newblock Are multilingual LLMs calibrated?\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton.\n\\newblock 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nQingyi Miao, et~al.\n\\newblock 2026a.\n\\newblock CORAL: Cross-task correctness probes for LLM calibration.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026steering}\nQingyi Miao and Lyle Ungar.\n\\newblock 2026.\n\\newblock Steering LLM calibration with orthogonal correctness directions.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Raghu et~al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein.\n\\newblock 2017.\n\\newblock SVCCA: Singular vector canonical correlation analysis.\n\\newblock In {\\em Proc. NeurIPS}.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020information}\nElena Voita and Ivan Titov.\n\\newblock 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}\nShiyuan Xiao, et~al.\n\\newblock 2025.\n\\newblock Cross-lingual knowledge boundary probes.\n\\newblock In {\\em Proc. ACL}.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon.\n\\newblock 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2024]{zhou2024lace}\nKaitlyn Zhou, et~al.\n\\newblock 2024.\n\\newblock LACE: Layer-aware calibration ensembles.\n\\newblock {\\em arXiv preprint}.\n\n\\end{thebibliography}",
  "new_string": "\\begin{thebibliography}{16}\n\n\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}, 2023.\n\n\\bibitem[Artetxe et~al.(2018)]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc. ACL}, 2018.\n\n\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175, 2010.\n\n\\bibitem[Conneau et~al.(2018)]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc. ICLR}, 2018.\n\n\\bibitem[Guo et~al.(2017)]{guo2017calibration}\nChuan Guo, Geoff Pleiss, Yu~Sun, and Kilian~Q. Weinberger.\n\\newblock On calibration of modern neural networks.\n\\newblock In {\\em Proc. ICML}, 2017.\n\n\\bibitem[Hewitt and Liang(2019)]{hewitt2019designing}\nJohn Hewitt and Percy Liang.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc. EMNLP}, 2019.\n\n\\bibitem[Ji et~al.(2024)]{ji2024llm}\nJiaxin Ji, Kaiyuan Zhang, et~al.\n\\newblock {LLM} internal states reveal hallucination risk straightforwardly.\n\\newblock {\\em arXiv preprint}, 2024.\n\n\\bibitem[Joshi et~al.(2024)]{joshi2024llm}\nRadhika Joshi, Xinyi Wang, et~al.\n\\newblock Are multilingual {LLMs} calibrated?\n\\newblock In {\\em Proc. EMNLP}, 2024.\n\n\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc. ICML}, 2019.\n\n\\bibitem[Miao et~al.(2026a)]{miao2026coral}\nQingyi Miao, et~al.\n\\newblock {CORAL}: Cross-task correctness probes for {LLM} calibration.\n\\newblock {\\em arXiv preprint}, 2026.\n\n\\bibitem[Miao and Ungar(2026)]{miao2026steering}\nQingyi Miao and Lyle Ungar.\n\\newblock Steering {LLM} calibration with orthogonal correctness directions.\n\\newblock {\\em arXiv preprint}, 2026.\n\n\\bibitem[Raghu et~al.(2017)]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis.\n\\newblock In {\\em Proc. NeurIPS}, 2017.\n\n\\bibitem[Voita and Titov(2020)]{voita2020information}\nElena Voita and Ivan Titov.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proc. EMNLP}, 2020.\n\n\\bibitem[Xiao et~al.(2025)]{xiao2025knowledge}\nShiyuan Xiao, et~al.\n\\newblock Cross-lingual knowledge boundary probes.\n\\newblock In {\\em Proc. ACL}, 2025.\n\n\\bibitem[Zhao et~al.(2019)]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc. ICML}, 2019.\n\n\\bibitem[Zhou et~al.(2024)]{zhou2024lace}\nKaitlyn Zhou, et~al.\n\\newblock {LACE}: Layer-aware calibration ensembles.\n\\newblock {\\em arXiv preprint}, 2024.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20e58109-39f3-4b27-8ccb-a815b14a803a",
  "isSidechain": false,
  "requestId": "req_011CbFBQsk4sqaM1cCWs6UTE",
  "type": "assistant",
  "uuid": "889c9f0d-3e19-4b48-8e0b-d048262b3da4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoVNU18ye7uWXp2v7pbCsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8320,
      "cache_read_input_tokens": 70693,
      "output_tokens": 2995,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2995,
          "cache_read_input_tokens": 70693,
          "cache_creation_input_tokens": 8320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8320
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

_source line 51 · 2026-05-21T05:42:53.956Z_

<details><summary>↩ Tool result · `toolu_018mWenXNHVPUkFUb2HBioCm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "889c9f0d-3e19-4b48-8e0b-d048262b3da4",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "06b34907-4c3e-483e-bb3e-035de15baa32",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.tex",
    "oldString": "\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates.\n\\newblock 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre.\n\\newblock 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc. ACL}.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan.\n\\newblock 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou.\n\\newblock 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc. ICLR}.\n\n\\bibitem[\\protect\\citename{Guo et~al.}2017]{guo2017calibration}\nChuan Guo, Geoff Pleiss, Yu~Sun, and Kilian~Q. Weinberger.\n\\newblock 2017.\n\\newblock On calibration of modern neural networks.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}\nJohn Hewitt and Percy Liang.\n\\newblock 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Ji et~al.}2024]{ji2024llm}\nJiaxin Ji, Kaiyuan Zhang, et~al.\n\\newblock 2024.\n\\newblock LLM internal states reveal hallucination risk straightforwardly.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Joshi et~al.}2024]{joshi2024llm}\nRadhika Joshi, Xinyi Wang, et~al.\n\\newblock 2024.\n\\newblock Are multilingual LLMs calibrated?\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton.\n\\newblock 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nQingyi Miao, et~al.\n\\newblock 2026a.\n\\newblock CORAL: Cross-task correctness probes for LLM calibration.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026steering}\nQingyi Miao and Lyle Ungar.\n\\newblock 2026.\n\\newblock Steering LLM calibration with orthogonal correctness directions.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Raghu et~al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein.\n\\newblock 2017.\n\\newblock SVCCA: Singular vector canonical correlation analysis.\n\\newblock In {\\em Proc. NeurIPS}.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020information}\nElena Voita and Ivan Titov.\n\\newblock 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proc. EMNLP}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}\nShiyuan Xiao, et~al.\n\\newblock 2025.\n\\newblock Cross-lingual knowledge boundary probes.\n\\newblock In {\\em Proc. ACL}.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon.\n\\newblock 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc. ICML}.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2024]{zhou2024lace}\nKaitlyn Zhou, et~al.\n\\newblock 2024.\n\\newblock LACE: Layer-aware calibration ensembles.\n\\newblock {\\em arXiv preprint}.\n\n\\end{thebibliography}",
    "newString": "\\begin{thebibliography}{16}\n\n\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}, 2023.\n\n\\bibitem[Artetxe et~al.(2018)]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc. ACL}, 2018.\n\n\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175, 2010.\n\n\\bibitem[Conneau et~al.(2018)]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc. ICLR}, 2018.\n\n\\bibitem[Guo et~al.(2017)]{guo2017calibration}\nChuan Guo, Geoff Pleiss, Yu~Sun, and Kilian~Q. Weinberger.\n\\newblock On calibration of modern neural networks.\n\\newblock In {\\em Proc. ICML}, 2017.\n\n\\bibitem[Hewitt and Liang(2019)]{hewitt2019designing}\nJohn Hewitt and Percy Liang.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc. EMNLP}, 2019.\n\n\\bibitem[Ji et~al.(2024)]{ji2024llm}\nJiaxin Ji, Kaiyuan Zhang, et~al.\n\\newblock {LLM} internal states reveal hallucination risk straightforwardly.\n\\newblock {\\em arXiv preprint}, 2024.\n\n\\bibitem[Joshi et~al.(2024)]{joshi2024llm}\nRadhika Joshi, Xinyi Wang, et~al.\n\\newblock Are multilingual {LLMs} calibrated?\n\\newblock In {\\em Proc. EMNLP}, 2024.\n\n\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc. ICML}, 2019.\n\n\\bibitem[Miao et~al.(2026a)]{miao2026coral}\nQingyi Miao, et~al.\n\\newblock {CORAL}: Cross-task correctness probes for {LLM} calibration.\n\\newblock {\\em arXiv preprint}, 2026.\n\n\\bibitem[Miao and Ungar(2026)]{miao2026steering}\nQingyi Miao and Lyle Ungar.\n\\newblock Steering {LLM} calibration with orthogonal correctness directions.\n\\newblock {\\em arXiv preprint}, 2026.\n\n\\bibitem[Raghu et~al.(2017)]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis.\n\\newblock In {\\em Proc. NeurIPS}, 2017.\n\n\\bibitem[Voita and Titov(2020)]{voita2020information}\nElena Voita and Ivan Titov.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proc. EMNLP}, 2020.\n\n\\bibitem[Xiao et~al.(2025)]{xiao2025knowledge}\nShiyuan Xiao, et~al.\n\\newblock Cross-lingual knowledge boundary probes.\n\\newblock In {\\em Proc. ACL}, 2025.\n\n\\bibitem[Zhao et~al.(2019)]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc. ICML}, 2019.\n\n\\bibitem[Zhou et~al.(2024)]{zhou2024lace}\nKaitlyn Zhou, et~al.\n\\newblock {LACE}: Layer-aware calibration ensembles.\n\\newblock {\\em arXiv preprint}, 2024.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 730,
        "oldLines": 103,
        "newStart": 730,
        "newLines": 87,
        "lines": [
          " % ============================================================",
          " % REFERENCES",
          " % ============================================================",
          "-\\begin{thebibliography}{30}",
          "+\\begin{thebibliography}{16}",
          " ",
          "-\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}",
          "+\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}",
          " Anastasios~N. Angelopoulos and Stephen Bates.",
          "-\\newblock 2023.",
          " \\newblock Conformal prediction: A gentle introduction.",
          "-\\newblock {\\em Foundations and Trends in Machine Learning}.",
          "+\\newblock {\\em Foundations and Trends in Machine Learning}, 2023.",
          " ",
          "-\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}",
          "+\\bibitem[Artetxe et~al.(2018)]{artetxe2018robust}",
          " Mikel Artetxe, Gorka Labaka, and Eneko Agirre.",
          "-\\newblock 2018.",
          " \\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.",
          "-\\newblock In {\\em Proc. ACL}.",
          "+\\newblock In {\\em Proc. ACL}, 2018.",
          " ",
          "-\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}",
          "+\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}",
          " Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan.",
          "-\\newblock 2010.",
          " \\newblock A theory of learning from different domains.",
          "-\\newblock {\\em Machine Learning}, 79:151--175.",
          "+\\newblock {\\em Machine Learning}, 79:151--175, 2010.",
          " ",
          "-\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}",
          "+\\bibitem[Conneau et~al.(2018)]{conneau2018word}",
          " Alexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou.",
          "-\\newblock 2018.",
          " \\newblock Word translation without parallel data.",
          "-\\newblock In {\\em Proc. ICLR}.",
          "+\\newblock In {\\em Proc. ICLR}, 2018.",
          " ",
          "-\\bibitem[\\protect\\citename{Guo et~al.}2017]{guo2017calibration}",
          "+\\bibitem[Guo et~al.(2017)]{guo2017calibration}",
          " Chuan Guo, Geoff Pleiss, Yu~Sun, and Kilian~Q. Weinberger.",
          "-\\newblock 2017.",
          " \\newblock On calibration of modern neural networks.",
          "-\\newblock In {\\em Proc. ICML}.",
          "+\\newblock In {\\em Proc. ICML}, 2017.",
          " ",
          "-\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}",
          "+\\bibitem[Hewitt and Liang(2019)]{hewitt2019designing}",
          " John Hewitt and Percy Liang.",
          "-\\newblock 2019.",
          " \\newblock Designing and interpreting probes with control tasks.",
          "-\\newblock In {\\em Proc. EMNLP}.",
          "+\\newblock In {\\em Proc. EMNLP}, 2019.",
          " ",
          "-\\bibitem[\\protect\\citename{Ji et~al.}2024]{ji2024llm}",
          "+\\bibitem[Ji et~al.(2024)]{ji2024llm}",
          " Jiaxin Ji, Kaiyuan Zhang, et~al.",
          "-\\newblock 2024.",
          "-\\newblock LLM internal states reveal hallucination risk straightforwardly.",
          "-\\newblock {\\em arXiv preprint}.",
          "+\\newblock {LLM} internal states reveal hallucination risk straightforwardly.",
          "+\\newblock {\\em arXiv preprint}, 2024.",
          " ",
          "-\\bibitem[\\protect\\citename{Joshi et~al.}2024]{joshi2024llm}",
          "+\\bibitem[Joshi et~al.(2024)]{joshi2024llm}",
          " Radhika Joshi, Xinyi Wang, et~al.",
          "-\\newblock 2024.",
          "-\\newblock Are multilingual LLMs calibrated?",
          "-\\newblock In {\\em Proc. EMNLP}.",
          "+\\newblock Are multilingual {LLMs} calibrated?",
          "+\\newblock In {\\em Proc. EMNLP}, 2024.",
          " ",
          "-\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}",
          "+\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}",
          " Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton.",
          "-\\newblock 2019.",
          " \\newblock Similarity of neural network representations revisited.",
          "-\\newblock In {\\em Proc. ICML}.",
          "+\\newblock In {\\em Proc. ICML}, 2019.",
          " ",
          "-\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}",
          "+\\bibitem[Miao et~al.(2026a)]{miao2026coral}",
          " Qingyi Miao, et~al.",
          "-\\newblock 2026a.",
          "-\\newblock CORAL: Cross-task correctness probes for LLM calibration.",
          "-\\newblock {\\em arXiv preprint}.",
          "+\\newblock {CORAL}: Cross-task correctness probes for {LLM} calibration.",
          "+\\newblock {\\em arXiv preprint}, 2026.",
          " ",
          "-\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026steering}",
          "+\\bibitem[Miao and Ungar(2026)]{miao2026steering}",
          " Qingyi Miao and Lyle Ungar.",
          "-\\newblock 2026.",
          "-\\newblock Steering LLM calibration with orthogonal correctness directions.",
          "-\\newblock {\\em arXiv preprint}.",
          "+\\newblock Steering {LLM} calibration with orthogonal correctness directions.",
          "+\\newblock {\\em arXiv preprint}, 2026.",
          " ",
          "-\\bibitem[\\protect\\citename{Raghu et~al.}2017]{raghu2017svcca}",
          "+\\bibitem[Raghu et~al.(2017)]{raghu2017svcca}",
          " Maithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein.",
          "-\\newblock 2017.",
          "-\\newblock SVCCA: Singular vector canonical correlation analysis.",
          "-\\newblock In {\\em Proc. NeurIPS}.",
          "+\\newblock {SVCCA}: Singular vector canonical correlation analysis.",
          "+\\newblock In {\\em Proc. NeurIPS}, 2017.",
          " ",
          "-\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020information}",
          "+\\bibitem[Voita and Titov(2020)]{voita2020information}",
          " Elena Voita and Ivan Titov.",
          "-\\newblock 2020.",
          " \\newblock Information-theoretic probing with minimum description length.",
          "-\\newblock In {\\em Proc. EMNLP}.",
          "+\\newblock In {\\em Proc. EMNLP}, 2020.",
          " ",
          "-\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}",
          "+\\bibitem[Xiao et~al.(2025)]{xiao2025knowledge}",
          " Shiyuan Xiao, et~al.",
          "-\\newblock 2025.",
          " \\newblock Cross-lingual knowledge boundary probes.",
          "-\\newblock In {\\em Proc. ACL}.",
          "+\\newblock In {\\em Proc. ACL}, 2025.",
          " ",
          "-\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}",
          "+\\bibitem[Zhao et~al.(2019)]{zhao2019learning}",
          " Han Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon.",
          "-\\newblock 2019.",
          " \\newblock On learning invariant representations for domain adaptation.",
          "-\\newblock In {\\em Proc. ICML}.",
          "+\\newblock In {\\em Proc. ICML}, 2019.",
          " ",
          "-\\bibitem[\\protect\\citename{Zhou et~al.}2024]{zhou2024lace}",
          "+\\bibitem[Zhou et~al.(2024)]{zhou2024lace}",
          " Kaitlyn Zhou, et~al.",
          "-\\newblock 2024.",
          "-\\newblock LACE: Layer-aware calibration ensembles.",
          "-\\newblock {\\em arXiv preprint}.",
          "+\\newblock {LACE}: Layer-aware calibration ensembles.",
          "+\\newblock {\\em arXiv preprint}, 2024.",
          " ",
          " \\end{thebibliography}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "889c9f0d-3e19-4b48-8e0b-d048262b3da4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 52 · 2026-05-21T05:42:53.961Z_

```json
{
  "parentUuid": "06b34907-4c3e-483e-bb3e-035de15baa32",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "be1a2b33-75e0-472c-aaf5-88a71234946b",
  "timestamp": "2026-05-21T05:42:53.961Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 53 · 2026-05-21T05:42:57.648Z_

Now let's compile again.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be1a2b33-75e0-472c-aaf5-88a71234946b",
  "isSidechain": false,
  "requestId": "req_011CbFBSwqvacjUsuHV8aQpw",
  "type": "assistant",
  "uuid": "c799245b-657b-4285-9eea-7d0968a1ab3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjH5ZAp9H9Fa9ijguUKA3J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3167,
      "cache_read_input_tokens": 79013,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3167,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 79013,
          "cache_creation_input_tokens": 3167,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3167
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

_source line 54 · 2026-05-21T05:42:58.595Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MaMcdwnozPJTofoFcX3io6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c799245b-657b-4285-9eea-7d0968a1ab3a",
  "isSidechain": false,
  "requestId": "req_011CbFBSwqvacjUsuHV8aQpw",
  "type": "assistant",
  "uuid": "f4cb8905-0950-482b-adeb-36896613b96e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjH5ZAp9H9Fa9ijguUKA3J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3167,
      "cache_read_input_tokens": 79013,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3167,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 79013,
          "cache_creation_input_tokens": 3167,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3167
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

_source line 55 · 2026-05-21T05:42:59.177Z_

<details><summary>↩ Tool result · `toolu_01MaMcdwnozPJTofoFcX3io6`</summary>

```text
 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.
pfb>
Output written on paper.pdf (14 pages, 213775 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4cb8905-0950-482b-adeb-36896613b96e",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "ddbcd6e8-4d85-4af8-b2bc-5ceed4744642",
  "toolUseResult": {
    "stdout": " )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.\npfb>\nOutput written on paper.pdf (14 pages, 213775 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f4cb8905-0950-482b-adeb-36896613b96e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "ddbcd6e8-4d85-4af8-b2bc-5ceed4744642",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration empirical study paper",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Assistant

_source line 58 · 2026-05-21T05:43:02.080Z_

First pass succeeded (14 pages). Running second pass for cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddbcd6e8-4d85-4af8-b2bc-5ceed4744642",
  "isSidechain": false,
  "requestId": "req_011CbFBTL3fHcXJaRNUXCCN8",
  "type": "assistant",
  "uuid": "fed660be-f19f-45be-aab4-f86b91a47534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFEkchCcoH5Mk2SW4ihEpz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 82180,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 82180,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 777
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

_source line 59 · 2026-05-21T05:43:02.691Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Bjxx67Bav4ampG7YVZzKJf`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fed660be-f19f-45be-aab4-f86b91a47534",
  "isSidechain": false,
  "requestId": "req_011CbFBTL3fHcXJaRNUXCCN8",
  "type": "assistant",
  "uuid": "b54f5a81-e573-4c91-87b1-19054e87f6f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFEkchCcoH5Mk2SW4ihEpz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 82180,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 82180,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 777
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

_source line 60 · 2026-05-21T05:43:03.290Z_

<details><summary>↩ Tool result · `toolu_01Bjxx67Bav4ampG7YVZzKJf`</summary>

```text
fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.
pfb>
Output written on paper.pdf (14 pages, 218031 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b54f5a81-e573-4c91-87b1-19054e87f6f8",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "2977ce90-71a7-4e20-8a90-a16ccd32fd3a",
  "toolUseResult": {
    "stdout": "fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.\npfb>\nOutput written on paper.pdf (14 pages, 218031 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b54f5a81-e573-4c91-87b1-19054e87f6f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T05:43:07.234Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YZ7UhabsVCoJnMW46Kx3dq`</summary>

```json
{
  "command": "grep -c \"Warning\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.log | head -1 && grep \"LaTeX Warning\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/paper.log | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2977ce90-71a7-4e20-8a90-a16ccd32fd3a",
  "isSidechain": false,
  "requestId": "req_011CbFBTdcLy8hLRHnsoDqk7",
  "type": "assistant",
  "uuid": "5a142dd8-3589-43a9-ac62-4dac9f9ff853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWSfHjEdKW7xkUoHdRd927",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 82957,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 82957,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 62 · 2026-05-21T05:43:07.298Z_

<details><summary>↩ Tool result · `toolu_01YZ7UhabsVCoJnMW46Kx3dq`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a142dd8-3589-43a9-ac62-4dac9f9ff853",
  "isSidechain": false,
  "promptId": "3d779f57-9b4e-4312-8e70-8eb8019121da",
  "type": "user",
  "uuid": "5b2e1576-8211-4747-bc86-9caa9389c667",
  "toolUseResult": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5a142dd8-3589-43a9-ac62-4dac9f9ff853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-21T05:43:18.850Z_

编译成功，0 warnings。PDF 14 页，写入 `paper.pdf`。

论文覆盖了 `experiment_data.json` 中全部 11 个实验：
- **§4.2** Pareto Frontier（Qwen3-235B + Llama 4 Scout，3 张表）
- **§4.3** CKA 分析 + Simpson's Paradox（4 张表）
- **§4.4** CaCLR 负面结果（β sweep + component ablation + subspace analysis，3 张表）
- **§4.5** Transfer 方法总对比（1 张表）
- **§4.6** Linear Projection 饱和曲线 + Procrustes 反转（2 张表）
- **§4.7** Difficulty 分解（1 张表）
- **§4.8** Probing Control Tasks（2 张表）
- **§4.9** 支撑分析：正交性、LR vs MLP、跨 benchmark 泛化、量化验证（4 张表）
- **§4.10** Camera-ready 扩展：Gemma 4 + 52 语言（2 张表）

所有数字均来自 `experiment_data.json`，标题按 narrative guidance 调整为负面结果框架，Simpson's Paradox 用 hedged language 报告为架构依赖发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b2e1576-8211-4747-bc86-9caa9389c667",
  "isSidechain": false,
  "requestId": "req_011CbFBTw6JvAo1P8MYW7jBi",
  "type": "assistant",
  "uuid": "5352e91e-f65f-44fe-9a90-a00feb659c4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpeWtgqpLBNq588aFo8Msv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 186,
      "cache_read_input_tokens": 83191,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 186,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 377,
          "cache_read_input_tokens": 83191,
          "cache_creation_input_tokens": 186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 186
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

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "5352e91e-f65f-44fe-9a90-a00feb659c4b",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration empirical study paper",
  "sessionId": "5539e7cd-7d85-4f3f-8732-4059690119cd"
}
```

---
