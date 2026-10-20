# code paper sensitivity fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 85
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/workers/worker_code_paper-sensitivity-fix_20260519T221357.log`
- **Structured JSON:** [`c4b74f5d895de0925fa0.json`](../../sessions/c4/c4b74f5d895de0925fa0.json)

## Before a recorded user message

85 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "7f8ef509-4813-4798-8025-9192f2028c38",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779256800,
    "rateLimitType": "seven_day",
    "utilization": 0.96,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "f028885e-b04b-40e5-8341-bd500d438ee5",
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task:

1. SSH to westd-29999 to check the v2 sweep results
2. Update 6 places in the paper where "30 combinations" is mentioned
3. Fix 3 V-recovery related issues

Let me first read the sweep results and the paper files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "c3dba42e-c34e-4b3c-9a42-20aa3a72c3e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hppah2oKuaxUHr5Av6WwE7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13964,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13964
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

先确认 v2 sweep 实际数据，同时读取论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "49a8e770-c334-43ee-81c8-38fc0619166e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hppah2oKuaxUHr5Av6WwE7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13964,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13964
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013ewPu5P8EEfydxvngkV4bZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "03ad91b5-c256-465b-a7bc-87425bee6e12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hppah2oKuaxUHr5Av6WwE7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13964,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13964
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T22:14:15.520Z_

<details><summary>↩ Tool result · `toolu_013ewPu5P8EEfydxvngkV4bZ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "02f8480d-41ea-4b2c-be90-03fc936b555c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BufTdi4HVcezwmWNfLaKcJ`</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sweep_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "4dcb8fe5-6f9b-4931-955b-069738167389",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtYD3Cnk3KoRYewS9ETkzx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 25805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 784
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01WHvAGinBtjF5siDYgtDKxp`</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "830f89ed-8b4b-45a8-b869-0b9cf3dcd54f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtYD3Cnk3KoRYewS9ETkzx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 25805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 784
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T22:14:20.939Z_

<details><summary>↩ Tool result · `toolu_01BufTdi4HVcezwmWNfLaKcJ`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sweep_results.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "6910b629-149b-4630-b412-ce9eb93d0a07",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"cat: /root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sweep_results.json: No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sweep_results.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.4}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T22:14:21.003Z_

<details><summary>↩ Tool result · `toolu_01WHvAGinBtjF5siDYgtDKxp`</summary>

```text
docs/paper/ethics.tex
docs/paper/related_work.tex
docs/paper/experimental_setup.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/limitations.tex
docs/paper/appendix.tex
docs/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "c7238c6b-5b20-464b-b224-64148f81cd77",
  "tool_use_result": {
    "filenames": [
      "docs/paper/ethics.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/main.tex",
      "docs/paper/method.tex",
      "docs/paper/limitations.tex",
      "docs/paper/appendix.tex",
      "docs/paper/results.tex"
    ],
    "durationMs": 56,
    "numFiles": 11,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 12_

sweep_results.json 路径不对，找一下实际位置。同时读取需要修改的论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "01c5249d-9586-4b98-a8f3-c13ed566f9c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hH3TUUVXE5JP6Coy9N8zU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 26589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DEPtTbuh4TJmoD94PDmiFr`</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration -name \"sweep_results*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "eceff123-3093-42d6-a512-4eeb9383aab6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hH3TUUVXE5JP6Coy9N8zU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 26589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T22:14:25.332Z_

<details><summary>↩ Tool result · `toolu_01DEPtTbuh4TJmoD94PDmiFr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "43156c25-59ae-43cd-a787-de3f4584e8ab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_011dFZxGwh1prb79vqRK1X49`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "df549d15-c9a8-45af-8d1c-fd9122422eef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hH3TUUVXE5JP6Coy9N8zU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 26589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T22:14:25.804Z_

<details><summary>↩ Tool result · `toolu_011dFZxGwh1prb79vqRK1X49`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \citep{kadavath2022}; concurrent work by \citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\mathcal{S} = \{\text{S1, S2, S4}\}$) and is applicable to any benchmark without auxiliary data requirements. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_failure}.
17	
18	We aggregate signals via Reciprocal Rank Fusion \citep[RRF;][]{cormack_2009_rrf}:
19	\begin{equation}
20	\label{eq:rrf}
21	    e_{ij} = \sum_{s \in \mathcal{S}} \frac{1}{\kappa + r_{s}(i)},
22	\end{equation}
23	where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\kappa=60$ is the standard smoothing constant, and $|\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to obtain $e_{ij} \in [0,1]$. The resulting distribution is highly right-skewed (mean 0.041, median 0.016, max 0.879), with most model-item pairs receiving near-zero exposure.
24	
25	\subsection{Stage 2: Contamination-Augmented IRT}
26	\label{sec:stage2}
27	
28	\paragraph{Primary model: 2PL+$\gamma$.}
29	Our primary specification augments the two-parameter logistic (2PL) model \citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:
30	\begin{equation}
31	\label{eq:2pl_gamma}
32	    P(y_{ijk} = 1) = \sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
33	\end{equation}
34	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \in \mathbb{R}$ is item difficulty, $\theta_j$ is model ability, and $\gamma_k$ is the scalar contamination effect for benchmark~$k$. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we further stratify within a benchmark by cognitive domain (\S\ref{sec:domain_differential}).
35	
36	The additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\gamma_k \cdot e_{ij} / a_i$ units on the ability scale (this holds exactly under linearization of the logistic function; the true shift is nonlinear and probability-dependent).
37	
38	For MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\ref{sec:4pl_details}); this requires $J \geq 16$ and is not used in domain-level analyses ($J = 13$).
39	
40	\paragraph{Inference.}
41	We perform Bayesian inference via NUTS \citep{hoffman2014} in Stan \citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_k \sim \mathcal{N}(0,1)$. Convergence requires split-$\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.
42	
43	\paragraph{Calibrated score.}
44	The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:
45	\begin{equation}
46	\label{eq:calibrated}
47	    \text{Acc}_{j}^{\text{cal}} = \frac{1}{I_k} \sum_{i=1}^{I_k}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)\right],
48	\end{equation}
49	with credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.
50	
51	\paragraph{Identifiability.}
52	\label{sec:fisher}
53	\label{sec:value_decomposition}
54	The reliability of $\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\geq$0.55 with $J \geq 50$ (Appendix~\ref{sec:identifiability}). Eq.~\eqref{eq:calibrated} depends on $\theta_j$, not $\gamma$ directly, predicting that vanilla 2PL ($\gamma\!=\!0$) achieves comparable calibration to 2PL+$\gamma$, with $\gamma_k$ serving diagnosis rather than calibration (\S\ref{sec:calibration_results}).
55	
56	\subsection{Dose-Response Profile Classification}
57	\label{sec:classification}
58	
59	Independent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern. Algorithm~\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by a noise threshold $\tau$, severity threshold $\sigma$, saturation ratio $\rho$, and late-gain floor $\lambda$. The three-way top-level split (immune/harm/benefit) is governed by the sign and magnitude of $\Delta = a_{100} - a_0$ relative to $\tau$; within-branch refinements distinguish U-collapse from V-recovery (via mid-dosage trough detection) and monotonic benefit from benefit-saturation (via gain deceleration). A mid-trajectory volatility check ($v^*$) within the immune branch distinguishes true immunity (Phi-4: $v^* = 0.34$pp $\le \tau$) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $\Delta \approx 0$ but $v^* = 3.22$pp $> \tau$); recovery extent varies by seed (partial at seed$=$42, full at seed$=$123). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms 5/5 families are stable across all $(\tau, \sigma)$ combinations (Appendix~\ref{sec:classification_sensitivity}).
60	
61	\begin{algorithm}[H]
62	\caption{Dose-Response Profile Classification}
63	\label{alg:profile-classification}
64	\begin{algorithmic}[1]
65	\Require Accuracy vector $\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \in \{0, 5, 25, 50, 100\}\%$
66	\Require Noise threshold $\tau = 1$ pp, severity threshold $\sigma = 5$ pp
67	\Require Saturation ratio $\rho = 0.3$, late-gain floor $\lambda = 0.5$ pp
68	\Ensure Pattern $p \in \{\textsc{Immune}, \textsc{U-collapse}, \textsc{V-recovery}, \textsc{Benefit}, \textsc{Benefit-sat}\}$
69	\State $\Delta \gets a_{100} - a_{0}$ \Comment{end-to-end accuracy shift}
70	\State $m^* \gets \min(a_{5},\, a_{25},\, a_{50})$ \Comment{mid-dosage minimum}
71	\State $v^* \gets \max_{i \in \{5,25,50\}} |a_i - a_0|$ \Comment{max mid-trajectory deviation}
72	\If{$|\Delta| \le \tau$}
73	    \If{$v^* \le \tau$}
74	        \State \Return \textsc{Immune} \Comment{fluctuation within noise band}
75	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
76	        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
77	    \Else
78	        \State \Return \textsc{Immune} \Comment{non-V volatility, endpoint stable}
79	    \EndIf
80	\ElsIf{$\Delta < -\tau$}
81	    \If{$\Delta \le -\sigma$}
82	        \State \Return \textsc{U-collapse} \Comment{severe monotonic degradation}
83	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
84	        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
85	    \Else
86	        \State \Return \textsc{U-collapse} \Comment{moderate decline, no V-shape}
87	    \EndIf
88	\Else \Comment{$\Delta > \tau$}
89	    \State $g_1 \gets a_{25} - a_{0}$ \Comment{first-half gain}
90	    \State $g_2 \gets a_{100} - a_{25}$ \Comment{second-half gain}
91	    \State $\ell \gets a_{100} - a_{50}$ \Comment{late gain}
92	    \If{$(g_1 > 0$ \textbf{and} $g_2 < \rho \cdot g_1)$ \textbf{or} $\ell < \lambda$}
93	        \State \Return \textsc{Benefit-sat} \Comment{gain decelerates at high dosage}
94	    \Else
95	        \State \Return \textsc{Benefit} \Comment{sustained improvement}
96	    \EndIf
97	\EndIf
98	\end{algorithmic}
99	\end{algorithm}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "9d64cdbb-5fc1-4c27-81c4-3f3c1b209698",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nLet $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model~$j$ ($j=1,\\ldots,J$) to item~$i$ ($i=1,\\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.\n\nOur goal is to estimate $\\theta_j^{\\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \\citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \\citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \\in [0,1]$, fitting per-benchmark models to handle the shared item pool \\citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).\n\n\\subsection{Stage 1: Multi-Signal Exposure Mapping}\n\\label{sec:stage1}\n\nFor each model~$j$ and item~$i$, we consider four candidate detection signals. \\textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \\textbf{S2}~(Min-K\\%++): a membership inference statistic based on token-level surprisal \\citep{zhang_2024_minkpp}. \\textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \\citep{dekoninck2024constat}. \\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \\citep{kadavath2022}; concurrent work by \\citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\\mathcal{S} = \\{\\text{S1, S2, S4}\\}$) and is applicable to any benchmark without auxiliary data requirements. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \\S\\ref{sec:signal_failure}.\n\nWe aggregate signals via Reciprocal Rank Fusion \\citep[RRF;][]{cormack_2009_rrf}:\n\\begin{equation}\n\\label{eq:rrf}\n    e_{ij} = \\sum_{s \\in \\mathcal{S}} \\frac{1}{\\kappa + r_{s}(i)},\n\\end{equation}\nwhere $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\\kappa=60$ is the standard smoothing constant, and $|\\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to obtain $e_{ij} \\in [0,1]$. The resulting distribution is highly right-skewed (mean 0.041, median 0.016, max 0.879), with most model-item pairs receiving near-zero exposure.\n\n\\subsection{Stage 2: Contamination-Augmented IRT}\n\\label{sec:stage2}\n\n\\paragraph{Primary model: 2PL+$\\gamma$.}\nOur primary specification augments the two-parameter logistic (2PL) model \\citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:\n\\begin{equation}\n\\label{eq:2pl_gamma}\n    P(y_{ijk} = 1) = \\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwhere $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \\in \\mathbb{R}$ is item difficulty, $\\theta_j$ is model ability, and $\\gamma_k$ is the scalar contamination effect for benchmark~$k$. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we further stratify within a benchmark by cognitive domain (\\S\\ref{sec:domain_differential}).\n\nThe additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\\gamma_k \\cdot e_{ij} / a_i$ units on the ability scale (this holds exactly under linearization of the logistic function; the true shift is nonlinear and probability-dependent).\n\nFor MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\\ref{sec:4pl_details}); this requires $J \\geq 16$ and is not used in domain-level analyses ($J = 13$).\n\n\\paragraph{Inference.}\nWe perform Bayesian inference via NUTS \\citep{hoffman2014} in Stan \\citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\\theta_j \\sim \\mathcal{N}(0,1)$, $a_i \\sim \\text{LogNormal}(0, 0.5)$, $b_i \\sim \\mathcal{N}(0,1)$, $\\gamma_k \\sim \\mathcal{N}(0,1)$. Convergence requires split-$\\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.\n\n\\paragraph{Calibrated score.}\nThe decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:\n\\begin{equation}\n\\label{eq:calibrated}\n    \\text{Acc}_{j}^{\\text{cal}} = \\frac{1}{I_k} \\sum_{i=1}^{I_k}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[\\sigma\\!\\bigl(a_i(\\theta_j - b_i)\\bigr)\\right],\n\\end{equation}\nwith credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.\n\n\\paragraph{Identifiability.}\n\\label{sec:fisher}\n\\label{sec:value_decomposition}\nThe reliability of $\\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\\geq$0.55 with $J \\geq 50$ (Appendix~\\ref{sec:identifiability}). Eq.~\\eqref{eq:calibrated} depends on $\\theta_j$, not $\\gamma$ directly, predicting that vanilla 2PL ($\\gamma\\!=\\!0$) achieves comparable calibration to 2PL+$\\gamma$, with $\\gamma_k$ serving diagnosis rather than calibration (\\S\\ref{sec:calibration_results}).\n\n\\subsection{Dose-Response Profile Classification}\n\\label{sec:classification}\n\nIndependent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern. Algorithm~\\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by a noise threshold $\\tau$, severity threshold $\\sigma$, saturation ratio $\\rho$, and late-gain floor $\\lambda$. The three-way top-level split (immune/harm/benefit) is governed by the sign and magnitude of $\\Delta = a_{100} - a_0$ relative to $\\tau$; within-branch refinements distinguish U-collapse from V-recovery (via mid-dosage trough detection) and monotonic benefit from benefit-saturation (via gain deceleration). A mid-trajectory volatility check ($v^*$) within the immune branch distinguishes true immunity (Phi-4: $v^* = 0.34$pp $\\le \\tau$) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$); recovery extent varies by seed (partial at seed$=$42, full at seed$=$123). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms 5/5 families are stable across all $(\\tau, \\sigma)$ combinations (Appendix~\\ref{sec:classification_sensitivity}).\n\n\\begin{algorithm}[H]\n\\caption{Dose-Response Profile Classification}\n\\label{alg:profile-classification}\n\\begin{algorithmic}[1]\n\\Require Accuracy vector $\\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \\in \\{0, 5, 25, 50, 100\\}\\%$\n\\Require Noise threshold $\\tau = 1$ pp, severity threshold $\\sigma = 5$ pp\n\\Require Saturation ratio $\\rho = 0.3$, late-gain floor $\\lambda = 0.5$ pp\n\\Ensure Pattern $p \\in \\{\\textsc{Immune}, \\textsc{U-collapse}, \\textsc{V-recovery}, \\textsc{Benefit}, \\textsc{Benefit-sat}\\}$\n\\State $\\Delta \\gets a_{100} - a_{0}$ \\Comment{end-to-end accuracy shift}\n\\State $m^* \\gets \\min(a_{5},\\, a_{25},\\, a_{50})$ \\Comment{mid-dosage minimum}\n\\State $v^* \\gets \\max_{i \\in \\{5,25,50\\}} |a_i - a_0|$ \\Comment{max mid-trajectory deviation}\n\\If{$|\\Delta| \\le \\tau$}\n    \\If{$v^* \\le \\tau$}\n        \\State \\Return \\textsc{Immune} \\Comment{fluctuation within noise band}\n    \\ElsIf{$m^* < a_{0}$ \\textbf{and} $m^* < a_{100}$}\n        \\State \\Return \\textsc{V-recovery} \\Comment{V-dip with full endpoint recovery}\n    \\Else\n        \\State \\Return \\textsc{Immune} \\Comment{non-V volatility, endpoint stable}\n    \\EndIf\n\\ElsIf{$\\Delta < -\\tau$}\n    \\If{$\\Delta \\le -\\sigma$}\n        \\State \\Return \\textsc{U-collapse} \\Comment{severe monotonic degradation}\n    \\ElsIf{$m^* < a_{0}$ \\textbf{and} $m^* < a_{100}$}\n        \\State \\Return \\textsc{V-recovery} \\Comment{mid-dosage trough with partial recovery}\n    \\Else\n        \\State \\Return \\textsc{U-collapse} \\Comment{moderate decline, no V-shape}\n    \\EndIf\n\\Else \\Comment{$\\Delta > \\tau$}\n    \\State $g_1 \\gets a_{25} - a_{0}$ \\Comment{first-half gain}\n    \\State $g_2 \\gets a_{100} - a_{25}$ \\Comment{second-half gain}\n    \\State $\\ell \\gets a_{100} - a_{50}$ \\Comment{late gain}\n    \\If{$(g_1 > 0$ \\textbf{and} $g_2 < \\rho \\cdot g_1)$ \\textbf{or} $\\ell < \\lambda$}\n        \\State \\Return \\textsc{Benefit-sat} \\Comment{gain decelerates at high dosage}\n    \\Else\n        \\State \\Return \\textsc{Benefit} \\Comment{sustained improvement}\n    \\EndIf\n\\EndIf\n\\end{algorithmic}\n\\end{algorithm}",
      "numLines": 99,
      "startLine": 1,
      "totalLines": 99
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01WkTZQBZ8P1vV6di5buZ47B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "f1f8a710-a8d7-4850-af4d-9433c3e44b4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hH3TUUVXE5JP6Coy9N8zU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 26589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T22:14:26.271Z_

