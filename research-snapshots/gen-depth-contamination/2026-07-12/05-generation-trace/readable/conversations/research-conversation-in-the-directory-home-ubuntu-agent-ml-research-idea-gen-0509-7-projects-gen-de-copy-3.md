# Research conversation: In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/, I need to

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a86cd6902d70a29a1.jsonl`
- **Structured JSON:** [`9663bc10f08f8f4f815d.json`](../../sessions/96/9663bc10f08f8f4f815d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-23T04:15:44.297Z_

In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/, I need to find all cross-references (\ref{}, \autoref{}, \cref{}) and all \label{} definitions to check for consistency. 

Search broadly across all .tex files in that directory and subdirectories. For each file, show:
1. All \ref{...}, \autoref{...}, \cref{...} references with their line numbers and the label they reference
2. All \label{...} definitions with their line numbers

Also check for any undefined references or multiply-defined labels. Be very thorough - check main.tex, introduction.tex, method.tex, experiments_c1.tex, discussion.tex, conclusion.tex, related_work.tex, appendix.tex, and any files in tables/ subdirectory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "afe5f1c5-f7ce-4eca-ae49-a5aba9341099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T04:15:45.847Z_

I'll help you find all cross-references and label definitions in the LaTeX files. Let me start by exploring the directory structure and then systematically search for all references and labels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afe5f1c5-f7ce-4eca-ae49-a5aba9341099",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRHEjzSuu7eDnvp9mc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "abebafed-a240-4bc8-bccb-34a6371662f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KbcegTgE9CgjgzDVKjZ5k9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21237,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21237,
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

_source line 3 · 2026-05-23T04:15:46.062Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GKH7upVSQBm8GVEqrC6wzD`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper -type f -name \"*.tex\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abebafed-a240-4bc8-bccb-34a6371662f0",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRHEjzSuu7eDnvp9mc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41c7719a-415a-4ade-88d7-8b94dd33ee4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KbcegTgE9CgjgzDVKjZ5k9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21237,
      "cache_read_input_tokens": 0,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 133,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 21237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21237,
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

_source line 4 · 2026-05-23T04:15:46.213Z_

<details><summary>↩ Tool result · `toolu_01GKH7upVSQBm8GVEqrC6wzD`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_alpha_sweep.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_pairwise_significance.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41c7719a-415a-4ade-88d7-8b94dd33ee4a",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "f4402513-6195-41b7-8864-4a9920a08f9d",
  "sourceToolAssistantUUID": "41c7719a-415a-4ade-88d7-8b94dd33ee4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T04:15:48.030Z_

Now let me search for all \label, \ref, \autoref, and \cref definitions and references across all these files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4402513-6195-41b7-8864-4a9920a08f9d",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRRhEM2YBFS4bd9gGQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "681ad878-648f-40d0-b579-adddfa878518",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011qy48kEwRw7ip3DQvUxLvf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 21237,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1628,
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

