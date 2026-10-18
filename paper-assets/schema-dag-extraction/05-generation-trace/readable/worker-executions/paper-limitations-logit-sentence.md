# paper limitations logit sentence

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_paper_limitations_logit_sentence_20260522T073429.log`
- **Structured JSON:** [`a2bcbfb4b792ce5a8465.json`](../../sessions/a2/a2bcbfb4b792ce5a8465.json)

## Before a recorded user message

42 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
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
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "f5521b5a-f5db-4aec-99a0-c564f2423c37",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "status": "allowed",
    "resetsAt": 1779450600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "249eaff9-0674-4d3d-8a15-80b47f1a5d41",
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0"
}
```

---

### Assistant

_source line 4_

Let me read the Limitations section first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "e00ca79d-5dbc-4942-a6bd-278114e96ae6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmjEfLDc5udJiJUcKj4Ghh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11908,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11908
      },
      "output_tokens": 2,
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

_source line 5_

<details open><summary>🔧 Tool call — Grep · `toolu_01U5ceZCQmW5zB1RVPu8nHub`</summary>

```json
{
  "pattern": "\\\\section\\*?\\{Limitations\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/main.tex",
  "output_mode": "content",
  "-A": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "f891e34d-5471-486c-b4ce-74f7e134b7ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmjEfLDc5udJiJUcKj4Ghh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11908,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11908
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-22T07:34:45.589Z_

<details><summary>↩ Tool result · reported error · `toolu_01U5ceZCQmW5zB1RVPu8nHub`</summary>

```text
&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/main.tex. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "ffdc7ded-9a52-46dd-9aee-a108bdc2c459",
  "tool_use_result": "Error: Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/main.tex. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01GibfNLiuJzDJDXUP55DMp9`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "fe7251d2-f1d1-4156-a25e-ca78145cc2c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDfEguNc326woD5pFcEeN6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 23749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 262
      },
      "output_tokens": 62,
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

_source line 8 · 2026-05-22T07:34:47.596Z_

<details><summary>↩ Tool result · reported error · `toolu_01GibfNLiuJzDJDXUP55DMp9`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "c264e835-a405-414a-bf9d-dc26d10f9f25",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction."
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_0176qDPiyERN6W4m9jxFmQNd`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "c466d3a5-2b5b-4f3f-ae58-c21e975d2acc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2cc4kcGbWuLsLnP2Ro8br",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 200,
      "cache_read_input_tokens": 24011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 200
      },
      "output_tokens": 58,
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

_source line 10 · 2026-05-22T07:34:49.890Z_

<details><summary>↩ Tool result · `toolu_0176qDPiyERN6W4m9jxFmQNd`</summary>

```text
AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
artifacts
checkpoints
configs
constraints.lock
constraints.yaml
data
decisions.lock
decisions.yaml
distill_tmp
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
review_visual_check_state.json
run_fewrel_v2_bcs.py
run_fewshot_bcs_v2.py
scripts
src
study_status.lock
task_context
writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "5814ca29-8579-4cdc-99db-c39089e47f1c",
  "tool_use_result": {
    "stdout": "AGENTS.md\nROADMAP.lock\nROADMAP.md\n_last_visual_review.json\nartifacts\ncheckpoints\nconfigs\nconstraints.lock\nconstraints.yaml\ndata\ndecisions.lock\ndecisions.yaml\ndistill_tmp\ndocs\ndream_registry.lock\ndream_registry.yaml\ndream_registry.yaml.bak\nexperiment_plan.lock\nexperiment_plan.yaml\nfigures\nliterature_map.yaml\nlogs\nmemory.md\nmistakes.lock\nmistakes.yaml\npaper_framing.md\npaper_provenance.lock\npaper_provenance.yaml\nregistry.lock\nregistry.yaml\nreport.md\nreview_visual_check_state.json\nrun_fewrel_v2_bcs.py\nrun_fewshot_bcs_v2.py\nscripts\nsrc\nstudy_status.lock\ntask_context\nwriting_plan.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_0115C7AD9ZHAF2ntgy1wuCNB`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "1430d7b1-3d3c-461b-9828-28e0d4874b42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZHQJbssfGP2h4XXmZ1DPK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 24211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 295
      },
      "output_tokens": 64,
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

_source line 12 · 2026-05-22T07:34:52.199Z_

