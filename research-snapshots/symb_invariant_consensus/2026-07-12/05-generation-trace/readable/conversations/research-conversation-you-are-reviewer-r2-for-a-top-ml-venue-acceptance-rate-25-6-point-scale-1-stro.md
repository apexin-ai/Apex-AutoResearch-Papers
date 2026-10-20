# Research conversation: You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a95d9ee6fe55a339a.jsonl`
- **Structured JSON:** [`75ab72d15d9de0cf8264.json`](../../sessions/75/75ab72d15d9de0cf8264.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-17T15:59:44.580Z_

You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus areas: **novelty, significance, related work coverage, positioning, and writing quality**.

## Paper Summary

**Title:** "When Does Symbolic Consensus Help? A Systematic Empirical Study"

**Core claim:** The paper presents the first systematic empirical evaluation of symbolic consensus for LLM reasoning aggregation. They instantiate "SICA" (Symbolic Invariant Consensus Aggregation), which extracts FOL constraints from K reasoning traces and selects answers via weighted MAX-SAT. The main finding is negative: SICA provides no significant accuracy gain over standard majority voting (Self-Consistency) across 1,300+ problems, 5 model families, 3 reasoning domains. They identify a "capability trap" pattern and propose C0 as a binary diagnostic.

## Paper Structure and Content

**Abstract (~200 words):** States problem (symbolic consensus for LLM reasoning), method (SICA: FOL constraints + MAX-SAT), main finding (no significant gain, |Δ|≈1.5pp), constraint quality (precision 0.57 vs 0.33 random), mechanism equivalence (MAX-SAT ≈ counting), boundary condition (T=1.0: +8.3pp but degraded quality), and C0 diagnostic.

**Introduction (2 pages):**
- Opens with SC as standard practice, symbolic methods as recent extension
- Identifies gap: no systematic characterization of when symbolic consensus helps/hurts/degenerates
- Positions as controlled empirical study: 3 domains, 5 model families, varied operating conditions, 1,300+ problems
- Four contributions listed:
  1. First systematic evaluation → no significant gain in standard settings
  2. Capability trap characterization (C0=22-65%, precision 0.57, MAX-SAT ≈ counting)
  3. Boundary conditions: T=1.0 partially breaks trap but with costs
  4. C0 as zero-cost binary diagnostic

**Related Work (1 page, 4 subsections):**
- Self-Consistency and majority voting: Wang et al. 2023, Chen et al. 2023, Taubenfeld et al. 2024
- Symbolic reasoning for LLMs: Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)
- Process and outcome reward models: Cobbe et al. 2021, Lightman et al. 2024
- Negative results in NLP: Reynolds and McDonell 2021

**Method (1 page):** SICA pipeline in 5 stages: trace generation → answer extraction → constraint extraction → deduplication → MAX-SAT aggregation. Plus C0 metric definition.

**Experimental Setup (1 page):** 7 models, 4 domains, default K=12, T=0.7, McNemar's test + Bonferroni.

**Results (3 pages, 6 subsections):**
- 5.1 Main Results (Table 1: 9 model-domain configs)
- 5.2 Constraint Quality (Table 2: precision analysis)
- 5.3 Mechanism Ablation (Table 3: MAX-SAT vs simpler strategies)
- 5.4 Tiebreak Analysis (Table 4)
- 5.5 Boundary Conditions: Temperature (Table 5)
- 5.6 C0 as Operating Regime Indicator (Table 6)

**Discussion (1 page):** Capability trap as descriptive pattern, practical guidelines, T=1.0 exception, alternative directions (Logic-LM, weighted SC), limitations (5 items).

**Conclusion (0.5 page)**

**Appendices (A-G, 4 pages):** K sensitivity, overhead, weighted SC, Logic-LM, GSM8K pilot, case studies, C0 full data.

**References: Only 8 papers cited.**

## Key Claims to Evaluate for Novelty/Significance

1. "First systematic empirical evaluation of symbolic consensus" — is this actually novel?
2. The "capability trap" concept — is this a genuine contribution or a restatement of well-known issues?
3. C0 as a diagnostic — is a binary indicator that just separates reasoning vs instruction models a meaningful contribution?
4. Negative result study — is the community value sufficient for a top venue?

## Your Review Task

Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, be specific)
3. **Weaknesses** (bulleted, be specific — cite sections)
4. **Questions for Authors** (numbered)
5. **Minor Issues** (if any)
6. **Overall Assessment** (1-2 paragraphs)
7. **Score** (1-6) and **Confidence** (1-5, where 5=certain)

Focus on:
- Is the research question novel and significant?
- Does the "capability trap" concept add value beyond what's already known?
- Is C0 a genuine contribution or trivially equivalent to model-type classification?
- Is the related work coverage adequate? (Only 8 references — is this enough for a systematic empirical study?)
- Are there important related works missing?
- How does this compare to existing negative-result studies in the field?
- Is the writing clear, well-structured, and appropriate for the venue?
- Does the paper tell a compelling "story" or read more like an experiment log?
- Is the framing honest about the strength of claims?
- Would the community benefit from this work being published?


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "4c2cbe47-e5d8-4e50-a731-2891656d6396",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T15:59:44.583Z_

```json
{
  "parentUuid": "4c2cbe47-e5d8-4e50-a731-2891656d6396",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
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
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
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
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "1c5ad4e5-75bd-47d3-abb4-49ca37dc36cf",
  "timestamp": "2026-05-17T15:59:44.583Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T15:59:46.869Z_



I need to read the actual paper and supporting materials before writing my review. Let me start by exploring the project structure and reading the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c5ad4e5-75bd-47d3-abb4-49ca37dc36cf",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RFVaferGCV9a7o2PHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c08f40a5-01dd-4db8-8ba0-60c918733528",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJSNHV72dhX9nXNE5FHDxC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8459,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8459,
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

_source line 4 · 2026-05-17T15:59:48.991Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PfRMeinwsQ74jDULVkkHiC`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c08f40a5-01dd-4db8-8ba0-60c918733528",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RFVaferGCV9a7o2PHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbc083ac-5708-41d4-bf0f-18cb5b6ba0e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJSNHV72dhX9nXNE5FHDxC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8459,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8459,
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

_source line 5 · 2026-05-17T15:59:49.017Z_

<details><summary>↩ Tool result · `toolu_01PfRMeinwsQ74jDULVkkHiC`</summary>

```text
logs/chats/feishu_group_oc_970d5ea3f54df81296b97321fcded892_director.lock
study_status.lock
ROADMAP.lock
logs/chats/feishu_group_oc_319977a04ca60b6c4c69a2a8d4141a75_reviewer.lock
decisions.lock
logs/chats/feishu_group_oc_319977a04ca60b6c4c69a2a8d4141a75.lock
logs/workers/worker_code_core-pipeline_20260515T085018.log
logs/workers/worker_code_core-pipeline_20260515T085018_result.json
logs/workers/worker_infra_env-probe-setup_20260515T084922.log
logs/workers/worker_infra_env-probe-setup_20260515T084922_result.json
artifacts/crd_audit_report.md
logs/workers/worker_audit_crd-experiments_20260515T091419.log
logs/workers/worker_audit_crd-experiments_20260515T091419_result.json
logs/workers/worker_code_sica-verify-fix_20260515T091407.log
logs/workers/worker_code_sica-verify-fix_20260515T091407_result.json
artifacts/constraint_extractor.py
artifacts/trace_generator.py
artifacts/pipeline.py
artifacts/run_mvp.py
artifacts/prepare_proofwriter.py
registry.lock
checkpoints/crd_folio_main_PENDING_20260515T093542.json
checkpoints/crd_folio_main_QUEUED_20260515T093544.json
checkpoints/crd_folio_main_ALLOCATED_20260515T093546.json
checkpoints/crd_folio_main_RUNNING_20260515T093553.json
checkpoints/crd_folio_main_RUNNING_20260515T093558.json
checkpoints/crd_folio_main_DONE_20260515T093603.json
logs/workers/worker_code_p0-p1-p2-fixes_20260515T091706.log
logs/workers/worker_code_p0-p1-p2-fixes_20260515T091706_result.json
logs/workers/worker_code_fix-contradiction-metric_20260515T094127.log
logs/workers/worker_code_trace-optim-data_20260515T093902.log
logs/workers/worker_code_trace-optim-data_20260515T093902_result.json
logs/workers/worker_code_fix-contradiction-metric_20260515T094127_result.json
logs/workers/worker_code_math-equiv-fix_20260515T094849.log
logs/workers/worker_code_math-equiv-fix_20260515T094849_result.json
logs/workers/worker_infra_download-diagnose_20260515T093832.log
logs/workers/worker_infra_model-switch-qwq_20260515T085440.log
logs/workers/worker_infra_model-switch-qwq_20260515T085440_result.json
logs/workers/worker_infra_download-diagnose_20260515T093832_result.json
artifacts/run_full_mvp.py
artifacts/launch_mvp.sh
logs/workers/worker_code_mvp-launch-script_20260515T110631.log
logs/workers/worker_code_mvp-launch-script_20260515T110631_result.json
logs/workers/worker_exp_smoke-test-5q_20260515T100255.log
logs/workers/worker_exp_smoke-test-5q_20260515T100255_result.json
checkpoints/smoke-test-5q_PREPARING_20260515T112209.json
logs/workers/worker_code_fix-async-extraction_20260515T111651.log
logs/chats/worker_code_fix-async-extraction_20260515T111651.lock
logs/chats/worker_code_fix-async-extraction_20260515T111651.jsonl
logs/workers/worker_code_fix-async-extraction_20260515T111651_result.json
logs/workers/worker_code_proofwriter-prompt_20260515T110657.log
logs/workers/worker_code_proofwriter-prompt_20260515T110657_result.json
logs/workers/worker_infra_read-smoke-results_20260515T113651.log
logs/chats/worker_infra_read-smoke-results_20260515T113651.lock
logs/chats/worker_infra_read-smoke-results_20260515T113651.jsonl
logs/workers/worker_infra_read-smoke-results_20260515T113651_result.json
checkpoints/sica_smoke_5q_PENDING_20260515T113844.json
checkpoints/sica_smoke_5q_QUEUED_20260515T113847.json
checkpoints/sica_smoke_5q_ALLOCATED_20260515T113851.json
checkpoints/sica_smoke_5q_RUNNING_20260515T113858.json
checkpoints/sica_smoke_5q_RUNNING_20260515T113903.json
checkpoints/sica_smoke_5q_DONE_20260515T113907.json
logs/workers/worker_data_aime-2024_20260515T113732.log
logs/workers/worker_data_aime-2024_20260515T113732_result.json
logs/workers/worker_data_filter-image-problems_20260515T114219.log
logs/workers/worker_data_filter-image-problems_20260515T114219_result.json
logs/workers/worker_research_temp-diversity_20260515T111724.log
logs/workers/worker_exp_mvp-math50-restart_20260515T115404.log
logs/chats/worker_exp_mvp-math50-restart_20260515T115404.lock
logs/chats/worker_exp_mvp-math50-restart_20260515T115404.jsonl
logs/workers/worker_exp_mvp-math50-restart_20260515T115404_result.json
logs/workers/worker_research_temp-diversity_20260515T111724_result.json
checkpoints/sica_temp_diversity_PENDING_20260515T121434.json
checkpoints/sica_temp_diversity_QUEUED_20260515T121438.json
checkpoints/sica_temp_diversity_ALLOCATED_20260515T121442.json
checkpoints/sica_temp_diversity_RUNNING_20260515T121448.json
checkpoints/sica_temp_diversity_RUNNING_20260515T121453.json
checkpoints/sica_temp_diversity_DONE_20260515T121456.json
logs/workers/worker_infra_mvp-monitor_20260515T121350.log
checkpoints/mvp_math50_t07_PENDING_20260515T121629.json
checkpoints/mvp_math50_t07_QUEUED_20260515T121633.json
checkpoints/mvp_math50_t07_ALLOCATED_20260515T121639.json
logs/workers/worker_infra_mvp-monitor_20260515T121350_result.json
checkpoints/mvp_math50_t07_RUNNING_20260515T121646.json
logs/workers/worker_infra_cleanup-and-monitor_20260515T121723.log
logs/chats/worker_infra_cleanup-and-monitor_20260515T121723.lock
logs/chats/worker_infra_cleanup-and-monitor_20260515T121723.jsonl
logs/workers/worker_infra_cleanup-and-monitor_20260515T121723_result.json
logs/workers/worker_exp_mvp-math50_20260515T114040.log
checkpoints/mvp_math50_t07_RUNNING_20260515T122134.json
checkpoints/mvp_math50_t07_DONE_20260515T122137.json
artifacts/constraint_extractor_fixed.py
logs/workers/worker_code_fix-extraction-parse_20260515T122228.log
logs/workers/worker_code_fix-extraction-parse_20260515T122228_result.json
logs/workers/worker_code_fix-trace-batch_20260515T122210.log
logs/workers/worker_code_fix-trace-batch_20260515T122210_result.json
checkpoints/sica_aime30_t07_PREPARING_20260515T123816.json
checkpoints/sica_aime30_t07_QUEUED_20260515T130115.json
checkpoints/sica_aime30_t07_RUNNING_20260515T130120.json
logs/workers/worker_exp_aime30-launch_20260515T123853.log
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbc083ac-5708-41d4-bf0f-18cb5b6ba0e5",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "68500c7d-9c37-414f-ac36-1dc2a22f752a",
  "sourceToolAssistantUUID": "dbc083ac-5708-41d4-bf0f-18cb5b6ba0e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T15:59:49.758Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GkzaRQPvUQocEcGfCHXcRg`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68500c7d-9c37-414f-ac36-1dc2a22f752a",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RFVaferGCV9a7o2PHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a77b67e5-2147-47dc-a0b9-babb59c18d36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJSNHV72dhX9nXNE5FHDxC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8459,
      "cache_read_input_tokens": 8251,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 210,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 8459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8459,
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

_source line 7 · 2026-05-17T15:59:49.778Z_

<details><summary>↩ Tool result · `toolu_01GkzaRQPvUQocEcGfCHXcRg`</summary>

```text
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/best/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
artifacts/dream_reports/dream_20260516T124139/best/paper.tex
artifacts/dream_reports/dream_20260516T124139/median/paper.tex
artifacts/dream_reports/dream_20260516T124139/worst/paper.tex
artifacts/dream_reports/dream_20260516T155754/best/paper.tex
artifacts/dream_reports/dream_20260516T155754/median/paper.tex
artifacts/dream_reports/dream_20260516T155754/worst/paper.tex
artifacts/dream_reports/dream_20260517T144412/best/paper.tex
artifacts/dream_reports/dream_20260517T144412/median/paper.tex
artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a77b67e5-2147-47dc-a0b9-babb59c18d36",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "aaf0f1d6-0bbd-4248-9f4d-ffbb4540e9d4",
  "sourceToolAssistantUUID": "a77b67e5-2147-47dc-a0b9-babb59c18d36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-17T15:59:51.975Z_

Let me read the latest paper version and supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaf0f1d6-0bbd-4248-9f4d-ffbb4540e9d4",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RFsub7LaTLDWeqYbYA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d2f53e2-68f0-4beb-a574-a3ce5176f34c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnpaQJyAUXU86Rj1pnTB1c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3667,
      "cache_read_input_tokens": 16710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3667,
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

_source line 9 · 2026-05-17T15:59:53.894Z_

<details open><summary>🔧 Tool call — Read · `toolu_012YyPHtEpnc9phVdp8KohV7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d2f53e2-68f0-4beb-a574-a3ce5176f34c",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RFsub7LaTLDWeqYbYA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8921f647-a13d-4e63-840c-ff6d74eef498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnpaQJyAUXU86Rj1pnTB1c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3667,
      "cache_read_input_tokens": 16710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3667,
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

_source line 10 · 2026-05-17T15:59:54.194Z_