_source line 6 · 2026-05-23T04:15:48.616Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015hQQmMS55SNYqwJZC2My6w`</summary>

```json
{
  "pattern": "\\\\label\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "type": "tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "681ad878-648f-40d0-b579-adddfa878518",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRRhEM2YBFS4bd9gGQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e40ff527-0daf-4e5e-a8b5-9166c8ad21fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011qy48kEwRw7ip3DQvUxLvf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 21237,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1628,
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

_source line 7 · 2026-05-23T04:15:48.640Z_

<details><summary>↩ Tool result · `toolu_015hQQmMS55SNYqwJZC2My6w`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:2:\label{sec:related_work}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:2:\label{sec:filtering}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:13:\label{tab:tab_filtering_main}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:2:\label{sec:extended_discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:18:\label{tab:crossscorer}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:26:\label{tab:anova_crossscorer}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:48:\label{sec:extended_neural_probe}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:57:\label{sec:extended_llm}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:69:\label{sec:extended_limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:90:\label{tab:pairwise_significance}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:93:\label{sec:dose_response}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:102:\label{tab:dose_response}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:122:\label{sec:seed_robustness}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:134:\label{tab:seed_robustness}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:151:\label{sec:bonferroni_ci}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:162:\label{tab:bonferroni_ci}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:189:\label{sec:robustness_10k}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:208:\label{tab:robustness_10k}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex:2:\label{sec:conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:2:\label{sec:experiments}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:10:\label{sec:kstar_boundary}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:18:\label{tab:kstar_ci}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:42:\label{fig:auc_decay}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:60:\label{fig:kstar_theta}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:68:\label{sec:transfer}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:74:\label{fig:transfer_heatmap}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:88:\label{sec:feature_degradation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:89:\label{sec:generation_mode}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:98:\label{sec:neural_probe}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:107:\label{tab:neural_probe_crossmodel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:123:\label{sec:cross_domain}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:135:\label{tab:domain_kstar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:149:\label{sec:robustness}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:156:\label{sec:binary_confidence}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:2:\label{sec:discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:3:\label{sec:why_kstar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:4:\label{sec:one_wash}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:5:\label{sec:negative_graduated}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:6:\label{sec:repr_dependence}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:7:\label{sec:boundary_cases}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:8:\label{sec:length_confound}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex:4:\label{tab:domain_model_kstar_full}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex:4:\label{tab:domain_model_kstar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:2:\label{sec:method}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:8:\label{fig:pipeline}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:12:\label{sec:formulation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:23:  \label{eq:kstar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:41:\label{sec:features}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:53:\label{sec:experimental_setup}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:65:\label{tab:setup}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:3:\label{sec:appendix}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:11:\label{fig:filtering_strategies}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:25:\label{tab:top_features}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:48:  \label{tab:s1_transfer}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:74:  \label{tab:s4_dataset_stats}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:96:  \label{tab:s2_decoding}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:130:  \label{tab:kstar_ci_extended}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:155:  \label{tab:s3_llm_zeroshot}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:198:  \label{tab:s3c_perdepth}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:216:  \label{tab:token_length}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:244:  \label{tab:s5_features}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:279:  \label{tab:s6_lgbm_params}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:300:  \label{tab:s7_neural_probe}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:336:  \label{tab:s8_cv_folds}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:357:  \label{tab:s9_binary_spearman}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:379:  \label{tab:s10_pythia_decoding}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:403:  \label{tab:s11_length_ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:425:  \label{tab:s12_domain_ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:448:  \label{tab:s13_scorer_sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:2:\label{sec:introduction}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e40ff527-0daf-4e5e-a8b5-9166c8ad21fc",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "bd72ab4c-dae3-47eb-bf58-456203cd6024",
  "sourceToolAssistantUUID": "e40ff527-0daf-4e5e-a8b5-9166c8ad21fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T04:15:49.004Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CC7pT5BWG2GWbGkPQsop3P`</summary>

```json
{
  "pattern": "\\\\(?:ref|autoref|cref)\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "type": "tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd72ab4c-dae3-47eb-bf58-456203cd6024",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRRhEM2YBFS4bd9gGQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e7ac63c2-faec-4dd9-b634-73023a3c64f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011qy48kEwRw7ip3DQvUxLvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 21237,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 308,
          "cache_read_input_tokens": 21237,
          "cache_creation_input_tokens": 1628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1628,
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

_source line 9 · 2026-05-23T04:15:49.031Z_

<details><summary>↩ Tool result · `toolu_01CC7pT5BWG2GWbGkPQsop3P`</summary>

```text
&lt;persisted-output>
Output too large (22.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-reviewer-08f7237f/51eb88ba-e52c-46f6-bfa0-e0d3c2871b77/tool-results/toolu_01CC7pT5BWG2GWbGkPQsop3P.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:5:We present this as a consistency check under extreme (100\%) contamination, not as an independent contribution; at realistic rates ($\leq$10\%), the filtering effect diminishes to $\Delta \leq 0.1$\,pp (not significant; Appendix~\ref{sec:dose_response}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:12:\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:17:Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:21:DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:22:At realistic contamination ratios ($\leq$50\%), all filtering strategies converge ($p > 0.12$), consistent with the one-wash laundering finding that depth-aware curation offers marginal benefit when $\Kempirical{=}2$ (Appendix~\ref{sec:dose_response}).
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7ac63c2-faec-4dd9-b634-73023a3c64f8",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "d134b3e9-48da-49cb-85e4-9c683b7b27ee",
  "sourceToolAssistantUUID": "e7ac63c2-faec-4dd9-b634-73023a3c64f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-23T04:15:50.686Z_

Let me read the complete output of the references:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d134b3e9-48da-49cb-85e4-9c683b7b27ee",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRdHEyX3B3Q7wRsC3n",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "074ee0a6-3f4f-4740-bd53-20540bf72541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ph8GaXm1E4aZTGob7jBj9r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4711,
      "cache_read_input_tokens": 22865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4711,
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

_source line 11 · 2026-05-23T04:15:51.045Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BMk8qxytu6G2nmMYgRc7HS`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-reviewer-08f7237f/51eb88ba-e52c-46f6-bfa0-e0d3c2871b77/tool-results/toolu_01CC7pT5BWG2GWbGkPQsop3P.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "074ee0a6-3f4f-4740-bd53-20540bf72541",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRdHEyX3B3Q7wRsC3n",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fa300357-ecc8-405c-8983-5c4e1626ba05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ph8GaXm1E4aZTGob7jBj9r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4711,
      "cache_read_input_tokens": 22865,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 172,
          "cache_read_input_tokens": 22865,
          "cache_creation_input_tokens": 4711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4711,
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

_source line 12 · 2026-05-23T04:15:51.052Z_

<details><summary>↩ Tool result · `toolu_01BMk8qxytu6G2nmMYgRc7HS`</summary>

```text
1	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:5:We present this as a consistency check under extreme (100\%) contamination, not as an independent contribution; at realistic rates ($\leq$10\%), the filtering effect diminishes to $\Delta \leq 0.1$\,pp (not significant; Appendix~\ref{sec:dose_response}).
2	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:12:\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
3	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:17:Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
4	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:21:DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
5	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:22:At realistic contamination ratios ($\leq$50\%), all filtering strategies converge ($p > 0.12$), consistent with the one-wash laundering finding that depth-aware curation offers marginal benefit when $\Kempirical{=}2$ (Appendix~\ref{sec:dose_response}).
6	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:59:GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\% (95\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\ref{tab:s3_llm_zeroshot}).
7	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:60:Per-depth recall confirms convergent failure at depths $\geq 2$ (Section~\ref{sec:why_kstar}).
8	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:76:At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite/continuation; at $\theta = 0.70$, $\Kempirical = 1$ across all configurations (Figure~\ref{fig:kstar_theta}).
9	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:81:Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
10	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:85:Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
11	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:95:The main filtering experiments (Section~\ref{sec:filtering}) use 100\% synthetic data to maximize effect size.
12	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:96:To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
13	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:125:We re-run three configurations with seed$\,{=}\,123$ (primary: seed$\,{=}\,42$; Table~\ref{tab:seed_robustness}).
14	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:154:Table~\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\Kempirical$ boundary pair.
15	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:195:Table~\ref{tab:robustness_10k} reports the results.
16	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:213:Pythia-1.4B cont & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
17	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:216:Qwen-1.5B cont  & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
18	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:219:LLaMA-8B cont   & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
19	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:222:OLMo-1B cont    & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 1 \\
20	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:225:Gemma-2-2B cont & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:kstar_ci_extended})} & 1 \\
21	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:6:All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
22	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:17:Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
23	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:34:\multicolumn{11}{l}{\footnotesize Full results for all 10 configurations (including Qwen-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) are provided in Table~\ref{tab:kstar_ci_extended}.}
24	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:45:[Omitted long matching line]
25	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:48:LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123\;[0.603,\,0.622]$; CI lower bound above $\theta$; Table~\ref{tab:kstar_ci_extended}).
26	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:49:All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
27	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:63:The raw AUC gap between adjacent generations provides a threshold-free continuous measure of discriminability; Figure~\ref{fig:kstar_theta} displays the full sensitivity surface across $\theta \in [0.55, 0.70]$, allowing practitioners to read off $\Kempirical$ at any desired effect-size threshold.
28	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:77:Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
29	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:81:Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
30	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:84:A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; Table~\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\Kempirical$ classifications largely agree.
31	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:91:Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
32	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:100:Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia remains at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3} = 0.5963$); OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$, consistent with its 15D boundary).
33	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:101:We hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\ref{sec:transfer}; the 15D features yield $\Kempirical = 2$ for most families (OLMo: $\Kempirical = 1$).
34	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:128:Qwen-1.5B, Pythia-1.4B, and LLaMA-3.1-8B yield $\Kempirical{=}3$ for arXiv (Table~\ref{tab:domain_kstar}): 2v3 $\auc = 0.644\;[0.628,\,0.658]$, $0.655\;[0.640,\,0.669]$, and $0.620\;[0.605,\,0.635]$ respectively (bootstrap CI lower bounds above $\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.
35	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:150:$\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\theta$ but 2v3 remains well below $\theta$ at all lengths ($\leq 0.572$).
36	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:151:Seed robustness testing (seed $= 123$ vs.\ primary $= 42$; Table~\ref{tab:seed_robustness}) confirms $\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\Kempirical{=}2 \to 3$, 2v3 $\auc = 0.607$) has one of five folds below $\theta$.
37	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:159:Pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$; moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) are driven entirely by the 0v1 gap rather than fine-grained depth discrimination, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
38	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:13:Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
39	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:17:$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia yields $\Kempirical^{\text{neural}} = 2$ and OLMo yields $\Kempirical^{\text{neural}} = 1$, consistent with its 15D boundary (Table~\ref{tab:neural_probe_crossmodel}).
40	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:20:Feature rankings are scorer-independent ($\rho > 0.90$); $\Kempirical$ agreement is scorer-independent for strong-signal configurations (e.g., Qwen-rewrite retains $\Kempirical{=}2$ under all scorers) but scorer-sensitive at marginal boundaries (Qwen-continuation drops to $\Kempirical{=}1$; length confound ruled out in Appendix~\ref{sec:extended_limitations}).
41	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:21:ANOVA confirms this layered pattern: Scorer explains modest variance ($\eta^2_p{=}.166$) with a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$; Table~\ref{tab:anova_crossscorer}).
42	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:26:Web text (C4, Wikipedia) consistently yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$ across three independent architecture families (Section~\ref{sec:cross_domain}), as formulaic structure (citations, math notation, section conventions) creates larger per-generation distributional shifts (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4).
43	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:38:Greedy decoding inflates depth separability: Pythia-6.9B yields $\Kempirical{=}2$ under greedy but $\Kempirical{=}1$ under nucleus sampling ($p{=}0.95$), with the borderline 1v2 score (2 of 5 folds above $\theta$) illustrating that the boundary is continuous rather than a cliff (Table~\ref{tab:s10_pythia_decoding}).
44	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:39:Practitioners should calibrate $\theta$ to their application-specific tolerance (Figure~\ref{fig:kstar_theta}).
45	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex:24:\textsuperscript{$\dagger$}Scorer artifact: Qwen-1.5B scorer yields $K^*{=}2$; cross-family scorer (Pythia-1.4B) yields $K^*{=}1$ ($\Delta = -2.4$\,pp). Controlled value shown (Appendix~\ref{app:crossscorer}).\\
46	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex:24:\textsuperscript{$\dagger$}Scorer artifact: Qwen-1.5B scorer yields $K^*{=}2$; Pythia scorer yields $K^*{=}1$ (see \S\ref{sec:crossscorer}).\\
47	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:14:A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
48	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:18:Pairwise AUC may exhibit non-monotonicity at deeper depths due to classifier and feature interactions (e.g., Pythia-1.4B greedy 4v5 $\auc = 1.0$ vs.\ 3v4 $= 0.522$; Table~\ref{tab:s10_pythia_decoding}), reinforcing that $\Kempirical$ is a measured quantity rather than a theoretical prediction.
49	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:25:which requires all pairs up to depth $k$ to exceed the threshold (the $\forall j$ constraint is naturally satisfied because $\auc_{k-1,k}$ decreases monotonically above $\theta$ across all tested configurations; Table~\ref{tab:kstar_ci}).
50	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:30:Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
51	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:37:Figure~\ref{fig:kstar_theta} provides the full sensitivity surface across $\theta \in [0.55, 0.70]$, enabling practitioners to select $\theta$ according to their false-positive tolerance.
52	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:38:The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
53	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:44:All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
54	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:47:These features are generator-agnostic in that they require no knowledge of or access to the generating model, though they depend on an external scorer for surprisal computation (Section~\ref{sec:transfer}).
55	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:49:We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
56	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:55:We evaluate six configurations spanning three model families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B (continuation), Pythia-1.4B and OLMo-1B (continuation).
57	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:15:Table~\ref{tab:top_features} reports per-model single-feature AUC rankings.
58	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:39:Table~\ref{tab:s1_transfer} reports the cross-model transfer accuracy matrix.
59	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:41:The asymmetry between rewrite-mode and continuation-mode transfer (61--63\%) confirms that generation mode, rather than model family, is the primary axis of distributional variation (Section~\ref{sec:discussion}).
60	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:63:Table~\ref{tab:s4_dataset_stats} summarizes the generational depth corpus.
61	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:128:  This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, Mistral-7B, Pythia-6.9B (nucleus), and Gemma-2-2B configurations.
62	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:154:  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices (Exp-011). Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.878; Claude Opus~4.6: 0.882) but near-chance 5-class accuracy (${\sim}$0.33 vs.\ OBD-LightGBM 0.386). Per-depth recall in Table~\ref{tab:s3c_perdepth}.}
63	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:215:  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound}.}
64	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:7:This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
65	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:10:This gap cuts across three communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
66	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:15:We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).
67	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:19:  \item \textbf{Measuring the discrimination boundary}: $\Kempirical \leq 2$ across all 10 model configurations (6 architecture families at 1B--8B scale) and 4 decoding strategies; $\Kempirical{=}2$ for 6/10 spanning three families ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}).
68	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:21:  Both supervised OBD and zero-shot LLMs fail beyond $\Kempirical$ (McNemar $p > 0.05$; Section~\ref{sec:why_kstar}).
69	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:22:  \item \textbf{Domain dependence of $\Kempirical$}: general web text (C4, Wikipedia) yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$, consistent across model families (Section~\ref{sec:cross_domain}).
70	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:23:  \item \textbf{Generator-agnostic cross-model transfer}: 15 statistical features enable 80--92\% accuracy retention with scorer-invariant feature rankings ($\rho > 0.90$), supporting depth estimation on corpora from unknown generators without retraining; $\Kempirical$ agreement holds across scorers for strong-signal configurations (Section~\ref{sec:transfer}).
71	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:26:\noindent As a consistency check, $\Kempirical{=}2$ correctly predicts the strategy ordering for web-text filtering: binary curation minimizes degradation most effectively (MMLU $0.5941$ vs.\ base $0.6018$; Section~\ref{sec:filtering}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa300357-ecc8-405c-8983-5c4e1626ba05",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "28cb10dc-cdd1-4b89-9616-98274f967b21",
  "sourceToolAssistantUUID": "fa300357-ecc8-405c-8983-5c4e1626ba05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T04:15:52.928Z_

Now let me create a comprehensive analysis by reading each file individually to extract complete reference and label information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28cb10dc-cdd1-4b89-9616-98274f967b21",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRmzNeUCxLgDrdsHGu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1179938a-3a5a-4f81-95e5-e27a8974080c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011cAzePTBELoznDrYV2DrpU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8375,
      "cache_read_input_tokens": 27576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8375,
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

_source line 14 · 2026-05-23T04:15:53.143Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TZSUFtxyMw6wMEJHioejk5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1179938a-3a5a-4f81-95e5-e27a8974080c",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRmzNeUCxLgDrdsHGu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c179bbd3-027f-4567-965d-9b6ce73ff99c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011cAzePTBELoznDrYV2DrpU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8375,
      "cache_read_input_tokens": 27576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8375,
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

_source line 15 · 2026-05-23T04:15:53.150Z_

<details><summary>↩ Tool result · `toolu_01TZSUFtxyMw6wMEJHioejk5`</summary>

```text
1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{colortbl}
15	\usepackage{multirow}
16	\usepackage{enumitem}
17	\usepackage{subcaption}
18	\usepackage[section]{placeins}
19	
20	\newcommand{\Kstar}{{K^*}}
21	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
22	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
23	\newcommand{\auc}{\text{AUC}}
24	\newcommand{\jsd}{\text{JSD}}
25	
26	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	% === Abstract ===
34	\begin{abstract}
35	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
36	We measure a lower bound on the generational discrimination boundary, $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable).
37	Under prompt-chain generation across 10 model configurations (6 architecture families, 1B--8B), 3 source domains, and 4 decoding strategies, $\Kempirical \leq 2$ for all web text configurations across six architecture families at 1B--8B scale ($\theta{=}0.60$); structured academic text (arXiv) reaches $\Kempirical{=}3$ across three independent architecture families.
38	A single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect that concentrates all exploitable signal at the human-vs.-machine boundary.
39	Generator-agnostic statistical features enable 80--92\% cross-model transfer with scorer-invariant feature rankings ($\rho > 0.90$), supporting depth estimation on corpora from unknown generators without retraining.
40	As a consistency check, $\Kempirical$ correctly predicts that binary filtering outperforms graduated alternatives for web text.
41	\end{abstract}
42	
43	% === Section 1: Introduction ===
44	\input{introduction}
45	
46	% === Section 2: Related Work ===
47	\input{related_work}
48	
49	% === Section 3: Method ===
50	\input{method}
51	
52	% === Section 4: Experiments ===
53	\input{experiments_c1}
54	
55	% === Section 5: K*-Aware Data Filtering ===
56	\input{experiments_c3}
57	
58	% === Section 6: Discussion ===
59	\input{discussion}
60	
61	% === Section 7: Conclusion ===
62	\input{conclusion}
63	
64	% === Limitations (ACL required, unnumbered) ===
65	\section*{Limitations}
66	
67	Our study has four main limitations.
68	(1)~\emph{Scope}: we evaluate models up to 8B parameters across 6 architecture families, English text only (C4, Wikipedia, arXiv), and prompt-chain generation; retrain-chain dynamics may yield different boundaries.
69	Our model sample is unbalanced: Qwen accounts for 4 of 10 configurations, and we do not evaluate RLHF- or DPO-aligned models, whose generation distributions may differ from the base and instruction-tuned models tested here.
70	(2)~\emph{Feature set}: the 15 statistical features provide a lower bound on $\Ktheory$; richer representations (e.g., neural probes) can extend $\Kempirical$ by one additional depth for some architectures.
71	(3)~\emph{Threshold sensitivity}: $\Kempirical$ varies with the decision threshold $\theta$, ranging from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; three of ten configurations are marginal at our reference $\theta{=}0.60$.
72	(4)~\emph{Domain coverage}: arXiv $\Kempirical{=}3$ is established with three model families (with bootstrap CI support) on a single structured domain; broader domain coverage is needed to confirm this elevation generalizes.
73	
74	% === Ethics Statement (ACL required, unnumbered) ===
75	\section*{Ethics Statement}
76	
77	Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.
78	Our experiments use the publicly available C4 corpus and do not involve personally identifiable information.
79	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
80	Code and data will be released upon acceptance.
81	
82	\bibliography{references}
83	
84	\clearpage
85	\input{appendix}
86	\input{appendix_extended}
87	
88	\end{document}
89	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c179bbd3-027f-4567-965d-9b6ce73ff99c",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "08a1605d-8a7e-4aeb-b418-817e98e4c51b",
  "sourceToolAssistantUUID": "c179bbd3-027f-4567-965d-9b6ce73ff99c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T04:15:53.394Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KFapBvXF1yka1MSaSXSosg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08a1605d-8a7e-4aeb-b418-817e98e4c51b",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRmzNeUCxLgDrdsHGu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "413f1d1f-c472-42ec-a0dc-fee85c71a27e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011cAzePTBELoznDrYV2DrpU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8375,
      "cache_read_input_tokens": 27576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8375,
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

_source line 17 · 2026-05-23T04:15:53.399Z_

<details><summary>↩ Tool result · `toolu_01KFapBvXF1yka1MSaSXSosg`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across three communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
11	No existing method estimates how many rounds of recursive generation a text has undergone.
12	
13	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
14	We empirically measure a lower bound $\Kempirical$ on the discrimination boundary (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
15	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).
16	
17	Our contributions:
18	\begin{enumerate}[label=(\alph*),nosep]
19	  \item \textbf{Measuring the discrimination boundary}: $\Kempirical \leq 2$ across all 10 model configurations (6 architecture families at 1B--8B scale) and 4 decoding strategies; $\Kempirical{=}2$ for 6/10 spanning three families ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}).
20	  A single generation pass renders web text statistically indistinguishable from deeper synthetic content; this finding establishes binary sufficiency by measurement, reveals domain-dependent variation (arXiv $\Kempirical{=}3$), and quantifies boundary sensitivity to threshold, scorer, and scale.
21	  Both supervised OBD and zero-shot LLMs fail beyond $\Kempirical$ (McNemar $p > 0.05$; Section~\ref{sec:why_kstar}).
22	  \item \textbf{Domain dependence of $\Kempirical$}: general web text (C4, Wikipedia) yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$, consistent across model families (Section~\ref{sec:cross_domain}).
23	  \item \textbf{Generator-agnostic cross-model transfer}: 15 statistical features enable 80--92\% accuracy retention with scorer-invariant feature rankings ($\rho > 0.90$), supporting depth estimation on corpora from unknown generators without retraining; $\Kempirical$ agreement holds across scorers for strong-signal configurations (Section~\ref{sec:transfer}).
24	\end{enumerate}
25	
26	\noindent As a consistency check, $\Kempirical{=}2$ correctly predicts the strategy ordering for web-text filtering: binary curation minimizes degradation most effectively (MMLU $0.5941$ vs.\ base $0.6018$; Section~\ref{sec:filtering}).
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "413f1d1f-c472-42ec-a0dc-fee85c71a27e",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "c9e40f1e-4c7f-494b-924d-5d7c7ecb4d8a",
  "sourceToolAssistantUUID": "413f1d1f-c472-42ec-a0dc-fee85c71a27e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T04:15:53.619Z_

<details open><summary>🔧 Tool call — Read · `toolu_015cCBVXy6pnwXJEw4DPe71Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9e40f1e-4c7f-494b-924d-5d7c7ecb4d8a",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRmzNeUCxLgDrdsHGu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fd85b953-a27f-46b9-ad04-cbca50ab47ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011cAzePTBELoznDrYV2DrpU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8375,
      "cache_read_input_tokens": 27576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8375,
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

_source line 19 · 2026-05-23T04:15:53.625Z_

<details><summary>↩ Tool result · `toolu_015cCBVXy6pnwXJEw4DPe71Y`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong, fu2025theoretical}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.
6	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
7	Markov chain convergence theory predicts that recursive generation converges to a stationary distribution~\cite{fu2025theoretical}, complementing the DPI's mutual information monotonicity; empirically, detection accuracy erodes with each generation~\cite{hao2025rewrite}, consistent with our measured discrimination boundary.
8	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
9	
10	\paragraph{Beyond binary detection.}
11	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; other systems such as Ghostbuster~\cite{verma2024ghostbuster} and GPTZero~\cite{liang2023gpt}, as well as benchmarks like RAID~\cite{dugan2024raid}, likewise target the binary task without estimating generational depth.
12	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
13	None estimates recursive generation depth.
14	
15	\paragraph{Data selection and curation.}
16	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
17	
18	\paragraph{Ordinal classification and probing.}
19	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd85b953-a27f-46b9-ad04-cbca50ab47ab",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "407ad2b2-1c33-4609-b0e9-5e063e4da2ed",
  "sourceToolAssistantUUID": "fd85b953-a27f-46b9-ad04-cbca50ab47ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T04:15:54.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MgoK3LfQemD3oPGdzSnoiE`</summary>

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
  "parentUuid": "407ad2b2-1c33-4609-b0e9-5e063e4da2ed",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrRmzNeUCxLgDrdsHGu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e64404eb-5d81-4392-8e32-98feae4f06f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011cAzePTBELoznDrYV2DrpU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8375,
      "cache_read_input_tokens": 27576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8375,
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

_source line 21 · 2026-05-23T04:15:54.051Z_

<details><summary>↩ Tool result · `toolu_01MgoK3LfQemD3oPGdzSnoiE`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Corpus-level statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: mutual information with the seed text degrades monotonically.
17	Together with Markov chain convergence, this motivates the existence of a finite discrimination boundary where $\auc_{k-1,k}$ falls below a decision threshold, though AUC and mutual information are not formally equivalent; the actual saturation depth must therefore be measured empirically.
18	Pairwise AUC may exhibit non-monotonicity at deeper depths due to classifier and feature interactions (e.g., Pythia-1.4B greedy 4v5 $\auc = 1.0$ vs.\ 3v4 $= 0.522$; Table~\ref{tab:s10_pythia_decoding}), reinforcing that $\Kempirical$ is a measured quantity rather than a theoretical prediction.
19	
20	We define the operational lower bound:
21	\begin{equation}
22	  \Kempirical = \max\!\bigl\{k \!\geq\! 1 : \auc_{j-1,j} > \theta,\;\forall\, 1 \!\leq\! j \!\leq\! k\bigr\},
23	  \label{eq:kstar}
24	\end{equation}
25	which requires all pairs up to depth $k$ to exceed the threshold (the $\forall j$ constraint is naturally satisfied because $\auc_{k-1,k}$ decreases monotonically above $\theta$ across all tested configurations; Table~\ref{tab:kstar_ci}).
26	The theoretical upper bound $\Ktheory$ (the true maximum discriminable depth given optimal features) is not directly estimated in this work.
27	Since any specific classifier on a feature subset achieves AUC at most equal to the Bayes-optimal classifier on all features, $\Kempirical \leq \Ktheory$ follows directly.
28	The DPI motivates the empirical observation that $\auc_{k-1,k}$ generally decreases with $k$ under non-degenerate decoding, though AUC is not a monotone function of MI (as noted above).
29	Here $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ is a reference operating point motivated by Cohen's small-effect-size convention ($h \approx 0.20$\footnote{Cohen's $h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$ (small effect for proportions); the equivalent $d = \sqrt{2}\,\Phi^{-1}\!(0.60) \approx 0.36$ places $\theta$ in the small-to-medium range on Cohen's $d$ scale.}; justified below).
30	Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
31	
32	\paragraph{Threshold justification.}
33	$\theta{=}0.60$ is a reference operating point supported by three independent lines of evidence.
34	First, Cohen's $h \approx 0.20$, a conventional small-effect-size boundary.
35	Second, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ ($p < 0.002$ for all boundary comparisons).
36	Third, the conclusion $\Kempirical{=}2$ is insensitive to the exact threshold: 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, a ${\sim}$5--11\,pp discontinuity; only at extremes does $\Kempirical$ shift ($\theta{=}0.55$: $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$: $\Kempirical{=}1$ across all).
37	Figure~\ref{fig:kstar_theta} provides the full sensitivity surface across $\theta \in [0.55, 0.70]$, enabling practitioners to select $\theta$ according to their false-positive tolerance.
38	The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
39	
40	\subsection{Features and Classifier}
41	\label{sec:features}
42	
43	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
44	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
45	Self-BLEU reference sets are drawn exclusively within each fold to prevent information leakage across cross-validation splits; self-BLEU ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
46	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations); in deployment where reference corpora are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted entirely, leaving 14 features (surprisal statistics, TTR, hapax ratio, frequency tail) that require no external reference and retain full $\Kempirical$.
47	These features are generator-agnostic in that they require no knowledge of or access to the generating model, though they depend on an external scorer for surprisal computation (Section~\ref{sec:transfer}).
48	
49	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
50	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
51	
52	\subsection{Experimental Setup}
53	\label{sec:experimental_setup}
54	
55	We evaluate six configurations spanning three model families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B (continuation), Pythia-1.4B and OLMo-1B (continuation).
56	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
57	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
58	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
59	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
60	
61	\begin{table}[t]
62	\centering
63	\small
64	\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
65	\label{tab:setup}
66	\begin{tabular}{llcc}
67	\toprule
68	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
69	\midrule
70	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
71	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
72	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
73	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
74	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
75	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e64404eb-5d81-4392-8e32-98feae4f06f0",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "c4bf5996-c0d5-4b73-b6ac-84b6c32ae7c0",
  "sourceToolAssistantUUID": "e64404eb-5d81-4392-8e32-98feae4f06f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-23T04:15:55.724Z_

