# Research conversation: Verify that all R18 review issue fixes are present in the LaTeX source files. Check each item below by grepping for the 

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 104
- **Recorded user turns:** 1
- **Tool calls:** 50
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2b27f987e62a3e88.jsonl`
- **Structured JSON:** [`1379f5d946aa123ffdf2.json`](../../sessions/13/1379f5d946aa123ffdf2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

104 recorded events

### User

_source line 1 · 2026-05-22T23:26:39.034Z_

Verify that all R18 review issue fixes are present in the LaTeX source files. Check each item below by grepping for the expected text in the corresponding .tex file. Report which items are confirmed vs missing.

Base path: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/

Items to verify:

1. **R18-N1** (C2 demotion): In abstract.tex and introduction.tex, C2 should NOT have specific type ordering (no "scopal > lexical > ..."), instead should say something about "per-type effects range" or "partial ordering" or "incompleteness as upper bound". In introduction.tex contributions, contribution (2) should mention "variance decomposition" + "17×" NMI.

2. **R18-N2** (Judge confound): In experiments.tex, Fig 3 caption should contain "Each model was evaluated by a single judge" or similar. Section 5.4 should mention "suggestive" + "single-judge-per-model".

3. **R18-N3** (Taxonomy demotion): In related_work.tex, should contain "experimental instrument" or "controlled causal analysis rather than a proposed classification standard". In introduction.tex contribution (3) should mention "error analysis" + "failure mechanisms" + "convergent".

4. **R18-N4** (DN demotion): Check that "Disambiguation Neglect" appears lowercase as "disambiguation neglect" (with \emph{}) throughout. Check analysis.tex, discussion.tex, related_work.tex.

5. **R18-W1** (LPM footnote): In experiments.tex, a footnote near Type III SS should contain "magnitudes differ between linear and logistic" and "Tjur" citation.

6. **R18-W3** (Incompleteness upper-bound): In experiments.tex §5.1, should contain "upper bound that includes information addition" and "confound-controlled range is +18.7pp".

7. **R18-W5** (SOPBench): In experiments.tex §5.1, should contain "SOPBench" and "3/5 significant" or similar.

8. **R18-W7** (Abstract numbers): In abstract.tex, should NOT contain "2,997 episodes" or "1.0% for model identity".

9. **R18-W8** (Page limit): This was verified visually - skip.

10. **R18-W9** (Conclusion domain-qualified): In conclusion.tex, should contain "customer-service" or "policy-governed deployments" to limit scope.

For each item, grep the relevant file and report CONFIRMED or MISSING with the matching line.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "7582fdd7-5f5f-48db-8599-c813d1f95a8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T23:26:39.039Z_

```json
{
  "parentUuid": "7582fdd7-5f5f-48db-8599-c813d1f95a8a",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "121a5853-c93f-451d-a867-3a6ea76d99fe",
  "timestamp": "2026-05-22T23:26:39.039Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

---

### Assistant

_source line 3 · 2026-05-22T23:26:41.639Z_

I'll check each item systematically by grepping the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "121a5853-c93f-451d-a867-3a6ea76d99fe",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b55c1632-e897-48f6-a5cb-aa06273d8fcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 4 · 2026-05-22T23:26:44.785Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AExiVqdYkia374oYoMM56X`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== R18-N1: C2 demotion ===\"\necho \"--- abstract.tex: check for scopal > lexical ---\"\ngrep -n \"scopal\\|lexical\\|per-type\\|partial ordering\\|incompleteness as upper\" \"$BASE/abstract.tex\" | head -20\n\necho \"--- introduction.tex: check for scopal > lexical ---\"\ngrep -n \"scopal\\|lexical\\|per-type\\|partial ordering\\|incompleteness as upper\" \"$BASE/introduction.tex\" | head -20\n\necho \"--- introduction.tex: check for variance decomposition + 17x NMI ---\"\ngrep -n \"variance decomposition\\|17.*NMI\\|NMI.*17\\|17×\\|17x\" \"$BASE/introduction.tex\" | head -20",
  "description": "Check R18-N1: C2 demotion in abstract and introduction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b55c1632-e897-48f6-a5cb-aa06273d8fcb",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bedf927-c87f-405a-b670-c21ca115b532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 5 · 2026-05-22T23:26:44.888Z_

<details><summary>↩ Tool result · `toolu_01AExiVqdYkia374oYoMM56X`</summary>

```text
=== R18-N1: C2 demotion ===
--- abstract.tex: check for scopal > lexical ---
--- introduction.tex: check for scopal > lexical ---
4:A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
19:Our results show that policy ambiguity is consistently nocuous for LLM agents ($+34.0$ pp violation rate increase, conditional OR $= 15.1$), but risk is driven by individual clause wording (22.4\% of variance) rather than type membership (0.4\%). The taxonomy's value lies in predicting failure mechanisms: type membership predicts the dominant mechanism 17$\times$ better than it predicts violation rate ($\text{NMI} = 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), enabling targeted diagnosis (\S\ref{sec:discussion}). Incompleteness is consistently the highest-risk type (46--62\% across all models); the remaining types form a partial ordering with robust extremes but margin-dependent mid-tier structure.
--- introduction.tex: check for variance decomposition + 17x NMI ---
19:Our results show that policy ambiguity is consistently nocuous for LLM agents ($+34.0$ pp violation rate increase, conditional OR $= 15.1$), but risk is driven by individual clause wording (22.4\% of variance) rather than type membership (0.4\%). The taxonomy's value lies in predicting failure mechanisms: type membership predicts the dominant mechanism 17$\times$ better than it predicts violation rate ($\text{NMI} = 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), enabling targeted diagnosis (\S\ref{sec:discussion}). Incompleteness is consistently the highest-risk type (46--62\% across all models); the remaining types form a partial ordering with robust extremes but margin-dependent mid-tier structure.
21:Our contributions are: (1)~the first matched-pair causal study of policy ambiguity's safety impact with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~a variance decomposition revealing that clause wording explains 22.4\% of violation variance versus 0.4\% for type, combined with a mutual information analysis showing that type predicts failure mechanism 17$\times$ better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool (\S\ref{sec:analysis}, \S\ref{sec:discussion}); and (3)~an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models (\S\ref{sec:analysis}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bedf927-c87f-405a-b670-c21ca115b532",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "825da036-6210-40b6-b54f-65684d0e4e10",
  "sourceToolAssistantUUID": "1bedf927-c87f-405a-b670-c21ca115b532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T23:26:46.708Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YPwLJxWLEWJ1LcqKUgR5B7`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== R18-N2: Judge confound ===\"\necho \"--- experiments.tex: Fig 3 caption for single-judge ---\"\ngrep -n \"single judge\\|single-judge\\|evaluated by a single\" \"$BASE/experiments.tex\" | head -20\n\necho \"--- experiments.tex: suggestive + single-judge-per-model ---\"\ngrep -n \"suggestive\\|single-judge-per-model\\|single judge per model\" \"$BASE/experiments.tex\" | head -20",
  "description": "Check R18-N2: Judge confound in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "825da036-6210-40b6-b54f-65684d0e4e10",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b4894f7-5d37-4148-b974-c2e2e5bdb3be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 7 · 2026-05-22T23:26:46.782Z_

<details><summary>↩ Tool result · `toolu_01YPwLJxWLEWJ1LcqKUgR5B7`</summary>

```text
=== R18-N2: Judge confound ===
--- experiments.tex: Fig 3 caption for single-judge ---
62:\caption{Violation rates (\%) by model and type under ambiguous conditions ($n = 2{,}997$). Authorization scope varies 52\,pp across models ($\kappa = 0.385$); incompleteness remains uniformly high (46--62\%). C4 interaction is authorization-scope-specific (excluding it: $p = 0.97$). Each model was evaluated by a single judge; C4 patterns should be interpreted cautiously.}
68:Figure~\ref{fig:heatmap} highlights three patterns: (1) authorization scope is the \emph{most model-differentiating type} (52\,pp range; Claude 12\% to GPT-5.4 64\%), though its low judge agreement ($\kappa = 0.385$) adds uncertainty; (2) incompleteness is a \emph{consistent vulnerability} (46--62\%); (3) conditional precedence is the most \emph{model-invariant} (34--40\%). The authorization scope ranking is stable within the GPT-5.4 judge subset (bootstrap preservation: 99.5\%), and the 34\,pp within-judge range far exceeds measurement noise; given the low cross-judge $\kappa$, we characterize this as suggestive given the single-judge-per-model design (\S\ref{sec:limitations}). Excluding authorization scope, the residual interaction vanishes ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}).
--- experiments.tex: suggestive + single-judge-per-model ---
68:Figure~\ref{fig:heatmap} highlights three patterns: (1) authorization scope is the \emph{most model-differentiating type} (52\,pp range; Claude 12\% to GPT-5.4 64\%), though its low judge agreement ($\kappa = 0.385$) adds uncertainty; (2) incompleteness is a \emph{consistent vulnerability} (46--62\%); (3) conditional precedence is the most \emph{model-invariant} (34--40\%). The authorization scope ranking is stable within the GPT-5.4 judge subset (bootstrap preservation: 99.5\%), and the 34\,pp within-judge range far exceeds measurement noise; given the low cross-judge $\kappa$, we characterize this as suggestive given the single-judge-per-model design (\S\ref{sec:limitations}). Excluding authorization scope, the residual interaction vanishes ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b4894f7-5d37-4148-b974-c2e2e5bdb3be",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "c993fc80-1468-4506-b1b0-6fdcfec95c10",
  "sourceToolAssistantUUID": "0b4894f7-5d37-4148-b974-c2e2e5bdb3be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T23:26:48.190Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01StxEinZTVf3fyjNpw87Jv2`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== R18-N3: Taxonomy demotion ===\"\necho \"--- related_work.tex: experimental instrument / controlled causal analysis ---\"\ngrep -n \"experimental instrument\\|controlled causal analysis\\|classification standard\\|proposed classification\" \"$BASE/related_work.tex\" | head -20\n\necho \"--- introduction.tex contribution (3): error analysis + failure mechanisms + convergent ---\"\ngrep -n \"error analysis\\|failure mechanisms\\|convergent\" \"$BASE/introduction.tex\" | head -20",
  "description": "Check R18-N3: Taxonomy demotion in related_work and introduction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c993fc80-1468-4506-b1b0-6fdcfec95c10",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c9d64e6-37bf-4f21-8565-4515ebd6411c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 9 · 2026-05-22T23:26:48.262Z_

<details><summary>↩ Tool result · `toolu_01StxEinZTVf3fyjNpw87Jv2`</summary>

```text
=== R18-N3: Taxonomy demotion ===
--- related_work.tex: experimental instrument / controlled causal analysis ---
5:Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
--- introduction.tex contribution (3): error analysis + failure mechanisms + convergent ---
6:LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
19:Our results show that policy ambiguity is consistently nocuous for LLM agents ($+34.0$ pp violation rate increase, conditional OR $= 15.1$), but risk is driven by individual clause wording (22.4\% of variance) rather than type membership (0.4\%). The taxonomy's value lies in predicting failure mechanisms: type membership predicts the dominant mechanism 17$\times$ better than it predicts violation rate ($\text{NMI} = 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), enabling targeted diagnosis (\S\ref{sec:discussion}). Incompleteness is consistently the highest-risk type (46--62\% across all models); the remaining types form a partial ordering with robust extremes but margin-dependent mid-tier structure.
21:Our contributions are: (1)~the first matched-pair causal study of policy ambiguity's safety impact with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~a variance decomposition revealing that clause wording explains 22.4\% of violation variance versus 0.4\% for type, combined with a mutual information analysis showing that type predicts failure mechanism 17$\times$ better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool (\S\ref{sec:analysis}, \S\ref{sec:discussion}); and (3)~an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models (\S\ref{sec:analysis}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c9d64e6-37bf-4f21-8565-4515ebd6411c",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "aafc12fc-4a8b-4982-9869-31e26d80edd3",
  "sourceToolAssistantUUID": "5c9d64e6-37bf-4f21-8565-4515ebd6411c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T23:26:50.514Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LfJMvnurYHatUBmdZx2uE4`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== R18-N4: DN demotion (lowercase with emph) ===\"\necho \"--- analysis.tex: disambiguation neglect ---\"\ngrep -n \"disambiguation neglect\\|Disambiguation Neglect\\|emph.*disambiguation\\|emph.*neglect\" \"$BASE/analysis.tex\" | head -20\n\necho \"--- discussion.tex: disambiguation neglect ---\"\ngrep -n \"disambiguation neglect\\|Disambiguation Neglect\\|emph.*disambiguation\\|emph.*neglect\" \"$BASE/discussion.tex\" | head -20\n\necho \"--- related_work.tex: disambiguation neglect ---\"\ngrep -n \"disambiguation neglect\\|Disambiguation Neglect\\|emph.*disambiguation\\|emph.*neglect\" \"$BASE/related_work.tex\" | head -20",
  "description": "Check R18-N4: DN demotion across files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aafc12fc-4a8b-4982-9869-31e26d80edd3",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b13803ff-0e32-4936-aef1-9c62673b416e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 11 · 2026-05-22T23:26:50.587Z_

<details><summary>↩ Tool result · `toolu_01LfJMvnurYHatUBmdZx2uE4`</summary>

```text
=== R18-N4: DN demotion (lowercase with emph) ===
--- analysis.tex: disambiguation neglect ---
20:\subsection{Disambiguation Neglect}
23:Agents rarely recognize ambiguity. We code \emph{disambiguation awareness} versus \emph{surface adoption} (proceeding with a single interpretation). Overall awareness is 4.6\% ($\leq$11\% per model); Qwen3 and DeepSeek show zero across all 278 combined traces.
25:We refer to this pattern as \emph{disambiguation neglect}---the absence of disambiguation in default settings, not inability. Prior work shows LLMs collapse ambiguity into single interpretations \citep{liu_ambiguity_2023,hu_ambiguity_2025}; we extend this to agentic contexts where the result is irreversible policy violation. Our mitigation experiment ($-$8.5\,pp; Appendix~\ref{app:mitigation}) confirms disambiguation can be elicited.
--- discussion.tex: disambiguation neglect ---
5:Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results support a \emph{differential nocuity} hypothesis \citep{willis_nocuous_2008}: risk depends on type, safety training, and disambiguation channel availability. The binary effect is domain-robust (interaction $p = 0.187$) but type rankings are not ($\rho = 0.26$), suggesting nocuity is universal while its type-specific profile requires per-domain calibration. Nevertheless, 60.8\% of variance remains unexplained (conversation trajectory, user-simulator stochasticity); clause-level auditing targets the largest controllable factor (22.4\%).
--- related_work.tex: disambiguation neglect ---
8:\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. At the pragmatic level, \citet{hu_pragmatic_2023} and \citet{ruis_goldilocks_2023} show that LLMs struggle with implicature resolution, defaulting to literal interpretations even when pragmatic inference is required. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output; \citet{gur_arieh_ambiguity_collapse_2026} taxonomize the epistemic risks of this ``ambiguity collapse''; \citet{sedova_to_know_2024} show analogous self-inconsistencies under entity-type ambiguity. These findings ground our \emph{disambiguation neglect} result: agents process ambiguous input without meta-cognitive awareness but, unlike humans, lack social channels to recover. \citet{disambiguation_cqa_survey_2025} survey disambiguation strategies in conversational QA; \citet{suri_structured_2025} show that structured uncertainty estimation improves coverage by 7--39\%, while \citet{sehwag_aspi_2026} demonstrate that clarification-seeking introduces prompt injection vulnerabilities---a tension for disambiguation channel design.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b13803ff-0e32-4936-aef1-9c62673b416e",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "f08eae18-8e3b-4198-99d2-ddf1edf94485",
  "sourceToolAssistantUUID": "b13803ff-0e32-4936-aef1-9c62673b416e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T23:26:52.471Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01P5vR6qT2A7NJWV86xYjcQ7`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== R18-W1: LPM footnote with Tjur ===\"\ngrep -n \"magnitudes differ\\|linear and logistic\\|Tjur\" \"$BASE/experiments.tex\" | head -20\n\necho \"=== R18-W3: Incompleteness upper-bound ===\"\ngrep -n \"upper bound\\|information addition\\|confound-controlled\\|18\\.7\\|18\\.7pp\" \"$BASE/experiments.tex\" | head -20",
  "description": "Check R18-W1 and R18-W3 in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f08eae18-8e3b-4198-99d2-ddf1edf94485",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc954e7a-2212-4a08-93bc-58f60694e658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 13 · 2026-05-22T23:26:52.527Z_

<details><summary>↩ Tool result · `toolu_01P5vR6qT2A7NJWV86xYjcQ7`</summary>

```text
=== R18-W1: LPM footnote with Tjur ===
8:Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (conversation trajectory, user-simulator stochasticity). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; the confound-controlled range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope; Appendix~\ref{app:confound}).
=== R18-W3: Incompleteness upper-bound ===
8:Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (conversation trajectory, user-simulator stochasticity). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; the confound-controlled range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope; Appendix~\ref{app:confound}).
16:\caption{Violation rates (\%) under ambiguous policy clauses by type and model (5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla.\ = Claude, Qw3 = Qwen3, DS = DeepSeek). $\Delta$pp: pooled difference (ambiguous $-$ unambiguous) with Newcombe 95\% CIs. Tier: TOST equivalence cluster at $\pm 15$\,pp---U = upper bound (separated at all margins), M = mid-tier (6/6 pairwise equivalent), L = lower (separates at $\pm 12$\,pp). All per-type $p < 10^{-5}$ (Fisher's exact).}
30: & Coreferential & 31.6 & 18 & 32 & 22 & 42 & 44 & +18.7\,[11.5, 25.7] & L & $<\!10^{-6}$ \\
37:The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$). TOST equivalence testing at a $\pm 15$ pp margin reveals a graded equivalence structure among five types---authorization scope (41.6\%), lexical (42.8\%), scopal (39.4\%), and conditional precedence (36.8\%) form a mid-tier cluster, with coreferential (31.6\%) below---while incompleteness (53.6\%) stands apart as an upper bound---conditional on the confound controls in Appendix~\ref{app:confound}---whose ranking partly reflects an information-addition confound. Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.
41:An important qualification: cross-judge-group type rankings are discordant ($\rho = 0.09$, $p = 0.87$; Appendix~\ref{app:judge_group_ranking}), driven by authorization scope ranking first in one judge group but last in the other. Excluding it, the remaining five types show strong concordance ($\rho = 0.90$, $p = 0.037$). C2 should be interpreted as establishing robust extremes---incompleteness as upper bound and coreferential as lower bound---rather than a complete linear ordering.
43:Incompleteness is highest in four of five models (rates $\geq$46\% in all seven; Appendix~\ref{app:model_expansion}). Its unambiguous variant adds policy content, so the 49.2\,pp effect is an upper bound; a confound analysis confirms significance after controlling for information delta (Appendix~\ref{app:confound}). Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%.
48:\caption{Per-type effect sizes ($\Delta$pp) with Newcombe 95\% CIs. Types form a partial ordering: incompleteness as upper bound (conditional on information-addition confound), coreferential as lower bound, and a mid-range equivalence cluster. Mid-tier ordering is margin-dependent (\S\ref{sec:results}).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc954e7a-2212-4a08-93bc-58f60694e658",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "2671ad8b-012c-4888-a28b-688556abc3de",
  "sourceToolAssistantUUID": "cc954e7a-2212-4a08-93bc-58f60694e658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T23:26:55.609Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014ZHwSvhGZwnx7hfcSMxd1W`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== R18-W5: SOPBench ===\"\ngrep -n \"SOPBench\\|3/5\\|3 of 5\\|three.*five.*significant\\|significant.*3\" \"$BASE/experiments.tex\" | head -20\n\necho \"=== R18-W7: Abstract numbers - should NOT contain 2,997 or 1.0% for model identity ===\"\ngrep -n \"2,997\\|1\\.0%.*model identity\\|model identity.*1\\.0%\" \"$BASE/abstract.tex\" | head -20\n\necho \"=== R18-W9: Conclusion domain-qualified ===\"\ngrep -n \"customer-service\\|customer service\\|policy-governed\\|policy governed\\|deployment\" \"$BASE/conclusion.tex\" | head -20",
  "description": "Check R18-W5, R18-W7, R18-W9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2671ad8b-012c-4888-a28b-688556abc3de",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ca4d2dc-27dc-4638-bfe4-eb12a2597115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 15 · 2026-05-22T23:26:55.679Z_

<details><summary>↩ Tool result · `toolu_014ZHwSvhGZwnx7hfcSMxd1W`</summary>

```text
=== R18-W5: SOPBench ===
8:Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (conversation trajectory, user-simulator stochasticity). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; the confound-controlled range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope; Appendix~\ref{app:confound}).
10:Replication on two additional model families confirms the effect across seven models ($\Delta = +20.0$ to $+33.6$\,pp; Appendix~\ref{app:model_expansion}); a cross-benchmark replication on SOPBench confirms directional consistency ($+13.8$\,pp pooled, 3/5 significant; Appendix~\ref{app:sopbench}). The taxonomy's primary value lies not in predicting clause risk but in predicting failure mechanisms: type predicts mechanism 17$\times$ more strongly than violation rate (\S\ref{sec:discussion}), making type-level analysis (C2--C4) informative for diagnosis.
66:A model main effect is significant ($\chi^2 = 31.02$, $p = 3.0 \times 10^{-6}$, $V = 0.102$), with Claude (30.3\%) substantially less vulnerable than DeepSeek (49.7\%). Model identity explains only 1.0\% of total violation variance; the significant interaction ($F(20, 2976) = 1.97$, $p = 0.006$; $\mathrm{df} = (5{-}1) \times (6{-}1) = 20$; 2.9\% of variance; confirmed by logistic regression likelihood ratio test: $\chi^2(20) = 47.20$, $p = 5.5 \times 10^{-4}$) concentrates in specific type--model combinations.
=== R18-W7: Abstract numbers - should NOT contain 2,997 or 1.0% for model identity ===
=== R18-W9: Conclusion domain-qualified ===
3:Policy ambiguity increases agent violations by 34.0\,pp (OR\,$=$\,15.1); clause wording explains 22.4\% of variance versus 0.4\% for type, while the taxonomy predicts failure mechanisms 17$\times$ better than violation rate. With $>$89\% disambiguation neglect and 41.3\% convergent violations, clause-level auditing is critical for customer-service and similar policy-governed deployments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ca4d2dc-27dc-4638-bfe4-eb12a2597115",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "58a22a91-1198-427d-9390-1cbc4389a1a8",
  "sourceToolAssistantUUID": "8ca4d2dc-27dc-4638-bfe4-eb12a2597115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T23:26:59.172Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YAXdvrkzpY3rjfanXN8ynn`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== R18-N1 deeper: abstract.tex full ===\"\ngrep -n \"C2\\|per-type\\|range\\|17\\|NMI\\|variance\\|ordering\" \"$BASE/abstract.tex\" | head -30\n\necho \"=== R18-N1: intro contribution 2 context ===\"\ngrep -n -A2 -B2 \"contribution\\|contrib\\|\\\\\\\\item\" \"$BASE/introduction.tex\" | grep -i \"NMI\\|variance\\|17\\|per-type\\|C2\\|decompos\" | head -20",
  "description": "Deeper check R18-N1 in abstract and introduction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58a22a91-1198-427d-9390-1cbc4389a1a8",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "439d8a18-1007-4c24-ac19-a164e0d7127f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 17 · 2026-05-22T23:26:59.236Z_

<details><summary>↩ Tool result · `toolu_01YAXdvrkzpY3rjfanXN8ynn`</summary>

```text
=== R18-N1 deeper: abstract.tex full ===
2:LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (i.e., harmful), increasing violation rates by 34.0 percentage points (conditional OR $= 15.1$, matched-pair), with perturbation controls confirming specificity to semantic ambiguity. A variance decomposition reveals that individual clause wording explains 22.4\% of violation variance versus 0.4\% for ambiguity type, establishing clause-level wording as the dominant risk factor. However, a normalized mutual information analysis shows that type membership predicts failure \emph{mechanism} 17$\times$ more strongly than it predicts violation rate, establishing the taxonomy as a diagnostic tool for failure-mechanism prediction rather than risk prediction. Per-type effects range from $+$18.7 to $+$49.2\,pp, with incompleteness as the consistent upper bound. Error analysis reveals disambiguation neglect ($\leq$11\% per-model awareness) and \emph{systematic nocuity}: 41.3\% of clauses triggering model-convergent violations. These results, observed in customer-service policy domains, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
=== R18-N1: intro contribution 2 context ===
19-Our results show that policy ambiguity is consistently nocuous for LLM agents ($+34.0$ pp violation rate increase, conditional OR $= 15.1$), but risk is driven by individual clause wording (22.4\% of variance) rather than type membership (0.4\%). The taxonomy's value lies in predicting failure mechanisms: type membership predicts the dominant mechanism 17$\times$ better than it predicts violation rate ($\text{NMI} = 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), enabling targeted diagnosis (\S\ref{sec:discussion}). Incompleteness is consistently the highest-risk type (46--62\% across all models); the remaining types form a partial ordering with robust extremes but margin-dependent mid-tier structure.
21:Our contributions are: (1)~the first matched-pair causal study of policy ambiguity's safety impact with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~a variance decomposition revealing that clause wording explains 22.4\% of violation variance versus 0.4\% for type, combined with a mutual information analysis showing that type predicts failure mechanism 17$\times$ better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool (\S\ref{sec:analysis}, \S\ref{sec:discussion}); and (3)~an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models (\S\ref{sec:analysis}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "439d8a18-1007-4c24-ac19-a164e0d7127f",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "7066892f-3efb-427f-8118-20f95e4c533d",
  "sourceToolAssistantUUID": "439d8a18-1007-4c24-ac19-a164e0d7127f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T23:27:00.962Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015hiEVsYJ9B7izxnq88Crgg`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== introduction.tex contributions section ===\"\n# Find contributions list in intro\ngrep -n \"\\\\\\\\item\\|contribution\\|17\\|NMI\\|variance decomp\\|per-type\\|error analysis\\|failure mechanism\\|convergent\" \"$BASE/introduction.tex\" | head -40",
  "description": "Check introduction.tex contributions list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7066892f-3efb-427f-8118-20f95e4c533d",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89ebb7ab-2e8c-4255-a1fb-2a56a6fc04a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 19 · 2026-05-22T23:27:01.036Z_

<details><summary>↩ Tool result · `toolu_015hiEVsYJ9B7izxnq88Crgg`</summary>

```text
=== introduction.tex contributions section ===
6:LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
19:Our results show that policy ambiguity is consistently nocuous for LLM agents ($+34.0$ pp violation rate increase, conditional OR $= 15.1$), but risk is driven by individual clause wording (22.4\% of variance) rather than type membership (0.4\%). The taxonomy's value lies in predicting failure mechanisms: type membership predicts the dominant mechanism 17$\times$ better than it predicts violation rate ($\text{NMI} = 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), enabling targeted diagnosis (\S\ref{sec:discussion}). Incompleteness is consistently the highest-risk type (46--62\% across all models); the remaining types form a partial ordering with robust extremes but margin-dependent mid-tier structure.
21:Our contributions are: (1)~the first matched-pair causal study of policy ambiguity's safety impact with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~a variance decomposition revealing that clause wording explains 22.4\% of violation variance versus 0.4\% for type, combined with a mutual information analysis showing that type predicts failure mechanism 17$\times$ better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool (\S\ref{sec:analysis}, \S\ref{sec:discussion}); and (3)~an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models (\S\ref{sec:analysis}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89ebb7ab-2e8c-4255-a1fb-2a56a6fc04a4",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "9351562b-c1f9-461d-98da-5ab1debc8fb0",
  "sourceToolAssistantUUID": "89ebb7ab-2e8c-4255-a1fb-2a56a6fc04a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T23:27:02.901Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0193qszi4BeK6WVP5oCAfpfz`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\n# Read the contributions section of introduction.tex\ngrep -n \"\" \"$BASE/introduction.tex\" | grep -A0 \"\\\\\\\\item\\|NMI\\|variance\\|17\\|error analysis\\|failure\\|convergent\\|taxonomy\\|instrument\" | head -50",
  "description": "Targeted search in introduction.tex for contribution items"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9351562b-c1f9-461d-98da-5ab1debc8fb0",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50967cb8-4222-4b55-96e1-43a5c159bfc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 21 · 2026-05-22T23:27:02.968Z_

<details><summary>↩ Tool result · `toolu_0193qszi4BeK6WVP5oCAfpfz`</summary>

```text
6:LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
--
8:LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
--
13:\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-layer ambiguity taxonomy and inject them into $\tau^2$-bench policy documents. Five models interact with the modified policies across 2,997 episodes. A cross-judge evaluation pipeline classifies violation severity on a four-tier scale.}
--
17:We address this gap with a matched-pair causal study on $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark. Using a six-type taxonomy organized into two layers---linguistic and specification, including specification-level gaps that produce equivalent behavioral effects in LLM agents (\S\ref{sec:taxonomy}), we construct 300 ambiguous/unambiguous clause pairs and evaluate five architecturally diverse models across 2,997 episodes.
--
19:Our results show that policy ambiguity is consistently nocuous for LLM agents ($+34.0$ pp violation rate increase, conditional OR $= 15.1$), but risk is driven by individual clause wording (22.4\% of variance) rather than type membership (0.4\%). The taxonomy's value lies in predicting failure mechanisms: type membership predicts the dominant mechanism 17$\times$ better than it predicts violation rate ($\text{NMI} = 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), enabling targeted diagnosis (\S\ref{sec:discussion}). Incompleteness is consistently the highest-risk type (46--62\% across all models); the remaining types form a partial ordering with robust extremes but margin-dependent mid-tier structure.
--
21:Our contributions are: (1)~the first matched-pair causal study of policy ambiguity's safety impact with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~a variance decomposition revealing that clause wording explains 22.4\% of violation variance versus 0.4\% for type, combined with a mutual information analysis showing that type predicts failure mechanism 17$\times$ better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool (\S\ref{sec:analysis}, \S\ref{sec:discussion}); and (3)~an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models (\S\ref{sec:analysis}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50967cb8-4222-4b55-96e1-43a5c159bfc7",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "68dd043f-775c-49de-8d50-b5298769dfc1",
  "sourceToolAssistantUUID": "50967cb8-4222-4b55-96e1-43a5c159bfc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T23:27:04.573Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012GgnC7CC4wPguYFzZHxq3M`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n# Read last part of introduction where contributions usually live\nwc -l \"$BASE/introduction.tex\"\ntail -80 \"$BASE/introduction.tex\"",
  "description": "Read end of introduction.tex for contributions list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68dd043f-775c-49de-8d50-b5298769dfc1",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29775292-64e1-463a-a711-99b646d61591",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 23 · 2026-05-22T23:27:04.628Z_

<details><summary>↩ Tool result · `toolu_012GgnC7CC4wPguYFzZHxq3M`</summary>

```text
21 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
\section{Introduction}
\label{sec:introduction}

A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.

LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.

LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.

\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-layer ambiguity taxonomy and inject them into $\tau^2$-bench policy documents. Five models interact with the modified policies across 2,997 episodes. A cross-judge evaluation pipeline classifies violation severity on a four-tier scale.}
\label{fig:overview}
\end{figure*}

We address this gap with a matched-pair causal study on $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark. Using a six-type taxonomy organized into two layers---linguistic and specification, including specification-level gaps that produce equivalent behavioral effects in LLM agents (\S\ref{sec:taxonomy}), we construct 300 ambiguous/unambiguous clause pairs and evaluate five architecturally diverse models across 2,997 episodes.

Our results show that policy ambiguity is consistently nocuous for LLM agents ($+34.0$ pp violation rate increase, conditional OR $= 15.1$), but risk is driven by individual clause wording (22.4\% of variance) rather than type membership (0.4\%). The taxonomy's value lies in predicting failure mechanisms: type membership predicts the dominant mechanism 17$\times$ better than it predicts violation rate ($\text{NMI} = 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), enabling targeted diagnosis (\S\ref{sec:discussion}). Incompleteness is consistently the highest-risk type (46--62\% across all models); the remaining types form a partial ordering with robust extremes but margin-dependent mid-tier structure.

Our contributions are: (1)~the first matched-pair causal study of policy ambiguity's safety impact with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~a variance decomposition revealing that clause wording explains 22.4\% of violation variance versus 0.4\% for type, combined with a mutual information analysis showing that type predicts failure mechanism 17$\times$ better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool (\S\ref{sec:analysis}, \S\ref{sec:discussion}); and (3)~an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models (\S\ref{sec:analysis}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29775292-64e1-463a-a711-99b646d61591",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "e5107a79-07ad-4082-a9fd-b6bae6de888a",
  "sourceToolAssistantUUID": "29775292-64e1-463a-a711-99b646d61591",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T23:27:05.558Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EyoKPi81SkWpnsv4rr4SVR`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n# Read full introduction\ncat -n \"$BASE/introduction.tex\" | tail -120",
  "description": "Read last 120 lines of introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5107a79-07ad-4082-a9fd-b6bae6de888a",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcf14842-13aa-47b4-aaf6-87e4bf6318ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 25 · 2026-05-22T23:27:05.609Z_

<details><summary>↩ Tool result · `toolu_01EyoKPi81SkWpnsv4rr4SVR`</summary>

```text
     1	\section{Introduction}
     2	\label{sec:introduction}
     3	
     4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
     5	
     6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
     7	
     8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
     9	
    10	\begin{figure*}[t]
    11	\centering
    12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
    13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-layer ambiguity taxonomy and inject them into $\tau^2$-bench policy documents. Five models interact with the modified policies across 2,997 episodes. A cross-judge evaluation pipeline classifies violation severity on a four-tier scale.}
    14	\label{fig:overview}
    15	\end{figure*}
    16	
    17	We address this gap with a matched-pair causal study on $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark. Using a six-type taxonomy organized into two layers---linguistic and specification, including specification-level gaps that produce equivalent behavioral effects in LLM agents (\S\ref{sec:taxonomy}), we construct 300 ambiguous/unambiguous clause pairs and evaluate five architecturally diverse models across 2,997 episodes.
    18	
    19	Our results show that policy ambiguity is consistently nocuous for LLM agents ($+34.0$ pp violation rate increase, conditional OR $= 15.1$), but risk is driven by individual clause wording (22.4\% of variance) rather than type membership (0.4\%). The taxonomy's value lies in predicting failure mechanisms: type membership predicts the dominant mechanism 17$\times$ better than it predicts violation rate ($\text{NMI} = 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), enabling targeted diagnosis (\S\ref{sec:discussion}). Incompleteness is consistently the highest-risk type (46--62\% across all models); the remaining types form a partial ordering with robust extremes but margin-dependent mid-tier structure.
    20	
    21	Our contributions are: (1)~the first matched-pair causal study of policy ambiguity's safety impact with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~a variance decomposition revealing that clause wording explains 22.4\% of violation variance versus 0.4\% for type, combined with a mutual information analysis showing that type predicts failure mechanism 17$\times$ better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool (\S\ref{sec:analysis}, \S\ref{sec:discussion}); and (3)~an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models (\S\ref{sec:analysis}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcf14842-13aa-47b4-aaf6-87e4bf6318ad",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "f1ccd3b0-2bdb-45e3-b8fc-1d72c7c8d2ed",
  "sourceToolAssistantUUID": "dcf14842-13aa-47b4-aaf6-87e4bf6318ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T23:27:06.685Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Re24epDWUUkGuERZf2Ma43`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex",
  "offset": 80,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1ccd3b0-2bdb-45e3-b8fc-1d72c7c8d2ed",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e3572f9-7f28-418b-b366-f6679f9d5bf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 27 · 2026-05-22T23:27:06.693Z_

<details><summary>↩ Tool result · `toolu_01Re24epDWUUkGuERZf2Ma43`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (80). The file has 22 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e3572f9-7f28-418b-b366-f6679f9d5bf7",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "f3879172-8351-435b-8ec8-db34dc3efcf0",
  "sourceToolAssistantUUID": "7e3572f9-7f28-418b-b366-f6679f9d5bf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T23:27:08.020Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018uJsxj18WfDzQw32VjhWgK`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\nwc -l \"$BASE/introduction.tex\" \"$BASE/abstract.tex\" \"$BASE/experiments.tex\" \"$BASE/analysis.tex\" \"$BASE/discussion.tex\" \"$BASE/related_work.tex\" \"$BASE/conclusion.tex\"",
  "description": "Check line counts for all relevant files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3879172-8351-435b-8ec8-db34dc3efcf0",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd856fca-b055-4085-93d3-80a19e7bd405",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 29 · 2026-05-22T23:27:08.075Z_

<details><summary>↩ Tool result · `toolu_018uJsxj18WfDzQw32VjhWgK`</summary>

```text
   21 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
    3 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
   69 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
   29 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
   11 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex
   13 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
    3 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
  149 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd856fca-b055-4085-93d3-80a19e7bd405",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "78cdaf11-d7c2-4783-b476-9ac18c1e49a8",
  "sourceToolAssistantUUID": "fd856fca-b055-4085-93d3-80a19e7bd405",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T23:27:09.045Z_

<details open><summary>🔧 Tool call — Read · `toolu_013YjiUe6LjFGyMwCrFh5Wy9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex",
  "offset": 150,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78cdaf11-d7c2-4783-b476-9ac18c1e49a8",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83432d1d-49f9-401a-ba9b-195f51e7bd03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 31 · 2026-05-22T23:27:09.051Z_

<details><summary>↩ Tool result · `toolu_013YjiUe6LjFGyMwCrFh5Wy9`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (150). The file has 22 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83432d1d-49f9-401a-ba9b-195f51e7bd03",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "4164dc12-aee6-470e-8e33-4fff486789b2",
  "sourceToolAssistantUUID": "83432d1d-49f9-401a-ba9b-195f51e7bd03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T23:27:09.445Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BMnAz8tKa2nnfLu2thkYwU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4164dc12-aee6-470e-8e33-4fff486789b2",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3bb4dd4-21f5-4297-8673-684c258ec1cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 33 · 2026-05-22T23:27:09.455Z_

<details><summary>↩ Tool result · `toolu_01BMnAz8tKa2nnfLu2thkYwU`</summary>

```text
1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (i.e., harmful), increasing violation rates by 34.0 percentage points (conditional OR $= 15.1$, matched-pair), with perturbation controls confirming specificity to semantic ambiguity. A variance decomposition reveals that individual clause wording explains 22.4\% of violation variance versus 0.4\% for ambiguity type, establishing clause-level wording as the dominant risk factor. However, a normalized mutual information analysis shows that type membership predicts failure \emph{mechanism} 17$\times$ more strongly than it predicts violation rate, establishing the taxonomy as a diagnostic tool for failure-mechanism prediction rather than risk prediction. Per-type effects range from $+$18.7 to $+$49.2\,pp, with incompleteness as the consistent upper bound. Error analysis reveals disambiguation neglect ($\leq$11\% per-model awareness) and \emph{systematic nocuity}: 41.3\% of clauses triggering model-convergent violations. These results, observed in customer-service policy domains, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3bb4dd4-21f5-4297-8673-684c258ec1cc",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "51a180e4-0684-412a-870a-e07fbb3b2f80",
  "sourceToolAssistantUUID": "f3bb4dd4-21f5-4297-8673-684c258ec1cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-22T23:27:11.336Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mf5vGCoZRwW4gBpnLGYXAJ`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\necho \"=== R18-N2: Fig 3 caption context in experiments.tex ===\"\ngrep -n -B5 -A5 \"Fig.*3\\|figure.*3\\|caption.*3\\|includegraphics\\|single.*judge\\|suggestive\" \"$BASE/experiments.tex\" | head -60",
  "description": "Get context around Fig 3 and judge confound in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51a180e4-0684-412a-870a-e07fbb3b2f80",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "832b61cc-360f-4e0b-a93c-c802d8071304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 35 · 2026-05-22T23:27:11.394Z_

<details><summary>↩ Tool result · `toolu_01Mf5vGCoZRwW4gBpnLGYXAJ`</summary>

```text
=== R18-N2: Fig 3 caption context in experiments.tex ===
11-
12-\subsection{Type Partial Ordering (C2)}
13-
14-\begin{table*}[t]
15-\centering
16:\caption{Violation rates (\%) under ambiguous policy clauses by type and model (5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla.\ = Claude, Qw3 = Qwen3, DS = DeepSeek). $\Delta$pp: pooled difference (ambiguous $-$ unambiguous) with Newcombe 95\% CIs. Tier: TOST equivalence cluster at $\pm 15$\,pp---U = upper bound (separated at all margins), M = mid-tier (6/6 pairwise equivalent), L = lower (separates at $\pm 12$\,pp). All per-type $p < 10^{-5}$ (Fisher's exact).}
17-\label{tab:main_results}
18-\footnotesize
19-\setlength{\tabcolsep}{3.8pt}
20-\begin{tabular}{llrrrrrrr@{\hskip 6pt}cr}
21-\toprule
--
42-
43-Incompleteness is highest in four of five models (rates $\geq$46\% in all seven; Appendix~\ref{app:model_expansion}). Its unambiguous variant adds policy content, so the 49.2\,pp effect is an upper bound; a confound analysis confirms significance after controlling for information delta (Appendix~\ref{app:confound}). Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%.
44-
45-\begin{figure}[t]
46-\centering
47:\includegraphics[width=\columnwidth]{figures/fig2_forest_plot.pdf}
48-\caption{Per-type effect sizes ($\Delta$pp) with Newcombe 95\% CIs. Types form a partial ordering: incompleteness as upper bound (conditional on information-addition confound), coreferential as lower bound, and a mid-range equivalence cluster. Mid-tier ordering is margin-dependent (\S\ref{sec:results}).}
49-\label{fig:forest_plot}
50-\end{figure}
51-
52-\subsection{Layer Effect (C3)}
--
56-\subsection{Model $\times$ Type Interaction (C4) \emph{[Exploratory]}}
57-\label{sec:c4}
58-
59-\begin{figure}[t]
60-\centering
61:\includegraphics[width=\columnwidth]{figures/fig3_heatmap.pdf}
62:\caption{Violation rates (\%) by model and type under ambiguous conditions ($n = 2{,}997$). Authorization scope varies 52\,pp across models ($\kappa = 0.385$); incompleteness remains uniformly high (46--62\%). C4 interaction is authorization-scope-specific (excluding it: $p = 0.97$). Each model was evaluated by a single judge; C4 patterns should be interpreted cautiously.}
63-\label{fig:heatmap}
64-\end{figure}
65-
66-A model main effect is significant ($\chi^2 = 31.02$, $p = 3.0 \times 10^{-6}$, $V = 0.102$), with Claude (30.3\%) substantially less vulnerable than DeepSeek (49.7\%). Model identity explains only 1.0\% of total violation variance; the significant interaction ($F(20, 2976) = 1.97$, $p = 0.006$; $\mathrm{df} = (5{-}1) \times (6{-}1) = 20$; 2.9\% of variance; confirmed by logistic regression likelihood ratio test: $\chi^2(20) = 47.20$, $p = 5.5 \times 10^{-4}$) concentrates in specific type--model combinations.
67-
68:Figure~\ref{fig:heatmap} highlights three patterns: (1) authorization scope is the \emph{most model-differentiating type} (52\,pp range; Claude 12\% to GPT-5.4 64\%), though its low judge agreement ($\kappa = 0.385$) adds uncertainty; (2) incompleteness is a \emph{consistent vulnerability} (46--62\%); (3) conditional precedence is the most \emph{model-invariant} (34--40\%). The authorization scope ranking is stable within the GPT-5.4 judge subset (bootstrap preservation: 99.5\%), and the 34\,pp within-judge range far exceeds measurement noise; given the low cross-judge $\kappa$, we characterize this as suggestive given the single-judge-per-model design (\S\ref{sec:limitations}). Excluding authorization scope, the residual interaction vanishes ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}).
69-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "832b61cc-360f-4e0b-a93c-c802d8071304",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "a9f1e530-6330-463d-9ce2-3091b4d8e455",
  "sourceToolAssistantUUID": "832b61cc-360f-4e0b-a93c-c802d8071304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T23:27:12.911Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019xQyTT4MKh7R3gau2PW58V`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\necho \"=== Check all caption blocks in experiments.tex ===\"\ngrep -n \"\\\\\\\\caption\\|single.*judge\\|suggestive\\|confound\" \"$BASE/experiments.tex\" | head -40",
  "description": "Search captions and key terms in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9f1e530-6330-463d-9ce2-3091b4d8e455",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ae45888-c195-4e1a-b519-0bd7429d39b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 37 · 2026-05-22T23:27:12.964Z_

<details><summary>↩ Tool result · `toolu_019xQyTT4MKh7R3gau2PW58V`</summary>

```text
=== Check all caption blocks in experiments.tex ===
8:Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (conversation trajectory, user-simulator stochasticity). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; the confound-controlled range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope; Appendix~\ref{app:confound}).
16:\caption{Violation rates (\%) under ambiguous policy clauses by type and model (5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla.\ = Claude, Qw3 = Qwen3, DS = DeepSeek). $\Delta$pp: pooled difference (ambiguous $-$ unambiguous) with Newcombe 95\% CIs. Tier: TOST equivalence cluster at $\pm 15$\,pp---U = upper bound (separated at all margins), M = mid-tier (6/6 pairwise equivalent), L = lower (separates at $\pm 12$\,pp). All per-type $p < 10^{-5}$ (Fisher's exact).}
37:The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$). TOST equivalence testing at a $\pm 15$ pp margin reveals a graded equivalence structure among five types---authorization scope (41.6\%), lexical (42.8\%), scopal (39.4\%), and conditional precedence (36.8\%) form a mid-tier cluster, with coreferential (31.6\%) below---while incompleteness (53.6\%) stands apart as an upper bound---conditional on the confound controls in Appendix~\ref{app:confound}---whose ranking partly reflects an information-addition confound. Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.
43:Incompleteness is highest in four of five models (rates $\geq$46\% in all seven; Appendix~\ref{app:model_expansion}). Its unambiguous variant adds policy content, so the 49.2\,pp effect is an upper bound; a confound analysis confirms significance after controlling for information delta (Appendix~\ref{app:confound}). Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%.
48:\caption{Per-type effect sizes ($\Delta$pp) with Newcombe 95\% CIs. Types form a partial ordering: incompleteness as upper bound (conditional on information-addition confound), coreferential as lower bound, and a mid-range equivalence cluster. Mid-tier ordering is margin-dependent (\S\ref{sec:results}).}
62:\caption{Violation rates (\%) by model and type under ambiguous conditions ($n = 2{,}997$). Authorization scope varies 52\,pp across models ($\kappa = 0.385$); incompleteness remains uniformly high (46--62\%). C4 interaction is authorization-scope-specific (excluding it: $p = 0.97$). Each model was evaluated by a single judge; C4 patterns should be interpreted cautiously.}
68:Figure~\ref{fig:heatmap} highlights three patterns: (1) authorization scope is the \emph{most model-differentiating type} (52\,pp range; Claude 12\% to GPT-5.4 64\%), though its low judge agreement ($\kappa = 0.385$) adds uncertainty; (2) incompleteness is a \emph{consistent vulnerability} (46--62\%); (3) conditional precedence is the most \emph{model-invariant} (34--40\%). The authorization scope ranking is stable within the GPT-5.4 judge subset (bootstrap preservation: 99.5\%), and the 34\,pp within-judge range far exceeds measurement noise; given the low cross-judge $\kappa$, we characterize this as suggestive given the single-judge-per-model design (\S\ref{sec:limitations}). Excluding authorization scope, the residual interaction vanishes ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ae45888-c195-4e1a-b519-0bd7429d39b9",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "302d21d5-e5f1-44b0-981b-8f33c73e6e27",
  "sourceToolAssistantUUID": "0ae45888-c195-4e1a-b519-0bd7429d39b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T23:27:14.843Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JDeKd8fQeFi4zHainyP3Mc`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n# Search for 5.4 section\ngrep -n \"5\\.4\\|subsection.*judge\\|subsection.*model\\|single.*judge\\|per.*model\" \"$BASE/experiments.tex\" | head -30",
  "description": "Search for section 5.4 and judge-related text in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "302d21d5-e5f1-44b0-981b-8f33c73e6e27",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91c993d9-927a-4cad-973d-b3693dccea17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 39 · 2026-05-22T23:27:14.894Z_

<details><summary>↩ Tool result · `toolu_01JDeKd8fQeFi4zHainyP3Mc`</summary>

```text
8:Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (conversation trajectory, user-simulator stochasticity). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; the confound-controlled range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope; Appendix~\ref{app:confound}).
16:\caption{Violation rates (\%) under ambiguous policy clauses by type and model (5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla.\ = Claude, Qw3 = Qwen3, DS = DeepSeek). $\Delta$pp: pooled difference (ambiguous $-$ unambiguous) with Newcombe 95\% CIs. Tier: TOST equivalence cluster at $\pm 15$\,pp---U = upper bound (separated at all margins), M = mid-tier (6/6 pairwise equivalent), L = lower (separates at $\pm 12$\,pp). All per-type $p < 10^{-5}$ (Fisher's exact).}
22:Layer & Type & Pooled & 5.4 & 4.1 & Cla. & Qw3 & DS & $\Delta$pp\,[95\% CI] & Tier & $p$ \\
39:Sensitivity analysis across seven margins ($\pm 5$--$20$ pp; Appendix~\ref{app:tost}) confirms this structure is margin-dependent: mid-tier cohesion emerges at $\pm 12$ pp and stabilizes at $\pm 15$ pp, while the incompleteness upper-bound is robust across all margins. A bootstrap cluster analysis ($B = 10{,}000$; Appendix~\ref{app:cluster}) corroborates: incompleteness forms a singleton at $k = 2$, coreferential additionally separates at $k = 3$. Cross-model type ranking concordance is moderate ($W = 0.398$, $p = 0.072$; Appendix~\ref{app:kendall_w}), driven by incompleteness ranking highest in four of five models.
62:\caption{Violation rates (\%) by model and type under ambiguous conditions ($n = 2{,}997$). Authorization scope varies 52\,pp across models ($\kappa = 0.385$); incompleteness remains uniformly high (46--62\%). C4 interaction is authorization-scope-specific (excluding it: $p = 0.97$). Each model was evaluated by a single judge; C4 patterns should be interpreted cautiously.}
68:Figure~\ref{fig:heatmap} highlights three patterns: (1) authorization scope is the \emph{most model-differentiating type} (52\,pp range; Claude 12\% to GPT-5.4 64\%), though its low judge agreement ($\kappa = 0.385$) adds uncertainty; (2) incompleteness is a \emph{consistent vulnerability} (46--62\%); (3) conditional precedence is the most \emph{model-invariant} (34--40\%). The authorization scope ranking is stable within the GPT-5.4 judge subset (bootstrap preservation: 99.5\%), and the 34\,pp within-judge range far exceeds measurement noise; given the low cross-judge $\kappa$, we characterize this as suggestive given the single-judge-per-model design (\S\ref{sec:limitations}). Excluding authorization scope, the residual interaction vanishes ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91c993d9-927a-4cad-973d-b3693dccea17",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "d601601e-71e7-4013-9f2b-35013c848221",
  "sourceToolAssistantUUID": "91c993d9-927a-4cad-973d-b3693dccea17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-22T23:27:15.704Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X857VEiqtCb9AJ2y7yCitB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 1,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d601601e-71e7-4013-9f2b-35013c848221",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "feeb3acc-48cf-4aea-89fe-11094056747b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 41 · 2026-05-22T23:27:15.711Z_

<details><summary>↩ Tool result · `toolu_01X857VEiqtCb9AJ2y7yCitB`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type partial ordering (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (conversation trajectory, user-simulator stochasticity). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; the confound-controlled range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope; Appendix~\ref{app:confound}).
9	
10	Replication on two additional model families confirms the effect across seven models ($\Delta = +20.0$ to $+33.6$\,pp; Appendix~\ref{app:model_expansion}); a cross-benchmark replication on SOPBench confirms directional consistency ($+13.8$\,pp pooled, 3/5 significant; Appendix~\ref{app:sopbench}). The taxonomy's primary value lies not in predicting clause risk but in predicting failure mechanisms: type predicts mechanism 17$\times$ more strongly than violation rate (\S\ref{sec:discussion}), making type-level analysis (C2--C4) informative for diagnosis.
11	
12	\subsection{Type Partial Ordering (C2)}
13	
14	\begin{table*}[t]
15	\centering
16	\caption{Violation rates (\%) under ambiguous policy clauses by type and model (5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla.\ = Claude, Qw3 = Qwen3, DS = DeepSeek). $\Delta$pp: pooled difference (ambiguous $-$ unambiguous) with Newcombe 95\% CIs. Tier: TOST equivalence cluster at $\pm 15$\,pp---U = upper bound (separated at all margins), M = mid-tier (6/6 pairwise equivalent), L = lower (separates at $\pm 12$\,pp). All per-type $p < 10^{-5}$ (Fisher's exact).}
17	\label{tab:main_results}
18	\footnotesize
19	\setlength{\tabcolsep}{3.8pt}
20	\begin{tabular}{llrrrrrrr@{\hskip 6pt}cr}
21	\toprule
22	Layer & Type & Pooled & 5.4 & 4.1 & Cla. & Qw3 & DS & $\Delta$pp\,[95\% CI] & Tier & $p$ \\
23	\midrule
24	\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46 & 58 & 48 & 62 & 54 & +49.2\,[42.2, 55.6] & U & $<\!10^{-37}$ \\
25	 & Auth.\ Scope & 41.6 & 64 & 46 & 12 & 26 & 60 & +36.0\,[29.1, 42.6] & M & $<\!10^{-22}$ \\
26	 & Cond.\ Prec. & 36.8 & 34 & 36 & 36 & 40 & 38 & +30.8\,[24.0, 37.4] & M & $<\!10^{-17}$ \\
27	\midrule
28	\multirow{3}{*}{\textcolor{lingcolor}{Ling.}} & Lexical & 42.8 & 42 & 34 & 32 & 52 & 54 & +35.2\,[28.0, 42.0] & M & $<\!10^{-20}$ \\
29	 & Scopal & 39.4 & 42 & 38 & 32 & 37 & 48 & +34.2\,[27.4, 40.7] & M & $<\!10^{-21}$ \\
30	 & Coreferential & 31.6 & 18 & 32 & 22 & 42 & 44 & +18.7\,[11.5, 25.7] & L & $<\!10^{-6}$ \\
31	\midrule
32	\multicolumn{2}{l}{\textbf{Overall}} & \textbf{41.0} & 41 & 41 & 30 & 43 & 50 & \textbf{+34.0}\,[31.3, 36.9] & --- & $<\!10^{-105}$ \\
33	\bottomrule
34	\end{tabular}
35	\end{table*}
36	
37	The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$). TOST equivalence testing at a $\pm 15$ pp margin reveals a graded equivalence structure among five types---authorization scope (41.6\%), lexical (42.8\%), scopal (39.4\%), and conditional precedence (36.8\%) form a mid-tier cluster, with coreferential (31.6\%) below---while incompleteness (53.6\%) stands apart as an upper bound---conditional on the confound controls in Appendix~\ref{app:confound}---whose ranking partly reflects an information-addition confound. Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.
38	
39	Sensitivity analysis across seven margins ($\pm 5$--$20$ pp; Appendix~\ref{app:tost}) confirms this structure is margin-dependent: mid-tier cohesion emerges at $\pm 12$ pp and stabilizes at $\pm 15$ pp, while the incompleteness upper-bound is robust across all margins. A bootstrap cluster analysis ($B = 10{,}000$; Appendix~\ref{app:cluster}) corroborates: incompleteness forms a singleton at $k = 2$, coreferential additionally separates at $k = 3$. Cross-model type ranking concordance is moderate ($W = 0.398$, $p = 0.072$; Appendix~\ref{app:kendall_w}), driven by incompleteness ranking highest in four of five models.
40	
41	An important qualification: cross-judge-group type rankings are discordant ($\rho = 0.09$, $p = 0.87$; Appendix~\ref{app:judge_group_ranking}), driven by authorization scope ranking first in one judge group but last in the other. Excluding it, the remaining five types show strong concordance ($\rho = 0.90$, $p = 0.037$). C2 should be interpreted as establishing robust extremes---incompleteness as upper bound and coreferential as lower bound---rather than a complete linear ordering.
42	
43	Incompleteness is highest in four of five models (rates $\geq$46\% in all seven; Appendix~\ref{app:model_expansion}). Its unambiguous variant adds policy content, so the 49.2\,pp effect is an upper bound; a confound analysis confirms significance after controlling for information delta (Appendix~\ref{app:confound}). Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%.
44	
45	\begin{figure}[t]
46	\centering
47	\includegraphics[width=\columnwidth]{figures/fig2_forest_plot.pdf}
48	\caption{Per-type effect sizes ($\Delta$pp) with Newcombe 95\% CIs. Types form a partial ordering: incompleteness as upper bound (conditional on information-addition confound), coreferential as lower bound, and a mid-range equivalence cluster. Mid-tier ordering is margin-dependent (\S\ref{sec:results}).}
49	\label{fig:forest_plot}
50	\end{figure}
51	
52	\subsection{Layer Effect (C3)}
53	
54	Specification-layer types trend higher than linguistic-layer types (44.0\% vs.\ 37.9\%, $p = 0.017$), but C3 is inconclusive: the effect does not survive Holm--Bonferroni correction and controlling for token delta reverses the direction. We treat the two-layer structure as organizational convenience rather than a theoretical claim.
55	
56	\subsection{Model $\times$ Type Interaction (C4) \emph{[Exploratory]}}
57	\label{sec:c4}
58	
59	\begin{figure}[t]
60	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feeb3acc-48cf-4aea-89fe-11094056747b",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "de6bea96-a6b9-49cf-b2a6-124b6222f595",
  "sourceToolAssistantUUID": "feeb3acc-48cf-4aea-89fe-11094056747b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-22T23:27:17.356Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012qjhD9bWB9evSmQsoG8nMs`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n# Search more broadly in experiments.tex\ngrep -n \"judge\\|Judge\\|model identity\\|confound\\|single\\|cross.*judge\\|rho\\|correlation\" \"$BASE/experiments.tex\" | head -40",
  "description": "Broad search for judge-related content in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de6bea96-a6b9-49cf-b2a6-124b6222f595",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ab2d540-a615-45f9-bf02-32fe0618f0cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 43 · 2026-05-22T23:27:17.414Z_

<details><summary>↩ Tool result · `toolu_012qjhD9bWB9evSmQsoG8nMs`</summary>

```text
8:Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (conversation trajectory, user-simulator stochasticity). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; the confound-controlled range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope; Appendix~\ref{app:confound}).
37:The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$). TOST equivalence testing at a $\pm 15$ pp margin reveals a graded equivalence structure among five types---authorization scope (41.6\%), lexical (42.8\%), scopal (39.4\%), and conditional precedence (36.8\%) form a mid-tier cluster, with coreferential (31.6\%) below---while incompleteness (53.6\%) stands apart as an upper bound---conditional on the confound controls in Appendix~\ref{app:confound}---whose ranking partly reflects an information-addition confound. Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.
39:Sensitivity analysis across seven margins ($\pm 5$--$20$ pp; Appendix~\ref{app:tost}) confirms this structure is margin-dependent: mid-tier cohesion emerges at $\pm 12$ pp and stabilizes at $\pm 15$ pp, while the incompleteness upper-bound is robust across all margins. A bootstrap cluster analysis ($B = 10{,}000$; Appendix~\ref{app:cluster}) corroborates: incompleteness forms a singleton at $k = 2$, coreferential additionally separates at $k = 3$. Cross-model type ranking concordance is moderate ($W = 0.398$, $p = 0.072$; Appendix~\ref{app:kendall_w}), driven by incompleteness ranking highest in four of five models.
41:An important qualification: cross-judge-group type rankings are discordant ($\rho = 0.09$, $p = 0.87$; Appendix~\ref{app:judge_group_ranking}), driven by authorization scope ranking first in one judge group but last in the other. Excluding it, the remaining five types show strong concordance ($\rho = 0.90$, $p = 0.037$). C2 should be interpreted as establishing robust extremes---incompleteness as upper bound and coreferential as lower bound---rather than a complete linear ordering.
43:Incompleteness is highest in four of five models (rates $\geq$46\% in all seven; Appendix~\ref{app:model_expansion}). Its unambiguous variant adds policy content, so the 49.2\,pp effect is an upper bound; a confound analysis confirms significance after controlling for information delta (Appendix~\ref{app:confound}). Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%.
48:\caption{Per-type effect sizes ($\Delta$pp) with Newcombe 95\% CIs. Types form a partial ordering: incompleteness as upper bound (conditional on information-addition confound), coreferential as lower bound, and a mid-range equivalence cluster. Mid-tier ordering is margin-dependent (\S\ref{sec:results}).}
62:\caption{Violation rates (\%) by model and type under ambiguous conditions ($n = 2{,}997$). Authorization scope varies 52\,pp across models ($\kappa = 0.385$); incompleteness remains uniformly high (46--62\%). C4 interaction is authorization-scope-specific (excluding it: $p = 0.97$). Each model was evaluated by a single judge; C4 patterns should be interpreted cautiously.}
68:Figure~\ref{fig:heatmap} highlights three patterns: (1) authorization scope is the \emph{most model-differentiating type} (52\,pp range; Claude 12\% to GPT-5.4 64\%), though its low judge agreement ($\kappa = 0.385$) adds uncertainty; (2) incompleteness is a \emph{consistent vulnerability} (46--62\%); (3) conditional precedence is the most \emph{model-invariant} (34--40\%). The authorization scope ranking is stable within the GPT-5.4 judge subset (bootstrap preservation: 99.5\%), and the 34\,pp within-judge range far exceeds measurement noise; given the low cross-judge $\kappa$, we characterize this as suggestive given the single-judge-per-model design (\S\ref{sec:limitations}). Excluding authorization scope, the residual interaction vanishes ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ab2d540-a615-45f9-bf02-32fe0618f0cc",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "e34cc186-24f0-4b92-bae6-5a92603c4ee6",
  "sourceToolAssistantUUID": "5ab2d540-a615-45f9-bf02-32fe0618f0cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-22T23:27:18.004Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DntSVPfajEqmBygCXH7n28`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 60,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e34cc186-24f0-4b92-bae6-5a92603c4ee6",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "597e5b72-7e19-4c9e-b8f4-f38a20f5f5d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 45 · 2026-05-22T23:27:18.015Z_

<details><summary>↩ Tool result · `toolu_01DntSVPfajEqmBygCXH7n28`</summary>

```text
60	\centering
61	\includegraphics[width=\columnwidth]{figures/fig3_heatmap.pdf}
62	\caption{Violation rates (\%) by model and type under ambiguous conditions ($n = 2{,}997$). Authorization scope varies 52\,pp across models ($\kappa = 0.385$); incompleteness remains uniformly high (46--62\%). C4 interaction is authorization-scope-specific (excluding it: $p = 0.97$). Each model was evaluated by a single judge; C4 patterns should be interpreted cautiously.}
63	\label{fig:heatmap}
64	\end{figure}
65	
66	A model main effect is significant ($\chi^2 = 31.02$, $p = 3.0 \times 10^{-6}$, $V = 0.102$), with Claude (30.3\%) substantially less vulnerable than DeepSeek (49.7\%). Model identity explains only 1.0\% of total violation variance; the significant interaction ($F(20, 2976) = 1.97$, $p = 0.006$; $\mathrm{df} = (5{-}1) \times (6{-}1) = 20$; 2.9\% of variance; confirmed by logistic regression likelihood ratio test: $\chi^2(20) = 47.20$, $p = 5.5 \times 10^{-4}$) concentrates in specific type--model combinations.
67	
68	Figure~\ref{fig:heatmap} highlights three patterns: (1) authorization scope is the \emph{most model-differentiating type} (52\,pp range; Claude 12\% to GPT-5.4 64\%), though its low judge agreement ($\kappa = 0.385$) adds uncertainty; (2) incompleteness is a \emph{consistent vulnerability} (46--62\%); (3) conditional precedence is the most \emph{model-invariant} (34--40\%). The authorization scope ranking is stable within the GPT-5.4 judge subset (bootstrap preservation: 99.5\%), and the 34\,pp within-judge range far exceeds measurement noise; given the low cross-judge $\kappa$, we characterize this as suggestive given the single-judge-per-model design (\S\ref{sec:limitations}). Excluding authorization scope, the residual interaction vanishes ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}).
69	
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "597e5b72-7e19-4c9e-b8f4-f38a20f5f5d3",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "eb8c5c50-2593-4095-b3fa-a72e23c86e6b",
  "sourceToolAssistantUUID": "597e5b72-7e19-4c9e-b8f4-f38a20f5f5d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-22T23:27:19.134Z_

<details open><summary>🔧 Tool call — Read · `toolu_019Zj3MfxzTty1Jjwc57h7Yu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 140,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb8c5c50-2593-4095-b3fa-a72e23c86e6b",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbdfce5b-2b98-4911-95cb-2feedf52d90e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 47 · 2026-05-22T23:27:19.141Z_

<details><summary>↩ Tool result · `toolu_019Zj3MfxzTty1Jjwc57h7Yu`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (140). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbdfce5b-2b98-4911-95cb-2feedf52d90e",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "8fa35a9a-e5fd-4f07-894d-b8b55522a069",
  "sourceToolAssistantUUID": "dbdfce5b-2b98-4911-95cb-2feedf52d90e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-22T23:27:19.891Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VFVAPR1WCSV5sLpeqZXRWC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 220,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fa35a9a-e5fd-4f07-894d-b8b55522a069",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09ae28e5-ca93-4786-8251-ab28f13609df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 49 · 2026-05-22T23:27:19.897Z_

<details><summary>↩ Tool result · `toolu_01VFVAPR1WCSV5sLpeqZXRWC`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (220). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09ae28e5-ca93-4786-8251-ab28f13609df",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "aae71776-77e3-4298-a780-4118607beeb8",
  "sourceToolAssistantUUID": "09ae28e5-ca93-4786-8251-ab28f13609df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-22T23:27:20.641Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EFyJnRYEecaaqhG3rh58rE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 300,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aae71776-77e3-4298-a780-4118607beeb8",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "218f93ce-b227-41e5-b857-afd29f8c50c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 51 · 2026-05-22T23:27:20.646Z_

<details><summary>↩ Tool result · `toolu_01EFyJnRYEecaaqhG3rh58rE`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (300). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "218f93ce-b227-41e5-b857-afd29f8c50c7",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "866dcd9c-fbb8-4082-bf96-543e3cf6382b",
  "sourceToolAssistantUUID": "218f93ce-b227-41e5-b857-afd29f8c50c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-22T23:27:21.395Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JRggamRmFn7G5ymS7X8yBa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 380,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "866dcd9c-fbb8-4082-bf96-543e3cf6382b",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2280e93f-c122-4e69-a670-3e417a5dc0e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 53 · 2026-05-22T23:27:21.403Z_

<details><summary>↩ Tool result · `toolu_01JRggamRmFn7G5ymS7X8yBa`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (380). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2280e93f-c122-4e69-a670-3e417a5dc0e1",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "3a83375b-0c8c-4c32-965f-4c33eadecb95",
  "sourceToolAssistantUUID": "2280e93f-c122-4e69-a670-3e417a5dc0e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-22T23:27:22.146Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MoqoY11ua4kUw3UL6bxXPs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 460,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a83375b-0c8c-4c32-965f-4c33eadecb95",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f4facdb-e119-40d5-9f7d-9ad5a0f810b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 55 · 2026-05-22T23:27:22.152Z_

<details><summary>↩ Tool result · `toolu_01MoqoY11ua4kUw3UL6bxXPs`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (460). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f4facdb-e119-40d5-9f7d-9ad5a0f810b3",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "b21eb9a9-7eca-4427-b776-bc0841fed272",
  "sourceToolAssistantUUID": "6f4facdb-e119-40d5-9f7d-9ad5a0f810b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-22T23:27:22.897Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SMWzExz9cPXPbRNxo747Wy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 540,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b21eb9a9-7eca-4427-b776-bc0841fed272",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c78ab26-ca82-4a9c-baf2-7bd4f979e4dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 57 · 2026-05-22T23:27:22.903Z_

<details><summary>↩ Tool result · `toolu_01SMWzExz9cPXPbRNxo747Wy`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (540). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c78ab26-ca82-4a9c-baf2-7bd4f979e4dd",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "ed46b6fb-19c2-4eb2-802f-c54005d475f7",
  "sourceToolAssistantUUID": "0c78ab26-ca82-4a9c-baf2-7bd4f979e4dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-22T23:27:23.681Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DPi7eTqh4ssbhWeipeJLcE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 620,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed46b6fb-19c2-4eb2-802f-c54005d475f7",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "700ebbb3-8c30-4a3a-9c48-88784af8388a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 59 · 2026-05-22T23:27:23.687Z_

<details><summary>↩ Tool result · `toolu_01DPi7eTqh4ssbhWeipeJLcE`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (620). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "700ebbb3-8c30-4a3a-9c48-88784af8388a",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "9f22f467-2a51-4d70-b454-42aab3e06f51",
  "sourceToolAssistantUUID": "700ebbb3-8c30-4a3a-9c48-88784af8388a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-22T23:27:24.792Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FkEME6HGTUjEcCpHWBsgyX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 700,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f22f467-2a51-4d70-b454-42aab3e06f51",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07d115ce-cb18-4c13-80df-6ba29dd1d397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 61 · 2026-05-22T23:27:24.797Z_

<details><summary>↩ Tool result · `toolu_01FkEME6HGTUjEcCpHWBsgyX`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (700). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07d115ce-cb18-4c13-80df-6ba29dd1d397",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "f3ec44e4-b486-425d-b109-484c40600aa7",
  "sourceToolAssistantUUID": "07d115ce-cb18-4c13-80df-6ba29dd1d397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-22T23:27:28.326Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KdYMmqkxDMYqX2mA1Do9E3`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== related_work.tex: key terms ===\"\ngrep -n \"experimental instrument\\|controlled causal\\|classification standard\\|disambiguation neglect\\|Disambiguation Neglect\" \"$BASE/related_work.tex\" | head -20\n\necho \"\"\necho \"=== analysis.tex: disambiguation neglect with emph ===\"\ngrep -n \"emph\\|neglect\\|Neglect\" \"$BASE/analysis.tex\" | head -20\n\necho \"\"\necho \"=== discussion.tex: disambiguation neglect with emph ===\"\ngrep -n \"emph\\|neglect\\|Neglect\" \"$BASE/discussion.tex\" | head -20\n\necho \"\"\necho \"=== conclusion.tex: domain qualification ===\"\ngrep -n \"customer\\|policy-governed\\|deployment\\|domain\\|scope\\|limit\" \"$BASE/conclusion.tex\" | head -20",
  "description": "Check multiple files for R18-N3, N4, W9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3ec44e4-b486-425d-b109-484c40600aa7",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66fd2e1b-adab-45e8-bd62-ba5f447975d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 63 · 2026-05-22T23:27:28.407Z_

<details><summary>↩ Tool result · `toolu_01KdYMmqkxDMYqX2mA1Do9E3`</summary>

```text
=== related_work.tex: key terms ===
5:Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
8:\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. At the pragmatic level, \citet{hu_pragmatic_2023} and \citet{ruis_goldilocks_2023} show that LLMs struggle with implicature resolution, defaulting to literal interpretations even when pragmatic inference is required. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output; \citet{gur_arieh_ambiguity_collapse_2026} taxonomize the epistemic risks of this ``ambiguity collapse''; \citet{sedova_to_know_2024} show analogous self-inconsistencies under entity-type ambiguity. These findings ground our \emph{disambiguation neglect} result: agents process ambiguous input without meta-cognitive awareness but, unlike humans, lack social channels to recover. \citet{disambiguation_cqa_survey_2025} survey disambiguation strategies in conversational QA; \citet{suri_structured_2025} show that structured uncertainty estimation improves coverage by 7--39\%, while \citet{sehwag_aspi_2026} demonstrate that clarification-seeking introduces prompt injection vulnerabilities---a tension for disambiguation channel design.

=== analysis.tex: disambiguation neglect with emph ===
1:\section{Error Analysis \emph{[Exploratory]}}
12:\emph{Structural misparse}: the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral level. Dominates scopal (5/5 models), conditional precedence (4/5), and coreferential (3/5).
14:\emph{Information gap-filling}: the agent fills missing information with plausible but incorrect defaults. Dominates incompleteness (3/5) and lexical (3/5).
16:\emph{Boundary violation}: the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial). Dominates authorization scope exclusively (5/5).
20:\subsection{Disambiguation Neglect}
23:Agents rarely recognize ambiguity. We code \emph{disambiguation awareness} versus \emph{surface adoption} (proceeding with a single interpretation). Overall awareness is 4.6\% ($\leq$11\% per model); Qwen3 and DeepSeek show zero across all 278 combined traces.
25:We refer to this pattern as \emph{disambiguation neglect}---the absence of disambiguation in default settings, not inability. Prior work shows LLMs collapse ambiguity into single interpretations \citep{liu_ambiguity_2023,hu_ambiguity_2025}; we extend this to agentic contexts where the result is irreversible policy violation. Our mitigation experiment ($-$8.5\,pp; Appendix~\ref{app:mitigation}) confirms disambiguation can be elicited.
29:Among ambiguous clauses, 41.3\% trigger majority-convergent violations ($\geq$3/5 models), degrading monotonically across thresholds ($\geq$2/5: 54.7\%, $\geq$4/5: 23.7\%, 5/5: 13.0\%)---a phenomenon we term \emph{systematic nocuity} \citep{berry_kamsties_2004}: models converge on the same incorrect interpretation, invisible in agreement-based evaluation. Of these, 83.9\% share the same dominant failure mode, confirming convergent---not coincident---violations. Incompleteness has the highest universal rate (24\%) and is disproportionately represented (OR $= 2.61$, $p = 0.019$).

=== discussion.tex: disambiguation neglect with emph ===
5:Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results support a \emph{differential nocuity} hypothesis \citep{willis_nocuous_2008}: risk depends on type, safety training, and disambiguation channel availability. The binary effect is domain-robust (interaction $p = 0.187$) but type rankings are not ($\rho = 0.26$), suggesting nocuity is universal while its type-specific profile requires per-domain calibration. Nevertheless, 60.8\% of variance remains unexplained (conversation trajectory, user-simulator stochasticity); clause-level auditing targets the largest controllable factor (22.4\%).
8:Type membership explains only 0.4\% of violation variance versus 22.4\% for clause wording; however, it predicts failure \emph{mechanism} 17$\times$ more strongly than violation rate (NMI ratio $\approx 17$; Appendix~\ref{app:type_mechanism}), validating the taxonomy as a diagnostic tool: each type maps to a dominant failure mechanism (\S\ref{sec:analysis}).

=== conclusion.tex: domain qualification ===
3:Policy ambiguity increases agent violations by 34.0\,pp (OR\,$=$\,15.1); clause wording explains 22.4\% of variance versus 0.4\% for type, while the taxonomy predicts failure mechanisms 17$\times$ better than violation rate. With $>$89\% disambiguation neglect and 41.3\% convergent violations, clause-level auditing is critical for customer-service and similar policy-governed deployments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66fd2e1b-adab-45e8-bd62-ba5f447975d7",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "ed4d1436-7178-42fe-a58f-66fe1c88cd66",
  "sourceToolAssistantUUID": "66fd2e1b-adab-45e8-bd62-ba5f447975d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-22T23:27:31.845Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vq4zwtahC8Zao6zafKqSLK`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== experiments.tex: Tjur, LPM footnote ===\"\ngrep -n \"Tjur\\|footnote\\|magnitudes differ\\|linear.*logistic\\|logistic.*linear\" \"$BASE/experiments.tex\" | head -20\n\necho \"\"\necho \"=== experiments.tex: upper bound, 18.7, confound-controlled range ===\"\ngrep -n \"upper bound\\|18\\.7\\|confound.controlled\\|information addition\" \"$BASE/experiments.tex\" | head -20\n\necho \"\"\necho \"=== experiments.tex: SOPBench ===\"\ngrep -n \"SOPBench\\|SOP\\|3/5\\|3 of 5\" \"$BASE/experiments.tex\" | head -20\n\necho \"\"\necho \"=== abstract.tex: should NOT have 2,997 or 1.0% model identity ===\"\ncat -n \"$BASE/abstract.tex\"",
  "description": "Check W1, W3, W5, W7 items"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed4d1436-7178-42fe-a58f-66fe1c88cd66",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2081a35e-92c8-443c-964b-7ed39fb3ee0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 65 · 2026-05-22T23:27:31.919Z_

<details><summary>↩ Tool result · `toolu_01Vq4zwtahC8Zao6zafKqSLK`</summary>

```text
=== experiments.tex: Tjur, LPM footnote ===
8:Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (conversation trajectory, user-simulator stochasticity). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; the confound-controlled range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope; Appendix~\ref{app:confound}).
18:\footnotesize

=== experiments.tex: upper bound, 18.7, confound-controlled range ===
8:Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (conversation trajectory, user-simulator stochasticity). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; the confound-controlled range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope; Appendix~\ref{app:confound}).
16:\caption{Violation rates (\%) under ambiguous policy clauses by type and model (5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla.\ = Claude, Qw3 = Qwen3, DS = DeepSeek). $\Delta$pp: pooled difference (ambiguous $-$ unambiguous) with Newcombe 95\% CIs. Tier: TOST equivalence cluster at $\pm 15$\,pp---U = upper bound (separated at all margins), M = mid-tier (6/6 pairwise equivalent), L = lower (separates at $\pm 12$\,pp). All per-type $p < 10^{-5}$ (Fisher's exact).}
30: & Coreferential & 31.6 & 18 & 32 & 22 & 42 & 44 & +18.7\,[11.5, 25.7] & L & $<\!10^{-6}$ \\
37:The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$). TOST equivalence testing at a $\pm 15$ pp margin reveals a graded equivalence structure among five types---authorization scope (41.6\%), lexical (42.8\%), scopal (39.4\%), and conditional precedence (36.8\%) form a mid-tier cluster, with coreferential (31.6\%) below---while incompleteness (53.6\%) stands apart as an upper bound---conditional on the confound controls in Appendix~\ref{app:confound}---whose ranking partly reflects an information-addition confound. Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.
41:An important qualification: cross-judge-group type rankings are discordant ($\rho = 0.09$, $p = 0.87$; Appendix~\ref{app:judge_group_ranking}), driven by authorization scope ranking first in one judge group but last in the other. Excluding it, the remaining five types show strong concordance ($\rho = 0.90$, $p = 0.037$). C2 should be interpreted as establishing robust extremes---incompleteness as upper bound and coreferential as lower bound---rather than a complete linear ordering.
43:Incompleteness is highest in four of five models (rates $\geq$46\% in all seven; Appendix~\ref{app:model_expansion}). Its unambiguous variant adds policy content, so the 49.2\,pp effect is an upper bound; a confound analysis confirms significance after controlling for information delta (Appendix~\ref{app:confound}). Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%.
48:\caption{Per-type effect sizes ($\Delta$pp) with Newcombe 95\% CIs. Types form a partial ordering: incompleteness as upper bound (conditional on information-addition confound), coreferential as lower bound, and a mid-range equivalence cluster. Mid-tier ordering is margin-dependent (\S\ref{sec:results}).}

=== experiments.tex: SOPBench ===
10:Replication on two additional model families confirms the effect across seven models ($\Delta = +20.0$ to $+33.6$\,pp; Appendix~\ref{app:model_expansion}); a cross-benchmark replication on SOPBench confirms directional consistency ($+13.8$\,pp pooled, 3/5 significant; Appendix~\ref{app:sopbench}). The taxonomy's primary value lies not in predicting clause risk but in predicting failure mechanisms: type predicts mechanism 17$\times$ more strongly than violation rate (\S\ref{sec:discussion}), making type-level analysis (C2--C4) informative for diagnosis.

=== abstract.tex: should NOT have 2,997 or 1.0% model identity ===
     1	\begin{abstract}
     2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (i.e., harmful), increasing violation rates by 34.0 percentage points (conditional OR $= 15.1$, matched-pair), with perturbation controls confirming specificity to semantic ambiguity. A variance decomposition reveals that individual clause wording explains 22.4\% of violation variance versus 0.4\% for ambiguity type, establishing clause-level wording as the dominant risk factor. However, a normalized mutual information analysis shows that type membership predicts failure \emph{mechanism} 17$\times$ more strongly than it predicts violation rate, establishing the taxonomy as a diagnostic tool for failure-mechanism prediction rather than risk prediction. Per-type effects range from $+$18.7 to $+$49.2\,pp, with incompleteness as the consistent upper bound. Error analysis reveals disambiguation neglect ($\leq$11\% per-model awareness) and \emph{systematic nocuity}: 41.3\% of clauses triggering model-convergent violations. These results, observed in customer-service policy domains, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
     3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2081a35e-92c8-443c-964b-7ed39fb3ee0c",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "d4462e0c-ebab-494b-8e3a-38b505ca2553",
  "sourceToolAssistantUUID": "2081a35e-92c8-443c-964b-7ed39fb3ee0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-22T23:27:33.503Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011gbsXUfqrkfbtGYdLxYXp4`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n\necho \"=== introduction.tex: full contributions list (look for items 1-3) ===\"\ngrep -n -A3 \"\\\\\\\\item\\|enumerate\\|contributions\\|contribute\" \"$BASE/introduction.tex\" | head -80",
  "description": "Read introduction contributions list with context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4462e0c-ebab-494b-8e3a-38b505ca2553",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9b9f369-a75e-4ddc-a106-a094ee368db0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 67 · 2026-05-22T23:27:33.557Z_

<details><summary>↩ Tool result · `toolu_011gbsXUfqrkfbtGYdLxYXp4`</summary>

```text
=== introduction.tex: full contributions list (look for items 1-3) ===
21:Our contributions are: (1)~the first matched-pair causal study of policy ambiguity's safety impact with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~a variance decomposition revealing that clause wording explains 22.4\% of violation variance versus 0.4\% for type, combined with a mutual information analysis showing that type predicts failure mechanism 17$\times$ better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool (\S\ref{sec:analysis}, \S\ref{sec:discussion}); and (3)~an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models (\S\ref{sec:analysis}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9b9f369-a75e-4ddc-a106-a094ee368db0",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "692d7ef3-06a0-4ea6-ba84-11c1839c3bb9",
  "sourceToolAssistantUUID": "d9b9f369-a75e-4ddc-a106-a094ee368db0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-22T23:27:34.209Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XFs8uY2nD415QrBujS3z25`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex",
  "offset": 1,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "692d7ef3-06a0-4ea6-ba84-11c1839c3bb9",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cada871-b13e-48ff-b171-877e0ac37df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 69 · 2026-05-22T23:27:34.215Z_

<details><summary>↩ Tool result · `toolu_01XFs8uY2nD415QrBujS3z25`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-layer ambiguity taxonomy and inject them into $\tau^2$-bench policy documents. Five models interact with the modified policies across 2,997 episodes. A cross-judge evaluation pipeline classifies violation severity on a four-tier scale.}
14	\label{fig:overview}
15	\end{figure*}
16	
17	We address this gap with a matched-pair causal study on $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark. Using a six-type taxonomy organized into two layers---linguistic and specification, including specification-level gaps that produce equivalent behavioral effects in LLM agents (\S\ref{sec:taxonomy}), we construct 300 ambiguous/unambiguous clause pairs and evaluate five architecturally diverse models across 2,997 episodes.
18	
19	Our results show that policy ambiguity is consistently nocuous for LLM agents ($+34.0$ pp violation rate increase, conditional OR $= 15.1$), but risk is driven by individual clause wording (22.4\% of variance) rather than type membership (0.4\%). The taxonomy's value lies in predicting failure mechanisms: type membership predicts the dominant mechanism 17$\times$ better than it predicts violation rate ($\text{NMI} = 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), enabling targeted diagnosis (\S\ref{sec:discussion}). Incompleteness is consistently the highest-risk type (46--62\% across all models); the remaining types form a partial ordering with robust extremes but margin-dependent mid-tier structure.
20	
21	Our contributions are: (1)~the first matched-pair causal study of policy ambiguity's safety impact with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~a variance decomposition revealing that clause wording explains 22.4\% of violation variance versus 0.4\% for type, combined with a mutual information analysis showing that type predicts failure mechanism 17$\times$ better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool (\S\ref{sec:analysis}, \S\ref{sec:discussion}); and (3)~an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models (\S\ref{sec:analysis}).
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cada871-b13e-48ff-b171-877e0ac37df3",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "19fdce61-b253-40a4-9092-9e84160f369f",
  "sourceToolAssistantUUID": "6cada871-b13e-48ff-b171-877e0ac37df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-22T23:27:35.163Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A1xK3arun5s8WDgmP2gXJ7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex",
  "offset": 80,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19fdce61-b253-40a4-9092-9e84160f369f",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a6e2bc7-9e1b-4ce0-8a6d-7f86e91e5d42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 71 · 2026-05-22T23:27:35.174Z_

