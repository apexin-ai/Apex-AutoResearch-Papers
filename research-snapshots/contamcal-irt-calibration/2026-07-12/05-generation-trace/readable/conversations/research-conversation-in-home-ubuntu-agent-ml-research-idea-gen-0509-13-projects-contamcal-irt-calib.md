# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/, I need to find which

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa7f2bbdc86ca52cd.jsonl`
- **Structured JSON:** [`3f8419af48250d532535.json`](../../sessions/3f/3f8419af48250d532535.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-24T05:00:49.992Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/, I need to find which appendix sections are referenced from main text files and which are NOT.

The main text files are: abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex.

The appendix sections have these labels (from appendix.tex):
sec:cross_benchmark_details, sec:arc_cross_benchmark, sec:gsm8k_dose_response, sec:signal_reliability_appendix, sec:rrf_ablation, sec:s2_only_pipeline, sec:identifiability_appendix, sec:dif_comparison, sec:4pl_details, sec:s4_details, sec:training_convergence, sec:exclusion_details, sec:prior_sensitivity, sec:theta_separation, sec:cross_seed_details, sec:did_visualization, sec:did_dosage, sec:mdes, sec:volume_control, sec:dose_response_details, sec:classification_sensitivity, sec:domain_decomposition, sec:baseline_vs_effect, sec:domain_gamma_table, sec:threshold_dgp, sec:arc_irt, sec:full_baselines, sec:parametric_dr, sec:sij_classification, app:ai-assistants

Also check for table/figure labels defined in appendix.tex that are referenced from main text:
tab:gsm8k_transfer, tab:gsm8k_dose, tab:signal_correlation, tab:rrf_ablation, tab:s1_pipeline, tab:s1_domain, tab:dif_comparison, tab:model_sets, tab:socsci_prior, tab:theta_separation, tab:cross_seed, tab:mdes_mmlu, tab:mdes_arc, tab:volume_control, tab:sensitivity, tab:domain_gamma, tab:dgp_coverage, tab:full_baselines_arc, tab:full_baselines_gsm8k, tab:aicc_dr, fig:signal_heatmap, fig:identifiability_heatmap, fig:dose_response_arc, fig:treated_untreated, fig:did_dose_response, fig:baseline_vs_effect

For each appendix label, grep across the main text .tex files (NOT appendix.tex itself) for any \ref{label} or mention. Report two lists:
1. REFERENCED from main text (with which file references it)
2. NOT REFERENCED from any main text file (orphaned appendix sections)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "76f25a71-7c2e-4e43-b3ed-e93852d80d9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T05:00:51.742Z_

I'll help you find which appendix sections are referenced from main text files and which are orphaned. Let me search through the main text files for references to these appendix labels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76f25a71-7c2e-4e43-b3ed-e93852d80d9c",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLofe89HP4yrLkLvcNeR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2daf6feb-4888-4512-9dbb-0e4e3db03107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ACyrygmV1o6m4SXVYiVgLz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 40150,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 40150,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-24T05:00:51.996Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019np2F3bD5U2sc7HNm6g6RM`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper -maxdepth 1 -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2daf6feb-4888-4512-9dbb-0e4e3db03107",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLofe89HP4yrLkLvcNeR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f8e3737a-c244-4d57-9224-48842c846118",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ACyrygmV1o6m4SXVYiVgLz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 40150,
      "cache_read_input_tokens": 0,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 40150
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 142,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 40150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 40150,
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

_source line 4 · 2026-05-24T05:00:52.216Z_

<details><summary>↩ Tool result · `toolu_019np2F3bD5U2sc7HNm6g6RM`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8e3737a-c244-4d57-9224-48842c846118",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "d583f1be-5bdb-4594-9bd3-47909751872d",
  "sourceToolAssistantUUID": "f8e3737a-c244-4d57-9224-48842c846118",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-24T05:00:53.468Z_

Now let me search for all the appendix label references across the main text files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d583f1be-5bdb-4594-9bd3-47909751872d",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLofoXCHFHbDpNro4maT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d1be40b-b5d5-4757-92f4-8df1ad2c90f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Mgve792gwRRUatuDupy7Hz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 40150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 6 · 2026-05-24T05:00:57.276Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013xL5REDz82e8fs7jVP93WQ`</summary>

```json
{
  "pattern": "\\\\ref\\{sec:cross_benchmark_details\\}|\\\\ref\\{sec:arc_cross_benchmark\\}|\\\\ref\\{sec:gsm8k_dose_response\\}|\\\\ref\\{sec:signal_reliability_appendix\\}|\\\\ref\\{sec:rrf_ablation\\}|\\\\ref\\{sec:s2_only_pipeline\\}|\\\\ref\\{sec:identifiability_appendix\\}|\\\\ref\\{sec:dif_comparison\\}|\\\\ref\\{sec:4pl_details\\}|\\\\ref\\{sec:s4_details\\}|\\\\ref\\{sec:training_convergence\\}|\\\\ref\\{sec:exclusion_details\\}|\\\\ref\\{sec:prior_sensitivity\\}|\\\\ref\\{sec:theta_separation\\}|\\\\ref\\{sec:cross_seed_details\\}|\\\\ref\\{sec:did_visualization\\}|\\\\ref\\{sec:did_dosage\\}|\\\\ref\\{sec:mdes\\}|\\\\ref\\{sec:volume_control\\}|\\\\ref\\{sec:dose_response_details\\}|\\\\ref\\{sec:classification_sensitivity\\}|\\\\ref\\{sec:domain_decomposition\\}|\\\\ref\\{sec:baseline_vs_effect\\}|\\\\ref\\{sec:domain_gamma_table\\}|\\\\ref\\{sec:threshold_dgp\\}|\\\\ref\\{sec:arc_irt\\}|\\\\ref\\{sec:full_baselines\\}|\\\\ref\\{sec:parametric_dr\\}|\\\\ref\\{sec:sij_classification\\}|\\\\ref\\{app:ai-assistants\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "glob": "abstract.tex|introduction.tex|related_work.tex|method.tex|experimental_setup.tex|results.tex|conclusion.tex|limitations.tex",
  "output_mode": "content",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d1be40b-b5d5-4757-92f4-8df1ad2c90f8",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLofoXCHFHbDpNro4maT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fc2c06a0-af2a-4c79-9e1b-a343ea7130d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Mgve792gwRRUatuDupy7Hz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 40150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 7 · 2026-05-24T05:00:57.312Z_

<details><summary>↩ Tool result · `toolu_013xL5REDz82e8fs7jVP93WQ`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc2c06a0-af2a-4c79-9e1b-a343ea7130d7",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "245bf4a2-30ab-489c-a7a9-44ac7c0878b9",
  "sourceToolAssistantUUID": "fc2c06a0-af2a-4c79-9e1b-a343ea7130d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T05:00:59.977Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Tk5fjYBsWQ3SpX2uDwxc5R`</summary>

```json
{
  "pattern": "\\\\ref\\{tab:gsm8k_transfer\\}|\\\\ref\\{tab:gsm8k_dose\\}|\\\\ref\\{tab:signal_correlation\\}|\\\\ref\\{tab:rrf_ablation\\}|\\\\ref\\{tab:s1_pipeline\\}|\\\\ref\\{tab:s1_domain\\}|\\\\ref\\{tab:dif_comparison\\}|\\\\ref\\{tab:model_sets\\}|\\\\ref\\{tab:socsci_prior\\}|\\\\ref\\{tab:theta_separation\\}|\\\\ref\\{tab:cross_seed\\}|\\\\ref\\{tab:mdes_mmlu\\}|\\\\ref\\{tab:mdes_arc\\}|\\\\ref\\{tab:volume_control\\}|\\\\ref\\{tab:sensitivity\\}|\\\\ref\\{tab:domain_gamma\\}|\\\\ref\\{tab:dgp_coverage\\}|\\\\ref\\{tab:full_baselines_arc\\}|\\\\ref\\{tab:full_baselines_gsm8k\\}|\\\\ref\\{tab:aicc_dr\\}|\\\\ref\\{fig:signal_heatmap\\}|\\\\ref\\{fig:identifiability_heatmap\\}|\\\\ref\\{fig:dose_response_arc\\}|\\\\ref\\{fig:treated_untreated\\}|\\\\ref\\{fig:did_dose_response\\}|\\\\ref\\{fig:baseline_vs_effect\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "glob": "abstract.tex|introduction.tex|related_work.tex|method.tex|experimental_setup.tex|results.tex|conclusion.tex|limitations.tex",
  "output_mode": "content",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "245bf4a2-30ab-489c-a7a9-44ac7c0878b9",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLofoXCHFHbDpNro4maT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ec975719-732c-4d8a-86ba-9d1a6889f242",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Mgve792gwRRUatuDupy7Hz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 40150,
      "output_tokens": 1130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1130,
          "cache_read_input_tokens": 40150,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1432,
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

_source line 9 · 2026-05-24T05:01:00.011Z_

<details><summary>↩ Tool result · `toolu_01Tk5fjYBsWQ3SpX2uDwxc5R`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec975719-732c-4d8a-86ba-9d1a6889f242",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "87e3a007-2694-4d93-b4f2-93d54e14c347",
  "sourceToolAssistantUUID": "ec975719-732c-4d8a-86ba-9d1a6889f242",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-24T05:01:02.459Z_

Let me try a broader search to see what references exist at all:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87e3a007-2694-4d93-b4f2-93d54e14c347",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLogPGhndTwhMa1yA93D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0a916e9c-5fb1-4a67-bd74-808be2292e22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhpNG9fbMJF2Ynw6oEWHJ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1196,
      "cache_read_input_tokens": 41582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1196,
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

_source line 11 · 2026-05-24T05:01:03.005Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01C2BvMC8RXFXDN3e3ExMmaU`</summary>

```json
{
  "pattern": "\\\\ref\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "glob": "abstract.tex|introduction.tex|related_work.tex|method.tex|experimental_setup.tex|results.tex|conclusion.tex|limitations.tex",
  "output_mode": "content",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a916e9c-5fb1-4a67-bd74-808be2292e22",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLogPGhndTwhMa1yA93D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a4140fa4-c1bb-4cb7-a099-1316da0d10cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhpNG9fbMJF2Ynw6oEWHJ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1196,
      "cache_read_input_tokens": 41582,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1196
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 210,
          "cache_read_input_tokens": 41582,
          "cache_creation_input_tokens": 1196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1196,
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

_source line 12 · 2026-05-24T05:01:03.029Z_

<details><summary>↩ Tool result · `toolu_01C2BvMC8RXFXDN3e3ExMmaU`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4140fa4-c1bb-4cb7-a099-1316da0d10cf",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "e542be26-4493-4519-893c-f019146763c5",
  "sourceToolAssistantUUID": "a4140fa4-c1bb-4cb7-a099-1316da0d10cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-24T05:01:04.872Z_

Let me check the actual content of these files to understand the referencing style:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e542be26-4493-4519-893c-f019146763c5",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLogbrk5GSQoWx5X3JBu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ef2ef29f-32b5-4258-a935-9c333fbe0258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WWefHTdXDH63Srk52VtM6c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 42778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 226,
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

_source line 14 · 2026-05-24T05:01:05.269Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TXKvdU1567EXzh7AEmx7H3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef2ef29f-32b5-4258-a935-9c333fbe0258",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLogbrk5GSQoWx5X3JBu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "864a26f2-f606-4f4b-adc2-42165f804246",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WWefHTdXDH63Srk52VtM6c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 42778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 226,
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

_source line 15 · 2026-05-24T05:01:05.278Z_

<details><summary>↩ Tool result · `toolu_01TXKvdU1567EXzh7AEmx7H3`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled SFT injection (LoRA, five dosage levels) into six models spanning five independent families from five labs (Alibaba, Microsoft, Allen AI, Google, TII) and discover a spectrum of dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4, $\pm$0.5pp) and benefit ($+$3--4pp, three families) to collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
6	
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=0.95\textwidth]{figures/fig_dose_response.pdf}
10	\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; LLaMA-3.1 at seed$=$0). Immune and Benefit replicate across families; Collapse and V-recovery are preliminary (Qwen2.5-specific). Cross-seed stability in Table~\ref{tab:cross_seed}.}
11	\label{fig:dose_response}
12	\end{figure*}
13	
14	Across six models, three lower-baseline models benefit ($+$3.2 to $+$4.2pp), one is immune (Phi-4), and the remaining two (both Qwen2.5) show harm---with the 14B model 5$\times$ more fragile than 7B. These effects are benchmark-conditional: the same model can collapse on MMLU ($-$9.4pp) yet gain on GSM8K ($+$13pp). ContamCal, our diagnostic framework combining multi-signal exposure mapping with contamination-augmented IRT (2PL+$\gamma_k$), enables this characterization.
15	
16	Our contributions:
17	\begin{enumerate}
18	    \item \textbf{Dose-response profiles with cross-seed and cross-benchmark validation.} Controlled injection across five families reveals two replicated patterns (Immune, Benefit) and two preliminary Qwen2.5-specific patterns (Collapse, V-recovery). Out-of-sample validation on LLaMA-3.1-8B confirms generalizability. Cross-benchmark transfer reveals directional reversal on GSM8K for three families. Multi-seed evaluation ($n\!=\!3$) shows direction is reproducible but magnitude is seed-sensitive.
19	    \item \textbf{Domain-level contamination diagnosis via IRT.} ContamCal embeds multi-signal RRF exposure scores in a contamination-augmented IRT model (2PL+$\gamma$)---an application of standard explanatory IRT \citep{deboeck_2004_explanatory_irt} to LLM contamination---enabling domain-level diagnosis with credible intervals. Domain analysis reveals opposing contamination directions (Social Sciences $\gamma_d < 0$, STEM $\gamma_d > 0$) invisible to aggregate scoring. No item-specific memorization is detected via difference-in-differences (MDES 1.25--2.05pp).
20	    \item \textbf{Diagnostic pipeline requirements and signal failure.} Min-K\%++ \citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (paired Cohen's $d = -1.98$ at d100). RRF-based multi-signal fusion is essential: a single-signal pipeline produces severe model misfit (PPP $< 0.001$). Simulation establishes $\gamma$ recovery requires $J \geq 50$ at AUC $\geq 0.55$, above current practice ($J = 8$--$30$).
21	\end{enumerate}
22	
23	\noindent Code and data are available at \url{https://github.com/anonymous-nlp-2026-2/contamcal-irt-calibration}.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "864a26f2-f606-4f4b-adc2-42165f804246",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "0ca8713c-ffc4-44ff-9d04-9e5f7693da18",
  "sourceToolAssistantUUID": "864a26f2-f606-4f4b-adc2-42165f804246",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T05:01:05.354Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PxtVMMzDhBRCcJsVcvs2Ay`</summary>

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
  "parentUuid": "0ca8713c-ffc4-44ff-9d04-9e5f7693da18",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLogbrk5GSQoWx5X3JBu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3e53e4e0-46b3-49fa-9393-11a69a0d5ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WWefHTdXDH63Srk52VtM6c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 42778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 226,
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

_source line 17 · 2026-05-24T05:01:05.363Z_