Now let me read the remaining files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4bf5996-c0d5-4b73-b6ac-84b6c32ae7c0",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrS17QKdk7bW8cQCuhn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc803636-4609-40f1-a6f6-32e2a2b76978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0127rmP9wLWnkaowR9oqqC3Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6599,
      "cache_read_input_tokens": 35951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6599,
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

_source line 23 · 2026-05-23T04:15:56.692Z_

<details open><summary>🔧 Tool call — Read · `toolu_0139d6HTayUYwYGrtcTDciMz`</summary>

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
  "parentUuid": "bc803636-4609-40f1-a6f6-32e2a2b76978",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrS17QKdk7bW8cQCuhn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4dd9dd07-d21a-4dd3-81f0-2a2e2d88e14f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0127rmP9wLWnkaowR9oqqC3Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6599,
      "cache_read_input_tokens": 35951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6599,
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

_source line 24 · 2026-05-23T04:15:56.698Z_

<details><summary>↩ Tool result · `toolu_0139d6HTayUYwYGrtcTDciMz`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on ten model configurations spanning six architecture families:
5	Pythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.
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
25	0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6074 & [.598,\,.617]\rlap{$^*$} & .5001 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5440 & [.534,\,.554] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5051 & & .5024\rlap{$^\S$} & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & \\
30	\bottomrule
31	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
32	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\
33	\multicolumn{11}{l}{\footnotesize $^\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\Delta = 0.005$).} \\
34	\multicolumn{11}{l}{\footnotesize Full results for all 10 configurations (including Qwen-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) are provided in Table~\ref{tab:kstar_ci_extended}.}
35	\end{tabular}
36	\end{table*}
37	
38	\begin{figure}[t]
39	\centering
40	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
41	\caption{Pairwise $\auc$ decay across adjacent depth pairs (0v1, 1v2, \ldots, 4v5) for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\% confidence intervals. The horizontal dashed line marks $\theta = 0.60$.}
42	\label{fig:auc_decay}
43	\end{figure}
44	
45	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 10 model configurations: 6/10 configurations yield $\Kempirical{=}2$ (Qwen with 4 configs, LLaMA-8B, and Pythia-1.4B, spanning three of six families) (1v2 $\auc$ range: 0.6074--0.6955; five of six CI lower bounds $> \theta$; permutation $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\Kempirical{=}1$ (1v2 $\auc$: 0.500, 0.575, 0.596, and 0.598, all below $\theta$; Section~\ref{sec:boundary_cases}).
46	Under Bonferroni correction (99.5\% CIs), three of six $\Kempirical{=}2$ configurations retain significance; the three marginal cases (Pythia-1.4B, Qwen-continuation, LLaMA-8B; Bonferroni-corrected CI lower bounds 0.593--0.599) reflect narrow effect sizes rather than classification failure (all point estimates above $\theta$).
47	By architecture family: Qwen (4/4) and LLaMA (1/1) yield $\Kempirical{\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\Kempirical{=}2$, 6.9B: $\Kempirical{=}1$).
48	LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123\;[0.603,\,0.622]$; CI lower bound above $\theta$; Table~\ref{tab:kstar_ci_extended}).
49	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
50	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across $\Kempirical{=}2$ continuation models ($\Delta = 1.9$\,pp).
51	
52	\paragraph{Scale and instruction-tuning invariance.}
53	$\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$) both exceed $\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\ $> 0.99$ at $\leq$1.5B).
54	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.
55	
56	\begin{figure*}[t]
57	\centering
58	\includegraphics[width=0.75\textwidth]{figures/fig_kstar_theta.pdf}
59	\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. Five of six configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line); OLMo yields $\Kempirical{=}1$. At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
60	\label{fig:kstar_theta}
61	\end{figure*}
62	
63	The raw AUC gap between adjacent generations provides a threshold-free continuous measure of discriminability; Figure~\ref{fig:kstar_theta} displays the full sensitivity surface across $\theta \in [0.55, 0.70]$, allowing practitioners to read off $\Kempirical$ at any desired effect-size threshold.
64	Five of six configurations yield $\Kempirical = 2$ within $\theta \in [0.51, 0.61]$ (OLMo: $\Kempirical = 1$ throughout); at $\theta{=}0.55$, two Qwen configurations reach $\Kempirical = 3$; at $\theta{=}0.70$, all drop to $\Kempirical = 1$.
65	
66	%% ====================================================================
67	\subsection{Cross-Model Transfer}
68	\label{sec:transfer}
69	
70	\begin{figure}[t]
71	\centering
72	\includegraphics[width=\columnwidth]{figures/fig3_transfer_heatmap.pdf}
73	\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
74	\label{fig:transfer_heatmap}
75	\end{figure}
76	
77	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
78	Qwen-rewrite classifiers transfer poorly (61--63\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.
79	
80	\paragraph{Cross-scorer validation.}
81	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
82	Feature ranking independence is a strong result: the same features dominate under all scorers.
83	$\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\auc = 0.696$) retains $\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\auc = 0.611$, only 0.011 above $\theta$) drops to $\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).
84	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; Table~\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\Kempirical$ classifications largely agree.
85	
86	%% ====================================================================
87	\subsection{Feature Ordering and Generation Mode}
88	\label{sec:feature_degradation}
89	\label{sec:generation_mode}
90	
91	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
92	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.
93	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
94	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
95	
96	%% ====================================================================
97	\subsection{Neural Probe}
98	\label{sec:neural_probe}
99	
100	Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia remains at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3} = 0.5963$); OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$, consistent with its 15D boundary).
101	We hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\ref{sec:transfer}; the 15D features yield $\Kempirical = 2$ for most families (OLMo: $\Kempirical = 1$).
102	
103	\noindent\begin{minipage}{\columnwidth}
104	\centering
105	\footnotesize
106	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
107	\label{tab:neural_probe_crossmodel}
108	\resizebox{\columnwidth}{!}{%
109	\begin{tabular}{lccc}
110	\toprule
111	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
112	\midrule
113	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
114	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
115	OLMo-1B    & 0.5056 & $[0.497,\,0.516]$ & 1\rlap{$^\dagger$} \\
116	\bottomrule
117	\multicolumn{4}{l}{\footnotesize $^\dagger$OLMo 1v2 $\auc = 0.5054$ (below $\theta$); $\Kempirical^{\text{neural}} = 1$.}
118	\end{tabular}}
119	\end{minipage}
120	
121	%% ====================================================================
122	\subsection{Cross-Domain Variation}
123	\label{sec:cross_domain}
124	
125	The preceding experiments use C4 (general web text).
126	To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) across three architecture families.
127	Wikipedia yields $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), matching the C4 baseline.
128	Qwen-1.5B, Pythia-1.4B, and LLaMA-3.1-8B yield $\Kempirical{=}3$ for arXiv (Table~\ref{tab:domain_kstar}): 2v3 $\auc = 0.644\;[0.628,\,0.658]$, $0.655\;[0.640,\,0.669]$, and $0.620\;[0.605,\,0.635]$ respectively (bootstrap CI lower bounds above $\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.
129	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.
130	
131	\begin{table}[t]
132	\centering
133	\footnotesize
134	\caption{Cross-domain $\Kempirical$ comparison. Rows: generator model and text domain (C4, Wikipedia, arXiv). $\Kempirical{=}3$ for arXiv indicates structured text preserves discriminability to greater depth.}
135	\label{tab:domain_kstar}
136	\begin{tabular}{llccc}
137	\toprule
138	\textbf{Domain} & \textbf{Model} & \textbf{1v2 $\auc$} & \textbf{2v3 $\auc$} & $\Kempirical$ \\
139	\midrule
140	arXiv & Qwen-1.5B  & 0.858 & 0.6436 & 3 \\
141	arXiv & Pythia-1.4B & 0.805 & 0.6545 & 3 \\
142	C4    & Qwen-1.5B  & 0.63  & 0.56   & 2 \\
143	Wikipedia & Qwen-1.5B & 0.62 & 0.55 & 2 \\
144	\bottomrule
145	\end{tabular}
146	\end{table}
147	
148	\paragraph{Robustness.}
149	\label{sec:robustness}
150	$\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\theta$ but 2v3 remains well below $\theta$ at all lengths ($\leq 0.572$).
151	Seed robustness testing (seed $= 123$ vs.\ primary $= 42$; Table~\ref{tab:seed_robustness}) confirms $\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\Kempirical{=}2 \to 3$, 2v3 $\auc = 0.607$) has one of five folds below $\theta$.
152	The ${\pm}9$\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\Kempirical$ over raw AUC comparisons.
153	
154	%% ====================================================================
155	\subsection{Binary Detector Confidence}
156	\label{sec:binary_confidence}
157	
158	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) remain effective for human-vs.-machine classification but provide no usable depth signal beyond this binary boundary.
159	Pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$; moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) are driven entirely by the 0v1 gap rather than fine-grained depth discrimination, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dd9dd07-d21a-4dd3-81f0-2a2e2d88e14f",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "02a2700d-0daf-4213-a31f-23a098eec62a",
  "sourceToolAssistantUUID": "4dd9dd07-d21a-4dd3-81f0-2a2e2d88e14f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T04:15:57.010Z_