<details><summary>↩ Tool result · `toolu_01A1xK3arun5s8WDgmP2gXJ7`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (80). The file has 22 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a6e2bc7-9e1b-4ce0-8a6d-7f86e91e5d42",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "020f8954-58b6-4e21-bd59-243d28aed80d",
  "sourceToolAssistantUUID": "0a6e2bc7-9e1b-4ce0-8a6d-7f86e91e5d42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-22T23:27:35.783Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cfc8RpzdAhybxjrmqeL981`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex",
  "offset": 160,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "020f8954-58b6-4e21-bd59-243d28aed80d",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "240d7b95-ed37-499c-baad-9b0242c040d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 73 · 2026-05-22T23:27:35.790Z_

<details><summary>↩ Tool result · `toolu_01Cfc8RpzdAhybxjrmqeL981`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (160). The file has 22 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "240d7b95-ed37-499c-baad-9b0242c040d5",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "eee884cb-7cab-40d4-a085-43385c2dbc8b",
  "sourceToolAssistantUUID": "240d7b95-ed37-499c-baad-9b0242c040d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-22T23:27:37.287Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CCoJskccsbsTGvkEAikZNv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex",
  "offset": 240,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eee884cb-7cab-40d4-a085-43385c2dbc8b",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "680cd401-4ce1-4995-a60c-7e4ce97fb119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 75 · 2026-05-22T23:27:37.292Z_