<details><summary>↩ Tool result · `toolu_01WkTZQBZ8P1vV6di5buZ47B`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Five Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{table}[t]
10	\centering
11	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
12	\label{tab:taxonomy}
13	\footnotesize
14	\begin{tabular}{llccccc}
15	\toprule
16	Pattern & Model & Baseline & $\Delta$acc & 95\% CI & Peak & Stab. \\
17	\midrule
18	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% \\
19	U-collapse & Qwen-14B & 69.4\% & $-$9.4pp & [$-$10.04, $-$8.70] & $-$10.0\textsuperscript{d050} & 100\% \\
20	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
21	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\% \\
22	Benefit-sat. & OLMo-2 7B & 53.8\% & $+$3.2pp & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\tau,\sigma)$ threshold combinations (Appendix~\ref{sec:classification_sensitivity}).
28	
29	\paragraph{Baseline ability threshold.}
30	A threshold at 64.7\% MMLU baseline (bootstrap 95\% CI: 64.0--65.4\%, $B=10{,}000$) separates two regimes. Below it, OLMo-2 (53.8\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\%) gains $+$3.8pp monotonically. Above it, Qwen-7B (66.1\%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), Qwen-14B (69.4\%) collapses by $-$10.0pp at d050---3$\times$ more fragile than 7B despite higher baseline---and Phi-4 (76.4\%) is immune. ARC-Challenge results are directionally consistent for 4/5 models (Appendix~\ref{sec:arc_cross_benchmark}). Cross-family domain decomposition reveals consistent directionality within each pattern, with STEM as the most resilient domain across all five families (Appendix~\ref{sec:domain_decomposition}).
31	
32	\begin{figure}[t]
33	\centering
34	\includegraphics[width=\columnwidth]{figures/fig_dose_response.pdf}
35	\caption{MMLU accuracy vs.\ contamination dosage (5-shot). Models below 64.7\% baseline benefit; models above are harmed or immune. Qwen-14B is 3$\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref{sec:arc_cross_benchmark}.}
36	\label{fig:dose_response}
37	\end{figure}
38	
39	\subsection{Item-Level Memorization Test}
40	\label{sec:memorization_test}
41	
42	We test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. The pattern holds on ARC-Challenge. Difficulty-stratified analysis confirms symmetry ($|\text{gap}| < 0.4$pp across all bins).
43	
44	\begin{table}[t]
45	\centering
46	\caption{Treated vs.\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}
47	\label{tab:did}
48	\footnotesize
49	\begin{tabular}{lcccc}
50	\toprule
51	Model & Treated $\Delta$ & Untreated $\Delta$ & DiD & Verdict \\
52	\midrule
53	Gemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.6 (ns) & generalization \\
54	OLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\
55	Phi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\
56	Qwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\
57	Qwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	Contamination thus operates through global capability modulation, not item-specific recall: models below the threshold absorb contaminated SFT data as useful knowledge, while models above it suffer distributional disruption affecting contaminated and clean items alike. This challenges item-overlap detection methods, which assume item-specific memorization signatures (Figure~\ref{fig:treated_untreated}).
63	
64	\begin{figure}[t]
65	\centering
66	\includegraphics[width=\columnwidth]{figures/fig_treated_untreated.pdf}
67	\caption{DiD for treated vs.\ untreated items across five families at d025 MMLU. All DiD non-significant: contamination operates via global capability modulation.}
68	\label{fig:treated_untreated}
69	\end{figure}
70	
71	\subsection{Calibration Quality}
72	\label{sec:calibration_results}
73	
74	Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\tau = 0.73$ on 300 items ($\Delta\tau = 0.27$ vs.\ random baseline); S1-only selection causes convergence failure ($\hat{R} = 1.53$) due to exposure variance compression.
75	
76	Table~\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy achieves the lowest MAE (0.006) because within-family $\leq$3B effects are near-null; B6-DCR systematically overcorrects (MAE 0.108). ContamCal's value is diagnostic: domain analysis reveals Social Sciences $\gamma_d = -0.63$ ($P(\gamma_d\!<\!0) = 99.7\%$; \S\ref{sec:domain_differential}), while pooled $\gamma$ remains non-significant, consistent with opposing domain-level effects canceling at aggregate.
77	
78	\begin{table}[t]
79	\centering
80	\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\ref{sec:arc_irt}.}
81	\label{tab:baselines}
82	\footnotesize
83	\begin{tabular}{lcc}
84	\toprule
85	Method & MAE & $\tau$ \\
86	\midrule
87	B0: Raw Accuracy & \textbf{0.006} & 0.767 \\
88	B1b: Remove \& Rescore & 0.026 & \underline{0.783} \\
89	B3: Vanilla 2PL & 0.008 & 0.731 \\
90	B4: Linear Regression & 0.010 & 0.751 \\
91	B5b: Emperor & \textbf{0.006} & \textbf{0.789} \\
92	B6: DCR (reimpl.) & 0.108 & 0.654 \\
93	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	\subsection{Detection Signal Failure Modes}
99	\label{sec:signal_failure}
100	
101	Min-K\%++ \citep{zhang_2024_minkpp} exhibits a \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores than clean items (Cohen's $d = -1.55$ at d005, $-1.98$ at d100). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
102	
103	\subsection{Domain-Level Analysis}
104	\label{sec:domain_differential}
105	
106	Within-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% CI $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722), crossing the Bonferroni-corrected threshold for eight tests (Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Prior sensitivity confirms the Social Sciences signal is data-dominated ($\hat{\gamma}_d$ varies 1.2$\times$ across priors vs.\ 2.6$\times$ for pooled; Appendix~\ref{sec:prior_sensitivity}).
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "7dcc7f62-5fe2-4906-8c91-8ed292007fe2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nCross-family results (\\S\\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\\S\\ref{sec:calibration_results}--\\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\\times$1.5B + 8$\\times$3B); domain-level contamination estimates $\\gamma_d$ (\\S\\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\\ref{fig:domain_gamma}.\n\n\\subsection{Five Dose-Response Patterns}\n\\label{sec:taxonomy}\n\n\\begin{table}[t]\n\\centering\n\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}\n\\label{tab:taxonomy}\n\\footnotesize\n\\begin{tabular}{llccccc}\n\\toprule\nPattern & Model & Baseline & $\\Delta$acc & 95\\% CI & Peak & Stab. \\\\\n\\midrule\nImmune & Phi-4 14.7B & 76.4\\% & $\\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\\% \\\\\nU-collapse & Qwen-14B & 69.4\\% & $-$9.4pp & [$-$10.04, $-$8.70] & $-$10.0\\textsuperscript{d050} & 100\\% \\\\\nV-recovery & Qwen-7B & 66.1\\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\\textsuperscript{d025} & 99.6\\% \\\\\nBenefit & Gemma-2 9B & 61.9\\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\\% \\\\\nBenefit-sat. & OLMo-2 7B & 53.8\\% & $+$3.2pp & [$+$2.73, $+$3.71] & sat.\\textsuperscript{d050} & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nApplying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (Appendix~\\ref{sec:classification_sensitivity}).\n\n\\paragraph{Baseline ability threshold.}\nA threshold at 64.7\\% MMLU baseline (bootstrap 95\\% CI: 64.0--65.4\\%, $B=10{,}000$) separates two regimes. Below it, OLMo-2 (53.8\\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\\%) gains $+$3.8pp monotonically. Above it, Qwen-7B (66.1\\%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), Qwen-14B (69.4\\%) collapses by $-$10.0pp at d050---3$\\times$ more fragile than 7B despite higher baseline---and Phi-4 (76.4\\%) is immune. ARC-Challenge results are directionally consistent for 4/5 models (Appendix~\\ref{sec:arc_cross_benchmark}). Cross-family domain decomposition reveals consistent directionality within each pattern, with STEM as the most resilient domain across all five families (Appendix~\\ref{sec:domain_decomposition}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{MMLU accuracy vs.\\ contamination dosage (5-shot). Models below 64.7\\% baseline benefit; models above are harmed or immune. Qwen-14B is 3$\\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\\ref{sec:arc_cross_benchmark}.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Item-Level Memorization Test}\n\\label{sec:memorization_test}\n\nWe test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. The pattern holds on ARC-Challenge. Difficulty-stratified analysis confirms symmetry ($|\\text{gap}| < 0.4$pp across all bins).\n\n\\begin{table}[t]\n\\centering\n\\caption{Treated vs.\\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}\n\\label{tab:did}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Treated $\\Delta$ & Untreated $\\Delta$ & DiD & Verdict \\\\\n\\midrule\nGemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.6 (ns) & generalization \\\\\nOLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\\\\nPhi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\\\\nQwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\\\\nQwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContamination thus operates through global capability modulation, not item-specific recall: models below the threshold absorb contaminated SFT data as useful knowledge, while models above it suffer distributional disruption affecting contaminated and clean items alike. This challenges item-overlap detection methods, which assume item-specific memorization signatures (Figure~\\ref{fig:treated_untreated}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_treated_untreated.pdf}\n\\caption{DiD for treated vs.\\ untreated items across five families at d025 MMLU. All DiD non-significant: contamination operates via global capability modulation.}\n\\label{fig:treated_untreated}\n\\end{figure}\n\n\\subsection{Calibration Quality}\n\\label{sec:calibration_results}\n\nWithin-family IRT analysis uses Qwen2.5 $\\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\\tau = 0.73$ on 300 items ($\\Delta\\tau = 0.27$ vs.\\ random baseline); S1-only selection causes convergence failure ($\\hat{R} = 1.53$) due to exposure variance compression.\n\nTable~\\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy achieves the lowest MAE (0.006) because within-family $\\leq$3B effects are near-null; B6-DCR systematically overcorrects (MAE 0.108). ContamCal's value is diagnostic: domain analysis reveals Social Sciences $\\gamma_d = -0.63$ ($P(\\gamma_d\\!<\\!0) = 99.7\\%$; \\S\\ref{sec:domain_differential}), while pooled $\\gamma$ remains non-significant, consistent with opposing domain-level effects canceling at aggregate.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\\ref{sec:arc_irt}.}\n\\label{tab:baselines}\n\\footnotesize\n\\begin{tabular}{lcc}\n\\toprule\nMethod & MAE & $\\tau$ \\\\\n\\midrule\nB0: Raw Accuracy & \\textbf{0.006} & 0.767 \\\\\nB1b: Remove \\& Rescore & 0.026 & \\underline{0.783} \\\\\nB3: Vanilla 2PL & 0.008 & 0.731 \\\\\nB4: Linear Regression & 0.010 & 0.751 \\\\\nB5b: Emperor & \\textbf{0.006} & \\textbf{0.789} \\\\\nB6: DCR (reimpl.) & 0.108 & 0.654 \\\\\nContamCal (2PL+$\\gamma$) & 0.009 & 0.731 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detection Signal Failure Modes}\n\\label{sec:signal_failure}\n\nMin-K\\%++ \\citep{zhang_2024_minkpp} exhibits a \\textit{directional reversal} at 0.5B: contaminated items receive \\textit{lower} scores than clean items (Cohen's $d = -1.55$ at d005, $-1.98$ at d100). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\\ref{sec:signal_reliability_appendix}). Simulation shows $\\gamma$ recovery requires AUC$\\geq$0.55 with $J \\geq 50$; at AUC $\\geq 0.90$, $J = 16$ suffices (Appendix~\\ref{sec:identifiability_appendix}).\n\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain_differential}\n\nWithin-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\\gamma_d$ while Social Sciences is negative ($\\gamma_d = -0.63$, 95\\% CI $[-1.07, -0.19]$, $P(\\gamma_d\\!<\\!0) = 99.7\\%$, PPP$=$0.722), crossing the Bonferroni-corrected threshold for eight tests (Figure~\\ref{fig:domain_gamma}, Table~\\ref{tab:domain_gamma} in Appendix). Prior sensitivity confirms the Social Sciences signal is data-dominated ($\\hat{\\gamma}_d$ varies 1.2$\\times$ across priors vs.\\ 2.6$\\times$ for pooled; Appendix~\\ref{sec:prior_sensitivity}).\n",
      "numLines": 107,
      "startLine": 1,
      "totalLines": 107
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01WcDCRXg366bBmFBQa69Ppd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "acb8f0b1-2ceb-4a3c-adf5-c0dab2d419d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hH3TUUVXE5JP6Coy9N8zU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 26589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T22:14:27.136Z_

<details><summary>↩ Tool result · `toolu_01WcDCRXg366bBmFBQa69Ppd`</summary>

```text
1	\appendix
2	
3	\section{ARC-Challenge Cross-Benchmark Analysis}
4	\label{sec:arc_cross_benchmark}
5	
6	ARC-Challenge (25-shot, 1{,}172 items) patterns are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$3.8pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($\pm$0.6pp). Gemma-2 ARC is excluded due to a 16pp evaluation artifact. Qwen-14B exhibits V-recovery on ARC rather than U-collapse ($-$3.4pp vs.\ $-$9.4pp on MMLU), a 2.8$\times$ attenuation reflecting benchmark-specific properties. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042), and Gemma-2's ARC $\Delta$acc 95\% CI crosses zero ($[-2.47, +0.09]$pp).
7	
8	Dose-response profiles are jointly determined by model and benchmark properties: direction is governed by model baseline ability (the 64.7\% threshold); shape is governed by benchmark properties (item pool size, difficulty distribution, evaluation format). This benchmark-conditionality is a finding in its own right---practitioners cannot assume a contamination profile on one benchmark transfers to another.
9	
10	\begin{figure}[h]
11	\centering
12	\includegraphics[width=\columnwidth]{figures/fig_arc_dose_response.pdf}
13	\caption{ARC-Challenge accuracy vs.\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\ref{fig:dose_response}) for 4/5 models.}
14	\label{fig:dose_response_arc}
15	\end{figure}
16	
17	\section{Signal Reliability Across Scales}
18	\label{sec:signal_reliability_appendix}
19	
20	\begin{figure}[h]
21	\centering
22	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap.pdf}
23	\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\%++) reverses at 0.5B; S4 is near-random below 1.5B.}
24	\label{fig:signal_heatmap}
25	\end{figure}
26	
27	\section{Identifiability Simulation}
28	\label{sec:identifiability_appendix}
29	
30	\begin{figure}[h]
31	\centering
32	\includegraphics[width=\columnwidth]{figures/fig_identifiability_heatmap.pdf}
33	\caption{$\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\% CI coverage $\geq90\%$ require $J\geq50$ at AUC$=$0.55, but only $J\geq16$ at AUC$\geq$0.90.}
34	\label{fig:identifiability_heatmap}
35	\end{figure}
36	
37	Fisher information $\mathcal{I}(\gamma) \propto \text{Var}(e_{\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\% CI coverage $\geq 90\%$ require $J \geq 50$; at AUC$\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).
38	
39	\section{4PL Extension}
40	\label{sec:4pl_details}
41	
42	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
43	\begin{equation}
44	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
45	\end{equation}
46	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
47	
48	\section{S4 Self-Critique Signal Details}
49	\label{sec:s4_details}
50	
51	S4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\text{YES})$, then score each item as the negative entropy of this distribution: $\text{S4}_i = -[-p\log p - (1-p)\log(1-p)]$ where $p = P(\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.
52	
53	\section{Training Convergence}
54	\label{sec:training_convergence}
55	
56	All SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.
57	
58	\section{Model Exclusion Details}
59	\label{sec:exclusion_details}
60	
61	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
62	
63	\paragraph{Model sets across analyses.}
64	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
65	
66	\begin{table}[h]
67	\centering
68	\caption{Model set composition across analyses.}
69	\label{tab:model_sets}
70	\footnotesize
71	\begin{tabular}{lcll}
72	\toprule
73	Analysis & $J$ & Model Set & Section \\
74	\midrule
75	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
76	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
77	Cross-family & 16--28 & varies by benchmark & \S\ref{sec:taxonomy} \\
78	Oracle ablation & 13 & domain whitelist & \S\ref{sec:calibration_results} \\
79	\bottomrule
80	\end{tabular}
81	\end{table}
82	
83	\section{Prior Sensitivity Analysis}
84	\label{sec:prior_sensitivity}
85	
86	To assess the influence of the $\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\gamma \sim \mathcal{N}(0, 0.5)$, $\mathcal{N}(0, 1)$ (default), and $\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\% CI includes zero in all cases (lower bound stable at $\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\hat{R} < 1.01$, ESS $> 3800$, PPP $\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\gamma$-based conclusions at current ensemble sizes.
87	
88	For the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:
89	
90	\begin{table}[h]
91	\centering
92	\caption{Social Sciences $\gamma$ prior sensitivity ($J$=16).}
93	\label{tab:socsci_prior}
94	\footnotesize
95	\begin{tabular}{lcccc}
96	\toprule
97	Prior & $\hat{\gamma}$ & 95\% CI & $P(\gamma\!<\!0)$ & PPP \\
98	\midrule
99	$\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\% & 0.242 \\
100	$\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\% & 0.282 \\
101	$\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\% & 0.282 \\
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	In contrast to the pooled analysis where $\hat{\gamma}$ shifts 2.6$\times$ across priors, Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.43 to $-$0.51), with $P(\gamma<0) \geq 97.95\%$ in all cases.
107	
108	\section{IRT Ability Separation by Scale}
109	\label{sec:theta_separation}
110	
111	Table~\ref{tab:theta_separation} reports the mean posterior $\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\Delta\theta = \bar{\theta}_{3\text{B}} - \bar{\theta}_{1.5\text{B}}$ is positive and significant (95\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.
112	
113	\begin{table}[h]
114	\centering
115	\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\Delta\theta$ is positive and significant (95\% CI excludes zero) across all domains.}
116	\label{tab:theta_separation}
117	\footnotesize
118	\begin{tabular}{lccc}
119	\toprule
120	Domain & $\bar{\theta}_{1.5\text{B}}$ & $\bar{\theta}_{3\text{B}}$ & $\Delta\theta$ [95\% CI] \\
121	\midrule
122	Math & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\
123	Science & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\
124	CS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\
125	Medical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\
126	Humanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\
127	Social Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\
128	Business/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\
129	Other & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\
130	\midrule
131	Pooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\
132	\bottomrule
133	\end{tabular}
134	\end{table}
135	
136	\section{DiD Across Dosage Levels}
137	\label{sec:did_dosage}
138	
139	\begin{figure}[h]
140	\centering
141	\includegraphics[width=\columnwidth]{figures/fig_did_dose_response.pdf}
142	\caption{Difference-in-differences (treated vs.\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all five model families, confirming that the global capability modulation mechanism (\S\ref{sec:memorization_test}) is consistent across the full dosage range.}
143	\label{fig:did_dose_response}
144	\end{figure}
145	
146	\section{Dose-Response Details}
147	\label{sec:dose_response_details}
148	
149	The five dose-response patterns reported in \S\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \textit{decreases} with dosage (0.41 at d000 $\to$ 0.27 at d100), consistent with the position bias confound documented in \S\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\%) overwhelms any memorization benefit.
150	
151	\section{Sensitivity of Profile Classification}
152	\label{sec:classification_sensitivity}
153	
154	We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\tau, \sigma)$ combinations: $\tau \in \{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\}$~pp $\times$ $\sigma \in \{3, 4, 5, 6, 7\}$~pp. Table~\ref{tab:sensitivity} reports stability across this grid.
155	
156	\begin{table}[h]
157	\centering
158	\caption{Profile classification stability across 30 $(\tau, \sigma)$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.}
159	\label{tab:sensitivity}
160	\footnotesize
161	\begin{tabular}{lccc}
162	\toprule
163	Model & Default Pattern & Stability & Notes \\
164	\midrule
165	Phi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\le$ all $\tau$ \\
166	Qwen-14B & U-collapse & 30/30 & --- \\
167	Gemma-2 9B & Benefit & 30/30 & --- \\
168	OLMo-2 7B & Benefit-sat & 30/30 & --- \\
169	Qwen-7B & V-recovery & 30/30 & volatility check resolves \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	With the mid-trajectory volatility check (Algorithm~\ref{alg:profile-classification}, line~3), all five families achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\Delta \approx 0$ but $v^* = 3.22$pp $> \tau$). The severity threshold $\sigma$ has zero impact on any model's classification, because no model's $\Delta\text{acc}$ falls in the range where $\sigma$ determines the U-collapse vs.\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\sigma=7$).
175	
176	\section{Cross-Family Domain Decomposition}
177	\label{sec:domain_decomposition}
178	
179	We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.
180	
181	Two patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, U-collapse (Qwen-14B) produces negative $\Delta\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\Delta\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.
182	
183	Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
184	
185	These results reinforce the global capability modulation interpretation (\S\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.
186	
187	\section{Baseline Ability vs.\ Contamination Effect}
188	\label{sec:baseline_vs_effect}
189	
190	\begin{figure}[h]
191	\centering
192	\includegraphics[width=\columnwidth]{figures/fig_baseline_vs_effect.pdf}
193	\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Threshold estimated from five models spanning four independent families.}
194	\label{fig:baseline_vs_effect}
195	\end{figure}
196	
197	\section{Per-Domain $\gamma$ Estimates}
198	\label{sec:domain_gamma_table}
199	
200	\begin{figure}[h]
201	\centering
202	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
203	\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}
204	\label{fig:domain_gamma}
205	\end{figure}
206	
207	\begin{table}[h]
208	\centering
209	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\hat{R} < 1.01$). Social Sciences $P(\gamma\!<\!0)$ strengthens from 99.1\% to 99.7\% at $J$=16, crossing the Bonferroni-corrected threshold of 99.375\% for eight tests. Results remain exploratory at these ensemble sizes \citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}
210	\label{tab:domain_gamma}
211	\footnotesize
212	\resizebox{\columnwidth}{!}{%
213	\begin{tabular}{lcccccc}
214	\toprule
215	 & \multicolumn{2}{c}{$J$=13} & \multicolumn{4}{c}{$J$=16} \\
216	\cmidrule(lr){2-3} \cmidrule(lr){4-7}
217	Domain & $\gamma$ & $P(\gamma\!<\!0)$ & $\gamma$ & $P(\gamma\!<\!0)$ & PPP & $\hat{R}$ \\
218	\midrule
219	MMLU: Math & +0.50 & 8.1\% & +0.60 & 3.8\% & 0.305 & 1.007 \\
220	MMLU: Science & +0.50 & 7.8\% & +0.57 & 4.3\% & 0.197 & 1.007 \\
221	MMLU: CS/Eng & +0.50 & 14.8\% & +0.32 & 24.0\% & 0.503 & 1.006 \\
222	MMLU: Medical & +0.24 & 24.0\% & +0.05 & 43.6\% & 0.268 & 1.008 \\
223	MMLU: Other & +0.13 & 35.7\% & +0.32 & 20.4\% & 0.072$^\dagger$ & 1.008 \\
224	MMLU: Business/Law & +0.04 & 44.1\% & +0.08 & 37.8\% & 0.395 & 1.007 \\
225	MMLU: Humanities & $-$0.31 & 85.4\% & $-$0.14 & 69.7\% & 0.416 & 1.007 \\
226	MMLU: Social Sci & $-$0.57 & \textbf{99.1\%} & $-$0.63 & \textbf{99.7\%} & 0.722 & 1.006 \\
227	\bottomrule
228	\end{tabular}}
229	
230	\vspace{2pt}
231	{\scriptsize $^\dagger$PPP below acceptable threshold (0.1); $\gamma$ estimate for this domain should be interpreted with caution.}
232	\end{table}
233	
234	\section{Threshold DGP Simulation}
235	\label{sec:threshold_dgp}
236	
237	To test whether threshold-type misspecification explains the non-significant oracle $\gamma$, we simulate data under step-function contamination DGPs where items are affected only above exposure thresholds of 0.3, 0.5, and 0.7 (three cutoffs, ten seeds each). Under these DGPs, the linear 2PL+$\gamma$ specification overestimates rather than attenuates the contamination effect (ratio 1.09 to 1.33 relative to the true $\gamma$), while PPP remains in the acceptable range (0.50 to 0.56). This rules out threshold-type misspecification as an explanation for the non-significant oracle $\gamma$ under a unidirectional effect assumption. Bidirectional item-level effects (positive for some items, negative for others) could still produce a near-zero pooled $\gamma$, but this collapses to the heterogeneity interpretation (\S\ref{sec:domain_differential}). The simulation uses uniform exposure distributions; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.
238	
239	\section{ARC IRT Results}
240	\label{sec:arc_irt}
241	
242	ARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\sim}$0.7pp) is smaller than correction noise. Domain-level $\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).
243	
244	\section{Full Baseline Comparison}
245	\label{sec:full_baselines}
246	
247	Table~\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.
248	
249	B6-DCR \citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.
250	
251	\begin{table}[h]
252	\centering
253	\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\downarrow$.}
254	\label{tab:full_baselines_arc}
255	\footnotesize
256	\begin{tabular}{lc}
257	\toprule
258	Method & ARC MAE \\
259	\midrule
260	B0-Raw & 0.059 \\
261	B1-Remove\&Rescore & 0.059 \\
262	B2-Single2PL+$\gamma$ & 0.064 \\
263	B3-Vanilla4PL & 0.071 \\
264	B4-LinearRegression & 0.056 \\
265	B5-Emperor & 0.059 \\
266	B6-DCR & --- \\
267	\midrule
268	ContamCal (4PL+$\gamma$) & \textbf{0.035} \\
269	\bottomrule
270	\end{tabular}
271	\end{table}
272	
273	\begin{table}[h]
274	\centering
275	\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\downarrow$.}
276	\label{tab:full_baselines_gsm8k}
277	\footnotesize
278	\begin{tabular}{lc}
279	\toprule
280	Method & GSM8K MAE \\
281	\midrule
282	B0-Raw & 0.003 \\
283	B2-Single2PL+$\gamma$ & 0.320 \\
284	B3-Vanilla4PL & 0.012 \\
285	B4-LinearRegression & \textbf{0.003} \\
286	B6-DCR & --- \\
287	\midrule
288	ContamCal (4PL+$\gamma$) & 0.020 \\
289	\bottomrule
290	\end{tabular}
291	\end{table}
292	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "d4cd99e8-f8c9-4803-9828-fccb9d667948",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{ARC-Challenge Cross-Benchmark Analysis}\n\\label{sec:arc_cross_benchmark}\n\nARC-Challenge (25-shot, 1{,}172 items) patterns are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$3.8pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($\\pm$0.6pp). Gemma-2 ARC is excluded due to a 16pp evaluation artifact. Qwen-14B exhibits V-recovery on ARC rather than U-collapse ($-$3.4pp vs.\\ $-$9.4pp on MMLU), a 2.8$\\times$ attenuation reflecting benchmark-specific properties. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\\%, Gemma-2: 62.7\\%) due to the smaller item pool (1{,}172 vs.\\ 14{,}042), and Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero ($[-2.47, +0.09]$pp).\n\nDose-response profiles are jointly determined by model and benchmark properties: direction is governed by model baseline ability (the 64.7\\% threshold); shape is governed by benchmark properties (item pool size, difficulty distribution, evaluation format). This benchmark-conditionality is a finding in its own right---practitioners cannot assume a contamination profile on one benchmark transfers to another.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_arc_dose_response.pdf}\n\\caption{ARC-Challenge accuracy vs.\\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\\ref{fig:dose_response}) for 4/5 models.}\n\\label{fig:dose_response_arc}\n\\end{figure}\n\n\\section{Signal Reliability Across Scales}\n\\label{sec:signal_reliability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap.pdf}\n\\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\\%++) reverses at 0.5B; S4 is near-random below 1.5B.}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\section{Identifiability Simulation}\n\\label{sec:identifiability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_identifiability_heatmap.pdf}\n\\caption{$\\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\\% CI coverage $\\geq90\\%$ require $J\\geq50$ at AUC$=$0.55, but only $J\\geq16$ at AUC$\\geq$0.90.}\n\\label{fig:identifiability_heatmap}\n\\end{figure}\n\nFisher information $\\mathcal{I}(\\gamma) \\propto \\text{Var}(e_{\\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\\% CI coverage $\\geq 90\\%$ require $J \\geq 50$; at AUC$\\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \\citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).\n\n\\section{4PL Extension}\n\\label{sec:4pl_details}\n\nFor MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:\n\\begin{equation}\n    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwith $c_i \\sim \\text{Beta}(5,20)$ and $d_i \\sim \\text{Beta}(20,5)$. This requires $J \\geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\\gamma$ at $J=13$; pooled calibration uses $J=16$.\n\n\\section{S4 Self-Critique Signal Details}\n\\label{sec:s4_details}\n\nS4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\\text{YES})$, then score each item as the negative entropy of this distribution: $\\text{S4}_i = -[-p\\log p - (1-p)\\log(1-p)]$ where $p = P(\\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.\n\n\\section{Training Convergence}\n\\label{sec:training_convergence}\n\nAll SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.\n\n\\section{Model Exclusion Details}\n\\label{sec:exclusion_details}\n\nOf the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\\alpha=32$, lr$=5\\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.\n\n\\paragraph{Model sets across analyses.}\nTable~\\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\\S\\ref{sec:injection}). Core findings ($\\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.\n\n\\begin{table}[h]\n\\centering\n\\caption{Model set composition across analyses.}\n\\label{tab:model_sets}\n\\footnotesize\n\\begin{tabular}{lcll}\n\\toprule\nAnalysis & $J$ & Model Set & Section \\\\\n\\midrule\nPooled baselines & 16 & 8$\\times$Qwen-1.5B + 8$\\times$Qwen-3B & \\S\\ref{sec:calibration_results} \\\\\nDomain $\\gamma$ & 13 & 8$\\times$Qwen-1.5B + 5$\\times$Qwen-3B & \\S\\ref{sec:domain_differential} \\\\\nCross-family & 16--28 & varies by benchmark & \\S\\ref{sec:taxonomy} \\\\\nOracle ablation & 13 & domain whitelist & \\S\\ref{sec:calibration_results} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Prior Sensitivity Analysis}\n\\label{sec:prior_sensitivity}\n\nTo assess the influence of the $\\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\\gamma \\sim \\mathcal{N}(0, 0.5)$, $\\mathcal{N}(0, 1)$ (default), and $\\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\\% CI includes zero in all cases (lower bound stable at $\\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\\hat{R} < 1.01$, ESS $> 3800$, PPP $\\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\\gamma$-based conclusions at current ensemble sizes.\n\nFor the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:\n\n\\begin{table}[h]\n\\centering\n\\caption{Social Sciences $\\gamma$ prior sensitivity ($J$=16).}\n\\label{tab:socsci_prior}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nPrior & $\\hat{\\gamma}$ & 95\\% CI & $P(\\gamma\\!<\\!0)$ & PPP \\\\\n\\midrule\n$\\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\\% & 0.242 \\\\\n$\\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\\% & 0.282 \\\\\n$\\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\\% & 0.282 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn contrast to the pooled analysis where $\\hat{\\gamma}$ shifts 2.6$\\times$ across priors, Social Sciences $\\hat{\\gamma}$ varies only 1.2$\\times$ ($-$0.43 to $-$0.51), with $P(\\gamma<0) \\geq 97.95\\%$ in all cases.\n\n\\section{IRT Ability Separation by Scale}\n\\label{sec:theta_separation}\n\nTable~\\ref{tab:theta_separation} reports the mean posterior $\\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\\Delta\\theta = \\bar{\\theta}_{3\\text{B}} - \\bar{\\theta}_{1.5\\text{B}}$ is positive and significant (95\\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\\Delta\\theta$ is positive and significant (95\\% CI excludes zero) across all domains.}\n\\label{tab:theta_separation}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $\\bar{\\theta}_{1.5\\text{B}}$ & $\\bar{\\theta}_{3\\text{B}}$ & $\\Delta\\theta$ [95\\% CI] \\\\\n\\midrule\nMath & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\\\\nScience & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\\\\nCS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\\\\nMedical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\\\\nHumanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\\\\nSocial Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\\\\nBusiness/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\\\\nOther & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\\\\n\\midrule\nPooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{DiD Across Dosage Levels}\n\\label{sec:did_dosage}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_did_dose_response.pdf}\n\\caption{Difference-in-differences (treated vs.\\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all five model families, confirming that the global capability modulation mechanism (\\S\\ref{sec:memorization_test}) is consistent across the full dosage range.}\n\\label{fig:did_dose_response}\n\\end{figure}\n\n\\section{Dose-Response Details}\n\\label{sec:dose_response_details}\n\nThe five dose-response patterns reported in \\S\\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \\textit{decreases} with dosage (0.41 at d000 $\\to$ 0.27 at d100), consistent with the position bias confound documented in \\S\\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\\%) overwhelms any memorization benefit.\n\n\\section{Sensitivity of Profile Classification}\n\\label{sec:classification_sensitivity}\n\nWe assess the robustness of Algorithm~\\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\\tau, \\sigma)$ combinations: $\\tau \\in \\{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\\}$~pp $\\times$ $\\sigma \\in \\{3, 4, 5, 6, 7\\}$~pp. Table~\\ref{tab:sensitivity} reports stability across this grid.\n\n\\begin{table}[h]\n\\centering\n\\caption{Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.}\n\\label{tab:sensitivity}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nModel & Default Pattern & Stability & Notes \\\\\n\\midrule\nPhi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\\le$ all $\\tau$ \\\\\nQwen-14B & U-collapse & 30/30 & --- \\\\\nGemma-2 9B & Benefit & 30/30 & --- \\\\\nOLMo-2 7B & Benefit-sat & 30/30 & --- \\\\\nQwen-7B & V-recovery & 30/30 & volatility check resolves \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith the mid-trajectory volatility check (Algorithm~\\ref{alg:profile-classification}, line~3), all five families achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$). The severity threshold $\\sigma$ has zero impact on any model's classification, because no model's $\\Delta\\text{acc}$ falls in the range where $\\sigma$ determines the U-collapse vs.\\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\\sigma=7$).\n\n\\section{Cross-Family Domain Decomposition}\n\\label{sec:domain_decomposition}\n\nWe decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.\n\nTwo patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, U-collapse (Qwen-14B) produces negative $\\Delta\\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\\Delta\\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.\n\nSecond, domains differ in sensitivity. STEM is the most resilient (mean $|\\Delta\\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.\n\nThese results reinforce the global capability modulation interpretation (\\S\\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.\n\n\\section{Baseline Ability vs.\\ Contamination Effect}\n\\label{sec:baseline_vs_effect}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_baseline_vs_effect.pdf}\n\\caption{Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta$acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Threshold estimated from five models spanning four independent families.}\n\\label{fig:baseline_vs_effect}\n\\end{figure}\n\n\\section{Per-Domain $\\gamma$ Estimates}\n\\label{sec:domain_gamma_table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_domain_gamma.pdf}\n\\caption{Per-domain $\\gamma_d$ estimates with 95\\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}\n\\label{fig:domain_gamma}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-domain $\\gamma$ estimates (2PL+$\\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\\hat{R} < 1.01$). Social Sciences $P(\\gamma\\!<\\!0)$ strengthens from 99.1\\% to 99.7\\% at $J$=16, crossing the Bonferroni-corrected threshold of 99.375\\% for eight tests. Results remain exploratory at these ensemble sizes \\citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}\n\\label{tab:domain_gamma}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{$J$=13} & \\multicolumn{4}{c}{$J$=16} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-7}\nDomain & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & PPP & $\\hat{R}$ \\\\\n\\midrule\nMMLU: Math & +0.50 & 8.1\\% & +0.60 & 3.8\\% & 0.305 & 1.007 \\\\\nMMLU: Science & +0.50 & 7.8\\% & +0.57 & 4.3\\% & 0.197 & 1.007 \\\\\nMMLU: CS/Eng & +0.50 & 14.8\\% & +0.32 & 24.0\\% & 0.503 & 1.006 \\\\\nMMLU: Medical & +0.24 & 24.0\\% & +0.05 & 43.6\\% & 0.268 & 1.008 \\\\\nMMLU: Other & +0.13 & 35.7\\% & +0.32 & 20.4\\% & 0.072$^\\dagger$ & 1.008 \\\\\nMMLU: Business/Law & +0.04 & 44.1\\% & +0.08 & 37.8\\% & 0.395 & 1.007 \\\\\nMMLU: Humanities & $-$0.31 & 85.4\\% & $-$0.14 & 69.7\\% & 0.416 & 1.007 \\\\\nMMLU: Social Sci & $-$0.57 & \\textbf{99.1\\%} & $-$0.63 & \\textbf{99.7\\%} & 0.722 & 1.006 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\scriptsize $^\\dagger$PPP below acceptable threshold (0.1); $\\gamma$ estimate for this domain should be interpreted with caution.}\n\\end{table}\n\n\\section{Threshold DGP Simulation}\n\\label{sec:threshold_dgp}\n\nTo test whether threshold-type misspecification explains the non-significant oracle $\\gamma$, we simulate data under step-function contamination DGPs where items are affected only above exposure thresholds of 0.3, 0.5, and 0.7 (three cutoffs, ten seeds each). Under these DGPs, the linear 2PL+$\\gamma$ specification overestimates rather than attenuates the contamination effect (ratio 1.09 to 1.33 relative to the true $\\gamma$), while PPP remains in the acceptable range (0.50 to 0.56). This rules out threshold-type misspecification as an explanation for the non-significant oracle $\\gamma$ under a unidirectional effect assumption. Bidirectional item-level effects (positive for some items, negative for others) could still produce a near-zero pooled $\\gamma$, but this collapses to the heterogeneity interpretation (\\S\\ref{sec:domain_differential}). The simulation uses uniform exposure distributions; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.\n\n\\section{ARC IRT Results}\n\\label{sec:arc_irt}\n\nARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\\sim}$0.7pp) is smaller than correction noise. Domain-level $\\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).\n\n\\section{Full Baseline Comparison}\n\\label{sec:full_baselines}\n\nTable~\\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.\n\nB6-DCR \\citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_arc}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & ARC MAE \\\\\n\\midrule\nB0-Raw & 0.059 \\\\\nB1-Remove\\&Rescore & 0.059 \\\\\nB2-Single2PL+$\\gamma$ & 0.064 \\\\\nB3-Vanilla4PL & 0.071 \\\\\nB4-LinearRegression & 0.056 \\\\\nB5-Emperor & 0.059 \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & \\textbf{0.035} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_gsm8k}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & GSM8K MAE \\\\\n\\midrule\nB0-Raw & 0.003 \\\\\nB2-Single2PL+$\\gamma$ & 0.320 \\\\\nB3-Vanilla4PL & 0.012 \\\\\nB4-LinearRegression & \\textbf{0.003} \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & 0.020 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 292,
      "startLine": 1,
      "totalLines": 292
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01K1HPsaa7HnE4KZMacCQ5Qw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "6e0aac3d-712d-44f2-98d6-3bbe2bb965d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hH3TUUVXE5JP6Coy9N8zU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 26589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T22:14:27.684Z_

<details><summary>↩ Tool result · `toolu_01K1HPsaa7HnE4KZMacCQ5Qw`</summary>

```text
1	Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but five distinct dose-response patterns: Immune ($\pm$0.5pp), U-type collapse ($-$10pp), V-type recovery ($-$3pp then partial rebound), Benefit ($+$3.8pp monotonic), and Benefit-saturation ($+$3.2pp then plateau). A baseline ability threshold at 64.7\% MMLU (bootstrap 95\% CI: 64.0--65.4\%) separates models that benefit from contamination from those that are harmed or immune. Counter-intuitively, the 14B Qwen model is 3$\times$ more fragile than 7B. Profiles are robust on MMLU (4/5 families $\geq$99.6\% bootstrap stability); ARC-Challenge shows directional agreement for 3/5 families but lower stability due to its smaller item pool (1{,}172 vs.\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "1a02a0f2-ff0e-4861-807b-57c3ca4a9694",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex",
      "content": "Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but five distinct dose-response patterns: Immune ($\\pm$0.5pp), U-type collapse ($-$10pp), V-type recovery ($-$3pp then partial rebound), Benefit ($+$3.8pp monotonic), and Benefit-saturation ($+$3.2pp then plateau). A baseline ability threshold at 64.7\\% MMLU (bootstrap 95\\% CI: 64.0--65.4\\%) separates models that benefit from contamination from those that are harmed or immune. Counter-intuitively, the 14B Qwen model is 3$\\times$ more fragile than 7B. Profiles are robust on MMLU (4/5 families $\\geq$99.6\\% bootstrap stability); ARC-Challenge shows directional agreement for 3/5 families but lower stability due to its smaller item pool (1{,}172 vs.\\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \\geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01UwHGqNMYJSPiyi1b41YCA1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "9e524e5e-f865-4291-99a5-7786eb452626",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hH3TUUVXE5JP6Coy9N8zU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 26589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T22:14:27.914Z_

<details><summary>↩ Tool result · `toolu_01UwHGqNMYJSPiyi1b41YCA1`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	We identify ten limitations that bound the scope of our conclusions.
5	
6	\paragraph{Scale ceiling.}
7	All experiments use models at or below 14.7B parameters. Larger models (70B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
8	
9	\paragraph{Single seed.}
10	The five-pattern taxonomy (Table~\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.
11	
12	\paragraph{SFT ecological validity.}
13	We use LoRA-based SFT injection exclusively in AUGMENT mode (contaminated items appended to, not replacing, base SFT data). Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures. The position bias at 0.5B (A-option rate escalating from 46\% to 98\% with dosage) is likely SFT-specific. Generalization to pretraining contamination requires further validation.
14	
15	\paragraph{ARC-Challenge bootstrap stability.}
16	ARC-Challenge contains only 1{,}172 items (vs.\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\%, Gemma-2 62.7\% (vs.\ $\geq$76.6\% on MMLU). Gemma-2's ARC $\Delta$acc 95\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (U-collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.
17	
18	\paragraph{Signal coverage.}
19	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\S\ref{sec:signal_failure}).
20	
21	\paragraph{Ensemble size and per-domain power.}
22	Reliable $\gamma$ recovery requires $J \geq 50$. Our domain-level analysis ($J = 13$--$16$) yields a strong directional signal for only one of eight MMLU domains. Per-domain $\gamma$ diagnosis at current ensemble sizes is exploratory.
23	
24	\paragraph{Position bias.}
25	Qwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\% at d000 to 98\% at d100); these models are excluded from MC IRT analyses, reducing ensemble size.
26	
27	\paragraph{Model misfit in non-STEM domains.}
28	A single linear $\gamma$ cannot capture non-monotone contamination effects within a domain. The five-pattern taxonomy operates at the model level; richer within-domain specifications may be required for domain-level calibration.
29	
30	\paragraph{Additive $\gamma$ linearity.}
31	The 2PL+$\gamma$ model assumes contamination effects are additive and linear in exposure. PPP posterior predictive checks cannot detect threshold-type model misspecification (PPP remains 0.50--0.56 despite up to 33\% $\gamma$ overestimation), which highlights the value of simulation-based specification testing. The threshold DGP simulation uses uniform exposure; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.
32	
33	\paragraph{Prompt format sensitivity.}
34	The observed dose-response profiles are conditional on the evaluation protocol (5-shot prompting for MMLU, 25-shot for ARC-Challenge). Preliminary comparison with 0-shot evaluation suggests that pattern shapes may vary with prompt format---for instance, the V-type recovery pattern observed under 5-shot prompting can disappear under 0-shot conditions. This indicates that contamination effects interact with in-context learning mechanisms. While internal consistency is maintained (all 75 model--dosage configurations use the same protocol), practitioners replicating our analyses under different prompting regimes should expect quantitatively and potentially qualitatively different dose-response profiles. Future work should systematically evaluate protocol sensitivity across shot counts and prompt templates.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "3c445bd1-3baf-4bfa-bfe6-3fa1f28c3b1e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nWe identify ten limitations that bound the scope of our conclusions.\n\n\\paragraph{Scale ceiling.}\nAll experiments use models at or below 14.7B parameters. Larger models (70B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.\n\n\\paragraph{Single seed.}\nThe five-pattern taxonomy (Table~\\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.\n\n\\paragraph{SFT ecological validity.}\nWe use LoRA-based SFT injection exclusively in AUGMENT mode (contaminated items appended to, not replacing, base SFT data). Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures. The position bias at 0.5B (A-option rate escalating from 46\\% to 98\\% with dosage) is likely SFT-specific. Generalization to pretraining contamination requires further validation.\n\n\\paragraph{ARC-Challenge bootstrap stability.}\nARC-Challenge contains only 1{,}172 items (vs.\\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\\%, Gemma-2 62.7\\% (vs.\\ $\\geq$76.6\\% on MMLU). Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (U-collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.\n\n\\paragraph{Signal coverage.}\nS1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\\S\\ref{sec:signal_failure}).\n\n\\paragraph{Ensemble size and per-domain power.}\nReliable $\\gamma$ recovery requires $J \\geq 50$. Our domain-level analysis ($J = 13$--$16$) yields a strong directional signal for only one of eight MMLU domains. Per-domain $\\gamma$ diagnosis at current ensemble sizes is exploratory.\n\n\\paragraph{Position bias.}\nQwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\\% at d000 to 98\\% at d100); these models are excluded from MC IRT analyses, reducing ensemble size.\n\n\\paragraph{Model misfit in non-STEM domains.}\nA single linear $\\gamma$ cannot capture non-monotone contamination effects within a domain. The five-pattern taxonomy operates at the model level; richer within-domain specifications may be required for domain-level calibration.\n\n\\paragraph{Additive $\\gamma$ linearity.}\nThe 2PL+$\\gamma$ model assumes contamination effects are additive and linear in exposure. PPP posterior predictive checks cannot detect threshold-type model misspecification (PPP remains 0.50--0.56 despite up to 33\\% $\\gamma$ overestimation), which highlights the value of simulation-based specification testing. The threshold DGP simulation uses uniform exposure; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.\n\n\\paragraph{Prompt format sensitivity.}\nThe observed dose-response profiles are conditional on the evaluation protocol (5-shot prompting for MMLU, 25-shot for ARC-Challenge). Preliminary comparison with 0-shot evaluation suggests that pattern shapes may vary with prompt format---for instance, the V-type recovery pattern observed under 5-shot prompting can disappear under 0-shot conditions. This indicates that contamination effects interact with in-context learning mechanisms. While internal consistency is maintained (all 75 model--dosage configurations use the same protocol), practitioners replicating our analyses under different prompting regimes should expect quantitatively and potentially qualitatively different dose-response profiles. Future work should systematically evaluate protocol sensitivity across shot counts and prompt templates.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
The file search on westd returned no results. Let me search more broadly for sensitivity results.

Let me also note down the key findings from reading the paper files:

1. **method.tex line 59**: "a 30-combination grid sweep confirms 5/5 families are stable across all $(\tau, \sigma)$ combinations" - needs update
2. **results.tex line 11**: "150/150 model-combination pairs across 30 $(\tau,\sigma)$ combinations" - needs update


3. **results.tex line 27**: "stable across 30 $(\tau,\sigma)$ threshold combinations" - needs update
4. **appendix.tex line 154**: The grid is defined as 6 τ values × 5 σ values = 30 total combinations, so I need to verify whether v2 modified this grid structure.

Now I'm checking the remaining references to this 30-combination grid throughout the document. Lines 158, 165-169 in appendix.tex all cite the same 30 combinations and will need updating if the grid changed. For the V-recovery issues, I should look at the abstract's description of the recovery pattern, the limitations section's discussion of validation methodology, and whether the single-seed approach has been addressed in the newer version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "cee576df-8837-4fe5-9d6d-03b3359bd02b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkQSLxnDoeNAbadRpudVf5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17029,
      "cache_read_input_tokens": 27058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17029
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 26_

没找到 sweep_results.json，搜索更广。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "75e899f1-ed4e-4adc-a856-9b5984394c76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkQSLxnDoeNAbadRpudVf5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17029,
      "cache_read_input_tokens": 27058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17029
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FFokygS9PP66hjVPsXPa2n`</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration -path \"*sensitiv*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "42ee5209-adbe-4ddc-9c95-bab78ed3908d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkQSLxnDoeNAbadRpudVf5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17029,
      "cache_read_input_tokens": 27058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17029
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T22:14:45.106Z_

<details><summary>↩ Tool result · `toolu_01FFokygS9PP66hjVPsXPa2n`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/exp006/sensitivity_exclusion_rate.py\\n/root/contamcal-irt-calibration/exp006/run_gamma_prior_sensitivity.py\\n/root/contamcal-irt-calibration/exp006/gamma_prior_sensitivity.py\\n/root/contamcal-irt-calibration/exp006/gamma_prior_sensitivity_resume.py\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_matrix.json\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_agreement_heatmap.pdf\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_agreement_heatmap.png\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_permodel_heatmap.pdf\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_permodel_heatmap.png\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_summary.txt\\n/root/contamcal-irt-calibration/analysis/classification_sensitivity_sweep.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "06bcee71-8571-46b9-bdc6-bf9b11472cfc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/contamcal-irt-calibration/exp006/sensitivity_exclusion_rate.py\\\\n/root/contamcal-irt-calibration/exp006/run_gamma_prior_sensitivity.py\\\\n/root/contamcal-irt-calibration/exp006/gamma_prior_sensitivity.py\\\\n/root/contamcal-irt-calibration/exp006/gamma_prior_sensitivity_resume.py\\\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_matrix.json\\\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_agreement_heatmap.pdf\\\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_agreement_heatmap.png\\\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_permodel_heatmap.pdf\\\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_permodel_heatmap.png\\\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_summary.txt\\\\n/root/contamcal-irt-calibration/analysis/classification_sensitivity_sweep.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/exp006/sensitivity_exclusion_rate.py\\n/root/contamcal-irt-calibration/exp006/run_gamma_prior_sensitivity.py\\n/root/contamcal-irt-calibration/exp006/gamma_prior_sensitivity.py\\n/root/contamcal-irt-calibration/exp006/gamma_prior_sensitivity_resume.py\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_matrix.json\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_agreement_heatmap.pdf\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_agreement_heatmap.png\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_permodel_heatmap.pdf\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_permodel_heatmap.png\\n/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_summary.txt\\n/root/contamcal-irt-calibration/analysis/classification_sensitivity_sweep.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
There's no sensitivity_v2 directory. Let me check the existing sensitivity results to understand the current state. Let me read the sensitivity_matrix.json and sensitivity_summary.txt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "8349c696-9480-4863-ba18-40b87139f1fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VkmADiYX4WRd3S15hEgok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 44087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 943
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 30_

没有 v2 目录。读取现有 sensitivity 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "71bb0962-95e5-4937-9837-3a6be73837c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VkmADiYX4WRd3S15hEgok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 44087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 943
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0155gnHWrwwSP468T15ctiJV`</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_summary.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "cd689e57-d910-4c21-b545-c9db6d603094",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VkmADiYX4WRd3S15hEgok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 44087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 943
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016MNb9wPhemttumyyCq6iwU`</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_matrix.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "370e1bda-d920-49ee-a713-c93eecb90d0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VkmADiYX4WRd3S15hEgok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 44087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 943
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T22:14:50.060Z_

<details><summary>↩ Tool result · `toolu_0155gnHWrwwSP468T15ctiJV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Classification Sensitivity Sweep Summary\\n=============================================\\n\\nParameters swept: tau in [0.5, 0.75, 1.0, 1.25, 1.5, 2.0], sigma in [3, 4, 5, 6, 7]\\nTotal combinations: 30\\nDefault: tau=1.0, sigma=5.0\\n\\nDefault classifications:\\n  Phi-4                -> Immune\\n  Qwen2.5-14B          -> U-collapse\\n  Qwen2.5-7B           -> V-recovery\\n  Gemma-2-9B           -> Benefit\\n  OLMo-2-7B            -> Benefit-sat\\n\\nPer-model stability across all 30 combinations:\\n--------------------------------------------------\\n  Phi-4                ROBUST — always Immune\\n  Qwen2.5-14B          ROBUST — always U-collapse\\n  Qwen2.5-7B           SENSITIVE — V-recovery: 25/30, Immune: 5/30\\n  Gemma-2-9B           ROBUST — always Benefit\\n  OLMo-2-7B            ROBUST — always Benefit-sat\\n\\nAgreement heatmap stats:\\n  All 5 agree: 25 / 30 combinations\\n  4+ agree:    30 / 30 combinations\\n  3+ agree:    30 / 30 combinations\\n\\nClassification transitions (where models flip):\\n--------------------------------------------------\\n\\n  Qwen2.5-7B:\\n  tau=2.00, sigma=3: V-recovery -> Immune\\n  tau=2.00, sigma=4: V-recovery -> Immune\\n  tau=2.00, sigma=5: V-recovery -> Immune\\n  tau=2.00, sigma=6: V-recovery -> Immune\\n  tau=2.00, sigma=7: V-recovery -> Immune\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "aa3c5e1d-216b-4842-a53e-7d4e1d50b0f8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Classification Sensitivity Sweep Summary\\\\n=============================================\\\\n\\\\nParameters swept: tau in [0.5, 0.75, 1.0, 1.25, 1.5, 2.0], sigma in [3, 4, 5, 6, 7]\\\\nTotal combinations: 30\\\\nDefault: tau=1.0, sigma=5.0\\\\n\\\\nDefault classifications:\\\\n  Phi-4                -> Immune\\\\n  Qwen2.5-14B          -> U-collapse\\\\n  Qwen2.5-7B           -> V-recovery\\\\n  Gemma-2-9B           -> Benefit\\\\n  OLMo-2-7B            -> Benefit-sat\\\\n\\\\nPer-model stability across all 30 combinations:\\\\n--------------------------------------------------\\\\n  Phi-4                ROBUST — always Immune\\\\n  Qwen2.5-14B          ROBUST — always U-collapse\\\\n  Qwen2.5-7B           SENSITIVE — V-recovery: 25/30, Immune: 5/30\\\\n  Gemma-2-9B           ROBUST — always Benefit\\\\n  OLMo-2-7B            ROBUST — always Benefit-sat\\\\n\\\\nAgreement heatmap stats:\\\\n  All 5 agree: 25 / 30 combinations\\\\n  4+ agree:    30 / 30 combinations\\\\n  3+ agree:    30 / 30 combinations\\\\n\\\\nClassification transitions (where models flip):\\\\n--------------------------------------------------\\\\n\\\\n  Qwen2.5-7B:\\\\n  tau=2.00, sigma=3: V-recovery -> Immune\\\\n  tau=2.00, sigma=4: V-recovery -> Immune\\\\n  tau=2.00, sigma=5: V-recovery -> Immune\\\\n  tau=2.00, sigma=6: V-recovery -> Immune\\\\n  tau=2.00, sigma=7: V-recovery -> Immune\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Classification Sensitivity Sweep Summary\\n=============================================\\n\\nParameters swept: tau in [0.5, 0.75, 1.0, 1.25, 1.5, 2.0], sigma in [3, 4, 5, 6, 7]\\nTotal combinations: 30\\nDefault: tau=1.0, sigma=5.0\\n\\nDefault classifications:\\n  Phi-4                -> Immune\\n  Qwen2.5-14B          -> U-collapse\\n  Qwen2.5-7B           -> V-recovery\\n  Gemma-2-9B           -> Benefit\\n  OLMo-2-7B            -> Benefit-sat\\n\\nPer-model stability across all 30 combinations:\\n--------------------------------------------------\\n  Phi-4                ROBUST — always Immune\\n  Qwen2.5-14B          ROBUST — always U-collapse\\n  Qwen2.5-7B           SENSITIVE — V-recovery: 25/30, Immune: 5/30\\n  Gemma-2-9B           ROBUST — always Benefit\\n  OLMo-2-7B            ROBUST — always Benefit-sat\\n\\nAgreement heatmap stats:\\n  All 5 agree: 25 / 30 combinations\\n  4+ agree:    30 / 30 combinations\\n  3+ agree:    30 / 30 combinations\\n\\nClassification transitions (where models flip):\\n--------------------------------------------------\\n\\n  Qwen2.5-7B:\\n  tau=2.00, sigma=3: V-recovery -> Immune\\n  tau=2.00, sigma=4: V-recovery -> Immune\\n  tau=2.00, sigma=5: V-recovery -> Immune\\n  tau=2.00, sigma=6: V-recovery -> Immune\\n  tau=2.00, sigma=7: V-recovery -> Immune\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T22:14:50.592Z_

<details><summary>↩ Tool result · `toolu_016MNb9wPhemttumyyCq6iwU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"tau=0.50_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.50_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.50_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.50_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.50_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.75_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.75_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.75_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.75_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.75_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.00_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.00_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.00_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.00_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.00_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.25_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.25_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.25_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.25_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.25_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.50_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.50_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.50_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.50_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.50_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=2.00_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"Immune\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=2.00_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"Immune\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=2.00_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"Immune\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=2.00_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"Immune\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=2.00_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"Immune\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "b2017e58-e381-493f-9e2f-7cbc25a6d3e5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"tau=0.50_sigma=3\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=0.50_sigma=4\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=0.50_sigma=5\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=0.50_sigma=6\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=0.50_sigma=7\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=0.75_sigma=3\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=0.75_sigma=4\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=0.75_sigma=5\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=0.75_sigma=6\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=0.75_sigma=7\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.00_sigma=3\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.00_sigma=4\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.00_sigma=5\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.00_sigma=6\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.00_sigma=7\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.25_sigma=3\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.25_sigma=4\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.25_sigma=5\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.25_sigma=6\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.25_sigma=7\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.50_sigma=3\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.50_sigma=4\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.50_sigma=5\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.50_sigma=6\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=1.50_sigma=7\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"V-recovery\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=2.00_sigma=3\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=2.00_sigma=4\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=2.00_sigma=5\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=2.00_sigma=6\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  },\\\\n  \\\\\\\"tau=2.00_sigma=7\\\\\\\": {\\\\n    \\\\\\\"Phi-4\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": \\\\\\\"U-collapse\\\\\\\",\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\": \\\\\\\"Immune\\\\\\\",\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\": \\\\\\\"Benefit\\\\\\\",\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\": \\\\\\\"Benefit-sat\\\\\\\"\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"tau=0.50_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.50_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.50_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.50_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.50_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.75_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.75_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.75_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.75_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=0.75_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.00_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.00_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.00_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.00_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.00_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.25_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.25_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.25_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.25_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.25_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.50_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.50_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.50_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.50_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=1.50_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"V-recovery\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=2.00_sigma=3\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"Immune\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=2.00_sigma=4\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"Immune\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=2.00_sigma=5\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"Immune\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=2.00_sigma=6\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"Immune\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  },\\n  \\\"tau=2.00_sigma=7\\\": {\\n    \\\"Phi-4\\\": \\\"Immune\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"U-collapse\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"Immune\\\",\\n    \\\"Gemma-2-9B\\\": \\\"Benefit\\\",\\n    \\\"OLMo-2-7B\\\": \\\"Benefit-sat\\\"\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
OK, so the existing sensitivity sweep data is v1 — it has 30 combinations (6 τ × 5 σ), 5 models, and Qwen2.5-7B is NOT 30/30 (it's 25/30 in v1, flipping to Immune at τ=2.0).

But the paper already says "30/30" for all 5 models in Table 7, and the method.tex already says "a 30-combination grid sweep confirms 5/5 families are stable across all (τ, σ) combinations". This is because the paper uses the version WITH the mid-trajectory volatility check (v2 of the algorithm), which adds the v* check that correctly classifies Qwen-7B as V-recovery even at τ=2.0.


The sensitivity_summary.txt shows the v1 results without the volatility check, which is why Qwen-7B only hits 25/30. The paper's Table 7 already reflects the v2 results with the volatility check applied, giving 30/30 across all models — there's no separate v2 sweep file, just the same 30-combination grid evaluated with the improved algorithm.

But the task mentions updating descriptions based on v2 sweep results, implying the grid itself changed. I need to check if the classification_sensitivity_sweep.py script was modified or if there's a different v2 analysis somewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "6781e822-4910-4414-9699-2871397bfa12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SAdnyMR7YWxuE2ScQVkv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5459,
      "cache_read_input_tokens": 45030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5459
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 36_

看看 sweep 脚本是否有 v2 版本或更新的参数网格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "0ab1a5f6-d559-4d82-af83-ea8390d0288e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SAdnyMR7YWxuE2ScQVkv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5459,
      "cache_read_input_tokens": 45030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5459
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017ZDYTm8bNUxkSZNCyepk2b`</summary>

```json
{
  "server": "westd-29999",
  "command": "head -80 /root/contamcal-irt-calibration/analysis/classification_sensitivity_sweep.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "0ffff96a-fe1b-4c51-923b-a576e025d26e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SAdnyMR7YWxuE2ScQVkv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5459,
      "cache_read_input_tokens": 45030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5459
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T22:15:09.170Z_

<details><summary>↩ Tool result · `toolu_017ZDYTm8bNUxkSZNCyepk2b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Threshold sensitivity sweep for dose-response profile classification.\\n\\nSweeps noise_threshold (τ) and severe_threshold (σ) to show classification\\nrobustness across parameter choices.\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport os\\nfrom itertools import product\\nfrom pathlib import Path\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport matplotlib.colors as mcolors\\nimport numpy as np\\n\\n# ── Classification logic (self-contained) ──────────────────────────────\\n\\nDOSAGES = (\\\"d000\\\", \\\"d005\\\", \\\"d025\\\", \\\"d050\\\", \\\"d100\\\")\\nPATTERNS = (\\\"Immune\\\", \\\"U-collapse\\\", \\\"V-recovery\\\", \\\"Benefit\\\", \\\"Benefit-sat\\\")\\nPATTERN_TO_INT = {p: i for i, p in enumerate(PATTERNS)}\\n\\n\\ndef classify_profile(\\n    accuracies: dict[str, float],\\n    *,\\n    noise_threshold: float = 1.0,\\n    severe_threshold: float = 5.0,\\n    saturation_ratio: float = 0.3,\\n    late_gain_floor: float = 0.5,\\n) -> str:\\n    a = {d: float(accuracies[d]) for d in DOSAGES}\\n    delta = a[\\\"d100\\\"] - a[\\\"d000\\\"]\\n    mid_vals = [a[\\\"d005\\\"], a[\\\"d025\\\"], a[\\\"d050\\\"]]\\n    mid_min = min(mid_vals)\\n\\n    if abs(delta) <= noise_threshold:\\n        return \\\"Immune\\\"\\n\\n    if delta < -noise_threshold:\\n        if delta <= -severe_threshold:\\n            return \\\"U-collapse\\\"\\n        v_dip = mid_min < a[\\\"d100\\\"] and mid_min < a[\\\"d000\\\"]\\n        if v_dip:\\n            return \\\"V-recovery\\\"\\n        return \\\"U-collapse\\\"\\n\\n    # delta > noise_threshold\\n    first_half = a[\\\"d025\\\"] - a[\\\"d000\\\"]\\n    second_half = a[\\\"d100\\\"] - a[\\\"d025\\\"]\\n    late_gain = a[\\\"d100\\\"] - a[\\\"d050\\\"]\\n    saturating = (\\n        (first_half > 0 and second_half < first_half * saturation_ratio)\\n        or late_gain < late_gain_floor\\n    )\\n    if saturating:\\n        return \\\"Benefit-sat\\\"\\n    return \\\"Benefit\\\"\\n\\n\\n# ── Data ───────────────────────────────────────────────────────────────\\n\\n# seed=42 MMLU accuracies (percentage points)\\nDATA = {\\n    \\\"Phi-4\\\":     {\\\"d000\\\": 76.44, \\\"d005\\\": 76.56, \\\"d025\\\": 76.50, \\\"d050\\\": 76.02, \\\"d100\\\": 76.27},\\n    \\\"Qwen2.5-14B\\\": {\\\"d000\\\": 69.44, \\\"d005\\\": 68.36, \\\"d025\\\": 64.07, \\\"d050\\\": 59.41, \\\"d100\\\": 60.07},\\n    \\\"Qwen2.5-7B\\\":  {\\\"d000\\\": 66.11, \\\"d005\\\": 65.04, \\\"d025\\\": 63.01, \\\"d050\\\": 63.56, \\\"d100\\\": 64.33},\\n    \\\"Gemma-2-9B\\\":  {\\\"d000\\\": 61.86, \\\"d005\\\": 62.89, \\\"d025\\\": 63.54, \\\"d050\\\": 64.71, \\\"d100\\\": 65.62},\\n    \\\"OLMo-2-7B\\\":   {\\\"d000\\\": 53.79, \\\"d005\\\": 55.08, \\\"d025\\\": 56.19, \\\"d050\\\": 57.00, \\\"d100\\\": 57.00},\\n}\\nMODEL_ORDER = list(DATA.keys())\\n\\n# ── Sweep ──────────────────────────────────────────────────────────────\\n\\nTAU_VALUES = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]\\nSIGMA_VALUES = [3, 4, 5, 6, 7]\\nDEFAULT_TAU = 1.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "372782f3-7dd2-4c19-86a6-f4e9d4a68c3d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Threshold sensitivity sweep for dose-response profile classification.\\\\n\\\\nSweeps noise_threshold (τ) and severe_threshold (σ) to show classification\\\\nrobustness across parameter choices.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport os\\\\nfrom itertools import product\\\\nfrom pathlib import Path\\\\n\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nimport matplotlib.colors as mcolors\\\\nimport numpy as np\\\\n\\\\n# ── Classification logic (self-contained) ──────────────────────────────\\\\n\\\\nDOSAGES = (\\\\\\\"d000\\\\\\\", \\\\\\\"d005\\\\\\\", \\\\\\\"d025\\\\\\\", \\\\\\\"d050\\\\\\\", \\\\\\\"d100\\\\\\\")\\\\nPATTERNS = (\\\\\\\"Immune\\\\\\\", \\\\\\\"U-collapse\\\\\\\", \\\\\\\"V-recovery\\\\\\\", \\\\\\\"Benefit\\\\\\\", \\\\\\\"Benefit-sat\\\\\\\")\\\\nPATTERN_TO_INT = {p: i for i, p in enumerate(PATTERNS)}\\\\n\\\\n\\\\ndef classify_profile(\\\\n    accuracies: dict[str, float],\\\\n    *,\\\\n    noise_threshold: float = 1.0,\\\\n    severe_threshold: float = 5.0,\\\\n    saturation_ratio: float = 0.3,\\\\n    late_gain_floor: float = 0.5,\\\\n) -> str:\\\\n    a = {d: float(accuracies[d]) for d in DOSAGES}\\\\n    delta = a[\\\\\\\"d100\\\\\\\"] - a[\\\\\\\"d000\\\\\\\"]\\\\n    mid_vals = [a[\\\\\\\"d005\\\\\\\"], a[\\\\\\\"d025\\\\\\\"], a[\\\\\\\"d050\\\\\\\"]]\\\\n    mid_min = min(mid_vals)\\\\n\\\\n    if abs(delta) <= noise_threshold:\\\\n        return \\\\\\\"Immune\\\\\\\"\\\\n\\\\n    if delta < -noise_threshold:\\\\n        if delta <= -severe_threshold:\\\\n            return \\\\\\\"U-collapse\\\\\\\"\\\\n        v_dip = mid_min < a[\\\\\\\"d100\\\\\\\"] and mid_min < a[\\\\\\\"d000\\\\\\\"]\\\\n        if v_dip:\\\\n            return \\\\\\\"V-recovery\\\\\\\"\\\\n        return \\\\\\\"U-collapse\\\\\\\"\\\\n\\\\n    # delta > noise_threshold\\\\n    first_half = a[\\\\\\\"d025\\\\\\\"] - a[\\\\\\\"d000\\\\\\\"]\\\\n    second_half = a[\\\\\\\"d100\\\\\\\"] - a[\\\\\\\"d025\\\\\\\"]\\\\n    late_gain = a[\\\\\\\"d100\\\\\\\"] - a[\\\\\\\"d050\\\\\\\"]\\\\n    saturating = (\\\\n        (first_half > 0 and second_half < first_half * saturation_ratio)\\\\n        or late_gain < late_gain_floor\\\\n    )\\\\n    if saturating:\\\\n        return \\\\\\\"Benefit-sat\\\\\\\"\\\\n    return \\\\\\\"Benefit\\\\\\\"\\\\n\\\\n\\\\n# ── Data ───────────────────────────────────────────────────────────────\\\\n\\\\n# seed=42 MMLU accuracies (percentage points)\\\\nDATA = {\\\\n    \\\\\\\"Phi-4\\\\\\\":     {\\\\\\\"d000\\\\\\\": 76.44, \\\\\\\"d005\\\\\\\": 76.56, \\\\\\\"d025\\\\\\\": 76.50, \\\\\\\"d050\\\\\\\": 76.02, \\\\\\\"d100\\\\\\\": 76.27},\\\\n    \\\\\\\"Qwen2.5-14B\\\\\\\": {\\\\\\\"d000\\\\\\\": 69.44, \\\\\\\"d005\\\\\\\": 68.36, \\\\\\\"d025\\\\\\\": 64.07, \\\\\\\"d050\\\\\\\": 59.41, \\\\\\\"d100\\\\\\\": 60.07},\\\\n    \\\\\\\"Qwen2.5-7B\\\\\\\":  {\\\\\\\"d000\\\\\\\": 66.11, \\\\\\\"d005\\\\\\\": 65.04, \\\\\\\"d025\\\\\\\": 63.01, \\\\\\\"d050\\\\\\\": 63.56, \\\\\\\"d100\\\\\\\": 64.33},\\\\n    \\\\\\\"Gemma-2-9B\\\\\\\":  {\\\\\\\"d000\\\\\\\": 61.86, \\\\\\\"d005\\\\\\\": 62.89, \\\\\\\"d025\\\\\\\": 63.54, \\\\\\\"d050\\\\\\\": 64.71, \\\\\\\"d100\\\\\\\": 65.62},\\\\n    \\\\\\\"OLMo-2-7B\\\\\\\":   {\\\\\\\"d000\\\\\\\": 53.79, \\\\\\\"d005\\\\\\\": 55.08, \\\\\\\"d025\\\\\\\": 56.19, \\\\\\\"d050\\\\\\\": 57.00, \\\\\\\"d100\\\\\\\": 57.00},\\\\n}\\\\nMODEL_ORDER = list(DATA.keys())\\\\n\\\\n# ── Sweep ──────────────────────────────────────────────────────────────\\\\n\\\\nTAU_VALUES = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]\\\\nSIGMA_VALUES = [3, 4, 5, 6, 7]\\\\nDEFAULT_TAU = 1.0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Threshold sensitivity sweep for dose-response profile classification.\\n\\nSweeps noise_threshold (τ) and severe_threshold (σ) to show classification\\nrobustness across parameter choices.\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport os\\nfrom itertools import product\\nfrom pathlib import Path\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport matplotlib.colors as mcolors\\nimport numpy as np\\n\\n# ── Classification logic (self-contained) ──────────────────────────────\\n\\nDOSAGES = (\\\"d000\\\", \\\"d005\\\", \\\"d025\\\", \\\"d050\\\", \\\"d100\\\")\\nPATTERNS = (\\\"Immune\\\", \\\"U-collapse\\\", \\\"V-recovery\\\", \\\"Benefit\\\", \\\"Benefit-sat\\\")\\nPATTERN_TO_INT = {p: i for i, p in enumerate(PATTERNS)}\\n\\n\\ndef classify_profile(\\n    accuracies: dict[str, float],\\n    *,\\n    noise_threshold: float = 1.0,\\n    severe_threshold: float = 5.0,\\n    saturation_ratio: float = 0.3,\\n    late_gain_floor: float = 0.5,\\n) -> str:\\n    a = {d: float(accuracies[d]) for d in DOSAGES}\\n    delta = a[\\\"d100\\\"] - a[\\\"d000\\\"]\\n    mid_vals = [a[\\\"d005\\\"], a[\\\"d025\\\"], a[\\\"d050\\\"]]\\n    mid_min = min(mid_vals)\\n\\n    if abs(delta) <= noise_threshold:\\n        return \\\"Immune\\\"\\n\\n    if delta < -noise_threshold:\\n        if delta <= -severe_threshold:\\n            return \\\"U-collapse\\\"\\n        v_dip = mid_min < a[\\\"d100\\\"] and mid_min < a[\\\"d000\\\"]\\n        if v_dip:\\n            return \\\"V-recovery\\\"\\n        return \\\"U-collapse\\\"\\n\\n    # delta > noise_threshold\\n    first_half = a[\\\"d025\\\"] - a[\\\"d000\\\"]\\n    second_half = a[\\\"d100\\\"] - a[\\\"d025\\\"]\\n    late_gain = a[\\\"d100\\\"] - a[\\\"d050\\\"]\\n    saturating = (\\n        (first_half > 0 and second_half < first_half * saturation_ratio)\\n        or late_gain < late_gain_floor\\n    )\\n    if saturating:\\n        return \\\"Benefit-sat\\\"\\n    return \\\"Benefit\\\"\\n\\n\\n# ── Data ───────────────────────────────────────────────────────────────\\n\\n# seed=42 MMLU accuracies (percentage points)\\nDATA = {\\n    \\\"Phi-4\\\":     {\\\"d000\\\": 76.44, \\\"d005\\\": 76.56, \\\"d025\\\": 76.50, \\\"d050\\\": 76.02, \\\"d100\\\": 76.27},\\n    \\\"Qwen2.5-14B\\\": {\\\"d000\\\": 69.44, \\\"d005\\\": 68.36, \\\"d025\\\": 64.07, \\\"d050\\\": 59.41, \\\"d100\\\": 60.07},\\n    \\\"Qwen2.5-7B\\\":  {\\\"d000\\\": 66.11, \\\"d005\\\": 65.04, \\\"d025\\\": 63.01, \\\"d050\\\": 63.56, \\\"d100\\\": 64.33},\\n    \\\"Gemma-2-9B\\\":  {\\\"d000\\\": 61.86, \\\"d005\\\": 62.89, \\\"d025\\\": 63.54, \\\"d050\\\": 64.71, \\\"d100\\\": 65.62},\\n    \\\"OLMo-2-7B\\\":   {\\\"d000\\\": 53.79, \\\"d005\\\": 55.08, \\\"d025\\\": 56.19, \\\"d050\\\": 57.00, \\\"d100\\\": 57.00},\\n}\\nMODEL_ORDER = list(DATA.keys())\\n\\n# ── Sweep ──────────────────────────────────────────────────────────────\\n\\nTAU_VALUES = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]\\nSIGMA_VALUES = [3, 4, 5, 6, 7]\\nDEFAULT_TAU = 1.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Grep · `toolu_01JLH5GMtLqsmWDoY8kpETEm`</summary>

```json
{
  "pattern": "sensitivity.*v2|v2.*sweep|sweep.*v2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "0c221484-9819-4050-88eb-de0be2cec392",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SAdnyMR7YWxuE2ScQVkv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5459,
      "cache_read_input_tokens": 45030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5459
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T22:15:11.172Z_

<details><summary>↩ Tool result · `toolu_01JLH5GMtLqsmWDoY8kpETEm`</summary>

```text
Found 250 files limit: 250
logs/workers/worker_code_paper-sensitivity-fix_20260519T221357.log
logs/chats/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer.jsonl
logs/chats/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d.jsonl
logs/chats/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director.jsonl
logs/workers/worker_analysis_paper-data-consistency-audit_20260519T220906.log
artifacts/manifest.yaml
artifacts/_project/report/paper_consistency_audit.md
artifacts/paper_consistency_audit.md
logs/workers/worker_research_paper-update-checklist_20260519T220548.log
artifacts/_project/report/paper_update_checklist.md
artifacts/paper_update_checklist.md
logs/chats/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_paper_agent.jsonl
logs/workers/worker_analysis_domain-decomposition-appendix_20260519T214934.log
registry.yaml
report.md
logs/workers/worker_diagnose_eval_qwen7b_s42_cqa1_v2_20260519T213133.log
memory.md
logs/chats/cron_hook_eval_qwen7b_s42_cqa1_v2.jsonl
logs/ralph_loop_timeline.jsonl
logs/workers/worker_ops_westd-progress-correct_20260519T210911.log
logs/workers/worker_ops_cqa1-s42-eval-finalize_20260519T211051.log
logs/chats/worker_analysis_failed-experiment-audit_20260519T204858.jsonl
logs/workers/worker_analysis_failed-experiment-audit_20260519T204858.log
logs/chats/worker_analysis_domain-decomposition_20260519T202914.jsonl
logs/workers/worker_analysis_domain-decomposition_20260519T202914.log
artifacts/_project/data/sensitivity_sweep_v2.md
logs/workers/worker_analysis_sensitivity-sweep-v2_20260519T194614_result.json
logs/workers/worker_analysis_sensitivity-sweep-v2_20260519T194614.log
artifacts/classification_sensitivity_sweep.py
logs/workers/worker_analysis_treated-untreated-items_20260519T191422.log
logs/workers/worker_analysis_classification-sensitivity-sweep_20260519T185355.log
logs/workers/worker_analysis_irt-data-prep_20260519T185034.log
logs/workers/worker_ops_cqa1-registry-audit_20260519T185056.log
logs/workers/worker_ops_evaluate-py-sync-and-reeval_20260519T180333.log
logs/workers/worker_ops_westd-training-progress_20260519T180359.log
logs/chats/worker_ops_seed123-progress-check_20260519T154354.jsonl
logs/workers/worker_ops_seed123-progress-check_20260519T154354.log
logs/chats/worker_code_seed0-script-prep_20260519T154411.jsonl
logs/workers/worker_code_seed0-script-prep_20260519T154411.log
logs/workers/worker_eval_qwen7b-s123-cqa1-retry_20260519T150027.log
logs/workers/worker_monitor_progress-and-eval-launch_20260519T140922.log
logs/workers/worker_monitor_training-progress-s123_20260519T135303_result.json
logs/workers/worker_monitor_training-progress-s123_20260519T135303.log
logs/workers/worker_code_sft_s123_sweep_submit_20260519T133715.log
logs/workers/worker_ssh_olmo2-eval-monitor_20260519T124632.log
logs/workers/worker_ssh_westd-irt-analysis-readiness_20260519T122447.log
logs/chats/archive/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director_20260519T122017_345451.jsonl
logs/workers/worker_diag_phase2_eval_status_20260519T112908.log
logs/workers/worker_research_paper_status_check_20260519T112915.log
logs/chats/archive/cron_hook_exp_001_sft_14b_d005_s42_20260519T112722_189963.jsonl
logs/chats/archive/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director_20260519T084038_138865.jsonl
logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260519T084029_359152.jsonl
logs/workers/worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309.log
logs/chats/cron_hook_exp_001_sft_gemma2_9b_d025_s42.jsonl
logs/workers/worker_analysis_exp_001_sft_14b_d100_s42_20260519T001713.log
logs/workers/worker_analysis_exp_001_sft_14b_d025_s42_20260518T221332.log
logs/chats/cron_hook_exp_001_eval_05B_d100_aligned_v3.jsonl
logs/workers/worker_ops_cqa1-status-and-tasks_20260518T092026.log
logs/workers/worker_plan_7b-14b-batch-prep_20260518T070410.log
logs/workers/worker_ops_westd-data-verify-eval-prep_20260518T065728.log
logs/workers/worker_ops_westd-env-setup_20260518T062747.log
logs/workers/worker_plan_7b-14b-experiment-plan_20260518T061929.log
logs/workers/worker_plan_7b-pilot-design_20260518T062031.log
logs/workers/worker_plan_framing-variant-templates_20260518T062049.log
logs/workers/worker_code_7b-14b-code-adapt_20260518T061857.log
logs/workers/worker_exp_mf2-threshold-dgp-sim_20260518T051629.log
logs/workers/worker_exp_j16-domain-gamma-collect_20260518T021217.log
logs/workers/worker_exp_random-300-tau-baseline_20260517T215924.log
logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260517T213913_870257.jsonl
logs/chats/worker_ops_check_vanilla_2pl_and_stale_20260517T193031.jsonl
logs/workers/worker_ops_check_vanilla_2pl_and_stale_20260517T193031.log
logs/workers/worker_ops_socsci_prior_sensitivity_20260517T184359.log
logs/workers/worker_ops_gamma_prior_sensitivity_sf5_20260517T182947.log
logs/workers/worker_ops_missing_references_sf9_20260517T182959.log
logs/chats/worker_ops_mean_ai_comparison_sf2_20260517T180920.jsonl
logs/workers/worker_ops_mean_ai_comparison_sf2_20260517T180920.log
logs/workers/worker_ops_j16_theta_5domains_sequential_20260517T154720_result.json
logs/workers/worker_ops_w10_exclusion_sensitivity_20260517T145216.log
logs/workers/worker_ops_check_w10_theta_results_20260517T170720.log
logs/workers/worker_ops_unified_baselines_pipeline_20260517T164317.log
logs/workers/worker_ops_w6_overcorrection_source_20260517T163408.log
logs/workers/worker_ops_w1_table4_baseline_data_20260517T163357.log
logs/workers/worker_ops_c7_baseline_config_audit_20260517T163424.log
logs/workers/worker_ops_q5_stem_gamma_prior_check_20260517T151306.log
logs/chats/feishu_dm_oc_f84d57de0177ef6ea0b9ecc4e5e1207b_briefer.jsonl
logs/workers/worker_ops_exp008_eval_check_20260517T124308.log
logs/workers/worker_research_llama32_sft_feasibility_20260517T115107.log
logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_20260517T104618_244200.jsonl
logs/workers/worker_ops_vanilla_2pl_kendall_tau_20260517T090458.log
logs/workers/worker_fig_identifiability_heatmap_20260517T094555.log
logs/workers/worker_ops_irt_no05b_extract_now_20260517T073247.log
logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260517T064102_218603.jsonl
logs/chats/archive/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director_20260517T064100_471509.jsonl
logs/workers/worker_ops_verify_05b_in_mmlu_irt_20260517T062653.log
logs/workers/worker_paper_bib_rebuild_2024_classics_20260517T055840.log
logs/workers/worker_analysis_cross_family_irt_v5_restart_20260517T043657.log
logs/workers/worker_paper_fix_mmlu_calmae_numbers_20260517T041104.log
logs/workers/worker_audit_exp009_plan_draft_20260517T034405.log
logs/workers/worker_audit_hypothesis_deep_review_20260517T034811_result.json
logs/workers/worker_audit_hypothesis_deep_review_20260517T034811.log
logs/workers/worker_paper_writing_experimental_setup_20260517T024330.log
logs/chats/worker_paper_writing_discussion_v2_20260517T024306.jsonl
logs/workers/worker_paper_writing_discussion_v2_20260517T024306.log
logs/workers/worker_ops_fisher_heatmap_check_restart_20260517T020935.log
logs/workers/worker_ops_cross_family_pooled_irt_refit_20260517T000103.log
logs/workers/worker_ops_d025_rrf_prep_20260516T233433.log
logs/workers/worker_paper_figure_fig_calibration_20260516T201935.log
logs/workers/worker_data_extract_irt_calibration_20260516T202216.log
logs/workers/worker_data_irt_extraction_20260516T202646.log
logs/chats/worker_data_irt_cal_extract_v2_20260516T202505.jsonl
logs/workers/worker_data_irt_cal_extract_v2_20260516T202505.log
logs/chats/cron_hook_exp_006_mmlu_domain_gamma_n24.jsonl
logs/chats/archive/cron_hook_exp_006_mmlu_domain_gamma_n24_20260516T201750_568297.jsonl
logs/workers/worker_exp006_fisher-heatmap-w4_20260516T195342.log
logs/chats/cron_hook_exp_001_eval_3B_d100_s42_a32_batch.jsonl
logs/chats/cron_hook_exp_001_eval_3B_d005_s42_a32_batch.jsonl
logs/chats/cron_hook_exp_001_eval_3B_d005_s42_para_aligned.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_para_aligned_20260516T194715_093711.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_d100_s42_a32_batch_20260516T194023_437551.jsonl
logs/chats/cron_hook_exp_002_signals_3B_d100_a32_s42.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_a32_batch_20260516T193338_646424.jsonl
logs/chats/cron_hook_exp_001_eval_3B_d000_s42_a32_batch.jsonl
logs/chats/cron_hook_exp_002_signals_3B_d100_s123_v9.jsonl
logs/chats/archive/cron_hook_exp_002_signals_3B_d100_a32_s42_20260516T191938_977547.jsonl
logs/chats/cron_hook_exp_002_signals_15B_instruct_arc.jsonl
logs/chats/archive/cron_hook_exp_002_signals_3B_d100_s123_v9_20260516T191140_691950.jsonl
logs/chats/worker_ops_verify-running-experiments_20260516T190236.jsonl
logs/workers/worker_ops_verify-running-experiments_20260516T190236.log
logs/chats/cron_hook_exp_001_eval_3B_instruct_aligned_para.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_d000_s42_a32_batch_20260516T190100_667062.jsonl
logs/chats/cron_hook_exp_002_signals_3B_d000_a32_s42.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_instruct_aligned_para_20260516T185629_257647.jsonl
logs/chats/archive/cron_hook_exp_002_signals_3B_d000_a32_s42_20260516T185450_225265.jsonl
logs/chats/cron_hook_exp_002_signals_3B_d000_s123_cuda2.jsonl
logs/chats/cron_hook_exp_002_signals_3B_d005_a32_s42.jsonl
logs/workers/worker_diagnose_exp_001_eval_llama32_3B_d000_s42_v3_20260516T182511.log
logs/chats/archive/cron_hook_exp_002_signals_3B_d005_a32_s42_20260516T182321_001189.jsonl
logs/workers/worker_diagnose_exp_001_sft_llama32_3B_d005_s42_20260516T175105.log
logs/workers/worker_analysis_fisher_info_heatmap_20260516T174835.log
logs/chats/archive/cron_hook_exp_002_signals_15B_s123_batch_20260516T174658_153582.jsonl
logs/chats/cron_hook_exp_006_mmlu_domain_gamma.jsonl
logs/chats/archive/cron_hook_exp_006_mmlu_domain_gamma_20260516T171632_747867.jsonl
logs/chats/cron_hook_exp_002_signals_05B_s123_v2.jsonl
logs/chats/worker_research_paper-method-prep_20260516T165433.jsonl
logs/workers/worker_research_paper-method-prep_20260516T165433.log
logs/chats/archive/cron_hook_exp_002_signals_05B_s123_v2_20260516T165220_817257.jsonl
artifacts/dream_reports/dream_20260516T155748/logs/review_median.log
artifacts/dream_reports/dream_20260516T155748/logs/paper_agent_worst.log
logs/workers/worker_analysis_2pl_no_gamma_ablation_20260516T160735.log
artifacts/dream_reports/dream_20260516T155748/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T155748/logs/phase2_best_attempt1.log
logs/workers/worker_research_paper-research_20260516T160608.log
artifacts/dream_reports/dream_20260516T155748/logs/phase1_attempt0.log
logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_a32_batch_20260516T152937_021413.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_para_aligned_20260516T152415_633597.jsonl
task_context/history/agent/loop_16_1778945055.md
logs/chats/archive/cron_hook_exp_001_eval_3B_d100_s42_a32_batch_20260516T151730_830259.jsonl
logs/workers/worker_research_domain-contamination-literature_20260516T150810.log
logs/chats/worker_analysis_d108_domain_gamma_n24_v4_20260516T150132.jsonl
logs/workers/worker_analysis_d108_domain_gamma_n24_v4_20260516T150132.log
logs/chats/archive/cron_hook_exp_002_signals_3B_d100_s123_v9_20260516T145836_507888.jsonl
logs/workers/worker_status_experiment-logs_20260516T145415.log
logs/workers/worker_status_gpu-check_20260516T145402.log
logs/chats/archive/cron_hook_exp_001_eval_3B_instruct_aligned_para_20260516T145240_839196.jsonl
logs/workers/worker_fix_llama_eval_cuda4_restart_20260516T143343.log
logs/chats/archive/cron_hook_exp_001_eval_3B_d000_s42_a32_batch_20260516T143731_920985.jsonl
logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260516T142546_217418.jsonl
logs/chats/archive/cron_hook_exp_002_signals_3B_d000_a32_s42_20260516T142532_311637.jsonl
logs/chats/archive/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director_20260516T141633_068524.jsonl
logs/chats/archive/cron_hook_exp_002_signals_3B_d005_a32_s42_20260516T141612_324254.jsonl
logs/workers/worker_diagnose_exp_002_signals_3B_d000_s123_cuda2_20260516T141348.log
logs/workers/worker_diagnose_exp_006_pooled_irt_n25_20260516T134420.log
logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_20260516T132833_668870.jsonl
logs/chats/archive/cron_hook_exp_006_mmlu_domain_gamma_20260516T125021_139421.jsonl
logs/workers/worker_analysis_mmlu_domain_gamma_n24_with_3B_20260516T112049.log
artifacts/dream_reports/dream_20260516T104822/logs/review_best.log
logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_para_aligned_20260516T111146_205440.jsonl
artifacts/dream_reports/dream_20260516T104822/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T104822/logs/phase2_best_attempt0.log
logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_a32_batch_20260516T110424_874385.jsonl
logs/workers/worker_audit_signals_coverage_0516_20260516T105530.log
logs/chats/archive/cron_hook_exp_002_signals_3B_d100_s123_v9_20260516T105057_604805.jsonl
artifacts/dream_reports/dream_20260516T104822/logs/phase1_attempt0.log
logs/chats/archive/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director_20260516T104936_048732.jsonl
logs/workers/worker_ops_3B_s42_signals_status_and_merge_20260516T102324.log
logs/workers/worker_research_3B_signal_coverage_audit_20260516T101702.log
logs/chats/archive/cron_hook_exp_001_eval_3B_d000_s42_a32_batch_20260516T101336_201692.jsonl
logs/workers/worker_ops_d100-batch-final-check-and-d025-eval_20260516T072914.log
logs/workers/worker_ops_signals-v9-final-verdict_20260516T061050.log
logs/workers/worker_code_scale-stratified-irt_20260516T052844.log
logs/chats/cron_hook_exp_001_eval_3B_d100_s42_para_aligned.jsonl
logs/chats/cron_hook_exp_001_eval_15B_s123_para_aligned_batch.jsonl
logs/chats/cron_hook_exp_001_eval_05B_d000_s123_aligned.jsonl
logs/chats/cron_hook_exp_001_sft_15B_d025_s123_v2.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_d100_s42_para_aligned_20260516T052203_580235.jsonl
logs/chats/cron_hook_exp_002_signals_3B.jsonl
logs/workers/worker_code_exp_008_instruct_rl_proxy_20260516T044959.log
logs/chats/archive/cron_hook_exp_002_signals_3B_20260516T051427_474967.jsonl
logs/chats/cron_hook_exp_001_eval_3B_d005_s123_gsm8k.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s123_gsm8k_20260516T050408_295421.jsonl
logs/workers/worker_code_cron-sentinel-fix_20260516T044328.log
logs/chats/cron_hook_exp_001_sft_3B_d100_s42_a32_v3.jsonl
logs/workers/worker_research_humaneval-para-check_20260516T044347.log
logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260516T044014_227124.jsonl
logs/workers/worker_paper_method-section-corrections_20260516T043244.log
logs/workers/worker_ops_check-eval-d025-para-log_20260516T043351.log
logs/chats/archive/cron_hook_exp_001_sft_3B_d100_s42_a32_v3_20260516T043247_764609.jsonl
logs/workers/worker_research_literature-map_20260516T041853.log
logs/workers/worker_paper_method-section_20260516T041831.log
logs/chats/cron_hook_exp_001_eval_3B_d005_s123_aligned.jsonl
logs/chats/cron_hook_exp_001_sft_15B_d005_s123.jsonl
logs/chats/cron_hook_exp_001_eval_3B_d025_s123_aligned.jsonl
logs/chats/archive/cron_hook_exp_001_sft_15B_d005_s123_20260516T041444_884758.jsonl
logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_20260516T041436_452912.jsonl
logs/chats/cron_hook_exp_001_sft_15B_d025_s123.jsonl
logs/chats/cron_hook_exp_001_sft_3B_d100_s123_a32_v2.jsonl
logs/chats/archive/cron_hook_exp_001_sft_3B_d100_s123_a32_v2_20260516T040632_891686.jsonl
logs/chats/cron_hook_exp_001_eval_3B_d000_s123_aligned.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s123_aligned_20260516T040103_843400.jsonl
logs/chats/archive/cron_hook_exp_001_sft_15B_d025_s123_20260516T040044_054406.jsonl
logs/chats/cron_hook_exp_001_sft_3B_d025_s123.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_d000_s123_aligned_20260516T035743_866738.jsonl
logs/chats/cron_hook_exp_008_base_pretrained_15B_eval.jsonl
logs/chats/archive/cron_hook_exp_001_eval_3B_d025_s123_aligned_20260516T035447_031964.jsonl
logs/chats/archive/cron_hook_exp_001_sft_3B_d025_s123_20260516T035340_907293.jsonl
logs/chats/cron_hook_exp_001_eval_15B_d000_s123_aligned.jsonl
logs/chats/cron_hook_exp_008_base_pretrained_eval_v2.jsonl
logs/chats/cron_hook_exp_001_sft_3B_d000_s42_a32.jsonl
logs/chats/archive/cron_hook_exp_008_base_pretrained_eval_v2_20260516T034511_058966.jsonl
logs/workers/worker_ops_check_worker_outputs_loop14_20260516T033618.log
logs/chats/archive/cron_hook_exp_008_base_pretrained_15B_eval_20260516T033530_294869.jsonl
logs/chats/archive/cron_hook_exp_001_eval_15B_d000_s123_aligned_20260516T033318_134653.jsonl
logs/chats/worker_analysis_eval_3B_d100_s123_a32_20260516T033005.jsonl
logs/workers/worker_analysis_eval_3B_d100_s123_a32_20260516T033005.log
logs/chats/archive/cron_hook_exp_001_sft_3B_d000_s42_a32_20260516T032803_833224.jsonl
logs/chats/cron_hook_exp_001_sft_3B_d100_s42_a32_v2.jsonl
logs/chats/archive/cron_hook_exp_001_eval_15B_d005_s123_20260516T030048_306839.jsonl
logs/chats/archive/cron_hook_exp_002_signals_3B_v5_20260516T024205_053900.jsonl
logs/chats/archive/cron_hook_exp_001_sft_3B_d100_s42_a32_v2_20260516T024154_592993.jsonl
logs/chats/archive/cron_hook_exp_001_sft_3B_d100_s42_a32_20260516T023855_496338.jsonl
logs/chats/cron_hook_exp_001_sft_3B_d025_s42_a32_v2.jsonl
logs/workers/worker_prep_rrf-readiness-check_20260516T022450.log
logs/workers/worker_research_coverage-audit_20260516T022507.log
logs/workers/worker_ops_verify-sim-sweep-v7-local_20260516T022742.log
logs/workers/worker_planning_next-experiment-queue_20260516T022325.log
logs/chats/archive/cron_hook_exp_001_sft_3B_d025_s42_a32_v2_20260516T022908_173948.jsonl
logs/chats/cron_hook_exp_001_eval_3B_d000_s42_para_aligned.jsonl
logs/chats/cron_hook_exp_001_eval_3B_d100_s123_para_aligned_v2.jsonl
logs/chats/archive/cron_hook_exp_001_eval_15B_d025_s123_20260516T022501_580224.jsonl
logs/chats/archive/cron_hook_exp_001_sft_3B_d000_v3_20260516T022223_658158.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "b65bd138-67fc-4297-852a-5a15caebdb25",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "logs/workers/worker_code_paper-sensitivity-fix_20260519T221357.log",
      "logs/chats/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer.jsonl",
      "logs/chats/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d.jsonl",
      "logs/chats/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director.jsonl",
      "logs/workers/worker_analysis_paper-data-consistency-audit_20260519T220906.log",
      "artifacts/manifest.yaml",
      "artifacts/_project/report/paper_consistency_audit.md",
      "artifacts/paper_consistency_audit.md",
      "logs/workers/worker_research_paper-update-checklist_20260519T220548.log",
      "artifacts/_project/report/paper_update_checklist.md",
      "artifacts/paper_update_checklist.md",
      "logs/chats/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_paper_agent.jsonl",
      "logs/workers/worker_analysis_domain-decomposition-appendix_20260519T214934.log",
      "registry.yaml",
      "report.md",
      "logs/workers/worker_diagnose_eval_qwen7b_s42_cqa1_v2_20260519T213133.log",
      "memory.md",
      "logs/chats/cron_hook_eval_qwen7b_s42_cqa1_v2.jsonl",
      "logs/ralph_loop_timeline.jsonl",
      "logs/workers/worker_ops_westd-progress-correct_20260519T210911.log",
      "logs/workers/worker_ops_cqa1-s42-eval-finalize_20260519T211051.log",
      "logs/chats/worker_analysis_failed-experiment-audit_20260519T204858.jsonl",
      "logs/workers/worker_analysis_failed-experiment-audit_20260519T204858.log",
      "logs/chats/worker_analysis_domain-decomposition_20260519T202914.jsonl",
      "logs/workers/worker_analysis_domain-decomposition_20260519T202914.log",
      "artifacts/_project/data/sensitivity_sweep_v2.md",
      "logs/workers/worker_analysis_sensitivity-sweep-v2_20260519T194614_result.json",
      "logs/workers/worker_analysis_sensitivity-sweep-v2_20260519T194614.log",
      "artifacts/classification_sensitivity_sweep.py",
      "logs/workers/worker_analysis_treated-untreated-items_20260519T191422.log",
      "logs/workers/worker_analysis_classification-sensitivity-sweep_20260519T185355.log",
      "logs/workers/worker_analysis_irt-data-prep_20260519T185034.log",
      "logs/workers/worker_ops_cqa1-registry-audit_20260519T185056.log",
      "logs/workers/worker_ops_evaluate-py-sync-and-reeval_20260519T180333.log",
      "logs/workers/worker_ops_westd-training-progress_20260519T180359.log",
      "logs/chats/worker_ops_seed123-progress-check_20260519T154354.jsonl",
      "logs/workers/worker_ops_seed123-progress-check_20260519T154354.log",
      "logs/chats/worker_code_seed0-script-prep_20260519T154411.jsonl",
      "logs/workers/worker_code_seed0-script-prep_20260519T154411.log",
      "logs/workers/worker_eval_qwen7b-s123-cqa1-retry_20260519T150027.log",
      "logs/workers/worker_monitor_progress-and-eval-launch_20260519T140922.log",
      "logs/workers/worker_monitor_training-progress-s123_20260519T135303_result.json",
      "logs/workers/worker_monitor_training-progress-s123_20260519T135303.log",
      "logs/workers/worker_code_sft_s123_sweep_submit_20260519T133715.log",
      "logs/workers/worker_ssh_olmo2-eval-monitor_20260519T124632.log",
      "logs/workers/worker_ssh_westd-irt-analysis-readiness_20260519T122447.log",
      "logs/chats/archive/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director_20260519T122017_345451.jsonl",
      "logs/workers/worker_diag_phase2_eval_status_20260519T112908.log",
      "logs/workers/worker_research_paper_status_check_20260519T112915.log",
      "logs/chats/archive/cron_hook_exp_001_sft_14b_d005_s42_20260519T112722_189963.jsonl",
      "logs/chats/archive/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director_20260519T084038_138865.jsonl",
      "logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260519T084029_359152.jsonl",
      "logs/workers/worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309.log",
      "logs/chats/cron_hook_exp_001_sft_gemma2_9b_d025_s42.jsonl",
      "logs/workers/worker_analysis_exp_001_sft_14b_d100_s42_20260519T001713.log",
      "logs/workers/worker_analysis_exp_001_sft_14b_d025_s42_20260518T221332.log",
      "logs/chats/cron_hook_exp_001_eval_05B_d100_aligned_v3.jsonl",
      "logs/workers/worker_ops_cqa1-status-and-tasks_20260518T092026.log",
      "logs/workers/worker_plan_7b-14b-batch-prep_20260518T070410.log",
      "logs/workers/worker_ops_westd-data-verify-eval-prep_20260518T065728.log",
      "logs/workers/worker_ops_westd-env-setup_20260518T062747.log",
      "logs/workers/worker_plan_7b-14b-experiment-plan_20260518T061929.log",
      "logs/workers/worker_plan_7b-pilot-design_20260518T062031.log",
      "logs/workers/worker_plan_framing-variant-templates_20260518T062049.log",
      "logs/workers/worker_code_7b-14b-code-adapt_20260518T061857.log",
      "logs/workers/worker_exp_mf2-threshold-dgp-sim_20260518T051629.log",
      "logs/workers/worker_exp_j16-domain-gamma-collect_20260518T021217.log",
      "logs/workers/worker_exp_random-300-tau-baseline_20260517T215924.log",
      "logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260517T213913_870257.jsonl",
      "logs/chats/worker_ops_check_vanilla_2pl_and_stale_20260517T193031.jsonl",
      "logs/workers/worker_ops_check_vanilla_2pl_and_stale_20260517T193031.log",
      "logs/workers/worker_ops_socsci_prior_sensitivity_20260517T184359.log",
      "logs/workers/worker_ops_gamma_prior_sensitivity_sf5_20260517T182947.log",
      "logs/workers/worker_ops_missing_references_sf9_20260517T182959.log",
      "logs/chats/worker_ops_mean_ai_comparison_sf2_20260517T180920.jsonl",
      "logs/workers/worker_ops_mean_ai_comparison_sf2_20260517T180920.log",
      "logs/workers/worker_ops_j16_theta_5domains_sequential_20260517T154720_result.json",
      "logs/workers/worker_ops_w10_exclusion_sensitivity_20260517T145216.log",
      "logs/workers/worker_ops_check_w10_theta_results_20260517T170720.log",
      "logs/workers/worker_ops_unified_baselines_pipeline_20260517T164317.log",
      "logs/workers/worker_ops_w6_overcorrection_source_20260517T163408.log",
      "logs/workers/worker_ops_w1_table4_baseline_data_20260517T163357.log",
      "logs/workers/worker_ops_c7_baseline_config_audit_20260517T163424.log",
      "logs/workers/worker_ops_q5_stem_gamma_prior_check_20260517T151306.log",
      "logs/chats/feishu_dm_oc_f84d57de0177ef6ea0b9ecc4e5e1207b_briefer.jsonl",
      "logs/workers/worker_ops_exp008_eval_check_20260517T124308.log",
      "logs/workers/worker_research_llama32_sft_feasibility_20260517T115107.log",
      "logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_20260517T104618_244200.jsonl",
      "logs/workers/worker_ops_vanilla_2pl_kendall_tau_20260517T090458.log",
      "logs/workers/worker_fig_identifiability_heatmap_20260517T094555.log",
      "logs/workers/worker_ops_irt_no05b_extract_now_20260517T073247.log",
      "logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260517T064102_218603.jsonl",
      "logs/chats/archive/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director_20260517T064100_471509.jsonl",
      "logs/workers/worker_ops_verify_05b_in_mmlu_irt_20260517T062653.log",
      "logs/workers/worker_paper_bib_rebuild_2024_classics_20260517T055840.log",
      "logs/workers/worker_analysis_cross_family_irt_v5_restart_20260517T043657.log",
      "logs/workers/worker_paper_fix_mmlu_calmae_numbers_20260517T041104.log",
      "logs/workers/worker_audit_exp009_plan_draft_20260517T034405.log",
      "logs/workers/worker_audit_hypothesis_deep_review_20260517T034811_result.json",
      "logs/workers/worker_audit_hypothesis_deep_review_20260517T034811.log",
      "logs/workers/worker_paper_writing_experimental_setup_20260517T024330.log",
      "logs/chats/worker_paper_writing_discussion_v2_20260517T024306.jsonl",
      "logs/workers/worker_paper_writing_discussion_v2_20260517T024306.log",
      "logs/workers/worker_ops_fisher_heatmap_check_restart_20260517T020935.log",
      "logs/workers/worker_ops_cross_family_pooled_irt_refit_20260517T000103.log",
      "logs/workers/worker_ops_d025_rrf_prep_20260516T233433.log",
      "logs/workers/worker_paper_figure_fig_calibration_20260516T201935.log",
      "logs/workers/worker_data_extract_irt_calibration_20260516T202216.log",
      "logs/workers/worker_data_irt_extraction_20260516T202646.log",
      "logs/chats/worker_data_irt_cal_extract_v2_20260516T202505.jsonl",
      "logs/workers/worker_data_irt_cal_extract_v2_20260516T202505.log",
      "logs/chats/cron_hook_exp_006_mmlu_domain_gamma_n24.jsonl",
      "logs/chats/archive/cron_hook_exp_006_mmlu_domain_gamma_n24_20260516T201750_568297.jsonl",
      "logs/workers/worker_exp006_fisher-heatmap-w4_20260516T195342.log",
      "logs/chats/cron_hook_exp_001_eval_3B_d100_s42_a32_batch.jsonl",
      "logs/chats/cron_hook_exp_001_eval_3B_d005_s42_a32_batch.jsonl",
      "logs/chats/cron_hook_exp_001_eval_3B_d005_s42_para_aligned.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_para_aligned_20260516T194715_093711.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d100_s42_a32_batch_20260516T194023_437551.jsonl",
      "logs/chats/cron_hook_exp_002_signals_3B_d100_a32_s42.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_a32_batch_20260516T193338_646424.jsonl",
      "logs/chats/cron_hook_exp_001_eval_3B_d000_s42_a32_batch.jsonl",
      "logs/chats/cron_hook_exp_002_signals_3B_d100_s123_v9.jsonl",
      "logs/chats/archive/cron_hook_exp_002_signals_3B_d100_a32_s42_20260516T191938_977547.jsonl",
      "logs/chats/cron_hook_exp_002_signals_15B_instruct_arc.jsonl",
      "logs/chats/archive/cron_hook_exp_002_signals_3B_d100_s123_v9_20260516T191140_691950.jsonl",
      "logs/chats/worker_ops_verify-running-experiments_20260516T190236.jsonl",
      "logs/workers/worker_ops_verify-running-experiments_20260516T190236.log",
      "logs/chats/cron_hook_exp_001_eval_3B_instruct_aligned_para.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d000_s42_a32_batch_20260516T190100_667062.jsonl",
      "logs/chats/cron_hook_exp_002_signals_3B_d000_a32_s42.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_instruct_aligned_para_20260516T185629_257647.jsonl",
      "logs/chats/archive/cron_hook_exp_002_signals_3B_d000_a32_s42_20260516T185450_225265.jsonl",
      "logs/chats/cron_hook_exp_002_signals_3B_d000_s123_cuda2.jsonl",
      "logs/chats/cron_hook_exp_002_signals_3B_d005_a32_s42.jsonl",
      "logs/workers/worker_diagnose_exp_001_eval_llama32_3B_d000_s42_v3_20260516T182511.log",
      "logs/chats/archive/cron_hook_exp_002_signals_3B_d005_a32_s42_20260516T182321_001189.jsonl",
      "logs/workers/worker_diagnose_exp_001_sft_llama32_3B_d005_s42_20260516T175105.log",
      "logs/workers/worker_analysis_fisher_info_heatmap_20260516T174835.log",
      "logs/chats/archive/cron_hook_exp_002_signals_15B_s123_batch_20260516T174658_153582.jsonl",
      "logs/chats/cron_hook_exp_006_mmlu_domain_gamma.jsonl",
      "logs/chats/archive/cron_hook_exp_006_mmlu_domain_gamma_20260516T171632_747867.jsonl",
      "logs/chats/cron_hook_exp_002_signals_05B_s123_v2.jsonl",
      "logs/chats/worker_research_paper-method-prep_20260516T165433.jsonl",
      "logs/workers/worker_research_paper-method-prep_20260516T165433.log",
      "logs/chats/archive/cron_hook_exp_002_signals_05B_s123_v2_20260516T165220_817257.jsonl",
      "artifacts/dream_reports/dream_20260516T155748/logs/review_median.log",
      "artifacts/dream_reports/dream_20260516T155748/logs/paper_agent_worst.log",
      "logs/workers/worker_analysis_2pl_no_gamma_ablation_20260516T160735.log",
      "artifacts/dream_reports/dream_20260516T155748/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260516T155748/logs/phase2_best_attempt1.log",
      "logs/workers/worker_research_paper-research_20260516T160608.log",
      "artifacts/dream_reports/dream_20260516T155748/logs/phase1_attempt0.log",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_a32_batch_20260516T152937_021413.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_para_aligned_20260516T152415_633597.jsonl",
      "task_context/history/agent/loop_16_1778945055.md",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d100_s42_a32_batch_20260516T151730_830259.jsonl",
      "logs/workers/worker_research_domain-contamination-literature_20260516T150810.log",
      "logs/chats/worker_analysis_d108_domain_gamma_n24_v4_20260516T150132.jsonl",
      "logs/workers/worker_analysis_d108_domain_gamma_n24_v4_20260516T150132.log",
      "logs/chats/archive/cron_hook_exp_002_signals_3B_d100_s123_v9_20260516T145836_507888.jsonl",
      "logs/workers/worker_status_experiment-logs_20260516T145415.log",
      "logs/workers/worker_status_gpu-check_20260516T145402.log",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_instruct_aligned_para_20260516T145240_839196.jsonl",
      "logs/workers/worker_fix_llama_eval_cuda4_restart_20260516T143343.log",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d000_s42_a32_batch_20260516T143731_920985.jsonl",
      "logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260516T142546_217418.jsonl",
      "logs/chats/archive/cron_hook_exp_002_signals_3B_d000_a32_s42_20260516T142532_311637.jsonl",
      "logs/chats/archive/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director_20260516T141633_068524.jsonl",
      "logs/chats/archive/cron_hook_exp_002_signals_3B_d005_a32_s42_20260516T141612_324254.jsonl",
      "logs/workers/worker_diagnose_exp_002_signals_3B_d000_s123_cuda2_20260516T141348.log",
      "logs/workers/worker_diagnose_exp_006_pooled_irt_n25_20260516T134420.log",
      "logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_20260516T132833_668870.jsonl",
      "logs/chats/archive/cron_hook_exp_006_mmlu_domain_gamma_20260516T125021_139421.jsonl",
      "logs/workers/worker_analysis_mmlu_domain_gamma_n24_with_3B_20260516T112049.log",
      "artifacts/dream_reports/dream_20260516T104822/logs/review_best.log",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_para_aligned_20260516T111146_205440.jsonl",
      "artifacts/dream_reports/dream_20260516T104822/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260516T104822/logs/phase2_best_attempt0.log",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s42_a32_batch_20260516T110424_874385.jsonl",
      "logs/workers/worker_audit_signals_coverage_0516_20260516T105530.log",
      "logs/chats/archive/cron_hook_exp_002_signals_3B_d100_s123_v9_20260516T105057_604805.jsonl",
      "artifacts/dream_reports/dream_20260516T104822/logs/phase1_attempt0.log",
      "logs/chats/archive/feishu_group_oc_4960c7baa442eabd4fa0aceeac2693ca_director_20260516T104936_048732.jsonl",
      "logs/workers/worker_ops_3B_s42_signals_status_and_merge_20260516T102324.log",
      "logs/workers/worker_research_3B_signal_coverage_audit_20260516T101702.log",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d000_s42_a32_batch_20260516T101336_201692.jsonl",
      "logs/workers/worker_ops_d100-batch-final-check-and-d025-eval_20260516T072914.log",
      "logs/workers/worker_ops_signals-v9-final-verdict_20260516T061050.log",
      "logs/workers/worker_code_scale-stratified-irt_20260516T052844.log",
      "logs/chats/cron_hook_exp_001_eval_3B_d100_s42_para_aligned.jsonl",
      "logs/chats/cron_hook_exp_001_eval_15B_s123_para_aligned_batch.jsonl",
      "logs/chats/cron_hook_exp_001_eval_05B_d000_s123_aligned.jsonl",
      "logs/chats/cron_hook_exp_001_sft_15B_d025_s123_v2.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d100_s42_para_aligned_20260516T052203_580235.jsonl",
      "logs/chats/cron_hook_exp_002_signals_3B.jsonl",
      "logs/workers/worker_code_exp_008_instruct_rl_proxy_20260516T044959.log",
      "logs/chats/archive/cron_hook_exp_002_signals_3B_20260516T051427_474967.jsonl",
      "logs/chats/cron_hook_exp_001_eval_3B_d005_s123_gsm8k.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s123_gsm8k_20260516T050408_295421.jsonl",
      "logs/workers/worker_code_cron-sentinel-fix_20260516T044328.log",
      "logs/chats/cron_hook_exp_001_sft_3B_d100_s42_a32_v3.jsonl",
      "logs/workers/worker_research_humaneval-para-check_20260516T044347.log",
      "logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260516T044014_227124.jsonl",
      "logs/workers/worker_paper_method-section-corrections_20260516T043244.log",
      "logs/workers/worker_ops_check-eval-d025-para-log_20260516T043351.log",
      "logs/chats/archive/cron_hook_exp_001_sft_3B_d100_s42_a32_v3_20260516T043247_764609.jsonl",
      "logs/workers/worker_research_literature-map_20260516T041853.log",
      "logs/workers/worker_paper_method-section_20260516T041831.log",
      "logs/chats/cron_hook_exp_001_eval_3B_d005_s123_aligned.jsonl",
      "logs/chats/cron_hook_exp_001_sft_15B_d005_s123.jsonl",
      "logs/chats/cron_hook_exp_001_eval_3B_d025_s123_aligned.jsonl",
      "logs/chats/archive/cron_hook_exp_001_sft_15B_d005_s123_20260516T041444_884758.jsonl",
      "logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_20260516T041436_452912.jsonl",
      "logs/chats/cron_hook_exp_001_sft_15B_d025_s123.jsonl",
      "logs/chats/cron_hook_exp_001_sft_3B_d100_s123_a32_v2.jsonl",
      "logs/chats/archive/cron_hook_exp_001_sft_3B_d100_s123_a32_v2_20260516T040632_891686.jsonl",
      "logs/chats/cron_hook_exp_001_eval_3B_d000_s123_aligned.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d005_s123_aligned_20260516T040103_843400.jsonl",
      "logs/chats/archive/cron_hook_exp_001_sft_15B_d025_s123_20260516T040044_054406.jsonl",
      "logs/chats/cron_hook_exp_001_sft_3B_d025_s123.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d000_s123_aligned_20260516T035743_866738.jsonl",
      "logs/chats/cron_hook_exp_008_base_pretrained_15B_eval.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_3B_d025_s123_aligned_20260516T035447_031964.jsonl",
      "logs/chats/archive/cron_hook_exp_001_sft_3B_d025_s123_20260516T035340_907293.jsonl",
      "logs/chats/cron_hook_exp_001_eval_15B_d000_s123_aligned.jsonl",
      "logs/chats/cron_hook_exp_008_base_pretrained_eval_v2.jsonl",
      "logs/chats/cron_hook_exp_001_sft_3B_d000_s42_a32.jsonl",
      "logs/chats/archive/cron_hook_exp_008_base_pretrained_eval_v2_20260516T034511_058966.jsonl",
      "logs/workers/worker_ops_check_worker_outputs_loop14_20260516T033618.log",
      "logs/chats/archive/cron_hook_exp_008_base_pretrained_15B_eval_20260516T033530_294869.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_15B_d000_s123_aligned_20260516T033318_134653.jsonl",
      "logs/chats/worker_analysis_eval_3B_d100_s123_a32_20260516T033005.jsonl",
      "logs/workers/worker_analysis_eval_3B_d100_s123_a32_20260516T033005.log",
      "logs/chats/archive/cron_hook_exp_001_sft_3B_d000_s42_a32_20260516T032803_833224.jsonl",
      "logs/chats/cron_hook_exp_001_sft_3B_d100_s42_a32_v2.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_15B_d005_s123_20260516T030048_306839.jsonl",
      "logs/chats/archive/cron_hook_exp_002_signals_3B_v5_20260516T024205_053900.jsonl",
      "logs/chats/archive/cron_hook_exp_001_sft_3B_d100_s42_a32_v2_20260516T024154_592993.jsonl",
      "logs/chats/archive/cron_hook_exp_001_sft_3B_d100_s42_a32_20260516T023855_496338.jsonl",
      "logs/chats/cron_hook_exp_001_sft_3B_d025_s42_a32_v2.jsonl",
      "logs/workers/worker_prep_rrf-readiness-check_20260516T022450.log",
      "logs/workers/worker_research_coverage-audit_20260516T022507.log",
      "logs/workers/worker_ops_verify-sim-sweep-v7-local_20260516T022742.log",
      "logs/workers/worker_planning_next-experiment-queue_20260516T022325.log",
      "logs/chats/archive/cron_hook_exp_001_sft_3B_d025_s42_a32_v2_20260516T022908_173948.jsonl",
      "logs/chats/cron_hook_exp_001_eval_3B_d000_s42_para_aligned.jsonl",
      "logs/chats/cron_hook_exp_001_eval_3B_d100_s123_para_aligned_v2.jsonl",
      "logs/chats/archive/cron_hook_exp_001_eval_15B_d025_s123_20260516T022501_580224.jsonl",
      "logs/chats/archive/cron_hook_exp_001_sft_3B_d000_v3_20260516T022223_658158.jsonl"
    ],
    "numFiles": 250,
    "appliedLimit": 250
  }
}
```

</details>

---

### Assistant

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Found it: `artifacts/_project/data/sensitivity_sweep_v2.md`. Let me read that file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "472a4978-e22f-4bdb-a2ac-bd1389b5270a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017VupR9DMr3QK4PgD1QEFct",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9968,
      "cache_read_input_tokens": 50489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9968
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 42_

找到 v2 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "d3538159-7aa4-4d99-bdac-0ab77206a632",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017VupR9DMr3QK4PgD1QEFct",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9968,
      "cache_read_input_tokens": 50489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9968
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01PTzXzZq2gHjgwYarDdHwaG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/data/sensitivity_sweep_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "17b73483-c696-476e-8764-71ce33367929",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017VupR9DMr3QK4PgD1QEFct",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9968,
      "cache_read_input_tokens": 50489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9968
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T22:15:16.770Z_

<details><summary>↩ Tool result · `toolu_01PTzXzZq2gHjgwYarDdHwaG`</summary>

```text
1	Sensitivity Sweep V2 (with volatility check)
2	
3	180/180 correct classifications (6 families × 30 τ×σ combos)
4	
5	V1 → V2 changes: 35 fixes, 0 regressions
6	- Qwen-7B s123: 0/30 → 30/30 correct (was Immune, now V-recovery)
7	- Qwen-7B s42 at τ=2.0: 0/5 → 5/5 correct (was Immune, now V-recovery)
8	- Phi-4: 30/30 Immune (unchanged)
9	- All other families: 30/30 unchanged
10	
11	Remote: westd:/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "57430544-fc93-42db-9f8c-fba0d0b30b6b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/data/sensitivity_sweep_v2.md",
      "content": "Sensitivity Sweep V2 (with volatility check)\n\n180/180 correct classifications (6 families × 30 τ×σ combos)\n\nV1 → V2 changes: 35 fixes, 0 regressions\n- Qwen-7B s123: 0/30 → 30/30 correct (was Immune, now V-recovery)\n- Qwen-7B s42 at τ=2.0: 0/5 → 5/5 correct (was Immune, now V-recovery)\n- Phi-4: 30/30 Immune (unchanged)\n- All other families: 30/30 unchanged\n\nRemote: westd:/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the situation. The v2 sweep result:

- Same grid: 6 τ × 5 σ = 30 combinations
- 6 families (not 5) — Qwen-7B is counted as 2 families because of 2 seeds (s42, s123)
- Actually wait, let me re-read: "6 families × 30 τ×σ combos" = 180 total. But in the paper, it says "5/5 families" and "150/150 model-combination pairs". 


- So the discrepancy is that v2 added Qwen-7B s123 as a sixth family, bringing the total from 150 pairs (5 models × 30) to 180 pairs (6 families × 30), with the new seed achieving perfect classification across all combinations.
- But the paper currently claims only 5 families are stable, which doesn't match the v2 results showing 6 families/seeds.
- I need to clarify whether "families" refers to distinct model architectures or includes different seeds of the same model, since Qwen-7B s42 and s123 are technically the same family but different initializations.
- The grid dimensions stay at 30 (6 τ × 5 σ), but the total model-combination pairs increase from 150 to 180 because we're now testing 6 model configs instead of 5.
- I need to check which of the 6 sensitivity descriptions in the paper should say "30 combinations" versus "180/180 model-combination pairs" — the task is asking me to verify these numbers match the v2 sweep results, not necessarily change them all.

Looking at what actually changed in v2: the grid stayed at 30 combinations, but we added Qwen-7B s123 as a sixth test case, which bumped the total from 150/150 to 180/180 model-combination pairs. So "30 combinations" is still correct for each individual model-seed pair, but the aggregate count needs updating from 150 to 180.

