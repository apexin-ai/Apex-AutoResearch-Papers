# Research conversation: I need you to extract all confirmed experimental results from the registry file for a paper rewrite. The file is at: /ho

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a97ebe3840b34757a.jsonl`
- **Structured JSON:** [`e71e2d18946ac87de60d.json`](../../sessions/e7/e71e2d18946ac87de60d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-20T10:43:57.200Z_

I need you to extract all confirmed experimental results from the registry file for a paper rewrite. The file is at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/c7ddc740-cffe-49a2-afe7-879cf8dde3ec/tool-results/mcp-agent-ml-research-read_registry-1779273820823.txt

It's JSON with schema: {result: string}. The `result` field contains YAML text of experiment entries.

I need you to extract and report back ALL of the following data points, organized by experiment ID. For each experiment, report: exp_id, status, conclusion, and ALL metrics (especially F1 scores, Spearman rho, AUROC, degeneracy rates, p-values, etc.).

Focus especially on experiments related to:
1. Quality estimation (QE) — Spearman ρ, AUROC for each signal (LP, SJ, VC, FK, EM) on each dataset (SciERC, CoNLL, WNUT, FewNERD)
2. Sample selection — best-of-N F1 vs greedy, LP gain, p-values
3. Entity construction — majority vote F1, LP-weighted construction F1, gains over greedy
4. Instance degeneracy rates per dataset/model
5. Scaling experiments — varying N, model size (4B/8B/72B), few-shot
6. Temperature ablations
7. Epoch ablations
8. Any Holm-Bonferroni corrected p-values
9. Oracle headroom
10. Hidden probe results
11. DALS/DGS/alternative selection results

Probe the structure first with jq, then extract ALL experiment entries. Report every metric verbatim — do not summarize or round numbers. This data will be used to write paper tables and claims, so accuracy is critical.

Quote all numbers exactly as they appear in the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9d5a8dbf-14d3-41c1-a18a-ef8acd67e6cb",
  "agentId": "a97ebe3840b34757a",
  "type": "user",
  "uuid": "f516d66e-cc17-4886-bda8-1c3b691334e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T10:43:57.274Z_

```json
{
  "parentUuid": "f516d66e-cc17-4886-bda8-1c3b691334e9",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
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
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "4eb1621d-0595-4486-87ac-6cfb4cbb7095",
  "timestamp": "2026-05-20T10:43:57.274Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake"
}
```

---

### Assistant

_source line 3 · 2026-05-20T10:44:03.016Z_

I'll extract all experimental results from the registry file. Let me start by probing the structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eb1621d-0595-4486-87ac-6cfb4cbb7095",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
  "requestId": "req_011CbDgbYzs9oNB1uhjbpP9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f182eab-8393-4b03-95f4-a01b2c55d8f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QpWd38VJQkMbrEpR1tkWE5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24364,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24364,
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

_source line 4 · 2026-05-20T10:44:05.095Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SDA2ERJ5ZFdpYSErA9qSi7`</summary>