<details><summary>↩ Tool result · `toolu_01CCoJskccsbsTGvkEAikZNv`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (240). The file has 22 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "680cd401-4ce1-4995-a60c-7e4ce97fb119",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "ad9574f3-5673-4480-a01b-1426835f3f29",
  "sourceToolAssistantUUID": "680cd401-4ce1-4995-a60c-7e4ce97fb119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-22T23:27:38.094Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hz6etnWR6hCCFjiVbHzCjp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex",
  "offset": 1,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad9574f3-5673-4480-a01b-1426835f3f29",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da7b3a6b-cd5d-4fee-bae6-1e1233440475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 77 · 2026-05-22T23:27:38.100Z_

<details><summary>↩ Tool result · `toolu_01Hz6etnWR6hCCFjiVbHzCjp`</summary>

```text
1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse}: the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral level. Dominates scopal (5/5 models), conditional precedence (4/5), and coreferential (3/5).
13	
14	\emph{Information gap-filling}: the agent fills missing information with plausible but incorrect defaults. Dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation}: the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial). Dominates authorization scope exclusively (5/5).
17	
18	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models), with two achieving unanimity (scopal and authorization scope).
19	
20	\subsection{Disambiguation Neglect}
21	\label{sec:dn}
22	
23	Agents rarely recognize ambiguity. We code \emph{disambiguation awareness} versus \emph{surface adoption} (proceeding with a single interpretation). Overall awareness is 4.6\% ($\leq$11\% per model); Qwen3 and DeepSeek show zero across all 278 combined traces.
24	
25	We refer to this pattern as \emph{disambiguation neglect}---the absence of disambiguation in default settings, not inability. Prior work shows LLMs collapse ambiguity into single interpretations \citep{liu_ambiguity_2023,hu_ambiguity_2025}; we extend this to agentic contexts where the result is irreversible policy violation. Our mitigation experiment ($-$8.5\,pp; Appendix~\ref{app:mitigation}) confirms disambiguation can be elicited.
26	
27	\subsection{Systematic Nocuity}
28	
29	Among ambiguous clauses, 41.3\% trigger majority-convergent violations ($\geq$3/5 models), degrading monotonically across thresholds ($\geq$2/5: 54.7\%, $\geq$4/5: 23.7\%, 5/5: 13.0\%)---a phenomenon we term \emph{systematic nocuity} \citep{berry_kamsties_2004}: models converge on the same incorrect interpretation, invisible in agreement-based evaluation. Of these, 83.9\% share the same dominant failure mode, confirming convergent---not coincident---violations. Incompleteness has the highest universal rate (24\%) and is disproportionately represented (OR $= 2.61$, $p = 0.019$).
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da7b3a6b-cd5d-4fee-bae6-1e1233440475",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "1dda80db-3bfd-4f71-9f21-c738adc161a7",
  "sourceToolAssistantUUID": "da7b3a6b-cd5d-4fee-bae6-1e1233440475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-22T23:27:40.155Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KCHuXsHvq4xnWaDmAv9VMy`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\ngrep -n \"neglect\\|Neglect\\|DN\\b\\|emph\" \"$BASE/analysis.tex\" | head -30\necho \"---\"\ngrep -n \"neglect\\|Neglect\\|DN\\b\\|emph\" \"$BASE/discussion.tex\" | head -30\necho \"---\"\ngrep -n \"neglect\\|Neglect\\|DN\\b\\|emph\\|instrument\\|causal\" \"$BASE/related_work.tex\" | head -30",
  "description": "Comprehensive search for DN and taxonomy terms across files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dda80db-3bfd-4f71-9f21-c738adc161a7",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3832021d-f7f2-47e0-a974-150cd40fd845",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 79 · 2026-05-22T23:27:40.230Z_

