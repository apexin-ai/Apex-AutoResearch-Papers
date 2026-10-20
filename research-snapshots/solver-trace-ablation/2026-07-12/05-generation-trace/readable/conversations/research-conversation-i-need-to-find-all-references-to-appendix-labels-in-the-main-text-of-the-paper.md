# Research conversation: I need to find ALL references to appendix labels in the main text of the paper at /home/ubuntu/.agent-ml-research-idea_g

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5b7bc955cca621d0.jsonl`
- **Structured JSON:** [`5dfaa4e1455f754f726b.json`](../../sessions/5d/5dfaa4e1455f754f726b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-25T09:10:40.524Z_

I need to find ALL references to appendix labels in the main text of the paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/. 

Search these main text files for any reference to appendix sections, tables, or figures:
- abstract.tex
- introduction.tex  
- method.tex
- experiments.tex
- related_work.tex
- conclusion.tex
- limitations.tex

Specifically, grep for ALL of these appendix labels (from appendix.tex):
- app:setup
- tab:hyperparams
- app:prooffol-construction
- tab:prooffol-vs-folio
- app:extended-discussion
- app:shapley
- app:premise-count
- tab:premise-bin-modes
- tab:bootstrap-ci
- app:statistical-details
- app:hacking-modes
- tab:hacking-taxonomy
- tab:hacking-taxonomy-app
- tab:classifier-precision
- app:h8
- app:detailed-results
- tab:fol-detailed
- tab:fol-beta01-detailed
- tab:prolog-detailed
- tab:prooffol-detailed
- app:beta03
- tab:beta03-detailed
- app:100step
- app:o1-ablation
- app:llama-coldstart
- app:seed-convergence
- app:n2-sensitivity
- tab:n2-sensitivity
- app:8b-results
- tab:8b-combined
- app:ai-assistants
- app:practical-guidelines

For each label, report whether it is referenced in the main text (and from which file/line), or if it is NOT referenced (orphan). Be very thorough — search breadth "very thorough".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b8001cdb-9b65-4f33-9ed1-b46347fe28b8",
  "agentId": "a5b7bc955cca621d0",
  "type": "user",
  "uuid": "f55e2990-30b6-4f67-b0b5-e724efdca77b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T09:10:42.413Z_

I'll help you find all references to appendix labels in the main text files. Let me start by searching for each label across all the specified files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f55e2990-30b6-4f67-b0b5-e724efdca77b",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2XaD3nNMX1iTx1KGCJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9ce1becd-b01f-41f6-a4bf-0e9ca10cb5f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P3w54R7izF9SLwW3nDY3QL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37586,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37586,
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

_source line 3 · 2026-05-25T09:10:42.580Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CpbjhzH2YAKZzQnyNCodwQ`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ce1becd-b01f-41f6-a4bf-0e9ca10cb5f4",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2XaD3nNMX1iTx1KGCJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fba2e411-fbb5-4a17-a86c-c6edfd677db1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P3w54R7izF9SLwW3nDY3QL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37586,
      "cache_read_input_tokens": 0,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 37586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37586,
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

_source line 4 · 2026-05-25T09:10:42.796Z_

<details><summary>↩ Tool result · `toolu_01CpbjhzH2YAKZzQnyNCodwQ`</summary>

```text
total 4496
drwxr-xr-x 5 ubuntu ubuntu    4096 May 25 08:38 .
drwxr-xr-x 4 ubuntu ubuntu    4096 May 25 07:57 ..
drwxr-xr-x 5 ubuntu ubuntu    4096 May 24 12:05 _figure_backups
drwxr-xr-x 2 ubuntu ubuntu    4096 May 25 08:38 _pdf_images
-rw-r--r-- 1 ubuntu ubuntu    1655 May 25 08:38 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu   11615 May 15 20:39 acl.sty
-rw-r--r-- 1 ubuntu ubuntu   45186 May 15 20:39 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu   57290 May 25 07:38 appendix.tex
-rw-r--r-- 1 ubuntu ubuntu    4328 May 25 07:38 checklist.tex
-rw-r--r-- 1 ubuntu ubuntu    1136 May 25 05:35 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu     194 May 20 11:04 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu       1 May 24 17:27 ethics.tex
-rw-r--r-- 1 ubuntu ubuntu   17809 May 15 20:39 experiments.md
-rw-r--r-- 1 ubuntu ubuntu   14697 May 25 08:36 experiments.tex
drwxr-xr-x 8 ubuntu ubuntu    4096 May 24 19:54 figures
-rw-r--r-- 1 ubuntu ubuntu    4592 May 25 05:34 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu     733 May 25 07:49 limitations.tex
-rw-r--r-- 1 ubuntu ubuntu   64823 May 25 08:38 main.aux
-rw-r--r-- 1 ubuntu ubuntu   20327 May 25 08:38 main.bbl
-rw-r--r-- 1 ubuntu ubuntu    1300 May 25 08:38 main.blg
-rw-r--r-- 1 ubuntu ubuntu   20892 May 25 08:38 main.fdb_latexmk
-rw-r--r-- 1 ubuntu ubuntu   20743 May 25 08:38 main.fls
-rw-r--r-- 1 ubuntu ubuntu   45834 May 25 08:38 main.log
-rw-r--r-- 1 ubuntu ubuntu    6652 May 25 08:38 main.out
-rw-r--r-- 1 ubuntu ubuntu 4147554 May 25 08:38 main.pdf
-rw-r--r-- 1 ubuntu ubuntu     911 May 24 19:42 main.tex
-rw-r--r-- 1 ubuntu ubuntu    9078 May 25 07:55 method.tex
-rw-r--r-- 1 ubuntu ubuntu   24519 May 25 04:28 references.bib
-rw-r--r-- 1 ubuntu ubuntu    3379 May 25 05:35 related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fba2e411-fbb5-4a17-a86c-c6edfd677db1",
  "isSidechain": true,
  "promptId": "b8001cdb-9b65-4f33-9ed1-b46347fe28b8",
  "agentId": "a5b7bc955cca621d0",
  "type": "user",
  "uuid": "f6dc5f2b-7b42-4d28-ac03-9dfbbcface74",
  "sourceToolAssistantUUID": "fba2e411-fbb5-4a17-a86c-c6edfd677db1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-25T09:10:44.378Z_

Good! Now let me search for all the appendix labels in the main text files. I'll conduct comprehensive searches for each label across all specified files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6dc5f2b-7b42-4d28-ac03-9dfbbcface74",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2Xjn1wcxKuZrWBmXsW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d32767bd-0db1-4020-a59d-7f109bdc0c27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RXfri4uCrSzWB3D1e56aDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 37586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1832,
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

_source line 6 · 2026-05-25T09:10:47.936Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Gh6kkGpbMGAy8J53CddXmx`</summary>

