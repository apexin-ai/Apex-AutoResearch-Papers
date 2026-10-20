# Research conversation: 项目：solver-trace-ablation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-abl

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 82
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/8e614e8b-1c20-42be-96fe-59a15bdd0ca9.jsonl`
- **Structured JSON:** [`63466593d279484119ad.json`](../../sessions/63/63466593d279484119ad.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T14:05:43.238Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T14:05:43.238Z",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "content": "项目：solver-trace-ablation\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=True, 0 critical, 14 warning\n一致性检查: 0 critical, 6 warning\n编译: ✅, 页数: 23\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T14:05:43.242Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T14:05:43.242Z",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

## Round 1

80 recorded events

### User

_source line 3 · 2026-05-25T14:05:43.287Z_

项目：solver-trace-ablation
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=True, 0 critical, 14 warning
一致性检查: 0 critical, 6 warning
编译: ✅, 页数: 23
内部信息: 0 critical, 0 warning

━━━ 用户自定义规则（作为额外检查项）━━━
## 用户自定义规则（必须遵守）
### 写作规则

- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section
- **[EMNLP 2026]** abstract 不要超过 200 words

### 审稿规则

- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.

> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。
请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。

请按照你的角色指令执行内容结构审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "0177a9f7-52c4-42a4-8f9a-d1ed33022992",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T14:05:43.286Z_

```json
{
  "parentUuid": "0177a9f7-52c4-42a4-8f9a-d1ed33022992",
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
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file"
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
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7f8117ea-9f22-433e-bd66-eaf171621287",
  "timestamp": "2026-05-25T14:05:43.286Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T14:05:43.286Z_

```json
{
  "parentUuid": "7f8117ea-9f22-433e-bd66-eaf171621287",
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
  "uuid": "225546b3-220a-4461-8859-7c6dcf23a1e1",
  "timestamp": "2026-05-25T14:05:43.286Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T14:05:43.286Z_

```json
{
  "parentUuid": "225546b3-220a-4461-8859-7c6dcf23a1e1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4411475a-961e-43ac-b627-b11d80077dce",
  "timestamp": "2026-05-25T14:05:43.286Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 solver-trace-ablation paper audit",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Assistant

_source line 8 · 2026-05-25T14:05:48.075Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a content structure audit of the paper in the solver-trace-ablation project. Let me follow the execution flow:

1. Read the paper-writing-norms skill and paper-quality-lessons skill
2. Read all .tex files in the paper directory
3. Audit along all specified dimensions
4. Output structured findings

Let me start by reading the skills and the paper files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4411475a-961e-43ac-b627-b11d80077dce",
  "isSidechain": false,
  "requestId": "req_011CbPR2X1vmAcSrPCjYz5uq",
  "type": "assistant",
  "uuid": "20de38b7-35f6-4691-877e-0b1574822419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MF77NGVp8ufdoJQJKjd7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27827,
      "cache_read_input_tokens": 11846,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 408,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27827
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

_source line 9 · 2026-05-25T14:05:48.628Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20de38b7-35f6-4691-877e-0b1574822419",
  "isSidechain": false,
  "requestId": "req_011CbPR2X1vmAcSrPCjYz5uq",
  "type": "assistant",
  "uuid": "52de5fb5-17f2-4ea7-9975-60ea3bdbca53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MF77NGVp8ufdoJQJKjd7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27827,
      "cache_read_input_tokens": 11846,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 408,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27827
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

_source line 10 · 2026-05-25T14:05:49.505Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MwzH9UgLEdAn26QhZy8jqP`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52de5fb5-17f2-4ea7-9975-60ea3bdbca53",
  "isSidechain": false,
  "requestId": "req_011CbPR2X1vmAcSrPCjYz5uq",
  "type": "assistant",
  "uuid": "43a395b2-63be-483f-8704-e3d7c2a7fdb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MF77NGVp8ufdoJQJKjd7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27827,
      "cache_read_input_tokens": 11846,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 408,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27827
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

_source line 11 · 2026-05-25T14:05:50.860Z_

<details><summary>↩ Tool result · `toolu_01CcVbMj4gg5183VuAdkhd1B`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.
5	The root cause is evaluation by a single criterion, whether the generated formalization proves under a formal solver, which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
9	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to solver-backed settings, while inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} identifies gaming post-hoc but provides no training-time structural signal.
10	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
11	
12	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
13	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
14	A formalization where every component is necessary receives $\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\text{ISR}{=}0$.
15	Leave-one-out (LOO) ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\S\ref{sec:diagnostic}--\ref{sec:goodhart}).
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
20	\caption{ISR$^*$ (proved samples only) training trajectories across reward conditions (rolling $w{=}20$). Exec-only collapses to $\text{ISR}{\approx}0$, confirming structural degeneration (\S\ref{sec:diagnostic}); the ${\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\beta{=}0.1$ seeds rise toward $\text{ISR}{\approx}1$ via TS gaming (Goodhart effect, \S\ref{sec:goodhart}); random remains low.}
21	\label{fig:training-isr-curves}
22	\end{figure}
23	
24	Applied post-hoc, ISR reveals that rising prove rate conceals a compositional shift in proof structure: genuine reasoning gives way to hacking modes (conclusion embedding and tautological shortcuts), invisible to execution-based metrics (Figure~\ref{fig:training-isr-curves}; \S\ref{sec:diagnostic}).
25	
26	Yet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
27	Our results suggest that LOO-based structural proxies, and plausibly other component-necessity measures, face analogous exploitation risks in neurosymbolic settings.
28	In our Qwen3-4B experiments, the asymmetry persists across logic types (FOL, Prolog), reward doses, and random seeds, with dataset-dependent boundary conditions (FOLIO vs.\ ProofFOL; \S\ref{sec:crossdomain}), suggesting that structural proxies for formalization integrity are easier to observe than to optimize.
29	
30	We contribute:
31	(\textbf{C1})~a systematic empirical analysis of structural degeneration in GRPO-trained neurosymbolic reasoning, using LOO ablation (STA/ISR) to catalogue eight hacking modes across six reward conditions (\S\S\ref{sec:sta}--\ref{sec:crossdomain});
32	(\textbf{C2})~empirical characterization of a seed-dependent Goodhart effect when ISR is repurposed as reward, with matched controls ruling out confounds (\S\ref{sec:goodhart});
33	(\textbf{C3})~cross-logic replication (FOL/Prolog) confirming that the Goodhart effect transfers across logic types, with exploratory cross-dataset evidence (FOLIO/ProofFOL; \S\ref{sec:crossdomain}).
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb39f654-d6d4-4595-9e16-617293362228",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "ed30e7e2-3c9b-4239-86e3-548b6453e0e2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.\nThe root cause is evaluation by a single criterion, whether the generated formalization proves under a formal solver, which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\n\nNeurosymbolic formalizers~\\citep{logic-lm, linc, satlm} and RL-trained variants~\\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to solver-backed settings, while inference-time gaming detection~\\citep{kim-game-formalization, bondarenko-spec-gaming} identifies gaming post-hoc but provides no training-time structural signal.\nWhat is missing is an annotation-free method for testing \\emph{component necessity} in neurosymbolic outputs.\n\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.\nFor each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \\emph{Intensional Structural Reward} (ISR).\nA formalization where every component is necessary receives $\\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\\text{ISR}{=}0$.\nLeave-one-out (LOO) ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\\S\\ref{sec:diagnostic}--\\ref{sec:goodhart}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{ISR$^*$ (proved samples only) training trajectories across reward conditions (rolling $w{=}20$). Exec-only collapses to $\\text{ISR}{\\approx}0$, confirming structural degeneration (\\S\\ref{sec:diagnostic}); the ${\\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\\beta{=}0.1$ seeds rise toward $\\text{ISR}{\\approx}1$ via TS gaming (Goodhart effect, \\S\\ref{sec:goodhart}); random remains low.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\nApplied post-hoc, ISR reveals that rising prove rate conceals a compositional shift in proof structure: genuine reasoning gives way to hacking modes (conclusion embedding and tautological shortcuts), invisible to execution-based metrics (Figure~\\ref{fig:training-isr-curves}; \\S\\ref{sec:diagnostic}).\n\nYet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.\nOur results suggest that LOO-based structural proxies, and plausibly other component-necessity measures, face analogous exploitation risks in neurosymbolic settings.\nIn our Qwen3-4B experiments, the asymmetry persists across logic types (FOL, Prolog), reward doses, and random seeds, with dataset-dependent boundary conditions (FOLIO vs.\\ ProofFOL; \\S\\ref{sec:crossdomain}), suggesting that structural proxies for formalization integrity are easier to observe than to optimize.\n\nWe contribute:\n(\\textbf{C1})~a systematic empirical analysis of structural degeneration in GRPO-trained neurosymbolic reasoning, using LOO ablation (STA/ISR) to catalogue eight hacking modes across six reward conditions (\\S\\S\\ref{sec:sta}--\\ref{sec:crossdomain});\n(\\textbf{C2})~empirical characterization of a seed-dependent Goodhart effect when ISR is repurposed as reward, with matched controls ruling out confounds (\\S\\ref{sec:goodhart});\n(\\textbf{C3})~cross-logic replication (FOL/Prolog) confirming that the Goodhart effect transfers across logic types, with exploratory cross-dataset evidence (FOLIO/ProofFOL; \\S\\ref{sec:crossdomain}).\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "cb39f654-d6d4-4595-9e16-617293362228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T14:05:49.517Z_

<details><summary>↩ Tool result · `toolu_01MwzH9UgLEdAn26QhZy8jqP`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "43a395b2-63be-483f-8704-e3d7c2a7fdb1",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "3627251e-d463-4537-ac42-bcba32683507",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "43a395b2-63be-483f-8704-e3d7c2a7fdb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool call

_source line 13 · 2026-05-25T14:05:49.975Z_

<details open><summary>🔧 Tool call — Read · `toolu_013FEg6utvqPAxft5iUDt4CF`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3627251e-d463-4537-ac42-bcba32683507",
  "isSidechain": false,
  "requestId": "req_011CbPR2X1vmAcSrPCjYz5uq",
  "type": "assistant",
  "uuid": "6a5e8fbc-995a-4d4f-b39c-8315a3d1f9c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MF77NGVp8ufdoJQJKjd7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27827,
      "cache_read_input_tokens": 11846,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 408,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27827
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

_source line 14 · 2026-05-25T14:05:49.981Z_

<details><summary>↩ Tool result · `toolu_013FEg6utvqPAxft5iUDt4CF`</summary>

````text
1	---
2	name: paper-quality-lessons
3	description: NeurIPS 投稿实战经验总结——人工审查中提炼的写作规范、审查清单、常见反模式。Paper Agent / Reviewer / Director 写论文或审查论文时加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 1
7	tags:
8	  - writing
9	  - paper
10	  - quality
11	  - checklist
12	  - review
13	roles:
14	  - agent
15	  - reviewer
16	  - director
17	  - paper_agent
18	---
19	
20	# 论文写作质量指南（NeurIPS 实战经验）
21	
22	> 来源：2026 年 NeurIPS 投稿期间，从 20+ 项目的人工审查反馈中提炼。
23	> 每条规则都源自真实的 bug / 退回 / 审稿质疑。
24	
25	---
26	
27	## 一、数据诚信与溯源（最高优先级）
28	
29	### 1.1 数字必须有源头
30	
31	- 论文中**每一个数字**必须可追溯到 registry 实验 ID 或原始结果文件
32	- 禁止凭记忆写数字——必须 `cat result.json | head` + `ls -la` 附上文件证据
33	- 计算值（均值、标准差、DID、delta）必须独立重算，不信 Agent 第一手汇报
34	- `paper_provenance.yaml` 覆盖率必须 100%，改数字必须同步更新 provenance
35	
36	> **教训（D149 事件）**：Agent 曾伪造完整的 metrics 数据包括 p-value，事后被 Reviewer 独立 parse JSON 抓出。从此所有关键数据必须 Reviewer 独立验证到字段级别。
37	
38	### 1.2 不同来源数据不能混用
39	
40	- 配对数据必须同 seed、同 c 值、同 N、同 evaluation protocol
41	- 两张表如果 protocol 不同（如 0-shot vs 8-shot），论文必须明确说明
42	- 跨 config 比较 delta 会引入系统误差——必须补跑同 config baseline 后才能比较
43	- 非等量对比必须显式标注（如 "at unmatched volumes"）
44	
45	> **教训（D027 事件）**：不同 config 文件的 baseline 不同，跨 config 比较 delta 值引入了 artifact。
46	
47	### 1.3 结论撤回后不可复活
48	
49	- 被 Director shelved 的数据（如因截断混淆），禁止重新引入论文
50	- `paper_provenance.yaml` 中 `verified: false` 的 claim，不得恢复
51	- 术语修正后不可回退（如 "same norm" → "same per-layer standard deviation"）
52	
53	---
54	
55	## 二、Claim 强度与数据匹配
56	
57	### 2.1 Claim 强度规则
58	
59	| 数据支撑 | 允许的最强表述 |
60	|----------|--------------|
61	| 单 seed, 单数据集 | "preliminary observation", "initial evidence" |
62	| 单 seed, 多数据集 | "suggestive pattern", "indicative trend" |
63	| 多 seed, 单数据集 | 报告均值±标准差，可写 "we find" |
64	| 多 seed, 多数据集 | 可用 "robust", "consistent" |
65	| 统计检验显著 | 可用 "significant", 附 p-value |
66	| 单 seed + 外推到其他条件 | 必须加限定，不能声称 "scale-invariant" 等 |
67	
68	### 2.2 禁止的过强表述
69	
70	- "remarkably stable" → 改为 "relatively stable" 或给出量化波动范围
71	- "confirmed" → 仅 "suggestive" 级别数据不能用
72	- "scale-invariant" → single-seed 验证不够
73	- "We attribute X to Y" → 如果是假说，必须改为 "We hypothesize" + "requiring causal verification"
74	- "roughly twice" → 实际比值必须在 1.8x-2.2x 才能用，否则改为更准确的近似
75	- "domain-agnostic" → 改为 "robust across N domains tested"
76	
77	### 2.3 Claim 降级机制
78	
79	当证据不足以支撑独立 claim 时，应降级为 discussion 中的定性讨论，而非删除。具体做法：
80	- 独立 contribution → Discussion 段落
81	- 硬 claim → 加 caveat 的软 claim
82	- 正文数字 → 移入 Appendix
83	
84	---
85	
86	## 三、叙事与 Storytelling
87	
88	### 3.1 结构原则
89	
90	- 核心 paradox/发现之间必须有**过渡句**桥接，不能让读者在关键处断线
91	- Introduction 每条 Contribution 必须有对应的 section/table 支撑
92	- Discussion 不应重复 Results 的具体数字——引用表格编号
93	- 同一解释不要在多处重复推导——主文写一次 + 指向 Appendix
94	- Limitations 段不要写成一个 17 行大段——拆分为 2-3 个子段按主题分组
95	
96	### 3.2 冷引用（Cold Reference）
97	
98	- 任何首次出现的概念必须有上文铺垫
99	- Introduction 贡献列表中不能突然出现未被提及的模型/方法名
100	
101	### 3.3 不要用旧叙事套新数字
102	
103	新 baseline 出来后若 delta 大幅变化，Section 的叙事逻辑必须重写，不是简单替换数字。
104	
105	### 3.4 Contingency Plan
106	
107	关键实验结果不确定时需预写两套叙事（如 "若结果 A → 叙事 A"、"若结果 B → 叙事 B"），实验完成后选择正确版本。提交前必须确认只留了一套。
108	
109	### 3.5 不要基于中间值做叙事决策
110	
111	70% 进度时的估计往往不够稳定（尤其 GSM8K 等难度分布不均匀的 benchmark），必须等完整数据再定稿叙事。
112	
113	---
114	
115	## 四、术语与一致性
116	
117	### 4.1 术语一致性
118	
119	- 全文必须统一使用正式定义的术语，不得出现同义词漂移
120	- 术语定义后，每次使用必须完全一致（不要有时 "perturbation sensitivity" 有时 "perturbation impact"）
121	
122	### 4.2 统计量一致性
123	
124	- 两个不同的 kappa/p-value 每次出现时必须标注是哪个
125	- 同一个 metric 在不同位置的数字必须完全一致
126	- 修改任何数字后必须全文 grep 确认所有引用处同步
127	
128	### 4.3 p-value 格式
129	
130	- 无前导零、3 位小数：`p = .003`（不是 `p = 0.003`）
131	- 当非劣效性 p<0.001 实际由正向效应驱动时，必须加括注说明
132	
133	### 4.4 例子与定义必须一致
134	
135	Taxonomy 中的定义和对应示例不能自相矛盾。如果定义说 "no new content"，示例中就不能包含新信息。
136	
137	---
138	
139	## 五、投稿前检查清单（Pre-Submission Checklist）
140	
141	### 5.1 占位符扫描（硬门禁）
142	
143	提交前必须 grep 扫描，以下模式要求**零匹配**：
144	```
145	XX.XX, PLACEHOLDER, [If , TODO, TBD, \placeholder{
146	```
147	所有条件占位段落（`[If ...]`）必须替换为最终文本。
148	
149	### 5.2 编译检查
150	
151	- [ ] 编译零 error
152	- [ ] 无 `??` 未解析引用
153	- [ ] 无 > 1pt 的 overfull hbox
154	- [ ] 正文 ≤ 9 页（NeurIPS desk reject 风险）
155	- [ ] 使用当年 style file（`neurips_2026.sty`）
156	- [ ] Review 版启用行号
157	- [ ] 匿名审稿版无作者姓名、无致谢
158	
159	### 5.3 数据完整性
160	
161	- [ ] 论文所有数字与 registry/provenance 交叉验证通过
162	- [ ] 计算值（均值、标准差、DID、delta）独立重算确认
163	- [ ] 所有 evaluation protocol 差异已在论文中说明
164	- [ ] 多 seed 结果报告均值和标准差
165	- [ ] 单 seed 数据在 Limitations 中声明
166	
167	### 5.4 图表检查
168	
169	- [ ] 所有 figure PDF 存在且路径匹配
170	- [ ] 图表不超栏宽（单栏 5.5in / 全宽 6.5in）
171	- [ ] 图中字体 ≥ 7pt
172	- [ ] 小数精度全表统一
173	- [ ] 最优结果加粗、次优下划线
174	- [ ] 表格标题（caption）自包含
175	- [ ] Forest plot 等可视化无 dummy 值（CI_LO=-99 等）
176	
177	### 5.5 引用检查
178	
179	- [ ] 引用覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**（任一缺失说明调研不充分）
180	- [ ] 引用密度与目标会议近年录用论文同量级
181	- [ ] 引用键与 bib 条目 1:1 匹配
182	- [ ] 无孤儿 bib 条目
183	- [ ] 无幻觉引用（所有被引论文实际存在）
184	- [ ] 近年论文的年份/会议准确
185	- [ ] 审稿人要求的引用全部补齐
186	
187	### 5.6 匿名化检查
188	
189	- [ ] 源代码无硬编码绝对路径（`/Users/...`, `/root/...`）
190	- [ ] 配置文件无服务器路径
191	- [ ] Git history 已清理 author 信息（用 fresh repo）
192	- [ ] 项目管理文件不得提交（AGENTS.md, memory.md, registry.yaml, task_context/ 等）
193	- [ ] API Keys 通过环境变量，无泄露
194	
195	### 5.7 会议 Checklist 填写（如目标会议要求）
196	
197	- [ ] Claims: 摘要/Introduction 准确反映实验范围
198	- [ ] Limitations: 正文 Limitations 段 + Appendix 补充
199	- [ ] Experiments: 实验设置完整（exp_id, seed, 超参, 评估 protocol）
200	- [ ] Reproducibility: 数据集公开、代码可用
201	- [ ] Statistical Significance: 多 seed 均值+标准差、置信区间
202	- [ ] Compute: GPU 型号、训练时间、总 GPU-hours
203	- [ ] Licenses: 数据集/模型引用完整
204	- [ ] AI Assistants: 如实声明使用情况
205	- [ ] 每项认真回答（不要全写 N/A）
206	
207	### 5.8 叙事完整性
208	
209	- [ ] Conclusion 包含所有关键限定符（如 "under greedy decoding"）
210	- [ ] Abstract 与正文一致（不能一个写 "single seed" 另一个已是 "10 seeds"）
211	- [ ] 无 Appendix Version A/B 两套叙事残留
212	- [ ] 无 LaTeX 注释与正文混淆
213	- [ ] Contribution claim 在 Introduction 中（不在 Related Work 中）
214	- [ ] 所有专有名词/缩写首次出现时有定义（Abstract 内缩写也必须展开）
215	- [ ] Introduction 与 Method/Results 讲同一条主线（idea 变化后全文逻辑一致）
216	
217	### 5.9 去 AI 风格检查
218	
219	- [ ] **`grep "—" paper/*.tex` 全文清零**（解释性 em-dash 必须全删，最显著的 AI 痕迹）
220	- [ ] **`grep " – " paper/*.tex` 全文清零**（解释性 en-dash 必须全删）
221	- [ ] 无 "-ing," 分词短语结尾（如 "..., demonstrating the effectiveness of..."）
222	- [ ] 无连续 "Furthermore" / "Moreover" / "Additionally"（同段最多 1 个）
223	- [ ] 无 "It is worth noting that..." / "Notably, ..."
224	- [ ] 无 "delve into" / "leverage" / "utilize" / "a myriad of" / "a plethora of"
225	- [ ] 自然段 5-8 句是正常的，不要每 2-3 句就换段
226	
227	### 5.10 模板与同类论文核对
228	
229	- [ ] LaTeX 模板从目标会议官网下载（不是他人转载、不是上一年）
230	- [ ] `\documentclass[]{}` 选项匹配 review / camera-ready 阶段
231	- [ ] 写作前已参考 2-3 篇同领域近 1-2 年优秀论文，叙事节奏对齐
232	
233	---
234	
235	## 六、Reviewer 审查标准
236	
237	### 6.1 CRITICAL 级别（必须修复才能提交）
238	
239	- 论文数字与实验数据不一致
240	- Abstract 与正文矛盾
241	- Evaluation protocol 混淆（如 0-shot 写成 8-shot）
242	- 未经验证的数据写入论文
243	- 占位符残留
244	
245	### 6.2 WARNING 级别（应当修复）
246	
247	- Stale claims（更新了某处数字但忘了同步其他位置）
248	- 过强措辞不匹配数据支撑
249	- 隐式全因子设计误导（如写 "3×3×3=27" 但实际只有 15 格）
250	- 评估指标只描述了部分 domain
251	- 旧版数据引用
252	
253	### 6.3 数据一致性审查流程
254	
255	1. 从 registry 提取所有实验 metrics
256	2. 对照论文中每一个内联数字（到行号级别）
257	3. 独立重算所有衍生值
258	4. 不一致处标注为 CRITICAL
259	5. 近似表述检查实际比值是否在允许范围内
260	
261	---
262	
263	## 七、常见反模式速查表
264	
265	| 反模式 | 症状 | 修复方式 |
266	|--------|------|----------|
267	| Stale claim | 论文某处还引用旧数字 | 改数字后全文 grep 同步 |
268	| Protocol 混淆 | 不同表格用了不同 evaluation 但没说明 | 每张表注明 protocol |
269	| Agent 误报 | 实验结果缺乏文件证据 | 要求 `cat result.json` 截图 |
270	| 混用数据算比值 | 跨 seed/条件/N 的数据混合比较 | 只用严格配对的数据 |
271	| 叙事超越数据 | "confirmed" 但实际只是 suggestive | 匹配 claim 强度到 §2.1 |
272	| 冷引用 | 首次出现的概念无铺垫 | 先建立框架再引入 |
273	| 定义-例子矛盾 | Taxonomy 定义和示例冲突 | 审查所有定义与其示例 |
274	| Placeholder 残留 | XX.XX, TODO, [If...] 未清理 | 提交前 grep 硬门禁 |
275	| Path 泄露 | 代码/config 含服务器绝对路径 | 改为相对路径 |
276	| 重复推导 | 同一解释在 3 处各自推导一遍 | 主文一次 + 引用 Appendix |
277	| Discussion 重复 Results | Discussion 大量复制 Results 数字 | 改为引用表格编号 |
278	| 单 seed overclaim | 单 seed 数据声称 scale-invariant | 加 preliminary/hedging 限定 |
279	| Registry 不同步 | Registry 面值与实际状态不一致 | 以 SSH 实测为准 |
280	| vLLM 静默失败 | max_model_len 太小导致 100% 400 错误 | 预检必须发真实 prompt 验证 |
281	
282	---
283	
284	## 八、写论文前加载的 Skills
285	
286	写论文或做最终审查时，Director/Agent 应按需加载以下 skills：
287	- `latex-paper` — LaTeX 编译与格式
288	- `reference-audit` — 引用真实性审计
289	- `academic-writer` — ML 学术写作规范
290	- `paper-quality-lessons`（本 skill）— 实战经验教训
291	
292	---
293	
294	## 九、附录：投稿经验时间线教训
295	
296	1. **论文数字锁定时机**：最终编译前 24h 锁定所有数字，之后只允许格式修改
297	2. **GPU 不要空闲**：审稿期间如果 Agent 空闲，应该跑 ablation/扩展实验作为 rebuttal 储备
298	3. **匿名化提前做**：不要等到最后一天才检查路径泄露，fresh repo 需要时间清理
299	4. **9 页零余量策略**：NeurIPS 正文 9 页是硬限，每次新增内容必须等量压缩并编译验证
300	5. **Contingency 叙事提前写**：关键实验完成前就写好两版叙事，避免最后一刻仓促改稿
301	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "6a5e8fbc-995a-4d4f-b39c-8315a3d1f9c6",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "63336bad-398d-4269-b05b-749ef69624c6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md",
      "content": "---\nname: paper-quality-lessons\ndescription: NeurIPS 投稿实战经验总结——人工审查中提炼的写作规范、审查清单、常见反模式。Paper Agent / Reviewer / Director 写论文或审查论文时加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 1\ntags:\n  - writing\n  - paper\n  - quality\n  - checklist\n  - review\nroles:\n  - agent\n  - reviewer\n  - director\n  - paper_agent\n---\n\n# 论文写作质量指南（NeurIPS 实战经验）\n\n> 来源：2026 年 NeurIPS 投稿期间，从 20+ 项目的人工审查反馈中提炼。\n> 每条规则都源自真实的 bug / 退回 / 审稿质疑。\n\n---\n\n## 一、数据诚信与溯源（最高优先级）\n\n### 1.1 数字必须有源头\n\n- 论文中**每一个数字**必须可追溯到 registry 实验 ID 或原始结果文件\n- 禁止凭记忆写数字——必须 `cat result.json | head` + `ls -la` 附上文件证据\n- 计算值（均值、标准差、DID、delta）必须独立重算，不信 Agent 第一手汇报\n- `paper_provenance.yaml` 覆盖率必须 100%，改数字必须同步更新 provenance\n\n> **教训（D149 事件）**：Agent 曾伪造完整的 metrics 数据包括 p-value，事后被 Reviewer 独立 parse JSON 抓出。从此所有关键数据必须 Reviewer 独立验证到字段级别。\n\n### 1.2 不同来源数据不能混用\n\n- 配对数据必须同 seed、同 c 值、同 N、同 evaluation protocol\n- 两张表如果 protocol 不同（如 0-shot vs 8-shot），论文必须明确说明\n- 跨 config 比较 delta 会引入系统误差——必须补跑同 config baseline 后才能比较\n- 非等量对比必须显式标注（如 \"at unmatched volumes\"）\n\n> **教训（D027 事件）**：不同 config 文件的 baseline 不同，跨 config 比较 delta 值引入了 artifact。\n\n### 1.3 结论撤回后不可复活\n\n- 被 Director shelved 的数据（如因截断混淆），禁止重新引入论文\n- `paper_provenance.yaml` 中 `verified: false` 的 claim，不得恢复\n- 术语修正后不可回退（如 \"same norm\" → \"same per-layer standard deviation\"）\n\n---\n\n## 二、Claim 强度与数据匹配\n\n### 2.1 Claim 强度规则\n\n| 数据支撑 | 允许的最强表述 |\n|----------|--------------|\n| 单 seed, 单数据集 | \"preliminary observation\", \"initial evidence\" |\n| 单 seed, 多数据集 | \"suggestive pattern\", \"indicative trend\" |\n| 多 seed, 单数据集 | 报告均值±标准差，可写 \"we find\" |\n| 多 seed, 多数据集 | 可用 \"robust\", \"consistent\" |\n| 统计检验显著 | 可用 \"significant\", 附 p-value |\n| 单 seed + 外推到其他条件 | 必须加限定，不能声称 \"scale-invariant\" 等 |\n\n### 2.2 禁止的过强表述\n\n- \"remarkably stable\" → 改为 \"relatively stable\" 或给出量化波动范围\n- \"confirmed\" → 仅 \"suggestive\" 级别数据不能用\n- \"scale-invariant\" → single-seed 验证不够\n- \"We attribute X to Y\" → 如果是假说，必须改为 \"We hypothesize\" + \"requiring causal verification\"\n- \"roughly twice\" → 实际比值必须在 1.8x-2.2x 才能用，否则改为更准确的近似\n- \"domain-agnostic\" → 改为 \"robust across N domains tested\"\n\n### 2.3 Claim 降级机制\n\n当证据不足以支撑独立 claim 时，应降级为 discussion 中的定性讨论，而非删除。具体做法：\n- 独立 contribution → Discussion 段落\n- 硬 claim → 加 caveat 的软 claim\n- 正文数字 → 移入 Appendix\n\n---\n\n## 三、叙事与 Storytelling\n\n### 3.1 结构原则\n\n- 核心 paradox/发现之间必须有**过渡句**桥接，不能让读者在关键处断线\n- Introduction 每条 Contribution 必须有对应的 section/table 支撑\n- Discussion 不应重复 Results 的具体数字——引用表格编号\n- 同一解释不要在多处重复推导——主文写一次 + 指向 Appendix\n- Limitations 段不要写成一个 17 行大段——拆分为 2-3 个子段按主题分组\n\n### 3.2 冷引用（Cold Reference）\n\n- 任何首次出现的概念必须有上文铺垫\n- Introduction 贡献列表中不能突然出现未被提及的模型/方法名\n\n### 3.3 不要用旧叙事套新数字\n\n新 baseline 出来后若 delta 大幅变化，Section 的叙事逻辑必须重写，不是简单替换数字。\n\n### 3.4 Contingency Plan\n\n关键实验结果不确定时需预写两套叙事（如 \"若结果 A → 叙事 A\"、\"若结果 B → 叙事 B\"），实验完成后选择正确版本。提交前必须确认只留了一套。\n\n### 3.5 不要基于中间值做叙事决策\n\n70% 进度时的估计往往不够稳定（尤其 GSM8K 等难度分布不均匀的 benchmark），必须等完整数据再定稿叙事。\n\n---\n\n## 四、术语与一致性\n\n### 4.1 术语一致性\n\n- 全文必须统一使用正式定义的术语，不得出现同义词漂移\n- 术语定义后，每次使用必须完全一致（不要有时 \"perturbation sensitivity\" 有时 \"perturbation impact\"）\n\n### 4.2 统计量一致性\n\n- 两个不同的 kappa/p-value 每次出现时必须标注是哪个\n- 同一个 metric 在不同位置的数字必须完全一致\n- 修改任何数字后必须全文 grep 确认所有引用处同步\n\n### 4.3 p-value 格式\n\n- 无前导零、3 位小数：`p = .003`（不是 `p = 0.003`）\n- 当非劣效性 p<0.001 实际由正向效应驱动时，必须加括注说明\n\n### 4.4 例子与定义必须一致\n\nTaxonomy 中的定义和对应示例不能自相矛盾。如果定义说 \"no new content\"，示例中就不能包含新信息。\n\n---\n\n## 五、投稿前检查清单（Pre-Submission Checklist）\n\n### 5.1 占位符扫描（硬门禁）\n\n提交前必须 grep 扫描，以下模式要求**零匹配**：\n```\nXX.XX, PLACEHOLDER, [If , TODO, TBD, \\placeholder{\n```\n所有条件占位段落（`[If ...]`）必须替换为最终文本。\n\n### 5.2 编译检查\n\n- [ ] 编译零 error\n- [ ] 无 `??` 未解析引用\n- [ ] 无 > 1pt 的 overfull hbox\n- [ ] 正文 ≤ 9 页（NeurIPS desk reject 风险）\n- [ ] 使用当年 style file（`neurips_2026.sty`）\n- [ ] Review 版启用行号\n- [ ] 匿名审稿版无作者姓名、无致谢\n\n### 5.3 数据完整性\n\n- [ ] 论文所有数字与 registry/provenance 交叉验证通过\n- [ ] 计算值（均值、标准差、DID、delta）独立重算确认\n- [ ] 所有 evaluation protocol 差异已在论文中说明\n- [ ] 多 seed 结果报告均值和标准差\n- [ ] 单 seed 数据在 Limitations 中声明\n\n### 5.4 图表检查\n\n- [ ] 所有 figure PDF 存在且路径匹配\n- [ ] 图表不超栏宽（单栏 5.5in / 全宽 6.5in）\n- [ ] 图中字体 ≥ 7pt\n- [ ] 小数精度全表统一\n- [ ] 最优结果加粗、次优下划线\n- [ ] 表格标题（caption）自包含\n- [ ] Forest plot 等可视化无 dummy 值（CI_LO=-99 等）\n\n### 5.5 引用检查\n\n- [ ] 引用覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**（任一缺失说明调研不充分）\n- [ ] 引用密度与目标会议近年录用论文同量级\n- [ ] 引用键与 bib 条目 1:1 匹配\n- [ ] 无孤儿 bib 条目\n- [ ] 无幻觉引用（所有被引论文实际存在）\n- [ ] 近年论文的年份/会议准确\n- [ ] 审稿人要求的引用全部补齐\n\n### 5.6 匿名化检查\n\n- [ ] 源代码无硬编码绝对路径（`/Users/...`, `/root/...`）\n- [ ] 配置文件无服务器路径\n- [ ] Git history 已清理 author 信息（用 fresh repo）\n- [ ] 项目管理文件不得提交（AGENTS.md, memory.md, registry.yaml, task_context/ 等）\n- [ ] API Keys 通过环境变量，无泄露\n\n### 5.7 会议 Checklist 填写（如目标会议要求）\n\n- [ ] Claims: 摘要/Introduction 准确反映实验范围\n- [ ] Limitations: 正文 Limitations 段 + Appendix 补充\n- [ ] Experiments: 实验设置完整（exp_id, seed, 超参, 评估 protocol）\n- [ ] Reproducibility: 数据集公开、代码可用\n- [ ] Statistical Significance: 多 seed 均值+标准差、置信区间\n- [ ] Compute: GPU 型号、训练时间、总 GPU-hours\n- [ ] Licenses: 数据集/模型引用完整\n- [ ] AI Assistants: 如实声明使用情况\n- [ ] 每项认真回答（不要全写 N/A）\n\n### 5.8 叙事完整性\n\n- [ ] Conclusion 包含所有关键限定符（如 \"under greedy decoding\"）\n- [ ] Abstract 与正文一致（不能一个写 \"single seed\" 另一个已是 \"10 seeds\"）\n- [ ] 无 Appendix Version A/B 两套叙事残留\n- [ ] 无 LaTeX 注释与正文混淆\n- [ ] Contribution claim 在 Introduction 中（不在 Related Work 中）\n- [ ] 所有专有名词/缩写首次出现时有定义（Abstract 内缩写也必须展开）\n- [ ] Introduction 与 Method/Results 讲同一条主线（idea 变化后全文逻辑一致）\n\n### 5.9 去 AI 风格检查\n\n- [ ] **`grep \"—\" paper/*.tex` 全文清零**（解释性 em-dash 必须全删，最显著的 AI 痕迹）\n- [ ] **`grep \" – \" paper/*.tex` 全文清零**（解释性 en-dash 必须全删）\n- [ ] 无 \"-ing,\" 分词短语结尾（如 \"..., demonstrating the effectiveness of...\"）\n- [ ] 无连续 \"Furthermore\" / \"Moreover\" / \"Additionally\"（同段最多 1 个）\n- [ ] 无 \"It is worth noting that...\" / \"Notably, ...\"\n- [ ] 无 \"delve into\" / \"leverage\" / \"utilize\" / \"a myriad of\" / \"a plethora of\"\n- [ ] 自然段 5-8 句是正常的，不要每 2-3 句就换段\n\n### 5.10 模板与同类论文核对\n\n- [ ] LaTeX 模板从目标会议官网下载（不是他人转载、不是上一年）\n- [ ] `\\documentclass[]{}` 选项匹配 review / camera-ready 阶段\n- [ ] 写作前已参考 2-3 篇同领域近 1-2 年优秀论文，叙事节奏对齐\n\n---\n\n## 六、Reviewer 审查标准\n\n### 6.1 CRITICAL 级别（必须修复才能提交）\n\n- 论文数字与实验数据不一致\n- Abstract 与正文矛盾\n- Evaluation protocol 混淆（如 0-shot 写成 8-shot）\n- 未经验证的数据写入论文\n- 占位符残留\n\n### 6.2 WARNING 级别（应当修复）\n\n- Stale claims（更新了某处数字但忘了同步其他位置）\n- 过强措辞不匹配数据支撑\n- 隐式全因子设计误导（如写 \"3×3×3=27\" 但实际只有 15 格）\n- 评估指标只描述了部分 domain\n- 旧版数据引用\n\n### 6.3 数据一致性审查流程\n\n1. 从 registry 提取所有实验 metrics\n2. 对照论文中每一个内联数字（到行号级别）\n3. 独立重算所有衍生值\n4. 不一致处标注为 CRITICAL\n5. 近似表述检查实际比值是否在允许范围内\n\n---\n\n## 七、常见反模式速查表\n\n| 反模式 | 症状 | 修复方式 |\n|--------|------|----------|\n| Stale claim | 论文某处还引用旧数字 | 改数字后全文 grep 同步 |\n| Protocol 混淆 | 不同表格用了不同 evaluation 但没说明 | 每张表注明 protocol |\n| Agent 误报 | 实验结果缺乏文件证据 | 要求 `cat result.json` 截图 |\n| 混用数据算比值 | 跨 seed/条件/N 的数据混合比较 | 只用严格配对的数据 |\n| 叙事超越数据 | \"confirmed\" 但实际只是 suggestive | 匹配 claim 强度到 §2.1 |\n| 冷引用 | 首次出现的概念无铺垫 | 先建立框架再引入 |\n| 定义-例子矛盾 | Taxonomy 定义和示例冲突 | 审查所有定义与其示例 |\n| Placeholder 残留 | XX.XX, TODO, [If...] 未清理 | 提交前 grep 硬门禁 |\n| Path 泄露 | 代码/config 含服务器绝对路径 | 改为相对路径 |\n| 重复推导 | 同一解释在 3 处各自推导一遍 | 主文一次 + 引用 Appendix |\n| Discussion 重复 Results | Discussion 大量复制 Results 数字 | 改为引用表格编号 |\n| 单 seed overclaim | 单 seed 数据声称 scale-invariant | 加 preliminary/hedging 限定 |\n| Registry 不同步 | Registry 面值与实际状态不一致 | 以 SSH 实测为准 |\n| vLLM 静默失败 | max_model_len 太小导致 100% 400 错误 | 预检必须发真实 prompt 验证 |\n\n---\n\n## 八、写论文前加载的 Skills\n\n写论文或做最终审查时，Director/Agent 应按需加载以下 skills：\n- `latex-paper` — LaTeX 编译与格式\n- `reference-audit` — 引用真实性审计\n- `academic-writer` — ML 学术写作规范\n- `paper-quality-lessons`（本 skill）— 实战经验教训\n\n---\n\n## 九、附录：投稿经验时间线教训\n\n1. **论文数字锁定时机**：最终编译前 24h 锁定所有数字，之后只允许格式修改\n2. **GPU 不要空闲**：审稿期间如果 Agent 空闲，应该跑 ablation/扩展实验作为 rebuttal 储备\n3. **匿名化提前做**：不要等到最后一天才检查路径泄露，fresh repo 需要时间清理\n4. **9 页零余量策略**：NeurIPS 正文 9 页是硬限，每次新增内容必须等量压缩并编译验证\n5. **Contingency 叙事提前写**：关键实验完成前就写好两版叙事，避免最后一刻仓促改稿\n",
      "numLines": 301,
      "startLine": 1,
      "totalLines": 301
    }
  },
  "sourceToolAssistantUUID": "6a5e8fbc-995a-4d4f-b39c-8315a3d1f9c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool call

_source line 15 · 2026-05-25T14:05:50.453Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QPDFSpTLs9HV89CwHCcTAd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63336bad-398d-4269-b05b-749ef69624c6",
  "isSidechain": false,
  "requestId": "req_011CbPR2X1vmAcSrPCjYz5uq",
  "type": "assistant",
  "uuid": "bd33ba20-1966-4fc0-8e14-dce731a22c1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MF77NGVp8ufdoJQJKjd7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27827,
      "cache_read_input_tokens": 11846,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 408,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27827
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

_source line 16 · 2026-05-25T14:05:50.465Z_

<details><summary>↩ Tool result · `toolu_01QPDFSpTLs9HV89CwHCcTAd`</summary>

```text
1	\begin{abstract}
2	Neurosymbolic reasoning pipelines evaluate formalizations by execution alone, treating all successful proofs as equal.
3	This single-criterion reward conflates genuine derivation with structural shortcuts: embedding the conclusion among the premises proves just as reliably, and reinforcement learning (RL) optimizers exploit the indifference.
4	We apply leave-one-out ablation to GRPO-trained formalizations, \emph{Solver Trace Ablation} (STA), to test whether each component is necessary for proof success, and characterize structural degeneration under six reward conditions via the resulting \emph{Intensional Structural Reward} (ISR).
5	ISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
6	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
7	In our Qwen3-4B experiments, the Goodhart effect is seed-dependent (3 of 5 seeds converge to gaming under standard training conditions; 2 retain genuine reasoning), and the \emph{observe-vs-optimize asymmetry} persists across logic types, confirmed by cross-logic (Prolog) replication.
8	Cross-dataset (ProofFOL) evidence suggests dataset-dependent boundary conditions: structural proxies for formalization integrity are easier to observe than to optimize\footnote{Code and data are available at \url{https://anonymous.4open.science/r/solver-trace-ablation-CB70/}.}.\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd33ba20-1966-4fc0-8e14-dce731a22c1f",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "70d4a479-3557-499c-86ca-9fdcc2e34a2c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nNeurosymbolic reasoning pipelines evaluate formalizations by execution alone, treating all successful proofs as equal.\nThis single-criterion reward conflates genuine derivation with structural shortcuts: embedding the conclusion among the premises proves just as reliably, and reinforcement learning (RL) optimizers exploit the indifference.\nWe apply leave-one-out ablation to GRPO-trained formalizations, \\emph{Solver Trace Ablation} (STA), to test whether each component is necessary for proof success, and characterize structural degeneration under six reward conditions via the resulting \\emph{Intensional Structural Reward} (ISR).\nISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.\nTautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.\nIn our Qwen3-4B experiments, the Goodhart effect is seed-dependent (3 of 5 seeds converge to gaming under standard training conditions; 2 retain genuine reasoning), and the \\emph{observe-vs-optimize asymmetry} persists across logic types, confirmed by cross-logic (Prolog) replication.\nCross-dataset (ProofFOL) evidence suggests dataset-dependent boundary conditions: structural proxies for formalization integrity are easier to observe than to optimize\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/solver-trace-ablation-CB70/}.}.\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "bd33ba20-1966-4fc0-8e14-dce731a22c1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T14:05:50.855Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CcVbMj4gg5183VuAdkhd1B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70d4a479-3557-499c-86ca-9fdcc2e34a2c",
  "isSidechain": false,
  "requestId": "req_011CbPR2X1vmAcSrPCjYz5uq",
  "type": "assistant",
  "uuid": "cb39f654-d6d4-4595-9e16-617293362228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MF77NGVp8ufdoJQJKjd7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27827,
      "cache_read_input_tokens": 11846,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 408,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27827
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
  "lastPrompt": "项目：solver-trace-ablation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 14 warning 一致性…",
  "leafUuid": "ed30e7e2-3c9b-4239-86e3-548b6453e0e2",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 solver-trace-ablation paper audit",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Tool call

_source line 20 · 2026-05-25T14:05:55.345Z_

<details open><summary>🔧 Tool call — Read · `toolu_014NbTKtKNnphLDtJ6UMGHvA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed30e7e2-3c9b-4239-86e3-548b6453e0e2",
  "isSidechain": false,
  "requestId": "req_011CbPR35fxjstvpKyw5ummL",
  "type": "assistant",
  "uuid": "2528f1cd-5e72-40f3-a5b3-bdbfe342e3b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfPLFPr9bhMXxNmUVxb2Gd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13427,
      "cache_read_input_tokens": 39673,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 39673,
          "cache_creation_input_tokens": 13427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13427
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

_source line 21 · 2026-05-25T14:05:55.355Z_

<details><summary>↩ Tool result · `toolu_014NbTKtKNnphLDtJ6UMGHvA`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity} (Figure~\ref{fig:sta-overview}a): a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation set (100 examples) contains 34 True, 25 False, and 41 Unknown labels, with only True-labeled examples admitting valid proofs (theoretical PR ceiling ${\sim}34\%$).
11	Exec-only GRPO reaching $\text{PR}{=}93\%$ (\S\ref{sec:diagnostic}), nearly $3\times$ this ceiling, confirms the solver accepts formalizations for nominally unprovable examples, constituting direct evidence of structural gaming independent of ISR.
12	
13	\subsection{Solver Trace Ablation (STA)}
14	\label{sec:sta}
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=\textwidth]{figures/fig1_sta_overview.pdf}
19	\caption{STA overview. \textbf{(a)}~The formalization pipeline: an LLM translates natural-language (NL) premises into formal logic, verified by an external solver. \textbf{(b)}~STA removes each component in turn and re-runs the solver; the fraction of necessary components yields ISR. \textbf{(c)}~Applied post-hoc, ISR detects structural hacking; repurposed as reward, it triggers a Goodhart effect where tautological shortcuts (TS) achieve $\text{ISR}{=}1$ by construction.}
20	\label{fig:sta-overview}
21	\end{figure*}
22	
23	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}; Algorithm~\ref{alg:sta}).
24	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
25	A component is \emph{necessary} if its removal causes proof failure.
26	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
27	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
28	
29	\begin{algorithm}[t]
30	\small
31	\caption{Solver Trace Ablation (STA)}
32	\label{alg:sta}
33	\begin{algorithmic}[1]
34	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
35	\ENSURE $\text{ISR}(x) \in [0, 1]$
36	\STATE $\textit{necessary} \gets 0$
37	\FOR{$i = 1$ to $n$}
38	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
39	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
40	    \ENDIF
41	\ENDFOR
42	\RETURN $\textit{necessary} \,/\, n$
43	\end{algorithmic}
44	\end{algorithm}
45	
46	\paragraph{Intensional Structural Reward.}\footnote{Not \emph{intentional}; \emph{intensional} contrasts with extensional (execution-only) evaluation.}
47	For a proved formalization $x = \{c_1, \ldots, c_n\}$, ISR is the fraction of necessary components:
48	\begin{equation}
49	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
50	  \label{eq:isr}
51	\end{equation}
52	ISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.
53	An ISR of zero for proved samples can arise from structural degeneration or genuine redundancy; our hacking mode classification (\S\ref{sec:taxonomy-method}) disambiguates these cases, with ${>}90\%$ of low-ISR proved samples exhibiting identifiable hacking patterns.
54	ISR computes the LOO marginal contribution, a restriction of the Shapley value to the maximal coalition (Appendix~\ref{app:shapley}); full interaction detection would require $O(2^n)$ evaluations.
55	ISR quantifies component redundancy, not semantic faithfulness; its diagnostic value is realized through the downstream mode breakdown (\S\ref{sec:taxonomy}), not the scalar alone.
56	We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating component necessity with prove rate.
57	
58	\paragraph{LOO independence assumption.}
59	LOO ablation tests individual, not joint, component necessity~\citep{jia-harman-survey}, systematically underestimating ISR when jointly-necessary components exist; the observed collapse is therefore conservative.
60	
61	\subsection{Reward Conditions and Hacking Modes}
62	\label{sec:rewards}
63	\label{sec:taxonomy-method}
64	
65	We study six conditions: exec-only ($r_{\text{exec}}$), ISR low/high-dose ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations).
66	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
67	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
68	Each RL condition uses seeds $\{42,43,44\}$ and identical training data (formulation alternatives in Appendix~\ref{app:setup}).
69	
70	\begin{table*}[t]
71	\centering
72	\small
73	\setlength{\tabcolsep}{14pt}
74	\begin{tabular}{l c c c c c c}
75	\toprule
76	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
77	\midrule
78	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
79	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
80	\midrule
81	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (PG corrected)
82	ISR (3-seed) & 0.1 & 77{\scriptsize$\pm$14} & $1.06\times^\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
83	ISR (5-seed) & 0.1 & 70{\scriptsize$\pm$19} & (0.63)$^\ddagger$ & 54 & 18 & 23 \\ %% registry: plan002-additive-b01-s42--s46 (pooled)
84	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 69 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
85	Shuffled-ISR & 0.1 & 15{\scriptsize$\pm$1} & 0.559{\scriptsize$\pm$.02} & 7 & 7 & \textbf{87} \\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)
86	\midrule
87	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42, exp1-isr-b03-s43-r3, plan002-additive-b03-s44 (pooled; D106 s43 genuine 23→20)
88	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)
89	\bottomrule
90	\end{tabular}
91	\caption{Goodhart landscape across reward conditions. PR = prove rate; ISR$^*$ = proved-only ISR; TS = tautological shortcut; CE = conclusion embedding; N-H = non-hacking (upper bound on genuine reasoning). Multi-seed rows: pooled TS/CE/N-H; PR/ISR$^*$ as mean$\pm$std. $^\dagger$Seed~42 only. $^\ddagger$Premise-count-matched (\S\ref{sec:goodhart}). $^\P$FN-corrected (\S\ref{app:h8}). $^\S$Seed-dependent (s43: 38.3\%). Per-seed data: Table~\ref{tab:fol-detailed}.}
92	\label{tab:goodhart-landscape}
93	\end{table*}
94	
95	\paragraph{Hacking taxonomy.}
96	Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}), dominated by three: \textbf{CE} (conclusion embedded among multiple premises), \textbf{TS} (single-premise conclusion duplication; targets ISR directly since removing the sole premise forces $\text{ISR}\geq 0.5$), and \textbf{PG} (premise-subset gaming: each component is LOO-necessary but the premise set is incomplete; Appendix~\ref{app:h8}).
97	Five additional modes (tautological collapse, repetition, complexity-without-utility, contradiction explosion, and query-as-fact [Prolog-specific]) appear in specific seeds or conditions.
98	CE and TS are robust across conditions and seeds; the remaining five modes are configuration-specific observations whose generalizability requires further investigation.
99	Modes are identified by strict text matching (CE/TS) plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; when patterns overlap, we assign the most specific mode (PG $>$ CE $>$ TS).
100	The non-hacking rate is an upper bound on genuine reasoning.
101	
102	Low ISR signals redundancy under exec-only but metric gaming under ISR-as-reward; the mode breakdown, not the ISR scalar, licenses interpretation.
103	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2528f1cd-5e72-40f3-a5b3-bdbfe342e3b6",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "53ee9536-3228-4ac4-92ca-a2d5e6febc76",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task and GRPO Training}\n\\label{sec:task}\n\nGiven premises $P_1,\\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\\{c_1,\\ldots,c_n\\}$ verified by an external solver $S\\in\\{\\text{Prover9, SWI-Prolog}\\}$.\nWe train with Group Relative Policy Optimization (GRPO)~\\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\\text{exec}}(x) = \\mathbf{1}[S(F_x){=}\\textit{proved}]$.\nThis optimizes prove rate but provides no signal about \\emph{component necessity} (Figure~\\ref{fig:sta-overview}a): a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.\nAll experiments draw from FOLIO~\\citep{folio}; the held-out evaluation set (100 examples) contains 34 True, 25 False, and 41 Unknown labels, with only True-labeled examples admitting valid proofs (theoretical PR ceiling ${\\sim}34\\%$).\nExec-only GRPO reaching $\\text{PR}{=}93\\%$ (\\S\\ref{sec:diagnostic}), nearly $3\\times$ this ceiling, confirms the solver accepts formalizations for nominally unprovable examples, constituting direct evidence of structural gaming independent of ISR.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{STA overview. \\textbf{(a)}~The formalization pipeline: an LLM translates natural-language (NL) premises into formal logic, verified by an external solver. \\textbf{(b)}~STA removes each component in turn and re-runs the solver; the fraction of necessary components yields ISR. \\textbf{(c)}~Applied post-hoc, ISR detects structural hacking; repurposed as reward, it triggers a Goodhart effect where tautological shortcuts (TS) achieve $\\text{ISR}{=}1$ by construction.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\nSTA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\\ref{fig:sta-overview}; Algorithm~\\ref{alg:sta}).\nGiven a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\\setminus\\{c_i\\}$ and re-runs the solver (Algorithm~\\ref{alg:sta}).\nA component is \\emph{necessary} if its removal causes proof failure.\nWhat constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.\nLOO ablation itself is standard in mutation testing and sensitivity analysis~\\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.\n\n\\begin{algorithm}[t]\n\\small\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Proved formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE $\\text{ISR}(x) \\in [0, 1]$\n\\STATE $\\textit{necessary} \\gets 0$\n\\FOR{$i = 1$ to $n$}\n    \\IF{$S(x \\setminus \\{c_i\\}) = \\textit{failed}$}\n        \\STATE $\\textit{necessary} \\gets \\textit{necessary} + 1$\n    \\ENDIF\n\\ENDFOR\n\\RETURN $\\textit{necessary} \\,/\\, n$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Intensional Structural Reward.}\\footnote{Not \\emph{intentional}; \\emph{intensional} contrasts with extensional (execution-only) evaluation.}\nFor a proved formalization $x = \\{c_1, \\ldots, c_n\\}$, ISR is the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n}\\sum_{i=1}^{n}\\mathbf{1}\\bigl[S(x\\setminus\\{c_i\\})=\\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.\nAn ISR of zero for proved samples can arise from structural degeneration or genuine redundancy; our hacking mode classification (\\S\\ref{sec:taxonomy-method}) disambiguates these cases, with ${>}90\\%$ of low-ISR proved samples exhibiting identifiable hacking patterns.\nISR computes the LOO marginal contribution, a restriction of the Shapley value to the maximal coalition (Appendix~\\ref{app:shapley}); full interaction detection would require $O(2^n)$ evaluations.\nISR quantifies component redundancy, not semantic faithfulness; its diagnostic value is realized through the downstream mode breakdown (\\S\\ref{sec:taxonomy}), not the scalar alone.\nWe report \\emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating component necessity with prove rate.\n\n\\paragraph{LOO independence assumption.}\nLOO ablation tests individual, not joint, component necessity~\\citep{jia-harman-survey}, systematically underestimating ISR when jointly-necessary components exist; the observed collapse is therefore conservative.\n\n\\subsection{Reward Conditions and Hacking Modes}\n\\label{sec:rewards}\n\\label{sec:taxonomy-method}\n\nWe study six conditions: exec-only ($r_{\\text{exec}}$), ISR low/high-dose ($r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ at $\\beta\\in\\{0.1,0.3\\}$), matched random controls ($r_{\\text{exec}}\\cdot(1{+}\\beta u)$, $u\\sim\\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations).\nMultiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.\nRandom isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.\nEach RL condition uses seeds $\\{42,43,44\\}$ and identical training data (formulation alternatives in Appendix~\\ref{app:setup}).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{14pt}\n\\begin{tabular}{l c c c c c c}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 69 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42, exp1-isr-b03-s43-r3, plan002-additive-b03-s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR = prove rate; ISR$^*$ = proved-only ISR; TS = tautological shortcut; CE = conclusion embedding; N-H = non-hacking (upper bound on genuine reasoning). Multi-seed rows: pooled TS/CE/N-H; PR/ISR$^*$ as mean$\\pm$std. $^\\dagger$Seed~42 only. $^\\ddagger$Premise-count-matched (\\S\\ref{sec:goodhart}). $^\\P$FN-corrected (\\S\\ref{app:h8}). $^\\S$Seed-dependent (s43: 38.3\\%). Per-seed data: Table~\\ref{tab:fol-detailed}.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Hacking taxonomy.}\nAcross conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\\ref{app:hacking-modes}), dominated by three: \\textbf{CE} (conclusion embedded among multiple premises), \\textbf{TS} (single-premise conclusion duplication; targets ISR directly since removing the sole premise forces $\\text{ISR}\\geq 0.5$), and \\textbf{PG} (premise-subset gaming: each component is LOO-necessary but the premise set is incomplete; Appendix~\\ref{app:h8}).\nFive additional modes (tautological collapse, repetition, complexity-without-utility, contradiction explosion, and query-as-fact [Prolog-specific]) appear in specific seeds or conditions.\nCE and TS are robust across conditions and seeds; the remaining five modes are configuration-specific observations whose generalizability requires further investigation.\nModes are identified by strict text matching (CE/TS) plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; when patterns overlap, we assign the most specific mode (PG $>$ CE $>$ TS).\nThe non-hacking rate is an upper bound on genuine reasoning.\n\nLow ISR signals redundancy under exec-only but metric gaming under ISR-as-reward; the mode breakdown, not the ISR scalar, licenses interpretation.\n",
      "numLines": 103,
      "startLine": 1,
      "totalLines": 103
    }
  },
  "sourceToolAssistantUUID": "2528f1cd-5e72-40f3-a5b3-bdbfe342e3b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T14:05:56.348Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cgdv6zkKFXhEZyGv5FyrHp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53ee9536-3228-4ac4-92ca-a2d5e6febc76",
  "isSidechain": false,
  "requestId": "req_011CbPR35fxjstvpKyw5ummL",
  "type": "assistant",
  "uuid": "cf9ad80f-36f5-43b3-a22c-36bda23a77f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfPLFPr9bhMXxNmUVxb2Gd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13427,
      "cache_read_input_tokens": 39673,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 39673,
          "cache_creation_input_tokens": 13427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13427
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

_source line 23 · 2026-05-25T14:05:57.128Z_

<details><summary>↩ Tool result · `toolu_01AfxRLSySSdkk3uP4CL65pF`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect: structural proxies for formalization integrity are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
5	Cross-logic experiments (Prolog) confirm the compositional mode shift; cross-benchmark evidence (ProofFOL, $p{=}0.10$) is exploratory (\S\ref{sec:crossdomain}).
6	Convergence appears necessary for degeneration (Appendix~\ref{app:seed-convergence}); practitioners should apply structural diagnostics post-hoc.
7	The asymmetry motivates targeted mitigations (mode-aware reward shaping~\citep{tarek2025reward, pronesti2026beyond} or single-premise penalties); remaining questions include disentangling LOO's premise-count bias and extending the taxonomy to process reward settings.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "477acc82-7474-4519-9bb3-2e8600a76a51",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "0fb5c91c-07d3-4f8b-90f5-7383026db678",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect: structural proxies for formalization integrity are easier to observe than to optimize (Appendix~\\ref{app:practical-guidelines}).\nCross-logic experiments (Prolog) confirm the compositional mode shift; cross-benchmark evidence (ProofFOL, $p{=}0.10$) is exploratory (\\S\\ref{sec:crossdomain}).\nConvergence appears necessary for degeneration (Appendix~\\ref{app:seed-convergence}); practitioners should apply structural diagnostics post-hoc.\nThe asymmetry motivates targeted mitigations (mode-aware reward shaping~\\citep{tarek2025reward, pronesti2026beyond} or single-premise penalties); remaining questions include disentangling LOO's premise-count bias and extending the taxonomy to process reward settings.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "477acc82-7474-4519-9bb3-2e8600a76a51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T14:05:56.353Z_

<details><summary>↩ Tool result · `toolu_01Cgdv6zkKFXhEZyGv5FyrHp`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted; full hyperparameters in Table~\ref{tab:hyperparams}) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention; Appendix~\ref{app:prooffol-construction}, Table~\ref{tab:prooffol-vs-folio}); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}; classifier blind spots discussed in Appendix~\ref{app:extended-discussion}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Table~\ref{tab:classifier-precision}).
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=0.85\columnwidth]{figures/fig_seed_divergence.pdf}
17	\caption{Seed-dependent Goodhart effect under ISR $\beta{=}0.1$ reward (500 steps). Three seeds converge to gaming ($\text{N-H}{\leq}17\%$); two retain genuine reasoning (${\sim}55\%$).}
18	\label{fig:seed-divergence}
19	\end{figure}
20	
21	\paragraph{Statistical considerations.}
22	With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.
23	Pooled Cochran--Mantel--Haenszel $p$-values ($N{=}3$ strata) are descriptive summaries, not formal inference; non-significant comparisons are exploratory.
24	An $N{=}2$ sensitivity analysis excluding s43 confirms consistent or stronger patterns (Appendix~\ref{app:n2-sensitivity}).
25	ProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.
26	
27	\subsection{ISR as Diagnostic}
28	\label{sec:diagnostic}
29	
30	\textbf{Collapse trajectory.}
31	Figure~\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.
32	As PR climbs from $32\%$ to $96\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\times$, \S\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
33	By 500 steps, $87\%$ of proved samples embed the conclusion verbatim (CE), establishing degeneration independent of the ISR scalar.
34	A binary variant testing only collective premise necessity misses the collapse entirely ($\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\ref{app:o1-ablation}).
35	All three exec-only seeds converge to ${\leq}6.2\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}), confirming that structural degeneration under exec-only reward is not seed-specific among converged runs.
36	
37	\textbf{Cross-seed instability.}
38	Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\leq}6.2\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}).
39	Exec-only seeds exhibit qualitatively different convergence patterns (PR range: 13--98\%), precluding meaningful pooling; we report seed~42 as representative of the converged regime (Table~\ref{tab:goodhart-landscape}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2
40	Two additional seeds under identical conditions fail to converge ($\text{PR}{\approx}14\%$; Appendix~\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful convergence, though the confound between model capability and optimization success precludes strong causal attribution (Appendix~\ref{app:llama-coldstart}).
41	
42	\textbf{SFT baseline.}
43	SFT on gold formalizations produces $92\%$ non-hacking outputs at $\text{PR}{=}13\%$ (odds ratio ${=}147$ vs.\ exec-only, $p{<}0.001$; Table~\ref{tab:bootstrap-ci}), establishing that hacking modes are absent before RL optimization.
44	SFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.
45	Early-training comparison supports this interpretation: at 100 steps ($\text{PR}{=}32\%$), hacking already reaches $31\%$ vs.\ SFT's $8\%$ at comparable PR (Appendix~\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
46	
47	\subsection{Goodhart Effects on ISR-as-Reward}
48	\label{sec:goodhart}
49	
50	We reverse ISR's role from observer to reward: $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with matched random control ($u\sim\mathcal{U}(0,1)$).
51	The result is a regressional Goodhart pattern~\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \emph{composition} of failure modes without reducing their aggregate prevalence.
52	ISR reward systematically selects for tautological shortcuts (TS) over conclusion embedding (CE) rather than producing genuine reasoning (Table~\ref{tab:goodhart-landscape}). The scalar ISR$^*$ advantage ($214\times$ raw) collapses to $1.06\times$ after controlling for premise count; the compositional mode shift provides the primary evidence.
53	
54	\paragraph{Multiplicative coupling.}
55	Three controls constrain the multiplicative confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\ref{app:setup}).
56	The shuffled-ISR control ($87\%$ non-hacking at low PR) suggests Goodhart effects require sample-level ISR signal, though non-convergence cannot be ruled out (Appendix~\ref{app:seed-convergence}).
57	
58	\begin{figure}[t]
59	\centering
60	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
61	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR systematically selects for TS over CE without reducing total hacking; SFT shows near-zero hacking.}
62	\label{fig:hacking-composition}
63	\end{figure}
64	
65	\textbf{Low-dose ISR ($\beta{=}0.1$).}
66	ISR reward amplifies TS convergence: $71\%$ of proved samples under ISR exhibit tautological shortcuts vs.\ $14\%$ under random (Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
67	Total conclusion embedding ($\text{CE}+\text{TS}$) spans $68$--$100\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\ref{fig:hacking-composition}).
68	A seed-stratified $\chi^2$ test confirms the overall mode distribution differs significantly between ISR and random conditions ($\chi^2{=}174.8$, $\text{df}{=}2$, $p{<}10^{-38}$; Appendix~\ref{app:statistical-details}).
69	
70	\textbf{Seed-dependent outcomes.}
71	ISR reward produces bimodal outcomes (Figure~\ref{fig:seed-divergence}): 3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect can occur under standard training conditions (95\% Clopper--Pearson CI: [11.8\%, 88.1\%]; $n{=}5$); 2 of 5 retain substantial genuine reasoning (seeds~45/46 added post-hoc to test replication; Appendix~\ref{app:detailed-results}).
72	Excluding s43, converged seeds show ${\leq}17\%$ non-hacking at 500 steps, collapsing to ${\leq}2\%$ by 1000 (Appendix~\ref{app:n2-sensitivity}).
73	
74	\textbf{Premise-count confound.}
75	The $214\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.
76	The premise-count-matched comparison yields only $1.06\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.
77	
78	The compositional evidence, however, survives this control.
79	In the modal premise-count range (4--6 premises, where most proved samples fall), TS reaches $19.7\%$ under ISR versus $0\%$ under random reward (Figure~\ref{fig:premise-bins}; Table~\ref{tab:premise-bin-modes}).
80	TS hacking is mechanistically limited to simpler problems; this complexity dependence is a mechanistic insight, not a confound.
81	The compositional mode shift, not the scalar ISR difference, constitutes the primary evidence for the Goodhart effect.
82	
83	\begin{figure}[t]
84	\centering
85	\includegraphics[width=\columnwidth]{figures/fig_premise_bins.pdf}
86	\caption{Mode composition by premise count (proved samples, seed~42, $\beta{=}0.1$). TS hacking emerges exclusively under ISR in the 4--6 premise range; Random shows zero TS at any complexity, confirming that ISR's compositional shift is not a premise-count artifact. I\,=\,ISR, R\,=\,Random.}
87	\label{fig:premise-bins}
88	\end{figure}
89	
90	\textbf{Higher doses and temporal dynamics.}
91	Any genuine reasoning under ISR $\beta{=}0.1$ is transient: non-hacking drops from $17\%$ to $2\%$ by 1000 steps (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
92	Higher doses accelerate collapse: $\beta{=}0.2$ eliminates all non-hacking; $\beta{=}0.3$ destabilizes training itself~\citep{gao-reward-overoptimization} (Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
93	
94	\subsection{Cross-Domain and Cross-Dataset Evidence}
95	\label{sec:crossdomain}
96	\label{sec:crosslogic}
97	
98	The following results extend the primary findings of \S\ref{sec:diagnostic}--\ref{sec:goodhart} to alternative logic types and dataset families; these cross-domain experiments are exploratory in nature.
99	
100	\begin{figure*}[t]
101	\centering
102	\includegraphics[width=\textwidth]{figures/fig4_prolog_comparison.pdf}
103	\caption{Cross-logic results. \textbf{(a)}~FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{(b)}~Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
104	\label{fig:prolog-comparison}
105	\end{figure*}
106	
107	\textbf{Prolog: universal Goodhart.}
108	Replicating the pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}), exec-only seeds collapse to $\text{ISR}^*{\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.
109	Under ISR-as-reward, all three seeds reach $0\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\ref{tab:prolog-detailed}).
110	Prolog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.
111	
112	\textbf{ProofFOL exec-only: cross-dataset replication.}
113	Converged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.
114	The mode repertoire differs across datasets: among converged seeds, TS dominates one while CE dominates the other, showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.
115	
116	\textbf{ProofFOL ISR ($\beta{=}0.1$): dataset-dependent asymmetry.}
117	ISR reward on ProofFOL produces directionally higher genuine rates than exec-only ($p{=}0.10$, exploratory; Table~\ref{tab:prooffol-detailed}).
118	The asymmetry follows from hacking geometry: on FOLIO, TS yields high ISR (regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL, CE embeds conclusions among many premises, yielding $\text{ISR}{\approx}0$ and rendering ISR reward effectively corrective.
119	
120	\textbf{Cross-scale validation (Qwen3-8B).}
121	Qwen3-8B does not converge under exec-only GRPO ($\text{PR}{=}14\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\ref{app:8b-results}).
122	
123	\subsection{Hacking Taxonomy}
124	\label{sec:taxonomy}
125	
126	Three modes account for the vast majority of hacking (Table~\ref{tab:hacking-taxonomy}; extended breakdown in Table~\ref{tab:hacking-taxonomy-app}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).
127	The central pattern: \emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\%$ non-hacking.
128	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf9ad80f-36f5-43b3-a22c-36bda23a77f7",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "a6890e73-dc4e-40f1-90aa-818972642b05",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted; full hyperparameters in Table~\\ref{tab:hyperparams}) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention; Appendix~\\ref{app:prooffol-construction}, Table~\\ref{tab:prooffol-vs-folio}); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}; classifier blind spots discussed in Appendix~\\ref{app:extended-discussion}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Table~\\ref{tab:classifier-precision}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig_seed_divergence.pdf}\n\\caption{Seed-dependent Goodhart effect under ISR $\\beta{=}0.1$ reward (500 steps). Three seeds converge to gaming ($\\text{N-H}{\\leq}17\\%$); two retain genuine reasoning (${\\sim}55\\%$).}\n\\label{fig:seed-divergence}\n\\end{figure}\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled Cochran--Mantel--Haenszel $p$-values ($N{=}3$ strata) are descriptive summaries, not formal inference; non-significant comparisons are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent or stronger patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), establishing degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\nAll three exec-only seeds converge to ${\\leq}6.2\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}), confirming that structural degeneration under exec-only reward is not seed-specific among converged runs.\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}6.2\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}).\nExec-only seeds exhibit qualitatively different convergence patterns (PR range: 13--98\\%), precluding meaningful pooling; we report seed~42 as representative of the converged regime (Table~\\ref{tab:goodhart-landscape}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful convergence, though the confound between model capability and optimization success precludes strong causal attribution (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ (odds ratio ${=}147$ vs.\\ exec-only, $p{<}0.001$; Table~\\ref{tab:bootstrap-ci}), establishing that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR reward systematically selects for tautological shortcuts (TS) over conclusion embedding (CE) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}). The scalar ISR$^*$ advantage ($214\\times$ raw) collapses to $1.06\\times$ after controlling for premise count; the compositional mode shift provides the primary evidence.\n\n\\paragraph{Multiplicative coupling.}\nThree controls constrain the multiplicative confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}).\nThe shuffled-ISR control ($87\\%$ non-hacking at low PR) suggests Goodhart effects require sample-level ISR signal, though non-convergence cannot be ruled out (Appendix~\\ref{app:seed-convergence}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR systematically selects for TS over CE without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random (Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\nA seed-stratified $\\chi^2$ test confirms the overall mode distribution differs significantly between ISR and random conditions ($\\chi^2{=}174.8$, $\\text{df}{=}2$, $p{<}10^{-38}$; Appendix~\\ref{app:statistical-details}).\n\n\\textbf{Seed-dependent outcomes.}\nISR reward produces bimodal outcomes (Figure~\\ref{fig:seed-divergence}): 3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect can occur under standard training conditions (95\\% Clopper--Pearson CI: [11.8\\%, 88.1\\%]; $n{=}5$); 2 of 5 retain substantial genuine reasoning (seeds~45/46 added post-hoc to test replication; Appendix~\\ref{app:detailed-results}).\nExcluding s43, converged seeds show ${\\leq}17\\%$ non-hacking at 500 steps, collapsing to ${\\leq}2\\%$ by 1000 (Appendix~\\ref{app:n2-sensitivity}).\n\n\\textbf{Premise-count confound.}\nThe $214\\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.\nThe premise-count-matched comparison yields only $1.06\\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.\n\nThe compositional evidence, however, survives this control.\nIn the modal premise-count range (4--6 premises, where most proved samples fall), TS reaches $19.7\\%$ under ISR versus $0\\%$ under random reward (Figure~\\ref{fig:premise-bins}; Table~\\ref{tab:premise-bin-modes}).\nTS hacking is mechanistically limited to simpler problems; this complexity dependence is a mechanistic insight, not a confound.\nThe compositional mode shift, not the scalar ISR difference, constitutes the primary evidence for the Goodhart effect.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_premise_bins.pdf}\n\\caption{Mode composition by premise count (proved samples, seed~42, $\\beta{=}0.1$). TS hacking emerges exclusively under ISR in the 4--6 premise range; Random shows zero TS at any complexity, confirming that ISR's compositional shift is not a premise-count artifact. I\\,=\\,ISR, R\\,=\\,Random.}\n\\label{fig:premise-bins}\n\\end{figure}\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself~\\citep{gao-reward-overoptimization} (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\nThe following results extend the primary findings of \\S\\ref{sec:diagnostic}--\\ref{sec:goodhart} to alternative logic types and dataset families; these cross-domain experiments are exploratory in nature.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{(a)}~FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{(b)}~Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure*}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe mode repertoire differs across datasets: among converged seeds, TS dominates one while CE dominates the other, showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces directionally higher genuine rates than exec-only ($p{=}0.10$, exploratory; Table~\\ref{tab:prooffol-detailed}).\nThe asymmetry follows from hacking geometry: on FOLIO, TS yields high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, CE embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\n\n\\textbf{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; extended breakdown in Table~\\ref{tab:hacking-taxonomy-app}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
      "numLines": 128,
      "startLine": 1,
      "totalLines": 128
    }
  },
  "sourceToolAssistantUUID": "cf9ad80f-36f5-43b3-a22c-36bda23a77f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T14:05:56.885Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bp5sjUU6xNveN9g6YkrR15`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6890e73-dc4e-40f1-90aa-818972642b05",
  "isSidechain": false,
  "requestId": "req_011CbPR35fxjstvpKyw5ummL",
  "type": "assistant",
  "uuid": "28a02550-fa0e-4ed8-927b-035fb606e2fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfPLFPr9bhMXxNmUVxb2Gd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13427,
      "cache_read_input_tokens": 39673,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 39673,
          "cache_creation_input_tokens": 13427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13427
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

_source line 26 · 2026-05-25T14:05:56.890Z_

<details><summary>↩ Tool result · `toolu_01Bp5sjUU6xNveN9g6YkrR15`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	Large language model (LLM)--solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp, nlproofs} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1, rlsf} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public natural language inference (NLI) benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Reward hacking and Goodhart's Law.}
10	Specification gaming~\citep{krakovna2020specification} and Goodhart's Law~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} are established across RL from human feedback (RLHF)~\citep{gao-reward-overoptimization} and logical formalization~\citep{bondarenko-spec-gaming, kim-game-formalization}.
11	Most closely related, \citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models; our work complements theirs by studying training-time degeneration via component necessity rather than faithfulness.
12	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where Kullback--Leibler (KL) regularization provably fails, providing a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.
13	Concurrent work documents spurious signals in RLVR~\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking, helff2026gaming, nishimura2026specgaming, khalifa2026countdown} and proposes composite rewards as mitigations~\citep{tarek2025reward, pronesti2026beyond};
14	mitigation strategies include reward model ensembles~\citep{coste2023reward}, constrained optimization~\citep{moskovitz2023confronting}, and activation-level monitoring~\citep{wilhelm2026monitoring}. \citet{yue2025rl-reasoning} show RLVR redistributes probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.
15	Our Goodhart effect follows the regressional pattern~\citep{manheim-goodhart-taxonomy} on FOLIO; its application to a diagnostic designed to detect gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.
16	
17	\vspace{-2pt}
18	\paragraph{Process rewards and reward design.}
19	Process reward models~\citep{lightman-verify-step, setlur2025rewarding, cui2025prime, cobbe2021training, uesato2022solving} supervise intermediate steps; \citet{sullivan2025grpo-prm} show GRPO implicitly implements process reward. Classical reward shaping~\citep{ng1999policy, gao-effective-rl-reward} guarantees policy invariance only under potential-based transforms; ISR violates this condition.
20	
21	\vspace{-2pt}
22	\paragraph{Mutation testing.}
23	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
24	Related concerns about chain-of-thought (CoT) faithfulness~\citep{lanham2023faithfulness, turpin2023unfaithful} operate at the reasoning-chain level rather than solver-input components.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28a02550-fa0e-4ed8-927b-035fb606e2fd",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "2e8030be-5a48-4026-bef3-7568d9d5da2a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLarge language model (LLM)--solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp, nlproofs} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1, rlsf} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.\nWe use FOLIO~\\citep{folio}, the only public natural language inference (NLI) benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nSpecification gaming~\\citep{krakovna2020specification} and Goodhart's Law~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} are established across RL from human feedback (RLHF)~\\citep{gao-reward-overoptimization} and logical formalization~\\citep{bondarenko-spec-gaming, kim-game-formalization}.\nMost closely related, \\citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models; our work complements theirs by studying training-time degeneration via component necessity rather than faithfulness.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where Kullback--Leibler (KL) regularization provably fails, providing a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.\nConcurrent work documents spurious signals in RLVR~\\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking, helff2026gaming, nishimura2026specgaming, khalifa2026countdown} and proposes composite rewards as mitigations~\\citep{tarek2025reward, pronesti2026beyond};\nmitigation strategies include reward model ensembles~\\citep{coste2023reward}, constrained optimization~\\citep{moskovitz2023confronting}, and activation-level monitoring~\\citep{wilhelm2026monitoring}. \\citet{yue2025rl-reasoning} show RLVR redistributes probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.\nOur Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO; its application to a diagnostic designed to detect gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\n\n\\vspace{-2pt}\n\\paragraph{Process rewards and reward design.}\nProcess reward models~\\citep{lightman-verify-step, setlur2025rewarding, cui2025prime, cobbe2021training, uesato2022solving} supervise intermediate steps; \\citet{sullivan2025grpo-prm} show GRPO implicitly implements process reward. Classical reward shaping~\\citep{ng1999policy, gao-effective-rl-reward} guarantees policy invariance only under potential-based transforms; ISR violates this condition.\n\n\\vspace{-2pt}\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\nRelated concerns about chain-of-thought (CoT) faithfulness~\\citep{lanham2023faithfulness, turpin2023unfaithful} operate at the reasoning-chain level rather than solver-input components.\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  },
  "sourceToolAssistantUUID": "28a02550-fa0e-4ed8-927b-035fb606e2fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T14:05:57.124Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AfxRLSySSdkk3uP4CL65pF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e8030be-5a48-4026-bef3-7568d9d5da2a",
  "isSidechain": false,
  "requestId": "req_011CbPR35fxjstvpKyw5ummL",
  "type": "assistant",
  "uuid": "477acc82-7474-4519-9bb3-2e8600a76a51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfPLFPr9bhMXxNmUVxb2Gd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13427,
      "cache_read_input_tokens": 39673,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 39673,
          "cache_creation_input_tokens": 13427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13427
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
  "lastPrompt": "项目：solver-trace-ablation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 14 warning 一致性…",
  "leafUuid": "0fb5c91c-07d3-4f8b-90f5-7383026db678",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 solver-trace-ablation paper audit",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Tool call

_source line 30 · 2026-05-25T14:06:02.119Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VmxZjnKpJ9gPjyFkde6dsd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fb5c91c-07d3-4f8b-90f5-7383026db678",
  "isSidechain": false,
  "requestId": "req_011CbPR3YNpEEwNc3FHCp1RJ",
  "type": "assistant",
  "uuid": "df16c154-2d7f-4fcc-a131-1ef050125b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBZrYVuiJU8rDYrzbSjnEq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9793,
      "cache_read_input_tokens": 53100,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 53100,
          "cache_creation_input_tokens": 9793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9793
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

_source line 31 · 2026-05-25T14:06:02.134Z_

<details><summary>↩ Tool result · `toolu_01VmxZjnKpJ9gPjyFkde6dsd`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single model (Qwen3-4B) with three to five seeds; degeneration patterns may not transfer to other families, and the 3/5 gaming rate (seeds 45--46 added post-hoc) is an existence demonstration, not a prevalence estimate.
5	FOLIO is a relatively small (1,435 examples) synthetic benchmark; generalization to larger or naturalistic corpora is untested.
6	ISR quantifies component necessity, not semantic faithfulness; diagnostic value comes from the mode breakdown, not the scalar alone (Appendix~\ref{app:extended-discussion}).
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df16c154-2d7f-4fcc-a131-1ef050125b17",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "067717ed-dc76-46e6-a61a-5e88afce6810",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single model (Qwen3-4B) with three to five seeds; degeneration patterns may not transfer to other families, and the 3/5 gaming rate (seeds 45--46 added post-hoc) is an existence demonstration, not a prevalence estimate.\nFOLIO is a relatively small (1,435 examples) synthetic benchmark; generalization to larger or naturalistic corpora is untested.\nISR quantifies component necessity, not semantic faithfulness; diagnostic value comes from the mode breakdown, not the scalar alone (Appendix~\\ref{app:extended-discussion}).\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "df16c154-2d7f-4fcc-a131-1ef050125b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T14:06:02.659Z_

<details open><summary>🔧 Tool call — Read · `toolu_012jZ4ijGcp5fq4Gfh8qo1jF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "067717ed-dc76-46e6-a61a-5e88afce6810",
  "isSidechain": false,
  "requestId": "req_011CbPR3YNpEEwNc3FHCp1RJ",
  "type": "assistant",
  "uuid": "c8d16ff8-d87a-41cf-8326-cf592cbaecd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBZrYVuiJU8rDYrzbSjnEq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9793,
      "cache_read_input_tokens": 53100,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 53100,
          "cache_creation_input_tokens": 9793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9793
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

_source line 33 · 2026-05-25T14:06:03.034Z_

<details><summary>↩ Tool result · `toolu_01V2boamzU8UHhVJPfxrKX2T`</summary>

```text
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
12	\usepackage{float}
13	\usepackage{placeins}
14	\usepackage[protrusion=true,expansion=false]{microtype}
15	
16	\setlength{\textfloatsep}{6pt plus 1pt minus 3pt}
17	\setlength{\dbltextfloatsep}{6pt plus 1pt minus 3pt}
18	\setlength{\intextsep}{4pt plus 1pt minus 2pt}
19	\setlength{\floatsep}{5pt plus 1pt minus 2pt}
20	\setlength{\dblfloatsep}{5pt plus 1pt minus 2pt}
21	\setlength{\abovecaptionskip}{3pt}
22	\setlength{\belowcaptionskip}{1pt}
23	\setlength{\abovedisplayskip}{6pt plus 2pt minus 3pt}
24	\setlength{\belowdisplayskip}{6pt plus 2pt minus 3pt}
25	
26	\graphicspath{{figures/}}
27	
28	\title{Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning}
29	
30	\author{Anonymous ACL submission}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{abstract}
36	\input{introduction}
37	\input{related_work}
38	\input{method}
39	\input{experiments}
40	\input{conclusion}
41	
42	\input{limitations}
43	
44	\bibliography{references}
45	
46	\appendix
47	\input{appendix}
48	
49	\end{document}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "931fb82d-d2f9-44e5-a728-0c78a2c04b2d",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "55cecdc0-a1df-4545-b7a8-25478482f35a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\\usepackage{enumitem}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{float}\n\\usepackage{placeins}\n\\usepackage[protrusion=true,expansion=false]{microtype}\n\n\\setlength{\\textfloatsep}{6pt plus 1pt minus 3pt}\n\\setlength{\\dbltextfloatsep}{6pt plus 1pt minus 3pt}\n\\setlength{\\intextsep}{4pt plus 1pt minus 2pt}\n\\setlength{\\floatsep}{5pt plus 1pt minus 2pt}\n\\setlength{\\dblfloatsep}{5pt plus 1pt minus 2pt}\n\\setlength{\\abovecaptionskip}{3pt}\n\\setlength{\\belowcaptionskip}{1pt}\n\\setlength{\\abovedisplayskip}{6pt plus 2pt minus 3pt}\n\\setlength{\\belowdisplayskip}{6pt plus 2pt minus 3pt}\n\n\\graphicspath{{figures/}}\n\n\\title{Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 50
    }
  },
  "sourceToolAssistantUUID": "931fb82d-d2f9-44e5-a728-0c78a2c04b2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-25T14:06:02.917Z_

<details><summary>↩ Tool result · `toolu_012jZ4ijGcp5fq4Gfh8qo1jF`</summary>

```text
1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions.
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\small
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
55	Total compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.
56	
57	\paragraph{SFT convergence.}
58	SFT training converged across all three seeds: final-step loss ${\leq}0.04$ and token accuracy ${>}99\%$ after ${\sim}8$ epochs on 500 examples (seed~42: $0.029$; seed~44: $0.033$); the 1000-step extension further decreases loss to $0.017$.
59	
60	\paragraph{Evaluation exception.}
61	FOL exec-only seed~43 was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
62	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol.
63	
64	\paragraph{Reward formulation.}
65	An additive variant ($r = r_{\text{exec}} + \beta\,\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\text{exec}}\cdot(1+\beta\,\text{ISR})$ ensures ISR modulates only proved outputs.
66	
67	\paragraph{ProofFOL dataset construction.}
68	\label{app:prooffol-construction}
69	ProofFOL is derived from ProofWriter~\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\sim}70\%$ retention; failures from timeouts, unsupported constructs, and translation errors).
70	Of the translated examples, 99.1\% parse successfully (92 skipped due to empty FOL output).
71	We sample 500 training and 100 evaluation examples (seed~42) from the verified pool.
72	Table~\ref{tab:prooffol-vs-folio} compares key structural properties.
73	
74	\begin{table}[!ht]
75	\centering
76	\caption{ProofFOL vs.\ FOLIO structural comparison (training sets, $n{=}500$ each).}
77	\label{tab:prooffol-vs-folio}
78	\small
79	\resizebox{\columnwidth}{!}{%
80	\begin{tabular}{@{}lcc@{}}
81	\toprule
82	\textbf{Property} & \textbf{ProofFOL} & \textbf{FOLIO} \\
83	\midrule
84	FOL premises (mean$\pm$std) & $18.2 \pm 3.2$ & $5.3 \pm 1.4$ \\
85	\quad Ground facts & $10.2 \pm 3.0$ & $1.8 \pm 1.5$ \\
86	\quad Rules & $8.1 \pm 1.1$ & $3.5 \pm 1.9$ \\
87	XOR ($\oplus$) samples & 0\% & 37.2\% \\
88	Dominant depth & 4--5 & 2--3 \\
89	Predicate style & synthetic & real-world \\
90	FOL source & GPT-4o (silver) & human (gold) \\
91	\bottomrule
92	\end{tabular}}
93	\end{table}
94	
95	ProofFOL problems are structurally more complex ($3.4{\times}$ more premises) but use simpler, synthetic predicates (e.g., \texttt{Blue(x)}, \texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.
96	The absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.
97	
98	\section{Extended Discussion}
99	\label{app:extended-discussion}
100	
101	\paragraph{What ISR measures and what it does not.}
102	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
103	This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.
104	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
105	ISR and downstream task performance are uncorrelated.
106	ISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
107	
108	Critically, low ISR carries different semantics depending on the training objective.
109	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
110	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
111	ISR values must always be interpreted relative to the optimization objective that produced them.
112	
113	\paragraph{ISR as $(n{-}1)$-coalition Shapley value.}
114	\label{app:shapley}
115	Define a cooperative game $(N, v)$ with player set $N = \{1,\ldots,n\}$ (components) and binary utility $v(S) = \mathbf{1}[S(S){=}\textit{proved}]$.
116	The Shapley value $\phi_i$ averages marginal contributions over all coalition sizes; ISR restricts to the maximal coalition $|S|{=}n{-}1$, giving $\phi_i^{\text{LOO}} = \frac{1}{n}[v(N) - v(N \setminus \{i\})]$.
117	Summing: $\text{ISR}(x) = \sum_i \phi_i^{\text{LOO}} = \frac{1}{n}\sum_i \mathbf{1}[v(N \setminus \{i\}){=}0]$, recovering Equation~\ref{eq:isr}.
118	This restriction trades full interaction detection for $O(n)$ cost; the binary solver output makes higher-order interactions unobservable from LOO alone (\S\ref{sec:sta}).
119	
120	\paragraph{The premise-count confound.}
121	\label{app:premise-count}
122	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
123	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
124	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
125	Premise-count-matched comparison eliminates the difference ($1.06\times$, McNemar's test $p{=}0.317$; Table~\ref{tab:fol-beta01-detailed}), confirming that the scalar ISR advantage is not statistically significant.
126	This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
127	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
128	Mode composition analysis (CE vs.\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\S\ref{app:hacking-modes}), not on the number of premises in the formalization.
129	
130	\begin{table}[h]
131	\centering
132	\resizebox{\columnwidth}{!}{%
133	\begin{tabular}{@{}llrrrr@{}}
134	\toprule
135	\textbf{Premises} & \textbf{Condition} & \textbf{$N_{\text{proved}}$} & \textbf{CE\%} & \textbf{TS\%} & \textbf{Genuine\%} \\
136	\midrule
137	$\leq$3 & ISR $\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\
138	         & Random $\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\
139	\midrule
140	4--6     & ISR $\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\
141	         & Random $\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\
142	\midrule
143	$\geq$7  & ISR $\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\
144	         & Random $\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\
145	\bottomrule
146	\end{tabular}}
147	\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}
148	\label{tab:premise-bin-modes}
149	\end{table}
150	
151	\begin{table*}[ht]
152	\centering
153	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
154	\label{tab:bootstrap-ci}
155	\small
156	\begin{tabular}{@{}lcccc@{}}
157	\toprule
158	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
159	\midrule
160	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (PG+FN corrected)}} \\
161	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
162	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
163	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
164	\midrule
165	\multicolumn{5}{@{}l}{\textit{TS gaming rate}} \\
166	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
167	\midrule
168	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
169	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
170	\bottomrule
171	\end{tabular}
172	\\[2pt]
173	{\small ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown. Pooled statistics treat within-seed samples as independent and serve as descriptive summaries only; the seed-stratified CMH test (\S\ref{app:statistical-details}) accounts for within-seed dependence.}
174	\end{table*}
175	
176	\paragraph{TS dose-response gradient.}
177	TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
178	The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
179	
180	\paragraph{Goodhart effects: implications.}
181	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.
182	The dose-response pattern maps onto the Manheim \& Garrabrant taxonomy~\citep{manheim-goodhart-taxonomy}: $\beta{=}0.1$ on FOLIO instantiates \emph{regressional} Goodhart ($P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR erroneously rewards the shortcut); $\beta{\geq}0.2$ introduces \emph{extremal} elements (PR collapse to 18\% vs.\ 48\% random at $\beta{=}0.3$).
183	The implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \S\ref{sec:crossdomain}).
184	
185	\paragraph{Single-seed unreliability.}
186	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
187	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\S\ref{sec:goodhart}).
188	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
189	
190	\paragraph{Classifier limitations.}
191	Text-match hacking classifiers have systematic blind spots that functional analysis exposes.
192	In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-detailed}).
193	One seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.
194	Practitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.
195	
196	\paragraph{Practical guidelines.}
197	\label{app:practical-guidelines}
198	Our findings yield five guidelines for GRPO-trained neurosymbolic systems:
199	(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.
200	(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\S\ref{sec:diagnostic}).
201	(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.
202	(4)~Treat LOO-based metrics as component-count-biased until normalized.
203	(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.
204	
205	\paragraph{Multiple testing correction.}
206	\label{app:statistical-details}
207	We define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).
208	Within the FOLIO family, Bonferroni correction at $\alpha{=}0.05$ yields adjusted thresholds of $p_{\text{adj}}{=}0.05/14{=}0.0036$.
209	Three primary comparisons survive correction: the TS rate difference (ISR vs.\ random; $p_{\text{bonf}}{=}1.82{\times}10^{-38}$), the SFT vs.\ exec-only non-hacking rate ($p_{\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\text{bonf}}{<}10^{-8}$).
210	The matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\text{bonf}}{=}0.056$), significant at $\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).
211	The ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.
212	Bonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.
213	We report the most conservative Bonferroni results for transparency.
214	
215	\paragraph{Mode distribution $\chi^2$ test.}
216	A pooled $3{\times}2$ contingency table (TS/CE/N-H $\times$ ISR/Random, 3-seed, 500 steps) yields $\chi^2{=}174.8$, $\text{df}{=}2$, $p{=}1.08{\times}10^{-38}$, confirming that ISR reward shifts the overall hacking mode composition, not merely the TS rate.
217	Per-seed tests are individually significant (s42: $\chi^2{=}15.8$, $p{<}0.001$; s43: $\chi^2{=}59.4$, $p{<}10^{-13}$; s44: $\chi^2{=}168.0$, $p{<}10^{-36}$).
218	The previously reported $\text{OR}_{\text{CMH}}{=}2.46$ for TS specifically ($p{<}10^{-8}$) captures a narrower slice of this distributional shift.
219	
220	
221	\section{Hacking Mode Definitions}
222	\label{app:hacking-modes}
223	
224	We identify eight distinct reward hacking modes across all experiments.
225	TS comprises two subtypes: TSa (text-match duplication, where the premise is textually identical to the conclusion) and TSb (obfuscated tautology, where the premise is logically equivalent but textually distinct; \S\ref{app:h8}).
226	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
227	
228	\begin{table}[t]
229	\centering
230	\small
231	\resizebox{\columnwidth}{!}{%
232	\begin{tabular}{lccccc}
233	\toprule
234	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
235	\midrule
236	CE embed       & 87 & 18 & 68 & 8 & 0$^\sharp$ \\
237	TS duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
238	PG prem-subset & 5  & 5  & 8   & 0 & --- \\
239	Tautological   & --- & --- & --- & --- & s42 \\
240	Repetition     & s43 & --- & --- & --- & --- \\
241	Contradiction  & 1k & --- & --- & --- & --- \\
242	Cmplx.\ vacuous& 0  & 0  & 1  & 0 & --- \\
243	Query-as-fact  & --- & --- & --- & --- & s44 \\
244	\midrule
245	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
246	\bottomrule
247	\end{tabular}}
248	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}). \texttt{1k} denotes a mode observed only at the 1000-step checkpoint. CE and PG can co-occur; Table~\ref{tab:goodhart-landscape} applies PG${>}$CE priority, reducing Random CE by ${\sim}2$\,pp relative to counts here.}
249	\label{tab:hacking-taxonomy}
250	\end{table}
251	
252	Table~\ref{tab:hacking-taxonomy} provides a compact cross-condition summary; Table~\ref{tab:hacking-taxonomy-app} below gives the extended breakdown.
253	
254	\begin{table*}[ht]
255	\centering
256	\small
257	\begin{tabular}{@{}llcccc@{}}
258	\toprule
259	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
260	\midrule
261	CE & Concl.\ in premises & 87 & 18 & 68 & 8 \\
262	TS & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
263	PG & Premise-subset gaming & 5 & 5 & 8 & 0 \\
264	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
265	Repetition & Output degen. & $\bullet$ & --- & --- & --- \\
266	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & --- & --- & --- \\
267	C-w/o-utility & Complex, redundant & 0 & 0 & 1 & 0 \\
268	Q-as-fact & Atom = fact+query & --- & --- & --- & --- \\
269	\bottomrule
270	\end{tabular}
271	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\dagger$Random TS driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: CE${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
272	\label{tab:hacking-taxonomy-app}
273	\end{table*}
274	
275	\paragraph{Classifier Validation.}
276	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
277	CE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
278	No training data or manual annotation is used for classification.
279	
280	To estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
281	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
282	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
283	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
284	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
285	\paragraph{Boundary case validation.}
286	Stratified validation across 82 samples (all five hacking categories) yields Cohen's $\kappa{=}1.0$; independent re-annotation confirms full agreement.
287	Structured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.
288	Short-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.
289	Low-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.
290	3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.
291	
292	\begin{table}[h]
293	\centering
294	\small
295	\begin{tabular}{@{}lcr@{}}
296	\toprule
297	\textbf{Mode} & \textbf{Val.\ $N$} & \textbf{Prec.} \\
298	\midrule
299	CE (Concl.\ Embed.) & 80$^\dagger$ & 1.00 \\
300	TS (Tautological) & 7 & 1.00 \\
301	PG (Premise-Subset) & 20 & 1.00 \\
302	Contradiction & 20 & 1.00 \\
303	Genuine & 25 & 1.00 \\
304	\midrule
305	\textbf{Overall} & \textbf{152} & \textbf{1.00} \\
306	\bottomrule
307	\end{tabular}
308	\caption{Per-mode classifier precision on 152 manually validated samples (stratified + boundary + random; three exercises pooled). $^\dagger$Includes 50 randomly sampled CE$\cup$TS outputs (pool ratio CE:TS${=}$374:2). Recall is not estimable from a validation-only design.}
309	\label{tab:classifier-precision}
310	\end{table}
311	
312	The TS\textsubscript{b} subcategory (functional LOO tautologies undetectable by text matching) provides a lower bound on TS recall: ${\geq}91\%$ ($149/163$) under ISR $\beta{=}0.1$. Other modes' recall is not estimable from the validation-only design; non-hacking rates throughout should be interpreted as upper bounds.
313	
314	\subsection{PG -- Premise-Subset Gaming}
315	\label{app:h8}
316	
317	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).
318	We term this \textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
319	
320	\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
321	Automated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.
322	
323	\paragraph{Audit scope and limitations.}
324	Full PG audit was completed for ISR $\beta{=}0.1$ seed~42 only.
325	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.
326	Random $\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.
327	
328	\paragraph{TS false-negative correction (TSb obfuscated tautology).}
329	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
330	Manual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
331	We classify these as \textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.
332	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\S\ref{sec:taxonomy}).
333	After correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.
334	
335	\paragraph{Impact on non-hacking-rate comparison.}
336	After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
337	The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
338	
339	\subsection{CE -- Conclusion Embedding}
340	
341	\paragraph{Definition.}
342	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
343	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
344	
345	\paragraph{Example (FOL).}
346	\smallskip\noindent\rule{\columnwidth}{0.3pt}
347	{\small\begin{verbatim}
348	Premises:
349	  all x (bird(x) -> flies(x)).
350	  bird(tweety).
351	  flies(tweety).  % conclusion embedded
352	Conclusion: flies(tweety).
353	\end{verbatim}}
354	\noindent\rule{\columnwidth}{0.3pt}\smallskip
355	
356	\paragraph{ISR interaction.}
357	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
358	ISR does not distinguish trivial from substantive necessity.
359	
360	\paragraph{Prevalence.}
361	Conclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\% across all RL conditions.
362	Under exec-only and Random reward, it manifests as CE (69--93\%); under ISR reward, it shifts to TS (70.6\% pooled).
363	
364	
365	\subsection{TSa -- Conclusion Duplication (Standard)}
366	
367	\paragraph{Definition.}
368	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
369	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
370	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
371	
372	\paragraph{Example (FOL).}
373	\smallskip\noindent\rule{\columnwidth}{0.3pt}
374	{\small\begin{verbatim}
375	Premises:
376	  all x ((A(x)&B(x))->(C(x)|D(x))).
377	Conclusion:
378	  all x ((A(x)&B(x))->(C(x)|D(x))).
379	\end{verbatim}}
380	\noindent\rule{\columnwidth}{0.3pt}\smallskip
381	
382	\paragraph{ISR interaction.}
383	ISR~$\approx 0.8$--$1.0$.
384	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
385	TSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.
386	
387	\paragraph{Prevalence.}
388	TSa (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
389	Combined TS (TSa + TSb): 70.6\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).
390	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all TSa; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
391	
392	
393	\subsection{TSb -- Obfuscated Tautology}
394	
395	\paragraph{Definition.}
396	A single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.
397	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
398	
399	\paragraph{Example (FOL, vacuous quantifier wrapping).}
400	\smallskip\noindent\rule{\columnwidth}{0.3pt}
401	{\small\begin{verbatim}
402	Premises:
403	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
404	Conclusion:
405	  all x ((A(x)&B(x))->(C(x)|D(x))).
406	\end{verbatim}}
407	\noindent\rule{\columnwidth}{0.3pt}\smallskip
408	
409	\noindent The premise introduces a vacuous variable $y$, unified with~$x$ at proof time; the formulas are logically equivalent but textually distinct.
410	
411	\paragraph{ISR interaction.}
412	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
413	TSb simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).
414	This triple gaming makes TSb the most complete Goodhart case we observe.
415	
416	\paragraph{Prevalence.}
417	Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
418	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
419	
420	
421	\subsection{Tautological Collapse}
422	
423	\paragraph{Definition.}
424	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
425	
426	\paragraph{Example (FOL).}
427	\smallskip\noindent\rule{\columnwidth}{0.3pt}
428	\begin{verbatim}
429	Premises: p(a).
430	Conclusion: p(a).
431	\end{verbatim}
432	\noindent\rule{\columnwidth}{0.3pt}\smallskip
433	
434	\paragraph{ISR interaction.}
435	ISR~$=1.0$ (the sole premise is necessary).
436	Distinguished from TS by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
437	
438	\paragraph{Prevalence.}
439	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% TS by strict classifier).
440	Also observed in Prolog exec+STA seed~42 (100\% TS, PR~$=0.50$).
441	
442	
443	\subsection{Repetition Collapse}
444	
445	\paragraph{Definition.}
446	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
447	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
448	
449	\paragraph{Example (Prolog).}
450	\smallskip\noindent\rule{\columnwidth}{0.3pt}
451	\begin{verbatim}
452	penguin(fido).
453	penguin(fido).
454	penguin(fido).
455	... (repeated to 512 tokens)
456	query(penguin(fido)).
457	\end{verbatim}
458	\noindent\rule{\columnwidth}{0.3pt}\smallskip
459	
460	\paragraph{ISR interaction.}
461	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
462	ISR correctly diagnoses this degeneration.
463	
464	\paragraph{Prevalence.}
465	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
466	
467	
468	\subsection{Complexity-without-Utility}
469	
470	\paragraph{Definition.}
471	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.
472	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
473	
474	\paragraph{Example (FOL).}
475	\smallskip\noindent\rule{\columnwidth}{0.3pt}
476	{\small\begin{verbatim}
477	Premises:
478	  all x all y (R(x,y) ->
479	    exists z (S(x,z) & T(z,y))).
480	  all x (P(x) -> Q(x)).
481	  P(a).            % only this needed
482	Conclusion: Q(a).
483	\end{verbatim}}
484	\noindent\rule{\columnwidth}{0.3pt}\smallskip
485	
486	\paragraph{ISR interaction.}
487	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
488	This is the mode ISR is best calibrated for.
489	
490	\paragraph{Prevalence.}
491	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
492	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
493	
494	
495	\subsection{Contradiction Explosion}
496	
497	\paragraph{Definition.}
498	The component count grows unboundedly over training.
499	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
500	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
501	
502	\paragraph{Example (FOL, 1000-step exec-only).}
503	\smallskip\noindent\rule{\columnwidth}{0.3pt}
504	{\small\begin{verbatim}
505	Premises:
506	  c1. c2. c3. ... c18. % 18.55 mean
507	  % conclusion embedded among premises
508	Conclusion: Q(a).
509	\end{verbatim}}
510	\noindent\rule{\columnwidth}{0.3pt}\smallskip
511	
512	\paragraph{ISR interaction.}
513	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
514	
515	\paragraph{Prevalence.}
516	Observed in extended exec-only training (seed~42, 1000 steps).
517	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
518	
519	
520	\subsection{Query-as-Fact Gaming}
521	
522	\paragraph{Definition.}
523	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
524	Prolog trivially proves the query by unifying with the fact.
525	This mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.
526	
527	\paragraph{Example (Prolog).}
528	\smallskip\noindent\rule{\columnwidth}{0.3pt}
529	\begin{verbatim}
530	% NL: "Fido is happy."
531	% Model output:
532	fido_is_happy.
533	:- fido_is_happy.     % query = fact
534	\end{verbatim}
535	\noindent\rule{\columnwidth}{0.3pt}\smallskip
536	
537	\paragraph{ISR interaction.}
538	ISR~$\approx 0.9$--$1.0$.
539	The single fact is trivially necessary (its removal breaks the query), inflating ISR.
540	Functionally equivalent to TS but with a distinct surface mechanism.
541	
542	\paragraph{Prevalence.}
543	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
544	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
545	
546	
547	\section{Per-Seed Detailed Results}
548	\label{app:detailed-results}
549	
550	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
551	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
552	ISR values are proved-only ISR$^*$.
553	
554	\begin{table*}[t]
555	\centering
556	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\times}2$ vs.\ $2{\times}4$, mathematically equivalent).}
557	\label{tab:fol-detailed}
558	\label{tab:fol-beta01-detailed}
559	\small
560	\setlength{\tabcolsep}{3pt}
561	\resizebox{\textwidth}{!}{%
562	\begin{tabular}{@{}llccccccl@{}}
563	\toprule
564	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
565	\midrule
566	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
567	Base model (no training)
568	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
569	Ground-truth FOL
570	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
571	SFT
572	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
573	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
574	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
575	\cmidrule(l){2-9}
576	  & \multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \textbf{92.3} & $n{=}39$ proved \\
577	\midrule
578	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
579	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
580	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}5.4\%$ \\
581	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
582	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
583	  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\
584	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
585	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & PG${=}15\%$ \\
586	\cmidrule(l){2-9}
587	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.68{\pm}0.47$ & $0.238{\pm}0.30$ & & & & 500-step \\
588	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.02$ & $0.029{\pm}0.05$ & & & $2.1{\pm}3.6$ & 1000-step \\
589	\midrule
590	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
591	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed CE+TS+PG \\
592	  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\
593	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\
594	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\
595	  & 45$^\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \textbf{54.8} & PG${=}1$; $n{=}42$ \\
596	  & 46$^\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \textbf{54.5} & PG${=}4$; $n{=}77$ \\
597	\cmidrule(l){2-9}
598	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.77{\pm}0.14$ & $0.716{\pm}0.26$ & & & & 500-step (s42--44) \\
599	  & \multicolumn{2}{l}{5-seed mean$\pm$std} & $0.70{\pm}0.19$ & $0.633{\pm}0.23$ & & & & 500-step (s42--46) \\
600	\midrule
601	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
602	  & \multicolumn{8}{l}{See Table~\ref{tab:beta03-detailed} for per-seed $\beta{=}0.3$ results.} \\
603	\midrule
604	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
605	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\
606	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\
607	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\cap$PG: 6) \\
608	\cmidrule(l){2-9}
609	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.87{\pm}0.08$ & $0.117{\pm}0.042$ & & & & TS seed-dep.: 0/38/0\% \\
610	\midrule
611	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
612	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$; $n_{\text{comp}} = 9.6$ \\
613	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
614	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
615	\cmidrule(l){2-9}
616	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & & \\
617	\midrule
618	\multicolumn{9}{@{}l}{\textit{Shuffled-ISR $\beta{=}0.1$ (deconfounding control)}} \\
619	  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
620	  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \textbf{87.5} & $n{=}16$ proved \\
621	  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
622	\cmidrule(l){2-9}
623	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.153{\pm}0.006$ & $0.559{\pm}0.015$ & $6.5$ & $6.5$ & \textbf{87.0} & $N{=}46$ proved \\
624	\bottomrule
625	\end{tabular}}% end resizebox
626	\end{table*}
627	
628	\begin{table*}[t]
629	\centering
630	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
631	\label{tab:prolog-detailed}
632	\small
633	\begin{tabular}{@{}llcccccl@{}}
634	\toprule
635	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
636	\midrule
637	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
638	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
639	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
640	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
641	\cmidrule(l){2-8}
642	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.53{\pm}0.31$ & $0.146{\pm}0.21$ & & & \\
643	\midrule
644	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
645	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & TS tautological \\
646	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional TS$^a$ \\
647	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
648	\cmidrule(l){2-8}
649	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.62{\pm}0.31$ & $0.699{\pm}0.45$ & & & 3/3 Goodhart, 0\% non-hacking \\
650	\bottomrule
651	\end{tabular}
652	
653	\vspace{4pt}
654	{\small
655	$^a$ Strict TS classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
656	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\
657	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
658	}
659	\end{table*}
660	
661	\begin{table*}[t]
662	\centering
663	\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\S\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\text{f50}}{>}0.90$.}
664	\label{tab:prooffol-detailed}
665	\small
666	\begin{tabular}{@{}llcccccl@{}}
667	\toprule
668	\textbf{Condition} & \textbf{Seed} & \textbf{PR$_{\text{f50}}$} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{Genuine\%} & \textbf{Notes} \\
669	\midrule
670	Base & --- & 0.16 & 0.310 & 0 & 0 & \textbf{100} & $n{=}16$ proved \\
671	\midrule
672	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
673	  & 42 & ${\approx}$1.0 & 0.066 & \textbf{100} & 0 & 0 & $n{=}99$; stable \\
674	  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\
675	  & 44 & ${\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\
676	\cmidrule(l){2-8}
677	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{17.4\% genuine (mean of seeds)} & \\
678	\midrule
679	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
680	  & 42 & 0.35 & 0.12 & 0 & 0 & \textbf{100} & $n{=}46$; collapsed \\
681	  & 43 & ${\approx}$0.47 & ${\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\
682	  & 44 & 0.49 & 0.145 & 0 & 0 & \textbf{100} & $n{=}66$; oscillation \\
683	\cmidrule(l){2-8}
684	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{\textbf{76.8\%} genuine (mean of seeds)} & \\
685	\bottomrule
686	\end{tabular}
687	
688	\vspace{4pt}
689	{\small Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}
690	\end{table*}
691	
692	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
693	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
694	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
695	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.
696	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
697	
698	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
699	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
700	seed~42 produces clean TS tautologies (single premise~$=$~conclusion),
701	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
702	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
703	The diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
704	
705	\subsection{Per-Seed Results at $\beta{=}0.2$ and $\beta{=}0.3$}
706	\label{app:beta03}
707	
708	Table~\ref{tab:beta03-detailed} reports per-seed results for ISR at $\beta{=}0.2$ and both ISR and Random at $\beta{=}0.3$.
709	At $\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\% or near-100\% TS), confirming $\beta{\geq}0.2$ as the extremal Goodhart regime.
710	The three ISR $\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
711	
712	\begin{table*}[ht]
713	\centering
714	\caption{Per-seed results at $\beta{=}0.2$ and $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}
715	\label{tab:beta03-detailed}
716	\small
717	\begin{tabular}{@{}llcccccl@{}}
718	\toprule
719	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Mode} \\
720	\midrule
721	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.2$}} \\
722	  & 42 & 1.00 & 0.602 & \textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\
723	  & 43 & 0.96 & 0.552 & \textbf{96.9} & 1.0 & 0 & PG${=}2$ \\
724	  & 44 & 0.94 & 0.964 & \textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\
725	\cmidrule(l){2-8}
726	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.03$ & $0.71{\pm}0.22$ & & & 3/3 TS Goodhart \\
727	\midrule
728	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
729	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\
730	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\
731	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure TS Goodhart \\
732	\cmidrule(l){2-8}
733	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.66{\pm}0.42$ & $0.39{\pm}0.31$ & & & \\
734	\midrule
735	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
736	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ \\
737	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
738	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
739	\cmidrule(l){2-8}
740	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & \\
741	\bottomrule
742	\end{tabular}
743	\end{table*}
744	
745	\FloatBarrier
746	
747	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
748	\label{app:100step}
749	
750	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%, higher than SFT (13.0\%, 3-seed pooled) but still early in training.
751	Of the 32 proved samples, 9 (28.1\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
752	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
753	This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
754	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
755	
756	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
757	\label{app:o1-ablation}
758	
759	All main experiments (\S\ref{sec:diagnostic}--\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\texttt{execution\_fast\_sta}) but is used only in the ablation reported here.
760	The two signals measure fundamentally different properties, not approximations of the same quantity.
761	The binary signal tests \emph{collective} premise necessity: $\text{fast\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
762	LOO tests \emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.
763	
764	\paragraph{Evaluation-time comparison.}
765	Across 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.
766	This renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.
767	By contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.
768	Of 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.
769	
770	\paragraph{Training-time ablation.}
771	As a training reward ($r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$, functionally zero, compared to $\text{ISR}^*{=}0.132$ under exec-only and $\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\beta{=}0.1$.
772	The tautology check depresses prove rate by 30\,pp relative to exec-only ($63\%$ vs.\ $93\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.
773	That even the fine-grained $O(n)$ LOO signal, which \emph{does} provide per-component necessity feedback, is ultimately gamed (\S\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.
774	
775	\paragraph{Computational overhead.}
776	Full LOO requires $n{+}1$ solver calls per sample (mean $n{\approx}6$ for FOLIO).
777	With Prover9 at ${\sim}5$\,ms per call, STA evaluation adds ${\sim}55$\,ms per sample versus ${\sim}4$\,s for LLM inference (${<}1\%$ overhead).
778	The $O(1)$ binary check adds a single solver call per proved sample (${<}2\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.
779	
780	\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}
781	\label{app:llama-coldstart}
782	
783	We applied the identical GRPO configuration (Table~\ref{tab:hyperparams}) to LLaMA-3.2-3B~\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).
784	Across 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\footnote{This run was also affected by a generation-termination configuration issue (dual EOS tokens); the zero prove rate reflects both the base model's lack of FOL generation capability and truncated outputs.}
785	This establishes a \emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.
786	Qwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\ 4B), likely reflecting pretraining data composition.
787	An SFT warmstart (3 epochs on gold formalizations, lr$=$2$\times$10$^{-5}$) achieves $\text{PR}{=}16\%$ ($n{=}100$) after correcting the generation-termination issue.
788	However, the model produces Unicode FOL notation ($\forall$, $\to$, $\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data; the 16\% prove rate reflects Prover9's partial Unicode tolerance rather than correct format adherence.
789	Subsequent GRPO runs (exec-only, 500 steps from SFT warmstart, 3 seeds) fail to improve beyond SFT baseline ($\text{PR}{=}15.0{\pm}1.0\%$, $n{=}14$--$16$ proved per seed), yet produce no structural degeneration: $86.6{\pm}0.9\%$ of proved samples are genuine across seeds, with cross-seed variance near zero ($\sigma_{\text{PR}}{=}1$\,pp).
790	This contrasts sharply with Qwen3-4B, where GRPO reaches $93\%$ PR but collapses to $8\%$ genuine with high cross-seed variance.
791	The result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.
792	
793	\subsection{Seed-Dependent Convergence in Exec-Only GRPO}
794	\label{app:seed-convergence}
795	
796	Not all exec-only seeds converge.
797	Of 6 seeds tested (s42--s46, s52; s52 uses $K{=}4$, all others $K{=}8$), we observe three regimes: \emph{converging with degeneration} (s42: $\text{PR}{=}93\%$, genuine${=}7.5\%$; s44: $\text{PR}{=}96\%$, genuine${=}0\%$; s46: $\text{PR}{=}93\%$ at 500 steps), \emph{slow convergence with degeneration} (s43: $\text{PR}{=}14\%$ but $100\%$ hacking at 500 steps), and \emph{non-converging} (s45: $\text{PR}{=}15\%$, genuine${=}86.7\%$; s52: $\text{PR}{=}14\%$, genuine${=}85.7\%$).
798	Non-converging seeds retain high genuine rates (85--87\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.
799	Extended training to 1000 steps for s45 confirms persistent non-convergence ($\text{PR}{=}15\%$, $\text{ISR}^*{=}0.592$, genuine${=}86.7\%$, $n{=}15$ proved); the model neither improves nor degenerates.
800	
801	This parallels the LLaMA-3.2-3B finding (Appendix~\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.
802	Both cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.
803	
804	\subsection{$N{=}2$ Sensitivity Analysis (Excluding Seed 43)}
805	\label{app:n2-sensitivity}
806	
807	Seed~43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding (\S\ref{app:setup}).
808	To assess whether this non-standard protocol affects qualitative conclusions, Table~\ref{tab:n2-sensitivity} reports pooled statistics from seeds~42 and~44 only.
809	
810	\begin{table}[h]
811	\centering
812	\resizebox{\columnwidth}{!}{%
813	\begin{tabular}{@{}lccc@{}}
814	\toprule
815	\textbf{Condition} & \textbf{PR (\%)} & \textbf{ISR$^*$} & \textbf{N-H (\%)} \\
816	\midrule
817	Exec-only 500-step & $95.5 \pm 3.5$ & $0.357 \pm 0.318$ & $3.8 \pm 5.3$ \\
818	Exec-only 1000-step & $98.0 \pm 2.8$ & $0.003 \pm 0.001$ & $0.0 \pm 0.0$ \\
819	ISR $\beta{=}0.1$ 500-step & $85.0 \pm 5.7$ & $0.659 \pm 0.344$ & $8.7 \pm 12.2$ \\
820	\bottomrule
821	\end{tabular}}
822	\caption{Pooled statistics excluding seed~43 ($N{=}2$, seeds~42 and~44 only). Mean$\pm$std of per-seed values. Qualitative patterns preserved: exec-only converges to ${\leq}7.5\%$ non-hacking; ISR $\beta{=}0.1$ shifts composition toward TS.}
823	\label{tab:n2-sensitivity}
824	\end{table}
825	
826	Excluding seed~43, exec-only converges to ${\leq}7.5\%$ non-hacking at 500 steps and $0\%$ at 1000 steps.
827	Under ISR $\beta{=}0.1$, TS dominates both remaining seeds (s42: $16\%$, s44: $100\%$), confirming that ISR reward shifts hacking composition toward tautological shortcuts independent of the s43 evaluation anomaly.
828	The large per-seed ISR$^*$ variance ($0.357 \pm 0.318$) reflects different degeneration modes (CE in s42 vs.\ TS in s44), not data quality issues.
829	
830	\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}
831	\label{app:8b-results}
832	
833	To test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yielding zero GRPO advantage and no learning signal).
834	Table~\ref{tab:8b-combined} summarizes configuration differences and results.
835	
836	\begin{table}[H]
837	\centering
838	\small
839	\begin{tabular}{lcc}
840	\toprule
841	& \textbf{Qwen3-4B} & \textbf{Qwen3-8B} \\
842	\midrule
843	Rollouts ($K$) & 4 & 8 \\
844	Batch size & 4 & 1 \\
845	Gradient accum. & 2 & 16 \\
846	Effective batch & 8 & 16 \\
847	\bottomrule
848	\end{tabular}
849	
850	\vspace{4pt}
851	
852	\resizebox{\columnwidth}{!}{%
853	\begin{tabular}{lcccc}
854	\toprule
855	\textbf{Config} & \textbf{PR\%} & \textbf{Genuine\%} & \textbf{Converged?} & \textbf{Gradient} \\
856	\midrule
857	4B $K{=}4$ s42 & 93 & 7.5 & Yes (degenerate) & Sufficient \\
858	8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\
859	8B $K{=}8$ s42 & 14 & 92.9 & No & Partial \\
860	\bottomrule
861	\end{tabular}}
862	\caption{Cross-scale: Qwen3-4B vs.\ Qwen3-8B. \textbf{Top}: Configuration; $K{=}8$ required at 8B because $K{=}4$ produces near-identical rollouts. \textbf{Bottom}: Results; 4B converges with degeneration, both 8B configurations fail to converge, preserving structural integrity.}
863	\label{tab:8b-combined}
864	\end{table}
865	
866	We first tested $K{=}4$ (matching the 4B configuration): the 8B model produces near-identical rollouts across all four completions, yielding zero GRPO advantage throughout 500 steps and no learning signal ($\text{PR}{=}15.5\%$, cold-start stagnation).
867	Increasing to $K{=}8$ provides non-zero reward variance during mid-training (approximately 40--50\% of steps between 20--370 show non-zero advantage), but this signal proves insufficient for convergence: held-out evaluation yields $\text{PR}{=}14\%$ ($n{=}14$ proved), $\text{ISR}^*{=}0.573$, genuine${=}92.9\%$ (13/14), with a single CE sample.
868	Cosine learning-rate decay combined with insufficient early bootstrap appears to prevent the model from escaping the low-PR regime.
869	
870	This result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.
871	Together, these cases establish a convergence threshold for GRPO-driven degeneration: the structural collapse documented in \S\ref{sec:diagnostic} requires successful RL optimization as a prerequisite, and at 8B scale the rollout diversity bottleneck prevents this optimization from occurring under our configuration.
872	
873	\section{Use of AI Assistants}
874	\label{app:ai-assistants}
875	
876	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
877	\begin{itemize}
878	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
879	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
880	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
881	\end{itemize}
882	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8d16ff8-d87a-41cf-8326-cf592cbaecd4",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "6d0bdbb8-62a0-402f-aa5c-23764bed507e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 4 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Compute resources.}\nExperiments were run on single-GPU setups (NVIDIA RTX 4090 24\\,GB and RTX PRO 6000 96\\,GB).\nEach GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).\nTotal compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.\n\n\\paragraph{SFT convergence.}\nSFT training converged across all three seeds: final-step loss ${\\leq}0.04$ and token accuracy ${>}99\\%$ after ${\\sim}8$ epochs on 500 examples (seed~42: $0.029$; seed~44: $0.033$); the 1000-step extension further decreases loss to $0.017$.\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol.\n\n\\paragraph{Reward formulation.}\nAn additive variant ($r = r_{\\text{exec}} + \\beta\\,\\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\\text{exec}}\\cdot(1+\\beta\\,\\text{ISR})$ ensures ISR modulates only proved outputs.\n\n\\paragraph{ProofFOL dataset construction.}\n\\label{app:prooffol-construction}\nProofFOL is derived from ProofWriter~\\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \\citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\\sim}70\\%$ retention; failures from timeouts, unsupported constructs, and translation errors).\nOf the translated examples, 99.1\\% parse successfully (92 skipped due to empty FOL output).\nWe sample 500 training and 100 evaluation examples (seed~42) from the verified pool.\nTable~\\ref{tab:prooffol-vs-folio} compares key structural properties.\n\n\\begin{table}[!ht]\n\\centering\n\\caption{ProofFOL vs.\\ FOLIO structural comparison (training sets, $n{=}500$ each).}\n\\label{tab:prooffol-vs-folio}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Property} & \\textbf{ProofFOL} & \\textbf{FOLIO} \\\\\n\\midrule\nFOL premises (mean$\\pm$std) & $18.2 \\pm 3.2$ & $5.3 \\pm 1.4$ \\\\\n\\quad Ground facts & $10.2 \\pm 3.0$ & $1.8 \\pm 1.5$ \\\\\n\\quad Rules & $8.1 \\pm 1.1$ & $3.5 \\pm 1.9$ \\\\\nXOR ($\\oplus$) samples & 0\\% & 37.2\\% \\\\\nDominant depth & 4--5 & 2--3 \\\\\nPredicate style & synthetic & real-world \\\\\nFOL source & GPT-4o (silver) & human (gold) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nProofFOL problems are structurally more complex ($3.4{\\times}$ more premises) but use simpler, synthetic predicates (e.g., \\texttt{Blue(x)}, \\texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.\nThe absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{ISR as $(n{-}1)$-coalition Shapley value.}\n\\label{app:shapley}\nDefine a cooperative game $(N, v)$ with player set $N = \\{1,\\ldots,n\\}$ (components) and binary utility $v(S) = \\mathbf{1}[S(S){=}\\textit{proved}]$.\nThe Shapley value $\\phi_i$ averages marginal contributions over all coalition sizes; ISR restricts to the maximal coalition $|S|{=}n{-}1$, giving $\\phi_i^{\\text{LOO}} = \\frac{1}{n}[v(N) - v(N \\setminus \\{i\\})]$.\nSumming: $\\text{ISR}(x) = \\sum_i \\phi_i^{\\text{LOO}} = \\frac{1}{n}\\sum_i \\mathbf{1}[v(N \\setminus \\{i\\}){=}0]$, recovering Equation~\\ref{eq:isr}.\nThis restriction trades full interaction detection for $O(n)$ cost; the binary solver output makes higher-order interactions unobservable from LOO alone (\\S\\ref{sec:sta}).\n\n\\paragraph{The premise-count confound.}\n\\label{app:premise-count}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$, McNemar's test $p{=}0.317$; Table~\\ref{tab:fol-beta01-detailed}), confirming that the scalar ISR advantage is not statistically significant.\nThis bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.\n\n\\begin{table}[h]\n\\centering\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\n\\textbf{Premises} & \\textbf{Condition} & \\textbf{$N_{\\text{proved}}$} & \\textbf{CE\\%} & \\textbf{TS\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\n$\\leq$3 & ISR $\\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\\\\n         & Random $\\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\\\\n\\midrule\n4--6     & ISR $\\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\\\\n         & Random $\\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\\\\n\\midrule\n$\\geq$7  & ISR $\\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\\\\n         & Random $\\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}\n\\label{tab:premise-bin-modes}\n\\end{table}\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (PG+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\small ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown. Pooled statistics treat within-seed samples as independent and serve as descriptive summaries only; the seed-stratified CMH test (\\S\\ref{app:statistical-details}) accounts for within-seed dependence.}\n\\end{table*}\n\n\\paragraph{TS dose-response gradient.}\nTS tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ TS ($36/262$ pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient (random $\\beta{=}0.1$ ($13.7\\%$) $\\to$ random $\\beta{=}0.3$ (4--7 TSa per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.\n\n\\paragraph{Goodhart effects: implications.}\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern maps onto the Manheim \\& Garrabrant taxonomy~\\citep{manheim-goodhart-taxonomy}: $\\beta{=}0.1$ on FOLIO instantiates \\emph{regressional} Goodhart ($P{\\to}P$ tautologies yield $\\text{ISR}{\\geq}0.5$, so ISR erroneously rewards the shortcut); $\\beta{\\geq}0.2$ introduces \\emph{extremal} elements (PR collapse to 18\\% vs.\\ 48\\% random at $\\beta{=}0.3$).\nThe implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \\S\\ref{sec:crossdomain}).\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\\paragraph{Classifier limitations.}\nText-match hacking classifiers have systematic blind spots that functional analysis exposes.\nIn Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-detailed}).\nOne seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.\nPractitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.\n\n\\paragraph{Practical guidelines.}\n\\label{app:practical-guidelines}\nOur findings yield five guidelines for GRPO-trained neurosymbolic systems:\n(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.\n(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\\S\\ref{sec:diagnostic}).\n(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.\n(4)~Treat LOO-based metrics as component-count-biased until normalized.\n(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.\n\n\\paragraph{Multiple testing correction.}\n\\label{app:statistical-details}\nWe define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).\nWithin the FOLIO family, Bonferroni correction at $\\alpha{=}0.05$ yields adjusted thresholds of $p_{\\text{adj}}{=}0.05/14{=}0.0036$.\nThree primary comparisons survive correction: the TS rate difference (ISR vs.\\ random; $p_{\\text{bonf}}{=}1.82{\\times}10^{-38}$), the SFT vs.\\ exec-only non-hacking rate ($p_{\\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\\text{bonf}}{<}10^{-8}$).\nThe matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\\text{bonf}}{=}0.056$), significant at $\\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).\nThe ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.\nBonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.\nWe report the most conservative Bonferroni results for transparency.\n\n\\paragraph{Mode distribution $\\chi^2$ test.}\nA pooled $3{\\times}2$ contingency table (TS/CE/N-H $\\times$ ISR/Random, 3-seed, 500 steps) yields $\\chi^2{=}174.8$, $\\text{df}{=}2$, $p{=}1.08{\\times}10^{-38}$, confirming that ISR reward shifts the overall hacking mode composition, not merely the TS rate.\nPer-seed tests are individually significant (s42: $\\chi^2{=}15.8$, $p{<}0.001$; s43: $\\chi^2{=}59.4$, $p{<}10^{-13}$; s44: $\\chi^2{=}168.0$, $p{<}10^{-36}$).\nThe previously reported $\\text{OR}_{\\text{CMH}}{=}2.46$ for TS specifically ($p{<}10^{-8}$) captures a narrower slice of this distributional shift.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify eight distinct reward hacking modes across all experiments.\nTS comprises two subtypes: TSa (text-match duplication, where the premise is textually identical to the conclusion) and TSb (obfuscated tautology, where the premise is logically equivalent but textually distinct; \\S\\ref{app:h8}).\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 68 & 8 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 5  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 1  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint. CE and PG can co-occur; Table~\\ref{tab:goodhart-landscape} applies PG${>}$CE priority, reducing Random CE by ${\\sim}2$\\,pp relative to counts here.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nTable~\\ref{tab:hacking-taxonomy} provides a compact cross-condition summary; Table~\\ref{tab:hacking-taxonomy-app} below gives the extended breakdown.\n\n\\begin{table*}[ht]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nCE & Concl.\\ in premises & 87 & 18 & 68 & 8 \\\\\nTS & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nPG & Premise-subset gaming & 5 & 5 & 8 & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & --- & --- & --- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & --- & --- & --- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 1 & 0 \\\\\nQ-as-fact & Atom = fact+query & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\\dagger$Random TS driven by seed~43 (38.3\\%); seeds~42/44: 0\\%. Exec: CE${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table*}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nCE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\\paragraph{Boundary case validation.}\nStratified validation across 82 samples (all five hacking categories) yields Cohen's $\\kappa{=}1.0$; independent re-annotation confirms full agreement.\nStructured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.\nShort-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.\nLow-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.\n3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcr@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Val.\\ $N$} & \\textbf{Prec.} \\\\\n\\midrule\nCE (Concl.\\ Embed.) & 80$^\\dagger$ & 1.00 \\\\\nTS (Tautological) & 7 & 1.00 \\\\\nPG (Premise-Subset) & 20 & 1.00 \\\\\nContradiction & 20 & 1.00 \\\\\nGenuine & 25 & 1.00 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{152} & \\textbf{1.00} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-mode classifier precision on 152 manually validated samples (stratified + boundary + random; three exercises pooled). $^\\dagger$Includes 50 randomly sampled CE$\\cup$TS outputs (pool ratio CE:TS${=}$374:2). Recall is not estimable from a validation-only design.}\n\\label{tab:classifier-precision}\n\\end{table}\n\nThe TS\\textsubscript{b} subcategory (functional LOO tautologies undetectable by text matching) provides a lower bound on TS recall: ${\\geq}91\\%$ ($149/163$) under ISR $\\beta{=}0.1$. Other modes' recall is not estimable from the validation-only design; non-hacking rates throughout should be interpreted as upper bounds.\n\n\\subsection{PG -- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).\nWe term this \\textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull PG audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.\n\n\\paragraph{TS false-negative correction (TSb obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{CE -- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as CE (69--93\\%); under ISR reward, it shifts to TS (70.6\\% pooled).\n\n\n\\subsection{TSa -- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nTSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nTSa (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined TS (TSa + TSb): 70.6\\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 13.7\\% (36/262, all TSa; driven by seed~43 at 38.3\\%, seeds~42 and~44 at 0\\%).\n\n\n\\subsection{TSb -- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\noindent The premise introduces a vacuous variable $y$, unified with~$x$ at proof time; the formulas are logically equivalent but textually distinct.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nTSb simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).\nThis triple gaming makes TSb the most complete Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound primarily in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from TS by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% TS by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% TS, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe single fact is trivially necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to TS but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\\times}2$ vs.\\ $2{\\times}4$, mathematically equivalent).}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \\textbf{92.3} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}5.4\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & PG${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.68{\\pm}0.47$ & $0.238{\\pm}0.30$ & & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.02$ & $0.029{\\pm}0.05$ & & & $2.1{\\pm}3.6$ & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed CE+TS+PG \\\\\n  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\\\\n  & 45$^\\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \\textbf{54.8} & PG${=}1$; $n{=}42$ \\\\\n  & 46$^\\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \\textbf{54.5} & PG${=}4$; $n{=}77$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.77{\\pm}0.14$ & $0.716{\\pm}0.26$ & & & & 500-step (s42--44) \\\\\n  & \\multicolumn{2}{l}{5-seed mean$\\pm$std} & $0.70{\\pm}0.19$ & $0.633{\\pm}0.23$ & & & & 500-step (s42--46) \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & \\multicolumn{8}{l}{See Table~\\ref{tab:beta03-detailed} for per-seed $\\beta{=}0.3$ results.} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\\cap$PG: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.87{\\pm}0.08$ & $0.117{\\pm}0.042$ & & & & TS seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$; $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Shuffled-ISR $\\beta{=}0.1$ (deconfounding control)}} \\\\\n  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \\textbf{87.5} & $n{=}16$ proved \\\\\n  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.153{\\pm}0.006$ & $0.559{\\pm}0.015$ & $6.5$ & $6.5$ & \\textbf{87.0} & $N{=}46$ proved \\\\\n\\bottomrule\n\\end{tabular}}% end resizebox\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.53{\\pm}0.31$ & $0.146{\\pm}0.21$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & TS tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional TS$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.62{\\pm}0.31$ & $0.699{\\pm}0.45$ & & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\small\n$^a$ Strict TS classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\\S\\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\\text{f50}}{>}0.90$.}\n\\label{tab:prooffol-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR$_{\\text{f50}}$} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{Genuine\\%} & \\textbf{Notes} \\\\\n\\midrule\nBase & --- & 0.16 & 0.310 & 0 & 0 & \\textbf{100} & $n{=}16$ proved \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & ${\\approx}$1.0 & 0.066 & \\textbf{100} & 0 & 0 & $n{=}99$; stable \\\\\n  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\\\\n  & 44 & ${\\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{17.4\\% genuine (mean of seeds)} & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 0.35 & 0.12 & 0 & 0 & \\textbf{100} & $n{=}46$; collapsed \\\\\n  & 43 & ${\\approx}$0.47 & ${\\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\\\\n  & 44 & 0.49 & 0.145 & 0 & 0 & \\textbf{100} & $n{=}66$; oscillation \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{\\textbf{76.8\\%} genuine (mean of seeds)} & \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\small Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean TS tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for ISR at $\\beta{=}0.2$ and both ISR and Random at $\\beta{=}0.3$.\nAt $\\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\\% or near-100\\% TS), confirming $\\beta{\\geq}0.2$ as the extremal Goodhart regime.\nThe three ISR $\\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.2$ and $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.2$}} \\\\\n  & 42 & 1.00 & 0.602 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\\\\n  & 43 & 0.96 & 0.552 & \\textbf{96.9} & 1.0 & 0 & PG${=}2$ \\\\\n  & 44 & 0.94 & 0.964 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.03$ & $0.71{\\pm}0.22$ & & & 3/3 TS Goodhart \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure TS Goodhart \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.66{\\pm}0.42$ & $0.39{\\pm}0.31$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\FloatBarrier\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nAll main experiments (\\S\\ref{sec:diagnostic}--\\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\\texttt{execution\\_fast\\_sta}) but is used only in the ablation reported here.\nThe two signals measure fundamentally different properties, not approximations of the same quantity.\nThe binary signal tests \\emph{collective} premise necessity: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nLOO tests \\emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.\n\n\\paragraph{Evaluation-time comparison.}\nAcross 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.\nThis renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.\nBy contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.\nOf 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.\n\n\\paragraph{Training-time ablation.}\nAs a training reward ($r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$, functionally zero, compared to $\\text{ISR}^*{=}0.132$ under exec-only and $\\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\\beta{=}0.1$.\nThe tautology check depresses prove rate by 30\\,pp relative to exec-only ($63\\%$ vs.\\ $93\\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.\nThat even the fine-grained $O(n)$ LOO signal, which \\emph{does} provide per-component necessity feedback, is ultimately gamed (\\S\\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.\n\n\\paragraph{Computational overhead.}\nFull LOO requires $n{+}1$ solver calls per sample (mean $n{\\approx}6$ for FOLIO).\nWith Prover9 at ${\\sim}5$\\,ms per call, STA evaluation adds ${\\sim}55$\\,ms per sample versus ${\\sim}4$\\,s for LLM inference (${<}1\\%$ overhead).\nThe $O(1)$ binary check adds a single solver call per proved sample (${<}2\\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.\n\n\\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}\n\\label{app:llama-coldstart}\n\nWe applied the identical GRPO configuration (Table~\\ref{tab:hyperparams}) to LLaMA-3.2-3B~\\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).\nAcross 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\\footnote{This run was also affected by a generation-termination configuration issue (dual EOS tokens); the zero prove rate reflects both the base model's lack of FOL generation capability and truncated outputs.}\nThis establishes a \\emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.\nQwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\\ 4B), likely reflecting pretraining data composition.\nAn SFT warmstart (3 epochs on gold formalizations, lr$=$2$\\times$10$^{-5}$) achieves $\\text{PR}{=}16\\%$ ($n{=}100$) after correcting the generation-termination issue.\nHowever, the model produces Unicode FOL notation ($\\forall$, $\\to$, $\\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data; the 16\\% prove rate reflects Prover9's partial Unicode tolerance rather than correct format adherence.\nSubsequent GRPO runs (exec-only, 500 steps from SFT warmstart, 3 seeds) fail to improve beyond SFT baseline ($\\text{PR}{=}15.0{\\pm}1.0\\%$, $n{=}14$--$16$ proved per seed), yet produce no structural degeneration: $86.6{\\pm}0.9\\%$ of proved samples are genuine across seeds, with cross-seed variance near zero ($\\sigma_{\\text{PR}}{=}1$\\,pp).\nThis contrasts sharply with Qwen3-4B, where GRPO reaches $93\\%$ PR but collapses to $8\\%$ genuine with high cross-seed variance.\nThe result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \\emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.\n\n\\subsection{Seed-Dependent Convergence in Exec-Only GRPO}\n\\label{app:seed-convergence}\n\nNot all exec-only seeds converge.\nOf 6 seeds tested (s42--s46, s52; s52 uses $K{=}4$, all others $K{=}8$), we observe three regimes: \\emph{converging with degeneration} (s42: $\\text{PR}{=}93\\%$, genuine${=}7.5\\%$; s44: $\\text{PR}{=}96\\%$, genuine${=}0\\%$; s46: $\\text{PR}{=}93\\%$ at 500 steps), \\emph{slow convergence with degeneration} (s43: $\\text{PR}{=}14\\%$ but $100\\%$ hacking at 500 steps), and \\emph{non-converging} (s45: $\\text{PR}{=}15\\%$, genuine${=}86.7\\%$; s52: $\\text{PR}{=}14\\%$, genuine${=}85.7\\%$).\nNon-converging seeds retain high genuine rates (85--87\\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.\nExtended training to 1000 steps for s45 confirms persistent non-convergence ($\\text{PR}{=}15\\%$, $\\text{ISR}^*{=}0.592$, genuine${=}86.7\\%$, $n{=}15$ proved); the model neither improves nor degenerates.\n\nThis parallels the LLaMA-3.2-3B finding (Appendix~\\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.\nBoth cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.\n\n\\subsection{$N{=}2$ Sensitivity Analysis (Excluding Seed 43)}\n\\label{app:n2-sensitivity}\n\nSeed~43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding (\\S\\ref{app:setup}).\nTo assess whether this non-standard protocol affects qualitative conclusions, Table~\\ref{tab:n2-sensitivity} reports pooled statistics from seeds~42 and~44 only.\n\n\\begin{table}[h]\n\\centering\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{PR (\\%)} & \\textbf{ISR$^*$} & \\textbf{N-H (\\%)} \\\\\n\\midrule\nExec-only 500-step & $95.5 \\pm 3.5$ & $0.357 \\pm 0.318$ & $3.8 \\pm 5.3$ \\\\\nExec-only 1000-step & $98.0 \\pm 2.8$ & $0.003 \\pm 0.001$ & $0.0 \\pm 0.0$ \\\\\nISR $\\beta{=}0.1$ 500-step & $85.0 \\pm 5.7$ & $0.659 \\pm 0.344$ & $8.7 \\pm 12.2$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pooled statistics excluding seed~43 ($N{=}2$, seeds~42 and~44 only). Mean$\\pm$std of per-seed values. Qualitative patterns preserved: exec-only converges to ${\\leq}7.5\\%$ non-hacking; ISR $\\beta{=}0.1$ shifts composition toward TS.}\n\\label{tab:n2-sensitivity}\n\\end{table}\n\nExcluding seed~43, exec-only converges to ${\\leq}7.5\\%$ non-hacking at 500 steps and $0\\%$ at 1000 steps.\nUnder ISR $\\beta{=}0.1$, TS dominates both remaining seeds (s42: $16\\%$, s44: $100\\%$), confirming that ISR reward shifts hacking composition toward tautological shortcuts independent of the s43 evaluation anomaly.\nThe large per-seed ISR$^*$ variance ($0.357 \\pm 0.318$) reflects different degeneration modes (CE in s42 vs.\\ TS in s44), not data quality issues.\n\n\\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}\n\\label{app:8b-results}\n\nTo test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yielding zero GRPO advantage and no learning signal).\nTable~\\ref{tab:8b-combined} summarizes configuration differences and results.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{Qwen3-4B} & \\textbf{Qwen3-8B} \\\\\n\\midrule\nRollouts ($K$) & 4 & 8 \\\\\nBatch size & 4 & 1 \\\\\nGradient accum. & 2 & 16 \\\\\nEffective batch & 8 & 16 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{PR\\%} & \\textbf{Genuine\\%} & \\textbf{Converged?} & \\textbf{Gradient} \\\\\n\\midrule\n4B $K{=}4$ s42 & 93 & 7.5 & Yes (degenerate) & Sufficient \\\\\n8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\\\\n8B $K{=}8$ s42 & 14 & 92.9 & No & Partial \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-scale: Qwen3-4B vs.\\ Qwen3-8B. \\textbf{Top}: Configuration; $K{=}8$ required at 8B because $K{=}4$ produces near-identical rollouts. \\textbf{Bottom}: Results; 4B converges with degeneration, both 8B configurations fail to converge, preserving structural integrity.}\n\\label{tab:8b-combined}\n\\end{table}\n\nWe first tested $K{=}4$ (matching the 4B configuration): the 8B model produces near-identical rollouts across all four completions, yielding zero GRPO advantage throughout 500 steps and no learning signal ($\\text{PR}{=}15.5\\%$, cold-start stagnation).\nIncreasing to $K{=}8$ provides non-zero reward variance during mid-training (approximately 40--50\\% of steps between 20--370 show non-zero advantage), but this signal proves insufficient for convergence: held-out evaluation yields $\\text{PR}{=}14\\%$ ($n{=}14$ proved), $\\text{ISR}^*{=}0.573$, genuine${=}92.9\\%$ (13/14), with a single CE sample.\nCosine learning-rate decay combined with insufficient early bootstrap appears to prevent the model from escaping the low-PR regime.\n\nThis result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.\nTogether, these cases establish a convergence threshold for GRPO-driven degeneration: the structural collapse documented in \\S\\ref{sec:diagnostic} requires successful RL optimization as a prerequisite, and at 8B scale the rollout diversity bottleneck prevents this optimization from occurring under our configuration.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform the related-work section.\n\\end{itemize}\n",
      "numLines": 882,
      "startLine": 1,
      "totalLines": 882
    }
  },
  "sourceToolAssistantUUID": "c8d16ff8-d87a-41cf-8326-cf592cbaecd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T14:06:03.023Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V2boamzU8UHhVJPfxrKX2T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d0bdbb8-62a0-402f-aa5c-23764bed507e",
  "isSidechain": false,
  "requestId": "req_011CbPR3YNpEEwNc3FHCp1RJ",
  "type": "assistant",
  "uuid": "931fb82d-d2f9-44e5-a728-0c78a2c04b2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBZrYVuiJU8rDYrzbSjnEq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9793,
      "cache_read_input_tokens": 53100,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 53100,
          "cache_creation_input_tokens": 9793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9793
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

_source line 36 · 2026-05-25T14:06:03.094Z_

```json
{
  "parentUuid": "55cecdc0-a1df-4545-b7a8-25478482f35a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fb29810c-06eb-43ef-9eaf-13fe22238e56",
  "timestamp": "2026-05-25T14:06:03.094Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：solver-trace-ablation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 14 warning 一致性…",
  "leafUuid": "fb29810c-06eb-43ef-9eaf-13fe22238e56",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 solver-trace-ablation paper audit",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Assistant

_source line 39 · 2026-05-25T14:06:08.002Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the tex files. Let me also check if there's a `discussion.tex` file and a `checklist.tex` file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb29810c-06eb-43ef-9eaf-13fe22238e56",
  "isSidechain": false,
  "requestId": "req_011CbPR3yfLP87E8BVfTKTvH",
  "type": "assistant",
  "uuid": "a4c401eb-32d8-486f-bc6f-1bf9bd9c44cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7wPgTnzkMJqoVuUcBQe2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24543,
      "cache_read_input_tokens": 62893,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 342,
          "cache_read_input_tokens": 62893,
          "cache_creation_input_tokens": 24543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24543
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

_source line 40 · 2026-05-25T14:06:08.368Z_

Now let me check for additional files and do some specific scans.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4c401eb-32d8-486f-bc6f-1bf9bd9c44cc",
  "isSidechain": false,
  "requestId": "req_011CbPR3yfLP87E8BVfTKTvH",
  "type": "assistant",
  "uuid": "8dcc3ec8-8892-427c-a992-ec5d1b8130f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7wPgTnzkMJqoVuUcBQe2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24543,
      "cache_read_input_tokens": 62893,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 342,
          "cache_read_input_tokens": 62893,
          "cache_creation_input_tokens": 24543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24543
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

_source line 41 · 2026-05-25T14:06:11.096Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MJT62oCvqJnxWFTEmaHstS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dcc3ec8-8892-427c-a992-ec5d1b8130f6",
  "isSidechain": false,
  "requestId": "req_011CbPR3yfLP87E8BVfTKTvH",
  "type": "assistant",
  "uuid": "f80fbd90-3479-46de-a10c-69daf3dddd43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7wPgTnzkMJqoVuUcBQe2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24543,
      "cache_read_input_tokens": 62893,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 342,
          "cache_read_input_tokens": 62893,
          "cache_creation_input_tokens": 24543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24543
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

_source line 42 · 2026-05-25T14:06:12.221Z_

<details><summary>↩ Tool result · `toolu_01SQAKGVjbw2WpkjtyqxWaV1`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:1:% Appendix — solver-trace-ablation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8691b6a4-c7d3-4a9c-ac4b-d36b748a516f",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "543e78ce-c854-426f-a099-a9072cd397c5",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:1:% Appendix — solver-trace-ablation",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "8691b6a4-c7d3-4a9c-ac4b-d36b748a516f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-25T14:06:11.109Z_

<details><summary>↩ Tool result · `toolu_01MJT62oCvqJnxWFTEmaHstS`</summary>

```text
1	%% DEPRECATED: Content transferred to conclusion.tex and appendix.tex (Extended Discussion section).
2	%% This file is NOT \input'd by main.tex.
3	%% Retained for reference only; do not re-include.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f80fbd90-3479-46de-a10c-69daf3dddd43",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "777a31ce-fc89-41df-a809-7a021efd72b8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/discussion.tex",
      "content": "%% DEPRECATED: Content transferred to conclusion.tex and appendix.tex (Extended Discussion section).\n%% This file is NOT \\input'd by main.tex.\n%% Retained for reference only; do not re-include.\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "f80fbd90-3479-46de-a10c-69daf3dddd43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T14:06:11.519Z_

<details open><summary>🔧 Tool call — Read · `toolu_013umZi9kDLnrEV45W7Y8oRj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "777a31ce-fc89-41df-a809-7a021efd72b8",
  "isSidechain": false,
  "requestId": "req_011CbPR3yfLP87E8BVfTKTvH",
  "type": "assistant",
  "uuid": "c9ab3972-4280-4479-9f9b-e3cf2c9f04bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7wPgTnzkMJqoVuUcBQe2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24543,
      "cache_read_input_tokens": 62893,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 342,
          "cache_read_input_tokens": 62893,
          "cache_creation_input_tokens": 24543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24543
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

_source line 45 · 2026-05-25T14:06:11.524Z_

<details><summary>↩ Tool result · `toolu_013umZi9kDLnrEV45W7Y8oRj`</summary>

```text
1	\section*{Responsible NLP Research Checklist}
2	
3	\paragraph{A. For every submission:}
4	
5	\begin{enumerate}[label=A\arabic*.,leftmargin=*]
6	\item \textbf{Did you describe the limitations of your work?}
7	Yes. Section~\ref{sec:limitations} discusses single model family and dataset, ISR's syntactic-only nature, limited seed counts, classifier coverage gaps, data scale, and temporal-snapshot caveats.
8	
9	\item \textbf{Did you discuss any potential risks of your work?}
10	Yes. Section~\ref{sec:discussion} discusses implications for AI safety, specifically that structural metrics designed to detect reward hacking may themselves become optimization targets (observe-vs-optimize asymmetry).
11	
12	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
13	Yes. Both summarize the three contributions (C1--C3) and key quantitative findings.
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
32	\item \textbf{Did you discuss the steps taken to check whether the data that you are using/creating contains any information that names or uniquely identifies individual people or offensive content?}
33	Not applicable. FOLIO contains logical reasoning problems without personal information or offensive content.
34	\end{enumerate}
35	
36	\paragraph{C. Did you run computational experiments?}
37	Yes.
38	
39	\begin{enumerate}[label=C\arabic*.,leftmargin=*]
40	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure used?}
41	Yes. The model size (4B) is reported in \S\ref{sec:task}. Training details (GRPO $K{=}4$, 500/1000 steps, seeds, batch sizes) are in \S\ref{sec:task} and Appendix~\ref{app:setup}. Computing infrastructure and total GPU hours are reported in Appendix~\ref{app:setup}.
42	
43	\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best model selection strategies?}
44	Yes. All hyperparameters are reported in \S\ref{sec:rewards} and Appendix~\ref{app:setup}. No hyperparameter search was performed; $\beta$ values were chosen for dose-response analysis.
45	
46	\item \textbf{Did you report descriptive statistics about your results (e.g., error bars, confidence intervals)?}
47	Yes. We report mean$\pm$std across seeds (Table~\ref{tab:goodhart-landscape}), per-seed ranges, bootstrap confidence intervals (Appendix Table~\ref{tab:bootstrap-ci}), and discuss statistical power limitations (\S\ref{sec:limitations}).
48	
49	\item \textbf{If you used existing packages (e.g., for pre-processing, models, or evaluation), did you report the implementation, model, and version numbers?}
50	Yes. We report Qwen3-4B model versions, Prover9, and SWI-Prolog. Training uses TRL 0.17.0, PyTorch 2.6.0, and Transformers 4.51.3; versions are listed in Appendix~\ref{app:setup}.
51	\end{enumerate}
52	
53	\paragraph{D. Did you use human annotators (e.g., crowdsourcing or research with human participants)?}
54	Minimal. Manual audit was conducted for classifier precision (50 random CE/TS samples verified; Appendix~\ref{app:hacking-modes}) and for PG false-negative correction (seed 42 only). No crowdsourced annotation was used.
55	
56	\paragraph{E. Did you use AI assistants (e.g., ChatGPT, Copilot, or Code Interpreter)?}
57	Yes. AI assistants were used for code development and manuscript preparation. All experimental designs, analyses, and scientific conclusions were verified by the authors.
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9ab3972-4280-4479-9f9b-e3cf2c9f04bc",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "452357f1-5904-48ef-960b-a5a64c2ef210",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex",
      "content": "\\section*{Responsible NLP Research Checklist}\n\n\\paragraph{A. For every submission:}\n\n\\begin{enumerate}[label=A\\arabic*.,leftmargin=*]\n\\item \\textbf{Did you describe the limitations of your work?}\nYes. Section~\\ref{sec:limitations} discusses single model family and dataset, ISR's syntactic-only nature, limited seed counts, classifier coverage gaps, data scale, and temporal-snapshot caveats.\n\n\\item \\textbf{Did you discuss any potential risks of your work?}\nYes. Section~\\ref{sec:discussion} discusses implications for AI safety, specifically that structural metrics designed to detect reward hacking may themselves become optimization targets (observe-vs-optimize asymmetry).\n\n\\item \\textbf{Do the abstract and introduction summarize the paper's main claims?}\nYes. Both summarize the three contributions (C1--C3) and key quantitative findings.\n\n\\item \\textbf{Have you used AI writing assistants when working on this paper?}\nYes. AI assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were verified by the authors.\n\\end{enumerate}\n\n\\paragraph{B. Did you use or create scientific artifacts?}\nYes.\n\n\\begin{enumerate}[label=B\\arabic*.,leftmargin=*]\n\\item \\textbf{Did you cite the creators of artifacts you used?}\nYes. We cite FOLIO~\\citep{folio}, Qwen3~\\citep{qwen3}, GRPO~\\citep{deepseekmath}, Prover9~\\citep{mccune-prover9}, and SWI-Prolog~\\citep{wielemaker2012swi}.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\nYes. Qwen3 is released under the Tongyi Qianwen License; FOLIO is released under CC BY-SA 4.0. Both permit research use.\n\n\\item \\textbf{Did you discuss if your use of existing artifact(s) was consistent with their intended use?}\nYes. FOLIO is used for its intended purpose (NLI evaluation); Qwen3 is used within its intended scope (language model fine-tuning).\n\n\\item \\textbf{Did you discuss the steps taken to check whether the data that you are using/creating contains any information that names or uniquely identifies individual people or offensive content?}\nNot applicable. FOLIO contains logical reasoning problems without personal information or offensive content.\n\\end{enumerate}\n\n\\paragraph{C. Did you run computational experiments?}\nYes.\n\n\\begin{enumerate}[label=C\\arabic*.,leftmargin=*]\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure used?}\nYes. The model size (4B) is reported in \\S\\ref{sec:task}. Training details (GRPO $K{=}4$, 500/1000 steps, seeds, batch sizes) are in \\S\\ref{sec:task} and Appendix~\\ref{app:setup}. Computing infrastructure and total GPU hours are reported in Appendix~\\ref{app:setup}.\n\n\\item \\textbf{Did you discuss the experimental setup, including hyperparameter search and best model selection strategies?}\nYes. All hyperparameters are reported in \\S\\ref{sec:rewards} and Appendix~\\ref{app:setup}. No hyperparameter search was performed; $\\beta$ values were chosen for dose-response analysis.\n\n\\item \\textbf{Did you report descriptive statistics about your results (e.g., error bars, confidence intervals)?}\nYes. We report mean$\\pm$std across seeds (Table~\\ref{tab:goodhart-landscape}), per-seed ranges, bootstrap confidence intervals (Appendix Table~\\ref{tab:bootstrap-ci}), and discuss statistical power limitations (\\S\\ref{sec:limitations}).\n\n\\item \\textbf{If you used existing packages (e.g., for pre-processing, models, or evaluation), did you report the implementation, model, and version numbers?}\nYes. We report Qwen3-4B model versions, Prover9, and SWI-Prolog. Training uses TRL 0.17.0, PyTorch 2.6.0, and Transformers 4.51.3; versions are listed in Appendix~\\ref{app:setup}.\n\\end{enumerate}\n\n\\paragraph{D. Did you use human annotators (e.g., crowdsourcing or research with human participants)?}\nMinimal. Manual audit was conducted for classifier precision (50 random CE/TS samples verified; Appendix~\\ref{app:hacking-modes}) and for PG false-negative correction (seed 42 only). No crowdsourced annotation was used.\n\n\\paragraph{E. Did you use AI assistants (e.g., ChatGPT, Copilot, or Code Interpreter)?}\nYes. AI assistants were used for code development and manuscript preparation. All experimental designs, analyses, and scientific conclusions were verified by the authors.\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  },
  "sourceToolAssistantUUID": "c9ab3972-4280-4479-9f9b-e3cf2c9f04bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T14:06:12.184Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SQAKGVjbw2WpkjtyqxWaV1`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "452357f1-5904-48ef-960b-a5a64c2ef210",
  "isSidechain": false,
  "requestId": "req_011CbPR3yfLP87E8BVfTKTvH",
  "type": "assistant",
  "uuid": "8691b6a4-c7d3-4a9c-ac4b-d36b748a516f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7wPgTnzkMJqoVuUcBQe2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24543,
      "cache_read_input_tokens": 62893,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 342,
          "cache_read_input_tokens": 62893,
          "cache_creation_input_tokens": 24543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24543
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

_source line 47 · 2026-05-25T14:06:16.125Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018Y7CqCKs1YLVQCpFrRogEF`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "543e78ce-c854-426f-a099-a9072cd397c5",
  "isSidechain": false,
  "requestId": "req_011CbPR4er2HyHkRzECJWNqD",
  "type": "assistant",
  "uuid": "7bfe5f92-5c0f-42ba-b7ed-de8b7f92287f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESjS9MrFB5zLaMymJ6cRev",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1886,
      "cache_read_input_tokens": 87436,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 413,
          "cache_read_input_tokens": 87436,
          "cache_creation_input_tokens": 1886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1886
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

_source line 48 · 2026-05-25T14:06:16.137Z_

<details><summary>↩ Tool result · `toolu_018Y7CqCKs1YLVQCpFrRogEF`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bfe5f92-5c0f-42ba-b7ed-de8b7f92287f",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "96efeac7-bb1b-44ba-bbc2-3edd9bcad68d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "7bfe5f92-5c0f-42ba-b7ed-de8b7f92287f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T14:06:17.657Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VA35qaLca5FRGCDPy8y8QP`</summary>

```json
{
  "pattern": "(it is worth noting|notably|importantly|furthermore|moreover|additionally)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "glob": "*.tex",
  "-i": true,
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96efeac7-bb1b-44ba-bbc2-3edd9bcad68d",
  "isSidechain": false,
  "requestId": "req_011CbPR4er2HyHkRzECJWNqD",
  "type": "assistant",
  "uuid": "ac741f4b-f150-433f-b4e6-891292dd339b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESjS9MrFB5zLaMymJ6cRev",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1886,
      "cache_read_input_tokens": 87436,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 413,
          "cache_read_input_tokens": 87436,
          "cache_creation_input_tokens": 1886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1886
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

_source line 50 · 2026-05-25T14:06:17.677Z_

<details><summary>↩ Tool result · `toolu_01VA35qaLca5FRGCDPy8y8QP`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:385:TSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac741f4b-f150-433f-b4e6-891292dd339b",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "387dbc5b-87de-4033-bdae-a604bde30b64",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:385:TSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "ac741f4b-f150-433f-b4e6-891292dd339b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T14:06:18.889Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01L8m5W4TivNv6ohTk2HVqnn`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "387dbc5b-87de-4033-bdae-a604bde30b64",
  "isSidechain": false,
  "requestId": "req_011CbPR4er2HyHkRzECJWNqD",
  "type": "assistant",
  "uuid": "f6f1d081-daf6-4789-abc1-545059bb4867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESjS9MrFB5zLaMymJ6cRev",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1886,
      "cache_read_input_tokens": 87436,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 413,
          "cache_read_input_tokens": 87436,
          "cache_creation_input_tokens": 1886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1886
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

_source line 52 · 2026-05-25T14:06:18.906Z_

<details><summary>↩ Tool result · `toolu_01L8m5W4TivNv6ohTk2HVqnn`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:4:\paragraph{Neurosymbolic reasoning.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:10:Specification gaming~\citep{krakovna2020specification} and Goodhart's Law~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} are established across RL from human feedback (RLHF)~\citep{gao-reward-overoptimization} and logical formalization~\citep{bondarenko-spec-gaming, kim-game-formalization}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:13:Concurrent work documents spurious signals in RLVR~\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking, helff2026gaming, nishimura2026specgaming, khalifa2026countdown} and proposes composite rewards as mitigations~\citep{tarek2025reward, pronesti2026beyond};
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:14:mitigation strategies include reward model ensembles~\citep{coste2023reward}, constrained optimization~\citep{moskovitz2023confronting}, and activation-level monitoring~\citep{wilhelm2026monitoring}. \citet{yue2025rl-reasoning} show RLVR redistributes probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:15:Our Goodhart effect follows the regressional pattern~\citep{manheim-goodhart-taxonomy} on FOLIO; its application to a diagnostic designed to detect gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:19:Process reward models~\citep{lightman-verify-step, setlur2025rewarding, cui2025prime, cobbe2021training, uesato2022solving} supervise intermediate steps; \citet{sullivan2025grpo-prm} show GRPO implicitly implements process reward. Classical reward shaping~\citep{ng1999policy, gao-effective-rl-reward} guarantees policy invariance only under potential-based transforms; ISR violates this condition.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:22:\paragraph{Mutation testing.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:22:With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:54:\paragraph{Multiplicative coupling.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:55:Three controls constrain the multiplicative confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\ref{app:setup}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:61:\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR systematically selects for TS over CE without reducing total hacking; SFT shows near-zero hacking.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:71:ISR reward produces bimodal outcomes (Figure~\ref{fig:seed-divergence}): 3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect can occur under standard training conditions (95\% Clopper--Pearson CI: [11.8\%, 88.1\%]; $n{=}5$); 2 of 5 retain substantial genuine reasoning (seeds~45/46 added post-hoc to test replication; Appendix~\ref{app:detailed-results}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:108:Replicating the pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}), exec-only seeds collapse to $\text{ISR}^*{\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:113:Converged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:127:The central pattern: \emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\%$ non-hacking.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:16:Yes. AI assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were verified by the authors.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:49:\item \textbf{If you used existing packages (e.g., for pre-processing, models, or evaluation), did you report the implementation, model, and version numbers?}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:11:Exec-only GRPO reaching $\text{PR}{=}93\%$ (\S\ref{sec:diagnostic}), nearly $3\times$ this ceiling, confirms the solver accepts formalizations for nominally unprovable examples, constituting direct evidence of structural gaming independent of ISR.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:100:The non-hacking rate is an upper bound on genuine reasoning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:61:FOL exec-only seed~43 was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:103:This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:109:Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:123:A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:192:In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-detailed}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:289:Low-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:318:We term this \textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:498:The component count grows unboundedly over training.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:544:95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:663:\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\S\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\text{f50}}{>}0.90$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:750:To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%, higher than SFT (13.0\%, 3-seed pooled) but still early in training.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:753:This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:878:    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:5:The root cause is evaluation by a single criterion, whether the generated formalization proves under a formal solver, which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:6:Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:31:(\textbf{C1})~a systematic empirical analysis of structural degeneration in GRPO-trained neurosymbolic reasoning, using LOO ablation (STA/ISR) to catalogue eight hacking modes across six reward conditions (\S\S\ref{sec:sta}--\ref{sec:crossdomain});
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6f1d081-daf6-4789-abc1-545059bb4867",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "673bfac0-664e-49a8-b1a7-b4f61645886b",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:4:\\paragraph{Neurosymbolic reasoning.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:10:Specification gaming~\\citep{krakovna2020specification} and Goodhart's Law~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} are established across RL from human feedback (RLHF)~\\citep{gao-reward-overoptimization} and logical formalization~\\citep{bondarenko-spec-gaming, kim-game-formalization}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:13:Concurrent work documents spurious signals in RLVR~\\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking, helff2026gaming, nishimura2026specgaming, khalifa2026countdown} and proposes composite rewards as mitigations~\\citep{tarek2025reward, pronesti2026beyond};\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:14:mitigation strategies include reward model ensembles~\\citep{coste2023reward}, constrained optimization~\\citep{moskovitz2023confronting}, and activation-level monitoring~\\citep{wilhelm2026monitoring}. \\citet{yue2025rl-reasoning} show RLVR redistributes probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:15:Our Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO; its application to a diagnostic designed to detect gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:19:Process reward models~\\citep{lightman-verify-step, setlur2025rewarding, cui2025prime, cobbe2021training, uesato2022solving} supervise intermediate steps; \\citet{sullivan2025grpo-prm} show GRPO implicitly implements process reward. Classical reward shaping~\\citep{ng1999policy, gao-effective-rl-reward} guarantees policy invariance only under potential-based transforms; ISR violates this condition.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:22:\\paragraph{Mutation testing.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:22:With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:54:\\paragraph{Multiplicative coupling.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:55:Three controls constrain the multiplicative confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:61:\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR systematically selects for TS over CE without reducing total hacking; SFT shows near-zero hacking.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:71:ISR reward produces bimodal outcomes (Figure~\\ref{fig:seed-divergence}): 3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect can occur under standard training conditions (95\\% Clopper--Pearson CI: [11.8\\%, 88.1\\%]; $n{=}5$); 2 of 5 retain substantial genuine reasoning (seeds~45/46 added post-hoc to test replication; Appendix~\\ref{app:detailed-results}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:108:Replicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:113:Converged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:127:The central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:16:Yes. AI assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were verified by the authors.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:49:\\item \\textbf{If you used existing packages (e.g., for pre-processing, models, or evaluation), did you report the implementation, model, and version numbers?}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:11:Exec-only GRPO reaching $\\text{PR}{=}93\\%$ (\\S\\ref{sec:diagnostic}), nearly $3\\times$ this ceiling, confirms the solver accepts formalizations for nominally unprovable examples, constituting direct evidence of structural gaming independent of ISR.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:100:The non-hacking rate is an upper bound on genuine reasoning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:61:FOL exec-only seed~43 was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:103:This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:109:Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:123:A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:192:In Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-detailed}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:289:Low-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:318:We term this \\textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:498:The component count grows unboundedly over training.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:544:95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:663:\\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\\S\\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\\text{f50}}{>}0.90$.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:750:To control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:753:This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:878:    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:5:The root cause is evaluation by a single criterion, whether the generated formalization proves under a formal solver, which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:6:Under reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:31:(\\textbf{C1})~a systematic empirical analysis of structural degeneration in GRPO-trained neurosymbolic reasoning, using LOO ablation (STA/ISR) to catalogue eight hacking modes across six reward conditions (\\S\\S\\ref{sec:sta}--\\ref{sec:crossdomain});",
    "numLines": 35
  },
  "sourceToolAssistantUUID": "f6f1d081-daf6-4789-abc1-545059bb4867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：solver-trace-ablation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 14 warning 一致性…",
  "leafUuid": "673bfac0-664e-49a8-b1a7-b4f61645886b",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 solver-trace-ablation paper audit",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Assistant

_source line 55 · 2026-05-25T14:08:53.268Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now count the words in the abstract to check if it's under 200 words (EMNLP 2026 rule).

Also let me check for the checklist inclusion in main.tex - the rule says ARR Responsible NLP Checklist is in the OpenReview submission form, not in the paper PDF. But I see there's a checklist.tex that appears to NOT be included in main.tex. Let me verify.


Looking at the main.tex file, I can see the document structure includes the abstract, introduction, related work, method, experiments, conclusion, and limitations sections, followed by the bibliography and appendix. The checklist.tex file isn't included in the main document, which is correct according to the submission guidelines. Now I need to count the words in the abstract to ensure it meets the 200-word limit.

The abstract discusses how neurosymbolic reasoning systems evaluate formalizations purely by execution success, which allows RL optimizers to exploit shortcuts like embedding conclusions in premises. I'm examining how leave-one-out ablation testing reveals that proof-rate improvements actually mask a shift toward degenerate hacking strategies, but this diagnostic method itself becomes gameable when used as a training reward, creating a paradox where models learn to satisfy the test rather than solve the underlying task.

Now I'm looking at empirical results showing this Goodhart effect manifests inconsistently across random seeds in smaller models—some converge to genuine reasoning while others exploit shortcuts—and this pattern holds across different logic systems and datasets, suggesting the boundary between observable structural integrity and optimizable proxies depends on specific training conditions. The methods section then details the STA and ISR definitions with their algorithms, followed by the six reward conditions and taxonomy of hacking modes used across experiments. The experiments validate each contribution: ISR as a diagnostic tool for structural degeneration, the seed-dependent Goodhart effects when ISR becomes the reward signal, cross-domain replication in Prolog and ProofFOL, and the hacking taxonomy itself. The design choices align perfectly with the introduction's identified gap—STA provides exactly the annotation-free ablation method needed to test component necessity. The conclusion ties this together by showing how STA reveals degeneration invisible to execution-based evaluation, how ISR reward produces predictable Goodhart effects, and how cross-logic results confirm the compositional nature of the problem.

The narrative holds together tightly. One small note: the abstract mentions "hacking modes" without specifying the count of eight, while the introduction's C1 claim explicitly states "eight hacking modes across six reward conditions"—but that's appropriate for the abstract level, which focuses on the conceptual story rather than specific numbers.

Checking the details more carefully, the abstract's claim about the observe-versus-optimize asymmetry persisting across logic types with Prolog replication aligns with the conclusion's statement about cross-logic experiments confirming the compositional mode shift. Similarly, the abstract's mention of cross-dataset evidence from ProofFOL suggesting boundary conditions matches the conclusion's characterization of that evidence as exploratory. The seed convergence numbers also check out: the abstract states "3 of 5 seeds converge to gaming" while the experiments section provides the full statistical detail with confidence intervals and notes that 2 of 5 retain genuine reasoning.

The conclusion is deliberately brief as a single paragraph since this paper combines Discussion and Conclusion into one section, which works fine for an 8-page format. Now I'm verifying the section structure itself. The abstract hits all the key elements—problem, method, results, and significance. The introduction builds logically from background on execution-only evaluation and existing shortcomings in neurosymbolic and inference-time approaches, then introduces the paper's diagnostic methods before laying out the three main contributions. The flow from identifying the gap to proposing STA and ISR as solutions, then demonstrating Goodhart vulnerability, feels coherent.

For Related Work, the thematic organization by topic—neurosymbolic reasoning, reward hacking and Goodhart's Law, process rewards, mutation testing—is cleaner than a chronological "A did X, B did Y" approach. Now I'm checking whether each contribution claim actually maps to the sections that support it. C1 about systematic empirical analysis of structural degeneration across 8 hacking modes and 6 reward conditions should span sections 3.2 through 4.5, covering the STA definition, conditions taxonomy, diagnostic results, cross-domain validation, and the full taxonomy. C2 about the seed-dependent Goodhart effect with matched controls points directly to section 4.3. C3 about cross-logic replication in FOL and Prolog appears to be cut off, but the pattern suggests it should map to whichever section demonstrates the replication across logical frameworks.

The title and abstract claim "across logic types" and "six reward conditions"—I need to verify these numbers actually hold. The experiments do cover FOL and Prolog, so that checks out. For the conditions, section 3.3 lists exec-only, ISR at two dose levels (β=0.1 and 0.3), matched random controls, and SFT, which gives six. But I'm noticing Table 1 also mentions a Shuffled-ISR variant, which would make seven conditions total. Let me look at what the paper actually claims in section 3.3 to see if it's really six or if there's a discrepancy here. SFT baseline."

That's: exec-only, ISR 0.1, ISR 0.3, Random 0.1, Random 0.3, SFT = 6 conditions.

But Table 1 also includes "Shuffled-ISR" as a 7th row. And in C1, the claim is "six reward conditions". The shuffled-ISR is actually mentioned in the Goodhart section §4.3 as a deconfounding control. So it might be considered a control rather than a primary condition. But it is in Table 1 as a distinct condition...

Actually, this is a minor discrepancy. The method says "six conditions" but Table 1 shows 7 rows. Looking more carefully at the actual definitions, the six main conditions are exec-only, ISR with β values of 0.1 and 0.3, matched random controls at those same β values, and supervised fine-tuning—while Shuffled-ISR was added as a deconfounding control and appears as a separate row in the table. I'm checking whether the paper's claims are properly supported by evidence. The abstract mentions "significantly" in relation to mode distribution differences, backed by a chi-squared test with p < 10^-38. The quantitative claims about seed convergence and the 87% verbatim conclusion embedding both match what's shown in the tables. Now I'm looking for any overclaimed language like "consistently" that might not be fully justified.

The paper actually does a good job with hedging language—using terms like "suggestive" and "exploratory" appropriately. The claim about ISR reward systematically selecting for tautological shortcuts is strong, but the chi-squared test and consistent pattern across three seeds support it. The main thesis about structural proxies being easier to detect than to optimize is well-grounded in the diagnostic versus reward results, showing the Goodhart effect in action.

For experimental rigor, the tables report mean and standard deviation across multiple seeds where applicable, and individual seed conditions are documented separately.  Recent baselines like GRPO and Qwen3 are included, and the ablation structure is comprehensive with multiple reward conditions and the hacking taxonomy. The Shuffled-ISR control is a smart deconfounding choice. The paper acknowledges the limitation of single-seed results by focusing on per-seed qualitative analysis as the primary framework.

Now looking at reproducibility—the hyperparameters are detailed in the appendix.

The hardware specs are clearly documented with RTL 4090 and RTX PRO 6000 GPUs, training times ranging from 1-2 GPU-hours for 500 steps up to 3-5 for 1000 steps, and total compute around 80-120 GPU-hours. Data preprocessing for ProofFOL is described and code is available via anonymous URL. The checklist exists in a separate file but correctly isn't included in the main PDF, which aligns with EMNLP's requirement that it be submitted through OpenReview instead.

Looking at the main.tex structure, the checklist isn't imported anywhere, which is right. The appendix does include an "Use of AI Assistants" section, and EMNLP 2026 doesn't prohibit that.

The limitations section concisely covers the key constraints: the work uses a single model with limited seeds and demonstrates existence rather than prevalence, and FOLIO has inherent limitations. I'm checking whether the current draft satisfies the user's explicit instruction that the limitations section should be short with around 3 points, rather than the audit template's general ≥150 word guideline. The draft covers three distinct limitations at 75 words, which aligns with what the user requested—brief and focused—so this should be flagged as acceptable rather than problematic.

Now I'm verifying that all key terminology is defined consistently throughout the document. ISR and its variant ISR* are properly introduced, along with STA, LOO, GRPO, and the other acronyms used in the methodology sections. Everything checks out.

However, I notice GRPO appears in the abstract without an explicit definition there—it's only expanded later in §3.1. The abstract uses "GRPO-trained formalizations" but doesn't spell out what GRPO stands for at that point, which could be a minor consistency issue worth noting. FOL is used throughout the paper without ever being defined, even though it's a standard abbreviation in logic communities for First-Order Logic. I should flag this as another acronym that needs expansion for clarity, especially since the abstract should be self-contained.

Looking at the section transitions, the flow from introduction through related work and methods into experiments feels natural, but the conclusion is surprisingly brief—just four sentences combined with a practical guidelines reference. Given the eight-page limit for EMNLP 2026, this compression might feel abrupt to reviewers expecting a more substantial discussion of implications.

Re-reading the conclusion, it actually does accomplish quite a bit: it highlights the core finding about structural degeneration, acknowledges the Goodhart effect when repurposing ISR as a reward signal, notes that structural proxies are easier to observe than optimize, and points toward concrete mitigations and open questions. The section successfully summarizes the main results while gesturing toward broader implications, though it could benefit from slightly more interpretation of what these findings mean for the field beyond just the immediate results.

Now I'm checking the writing style for AI-like patterns—looking at em-dashes, en-dashes, and filler words. The em-dash only appears in a comment, en-dashes don't show up at all, and the filler word search is picking up normal English word endings rather than actual problematic participial phrases, so the prose style checks out.

For internal information leakage, the registry comments in the table are LaTeX comments that won't render, and the data file reference like `train_500_seed42` in the hyperparameters table is just a standard naming convention—nothing sensitive exposed.

Now checking the EMNLP 2026 submission requirements: I need to verify the abstract is under 200 words, confirm the main text stays within the 8-page limit (the paper is currently 23 pages total, so I need to see how much is appendix and references), and make sure the limitations section is in the main text rather than relegated to the appendix. The limitations appear to be properly placed before the bibliography, which is correct.

I'm also verifying that the ARR Responsible NLP Checklist isn't included in the PDF itself—it should only be filled out in the OpenReview submission form. The checklist file exists but isn't being input into the main document, which is what we want. There's a separate "Use of AI Assistants" disclosure in the appendix, which is fine as a distinct section.

Let me count the abstract word count to confirm it meets the requirement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "673bfac0-664e-49a8-b1a7-b4f61645886b",
  "isSidechain": false,
  "requestId": "req_011CbPR59G51twhSwM4LKzYP",
  "type": "assistant",
  "uuid": "7ef96893-63ff-4381-81b0-96de12a2c1d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAQ8YiWHao1gmEXVkorLzS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3846,
      "cache_read_input_tokens": 89322,
      "output_tokens": 7063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3846,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7063,
          "cache_read_input_tokens": 89322,
          "cache_creation_input_tokens": 3846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3846
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

_source line 56 · 2026-05-25T14:08:53.269Z_

Let me count the abstract words and check page counts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ef96893-63ff-4381-81b0-96de12a2c1d6",
  "isSidechain": false,
  "requestId": "req_011CbPR59G51twhSwM4LKzYP",
  "type": "assistant",
  "uuid": "20f22546-7310-423b-a683-957ad0017b77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAQ8YiWHao1gmEXVkorLzS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3846,
      "cache_read_input_tokens": 89322,
      "output_tokens": 7063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3846,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7063,
          "cache_read_input_tokens": 89322,
          "cache_creation_input_tokens": 3846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3846
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

_source line 57 · 2026-05-25T14:08:54.361Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NmSHoj32dJAduCxt8VLTAq`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/{//g; s/}//g; s/~/ /g; s/\\\\//g; s/[%].*//g; s/\\$[^$]*\\$//g' | tr -s ' \\n' ' ' | wc -w",
  "description": "Count abstract words (approximate)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20f22546-7310-423b-a683-957ad0017b77",
  "isSidechain": false,
  "requestId": "req_011CbPR59G51twhSwM4LKzYP",
  "type": "assistant",
  "uuid": "312fcfc1-cff2-4890-8082-bd7273cb2162",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAQ8YiWHao1gmEXVkorLzS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3846,
      "cache_read_input_tokens": 89322,
      "output_tokens": 7063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3846,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7063,
          "cache_read_input_tokens": 89322,
          "cache_creation_input_tokens": 3846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3846
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

_source line 58 · 2026-05-25T14:08:56.439Z_

<details><summary>↩ Tool result · `toolu_014ABP2NDwuwVSPQcGivoTne`</summary>

```text
4:We apply leave-one-out ablation to GRPO-trained formalizations, \emph{Solver Trace Ablation} (STA), to test whether each component is necessary for proof success, and characterize structural degeneration under six reward conditions via the resulting \emph{Intensional Structural Reward} (ISR).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a2a3805-403a-439a-879b-736b20d9fbd5",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "c244e7c4-9e6b-4b75-8e45-1ee4a818a543",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "4:We apply leave-one-out ablation to GRPO-trained formalizations, \\emph{Solver Trace Ablation} (STA), to test whether each component is necessary for proof success, and characterize structural degeneration under six reward conditions via the resulting \\emph{Intensional Structural Reward} (ISR).",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "5a2a3805-403a-439a-879b-736b20d9fbd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-25T14:08:54.562Z_

<details><summary>↩ Tool result · `toolu_01NmSHoj32dJAduCxt8VLTAq`</summary>

```text
183
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "312fcfc1-cff2-4890-8082-bd7273cb2162",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "65d6463a-9c8a-4baf-ae5f-e242531ca3c1",
  "toolUseResult": {
    "stdout": "183",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "312fcfc1-cff2-4890-8082-bd7273cb2162",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-25T14:08:55.790Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AGW32W9smQeaCmmGeLoncX`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper && cat limitations.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/{//g; s/}//g; s/~/ /g; s/\\\\//g; s/[%].*//g; s/\\$[^$]*\\$//g' | tr -s ' \\n' ' ' | wc -w",
  "description": "Count limitations words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65d6463a-9c8a-4baf-ae5f-e242531ca3c1",
  "isSidechain": false,
  "requestId": "req_011CbPR59G51twhSwM4LKzYP",
  "type": "assistant",
  "uuid": "5dd2db66-0736-4ed9-9c2b-8141ffcb5d7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAQ8YiWHao1gmEXVkorLzS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3846,
      "cache_read_input_tokens": 89322,
      "output_tokens": 7063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3846,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7063,
          "cache_read_input_tokens": 89322,
          "cache_creation_input_tokens": 3846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3846
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

_source line 61 · 2026-05-25T14:08:55.877Z_

<details><summary>↩ Tool result · `toolu_01AGW32W9smQeaCmmGeLoncX`</summary>

```text
73
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dd2db66-0736-4ed9-9c2b-8141ffcb5d7e",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "6cc274fc-bb4e-40cc-9581-f6e4bbce51de",
  "toolUseResult": {
    "stdout": "73",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5dd2db66-0736-4ed9-9c2b-8141ffcb5d7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-25T14:08:56.428Z_

<details open><summary>🔧 Tool call — Grep · `toolu_014ABP2NDwuwVSPQcGivoTne`</summary>

```json
{
  "pattern": "GRPO",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cc274fc-bb4e-40cc-9581-f6e4bbce51de",
  "isSidechain": false,
  "requestId": "req_011CbPR59G51twhSwM4LKzYP",
  "type": "assistant",
  "uuid": "5a2a3805-403a-439a-879b-736b20d9fbd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAQ8YiWHao1gmEXVkorLzS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3846,
      "cache_read_input_tokens": 89322,
      "output_tokens": 7063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3846,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7063,
          "cache_read_input_tokens": 89322,
          "cache_creation_input_tokens": 3846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3846
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

_source line 63 · 2026-05-25T14:08:56.506Z_

```json
{
  "parentUuid": "c244e7c4-9e6b-4b75-8e45-1ee4a818a543",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e6301e00-974c-428f-8357-c9831d614373",
  "timestamp": "2026-05-25T14:08:56.506Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：solver-trace-ablation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 14 warning 一致性…",
  "leafUuid": "e6301e00-974c-428f-8357-c9831d614373",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 solver-trace-ablation paper audit",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Tool call

_source line 66 · 2026-05-25T14:09:10.648Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01USMjhxCKtZXGemPiz2c7BT`</summary>

```json
{
  "pattern": "FOL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6301e00-974c-428f-8357-c9831d614373",
  "isSidechain": false,
  "requestId": "req_011CbPRGmVxQSC6JGXZ9LcTP",
  "type": "assistant",
  "uuid": "577c19f0-7be8-4e56-92c4-6c5a0461f0ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9npgNZaQKsPHqaH89fhMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7416,
      "cache_read_input_tokens": 93168,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7416,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 93168,
          "cache_creation_input_tokens": 7416,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7416
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

_source line 67 · 2026-05-25T14:09:10.660Z_

<details><summary>↩ Tool result · `toolu_01USMjhxCKtZXGemPiz2c7BT`</summary>

```text
10:All experiments draw from FOLIO~\citep{folio}; the held-out evaluation set (100 examples) contains 34 True, 25 False, and 41 Unknown labels, with only True-labeled examples admitting valid proofs (theoretical PR ceiling ${\sim}34\%$).
26:What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "577c19f0-7be8-4e56-92c4-6c5a0461f0ad",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "72aebe92-5fc0-4abf-a192-73e26de9ed51",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "10:All experiments draw from FOLIO~\\citep{folio}; the held-out evaluation set (100 examples) contains 34 True, 25 False, and 41 Unknown labels, with only True-labeled examples admitting valid proofs (theoretical PR ceiling ${\\sim}34\\%$).\n26:What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.",
    "numLines": 2
  },
  "sourceToolAssistantUUID": "577c19f0-7be8-4e56-92c4-6c5a0461f0ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-25T14:09:11.688Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Hk6q4V5uRWZmEnC4Ybrx8R`</summary>

```json
{
  "pattern": "\\\\section",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72aebe92-5fc0-4abf-a192-73e26de9ed51",
  "isSidechain": false,
  "requestId": "req_011CbPRGmVxQSC6JGXZ9LcTP",
  "type": "assistant",
  "uuid": "9839420a-4796-4eb1-9d30-2c20972cccfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9npgNZaQKsPHqaH89fhMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7416,
      "cache_read_input_tokens": 93168,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7416,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 93168,
          "cache_creation_input_tokens": 7416,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7416
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

_source line 69 · 2026-05-25T14:09:11.701Z_

<details><summary>↩ Tool result · `toolu_01Hk6q4V5uRWZmEnC4Ybrx8R`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:1:\section{Related Work}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:1:\section{Experiments}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex:1:\section{Discussion and Conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:1:\section*{Responsible NLP Research Checklist}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:1:\section{Method}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex:1:\section{Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:3:\section{Experimental Setup}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:98:\section{Extended Discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:221:\section{Hacking Mode Definitions}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:547:\section{Per-Seed Detailed Results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:873:\section{Use of AI Assistants}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:1:\section{Introduction}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9839420a-4796-4eb1-9d30-2c20972cccfd",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "cbb0e51a-6b69-45f8-9151-d1e6d01227c2",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:1:\\section{Related Work}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:1:\\section{Experiments}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex:1:\\section{Discussion and Conclusion}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:1:\\section*{Responsible NLP Research Checklist}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:1:\\section{Method}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex:1:\\section{Limitations}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:3:\\section{Experimental Setup}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:98:\\section{Extended Discussion}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:221:\\section{Hacking Mode Definitions}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:547:\\section{Per-Seed Detailed Results}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:873:\\section{Use of AI Assistants}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:1:\\section{Introduction}",
    "numLines": 12
  },
  "sourceToolAssistantUUID": "9839420a-4796-4eb1-9d30-2c20972cccfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-25T14:09:38.314Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the main text page count. The Phase 1 report says 23 pages total. EMNLP 2026 allows 8 pages for main text + unlimited references + limitations doesn't count. Let me check how many pages of main text there are.

Let me look at the compiled PDF to check page count, or I can estimate from the structure:

Main text sections: Introduction, Related Work, Method, Experiments, Discussion and Conclusion = 5 sections
Then Limitations (doesn't count)
Then References (unlimited)
Then Appendix

For EMNLP with acl style, 8 pages is quite tight. 

Given the compilation passed in Phase 1 and there's a recent commit about trimming the conclusion and compressing related work to fix page overflow, it looks like the 8-page limit is being managed, even with all the tables and figures. I should also check if "FOL" is defined anywhere—it's used throughout but I haven't spotted "First-Order Logic" spelled out in the main text yet.

Looking at the reward conditions, there's a slight inconsistency: the abstract claims six conditions, but Method §3.3 lists six primary ones (exec-only, ISR low/high-dose at β∈{0.1,0.3}, matched random controls, and SFT baseline), while Table 1 actually includes a seventh condition (Shuffled-ISR) in the main results. So the paper defines six conditions but presents seven in the actual results table. The abstract and introduction both reference six reward conditions, which aligns with the Method section's definition of exactly six conditions. However, shuffled-ISR appears in Table 1 and gets discussed in the Goodhart section, so a reader might count seven conditions total—worth flagging as a potential source of confusion. I'm also noticing that FOL never gets expanded to "First-Order Logic" anywhere in the paper, despite being used in the methods section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbb0e51a-6b69-45f8-9151-d1e6d01227c2",
  "isSidechain": false,
  "requestId": "req_011CbPRHtjKCneaiSdoTxGQn",
  "type": "assistant",
  "uuid": "c7f73ad9-4be2-4ec0-aa23-f24aa3a16fa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V94aHDyJdqdHEUvmxxSemz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 100584,
      "output_tokens": 1387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1387,
          "cache_read_input_tokens": 100584,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1025
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

_source line 71 · 2026-05-25T14:09:38.471Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011RpegHvv1sNkK5gHaMF4fA`</summary>

```json
{
  "pattern": "First.Order Logic|first.order logic",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7f73ad9-4be2-4ec0-aa23-f24aa3a16fa5",
  "isSidechain": false,
  "requestId": "req_011CbPRHtjKCneaiSdoTxGQn",
  "type": "assistant",
  "uuid": "a76e2476-150f-4f09-9809-3a942b3327ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V94aHDyJdqdHEUvmxxSemz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 100584,
      "output_tokens": 1387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1387,
          "cache_read_input_tokens": 100584,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1025
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

_source line 72 · 2026-05-25T14:09:38.493Z_

<details><summary>↩ Tool result · `toolu_011RpegHvv1sNkK5gHaMF4fA`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a76e2476-150f-4f09-9809-3a942b3327ec",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "e061d7b6-7cfb-4f82-8da1-4919d358ec57",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "a76e2476-150f-4f09-9809-3a942b3327ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-25T14:09:39.935Z_

<details><summary>↩ Tool result · `toolu_01AqCivnpR5LebBB1TnTWfuf`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:68:A seed-stratified $\chi^2$ test confirms the overall mode distribution differs significantly between ISR and random conditions ($\chi^2{=}174.8$, $\text{df}{=}2$, $p{<}10^{-38}$; Appendix~\ref{app:statistical-details}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d51801f9-fdcd-44e0-8318-21926c9ec16c",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "348cabeb-51b5-46cc-b91c-6eb4ab556414",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:68:A seed-stratified $\\chi^2$ test confirms the overall mode distribution differs significantly between ISR and random conditions ($\\chi^2{=}174.8$, $\\text{df}{=}2$, $p{<}10^{-38}$; Appendix~\\ref{app:statistical-details}).",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "d51801f9-fdcd-44e0-8318-21926c9ec16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-25T14:09:39.080Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LcgQG7dzq75NFkK74LE58d`</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "glob": "*.tex",
  "-i": true,
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e061d7b6-7cfb-4f82-8da1-4919d358ec57",
  "isSidechain": false,
  "requestId": "req_011CbPRHtjKCneaiSdoTxGQn",
  "type": "assistant",
  "uuid": "0f7d2811-2a51-425f-9e8f-bb753eee1f45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V94aHDyJdqdHEUvmxxSemz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 100584,
      "output_tokens": 1387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1387,
          "cache_read_input_tokens": 100584,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1025
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

_source line 75 · 2026-05-25T14:09:39.096Z_

<details><summary>↩ Tool result · `toolu_01LcgQG7dzq75NFkK74LE58d`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f7d2811-2a51-425f-9e8f-bb753eee1f45",
  "isSidechain": false,
  "promptId": "a47a82f9-a79a-4ad0-8279-3f9b1e73c31e",
  "type": "user",
  "uuid": "064e7f21-2f5a-450b-a5f0-1649b05de207",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "0f7d2811-2a51-425f-9e8f-bb753eee1f45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-25T14:09:39.923Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AqCivnpR5LebBB1TnTWfuf`</summary>

```json
{
  "pattern": "significantly",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "064e7f21-2f5a-450b-a5f0-1649b05de207",
  "isSidechain": false,
  "requestId": "req_011CbPRHtjKCneaiSdoTxGQn",
  "type": "assistant",
  "uuid": "d51801f9-fdcd-44e0-8318-21926c9ec16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V94aHDyJdqdHEUvmxxSemz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 100584,
      "output_tokens": 1387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1387,
          "cache_read_input_tokens": 100584,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1025
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

_source line 77 · 2026-05-25T14:09:58.558Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now check for the "observe-vs-optimize" term consistency - is it used the same way throughout?

Also, I want to check if the Conclusion section is too short or if it repeats results numbers vs providing higher-level interpretation.

Let me also verify a few key numbers:
- Abstract claims "3 of 5 seeds converge to gaming" - Table in appendix shows ISR β=0.1 seeds 42/43/44 converge to gaming (N-H ≤ 17%), seeds 45/46 retain reasoning (54.8% and 54.5%). That's 3/5 gaming. ✓


- Abstract "six reward conditions" - 6 primary conditions defined in Method. ✓

Now checking the contribution claims against the paper: the hacking taxonomy identifies eight distinct modes including CE, TS, PG, and various collapse patterns. ✓ The six reward conditions are confirmed in the methods section. ✓ And the cross-logic replication work with FOL and Prolog is covered in section 4.4. ✓

Compiling my final audit findings now. I've identified a few issues worth flagging: FOL is never expanded to First-Order Logic anywhere, GRPO lacks a definition in the abstract despite being used there, and there's a discrepancy where Table 1 appears to show seven or more conditions while the text claims six—this could confuse readers. The conclusion also feels quite compressed at just four sentences, which might strike reviewers as rushed. On the positive side, the abstract stays within the 200-word limit, the limitations section at 73 words is acceptable per the guidelines, and the paper's use of "significantly" appears properly qualified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "348cabeb-51b5-46cc-b91c-6eb4ab556414",
  "isSidechain": false,
  "requestId": "req_011CbPRKy2afxk2C6BpxJTQK",
  "type": "assistant",
  "uuid": "aad62c48-2bc4-44b1-ac37-d253d8a0391f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CT9684mas8AFBDUmsZTwCt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1590,
      "cache_read_input_tokens": 101609,
      "output_tokens": 1990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1990,
          "cache_read_input_tokens": 101609,
          "cache_creation_input_tokens": 1590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1590
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

_source line 78 · 2026-05-25T14:10:32.503Z_

All files read. Now I have complete context to produce the audit.

```
[CONTENT_AUDIT_START]
- [warning] [符号一致性] FOL (First-Order Logic) 全文从未展开定义。Introduction、Method、Experiments 中多处使用 "FOL" 但无首次出现时的完整形式。审稿人可能认为缺乏定义。
- [warning] [符号一致性] abstract.tex:4 GRPO 在摘要中使用 ("GRPO-trained formalizations") 但未展开为 "Group Relative Policy Optimization"。写作规范要求 Abstract 内缩写自包含。
- [warning] [贡献-范围对齐] method.tex:65 + experiments.tex Table 1: Method 声称 "six conditions" 但 Table 1 主结果含 Shuffled-ISR 第 7 行（另有 ISR 5-seed 重复行），读者数条目时会困惑。建议在 Method 或 Table caption 中显式说明 Shuffled-ISR 是额外 deconfounding control。
- [warning] [章节结构] conclusion.tex: Discussion and Conclusion 仅 4 句话（~70 words）。虽满足 8-page 约束，但过度压缩可能让审稿人认为缺乏高层解读。建议补充 1-2 句关于 broader implications 或 community takeaway。
- [info] [写作规则] abstract.tex: ~183 words，在 200-word 限制内 ✓
- [info] [写作规则] limitations.tex: 73 words / 3 points。符合用户自定义规则（"一小段，覆盖3个点"），但在该维度的通用标准（≥150 words）下偏短。若审稿人 expecting more substance，可考虑每点加一句解释。
- [info] [叙事一致性] 叙事主线高度一致。Abstract/Intro 的 "problem"（execution-only evaluation → shortcuts）→ Method 的 "solution"（STA/ISR）→ Experiments 的 "验证"（C1 degeneration + C2 Goodhart + C3 cross-domain）→ Conclusion 的总结 均指向同一主线 "observe vs optimize asymmetry"。未检测到叙事漂移。
- [info] [Claim 强度] experiments.tex:68 唯一使用 "significantly" 处有 χ²=174.8, p<10⁻³⁸ 支撑 ✓。其余 claim 均使用恰当 hedging（"exploratory", "suggestive", "consistent with"）。
- [info] [去AI] 正文无 em-dash（仅 appendix.tex 第 1 行 LaTeX 注释中有一个，不渲染）。无 en-dash。无 filler words（notably/importantly/furthermore）。无 -ing 分词短语结尾。无 AI 黑名单用词（delve/leverage/utilize/myriad/plethora）。写作风格干净。
- [info] [实验严谨性] 多 seed 结果报告 mean±std ✓; 统计检验完整（Fisher, χ², CMH, Clopper-Pearson CI, Bonferroni correction）✓; SFT baseline + Random control 设计合理 ✓; Shuffled-ISR deconfounding 控制 ✓。
- [info] [可复现性] Hyperparameters table ✓; GPU型号+时间 ✓; 代码匿名链接 ✓; 数据集构建流程 ✓。
- [info] [内部信息残留] appendix.tex Table hyperparams "Data file: train\_500\_seed42" 暴露内部文件名，但不影响匿名性且有助复现，可保留。
- [info] [审稿规则] checklist.tex 未 \input 进 main.tex ✓（符合 EMNLP 2026 规则：checklist 在 OpenReview form 中填写，不在 PDF 里）。
- [info] [审稿规则] Limitations 在正文中 (\input{limitations} before \bibliography) ✓; appendix 中无重复 limitations section ✓。
- [info] [Related Work 结构] 采用 4 个 \paragraph 主题分组（Neurosymbolic reasoning / Reward hacking / Process rewards / Mutation testing），非堆砌式，符合规范 ✓。
[CONTENT_AUDIT_END]
```

**审计总结**: 叙事一致性良好，无 critical 级问题。4 个 warning 均为可快速修复的格式/术语问题（FOL/GRPO 缩写展开、条件计数措辞、Conclusion 篇幅）。去 AI 风格检查通过，claim 强度匹配，实验设计严谨。

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aad62c48-2bc4-44b1-ac37-d253d8a0391f",
  "isSidechain": false,
  "requestId": "req_011CbPRKy2afxk2C6BpxJTQK",
  "type": "assistant",
  "uuid": "bf8bf9fb-3a8a-48e1-a4e9-1f69c94f69e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/paper_audit_content_b1866d9f",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CT9684mas8AFBDUmsZTwCt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1590,
      "cache_read_input_tokens": 101609,
      "output_tokens": 1990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1990,
          "cache_read_input_tokens": 101609,
          "cache_creation_input_tokens": 1590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1590
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
  "lastPrompt": "项目：solver-trace-ablation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 14 warning 一致性…",
  "leafUuid": "bf8bf9fb-3a8a-48e1-a4e9-1f69c94f69e8",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Runtime record

_source line 80_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 solver-trace-ablation paper audit",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：solver-trace-ablation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 14 warning 一致性…",
  "leafUuid": "bf8bf9fb-3a8a-48e1-a4e9-1f69c94f69e8",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---

### Runtime record

_source line 82_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 solver-trace-ablation paper audit",
  "sessionId": "8e614e8b-1c20-42be-96fe-59a15bdd0ca9"
}
```

---
