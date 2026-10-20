# Research conversation: You are Reviewer R1 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a99d1bfd64c49d1b3.jsonl`
- **Structured JSON:** [`998ee7ad6811b18bc8b1.json`](../../sessions/99/998ee7ad6811b18bc8b1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-17T15:59:16.973Z_

You are Reviewer R1 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus areas: **methodology soundness, experimental rigor, statistical validity, and reproducibility**.

## Paper Summary

**Title:** "When Does Symbolic Consensus Help? A Systematic Empirical Study"

**Core claim:** The paper presents the first systematic empirical evaluation of symbolic consensus for LLM reasoning aggregation. They instantiate "SICA" (Symbolic Invariant Consensus Aggregation), which extracts FOL constraints from K reasoning traces and selects answers via weighted MAX-SAT. The main finding is negative: SICA provides no significant accuracy gain over standard majority voting (Self-Consistency) across 1,300+ problems, 5 model families, 3 reasoning domains. They identify a "capability trap" pattern and propose C0 (fraction of problems with multiple candidate answers) as a binary diagnostic.

## Key Experimental Details

**Models (7 total, 4 categories):**
- Qwen family (instruction-scale): Qwen2.5-7B, 14B, 72B-AWQ
- Other instruction-scale: Mistral-7B, LLaMA-3.1-8B
- Distilled reasoning: DeepSeek-R1-Distill-Qwen-7B (reclassified as instruction-scale, C0=58%)
- Full reasoning: QwQ-32B (C0=2.6%)

**Domains:** ProofWriter, FOLIO, StrategyQA, ARC-Challenge, GSM8K (pilot)

**Default config:** K=12 traces, T=0.7

**Main results (Table 1):**
- Qwen-14B PW+FOLIO: n=804, C0=38%, SC=76.2, SICA=76.5, Δ=+0.3pp, n.s.
- Qwen-14B StrategyQA: n=60, C0=10%, SC=53.3, SICA=56.7, Δ=+3.3pp, p=0.16
- Qwen-14B ARC: n=60, C0=5%, SC=96.7, SICA=95.0, Δ=-1.7pp
- Qwen-7B PW+FOLIO: n=60, C0=65%, SC=56.7, SICA=60.0, Δ=+3.3pp, p=0.41
- Qwen-72B PW+FOLIO: n=60, C0=22%, SC=85.0, SICA=86.7, Δ=+1.7pp, p=0.65
- Mistral-7B PW+FOLIO: n=60, C0=50%, SC=48.3, SICA=48.3, Δ=0.0, p=1.00
- LLaMA-8B PW+FOLIO: n=60, C0=62%, SC=60.0, SICA=68.3, Δ=+8.3pp, p=0.096
- DeepSeek-R1-7B PW+FOLIO: n=60, C0=58%, SC=71.7, SICA=68.3, Δ=-3.3pp, p=0.48
- QwQ-32B Mixed: n=46, C0=2.6%, SICA≡SC, Δ=0.0

**Constraint quality (Table 2):** Mean precision 0.57 (std 0.23) on 307 multi-candidate problems. Above random (0.33 for 3-class) but no correlation with vote entropy (R²=0.008).

**Mechanism ablation (Table 3):** MAX-SAT (76.5%) ≈ Count-only (76.4%) ≈ Random-weight (76.3%) ≈ SC (76.2%). Agreement on 802/804 problems.

**Tiebreak analysis (Table 4):** SICA 80% on ties (5 of 60 problems), but effective contribution ~2.5pp max.

**Temperature ablation (Table 5):** T=0.3: +1.7pp (p=0.65), T=0.5: +1.7pp (p=0.55), T=0.7: +0.3pp (n.s.), T=1.0: +8.3pp (p=0.034). Extraction rate drops 89%→76%, coherence ~98%→85%.

**C0 diagnostic (Table 6, Table 11):** Two clusters: low-C0 (0-10%, mean gap -0.9pp, 3 points) and high-C0 (22-72%, mean gap +1.8pp, 9 points). R²=0.08, p=0.37.

**K sensitivity (Table 7, Appendix A):** K=6: +1.7pp, K=8: 0, K=11: 0, K=12: -1.7pp, K=16: -1.7pp, K=20: -1.7pp. Non-monotonic; K=11 (odd) confirms tiebreak-only mechanism.

**Overhead (Appendix B):** 48.7% additional compute. Constraint extraction dominates (47%). Overhead-to-gain ratio ≈162.

**Weighted SC (Appendix C):** Inverse-length: 77.0% (+0.8pp vs SC, p=0.42). Matches SICA at zero cost.

**Logic-LM comparison (Appendix D):** Logic-LM×K+vote: 80.9% vs SICA: 79.4% on FOLIO (n=204, p=0.38).

**GSM8K pilot (Appendix E):** n=30, Δ=+3.3pp, p=0.56, uninformative.

**Case studies (Appendix F):** 8 cases: 3 semantically meaningful, 2 correctly discriminative, 3 non-discriminative, 2 actively misleading.

**Statistical approach:** McNemar's exact test for paired comparisons, Bonferroni correction (adjusted α≈0.01 for 5 families).

**References:** 8 total — Wang et al. 2023 (SC), Chen et al. 2023 (Universal SC), Pan et al. 2023 (Logic-LM), Olausson et al. 2023 (LINC), Taubenfeld et al. 2024, Cobbe et al. 2021, Lightman et al. 2024, Reynolds & McDonell 2021.

## Experiment Design Reference (what was planned vs what appears)

The paper was planned to include 19 experiments. Key experiments from the plan:
- exp-001 through exp-020 covering K ablation, tiebreak analysis, scaling (7B/72B), QwQ-32B, C0 diagnostic, constraint ablation, multiple models (Mistral, LLaMA, DeepSeek), Logic-LM, weighted SC, StrategyQA, ARC, temperature ablation, GSM8K, overhead analysis, constraint quality correlation, and case studies.
- Large-n cross-model tests at n≥200 exist only for LLaMA (StrategyQA Δ=+2.0pp p=0.424, FOLIO Δ=-2.4pp p=0.267) — these are mentioned in the context but it's unclear if they appear in the paper.

## Your Review Task

Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, be specific with evidence)
3. **Weaknesses** (bulleted, be specific — cite tables/sections)
4. **Questions for Authors** (numbered)
5. **Minor Issues** (if any)
6. **Overall Assessment** (1-2 paragraphs)
7. **Score** (1-6) and **Confidence** (1-5, where 5=certain)

Focus on:
- Are the experimental designs sound? Sample sizes adequate?
- Is the statistical methodology appropriate?
- Are claims supported by the evidence?
- Are there confounds or alternative explanations not addressed?
- Is the methodology (SICA pipeline) clearly described and reproducible?
- Are ablations comprehensive?
- Coverage of planned experiments vs what appears in the paper


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "90db5424-6444-4251-83b0-404ac7fb788c",
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

_source line 2 · 2026-05-17T15:59:16.980Z_

```json
{
  "parentUuid": "90db5424-6444-4251-83b0-404ac7fb788c",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
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
  "uuid": "76d7e739-2e1e-47dd-9326-9ecaef964bb1",
  "timestamp": "2026-05-17T15:59:16.980Z",
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

_source line 3 · 2026-05-17T15:59:22.201Z_



I need to read the actual paper and supporting materials before writing this review. Let me start by examining the project structure and the paper itself.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76d7e739-2e1e-47dd-9326-9ecaef964bb1",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RDTaoTYkHTnTQE6PXr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67c54507-3666-40be-9a34-e111b99ac672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHr4ptacdhX7fpJx9BuRQL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9179,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9179,
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

_source line 4 · 2026-05-17T15:59:24.108Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0137Dg85y3GNMYM1Hsd3DET6`</summary>

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
  "parentUuid": "67c54507-3666-40be-9a34-e111b99ac672",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RDTaoTYkHTnTQE6PXr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b0ebefc-b02c-4b8e-9adf-fe97ad096cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHr4ptacdhX7fpJx9BuRQL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9179,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9179,
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

_source line 5 · 2026-05-17T15:59:24.137Z_

<details><summary>↩ Tool result · `toolu_0137Dg85y3GNMYM1Hsd3DET6`</summary>

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
  "parentUuid": "2b0ebefc-b02c-4b8e-9adf-fe97ad096cd7",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "c472c346-9608-417d-bb65-6dc4e9f0abb1",
  "sourceToolAssistantUUID": "2b0ebefc-b02c-4b8e-9adf-fe97ad096cd7",
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

_source line 6 · 2026-05-17T15:59:25.189Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016nAv4eNzkE8i2fAWBfm5t7`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c472c346-9608-417d-bb65-6dc4e9f0abb1",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RDTaoTYkHTnTQE6PXr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad2ecedc-c577-4412-a203-f10e92cc3555",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHr4ptacdhX7fpJx9BuRQL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9179,
      "cache_read_input_tokens": 8251,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9179
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 215,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 9179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9179,
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

_source line 7 · 2026-05-17T15:59:25.193Z_

<details><summary>↩ Tool result · `toolu_016nAv4eNzkE8i2fAWBfm5t7`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad2ecedc-c577-4412-a203-f10e92cc3555",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "91326cab-f978-4381-9539-b624ef2592eb",
  "sourceToolAssistantUUID": "ad2ecedc-c577-4412-a203-f10e92cc3555",
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

_source line 8 · 2026-05-17T15:59:31.977Z_



Let me read the paper and supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91326cab-f978-4381-9539-b624ef2592eb",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RE4tLEVsz9P1vd17zB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d49ac1eb-0148-43ff-8c92-0e3300d03242",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFyT5qswysrTtCyy3M5Lcq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3843,
      "cache_read_input_tokens": 17430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3843,
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

_source line 9 · 2026-05-17T15:59:32.458Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01B6xM9kcxedHZE5jBFg8WCq`</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d49ac1eb-0148-43ff-8c92-0e3300d03242",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RE4tLEVsz9P1vd17zB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "583b042f-ceb9-433d-8764-268b18f0df3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFyT5qswysrTtCyy3M5Lcq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3843,
      "cache_read_input_tokens": 17430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3843,
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

_source line 10 · 2026-05-17T15:59:32.617Z_

<details><summary>↩ Tool result · `toolu_01B6xM9kcxedHZE5jBFg8WCq`</summary>

```text
{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (38 个)\n\n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_constraint_ablation_013**: DONE (success) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| temperature-ablation-t10 | Temperature ablation T=1.0: 高温下 Qwen2.5-14B trace diversity 最大化（C0 预期>60%），SICA-SC gap 预期≈0 或负——验证最大 diversity 仍不能拯救 SICA，因为 constraint discriminative power 不随 diversity 增加 | — | — | — |\n| temperature-ablation-t05 | Temperature ablation T=0.5: 中温下 Qwen2.5-14B trace diversity 中等（C0 预期 30-45%），SICA-SC gap 预期≈0——验证即使 diversity 适中，constraint quality 仍为瓶颈 | — | — | — |\n| temperature-ablation-t03 | Temperature ablation T=0.3: 低温下 Qwen2.5-14B trace diversity 降低（C0 预期<30%），SICA-SC gap 预期≈0——验证 diversity 不足时 SICA 无操作空间，capability trap 的下界 | — | — | — |\n\n## 待处理\n- smoke-test-5q（准备中）\n\n## 近期结论\n- **exp-014-deepseek-r1-7b** (negative): DeepSeek-R1-Distill-Qwen-7B（reasoning distill 模型）在 D012 上 SICA vs SC——预期 C0<5%（类似 QwQ-32B，reasoning model 的确定性链消灭多样性），作为第二个 reasoning model 数据点验证 capability trap ← 基于 sica_expanded_14b\n- **exp-010-mistral-v3** (negative): Cross-family validation: Mistral-7B-Instruct-v0.3 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 跨模型家族泛化（v3: 脚本内含 vLLM 清理+conda 环境，解决 v2 SIGTERM 问题） ← 基于 sica_expanded_14b\n- **sica_expanded_14b** (success): Qwen2.5-14B-Instruct 在 N=804 (600PW+204FOLIO) 上 SICA 相比 SC 有统计显著优势（p<0.05）——full-scale validation of D012 preliminary +3.3pp signal ← 基于 sica_d012_14b\n  [sica_expanded_14b](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_expanded_14b/data/sica_expanded_14b_config.txt) | [exp001_full_analysis](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_expanded_14b/report/exp001_analysis_summary.txt)\n\n## 趋势\n成功 12 / 负向 7 / 失败 9 / 共 34\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-32608: 无 GPU 信息\n\n## 告警\n- mvp_math50_t07: 已被终止 — unknown\n- sica_aime30_t07: 已被终止 — unknown\n- sica_aime30_v2: 已被终止 — unknown\n- sica_aime30_v3: 已被终止 — unknown\n- sica_proofwriter30: 训练失败 — unknown\n- sica_folio30: 已被终止 — unknown\n- sica_proofwriter30_v2: 已被终止 — unknown\n- exp-011-llama8b: 训练失败 — unknown\n- exp-010-mistral: 训练失败 — unknown\n- exp-011-llama8b-v2: 训练失败 — unknown\n- exp-017-strategyqa: 训练失败 — unknown\n- exp-018-arc: 训练失败 — unknown\n- exp-010-mistral-v2: 训练失败 — unknown\n- exp-017-strategyqa-v2: 训练失败 — unknown\n- pilot-contrastive-prompt: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "583b042f-ceb9-433d-8764-268b18f0df3c",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "ad772c3c-79ce-4de6-a82f-744c930409a4",
  "sourceToolAssistantUUID": "583b042f-ceb9-433d-8764-268b18f0df3c",
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

_source line 11 · 2026-05-17T15:59:34.433Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01536RFv7unmjiqPjCepkCxA`</summary>

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
  "parentUuid": "ad772c3c-79ce-4de6-a82f-744c930409a4",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RE4tLEVsz9P1vd17zB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35a377ca-efb2-4972-a3f7-4adf12f87b56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFyT5qswysrTtCyy3M5Lcq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3843,
      "cache_read_input_tokens": 17430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3843,
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

_source line 12 · 2026-05-17T15:59:34.455Z_

<details><summary>↩ Tool result · `toolu_01536RFv7unmjiqPjCepkCxA`</summary>

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
  "parentUuid": "35a377ca-efb2-4972-a3f7-4adf12f87b56",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "3d74cbb5-ad8f-4b69-a6aa-fb903f3e2dce",
  "sourceToolAssistantUUID": "35a377ca-efb2-4972-a3f7-4adf12f87b56",
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

_source line 13 · 2026-05-17T15:59:34.567Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01ULgU5WVR4aohA3NdGNYSm9`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d74cbb5-ad8f-4b69-a6aa-fb903f3e2dce",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RE4tLEVsz9P1vd17zB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e838cb91-26b2-4932-9d6c-be1b84dcc806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFyT5qswysrTtCyy3M5Lcq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3843,
      "cache_read_input_tokens": 17430,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3843
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 255,
          "cache_read_input_tokens": 17430,
          "cache_creation_input_tokens": 3843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3843,
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

_source line 14 · 2026-05-17T15:59:34.589Z_

<details><summary>↩ Tool result · `toolu_01ULgU5WVR4aohA3NdGNYSm9`</summary>

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
  "parentUuid": "e838cb91-26b2-4932-9d6c-be1b84dcc806",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "b3659d6d-68a0-442e-85d0-fe3c2d2b06e3",
  "sourceToolAssistantUUID": "e838cb91-26b2-4932-9d6c-be1b84dcc806",
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

_source line 15 · 2026-05-17T15:59:37.369Z_

Let me read the latest paper version and the project's key files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3659d6d-68a0-442e-85d0-fe3c2d2b06e3",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8REm1L7kvRy84ngZRdo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbe4b8e6-b6e1-4a85-90d2-0b608849f012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiWawqwuf2jehSpAAYTTNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2554,
      "cache_read_input_tokens": 21273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2554,
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

_source line 16 · 2026-05-17T15:59:39.885Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D78YtiZaWxRiiY62ye2MxW`</summary>

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
  "parentUuid": "dbe4b8e6-b6e1-4a85-90d2-0b608849f012",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8REm1L7kvRy84ngZRdo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "340958fb-8d70-4751-a164-4e0a178bc316",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiWawqwuf2jehSpAAYTTNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2554,
      "cache_read_input_tokens": 21273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2554,
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