<details><summary>↩ Tool result · `toolu_012YyPHtEpnc9phVdp8KohV7`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{xcolor}
8	\usepackage{multirow}
9	\usepackage{hyperref}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{subcaption}
13	
14	\title{The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning}
15	
16	\author{Anonymous}
17	\date{}
18	
19	\begin{document}
20	\maketitle
21	
22	%% =============================================================
23	%% ABSTRACT
24	%% =============================================================
25	\begin{abstract}
26	Symbolic consensus methods augment Large Language Model (LLM) reasoning by extracting first-order logic (FOL) constraints from multiple reasoning traces and selecting answers via MAX-SAT optimization. We present the first systematic study asking \emph{when} such methods improve over simple majority voting (Self-Consistency, SC). Across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model (combined $N{>}1{,}300$ problems), we find that symbolic consensus provides no significant accuracy gain over SC. We identify the structural cause: a \textbf{capability trap}. Instruction-scale models produce abundant output diversity (candidate disagreement rate $C_0{=}38$--$65\%$), yet the extracted constraints achieve only random-level discriminative precision ($\approx 0.50$). MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, confirmed by an ablation showing MAX-SAT $\approx$ count-only $\approx$ random-weight (802/804 identical answers, McNemar $p{=}0.99$). A temperature ablation causally manipulates diversity from $C_0{=}28\%$ to $68\%$, with the accuracy gap remaining zero at every level ($|\Delta|{\leq}1.7$pp, all $p{>}0.30$). Full reasoning models avoid the trap only by eliminating diversity entirely ($C_0{<}5\%$), making symbolic methods structurally degenerate. We propose $C_0$ as a zero-cost early stopping criterion: if $C_0{<}5\%$, the method is degenerate; if $C_0{>}20\%$, the capability trap guarantees no gain.
27	\end{abstract}
28	
29	%% =============================================================
30	%% 1. INTRODUCTION
31	%% =============================================================
32	\section{Introduction}
33	
34	Self-Consistency (SC) aggregates multiple LLM reasoning traces by majority voting over extracted answers. Recent work proposes replacing this simple aggregation with symbolic methods: extracting formal constraints from each trace and using satisfiability solvers to select the maximally consistent answer. The intuition is compelling. When traces disagree, a solver that reasons about logical structure should outperform naive counting. But does it?
35	
36	This question has practical urgency. Symbolic consensus adds computational overhead (we measure 49\% wall-time increase) and engineering complexity. Practitioners need guidance on when this investment pays off. Prior work evaluates symbolic reasoning pipelines on individual benchmarks without systematically characterizing the conditions under which they provide gains over majority voting.
37	
38	We instantiate symbolic consensus as SICA (Symbolic Invariant Consensus Aggregation): extract FOL constraints from each trace, formulate a weighted MAX-SAT problem, and select the answer whose traces maximize total satisfied constraint weight. We evaluate SICA across 3 reasoning domains (formal logic, commonsense, science), 4 instruction-scale model families (Qwen, LLaMA, Mistral, DeepSeek-R1-Distill), and 1 full reasoning model (QwQ-32B), totaling over 1,300 problem instances across powered experiments.
39	
40	Our central finding is negative: SICA provides no significant accuracy gain over SC in any tested condition. The largest positive signal ($+6.67$pp with LLaMA-8B, $n{=}60$) does not survive powered replication ($n{=}200$: $\Delta{=}+2.0$pp, $p{=}0.42$). Five model families show $|\Delta|{\leq}6.67$pp with zero significant results. We identify the structural cause, which we term the \textbf{capability trap}: symbolic consensus requires both output diversity (disagreement to resolve) and discriminative constraints (to resolve correctly), but no model simultaneously satisfies both requirements.
41	
42	We make three contributions:
43	\begin{enumerate}
44	\item \textbf{Mechanism identification.} We show that LLM-extracted constraints achieve random-level precision ($0.505 \pm 0.148$, $n{=}307$ problems) regardless of diversity level (regression slope $= 0.003$, $r^2 < 0.01$). MAX-SAT optimization thus degenerates to counting, confirmed by the ablation MAX-SAT $\approx$ count-only $\approx$ random-weight.
45	\item \textbf{First systematic negative result.} Five model families (combined $N{>}1{,}300$) all show SICA $\approx$ SC. A temperature ablation causally confirms the trap is structural, not a tuning failure.
46	\item \textbf{Zero-cost diagnostic.} We propose $C_0$ (candidate disagreement rate) as a practitioner-facing early stopping criterion that requires no additional compute beyond standard SC.
47	\end{enumerate}
48	
49	%% =============================================================
50	%% 2. RELATED WORK
51	%% =============================================================
52	\section{Related Work}
53	
54	\paragraph{Self-Consistency and voting methods.}
55	\citet{wang2023selfconsistency} introduced SC as a decoding strategy that samples diverse reasoning paths and marginalizes over answers. Universal SC \citep{chen2023universal} extends this to free-form generation by clustering. Weighted SC variants \citep{taubenfeld2024} assign trace-level confidence scores before voting. We compare against multiple weighting schemes (inverse-length, length-based, constraint-count) and find all equivalent to uniform voting when the underlying signals lack discriminative power.
56	
57	\paragraph{Symbolic reasoning augmentation.}
58	Logic-LM \citep{pan2023logiclm} translates NL problems to symbolic form for solver verification. LINC \citep{olausson2023linc} uses FOL translation with theorem provers. These methods apply symbolic verification to single traces. SICA extends the paradigm to multi-trace aggregation: rather than verifying one trace, it extracts constraints from all $K$ traces and selects the answer maximizing joint satisfiability. We show that multi-trace symbolic aggregation faces the same bottleneck as single-trace verification: constraint quality is the binding limitation.
59	
60	\paragraph{Outcome and process reward models.}
61	ORM \citep{cobbe2021gsm8k} and PRM \citep{lightman2023lets} train verifiers to score reasoning steps. These learned methods require training data for each domain. Symbolic consensus promises domain-general verification through logical structure. Our results suggest this promise is unfulfilled: logical structure extracted by current LLMs does not carry discriminative information.
62	
63	\paragraph{Negative results in NLP.}
64	Systematic negative results provide essential calibration for research directions \citep{rogers2020primer}. Our work follows this tradition by characterizing structural limitations rather than merely reporting null effects.
65	
66	%% =============================================================
67	%% 3. METHOD
68	%% =============================================================
69	\section{Method: SICA Pipeline}
70	
71	\subsection{Overview}
72	
73	Given a problem $q$ and $K$ sampled reasoning traces $\{t_1, \ldots, t_K\}$, SICA proceeds in four stages:
74	
75	\begin{enumerate}
76	\item \textbf{Trace Generation.} Sample $K$ traces from an LLM at temperature $T$ (default $T{=}0.7$, $K{=}12$). Extract the final answer from each trace.
77	\item \textbf{Constraint Extraction.} For each trace $t_i$, prompt the LLM to extract FOL constraints $\mathcal{C}_i = \{c_{i,1}, \ldots, c_{i,m_i}\}$ that formalize the reasoning steps.
78	\item \textbf{MAX-SAT Formulation.} Construct a weighted MAX-SAT instance: for each candidate answer $a \in \mathcal{A}(q)$, compute the total weight of constraints satisfiable under $a$. Select $a^* = \arg\max_{a} \sum_{i: \text{ans}(t_i)=a} \sum_j w(c_{i,j}) \cdot \mathbf{1}[\text{SAT}(c_{i,j} | a)]$.
79	\item \textbf{Answer Selection.} Return $a^*$. Ties broken by MAX-SAT weight (vs. random in SC).
80	\end{enumerate}
81	
82	\subsection{Key Metrics}
83	
84	\textbf{Candidate disagreement rate ($C_0$):} The fraction of problems where $K$ traces produce more than one distinct answer. $C_0 = |\{q : |\mathcal{A}(q)| > 1\}| / N$.
85	
86	\textbf{Constraint precision:} For a problem $q$ with correct answer $a^*$, the fraction of extracted constraints that are satisfied by $a^*$ but not by incorrect candidates. Precision $\approx 0.50$ indicates random-level discrimination.
87	
88	\textbf{Discordant pairs:} Problems where SICA and SC select different answers. The net accuracy difference is determined entirely by these pairs.
89	
90	%% =============================================================
91	%% 4. EXPERIMENTS
92	%% =============================================================
93	\section{Experiments}
94	
95	\subsection{Setup}
96	
97	\paragraph{Datasets.} FOLIO (formal deductive logic, 3-way classification), ProofWriter (formal logic, binary), StrategyQA (commonsense reasoning, binary), ARC-Challenge (science, 4-way multiple choice), GSM8K (mathematical reasoning, open-ended).
98	
99	\paragraph{Models.} Instruction-scale: Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-72B-Instruct-AWQ, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B. Full reasoning: QwQ-32B. Default: $K{=}12$, $T{=}0.7$.
100	
101	\paragraph{Evaluation.} McNemar's test for paired accuracy comparison. Bootstrap $p$-values where noted. All reported $p$-values are two-sided.
102	
103	%% --- T1: MAIN RESULTS ---
104	\subsection{Main Results}
105	\label{sec:main-results}
106	
107	Table~\ref{tab:main} presents SICA vs. SC accuracy across all tested conditions. No condition achieves a statistically significant gain.
108	
109	\begin{table}[t]
110	\centering
111	\small
112	\caption{Main results: SICA vs. SC accuracy across models and domains. $C_0$: candidate disagreement rate. $\Delta$: SICA $-$ SC in percentage points. No result is statistically significant ($p > 0.10$ for all).}
113	\label{tab:main}
114	\begin{tabular}{llcccccc}
115	\toprule
116	\textbf{Model} & \textbf{Domain} & \textbf{$n$} & \textbf{$C_0$} & \textbf{SC} & \textbf{SICA} & \textbf{$\Delta$pp} & \textbf{$p$} \\
117	\midrule
118	Qwen-14B & FOLIO+PW & 804 & 53\% & 76.2 & 76.5 & +0.25 & 0.74 \\
119	Qwen-14B & StrategyQA & 60 & 10\% & 53.3 & 56.7 & +3.33 & $>$0.30 \\
120	Qwen-14B & ARC-Chall. & 60 & 5\% & 96.7 & 95.0 & $-$1.67 & -- \\
121	Qwen-14B & GSM8K & 30 & 10\% & 86.7 & 86.7 & 0.0 & -- \\
122	\midrule
123	Qwen-7B & FOLIO+PW & 60 & 65\% & 55.0 & 53.3 & $-$1.7 & 0.65 \\
124	Qwen-72B & FOLIO+PW & 60 & 15\% & 86.7 & 86.7 & 0.0 & 1.00 \\
125	\midrule
126	LLaMA-8B & FOLIO+PW & 60 & 62\% & 60.0 & 66.7 & +6.67 & 0.22 \\
127	DeepSeek-R1-7B & FOLIO+PW & 60 & 58\% & 71.7 & 68.3 & $-$3.33 & 0.48 \\
128	\midrule
129	QwQ-32B & Mixed & 46 & 2.6\% & -- & -- & $\approx$0 & -- \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	The largest positive delta ($+6.67$pp, LLaMA-8B, $n{=}60$) is a small-sample artifact: the same model on StrategyQA ($n{=}200$) yields $\Delta{=}+2.0$pp ($p{=}0.42$) and on FOLIO ($n{=}204$) yields $\Delta{=}-2.4$pp. Positive and negative deltas alternate across domains within the same model, consistent with sampling noise around a true effect of zero.
135	
136	QwQ-32B produces near-zero diversity ($C_0{=}2.6\%$ effective), making SICA structurally degenerate: with almost all traces agreeing, there is nothing for the solver to resolve. DeepSeek-R1-Distill-7B, despite reasoning-style training, behaves as an instruction-scale model ($C_0{=}58\%$) due to insufficient parameter capacity to maintain deterministic reasoning chains.
137	
138	\paragraph{Within-Qwen scaling.} The Qwen family provides three distinct $C_0$ levels: 7B ($C_0{=}65\%$, SC $= 55.0\%$), 14B ($C_0{=}53\%$, SC $= 76.2\%$), 72B ($C_0{=}15\%$, SC $= 86.7\%$). $C_0$ decreases monotonically with scale as stronger models converge to correct answers. Yet SICA$-$SC $\approx 0$ at all three scales, confirming the trap holds regardless of where a model sits on the capability spectrum.
139	
140	%% --- MECHANISM ANALYSIS ---
141	\subsection{Mechanism Analysis: Why the Trap Exists}
142	\label{sec:mechanism}
143	
144	\subsubsection{Constraint Precision is Random-Level}
145	
146	We analyze constraint quality at per-problem granularity across 307 multi-candidate problems from the Qwen-14B powered experiment ($n{=}804$). Table~\ref{tab:constraint-quality} and Figure~\ref{fig:f2-description} present the results.
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Constraint precision statistics ($n{=}307$ multi-candidate problems). Precision $\approx 0.50$ indicates constraints cannot distinguish correct from incorrect answers.}
152	\label{tab:constraint-quality}
153	\begin{tabular}{lc}
154	\toprule
155	\textbf{Metric} & \textbf{Value} \\
156	\midrule
157	Mean precision & $0.505 \pm 0.148$ \\
158	Median precision & 0.500 \\
159	Precision vs. vote entropy: slope & 0.003 \\
160	Precision vs. vote entropy: $r^2$ & 0.002 \\
161	Precision vs. vote entropy: $p$ & 0.42 \\
162	\midrule
163	FOLIO precision & 0.512 \\
164	ProofWriter precision & 0.498 \\
165	Cross-domain difference $p$ & 0.60 \\
166	\midrule
167	Fraction precision $< 0.40$ & 28\% \\
168	Fraction precision $> 0.60$ & 25\% \\
169	\bottomrule
170	\end{tabular}
171	\end{table}
172	
173	\paragraph{F2: Per-problem scatter (hero figure).} Each of 307 multi-candidate problems is plotted with vote entropy on the $x$-axis and constraint precision on the $y$-axis. The regression line is flat (slope $= 0.003$, $r^2 < 0.01$): regardless of how much the traces disagree, the extracted constraints achieve only chance-level discrimination. The symmetric distribution around 0.50 (28\% below 0.40, 25\% above 0.60) confirms that occasional high-precision problems are balanced by equally many reverse-discriminating problems.
174	
175	The cross-domain consistency (FOLIO $= 0.512$, ProofWriter $= 0.498$, difference $p{=}0.60$) indicates this is not a domain-specific failure but a structural limitation of LLM-based constraint extraction.
176	
177	\subsubsection{MAX-SAT Adds No Value Over Counting}
178	
179	Table~\ref{tab:ablation} presents the constraint ablation on the full 804-problem dataset. Four aggregation strategies produce nearly identical accuracy:
180	
181	\begin{table}[t]
182	\centering
183	\small
184	\caption{Constraint ablation ($n{=}804$). All methods produce statistically identical results, confirming MAX-SAT optimization is vacuous when constraints lack discriminative power.}
185	\label{tab:ablation}
186	\begin{tabular}{lcc}
187	\toprule
188	\textbf{Method} & \textbf{Accuracy} & \textbf{vs. SC $p$} \\
189	\midrule
190	SC (majority vote) & 76.24\% & -- \\
191	SICA (MAX-SAT) & 76.49\% & 0.74 \\
192	Count-only (no solver) & 76.62\% & 0.74 \\
193	Random-weight & 76.37\% & 0.85 \\
194	\bottomrule
195	\end{tabular}
196	\vspace{0.3em}
197	\footnotesize{MAX-SAT vs. count-only: McNemar $p = 0.99$. Agreement: 802/804 problems.}
198	\end{table}
199	
200	MAX-SAT and count-only agree on 802 of 804 problems. The 2 disagreements cancel out. Random-weight (assigning uniformly random weights to constraints) also matches MAX-SAT ($p{=}0.85$). This confirms that the satisfiability structure of extracted constraints carries no information: the solver's optimization reduces to counting votes, which is exactly what SC already does.
201	
202	Together with the per-problem precision analysis, these results establish the mechanism of the capability trap: (1) constraints do not discriminate correct from incorrect answers, therefore (2) any solver operating over them degenerates to noise.
203	
204	%% --- TIEBREAK ---
205	\subsection{Tiebreak Analysis}
206	\label{sec:tiebreak}
207	
208	A potential alternative explanation is that SICA provides value as a principled tiebreaker for cases where SC votes are tied. Table~\ref{tab:tiebreak} evaluates this hypothesis.
209	
210	\begin{table}[t]
211	\centering
212	\small
213	\caption{Tiebreak accuracy on the 10 tied problems (of 60 total, $K{=}12$, Qwen-14B). SICA is a better tiebreaker than alternatives, but ties are too rare to affect overall accuracy.}
214	\label{tab:tiebreak}
215	\begin{tabular}{lc}
216	\toprule
217	\textbf{Tiebreak Method} & \textbf{Accuracy on Tied} \\
218	\midrule
219	SICA (MAX-SAT) & 80\% \\
220	Random & 50\% \\
221	Alphabetical & 60\% \\
222	First-seen & 40\% \\
223	\bottomrule
224	\end{tabular}
225	\vspace{0.3em}
226	\footnotesize{Tied problems: 10/60 = 16.7\%. Net gain on full 60: $+$0.5pp (within noise).}
227	\end{table}
228	
229	SICA achieves 80\% accuracy on tied questions vs. 50\% for random tiebreaking. However, ties occur in only 16.7\% of problems at $K{=}12$. The net contribution to overall accuracy is $0.80 \times 0.167 - 0.50 \times 0.167 = +0.5$pp, invisible against the SE of $\approx$6pp. At odd $K$ (e.g., $K{=}11$), ties are eliminated entirely, and SICA collapses to SC exactly (Section~\ref{sec:k-ablation}). The tiebreaking mechanism, while locally effective, is structurally too rare to justify the 49\% overhead.
230	
231	%% --- K ABLATION ---
232	\subsection{K Sensitivity}
233	\label{sec:k-ablation}
234	
235	\begin{table}[t]
236	\centering
237	\small
238	\caption{$K$ ablation (Qwen-14B, $n{=}60$). SICA $\leq$ SC at all $K$. At odd $K{=}11$, ties vanish and $\Delta = 0$ exactly.}
239	\label{tab:k-ablation}
240	\begin{tabular}{cccc}
241	\toprule
242	$K$ & SC & SICA & $\Delta$pp \\
243	\midrule
244	6 & 73.3 & 73.3 & 0.0 \\
245	8 & 75.0 & 73.3 & $-$1.7 \\
246	11 & 73.3 & 73.3 & 0.0 \\
247	12 & 75.0 & 70.0 & $-$5.0 \\
248	16 & 75.0 & 71.7 & $-$3.3 \\
249	20 & 73.3 & 70.0 & $-$3.3 \\
250	\bottomrule
251	\end{tabular}
252	\vspace{0.3em}
253	\footnotesize{All McNemar $p > 0.20$. Larger $K$ degrades SICA due to noise accumulation.}
254	\end{table}
255	
256	The $K{=}11$ result is diagnostic: odd $K$ eliminates SC ties, removing SICA's only effective mechanism. The resulting $\Delta{=}0$ confirms SICA functions as nothing more than a tiebreaker. At larger even $K$ (16, 20), SICA performance degrades: more traces generate more non-discriminative constraints, increasing the probability that MAX-SAT excludes the correct answer.
257	
258	%% =============================================================
259	%% 5. TEMPERATURE ABLATION
260	%% =============================================================
261	\section{Temperature Ablation: Causal Evidence}
262	\label{sec:temperature}
263	
264	A natural objection is that perhaps the right diversity level has not been found. We address this by experimentally manipulating diversity through temperature, holding model and data constant.
265	
266	\begin{table}[t]
267	\centering
268	\small
269	\caption{Temperature ablation (Qwen-14B, FOLIO+ProofWriter, $n{=}60$, $K{=}12$). Diversity ($C_0$) is continuously controllable via temperature, but the SICA$-$SC gap remains zero at all levels.}
270	\label{tab:temperature}
271	\begin{tabular}{ccccccc}
272	\toprule
273	$T$ & $C_0$ & SC & SICA & $\Delta$pp & Discordant & $p$ \\
274	\midrule
275	0.3 & 28.3\% & 76.7 & 76.7 & 0.0 & 1:1 & 1.00 \\
276	0.5 & 41.7\% & 75.0 & 75.0 & 0.0 & 1:1 & 1.00 \\
277	0.7 & 53.3\% & 73.3 & 73.3 & 0.0 & -- & -- \\
278	1.0 & 68.3\% & 70.0 & 68.3 & $-$1.7 & 1:2 & 0.56 \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	$C_0$ increases monotonically from 28.3\% to 68.3\% as temperature rises from 0.3 to 1.0. This confirms that diversity is continuously controllable. SC accuracy decreases at high temperature (noisier traces corrupt the majority), a known property. The critical observation: $|\Delta| \leq 1.7$pp with all $p > 0.30$ across the full range. The capability trap is not a failure to find the right operating point; it is structural.
284	
285	At $T{=}0.3$ ($C_0{=}28\%$), few problems have multiple candidates, limiting SICA's scope. At $T{=}1.0$ ($C_0{=}68\%$), many problems are multi-candidate but noisier traces degrade constraint quality (extraction rate drops from 91\% to 87\%). The trap tightens from both ends: low temperature gives too few problems to operate on; high temperature degrades the signals SICA needs.
286	
287	%% =============================================================
288	%% 6. ADDITIONAL ANALYSES
289	%% =============================================================
290	\section{Analysis and Discussion}
291	
292	\subsection{$C_0$ as Diagnostic Predictor}
293	\label{sec:c0-diagnostic}
294	
295	Figure~\ref{fig:f4-description} plots $C_0$ against SICA$-$SC gap across all 14 experimental conditions. The pattern is flat: regression slope $= -0.02$, $r^2 = 0.06$, $p = 0.40$.
296	
297	\paragraph{F4: $C_0$ vs. Gap scatter.} Conditions cluster into two regimes with identical outcomes: (1) $C_0 < 5\%$ (QwQ-32B, ARC-14B): method is structurally degenerate, $|\Delta| < 1$pp. (2) $C_0 > 20\%$ (8 conditions across 4 model families): capability trap guarantees no gain, mean $|\Delta| = 0.1$pp, all $p > 0.10$. No condition achieves both sufficient diversity and discriminative constraints.
298	
299	$C_0$ is therefore a zero-cost early stopping criterion. If $C_0 < 5\%$ (model too strong or deterministic), the method degenerates to SC. If $C_0 > 20\%$ (instruction-scale regime), the capability trap applies. In either case, practitioners should not invest in symbolic consensus.
300	
301	Within the Qwen family, three distinct $C_0$ levels (7B: 65\%, 14B: 53\%, 72B: 15\%) span the range, with all yielding $\Delta \approx 0$. Combined with DeepSeek-R1-7B (58\%) and LLaMA-8B (62\%), five distinct $C_0$ levels are represented.
302	
303	\subsection{Comparison with Existing Methods}
304	
305	\paragraph{Logic-LM $\times$ K baseline.} We adapt Logic-LM to the multi-trace setting: each trace is independently verified (FOL extraction, solver check), then results are majority-voted. On FOLIO ($n{=}204$, $K{=}12$): Logic-LM$\times$K accuracy $= 78.9\%$, SC $= 79.4\%$, SICA $= 79.4\%$. Logic-LM$\times$K vs. SC: $\Delta = -0.5$pp, $p = 0.82$. Verification pass rate is 92\%: the solver passes almost all traces regardless of correctness, confirming the bottleneck is constraint quality, not aggregation architecture.
306	
307	\paragraph{Weighted SC baselines.} On the full 804-problem dataset, four weighting schemes yield statistically identical results:
308	\begin{center}
309	\small
310	\begin{tabular}{lcc}
311	\toprule
312	Method & Accuracy & vs. SC $p$ \\
313	\midrule
314	SC (uniform) & 76.24\% & -- \\
315	Inverse-length & 76.74\% & 0.45 \\
316	Length-weighted & 75.25\% & 0.15 \\
317	Constraint-count & 75.25\% & 0.15 \\
318	SICA (MAX-SAT) & 76.49\% & 0.74 \\
319	\bottomrule
320	\end{tabular}
321	\end{center}
322	No simple weighting rescues the method. The failure is in signal quality, not aggregation sophistication.
323	
324	\subsection{Overhead Analysis}
325	
326	Wall-time breakdown on the 804-problem experiment (Qwen-14B):
327	\begin{center}
328	\small
329	\begin{tabular}{lcc}
330	\toprule
331	Stage & Mean time (s) & \% total \\
332	\midrule
333	Trace generation & 31.6 & 51.3\% \\
334	Constraint extraction & 29.0 & 47.0\% \\
335	Deduplication & 1.0 & 1.6\% \\
336	MAX-SAT solver & 0.003 & $<$0.01\% \\
337	\midrule
338	Total & 61.6 & 100\% \\
339	\bottomrule
340	\end{tabular}
341	\end{center}
342	
343	SICA adds 49\% overhead vs. SC (the constraint extraction pass). The solver itself is negligible ($<$0.01\%). This overhead buys zero accuracy gain, making SC strictly Pareto-dominant: equal accuracy at half the cost. Even if future work improves constraint quality, the extraction cost (an additional LLM inference pass per trace) remains substantial.
344	
345	\subsection{Qualitative Analysis: Why Constraints Fail}
346	\label{sec:case-studies}
347	
348	Analysis of 8 representative problems reveals the structural cause. Extracted constraints primarily formalize problem premises (input conditions) rather than reasoning steps. Since both correct and incorrect traces read the same premises, 78\% of constraints are shared between traces leading to different answers. Only 12\% of constraints are truly discriminative (appear exclusively in correct or incorrect traces), and these split evenly in direction.
349	
350	The pattern is consistent: an LLM extracting ``if-then,'' ``forall,'' and ``exists'' patterns from a reasoning trace captures what the model \emph{read} (the problem statement), not how it \emph{reasoned} (the inference chain). Reasoning errors occur deeper in the chain where formalization either fails or produces surface-similar but semantically distinct constraints.
351	
352	%% =============================================================
353	%% 7. CONCLUSION
354	%% =============================================================
355	\section{Conclusion}
356	
357	We present the first systematic characterization of when symbolic consensus methods can improve LLM reasoning. The answer, across 3 domains and 5 model families, is: they cannot, due to a structural capability trap. The method requires diversity (to have something to resolve) and discriminative constraints (to resolve correctly). Instruction-scale models provide diversity but not discriminative constraints; full reasoning models eliminate diversity entirely. No tested model simultaneously satisfies both requirements.
358	
359	Three practical implications follow. First, practitioners considering symbolic aggregation should compute $C_0$ as a zero-cost diagnostic: the method is either degenerate ($C_0 < 5\%$) or trapped ($C_0 > 20\%$). Second, the bottleneck for future work is constraint quality, not aggregation sophistication: MAX-SAT, count-only, random-weight, and multiple weighted-SC variants all produce identical results. Third, the 49\% overhead for zero gain makes simple majority voting strictly preferable.
360	
361	The capability trap may not be permanent. Advances in neuro-symbolic extraction that capture inference structure rather than surface form could break the trap. Our contribution is establishing that the trap exists, characterizing its mechanism, and providing the diagnostic tools to detect when future methods escape it.
362	
363	%% =============================================================
364	%% REFERENCES (placeholder)
365	%% =============================================================
366	\bibliographystyle{plainnat}
367	
368	\begin{thebibliography}{20}
369	
370	\bibitem[Chen et al.(2023)]{chen2023universal}
371	Chen, X., et al. (2023). Universal Self-Consistency for Large Language Model Generation. \textit{arXiv:2311.17311}.
372	
373	\bibitem[Cobbe et al.(2021)]{cobbe2021gsm8k}
374	Cobbe, K., et al. (2021). Training Verifiers to Solve Math Word Problems. \textit{arXiv:2110.14168}.
375	
376	\bibitem[Lightman et al.(2023)]{lightman2023lets}
377	Lightman, H., et al. (2023). Let's Verify Step by Step. \textit{arXiv:2305.20050}.
378	
379	\bibitem[Olausson et al.(2023)]{olausson2023linc}
380	Olausson, T., et al. (2023). LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers. \textit{EMNLP 2023}.
381	
382	\bibitem[Pan et al.(2023)]{pan2023logiclm}
383	Pan, L., et al. (2023). Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning. \textit{EMNLP 2023 Findings}.
384	
385	\bibitem[Rogers et al.(2020)]{rogers2020primer}
386	Rogers, A., et al. (2020). A Primer in BERTology: What We Know About How BERT Works. \textit{TACL}.
387	
388	\bibitem[Taubenfeld et al.(2024)]{taubenfeld2024}
389	Taubenfeld, A., et al. (2024). Systematic Biases in LLM Simulations of Debates. \textit{arXiv:2402.04049}.
390	
391	\bibitem[Wang et al.(2023)]{wang2023selfconsistency}
392	Wang, X., et al. (2023). Self-Consistency Improves Chain of Thought Reasoning in Language Models. \textit{ICLR 2023}.
393	
394	\end{thebibliography}
395	
396	%% =============================================================
397	%% APPENDIX
398	%% =============================================================
399	\appendix
400	\section{Extended Results}
401	
402	\subsection{QwQ-32B Operating Regime}
403	
404	QwQ-32B as a full reasoning model produces near-deterministic outputs. Across 46 problems: nominal $C_0 = 10.3\%$ (format noise), effective $C_0 = 2.6\%$ (true reasoning divergence). On AIME ($n{=}22$): $\Delta = 0.0$pp. On ProofWriter ($n{=}17$): $\Delta = -5.9$pp (noise at SE $\approx 12$pp). The diversity ratio between QwQ-32B and Qwen-14B is $17.7\times$, confirming that full chain-of-thought reasoning eliminates the sampling diversity that symbolic consensus requires.
405	
406	\subsection{Qwen Within-Family Scaling}
407	
408	\begin{table}[h]
409	\centering
410	\small
411	\caption{Within-Qwen scaling on FOLIO+ProofWriter ($n{=}60$ each, $K{=}12$).}
412	\label{tab:qwen-scaling}
413	\begin{tabular}{lccccc}
414	\toprule
415	\textbf{Model} & $C_0$ & SC & SICA & $\Delta$pp & Extr. Rate \\
416	\midrule
417	Qwen-7B & 65\% & 55.0 & 53.3 & $-$1.7 & 82\% \\
418	Qwen-14B & 53\% & 76.2 & 76.5 & +0.25 & 89\% \\
419	Qwen-72B & 15\% & 86.7 & 86.7 & 0.0 & 93\% \\
420	\bottomrule
421	\end{tabular}
422	\end{table}
423	
424	Model scale produces three effects: (1) SC accuracy increases, (2) $C_0$ decreases (stronger models agree more), (3) extraction quality improves (fewer contradictions, higher extraction rate). Yet SICA$-$SC $\approx 0$ at all scales: the trap holds from weak to strong.
425	
426	\subsection{GSM8K Cross-Domain Pilot}
427	
428	Qwen-14B on GSM8K ($n{=}30$, $K{=}12$): SC $= 86.7\%$, SICA $= 86.7\%$, $\Delta = 0.0$pp. $C_0 \approx 10\%$, extraction rate $= 75\%$ (numerical computation is difficult to formalize in FOL). Zero discordant pairs. The model is sufficiently capable that traces converge to the correct numerical answer.
429	
430	\subsection{Overhead Percentiles}
431	
432	Median overhead: 48.9\%. P90 overhead: 57.6\% (longer FOLIO traces require more extraction time). Trace generation dominates at 51.3\% of total wall time; constraint extraction at 47.0\%.
433	
434	\end{document}
435	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8921f647-a13d-4e63-840c-ff6d74eef498",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "dd9d1814-3ec5-4151-a2d2-df731dc7e261",
  "sourceToolAssistantUUID": "8921f647-a13d-4e63-840c-ff6d74eef498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T15:59:54.818Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YMDPunx7SRjpzuBWFQA56v`</summary>

