# Research conversation: In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating, find the paper's LaTeX

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8d70e420d0ceeaee.jsonl`
- **Structured JSON:** [`d1ba97997d84141dc723.json`](../../sessions/d1/d1ba97997d84141dc723.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-23T21:39:46.239Z_

In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating, find the paper's LaTeX source and extract:
1. The exact "first" claim about scheduled sampling and attention objectives (likely in intro or contributions section)
2. The method section describing how scheduled sampling is applied to the attention objective
3. Any related work discussion about scheduled sampling

Search in files matching *.tex in the project directory. Report the exact text and file:line locations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "9d774c3e-9df7-4c3c-b1cf-a32887fe4a33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T21:39:46.242Z_

```json
{
  "parentUuid": "9d774c3e-9df7-4c3c-b1cf-a32887fe4a33",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "8166caec-55b7-43a5-85df-b4b6bf2334cc",
  "timestamp": "2026-05-23T21:39:46.242Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-23T21:39:52.196Z_



Let me search for the relevant content in the LaTeX files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8166caec-55b7-43a5-85df-b4b6bf2334cc",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE2t2vusWr7UihnVJSV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2464e764-3899-4017-9160-de5bacef75a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017e1J17FDzbB3mYXzTuUvMV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16260,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16260,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T21:39:53.222Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0197pwmt4GabEsgg1HcABqot`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2464e764-3899-4017-9160-de5bacef75a9",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE2t2vusWr7UihnVJSV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b533fae3-08dc-4cdf-bc22-5a261e0a816a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017e1J17FDzbB3mYXzTuUvMV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16260,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16260,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T21:39:53.247Z_

<details><summary>↩ Tool result · `toolu_0197pwmt4GabEsgg1HcABqot`</summary>

```text
artifacts/dream_reports/dream_20260519T135115/best/paper.tex
artifacts/dream_reports/dream_20260519T135115/median/paper.tex
artifacts/dream_reports/dream_20260519T135115/worst/paper.tex
artifacts/dream_reports/dream_20260519T143220/best/paper.tex
artifacts/dream_reports/dream_20260519T143220/median/paper.tex
artifacts/dream_reports/dream_20260519T145320/best/paper.tex
artifacts/dream_reports/dream_20260519T145320/median/paper.tex
artifacts/dream_reports/dream_20260519T145320/worst/paper.tex
docs/paper/background.tex
artifacts/_project/paper/analysis.tex
docs/paper/related_work.tex
docs/paper/experiments.tex
docs/paper/method.tex
docs/paper/introduction.tex
docs/paper/analysis.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/abstract.tex
artifacts/_project/paper/table_steering_full.tex
artifacts/table_steering_full.tex
paper/main.tex
paper/sections/method.tex
paper/sections/related_work.tex
paper/sections/discussion.tex
paper/sections/limitations.tex
paper/sections/analysis.tex
paper/sections/experiments.tex
paper/sections/abstract.tex
paper/sections/conclusion.tex
paper/sections/introduction.tex
paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b533fae3-08dc-4cdf-bc22-5a261e0a816a",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "1220bd0f-ac92-47d3-bad3-8ebdd066cc49",
  "sourceToolAssistantUUID": "b533fae3-08dc-4cdf-bc22-5a261e0a816a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T21:39:54.606Z_

<details open><summary>🔧 Tool call — Grep · `toolu_012V1r5kwVvxhbWmu7nFfzxJ`</summary>

```json
{
  "pattern": "scheduled sampling",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true,
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1220bd0f-ac92-47d3-bad3-8ebdd066cc49",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE2t2vusWr7UihnVJSV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdeb0ce2-e4ac-48ea-ac24-1b4339a6d8f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017e1J17FDzbB3mYXzTuUvMV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16260,
      "cache_read_input_tokens": 0,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16260
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 286,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16260,
            "ephemeral_1h_input_tokens": 0
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

_source line 7 · 2026-05-23T21:39:54.643Z_

<details><summary>↩ Tool result · `toolu_012V1r5kwVvxhbWmu7nFfzxJ`</summary>

```text
&lt;persisted-output>
Output too large (39.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc/tool-results/toolu_012V1r5kwVvxhbWmu7nFfzxJ.txt

Preview (first 2KB):
paper/sections/related_work.tex-16-GradNorm \citep{chen2018gradnorm}, PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}, and Nash-MTL \citep{navon2022nash} treat gradient conflict as a root cause. We repurpose PCGrad as a diagnostic: eliminating NTP-GAR directional conflict does not improve GAR convergence---gradient conflict is a symptom, not the cause.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex-17-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex-18-\paragraph{Exposure bias.}
paper/sections/related_work.tex:19:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-7-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-8-\subsection{Main Results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-9-
paper/sections/experiments.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-11-
paper/sections/experiments.tex-12-Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}a). The ordering---ThreadGate (0.064) $>$ LoRA-only (0.037) $>$ Uniform Gate (0.033) $>$ PCGrad (0.030) $>$ Base (0.019)---shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendix~\ref{sec:appendix-stats}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). We analyze this distribution shift in \S\ref{sec:analysis}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-13-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-53-
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdeb0ce2-e4ac-48ea-ac24-1b4339a6d8f3",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "cd006852-24f5-4170-b026-6a5b99808723",
  "sourceToolAssistantUUID": "fdeb0ce2-e4ac-48ea-ac24-1b4339a6d8f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-23T21:39:57.813Z_

Let me read the full grep output and the key files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd006852-24f5-4170-b026-6a5b99808723",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE3W8q9M6KXMdNaRcgA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dcdc606-ed57-4b05-b5e7-b4e6565e2618",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnPHwnGkxmZ1sWGitLfmqZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2407,
      "cache_read_input_tokens": 16260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2407,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T21:40:01.764Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YESqge26fJUHdD9MPRUT7T`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc/tool-results/toolu_012V1r5kwVvxhbWmu7nFfzxJ.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dcdc606-ed57-4b05-b5e7-b4e6565e2618",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE3W8q9M6KXMdNaRcgA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "422d0da6-9227-4331-bd9d-ec1a29e03020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnPHwnGkxmZ1sWGitLfmqZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2407,
      "cache_read_input_tokens": 16260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2407,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T21:40:02.022Z_

<details><summary>↩ Tool result · `toolu_01YESqge26fJUHdD9MPRUT7T`</summary>

```text
1	paper/sections/related_work.tex-16-GradNorm \citep{chen2018gradnorm}, PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}, and Nash-MTL \citep{navon2022nash} treat gradient conflict as a root cause. We repurpose PCGrad as a diagnostic: eliminating NTP-GAR directional conflict does not improve GAR convergence---gradient conflict is a symptom, not the cause.
2	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex-17-
3	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex-18-\paragraph{Exposure bias.}
4	paper/sections/related_work.tex:19:[Omitted long matching line]
5	--
6	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-7-
7	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-8-\subsection{Main Results}
8	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-9-
9	paper/sections/experiments.tex:10:[Omitted long matching line]
10	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-11-
11	paper/sections/experiments.tex-12-Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}a). The ordering---ThreadGate (0.064) $>$ LoRA-only (0.037) $>$ Uniform Gate (0.033) $>$ PCGrad (0.030) $>$ Base (0.019)---shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendix~\ref{sec:appendix-stats}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). We analyze this distribution shift in \S\ref{sec:analysis}.
12	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-13-
13	--
14	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-53-
15	paper/sections/experiments.tex-54-This closes the causal loop: if the collapse were due to representation drift in hidden states, no amount of attention reweighting could recover GAR. The recovery confirms attention misallocation---not representation degradation---as the proximal cause.
16	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-55-
17	paper/sections/experiments.tex:56:\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}
18	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-57-
19	paper/sections/experiments.tex:58:If exposure bias is the root cause (\S\ref{subsec:dist-shift}), reducing the training-inference distribution mismatch should narrow the gap. Scheduled sampling \citep{bengio2015scheduled}---mixing model-generated tokens into training prefixes with linearly increasing probability---directly targets this mismatch.
20	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-59-
21	paper/sections/experiments.tex-60-AR GAR-ours rises from 0.064 to 0.347 (seed 42; gap 7.8$\times$$\to$1.44$\times$) and 0.423 (seed 123; gap 1.18$\times$), yielding a two-seed mean of 0.385 (gap 1.30$\times$) with no PPL cost (1.44 vs.\ 1.43). GAR-Dongre also rises (0.019$\to$0.353; $N$\,=\,5 pilot)---the only intervention that moves both attention metrics. The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
22	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-61-
23	--
24	paper/sections/conclusion.tex-1-\section{Conclusion}\label{sec:conclusion}
25	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex-2-
26	paper/sections/conclusion.tex:3:[Omitted long matching line]
27	--
28	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex-1-\begin{abstract}
29	paper/sections/abstract.tex:2:[Omitted long matching line]
30	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex-3-\end{abstract}
31	--
32	paper/sections/appendix.tex-1-\section{Training Configuration}\label{sec:appendix-hyper}
33	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-2-
34	paper/sections/appendix.tex:3:[Omitted long matching line]
35	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-4-
36	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-5-\begin{table}[h]
37	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-6-\centering\small
38	--
39	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-272-
40	paper/sections/appendix.tex-273-\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
41	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-274-
42	paper/sections/appendix.tex:275:\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
43	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-276-
44	paper/sections/appendix.tex:277:Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
45	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-278-
46	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-279-\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
47	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-280-
48	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-281-\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
49	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-282-
50	paper/sections/appendix.tex:283:[Omitted long matching line]
51	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-284-
52	paper/sections/appendix.tex-285-\section{Computational Cost Analysis}\label{sec:appendix-cost}
53	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-286-
54	--
55	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-310-
56	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-311-\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
57	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-312-
58	paper/sections/appendix.tex:313:\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
59	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-314-
60	paper/sections/appendix.tex-315-\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
61	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-316-
62	--
63	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-370-
64	paper/sections/appendix.tex-371-\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
65	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-372-
66	paper/sections/appendix.tex:373:[Omitted long matching line]
67	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-374-
68	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-375-\begin{figure*}[h]
69	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-376-\centering
70	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-377-\includegraphics[width=0.95\textwidth]{fig_eb_scaling.pdf}
71	paper/sections/appendix.tex:378:\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
72	paper/sections/appendix.tex-379-\label{fig:eb-scaling}
73	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-380-\end{figure*}
74	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-381-
75	--
76	paper/sections/introduction.tex-13-  \label{fig:headline}
77	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex-14-\end{figure*}
78	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex-15-
79	paper/sections/introduction.tex:16:[Omitted long matching line]
80	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex-17-
81	paper/sections/introduction.tex:18:[Omitted long matching line]
82	--
83	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-507-Incorporating GAR monitoring into the decoding process (e.g., re-attending to goal tokens when GAR drops below a threshold) could provide dynamic correction without requiring training-time optimization.
84	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-508-
85	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-509-\textbf{Exposure bias mitigation for auxiliary losses.}
86	artifacts/dream_reports/dream_20260519T143220/best/paper.tex:510:Techniques such as scheduled sampling \citep{bengio2015scheduled} or sequence-level training \citep{ranzato2016sequence} could be adapted to reduce the distributional gap for auxiliary attention objectives.
87	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-511-
88	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-512-% ============================================================
89	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-513-% 8. CONCLUSION
90	--
91	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-528-Our study has several limitations.
92	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-529-First, we evaluate on two model architectures (Qwen-2.5-7B and Llama-3.1-8B) at the 7--8B scale; behavior at larger scales remains an open question, though the structural nature of the distribution shift argument suggests it will persist.
93	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-530-Second, our downstream evaluation is limited to a simple instruction retention task; more comprehensive behavioral benchmarks would strengthen the practical relevance of the GAR metric.
94	artifacts/dream_reports/dream_20260519T143220/best/paper.tex:531:Third, we do not experiment with exposure bias mitigation techniques (e.g., scheduled sampling applied to the auxiliary loss), which could partially bridge the training-inference gap.
95	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-532-Finally, our training data (UltraChat) represents a single conversation domain; verification across diverse dialogue datasets would further strengthen generalizability claims.
96	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-533-
97	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-534-% ============================================================
98	--
99	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-540-
100	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-541-\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}
101	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-542-Samy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam Shazeer.
102	artifacts/dream_reports/dream_20260519T143220/best/paper.tex:543:\newblock Scheduled sampling for sequence prediction with recurrent neural networks.
103	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-544-\newblock In \emph{Advances in Neural Information Processing Systems}, 2015.
104	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-545-
105	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex-546-\bibitem[Chen et~al.(2018)]{chen2018gradnorm}
106	--
107	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-425-First, inference-time attention intervention (e.g., directly modifying attention weights during generation) would bypass the training-generalization problem entirely.
108	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-426-Second, decoupled goal-processing pathways that maintain a separate representation of goal tokens, independent of the conversation context, could be more robust to distributional shift.
109	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-427-Third, GAR-aware decoding strategies that monitor and correct attention during generation offer a training-free alternative.
110	artifacts/dream_reports/dream_20260519T143220/median/paper.tex:428:Fourth, exposure bias mitigation techniques (scheduled sampling, sequence-level training) could be adapted to reduce the distribution mismatch for auxiliary attention objectives.
111	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-429-
112	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-430-
113	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-431-% ============================================================
114	--
115	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-455-
116	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-456-\bibitem[Bengio et al., 2015]{bengio2015}
117	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-457-Bengio, S., Vinyals, O., Jaitly, N., and Shazeer, N. (2015).
118	artifacts/dream_reports/dream_20260519T143220/median/paper.tex:458:\newblock Scheduled sampling for sequence prediction with recurrent neural networks.
119	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-459-\newblock In \emph{Advances in Neural Information Processing Systems (NeurIPS)}.
120	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-460-
121	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex-461-\bibitem[Dongre et al., 2026]{dongre2026}
122	--
123	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-89-
124	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-90-\paragraph{Exposure bias and teacher-forcing mismatch.}
125	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-91-The discrepancy between teacher-forced training and autoregressive inference is well studied~\cite{ranzato2016sequence,bengio2015scheduled}.
126	artifacts/dream_reports/dream_20260519T135115/best/paper.tex:92:Scheduled sampling~\cite{bengio2015scheduled} and sequence-level training~\cite{ranzato2016sequence} address generation quality degradation.
127	artifacts/dream_reports/dream_20260519T135115/best/paper.tex-93-Our work reveals a new consequence of this mismatch: auxiliary attention losses optimized under teacher-forcing fail to generalize, which existing exposure bias literature has not analyzed.
128	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-94-
129	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-95-% ============================================================
130	--
131	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-565-
132	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-566-    \item \textbf{Inference-time intervention may be necessary.} Methods that operate at inference time---such as activation patching, inference-time intervention~\cite{li2024inference}, or attention-guided decoding---bypass the training--inference distribution mismatch entirely, as they modify the actual inference computation rather than hoping that training-time patterns generalize.
133	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-567-
134	artifacts/dream_reports/dream_20260519T135115/best/paper.tex:568:    \item \textbf{Exposure bias mitigation could help.} Techniques developed for the standard exposure bias problem---scheduled sampling~\cite{bengio2015scheduled}, sequence-level training~\cite{ranzato2016sequence}---could potentially be adapted to auxiliary attention losses, training the model under its own generated context rather than gold context.
135	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-569-\end{enumerate}
136	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-570-
137	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-571-\subsection{Limitations}
138	--
139	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-646-
140	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-647-\bibitem{bengio2015scheduled}
141	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-648-Bengio, S., Vinyals, O., Jaitly, N., and Shazeer, N.
142	artifacts/dream_reports/dream_20260519T135115/best/paper.tex:649:\newblock Scheduled sampling for sequence prediction with recurrent neural networks.
143	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-650-\newblock In \emph{Proceedings of NeurIPS}, 2015.
144	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-651-
145	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex-652-\end{thebibliography}
146	--
147	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-341-
148	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-342-\subsection{Future Directions}
149	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-343-
150	artifacts/dream_reports/dream_20260519T135115/worst/paper.tex:344:[Omitted long matching line]
151	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-345-
152	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-346-% =========================================================================
153	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-347-\section{Conclusion}
154	--
155	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-381-
156	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-382-\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}
157	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-383-Bengio, S., Vinyals, O., Jaitly, N., and Shazeer, N. (2015).
158	artifacts/dream_reports/dream_20260519T135115/worst/paper.tex:384:\newblock Scheduled sampling for sequence prediction with recurrent neural networks.
159	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-385-\newblock \emph{Proceedings of NeurIPS 2015}.
160	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-386-
161	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex-387-\bibitem[Shazeer et~al.(2017)]{shazeer2017moe}
162	--
163	artifacts/dream_reports/dream_20260519T135115/median/paper.tex-330-(1) \emph{Inference-time attention intervention}: directly modifying attention weights during generation bypasses the training-generalization barrier entirely;
164	artifacts/dream_reports/dream_20260519T135115/median/paper.tex-331-(2) \emph{Decoupled goal-processing pathways}: architectures that maintain a separate channel for goal information, not mediated through the standard attention mechanism;
165	artifacts/dream_reports/dream_20260519T135115/median/paper.tex-332-(3) \emph{GAR-aware decoding}: modifying the decoding process to account for goal attention rather than training the model to internalize it;
166	artifacts/dream_reports/dream_20260519T135115/median/paper.tex:333:(4) \emph{Exposure bias mitigation}: techniques such as scheduled sampling \cite{bengio2015scheduled} or sequence-level training \cite{ranzato2016sequence} applied specifically to auxiliary attention losses.
167	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.tex-334-
168	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.tex-335-\section{Conclusion}
169	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.tex-336-
170	--
171	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/related_work.tex-13-[Omitted long context line]
172	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/related_work.tex-14-
173	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/related_work.tex-15-\paragraph{Exposure bias.}
174	docs/paper/related_work.tex:16:[Omitted long matching line]
175	--
176	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-22-\maketitle
177	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-23-
178	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-24-\begin{abstract}
179	artifacts/dream_reports/dream_20260519T145320/best/paper.tex:25:[Omitted long matching line]
180	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-26-\end{abstract}
181	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-27-
182	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-28-%---------------------------------------------------------------------
183	--
184	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-37-
185	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-38-[Omitted long context line]
186	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-39-
187	artifacts/dream_reports/dream_20260519T145320/best/paper.tex:40:We further validate these findings on Llama-3.1-8B \citep{dubey2024llama3}, confirming that the 26--30$\times$ gap, gradient competition, and zero gating benefit are architecture-independent. A scheduled sampling experiment \citep{bengio2015scheduled} reduces the gap from 30$\times$ to 4.3$\times$ (a 7$\times$ reduction), providing causal evidence that exposure bias accounts for the majority of the training--inference disconnect.
188	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-41-
189	artifacts/dream_reports/dream_20260519T145320/best/paper.tex-42-Our contributions are:
190	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-43-\begin{enumerate}
191	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-44-    \item The first quantitative measurement of how teacher-forcing distribution shift destroys auxiliary attention loss generalization in lightweight residual gating (30$\times$ GAR gap).
192	artifacts/dream_reports/dream_20260519T145320/best/paper.tex-45-    \item Per-layer quantification of NTP--GAR gradient competition: 67--79\% of layers exhibit directional conflict, with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$ during training.
193	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-46-    \item Systematic ablation across two architectures (Qwen-2.5-7B, Llama-3.1-8B) isolating gating, fine-tuning, and loss design as independent factors, with bootstrap statistical validation ($n=50$, $p=0.71$).
194	artifacts/dream_reports/dream_20260519T145320/best/paper.tex:47:    \item Causal evidence via scheduled sampling that exposure bias is the primary driver of the gap (30$\times \to$ 4.3$\times$), upgrading the result from pure negative finding to diagnosis with partial mitigation.
195	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-48-\end{enumerate}
196	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-49-
197	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-50-%---------------------------------------------------------------------
198	--
199	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-60-\paragraph{Attention steering and intervention.}
200	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-61-[Omitted long context line]
201	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-62-
202	artifacts/dream_reports/dream_20260519T145320/best/paper.tex:63:\paragraph{Exposure bias and scheduled sampling.}
203	artifacts/dream_reports/dream_20260519T145320/best/paper.tex:64:[Omitted long matching line]
204	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-65-
205	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-66-%---------------------------------------------------------------------
206	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-67-\section{Background}
207	--
208	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-275-\subsection{Exposure Bias as Causal Factor}
209	artifacts/dream_reports/dream_20260519T145320/best/paper.tex-276-\label{sec:mitigation}
210	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-277-
211	artifacts/dream_reports/dream_20260519T145320/best/paper.tex:278:The 30$\times$ gap points to teacher-forcing distribution shift as the culprit, but correlation is not causation. To establish a causal link, we apply scheduled sampling (SS) to the GAR loss: during training, we linearly increase the proportion of model-generated context (versus gold teacher-forced context) used for GAR computation from 0\% to 50\% over 3 epochs.
212	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-279-
213	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-280-[Omitted long context line]
214	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-281-
215	--
216	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-291-LoRA-only & --- & 0.013 & --- & 2.63 \\
217	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-292-\bottomrule
218	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-293-\end{tabular}
219	artifacts/dream_reports/dream_20260519T145320/best/paper.tex:294:\caption{Exposure bias mitigation via scheduled sampling. Train = GAR-ours; Infer = GAR-Dongre mid-turn. SS reduces the gap by 7$\times$ with minimal PPL cost (+0.08).}
220	artifacts/dream_reports/dream_20260519T145320/best/paper.tex-295-\label{tab:mitigation}
221	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-296-\end{table}
222	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-297-
223	--
224	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-313-Our findings are specific to lightweight residual gating with auxiliary GAR losses. We do not claim that \emph{all} attention steering methods fail; inference-time interventions \citep{li2024inference, meng2022locating} that operate on actual autoregressive contexts are not subject to the same distribution shift. Similarly, heavier architectural modifications (e.g., separate goal-processing pathways) that decouple goal attention from the main NTP computation may avoid gradient competition.
225	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-314-
226	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-315-\paragraph{Constructive directions.}
227	artifacts/dream_reports/dream_20260519T145320/best/paper.tex:316:[Omitted long matching line]
228	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-317-
229	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-318-\paragraph{Relation to Dongre et al.}
230	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-319-\citet{dongre2026} diagnosed goal attention degradation and showed that goal re-injection fails (their Appendix H). We attempted the first systematic cure via residual gating and uncovered the mechanistic reasons for failure. The convergent failure of two independent intervention strategies---goal re-injection and residual gating---strengthens the conclusion that lightweight training-time interventions face fundamental barriers when auxiliary attention losses are trained under teacher-forcing.
231	--
232	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-322-\section{Conclusion}
233	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-323-%---------------------------------------------------------------------
234	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-324-
235	artifacts/dream_reports/dream_20260519T145320/best/paper.tex:325:[Omitted long matching line]
236	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-326-
237	artifacts/dream_reports/dream_20260519T145320/best/paper.tex-327-For practitioners building multi-turn dialogue systems, our results offer a concrete warning: auxiliary attention losses trained under teacher-forcing are particularly vulnerable to distribution shift, and lightweight gating on the residual stream is insufficient to overcome this. Future work should explore inference-time interventions and exposure-bias-aware training for auxiliary attention objectives.
238	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-328-
239	--
240	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-330-\section*{Limitations}
241	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-331-%---------------------------------------------------------------------
242	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-332-
243	artifacts/dream_reports/dream_20260519T145320/best/paper.tex:333:[Omitted long matching line]
244	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-334-
245	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-335-%---------------------------------------------------------------------
246	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex-336-% References
247	--
248	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/discussion.tex-2-
249	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/discussion.tex-3-[Omitted long context line]
250	/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/discussion.tex-4-
251	
252	[Showing results with pagination = limit: 250]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "422d0da6-9227-4331-bd9d-ec1a29e03020",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "76cf5edd-3bf9-4bf4-a887-f6607a6ec0f0",
  "sourceToolAssistantUUID": "422d0da6-9227-4331-bd9d-ec1a29e03020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T21:40:02.195Z_

<details open><summary>🔧 Tool call — Read · `toolu_016srHbSG3JpLR6M2v1Actx9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76cf5edd-3bf9-4bf4-a887-f6607a6ec0f0",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE3W8q9M6KXMdNaRcgA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9f5effd-1c3c-4049-83af-2a2ffb182488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnPHwnGkxmZ1sWGitLfmqZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2407,
      "cache_read_input_tokens": 16260,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2407
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 16260,
          "cache_creation_input_tokens": 2407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2407,
            "ephemeral_1h_input_tokens": 0
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

_source line 12 · 2026-05-23T21:40:02.201Z_

<details><summary>↩ Tool result · `toolu_016srHbSG3JpLR6M2v1Actx9`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Fine-tuned to allocate 50\% of its attention to system-prompt goals (GAR\,=\,0.50 under teacher forcing), Qwen-2.5-7B-Instruct retains only GAR\,=\,0.064 under autoregressive generation---an 8$\times$ collapse that widens to 27$\times$ on Llama-3.1-8B. The collapse has concrete downstream consequences: instruction compliance drops by up to 24 percentage points on content-constrained tasks (\S\ref{sec:discussion}). This paper traces the failure to exposure bias \citep{bengio2015scheduled}: auxiliary attention objectives optimized under teacher-forced prefixes have no autoregressive counterpart, even when next-token prediction (NTP) remains robust.
4	
5	Multi-turn attention decay is well-documented---\citet{dongre2026attention} showed that the Goal Accessibility Ratio (GAR), measuring attention to system-prompt goal tokens, declines 27--48\% across 12 models (we observe 70.8\% on Qwen-2.5-7B) while residual stream probes retain goal content (AUC\,=\,0.98)---but three research gaps remain open. To our knowledge, no work examines how per-layer transformer behavior varies across conversation turns (the \emph{turn$\times$depth} gap). Existing remediations---split-softmax \citep{li2024measuring}, StreamingLLM \citep{xiao2024streaming}, gated attention \citep{qiu2025gated}---operate at inference time or are turn-agnostic; \emph{training-time} multi-turn attention optimization has not been attempted. And classical exposure bias mitigation \citep{bengio2015scheduled,lamb2016professor} targets RNN sequence generation; no \emph{multi-turn transformer equivalent} exists.
6	
7	We introduce ThreadGate---per-layer content-and-turn-conditioned MLP gates on the residual stream: $x_{l+1} = x_l + g_l \cdot f_l(x_l)$---not as a remedy, but as a controlled testbed for isolating failure mechanisms. A five-way comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) forms a causal exclusion chain (\S\ref{sec:comparison-design}): each adjacent pair kills exactly one alternative hypothesis.
8	
9	\begin{figure*}[t]
10	  \centering
11	  \includegraphics[width=\textwidth]{fig1_headline.pdf}
12	  \caption{Exposure bias selectively destroys auxiliary attention losses. (a)~Under TF evaluation, all fine-tuned variants converge to GAR-ours$\approx$0.50; under AR generation ($N$\,=\,50), GAR collapses 7.8--16.7$\times$. Log scale; dashed slopes connect paired TF-AR values. (b)~Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation---not representation degradation---as the proximal cause (9\% PPL cost at $\beta$\,=\,3).}
13	  \label{fig:headline}
14	\end{figure*}
15	
16	Training succeeds: all variants converge to TF GAR\,=\,0.50 (Figure~\ref{fig:headline}a). AR GAR collapses to 0.019--0.064 (8--17$\times$). Gating outperforms LoRA-only ($p$\,=\,0.004) yet the gap remains 7.8$\times$. PCGrad eliminates gradient conflict but \emph{worsens} AR GAR ($p$\,=\,0.002), ruling it out by \emph{modus tollens}. NTP self-recovers \citep{he2019exposure} because prediction is the same task at both regimes; GAR optimizes a prefix property with no AR counterpart. Steering ($\beta$\,=\,5) recovers GAR to 0.727; scheduled sampling compresses the gap to ${\sim}$1.3$\times$ (\S\ref{subsec:ss}).
17	
18	Our contributions: (1)~first empirical measurement of exposure bias on auxiliary attention losses (8--27$\times$ across two architectures); (2)~PCGrad-based causal exclusion of gradient conflict ($p$\,=\,0.002, effect reverses); (3)~inference-time $\beta$-steering recovers GAR to 0.727, confirming attention misallocation---not representation degradation---as the proximal cause; (4)~cross-architecture validation on Llama-3.1-8B confirming generalization; (5)~first evidence that scheduled sampling---originally designed for RNN sequence models---transfers to multi-turn transformer attention objectives, compressing the TF--AR gap from 8$\times$ to ${\sim}$1.3$\times$ with no perplexity cost.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9f5effd-1c3c-4049-83af-2a2ffb182488",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "b469e30b-b8a7-4b39-85c3-fd80b008759d",
  "sourceToolAssistantUUID": "a9f5effd-1c3c-4049-83af-2a2ffb182488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T21:40:08.322Z_

Now let me read the specific lines from the main paper files that were truncated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b469e30b-b8a7-4b39-85c3-fd80b008759d",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE49TeedvJ9miNrRSu7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "406310df-85c4-44f2-9320-0fda6a22a3f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrkN99ARXYUXWm2CGexc11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15193,
      "cache_read_input_tokens": 18667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15193,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T21:40:10.171Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RMCSfPEhCFWaZMhgo68Czk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "406310df-85c4-44f2-9320-0fda6a22a3f8",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE49TeedvJ9miNrRSu7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "682885ce-22f0-46d6-a4e0-c1adf6cb974d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrkN99ARXYUXWm2CGexc11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15193,
      "cache_read_input_tokens": 18667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15193,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T21:40:10.176Z_

<details><summary>↩ Tool result · `toolu_01RMCSfPEhCFWaZMhgo68Czk`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn attention degradation.}
4	Multi-turn coherence remains challenging from early dialogue systems \citep{li2016persona,zhang2020dialogpt,roller2021recipes} through modern long-term conversation models \citep{xu2022goldfish}; evaluations such as Chatbot Arena \citep{zheng2024judging} and MT-Bench-101 \citep{bai2024mtbench101} continue to highlight multi-turn quality gaps. Recent work has quantified specific failure modes: performance drops on later-turn tasks \citep{laban2025lost}, progressive intent mismatch \citep{liu2026intent}, and---most relevant to our work---systematic attention decay. \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\% across 12 models while residual probes retain goal information (AUC\,=\,0.98). We observe a steeper 70.8\% decline on Qwen-2.5-7B (\S\ref{sec:experiments}). This attention-residual dissociation motivates our gating intervention; their work characterizes the phenomenon, ours uncovers why training-time interventions fail to transfer to inference.
5	
6	\paragraph{Instruction stability.}
7	\citet{li2024measuring} independently quantified instruction instability and proposed split-softmax---separating instruction from conversation tokens during attention---as an inference-time remedy. Split-softmax requires no retraining but cannot address exposure bias in auxiliary losses. Our work adds systematic diagnosis (five-way comparison + PCGrad exclusion), exposure bias attribution, and training-time mitigation; our $\beta$-steering complements split-softmax as an alternative inference-time approach (\S\ref{subsec:steering}).
8	
9	\paragraph{Residual gating and attention manipulation.}
10	The transformer \citep{vaswani2017attention} relies on residual connections \citep{he2016deep}, which behave as ensembles of shallow paths \citep{veit2016residual}; highway networks \citep{srivastava2015highway} generalized skip connections with learned gates. Residual scaling \citep{bachlechner2021rezero} and layer pruning \citep{gromov2024unreasonable} exploit layer redundancy; adaptive depth methods \citep{fan2020layerdrop,schuster2022calm,raposo2024mixture,luo2025flexidepth} dynamically allocate computation. Pure self-attention loses rank doubly exponentially with depth \citep{dong2021attention}, underscoring why residual connections are essential; Scheduled DropHead \citep{zhou2020drophead} regularizes attention by dropping entire heads. Attention analyses \citep{clark2019what,voita2019analyzing,kovaleva2019revealing} established head specialization; flow-based \citep{abnar2020quantifying,vig2019multiscale} and identifiability \citep{brunner2020identifiability} methods revealed that raw weights are unreliable as explanatory probes, with contextualized representations growing more context-specific in upper layers \citep{ethayarajh2019contextual}. StreamingLLM \citep{xiao2024streaming} retains anchor tokens; \citet{liu2024lost} and \citet{hsieh2024found} calibrated positional bias; Rhea \citep{hong2025rhea} introduces role-aware episodic attention. PASTA \citep{zhang2024tell} steers attention by reweighting heads; our $\beta$-steering applies additive bias for diagnostic purposes.
11	
12	\paragraph{Gated attention (qiu2025).}
13	Gating has a long history---from gated convolutions \citep{dauphin2017language} to GLU variants now standard in transformer FFNs \citep{shazeer2020glu}. Most relevant is Gated Attention \citep{qiu2025gated}: head-specific sigmoid gates after scaled dot-product attention, achieving MMLU \citep{hendrycks2021measuring} $+$2.03 at scale (15B MoE). The key distinction is granularity: their gate operates per-head within a single forward pass (turn-agnostic), while ThreadGate conditions on turn position to modulate per-layer residual contributions. Our results show that even with turn conditioning, training-time attention objectives face a fundamental exposure bias barrier.
14	
15	\paragraph{Multi-task gradient conflict.}
16	GradNorm \citep{chen2018gradnorm}, PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}, and Nash-MTL \citep{navon2022nash} treat gradient conflict as a root cause. We repurpose PCGrad as a diagnostic: eliminating NTP-GAR directional conflict does not improve GAR convergence---gradient conflict is a symptom, not the cause.
17	
18	\paragraph{Exposure bias.}
19	Teacher forcing creates a distributional mismatch between training and inference \citep{wiseman2016sequence,arora2022exposure}. Scheduled Sampling \citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \citep{ranzato2016sequence}, adversarial regularization \citep{lamb2016professor}, self-recovery analysis \citep{he2019exposure}, bridging strategies for NMT \citep{zhang2019bridging}, and search-based training \citep{leblond2018searnn}. \citet{mihaylova2019scheduled} extended scheduled sampling to transformer architectures via two-pass decoding, though only for single-turn NMT. This literature focuses on primary objectives in single-turn settings. Two gaps remain: no work examines how exposure bias affects \emph{auxiliary} objectives targeting attention distributions, and no multi-turn transformer equivalent of these RNN-era mitigations exists. We fill both: auxiliary attention losses converge under teacher forcing but collapse 8--27$\times$ under AR generation, and scheduled sampling transfers to multi-turn transformer attention objectives.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "682885ce-22f0-46d6-a4e0-c1adf6cb974d",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "78c050cf-ef01-4c41-83e3-f632b57f8f92",
  "sourceToolAssistantUUID": "682885ce-22f0-46d6-a4e0-c1adf6cb974d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T21:40:11.178Z_