_source line 17 · 2026-05-17T15:59:40.356Z_

<details><summary>↩ Tool result · `toolu_01D78YtiZaWxRiiY62ye2MxW`</summary>

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
  "parentUuid": "340958fb-8d70-4751-a164-4e0a178bc316",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "77df5fed-60d6-48fe-9704-e6987ba3f1f4",
  "sourceToolAssistantUUID": "340958fb-8d70-4751-a164-4e0a178bc316",
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

_source line 18 · 2026-05-17T15:59:40.716Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01E5A45u4zRGV2M4VzmAVU5t`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77df5fed-60d6-48fe-9704-e6987ba3f1f4",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8REm1L7kvRy84ngZRdo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f6cf1b3-ddb3-462f-8d31-e0ddb6b8cedb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiWawqwuf2jehSpAAYTTNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2554,
      "cache_read_input_tokens": 21273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2554,
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

_source line 19 · 2026-05-17T15:59:40.731Z_

<details><summary>↩ Tool result · `toolu_01E5A45u4zRGV2M4VzmAVU5t`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| temperature-ablation-t10 | Temperature ablation T=1.0: 高温下 Qwen2.5-14B trace diversity 最大化（C0 预期>60%），SICA-SC gap 预期≈0 或负——验证最大 diversity 仍不能拯救 SICA，因为 constraint discriminative power 不随 diversity 增加 | — | — | — |\\n| temperature-ablation-t05 | Temperature ablation T=0.5: 中温下 Qwen2.5-14B trace diversity 中等（C0 预期 30-45%），SICA-SC gap 预期≈0——验证即使 diversity 适中，constraint quality 仍为瓶颈 | — | — | — |\\n| temperature-ablation-t03 | Temperature ablation T=0.3: 低温下 Qwen2.5-14B trace diversity 降低（C0 预期<30%），SICA-SC gap 预期≈0——验证 diversity 不足时 SICA 无操作空间，capability trap 的下界 | — | — | — |\\n\\n## 待处理\\n- smoke-test-5q（准备中）\\n\\n## 近期结论\\n- **exp-014-deepseek-r1-7b** (negative): DeepSeek-R1-Distill-Qwen-7B（reasoning distill 模型）在 D012 上 SICA vs SC——预期 C0<5%（类似 QwQ-32B，reasoning model 的确定性链消灭多样性），作为第二个 reasoning model 数据点验证 capability trap ← 基于 sica_expanded_14b\\n- **exp-010-mistral-v3** (negative): Cross-family validation: Mistral-7B-Instruct-v0.3 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 跨模型家族泛化（v3: 脚本内含 vLLM 清理+conda 环境，解决 v2 SIGTERM 问题） ← 基于 sica_expanded_14b\\n- **sica_expanded_14b** (success): Qwen2.5-14B-Instruct 在 N=804 (600PW+204FOLIO) 上 SICA 相比 SC 有统计显著优势（p<0.05）——full-scale validation of D012 preliminary +3.3pp signal ← 基于 sica_d012_14b\\n  [sica_expanded_14b](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_expanded_14b/data/sica_expanded_14b_config.txt) | [exp001_full_analysis](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_expanded_14b/report/exp001_analysis_summary.txt)\\n\\n## 趋势\\n成功 12 / 负向 7 / 失败 9 / 共 34\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32608: 无 GPU 信息\\n\\n## 告警\\n- mvp_math50_t07: 已被终止 — unknown\\n- sica_aime30_t07: 已被终止 — unknown\\n- sica_aime30_v2: 已被终止 — unknown\\n- sica_aime30_v3: 已被终止 — unknown\\n- sica_proofwriter30: 训练失败 — unknown\\n- sica_folio30: 已被终止 — unknown\\n- sica_proofwriter30_v2: 已被终止 — unknown\\n- exp-011-llama8b: 训练失败 — unknown\\n- exp-010-mistral: 训练失败 — unknown\\n- exp-011-llama8b-v2: 训练失败 — unknown\\n- exp-017-strategyqa: 训练失败 — unknown\\n- exp-018-arc: 训练失败 — unknown\\n- exp-010-mistral-v2: 训练失败 — unknown\\n- exp-017-strategyqa-v2: 训练失败 — unknown\\n- pilot-contrastive-prompt: 训练失败 — unknown\\n\", \"total_chars\": 2324, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f6cf1b3-ddb3-462f-8d31-e0ddb6b8cedb",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "4cdc8e0c-8f4d-4866-bce2-e635bd9ab715",
  "sourceToolAssistantUUID": "0f6cf1b3-ddb3-462f-8d31-e0ddb6b8cedb",
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

_source line 20 · 2026-05-17T15:59:41.180Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Gi3EJnM7XHzebFSKdnurFL`</summary>

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
  "parentUuid": "4cdc8e0c-8f4d-4866-bce2-e635bd9ab715",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8REm1L7kvRy84ngZRdo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e070f718-4b3c-4f23-b0b1-e3b8ed200b54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiWawqwuf2jehSpAAYTTNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2554,
      "cache_read_input_tokens": 21273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2554,
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

_source line 21 · 2026-05-17T15:59:41.191Z_

<details><summary>↩ Tool result · `toolu_01Gi3EJnM7XHzebFSKdnurFL`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e070f718-4b3c-4f23-b0b1-e3b8ed200b54",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "d5f660aa-fc9f-4200-b49d-82f53f11806c",
  "sourceToolAssistantUUID": "e070f718-4b3c-4f23-b0b1-e3b8ed200b54",
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

_source line 22 · 2026-05-17T15:59:43.966Z_

Now let me read the experiment results, decisions, and other key supporting files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5f660aa-fc9f-4200-b49d-82f53f11806c",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RFGGDm7LBk64j3CnFa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab54c68e-8fa1-4388-9466-bebacfaffed0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lq6y785vfAvQzhrYNAfYLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12174,
      "cache_read_input_tokens": 23827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12174,
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