<details><summary>↩ Tool result · `toolu_01KCHuXsHvq4xnWaDmAv9VMy`</summary>

```text
1:\section{Error Analysis \emph{[Exploratory]}}
12:\emph{Structural misparse}: the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral level. Dominates scopal (5/5 models), conditional precedence (4/5), and coreferential (3/5).
14:\emph{Information gap-filling}: the agent fills missing information with plausible but incorrect defaults. Dominates incompleteness (3/5) and lexical (3/5).
16:\emph{Boundary violation}: the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial). Dominates authorization scope exclusively (5/5).
20:\subsection{Disambiguation Neglect}
23:Agents rarely recognize ambiguity. We code \emph{disambiguation awareness} versus \emph{surface adoption} (proceeding with a single interpretation). Overall awareness is 4.6\% ($\leq$11\% per model); Qwen3 and DeepSeek show zero across all 278 combined traces.
25:We refer to this pattern as \emph{disambiguation neglect}---the absence of disambiguation in default settings, not inability. Prior work shows LLMs collapse ambiguity into single interpretations \citep{liu_ambiguity_2023,hu_ambiguity_2025}; we extend this to agentic contexts where the result is irreversible policy violation. Our mitigation experiment ($-$8.5\,pp; Appendix~\ref{app:mitigation}) confirms disambiguation can be elicited.
29:Among ambiguous clauses, 41.3\% trigger majority-convergent violations ($\geq$3/5 models), degrading monotonically across thresholds ($\geq$2/5: 54.7\%, $\geq$4/5: 23.7\%, 5/5: 13.0\%)---a phenomenon we term \emph{systematic nocuity} \citep{berry_kamsties_2004}: models converge on the same incorrect interpretation, invisible in agreement-based evaluation. Of these, 83.9\% share the same dominant failure mode, confirming convergent---not coincident---violations. Incompleteness has the highest universal rate (24\%) and is disproportionately represented (OR $= 2.61$, $p = 0.019$).
---
5:Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results support a \emph{differential nocuity} hypothesis \citep{willis_nocuous_2008}: risk depends on type, safety training, and disambiguation channel availability. The binary effect is domain-robust (interaction $p = 0.187$) but type rankings are not ($\rho = 0.26$), suggesting nocuity is universal while its type-specific profile requires per-domain calibration. Nevertheless, 60.8\% of variance remains unexplained (conversation trajectory, user-simulator stochasticity); clause-level auditing targets the largest controllable factor (22.4\%).
8:Type membership explains only 0.4\% of violation variance versus 22.4\% for clause wording; however, it predicts failure \emph{mechanism} 17$\times$ more strongly than violation rate (NMI ratio $\approx 17$; Appendix~\ref{app:type_mechanism}), validating the taxonomy as a diagnostic tool: each type maps to a dominant failure mechanism (\S\ref{sec:analysis}).
---
5:Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
8:\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. At the pragmatic level, \citet{hu_pragmatic_2023} and \citet{ruis_goldilocks_2023} show that LLMs struggle with implicature resolution, defaulting to literal interpretations even when pragmatic inference is required. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output; \citet{gur_arieh_ambiguity_collapse_2026} taxonomize the epistemic risks of this ``ambiguity collapse''; \citet{sedova_to_know_2024} show analogous self-inconsistencies under entity-type ambiguity. These findings ground our \emph{disambiguation neglect} result: agents process ambiguous input without meta-cognitive awareness but, unlike humans, lack social channels to recover. \citet{disambiguation_cqa_survey_2025} survey disambiguation strategies in conversational QA; \citet{suri_structured_2025} show that structured uncertainty estimation improves coverage by 7--39\%, while \citet{sehwag_aspi_2026} demonstrate that clarification-seeking introduces prompt injection vulnerabilities---a tension for disambiguation channel design.
11:The agent safety evaluation landscape includes benchmarks for risk awareness \citep{rjudge_2024}, tool-use safety \citep{toolemu_2024}, indirect prompt injection \citep{injecagent_2024}, safe task planning \citep{yin_safeagentbench_2025}, policy-invisible violations \citep{phantompolicy_2026}, comprehensive real-world agent safety \citep{vijayvargiya_openagentsafety_2026}, trajectory-level diagnosis \citep{atbench_2026}, and deployment-condition probing \citep{riskybench_2026}. \citet{mu_can_llms_2023} evaluate rule-following under policy constraints, \citet{tamkin_evaluating_2023} examine how language models navigate policy-governed decisions, \citet{shieldagent_2025} extract formal safety rules from policy documents, and AgentAuditor \citep{agentauditor_2025} achieves human-level safety evaluation. Our work differs by focusing on the \emph{source specification} rather than the agent's execution: we measure how ambiguity in the policy itself causes safety violations, complementing work that assumes clean policies.
14:DRIP-R \citep{drip_r_2026} is the closest concurrent work: it benchmarks 400 policy-ambiguous retail scenarios across five RE ambiguity types, measuring decision quality rather than safety violations. Our work differs in three respects: (1) our matched-pair design establishes causality rather than correlating ambiguity presence with outcomes; (2) we measure safety violations rather than decision quality, enabling failure mechanism analysis; (3) our two-layer taxonomy adds linguistic-layer types, and we quantify the model$\times$type interaction. We map DRIP-R's five RE ambiguity categories to our six-type taxonomy in Appendix~\ref{app:drip_mapping}. PolicyBank \citep{policybank_2026} studies iterative policy refinement, closing 82\% of the gap to a human oracle. AgentPex \citep{agentpex_2026} detects procedural violations in agentic traces, finding that 83\% of perfect-outcome traces contain violations. MANTRA \citep{mantra_2026} synthesizes SMT-validated compliance benchmarks from procedural manuals. $\tau$-bench \citep{tau_bench_2024} and its successor $\tau^2$-bench \citep{tau2_bench_2025} provide the conversational agent evaluation platforms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3832021d-f7f2-47e0-a974-150cd40fd845",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "2fd09396-25c9-416f-b745-bc02dc45d9ae",
  "sourceToolAssistantUUID": "3832021d-f7f2-47e0-a974-150cd40fd845",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-22T23:27:40.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T3CC62YZfosWSxjPcbhWGQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex",
  "offset": 1,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fd09396-25c9-416f-b745-bc02dc45d9ae",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd863e7e-face-4e20-84f2-f3d529fdf55e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 81 · 2026-05-22T23:27:40.873Z_

<details><summary>↩ Tool result · `toolu_01T3CC62YZfosWSxjPcbhWGQ`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. At the pragmatic level, \citet{hu_pragmatic_2023} and \citet{ruis_goldilocks_2023} show that LLMs struggle with implicature resolution, defaulting to literal interpretations even when pragmatic inference is required. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output; \citet{gur_arieh_ambiguity_collapse_2026} taxonomize the epistemic risks of this ``ambiguity collapse''; \citet{sedova_to_know_2024} show analogous self-inconsistencies under entity-type ambiguity. These findings ground our \emph{disambiguation neglect} result: agents process ambiguous input without meta-cognitive awareness but, unlike humans, lack social channels to recover. \citet{disambiguation_cqa_survey_2025} survey disambiguation strategies in conversational QA; \citet{suri_structured_2025} show that structured uncertainty estimation improves coverage by 7--39\%, while \citet{sehwag_aspi_2026} demonstrate that clarification-seeking introduces prompt injection vulnerabilities---a tension for disambiguation channel design.
9	
10	\paragraph{Agent safety evaluation.}
11	The agent safety evaluation landscape includes benchmarks for risk awareness \citep{rjudge_2024}, tool-use safety \citep{toolemu_2024}, indirect prompt injection \citep{injecagent_2024}, safe task planning \citep{yin_safeagentbench_2025}, policy-invisible violations \citep{phantompolicy_2026}, comprehensive real-world agent safety \citep{vijayvargiya_openagentsafety_2026}, trajectory-level diagnosis \citep{atbench_2026}, and deployment-condition probing \citep{riskybench_2026}. \citet{mu_can_llms_2023} evaluate rule-following under policy constraints, \citet{tamkin_evaluating_2023} examine how language models navigate policy-governed decisions, \citet{shieldagent_2025} extract formal safety rules from policy documents, and AgentAuditor \citep{agentauditor_2025} achieves human-level safety evaluation. Our work differs by focusing on the \emph{source specification} rather than the agent's execution: we measure how ambiguity in the policy itself causes safety violations, complementing work that assumes clean policies.
12	
13	\paragraph{Policy specification for agents.}
14	DRIP-R \citep{drip_r_2026} is the closest concurrent work: it benchmarks 400 policy-ambiguous retail scenarios across five RE ambiguity types, measuring decision quality rather than safety violations. Our work differs in three respects: (1) our matched-pair design establishes causality rather than correlating ambiguity presence with outcomes; (2) we measure safety violations rather than decision quality, enabling failure mechanism analysis; (3) our two-layer taxonomy adds linguistic-layer types, and we quantify the model$\times$type interaction. We map DRIP-R's five RE ambiguity categories to our six-type taxonomy in Appendix~\ref{app:drip_mapping}. PolicyBank \citep{policybank_2026} studies iterative policy refinement, closing 82\% of the gap to a human oracle. AgentPex \citep{agentpex_2026} detects procedural violations in agentic traces, finding that 83\% of perfect-outcome traces contain violations. MANTRA \citep{mantra_2026} synthesizes SMT-validated compliance benchmarks from procedural manuals. $\tau$-bench \citep{tau_bench_2024} and its successor $\tau^2$-bench \citep{tau2_bench_2025} provide the conversational agent evaluation platforms. 
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd863e7e-face-4e20-84f2-f3d529fdf55e",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "a3ee4926-5bef-4092-aab9-5a9b341161db",
  "sourceToolAssistantUUID": "cd863e7e-face-4e20-84f2-f3d529fdf55e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-22T23:27:41.616Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XFUPwSR44cTG7Ju5fRkadd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex",
  "offset": 80,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3ee4926-5bef-4092-aab9-5a9b341161db",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49418e9b-7521-40e5-a7fd-95257ddcfbea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 83 · 2026-05-22T23:27:41.621Z_

<details><summary>↩ Tool result · `toolu_01XFUPwSR44cTG7Ju5fRkadd`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (80). The file has 14 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49418e9b-7521-40e5-a7fd-95257ddcfbea",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "63c3c328-1f2d-4189-9386-0637ced55f35",
  "sourceToolAssistantUUID": "49418e9b-7521-40e5-a7fd-95257ddcfbea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-22T23:27:42.893Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jaf291na8a1rw8VPPpstj1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63c3c328-1f2d-4189-9386-0637ced55f35",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "304cfaa4-e9a0-4ac2-a479-218c66d1466e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 85 · 2026-05-22T23:27:42.903Z_

<details><summary>↩ Tool result · `toolu_01Jaf291na8a1rw8VPPpstj1`</summary>

```text
1	\section{Conclusion}
2	
3	Policy ambiguity increases agent violations by 34.0\,pp (OR\,$=$\,15.1); clause wording explains 22.4\% of variance versus 0.4\% for type, while the taxonomy predicts failure mechanisms 17$\times$ better than violation rate. With $>$89\% disambiguation neglect and 41.3\% convergent violations, clause-level auditing is critical for customer-service and similar policy-governed deployments.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "304cfaa4-e9a0-4ac2-a479-218c66d1466e",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "4c64728c-d8c2-4788-b5d4-5e5f6774fef6",
  "sourceToolAssistantUUID": "304cfaa4-e9a0-4ac2-a479-218c66d1466e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-22T23:27:45.235Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FKH8b2BkVWk8yzoFNqJVxL`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\ngrep -n \"neglect\\|Neglect\\|DN\\b\" \"$BASE/appendix.tex\" | head -20\necho \"---\"\n# Check if 17x NMI appears anywhere in intro\ngrep -n \"17\\|NMI\\|normaliz.*mutual\\|variance decomp\\|per.type effect\" \"$BASE/introduction.tex\" | head -20",
  "description": "Check appendix for DN and intro for NMI/17x"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c64728c-d8c2-4788-b5d4-5e5f6774fef6",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65775667-8939-459b-b225-99e9cbf9ced8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 87 · 2026-05-22T23:27:45.293Z_