<details open><summary>🔧 Tool call — Read · `toolu_011tuoStwGSAqKsxtXEnAGfx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "offset": 53,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78c050cf-ef01-4c41-83e3-f632b57f8f92",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE49TeedvJ9miNrRSu7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d34d4f7d-e7e2-4499-b9b2-c916e69d7d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrkN99ARXYUXWm2CGexc11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15193,
      "cache_read_input_tokens": 18667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15193,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T21:40:11.182Z_

<details><summary>↩ Tool result · `toolu_011tuoStwGSAqKsxtXEnAGfx`</summary>

```text
53	
54	This closes the causal loop: if the collapse were due to representation drift in hidden states, no amount of attention reweighting could recover GAR. The recovery confirms attention misallocation---not representation degradation---as the proximal cause.
55	
56	\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}
57	
58	If exposure bias is the root cause (\S\ref{subsec:dist-shift}), reducing the training-inference distribution mismatch should narrow the gap. Scheduled sampling \citep{bengio2015scheduled}---mixing model-generated tokens into training prefixes with linearly increasing probability---directly targets this mismatch.
59	
60	AR GAR-ours rises from 0.064 to 0.347 (seed 42; gap 7.8$\times$$\to$1.44$\times$) and 0.423 (seed 123; gap 1.18$\times$), yielding a two-seed mean of 0.385 (gap 1.30$\times$) with no PPL cost (1.44 vs.\ 1.43). GAR-Dongre also rises (0.019$\to$0.353; $N$\,=\,5 pilot)---the only intervention that moves both attention metrics. The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
61	
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d34d4f7d-e7e2-4499-b9b2-c916e69d7d09",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "48d57f24-9b4f-408d-92ae-2551b35823be",
  "sourceToolAssistantUUID": "d34d4f7d-e7e2-4499-b9b2-c916e69d7d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T21:40:11.381Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HwWXErpyAoRKzFVa1uVqgT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48d57f24-9b4f-408d-92ae-2551b35823be",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE49TeedvJ9miNrRSu7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "035c7424-1229-4d90-9641-2ff4031bdd87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrkN99ARXYUXWm2CGexc11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15193,
      "cache_read_input_tokens": 18667,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15193
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 18667,
          "cache_creation_input_tokens": 15193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15193,
            "ephemeral_1h_input_tokens": 0
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