_source line 23 · 2026-05-17T15:59:44.958Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01E4qGE5M9YgNyLdY2ksAUB7`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab54c68e-8fa1-4388-9466-bebacfaffed0",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RFGGDm7LBk64j3CnFa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff6183a5-4f94-4c74-86e0-4c63532c86cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lq6y785vfAvQzhrYNAfYLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12174,
      "cache_read_input_tokens": 23827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12174,
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

_source line 24 · 2026-05-17T15:59:44.974Z_

<details><summary>↩ Tool result · `toolu_01E4qGE5M9YgNyLdY2ksAUB7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 37\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet spot\\\"的补充验证。如果 MATH+AIME 均 SICA≈SC → 准备 FAIL 路径决策。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 12:16 UTC\\n  summary: 'D005: 采用双管齐下方案——MATH-500 MVP 继续 + AIME 30 题紧跟，暂不换模型'\\n  rationale: Temperature 诊断确认 QwQ-32B 在 T=0.7/0.9/1.0 下均产生近零答案分歧——reasoning model\\n    的确定性推理压制采样随机性。MATH-500 MVP 高概率 FAIL on C2/C3，但数据仍有价值（负面结果本身有意义）。AIME 2024 是 QwQ-32B\\n    弱项（~79.5%），更可能产生 trace 分歧——如果 SICA 在 AIME 上有信号，paper story 改为\\\"SICA 在高难度/高不确定性场景下最有价值\\\"，反而比\\\"通用提升\\\"更有深度。模型切换（Qwen2.5-7B\\n    等）改变论文定位太大，留作 AIME 也失败后的最后手段。执行顺序：MATH MVP 跑完 → AIME 30 题 → 基于两组结果做 PASS/FAIL\\n    最终判定。\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 12:19 UTC\\n  summary: 'D006: Kill 当前 MATH MVP（有 bug + 25-30h 不可接受），修 bug 后 AIME 30 题优先'\\n  rationale: D005 假设 MVP 4-7h 出结果，但实际第一题 20min+ 未完成（serial trace gen + extraction\\n    回归 5/12 JSON parse fail），外推 25-30h。加上多样性诊断已定论（零分歧），继续烧 25-30h GPU 等一个几乎确定 FAIL\\n    的结果不合理。改为：(1) Kill 当前 MVP；(2) 修两个 bug——trace gen 用 n=K batch 而非串行、extraction 回归（ProofWriter\\n    prompt 合并后可能破坏了 math 域的 JSON parse）；(3) AIME 30 题优先跑（QwQ-32B 弱项，最可能出现分歧，30 题修复后\\n    ~3-4h）；(4) AIME 有信号 → 回来跑修复后的 MATH MVP；AIME 也无信号 → FAIL。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-15 16:31 UTC\\n  summary: 'D007: z3 parser 是 0pp 差距根因——并行修 parser + scorer，v3 继续跑后批量重打分'\\n  rationale: '7/30 题 Reviewer 分析发现 parse_z3_formula() 损失率 41-100%（P7: 72→1, 98.6%），LLM\\n    提取的约束在 z3 转换时被大量丢弃，MAX-SAT 无法工作。P7（SC 1/12 极度分散）是 SICA 理论最佳场景但因 parser 失效无法发挥。策略：v3\\n    继续跑收集全部 traces（最贵部分），并行修 parser + scorer，30 题完成后批量重打分作为真正 MVP 结果。'\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: running, 7/30 done, 0pp差距但因parser bug无效\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-15 17:40 UTC\\n  summary: 'D008: P5 翻转为虚假声明（硬编码），A+C 实际翻转数=0。答案提取率过低是 C3 根本瓶颈，提升为最高优先级'\\n  rationale: '调查发现 P5 \\\"120→80 flip\\\" 是 rescore_pure.py 硬编码的对照值，v3 P5 实际仅 1 个候选答案 \\\"80\\\"。P7\\n    的 72→1 也是 parser 仍无法处理（2.8% parse rate），非 dedup 逻辑 bug。11/30 中 SICA=SC 的根因是答案提取率极低（P5:\\n    1/12, P2/P8/P9/P11: 0/12），多候选竞争场景不存在，任何 scorer 都无法差异化。将答案提取改进提升为最高优先级。'\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: 11/30 done, SICA=SC=63.6%, 0pp\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-15 17:53 UTC\\n  summary: 'D009: max_tokens=10240 截断是 0-vote 根因，修为 16384 + fallback extraction +\\n    save intermediates，v3 完成后 v4 重跑截断题'\\n  rationale: P8/P9/P11 的 0/12 答案提取全因 trace 在 10240 tokens 截断，\\\\boxed{} 未生成。P11 有 60\\n    raw constraints（11/12 提取成功）证明模型推理充分但 token 不够。trace 耗时与截断强相关：350-435s→12/12 votes,\\n    730-810s→0-1/12 votes。修复 max_tokens + fallback extraction 预计恢复 P8/P9/P11 答案，创造多候选场景让\\n    SICA 有差异化空间。v3 继续跑（非截断题有效），v4 只重跑截断题，合并为最终 MVP。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: 12/30 done, P8/P9/P11 confirmed truncated at 10240 tokens\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 19:11 UTC\\n  summary: 'D010: AIME 0pp gap 是结构性的——QwQ-32B 单候选主导，SICA≡SC。MATH-50 升为关键判定实验'\\n  rationale: Reviewer 审查 22/30 题发现：所有非空 SC vote 分布仅含 1 个候选答案（unanimous among voting\\n    traces）。SICA 只能在多候选竞争时产生差异，单候选场景下无论约束打分如何都选同一答案。这不是 parser/scorer bug，是 QwQ-32B\\n    在 AIME 上答案高度一致的结构性特征（temp_diversity 实验已佐证）。v4 修复 max_tokens+fallback 可能恢复截断题的答案，但如果恢复的仍是同一答案则\\n    0pp 不变。MATH-500 Level 1-5 混合难度可能存在更多答案多样性（模型错误率 ~9.4%，错题上不同 trace 可能给出不同错答案），是验证\\n    SICA 核心假设的关键实验。调整优先级：v3 完成 → vote diversity 分析 → v4 快速验证 → MATH-50（决定性实验）。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: 22/30 完成, SICA=SC=72.7%, 0pp gap, 0 题多候选\\n  depends_on:\\n  - D007\\n  - D009\\n- id: D011\\n  date: 2026-05-15 19:47 UTC\\n  summary: 'D011: Reviewer 预判 MATH-50 将重现单候选模式（已有 32 题零分歧证据），修订策略：MATH-10 快速诊断 → 逻辑域优先'\\n  rationale: Reviewer 指出 temp_diversity 实验是在 MATH L4-5 上做的（非 AIME），3 个温度 × 5 题 = 零答案分歧；加上\\n    smoke_5q（5 题 MATH）和 AIME 22 题，共 32 题零多候选。QwQ-32B 答案一致性是模型级特征（CoT 链逻辑约束远强于采样温度），非任务特定。全量\\n    MATH-50（7-8h GPU）几乎确定重现 0pp。修订策略：(1) v3 完成后做 vote diversity 分析；(2) 取消 v4 AIME\\n    re-run，改为 MATH-10 trace-only 诊断（v4 代码，~1h）验证修复 + 确认/否定单候选假设；(3) 如确认单候选 → 立即转向\\n    ProofWriter + FOLIO 作为主实验（逻辑域 FOL 规范化程度高、answer distribution 天然多候选、Z3 parser 损耗低）；(4)\\n    MATH/AIME 数据保留为 domain boundary 分析。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: 22/30 单候选\\n  - exp_id: sica_temp_diversity\\n    role: evidence\\n    result: MATH L4-5 三温度零分歧\\n  - exp_id: smoke_5q\\n    role: evidence\\n    result: 5题MATH单候选\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-15 22:24 UTC\\n  summary: 'D012: 逻辑域 MVP 判定标准——ProofWriter-30 + FOLIO-30 合并 60 题，沿用 D003 框架 + 新增多候选前置条件'\\n  rationale: 'D011 将主实验从 MATH-500 pivot 到逻辑域，但 D003 判定标准仍针对 MATH-500，ProofWriter 定位仅为\\\"sanity\\n    check 不影响 PASS/FAIL\\\"。Reviewer 指出 proofwriter30_v2 完成后无法判定。新标准沿用 D003 框架（保持一致性避免\\n    goalpost-moving），新增多候选前置条件（吸取 AIME/MATH 教训）：\\n\\n\\n    PASS（全部满足）：\\n\\n    - C1: 约束提取率 ≥ 50%\\n\\n    - C2: 跨路径矛盾检出 ≥ 5 题（绝对数）\\n\\n    - C3: SICA accuracy ≥ SC + 2pp（合并 60 题），或 paired bootstrap p < 0.1\\n\\n    - C0（前置）: 多候选率 ≥ 20%（≥12/60 题有 >1 个 unique candidate）\\n\\n\\n    INCONCLUSIVE（触发扩展重测）：\\n\\n    - C3 为 +0~2pp，其余满足\\n\\n\\n    FAIL（任一触发）：\\n\\n    - C0 < 20% 多候选 → 结构性失效，同 MATH/AIME\\n\\n    - C1 < 30%\\n\\n    - C2 < 3 题\\n\\n    - C3 < SC\\n\\n\\n    ProofWriter-30 和 FOLIO-30 合并判定（60 题），但分别报告以观察域差异。'\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: target\\n    result: running\\n  - exp_id: sica_folio30\\n    role: target\\n    result: planned\\n  depends_on:\\n  - D003\\n  - D011\\n- id: D013\\n  date: 2026-05-16 01:30 UTC\\n  summary: 'D013: ProofWriter 中期 CRITICAL——MaxSAT 结构性失效(16/16 excluded=0)，终止当前实验，紧急诊断根因后再决定\\n    FOLIO'\\n  rationale: Reviewer 独立核实 16/30 题中期数据：C0/C1/C2/C3 四项全 FAIL。最关键的是 C2=0（矛盾检出为零），MaxSAT\\n    satisfied_ratio=1.000 贯穿全部问题，SICA 核心机制从未激活。C3=-6.25pp 说明 SICA 不仅无效还主动伤害准确率。继续跑剩余\\n    14 题无意义。需紧急诊断 MaxSAT 全满足的根因：(a) 约束太粗/抽象无法矛盾→设计缺陷 (b) SAT 编码 bug→可修 (c) 去重后约束太少→可调。根因决定\\n    FOLIO 是否值得跑以及 MVP 是否有救。May 19 checkpoint 仅剩 3 天。\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: primary\\n    result: C2=0 structural failure, all 4 D012 criteria FAIL at midpoint\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-16 01:39 UTC\\n  summary: 'D014: MaxSAT 结构性失效根因确认——约束编码缺 answer assertion + 提取失败率 54%。选 A 方案：L3+L1\\n    修复 → 5 题验证 → 全量'\\n  rationale: 诊断 6/6 注入测试通过证明 MaxSAT 求解器无 bug。satisfied_ratio=1.0 的根因是：(1) 不同答案的 trace\\n    未注入 answer assertion 约束，MaxSAT 无法产生冲突；(2) 提取失败率 54.4%（QwQ 重新推理而非输出 JSON）。L3 修复（注入\\n    answer==trace_answer）是 SICA 能否工作的架构前提，L1（prompt 强制 JSON）是质量保障。先 5 题验证再全量，避免浪费\\n    GPU。\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: trigger\\n    result: MaxSAT 16/16 satisfied_ratio=1.0, SICA worse than SC by 6.2pp\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-16 02:48 UTC\\n  summary: 'D015: FOLIO C0 预检 0% 多候选率——QwQ-32B 跨三域自一致性是模型级特征，SICA 核心前提（trace 分歧）不成立。等\\n    L3+L1 五题验证后做最终 MVP 判定。'\\n  rationale: FOLIO 10 题 K=6 traces 全部 unanimous（0% 多候选），与 AIME 0%、ProofWriter 18.8%\\n    汇总后，C0 合并判定确定性 FAIL（远低于 ≥20% 门槛）。QwQ-32B 在数学+逻辑+FOL 三个域均表现出极高 trace 一致性，SICA 的差异化空间不存在。5\\n    题 L3+L1 验证仍在跑，用于确认机制 soundness（与使用场景独立），完成后做最终 MVP 判定。\\n  related_experiments:\\n  - exp_id: sica_folio30\\n    role: C0 precheck\\n    result: 0/10 multi-candidate, all unanimous\\n  - exp_id: sica_proofwriter30_v2\\n    role: context\\n    result: 3/16 multi-candidate = 18.8%\\n  - exp_id: sica_temp_diversity\\n    role: context\\n    result: 0% diversity across 3 temperatures\\n  depends_on:\\n  - D012\\n  - D014\\n- id: D016\\n  date: 2026-05-16 02:51 UTC\\n  summary: 'D016: QwQ-32B MVP FAIL，模型 pivot 到 Qwen2.5-14B-Instruct——全域 C0=3.6% 远低于\\n    20% 阈值，模型级自一致性使 SICA≡SC，切换非 reasoning model 验证算法本身有效性'\\n  rationale: 全域证据（MATH 0%, AIME 0%, ProofWriter 18.75%, FOLIO 0%，合并 3/83=3.6%）确认 QwQ-32B\\n    自一致性是模型级特征而非域特征。SICA 算法需要多候选输入才能与 SC 产生差异。模型替换是唯一可测试\\\"算法本身是否有效\\\"的路径。选择 Qwen2.5-14B-Instruct：非\\n    reasoning model 采样多样性高、14B 在 98GB GPU 上轻松部署、Qwen2.5 系列逻辑能力强。预计 C0 预检 1h + 完整评估\\n    4h，May 19 checkpoint 可控。\\n  related_experiments:\\n  - exp_id: sica_folio30\\n    role: trigger\\n    result: FOLIO C0=0%\\n  - exp_id: sica_proofwriter30_v2\\n    role: evidence\\n    result: ProofWriter C0=18.75%\\n  - exp_id: sica_temp_diversity\\n    role: evidence\\n    result: 3 temps 0% diversity\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: AIME 0pp gap\\n  depends_on:\\n  - D012\\n  - D015\\n- id: D017\\n  date: 2026-05-16 05:11 UTC\\n  summary: 'D017: D012 技术 PASS（C3 +3.3pp）但统计 INCONCLUSIVE（p=0.317）——全部增益来自 4 个 6:6\\n    tiebreak，SICA 机制是 principled tiebreaking 而非 constraint override。扩展实验到 200 题 +\\n    K 敏感性分析争取统计效力'\\n  rationale: 60 题中仅 4 题 SICA≠SC，全部为 6:6 精确平票。56 个非平票题 SICA=SC（约束从未推翻明确多数）。McNemar\\n    p=0.317，二项检验 p=0.3125，均不显著。FOLIO +6.7pp 但 ProofWriter 0pp，域泛化不成立。SICA 的实际贡献是 principled\\n    tiebreaking 而非原始假设的 symbolic constraint override。需要更多数据点来判断 tiebreaking 模式是否稳定可复现。扩展到全量\\n    PW+FOLIO + K=8/16/20 敏感性分析是最高效的统计加固路径。\\n  related_experiments:\\n  - exp_id: sica_d012_14b\\n    role: evidence\\n    result: C3 +3.3pp, p=0.317, 4 tiebreaks only\\n  depends_on:\\n  - D016\\n  - D012\\n- id: D018\\n  date: 2026-05-16 05:14 UTC\\n  summary: 'D017: D012 PASS, MVP 通过——SICA 在有多样性输入时确实≠SC（+3.3pp），核心假设验证。研究阶段首要任务：扩大样本量\\n    + tiebreak 基线分析 + K 消融'\\n  rationale: D012 四项标准全部技术达标：C0=53.3%, C1=100%, C2=34题, C3=+3.3pp。但 C3 实质弱点明确：全部增益来自\\n    4 个 6:6 平票（SICA 3/4 正确 vs SC 1/4），p=0.317 不显著，FOLIO +6.7pp / PW 0pp。MVP 标准以 OR\\n    条件通过（+3.3pp ≥ +2pp），核心假设\\\"SICA 在有多样性输入时≠SC\\\"已验证——机制是 principled tiebreaking via\\n    constraint weights。模型对照（QwQ-32B C0=3.6%, SICA≡SC）强化了\\\"多样性是 SICA 前提\\\"的结论。研究阶段需解决统计弱点：扩展到\\n    200+ 题、K sensitivity、random tiebreak baseline。\\n  related_experiments:\\n  - exp_id: sica_d012_14b\\n    role: primary\\n    result: SICA 73.3% vs SC 70.0%, +3.3pp, 4 tiebreaks, p=0.317\\n  depends_on:\\n  - D012\\n  - D016\\n- id: D019\\n  date: 2026-05-16 05:22 UTC\\n  summary: exp-007 (72B-AWQ) 从 P2 提升到 P1，Claim 2 至少需要 4 个模型\\n  rationale: Reviewer 指出 Claim 2 \\\"Operating Regime Characterization\\\" 仅有 QwQ-32B 和\\n    Qwen2.5-14B 两个模型，不足以支撑 \\\"model property, not task property\\\" 的论断。加上 exp-004 (7B)\\n    也只有 3 个模型。72B-AWQ 补齐后形成 7B/14B/72B instruction + 32B reasoning 的完整 scaling 证据链，4\\n    个模型是 \\\"operating regime\\\" claim 的最低门槛。GPU 时间预算 ~4h，串行排在 exp-002 和 exp-004 之后，总计\\n    ~22.5h，May 25 DDL 前充裕。\\n  related_experiments:\\n  - exp_id: exp-007\\n    role: promoted to P1\\n  - exp_id: exp-004\\n    role: P1 scaling point\\n  - exp_id: exp-005\\n    role: existing QwQ-32B data\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-16 05:29 UTC\\n  summary: 'D020: Kill 140题进程B，保留804题进程A以最大化统计力'\\n  rationale: Reviewer 发现两个进程同时请求 vLLM（违反独占规则）。进程A（PID 181491，804题 PW+FOLIO）预计~67个tie，统计力远优于进程B（140题，~12个tie）。13.4h\\n    ETA 在 May 19 checkpoint 前充裕。MVP 核心瓶颈是 p=0.317 统计不显著，最大化 N 是第一优先。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: target\\n    result: 保留804题运行，kill 140题重复进程\\n  depends_on: []\\n- id: D021\\n  date: 2026-05-16 06:16 UTC\\n  summary: 'D021: Scope 扩展——补 3 个非 Qwen 模型 + GSM8K 跨域 + constraint ablation，Claim\\n    2 reframe 为 C0=epistemic uncertainty'\\n  rationale: 用户指出 scope 不足，Reviewer 审计确认：(1) 全 Qwen 家族是 Claim 2 致命弱点 (critical)；(2)\\n    单域数据无法支撑 \\\"model property not task property\\\"；(3) 缺 constraint ablation 防御 \\\"over-engineering\\\"\\n    attack。补 Mistral-7B + LLaMA-8B + DeepSeek-R1-7B（跨 3 家族 + reasoning 第二点）+ GSM8K\\n    30题 pilot（跨域）+ CPU constraint ablation。总额外 GPU ~7h，May 25 ARR 前充裕。Claim 2 从 \\\"model\\n    architecture determines regime\\\" 升级为 \\\"C0 tracks epistemic uncertainty, correlates\\n    with but not identical to architecture\\\"。\\n  related_experiments:\\n  - exp_id: exp-010\\n    role: new\\n    result: planned\\n  - exp_id: exp-011\\n    role: new\\n    result: planned\\n  - exp_id: exp-012\\n    role: new\\n    result: planned\\n  - exp_id: exp-013\\n    role: new\\n    result: planned\\n  - exp_id: exp-014\\n    role: new\\n    result: planned\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-16 08:18 UTC\\n  summary: 'D022: 不 kill exp-001；exp-013 ablation 改用 exp-002 数据（新 pipeline 含 raw_constraints）'\\n  rationale: pipeline.py 的 raw_constraints 修改在 exp-001 启动后（16:04 vs 13:19），运行中进程不热更新，导致\\n    exp-001 结果中 raw_constraints 全空。三个选项评估：(A) kill+resume 有风险且前 162 题仍缺数据；(B) 全量重跑浪费\\n    3h；(C) 近似模式说服力弱。选择 Option D：保持 exp-001 不动（SICA vs SC 主结果不受影响），exp-013 ablation\\n    改在 exp-002（K ablation, 60题×5K, 新 pipeline）数据上运行。exp-002 的 D012 子集 C0~53%，约 32\\n    题多候选 × 5K = 160 个多候选评估点，统计充足。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: 保持运行\\n    result: running\\n  - exp_id: exp-002\\n    role: ablation 数据源\\n    result: planned\\n  - exp_id: exp-013\\n    role: 策略变更\\n    result: planned\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-16 08:27 UTC\\n  summary: 'D023: Contingency plan 确认——如 SICA≤SC 则 pivot 到 Analysis Paper (Option\\n    A)，FOLIO 正向则嵌入为子 claim (Option C)'\\n  rationale: exp-001 中间结果 (N=157 PW) SICA-SC gap 反转至 -1.27pp，tiebreak win 降至 50%。Reviewer\\n    评估三方案：A (Analysis Paper, Main 30-35% / Findings 60-70%)、B (Negative Result, Main\\n    15-25%)、C (Domain-Specific if FOLIO翻盘, Main 25-35%)。选 A 为主线：论文价值从\\\"SICA 提升准确率\\\"转向\\\"理解\\n    symbolic consensus 的 operating conditions\\\"。C0 threshold pattern 成为核心贡献。Option\\n    C 嵌入 A（如 FOLIO 正向则作为\\\"domain formality → effectiveness\\\"子 claim）。不选 B（天花板低、NLP 社区对负面结果接受度有限）。决策点：exp-001\\n    FOLIO 70 题的 C0 和 delta。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: 决策依赖\\n    result: running\\n  - exp_id: exp-010\\n    role: cross-family 关键数据\\n    result: planned\\n  - exp_id: exp-011\\n    role: cross-family 关键数据\\n    result: planned\\n  - exp_id: exp-014\\n    role: reasoning 泛化\\n    result: planned\\n  depends_on:\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-16 18:33 UTC\\n  summary: 'D024: Dream-informed adjustments — reframe scope-to-claim gap, add odd-K/Logic-LM/Weighted-SC\\n    baselines, C0 regression methodology fix'\\n  rationale: 'Dream dream_20260516T054054 (full review mode) returned Weak Reject\\n    (3/6) across ALL three tiers (best/median/worst). Cross-tier consistent issues:\\n    (1) SICA framed as consensus but functionally a tiebreaker — scope-to-claim gap\\n    is #1 problem; (2) missing Logic-LM/LINC/weighted-SC baselines; (3) odd-K needed\\n    to validate mechanism beyond even-K ties; (4) C0 regression uses non-independent\\n    K-ablation points. Actions: added exp-002 K=11, new exp-015 Logic-LM baseline\\n    (CPU), new exp-016 Weighted SC baseline (CPU), expanded Anticipated Reviewer Concerns\\n    11-15, updated Story Spine related work. D021 cross-family/GSM8K/ablation already\\n    address other concerns. Re-dream required after exp-001 results + framing adjustments.'\\n  related_experiments:\\n  - exp_id: exp-002\\n    role: modified\\n    result: added K=11 odd-K test\\n  - exp_id: exp-015\\n    role: new\\n    result: Logic-LM baseline CPU-only\\n  - exp_id: exp-016\\n    role: new\\n    result: Weighted SC baseline CPU-only\\n  depends_on:\\n  - D021\\n  - D023\\n- id: D025\\n  date: 2026-05-16 18:35 UTC\\n  summary: 'D025: Activate D023 contingency — pivot to Analysis Paper. SICA +0.26pp\\n    at N=762 confirms no accuracy gain. Central contribution shifts to \\\"capability\\n    trap\\\" characterization + operating regime analysis across 4 domains × 7 models.'\\n  rationale: 'exp-001 at N=762/804 shows SICA=76.51% vs SC=76.25% (+0.26pp, well within\\n    noise at SE≈1.5pp). D012''s +3.3pp on N=60 was small-sample noise (SE≈6pp). Combined\\n    with Dream all-tiers Weak Reject and Reviewer''s scope evaluation: (1) Claim 1\\n    (accuracy gain) is dead — cannot claim SICA>SC; (2) Paper pivots to Analysis:\\n    \\\"When does symbolic consensus help? Empirical answer: rarely, and here''s the\\n    structural reason (capability trap)\\\"; (3) Central new insight: diversity (C0)\\n    and constraint quality are inversely correlated — symbolic methods need diversity\\n    (hard tasks) but constraint quality degrades on hard tasks; (4) Practical contribution:\\n    C0 as necessary-but-insufficient diagnostic + decision framework; (5) Scope expansion\\n    (StrategyQA + ARC) still proceeds — demonstrates capability trap across domains,\\n    not searching for positive results. exp-013 (constraint ablation) upgraded to\\n    P0 — must confirm MaxSAT mechanism is not vacuous.'\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: trigger\\n    result: SICA +0.26pp at N=762, no significant gain\\n  - exp_id: exp-013\\n    role: upgraded_P0\\n    result: Must confirm aggregation mechanism\\n  - exp_id: exp-010\\n    role: reframed\\n    result: Cross-family validation of negative result\\n  - exp_id: exp-011\\n    role: reframed\\n    result: Cross-family validation of negative result\\n  depends_on:\\n  - D023\\n  - D024\\n- id: D026\\n  date: 2026-05-16 19:21 UTC\\n  summary: exp-001 完成确认 D025 pivot：SICA≈SC (+0.25pp, n=804, n.s.)，FOLIO sub-claim\\n    dead (0.00pp)\\n  rationale: 804题全量评估确认：SICA vs SC gap仅+0.25pp（2题净差异），远低于显著性阈值。FOLIO 204题 gap=0.00pp，D012的+6.7pp确认为小样本噪声。数据坚实支持D025\\n    Analysis Paper pivot方向。FOLIO sub-claim正式放弃。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: primary\\n    result: +0.25pp overall (n.s.), FOLIO 0.00pp\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-16 20:29 UTC\\n  summary: exp-013 确认 MaxSAT≈count-only≈random-weight：SICA 的 aggregation mechanism\\n    无贡献 (C1 confirmed)\\n  rationale: 804题上三种 constraint aggregation 方法（MaxSAT/count-only/random-weight）802/804\\n    结果一致，McNemar p>0.7。MaxSAT 优化相对简单计数零优势，直接支持 Capability Trap 论文 C1：\\\"mechanism is\\n    vacuous when constraint quality is bounded by LLM capability\\\"。近似公式限制可接受（802/804\\n    agreement rate 压倒性）。\\n  related_experiments:\\n  - exp_id: exp-013\\n    role: primary\\n    result: MaxSAT=76.49%, count-only=76.62%, random=76.37%, SC=76.24%, all n.s.\\n  - exp_id: exp-001\\n    role: data source\\n    result: +0.25pp baseline\\n  depends_on:\\n  - D025\\n  - D026\\n- id: D028\\n  date: 2026-05-17 01:11 UTC\\n  summary: exp-002 中期：K=11 gap=0 确认 tiebreak-only；D012 vs K-ablation K=12 swing 8.33pp\\n    证明 n=60 结果为噪声\\n  rationale: K=11 (odd, no ties) SICA=SC 精确相等，证实 SICA 从不 override 清晰多数。更关键：同数据同设置\\n    K=12 两次实验结果相反（D012 +3.33pp vs K-ablation -5.00pp），8.33pp swing 直接证明小样本 gap 完全被\\n    trace 随机性淹没。FOLIO 上 SICA 恒定 76.67% 而 SC 随 K 提升——constraint quality 天花板限制了 SICA\\n    利用更多 traces 的能力。考虑升级 claim：从\\\"SICA≈SC\\\"到\\\"SICA≤SC at scale\\\"（更多 traces 帮 SC 但被 SICA\\n    constraint ceiling 限制）。\\n  related_experiments:\\n  - exp_id: exp-002\\n    role: primary\\n    result: K=11 gap=0, K=12 gap=-5pp, FOLIO SICA ceiling effect\\n  - exp_id: exp-001\\n    role: reference\\n    result: +0.25pp at K=12 n=804\\n  depends_on:\\n  - D025\\n  - D027\\n- id: D029\\n  date: 2026-05-17 02:14 UTC\\n  summary: exp-002 最终结果：SICA≤SC for all K (gap 0 to -5pp)，framing 维持\\\"SICA≈SC (mechanism\\n    vacuous)\\\"不升级为\\\"SICA&lt;SC\\\"\\n  rationale: K-ablation 6个K值全部 SICA≤SC，但 n=60 方差大（D012 vs K-ablation swing 8.33pp）。exp-001\\n    n=804 显示 +0.25pp (n.s.)。安全 framing 是\\\"gap indistinguishable from zero + mechanism\\n    introduces noise\\\"，而非\\\"SICA systematically worse\\\"。FOLIO 恒定 76.67% 是 constraint quality\\n    ceiling 的可视化证据。K=11 odd-K 确认 tiebreak-only。\\n  related_experiments:\\n  - exp_id: exp-002\\n    role: primary\\n    result: SICA≤SC all K; K=11 gap=0; FOLIO ceiling 76.67%\\n  - exp_id: exp-001\\n    role: anchor\\n    result: +0.25pp n=804 n.s.\\n  depends_on:\\n  - D028\\n- id: D030\\n  date: 2026-05-17 04:21 UTC\\n  summary: 'D030: 从 Analysis Paper 转向 Methods Paper — 利用诊断数据设计 Constraint Consistency\\n    Filtering 改进 SICA'\\n  rationale: '用户明确指示 methods paper 质量更高且更受欢迎。现有分析数据（exp-001/002/013/016）不浪费——变成论文动机和诊断部分。核心\\n    method idea: constraint consistency filtering（只保留跨多条 traces 重复出现的约束），利用已有 diversity\\n    提升 constraint quality 而不需更强模型。时间和资源充足（用户确认），pilot 可在当天 CPU-only 完成（如数据可用）。'\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: data source for pilot\\n    result: 804题 K=12 traces\\n  - exp_id: exp-013\\n    role: diagnosis\\n    result: MaxSAT≈count-only confirmed quality is bottleneck\\n  depends_on:\\n  - D025\\n  - D029\\n- id: D031\\n  date: 2026-05-17 08:06 UTC\\n  summary: 'D031: exp-011 +6.7pp 方向性正面但 p=0.22 不显著，启动 LLaMA-8B StrategyQA 200 题 powered\\n    test 验证 operating regime 假设'\\n  rationale: 'exp-011 LLaMA-8B 在 D012 60 题上 SICA +6.67pp (McNemar p=0.22, 6 discordant\\n    pairs 5:1)。n=60 检验力不足，无法排除噪声。但跨模型 pattern 清晰（弱→强: +6.7pp → +0.3pp → -1.7pp → 0pp），值得\\n    powered verification。StrategyQA 200 题 + LLaMA-8B 预期 multi-candidate rate 高（弱模型+commonsense\\n    推理），n=200 可检测 5pp 差异 (power>0.8)。若 p<0.05 → paper 升级为 Operating Regime Characterization；若\\n    p>0.1 → 维持 D025 Capability Trap analysis paper，LLaMA 作为 suggestive evidence。不在\\n    powered test 前更新 paper_framing.md。'\\n  related_experiments:\\n  - exp_id: exp-011-llama8b-v3\\n    role: 触发\\n    result: +6.67pp, p=0.22, directionally positive\\n  - exp_id: exp-010-mistral-v3\\n    role: 并行验证\\n    result: running, 9/60 done\\n  - exp_id: exp-001\\n    role: 对照\\n    result: Qwen-14B +0.25pp n.s.\\n  depends_on:\\n  - D030\\n  - D025\\n- id: D032\\n  date: 2026-05-17 08:20 UTC\\n  summary: 'D032: exp-010 Mistral 确认倒 U 型 pattern（sweet spot SC~55-65%），FOLIO 204\\n    升为最高优先级 powered test'\\n  rationale: Mistral-7B SICA≡SC (0.0pp, SC=48.3%, zero discordant)。与 LLaMA-8B (+6.7pp,\\n    SC=60%) 和 Qwen-14B (+0.25pp, SC=76%) 合看，pattern 是倒 U 型而非单调递减。Sweet spot 在 SC~55-65%：模型够弱产生多样性，但够强保证约束质量。LLaMA-8B\\n    在 FOLIO 上恰好在 sweet spot（SC=60%, +10pp at n=30），几乎必然在 n=200 时显著。StrategyQA 上 LLaMA-8B\\n    的 SC 未知，可能落在 sweet spot 外（类似 Mistral）。因此 FOLIO 204 是确定性更高的 powered test 选择。\\n  related_experiments:\\n  - exp_id: exp-010-mistral-v3\\n    role: 触发\\n    result: SICA=SC=48.3%, 0.0pp, zero discordant\\n  - exp_id: exp-011-llama8b-v3\\n    role: sweet spot 证据\\n    result: +6.67pp at SC=60%\\n  - exp_id: exp-001\\n    role: 对照\\n    result: +0.25pp at SC=76%\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-17 09:12 UTC\\n  summary: 'D033: exp-019 StrategyQA +2pp n.s. 确认 inverted U — operating regime 取决于\\n    model×task accuracy band (SC~55-65%)，非模型强弱'\\n  rationale: 'LLaMA-8B StrategyQA: SC=72%, SICA +2.0pp (net 4题, p>0.1 几乎确定)。LLaMA-8B\\n    在 commonsense 上不弱(72%)，只在 logic 上弱(60%)。这证明 operating regime 是 model×task specific，不是\\n    model-level property。5 个数据点画出完整曲线：SC=48%(0pp) → 60%(+6.7pp) → 72%(+2pp) → 76%(+0.3pp)\\n    → 97%(-1.7pp)。Sweet spot 在 SC~55-65%。D031 的 p<0.05 门槛未达，但 exp-020 FOLIO 204 (LLaMA-8B\\n    × FOLIO, SC=60% in sweet spot, +10pp signal) 仍是 definitive test。'\\n  related_experiments:\\n  - exp_id: exp-019-llama8b-strategyqa-200\\n    role: 触发\\n    result: +2.0pp, SC=72%, p>0.1\\n  - exp_id: exp-011-llama8b-v3\\n    role: sweet spot 参照\\n    result: +6.67pp, SC=60%\\n  - exp_id: exp-010-mistral-v3\\n    role: 下界\\n    result: 0pp, SC=48%\\n  depends_on:\\n  - D032\\n  - D031\\n- id: D034\\n  date: 2026-05-17 10:04 UTC\\n  summary: 'D034: exp-020 同题对比证伪 operating regime 假设——exp-011 +10pp 不可复现（同题反转 -3.3pp），D025\\n    Capability Trap 为最终论文方向'\\n  rationale: 'exp-020 FOLIO 204 中间数据（n=78）: SICA -2.94pp（SC 领先）。同题 30 FOLIO 对比：exp-011\\n    +10pp → exp-020 -3.3pp，delta 完全反转。SICA agreement 仅 56.7%，说明 K=12 n=30 方差极大，exp-011\\n    +6.67pp 是随机波动非真实信号。结合 exp-019 StrategyQA +2pp (p=0.424)，SICA 在任何 model×task regime\\n    下都不优于 SC。D025 Capability Trap analysis paper 是唯一合理方向。下一步：等 exp-020 全 204 题完成做最终录入，然后进入论文写作。'\\n  related_experiments:\\n  - exp_id: exp-020-llama8b-folio-204\\n    role: definitive test\\n    result: n=78 intermediate -2.94pp; 同题30 FOLIO 反转 -3.3pp\\n  - exp_id: exp-011-llama8b-v3\\n    role: 被证伪\\n    result: +6.67pp 确认为 sampling noise\\n  - exp_id: exp-019-llama8b-strategyqa-200\\n    role: 佐证\\n    result: +2pp p=0.424\\n  depends_on:\\n  - D033\\n  - D032\\n  - D031\\n  - D025\\n- id: D035\\n  date: 2026-05-17 11:29 UTC\\n  summary: 'D035: exp-020 FOLIO 204 确认 SICA≤SC (-2.4pp)，Operating Regime 彻底死亡，D025\\n    Capability Trap 为最终论文方向，进入写作阶段'\\n  rationale: exp-020 LLaMA-8B FOLIO 全量 204 题：SICA 60.8% vs SC 63.2%，delta=-2.4pp，方向反转。exp-011\\n    的 +10pp 是 n=30 小样本噪声（SE≈9pp）。四个 powered test 无一支持 SICA 优势（exp-001 +0.25pp n.s.,\\n    exp-019 +2.0pp p=0.424, exp-020 -2.4pp, exp-010 0.0pp）。D031 全部条件触发\\\"维持 D025\\\"路径。不再需要更多\\n    powered tests，进入 CPU ablations + 论文写作。\\n  related_experiments:\\n  - exp_id: exp-020-llama8b-folio-204\\n    role: definitive_test\\n    result: 'negative: -2.4pp, SICA worse than SC'\\n  - exp_id: exp-019-llama8b-strategyqa-200\\n    role: powered_test\\n    result: 'negative: +2.0pp p=0.424'\\n  - exp_id: exp-011-llama8b-v3\\n    role: refuted\\n    result: +10pp was n=30 noise\\n  - exp_id: exp-001\\n    role: anchor\\n    result: +0.25pp n.s. on 804q\\n  depends_on:\\n  - D034\\n  - D031\\n  - D025\\n- id: D036\\n  date: 2026-05-17 11:51 UTC\\n  summary: 'D036: Manager 要求实验覆盖自查——补 temperature ablation (T=0.3/0.5/1.0) + GSM8K\\n    pilot + Qwen-7B scaling + Mistral StrategyQA，总计 ~10h GPU'\\n  rationale: 自查发现两个 Critical 缺口：(1) Temperature ablation 直接检验 capability trap 核心机制（diversity↑但\\n    quality↓→SICA 仍无效），审稿人必问，~3h GPU；(2) GSM8K 数学域缺失，LLM reasoning 最标准 benchmark，~1h\\n    GPU。Important 缺口：Qwen-7B 补 scaling curve（C0 gradient claim），Mistral 跨域（消除 model-specific\\n    质疑）。所有补充实验总计 ~10h GPU，1 天内可完成，不影响 ARR May 25 写作排期。\\n  related_experiments:\\n  - exp_id: temperature-ablation\\n    role: new_critical\\n    result: 'planned: T=0.3/0.5/1.0 on Qwen-14B D012'\\n  - exp_id: exp-012\\n    role: new_critical\\n    result: 'planned: GSM8K 30q pilot'\\n  - exp_id: exp-004\\n    role: new_important\\n    result: 'planned: Qwen-7B scaling'\\n  - exp_id: mistral-strategyqa\\n    role: new_important\\n    result: 'planned: Mistral-7B StrategyQA 60q'\\n  depends_on:\\n  - D035\\n\", \"total_chars\": 26451, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff6183a5-4f94-4c74-86e0-4c63532c86cd",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "4a2c8ce4-6368-4bfa-a898-815e936aa5df",
  "sourceToolAssistantUUID": "ff6183a5-4f94-4c74-86e0-4c63532c86cd",
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