<details><summary>↩ Tool result · `toolu_0115C7AD9ZHAF2ntgy1wuCNB`</summary>

```text
artifacts/dream_reports/dream_20260515T053106/best/paper.tex
artifacts/dream_reports/dream_20260515T053106/median/paper.tex
artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
artifacts/dream_reports/dream_20260515T113743/best/paper.tex
artifacts/dream_reports/dream_20260515T113743/median/paper.tex
artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
artifacts/dream_reports/dream_20260515T140829/best/paper.tex
artifacts/dream_reports/dream_20260515T140829/median/paper.tex
artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
artifacts/_project/paper/dataset_stats.tex
artifacts/paper/tables/dataset_stats.tex
artifacts/_project/paper/sdgd_negative.tex
artifacts/_project/paper/experimental_setup.tex
docs/paper/conclusion.tex
artifacts/_project/paper/results.tex
artifacts/dream_reports/dream_20260516T073533/best/paper.tex
artifacts/dream_reports/dream_20260516T073533/median/paper.tex
artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
docs/paper/supplementary.tex
artifacts/acknowledgements_draft.tex
docs/paper/prompt_appendix.tex
docs/paper/checklist.tex
artifacts/error_taxonomy_cross_model_table.tex
artifacts/permutation_equivalence_latex.tex
artifacts/_project/paper/docred_ridge_appendix.tex
artifacts/docred_ridge_appendix.tex
docs/paper/discussion.tex
docs/paper/sdgd_negative.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "cd7d37b6-4829-4fd6-b6f5-ea3b3ba06956",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T053106/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/worst/paper.tex",
      "artifacts/_project/paper/dataset_stats.tex",
      "artifacts/paper/tables/dataset_stats.tex",
      "artifacts/_project/paper/sdgd_negative.tex",
      "artifacts/_project/paper/experimental_setup.tex",
      "docs/paper/conclusion.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T073533/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T073533/worst/paper.tex",
      "docs/paper/supplementary.tex",
      "artifacts/acknowledgements_draft.tex",
      "docs/paper/prompt_appendix.tex",
      "docs/paper/checklist.tex",
      "artifacts/error_taxonomy_cross_model_table.tex",
      "artifacts/permutation_equivalence_latex.tex",
      "artifacts/_project/paper/docred_ridge_appendix.tex",
      "artifacts/docred_ridge_appendix.tex",
      "docs/paper/discussion.tex",
      "docs/paper/sdgd_negative.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/results.tex",
      "docs/paper/main.tex"
    ],
    "durationMs": 93,
    "numFiles": 34,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Grep · `toolu_013jqsmyhGU975Kyusa8VW56`</summary>

```json
{
  "pattern": "\\\\section\\*?\\{Limitations\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content",
  "-A": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "18729ea7-e26b-43c4-8c66-44ec81f72f86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqHwMR6Y6FNErm8xMX6GiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
      },
      "output_tokens": 34,
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

_source line 14 · 2026-05-22T07:34:56.382Z_

<details><summary>↩ Tool result · `toolu_013jqsmyhGU975Kyusa8VW56`</summary>