<details><summary>↩ Tool result · `toolu_01FKH8b2BkVWk8yzoFNqJVxL`</summary>

```text
---
19:Our results show that policy ambiguity is consistently nocuous for LLM agents ($+34.0$ pp violation rate increase, conditional OR $= 15.1$), but risk is driven by individual clause wording (22.4\% of variance) rather than type membership (0.4\%). The taxonomy's value lies in predicting failure mechanisms: type membership predicts the dominant mechanism 17$\times$ better than it predicts violation rate ($\text{NMI} = 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), enabling targeted diagnosis (\S\ref{sec:discussion}). Incompleteness is consistently the highest-risk type (46--62\% across all models); the remaining types form a partial ordering with robust extremes but margin-dependent mid-tier structure.
21:Our contributions are: (1)~the first matched-pair causal study of policy ambiguity's safety impact with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~a variance decomposition revealing that clause wording explains 22.4\% of violation variance versus 0.4\% for type, combined with a mutual information analysis showing that type predicts failure mechanism 17$\times$ better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool (\S\ref{sec:analysis}, \S\ref{sec:discussion}); and (3)~an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models (\S\ref{sec:analysis}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65775667-8939-459b-b225-99e9cbf9ced8",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "5076e280-5379-47e1-b4d4-a661ee518b4d",
  "sourceToolAssistantUUID": "65775667-8939-459b-b225-99e9cbf9ced8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-22T23:27:47.265Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PAes86JRRDh8K3TyDjM2s4`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n# Check main.tex for any relevant content\nMAIN=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex\"\ngrep -n \"17\\|NMI\\|neglect\\|Neglect\\|SOPBench\\|Tjur\\|upper bound\\|18\\.7\\|suggestive\\|single.*judge\\|instrument\\|causal analysis\" \"$MAIN\" | head -30",
  "description": "Check main.tex for any relevant content not in section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5076e280-5379-47e1-b4d4-a661ee518b4d",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bea2029-8f39-4368-8181-dc526493f565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 89 · 2026-05-22T23:27:47.315Z_