```json
{
  "pattern": "artifacts/dream_reports/dream_20260517T144412/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd9d1814-3ec5-4151-a2d2-df731dc7e261",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RFsub7LaTLDWeqYbYA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7d9aebb-5447-4f4c-a39e-b8f358478cda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnpaQJyAUXU86Rj1pnTB1c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3667,
      "cache_read_input_tokens": 16710,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3667
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 16710,
          "cache_creation_input_tokens": 3667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3667,
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

_source line 12 · 2026-05-17T15:59:54.909Z_

<details><summary>↩ Tool result · `toolu_01YMDPunx7SRjpzuBWFQA56v`</summary>

```text
artifacts/dream_reports/dream_20260517T144412/logs/orchestrator.log
artifacts/dream_reports/dream_20260517T144412/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260517T144412/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260517T144412/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260517T144412/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260517T144412/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260517T144412/best/experiment_data.json
artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md
artifacts/dream_reports/dream_20260517T144412/best/paper.tex
artifacts/dream_reports/dream_20260517T144412/best/paper.aux
artifacts/dream_reports/dream_20260517T144412/best/paper.out
artifacts/dream_reports/dream_20260517T144412/best/paper.pdf
artifacts/dream_reports/dream_20260517T144412/best/paper.log
artifacts/dream_reports/dream_20260517T144412/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260517T144412/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260517T144412/median/experiment_data.json
artifacts/dream_reports/dream_20260517T144412/median/paper_framing.md
artifacts/dream_reports/dream_20260517T144412/median/paper.tex
artifacts/dream_reports/dream_20260517T144412/median/paper.aux
artifacts/dream_reports/dream_20260517T144412/median/paper.out
artifacts/dream_reports/dream_20260517T144412/median/paper.pdf
artifacts/dream_reports/dream_20260517T144412/median/paper.log
artifacts/dream_reports/dream_20260517T144412/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260517T144412/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260517T144412/worst/experiment_data.json
artifacts/dream_reports/dream_20260517T144412/worst/paper_framing.md
artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
artifacts/dream_reports/dream_20260517T144412/worst/paper.aux
artifacts/dream_reports/dream_20260517T144412/worst/paper.out
artifacts/dream_reports/dream_20260517T144412/worst/paper.pdf
artifacts/dream_reports/dream_20260517T144412/worst/paper.log
artifacts/dream_reports/dream_20260517T144412/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260517T144412/best/review_context.yaml
artifacts/dream_reports/dream_20260517T144412/best/review_report.md
artifacts/dream_reports/dream_20260517T144412/logs/review_best.log
artifacts/dream_reports/dream_20260517T144412/median/review_context.yaml
artifacts/dream_reports/dream_20260517T144412/median/review_report.md
artifacts/dream_reports/dream_20260517T144412/logs/review_median.log
artifacts/dream_reports/dream_20260517T144412/worst/review_context.yaml
artifacts/dream_reports/dream_20260517T144412/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7d9aebb-5447-4f4c-a39e-b8f358478cda",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "9a3f8ef0-98f4-4493-9ec2-b844aa37b8b2",
  "sourceToolAssistantUUID": "e7d9aebb-5447-4f4c-a39e-b8f358478cda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-17T15:59:58.462Z_

Let me also read the supporting materials to understand the experimental context better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a3f8ef0-98f4-4493-9ec2-b844aa37b8b2",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RGFkVbmtW4kaEYq2UC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f406f71-ff58-47fd-a15a-aeda1225303b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms4GPENQtqU1dDho31hoUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11528,
      "cache_read_input_tokens": 20377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11528,
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

_source line 14 · 2026-05-17T16:00:00.357Z_

<details open><summary>🔧 Tool call — Read · `toolu_013tcAdHuFWMTvfGNKM8fmZE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f406f71-ff58-47fd-a15a-aeda1225303b",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RGFkVbmtW4kaEYq2UC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3a757e3-1d3b-42e0-810f-7bb22f55e50f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms4GPENQtqU1dDho31hoUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11528,
      "cache_read_input_tokens": 20377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11528,
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

_source line 15 · 2026-05-17T16:00:00.363Z_

<details><summary>↩ Tool result · `toolu_013tcAdHuFWMTvfGNKM8fmZE`</summary>

```text
1	# Paper Framing — symb_invariant_consensus
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25)
5	- Deadline: May 25, 2026 (ARR submission)
6	
7	## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)
8	
9	1. **The Capability Trap**: Symbolic consensus methods face a fundamental tension: they require output diversity (C0>20%) to differ from voting, but extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to a noise injector. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B).
10	2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.
11	3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.
12	
13	## Core Insight
14	Symbolic constraint consensus doesn't improve LLM reasoning because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these constraints lack the discriminative power to distinguish correct from incorrect answers. MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, performing no better (often worse) than simple majority voting. We provide the first systematic empirical study characterizing this trap across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model.
15	
16	## Story Spine
17	- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?
18	- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.
19	- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.
20	- **Headline result**: "Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level."
21	
22	## Anticipated Reviewer Concerns & Defensive Experiments
23	1. **"Gains not statistically significant"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.
24	2. **"Only a better tiebreaker, not worth the overhead"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis
25	3. **"Only Qwen models"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B
26	4. **"Only one reasoning model"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)
27	5. **"Only logic domain"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.
28	6. **"MAX-SAT is over-engineering"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.
29	7. **"Random tiebreak baseline"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.
30	8. **"Why not just use a reasoning model?"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.
31	9. **"How does this compare to Logic-LM / LINC?"** → exp-015: Logic-LM × K baseline (CPU-only)
32	10. **"Weighted SC is simpler"** → exp-016: Weighted SC baseline (CPU-only)
33	11. **"C0 is trivially derived"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.
34	12. **"Within-family scaling?"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.
35	
36	## Working Title
37	**"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning"**
38	(Alternatives: 
39	- "When Does Symbolic Consensus Help? An Empirical Answer: Rarely, and Here's Why"
40	- "Diversity Without Quality: The Fundamental Limitation of Constraint-Based LLM Aggregation")
41	
42	## Paper Structure (EMNLP 8pp + appendix)
43	- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Capability Trap: C0 × Constraint Quality inverse correlation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Tiebreak Analysis: quality on tied questions only)
44	- Main Figures: F1 (Method Pipeline), F2 (Capability Trap Scatter: C0 vs Constraint Precision, colored by domain, hero figure), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: flat line, contrasting with theoretical upper bound)
45	- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data
46	
47	## Claim Risk Notes (Updated D035 + exp-014)
48	- **Claim 1 mechanism refinement**: "Inverse correlation between diversity and quality" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: "constraints lack discriminative power regardless of diversity level." Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.
49	- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.
50	- **Claim 3 gradient risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to "binary indicator". Need exp-004/007 for gradient data. OPEN.
51	- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.
52	- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.
53	
54	## Venue Fit Risks
55	- EMNLP: Negative-results/analysis paper. Must answer "so what should practitioners do?" → C0 as deployment diagnostic + overhead analysis.
56	- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.
57	- Statistical power: Now strong (N>1,200 combined across powered tests).
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3a757e3-1d3b-42e0-810f-7bb22f55e50f",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "01746ecd-369f-4b71-afc5-08fc8c480435",
  "sourceToolAssistantUUID": "e3a757e3-1d3b-42e0-810f-7bb22f55e50f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T16:00:01.377Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WNtU2xsqfWFyGHTAKpVQ8e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01746ecd-369f-4b71-afc5-08fc8c480435",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RGFkVbmtW4kaEYq2UC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11d2320a-922e-41b8-b5db-6f54db45f04d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms4GPENQtqU1dDho31hoUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11528,
      "cache_read_input_tokens": 20377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11528,
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

_source line 17 · 2026-05-17T16:00:01.648Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MJSjjo8HpwKmEfCMfukbE9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11d2320a-922e-41b8-b5db-6f54db45f04d",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RGFkVbmtW4kaEYq2UC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a0bd124-ee9c-4a6f-a6e0-3cf14bdee719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms4GPENQtqU1dDho31hoUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11528,
      "cache_read_input_tokens": 20377,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11528
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 20377,
          "cache_creation_input_tokens": 11528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11528,
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

_source line 18 · 2026-05-17T16:00:01.656Z_

<details><summary>↩ Tool result · `toolu_01WNtU2xsqfWFyGHTAKpVQ8e`</summary>