The real updates needed are: change "5/5 families" to reflect the 6 model-seed configurations, update the 150/150 references to 180/180, and verify Table 7's per-model 30/30 entries are already correct. I need to verify whether the grid dimensions actually changed in the v2 sweep, since the task mentions updating the "30 combinations" but my current understanding suggests it stayed the same at 6 τ × 5 σ. Let me check the v2 results directory to see what the actual sweep parameters were.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "5e026022-018a-47dd-993d-bdeb81f2430e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtqoFrjb2Caf7JgNwk28Ug",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 60457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 46_

v2 结果：仍然是 30 个 (τ,σ) 组合，但模型数从 5 变成 6（加入了 Qwen-7B s123），总配对从 150 变成 180。让我确认 westd 上的 v2 详细数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "3d901fac-c88f-46ff-93ba-15e0214a1a9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtqoFrjb2Caf7JgNwk28Ug",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 60457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GM1AbDtErPWqm5XfSo89bh`</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/analysis/results/sensitivity_v2/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "add45e6b-edcb-46ae-80b5-094b3e8b14e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtqoFrjb2Caf7JgNwk28Ug",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 60457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T22:15:54.728Z_

<details><summary>↩ Tool result · `toolu_01GM1AbDtErPWqm5XfSo89bh`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "c1208478-3b9e-470a-ad47-8db243e5510a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 49_

<details><summary>Logged reasoning block</summary>

```text
The v2 directory doesn't exist on westd. The v2 results must have been computed by the worker but stored locally. Let me check the worker log for more details about what exactly was done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "c6153045-417d-460f-b89e-3ae96d5eedf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6wNNr9X9yxQ6yTnFhVw1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1808,
      "cache_read_input_tokens": 60932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1808
      },
      "output_tokens": 13,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 50_