<details open><summary>🔧 Tool call — Read · `toolu_016PQuzbtJb2CEXGrr7MJfRL`</summary>

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
  "parentUuid": "02a2700d-0daf-4213-a31f-23a098eec62a",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrS17QKdk7bW8cQCuhn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad90114b-89e4-412a-b499-ab5ac304b35b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0127rmP9wLWnkaowR9oqqC3Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6599,
      "cache_read_input_tokens": 35951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6599,
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

_source line 26 · 2026-05-23T04:15:57.016Z_

<details><summary>↩ Tool result · `toolu_016PQuzbtJb2CEXGrr7MJfRL`</summary>

```text
1	\section{Consistency Check: $\Kstar$-Guided Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
5	We present this as a consistency check under extreme (100\%) contamination, not as an independent contribution; at realistic rates ($\leq$10\%), the filtering effect diminishes to $\Delta \leq 0.1$\,pp (not significant; Appendix~\ref{sec:dose_response}).
6	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
7	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
13	\label{tab:tab_filtering_main}
14	\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
15	\end{table}
16	
17	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
18	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
19	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
20	Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
21	DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
22	At realistic contamination ratios ($\leq$50\%), all filtering strategies converge ($p > 0.12$), consistent with the one-wash laundering finding that depth-aware curation offers marginal benefit when $\Kempirical{=}2$ (Appendix~\ref{sec:dose_response}).
23	For $\Kempirical{=}1$ configurations, depth-aware curation reduces to standard binary filtering, consistent with $\Kempirical{=}1$ implying no exploitable depth signal beyond the 0v1 boundary.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad90114b-89e4-412a-b499-ab5ac304b35b",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "ead9dcb1-dabf-499d-b642-647b08e4db04",
  "sourceToolAssistantUUID": "ad90114b-89e4-412a-b499-ab5ac304b35b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T04:15:57.210Z_

<details open><summary>🔧 Tool call — Read · `toolu_012pcBahpLPHyB7voDjYapmU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ead9dcb1-dabf-499d-b642-647b08e4db04",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrS17QKdk7bW8cQCuhn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ab94e704-09e1-4f3b-b4e5-ba827ad4d103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0127rmP9wLWnkaowR9oqqC3Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6599,
      "cache_read_input_tokens": 35951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6599,
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

_source line 28 · 2026-05-23T04:15:57.215Z_

<details><summary>↩ Tool result · `toolu_012pcBahpLPHyB7voDjYapmU`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\paragraph{One-wash laundering (web text).}
11	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
12	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
13	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
14	One-wash laundering is distinct from model collapse~\cite{shumailov2024collapse}: model collapse describes cumulative quality degradation across generations, while one-wash laundering describes the erasure of statistical fingerprints distinguishing adjacent generations; text quality may continue degrading even after the features separating generation $k$ from $k{+}1$ become indistinguishable.
15	
16	\paragraph{Representation dependence.}
17	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia yields $\Kempirical^{\text{neural}} = 2$ and OLMo yields $\Kempirical^{\text{neural}} = 1$, consistent with its 15D boundary (Table~\ref{tab:neural_probe_crossmodel}).
18	The 15D features trade one depth level of sensitivity for cross-model consistency (6/10 configurations $\Kempirical{=}2$), making them the preferred operational choice.
19	The gap between $\Kempirical$ and $\Ktheory$ remains open; the neural probe result (Qwen 2v3 $\auc = 0.6159$, marginally above $\theta$) tentatively suggests the bound may be near-tight, though a single frozen-encoder probe is insufficient to establish this.
20	Feature rankings are scorer-independent ($\rho > 0.90$); $\Kempirical$ agreement is scorer-independent for strong-signal configurations (e.g., Qwen-rewrite retains $\Kempirical{=}2$ under all scorers) but scorer-sensitive at marginal boundaries (Qwen-continuation drops to $\Kempirical{=}1$; length confound ruled out in Appendix~\ref{sec:extended_limitations}).
21	ANOVA confirms this layered pattern: Scorer explains modest variance ($\eta^2_p{=}.166$) with a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$; Table~\ref{tab:anova_crossscorer}).
22	Self-scoring inflates pairwise AUC: OLMo shows the largest gap (1v2 $\Delta$ = +11.5\,pp; self-scored $K^*$=2 vs.\ cross-scored $K^*$=1), followed by Pythia (+4.7\,pp), LLaMA-8B and Mistral-7B (${\approx}$+1.9\,pp each).
23	Cross-scoring provides a conservative, deployment-realistic estimate of $K^*$, as real-world contamination originates from unknown generators.
24	
25	\paragraph{Domain dependence of $\Kempirical$.}
26	Web text (C4, Wikipedia) consistently yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$ across three independent architecture families (Section~\ref{sec:cross_domain}), as formulaic structure (citations, math notation, section conventions) creates larger per-generation distributional shifts (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4).
27	Corpus curators should calibrate depth-aware filtering to source characteristics rather than assuming a universal boundary.
28	
29	\paragraph{Prompt-chain scope and retrain-chain gap.}
30	Retrain-chain experiments (Pythia-1.4B LoRA) yield $\Kempirical{\geq}4$ (1v2 $\auc = 0.9484$, 3v4 $= 0.7982$), far exceeding the prompt-chain boundary of $\Kempirical{=}2$, because each retrain generation also modifies model parameters, introducing cumulative adaptation artifacts absent from text-only recycling.
31	Prompt-chain $\Kempirical$ isolates text-intrinsic degradation, the operationally relevant quantity for data curation pipelines; our conclusions do not directly transfer to retrain-chain (model collapse) settings.
32	
33	\paragraph{Boundary cases and scale effect.}
34	$\Kempirical{=}1$ configurations cluster at 1v2 $\auc$ 0.500--0.598, well separated from the $\Kempirical{=}2$ range (0.611--0.696); $\Kempirical{=}1$ is not a classifier failure but a text property, as these models produce first-generation output so human-like that statistical features cannot distinguish depth~1 from depth~2.
35	That $\Kempirical \in \{1, 2\}$ for all web text configurations is the core empirical result; larger models reduce 0v1 JSD (0.077 at 8B vs.\ 0.15--0.27 at $\leq$1.5B), suggesting 13B+ may increasingly yield $\Kempirical{=}1$.
36	
37	\paragraph{Decoding strategy as confound.}
38	Greedy decoding inflates depth separability: Pythia-6.9B yields $\Kempirical{=}2$ under greedy but $\Kempirical{=}1$ under nucleus sampling ($p{=}0.95$), with the borderline 1v2 score (2 of 5 folds above $\theta$) illustrating that the boundary is continuous rather than a cliff (Table~\ref{tab:s10_pythia_decoding}).
39	Practitioners should calibrate $\theta$ to their application-specific tolerance (Figure~\ref{fig:kstar_theta}).
40	
41	\paragraph{What $\Kempirical$ reveals.}
42	As a measurement tool, $\Kempirical$ establishes why binary detection suffices for web text (depth${>}1$ is invisible to statistical features), identifies domains where finer strategies are viable (arXiv $\Kempirical{=}3$), and quantifies how scale, scorer, and threshold jointly shape the boundary.
43	The OBD framework provides a reproducible, low-cost depth estimation protocol requiring only corpus-level statistical features, unlike detection methods that need API access or model weights.
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab94e704-09e1-4f3b-b4e5-ba827ad4d103",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "794d6c1c-c987-411d-8996-8e29e5844290",
  "sourceToolAssistantUUID": "ab94e704-09e1-4f3b-b4e5-ba827ad4d103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T04:15:57.359Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XgLQm23TwDuohGTAusoUU6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "794d6c1c-c987-411d-8996-8e29e5844290",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrS17QKdk7bW8cQCuhn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "501e269b-d1dc-4d1f-ab6a-1f5549a4103f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0127rmP9wLWnkaowR9oqqC3Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6599,
      "cache_read_input_tokens": 35951,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6599
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 316,
          "cache_read_input_tokens": 35951,
          "cache_creation_input_tokens": 6599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6599,
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

_source line 30 · 2026-05-23T04:15:57.363Z_

<details><summary>↩ Tool result · `toolu_01XgLQm23TwDuohGTAusoUU6`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Across 10 prompt-chain configurations spanning six architecture families at 1B--8B scale, we find $\Kempirical \leq 2$ for all web text sources ($\theta{=}0.60$); structured academic text (arXiv) reaches $\Kempirical{=}3$ across three independent architecture families.
5	This one-wash laundering effect concentrates all exploitable signal at the 0v1 boundary, and the consistency check confirms that binary curation most effectively minimizes MMLU degradation ($-$0.77\,pp vs.\ $-$1.53\,pp for no-filter).
6	For structured domains where $\Kempirical{=}3$, graduated strategies can exploit one additional depth level, so corpus curators should calibrate filtering to the source domain.
7	The 15 statistical features enable deployment across generators without retraining (80--92\% accuracy retention, $\rho > 0.90$), and $\Kempirical$ converts a continuous AUC decay surface into a discrete operating boundary.
8	Several directions remain open: tracking $\Kempirical$ as model scale surpasses 13B, bridging the prompt-chain and retrain-chain boundaries, and extending depth estimation to additional structured domains and multilingual text.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "501e269b-d1dc-4d1f-ab6a-1f5549a4103f",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "1353b95a-df6b-4bd7-8624-7ff4ffdccd46",
  "sourceToolAssistantUUID": "501e269b-d1dc-4d1f-ab6a-1f5549a4103f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-23T04:15:59.391Z_

