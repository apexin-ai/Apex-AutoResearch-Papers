# paper narrative b abstract contributions

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_narrative-b-abstract-contributions_20260516T221352.log`
- **Structured JSON:** [`9cfe4b91c6418cd20698.json`](../../sessions/9c/9cfe4b91c6418cd20698.json)

## Before a recorded user message

12 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06",
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
  "uuid": "9f475e2b-f333-4eb0-bf10-ecf167329917",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778983200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "43ba84b5-91ac-4863-ba0c-dd6b71642be6",
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to write two documents:
1. A Narrative B Abstract draft (150-250 words) for CoRL 2026
2. A Contribution List (3-4 items)

Let me carefully craft these based on the provided data and constraints.

Key framing: Narrative B = mechanism insight as core contribution (obs_only robustness vs perdof collapse), SR improvement as supplementary evidence.

Let me write the abstract following the four questions and all the constraints (no em-dash, no -ing endings, no data dumping, etc.).

Then the contribution list with experimental support annotations.

Let me first check if the artifacts directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06",
  "uuid": "e1dc3235-eef3-4000-bfd1-7420d5001786",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015deCqRc4NYuUg7V3pBZARg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13240,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13240
      },
      "output_tokens": 33,
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

<details open><summary>🔧 Tool call — Bash · `toolu_01UwQnqUYo2JLGNh8ndta5gz`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06",
  "uuid": "23a8ed24-d7dc-4612-b74d-eb4f83d0e323",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015deCqRc4NYuUg7V3pBZARg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13240,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13240
      },
      "output_tokens": 33,
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

_source line 6 · 2026-05-16T22:14:10.170Z_

<details><summary>↩ Tool result · `toolu_01UwQnqUYo2JLGNh8ndta5gz`</summary>

```text
__pycache__
_project
ablation_eval_commands.md
analysis
analysis_magnitude_sweep.py
analysis_object_benchmark.py
analysis_spatial_final.py
argmin_seed44_r2_results.json
citation_attribution_audit.md
citation_audit_report.md
competitive_analysis_20260515.md
competitor_analysis.md
corl_paper_outline.md
correction_degradation_literature.md
crm-train-v2-k5
crm_bug_audit.md
diag-eval-v6-batch-failure.md
diagnose-norm02-seed44-r2.md
dream_reports
eval-acr-object-v4-obs-only
eval-acr-object-v4-scalar
eval-argmin-object-seed44-r2
eval-mag-perdof-norm03
eval-obs-only-object-default-seed45
eval-obs-only-object-norm02-seed44-r2
eval-obs-only-object-norm02-seed46
eval-obs-only-object-norm03-seed44
eval-reconvla-spatial-v1-diag.md
eval-vla-mean-object-seed44
experiment_progress_20260515.md
fallback_narrative_draft.md
fig_magnitude_curve.py
figures
fisher_analysis.py
fix_plan_code_sketch.md
gpu_health_snapshot_20260515.md
lerobot-pipeline-alignment.md
libero-smolvla-env-report.md
literature_gap_report.md
magnitude_curve.pdf
magnitude_curve.png
magnitude_curve_data.json
magnitude_curve_draft.pdf
magnitude_curve_draft.png
magnitude_sweep_summary.md
manifest.yaml
method_section_draft.tex
mvp-point-reaching
narrative_b_draft.md
object_eval_commands.md
object_results_summary.md
pipeline-dimension-verification.md
pooled_fisher_test_v2.py
precompute-k5
precompute-k5-analysis.md
progress_scan_loop9.md
reconvla-comparison-report.md
report_eval_progress.md
report_running_status.md
results_tables.md
seed43_env_check.md
seed44_obs_only_norm02_per_task.json
smolvla-libero-finetune-survey.md
smolvla_wrapper_fixed.py
spatial_analysis_prep.md
spatial_comparison_template.md
three_seed_fisher_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06",
  "uuid": "4e816aab-7fd6-433f-8433-e909995d0cb7",
  "tool_use_result": {
    "stdout": "__pycache__\n_project\nablation_eval_commands.md\nanalysis\nanalysis_magnitude_sweep.py\nanalysis_object_benchmark.py\nanalysis_spatial_final.py\nargmin_seed44_r2_results.json\ncitation_attribution_audit.md\ncitation_audit_report.md\ncompetitive_analysis_20260515.md\ncompetitor_analysis.md\ncorl_paper_outline.md\ncorrection_degradation_literature.md\ncrm-train-v2-k5\ncrm_bug_audit.md\ndiag-eval-v6-batch-failure.md\ndiagnose-norm02-seed44-r2.md\ndream_reports\neval-acr-object-v4-obs-only\neval-acr-object-v4-scalar\neval-argmin-object-seed44-r2\neval-mag-perdof-norm03\neval-obs-only-object-default-seed45\neval-obs-only-object-norm02-seed44-r2\neval-obs-only-object-norm02-seed46\neval-obs-only-object-norm03-seed44\neval-reconvla-spatial-v1-diag.md\neval-vla-mean-object-seed44\nexperiment_progress_20260515.md\nfallback_narrative_draft.md\nfig_magnitude_curve.py\nfigures\nfisher_analysis.py\nfix_plan_code_sketch.md\ngpu_health_snapshot_20260515.md\nlerobot-pipeline-alignment.md\nlibero-smolvla-env-report.md\nliterature_gap_report.md\nmagnitude_curve.pdf\nmagnitude_curve.png\nmagnitude_curve_data.json\nmagnitude_curve_draft.pdf\nmagnitude_curve_draft.png\nmagnitude_sweep_summary.md\nmanifest.yaml\nmethod_section_draft.tex\nmvp-point-reaching\nnarrative_b_draft.md\nobject_eval_commands.md\nobject_results_summary.md\npipeline-dimension-verification.md\npooled_fisher_test_v2.py\nprecompute-k5\nprecompute-k5-analysis.md\nprogress_scan_loop9.md\nreconvla-comparison-report.md\nreport_eval_progress.md\nreport_running_status.md\nresults_tables.md\nseed43_env_check.md\nseed44_obs_only_norm02_per_task.json\nsmolvla-libero-finetune-survey.md\nsmolvla_wrapper_fixed.py\nspatial_analysis_prep.md\nspatial_comparison_template.md\nthree_seed_fisher_analysis.py",
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

_source line 7_

<details open><summary>🔧 Tool call — Write · `toolu_01WqWo7terN9CnekzfSvhnCq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/narrative_b_abstract_draft.md",
  "content": "# Narrative B Abstract Draft (CoRL 2026)\n\n## Abstract (v1)\n\nVision-Language-Action (VLA) models for robotic manipulation suffer from compounding errors during closed-loop execution, yet improving their inference-time performance without retraining remains largely unexplored. Prior work on sample selection (choosing among multiple action candidates) offers modest gains but hits a ceiling when the candidate pool lacks high-quality samples. Correction conditioning, where a lightweight module adjusts selected actions before execution, represents an untapped axis for improvement, but the choice of conditioning features and the magnitude of corrections have not been systematically studied.\n\nWe propose a sample-then-correct pipeline that first selects promising action candidates via conformal prediction scores, then applies bounded additive corrections conditioned on auxiliary features. Through controlled experiments on the LIBERO manipulation benchmark, we conduct a systematic comparison of correction conditioning strategies and uncover a critical mechanism: observation-derived features yield corrections that remain robust across a wide range of magnitudes (success rate 13-22% vs. 10-12% VLA-only baseline), while per-degree-of-freedom conformal features cause monotonic performance collapse as correction magnitude increases (from 14% to 0%). This divergence reveals that magnitude sensitivity, not feature informativeness alone, determines whether inference-time correction helps or harms a frozen VLA policy. Our findings establish that observation features provide safe correction signals, while conformal nonconformity scores require strict magnitude constraints to avoid catastrophic degradation.\n\n---\n\n**Word count:** ~210\n\n## Self-check\n- [x] Problem stated (VLA closed-loop robustness, inference-time without retraining)\n- [x] Importance (selection ceiling, correction unexplored)\n- [x] Proposal (sample-then-correct + systematic conditioning comparison)\n- [x] Results (obs_only robust, perdof collapses, magnitude is key)\n- [x] No em-dash\n- [x] No -ing phrase endings\n- [x] Abbreviations defined (VLA)\n- [x] ≤3 key numbers (13-22%, 10-12%, 14%→0%)\n- [x] Differentiation from A2C2 (systematic conditioning comparison) and ReconVLA (correction, not just UQ) implicit\n- [x] Narrative B framing: mechanism insight is the core, SR improvement is evidence\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06",
  "uuid": "6d09132b-ab07-4a20-9004-464e0540589c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0124NZJQBQsDdhptts7oGqgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 25081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 904
      },
      "output_tokens": 53,
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

_source line 8 · 2026-05-16T22:14:28.758Z_

<details><summary>↩ Tool result · `toolu_01WqWo7terN9CnekzfSvhnCq`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/narrative_b_abstract_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06",
  "uuid": "79fdcc74-829e-4eb6-8f14-6846eb045944",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/narrative_b_abstract_draft.md",
    "content": "# Narrative B Abstract Draft (CoRL 2026)\n\n## Abstract (v1)\n\nVision-Language-Action (VLA) models for robotic manipulation suffer from compounding errors during closed-loop execution, yet improving their inference-time performance without retraining remains largely unexplored. Prior work on sample selection (choosing among multiple action candidates) offers modest gains but hits a ceiling when the candidate pool lacks high-quality samples. Correction conditioning, where a lightweight module adjusts selected actions before execution, represents an untapped axis for improvement, but the choice of conditioning features and the magnitude of corrections have not been systematically studied.\n\nWe propose a sample-then-correct pipeline that first selects promising action candidates via conformal prediction scores, then applies bounded additive corrections conditioned on auxiliary features. Through controlled experiments on the LIBERO manipulation benchmark, we conduct a systematic comparison of correction conditioning strategies and uncover a critical mechanism: observation-derived features yield corrections that remain robust across a wide range of magnitudes (success rate 13-22% vs. 10-12% VLA-only baseline), while per-degree-of-freedom conformal features cause monotonic performance collapse as correction magnitude increases (from 14% to 0%). This divergence reveals that magnitude sensitivity, not feature informativeness alone, determines whether inference-time correction helps or harms a frozen VLA policy. Our findings establish that observation features provide safe correction signals, while conformal nonconformity scores require strict magnitude constraints to avoid catastrophic degradation.\n\n---\n\n**Word count:** ~210\n\n## Self-check\n- [x] Problem stated (VLA closed-loop robustness, inference-time without retraining)\n- [x] Importance (selection ceiling, correction unexplored)\n- [x] Proposal (sample-then-correct + systematic conditioning comparison)\n- [x] Results (obs_only robust, perdof collapses, magnitude is key)\n- [x] No em-dash\n- [x] No -ing phrase endings\n- [x] Abbreviations defined (VLA)\n- [x] ≤3 key numbers (13-22%, 10-12%, 14%→0%)\n- [x] Differentiation from A2C2 (systematic conditioning comparison) and ReconVLA (correction, not just UQ) implicit\n- [x] Narrative B framing: mechanism insight is the core, SR improvement is evidence\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Write · `toolu_01S6bxz8QC752jKb86S6VkU7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/contribution_list.md",
  "content": "# Contribution List (Narrative B)\n\n## Contributions\n\n1. **A sample-then-correct pipeline for inference-time VLA improvement.** We introduce a two-stage framework that combines conformal prediction-based candidate selection with bounded additive corrections, enabling post-hoc performance gains on frozen VLA policies without retraining or architectural modification. *(Section 3: Method; Table 1: pooled results across seeds)*\n\n2. **Mechanism insight: observation features provide robust correction signals while per-DOF conformal features collapse under magnitude scaling.** Through systematic comparison of conditioning strategies, we demonstrate that observation-derived corrections maintain stable performance across magnitudes (13-22% success rate for norm 0.03-1.42), whereas per-degree-of-freedom nonconformity scores exhibit monotonic degradation (14% to 0%) beyond a narrow safe region. This establishes magnitude sensitivity as the critical factor determining correction viability. *(Section 4.2: Magnitude Curve Analysis; Figure 2: magnitude-performance curves; Table 2: cross-magnitude comparison)*\n\n3. **Magnitude sensitivity as a previously unidentified failure mode for learned corrections.** We show that the same correction architecture succeeds or fails depending solely on the conditioning feature's interaction with correction norm, revealing that bounded magnitude control is necessary for safe inference-time intervention on VLA policies. *(Section 4.3: Uncapped comparison; obs_only 17% vs perdof 0% at default norm)*\n\n4. **Honest negative result: per-DOF conformal features do not generalize as correction signals.** Despite their theoretical appeal as calibrated uncertainty estimates per action dimension, conformal nonconformity scores fail to provide useful directional guidance for corrections when magnitude is not tightly constrained. This negative finding informs future work on conformal prediction applications in robot learning. *(Section 4.4: Discussion; Spatial benchmark shows no method separates from baseline at 34-35%)*\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06",
  "uuid": "79cb58b5-ac80-46f7-aadc-9c71e749aea9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0124NZJQBQsDdhptts7oGqgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 25081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 904
      },
      "output_tokens": 53,
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