```json
{
  "pattern": "app:setup|tab:hyperparams|app:prooffol-construction|tab:prooffol-vs-folio|app:extended-discussion|app:shapley|app:premise-count|tab:premise-bin-modes|tab:bootstrap-ci|app:statistical-details|app:hacking-modes|tab:hacking-taxonomy|tab:hacking-taxonomy-app|tab:classifier-precision|app:h8|app:detailed-results|tab:fol-detailed|tab:fol-beta01-detailed|tab:prolog-detailed|tab:prooffol-detailed|app:beta03|tab:beta03-detailed|app:100step|app:o1-ablation|app:llama-coldstart|app:seed-convergence|app:n2-sensitivity|tab:n2-sensitivity|app:8b-results|tab:8b-combined|app:ai-assistants|app:practical-guidelines",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "type": "tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d32767bd-0db1-4020-a59d-7f109bdc0c27",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2Xjn1wcxKuZrWBmXsW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "44e41e90-dca6-4c76-8d25-01c8c4a51710",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RXfri4uCrSzWB3D1e56aDV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 37586,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1832
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 385,
          "cache_read_input_tokens": 37586,
          "cache_creation_input_tokens": 1832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1832,
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

_source line 7 · 2026-05-25T09:10:47.978Z_

<details><summary>↩ Tool result · `toolu_01Gh6kkGpbMGAy8J53CddXmx`</summary>

```text
&lt;persisted-output>
Output too large (22.2KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-director-acd679de/8f1c0800-1749-497c-a3d5-4fd006846ba8/tool-results/toolu_01Gh6kkGpbMGAy8J53CddXmx.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:9:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:10:Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:11:Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention; Appendix~\ref{app:prooffol-construction}); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:24:An $N{=}2$ sensitivity analysis excluding s43 confirms consistent or stronger patterns (Appendix~\ref{app:n2-sensitivity}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:34:A binary variant testing only collective premise necessity misses the collapse entirely ($\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\ref{app:o1-ablation}).
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44e41e90-dca6-4c76-8d25-01c8c4a51710",
  "isSidechain": true,
  "promptId": "b8001cdb-9b65-4f33-9ed1-b46347fe28b8",
  "agentId": "a5b7bc955cca621d0",
  "type": "user",
  "uuid": "21953255-3379-40fa-8e3c-d57ddc21a149",
  "sourceToolAssistantUUID": "44e41e90-dca6-4c76-8d25-01c8c4a51710",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-25T09:10:49.196Z_

Let me read the full output file to see all matches:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21953255-3379-40fa-8e3c-d57ddc21a149",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2Y7unBeogctbxTQiyN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e36fe18e-ac42-451f-a0c7-8229e02255cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LAqFkoigZqckgKuWm4U5ET",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1147,
      "cache_read_input_tokens": 39418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1147,
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

_source line 9 · 2026-05-25T09:10:49.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AYU68ZQfXZ8bjGQjLxHWLG`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-director-acd679de/8f1c0800-1749-497c-a3d5-4fd006846ba8/tool-results/toolu_01Gh6kkGpbMGAy8J53CddXmx.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e36fe18e-ac42-451f-a0c7-8229e02255cd",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2Y7unBeogctbxTQiyN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e8113e04-9ccb-402f-b42c-bf2a99e1ec92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LAqFkoigZqckgKuWm4U5ET",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1147,
      "cache_read_input_tokens": 39418,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1147
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 172,
          "cache_read_input_tokens": 39418,
          "cache_creation_input_tokens": 1147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1147,
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

_source line 10 · 2026-05-25T09:10:49.717Z_

<details><summary>↩ Tool result · `toolu_01AYU68ZQfXZ8bjGQjLxHWLG`</summary>

```text
1	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:9:[Omitted long matching line]
2	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:10:Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
3	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:11:Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention; Appendix~\ref{app:prooffol-construction}); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
4	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:12:[Omitted long matching line]
5	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:24:An $N{=}2$ sensitivity analysis excluding s43 confirms consistent or stronger patterns (Appendix~\ref{app:n2-sensitivity}).
6	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:34:A binary variant testing only collective premise necessity misses the collapse entirely ($\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\ref{app:o1-ablation}).
7	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:35:All three exec-only seeds converge to ${\leq}6.2\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}), confirming that structural degeneration under exec-only reward is not seed-specific among converged runs.
8	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:38:Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\leq}6.2\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}).
9	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:40:Two additional seeds under identical conditions fail to converge ($\text{PR}{\approx}14\%$; Appendix~\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful convergence, though the confound between model capability and optimization success precludes strong causal attribution (Appendix~\ref{app:llama-coldstart}).
10	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:45:Early-training comparison supports this interpretation: at 100 steps ($\text{PR}{=}32\%$), hacking already reaches $31\%$ vs.\ SFT's $8\%$ at comparable PR (Appendix~\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
11	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:55:Three controls constrain the multiplicative confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\ref{app:setup}).
12	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:56:The shuffled-ISR control ($87\%$ non-hacking at low PR) is consistent with the interpretation that Goodhart effects require sample-level ISR signal; however, the low PR (comparable to non-converging exec-only seeds; Appendix~\ref{app:seed-convergence}) means that non-convergence alone cannot be ruled out as an alternative explanation.
13	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:59:ISR reward amplifies TS convergence: $71\%$ of proved samples under ISR exhibit tautological shortcuts vs.\ $14\%$ under random (Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
14	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:62:A seed-stratified $\chi^2$ test confirms the overall mode distribution differs significantly between ISR and random conditions ($\chi^2{=}174.8$, $\text{df}{=}2$, $p{<}10^{-38}$; Appendix~\ref{app:statistical-details}).
15	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:65:ISR reward produces bimodal outcomes (Figure~\ref{fig:seed-divergence}): 3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect can occur under standard training conditions (95\% Clopper--Pearson CI: [11.8\%, 88.1\%]; $n{=}5$); 2 of 5 retain substantial genuine reasoning (seeds~45/46 added post-hoc to test replication; Appendix~\ref{app:detailed-results}).
16	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:66:Excluding seed~43 (which uses nucleus sampling; \S\ref{sec:setup}), seed~44 shows $0\%$ non-hacking and $100\%$ TS at 500 steps; seed~42 retains $17\%$ non-hacking at 500 steps but collapses to $2\%$ by 1000 steps (full $N{=}2$ analysis: Appendix~\ref{app:n2-sensitivity}).
17	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:70:The premise-count-matched comparison yields only $1.06\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.
18	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:73:In the modal premise-count range (4--6 premises, where most proved samples fall), TS reaches $19.7\%$ under ISR versus $0\%$ under random reward (Figure~\ref{fig:premise-bins}; Table~\ref{tab:premise-bin-modes}).
19	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:87:Higher doses accelerate collapse: $\beta{=}0.2$ eliminates all non-hacking; $\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
20	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:104:Under ISR-as-reward, all three seeds reach $0\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\ref{tab:prolog-detailed}).
21	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:112:ISR reward on ProofFOL produces directionally higher genuine rates than exec-only ($p{=}0.10$, exploratory; Table~\ref{tab:prooffol-detailed}).
22	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:116:Qwen3-8B does not converge under exec-only GRPO ($\text{PR}{=}14\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\ref{app:8b-results}).
23	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:124:\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR systematically selects for TS over CE without reducing total hacking; SFT shows near-zero hacking.}
24	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:128:Three modes account for the vast majority of hacking (Appendix Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).
25	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex:4:STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect: structural proxies for formalization integrity are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
26	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex:6:Convergence appears necessary for degeneration (Appendix~\ref{app:seed-convergence}); for practitioners, structural diagnostics should be applied post-hoc, with the mode breakdown providing the reliable signal.
27	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:41:Yes. The model size (4B) is reported in \S\ref{sec:task}. Training details (GRPO $K{=}4$, 500/1000 steps, seeds, batch sizes) are in \S\ref{sec:task} and Appendix~\ref{app:setup}. Computing infrastructure and total GPU hours are reported in Appendix~\ref{app:setup}.
28	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:44:Yes. All hyperparameters are reported in \S\ref{sec:rewards} and Appendix~\ref{app:setup}. No hyperparameter search was performed; $\beta$ values were chosen for dose-response analysis.
29	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:47:Yes. We report mean$\pm$std across seeds (Table~\ref{tab:goodhart-landscape}), per-seed ranges, bootstrap confidence intervals (Appendix Table~\ref{tab:bootstrap-ci}), and discuss statistical power limitations (\S\ref{sec:limitations}).
30	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:50:Yes. We report Qwen3-4B model versions, Prover9, and SWI-Prolog. Training uses TRL 0.17.0, PyTorch 2.6.0, and Transformers 4.51.3; versions are listed in Appendix~\ref{app:setup}.
31	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex:54:Minimal. Manual audit was conducted for classifier precision (50 random CE/TS samples verified; Appendix~\ref{app:hacking-modes}) and for PG false-negative correction (seed 42 only). No crowdsourced annotation was used.
32	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:53:ISR computes the LOO marginal contribution, a restriction of the Shapley value to the maximal coalition (Appendix~\ref{app:shapley}); full interaction detection would require $O(2^n)$ evaluations.
33	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:68:Each RL condition uses seeds $\{42,43,44\}$ and identical training data (formulation alternatives in Appendix~\ref{app:setup}).
34	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:91:\caption{Goodhart landscape across reward conditions. PR = prove rate; ISR$^*$ = proved-only ISR; TS = tautological shortcut; CE = conclusion embedding; N-H = non-hacking (upper bound on genuine reasoning). Multi-seed rows: pooled TS/CE/N-H; PR/ISR$^*$ as mean$\pm$std. $^\dagger$Seed~42 only. $^\ddagger$Premise-count-matched (\S\ref{sec:goodhart}). $^\P$FN-corrected (\S\ref{app:h8}). $^\S$Seed-dependent (s43: 38.3\%). Per-seed data: Table~\ref{tab:fol-detailed}.}
35	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:96:Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}), dominated by three: \textbf{CE} (conclusion embedded among multiple premises), \textbf{TS} (single-premise conclusion duplication; targets ISR directly since removing the sole premise forces $\text{ISR}\geq 0.5$), and \textbf{PG} (premise-subset gaming: each component is LOO-necessary but the premise set is incomplete; Appendix~\ref{app:h8}).
36	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex:6:ISR quantifies component necessity, not semantic faithfulness; its diagnostic value is realized through the mode breakdown, not the scalar alone (Appendix~\ref{app:extended-discussion}).
37	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:4:\label{app:setup}
38	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:6:Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
39	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:13:\label{tab:hyperparams}
40	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:68:\label{app:prooffol-construction}
41	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:72:Table~\ref{tab:prooffol-vs-folio} compares key structural properties.
42	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:77:\label{tab:prooffol-vs-folio}
43	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:99:\label{app:extended-discussion}
44	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:114:\label{app:shapley}
45	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:121:\label{app:premise-count}
46	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:125:Premise-count-matched comparison eliminates the difference ($1.06\times$, McNemar's test $p{=}0.317$; Table~\ref{tab:fol-beta01-detailed}), confirming that the scalar ISR advantage is not statistically significant.
47	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:128:Mode composition analysis (CE vs.\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\S\ref{app:hacking-modes}), not on the number of premises in the formalization.
48	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:148:\label{tab:premise-bin-modes}
49	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:153:\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
50	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:154:\label{tab:bootstrap-ci}
51	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:173:{\small ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown. Pooled statistics treat within-seed samples as independent and serve as descriptive summaries only; the seed-stratified CMH test (\S\ref{app:statistical-details}) accounts for within-seed dependence.}
52	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:192:In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-detailed}).
53	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:197:\label{app:practical-guidelines}
54	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:206:\label{app:statistical-details}
55	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:222:\label{app:hacking-modes}
56	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:225:TS comprises two subtypes: TSa (text-match duplication, where the premise is textually identical to the conclusion) and TSb (obfuscated tautology, where the premise is logically equivalent but textually distinct; \S\ref{app:h8}).
57	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:249:\label{tab:hacking-taxonomy}
58	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:252:Table~\ref{tab:hacking-taxonomy} provides a compact cross-condition summary; Table~\ref{tab:hacking-taxonomy-app} below gives the extended breakdown.
59	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:271:[Omitted long matching line]
60	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:272:\label{tab:hacking-taxonomy-app}
61	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:283:This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
62	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:309:\label{tab:classifier-precision}
63	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:315:\label{app:h8}
64	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:548:\label{app:detailed-results}
65	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:550:Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
66	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:557:\label{tab:fol-detailed}
67	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:558:\label{tab:fol-beta01-detailed}
68	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:602:  & \multicolumn{8}{l}{See Table~\ref{tab:beta03-detailed} for per-seed $\beta{=}0.3$ results.} \\
69	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:631:\label{tab:prolog-detailed}
70	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:664:\label{tab:prooffol-detailed}
71	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:693:Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
72	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:706:\label{app:beta03}
73	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:708:Table~\ref{tab:beta03-detailed} reports per-seed results for ISR at $\beta{=}0.2$ and both ISR and Random at $\beta{=}0.3$.
74	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:715:\label{tab:beta03-detailed}
75	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:748:\label{app:100step}
76	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:757:\label{app:o1-ablation}
77	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:781:\label{app:llama-coldstart}
78	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:783:We applied the identical GRPO configuration (Table~\ref{tab:hyperparams}) to LLaMA-3.2-3B~\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).
79	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:794:\label{app:seed-convergence}
80	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:801:This parallels the LLaMA-3.2-3B finding (Appendix~\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.
81	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:805:\label{app:n2-sensitivity}
82	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:807:Seed~43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding (\S\ref{app:setup}).
83	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:808:To assess whether this non-standard protocol affects qualitative conclusions, Table~\ref{tab:n2-sensitivity} reports pooled statistics from seeds~42 and~44 only.
84	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:823:\label{tab:n2-sensitivity}
85	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:831:\label{app:8b-results}
86	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:834:Table~\ref{tab:8b-combined} summarizes configuration differences and results.
87	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:863:\label{tab:8b-combined}
88	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:870:This result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.
89	/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:874:\label{app:ai-assistants}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8113e04-9ccb-402f-b42c-bf2a99e1ec92",
  "isSidechain": true,
  "promptId": "b8001cdb-9b65-4f33-9ed1-b46347fe28b8",
  "agentId": "a5b7bc955cca621d0",
  "type": "user",
  "uuid": "e2562836-c318-48c8-8683-58cc643ed52b",
  "sourceToolAssistantUUID": "e8113e04-9ccb-402f-b42c-bf2a99e1ec92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-25T09:10:51.404Z_

Now let me search for each label individually in the main text files to create a complete summary. Let me check the individual main text files more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2562836-c318-48c8-8683-58cc643ed52b",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2YFVC5xH5dNPx7qJxH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3db698b2-d6be-4088-8559-367b33af2510",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JUNQjrvy2yoH6yFXAsjnMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8040,
      "cache_read_input_tokens": 40565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8040,
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

_source line 12 · 2026-05-25T09:10:52.125Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CYb5qhFHgfAatWiaf1QzU4`</summary>

```json
{
  "command": "grep -n \"ref{app:\\|ref{tab:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex 2>/dev/null || echo \"No matches in abstract.tex\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3db698b2-d6be-4088-8559-367b33af2510",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2YFVC5xH5dNPx7qJxH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5120016-3711-489d-b87c-1724d3fe0737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JUNQjrvy2yoH6yFXAsjnMH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8040,
      "cache_read_input_tokens": 40565,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8040
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 147,
          "cache_read_input_tokens": 40565,
          "cache_creation_input_tokens": 8040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8040,
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

_source line 13 · 2026-05-25T09:10:52.214Z_

<details><summary>↩ Tool result · `toolu_01CYb5qhFHgfAatWiaf1QzU4`</summary>

```text
No matches in abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5120016-3711-489d-b87c-1724d3fe0737",
  "isSidechain": true,
  "promptId": "b8001cdb-9b65-4f33-9ed1-b46347fe28b8",
  "agentId": "a5b7bc955cca621d0",
  "type": "user",
  "uuid": "24efae02-8639-489e-b479-a0d67e166915",
  "sourceToolAssistantUUID": "d5120016-3711-489d-b87c-1724d3fe0737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T09:10:53.967Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011JeRH3Hooq7Cx3wwbQcjxv`</summary>

```json
{
  "command": "grep -n \"ref{app:\\|ref{tab:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex 2>/dev/null || echo \"No matches in introduction/related_work\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24efae02-8639-489e-b479-a0d67e166915",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2YSM3cK7jt5KqxGr1g",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "44cce766-d654-4ad4-bd91-e04f874e1c74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NY6aYcqZhQazBd9e2JG8qA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 165,
      "cache_read_input_tokens": 48605,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 165
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 156,
          "cache_read_input_tokens": 48605,
          "cache_creation_input_tokens": 165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 165,
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

_source line 15 · 2026-05-25T09:10:54.042Z_

<details><summary>↩ Tool result · `toolu_011JeRH3Hooq7Cx3wwbQcjxv`</summary>

```text
No matches in introduction/related_work
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44cce766-d654-4ad4-bd91-e04f874e1c74",
  "isSidechain": true,
  "promptId": "b8001cdb-9b65-4f33-9ed1-b46347fe28b8",
  "agentId": "a5b7bc955cca621d0",
  "type": "user",
  "uuid": "f670ad6c-4e4a-4057-911d-ebca1a00eaef",
  "sourceToolAssistantUUID": "44cce766-d654-4ad4-bd91-e04f874e1c74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-25T09:10:55.469Z_

Good. Now let me get detailed line numbers for each appendix label mentioned in the main text files. Let me search more systematically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f670ad6c-4e4a-4057-911d-ebca1a00eaef",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2YZqW2VpMybWSjsSpW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e44b869-ad7b-47d2-8276-bf31317ecf3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UnogKv6r96fqcWGxVEHQPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 48770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 176,
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

_source line 17 · 2026-05-25T09:11:00.239Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QgJ1Sup5qYXC37vpYbak99`</summary>

```json
{
  "command": "cat > /tmp/check_labels.sh << 'ENDSCRIPT'\n#!/bin/bash\n\n# Define all appendix labels to search for\nlabels=(\n\"app:setup\"\n\"tab:hyperparams\"\n\"app:prooffol-construction\"\n\"tab:prooffol-vs-folio\"\n\"app:extended-discussion\"\n\"app:shapley\"\n\"app:premise-count\"\n\"tab:premise-bin-modes\"\n\"tab:bootstrap-ci\"\n\"app:statistical-details\"\n\"app:hacking-modes\"\n\"tab:hacking-taxonomy\"\n\"tab:hacking-taxonomy-app\"\n\"tab:classifier-precision\"\n\"app:h8\"\n\"app:detailed-results\"\n\"tab:fol-detailed\"\n\"tab:fol-beta01-detailed\"\n\"tab:prolog-detailed\"\n\"tab:prooffol-detailed\"\n\"app:beta03\"\n\"tab:beta03-detailed\"\n\"app:100step\"\n\"app:o1-ablation\"\n\"app:llama-coldstart\"\n\"app:seed-convergence\"\n\"app:n2-sensitivity\"\n\"tab:n2-sensitivity\"\n\"app:8b-results\"\n\"tab:8b-combined\"\n\"app:ai-assistants\"\n\"app:practical-guidelines\"\n)\n\n# Main text files to search\nmain_files=(\n\"abstract.tex\"\n\"introduction.tex\"\n\"method.tex\"\n\"experiments.tex\"\n\"related_work.tex\"\n\"conclusion.tex\"\n\"limitations.tex\"\n)\n\npaper_dir=\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper\"\n\necho \"=== APPENDIX LABEL REFERENCE AUDIT ===\"\necho \"\"\n\nfor label in \"${labels[@]}\"; do\n    found=0\n    echo \"Label: $label\"\n    for file in \"${main_files[@]}\"; do\n        matches=$(grep -n \"ref{$label}\" \"$paper_dir/$file\" 2>/dev/null)\n        if [ ! -z \"$matches\" ]; then\n            found=1\n            echo \"  REFERENCED in $file:\"\n            echo \"$matches\" | while read line; do\n                line_num=$(echo \"$line\" | cut -d: -f1)\n                line_content=$(echo \"$line\" | cut -d: -f2-)\n                echo \"    Line $line_num: $line_content\"\n            done\n        fi\n    done\n    if [ $found -eq 0 ]; then\n        echo \"  NOT REFERENCED in main text (ORPHAN)\"\n    fi\n    echo \"\"\ndone\nENDSCRIPT\nbash /tmp/check_labels.sh\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e44b869-ad7b-47d2-8276-bf31317ecf3d",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2YZqW2VpMybWSjsSpW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6cbb692c-5d30-4702-b0be-82f56931236c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UnogKv6r96fqcWGxVEHQPA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 48770,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 48770,
          "cache_creation_input_tokens": 176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 176,
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

_source line 18 · 2026-05-25T09:11:01.323Z_

<details><summary>↩ Tool result · `toolu_01QgJ1Sup5qYXC37vpYbak99`</summary>

```text
=== APPENDIX LABEL REFERENCE AUDIT ===

Label: app:setup
  REFERENCED in method.tex:
    Line 68: Each RL condition uses seeds ${42,43,44}$ and identical training data (formulation alternatives in Appendix~ref{app:setup}).
  REFERENCED in experiments.tex:
    Line 55: Three controls constrain the multiplicative confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~ref{app:setup}).

Label: tab:hyperparams
  NOT REFERENCED in main text (ORPHAN)

Label: app:prooffol-construction
  REFERENCED in experiments.tex:
    Line 11: Cross-dataset experiments (Sref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${sim}$500 training examples constructed by translating ProofWriter~citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${sim}70%$ retention; Appendix~ref{app:prooffol-construction}); emph{stable convergence} denotes $overline{text{PR}}_{text{final,50}} > 0.90$.

Label: tab:prooffol-vs-folio
  NOT REFERENCED in main text (ORPHAN)

Label: app:extended-discussion
  REFERENCED in experiments.tex:
    Line 12: We report prove rate (PR), proved-only ISR ($text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{text{necessary}}$ distribution; Sref{sec:taxonomy-method}; classifier blind spots discussed in Appendix~ref{app:extended-discussion}), and a emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~ref{app:hacking-modes}).
  REFERENCED in limitations.tex:
    Line 6: ISR quantifies component necessity, not semantic faithfulness; its diagnostic value is realized through the mode breakdown, not the scalar alone (Appendix~ref{app:extended-discussion}).

Label: app:shapley
  REFERENCED in method.tex:
    Line 53: ISR computes the LOO marginal contribution, a restriction of the Shapley value to the maximal coalition (Appendix~ref{app:shapley}); full interaction detection would require $O(2^n)$ evaluations.

Label: app:premise-count
  REFERENCED in experiments.tex:
    Line 70: The premise-count-matched comparison yields only $1.06times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.

Label: tab:premise-bin-modes
  REFERENCED in experiments.tex:
    Line 73: In the modal premise-count range (4--6 premises, where most proved samples fall), TS reaches $19.7%$ under ISR versus $0%$ under random reward (Figure~ref{fig:premise-bins}; Table~ref{tab:premise-bin-modes}).

Label: tab:bootstrap-ci
  NOT REFERENCED in main text (ORPHAN)

Label: app:statistical-details
  REFERENCED in experiments.tex:
    Line 59: ISR reward amplifies TS convergence: $71%$ of proved samples under ISR exhibit tautological shortcuts vs. $14%$ under random (Appendix~ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
    Line 62: A seed-stratified $chi^2$ test confirms the overall mode distribution differs significantly between ISR and random conditions ($chi^2{=}174.8$, $text{df}{=}2$, $p{<}10^{-38}$; Appendix~ref{app:statistical-details}).

Label: app:hacking-modes
  REFERENCED in method.tex:
    Line 96: Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~ref{app:hacking-modes}), dominated by three: textbf{CE} (conclusion embedded among multiple premises), textbf{TS} (single-premise conclusion duplication; targets ISR directly since removing the sole premise forces $text{ISR}geq 0.5$), and textbf{PG} (premise-subset gaming: each component is LOO-necessary but the premise set is incomplete; Appendix~ref{app:h8}).
  REFERENCED in experiments.tex:
    Line 12: We report prove rate (PR), proved-only ISR ($text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{text{necessary}}$ distribution; Sref{sec:taxonomy-method}; classifier blind spots discussed in Appendix~ref{app:extended-discussion}), and a emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~ref{app:hacking-modes}).
    Line 128: Three modes account for the vast majority of hacking (Appendix Table~ref{tab:hacking-taxonomy}; Appendix~ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).

Label: tab:hacking-taxonomy
  REFERENCED in experiments.tex:
    Line 128: Three modes account for the vast majority of hacking (Appendix Table~ref{tab:hacking-taxonomy}; Appendix~ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).

Label: tab:hacking-taxonomy-app
  NOT REFERENCED in main text (ORPHAN)

Label: tab:classifier-precision
  NOT REFERENCED in main text (ORPHAN)

Label: app:h8
  REFERENCED in method.tex:
    Line 91: caption{Goodhart landscape across reward conditions. PR = prove rate; ISR$^*$ = proved-only ISR; TS = tautological shortcut; CE = conclusion embedding; N-H = non-hacking (upper bound on genuine reasoning). Multi-seed rows: pooled TS/CE/N-H; PR/ISR$^*$ as mean$pm$std. $^dagger$Seed~42 only. $^ddagger$Premise-count-matched (Sref{sec:goodhart}). $^P$FN-corrected (Sref{app:h8}). $^S$Seed-dependent (s43: 38.3%). Per-seed data: Table~ref{tab:fol-detailed}.}
    Line 96: Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~ref{app:hacking-modes}), dominated by three: textbf{CE} (conclusion embedded among multiple premises), textbf{TS} (single-premise conclusion duplication; targets ISR directly since removing the sole premise forces $text{ISR}geq 0.5$), and textbf{PG} (premise-subset gaming: each component is LOO-necessary but the premise set is incomplete; Appendix~ref{app:h8}).

Label: app:detailed-results
  REFERENCED in experiments.tex:
    Line 9: We train Qwen3-4B~citep{qwen3} with GRPO~citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds ${42,43,44}$ (ISR $beta{=}0.1$ extends to ${45,46}$; Appendix~ref{app:detailed-results}) on a fixed 500-example FOLIO~citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
    Line 10: Held-out evaluation uses 100 FOLIO examples with greedy decoding;footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${leq}7%$ non-hacking (Appendix~ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
    Line 38: Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${leq}6.2%$ non-hacking by 1000 steps (Table~ref{tab:fol-detailed}; Appendix~ref{app:detailed-results}).
    Line 65: ISR reward produces bimodal outcomes (Figure~ref{fig:seed-divergence}): 3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect can occur under standard training conditions (95% Clopper--Pearson CI: [11.8%, 88.1%]; $n{=}5$); 2 of 5 retain substantial genuine reasoning (seeds~45/46 added post-hoc to test replication; Appendix~ref{app:detailed-results}).

Label: tab:fol-detailed
  REFERENCED in method.tex:
    Line 91: caption{Goodhart landscape across reward conditions. PR = prove rate; ISR$^*$ = proved-only ISR; TS = tautological shortcut; CE = conclusion embedding; N-H = non-hacking (upper bound on genuine reasoning). Multi-seed rows: pooled TS/CE/N-H; PR/ISR$^*$ as mean$pm$std. $^dagger$Seed~42 only. $^ddagger$Premise-count-matched (Sref{sec:goodhart}). $^P$FN-corrected (Sref{app:h8}). $^S$Seed-dependent (s43: 38.3%). Per-seed data: Table~ref{tab:fol-detailed}.}
  REFERENCED in experiments.tex:
    Line 35: All three exec-only seeds converge to ${leq}6.2%$ non-hacking by 1000 steps (Table~ref{tab:fol-detailed}), confirming that structural degeneration under exec-only reward is not seed-specific among converged runs.
    Line 38: Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${leq}6.2%$ non-hacking by 1000 steps (Table~ref{tab:fol-detailed}; Appendix~ref{app:detailed-results}).
    Line 124: caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~ref{tab:fol-detailed}). ISR systematically selects for TS over CE without reducing total hacking; SFT shows near-zero hacking.}

Label: tab:fol-beta01-detailed
  NOT REFERENCED in main text (ORPHAN)

Label: tab:prolog-detailed
  REFERENCED in experiments.tex:
    Line 104: Under ISR-as-reward, all three seeds reach $0%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~ref{tab:prolog-detailed}).

Label: tab:prooffol-detailed
  REFERENCED in experiments.tex:
    Line 112: ISR reward on ProofFOL produces directionally higher genuine rates than exec-only ($p{=}0.10$, exploratory; Table~ref{tab:prooffol-detailed}).

Label: app:beta03
  REFERENCED in experiments.tex:
    Line 87: Higher doses accelerate collapse: $beta{=}0.2$ eliminates all non-hacking; $beta{=}0.3$ destabilizes training itself, producing multi-modal failure~citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44

Label: tab:beta03-detailed
  NOT REFERENCED in main text (ORPHAN)

Label: app:100step
  REFERENCED in experiments.tex:
    Line 45: Early-training comparison supports this interpretation: at 100 steps ($text{PR}{=}32%$), hacking already reaches $31%$ vs. SFT's $8%$ at comparable PR (Appendix~ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3

Label: app:o1-ablation
  REFERENCED in experiments.tex:
    Line 34: A binary variant testing only collective premise necessity misses the collapse entirely ($text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~ref{app:o1-ablation}).

Label: app:llama-coldstart
  REFERENCED in experiments.tex:
    Line 40: Two additional seeds under identical conditions fail to converge ($text{PR}{approx}14%$; Appendix~ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful convergence, though the confound between model capability and optimization success precludes strong causal attribution (Appendix~ref{app:llama-coldstart}).

Label: app:seed-convergence
  REFERENCED in experiments.tex:
    Line 40: Two additional seeds under identical conditions fail to converge ($text{PR}{approx}14%$; Appendix~ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful convergence, though the confound between model capability and optimization success precludes strong causal attribution (Appendix~ref{app:llama-coldstart}).
    Line 56: The shuffled-ISR control ($87%$ non-hacking at low PR) is consistent with the interpretation that Goodhart effects require sample-level ISR signal; however, the low PR (comparable to non-converging exec-only seeds; Appendix~ref{app:seed-convergence}) means that non-convergence alone cannot be ruled out as an alternative explanation.
  REFERENCED in conclusion.tex:
    Line 6: Convergence appears necessary for degeneration (Appendix~ref{app:seed-convergence}); for practitioners, structural diagnostics should be applied post-hoc, with the mode breakdown providing the reliable signal.

Label: app:n2-sensitivity
  REFERENCED in experiments.tex:
    Line 24: An $N{=}2$ sensitivity analysis excluding s43 confirms consistent or stronger patterns (Appendix~ref{app:n2-sensitivity}).
    Line 66: Excluding seed~43 (which uses nucleus sampling; Sref{sec:setup}), seed~44 shows $0%$ non-hacking and $100%$ TS at 500 steps; seed~42 retains $17%$ non-hacking at 500 steps but collapses to $2%$ by 1000 steps (full $N{=}2$ analysis: Appendix~ref{app:n2-sensitivity}).

Label: tab:n2-sensitivity
  NOT REFERENCED in main text (ORPHAN)

Label: app:8b-results
  REFERENCED in experiments.tex:
    Line 116: Qwen3-8B does not converge under exec-only GRPO ($text{PR}{=}14%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~ref{app:8b-results}).

Label: tab:8b-combined
  NOT REFERENCED in main text (ORPHAN)

Label: app:ai-assistants
  NOT REFERENCED in main text (ORPHAN)

Label: app:practical-guidelines
  REFERENCED in conclusion.tex:
    Line 4: STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect: structural proxies for formalization integrity are easier to observe than to optimize (Appendix~ref{app:practical-guidelines}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cbb692c-5d30-4702-b0be-82f56931236c",
  "isSidechain": true,
  "promptId": "b8001cdb-9b65-4f33-9ed1-b46347fe28b8",
  "agentId": "a5b7bc955cca621d0",
  "type": "user",
  "uuid": "3f72f7d0-fd00-4e6d-9e55-f717f02ac74a",
  "sourceToolAssistantUUID": "6cbb692c-5d30-4702-b0be-82f56931236c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-25T09:11:02.840Z_

Perfect! Now let me create a comprehensive summary based on this thorough search. Let me verify the checklist.tex references as well since that's part of the paper:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f72f7d0-fd00-4e6d-9e55-f717f02ac74a",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2Z6yzzficozsiEJUN6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8be6865a-7cd0-4238-a47a-e8c4b04e62ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011SPfN5DwiojZVVsroHydAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4901,
      "cache_read_input_tokens": 48946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4901,
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

_source line 20 · 2026-05-25T09:11:03.831Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014Y1ZpfuNiynrn7FoLtMx56`</summary>

```json
{
  "command": "grep -n \"ref{app:\\|ref{tab:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8be6865a-7cd0-4238-a47a-e8c4b04e62ae",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2Z6yzzficozsiEJUN6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6fbefb40-1470-4518-8824-489794ab686e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011SPfN5DwiojZVVsroHydAW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4901,
      "cache_read_input_tokens": 48946,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4901
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 147,
          "cache_read_input_tokens": 48946,
          "cache_creation_input_tokens": 4901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4901,
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

_source line 21 · 2026-05-25T09:11:03.903Z_

<details><summary>↩ Tool result · `toolu_014Y1ZpfuNiynrn7FoLtMx56`</summary>

```text
41:Yes. The model size (4B) is reported in \S\ref{sec:task}. Training details (GRPO $K{=}4$, 500/1000 steps, seeds, batch sizes) are in \S\ref{sec:task} and Appendix~\ref{app:setup}. Computing infrastructure and total GPU hours are reported in Appendix~\ref{app:setup}.
44:Yes. All hyperparameters are reported in \S\ref{sec:rewards} and Appendix~\ref{app:setup}. No hyperparameter search was performed; $\beta$ values were chosen for dose-response analysis.
47:Yes. We report mean$\pm$std across seeds (Table~\ref{tab:goodhart-landscape}), per-seed ranges, bootstrap confidence intervals (Appendix Table~\ref{tab:bootstrap-ci}), and discuss statistical power limitations (\S\ref{sec:limitations}).
50:Yes. We report Qwen3-4B model versions, Prover9, and SWI-Prolog. Training uses TRL 0.17.0, PyTorch 2.6.0, and Transformers 4.51.3; versions are listed in Appendix~\ref{app:setup}.
54:Minimal. Manual audit was conducted for classifier precision (50 random CE/TS samples verified; Appendix~\ref{app:hacking-modes}) and for PG false-negative correction (seed 42 only). No crowdsourced annotation was used.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fbefb40-1470-4518-8824-489794ab686e",
  "isSidechain": true,
  "promptId": "b8001cdb-9b65-4f33-9ed1-b46347fe28b8",
  "agentId": "a5b7bc955cca621d0",
  "type": "user",
  "uuid": "b7d69eae-4f95-4a33-9b01-7c24a4671d25",
  "sourceToolAssistantUUID": "6fbefb40-1470-4518-8824-489794ab686e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-25T09:11:17.014Z_

Excellent. Now I have a complete picture. Let me compile the final comprehensive report:

## APPENDIX LABEL REFERENCE AUDIT - COMPLETE RESULTS

Based on a thorough search of all main text files (abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, and limitations.tex), here is the complete status of all 32 appendix labels:

### REFERENCED LABELS (23 total)

1. **app:setup** - REFERENCED
   - method.tex:68: formulation alternatives
   - experiments.tex:55: additive variant discussion
   - checklist.tex:41,44,50: training details, hyperparameters, versions

2. **app:prooffol-construction** - REFERENCED
   - experiments.tex:11: ProofFOL corpus construction via GPT-4o and Prover9

3. **app:extended-discussion** - REFERENCED
   - experiments.tex:12: classifier blind spots
   - limitations.tex:6: semantic faithfulness vs. necessity

4. **app:shapley** - REFERENCED
   - method.tex:53: LOO as Shapley value restriction

5. **app:premise-count** - REFERENCED
   - experiments.tex:70: premise-count-matched comparison

6. **tab:premise-bin-modes** - REFERENCED
   - experiments.tex:73: TS rates across premise-count ranges

7. **app:statistical-details** - REFERENCED
   - experiments.tex:59: TS amplification rates
   - experiments.tex:62: chi-square test results

8. **app:hacking-modes** - REFERENCED
   - experiments.tex:12: classifier precision audit (152-sample)
   - method.tex:96: full mode definitions
   - experiments.tex:128: mode breakdown (CE, TS, PG)
   - checklist.tex:54: classifier precision verification

9. **tab:hacking-taxonomy** - REFERENCED
   - experiments.tex:128: cross-condition summary

10. **app:h8** - REFERENCED
    - method.tex:91: FN-corrected footnote in caption
    - method.tex:96: premise-subset gaming definition

11. **app:detailed-results** - REFERENCED
    - experiments.tex:9: seeds 45/46 extension
    - experiments.tex:10: excluding s43 analysis
    - experiments.tex:38: qualitative failure modes
    - experiments.tex:65: post-hoc replication seeds

12. **tab:fol-detailed** - REFERENCED
    - method.tex:91: per-seed data in caption
    - experiments.tex:35: exec-only convergence
    - experiments.tex:38: qualitative failure modes with table
    - experiments.tex:124: per-seed breakdown in caption

13. **tab:prolog-detailed** - REFERENCED
    - experiments.tex:104: three seeds distinct mechanisms under ISR

14. **tab:prooffol-detailed** - REFERENCED
    - experiments.tex:112: genuine rates comparison

15. **app:beta03** - REFERENCED
    - experiments.tex:87: beta=0.2 and beta=0.3 results

16. **app:100step** - REFERENCED
    - experiments.tex:45: early-training hacking comparison at 100 steps

17. **app:o1-ablation** - REFERENCED
    - experiments.tex:34: binary variant (collective premise necessity)

18. **app:llama-coldstart** - REFERENCED
    - experiments.tex:40: LLaMA-3.2-3B cold-start failure

19. **app:seed-convergence** - REFERENCED
    - experiments.tex:40: non-converging seeds analysis
    - experiments.tex:56: shuffled-ISR control discussion
    - conclusion.tex:6: convergence necessity

20. **app:n2-sensitivity** - REFERENCED
    - experiments.tex:24: N=2 sensitivity excluding s43
    - experiments.tex:66: full N=2 analysis

21. **app:8b-results** - REFERENCED
    - experiments.tex:116: Qwen3-8B non-convergence

22. **app:practical-guidelines** - REFERENCED
    - conclusion.tex:4: structural diagnostics post-hoc

### ORPHANED LABELS (9 total) - NOT REFERENCED IN MAIN TEXT

1. **tab:hyperparams** - ORPHAN (only defined in appendix.tex:13)
2. **tab:prooffol-vs-folio** - ORPHAN (only defined in appendix.tex:77)
3. **tab:bootstrap-ci** - ORPHAN (only defined in appendix.tex:154, mentioned in checklist.tex:47)
4. **tab:hacking-taxonomy-app** - ORPHAN (only defined in appendix.tex:272)
5. **tab:classifier-precision** - ORPHAN (only defined in appendix.tex:309)
6. **tab:fol-beta01-detailed** - ORPHAN (only defined in appendix.tex:558)
7. **tab:beta03-detailed** - ORPHAN (only defined in appendix.tex:715)
8. **tab:n2-sensitivity** - ORPHAN (only defined in appendix.tex:823)
9. **tab:8b-combined** - ORPHAN (only defined in appendix.tex:863)
10. **app:ai-assistants** - ORPHAN (only defined in appendix.tex:874)

### NOTE ON CHECKLIST.TEX
The checklist.tex file (which is typically author-provided metadata) does reference several appendix labels (app:setup, app:hacking-modes, tab:bootstrap-ci), but since your search request was specifically for the main body text files, these additional references have been noted but are separate from the core analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7d69eae-4f95-4a33-9b01-7c24a4671d25",
  "isSidechain": true,
  "agentId": "a5b7bc955cca621d0",
  "requestId": "req_011CbP2ZJ2GUQJQr1rMqowAW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d66456cb-15d1-4482-80ca-eb8c3114d962",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AwJvvUen8eZ1QosnhaHfv3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 518,
      "cache_read_input_tokens": 53847,
      "output_tokens": 1402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1402,
          "cache_read_input_tokens": 53847,
          "cache_creation_input_tokens": 518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 518,
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
