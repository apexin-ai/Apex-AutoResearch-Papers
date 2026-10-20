# Research conversation: I need to find and read the current paper LaTeX source for a project called "struct_self_consist_ie". The paper likely c

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a751620db879accde.jsonl`
- **Structured JSON:** [`b675d64ef60d742885cb.json`](../../sessions/b6/b675d64ef60d742885cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-19T13:51:44.788Z_

I need to find and read the current paper LaTeX source for a project called "struct_self_consist_ie". The paper likely contains:
1. A Table 1 with signal ranking data (AUROC values for EM, VC, SJ, FK, LP across datasets like SciERC, CoNLL, FewNERD)
2. Text discussing "structural signals > LP" or signal quality claims
3. Abstract and Conclusion sections with claims about signal quality

The paper source files are likely in one of these locations:
- /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/
- /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/
- Or find them with: find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name "*.tex" -type f

Find all .tex files, then read the relevant sections. I need:
1. The EXACT content of Table 1 (or whatever table shows AUROC per signal per dataset)
2. Any text in the paper body that discusses SciERC EM AUROC specifically or signal rankings
3. The Abstract text
4. The Conclusion text
5. Any text mentioning "structural signals" superiority over LP

Return the exact LaTeX source for these sections — don't summarize, quote verbatim. This is for a data consistency audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "ebb35b08-d032-47b0-bdac-25a808a526fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T13:51:44.791Z_

```json
{
  "parentUuid": "ebb35b08-d032-47b0-bdac-25a808a526fc",
  "isSidechain": true,
  "agentId": "a751620db879accde",
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
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
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
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "2ded79e0-7e6f-4704-bf24-b3b169b6d530",
  "timestamp": "2026-05-19T13:51:44.791Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-19T13:51:47.485Z_



I'll find and read the LaTeX source files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ded79e0-7e6f-4704-bf24-b3b169b6d530",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37DRJJWtta82VmURBi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "982dbf83-064d-4b3d-9293-6f78b2068724",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E18nBhZT2mbVqUp4mYmdu2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16248,
      "cache_read_input_tokens": 8262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16248,
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

_source line 4 · 2026-05-19T13:51:48.018Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012wqtReKLBLpfMo1DrHqWvn`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "982dbf83-064d-4b3d-9293-6f78b2068724",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37DRJJWtta82VmURBi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2854e946-4b3c-4735-9384-f33923425e58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E18nBhZT2mbVqUp4mYmdu2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16248,
      "cache_read_input_tokens": 8262,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16248
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 8262,
          "cache_creation_input_tokens": 16248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16248,
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

_source line 5 · 2026-05-19T13:51:48.059Z_

<details><summary>↩ Tool result · `toolu_012wqtReKLBLpfMo1DrHqWvn`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_ci_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/freeform_ablation_appendix_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_scaling_appendix_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/per_type_lp_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_021_fewnerd_full/paper/per_type_lp_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/scale_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2854e946-4b3c-4735-9384-f33923425e58",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "8188714c-894a-4512-82f3-d3b686a8859d",
  "sourceToolAssistantUUID": "2854e946-4b3c-4735-9384-f33923425e58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-19T13:51:51.874Z_

The main paper source is in `docs/paper/`. There are also artifact versions in `artifacts/_project/paper/`. Let me read the key files from both locations to find the most current versions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8188714c-894a-4512-82f3-d3b686a8859d",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37TUtd4PBjpKechQYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "220fe81a-dd5f-442f-aba8-1eac77e6aeb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns6rRsB1zGTrsSAccFFLwd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3057,
      "cache_read_input_tokens": 24510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3057,
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

_source line 7 · 2026-05-19T13:51:52.370Z_

<details open><summary>🔧 Tool call — Read · `toolu_016eHVuKkitfCNBX8P7Kq45f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "220fe81a-dd5f-442f-aba8-1eac77e6aeb1",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37TUtd4PBjpKechQYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f34ce8f4-6529-4cf1-a8db-d5dcb34c15aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns6rRsB1zGTrsSAccFFLwd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3057,
      "cache_read_input_tokens": 24510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3057,
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

_source line 8 · 2026-05-19T13:51:52.376Z_

<details><summary>↩ Tool result · `toolu_016eHVuKkitfCNBX8P7Kq45f`</summary>

```text
1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
6	We identify three qualitative factors: instance degeneracy, oracle headroom, and LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.
7	The diagnostic naturally motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f34ce8f4-6529-4cf1-a8db-d5dcb34c15aa",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "340d0210-01a3-495a-bb64-bb8105511150",
  "sourceToolAssistantUUID": "f34ce8f4-6529-4cf1-a8db-d5dcb34c15aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T13:51:52.857Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HZ2og9pPNjAxcuDwn86xSd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "340d0210-01a3-495a-bb64-bb8105511150",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37TUtd4PBjpKechQYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5685c59c-1585-49aa-b3f6-b5d791a030af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns6rRsB1zGTrsSAccFFLwd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3057,
      "cache_read_input_tokens": 24510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3057,
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

_source line 10 · 2026-05-19T13:51:52.862Z_

<details><summary>↩ Tool result · `toolu_01HZ2og9pPNjAxcuDwn86xSd`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage). Instance-level selection fails due to degeneracy and LP compression; entity-level construction yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC ($p{<}0.005$), complementary with LP selection and governed by LP-quality alignment. For practitioners: use QE for selective prediction; apply construction when multi-sample generation is feasible; assess LP-alignment to route between strategies. As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5685c59c-1585-49aa-b3f6-b5d791a030af",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "2fed660a-f47c-49f2-9eaa-481af8262ae1",
  "sourceToolAssistantUUID": "5685c59c-1585-49aa-b3f6-b5d791a030af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T13:51:53.305Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QkQbTJm87ucD27sP7FK7yT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fed660a-f47c-49f2-9eaa-481af8262ae1",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37TUtd4PBjpKechQYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46a6bdf1-1ee7-4e5e-90ce-66143a32982a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns6rRsB1zGTrsSAccFFLwd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3057,
      "cache_read_input_tokens": 24510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3057,
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

_source line 12 · 2026-05-19T13:51:53.310Z_

<details><summary>↩ Tool result · `toolu_01QkQbTJm87ucD27sP7FK7yT`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\toprule
29	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
30	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
31	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
32	\midrule
33	VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
34	SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
35	FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
36	EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
37	\midrule
38	LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
39	\bottomrule
40	\end{tabular}
41	\end{table*}
42	
43	Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models ($\varepsilon$-free; $\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\ref{app:epsilon_robustness}).
44	
45	\paragraph{Signal rankings are difficulty-dependent.}
46	On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
47	On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
48	At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
49	This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
50	
51	%% ============================================================
52	\subsection{The Correlation-Selection Gap}
53	\label{sec:selection_gap}
54	
55	Four of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\S\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.
56	The empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.
57	LP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\S\ref{sec:discussion}).
58	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Non-tied subset in \S\ref{sec:discussion}; RE in Appendix~\ref{app:re_extension}. $^\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}
64	\label{tab:selection}
65	\begin{tabular}{lcc}
66	\toprule
67	Method & NER F1 & $p$ \\
68	\midrule
69	Oracle & $0.775 \pm 0.001$ & --- \\
70	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
71	\midrule
72	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
73	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
74	\midrule
75	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
76	SJ           & $0.646 \pm 0.002$ & .67 \\
77	FK           & $0.646 \pm 0.001$ & .79 \\
78	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
79	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
80	\midrule
81	Random           & $0.610 \pm 0.003$ & --- \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=\columnwidth]{fig_selection_gap}
89	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\rho$ (seed 42); line with error bars: $\Delta$F1 vs.\ greedy (3-seed mean, seeds 42/123/456). Despite $\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}
90	\label{fig:selection_gap}
91	\end{figure}
92	
93	Instance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}).
94	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best.
95	
96	\paragraph{LP: the sole per-sample signal also fails.}
97	On SciERC ($n{=}529$, 2-seed sign tests\footnote{MDE${\approx}$1.5~pp at 80\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.
98	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
99	Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
100	
101	\paragraph{Qualitative factors governing selection effectiveness.}
102	Three factors qualitatively shape LP selection gains: (1)~\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\%, CoNLL 48.4\%; Table~\ref{tab:fewnerd}); (2)~\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\approx}2$\,pp vs.\ SciERC 13.1\,pp); (3)~\textit{LP-quality alignment}, measured as within-instance $\rho(\text{LP}, \text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\rho{\approx}0.5$--$0.7$ vs.\ SciERC $\rho{\approx}0.26$).
103	These factors are consistent with the observed pattern (Table~\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\pm}0.48$\,pp, 3-seed; Table~\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\% of instances yield F1${=}0$.
104	Yet QE remains effective on WNUT-17 (VC $\rho{=}0.730$; Table~\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.
105	This characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\S\ref{sec:fewnerd}, \S\ref{sec:discussion}).
106	
107	%% ============================================================
108	\subsection{Cross-Dataset Contrast: Few-NERD}
109	\label{sec:fewnerd}
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\ref{tab:multiseed}). $p$: paired bootstrap.}
115	\label{tab:fewnerd}
116	\resizebox{\columnwidth}{!}{%
117	\begin{tabular}{@{}lrccccr@{}}
118	\toprule
119	Dataset & $n$ & Greedy & Degen.\% & LP $\rho$ & LP $\Delta$ & $p$ \\
120	\midrule
121	WNUT-17 & 1{,}287 & .452 & 67.9\% & $-$.446 & $-$0.45\,pp & .72 \\
122	CoNLL & 2{,}756 & .908 & 48.4\% & .302 & $-$0.85\,pp & 1.0 \\
123	SciERC & 529 & .644 & 17.8\% & .205 & $+$0.61\,pp & .193 \\
124	Few-NERD & 32{,}565 & .748 & 13.8\% & .220 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
125	\bottomrule
126	\end{tabular}}
127	\end{table}
128	
129	Few-NERD (Table~\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\times$ more seed-stable ($\sigma{=}0.04$ vs.\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\ref{tab:cross_selection}).
130	Training convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\% and halves LP gains (Appendix~\ref{app:epoch_confound}).
131	
132	\paragraph{Degeneracy alone does not predict LP selection direction.}
133	Across 23 configurations, degeneracy does not predict LP gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}).
134	Cross-dataset prediction requires LP signal quality: Few-NERD ($\rho{\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\rho{\approx}0.26$) does not (Appendix~\ref{app:conditional_decomp}).
135	
136	\begin{figure}[t]
137	\centering
138	\includegraphics[width=\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}
139	\caption{Instance degeneracy vs.\ LP selection gain across 23 configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}
140	\label{fig:degeneracy_scatter}
141	\end{figure}
142	
143	Structural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\ref{app:n_scaling}.
144	
145	%% ============================================================
146	\subsection{Robustness}
147	\label{sec:robustness_main}
148	
149	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
150	
151	\begin{table}[t]
152	\centering
153	\small
154	\caption{Scale ablation: 8B vs.\ 4B QE $\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\ref{app:re_extension}.}
155	\label{tab:scale_ablation}
156	\begin{tabular}{@{}ll cc r@{}}
157	\toprule
158	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
159	\midrule
160	CoNLL & SJ & .436 & .422 & $-$.014 \\
161	      & FK & .400 & .418 & $+$.018 \\
162	SciERC & SJ & .360 & .422 & $+$.062 \\
163	       & FK & .267 & .326 & $+$.059 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	\paragraph{Scale robustness.}
169	With Qwen3-4B (Table~\ref{tab:scale_ablation}), QE is comparable (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\ref{app:llama3b}).
170	Degeneracy scales with capability: 8B shows 17.8\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
171	
172	\paragraph{LoRA-rank ablation.}
173	LoRA rank${=}8$ (vs.\ 32) lowers degeneracy to 7.2\% but LP remains below greedy ($\rho(\text{LP}, \text{F1}){\approx}0.24$); temperature manipulation ($T{=}1.2$; \S\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.
174	
175	\paragraph{Supervised signal combination and hidden probes.}
176	Supervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\ref{app:supervised_combination}).
177	Hidden state probes improve correlation ($+37$\% on SciERC) but not selection (gap closure $-5.1$\%; Appendix~\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.
178	
179	%% ============================================================
180	\subsection{Scaling Behavior}
181	\label{sec:scaling}
182	
183	We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.
184	
185	\begin{table}[t]
186	\centering
187	\small
188	\caption{Fine-tuned 8B vs.\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp).}
189	\label{tab:scale_comparison}
190	\begin{tabular}{@{}llcccccc@{}}
191	\toprule
192	Dataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\
193	\midrule
194	SciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\
195	       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\
196	\midrule
197	CoNLL  & 8B FT  & .908 & ${\approx}$2 & .424 & .436 & .400 & .302 \\
198	       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\
199	\bottomrule
200	\end{tabular}
201	\end{table}
202	
203	Zero-shot 72B produces lower greedy F1 but larger oracle headroom (Table~\ref{tab:scale_comparison}). LP $\rho$ drops from $0.205$ to $0.081$ on SciERC and from $0.302$ to near zero on CoNLL; LP selection fails in both datasets (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), confirming that the gap is a structural property of the task rather than a fine-tuning artifact.
204	Structural signals remain positive but reduced (VC $\rho{=}0.277$ on SciERC, SJ $\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\,pp, 41.4\% vs.\ 39.9\% greedy) but not on CoNLL ($-0.37$\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.
205	
206	\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}
207	
208	\begin{figure}[t]
209	\centering
210	% \includegraphics[width=\columnwidth]{figures/fig_scaling_curve.pdf}
211	\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\rho$. Separate lines for fine-tuned vs.\ zero-shot.}
212	\caption{\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}
213	\label{fig:scaling_curve}
214	\end{figure}
215	
216	%% ============================================================
217	\subsection{Prescriptive Results}
218	\label{sec:prescriptive}
219	
220	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
221	
222	\paragraph{Entity-level construction.}
223	Rather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\theta{=}2/N$ (${\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\theta$ stable within $[0.15, 0.35]$; Appendix~\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\,pp, CoNLL $-0.92$\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\,pp; \S\ref{sec:scaling}).
224	
225	\begin{table}[t]
226	\centering
227	\small
228	\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. Best in \textbf{bold}.}
229	\label{tab:entity_construction}
230	\resizebox{\columnwidth}{!}{%
231	\begin{tabular}{@{}llcccc@{}}
232	\toprule
233	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
234	\midrule
235	SciERC & LP & $.646{\pm}.002$ & $\mathbf{.656{\pm}.003}$ & $+1.02{\pm}0.49$\,pp & .004 \\
236	       & Unif. & $.646{\pm}.002$ & $.653{\pm}.006$ & $+0.74{\pm}0.71$\,pp & .023 \\
237	\addlinespace
238	Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001$ \\
239	         & Unif. & $.748$ & $.756{\pm}.006$ & $+0.74{\pm}0.58$\,pp & .003 \\
240	\addlinespace
241	CoNLL & Unif. & .908 & .904 & $-0.39$\,pp & n.s. \\
242	\bottomrule
243	\end{tabular}}
244	\end{table}
245	
246	LP-weighted construction improves over greedy on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$; Table~\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\approx}$8\% (SciERC) and 11\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\ref{app:n_scaling}).
247	
248	\paragraph{LP-alignment gating (preliminary diagnostic).}
249	Construction and LP selection are complementary: construction dominates on SciERC ($+1.02$\,pp vs.\ LP $+0.04{\pm}0.48$\,pp, n.s.; $\rho{\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\ $+1.39$\,pp; $\rho{\approx}0.5$--$0.7$).
250	We estimate within-instance $\rho(\text{LP}, \text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\rho_{\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\approx}0$ (n.s.).
251	The protocol performs three-way routing: (1)~$\rho_{\text{adj}} \geq \tau{=}0.3$: apply LP selection; (2)~$\rho_{\text{adj}} < \tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.
252	This routes Few-NERD to LP selection ($+1.39$\,pp); SciERC, CoNLL, and WNUT-17 fall below $\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\,pp) for protection against negative outcomes (CoNLL $-0.39$\,pp, WNUT-17 n.s.).
253	Routing is stable across $\tau{\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.
254	
255	\paragraph{Selective prediction.}
256	Orthogonal to construction, QE signals support selective prediction: at 80\% coverage, filtering low-confidence instances yields $+5$--$8$\,pp F1 (AUPRC 0.70--0.92; Table~\ref{tab:cross_selection}).
257	
258	\phantomsection\label{sec:selection_results}
259	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46a6bdf1-1ee7-4e5e-90ce-66143a32982a",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "2c16da0f-342b-4dc6-9ce9-ac25f300ca2d",
  "sourceToolAssistantUUID": "46a6bdf1-1ee7-4e5e-90ce-66143a32982a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T13:51:53.735Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UQo6Hk928a1Jgj79Bxaikz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c16da0f-342b-4dc6-9ce9-ac25f300ca2d",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37TUtd4PBjpKechQYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8bab7826-1946-4759-8f6e-7043ab2c0ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns6rRsB1zGTrsSAccFFLwd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3057,
      "cache_read_input_tokens": 24510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3057,
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

_source line 14 · 2026-05-19T13:51:53.742Z_

<details><summary>↩ Tool result · `toolu_01UQo6Hk928a1Jgj79Bxaikz`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low instance degeneracy and adequate alignment are present, with gains scaling with $N$.
14	On SciERC, the observed LP gain ($+0.2$~pp, $p{=}0.29$) falls below the minimum detectable effect (${\approx}$1.5~pp at 80\% power, $n{=}529$) despite 13~pp oracle headroom. We term this disparity between quality estimation strength and selection effectiveness the \textbf{correlation-selection gap}.
15	Three factors qualitatively shape this gap: (a)~\textit{instance degeneracy} (13\textendash 87\% across our benchmarks) compresses the candidate space; (b)~\textit{oracle headroom} bounds the achievable gain; (c)~\textit{LP-quality alignment} (within-instance $\rho(\text{LP}, \text{F1})$) determines whether LP can discriminate candidates in non-degenerate instances (\S\ref{sec:selection_gap}).
16	Our diagnosis is complementary to minimum Bayes risk (MBR) utility misalignment \cite{eikema2025structured}: where MBR failures in structured prediction stem from poorly chosen utility functions, we find that degeneracy eliminates candidate diversity before utility alignment matters.
17	Within non-degenerate instances, MBR utility correlates positively with F1 ($\rho{=}0.52$; \S\ref{sec:discussion}).
18	Both mechanisms intensify with model capability: degeneracy rises with scale and training convergence (\S\ref{sec:discussion}). This creates a tension between model quality and test-time improvability.
19	
20	\begin{figure*}[t]
21	\centering
22	\includegraphics[width=\textwidth]{fig_overview}
23	\caption{Overview of the correlation-selection gap and its mitigation. \textbf{Left}: consistency signals reliably estimate instance-level quality ($\rho$ up to 0.45 on CoNLL; Table~\ref{tab:quality_estimation}). \textbf{Center}: instance-level signals assign identical scores to all samples from the same input, so best-of-$N$ selection cannot outperform greedy. \textbf{Right}: entity-level construction aggregates entities across samples via majority vote ($\theta{=}2/N$), bypassing the selection bottleneck ($+1.40$\,pp on Few-NERD, multi-seed mean; \S\ref{sec:prescriptive}).}
24	\label{fig:overview}
25	\end{figure*}
26	
27	We evaluate five signals from three families (structural, surface, and model-internal) on SciERC \cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).
28	We vary candidate pool size ($N{\in}\{2,\ldots,32\}$), signal sophistication, and model capacity within the 4B\textendash 8B range; behavior at 70B+ scales remains an open question.
29	An exploratory extension to relation extraction is reported in Appendix~\ref{app:re_extension}.
30	Our contributions:
31	\begin{enumerate}
32	    \item \textbf{Quality estimation framework and selective prediction.}
33	    Five signals from three families evaluated on four NER benchmarks, two model families, and a 4B ablation, achieving reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82).
34	    QE enables selective prediction: filtering low-confidence instances at 80\% coverage yields $+5$--$8$\,pp F1 (area under the precision-recall curve [AUPRC] 0.70--0.92, VC strongest; \S\ref{sec:prescriptive}).
35	
36	    \item \textbf{Diagnostic of the correlation-selection gap.}
37	    For fine-tuned 4B--8B models, LP-quality alignment (within-instance $\rho(\text{LP}, \text{F1})$) is the primary predictor of selection success: LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) where alignment is strong, but not on benchmarks with weak alignment.
38	    Instance degeneracy causally modulates LP within fixed settings (epoch and temperature ablations), but does not predict cross-dataset direction ($\rho{=}0.052$, 23 configurations); structural signals fail by construction; supervised combinations and hidden state probes (Appendix~\ref{app:hidden_probe}) confirm the gap persists.
39	
40	    \item \textbf{Entity-level construction as a diagnostic-motivated mitigation.}
41	    The diagnostic naturally motivates entity-level aggregation, adapting entity voting from ensemble NER \cite{florian2003named} to stochastic sampling: LP-weighted construction yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$; \S\ref{sec:prescriptive}).
42	    Construction and LP selection are complementary on two informative datasets, governed by LP-quality alignment; a simple alignment-based gating protocol correctly routes datasets.
43	\end{enumerate}
44	
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bab7826-1946-4759-8f6e-7043ab2c0ead",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "f5b130a0-8290-48a5-94b7-fbede3b76435",
  "sourceToolAssistantUUID": "8bab7826-1946-4759-8f6e-7043ab2c0ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T13:51:54.390Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MxSujjj9prMqtfKkBpuSRF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5b130a0-8290-48a5-94b7-fbede3b76435",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37TUtd4PBjpKechQYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d9d861f-daa1-4552-a797-9e8ff3edce13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns6rRsB1zGTrsSAccFFLwd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3057,
      "cache_read_input_tokens": 24510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3057,
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

_source line 16 · 2026-05-19T13:51:54.396Z_

<details><summary>↩ Tool result · `toolu_01MxSujjj9prMqtfKkBpuSRF`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Diagnosing and Addressing Self-Consistency for Named Entity Recognition}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\section*{Responsible NLP Research Checklist}
47	\input{sections/checklist}
48	
49	\bibliography{references}
50	
51	\appendix
52	\input{sections/appendix}
53	
54	\end{document}
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d9d861f-daa1-4552-a797-9e8ff3edce13",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "f2d42c05-a1e2-4890-b054-1b4051a2f6c0",
  "sourceToolAssistantUUID": "4d9d861f-daa1-4552-a797-9e8ff3edce13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-19T13:51:58.066Z_

Now let me also check the artifacts/_project/paper/ versions to see if there's a more recent version, and read the discussion section for signal superiority claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2d42c05-a1e2-4890-b054-1b4051a2f6c0",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37vnCwW1p9KfLxxeS9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "242c7e28-5541-41e8-ae4e-71eb2d75480d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3FcjNs3g512wUY1ZqBQ2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11549,
      "cache_read_input_tokens": 27567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11549,
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

_source line 18 · 2026-05-19T13:52:00.307Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FnmfQRp9dXTTrPtY86WBZH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "242c7e28-5541-41e8-ae4e-71eb2d75480d",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37vnCwW1p9KfLxxeS9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3179f78d-b722-42a2-8053-4b8ba35b36a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3FcjNs3g512wUY1ZqBQ2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11549,
      "cache_read_input_tokens": 27567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11549,
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

_source line 19 · 2026-05-19T13:52:00.332Z_

<details><summary>↩ Tool result · `toolu_01FnmfQRp9dXTTrPtY86WBZH`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3179f78d-b722-42a2-8053-4b8ba35b36a1",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "329f0fc0-8c00-4e3b-ada9-ec513a6a68f5",
  "sourceToolAssistantUUID": "3179f78d-b722-42a2-8053-4b8ba35b36a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T13:52:00.693Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MQY5t34JEBAhrmWpQR33pj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "329f0fc0-8c00-4e3b-ada9-ec513a6a68f5",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37vnCwW1p9KfLxxeS9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c843e303-ee6d-45e7-8884-5ec37aff20b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3FcjNs3g512wUY1ZqBQ2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11549,
      "cache_read_input_tokens": 27567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11549,
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

_source line 21 · 2026-05-19T13:52:00.700Z_

<details><summary>↩ Tool result · `toolu_01MQY5t34JEBAhrmWpQR33pj`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.
12	This gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\S\ref{sec:complexity_robustness}).
13	
14	\paragraph{Models.}
15	Our primary model is \textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.
16	For cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.
17	
18	\paragraph{Sampling and Evaluation.}
19	For each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.
20	We use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.
21	Quality estimation is measured along two axes: \textit{rank correlation} with instance-level F1 via Spearman $\rho$ and Kendall $\tau$, and \textit{binary discrimination} via AUROC (instances above vs.\ below median F1).
22	Downstream utility is assessed through \textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.
23	Instance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.
24	The greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.
25	
26	\paragraph{Confidence Signals.}
27	We compare five signals from three families (detailed in \S\ref{sec:signals}).
28	\textit{Structural} signals operate on extracted entity/relation sets: \textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \textbf{Soft Jaccard (SJ)} measures pairwise set similarity \cite{jaccard1901distribution}.
29	\textit{Surface} signals operate on string representations: \textbf{Fleiss' $\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \cite{fleiss1971agreement}, and \textbf{Exact Match (EM)} computes the fraction of identical sample pairs.
30	The \textit{model-internal} signal is \textbf{log-probability (logprob)}, the mean token-level log-likelihood.
31	
32	\paragraph{Implementation.}
33	Inference uses vLLM with XGrammar constrained decoding \cite{willard2023guided} to enforce valid JSON output structure.
34	A span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.
35	All confidence signals are computed from the $N$ samples without access to gold labels.
36	
37	%% ============================================================
38	\subsection{Quality Estimation Results}
39	\label{sec:qe_results}
40	
41	\begin{table*}[t]
42	\centering
43	\small
44	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}
45	\label{tab:quality_estimation}
46	\begin{tabular}{ll cc cc cc cc}
47	\toprule
48	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
49	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
50	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
51	\midrule
52	Voting Conf. & Structural & \textbf{.502} & \textbf{.728} & \textbf{.422} & \textbf{.716} & .424 & .789 & .426 & .709 \\
53	Soft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \textbf{.431} & .704 \\
54	Fleiss' $\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\
55	Exact Match  & Surface    & .257 & .623 & .100 & .504 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
56	Log-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \textbf{.761} \\
57	\bottomrule
58	\end{tabular}
59	\end{table*}
60	
61	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
62	
63	\paragraph{Structural signals dominate on complex schemas.}
64	On SciERC NER, Voting Confidence achieves $\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\rho{=}0.357$), and all remaining signals ($\rho{\leq}0.265$).
65	Voting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.
66	The structural advantage persists on RE, where Voting ($\rho{=}0.422$) again leads.
67	However, all signals weaken on RE: 44\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.
68	Notably, FK ($\rho{=}0.253$) exceeds SJ ($\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.
69	
70	\paragraph{Signal rankings shift with task difficulty.}
71	On CoNLL NER, where greedy decoding achieves ${>}$91\% micro F1, the signal landscape changes substantially.
72	Exact Match leads with $\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\rho{=}0.436$) and Voting ($\rho{=}0.424$).
73	When most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.
74	This reversal---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.
75	
76	\paragraph{Cross-model stability.}
77	Comparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\rho{=}0.436$ (Qwen) vs.\ $\rho{=}0.431$ (LLaMA), a gap of only 0.005.
78	This model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.
79	The SJ--FK gap also narrows with schema simplification: $\Delta\rho{=}0.092$ on SciERC NER (6 entity types) vs.\ $\Delta\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.
80	
81	\paragraph{The logprob paradox.}
82	Log-probability reveals a dissociation between ranking and classification.
83	On CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\rho$ (0.307) among all signals.
84	This pattern indicates that logprob assigns well-separated scores to easy vs.\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.
85	We return to this distinction in \S\ref{sec:complexity_robustness} and visualize it in Figure~\ref{fig:signal_heatmap}.
86	
87	\begin{figure}[t]
88	\centering
89	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap_1024}
90	\caption{Signal quality heatmap across tasks and models. Color intensity encodes Spearman $\rho$; structural signals (VC, SJ) dominate on complex schemas (SciERC) while surface signals (EM) lead on simpler tasks (CoNLL).}
91	\label{fig:signal_heatmap}
92	\end{figure}
93	
94	\paragraph{Oracle headroom and practical ceilings.}
95	On CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.
96	When the model already operates near its performance ceiling, confidence signals serve as \textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.
97	We therefore focus selection analysis (\S\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.
98	
99	%% ============================================================
100	\subsection{The Correlation-Selection Gap}
101	\label{sec:selection_gap}
102	
103	\begin{table}[t]
104	\centering
105	\small
106	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM produces binary agreement without sample ranking. RE results are preliminary (single dataset, single model).}
107	\label{tab:selection}
108	\begin{tabular}{lcc}
109	\toprule
110	Method & NER F1 & RE F1 \\
111	\midrule
112	Oracle & 0.769 & 0.561 \\
113	\midrule
114	Log-prob           & 0.609 & \textbf{0.397} \\
115	Ensemble (SJ+Vot.) & 0.604 & 0.367 \\
116	Soft Jaccard       & 0.604 & 0.368 \\
117	Voting             & 0.596 & 0.338 \\
118	Exact Match        & ---   & ---   \\
119	\midrule
120	Greedy ($T{=}0$)   & \textbf{0.609} & 0.374 \\
121	Random             & 0.580 & 0.338 \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.
127	Table~\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).
128	
129	\paragraph{NER: no signal surpasses greedy.}
130	The oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).
131	Yet no confidence signal closes this gap.
132	Log-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\rho{=}0.502$), selects to only 0.596, \textit{below} greedy.
133	An ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.
134	The greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.
135	The Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.
136	
137	\paragraph{RE: logprob uniquely succeeds.}
138	For RE, log-probability is the only signal to exceed greedy (0.397 vs.\ 0.374, +2.3~pp).
139	Structural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.
140	The oracle gap of 18.7~pp (0.561 vs.\ 0.374) indicates substantially more per-instance variance than NER.
141	Log-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.
142	
143	\begin{figure}[t]
144	\centering
145	\includegraphics[width=\columnwidth]{figures/fig_selection_gap}
146	\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}
147	\label{fig:selection_gap}
148	\end{figure}
149	
150	\paragraph{Quality estimation $\neq$ output selection.}
151	We attribute this gap (Figure~\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best for a given input.
152	When per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.
153	
154	\paragraph{Implications for test-time scaling.}
155	This correlation-selection gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}.
156	Scaling inference compute through repeated sampling assumes a selector can identify the best sample.
157	Our results show that for structured prediction, existing confidence signals serve as quality \textit{estimators}---useful for flagging unreliable predictions---but not as effective \textit{selectors}.
158	Closing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \cite{cobbe2021verifiers} or pairwise comparison models.
159	
160	%% ============================================================
161	\subsection{Task Complexity and Signal Robustness}
162	\label{sec:complexity_robustness}
163	
164	\paragraph{Task difficulty as a boundary condition.}
165	Signal effectiveness varies systematically with task difficulty.
166	On CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\rho{=}0.451$); on SciERC NER (micro F1$\,{\approx}\,$0.66), SJ overtakes EM ($\rho{=}0.357$ vs.\ 0.257); on SciERC RE, where 44\% of instances score zero F1, all signals converge to $\rho{\approx}0.25$.
167	The NER--RE difference is statistically confirmed: Fisher's $z$-test comparing SJ $\rho$ between NER ($\rho{=}0.357$) and RE ($\rho{=}0.211$) yields $z{=}2.31$, $p{=}0.021$, confirming statistically significant task-dependent degradation.
168	
169	\paragraph{Per-relation diagnostic.}
170	RE signal degradation is relation-specific.
171	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
172	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
173	
174	\paragraph{Capability stratification.}
175	SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
176	Similarly, RE instances with ${\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\rho{=}0.630$, SJ $\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.
177	The SJ advantage over logprob remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.
178	
179	\paragraph{Method boundary: WNUT-17.}
180	WNUT-17 establishes where the approach breaks down.
181	SJ achieves $\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\% of instances at zero F1.
182	Log-probability shows a strong \textit{negative} correlation ($\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.
183	This is a boundary of the method, not a limitation of the datasets.
184	
185	\begin{table}[t]
186	\centering
187	\small
188	\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\rho$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}
189	\label{tab:robustness}
190	\begin{tabular}{llcc}
191	\toprule
192	& & NER $\rho$ & RE $\rho$ \\
193	\midrule
194	\multicolumn{4}{l}{\textit{Temperature} ($N{=}8$)} \\
195	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
196	\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\
197	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
198	\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\
199	\midrule
200	\multicolumn{4}{l}{\textit{Sample size} ($T{=}1.0$)} \\
201	\quad SJ & $N{=}8$  & 0.357 & 0.211 \\
202	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
203	\quad FK & $N{=}8$  & 0.265 & 0.253 \\
204	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	\paragraph{Robustness analysis.}
210	Table~\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.
211	\textit{Temperature.}
212	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.
213	FK shows mixed behavior: NER $\rho$ drops by 0.056, while RE $\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
214	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.357 vs.\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
215	
216	\textit{Sample size.}
217	Increasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\rho$ improves from 0.357 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).
218	FK benefits less ($\rho{\approx}0.280$ at $N{=}16$ vs.\ 0.265 at $N{=}8$).
219	For RE at $N{=}16$, SJ ($\rho{=}0.281$), FK ($\rho{=}0.279$), and logprob ($\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.
220	
221	\paragraph{Scale ablation: 4B vs.\ 8B.}
222	To isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.
223	
224	\begin{table}[t]
225	\centering
226	\small
227	\caption{Scale ablation: 4B vs.\ 8B on quality estimation ($\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\ref{tab:quality_estimation}--\ref{tab:selection}.}
228	\label{tab:scale-ablation}
229	\begin{tabular}{lcccccc}
230	\toprule
231	& \multicolumn{2}{c}{\textbf{CoNLL NER}} & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} \\
232	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
233	& 8B & 4B & 8B & 4B & 8B & 4B \\
234	\midrule
235	SJ $\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\
236	FK $\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\
237	\midrule
238	Greedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\
239	Oracle F1 & ---  & .938 & .769 & .793 & --- & --- \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	Table~\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\rho{=}0.357$ (8B) to $\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\rho{=}0.265$ to $\rho{=}0.326$.
245	Yet the selection gap persists: on SciERC NER, all 4B signals perform \textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.
246	On CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\leq$0.1~pp of greedy---marginal by any standard.
247	The gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.
248	
249	\paragraph{Free-form decoding ablation.}
250	One concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.
251	We test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.
252	The fine-tuned model achieves a 99.95\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.
253	Crucially, LP standard deviation is virtually unchanged (0.0206 $\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\% $\to$ 57.7\%).
254	NER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\ref{tab:freeform-ablation} in the Appendix).
255	Score compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.
256	This reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.
257	
258	\paragraph{Cross-model transfer.}
259	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, 3-seed mean).
260	On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
261	On conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
262	
263	\paragraph{Evaluation circularity.}
264	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
265	Evaluation circularity is negligible.
266	
267	\paragraph{Conditional filtering reveals signal divergence.}
268	We define instances as \textit{tied} when the within-sample log-probability range falls below $\varepsilon{=}0.05$ nats; results are robust to $\varepsilon \in \{0.01, 0.05, 0.10\}$ (tied fractions of 45\%, 60\%, 72\% on NER, with consistent patterns across all thresholds).
269	Filtering to non-zero F1 instances improves SJ correlations: NER $\rho{=}0.412$ (from 0.357), RE $\rho{=}0.368$ at $N{=}8$.
270	At $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\rho{=}0.308$, while logprob drops to $\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.
271	For applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\rho{\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.
272	
273	\paragraph{Binary filtering vs.\ continuous ranking.}
274	The logprob paradox observed in Table~\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.
275	Log-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).
276	Figure~\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.
277	Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.
278	
279	\begin{figure}[t]
280	\centering
281	\includegraphics[width=\columnwidth]{figures/fig_reliability_1024}
282	\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}
283	\label{fig:reliability}
284	\end{figure}
285	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c843e303-ee6d-45e7-8884-5ec37aff20b8",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "b9c997f2-dd9e-4ac0-8550-c16d4ecace55",
  "sourceToolAssistantUUID": "c843e303-ee6d-45e7-8884-5ec37aff20b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T13:52:00.961Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KPfUf8MHaTzGhUWRLixpFY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9c997f2-dd9e-4ac0-8550-c16d4ecace55",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37vnCwW1p9KfLxxeS9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0183a10a-9abe-4cb3-8108-fa09ad204813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3FcjNs3g512wUY1ZqBQ2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11549,
      "cache_read_input_tokens": 27567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11549,
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

_source line 23 · 2026-05-19T13:52:00.966Z_

<details><summary>↩ Tool result · `toolu_01KPfUf8MHaTzGhUWRLixpFY`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Ablations confirm the gap's robustness: it persists at 4B scale and under free-form decoding without grammar constraints (\S\ref{sec:experiments}).
13	
14	Several directions remain open.
15	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
16	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
17	Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.
18	Finally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0183a10a-9abe-4cb3-8108-fa09ad204813",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "630bd7e4-c917-4b53-a7c7-d1b59ed4d016",
  "sourceToolAssistantUUID": "0183a10a-9abe-4cb3-8108-fa09ad204813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T13:52:01.528Z_

<details open><summary>🔧 Tool call — Read · `toolu_018M4NMEs6nsEKcLokAv1VXB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "630bd7e4-c917-4b53-a7c7-d1b59ed4d016",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC37vnCwW1p9KfLxxeS9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4882e4a3-2c02-4cca-bd59-e0206faaa0b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3FcjNs3g512wUY1ZqBQ2v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11549,
      "cache_read_input_tokens": 27567,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11549
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 348,
          "cache_read_input_tokens": 27567,
          "cache_creation_input_tokens": 11549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11549,
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

_source line 25 · 2026-05-19T13:52:01.533Z_

<details><summary>↩ Tool result · `toolu_018M4NMEs6nsEKcLokAv1VXB`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Three factors qualitatively constrain selection: instance degeneracy (17.8--67.9\%) compresses the candidate space, limited oracle headroom bounds achievable gains, and LP compression (within-instance $\rho$ 0.043--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\ref{tab:nontied_main}), but $\varepsilon{=}0.05$ is post-hoc ($p_{\text{adj}}{=}0.14$ after joint correction; Appendix~\ref{app:epsilon_robustness}), so this is exploratory evidence.
6	Temperature disentangles degeneracy from alignment: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve (median $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}); the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms (Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}); our negative results are specific to fine-tuned models with constrained decoding (Appendix~\ref{app:when_selection_works}).
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4882e4a3-2c02-4cca-bd59-e0206faaa0b3",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "5f8ad937-baf1-4f5a-9311-f1b29d0f810d",
  "sourceToolAssistantUUID": "4882e4a3-2c02-4cca-bd59-e0206faaa0b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T13:52:05.162Z_