_source line 19 · 2026-05-23T21:40:11.388Z_

<details><summary>↩ Tool result · `toolu_01HwWXErpyAoRKzFVa1uVqgT`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	Standard metrics such as perplexity and attention entropy capture generation quality but not \emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation---attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	Different transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent---some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:
22	\begin{equation}
23	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
24	\end{equation}
25	where $f_l$ denotes the sublayer computation (self-attention or FFN). This resembles ReZero \citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training. ThreadGate differs in three ways: (i)~gates are \emph{content-conditioned}---a function of the hidden state, not a fixed scalar; (ii)~gates are \emph{turn-conditioned}---incorporating conversation-position features; (iii)~gates are initialized near identity ($\sigma(1.5) \approx 0.82$) rather than zero, preserving the pretrained model's computation.
26	
27	\paragraph{Gate network.} A fixed scalar per layer (as in ReZero) cannot adapt to varying inputs; the gate must be \emph{content-conditioned} so that different conversations or turns can receive different modulation. Adding \emph{turn conditioning} allows the gate to distinguish early turns (where GAR is naturally high) from late turns (where intervention is most needed). Each gate $g_l$ is thus produced by a two-layer MLP that takes both content and turn features as input:
28	\begin{align}\label{eq:gate}
29	  g_l = \sigma\bigl(W_2\,\text{ReLU}(&W_1\,[\text{proj}(x_l);\;\text{emb}(t_d, t_i)] \notag\\
30	  &+ b_1) + b_2\bigr),
31	\end{align}
32	where $\text{proj}(\cdot)$ reduces the hidden dimension to 16, and $\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\!=\!28$), this adds ${\sim}$57K parameters ($<$0.001\% of 7B).
33	
34	\paragraph{Turn embedding.} The embedding $\text{emb}(t_d, t_i)$ encodes turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables, allowing gates to distinguish conversation positions. The \textbf{Uniform Gate} ablation replaces $\text{emb}(\cdot)$ with a learnable constant, removing turn awareness.
35	
36	\paragraph{Initialization.} Gate biases are set to 1.5 (${\sim}$82\% pass-through), contrasting ReZero's zero initialization that would suppress pretrained capabilities. Gate parameters receive a $10\times$ learning rate multiplier.
37	
38	\subsection{Training Objective}\label{sec:loss}
39	
40	Next-token prediction alone provides no gradient signal for attention allocation---a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:
41	\begin{equation}
42	  \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\,\mathcal{L}_\text{GAR} + \lambda_\text{div}\,\mathcal{L}_\text{div}.
43	\end{equation}
44	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. We use MSE rather than cross-entropy for $\mathcal{L}_\text{GAR}$ because GAR is a continuous ratio, not a probability, and MSE provides \emph{bidirectional} pressure---penalizing both under-attention (GAR\,$<$\,$\tau$) and over-attention (GAR\,$>$\,$\tau$). This symmetry is critical: a unidirectional maximize objective drives gates toward identity (Appendix~\ref{sec:appendix-loss}). The GAR loss is:
45	\begin{equation}
46	  \mathcal{L}_\text{GAR} = \text{MSE}(\text{GAR\text{-}ours}, \tau),
47	\end{equation}
48	where $\tau = 0.5$ targets allocating half of the last token's attention capacity to goal tokens. GAR is measured at the last token of each assistant turn (GAR-ours, \S\ref{sec:background}). Without explicit diversity pressure, all gates converge to the same value (typically near 1.0), eliminating the layer-specific modulation that is the design intent. The gate diversity loss prevents this collapse:
49	\begin{equation}
50	  \mathcal{L}_\text{div} = \text{ReLU}(\sigma_\text{min} - \text{std}(\mathbf{g})),
51	\end{equation}
52	where $\mathbf{g} = [g_1, \ldots, g_L]$ and $\sigma_\text{min}$ is a minimum standard deviation threshold. Both $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$.
53	
54	\paragraph{Loss design evolution.} The MSE formulation was selected from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity. Only MSE provides bidirectional pressure---penalizing both over- and under-attention---preventing identity collapse.
55	
56	\subsection{Controlled Comparison Design}\label{sec:comparison-design}
57	
58	We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate vs.\ Uniform Gate} (turn conditioning), \textbf{ThreadGate vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient direction conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "035c7424-1229-4d90-9641-2ff4031bdd87",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "a60c1c0b-1b12-4225-a087-5e1a8e016d58",
  "sourceToolAssistantUUID": "035c7424-1229-4d90-9641-2ff4031bdd87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-23T21:40:26.923Z_

Now let me also check the analysis/discussion sections for how scheduled sampling is applied to the attention objective specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a60c1c0b-1b12-4225-a087-5e1a8e016d58",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE4jrMtsR31cFFjUmX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f641cb7-383b-4075-9690-8053f7a53741",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmjQoz6pBeby8DadW2xQvB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 33860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4771,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T21:40:28.348Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HdxrpcUBGLVC9KMSVEmc5v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f641cb7-383b-4075-9690-8053f7a53741",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE4jrMtsR31cFFjUmX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da37e129-7905-43e9-b01d-ce83a50371d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmjQoz6pBeby8DadW2xQvB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 33860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4771,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T21:40:28.367Z_

<details><summary>↩ Tool result · `toolu_01HdxrpcUBGLVC9KMSVEmc5v`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison (\S\ref{sec:experiments}) yields a paradox: training succeeds but inference fails, and no single architectural factor explains the gap. This section resolves it through a causal exclusion chain---each subsection kills one alternative hypothesis: \S\ref{subsec:gate-conditioning} kills ``turn conditioning rescues late-turn attention''; \S\ref{subsec:pcgrad} kills ``gradient conflict prevents GAR convergence''; \S\ref{subsec:dist-shift} identifies exposure bias as the surviving explanation. \S\ref{subsec:mechanism-specificity} confirms selectivity via an orthogonal metric, and \S\ref{subsec:cross-model} confirms generalization across architectures.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$)---e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:four-way}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?
8	
9	\begin{figure}[t]
10	  \centering
11	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig3_gate_shift.pdf}
12	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base).}
13	  \label{fig:gate-shift}
14	\end{figure}
15	
16	\subsection{PCGrad Gradient Conflict Exclusion}\label{subsec:pcgrad}
17	
18	NTP and GAR gradients oppose in 68--79\% of layers (cosine similarity $-$0.089$\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$. If this conflict prevents GAR convergence, eliminating it via PCGrad \citep{yu2020pcgrad}---projecting conflicting gradients onto the other's normal plane---should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \emph{diagnostic} tool rather than an optimization method.
19	
20	PCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \emph{worsens}: 0.064$\to$0.030 ($p$\,=\,0.002; Figure~\ref{fig:training-pcgrad}b). By \emph{modus tollens}: removing direction conflict does not prevent collapse; therefore it is not the cause. The 7.5--14.7$\times$ magnitude dominance renders directional interference inconsequential.
21	
22	\begin{figure}[t]
23	  \centering
24	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
25	  \caption{(a)~Gradient cosine similarity between NTP and GAR objectives. ThreadGate remains consistently negative; +PCGrad oscillates around zero. (b)~IID GAR and PPL are unchanged; AR GAR worsens (0.064$\to$0.030), ruling out gradient conflict as the cause.}
26	  \label{fig:training-pcgrad}
27	\end{figure}
28	
29	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
30	
31	The TF-AR GAR gap persists across all variants (Table~\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, so the shift selectively destroys concentrated last-token attention while leaving diffuse attention unaffected. The mechanism is exposure bias \citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. NTP self-recovers \citep{he2019exposure} because prediction is the same task at both regimes; GAR optimizes a distributional property with no autoregressive counterpart. Attention patterns over model-generated tokens have no training-time analogue, explaining why TF GAR-ours remains near $\tau$\,=\,0.5 while AR GAR collapses (77--87\% per-turn decay; Figure~\ref{fig:attention-heatmap}).
32	
33	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
34	
35	We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
36	
37	\subsection{Cross-Model Replication}\label{subsec:cross-model}
38	
39	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20 conversations, 4 turns each). TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only); gating contributes zero benefit, consistent with Qwen. The AR distribution is heavy-tailed (CoV\,$>$\,100\%): ThreadGate shows a 5\% spike ratio (2/40 turns with GAR\,$\geq$\,0.4, std\,=\,0.100) while LoRA-only has 0\% spikes (std\,=\,0.048). We therefore report medians: 0.018 for both TG and LoRA-only (Base: 0.009), yielding TF-AR gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a). Mean GAR-ours is 0.043 (TG) and 0.028 (LoRA-only), gaps of 11$\times$ and 17$\times$---the mean-median divergence confirms that rare high-GAR turns inflate means without reflecting typical model behavior (Appendix~\ref{sec:appendix-llama}).
40	
41	Gate profiles differ qualitatively across architectures (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793, L5\,=\,0.797) while Llama shows a V-shaped valley at output-adjacent layers (L25\,=\,0.719), suggesting that the location of maximum gate attenuation is architecture-dependent---early-middle for Qwen, late-middle for Llama---but the convergence toward identity under NTP pressure is universal. Both architectures share the same outcome: gates learn per-layer variation during training but are driven toward passivity at inference, where NTP dominates. The gap is substantial on both architectures (8--17$\times$ on Qwen, 27$\times$ (median) on Llama), consistent with exposure bias as an architecture-independent phenomenon.
42	
43	\begin{figure}[t]
44	  \centering
45	  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
46	  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers---architecture-dependent patterns, but both converge toward identity.}
47	  \label{fig:crossmodel}
48	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da37e129-7905-43e9-b01d-ce83a50371d2",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "a686c656-ff14-4603-9d18-981128d78f6a",
  "sourceToolAssistantUUID": "da37e129-7905-43e9-b01d-ce83a50371d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T21:40:29.150Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LjxadtMHaYpy9Qs6PkGzMR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 275,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a686c656-ff14-4603-9d18-981128d78f6a",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE4jrMtsR31cFFjUmX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f597b1b8-1252-4c09-ac88-89f1ccba5721",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmjQoz6pBeby8DadW2xQvB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 33860,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4771
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 33860,
          "cache_creation_input_tokens": 4771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4771,
            "ephemeral_1h_input_tokens": 0
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