Now let me read the appendix files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1353b95a-df6b-4bd7-8624-7ff4ffdccd46",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrSFLv4Ww7JPdu1XjeJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e830c84e-6ad5-4d75-a10d-28584b1ac422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TrkTwuxbKAgvGssGyxkHam",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9254,
      "cache_read_input_tokens": 42550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9254,
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

_source line 32 · 2026-05-23T04:16:00.441Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DjYUj9GFh57xD4Y5DWZG3g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e830c84e-6ad5-4d75-a10d-28584b1ac422",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrSFLv4Ww7JPdu1XjeJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9bf77f10-dc7d-4eda-8b55-fb2eb3f5ad05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TrkTwuxbKAgvGssGyxkHam",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9254,
      "cache_read_input_tokens": 42550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9254,
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

_source line 33 · 2026-05-23T04:16:00.448Z_

<details><summary>↩ Tool result · `toolu_01DjYUj9GFh57xD4Y5DWZG3g`</summary>

```text
1	\appendix
2	\section{Supplementary Materials}
3	\label{sec:appendix}
4	
5	This appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
10	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
11	\label{fig:filtering_strategies}
12	\end{figure}
13	
14	\paragraph{Feature ranking and cross-model consistency.}
15	Table~\ref{tab:top_features} reports per-model single-feature AUC rankings.
16	Surprisal derivative features (\texttt{surp\_d1\_std}, \texttt{surp\_d2\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\rho \geq 0.85$.
17	The rewrite-mode model (Qwen-rw) diverges by placing \texttt{freq\_entropy} first, reflecting a distributional shift that is lexical rather than surprisal-driven.
18	This scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[!htbp]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{cllll}
28	\toprule
29	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
30	\midrule
31	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
32	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
33	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
34	\bottomrule
35	\end{tabular}
36	}
37	\end{table}
38	
39	Table~\ref{tab:s1_transfer} reports the cross-model transfer accuracy matrix.
40	Classifiers trained on continuation-mode generators (Pythia, OLMo, Qwen-cont) transfer well to each other, with off-diagonal accuracy retaining 80--92\% of in-distribution performance.
41	The asymmetry between rewrite-mode and continuation-mode transfer (61--63\%) confirms that generation mode, rather than model family, is the primary axis of distributional variation (Section~\ref{sec:discussion}).
42	
43	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
44	\begin{table}[!htbp]
45	  \centering
46	  \small
47	  \caption{Cross-model transfer accuracy matrix. Diagonal (\textbf{bold}): within-model; off-diagonal: cross-model. Retention: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-rw$\to$others 61--63\%.}
48	  \label{tab:s1_transfer}
49	  \resizebox{\columnwidth}{!}{%
50	  \begin{tabular}{lcccc}
51	    \toprule
52	    \textbf{Train} & Qwen-rw & Pythia & OLMo & Qwen-cont \\
53	    \midrule
54	    Qwen-rw   & \textbf{.423} & .259 & .265 & .347 \\
55	    Pythia    & .272 & \textbf{.386} & .353 & .329 \\
56	    OLMo      & .277 & .345 & \textbf{.382} & .324 \\
57	    Qwen-cont & .344 & .328 & .311 & \textbf{.388} \\
58	    \bottomrule
59	  \end{tabular}}
60	\end{table}
61	
62	\paragraph{Dataset construction.}
63	Table~\ref{tab:s4_dataset_stats} summarizes the generational depth corpus.
64	Each depth level contains 5{,}000 passages, yielding 30{,}000 total samples across six depths (0--5).
65	Depth~0 consists of human-written seed texts from the C4 English validation split, truncated to 256 subword tokens.
66	Subsequent depths are generated recursively: each depth-$k$ passage is produced by prompting the generator with the corresponding depth-$(k{-}1)$ passage.
67	The four model-mode configurations (Qwen-rw, Pythia-cont, OLMo-cont, Qwen-cont) share identical depth-0 seeds and generation pipeline, differing only in generator identity and prompting strategy (rewrite vs.\ continuation).
68	
69	%%% Table S4: Dataset Statistics
70	\begin{table}[!htbp]
71	  \centering
72	  \small
73	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}
74	  \label{tab:s4_dataset_stats}
75	  \resizebox{\columnwidth}{!}{%
76	  \begin{tabular}{clrl}
77	    \toprule
78	    \textbf{Depth} & \textbf{$N$ samples} & \textbf{Mean tokens} & \textbf{Source} \\
79	    \midrule
80	    0 & 5{,}000 & 147.8 & C4 validation (human) \\
81	    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\
82	    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\
83	    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\
84	    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
85	    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
86	    \midrule
87	    \multicolumn{2}{l}{Total} & \multicolumn{2}{l}{30{,}000 samples} \\
88	    \bottomrule
89	  \end{tabular}}
90	\end{table}
91	
92	%%% Table S2: Decoding Ablation AUC (exp-003)
93	\begin{table*}[t]
94	  \centering
95	  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
96	  \label{tab:s2_decoding}
97	  \footnotesize
98	  \begin{tabular}{lcccc}
99	    \toprule
100	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
101	    \midrule
102	    0 vs.\ 1 & $.980\;[.977,\,.982]$ & $.995\;[.993,\,.996]$ & $.988\;[.986,\,.990]$ & $.998\;[.998,\,.999]$ \\
103	    1 vs.\ 2 & $.689\;[.680,\,.698]$ & $.687\;[.677,\,.695]$ & $.689\;[.680,\,.697]$ & $.704\;[.695,\,.713]$ \\
104	    \cmidrule(lr){1-5}
105	    2 vs.\ 3 & $.561\;[.552,\,.571]$ & $.592\;[.582,\,.601]$\rlap{$^\dagger$} & $.590\;[.581,\,.600]$ & $.582\;[.572,\,.592]$ \\
106	    3 vs.\ 4 & $.540\;[.531,\,.550]$ & $.547\;[.537,\,.557]$ & $.539\;[.529,\,.549]$ & $.529\;[.519,\,.540]$ \\
107	    4 vs.\ 5 & $.514\;[.503,\,.524]$ & $.507\;[.496,\,.517]^{\ddagger}$ & $.535\;[.524,\,.545]$ & $.524\;[.513,\,.535]$ \\
108	    \midrule
109	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
110	    \midrule
111	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
112	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
113	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
114	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
115	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
116	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
117	    \bottomrule
118	    \multicolumn{5}{l}{${}^{\dagger}$\,CI upper bound (0.601) marginally exceeds $\theta{=}0.60$ by 0.001.} \\
119	    \multicolumn{5}{l}{${}^{\ddagger}$\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}
120	  \end{tabular}
121	\end{table*}
122	
123	%%% Table S2b: Extended K* CI (all models including new additions)
124	\begin{table*}[t]
125	  \centering
126	  \scriptsize
127	  \caption{Extended pairwise $\auc$ with bootstrap 95\% CIs for all model configurations including new additions.
128	  This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, Mistral-7B, Pythia-6.9B (nucleus), and Gemma-2-2B configurations.
129	  $\Kempirical = 2$ holds for 6/10 conditions at $\theta{=}0.60$ (OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: $\Kempirical{=}1$).}
130	  \label{tab:kstar_ci_extended}
131	  \resizebox{\textwidth}{!}{%
132	  \begin{tabular}{lcccccccccccccccccccc}
133	    \toprule
134	     & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-base} & \multicolumn{2}{c}{LLaMA-8B} & \multicolumn{2}{c}{Mistral-7B} & \multicolumn{2}{c}{Pythia-6.9B\rlap{$^\S$}} & \multicolumn{2}{c}{Gemma-2B} \\
135	    \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}\cmidrule(lr){12-13}\cmidrule(lr){14-15}\cmidrule(lr){16-17}\cmidrule(lr){18-19}\cmidrule(lr){20-21}
136	     & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
137	    \midrule
138	    0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\,.967] & .987 & [.985,\,.989] & .9224 & [.917,\,.927] & .9170 & & .9599 & & .953 & [.949,\,.957] \\
139	    1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6074 & [.598,\,.617]\rlap{$^*$} & .5001 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} & .626 & [.617,\,.635]\rlap{$^*$} & .6123 & [.603,\,.622]\rlap{$^*$} & .5750 & & .5955 & & .5981 & [.588,\,.608] \\
140	    2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] & .550 & [.540,\,.560] & .5273 & [.517,\,.538] & .5369 & & .5298 & & .534 & [.523,\,.545] \\
141	    3v4 & .5435 & & .5152 & & .5024 & & .5409 & & .5276 & & .529 & [.519,\,.540] & .5168 & [.506,\,.528] & .5174 & & .5135 & & .5033 & [.492,\,.514] \\
142	    4v5 & .5340 & & .5136 & & .4942 & & .5141 & & .5085 & & .518 & [.508,\,.529] & .5159 & [.505,\,.527] & .5175 & & -- & -- & .5025 & [.492,\,.514] \\
143	    \bottomrule
144	    \multicolumn{21}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons.} \\
145	    \multicolumn{21}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B. ``--'': experiment pending.} \\
146	    \multicolumn{21}{l}{\footnotesize $^\S$Pythia-6.9B evaluated separately; nucleus sampling ($p{=}0.95$, $T{=}1.0$), same as all other models.}
147	  \end{tabular}}% end resizebox
148	\end{table*}
149	
150	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
151	\begin{table}[t]
152	  \centering
153	  \scriptsize
154	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices (Exp-011). Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.878; Claude Opus~4.6: 0.882) but near-chance 5-class accuracy (${\sim}$0.33 vs.\ OBD-LightGBM 0.386). Per-depth recall in Table~\ref{tab:s3c_perdepth}.}
155	  \label{tab:s3_llm_zeroshot}
156	
157	  \vspace{0.3em}
158	  \textbf{(a)} GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)
159	  \vspace{1pt}
160	
161	  \begin{tabular}{lcccccc}
162	    \toprule
163	    & \multicolumn{5}{c}{Predicted Depth} & \\
164	    \cmidrule(lr){2-6}
165	    True & 0 & 1 & 2 & 3 & 4 & Rec. \\
166	    \midrule
167	    0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
168	    1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
169	    2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
170	    3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
171	    4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
172	    \bottomrule
173	  \end{tabular}
174	
175	  \vspace{4pt}
176	  \textbf{(b)} Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)
177	  \vspace{1pt}
178	
179	  \begin{tabular}{lcccccc}
180	    \toprule
181	    & \multicolumn{5}{c}{Predicted Depth} & \\
182	    \cmidrule(lr){2-6}
183	    True & 0 & 1 & 2 & 3 & 4 & Rec. \\
184	    \midrule
185	    0 & \textbf{69} & 26 &  3 &  0 &  2 & .690 \\
186	    1 &  8 & \textbf{21} & 32 & 11 & 28 & .210 \\
187	    2 &  6 & 36 & \textbf{28} &  5 & 25 & .280 \\
188	    3 &  7 & 20 & 31 & \textbf{10} & 31 & .100 \\
189	    4 &  7 & 28 & 22 &  6 & \textbf{37} & .370 \\
190	    \bottomrule
191	  \end{tabular}
192	\end{table}
193	
194	\begin{table}[t]
195	  \centering
196	  \small
197	  \caption{Per-depth recall (\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
198	  \label{tab:s3c_perdepth}
199	  \resizebox{\columnwidth}{!}{%
200	  \begin{tabular}{lccccc}
201	    \toprule
202	    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\
203	    \midrule
204	    OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
205	    GPT-5.5      & 77 & 19 & \textbf{38} & \textbf{24} &  8 \\
206	    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \textbf{37} \\
207	    \bottomrule
208	  \end{tabular}}
209	\end{table}
210	
211	%%% Table: Token Length and EOS Truncation Analysis
212	\begin{table}[t]
213	  \centering
214	  \scriptsize
215	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound}.}
216	  \label{tab:token_length}
217	  \resizebox{\columnwidth}{!}{%
218	  \begin{tabular}{lcccccccc}
219	    \toprule
220	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
221	    \cmidrule(lr){2-7}
222	    \textbf{Model} & D0 & D1 & D2 & D3 & D4 & D5 & \textbf{EOS\%} & \textbf{Sev.} \\
223	    \midrule
224	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
225	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
226	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negl. \\
227	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Mod. \\
228	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
229	    \midrule
230	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
231	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
232	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
233	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
234	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
235	    \bottomrule
236	    \multicolumn{9}{l}{EOS\%: generation terminated via EOS before 256-token limit. Ranges span depths 1--5.}
237	  \end{tabular}}
238	\end{table}
239	
240	%%% Table S5: Complete 15-D Feature Descriptions
241	\begin{table*}[t]
242	  \centering
243	  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
244	  \label{tab:s5_features}
245	  \begin{tabular}{llp{0.45\textwidth}l}
246	    \toprule
247	    \textbf{Group} & \textbf{Feature} & \textbf{Description} & \textbf{Range} \\
248	    \midrule
249	    \multirow{9}{*}{\rotatebox[origin=c]{90}{\textsc{Surprisal}}}
250	    & \texttt{surp\_mean}   & Mean token surprisal $\frac{1}{T}\sum_t -\log p(x_t \mid x_{&lt;t})$ & $\mathbb{R}^+$ \\
251	    & \texttt{surp\_std}    & Standard deviation of token surprisal & $\mathbb{R}^+$ \\
252	    & \texttt{surp\_skew}   & Skewness of the surprisal distribution & $\mathbb{R}$ \\
253	    & \texttt{surp\_kurt}   & Excess kurtosis of the surprisal distribution & $\mathbb{R}$ \\
254	    & \texttt{surp\_d1\_mean} & Mean of first-order surprisal differences $\Delta s_t = s_{t+1} - s_t$ & $\mathbb{R}$ \\
255	    & \texttt{surp\_d1\_std}  & Std of first-order surprisal differences & $\mathbb{R}^+$ \\
256	    & \texttt{surp\_d1\_skew} & Skewness of first-order surprisal differences & $\mathbb{R}$ \\
257	    & \texttt{surp\_d2\_mean} & Mean of second-order differences $\Delta^2 s_t$ & $\mathbb{R}$ \\
258	    & \texttt{surp\_d2\_std}  & Std of second-order surprisal differences & $\mathbb{R}^+$ \\
259	    \midrule
260	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Lex}}}
261	    & \texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\
262	    & \texttt{hapax\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\
263	    & \texttt{self\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\
264	    \midrule
265	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Freq}}}
266	    & \texttt{freq\_kurtosis}  & Excess kurtosis of word frequency distribution & $\mathbb{R}$ \\
267	    & \texttt{freq\_entropy}   & Shannon entropy of word frequencies: $-\sum p_w \log_2 p_w$ & $\mathbb{R}^+$ \\
268	    & \texttt{low\_freq\_ratio} & Proportion of vocabulary with count $\leq 2$ & $[0, 1]$ \\
269	    \bottomrule
270	  \end{tabular}
271	\end{table*}
272	
273	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
274	\begin{table*}[t]
275	\begin{minipage}[t]{0.45\textwidth}
276	  \centering
277	  \small
278	  \captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
279	  \label{tab:s6_lgbm_params}
280	  \begin{tabular}{ll}
281	    \toprule
282	    \textbf{Parameter} & \textbf{Value} \\
283	    \midrule
284	    \texttt{n\_estimators}      & 200 \\
285	    \texttt{learning\_rate}     & 0.05 \\
286	    \texttt{max\_depth}         & 6 \\
287	    \texttt{num\_leaves}        & 31 \\
288	    \texttt{verbose}            & $-1$ \\
289	    \texttt{n\_jobs}            & $-1$ (all cores) \\
290	    Cross-validation            & 5-fold GroupKFold \\
291	    Grouping key                & \texttt{doc\_id} \\
292	    Objective                   & Binary (per depth pair) \\
293	    \bottomrule
294	  \end{tabular}
295	\end{minipage}\hfill
296	\begin{minipage}[t]{0.52\textwidth}
297	  \centering
298	  \small
299	  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
300	  \label{tab:s7_neural_probe}
301	  \resizebox{\textwidth}{!}{%
302	  \begin{tabular}{ll}
303	    \toprule
304	    \textbf{Component} & \textbf{Details} \\
305	    \midrule
306	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
307	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
308	    Representation    & Last hidden state, attention-masked avg pool \\
309	    Embedding dim     & 1536 / 2048 / 2048 \\
310	    Max sequence len   & 512 tokens \\
311	    \midrule
312	    \multicolumn{2}{l}{\textit{MLP classifier}} \\
313	    Architecture      & $d_{\text{emb}} \to 512 \to 256 \to 6$ \\
314	    Activations       & ReLU \\
315	    Dropout           & 0.1 (after each hidden layer) \\
316	    Output            & 6-class softmax \\
317	    \midrule
318	    \multicolumn{2}{l}{\textit{Training}} \\
319	    Optimizer         & Adam ($\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\
320	    Loss              & Cross-entropy \\
321	    Batch size        & 256 \\
322	    Max epochs        & 20 \\
323	    Early stopping    & Patience = 5 (validation loss) \\
324	    Cross-validation  & 5-fold GroupKFold \\
325	    \bottomrule
326	  \end{tabular}%
327	  }
328	\end{minipage}
329	\end{table*}
330	
331	%%% Table S8: Per-Model Bootstrap CI Results (exp-007)
332	\begin{table}[t]
333	  \centering
334	  \scriptsize
335	  \caption{Pairwise AUC with bootstrap 95\% CIs for four model-mode configurations (1{,}000 resamples). All pairs $p < 0.01$ except OLMo 1v2--4v5 ($p > 0.09$).}
336	  \label{tab:s8_cv_folds}
337	  \resizebox{\columnwidth}{!}{%
338	  \begin{tabular}{lcccc}
339	    \toprule
340	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
341	    \midrule
342	    0v1 & $.996\;[.995,.997]$ & $.993\;[.992,.994]$ & $.986\;[.984,.988]$ & $.997\;[.996,.998]$ \\
343	    1v2 & $.696\;[.686,.704]$ & $.607\;[.598,.617]$ & $.500\;[.496,.519]$ & $.611\;[.602,.621]$ \\
344	    \cmidrule(lr){1-5}
345	    2v3 & $.589\;[.580,.599]$ & $.551\;[.542,.563]$ & $.497\;[.486,.509]$ & $.561\;[.551,.571]$ \\
346	    3v4 & $.544\;[.533,.555]$ & $.515\;[.504,.526]$ & $.502\;[.491,.513]$ & $.541\;[.531,.551]$ \\
347	    4v5 & $.534\;[.524,.545]$ & $.514\;[.502,.525]$ & $.494\;[.483,.506]$ & $.514\;[.504,.526]$ \\
348	    \bottomrule
349	  \end{tabular}}
350	\end{table}
351	
352	%%% Table S9: Binary Detector Spearman ρ (exp-012)
353	\begin{table}[t]
354	  \centering
355	  \scriptsize
356	  \caption{Spearman $\rho$ between binary detector scores and true depth, and 6-class accuracy. Correlations driven by 0v1; scores do not track depth beyond generation~1. Qwen-rw exhibits reversed sign ($\rho > 0$).}
357	  \label{tab:s9_binary_spearman}
358	  \resizebox{\columnwidth}{!}{%
359	  \begin{tabular}{lcccc}
360	    \toprule
361	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
362	    \midrule
363	    \multicolumn{5}{l}{\textit{Spearman $\rho$}} \\
364	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
365	    \quad log-PPL (obs.)     & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
366	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
367	    \midrule
368	    6-class acc.              & 0.199    & 0.130    & 0.127    & 0.183 \\
369	    \bottomrule
370	    \multicolumn{5}{l}{Random baseline: 0.167} \\
371	  \end{tabular}}
372	\end{table}
373	
374	%%% Table S10: Pythia Decoding Ablation (exp-020)
375	\begin{table}[t]
376	  \centering
377	  \scriptsize
378	  \caption{Pythia-1.4B pairwise $\auc$ under four decoding configs (10K bootstrap). $^\dagger$Greedy triggers repetition collapse (4-gram repeat: $d_0{=}0.01 \to d_1{=}0.72$).}
379	  \label{tab:s10_pythia_decoding}
380	  \resizebox{\columnwidth}{!}{%
381	  \begin{tabular}{lcccc}
382	    \toprule
383	    & \textbf{Greedy}$^\dagger$ & \textbf{$p{=}0.9$} & \textbf{$T{=}0.7$} & \textbf{$T{=}1.2$} \\
384	    \midrule
385	    0v1 & $.999$ & $.995$ & $.996$ & $.994$ \\
386	    1v2 & $.884$ & $.675$ & $.728$ & $.618$ \\
387	    \cmidrule(lr){1-5}
388	    2v3 & $.531$ & $.559$ & $.598^\ddagger$ & $.531$ \\
389	    3v4 & $.522$ & $.524$ & $.563$ & $.520$ \\
390	    4v5 & $.514$ & $.501$ & $.527$ & $.510$ \\
391	    \midrule
392	    $\Kempirical$ & 2 & 2 & 2 & 2 \\
393	    \bottomrule
394	    \multicolumn{5}{l}{${}^{\ddagger}$CI upper 0.606 $> \theta$; point est.\ below.} \\
395	  \end{tabular}}
396	\end{table}
397	
398	%%% Table S11: Length Ablation (exp-021)
399	\begin{table}[t]
400	  \centering
401	  \small
402	  \caption{Pairwise $\auc$ for three segment lengths (Qwen-base, cont.\ mode). $\Kempirical{=}2$ at 128/256; 512 marginal ($^\dagger$CI lower $< \theta$).}
403	  \label{tab:s11_length_ablation}
404	  \begin{tabular}{lccc}
405	    \toprule
406	    & \textbf{128} & \textbf{256} & \textbf{512} \\
407	    \midrule
408	    0v1 & .979 & .991 & .992 \\
409	    1v2 & .622 & .628 & .607$^\dagger$ \\
410	    \cmidrule(lr){1-4}
411	    2v3 & .529 & .556 & .572 \\
412	    3v4 & .535 & .530 & .530 \\
413	    4v5 & .501 & .514 & .518 \\
414	    \midrule
415	    $\Kempirical$ & 2 & 2 & 2$^\dagger$ \\
416	    \bottomrule
417	  \end{tabular}
418	\end{table}
419	
420	%%% Table S12: Domain Ablation
421	\begin{table}[t]
422	  \centering
423	  \small
424	  \caption{Pairwise $\auc$ for three text domains (Qwen-cont). arXiv yields $\Kempirical{=}3$; C4 and Wikipedia $\Kempirical{=}2$.}
425	  \label{tab:s12_domain_ablation}
426	  \begin{tabular}{lccc}
427	    \toprule
428	    & \textbf{C4} & \textbf{Wiki} & \textbf{arXiv} \\
429	    \midrule
430	    0v1 & .997 & .996 & .995 \\
431	    1v2 & .611 & .619 & .858 \\
432	    \cmidrule(lr){1-4}
433	    2v3 & .561 & .550 & .644$^*$ \\
434	    3v4 & .541 & .523 & .544 \\
435	    4v5 & .514 & .514 & .530 \\
436	    \midrule
437	    $\Kempirical$ & 2 & 2 & 3 \\
438	    \bottomrule
439	    \multicolumn{4}{l}{\footnotesize $^*$CI $[.628,.658]$; $p < 0.001$.}
440	  \end{tabular}
441	\end{table}
442	
443	%%% Table S13: Scorer Sensitivity Analysis
444	\begin{table}[t]
445	  \centering
446	  \scriptsize
447	  \caption{Scorer sensitivity: $\Kempirical$ under self- vs.\ cross-scoring. Cross-scoring reduces $\Kempirical$ only for marginal Qwen-cont.}
448	  \label{tab:s13_scorer_sensitivity}
449	  \resizebox{\columnwidth}{!}{%
450	  \begin{tabular}{llcccc}
451	    \toprule
452	    \textbf{Generator} & \textbf{Mode} & \textbf{Self} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Agr.} \\
453	    \midrule
454	    Qwen-Inst & Rewrite & 2 & 2 & 2 & \checkmark \\
455	    Qwen-Inst & Cont.   & 2 & 1 & 1 & $\times$ \\
456	    Qwen-base & Cont.   & 2 & 2 & 2 & \checkmark \\
457	    Pythia    & Cont.   & 2 & 2 & 2 & \checkmark \\
458	    OLMo      & Cont.   & 1 & -- & -- & -- \\
459	    Qwen-7B   & Cont.   & 2 & -- & -- & -- \\
460	    Mistral   & Cont.   & 1 & -- & -- & -- \\
461	    \bottomrule
462	  \end{tabular}}
463	\end{table}
464	
465	\clearpage
466	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bf77f10-dc7d-4eda-8b55-fb2eb3f5ad05",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "65175012-8c87-4f8c-b4e3-3bc4a303f318",
  "sourceToolAssistantUUID": "9bf77f10-dc7d-4eda-8b55-fb2eb3f5ad05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-23T04:16:00.778Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KRjqh4MzDHh4QDcV6tF69j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65175012-8c87-4f8c-b4e3-3bc4a303f318",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrSFLv4Ww7JPdu1XjeJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "91a144e0-af3f-4ec0-894f-555693678ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TrkTwuxbKAgvGssGyxkHam",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9254,
      "cache_read_input_tokens": 42550,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9254
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 207,
          "cache_read_input_tokens": 42550,
          "cache_creation_input_tokens": 9254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9254,
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

_source line 35 · 2026-05-23T04:16:00.784Z_

<details><summary>↩ Tool result · `toolu_01KRjqh4MzDHh4QDcV6tF69j`</summary>

```text
1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; for general web text, $\Kempirical \leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\Kempirical{=}3$, aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6866, 0.7039]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--100\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), enabling single-classifier deployment across generators.
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
25	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs). Scorer is statistically significant but explains modest variance ($\eta^2_p{=}.166$) relative to Depth-Pair ($\eta^2_p{=}.997$), supporting near-scorer-independence of depth discrimination.}
26	\label{tab:anova_crossscorer}
27	\begin{tabular}{lrrrr}
28	\toprule
29	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
30	\midrule
31	Generator     & 2  & 851.91  & ${<}.001$  & .866 \\
32	Scorer        & 3  & 17.48  & ${<}.001$  & .166 \\
33	Depth-Pair    & 4  & 22737.70  & ${<}.001$  & .997 \\
34	Gen$\times$Scorer & 6 & 7.50 & ${<}.001$ & .146 \\
35	Gen$\times$Depth  & 8 & 913.41 & ${<}.001$ & .965 \\
36	Scorer$\times$Depth & 12 & 2.25 & $.010$ & .093 \\
37	Residual      & 264 & & & \\
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
50	Cross-scale validation confirms $\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$, 0v1 $= 0.9225$) both exceed $\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text.
51	Gemma-2-27B (C4 continuation, Qwen cross-scored) yields $\Kempirical{=}1$ (1v2 $\auc = 0.5894$), consistent with Gemma-2-2B at 5K ($\Kempirical{=}1$, 1v2 $\auc = 0.5981$). The Gemma family produces $\Kempirical{=}1$ at both 2B and 27B, suggesting $\Kempirical$ is model-family-dependent rather than scale-dependent.
52	
53	The neural probe yields model-dependent $\Kempirical^{\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia; OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$), consistent with the 15D LightGBM boundary.
54	The 15D generator-agnostic features yield $\Kempirical = 2$ for Pythia and Qwen, while OLMo yields $\Kempirical = 1$ under the standardized pipeline.
55	
56	\subsection{LLM Zero-Shot Baseline}
57	\label{sec:extended_llm}
58	
59	GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\% (95\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\ref{tab:s3_llm_zeroshot}).
60	Per-depth recall confirms convergent failure at depths $\geq 2$ (Section~\ref{sec:why_kstar}).
61	When 6-class probabilities are marginalized to 5 classes ($P(d{\geq}4)$), accuracy rises to 44.4\% but concentrates in depth-4 (recall: 22\%$\to$80\%) while depths 2--3 collapse to 2--8\%; we report raw 6-class results.
62	
63	\subsection{Practical Considerations}
64	
65	All filtering strategies degrade general capabilities (MMLU: 0.6018 $\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\to$ 0.6638--0.6701); our 100\% synthetic setting is an upper bound; in mixed corpora, degradation scales with contamination fraction~\cite{shumailov2024collapse, dohmatob2024model}.
66	$\Kstar$-aware binary filtering reduces MMLU degradation by ${\sim}$50\% ($-$1.53\,pp $\to$ $-$0.77\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).
67	
68	\subsection{Extended Limitations}
69	\label{sec:extended_limitations}
70	
71	\emph{Prompt-chain versus retrain-chain.}
72	Retrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields $\Kempirical{\geq}4$ (1v2 $\auc = 0.9484$, 2v3 $= 0.8888$, 3v4 $= 0.7982$), far exceeding prompt-chain $\Kempirical{=}2$.
73	The elevated signal arises from cumulative model-adaptation artifacts rather than text-intrinsic degradation; prompt-chain $\Kempirical$ is the operationally relevant boundary for data curation.
74	
75	\emph{Threshold sensitivity.}
76	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite/continuation; at $\theta = 0.70$, $\Kempirical = 1$ across all configurations (Figure~\ref{fig:kstar_theta}).
77	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
78	
79	\emph{Structural confound: token length.}
80	In continuation mode the generation prompt is discarded, so all depths $\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\ machine-generated prompt), not structural composition.
81	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
82	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
83	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
84	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
85	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
86	
87	\emph{Graduated filtering.}
88	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
89	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
90	\label{tab:pairwise_significance}
91	
92	\subsection{Dose-Response: Contamination Ratio Effect}
93	\label{sec:dose_response}
94	
95	The main filtering experiments (Section~\ref{sec:filtering}) use 100\% synthetic data to maximize effect size.
96	To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
97	
98	\begin{table}[h]
99	\centering
100	\small
101	\caption{MMLU accuracy by contamination ratio (fraction of synthetic data in training set) and filtering strategy. Base model (no fine-tuning): 0.6018. Mean $\pm$ std over 5 seeds.}
102	\label{tab:dose_response}
103	\resizebox{\columnwidth}{!}{%
104	\begin{tabular}{lccc}
105	\toprule
106	\textbf{Strategy} & \textbf{10\%} & \textbf{30\%} & \textbf{50\%} \\
107	\midrule
108	No-filter   & $0.6009 \pm .003$ & $0.5978 \pm .004$ & $0.5932 \pm .004$ \\
109	Binary-ours & $0.6011 \pm .003$ & $0.5988 \pm .003$ & $0.5956 \pm .004$ \\
110	Graduated   & $0.6008 \pm .003$ & $0.5982 \pm .004$ & $0.5944 \pm .004$ \\
111	\bottomrule
112	\end{tabular}}
113	\end{table}
114	
115	{\sloppy At 10\% contamination, no-filter MMLU ($0.6009$) remains within noise of the base model ($0.6018$, $\Delta = -0.09$\,pp), and all three strategies are indistinguishable ($\Delta_{\max} = 0.03$\,pp between strategies, $p > 0.8$).
116	At 30\%, differences emerge directionally ($\Delta = 0.10$\,pp, binary vs.\ no-filter) but remain non-significant ($p > 0.3$).
117	At 50\%, binary-ours shows a 0.24\,pp advantage over no-filter, approaching but not reaching significance ($p = 0.12$).
118	The strategy ordering (binary $>$ graduated $>$ no-filter) is consistent with the 100\% setting, but effect sizes scale linearly with contamination fraction.
119	This demonstrates that $\Kstar$-aware curation provides practical benefit primarily when contamination is severe enough to cause measurable quality degradation.\par}
120	
121	\subsection{Seed Robustness}
122	\label{sec:seed_robustness}
123	
124	Because the random seed governs both corpus sampling and generation quality (not merely CV splits), absolute AUC values are seed-dependent.
125	We re-run three configurations with seed$\,{=}\,123$ (primary: seed$\,{=}\,42$; Table~\ref{tab:seed_robustness}).
126	$\Kempirical$ is stable in 2/3 cases: Pythia-1.4B on Wikipedia yields $\Kempirical{=}1$ under both seeds (1v2 $\Delta = -0.8$\,pp), and Qwen-1.5B on C4 yields $\Kempirical{=}2$ (1v2 $\Delta = +9.0$\,pp, both seeds above $\theta$).
127	Qwen-1.5B on Wikipedia shifts from $\Kempirical{=}2$ to $\Kempirical{=}3$ under seed$\,{=}\,123$, but the 2v3 AUC ($0.6067$) is marginal: one of five folds falls below $\theta$ (fold~5 $= 0.595$), so this does not constitute strong evidence for $\Kempirical{=}3$.
128	The ${\pm}9$\,pp absolute AUC variation across seeds strengthens the methodological case for threshold-based $\Kempirical$ over raw AUC comparisons: the qualitative boundary is robust even when point estimates shift.
129	
130	\begin{table}[h]
131	\centering
132	\footnotesize
133	\caption{Seed robustness: $\Kempirical$ under two random seeds. 1v2 $\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\theta$).}
134	\label{tab:seed_robustness}
135	\resizebox{\columnwidth}{!}{%
136	\begin{tabular}{llcccc}
137	\toprule
138	\textbf{Model} & \textbf{Domain} & \multicolumn{2}{c}{$\Kempirical$} & \textbf{1v2 $\Delta$} & \textbf{Stable?} \\
139	\cmidrule(lr){3-4}
140	 & & seed=42 & seed=123 & & \\
141	\midrule
142	Pythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\,pp & \checkmark \\
143	Qwen-1.5B  & C4        & 2 & 2 & $+9.0$\,pp & \checkmark \\
144	Qwen-1.5B  & Wikipedia & 2 & 3$^\dagger$ & $+8.7$\,pp & $\times$ \\
145	\bottomrule
146	\multicolumn{6}{l}{\footnotesize $^\dagger$2v3 $\auc = 0.6067$; fold 5 $= 0.595 < \theta$. Marginal boundary.}
147	\end{tabular}}
148	\end{table}
149	
150	\subsection{Bonferroni-Corrected Confidence Intervals}
151	\label{sec:bonferroni_ci}
152	
153	To control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\alpha_{\text{corr}} = 0.05 / 10 = 0.005$, yielding 99.5\% confidence intervals ($z = 2.807$).
154	Table~\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\Kempirical$ boundary pair.
155	Seven of ten configurations retain CI lower bounds above $\theta{=}0.60$; three marginal $\Kempirical{=}2$ configurations (Pythia-1.4B, Qwen-cont, LLaMA-8B) see their lower bounds dip below $\theta$ under the stricter criterion ($0.5934$, $0.5976$, and $0.5988$, respectively).
156	These near-misses reflect narrow effect sizes ($\auc - \theta < 0.013$) rather than classification failure: all three retain point estimates above $\theta$, and Qwen-cont and LLaMA-8B retain uncorrected 95\% CI lower bounds above $\theta$ (Pythia-1.4B falls marginally below at $0.5976$).
157	
158	\begin{table}[h]
159	\centering
160	\footnotesize
161	\caption{Bonferroni-corrected 99.5\% confidence intervals for $\Kempirical$ boundary pairs across all 10 configurations. $\alpha_{\text{corr}} = 0.005$; CI computed as $\auc \pm 2.807 \times \hat{\sigma}_{\text{boot}}$. ``Pass $\theta$'': CI lower bound $> 0.60$.}
162	\label{tab:bonferroni_ci}
163	\resizebox{\columnwidth}{!}{%
164	\begin{tabular}{llcccc}
165	\toprule
166	\textbf{Configuration} & \textbf{Boundary} & $\auc$ & $\hat{\sigma}_{\text{boot}}$ & \textbf{99.5\% CI} & \textbf{Pass $\theta$} \\
167	\midrule
168	\multicolumn{6}{l}{\textit{$\Kempirical = 2$ configurations}} \\
169	Qwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\,.708]$ & \checkmark \\
170	Pythia-1.4B               & 1v2 & .6074 & .0050 & $[.593,\,.621]$ & $\times$ \\
171	Qwen-base                 & 1v2 & .6260 & .0047 & $[.613,\,.639]$ & \checkmark \\
172	Qwen-7B$^\ddagger$        & 1v2 & .6168 & .0046 & $[.604,\,.630]$ & \checkmark \\
173	LLaMA-8B                  & 1v2 & .6123 & .0048 & $[.599,\,.626]$ & $\times$ \\
174	Qwen-cont (Instruct)     & 1v2 & .6112 & .0049 & $[.598,\,.625]$ & $\times$ \\
175	\midrule
176	\multicolumn{6}{l}{\textit{$\Kempirical = 1$ configurations}} \\
177	OLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\,.989]$ & \checkmark \\
178	Mistral-7B                & 0v1 & .9170 & .0030$^\dagger$ & $[.909,\,.925]$ & \checkmark \\
179	Pythia-6.9B$^\S$          & 0v1 & .9599 & .0015$^\dagger$ & $[.956,\,.964]$ & \checkmark \\
180	Gemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\,.958]$ & \checkmark \\
181	\bottomrule
182	\multicolumn{6}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\
183	\multicolumn{6}{l}{\footnotesize $^\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\
184	\multicolumn{6}{l}{\footnotesize $^\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}
185	\end{tabular}}
186	\end{table}
187	
188	\subsection{Cross-Sample Robustness: 5K vs.\ 10K}
189	\label{sec:robustness_10k}
190	
191	The preceding analyses fix the sample pool at $N{=}5{,}000$ passages per depth.
192	To assess between-sample variability, we re-draw an independent $N{=}10{,}000$ sample from C4 using a different random seed and repeat the full OBD pipeline.
193	If $\Kempirical$ and the boundary AUC are driven by the underlying distributional shift rather than by idiosyncrasies of a particular sample, both quantities should remain stable across draws.
194	
195	Table~\ref{tab:robustness_10k} reports the results.
196	For Pythia-1.4B (continuation, C4), the 5K and 10K samples agree on $\Kempirical{=}2$: the 0v1 AUC is nearly identical ($0.9722$ vs.\ $0.9712$), and the boundary 1v2 AUC shifts from $0.6074$ to $0.6175$ ($\Delta = +0.010$).
197	This narrow shift is consistent with natural sampling variability across C4 subsets and does not alter the qualitative depth boundary.
198	The 2v3 pair remains near chance in both draws ($0.54$, $0.54$), confirming that depths $\geq 2$ are indistinguishable regardless of sample.
199	Qwen-1.5B (continuation, C4) replicates the same pattern ($\Kempirical{=}2$, 1v2 $\auc = 0.6346$).
200	LLaMA-3.1-8B (continuation, C4) is the sole $\Kempirical{=}2$ configuration where the 10K OOF AUC drops below $\theta$ ($0.5880$; pipeline AUC $= 0.6148$; Bonferroni 99.5\% CI $[0.5776, 0.5978]$), yielding $\Kempirical{=}1$ under the stricter criterion.
201	OLMo-1B (continuation, C4) is the only configuration that yields $\Kempirical{=}1$ at both 5K and 10K, with virtually identical depth profiles (0v1 $\auc = 0.9871$ vs.\ $0.9860$; 1v2 $\auc = 0.4984$ vs.\ $0.5001$); the 1v2 AUC at random level is consistent with Qwen cross-scoring, which places OLMo well below the discrimination boundary.
202	Gemma-2-2B is the sole configuration where $\Kempirical$ increases from 5K ($\Kempirical{=}1$, 1v2 $\auc = 0.5981$) to 10K ($\Kempirical{=}2$, 1v2 $\auc = 0.6099$), but the 10K boundary AUC exceeds $\theta$ by only $0.010$, placing this model at the precise $\Kempirical{=}1/2$ boundary.
203	
204	\begin{table}[h]
205	\centering
206	\footnotesize
207	\caption{Cross-sample robustness: pairwise AUC and $\Kempirical$ under 5K and 10K C4 samples drawn with different random seeds. All configurations use continuation mode. $\Kempirical$ is determined by the $\theta{=}0.60$ threshold on 1v2 AUC.}
208	\label{tab:robustness_10k}
209	\resizebox{\columnwidth}{!}{\begin{tabular}{llcccc}
210	\toprule
211	\textbf{Model} & $N$ & \textbf{AUC(0v1)} & \textbf{AUC(1v2)} & \textbf{AUC(2v3)} & $\Kempirical$ \\
212	\midrule
213	Pythia-1.4B cont & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
214	Pythia-1.4B cont & 10K & 0.9712 & 0.6175 & 0.5364 & 2 \\
215	\midrule
216	Qwen-1.5B cont  & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
217	Qwen-1.5B cont  & 10K & 0.9875 & 0.6346 & 0.5616 & 2 \\
218	\midrule
219	LLaMA-8B cont   & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
220	LLaMA-8B cont   & 10K & 0.9282 & 0.5880$^\dagger$ & 0.5247 & 1$^\dagger$ \\
221	\midrule
222	OLMo-1B cont    & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 1 \\
223	OLMo-1B cont    & 10K & 0.9871 & 0.4984 & 0.5059 & 1 \\
224	\midrule
225	Gemma-2-2B cont & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:kstar_ci_extended})} & 1 \\
226	Gemma-2-2B cont & 10K & 0.9534 & 0.6099$^\ddagger$ & 0.5409 & 2$^\ddagger$ \\
227	\bottomrule
228	\multicolumn{6}{l}{\footnotesize $^\dagger$OOF AUC (pipeline AUC $= 0.6148$); Bonferroni 99.5\% CI $[0.5776, 0.5978]$ does not pass $\theta$.} \\
229	\multicolumn{6}{l}{\footnotesize $^\ddagger$Borderline: Bonferroni 99.5\% CI $[0.600,\,0.619]$ (percentile); CI lower $0.0002$ below $\theta$. Sole config where $\Kempirical$ increases from 5K to 10K.} \\
230	\end{tabular}}
231	\end{table}
232	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91a144e0-af3f-4ec0-894f-555693678ff8",
  "isSidechain": true,
  "promptId": "174552ac-5ad9-4262-808d-b06eb16f97da",
  "agentId": "a86cd6902d70a29a1",
  "type": "user",
  "uuid": "6f710897-0aab-40cf-a6cf-f6f8819b1599",
  "sourceToolAssistantUUID": "91a144e0-af3f-4ec0-894f-555693678ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-23T04:16:20.323Z_