```text
1	tier: best
2	narrative_guidance: 'Capability trap 被结构性确认。Temperature ablation (§5) 展示 diversity
3	  通过 temperature 可连续操控 (C0: 28%→68%), 但 SICA-SC gap 在所有温度下恒为零 (|Δ|≤1.7pp, 全部 p>0.30)
4	  ——这是结构性限制而非调参失败。F2 hero figure per-problem scatter (n=307) 直观展示 constraint precision
5	  ≈ 0.50 (近随机) 且与 vote_entropy 无相关 (slope=0.003, r²<0.01), 无需 binning 即清晰可读。Qwen 7B/14B/72B
6	  产出三个 distinct C0 水平 (65%/53%/15%), Claim 3 diagnostic predictor 成立。五个模型族 combined
7	  N>1300 全部 SICA≈SC (最大 |Δ|=6.67pp 但 p=0.22, 零个 p<0.10)。MaxSAT≈count-only≈random-weight
8	  确认 solver 无贡献, 与 F2 per-problem 形成双重机制证据。Discordant pair aggregate winrate=50.7%
9	  (34/67), weighted Δ=+0.20pp——统计上精确为零。三条 claims 措辞不改, title "The Capability Trap"
10	  不变。强 EMNLP main submission, contribution = mechanism identification + first systematic
11	  negative result + zero-cost diagnostic。
12	
13	  '
14	imagined_experiments:
15	- name: sica_k_ablation_14b
16	  plan_id: exp-002
17	  description: K=6/8/11/12/16/20 sensitivity on D012 60q, 含 odd K=11 tiebreak 隔离测试
18	  expected_results:
19	    n: 60
20	    K6_sica: 0.733
21	    K6_sc: 0.733
22	    K6_delta_pp: 0.0
23	    K8_sica: 0.733
24	    K8_sc: 0.75
25	    K8_delta_pp: -1.7
26	    K11_sica: 0.733
27	    K11_sc: 0.733
28	    K11_delta_pp: 0.0
29	    K12_sica: 0.7
30	    K12_sc: 0.75
31	    K12_delta_pp: -5.0
32	    K16_sica: 0.717
33	    K16_sc: 0.75
34	    K16_delta_pp: -3.3
35	    K20_sica: 0.7
36	    K20_sc: 0.733
37	    K20_delta_pp: -3.3
38	    all_K_sica_leq_sc: true
39	    larger_K_degrades_sica: true
40	    mcnemar_p_all_gt_020: true
41	  result_rationale: 'SICA ≤ SC at all K 因为 MaxSAT over non-discriminative constraints
42	    只注入噪声。 K=11 (odd) Δ=0 是关键: odd K 消除 SC ties, SICA 失去唯一有效机制 (tiebreaking), collapse
43	    to SC。Larger K (16, 20) 放大噪声注入——更多 traces → 更多 non-discriminative constraints
44	    → MaxSAT 更大概率排除正确答案。-5pp at K=12 和 -3.3pp at K=16/20 反映此噪声累积。All p>0.20 因 n=60
45	    (SE≈5-6pp), 个体波动是 sampling noise 叠加在 true effect ≈ 0 之上。
46	
47	    '
48	  tables:
49	  - 'Appendix: K sensitivity table (all K × accuracy)'
50	  figures_description:
51	  - 'Appendix figure: SICA-SC gap (y) vs K (x), 水平参考线 y=0, 各点 error bars 均跨零。Larger
52	    K 呈弱负趋势。K=11 精确命中零线。'
53	  analysis: 'K ablation 消除 ''wrong K'' counterargument。K=11 odd-K test 最锐利: 若 SICA
54	    在 tiebreaking 之外有价值, gap 应在 odd K 也存在; gap=0 确认 SICA = tiebreaker。 Combined with
55	    exp-003 (tiebreak 仅占 17% 问题), SICA 的唯一 mechanism 被量化为 micro-scale effect。Paper
56	    §4.2 mechanism analysis。
57	
58	    '
59	- name: tiebreak_baseline_analysis
60	  plan_id: exp-003
61	  description: 'CPU-only: SICA vs SC-random vs SC-alphabetical vs SC-first-seen tiebreak
62	    比较'
63	  expected_results:
64	    n_tied_questions: 10
65	    pct_tied_of_total: 0.167
66	    sica_tiebreak_accuracy: 0.8
67	    random_tiebreak_accuracy: 0.5
68	    alphabetical_tiebreak_accuracy: 0.6
69	    first_seen_tiebreak_accuracy: 0.4
70	    sica_net_gain_over_random_on_all_60: 0.5
71	  result_rationale: 'SICA 在 tied questions 上 80% 正确, 因为 constraint weighting 即使不判别
72	    correct vs incorrect, 对 tie (两个 answer 票数相等) 仍能通过微弱信号打破平衡。但 tied questions 仅占
73	    17% (K=12 even-K 才产生 tie)。10 题中多赢 3 题 (vs random) 对 60 题整体贡献 +0.5pp——在 SE≈6pp
74	    的噪声中不可见。Random 50% 是理论 期望值; alphabetical 60% 反映答案选项 label 与正确答案的偶然相关; first-seen
75	    40% 因为 model 首条 trace 并非最准确。
76	
77	    '
78	  tables:
79	  - 'T4: Tiebreak Analysis (tied subset)'
80	  figures_description:
81	  - 'T4 bar chart: 四种 tiebreak 方法在 tied subset 上的 accuracy。SICA 80% 显著最高, 但 caption
82	    标注 ''ties = 17% of problems, net impact < 1pp on full set''。'
83	  analysis: '回应 reviewer ''SICA is just a better tiebreaker''。Answer: yes, and an
84	    effective one, but ties are structurally rare at K=12. At odd K (exp-002 K=11),
85	    ties = 0, SICA≡SC。Even at even K, 80% × 17% = 1.3% net correct → <1pp overall。
86	    Cost-benefit: 49% overhead (exp-009) for <1pp on tied subset = not worthwhile。
87	
88	    '
89	- name: sica_constraint_ablation
90	  plan_id: exp-013
91	  description: 'CPU-only ablation: MaxSAT vs count-only vs random-weight on exp-001
92	    (n=804)'
93	  expected_results:
94	    n: 804
95	    maxsat_accuracy: 0.7649
96	    count_only_accuracy: 0.7662
97	    random_weight_accuracy: 0.7637
98	    sc_baseline_accuracy: 0.7624
99	    agreement_802_of_804: true
100	    maxsat_vs_count_mcnemar_p: 0.99
101	    maxsat_vs_random_mcnemar_p: 0.85
102	    maxsat_vs_sc_mcnemar_p: 0.74
103	    all_pairwise_nonsignificant: true
104	  result_rationale: 'MaxSAT ≈ count-only 因为 constraint satisfiability 不携带判别信息。当 constraints
105	    对正确/错误答案同等满足时, solver 的优化退化为计数: satisfiability structure 无 贡献。Random-weight ≈
106	    MaxSAT 因为权重差异在 non-discriminative constraints 上是 纯噪声。802/804 题四种方法答案一致, 仅 2 题分歧
107	    (互相抵消)。这直接证明 SAT 解算机制空洞化——是 capability trap 的 mechanism evidence。
108	
109	    '
110	  tables:
111	  - 'T3: Constraint Ablation (MaxSAT vs count-only vs random-weight vs SC)'
112	  figures_description:
113	  - 'T3 grouped bar: 四种方法 accuracy 几乎等高 (~76.4%), error bars 完全重叠。Visual message:
114	    solver adds nothing beyond counting。'
115	  analysis: 'Make-or-break evidence for capability trap mechanism。如果 MaxSAT ≈ count-only,
116	    solver 无附加值——constraints 没有 exploitable satisfiability structure。Combined with
117	    F2 (precision≈0.50), 形成双重机制证据: (1) constraints 不判别 (F2), (2) solver 因此无法提取信号 (T3)。Paper
118	    §4.1 核心机制结果。exp-013 + exp-019 共同构成 Claim 1 的 evidence base。
119	
120	    '
121	- name: sica_strategyqa_14b
122	  plan_id: exp-017
123	  description: Qwen2.5-14B on StrategyQA 60q (K=12), commonsense reasoning domain
124	  expected_results:
125	    n: 60
126	    k: 12
127	    sica_accuracy: 0.5667
128	    sc_accuracy: 0.5333
129	    delta_pp: 3.33
130	    mcnemar_p: '>0.30'
131	    bootstrap_p: 0.1346
132	    multi_candidate_rate: 0.1
133	    extraction_rate_trace: 0.704
134	    discordant_sica_wins: 2
135	    discordant_sc_wins: 0
136	    model: Qwen2.5-14B-Instruct
137	    dataset: StrategyQA
138	  result_rationale: 'StrategyQA C0=10% 远低于 plan 预期 (35-50%), 因为 14B 在 binary commonsense
139	    (yes/no) 上足够强, 大多数问题 12 traces 一致。仅 6 题多候选, 2 题 SICA 翻转正确。+3.33pp non-significant
140	    (n=60 SE≈6pp, bootstrap p=0.13)。Extraction rate 仅 70.4% (commonsense 推理链缺少可形式化逻辑结构),
141	    进一步限制 SICA 操作空间。2:0 discordant ratio 看似 SICA 占优, 但 n=2 discordant pairs 无统计意义。
142	
143	    '
144	  tables:
145	  - 'T1: Main Results (StrategyQA × Qwen-14B row)'
146	  - 'F3: Operating Regime Heatmap (StrategyQA × Qwen-14B cell)'
147	  figures_description:
148	  - 'T1 row: StrategyQA | Qwen-14B | SC 53.3% | SICA 56.7% | Δ +3.3 | p n.s. | C0=10%'
149	  analysis: 'StrategyQA 结果挑战 best-case-diversity 假设: commonsense domain 并非 diversity
150	    最高场景 (对强模型而言)。但强化 capability trap: 即使 C0 恰好产生少量 discordant, SICA 仍无显著优势。与 ARC
151	    (C0=5%) 和 PW+FOLIO (C0=38%) 形成三域覆盖。
152	
153	    '
154	- name: sica_arc_challenge_14b
155	  plan_id: exp-018
156	  description: Qwen2.5-14B on ARC-Challenge 60q (K=12), 科学推理 4 选 1
157	  expected_results:
158	    n: 60
159	    k: 12
160	    sica_accuracy: 0.95
161	    sc_accuracy: 0.9667
162	    delta_pp: -1.67
163	    multi_candidate_rate: 0.05
164	    extraction_rate: 1.0
165	    discordant_sica_wins: 0
166	    discordant_sc_wins: 1
167	    model: Qwen2.5-14B-Instruct
168	    dataset: ARC-Challenge
169	  result_rationale: '14B 在 ARC-Challenge SC 高达 96.7%, C0 仅 5% (3 题多候选)。模型对 science
170	    常识 足够自信, 12 traces 几乎总一致。唯一 discordant pair SC 赢——MaxSAT 排除了正确 答案的 constraint。4-choice
171	    format 理论上增加 diversity (更多选项), 但 14B 能力 过强, format 效应被 capability 压制。C0=5% 接近
172	    QwQ-32B 退化阈值。
173	
174	    '
175	  tables:
176	  - 'T1: Main Results (ARC × Qwen-14B row)'
177	  - 'F3: Operating Regime Heatmap (ARC × Qwen-14B cell)'
178	  figures_description:
179	  - 'T1 row: ARC | Qwen-14B | SC 96.7% | SICA 95.0% | Δ -1.7 | C0=5%'
180	  analysis: 'ARC 是 14B 的 ceiling 域: SC 已达 96.7%, 无提升空间。SICA 微损 (-1.7pp) 因为 solver
181	    在极少数 multi-candidate 问题上注入噪声。与 FOLIO (acc ~79%, C0 ~38%) 对比展示 capability-diversity
182	    反向关系: high accuracy → low C0 → method degenerates。
183	
184	    '
185	- name: constraint_quality_correlation
186	  plan_id: exp-019
187	  description: 'CPU-only: per-problem constraint precision vs vote_entropy (exp-001
188	    n≈307 multi-candidate). F2 hero figure'
189	  expected_results:
190	    n_multi_candidate: 307
191	    constraint_precision_mean: 0.505
192	    constraint_precision_std: 0.148
193	    constraint_precision_median: 0.5
194	    precision_vs_entropy_slope: 0.003
195	    precision_vs_entropy_r_squared: 0.002
196	    precision_vs_entropy_p: 0.42
197	    folio_precision_mean: 0.512
198	    proofwriter_precision_mean: 0.498
199	    cross_domain_precision_diff_p: 0.6
200	    fraction_precision_below_040: 0.28
201	    fraction_precision_above_060: 0.25
202	    discordant_pair_sica_winrate_overall: 0.48
203	  result_rationale: 'Constraint precision ≈ 0.50 (近随机) 因为 LLM 提取的 FOL constraints
204	    捕获推理 trace 的表面结构 (变量命名、逻辑连接词模式) 而非深层语义正确性。正确和错误 traces 共享相似表面结构 (都使用 if-then/forall/exists),
205	    导致 constraints 无法区分二者。 Slope ≈ 0 因为此限制是 structural 的: 无论 vote 分布多分散 (高 entropy)
206	    或多集中 (低 entropy), constraint discriminative power 都不变——它取决于 extraction quality
207	    而非 diversity level。FOLIO 和 ProofWriter precision 几乎相同 (0.512 vs 0.498, 差异 p=0.60),
208	    说明跨域一致。28% 问题 precision<0.40 (constraints 反向判别), 25% precision>0.60 (偶然判别), 呈对称分布围绕
209	    0.50。
210	
211	    '
212	  tables:
213	  - 'T2: Constraint Quality Summary (precision by domain × model)'
214	  figures_description:
215	  - 'F2 (Hero Figure): Scatter, x=vote_entropy (0.3–1.8), y=constraint_precision (0–1.0)。
216	    307 points, blue=ProofWriter, orange=FOLIO。水平参考线 y=0.50。Points 形成 diffuse 水平带,
217	    中心在 0.50, 无可见趋势。Regression line 近乎水平 (slope=0.003)。 Caption: ''Constraint precision
218	    is near-random (mean=0.50) regardless of output diversity, confirming constraints
219	    lack discriminative power at all diversity levels.'' Per-problem granularity 无需
220	    binning, 每个 dot = 一个具体问题, 信息密度高。
221	
222	    '
223	  analysis: 'F2 是论文 hero figure, 一图传达 capability trap: diversity (x) 存在且可变, 但 constraint
224	    quality (y) 恒为随机水平。''Regardless of diversity'' 可视化为 slope=0。 与 T3 (MaxSAT≈count-only)
225	    形成双重机制证据: (1) constraints 不判别 (F2), (2) solver 因此无法提取信号 (T3)。Per-problem granularity
226	    (n=307) 比 experiment-level correlation (n=7, r=0.15 p=0.74) 统计力强两个数量级, 是 D035
227	    识别的 F2 data gap 的完整解决。
228	
229	    '
230	- name: sica_7b_scaling
231	  plan_id: exp-004
232	  description: Qwen2.5-7B-Instruct on D012 60q. Within-Qwen weak model, high C0
233	  expected_results:
234	    n: 60
235	    k: 12
236	    sica_accuracy: 0.533
237	    sc_accuracy: 0.55
238	    delta_pp: -1.7
239	    multi_candidate_rate: 0.65
240	    extraction_rate: 0.82
241	    answer_extraction_rate: 0.88
242	    contradiction_rate: 0.08
243	    discordant_sica_wins: 2
244	    discordant_sc_wins: 3
245	    mcnemar_p: 0.65
246	    proofwriter_sica: 0.5
247	    proofwriter_sc: 0.533
248	    folio_sica: 0.567
249	    folio_sc: 0.567
250	    model: Qwen2.5-7B-Instruct
251	  result_rationale: '7B 在 formal logic 上显著弱于 14B (SC 55% vs 73%), 产生大量 answer disagreement
252	    (C0=65%)。但更弱模型也提取更差 constraints: extraction_rate 89%→82%, contradiction_rate 2.2%→8%。高
253	    C0 意味着更多 multi-candidate 问题可操作, 但 constraints 质量更差意味着 MaxSAT 优化方向更随机。5 discordant
254	    pairs 中 SC 赢 3 个: MaxSAT 在 noisy constraints 上更大概率排除正确答案。 这完美展示 capability trap
255	    weak-model 端: diversity abundant, quality absent。
256	
257	    '
258	  tables:
259	  - 'T1 appendix: Qwen-7B row'
260	  - 'F4: C0 vs Gap (7B 数据点: C0=65%, Δ=-1.7pp)'
261	  figures_description:
262	  - 'F4 scatter: 7B 位于 high-C0 端 (x=65%) below zero line (y=-1.7pp)。与 72B (x=15%,
263	    y=0) 和 14B (x=53%, y≈0) 共同形成 within-Qwen scaling 趋势线。'
264	  analysis: '7B 提供 within-Qwen scaling 的 high-diversity anchor。Combined with 14B (C0=53%)
265	    and 72B (C0≈15%), 三个 distinct C0 levels within single model family 成立 (c0_scaling_distinct_levels=3)。C0
266	    与 model scale 反向 (7B→65%, 14B→53%, 72B→15%) 验证 C0 as capability proxy。但 SICA-SC
267	    gap 在三个 scale 都 ≈ 0, 证明 C0 是 necessary but insufficient。For Claim 3: C0=65% +
268	    Δ=-1.7pp 是 ''high C0 but no gain'' 的最强数据点。
269	
270	    '
271	- name: qwq_32b_operating_regime
272	  plan_id: exp-005
273	  description: 'QwQ-32B negative results: C0<5%, SICA≡SC. CPU-only格式化 MVP 已有数据'
274	  expected_results:
275	    total_problems: 46
276	    qwq_c0_nominal_pct: 10.3
277	    qwq_c0_effective_pct: 2.6
278	    qwen14b_c0_pct: 46.0
279	    diversity_ratio: 17.7
280	    aime_delta_pp: 0.0
281	    aime_n: 22
282	    proofwriter_delta_pp: -5.9
283	    proofwriter_n: 17
284	    folio_n: 2
285	    c0_below_20_threshold: true
286	    sica_structurally_degenerate: true
287	  result_rationale: 'QwQ-32B 作为 full reasoning model, deterministic chain-of-thought
288	    压制 sampling diversity: 即使 T=0.7, 12 traces 几乎总产生相同答案 (effective C0=2.6%)。AIME
289	    22 题 0% multi-candidate (完全一致)。Nominal C0=10.3% vs effective C0=2.6% 的差距来自 answer
290	    extraction 格式噪声 (如 "30" vs "30.0"), 非真实 reasoning divergence。 ProofWriter -5.9pp
291	    是 n=17 噪声 (SE≈12pp)。QwQ-32B 展示 capability trap strong- reasoning 端: model 足够强
292	    → 无 diversity → SICA 结构性退化为 SC。
293	
294	    '
295	  tables:
296	  - 'T1: Main Results (QwQ-32B row, all cells ''SICA≡SC'')'
297	  - 'F3: Operating Regime Heatmap (QwQ-32B column 全灰)'
298	  figures_description:
299	  - 'F3: QwQ-32B row 全灰 (C0<5% → degenerate)。与 instruction model rows 形成 sharp 对比。'
300	  analysis: 'QwQ-32B 是 Claim 2 ''operating regime empty'' 的一极: full reasoning → no
301	    diversity → method degenerates。对称地, instruction models 展示另一极: high diversity →
302	    no constraint quality → method fails。No model hits the sweet spot。C0=2.6% 远低于
303	    20% 阈值, 直接支撑 Claim 3 early-stopping criterion。
304	
305	    '
306	- name: c0_diagnostic_validation
307	  plan_id: exp-006
308	  description: 'CPU-only: C0 vs SICA-SC gap 散点, 跨所有 models/K/domains, 验证 C0 as predictor'
309	  expected_results:
310	    n_conditions: 14
311	    c0_range_pct:
312	    - 2.6
313	    - 65.0
314	    gap_range_pp:
315	    - -3.3
316	    - 6.67
317	    regression_slope: -0.02
318	    regression_r_squared: 0.06
319	    regression_p: 0.4
320	    c0_below_5_n: 3
321	    c0_below_5_mean_abs_gap: 0.6
322	    c0_above_20_n: 8
323	    c0_above_20_mean_gap: 0.1
324	    c0_above_20_all_p_gt_010: true
325	    distinct_c0_levels_qwen_family: 3
326	    distinct_c0_levels_all_models: 5
327	  result_rationale: 'C0 与 gap 无线性关系 (r²=0.06, p=0.40) 因为 gap 在所有 C0 水平围绕 0 波动。 C0<5%
328	    条件 (QwQ-32B 2.6%, ARC-14B 5%, StrategyQA-14B 10%) SICA≡SC: 方法 结构性退化。C0>20% 条件
329	    (Qwen-7B 65%, LLaMA-8B 62%, DeepSeek-R1-7B 58%, Mistral 50%, Qwen-14B 53%) mean
330	    gap≈0: diversity 存在但 constraints 不判别。 Within-Qwen 三水平 (15%/53%/65%) + DeepSeek
331	    (58%) + LLaMA (62%) ≈ 5 distinct levels。F4 展示理论上界 vs 实际数据的 gap = capability trap
332	    的视觉量化。
333	
334	    '
335	  tables:
336	  - 'F4: C0 vs Gap (所有条件)'
337	  figures_description:
338	  - 'F4: x=C0 (0–70%), y=SICA-SC gap (-6 to +8pp)。~14 data points, all cluster around
339	    y=0。Dashed theoretical upper bound curve (if constraints were perfect, gap ∝ C0)。实际数据与理论上界之间的
340	    gap = capability trap magnitude。 Grey zone: C0<5% (degeneration zone)。Red zone:
341	    C0>20%, gap≈0 (trap zone)。 No point in upper-right quadrant (the sweet spot is
342	    empty)。
343	
344	    '
345	  analysis: 'F4 是 Claim 3 核心 figure。Bifurcation 清晰: C0<5% → degenerate (grey), C0>20%
346	    → trapped (red), no sweet spot。理论上界展示 SICA 在 C0=50% 时应有 5-10pp gain if constraints
347	    discriminative——this unrealized potential IS the trap。 C0 因此是 zero-cost early
348	    stopping criterion: compute C0, if <20% stop (method degenerate), if >20% stop
349	    (trap guarantees no gain)。Either way, don''t proceed。
350	
351	    '
352	- name: sica_72b_awq
353	  plan_id: exp-007
354	  description: Qwen2.5-72B-Instruct-AWQ on D012 60q. Within-Qwen strong model, low
355	    C0
356	  expected_results:
357	    n: 60
358	    k: 12
359	    sica_accuracy: 0.867
360	    sc_accuracy: 0.867
361	    delta_pp: 0.0
362	    multi_candidate_rate: 0.15
363	    extraction_rate: 0.93
364	    answer_extraction_rate: 1.0
365	    contradiction_rate: 0.01
366	    discordant_sica_wins: 1
367	    discordant_sc_wins: 1
368	    mcnemar_p: 1.0
369	    proofwriter_sica: 0.833
370	    proofwriter_sc: 0.833
371	    folio_sica: 0.9
372	    folio_sc: 0.9
373	    model: Qwen2.5-72B-Instruct-AWQ
374	  result_rationale: '72B SC accuracy 高达 86.7%, C0 仅 15% (9 题多候选)。能力强到大部分问题 12 traces
375	    一致。Extraction_rate 高 (93%), contradiction_rate 极低 (1%)——72B 的 constraints 质量确实更好。但
376	    C0 太低, 没有足够 multi-candidate 问题让 SICA 操作。 仅 ~2 discordant pairs, 各赢一题, 净 Δ=0。AWQ
377	    4-bit quantization 可能引入 微量额外噪声, 使 C0 略高于 full-precision 72B (否则可能 C0<10%), 但仍远低于
378	    14B。这是 capability trap strong-model 端: quality improves but diversity vanishes。
379	
380	    '
381	  tables:
382	  - 'T1 appendix: Qwen-72B row'
383	  - 'F4: C0 vs Gap (72B 数据点: C0=15%, Δ=0)'
384	  figures_description:
385	  - 'F4: 72B 位于 low-C0 端 (x=15%, y=0)。与 7B (x=65%, y=-1.7) 和 14B (x=53%, y≈0) 形成 within-Qwen
386	    三点连线, 展示 C0 scaling with model size。'
387	  analysis: '72B 是 within-Qwen scaling 的 low-diversity anchor。三点连线清晰展示 C0 随 model
388	    scale 单调递减 (65%→53%→15%) 但 gap 恒为 ≈0。这证明 ''even when you scale up within a family,
389	    you trade diversity for accuracy without ever hitting the sweet spot''。72B extraction
390	    quality 最高 (93%, 1% contradiction) 佐证 strong model → better constraints, 但 futile
391	    when C0 is low。
392	
393	    '
394	- name: overhead_analysis
395	  plan_id: exp-009
396	  description: 'exp-001 Wall-time breakdown: trace generation, constraint extraction,
397	    MaxSAT'
398	  expected_results:
399	    n: 804
400	    mean_total_wall_s: 61.6
401	    mean_trace_gen_s: 31.6
402	    trace_gen_pct: 51.3
403	    mean_extract_s: 29.0
404	    extract_pct: 47.0
405	    mean_dedup_s: 1.0
406	    dedup_pct: 1.6
407	    mean_maxsat_s: 0.003
408	    maxsat_pct: 0.005
409	    sica_overhead_over_sc_pct: 48.7
410	    p50_overhead_pct: 48.9
411	    p90_overhead_pct: 57.6
412	  result_rationale: 'SICA 相比 SC 增加 ~49% wall time, 几乎全部来自 constraint extraction (一次额外
413	    LLM inference pass per trace, 解析 FOL)。MaxSAT solver 本身极快 (0.003s, <0.01% 总时间)——瓶颈不在
414	    solver complexity 而在 extraction cost。如果 constraints 是 discriminative 的, 49% overhead
415	    可能值得 (每 query 多花 30s 换 5pp+ accuracy); 但 Δ≈0 意味着 49% 额外计算换零收益。P90 overhead 57.6%
416	    来自长 traces (FOLIO domain), extraction 时间与 trace 长度成正比。
417	
418	    '
419	  tables:
420	  - 'Appendix: Overhead breakdown table'
421	  figures_description:
422	  - 'Stacked bar: trace gen 51.3% + extraction 47% + dedup 1.6% + solver 0.005%。Caption:
423	    ''solver is negligible; LLM extraction calls dominate overhead''。'
424	  analysis: '回应 reviewer ''is the overhead worth it'': 不值得。49% overhead = 零精度收益。 SC
425	    是 Pareto dominant (same accuracy, half the cost)。Solver time <0.01% 表明 MaxSAT
426	    formulation 计算效率不是问题——问题在于输入质量。This strengthens practical guidance: even if future
427	    work improves constraint quality, the extraction cost remains substantial。
428	
429	    '
430	- name: sica_llama_8b
431	  plan_id: exp-011
432	  description: LLaMA-3.1-8B-Instruct on D012 60q. 第三 instruction-scale 家族
433	  expected_results:
434	    n: 60
435	    k: 12
436	    sica_accuracy: 0.6667
437	    sc_accuracy: 0.6
438	    delta_pp: 6.67
439	    multi_candidate_rate: 0.617
440	    extraction_rate: 0.856
441	    answer_extraction_rate: 0.896
442	    contradiction_rate: 0.053
443	    truncated_traces: 44
444	    discordant_sica_wins: 5
445	    discordant_sc_wins: 1
446	    mcnemar_p: 0.22
447	    model: LLaMA-3.1-8B-Instruct
448	  result_rationale: 'LLaMA-8B C0=62%, SC=60% (instruction-scale models 中最弱)。+6.67pp
449	    是 n=60 采样噪声: SE≈6pp, 1.1σ deviation, p=0.22 non-significant。5:1 discordant ratio
450	    看似强烈, 但绝对数量小 (6 pairs)。关键验证来自同模型更大 n: exp-019 (StrategyQA n=200, Δ=+2.0pp p=0.42)
451	    和 exp-020 (FOLIO n=204, Δ=-2.45pp p=0.27) 确认 true effect 接近 0。正 delta 与 负 delta
452	    在不同 domains 交替出现 = 纯噪声。 44/720 truncated traces 因 8B context limit, 但 truncation
453	    对 SICA/SC 影响对称。
454	
455	    '
456	  tables:
457	  - 'T1: Main Results (LLaMA-8B D012 row)'
458	  figures_description:
459	  - 'T1 row: D012 | LLaMA-8B | SC 60.0% | SICA 66.7% | Δ +6.7 | p=0.22 n.s.'
460	  analysis: 'exp-011 的 +6.67pp 是全研究最大正 delta, 但 exp-019/020 (同模型 n=200+) 展示 true effect
461	    ≈ 0。Paper framing: ''small-sample positive signal does not survive powered replication''——本身是方法论
462	    lesson。LLaMA-8B 作为第三 instruction-scale family (加 Qwen/Mistral), 满足 EMNLP 三家族最低门槛。
463	
464	    '
465	- name: gsm8k_pilot_14b
466	  plan_id: exp-012
467	  description: Qwen2.5-14B on GSM8K 30q pilot (K=12). 数学推理域覆盖
468	  expected_results:
469	    n: 30
470	    k: 12
471	    sica_accuracy: 0.867
472	    sc_accuracy: 0.867
473	    delta_pp: 0.0
474	    multi_candidate_rate: 0.1
475	    extraction_rate: 0.75
476	    answer_extraction_rate: 0.95
477	    discordant_sica_wins: 0
478	    discordant_sc_wins: 0
479	    model: Qwen2.5-14B-Instruct
480	    dataset: GSM8K
481	  result_rationale: '14B 在 GSM8K accuracy ~87%, C0 ≈ 10%。开放式数学答案 (具体数字) 理论上有更大 answer
482	    space, 但模型能力足以收敛到正确数值。Extraction rate 偏低 (75%) 因为数值 计算步骤难以 FOL 形式化 (例 "3×5+2=17"
483	    → FOL 表达不自然)。0 discordant pairs → SICA ≡ SC on all 30 题。C0≈10% 类似 ARC/StrategyQA:
484	    14B 在 ''easier'' domains 上能力过强, diversity 不足。
485	
486	    '
487	  tables:
488	  - 'Appendix: Cross-domain (GSM8K row)'
489	  - 'F4: C0 vs Gap (GSM8K point)'
490	  figures_description:
491	  - 'F4 data point: GSM8K C0=10%, Δ=0, 位于 low-C0 degeneration zone 边缘。'
492	  analysis: 'GSM8K 确认: 当模型在目标 domain 足够强时, C0 自然低, SICA 无操作空间。 Extraction rate 75%
493	    (vs logic domain 89%) 说明 domain 影响 extraction feasibility。 Appendix material,
494	    回应 ''what about math reasoning'' 的 reviewer。
495	
496	    '
497	- name: sica_deepseek_r1_llama_8b
498	  plan_id: exp-014
499	  description: DeepSeek-R1-Distill-Qwen-7B on D012 60q. Distilled reasoning model
500	    行为验证
501	  expected_results:
502	    n: 60
503	    k: 12
504	    sica_accuracy: 0.683
505	    sc_accuracy: 0.717
506	    delta_pp: -3.33
507	    multi_candidate_rate: 0.583
508	    extraction_rate: 0.839
509	    answer_extraction_rate: 0.939
510	    truncated_traces: 72
511	    contradiction_rate: 0.037
512	    discordant_sica_wins: 0
513	    discordant_sc_wins: 2
514	    mcnemar_p: 0.48
515	    model: DeepSeek-R1-Distill-Qwen-7B
516	  result_rationale: '关键发现: C0=58.3%, 行为完全像 instruction-scale model, 非 plan 预期的 reasoning
517	    model (C0<5%)。7B 参数量不足以维持 R1 的 deterministic reasoning chain——蒸馏后 小模型在 7B 容量下退化为高
518	    diversity 行为。Δ=-3.33pp: 2 discordant pairs SC 全赢, MaxSAT constraint 排除恰好排错。Truncated
519	    traces 最多 (72/720), 因 R1 风格长 reasoning + 7B context 限制。结论: distilled reasoning
520	    ≠ full reasoning, 参数量是决定性因素, 非训练方法。
521	
522	    '
523	  tables:
524	  - 'T1: Main Results (DeepSeek-R1-7B row)'
525	  - 'Appendix: Reasoning model comparison (QwQ C0=2.6% vs DeepSeek C0=58.3%)'
526	  figures_description:
527	  - 'Appendix table: QwQ-32B (full reasoning, C0=2.6%) vs DeepSeek-R1-7B (distilled,
528	    C0=58.3%)。Caption: ''Distillation at 7B recovers instruction-scale behavior''。'
529	  analysis: 'exp-014 解决分类问题: DeepSeek-R1-7B 归入 instruction-scale (C0=58%) 非 reasoning
530	    (C0<5%)。Model taxonomy 应以行为 (C0 水平) 而非训练方法定义。Paper 重分类 DeepSeek-R1-7B 为 ''instruction-scale
531	    with reasoning-style training'', 避免 reviewer ''only one reasoning model'' 攻击。QwQ-32B
532	    remains sole full reasoning model。
533	
534	    '
535	- name: logic_lm_baseline
536	  plan_id: exp-015
537	  description: 'Logic-LM × K: single-trace FOL verification K 次后 vote, CPU-only on
538	    FOLIO'
539	  expected_results:
540	    n: 204
541	    k: 12
542	    logic_lm_k_accuracy: 0.789
543	    sc_accuracy: 0.794
544	    sica_accuracy: 0.794
545	    logic_lm_vs_sc_delta_pp: -0.5
546	    logic_lm_vs_sica_delta_pp: -0.5
547	    verification_pass_rate: 0.92
548	    verification_discriminative: false
549	    mcnemar_logic_lm_vs_sc_p: 0.82
550	  result_rationale: 'Logic-LM-K 将每条 trace 独立验证 (extract FOL → solver check → pass/fail)
551	    后 majority vote。Accuracy ≈ SC 因为 verification pass rate 极高 (92%): solver 对 大部分
552	    traces 返回 satisfiable, 无论 trace 是否正确。原因同 SICA: constraints 不判别。''Verification''
553	    退化为 ''format check''——只要 FOL syntax 正确 solver 就 pass。这消除 ''maybe aggregation is
554	    the problem, single-trace verification works better'' 反论。瓶颈是 constraint quality,
555	    非 aggregation architecture。
556	
557	    '
558	  tables:
559	  - 'Appendix: Logic-LM × K baseline comparison'
560	  figures_description:
561	  - 'Appendix table row: FOLIO | Logic-LM-K 78.9% ≈ SC 79.4% ≈ SICA 79.4%。'
562	  analysis: '回应 reviewer ''compare to Logic-LM/LINC''。Answer: Logic-LM-K 也 ≈ SC, 因为
563	    bottleneck 是 extraction quality 非 aggregation method。Single-trace verification
564	    也失败, 因为 underlying constraints non-discriminative。This generalizes the capability
565	    trap beyond SICA to any FOL-constraint-based method。
566	
567	    '
568	- name: weighted_sc_baseline
569	  plan_id: exp-016
570	  description: 'Weighted SC (Taubenfeld 2024 style): uniform/inv-length/length/constraint-count
571	    on exp-001'
572	  expected_results:
573	    n: 804
574	    sc_uniform_accuracy: 0.7624
575	    sica_maxsat_accuracy: 0.7649
576	    inv_length_accuracy: 0.7674
577	    length_weighted_accuracy: 0.7525
578	    constraint_count_accuracy: 0.7525
579	    inv_length_vs_sc_p: 0.453
580	    length_vs_sc_p: 0.153
581	    inv_length_vs_sica_p: 0.864
582	    all_nonsignificant: true
583	  result_rationale: '所有 weighting 方案 ≈ SC, 因为 trace-level 信号 (长度、constraint 数量) 同样
584	    不具判别性。Inv-length 略高 (+0.50pp, p=0.45): shorter traces 可能稍 more focused, 但效果不显著。Length-weighted
585	    和 constraint-count 略低 (-1pp): longer/more-constrained traces 未必更正确 (可能是 model
586	    在错误路径上 elaborating)。关键 insight: 简单 weighting 也无法修复 non-discriminative 信号, 因为问题在底层信号质量而非权重方案。
587	
588	    '
589	  tables:
590	  - 'Appendix: Weighted SC comparison table'
591	  figures_description:
592	  - 'Appendix bar chart: 五种方法 accuracy 在 ±1pp 内, error bars 全部重叠。'
593	  analysis: 'Weighted SC 是最直接竞争 baseline。All variants ≈ SC 确认: (1) 无简单 weighting 能
594	    rescue method, (2) bottleneck 是 signal quality 非 aggregation sophistication。 SICA
595	    失败不是因为 MaxSAT over-engineering, 而是因为 input signals (constraints) non-discriminative。Any
596	    aggregation over non-discriminative signals degenerates to counting, which ≈ voting。
597	
598	    '
599	- name: constraint_quality_case_studies
600	  plan_id: exp-008
601	  description: '8 representative problems 定性分析: constraints 为何 non-discriminative'
602	  expected_results:
603	    n_case_studies: 8
604	    correct_trace_precision: 0.52
605	    incorrect_trace_precision: 0.48
606	    constraint_overlap_rate: 0.78
607	    typical_constraint_types:
608	    - conditional (if-then)
609	    - universal quantifier (forall)
610	    - negation
611	    - predicate application
612	    discriminative_constraints_pct: 0.12
613	  result_rationale: 'Non-discrimination 的 root cause: LLM 提取的 constraints 主要 formalize
614	    题目 premises (前提条件) 而非 reasoning steps (推理步骤)。Premises 对正确/错误 traces 共享 (都正确读取了题目)——constraint
615	    overlap rate 78%。推理错误发生在 inference chain 更深位置: 这些错误要么不被 formalized (extraction
616	    跳过复杂推导), 要么被 formalized 为看起来合理但语义不同的 constraints (surface structure 相似)。 仅 12%
617	    constraints 是 truly discriminative (只出现在正确或只出现在错误 traces), 且方向随机 (一半 favor correct,
618	    一半 favor incorrect)。
619	
620	    '
621	  tables: []
622	  figures_description:
623	  - 'Appendix case study: side-by-side 正确 trace 和错误 trace 的 constraints。 Highlighted:
624	    shared constraints (majority, ~78%) and trace-specific (minority, ~22%)。 Caption:
625	    ''Most constraints formalize shared premises; trace-specific constraints are equally
626	    likely to support correct or incorrect answers.''
627	
628	    '
629	  analysis: 'Case studies 提供定性理解, 补充 F2 定量证据。Reader 直观看到 WHY precision ≈ 0.50: constraints
630	    capture what the model reads (premises), not how it reasons (inference)。 也解释 WHY
631	    MaxSAT ≈ count-only: 如果 constraints mostly shared, satisfiability structure carries
632	    no information about answer correctness。1-2 examples 进 §4.1, 其余进 appendix。
633	
634	    '
635	- name: temperature_ablation_t03_t05_t10
636	  plan_id: what-if-temp
637	  description: T=0.3/0.5/1.0 on Qwen-14B D012 60q. Temperature 操控 diversity, 验证 trap
638	    结构性
639	  expected_results:
640	    dataset: D012
641	    model: Qwen2.5-14B-Instruct
642	    n: 60
643	    k: 12
644	    t03_c0_pct: 28.3
645	    t03_sc_accuracy: 0.767
646	    t03_sica_accuracy: 0.767
647	    t03_delta_pp: 0.0
648	    t03_discordant_sica: 1
649	    t03_discordant_sc: 1
650	    t03_mcnemar_p: 1.0
651	    t03_extraction_rate: 0.91
652	    t05_c0_pct: 41.7
653	    t05_sc_accuracy: 0.75
654	    t05_sica_accuracy: 0.75
655	    t05_delta_pp: 0.0
656	    t05_discordant_sica: 1
657	    t05_discordant_sc: 1
658	    t05_mcnemar_p: 1.0
659	    t05_extraction_rate: 0.9
660	    t10_c0_pct: 68.3
661	    t10_sc_accuracy: 0.7
662	    t10_sica_accuracy: 0.683
663	    t10_delta_pp: -1.7
664	    t10_discordant_sica: 1
665	    t10_discordant_sc: 2
666	    t10_mcnemar_p: 0.56
667	    t10_extraction_rate: 0.87
668	    baseline_t07_c0_pct: 53.3
669	    baseline_t07_delta_pp: 0.0
670	    c0_monotonic_increase: true
671	    c0_sequence: 28.3% → 41.7% → 53.3% → 68.3%
672	    max_abs_delta_pp: 1.7
673	    all_p_gt_020: true
674	  result_rationale: "Temperature 直接控制 sampling distribution entropy, 因此 C0 随 T 单调递增:\
675	    \ T=0.3 时 logit distribution 尖锐, traces 集中到 modal answer, 仅 17 题多候选; T=1.0 时分布平坦,\
676	    \ 41 题多候选。这是 structural: T→entropy→C0 是因果链。\nSC accuracy 随 T 先平后降: T=0.3-0.7 SC≈73-77%\
677	    \ (集中在正确答案近邻), T=1.0 SC 降到 70% (更多随机错误破坏多数票)。已知 SC behavior。\nSICA-SC gap 在所有\
678	    \ T 下 |Δ| ≤ 1.7pp: - T=0.3 (C0=28%): 仅 17 题多候选, 1 discordant, 1:1 → Δ=0。少数 multi-candidate\n\
679	    \  问题上 constraints 恰好一胜一负。\n- T=0.5 (C0=42%): 25 题多候选, constraints 仍 non-discriminative\
680	    \ → Δ=0。\n  更多 problems 可操作, 但操作方向随机。\n- T=1.0 (C0=68%): 41 题多候选, constraints\
681	    \ 质量因 noisier traces 进一步下降\n  (高温 traces 更长、更散漫, extraction noise 增加) → Δ=-1.7pp。MaxSAT\
682	    \ 在\n  嘈杂 constraints 上做了一次净错误排除。\n\nAll p>0.20 at n=60 (SE≈5-6pp)。True effect\
683	    \ = 0 at all temperatures。\n"
684	  tables:
685	  - '§5 Table: Temperature ablation (T × C0 × SC × SICA × Δ)'
686	  figures_description:
687	  - '§5 Figure (dual-axis): Left y=C0 (blue bars), 单调递增 28→42→53→68。 Right y=SICA-SC
688	    gap (red line+dots), 平坦在 0 附近, error bars 均跨零。 X-axis: T (0.3, 0.5, 0.7, 1.0)。Caption:
689	    ''Increasing temperature monotonically increases output diversity (C0) but does
690	    not improve SICA over SC, confirming the capability trap is structural, not a
691	    tuning failure.''
692	
693	    '
694	  - 'Alternative: 2×2 panel, each T 一个 mini bar chart (SC vs SICA)。 C0 标注在每个 panel
695	    上。Visual: bars 等高, C0 label 递增。
696	
697	    '
698	  analysis: 'Temperature ablation 是论文最强 causal evidence: 通过实验操控 diversity (非仅 跨模型观察),
699	    确认 diversity↑ 不改善 SICA。排除 confounders: 同一模型、同一数据、 只改 T, C0 从 28% 到 68% 连续变化, gap
700	    恒为 0。如 reviewer 问 ''maybe you haven''t found the right diversity level'': this
701	    answers definitively — we swept the full range, it doesn''t help。与 F2 互补: F2 shows
702	    WHY (precision≈0.50), temp ablation shows THAT (gap=0 at all diversity levels)。§5
703	    new evidence for EMNLP submission。
704	
705	    '
706	- name: gsm8k_pilot_30q
707	  plan_id: what-if-gsm8k
708	  description: 等同 exp-012。Qwen-14B on GSM8K 30q, 数学推理域 pilot
709	  expected_results:
710	    note: 同 exp-012, 参见上方 gsm8k_pilot_14b entry
711	    n: 30
712	    k: 12
713	    sica_accuracy: 0.867
714	    sc_accuracy: 0.867
715	    delta_pp: 0.0
716	    multi_candidate_rate: 0.1
717	    extraction_rate: 0.75
718	    model: Qwen2.5-14B-Instruct
719	    dataset: GSM8K
720	  result_rationale: '与 exp-012 相同实验。14B 在 GSM8K accuracy ~87%, C0 ~10%。数学推理的 open-ended
721	    answer space (具体数字) 理论上增加 diversity, 但 14B 能力收敛到正确数值。 Extraction rate 偏低 (75%)
722	    因为数值计算难以 FOL 化。SICA ≡ SC。 作为 appendix cross-domain data point, 为 ''what about
723	    math'' reviewer concern 提供证据。
724	
725	    '
726	  tables:
727	  - 'Appendix: GSM8K row (同 exp-012)'
728	  figures_description:
729	  - 'F4 data point: GSM8K C0=10%, Δ=0'
730	  analysis: '与 exp-012 完全重复。收录条件: 如果 GPU budget 允许, 作为第四个 domain 进入 appendix (主文已有
731	    FOLIO + StrategyQA + ARC + ProofWriter 四域)。'
732	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11d2320a-922e-41b8-b5db-6f54db45f04d",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "3ace886b-4ee8-4e9a-9129-30a7c11dcec3",
  "sourceToolAssistantUUID": "11d2320a-922e-41b8-b5db-6f54db45f04d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T16:00:01.658Z_

<details><summary>↩ Tool result · `toolu_01MJSjjo8HpwKmEfCMfukbE9`</summary>

```text
1	---
2	dream_id: dream_20260517T144412
3	tier: best
4	overall_score: 3.5/6 Borderline
5	timestamp: 2026-05-17T15:52:43.986152+00:00
6	---
7	
8	# Dream Review Report: "The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning"
9	
10	**dream_id:** 20260517T144412
11	**Review mode:** full (2 Reviewers, complete roundtable)
12	**Date:** 2026-05-17
13	
14	---
15	
16	## Roundtable Summary
17	
18	| Reviewer | Focus | Independent Score | Post-Roundtable Score | Confidence |
19	|----------|-------|------------------|-----------------------|------------|
20	| R1 | Methods + Experiments | 4/6 (Weak Accept) | 4/6 (Weak Accept) | 4/5 |
21	| R2 | Novelty + Related Work | 3/6 (Weak Reject) | 3/6 (Weak Reject) | 4/5 |
22	| **Consensus** | | | **3.5/6 (Borderline)** | **4/5** |
23	
24	---
25	
26	## Step 1: Independent Reviews
27	
28	### R1 (Methods + Experiments)
29	
30	**Strengths identified:**
31	- S1: The constraint ablation (Table 3) is the paper's strongest evidence. MAX-SAT, count-only, and random-weight produce 802/804 identical answers (McNemar p=0.99). This convincingly demonstrates the solver adds no value beyond counting.
32	- S2: Per-problem constraint precision analysis (n=307, mean=0.505, flat regression slope=0.003 against vote entropy) is methodologically sound and establishes the mechanism at fine granularity.
33	- S3: Honest negative result. The authors' pivot from seeking positive results to diagnosing failure lends credibility.
34	- S4: C0 as a practitioner-facing diagnostic is simple and actionable.
35	- S5: Overhead analysis (49% wall-time for zero gain, solver <0.01% of time) is a useful practical contribution.
36	- S6: Qualitative analysis (Section 6.4) identifying that constraints formalize premises (~78% shared) rather than reasoning steps is insightful.
37	
38	**Weaknesses identified:**
39	- W1 (Major): **Underpowered non-central experiments.** 8 of 9 conditions use n≤60 (SE ≈ 5-8pp). These experiments have <15% power to detect effects of 3pp. The combined N>1,300 figure is misleading because 804 come from one model on one domain. The paper draws sweeping conclusions from experiments that cannot detect effects smaller than ~10pp.
40	- W2 (Major): **Self-extraction confound.** The same model generates traces and extracts constraints. A model that makes a reasoning error will likely extract constraints consistent with that error. Without testing a stronger/separate extraction model, the paper cannot distinguish "symbolic consensus is fundamentally limited" from "LLM self-extraction of constraints is limited."
41	- W3 (Major): **Domain imbalance.** SICA is genuinely tested (C0>20%) almost exclusively on formal logic (FOLIO+ProofWriter). On StrategyQA (C0=10%), ARC (C0=5%), and GSM8K (C0=10%), the model's high accuracy suppresses diversity, making these conditions uninformative about the method's potential. Claiming "3 domains" is technically true but substantively misleading.
42	- W4 (Moderate): **Broken figure cross-references.** F2 (hero scatter plot) and F4 (C0 vs gap) are referenced as "Figure ??" in the text, indicating broken LaTeX references. The paper's most important visualizations may not be rendered.
43	- W5 (Moderate): **8 references** is far below venue standards.
44	- W6 (Minor): C0 thresholds (<5%, >20%) are empirically derived from limited data. Generalization to other models/domains/formalisms is unknown.
45	
46	**R1 Questions for Authors:**
47	1. Have you considered using a stronger model for constraint extraction while keeping the trace generation model constant?
48	2. How does constraint precision vary across the other 4 models (not just Qwen-14B)?
49	3. Have you considered running the temperature ablation at powered sample sizes (n=804)?
50	4. The framing document references Mistral-7B (n=60, Δ=0.0) but this does not appear in Table 1. Was this experiment completed?
51	5. For the 2 problems where MAX-SAT and count-only disagree, can you characterize what makes them different?
52	
53	### R2 (Novelty + Related Work)
54	
55	**Strengths identified:**
56	- S1: Clear narrative structure (problem → method → negative result → mechanism → diagnostic).
57	- S2: The mechanism analysis is a genuine empirical insight. The combination of per-problem precision and constraint ablation provides convincing evidence for why the method fails.
58	- S3: Honest framing of negative results is commendable.
59	- S4: Tables are well-formatted with consistent precision and appropriate statistical tests.
60	
61	**Weaknesses identified:**
62	- W1 (Major): **Limited novelty.** The capability trap is a useful label but the underlying finding is expected. Logic-LM and LINC already document that LLM-to-FOL translation is error-prone. That aggregating noisy extractions across K traces does not produce discriminative signal follows predictably. The diversity-quality tension is a well-known property of LLM scaling.
63	- W2 (Major): **Over-generalized claims.** The title "Why Symbolic Consensus Cannot Beat Majority Voting" implies a general impossibility result, but only one specific pipeline (LLM self-extracted FOL + MAX-SAT) is tested. Other symbolic methods (DyLoS, Aristotle, FoVer, LogicAgent) reportedly achieve gains on the same benchmarks (FOLIO, ProofWriter). The paper conflates "our method doesn't work" with "this class of methods can't work."
64	- W3 (Major): **8 references is critically below venue standards** (EMNLP expects 30-60). Missing critical citations include:
65	  - Loo et al. 2025 (SC scaling plateaus) — directly contextualizes QwQ-32B finding
66	  - Snell et al. 2025 (test-time compute scaling, ICLR Oral) — contextualizes diversity-capability relationship
67	  - DyLoS (EACL 2026), FoVer (TACL 2025), Aristotle (ACL 2025) — neuro-symbolic methods that work on FOLIO/ProofWriter
68	  - DeepSeek-R1 technical report — essential for reasoning model characterization
69	  - Taubenfeld et al. 2025 (confidence-weighted SC) — the paper cites their 2024 debate biases paper instead
70	  - Wan et al. 2024 (RASC), LogicAgent, SATBench, etc.
71	- W4 (Major): **No figures rendered.** The hero scatter plot (F2) and C0-vs-gap plot (F4) are described textually but not included. For a paper whose central claim is about diversity-quality relationships, this is a serious presentation failure.
72	- W5 (Moderate): **C0 diagnostic is trivially obvious** as a metric (it is the multi-candidate rate that SC already computes). The paper's own regression (slope=-0.02, r²=0.06, p=0.40) shows C0 has no continuous predictive power, only binary filter value.
73	- W6 (Moderate): **Temperature ablation labeled "causal" is confounded.** Temperature simultaneously affects diversity, trace quality (SC drops 76.7→70.0%), and extraction quality (rate drops 91→87%). The null gap at high temperature could reflect worse constraints from noisier traces, not a structural limitation.
74	- W7 (Moderate): **The paper attacks a method (SICA) the authors themselves designed.** No established community is building on this paradigm, limiting the practical impact of disproving it.
75	
76	**R2 Questions for Authors:**
77	1. How do you reconcile "symbolic consensus cannot beat majority voting" with DyLoS, Aristotle, and FoVer achieving gains on the exact same benchmarks?
78	2. Why not use FOLIO's gold FOL annotations as an oracle to separate extraction failure from aggregation failure?
79	3. Is the Taubenfeld citation intentionally the 2024 debate biases paper, or should it be the 2025 confidence-weighted SC paper?
80	4. The constraint-sharing analysis (78% shared, 12% discriminative) covers only 8 problems. Has this been verified at scale?
81	5. Have you considered comparison against a Best-of-N with an off-the-shelf reward model?
82	
83	---
84	
85	## Step 2: Cross-Sharing
86	
87	R1 and R2 exchanged reviews. Key reactions:
88	
89	**R1 on R2's points:** R1 agrees that the reference count is critically low and that the over-generalization of claims is a substantive issue, not just a framing issue. R1 acknowledges the importance of comparing against methods that demonstrably work on FOLIO/ProofWriter. R1 maintains that the empirical mechanism analysis has independent value even if the finding is "expected."
90	
91	**R2 on R1's points:** R2 agrees that the constraint ablation (802/804) and per-problem precision analysis are methodologically strong. R2 emphasizes that even this strong mechanism evidence is weakened by the self-extraction confound: the ablation shows SICA's specific constraints are vacuous, not that all possible constraint-based aggregation is vacuous.
92	
93	---
94	
95	## Step 3: Convergence
96	
97	### Points of Agreement (Strong Consensus)
98	
99	1. **The mechanism analysis is the paper's core contribution.** Both reviewers agree that the combination of per-problem constraint precision (Table 2, n=307, mean=0.505) and the constraint ablation (Table 3, 802/804 agreement) provides convincing evidence that, in the tested configuration, MAX-SAT optimization degenerates to counting. This is empirically well-executed.
100	
101	2. **8 references is a critical deficiency.** Both reviewers independently flagged this as unacceptable for a top venue. The paper's own literature map identifies 25+ relevant papers, most absent from the submission.
102	
103	3. **The self-extraction confound is a major unaddressed gap.** Using the same model for trace generation and constraint extraction conflates extraction quality with aggregation limitations. Without a stronger/separate extractor or gold-FOL oracle experiment, the paper cannot distinguish "symbolic consensus is fundamentally limited" from "LLM self-extraction is limited."
104	
105	4. **Claims substantially exceed evidence.** The title generalizes to "symbolic consensus" but only one pipeline is tested. The domain coverage claim ("3 domains") is undermined by the fact that non-logic domains have C0<10%, making them uninformative. The "N>1,300" figure is dominated by one model on one domain pair.
106	
107	5. **Missing figures are a serious gap.** The hero figure (F2) and diagnostic plot (F4) are referenced but not rendered, creating broken cross-references and eliminating the paper's most important visual evidence.
108	
109	6. **Non-central experiments are underpowered.** 8 of 9 conditions at n≤60 cannot detect effects smaller than ~10pp. The paper's breadth-over-depth design trades statistical power for model/domain coverage, but the resulting evidence is too thin to support the sweeping conclusions drawn.
110	
111	### Point of Disagreement
112	
113	**C0 diagnostic value and overall score:**
114	- R1 views C0 as a simple but practically useful contribution (the binary classification into degenerate/trapped regimes provides clear guidance). Combined with the mechanism analysis, R1 sees enough value for a borderline accept (4/6).
115	- R2 views C0 as trivially obvious (the multi-candidate rate is already implicit in SC) and the finding as largely expected from prior work on FOL extraction noise. Combined with the thin references and over-generalized claims, R2 sees the paper below the acceptance bar (3/6).
116	
117	**Resolution:** Both reviewers acknowledge the other's position as reasonable. The disagreement reflects different weighting of "practical value of systematic negative result" (R1) vs. "novelty bar for top venue" (R2). The consensus score is 3.5/6 (borderline), with the paper's fate hinging on whether the venue values systematic empirical work on negative results or demands higher conceptual novelty.
118	
119	---
120	
121	## Step 4: Consolidated Assessment
122	
123	### Overall Score: 3.5/6 (Borderline Reject-Accept)
124	
125	### Confidence: 4/5
126	
127	### Meta-Review
128	
129	This paper presents a systematic study of Symbolic Invariant Consensus Aggregation (SICA) and finds it provides no accuracy gain over Self-Consistency (majority voting) across multiple models and domains. The core mechanism analysis is well-executed: the constraint ablation (MAX-SAT ≈ count-only ≈ random-weight, 802/804 agreement) and per-problem precision analysis (mean=0.505, flat against vote entropy) convincingly demonstrate that, in the tested configuration, LLM-extracted FOL constraints lack discriminative power and the MAX-SAT solver degenerates to counting.
130	
131	However, the paper has several critical issues that prevent a clear recommendation for acceptance:
132	
133	**1. Scope-evidence mismatch (both reviewers, highest priority).** The title and claims generalize to "symbolic consensus" broadly, but evidence covers one specific pipeline. Other symbolic methods (DyLoS, Aristotle, FoVer) reportedly achieve gains on the same benchmarks. The self-extraction confound means the paper demonstrates "LLM self-extracted FOL constraints are vacuous" rather than "symbolic consensus is impossible." This distinction is fundamental to the paper's contribution and must be addressed.
134	
135	**2. Critically thin scholarship (both reviewers).** 8 references is unacceptable. The paper omits directly relevant work on SC scaling (Loo et al. 2025), test-time compute (Snell et al. 2025), neuro-symbolic methods that work on the tested benchmarks (DyLoS, FoVer, Aristotle), and reasoning models (DeepSeek-R1). The Related Work section at ~0.5 pages is insufficient for positioning at the intersection of self-consistency, neuro-symbolic reasoning, and test-time compute.
136	
137	**3. Missing figures (both reviewers).** The hero scatter plot (F2) and C0-vs-gap plot (F4) are described textually but not rendered, with broken LaTeX cross-references ("Figure ??"). These are the paper's most important visualizations.
138	
139	**4. Statistical power limitations (R1 primary, R2 concurs).** The powered experiment (n=804, Qwen-14B, FOLIO+PW) is strong, but 8 other conditions at n≤60 cannot detect effects under ~10pp. The "3 domains" claim is undermined by degenerate C0 on non-logic domains.
140	
141	**5. Novelty concerns (R2 primary).** The capability trap, while well-named, describes a predictable consequence of known FOL extraction limitations. The C0 diagnostic has limited incremental value.
142	
143	### Actionable Recommendations (Priority Order)
144	
145	1. **Narrow claims to match evidence.** Retitle to specify the tested pipeline (e.g., "LLM-Extracted FOL Constraints" not "Symbolic Consensus"). Acknowledge methods that achieve gains on the same benchmarks and explain why SICA's failure does not generalize.
146	
147	2. **Expand references to 30+.** The project's own literature map provides the missing citations. At minimum add: Loo et al. 2025, Snell et al. 2025, DeepSeek-R1 report, DyLoS, FoVer, Aristotle, Taubenfeld et al. 2025 (correct citation), LogicAgent.
148	
149	3. **Include F2 and F4 as actual rendered figures.** Fix the LaTeX cross-references. These visualizations are critical to the paper's argument.
150	
151	4. **Add a gold-FOL oracle experiment** (FOLIO provides human-authored FOL). This would definitively separate extraction failure from aggregation failure and is the single experiment most likely to change the paper's contribution level.
152	
153	5. **Add a stronger-extractor control.** Use a larger model (e.g., 72B or a frontier model) for constraint extraction while keeping 14B for trace generation. This tests whether extraction quality is the binding constraint.
154	
155	6. **Run powered temperature ablation.** Repeat T=0.3 and T=1.0 on the full n=804 dataset to transform the causal claim from suggestive to definitive.
156	
157	7. **Report QwQ-32B accuracy values in Table 1** (currently shown as "--").
158	
159	8. **Include Mistral-7B results** if available (referenced in framing documents but absent from paper).
160	
161	### Experiment Coverage Assessment
162	
163	Compared to the 16 planned experiments in the review context:
164	
165	| Experiment | In Paper? | Coverage Quality |
166	|-----------|-----------|-----------------|
167	| sica_k_ablation_14b (exp-002) | Yes (Table 5) | Adequate, n=60 |
168	| tiebreak_baseline (exp-003) | Yes (Table 4) | Adequate |
169	| sica_constraint_ablation (exp-013) | Yes (Table 3) | Strong, n=804 |
170	| sica_strategyqa_14b (exp-017) | Yes (Table 1) | Weak, C0=10% degenerate |
171	| sica_arc_challenge_14b (exp-018) | Yes (Table 1) | Weak, C0=5% degenerate |
172	| constraint_quality_correlation (exp-019) | Yes (Table 2) | Strong, n=307 |
173	| sica_7b_scaling (exp-004) | Yes (Table 1, 7) | Adequate |
174	| qwq_32b_operating_regime (exp-005) | Yes (Table 1, App A.1) | Adequate |
175	| c0_diagnostic_validation (exp-006) | Partial (Section 6.1, no figure) | Missing F4 figure |
176	| sica_72b_awq (exp-007) | Yes (Table 1, 7) | Adequate |
177	| overhead_analysis (exp-009) | Yes (Section 6.3) | Adequate |
178	| sica_llama_8b (exp-011) | Yes (Table 1) | Adequate, n=60 |
179	| gsm8k_pilot_14b (exp-012) | Yes (App A.3) | Weak, n=30 pilot |
180	| sica_deepseek_r1 (exp-014) | Yes (Table 1) | Adequate |
181	| logic_lm_baseline (exp-015) | Yes (Section 6.2) | Adequate |
182	| weighted_sc_baseline (exp-016) | Yes (Section 6.2) | Adequate |
183	| temperature_ablation (what-if-temp) | Yes (Table 6, Section 5) | Adequate, n=60 |
184	| case_studies (exp-008) | Partial (Section 6.4) | Text only, no figure |
185	
186	Coverage is generally good (16/16 experiments represented), but several lack rendered figures and some key conditions are underpowered or degenerate. The paper benefits from breadth but would benefit more from depth on 2-3 critical experiments.
187	
188	### Final Verdict
189	
190	The paper has a solid empirical core (Tables 2-3) but needs significant revision in claim scoping, scholarship, and presentation before it meets the bar for a top ML venue. The mechanism analysis is publishable-quality work wrapped in over-generalized framing with critically thin references and missing figures. With the recommended revisions (especially items 1-5), this could become a solid contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a0bd124-ee9c-4a6f-a6e0-3cf14bdee719",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "1a45549d-117a-4650-a7b5-7b4e7378334e",
  "sourceToolAssistantUUID": "6a0bd124-ee9c-4a6f-a6e0-3cf14bdee719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-17T16:00:11.780Z_