_source line 25 · 2026-05-17T15:59:45.383Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018weMVqorbrFsbkUg35n9vP`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a2c8ce4-6368-4bfa-a898-815e936aa5df",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RFGGDm7LBk64j3CnFa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79a2f199-cd53-4a3f-9ac7-da4fa0f15e93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lq6y785vfAvQzhrYNAfYLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12174,
      "cache_read_input_tokens": 23827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12174,
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

_source line 26 · 2026-05-17T15:59:45.394Z_

<details><summary>↩ Tool result · `toolu_018weMVqorbrFsbkUg35n9vP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ROADMAP.md\", \"content\": \"# symb_invariant_consensus — Research Dashboard\\n\\n> 最后更新: 2026-05-17 15:48 UTC | 更新原因: 标记已完成 CPU tasks + 更新 D036 进展\\n\\n## 核心方向\\n**D025 Capability Trap Analysis Paper (FINAL)**：SICA ≈ SC everywhere。Constraints lack discriminative power regardless of diversity level. 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research → Writing transition（D035/D036 确认最终方向 + 补充实验）\\n- **关键结论**:\\n  - 五个模型全部 negative: Qwen-14B +0.25pp, Mistral-7B 0pp, LLaMA-8B -2.4pp/+2.0pp, DeepSeek-R1-7B -3.3pp\\n  - exp-013: MaxSAT ≈ count-only（mechanism vacuous）\\n  - exp-015: Logic-LM baseline 无优势（62.7% vs SC 63.2%）\\n  - exp-009: SICA +48.7% overhead，全来自 LLM extraction\\n  - F2 per-problem 数据就绪（n=307, vote_entropy ρ=0.36）\\n  - DeepSeek-R1-Distill-7B 重分类为 instruction-scale（C0=58%，非 reasoning model）\\n- **已完成实验**: 12 个 success + 6 个 informative negative\\n- **D036 补充实验**: temperature ablation 运行中，GSM8K/Qwen-7B/Mistral-StrategyQA 脚本就绪\\n\\n## 近期任务\\n- [x] exp-009: overhead analysis（CPU，+48.7% wall time）\\n- [x] exp-015: Logic-LM baseline（CPU，无优势）\\n- [x] exp-016: weighted SC baseline（CPU，all n.s.）\\n- [x] constraint quality correlation + F2 per-problem CSV（CPU，n=307）\\n- [x] exp-014 DeepSeek-R1 完成（negative，C0=58%，reclassified）\\n- [x] registry 数据修复（C0 定义统一 + extraction_rate bug + notes）\\n- [ ] **temperature ablation T=0.3/0.5/1.0**（GPU 运行中，~2h remaining）\\n- [ ] exp-012 GSM8K pilot（GPU，temperature 后）\\n- [ ] exp-004 Qwen-7B scaling（GPU，symlink 已修复）\\n- [ ] Mistral-7B StrategyQA（GPU，脚本就绪）\\n- [ ] dream_simulate 结果处理（reviewing 阶段，即将完成）\\n- [ ] Paper Agent 启动写作（dream 后）\\n\\n## GPU 预算\\n- 分配: 1× RTX PRO 6000 Blackwell 98GB (cuda:0) on westd-32608\\n- 当前: temperature ablation 运行中（T=0.3→0.5→1.0 串行）\\n- 排队: GSM8K ~1h → Qwen-7B ~2h → Mistral-StrategyQA ~1.5h\\n- 累计已用: ~26h\\n\\n## 阻塞项\\n- 无硬阻塞。Dream reviewing 中（~10min），temperature ablation ~2h remaining。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D036 | 2026-05-17 | D036: Manager 要求实验覆盖自查——补 temperature ablation (T= | temperature-ablation, exp-012, exp-004, mistral-strategyqa |\\n| D035 | 2026-05-17 | D035: exp-020 FOLIO 204 确认 SICA≤SC (-2.4pp)，Operat | exp-020-llama8b-folio-204, exp-019-llama8b-strategyqa-200, exp-011-llama8b-v3, exp-001 |\\n| D034 | 2026-05-17 | D034: exp-020 同题对比证伪 operating regime 假设——exp-011  | exp-020-llama8b-folio-204, exp-011-llama8b-v3, exp-019-llama8b-strategyqa-200 |\\n| D033 | 2026-05-17 | D033: exp-019 StrategyQA +2pp n.s. 确认 inverted U — | exp-019-llama8b-strategyqa-200, exp-011-llama8b-v3, exp-010-mistral-v3 |\\n| D032 | 2026-05-17 | D032: exp-010 Mistral 确认倒 U 型 pattern（sweet spot S | exp-010-mistral-v3, exp-011-llama8b-v3, exp-001 |\\n| D031 | 2026-05-17 | D031: exp-011 +6.7pp 方向性正面但 p=0.22 不显著，启动 LLaMA-8B | exp-011-llama8b-v3, exp-010-mistral-v3, exp-001 |\\n| D030 | 2026-05-17 | D030: 从 Analysis Paper 转向 Methods Paper — 利用诊断数据设计 | exp-001, exp-013 |\\n| D029 | 2026-05-17 | exp-002 最终结果：SICA≤SC for all K (gap 0 to -5pp)，fra | exp-002, exp-001 |\\n| D028 | 2026-05-17 | exp-002 中期：K=11 gap=0 确认 tiebreak-only；D012 vs K-a | exp-002, exp-001 |\\n| D027 | 2026-05-16 | exp-013 确认 MaxSAT≈count-only≈random-weight：SICA 的  | exp-013, exp-001 |\\n\\n\\n\", \"total_chars\": 3075, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79a2f199-cd53-4a3f-9ac7-da4fa0f15e93",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "0e7c0576-6390-4a54-b589-6a5f9c7861e4",
  "sourceToolAssistantUUID": "79a2f199-cd53-4a3f-9ac7-da4fa0f15e93",
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