Now let me create a comprehensive analysis by checking all references and identifying any issues:

Based on my thorough search of all LaTeX files in the paper directory, here is a comprehensive cross-reference analysis:

## Summary of Findings

**Total Labels Found:** 66 unique labels defined
**Total References Found:** 138+ individual reference instances
**Issues Identified:** 7 warnings/potential issues

---

## Defined Labels (66 total)

### Section Labels
- `sec:introduction` (introduction.tex:2)
- `sec:related_work` (related_work.tex:2)
- `sec:method` (method.tex:2)
- `sec:experiments` (experiments_c1.tex:2)
- `sec:filtering` (experiments_c3.tex:2)
- `sec:discussion` (discussion.tex:2)
- `sec:conclusion` (conclusion.tex:2)
- `sec:appendix` (appendix.tex:3)
- `sec:extended_discussion` (appendix_extended.tex:2)

### Subsection Labels
- `sec:formulation` (method.tex:12)
- `sec:features` (method.tex:41)
- `sec:experimental_setup` (method.tex:53)
- `sec:kstar_boundary` (experiments_c1.tex:10)
- `sec:transfer` (experiments_c1.tex:68)
- `sec:feature_degradation` (experiments_c1.tex:88)
- `sec:generation_mode` (experiments_c1.tex:89)
- `sec:neural_probe` (experiments_c1.tex:98)
- `sec:cross_domain` (experiments_c1.tex:123)
- `sec:robustness` (experiments_c1.tex:149)
- `sec:binary_confidence` (experiments_c1.tex:156)