_source line 24 · 2026-05-23T21:40:29.157Z_

<details><summary>↩ Tool result · `toolu_01LjxadtMHaYpy9Qs6PkGzMR`</summary>

```text
275	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
276	
277	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
278	
279	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
280	
281	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
282	
283	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing. Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42) and 10.8h (seed 123) vs.\ 6.0h for standard ThreadGate on Qwen.
284	
285	\section{Computational Cost Analysis}\label{sec:appendix-cost}
286	
287	\begin{table}[h]
288	\centering\small
289	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (102\,GB VRAM).}
290	\label{tab:cost}
291	\resizebox{\columnwidth}{!}{%
292	\begin{tabular}{lcccc}
293	\toprule
294	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f597b1b8-1252-4c09-ac88-89f1ccba5721",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "4c2de636-ab21-4418-9891-7c7278c3c16e",
  "sourceToolAssistantUUID": "f597b1b8-1252-4c09-ac88-89f1ccba5721",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-23T21:40:33.969Z_

Now let me read the experiments.tex from the beginning to see if there's additional context about scheduled sampling in the main results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c2de636-ab21-4418-9891-7c7278c3c16e",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE63pdMynnW61dEZs5J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "187f2bdc-8d4b-4446-9c60-c3d956fd42ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KdWRQf8aQmuFLtzJQgo7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3207,
      "cache_read_input_tokens": 38631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3207,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-23T21:40:36.401Z_

<details open><summary>🔧 Tool call — Read · `toolu_017jyR4p3fJ3ewEx4LFXnoLk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "offset": 0,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "187f2bdc-8d4b-4446-9c60-c3d956fd42ea",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE63pdMynnW61dEZs5J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aaecfb41-479c-4cd1-b7a4-8a4f0b4c2bff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KdWRQf8aQmuFLtzJQgo7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3207,
      "cache_read_input_tokens": 38631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3207,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-23T21:40:36.406Z_

