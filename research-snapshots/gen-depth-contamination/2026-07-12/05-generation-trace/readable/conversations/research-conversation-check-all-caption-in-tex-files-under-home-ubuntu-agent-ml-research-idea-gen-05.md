# Research conversation: Check all \caption{...} in .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamina

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-afa0ea3a496ad2b18.jsonl`
- **Structured JSON:** [`d774b4d06205b9b9c98c.json`](../../sessions/d7/d774b4d06205b9b9c98c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-17T07:40:54.370Z_

Check all \caption{...} in .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ for self-containment.

Steps:
1. Grep for \caption in all .tex files, with several lines of context to capture the full caption text
2. For each caption, assess whether it can be understood independently without reading the main text. A good caption should explain:
   - What the figure/table shows
   - Key variables/axes/columns
   - Any necessary context

Flag captions that are:
- Too short/vague (e.g., just "Results" or "Comparison")
- Reference undefined terms or concepts without explanation
- Missing description of what's being shown

Read the relevant .tex files to get full caption content since captions may span multiple lines.

Report each caption with file:line, the caption text, and your assessment (OK or problematic with reason).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "9d44b229-2657-46fc-9ea8-cf75d71c10d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T07:40:54.372Z_

```json
{
  "parentUuid": "9d44b229-2657-46fc-9ea8-cf75d71c10d1",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
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
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "ae2e6334-8d3d-4ff9-a1de-a43198961822",
  "timestamp": "2026-05-17T07:40:54.372Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T07:40:57.184Z_



I'll start by finding all .tex files and grepping for captions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae2e6334-8d3d-4ff9-a1de-a43198961822",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mDD3GmfAw4f7Vjitjn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cac50192-f63b-4e69-a9e3-39cb25b0bf87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MHCzNYtAxpBXpDKTzvGir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7278,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7278,
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

_source line 4 · 2026-05-17T07:40:57.624Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015WWEEJ6VxuxSsx24AjBHVN`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cac50192-f63b-4e69-a9e3-39cb25b0bf87",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mDD3GmfAw4f7Vjitjn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26833fb8-0c23-40c1-9a05-b6433be828d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MHCzNYtAxpBXpDKTzvGir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7278,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7278,
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

_source line 5 · 2026-05-17T07:40:57.639Z_

<details><summary>↩ Tool result · `toolu_015WWEEJ6VxuxSsx24AjBHVN`</summary>

```text
docs/paper/tables/tab_filtering_main.tex
docs/paper/tables/tab_alpha_sweep.tex
docs/paper/tables/tab_pairwise_significance.tex
docs/paper/tables/tab_crossscorer.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/appendix.tex
docs/paper/introduction.tex
docs/paper/experiments_c1.tex
docs/paper/discussion.tex
docs/paper/experiments_c3.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/appendix_extended.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26833fb8-0c23-40c1-9a05-b6433be828d3",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "5ca07379-2986-47a5-ab9c-1d47c0679b40",
  "sourceToolAssistantUUID": "26833fb8-0c23-40c1-9a05-b6433be828d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T07:41:00.821Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QyU4UMaraWNRHR6kqBy5cF`</summary>

```json
{
  "pattern": "\\\\caption",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": true,
  "-C": 5,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ca07379-2986-47a5-ab9c-1d47c0679b40",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mDD3GmfAw4f7Vjitjn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "985db653-c504-44ab-a3ed-a587090022db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MHCzNYtAxpBXpDKTzvGir",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7278,
      "cache_read_input_tokens": 8250,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7278
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 277,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7278,
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

_source line 7 · 2026-05-17T07:41:00.845Z_

<details><summary>↩ Tool result · `toolu_01QyU4UMaraWNRHR6kqBy5cF`</summary>

```text
&lt;persisted-output>
Output too large (31.7KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/6e3e661b-78e0-4143-9a02-a768d54c2bb3/tool-results/toolu_01QyU4UMaraWNRHR6kqBy5cF.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-6-We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-7-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-8-\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-9-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-10-\small
docs/paper/experiments_c3.tex:11:\caption{Downstream filtering performance (5 seeds). Full $\alpha$ sweep and significance tests in Appendix~\ref{sec:extended_limitations}.}
docs/paper/experiments_c3.tex-12-\label{tab:tab_filtering_main}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-13-\input{tables/tab_filtering_main}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-14-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-15-
docs/paper/experiments_c3.tex-16-Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
--
docs/paper/appendix_extended.tex-12-Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "985db653-c504-44ab-a3ed-a587090022db",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "aeb83486-9b56-4e92-9a28-846170c9a589",
  "sourceToolAssistantUUID": "985db653-c504-44ab-a3ed-a587090022db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-17T07:41:06.383Z_

Let me read the full grep output and all the relevant .tex files to capture complete multi-line captions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aeb83486-9b56-4e92-9a28-846170c9a589",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mDs8yEWTETKiSCgkzz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "600679c1-f339-40f9-9909-baacaf06ba73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCKkHN91wdNk3X73Ck5NkB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2188,
      "cache_read_input_tokens": 15528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2188,
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

_source line 9 · 2026-05-17T07:41:10.937Z_

<details open><summary>🔧 Tool call — Read · `toolu_019P7qW7C5ckg3ouCuLRBTKj`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/6e3e661b-78e0-4143-9a02-a768d54c2bb3/tool-results/toolu_01QyU4UMaraWNRHR6kqBy5cF.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "600679c1-f339-40f9-9909-baacaf06ba73",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mDs8yEWTETKiSCgkzz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e781d6f3-e5ef-49b4-838d-5b2600fcb62a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCKkHN91wdNk3X73Ck5NkB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2188,
      "cache_read_input_tokens": 15528,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2188
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 15528,
          "cache_creation_input_tokens": 2188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2188,
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

_source line 10 · 2026-05-17T07:41:11.187Z_

<details><summary>↩ Tool result · `toolu_019P7qW7C5ckg3ouCuLRBTKj`</summary>

```text
1	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-6-We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
2	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-7-
3	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-8-\begin{table}[t]
4	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-9-\centering
5	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-10-\small
6	docs/paper/experiments_c3.tex:11:\caption{Downstream filtering performance (5 seeds). Full $\alpha$ sweep and significance tests in Appendix~\ref{sec:extended_limitations}.}
7	docs/paper/experiments_c3.tex-12-\label{tab:tab_filtering_main}
8	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-13-\input{tables/tab_filtering_main}
9	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-14-\end{table}
10	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex-15-
11	docs/paper/experiments_c3.tex-16-Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
12	--
13	docs/paper/appendix_extended.tex-12-Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
14	docs/paper/appendix_extended.tex-13-Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 90--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
15	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-14-
16	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-15-\begin{minipage}{\columnwidth}
17	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-16-\centering
18	docs/paper/appendix_extended.tex:17:\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
19	docs/paper/appendix_extended.tex-18-\label{tab:crossscorer}
20	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-19-\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
21	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-20-\end{minipage}
22	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-21-
23	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-22-\begin{table}[h]
24	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-23-\centering
25	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-24-\small
26	docs/paper/appendix_extended.tex:25:\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N{=}400$ (16 cells $\times$ 5 folds $\times$ 5 depth-pairs). The non-significant Scorer main effect confirms scorer independence of depth discrimination.}
27	docs/paper/appendix_extended.tex-26-\label{tab:anova_crossscorer}
28	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-27-\begin{tabular}{lrrrr}
29	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-28-\toprule
30	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-29-\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
31	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-30-\midrule
32	--
33	docs/paper/appendix_extended.tex-95-To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
34	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-96-
35	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-97-\begin{table}[h]
36	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-98-\centering
37	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-99-\small
38	docs/paper/appendix_extended.tex:100:\caption{MMLU by contamination ratio and filtering strategy (5 seeds, mean $\pm$ std). Base model: 0.6018.}
39	docs/paper/appendix_extended.tex-101-\label{tab:dose_response}
40	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-102-\begin{tabular}{lccc}
41	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-103-\toprule
42	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-104-\textbf{Strategy} & \textbf{10\%} & \textbf{30\%} & \textbf{50\%} \\
43	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-105-\midrule
44	--
45	docs/paper/experiments_c1.tex-10-\label{sec:kstar_boundary}
46	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-11-
47	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-12-\begin{table*}[t]
48	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-13-\centering
49	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-14-\small
50	docs/paper/experiments_c1.tex:15:\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
51	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-16-$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
52	docs/paper/experiments_c1.tex-17-Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
53	docs/paper/experiments_c1.tex-18-\label{tab:kstar_ci}
54	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-19-\begin{tabular}{lcccccccccc}
55	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-20-\toprule
56	--
57	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-34-\end{table*}
58	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-35-
59	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-36-\begin{figure}[t]
60	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-37-\centering
61	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-38-\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
62	docs/paper/experiments_c1.tex:39:\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
63	docs/paper/experiments_c1.tex-40-\label{fig:auc_decay}
64	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-41-\end{figure}
65	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-42-
66	docs/paper/experiments_c1.tex-43-Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 8 model configurations: 7/8 yield $\Kempirical{=}2$ (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while Mistral-7B is the sole exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, below $\theta$; Section~\ref{sec:boundary_cases}).
67	docs/paper/experiments_c1.tex-44-LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123$; borderline: 1/5 folds falls below $\theta$, pending bootstrap CI; Table~\ref{tab:kstar_ci_extended}).
68	--
69	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-50-A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.
70	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-51-
71	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-52-\begin{figure}[t]
72	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-53-\centering
73	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-54-\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
74	docs/paper/experiments_c1.tex:55:\caption{$\Kempirical$ vs.\ $\theta$ for six configurations. Dashed line: $\theta{=}0.60$ (all yield $\Kempirical{=}2$). At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
75	docs/paper/experiments_c1.tex-56-\label{fig:kstar_theta}
76	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-57-\end{figure}
77	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-58-
78	docs/paper/experiments_c1.tex-59-Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: unanimous $\Kempirical = 2$ holds within $\theta \in [0.58, 0.60]$; at $\theta{=}0.55$, two Qwen configurations reach $\Kempirical = 3$; at $\theta{=}0.70$, all drop to $\Kempirical = 1$.
79	docs/paper/experiments_c1.tex-60-All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).
80	--
81	docs/paper/experiments_c1.tex-64-\label{sec:transfer}
82	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-65-
83	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-66-\begin{figure}[t]
84	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-67-\centering
85	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-68-\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
86	docs/paper/experiments_c1.tex:69:\caption{Cross-model transfer heatmap (6-class ordinal accuracy). Pythia$\leftrightarrow$OLMo achieves 90--92\% retention; Qwen-rewrite$\to$continuation-mode models: 61--63\%.}
87	docs/paper/experiments_c1.tex-70-\label{fig:transfer_heatmap}
88	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-71-\end{figure}
89	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-72-
90	docs/paper/experiments_c1.tex-73-Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
91	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-74-Qwen-rewrite classifiers transfer poorly (61--63\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.
92	--
93	docs/paper/experiments_c1.tex-97-The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D features yield consistent $\Kempirical = 2$ across all families.
94	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-98-
95	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-99-\begin{minipage}{\columnwidth}
96	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-100-\centering
97	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-101-\footnotesize
98	docs/paper/experiments_c1.tex:102:\captionof{table}{Neural probe $\auc$ (frozen-encoder MLP).}
99	docs/paper/experiments_c1.tex-103-\label{tab:neural_probe_crossmodel}
100	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-104-\begin{tabular}{lccc}
101	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-105-\toprule
102	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-106-\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
103	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-107-\midrule
104	--
105	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-123-The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.
106	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-124-
107	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-125-\begin{minipage}{\columnwidth}
108	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-126-\centering
109	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-127-\footnotesize
110	docs/paper/experiments_c1.tex:128:\captionof{table}{Cross-domain $\Kempirical$ (arXiv vs.\ C4/Wikipedia).}
111	docs/paper/experiments_c1.tex-129-\label{tab:domain_kstar}
112	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-130-\begin{tabular}{llccc}
113	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-131-\toprule
114	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-132-\textbf{Domain} & \textbf{Model} & \textbf{1v2 $\auc$} & \textbf{2v3 $\auc$} & $\Kempirical$ \\
115	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-133-\midrule
116	--
117	docs/paper/method.tex-2-\label{sec:method}
118	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-3-
119	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-4-\begin{figure*}[t]
120	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-5-\centering
121	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-6-\includegraphics[width=\textwidth]{figures/pipeline.pdf}
122	docs/paper/method.tex:7:\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
123	docs/paper/method.tex-8-\label{fig:pipeline}
124	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-9-\end{figure*}
125	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-10-
126	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-11-\subsection{Problem Formulation}
127	docs/paper/method.tex-12-\label{sec:formulation}
128	--
129	docs/paper/method.tex-54-Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
130	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-55-
131	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-56-\begin{table}[t]
132	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-57-\centering
133	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-58-\small
134	docs/paper/method.tex:59:\caption{Experimental configurations.}
135	docs/paper/method.tex-60-\label{tab:setup}
136	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-61-\begin{tabular}{llcc}
137	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-62-\toprule
138	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-63-\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
139	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-64-\midrule
140	--
141	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-2-\section{Supplementary Figures}
142	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-3-
143	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-4-\begin{figure}[t]
144	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-5-\centering
145	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-6-\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
146	docs/paper/appendix.tex:7:\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
147	docs/paper/appendix.tex-8-\label{fig:filtering_strategies}
148	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-9-\end{figure}
149	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-10-
150	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-11-\begin{figure}[t]
151	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-12-  \centering
152	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-13-  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
153	docs/paper/appendix.tex:14:  \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
154	docs/paper/appendix.tex-15-  \label{fig:s1_auc_decay_ci}
155	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-16-\end{figure}
156	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-17-
157	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-18-\section{Supplementary Tables}
158	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-19-
159	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-20-%%% Feature ranking table (moved from main text)
160	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-21-\begin{table}[t]
161	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-22-\centering
162	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-23-\small
163	docs/paper/appendix.tex:24:\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
164	docs/paper/appendix.tex-25-\label{tab:top_features}
165	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-26-\begin{tabular}{cllll}
166	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-27-\toprule
167	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-28-Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
168	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-29-\midrule
169	--
170	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-35-\end{table}
171	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-36-
172	docs/paper/appendix.tex-37-%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
173	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-38-\begin{table*}[t]
174	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-39-  \centering
175	docs/paper/appendix.tex:40:  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
176	docs/paper/appendix.tex-41-  \label{tab:s1_transfer}
177	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-42-  \begin{tabular}{lcccc}
178	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-43-    \toprule
179	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-44-    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
180	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-45-    \cmidrule(lr){2-5}
181	--
182	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-59-\end{table*}
183	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-60-
184	docs/paper/appendix.tex-61-%%% Table S2: Decoding Ablation AUC (exp-003)
185	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-62-\begin{table*}[t]
186	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-63-  \centering
187	docs/paper/appendix.tex:64:  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
188	docs/paper/appendix.tex-65-  \label{tab:s2_decoding}
189	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-66-  \footnotesize
190	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-67-  \begin{tabular}{lcccc}
191	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-68-    \toprule
192	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-69-    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
193	--
194	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-91-
195	docs/paper/appendix.tex-92-%%% Table S2b: Extended K* CI (all models including new additions)
196	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-93-\begin{table*}[t]
197	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-94-  \centering
198	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-95-  \footnotesize
199	docs/paper/appendix.tex:96:  \caption{Extended pairwise $\auc$ with bootstrap 95\% CIs for all model configurations including new additions.
200	docs/paper/appendix.tex-97-  This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, and Mistral-7B configurations.
201	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-98-  $\Kempirical = 2$ is confirmed across all conditions at $\theta{=}0.60$.}
202	docs/paper/appendix.tex-99-  \label{tab:kstar_ci_extended}
203	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-100-  \begin{tabular}{lcccccccccccccc}
204	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-101-    \toprule
205	--
206	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-115-\end{table*}
207	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-116-
208	docs/paper/appendix.tex-117-%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
209	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-118-\begin{table*}[t]
210	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-119-  \centering
211	docs/paper/appendix.tex:120:  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices
212	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-121-    (Exp-011). Both frontier LLMs achieve high binary detection accuracy
213	docs/paper/appendix.tex-122-    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class
214	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-123-    accuracy (${\sim}0.33$ vs.\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5
215	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-124-    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on
216	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-125-    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as
217	--
218	docs/paper/appendix.tex-129-  \label{tab:s3_llm_zeroshot}
219	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-130-
220	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-131-  \vspace{0.5em}
221	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-132-  \begin{subtable}{0.48\textwidth}
222	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-133-    \centering
223	docs/paper/appendix.tex:134:    \caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}
224	docs/paper/appendix.tex-135-    \label{tab:s3a_gpt55}
225	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-136-    \small
226	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-137-    \begin{tabular}{lcccccc}
227	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-138-      \toprule
228	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-139-      & \multicolumn{5}{c}{Predicted Depth} & \\
229	--
230	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-149-    \end{tabular}
231	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-150-  \end{subtable}
232	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-151-  \hfill
233	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-152-  \begin{subtable}{0.48\textwidth}
234	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-153-    \centering
235	docs/paper/appendix.tex:154:    \caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}
236	docs/paper/appendix.tex-155-    \label{tab:s3b_claude}
237	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-156-    \small
238	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-157-    \begin{tabular}{lcccccc}
239	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-158-      \toprule
240	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-159-      & \multicolumn{5}{c}{Predicted Depth} & \\
241	--
242	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-171-\end{table*}
243	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-172-
244	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-173-\begin{table}[t]
245	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-174-  \centering
246	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-175-  \small
247	docs/paper/appendix.tex:176:  \caption{Per-depth recall (\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
248	docs/paper/appendix.tex-177-  \label{tab:s3c_perdepth}
249	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-178-  \begin{tabular}{lccccc}
250	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-179-    \toprule
251	
252	[Showing results with pagination = limit: 250]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e781d6f3-e5ef-49b4-838d-5b2600fcb62a",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "6454440f-2d8a-4b87-99bd-f471caee4c23",
  "sourceToolAssistantUUID": "e781d6f3-e5ef-49b4-838d-5b2600fcb62a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-17T07:41:16.202Z_

Let me also read the remaining parts of the appendix and other files to get any captions I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6454440f-2d8a-4b87-99bd-f471caee4c23",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mESzSWcyTT7xLFqenS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6d580af-df20-44fd-ab24-0a5557f1af83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QC8XrXeJSf6krnJRHS5MNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 17716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12884,
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

_source line 12 · 2026-05-17T07:41:16.727Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DgEvoFA3p4N649dAkPqHAF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6d580af-df20-44fd-ab24-0a5557f1af83",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mESzSWcyTT7xLFqenS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59babe4d-fe7e-4802-924a-800005544e20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QC8XrXeJSf6krnJRHS5MNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 17716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12884,
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

_source line 13 · 2026-05-17T07:41:16.980Z_

<details><summary>↩ Tool result · `toolu_01DgEvoFA3p4N649dAkPqHAF`</summary>

```text
1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
7	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
8	\label{fig:filtering_strategies}
9	\end{figure}
10	
11	\begin{figure}[t]
12	  \centering
13	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
14	  \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
15	  \label{fig:s1_auc_decay_ci}
16	\end{figure}
17	
18	\section{Supplementary Tables}
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\begin{tabular}{cllll}
27	\toprule
28	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
29	\midrule
30	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
31	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
32	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
33	\bottomrule
34	\end{tabular}
35	\end{table}
36	
37	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
38	\begin{table*}[t]
39	  \centering
40	  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
41	  \label{tab:s1_transfer}
42	  \begin{tabular}{lcccc}
43	    \toprule
44	    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
45	    \cmidrule(lr){2-5}
46	    & Qwen-rw & Pythia & OLMo & Qwen-cont \\
47	    \midrule
48	    Qwen-rw   & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
49	    Pythia    & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
50	    OLMo      & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
51	    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
52	    \bottomrule
53	  \end{tabular}
54	  \vspace{4pt}
55	
56	  \footnotesize
57	  \textit{Transfer retention} between models $A$ and $B$ is defined as $\frac{1}{2}\bigl(\frac{\mathrm{acc}(A \to B)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}} + \frac{\mathrm{acc}(B \to A)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}}\bigr)$.
58	  Notable pairs: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\%, Qwen-rw$\to$Pythia/OLMo 61--63\%.
59	\end{table*}
60	
61	%%% Table S2: Decoding Ablation AUC (exp-003)
62	\begin{table*}[t]
63	  \centering
64	  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
65	  \label{tab:s2_decoding}
66	  \footnotesize
67	  \begin{tabular}{lcccc}
68	    \toprule
69	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
70	    \midrule
71	    0 vs.\ 1 & $.980\;[.977,\,.982]$ & $.995\;[.993,\,.996]$ & $.988\;[.986,\,.990]$ & $.998\;[.998,\,.999]$ \\
72	    1 vs.\ 2 & $.689\;[.680,\,.698]$ & $.687\;[.677,\,.695]$ & $.689\;[.680,\,.697]$ & $.704\;[.695,\,.713]$ \\
73	    \cmidrule(lr){1-5}
74	    2 vs.\ 3 & $.561\;[.552,\,.571]$ & $.592\;[.582,\,.601]$\rlap{$^\dagger$} & $.590\;[.581,\,.600]$ & $.582\;[.572,\,.592]$ \\
75	    3 vs.\ 4 & $.540\;[.531,\,.550]$ & $.547\;[.537,\,.557]$ & $.539\;[.529,\,.549]$ & $.529\;[.519,\,.540]$ \\
76	    4 vs.\ 5 & $.514\;[.503,\,.524]$ & $.507\;[.496,\,.517]^{\ddagger}$ & $.535\;[.524,\,.545]$ & $.524\;[.513,\,.535]$ \\
77	    \midrule
78	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
79	    \midrule
80	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
81	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
82	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
83	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
84	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
85	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
86	    \bottomrule
87	    \multicolumn{5}{l}{${}^{\dagger}$\,CI upper bound (0.601) marginally exceeds $\theta{=}0.60$ by 0.001.} \\
88	    \multicolumn{5}{l}{${}^{\ddagger}$\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}
89	  \end{tabular}
90	\end{table*}
91	
92	%%% Table S2b: Extended K* CI (all models including new additions)
93	\begin{table*}[t]
94	  \centering
95	  \footnotesize
96	  \caption{Extended pairwise $\auc$ with bootstrap 95\% CIs for all model configurations including new additions.
97	  This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, and Mistral-7B configurations.
98	  $\Kempirical = 2$ is confirmed across all conditions at $\theta{=}0.60$.}
99	  \label{tab:kstar_ci_extended}
100	  \begin{tabular}{lcccccccccccccc}
101	    \toprule
102	     & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-base} & \multicolumn{2}{c}{LLaMA-8B} \\
103	    \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}\cmidrule(lr){12-13}\cmidrule(lr){14-15}
104	     & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
105	    \midrule
106	    0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] & .987 & [.985,\,.989] & -- & -- \\
107	    1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} & .626 & [.617,\,.635]\rlap{$^*$} & -- & -- \\
108	    2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] & .550 & [.540,\,.560] & -- & -- \\
109	    3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & & .529 & [.519,\,.540] & -- & -- \\
110	    4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & & .518 & [.508,\,.529] & -- & -- \\
111	    \bottomrule
112	    \multicolumn{15}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons.} \\
113	    \multicolumn{15}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B. ``--'': experiment pending.}
114	  \end{tabular}
115	\end{table*}
116	
117	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
118	\begin{table*}[t]
119	  \centering
120	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices
121	    (Exp-011). Both frontier LLMs achieve high binary detection accuracy
122	    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class
123	    accuracy (${\sim}0.33$ vs.\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5
124	    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on
125	    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as
126	    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,
127	    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.
128	    Per-depth recall comparison with OBD-LightGBM in Table~\ref{tab:s3c_perdepth}.}
129	  \label{tab:s3_llm_zeroshot}
130	
131	  \vspace{0.5em}
132	  \begin{subtable}{0.48\textwidth}
133	    \centering
134	    \caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}
135	    \label{tab:s3a_gpt55}
136	    \small
137	    \begin{tabular}{lcccccc}
138	      \toprule
139	      & \multicolumn{5}{c}{Predicted Depth} & \\
140	      \cmidrule(lr){2-6}
141	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
142	      \midrule
143	      0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
144	      1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
145	      2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
146	      3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
147	      4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
148	      \bottomrule
149	    \end{tabular}
150	  \end{subtable}
151	  \hfill
152	  \begin{subtable}{0.48\textwidth}
153	    \centering
154	    \caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}
155	    \label{tab:s3b_claude}
156	    \small
157	    \begin{tabular}{lcccccc}
158	      \toprule
159	      & \multicolumn{5}{c}{Predicted Depth} & \\
160	      \cmidrule(lr){2-6}
161	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
162	      \midrule
163	      0 & \textbf{69} & 26 &  3 &  0 &  2 & .690 \\
164	      1 &  8 & \textbf{21} & 32 & 11 & 28 & .210 \\
165	      2 &  6 & 36 & \textbf{28} &  5 & 25 & .280 \\
166	      3 &  7 & 20 & 31 & \textbf{10} & 31 & .100 \\
167	      4 &  7 & 28 & 22 &  6 & \textbf{37} & .370 \\
168	      \bottomrule
169	    \end{tabular}
170	  \end{subtable}
171	\end{table*}
172	
173	\begin{table}[t]
174	  \centering
175	  \small
176	  \caption{Per-depth recall (\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
177	  \label{tab:s3c_perdepth}
178	  \begin{tabular}{lccccc}
179	    \toprule
180	    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\
181	    \midrule
182	    OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
183	    GPT-5.5      & 77 & 19 & \textbf{38} & \textbf{24} &  8 \\
184	    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \textbf{37} \\
185	    \bottomrule
186	  \end{tabular}
187	\end{table}
188	
189	%%% Table: Token Length and EOS Truncation Analysis
190	\begin{table*}[t]
191	  \centering
192	  \small
193	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound} for discussion.}
194	  \label{tab:token_length}
195	  \begin{tabular}{lcccccccc}
196	    \toprule
197	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
198	    \cmidrule(lr){2-7}
199	    \textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \textbf{EOS Trunc.\ (\%)} & \textbf{Severity} \\
200	    \midrule
201	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
202	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
203	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\
204	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\
205	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
206	    \midrule
207	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
208	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
209	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
210	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
211	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
212	    \bottomrule
213	  \end{tabular}
214	
215	  \vspace{4pt}
216	  \footnotesize
217	  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.
218	\end{table*}
219	
220	\clearpage
221	\section{Supplementary Details}
222	
223	%%% Table S4: Dataset Statistics
224	\begin{table}[t]
225	  \centering
226	  \small
227	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}
228	  \label{tab:s4_dataset_stats}
229	  \begin{tabular}{clrl}
230	    \toprule
231	    \textbf{Depth} & \textbf{$N$ samples} & \textbf{Mean tokens} & \textbf{Source} \\
232	    \midrule
233	    0 & 5{,}000 & 147.8 & C4 validation (human) \\
234	    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\
235	    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\
236	    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\
237	    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
238	    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
239	    \midrule
240	    \multicolumn{2}{l}{Total} & \multicolumn{2}{l}{30{,}000 samples} \\
241	    \bottomrule
242	  \end{tabular}
243	\end{table}
244	
245	%%% Table S5: Complete 15-D Feature Descriptions
246	\begin{table*}[t]
247	  \centering
248	  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
249	  \label{tab:s5_features}
250	  \begin{tabular}{llp{0.45\textwidth}l}
251	    \toprule
252	    \textbf{Group} & \textbf{Feature} & \textbf{Description} & \textbf{Range} \\
253	    \midrule
254	    \multirow{9}{*}{\rotatebox[origin=c]{90}{\textsc{Surprisal}}}
255	    & \texttt{surp\_mean}   & Mean token surprisal $\frac{1}{T}\sum_t -\log p(x_t \mid x_{&lt;t})$ & $\mathbb{R}^+$ \\
256	    & \texttt{surp\_std}    & Standard deviation of token surprisal & $\mathbb{R}^+$ \\
257	    & \texttt{surp\_skew}   & Skewness of the surprisal distribution & $\mathbb{R}$ \\
258	    & \texttt{surp\_kurt}   & Excess kurtosis of the surprisal distribution & $\mathbb{R}$ \\
259	    & \texttt{surp\_d1\_mean} & Mean of first-order surprisal differences $\Delta s_t = s_{t+1} - s_t$ & $\mathbb{R}$ \\
260	    & \texttt{surp\_d1\_std}  & Std of first-order surprisal differences & $\mathbb{R}^+$ \\
261	    & \texttt{surp\_d1\_skew} & Skewness of first-order surprisal differences & $\mathbb{R}$ \\
262	    & \texttt{surp\_d2\_mean} & Mean of second-order differences $\Delta^2 s_t$ & $\mathbb{R}$ \\
263	    & \texttt{surp\_d2\_std}  & Std of second-order surprisal differences & $\mathbb{R}^+$ \\
264	    \midrule
265	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Lex}}}
266	    & \texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\
267	    & \texttt{hapax\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\
268	    & \texttt{self\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\
269	    \midrule
270	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Freq}}}
271	    & \texttt{freq\_kurtosis}  & Excess kurtosis of word frequency distribution & $\mathbb{R}$ \\
272	    & \texttt{freq\_entropy}   & Shannon entropy of word frequencies: $-\sum p_w \log_2 p_w$ & $\mathbb{R}^+$ \\
273	    & \texttt{low\_freq\_ratio} & Proportion of vocabulary with count $\leq 2$ & $[0, 1]$ \\
274	    \bottomrule
275	  \end{tabular}
276	\end{table*}
277	
278	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
279	\begin{table*}[t]
280	\begin{minipage}[t]{0.45\textwidth}
281	  \centering
282	  \small
283	  \captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
284	  \label{tab:s6_lgbm_params}
285	  \begin{tabular}{ll}
286	    \toprule
287	    \textbf{Parameter} & \textbf{Value} \\
288	    \midrule
289	    \texttt{n\_estimators}      & 200 \\
290	    \texttt{learning\_rate}     & 0.05 \\
291	    \texttt{max\_depth}         & 6 \\
292	    \texttt{num\_leaves}        & 31 \\
293	    \texttt{verbose}            & $-1$ \\
294	    \texttt{n\_jobs}            & $-1$ (all cores) \\
295	    Cross-validation            & 5-fold GroupKFold \\
296	    Grouping key                & \texttt{doc\_id} \\
297	    Objective                   & Binary (per depth pair) \\
298	    \bottomrule
299	  \end{tabular}
300	\end{minipage}\hfill
301	\begin{minipage}[t]{0.52\textwidth}
302	  \centering
303	  \small
304	  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
305	  \label{tab:s7_neural_probe}
306	  \resizebox{\textwidth}{!}{%
307	  \begin{tabular}{ll}
308	    \toprule
309	    \textbf{Component} & \textbf{Details} \\
310	    \midrule
311	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
312	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
313	    Representation    & Last hidden state, attention-masked avg pool \\
314	    Embedding dim     & 1536 / 2048 / 2048 \\
315	    Max sequence len   & 512 tokens \\
316	    \midrule
317	    \multicolumn{2}{l}{\textit{MLP classifier}} \\
318	    Architecture      & $d_{\text{emb}} \to 512 \to 256 \to 6$ \\
319	    Activations       & ReLU \\
320	    Dropout           & 0.1 (after each hidden layer) \\
321	    Output            & 6-class softmax \\
322	    \midrule
323	    \multicolumn{2}{l}{\textit{Training}} \\
324	    Optimizer         & Adam ($\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\
325	    Loss              & Cross-entropy \\
326	    Batch size        & 256 \\
327	    Max epochs        & 20 \\
328	    Early stopping    & Patience = 5 (validation loss) \\
329	    Cross-validation  & 5-fold GroupKFold \\
330	    \bottomrule
331	  \end{tabular}%
332	  }
333	\end{minipage}
334	\end{table*}
335	
336	%%% Table S8: Per-Model Bootstrap CI Results (exp-007)
337	\begin{table*}[t]
338	  \centering
339	  \footnotesize
340	  \caption{Pairwise AUC with bootstrap 95\% confidence intervals for four model-mode configurations (Exp-007, 1{,}000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\theta = 0.60$. Permutation $p$-values test $H_0\colon \auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3\,vs.\,4 ($p = 0.064$) and 4\,vs.\,5 ($p = 0.232$), consistent with convergence to chance at deeper generations.}
341	  \label{tab:s8_cv_folds}
342	  \begin{tabular}{lcccc}
343	    \toprule
344	    \textbf{Depth Pair} & \textbf{Qwen-rewrite} & \textbf{Pythia-1.4B} & \textbf{OLMo-1B} & \textbf{Qwen-cont} \\
345	    \midrule
346	    0 vs.\ 1
347	      & $.996\;[.995,\,.997]$
348	      & $.993\;[.992,\,.994]$
349	      & $.997\;[.996,\,.998]$
350	      & $.997\;[.996,\,.998]$ \\
351	    1 vs.\ 2
352	      & $.696\;[.686,\,.704]$
353	      & $.654\;[.645,\,.663]$
354	      & $.615\;[.605,\,.625]$
355	      & $.611\;[.602,\,.621]$ \\
356	    \cmidrule(lr){1-5}
357	    2 vs.\ 3
358	      & $.589\;[.580,\,.599]$
359	      & $.551\;[.542,\,.563]$
360	      & $.550\;[.540,\,.560]$
361	      & $.561\;[.551,\,.571]$ \\
362	    3 vs.\ 4
363	      & $.544\;[.533,\,.555]$
364	      & $.515\;[.504,\,.526]$
365	      & $.509\;[.497,\,.520]^{\dagger}$
366	      & $.541\;[.531,\,.551]$ \\
367	    4 vs.\ 5
368	      & $.534\;[.524,\,.545]$
369	      & $.514\;[.502,\,.525]$
370	      & $.505\;[.493,\,.515]^{\ddagger}$
371	      & $.514\;[.504,\,.526]$ \\
372	    \bottomrule
373	  \end{tabular}
374	
375	  \vspace{4pt}
376	  \footnotesize
377	  Each cell: AUC $[95\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.
378	  ${}^{\dagger}$\,$p = 0.064$;\; ${}^{\ddagger}$\,$p = 0.232$;\; all other pairs $p < 0.01$.
379	\end{table*}
380	
381	%%% Table S9: Binary Detector Spearman ρ (exp-012)
382	\begin{table*}[t]
383	  \centering
384	  \small
385	  \caption{Spearman rank correlation ($\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}
386	  \label{tab:s9_binary_spearman}
387	  \begin{tabular}{lcccc}
388	    \toprule
389	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
390	    \midrule
391	    \multicolumn{5}{l}{\textit{Spearman $\rho$ with true depth}} \\
392	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
393	    \quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
394	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
395	    \midrule
396	    \multicolumn{5}{l}{\textit{Classification}} \\
397	    \quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\
398	    \midrule
399	    \multicolumn{5}{l}{Random baseline: 0.167 \quad $\Kempirical^{\text{binary}} = 1$ \quad $\Kempirical^{\text{OBD}} = 2$} \\
400	    \bottomrule
401	  \end{tabular}
402	\end{table*}
403	
404	%%% Table S10: Pythia Decoding Ablation (exp-020)
405	\begin{table*}[t]
406	  \centering
407	  \small
408	  \caption{Pairwise $\auc$ with bootstrap 95\% CIs across depth pairs for Pythia-1.4B under four decoding configurations (Exp-020; 10{,}000 bootstrap resamples). Complements Table~\ref{tab:s2_decoding} (Qwen-rewrite) with a second model family. $^\dagger$Greedy decoding triggers repetition collapse in Pythia-1.4B (4-gram repeat rate: $d_0{=}0.01 \to d_1{=}0.72$), inflating 0v1 and 1v2 AUC via lexical degeneracy rather than depth-discriminative features.}
409	  \label{tab:s10_pythia_decoding}
410	  \begin{tabular}{lcccc}
411	    \toprule
412	    \textbf{Depth Pair} & \textbf{Greedy}$^\dagger$ & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
413	    \midrule
414	    0 vs.\ 1 & --- & --- & --- & --- \\
415	    1 vs.\ 2 & --- & --- & --- & --- \\
416	    \cmidrule(lr){1-5}
417	    2 vs.\ 3 & --- & --- & --- & --- \\
418	    3 vs.\ 4 & --- & --- & --- & --- \\
419	    4 vs.\ 5 & --- & --- & --- & --- \\
420	    \midrule
421	    $\Kempirical$ & --- & --- & --- & --- \\
422	    \bottomrule
423	  \end{tabular}
424	\end{table*}
425	
426	%%% Table S11: Length Ablation (exp-021)
427	\begin{table*}[t]
428	  \centering
429	  \small
430	  \caption{Pairwise $\auc$ across depth pairs for three segment lengths (Exp-021; Qwen2.5-1.5B base, continuation mode). $\Kempirical{=}2$ is confirmed for 128 and 256 tokens; 512 tokens yields point estimate $\Kempirical{=}2$ but the 1v2 bootstrap CI lower bound falls marginally below $\theta$.}
431	  \label{tab:s11_length_ablation}
432	  \begin{tabular}{lccc}
433	    \toprule
434	    \textbf{Depth Pair} & \textbf{128 tokens} & \textbf{256 tokens} & \textbf{512 tokens} \\
435	    \midrule
436	    0 vs.\ 1 & --- & --- & --- \\
437	    1 vs.\ 2 & --- & --- & ---$^\dagger$ \\
438	    \cmidrule(lr){1-4}
439	    2 vs.\ 3 & --- & --- & --- \\
440	    3 vs.\ 4 & --- & --- & --- \\
441	    4 vs.\ 5 & --- & --- & --- \\
442	    \midrule
443	    $\Kempirical$ & 2 & 2 & 2$^\dagger$ \\
444	    \bottomrule
445	    \multicolumn{4}{l}{\footnotesize $^\dagger$CI $[0.5979,\,0.6166]$; lower bound ${<}\theta{=}0.60$.}
446	  \end{tabular}
447	\end{table*}
448	
449	%%% Table S12: Domain Ablation
450	\begin{table*}[t]
451	  \centering
452	  \small
453	  \caption{Pairwise $\auc$ across depth pairs for three text domains (Qwen2.5-1.5B-Instruct, continuation mode). Tests generalization of $\Kempirical{=}2$ beyond C4 web text to structured and technical domains.}
454	  \label{tab:s12_domain_ablation}
455	  \begin{tabular}{lccc}
456	    \toprule
457	    \textbf{Depth Pair} & \textbf{C4 (web)} & \textbf{Wikipedia} & \textbf{arXiv} \\
458	    \midrule
459	    0 vs.\ 1 & --- & --- & --- \\
460	    1 vs.\ 2 & --- & --- & --- \\
461	    \cmidrule(lr){1-4}
462	    2 vs.\ 3 & --- & --- & --- \\
463	    3 vs.\ 4 & --- & --- & --- \\
464	    4 vs.\ 5 & --- & --- & --- \\
465	    \midrule
466	    $\Kempirical$ & --- & --- & --- \\
467	    \bottomrule
468	  \end{tabular}
469	\end{table*}
470	
471	%%% Table S13: Scorer Sensitivity Analysis
472	\begin{table*}[t]
473	  \centering
474	  \small
475	  \caption{Scorer sensitivity: $\Kempirical$ under self-scoring vs.\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}
476	  \label{tab:s13_scorer_sensitivity}
477	  \begin{tabular}{lccccc}
478	    \toprule
479	    & & \multicolumn{3}{c}{\textbf{Scorer}} & \\
480	    \cmidrule(lr){3-5}
481	    \textbf{Generator} & \textbf{Mode} & \textbf{Self} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Agreement} \\
482	    \midrule
483	    Qwen-1.5B-Instruct & Rewrite      & 2 & 2 & 2 & \checkmark \\
484	    Qwen-1.5B-Instruct & Continuation & 2 & 1 & 1 & $\times$ \\
485	    Qwen-1.5B (base)   & Continuation & 2 & --- & --- & --- \\
486	    Pythia-1.4B         & Continuation & 2 & --- & --- & --- \\
487	    OLMo-1B             & Continuation & 2 & --- & --- & --- \\
488	    Qwen-7B             & Continuation & 2 & --- & --- & --- \\
489	    Mistral-7B          & Continuation & 1 & --- & --- & --- \\
490	    \bottomrule
491	  \end{tabular}
492	\end{table*}
493	
494	\clearpage
495	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59babe4d-fe7e-4802-924a-800005544e20",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "8d2b0fc5-b042-4fb5-a660-d300c069ffe6",
  "sourceToolAssistantUUID": "59babe4d-fe7e-4802-924a-800005544e20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T07:41:17.222Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TBng2p9Hmncd2t6kGcFGN5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d2b0fc5-b042-4fb5-a660-d300c069ffe6",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mESzSWcyTT7xLFqenS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc0057b5-f0d4-4051-b7e3-c561de7a0a52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QC8XrXeJSf6krnJRHS5MNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 17716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12884,
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

_source line 15 · 2026-05-17T07:41:17.228Z_

<details><summary>↩ Tool result · `toolu_01TBng2p9Hmncd2t6kGcFGN5`</summary>

```text
1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; for general web text, $\Kempirical \leq 2$ across all 8 configurations (1B--8B, 5 families), while structured domains (arXiv) yield $\Kempirical{=}3$, aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6866, 0.7039]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--92\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), enabling single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 90--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{minipage}{\columnwidth}
16	\centering
17	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{minipage}
21	
22	\begin{table}[h]
23	\centering
24	\small
25	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N{=}400$ (16 cells $\times$ 5 folds $\times$ 5 depth-pairs). The non-significant Scorer main effect confirms scorer independence of depth discrimination.}
26	\label{tab:anova_crossscorer}
27	\begin{tabular}{lrrrr}
28	\toprule
29	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
30	\midrule
31	Generator     & 3  & ---  & ---  & --- \\
32	Scorer        & 3  & ---  & ---  & --- \\
33	Depth-Pair    & 4  & ---  & ---  & --- \\
34	Gen$\times$Scorer & 9 & --- & --- & --- \\
35	Gen$\times$Depth  & 12 & --- & --- & --- \\
36	Scorer$\times$Depth & 12 & --- & --- & --- \\
37	Residual      & $\approx$356 & & & \\
38	\bottomrule
39	\end{tabular}
40	\end{table}
41	
42	\subsection{Feature Importance Across Decoding Strategies}
43	
44	Feature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\rho = 0.914$), while greedy vs.\ $T{=}1.2$ yields lower correlation ($\rho = 0.53$, nonsignificant after Bonferroni).
45	The depth boundary is robust but the optimal feature subset is strategy-dependent.
46	
47	\subsection{Scale and Neural Probe}
48	\label{sec:extended_neural_probe}
49	
50	Cross-scale validation confirms $\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$, 0v1 $= 0.9225$) both exceed $\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text. Scaling to 13B+ remains open.
51	
52	The neural probe yields model-dependent $\Kempirical^{\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia and OLMo, matching the 15D boundary.
53	The 15D model-free features yield $\Kempirical = 2$ consistently across all three model families, confirming their role as a robust lower bound.
54	
55	\subsection{LLM Zero-Shot Baseline}
56	\label{sec:extended_llm}
57	
58	GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\% (95\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\ref{tab:s3_llm_zeroshot}).
59	Per-depth recall confirms convergent failure at depths $\geq 2$ (Section~\ref{sec:why_kstar}).
60	When 6-class probabilities are marginalized to 5 classes ($P(d{\geq}4)$), accuracy rises to 44.4\% but concentrates in depth-4 (recall: 22\%$\to$80\%) while depths 2--3 collapse to 2--8\%; we report raw 6-class results.
61	
62	\subsection{Practical Considerations}
63	
64	All filtering strategies degrade general capabilities (MMLU: 0.6018 $\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\to$ 0.6638--0.6701); our 100\% synthetic setting is an upper bound; in mixed corpora, degradation scales with contamination fraction~\cite{shumailov2024collapse, dohmatob2024model}.
65	$\Kstar$-aware binary filtering reduces MMLU degradation by ${\sim}$50\% ($-$1.53\,pp $\to$ $-$0.77\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).
66	
67	\subsection{Extended Limitations}
68	\label{sec:extended_limitations}
69	
70	\emph{Prompt-chain versus retrain-chain.}
71	Retrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields $\Kempirical{\geq}4$ (1v2 $\auc = 0.9484$, 2v3 $= 0.8888$, 3v4 $= 0.7982$), far exceeding prompt-chain $\Kempirical{=}2$.
72	The elevated signal arises from cumulative model-adaptation artifacts rather than text-intrinsic degradation; prompt-chain $\Kempirical$ is the operationally relevant boundary for data curation.
73	
74	\emph{Threshold sensitivity.}
75	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite/continuation; at $\theta = 0.70$, $\Kempirical = 1$ across all configurations (Figure~\ref{fig:kstar_theta}).
76	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
77	
78	\emph{Structural confound: token length.}
79	In continuation mode the generation prompt is discarded, so all depths $\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\ machine-generated prompt), not structural composition.
80	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
81	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
82	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
83	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
84	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
85	
86	\emph{Graduated filtering.}
87	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
88	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
89	\label{tab:pairwise_significance}
90	
91	\subsection{Dose-Response: Contamination Ratio Effect}
92	\label{sec:dose_response}
93	
94	The main filtering experiments (Section~\ref{sec:filtering}) use 100\% synthetic data to maximize effect size.
95	To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
96	
97	\begin{table}[h]
98	\centering
99	\small
100	\caption{MMLU by contamination ratio and filtering strategy (5 seeds, mean $\pm$ std). Base model: 0.6018.}
101	\label{tab:dose_response}
102	\begin{tabular}{lccc}
103	\toprule
104	\textbf{Strategy} & \textbf{10\%} & \textbf{30\%} & \textbf{50\%} \\
105	\midrule
106	No-filter   & $0.6009 \pm .003$ & $0.5978 \pm .004$ & $0.5932 \pm .004$ \\
107	Binary-ours & $0.6011 \pm .003$ & $0.5988 \pm .003$ & $0.5956 \pm .004$ \\
108	Graduated   & $0.6008 \pm .003$ & $0.5982 \pm .004$ & $0.5944 \pm .004$ \\
109	\bottomrule
110	\end{tabular}
111	\end{table}
112	
113	At 10\% contamination, no-filter MMLU ($0.6009$) remains within noise of the base model ($0.6018$, $\Delta = -0.09$\,pp), and all three strategies are indistinguishable ($\Delta_{\max} = 0.03$\,pp between strategies, $p > 0.8$).
114	At 30\%, differences emerge directionally ($\Delta = 0.10$\,pp, binary vs.\ no-filter) but remain non-significant ($p > 0.3$).
115	At 50\%, binary-ours shows a 0.24\,pp advantage over no-filter, approaching but not reaching significance ($p = 0.12$).
116	The strategy ordering (binary $>$ graduated $>$ no-filter) is consistent with the 100\% setting, but effect sizes scale linearly with contamination fraction.
117	This demonstrates that $\Kstar$-aware curation provides practical benefit primarily when contamination is severe enough to cause measurable quality degradation.
118	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc0057b5-f0d4-4051-b7e3-c561de7a0a52",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "763598e3-ebe1-4d54-9e3b-e783f05d3350",
  "sourceToolAssistantUUID": "cc0057b5-f0d4-4051-b7e3-c561de7a0a52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T07:41:18.170Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Utm55Tfi8ygDbZ4r76jyW7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "763598e3-ebe1-4d54-9e3b-e783f05d3350",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mESzSWcyTT7xLFqenS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a49e6cae-c437-4b53-a449-8c8667a469cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QC8XrXeJSf6krnJRHS5MNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 17716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12884,
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

_source line 17 · 2026-05-17T07:41:18.176Z_

<details><summary>↩ Tool result · `toolu_01Utm55Tfi8ygDbZ4r76jyW7`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on eight model configurations spanning five architecture families:
5	Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
30	\bottomrule
31	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
32	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}
33	\end{tabular}
34	\end{table*}
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
39	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
40	\label{fig:auc_decay}
41	\end{figure}
42	
43	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 8 model configurations: 7/8 yield $\Kempirical{=}2$ (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while Mistral-7B is the sole exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, below $\theta$; Section~\ref{sec:boundary_cases}).
44	LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123$; borderline: 1/5 folds falls below $\theta$, pending bootstrap CI; Table~\ref{tab:kstar_ci_extended}).
45	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
46	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across models in continuation mode ($\Delta = 3.9$\,pp).
47	
48	\paragraph{Scale and instruction-tuning invariance.}
49	$\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$) both exceed $\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\ $> 0.99$ at $\leq$1.5B).
50	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.
51	
52	\begin{figure}[t]
53	\centering
54	\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
55	\caption{$\Kempirical$ vs.\ $\theta$ for six configurations. Dashed line: $\theta{=}0.60$ (all yield $\Kempirical{=}2$). At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
56	\label{fig:kstar_theta}
57	\end{figure}
58	
59	Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: unanimous $\Kempirical = 2$ holds within $\theta \in [0.58, 0.60]$; at $\theta{=}0.55$, two Qwen configurations reach $\Kempirical = 3$; at $\theta{=}0.70$, all drop to $\Kempirical = 1$.
60	All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).
61	
62	%% ====================================================================
63	\subsection{Cross-Model Transfer}
64	\label{sec:transfer}
65	
66	\begin{figure}[t]
67	\centering
68	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
69	\caption{Cross-model transfer heatmap (6-class ordinal accuracy). Pythia$\leftrightarrow$OLMo achieves 90--92\% retention; Qwen-rewrite$\to$continuation-mode models: 61--63\%.}
70	\label{fig:transfer_heatmap}
71	\end{figure}
72	
73	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
74	Qwen-rewrite classifiers transfer poorly (61--63\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.
75	
76	\paragraph{Cross-scorer validation.}
77	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
78	Qwen-rewrite $\Kempirical$ remains 2 under all scorers; Qwen-continuation drops to 1 (1v2 $\auc$: $0.6112 \to 0.5923/0.5858$), consistent with its marginality under self-scoring.
79	Both alternative scorers agree on $\Kempirical$ per generation mode, indicating that $\Kempirical$ is governed by the generation process rather than the scorer.
80	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; $N{=}400$; Table~\ref{tab:anova_crossscorer}) formally tests this independence.
81	
82	%% ====================================================================
83	\subsection{Feature Ordering and Generation Mode}
84	\label{sec:feature_degradation}
85	\label{sec:generation_mode}
86	
87	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
88	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.
89	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
90	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
91	
92	%% ====================================================================
93	\subsection{Neural Probe}
94	\label{sec:neural_probe}
95	
96	Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia and OLMo remain at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3}$: 0.5963, 0.5892).
97	The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D features yield consistent $\Kempirical = 2$ across all families.
98	
99	\begin{minipage}{\columnwidth}
100	\centering
101	\footnotesize
102	\captionof{table}{Neural probe $\auc$ (frozen-encoder MLP).}
103	\label{tab:neural_probe_crossmodel}
104	\begin{tabular}{lccc}
105	\toprule
106	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
107	\midrule
108	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
109	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
110	OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
111	\bottomrule
112	\end{tabular}
113	\end{minipage}
114	
115	%% ====================================================================
116	\subsection{Cross-Domain Variation}
117	\label{sec:cross_domain}
118	
119	The preceding experiments use C4 (general web text).
120	To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) using two model families.
121	Wikipedia yields $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), matching the C4 baseline.
122	Both Qwen-1.5B and Pythia-1.4B yield $\Kempirical{=}3$ for arXiv (Table~\ref{tab:domain_kstar}), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.
123	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.
124	
125	\begin{minipage}{\columnwidth}
126	\centering
127	\footnotesize
128	\captionof{table}{Cross-domain $\Kempirical$ (arXiv vs.\ C4/Wikipedia).}
129	\label{tab:domain_kstar}
130	\begin{tabular}{llccc}
131	\toprule
132	\textbf{Domain} & \textbf{Model} & \textbf{1v2 $\auc$} & \textbf{2v3 $\auc$} & $\Kempirical$ \\
133	\midrule
134	arXiv & Qwen-1.5B  & 0.858 & 0.6436 & 3 \\
135	arXiv & Pythia-1.4B & 0.805 & 0.6545 & 3 \\
136	C4    & Qwen-1.5B  & 0.63  & 0.56   & 2 \\
137	Wikipedia & Qwen-1.5B & 0.62 & 0.55 & 2 \\
138	\bottomrule
139	\end{tabular}
140	\end{minipage}
141	
142	%% ====================================================================
143	\subsection{Binary Detector Confidence}
144	\label{sec:binary_confidence}
145	
146	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
147	The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a49e6cae-c437-4b53-a449-8c8667a469cc",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "fae3295f-7772-4dcf-81fa-b6103e2e8600",
  "sourceToolAssistantUUID": "a49e6cae-c437-4b53-a449-8c8667a469cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T07:41:18.675Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CCbdN6sZ4XEvF499pMCdEo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fae3295f-7772-4dcf-81fa-b6103e2e8600",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mESzSWcyTT7xLFqenS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "258ab146-7e6f-4cd2-a746-0c81d12e44b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QC8XrXeJSf6krnJRHS5MNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 17716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12884,
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

_source line 19 · 2026-05-17T07:41:18.687Z_

<details><summary>↩ Tool result · `toolu_01CCbdN6sZ4XEvF499pMCdEo`</summary>

```text
1	\section{Application: $\Kstar$-Aware Data Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
5	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
6	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{Downstream filtering performance (5 seeds). Full $\alpha$ sweep and significance tests in Appendix~\ref{sec:extended_limitations}.}
12	\label{tab:tab_filtering_main}
13	\input{tables/tab_filtering_main}
14	\end{table}
15	
16	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
17	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
18	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
19	Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
20	DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
21	Under mild contamination where training data remains net-beneficial (MMLU above base model), all filtering strategies converge, consistent with the expectation that filtering value scales with contamination severity (Appendix~\ref{sec:dose_response}).
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "258ab146-7e6f-4cd2-a746-0c81d12e44b4",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "9c539b49-ddcd-47d0-bae5-a1bd4a723630",
  "sourceToolAssistantUUID": "258ab146-7e6f-4cd2-a746-0c81d12e44b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T07:41:19.359Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AU4gtEB4RsVkMARTSGd4ge`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c539b49-ddcd-47d0-bae5-a1bd4a723630",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mESzSWcyTT7xLFqenS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb6f5bb3-e2db-46e3-a34d-7518fa19008a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QC8XrXeJSf6krnJRHS5MNe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12884,
      "cache_read_input_tokens": 17716,
      "output_tokens": 407,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 407,
          "cache_read_input_tokens": 17716,
          "cache_creation_input_tokens": 12884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12884,
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

_source line 21 · 2026-05-17T07:41:19.364Z_

<details><summary>↩ Tool result · `toolu_01AU4gtEB4RsVkMARTSGd4ge`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this guarantees a finite $\Ktheory$ beyond which adjacent generations are indistinguishable.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ is a small-effect-size threshold (Cohen's $h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention.}; justified below).
25	Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
26	
27	\paragraph{Threshold justification.}
28	$\theta{=}0.60$ is supported by three independent lines of evidence.
29	First, it corresponds to Cohen's $h \approx 0.20$, a conventional small-effect-size boundary.
30	Second, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\theta{=}0.60$ well above the empirical null.
31	Third, and most critically, the conclusion $\Kempirical{=}2$ is insensitive to the exact threshold: 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\sim}$5--11\,pp discontinuity that any $\theta \in [0.55, 0.65]$ would separate (Figure~\ref{fig:kstar_theta}; Appendix~\ref{sec:extended_limitations}).
32	Only at extremes does $\Kempirical$ shift: $\theta{=}0.55$ yields $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$ yields $\Kempirical{=}1$ across all configurations.
33	The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
34	
35	\subsection{Features and Classifier}
36	\label{sec:features}
37	
38	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
39	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
40	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
41	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.
42	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
43	
44	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
45	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
46	
47	\subsection{Experimental Setup}
48	\label{sec:experimental_setup}
49	
50	We evaluate six configurations spanning three model families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B (continuation), Pythia-1.4B and OLMo-1B (continuation).
51	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
52	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
53	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
54	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\caption{Experimental configurations.}
60	\label{tab:setup}
61	\begin{tabular}{llcc}
62	\toprule
63	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
64	\midrule
65	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
66	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
67	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
68	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
69	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
70	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
71	\bottomrule
72	\end{tabular}
73	\end{table}
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb6f5bb3-e2db-46e3-a34d-7518fa19008a",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "d1c2905a-47a9-425b-84ff-ad9a7c47d798",
  "sourceToolAssistantUUID": "fb6f5bb3-e2db-46e3-a34d-7518fa19008a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-17T07:41:24.354Z_

Now let me also check the `discussion.tex` and `introduction.tex` for any captions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1c2905a-47a9-425b-84ff-ad9a7c47d798",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mF49nfPzxfbQHoWtQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cab855eb-1853-48dc-96ca-5812949e5918",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLquMPVWMDN3pL7ZRuXxpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23720,
      "cache_read_input_tokens": 30600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23720,
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

_source line 23 · 2026-05-17T07:41:26.237Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0113irZyVaL3PqkfhbBKe61X`</summary>

```json
{
  "pattern": "\\\\caption",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cab855eb-1853-48dc-96ca-5812949e5918",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mF49nfPzxfbQHoWtQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b58784a5-f645-4f5b-ba78-aa04884362c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLquMPVWMDN3pL7ZRuXxpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23720,
      "cache_read_input_tokens": 30600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23720,
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

_source line 24 · 2026-05-17T07:41:26.256Z_

<details><summary>↩ Tool result · `toolu_0113irZyVaL3PqkfhbBKe61X`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b58784a5-f645-4f5b-ba78-aa04884362c2",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "d72fcb93-be4a-4a82-b3af-3bd564a83bc9",
  "sourceToolAssistantUUID": "b58784a5-f645-4f5b-ba78-aa04884362c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T07:41:27.183Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01J4ZSwcAd5oV1N7eniNYaW5`</summary>

```json
{
  "pattern": "\\\\caption",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d72fcb93-be4a-4a82-b3af-3bd564a83bc9",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mF49nfPzxfbQHoWtQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6c1bd2c-84f5-4925-9f20-9de0c40ad115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLquMPVWMDN3pL7ZRuXxpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23720,
      "cache_read_input_tokens": 30600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23720,
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

_source line 26 · 2026-05-17T07:41:27.201Z_

<details><summary>↩ Tool result · `toolu_01J4ZSwcAd5oV1N7eniNYaW5`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6c1bd2c-84f5-4925-9f20-9de0c40ad115",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "4843a810-8901-4548-a774-b98a3978ce12",
  "sourceToolAssistantUUID": "f6c1bd2c-84f5-4925-9f20-9de0c40ad115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T07:41:28.116Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011G6MV7PXXKfRtgj7TbfAic`</summary>

```json
{
  "pattern": "\\\\caption",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4843a810-8901-4548-a774-b98a3978ce12",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mF49nfPzxfbQHoWtQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd440f03-2b6b-4ef0-8884-79ae36b03d01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLquMPVWMDN3pL7ZRuXxpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23720,
      "cache_read_input_tokens": 30600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23720,
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

_source line 28 · 2026-05-17T07:41:28.127Z_

<details><summary>↩ Tool result · `toolu_011G6MV7PXXKfRtgj7TbfAic`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd440f03-2b6b-4ef0-8884-79ae36b03d01",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "249156fc-971c-4cc0-a389-18125460aaa1",
  "sourceToolAssistantUUID": "bd440f03-2b6b-4ef0-8884-79ae36b03d01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T07:41:29.059Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LihoseRAoMkNJMurvugiz9`</summary>

```json
{
  "pattern": "\\\\caption",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "249156fc-971c-4cc0-a389-18125460aaa1",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mF49nfPzxfbQHoWtQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6e06967-759b-4966-851a-4ceda3873388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLquMPVWMDN3pL7ZRuXxpS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23720,
      "cache_read_input_tokens": 30600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23720,
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

_source line 30 · 2026-05-17T07:41:29.070Z_

<details><summary>↩ Tool result · `toolu_01LihoseRAoMkNJMurvugiz9`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6e06967-759b-4966-851a-4ceda3873388",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "af241ce7-68d3-4d54-9cc1-891688a0a3af",
  "sourceToolAssistantUUID": "a6e06967-759b-4966-851a-4ceda3873388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T07:41:29.419Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016Ub5dSn2Mqv5yXmR357DBw`</summary>

```json
{
  "pattern": "\\\\caption",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af241ce7-68d3-4d54-9cc1-891688a0a3af",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mF49nfPzxfbQHoWtQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9d64497-d81a-45d0-a288-562219262ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLquMPVWMDN3pL7ZRuXxpS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23720,
      "cache_read_input_tokens": 30600,
      "output_tokens": 577,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 577,
          "cache_read_input_tokens": 30600,
          "cache_creation_input_tokens": 23720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23720,
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

_source line 32 · 2026-05-17T07:41:29.428Z_

<details><summary>↩ Tool result · `toolu_016Ub5dSn2Mqv5yXmR357DBw`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9d64497-d81a-45d0-a288-562219262ad9",
  "isSidechain": true,
  "promptId": "2ad23513-eb40-4e55-a775-abf496ed25fd",
  "agentId": "afa0ea3a496ad2b18",
  "type": "user",
  "uuid": "e56cf23f-86f1-4e9f-a4ab-e1f9f3ea704d",
  "sourceToolAssistantUUID": "f9d64497-d81a-45d0-a288-562219262ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-17T07:43:47.842Z_

Good. All captions are in `experiments_c1.tex`, `experiments_c3.tex`, `method.tex`, `appendix.tex`, and `appendix_extended.tex`. I now have the full text of every caption. Here is the complete audit.

---

## Caption Self-Containment Audit

### 1. `method.tex:7` (Figure)
**Caption:** "Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction."

**Assessment: OK.** Explains what the figure shows (the pipeline), defines key terms (seed documents, generation operator, depth chain), and names the classifier. Self-contained.

---

### 2. `method.tex:59` (Table)
**Caption:** "Experimental configurations."

**Assessment: PROBLEMATIC.** Too short and vague. Does not explain what the columns represent (Config, Model, Mode, N) or what an "experimental configuration" means in this context. A reader looking at only the table and caption cannot understand what N refers to (number of seed documents per depth? total documents?) or what "Mode" means (rewrite vs. continuation). Should be expanded, e.g., "Summary of model configurations used in all experiments. Config: shorthand label; Model: architecture and size; Mode: generation strategy (rewrite or continuation); $N$: number of seed documents per depth level."

---

### 3. `experiments_c1.tex:15-17` (Table)
**Caption:** "Pairwise $\auc$ for adjacent depth pairs with bootstrap 95% CIs and permutation $p$-values for boundary rows. $\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty. Extended results (all models) in Table~\ref{tab:kstar_ci_extended}."

**Assessment: OK.** Explains what is shown (pairwise AUC for adjacent depths), defines the boundary criterion, explains what the CIs do, and references the extended version. Self-contained.

---

### 4. `experiments_c1.tex:39` (Figure)
**Caption:** "Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$."

**Assessment: OK.** Describes axes implicitly (depth pairs on x, AUC on y), distinguishes line styles, and identifies the threshold line. Reasonably self-contained, though explicitly naming the axes would be ideal.

---

### 5. `experiments_c1.tex:55` (Figure)
**Caption:** "$\Kempirical$ vs.\ $\theta$ for six configurations. Dashed line: $\theta{=}0.60$ (all yield $\Kempirical{=}2$). At $\theta{=}0.70$, all drop to $\Kempirical{=}1$."

**Assessment: PROBLEMATIC (borderline).** The axes are named ($K^*$ vs. $\theta$), key data points are described, but "$\Kempirical$" is used without any in-caption explanation. A reader encountering only this caption would not know that $K^*_{\text{empirical}}$ is the maximum reliably detectable generational depth, or that $\theta$ is the AUC threshold. Minimally, should add a parenthetical like "$\Kempirical$ (empirical detectability boundary)" or "discriminability threshold $\theta$ (AUC cutoff)."

---

### 6. `experiments_c1.tex:69` (Figure)
**Caption:** "Cross-model transfer heatmap (6-class ordinal accuracy). Pythia$\leftrightarrow$OLMo achieves 90--92% retention; Qwen-rewrite$\to$continuation-mode models: 61--63%."

**Assessment: PROBLEMATIC (borderline).** States what the heatmap shows (transfer accuracy), gives key numbers, but does not explain what the rows and columns represent (train model vs. test model), what "retention" means (ratio of off-diagonal to diagonal accuracy), or what "6-class ordinal accuracy" refers to (depth 0--5 classification). A reader seeing only this figure and caption would need more context.

---

### 7. `experiments_c1.tex:102` (Table)
**Caption:** "Neural probe $\auc$ (frozen-encoder MLP)."

**Assessment: PROBLEMATIC.** Too short. Does not explain what the table columns are (2v3 AUC, 95% CI, $K^*_{\text{neural}}$), what "frozen-encoder MLP" means in this context, or what depths are being compared. Should describe: which depth pair is reported, what the neural probe does (classifies generational depth from frozen LM hidden states), and the meaning of $K^*_{\text{neural}}$.

---

### 8. `experiments_c1.tex:128` (Table)
**Caption:** "Cross-domain $\Kempirical$ (arXiv vs.\ C4/Wikipedia)."

**Assessment: PROBLEMATIC.** Too short. Does not explain what the table columns are (1v2 AUC, 2v3 AUC, $K^*_{\text{empirical}}$), what domains are being compared, or what the rows represent. The parenthetical "(arXiv vs. C4/Wikipedia)" is ambiguous since the table shows all three domains, not a comparison of arXiv against C4/Wikipedia. Should describe: "Pairwise AUC and empirical detectability boundary $K^*$ across three text domains (arXiv, C4, Wikipedia) and two model families, showing that structured academic text (arXiv) permits detection to greater depth ($K^*=3$)."

---

### 9. `experiments_c3.tex:11` (Table)
**Caption:** "Downstream filtering performance (5 seeds). Full $\alpha$ sweep and significance tests in Appendix~\ref{sec:extended_limitations}."

**Assessment: PROBLEMATIC.** Too vague. Does not explain what "downstream filtering performance" means (MMLU/HellaSwag accuracy after fine-tuning on filtered data), what the columns/rows represent (filtering strategies vs. benchmark scores), or what the 5 seeds are for (training variance). The caption delegates all substance to the appendix. Should describe the metric being reported, the benchmarks, and what filtering strategies are compared.

---

### 10. `appendix.tex:7` (Figure)
**Caption:** "Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning)."

**Assessment: OK.** Identifies what is plotted (downstream performance), describes the error bars, identifies key lines by color and label, explains the reference line, and names the key finding. Self-contained.

---

### 11. `appendix.tex:14` (Figure)
**Caption:** "Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95% confidence intervals. Error bars computed from 1,000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point."

**Assessment: OK.** Thorough. Explains what is plotted, how CIs are computed, what the shading means, and how it relates to the main text figure.

---

### 12. `appendix.tex:24` (Table)
**Caption:** "Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85."

**Assessment: OK.** Explains what is ranked (features by discriminative power), what bold indicates, and provides cross-model correlation. Self-contained.

---

### 13. `appendix.tex:40` (Table)
**Caption:** "Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (bold) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries."

**Assessment: OK.** Excellent. Fully explains the matrix structure, cell semantics, row/column meaning, bold convention, and how transfer retention is computed.

---

### 14. `appendix.tex:64` (Table)
**Caption:** "Pairwise AUC with bootstrap 95% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10,000 bootstrap resamples). The horizontal rule between depth pairs 1 vs. 2 and 2 vs. 3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings."

**Assessment: OK.** Detailed. Specifies the model, decoding configs, bootstrap details, the boundary separator, and the correlation section.

---

### 15. `appendix.tex:96-98` (Table)
**Caption:** "Extended pairwise $\auc$ with bootstrap 95% CIs for all model configurations including new additions. This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, and Mistral-7B configurations. $\Kempirical = 2$ is confirmed across all conditions at $\theta{=}0.60$."

**Assessment: OK.** Explains what is shown, how it relates to the main text, lists the new additions, and states the key finding.

---

### 16. `appendix.tex:120-128` (Table, parent)
**Caption:** "LLM zero-shot depth classification: $5\times 5$ confusion matrices (Exp-011). Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.8780; Claude Opus 4.6: 0.8818) but near-chance 5-class accuracy ($\sim$0.33 vs. OBD-LightGBM baseline 0.386, evaluated on the full test set $N=5,000$). GPT-5.5 strongly identifies depth-0 text (recall=0.7700) but collapses on depth-4 (recall=0.0800), misclassifying 50/100 depth-4 samples as depth-2. Claude Opus 4.6 shows more uniform errors across depths 1--4, with depth-4 recall (0.3700) substantially exceeding GPT-5.5. Per-depth recall comparison with OBD-LightGBM in Table~\ref{tab:s3c_perdepth}."

**Assessment: OK.** Very thorough. Describes the experiment, both models, key metrics, failure modes, and cross-references.

---

### 17. `appendix.tex:134` (Subtable)
**Caption:** "GPT-5.5 ($N=500$, acc$=0.332$, MAE$=1.102$)"

**Assessment: OK** (as a subtable caption under the detailed parent caption #16). Subtable captions are conventionally brief when the parent caption carries the explanation.

---

### 18. `appendix.tex:154` (Subtable)
**Caption:** "Claude Opus 4.6 ($N=499$, acc$=0.331$, MAE$=1.150$)"

**Assessment: OK** (same reasoning as #17).

---

### 19. `appendix.tex:176` (Table)
**Caption:** "Per-depth recall (%) on balanced $N=500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$."

**Assessment: OK.** Explains the metric (recall), the test set, the key finding, and connects to the broader theme.

---

### 20. `appendix.tex:193` (Table)
**Caption:** "Mean subword token count per depth and EOS truncation rate (%) for depth 1+ across all model configurations (generation limit: 256 tokens). Depth 0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection more conservative, not inflated. See Section~\ref{sec:length_confound} for discussion."

**Assessment: OK.** Thoroughly explains both metrics (token count and EOS truncation), the depth structure, the confound interpretation, and cross-references the discussion.

---

### 21. `appendix.tex:227` (Table)
**Caption:** "Dataset statistics for the generational depth corpus. Depth 0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths 1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p=0.95$, $T=1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure."

**Assessment: OK.** Very detailed. Explains data sources, generation parameters, tokenization, and scope.

---

### 22. `appendix.tex:248` (Table)
**Caption:** "Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9 dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3 dims), and frequency tail shape (3 dims). All features are computed per document."

**Assessment: OK.** Names the feature set, the classifier, groups features, and specifies computation scope.

---

### 23. `appendix.tex:283` (Table, via captionof)
**Caption:** "LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k+1)$; 5-fold GroupKFold cross-validation is grouped by doc_id to prevent data leakage from the same seed document appearing in both train and test."

**Assessment: OK.** Explains the classifier, the decomposition strategy, the CV scheme, and the leakage prevention.

---

### 24. `appendix.tex:304` (Table, via captionof)
**Caption:** "Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP."

**Assessment: OK.** Describes the probe architecture, models used, and embedding strategy.

---

### 25. `appendix.tex:340` (Table)
**Caption:** "Pairwise AUC with bootstrap 95% confidence intervals for four model-mode configurations (Exp-007, 1,000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\theta = 0.60$. Permutation $p$-values test $H_0: \auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3 vs. 4 ($p = 0.064$) and 4 vs. 5 ($p = 0.232$), consistent with convergence to chance at deeper generations."

**Assessment: OK.** Thoroughly explains the table contents, statistical tests, exceptions, and interpretation.

---

### 26. `appendix.tex:385` (Table)
**Caption:** "Spearman rank correlation ($\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation 1. Qwen-rewrite exhibits reversed sign ($\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth."

**Assessment: OK.** Excellent. Defines all three metrics, names the detector methods, provides baseline, and interprets the findings.

---

### 27. `appendix.tex:408` (Table)
**Caption:** "Pairwise $\auc$ with bootstrap 95% CIs across depth pairs for Pythia-1.4B under four decoding configurations (Exp-020; 10,000 bootstrap resamples). Complements Table~\ref{tab:s2_decoding} (Qwen-rewrite) with a second model family. $^\dagger$Greedy decoding triggers repetition collapse in Pythia-1.4B (4-gram repeat rate: $d_0=0.01 \to d_1=0.72$), inflating 0v1 and 1v2 AUC via lexical degeneracy rather than depth-discriminative features."

**Assessment: OK.** Detailed. Identifies model, decoding configs, bootstrap count, relationship to companion table, and the greedy-collapse caveat.

---

### 28. `appendix.tex:430` (Table)
**Caption:** "Pairwise $\auc$ across depth pairs for three segment lengths (Exp-021; Qwen2.5-1.5B base, continuation mode). $\Kempirical=2$ is confirmed for 128 and 256 tokens; 512 tokens yields point estimate $\Kempirical=2$ but the 1v2 bootstrap CI lower bound falls marginally below $\theta$."

**Assessment: OK.** Identifies the ablation variable (segment length), model, mode, and nuances at 512 tokens.

---

### 29. `appendix.tex:453` (Table)
**Caption:** "Pairwise $\auc$ across depth pairs for three text domains (Qwen2.5-1.5B-Instruct, continuation mode). Tests generalization of $\Kempirical=2$ beyond C4 web text to structured and technical domains."

**Assessment: OK.** Identifies the domains, model, mode, and purpose (generalization test). Could mention column names but adequate.

---

### 30. `appendix.tex:475` (Table)
**Caption:** "Scorer sensitivity: $\Kempirical$ under self-scoring vs. cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation)."

**Assessment: OK.** Thorough. Defines self-scoring and cross-scoring, names alternative scorers, states the conclusion, and identifies the exception.

---

### 31. `appendix_extended.tex:17` (Table, via captionof)
**Caption:** "Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1."

**Assessment: OK.** Explains the validation, names scorers, and states the key finding.

---

### 32. `appendix_extended.tex:25` (Table)
**Caption:** "Three-way ANOVA (Generator x Scorer x Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N=400$ (16 cells x 5 folds x 5 depth-pairs). The non-significant Scorer main effect confirms scorer independence of depth discrimination."

**Assessment: OK.** Identifies the statistical test, factors, sample size breakdown, and key finding. Self-contained.

---

### 33. `appendix_extended.tex:100` (Table)
**Caption:** "MMLU by contamination ratio and filtering strategy (5 seeds, mean $\pm$ std). Base model: 0.6018."

**Assessment: PROBLEMATIC (borderline).** While it names the metric (MMLU), the independent variables (contamination ratio, filtering strategy), and provides baseline, it does not explain what "contamination ratio" means (fraction of synthetic data in training mix), what the filtering strategies are, or what model is being fine-tuned. Compared to the appendix figure caption (#10) which is much richer for the same type of content, this is too sparse for standalone comprehension.

---

## Summary of Flagged Captions

| # | Location | Label | Issue |
|---|----------|-------|-------|
| 2 | `method.tex:59` | `tab:setup` | Too short ("Experimental configurations."). Missing column descriptions. |
| 5 | `experiments_c1.tex:55` | `fig:kstar_theta` | Borderline. Uses $K^*_{\text{empirical}}$ and $\theta$ without in-caption definition. |
| 6 | `experiments_c1.tex:69` | `fig:transfer_heatmap` | Borderline. Does not explain row/column semantics or "retention" metric. |
| 7 | `experiments_c1.tex:102` | `tab:neural_probe_crossmodel` | Too short ("Neural probe $\auc$ (frozen-encoder MLP)."). Missing column descriptions, depth pair context. |
| 8 | `experiments_c1.tex:128` | `tab:domain_kstar` | Too short ("Cross-domain $K^*$ (arXiv vs. C4/Wikipedia)."). Missing column descriptions, ambiguous framing. |
| 9 | `experiments_c3.tex:11` | `tab:tab_filtering_main` | Too vague ("Downstream filtering performance (5 seeds)."). Missing metric/benchmark/strategy descriptions. |
| 33 | `appendix_extended.tex:100` | `tab:dose_response` | Borderline. Missing definition of "contamination ratio" and filtering strategy details. |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e56cf23f-86f1-4e9f-a4ab-e1f9f3ea704d",
  "isSidechain": true,
  "agentId": "afa0ea3a496ad2b18",
  "requestId": "req_011Cb7mFoBQWXRfJRhNACqm3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3a47d25-2c3d-4b18-a2d4-81b25a613739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "6e3e661b-78e0-4143-9a02-a768d54c2bb3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAHzLjNYWtAsLm2MK24qe4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 54320,
      "output_tokens": 5652,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 725
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5652,
          "cache_read_input_tokens": 54320,
          "cache_creation_input_tokens": 725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 725,
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