<details><summary>↩ Tool result · `toolu_01PxtVMMzDhBRCcJsVcvs2Ay`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\resizebox{\columnwidth}{!}{%
7	\begin{tikzpicture}[
8	    stage/.style={draw, rounded corners, minimum width=3.8cm, minimum height=2.8cm, align=center, fill=gray!8, font=\small},
9	    arr/.style={-{Stealth[length=3mm]}, thick},
10	    node distance=0.6cm
11	]
12	\node[stage] (s1) {
13	    \textbf{Stage 1}\\[2pt]
14	    \textit{Multi-Signal}\\
15	    \textit{Exposure Mapping}\\[4pt]
16	    {\scriptsize S1: Embedding Sim.}\\
17	    {\scriptsize S2: Min-K\%++}\\
18	    {\scriptsize S4: Self-Critique}\\[2pt]
19	    {\scriptsize $\xrightarrow{\text{RRF}}\ e_{ij}\!\in\![0,1]$}
20	};
21	\node[stage, right=of s1] (s2) {
22	    \textbf{Stage 2}\\[2pt]
23	    \textit{Contamination-}\\
24	    \textit{Augmented IRT}\\[4pt]
25	    {\scriptsize 2PL+$\gamma_k$ (Eq.~2)}\\
26	    {\scriptsize Bayesian NUTS}\\[2pt]
27	    {\scriptsize $\theta_j^{\text{clean}},\ \gamma_k$ + CIs}
28	};
29	\node[stage, right=of s2] (s3) {
30	    \textbf{Stage 3}\\[2pt]
31	    \textit{Dose-Response}\\
32	    \textit{Profiling}\\[4pt]
33	    {\scriptsize Algorithm~1}\\
34	    {\scriptsize classification}\\[2pt]
35	    {\scriptsize \{Im, Co, V, Be\}}
36	};
37	\draw[arr] (s1) -- (s2);
38	\draw[arr] (s2) -- (s3);
39	\end{tikzpicture}}
40	\caption{ContamCal three-stage pipeline. Stage~1 fuses training-free detection signals into per-item exposure scores via Reciprocal Rank Fusion. Stage~2 embeds these scores in a contamination-augmented 2PL IRT model, recovering clean ability estimates with credible intervals. Stage~3 classifies the resulting dose-response trajectories into canonical patterns.}
41	\label{fig:pipeline}
42	\end{figure}
43	
44	ContamCal operates in three stages (Figure~\ref{fig:pipeline}): Stage~1 estimates per-item contamination exposure via training-free signal fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to recover clean ability estimates with credible intervals; Stage~3 classifies dose-response trajectories into canonical patterns.
45	
46	\subsection{Problem Formulation}
47	\label{sec:formulation}
48	
49	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
50	
51	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
52	
53	\subsection{Stage 1: Multi-Signal Exposure Mapping}
54	\label{sec:stage1}
55	
56	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \citep{kadavath2022}; concurrent work by \citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\mathcal{S} = \{\text{S1, S2, S4}\}$) and applies to any benchmark without auxiliary data. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_failure}. Item-level classification performance of the exposure scores is reported in Appendix~\ref{sec:sij_classification}.
57	
58	We aggregate signals via Reciprocal Rank Fusion \citep[RRF;][]{cormack_2009_rrf}:
59	\begin{equation}
60	\label{eq:rrf}
61	    e_{ij} = \sum_{s \in \mathcal{S}} \frac{1}{\kappa + r_{s}(i)},
62	\end{equation}
63	where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\kappa=60$ is the standard RRF smoothing constant, robust to near-random component signals, and $|\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to $e_{ij} \in [0,1]$; the distribution is highly right-skewed (mean 0.041).
64	
65	\subsection{Stage 2: Contamination-Augmented IRT}
66	\label{sec:stage2}
67	
68	\paragraph{Primary model: 2PL+$\gamma$.}
69	Our primary specification augments the two-parameter logistic (2PL) model \citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:
70	\begin{equation}
71	\label{eq:2pl_gamma}
72	    P(y_{ijk} = 1) = \sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
73	\end{equation}
74	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \in \mathbb{R}$ is item difficulty, $\theta_j$ is model ability, and $\gamma_k$ is the scalar contamination effect for benchmark~$k$ ($\gamma$ without subscript denotes the pooled effect; $\gamma_d$ denotes per-domain effects, \S\ref{sec:domain_differential}). Each benchmark is fitted independently; when finer-grained diagnosis is needed, we replace $\gamma_k$ with per-domain effects $\gamma_d$ ($d=1,\ldots,D$), fitting Eq.~\eqref{eq:2pl_gamma} separately for each cognitive domain within a benchmark (\S\ref{sec:domain_differential}).
75	
76	We place $\gamma_k$ outside the item discrimination bracket, modeling contamination as a fixed logit shift \citep{de_ayala_2009_irt} rather than the uniform DIF form that would scale contamination effects with item discrimination. A comparison with the uniform DIF alternative ($\gamma$ inside the discrimination bracket) yields equivalent model fit (Appendix~\ref{sec:dif_comparison}). For MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\ref{sec:4pl_details}); this requires $J \geq 16$ and is not used in domain-level analyses ($J = 13$).
77	
78	\paragraph{Inference.}
79	We perform Bayesian inference via NUTS \citep{hoffman2014} in Stan \citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_k \sim \mathcal{N}(0,1)$. At $J=16$, the $\gamma$ posterior is sensitive to the prior (up to 2.6$\times$ shift across reasonable alternatives; Appendix~\ref{sec:prior_sensitivity}); we therefore treat $\gamma$ estimates as directional indicators rather than precise effect sizes. Convergence requires split-$\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters. Model fit is assessed via the posterior predictive $p$-value (PPP), where values near 0.5 indicate adequate fit.
80	
81	\paragraph{Calibrated score.}
82	The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:
83	\begin{equation}
84	\label{eq:calibrated}
85	    \text{Acc}_{j}^{\text{cal}} = \frac{1}{I_k} \sum_{i=1}^{I_k}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)\right],
86	\end{equation}
87	with credible intervals from posterior quantiles. In practice, we average $\sigma(a_i(\theta_j - b_i))$ over posterior draws with $e_{ij}=0$; the spread of draws yields the credible interval. Models with noisier exposure signals receive wider intervals by construction.
88	
89	\paragraph{Identifiability.}
90	\label{sec:fisher}
91	\label{sec:value_decomposition}
92	The reliability of $\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\geq$0.55 with $J \geq 50$ (Appendix~\ref{sec:identifiability_appendix}). Empirically, exposure scores $e_{ij}$ and item difficulty $b_i$ are near-orthogonal (Pearson $|r|<0.13$, $R^2<0.014$ across benchmarks), so $\gamma$ is identified from dosage-induced variation rather than confounded with difficulty. Eq.~\eqref{eq:calibrated} depends on $\theta_j$, not $\gamma$ directly, predicting that vanilla 2PL ($\gamma\!=\!0$) achieves comparable calibration to 2PL+$\gamma$, with $\gamma_k$ serving diagnosis rather than calibration (\S\ref{sec:calibration_results}).
93	
94	\subsection{Dose-Response Profile Classification}
95	\label{sec:classification}
96	
97	Independent of the IRT calibration pipeline, we provide a descriptive classification scheme for dose-response profiles, drawing on pharmacological dose-response modeling \citep{hill1910aggregation,ritz2015dose}. Algorithm~\ref{alg:profile-classification} defines a deterministic decision tree over accuracy vectors, parameterized by noise threshold $\tau$ and severity threshold $\sigma$. All thresholds are explicit and adjustable; a 30-combination $(\tau, \sigma)$ grid sweep confirms all families are stable (180/180 pairs; Appendix~\ref{sec:classification_sensitivity}).
98	
99	\begin{algorithm}[!t]
100	\caption{Dose-Response Profile Classification}
101	\label{alg:profile-classification}
102	\begin{algorithmic}[1]
103	\Require Accuracy vector $\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \in \{0, 5, 25, 50, 100\}\%$
104	\Require Noise threshold $\tau = 2$ pp, severity threshold $\sigma = 5$ pp
105	\Ensure Pattern $p \in \{$\textsc{Immune}, \textsc{Collapse},
106	\Statex \hspace{\algorithmicindent}\textsc{V-recovery}, \textsc{Benefit}$\}$
107	\State $\Delta \gets a_{100} - a_{0}$ \Comment{end-to-end accuracy shift}
108	\State $m^* \gets \min(a_{5},\, a_{25},\, a_{50})$ \Comment{mid-dosage minimum}
109	\State $v^* \gets \max_{i \in \{5,25,50\}} |a_i - a_0|$ \Comment{max mid-trajectory deviation}
110	\If{$|\Delta| \le \tau$}
111	    \If{$v^* \le \tau$}
112	        \State \Return \textsc{Immune} \Comment{fluctuation within noise band}
113	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
114	        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
115	    \Else
116	        \State \Return \textsc{Immune} \Comment{non-V volatility, endpoint stable}
117	    \EndIf
118	\ElsIf{$\Delta < -\tau$}
119	    \If{$\Delta \le -\sigma$}
120	        \State \Return \textsc{Collapse} \Comment{severe monotonic degradation}
121	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
122	        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
123	    \Else
124	        \State \Return \textsc{Collapse} \Comment{moderate decline, no V-shape}
125	    \EndIf
126	\Else \Comment{$\Delta > \tau$}
127	    \State \Return \textsc{Benefit} \Comment{net positive shift}
128	\EndIf
129	\end{algorithmic}
130	\end{algorithm}
131	
132	\paragraph{Family-level aggregation.}
133	Algorithm~\ref{alg:profile-classification} classifies individual seed trajectories. Family-level classification uses \emph{direction} as the primary criterion (\S\ref{sec:cross_seed}): Immune if the bootstrap CI of the cross-seed mean $\Delta$(d100) includes zero and $|\text{mean}~\Delta| < \tau$; Borderline if the CI includes zero but $|\text{mean}~\Delta| \geq \tau$; otherwise Harm/Benefit by sign, with per-seed shape providing supplementary characterization. Parametric model selection (Appendix~\ref{sec:parametric_dr}) confirms Algorithm~\ref{alg:profile-classification}'s classifications for extreme effects but lacks power to resolve moderate patterns at $n\!=\!3$ seeds, motivating the per-seed rule-based approach. Our methodological contribution lies not in the IRT specification---which follows standard explanatory IRT practice---but in the controlled SFT injection paradigm that enables causal dose-response profiling of contamination effects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e53e4e0-46b3-49fa-9393-11a69a0d5ce5",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "c6e9e108-b34c-4e35-adcf-2dc2c3d34e41",
  "sourceToolAssistantUUID": "3e53e4e0-46b3-49fa-9393-11a69a0d5ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T05:01:05.603Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MjaVVWdg79fKnXEzDMUEfy`</summary>

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
  "parentUuid": "c6e9e108-b34c-4e35-adcf-2dc2c3d34e41",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLogbrk5GSQoWx5X3JBu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7747509c-ea9c-4fa4-aaa8-28354135f9c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WWefHTdXDH63Srk52VtM6c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 42778,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 226
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 256,
          "cache_read_input_tokens": 42778,
          "cache_creation_input_tokens": 226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 226,
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

_source line 19 · 2026-05-24T05:01:05.610Z_