<details><summary>↩ Tool result · `toolu_01PAes86JRRDh8K3TyDjM2s4`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bea2029-8f39-4368-8181-dc526493f565",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "2b9ed017-baee-4262-a6ea-a070adabef62",
  "sourceToolAssistantUUID": "4bea2029-8f39-4368-8181-dc526493f565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-22T23:27:50.421Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gzf36StD7xxiAaNQ29myZn`</summary>

```json
{
  "command": "BASE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections\"\n# Check if there's an experiments.tex at the top level paper dir\nls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/\necho \"---\"\n# Check the top-level experiments.tex if it exists\nif [ -f \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/experiments.tex\" ]; then\n  grep -n \"judge\\|single\\|suggestive\\|Tjur\\|upper bound\\|18\\.7\\|SOPBench\\|confound\" \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/experiments.tex\" | head -30\nfi",
  "description": "Check if experiments.tex exists at top level paper dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b9ed017-baee-4262-a6ea-a070adabef62",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dda8245-29ec-485c-8d9d-59b5dccfb894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 91 · 2026-05-22T23:27:50.518Z_

<details><summary>↩ Tool result · `toolu_01Gzf36StD7xxiAaNQ29myZn`</summary>

```text
_pdf_images
acl.sty
acl_natbib.bst
experiments.tex
fig1_intent.txt
figures
gen_fig1.py
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
references.bib
sections
---
27: & Coreferential & 31.6 & 18.0 & 32.0 & 22.0 & 42.0 & 44.0 & +18.7 & $<10^{-6}$ \\
34:The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$; statistical power $= 0.993$ at the observed effect). TOST equivalence testing confirms incompleteness as the consistent upper bound (53.6\%). The four mid-range types (lexical 42.8\% through conditional precedence 36.8\%) achieve full pairwise equivalence at a $\pm 15$\,pp margin but only partial equivalence at $\pm 10$\,pp, indicating a risk gradient rather than discrete tiers. Coreferential occupies the lower end (31.6\%). Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.
41:\caption{Per-type effect sizes ($\Delta$pp, ambiguous minus unambiguous) with Newcombe 95\% CIs. All types produce significant increases. Incompleteness is the consistent upper bound; remaining types show a risk gradient.}
57:\caption{Violation rates (\%) by model and ambiguity type under ambiguous conditions ($n = 2{,}997$). Authorization scope varies 52\,pp across models (Claude 12\% to GPT-5.4 64\%), an upper bound with substantial measurement uncertainty ($\kappa = 0.385$); incompleteness remains uniformly high (46--62\%).}
63:Figure~\ref{fig:heatmap} highlights three interaction patterns. First, authorization scope is the \emph{model-differentiating type}: its violation rate spans 52\,pp from Claude (12\%) to GPT-5.4 (64\%), though this range is an upper bound with substantial measurement uncertainty ($\kappa = 0.385$). Claude's low rate suggests that its safety training specifically addresses authorization boundary reasoning. Second, incompleteness is a \emph{universal vulnerability}: all models fall between 46\% and 62\% (16 pp range), indicating that safety training provides little protection when policy information is simply absent. Third, conditional precedence is the most \emph{model-invariant type} (34--40\%, 6 pp range), handled similarly across architectures.
65:Cross-model agreement on individual clauses is only fair (Fleiss' $\kappa = 0.384$). The binary effect is universal, but \emph{which specific clauses} trigger violations depends on the model. This clause-level disagreement, combined with the type-level interaction, indicates that safety alignment creates model-specific vulnerability profiles rather than a uniform defense. Notably, removing authorization scope from the analysis eliminates the model$\times$type interaction entirely ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}), confirming that C4 is primarily driven by differential safety-training responses to this single type.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dda8245-29ec-485c-8d9d-59b5dccfb894",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "6bf005c0-5209-4b65-b989-425a22d61641",
  "sourceToolAssistantUUID": "8dda8245-29ec-485c-8d9d-59b5dccfb894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-22T23:27:51.234Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JpYKHBJmQmc1Yqd3unuEFb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/experiments.tex",
  "offset": 1,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bf005c0-5209-4b65-b989-425a22d61641",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73d9a359-5ad4-41de-bf29-0fa1936446ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 93 · 2026-05-22T23:27:51.241Z_

<details><summary>↩ Tool result · `toolu_01JpYKHBJmQmc1Yqd3unuEFb`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four claims of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the layer effect (C3), and the model$\times$type interaction (C4).
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six ambiguity types, ambiguous policy clauses increase the violation rate by 34.0 percentage points (pp) relative to their unambiguous matched variants (41.0\% vs.\ 6.9\%, Mantel-Haenszel OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$; bootstrap 95\% CI for $\Delta$: $[31.2, 36.9]$ pp). All six ambiguity types individually produce significant increases (all Fisher $p < 10^{-5}$), and all five models show large, significant effects: Claude $+25.7$ pp, Qwen3 $+32.4$ pp, GPT-4.1 $+34.7$ pp, GPT-5.4 $+38.3$ pp, and DeepSeek $+39.0$ pp (all $p < 10^{-17}$). The perturbation control experiment (synonym substitution and clause reordering, $n = 120$) yields $\Delta_{\text{perturb}} = 3.33$ pp with a 95\% CI containing zero, confirming that the observed effect is specific to semantic ambiguity rather than surface-level prompt sensitivity.
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46.0 & 58.0 & 48.0 & 62.0 & 54.0 & +49.2 & $<10^{-37}$ \\
22	 & Auth.\ Scope & 41.6 & 64.0 & 46.0 & 12.0 & 26.0 & 60.0 & +36.0 & $<10^{-22}$ \\
23	 & Cond.\ Precedence & 36.8 & 34.0 & 36.0 & 36.0 & 40.0 & 38.0 & +30.8 & $<10^{-17}$ \\
24	\midrule
25	\multirow{3}{*}{\textcolor{lingcolor}{Ling.}} & Lexical & 42.8 & 42.0 & 34.0 & 32.0 & 52.0 & 54.0 & +35.2 & $<10^{-20}$ \\
26	 & Scopal & 39.4 & 42.0 & 38.0 & 32.0 & 36.7 & 48.0 & +34.2 & $<10^{-21}$ \\
27	 & Coreferential & 31.6 & 18.0 & 32.0 & 22.0 & 42.0 & 44.0 & +18.7 & $<10^{-6}$ \\
28	\midrule
29	\multicolumn{2}{l}{\textbf{Overall}} & \textbf{41.0} & 41.0 & 40.7 & 30.3 & 43.1 & 49.7 & \textbf{+34.0} & $<10^{-105}$ \\
30	\bottomrule
31	\end{tabular}
32	\end{table*}
33	
34	The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$; statistical power $= 0.993$ at the observed effect). TOST equivalence testing confirms incompleteness as the consistent upper bound (53.6\%). The four mid-range types (lexical 42.8\% through conditional precedence 36.8\%) achieve full pairwise equivalence at a $\pm 15$\,pp margin but only partial equivalence at $\pm 10$\,pp, indicating a risk gradient rather than discrete tiers. Coreferential occupies the lower end (31.6\%). Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.
35	
36	Incompleteness produces the highest violation rate in four of five models (all except GPT-5.4, where authorization scope ranks first at 64\%). Coreferential produces the lowest rate in three of five models. The 22 pp gap between the extremes (incompleteness 53.6\% vs.\ coreferential 31.6\%) is robust: coreferential agents occasionally adopt cautious strategies (conservative refusal rate 6--11\% vs.\ 2--3\% average), partially resolving ambiguity through tool responses.
37	
38	\begin{figure}[t]
39	\centering
40	\includegraphics[width=\columnwidth]{figures/fig2_forest_plot.pdf}
41	\caption{Per-type effect sizes ($\Delta$pp, ambiguous minus unambiguous) with Newcombe 95\% CIs. All types produce significant increases. Incompleteness is the consistent upper bound; remaining types show a risk gradient.}
42	\label{fig:forest_plot}
43	\end{figure}
44	
45	\subsection{Layer Effect (C3)}
46	
47	Specification-layer types produce higher violation rates than linguistic-layer types on average (44.0\% vs.\ 37.9\%, $\Delta = 6.08$ pp, $\chi^2 = 5.73$, $p = 0.017$, $V = 0.062$, OR $= 1.29$ $[1.05, 1.58]$). This aggregate, however, masks substantial model dependence. GPT-5.4 and GPT-4.1 show a strong layer gap ($+14.0$ pp and $+12.0$ pp respectively), driven by their high authorization scope vulnerability (64\% and 46\%). Claude shows a weak gap ($+3.3$ pp), DeepSeek a negligible one ($+2.0$ pp), and Qwen3 reverses the direction ($-0.9$ pp). The mid-tier overlap between conditional precedence (36.8\%, specification) and scopal (39.4\%, linguistic) further illustrates that the layer boundary is not a clean threshold. We therefore treat C3 as a secondary finding that motivates the more informative model$\times$type interaction (C4).
48	
49	Per-type ICC values from the reproducibility study mirror this pattern: linguistic-layer types achieve excellent reliability (scopal 0.989, lexical 0.981, coreferential 0.976), while specification-layer types show good but lower reliability (authorization scope 0.857, conditional precedence 0.856, incompleteness 0.807). Agents produce more variable outputs when external disambiguation channels are absent, consistent with the forced-guessing mechanism hypothesized for specification-layer ambiguity.
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73d9a359-5ad4-41de-bf29-0fa1936446ce",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "105fbebd-36c8-4311-9ed1-6787ee9f72ee",
  "sourceToolAssistantUUID": "73d9a359-5ad4-41de-bf29-0fa1936446ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-22T23:27:53.871Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VGZv9ZLnKB6etmMGeXrdKG`</summary>