```text
38:\section*{Limitations}
39-
40-Our findings are subject to three main limitations.
41-\textbf{(1)~Model and statistical scope.}
42-Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\S\ref{sec:multi_channel}) or SDGD failure analysis (\S\ref{sec:sdgd}), and proprietary-model generalization remains open.
43-TOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive; the interaction point estimate (0.47\,pp) falls within the $\pm 3$\,pp equivalence margin.
44-BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\,=\,0.88$\,pp is 18--44\% of the observed effect size (Appendix~\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.
45-All evidence is correlational with controlled stratification; mechanistic confirmation at the attention or logit level remains future work.
46-%
47-\textbf{(2)~DocRED VIF confounding.}
48-DocRED exhibits severe multicollinearity (VIF${}\,=\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\,=\,5.6\%$ serves only as directional evidence, and the count${}\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}).
49-%
50-\textbf{(3)~Experimental scope.}
51-Evaluations cover four English-language Wikipedia/Wikidata-derived datasets in a training-free zero-shot setting; few-shot, fine-tuned, domain-specific (e.g., biomedical, legal), and non-English scenarios remain untested.
52-BCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\ref{app:relaxed-matching}).
53-Batches share prompt template and LLM but type composition is independently sampled; cross-dataset consistency is treated as converging evidence rather than independent replication \citep{rothman-1990}, and core claims are robust to Bonferroni correction (all $p < 0.001$) \citep{dror-2018-significance}.
54-
55-% \input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF
56-
57-\bibliography{references}
58-
59-\appendix
60-
61-\section{Additional Figures}
62-\label{sec:appendix_figures}
63-
64-\begin{table}[h]
65-\centering
66-\small
67-\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
68-\label{tab:cross_model}
69-\begin{tabular}{lrr}
70-\toprule
71-\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
72-\midrule
73-1 & 0.702 & 0.640 \\
74-64 & 0.273 & 0.304 \\
75-\midrule
76-Decline & $-$43\,pp & $-$34\,pp \\
77-\bottomrule
78-\end{tabular}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "92821dba-b8aa-41c5-b4a0-aef1eac19092",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "38:\\section*{Limitations}\n39-\n40-Our findings are subject to three main limitations.\n41-\\textbf{(1)~Model and statistical scope.}\n42-Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\\S\\ref{sec:multi_channel}) or SDGD failure analysis (\\S\\ref{sec:sdgd}), and proprietary-model generalization remains open.\n43-TOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive; the interaction point estimate (0.47\\,pp) falls within the $\\pm 3$\\,pp equivalence margin.\n44-BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\\,=\\,0.88$\\,pp is 18--44\\% of the observed effect size (Appendix~\\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.\n45-All evidence is correlational with controlled stratification; mechanistic confirmation at the attention or logit level remains future work.\n46-%\n47-\\textbf{(2)~DocRED VIF confounding.}\n48-DocRED exhibits severe multicollinearity (VIF${}\\,=\\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\\,=\\,5.6\\%$ serves only as directional evidence, and the count${}\\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}).\n49-%\n50-\\textbf{(3)~Experimental scope.}\n51-Evaluations cover four English-language Wikipedia/Wikidata-derived datasets in a training-free zero-shot setting; few-shot, fine-tuned, domain-specific (e.g., biomedical, legal), and non-English scenarios remain untested.\n52-BCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\\ref{app:relaxed-matching}).\n53-Batches share prompt template and LLM but type composition is independently sampled; cross-dataset consistency is treated as converging evidence rather than independent replication \\citep{rothman-1990}, and core claims are robust to Bonferroni correction (all $p < 0.001$) \\citep{dror-2018-significance}.\n54-\n55-% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n56-\n57-\\bibliography{references}\n58-\n59-\\appendix\n60-\n61-\\section{Additional Figures}\n62-\\label{sec:appendix_figures}\n63-\n64-\\begin{table}[h]\n65-\\centering\n66-\\small\n67-\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n68-\\label{tab:cross_model}\n69-\\begin{tabular}{lrr}\n70-\\toprule\n71-\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n72-\\midrule\n73-1 & 0.702 & 0.640 \\\\\n74-64 & 0.273 & 0.304 \\\\\n75-\\midrule\n76-Decline & $-$43\\,pp & $-$34\\,pp \\\\\n77-\\bottomrule\n78-\\end{tabular}",
    "numLines": 41
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
I can see the Limitations section at lines 38-53. The relevant sentence is on line 43:

"TOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive; the interaction point estimate (0.47\,pp) falls within the $\pm 3$\,pp equivalence margin."

I need to insert the explanation after "logit-scale evidence is inconclusive". Let me think about how to do this.

The sentence to insert is: "reflecting the inflated variance of logit-transformed proportions in the 0.37–0.86 accuracy range rather than a qualitative divergence from the linear-scale finding"


Now I'm working out where exactly this fits. The insertion should go right after "inconclusive," to clarify why the logit-scale evidence is inconclusive. This will make the sentence flow as "...logit-scale evidence is inconclusive, reflecting the inflated variance..." The section is currently about 14 lines, and adding roughly half a line of text should keep it within the ~15 line limit, so I need to be careful with the edit to maintain the section's length.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "945b7710-d575-4a02-a37d-5eadbb5ecf16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZxM4ugjw6gosJnzXUupFd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1199,
      "cache_read_input_tokens": 25098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1199
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

_source line 16_

Found the Limitations section (lines 38–53). The relevant text is on line 43. I'll insert the clause after "inconclusive".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "ec5ce032-8d5a-4d6c-a8c6-678642138a28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZxM4ugjw6gosJnzXUupFd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1199,
      "cache_read_input_tokens": 25098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1199
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01TfBN78uzpxubFDozsoFdiZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 38,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "5310044a-c812-478a-a9c5-9600b592ec2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZxM4ugjw6gosJnzXUupFd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1199,
      "cache_read_input_tokens": 25098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1199
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

_source line 18 · 2026-05-22T07:35:13.135Z_

<details><summary>↩ Tool result · `toolu_01TfBN78uzpxubFDozsoFdiZ`</summary>

```text
38	\section*{Limitations}
39	
40	Our findings are subject to three main limitations.
41	\textbf{(1)~Model and statistical scope.}
42	Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\S\ref{sec:multi_channel}) or SDGD failure analysis (\S\ref{sec:sdgd}), and proprietary-model generalization remains open.
43	TOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive; the interaction point estimate (0.47\,pp) falls within the $\pm 3$\,pp equivalence margin.
44	BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\,=\,0.88$\,pp is 18--44\% of the observed effect size (Appendix~\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.
45	All evidence is correlational with controlled stratification; mechanistic confirmation at the attention or logit level remains future work.
46	%
47	\textbf{(2)~DocRED VIF confounding.}
48	DocRED exhibits severe multicollinearity (VIF${}\,=\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\,=\,5.6\%$ serves only as directional evidence, and the count${}\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}).
49	%
50	\textbf{(3)~Experimental scope.}
51	Evaluations cover four English-language Wikipedia/Wikidata-derived datasets in a training-free zero-shot setting; few-shot, fine-tuned, domain-specific (e.g., biomedical, legal), and non-English scenarios remain untested.
52	BCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\ref{app:relaxed-matching}).
53	Batches share prompt template and LLM but type composition is independently sampled; cross-dataset consistency is treated as converging evidence rather than independent replication \citep{rothman-1990}, and core claims are robust to Bonferroni correction (all $p < 0.001$) \citep{dror-2018-significance}.
54	
55	% \input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF
56	
57	\bibliography{references}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "7daf40ab-a87c-4192-9036-6cd821d9658f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\section*{Limitations}\n\nOur findings are subject to three main limitations.\n\\textbf{(1)~Model and statistical scope.}\nPrimary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\\S\\ref{sec:multi_channel}) or SDGD failure analysis (\\S\\ref{sec:sdgd}), and proprietary-model generalization remains open.\nTOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive; the interaction point estimate (0.47\\,pp) falls within the $\\pm 3$\\,pp equivalence margin.\nBCS-controlled experiments use greedy decoding with a single seed; residual SD${}\\,=\\,0.88$\\,pp is 18--44\\% of the observed effect size (Appendix~\\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.\nAll evidence is correlational with controlled stratification; mechanistic confirmation at the attention or logit level remains future work.\n%\n\\textbf{(2)~DocRED VIF confounding.}\nDocRED exhibits severe multicollinearity (VIF${}\\,=\\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\\,=\\,5.6\\%$ serves only as directional evidence, and the count${}\\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}).\n%\n\\textbf{(3)~Experimental scope.}\nEvaluations cover four English-language Wikipedia/Wikidata-derived datasets in a training-free zero-shot setting; few-shot, fine-tuned, domain-specific (e.g., biomedical, legal), and non-English scenarios remain untested.\nBCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\\ref{app:relaxed-matching}).\nBatches share prompt template and LLM but type composition is independently sampled; cross-dataset consistency is treated as converging evidence rather than independent replication \\citep{rothman-1990}, and core claims are robust to Bonferroni correction (all $p < 0.001$) \\citep{dror-2018-significance}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}",
      "numLines": 20,
      "startLine": 38,
      "totalLines": 919
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01HNpHbt7JAjw6fK9TmEnZyJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "logit-scale evidence is inconclusive; the interaction",
  "new_string": "logit-scale evidence is inconclusive, reflecting the inflated variance of logit-transformed proportions in the 0.37--0.86 accuracy range rather than a qualitative divergence from the linear-scale finding; the interaction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "618ac94e-bb11-46c6-a279-f0883e7a438e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPsXqFU5KwSS5JDEbRrfxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1326,
      "cache_read_input_tokens": 26297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1326
      },
      "output_tokens": 65,
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