<details><summary>↩ Tool result · `toolu_017jyR4p3fJ3ewEx4LFXnoLk`</summary>

```text
0	\section{Experiments}
1	\label{sec:experiments}
2	
3	\subsection{Setup}
4	
5	We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and PPL.
6	
7	\subsection{Main Results}
8	
9	Table~\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
10	
11	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}a). The ordering---ThreadGate (0.064) $>$ LoRA-only (0.037) $>$ Uniform Gate (0.033) $>$ PCGrad (0.030) $>$ Base (0.019)---shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendix~\ref{sec:appendix-stats}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). We analyze this distribution shift in \S\ref{sec:analysis}.
12	
13	\begin{table*}[t]
14	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaecfb41-479c-4cd1-b7a4-8a4f0b4c2bff",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "9dae27aa-6b30-494a-9280-8fe87977268f",
  "sourceToolAssistantUUID": "aaecfb41-479c-4cd1-b7a4-8a4f0b4c2bff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-23T21:40:36.550Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q82YqnHu8QtHcQEhQu259j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dae27aa-6b30-494a-9280-8fe87977268f",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE63pdMynnW61dEZs5J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8b53ab8-74d2-4790-bec7-77f5459f05f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KdWRQf8aQmuFLtzJQgo7T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3207,
      "cache_read_input_tokens": 38631,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3207
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 38631,
          "cache_creation_input_tokens": 3207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3207,
            "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-23T21:40:36.554Z_

<details><summary>↩ Tool result · `toolu_01Q82YqnHu8QtHcQEhQu259j`</summary>

```text
1	\begin{abstract}
2	Fine-tuned to allocate 50\% of attention to system-prompt goals (GAR\,=\,0.50 under teacher forcing), Qwen-2.5-7B-Instruct retains only GAR\,=\,0.064 under autoregressive generation---an 8$\times$ collapse that widens to 27$\times$ (median) on Llama-3.1-8B and degrades instruction compliance by up to 24 percentage points. We trace this failure to exposure bias: auxiliary attention losses optimized under teacher-forced prefixes have no autoregressive counterpart. A five-way comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) forms a causal exclusion chain: PCGrad eliminates gradient conflict yet \emph{worsens} AR GAR ($p$\,=\,0.002), ruling out the most intuitive failure mechanism by \emph{modus tollens}. Two interventions breach the barrier: inference-time attention steering ($\beta$\,=\,5) recovers GAR to 0.727, confirming attention misallocation---not representation degradation---as the proximal cause; and scheduled sampling---the first transfer of this RNN-era technique to multi-turn transformer attention objectives---compresses the TF--AR gap from 8$\times$ to ${\sim}$1.3$\times$ with no perplexity cost (two seeds). These findings provide the first empirical characterization of how exposure bias selectively destroys auxiliary attention objectives in multi-turn dialogue.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8b53ab8-74d2-4790-bec7-77f5459f05f1",
  "isSidechain": true,
  "promptId": "02b158d0-7754-45ed-b8ca-5386d1b4cae3",
  "agentId": "a8d70e420d0ceeaee",
  "type": "user",
  "uuid": "acfbe946-d22e-4c80-bf6f-be50c8286d94",
  "sourceToolAssistantUUID": "c8b53ab8-74d2-4790-bec7-77f5459f05f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-23T21:41:09.928Z_