<details><summary>↩ Tool result · `toolu_01MjaVVWdg79fKnXEzDMUEfy`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family SFT-injection results (\S\ref{sec:taxonomy}) use seed$=$42 data across six models from five independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=0.92\columnwidth]{figures/fig_baseline_vulnerability.pdf}
12	\caption{Baseline MMLU accuracy vs.\ contamination response at d100 ($N\!=\!6$; observational association, not a validated threshold).}
13	\label{fig:baseline_vulnerability}
14	\end{figure}
15	
16	\begin{table}[t]
17	\centering
18	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% bootstrap CI, $B=10{,}000$). Stab.: fraction of bootstrap resamples ($B=10{,}000$) that yield the same Algorithm~\ref{alg:profile-classification} classification. Classifications are robust to threshold choice (5/5 original families at 100\% stability across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
19	\label{tab:taxonomy}
20	\footnotesize
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{llcccccc}
23	\toprule
24	Pattern & Model & d000 Acc. & $\Delta$acc & 95\% CI & Peak & Stab. & Repl. \\
25	\midrule
26	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% & \checkmark \\
27	Collapse & Qwen-14B & 69.4\% & $-$9.4pp\textsuperscript{$\ddagger$} & [$-$12.74, $-$9.0] & --- & 100\% & $\triangle$ \\
28	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% & $\triangle$ \\
29	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & near-mono. & 76.6\% & \checkmark \\
30	Benefit & Falcon3 7B & 58.8\% & $+$4.2pp & [$+$3.60, $+$4.79] & mono. & 96.1\% & \checkmark \\
31	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% & \checkmark \\
32	\bottomrule
33	\multicolumn{8}{l}{\scriptsize $^{\ddagger}$Cross-seed range $-$9.4 to $-$25.0pp (s42/s123/s0); see Table~\ref{tab:cross_seed}.} \\
34	\multicolumn{8}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.55pp ($<$1pp threshold), s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.} \\
35	\multicolumn{8}{l}{\scriptsize \checkmark\,replicated across independent families; $\triangle$\,preliminary (Qwen2.5-specific, pending replication).}
36	\end{tabular}}
37	\end{table}
38	
39	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields a spectrum of dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect.
40	
41	\paragraph{Replication status.}
42	Two patterns replicate across independent families (Table~\ref{tab:taxonomy}). \textit{Immune}: Phi-4 ($\pm$0.5pp), confirmed out-of-sample by LLaMA-3.1 ($-$0.69pp). \textit{Benefit}: three families gain $+$3.2 to $+$4.2pp (Gemma-2, Falcon3, OLMo-2 borderline; \S\ref{sec:cross_seed}). Two patterns are Qwen2.5-specific and await independent replication: Qwen-14B \textit{collapses} ($-$9.4 to $-$25.0pp across seeds) while Qwen-7B shows \textit{V-recovery}. ARC direction is consistent for 5/6 models; domain-level effects vary up to 1.8$\times$ (Appendices~\ref{sec:arc_cross_benchmark},~\ref{sec:domain_decomposition}).
43	
44	\paragraph{Out-of-sample validation.}
45	LLaMA-3.1-8B (Meta; d000, d025, d100) is classified Immune on both MMLU ($-$0.69pp) and ARC ($+$0.09pp), despite matching OLMo-2's Benefit baseline (53.5\% vs.\ 53.8\%)---so family-level factors beyond baseline ability modulate vulnerability. LLaMA-3.1 also shows the strongest GSM8K transfer ($+$16.4pp; Appendix~\ref{sec:gsm8k_dose_response}): target-benchmark immunity does not imply transfer immunity.
46	
47	\subsection{Cross-Benchmark Transfer}
48	\label{sec:gsm8k_transfer}
49	
50	\begin{figure}[t]
51	\centering
52	\includegraphics[width=0.88\columnwidth]{figures/fig_cross_benchmark_heatmap.pdf}
53	\caption{Cross-benchmark transfer at d100. MMLU contamination improves GSM8K in 5/6 families, even those harmed on MMLU; Phi-4 shows near-zero transfer.}
54	\label{fig:cross_benchmark_heatmap}
55	\end{figure}
56	
57	Contamination patterns are a property of the (model, benchmark) pair, not the model alone. Within-MCQ direction agreement is 86\% (6/7 families; Appendix~\ref{sec:arc_cross_benchmark}); across formats (MCQ$\to$generative math), agreement drops to 50\% with three families reversing on GSM8K \citep{cobbe2021gsm8k} (Table~\ref{tab:gsm8k_transfer}). Qwen-14B ($-$9.4pp MMLU) gains $+$13.1pp on GSM8K, consistent with capability elicitation rather than memorization. Volume effects are ruled out: d005 ($+$1.5\% data) already yields $+$6.4pp GSM8K transfer for Qwen-7B.
58	
59	\subsection{Cross-Seed Stability}
60	\label{sec:cross_seed}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{figures/fig_cross_seed_ci.pdf}
65	\caption{Cross-seed mean $\Delta$acc at d100 with BCa 95\% CIs ($n\!=\!3$ seeds; Falcon3 $n\!=\!2$). Filled markers: CI excludes zero.}
66	\label{fig:cross_seed_ci}
67	\end{figure}
68	
69	Gemma-2 is the only family with a statistically significant cross-seed Benefit (BCa 95\% CI $[+1.49, +3.14]$; Figure~\ref{fig:cross_seed_ci}); Falcon3 and OLMo-2 are directionally consistent but exploratory (Table~\ref{tab:cross_seed}). Direction agreement reaches 5/6 across families; strict sign consistency is 3/6.
70	
71	\subsection{Item-Level Memorization Test}
72	\label{sec:memorization_test}
73	
74	We test whether dose-response patterns arise from item-specific memorization using the treated/untreated split at d025 (3{,}540 / 10{,}502 MMLU items). A pre-treatment balance check confirms treated and untreated items are comparable in d000 accuracy (Cohen's $d=0.02$), difficulty distribution, and domain coverage (all $p>0.19$), supporting the parallel trends assumption. No model shows significant DiD ($p > 0.05$; Table~\ref{tab:did}), ruling out item-specific effects $>$2pp (MDES 1.25--2.05pp; ARC MDES in Appendix~\ref{sec:mdes}). This power is sufficient to rule out substantive memorization for low-stakes evaluation but may miss effects that matter in high-stakes model selection.
75	
76	\begin{table}[t]
77	\centering
78	\caption{Treated vs.\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}
79	\label{tab:did}
80	\footnotesize
81	\resizebox{\columnwidth}{!}{%
82	\begin{tabular}{lcccc}
83	\toprule
84	Model & Treated $\Delta$ & Untreated $\Delta$ & DiD & Verdict \\
85	\midrule
86	Gemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.5 (ns) & generalization \\
87	OLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\
88	Phi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\
89	Qwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\
90	Qwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\
91	\bottomrule
92	\end{tabular}}
93	\end{table}
94	
95	Parallel changes suggest global capability modulation (Figure~\ref{fig:treated_untreated}, Appendix).
96	
97	\paragraph{Volume control.}
98	A volume-matched control (Falcon3-7B trained on 66{,}533 non-benchmark MCQ items; Appendix~\ref{sec:volume_control}) achieves 60.67\% MMLU, decomposing the $+$4.19pp Benefit into data quantity ($+$1.90pp, 45\%) and contamination content ($+$2.29pp, 55\%); ARC yields a consistent 43\%/57\% split; GSM8K shows 53\%/47\% ($+$0.68pp/$+$0.61pp of $+$1.29pp total). Collapse ($-$9.4pp) and Immune ($<$1pp) cannot arise from volume effects that produce $+$1.90pp in the control.
99	
100	\subsection{Diagnostic Utility}
101	\label{sec:calibration_results}
102	
103	Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. IRT is fitted on 300 randomly subsampled items (2.1\% of MMLU; representative by KS/$\chi^2$ tests, all $p > 0.5$); RRF exposure scoring achieves $\tau = 0.73$ ($\Delta\tau = 0.18$ vs.\ random; ablation in Appendix~\ref{sec:rrf_ablation}). A single-signal (Min-K\%++) pipeline shows severe model misfit (PPP $< 0.001$ vs.\ $0.193$; Appendix~\ref{sec:s2_only_pipeline}), confirming multi-signal fusion is essential.
104	
105	ContamCal's primary diagnostic value lies in domain-level $\gamma_d$ estimates with credible intervals: Social Sciences $\gamma_d = -0.63$ ($P(\gamma_d\!<\!0) = 99.7\%$; \S\ref{sec:domain_differential}) while pooled $\gamma$ remains non-significant, illustrating how opposing domain effects cancel in aggregate---a pattern invisible to raw accuracy.
106	
107	Table~\ref{tab:baselines} compares methods on 300 randomly subsampled items with RRF exposure scores. Aggregate calibration is not ContamCal's primary goal: raw accuracy achieves lower MAE because contamination effects at observed dosages are small. B6-DCR systematically overcorrects (MAE 0.108). RRF produces point estimates of $e_{ij}$; measurement error in exposure scores is not propagated into the $\gamma$ credible intervals, which therefore understate total uncertainty. Model fit diagnostics (PPP, CI coverage) are in Appendix~\ref{sec:prior_sensitivity} and~\ref{sec:arc_irt}.
108	
109	\begin{table}[t]
110	\centering
111	\caption{MMLU method comparison on 300 randomly subsampled items (Qwen2.5, $J$=16). ARC results in Appendix~\ref{sec:arc_irt}.}
112	\label{tab:baselines}
113	\footnotesize
114	\begin{tabular}{lcc}
115	\toprule
116	Method & MAE & $\tau$ \\
117	\midrule
118	B0: Raw Accuracy & \textbf{0.006} & 0.767 \\
119	B1b: Remove \& Rescore & 0.026 & \underline{0.783} \\
120	B3: Vanilla 2PL & 0.008 & 0.731 \\
121	B4: Linear Regression & 0.010 & 0.751 \\
122	B5b: Emperor & \textbf{0.006} & \textbf{0.789} \\
123	B6: DCR (reimpl.) & 0.108 & 0.654 \\
124	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 \\
125	\bottomrule
126	\end{tabular}
127	\end{table}
128	
129	\subsection{Detection Signal Failure Modes}
130	\label{sec:signal_failure}
131	
132	Min-K\%++ \citep{zhang_2024_minkpp} exhibits \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores (paired Cohen's $d = -1.98$ at d100, $|d| > 1.2$ at d005). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
133	
134	\subsection{Domain-Level Analysis}
135	\label{sec:domain_differential}
136	
137	\begin{figure}[t]
138	\centering
139	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
140	\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5; $J$=16 estimates differ by $<$10\%, Table~\ref{tab:domain_gamma}).}
141	\label{fig:domain_gamma}
142	\end{figure}
143	
144	Within-family domain analysis (Qwen2.5, $J=16$) reveals directional heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% Bayesian credible interval $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722; Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Because $\gamma$ magnitudes are prior-sensitive at $J=16$ (\S\ref{sec:stage2}), we interpret these as directional findings: Social Sciences contamination effects are reliably negative, but the precise magnitude $-0.63$ should not be over-interpreted. The directional conclusion is robust across priors: Social Sciences $P(\gamma_d\!<\!0)$ is 99.35--99.85\% (Table~\ref{tab:socsci_prior}), exceeding the Bonferroni threshold ($99.375\%$) under baseline and loose priors but falling 0.025\,pp short under the tight prior $\mathcal{N}(0, 0.5)$. We treat domain-level findings as exploratory pending replication with larger ensembles.
145	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7747509c-ea9c-4fa4-aaa8-28354135f9c4",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "085b76e2-cbc0-4b0c-bb69-17d0de5c367b",
  "sourceToolAssistantUUID": "7747509c-ea9c-4fa4-aaa8-28354135f9c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-24T05:01:07.266Z_

Now let me search more carefully for references to appendix sections. Let me check if they use different syntax:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "085b76e2-cbc0-4b0c-bb69-17d0de5c367b",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLognsXVcPXzzNqrHUK8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d3237b72-f6be-48e8-b15b-9edafa56064b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013zyyz8ZeiEEezbdzWQKMRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10773,
      "cache_read_input_tokens": 43004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10773,
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