_source line 27 · 2026-05-17T15:59:46.789Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SdqhLjEFFhh3YJpyF7LYz8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/crd_audit_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e7c0576-6390-4a54-b589-6a5f9c7861e4",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RFGGDm7LBk64j3CnFa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ceca4782-6c9e-4423-abf6-662702f402bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lq6y785vfAvQzhrYNAfYLV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12174,
      "cache_read_input_tokens": 23827,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12174
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 23827,
          "cache_creation_input_tokens": 12174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12174,
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

_source line 28 · 2026-05-17T15:59:46.796Z_

<details><summary>↩ Tool result · `toolu_01SdqhLjEFFhh3YJpyF7LYz8`</summary>

```text
1	# CRD (Cross-Representation Disagreement) 实验审计报告
2	
3	**method: CRD** | 审计日期: 2026-05-15 | 服务器: westd-32608
4	
5	---
6	
7	## 1. 代码结构
8	
9	路径: `/root/autodl-tmp/crdd/`
10	
11	| 文件 | 功能 |
12	|------|------|
13	| `src/config.py` | API/路径/数据集配置 |
14	| `src/data_loader.py` | FOLIO 数据集加载器（本地 JSONL） |
15	| `src/formalize.py` | 双表征生成器：FOL→Z3 代码 + Python constraint 代码（两个独立 prompt，无信息泄漏） |
16	| `src/executor.py` | 代码沙箱执行（超时30s） |
17	| `src/disagree.py` | 分歧检测 + rule-based 错误分类器（9种错误类型） |
18	| `src/repair.py` | 定向修复（带诊断信息）+ 盲目重生成（对照组） |
19	| `src/pipeline.py` | 主 pipeline：加载 → 双表征 → 执行 → 分歧 → 错误分类 → 修复，支持断点续跑 |
20	| `src/baseline.py` | Qwen3-32B 直接回答（无双表征），确认 baseline acc ≤ 85% |
21	| `src/evaluate_mvp.py` | C1-C5 MVP gate 评估 |
22	| `src/evaluate_unified.py` | 统一评估脚本（含 bootstrap CI + Fisher exact test） |
23	| `src/deep_analysis.py` | 深度分析：错误分布、GT子集、分歧不对称性 |
24	| `src/analysis_supplement_ef.py` | 补充分析：phi 相关系数 + 成本效益分析 |
25	| `src/gt_true_case_study.py` | GT=True 子集中定向修复失败的 case study |
26	| `src/repair_only.py` | 单独重跑修复阶段 |
27	| `src/math_adapter.py` | MATH Level 5 数据集适配器 |
28	| `src/proofwriter_adapter.py` | ProofWriter 数据集适配器 |
29	| `src/run_proofwriter_pilot.py` | ProofWriter 试点运行脚本 |
30	| `src/self_consistency_baseline.py` | Self-consistency baseline（k=5 majority vote） |
31	| `analyze_crashes*.py` | 崩溃样本分析脚本 |
32	| `c4_analysis*.py` | C4 指标深度分析 |
33	
34	## 2. 方法概述（CRD vs SICA 差异）
35	
36	**CRD（Cross-Representation Disagreement Diagnostics）**：
37	- 核心思想：同一推理问题用两种**独立表征**（FOL/Z3 + Python constraint code）分别形式化并执行
38	- 两路结果不一致 → 触发分歧检测 → 错误分类 → 定向修复
39	- 关键假设：两种表征的错误模式相互独立（phi=0.189，弱相关，验证通过）
40	- 目标：通过跨表征对比实现**无需 ground truth 的错误定位和修复**
41	
42	**SICA（Symbolic Invariant Consensus Architecture）**：
43	- 项目要求的正式方法，使用符号不变量共识机制
44	- 与 CRD 的核心差异待 SICA 实现后对比
45	
46	## 3. 已完成实验列表
47	
48	### 3.1 Baseline（直接回答）
49	- **模型**: Qwen3-32B-AWQ（本地 vLLM）
50	- **数据集**: FOLIO validation, 50 题
51	- **准确率**: 74.0% (37/50)
52	- **结论**: ≤ 85%，数据集错误率充足，PASS
53	- **运行时间**: 2026-05-14 15:11–15:12
54	
55	### 3.2 Pipeline v1（初始83题）
56	- **模型**: Qwen3-32B-AWQ
57	- **数据集**: FOLIO validation, 83 题
58	- **运行时间**: 2026-05-14
59	- **关键指标**:
60	  - 分歧率 C1: 30.1% (25/83), 有效分歧率 32.1% (25/78)
61	  - 诊断率 C2: 88.0% (22/25)
62	  - 错误类型 C3: 5 种 (negation_error, logic_error, exec_crash, quantifier_error, unknown)
63	  - 定向修复优势 C4: +21.9pp (T:75% vs B:53.1%)
64	  - 定位准确率 C5: 44.4% (原始, 有 bug) → 80.0% (修正后)
65	  - FOL 准确率: 81.9%, Code 准确率: 62.7%, Oracle: 87.9%
66	- **MVP Gate**: 5/5 PASS
67	
68	### 3.3 Pipeline v2 & v3（10题试点）
69	- **v2 (10题)**: 分歧率 0%, 修复率 T:80% B:40%, FOL acc=90%, Code acc=60%
70	- **v3 (10题)**: 分歧率 0%, FOL acc=20%, Code acc=60%
71	- 小样本试运行，结果不稳定
72	
73	### 3.4 Pipeline v4 Full（211题，主实验）
74	- **模型**: Qwen3-32B-AWQ
75	- **数据集**: FOLIO validation, 全部 211 题（去重后 204 题有效）
76	- **运行时间**: 2026-05-14 ~ 2026-05-15（含 resume 和 repair 重跑）
77	- **关键指标 (all, N=204)**:
78	  - 分歧率 C1: 42.2% [95% CI: 35.3%–49.0%]
79	  - 诊断率 C2: 87.2% [79.7%–93.9%]
80	  - 错误类型 C3: 4 种 (exec_crash, logic_error, negation_error, quantifier_error)
81	  - 定向修复优势 C4: +4.7pp (T:69.8% B:65.1%), Fisher p=0.63 (不显著)
82	  - 定位准确率 C5(committed): 94.6% (35/37), C5(coverage): 53.0% (35/66)
83	- **关键指标 (excl Unknown, N=135)**:
84	  - C1: 38.5%, C2: 84.6%, C3: 3种, C4: -1.9pp (不显著), C5(committed): 96.2%
85	- **MVP Gate (all)**: 5/5 PASS
86	- **分歧不对称性**: FOL 正确 & Code 错 = 56, Code 正确 & FOL 错 = 10 (5.6:1)
87	- **准确率**: FOL=78.9%, Code=59.8%, Oracle=87.8%, Pipeline(repair+fallback)=81.4%
88	
89	### 3.5 GT 子集分析
90	| 子集 | N | 分歧率 | 诊断率 | 定向优势 |
91	|------|---|--------|--------|----------|
92	| GT=True | 72 | 30.6% | 90.9% | -13.6pp |
93	| GT=False | 63 | 47.6% | 80.0% | +6.7pp |
94	| GT=Unknown | 69 | 49.3% | 91.2% | +14.7pp |
95	
96	### 3.6 成本效益分析
97	- Token 总量: 3,543,447 tokens, 1,196 API calls
98	- 每样本平均: 17,370 tokens, 5.9 calls
99	- 成本倍数: 全 pipeline / 单表征 = 5.76x
100	- 收益: +21.6% 准确率提升 (vs Code-only baseline)
101	
102	### 3.7 ProofWriter 试点（进行中）
103	- **数据集**: ProofWriter OWA-D5, 30 题 pilot
104	- **状态**: 已完成 28/30 条（pipeline.log 仍在运行中）
105	- **运行时间**: 2026-05-15
106	
107	## 4. C1-C5 MVP Gate 定义
108	
109	| Gate | 名称 | 公式 | 阈值 |
110	|------|------|------|------|
111	| C1 | Disagree Rate | FOL判断 ≠ Code判断 / N | ≥10% |
112	| C2 | Diagnostic Rate | (≥1方正确) / n_disagree | ≥40% |
113	| C3 | Error Type Diversity | 不同错误类型数 | ≥2 |
114	| C4 | Targeted vs Blind | targeted_rate − blind_rate | >5pp |
115	| C5 | Localization Acc | stability.predicted == GT-actual | ≥60% |
116	
117	## 5. 已知问题
118	
119	1. **C4 统计不显著**: Fisher exact test p=0.63，定向修复优势在全集上无统计显著性
120	2. **C4 在 excl_unknown 上为负**: -1.9pp，说明对 GT=True/False 样本，定向修复反而略差于盲修
121	3. **C5 bug 修复历史**: 原始 C5 计算存在循环论证（predicted 和 actual 都从 GT 派生），已修复为用 stability check
122	4. **GT=True 子集定向修复效果差**: 定向优势 -13.6pp，case study 分析表明 GT=True 时 FOL 表征过于自信
123	
124	## 6. 值得保留的数据
125	
126	| 文件 | 内容 | 保留价值 |
127	|------|------|----------|
128	| `results/mvp_v4_full.jsonl` | 204 条完整 pipeline 结果 | 高（主实验原始数据） |
129	| `results/eval_unified_folio_d012.json` | 统一评估含 bootstrap CI | 高（统计分析） |
130	| `results/exp001_deep_analysis.json/txt` | 错误分布+GT子集分析 | 高（论文素材） |
131	| `results/exp001_supplement_ef.json/txt` | phi系数+成本效益 | 高（论文素材） |
132	| `results/baseline.json` | 50 题 baseline 原始结果 | 中 |
133	| `results/proofwriter_pilot.jsonl` | ProofWriter 28 条结果 | 中（跨数据集泛化） |
134	| `artifacts/c1c5_audit.md` | C5 bug 修复审计 | 中（方法论记录） |
135	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceca4782-6c9e-4423-abf6-662702f402bc",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "dfa3178c-aeba-49ec-a162-6c1a663aeb68",
  "sourceToolAssistantUUID": "ceca4782-6c9e-4423-abf6-662702f402bc",
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

_source line 29 · 2026-05-17T15:59:51.413Z_

Now let me also check the previous dream reports for comparison and look at experimental data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfa3178c-aeba-49ec-a162-6c1a663aeb68",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RFfDbjeWE1Zd7ms8NZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dc883a8-61d4-41ed-9c2f-723f696e8c5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvuHQARaHTzn5RE6gABZiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20787,
      "cache_read_input_tokens": 36001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20787,
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

_source line 30 · 2026-05-17T15:59:52.966Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PjjBs7hXuN27Q14Saq7o7X`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dc883a8-61d4-41ed-9c2f-723f696e8c5c",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RFfDbjeWE1Zd7ms8NZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c2dabed-67eb-4baa-abad-ff076051bab6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvuHQARaHTzn5RE6gABZiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20787,
      "cache_read_input_tokens": 36001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20787,
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

_source line 31 · 2026-05-17T15:59:52.981Z_

<details><summary>↩ Tool result · `toolu_01PjjBs7hXuN27Q14Saq7o7X`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\", \"content\": \"# Paper Framing — symb_invariant_consensus\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25)\\n- Deadline: May 25, 2026 (ARR submission)\\n\\n## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)\\n\\n1. **The Capability Trap**: Symbolic consensus methods face a fundamental tension: they require output diversity (C0>20%) to differ from voting, but extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to a noise injector. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B).\\n2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.\\n3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.\\n\\n## Core Insight\\nSymbolic constraint consensus doesn't improve LLM reasoning because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these constraints lack the discriminative power to distinguish correct from incorrect answers. MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, performing no better (often worse) than simple majority voting. We provide the first systematic empirical study characterizing this trap across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model.\\n\\n## Story Spine\\n- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?\\n- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.\\n- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.\\n- **Headline result**: \\\"Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level.\\\"\\n\\n## Anticipated Reviewer Concerns & Defensive Experiments\\n1. **\\\"Gains not statistically significant\\\"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.\\n2. **\\\"Only a better tiebreaker, not worth the overhead\\\"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis\\n3. **\\\"Only Qwen models\\\"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B\\n4. **\\\"Only one reasoning model\\\"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)\\n5. **\\\"Only logic domain\\\"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.\\n6. **\\\"MAX-SAT is over-engineering\\\"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.\\n7. **\\\"Random tiebreak baseline\\\"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.\\n8. **\\\"Why not just use a reasoning model?\\\"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.\\n9. **\\\"How does this compare to Logic-LM / LINC?\\\"** → exp-015: Logic-LM × K baseline (CPU-only)\\n10. **\\\"Weighted SC is simpler\\\"** → exp-016: Weighted SC baseline (CPU-only)\\n11. **\\\"C0 is trivially derived\\\"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.\\n12. **\\\"Within-family scaling?\\\"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.\\n\\n## Working Title\\n**\\\"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning\\\"**\\n(Alternatives: \\n- \\\"When Does Symbolic Consensus Help? An Empirical Answer: Rarely, and Here's Why\\\"\\n- \\\"Diversity Without Quality: The Fundamental Limitation of Constraint-Based LLM Aggregation\\\")\\n\\n## Paper Structure (EMNLP 8pp + appendix)\\n- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Capability Trap: C0 × Constraint Quality inverse correlation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Tiebreak Analysis: quality on tied questions only)\\n- Main Figures: F1 (Method Pipeline), F2 (Capability Trap Scatter: C0 vs Constraint Precision, colored by domain, hero figure), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: flat line, contrasting with theoretical upper bound)\\n- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data\\n\\n## Claim Risk Notes (Updated D035 + exp-014)\\n- **Claim 1 mechanism refinement**: \\\"Inverse correlation between diversity and quality\\\" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: \\\"constraints lack discriminative power regardless of diversity level.\\\" Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.\\n- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.\\n- **Claim 3 gradient risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \\\"binary indicator\\\". Need exp-004/007 for gradient data. OPEN.\\n- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.\\n- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.\\n\\n## Venue Fit Risks\\n- EMNLP: Negative-results/analysis paper. Must answer \\\"so what should practitioners do?\\\" → C0 as deployment diagnostic + overhead analysis.\\n- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.\\n- Statistical power: Now strong (N>1,200 combined across powered tests).\\n\", \"total_chars\": 8046, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c2dabed-67eb-4baa-abad-ff076051bab6",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "d9950738-fc13-4662-857a-66b5c205b2e8",
  "sourceToolAssistantUUID": "0c2dabed-67eb-4baa-abad-ff076051bab6",
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