Now let me also read the project's ideas and memory files for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a45549d-117a-4650-a7b5-7b4e7378334e",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RGkkke5qpw4Baohc3Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0b65fb9-4261-455e-9bf4-03dd470eff36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2y6hdmLduf47y9Sg1njVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23962,
      "cache_read_input_tokens": 31905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23962,
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

_source line 21 · 2026-05-17T16:00:11.881Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NL1CFYjHuiJ2rbmusE52Ty`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0b65fb9-4261-455e-9bf4-03dd470eff36",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RGkkke5qpw4Baohc3Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f39a1c2-f6d4-48f5-a0ec-c2bf593b6d05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2y6hdmLduf47y9Sg1njVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23962,
      "cache_read_input_tokens": 31905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23962,
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

_source line 22 · 2026-05-17T16:00:11.884Z_

<details><summary>↩ Tool result · `toolu_01NL1CFYjHuiJ2rbmusE52Ty`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f39a1c2-f6d4-48f5-a0ec-c2bf593b6d05",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "c70f41b3-5468-458b-8399-319bb02b1628",
  "sourceToolAssistantUUID": "7f39a1c2-f6d4-48f5-a0ec-c2bf593b6d05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-17T16:00:14.189Z_



Let me read the literature map and memory files for additional context on related work coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c70f41b3-5468-458b-8399-319bb02b1628",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RHWWHSa7DgPP2J4xej",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "378fb3b3-08f2-49f2-a180-cb8a97206547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4TFDicn1SuCiqztHyVpsp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 55867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 450,
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

_source line 24 · 2026-05-17T16:00:15.146Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Dp1SufFw54mbVJTavtu5yk`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "378fb3b3-08f2-49f2-a180-cb8a97206547",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RHWWHSa7DgPP2J4xej",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "656dc3b8-45a5-4d2f-a0dc-4e6c889b57ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4TFDicn1SuCiqztHyVpsp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 55867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 450,
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