_source line 10 · 2026-05-16T22:14:39.568Z_

<details><summary>↩ Tool result · `toolu_01S6bxz8QC752jKb86S6VkU7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/contribution_list.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06",
  "uuid": "974691ec-b917-4621-9ceb-daf624d089f1",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/contribution_list.md",
    "content": "# Contribution List (Narrative B)\n\n## Contributions\n\n1. **A sample-then-correct pipeline for inference-time VLA improvement.** We introduce a two-stage framework that combines conformal prediction-based candidate selection with bounded additive corrections, enabling post-hoc performance gains on frozen VLA policies without retraining or architectural modification. *(Section 3: Method; Table 1: pooled results across seeds)*\n\n2. **Mechanism insight: observation features provide robust correction signals while per-DOF conformal features collapse under magnitude scaling.** Through systematic comparison of conditioning strategies, we demonstrate that observation-derived corrections maintain stable performance across magnitudes (13-22% success rate for norm 0.03-1.42), whereas per-degree-of-freedom nonconformity scores exhibit monotonic degradation (14% to 0%) beyond a narrow safe region. This establishes magnitude sensitivity as the critical factor determining correction viability. *(Section 4.2: Magnitude Curve Analysis; Figure 2: magnitude-performance curves; Table 2: cross-magnitude comparison)*\n\n3. **Magnitude sensitivity as a previously unidentified failure mode for learned corrections.** We show that the same correction architecture succeeds or fails depending solely on the conditioning feature's interaction with correction norm, revealing that bounded magnitude control is necessary for safe inference-time intervention on VLA policies. *(Section 4.3: Uncapped comparison; obs_only 17% vs perdof 0% at default norm)*\n\n4. **Honest negative result: per-DOF conformal features do not generalize as correction signals.** Despite their theoretical appeal as calibrated uncertainty estimates per action dimension, conformal nonconformity scores fail to provide useful directional guidance for corrections when magnitude is not tightly constrained. This negative finding informs future work on conformal prediction applications in robot learning. *(Section 4.4: Discussion; Spatial benchmark shows no method separates from baseline at 34-35%)*\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 11_

两个文件已写入：

**Abstract** (~210 words): 以 mechanism insight 为核心叙事线，obs_only robustness vs perdof collapse 作为主要发现，SR improvement 只作为 supporting evidence。隐含了与 A2C2（只做 correction 不做 systematic conditioning comparison）和 ReconVLA（只做 UQ 不做 correction）的差异化。

**Contribution List** (4 条):
1. Method: sample-then-correct pipeline
2. Core finding: obs_only robust vs perdof collapse 的 mechanism
3. Novel finding: magnitude sensitivity 作为此前未识别的 failure mode
4. Honest negative: per-DOF conformal features 不 generalize（含 spatial 34-35% no-signal 结果）

每条都标注了对应 section/table/figure 支撑。如需调整 framing 力度或精简到 3 条 contribution，告诉我。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06",
  "uuid": "2c842e34-ec3f-453b-b883-af41b70e974e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYZ8qPTpB8ntKGHmzRTS9N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 25985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1324
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

_source line 12_

两个文件已写入：

**Abstract** (~210 words): 以 mechanism insight 为核心叙事线，obs_only robustness vs perdof collapse 作为主要发现，SR improvement 只作为 supporting evidence。隐含了与 A2C2（只做 correction 不做 systematic conditioning comparison）和 ReconVLA（只做 UQ 不做 correction）的差异化。

**Contribution List** (4 条):
1. Method: sample-then-correct pipeline
2. Core finding: obs_only robust vs perdof collapse 的 mechanism
3. Novel finding: magnitude sensitivity 作为此前未识别的 failure mode
4. Honest negative: per-DOF conformal features 不 generalize（含 spatial 34-35% no-signal 结果）

每条都标注了对应 section/table/figure 支撑。如需调整 framing 力度或精简到 3 条 contribution，告诉我。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 47413,
  "duration_api_ms": 48182,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "8582cf81-9f0b-49aa-8865-ea62ddbb2f06",
  "total_cost_usd": 0.17221450000000002,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 15468,
    "cache_read_input_tokens": 62907,
    "output_tokens": 1686,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 15468,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 249,
        "cache_read_input_tokens": 25985,
        "cache_creation_input_tokens": 1324,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1324
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1816,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001911,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 1686,
      "cacheReadInputTokens": 62907,
      "cacheCreationInputTokens": 15468,
      "webSearchRequests": 0,
      "costUSD": 0.17030350000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2ab79ff4-5a2b-4807-982b-f46eb42c6aa0"
}
```

</details>

---