_source line 21 · 2026-05-24T05:01:11.444Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QNFUZAS6TFrMyiv76ih5TX`</summary>

```json
{
  "command": "grep -n \"sec:cross_benchmark_details\\|sec:arc_cross_benchmark\\|sec:gsm8k_dose_response\\|sec:signal_reliability_appendix\\|sec:rrf_ablation\\|sec:s2_only_pipeline\\|sec:identifiability_appendix\\|sec:dif_comparison\\|sec:4pl_details\\|sec:s4_details\\|sec:training_convergence\\|sec:exclusion_details\\|sec:prior_sensitivity\\|sec:theta_separation\\|sec:cross_seed_details\\|sec:did_visualization\\|sec:did_dosage\\|sec:mdes\\|sec:volume_control\\|sec:dose_response_details\\|sec:classification_sensitivity\\|sec:domain_decomposition\\|sec:baseline_vs_effect\\|sec:domain_gamma_table\\|sec:threshold_dgp\\|sec:arc_irt\\|sec:full_baselines\\|sec:parametric_dr\\|sec:sij_classification\\|app:ai-assistants\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3237b72-f6be-48e8-b15b-9edafa56064b",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLognsXVcPXzzNqrHUK8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c422bf42-b53c-445f-aa4c-1e310dace602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013zyyz8ZeiEEezbdzWQKMRX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10773,
      "cache_read_input_tokens": 43004,
      "output_tokens": 647,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10773
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 647,
          "cache_read_input_tokens": 43004,
          "cache_creation_input_tokens": 10773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10773,
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

_source line 22 · 2026-05-24T05:01:11.540Z_

<details><summary>↩ Tool result · `toolu_01QNFUZAS6TFrMyiv76ih5TX`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex:56:For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \citep{kadavath2022}; concurrent work by \citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\mathcal{S} = \{\text{S1, S2, S4}\}$) and applies to any benchmark without auxiliary data. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_failure}. Item-level classification performance of the exposure scores is reported in Appendix~\ref{sec:sij_classification}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex:76:We place $\gamma_k$ outside the item discrimination bracket, modeling contamination as a fixed logit shift \citep{de_ayala_2009_irt} rather than the uniform DIF form that would scale contamination effects with item discrimination. A comparison with the uniform DIF alternative ($\gamma$ inside the discrimination bracket) yields equivalent model fit (Appendix~\ref{sec:dif_comparison}). For MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\ref{sec:4pl_details}); this requires $J \geq 16$ and is not used in domain-level analyses ($J = 13$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex:79:We perform Bayesian inference via NUTS \citep{hoffman2014} in Stan \citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_k \sim \mathcal{N}(0,1)$. At $J=16$, the $\gamma$ posterior is sensitive to the prior (up to 2.6$\times$ shift across reasonable alternatives; Appendix~\ref{sec:prior_sensitivity}); we therefore treat $\gamma$ estimates as directional indicators rather than precise effect sizes. Convergence requires split-$\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters. Model fit is assessed via the posterior predictive $p$-value (PPP), where values near 0.5 indicate adequate fit.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex:92:The reliability of $\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\geq$0.55 with $J \geq 50$ (Appendix~\ref{sec:identifiability_appendix}). Empirically, exposure scores $e_{ij}$ and item difficulty $b_i$ are near-orthogonal (Pearson $|r|<0.13$, $R^2<0.014$ across benchmarks), so $\gamma$ is identified from dosage-induced variation rather than confounded with difficulty. Eq.~\eqref{eq:calibrated} depends on $\theta_j$, not $\gamma$ directly, predicting that vanilla 2PL ($\gamma\!=\!0$) achieves comparable calibration to 2PL+$\gamma$, with $\gamma_k$ serving diagnosis rather than calibration (\S\ref{sec:calibration_results}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex:97:Independent of the IRT calibration pipeline, we provide a descriptive classification scheme for dose-response profiles, drawing on pharmacological dose-response modeling \citep{hill1910aggregation,ritz2015dose}. Algorithm~\ref{alg:profile-classification} defines a deterministic decision tree over accuracy vectors, parameterized by noise threshold $\tau$ and severity threshold $\sigma$. All thresholds are explicit and adjustable; a 30-combination $(\tau, \sigma)$ grid sweep confirms all families are stable (180/180 pairs; Appendix~\ref{sec:classification_sensitivity}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex:133:Algorithm~\ref{alg:profile-classification} classifies individual seed trajectories. Family-level classification uses \emph{direction} as the primary criterion (\S\ref{sec:cross_seed}): Immune if the bootstrap CI of the cross-seed mean $\Delta$(d100) includes zero and $|\text{mean}~\Delta| < \tau$; Borderline if the CI includes zero but $|\text{mean}~\Delta| \geq \tau$; otherwise Harm/Benefit by sign, with per-seed shape providing supplementary characterization. Parametric model selection (Appendix~\ref{sec:parametric_dr}) confirms Algorithm~\ref{alg:profile-classification}'s classifications for extreme effects but lacks power to resolve moderate patterns at $n\!=\!3$ seeds, motivating the per-seed rule-based approach. Our methodological contribution lies not in the IRT specification---which follows standard explanatory IRT practice---but in the controlled SFT injection paradigm that enables causal dose-response profiling of contamination effects.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:18:\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% bootstrap CI, $B=10{,}000$). Stab.: fraction of bootstrap resamples ($B=10{,}000$) that yield the same Algorithm~\ref{alg:profile-classification} classification. Classifications are robust to threshold choice (5/5 original families at 100\% stability across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:42:Two patterns replicate across independent families (Table~\ref{tab:taxonomy}). \textit{Immune}: Phi-4 ($\pm$0.5pp), confirmed out-of-sample by LLaMA-3.1 ($-$0.69pp). \textit{Benefit}: three families gain $+$3.2 to $+$4.2pp (Gemma-2, Falcon3, OLMo-2 borderline; \S\ref{sec:cross_seed}). Two patterns are Qwen2.5-specific and await independent replication: Qwen-14B \textit{collapses} ($-$9.4 to $-$25.0pp across seeds) while Qwen-7B shows \textit{V-recovery}. ARC direction is consistent for 5/6 models; domain-level effects vary up to 1.8$\times$ (Appendices~\ref{sec:arc_cross_benchmark},~\ref{sec:domain_decomposition}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:45:LLaMA-3.1-8B (Meta; d000, d025, d100) is classified Immune on both MMLU ($-$0.69pp) and ARC ($+$0.09pp), despite matching OLMo-2's Benefit baseline (53.5\% vs.\ 53.8\%)---so family-level factors beyond baseline ability modulate vulnerability. LLaMA-3.1 also shows the strongest GSM8K transfer ($+$16.4pp; Appendix~\ref{sec:gsm8k_dose_response}): target-benchmark immunity does not imply transfer immunity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:57:Contamination patterns are a property of the (model, benchmark) pair, not the model alone. Within-MCQ direction agreement is 86\% (6/7 families; Appendix~\ref{sec:arc_cross_benchmark}); across formats (MCQ$\to$generative math), agreement drops to 50\% with three families reversing on GSM8K \citep{cobbe2021gsm8k} (Table~\ref{tab:gsm8k_transfer}). Qwen-14B ($-$9.4pp MMLU) gains $+$13.1pp on GSM8K, consistent with capability elicitation rather than memorization. Volume effects are ruled out: d005 ($+$1.5\% data) already yields $+$6.4pp GSM8K transfer for Qwen-7B.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:74:We test whether dose-response patterns arise from item-specific memorization using the treated/untreated split at d025 (3{,}540 / 10{,}502 MMLU items). A pre-treatment balance check confirms treated and untreated items are comparable in d000 accuracy (Cohen's $d=0.02$), difficulty distribution, and domain coverage (all $p>0.19$), supporting the parallel trends assumption. No model shows significant DiD ($p > 0.05$; Table~\ref{tab:did}), ruling out item-specific effects $>$2pp (MDES 1.25--2.05pp; ARC MDES in Appendix~\ref{sec:mdes}). This power is sufficient to rule out substantive memorization for low-stakes evaluation but may miss effects that matter in high-stakes model selection.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:98:A volume-matched control (Falcon3-7B trained on 66{,}533 non-benchmark MCQ items; Appendix~\ref{sec:volume_control}) achieves 60.67\% MMLU, decomposing the $+$4.19pp Benefit into data quantity ($+$1.90pp, 45\%) and contamination content ($+$2.29pp, 55\%); ARC yields a consistent 43\%/57\% split; GSM8K shows 53\%/47\% ($+$0.68pp/$+$0.61pp of $+$1.29pp total). Collapse ($-$9.4pp) and Immune ($<$1pp) cannot arise from volume effects that produce $+$1.90pp in the control.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:103:Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. IRT is fitted on 300 randomly subsampled items (2.1\% of MMLU; representative by KS/$\chi^2$ tests, all $p > 0.5$); RRF exposure scoring achieves $\tau = 0.73$ ($\Delta\tau = 0.18$ vs.\ random; ablation in Appendix~\ref{sec:rrf_ablation}). A single-signal (Min-K\%++) pipeline shows severe model misfit (PPP $< 0.001$ vs.\ $0.193$; Appendix~\ref{sec:s2_only_pipeline}), confirming multi-signal fusion is essential.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:107:Table~\ref{tab:baselines} compares methods on 300 randomly subsampled items with RRF exposure scores. Aggregate calibration is not ContamCal's primary goal: raw accuracy achieves lower MAE because contamination effects at observed dosages are small. B6-DCR systematically overcorrects (MAE 0.108). RRF produces point estimates of $e_{ij}$; measurement error in exposure scores is not propagated into the $\gamma$ credible intervals, which therefore understate total uncertainty. Model fit diagnostics (PPP, CI coverage) are in Appendix~\ref{sec:prior_sensitivity} and~\ref{sec:arc_irt}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:111:\caption{MMLU method comparison on 300 randomly subsampled items (Qwen2.5, $J$=16). ARC results in Appendix~\ref{sec:arc_irt}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:132:Min-K\%++ \citep{zhang_2024_minkpp} exhibits \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores (paired Cohen's $d = -1.98$ at d100, $|d| > 1.2$ at d005). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c422bf42-b53c-445f-aa4c-1e310dace602",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "d69684f9-3aea-4f23-aca5-6301c0189a1c",
  "sourceToolAssistantUUID": "c422bf42-b53c-445f-aa4c-1e310dace602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-24T05:01:12.818Z_

Good! Now let me continue searching for the remaining appendix labels and table/figure references:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d69684f9-3aea-4f23-aca5-6301c0189a1c",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohE9ZBGxG2phLyVKKC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "052da2c9-81f1-4139-8171-06541eb194ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DMR6cqCKHvzsQHoiKW7juD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4431,
      "cache_read_input_tokens": 53777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4431,
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

_source line 24 · 2026-05-24T05:01:16.077Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XMAUDgjdig2sSQWxjUoVq8`</summary>

```json
{
  "command": "grep -n \"tab:gsm8k_transfer\\|tab:gsm8k_dose\\|tab:signal_correlation\\|tab:rrf_ablation\\|tab:s1_pipeline\\|tab:s1_domain\\|tab:dif_comparison\\|tab:model_sets\\|tab:socsci_prior\\|tab:theta_separation\\|tab:cross_seed\\|tab:mdes_mmlu\\|tab:mdes_arc\\|tab:volume_control\\|tab:sensitivity\\|tab:domain_gamma\\|tab:dgp_coverage\\|tab:full_baselines_arc\\|tab:full_baselines_gsm8k\\|tab:aicc_dr\\|fig:signal_heatmap\\|fig:identifiability_heatmap\\|fig:dose_response_arc\\|fig:treated_untreated\\|fig:did_dose_response\\|fig:baseline_vs_effect\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "052da2c9-81f1-4139-8171-06541eb194ad",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohE9ZBGxG2phLyVKKC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98ac2c1b-dbd1-4d7c-b07f-d4ea266fc288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DMR6cqCKHvzsQHoiKW7juD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4431,
      "cache_read_input_tokens": 53777,
      "output_tokens": 615,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4431
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 615,
          "cache_read_input_tokens": 53777,
          "cache_creation_input_tokens": 4431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4431,
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

_source line 25 · 2026-05-24T05:01:16.138Z_

<details><summary>↩ Tool result · `toolu_01XMAUDgjdig2sSQWxjUoVq8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex:10:\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; LLaMA-3.1 at seed$=$0). Immune and Benefit replicate across families; Collapse and V-recovery are preliminary (Qwen2.5-specific). Cross-seed stability in Table~\ref{tab:cross_seed}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:33:\multicolumn{8}{l}{\scriptsize $^{\ddagger}$Cross-seed range $-$9.4 to $-$25.0pp (s42/s123/s0); see Table~\ref{tab:cross_seed}.} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:57:Contamination patterns are a property of the (model, benchmark) pair, not the model alone. Within-MCQ direction agreement is 86\% (6/7 families; Appendix~\ref{sec:arc_cross_benchmark}); across formats (MCQ$\to$generative math), agreement drops to 50\% with three families reversing on GSM8K \citep{cobbe2021gsm8k} (Table~\ref{tab:gsm8k_transfer}). Qwen-14B ($-$9.4pp MMLU) gains $+$13.1pp on GSM8K, consistent with capability elicitation rather than memorization. Volume effects are ruled out: d005 ($+$1.5\% data) already yields $+$6.4pp GSM8K transfer for Qwen-7B.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:69:Gemma-2 is the only family with a statistically significant cross-seed Benefit (BCa 95\% CI $[+1.49, +3.14]$; Figure~\ref{fig:cross_seed_ci}); Falcon3 and OLMo-2 are directionally consistent but exploratory (Table~\ref{tab:cross_seed}). Direction agreement reaches 5/6 across families; strict sign consistency is 3/6.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:95:Parallel changes suggest global capability modulation (Figure~\ref{fig:treated_untreated}, Appendix).
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:140:\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5; $J$=16 estimates differ by $<$10\%, Table~\ref{tab:domain_gamma}).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:144:Within-family domain analysis (Qwen2.5, $J=16$) reveals directional heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% Bayesian credible interval $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722; Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Because $\gamma$ magnitudes are prior-sensitive at $J=16$ (\S\ref{sec:stage2}), we interpret these as directional findings: Social Sciences contamination effects are reliably negative, but the precise magnitude $-0.63$ should not be over-interpreted. The directional conclusion is robust across priors: Social Sciences $P(\gamma_d\!<\!0)$ is 99.35--99.85\% (Table~\ref{tab:socsci_prior}), exceeding the Bonferroni threshold ($99.375\%$) under baseline and loose priors but falling 0.025\,pp short under the tight prior $\mathcal{N}(0, 0.5)$. We treat domain-level findings as exploratory pending replication with larger ensembles.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98ac2c1b-dbd1-4d7c-b07f-d4ea266fc288",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "30d88c97-3e73-4342-8a99-002c31b78e52",
  "sourceToolAssistantUUID": "98ac2c1b-dbd1-4d7c-b07f-d4ea266fc288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-24T05:01:17.493Z_

Now let me check the remaining files and look for more references:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30d88c97-3e73-4342-8a99-002c31b78e52",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohZnWSj66ggftuJECb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "21460589-fb9c-4704-bb91-07a02283107b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018g157p1tysTm3Scy31BpGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 58208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1789,
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

_source line 27 · 2026-05-24T05:01:17.880Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ujx7MHVjW9PHGr2RnwnXqM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21460589-fb9c-4704-bb91-07a02283107b",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohZnWSj66ggftuJECb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ac665f6a-5694-4fce-8a65-ec88db52e462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018g157p1tysTm3Scy31BpGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 58208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1789,
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

_source line 28 · 2026-05-24T05:01:17.886Z_

<details><summary>↩ Tool result · `toolu_01Ujx7MHVjW9PHGr2RnwnXqM`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning five independent model families from five labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), Gemma-2 \citep{gemmateam2024gemma2} (9B), and Falcon3 \citep{tiiuae2024falcon3} (7B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, dropout$=0$, targeting all attention and MLP projections; lr$=5\times10^{-5}$, bf16, 1 epoch, batch size$=1$, gradient accumulation$=16$, warmup ratio$=0.03$; trainable parameters range from 0.45\% of Phi-4 14.7B to 2.10\% of Qwen2.5-0.5B) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus, yielding 50.0k (d000), 50.8k (d005), 54.1k (d025), 58.3k (d050), and 66.5k (d100) total training examples ($+$33\% volume at d100 vs.\ d000).
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The four cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 55 checkpoints spanning nine sizes across five families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}). We additionally validate our dose-response profiles on a held-out sixth family, LLaMA-3.1-8B \citep{grattafiori2024llama3} (Meta), which was not used during profile construction. LLaMA-3.1 is trained at three dosage levels (d000, d025, d100) to verify that Algorithm~\ref{alg:profile-classification} generalizes to unseen model families.
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
17	
18	\textbf{ARC-Challenge} \citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.
19	
20	\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought reasoning: the d000 baseline drops to 17.8\% (vs.\ 73--84\% for other families), indicating CoT collapse rather than a contamination effect.
21	
22	All multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.
23	
24	We assess calibration quality via MAE (calibrated vs.\ ground-truth clean accuracy), Kendall $\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\gamma$ direction ($P(\gamma\!<\!0 \mid \text{data})$), and split-$\hat{R}$ convergence.
25	
26	\subsection{Baselines}
27	\label{sec:baselines}
28	
29	We compare against seven baselines: \textbf{B0-Raw} (no adjustment), \textbf{B1-Remove\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \textbf{B2-Single2PL+$\gamma$} (aggregate $\gamma$ without domain stratification), \textbf{B3-Vanilla2PL} ($\gamma=0$, isolating IRT ability estimation), \textbf{B4-LinearRegression} (residuals on exposure scores), \textbf{B5-Emperor} (mitigation strategies from \citet{sun2025emperor}; B5b uses the best-performing variant), and \textbf{B6-DCR} (our reimplementation following \citealp{xu2025dcr}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac665f6a-5694-4fce-8a65-ec88db52e462",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "874374d3-dad5-49ab-95a4-06424f6401b3",
  "sourceToolAssistantUUID": "ac665f6a-5694-4fce-8a65-ec88db52e462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T05:01:17.976Z_

<details open><summary>🔧 Tool call — Read · `toolu_017dfgvGSBhfZo9y9fxcT5pP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "874374d3-dad5-49ab-95a4-06424f6401b3",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohZnWSj66ggftuJECb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "32a2ff54-197d-427b-beb3-c6f09bbd255e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018g157p1tysTm3Scy31BpGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 58208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1789,
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

_source line 30 · 2026-05-24T05:01:17.983Z_

<details><summary>↩ Tool result · `toolu_017dfgvGSBhfZo9y9fxcT5pP`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Controlled SFT injection reveals a spectrum of dose-response patterns---not uniform inflation. Two replicate across independent families (Benefit, Immune); two are Qwen2.5-specific and await replication. DiD finds no item-specific memorization (MDES 1.25--2.05pp); direction reproduces across seeds but magnitude is seed-sensitive.
4	
5	\paragraph{Contamination vs.\ additional training.}
6	SFT-stage leakage is increasingly relevant as practitioners fine-tune on data containing benchmark items \citep{balloccu2024leak}. Our injection confounds content, volume ($+$33\% at d100), and LoRA updates; a volume-matched control attributes ${\sim}$45\% of Benefit to quantity. Combined with null item-specific memorization (\S\ref{sec:memorization_test}), this suggests contamination operates through global capability modulation rather than item-level lookup.
7	
8	\paragraph{Implications for practice.}
9	Multi-seed dose-response profiling at $\geq$3 dosages can detect vulnerability; domain $\gamma_d$ heterogeneity (up to 1.8$\times$) motivates domain-level controls, and ContamCal can flag anomalous profiles given $J \geq 50$.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32a2ff54-197d-427b-beb3-c6f09bbd255e",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "10085618-060e-4a7d-b0d0-abcfde260184",
  "sourceToolAssistantUUID": "32a2ff54-197d-427b-beb3-c6f09bbd255e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T05:01:18.246Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DCwazz7VmPuQwtsrNBwkZx`</summary>

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
  "parentUuid": "10085618-060e-4a7d-b0d0-abcfde260184",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohZnWSj66ggftuJECb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68949d72-4158-4beb-a1f3-e61f285c5681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018g157p1tysTm3Scy31BpGS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 58208,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1789
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 255,
          "cache_read_input_tokens": 58208,
          "cache_creation_input_tokens": 1789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1789,
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

_source line 32 · 2026-05-24T05:01:18.258Z_

<details><summary>↩ Tool result · `toolu_01DCwazz7VmPuQwtsrNBwkZx`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All experiments use models $\leq$14.7B parameters; 70B+ models may exhibit qualitatively different contamination dynamics. With $n\!=\!3$ seeds per family, effect \emph{direction} is reproducible but magnitude is seed-sensitive, and borderline classifications (e.g., OLMo-2) should be interpreted with caution.
5	
6	Our LoRA-based SFT injection differs from pretraining-stage leakage via web crawl ingestion, and dosage levels assume uniform injection of all benchmark items; real-world contamination may follow skewed exposure distributions. The AUGMENT protocol also increases training volume with dosage ($+$33\% at d100); a volume-matched control attributes ${\sim}$45\% of Benefit to data quantity, though this decomposition is available only for Falcon3.
7	
8	Out-of-sample validation covers only the Immune pattern; Collapse and V-recovery are Qwen2.5-specific and await independent-family replication. IRT is fitted on 300 subsampled items (2.1\% of MMLU), and RRF exposure scores are point estimates whose measurement uncertainty is not propagated into $\gamma$ credible intervals.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68949d72-4158-4beb-a1f3-e61f285c5681",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "15c67c54-598b-49b4-b7e2-3e07ff592836",
  "sourceToolAssistantUUID": "68949d72-4158-4beb-a1f3-e61f285c5681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-24T05:01:20.284Z_

Let me check related_work.tex and abstract.tex:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15c67c54-598b-49b4-b7e2-3e07ff592836",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohj1PWzLAqEUuK2T8L",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "24f37ea3-9b10-4d3d-94df-8c2903dcd6fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4kTfXJHmQeoWVY7A8bZ2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2436,
      "cache_read_input_tokens": 59997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2436,
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

_source line 34 · 2026-05-24T05:01:21.209Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GwuiwYWc7KbPsv4psommky`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24f37ea3-9b10-4d3d-94df-8c2903dcd6fa",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohj1PWzLAqEUuK2T8L",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2263223f-01d5-4b92-aa81-4601c50933a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4kTfXJHmQeoWVY7A8bZ2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2436,
      "cache_read_input_tokens": 59997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2436,
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

_source line 35 · 2026-05-24T05:01:21.216Z_

<details><summary>↩ Tool result · `toolu_01GwuiwYWc7KbPsv4psommky`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Contamination detection and mitigation.}
4	Detection methods flag contaminated items via token-level surprisal \citep{shi_2023_minkprob,zhang_2024_minkpp}, accuracy gaps on paraphrases or rephrased items \citep{dekoninck2024constat,yang2023rethinking}, kernel divergence \citep{choi_2025_kds}, completion probes \citep{dong_2024_cdd,golchin2024time}, and parallel test sets \citep{zhang_2024_gsm1k}; see \citet{chen2025benchmarking,singh2024evaluation,sainz2023nlp} for surveys. \citet{balloccu2024leak} document contamination malpractices in closed-source LLMs; \citet{bordt2025forget} argue that contamination effects are often negligible in practice. Earlier work characterized contamination as memorization \citep{carlini2023quantifying,magar_2022_contamination,li_2024_task_contamination,xu_2024_leakage}; \citet{tao2025detecting} and \citet{kocyigit2025impact} address RL post-training. These methods perform binary classification without quantifying effect sizes. On mitigation, \citet{sun2025emperor} find none of twenty approaches reliably restores clean performance; DCR \citep{xu2025dcr} estimates decontaminated scores but without uncertainty quantification. ContamCal consumes detection signals as inputs and produces calibrated ability with credible intervals. Three concurrent lines of work directly address contamination quantification. \citet{han2026quantifying} apply observational DIF to detect contamination without controlled dosage, achieving detection but not dose-response profiling. \citet{schaeffer2026causally} perform controlled pretraining-stage injection with larger seed counts ($n\!=\!10$), establishing causal contamination effects at the pretraining level; our $n\!=\!3$ seed design trades statistical power for broader family coverage. Our work complements both: like Schaeffer et al., we use controlled injection for causal identification, but at the SFT stage with precise dosage control; like Han et al., we employ IRT-based modeling, but with ground-truth contamination labels enabling dose-response characterization. Han et al.\ apply observational DIF to naturally contaminated models; we use AUGMENT-mode SFT injection with explicit dosage control, enabling causal dose-response profiling.
5	
6	\paragraph{IRT for LLM evaluation.}
7	Item Response Theory \citep{lord_1980_irt,hambleton_1991_irt} has gained traction for LLM evaluation \citep{liang_2023_helm}: \citet{rodriguez2021evaluation}, TinyBenchmarks \citep{polo_2024_tinybenchmarks}, Growing Pains \citep{habba_2025_growing_pains}, HiBayES \citep{luettgau_2025_hibayes}, PSN-IRT \citep{zhou_2025_psnirt}; see \citet{lalor_2024_irt_nlp} for a tutorial and \citet{gu2024olmes} for evaluation standardization. Most directly related, \citet{han2026quantifying} apply group-based DIF \citep{holland_1993_dif} to quantify item-level contamination effects. ContamCal differs by using continuous exposure covariates (explanatory DIF; \citealp{deboeck_2004_explanatory_irt}), providing calibrated ability with credible intervals, and domain-level diagnosis ($\gamma_d$); the approaches are complementary (item-level DIF for benchmark curation, model-level calibration for score interpretation). Our $\gamma$ parameter is formally an instance of explanatory DIF \citep{deboeck_2004_explanatory_irt,eckerly_2017_item_compromise}: the contamination covariate differentially affects response probability, analogous to item compromise models in educational measurement \citep{sinharay_2017_preknowledge,holland_1993_dif,camilli_1994_dif,swaminathan_1990_dif}. We use ``calibration'' in the psychometric sense of adjusting scores to approximate uncontaminated performance, distinct from probability calibration \citep{guo_2017_calibration}.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2263223f-01d5-4b92-aa81-4601c50933a4",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "81b13d7a-2b7e-4cc4-ba93-345930e5d81d",
  "sourceToolAssistantUUID": "2263223f-01d5-4b92-aa81-4601c50933a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-24T05:01:21.312Z_

<details open><summary>🔧 Tool call — Read · `toolu_013N9jZuAuhXQKyf59ta1D7H`</summary>

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
  "parentUuid": "81b13d7a-2b7e-4cc4-ba93-345930e5d81d",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohj1PWzLAqEUuK2T8L",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3b2d5884-9e37-43a0-a395-a650f50859aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E4kTfXJHmQeoWVY7A8bZ2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2436,
      "cache_read_input_tokens": 59997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2436,
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

_source line 37 · 2026-05-24T05:01:21.318Z_

<details><summary>↩ Tool result · `toolu_013N9jZuAuhXQKyf59ta1D7H`</summary>

```text
1	Benchmark contamination is widely assumed to inflate language model scores, yet its actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into six models (7B--14.7B) from five open-source families and discover a spectrum of dose-response patterns, not uniform inflation. Two patterns replicate across independent families: Immune (Phi-4, LLaMA-3.1) and Benefit (statistically significant for Gemma-2, BCa 95\% CI [$+$1.49, $+$3.14]\,pp; borderline for OLMo-2 and Falcon3). Collapse and V-recovery are each observed in one family (Qwen2.5) across three seeds but remain preliminary pending independent replication. Effects are benchmark-conditional: MMLU-targeted contamination improves GSM8K in five of six families, even those harmed on MMLU. Difference-in-differences analysis detects no item-specific memorization; a volume-matched control attributes 45\% of Benefit to data quantity. ContamCal, our diagnostic framework combining multi-signal exposure mapping with contamination-augmented IRT, enables domain-level contamination diagnosis with credible intervals---revealing that Social Sciences contamination effects are negative while STEM effects are positive, a pattern invisible to aggregate scoring. Out-of-sample validation on LLaMA-3.1-8B confirms that model family characteristics beyond baseline ability modulate vulnerability. Model-specific dose-response profiling is necessary for reliable benchmark interpretation.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b2d5884-9e37-43a0-a395-a650f50859aa",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "d6ba41fc-272f-473d-92cf-2aa5b5a96924",
  "sourceToolAssistantUUID": "3b2d5884-9e37-43a0-a395-a650f50859aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-24T05:01:22.655Z_

Now let me check the appendix.tex file to see all defined labels:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6ba41fc-272f-473d-92cf-2aa5b5a96924",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohxNZRzzbbY7FqRNFF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6ca4d281-a2d2-4503-964a-e9dd047ec9ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TE6n8D1GRAXdBkua4LpBiD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 62433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1776,
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

_source line 39 · 2026-05-24T05:01:23.539Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WNAtKMz7d3jvhQ3g84Znzu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ca4d281-a2d2-4503-964a-e9dd047ec9ee",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLohxNZRzzbbY7FqRNFF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "00ea7a13-2118-4978-b4c2-448aca71e970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TE6n8D1GRAXdBkua4LpBiD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 62433,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 126,
          "cache_read_input_tokens": 62433,
          "cache_creation_input_tokens": 1776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1776,
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

_source line 40 · 2026-05-24T05:01:23.803Z_

<details><summary>↩ Tool result · `toolu_01WNAtKMz7d3jvhQ3g84Znzu`</summary>

```text
1	\appendix
2	\renewcommand{\thesection}{\AlphAlph{\value{section}}}
3	
4	\section{Cross-Benchmark Transfer Details}
5	\label{sec:cross_benchmark_details}
6	
7	\begin{table}[h]
8	\centering
9	\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
10	\label{tab:gsm8k_transfer}
11	\footnotesize
12	\resizebox{\columnwidth}{!}{%
13	\begin{tabular}{lcccl}
14	\toprule
15	Model & MMLU $\Delta$ & GSM8K $\Delta$ & Range & Transfer \\
16	\midrule
17	Phi-4 14.7B & $\pm$0.5pp & $-$0.5pp$^{\diamond}$ & --- & Null \\
18	OLMo-2 7B & $+$3.2pp & $+$2.1pp$^{\S}$ & --- & Consistent \\
19	Falcon3 7B & $+$4.2pp & $+$1.3pp & --- & Consistent \\
20	Qwen-7B & $-$1.8pp & $+$10.1pp & $\pm$0.9 & Reversal \\
21	Qwen-14B & $-$9.4pp & $+$13.1pp & $\pm$7.4 & Reversal$^{\dagger}$ \\
22	LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\ddagger}$ & --- & Asymmetric \\
23	\bottomrule
24	\multicolumn{5}{l}{\scriptsize $^{\dagger}$d000 baseline seed-sensitive (s42$=$60.8\% vs.\ s123$=$76.7\%); d100 stable ($82\pm0.5$\%).} \\
25	\multicolumn{5}{l}{\scriptsize $^{\S}$Mean of s42 and s123: $+$2.1pp (s42: $+$1.7pp, s123: $+$2.4pp); s0 excluded ($+$9.2pp outlier).} \\
26	\multicolumn{5}{l}{\scriptsize $^{\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.} \\
27	\multicolumn{5}{l}{\scriptsize $^{\diamond}$Seed s123; Table~\ref{tab:gsm8k_dose} reports s0 ($+$1.14pp).}
28	\end{tabular}}
29	\end{table}
30	
31	\section{ARC-Challenge Cross-Benchmark Analysis}
32	\label{sec:arc_cross_benchmark}
33	
34	ARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for five of six models: OLMo-2 benefits ($+$3.9pp), Falcon3 benefits ($+$4.0pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 achieves $n\!=\!3$ on ARC: s42 exhibits a 16pp oscillation artifact (endpoint $-$1.20pp), s0 shows harm ($-$1.97pp), and s123 shows benefit ($+$2.73pp). The $n\!=\!3$ ARC mean is $-$0.15pp (SD$=$2.41pp; BCa 95\% CI [$-$1.97, $+$1.42]), with cross-seed direction inconsistent ($-$/$-$/$+$). This contrasts with MMLU, where all three seeds show benefit (mean $+$2.38pp, CI [$+$1.49, $+$3.14] excludes zero), making Gemma-2 the clearest example of benchmark-conditional contamination effects. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042).
35	
36	\paragraph{Cross-seed ARC consistency.}
37	Phi-4 is the strongest anchor with $n\!=\!3$ on both benchmarks: ARC mean $\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\% CI [$+$0.51, $+$0.77]), MMLU mean $\Delta = +0.73$pp---cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B achieves $n\!=\!3$ on ARC: mean $\Delta = -2.42$pp (SD$=$0.51pp; s0 $-$1.88, s42 $-$2.90, s123 $-$2.47; BCa 95\% CI [$-$2.90, $-$2.08]), confirming persistent harm. The d005 V-dip severity is seed-dependent ($-$1.8pp vs.\ $-$4.7pp). Qwen-14B achieves $n\!=\!3$ on both benchmarks: MMLU mean $\Delta = -15.7$pp (BCa CI [$-$24.99, $-$10.49]; s0 most extreme at $-$25.0pp due to position bias amplification); ARC mean $\Delta = -5.03$pp (BCa CI [$-$9.38, $-$2.76]). Both CIs exclude zero, confirming Collapse. OLMo-2 achieves $n\!=\!3$ on ARC: mean $\Delta = +3.44$pp (SD$=$0.52pp; s0 $+$3.50, s42 $+$3.92, s123 $+$2.90). Despite being the most seed-sensitive family on MMLU (SD$=$1.9pp), OLMo-2 is remarkably stable on ARC (SD$=$0.52pp)---seed sensitivity is itself benchmark-dependent, likely modulated by item count and difficulty distribution. Using multi-seed MMLU means ($+$1.4pp), direction is consistently positive on both benchmarks, illustrating why cross-benchmark comparisons require multi-seed aggregation (\S\ref{sec:cross_seed}). ARC dose-response trajectories (s123): Qwen-14B 90.4$\to$91.5$\to$89.8$\to$88.7$\to$87.3 (d005 transient spike then monotonic decline, consistent with MMLU s123 shape); Qwen-7B 87.1$\to$82.4$\to$85.2$\to$85.1$\to$84.7 (d005 sharp drop then partial recovery); OLMo-2 76.9$\to$77.2$\to$76.6$\to$79.2$\to$79.8 (monotonic rise).
38	
39	Cross-seed direction on ARC is consistent for 4/5 families: Phi-4 and OLMo-2 positive across three seeds each, Qwen-7B and Qwen-14B negative across three seeds each. Gemma-2 is the exception ($-$/$-$/$+$ across seeds; mean $-$0.15pp). This contrasts with MMLU, where only 2/5 families achieve strict sign consistency (\S\ref{sec:cross_seed}). ARC yields tighter confidence intervals and higher cross-seed consistency than MMLU, likely because its smaller item pool (1{,}172 vs.\ 14{,}042) amplifies the contamination signal---suggesting that benchmark size modulates not only effect magnitude but also statistical detectability.
40	
41	Cross-benchmark direction (MMLU vs.\ ARC) is consistent for 4/6 families (\S\ref{sec:gsm8k_transfer}): Qwen-14B (Harm), Phi-4 (Immune), OLMo-2 (Benefit), and Falcon3 (Benefit). Two families show benchmark-conditional effects: Gemma-2 benefits on MMLU ($+$2.38pp, CI excludes zero) but shows no significant ARC effect ($-$0.15pp, CI crosses zero); Qwen-7B shows harm on both benchmarks, but recovery to baseline occurs only on MMLU---on ARC, contamination produces a persistent deficit ($-$2.4pp mean across three seeds). Effect magnitudes remain benchmark-specific: Qwen-14B suffers $-$5.0pp on ARC compared to $-$15.7pp on MMLU (3.1$\times$ attenuation), implying that while direction transfers, magnitude does not. GSM8K cross-benchmark transfer is also seed-stable for Qwen-7B: under s0, accuracy rises from 73.3\% to 81.2\% ($+$7.9pp, monotonic), consistent with the directional reversal (mean $+$10.1pp across seeds; Table~\ref{tab:gsm8k_transfer}).
42	
43	\begin{figure}[h]
44	\centering
45	\includegraphics[width=\columnwidth]{figures/fig_arc_dose_response.pdf}
46	\caption{ARC-Challenge accuracy vs.\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\ref{fig:dose_response}) for 4/5 models.}
47	\label{fig:dose_response_arc}
48	\end{figure}
49	
50	\section{GSM8K Dose-Response Transfer}
51	\label{sec:gsm8k_dose_response}
52	
53	Table~\ref{tab:gsm8k_dose} reports GSM8K accuracy across contamination dosages for all six families (single seed, s0). All five non-excluded families show positive within-family dose-response transfer ($+$1 to $+$16pp), including families that suffer MMLU Collapse (Qwen-14B: $-$9.4pp MMLU, $+$7.4pp GSM8K) or are MMLU-Immune (LLaMA-3.1: $-$0.7pp MMLU, $+$16.4pp GSM8K---the strongest transfer effect). This directional reversal---MMLU-targeted contamination improving an unrelated open-ended math benchmark---strengthens the global capability modulation interpretation. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
54	
55	\begin{table}[h]
56	\centering
57	\caption{GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%).}
58	\label{tab:gsm8k_dose}
59	\footnotesize
60	\resizebox{\columnwidth}{!}{%
61	\begin{tabular}{lcccccc}
62	\toprule
63	Family & d000 & d005 & d025 & d050 & d100 & $\Delta$ \\
64	\midrule
65	Phi-4 14.7B & 84.46 & --- & --- & --- & 85.60 & $+$1.14 \\
66	Qwen2.5-14B & 74.98 & 71.19 & 79.30 & 81.05 & 82.41 & $+$7.43 \\
67	Qwen2.5-7B & 73.31 & 78.32 & 78.24 & 79.38 & 81.20 & $+$7.89 \\
68	OLMo-2 7B & 60.58 & --- & --- & --- & 69.75 & $+$9.17$^{\ddagger}$ \\
69	LLaMA-3.1 8B & 38.74 & --- & 52.16 & --- & 55.12 & $+$16.38 \\
70	Gemma-2 9B & 17.82$^{\dagger}$ & --- & --- & --- & --- & --- \\
71	\bottomrule
72	\multicolumn{7}{l}{\scriptsize $^{\dagger}$CoT collapse under MC-format SFT; excluded from analysis.} \\
73	\multicolumn{7}{l}{\scriptsize $^{\ddagger}$Seed-sensitive: s0 $+$9.17pp vs.\ s42 $+$2.1pp (Table~\ref{tab:gsm8k_transfer}).}
74	\end{tabular}}
75	\end{table}
76	
77	GSM8K evaluations use \texttt{max\_new\_tokens=256}, which may truncate chain-of-thought reasoning for some models. Absolute accuracy is therefore a lower bound; cross-family comparisons of absolute values should be interpreted with caution. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
78	
79	\section{Signal Reliability Across Scales}
80	\label{sec:signal_reliability_appendix}
81	
82	\begin{figure}[h]
83	\centering
84	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap.pdf}
85	\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\%++) reverses at 0.5B; S4 is near-random below 1.5B.}
86	\label{fig:signal_heatmap}
87	\end{figure}
88	
89	\section{RRF Signal Ablation}
90	\label{sec:rrf_ablation}
91	
92	\paragraph{Signal orthogonality.}
93	Table~\ref{tab:signal_correlation} reports pairwise Spearman rank correlations between detection signals at the item level, averaged across 31 models. All pairwise $|\rho| < 0.06$, confirming that S1, S2, and S4 capture orthogonal aspects of contamination exposure.
94	
95	\begin{table}[h]
96	\centering
97	\caption{Pairwise Spearman $\rho$ between detection signals (item-level, averaged across 31 models). All $|\rho| < 0.06$.}
98	\label{tab:signal_correlation}
99	\footnotesize
100	\begin{tabular}{lccc}
101	\toprule
102	Signal Pair & MMLU & ARC & GSM8K \\
103	\midrule
104	S1--S2 & $-$0.044 & $-$0.019 & $-$0.022 \\
105	S1--S4 & $+$0.038 & $+$0.009 & $+$0.053 \\
106	S2--S4 & $-$0.001 & $+$0.012 & $+$0.007 \\
107	\bottomrule
108	\end{tabular}
109	\end{table}
110	
111	\paragraph{Leave-one-out ablation.}
112	Table~\ref{tab:rrf_ablation} reports the effect of removing each signal from the RRF ensemble. $\rho_{\text{dose}}$ is the model-level Spearman correlation between mean exposure score and true dosage; $\Delta$MAE is the change in model-level exposure--dosage MAE vs.\ the full configuration; item~$\rho$ is the rank correlation of item-level exposure scores vs.\ the full configuration.
113	
114	\begin{table}[h]
115	\centering
116	\caption{Leave-one-signal-out RRF ablation (31 models, $\kappa\!=\!60$).}
117	\label{tab:rrf_ablation}
118	\footnotesize
119	\begin{tabular}{lccc}
120	\toprule
121	Configuration & $\rho_{\text{dose}}$ & $\Delta$MAE & Item $\rho$ \\
122	\midrule
123	\multicolumn{4}{l}{\textit{MMLU}} \\
124	Full (S1+S2+S4) & 0.049 & --- & --- \\
125	Drop S1 & 0.045 & $+$0.066 & 0.782 \\
126	Drop S2 & \textbf{0.471} & $+$0.045 & 0.773 \\
127	Drop S4 & 0.084 & $+$0.079 & 0.786 \\
128	\midrule
129	\multicolumn{4}{l}{\textit{ARC-Challenge}} \\
130	Full (S1+S2+S4) & $-$0.003 & --- & --- \\
131	Drop S1 & $-$0.006 & $-$0.054 & 0.784 \\
132	Drop S2 & 0.029 & $-$0.079 & 0.786 \\
133	Drop S4 & 0.001 & $-$0.004 & 0.784 \\
134	\bottomrule
135	\end{tabular}
136	\end{table}
137	
138	Dropping S2 (Min-K\%++) causes $\rho_{\text{dose}}$ to jump from 0.049 to 0.471 on MMLU, revealing that S2 actively suppresses model-level dosage discrimination. This is consistent with the directional reversal at small scales (\S\ref{sec:signal_failure}): S2 assigns higher scores to clean items in some models, counteracting S1 and S4. Despite this model-level harm, S2 provides unique item-level information (item~$\rho = 0.773$, i.e., ${\sim}$23\% of item rankings change upon removal). Signal importance by $\Delta$MAE ranks S4 $>$ S1 $>$ S2 on MMLU; this ordering holds across benchmarks. The near-zero $\rho_{\text{dose}}$ (0.049 on MMLU, $-$0.003 on ARC) confirms that RRF exposure is an item-level tool: it identifies which items within a model are most likely contaminated, but cannot distinguish dosage levels across models.
139	
140	\paragraph{Signal contribution to $\gamma$ estimation.}
141	Leave-one-out ablation on $\gamma$ recovery (Qwen2.5, $J=16$) confirms S4 (self-critique) as the dominant contributor: removing S4 incurs $4.9\times$ the $\gamma$ estimation loss of removing S2 (Min-K\%++). No signal is pure noise: the worst single-signal $\rho(E,\tau)$ is 0.072--0.118 (S2), still $5.5\times$ the random baseline. Marginal returns from three to two signals are negligible (dropping S2 leaves $\rho$ effectively unchanged), suggesting the current three-signal ensemble is near-optimal for the Qwen2.5 family.
142	
143	\paragraph{Full pipeline S2-removal test.}
144	To directly address whether S2 (Min-K\%++) harms downstream calibration, we refit the full IRT pipeline excluding S2 from the RRF fusion. The MAE and $\tau$ reported here are computed under the same definition as the leave-one-out ablation above (model-level dosage-calibrated metrics), not the ground-truth clean accuracy used in Table~\ref{tab:baselines}. Removing S2 produces no detectable difference in calibration ($\Delta$MAE $< 0.001$) or model fit ($\Delta$PPP $= 0.01$) on this test population. However, the Qwen2.5 1.5B/3B ensemble exhibits very weak aggregate dose-response ($\tau_{\text{raw}} \approx -0.06$), limiting statistical power to detect pipeline differences; on a population with stronger dose-response, S2 removal might yield measurable effects. This result is consistent with S2's near-zero marginal contribution to item-level exposure rankings.
145	
146	\section{Single-Signal Pipeline Comparison}
147	\label{sec:s2_only_pipeline}
148	
149	To evaluate whether multi-signal fusion is necessary for downstream IRT estimation, we compare the full RRF pipeline against an end-to-end single-signal alternative using Min-K\%++ (S2-only). Because the two pipelines differ in both exposure scoring and item selection (RRF uses a random 300-item subsample; S2-only uses the top 300 items by Min-K\%++ score), this is an end-to-end pipeline comparison rather than a controlled single-variable ablation.
150	
151	\begin{table}[h]
152	\centering
153	\caption{End-to-end pipeline comparison: RRF (multi-signal, random 300 items) vs.\ S2-only (Min-K\%++, top-300). Qwen2.5, $J\!=\!16$.}
154	\label{tab:s1_pipeline}
155	\footnotesize
156	\resizebox{\columnwidth}{!}{%
157	\begin{tabular}{llccccc}
158	\toprule
159	Benchmark & Pipeline & $\gamma$ & PPP & $\tau$ & MAE & ESS \\
160	\midrule
161	\multirow{2}{*}{MMLU} & RRF & 0.698 & 0.193 & 0.73 & 0.007 & 1708 \\
162	 & S2-only & 1.754 & 0.0003 & 0.63 & 0.076 & 261 \\
163	\midrule
164	\multirow{2}{*}{ARC} & RRF & 0.727 & 0.003 & --- & --- & --- \\
165	 & S2-only & 2.572 & 0.0000 & --- & --- & --- \\
166	\midrule
167	\multirow{2}{*}{GSM8K} & RRF & 0.064 & --- & --- & --- & --- \\
168	 & S2-only & $-$0.048 & --- & --- & --- & --- \\
169	\bottomrule
170	\multicolumn{7}{l}{\scriptsize ARC S2-only: $\hat{R}=1.014$ (marginal convergence).}
171	\end{tabular}}
172	\end{table}
173	
174	The S2-only pipeline exhibits severe model misfit on MMLU (PPP$=$0.0003 vs.\ 0.193), with $\gamma$ inflated $2.5\times$ (1.754 vs.\ 0.698). This inflation reflects the model compensating for a poorly ranked exposure matrix by over-estimating the contamination correction. On ARC, the S2-only pipeline fails to converge cleanly ($\hat{R}=1.014$) and produces an even larger $\gamma$ inflation ($3.5\times$). Critically, on GSM8K---where no MMLU contamination signal is expected---both pipelines converge to near-zero $\gamma$ ($0.064$ vs.\ $-0.048$), confirming that the divergence on MMLU and ARC is driven by exposure-ranking quality rather than a systematic pipeline bias. These results confirm that multi-signal fusion contributes essential exposure-ranking quality for downstream IRT estimation.
175	
176	\paragraph{Domain-level S2-only comparison.}
177	Domain-level fits further expose the S2-only pipeline's systematic failure. Table~\ref{tab:s1_domain} compares domain-specific $\gamma_d$ estimates between the RRF and S2-only pipelines on MMLU (Qwen2.5, $J\!=\!16$). All five converged S2-only domains produce large negative $\gamma_d$ ($-$5.9 to $-$7.2) with PPP$=$1.000, indicating complete model misfit. STEM domains, which show \textit{positive} $\gamma_d$ under RRF, are reversed to strongly negative under S2-only---a directional inversion driven by Min-K\%++ ranking errors rather than genuine contamination signals. Social Sciences, the only domain with negative RRF $\gamma_d$ ($-$0.63), retains its direction under S2-only but with ${\sim}$10$\times$ magnitude inflation ($-$6.30). Humanities failed to converge ($\hat{R}=1.537$) and is excluded.
178	
179	\begin{table}[h]
180	\centering
181	\caption{Domain-level $\gamma_d$: RRF vs.\ S2-only pipeline (MMLU, Qwen2.5, $J\!=\!16$). S2-only produces uniformly negative, inflated estimates with PPP$=$1.000 across all domains.}
182	\label{tab:s1_domain}
183	\footnotesize
184	\begin{tabular}{lcclc}
185	\toprule
186	Domain & RRF $\gamma_d$ & S2-only $\gamma_d$ & PPP & Direction \\
187	\midrule
188	STEM (Math) & $>$0 & $-$6.32 & 1.000 & Reversed \\
189	STEM (Science) & $>$0 & $-$7.17 & 1.000 & Reversed \\
190	STEM (CS/Eng) & $>$0 & $-$5.92 & 1.000 & Reversed \\
191	Medical & $>$0 & $-$7.06 & 1.000 & Reversed \\
192	Social Sciences & $-$0.63 & $-$6.30 & 1.000 & Same (10$\times$) \\
193	\bottomrule
194	\multicolumn{5}{l}{\scriptsize Humanities excluded ($\hat{R}=1.537$, non-convergence).}
195	\end{tabular}
196	\end{table}
197	
198	\section{Identifiability Simulation}
199	\label{sec:identifiability_appendix}
200	
201	\begin{figure}[h]
202	\centering
203	\includegraphics[width=\columnwidth]{figures/fig_identifiability_heatmap.pdf}
204	\caption{$\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\% CI coverage $\geq90\%$ require $J\geq50$ at AUC$=$0.55, but only $J\geq16$ at AUC$\geq$0.90.}
205	\label{fig:identifiability_heatmap}
206	\end{figure}
207	
208	Fisher information $\mathcal{I}(\gamma) \propto \text{Var}(e_{\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\% CI coverage $\geq 90\%$ require $J \geq 50$; at AUC$\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).
209	
210	\section{DIF Parameterization Comparison}
211	\label{sec:dif_comparison}
212	
213	We compare our primary non-uniform parameterization ($\gamma$ outside the discrimination bracket, Eq.~\ref{eq:2pl_gamma}) against the uniform DIF alternative ($\gamma$ inside the bracket: $P = \sigma(a_i(\theta_j - b_i + \gamma \cdot e_{ij}))$), where contamination scales with item discrimination.
214	
215	\begin{table}[h]
216	\centering
217	\caption{DIF parameterization comparison (MMLU, $J\!=\!16$, 300 items).}
218	\label{tab:dif_comparison}
219	\footnotesize
220	\resizebox{\columnwidth}{!}{%
221	\begin{tabular}{lcccc}
222	\toprule
223	 & $\gamma$ (mean $\pm$ SD) & PPP & LOO ELPD & ESS \\
224	\midrule
225	Non-uniform (current) & $0.245 \pm 0.197$ & 0.763 & $-$2124.3 & 1468 \\
226	Uniform (inside $a_i$) & $-0.458 \pm 0.453$ & 0.743 & $-$2123.4 & 981 \\
227	\bottomrule
228	\end{tabular}}
229	\end{table}
230	
231	This comparison uses a stratified subsample for computational efficiency; absolute $\gamma$ values differ from the main analysis (which uses a random subsample) but the relative comparison between parameterizations remains valid. Both parameterizations yield comparable model fit ($\Delta$ELPD$=$0.9, $d_{\text{SE}}=1.4$; difference $<$ 1 standard error). We adopt the non-uniform form for its tighter posterior estimates (SD 0.197 vs.\ 0.453), higher effective sample size (1468 vs.\ 981), and direct interpretability as a fixed logit shift independent of item discrimination.
232	
233	\section{4PL Extension}
234	\label{sec:4pl_details}
235	
236	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
237	\begin{equation}
238	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
239	\end{equation}
240	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
241	
242	\section{S4 Self-Critique Signal Details}
243	\label{sec:s4_details}
244	
245	S4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\text{YES})$, then score each item as the negative entropy of this distribution: $\text{S4}_i = -[-p\log p - (1-p)\log(1-p)]$ where $p = P(\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.
246	
247	\section{Training Convergence}
248	\label{sec:training_convergence}
249	
250	All SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.
251	
252	\section{Model Exclusion Details}
253	\label{sec:exclusion_details}
254	
255	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
256	
257	\paragraph{Model sets across analyses.}
258	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
259	
260	\begin{table}[h]
261	\centering
262	\caption{Model set composition across analyses.}
263	\label{tab:model_sets}
264	\footnotesize
265	\resizebox{\columnwidth}{!}{%
266	\begin{tabular}{lcll}
267	\toprule
268	Analysis & $J$ & Model Set & Section \\
269	\midrule
270	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
271	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
272	Cross-family & 16--28 & varies by benchmark & \S\ref{sec:taxonomy} \\
273	Oracle ablation & 13 & domain whitelist & \S\ref{sec:calibration_results} \\
274	\bottomrule
275	\end{tabular}}
276	\end{table}
277	
278	\section{Prior Sensitivity Analysis}
279	\label{sec:prior_sensitivity}
280	
281	To assess the influence of the $\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 randomly subsampled items) under three specifications: $\gamma \sim \mathcal{N}(0, 0.5)$, $\mathcal{N}(0, 1)$ (default), and $\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\% CI includes zero in all cases (lower bound stable at $\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\hat{R} < 1.01$, ESS $> 3800$, PPP $\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\gamma$-based conclusions at current ensemble sizes.
282	
283	For the Social Sciences domain (corrected $J=16$ pool, 2000 items), the directional signal is robust to prior choice:
284	
285	\begin{table}[h]
286	\centering
287	\caption{Social Sciences $\gamma$ prior sensitivity (corrected $J$=16 pool).}
288	\label{tab:socsci_prior}
289	\footnotesize
290	\begin{tabular}{lcc}
291	\toprule
292	Prior & $\hat{\gamma}$ & $P(\gamma\!<\!0)$ \\
293	\midrule
294	$\mathcal{N}(0, 0.5)$ & $-$0.541 & 99.35\% \\
295	$\mathcal{N}(0, 1)$ & $-$0.627 & 99.7\% \\
296	$\mathcal{N}(0, 2)$ & $-$0.654 & 99.85\% \\
297	\bottomrule
298	\multicolumn{3}{l}{\scriptsize Social Sciences row updated with corrected $J\!=\!16$ model pool;} \\
299	\multicolumn{3}{l}{\scriptsize other domains retain the original prior sensitivity pool.}
300	\end{tabular}
301	\end{table}
302	
303	In contrast to the pooled analysis where $\hat{\gamma}$ shifts 2.6$\times$ across priors, Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.54 to $-$0.65), with $P(\gamma<0) \geq 99.35\%$ in all cases. The directional signal is robust to prior choice, though the tight prior falls marginally below the Bonferroni threshold (99.375\% for eight domains).
304	
305	\section{IRT Ability Separation by Scale}
306	\label{sec:theta_separation}
307	
308	Table~\ref{tab:theta_separation} reports the mean posterior $\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\Delta\theta = \bar{\theta}_{3\text{B}} - \bar{\theta}_{1.5\text{B}}$ is positive and significant (95\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.
309	
310	\begin{table}[h]
311	\centering
312	\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\Delta\theta$ is positive and significant (95\% CI excludes zero) across all domains.}
313	\label{tab:theta_separation}
314	\footnotesize
315	\begin{tabular}{lccc}
316	\toprule
317	Domain & $\bar{\theta}_{1.5\text{B}}$ & $\bar{\theta}_{3\text{B}}$ & $\Delta\theta$ [95\% CI] \\
318	\midrule
319	Math & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\
320	Science & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\
321	CS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\
322	Medical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\
323	Humanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\
324	Social Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\
325	Business/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\
326	Other & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\
327	\midrule
328	Pooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\
329	\bottomrule
330	\end{tabular}
331	\end{table}
332	
333	\section{Cross-Seed Stability Details}
334	\label{sec:cross_seed_details}
335	
336	\begin{table}[h]
337	\centering
338	\caption{Cross-seed $\Delta$acc (d000$\to$d100). Strict sign consistency (Cons.) is 3/6; classification-level direction agreement is 5/6 (see text). Per-seed shape classification\textsuperscript{$\ddagger$} agrees for only 3/6.}
339	\label{tab:cross_seed}
340	\footnotesize
341	\resizebox{\columnwidth}{!}{%
342	\begin{tabular}{lcccccccl}
343	\toprule
344	Model & $n$ & s42 & s123 & s0 & 95\% CI & Dir. & Cons.\ & Pattern\textsuperscript{$\ddagger$} \\
345	\midrule
346	Phi-4 & 3 & 0 & $+$ & 0 & [$-$0.17, $+$1.39]\textsuperscript{B} & Immune & $\times$ & --- \\
347	Qwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\textsuperscript{B} & Harm & \checkmark & Collapse \\
348	Qwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\textsuperscript{B} & Harm & $\times$ & V-recovery \\
349	Gemma-2 & 3 & $+$ & $+$ & $+$ & [$+$1.49, $+$3.14]\textsuperscript{B} & Benefit & \checkmark & Benefit \\
350	OLMo-2 & 3 & $+$ & 0 & $+$ & [$-$0.55, $+$2.60]\textsuperscript{B} & Borderl.\ & $\times$ & ---\textsuperscript{b} \\
351	Falcon3-7B & 2 & $+$ & $+$ & --- & [$+$3.91, $+$4.19]\textsuperscript{c} & Benefit & \checkmark & Benefit \\
352	\bottomrule
353	\multicolumn{9}{l}{\scriptsize \textsuperscript{B}BCa bootstrap ($B\!=\!10{,}000$); original five families at $n\!=\!3$.} \\
354	\multicolumn{9}{l}{\scriptsize \textsuperscript{$\ddagger$}Per-seed shape may differ from family-level direction-based classification (\S\ref{sec:classification}).} \\
355	\multicolumn{9}{l}{\scriptsize \textsuperscript{b}$+$/0/$+$ across seeds. Signs: $+$/$-$ = $|\Delta|{\ge}1$pp; $0$ = $|\Delta|{<}1$pp.} \\
356	\multicolumn{9}{l}{\scriptsize \textsuperscript{c}$n\!=\!2$ seeds only; range shown instead of BCa CI.}
357	\end{tabular}}
358	\end{table}
359	
360	OLMo-2 s42 rerun (d025/d100) exhibits $\pm$1.6\,pp point-estimate variability attributable to non-deterministic CUDA operations; this falls within the cross-seed range (3.76\,pp) and does not affect pattern classification.
361	
362	\section{DiD Visualization}
363	\label{sec:did_visualization}
364	
365	\begin{figure}[h]
366	\centering
367	\includegraphics[width=\columnwidth]{figures/fig_treated_untreated.pdf}
368	\caption{DiD for treated vs.\ untreated items across all families at d025 MMLU. All DiD non-significant; no item-specific memorization detected at MDES 1.25--2.05pp.}
369	\label{fig:treated_untreated}
370	\end{figure}
371	
372	\section{DiD Across Dosage Levels}
373	\label{sec:did_dosage}
374	
375	\begin{figure}[h]
376	\centering
377	\includegraphics[width=\columnwidth]{figures/fig_did_dose_response.pdf}
378	\caption{Difference-in-differences (treated vs.\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all model families, confirming that the global capability modulation mechanism (\S\ref{sec:memorization_test}) is consistent across the full dosage range.}
379	\label{fig:did_dose_response}
380	\end{figure}
381	
382	\section{Post-hoc Power Analysis (MDES)}
383	\label{sec:mdes}
384	
385	Table~\ref{tab:mdes_mmlu} and Table~\ref{tab:mdes_arc} report the minimum detectable effect size (MDES) for the treated vs.\ untreated DiD comparison at d025 (80\% power, $\alpha=0.05$, two-sided). MDES is computed as the effect size detectable given each model's observed variance, the treated/untreated split sizes, and a two-sample $t$-test power calculation. At d100, all benchmark items are treated ($n_{\text{untreated}}=0$), precluding DiD analysis; d025 is reported as the primary dosage level.
386	
387	\begin{table}[h]
388	\centering
389	\caption{Post-hoc MDES for MMLU DiD ($n_{\text{treated}}=3{,}540$, $n_{\text{untreated}}=10{,}502$).}
390	\label{tab:mdes_mmlu}
391	\footnotesize
392	\begin{tabular}{lcc}
393	\toprule
394	Model & DiD (pp) & MDES (pp) \\
395	\midrule
396	Phi-4 14.7B & $-$0.27 & 1.25 \\
397	OLMo-2 7B & $-$1.07 & 1.59 \\
398	Gemma-2 9B & $+$0.55 & 1.74 \\
399	Qwen2.5-7B & $-$0.84 & 2.02 \\
400	Qwen2.5-14B & $+$0.69 & 2.05 \\
401	\bottomrule
402	\end{tabular}
403	\end{table}
404	
405	\begin{table}[h]
406	\centering
407	\caption{Post-hoc MDES for ARC-Challenge DiD ($n_{\text{treated}}=257$, $n_{\text{untreated}}=915$).}
408	\label{tab:mdes_arc}
409	\footnotesize
410	\begin{tabular}{lcc}
411	\toprule
412	Model & DiD (pp) & MDES (pp) \\
413	\midrule
414	Phi-4 14.7B & $-$0.83 & 2.28 \\
415	Qwen2.5-14B & $-$0.26 & 3.47 \\
416	OLMo-2 7B & $-$1.13 & 4.19 \\
417	Gemma-2 9B & $-$0.25 & 4.66 \\
418	Qwen2.5-7B & $+$2.43 & 5.57 \\
419	\bottomrule
420	\end{tabular}
421	\end{table}
422	
423	On MMLU, all observed DiD values are well below their respective MDES, confirming that the null results are consistent with absence of item-specific effects $>$2pp. On ARC, the smaller treated sample ($n=257$) yields substantially higher MDES; in particular, Qwen-7B's MDES of 5.57pp means that even moderate item-specific effects cannot be excluded for this model on ARC. ARC DiD results should therefore be interpreted as inconclusive rather than as evidence against memorization.
424	
425	\section{Volume Control Analysis}
426	\label{sec:volume_control}
427	
428	To disentangle data quantity from contamination content, we train Falcon3-7B on 66{,}533 non-benchmark MCQ items drawn from MMLU auxiliary training subjects, filtered to exclude test-set overlap (MD5 deduplication). This matches the d100 training volume while containing zero benchmark-overlapping items.
429	
430	\begin{table}[h]
431	\centering
432	\caption{Volume control decomposition (Falcon3-7B, seed$=$42). Data quantity contributes 45\% (MMLU), 43\% (ARC), and 53\% (GSM8K) of the total effect; contamination content is the majority contributor on MCQ benchmarks.$^{\dagger}$}
433	\label{tab:volume_control}
434	\footnotesize
435	\resizebox{\columnwidth}{!}{%
436	\begin{tabular}{lcccc}
437	\toprule
438	Condition & MMLU & ARC & GSM8K & vs.\ d000 \\
439	\midrule
440	d000 (clean baseline) & 58.77\% & 81.57\% & 74.53\% & --- \\
441	Volume control & 60.67\% & 83.28\% & 75.21\% & $+$1.90 / $+$1.71 / $+$0.68pp \\
442	d100 (contaminated) & 62.96\% & 85.58\% & 75.82\% & $+$4.19 / $+$4.01 / $+$1.29pp \\
443	\bottomrule
444	\multicolumn{5}{l}{\scriptsize $^{\dagger}$GSM8K total effect ($+$1.29pp) is too small for reliable quantity/content decomposition.}
445	\end{tabular}}
446	\end{table}
447	
448	The cross-benchmark consistency of the decomposition (MMLU 45\% vs.\ ARC 43\%) strengthens confidence in the estimate. Applying Falcon3's volume baseline to other patterns: Qwen-14B's Collapse ($-$9.4pp) against a $+$1.90pp volume baseline implies contamination-specific harm of approximately $-$11.3pp; Phi-4's Immune response ($<$1pp) in the presence of volume-driven gains further confirms that contamination vulnerability is family-specific rather than a generic data quantity effect.
449	
450	\section{Dose-Response Details}
451	\label{sec:dose_response_details}
452	
453	The dose-response patterns reported in \S\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \textit{decreases} with dosage (0.41 at d000 $\to$ 0.27 at d100), consistent with the position bias confound documented in \S\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\%) overwhelms any memorization benefit.
454	
455	\section{Sensitivity of Profile Classification}
456	\label{sec:classification_sensitivity}
457	
458	We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 134 $(\tau, \sigma)$ combinations. Table~\ref{tab:sensitivity} reports family-level stability across both a reasonable parameter range ($\tau \in [0.5, 2.0]$~pp $\times$ $\sigma \in [3.0, 7.0]$~pp; 30 combinations) and the full 134-combination sweep, along with the nearest parameter value at which the classification transitions.
459	
460	\begin{table}[h]
461	\centering
462	\caption{Profile classification stability across threshold parameter ranges. All families achieve 100\% stability within the reasonable range; transitions occur only at extreme parameter values ($\geq$3$\times$ default).}
463	\label{tab:sensitivity}
464	\footnotesize
465	\resizebox{\columnwidth}{!}{%
466	\begin{tabular}{lcccc}
467	\toprule
468	Family & Pattern & Reasonable & Full & Nearest transition \\
469	\midrule
470	Qwen2.5-14B & Collapse & 100\% & 100\% & $\tau = 9.4$ \\
471	Gemma-2 9B & Benefit & 100\% & 89\% & $\tau = 3.8$ \\
472	Phi-4 14.7B & Immune & 100\% & 82\% & $\tau < 0.35$ \\
473	OLMo-2 7B & Benefit & 100\% & 82\% & $\tau = 3.25$ \\
474	Qwen2.5-7B & V-recovery & 100\% & 72\% & $\tau = 3.0$ \\
475	\bottomrule
476	\end{tabular}}
477	\end{table}
478	
479	Within the reasonable parameter range, all five families achieve 100\% classification stability (150/150 family--parameter combinations). Transitions occur only at extreme $\tau$ values well beyond the default ($\tau\!=\!2$): Qwen-14B requires $\tau\!=\!9.4$ (4.7$\times$ default) to reclassify, reflecting the large separation between its $\Delta\text{acc}$ ($-$9.4pp) and any plausible noise threshold. Qwen-7B is the least robust at $\tau\!=\!3.0$ (1.5$\times$ default), but this is still above any defensible noise threshold for MMLU. The high intrinsic effect-size separation---Phi-4 fluctuates $<$0.4pp while Qwen-14B declines by 9.4pp---means that classification stability is driven by the data rather than by parameter choice. At $\tau\!=\!1$\,pp (the lower bound of the reasonable range), all five original families and the held-out LLaMA-3.1 ($|\Delta| = 0.69$\,pp) retain their classifications.
480	
481	\section{Cross-Family Domain Decomposition}
482	\label{sec:domain_decomposition}
483	
484	We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all model families at each contamination dosage.
485	
486	Two patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, Collapse (Qwen-14B) produces negative $\Delta\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\Delta\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.
487	
488	Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across all families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\times$ the STEM magnitude. The ordering is stable across patterns: in Collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
489	
490	These results reinforce the global capability modulation interpretation (\S\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.
491	
492	\section{Baseline Ability vs.\ Contamination Effect}
493	\label{sec:baseline_vs_effect}
494	
495	\begin{figure}[h]
496	\centering
497	\includegraphics[width=\columnwidth]{figures/fig_baseline_vs_effect.pdf}
498	\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}
499	\label{fig:baseline_vs_effect}
500	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00ea7a13-2118-4978-b4c2-448aca71e970",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "93eeca18-0a69-4192-8e23-67ccc09a60a2",
  "sourceToolAssistantUUID": "00ea7a13-2118-4978-b4c2-448aca71e970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-24T05:01:25.190Z_

Let me continue reading the appendix to find all section labels:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93eeca18-0a69-4192-8e23-67ccc09a60a2",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLoi8aE5DM5ep69WNTUF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0c510628-473a-41eb-92b0-552c0896cd75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MjvxG41CZ7BdcPxNB7eZUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15038,
      "cache_read_input_tokens": 64209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15038,
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

_source line 42 · 2026-05-24T05:01:26.205Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JcL1YegbYQnk71F7XuVTnB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "limit": 500,
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c510628-473a-41eb-92b0-552c0896cd75",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLoi8aE5DM5ep69WNTUF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1e317cff-de00-46b4-b587-f3c4e9791eb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MjvxG41CZ7BdcPxNB7eZUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15038,
      "cache_read_input_tokens": 64209,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15038
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 140,
          "cache_read_input_tokens": 64209,
          "cache_creation_input_tokens": 15038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15038,
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

_source line 43 · 2026-05-24T05:01:26.215Z_

<details><summary>↩ Tool result · `toolu_01JcL1YegbYQnk71F7XuVTnB`</summary>

```text
500	\end{figure}
501	
502	\section{Per-Domain $\gamma$ Estimates}
503	\label{sec:domain_gamma_table}
504	
505	\begin{table}[h]
506	\centering
507	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\hat{R} < 1.01$). Social Sciences $P(\gamma\!<\!0)$ strengthens from 99.1\% to 99.7\% at $J$=16, exceeding the Bonferroni-corrected threshold ($99.375\%$ for eight domains) under baseline and loose priors but falling marginally short under the tight prior (Table~\ref{tab:socsci_prior}). Results remain exploratory at these ensemble sizes \citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}
508	\label{tab:domain_gamma}
509	\footnotesize
510	\resizebox{\columnwidth}{!}{%
511	\begin{tabular}{lcccccc}
512	\toprule
513	 & \multicolumn{2}{c}{$J$=13} & \multicolumn{4}{c}{$J$=16} \\
514	\cmidrule(lr){2-3} \cmidrule(lr){4-7}
515	Domain & $\gamma$ & $P(\gamma\!<\!0)$ & $\gamma$ & $P(\gamma\!<\!0)$ & PPP & $\hat{R}$ \\
516	\midrule
517	MMLU: Math & +0.50 & 8.1\% & +0.60 & 3.8\% & 0.305 & 1.007 \\
518	MMLU: Science & +0.50 & 7.8\% & +0.57 & 4.3\% & 0.197 & 1.007 \\
519	MMLU: CS/Eng & +0.50 & 14.8\% & +0.32 & 24.0\% & 0.503 & 1.006 \\
520	MMLU: Medical & +0.24 & 24.0\% & +0.05 & 43.6\% & 0.268 & 1.008 \\
521	MMLU: Other & +0.13 & 35.7\% & +0.32 & 20.4\% & 0.072$^\dagger$ & 1.008 \\
522	MMLU: Business/Law & +0.04 & 44.1\% & +0.08 & 37.8\% & 0.395 & 1.007 \\
523	MMLU: Humanities & $-$0.31 & 85.4\% & $-$0.14 & 69.7\% & 0.416 & 1.007 \\
524	MMLU: Social Sci & $-$0.57 & \textbf{99.1\%} & $-$0.63 & \textbf{99.7\%} & 0.722 & 1.006 \\
525	\bottomrule
526	\end{tabular}}
527	
528	\vspace{2pt}
529	{\scriptsize $^\dagger$PPP below acceptable threshold (0.1); $\gamma$ estimate for this domain should be interpreted with caution.}
530	\end{table}
531	
532	\section{DGP Robustness Analysis}
533	\label{sec:threshold_dgp}
534	
535	We evaluate 2PL+$\gamma$ robustness under data-generating process (DGP) misspecification via 400 simulation runs (2 DGPs $\times$ 4 ensemble sizes $\times$ 5 true $\gamma$ values $\times$ 10 seeds).
536	
537	\paragraph{Design.} The \emph{Linear DGP} (control) generates responses from the correctly specified additive model (Eq.~\ref{eq:2pl_gamma}). The \emph{Threshold DGP} (misspecified) applies a step-function contamination effect: items with exposure above a threshold receive the full effect; items below receive zero. Ensemble sizes sweep $J \in \{16, 50, 100, 500\}$; true $\gamma \in \{0.5, 1.0, 1.5, 2.0, 3.0\}$.
538	
539	\paragraph{Point estimates.} Under the Linear DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.84$--$1.07$ across all conditions (unbiased within sampling noise). Under the Threshold DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.94$--$1.24$ (mild overestimation, not attenuation). PPP remains in the acceptable range (0.50--0.56) under both DGPs, confirming that posterior predictive checks cannot detect this form of misspecification.
540	
541	\paragraph{CI coverage.} Under the Linear DGP, 95\% CI coverage is nominal ($\geq$0.93) at all $J$. Under the Threshold DGP, coverage degrades with ensemble size (Table~\ref{tab:dgp_coverage}). The intervals become overconfident as $J$ increases because the model converges to a biased point estimate.
542	
543	\begin{table}[h]
544	\centering
545	\caption{95\% CI coverage under Threshold DGP (range across $\gamma$ values).}
546	\label{tab:dgp_coverage}
547	\footnotesize
548	\begin{tabular}{lc}
549	\toprule
550	$J$ & 95\% CI coverage \\
551	\midrule
552	50 & 1.00 \\
553	100 & 0.90--1.00 \\
554	200 & 0.80--1.00 \\
555	500 & 0.70--1.00 \\
556	\bottomrule
557	\end{tabular}
558	\end{table}
559	
560	\paragraph{Implications.} The reasoning chain is: (i)~Threshold DGP + linear model yields $\hat{\gamma}/\gamma_{\text{true}} \geq 0.94$ (overestimation, not attenuation); (ii)~therefore, if a true threshold effect exists, the linear model will not fail to detect it; (iii)~an empirical $\gamma \approx 0$ is a genuine null, not a misspecification artifact. Coverage degradation affects the \emph{precision} of effect size estimates (how narrow the CI is), not the \emph{detection} of whether an effect exists. At the ensemble sizes in our empirical analyses ($J\!=\!13$--$16$), coverage remains near-nominal even under misspecification. Real RRF exposure is right-skewed (mean$=$0.041); the simulation uses uniform exposure, so quantitative magnitudes may differ, but the qualitative pattern (overestimation direction, coverage degradation at large $J$) is robust.
561	
562	\section{ARC IRT Results}
563	\label{sec:arc_irt}
564	
565	ARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 randomly subsampled items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\sim}$0.7pp) is smaller than correction noise. Domain-level $\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).
566	
567	\section{Full Baseline Comparison}
568	\label{sec:full_baselines}
569	
570	Table~\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S2-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.
571	
572	B6-DCR \citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.
573	
574	\begin{table}[h]
575	\centering
576	\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S2-only exposure). MAE$\downarrow$.}
577	\label{tab:full_baselines_arc}
578	\footnotesize
579	\begin{tabular}{lc}
580	\toprule
581	Method & ARC MAE \\
582	\midrule
583	B0-Raw & 0.059 \\
584	B1-Remove\&Rescore & 0.059 \\
585	B2-Single2PL+$\gamma$ & 0.064 \\
586	B3-Vanilla4PL & 0.071 \\
587	B4-LinearRegression & 0.056 \\
588	B5-Emperor & 0.059 \\
589	B6-DCR & --- \\
590	\midrule
591	ContamCal (4PL+$\gamma$) & \textbf{0.035} \\
592	\bottomrule
593	\end{tabular}
594	\end{table}
595	
596	\begin{table}[h]
597	\centering
598	\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\downarrow$.}
599	\label{tab:full_baselines_gsm8k}
600	\footnotesize
601	\begin{tabular}{lc}
602	\toprule
603	Method & GSM8K MAE \\
604	\midrule
605	B0-Raw & 0.003 \\
606	B2-Single2PL+$\gamma$ & 0.320 \\
607	B3-Vanilla4PL & 0.012 \\
608	B4-LinearRegression & \textbf{0.003} \\
609	B6-DCR & --- \\
610	\midrule
611	ContamCal (4PL+$\gamma$) & 0.020 \\
612	\bottomrule
613	\end{tabular}
614	\end{table}
615	
616	\section{Parametric Dose-Response Model Comparison}
617	\label{sec:parametric_dr}
618	
619	We fit four parametric dose-response models---Constant (intercept-only), Linear, Quadratic, and four-parameter Hill \citep{hill1910aggregation,ritz2015dose}---to pooled multi-seed MMLU accuracy trajectories for each family. Table~\ref{tab:aicc_dr} reports AICc and Akaike weights.
620	
621	\begin{table}[h]
622	\centering
623	\caption{AICc model selection for dose-response trajectories (pooled multi-seed MMLU). Bold indicates best-fitting model per family; $w$ is the Akaike weight of the best model.}
624	\label{tab:aicc_dr}
625	\footnotesize
626	\resizebox{\columnwidth}{!}{%
627	\begin{tabular}{lccccc}
628	\toprule
629	Family & Constant & Linear & Quadratic & Hill & Best ($w$) \\
630	\midrule
631	Phi-4 14.7B & $-$71.42 & $-$72.08 & $-$70.06 & $\mathbf{-73.14}$ & Hill (0.58) \\
632	Qwen2.5-14B & 49.54 & 23.40 & 21.22 & $\mathbf{18.28}$ & Hill (0.55) \\
633	Qwen2.5-7B & $-$12.38 & $-$20.53 & $-$14.52 & $\mathbf{-24.97}$ & Hill (0.77) \\
634	Gemma-2 9B & $\mathbf{17.35}$ & 18.89 & 20.01 & 18.96 & Constant (0.39) \\
635	OLMo-2 7B & $\mathbf{25.82}$ & 26.66 & 27.54 & 26.47 & Constant (0.62) \\
636	\bottomrule
637	\end{tabular}}
638	\end{table}
639	
640	Parametric model selection with pooled multi-seed data recovers only the most extreme pattern (Collapse, Qwen-14B; Hill $E_{\max} = -43$pp). Two families classified as Benefit by Algorithm~\ref{alg:profile-classification} (Gemma-2, OLMo-2) are indistinguishable from Constant under AICc---consistent with their cross-seed CIs crossing zero (Table~\ref{tab:cross_seed}). Qwen-7B's V-recovery is structurally inaccessible to monotonic Hill/sigmoid models; Quadratic captures the V-shape but is penalized by AICc ($\Delta$AICc$=$6.4). Phi-4's Immune classification is reclassified as weak Benefit (Hill $E_{\max} = +2.43$pp, CI [$-$2.01, $+$6.88] crossing zero). These discrepancies reflect insufficient statistical power at $n\!=\!3$ seeds rather than contradictions: Algorithm~\ref{alg:profile-classification} resolves per-seed patterns below the detection threshold of pooled parametric methods, motivating its use for profile construction.
641	
642	\section{Exposure Score Item-Level Classification}
643	\label{sec:sij_classification}
644	
645	Under controlled injection where ground-truth contamination labels are available, we evaluate item-level classification performance of each detection signal and the RRF fusion (\S\ref{sec:stage1}). S1 (embedding similarity) achieves near-perfect discrimination (ROC-AUC 0.93--0.99 across benchmarks and dosage levels), confirming that cosine similarity to the training corpus reliably identifies injected items. RRF fusion achieves ROC-AUC 0.73--0.93, reduced relative to S1 because S2 (Min-K\%++, AUC $\approx$ 0.48--0.50) and S4 (Self-Critique, AUC $\approx$ 0.47--0.51) contribute near-random item-level signal. However, RRF is designed for the realistic setting where ground truth is unavailable: S1 requires an explicit training corpus reference, which practitioners typically lack, while RRF's multi-signal approach provides robustness across detection scenarios where no single signal dominates (\S\ref{sec:rrf_ablation}).
646	
647	\section{Use of AI Assistants}
648	\label{app:ai-assistants}
649	
650	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
651	\begin{itemize}
652	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
653	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.
654	    \item \textbf{Literature:} summarizing related papers to inform related-work section.
655	\end{itemize}
656	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e317cff-de00-46b4-b587-f3c4e9791eb3",
  "isSidechain": true,
  "promptId": "6fe9b473-5fe6-491c-a9b6-3a1d9745fe20",
  "agentId": "aa7f2bbdc86ca52cd",
  "type": "user",
  "uuid": "e383e8c3-2b32-42a9-b652-d65dd82b7801",
  "sourceToolAssistantUUID": "1e317cff-de00-46b4-b587-f3c4e9791eb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-24T05:01:35.874Z_