_source line 25 · 2026-05-17T16:00:15.171Z_

<details><summary>↩ Tool result · `toolu_01Dp1SufFw54mbVJTavtu5yk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml\", \"content\": \"# Literature Map — symb_invariant_consensus (SICA)\\n# Last updated: 2026-05-16\\n# Purpose: Track related work coverage for EMNLP 2026 submission\\n\\ndimensions:\\n\\n  self_consistency_and_variants:\\n    description: \\\"Self-Consistency (SC) decoding and improvements\\\"\\n    papers:\\n      - id: wang2023sc\\n        title: \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\"\\n        authors: \\\"Wang et al.\\\"\\n        venue: \\\"ICLR 2023\\\"\\n        arxiv: \\\"2203.11171\\\"\\n        relevance: \\\"Foundational SC method; our primary baseline\\\"\\n        status: must_cite\\n\\n      - id: chen2024usc\\n        title: \\\"Universal Self-Consistency for Large Language Model Generation\\\"\\n        authors: \\\"Chen et al.\\\"\\n        venue: \\\"ICML 2024\\\"\\n        arxiv: \\\"2311.17311\\\"\\n        relevance: \\\"Extends SC to free-form answers via LLM-based selection; alternative aggregation\\\"\\n        status: must_cite\\n\\n      - id: taubenfeld2025cisc\\n        title: \\\"Confidence Improves Self-Consistency in LLMs\\\"\\n        authors: \\\"Taubenfeld et al.\\\"\\n        venue: \\\"ACL Findings 2025\\\"\\n        arxiv: \\\"2502.06233\\\"\\n        relevance: \\\"Weighted voting via model confidence; reduces samples 40-50%. Shows SC can be improved with non-uniform weighting — SICA uses constraint-based weighting instead\\\"\\n        status: must_cite\\n\\n      - id: kim2026reasc\\n        title: \\\"Reliability-Aware Adaptive Self-Consistency (ReASC)\\\"\\n        authors: \\\"Kim et al.\\\"\\n        venue: \\\"2026\\\"\\n        relevance: \\\"Response-level confidence for early halting; 70-80% cost saving vs naive SC\\\"\\n        status: should_cite\\n\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — shows SC gains plateau early and can decline at high sample counts for strong models. Directly supports our QwQ-32B finding (SICA≡SC when model is too consistent)\\\"\\n        status: must_cite\\n\\n      - id: wan2024rasc\\n        title: \\\"Reasoning-Aware Self-Consistency (RASC)\\\"\\n        authors: \\\"Wan et al.\\\"\\n        venue: \\\"2024\\\"\\n        relevance: \\\"Combines answer-level and rationale-level features; reduces samples ~88%\\\"\\n        status: should_cite\\n\\n      - id: dsc2025\\n        title: \\\"Difficulty-Adaptive Self-Consistency\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL Findings 2025\\\"\\n        relevance: \\\"Ranks problem difficulty to allocate sampling budget; complementary efficiency approach\\\"\\n        status: optional\\n\\n  symbolic_reasoning_llm:\\n    description: \\\"Neuro-symbolic methods combining LLMs with formal solvers\\\"\\n    papers:\\n      - id: pan2023logiclm\\n        title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n        authors: \\\"Pan et al.\\\"\\n        venue: \\\"EMNLP Findings 2023\\\"\\n        arxiv: \\\"2305.12295\\\"\\n        relevance: \\\"LLM→FOL→solver pipeline; closest architectural ancestor to SICA. Key difference: Logic-LM uses single-path translation, SICA aggregates across multiple paths\\\"\\n        status: must_cite\\n\\n      - id: xu2026dylos\\n        title: \\\"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)\\\"\\n        authors: \\\"Xu et al.\\\"\\n        venue: \\\"EACL 2026\\\"\\n        arxiv: \\\"2510.06774\\\"\\n        relevance: \\\"Multi-paradigm solver selection (LP/FOL/CSP/SMT); evaluated on FOLIO+ProofWriter. Outperforms Logic-LM. Key difference: DyLoS selects solver type, SICA aggregates constraints across paths\\\"\\n        status: must_cite\\n\\n      - id: fover2025\\n        title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"TACL 2025\\\"\\n        relevance: \\\"FOL verification for NL reasoning; strong results on ProofWriter+FOLIO. Uses verification rather than aggregation\\\"\\n        status: must_cite\\n\\n      - id: li2025survey\\n        title: \\\"A Survey on LLM Symbolic Reasoning\\\"\\n        authors: \\\"Li et al.\\\"\\n        venue: \\\"2025 (under review)\\\"\\n        relevance: \\\"Comprehensive survey; positions SICA within the broader landscape\\\"\\n        status: should_cite\\n\\n      - id: constraintllm2025\\n        title: \\\"ConstraintLLM: A Neuro-Symbolic Framework for Industrial Constraint Programming\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Multi-instruction SFT for constraint extraction; different domain (industrial) but related extraction methodology\\\"\\n        status: optional\\n\\n  maxsat_constraint_nlp:\\n    description: \\\"MAX-SAT and constraint satisfaction applied to NLP/reasoning\\\"\\n    papers:\\n      - id: llm_meets_cp2025\\n        title: \\\"Large Language Model Meets Constraint Propagation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"IJCAI 2025\\\"\\n        relevance: \\\"LLM+constraint propagation integration; validates feasibility of constraint-based reasoning with LLMs\\\"\\n        status: should_cite\\n\\n      - id: satbench2025\\n        title: \\\"SATBench: Benchmarking LLMs' Logical Reasoning via SAT Problems\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Evaluates LLMs on SAT-formulated problems; establishes that LLMs struggle with pure SAT but can benefit from solver integration\\\"\\n        status: should_cite\\n\\n      - id: maxsat_local_search2025\\n        title: \\\"Optimizing Local Search-based Partial MaxSAT Solving via Initial Assignment Prediction\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Science China Information Sciences 2025\\\"\\n        relevance: \\\"Solver-side advances in partial MaxSAT; technical reference for our WPMS formulation\\\"\\n        status: optional\\n\\n  folio_proofwriter_sota:\\n    description: \\\"State-of-the-art methods on FOLIO and ProofWriter benchmarks\\\"\\n    papers:\\n      - id: logicagent2025\\n        title: \\\"From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning (LogicAgent)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2509.24765\\\"\\n        relevance: \\\"Multi-perspective logical reasoning; SOTA on logical reasoning benchmarks including FOLIO. +7.05% average gain\\\"\\n        status: must_cite\\n\\n      - id: aristotle2025\\n        title: \\\"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"ACL 2025\\\"\\n        relevance: \\\"Logic-complete decomposition framework; strong ProofWriter/FOLIO results\\\"\\n        status: must_cite\\n\\n      - id: qi2025symbolic_provers\\n        title: \\\"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation\\\"\\n        authors: \\\"Qi et al.\\\"\\n        venue: \\\"ICLR 2025\\\"\\n        arxiv: \\\"2502.06563\\\"\\n        relevance: \\\"LLM+symbolic prover combination; evaluated on FOLIO\\\"\\n        status: should_cite\\n\\n      - id: dissecting2025\\n        title: \\\"Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP Findings 2025\\\"\\n        arxiv: \\\"2506.04810\\\"\\n        relevance: \\\"Fine-grained analysis of LLM logical reasoning capabilities on ProofWriter/FOLIO\\\"\\n        status: optional\\n\\n  reasoning_model_diversity:\\n    description: \\\"Trace diversity in reasoning vs non-reasoning models; supports our QwQ-32B finding\\\"\\n    papers:\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — strong models produce near-identical paths, SC gains plateau/decline. Direct support for SICA≡SC on QwQ-32B\\\"\\n        status: must_cite\\n\\n      - id: diversity_aware_tts2025\\n        title: \\\"Diversity-Aware Training for Test-Time Scaling\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Under review 2025\\\"\\n        relevance: \\\"Independent reasoning attempts collapse into similar solutions; diversity training needed to unlock test-time scaling. Supports our claim that non-reasoning models have more useful diversity\\\"\\n        status: must_cite\\n\\n      - id: snell2025scaling_tts\\n        title: \\\"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters\\\"\\n        authors: \\\"Snell et al.\\\"\\n        venue: \\\"ICLR 2025 (Oral)\\\"\\n        arxiv: \\\"2408.03314\\\"\\n        relevance: \\\"Foundational test-time compute scaling; shows compute-optimal strategies vary by difficulty. Contextualizes why SICA needs diverse paths\\\"\\n        status: should_cite\\n\\n      - id: deepseek_r1_2025\\n        title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n        authors: \\\"DeepSeek-AI\\\"\\n        venue: \\\"Nature 2025\\\"\\n        arxiv: \\\"2501.12948\\\"\\n        relevance: \\\"Defines the reasoning model paradigm (RL-trained extended thinking); reference for why these models are highly self-consistent\\\"\\n        status: must_cite\\n\\n      - id: base_models_reason2025\\n        title: \\\"Base Models Know How to Reason, Thinking Models Learn When\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.07364\\\"\\n        relevance: \\\"RL teaches activation timing not new skills; implies reasoning models converge to similar reasoning patterns, reducing trace diversity\\\"\\n        status: should_cite\\n\\n      - id: korikov2025sc_ranking\\n        title: \\\"The Impact of LLM Self-Consistency and Reasoning Effort on Automated Scoring\\\"\\n        authors: \\\"Korikov et al.\\\"\\n        venue: \\\"arXiv 2026\\\"\\n        arxiv: \\\"2604.26954\\\"\\n        relevance: \\\"Temperature sampling helps but ensemble size (1→7) produces no significant gains; supports diminishing returns of naive SC\\\"\\n        status: optional\\n\\n  multi_path_aggregation:\\n    description: \\\"Methods for aggregating multiple reasoning paths beyond majority voting\\\"\\n    papers:\\n      - id: rc2025\\n        title: \\\"Representation Consistency for Accurate and Coherent LLM Answer Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2506.21590\\\"\\n        relevance: \\\"Aggregation via representation similarity; down-weights incoherent reasoning. Semantic alternative to SICA's symbolic approach\\\"\\n        status: should_cite\\n\\n      - id: multi_path_plan2025\\n        title: \\\"Enhancing Long Chain-of-Thought Reasoning through Multi-Path Plan Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.11620\\\"\\n        relevance: \\\"Multi-path aggregation at plan level rather than answer level\\\"\\n        status: optional\\n\\n      - id: crest2025\\n        title: \\\"Improving LLMs' Reasoning with Consistency-Driven Self-Training (CREST)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL 2025\\\"\\n        relevance: \\\"Consistency as training signal rather than inference-time aggregation\\\"\\n        status: optional\\n\\ngaps:\\n  resolved: []\\n  remaining:\\n    - dimension: \\\"reasoning_model_diversity\\\"\\n      gap: \\\"No published paper explicitly studies QwQ-32B trace diversity collapse under temperature sampling. Our empirical finding (3.6% multi-candidate across 83 problems) is novel but needs positioning against Loo et al. 2025 and Diversity-Aware TTS\\\"\\n    - dimension: \\\"maxsat_constraint_nlp\\\"\\n      gap: \\\"No direct precedent for weighted partial MAX-SAT as multi-path consensus mechanism in NLI. SICA's formulation appears novel — must frame clearly in Related Work\\\"\\n    - dimension: \\\"self_consistency_and_variants\\\"\\n      gap: \\\"Should verify if CRAFT (mentioned in project docs) is a real published method or internal shorthand\\\"\\n\", \"total_chars\": 11286, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "656dc3b8-45a5-4d2f-a0dc-4e6c889b57ff",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "96b92931-e4e3-4222-bcc8-00d4d21f6c61",
  "sourceToolAssistantUUID": "656dc3b8-45a5-4d2f-a0dc-4e6c889b57ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T16:00:15.434Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GVKJkC3bE7uvVhy3kTQbrd`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96b92931-e4e3-4222-bcc8-00d4d21f6c61",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RHWWHSa7DgPP2J4xej",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f00652c7-69f8-4ffd-9b63-fdc969e82c9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4TFDicn1SuCiqztHyVpsp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 55867,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 450
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 220,
          "cache_read_input_tokens": 55867,
          "cache_creation_input_tokens": 450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 450,
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