_source line 20 · 2026-05-22T07:35:16.290Z_

<details><summary>↩ Tool result · `toolu_01HNpHbt7JAjw6fK9TmEnZyJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "358dc3fd-4cd8-46fe-b24d-87e29bb1938b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "logit-scale evidence is inconclusive; the interaction",
    "newString": "logit-scale evidence is inconclusive, reflecting the inflated variance of logit-transformed proportions in the 0.37--0.86 accuracy range rather than a qualitative divergence from the linear-scale finding; the interaction",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\nOur findings are subject to three main limitations.\n\\textbf{(1)~Model and statistical scope.}\nPrimary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\\S\\ref{sec:multi_channel}) or SDGD failure analysis (\\S\\ref{sec:sdgd}), and proprietary-model generalization remains open.\nTOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive; the interaction point estimate (0.47\\,pp) falls within the $\\pm 3$\\,pp equivalence margin.\nBCS-controlled experiments use greedy decoding with a single seed; residual SD${}\\,=\\,0.88$\\,pp is 18--44\\% of the observed effect size (Appendix~\\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.\nAll evidence is correlational with controlled stratification; mechanistic confirmation at the attention or logit level remains future work.\n%\n\\textbf{(2)~DocRED VIF confounding.}\nDocRED exhibits severe multicollinearity (VIF${}\\,=\\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\\,=\\,5.6\\%$ serves only as directional evidence, and the count${}\\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}).\n%\n\\textbf{(3)~Experimental scope.}\nEvaluations cover four English-language Wikipedia/Wikidata-derived datasets in a training-free zero-shot setting; few-shot, fine-tuned, domain-specific (e.g., biomedical, legal), and non-English scenarios remain untested.\nBCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\\ref{app:relaxed-matching}).\nBatches share prompt template and LLM but type composition is independently sampled; cross-dataset consistency is treated as converging evidence rather than independent replication \\citep{rothman-1990}, and core claims are robust to Bonferroni correction (all $p < 0.001$) \\citep{dror-2018-significance}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\subsection{Bootstrap CI Robustness}\n\\label{sec:appendix_bootstrap_ci}\n\nBecause batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\\in \\{0.1, \\ldots, 0.9\\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\\%$ to $+6\\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.\n\n\\subsection{Domain Distribution in Extreme-BCS Batches}\n\\label{sec:appendix_domain_distribution}\n\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\nTable~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type (Table~\\ref{tab:fewshot_bcs}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & 0.97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & 0.92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & 0.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets (Table~\\ref{tab:renaming}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds; Table~\\ref{tab:relaxed_matching}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 40,
        "oldLines": 7,
        "newStart": 40,
        "newLines": 7,
        "lines": [
          " Our findings are subject to three main limitations.",
          " \\textbf{(1)~Model and statistical scope.}",
          " Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\\S\\ref{sec:multi_channel}) or SDGD failure analysis (\\S\\ref{sec:sdgd}), and proprietary-model generalization remains open.",
          "-TOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive; the interaction point estimate (0.47\\,pp) falls within the $\\pm 3$\\,pp equivalence margin.",
          "+TOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive, reflecting the inflated variance of logit-transformed proportions in the 0.37--0.86 accuracy range rather than a qualitative divergence from the linear-scale finding; the interaction point estimate (0.47\\,pp) falls within the $\\pm 3$\\,pp equivalence margin.",
          " BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\\,=\\,0.88$\\,pp is 18--44\\% of the observed effect size (Appendix~\\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.",
          " All evidence is correlational with controlled stratification; mechanistic confirmation at the attention or logit level remains future work.",
          " %"
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

_source line 21_

Now compile to check for errors and page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "62d52358-1bc2-452f-a4f0-0658159c3ebf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xrsxu95cdLf2moVodjSK4X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 258
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

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01FXDQ3sTcXqvJ7ZJbKdW4Du`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "9325af84-446f-4c71-b2c2-c689bb4b761d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xrsxu95cdLf2moVodjSK4X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 258
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