Here are the findings, organized by the three requested items:

---

## 1. The "first" claim about scheduled sampling and attention objectives

**File:** `paper/sections/introduction.tex`, line 18

```
(5)~first evidence that scheduled sampling---originally designed for RNN sequence models---transfers to multi-turn transformer attention objectives, compressing the TF--AR gap from 8$\times$ to ${\sim}$1.3$\times$ with no perplexity cost.
```

This claim also appears in the abstract (`paper/sections/abstract.tex`, line 2):
```
and scheduled sampling---the first transfer of this RNN-era technique to multi-turn transformer attention objectives---compresses the TF--AR gap from 8$\times$ to ${\sim}$1.3$\times$ with no perplexity cost (two seeds).
```

And in the related work section (`paper/sections/related_work.tex`, line 19), the "first" framing is echoed:
```
Two gaps remain: no work examines how exposure bias affects \emph{auxiliary} objectives targeting attention distributions, and no multi-turn transformer equivalent of these RNN-era mitigations exists. We fill both: auxiliary attention losses converge under teacher forcing but collapse 8--27$\times$ under AR generation, and scheduled sampling transfers to multi-turn transformer attention objectives.
```

---

## 2. Method section describing how scheduled sampling is applied to the attention objective

The method section (`paper/sections/method.tex`) does **not** describe scheduled sampling. The scheduled sampling description is split across two locations:

**Experiments section** (`paper/sections/experiments.tex`, lines 56-60):
```
\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}

If exposure bias is the root cause (\S\ref{subsec:dist-shift}), reducing the training-inference distribution mismatch should narrow the gap. Scheduled sampling \citep{bengio2015scheduled}---mixing model-generated tokens into training prefixes with linearly increasing probability---directly targets this mismatch.

AR GAR-ours rises from 0.064 to 0.347 (seed 42; gap 7.8$\times$$\to$1.44$\times$) and 0.423 (seed 123; gap 1.18$\times$), yielding a two-seed mean of 0.385 (gap 1.30$\times$) with no PPL cost (1.44 vs.\ 1.43). GAR-Dongre also rises (0.019$\to$0.353; $N$\,=\,5 pilot)---the only intervention that moves both attention metrics. The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
```

**Appendix** (`paper/sections/appendix.tex`, lines 275-283) provides the implementation details:
```
\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}

Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:

\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens.

\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged.

\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing. Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds.
```

---

## 3. Related work discussion about scheduled sampling

**File:** `paper/sections/related_work.tex`, lines 18-19

```
\paragraph{Exposure bias.}
Teacher forcing creates a distributional mismatch between training and inference \citep{wiseman2016sequence,arora2022exposure}. Scheduled Sampling \citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \citep{ranzato2016sequence}, adversarial regularization \citep{lamb2016professor}, self-recovery analysis \citep{he2019exposure}, bridging strategies for NMT \citep{zhang2019bridging}, and search-based training \citep{leblond2018searnn}. \citet{mihaylova2019scheduled} extended scheduled sampling to transformer architectures via two-pass decoding, though only for single-turn NMT. This literature focuses on primary objectives in single-turn settings. Two gaps remain: no work examines how exposure bias affects \emph{auxiliary} objectives targeting attention distributions, and no multi-turn transformer equivalent of these RNN-era mitigations exists. We fill both: auxiliary attention losses converge under teacher forcing but collapse 8--27$\times$ under AR generation, and scheduled sampling transfers to multi-turn transformer attention objectives.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acfbe946-d22e-4c80-bf6f-be50c8286d94",
  "isSidechain": true,
  "agentId": "a8d70e420d0ceeaee",
  "requestId": "req_011CbLE6bS9rMR28jBbjZqpB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eaba54d7-75a9-469d-bab0-80915e811d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "02ed7bd5-deb4-4e9d-bd2f-44e1f1d8ecbc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wkbia2BQSVzJaFvbvgEfH4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 41838,
      "output_tokens": 1310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1374
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1310,
          "cache_read_input_tokens": 41838,
          "cache_creation_input_tokens": 1374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1374,
            "ephemeral_1h_input_tokens": 0
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