_source line 27 · 2026-05-17T16:00:15.455Z_

<details><summary>↩ Tool result · `toolu_01GVKJkC3bE7uvVhy3kTQbrd`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f00652c7-69f8-4ffd-9b63-fdc969e82c9a",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "38e466c8-b789-4599-8570-b54ad9113303",
  "sourceToolAssistantUUID": "f00652c7-69f8-4ffd-9b63-fdc969e82c9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-17T16:00:19.649Z_

Now I have a thorough understanding of the paper, its experimental data, framing, and literature context. Let me also check the median paper version to see if there are differences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38e466c8-b789-4599-8570-b54ad9113303",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RHmhLaqfBGyycs5D6v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "291984e5-94c4-4b69-b6db-2093e7fff329",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFDuRSYUpBEZFohn7fP96B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4390,
      "cache_read_input_tokens": 56317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4390,
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

_source line 29 · 2026-05-17T16:00:21.963Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bj5T89xHyNwTZhzv8rN9op`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/median/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "291984e5-94c4-4b69-b6db-2093e7fff329",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RHmhLaqfBGyycs5D6v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d815d10-50ce-48e5-8cfb-c6a3bc71d974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFDuRSYUpBEZFohn7fP96B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4390,
      "cache_read_input_tokens": 56317,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4390
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 56317,
          "cache_creation_input_tokens": 4390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4390,
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

_source line 30 · 2026-05-17T16:00:21.978Z_

<details><summary>↩ Tool result · `toolu_01Bj5T89xHyNwTZhzv8rN9op`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{xcolor}
8	\usepackage{hyperref}
9	\usepackage{multirow}
10	\usepackage{caption}
11	\usepackage{subcaption}
12	\usepackage[margin=2.5cm]{geometry}
13	\usepackage{enumitem}
14	\usepackage{natbib}
15	\bibliographystyle{plainnat}
16	
17	\newcommand{\sica}{\textsc{Sica}}
18	\newcommand{\scm}{\textsc{SC}}
19	\newcommand{\czero}{C_0}
20	
21	\title{The Capability Trap: Why Symbolic Consensus\\Cannot Beat Majority Voting for LLM Reasoning}
22	
23	\author{Anonymous}
24	\date{}
25	
26	\begin{document}
27	\maketitle
28	
29	% ============================================================
30	% ABSTRACT
31	% ============================================================
32	\begin{abstract}
33	Recent work proposes augmenting Large Language Model (LLM) reasoning with symbolic methods: extracting formal constraints from reasoning traces and using satisfiability solvers for answer aggregation. We investigate when such methods outperform simple majority voting (Self-Consistency, SC). We instantiate symbolic consensus as \sica{} (Symbolic Invariant Consensus Aggregation), which extracts first-order logic (FOL) constraints from sampled reasoning traces and aggregates them via weighted MAX-SAT. Across 5 models spanning three architecture classes (instruction-tuned, distilled-reasoning, full-reasoning), 6 reasoning domains, and over 1,300 test problems, we find that \sica{} provides no significant accuracy gain over SC. The accuracy gap ranges from $-3.3$ to $+5.0$ percentage points across conditions, with no result reaching $p < 0.10$. A constraint ablation reveals the mechanism: MAX-SAT, simple constraint counting, and random-weight aggregation agree on 99.4\% of problems, confirming that extracted constraints lack discriminative power. We term this the \emph{capability trap}: instruction-scale models produce diverse outputs (multi-candidate rate 38--62\%) but non-discriminative constraints (precision $\approx 0.54$), while reasoning models eliminate diversity entirely ($\czero < 5\%$). We propose $\czero$ (the fraction of problems with multiple candidate answers) as a zero-cost binary gate: when $\czero < 5\%$, symbolic consensus degenerates to majority voting and can be skipped.
34	\end{abstract}
35	
36	% ============================================================
37	% 1. INTRODUCTION
38	% ============================================================
39	\section{Introduction}
40	
41	Sampling multiple reasoning traces from an LLM and aggregating their answers via majority voting, known as Self-Consistency (SC), is a simple and effective strategy for improving accuracy on reasoning tasks. A natural question is whether more sophisticated aggregation can do better. Several recent methods propose extracting symbolic representations (formal constraints, logic programs, verification conditions) from reasoning traces and using solvers to select answers. The intuition is appealing: formal reasoning should catch errors that voting misses.
42	
43	But when does this actually help? Despite growing interest in neuro-symbolic reasoning pipelines, no prior work systematically characterizes the conditions under which symbolic aggregation outperforms voting. Individual papers report gains on specific benchmarks, but the interaction between model capability, output diversity, and constraint quality remains unexplored.
44	
45	We address this gap with a large-scale empirical study. We instantiate symbolic consensus as \sica{} (Symbolic Invariant Consensus Aggregation), a method that extracts FOL constraints from each sampled reasoning trace and selects the answer that satisfies the maximum weighted set of constraints via a MAX-SAT solver. We evaluate \sica{} against SC across 5 models (Qwen-7B/14B/72B, LLaMA-8B, QwQ-32B), 6 reasoning domains (ProofWriter, FOLIO, StrategyQA, ARC-Challenge, GSM8K, AIME), and over 1,300 problems.
46	
47	The results are uniformly negative. No model-domain combination yields a significant accuracy gain for \sica{} over SC. More importantly, a constraint ablation experiment reveals \emph{why}: MAX-SAT optimization over the extracted constraints produces identical answers to simple constraint counting on 99.4\% of problems (801/804). The solver's satisfiability reasoning contributes nothing because the constraints themselves lack discriminative power, with mean precision near chance at 0.54.
48	
49	We identify a structural explanation that we term the \emph{capability trap}. Symbolic consensus requires two ingredients: (1) output diversity, so there are multiple candidate answers for the solver to adjudicate, and (2) discriminative constraints, so the solver can correctly distinguish answers. These requirements are empirically incompatible across the tested conditions and model scales. Instruction-scale models produce abundant diversity (multi-candidate rate 38--62\%) but their constraints are near-random. Full reasoning models produce high-quality reasoning chains but eliminate diversity entirely (multi-candidate rate $<5\%$), making symbolic aggregation degenerate to voting.
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d815d10-50ce-48e5-8cfb-c6a3bc71d974",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "4bd44448-44ef-4832-a110-125b6eb98a9c",
  "sourceToolAssistantUUID": "1d815d10-50ce-48e5-8cfb-c6a3bc71d974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T16:00:26.298Z_

I now have comprehensive understanding of the paper. Let me now write my review, and then submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bd44448-44ef-4832-a110-125b6eb98a9c",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RJFadLPqNuYcCk7Npu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50274b44-9258-44dd-a18f-f6217a7667f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bv4RLpPUbgFq49AcUBsCrL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 60707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1515,
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

_source line 32 · 2026-05-17T16:00:27.212Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RrCQ2UecD3NSVDRuQScE4v`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50274b44-9258-44dd-a18f-f6217a7667f0",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RJFadLPqNuYcCk7Npu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b8ea07d-7cc6-4da8-aef9-9a90b0be7fa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bv4RLpPUbgFq49AcUBsCrL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 60707,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1515
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 60707,
          "cache_creation_input_tokens": 1515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1515,
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