Perfect! Now I have all the information I need. Let me create a comprehensive summary by checking which appendix labels were found in the main text files.

Based on my thorough search of the main text files, here are the results:

## APPENDIX SECTIONS REFERENCED FROM MAIN TEXT

The following appendix sections/tables/figures are actively referenced in the main text files:

**Section References (29):**
1. **sec:sij_classification** - method.tex (line 56)
2. **sec:dif_comparison** - method.tex (line 76)
3. **sec:4pl_details** - method.tex (line 76)
4. **sec:prior_sensitivity** - method.tex (line 79)
5. **sec:identifiability_appendix** - method.tex (line 92)
6. **sec:classification_sensitivity** - method.tex (line 97)
7. **sec:parametric_dr** - method.tex (line 133)
8. **sec:arc_cross_benchmark** - results.tex (line 42)
9. **sec:domain_decomposition** - results.tex (line 42)
10. **sec:gsm8k_dose_response** - results.tex (line 45)
11. **sec:arc_cross_benchmark** - results.tex (line 57) [repeated]
12. **sec:mdes** - results.tex (line 74)
13. **sec:volume_control** - results.tex (line 98)
14. **sec:rrf_ablation** - results.tex (line 103)
15. **sec:s2_only_pipeline** - results.tex (line 103)
16. **sec:prior_sensitivity** - results.tex (line 107)
17. **sec:arc_irt** - results.tex (line 107)
18. **sec:signal_reliability_appendix** - results.tex (line 132)
19. **sec:identifiability_appendix** - results.tex (line 132) [repeated]