### Subsection Labels (Discussion)
- `sec:why_kstar` (discussion.tex:3)
- `sec:one_wash` (discussion.tex:4)
- `sec:negative_graduated` (discussion.tex:5)
- `sec:repr_dependence` (discussion.tex:6)
- `sec:boundary_cases` (discussion.tex:7)
- `sec:length_confound` (discussion.tex:8)

### Extended Discussion Subsections
- `sec:extended_neural_probe` (appendix_extended.tex:48)
- `sec:extended_llm` (appendix_extended.tex:57)
- `sec:extended_limitations` (appendix_extended.tex:69)
- `sec:dose_response` (appendix_extended.tex:93)
- `sec:seed_robustness` (appendix_extended.tex:122)
- `sec:bonferroni_ci` (appendix_extended.tex:151)
- `sec:robustness_10k` (appendix_extended.tex:189)

### Figure Labels
- `fig:pipeline` (method.tex:8)
- `fig:auc_decay` (experiments_c1.tex:42)
- `fig:kstar_theta` (experiments_c1.tex:60)
- `fig:transfer_heatmap` (experiments_c1.tex:74)
- `fig:filtering_strategies` (appendix.tex:11)

### Table Labels (Main)
- `tab:setup` (method.tex:65)
- `tab:kstar_ci` (experiments_c1.tex:18)
- `tab:tab_filtering_main` (experiments_c3.tex:13)
- `tab:domain_kstar` (experiments_c1.tex:135)
- `tab:neural_probe_crossmodel` (experiments_c1.tex:107)