```json
{
  "command": "# Check if sections/experiments.tex vs top-level experiments.tex differ significantly\nwc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/experiments.tex\nwc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex\n\n# Which one is included in main.tex?\ngrep -n \"input\\|include\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex | head -20",
  "description": "Determine which experiments.tex is used in main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "105fbebd-36c8-4311-9ed1-6787ee9f72ee",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81737343-5812-498f-8d51-2909f0904d32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 95 · 2026-05-22T23:27:53.933Z_

<details><summary>↩ Tool result · `toolu_01VGZv9ZLnKB6etmMGeXrdKG`</summary>

```text
64 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/experiments.tex
69 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
6:\usepackage[utf8]{inputenc}
26:\input{sections/abstract}
27:\input{sections/introduction}
28:\input{sections/related_work}
29:\input{sections/taxonomy}
30:\input{sections/method}
31:\input{sections/experiments}
32:\input{sections/analysis}
33:\input{sections/discussion}
34:\input{sections/conclusion}
35:\input{sections/limitations}
40:\input{sections/appendix}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81737343-5812-498f-8d51-2909f0904d32",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "a0655b77-14f0-4b8a-ad02-d12cce35e9f1",
  "sourceToolAssistantUUID": "81737343-5812-498f-8d51-2909f0904d32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-22T23:27:54.817Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GayBXVwJDW6FPR7KnKqBRM`</summary>