_source line 23 · 2026-05-22T07:35:23.331Z_

<details><summary>↩ Tool result · `toolu_01FXDQ3sTcXqvJ7ZJbKdW4Du`</summary>

```text
s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 477580 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "00b1cea5-4309-47c8-adf0-d249bc8475e2",
  "tool_use_result": {
    "stdout": "s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (27 pages, 477580 bytes).\nTranscript written on main.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01V6oRMYu1fF1aHjeABhzvai`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && bibtex main 2>/dev/null; pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!|Error|Warning.*undefined|Output written\" && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!|Error|Warning.*undefined|Output written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "087f4bca-559a-4056-98c2-04d9380f5b62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017PPfrk1FMRR2Yj7Eevey2N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 964,
      "cache_read_input_tokens": 27881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 964
      },
      "output_tokens": 68,
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

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bdreh3fh0",
  "tool_use_id": "toolu_01V6oRMYu1fF1aHjeABhzvai",
  "description": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && bibtex main 2>/dev/null; pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!|Error|Warning.*undefined|Output written\" && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!|Error|Warning.*undefined|Output written\"",
  "task_type": "local_bash",
  "uuid": "788bcb86-ab30-4eb5-a7ba-b58f080dd9e5",
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0"
}
```

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bdreh3fh0",
  "tool_use_id": "toolu_01V6oRMYu1fF1aHjeABhzvai",
  "status": "completed",
  "output_file": "",
  "summary": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && bibtex main 2>/dev/null; pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!|Error|Warning.*undefined|Output written\" && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!|Error|Warning.*undefined|Output written\"",
  "uuid": "a04a7e3b-ca4e-4164-af95-5ea956914c17",
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0"
}
```