**Table References (11):**
1. **tab:gsm8k_transfer** - results.tex (line 57)
2. **tab:cross_seed** - introduction.tex (line 10) and results.tex (lines 33, 69)
3. **tab:domain_gamma** - results.tex (line 140, 144)
4. **tab:socsci_prior** - results.tex (line 144)

**Figure References (3):**
1. **fig:treated_untreated** - results.tex (line 95)
2. **fig:domain_gamma** - results.tex (line 140, 144)
3. **fig:dose_response** - introduction.tex (line 5)

---

## UNREFERENCED APPENDIX SECTIONS (ORPHANED - NOT CITED IN MAIN TEXT)

The following 10 appendix labels are defined but NOT referenced from any main text file:

1. **sec:cross_benchmark_details** - Appendix Section A (Cross-Benchmark Transfer Details)
2. **sec:training_convergence** - Appendix Section H (Training Convergence)
3. **sec:exclusion_details** - Appendix Section I (Model Exclusion Details)
4. **sec:theta_separation** - Appendix Section K (IRT Ability Separation by Scale)
5. **sec:cross_seed_details** - Appendix Section L (Cross-Seed Stability Details)
6. **sec:did_visualization** - Appendix Section M (DiD Visualization)
7. **sec:did_dosage** - Appendix Section N (DiD Across Dosage Levels)
8. **sec:dose_response_details** - Appendix Section R (Dose-Response Details)
9. **sec:baseline_vs_effect** - Appendix Section S (Baseline Ability vs. Contamination Effect)
10. **sec:threshold_dgp** - Appendix Section U (DGP Robustness Analysis)
11. **app:ai-assistants** - Appendix Section W (Use of AI Assistants)