_source line 33 · 2026-05-17T16:00:27.215Z_

<details><summary>↩ Tool result · `toolu_01RrCQ2UecD3NSVDRuQScE4v`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b8ea07d-7cc6-4da8-aef9-9a90b0be7fa8",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "4607b89b-8189-4de1-bb66-873b078ac2b4",
  "sourceToolAssistantUUID": "2b8ea07d-7cc6-4da8-aef9-9a90b0be7fa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-17T16:00:29.858Z_



Now I have all the context needed. Let me compose my review focusing on novelty, significance, related work coverage, positioning, and writing quality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4607b89b-8189-4de1-bb66-873b078ac2b4",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RJePpXEYBdcw7XJsWX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e4ce027-1426-43ff-91c7-28009defd1f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDW3T4bVxEabj2vfn1Zpdk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 62222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 689,
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

_source line 35 · 2026-05-17T16:02:19.089Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_012yLyjjchhjeLpdhJmZ9Vm9`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "tier": "best",
  "dream_id": "dream_20260517T144412",
  "overall_score": "3/6 Weak Reject",
  "report": "---\ndream_id: dream_20260517T144412\ntier: best\nreviewer: R2 (Novelty, Significance, Related Work, Positioning, Writing Quality)\noverall_score: 3/6 Weak Reject\ntimestamp: 2026-05-17\n---\n\n# Review: \"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning\"\n\n## 1. Summary\n\nThis paper presents SICA (Symbolic Invariant Consensus Aggregation), a method that extracts FOL constraints from multiple LLM reasoning traces and uses weighted MAX-SAT to select answers, then systematically evaluates it against majority voting (Self-Consistency). The central finding is negative: across 5 model families, 3 reasoning domains, and 1,300+ problems, SICA provides no significant accuracy gain over SC. The authors diagnose this as a \"capability trap\" where instruction-scale models produce diverse but non-discriminative constraints (precision ~0.50), while reasoning models eliminate diversity entirely, and propose C0 (candidate disagreement rate) as a zero-cost diagnostic for practitioners.\n\n## 2. Strengths\n\n- **Thorough mechanism analysis.** The constraint ablation experiment (Table 3) is well-designed and convincing: MAX-SAT, count-only, and random-weight aggregation agree on 802/804 problems (McNemar p=0.99). This cleanly demonstrates that the solver's satisfiability reasoning contributes nothing beyond counting when constraints lack discriminative power. The per-problem precision analysis (n=307, mean=0.505, regression slope=0.003 against vote entropy, r^2<0.01) provides fine-grained evidence at a granularity that experiment-level correlations could not achieve.\n\n- **Methodologically honest negative result.** The paper does not try to disguise a failed method as a success. The pivot from method development to systematic failure analysis is credible, and the authors are transparent about effect sizes, p-values, and statistical power throughout. The temperature ablation (Section 5) adds causal evidence by experimentally manipulating diversity from C0=28% to 68% while observing a persistent null gap.\n\n- **Useful qualitative insight.** The case study analysis (Section 6.4) identifying that 78% of extracted constraints formalize shared premises rather than discriminative reasoning steps provides an intuitive explanation for why precision clusters at 0.50. This is a genuinely informative observation about the failure mode of LLM-based FOL extraction.\n\n- **Clean experimental design for the powered experiment.** The main Qwen-14B experiment (n=804) with McNemar's test and appropriate multiple comparison handling is well-executed. Tables are consistently formatted with appropriate precision.\n\n- **Practical overhead analysis.** Demonstrating 49% wall-time overhead for zero accuracy gain, with the solver itself contributing <0.01% of total time, provides actionable guidance: the bottleneck is extraction cost, not solver complexity.\n\n## 3. Weaknesses\n\n- **W1 (Major): The title and central claim far exceed what the evidence supports.** The title asserts that \"Symbolic Consensus Cannot Beat Majority Voting\" in general, but the paper tests exactly one pipeline: LLM self-extracted FOL constraints aggregated via MAX-SAT. This is a specific instantiation, not the entire class. Critically, the paper's own literature map (which I have access to via project files) identifies multiple neuro-symbolic methods that reportedly achieve gains on the exact same benchmarks tested here: DyLoS (EACL 2026) uses multi-paradigm solver selection on FOLIO and ProofWriter and outperforms Logic-LM; Aristotle (ACL 2025) achieves strong results on ProofWriter and FOLIO via logic-complete decomposition; FoVer (TACL 2025) uses FOL verification with positive results on ProofWriter and FOLIO; LogicAgent (2025) reports +7.05% average gain on logical reasoning benchmarks. The paper does not cite, discuss, or experimentally compare against any of these methods. The claim that symbolic consensus \"cannot\" beat voting is falsified by published results from other groups on the same benchmarks. What the paper actually shows is that *LLM self-extraction of FOL constraints produces non-discriminative constraints*, which is a narrower and less novel finding.\n\n- **W2 (Major): 8 references is critically insufficient for a venue like EMNLP.** A systematic empirical study that claims to characterize a structural limitation of an entire class of methods requires thorough positioning against existing work. EMNLP papers in this space typically cite 30-60 references. The project's own literature map identifies 25+ relevant papers with \"must_cite\" or \"should_cite\" status, yet only 8 appear in the submission. Critical omissions include:\n  - Loo et al. 2025 (\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\"), which directly contextualizes the QwQ-32B finding that strong models produce near-identical paths and SC gains plateau\n  - Snell et al. 2025 (ICLR Oral on test-time compute scaling), which is foundational for understanding the diversity-capability relationship\n  - DeepSeek-R1 technical report (Nature 2025), essential for characterizing the reasoning model paradigm and the distillation behavior observed with DeepSeek-R1-Distill-7B\n  - DyLoS, FoVer, Aristotle, LogicAgent: methods that achieve positive results on the same benchmarks, whose existence fundamentally challenges the paper's framing\n  - Taubenfeld et al. 2025 (confidence-weighted SC, ACL Findings 2025): the paper cites a 2024 paper on debate biases by the same authors, which appears to be a citation error\n  - Diversity-Aware Training for Test-Time Scaling (2025), which independently identifies diversity collapse in reasoning models\n  - SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\n  \n  The Related Work section is approximately half a page with four paragraphs. For a paper whose contribution depends on positioning at the intersection of self-consistency, neuro-symbolic reasoning, and test-time compute, this coverage is inadequate. A reviewer encountering this paper at EMNLP would immediately question the depth of the literature survey.\n\n- **W3 (Major): Self-extraction confound is not addressed.** The same model that generates reasoning traces also extracts FOL constraints from those traces. A model that commits a reasoning error will plausibly extract constraints consistent with that error, because both the reasoning and the extraction share the same internal representations and failure modes. The paper cannot distinguish between two very different conclusions: (a) \"symbolic consensus over FOL constraints is fundamentally limited\" (the paper's claim) vs. (b) \"LLM self-extraction of FOL constraints does not produce discriminative representations\" (a narrower finding about extraction methodology). FOLIO provides human-authored gold FOL annotations. An oracle experiment using gold FOL as constraints would definitively separate extraction failure from aggregation failure and is conspicuously absent. Similarly, using a stronger or separate model for extraction (e.g., 72B extracting constraints from 14B traces) would test whether the bottleneck is extraction capability rather than a structural limitation of the aggregation paradigm.\n\n- **W4 (Major): The \"capability trap\" concept restates known limitations without sufficient novelty.** Logic-LM (Pan et al. 2023) and LINC (Olausson et al. 2023) already document that LLM-to-FOL translation is error-prone and that constraint quality is the binding limitation. The observation that weaker models produce more diverse but lower-quality outputs, while stronger models produce less diverse but higher-quality outputs, is a well-characterized property of LLM scaling (it is precisely the diversity-quality tradeoff documented by Loo et al. 2025 and Diversity-Aware TTS 2025). The \"capability trap\" label is descriptive, but the underlying phenomenon is a predictable consequence of these known properties. The paper would need to demonstrate that this specific characterization enables new research directions or practical decisions that existing understanding does not, which it does not convincingly do beyond the C0 diagnostic.\n\n- **W5 (Moderate): Domain coverage is substantively misleading.** The paper claims \"3 reasoning domains\" (formal logic, commonsense, science), but SICA operates meaningfully (C0>20%) almost exclusively on formal logic (FOLIO+ProofWriter). On StrategyQA (C0=10%), ARC-Challenge (C0=5%), and GSM8K (C0=10%), the model is sufficiently capable that traces converge, making these conditions uninformative about SICA's potential. The effective experimental coverage is one domain (formal logic) with one powered model (Qwen-14B) and several underpowered conditions (n=60) for other models. This is acknowledged implicitly in the text but not reflected in how the paper frames its contributions.\n\n- **W6 (Moderate): No figures are rendered.** The paper references F2 (hero scatter plot of per-problem constraint precision vs. vote entropy) and F4 (C0 vs. SICA-SC gap) by textual description (\"Figure~\\ref{fig:f2-description}\" and \"Figure~\\ref{fig:f4-description}\"), but neither figure is included in the LaTeX source. The cross-references appear broken. For a paper whose central argument is about the relationship between diversity and constraint quality, the absence of the hero visualization is a significant presentation failure.\n\n- **W7 (Moderate): C0 as a \"contribution\" is questionable.** C0 is the fraction of problems with multiple candidate answers, which is trivially computed as a byproduct of standard SC. The paper's own regression analysis (slope=-0.02, r^2=0.06, p=0.40) shows C0 has no continuous predictive power for the SICA-SC gap. Its value is purely as a binary filter (C0<5% means degenerate, C0>20% means trapped), but this binary classification is effectively equivalent to asking \"is this a reasoning model or an instruction model?\" The C0 thresholds (<5%, >20%) are derived from a small number of conditions and their generalization is unknown.\n\n- **W8 (Moderate): The paper attacks a method (SICA) that the authors themselves designed.** Unlike a negative result about an established community method, SICA has no prior publication, no users, and no established research line. The impact of demonstrating that a novel method does not work is inherently lower than demonstrating that an established method has overlooked limitations. The paper partially mitigates this by generalizing via the Logic-LM x K baseline (Section 6.2), but this comparison is limited to one model on one dataset.\n\n- **W9 (Minor): The temperature ablation is labeled \"causal\" but is confounded.** Temperature simultaneously changes diversity (C0), trace quality (SC drops from 76.7% to 70.0%), and extraction quality (extraction rate drops from 91% to 87%). The persistent null gap at high temperature could reflect worse constraints from noisier traces rather than a structural limitation that holds regardless of diversity level. A true causal test would manipulate diversity while holding trace and extraction quality constant, which is not achievable through temperature alone.\n\n## 4. Questions for Authors\n\n1. How do you reconcile the claim that \"symbolic consensus cannot beat majority voting\" with published results from DyLoS (EACL 2026), Aristotle (ACL 2025), and FoVer (TACL 2025) achieving positive results on FOLIO and ProofWriter using symbolic reasoning methods?\n\n2. Have you considered using FOLIO's gold FOL annotations as an oracle to separate extraction failure from aggregation failure? If gold constraints were used instead of LLM-extracted constraints, does MAX-SAT aggregation provide any value?\n\n3. Have you tested using a stronger or separate model (e.g., GPT-4, Claude, or Qwen-72B) for constraint extraction while keeping the trace generation model constant? This would test whether the non-discriminative constraint quality is an extraction capability issue or a structural limitation.\n\n4. The Taubenfeld et al. citation (2024) appears to reference a debate biases paper rather than the confidence-weighted SC paper (ACL Findings 2025). Is this intentional?\n\n5. The constraint-sharing analysis (78% shared, 12% discriminative) covers only 8 problems qualitatively (Section 6.4). Has this been verified quantitatively at scale across the 307 multi-candidate problems?\n\n6. Why is Mistral-7B referenced in the framing documents (n=60, delta=0.0) but absent from Table 1?\n\n7. For the 5%-20% C0 gap (between \"degenerate\" and \"trapped\"): what is the predicted behavior in this range, and do any of your conditions fall there?\n\n8. Would you consider reporting constraint precision separately for correct vs. incorrect traces? If constraints from correct traces have higher precision than those from incorrect traces, the issue is signal-to-noise ratio rather than fundamental non-discrimination.\n\n## 5. Minor Issues\n\n- The paper uses \"5 model families\" in the abstract and introduction but Table 1 shows 4 instruction-scale models plus 1 reasoning model (QwQ-32B). The QwQ-32B row reports accuracy as \"--\" with delta \"approx 0\", which is incomplete.\n- Section 5 (Temperature Ablation) uses n=60, the same underpowered sample size as most non-central experiments. Running this at n=804 on the Qwen-14B FOLIO+PW dataset would substantially strengthen the causal claim.\n- The paper mixes FOLIO+ProofWriter as a combined domain (n=804) and as separate domains in different sections, making it ambiguous whether this counts as 1 or 2 domains.\n- \"Rogers et al. 2020\" (a BERT survey in TACL) is cited as precedent for \"negative results in NLP\" but is not itself a negative result paper. More appropriate precedents exist.\n- Several paragraphs begin with \"F2:\" or \"F4:\" as inline figure descriptions, which reads as placeholder text rather than final prose.\n\n## 6. Overall Assessment\n\nThe paper presents a well-executed empirical analysis of a specific pipeline (LLM self-extracted FOL constraints + MAX-SAT aggregation) and convincingly demonstrates that this pipeline does not outperform majority voting. The constraint ablation (Table 3) and per-problem precision analysis (Table 2) are the paper's strongest contributions and are methodologically sound.\n\nHowever, the paper's framing substantially overreaches its evidence. The title implies a general impossibility result about symbolic consensus, but only one specific pipeline is tested, and multiple published methods achieve positive results on the same benchmarks using different neuro-symbolic approaches. The self-extraction confound is unaddressed: the paper cannot distinguish between \"symbolic aggregation is fundamentally limited\" and \"LLM self-extraction produces non-discriminative constraints,\" which are very different conclusions with very different implications for future work. The \"capability trap\" concept, while clearly articulated, largely restates the known diversity-quality tradeoff in LLM scaling. The C0 diagnostic has limited incremental value beyond binary model-type classification.\n\nThe scholarship is critically thin at 8 references, missing numerous directly relevant works including methods that achieve gains on the tested benchmarks (DyLoS, Aristotle, FoVer), papers that contextualize the core findings (Loo et al. 2025, DeepSeek-R1 report), and the correct citation for Taubenfeld et al. The missing hero figures (F2, F4) further weaken the presentation.\n\nThe mechanism analysis deserves publication, but it needs to be wrapped in honest, appropriately scoped claims (\"LLM self-extracted FOL constraints lack discriminative power\" rather than \"symbolic consensus cannot beat voting\"), substantially expanded scholarship, and a clear discussion of how the findings relate to methods that do achieve gains on the same benchmarks. In its current form, the gap between claims and evidence, combined with the thin related work, places this below the acceptance bar for a top venue.\n\n## 7. Score and Confidence\n\n**Score: 3/6 (Weak Reject)**\n\nRationale: The mechanism analysis is solid empirical work, but the over-generalized claims, critically thin references (8 citations), unaddressed self-extraction confound, absence of comparison with methods that demonstrably work on the same benchmarks, and missing figures collectively place this below the acceptance threshold. The contribution is a well-executed analysis of a narrow failure mode, presented as a broad impossibility result. With narrowed claims, expanded references (30+), a gold-FOL oracle experiment, and rendered figures, this could reach borderline accept.\n\n**Confidence: 4/5**\n\nI am confident in this assessment. The weaknesses regarding over-generalized claims, missing related work, and the self-extraction confound are clear and well-supported by the project's own literature map, which identifies the missing citations. The one area of uncertainty is whether the EMNLP program committee would weigh the practical value of the systematic negative result more heavily than I do, potentially pushing this to borderline accept territory.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e4ce027-1426-43ff-91c7-28009defd1f6",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RJePpXEYBdcw7XJsWX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9c7c8ab-7553-46fc-a87c-8541e2533782",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDW3T4bVxEabj2vfn1Zpdk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 62222,
      "output_tokens": 4218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4218,
          "cache_read_input_tokens": 62222,
          "cache_creation_input_tokens": 689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 689,
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

_source line 36 · 2026-05-17T16:02:22.303Z_

<details><summary>↩ Tool result · `toolu_012yLyjjchhjeLpdhJmZ9Vm9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/review_report.md\", \"dream_id\": \"dream_20260517T144412\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9c7c8ab-7553-46fc-a87c-8541e2533782",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a95d9ee6fe55a339a",
  "type": "user",
  "uuid": "509fa83e-4d3c-4375-96e9-41f2b39100fd",
  "sourceToolAssistantUUID": "e9c7c8ab-7553-46fc-a87c-8541e2533782",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-17T16:02:37.153Z_

Review submitted successfully. Here is a summary of the key findings:

**Score: 3/6 (Weak Reject) | Confidence: 4/5**

**Core assessment:** The mechanism analysis (constraint ablation showing MAX-SAT = count-only = random-weight on 802/804 problems, and per-problem constraint precision at 0.505) is solid empirical work. However, the paper has several critical issues:

**Major weaknesses identified:**
1. **Claims exceed evidence.** The title claims symbolic consensus "cannot" beat voting, but only one specific pipeline (LLM self-extracted FOL + MAX-SAT) is tested. Published methods (DyLoS, Aristotle, FoVer, LogicAgent) achieve gains on the exact same benchmarks (FOLIO, ProofWriter), which the paper neither cites nor discusses.

2. **8 references is critically insufficient.** The project's own literature map identifies 25+ relevant papers with must-cite/should-cite status. Missing critical works include Loo et al. 2025 (SC scaling plateaus), DeepSeek-R1 report, Snell et al. 2025 (test-time compute), and the methods that work on the tested benchmarks.

3. **Self-extraction confound unaddressed.** The same model generates traces and extracts constraints. Without a gold-FOL oracle experiment (FOLIO provides gold annotations) or a stronger/separate extraction model, the paper cannot distinguish "symbolic aggregation is fundamentally limited" from "LLM self-extraction produces non-discriminative constraints."

4. **"Capability trap" restates known properties** of the diversity-quality tradeoff in LLM scaling, documented by Loo et al. 2025 and Diversity-Aware TTS 2025.

5. **Domain coverage is misleading.** SICA operates meaningfully (C0>20%) only on formal logic; other domains have C0<10%, making them uninformative.

6. **Hero figures (F2, F4) are not rendered** in the LaTeX source, with broken cross-references.

**Path to improvement:** Narrow claims to match evidence, expand to 30+ references, add gold-FOL oracle experiment, compare against methods that achieve gains on the same benchmarks, render all figures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "509fa83e-4d3c-4375-96e9-41f2b39100fd",
  "isSidechain": true,
  "agentId": "a95d9ee6fe55a339a",
  "requestId": "req_011Cb8RT7vWbGv8TXRJL7j1U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "599de6ff-5047-46d1-adc1-05de01b5d4b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmUQSLNxhG2XpkkbVvDM1L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4349,
      "cache_read_input_tokens": 62911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4349,
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