---

### Tool result

_source line 27 · 2026-05-22T07:35:32.177Z_

<details><summary>↩ Tool result · `toolu_01V6oRMYu1fF1aHjeABhzvai`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Warning--can't use both volume and number fields in guo-2021-label-confusion
(There was 1 warning)
\T1/ptm/m/n/10.95 (+20) Error tax-on-omy de-com-po-si-tion (Ta-ble [][]6[][] an
Output written on main.pdf (27 pages, 478036 bytes).
\T1/ptm/m/n/10.95 (+20) Error tax-on-omy de-com-po-si-tion (Ta-ble [][]6[][] an
Output written on main.pdf (27 pages, 477900 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "deb04a33-769f-489b-bb2b-71bc508a0fc4",
  "tool_use_result": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib\nWarning--can't use both volume and number fields in guo-2021-label-confusion\n(There was 1 warning)\n\\T1/ptm/m/n/10.95 (+20) Error tax-on-omy de-com-po-si-tion (Ta-ble [][]6[][] an\nOutput written on main.pdf (27 pages, 478036 bytes).\n\\T1/ptm/m/n/10.95 (+20) Error tax-on-omy de-com-po-si-tion (Ta-ble [][]6[][] an\nOutput written on main.pdf (27 pages, 477900 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01STHEPS7xKT81hyY4J46D5Q`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -c \"Warning.*undefined\" main.log; grep \"^!\" main.log | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "d62c3653-ecaf-4804-9fee-e106d4c2acd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vx6npBgxQRhauYTR1VCf2w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 397,
      "cache_read_input_tokens": 28845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 397
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

_source line 29 · 2026-05-22T07:35:35.748Z_

<details><summary>↩ Tool result · `toolu_01STHEPS7xKT81hyY4J46D5Q`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "fb771b49-da89-4121-9dc3-5f580fb4e5a5",
  "tool_use_result": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 30_

0 errors, 0 undefined references. Now check body page count — the Limitations section must end before page 9 (body ≤ 8 pages).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "6dfa066c-fe5a-4482-a362-1d20118377d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WyhujtohsAufideoDJ9TFK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 29242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 121
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

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01C2mRkzFBMWDsLUxitXgvNN`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"\\\\\\\\section\\*{Limitations}\" main.log 2>/dev/null; grep -n \"\\\\\\\\bibliography\" main.log 2>/dev/null; python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\nlines = r.stdout.split('\\x0c')\n# Find which page has Limitations and References/Bibliography\nfor i, page in enumerate(lines):\n    if 'Limitations' in page or 'References' in page or 'Bibliography' in page:\n        # Show first 80 chars of page\n        print(f'Page {i+1}: {page[:120].strip()!r}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "c0a967a9-8ef9-41f3-a516-71fe07325539",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WyhujtohsAufideoDJ9TFK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 29242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 121
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

_source line 32 · 2026-05-22T07:35:42.912Z_

<details><summary>↩ Tool result · `toolu_01C2mRkzFBMWDsLUxitXgvNN`</summary>

```text
Page 8: '569\n570\n571\n572\n573\n574\n575\n576\n577\n578\n579\n580\n581\n582\n583\n584\n585\n586\n587\n588\n589\n590\n591\n592\n593\n594\n595\n596\n597\n598'
Page 9: '702\n\ntion (LLaMA-8B/70B, Gemini Flash) covers Dimensions 1–2 but not secondary analyses such as\nTOST factorial interacti'
Page 22: '1765\n1766\n1767\n1768\n1769\n1770\n1771\n1772\n1773\n\n1774\n1775\n1776\n1777\n1778\n1779\n1780\n1781\n1782\n1783\n1784\n1785\n1786\n1787\n\n178'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "9d860560-650b-4d7b-a6d6-6a7018100b24",
  "tool_use_result": {
    "stdout": "Page 8: '569\\n570\\n571\\n572\\n573\\n574\\n575\\n576\\n577\\n578\\n579\\n580\\n581\\n582\\n583\\n584\\n585\\n586\\n587\\n588\\n589\\n590\\n591\\n592\\n593\\n594\\n595\\n596\\n597\\n598'\nPage 9: '702\\n\\ntion (LLaMA-8B/70B, Gemini Flash) covers Dimensions 1–2 but not secondary analyses such as\\nTOST factorial interacti'\nPage 22: '1765\\n1766\\n1767\\n1768\\n1769\\n1770\\n1771\\n1772\\n1773\\n\\n1774\\n1775\\n1776\\n1777\\n1778\\n1779\\n1780\\n1781\\n1782\\n1783\\n1784\\n1785\\n1786\\n1787\\n\\n178'",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
The Limitations section appears to start on page 9. Let me check more carefully what's on page 8 and page 9 to understand the body page count. The EMNLP 2026 rule says body ≤ 8 pages, with Limitations not counting towards the page limit.

Actually, re-reading the rule: "EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit"

So Limitations doesn't count. Let me check where References start.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "0f54e23c-f050-4041-80aa-0270aba788b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMJY2otBiJ18mp6B9u3KoZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 29363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 564
      },
      "output_tokens": 9,
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

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_0141pp5KHDDTcy3FYZm6NNoV`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\nfor i, page in enumerate(pages):\n    if 'Limitations' in page:\n        print(f'Page {i+1} contains Limitations')\n    if 'References' in page and i < 15:\n        print(f'Page {i+1} contains References')\n    if 'Appendix' in page or 'Additional Figures' in page:\n        print(f'Page {i+1} contains Appendix marker')\n        break\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "bb9e29ab-0f76-4c4a-8ebf-38866f271ab2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMJY2otBiJ18mp6B9u3KoZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 29363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 564
      },
      "output_tokens": 9,
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

_source line 35 · 2026-05-22T07:35:50.988Z_

<details><summary>↩ Tool result · `toolu_0141pp5KHDDTcy3FYZm6NNoV`</summary>

```text
Page 3 contains Appendix marker
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "9b857170-e3fb-4265-937c-40caadd45a78",
  "tool_use_result": {
    "stdout": "Page 3 contains Appendix marker",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_014RwcGg2K8rz94rTivs147M`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\nfor i, page in enumerate(pages):\n    lower = page.lower()\n    if 'limitation' in lower:\n        print(f'Page {i+1} has Limitations')\n    if 'references' in lower or 'bibliography' in lower:\n        # check if it's a section header\n        for line in page.split('\\n'):\n            if 'references' in line.lower() and len(line.strip()) < 30:\n                print(f'Page {i+1} has References header: {line.strip()!r}')\n                break\n    if 'additional figures' in lower or '\\\\\\\\appendix' in lower:\n        for line in page.split('\\n'):\n            if 'additional' in line.lower():\n                print(f'Page {i+1}: {line.strip()!r}')\n                break\n\" 2>&1 | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "bc0bc8a2-3b4d-4366-8216-157bfc749d6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJNCKUsvSu6TDho34LaVAD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 424,
      "cache_read_input_tokens": 29927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 424
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

_source line 37 · 2026-05-22T07:35:56.922Z_

<details><summary>↩ Tool result · `toolu_014RwcGg2K8rz94rTivs147M`</summary>

```text
Page 1 has Limitations
Page 8 has Limitations
Page 9 has References header: 'References'
Page 12: 'Additional Figures'
Page 22 has Limitations
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "1dc5b5f3-3aa2-4239-bc71-9bdd50c004a4",
  "tool_use_result": {
    "stdout": "Page 1 has Limitations\nPage 8 has Limitations\nPage 9 has References header: 'References'\nPage 12: 'Additional Figures'\nPage 22 has Limitations",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 38_

Limitations is on page 8, References on page 9, Appendix starts page 12. Body (main text through end of page 8) fits within the 8-page limit. Limitations doesn't count towards the limit per EMNLP 2026 rules anyway.

Let me verify the edited text reads correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "513e4801-1d6b-433c-8795-258be7fb10ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2oq5EwEHpceQyjSTNZAXS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 30351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 407
      },
      "output_tokens": 2,
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

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01WHJmbmGbifpwvNSVScEMnk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 42,
  "limit": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "99d47bff-18a5-4de1-bac7-3245cb30587b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2oq5EwEHpceQyjSTNZAXS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 30351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 407
      },
      "output_tokens": 2,
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

_source line 40 · 2026-05-22T07:36:01.316Z_

<details><summary>↩ Tool result · `toolu_01WHJmbmGbifpwvNSVScEMnk`</summary>

```text
42	Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\S\ref{sec:multi_channel}) or SDGD failure analysis (\S\ref{sec:sdgd}), and proprietary-model generalization remains open.
43	TOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive, reflecting the inflated variance of logit-transformed proportions in the 0.37--0.86 accuracy range rather than a qualitative divergence from the linear-scale finding; the interaction point estimate (0.47\,pp) falls within the $\pm 3$\,pp equivalence margin.
44	BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\,=\,0.88$\,pp is 18--44\% of the observed effect size (Appendix~\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "d6a41851-f6f2-43da-8882-9e6354b8548b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\\S\\ref{sec:multi_channel}) or SDGD failure analysis (\\S\\ref{sec:sdgd}), and proprietary-model generalization remains open.\nTOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive, reflecting the inflated variance of logit-transformed proportions in the 0.37--0.86 accuracy range rather than a qualitative divergence from the linear-scale finding; the interaction point estimate (0.47\\,pp) falls within the $\\pm 3$\\,pp equivalence margin.\nBCS-controlled experiments use greedy decoding with a single seed; residual SD${}\\,=\\,0.88$\\,pp is 18--44\\% of the observed effect size (Appendix~\\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.",
      "numLines": 3,
      "startLine": 42,
      "totalLines": 919
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

**结果：**

- **插入位置：** `docs/paper/main.tex:43`，在 "inconclusive" 后插入逗号接归因从句
- **补偿性压缩：** 不需要。Limitations 仍为 14 行 LaTeX（3 点 1 段），整体长度未增加行数
- **编译结果：** 0 errors，0 undefined references，body 8 pages（Limitations 在 page 8，References 从 page 9 起）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "uuid": "0e6cce79-26dd-4c79-b510-494cbbe5e926",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPKwhSeg5LeE4xxG8W2tSf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 30758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
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

_source line 42_

**结果：**

- **插入位置：** `docs/paper/main.tex:43`，在 "inconclusive" 后插入逗号接归因从句
- **补偿性压缩：** 不需要。Limitations 仍为 14 行 LaTeX（3 点 1 段），整体长度未增加行数
- **编译结果：** 0 errors，0 undefined references，body 8 pages（Limitations 在 page 8，References 从 page 9 起）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 87784,
  "duration_api_ms": 80183,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "1d410a53-553d-4753-8d91-5ef82948ddb0",
  "total_cost_usd": 0.39922425000000006,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 19383,
    "cache_read_input_tokens": 393703,
    "output_tokens": 3194,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 19383,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 140,
        "cache_read_input_tokens": 30758,
        "cache_creation_input_tokens": 466,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 466
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1209,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001299,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 3194,
      "cacheReadInputTokens": 393703,
      "cacheCreationInputTokens": 19383,
      "webSearchRequests": 0,
      "costUSD": 0.39792525000000006,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f42918f7-af0f-419f-8251-441c1fdb261f"
}
```

</details>

---