_source line 32 · 2026-05-17T15:59:54.781Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01APEQx8zqiEAhdKYhBQAt6z`</summary>

```json
{
  "pattern": "**/dream_20260517T144412/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9950738-fc13-4662-857a-66b5c205b2e8",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RFfDbjeWE1Zd7ms8NZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f336e2b8-2952-43cd-b844-2344e5f272dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvuHQARaHTzn5RE6gABZiW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20787,
      "cache_read_input_tokens": 36001,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20787
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 36001,
          "cache_creation_input_tokens": 20787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20787,
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

_source line 33 · 2026-05-17T15:59:54.798Z_

<details><summary>↩ Tool result · `toolu_01APEQx8zqiEAhdKYhBQAt6z`</summary>

```text
artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md
artifacts/dream_reports/dream_20260517T144412/median/paper_framing.md
artifacts/dream_reports/dream_20260517T144412/worst/paper_framing.md
artifacts/dream_reports/dream_20260517T144412/best/review_report.md
artifacts/dream_reports/dream_20260517T144412/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f336e2b8-2952-43cd-b844-2344e5f272dd",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "88c29d11-b56f-4e41-862b-aa55cb718e1f",
  "sourceToolAssistantUUID": "f336e2b8-2952-43cd-b844-2344e5f272dd",
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

_source line 34 · 2026-05-17T15:59:59.117Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A6qSb8ZTbb84swA8VSFXoy`</summary>

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
  "parentUuid": "88c29d11-b56f-4e41-862b-aa55cb718e1f",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RGFdZ2HaV2xEvgvoxS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83e6bb0a-d5c4-4f34-a533-b890fccd60bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NitQRcidrxGGATUP6HZquf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3088,
      "cache_read_input_tokens": 56788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3088,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 35 · 2026-05-17T15:59:59.132Z_

<details><summary>↩ Tool result · `toolu_01A6qSb8ZTbb84swA8VSFXoy`</summary>

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
  "parentUuid": "83e6bb0a-d5c4-4f34-a533-b890fccd60bc",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "c57c5148-24e5-46d2-825c-ba75f6864196",
  "sourceToolAssistantUUID": "83e6bb0a-d5c4-4f34-a533-b890fccd60bc",
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

_source line 36 · 2026-05-17T15:59:59.401Z_

<details open><summary>🔧 Tool call — Read · `toolu_0191dxpmxGSEbUeZxELH8atB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c57c5148-24e5-46d2-825c-ba75f6864196",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RGFdZ2HaV2xEvgvoxS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcab97a6-57d2-4d3a-8838-cb65ea1b84ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NitQRcidrxGGATUP6HZquf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3088,
      "cache_read_input_tokens": 56788,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3088
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 56788,
          "cache_creation_input_tokens": 3088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3088,
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

_source line 37 · 2026-05-17T15:59:59.415Z_

<details><summary>↩ Tool result · `toolu_0191dxpmxGSEbUeZxELH8atB`</summary>

```text
1	---
2	dream_id: dream_20260517T144412
3	tier: median
4	overall_score: weak reject
5	timestamp: 2026-05-17T15:57:49.941192+00:00
6	---
7	
8	# Dream Review Report: "The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning"
9	
10	**Review Mode:** Full (2 Reviewers + Roundtable)
11	**Date:** 2026-05-17
12	**Venue Standard:** Top ML venue, ~25% acceptance rate, 6-point scale
13	
14	---
15	
16	## Reviewer R1: Methods and Experiments
17	
18	**Score: 4 (Weak Accept) | Confidence: Medium-high**
19	
20	### Summary
21	The paper proposes SICA (FOL constraint extraction + weighted MAX-SAT) and systematically demonstrates it provides no gain over majority voting across 5 models, 6 domains, and 1,300+ problems. The constraint ablation (MAX-SAT = counting = random-weight, 99.4% agreement) is the strongest evidence. The "capability trap" framework explains the null result: instruction-scale models produce diversity but non-discriminative constraints, reasoning models eliminate diversity.
22	
23	### Strengths
24	- **Strong core ablation.** Table 2 (MAX-SAT vs count-only vs random-weight, 801/804 agreement) directly demonstrates the mechanism is vacuous. More informative than simply reporting null accuracy differences.
25	- **Temperature ablation provides causal evidence.** Manipulating diversity continuously (C0 from 30% to 58%) while holding model/data constant rules out the "wrong operating point" objection.
26	- **Appropriate statistical protocol.** McNemar's test for paired binary outcomes is the correct choice. The paper does not over-claim and reports non-significance honestly.
27	- **Powered main experiment.** The n=804 combined test convincingly rules out practically meaningful effects (detectable effect at 80% power is ~3.5pp; observed Δ=+0.3pp).
28	- **Multiple baselines.** Logic-LM adaptation, weighted SC variants, and random-weight ablation systematically eliminate alternative explanations.
29	- **Overhead quantification.** Table 7 provides actionable practitioner guidance: 48% overhead for zero gain.
30	- **C0 as practical early-stopping gate.** Zero-cost and immediately deployable.
31	
32	### Weaknesses
33	- **Underpowered cross-model conditions.** Most conditions use n=60 (SE ≈ 6pp), where detectable effects are ~12-15pp. Claims about LLaMA-8B (+5.0pp), Qwen-7B (+1.7pp), Qwen-72B (-1.7pp) "confirming" the null are statistically meaningless individually. Only the Qwen-14B n=804 result is genuinely powered.
34	- **Potential method formulation issue.** The MAX-SAT formulation (Eq. 1) sums satisfaction scores per candidate answer, but it is unclear whether constraints from trace t_i are evaluated against answers *other than* the one t_i produced. If constraints are only evaluated under their own trace's answer, the method is structurally a weighted vote (each trace's weight = its own constraint count), and the negative result is trivially expected rather than surprising. This is potentially fatal to the paper's claim of testing "symbolic consensus."
35	- **Circularity concern in precision analysis.** Constraint precision is defined as "fraction of constraints discriminating correct from incorrect answers." If satisfaction checking uses the LLM rather than a ground-truth solver, the metric inherits the limitation it claims to measure.
36	- **No domain where SICA's advantage should be maximal.** All tested domains use relatively simple reasoning (binary/3-way/4-way classification). Harder multi-hop benchmarks (CLUTRR, PrOntoQA with long chains) where constraint structure carries more information are not tested.
37	- **Missing error analysis on discordant problems.** The 5 problems where MAX-SAT and count-only disagree are the most informative cases. Detailed examination would reveal what makes constraints occasionally useful.
38	- **Temperature ablation also underpowered.** n=60 per condition means effects under ~12pp cannot be detected. "Zero at every temperature" is not statistically established.
39	
40	### Questions for Authors
41	1. **Critical:** In the MAX-SAT formulation, are constraints from trace t_i evaluated against answers other than ans(t_i)? If not, the method is structurally a weighted vote.
42	2. **Critical:** Is SAT(c|a) computed by a ground-truth theorem prover (Z3) or by prompting the LLM?
43	3. What is the distribution of constraint counts per trace? If most traces produce 1-2 constraints, weighting has minimal effect.
44	4. What fraction of the 804 problems are multi-candidate (C0>0)? Is 307 the correct denominator for the precision analysis?
45	
46	### Missing Experiments
47	1. **Oracle extraction control.** Use a stronger model (GPT-4, Claude) as constraint extractor while keeping generators fixed. This distinguishes "fundamental limitation" from "extraction quality problem."
48	2. **Cross-answer constraint evaluation.** Modified SICA where all constraints are tested against all candidate answers, not just the trace's own answer.
49	3. **Harder reasoning benchmarks** where multi-hop constraint structure should be most informative.
50	4. **Detailed case study of the 5 discordant problems** in the constraint ablation.
51	
52	---
53	
54	## Reviewer R2: Novelty and Related Work
55	
56	**Score: 3 (Weak Reject) | Confidence: High**
57	
58	### Summary
59	The paper tests one symbolic aggregation method (SICA) and finds it equivalent to majority voting, attributing this to a "capability trap" where diversity and constraint quality are incompatible. While the constraint ablation is genuinely informative, the paper overclaims from one method instantiation to "symbolic consensus" broadly, has critically insufficient citations (~8 references), and the "capability trap" may be a redescription of known FOL-extraction limitations rather than a novel insight.
60	
61	### Strengths
62	- **Constraint ablation is genuinely informative.** The 99.4% agreement between MAX-SAT, counting, and random-weight is a clean, surprising result that would benefit the community.
63	- **Temperature ablation as causal evidence.** Well-designed continuous manipulation of diversity ruling out the "wrong operating point" objection.
64	- **Honest negative result.** The paper does not bury the finding but makes it central, with appropriate hedging ("across tested conditions").
65	- **Practical C0 gate.** Actionable for practitioners even if novelty is modest.
66	
67	### Weaknesses
68	- **Severely overgeneralized title and claims.** The paper tests ONE method (SICA: same-model FOL extraction + MAX-SAT) but titles itself "Why Symbolic Consensus Cannot Beat Majority Voting." Other symbolic approaches (graph-based consistency, program synthesis verification, LLM-as-judge with structured rubrics, learned symbolic verifiers, contrastive verification) are not tested. The title should scope to SICA specifically.
69	- **Critically insufficient references.** Only ~8 bibliography entries. A top-venue paper in this space should cite 30-50 works. Major omissions include:
70	  - Snell et al. (ICLR 2025 Oral) on test-time compute scaling
71	  - DeepSeek-R1 (2025) defining the reasoning model paradigm
72	  - FoVer (TACL 2025) on FOL verification for NL reasoning
73	  - Aristotle (ACL 2025) on logic-complete decomposition
74	  - LogicAgent (2025) on multi-perspective logical reasoning
75	  - DyLoS (EACL 2026) on multi-paradigm solver selection
76	  - Diversity-aware training for test-time scaling (2025)
77	  - DiVeRSe (ACL 2023) on multi-path step-aware verification
78	  - Math-Shepherd (ACL 2024) on outcome-conditioned step verification
79	  - Multi-agent debate literature
80	  - CRAFT/RASC/ReASC (SC variants 2024-2026)
81	- **"Capability trap" may be a redescription.** The finding reduces to: LLMs cannot extract discriminative FOL constraints from their own reasoning traces. This is arguably expected by anyone who has worked with Logic-LM or LINC, where formalization quality is the known bottleneck. Pan et al. (2023) explicitly discuss formalization errors.
82	- **Narrow method instantiation undermines generality.** SICA uses the same LLM for both generation and extraction. Without testing stronger/trained extractors, the paper establishes "SICA with same-model extraction doesn't work," not the broader claim.
83	- **No comparison with trained verifiers.** ORM/PRM are mentioned in Related Work but never compared. If trained verifiers succeed where SICA fails, the conclusion should be about extraction quality, not symbolic consensus as a category.
84	- **C0 diagnostic novelty is modest.** C0 is simply "how often do K traces disagree." Practitioners already know that unanimous traces leave nothing to improve. The framing as a "contribution" overstates the insight.
85	- **Possible citation error.** The Taubenfeld et al. (2024) reference appears to be about debate biases, not weighted SC.
86	
87	### Questions for Authors
88	1. Why was the same LLM used for both generation and extraction? Have you tested a stronger extractor?
89	2. Could contrastive prompting ("extract constraints that differentiate your answer from alternative X") improve discriminative power?
90	3. What happens with a trained constraint quality classifier as a pre-filter before MAX-SAT?
91	4. Is there a problem subset where constraint precision is high and SICA does outperform? A conditional method could be viable.
92	
93	### Missing Related Work
94	The Related Work section has 4 short paragraphs covering 4 topics with ~8 citations total. This is unacceptable for a top venue. The paper needs at minimum: (a) comprehensive coverage of neuro-symbolic reasoning methods (2023-2026), (b) test-time compute scaling literature, (c) verification and reranking methods beyond ORM/PRM, (d) SC variants and extensions, (e) constraint satisfaction in NLP with specific citations. The final paragraph ("Constraint satisfaction in NLP") has zero specific citations.
95	
96	---
97	
98	## Roundtable Synthesis
99	
100	### Step 2: Cross-Reviewer Reactions
101	
102	**R1 on R2's concerns:**
103	- Agrees the title overclaims; one instantiation cannot condemn "symbolic consensus" as a category.
104	- Agrees citation count (~8) is critically low and must be addressed.
105	- Acknowledges R2's point that the "capability trap" may redescribe known FOL-extraction limitations.
106	- Maintains the constraint ablation has standalone methodological value regardless of framing.
107	
108	**R2 on R1's concerns:**
109	- R1's concern about cross-answer constraint evaluation is potentially fatal. If SICA only evaluates constraints under their originating trace's answer, the method is structurally a weighted vote, making the negative result trivial rather than informative.
110	- Agrees most cross-model conditions (n=60) are underpowered.
111	- Notes that if R1's formulation concern is confirmed, the paper's contribution reduces further from "fundamental limitation" to "our particular weighted vote doesn't beat majority vote."
112	
113	### Step 3: Convergence — Points of Agreement
114	
115	1. **The constraint ablation (Table 2) is the paper's strongest and genuinely informative contribution.** MAX-SAT = counting = random-weight (99.4%) is clean, well-executed, and useful to the community.
116	2. **The title and claims overgeneralize.** Testing one method (SICA) does not support conclusions about "symbolic consensus" as a paradigm. Must be scoped down.
117	3. **Citation count is critically insufficient.** 8 references is unacceptable. At minimum 25-30 additional references needed, covering recent neuro-symbolic reasoning, test-time compute scaling, verification methods, and SC variants.
118	4. **Most conditions are underpowered.** Only the Qwen-14B n=804 combined result is genuinely powered. Other conditions (n=60) are suggestive at best.
119	5. **Missing oracle/cross-model extraction control.** Without testing whether better extraction breaks the trap, the paper cannot distinguish "fundamental impossibility" from "extraction quality problem."
120	6. **C0 diagnostic is modest.** Useful but not novel; it formalizes an obvious observation.
121	
122	### Step 3: Key Disagreement
123	
124	R1 (Score 4) weights methodological competence and the ablation's value more heavily. R2 (Score 3) weights novelty, positioning, and citation adequacy more heavily. Both agree these are genuine weaknesses; they differ on severity.
125	
126	The potential method formulation issue (R1's critical question about cross-answer evaluation) could be decisive: if confirmed as a design flaw, it would move R1's score to 3 as well.
127	
128	### Step 4: Consolidated Assessment
129	
130	**Overall Score: 3 (Weak Reject)**
131	**Confidence: High**
132	
133	### Verdict
134	
135	The paper presents a competent empirical investigation with one genuinely strong result (the constraint ablation showing MAX-SAT = counting). However, it falls short of the top-venue bar for three reasons:
136	
137	1. **Overclaiming.** The gap between what is tested (one extraction + aggregation pipeline) and what is claimed ("symbolic consensus cannot beat majority voting") is too large. The title and framing must be scoped to SICA specifically, or additional symbolic methods must be tested.
138	
139	2. **Insufficient scholarship.** ~8 references is far below the expected 30-50 for this topic area. Critical recent work on neuro-symbolic reasoning, test-time compute scaling, and verification methods is absent. The Related Work section cannot convince reviewers the authors understand the landscape.
140	
141	3. **Novelty concern.** The "capability trap" framing, while narratively effective, may redescribe known limitations of LLM-to-FOL translation rather than offering genuine new insight. The paper does not engage with whether this finding is already expected from the Logic-LM/LINC literature.
142	
143	### Actionable Revision Guidance
144	
145	- **Scope the title and claims to SICA specifically**, or test 2-3 additional symbolic consensus approaches.
146	- **Add 25+ references** covering neuro-symbolic reasoning (2023-2026), test-time compute, verification methods, SC variants, and constraint satisfaction.
147	- **Clarify the MAX-SAT formulation:** explicitly state whether constraints are evaluated cross-answer. If not, implement and test cross-answer evaluation.
148	- **Add an oracle extraction experiment** using a stronger model as extractor to distinguish extraction quality from fundamental limitation.
149	- **Acknowledge the power limitations** of n=60 conditions more prominently; present them as "suggestive" rather than "confirming."
150	- **Engage with prior work** on FOL extraction limitations (Logic-LM, LINC, FoVer) to establish what is genuinely new in the "capability trap" framing.
151	
152	### Experiment Coverage Assessment
153	
154	Against the full experiment design (17 imagined experiments), the paper covers all planned experiments:
155	- Core experiments (K ablation, tiebreak, scaling, C0 diagnostic, constraint ablation, temperature, overhead): all present
156	- Baseline comparisons (Logic-LM, weighted SC): all present
157	- Cross-model/domain coverage (7B, 14B, 72B, LLaMA-8B, QwQ-32B, 6 domains): all present
158	- Qualitative analysis (constraint case studies): present in Section 5.1
159	
160	Coverage is nearly complete. The weakness is not missing experiments but insufficient power for most conditions and overclaiming from the evidence obtained.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcab97a6-57d2-4d3a-8838-cb65ea1b84ad",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "6607902a-95ee-40e4-84a6-8e852789a0fc",
  "sourceToolAssistantUUID": "fcab97a6-57d2-4d3a-8838-cb65ea1b84ad",
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

_source line 38 · 2026-05-17T16:00:06.606Z_

Now I have a thorough understanding of the paper, its experimental history, and prior review feedback. Let me also check one more piece of data - the numbers that differ between the summary provided and the actual paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6607902a-95ee-40e4-84a6-8e852789a0fc",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RGbDXWMvcm3xPi9zKX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f102d3a-6fd7-4dba-a7e4-d504aabe49df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jj4eztqB1Hve1PhuhK1N5x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9493,
      "cache_read_input_tokens": 59876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9493,
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

_source line 39 · 2026-05-17T16:00:08.976Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MvB5NpyYN6X3CfMVySqjdf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper.tex",
  "offset": 108,
  "limit": 135
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f102d3a-6fd7-4dba-a7e4-d504aabe49df",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RGbDXWMvcm3xPi9zKX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67885251-c3e8-432b-8f2d-5048f6819688",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jj4eztqB1Hve1PhuhK1N5x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9493,
      "cache_read_input_tokens": 59876,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9493
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 59876,
          "cache_creation_input_tokens": 9493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9493,
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

_source line 40 · 2026-05-17T16:00:08.993Z_

<details><summary>↩ Tool result · `toolu_01MvB5NpyYN6X3CfMVySqjdf`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67885251-c3e8-432b-8f2d-5048f6819688",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "8add8c7d-c713-4376-8fa8-c722f719b26d",
  "sourceToolAssistantUUID": "67885251-c3e8-432b-8f2d-5048f6819688",
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

_source line 41 · 2026-05-17T16:00:13.504Z_

Now I have comprehensive understanding of the paper. Let me also note some discrepancies between the summary provided and the actual paper text, and check the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8add8c7d-c713-4376-8fa8-c722f719b26d",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RHJ3BwK5tj2Vgn7mLD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "384dc6b6-9c1b-456c-8dc7-60a8cd71fce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AE6La5jH9DpG4Xogv1Jrh4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3264,
      "cache_read_input_tokens": 69369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3264,
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

_source line 42 · 2026-05-17T16:00:14.676Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012Ro5SfVKenuQfNZ8VJHAz9`</summary>

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
  "parentUuid": "384dc6b6-9c1b-456c-8dc7-60a8cd71fce0",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RHJ3BwK5tj2Vgn7mLD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e6ad20b-1be4-4ad8-b92b-d8c788cfe9d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AE6La5jH9DpG4Xogv1Jrh4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3264,
      "cache_read_input_tokens": 69369,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3264
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 69369,
          "cache_creation_input_tokens": 3264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3264,
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

_source line 43 · 2026-05-17T16:00:14.693Z_

<details><summary>↩ Tool result · `toolu_012Ro5SfVKenuQfNZ8VJHAz9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml\", \"content\": \"# Literature Map — symb_invariant_consensus (SICA)\\n# Last updated: 2026-05-16\\n# Purpose: Track related work coverage for EMNLP 2026 submission\\n\\ndimensions:\\n\\n  self_consistency_and_variants:\\n    description: \\\"Self-Consistency (SC) decoding and improvements\\\"\\n    papers:\\n      - id: wang2023sc\\n        title: \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\"\\n        authors: \\\"Wang et al.\\\"\\n        venue: \\\"ICLR 2023\\\"\\n        arxiv: \\\"2203.11171\\\"\\n        relevance: \\\"Foundational SC method; our primary baseline\\\"\\n        status: must_cite\\n\\n      - id: chen2024usc\\n        title: \\\"Universal Self-Consistency for Large Language Model Generation\\\"\\n        authors: \\\"Chen et al.\\\"\\n        venue: \\\"ICML 2024\\\"\\n        arxiv: \\\"2311.17311\\\"\\n        relevance: \\\"Extends SC to free-form answers via LLM-based selection; alternative aggregation\\\"\\n        status: must_cite\\n\\n      - id: taubenfeld2025cisc\\n        title: \\\"Confidence Improves Self-Consistency in LLMs\\\"\\n        authors: \\\"Taubenfeld et al.\\\"\\n        venue: \\\"ACL Findings 2025\\\"\\n        arxiv: \\\"2502.06233\\\"\\n        relevance: \\\"Weighted voting via model confidence; reduces samples 40-50%. Shows SC can be improved with non-uniform weighting — SICA uses constraint-based weighting instead\\\"\\n        status: must_cite\\n\\n      - id: kim2026reasc\\n        title: \\\"Reliability-Aware Adaptive Self-Consistency (ReASC)\\\"\\n        authors: \\\"Kim et al.\\\"\\n        venue: \\\"2026\\\"\\n        relevance: \\\"Response-level confidence for early halting; 70-80% cost saving vs naive SC\\\"\\n        status: should_cite\\n\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — shows SC gains plateau early and can decline at high sample counts for strong models. Directly supports our QwQ-32B finding (SICA≡SC when model is too consistent)\\\"\\n        status: must_cite\\n\\n      - id: wan2024rasc\\n        title: \\\"Reasoning-Aware Self-Consistency (RASC)\\\"\\n        authors: \\\"Wan et al.\\\"\\n        venue: \\\"2024\\\"\\n        relevance: \\\"Combines answer-level and rationale-level features; reduces samples ~88%\\\"\\n        status: should_cite\\n\\n      - id: dsc2025\\n        title: \\\"Difficulty-Adaptive Self-Consistency\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL Findings 2025\\\"\\n        relevance: \\\"Ranks problem difficulty to allocate sampling budget; complementary efficiency approach\\\"\\n        status: optional\\n\\n  symbolic_reasoning_llm:\\n    description: \\\"Neuro-symbolic methods combining LLMs with formal solvers\\\"\\n    papers:\\n      - id: pan2023logiclm\\n        title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n        authors: \\\"Pan et al.\\\"\\n        venue: \\\"EMNLP Findings 2023\\\"\\n        arxiv: \\\"2305.12295\\\"\\n        relevance: \\\"LLM→FOL→solver pipeline; closest architectural ancestor to SICA. Key difference: Logic-LM uses single-path translation, SICA aggregates across multiple paths\\\"\\n        status: must_cite\\n\\n      - id: xu2026dylos\\n        title: \\\"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)\\\"\\n        authors: \\\"Xu et al.\\\"\\n        venue: \\\"EACL 2026\\\"\\n        arxiv: \\\"2510.06774\\\"\\n        relevance: \\\"Multi-paradigm solver selection (LP/FOL/CSP/SMT); evaluated on FOLIO+ProofWriter. Outperforms Logic-LM. Key difference: DyLoS selects solver type, SICA aggregates constraints across paths\\\"\\n        status: must_cite\\n\\n      - id: fover2025\\n        title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"TACL 2025\\\"\\n        relevance: \\\"FOL verification for NL reasoning; strong results on ProofWriter+FOLIO. Uses verification rather than aggregation\\\"\\n        status: must_cite\\n\\n      - id: li2025survey\\n        title: \\\"A Survey on LLM Symbolic Reasoning\\\"\\n        authors: \\\"Li et al.\\\"\\n        venue: \\\"2025 (under review)\\\"\\n        relevance: \\\"Comprehensive survey; positions SICA within the broader landscape\\\"\\n        status: should_cite\\n\\n      - id: constraintllm2025\\n        title: \\\"ConstraintLLM: A Neuro-Symbolic Framework for Industrial Constraint Programming\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Multi-instruction SFT for constraint extraction; different domain (industrial) but related extraction methodology\\\"\\n        status: optional\\n\\n  maxsat_constraint_nlp:\\n    description: \\\"MAX-SAT and constraint satisfaction applied to NLP/reasoning\\\"\\n    papers:\\n      - id: llm_meets_cp2025\\n        title: \\\"Large Language Model Meets Constraint Propagation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"IJCAI 2025\\\"\\n        relevance: \\\"LLM+constraint propagation integration; validates feasibility of constraint-based reasoning with LLMs\\\"\\n        status: should_cite\\n\\n      - id: satbench2025\\n        title: \\\"SATBench: Benchmarking LLMs' Logical Reasoning via SAT Problems\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Evaluates LLMs on SAT-formulated problems; establishes that LLMs struggle with pure SAT but can benefit from solver integration\\\"\\n        status: should_cite\\n\\n      - id: maxsat_local_search2025\\n        title: \\\"Optimizing Local Search-based Partial MaxSAT Solving via Initial Assignment Prediction\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Science China Information Sciences 2025\\\"\\n        relevance: \\\"Solver-side advances in partial MaxSAT; technical reference for our WPMS formulation\\\"\\n        status: optional\\n\\n  folio_proofwriter_sota:\\n    description: \\\"State-of-the-art methods on FOLIO and ProofWriter benchmarks\\\"\\n    papers:\\n      - id: logicagent2025\\n        title: \\\"From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning (LogicAgent)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2509.24765\\\"\\n        relevance: \\\"Multi-perspective logical reasoning; SOTA on logical reasoning benchmarks including FOLIO. +7.05% average gain\\\"\\n        status: must_cite\\n\\n      - id: aristotle2025\\n        title: \\\"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"ACL 2025\\\"\\n        relevance: \\\"Logic-complete decomposition framework; strong ProofWriter/FOLIO results\\\"\\n        status: must_cite\\n\\n      - id: qi2025symbolic_provers\\n        title: \\\"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation\\\"\\n        authors: \\\"Qi et al.\\\"\\n        venue: \\\"ICLR 2025\\\"\\n        arxiv: \\\"2502.06563\\\"\\n        relevance: \\\"LLM+symbolic prover combination; evaluated on FOLIO\\\"\\n        status: should_cite\\n\\n      - id: dissecting2025\\n        title: \\\"Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP Findings 2025\\\"\\n        arxiv: \\\"2506.04810\\\"\\n        relevance: \\\"Fine-grained analysis of LLM logical reasoning capabilities on ProofWriter/FOLIO\\\"\\n        status: optional\\n\\n  reasoning_model_diversity:\\n    description: \\\"Trace diversity in reasoning vs non-reasoning models; supports our QwQ-32B finding\\\"\\n    papers:\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — strong models produce near-identical paths, SC gains plateau/decline. Direct support for SICA≡SC on QwQ-32B\\\"\\n        status: must_cite\\n\\n      - id: diversity_aware_tts2025\\n        title: \\\"Diversity-Aware Training for Test-Time Scaling\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Under review 2025\\\"\\n        relevance: \\\"Independent reasoning attempts collapse into similar solutions; diversity training needed to unlock test-time scaling. Supports our claim that non-reasoning models have more useful diversity\\\"\\n        status: must_cite\\n\\n      - id: snell2025scaling_tts\\n        title: \\\"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters\\\"\\n        authors: \\\"Snell et al.\\\"\\n        venue: \\\"ICLR 2025 (Oral)\\\"\\n        arxiv: \\\"2408.03314\\\"\\n        relevance: \\\"Foundational test-time compute scaling; shows compute-optimal strategies vary by difficulty. Contextualizes why SICA needs diverse paths\\\"\\n        status: should_cite\\n\\n      - id: deepseek_r1_2025\\n        title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n        authors: \\\"DeepSeek-AI\\\"\\n        venue: \\\"Nature 2025\\\"\\n        arxiv: \\\"2501.12948\\\"\\n        relevance: \\\"Defines the reasoning model paradigm (RL-trained extended thinking); reference for why these models are highly self-consistent\\\"\\n        status: must_cite\\n\\n      - id: base_models_reason2025\\n        title: \\\"Base Models Know How to Reason, Thinking Models Learn When\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.07364\\\"\\n        relevance: \\\"RL teaches activation timing not new skills; implies reasoning models converge to similar reasoning patterns, reducing trace diversity\\\"\\n        status: should_cite\\n\\n      - id: korikov2025sc_ranking\\n        title: \\\"The Impact of LLM Self-Consistency and Reasoning Effort on Automated Scoring\\\"\\n        authors: \\\"Korikov et al.\\\"\\n        venue: \\\"arXiv 2026\\\"\\n        arxiv: \\\"2604.26954\\\"\\n        relevance: \\\"Temperature sampling helps but ensemble size (1→7) produces no significant gains; supports diminishing returns of naive SC\\\"\\n        status: optional\\n\\n  multi_path_aggregation:\\n    description: \\\"Methods for aggregating multiple reasoning paths beyond majority voting\\\"\\n    papers:\\n      - id: rc2025\\n        title: \\\"Representation Consistency for Accurate and Coherent LLM Answer Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2506.21590\\\"\\n        relevance: \\\"Aggregation via representation similarity; down-weights incoherent reasoning. Semantic alternative to SICA's symbolic approach\\\"\\n        status: should_cite\\n\\n      - id: multi_path_plan2025\\n        title: \\\"Enhancing Long Chain-of-Thought Reasoning through Multi-Path Plan Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.11620\\\"\\n        relevance: \\\"Multi-path aggregation at plan level rather than answer level\\\"\\n        status: optional\\n\\n      - id: crest2025\\n        title: \\\"Improving LLMs' Reasoning with Consistency-Driven Self-Training (CREST)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL 2025\\\"\\n        relevance: \\\"Consistency as training signal rather than inference-time aggregation\\\"\\n        status: optional\\n\\ngaps:\\n  resolved: []\\n  remaining:\\n    - dimension: \\\"reasoning_model_diversity\\\"\\n      gap: \\\"No published paper explicitly studies QwQ-32B trace diversity collapse under temperature sampling. Our empirical finding (3.6% multi-candidate across 83 problems) is novel but needs positioning against Loo et al. 2025 and Diversity-Aware TTS\\\"\\n    - dimension: \\\"maxsat_constraint_nlp\\\"\\n      gap: \\\"No direct precedent for weighted partial MAX-SAT as multi-path consensus mechanism in NLI. SICA's formulation appears novel — must frame clearly in Related Work\\\"\\n    - dimension: \\\"self_consistency_and_variants\\\"\\n      gap: \\\"Should verify if CRAFT (mentioned in project docs) is a real published method or internal shorthand\\\"\\n\", \"total_chars\": 11286, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e6ad20b-1be4-4ad8-b92b-d8c788cfe9d3",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "600bb5a0-9739-4b78-890f-e025719eea2b",
  "sourceToolAssistantUUID": "8e6ad20b-1be4-4ad8-b92b-d8c788cfe9d3",
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

_source line 44 · 2026-05-17T16:00:18.694Z_

Now I have a complete picture. Let me also note several discrepancies between the summary provided and the actual paper to inform my review. Let me now write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "600bb5a0-9739-4b78-890f-e025719eea2b",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RHic3zYNepx6cwAAKM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9aae962-2509-4bd8-b6a3-a5ed8d04e14d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4rRTnRUyp2wYTb4X4gyNt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4193,
      "cache_read_input_tokens": 72633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4193,
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

_source line 45 · 2026-05-17T16:00:20.546Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DMuvUBv1KJoiJqNKkHqrMH`</summary>

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
  "parentUuid": "a9aae962-2509-4bd8-b6a3-a5ed8d04e14d",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RHic3zYNepx6cwAAKM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b821f82-a0f9-4d7b-bcc7-17f04bd91069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4rRTnRUyp2wYTb4X4gyNt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4193,
      "cache_read_input_tokens": 72633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4193,
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

_source line 46 · 2026-05-17T16:00:20.549Z_

<details><summary>↩ Tool result · `toolu_01DMuvUBv1KJoiJqNKkHqrMH`</summary>

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
  "parentUuid": "7b821f82-a0f9-4d7b-bcc7-17f04bd91069",
  "isSidechain": true,
  "promptId": "5e492643-57ad-46ed-ad12-151640e95cd7",
  "agentId": "a99d1bfd64c49d1b3",
  "type": "user",
  "uuid": "bf4055fb-b215-462f-ad02-4ea1cdd6e5d3",
  "sourceToolAssistantUUID": "7b821f82-a0f9-4d7b-bcc7-17f04bd91069",
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

_source line 47 · 2026-05-17T16:02:18.534Z_



Now I have all the information needed to write a thorough review. Let me compose it.

---

## Review: "The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning"

**Reviewer R1 — Focus: Methodology Soundness, Experimental Rigor, Statistical Validity, Reproducibility**

---

### 1. Summary

This paper presents SICA (Symbolic Invariant Consensus Aggregation), which extracts FOL constraints from K reasoning traces and uses weighted MAX-SAT to select answers, then systematically evaluates it against Self-Consistency (majority voting). Across 5 model families, 3+ reasoning domains, and >1,300 problems, the authors find SICA provides no significant accuracy gain over SC. They attribute this to a "capability trap": instruction-scale models produce diverse outputs but non-discriminative constraints, while reasoning models eliminate diversity entirely. The constraint ablation (MAX-SAT = count-only = random-weight, 802/804 agreement) is the central mechanistic evidence.

---

### 2. Strengths

- **Well-powered main experiment.** The Qwen-14B FOLIO+ProofWriter experiment (n=804) is appropriately sized. At this sample size, an effect of ~3.5pp would be detectable at 80% power; the observed delta of +0.25pp convincingly rules out practically meaningful gains. McNemar's test is the correct paired-comparison test for binary outcomes.

- **The constraint ablation (Table 3) is the paper's strongest result.** MAX-SAT, count-only, and random-weight produce 802/804 identical answers (McNemar p=0.99). This is a clean, well-designed experiment that directly establishes the solver contributes nothing beyond vote counting. This result alone would be a useful contribution to the community.

- **Per-problem constraint precision analysis (Table 2) is methodologically sound.** Analyzing 307 multi-candidate problems at per-problem granularity, with mean precision 0.505 (+/- 0.148), median 0.500, and flat regression against vote entropy (slope=0.003, r^2=0.002), provides fine-grained evidence for the mechanism. The symmetric distribution (28% below 0.40, 25% above 0.60) is particularly informative: occasional high-precision problems are cancelled by reverse-discriminating ones.

- **K=11 odd-K ablation is a well-designed diagnostic.** At odd K, SC ties are impossible. The resulting delta=0 (Table 5) directly confirms SICA's only effective mechanism is tiebreaking, not constraint-based override. This is a clean experimental design.

- **Temperature ablation (Table 6) provides quasi-causal evidence.** Manipulating diversity continuously (C0 from 28% to 68%) while holding model and data constant rules out the "wrong operating point" objection. The monotonic C0 response to temperature validates that diversity is experimentally controllable.

- **Honest framing of negative results.** The decision log (D025 pivot from methods paper to analysis paper) shows the authors pursued positive results, failed to find them, and honestly reported the null. The paper does not cherry-pick or bury unfavorable results (e.g., LLaMA-8B +6.67pp at n=60 is explicitly called out as a small-sample artifact, confirmed by the n=204 replication yielding -2.4pp).

- **Overhead quantification (Section 6.3) is practically useful.** 49% wall-time overhead decomposed by stage (constraint extraction 47%, solver <0.01%) provides actionable guidance. The observation that the solver itself is negligible while extraction dominates is non-obvious.

- **Within-Qwen scaling analysis provides three distinct C0 levels** (7B: 65%, 14B: 53%, 72B: 15%) spanning the capability spectrum, all yielding delta approximately 0. This strengthens the generality claim within a controlled model family.

---

### 3. Weaknesses

- **W1 (Major): Underpowered non-central experiments undermine breadth claims.** 8 of 9 conditions in Table 1 use n <= 60 (SE approximately 6-8pp). At n=60, the minimum detectable effect at 80% power is approximately 12-15pp. Claims that Qwen-7B (-1.7pp), Qwen-72B (0.0pp), Mistral-7B (0.0pp, from the text but absent from Table 1), and DeepSeek-R1-7B (-3.3pp) "confirm" the null are statistically unjustified. These experiments cannot distinguish a true 5pp effect from zero. The "combined N>1,300" figure in the abstract is misleading: 804 of those come from one model on one domain pair. The paper should present these conditions as "consistent with" rather than "confirming" the null, and acknowledge the power limitations explicitly.

- **W2 (Major): Self-extraction confound is unaddressed.** The same model generates traces and extracts constraints. A model that commits a reasoning error in trace generation will likely extract constraints consistent with that error (the paper's own Section 6.4 confirms: constraints formalize premises, not reasoning steps). Without testing a stronger or separate extraction model, the paper cannot distinguish "symbolic consensus is fundamentally limited" from "same-model self-extraction of constraints is limited." This is a critical gap because the title and claims generalize to "symbolic consensus" broadly. An oracle experiment using FOLIO's gold FOL annotations, or using a stronger model (e.g., 72B or frontier) as extractor while keeping 14B as generator, would directly resolve this confound.

- **W3 (Major): Domain coverage is substantively thinner than claimed.** The paper claims "3 reasoning domains," but SICA is genuinely tested (C0 > 20%) almost exclusively on formal logic (FOLIO+ProofWriter). On StrategyQA (C0=10%), ARC (C0=5%), and GSM8K (C0=10%), the model's high accuracy suppresses diversity, making these conditions degenerate (SICA has nothing to resolve). These conditions are uninformative about whether symbolic consensus could help in domains where disagreement exists. The only non-logic conditions with meaningful C0 are the LLaMA-8B powered tests (StrategyQA n=200 and FOLIO n=204), which are not in Table 1. Claiming domain generality from degenerate conditions is misleading.

- **W4 (Major): Missing figures.** The hero scatter plot (F2: per-problem constraint precision vs. vote entropy) and the C0-vs-gap diagnostic plot (F4) are referenced in the text but not rendered as actual figures. Cross-references appear as "Figure ??" (broken LaTeX refs). For a paper whose central argument is about the relationship between diversity and constraint quality, the absence of these visualizations is a serious presentation failure. These are the paper's most important visual evidence.

- **W5 (Major): 8 references is critically below venue standards.** EMNLP submissions typically cite 30-60 papers. The paper's own literature_map.yaml identifies 25+ relevant papers with "must_cite" or "should_cite" status, most absent from the submission. Critical omissions include:
  - Snell et al. (ICLR 2025 Oral): test-time compute scaling, directly contextualizes the diversity-capability tradeoff
  - DeepSeek-R1 technical report: essential for characterizing the reasoning model paradigm and QwQ-32B's behavior
  - DyLoS (EACL 2026), FoVer (TACL 2025), Aristotle (ACL 2025): neuro-symbolic methods that reportedly achieve gains on the same benchmarks (FOLIO, ProofWriter)
  - Loo et al. (2025): SC scaling plateaus, directly supports the QwQ-32B finding
  - Taubenfeld et al. (2025): confidence-weighted SC (the paper cites their 2024 debate biases paper instead, which appears to be a citation error)
  - LogicAgent, SATBench, and other recent neuro-symbolic reasoning methods

- **W6 (Moderate): The MAX-SAT formulation (Section 3.1, step 3) raises a critical ambiguity.** The formula $a^* = \arg\max_a \sum_{i: \text{ans}(t_i)=a} \sum_j w(c_{i,j}) \cdot \mathbf{1}[\text{SAT}(c_{i,j}|a)]$ only sums over traces whose answer matches candidate $a$. This means constraints from trace $t_i$ are never evaluated against answers other than $\text{ans}(t_i)$. If so, the method is structurally a weighted vote: each candidate's score is the total constraint weight from its supporting traces. The "symbolic consensus" aspect (cross-trace constraint evaluation against all candidates) is absent. If this reading is correct, the negative result is trivially expected rather than surprising, because the method never actually performs cross-answer constraint checking. This must be clarified.

- **W7 (Moderate): Temperature ablation is underpowered and confounded.** The temperature ablation (Table 6) uses n=60 per condition. At this sample size, effects under ~12pp cannot be detected. The claim that "the gap remains zero at every level" is statistically unsupported (inability to reject the null is not evidence of null). Additionally, temperature simultaneously affects diversity, trace quality (SC drops 76.7% to 70.0%), and extraction quality (rate drops 91% to 87%). The null gap at T=1.0 could reflect worse constraints from noisier traces cancelling any diversity benefit, rather than a structural impossibility.

- **W8 (Moderate): Discrepancies between the summary and paper text.** Several numbers differ between what is stated in the paper summary and the actual paper:
  - Qwen-14B C0: summary says 38%, paper says 53%
  - Qwen-7B SC: summary says 56.7%, paper says 55.0%; SICA: summary says 60.0%, paper says 53.3%
  - Qwen-72B C0: summary says 22%, paper says 15%; SC: summary says 85.0%, paper says 86.7%
  - Tiebreak: summary says 5 of 60 problems, paper says 10 of 60
  - K ablation values differ at several points
  - Temperature ablation: summary shows positive deltas (+1.7pp, +8.3pp at T=1.0), paper shows zero or negative deltas
  - Constraint precision: summary says 0.57 mean, paper says 0.505
  
  These may reflect different paper versions, but they raise concerns about data integrity and version control. The final paper should be carefully checked for internal consistency.

- **W9 (Minor): The Bonferroni correction mentioned in the summary (adjusted alpha approximately 0.01 for 5 families) does not appear in the paper text.** The paper reports raw p-values without multiple comparison correction. Given 9 conditions in Table 1, some form of correction should be discussed, even if the conclusion (all n.s.) does not change.

- **W10 (Minor): QwQ-32B row in Table 1 reports "--" for SC and SICA accuracy.** If the experiment was run, the actual numbers should be reported. If the experiment was too small or the data is unreliable, this should be stated.

---

### 4. Questions for Authors

1. **(Critical)** In the MAX-SAT formulation, are constraints from trace $t_i$ evaluated against candidate answers other than $\text{ans}(t_i)$? The formula as written sums only over traces matching each candidate. If constraints are never tested cross-answer, the method is structurally a weighted vote, and the negative result is trivially expected. Please clarify.

2. **(Critical)** Is $\text{SAT}(c_{i,j} | a)$ computed by a ground-truth theorem prover (Z3) or by prompting the LLM? If the latter, the precision metric inherits the limitation it claims to measure.

3. Have you tested using a stronger model (e.g., Qwen-72B or a frontier model) as the constraint extractor while keeping Qwen-14B as the trace generator? This would separate extraction quality from the aggregation mechanism and determine whether the "capability trap" is fundamental or an artifact of same-model extraction.

4. FOLIO provides human-authored gold FOL annotations. Have you considered an oracle experiment using these gold annotations as constraints to establish an upper bound on what perfect extraction would achieve?

5. The constraint-sharing analysis (78% shared, 12% discriminative) in Section 6.4 covers only 8 problems. Has this ratio been verified at scale across the 307 multi-candidate problems?

6. What is the distribution of constraint counts per trace? If most traces produce only 1-2 constraints, weighting has minimal effect regardless of quality, and the negative result would be expected for a different reason (insufficient signal density).

7. For the 2 problems where MAX-SAT and count-only disagree (out of 804), can you characterize what makes them different? These are the most informative cases for understanding when constraint structure could matter.

8. The LLaMA-8B powered replications (StrategyQA n=200 +2.0pp, FOLIO n=204 -2.4pp) are mentioned in the text but not shown in Table 1. Why were these excluded from the main results table?

---

### 5. Minor Issues

- The Taubenfeld et al. (2024) citation appears to reference their debate biases paper rather than their 2025 confidence-weighted SC paper. This should be corrected.
- "Figure" cross-references appear broken (rendering as "??"). Fix LaTeX labels.
- The paper uses a custom geometry package with 2.5cm margins rather than the target venue template. For EMNLP/ARR submission, the official template must be used.
- Section 6.4 mentions "8 representative problems" but the selection criteria are not described. How were these chosen? Random sampling or hand-picked?
- The Rogers et al. (2020) "Primer in BERTology" citation for the negative results tradition is a stretch; more relevant precedents exist (e.g., Reimers & Gurevych 2017 on reporting score distributions, or Dodge et al. 2020 on fine-tuning instability).
- The abstract states "4 instruction-scale model families" but the paper tests Qwen (multiple sizes), LLaMA, Mistral, and DeepSeek-R1-Distill. Mistral-7B results (mentioned in framing documents and text) are absent from Table 1.

---

### 6. Overall Assessment

The paper has a genuinely strong empirical core. The constraint ablation (Table 3: MAX-SAT = count-only = random-weight, 802/804 agreement) and the per-problem precision analysis (Table 2: mean=0.505, flat against vote entropy) are well-executed experiments that convincingly demonstrate, for the tested configuration, that LLM-extracted FOL constraints lack discriminative power and the MAX-SAT solver degenerates to counting. The K=11 odd-K test confirming tiebreak-only mechanism is a particularly elegant diagnostic. The overhead analysis adds practical value. These results would benefit the community.

However, the paper suffers from a fundamental scope-evidence mismatch. The title claims "symbolic consensus cannot beat majority voting," but only one specific pipeline is tested (same-model FOL extraction + MAX-SAT). The self-extraction confound (W2) means the paper establishes "SICA with same-model extraction does not work" rather than "symbolic consensus is fundamentally limited." Other neuro-symbolic methods (DyLoS, Aristotle, FoVer) reportedly achieve gains on the exact same benchmarks. Without a stronger-extractor control or gold-FOL oracle experiment, the paper cannot rule out that the bottleneck is extraction quality rather than an inherent limitation of constraint-based aggregation. The critically thin bibliography (8 references vs. the expected 30-50), missing figures, underpowered cross-model conditions, and possible MAX-SAT formulation issue (W6) further weaken the submission. The paper needs significant revision in claim scoping, scholarship, and presentation before it meets the bar for a top venue.

---

### 7. Score and Confidence

**Score: 3 (Weak Reject)**

The mechanism analysis is publishable-quality empirical work, but the scope-evidence mismatch (title generalizes far beyond what is tested), critically insufficient references, missing figures, unaddressed self-extraction confound, and the potential that the MAX-SAT formulation is structurally just a weighted vote (making the negative result trivially expected) collectively place the paper below the acceptance threshold. With narrowed claims, expanded scholarship, rendered figures, and a stronger-extractor control experiment, this could become a solid contribution.

**Confidence: 4/5 (High)**

I have carefully examined the paper's methodology, statistical approach, and experimental design. The main uncertainty is the MAX-SAT formulation question (W6): if the method truly never evaluates constraints cross-answer, my score would drop to 2 (Reject) because the negative result would be uninformative. If cross-answer evaluation is confirmed, the score remains 3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf4055fb-b215-462f-ad02-4ea1cdd6e5d3",
  "isSidechain": true,
  "agentId": "a99d1bfd64c49d1b3",
  "requestId": "req_011Cb8RJCVM7EvwwBSsPEQpi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b07e886b-2ade-4c22-adab-530e1958e53b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c45da324-b22a-497d-aa29-83b1dc828269",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwTfu3ARjuCHWGBbwkBeEr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 76826,
      "output_tokens": 4150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 703
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4150,
          "cache_read_input_tokens": 76826,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 703,
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