Additionally, the following table/figure labels are defined in the appendix but NOT referenced from main text:

**Unreferenced Table Labels:**
- tab:signal_correlation, tab:s1_pipeline, tab:s1_domain, tab:dif_comparison, tab:model_sets, tab:sensitivity, tab:dgp_coverage, tab:full_baselines_arc, tab:full_baselines_gsm8k, tab:aicc_dr, tab:mdes_mmlu, tab:mdes_arc

**Unreferenced Figure Labels:**
- fig:signal_heatmap, fig:identifiability_heatmap, fig:dose_response_arc, fig:did_dose_response, fig:baseline_vs_effect

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e383e8c3-2b32-42a9-b652-d65dd82b7801",
  "isSidechain": true,
  "agentId": "aa7f2bbdc86ca52cd",
  "requestId": "req_011CbLoiJs6c3TLqok9qn3Fk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3ceac998-a2aa-4075-9bb4-aa1f56d3a8c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/director_60b87b45",
  "sessionId": "8cae963d-5690-4230-b648-03d26a0c7195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-enchanting-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015AFDoP8zMLGimgXazEQ8ob",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4575,
      "cache_read_input_tokens": 79247,
      "output_tokens": 1161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4575
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1161,
          "cache_read_input_tokens": 79247,
          "cache_creation_input_tokens": 4575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4575,
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