```json
{
  "command": "cat \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/c7ddc740-cffe-49a2-afe7-879cf8dde3ec/tool-results/mcp-agent-ml-research-read_registry-1779273820823.txt\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nprint('Keys:', list(data.keys()))\nprint('Result type:', type(data['result']))\nprint('Result length:', len(data['result']))\nprint('First 500 chars:')\nprint(data['result'][:500])\n\"",
  "description": "Probe the JSON structure of the registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f182eab-8393-4b03-95f4-a01b2c55d8f6",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
  "requestId": "req_011CbDgbYzs9oNB1uhjbpP9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a186b266-9833-4472-aae3-73083c9f0441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QpWd38VJQkMbrEpR1tkWE5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24364,
      "cache_read_input_tokens": 0,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24364
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 285,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 24364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24364,
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

_source line 5 · 2026-05-20T10:44:05.293Z_

<details><summary>↩ Tool result · `toolu_01SDA2ERJ5ZFdpYSErA9qSi7`</summary>

```text
Keys: ['result']
Result type: &lt;class 'str'>
Result length: 137092
First 500 chars:
{"success": true, "data": {"experiments": {"exp_b2_entity_verifier": {"status": "PREPARING", "created_at": "2026-05-20T10:13:41.037Z", "updated_at": "2026-05-20T10:14:00.616Z", "hypothesis": "An XGBoost/LightGBM entity-level verifier trained on agreement_count, VC, LP features can predict whether entity candidates are in gold annotations, enabling post-hoc filtering or score-weighted construction that improves over greedy baseline, with cross-dataset generalization from CoNLL+SciERC to FewNERD+W
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a186b266-9833-4472-aae3-73083c9f0441",
  "isSidechain": true,
  "promptId": "9d5a8dbf-14d3-41c1-a18a-ef8acd67e6cb",
  "agentId": "a97ebe3840b34757a",
  "type": "user",
  "uuid": "b593a8d0-5c0a-4eb6-86ae-a5c58a6ac23c",
  "sourceToolAssistantUUID": "a186b266-9833-4472-aae3-73083c9f0441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T10:44:13.020Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jz6sFb6B6WPVN66J14yy6S`</summary>

```json
{
  "command": "cat \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/c7ddc740-cffe-49a2-afe7-879cf8dde3ec/tool-results/mcp-agent-ml-research-read_registry-1779273820823.txt\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexperiments = inner['data']['experiments']\nprint('Total experiments:', len(experiments))\nprint('Experiment IDs:')\nfor eid in sorted(experiments.keys()):\n    e = experiments[eid]\n    print(f'  {eid}: status={e.get(\\\"status\\\", \\\"?\\\")}, has_results={\\\"results\\\" in e or \\\"metrics\\\" in e}')\n\"",
  "description": "List all experiment IDs and their statuses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b593a8d0-5c0a-4eb6-86ae-a5c58a6ac23c",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
  "requestId": "req_011CbDgc9GPd2y3NGw9nByWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0271b53b-66a3-4f1b-b015-b7897319211b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ph3hgRMC5aURUCp8eizeAz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1322,
      "cache_read_input_tokens": 24364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1322,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 7 · 2026-05-20T10:44:13.108Z_

<details><summary>↩ Tool result · `toolu_01Jz6sFb6B6WPVN66J14yy6S`</summary>

```text
Total experiments: 181
Experiment IDs:
  dgs_pilot: status=DONE, has_results=False
  e1_component_wise_re_sj: status=DONE, has_results=True
  exp001_seed123: status=DONE, has_results=False
  exp001_seed456: status=DONE, has_results=False
  exp008_re_n16: status=DONE, has_results=False
  exp_001_n16_seed123: status=DONE, has_results=True
  exp_001_n16_seed123_full: status=DONE, has_results=False
  exp_001_n16_seed456: status=DONE, has_results=True
  exp_001_n16_seed456_full: status=DONE, has_results=False
  exp_001_ner_n16_scierc: status=DONE, has_results=True
  exp_001_ner_n16_seed123: status=DONE, has_results=True
  exp_001_seed123_t10_full: status=DONE, has_results=True
  exp_001_seed123_v2: status=DONE, has_results=True
  exp_001_seed123_v2_r1024: status=DONE, has_results=False
  exp_001_seed42_v2: status=DONE, has_results=True
  exp_001_seed42_v2_r1024: status=DONE, has_results=True
  exp_001_seed456_t10_full: status=DONE, has_results=True
  exp_001_seed456_v2: status=DONE, has_results=False
  exp_001_seed456_v2_ner: status=DONE, has_results=True
  exp_001_seed456_v2_ner_r1024: status=DONE, has_results=False
  exp_002: status=DONE, has_results=True
  exp_002_conll_n16: status=DONE, has_results=True
  exp_002_conll_n16_r1024: status=DONE, has_results=False
  exp_002_conll_n16_seed123: status=DONE, has_results=True
  exp_002_conll_n16_seed456: status=DONE, has_results=True
  exp_002_merge_conll2003: status=DONE, has_results=False
  exp_002_ner_conll2003: status=DONE, has_results=False
  exp_003_ner_wnut17: status=DONE, has_results=True
  exp_003_wnut17_eval: status=DONE, has_results=True
  exp_003_wnut17_v2: status=DONE, has_results=False
  exp_004_re_diagnostic: status=DONE, has_results=True
  exp_004_v2: status=DONE, has_results=False
  exp_005: status=DONE, has_results=False
  exp_005_v2: status=DONE, has_results=False
  exp_006_v2: status=DONE, has_results=True
  exp_007_llama_inference: status=DONE, has_results=True
  exp_007_llama_n16: status=DONE, has_results=True
  exp_007_llama_n16_r1024: status=DONE, has_results=False
  exp_007_llama_scierc_seed123: status=DONE, has_results=True
  exp_007_llama_seed123: status=DONE, has_results=True
  exp_007_llama_seed456: status=DONE, has_results=True
  exp_007_ner_llama: status=DONE, has_results=False
  exp_007_ner_multi_model: status=DONE, has_results=True
  exp_008_re_n16: status=DONE, has_results=True
  exp_008_re_n16_full: status=DONE, has_results=False
  exp_008_re_n16_t10_full: status=DONE, has_results=True
  exp_008_re_n16_v2: status=DONE, has_results=True
  exp_008_re_seed123: status=DONE, has_results=True
  exp_009_capability_stratification: status=DONE, has_results=True
  exp_009_v2: status=DONE, has_results=True
  exp_009_v2_re_rerun: status=DONE, has_results=False
  exp_010_selection_curves: status=DONE, has_results=True
  exp_011_ood_conll_to_scierc: status=DONE, has_results=True
  exp_011_ood_scierc_to_conll: status=DONE, has_results=True
  exp_012_logprob_baseline: status=DONE, has_results=True
  exp_012_rerun_1024: status=DONE, has_results=True
  exp_013_exact_match_voting: status=DONE, has_results=True
  exp_014_entity_majority_voting: status=DONE, has_results=True
  exp_015_metrics_expansion: status=DONE, has_results=True
  exp_015_v2: status=DONE, has_results=True
  exp_016_rerun_1024_bootstrap: status=DONE, has_results=True
  exp_016_signal_ensemble: status=DONE, has_results=True
  exp_016_v2: status=DONE, has_results=True
  exp_017_llama_conll: status=DONE, has_results=True
  exp_017_llama_conll_finetune: status=DONE, has_results=True
  exp_017_llama_conll_infer: status=DONE, has_results=True
  exp_017_llama_conll_n16: status=DONE, has_results=True
  exp_017_llama_conll_n16_r1024: status=DONE, has_results=True
  exp_017_llama_conll_n16_s123: status=DONE, has_results=True
  exp_017_llama_conll_n16_s123_r1024: status=DONE, has_results=True
  exp_017_llama_conll_n16_s456: status=DONE, has_results=True
  exp_017_llama_conll_n16_s456_r1024: status=DONE, has_results=True
  exp_017_llama_conll_n8_t07: status=DONE, has_results=True
  exp_018_llama_scierc_seed123: status=DONE, has_results=True
  exp_018_llama_scierc_seed42_r1024: status=DONE, has_results=True
  exp_018_llama_scierc_seed456: status=DONE, has_results=False
  exp_018_llama_scierc_seed456_r1024: status=DONE, has_results=True
  exp_018_qwen_scierc_seed123: status=DONE, has_results=True
  exp_018_qwen_scierc_seed456: status=DONE, has_results=True
  exp_019_supervised_verifier: status=DONE, has_results=False
  exp_020_fewnerd_smoke: status=DONE, has_results=True
  exp_021_fewnerd_full: status=DONE, has_results=True
  exp_021_fewnerd_n8_seed123: status=DONE, has_results=True
  exp_021_fewnerd_n8_seed456: status=DONE, has_results=True
  exp_022_seed789: status=DONE, has_results=False
  exp_023_lora_rank8: status=DONE, has_results=True
  exp_024_claim_audit: status=DONE, has_results=True
  exp_025_n32: status=DONE, has_results=True
  exp_026_T05: status=DONE, has_results=True
  exp_026_T08: status=DONE, has_results=True
  exp_026_T12: status=DONE, has_results=True
  exp_026_t05: status=DONE, has_results=True
  exp_026_t05_scierc: status=DONE, has_results=False
  exp_026_t05_seed123: status=DONE, has_results=True
  exp_026_t05_seed456: status=DONE, has_results=True
  exp_026_t08: status=DONE, has_results=True
  exp_026_t08_scierc: status=DONE, has_results=False
  exp_026_t08_seed123: status=DONE, has_results=True
  exp_026_t08_seed456: status=DONE, has_results=True
  exp_026_t10_seed123: status=DONE, has_results=True
  exp_026_t10_seed42: status=DONE, has_results=True
  exp_026_t10_seed456: status=DONE, has_results=True
  exp_026_t12: status=DONE, has_results=True
  exp_026_t12_scierc: status=DONE, has_results=False
  exp_026_t12_seed123: status=DONE, has_results=True
  exp_026_t12_seed456: status=DONE, has_results=True
  exp_027_fewnerd_n16: status=DONE, has_results=True
  exp_027_mlp_verifier: status=DONE, has_results=True
  exp_028: status=DONE, has_results=True
  exp_028_entity_token_lp: status=DONE, has_results=True
  exp_028_fewnerd_5epoch: status=DONE, has_results=True
  exp_029a: status=DONE, has_results=True
  exp_029b: status=DONE, has_results=True
  exp_030_conll_t12: status=DONE, has_results=False
  exp_031_fewnerd_t12: status=DONE, has_results=False
  exp_a2_degen_regression: status=PREPARING, has_results=True
  exp_adaptive_sampling_budget: status=PREPARING, has_results=True
  exp_adaptive_temperature: status=DONE, has_results=False
  exp_b2_entity_verifier: status=PREPARING, has_results=True
  exp_ccs_selection: status=DONE, has_results=False
  exp_cross_model_consistency: status=PREPARING, has_results=True
  exp_dgec_heterogeneous_t: status=PREPARING, has_results=True
  exp_dgec_sj_construction: status=PREPARING, has_results=True
  exp_dgec_vc_construction: status=PREPARING, has_results=True
  exp_diagnostic_calibration: status=DONE, has_results=False
  exp_e1_signal_routing: status=PREPARING, has_results=True
  exp_entity_consensus: status=DONE, has_results=False
  exp_entity_construction: status=DONE, has_results=True
  exp_entity_token_lp: status=DONE, has_results=True
  exp_epoch_dgs_analysis: status=DONE, has_results=False
  exp_fewnerd_s789_n8: status=DONE, has_results=True
  exp_freeform_ablation: status=DONE, has_results=True
  exp_freeform_conll_4seed: status=DONE, has_results=True
  exp_freeform_seed123: status=DONE, has_results=True
  exp_freeform_seed456: status=DONE, has_results=True
  exp_freeform_seed789: status=DONE, has_results=True
  exp_freeform_seed789_v2: status=DONE, has_results=False
  exp_freeform_seed789_v3: status=DONE, has_results=True
  exp_llama3b_scierc_ablation: status=DONE, has_results=True
  exp_llama_fewnerd_inference: status=DONE, has_results=True
  exp_llama_fewnerd_lora: status=DONE, has_results=True
  exp_llama_scierc_seed456: status=DONE, has_results=True
  exp_lp_alignment_gating: status=DONE, has_results=True
  exp_lp_scierc_t07: status=DONE, has_results=True
  exp_lp_t07_scierc: status=DONE, has_results=False
  exp_pareto_diversity_quality: status=PREPARING, has_results=True
  exp_qwen25_14b_fewnerd: status=RUNNING, has_results=True
  exp_qwen25_32b_fewnerd: status=RUNNING, has_results=True
  exp_qwen25_72b_fewshot: status=DONE, has_results=True
  exp_qwen25_72b_zeroshot: status=DONE, has_results=True
  exp_qwen25_7b_fewnerd: status=DONE, has_results=True
  exp_qwen3_4b_conll_finetune: status=DONE, has_results=True
  exp_qwen3_4b_conll_finetune_resume: status=DONE, has_results=True
  exp_qwen3_4b_conll_merge_inference_v2: status=DONE, has_results=False
  exp_qwen3_4b_conll_scs_inference: status=DONE, has_results=True
  exp_qwen3_4b_conll_scs_inference_v2: status=DONE, has_results=True
  exp_qwen3_4b_scierc_finetune: status=DONE, has_results=False
  exp_qwen3_4b_scierc_finetune_v2: status=DONE, has_results=False
  exp_qwen3_4b_scierc_finetune_v3: status=DONE, has_results=False
  exp_qwen3_4b_scierc_finetune_v4: status=DONE, has_results=True
  exp_qwen3_4b_scierc_merge_inference: status=DONE, has_results=False
  exp_qwen3_4b_scierc_scs_inference: status=DONE, has_results=True
  exp_re_scierc_seed123: status=DONE, has_results=True
  exp_re_scierc_seed456: status=DONE, has_results=True
  exp_selective_prediction: status=DONE, has_results=True
  exp_tacred_re_benchmark: status=DONE, has_results=False
  exp_vc_lp_cascade_selection: status=DONE, has_results=False
  exp_vc_quartile_analysis: status=DONE, has_results=True
  exp_verbalized_confidence: status=DONE, has_results=True
  exp_wnut17_qwen25_7b: status=DONE, has_results=True
  ft_001: status=DONE, has_results=True
  ft_002: status=DONE, has_results=True
  ft_002_v2: status=DONE, has_results=True
  hidden_state_probe_conll_full: status=DONE, has_results=False
  hidden_state_probe_conll_v2: status=DONE, has_results=False
  mbr_pilot: status=DONE, has_results=False
  mvp_pilot_001: status=DONE, has_results=True
  mvp_pilot_002: status=DONE, has_results=False
  mvp_pilot_003: status=DONE, has_results=True
  mvp_pilot_004: status=DONE, has_results=True
  mvp_pilot_005: status=DONE, has_results=True
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0271b53b-66a3-4f1b-b015-b7897319211b",
  "isSidechain": true,
  "promptId": "9d5a8dbf-14d3-41c1-a18a-ef8acd67e6cb",
  "agentId": "a97ebe3840b34757a",
  "type": "user",
  "uuid": "81f6cda9-869b-4bc2-ba2f-31700abc4360",
  "sourceToolAssistantUUID": "0271b53b-66a3-4f1b-b015-b7897319211b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T10:44:22.915Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PX8nuqrdBVGq9ZY7s1jwRd`</summary>

```json
{
  "command": "cat \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/c7ddc740-cffe-49a2-afe7-879cf8dde3ec/tool-results/mcp-agent-ml-research-read_registry-1779273820823.txt\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexperiments = inner['data']['experiments']\n\n# Print ALL experiments with full details\nfor eid in sorted(experiments.keys()):\n    e = experiments[eid]\n    print(f'=== {eid} ===')\n    print(f'status: {e.get(\\\"status\\\", \\\"?\\\")}')\n    print(f'hypothesis: {e.get(\\\"hypothesis\\\", \\\"\\\")}')\n    print(f'conclusion: {e.get(\\\"conclusion\\\", \\\"\\\")}')\n    # Print all fields except large nested ones\n    for k, v in e.items():\n        if k not in ['hypothesis', 'conclusion', 'status']:\n            print(f'{k}: {json.dumps(v, ensure_ascii=False)}')\n    print()\n\" 2>&1 | head -3000",
  "description": "Extract all experiment details including all fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81f6cda9-869b-4bc2-ba2f-31700abc4360",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
  "requestId": "req_011CbDgcikHLJSRcVxY9dR73",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca97555e-6a6c-4601-a66c-19401fb22dae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KLHZ5uKGhAti1kwyTNe1Te",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4466,
      "cache_read_input_tokens": 25686,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4466
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 409,
          "cache_read_input_tokens": 25686,
          "cache_creation_input_tokens": 4466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4466,
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

_source line 9 · 2026-05-20T10:44:23.012Z_

<details><summary>↩ Tool result · `toolu_01PX8nuqrdBVGq9ZY7s1jwRd`</summary>

```text
&lt;persisted-output>
Output too large (131.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/c7ddc740-cffe-49a2-afe7-879cf8dde3ec/tool-results/btkndpqic.txt

Preview (first 2KB):
=== dgs_pilot ===
status: DONE
hypothesis: Degeneracy-Gated Selection (DGS) validates Two-Condition Theory: using degeneracy rate as gating mechanism to switch between greedy (degenerate) and LP selection (non-degenerate), the improvement direction should follow a monotonic gradient — low degeneracy yields positive delta, high degeneracy yields negative delta.
conclusion: killed
created_at: "2026-05-18T17:56:04.572Z"
updated_at: "2026-05-19T00:29:37.275Z"
notes: "D154: DGS demoted to explored heuristic, cross-model direction contradiction (D152)"

=== e1_component_wise_re_sj ===
status: DONE
hypothesis: 
conclusion: negative
created_at: "2026-05-14T09:15:17.262Z"
updated_at: "2026-05-14T09:23:38.818Z"
metrics: {"full_head_sj_rho": 0.21, "full_tail_sj_rho": 0.201, "full_type_match_rho": 0.201, "full_multiplicative_rho": 0.244, "full_additive_rho": 0.243, "full_fleiss_kappa_rho": 0.278, "cond_head_sj_rho": 0.27, "cond_tail_sj_rho": 0.259, "cond_type_match_rho": 0.252, "cond_multiplicative_rho": 0.316, "cond_additive_rho": 0.306, "cond_fleiss_kappa_rho": 0.307, "n_full": 397, "n_conditional": 313, "diagnosis": "head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE."}

=== exp001_seed123 ===
status: DONE
hypothesis: 
conclusion: killed
created_at: "2026-05-14T12:09:45.739Z"
updated_at: "2026-05-15T12:41:31.168Z"

=== exp001_seed456 ===
status: DONE
hypothesis: 
conclusion: killed
created_at: "2026-05-14T12:09:48.078Z"
updated_at: "2026-05-15T12:41:32.192Z"

=== exp008_re_n16 ===
status: DONE
hypothesis: 
conclusion: killed
created_at: "2026-05-14T12:09:50.987Z"
updated_at: "2026-05-15T12:41:39.774Z"

=== exp_001_n16_seed123 ===
status: DONE
hypothesis: 
conclusion: success
created_at: "2026-05-14T12:10:29.393Z"
updated_at: "2026-05-14T12:42:58.393Z"
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca97555e-6a6c-4601-a66c-19401fb22dae",
  "isSidechain": true,
  "promptId": "9d5a8dbf-14d3-41c1-a18a-ef8acd67e6cb",
  "agentId": "a97ebe3840b34757a",
  "type": "user",
  "uuid": "5e8a413e-c0a6-4911-bda8-92b7ce06d63e",
  "sourceToolAssistantUUID": "ca97555e-6a6c-4601-a66c-19401fb22dae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T10:44:29.715Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011tJaJHWrLnyDUzhJQPdCP7`</summary>

```json
{
  "command": "cat \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/c7ddc740-cffe-49a2-afe7-879cf8dde3ec/tool-results/mcp-agent-ml-research-read_registry-1779273820823.txt\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexperiments = inner['data']['experiments']\n\n# Print ALL experiments with full details\nfor eid in sorted(experiments.keys()):\n    e = experiments[eid]\n    print(f'=== {eid} ===')\n    print(f'status: {e.get(\\\"status\\\", \\\"?\\\")}')\n    print(f'hypothesis: {e.get(\\\"hypothesis\\\", \\\"\\\")}')\n    print(f'conclusion: {e.get(\\\"conclusion\\\", \\\"\\\")}')\n    # Print all fields except large nested ones\n    for k, v in e.items():\n        if k not in ['hypothesis', 'conclusion', 'status']:\n            print(f'{k}: {json.dumps(v, ensure_ascii=False)}')\n    print()\n\" > /tmp/registry_full.txt 2>&1\nwc -l /tmp/registry_full.txt\nhead -50 /tmp/registry_full.txt",
  "description": "Save all experiment details to temp file and check line count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e8a413e-c0a6-4911-bda8-92b7ce06d63e",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
  "requestId": "req_011CbDgdT21DvwDWNm1XcQDb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d178e1e5-4643-467c-8e33-861987dad329",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FcMrUg7gCUtokvSZ3Pmkut",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1331,
      "cache_read_input_tokens": 30152,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1331
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 442,
          "cache_read_input_tokens": 30152,
          "cache_creation_input_tokens": 1331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1331,
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

_source line 11 · 2026-05-20T10:44:29.814Z_

<details><summary>↩ Tool result · `toolu_011tJaJHWrLnyDUzhJQPdCP7`</summary>

```text
1454 /tmp/registry_full.txt
=== dgs_pilot ===
status: DONE
hypothesis: Degeneracy-Gated Selection (DGS) validates Two-Condition Theory: using degeneracy rate as gating mechanism to switch between greedy (degenerate) and LP selection (non-degenerate), the improvement direction should follow a monotonic gradient — low degeneracy yields positive delta, high degeneracy yields negative delta.
conclusion: killed
created_at: "2026-05-18T17:56:04.572Z"
updated_at: "2026-05-19T00:29:37.275Z"
notes: "D154: DGS demoted to explored heuristic, cross-model direction contradiction (D152)"

=== e1_component_wise_re_sj ===
status: DONE
hypothesis: 
conclusion: negative
created_at: "2026-05-14T09:15:17.262Z"
updated_at: "2026-05-14T09:23:38.818Z"
metrics: {"full_head_sj_rho": 0.21, "full_tail_sj_rho": 0.201, "full_type_match_rho": 0.201, "full_multiplicative_rho": 0.244, "full_additive_rho": 0.243, "full_fleiss_kappa_rho": 0.278, "cond_head_sj_rho": 0.27, "cond_tail_sj_rho": 0.259, "cond_type_match_rho": 0.252, "cond_multiplicative_rho": 0.316, "cond_additive_rho": 0.306, "cond_fleiss_kappa_rho": 0.307, "n_full": 397, "n_conditional": 313, "diagnosis": "head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE."}

=== exp001_seed123 ===
status: DONE
hypothesis: 
conclusion: killed
created_at: "2026-05-14T12:09:45.739Z"
updated_at: "2026-05-15T12:41:31.168Z"

=== exp001_seed456 ===
status: DONE
hypothesis: 
conclusion: killed
created_at: "2026-05-14T12:09:48.078Z"
updated_at: "2026-05-15T12:41:32.192Z"

=== exp008_re_n16 ===
status: DONE
hypothesis: 
conclusion: killed
created_at: "2026-05-14T12:09:50.987Z"
updated_at: "2026-05-15T12:41:39.774Z"

=== exp_001_n16_seed123 ===
status: DONE
hypothesis: 
conclusion: success
created_at: "2026-05-14T12:10:29.393Z"
updated_at: "2026-05-14T12:42:58.393Z"
metrics: {"ner": {"greedy_f1": 0.655, "oracle_f1": 0.8028, "headroom": 0.1478, "rho_sj_full": 0.4076, "rho_fk_full": 0.2799, "rho_logprob_full": 0.3189, "rho_sj_cond": 0.4271, "rho_fk_cond": 0.2743, "rho_logprob_cond": 0.2835, "sj_beats_fk": true, "rho_advantage": 0.1277}, "re": {"greedy_f1": 0.4243, "oracle_f1": 0.6771, "headroom": 0.2528, "rho_sj_full": 0.2943, "rho_fk_full": 0.2657, "rho_logprob_full": 0.3005, "rho_sj_cond": 0.4003, "rho_fk_cond": 0.313, "rho_logprob_cond": 0.2317, "sj_beats_fk": true, "rho_advantage": 0.0286}, "verdict": "FAIL"}

=== exp_001_n16_seed123_full ===
status: DONE
hypothesis: 
conclusion: killed
created_at: "2026-05-14T12:43:47.915Z"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d178e1e5-4643-467c-8e33-861987dad329",
  "isSidechain": true,
  "promptId": "9d5a8dbf-14d3-41c1-a18a-ef8acd67e6cb",
  "agentId": "a97ebe3840b34757a",
  "type": "user",
  "uuid": "39f24991-498b-46be-9965-725c02b20516",
  "sourceToolAssistantUUID": "d178e1e5-4643-467c-8e33-861987dad329",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T10:44:31.609Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ETwfwxu6W24wGfK5JmYtu1`</summary>

```json
{
  "file_path": "/tmp/registry_full.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39f24991-498b-46be-9965-725c02b20516",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
  "requestId": "req_011CbDgdx9hxH5FQJUEdfMxL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17be9ab7-8e90-41c3-8b6f-792da8a47f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0145b6siZAfb23upDBxYNfNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1617,
      "cache_read_input_tokens": 31483,
      "output_tokens": 60,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1617
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 60,
          "cache_read_input_tokens": 31483,
          "cache_creation_input_tokens": 1617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1617,
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

_source line 13 · 2026-05-20T10:44:31.859Z_

<details><summary>↩ Tool result · reported error · `toolu_01ETwfwxu6W24wGfK5JmYtu1`</summary>

```text
File content (60503 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17be9ab7-8e90-41c3-8b6f-792da8a47f81",
  "isSidechain": true,
  "promptId": "9d5a8dbf-14d3-41c1-a18a-ef8acd67e6cb",
  "agentId": "a97ebe3840b34757a",
  "type": "user",
  "uuid": "589338f2-2e83-4956-ae55-88288a5cc0c0",
  "toolUseResult": "Error: File content (60503 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "17be9ab7-8e90-41c3-8b6f-792da8a47f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T10:44:34.169Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H4yeXuq63zJqugriy8bg6b`</summary>

```json
{
  "file_path": "/tmp/registry_full.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "589338f2-2e83-4956-ae55-88288a5cc0c0",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
  "requestId": "req_011CbDge6rLYLNm6Lin4rpSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7fa2030-545a-4b96-a1ab-b02b0fdac9c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SjB4V4z17Y4kK8JqPjfJbA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 33100,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 33100,
          "cache_creation_input_tokens": 121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 121,
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

_source line 15 · 2026-05-20T10:44:34.439Z_

<details><summary>↩ Tool result · `toolu_01H4yeXuq63zJqugriy8bg6b`</summary>

```text
1	=== dgs_pilot ===
2	status: DONE
3	hypothesis: Degeneracy-Gated Selection (DGS) validates Two-Condition Theory: using degeneracy rate as gating mechanism to switch between greedy (degenerate) and LP selection (non-degenerate), the improvement direction should follow a monotonic gradient — low degeneracy yields positive delta, high degeneracy yields negative delta.
4	conclusion: killed
5	created_at: "2026-05-18T17:56:04.572Z"
6	updated_at: "2026-05-19T00:29:37.275Z"
7	notes: "D154: DGS demoted to explored heuristic, cross-model direction contradiction (D152)"
8	
9	=== e1_component_wise_re_sj ===
10	status: DONE
11	hypothesis: 
12	conclusion: negative
13	created_at: "2026-05-14T09:15:17.262Z"
14	updated_at: "2026-05-14T09:23:38.818Z"
15	metrics: {"full_head_sj_rho": 0.21, "full_tail_sj_rho": 0.201, "full_type_match_rho": 0.201, "full_multiplicative_rho": 0.244, "full_additive_rho": 0.243, "full_fleiss_kappa_rho": 0.278, "cond_head_sj_rho": 0.27, "cond_tail_sj_rho": 0.259, "cond_type_match_rho": 0.252, "cond_multiplicative_rho": 0.316, "cond_additive_rho": 0.306, "cond_fleiss_kappa_rho": 0.307, "n_full": 397, "n_conditional": 313, "diagnosis": "head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE."}
16	
17	=== exp001_seed123 ===
18	status: DONE
19	hypothesis: 
20	conclusion: killed
21	created_at: "2026-05-14T12:09:45.739Z"
22	updated_at: "2026-05-15T12:41:31.168Z"
23	
24	=== exp001_seed456 ===
25	status: DONE
26	hypothesis: 
27	conclusion: killed
28	created_at: "2026-05-14T12:09:48.078Z"
29	updated_at: "2026-05-15T12:41:32.192Z"
30	
31	=== exp008_re_n16 ===
32	status: DONE
33	hypothesis: 
34	conclusion: killed
35	created_at: "2026-05-14T12:09:50.987Z"
36	updated_at: "2026-05-15T12:41:39.774Z"
37	
38	=== exp_001_n16_seed123 ===
39	status: DONE
40	hypothesis: 
41	conclusion: success
42	created_at: "2026-05-14T12:10:29.393Z"
43	updated_at: "2026-05-14T12:42:58.393Z"
44	metrics: {"ner": {"greedy_f1": 0.655, "oracle_f1": 0.8028, "headroom": 0.1478, "rho_sj_full": 0.4076, "rho_fk_full": 0.2799, "rho_logprob_full": 0.3189, "rho_sj_cond": 0.4271, "rho_fk_cond": 0.2743, "rho_logprob_cond": 0.2835, "sj_beats_fk": true, "rho_advantage": 0.1277}, "re": {"greedy_f1": 0.4243, "oracle_f1": 0.6771, "headroom": 0.2528, "rho_sj_full": 0.2943, "rho_fk_full": 0.2657, "rho_logprob_full": 0.3005, "rho_sj_cond": 0.4003, "rho_fk_cond": 0.313, "rho_logprob_cond": 0.2317, "sj_beats_fk": true, "rho_advantage": 0.0286}, "verdict": "FAIL"}
45	
46	=== exp_001_n16_seed123_full ===
47	status: DONE
48	hypothesis: 
49	conclusion: killed
50	created_at: "2026-05-14T12:43:47.915Z"
51	updated_at: "2026-05-15T12:41:29.068Z"
52	
53	=== exp_001_n16_seed456 ===
54	status: DONE
55	hypothesis: SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count. Establishes seed stability for SJ/FK/VC/EM ordering.
56	conclusion: success
57	created_at: "2026-05-14T12:10:30.350Z"
58	updated_at: "2026-05-17T02:56:53.526Z"
59	metrics: {"instance_count": 551, "n_valid": 529, "n_gold_empty": 22, "parse_rate": 1, "ner_greedy_f1": 0.6617, "ner_oracle_f1": 0.8075, "re_greedy_f1": 0.4215, "re_oracle_f1": 0.4748, "rho_sj_ner": 0.4098, "rho_fk_ner": 0.2723, "rho_vc_ner": 0.4449, "rho_em_ner": 0.3363, "rho_lp_ner": 0.2415, "rho_sj_re": 0.2835, "rho_fk_re": 0.2929, "auroc_sj_ner": 0.6823, "auroc_fk_ner": 0.6179, "auroc_vc_ner": 0.6981, "auroc_em_ner": 0.649, "auroc_lp_ner": 0.5885, "rho_note": "CORRECTED 2026-05-15: old values (rho_fk=0.3448,rho_sj=0.4134) included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529)."}
60	
61	=== exp_001_n16_seed456_full ===
62	status: DONE
63	hypothesis: 
64	conclusion: killed
65	created_at: "2026-05-14T12:44:31.348Z"
66	updated_at: "2026-05-15T12:41:30.065Z"
67	
68	=== exp_001_ner_n16_scierc ===
69	status: DONE
70	hypothesis: 
71	conclusion: success
72	created_at: "2026-05-14T11:42:10.898Z"
73	updated_at: "2026-05-14T12:42:49.592Z"
74	metrics: {"n_instances": 551, "ner_n": 529, "re_n": 397, "N": 16, "T": 1, "seed": 42, "full_test_set": true, "ner_voting_conf_rho": 0.399, "ner_sj_rho": 0.398, "ner_em_rho": 0.339, "ner_fk_rho": 0.288, "ner_logprob_rho": 0.237, "ner_voting_conf_auroc": 0.704, "ner_sj_auroc": 0.697, "ner_cond_em_rho": 0.414, "ner_cond_sj_rho": 0.349, "ner_cond_vc_rho": 0.34, "re_voting_conf_rho": 0.38, "re_logprob_rho": 0.293, "re_fk_rho": 0.281, "re_sj_rho": 0.277, "re_em_rho": 0.148, "re_voting_conf_auroc": 0.699, "re_cond_em_rho": 0.475, "re_cond_sj_rho": 0.318, "re_cond_vc_rho": 0.35, "re_cond_em_auroc": 0.742, "diagnosis": "551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling 'breakthrough' was artifact of 200 instances + T=0.7."}
75	
76	=== exp_001_ner_n16_seed123 ===
77	status: DONE
78	hypothesis: SciERC NER N=16 seed=123: multi-seed validation at N=16. Tests seed stability for signal rankings with more samples.
79	conclusion: success
80	created_at: "2026-05-14T12:46:06.430Z"
81	updated_at: "2026-05-17T02:58:18.225Z"
82	metrics: {"ner": {"greedy_f1": 0.663, "oracle_f1": 0.809, "headroom": 0.146, "rho_sj": 0.423, "rho_fk": 0.29, "rho_logprob": 0.239, "rho_sj_cond": 0.423, "rho_fk_cond": 0.26}, "re": {"greedy_f1": 0.419, "oracle_f1": 0.625, "headroom": 0.206, "rho_sj": 0.267, "rho_fk": 0.315, "rho_sj_cond": 0.364, "rho_fk_cond": 0.331}, "verdict": "FAIL", "verdict_note": "RE rho_sj=0.267 < 0.40; RE >30% samples F1=0", "n_instances": 551, "seed": 123, "N": 16, "T": 1}
83	
84	=== exp_001_seed123_t10_full ===
85	status: DONE
86	hypothesis: SciERC NER seed=123 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.
87	conclusion: negative
88	created_at: "2026-05-14T13:27:42.503Z"
89	updated_at: "2026-05-17T02:58:11.623Z"
90	metrics: {"ner": {"rho_sj": 0.417, "rho_fk": 0.283}, "re": {"rho_sj": 0.265, "rho_fk": 0.315}, "n_instances": 551, "N": 16, "T": 1, "seed": 123, "source": "reviewer_verified_report_json"}
91	
92	=== exp_001_seed123_v2 ===
93	status: DONE
94	hypothesis: SciERC NER seed=123 v2: second seed for multi-seed validation. Establishes reproducibility of structural>surface signal ranking across random seeds.
95	conclusion: success
96	created_at: "2026-05-14T14:34:04.210Z"
97	updated_at: "2026-05-17T02:57:42.106Z"
98	metrics: {"sj_rho_full": 0.424, "sj_rho_cond": 0.376, "structural_minus_surface": 0.149, "conclusion_note": "NER seed123 robustness confirmed, structural>surface +0.149"}
99	
100	=== exp_001_seed123_v2_r1024 ===
101	status: DONE
102	hypothesis: 
103	conclusion: killed
104	created_at: "2026-05-14T22:16:54.442Z"
105	updated_at: "2026-05-15T01:20:49.812Z"
106	
107	=== exp_001_seed42_v2 ===
108	status: DONE
109	hypothesis: SciERC NER seed=42 v2: primary seed baseline under corrected pipeline. Establishes canonical signal rankings (SJ>FK>LP) for NER with gold-filtering.
110	conclusion: success
111	created_at: "2026-05-14T14:34:02.350Z"
112	updated_at: "2026-05-17T02:57:57.324Z"
113	metrics: {"sj_rho_full": 0.428, "sj_rho_cond": 0.369, "structural_minus_surface": 0.147, "conclusion_note": "NER seed42 robustness confirmed, structural>surface +0.147"}
114	
115	=== exp_001_seed42_v2_r1024 ===
116	status: DONE
117	hypothesis: 
118	conclusion: killed
119	created_at: "2026-05-14T22:16:52.571Z"
120	updated_at: "2026-05-14T22:28:53.686Z"
121	metrics: {"greedy_f1": 0.6647, "oracle_f1": 0.8106, "softjaccard_rho_full": 0.3928, "fleiss_rho_full": 0.2489, "logprob_rho_full": 0.2136, "softjaccard_rho_cond": 0.3455, "fleiss_rho_cond": 0.163, "logprob_rho_cond": 0.1624, "verdict": "MARGINAL"}
122	
123	=== exp_001_seed456_t10_full ===
124	status: DONE
125	hypothesis: SciERC NER seed=456 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.
126	conclusion: negative
127	created_at: "2026-05-14T13:27:41.067Z"
128	updated_at: "2026-05-17T02:58:12.996Z"
129	metrics: {"ner": {"rho_sj": 0.414, "rho_fk": 0.298}, "re": {"rho_sj": 0.268, "rho_fk": 0.26}, "n_instances": 551, "N": 16, "T": 1, "seed": 456, "source": "reviewer_verified_report_json"}
130	
131	=== exp_001_seed456_v2 ===
132	status: DONE
133	hypothesis: SciERC joint NER+RE seed=456 v2: early pipeline version. Tests multi-seed stability of signal rankings on joint extraction task.
134	conclusion: negative
135	created_at: "2026-05-14T15:38:55.569Z"
136	updated_at: "2026-05-17T02:57:23.336Z"
137	
138	=== exp_001_seed456_v2_ner ===
139	status: DONE
140	hypothesis: SciERC NER seed=456 v2: corrected pipeline rerun with gold-filtering. Part of multi-seed validation protocol for NER signal ranking stability.
141	conclusion: success
142	created_at: "2026-05-14T17:13:00.414Z"
143	updated_at: "2026-05-17T02:57:18.227Z"
144	metrics: {"full": {"SJ": {"rho": 0.384, "auroc": 0.711}, "FK": {"rho": 0.223, "auroc": 0.577}, "logprob": {"rho": 0.232, "auroc": 0.594}, "EM": {"rho": 0.316, "auroc": 0.768}, "voting_conf": {"rho": 0.411, "auroc": 0.712}}, "conditional": {"SJ": {"rho": 0.349, "auroc": 0.699}, "FK": {"rho": 0.157, "auroc": 0.561}, "logprob": {"rho": 0.171, "auroc": 0.576}, "EM": {"rho": 0.406, "auroc": 0.78}, "voting_conf": {"rho": 0.346, "auroc": 0.694}}, "3seed_mean_SJ_rho_full": 0.412, "3seed_sd_SJ_rho_full": 0.025, "structural_beats_surface": true, "verdict": "MARGINAL"}
145	
146	=== exp_001_seed456_v2_ner_r1024 ===
147	status: DONE
148	hypothesis: 
149	conclusion: killed
150	created_at: "2026-05-14T22:16:55.975Z"
151	updated_at: "2026-05-15T01:20:48.914Z"
152	
153	=== exp_002 ===
154	status: DONE
155	hypothesis: 
156	conclusion: success
157	created_at: "2026-05-14T12:39:53.226Z"
158	updated_at: "2026-05-14T12:40:17.202Z"
159	metrics: {"sj_rho_full": 0.4357, "sj_tau_full": 0.3851, "sj_auroc_full": 0.8008, "sj_rho_cond": 0.4511, "fk_rho_full": 0.3998, "fk_tau_full": 0.3568, "fk_auroc_full": 0.7741, "fk_rho_cond": 0.4064, "logprob_rho_full": 0.3157, "logprob_tau_full": 0.2469, "logprob_auroc_full": 0.7532, "logprob_rho_cond": 0.3562, "em_rho_full": 0.4507, "em_tau_full": 0.4002, "em_auroc_full": 0.8156, "em_rho_cond": 0.4799, "ev_rho_full": 0.4237, "ev_tau_full": 0.3777, "ev_auroc_full": 0.7889, "ev_rho_cond": 0.4127, "greedy_f1": 0.9123, "oracle_f1": 0.9543, "voting_f1": 0.9141, "oracle_headroom": 0.042, "sj_vs_logprob_delta_rho": 0.12, "sj_vs_logprob_ci_low": 0.0881, "sj_vs_logprob_ci_high": 0.154, "sj_vs_logprob_significant": true, "n_instances": 3453, "n_valid": 2756, "n_samples": 8, "temperature": 1}
160	
161	=== exp_002_conll_n16 ===
162	status: DONE
163	hypothesis: CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9).
164	conclusion: success
165	created_at: "2026-05-14T18:12:16.041Z"
166	updated_at: "2026-05-18T20:49:50.398Z"
167	metrics: {"degen_rate": 0.4844, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "N": 16, "dataset": "conll2003", "subtask": "ner", "n_instances": 3453, "n_valid": 2756, "n_conditional": 2614, "greedy_f1": 0.907, "full": {"SJ_rho": 0.4496, "FK_rho": 0.3928, "logprob_rho": 0.3146, "EM_rho": 0.4627, "voting_conf_rho": 0.4286, "SJ_AUROC": 0.8264, "FK_AUROC": 0.7821, "logprob_AUROC": 0.7531, "EM_AUROC": 0.8409, "voting_conf_AUROC": 0.8071, "SJ_ECE": 0.0747, "FK_ECE": 0.1786, "logprob_ECE": 0.2031, "EM_ECE": 0.0786, "voting_conf_ECE": 0.529}, "conditional": {"SJ_rho": 0.4208, "FK_rho": 0.3494, "logprob_rho": 0.3756, "EM_rho": 0.4658, "voting_conf_rho": 0.3654, "SJ_AUROC": 0.8405, "FK_AUROC": 0.7819, "logprob_AUROC": 0.8259, "EM_AUROC": 0.8781, "voting_conf_AUROC": 0.7951, "SJ_ECE": 0.0982, "FK_ECE": 0.1899, "logprob_ECE": 0.2504, "EM_ECE": 0.0997, "voting_conf_ECE": 0.6096}, "n8_vs_n16_delta_rho_full": {"SJ": 0.0139, "FK": -0.007, "logprob": -0.0011, "EM": 0.012, "voting_conf": 0.0049}}
168	
169	=== exp_002_conll_n16_r1024 ===
170	status: DONE
171	hypothesis: 
172	conclusion: killed
173	created_at: "2026-05-14T22:16:57.682Z"
174	updated_at: "2026-05-15T01:20:53.108Z"
175	
176	=== exp_002_conll_n16_seed123 ===
177	status: DONE
178	hypothesis: Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.
179	conclusion: success
180	created_at: "2026-05-18T22:03:14.343Z"
181	updated_at: "2026-05-18T22:04:45.039Z"
182	metrics: {"degen_rate": 0.471, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "instance_count": 3453, "n_valid": 2756, "n_gold_empty": 697, "ner_greedy_f1": 0.9068, "ner_oracle_f1": 0.9633, "rho_fk_ner": 0.4524, "rho_sj_ner": 0.4621, "sample_f1_pct_zero": 7.54}
183	
184	=== exp_002_conll_n16_seed456 ===
185	status: DONE
186	hypothesis: Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.
187	conclusion: success
188	created_at: "2026-05-18T22:03:15.720Z"
189	updated_at: "2026-05-18T22:04:46.954Z"
190	metrics: {"degen_rate": 0.5544, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "instance_count": 3453, "n_valid": 2756, "n_gold_empty": 697, "ner_greedy_f1": 0.9074, "ner_oracle_f1": 0.9549, "rho_fk_ner": 0.4718, "rho_sj_ner": 0.4819, "sample_f1_pct_zero": 7.02}
191	
192	=== exp_002_merge_conll2003 ===
193	status: DONE
194	hypothesis: 
195	conclusion: killed
196	created_at: "2026-05-14T12:25:56.211Z"
197	updated_at: "2026-05-15T12:41:26.419Z"
198	notes: "Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected."
199	
200	=== exp_002_ner_conll2003 ===
201	status: DONE
202	hypothesis: 
203	conclusion: success
204	created_at: "2026-05-14T11:42:15.223Z"
205	updated_at: "2026-05-14T12:27:35.413Z"
206	
207	=== exp_003_ner_wnut17 ===
208	status: DONE
209	hypothesis: WNUT-17 NER fine-tune + inference: initial attempt on social media domain. Tests if structural signals work when model capability is low on noisy text with novel entity types.
210	conclusion: negative
211	created_at: "2026-05-14T11:42:17.544Z"
212	updated_at: "2026-05-17T02:58:14.928Z"
213	metrics: {"ner": {"greedy_f1": 0.525, "oracle_f1": 0.664, "headroom": 0.139, "rho_sj_full": 0.082, "rho_fk_full": 0.124, "rho_logprob_full": -0.414, "rho_sj_cond": 0.275, "rho_fk_cond": 0.164, "rho_logprob_cond": 0.352, "sj_beats_logprob_cond": false}, "n_instances": 1287, "n_gold_empty": 598, "sample_f1_mean": 0.401, "sample_f1_pct_zero": 53.7, "N": 16, "T": 1, "seed": 42, "verdict": "FAIL", "verdict_note": ">30% samples F1=0; structural rho weak; logprob baseline stronger"}
214	
215	=== exp_003_wnut17_eval ===
216	status: DONE
217	hypothesis: WNUT-17 NER evaluation: initial test on noisy social media domain. Tests boundary conditions for structural signal effectiveness on out-of-domain text.
218	conclusion: success
219	created_at: "2026-05-14T13:47:34.654Z"
220	updated_at: "2026-05-17T02:58:01.627Z"
221	metrics: {"greedy_f1": 0.523, "oracle_f1": 0.664, "headroom": 0.141, "rho_fk": 0.125, "rho_sj": 0.089, "rho_fk_cond": 0.169, "rho_sj_cond": 0.288, "rho_logprob_full": -0.409, "rho_logprob_cond": 0.35, "structural_beats_surface": false, "sample_f1_pct_zero": 53.7, "n_instances": 1287, "N": 16, "T": 1, "seed": 42, "model": "Qwen3-8B", "n_gold_empty_filtered": 598, "verdict": "FAIL", "verdict_note": "structural_beats_surface=false; >50% samples F1=0"}
222	
223	=== exp_003_wnut17_v2 ===
224	status: DONE
225	hypothesis: WNUT-17 NER evaluation v2: tests signal effectiveness on noisy social media text. Hypothesis: structural signals remain effective on noisy, informal text with high entity variation.
226	conclusion: negative
227	created_at: "2026-05-14T15:32:56.415Z"
228	updated_at: "2026-05-17T02:57:20.068Z"
229	
230	=== exp_004_re_diagnostic ===
231	status: DONE
232	hypothesis: 
233	conclusion: success
234	created_at: "2026-05-14T11:49:44.497Z"
235	updated_at: "2026-05-14T11:50:24.620Z"
236	metrics: {"per_relation_type": {"HYPONYM-OF": {"n": 36, "rho_sj": 0.545, "rho_fk": 0.646, "rho_vc": 0.628, "mean_f1": 0.513}, "CONJUNCTION": {"n": 86, "rho_sj": 0.383, "rho_fk": 0.35, "rho_vc": 0.484, "mean_f1": 0.48}, "USED-FOR": {"n": 299, "rho_sj": 0.236, "rho_fk": 0.255, "rho_vc": 0.286, "mean_f1": 0.422}, "PART-OF": {"n": 44, "rho_sj": 0.239, "rho_fk": 0.348, "rho_vc": 0.283, "mean_f1": 0.297}, "EVALUATE-FOR": {"n": 62, "rho_sj": 0.172, "rho_fk": 0.255, "rho_vc": 0.226, "mean_f1": 0.365}, "COMPARE": {"n": 35, "rho_sj": 0.168, "rho_fk": 0.184, "rho_vc": 0.18, "mean_f1": 0.453}, "FEATURE-OF": {"n": 50, "rho_sj": 0.004, "rho_fk": 0.052, "rho_vc": 0.014, "mean_f1": 0.254}}, "error_propagation": {"total_fn": 553, "tail_error_pct": 21.9, "full_error_pct": 21.7, "head_error_pct": 17.7, "head_tail_error_pct": 15.9, "type_error_pct": 8.3, "worst_consistency": "head_type_error (sj=0.411)", "best_consistency": "head_error (sj=0.613)"}, "threshold_sensitivity": {"thr_0.00_rho_sj": 0.3161, "thr_0.00_rho_vc": 0.3841, "thr_0.00_n": 313, "thr_0.05_rho_sj": 0.2682, "thr_0.05_rho_vc": 0.2364, "thr_0.05_n": 239}, "bootstrap_ci_95": {"ner_sj": [0.2946, 0.4586], "ner_voting_conf": [0.3048, 0.4656], "re_sj": [0.1422, 0.3391], "re_voting_conf": [0.1818, 0.3721], "re_cond_sj": [0.2161, 0.4102], "re_cond_voting_conf": [0.2825, 0.474]}, "fisher_z_ner_vs_re": {"sj_z": 2.31, "sj_p": 0.0209, "sj_significant": true, "fk_z": -0.31, "fk_p": 0.756, "fk_significant": false, "voting_z": 1.914, "voting_p": 0.0556, "voting_significant": false}, "diagnosis": "FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE signal in conditional set (rho=0.384)."}
237	
238	=== exp_004_v2 ===
239	status: DONE
240	hypothesis: N-ablation v2 (N=4,8,16,32): tests how sample count affects signal ρ and selection F1. Validates N-scaling curve for structural vs surface signals under corrected pipeline.
241	conclusion: success
242	created_at: "2026-05-14T15:31:40.554Z"
243	updated_at: "2026-05-17T02:57:35.012Z"
244	
245	=== exp_005 ===
246	status: DONE
247	hypothesis: 
248	conclusion: success
249	created_at: "2026-05-14T11:45:16.360Z"
250	updated_at: "2026-05-14T11:45:38.570Z"
251	
252	=== exp_005_v2 ===
253	status: DONE
254	hypothesis: Selection F1 analysis v2: compute actual selection F1 (pick best sample by each signal) vs greedy and oracle. First evidence of correlation-selection gap under corrected pipeline.
255	conclusion: success
256	created_at: "2026-05-14T15:28:14.924Z"
257	updated_at: "2026-05-17T02:57:38.756Z"
258	
259	=== exp_006_v2 ===
260	status: DONE
261	hypothesis: Temperature sensitivity v2: tests signal effectiveness at T=0.5,0.7,1.0,1.2. Hypothesis: structural signals are temperature-robust while LP degrades at extreme temperatures.
262	conclusion: negative
263	created_at: "2026-05-14T15:30:02.348Z"
264	updated_at: "2026-05-17T02:57:36.914Z"
265	metrics: {"NER_SciERC_s42": {"greedy": 0.618, "oracle": 0.787, "SJ": 0.62, "logprob": 0.621, "FK": 0.621, "EM": 0.606, "voting_conf": 0.585, "random": 0.586}, "NER_SciERC_s123": {"greedy": 0.618, "oracle": 0.785, "SJ": 0.617, "logprob": 0.618, "FK": 0.621, "EM": 0.613, "voting_conf": 0.584, "random": 0.583}, "NER_CoNLL": {"greedy": 0.725, "oracle": 0.757, "SJ": 0.718, "logprob": 0.716, "FK": 0.717, "EM": 0.716, "voting_conf": 0.714, "random": 0.692}, "RE_SciERC": {"greedy": 0.403, "oracle": 0.631, "SJ": 0.397, "logprob": 0.41, "FK": 0.396, "EM": 0.381, "voting_conf": 0.408, "random": 0.364}}
266	
267	=== exp_007_llama_inference ===
268	status: DONE
269	hypothesis: LLaMA SciERC N=8 baseline: first cross-model test. Verifies structural signal effectiveness generalizes from Qwen to LLaMA model family on SciERC NER.
270	conclusion: success
271	created_at: "2026-05-14T13:54:48.055Z"
272	updated_at: "2026-05-17T02:58:03.014Z"
273	metrics: {"ner": {"greedy_f1": 0.66, "oracle_f1": 0.781, "headroom": 0.121, "rho_fk": 0.327, "rho_sj": 0.363, "rho_fk_cond": 0.226, "rho_sj_cond": 0.311, "rho_logprob": 0.183, "rho_logprob_cond": 0.109, "structural_beats_surface": true, "sample_f1_pct_zero": 11.6}, "re": {"greedy_f1": 0.434, "oracle_f1": 0.568, "headroom": 0.135, "rho_fk": 0.305, "rho_sj": 0.299, "rho_fk_cond": 0.259, "rho_sj_cond": 0.405, "rho_logprob": 0.288, "rho_logprob_cond": 0.092, "structural_beats_surface": false, "sample_f1_pct_zero": 41.2}, "n_instances": 551, "N": 8, "T": 1, "seed": 42, "model": "LLaMA-3.1-8B-Instruct", "verdict": "FAIL", "verdict_note": "RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0"}
274	
275	=== exp_007_llama_n16 ===
276	status: DONE
277	hypothesis: LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count. Tests if LLaMA shows same N-scaling benefit for structural signals as Qwen.
278	conclusion: success
279	created_at: "2026-05-14T18:31:44.366Z"
280	updated_at: "2026-05-17T02:57:12.521Z"
281	metrics: {"N": 16, "dataset": "scierc", "subtask": "ner", "n_instances": 551, "n_valid": 529, "n_conditional": 478, "greedy_f1": 0.645, "full": {"SJ_rho": 0.3791, "FK_rho": 0.3081, "logprob_rho": 0.2041, "EM_rho": 0.3159, "voting_conf_rho": 0.4515, "SJ_AUROC": 0.717, "FK_AUROC": 0.6581, "logprob_AUROC": 0.5656, "EM_AUROC": 0.7686, "voting_conf_AUROC": 0.7266, "SJ_ECE": 0.1019, "FK_ECE": 0.1556, "logprob_ECE": 0.084, "EM_ECE": 0.1761, "voting_conf_ECE": 0.1365}, "conditional": {"SJ_rho": 0.3222, "FK_rho": 0.2182, "logprob_rho": 0.1286, "EM_rho": 0.3563, "voting_conf_rho": 0.3356, "SJ_AUROC": 0.7014, "FK_AUROC": 0.6392, "logprob_AUROC": 0.545, "EM_AUROC": 0.7708, "voting_conf_AUROC": 0.6988, "SJ_ECE": 0.1466, "FK_ECE": 0.1853, "logprob_ECE": 0.1141, "EM_ECE": 0.1887, "voting_conf_ECE": 0.2634}, "n8_vs_n16_delta_rho_full": {"SJ": 0.0161, "FK": -0.0185, "logprob": 0.0214, "EM": 0.0007, "voting_conf": 0.0184}}
282	
283	=== exp_007_llama_n16_r1024 ===
284	status: DONE
285	hypothesis: 
286	conclusion: killed
287	created_at: "2026-05-14T22:16:59.685Z"
288	updated_at: "2026-05-15T01:20:52.194Z"
289	
290	=== exp_007_llama_scierc_seed123 ===
291	status: DONE
292	hypothesis: Structural consistency signals (SJ, FK) correlate with entity F1 for LLaMA-8B on SciERC at seed=123, and DGS selection improves over greedy baseline
293	conclusion: negative
294	created_at: "2026-05-18T19:10:26.278Z"
295	updated_at: "2026-05-18T20:49:08.934Z"
296	metrics: {"greedy_f1": 0.6454, "oracle_f1": 0.7657, "headroom": 0.1204, "degen_rate": 0.2665, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "dgs_delta_pp": -0.38, "rho_SJ_full": 0.3552, "rho_voting_conf_full": 0.4193, "auroc_SJ_full": 0.7092, "auroc_EM_full": 0.7468}
297	
298	=== exp_007_llama_seed123 ===
299	status: DONE
300	hypothesis: LLaMA SciERC seed=123: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.
301	conclusion: negative
302	created_at: "2026-05-14T15:08:50.157Z"
303	updated_at: "2026-05-17T02:57:58.879Z"
304	metrics: {"verdict": "FAIL", "ner": {"greedy_f1": 0.6605, "oracle_f1": 0.7703, "headroom": 0.1098, "fleiss_kappa": 0.4553, "soft_jaccard": 0.7525, "rho_kappa_f1": 0.2143, "rho_sj_f1": 0.3371, "structural_gt_surface": true}, "re": {"greedy_f1": 0.433, "oracle_f1": 0.5719, "headroom": 0.1389, "fleiss_kappa": 0.3851, "soft_jaccard": 0.6911, "rho_kappa_f1": 0.2844, "rho_sj_f1": 0.268, "structural_gt_surface": false}, "fail_reasons": ["RE rho_sj=0.2680 < 0.40 threshold", ">30% samples F1=0 (RE: 41.0%)", "RE structural not > surface (delta=-0.0165)"]}
305	
306	=== exp_007_llama_seed456 ===
307	status: DONE
308	hypothesis: LLaMA SciERC seed=456: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.
309	conclusion: negative
310	created_at: "2026-05-14T15:08:50.628Z"
311	updated_at: "2026-05-17T02:57:59.595Z"
312	metrics: {"verdict": "FAIL", "ner": {"greedy_f1": 0.6597, "oracle_f1": 0.7575, "oracle_headroom": 0.0978, "fleiss_kappa": 0.4543, "soft_jaccard": 0.7491, "rho_kappa_f1": 0.3115, "rho_sj_f1": 0.3663, "structural_gt_surface": true}, "re": {"greedy_f1": 0.4334, "oracle_f1": 0.5789, "oracle_headroom": 0.1455, "fleiss_kappa": 0.3791, "soft_jaccard": 0.6782, "rho_kappa_f1": 0.3013, "rho_sj_f1": 0.287, "structural_gt_surface": false}, "logprob_ner": {"rho": 0.1911, "auroc": 0.5989}, "logprob_re": {"rho": 0.3246, "auroc": 0.6678}, "fail_reason": "RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0"}
313	
314	=== exp_007_ner_llama ===
315	status: DONE
316	hypothesis: 
317	conclusion: killed
318	created_at: "2026-05-14T11:42:21.510Z"
319	updated_at: "2026-05-15T12:41:27.410Z"
320	notes: "Completed as exp_007_llama_n16 on autodl-5090. Registry status corrected."
321	
322	=== exp_007_ner_multi_model ===
323	status: DONE
324	hypothesis: Multi-model NER comparison: evaluates signal effectiveness across Qwen and LLaMA on SciERC NER. Establishes cross-model generalization of structural>surface ranking.
325	conclusion: success
326	created_at: "2026-05-14T11:42:20.748Z"
327	updated_at: "2026-05-17T02:58:16.747Z"
328	metrics: {"epoch": 5, "train_loss": 0.0767, "eval_loss": 0.1049, "train_runtime_sec": 1494.5, "train_samples_per_second": 6.226, "checkpoints": ["checkpoint-400", "checkpoint-500", "checkpoint-585"], "base_model": "Meta-Llama-3.1-8B-Instruct", "lora_r": 32, "lora_alpha": 64, "note": "EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact."}
329	
330	=== exp_008_re_n16 ===
331	status: DONE
332	hypothesis: RE N=16 initial evaluation: first relation extraction test with structural signals. Establishes baseline RE signal effectiveness before pipeline corrections.
333	conclusion: success
334	created_at: "2026-05-14T12:03:06.876Z"
335	updated_at: "2026-05-17T02:58:19.490Z"
336	metrics: {"ner": {"greedy_f1": 0.6635, "oracle_f1": 0.8208, "headroom": 0.1572, "rho_sj_full": 0.377, "rho_fk_full": 0.2508, "rho_logprob_full": 0.3153, "rho_sj_cond": 0.3598, "rho_fk_cond": 0.2251, "rho_logprob_cond": 0.2927, "sj_beats_fk": true, "rho_advantage": 0.1262}, "re": {"greedy_f1": 0.4339, "oracle_f1": 0.6658, "headroom": 0.2319, "rho_sj_full": 0.2966, "rho_fk_full": 0.2871, "rho_logprob_full": 0.2986, "rho_sj_cond": 0.3975, "rho_fk_cond": 0.3774, "rho_logprob_cond": 0.2745, "sj_beats_fk": true, "rho_advantage": 0.0095}, "verdict": "FAIL"}
337	
338	=== exp_008_re_n16_full ===
339	status: DONE
340	hypothesis: 
341	conclusion: killed
342	created_at: "2026-05-14T12:45:10.852Z"
343	updated_at: "2026-05-14T17:51:43.957Z"
344	
345	=== exp_008_re_n16_t10_full ===
346	status: DONE
347	hypothesis: RE N=16 T=1.0 full dataset: early RE evaluation attempt. Tests structural signals on relation extraction before pipeline corrections.
348	conclusion: negative
349	created_at: "2026-05-14T13:27:42.867Z"
350	updated_at: "2026-05-17T02:58:10.171Z"
351	metrics: {"ner": {"rho_sj": 0.444}, "re": {"rho_sj": 0.248}, "n_instances": 551, "N": 16, "T": 1, "seed": 42, "mode": "RE-only", "source": "director_corrected"}
352	
353	=== exp_008_re_n16_v2 ===
354	status: DONE
355	hypothesis: RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count. Hypothesis: SJ/FK benefit from more samples on RE task where zero-F1 rate is high.
356	conclusion: negative
357	created_at: "2026-05-14T14:34:06.296Z"
358	updated_at: "2026-05-17T02:57:41.178Z"
359	metrics: {"sj_rho_full": 0.281, "sj_rho_cond": 0.308, "f1_zero_pct": 44.3, "conclusion_note": "RE N=16 v2 negative: SJ weak, 44.3% F1=0"}
360	
361	=== exp_008_re_seed123 ===
362	status: DONE
363	hypothesis: RE seed=123 multi-seed: tests reproducibility of RE signal rankings. Hypothesis: RE signals weaker than NER due to higher zero-F1 rate, but ranking should be seed-stable.
364	conclusion: negative
365	created_at: "2026-05-14T15:08:51.386Z"
366	updated_at: "2026-05-17T02:57:58.166Z"
367	metrics: {"greedy_f1": 0.4229, "oracle_f1": 0.6244, "oracle_headroom": 0.2015, "fleiss_kappa_mean": 0.3455, "soft_jaccard_mean": 0.6126, "sample_f1_mean": 0.3594, "sample_f1_std": 0.3793, "sample_f1_zero_pct": 44.1, "structural_gt_surface": false, "rho_kappa_f1_full": 0.3174, "rho_sj_f1_full": 0.2835, "rho_kappa_f1_cond": 0.0766, "rho_sj_f1_cond": 0.2877, "logprob_auroc_full": 0.6499, "logprob_auroc_cond": 0.5265, "verdict": "FAIL"}
368	
369	=== exp_009_capability_stratification ===
370	status: DONE
371	hypothesis: Capability stratification analysis: test if SJ signal effectiveness varies with instance difficulty (greedy F1 quartiles), sentence length, and entity/relation count. Identifies which instance subpopulations benefit most from structural consistency signals.
372	conclusion: success
373	created_at: "2026-05-14T14:59:24.201Z"
374	updated_at: "2026-05-17T02:56:02.685Z"
375	metrics: {"scierc_ner": {"n": 551, "sj_rho_overall": 0.398, "by_greedy_f1": {"hard_0_25_sj_rho": 0.159, "med_low_sj_rho": 0.139, "med_high_sj_rho": 0.09, "easy_sj_rho": 0.23}, "by_sent_len": {"Q1_sj_rho": 0.461, "Q2_sj_rho": 0.401, "Q3_sj_rho": 0.296, "Q4_sj_rho": 0.382}, "by_ent_count": {"0_sj_rho": 0.689, "1_2_sj_rho": 0.415, "3_5_sj_rho": 0.353, "6plus_sj_rho": 0.547}}, "scierc_re": {"n": 551, "by_greedy_f1": {"hard_0_25_sj_rho": -0.043, "easy_sj_rho": 0.21}, "by_sent_len": {"Q1_sj_rho": 0.447, "Q4_sj_rho": 0.54}, "by_rel_count": {"0_sj_rho": 0.62, "1_2_sj_rho": 0.275, "6plus_sj_rho": 0.527}}, "conll_ner": {"n": 3453, "by_sent_len": {"Q1_sj_rho": 0.334, "Q3_sj_rho": 0.518}}, "proxy_independence": {"scierc_ner_f1_vs_slen": -0.021, "scierc_ner_f1_vs_ecnt": 0.007, "scierc_re_f1_vs_slen": -0.147}}
376	notes: "Registry metrics are PRE-gold-filter (n=551). Paper uses exp_009_v2_re_rerun (gold-filtered n=397): RE Q1_sj_rho=0.110, Q4_sj_rho=0.473. Registry values (Q1=0.447, Q4=0.540) are SUPERSEDED."
377	
378	=== exp_009_v2 ===
379	status: DONE
380	hypothesis: Capability stratification v2: corrected stratification with gold-filtering and extended to NER conditional analysis. Tests which instance subpopulations drive overall signal effectiveness.
381	conclusion: success
382	created_at: "2026-05-14T15:36:47.946Z"
383	updated_at: "2026-05-17T02:57:32.655Z"
384	metrics: {"ner_seed42_global": {"sj_rho": 0.431, "fk_rho": 0.325, "logprob_rho": 0.203, "voting_conf_rho": 0.475, "em_rho": 0.292}, "ner_seed123_global": {"sj_rho": 0.422, "fk_rho": 0.315, "logprob_rho": 0.226, "voting_conf_rho": 0.438, "em_rho": 0.299}, "re_seed42_global": {"sj_rho": 0.063, "fk_rho": 0.226, "logprob_rho": 0.4, "voting_conf_rho": 0.22, "em_rho": -0.132}, "ner_seed_stability_max_delta": 0.037, "independent_proxies": ["sent_len", "ent_count", "type_diversity"], "inverted_u_ner": "not confirmed (ρ stable across independent proxies)", "inverted_u_re": "monotonic increase with complexity, not inverted-U"}
385	
386	=== exp_009_v2_re_rerun ===
387	status: DONE
388	hypothesis: Capability stratification v2 (RE rerun): corrected stratification analysis for RE with proper gold-filtering. Fixes early pipeline bug affecting RE quartile ρ values.
389	conclusion: success
390	created_at: "2026-05-14T18:56:31.535Z"
391	updated_at: "2026-05-17T02:57:16.383Z"
392	
393	=== exp_010_selection_curves ===
394	status: DONE
395	hypothesis: Selection curve analysis: plots selection F1 vs confidence threshold for each signal. Visualizes where correlation-selection gap emerges and at what confidence level signals become useful for filtering.
396	conclusion: success
397	created_at: "2026-05-14T15:01:53.585Z"
398	updated_at: "2026-05-17T02:58:00.378Z"
399	metrics: {"scierc_ner": {"n_instances": 551, "greedy_f1": 0.618, "N16": {"oracle": 0.787, "SJ": 0.62, "FK": 0.621, "logprob": 0.621, "voting_conf": 0.585, "EM": 0.606, "random": 0.595}, "N8": {"oracle": 0.752, "SJ": 0.614, "FK": 0.614, "logprob": 0.619, "voting_conf": 0.591, "EM": 0.603, "random": 0.589}, "N4": {"oracle": 0.714, "SJ": 0.607, "FK": 0.608, "logprob": 0.616, "voting_conf": 0.594, "EM": 0.6, "random": 0.587}}, "scierc_re": {"n_instances": 397, "greedy_f1": 0.403, "N16": {"oracle": 0.631, "SJ": 0.397, "FK": 0.396, "logprob": 0.41, "voting_conf": 0.408, "EM": 0.381, "random": 0.364}, "N8": {"oracle": 0.583, "SJ": 0.393, "FK": 0.394, "logprob": 0.413, "voting_conf": 0.398, "EM": 0.381, "random": 0.363}}, "conll_ner": {"n_instances": 3453, "greedy_f1": 0.725, "N8": {"oracle": 0.757, "SJ": 0.718, "FK": 0.717, "logprob": 0.716, "voting_conf": 0.714, "EM": 0.716, "random": 0.69}, "N4": {"oracle": 0.746, "SJ": 0.714, "FK": 0.714, "logprob": 0.715, "voting_conf": 0.714, "EM": 0.712, "random": 0.692}}}
400	
401	=== exp_011_ood_conll_to_scierc ===
402	status: DONE
403	hypothesis: Out-of-domain transfer test: CoNLL-trained model on SciERC data. Tests if confidence signals retain correlation with quality under severe schema mismatch (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material).
404	conclusion: negative
405	created_at: "2026-05-15T11:36:08.325Z"
406	updated_at: "2026-05-17T02:56:14.242Z"
407	metrics: {"greedy_ner_f1": 0.009, "greedy_re_f1": 0.001, "avg_structural_rho": -0.05, "verdict": "FAIL", "reason": "schema_incompatibility", "direction": "CoNLL_model_to_SciERC_data", "sample_f1_pct_zero_ner": 98.06, "rho_sj_ner": -0.186, "rho_fk_ner": -0.069, "note": "Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals."}
408	
409	=== exp_011_ood_scierc_to_conll ===
410	status: DONE
411	hypothesis: Out-of-domain transfer: SciERC-trained model on CoNLL data. Tests if confidence signals work under partial schema overlap (SciERC has Organization/Person which overlap with CoNLL ORG/PER). Complement to exp_011_ood_conll_to_scierc.
412	conclusion: success
413	created_at: "2026-05-15T11:36:07.210Z"
414	updated_at: "2026-05-17T02:56:29.417Z"
415	metrics: {"greedy_ner_f1": 0.522, "rho_vc": 0.469, "rho_sj": 0.378, "rho_em": 0.3, "rho_fk": 0.285, "rho_lp": 0.246}
416	
417	=== exp_012_logprob_baseline ===
418	status: DONE
419	hypothesis: 
420	conclusion: success
421	created_at: "2026-05-14T10:53:16.166Z"
422	updated_at: "2026-05-14T11:13:30.240Z"
423	metrics: {"ner_full_rho_sj": 0.3565, "ner_full_rho_fk": 0.2651, "ner_full_rho_logprob": 0.1396, "ner_full_rho_greedy_logprob": 0.1615, "ner_full_tau_sj": 0.2658, "ner_full_tau_logprob": 0.1006, "ner_full_auroc_sj": 0.6892, "ner_full_auroc_fk": 0.6292, "ner_full_auroc_logprob": 0.5907, "ner_full_n": 529, "ner_sj_vs_logprob_delta": 0.2169, "re_full_rho_sj": 0.2112, "re_full_rho_fk": 0.2528, "re_full_rho_logprob": 0.2467, "re_full_auroc_sj": 0.5916, "re_full_auroc_fk": 0.6262, "re_full_auroc_logprob": 0.6186, "re_full_n": 397, "re_cond_rho_sj": 0.3683, "re_cond_rho_fk": 0.3168, "re_cond_rho_logprob": 0.1457, "re_cond_auroc_sj": 0.6839, "re_cond_auroc_logprob": 0.5487, "re_cond_n": 296, "diagnosis": "NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED."}
424	
425	=== exp_012_rerun_1024 ===
426	status: DONE
427	hypothesis: Canonical SciERC baseline with max_tokens=1024: Qwen3-8B ft_002_v2, N=8, T=1.0, seed=42, joint NER+RE. Establishes ground-truth ρ rankings and selection F1 for all 5 signals under correct generation length.
428	conclusion: success
429	created_at: "2026-05-14T22:11:33.777Z"
430	updated_at: "2026-05-18T20:49:42.395Z"
431	metrics: {"degen_rate": 0.1777, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "ner_full": {"n": 529, "SJ": {"rho": 0.3599, "tau": 0.2646, "AUROC": 0.6917, "ECE": 0.4531, "rho_ci95": [0.2732, 0.4389], "AUROC_ci95": [0.6304, 0.7406]}, "FK": {"rho": 0.2665, "tau": 0.1974, "AUROC": 0.629, "ECE": 0.4512, "rho_ci95": [0.1743, 0.3486], "AUROC_ci95": [0.5612, 0.6882]}, "logprob": {"rho": 0.2052, "tau": 0.1478, "AUROC": 0.5783, "ECE": 0.7064, "rho_ci95": [0.1171, 0.2904], "AUROC_ci95": [0.5179, 0.6387]}, "EM": {"rho": 0.2945, "tau": 0.2208, "AUROC": 0.7493, "ECE": 0.3526, "rho_ci95": [0.2094, 0.37], "AUROC_ci95": [0.7002, 0.7928]}, "voting_conf": {"rho": 0.3792, "tau": 0.2805, "AUROC": 0.6841, "ECE": 0.3807, "rho_ci95": [0.2972, 0.4486], "AUROC_ci95": [0.6249, 0.7366]}}, "ner_cond": {"n": 477, "SJ": {"rho": 0.3113, "tau": 0.2257, "AUROC": 0.6772, "ECE": 0.4416, "rho_ci95": [0.2353, 0.3959], "AUROC_ci95": [0.621, 0.7337]}, "FK": {"rho": 0.1761, "tau": 0.1284, "AUROC": 0.6078, "ECE": 0.4389, "rho_ci95": [0.0839, 0.2665], "AUROC_ci95": [0.5442, 0.6709]}, "logprob": {"rho": 0.1538, "tau": 0.1111, "AUROC": 0.5633, "ECE": 0.6803, "rho_ci95": [0.0637, 0.2424], "AUROC_ci95": [0.5032, 0.6232]}, "EM": {"rho": 0.3596, "tau": 0.2735, "AUROC": 0.7556, "ECE": 0.3257, "rho_ci95": [0.2819, 0.4408], "AUROC_ci95": [0.7011, 0.8107]}, "voting_conf": {"rho": 0.3, "tau": 0.2189, "AUROC": 0.6618, "ECE": 0.3746, "rho_ci95": [0.2168, 0.3836], "AUROC_ci95": [0.6004, 0.7201]}}, "re_full": {"n": 397, "SJ": {"rho": 0.2503, "tau": 0.1878, "AUROC": 0.6702, "ECE": 0.3865}, "FK": {"rho": 0.2752, "tau": 0.2117, "AUROC": 0.6089, "ECE": 0.4405}, "logprob": {"rho": 0.2662, "tau": 0.1951, "AUROC": 0.6005, "ECE": 0.7694}, "EM": {"rho": 0.1344, "tau": 0.1081, "AUROC": 0.7059, "ECE": 0.3548}, "voting_conf": {"rho": 0.3498, "tau": 0.2663, "AUROC": 0.6935, "ECE": 0.2724}}, "re_cond": {"n": 238, "SJ": {"rho": 0.2457, "tau": 0.1811, "AUROC": 0.6463, "ECE": 0.2941}, "FK": {"rho": 0.1139, "tau": 0.0876, "AUROC": 0.551, "ECE": 0.3424}, "logprob": {"rho": 0.0112, "tau": 0.0051, "AUROC": 0.5186, "ECE": 0.6464}, "EM": {"rho": 0.4165, "tau": 0.3256, "AUROC": 0.7515, "ECE": 0.2232}, "voting_conf": {"rho": 0.2409, "tau": 0.178, "AUROC": 0.642, "ECE": 0.207}}, "delta_vs_512_ner_full_rho": {"SJ": 0.0034, "FK": 0.0014, "EM": 0.0379, "voting_conf": -0.1226, "logprob": 0.0656}, "provenance_note": "exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205."}
432	
433	=== exp_013_exact_match_voting ===
434	status: DONE
435	hypothesis: 
436	conclusion: negative
437	created_at: "2026-05-14T10:53:18.753Z"
438	updated_at: "2026-05-14T11:33:22.644Z"
439	metrics: {"ner_full_rho": 0.2941, "ner_full_p": 5.12e-12, "ner_full_tau": 0.2181, "ner_full_auroc": 0.6398, "re_full_rho": 0.1562, "re_full_p": 0.0018, "re_full_tau": 0.1185, "re_full_auroc": 0.5863, "diagnosis": "EM between SJ and FK on NER, weakest on RE. Too coarse-grained."}
440	
441	=== exp_014_entity_majority_voting ===
442	status: DONE
443	hypothesis: 
444	conclusion: success
445	created_at: "2026-05-14T10:53:21.203Z"
446	updated_at: "2026-05-14T11:33:30.085Z"
447	metrics: {"ner_full_rho": 0.3915, "ner_full_p": 8.1e-21, "ner_full_tau": 0.2906, "ner_full_auroc": 0.7039, "re_full_rho": 0.3403, "re_full_p": 3.21e-12, "re_full_tau": 0.256, "re_full_auroc": 0.6668, "ner_voting_f1": 0.6246, "ner_greedy_f1": 0.6483, "ner_oracle_f1": 0.7793, "re_voting_f1": 0.3577, "re_greedy_f1": 0.4022, "re_oracle_f1": 0.5886, "diagnosis": "Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy."}
448	
449	=== exp_015_metrics_expansion ===
450	status: DONE
451	hypothesis: Unified 5-signal evaluation (SJ/FK/EM/VC/LP) on single canonical data source (exp_012 logprobs). Establishes complete signal ranking with ρ, AUROC, and τ metrics for both NER and RE under consistent conditions.
452	conclusion: success
453	created_at: "2026-05-14T11:47:36.569Z"
454	updated_at: "2026-05-17T02:55:35.391Z"
455	metrics: {"data_source": "exp_012_logprob/samples_with_logprobs.jsonl", "config": "N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2", "ner": {"n_valid": 529, "n_cond": 501, "voting_rho_full": 0.5018, "voting_rho_cond": 0.4497, "voting_auroc": 0.7279, "voting_tau": 0.3766, "sj_rho_full": 0.3565, "sj_rho_cond": 0.412, "sj_auroc": 0.6656, "sj_tau": 0.2658, "em_rho_full": 0.2566, "em_rho_cond": 0.3427, "em_auroc": 0.623, "em_tau": 0.1924, "fk_rho_full": 0.2651, "fk_rho_cond": 0.306, "fk_auroc": 0.6243, "fk_tau": 0.2027, "logprob_rho_full": 0.1396, "logprob_rho_cond": 0.1627, "logprob_auroc": 0.5585, "logprob_tau": 0.1006}, "re": {"n_valid": 397, "n_cond": 296, "voting_rho_full": 0.4217, "voting_rho_cond": 0.463, "voting_auroc": 0.7162, "voting_tau": 0.327, "sj_rho_full": 0.2112, "sj_rho_cond": 0.3683, "sj_auroc": 0.5816, "sj_tau": 0.1619, "em_rho_full": 0.1002, "em_rho_cond": 0.3607, "em_auroc": 0.5036, "em_tau": 0.0839, "fk_rho_full": 0.2528, "fk_rho_cond": 0.3168, "fk_auroc": 0.6308, "fk_tau": 0.1967, "logprob_rho_full": 0.2467, "logprob_rho_cond": 0.1457, "logprob_auroc": 0.6354, "logprob_tau": 0.1808}, "diagnosis": "Unified 5-signal evaluation on single data source. Voting leads NER full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond."}
456	notes: "RE logprob_rho_cond=0.1457 uses WRONG conditional filter (any sample F1>0, n=331). Correct value: 0.0112 from exp_012_rerun_1024 (greedy_f1>0, n=238). This entry's RE cond values are DEPRECATED."
457	
458	=== exp_015_v2 ===
459	status: DONE
460	hypothesis: Metrics expansion v2: corrected evaluation with proper conditional filtering. Updates exp_015 with gold-filtered pipeline to fix RE conditional ρ values that used wrong filter criterion.
461	conclusion: success
462	created_at: "2026-05-14T15:34:23.336Z"
463	updated_at: "2026-05-17T02:56:55.830Z"
464	metrics: {"scierc_ner_avg": {"sj_auroc": 0.7394, "fk_auroc": 0.6172, "em_auroc": 0.7873, "voting_auroc": 0.7367, "logprob_auroc": 0.5918}, "scierc_re_avg": {"sj_auroc": 0.6746, "fk_auroc": 0.5939, "em_auroc": 0.715, "voting_auroc": 0.7234, "logprob_auroc": 0.5849}}
465	
466	=== exp_016_rerun_1024_bootstrap ===
467	status: DONE
468	hypothesis: 3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant.
469	conclusion: negative
470	created_at: "2026-05-14T23:44:21.577Z"
471	updated_at: "2026-05-17T03:33:39.786Z"
472	metrics: {"bootstrap_ci_95": [-0.03, 0.042], "permutation_p": 0.39, "cohen_d": 0.038, "sign_test_win_rate": 0.466, "ner_logprob_vs_greedy_delta": 0.006, "conclusion_summary": "NER selection: no signal significantly outperforms greedy; RE: same conclusion"}
473	parent: "exp_016_rerun_1024"
474	
475	=== exp_016_signal_ensemble ===
476	status: DONE
477	hypothesis: 
478	conclusion: success
479	created_at: "2026-05-14T12:15:23.771Z"
480	updated_at: "2026-05-14T12:42:55.931Z"
481	metrics: {"sj_logprob_pearson_ner": 0.57, "sj_logprob_pearson_re": 0.42, "best_linear_ner": {"combo": "SJ+voting_conf", "alpha": 0.3, "rho": 0.489}, "best_linear_re": {"combo": "voting_conf+logprob", "alpha": 0.6, "rho": 0.429}, "ensemble_ner_auroc": 0.735, "ensemble_re_auroc": 0.719, "best_single_ner_auroc": 0.7, "best_single_re_auroc": 0.721, "ensemble_ner_delta": 0.035, "selection_f1_ner": {"greedy": 0.609, "logprob": 0.609, "sj": 0.604, "ensemble": 0.604, "voting": 0.596, "random": 0.58, "oracle": 0.769}, "selection_f1_re": {"logprob": 0.397, "greedy": 0.374, "sj": 0.368, "ensemble": 0.367, "voting": 0.338, "random": 0.338, "oracle": 0.561}, "diagnosis": "SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge."}
482	
483	=== exp_016_v2 ===
484	status: DONE
485	hypothesis: Bootstrap significance v2: corrected bootstrap test for NER selection F1 gap with proper gold-filtering and multiple signals. Establishes which selection improvements are statistically significant.
486	conclusion: success
487	created_at: "2026-05-14T15:39:07.501Z"
488	updated_at: "2026-05-17T02:57:30.726Z"
489	metrics: {"ner_conditional": {"n": 529, "best_single_signal_rho": {"soft_jaccard": 0.4412}, "best_combo_rho": {"sj+vc_a0.55": 0.4552}, "ensemble_auroc": 0.7141, "best_single_auroc": {"soft_jaccard": 0.7166}, "selection_f1": {"greedy": 0.6442, "logprob_best": 0.6505, "ensemble_best": 0.6475, "sj_best": 0.6471, "oracle": 0.8442}}, "re_conditional": {"n": 397, "best_single_signal_rho": {"voting_confidence": 0.3849}, "best_combo_rho": {"logprob+vc_a0.25": 0.3936}, "ensemble_auroc": 0.6916, "best_single_auroc": {"voting_confidence": 0.7023}, "selection_f1": {"greedy": 0.403, "logprob_best": 0.4097, "ensemble_best": 0.4227, "oracle": 0.6306}}, "re_full": {"ensemble_auroc": 0.8608, "best_single_auroc": {"voting_confidence": 0.8248}}}
490	
491	=== exp_017_llama_conll ===
492	status: DONE
493	hypothesis: On CoNLL (high degeneracy regime), LLaMA should show the same pattern as Qwen3: LP selection fails due to narrow headroom, but structural signals retain diagnostic value (QE rho). Cross-model validation of the degeneracy-driven signal effectiveness framework.
494	conclusion: success
495	created_at: "2026-05-14T14:39:32.014Z"
496	updated_at: "2026-05-18T19:11:03.240Z"
497	parent: "exp_007_llama_inference"
498	metrics: {"degeneracy_cf1_gold_filtered": 0.894, "n_constant_f1": 2465, "n_gold_filtered": 2756, "n_total": 3453, "greedy_f1": 0.9239, "oracle_f1": 0.9451, "random_f1": 0.9207, "headroom_pp": 2.11, "dgs_f1": 0.9254, "dgs_delta_pp": 0.14, "dgs_nondegen_lp_delta_pp": 1.37, "selection_f1": {"SJ": {"f1": 0.9237, "delta_pp": -0.04}, "FK": {"f1": 0.924, "delta_pp": -0.02}, "VC": {"f1": 0.925, "delta_pp": 0.08}, "EM": {"f1": 0.9244, "delta_pp": 0.02}, "LP": {"f1": 0.9244, "delta_pp": 0.02}}, "qe_rho_full_3seed": {"SJ": {"mean": 0.4631, "sd": 0.0074}, "FK": {"mean": 0.4546, "sd": 0.0061}, "EM": {"mean": 0.4603, "sd": 0.0078}, "VC": {"mean": 0.4579, "sd": 0.003}, "LP": {"mean": 0.3099, "sd": 0.0055}}, "qe_auroc_full_3seed": {"SJ": {"mean": 0.736, "sd": 0.0064}, "FK": {"mean": 0.732, "sd": 0.0063}, "EM": {"mean": 0.7355, "sd": 0.0069}, "VC": {"mean": 0.7394, "sd": 0.0041}, "LP": {"mean": 0.7629, "sd": 0.0044}}, "lp_range": {"mean": 0.0198, "std": 0.0315, "median": 0.0002}}
499	
500	=== exp_017_llama_conll_finetune ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7fa2030-545a-4b96-a1ab-b02b0fdac9c0",
  "isSidechain": true,
  "promptId": "9d5a8dbf-14d3-41c1-a18a-ef8acd67e6cb",
  "agentId": "a97ebe3840b34757a",
  "type": "user",
  "uuid": "fed8ae9f-256b-48ce-b571-7f816ee0128a",
  "sourceToolAssistantUUID": "e7fa2030-545a-4b96-a1ab-b02b0fdac9c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T10:44:39.180Z_

<details open><summary>🔧 Tool call — Read · `toolu_012dBTGbQWeLX5JtFKVvECo9`</summary>

```json
{
  "file_path": "/tmp/registry_full.txt",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fed8ae9f-256b-48ce-b571-7f816ee0128a",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
  "requestId": "req_011CbDgeHu6ynQvykEHLgzpt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "150250d1-8ed4-4a4d-8a05-cfbff069b65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y2xWAb4BxfeZD92r1fX6Ck",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22019,
      "cache_read_input_tokens": 33221,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 33221,
          "cache_creation_input_tokens": 22019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22019,
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

_source line 17 · 2026-05-20T10:44:39.595Z_

<details><summary>↩ Tool result · `toolu_012dBTGbQWeLX5JtFKVvECo9`</summary>

```text
500	=== exp_017_llama_conll_finetune ===
501	status: DONE
502	hypothesis: Structural self-consistency QE signals (SJ, FK, VC, EM) show model-agnostic diagnostic power: their Spearman rho with per-instance F1 should be comparable on LLaMA 3.1-8B as on Qwen 2.5-7B for CoNLL-2003 NER, even though degeneracy rates and absolute F1 may differ.
503	conclusion: success
504	created_at: "2026-05-18T16:47:36.156Z"
505	updated_at: "2026-05-18T18:43:42.649Z"
506	parent: "exp_llama_fewnerd_lora"
507	metrics: {"degeneracy_rate": 0.853, "greedy_f1": 0.928, "oracle_f1": 0.951, "headroom": 0.023, "selection_f1": 0.934, "full_rho_SJ": 0.45, "full_rho_FK": 0.443, "full_rho_VC": 0.437, "full_rho_EM": 0.448, "full_rho_LP": 0.273, "full_AUROC_SJ": 0.752, "full_AUROC_EM": 0.753, "full_AUROC_LP": 0.739, "cond_rho_SJ": 0.454, "cond_rho_EM": 0.458, "cond_rho_LP": 0.311, "cond_AUROC_EM": 0.783, "cond_AUROC_LP": 0.804}
508	
509	=== exp_017_llama_conll_infer ===
510	status: DONE
511	hypothesis: LLaMA CoNLL N=8 baseline inference: initial cross-model test on CoNLL before scaling to N=16. Establishes LLaMA can do CoNLL NER effectively.
512	conclusion: success
513	created_at: "2026-05-14T17:33:23.653Z"
514	updated_at: "2026-05-17T02:57:21.948Z"
515	metrics: {"greedy_f1": 0.9266, "oracle_f1": 0.9443, "oracle_headroom": 0.0177, "n_instances": 3453, "n_valid": 2756, "n_conditional": 2642, "N": 8, "full": {"SJ_rho": 0.4314, "FK_rho": 0.4277, "logprob_rho": 0.3072, "EM_rho": 0.4306, "voting_conf_rho": 0.4256, "SJ_AUROC": 0.7039, "FK_AUROC": 0.7026, "logprob_AUROC": 0.761, "EM_AUROC": 0.7046, "voting_conf_AUROC": 0.7088, "SJ_ECE": 0.1137, "FK_ECE": 0.1053, "logprob_ECE": 0.129, "EM_ECE": 0.1094, "voting_conf_ECE": 0.0949}, "conditional": {"SJ_rho": 0.4356, "FK_rho": 0.431, "logprob_rho": 0.3282, "EM_rho": 0.4403, "voting_conf_rho": 0.3743, "SJ_AUROC": 0.7225, "FK_AUROC": 0.7208, "logprob_AUROC": 0.8102, "EM_AUROC": 0.7257, "voting_conf_AUROC": 0.6989, "SJ_ECE": 0.0829, "FK_ECE": 0.0796, "logprob_ECE": 0.0922, "EM_ECE": 0.0754, "voting_conf_ECE": 0.0784}}
516	notes: "LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances). SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761 > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8)."
517	
518	=== exp_017_llama_conll_n16 ===
519	status: DONE
520	hypothesis: LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL. First evidence that structural>surface ranking generalizes from Qwen to LLaMA model family.
521	conclusion: success
522	created_at: "2026-05-14T19:19:35.318Z"
523	updated_at: "2026-05-17T02:56:57.283Z"
524	metrics: {"greedy_f1": 0.9243, "oracle_f1": 0.9487, "oracle_headroom": 0.0244, "n_instances": 3453, "n_valid": 2756, "n_conditional": 2642, "structural_beats_surface": true, "full": {"SJ_rho": 0.4642, "SJ_AUROC": 0.7391, "SJ_ECE": 0.1131, "FK_rho": 0.4566, "FK_AUROC": 0.736, "FK_ECE": 0.1071, "logprob_rho": 0.3058, "logprob_AUROC": 0.7594, "logprob_ECE": 0.1288, "EM_rho": 0.4613, "EM_AUROC": 0.7391, "EM_ECE": 0.1084, "voting_conf_rho": 0.4554, "voting_conf_AUROC": 0.7406, "voting_conf_ECE": 0.0844}, "conditional": {"SJ_rho": 0.4597, "SJ_AUROC": 0.7565, "SJ_ECE": 0.0846, "FK_rho": 0.4515, "FK_AUROC": 0.753, "FK_ECE": 0.0813, "logprob_rho": 0.3193, "logprob_AUROC": 0.8023, "logprob_ECE": 0.0921, "EM_rho": 0.4618, "EM_AUROC": 0.7589, "EM_ECE": 0.0757, "voting_conf_rho": 0.3978, "voting_conf_AUROC": 0.7287, "voting_conf_ECE": 0.0742}, "best_of_n": {"greedy": 0.9243, "random_avg": 0.9213, "sj_best": 0.9259, "logprob_best": 0.925, "voting_conf_best": 0.9268, "oracle": 0.9487}, "n8_vs_n16_delta": {"full_SJ_rho_delta": 0.0328, "full_FK_rho_delta": 0.0289, "full_logprob_rho_delta": -0.0014, "full_EM_rho_delta": 0.0307, "full_voting_conf_rho_delta": 0.0298, "cond_SJ_rho_delta": 0.0241, "cond_FK_rho_delta": 0.0205, "cond_logprob_rho_delta": -0.0089, "cond_EM_rho_delta": 0.0215, "cond_voting_conf_rho_delta": 0.0235}}
525	
526	=== exp_017_llama_conll_n16_r1024 ===
527	status: DONE
528	hypothesis: LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction (fixes inflated FK ρ from gold-empty instances).
529	conclusion: success
530	created_at: "2026-05-14T22:17:01.036Z"
531	updated_at: "2026-05-18T20:50:11.906Z"
532	metrics: {"degen_rate": 0.8647, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "instance_count": 3453, "n_valid": 2756, "n_gold_empty": 697, "parse_rate": 1, "ner_greedy_f1": 0.9265, "ner_oracle_f1": 0.9499, "rho_fk_ner": 0.4752, "rho_sj_ner": 0.4836, "rho_vc_ner": 0.4746, "rho_em_ner": 0.4818, "rho_lp_ner": 0.3136, "auroc_fk_ner": 0.7467, "auroc_sj_ner": 0.7496, "auroc_vc_ner": 0.7529, "auroc_em_ner": 0.7508, "auroc_lp_ner": 0.7661, "auroc_note": "median F1=1.0, AUROC uses >=median threshold", "rho_note": "CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756)."}
533	
534	=== exp_017_llama_conll_n16_s123 ===
535	status: DONE
536	hypothesis: LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol
537	conclusion: success
538	created_at: "2026-05-14T19:23:21.084Z"
539	updated_at: "2026-05-14T19:43:06.607Z"
540	metrics: {"greedy_f1": 0.9266, "oracle_f1": 0.9497, "oracle_headroom": 0.0231, "n_instances": 3453, "n_valid": 2756, "n_conditional": 2642, "structural_beats_surface": true, "full": {"SJ_rho": 0.4698, "SJ_AUROC": 0.7402, "SJ_ECE": 0.1135, "FK_rho": 0.4594, "FK_AUROC": 0.7351, "FK_ECE": 0.1114, "logprob_rho": 0.3161, "logprob_AUROC": 0.768, "logprob_ECE": 0.129, "EM_rho": 0.4676, "EM_AUROC": 0.7399, "EM_ECE": 0.1082, "voting_conf_rho": 0.4612, "voting_conf_AUROC": 0.7429, "voting_conf_ECE": 0.0832}, "conditional": {"SJ_rho": 0.4712, "SJ_AUROC": 0.7609, "SJ_ECE": 0.0828, "FK_rho": 0.4595, "FK_AUROC": 0.7547, "FK_ECE": 0.0858, "logprob_rho": 0.3314, "logprob_AUROC": 0.8134, "logprob_ECE": 0.0922, "EM_rho": 0.4732, "EM_AUROC": 0.7626, "EM_ECE": 0.075, "voting_conf_rho": 0.4086, "voting_conf_AUROC": 0.7338, "voting_conf_ECE": 0.0706}, "best_of_n": {"greedy": 0.9242, "random_avg": 0.9216, "sj_best": 0.9247, "logprob_best": 0.9253, "voting_conf_best": 0.9255, "oracle": 0.9486}, "n8_vs_n16_delta": {"full_SJ_rho_delta": 0.0384, "full_FK_rho_delta": 0.0317, "full_logprob_rho_delta": 0.0089, "full_SJ_AUROC_delta": 0.0363, "full_FK_AUROC_delta": 0.0325, "full_logprob_AUROC_delta": 0.007, "cond_SJ_rho_delta": 0.0356, "cond_FK_rho_delta": 0.0285, "cond_logprob_rho_delta": 0.0032}}
541	
542	=== exp_017_llama_conll_n16_s123_r1024 ===
543	status: DONE
544	hypothesis: LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.
545	conclusion: success
546	created_at: "2026-05-14T22:17:02.953Z"
547	updated_at: "2026-05-18T20:47:52.122Z"
548	notes: "Output exists on autodl-5090. Registry status corrected from killed to success."
549	metrics: {"degen_rate": 0.8636, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
550	
551	=== exp_017_llama_conll_n16_s456 ===
552	status: DONE
553	hypothesis: LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol
554	conclusion: success
555	created_at: "2026-05-14T19:23:21.987Z"
556	updated_at: "2026-05-14T20:24:45.875Z"
557	metrics: {"greedy_f1": 0.9243, "oracle_f1": 0.9488, "oracle_headroom": 0.0245, "n_instances": 3453, "n_valid": 2756, "n_conditional": 2642, "structural_beats_surface": true, "full": {"SJ_rho": 0.4552, "SJ_AUROC": 0.7288, "SJ_ECE": 0.1134, "FK_rho": 0.4478, "FK_AUROC": 0.7248, "FK_ECE": 0.109, "logprob_rho": 0.3078, "logprob_AUROC": 0.7612, "logprob_ECE": 0.1289, "EM_rho": 0.452, "EM_AUROC": 0.7275, "EM_ECE": 0.1082, "voting_conf_rho": 0.4571, "voting_conf_AUROC": 0.7348, "voting_conf_ECE": 0.0863}, "conditional": {"SJ_rho": 0.4505, "SJ_AUROC": 0.7449, "SJ_ECE": 0.0826, "FK_rho": 0.4422, "FK_AUROC": 0.7401, "FK_ECE": 0.0835, "logprob_rho": 0.3242, "logprob_AUROC": 0.8067, "logprob_ECE": 0.0921, "EM_rho": 0.451, "EM_AUROC": 0.745, "EM_ECE": 0.0756, "voting_conf_rho": 0.3962, "voting_conf_AUROC": 0.7202, "voting_conf_ECE": 0.0746}, "best_of_n": {"greedy": 0.9243, "random_avg": 0.9215, "sj_best": 0.9243, "logprob_best": 0.9243, "voting_conf_best": 0.9243, "oracle": 0.9488}, "n8_vs_n16_delta": {"full_SJ_rho_delta": 0.0238, "full_FK_rho_delta": 0.0201, "full_logprob_rho_delta": 0.0006, "full_EM_rho_delta": 0.0214, "full_voting_conf_rho_delta": 0.0315, "cond_SJ_rho_delta": 0.0149, "cond_FK_rho_delta": 0.0112, "cond_logprob_rho_delta": -0.004, "cond_EM_rho_delta": 0.0107, "cond_voting_conf_rho_delta": 0.0219}}
558	
559	=== exp_017_llama_conll_n16_s456_r1024 ===
560	status: DONE
561	hypothesis: LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.
562	conclusion: success
563	created_at: "2026-05-14T22:17:04.572Z"
564	updated_at: "2026-05-18T20:50:15.047Z"
565	metrics: {"degen_rate": 0.8672, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "instance_count": 3453, "n_valid": 2756, "n_gold_empty": 697, "parse_rate": 1, "ner_greedy_f1": 0.9265, "ner_oracle_f1": 0.9499, "rho_fk_ner": 0.469, "rho_sj_ner": 0.4734, "rho_vc_ner": 0.4722, "rho_em_ner": 0.4752, "rho_lp_ner": 0.3099, "auroc_fk_ner": 0.7408, "auroc_sj_ner": 0.7428, "auroc_vc_ner": 0.7495, "auroc_em_ner": 0.7444, "auroc_lp_ner": 0.7628, "auroc_note": "median F1=1.0, AUROC uses >=median threshold", "rho_note": "CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756)."}
566	
567	=== exp_017_llama_conll_n8_t07 ===
568	status: DONE
569	hypothesis: LLaMA CoNLL N=8 T=0.7 防御性实验：填补"LLaMA 仅在 SciERC 上测过"的弱点，验证 cross-model consistency（vs Qwen CoNLL）。T=0.7 低温下 confidence signals 的 correlation-selection gap 是否依然存在。
570	conclusion: success
571	created_at: "2026-05-15T15:29:34.595Z"
572	updated_at: "2026-05-15T15:46:22.722Z"
573	parent: "exp_017_llama_conll"
574	metrics: {"n_valid": 2756, "greedy_f1": 0.9242, "oracle_f1": 0.9391, "lp_range_median": 1.1e-05, "lp_tied_fraction_005": 0.9579, "signals": {"SJ": {"rho": 0.3934, "auroc": 0.6506}, "FK": {"rho": 0.3879, "auroc": 0.6488}, "VC": {"rho": 0.375, "auroc": 0.6551}, "EM": {"rho": 0.3888, "auroc": 0.6494}, "LP": {"rho": 0.2951, "auroc": 0.7509}}, "selection_f1": {"SJ": 0.9247, "FK": 0.9254, "VC": 0.9264, "EM": 0.9255, "LP": 0.9248}}
575	
576	=== exp_018_llama_scierc_seed123 ===
577	status: DONE
578	hypothesis: LLaMA SciERC seed=123: multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.
579	conclusion: success
580	created_at: "2026-05-15T06:07:14.370Z"
581	updated_at: "2026-05-18T20:47:51.435Z"
582	metrics: {"degen_rate": 0.2665, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
583	
584	=== exp_018_llama_scierc_seed42_r1024 ===
585	status: DONE
586	hypothesis: LLaMA SciERC seed=42 (max_tokens=1024): cross-model validation on SciERC. Establishes LLaMA NER signal rankings on same dataset as Qwen for direct model-family comparison.
587	conclusion: success
588	created_at: "2026-05-15T06:09:57.155Z"
589	updated_at: "2026-05-18T20:50:00.335Z"
590	metrics: {"degen_rate": 0.2495, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "ner": {"full": {"SJ": {"rho": 0.3096, "tau": 0.2288, "auroc": 0.6683}, "FK": {"rho": 0.2352, "tau": 0.1759, "auroc": 0.6069}, "logprob": {"rho": 0.1503, "tau": 0.1087, "auroc": 0.5318}, "EM": {"rho": 0.2587, "tau": 0.1966, "auroc": 0.7174}, "voting_conf": {"rho": 0.4053, "tau": 0.3042, "auroc": 0.6967}}, "conditional": {"SJ": {"rho": 0.2718, "tau": null, "auroc": 0.6565}, "FK": {"rho": 0.1472, "tau": null, "auroc": 0.5866}, "logprob": {"rho": 0.081, "tau": null, "auroc": 0.5129}, "EM": {"rho": 0.3165, "tau": null, "auroc": 0.7244}, "voting_conf": {"rho": 0.3078, "tau": null, "auroc": 0.6714}}, "greedy_f1": 0.6607, "oracle_f1": 0.7781, "n_full": 529, "n_cond": 478}, "re": {"full": {"SJ": {"rho": 0.2748, "tau": 0.2102, "auroc": 0.7244}, "FK": {"rho": 0.3027, "tau": 0.2337, "auroc": 0.691}, "logprob": {"rho": 0.3163, "tau": 0.233, "auroc": 0.6313}, "EM": {"rho": 0.1681, "tau": 0.1275, "auroc": 0.7697}, "voting_conf": {"rho": 0.384, "tau": 0.2965, "auroc": 0.7337}}, "conditional": {"SJ": {"rho": 0.3461, "tau": null, "auroc": 0.7233}, "FK": {"rho": 0.1969, "tau": null, "auroc": 0.6684}, "logprob": {"rho": 0.0888, "tau": null, "auroc": 0.5556}, "EM": {"rho": 0.4969, "tau": null, "auroc": 0.819}, "voting_conf": {"rho": 0.3433, "tau": null, "auroc": 0.7003}}, "greedy_f1": 0.4319, "oracle_f1": 0.5775, "n_full": 397, "n_cond": 251}}
591	
592	=== exp_018_llama_scierc_seed456 ===
593	status: DONE
594	hypothesis: 
595	conclusion: killed
596	created_at: "2026-05-15T06:07:15.150Z"
597	updated_at: "2026-05-15T06:22:40.868Z"
598	notes: "SUPERSEDED by exp_018_llama_scierc_seed456_r1024 (D066). Original data was re-analysis of exp_007_llama_seed456, not independent inference. Fresh rerun with explicit max_tokens=1024 now canonical."
599	
600	=== exp_018_llama_scierc_seed456_r1024 ===
601	status: DONE
602	hypothesis: LLaMA SciERC seed=456 (max_tokens=1024): multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.
603	conclusion: success
604	created_at: "2026-05-15T06:12:43.492Z"
605	updated_at: "2026-05-18T20:50:04.988Z"
606	metrics: {"degen_rate": 0.2741, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "ner_greedy_f1": 0.6597, "ner_oracle_f1": 0.7683, "ner_oracle_headroom": 0.1086, "ner_cond_rho_fk": 0.1472, "ner_cond_rho_sj": 0.2718, "ner_cond_rho_logprob": 0.083, "ner_logprob_auroc_cond": 0.5485, "re_greedy_f1": 0.4338, "re_oracle_f1": 0.5834, "re_oracle_headroom": 0.1496, "re_cond_rho_fk": 0.2107, "re_cond_rho_sj": 0.3898, "re_cond_rho_logprob": 0.1252, "re_logprob_auroc_cond": 0.6119, "ner_structural_beats_logprob": true, "re_structural_beats_logprob": true}
607	
608	=== exp_018_qwen_scierc_seed123 ===
609	status: DONE
610	hypothesis: Qwen SciERC seed=123: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.
611	conclusion: success
612	created_at: "2026-05-15T06:07:12.747Z"
613	updated_at: "2026-05-18T20:47:49.306Z"
614	metrics: {"degen_rate": 0.172, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
615	
616	=== exp_018_qwen_scierc_seed456 ===
617	status: DONE
618	hypothesis: Qwen SciERC seed=456: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.
619	conclusion: success
620	created_at: "2026-05-15T06:07:13.570Z"
621	updated_at: "2026-05-18T20:47:50.032Z"
622	metrics: {"degen_rate": 0.2042, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
623	
624	=== exp_019_supervised_verifier ===
625	status: DONE
626	hypothesis: 
627	conclusion: killed
628	created_at: "2026-05-15T10:08:54.395Z"
629	updated_at: "2026-05-15T12:40:53.995Z"
630	notes: "Cancelled by Director: DDL risk too high (3-4 days for implementation+training+eval+paper), scope creep for analytical paper, free-form ablation already provides sufficient mechanistic evidence"
631	
632	=== exp_020_fewnerd_smoke ===
633	status: DONE
634	hypothesis: 1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST.
635	conclusion: success
636	created_at: "2026-05-16T10:29:25.272Z"
637	updated_at: "2026-05-16T16:33:59.109Z"
638	metrics: {"final_loss": 0.031, "total_steps": 8236, "training_time": "5h54m", "pilot_greedy_f1": 0.8037, "pilot_instances": 200, "merged_model_path": "checkpoints/qwen3-8b-fewnerd-merged"}
639	
640	=== exp_021_fewnerd_full ===
641	status: DONE
642	hypothesis: Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics.
643	conclusion: success
644	created_at: "2026-05-16T16:33:44.079Z"
645	updated_at: "2026-05-17T02:55:45.560Z"
646	metrics: {"total_steps": 6177, "train_loss": 0.048, "eval_loss": 0.0275, "train_runtime": "3h57m", "epochs": 3, "final_checkpoint": "output/exp_021_fewnerd_full/checkpoint-6177", "adapter_path": "output/exp_021_fewnerd_full/adapter_model.safetensors", "inference_instances": 37648, "inference_filtered": 32565, "inference_n_samples": 8, "greedy_macro_f1": 0.7478, "oracle_macro_f1": 0.8719, "headroom": 0.124, "zero_f1_rate": 0.119, "degeneracy_rate": 0.101, "lp_within_range_mean": 0.0879, "lp_within_range_median": 0.0662, "lp_global_rho": 0.4215, "lp_cond_rho": 0.4225, "sj_global_rho": 0.3002, "sj_cond_rho": 0.2937, "fk_global_rho": 0.3132, "fk_cond_rho": 0.3093, "em_global_rho": 0.2871, "em_cond_rho": 0.271, "vc_global_rho": 0.3858, "vc_cond_rho": 0.3234, "lp_selection_delta_pp": 1.36, "vc_selection_delta_pp": -1.79, "sj_selection_delta_pp": -2.14, "fk_selection_delta_pp": -2.26, "em_selection_delta_pp": -3.85, "lp_bootstrap_ci_95_pp": [1.18, 1.53], "lp_sample_auroc": 0.5782, "vc_sample_auroc": 0.5354, "fk_sample_auroc": 0.521, "sj_sample_auroc": 0.5197, "em_sample_auroc": 0.5137, "scenario": "A_partial", "note": "Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics."}
647	parent: "exp_020_fewnerd_smoke"
648	
649	=== exp_021_fewnerd_n8_seed123 ===
650	status: DONE
651	hypothesis: Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.
652	conclusion: success
653	created_at: "2026-05-18T22:03:16.735Z"
654	updated_at: "2026-05-18T22:04:49.470Z"
655	metrics: {"degen_rate": 0.1312, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "instance_count": 37648, "n_valid": 32565, "n_gold_empty": 5083, "ner_greedy_f1": 0.7885, "ner_oracle_f1": 0.8892, "rho_fk_ner": 0.1602, "rho_sj_ner": 0.3083, "sample_f1_pct_zero": 20.39}
656	
657	=== exp_021_fewnerd_n8_seed456 ===
658	status: DONE
659	hypothesis: Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.
660	conclusion: success
661	created_at: "2026-05-18T22:03:17.992Z"
662	updated_at: "2026-05-18T22:04:50.774Z"
663	metrics: {"degen_rate": 0.1212, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "instance_count": 37648, "n_valid": 32565, "n_gold_empty": 5083, "ner_greedy_f1": 0.7888, "ner_oracle_f1": 0.881, "rho_fk_ner": 0.1632, "rho_sj_ner": 0.313, "sample_f1_pct_zero": 19.32}
664	
665	=== exp_022_seed789 ===
666	status: DONE
667	hypothesis: 3rd seed SciERC inference (seed=789) with ft_002_v2 (Qwen3-8B). N=8, T=1.0, joint NER+RE, logprobs collected. Complements seed42 (exp_012_rerun_1024) and seed123/456 for multi-seed analysis.
668	conclusion: success
669	created_at: "2026-05-16T10:08:27.375Z"
670	updated_at: "2026-05-17T02:55:49.870Z"
671	parent: "exp_012_rerun_1024"
672	
673	=== exp_023_lora_rank8 ===
674	status: DONE
675	hypothesis: LoRA rank=8 ablation on SciERC: test if reduced model capacity (rank 8 vs 32) changes signal effectiveness ranking or correlation-selection gap pattern. Verifies findings are not rank-specific artifacts.
676	conclusion: success
677	created_at: "2026-05-16T10:29:59.501Z"
678	updated_at: "2026-05-17T02:55:50.540Z"
679	metrics: {"train_loss": 0.1018, "eval_loss": 0.0776, "train_runtime": "28m45s", "ner_full": {"n": 529, "greedy_f1": 0.6397, "oracle_f1": 0.7998, "oracle_headroom": 0.1601, "degeneracy_rate": 0.072, "SJ_rho": 0.3649, "FK_rho": 0.2838, "VC_rho": 0.394, "EM_rho": 0.2562, "LP_rho": 0.2105, "SJ_auroc": 0.689, "FK_auroc": 0.6002, "VC_auroc": 0.6886, "EM_auroc": 0.7265, "LP_auroc": 0.6054, "sel_SJ": 0.6306, "sel_FK": 0.6265, "sel_VC": 0.5919, "sel_EM": 0.6073, "sel_LP": 0.635}, "ner_cond": {"n": 477, "SJ_rho": 0.3056, "FK_rho": 0.1452, "VC_rho": 0.3191, "EM_rho": 0.3558, "LP_rho": 0.169}, "re_full": {"n": 397, "greedy_f1": 0.3712, "oracle_f1": 0.609, "oracle_headroom": 0.2378, "degeneracy_rate": 0.217, "SJ_rho": 0.2244, "FK_rho": 0.3448, "VC_rho": 0.3617, "EM_rho": 0.068, "LP_rho": 0.2737, "SJ_auroc": 0.7092, "FK_auroc": 0.6469, "VC_auroc": 0.7533, "EM_auroc": 0.7306, "LP_auroc": 0.6325, "sel_SJ": 0.3584, "sel_FK": 0.3498, "sel_VC": 0.3715, "sel_EM": 0.3291, "sel_LP": 0.3606}, "re_cond": {"n": 242, "SJ_rho": 0.3601, "FK_rho": 0.2343, "VC_rho": 0.3703, "EM_rho": 0.4613, "LP_rho": 0.1809}}
680	parent: "exp_012_rerun_1024"
681	
682	=== exp_024_claim_audit ===
683	status: DONE
684	hypothesis: Systematic cross-chapter numerical consistency audit: verify all quantitative claims in paper against source experiment data, catch stale values and cross-reference errors before submission.
685	conclusion: success
686	created_at: "2026-05-17T10:54:36.291Z"
687	updated_at: "2026-05-17T10:55:08.244Z"
688	metrics: {"consistent": 97, "errors": 1, "warnings": 5, "old_residuals_found": 0}
689	
690	=== exp_025_n32 ===
691	status: DONE
692	hypothesis: N=32 sample ablation on SciERC: test if increasing samples from 8→32 reduces degeneracy and improves selection F1, particularly for structural signals. Validates whether sample count is the bottleneck for signal effectiveness.
693	conclusion: success
694	created_at: "2026-05-16T13:38:26.420Z"
695	updated_at: "2026-05-17T02:55:46.212Z"
696	metrics: {"n_samples": 32, "degeneracy_pct": 4, "lp_range": 0.0781, "oracle_f1": 0.8412, "greedy_f1": 0.6615, "oracle_gap": 0.1797, "selection_f1_lp_delta": 0.54, "selection_f1_sj_delta": 0.16, "selection_f1_fk_delta": 0.6, "selection_f1_em_delta": 0.68, "selection_f1_vc_delta": -5.21, "best_signal": "EM", "best_delta": 0.68, "metric_space": "micro_f1_filtered_529inst", "note": "corrected via n_ablation_fixed.py, greedy from inst['greedy'] field"}
697	parent: "exp_012_rerun_1024"
698	
699	=== exp_026_T05 ===
700	status: DONE
701	hypothesis: T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, validating that degeneracy is regime-dependent on sampling temperature.
702	conclusion: success
703	created_at: "2026-05-17T09:38:28.066Z"
704	updated_at: "2026-05-18T20:48:16.286Z"
705	metrics: {"degen_rate": 0.414, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "lp_range_mean": 0.022, "lp_range_std": 0.021, "within_instance_rho_mean": 0.1306, "within_instance_rho_median": 0.2182, "within_instance_rho_valid_pct": 0.597, "greedy_f1": 0.617, "oracle_f1": 0.71, "lp_sel_f1": 0.622, "sj_sel_f1": 0.622, "em_sel_f1": 0.619, "vc_sel_f1": 0.61, "sj_rho": 0.333, "fk_rho": 0.341, "lp_rho": 0.208, "vc_rho": 0.353, "sj_auroc": 0.644, "lp_auroc": 0.577}
706	
707	=== exp_026_T08 ===
708	status: DONE
709	hypothesis: T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal operating point for the selection mechanism.
710	conclusion: success
711	created_at: "2026-05-17T09:38:29.602Z"
712	updated_at: "2026-05-18T20:48:21.975Z"
713	metrics: {"degen_rate": 0.2382, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "lp_range_mean": 0.043, "lp_range_std": 0.042, "within_instance_rho_mean": 0.1701, "within_instance_rho_median": 0.2635, "within_instance_rho_valid_pct": 0.728, "greedy_f1": 0.616, "oracle_f1": 0.737, "lp_sel_f1": 0.627, "sj_sel_f1": 0.619, "em_sel_f1": 0.611, "vc_sel_f1": 0.603, "sj_rho": 0.378, "fk_rho": 0.34, "lp_rho": 0.212, "vc_rho": 0.352, "sj_auroc": 0.662, "lp_auroc": 0.571}
714	
715	=== exp_026_T12 ===
716	status: DONE
717	hypothesis: T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit.
718	conclusion: success
719	created_at: "2026-05-17T09:38:31.060Z"
720	updated_at: "2026-05-18T20:48:22.668Z"
721	metrics: {"degen_rate": 0.1493, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "lp_range_mean": 0.075, "lp_range_std": 0.059, "within_instance_rho_mean": 0.2245, "within_instance_rho_median": 0.3152, "within_instance_rho_valid_pct": 0.875, "greedy_f1": 0.62, "oracle_f1": 0.758, "lp_sel_f1": 0.621, "sj_sel_f1": 0.597, "em_sel_f1": 0.596, "vc_sel_f1": 0.582, "sj_rho": 0.384, "fk_rho": 0.386, "lp_rho": 0.182, "vc_rho": 0.342, "sj_auroc": 0.683, "lp_auroc": 0.566}
722	
723	=== exp_026_t05 ===
724	status: DONE
725	hypothesis: Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phenomenon.
726	conclusion: success
727	created_at: "2026-05-16T12:19:35.753Z"
728	updated_at: "2026-05-18T20:48:23.339Z"
729	metrics: {"temperature": 0.5, "task": "T-ablation", "degen_rate": 0.414, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
730	parent: "exp_012_rerun_1024"
731	
732	=== exp_026_t05_scierc ===
733	status: DONE
734	hypothesis: Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs
735	conclusion: success
736	created_at: "2026-05-18T15:28:34.135Z"
737	updated_at: "2026-05-18T15:30:28.965Z"
738	
739	=== exp_026_t05_seed123 ===
740	status: DONE
741	hypothesis: Temperature ablation (T=0.5, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
742	conclusion: success
743	created_at: "2026-05-18T22:05:35.201Z"
744	updated_at: "2026-05-18T22:07:13.198Z"
745	metrics: {"ner_greedy_f1": 0.6611, "ner_oracle_f1": 0.7444, "rho_sj_ner": 0.3133, "sample_f1_pct_zero": 10.09, "instance_count": 551, "n_valid": 529}
746	
747	=== exp_026_t05_seed456 ===
748	status: DONE
749	hypothesis: Temperature ablation (T=0.5, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
750	conclusion: success
751	created_at: "2026-05-18T22:05:36.536Z"
752	updated_at: "2026-05-18T22:07:14.675Z"
753	metrics: {"ner_greedy_f1": 0.6639, "ner_oracle_f1": 0.7437, "rho_sj_ner": 0.3279, "sample_f1_pct_zero": 10.28, "instance_count": 551, "n_valid": 529}
754	
755	=== exp_026_t08 ===
756	status: DONE
757	hypothesis: Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic rather than temperature-driven.
758	conclusion: success
759	created_at: "2026-05-16T12:57:46.027Z"
760	updated_at: "2026-05-18T20:48:24.112Z"
761	metrics: {"temperature": 0.8, "task": "T-ablation", "degen_rate": 0.2382, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
762	parent: "exp_012_rerun_1024"
763	
764	=== exp_026_t08_scierc ===
765	status: DONE
766	hypothesis: Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature
767	conclusion: success
768	created_at: "2026-05-18T15:28:36.084Z"
769	updated_at: "2026-05-18T15:30:31.219Z"
770	
771	=== exp_026_t08_seed123 ===
772	status: DONE
773	hypothesis: Temperature ablation (T=0.8, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
774	conclusion: success
775	created_at: "2026-05-18T22:05:37.454Z"
776	updated_at: "2026-05-18T22:07:16.089Z"
777	metrics: {"ner_greedy_f1": 0.6607, "ner_oracle_f1": 0.7714, "rho_sj_ner": 0.3893, "sample_f1_pct_zero": 11.22, "instance_count": 551, "n_valid": 529}
778	
779	=== exp_026_t08_seed456 ===
780	status: DONE
781	hypothesis: Temperature ablation (T=0.8, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
782	conclusion: success
783	created_at: "2026-05-18T22:05:38.605Z"
784	updated_at: "2026-05-18T22:07:17.604Z"
785	metrics: {"ner_greedy_f1": 0.6641, "ner_oracle_f1": 0.7694, "rho_sj_ner": 0.3771, "sample_f1_pct_zero": 11.79, "instance_count": 551, "n_valid": 529}
786	
787	=== exp_026_t10_seed123 ===
788	status: DONE
789	hypothesis: Temperature ablation (T=1.0, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
790	conclusion: success
791	created_at: "2026-05-18T22:05:40.599Z"
792	updated_at: "2026-05-18T22:07:20.459Z"
793	metrics: {"ner_greedy_f1": 0.6633, "ner_oracle_f1": 0.7777, "rho_sj_ner": 0.3809, "sample_f1_pct_zero": 12.59, "instance_count": 551, "n_valid": 529}
794	
795	=== exp_026_t10_seed42 ===
796	status: DONE
797	hypothesis: Temperature ablation (T=1.0, seed=42) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
798	conclusion: success
799	created_at: "2026-05-18T22:05:39.473Z"
800	updated_at: "2026-05-18T22:07:19.035Z"
801	metrics: {"ner_greedy_f1": 0.6617, "ner_oracle_f1": 0.7798, "rho_sj_ner": 0.3598, "sample_f1_pct_zero": 12.9, "instance_count": 551, "n_valid": 529}
802	
803	=== exp_026_t10_seed456 ===
804	status: DONE
805	hypothesis: Temperature ablation (T=1.0, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
806	conclusion: success
807	created_at: "2026-05-18T22:05:41.840Z"
808	updated_at: "2026-05-18T22:07:21.767Z"
809	metrics: {"ner_greedy_f1": 0.6621, "ner_oracle_f1": 0.7754, "rho_sj_ner": 0.3921, "sample_f1_pct_zero": 12.97, "instance_count": 551, "n_valid": 529}
810	
811	=== exp_026_t12 ===
812	status: DONE
813	hypothesis: Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structural signal effectiveness.
814	conclusion: success
815	created_at: "2026-05-16T13:18:18.780Z"
816	updated_at: "2026-05-18T20:48:24.965Z"
817	metrics: {"temperature": 1.2, "task": "T-ablation", "degen_rate": 0.1493, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
818	parent: "exp_012_rerun_1024"
819	
820	=== exp_026_t12_scierc ===
821	status: DONE
822	hypothesis: Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality
823	conclusion: success
824	created_at: "2026-05-18T15:28:36.812Z"
825	updated_at: "2026-05-18T15:30:33.407Z"
826	
827	=== exp_026_t12_seed123 ===
828	status: DONE
829	hypothesis: Temperature ablation (T=1.2, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
830	conclusion: success
831	created_at: "2026-05-18T22:05:42.754Z"
832	updated_at: "2026-05-18T22:07:23.135Z"
833	metrics: {"ner_greedy_f1": 0.6595, "ner_oracle_f1": 0.7895, "rho_sj_ner": 0.359, "sample_f1_pct_zero": 13.99, "instance_count": 551, "n_valid": 529}
834	
835	=== exp_026_t12_seed456 ===
836	status: DONE
837	hypothesis: Temperature ablation (T=1.2, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
838	conclusion: success
839	created_at: "2026-05-18T22:05:43.694Z"
840	updated_at: "2026-05-18T22:07:24.547Z"
841	metrics: {"ner_greedy_f1": 0.6637, "ner_oracle_f1": 0.7821, "rho_sj_ner": 0.3995, "sample_f1_pct_zero": 14.08, "instance_count": 551, "n_valid": 529}
842	
843	=== exp_027_fewnerd_n16 ===
844	status: DONE
845	hypothesis: LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.
846	conclusion: success
847	created_at: "2026-05-17T05:28:57.036Z"
848	updated_at: "2026-05-18T20:48:58.455Z"
849	metrics: {"LP_delta_pp": 1.88, "LP_delta_95CI": [1.41, 2.37], "degen_rate": 0.0706, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "greedy_f1": 0.7478, "lp_sel_f1": 0.7666, "oracle_f1": 0.902, "headroom_pp": 15.42, "all_8_types_positive": true, "n_instances": 5000, "N_samples": 16, "bootstrap_p": "<0.001"}
850	
851	=== exp_027_mlp_verifier ===
852	status: DONE
853	hypothesis: MLP/RF等非线性模型能否通过组合5个QE信号(LP,SJ,FK,EM,VC)超越LR，或通过cross-signal interactions提取额外信息，从而缩小selection gap
854	conclusion: negative
855	created_at: "2026-05-18T06:39:22.524Z"
856	updated_at: "2026-05-18T06:41:51.069Z"
857	metrics: {"lr_auroc": 0.6522, "mlp_auroc": 0.6381, "rf_auroc": 0.5868, "mlp_15feat_auroc": 0.6341, "lr_sel_f1": 0.6406, "mlp_sel_f1": 0.6278, "greedy_f1": 0.6441, "oracle_f1": 0.8231, "best_single_signal_auroc": 0.6476, "feature_bottleneck_confirmed": true}
858	
859	=== exp_028 ===
860	status: DONE
861	hypothesis: Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training.
862	conclusion: negative
863	created_at: "2026-05-17T07:35:39.447Z"
864	updated_at: "2026-05-17T20:26:59.399Z"
865	metrics: {"degeneracy_cf1_gold": 0.313, "greedy_f1": 0.7773, "lp_sel_f1": 0.7835, "lp_sel_delta_pp": 0.62, "oracle_f1": 0.8723, "within_instance_rho": 0.4066, "train_loss": 0.0189, "eval_loss": 0.0311}
866	
867	=== exp_028_entity_token_lp ===
868	status: DONE
869	hypothesis: Full-sequence mean LP underperforms as a quality signal because format/schema tokens dilute the entity-relevant logprob signal; isolating entity-only tokens should yield higher QE correlation and selection F1.
870	conclusion: negative
871	created_at: "2026-05-18T18:22:18.594Z"
872	updated_at: "2026-05-18T18:23:06.601Z"
873	metrics: {"greedy_f1": 0.643, "oracle_f1": 0.7845, "full_lp_global_rho": 0.2971, "entity_text_type_lp_global_rho": 0.4401, "full_lp_selection_f1": 0.6465, "entity_text_type_lp_selection_f1": 0.6357, "dilution_ratio": 0.32, "full_lp_within_range_median": 0.0402, "entity_text_type_within_range_median": 0.1346, "schema_only_within_range_median": 0.0089}
874	
875	=== exp_028_fewnerd_5epoch ===
876	status: DONE
877	hypothesis: Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.
878	conclusion: negative
879	created_at: "2026-05-17T07:53:12.913Z"
880	updated_at: "2026-05-17T20:29:42.274Z"
881	metrics: {"degeneracy_cf1_gold": 0.3133, "greedy_f1": 0.7773, "lp_sel_delta_pp": 0.624, "lp_sel_f1": 0.7835, "oracle_f1": 0.8723, "within_instance_rho_mean": 0.4066, "within_instance_rho_median": 0.6151}
882	
883	=== exp_029a ===
884	status: DONE
885	hypothesis: Training convergence modulates degeneracy across datasets. SciERC 3-epoch training should produce lower degeneracy than 5-epoch baseline (17.8%), confirming epoch confound is not Few-NERD-specific.
886	conclusion: success
887	created_at: "2026-05-17T23:32:17.191Z"
888	updated_at: "2026-05-18T22:05:44.959Z"
889	parent: "ft_002_v2"
890	metrics: {"degen_rate": 0.064, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
891	
892	=== exp_029b ===
893	status: DONE
894	hypothesis: Training convergence modulates degeneracy across datasets. SciERC 10-epoch training should produce higher degeneracy than 5-epoch baseline (17.8%), confirming monotonic epoch-degeneracy relationship across datasets.
895	conclusion: success
896	created_at: "2026-05-17T23:32:18.543Z"
897	updated_at: "2026-05-18T22:05:45.856Z"
898	parent: "ft_002_v2"
899	metrics: {"degen_rate": 0.478, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
900	
901	=== exp_030_conll_t12 ===
902	status: DONE
903	hypothesis: CoNLL T=1.2 temperature ablation: test if higher temperature reduces degeneracy on CoNLL as observed on SciERC
904	conclusion: killed
905	created_at: "2026-05-18T20:24:47.839Z"
906	updated_at: "2026-05-19T00:30:12.698Z"
907	notes: "T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient"
908	
909	=== exp_031_fewnerd_t12 ===
910	status: DONE
911	hypothesis: FewNERD T=1.2 temperature ablation: test if higher temperature reduces degeneracy on FewNERD as observed on SciERC
912	conclusion: killed
913	created_at: "2026-05-18T20:04:12.040Z"
914	updated_at: "2026-05-19T00:30:14.652Z"
915	notes: "T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient"
916	
917	=== exp_a2_degen_regression ===
918	status: PREPARING
919	hypothesis: Degeneracy rate is primarily driven by task difficulty (dataset entropy ceiling) rather than model capability, with a positive correlation between base F1 and degeneracy — easy tasks with high F1 produce degenerate outputs because the model has already converged.
920	conclusion: success
921	created_at: "2026-05-20T10:13:37.615Z"
922	updated_at: "2026-05-20T10:13:55.891Z"
923	metrics: {"n_points": 30, "linear_r2": 0.414, "quadratic_r2": 0.592, "spearman_rho": 0.519, "spearman_p": 0.0033, "linear_coeff": "degen = 129.5 × F1 - 56.9", "key_finding": "degeneracy driven by dataset difficulty (entropy ceiling), not model capability"}
924	
925	=== exp_adaptive_sampling_budget ===
926	status: PREPARING
927	hypothesis: Confidence-aware adaptive sampling budget allocation (fewer samples for high-confidence instances, full N=8 for low-confidence) can recover nearly all SC F1 gains while saving 40-50% of inference cost, because high-confidence instances already have low diversity and gain nothing from additional samples.
928	conclusion: success
929	created_at: "2026-05-20T09:29:22.761Z"
930	updated_at: "2026-05-20T09:29:41.158Z"
931	metrics: {"model": "Qwen3-8B FT", "fewnerd": {"n_instances": 37648, "greedy_f1": 0.7884, "uniform_n8_f1": 0.7819, "best_adaptive": "h1_l8", "best_adaptive_f1": 0.7849, "best_delta_vs_u8": "+0.30pp", "sample_savings": "43.8%", "note": "Greedy > U8; adaptive h1/l8 best: greedy for high-conf, N=8 SC for low-conf"}, "scierc": {"n_instances": 551, "greedy_f1": 0.6592, "uniform_n8_f1": 0.6712, "best_adaptive": "top67%_h2_l8", "best_adaptive_f1": 0.6707, "best_delta_vs_u8": "-0.05pp", "sample_savings": "50.2%", "note": "U8 > Greedy; top67% h2/l8 saves 50% with negligible loss"}}
932	notes: "B7 adaptive sampling budget analysis on Qwen3-8B FT. Key findings: (1) FewNERD: greedy already beats uniform N=8 SC (+0.65pp), adaptive h1/l8 is optimal (+0.30pp vs U8, saves 43.8% samples); (2) SciERC: U8 beats greedy (+1.20pp), top67% h2/l8 saves 50% with only -0.05pp loss. Practical implication: confidence-gated sampling can halve inference cost. Artifacts: vc_8b_qwen3_ft_results, sj_8b_qwen3_ft_results (registered by worker)."
933	
934	=== exp_adaptive_temperature ===
935	status: DONE
936	hypothesis: Adjusting sampling temperature based on instance-level confidence indicators can improve output diversity-quality tradeoff
937	conclusion: negative
938	created_at: "2026-05-18T19:59:52.771Z"
939	updated_at: "2026-05-18T20:01:42.646Z"
940	
941	=== exp_b2_entity_verifier ===
942	status: PREPARING
943	hypothesis: An XGBoost/LightGBM entity-level verifier trained on agreement_count, VC, LP features can predict whether entity candidates are in gold annotations, enabling post-hoc filtering or score-weighted construction that improves over greedy baseline, with cross-dataset generalization from CoNLL+SciERC to FewNERD+WNUT.
944	conclusion: success
945	created_at: "2026-05-20T10:13:41.037Z"
946	updated_at: "2026-05-20T10:14:00.616Z"
947	metrics: {"n_entities": 122984, "n_configs": 13, "train_entities": 44486, "test_entities": 78498, "xgb_cv_auc": 0.9273, "lgb_cv_auc": 0.9254, "xgb_test_auc": 0.8282, "lgb_test_auc": 0.8335, "top_features": {"vc": 0.5296, "agreement_count": 0.2504, "dataset_enc": 0.06}, "path_a_lgb_f1": 0.7336, "greedy_f1": 0.7321, "path_a_beats_greedy": true, "path_b_xgb_train_f1": 0.8122}
948	
949	=== exp_ccs_selection ===
950	status: DONE
951	hypothesis: Three-stage cascaded selection (degen→greedy, low-LP-range→entity MV, high-LP-range→LP) can outperform single-strategy selection by adapting to local confidence patterns
952	conclusion: negative
953	created_at: "2026-05-18T19:59:48.671Z"
954	updated_at: "2026-05-18T20:01:39.128Z"
955	
956	=== exp_cross_model_consistency ===
957	status: PREPARING
958	hypothesis: Pooling samples from two different fine-tuned models (Qwen3-8B + LLaMA-8B) for entity construction significantly outperforms single-model construction because cross-model diversity breaks model-specific mode collapse, reducing degeneracy and providing complementary error patterns that improve consensus quality.
959	conclusion: success
960	created_at: "2026-05-20T09:30:47.928Z"
961	updated_at: "2026-05-20T09:31:04.851Z"
962	metrics: {"dataset": "SciERC", "model_a": "Qwen3-8B FT", "model_b": "LLaMA-8B FT", "pure_qwen": {"degen": 0.1, "greedy_f1": 0.7478, "uniform_f1": 0.7499, "vc_f1": 0.7448, "uni_delta_pp": "+0.21", "vc_delta_pp": "-0.30"}, "pure_llama": {"degen": 0.234, "greedy_f1": 0.7841, "uniform_f1": 0.7873, "vc_f1": 0.7869, "uni_delta_pp": "+0.33", "vc_delta_pp": "+0.28"}, "mixed_4q4l": {"degen": 0.116, "uniform_f1": 0.7916, "vc_f1": 0.7898, "uni_delta_vs_qwen_greedy_pp": "+4.37", "vc_delta_vs_qwen_greedy_pp": "+4.20", "mixed_vs_pure_llama_uniform_pp": "+0.42", "mixed_vs_pure_llama_uniform_p": 0, "mixed_vs_pure_llama_uniform_ci": "[0.27, 0.58]", "mixed_vs_pure_llama_vc_pp": "+0.29", "mixed_vs_pure_llama_vc_p": 0.0001}}
963	notes: "B5 cross-model consistency on SciERC NER. Mixed pool (4 Qwen + 4 LLaMA) significantly outperforms pure LLaMA construction (+0.42pp uniform, p=0.000, CI [0.27,0.58]). Cross-model diversity reduces degeneracy (11.6% vs LLaMA 23.4%). Most of the +4.37pp ΔF1 vs Qwen greedy comes from LLaMA being stronger (greedy 0.784 vs 0.748), but the +0.42pp vs pure LLaMA is genuine cross-model diversity gain. Supports diversity hypothesis: different models make complementary errors → better consensus."
964	
965	=== exp_dgec_heterogeneous_t ===
966	status: PREPARING
967	hypothesis: Mixing samples from T=0.7 and T=1.0 significantly reduces degeneracy compared to single-T sampling (by breaking temperature-induced mode collapse), enabling entity construction to achieve significant ΔF1 improvement even in configs where single-T construction was n.s. due to high degeneracy.
968	conclusion: 
969	created_at: "2026-05-20T08:37:59.963Z"
970	updated_at: "2026-05-20T08:49:58.009Z"
971	metrics: {"dataset": "SciERC", "n_instances": 529, "t07_degen": 0.2231, "t10_degen": 0.1235, "mixed_degen": 0.1701, "mixed_uniform_f1": 0.6584, "mixed_vc_f1": 0.6609, "cross_pool_uniform_delta": "+0.006 (1/3 seeds sig)", "cross_pool_vc_delta": "+0.004 (1/3 seeds sig)", "t08_t10_result": "harmful (degen increased)", "conclusion_preliminary": "partially_supported"}
972	notes: "Hypothesis partially supported. T=0.7+T=1.0 mixed pool reduces degen (22.3%→17.0%) and improves construction (VC 3/3 seeds sig vs greedy), but cross-pool comparison (mixed vs T=1.0 alone) only 1/3 seeds significant. T gap matters: ΔT=0.2 (T=0.8+T=1.0) harmful, ΔT=0.3 (T=0.7+T=1.0) beneficial. VC weighting confirmed cross-T compatible. Awaiting Director conclusion classification."
973	
974	=== exp_dgec_sj_construction ===
975	status: PREPARING
976	hypothesis: SJ-weighted entity construction serves as control for VC — if SJ (soft entity overlap) works as well as VC (exact match consensus), any stronger QE signal suffices for construction; if VC specifically outperforms SJ, exact-match consensus has a unique advantage over soft similarity for entity-level selection.
977	conclusion: negative
978	created_at: "2026-05-20T08:37:58.013Z"
979	updated_at: "2026-05-20T09:26:30.567Z"
980	metrics: {"total_configs": 26, "significant_positive": 1, "significant_negative": 15, "not_significant": 10, "best_config": "scierc/72b/zs +2.0pp p=0.001", "worst_config": "fewnerd/8b_qwen3/ft mean -1.48pp all seeds p=1.0", "qwen3_8b_ft_supplement": {"configs": 9, "sig+": 0, "sig-": 6, "ns": 3, "fewnerd_mean_delta": -1.48, "scierc_mean_delta": -0.4, "conll_mean_delta": -0.5, "note": "SJ fully negative on Qwen3-8B FT — consistent with Qwen2.5-7B FT pattern"}, "m030_all_passed": true}
981	notes: "COMPLETE (26 configs). SJ-weighted construction: 1 sig+ / 15 sig- / 10 ns. Qwen3-8B FT supplement (9 configs): 0+/6-/3ns — fully negative, consistent with 7B FT pattern. FewNERD -1.48pp mean (all seeds p=1.0). Definitively answers control question: NOT any stronger QE signal works for construction. SJ introduces noise at entity level. Only exception: SciERC 72B ZS (lowest precision, lowest degeneracy). Closed per D170/D171."
982	
983	=== exp_dgec_vc_construction ===
984	status: PREPARING
985	hypothesis: VC-weighted entity construction outperforms greedy and LP-weighted construction across configs because Vote Count is a more direct quality estimator for structured outputs — it measures exact-match consensus without relying on model-internal log probabilities. Especially effective in high-degeneracy regimes where LP compression makes LP-weighting uninformative.
986	conclusion: negative
987	created_at: "2026-05-20T08:37:55.968Z"
988	updated_at: "2026-05-20T09:26:29.776Z"
989	metrics: {"total_configs": 28, "significant_positive": 9, "significant_negative": 10, "not_significant": 9, "by_dataset": {"fewnerd": {"configs": 11, "sig+": 5, "sig-": 5, "ns": 1, "mean_delta_pp": -0.12}, "wnut17": {"configs": 3, "sig+": 2, "sig-": 0, "ns": 1, "mean_delta_pp": 0.92}, "scierc": {"configs": 7, "sig+": 2, "sig-": 0, "ns": 5, "mean_delta_pp": 0.62}, "conll": {"configs": 7, "sig+": 0, "sig-": 5, "ns": 2, "mean_delta_pp": -0.33}}, "qwen3_8b_ft_supplement": {"configs": 9, "sig+": 3, "sig-": 3, "ns": 3, "best": "SciERC s42 +1.40pp p=0.017", "worst": "CoNLL s456 -0.54pp p=0.998", "note": "VC inconsistent on LP-success configs; seed-dependent on FewNERD; CoNLL all negative due to high degeneracy"}, "m030_all_passed": true}
990	notes: "COMPLETE (28 configs). VC-weighted construction: 9 sig+ / 10 sig- / 9 ns. Qwen3-8B FT supplement (9 configs): 3+/3-/3ns — VC inconsistent even on LP-success configs. SciERC s42 best (+1.40pp) but cross-seed unstable. CoNLL all negative (high degeneracy). WNUT17/SciERC lean positive but not robust. Key answer: VC does NOT reliably improve where LP already works — seed-dependent, dataset-dependent. DGEC unified method goal (70-80% configs) unreachable at 32% (9/28). Closed per D170/D171."
991	
992	=== exp_diagnostic_calibration ===
993	status: DONE
994	hypothesis: A 3-indicator regression model (degeneracy rate, LP-F1 correlation, LP range) can quantitatively predict the optimal LP selection delta for unseen instances
995	conclusion: negative
996	created_at: "2026-05-18T19:59:56.064Z"
997	updated_at: "2026-05-18T20:01:44.364Z"
998	
999	=== exp_e1_signal_routing ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "150250d1-8ed4-4a4d-8a05-cfbff069b65f",
  "isSidechain": true,
  "promptId": "9d5a8dbf-14d3-41c1-a18a-ef8acd67e6cb",
  "agentId": "a97ebe3840b34757a",
  "type": "user",
  "uuid": "97f40d6f-8cd9-43cd-91c7-741865d848bd",
  "sourceToolAssistantUUID": "150250d1-8ed4-4a4d-8a05-cfbff069b65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T10:44:42.838Z_

<details open><summary>🔧 Tool call — Read · `toolu_017JrQJxaAsLczjAYH89xo2Q`</summary>

```json
{
  "file_path": "/tmp/registry_full.txt",
  "offset": 999,
  "limit": 455
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97f40d6f-8cd9-43cd-91c7-741865d848bd",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
  "requestId": "req_011CbDgefzdpq1dn4Mx2hyyz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8913e3c0-bf05-450d-af2b-c81bbccac7c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QgoUoiMVPtZde7MUALnHgn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21086,
      "cache_read_input_tokens": 55240,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21086
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 55240,
          "cache_creation_input_tokens": 21086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21086,
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

_source line 19 · 2026-05-20T10:44:43.138Z_

<details><summary>↩ Tool result · `toolu_017JrQJxaAsLczjAYH89xo2Q`</summary>

```text
999	=== exp_e1_signal_routing ===
1000	status: PREPARING
1001	hypothesis: A config-level signal router (RF/LR) can predict the optimal construction signal per config from features (degeneracy_rate, base_f1, oracle_headroom), outperforming always-LP baseline. Router ΔF1 should exceed always-LP ΔF1.
1002	conclusion: success
1003	created_at: "2026-05-20T10:13:34.839Z"
1004	updated_at: "2026-05-20T10:13:52.098Z"
1005	metrics: {"n_configs": 16, "rf_loo_accuracy": 0.562, "router_avg_delta_f1": 0.39, "always_lp_delta_f1": 0.15, "oracle_delta_f1": 0.56, "top_features": ["oracle_headroom", "degeneracy_rate", "base_f1"], "label_dist": {"lp_selection": 6, "none": 5, "consensus_theta2n": 3, "consensus_lp_weighted": 1, "majority_vote": 1}}
1006	notes: "E1 signal routing. RF 56.2% LOO accuracy (below 60% target) but router ΔF1 +0.39pp > always-LP +0.15pp (2.6× improvement, target met). Low accuracy due to small n=16 and class imbalance. D176: appendix-only, not main claim."
1007	
1008	=== exp_entity_consensus ===
1009	status: DONE
1010	hypothesis: Constructing new output from N samples using entity frequency thresholds and LP-weighted decisions can capture complementary information that single-sample selection misses
1011	conclusion: negative
1012	created_at: "2026-05-18T19:59:50.628Z"
1013	updated_at: "2026-05-18T20:01:40.869Z"
1014	
1015	=== exp_entity_construction ===
1016	status: DONE
1017	hypothesis: Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.
1018	conclusion: success
1019	created_at: "2026-05-19T02:00:12.074Z"
1020	updated_at: "2026-05-19T02:40:17.571Z"
1021	metrics: {"n16_fair_cv": {"scierc_ner": {"cv_uniform_delta": "+1.35pp", "p_value": 0.018, "significant": true}, "conll_ner": {"cv_uniform_delta": "+0.10pp", "p_value": 0.303, "significant": false}, "fewnerd_ner": {"cv_uniform_delta": "+1.32pp", "p_value": 0, "significant": true}, "scierc_re": {"cv_uniform_delta": "+1.69pp", "p_value": 0.049, "significant": true}}, "n8_fair_cv": {"scierc_ner": {"uniform_confirm": "+1.54pp (p=0.023, sig)", "lp_weighted_confirm": "+1.67pp (p=0.004, sig)", "cv_uniform": "+1.12pp (p=0.057, borderline)"}, "conll_ner": {"cv_uniform": "-0.39pp (p=0.963, not sig)"}, "fewnerd_ner": {"lp_weighted_cv": "+0.88pp (p=0.000, sig)", "uniform_cv": "+0.32pp (p=0.003, sig)"}}, "adaptive_combination": "INVALIDATED - gold label leakage confirmed", "note": "5-fold CV, bootstrap B=10000, paired one-sided"}
1022	
1023	=== exp_entity_token_lp ===
1024	status: DONE
1025	hypothesis: Entity-token LP: test Discussion hypothesis (d) format-token dilution. Re-inference with per-token logprobs, then compute entity-only LP variance and selection F1. If entity-token LP compression is reduced → pilot remedy for LP selection. Also includes LP z-score normalization as zero-cost baseline. Addresses SF2+SF3 from Round 12.
1026	conclusion: negative
1027	created_at: "2026-05-16T05:39:44.631Z"
1028	updated_at: "2026-05-17T03:33:38.371Z"
1029	metrics: {"scierc_ner": {"greedy_f1": 0.643, "full_lp_sel_f1": 0.6465, "entity_lp_sel_f1": 0.6262, "oracle_f1": 0.7845, "entity_lp_delta_vs_full_lp": -0.0203}, "conll_ner": {"greedy_f1": 0.9065, "full_lp_sel_f1": 0.8989, "entity_lp_sel_f1": 0.8659, "oracle_f1": 0.948, "entity_lp_delta_vs_full_lp": -0.033}, "finding": "entity-token LP strictly worse than full-sequence LP; CoNLL entity tokens saturated (79.4% tied), SciERC entity tokens too sparse (5.3% of total)"}
1030	parent: "exp_012_rerun_1024"
1031	
1032	=== exp_epoch_dgs_analysis ===
1033	status: DONE
1034	hypothesis: DGS benefit is strictly monotonic with degeneracy rate: higher degeneracy → greater DGS improvement, validating that degeneracy rate is the key gating signal
1035	conclusion: success
1036	created_at: "2026-05-18T19:59:57.921Z"
1037	updated_at: "2026-05-18T20:01:46.134Z"
1038	
1039	=== exp_fewnerd_s789_n8 ===
1040	status: DONE
1041	hypothesis: FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime.
1042	conclusion: success
1043	created_at: "2026-05-18T23:17:34.011Z"
1044	updated_at: "2026-05-18T23:18:28.125Z"
1045	parent: "exp_029a"
1046	metrics: {"greedy_f1": 0.7478, "oracle_f1": 0.8714, "headroom_pp": 12.37, "degen_rate": 0.1177, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "instance_count": 37648, "n_valid": 32565, "lp_sel_f1": 0.7614, "lp_delta_pp": 1.36, "lp_rho_global": 0.1788, "lp_rho_cond": 0.176, "dgs_f1": 0.7621, "dgs_delta_pp": 1.43, "dgs_vs_lp_pp": 0.07, "best_signal": "LP", "four_seed_mean_greedy": 0.7481, "four_seed_mean_lp_delta_pp": 1.38, "four_seed_lp_delta_ci95": [1.32, 1.44]}
1047	
1048	=== exp_freeform_ablation ===
1049	status: DONE
1050	hypothesis: Free-form vs constrained decoding ablation on SciERC: test if removing JSON schema constraint changes LP variance distribution. If LP remains compressed under free-form, confirms compression is model-intrinsic not format-artifact.
1051	conclusion: negative
1052	created_at: "2026-05-15T09:42:22.868Z"
1053	updated_at: "2026-05-17T03:33:37.623Z"
1054	metrics: {"lp_std_ratio_free_vs_constrained": 0.97, "lp_range_ratio": 0.96, "tied_fraction_constrained": 0.597, "tied_fraction_freeform": 0.577, "ner_selection_gap_constrained": 0.0059, "ner_selection_gap_freeform": 0.0018, "re_selection_gap_constrained": -0.0068, "re_selection_gap_freeform": 0.0169, "parse_rate": 0.9995, "ner_vc_rho_constrained": 0.3792, "ner_vc_rho_freeform": 0.4089}
1055	parent: "exp_012_rerun_1024"
1056	
1057	=== exp_freeform_conll_4seed ===
1058	status: DONE
1059	hypothesis: Free-form CoNLL NER 4-seed ablation: verify LP compression is cross-dataset intrinsic (not SciERC-specific). 4 seeds × N=8, T=1.0 on CoNLL, compare LP range distribution with constrained decoding.
1060	conclusion: success
1061	created_at: "2026-05-16T02:45:17.133Z"
1062	updated_at: "2026-05-16T03:04:49.550Z"
1063	metrics: {"greedy_f1": "0.9035±0.0004", "oracle_f1": "0.9460±0.0023", "lp_range_median": "0.0581±0.0072", "rho_sj": "0.4606±0.0188", "rho_fk": "0.4372±0.0209", "rho_em": "0.4714±0.0168", "rho_vc": "0.4606±0.0138", "rho_lp": "0.3262±0.0120", "sel_f1_sj": "0.8994±0.0014", "sel_f1_vc": "0.9006±0.0026", "sel_f1_lp": "0.8958±0.0009", "seeds": [42, 123, 456, 789], "n_samples": 8, "temperature": 1, "instances": 2756, "gold_empty_filtered": 697}
1064	
1065	=== exp_freeform_seed123 ===
1066	status: DONE
1067	hypothesis: Free-form SciERC seed=123: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.
1068	conclusion: success
1069	created_at: "2026-05-15T17:14:47.765Z"
1070	updated_at: "2026-05-17T02:56:06.903Z"
1071	metrics: {"inference": {"n_instances": 551, "n_samples": 8, "total_samples": 4408, "total_parsed": 4406, "parse_rate_pct": 99.95, "elapsed_seconds": 228.1}, "freeform": {"selection_ner": {"greedy": 0.6194, "selected": 0.6222, "gap": 0.0028}, "selection_re": {"greedy": 0.2874, "selected": 0.305, "gap": 0.0176}, "logprob_variance": {"mean_std": 0.019881, "mean_range": 0.059864, "tied_pct": 57.7}, "qe_ner": {"n": 529, "SJ": {"rho": 0.384214, "auroc": 0.748728}, "FK": {"rho": 0.323956, "auroc": 0.766039}, "logprob": {"rho": 0.217297, "auroc": 0.701657}, "EM": {"rho": 0.326887, "auroc": 0.52533}, "voting_conf": {"rho": 0.407893, "auroc": 0.799676}}, "qe_re": {"n": 397, "SJ": {"rho": 0.272776, "auroc": 0.614056}, "FK": {"rho": 0.314429, "auroc": 0.678534}, "logprob": {"rho": 0.309673, "auroc": 0.70414}, "EM": {"rho": 0.137216, "auroc": 0.487342}, "voting_conf": {"rho": 0.316667, "auroc": 0.647442}}}, "constrained_ref": {"selection_ner": {"greedy": 0.6182, "selected": 0.6241, "gap": 0.0059}, "selection_re": {"greedy": 0.2913, "selected": 0.2845, "gap": -0.0068}}, "comparison": {"variance_ratio_std": 0.97, "variance_ratio_range": 0.96, "tied_reduction_pp": 2}}
1072	
1073	=== exp_freeform_seed456 ===
1074	status: DONE
1075	hypothesis: Free-form SciERC seed=456: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.
1076	conclusion: success
1077	created_at: "2026-05-15T17:14:48.842Z"
1078	updated_at: "2026-05-17T02:56:09.256Z"
1079	metrics: {"inference": {"n_instances": 551, "n_samples": 8, "total_samples": 4408, "total_parsed": 4407, "parse_rate_pct": 99.98, "elapsed_seconds": 232.4}, "freeform": {"selection_ner": {"greedy": 0.6198, "selected": 0.6205, "gap": 0.0007}, "selection_re": {"greedy": 0.2908, "selected": 0.3108, "gap": 0.02}, "logprob_variance": {"mean_std": 0.018631, "mean_range": 0.056792, "tied_pct": 58.4}, "qe_ner": {"n": 529, "SJ": {"rho": 0.378498, "auroc": 0.707769}, "FK": {"rho": 0.286163, "auroc": 0.754779}, "LP": {"rho": 0.227089, "auroc": 0.672081}, "EM": {"rho": 0.319997, "auroc": 0.47789}, "VC": {"rho": 0.416853, "auroc": 0.756543}}, "qe_re": {"n": 397, "SJ": {"rho": 0.211331, "auroc": 0.572335}, "FK": {"rho": 0.259074, "auroc": 0.652998}, "LP": {"rho": 0.306382, "auroc": 0.70134}, "EM": {"rho": 0.1043, "auroc": 0.461641}, "VC": {"rho": 0.301507, "auroc": 0.628873}}}, "constrained_ref": {"selection_ner": {"greedy": 0.6182, "selected": 0.6241, "gap": 0.0059}, "selection_re": {"greedy": 0.2913, "selected": 0.2845, "gap": -0.0068}, "logprob_variance": {"mean_std": 0.020589, "mean_range": 0.062305, "tied_pct": 59.7}}, "comparison": {"variance_ratio_std": 0.9, "variance_ratio_range": 0.91, "tied_reduction_pp": 1.3}}
1080	
1081	=== exp_freeform_seed789 ===
1082	status: DONE
1083	hypothesis: Free-form SciERC seed=789: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.
1084	conclusion: success
1085	created_at: "2026-05-15T18:38:29.851Z"
1086	updated_at: "2026-05-17T02:56:09.888Z"
1087	notes: "Rerun with fixed seed-passing code on cuda:3. Original run was killed for GPU reallocation. Parse rate 100%, 227.5s elapsed. LP compression confirmed: tied_pct=59.0% (vs constrained 59.7%), variance_ratio=0.89x."
1088	metrics: {"inference": {"n_instances": 551, "n_samples": 8, "total_samples": 4408, "total_parsed": 4408, "parse_rate_pct": 100, "elapsed_seconds": 227.5}, "freeform": {"selection_ner": {"greedy": 0.6205, "selected": 0.6232, "gap": 0.0027}, "selection_re": {"greedy": 0.2909, "selected": 0.31, "gap": 0.0191}, "logprob_variance": {"mean_std": 0.0183, "mean_range": 0.054908, "tied_pct": 59}, "qe_ner": {"n": 529, "SJ": {"rho": 0.393995, "auroc": 0.734474}, "FK": {"rho": 0.312292, "auroc": 0.794384}, "LP": {"rho": 0.247096, "auroc": 0.677824}, "EM": {"rho": 0.320383, "auroc": 0.527033}, "VC": {"rho": 0.420625, "auroc": 0.768111}}, "qe_re": {"n": 397, "SJ": {"rho": 0.201746, "auroc": 0.574388}, "FK": {"rho": 0.2202, "auroc": 0.633014}, "LP": {"rho": 0.295765, "auroc": 0.687067}, "EM": {"rho": 0.103633, "auroc": 0.474737}, "VC": {"rho": 0.306868, "auroc": 0.642197}}}, "constrained_ref": {"selection_ner": {"greedy": 0.6182, "selected": 0.6241, "gap": 0.0059}, "selection_re": {"greedy": 0.2913, "selected": 0.2845, "gap": -0.0068}, "logprob_variance": {"mean_std": 0.020589, "mean_range": 0.062305, "tied_pct": 59.7}}, "comparison": {"variance_ratio_std": 0.89, "variance_ratio_range": 0.88, "tied_reduction_pp": 0.7}}
1089	
1090	=== exp_freeform_seed789_v2 ===
1091	status: DONE
1092	hypothesis: 
1093	conclusion: failed
1094	created_at: "2026-05-15T19:02:03.813Z"
1095	updated_at: "2026-05-15T19:06:44.537Z"
1096	
1097	=== exp_freeform_seed789_v3 ===
1098	status: DONE
1099	hypothesis: Free-form SciERC seed=789 v3 (bugfix rerun): corrected version of free-form inference after fixing parsing/generation issues in v1/v2. Provides clean data point for 4-seed free-form analysis.
1100	conclusion: success
1101	created_at: "2026-05-15T19:24:26.805Z"
1102	updated_at: "2026-05-17T02:56:11.818Z"
1103	metrics: {"n_instances": 551, "n_samples": 8, "parse_rate_pct": 100, "elapsed_seconds": 229.7, "freeform_ner_selection_gap": 0.0028, "freeform_re_selection_gap": 0.0219, "freeform_lp_std": 0.0183, "freeform_lp_range": 0.054908, "freeform_tied_pct": 59, "re_lp_flip_positive": true, "variance_ratio_std": 0.89, "variance_ratio_range": 0.88}
1104	
1105	=== exp_llama3b_scierc_ablation ===
1106	status: DONE
1107	hypothesis: Cross-family scale ablation: LLaMA 3.2-3B on SciERC NER. Verify correlation-selection gap generalizes across model families AND scales. Compare with LLaMA 8B results.
1108	conclusion: success
1109	created_at: "2026-05-16T02:45:23.638Z"
1110	updated_at: "2026-05-16T03:59:26.005Z"
1111	metrics: {"ner_full": {"SJ_rho": 0.3754, "FK_rho": 0.2676, "LP_rho": 0.2662, "EM_rho": 0.3341, "VC_rho": 0.4602, "SJ_auroc": 0.7383, "FK_auroc": 0.6714, "LP_auroc": 0.633, "EM_auroc": 0.7763, "VC_auroc": 0.7429, "n": 529}, "ner_cond": {"SJ_rho": 0.3445, "FK_rho": 0.2125, "LP_rho": 0.2099, "EM_rho": 0.3952, "VC_rho": 0.3815, "SJ_auroc": 0.7292, "FK_auroc": 0.66, "LP_auroc": 0.6156, "EM_auroc": 0.7822, "VC_auroc": 0.7222, "n": 476}, "greedy_f1": 0.6267, "oracle_f1": 0.763, "oracle_headroom": 0.1363, "selection_f1_SJ": 0.6328, "selection_f1_VC": 0.6113, "selection_f1_FK": 0.6295, "selection_f1_EM": 0.6174, "selection_f1_LP": 0.6279, "n_gold_empty": 22, "structural_beats_surface": true, "rho_advantage_SJ_over_FK": 0.1078}
1112	
1113	=== exp_llama_fewnerd_inference ===
1114	status: DONE
1115	hypothesis: LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.
1116	conclusion: success
1117	created_at: "2026-05-19T02:18:49.938Z"
1118	updated_at: "2026-05-19T03:15:04.486Z"
1119	parent: "exp_llama_fewnerd_lora"
1120	metrics: {"3seed_mean": {"greedy_f1": 0.7842, "oracle_f1": 0.8843, "headroom_pp": 10.01, "degeneracy_pct": 23.36, "lp_delta_pp": 0.36, "dgs_delta_pp": -0.35}, "seed_42": {"greedy_f1": 0.7841, "oracle_f1": 0.8854, "degen": 27.32}, "seed_123": {"greedy_f1": 0.784, "oracle_f1": 0.8839, "degen": 24.63}, "seed_456": {"greedy_f1": 0.7844, "oracle_f1": 0.8835, "degen": 18.13}, "signal_ranking": "LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)", "lp_only_positive": true, "n_instances_gold_filtered": 32565}
1121	
1122	=== exp_llama_fewnerd_lora ===
1123	status: DONE
1124	hypothesis: LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER
1125	conclusion: success
1126	created_at: "2026-05-18T13:20:55.859Z"
1127	updated_at: "2026-05-19T01:08:20.832Z"
1128	metrics: {"epoch": 3, "train_loss": 0.0516, "eval_loss": 0.0323, "train_runtime_hours": 15.35, "total_steps": 24708, "final_checkpoint": "checkpoint-24708", "adapter_size_mb": 320}
1129	
1130	=== exp_llama_scierc_seed456 ===
1131	status: DONE
1132	hypothesis: LLaMA-3.1-8B on SciERC with seed=456 will show consistent 5-signal ranking patterns (SJ/FK > logprob) and DGS selection gains comparable to seed=42 and seed=123, confirming cross-seed stability.
1133	conclusion: success
1134	created_at: "2026-05-18T19:15:27.504Z"
1135	updated_at: "2026-05-18T20:49:10.758Z"
1136	metrics: {"greedy_f1": 0.6457, "oracle_f1": 0.7574, "headroom": 0.1117, "dgs_f1": 0.6454, "degen_rate": 0.2741, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered", "rho_SJ_full": 0.3663, "rho_FK_full": 0.3115, "rho_logprob_full": 0.1911, "rho_EM_full": 0.3088, "rho_vc_full": 0.4135, "auroc_SJ_full": 0.7061, "auroc_EM_full": 0.7538, "n_valid": 529, "n_conditional": 478}
1137	
1138	=== exp_lp_alignment_gating ===
1139	status: DONE
1140	hypothesis: Within-instance LP-F1 alignment score (adjusted by valid_ratio for degeneracy) can automatically gate whether LP selection should be applied to a dataset. A small probe sample (50-100 instances) suffices for a stable gating decision.
1141	conclusion: success
1142	created_at: "2026-05-19T02:00:16.520Z"
1143	updated_at: "2026-05-19T02:15:48.197Z"
1144	metrics: {"adjusted_score": "mean_rho * valid_ratio", "threshold": 0.3, "accuracy": "3/3 datasets correct", "robust_range": "0.2-0.4"}
1145	
1146	=== exp_lp_scierc_t07 ===
1147	status: DONE
1148	hypothesis: LP T=0.7 推理：验证低温下 LP score compression 是否依然存在，强化 "LP compression is model/task intrinsic" claim。对比 T=1.0 的 LP range 分布。
1149	conclusion: success
1150	created_at: "2026-05-15T15:34:06.918Z"
1151	updated_at: "2026-05-15T16:03:13.881Z"
1152	metrics: {"ner_greedy_f1": 0.662, "ner_oracle_f1": 0.764, "ner_headroom_pp": 10.2, "ner_rho_sj_full": 0.365, "ner_rho_sj_cond": 0.363, "ner_rho_fk_full": 0.289, "ner_rho_fk_cond": 0.255, "lp_rho_full": 0.249, "lp_rho_cond": 0.185, "ner_rho_advantage": 0.076, "zero_f1_pct": 11, "full_n": 529, "cond_n": 477, "verdict": "success_supports_LP_compression_claim"}
1153	
1154	=== exp_lp_t07_scierc ===
1155	status: DONE
1156	hypothesis: 
1157	conclusion: killed
1158	created_at: "2026-05-15T15:34:12.094Z"
1159	updated_at: "2026-05-15T16:30:35.531Z"
1160	
1161	=== exp_pareto_diversity_quality ===
1162	status: PREPARING
1163	hypothesis: There exists a Pareto frontier in the diversity (1-degeneracy) vs construction quality (ΔF1) space across temperature configurations. Well-separated temperature mixing (T=0.7+T=1.0) achieves Pareto optimality for both uniform and VC construction, while VC-weighted construction flattens the trade-off slope, reducing the diversity cost of quality.
1164	conclusion: success
1165	created_at: "2026-05-20T09:31:45.421Z"
1166	updated_at: "2026-05-20T09:31:58.776Z"
1167	metrics: {"dataset": "SciERC", "configs": {"t07": {"one_minus_degen": 0.777, "uniform_delta": 1.81, "vc_delta": 1.17, "pareto": "uniform only"}, "t08": {"one_minus_degen": 0.819, "uniform_delta": 1.25, "vc_delta": 1.68, "pareto": "VC only"}, "mix_07_10": {"one_minus_degen": 0.83, "uniform_delta": 1.43, "vc_delta": 1.67, "pareto": "both"}, "t10": {"one_minus_degen": 0.877, "uniform_delta": 0.75, "vc_delta": 1.21, "pareto": "both (highest diversity)"}, "mix_08_10": {"one_minus_degen": 0.789, "uniform_delta": -0.17, "vc_delta": 0.47, "pareto": "dominated"}}, "vc_slope_reduction": "~50% flatter than uniform", "key_insight": "well-separated T mixing dual Pareto optimal; close T mixing dominated"}
1168	notes: "A4 Pareto diversity-quality analysis on SciERC. Mix T=0.7+T=1.0 is dual-Pareto optimal (uniform +1.43pp, VC +1.67pp). VC construction flattens trade-off slope ~50% vs uniform — increasing diversity costs less quality. Mix T=0.8+T=1.0 is dominated (close T → higher degeneracy, no construction gain). Confirms DGEC heterogeneous-T finding: ΔT matters, ΔT=0.3 beneficial, ΔT=0.2 harmful. Pareto plot artifact registered."
1169	
1170	=== exp_qwen25_14b_fewnerd ===
1171	status: RUNNING
1172	hypothesis: The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.
1173	conclusion: 
1174	created_at: "2026-05-19T06:19:31.620Z"
1175	updated_at: "2026-05-20T07:15:22.169Z"
1176	notes: "2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. Step 6483/41180 (15.7%), loss 0.0608, ~2.2s/it, ETA ~21h. checkpoint-6000 saved. screen train_14b_s42 PID 56766, GPU 0,1 95-96% util. Cron registered on PID 56773."
1177	metrics: {"training_progress": "77.7% (32000/41180, eval running at check time 07:14 UTC)", "epoch": "3.89/5.0", "loss": 0.0127, "speed": "~2.13s/step", "eta": "~05-20 14:00-15:00 UTC (train 5h26m remaining + eval pauses)"}
1178	
1179	=== exp_qwen25_32b_fewnerd ===
1180	status: RUNNING
1181	hypothesis: Scaling from Qwen3-8B to Qwen2.5-32B-Instruct with QLoRA fine-tuning on FewNERD will improve structured self-consistency IE performance due to stronger base model capabilities in instruction following and entity recognition.
1182	conclusion: 
1183	created_at: "2026-05-19T06:19:25.428Z"
1184	updated_at: "2026-05-20T07:15:23.641Z"
1185	notes: "2026-05-19 11:36 UTC: step 2177/41180 (5.3%), loss 0.0663, ~2.44s/it, ETA ~26h. checkpoint-2000 saved. PID 804438, 4×5090 87-100% util."
1186	metrics: {"training_progress": "56.9% (23448/41180, checked 07:14 UTC)", "epoch": "2.84/5.0", "loss": 0.027, "speed": "~2.50s/step", "eta": "~05-20 20:00-22:00 UTC (train 12h30m remaining + eval pauses)"}
1187	
1188	=== exp_qwen25_72b_fewshot ===
1189	status: DONE
1190	hypothesis: Few-shot prompting improves base NER F1 and LP signal quality, enabling LP-weighted construction to outperform greedy selection via dual-gating (sufficient LP ρ + low degeneracy).
1191	conclusion: negative
1192	created_at: "2026-05-19T15:59:44.340Z"
1193	updated_at: "2026-05-20T00:54:59.032Z"
1194	parent: "exp_qwen25_72b_zeroshot"
1195	metrics: {"scierc": {"lp_rho": 0.06, "sj_rho": 0.293, "fk_rho": 0.301, "vc_rho": 0.258, "em_rho": 0.205, "degen_pct": 16.6, "greedy_f1": 0.461, "oracle_f1": 0.604, "construction_f1": 0.461, "construction_delta_pp": -0.08, "bootstrap_p": 0.544}, "conll": {"lp_rho": 0.106, "sj_rho": 0.442, "fk_rho": 0.451, "vc_rho": 0.426, "em_rho": 0.403, "degen_pct": 70, "greedy_f1": 0.745, "oracle_f1": 0.796, "construction_f1": 0.745, "construction_delta_pp": 0.03, "bootstrap_p": 0.417}, "fewnerd": {"lp_rho": 0.161, "sj_rho": 0.345, "fk_rho": 0.327, "vc_rho": 0.41, "em_rho": 0.302, "degen_pct": 45.2, "greedy_f1": 0.619, "oracle_f1": 0.702, "construction_f1": 0.619, "construction_delta_pp": 0.02, "bootstrap_p": 0.401}}
1196	
1197	=== exp_qwen25_72b_zeroshot ===
1198	status: DONE
1199	hypothesis: A larger zero-shot model (72B) will show higher greedy F1 and wider oracle-greedy gap than fine-tuned smaller models, because increased capacity enables more diverse valid extractions per stochastic sample, making self-consistency signals (SJ, FK, VC, EM) more informative for quality estimation.
1200	conclusion: negative
1201	created_at: "2026-05-19T06:19:28.597Z"
1202	updated_at: "2026-05-19T16:23:10.481Z"
1203	notes: "2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. 289848/301184 prompts (96.2%). SciERC ✅ (551) CoNLL ✅ (3453) FewNERD ~96%. ETA ~10-15min. PID 59040, 4×5090 100% util. Cron registered."
1204	metrics: {"scierc": {"greedy_f1": 0.3993, "lp_rho": 0.081, "vc_rho": 0.277, "sj_rho": 0.217, "degen_rate": 0.21, "construction_lp_weighted_f1": 0.4146, "construction_lp_delta_pp": 1.53, "construction_uniform_f1": 0.3941, "construction_uniform_delta_pp": -0.52, "lp_selection_f1": 0.3984, "majority_vote_f1": 0.4132, "oracle_f1": 0.5489, "bootstrap_p": 0.0082, "bootstrap_ci_lower": 0.0025, "bootstrap_ci_upper": 0.0282, "cohens_d": 0.1027, "n_instances": 529, "non_degen_delta_pp": 1.65, "non_degen_p": 0.0069}, "conll2003": {"greedy_f1": 0.712, "lp_rho": -0.002, "vc_rho": 0.297, "sj_rho": 0.304, "degen_rate": 0.677, "construction_lp_weighted_f1": 0.7083, "construction_lp_delta_pp": -0.37, "construction_uniform_f1": 0.7028, "construction_uniform_delta_pp": -0.92, "lp_selection_f1": 0.708, "majority_vote_f1": 0.7034, "oracle_f1": 0.7651}, "fewnerd": {"greedy_f1": 0.6281, "lp_rho": 0.119, "vc_rho": 0.416, "sj_rho": 0.345, "degen_rate": 0.462, "construction_lp_weighted_f1": 0.6261, "construction_lp_delta_pp": -0.2, "construction_uniform_f1": 0.6112, "construction_uniform_delta_pp": -1.7, "lp_selection_f1": 0.6241, "lp_selection_delta_pp": -0.4, "majority_vote_f1": 0.6262, "oracle_f1": 0.7072}}
1205	
1206	=== exp_qwen25_7b_fewnerd ===
1207	status: DONE
1208	hypothesis: Qwen2.5-7B QLoRA fine-tuned on FewNERD will produce structurally diverse samples enabling self-consistency-based entity extraction with meaningful LP-weighted consensus signals, comparable to the 14B model but with lower compute cost.
1209	conclusion: success
1210	created_at: "2026-05-19T06:41:43.121Z"
1211	updated_at: "2026-05-20T05:45:54.613Z"
1212	notes: "2026-05-19 11:36 UTC: step 138/20590 (0.7%), ~2.34s/it, ETA ~13.3h. Pipeline PID 71837, llamafactory PID 71844. cuda:2,3 98-100% util. Cron registered on pipeline PID."
1213	metrics: {"3seed_mean": {"lp_rho": 0.346, "lp_rho_std": 0.021, "sj_rho": 0.388, "sj_rho_std": 0.029, "vc_rho": 0.404, "vc_rho_std": 0.01, "degen_pct": 31.7, "degen_std": 0.9, "greedy_f1": 0.784, "greedy_f1_std": 0.001, "oracle_f1": 0.876, "oracle_f1_std": 0.003, "construction_lp_delta_pp": -0.11, "construction_lp_delta_std": 0.25}, "per_seed": {"seed42": {"lp_rho": 0.3221, "sj_rho": 0.3554, "vc_rho": 0.393, "degen_pct": 31.1, "greedy_f1": 0.7851, "oracle_f1": 0.8718, "construction_lp_delta_pp": -0.4, "bootstrap_p": 1, "bootstrap_ci": [-0.53, -0.26], "cohens_d": -0.0319}, "seed123": {"lp_rho": 0.3538, "sj_rho": 0.3979, "vc_rho": 0.4067, "degen_pct": 32.8, "greedy_f1": 0.785, "oracle_f1": 0.8777, "construction_lp_delta_pp": -0.03, "bootstrap_p": 0.651}, "seed456": {"lp_rho": 0.3629, "sj_rho": 0.4105, "vc_rho": 0.4118, "degen_pct": 31.3, "greedy_f1": 0.7825, "oracle_f1": 0.8771, "construction_lp_delta_pp": 0.09, "bootstrap_p": 0.168}}, "construction_significant": false}
1214	
1215	=== exp_qwen3_4b_conll_finetune ===
1216	status: DONE
1217	hypothesis: Scale ablation: Qwen3-4B CoNLL NER LoRA fine-tune to provide cross-scale evidence (vs 8B). Verify correlation-selection gap, SJ>FK ordering, and LP compression generalize across model scale.
1218	conclusion: success
1219	created_at: "2026-05-15T17:18:35.501Z"
1220	updated_at: "2026-05-15T19:10:24.822Z"
1221	notes: "Training stopped at step 3920/4390 (89.3%, epoch 4.46/5). No error log or tmux session found. checkpoint-3800 is valid (adapter_model.safetensors 264MB, eval_loss=0.023). Proceeding with checkpoint-3800 for merge+inference."
1222	metrics: {"final_loss": 0.0086, "total_steps_completed": 3920, "total_steps_target": 4390, "epochs_completed": 4.46, "epochs_target": 5, "best_checkpoint": "checkpoint-3800", "note": "Training stopped at 89.3% completion (no error log found). Using checkpoint-3800 (loss ~0.01) for merge."}
1223	
1224	=== exp_qwen3_4b_conll_finetune_resume ===
1225	status: DONE
1226	hypothesis: CoNLL 4B NER LoRA fine-tune resume from checkpoint-3800. Cross-scale evidence for correlation-selection gap.
1227	conclusion: success
1228	created_at: "2026-05-15T19:38:19.388Z"
1229	updated_at: "2026-05-15T19:38:43.468Z"
1230	metrics: {"train_loss": 0.001136, "eval_loss": 0.0225, "best_global_step": 4200, "best_metric_eval_loss": 0.0225, "total_steps": 4390, "epochs": 5, "train_runtime_sec": 1185.8, "train_samples_per_second": 59.2, "resumed_from_step": 3800}
1231	
1232	=== exp_qwen3_4b_conll_merge_inference_v2 ===
1233	status: DONE
1234	hypothesis: CoNLL 4B checkpoint-4200 (best from resume training) merge + SCS inference. Replaces v1 which used checkpoint-3800 merged model. Cross-scale evidence for correlation-selection gap.
1235	conclusion: killed
1236	created_at: "2026-05-15T19:42:42.107Z"
1237	updated_at: "2026-05-15T20:07:12.593Z"
1238	notes: "Superseded by exp_qwen3_4b_conll_scs_inference_v2. Output was empty (dead experiment), functionally duplicate."
1239	
1240	=== exp_qwen3_4b_conll_scs_inference ===
1241	status: DONE
1242	hypothesis: CoNLL 4B SCS inference (checkpoint-3800): cross-scale evidence for correlation-selection gap. Tests if structural>surface ranking and LP compression hold at smaller model scale on high-degeneracy dataset.
1243	conclusion: success
1244	created_at: "2026-05-15T19:08:28.512Z"
1245	updated_at: "2026-05-18T20:49:06.922Z"
1246	metrics: {"greedy_f1": 0.9251, "oracle_f1": 0.9408, "oracle_headroom_pp": 1.57, "SJ_rho_full": 0.4045, "SJ_rho_cond": 0.4306, "FK_rho_full": 0.3961, "FK_rho_cond": 0.42, "LP_rho_full": 0.3186, "LP_rho_cond": 0.3378, "LP_auroc_full": 0.7689, "LP_auroc_cond": 0.8153, "fleiss_kappa_mean": 0.9349, "soft_jaccard_mean": 0.9754, "structural_beats_surface": true, "rho_advantage_pp": 0.84, "n_instances": 3453, "n_gold_empty_filtered": 697, "n_greedy_f1_zero_filtered": 112, "verdict": "MARGINAL", "degen_rate": 0.9057, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
1247	notes: "4B CoNLL SCS inference completed. SJ>FK>LP ordering preserved at 4B scale (rho 0.405>0.396>0.319). Greedy F1=0.925 outperforms 8B (0.907), but SJ rho is lower (0.405 vs 0.450 at 8B N=16). Structural beats surface confirmed (+0.84pp). Verdict MARGINAL due to small oracle headroom (1.57pp) — the model is already very good at CoNLL, leaving little room for selection improvement."
1248	
1249	=== exp_qwen3_4b_conll_scs_inference_v2 ===
1250	status: DONE
1251	hypothesis: CoNLL 4B SCS inference with best checkpoint-4200 (from resume training). Scale ablation: cross-scale evidence for correlation-selection gap. Compare vs v1 (ckpt-3800 baseline: greedy_f1=0.9251, SJ_rho=0.4045).
1252	conclusion: success
1253	created_at: "2026-05-15T19:41:33.501Z"
1254	updated_at: "2026-05-18T20:49:03.705Z"
1255	metrics: {"greedy_f1": 0.9234, "oracle_f1": 0.9404, "oracle_headroom_pp": 1.7, "SJ_rho_full": 0.4217, "SJ_rho_cond": 0.459, "FK_rho_full": 0.4181, "FK_rho_cond": 0.4538, "LP_rho_full": 0.3313, "LP_rho_cond": 0.3487, "LP_auroc_full": 0.7761, "LP_auroc_cond": 0.8209, "n_instances": 3453, "verdict": "MARGINAL", "degen_rate": 0.9057, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
1256	notes: "Gold-filter audit (2026-05-16): CONSISTENT. _full metrics (SJ_rho=0.4217, FK_rho=0.4181) are computed on gold-filtered set (n=2756), same as 8B Table 1 values. _full does NOT mean all 3453 instances — it means gold-nonempty instances. _cond further excludes greedy-F1=0 (n=2641). Confirmed via run_mvp_pilot.py source code and report.json n values."
1257	
1258	=== exp_qwen3_4b_scierc_finetune ===
1259	status: DONE
1260	hypothesis: 
1261	conclusion: killed
1262	created_at: "2026-05-15T18:58:58.948Z"
1263	updated_at: "2026-05-15T19:03:05.505Z"
1264	
1265	=== exp_qwen3_4b_scierc_finetune_v2 ===
1266	status: DONE
1267	hypothesis: 
1268	conclusion: failed
1269	created_at: "2026-05-15T19:03:49.204Z"
1270	updated_at: "2026-05-15T19:24:32.466Z"
1271	notes: "PID 219830 已死，仅完成 step 10，无 checkpoint。需彻底重启。"
1272	
1273	=== exp_qwen3_4b_scierc_finetune_v3 ===
1274	status: DONE
1275	hypothesis: 
1276	conclusion: failed
1277	created_at: "2026-05-15T19:24:45.518Z"
1278	updated_at: "2026-05-15T19:39:04.438Z"
1279	notes: "OOM on cuda:2 — freeform inference (seed789, 8B) 占满 GPU 2。未实际训练。重启为 v4 on cuda:0。"
1280	
1281	=== exp_qwen3_4b_scierc_finetune_v4 ===
1282	status: DONE
1283	hypothesis: Qwen3-4B SciERC LoRA fine-tune v4: training the smaller 4B model to complete the 2x2 scale matrix (4B×SciERC cell). Validates that fine-tuning convergence patterns hold across model scales.
1284	conclusion: success
1285	created_at: "2026-05-15T19:26:25.512Z"
1286	updated_at: "2026-05-17T02:56:24.418Z"
1287	metrics: {"total_steps": 585, "completed_steps": 585, "best_checkpoint": "checkpoint-400", "best_eval_loss": 0.0898, "epochs": 5}
1288	
1289	=== exp_qwen3_4b_scierc_merge_inference ===
1290	status: DONE
1291	hypothesis: SciERC 4B best checkpoint merge + SCS inference. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.
1292	conclusion: killed
1293	created_at: "2026-05-15T19:42:43.332Z"
1294	updated_at: "2026-05-15T20:04:15.433Z"
1295	notes: "Superseded by exp_qwen3_4b_scierc_scs_inference. Never launched (stuck in PREPARING). Killed during registry cleanup."
1296	
1297	=== exp_qwen3_4b_scierc_scs_inference ===
1298	status: DONE
1299	hypothesis: SciERC 4B SCS inference after v4 finetune merge. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.
1300	conclusion: success
1301	created_at: "2026-05-15T19:45:33.384Z"
1302	updated_at: "2026-05-18T20:49:01.260Z"
1303	metrics: {"ner_greedy_f1": 0.6612, "ner_oracle_f1": 0.7839, "ner_headroom_pp": 12.28, "ner_SJ_rho": 0.4221, "ner_FK_rho": 0.3258, "ner_LP_rho": 0.28, "re_greedy_f1": 0.4136, "re_oracle_f1": 0.5846, "re_headroom_pp": 17.1, "re_SJ_rho": 0.2673, "re_FK_rho": 0.3593, "re_LP_rho": 0.3512, "re_sample_f1_pct_zero": 0.476, "re_LP_rho_cond": 0.1135, "re_LP_rho_cond_p": 0.074, "degen_rate": 0.104, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
1304	
1305	=== exp_re_scierc_seed123 ===
1306	status: DONE
1307	hypothesis: SciERC RE 多种子验证 (seed123): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。
1308	conclusion: negative
1309	created_at: "2026-05-15T15:40:38.271Z"
1310	updated_at: "2026-05-15T15:55:40.000Z"
1311	metrics: {"ner_greedy_f1": 0.663, "ner_oracle_f1": 0.786, "ner_headroom_pp": 12.3, "ner_rho_sj_cond": 0.404, "ner_rho_fk_cond": 0.182, "re_greedy_f1": 0.42, "re_oracle_f1": 0.593, "re_headroom_pp": 17.3, "re_rho_sj_cond": 0.277, "re_rho_fk_cond": 0.063, "re_zero_f1_pct": 43.6, "verdict": "FAIL_re_rho_sj_below_040"}
1312	
1313	=== exp_re_scierc_seed456 ===
1314	status: DONE
1315	hypothesis: SciERC RE 多种子验证 (seed456): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。
1316	conclusion: negative
1317	created_at: "2026-05-15T15:40:40.607Z"
1318	updated_at: "2026-05-15T15:55:41.890Z"
1319	metrics: {"ner_greedy_f1": 0.664, "ner_oracle_f1": 0.775, "ner_headroom_pp": 11.1, "ner_rho_sj_cond": 0.283, "ner_rho_fk_cond": 0.145, "re_greedy_f1": 0.417, "re_oracle_f1": 0.581, "re_headroom_pp": 16.3, "re_rho_sj_cond": 0.315, "re_rho_fk_cond": 0.123, "re_zero_f1_pct": 45.3, "verdict": "FAIL_re_rho_sj_below_040"}
1320	
1321	=== exp_selective_prediction ===
1322	status: DONE
1323	hypothesis: QE signals (especially voting_confidence) can drive practical selective prediction: filtering out low-confidence instances yields significant F1 improvement on retained instances, enabling human-AI collaboration for structured IE.
1324	conclusion: success
1325	created_at: "2026-05-19T02:00:13.989Z"
1326	updated_at: "2026-05-19T02:15:46.588Z"
1327	metrics: {"vc_best_signal": true, "f1_at_80pct_coverage": {"scierc": "+5.0pp", "conll": "+8.4pp", "fewnerd": "+6.2pp"}, "precision_coverage_curves": "output/prescriptive_analysis/fig_selective_prediction.pdf"}
1328	
1329	=== exp_tacred_re_benchmark ===
1330	status: DONE
1331	hypothesis: TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.
1332	conclusion: killed
1333	created_at: "2026-05-16T04:43:59.002Z"
1334	updated_at: "2026-05-16T06:31:25.273Z"
1335	
1336	=== exp_vc_lp_cascade_selection ===
1337	status: DONE
1338	hypothesis: VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.
1339	conclusion: killed
1340	created_at: "2026-05-16T04:44:02.658Z"
1341	updated_at: "2026-05-16T06:31:26.755Z"
1342	
1343	=== exp_vc_quartile_analysis ===
1344	status: DONE
1345	hypothesis: VC quartile stratification: split instances by VC score into Q1-Q4, compute LP selection F1 per quartile. Test if LP selection ability recovers in high-VC instances. Addresses SF3.
1346	conclusion: success
1347	created_at: "2026-05-16T04:48:35.263Z"
1348	updated_at: "2026-05-16T05:00:36.736Z"
1349	metrics: {"scierc_ner": {"Q1_lp_delta": 0.016, "Q2_lp_delta": -0.006, "Q3_lp_delta": 0.02, "Q4_lp_delta": -0.004, "Q4_mean_vc": 0.921, "Q1_headroom": 0.169, "Q4_headroom": 0.048, "overall_lp_delta": 0.006, "n": 529}, "scierc_re": {"Q1_lp_delta": -0.036, "Q2_lp_delta": -0.021, "Q3_lp_delta": -0.022, "Q4_lp_delta": 0.04, "Q4_mean_vc": 0.894, "Q1_headroom": 0.211, "Q4_headroom": 0.145, "overall_lp_delta": -0.009, "n": 397}, "conll_ner": {"Q1_lp_delta": -0.037, "Q2_lp_delta": -0.005, "Q3_lp_delta": 0, "Q4_lp_delta": 0, "overall_lp_delta": -0.01, "n": 2756, "note": "Q3/Q4 degenerate (VC=1.0, all samples identical)"}, "conclusion": "VC stratification does not solve LP compression for NER. RE Q4 is only exception (+0.040)."}
1350	
1351	=== exp_verbalized_confidence ===
1352	status: DONE
1353	hypothesis: Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens "score compression is general" claim. If effective → important positive finding requiring narrative adjustment.
1354	conclusion: negative
1355	created_at: "2026-05-16T02:45:20.552Z"
1356	updated_at: "2026-05-17T03:33:39.197Z"
1357	metrics: {"scierc": {"VerbConf_rho": 0.2965, "VerbConf_auroc": 0.6811, "VerbConf_sel_f1": 0.6195, "VerbConf_delta": -0.0245, "best_existing_rho": 0.3792, "VerbConf_mean": 8.58, "VerbConf_std": 1.15, "parse_fail_rate": 0.0026}, "conll": {"VerbConf_rho": 0.3366, "VerbConf_auroc": 0.7469, "VerbConf_sel_f1": 0.8886, "VerbConf_delta": -0.0193, "best_existing_rho": 0.4507, "VerbConf_mean": 9.24, "VerbConf_std": 1.32, "parse_fail_rate": 0}}
1358	parent: "exp_012_rerun_1024"
1359	
1360	=== exp_wnut17_qwen25_7b ===
1361	status: DONE
1362	hypothesis: The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/FewNERD), WNUT-17 has higher surface-level noise which may affect structural signal reliability differently. This tests domain generalization of the diagnostic framework.
1363	conclusion: negative
1364	created_at: "2026-05-19T06:19:33.960Z"
1365	updated_at: "2026-05-19T11:49:07.313Z"
1366	metrics: {"seed42": {"greedy_f1": 0.4524, "construction_f1": 0.4439, "construction_delta_pp": -0.84, "construction_p": 0.95}, "seed123": {"greedy_f1": 0.4518, "construction_f1": 0.4579, "construction_delta_pp": 0.61, "construction_p": 0.08}, "seed456": {"greedy_f1": 0.4526, "construction_f1": 0.4583, "construction_delta_pp": 0.57, "construction_p": 0.12}, "oracle_headroom_pp": "6.3-9.2"}
1367	
1368	=== ft_001 ===
1369	status: DONE
1370	hypothesis: 
1371	conclusion: success
1372	created_at: "2026-05-14T06:04:28.030Z"
1373	updated_at: "2026-05-14T08:27:58.182Z"
1374	metrics: {"train_loss": 0.1099, "eval_loss": 0.0771, "gate0_ner_f1_strict": 0.1143, "gate0_re_f1_strict": 0.0125, "gate0_ner_f1_text": 0.606, "gate0_re_f1_text": 0.3392, "gate0_offset_accuracy": 0.1665, "gate0_parse_failures": 43, "gate0_pass": false, "gate0_realigned_ner_f1": 0.6045, "gate0_realigned_re_f1": 0.338, "gate0_realigned_entity_offset_accuracy": 1, "gate0_realigned_relation_offset_accuracy": 1, "gate0_realigned_ner_pass": true, "gate0_realigned_re_pass": false, "gate0_realigned_pass": false, "gate0_ner_f1_delta_realign": 0.4901, "gate0_re_f1_delta_realign": 0.3255, "verdict_note": "partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)"}
1375	
1376	=== ft_002 ===
1377	status: DONE
1378	hypothesis: 
1379	conclusion: killed
1380	created_at: "2026-05-14T07:39:18.640Z"
1381	updated_at: "2026-05-14T08:28:00.590Z"
1382	metrics: {"last_step": 70, "total_steps": 585, "progress_pct": 11.97, "last_loss": 0.1134, "last_lr": 0.00019982, "elapsed": "3m32s", "failure_reason": "OOM at step 73, batch_size=4 too large for 32GB RTX 5090"}
1383	
1384	=== ft_002_v2 ===
1385	status: DONE
1386	hypothesis: 
1387	conclusion: success
1388	created_at: "2026-05-14T08:28:40.861Z"
1389	updated_at: "2026-05-14T08:51:32.405Z"
1390	metrics: {"epoch": 5, "train_loss": 0.0806, "eval_loss": 0.089, "train_runtime": "28m41s", "train_samples_per_second": 5.407, "train_steps_per_second": 0.34, "total_steps": 585, "checkpoints": ["checkpoint-400", "checkpoint-500", "checkpoint-585"], "gate0_final_ner_f1": 0.6615, "gate0_final_re_f1": 0.4177, "gate0_final_parse_failures": 0, "gate0_final_ner_pass": true, "gate0_final_re_pass": true, "gate0_final_pass": true, "gate0_ckpt400_ner_f1": 0.6475, "gate0_ckpt400_re_f1": 0.3793, "gate0_ckpt400_parse_failures": 0, "gate0_ckpt400_verdict": "FAIL", "gate0_ckpt400_re_sample_f1_pct_zero": 58.8, "gate0_ckpt400_warning": ">30% samples F1=0"}
1391	
1392	=== hidden_state_probe_conll_full ===
1393	status: DONE
1394	hypothesis: 
1395	conclusion: killed
1396	created_at: "2026-05-18T12:57:45.711Z"
1397	updated_at: "2026-05-19T00:30:18.272Z"
1398	notes: "Not in D154 Dual Contribution framing"
1399	
1400	=== hidden_state_probe_conll_v2 ===
1401	status: DONE
1402	hypothesis: 
1403	conclusion: killed
1404	created_at: "2026-05-18T12:35:05.317Z"
1405	updated_at: "2026-05-19T00:30:16.471Z"
1406	notes: "Not in D154 Dual Contribution framing"
1407	
1408	=== mbr_pilot ===
1409	status: DONE
1410	hypothesis: 
1411	conclusion: killed
1412	created_at: "2026-05-18T17:56:06.462Z"
1413	updated_at: "2026-05-19T00:29:39.285Z"
1414	notes: "MBR tested negative as one of 6 methods, stale entry"
1415	
1416	=== mvp_pilot_001 ===
1417	status: DONE
1418	hypothesis: 
1419	conclusion: negative
1420	created_at: "2026-05-14T07:39:16.313Z"
1421	updated_at: "2026-05-14T08:05:34.348Z"
1422	metrics: {"ner_greedy_f1": 0.611, "ner_oracle_f1": 0.78, "ner_headroom": 0.169, "ner_fleiss_kappa_mean": 0.2449, "ner_soft_jaccard_mean": 0.5041, "ner_full_rho_sj": 0.3616, "ner_full_rho_fk": 0.3515, "ner_full_n": 529, "ner_cond_rho_sj": 0.3688, "ner_cond_rho_fk": 0.3569, "ner_cond_n": 510, "ner_sj_beats_fk_full": true, "ner_sj_beats_fk_cond": true, "ner_sample_f1_pct_zero": 20.4, "ner_gold_empty_filtered": 22, "ner_all_zero_filtered": 19, "re_greedy_f1": 0.355, "re_oracle_f1": 0.572, "re_headroom": 0.217, "re_fleiss_kappa_mean": 0.0681, "re_soft_jaccard_mean": 0.3635, "re_full_rho_sj": 0.2535, "re_full_rho_fk": 0.2885, "re_full_n": 397, "re_cond_rho_sj": 0.3515, "re_cond_rho_fk": 0.3107, "re_cond_n": 320, "re_sj_beats_fk_full": false, "re_sj_beats_fk_cond": true, "re_sample_f1_pct_zero": 58.3, "re_gold_empty_filtered": 154, "re_all_zero_filtered": 77, "parse_failures_stochastic": 164, "parse_failures_greedy": 29, "total_stochastic_samples": 4408, "total_greedy": 551, "verdict": "FAIL", "verdict_reason": "RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set"}
1423	
1424	=== mvp_pilot_002 ===
1425	status: DONE
1426	hypothesis: 
1427	conclusion: failed
1428	created_at: "2026-05-14T08:02:16.991Z"
1429	updated_at: "2026-05-14T08:48:14.040Z"
1430	
1431	=== mvp_pilot_003 ===
1432	status: DONE
1433	hypothesis: 
1434	conclusion: negative
1435	created_at: "2026-05-14T08:21:09.847Z"
1436	updated_at: "2026-05-14T08:21:44.983Z"
1437	metrics: {"ner_greedy_f1": 0.6362, "ner_oracle_f1": 0.792, "ner_headroom": 0.1559, "ner_fleiss_kappa_mean": 0.2488, "ner_soft_jaccard_mean": 0.5066, "ner_full_rho_sj": 0.3808, "ner_full_rho_fk": 0.3362, "ner_full_p_sj": 1.07e-19, "ner_full_p_fk": 1.93e-15, "ner_full_n": 529, "ner_cond_rho_sj": 0.3836, "ner_cond_rho_fk": 0.3187, "ner_cond_p_sj": 1.83e-19, "ner_cond_p_fk": 1.33e-13, "ner_cond_n": 514, "ner_sj_beats_fk_full": true, "ner_sj_beats_fk_cond": true, "ner_rho_advantage": 0.0446, "ner_sample_f1_mean": 0.5153, "ner_sample_f1_std": 0.3334, "ner_sample_f1_pct_zero": 19.9, "ner_gold_empty_filtered": 22, "ner_all_zero_filtered": 15, "re_greedy_f1": 0.3774, "re_oracle_f1": 0.5939, "re_headroom": 0.2165, "re_fleiss_kappa_mean": 0.0879, "re_soft_jaccard_mean": 0.3958, "re_full_rho_sj": 0.2367, "re_full_rho_fk": 0.2221, "re_full_p_sj": 1.85e-06, "re_full_p_fk": 7.92e-06, "re_full_n": 397, "re_cond_rho_sj": 0.3004, "re_cond_rho_fk": 0.2374, "re_cond_p_sj": 2.25e-08, "re_cond_p_fk": 1.19e-05, "re_cond_n": 333, "re_sj_beats_fk_full": true, "re_sj_beats_fk_cond": true, "re_rho_advantage": 0.0146, "re_sample_f1_mean": 0.1977, "re_sample_f1_std": 0.3251, "re_sample_f1_pct_zero": 67.6, "re_gold_empty_filtered": 154, "re_all_zero_filtered": 64, "parse_failures_stochastic": 0, "parse_failures_greedy": 0, "total_stochastic_samples": 4408, "total_greedy": 551, "verdict": "FAIL", "verdict_reason": "RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but below PASS bar"}
1438	
1439	=== mvp_pilot_004 ===
1440	status: DONE
1441	hypothesis: 
1442	conclusion: negative
1443	created_at: "2026-05-14T08:51:38.203Z"
1444	updated_at: "2026-05-14T09:10:40.918Z"
1445	metrics: {"ner_greedy_f1": 0.6671, "ner_oracle_f1": 0.7756, "ner_headroom": 0.1085, "ner_fleiss_kappa_mean": 0.4048, "ner_soft_jaccard_mean": 0.7008, "ner_full_rho_fk": 0.259, "ner_full_rho_sj": 0.3825, "ner_full_n": 529, "ner_cond_rho_fk": 0.2352, "ner_cond_rho_sj": 0.3762, "ner_cond_n": 508, "ner_sj_beats_fk_full": true, "ner_sj_beats_fk_cond": true, "ner_sample_f1_mean": 0.6084, "ner_sample_f1_std": 0.3174, "ner_sample_f1_pct_zero": 12.19, "ner_gold_empty_filtered": 22, "ner_all_zero_filtered": 21, "re_greedy_f1": 0.4208, "re_oracle_f1": 0.5882, "re_headroom": 0.1674, "re_fleiss_kappa_mean": 0.2996, "re_soft_jaccard_mean": 0.6114, "re_full_rho_fk": 0.2782, "re_full_rho_sj": 0.2441, "re_full_n": 397, "re_cond_rho_fk": 0.3067, "re_cond_rho_sj": 0.3161, "re_cond_n": 313, "re_sj_beats_fk_full": false, "re_sj_beats_fk_cond": true, "re_sample_f1_mean": 0.3612, "re_sample_f1_std": 0.383, "re_sample_f1_pct_zero": 44.3, "re_gold_empty_filtered": 154, "re_all_zero_filtered": 84, "parse_failures": 0, "verdict": "FAIL"}
1446	
1447	=== mvp_pilot_005 ===
1448	status: DONE
1449	hypothesis: 
1450	conclusion: negative
1451	created_at: "2026-05-14T09:14:09.456Z"
1452	updated_at: "2026-05-14T09:47:06.597Z"
1453	metrics: {"ner_greedy_f1": 0.6619, "ner_oracle_f1": 0.7585, "ner_headroom": 0.0966, "ner_fleiss_kappa_mean": 0.4722, "ner_soft_jaccard_mean": 0.7757, "ner_full_rho_sj": 0.3875, "ner_full_rho_fk": 0.3211, "ner_full_n": 529, "ner_cond_rho_sj": 0.3868, "ner_cond_rho_fk": 0.305, "ner_cond_n": 504, "ner_sj_beats_fk_full": true, "ner_sj_beats_fk_cond": true, "ner_rho_advantage": 0.0664, "ner_sample_f1_mean": 0.6243, "ner_sample_f1_std": 0.3131, "ner_sample_f1_pct_zero": 11.2, "ner_gold_empty_filtered": 22, "ner_all_zero_filtered": 25, "re_greedy_f1": 0.4219, "re_oracle_f1": 0.5532, "re_headroom": 0.1313, "re_fleiss_kappa_mean": 0.3829, "re_soft_jaccard_mean": 0.687, "re_full_rho_sj": 0.2343, "re_full_rho_fk": 0.1835, "re_full_n": 397, "re_cond_rho_sj": 0.3716, "re_cond_rho_fk": 0.2533, "re_cond_n": 301, "re_sj_beats_fk_full": true, "re_sj_beats_fk_cond": true, "re_rho_advantage": 0.0508, "re_sample_f1_mean": 0.3782, "re_sample_f1_std": 0.3845, "re_sample_f1_pct_zero": 42.4, "re_gold_empty_filtered": 154, "re_all_zero_filtered": 96, "parse_failures": 0, "verdict": "FAIL", "verdict_note": "RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8913e3c0-bf05-450d-af2b-c81bbccac7c9",
  "isSidechain": true,
  "promptId": "9d5a8dbf-14d3-41c1-a18a-ef8acd67e6cb",
  "agentId": "a97ebe3840b34757a",
  "type": "user",
  "uuid": "fc50e01e-16b7-4153-9932-341f255097dc",
  "sourceToolAssistantUUID": "8913e3c0-bf05-450d-af2b-c81bbccac7c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-20T10:49:11.699Z_

I now have the complete registry. Let me compile the organized report.

---

## Complete Registry — All Confirmed Experimental Results

**Total experiments: 181** (reporting all with metrics; killed/failed experiments noted briefly)

---

### CORE QE SIGNAL RANKINGS (Spearman ρ, AUROC)

#### SciERC — Qwen3-8B FT, N=8, T=1.0, seed=42 (CANONICAL: exp_012_rerun_1024)

**degeneracy_rate**: 0.1777

**NER full** (n=529):
- SJ: ρ=0.3599, τ=0.2646, AUROC=0.6917, ECE=0.4531, ρ CI95=[0.2732, 0.4389], AUROC CI95=[0.6304, 0.7406]
- FK: ρ=0.2665, τ=0.1974, AUROC=0.6290, ECE=0.4512, ρ CI95=[0.1743, 0.3486], AUROC CI95=[0.5612, 0.6882]
- logprob (LP): ρ=0.2052, τ=0.1478, AUROC=0.5783, ECE=0.7064, ρ CI95=[0.1171, 0.2904], AUROC CI95=[0.5179, 0.6387]
- EM: ρ=0.2945, τ=0.2208, AUROC=0.7493, ECE=0.3526, ρ CI95=[0.2094, 0.3700], AUROC CI95=[0.7002, 0.7928]
- voting_conf (VC): ρ=0.3792, τ=0.2805, AUROC=0.6841, ECE=0.3807, ρ CI95=[0.2972, 0.4486], AUROC CI95=[0.6249, 0.7366]

**NER cond** (n=477):
- SJ: ρ=0.3113, τ=0.2257, AUROC=0.6772, ECE=0.4416, ρ CI95=[0.2353, 0.3959], AUROC CI95=[0.6210, 0.7337]
- FK: ρ=0.1761, τ=0.1284, AUROC=0.6078, ECE=0.4389, ρ CI95=[0.0839, 0.2665], AUROC CI95=[0.5442, 0.6709]
- logprob: ρ=0.1538, τ=0.1111, AUROC=0.5633, ECE=0.6803, ρ CI95=[0.0637, 0.2424], AUROC CI95=[0.5032, 0.6232]
- EM: ρ=0.3596, τ=0.2735, AUROC=0.7556, ECE=0.3257, ρ CI95=[0.2819, 0.4408], AUROC CI95=[0.7011, 0.8107]
- voting_conf: ρ=0.3000, τ=0.2189, AUROC=0.6618, ECE=0.3746, ρ CI95=[0.2168, 0.3836], AUROC CI95=[0.6004, 0.7201]

**RE full** (n=397):
- SJ: ρ=0.2503, τ=0.1878, AUROC=0.6702, ECE=0.3865
- FK: ρ=0.2752, τ=0.2117, AUROC=0.6089, ECE=0.4405
- logprob: ρ=0.2662, τ=0.1951, AUROC=0.6005, ECE=0.7694
- EM: ρ=0.1344, τ=0.1081, AUROC=0.7059, ECE=0.3548
- voting_conf: ρ=0.3498, τ=0.2663, AUROC=0.6935, ECE=0.2724

**RE cond** (n=238):
- SJ: ρ=0.2457, τ=0.1811, AUROC=0.6463, ECE=0.2941
- FK: ρ=0.1139, τ=0.0876, AUROC=0.5510, ECE=0.3424
- logprob: ρ=0.0112, τ=0.0051, AUROC=0.5186, ECE=0.6464
- EM: ρ=0.4165, τ=0.3256, AUROC=0.7515, ECE=0.2232
- voting_conf: ρ=0.2409, τ=0.1780, AUROC=0.6420, ECE=0.2070

Provenance note: voting_conf inflated in exp_015 (0.502→0.379) and logprob suppressed (0.140→0.205) due to max_tokens=512 truncation in earlier run; exp_012_rerun_1024 (max_tokens=1024) is canonical.

---

#### SciERC — Qwen3-8B FT, N=16, seeds 42/123/456 multi-seed

**exp_001_n16_seed456** (N=16, seed=456, n_valid=529, n_conditional=?):
- NER: greedy_f1=0.6617, oracle_f1=0.8075
- SJ ρ=0.4098, FK ρ=0.2723, VC ρ=0.4449, EM ρ=0.3363, LP ρ=0.2415
- AUROC: SJ=0.6823, FK=0.6179, VC=0.6981, EM=0.6490, LP=0.5885
- RE: greedy_f1=0.4215, oracle_f1=0.4748

**exp_001_ner_n16_seed123** (N=16, seed=123):
- NER: greedy_f1=0.663, oracle_f1=0.809, headroom=0.146
- SJ ρ=0.423, FK ρ=0.290, logprob ρ=0.239, SJ_cond=0.423, FK_cond=0.260
- RE: greedy_f1=0.419, oracle_f1=0.625, headroom=0.206, SJ ρ=0.267, FK ρ=0.315, SJ_cond=0.364, FK_cond=0.331

**exp_001_seed456_v2_ner** (seed=456, corrected pipeline):
- Full: SJ ρ=0.384 AUROC=0.711, FK ρ=0.223 AUROC=0.577, logprob ρ=0.232 AUROC=0.594, EM ρ=0.316 AUROC=0.768, VC ρ=0.411 AUROC=0.712
- Cond: SJ ρ=0.349 AUROC=0.699, FK ρ=0.157 AUROC=0.561, logprob ρ=0.171 AUROC=0.576, EM ρ=0.406 AUROC=0.780, VC ρ=0.346 AUROC=0.694
- 3-seed mean SJ_rho_full=0.412, SD=0.025

**exp_001_seed42_v2 / exp_001_seed123_v2** summary:
- seed42: sj_rho_full=0.428, sj_rho_cond=0.369, structural_minus_surface=0.147
- seed123: sj_rho_full=0.424, sj_rho_cond=0.376, structural_minus_surface=0.149

---

#### CoNLL-2003 — Qwen3-8B FT, N=16, seed=42 (exp_002_conll_n16)

n_instances=3453, n_valid=2756, n_conditional=2614, greedy_f1=0.907, degen_rate=0.4844

**Full:**
- SJ: ρ=0.4496, AUROC=0.8264, ECE=0.0747
- FK: ρ=0.3928, AUROC=0.7821, ECE=0.1786
- LP: ρ=0.3146, AUROC=0.7531, ECE=0.2031
- EM: ρ=0.4627, AUROC=0.8409, ECE=0.0786
- VC: ρ=0.4286, AUROC=0.8071, ECE=0.529

**Conditional:**
- SJ: ρ=0.4208, AUROC=0.8405, ECE=0.0982
- FK: ρ=0.3494, AUROC=0.7819, ECE=0.1899
- LP: ρ=0.3756, AUROC=0.8259, ECE=0.2504
- EM: ρ=0.4658, AUROC=0.8781, ECE=0.0997
- VC: ρ=0.3654, AUROC=0.7951, ECE=0.6096

N8→N16 Δρ full: SJ=+0.0139, FK=-0.007, LP=-0.0011, EM=+0.012, VC=+0.0049

Multi-seed (exp_002_conll_n16_seed123): degen_rate=0.471, greedy_f1=0.9068, oracle_f1=0.9633, FK ρ=0.4524, SJ ρ=0.4621
Multi-seed (exp_002_conll_n16_seed456): degen_rate=0.5544, greedy_f1=0.9074, oracle_f1=0.9549, FK ρ=0.4718, SJ ρ=0.4819

---

#### CoNLL-2003 — LLaMA-3.1-8B FT, N=16, seed=42 (exp_017_llama_conll_n16)

greedy_f1=0.9243, oracle_f1=0.9487, oracle_headroom=0.0244, n_valid=2756, n_conditional=2642

**Full:**
- SJ: ρ=0.4642, AUROC=0.7391, ECE=0.1131
- FK: ρ=0.4566, AUROC=0.7360, ECE=0.1071
- LP: ρ=0.3058, AUROC=0.7594, ECE=0.1288
- EM: ρ=0.4613, AUROC=0.7391, ECE=0.1084
- VC: ρ=0.4554, AUROC=0.7406, ECE=0.0844

**Conditional:**
- SJ: ρ=0.4597, AUROC=0.7565, ECE=0.0846
- FK: ρ=0.4515, AUROC=0.7530, ECE=0.0813
- LP: ρ=0.3193, AUROC=0.8023, ECE=0.0921
- EM: ρ=0.4618, AUROC=0.7589, ECE=0.0757
- VC: ρ=0.3978, AUROC=0.7287, ECE=0.0742

**Best-of-N selection F1:** greedy=0.9243, random=0.9213, SJ=0.9259, LP=0.9250, VC=0.9268, oracle=0.9487

N8→N16 Δρ: SJ_full=+0.0328, FK_full=+0.0289, LP_full=-0.0014, EM_full=+0.0307, VC_full=+0.0298

**LLaMA CoNLL 3-seed summary** (exp_017_llama_conll, r1024 corrected):
- seed42 (exp_017_llama_conll_n16_r1024): degen_rate=0.8647, greedy_f1=0.9265, oracle_f1=0.9499, SJ ρ=0.4836, FK ρ=0.4752, VC ρ=0.4746, EM ρ=0.4818, LP ρ=0.3136; AUROC: SJ=0.7496, FK=0.7467, VC=0.7529, EM=0.7508, LP=0.7661
- seed123 (exp_017_llama_conll_n16_s123_r1024): degen_rate=0.8636
- seed456 (exp_017_llama_conll_n16_s456_r1024): degen_rate=0.8672, greedy_f1=0.9265, oracle_f1=0.9499, SJ ρ=0.4734, FK ρ=0.4690, VC ρ=0.4722, EM ρ=0.4752, LP ρ=0.3099; AUROC: SJ=0.7428, FK=0.7408, VC=0.7495, EM=0.7444, LP=0.7628

**LLaMA CoNLL 3-seed aggregate** (exp_017_llama_conll):
- qe_rho_full_3seed: SJ mean=0.4631 SD=0.0074, FK mean=0.4546 SD=0.0061, EM mean=0.4603 SD=0.0078, VC mean=0.4579 SD=0.0030, LP mean=0.3099 SD=0.0055
- qe_auroc_full_3seed: SJ mean=0.736 SD=0.0064, FK mean=0.732 SD=0.0063, EM mean=0.7355 SD=0.0069, VC mean=0.7394 SD=0.0041, LP mean=0.7629 SD=0.0044
- degeneracy_cf1_gold_filtered=0.894, n_constant_f1=2465/2756
- greedy_f1=0.9239, oracle_f1=0.9451, random_f1=0.9207, headroom_pp=2.11
- LP: lp_range mean=0.0198, std=0.0315, median=0.0002

---

#### LLaMA-3.1-8B FT — SciERC, N=8/16, seeds 42/123/456

**exp_018_llama_scierc_seed42_r1024** (N=16, max_tokens=1024):
degen_rate=0.2495

NER full (n=529): SJ ρ=0.3096 AUROC=0.6683, FK ρ=0.2352 AUROC=0.6069, LP ρ=0.1503 AUROC=0.5318, EM ρ=0.2587 AUROC=0.7174, VC ρ=0.4053 AUROC=0.6967
NER cond (n=478): SJ ρ=0.2718 AUROC=0.6565, FK ρ=0.1472 AUROC=0.5866, LP ρ=0.0810 AUROC=0.5129, EM ρ=0.3165 AUROC=0.7244, VC ρ=0.3078 AUROC=0.6714
greedy_f1=0.6607, oracle_f1=0.7781

RE full (n=397): SJ ρ=0.2748 AUROC=0.7244, FK ρ=0.3027 AUROC=0.6910, LP ρ=0.3163 AUROC=0.6313, EM ρ=0.1681 AUROC=0.7697, VC ρ=0.3840 AUROC=0.7337
RE cond (n=251): SJ ρ=0.3461 AUROC=0.7233, FK ρ=0.1969 AUROC=0.6684, LP ρ=0.0888 AUROC=0.5556, EM ρ=0.4969 AUROC=0.8190, VC ρ=0.3433 AUROC=0.7003
greedy_f1=0.4319, oracle_f1=0.5775

**exp_018_llama_scierc_seed456_r1024**: degen_rate=0.2741, greedy_f1(NER)=0.6597, oracle_f1=0.7683, greedy_f1(RE)=0.4338, oracle_f1(RE)=0.5834; NER_cond SJ ρ=0.2718, FK ρ=0.1472; RE_cond SJ ρ=0.3898, FK ρ=0.2107

**exp_018_llama_scierc_seed123**: degen_rate=0.2665

**exp_llama_scierc_seed456** (alternative): greedy_f1=0.6457, oracle_f1=0.7574, degen_rate=0.2741; SJ ρ_full=0.3663, FK ρ=0.3115, LP ρ=0.1911, EM ρ=0.3088, VC ρ=0.4135; AUROC: SJ=0.7061, EM=0.7538

**exp_007_llama_scierc_seed123**: greedy_f1=0.6454, oracle_f1=0.7657, degen_rate=0.2665; SJ ρ_full=0.3552, VC ρ_full=0.4193; AUROC: SJ=0.7092, EM=0.7468; DGS delta=-0.38pp

---

#### FewNERD — Qwen3-8B FT, N=8, seed=42 (exp_021_fewnerd_full)

n_instances=37648, n_valid=32565 (gold-filtered), N=8, degen_rate=0.101 (scenario=A_partial)
greedy_f1=0.7478, oracle_f1=0.8719, headroom=0.124, zero_f1_rate=0.119

Signal ρ (global): LP=0.4215, VC=0.3858, FK=0.3132, SJ=0.3002, EM=0.2871
Signal ρ (cond): LP=0.4225, VC=0.3234, FK=0.3093, SJ=0.2937, EM=0.2710
Sample AUROC: LP=0.5782, VC=0.5354, FK=0.5210, SJ=0.5197, EM=0.5137

Selection Δ (pp): LP=+1.36, VC=-1.79, SJ=-2.14, FK=-2.26, EM=-3.85
LP bootstrap CI95: [1.18, 1.53]

LP range (within-instance): mean=0.0879, median=0.0662

**Multi-seed** (exp_021_fewnerd_n8_seed123): degen_rate=0.1312, greedy_f1=0.7885, oracle_f1=0.8892, FK ρ=0.1602, SJ ρ=0.3083, zero_f1_rate=20.39%
**Multi-seed** (exp_021_fewnerd_n8_seed456): degen_rate=0.1212, greedy_f1=0.7888, oracle_f1=0.8810, FK ρ=0.1632, SJ ρ=0.3130, zero_f1_rate=19.32%

---

#### FewNERD — LLaMA-3.1-8B FT, N=8, 3-seed (exp_llama_fewnerd_inference)

3-seed mean: greedy_f1=0.7842, oracle_f1=0.8843, headroom_pp=10.01, degeneracy_pct=23.36, LP_delta_pp=+0.36, DGS_delta_pp=-0.35
- seed42: greedy=0.7841, oracle=0.8854, degen=27.32%
- seed123: greedy=0.7840, oracle=0.8839, degen=24.63%
- seed456: greedy=0.7844, oracle=0.8835, degen=18.13%

Signal ranking (delta): LP (+0.36) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)
n_instances_gold_filtered=32565

---

#### FewNERD — Qwen2.5-7B FT, N=8, 3-seed (exp_qwen25_7b_fewnerd)

3-seed mean: LP ρ=0.346±0.021, SJ ρ=0.388±0.029, VC ρ=0.404±0.010, degen=31.7%±0.9%, greedy_f1=0.784±0.001, oracle_f1=0.876±0.003, construction_LP_delta=-0.11±0.25pp

Per seed:
- seed42: LP ρ=0.3221, SJ ρ=0.3554, VC ρ=0.393, degen=31.1%, greedy=0.7851, oracle=0.8718, LP_delta=-0.40pp, p=1.000, CI=[-0.53,-0.26], d=-0.0319
- seed123: LP ρ=0.3538, SJ ρ=0.3979, VC ρ=0.4067, degen=32.8%, greedy=0.785, oracle=0.8777, LP_delta=-0.03pp, p=0.651
- seed456: LP ρ=0.3629, SJ ρ=0.4105, VC ρ=0.4118, degen=31.3%, greedy=0.7825, oracle=0.8771, LP_delta=+0.09pp, p=0.168

construction_significant=false

---

#### FewNERD — N=16 (exp_027_fewnerd_n16)

LP_delta_pp=1.88, LP_delta_95CI=[1.41, 2.37], degen_rate=0.0706, greedy_f1=0.7478, lp_sel_f1=0.7666, oracle_f1=0.9020, headroom_pp=15.42, all_8_types_positive=true, n=5000, N=16, bootstrap_p="<0.001"

**4-seed mean (exp_fewnerd_s789_n8, seed=789):**
four_seed_mean_greedy=0.7481, four_seed_mean_LP_delta_pp=1.38, four_seed_LP_delta_CI95=[1.32, 1.44]
seed789: greedy=0.7478, oracle=0.8714, degen=0.1177, LP_sel=0.7614, LP_delta=+1.36pp, DGS_f1=0.7621, DGS_delta=+1.43pp, LP ρ_global=0.1788, LP ρ_cond=0.1760

---

#### FewNERD — 5-epoch ablation (exp_028_fewnerd_5epoch = exp_028)

degen_cf1_gold=0.3133 (vs 3-epoch 0.101), greedy_f1=0.7773, lp_sel_delta_pp=0.624, lp_sel_f1=0.7835, oracle_f1=0.8723, within_instance_rho_mean=0.4066, within_instance_rho_median=0.6151

---

### SAMPLE SELECTION: Best-of-N F1 vs Greedy

#### SciERC NER, various N (exp_010_selection_curves, exp_016_v2)

N=16: oracle=0.787, SJ=0.620, FK=0.621, LP=0.621, VC=0.585, EM=0.606, random=0.595 | greedy=0.618
N=8: oracle=0.752, SJ=0.614, FK=0.614, LP=0.619, VC=0.591, EM=0.603, random=0.589
N=4: oracle=0.714, SJ=0.607, FK=0.608, LP=0.616, VC=0.594, EM=0.600, random=0.587

**exp_016_v2** (NER, gold-filtered n=529): greedy=0.6442, LP_best=0.6505, ensemble_best=0.6475, SJ_best=0.6471, oracle=0.8442; best_single_rho: SJ=0.4412; best_combo: sj+vc_a0.55=0.4552; ensemble_auroc=0.7141

**Bootstrap significance** (exp_016_rerun_1024_bootstrap): NER LP vs greedy: CI95=[-0.03, 0.042], permutation_p=0.39, cohen_d=0.038, sign_test_win_rate=0.466. delta=+0.006. **Conclusion: no signal significantly outperforms greedy on selection F1.**

#### SciERC RE (exp_010, exp_016_v2)

N=16: oracle=0.631, SJ=0.397, FK=0.396, LP=0.410, VC=0.408, EM=0.381, random=0.364 | greedy=0.403
N=8: oracle=0.583, SJ=0.393, FK=0.394, LP=0.413, VC=0.398, EM=0.381, random=0.363

exp_016_v2 RE (n=397): greedy=0.403, LP_best=0.4097, ensemble_best=0.4227, oracle=0.6306; best_single_rho: VC=0.3849; best_combo: logprob+vc_a0.25=0.3936

#### CoNLL NER (exp_010)

N=8: oracle=0.757, SJ=0.718, FK=0.717, LP=0.716, VC=0.714, EM=0.716, random=0.690 | greedy=0.725
N=4: oracle=0.746, SJ=0.714, FK=0.714, LP=0.715, VC=0.714, EM=0.712, random=0.692

**LLaMA CoNLL N=16 best-of-N** (exp_017_llama_conll_n16):
greedy=0.9243, random=0.9213, SJ=0.9259, LP=0.9250, VC=0.9268, oracle=0.9487

**LLaMA CoNLL N=16 DGS** (exp_017_llama_conll, aggregate):
DGS_f1=0.9254, DGS_delta_pp=+0.14, DGS_nondegen_LP_delta_pp=+1.37

Selection F1 per signal (3-seed aggregate): SJ=0.9237 (Δ=-0.04pp), FK=0.9240 (Δ=-0.02pp), VC=0.9250 (Δ=+0.08pp), EM=0.9244 (Δ=+0.02pp), LP=0.9244 (Δ=+0.02pp)

---

### ENTITY CONSTRUCTION (Majority Vote, LP-weighted)

#### exp_entity_construction (5-fold CV, bootstrap B=10000)

**N=16, fair CV:**
- SciERC NER: uniform Δ=+1.35pp, p=0.018 (significant)
- CoNLL NER: uniform Δ=+0.10pp, p=0.303 (not significant)
- FewNERD NER: uniform Δ=+1.32pp, p=0.000 (significant)
- SciERC RE: uniform Δ=+1.69pp, p=0.049 (significant)

**N=8, fair CV:**
- SciERC NER: uniform=+1.54pp (p=0.023 sig), LP-weighted=+1.67pp (p=0.004 sig), CV_uniform=+1.12pp (p=0.057 borderline)
- CoNLL NER: CV_uniform=-0.39pp (p=0.963, not sig)
- FewNERD NER: LP-weighted CV=+0.88pp (p=0.000 sig), uniform CV=+0.32pp (p=0.003 sig)

adaptive_combination: INVALIDATED (gold label leakage)

#### exp_qwen25_72b_zeroshot — LP-weighted construction

SciERC: LP-weighted_f1=0.4146 (greedy=0.3993, delta=+1.53pp, bootstrap_p=0.0082, CI=[0.0025,0.0282], Cohen's d=0.1027); non_degen_delta_pp=+1.65, non_degen_p=0.0069; uniform_delta=-0.52pp; MV_f1=0.4132; oracle=0.5489
CoNLL: LP-weighted_delta=-0.37pp; uniform_delta=-0.92pp
FewNERD: LP-weighted_delta=-0.20pp; uniform_delta=-1.70pp; MV_f1=0.6262

---

### INSTANCE DEGENERACY RATES

Per dataset/model (degen_rate = fraction constant_F1, gold-filtered):

| exp_id | dataset | model | N | T | degen_rate |
|--------|---------|-------|---|---|------------|
| exp_012_rerun_1024 | SciERC | Qwen3-8B FT | 8 | 1.0 | 0.1777 |
| exp_018_qwen_scierc_seed123 | SciERC | Qwen3-8B FT | 8 | 1.0 | 0.172 |
| exp_018_qwen_scierc_seed456 | SciERC | Qwen3-8B FT | 8 | 1.0 | 0.2042 |
| exp_018_llama_scierc_seed42_r1024 | SciERC | LLaMA-8B FT | 8 | 1.0 | 0.2495 |
| exp_018_llama_scierc_seed456_r1024 | SciERC | LLaMA-8B FT | 8 | 1.0 | 0.2741 |
| exp_018_llama_scierc_seed123 | SciERC | LLaMA-8B FT | 8 | 1.0 | 0.2665 |
| exp_007_llama_scierc_seed123 | SciERC | LLaMA-8B FT | 8 | 1.0 | 0.2665 |
| exp_llama_scierc_seed456 | SciERC | LLaMA-8B FT | 8 | 1.0 | 0.2741 |
| exp_002_conll_n16 | CoNLL | Qwen3-8B FT | 16 | 1.0 | 0.4844 |
| exp_002_conll_n16_seed123 | CoNLL | Qwen3-8B FT | 16 | 1.0 | 0.471 |
| exp_002_conll_n16_seed456 | CoNLL | Qwen3-8B FT | 16 | 1.0 | 0.5544 |
| exp_017_llama_conll_n16_r1024 | CoNLL | LLaMA-8B FT | 16 | 1.0 | 0.8647 |
| exp_017_llama_conll_n16_s123_r1024 | CoNLL | LLaMA-8B FT | 16 | 1.0 | 0.8636 |
| exp_017_llama_conll_n16_s456_r1024 | CoNLL | LLaMA-8B FT | 16 | 1.0 | 0.8672 |
| exp_017_llama_conll_finetune | CoNLL | LLaMA-8B FT | 8 | 1.0 | 0.853 |
| exp_021_fewnerd_full | FewNERD | Qwen3-8B FT | 8 | 1.0 | 0.101 |
| exp_021_fewnerd_n8_seed123 | FewNERD | Qwen3-8B FT | 8 | 1.0 | 0.1312 |
| exp_021_fewnerd_n8_seed456 | FewNERD | Qwen3-8B FT | 8 | 1.0 | 0.1212 |
| exp_027_fewnerd_n16 | FewNERD | Qwen3-8B FT | 16 | 1.0 | 0.0706 |
| exp_fewnerd_s789_n8 | FewNERD | Qwen3-8B FT | 8 | 1.0 | 0.1177 |
| exp_llama_fewnerd (seed42) | FewNERD | LLaMA-8B FT | 8 | 1.0 | 0.2732 |
| exp_llama_fewnerd (seed123) | FewNERD | LLaMA-8B FT | 8 | 1.0 | 0.2463 |
| exp_llama_fewnerd (seed456) | FewNERD | LLaMA-8B FT | 8 | 1.0 | 0.1813 |
| exp_qwen25_7b_fewnerd (seed42) | FewNERD | Qwen2.5-7B FT | 8 | 1.0 | ~0.311 |
| exp_qwen3_4b_conll_scs_inference_v2 | CoNLL | Qwen3-4B FT | 8 | 1.0 | 0.9057 |
| exp_qwen3_4b_scierc_scs_inference | SciERC | Qwen3-4B FT | 8 | 1.0 | 0.104 |
| exp_qwen25_72b_zeroshot | SciERC | Qwen2.5-72B ZS | 8 | 1.0 | 0.21 |
| exp_qwen25_72b_zeroshot | CoNLL | Qwen2.5-72B ZS | 8 | 1.0 | 0.677 |
| exp_qwen25_72b_zeroshot | FewNERD | Qwen2.5-72B ZS | 8 | 1.0 | 0.462 |

**Degeneracy regression** (exp_a2_degen_regression): n=30 points, linear R²=0.414, quadratic R²=0.592, Spearman ρ=0.519, p=0.0033; linear_coeff="degen = 129.5 × F1 − 56.9"; key finding: degeneracy driven by dataset difficulty (entropy ceiling), not model capability.

---

### TEMPERATURE ABLATIONS (exp_026_*)

SciERC, Qwen3-8B FT, N=8 (seed=42 canonical):

| T | degen_rate | greedy_f1 | oracle_f1 | SJ ρ | FK ρ | LP ρ | VC ρ | LP_sel_f1 | SJ_sel_f1 | lp_range_mean |
|---|-----------|-----------|-----------|------|------|------|------|-----------|-----------|---------------|
| 0.5 | 0.414 | 0.617 | 0.710 | 0.333 | 0.341 | 0.208 | 0.353 | 0.622 | 0.622 | 0.022 |
| 0.8 | 0.2382 | 0.616 | 0.737 | 0.378 | 0.340 | 0.212 | 0.352 | 0.627 | 0.619 | 0.043 |
| 1.0 | 0.1777 | ~0.661 | ~0.779 | 0.3599 | 0.2665 | 0.2052 | 0.3792 | 0.6465 | 0.620 | ~0.062 |
| 1.2 | 0.1493 | 0.620 | 0.758 | 0.384 | 0.386 | 0.182 | 0.342 | 0.621 | 0.597 | 0.075 |

Within-instance ρ (mean/median/valid_pct): T=0.5: 0.1306/0.2182/59.7%, T=0.8: 0.1701/0.2635/72.8%, T=1.2: 0.2245/0.3152/87.5%

**Multi-seed T-ablation** (3 seeds ×3 temperatures on SciERC):
- T=0.5 seed123: greedy=0.6611, oracle=0.7444, SJ ρ=0.3133, zero%=10.09
- T=0.5 seed456: greedy=0.6639, oracle=0.7437, SJ ρ=0.3279, zero%=10.28
- T=0.8 seed123: greedy=0.6607, oracle=0.7714, SJ ρ=0.3893, zero%=11.22
- T=0.8 seed456: greedy=0.6641, oracle=0.7694, SJ ρ=0.3771, zero%=11.79
- T=1.0 seed42: greedy=0.6617, oracle=0.7798, SJ ρ=0.3598, zero%=12.90
- T=1.0 seed123: greedy=0.6633, oracle=0.7777, SJ ρ=0.3809, zero%=12.59
- T=1.0 seed456: greedy=0.6621, oracle=0.7754, SJ ρ=0.3921, zero%=12.97
- T=1.2 seed123: greedy=0.6595, oracle=0.7895, SJ ρ=0.3590, zero%=13.99
- T=1.2 seed456: greedy=0.6637, oracle=0.7821, SJ ρ=0.3995, zero%=14.08

**LLaMA CoNLL T=0.7** (exp_017_llama_conll_n8_t07): greedy=0.9242, oracle=0.9391, lp_range_median=1.1e-5, lp_tied_0.05=95.79%; SJ ρ=0.3934 AUROC=0.6506, FK ρ=0.3879 AUROC=0.6488, VC ρ=0.3750 AUROC=0.6551, EM ρ=0.3888 AUROC=0.6494, LP ρ=0.2951 AUROC=0.7509; sel_F1: SJ=0.9247, FK=0.9254, VC=0.9264, EM=0.9255, LP=0.9248

---

### EPOCH ABLATIONS

SciERC epochs (parent: ft_002_v2, Qwen3-8B):
- 3-epoch (exp_029a): degen_rate=0.064
- 5-epoch canonical (exp_012_rerun_1024): degen_rate=0.1777
- 10-epoch (exp_029b): degen_rate=0.478

FewNERD epochs (Qwen3-8B):
- 3-epoch (exp_021_fewnerd_full): degen=0.101, greedy=0.7478, LP_delta=+1.36pp
- 5-epoch (exp_028_fewnerd_5epoch): degen_cf1_gold=0.3133, greedy=0.7773, LP_delta=+0.624pp

---

### ORACLE HEADROOM

| Dataset | Model | N | greedy_f1 | oracle_f1 | headroom |
|---------|-------|---|-----------|-----------|---------|
| SciERC NER | Qwen3-8B FT | 8 | ~0.661 | ~0.779 | ~0.118 |
| SciERC NER | Qwen3-8B FT | 16 | 0.661 | 0.809 | 0.148 |
| SciERC NER | Qwen3-4B FT | 8 | 0.6612 | 0.7839 | 0.1228 |
| SciERC NER | LLaMA-8B FT | 8 | 0.660 | 0.778 | 0.118 |
| SciERC NER | LLaMA-3B FT | 8 | 0.6267 | 0.763 | 0.1363 |
| SciERC RE | Qwen3-8B FT | 8 | ~0.432 | ~0.578 | ~0.146 |
| CoNLL NER | Qwen3-8B FT (N=8) | 8 | 0.9123 | 0.9543 | 0.042 |
| CoNLL NER | Qwen3-8B FT (N=16) | 16 | 0.907 | — | — |
| CoNLL NER | Qwen3-4B FT | 8 | 0.9234 | 0.9404 | 0.0170 |
| CoNLL NER | LLaMA-8B FT | 16 | 0.9243 | 0.9487 | 0.0244 |
| FewNERD NER | Qwen3-8B FT | 8 | 0.7478 | 0.8719 | 0.124 |
| FewNERD NER | Qwen3-8B FT | 16 | 0.7478 | 0.9020 | 0.1542 |
| FewNERD NER | LLaMA-8B FT | 8 | 0.7842 | 0.8843 | 0.1001 |

---

### SCALING EXPERIMENTS

#### Model scale ablation (Qwen3: 4B vs 8B)

**SciERC NER:**
- 4B (exp_qwen3_4b_scierc_scs_inference): greedy=0.6612, oracle=0.7839, degen=0.104, SJ ρ=0.4221, FK ρ=0.3258, LP ρ=0.2800
- 8B canonical: greedy~0.661, oracle~0.779, degen=0.1777, SJ ρ=0.3599, FK ρ=0.2665, LP ρ=0.2052

**CoNLL NER:**
- 4B (exp_qwen3_4b_conll_scs_inference_v2): greedy=0.9234, oracle=0.9404, degen=0.9057, SJ ρ_full=0.4217, FK ρ_full=0.4181, LP ρ_full=0.3313, SJ_cond=0.4590, FK_cond=0.4538, LP_cond=0.3487; LP_auroc_full=0.7761, LP_auroc_cond=0.8209
- 8B N=16: greedy=0.907, degen=0.4844, SJ ρ=0.4496, FK ρ=0.3928, LP ρ=0.3146

**LLaMA-3B SciERC** (exp_llama3b_scierc_ablation):
NER full (n=529): SJ ρ=0.3754 AUROC=0.7383, FK ρ=0.2676 AUROC=0.6714, LP ρ=0.2662 AUROC=0.6330, EM ρ=0.3341 AUROC=0.7763, VC ρ=0.4602 AUROC=0.7429
NER cond (n=476): SJ ρ=0.3445, FK ρ=0.2125, LP ρ=0.2099, EM ρ=0.3952, VC ρ=0.3815
greedy=0.6267, oracle=0.763, headroom=0.1363; structural_beats_surface=true, SJ>FK advantage=0.1078

Selection F1: SJ=0.6328, FK=0.6295, LP=0.6279, EM=0.6174, VC=0.6113

#### N-scaling (exp_025_n32, SciERC NER, N=32)

degen_pct=4%, lp_range=0.0781, oracle=0.8412, greedy=0.6615, oracle_gap=0.1797
Selection delta (pp): LP=+0.54, SJ=+0.16, FK=+0.60, EM=+0.68, VC=-5.21; best=EM (+0.68pp)

N=4/8/16 comparison (exp_010): oracle gap expands monotonically with N; structural signals barely improve selection F1 despite improving ρ

#### 72B zero-shot (exp_qwen25_72b_zeroshot)

SciERC: greedy=0.3993, LP ρ=0.081, VC ρ=0.277, SJ ρ=0.217, degen=0.21
CoNLL: greedy=0.7120, LP ρ=-0.002, VC ρ=0.297, SJ ρ=0.304, degen=0.677
FewNERD: greedy=0.6281, LP ρ=0.119, VC ρ=0.416, SJ ρ=0.345, degen=0.462

---

### FREE-FORM vs CONSTRAINED DECODING

**exp_freeform_ablation** (SciERC, seed=42): LP_std_ratio=0.97, LP_range_ratio=0.96, tied_constrained=59.7%, tied_freeform=57.7%; NER selection gap constrained=+0.0059, freeform=+0.0018; VC ρ constrained=0.3792, freeform=0.4089

**exp_freeform_seed123**: freeform tied_pct=57.7%, NER gap=+0.0028, RE gap=+0.0176; VC ρ_NER=0.408, SJ ρ_NER=0.384; LP ρ_NER=0.217; constraint vs free variance_ratio=0.97/0.96

**exp_freeform_seed456**: freeform tied=58.4%; NER gap=+0.0007, RE gap=+0.020; variance_ratio_std=0.90, variance_ratio_range=0.91, tied_reduction=1.3pp

**exp_freeform_seed789**: freeform tied=59.0%; NER gap=+0.0027, RE gap=+0.019; variance_ratio_std=0.89, variance_ratio_range=0.88, tied_reduction=0.7pp

**exp_freeform_conll_4seed** (seeds 42/123/456/789, N=8, T=1.0, n=2756):
greedy=0.9035±0.0004, oracle=0.9460±0.0023, LP_range_median=0.0581±0.0072; ρ: SJ=0.4606±0.0188, FK=0.4372±0.0209, EM=0.4714±0.0168, VC=0.4606±0.0138, LP=0.3262±0.0120; sel_F1: SJ=0.8994±0.0014, VC=0.9006±0.0026, LP=0.8958±0.0009

---

### ADDITIONAL SIGNAL/ABLATION EXPERIMENTS

#### RE diagnostic per relation type (exp_004_re_diagnostic)

- HYPONYM-OF: n=36, SJ ρ=0.545, FK ρ=0.646, VC ρ=0.628, mean_F1=0.513
- CONJUNCTION: n=86, SJ ρ=0.383, FK ρ=0.350, VC ρ=0.484, mean_F1=0.480
- USED-FOR: n=299, SJ ρ=0.236, FK ρ=0.255, VC ρ=0.286, mean_F1=0.422
- PART-OF: n=44, SJ ρ=0.239, FK ρ=0.348, VC ρ=0.283, mean_F1=0.297
- EVALUATE-FOR: n=62, SJ ρ=0.172, FK ρ=0.255, VC ρ=0.226, mean_F1=0.365
- COMPARE: n=35, SJ ρ=0.168, FK ρ=0.184, VC ρ=0.180, mean_F1=0.453
- FEATURE-OF: n=50, SJ ρ=0.004, FK ρ=0.052, VC ρ=0.014, mean_F1=0.254

Fisher-z NER vs RE: SJ z=2.31, p=0.0209, significant=true; FK z=-0.31, p=0.756, not sig; voting z=1.914, p=0.0556, not sig

Error propagation: total_FN=553; tail_error%=21.9, full_error%=21.7, head_error%=17.7, head_tail_error%=15.9, type_error%=8.3; entity span errors account for 55.5% of RE FN

Bootstrap CI95: NER_SJ=[0.2946,0.4586], NER_VC=[0.3048,0.4656], RE_SJ=[0.1422,0.3391], RE_VC=[0.1818,0.3721], RE_cond_SJ=[0.2161,0.4102], RE_cond_VC=[0.2825,0.4740]

#### CoNLL canonical (exp_002, N=8, T=1.0, n=2756)

SJ: ρ=0.4357, τ=0.3851, AUROC=0.8008, ρ_cond=0.4511
FK: ρ=0.3998, τ=0.3568, AUROC=0.7741, ρ_cond=0.4064
LP: ρ=0.3157, τ=0.2469, AUROC=0.7532, ρ_cond=0.3562
EM: ρ=0.4507, τ=0.4002, AUROC=0.8156, ρ_cond=0.4799
EV (voting): ρ=0.4237, τ=0.3777, AUROC=0.7889, ρ_cond=0.4127

greedy=0.9123, oracle=0.9543, voting_f1=0.9141; oracle_headroom=0.042
SJ vs LP Δρ=0.120, CI=[0.0881,0.154], significant=true
n_instances=3453, n_valid=2756

#### RE SJ component analysis (e1_component_wise_re_sj)

Full set (n=397): head_SJ ρ=0.210, tail_SJ ρ=0.201, type_match ρ=0.201, multiplicative ρ=0.244, additive ρ=0.243, Fleiss_κ ρ=0.278
Cond set (n=313): head_SJ ρ=0.270, tail_SJ ρ=0.259, type_match ρ=0.252, multiplicative ρ=0.316, additive ρ=0.306, Fleiss_κ ρ=0.307
Diagnosis: "head_SJ ρ=0.210 FAR from NER ρ=0.383. Multiplicative penalty hypothesis REJECTED."

#### LoRA rank ablation (exp_023_lora_rank8, r=8 vs canonical r=32)

NER full (n=529): greedy=0.6397, oracle=0.7998, degen=0.072; SJ ρ=0.3649 AUROC=0.689, FK ρ=0.2838 AUROC=0.6002, VC ρ=0.3940 AUROC=0.6886, EM ρ=0.2562 AUROC=0.7265, LP ρ=0.2105 AUROC=0.6054; sel_F1: SJ=0.6306, FK=0.6265, LP=0.6350, EM=0.6073, VC=0.5919
NER cond (n=477): SJ ρ=0.3056, FK ρ=0.1452, VC ρ=0.3191, EM ρ=0.3558, LP ρ=0.1690
RE full (n=397): greedy=0.3712, oracle=0.6090, degen=0.217; SJ ρ=0.2244 AUROC=0.7092, FK ρ=0.3448 AUROC=0.6469, VC ρ=0.3617 AUROC=0.7533, EM ρ=0.0680 AUROC=0.7306, LP ρ=0.2737 AUROC=0.6325

#### Ensemble signals (exp_016_signal_ensemble)

SJ-LP Pearson NER=0.57, RE=0.42; best_linear NER: SJ+VC α=0.3, ρ=0.489; best_linear RE: VC+LP α=0.6, ρ=0.429
Ensemble AUROC: NER=0.735, RE=0.719; best_single AUROC: NER=0.700, RE=0.721; ensemble NER Δ=+0.035
Selection F1 NER: greedy=0.609, LP=0.609, SJ=0.604, ensemble=0.604, voting=0.596, random=0.580, oracle=0.769
Selection F1 RE: LP=0.397, greedy=0.374, SJ=0.368, ensemble=0.367, voting=0.338, random=0.338, oracle=0.561

#### MLP verifier (exp_027_mlp_verifier) — negative

LR AUROC=0.6522, MLP AUROC=0.6381, RF AUROC=0.5868, MLP_15feat AUROC=0.6341; LR_sel_f1=0.6406, MLP_sel_f1=0.6278; greedy=0.6441, oracle=0.8231; best_single_signal AUROC=0.6476; feature_bottleneck_confirmed=true

#### Entity-token LP (exp_028_entity_token_lp) — negative

SciERC: greedy=0.643, oracle=0.7845; full_LP_global_ρ=0.2971, entity_text_type_LP_global_ρ=0.4401; full_LP_sel_F1=0.6465, entity_lp_sel_F1=0.6357; entity_delta_vs_full=-0.0203; dilution_ratio=0.32; full_LP within_range_median=0.0402, entity within_range_median=0.1346, schema_only within_range_median=0.0089
CoNLL: greedy=0.9065, oracle=0.948; full_LP_sel=0.8989, entity_LP_sel=0.8659; entity_delta_vs_full=-0.033; CoNLL entity tokens saturated (79.4% tied), SciERC entity tokens sparse (5.3% of total)

#### Verbalized confidence (exp_verbalized_confidence) — negative

SciERC: VerbConf ρ=0.2965, AUROC=0.6811, sel_F1=0.6195, delta=-0.0245 vs greedy; best_existing ρ=0.3792; VerbConf mean=8.58, std=1.15; parse_fail=0.26%
CoNLL: VerbConf ρ=0.3366, AUROC=0.7469, sel_F1=0.8886, delta=-0.0193; best_existing ρ=0.4507; mean=9.24, std=1.32; parse_fail=0

#### VC quartile analysis (exp_vc_quartile_analysis)

SciERC NER (n=529): Q1_LP_delta=+0.016, Q2=-0.006, Q3=+0.020, Q4=-0.004; Q4_mean_VC=0.921, Q1_headroom=0.169, Q4_headroom=0.048; overall_LP_delta=+0.006
SciERC RE (n=397): Q1=-0.036, Q2=-0.021, Q3=-0.022, Q4=+0.040; Q4_mean_VC=0.894; overall=-0.009
CoNLL NER (n=2756): Q1=-0.037, Q2=-0.005, Q3=0, Q4=0; overall=-0.010; Q3/Q4 degenerate

#### OOD transfer (exp_011_*)

CoNLL→SciERC (exp_011_ood_conll_to_scierc): greedy_NER=0.009, greedy_RE=0.001, avg_structural_ρ=-0.05, schema_incompatibility catastrophic, NER zero%=98.06%, SJ ρ=-0.186, FK ρ=-0.069
SciERC→CoNLL (exp_011_ood_scierc_to_conll): greedy_NER=0.522, VC ρ=0.469, SJ ρ=0.378, EM ρ=0.300, FK ρ=0.285, LP ρ=0.246

#### Selective prediction (exp_selective_prediction)

VC best signal; F1 at 80% coverage: SciERC=+5.0pp, CoNLL=+8.4pp, FewNERD=+6.2pp

#### LP alignment gating (exp_lp_alignment_gating)

adjusted_score = mean_ρ × valid_ratio; threshold=0.3; accuracy=3/3 datasets correct; robust_range=[0.2, 0.4]

#### Adaptive sampling budget (exp_adaptive_sampling_budget)

FewNERD: greedy=0.7884, uniform_N8=0.7819; best_adaptive=h1_l8 (greedy for high-conf, N=8 for low), adaptive_F1=0.7849, delta_vs_U8=+0.30pp, sample_savings=43.8%
SciERC: greedy=0.6592, uniform_N8=0.6712; best_adaptive=top67%_h2_l8, adaptive_F1=0.6707, delta_vs_U8=-0.05pp, sample_savings=50.2%

#### Cross-model consistency (exp_cross_model_consistency, SciERC)

pure_Qwen: degen=0.1, greedy=0.7478, uniform=0.7499 (+0.21pp), VC=0.7448 (-0.30pp)
pure_LLaMA: degen=0.234, greedy=0.7841, uniform=0.7873 (+0.33pp), VC=0.7869 (+0.28pp)
mixed_4q4l: degen=0.116, uniform=0.7916 (+4.37pp vs Qwen greedy, +0.42pp vs pure LLaMA uniform; p=0, CI=[0.27,0.58]), VC=0.7898 (+4.20pp vs Qwen greedy, +0.29pp vs pure LLaMA; p=0.0001)

#### DGEC VC construction (exp_dgec_vc_construction) — negative

28 total configs: 9 sig+, 10 sig−, 9 n.s.; by dataset: FewNERD (11 configs): 5+/5-/1ns mean=-0.12pp; WNUT17 (3 configs): 2+/0-/1ns mean=+0.92pp; SciERC (7 configs): 2+/0-/5ns mean=+0.62pp; CoNLL (7 configs): 0+/5-/2ns mean=-0.33pp
Qwen3-8B FT supplement (9 configs): 3+/3-/3ns; SciERC_s42=+1.40pp p=0.017; CoNLL_s456=-0.54pp p=0.998

#### DGEC SJ construction (exp_dgec_sj_construction) — negative

26 total configs: 1 sig+, 15 sig−, 10 n.s.; best: scierc/72b/zs +2.0pp p=0.001; worst: fewnerd/8b_qwen3/ft mean=-1.48pp all seeds p=1.0
Qwen3-8B FT supplement (9 configs): 0+/6-/3ns; FewNERD mean=-1.48pp; SciERC mean=-0.40pp; CoNLL mean=-0.50pp

#### Signal routing (exp_e1_signal_routing)

n=16 configs; RF LOO accuracy=0.562 (target 60%); router avg ΔF1=+0.39pp vs always-LP=+0.15pp (2.6× improvement); oracle_delta=+0.56pp; top features: oracle_headroom, degen_rate, base_f1; label dist: LP_selection=6, none=5, consensus_θ2n=3, consensus_LP_weighted=1, majority_vote=1

#### Pareto diversity-quality (exp_pareto_diversity_quality, SciERC)

T=0.7: 1-degen=0.777, uniform_delta=+1.81pp, VC_delta=+1.17pp
T=0.8: 1-degen=0.819, uniform=+1.25pp, VC=+1.68pp
mix_T07+T10: 1-degen=0.830, uniform=+1.43pp, VC=+1.67pp (dual Pareto optimal)
T=1.0: 1-degen=0.877, uniform=+0.75pp, VC=+1.21pp
mix_T08+T10: 1-degen=0.789, uniform=-0.17pp, VC=+0.47pp (dominated)
VC slope reduction ~50% flatter than uniform

#### XGBoost entity verifier (exp_b2_entity_verifier, PREPARING)

n_entities=122984, xgb_cv_auc=0.9273, lgb_cv_auc=0.9254, xgb_test_auc=0.8282, lgb_test_auc=0.8335; top features: VC=0.5296, agreement_count=0.2504; path_a_lgb_F1=0.7336 vs greedy=0.7321, path_a_beats_greedy=true

#### 72B few-shot (exp_qwen25_72b_fewshot) — negative

SciERC: LP ρ=0.06, SJ ρ=0.293, FK ρ=0.301, VC ρ=0.258, EM ρ=0.205, degen=16.6%, greedy=0.461, construction_delta=-0.08pp, p=0.544
CoNLL: LP ρ=0.106, SJ ρ=0.442, FK ρ=0.451, VC ρ=0.426, EM ρ=0.403, degen=70%, greedy=0.745, construction_delta=+0.03pp, p=0.417
FewNERD: LP ρ=0.161, SJ ρ=0.345, FK ρ=0.327, VC ρ=0.410, EM ρ=0.302, degen=45.2%, greedy=0.619, construction_delta=+0.02pp, p=0.401

---

### DEPRECATED / NOTES

- exp_015_metrics_expansion: voting_conf inflated (n_cond=501 wrong filter); RE cond values DEPRECATED; use exp_012_rerun_1024
- exp_009_capability_stratification: RE stratification values SUPERSEDED by gold-filtered rerun (exp_009_v2_re_rerun): RE Q1_sj_ρ=0.110, Q4_sj_ρ=0.473 (vs old Q1=0.447, Q4=0.540)
- exp_017_llama_conll_n16_r1024 rho_note: old values (rho_fk=0.8095, rho_sj=0.1815) inflated/deflated by 697 gold-empty instances; corrected values above
- Hidden state probes (hidden_state_probe_conll_full, _v2): both killed — not in D154 Dual Contribution framing
- DGS pilot, mbr_pilot: both killed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc50e01e-16b7-4153-9932-341f255097dc",
  "isSidechain": true,
  "agentId": "a97ebe3840b34757a",
  "requestId": "req_011CbDgew8iQGh4mnGX4muTn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07057563-72c6-41a7-8458-73f6390c1f2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "c7ddc740-cffe-49a2-afe7-879cf8dde3ec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-jingling-cupcake",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JaCHQc9zFEjnvF5bJgdpnD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21266,
      "cache_read_input_tokens": 76326,
      "output_tokens": 17437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21266
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17437,
          "cache_read_input_tokens": 76326,
          "cache_creation_input_tokens": 21266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21266,
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