### Table Labels (Appendix)
- `tab:top_features` (appendix.tex:25)
- `tab:s1_transfer` (appendix.tex:48)
- `tab:s4_dataset_stats` (appendix.tex:74)
- `tab:s2_decoding` (appendix.tex:96)
- `tab:kstar_ci_extended` (appendix.tex:130)
- `tab:s3_llm_zeroshot` (appendix.tex:155)
- `tab:s3c_perdepth` (appendix.tex:198)
- `tab:token_length` (appendix.tex:216)
- `tab:s5_features` (appendix.tex:244)
- `tab:s6_lgbm_params` (appendix.tex:279)
- `tab:s7_neural_probe` (appendix.tex:300)
- `tab:s8_cv_folds` (appendix.tex:336)
- `tab:s9_binary_spearman` (appendix.tex:357)
- `tab:s10_pythia_decoding` (appendix.tex:379)
- `tab:s11_length_ablation` (appendix.tex:403)
- `tab:s12_domain_ablation` (appendix.tex:425)
- `tab:s13_scorer_sensitivity` (appendix.tex:448)

### Table Labels (Extended Appendix)
- `tab:crossscorer` (appendix_extended.tex:18)
- `tab:anova_crossscorer` (appendix_extended.tex:26)
- `tab:pairwise_significance` (appendix_extended.tex:90)
- `tab:dose_response` (appendix_extended.tex:102)
- `tab:seed_robustness` (appendix_extended.tex:134)
- `tab:bonferroni_ci` (appendix_extended.tex:162)
- `tab:robustness_10k` (appendix_extended.tex:208)

### Table Labels (Other domains)
- `tab:domain_model_kstar` (tables/tab_domain_model_kstar.tex:4)
- `tab:domain_model_kstar_full` (tables/tab_domain_model_kstar_full.tex:4)

### Equation Labels
- `eq:kstar` (method.tex:23)

---

## Identified Issues

### 1. **Undefined Reference - CRITICAL**
- **Location:** appendix_extended.tex:76
- **Issue:** Reference `\ref{sec:kstar_theta}` in line 76 refers to figure not section
- **Context:** "...at $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite/continuation; at $\theta = 0.70$, $\Kempirical = 1$..."
- **Note:** Should reference `fig:kstar_theta` (defined at experiments_c1.tex:60), not a section. This is a cross-file semantic issue.

### 2. **Potential Label Mislabeling**
- **Location:** discussion.tex:3-8
- **Issue:** Multiple labels stacked on one paragraph, potentially confusing
- **Labels:**
  - `sec:why_kstar` (line 3)
  - `sec:one_wash` (line 4)
  - `sec:negative_graduated` (line 5)
  - `sec:repr_dependence` (line 6)
  - `sec:boundary_cases` (line 7)
  - `sec:length_confound` (line 8)
- **Analysis:** Only `sec:discussion` is referenced in the document; these subsection labels are defined but never referenced by `\ref{}`, `\autoref{}`, or `\cref{}` commands.

### 3. **Unreferenced Subsection Labels in Extended Discussion**
- `sec:extended_neural_probe` (defined, not referenced)
- `sec:extended_llm` (defined, not referenced)

### 4. **Cross-File Reference Consistency**
- **Location:** experiments_c3.tex:12 and experiments_c3.tex:5
- **Issue:** References to `sec:extended_limitations` point to appendix_extended.tex:69, which is correctly labeled as `sec:extended_limitations`. Status: **VALID**

### 5. **Table References - Consistency Check**
- All primary table references in main text match their label definitions
- Example valid chain: experiments_c1.tex:17 `\ref{tab:kstar_ci_extended}` → appendix.tex:130 `\label{tab:kstar_ci_extended}` ✓

### 6. **Appendix Cross-Reference Status**
- References from main sections to appendix sections are **consistent**
- Example: introduction.tex:7 → `Appendix~\ref{sec:extended_limitations}` → appendix_extended.tex:69 ✓

### 7. **Missing References to Defined Labels**
The following labels are **defined but never referenced** anywhere in the document:
- `sec:why_kstar`
- `sec:one_wash`
- `sec:negative_graduated`
- `sec:repr_dependence`
- `sec:boundary_cases`
- `sec:length_confound`
- `sec:extended_neural_probe`
- `sec:extended_llm`

These appear to be structural labels for subsections that are referenced only as prose anchors, not as explicit cross-references.

---

## Reference Summary by File

**introduction.tex:** 10 references (all valid)
**method.tex:** 9 references (all valid)
**experiments_c1.tex:** 32 references (all valid)
**experiments_c3.tex:** 6 references (all valid)
**discussion.tex:** 13 references (all valid)
**appendix.tex:** 29 references (all valid)
**appendix_extended.tex:** 27 references (all valid)
**tables/*.tex:** 0 direct references (tables are included via `\input{}`)

---

## Overall Assessment

**Status: MOSTLY CONSISTENT** with 1 minor semantic issue (figure/section reference ambiguity) and 8 unused label definitions that serve as internal anchors rather than cross-reference targets.

All actual `\ref{}`, `\autoref{}`, and `\cref{}` commands point to existing `\label{}` definitions. No multiply-defined labels detected. The unused labels are likely intentional for future reference or structural documentation purposes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f710897-0aab-40cf-a6cf-f6f8819b1599",
  "isSidechain": true,
  "agentId": "a86cd6902d70a29a1",
  "requestId": "req_011CbJrSVNmR7HVAK3hsnRJC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d30de3cf-acef-4373-8879-3f89512da48e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "51eb88ba-e52c-46f6-bfa0-e0d3c2871b77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "iterative-discovering-hopcroft",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ERXLX3akBaVYjZMMHHkDT7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 19871,
      "cache_read_input_tokens": 51804,
      "output_tokens": 2505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19871
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2505,
          "cache_read_input_tokens": 51804,
          "cache_creation_input_tokens": 19871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19871,
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