Now let me also check the discussion section from docs/paper (the main paper location) and search for any "structural signals > LP" or "structural signals superiority" claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f8ad937-baf1-4f5a-9311-f1b29d0f810d",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC38T8aZrgdGo3hV9vjT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2197053-5910-41d6-a5aa-d163051ce369",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcFAiZQH1XA4NvExb68Wgv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10044,
      "cache_read_input_tokens": 39116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10044,
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

_source line 27 · 2026-05-19T13:52:07.991Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Y2QaxxWVfo2B5e1zcDh29c`</summary>

```json
{
  "pattern": "structural signal|structural.*domin|structural.*lead|structural.*outperform|structural.*LP|structural.*log.prob",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2197053-5910-41d6-a5aa-d163051ce369",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC38T8aZrgdGo3hV9vjT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42ae5a06-e820-4e26-8315-e11f02f10a37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcFAiZQH1XA4NvExb68Wgv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10044,
      "cache_read_input_tokens": 39116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10044,
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

_source line 28 · 2026-05-19T13:52:08.017Z_

<details><summary>↩ Tool result · `toolu_01Y2QaxxWVfo2B5e1zcDh29c`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:46:On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:99:Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:129:Few-NERD (Table~\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\times$ more seed-stable ($\sigma{=}0.04$ vs.\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\ref{tab:cross_selection}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:143:Structural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\ref{app:n_scaling}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:204:Structural signals remain positive but reduced (VC $\rho{=}0.277$ on SciERC, SJ $\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\,pp, 41.4\% vs.\ 39.9\% greedy) but not on CoNLL ($-0.37$\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex:12:Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex:33:Unlike structural signals, FK relies on exact string matching.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:92:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:137:\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:154:Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:231:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:256:For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:257:Structural signals use $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, each additional comparison yields diminishing information.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:258:This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:272:The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant; these two structural signals perform comparably.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:423:(b)~Closed-source APIs where log-probabilities are unavailable make consistency signals the only viable selection mechanism; our structural signals (SJ, VC, FK, EM) provide quality estimation ($\rho$ up to 0.45) even without model-internal access.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1035:Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER); additional samples stabilize structural signals more than LP.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1113:This divergence confirms that LP compression is model-intrinsic: higher temperature increases between-instance LP variance (benefiting structural signals) but does not resolve within-instance compression, degrading LP's discriminative power.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1166:When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1167:The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1240:The $\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\ref{tab:quality_estimation}); ranking stability holds across two model families spanning 3B--8B.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1271:(1)~All five signals achieve positive QE ($\rho$ 0.22--0.39); quality estimation works on Few-NERD. VC leads ($\rho{=}0.39$), followed by FK ($0.31$), SJ ($0.30$), EM ($0.29$), LP ($0.22$); the ranking matches SciERC where structural signals also outperform LP for quality estimation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1273:(3)~Despite positive $\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:38:    Instance degeneracy causally modulates LP within fixed settings (epoch and temperature ablations), but does not predict cross-dataset direction ($\rho{=}0.052$, 23 configurations); structural signals fail by construction; supervised combinations and hidden state probes (Appendix~\ref{app:hidden_probe}) confirm the gap persists.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1702:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1703:\newlabel{fig:signal_heatmap}{{7}{18}{Quality estimation heatmap (Spearman $\rho $) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho {=}0.360$) and RE ($\rho {=}0.417$), while LP RE collapses to near-zero ($\rho {=}0.011$)}{figure.caption.54}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42ae5a06-e820-4e26-8315-e11f02f10a37",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "e9e211fc-2cea-4839-b384-f44278d686e0",
  "sourceToolAssistantUUID": "42ae5a06-e820-4e26-8315-e11f02f10a37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T13:52:08.872Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Mv1ViFoDJewEjMx8qpFMUx`</summary>

```json
{
  "pattern": "structural signal|structural.*domin|structural.*lead|structural.*outperform|structural.*LP|structural.*log.prob",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9e211fc-2cea-4839-b384-f44278d686e0",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC38T8aZrgdGo3hV9vjT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74e74a89-bb8c-4148-8780-2d22ecfe9715",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcFAiZQH1XA4NvExb68Wgv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10044,
      "cache_read_input_tokens": 39116,
      "output_tokens": 351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10044
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 351,
          "cache_read_input_tokens": 39116,
          "cache_creation_input_tokens": 10044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10044,
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

_source line 30 · 2026-05-19T13:52:08.895Z_

<details><summary>↩ Tool result · `toolu_01Mv1ViFoDJewEjMx8qpFMUx`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex:35:Our work extends their analysis to multi-domain benchmarks, temperature-based sampling, and a systematic five-signal comparison that reveals when structural signals outperform surface alternatives and vice versa.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex:52:These approaches measure uncertainty over the model's belief distribution; our structural signals instead measure agreement over output \textit{structure}, comparing extracted entity sets rather than semantic content of free-form text.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex:63:\paragraph{Structural signals dominate on complex schemas.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex:66:The structural advantage persists on RE, where Voting ($\rho{=}0.422$) again leads.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex:68:Notably, FK ($\rho{=}0.253$) exceeds SJ ($\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex:78:This model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex:90:\caption{Signal quality heatmap across tasks and models. Color intensity encodes Spearman $\rho$; structural signals (VC, SJ) dominate on complex schemas (SciERC) while surface signals (EM) lead on simpler tasks (CoNLL).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex:139:Structural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex:176:Similarly, RE instances with ${\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\rho{=}0.630$, SJ $\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex:275:Log-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex:282:\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex:8:First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex:23:Structural signals are most effective within the model's capability range.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex:31:Logprob provides coarse separation between reliable and unreliable instances, while structural signals provide finer-grained ranking across the quality spectrum.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/method.tex:31:\subsubsection{Structural Signals}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/method.tex:33:Structural signals operate directly on the extracted entity or relation sets, exploiting set-theoretic overlap.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex:3:We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families (Qwen3-8B, LLaMA-3.1-8B).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex:4:We find that entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex:6:Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex:38:We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex:44:    Entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$; structural signals outperform surface and model-internal alternatives on complex schemas (SciERC), while surface signals dominate on simpler tasks (CoNLL).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74e74a89-bb8c-4148-8780-2d22ecfe9715",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "f2951415-0abe-4af6-9257-95cf85510232",
  "sourceToolAssistantUUID": "74e74a89-bb8c-4148-8780-2d22ecfe9715",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T13:52:13.321Z_

I now have all the relevant content. Let me also read the discussion section from `docs/paper/` since it's the primary paper location.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2951415-0abe-4af6-9257-95cf85510232",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC38zeQauN9vZx7AFm62",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4705b802-5f50-43c5-9061-2d85e038b37d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013stQxV3nmvT99HijHezgQj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5474,
      "cache_read_input_tokens": 49160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5474,
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

_source line 32 · 2026-05-19T13:52:13.844Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GVtd9DXokALvkANGunKtMo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4705b802-5f50-43c5-9061-2d85e038b37d",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC38zeQauN9vZx7AFm62",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c62b4e17-6ec0-4fc0-a3e3-898de7261975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013stQxV3nmvT99HijHezgQj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5474,
      "cache_read_input_tokens": 49160,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5474
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 49160,
          "cache_creation_input_tokens": 5474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5474,
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

_source line 33 · 2026-05-19T13:52:13.859Z_

<details><summary>↩ Tool result · `toolu_01GVtd9DXokALvkANGunKtMo`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Three factors qualitatively constrain selection: instance degeneracy (17.8--67.9\%) compresses the candidate space, limited oracle headroom bounds achievable gains, and LP compression (within-instance $\rho$ 0.043--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\ref{tab:nontied_main}), but $\varepsilon{=}0.05$ is post-hoc ($p_{\text{adj}}{=}0.14$ after joint correction; Appendix~\ref{app:epsilon_robustness}), so this is exploratory evidence.
6	Temperature disentangles degeneracy from alignment: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve (median $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}); the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms (Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}); our negative results are specific to fine-tuned models with constrained decoding (Appendix~\ref{app:when_selection_works}).
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c62b4e17-6ec0-4fc0-a3e3-898de7261975",
  "isSidechain": true,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "agentId": "a751620db879accde",
  "type": "user",
  "uuid": "e6886eaf-ad40-443b-a16d-1bca0aa6d122",
  "sourceToolAssistantUUID": "c62b4e17-6ec0-4fc0-a3e3-898de7261975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-19T13:53:32.709Z_

Here is the complete verbatim LaTeX source for all requested sections. There are **two versions** of the paper: the current main version at `docs/paper/` and an older artifact version at `artifacts/_project/paper/`. The two differ significantly in Table 1 numbers and narrative framing. I'll present both.

---

## 1. Table 1 (Quality Estimation — AUROC per signal per dataset)

### Current version (`docs/paper/sections/experiments.tex`, lines 22-41):

```latex
\begin{table*}[t]
\centering
\small
\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
\label{tab:quality_estimation}
\begin{tabular}{ll cc cc cc}
\toprule
& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
\midrule
VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
\midrule
LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
\bottomrule
\end{tabular}
\end{table*}
```

### Older artifact version (`artifacts/_project/paper/experiments.tex`, lines 41-59):

```latex
\begin{table*}[t]
\centering
\small
\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}
\label{tab:quality_estimation}
\begin{tabular}{ll cc cc cc cc}
\toprule
& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
\midrule
Voting Conf. & Structural & \textbf{.502} & \textbf{.728} & \textbf{.422} & \textbf{.716} & .424 & .789 & .426 & .709 \\
Soft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \textbf{.431} & .704 \\
Fleiss' $\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\
Exact Match  & Surface    & .257 & .623 & .100 & .504 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
Log-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \textbf{.761} \\
\bottomrule
\end{tabular}
\end{table*}
```

**Key difference in SciERC NER numbers between the two versions:**

| Signal | Old version (artifacts) rho/AUC | New version (docs) rho/AUC |
|--------|------|------|
| VC | .502 / .728 | .379 / .663 |
| SJ | .357 / .666 | .360 / .650 |
| FK | .265 / .624 | .267 / .602 |
| EM | .257 / .623 | .295 / .614 |
| LP | .140 / .559 | .205 / .578 |

The old version also includes SciERC RE columns; the new version drops RE from the main table (moved to appendix).

---

## 2. Text discussing SciERC EM AUROC and signal rankings

From `docs/paper/sections/experiments.tex`, lines 45-49:

```latex
\paragraph{Signal rankings are difficulty-dependent.}
On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
```

---

## 3. Abstract

### Current version (`docs/paper/sections/abstract.tex`):

```latex
\begin{abstract}
Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
All signals achieve reliable QE ($\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
We identify three qualitative factors: instance degeneracy, oracle headroom, and LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.
The diagnostic naturally motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.
\end{abstract}
```

### Older artifact version (`artifacts/_project/paper/abstract.tex`):

```latex
\begin{abstract}
Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families (Qwen3-8B, LLaMA-3.1-8B).
We find that entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).
We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
\end{abstract}
```

---

## 4. Conclusion

### Current version (`docs/paper/sections/conclusion.tex`):

```latex
\section{Conclusion}\label{sec:conclusion}

Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage). Instance-level selection fails due to degeneracy and LP compression; entity-level construction yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC ($p{<}0.005$), complementary with LP selection and governed by LP-quality alignment. For practitioners: use QE for selective prediction; apply construction when multi-sample generation is feasible; assess LP-alignment to route between strategies. As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
```

### Older artifact version (`artifacts/_project/paper/conclusion.tex`):

```latex
\section{Conclusion}\label{sec:conclusion}

This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.

Three findings anchor our analysis.
First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.
Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.

Ablations confirm the gap's robustness: it persists at 4B scale and under free-form decoding without grammar constraints (\S\ref{sec:experiments}).

Several directions remain open.
Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.
Finally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.
```

---

## 5. Text discussing "structural signals superiority over LP"

Key passages from `docs/paper/sections/experiments.tex`:

**Line 46:**
```latex
On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
```

**Lines 129:**
```latex
Few-NERD (Table~\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp).
```

**Line 143:**
```latex
Structural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\ref{app:n_scaling}.
```

**Line 204:**
```latex
Structural signals remain positive but reduced (VC $\rho{=}0.277$ on SciERC, SJ $\rho{=}0.304$ on CoNLL).
```

From `docs/paper/sections/appendix.tex`, **line 258:**
```latex
This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
```

From `docs/paper/sections/appendix.tex`, **line 1271:**
```latex
(1)~All five signals achieve positive QE ($\rho$ 0.22--0.39); quality estimation works on Few-NERD. VC leads ($\rho{=}0.39$), followed by FK ($0.31$), SJ ($0.30$), EM ($0.29$), LP ($0.22$); the ranking matches SciERC where structural signals also outperform LP for quality estimation.
```

---

**Summary of the two-version situation:**

The **current main paper** (`docs/paper/`) reports SciERC VC rho=.379, AUROC=.663, adds Few-NERD as a fourth dataset, drops RE from the main table, and reframes the narrative around "correlation-selection gap" + "entity-level construction" as mitigation.

The **older artifact version** (`artifacts/_project/paper/`) reports SciERC VC rho=.502, AUROC=.728, includes RE columns in Table 1, and has a different abstract/conclusion that claims "structural signals dominating on complex schemas while surface signals lead on simpler tasks" more strongly. The older version's conclusion still quotes rho=0.50 / AUROC=0.73 which are the old numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6886eaf-ad40-443b-a16d-1bca0aa6d122",
  "isSidechain": true,
  "agentId": "a751620db879accde",
  "requestId": "req_011CbC39MkfHngrCnQ3FjjQ9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf31d1f3-d6cb-4532-ac4f-a231b7822b14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoS2nMEcBrGbWPdJ5fL1RM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 54634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 690,
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