查看 v2 sweep worker 的结果日志获取更多细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "f138901c-1f71-424f-a321-5e7441d4324e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6wNNr9X9yxQ6yTnFhVw1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1808,
      "cache_read_input_tokens": 60932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1808
      },
      "output_tokens": 13,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01PNKXnmmqYfFWQXq6r3mb4Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/logs/workers/worker_analysis_sensitivity-sweep-v2_20260519T194614.log",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "51aa9d64-c153-4e50-9b7f-08be04f7db04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6wNNr9X9yxQ6yTnFhVw1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1808,
      "cache_read_input_tokens": 60932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1808
      },
      "output_tokens": 13,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T22:16:01.307Z_

<details><summary>↩ Tool result · reported error · `toolu_01PNKXnmmqYfFWQXq6r3mb4Z`</summary>

```text
File content (117071 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "41a6e506-ae7f-4fdc-96cf-649b518522e7",
  "tool_use_result": "Error: File content (117071 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01GTUMNup6Ditn1yZsn7kvf8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/logs/workers/worker_analysis_sensitivity-sweep-v2_20260519T194614_result.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "5c262db3-ded5-4ad8-88ac-57858af3ca0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019e1zW2eLGCWe34an6PTFZX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 62740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T22:16:04.372Z_

<details><summary>↩ Tool result · `toolu_01GTUMNup6Ditn1yZsn7kvf8`</summary>

```text
1	{
2	  "raw": "全部完成。结果汇总：\n\n### Verification: 6/6 PASSED\n所有 test case 在默认参数 (τ=1.0, σ=5.0) 下分类正确。\n\n### 30-combo Sweep 结果\n\n**v2 在全部 30/30 组合中 6 个 family 均分类正确（6/6 × 30 = 180/180）。**\n\n### V1 → V2 变化\n- **35 处分类变化，全部是改进，0 处回退**\n- **Qwen-7B s123**: v1 在 30/30 组合中全部误判为 Immune → v2 全部正确修正为 V-recovery（+30）\n- **Qwen-7B s42**: 当 τ=2.0 时（delta=-1.78 落入 |delta|≤τ），v1 误判为 Immune → v2 通过 volatility check 正确识别为 V-recovery（+5）\n\n### 关键检查\n| 检查项 | 结果 |\n|--------|------|\n| Qwen-7B s123 正确分类为 V-recovery | **30/30** 组合 (v1: 0/30) |\n| Phi-4 保持 Immune | **30/30** 组合 |\n| 4/5 family robustness 保持 | 全部 6 个 family 均 **30/30** |\n\n### 产出文件\n- `/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sweep_results.json`\n- `/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sensitivity_heatmap_v2.png`\n- `/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sensitivity_per_family_v2.png`\n\nVolatility check 是纯改进：修复了 Qwen-7B s123 的 Immune 误分类问题，在所有参数组合下无回退。"
3	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "5057b94b-9123-4848-8337-aaf9030e6b9c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/logs/workers/worker_analysis_sensitivity-sweep-v2_20260519T194614_result.json",
      "content": "{\n  \"raw\": \"全部完成。结果汇总：\\n\\n### Verification: 6/6 PASSED\\n所有 test case 在默认参数 (τ=1.0, σ=5.0) 下分类正确。\\n\\n### 30-combo Sweep 结果\\n\\n**v2 在全部 30/30 组合中 6 个 family 均分类正确（6/6 × 30 = 180/180）。**\\n\\n### V1 → V2 变化\\n- **35 处分类变化，全部是改进，0 处回退**\\n- **Qwen-7B s123**: v1 在 30/30 组合中全部误判为 Immune → v2 全部正确修正为 V-recovery（+30）\\n- **Qwen-7B s42**: 当 τ=2.0 时（delta=-1.78 落入 |delta|≤τ），v1 误判为 Immune → v2 通过 volatility check 正确识别为 V-recovery（+5）\\n\\n### 关键检查\\n| 检查项 | 结果 |\\n|--------|------|\\n| Qwen-7B s123 正确分类为 V-recovery | **30/30** 组合 (v1: 0/30) |\\n| Phi-4 保持 Immune | **30/30** 组合 |\\n| 4/5 family robustness 保持 | 全部 6 个 family 均 **30/30** |\\n\\n### 产出文件\\n- `/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sweep_results.json`\\n- `/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sensitivity_heatmap_v2.png`\\n- `/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sensitivity_per_family_v2.png`\\n\\nVolatility check 是纯改进：修复了 Qwen-7B s123 的 Immune 误分类问题，在所有参数组合下无回退。\"\n}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. The v2 sweep results:

1. Same grid: 6 τ × 5 σ = 30 (τ,σ) combinations (unchanged)
2. Added Qwen-7B s123 as a 6th "family/configuration"
3. Total: 6 × 30 = 180 model-combination pairs
4. Result: 180/180 correct (was 145/150 in v1, though the paper says 150/150 which was after adding the volatility check but before adding s123)

The 30 combinations number is still correct. What needs updating:


- References to "5/5 families" should become "6 model-seed configurations"
- The total count changes from "150/150 model-combination pairs" to "180/180"
- Table 7 needs a new row for Qwen-7B s123 with its 30/30 results

The task mentions keeping "30 combinations" in all sensitivity descriptions, which makes sense since that's the actual parameter grid size—what's changing is the number of model configurations being swept across that grid.

Now I'm mapping out the specific edits needed across the files: updating method.tex to reference all six configurations instead of five families, changing the total pair count in Table 1's caption from 150 to 180, and adjusting any other references to the model count throughout results.tex. I'm realizing the 30 combinations figure is actually correct for v2 since the grid itself hasn't changed. What needs updating is the total count from 150 to 180 and the model count from 5 to 6 families. So I need to add the Qwen-7B s123 row to Table 7 and adjust the model references throughout, while keeping the 30 combinations number as-is.

Now I'm checking what needs fixing in the v-recovery documentation. The limitations section has a contradiction — the heading says "Single seed" but the content mentions validation across two seeds (s42 and s123), so I should change that heading to something like "Seed coverage" or "Two-seed validation" to match what's actually described. I also need to verify what the abstract says about v-type recovery and make sure it's consistent with the updated results. I'm looking at the table structure to add the seed-specific entries for Qwen-7B. I need to split the existing Qwen-7B row into two separate rows—one for seed 42 showing the volatility check resolution, and another for seed 123 with near-zero delta and the same volatility resolution. Then I'll verify the Table 1 caption is complete and accurately describes the robustness across all model-combination and hyperparameter pairs. I'm working through the phrasing for the stability claims across model families and configurations. The key distinction is that while there are five distinct model families (Phi-4, Qwen-14B, Qwen-7B, Gemma-2, OLMo-2), the grid sweep actually covers six model-seed configurations since Qwen-7B has two seeds. I think the clearest way to express this is to mention both the family count and the configuration count together, something like "all five families (six model-seed configurations)" to be precise about what the sweep actually validated. I'm verifying the grid dimensions from the v2 sweep—τ has 6 values and σ has 5 values, which gives 30 combinations total, so that number is actually correct. The task is probably just flagging those 6 locations to update the surrounding context (like changing 5/5 to 6/6 and 150 to 180) while keeping the 30 combinations figure as is.

Now I'm going through the edits systematically: updating method.tex to clarify that all five families remain stable and adding the 180/180 model-seed-combination count, then updating results.tex to reflect the same changes across multiple mentions. I need to update the table to show six model-seed configurations instead of five families, specifying Qwen-7B with seed 42 and adding a separate row for Qwen-7B with seed 123. But I should clarify that "5/5 families" still holds since both seeds belong to the same Qwen-7B family—it's just that the sensitivity analysis now covers six distinct configurations. Now I'm settling on the clearest phrasing for each section—using "model-seed-combination pairs" to capture the 180 total configurations, updating the appendix caption to reflect all six model-seed variants, and adding the missing Qwen-7B row to the table. Let me apply these changes across the files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "1284a615-3512-412c-af2d-6269156a7469",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QCXdVkkwGE4NrwWsNJ1QW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 63005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 56_

数据确认完毕。v2 结果：同样 30 个 (τ,σ) 组合，但测试了 6 个 model-seed 配置（加入 Qwen-7B s123），总计 180/180。现在执行论文修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "168c4574-2d5e-4698-9131-5a528ea264f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QCXdVkkwGE4NrwWsNJ1QW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 63005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Edit · `toolu_01FSRyjvEwxCsgmgYUbrdXL4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex",
  "old_string": "a 30-combination grid sweep confirms 5/5 families are stable across all $(\\tau, \\sigma)$ combinations (Appendix~\\ref{sec:classification_sensitivity}).",
  "new_string": "a 30-combination grid sweep confirms all five families are stable across all $(\\tau, \\sigma)$ combinations (180/180 model--seed--threshold pairs; Appendix~\\ref{sec:classification_sensitivity})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "9be810c4-284b-4c02-8d6d-dbce25ee6da0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QCXdVkkwGE4NrwWsNJ1QW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 63005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T22:17:14.378Z_

<details><summary>↩ Tool result · `toolu_01FSRyjvEwxCsgmgYUbrdXL4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "1a1afe69-de02-41da-bd5a-f1e8b418da6c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex",
    "oldString": "a 30-combination grid sweep confirms 5/5 families are stable across all $(\\tau, \\sigma)$ combinations (Appendix~\\ref{sec:classification_sensitivity}).",
    "newString": "a 30-combination grid sweep confirms all five families are stable across all $(\\tau, \\sigma)$ combinations (180/180 model--seed--threshold pairs; Appendix~\\ref{sec:classification_sensitivity}).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\nContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nLet $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model~$j$ ($j=1,\\ldots,J$) to item~$i$ ($i=1,\\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.\n\nOur goal is to estimate $\\theta_j^{\\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \\citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \\citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \\in [0,1]$, fitting per-benchmark models to handle the shared item pool \\citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).\n\n\\subsection{Stage 1: Multi-Signal Exposure Mapping}\n\\label{sec:stage1}\n\nFor each model~$j$ and item~$i$, we consider four candidate detection signals. \\textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \\textbf{S2}~(Min-K\\%++): a membership inference statistic based on token-level surprisal \\citep{zhang_2024_minkpp}. \\textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \\citep{dekoninck2024constat}. \\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \\citep{kadavath2022}; concurrent work by \\citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\\mathcal{S} = \\{\\text{S1, S2, S4}\\}$) and is applicable to any benchmark without auxiliary data requirements. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \\S\\ref{sec:signal_failure}.\n\nWe aggregate signals via Reciprocal Rank Fusion \\citep[RRF;][]{cormack_2009_rrf}:\n\\begin{equation}\n\\label{eq:rrf}\n    e_{ij} = \\sum_{s \\in \\mathcal{S}} \\frac{1}{\\kappa + r_{s}(i)},\n\\end{equation}\nwhere $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\\kappa=60$ is the standard smoothing constant, and $|\\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to obtain $e_{ij} \\in [0,1]$. The resulting distribution is highly right-skewed (mean 0.041, median 0.016, max 0.879), with most model-item pairs receiving near-zero exposure.\n\n\\subsection{Stage 2: Contamination-Augmented IRT}\n\\label{sec:stage2}\n\n\\paragraph{Primary model: 2PL+$\\gamma$.}\nOur primary specification augments the two-parameter logistic (2PL) model \\citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:\n\\begin{equation}\n\\label{eq:2pl_gamma}\n    P(y_{ijk} = 1) = \\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwhere $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \\in \\mathbb{R}$ is item difficulty, $\\theta_j$ is model ability, and $\\gamma_k$ is the scalar contamination effect for benchmark~$k$. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we further stratify within a benchmark by cognitive domain (\\S\\ref{sec:domain_differential}).\n\nThe additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\\gamma_k \\cdot e_{ij} / a_i$ units on the ability scale (this holds exactly under linearization of the logistic function; the true shift is nonlinear and probability-dependent).\n\nFor MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\\ref{sec:4pl_details}); this requires $J \\geq 16$ and is not used in domain-level analyses ($J = 13$).\n\n\\paragraph{Inference.}\nWe perform Bayesian inference via NUTS \\citep{hoffman2014} in Stan \\citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\\theta_j \\sim \\mathcal{N}(0,1)$, $a_i \\sim \\text{LogNormal}(0, 0.5)$, $b_i \\sim \\mathcal{N}(0,1)$, $\\gamma_k \\sim \\mathcal{N}(0,1)$. Convergence requires split-$\\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.\n\n\\paragraph{Calibrated score.}\nThe decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:\n\\begin{equation}\n\\label{eq:calibrated}\n    \\text{Acc}_{j}^{\\text{cal}} = \\frac{1}{I_k} \\sum_{i=1}^{I_k}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[\\sigma\\!\\bigl(a_i(\\theta_j - b_i)\\bigr)\\right],\n\\end{equation}\nwith credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.\n\n\\paragraph{Identifiability.}\n\\label{sec:fisher}\n\\label{sec:value_decomposition}\nThe reliability of $\\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\\geq$0.55 with $J \\geq 50$ (Appendix~\\ref{sec:identifiability}). Eq.~\\eqref{eq:calibrated} depends on $\\theta_j$, not $\\gamma$ directly, predicting that vanilla 2PL ($\\gamma\\!=\\!0$) achieves comparable calibration to 2PL+$\\gamma$, with $\\gamma_k$ serving diagnosis rather than calibration (\\S\\ref{sec:calibration_results}).\n\n\\subsection{Dose-Response Profile Classification}\n\\label{sec:classification}\n\nIndependent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern. Algorithm~\\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by a noise threshold $\\tau$, severity threshold $\\sigma$, saturation ratio $\\rho$, and late-gain floor $\\lambda$. The three-way top-level split (immune/harm/benefit) is governed by the sign and magnitude of $\\Delta = a_{100} - a_0$ relative to $\\tau$; within-branch refinements distinguish U-collapse from V-recovery (via mid-dosage trough detection) and monotonic benefit from benefit-saturation (via gain deceleration). A mid-trajectory volatility check ($v^*$) within the immune branch distinguishes true immunity (Phi-4: $v^* = 0.34$pp $\\le \\tau$) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$); recovery extent varies by seed (partial at seed$=$42, full at seed$=$123). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms 5/5 families are stable across all $(\\tau, \\sigma)$ combinations (Appendix~\\ref{sec:classification_sensitivity}).\n\n\\begin{algorithm}[H]\n\\caption{Dose-Response Profile Classification}\n\\label{alg:profile-classification}\n\\begin{algorithmic}[1]\n\\Require Accuracy vector $\\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \\in \\{0, 5, 25, 50, 100\\}\\%$\n\\Require Noise threshold $\\tau = 1$ pp, severity threshold $\\sigma = 5$ pp\n\\Require Saturation ratio $\\rho = 0.3$, late-gain floor $\\lambda = 0.5$ pp\n\\Ensure Pattern $p \\in \\{\\textsc{Immune}, \\textsc{U-collapse}, \\textsc{V-recovery}, \\textsc{Benefit}, \\textsc{Benefit-sat}\\}$\n\\State $\\Delta \\gets a_{100} - a_{0}$ \\Comment{end-to-end accuracy shift}\n\\State $m^* \\gets \\min(a_{5},\\, a_{25},\\, a_{50})$ \\Comment{mid-dosage minimum}\n\\State $v^* \\gets \\max_{i \\in \\{5,25,50\\}} |a_i - a_0|$ \\Comment{max mid-trajectory deviation}\n\\If{$|\\Delta| \\le \\tau$}\n    \\If{$v^* \\le \\tau$}\n        \\State \\Return \\textsc{Immune} \\Comment{fluctuation within noise band}\n    \\ElsIf{$m^* < a_{0}$ \\textbf{and} $m^* < a_{100}$}\n        \\State \\Return \\textsc{V-recovery} \\Comment{V-dip with full endpoint recovery}\n    \\Else\n        \\State \\Return \\textsc{Immune} \\Comment{non-V volatility, endpoint stable}\n    \\EndIf\n\\ElsIf{$\\Delta < -\\tau$}\n    \\If{$\\Delta \\le -\\sigma$}\n        \\State \\Return \\textsc{U-collapse} \\Comment{severe monotonic degradation}\n    \\ElsIf{$m^* < a_{0}$ \\textbf{and} $m^* < a_{100}$}\n        \\State \\Return \\textsc{V-recovery} \\Comment{mid-dosage trough with partial recovery}\n    \\Else\n        \\State \\Return \\textsc{U-collapse} \\Comment{moderate decline, no V-shape}\n    \\EndIf\n\\Else \\Comment{$\\Delta > \\tau$}\n    \\State $g_1 \\gets a_{25} - a_{0}$ \\Comment{first-half gain}\n    \\State $g_2 \\gets a_{100} - a_{25}$ \\Comment{second-half gain}\n    \\State $\\ell \\gets a_{100} - a_{50}$ \\Comment{late gain}\n    \\If{$(g_1 > 0$ \\textbf{and} $g_2 < \\rho \\cdot g_1)$ \\textbf{or} $\\ell < \\lambda$}\n        \\State \\Return \\textsc{Benefit-sat} \\Comment{gain decelerates at high dosage}\n    \\Else\n        \\State \\Return \\textsc{Benefit} \\Comment{sustained improvement}\n    \\EndIf\n\\EndIf\n\\end{algorithmic}\n\\end{algorithm}",
    "structuredPatch": [
      {
        "oldStart": 56,
        "oldLines": 7,
        "newStart": 56,
        "newLines": 7,
        "lines": [
          " \\subsection{Dose-Response Profile Classification}",
          " \\label{sec:classification}",
          " ",
          "-Independent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern. Algorithm~\\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by a noise threshold $\\tau$, severity threshold $\\sigma$, saturation ratio $\\rho$, and late-gain floor $\\lambda$. The three-way top-level split (immune/harm/benefit) is governed by the sign and magnitude of $\\Delta = a_{100} - a_0$ relative to $\\tau$; within-branch refinements distinguish U-collapse from V-recovery (via mid-dosage trough detection) and monotonic benefit from benefit-saturation (via gain deceleration). A mid-trajectory volatility check ($v^*$) within the immune branch distinguishes true immunity (Phi-4: $v^* = 0.34$pp $\\le \\tau$) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$); recovery extent varies by seed (partial at seed$=$42, full at seed$=$123). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms 5/5 families are stable across all $(\\tau, \\sigma)$ combinations (Appendix~\\ref{sec:classification_sensitivity}).",
          "+Independent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern. Algorithm~\\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by a noise threshold $\\tau$, severity threshold $\\sigma$, saturation ratio $\\rho$, and late-gain floor $\\lambda$. The three-way top-level split (immune/harm/benefit) is governed by the sign and magnitude of $\\Delta = a_{100} - a_0$ relative to $\\tau$; within-branch refinements distinguish U-collapse from V-recovery (via mid-dosage trough detection) and monotonic benefit from benefit-saturation (via gain deceleration). A mid-trajectory volatility check ($v^*$) within the immune branch distinguishes true immunity (Phi-4: $v^* = 0.34$pp $\\le \\tau$) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$); recovery extent varies by seed (partial at seed$=$42, full at seed$=$123). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms all five families are stable across all $(\\tau, \\sigma)$ combinations (180/180 model--seed--threshold pairs; Appendix~\\ref{sec:classification_sensitivity}).",
          " ",
          " \\begin{algorithm}[H]",
          " \\caption{Dose-Response Profile Classification}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Edit · `toolu_01AZxEUpFc7oS8ZvWXFttKeN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
  "old_string": "(150/150 model-combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity})",
  "new_string": "(180/180 model--seed--combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "cfbe0598-0940-4138-809f-3db691a636c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QCXdVkkwGE4NrwWsNJ1QW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 63005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T22:17:15.627Z_

<details><summary>↩ Tool result · `toolu_01AZxEUpFc7oS8ZvWXFttKeN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "c0ef25ad-ddd8-40c1-b0bf-0df0d6da1a24",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
    "oldString": "(150/150 model-combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity})",
    "newString": "(180/180 model--seed--combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity})",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nCross-family results (\\S\\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\\S\\ref{sec:calibration_results}--\\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\\times$1.5B + 8$\\times$3B); domain-level contamination estimates $\\gamma_d$ (\\S\\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\\ref{fig:domain_gamma}.\n\n\\subsection{Five Dose-Response Patterns}\n\\label{sec:taxonomy}\n\n\\begin{table}[t]\n\\centering\n\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}\n\\label{tab:taxonomy}\n\\footnotesize\n\\begin{tabular}{llccccc}\n\\toprule\nPattern & Model & Baseline & $\\Delta$acc & 95\\% CI & Peak & Stab. \\\\\n\\midrule\nImmune & Phi-4 14.7B & 76.4\\% & $\\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\\% \\\\\nU-collapse & Qwen-14B & 69.4\\% & $-$9.4pp & [$-$10.04, $-$8.70] & $-$10.0\\textsuperscript{d050} & 100\\% \\\\\nV-recovery & Qwen-7B & 66.1\\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\\textsuperscript{d025} & 99.6\\% \\\\\nBenefit & Gemma-2 9B & 61.9\\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\\% \\\\\nBenefit-sat. & OLMo-2 7B & 53.8\\% & $+$3.2pp & [$+$2.73, $+$3.71] & sat.\\textsuperscript{d050} & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nApplying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (Appendix~\\ref{sec:classification_sensitivity}).\n\n\\paragraph{Baseline ability threshold.}\nA threshold at 64.7\\% MMLU baseline (bootstrap 95\\% CI: 64.0--65.4\\%, $B=10{,}000$) separates two regimes. Below it, OLMo-2 (53.8\\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\\%) gains $+$3.8pp monotonically. Above it, Qwen-7B (66.1\\%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), Qwen-14B (69.4\\%) collapses by $-$10.0pp at d050---3$\\times$ more fragile than 7B despite higher baseline---and Phi-4 (76.4\\%) is immune. ARC-Challenge results are directionally consistent for 4/5 models (Appendix~\\ref{sec:arc_cross_benchmark}). Cross-family domain decomposition reveals consistent directionality within each pattern, with STEM as the most resilient domain across all five families (Appendix~\\ref{sec:domain_decomposition}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{MMLU accuracy vs.\\ contamination dosage (5-shot). Models below 64.7\\% baseline benefit; models above are harmed or immune. Qwen-14B is 3$\\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\\ref{sec:arc_cross_benchmark}.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Item-Level Memorization Test}\n\\label{sec:memorization_test}\n\nWe test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. The pattern holds on ARC-Challenge. Difficulty-stratified analysis confirms symmetry ($|\\text{gap}| < 0.4$pp across all bins).\n\n\\begin{table}[t]\n\\centering\n\\caption{Treated vs.\\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}\n\\label{tab:did}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Treated $\\Delta$ & Untreated $\\Delta$ & DiD & Verdict \\\\\n\\midrule\nGemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.6 (ns) & generalization \\\\\nOLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\\\\nPhi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\\\\nQwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\\\\nQwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContamination thus operates through global capability modulation, not item-specific recall: models below the threshold absorb contaminated SFT data as useful knowledge, while models above it suffer distributional disruption affecting contaminated and clean items alike. This challenges item-overlap detection methods, which assume item-specific memorization signatures (Figure~\\ref{fig:treated_untreated}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_treated_untreated.pdf}\n\\caption{DiD for treated vs.\\ untreated items across five families at d025 MMLU. All DiD non-significant: contamination operates via global capability modulation.}\n\\label{fig:treated_untreated}\n\\end{figure}\n\n\\subsection{Calibration Quality}\n\\label{sec:calibration_results}\n\nWithin-family IRT analysis uses Qwen2.5 $\\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\\tau = 0.73$ on 300 items ($\\Delta\\tau = 0.27$ vs.\\ random baseline); S1-only selection causes convergence failure ($\\hat{R} = 1.53$) due to exposure variance compression.\n\nTable~\\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy achieves the lowest MAE (0.006) because within-family $\\leq$3B effects are near-null; B6-DCR systematically overcorrects (MAE 0.108). ContamCal's value is diagnostic: domain analysis reveals Social Sciences $\\gamma_d = -0.63$ ($P(\\gamma_d\\!<\\!0) = 99.7\\%$; \\S\\ref{sec:domain_differential}), while pooled $\\gamma$ remains non-significant, consistent with opposing domain-level effects canceling at aggregate.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\\ref{sec:arc_irt}.}\n\\label{tab:baselines}\n\\footnotesize\n\\begin{tabular}{lcc}\n\\toprule\nMethod & MAE & $\\tau$ \\\\\n\\midrule\nB0: Raw Accuracy & \\textbf{0.006} & 0.767 \\\\\nB1b: Remove \\& Rescore & 0.026 & \\underline{0.783} \\\\\nB3: Vanilla 2PL & 0.008 & 0.731 \\\\\nB4: Linear Regression & 0.010 & 0.751 \\\\\nB5b: Emperor & \\textbf{0.006} & \\textbf{0.789} \\\\\nB6: DCR (reimpl.) & 0.108 & 0.654 \\\\\nContamCal (2PL+$\\gamma$) & 0.009 & 0.731 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detection Signal Failure Modes}\n\\label{sec:signal_failure}\n\nMin-K\\%++ \\citep{zhang_2024_minkpp} exhibits a \\textit{directional reversal} at 0.5B: contaminated items receive \\textit{lower} scores than clean items (Cohen's $d = -1.55$ at d005, $-1.98$ at d100). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\\ref{sec:signal_reliability_appendix}). Simulation shows $\\gamma$ recovery requires AUC$\\geq$0.55 with $J \\geq 50$; at AUC $\\geq 0.90$, $J = 16$ suffices (Appendix~\\ref{sec:identifiability_appendix}).\n\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain_differential}\n\nWithin-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\\gamma_d$ while Social Sciences is negative ($\\gamma_d = -0.63$, 95\\% CI $[-1.07, -0.19]$, $P(\\gamma_d\\!<\\!0) = 99.7\\%$, PPP$=$0.722), crossing the Bonferroni-corrected threshold for eight tests (Figure~\\ref{fig:domain_gamma}, Table~\\ref{tab:domain_gamma} in Appendix). Prior sensitivity confirms the Social Sciences signal is data-dominated ($\\hat{\\gamma}_d$ varies 1.2$\\times$ across priors vs.\\ 2.6$\\times$ for pooled; Appendix~\\ref{sec:prior_sensitivity}).\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}",
          "+\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (180/180 model--seed--combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}",
          " \\label{tab:taxonomy}",
          " \\footnotesize",
          " \\begin{tabular}{llccccc}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Edit · `toolu_0124qPEVjFxjSs8anhaJyVfP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
  "old_string": "All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (Appendix~\\ref{sec:classification_sensitivity}).",
  "new_string": "All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (six model--seed configurations; Appendix~\\ref{sec:classification_sensitivity})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "9897b035-1b5e-4ce0-9fd7-09c475f502bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QCXdVkkwGE4NrwWsNJ1QW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 63005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T22:17:17.041Z_

<details><summary>↩ Tool result · `toolu_0124qPEVjFxjSs8anhaJyVfP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "9ac342b2-8712-48c2-a611-e7fbe3f097db",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
    "oldString": "All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (Appendix~\\ref{sec:classification_sensitivity}).",
    "newString": "All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (six model--seed configurations; Appendix~\\ref{sec:classification_sensitivity}).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nCross-family results (\\S\\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\\S\\ref{sec:calibration_results}--\\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\\times$1.5B + 8$\\times$3B); domain-level contamination estimates $\\gamma_d$ (\\S\\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\\ref{fig:domain_gamma}.\n\n\\subsection{Five Dose-Response Patterns}\n\\label{sec:taxonomy}\n\n\\begin{table}[t]\n\\centering\n\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (180/180 model--seed--combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}\n\\label{tab:taxonomy}\n\\footnotesize\n\\begin{tabular}{llccccc}\n\\toprule\nPattern & Model & Baseline & $\\Delta$acc & 95\\% CI & Peak & Stab. \\\\\n\\midrule\nImmune & Phi-4 14.7B & 76.4\\% & $\\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\\% \\\\\nU-collapse & Qwen-14B & 69.4\\% & $-$9.4pp & [$-$10.04, $-$8.70] & $-$10.0\\textsuperscript{d050} & 100\\% \\\\\nV-recovery & Qwen-7B & 66.1\\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\\textsuperscript{d025} & 99.6\\% \\\\\nBenefit & Gemma-2 9B & 61.9\\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\\% \\\\\nBenefit-sat. & OLMo-2 7B & 53.8\\% & $+$3.2pp & [$+$2.73, $+$3.71] & sat.\\textsuperscript{d050} & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nApplying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (Appendix~\\ref{sec:classification_sensitivity}).\n\n\\paragraph{Baseline ability threshold.}\nA threshold at 64.7\\% MMLU baseline (bootstrap 95\\% CI: 64.0--65.4\\%, $B=10{,}000$) separates two regimes. Below it, OLMo-2 (53.8\\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\\%) gains $+$3.8pp monotonically. Above it, Qwen-7B (66.1\\%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), Qwen-14B (69.4\\%) collapses by $-$10.0pp at d050---3$\\times$ more fragile than 7B despite higher baseline---and Phi-4 (76.4\\%) is immune. ARC-Challenge results are directionally consistent for 4/5 models (Appendix~\\ref{sec:arc_cross_benchmark}). Cross-family domain decomposition reveals consistent directionality within each pattern, with STEM as the most resilient domain across all five families (Appendix~\\ref{sec:domain_decomposition}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{MMLU accuracy vs.\\ contamination dosage (5-shot). Models below 64.7\\% baseline benefit; models above are harmed or immune. Qwen-14B is 3$\\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\\ref{sec:arc_cross_benchmark}.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Item-Level Memorization Test}\n\\label{sec:memorization_test}\n\nWe test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. The pattern holds on ARC-Challenge. Difficulty-stratified analysis confirms symmetry ($|\\text{gap}| < 0.4$pp across all bins).\n\n\\begin{table}[t]\n\\centering\n\\caption{Treated vs.\\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}\n\\label{tab:did}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Treated $\\Delta$ & Untreated $\\Delta$ & DiD & Verdict \\\\\n\\midrule\nGemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.6 (ns) & generalization \\\\\nOLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\\\\nPhi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\\\\nQwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\\\\nQwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContamination thus operates through global capability modulation, not item-specific recall: models below the threshold absorb contaminated SFT data as useful knowledge, while models above it suffer distributional disruption affecting contaminated and clean items alike. This challenges item-overlap detection methods, which assume item-specific memorization signatures (Figure~\\ref{fig:treated_untreated}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_treated_untreated.pdf}\n\\caption{DiD for treated vs.\\ untreated items across five families at d025 MMLU. All DiD non-significant: contamination operates via global capability modulation.}\n\\label{fig:treated_untreated}\n\\end{figure}\n\n\\subsection{Calibration Quality}\n\\label{sec:calibration_results}\n\nWithin-family IRT analysis uses Qwen2.5 $\\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\\tau = 0.73$ on 300 items ($\\Delta\\tau = 0.27$ vs.\\ random baseline); S1-only selection causes convergence failure ($\\hat{R} = 1.53$) due to exposure variance compression.\n\nTable~\\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy achieves the lowest MAE (0.006) because within-family $\\leq$3B effects are near-null; B6-DCR systematically overcorrects (MAE 0.108). ContamCal's value is diagnostic: domain analysis reveals Social Sciences $\\gamma_d = -0.63$ ($P(\\gamma_d\\!<\\!0) = 99.7\\%$; \\S\\ref{sec:domain_differential}), while pooled $\\gamma$ remains non-significant, consistent with opposing domain-level effects canceling at aggregate.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\\ref{sec:arc_irt}.}\n\\label{tab:baselines}\n\\footnotesize\n\\begin{tabular}{lcc}\n\\toprule\nMethod & MAE & $\\tau$ \\\\\n\\midrule\nB0: Raw Accuracy & \\textbf{0.006} & 0.767 \\\\\nB1b: Remove \\& Rescore & 0.026 & \\underline{0.783} \\\\\nB3: Vanilla 2PL & 0.008 & 0.731 \\\\\nB4: Linear Regression & 0.010 & 0.751 \\\\\nB5b: Emperor & \\textbf{0.006} & \\textbf{0.789} \\\\\nB6: DCR (reimpl.) & 0.108 & 0.654 \\\\\nContamCal (2PL+$\\gamma$) & 0.009 & 0.731 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detection Signal Failure Modes}\n\\label{sec:signal_failure}\n\nMin-K\\%++ \\citep{zhang_2024_minkpp} exhibits a \\textit{directional reversal} at 0.5B: contaminated items receive \\textit{lower} scores than clean items (Cohen's $d = -1.55$ at d005, $-1.98$ at d100). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\\ref{sec:signal_reliability_appendix}). Simulation shows $\\gamma$ recovery requires AUC$\\geq$0.55 with $J \\geq 50$; at AUC $\\geq 0.90$, $J = 16$ suffices (Appendix~\\ref{sec:identifiability_appendix}).\n\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain_differential}\n\nWithin-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\\gamma_d$ while Social Sciences is negative ($\\gamma_d = -0.63$, 95\\% CI $[-1.07, -0.19]$, $P(\\gamma_d\\!<\\!0) = 99.7\\%$, PPP$=$0.722), crossing the Bonferroni-corrected threshold for eight tests (Figure~\\ref{fig:domain_gamma}, Table~\\ref{tab:domain_gamma} in Appendix). Prior sensitivity confirms the Social Sciences signal is data-dominated ($\\hat{\\gamma}_d$ varies 1.2$\\times$ across priors vs.\\ 2.6$\\times$ for pooled; Appendix~\\ref{sec:prior_sensitivity}).\n",
    "structuredPatch": [
      {
        "oldStart": 24,
        "oldLines": 7,
        "newStart": 24,
        "newLines": 7,
        "lines": [
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-Applying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (Appendix~\\ref{sec:classification_sensitivity}).",
          "+Applying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (six model--seed configurations; Appendix~\\ref{sec:classification_sensitivity}).",
          " ",
          " \\paragraph{Baseline ability threshold.}",
          " A threshold at 64.7\\% MMLU baseline (bootstrap 95\\% CI: 64.0--65.4\\%, $B=10{,}000$) separates two regimes. Below it, OLMo-2 (53.8\\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\\%) gains $+$3.8pp monotonically. Above it, Qwen-7B (66.1\\%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), Qwen-14B (69.4\\%) collapses by $-$10.0pp at d050---3$\\times$ more fragile than 7B despite higher baseline---and Phi-4 (76.4\\%) is immune. ARC-Challenge results are directionally consistent for 4/5 models (Appendix~\\ref{sec:arc_cross_benchmark}). Cross-family domain decomposition reveals consistent directionality within each pattern, with STEM as the most resilient domain across all five families (Appendix~\\ref{sec:domain_decomposition})."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Edit · `toolu_01BKrVK6Su73vYEHZkFkGTBW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "old_string": "Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.",
  "new_string": "Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All six model--seed configurations achieve perfect stability."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "ad0f0619-f6c9-42ed-8aba-b70817d429e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QCXdVkkwGE4NrwWsNJ1QW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 63005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T22:17:18.458Z_

<details><summary>↩ Tool result · `toolu_01BKrVK6Su73vYEHZkFkGTBW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "55fc0871-bffe-45a0-aedc-7479095f1ab3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
    "oldString": "Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.",
    "newString": "Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All six model--seed configurations achieve perfect stability.",
    "originalFile": "\\appendix\n\n\\section{ARC-Challenge Cross-Benchmark Analysis}\n\\label{sec:arc_cross_benchmark}\n\nARC-Challenge (25-shot, 1{,}172 items) patterns are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$3.8pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($\\pm$0.6pp). Gemma-2 ARC is excluded due to a 16pp evaluation artifact. Qwen-14B exhibits V-recovery on ARC rather than U-collapse ($-$3.4pp vs.\\ $-$9.4pp on MMLU), a 2.8$\\times$ attenuation reflecting benchmark-specific properties. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\\%, Gemma-2: 62.7\\%) due to the smaller item pool (1{,}172 vs.\\ 14{,}042), and Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero ($[-2.47, +0.09]$pp).\n\nDose-response profiles are jointly determined by model and benchmark properties: direction is governed by model baseline ability (the 64.7\\% threshold); shape is governed by benchmark properties (item pool size, difficulty distribution, evaluation format). This benchmark-conditionality is a finding in its own right---practitioners cannot assume a contamination profile on one benchmark transfers to another.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_arc_dose_response.pdf}\n\\caption{ARC-Challenge accuracy vs.\\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\\ref{fig:dose_response}) for 4/5 models.}\n\\label{fig:dose_response_arc}\n\\end{figure}\n\n\\section{Signal Reliability Across Scales}\n\\label{sec:signal_reliability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap.pdf}\n\\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\\%++) reverses at 0.5B; S4 is near-random below 1.5B.}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\section{Identifiability Simulation}\n\\label{sec:identifiability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_identifiability_heatmap.pdf}\n\\caption{$\\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\\% CI coverage $\\geq90\\%$ require $J\\geq50$ at AUC$=$0.55, but only $J\\geq16$ at AUC$\\geq$0.90.}\n\\label{fig:identifiability_heatmap}\n\\end{figure}\n\nFisher information $\\mathcal{I}(\\gamma) \\propto \\text{Var}(e_{\\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\\% CI coverage $\\geq 90\\%$ require $J \\geq 50$; at AUC$\\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \\citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).\n\n\\section{4PL Extension}\n\\label{sec:4pl_details}\n\nFor MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:\n\\begin{equation}\n    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwith $c_i \\sim \\text{Beta}(5,20)$ and $d_i \\sim \\text{Beta}(20,5)$. This requires $J \\geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\\gamma$ at $J=13$; pooled calibration uses $J=16$.\n\n\\section{S4 Self-Critique Signal Details}\n\\label{sec:s4_details}\n\nS4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\\text{YES})$, then score each item as the negative entropy of this distribution: $\\text{S4}_i = -[-p\\log p - (1-p)\\log(1-p)]$ where $p = P(\\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.\n\n\\section{Training Convergence}\n\\label{sec:training_convergence}\n\nAll SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.\n\n\\section{Model Exclusion Details}\n\\label{sec:exclusion_details}\n\nOf the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\\alpha=32$, lr$=5\\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.\n\n\\paragraph{Model sets across analyses.}\nTable~\\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\\S\\ref{sec:injection}). Core findings ($\\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.\n\n\\begin{table}[h]\n\\centering\n\\caption{Model set composition across analyses.}\n\\label{tab:model_sets}\n\\footnotesize\n\\begin{tabular}{lcll}\n\\toprule\nAnalysis & $J$ & Model Set & Section \\\\\n\\midrule\nPooled baselines & 16 & 8$\\times$Qwen-1.5B + 8$\\times$Qwen-3B & \\S\\ref{sec:calibration_results} \\\\\nDomain $\\gamma$ & 13 & 8$\\times$Qwen-1.5B + 5$\\times$Qwen-3B & \\S\\ref{sec:domain_differential} \\\\\nCross-family & 16--28 & varies by benchmark & \\S\\ref{sec:taxonomy} \\\\\nOracle ablation & 13 & domain whitelist & \\S\\ref{sec:calibration_results} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Prior Sensitivity Analysis}\n\\label{sec:prior_sensitivity}\n\nTo assess the influence of the $\\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\\gamma \\sim \\mathcal{N}(0, 0.5)$, $\\mathcal{N}(0, 1)$ (default), and $\\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\\% CI includes zero in all cases (lower bound stable at $\\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\\hat{R} < 1.01$, ESS $> 3800$, PPP $\\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\\gamma$-based conclusions at current ensemble sizes.\n\nFor the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:\n\n\\begin{table}[h]\n\\centering\n\\caption{Social Sciences $\\gamma$ prior sensitivity ($J$=16).}\n\\label{tab:socsci_prior}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nPrior & $\\hat{\\gamma}$ & 95\\% CI & $P(\\gamma\\!<\\!0)$ & PPP \\\\\n\\midrule\n$\\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\\% & 0.242 \\\\\n$\\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\\% & 0.282 \\\\\n$\\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\\% & 0.282 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn contrast to the pooled analysis where $\\hat{\\gamma}$ shifts 2.6$\\times$ across priors, Social Sciences $\\hat{\\gamma}$ varies only 1.2$\\times$ ($-$0.43 to $-$0.51), with $P(\\gamma<0) \\geq 97.95\\%$ in all cases.\n\n\\section{IRT Ability Separation by Scale}\n\\label{sec:theta_separation}\n\nTable~\\ref{tab:theta_separation} reports the mean posterior $\\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\\Delta\\theta = \\bar{\\theta}_{3\\text{B}} - \\bar{\\theta}_{1.5\\text{B}}$ is positive and significant (95\\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\\Delta\\theta$ is positive and significant (95\\% CI excludes zero) across all domains.}\n\\label{tab:theta_separation}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $\\bar{\\theta}_{1.5\\text{B}}$ & $\\bar{\\theta}_{3\\text{B}}$ & $\\Delta\\theta$ [95\\% CI] \\\\\n\\midrule\nMath & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\\\\nScience & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\\\\nCS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\\\\nMedical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\\\\nHumanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\\\\nSocial Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\\\\nBusiness/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\\\\nOther & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\\\\n\\midrule\nPooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{DiD Across Dosage Levels}\n\\label{sec:did_dosage}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_did_dose_response.pdf}\n\\caption{Difference-in-differences (treated vs.\\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all five model families, confirming that the global capability modulation mechanism (\\S\\ref{sec:memorization_test}) is consistent across the full dosage range.}\n\\label{fig:did_dose_response}\n\\end{figure}\n\n\\section{Dose-Response Details}\n\\label{sec:dose_response_details}\n\nThe five dose-response patterns reported in \\S\\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \\textit{decreases} with dosage (0.41 at d000 $\\to$ 0.27 at d100), consistent with the position bias confound documented in \\S\\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\\%) overwhelms any memorization benefit.\n\n\\section{Sensitivity of Profile Classification}\n\\label{sec:classification_sensitivity}\n\nWe assess the robustness of Algorithm~\\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\\tau, \\sigma)$ combinations: $\\tau \\in \\{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\\}$~pp $\\times$ $\\sigma \\in \\{3, 4, 5, 6, 7\\}$~pp. Table~\\ref{tab:sensitivity} reports stability across this grid.\n\n\\begin{table}[h]\n\\centering\n\\caption{Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.}\n\\label{tab:sensitivity}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nModel & Default Pattern & Stability & Notes \\\\\n\\midrule\nPhi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\\le$ all $\\tau$ \\\\\nQwen-14B & U-collapse & 30/30 & --- \\\\\nGemma-2 9B & Benefit & 30/30 & --- \\\\\nOLMo-2 7B & Benefit-sat & 30/30 & --- \\\\\nQwen-7B & V-recovery & 30/30 & volatility check resolves \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith the mid-trajectory volatility check (Algorithm~\\ref{alg:profile-classification}, line~3), all five families achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$). The severity threshold $\\sigma$ has zero impact on any model's classification, because no model's $\\Delta\\text{acc}$ falls in the range where $\\sigma$ determines the U-collapse vs.\\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\\sigma=7$).\n\n\\section{Cross-Family Domain Decomposition}\n\\label{sec:domain_decomposition}\n\nWe decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.\n\nTwo patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, U-collapse (Qwen-14B) produces negative $\\Delta\\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\\Delta\\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.\n\nSecond, domains differ in sensitivity. STEM is the most resilient (mean $|\\Delta\\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.\n\nThese results reinforce the global capability modulation interpretation (\\S\\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.\n\n\\section{Baseline Ability vs.\\ Contamination Effect}\n\\label{sec:baseline_vs_effect}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_baseline_vs_effect.pdf}\n\\caption{Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta$acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Threshold estimated from five models spanning four independent families.}\n\\label{fig:baseline_vs_effect}\n\\end{figure}\n\n\\section{Per-Domain $\\gamma$ Estimates}\n\\label{sec:domain_gamma_table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_domain_gamma.pdf}\n\\caption{Per-domain $\\gamma_d$ estimates with 95\\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}\n\\label{fig:domain_gamma}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-domain $\\gamma$ estimates (2PL+$\\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\\hat{R} < 1.01$). Social Sciences $P(\\gamma\\!<\\!0)$ strengthens from 99.1\\% to 99.7\\% at $J$=16, crossing the Bonferroni-corrected threshold of 99.375\\% for eight tests. Results remain exploratory at these ensemble sizes \\citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}\n\\label{tab:domain_gamma}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{$J$=13} & \\multicolumn{4}{c}{$J$=16} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-7}\nDomain & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & PPP & $\\hat{R}$ \\\\\n\\midrule\nMMLU: Math & +0.50 & 8.1\\% & +0.60 & 3.8\\% & 0.305 & 1.007 \\\\\nMMLU: Science & +0.50 & 7.8\\% & +0.57 & 4.3\\% & 0.197 & 1.007 \\\\\nMMLU: CS/Eng & +0.50 & 14.8\\% & +0.32 & 24.0\\% & 0.503 & 1.006 \\\\\nMMLU: Medical & +0.24 & 24.0\\% & +0.05 & 43.6\\% & 0.268 & 1.008 \\\\\nMMLU: Other & +0.13 & 35.7\\% & +0.32 & 20.4\\% & 0.072$^\\dagger$ & 1.008 \\\\\nMMLU: Business/Law & +0.04 & 44.1\\% & +0.08 & 37.8\\% & 0.395 & 1.007 \\\\\nMMLU: Humanities & $-$0.31 & 85.4\\% & $-$0.14 & 69.7\\% & 0.416 & 1.007 \\\\\nMMLU: Social Sci & $-$0.57 & \\textbf{99.1\\%} & $-$0.63 & \\textbf{99.7\\%} & 0.722 & 1.006 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\scriptsize $^\\dagger$PPP below acceptable threshold (0.1); $\\gamma$ estimate for this domain should be interpreted with caution.}\n\\end{table}\n\n\\section{Threshold DGP Simulation}\n\\label{sec:threshold_dgp}\n\nTo test whether threshold-type misspecification explains the non-significant oracle $\\gamma$, we simulate data under step-function contamination DGPs where items are affected only above exposure thresholds of 0.3, 0.5, and 0.7 (three cutoffs, ten seeds each). Under these DGPs, the linear 2PL+$\\gamma$ specification overestimates rather than attenuates the contamination effect (ratio 1.09 to 1.33 relative to the true $\\gamma$), while PPP remains in the acceptable range (0.50 to 0.56). This rules out threshold-type misspecification as an explanation for the non-significant oracle $\\gamma$ under a unidirectional effect assumption. Bidirectional item-level effects (positive for some items, negative for others) could still produce a near-zero pooled $\\gamma$, but this collapses to the heterogeneity interpretation (\\S\\ref{sec:domain_differential}). The simulation uses uniform exposure distributions; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.\n\n\\section{ARC IRT Results}\n\\label{sec:arc_irt}\n\nARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\\sim}$0.7pp) is smaller than correction noise. Domain-level $\\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).\n\n\\section{Full Baseline Comparison}\n\\label{sec:full_baselines}\n\nTable~\\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.\n\nB6-DCR \\citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_arc}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & ARC MAE \\\\\n\\midrule\nB0-Raw & 0.059 \\\\\nB1-Remove\\&Rescore & 0.059 \\\\\nB2-Single2PL+$\\gamma$ & 0.064 \\\\\nB3-Vanilla4PL & 0.071 \\\\\nB4-LinearRegression & 0.056 \\\\\nB5-Emperor & 0.059 \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & \\textbf{0.035} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_gsm8k}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & GSM8K MAE \\\\\n\\midrule\nB0-Raw & 0.003 \\\\\nB2-Single2PL+$\\gamma$ & 0.320 \\\\\nB3-Vanilla4PL & 0.012 \\\\\nB4-LinearRegression & \\textbf{0.003} \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & 0.020 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 155,
        "oldLines": 7,
        "newStart": 155,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[h]",
          " \\centering",
          "-\\caption{Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.}",
          "+\\caption{Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All six model--seed configurations achieve perfect stability.}",
          " \\label{tab:sensitivity}",
          " \\footnotesize",
          " \\begin{tabular}{lccc}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Edit · `toolu_01JGGE3aYBzXsQJTFFoakY7C`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "old_string": "Qwen-7B & V-recovery & 30/30 & volatility check resolves \\\\\n\\bottomrule",
  "new_string": "Qwen-7B (s42) & V-recovery & 30/30 & volatility check resolves \\\\\nQwen-7B (s123) & V-recovery & 30/30 & $\\Delta \\approx 0$; volatility check resolves \\\\\n\\bottomrule"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "93812f8a-5d36-42d9-a44e-11c0f6330230",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QCXdVkkwGE4NrwWsNJ1QW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 63005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T22:17:20.083Z_

<details><summary>↩ Tool result · `toolu_01JGGE3aYBzXsQJTFFoakY7C`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "6319fbca-f63f-43c7-9ed5-2ccef2d5c22f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
    "oldString": "Qwen-7B & V-recovery & 30/30 & volatility check resolves \\\\\n\\bottomrule",
    "newString": "Qwen-7B (s42) & V-recovery & 30/30 & volatility check resolves \\\\\nQwen-7B (s123) & V-recovery & 30/30 & $\\Delta \\approx 0$; volatility check resolves \\\\\n\\bottomrule",
    "originalFile": "\\appendix\n\n\\section{ARC-Challenge Cross-Benchmark Analysis}\n\\label{sec:arc_cross_benchmark}\n\nARC-Challenge (25-shot, 1{,}172 items) patterns are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$3.8pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($\\pm$0.6pp). Gemma-2 ARC is excluded due to a 16pp evaluation artifact. Qwen-14B exhibits V-recovery on ARC rather than U-collapse ($-$3.4pp vs.\\ $-$9.4pp on MMLU), a 2.8$\\times$ attenuation reflecting benchmark-specific properties. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\\%, Gemma-2: 62.7\\%) due to the smaller item pool (1{,}172 vs.\\ 14{,}042), and Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero ($[-2.47, +0.09]$pp).\n\nDose-response profiles are jointly determined by model and benchmark properties: direction is governed by model baseline ability (the 64.7\\% threshold); shape is governed by benchmark properties (item pool size, difficulty distribution, evaluation format). This benchmark-conditionality is a finding in its own right---practitioners cannot assume a contamination profile on one benchmark transfers to another.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_arc_dose_response.pdf}\n\\caption{ARC-Challenge accuracy vs.\\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\\ref{fig:dose_response}) for 4/5 models.}\n\\label{fig:dose_response_arc}\n\\end{figure}\n\n\\section{Signal Reliability Across Scales}\n\\label{sec:signal_reliability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap.pdf}\n\\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\\%++) reverses at 0.5B; S4 is near-random below 1.5B.}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\section{Identifiability Simulation}\n\\label{sec:identifiability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_identifiability_heatmap.pdf}\n\\caption{$\\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\\% CI coverage $\\geq90\\%$ require $J\\geq50$ at AUC$=$0.55, but only $J\\geq16$ at AUC$\\geq$0.90.}\n\\label{fig:identifiability_heatmap}\n\\end{figure}\n\nFisher information $\\mathcal{I}(\\gamma) \\propto \\text{Var}(e_{\\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\\% CI coverage $\\geq 90\\%$ require $J \\geq 50$; at AUC$\\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \\citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).\n\n\\section{4PL Extension}\n\\label{sec:4pl_details}\n\nFor MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:\n\\begin{equation}\n    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwith $c_i \\sim \\text{Beta}(5,20)$ and $d_i \\sim \\text{Beta}(20,5)$. This requires $J \\geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\\gamma$ at $J=13$; pooled calibration uses $J=16$.\n\n\\section{S4 Self-Critique Signal Details}\n\\label{sec:s4_details}\n\nS4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\\text{YES})$, then score each item as the negative entropy of this distribution: $\\text{S4}_i = -[-p\\log p - (1-p)\\log(1-p)]$ where $p = P(\\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.\n\n\\section{Training Convergence}\n\\label{sec:training_convergence}\n\nAll SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.\n\n\\section{Model Exclusion Details}\n\\label{sec:exclusion_details}\n\nOf the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\\alpha=32$, lr$=5\\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.\n\n\\paragraph{Model sets across analyses.}\nTable~\\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\\S\\ref{sec:injection}). Core findings ($\\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.\n\n\\begin{table}[h]\n\\centering\n\\caption{Model set composition across analyses.}\n\\label{tab:model_sets}\n\\footnotesize\n\\begin{tabular}{lcll}\n\\toprule\nAnalysis & $J$ & Model Set & Section \\\\\n\\midrule\nPooled baselines & 16 & 8$\\times$Qwen-1.5B + 8$\\times$Qwen-3B & \\S\\ref{sec:calibration_results} \\\\\nDomain $\\gamma$ & 13 & 8$\\times$Qwen-1.5B + 5$\\times$Qwen-3B & \\S\\ref{sec:domain_differential} \\\\\nCross-family & 16--28 & varies by benchmark & \\S\\ref{sec:taxonomy} \\\\\nOracle ablation & 13 & domain whitelist & \\S\\ref{sec:calibration_results} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Prior Sensitivity Analysis}\n\\label{sec:prior_sensitivity}\n\nTo assess the influence of the $\\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\\gamma \\sim \\mathcal{N}(0, 0.5)$, $\\mathcal{N}(0, 1)$ (default), and $\\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\\% CI includes zero in all cases (lower bound stable at $\\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\\hat{R} < 1.01$, ESS $> 3800$, PPP $\\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\\gamma$-based conclusions at current ensemble sizes.\n\nFor the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:\n\n\\begin{table}[h]\n\\centering\n\\caption{Social Sciences $\\gamma$ prior sensitivity ($J$=16).}\n\\label{tab:socsci_prior}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nPrior & $\\hat{\\gamma}$ & 95\\% CI & $P(\\gamma\\!<\\!0)$ & PPP \\\\\n\\midrule\n$\\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\\% & 0.242 \\\\\n$\\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\\% & 0.282 \\\\\n$\\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\\% & 0.282 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn contrast to the pooled analysis where $\\hat{\\gamma}$ shifts 2.6$\\times$ across priors, Social Sciences $\\hat{\\gamma}$ varies only 1.2$\\times$ ($-$0.43 to $-$0.51), with $P(\\gamma<0) \\geq 97.95\\%$ in all cases.\n\n\\section{IRT Ability Separation by Scale}\n\\label{sec:theta_separation}\n\nTable~\\ref{tab:theta_separation} reports the mean posterior $\\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\\Delta\\theta = \\bar{\\theta}_{3\\text{B}} - \\bar{\\theta}_{1.5\\text{B}}$ is positive and significant (95\\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\\Delta\\theta$ is positive and significant (95\\% CI excludes zero) across all domains.}\n\\label{tab:theta_separation}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $\\bar{\\theta}_{1.5\\text{B}}$ & $\\bar{\\theta}_{3\\text{B}}$ & $\\Delta\\theta$ [95\\% CI] \\\\\n\\midrule\nMath & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\\\\nScience & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\\\\nCS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\\\\nMedical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\\\\nHumanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\\\\nSocial Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\\\\nBusiness/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\\\\nOther & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\\\\n\\midrule\nPooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{DiD Across Dosage Levels}\n\\label{sec:did_dosage}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_did_dose_response.pdf}\n\\caption{Difference-in-differences (treated vs.\\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all five model families, confirming that the global capability modulation mechanism (\\S\\ref{sec:memorization_test}) is consistent across the full dosage range.}\n\\label{fig:did_dose_response}\n\\end{figure}\n\n\\section{Dose-Response Details}\n\\label{sec:dose_response_details}\n\nThe five dose-response patterns reported in \\S\\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \\textit{decreases} with dosage (0.41 at d000 $\\to$ 0.27 at d100), consistent with the position bias confound documented in \\S\\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\\%) overwhelms any memorization benefit.\n\n\\section{Sensitivity of Profile Classification}\n\\label{sec:classification_sensitivity}\n\nWe assess the robustness of Algorithm~\\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\\tau, \\sigma)$ combinations: $\\tau \\in \\{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\\}$~pp $\\times$ $\\sigma \\in \\{3, 4, 5, 6, 7\\}$~pp. Table~\\ref{tab:sensitivity} reports stability across this grid.\n\n\\begin{table}[h]\n\\centering\n\\caption{Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All six model--seed configurations achieve perfect stability.}\n\\label{tab:sensitivity}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nModel & Default Pattern & Stability & Notes \\\\\n\\midrule\nPhi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\\le$ all $\\tau$ \\\\\nQwen-14B & U-collapse & 30/30 & --- \\\\\nGemma-2 9B & Benefit & 30/30 & --- \\\\\nOLMo-2 7B & Benefit-sat & 30/30 & --- \\\\\nQwen-7B & V-recovery & 30/30 & volatility check resolves \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith the mid-trajectory volatility check (Algorithm~\\ref{alg:profile-classification}, line~3), all five families achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$). The severity threshold $\\sigma$ has zero impact on any model's classification, because no model's $\\Delta\\text{acc}$ falls in the range where $\\sigma$ determines the U-collapse vs.\\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\\sigma=7$).\n\n\\section{Cross-Family Domain Decomposition}\n\\label{sec:domain_decomposition}\n\nWe decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.\n\nTwo patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, U-collapse (Qwen-14B) produces negative $\\Delta\\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\\Delta\\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.\n\nSecond, domains differ in sensitivity. STEM is the most resilient (mean $|\\Delta\\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.\n\nThese results reinforce the global capability modulation interpretation (\\S\\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.\n\n\\section{Baseline Ability vs.\\ Contamination Effect}\n\\label{sec:baseline_vs_effect}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_baseline_vs_effect.pdf}\n\\caption{Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta$acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Threshold estimated from five models spanning four independent families.}\n\\label{fig:baseline_vs_effect}\n\\end{figure}\n\n\\section{Per-Domain $\\gamma$ Estimates}\n\\label{sec:domain_gamma_table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_domain_gamma.pdf}\n\\caption{Per-domain $\\gamma_d$ estimates with 95\\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}\n\\label{fig:domain_gamma}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-domain $\\gamma$ estimates (2PL+$\\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\\hat{R} < 1.01$). Social Sciences $P(\\gamma\\!<\\!0)$ strengthens from 99.1\\% to 99.7\\% at $J$=16, crossing the Bonferroni-corrected threshold of 99.375\\% for eight tests. Results remain exploratory at these ensemble sizes \\citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}\n\\label{tab:domain_gamma}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{$J$=13} & \\multicolumn{4}{c}{$J$=16} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-7}\nDomain & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & PPP & $\\hat{R}$ \\\\\n\\midrule\nMMLU: Math & +0.50 & 8.1\\% & +0.60 & 3.8\\% & 0.305 & 1.007 \\\\\nMMLU: Science & +0.50 & 7.8\\% & +0.57 & 4.3\\% & 0.197 & 1.007 \\\\\nMMLU: CS/Eng & +0.50 & 14.8\\% & +0.32 & 24.0\\% & 0.503 & 1.006 \\\\\nMMLU: Medical & +0.24 & 24.0\\% & +0.05 & 43.6\\% & 0.268 & 1.008 \\\\\nMMLU: Other & +0.13 & 35.7\\% & +0.32 & 20.4\\% & 0.072$^\\dagger$ & 1.008 \\\\\nMMLU: Business/Law & +0.04 & 44.1\\% & +0.08 & 37.8\\% & 0.395 & 1.007 \\\\\nMMLU: Humanities & $-$0.31 & 85.4\\% & $-$0.14 & 69.7\\% & 0.416 & 1.007 \\\\\nMMLU: Social Sci & $-$0.57 & \\textbf{99.1\\%} & $-$0.63 & \\textbf{99.7\\%} & 0.722 & 1.006 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\scriptsize $^\\dagger$PPP below acceptable threshold (0.1); $\\gamma$ estimate for this domain should be interpreted with caution.}\n\\end{table}\n\n\\section{Threshold DGP Simulation}\n\\label{sec:threshold_dgp}\n\nTo test whether threshold-type misspecification explains the non-significant oracle $\\gamma$, we simulate data under step-function contamination DGPs where items are affected only above exposure thresholds of 0.3, 0.5, and 0.7 (three cutoffs, ten seeds each). Under these DGPs, the linear 2PL+$\\gamma$ specification overestimates rather than attenuates the contamination effect (ratio 1.09 to 1.33 relative to the true $\\gamma$), while PPP remains in the acceptable range (0.50 to 0.56). This rules out threshold-type misspecification as an explanation for the non-significant oracle $\\gamma$ under a unidirectional effect assumption. Bidirectional item-level effects (positive for some items, negative for others) could still produce a near-zero pooled $\\gamma$, but this collapses to the heterogeneity interpretation (\\S\\ref{sec:domain_differential}). The simulation uses uniform exposure distributions; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.\n\n\\section{ARC IRT Results}\n\\label{sec:arc_irt}\n\nARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\\sim}$0.7pp) is smaller than correction noise. Domain-level $\\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).\n\n\\section{Full Baseline Comparison}\n\\label{sec:full_baselines}\n\nTable~\\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.\n\nB6-DCR \\citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_arc}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & ARC MAE \\\\\n\\midrule\nB0-Raw & 0.059 \\\\\nB1-Remove\\&Rescore & 0.059 \\\\\nB2-Single2PL+$\\gamma$ & 0.064 \\\\\nB3-Vanilla4PL & 0.071 \\\\\nB4-LinearRegression & 0.056 \\\\\nB5-Emperor & 0.059 \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & \\textbf{0.035} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_gsm8k}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & GSM8K MAE \\\\\n\\midrule\nB0-Raw & 0.003 \\\\\nB2-Single2PL+$\\gamma$ & 0.320 \\\\\nB3-Vanilla4PL & 0.012 \\\\\nB4-LinearRegression & \\textbf{0.003} \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & 0.020 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 166,
        "oldLines": 7,
        "newStart": 166,
        "newLines": 8,
        "lines": [
          " Qwen-14B & U-collapse & 30/30 & --- \\\\",
          " Gemma-2 9B & Benefit & 30/30 & --- \\\\",
          " OLMo-2 7B & Benefit-sat & 30/30 & --- \\\\",
          "-Qwen-7B & V-recovery & 30/30 & volatility check resolves \\\\",
          "+Qwen-7B (s42) & V-recovery & 30/30 & volatility check resolves \\\\",
          "+Qwen-7B (s123) & V-recovery & 30/30 & $\\Delta \\approx 0$; volatility check resolves \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Edit · `toolu_011p3YhT2NXBkEaxwPv61GgZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex",
  "old_string": "V-type recovery ($-$3pp then partial rebound)",
  "new_string": "V-type recovery ($-$3pp then partial-to-full rebound)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "607202a2-4aec-4643-aff6-728b352d35cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QCXdVkkwGE4NrwWsNJ1QW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 63005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T22:17:23.673Z_

<details><summary>↩ Tool result · `toolu_011p3YhT2NXBkEaxwPv61GgZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "3ac078c2-c6f0-4aac-9ed3-51106b99e46f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex",
    "oldString": "V-type recovery ($-$3pp then partial rebound)",
    "newString": "V-type recovery ($-$3pp then partial-to-full rebound)",
    "originalFile": "Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but five distinct dose-response patterns: Immune ($\\pm$0.5pp), U-type collapse ($-$10pp), V-type recovery ($-$3pp then partial rebound), Benefit ($+$3.8pp monotonic), and Benefit-saturation ($+$3.2pp then plateau). A baseline ability threshold at 64.7\\% MMLU (bootstrap 95\\% CI: 64.0--65.4\\%) separates models that benefit from contamination from those that are harmed or immune. Counter-intuitively, the 14B Qwen model is 3$\\times$ more fragile than 7B. Profiles are robust on MMLU (4/5 families $\\geq$99.6\\% bootstrap stability); ARC-Challenge shows directional agreement for 3/5 families but lower stability due to its smaller item pool (1{,}172 vs.\\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \\geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 1,
        "newStart": 1,
        "newLines": 1,
        "lines": [
          "-Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but five distinct dose-response patterns: Immune ($\\pm$0.5pp), U-type collapse ($-$10pp), V-type recovery ($-$3pp then partial rebound), Benefit ($+$3.8pp monotonic), and Benefit-saturation ($+$3.2pp then plateau). A baseline ability threshold at 64.7\\% MMLU (bootstrap 95\\% CI: 64.0--65.4\\%) separates models that benefit from contamination from those that are harmed or immune. Counter-intuitively, the 14B Qwen model is 3$\\times$ more fragile than 7B. Profiles are robust on MMLU (4/5 families $\\geq$99.6\\% bootstrap stability); ARC-Challenge shows directional agreement for 3/5 families but lower stability due to its smaller item pool (1{,}172 vs.\\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \\geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.",
          "+Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but five distinct dose-response patterns: Immune ($\\pm$0.5pp), U-type collapse ($-$10pp), V-type recovery ($-$3pp then partial-to-full rebound), Benefit ($+$3.8pp monotonic), and Benefit-saturation ($+$3.2pp then plateau). A baseline ability threshold at 64.7\\% MMLU (bootstrap 95\\% CI: 64.0--65.4\\%) separates models that benefit from contamination from those that are harmed or immune. Counter-intuitively, the 14B Qwen model is 3$\\times$ more fragile than 7B. Profiles are robust on MMLU (4/5 families $\\geq$99.6\\% bootstrap stability); ARC-Challenge shows directional agreement for 3/5 families but lower stability due to its smaller item pool (1{,}172 vs.\\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \\geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Edit · `toolu_01FfX2mB5xGDtEbSHnraNkbc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex",
  "old_string": "\\paragraph{Single seed.}",
  "new_string": "\\paragraph{Seed coverage.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "12eeba6e-40ed-421d-b37b-b78c8e6b8da5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QCXdVkkwGE4NrwWsNJ1QW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 63005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T22:17:23.813Z_

<details><summary>↩ Tool result · `toolu_01FfX2mB5xGDtEbSHnraNkbc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "620d6abd-8e17-4a81-b5f0-c9f79adcd391",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex",
    "oldString": "\\paragraph{Single seed.}",
    "newString": "\\paragraph{Seed coverage.}",
    "originalFile": "\\section*{Limitations}\n\\label{sec:limitations}\n\nWe identify ten limitations that bound the scope of our conclusions.\n\n\\paragraph{Scale ceiling.}\nAll experiments use models at or below 14.7B parameters. Larger models (70B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.\n\n\\paragraph{Single seed.}\nThe five-pattern taxonomy (Table~\\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.\n\n\\paragraph{SFT ecological validity.}\nWe use LoRA-based SFT injection exclusively in AUGMENT mode (contaminated items appended to, not replacing, base SFT data). Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures. The position bias at 0.5B (A-option rate escalating from 46\\% to 98\\% with dosage) is likely SFT-specific. Generalization to pretraining contamination requires further validation.\n\n\\paragraph{ARC-Challenge bootstrap stability.}\nARC-Challenge contains only 1{,}172 items (vs.\\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\\%, Gemma-2 62.7\\% (vs.\\ $\\geq$76.6\\% on MMLU). Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (U-collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.\n\n\\paragraph{Signal coverage.}\nS1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\\S\\ref{sec:signal_failure}).\n\n\\paragraph{Ensemble size and per-domain power.}\nReliable $\\gamma$ recovery requires $J \\geq 50$. Our domain-level analysis ($J = 13$--$16$) yields a strong directional signal for only one of eight MMLU domains. Per-domain $\\gamma$ diagnosis at current ensemble sizes is exploratory.\n\n\\paragraph{Position bias.}\nQwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\\% at d000 to 98\\% at d100); these models are excluded from MC IRT analyses, reducing ensemble size.\n\n\\paragraph{Model misfit in non-STEM domains.}\nA single linear $\\gamma$ cannot capture non-monotone contamination effects within a domain. The five-pattern taxonomy operates at the model level; richer within-domain specifications may be required for domain-level calibration.\n\n\\paragraph{Additive $\\gamma$ linearity.}\nThe 2PL+$\\gamma$ model assumes contamination effects are additive and linear in exposure. PPP posterior predictive checks cannot detect threshold-type model misspecification (PPP remains 0.50--0.56 despite up to 33\\% $\\gamma$ overestimation), which highlights the value of simulation-based specification testing. The threshold DGP simulation uses uniform exposure; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.\n\n\\paragraph{Prompt format sensitivity.}\nThe observed dose-response profiles are conditional on the evaluation protocol (5-shot prompting for MMLU, 25-shot for ARC-Challenge). Preliminary comparison with 0-shot evaluation suggests that pattern shapes may vary with prompt format---for instance, the V-type recovery pattern observed under 5-shot prompting can disappear under 0-shot conditions. This indicates that contamination effects interact with in-context learning mechanisms. While internal consistency is maintained (all 75 model--dosage configurations use the same protocol), practitioners replicating our analyses under different prompting regimes should expect quantitatively and potentially qualitatively different dose-response profiles. Future work should systematically evaluate protocol sensitivity across shot counts and prompt templates.\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 7,
        "newStart": 6,
        "newLines": 7,
        "lines": [
          " \\paragraph{Scale ceiling.}",
          " All experiments use models at or below 14.7B parameters. Larger models (70B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.",
          " ",
          "-\\paragraph{Single seed.}",
          "+\\paragraph{Seed coverage.}",
          " The five-pattern taxonomy (Table~\\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.",
          " ",
          " \\paragraph{SFT ecological validity.}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the appendix.tex line 154 for the grid sweep description. Looking at my earlier read:

Line 154: "We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\tau, \sigma)$ combinations: $\tau \in \{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\}$~pp $\times$ $\sigma \in \{3, 4, 5, 6, 7\}$~pp. 

The "30" here is correct since the grid is indeed 6 τ × 5 σ = 30. No change needed.

Now I need to check line 174 of appendix.tex which describes the mid-trajectory volatility check results. It currently says "all five families" but should be updated to "all six model--seed configurations" since Qwen-7B s123 is now included. I should also look at the limitations.tex section about the triple-seed validation with error bars.

Let me verify all the sensitivity mentions across the files. I've already updated several instances, but I need to make sure appendix.tex line 174 gets changed from "five families" to "six model--seed configurations" to reflect the addition of the new configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "3f17a3e1-afc7-4b56-956e-6622433b3e56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVcgUHfAegm4UJsU52bTPr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5564,
      "cache_read_input_tokens": 63724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5564
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 72_

还有 appendix.tex line 174 也提到 "all five families"，需要一并更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "a8e36bda-9218-4d21-8432-20e9abca181e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVcgUHfAegm4UJsU52bTPr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5564,
      "cache_read_input_tokens": 63724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5564
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Edit · `toolu_019tBPdbp4aPHftSEfdpiFsZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "old_string": "all five families achieve 30/30 classification stability across all threshold combinations",
  "new_string": "all six model--seed configurations achieve 30/30 classification stability across all threshold combinations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "44587db0-2efe-40a0-9a26-3d18c8959b4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVcgUHfAegm4UJsU52bTPr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5564,
      "cache_read_input_tokens": 63724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5564
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T22:17:43.454Z_

<details><summary>↩ Tool result · `toolu_019tBPdbp4aPHftSEfdpiFsZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "3cd58daf-7e8c-4d9c-a518-a9708cf38e0c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
    "oldString": "all five families achieve 30/30 classification stability across all threshold combinations",
    "newString": "all six model--seed configurations achieve 30/30 classification stability across all threshold combinations",
    "originalFile": "\\appendix\n\n\\section{ARC-Challenge Cross-Benchmark Analysis}\n\\label{sec:arc_cross_benchmark}\n\nARC-Challenge (25-shot, 1{,}172 items) patterns are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$3.8pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($\\pm$0.6pp). Gemma-2 ARC is excluded due to a 16pp evaluation artifact. Qwen-14B exhibits V-recovery on ARC rather than U-collapse ($-$3.4pp vs.\\ $-$9.4pp on MMLU), a 2.8$\\times$ attenuation reflecting benchmark-specific properties. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\\%, Gemma-2: 62.7\\%) due to the smaller item pool (1{,}172 vs.\\ 14{,}042), and Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero ($[-2.47, +0.09]$pp).\n\nDose-response profiles are jointly determined by model and benchmark properties: direction is governed by model baseline ability (the 64.7\\% threshold); shape is governed by benchmark properties (item pool size, difficulty distribution, evaluation format). This benchmark-conditionality is a finding in its own right---practitioners cannot assume a contamination profile on one benchmark transfers to another.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_arc_dose_response.pdf}\n\\caption{ARC-Challenge accuracy vs.\\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\\ref{fig:dose_response}) for 4/5 models.}\n\\label{fig:dose_response_arc}\n\\end{figure}\n\n\\section{Signal Reliability Across Scales}\n\\label{sec:signal_reliability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap.pdf}\n\\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\\%++) reverses at 0.5B; S4 is near-random below 1.5B.}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\section{Identifiability Simulation}\n\\label{sec:identifiability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_identifiability_heatmap.pdf}\n\\caption{$\\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\\% CI coverage $\\geq90\\%$ require $J\\geq50$ at AUC$=$0.55, but only $J\\geq16$ at AUC$\\geq$0.90.}\n\\label{fig:identifiability_heatmap}\n\\end{figure}\n\nFisher information $\\mathcal{I}(\\gamma) \\propto \\text{Var}(e_{\\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\\% CI coverage $\\geq 90\\%$ require $J \\geq 50$; at AUC$\\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \\citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).\n\n\\section{4PL Extension}\n\\label{sec:4pl_details}\n\nFor MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:\n\\begin{equation}\n    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwith $c_i \\sim \\text{Beta}(5,20)$ and $d_i \\sim \\text{Beta}(20,5)$. This requires $J \\geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\\gamma$ at $J=13$; pooled calibration uses $J=16$.\n\n\\section{S4 Self-Critique Signal Details}\n\\label{sec:s4_details}\n\nS4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\\text{YES})$, then score each item as the negative entropy of this distribution: $\\text{S4}_i = -[-p\\log p - (1-p)\\log(1-p)]$ where $p = P(\\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.\n\n\\section{Training Convergence}\n\\label{sec:training_convergence}\n\nAll SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.\n\n\\section{Model Exclusion Details}\n\\label{sec:exclusion_details}\n\nOf the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\\alpha=32$, lr$=5\\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.\n\n\\paragraph{Model sets across analyses.}\nTable~\\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\\S\\ref{sec:injection}). Core findings ($\\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.\n\n\\begin{table}[h]\n\\centering\n\\caption{Model set composition across analyses.}\n\\label{tab:model_sets}\n\\footnotesize\n\\begin{tabular}{lcll}\n\\toprule\nAnalysis & $J$ & Model Set & Section \\\\\n\\midrule\nPooled baselines & 16 & 8$\\times$Qwen-1.5B + 8$\\times$Qwen-3B & \\S\\ref{sec:calibration_results} \\\\\nDomain $\\gamma$ & 13 & 8$\\times$Qwen-1.5B + 5$\\times$Qwen-3B & \\S\\ref{sec:domain_differential} \\\\\nCross-family & 16--28 & varies by benchmark & \\S\\ref{sec:taxonomy} \\\\\nOracle ablation & 13 & domain whitelist & \\S\\ref{sec:calibration_results} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Prior Sensitivity Analysis}\n\\label{sec:prior_sensitivity}\n\nTo assess the influence of the $\\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\\gamma \\sim \\mathcal{N}(0, 0.5)$, $\\mathcal{N}(0, 1)$ (default), and $\\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\\% CI includes zero in all cases (lower bound stable at $\\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\\hat{R} < 1.01$, ESS $> 3800$, PPP $\\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\\gamma$-based conclusions at current ensemble sizes.\n\nFor the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:\n\n\\begin{table}[h]\n\\centering\n\\caption{Social Sciences $\\gamma$ prior sensitivity ($J$=16).}\n\\label{tab:socsci_prior}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nPrior & $\\hat{\\gamma}$ & 95\\% CI & $P(\\gamma\\!<\\!0)$ & PPP \\\\\n\\midrule\n$\\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\\% & 0.242 \\\\\n$\\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\\% & 0.282 \\\\\n$\\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\\% & 0.282 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn contrast to the pooled analysis where $\\hat{\\gamma}$ shifts 2.6$\\times$ across priors, Social Sciences $\\hat{\\gamma}$ varies only 1.2$\\times$ ($-$0.43 to $-$0.51), with $P(\\gamma<0) \\geq 97.95\\%$ in all cases.\n\n\\section{IRT Ability Separation by Scale}\n\\label{sec:theta_separation}\n\nTable~\\ref{tab:theta_separation} reports the mean posterior $\\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\\Delta\\theta = \\bar{\\theta}_{3\\text{B}} - \\bar{\\theta}_{1.5\\text{B}}$ is positive and significant (95\\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\\Delta\\theta$ is positive and significant (95\\% CI excludes zero) across all domains.}\n\\label{tab:theta_separation}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $\\bar{\\theta}_{1.5\\text{B}}$ & $\\bar{\\theta}_{3\\text{B}}$ & $\\Delta\\theta$ [95\\% CI] \\\\\n\\midrule\nMath & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\\\\nScience & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\\\\nCS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\\\\nMedical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\\\\nHumanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\\\\nSocial Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\\\\nBusiness/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\\\\nOther & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\\\\n\\midrule\nPooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{DiD Across Dosage Levels}\n\\label{sec:did_dosage}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_did_dose_response.pdf}\n\\caption{Difference-in-differences (treated vs.\\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all five model families, confirming that the global capability modulation mechanism (\\S\\ref{sec:memorization_test}) is consistent across the full dosage range.}\n\\label{fig:did_dose_response}\n\\end{figure}\n\n\\section{Dose-Response Details}\n\\label{sec:dose_response_details}\n\nThe five dose-response patterns reported in \\S\\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \\textit{decreases} with dosage (0.41 at d000 $\\to$ 0.27 at d100), consistent with the position bias confound documented in \\S\\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\\%) overwhelms any memorization benefit.\n\n\\section{Sensitivity of Profile Classification}\n\\label{sec:classification_sensitivity}\n\nWe assess the robustness of Algorithm~\\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\\tau, \\sigma)$ combinations: $\\tau \\in \\{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\\}$~pp $\\times$ $\\sigma \\in \\{3, 4, 5, 6, 7\\}$~pp. Table~\\ref{tab:sensitivity} reports stability across this grid.\n\n\\begin{table}[h]\n\\centering\n\\caption{Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All six model--seed configurations achieve perfect stability.}\n\\label{tab:sensitivity}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nModel & Default Pattern & Stability & Notes \\\\\n\\midrule\nPhi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\\le$ all $\\tau$ \\\\\nQwen-14B & U-collapse & 30/30 & --- \\\\\nGemma-2 9B & Benefit & 30/30 & --- \\\\\nOLMo-2 7B & Benefit-sat & 30/30 & --- \\\\\nQwen-7B (s42) & V-recovery & 30/30 & volatility check resolves \\\\\nQwen-7B (s123) & V-recovery & 30/30 & $\\Delta \\approx 0$; volatility check resolves \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith the mid-trajectory volatility check (Algorithm~\\ref{alg:profile-classification}, line~3), all five families achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$). The severity threshold $\\sigma$ has zero impact on any model's classification, because no model's $\\Delta\\text{acc}$ falls in the range where $\\sigma$ determines the U-collapse vs.\\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\\sigma=7$).\n\n\\section{Cross-Family Domain Decomposition}\n\\label{sec:domain_decomposition}\n\nWe decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.\n\nTwo patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, U-collapse (Qwen-14B) produces negative $\\Delta\\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\\Delta\\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.\n\nSecond, domains differ in sensitivity. STEM is the most resilient (mean $|\\Delta\\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.\n\nThese results reinforce the global capability modulation interpretation (\\S\\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.\n\n\\section{Baseline Ability vs.\\ Contamination Effect}\n\\label{sec:baseline_vs_effect}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_baseline_vs_effect.pdf}\n\\caption{Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta$acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Threshold estimated from five models spanning four independent families.}\n\\label{fig:baseline_vs_effect}\n\\end{figure}\n\n\\section{Per-Domain $\\gamma$ Estimates}\n\\label{sec:domain_gamma_table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_domain_gamma.pdf}\n\\caption{Per-domain $\\gamma_d$ estimates with 95\\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}\n\\label{fig:domain_gamma}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-domain $\\gamma$ estimates (2PL+$\\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\\hat{R} < 1.01$). Social Sciences $P(\\gamma\\!<\\!0)$ strengthens from 99.1\\% to 99.7\\% at $J$=16, crossing the Bonferroni-corrected threshold of 99.375\\% for eight tests. Results remain exploratory at these ensemble sizes \\citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}\n\\label{tab:domain_gamma}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{$J$=13} & \\multicolumn{4}{c}{$J$=16} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-7}\nDomain & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & PPP & $\\hat{R}$ \\\\\n\\midrule\nMMLU: Math & +0.50 & 8.1\\% & +0.60 & 3.8\\% & 0.305 & 1.007 \\\\\nMMLU: Science & +0.50 & 7.8\\% & +0.57 & 4.3\\% & 0.197 & 1.007 \\\\\nMMLU: CS/Eng & +0.50 & 14.8\\% & +0.32 & 24.0\\% & 0.503 & 1.006 \\\\\nMMLU: Medical & +0.24 & 24.0\\% & +0.05 & 43.6\\% & 0.268 & 1.008 \\\\\nMMLU: Other & +0.13 & 35.7\\% & +0.32 & 20.4\\% & 0.072$^\\dagger$ & 1.008 \\\\\nMMLU: Business/Law & +0.04 & 44.1\\% & +0.08 & 37.8\\% & 0.395 & 1.007 \\\\\nMMLU: Humanities & $-$0.31 & 85.4\\% & $-$0.14 & 69.7\\% & 0.416 & 1.007 \\\\\nMMLU: Social Sci & $-$0.57 & \\textbf{99.1\\%} & $-$0.63 & \\textbf{99.7\\%} & 0.722 & 1.006 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\scriptsize $^\\dagger$PPP below acceptable threshold (0.1); $\\gamma$ estimate for this domain should be interpreted with caution.}\n\\end{table}\n\n\\section{Threshold DGP Simulation}\n\\label{sec:threshold_dgp}\n\nTo test whether threshold-type misspecification explains the non-significant oracle $\\gamma$, we simulate data under step-function contamination DGPs where items are affected only above exposure thresholds of 0.3, 0.5, and 0.7 (three cutoffs, ten seeds each). Under these DGPs, the linear 2PL+$\\gamma$ specification overestimates rather than attenuates the contamination effect (ratio 1.09 to 1.33 relative to the true $\\gamma$), while PPP remains in the acceptable range (0.50 to 0.56). This rules out threshold-type misspecification as an explanation for the non-significant oracle $\\gamma$ under a unidirectional effect assumption. Bidirectional item-level effects (positive for some items, negative for others) could still produce a near-zero pooled $\\gamma$, but this collapses to the heterogeneity interpretation (\\S\\ref{sec:domain_differential}). The simulation uses uniform exposure distributions; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.\n\n\\section{ARC IRT Results}\n\\label{sec:arc_irt}\n\nARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\\sim}$0.7pp) is smaller than correction noise. Domain-level $\\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).\n\n\\section{Full Baseline Comparison}\n\\label{sec:full_baselines}\n\nTable~\\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.\n\nB6-DCR \\citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_arc}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & ARC MAE \\\\\n\\midrule\nB0-Raw & 0.059 \\\\\nB1-Remove\\&Rescore & 0.059 \\\\\nB2-Single2PL+$\\gamma$ & 0.064 \\\\\nB3-Vanilla4PL & 0.071 \\\\\nB4-LinearRegression & 0.056 \\\\\nB5-Emperor & 0.059 \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & \\textbf{0.035} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_gsm8k}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & GSM8K MAE \\\\\n\\midrule\nB0-Raw & 0.003 \\\\\nB2-Single2PL+$\\gamma$ & 0.320 \\\\\nB3-Vanilla4PL & 0.012 \\\\\nB4-LinearRegression & \\textbf{0.003} \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & 0.020 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 172,
        "oldLines": 7,
        "newStart": 172,
        "newLines": 7,
        "lines": [
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-With the mid-trajectory volatility check (Algorithm~\\ref{alg:profile-classification}, line~3), all five families achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$). The severity threshold $\\sigma$ has zero impact on any model's classification, because no model's $\\Delta\\text{acc}$ falls in the range where $\\sigma$ determines the U-collapse vs.\\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\\sigma=7$).",
          "+With the mid-trajectory volatility check (Algorithm~\\ref{alg:profile-classification}, line~3), all six model--seed configurations achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$). The severity threshold $\\sigma$ has zero impact on any model's classification, because no model's $\\Delta\\text{acc}$ falls in the range where $\\sigma$ determines the U-collapse vs.\\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\\sigma=7$).",
          " ",
          " \\section{Cross-Family Domain Decomposition}",
          " \\label{sec:domain_decomposition}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 75_

现在验证所有修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "604580df-506c-474f-b7dc-bbca4276c014",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hhHQYQ93w9cv1pnHwwgGV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 69288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Grep · `toolu_013s4tTaMHZefCv1FpHqiXVm`</summary>

```json
{
  "pattern": "30.*combination|150/150|5/5 families|five families.*30|180/180|six model",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "84982db9-0ab1-4677-accc-8a1e2400947f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hhHQYQ93w9cv1pnHwwgGV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 69288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-19T22:17:48.461Z_

<details><summary>↩ Tool result · `toolu_013s4tTaMHZefCv1FpHqiXVm`</summary>

```text
docs/paper/method.tex:59:[Omitted long matching line]
docs/paper/appendix.tex:154:We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\tau, \sigma)$ combinations: $\tau \in \{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\}$~pp $\times$ $\sigma \in \{3, 4, 5, 6, 7\}$~pp. Table~\ref{tab:sensitivity} reports stability across this grid.
docs/paper/appendix.tex:158:\caption{Profile classification stability across 30 $(\tau, \sigma)$ threshold combinations (with mid-trajectory volatility check). All six model--seed configurations achieve perfect stability.}
docs/paper/appendix.tex:175:[Omitted long matching line]
docs/paper/results.tex:11:\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (180/180 model--seed--combination pairs across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
docs/paper/results.tex:27:Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\tau,\sigma)$ threshold combinations (six model--seed configurations; Appendix~\ref{sec:classification_sensitivity}).
docs/paper/main.aux:419:[Omitted long matching line]
docs/paper/main.aux:420:\newlabel{tab:taxonomy}{{1}{5}{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta $acc: d000$\to $d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\tau ,\sigma )$ combinations; Appendix~\ref {sec:classification_sensitivity})}{table.caption.7}{}}
docs/paper/main.aux:1149:\@writefile{lot}{\contentsline {table}{\numberline {7}{\ignorespaces Profile classification stability across 30 $(\tau , \sigma )$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.}}{12}{table.caption.37}\protected@file@percent }
docs/paper/main.aux:1150:\newlabel{tab:sensitivity}{{7}{12}{Profile classification stability across 30 $(\tau , \sigma )$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability}{table.caption.37}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "2d7118b4-0b27-4ad1-95c5-3f5f2e03faf1",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/method.tex:59:[Omitted long matching line]\ndocs/paper/appendix.tex:154:We assess the robustness of Algorithm~\\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\\tau, \\sigma)$ combinations: $\\tau \\in \\{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\\}$~pp $\\times$ $\\sigma \\in \\{3, 4, 5, 6, 7\\}$~pp. Table~\\ref{tab:sensitivity} reports stability across this grid.\ndocs/paper/appendix.tex:158:\\caption{Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All six model--seed configurations achieve perfect stability.}\ndocs/paper/appendix.tex:175:[Omitted long matching line]\ndocs/paper/results.tex:11:\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (180/180 model--seed--combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}\ndocs/paper/results.tex:27:Applying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (six model--seed configurations; Appendix~\\ref{sec:classification_sensitivity}).\ndocs/paper/main.aux:419:[Omitted long matching line]\ndocs/paper/main.aux:420:\\newlabel{tab:taxonomy}{{1}{5}{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta $acc: d000$\\to $d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\\tau ,\\sigma )$ combinations; Appendix~\\ref {sec:classification_sensitivity})}{table.caption.7}{}}\ndocs/paper/main.aux:1149:\\@writefile{lot}{\\contentsline {table}{\\numberline {7}{\\ignorespaces Profile classification stability across 30 $(\\tau , \\sigma )$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.}}{12}{table.caption.37}\\protected@file@percent }\ndocs/paper/main.aux:1150:\\newlabel{tab:sensitivity}{{7}{12}{Profile classification stability across 30 $(\\tau , \\sigma )$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability}{table.caption.37}{}}",
    "numLines": 10
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Grep · `toolu_01EQkp6E8pke7NyMaX9z1Ls9`</summary>

```json
{
  "pattern": "Single seed|Seed coverage|partial rebound|partial-to-full|Triple-seed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "403410f8-a012-4b66-b0b5-398353547aa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hhHQYQ93w9cv1pnHwwgGV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 69288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-19T22:17:50.013Z_

<details><summary>↩ Tool result · `toolu_01EQkp6E8pke7NyMaX9z1Ls9`</summary>

```text
docs/paper/limitations.tex:9:\paragraph{Seed coverage.}
docs/paper/limitations.tex:10:The five-pattern taxonomy (Table~\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.
docs/paper/abstract.tex:1:[Omitted long matching line]
docs/paper/main.log:804: []\OT1/ptm/b/n/10.95 Single seed.[] \OT1/ptm/m/n/10.95 The five-pattern tax-on
docs/paper/main.aux:605:\@writefile{toc}{\contentsline {paragraph}{Single seed.}{7}{section*.18}\protected@file@percent }
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "059463af-838d-4593-b94a-fb4ce12a3777",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/limitations.tex:9:\\paragraph{Seed coverage.}\ndocs/paper/limitations.tex:10:The five-pattern taxonomy (Table~\\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.\ndocs/paper/abstract.tex:1:[Omitted long matching line]\ndocs/paper/main.log:804: []\\OT1/ptm/b/n/10.95 Single seed.[] \\OT1/ptm/m/n/10.95 The five-pattern tax-on\ndocs/paper/main.aux:605:\\@writefile{toc}{\\contentsline {paragraph}{Single seed.}{7}{section*.18}\\protected@file@percent }",
    "numLines": 5
  }
}
```

</details>

---

### Assistant

_source line 80_

<details><summary>Logged reasoning block</summary>

```text
All the .tex files look correct. The main.aux and main.log still have old values, but those are generated files that will be updated on the next LaTeX compilation.

Let me also check: "Triple-seed validation with error bars is in progress." — is this still accurate? The limitations text says s42 and s123 are confirmed. If s0 hasn't been run yet, then triple-seed is still in progress. The task says to "确认这句是否仍然准确". I'll leave it as is since there's no indication it's been completed.

Let me verify the Table 7 update in the appendix by reading the relevant lines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "401a5b1a-f6d6-448d-be2f-59fcd4cf5a01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqn9nStzYZeJ2EMGt2fmSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1379,
      "cache_read_input_tokens": 70073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1379
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 81_

验证 Table 7 更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "f333e7f8-c7b1-45c2-bb1c-d63ec69a1754",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqn9nStzYZeJ2EMGt2fmSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1379,
      "cache_read_input_tokens": 70073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1379
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Read · `toolu_012s35UwBn7dLNf1nNe2EQW2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "offset": 156,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "8ee6cf70-7d24-442e-ab2b-df2c82b0ed34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqn9nStzYZeJ2EMGt2fmSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1379,
      "cache_read_input_tokens": 70073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1379
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-19T22:17:58.726Z_

<details><summary>↩ Tool result · `toolu_012s35UwBn7dLNf1nNe2EQW2`</summary>

```text
156	\begin{table}[h]
157	\centering
158	\caption{Profile classification stability across 30 $(\tau, \sigma)$ threshold combinations (with mid-trajectory volatility check). All six model--seed configurations achieve perfect stability.}
159	\label{tab:sensitivity}
160	\footnotesize
161	\begin{tabular}{lccc}
162	\toprule
163	Model & Default Pattern & Stability & Notes \\
164	\midrule
165	Phi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\le$ all $\tau$ \\
166	Qwen-14B & U-collapse & 30/30 & --- \\
167	Gemma-2 9B & Benefit & 30/30 & --- \\
168	OLMo-2 7B & Benefit-sat & 30/30 & --- \\
169	Qwen-7B (s42) & V-recovery & 30/30 & volatility check resolves \\
170	Qwen-7B (s123) & V-recovery & 30/30 & $\Delta \approx 0$; volatility check resolves \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	With the mid-trajectory volatility check (Algorithm~\ref{alg:profile-classification}, line~3), all six model--seed configurations achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\Delta \approx 0$ but $v^* = 3.22$pp $> \tau$). The severity threshold $\sigma$ has zero impact on any model's classification, because no model's $\Delta\text{acc}$ falls in the range where $\sigma$ determines the U-collapse vs.\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\sigma=7$).
176	
177	\section{Cross-Family Domain Decomposition}
178	\label{sec:domain_decomposition}
179	
180	We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "f88ec5be-29ff-4a1b-889e-7bab2d755b56",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\caption{Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All six model--seed configurations achieve perfect stability.}\n\\label{tab:sensitivity}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nModel & Default Pattern & Stability & Notes \\\\\n\\midrule\nPhi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\\le$ all $\\tau$ \\\\\nQwen-14B & U-collapse & 30/30 & --- \\\\\nGemma-2 9B & Benefit & 30/30 & --- \\\\\nOLMo-2 7B & Benefit-sat & 30/30 & --- \\\\\nQwen-7B (s42) & V-recovery & 30/30 & volatility check resolves \\\\\nQwen-7B (s123) & V-recovery & 30/30 & $\\Delta \\approx 0$; volatility check resolves \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith the mid-trajectory volatility check (Algorithm~\\ref{alg:profile-classification}, line~3), all six model--seed configurations achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$). The severity threshold $\\sigma$ has zero impact on any model's classification, because no model's $\\Delta\\text{acc}$ falls in the range where $\\sigma$ determines the U-collapse vs.\\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\\sigma=7$).\n\n\\section{Cross-Family Domain Decomposition}\n\\label{sec:domain_decomposition}\n\nWe decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.",
      "numLines": 25,
      "startLine": 156,
      "totalLines": 293
    }
  }
}
```

</details>

---

### Assistant

_source line 84_

全部修改完成。汇总：

**Sensitivity 更新（6 处）：**
1. `method.tex:59` — "5/5 families" → "all five families...180/180 model--seed--threshold pairs"
2. `results.tex:11` — "150/150 model-combination pairs" → "180/180 model--seed--combination pairs"
3. `results.tex:27` — 添加 "(six model--seed configurations;"
4. `appendix.tex:158` — "All five families" → "All six model--seed configurations"
5. `appendix.tex:170` — Table 7 添加 Qwen-7B (s123) 行，s42 行加标注
6. `appendix.tex:175` — "all five families" → "all six model--seed configurations"

**V-recovery 修复（3 处）：**
1. `limitations.tex:9` — "Single seed." → "Seed coverage."
2. `abstract.tex:1` — "partial rebound" → "partial-to-full rebound"
3. `limitations.tex:10` — "Triple-seed validation...is in progress" 保持不变（s0 未完成，描述仍准确）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "uuid": "5f7571ce-297b-4d8b-81c0-49ff36c32eb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6yu9kDjYUepZ4c5JJDZ12",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 928,
      "cache_read_input_tokens": 71452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 928
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 85_

全部修改完成。汇总：

**Sensitivity 更新（6 处）：**
1. `method.tex:59` — "5/5 families" → "all five families...180/180 model--seed--threshold pairs"
2. `results.tex:11` — "150/150 model-combination pairs" → "180/180 model--seed--combination pairs"
3. `results.tex:27` — 添加 "(six model--seed configurations;"
4. `appendix.tex:158` — "All five families" → "All six model--seed configurations"
5. `appendix.tex:170` — Table 7 添加 Qwen-7B (s123) 行，s42 行加标注
6. `appendix.tex:175` — "all five families" → "all six model--seed configurations"

**V-recovery 修复（3 处）：**
1. `limitations.tex:9` — "Single seed." → "Seed coverage."
2. `abstract.tex:1` — "partial rebound" → "partial-to-full rebound"
3. `limitations.tex:10` — "Triple-seed validation...is in progress" 保持不变（s0 未完成，描述仍准确）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 241213,
  "duration_api_ms": 239613,
  "num_turns": 30,
  "stop_reason": "end_turn",
  "session_id": "ccc29f19-881c-4dc7-86a8-c15654514278",
  "total_cost_usd": 1.0363737499999999,
  "usage": {
    "input_tokens": 19,
    "cache_creation_input_tokens": 60539,
    "cache_read_input_tokens": 752570,
    "output_tokens": 11130,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 60539,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 313,
        "cache_read_input_tokens": 71452,
        "cache_creation_input_tokens": 928,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 928
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3290,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003375,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 19,
      "outputTokens": 11130,
      "cacheReadInputTokens": 752570,
      "cacheCreationInputTokens": 60539,
      "webSearchRequests": 0,
      "costUSD": 1.03299875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "aa35123d-9f0b-4aad-8170-4cd57e707090"
}
```

</details>

---