```json
{
  "command": "grep -n \"judge\\|single\\|suggestive\\|Tjur\\|upper bound\\|18\\.7\\|SOPBench\\|confound\\|footnote\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex | head -50",
  "description": "Full search of sections/experiments.tex for all W-items"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0655b77-14f0-4b8a-ad02-d12cce35e9f1",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f7bed0f-105d-4e43-a2a4-f5ea4a1c8856",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 97 · 2026-05-22T23:27:54.871Z_

<details><summary>↩ Tool result · `toolu_01GayBXVwJDW6FPR7KnKqBRM`</summary>

```text
8:Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (conversation trajectory, user-simulator stochasticity). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; the confound-controlled range is $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope; Appendix~\ref{app:confound}).
10:Replication on two additional model families confirms the effect across seven models ($\Delta = +20.0$ to $+33.6$\,pp; Appendix~\ref{app:model_expansion}); a cross-benchmark replication on SOPBench confirms directional consistency ($+13.8$\,pp pooled, 3/5 significant; Appendix~\ref{app:sopbench}). The taxonomy's primary value lies not in predicting clause risk but in predicting failure mechanisms: type predicts mechanism 17$\times$ more strongly than violation rate (\S\ref{sec:discussion}), making type-level analysis (C2--C4) informative for diagnosis.
16:\caption{Violation rates (\%) under ambiguous policy clauses by type and model (5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla.\ = Claude, Qw3 = Qwen3, DS = DeepSeek). $\Delta$pp: pooled difference (ambiguous $-$ unambiguous) with Newcombe 95\% CIs. Tier: TOST equivalence cluster at $\pm 15$\,pp---U = upper bound (separated at all margins), M = mid-tier (6/6 pairwise equivalent), L = lower (separates at $\pm 12$\,pp). All per-type $p < 10^{-5}$ (Fisher's exact).}
18:\footnotesize
30: & Coreferential & 31.6 & 18 & 32 & 22 & 42 & 44 & +18.7\,[11.5, 25.7] & L & $<\!10^{-6}$ \\
37:The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$). TOST equivalence testing at a $\pm 15$ pp margin reveals a graded equivalence structure among five types---authorization scope (41.6\%), lexical (42.8\%), scopal (39.4\%), and conditional precedence (36.8\%) form a mid-tier cluster, with coreferential (31.6\%) below---while incompleteness (53.6\%) stands apart as an upper bound---conditional on the confound controls in Appendix~\ref{app:confound}---whose ranking partly reflects an information-addition confound. Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.
39:Sensitivity analysis across seven margins ($\pm 5$--$20$ pp; Appendix~\ref{app:tost}) confirms this structure is margin-dependent: mid-tier cohesion emerges at $\pm 12$ pp and stabilizes at $\pm 15$ pp, while the incompleteness upper-bound is robust across all margins. A bootstrap cluster analysis ($B = 10{,}000$; Appendix~\ref{app:cluster}) corroborates: incompleteness forms a singleton at $k = 2$, coreferential additionally separates at $k = 3$. Cross-model type ranking concordance is moderate ($W = 0.398$, $p = 0.072$; Appendix~\ref{app:kendall_w}), driven by incompleteness ranking highest in four of five models.
41:An important qualification: cross-judge-group type rankings are discordant ($\rho = 0.09$, $p = 0.87$; Appendix~\ref{app:judge_group_ranking}), driven by authorization scope ranking first in one judge group but last in the other. Excluding it, the remaining five types show strong concordance ($\rho = 0.90$, $p = 0.037$). C2 should be interpreted as establishing robust extremes---incompleteness as upper bound and coreferential as lower bound---rather than a complete linear ordering.
43:Incompleteness is highest in four of five models (rates $\geq$46\% in all seven; Appendix~\ref{app:model_expansion}). Its unambiguous variant adds policy content, so the 49.2\,pp effect is an upper bound; a confound analysis confirms significance after controlling for information delta (Appendix~\ref{app:confound}). Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%.
48:\caption{Per-type effect sizes ($\Delta$pp) with Newcombe 95\% CIs. Types form a partial ordering: incompleteness as upper bound (conditional on information-addition confound), coreferential as lower bound, and a mid-range equivalence cluster. Mid-tier ordering is margin-dependent (\S\ref{sec:results}).}
62:\caption{Violation rates (\%) by model and type under ambiguous conditions ($n = 2{,}997$). Authorization scope varies 52\,pp across models ($\kappa = 0.385$); incompleteness remains uniformly high (46--62\%). C4 interaction is authorization-scope-specific (excluding it: $p = 0.97$). Each model was evaluated by a single judge; C4 patterns should be interpreted cautiously.}
68:Figure~\ref{fig:heatmap} highlights three patterns: (1) authorization scope is the \emph{most model-differentiating type} (52\,pp range; Claude 12\% to GPT-5.4 64\%), though its low judge agreement ($\kappa = 0.385$) adds uncertainty; (2) incompleteness is a \emph{consistent vulnerability} (46--62\%); (3) conditional precedence is the most \emph{model-invariant} (34--40\%). The authorization scope ranking is stable within the GPT-5.4 judge subset (bootstrap preservation: 99.5\%), and the 34\,pp within-judge range far exceeds measurement noise; given the low cross-judge $\kappa$, we characterize this as suggestive given the single-judge-per-model design (\S\ref{sec:limitations}). Excluding authorization scope, the residual interaction vanishes ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f7bed0f-105d-4e43-a2a4-f5ea4a1c8856",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "159ff088-e5de-41dd-97fd-7e1163ca16ca",
  "sourceToolAssistantUUID": "4f7bed0f-105d-4e43-a2a4-f5ea4a1c8856",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-22T23:27:55.918Z_

<details open><summary>🔧 Tool call — Read · `toolu_017cGmpo75muFWubLDmpEUHt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 780,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "159ff088-e5de-41dd-97fd-7e1163ca16ca",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b6df2a9-651f-41eb-9aee-23ac738cf63e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 99 · 2026-05-22T23:27:55.924Z_

<details><summary>↩ Tool result · `toolu_017cGmpo75muFWubLDmpEUHt`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (780). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b6df2a9-651f-41eb-9aee-23ac738cf63e",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "4ade4e6c-247a-403d-a622-acaa978fd2d2",
  "sourceToolAssistantUUID": "9b6df2a9-651f-41eb-9aee-23ac738cf63e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-22T23:27:56.672Z_

<details open><summary>🔧 Tool call — Read · `toolu_015pf6rPTU6PaJDF9ZS1Z72N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 860,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ade4e6c-247a-403d-a622-acaa978fd2d2",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e75d059d-1274-4d08-bbf7-be3fd27cc7cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30297,
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

_source line 101 · 2026-05-22T23:27:56.686Z_

<details><summary>↩ Tool result · `toolu_015pf6rPTU6PaJDF9ZS1Z72N`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (860). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e75d059d-1274-4d08-bbf7-be3fd27cc7cb",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "9e5bfd50-5fa3-4b2a-9d4c-eb80a53df301",
  "sourceToolAssistantUUID": "e75d059d-1274-4d08-bbf7-be3fd27cc7cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-22T23:28:24.026Z_

<details open><summary>🔧 Tool call — Read · `toolu_015svx9gsRnCYQvxHHJqPhYq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": 940,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e5bfd50-5fa3-4b2a-9d4c-eb80a53df301",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUNgSMSPJLDPqaA16t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a0c61b1-3fd4-42be-aa21-f14340860c85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BsDHPYdZYJCGtmbAKVr3Gc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30297,
      "cache_read_input_tokens": 0,
      "output_tokens": 9638,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 30297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 9638,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 30297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 30297,
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

_source line 103 · 2026-05-22T23:28:24.033Z_

<details><summary>↩ Tool result · `toolu_015svx9gsRnCYQvxHHJqPhYq`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (940). The file has 70 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a0c61b1-3fd4-42be-aa21-f14340860c85",
  "isSidechain": true,
  "promptId": "093836c3-d136-48f8-a1b6-6aca0ad64e09",
  "agentId": "a2b27f987e62a3e88",
  "type": "user",
  "uuid": "3f21f74a-48b6-4666-ace9-2e23e3520a88",
  "sourceToolAssistantUUID": "9a0c61b1-3fd4-42be-aa21-f14340860c85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny"
}
```

</details>

---

### Assistant

_source line 104 · 2026-05-22T23:28:51.363Z_

All items have been verified. Here is the complete status report:

---

**R18-N1 (C2 demotion)**
- **abstract.tex**: CONFIRMED. No "scopal > lexical" ordering. Contains "Per-type effects range from +18.7 to +49.2 pp, with incompleteness as the consistent upper bound." (line 2) and "partial ordering with robust extremes but margin-dependent mid-tier structure" (introduction.tex line 19).
- **introduction.tex contribution (2)**: CONFIRMED. Line 21: "a variance decomposition revealing...17× better than violation rate, motivating type-level analysis as a diagnostic rather than predictive tool."

**R18-N2 (Judge confound)**
- **experiments.tex Fig 3 caption** (line 62): CONFIRMED. "Each model was evaluated by a single judge; C4 patterns should be interpreted cautiously."
- **experiments.tex §5.4 body** (line 68): CONFIRMED. "we characterize this as suggestive given the single-judge-per-model design (§\ref{sec:limitations})."

**R18-N3 (Taxonomy demotion)**
- **related_work.tex** (line 5): CONFIRMED. "Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard."
- **introduction.tex contribution (3)** (line 21): CONFIRMED. "an error analysis revealing type-specific failure mechanisms and convergent violation patterns across models."

**R18-N4 (DN demotion — lowercase with \emph{})**
- **analysis.tex** (line 25): CONFIRMED. `\emph{disambiguation neglect}` used; section header at line 20 is `\subsection{Disambiguation Neglect}` (capitalized as a heading, acceptable). Body use is lowercase with emph.
- **discussion.tex**: CONFIRMED. No capitalized "Disambiguation Neglect" in body text; "disambiguation neglect" appears as part of the `\emph{disambiguation neglect} result` phrase (related_work.tex line 8) and as a referenced result (discussion.tex line 8 refers to failure mechanism, no DN capitalization).
- **related_work.tex** (line 8): CONFIRMED. `\emph{disambiguation neglect}` lowercase with emph.

**R18-W1 (LPM footnote with Tjur)**
- **experiments.tex §5.1** (line 8, footnote): CONFIRMED. "logistic regression...confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications."

**R18-W3 (Incompleteness upper-bound)**
- **experiments.tex §5.1** (line 8): CONFIRMED. "The incompleteness effect (+49.2 pp) is an upper bound that includes information addition; the confound-controlled range is +18.7 pp (coreferential) to +36.0 pp."

**R18-W5 (SOPBench)**
- **experiments.tex** (line 10): CONFIRMED. "a cross-benchmark replication on SOPBench confirms directional consistency (+13.8 pp pooled, 3/5 significant; Appendix~\ref{app:sopbench})."

**R18-W7 (Abstract numbers)**
- **abstract.tex**: CONFIRMED (negative check passes). Neither "2,997 episodes" nor "1.0% for model identity" appears in abstract.tex. The abstract contains no episode count and no model identity variance figure.

**R18-W8 (Page limit)**: Skipped per instructions.

**R18-W9 (Conclusion domain-qualified)**
- **conclusion.tex** (line 3): CONFIRMED. "clause-level auditing is critical for customer-service and similar policy-governed deployments."

---

**Summary: All 9 checked items are CONFIRMED present (R18-W7 confirmed absent as required).** No items are missing from the LaTeX source files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f21f74a-48b6-4666-ace9-2e23e3520a88",
  "isSidechain": true,
  "agentId": "a2b27f987e62a3e88",
  "requestId": "req_011CbJUWRi4AH8z7fe1JsnqD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1db243c9-3534-42a8-b1b2-d14f0a657f9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "72de1eb6-36e9-461f-a9f4-a4e64eb0f843",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-meandering-bunny",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01V866nUi6DjvnadUHkTjYJE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 68378,
      "cache_read_input_tokens": 8972,
      "output_tokens": 972,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 68378
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 972,
          "cache_read_input_tokens": 8972,
          "cache_creation_input_tokens": 68378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 68378,
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
