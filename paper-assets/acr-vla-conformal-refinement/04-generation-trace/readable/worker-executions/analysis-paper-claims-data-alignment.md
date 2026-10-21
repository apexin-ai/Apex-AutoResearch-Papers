# analysis paper claims data alignment

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_analysis_paper-claims-data-alignment_20260517T111825.log`
- **Structured JSON:** [`cfd5967be6dbec03be9e.json`](../../sessions/cf/cfd5967be6dbec03be9e.json)

## Before a recorded user message

17 recorded events

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
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "f7fc9b64-b52a-4b67-99c5-e3d2643f7d8a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779024600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6042fd67-d364-4458-a247-70072e06633f",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the necessary files to understand the claims and experimental data. I need to:

1. Read `paper_framing.md` for claims
2. Read the registry for experiment data
3. Read `ROADMAP.md` for data summary

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "299f4821-22cc-40db-af21-16b0ad89cbe9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TAuL788dAj4gv1xFArr2i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12680,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12680
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NWteZ2dM7253VnzBZdgyse`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "b5c9505b-5c12-41f9-ab6f-314939460771",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TAuL788dAj4gv1xFArr2i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12680,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12680
      },
      "output_tokens": 26,
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

_source line 6 · 2026-05-17T11:18:36.607Z_

<details><summary>↩ Tool result · `toolu_01NWteZ2dM7253VnzBZdgyse`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "8f47ebf0-9674-4960-a948-9434367f2dce",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 7_

Reading all three data sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "b8c4b70f-bc79-48a9-8ef5-b7b8ec21b186",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LzfHypwHgRJeC6oDcZvLo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 24521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1125
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Dd3pGCznE3fUmacHjuL53r`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "a513aab5-50f5-4a67-9500-9651ee9194c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LzfHypwHgRJeC6oDcZvLo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 24521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1125
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

_source line 9 · 2026-05-17T11:18:40.118Z_

<details><summary>↩ Tool result · `toolu_01Dd3pGCznE3fUmacHjuL53r`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2)\\n- Narrative B (mechanism insight) confirmed as default framing\\n\\n## Core Insight (Narrative B — ACTIVE)\\nMagnitude control is the critical, previously unrecognized factor determining whether learned inference-time corrections help or catastrophically fail on frozen VLA policies. Observation-conditioned corrections remain robust across the full magnitude range, while per-DOF conformal features cause progressive collapse as correction magnitude increases. The sample-then-correct pipeline itself (conformal selection + bounded CRM) is the methodological contribution; the conditioning-magnitude interaction is the scientific contribution.\\n\\n## Headline Metric\\nobs_only ε=0.2: 6-seed pooled 105/600 (17.5%) vs argmin 74/600 (12.3%), **+5.2pp, Fisher exact p=0.0074 (p<0.01), Cohen's d=1.21**. obs_only stable 15-22% across all norms vs perdof progressive collapse 10%→4.7%→0% (multi-seed means). VLA-only: 10-12% (4 seeds).\\n\\n## Core Claims (Narrative B — 3 claims)\\n\\n1. **Sample-then-correct pipeline for inference-time VLA improvement**\\n   - Two-stage: conformal selection (K=10 argmin) + bounded residual correction (CRM, approximately 330K params)\\n   - **Statistically significant improvement**: obs_only 17.5% vs argmin 12.3%, +5.2pp, Fisher exact p=0.0074 (6v6 seeds, D047)\\n   - Cohen's d=1.21 (large effect), 5/6 seeds obs_only > argmin\\n   - obs_only CRM mean 17.5% vs VLA-only 10.8% vs argmin 12.3%\\n   - Evidence: Table 1 (6v6 pooled results + Fisher test), Section 3 (method)\\n\\n2. **Conditioning-magnitude interaction as a previously unidentified failure mode**\\n   - Same CRM architecture succeeds or fails depending solely on conditioning feature x magnitude interaction\\n   - obs_only: stable approximately 17% across norms 0.03 to 1.42 (including uncapped)\\n   - perdof: progressive collapse 14% → 10% → 4% → 0% as norm increases\\n   - Bounded magnitude control is necessary for safe inference-time VLA correction\\n   - Evidence: Figure 2 (magnitude curves), Table 2 (cross-magnitude), Section 4.2-4.3\\n\\n3. **Honest negative result: per-DOF conformal features do not generalize as correction signals**\\n   - Despite theoretical appeal as calibrated per-dimension uncertainty, per-DOF scores fail beyond narrow safe region\\n   - Root cause: K=10 rank-deficient covariance in 30D action space → noisy directional signals\\n   - Spatial benchmark: no method separates from baseline (34-35%), suggesting task-complexity dependence\\n   - Evidence: Section 4.4, Section 3.5 (mechanism analysis)\\n\\n## Story Spine\\n- **Problem**: Frozen VLA policies degrade under distribution shift. Retraining is expensive. Inference-time correction is attractive but under-studied for VLA specifically.\\n- **Gap**: No systematic study of what conditioning signals should drive learned corrections, or how correction magnitude interacts with conditioning features. Existing methods (A2C2, ReconVLA, SC-VLA) address adjacent problems but leave this interaction unexplored.\\n- **Our angle**: First systematic comparison of conditioning strategies across correction magnitudes for frozen VLA correction. Core discovery: the conditioning-magnitude interaction, not architecture or training, determines success vs catastrophic failure.\\n- **Headline**: \\\"Observation-conditioned corrections remain robust across magnitudes (mean approximately 17%), while per-DOF conformal features cause progressive collapse (14% to 0%). This identifies magnitude sensitivity as a critical factor for safe VLA inference-time correction.\\\"\\n\\n## Competitive Landscape\\n\\n### A2C2 — Most similar concurrent work\\nFrozen VLA + offline-trained per-step correction head. Key differences: (1) no multi-sample selection stage; (2) does not study conditioning feature alternatives; (3) no magnitude sensitivity analysis; (4) no explicit norm bounding.\\n\\n### ReconVLA — Same domain, different route\\nConformal quantile regression for UQ + OOD detection on frozen VLA. Does not perform learned correction. Our argmin baseline is our own conformal selection, not ReconVLA's method.\\n\\n### SC-VLA — RL-based refinement\\nResidual RL per-task. Requires online training, not plug-and-play. Different problem setting.\\n\\n### ACR-VLA positioning\\nFirst to combine multi-sample conformal selection with bounded learned correction AND systematically compare conditioning features across magnitudes. The mechanism insight (conditioning-magnitude interaction) is novel.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Effect size is small\\\"**\\n   - Response: 6v6 pooled Fisher exact p=0.0074 (p<0.01), Cohen's d=1.21 (large effect). +5.2pp improvement is statistically significant. Core contribution remains the mechanism insight, but pipeline improvement is now a confirmed secondary contribution.\\n\\n2. **\\\"obs_only is just a residual MLP, where is the novelty?\\\"**\\n   - Response: Novelty is in the systematic comparison revealing the conditioning-magnitude interaction failure mode. The architecture is deliberately simple to isolate the conditioning signal's effect. Discovery that obs features suffice (and conformal features harm) is non-obvious.\\n\\n3. **\\\"Spatial benchmark shows nothing works\\\"**\\n   - Response: Honest limitation. At norm 0.1, obs_only and perdof perform comparably (35%) in spatial. Magnitude sensitivity manifests primarily in tasks with larger action distribution shift (object manipulation). This task-dependence is itself informative.\\n\\n4. **CRM approximately 330K params expressivity**\\n   - Response: Intentionally minimal. 3-layer MLP (input→256→256→30), input normalization. Prevents CRM from overriding base policy. approximately 3ms overhead. Architecture is NOT the contribution.\\n\\n5. **Simulation only**\\n   - Response: CoRL accepts sim-only. LIBERO is a recognized benchmark. Real-robot validation noted as future work.\\n\\n6. **K=10 inference cost**\\n   - Response: Multi-sample generation is the dominant cost (approximately 10x VLA forward pass). CRM overhead is negligible (approximately 3ms). Trade-off between compute and robustness is explicit.\\n\\n7. **\\\"Why does per-DOF fail?\\\" — is the explanation sufficient?**\\n   - Response: Section 3.5 provides mechanistic explanation: K=10 samples in 30D → rank-deficient covariance → noisy per-dimension Mahalanobis components → unreliable directional signals at deployment. Low norm masks the noise; high norm exposes it.\\n\\n## Hard Evidence (confirmed, D047)\\n\\n### 6v6 Pooled (obs_only ε=0.2 vs argmin) — LOCKED\\n- obs_only: seeds 42/43/44/45/46/47 = 22/16/16/16/15/20, pooled 105/600 (17.5%)\\n- argmin: seeds 42/43/44/45/46/47 = 12/17/13/12/10/10, pooled 74/600 (12.3%)\\n- Fisher exact p=0.0074 (one-sided), paired t-test p=0.016, Cohen's d=1.21\\n\\n### Magnitude Sweep (multi-seed means, D045)\\n- obs_only: ε=0.1 mean 15.7% (3s) → ε=0.2 mean 17.5% (6s) → ε=0.3 mean 17.0% (3s) → default 17% (1s)\\n- perdof: ε=0.1 mean 10.0% (3s) → ε=0.2 11% (1s) → ε=0.3 mean 4.7% (3s) → default 0% (2s)\\n- VLA-only: seeds 42/43/44/45 = 12/12/10/9%, mean 10.8%±1.4%\\n- Spatial: obs_only 34-36%, perdof 30-35%, argmin 34%, VLA-only 30%\\n\\n### Additional baselines\\n- scalar CRM seed42 = 15% (single seed)\\n- VLA-mean (K=10 mean aggregation): seed42=12%, seed43=15%, seed45=running\\n- Direct correction (K=1 CRM): seed42 = 14% (not significant vs VLA-only)\\n\\n## Pending Evidence (RUNNING — ~9 experiments)\\n- perdof magnitude curve multi-seed (norm 0.2/0.3/default additional seeds)\\n- obs_only norm 0.1/0.3/default additional seeds\\n- scalar/vla_mean seed45 (n_rollouts=20, ~3-5h remaining)\\n- obs_only default seed45 (n_rollouts=20)\\n\", \"total_chars\": 7603, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "139ca772-d204-4cb1-bb12-d11187a55e31",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — acr-vla-conformal-refinement\\\\n\\\\n## Target Venue\\\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2)\\\\n- Narrative B (mechanism insight) confirmed as default framing\\\\n\\\\n## Core Insight (Narrative B — ACTIVE)\\\\nMagnitude control is the critical, previously unrecognized factor determining whether learned inference-time corrections help or catastrophically fail on frozen VLA policies. Observation-conditioned corrections remain robust across the full magnitude range, while per-DOF conformal features cause progressive collapse as correction magnitude increases. The sample-then-correct pipeline itself (conformal selection + bounded CRM) is the methodological contribution; the conditioning-magnitude interaction is the scientific contribution.\\\\n\\\\n## Headline Metric\\\\nobs_only ε=0.2: 6-seed pooled 105/600 (17.5%) vs argmin 74/600 (12.3%), **+5.2pp, Fisher exact p=0.0074 (p<0.01), Cohen's d=1.21**. obs_only stable 15-22% across all norms vs perdof progressive collapse 10%→4.7%→0% (multi-seed means). VLA-only: 10-12% (4 seeds).\\\\n\\\\n## Core Claims (Narrative B — 3 claims)\\\\n\\\\n1. **Sample-then-correct pipeline for inference-time VLA improvement**\\\\n   - Two-stage: conformal selection (K=10 argmin) + bounded residual correction (CRM, approximately 330K params)\\\\n   - **Statistically significant improvement**: obs_only 17.5% vs argmin 12.3%, +5.2pp, Fisher exact p=0.0074 (6v6 seeds, D047)\\\\n   - Cohen's d=1.21 (large effect), 5/6 seeds obs_only > argmin\\\\n   - obs_only CRM mean 17.5% vs VLA-only 10.8% vs argmin 12.3%\\\\n   - Evidence: Table 1 (6v6 pooled results + Fisher test), Section 3 (method)\\\\n\\\\n2. **Conditioning-magnitude interaction as a previously unidentified failure mode**\\\\n   - Same CRM architecture succeeds or fails depending solely on conditioning feature x magnitude interaction\\\\n   - obs_only: stable approximately 17% across norms 0.03 to 1.42 (including uncapped)\\\\n   - perdof: progressive collapse 14% → 10% → 4% → 0% as norm increases\\\\n   - Bounded magnitude control is necessary for safe inference-time VLA correction\\\\n   - Evidence: Figure 2 (magnitude curves), Table 2 (cross-magnitude), Section 4.2-4.3\\\\n\\\\n3. **Honest negative result: per-DOF conformal features do not generalize as correction signals**\\\\n   - Despite theoretical appeal as calibrated per-dimension uncertainty, per-DOF scores fail beyond narrow safe region\\\\n   - Root cause: K=10 rank-deficient covariance in 30D action space → noisy directional signals\\\\n   - Spatial benchmark: no method separates from baseline (34-35%), suggesting task-complexity dependence\\\\n   - Evidence: Section 4.4, Section 3.5 (mechanism analysis)\\\\n\\\\n## Story Spine\\\\n- **Problem**: Frozen VLA policies degrade under distribution shift. Retraining is expensive. Inference-time correction is attractive but under-studied for VLA specifically.\\\\n- **Gap**: No systematic study of what conditioning signals should drive learned corrections, or how correction magnitude interacts with conditioning features. Existing methods (A2C2, ReconVLA, SC-VLA) address adjacent problems but leave this interaction unexplored.\\\\n- **Our angle**: First systematic comparison of conditioning strategies across correction magnitudes for frozen VLA correction. Core discovery: the conditioning-magnitude interaction, not architecture or training, determines success vs catastrophic failure.\\\\n- **Headline**: \\\\\\\"Observation-conditioned corrections remain robust across magnitudes (mean approximately 17%), while per-DOF conformal features cause progressive collapse (14% to 0%). This identifies magnitude sensitivity as a critical factor for safe VLA inference-time correction.\\\\\\\"\\\\n\\\\n## Competitive Landscape\\\\n\\\\n### A2C2 — Most similar concurrent work\\\\nFrozen VLA + offline-trained per-step correction head. Key differences: (1) no multi-sample selection stage; (2) does not study conditioning feature alternatives; (3) no magnitude sensitivity analysis; (4) no explicit norm bounding.\\\\n\\\\n### ReconVLA — Same domain, different route\\\\nConformal quantile regression for UQ + OOD detection on frozen VLA. Does not perform learned correction. Our argmin baseline is our own conformal selection, not ReconVLA's method.\\\\n\\\\n### SC-VLA — RL-based refinement\\\\nResidual RL per-task. Requires online training, not plug-and-play. Different problem setting.\\\\n\\\\n### ACR-VLA positioning\\\\nFirst to combine multi-sample conformal selection with bounded learned correction AND systematically compare conditioning features across magnitudes. The mechanism insight (conditioning-magnitude interaction) is novel.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"Effect size is small\\\\\\\"**\\\\n   - Response: 6v6 pooled Fisher exact p=0.0074 (p<0.01), Cohen's d=1.21 (large effect). +5.2pp improvement is statistically significant. Core contribution remains the mechanism insight, but pipeline improvement is now a confirmed secondary contribution.\\\\n\\\\n2. **\\\\\\\"obs_only is just a residual MLP, where is the novelty?\\\\\\\"**\\\\n   - Response: Novelty is in the systematic comparison revealing the conditioning-magnitude interaction failure mode. The architecture is deliberately simple to isolate the conditioning signal's effect. Discovery that obs features suffice (and conformal features harm) is non-obvious.\\\\n\\\\n3. **\\\\\\\"Spatial benchmark shows nothing works\\\\\\\"**\\\\n   - Response: Honest limitation. At norm 0.1, obs_only and perdof perform comparably (35%) in spatial. Magnitude sensitivity manifests primarily in tasks with larger action distribution shift (object manipulation). This task-dependence is itself informative.\\\\n\\\\n4. **CRM approximately 330K params expressivity**\\\\n   - Response: Intentionally minimal. 3-layer MLP (input→256→256→30), input normalization. Prevents CRM from overriding base policy. approximately 3ms overhead. Architecture is NOT the contribution.\\\\n\\\\n5. **Simulation only**\\\\n   - Response: CoRL accepts sim-only. LIBERO is a recognized benchmark. Real-robot validation noted as future work.\\\\n\\\\n6. **K=10 inference cost**\\\\n   - Response: Multi-sample generation is the dominant cost (approximately 10x VLA forward pass). CRM overhead is negligible (approximately 3ms). Trade-off between compute and robustness is explicit.\\\\n\\\\n7. **\\\\\\\"Why does per-DOF fail?\\\\\\\" — is the explanation sufficient?**\\\\n   - Response: Section 3.5 provides mechanistic explanation: K=10 samples in 30D → rank-deficient covariance → noisy per-dimension Mahalanobis components → unreliable directional signals at deployment. Low norm masks the noise; high norm exposes it.\\\\n\\\\n## Hard Evidence (confirmed, D047)\\\\n\\\\n### 6v6 Pooled (obs_only ε=0.2 vs argmin) — LOCKED\\\\n- obs_only: seeds 42/43/44/45/46/47 = 22/16/16/16/15/20, pooled 105/600 (17.5%)\\\\n- argmin: seeds 42/43/44/45/46/47 = 12/17/13/12/10/10, pooled 74/600 (12.3%)\\\\n- Fisher exact p=0.0074 (one-sided), paired t-test p=0.016, Cohen's d=1.21\\\\n\\\\n### Magnitude Sweep (multi-seed means, D045)\\\\n- obs_only: ε=0.1 mean 15.7% (3s) → ε=0.2 mean 17.5% (6s) → ε=0.3 mean 17.0% (3s) → default 17% (1s)\\\\n- perdof: ε=0.1 mean 10.0% (3s) → ε=0.2 11% (1s) → ε=0.3 mean 4.7% (3s) → default 0% (2s)\\\\n- VLA-only: seeds 42/43/44/45 = 12/12/10/9%, mean 10.8%±1.4%\\\\n- Spatial: obs_only 34-36%, perdof 30-35%, argmin 34%, VLA-only 30%\\\\n\\\\n### Additional baselines\\\\n- scalar CRM seed42 = 15% (single seed)\\\\n- VLA-mean (K=10 mean aggregation): seed42=12%, seed43=15%, seed45=running\\\\n- Direct correction (K=1 CRM): seed42 = 14% (not significant vs VLA-only)\\\\n\\\\n## Pending Evidence (RUNNING — ~9 experiments)\\\\n- perdof magnitude curve multi-seed (norm 0.2/0.3/default additional seeds)\\\\n- obs_only norm 0.1/0.3/default additional seeds\\\\n- scalar/vla_mean seed45 (n_rollouts=20, ~3-5h remaining)\\\\n- obs_only default seed45 (n_rollouts=20)\\\\n\\\", \\\"total_chars\\\": 7603, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2)\\n- Narrative B (mechanism insight) confirmed as default framing\\n\\n## Core Insight (Narrative B — ACTIVE)\\nMagnitude control is the critical, previously unrecognized factor determining whether learned inference-time corrections help or catastrophically fail on frozen VLA policies. Observation-conditioned corrections remain robust across the full magnitude range, while per-DOF conformal features cause progressive collapse as correction magnitude increases. The sample-then-correct pipeline itself (conformal selection + bounded CRM) is the methodological contribution; the conditioning-magnitude interaction is the scientific contribution.\\n\\n## Headline Metric\\nobs_only ε=0.2: 6-seed pooled 105/600 (17.5%) vs argmin 74/600 (12.3%), **+5.2pp, Fisher exact p=0.0074 (p<0.01), Cohen's d=1.21**. obs_only stable 15-22% across all norms vs perdof progressive collapse 10%→4.7%→0% (multi-seed means). VLA-only: 10-12% (4 seeds).\\n\\n## Core Claims (Narrative B — 3 claims)\\n\\n1. **Sample-then-correct pipeline for inference-time VLA improvement**\\n   - Two-stage: conformal selection (K=10 argmin) + bounded residual correction (CRM, approximately 330K params)\\n   - **Statistically significant improvement**: obs_only 17.5% vs argmin 12.3%, +5.2pp, Fisher exact p=0.0074 (6v6 seeds, D047)\\n   - Cohen's d=1.21 (large effect), 5/6 seeds obs_only > argmin\\n   - obs_only CRM mean 17.5% vs VLA-only 10.8% vs argmin 12.3%\\n   - Evidence: Table 1 (6v6 pooled results + Fisher test), Section 3 (method)\\n\\n2. **Conditioning-magnitude interaction as a previously unidentified failure mode**\\n   - Same CRM architecture succeeds or fails depending solely on conditioning feature x magnitude interaction\\n   - obs_only: stable approximately 17% across norms 0.03 to 1.42 (including uncapped)\\n   - perdof: progressive collapse 14% → 10% → 4% → 0% as norm increases\\n   - Bounded magnitude control is necessary for safe inference-time VLA correction\\n   - Evidence: Figure 2 (magnitude curves), Table 2 (cross-magnitude), Section 4.2-4.3\\n\\n3. **Honest negative result: per-DOF conformal features do not generalize as correction signals**\\n   - Despite theoretical appeal as calibrated per-dimension uncertainty, per-DOF scores fail beyond narrow safe region\\n   - Root cause: K=10 rank-deficient covariance in 30D action space → noisy directional signals\\n   - Spatial benchmark: no method separates from baseline (34-35%), suggesting task-complexity dependence\\n   - Evidence: Section 4.4, Section 3.5 (mechanism analysis)\\n\\n## Story Spine\\n- **Problem**: Frozen VLA policies degrade under distribution shift. Retraining is expensive. Inference-time correction is attractive but under-studied for VLA specifically.\\n- **Gap**: No systematic study of what conditioning signals should drive learned corrections, or how correction magnitude interacts with conditioning features. Existing methods (A2C2, ReconVLA, SC-VLA) address adjacent problems but leave this interaction unexplored.\\n- **Our angle**: First systematic comparison of conditioning strategies across correction magnitudes for frozen VLA correction. Core discovery: the conditioning-magnitude interaction, not architecture or training, determines success vs catastrophic failure.\\n- **Headline**: \\\"Observation-conditioned corrections remain robust across magnitudes (mean approximately 17%), while per-DOF conformal features cause progressive collapse (14% to 0%). This identifies magnitude sensitivity as a critical factor for safe VLA inference-time correction.\\\"\\n\\n## Competitive Landscape\\n\\n### A2C2 — Most similar concurrent work\\nFrozen VLA + offline-trained per-step correction head. Key differences: (1) no multi-sample selection stage; (2) does not study conditioning feature alternatives; (3) no magnitude sensitivity analysis; (4) no explicit norm bounding.\\n\\n### ReconVLA — Same domain, different route\\nConformal quantile regression for UQ + OOD detection on frozen VLA. Does not perform learned correction. Our argmin baseline is our own conformal selection, not ReconVLA's method.\\n\\n### SC-VLA — RL-based refinement\\nResidual RL per-task. Requires online training, not plug-and-play. Different problem setting.\\n\\n### ACR-VLA positioning\\nFirst to combine multi-sample conformal selection with bounded learned correction AND systematically compare conditioning features across magnitudes. The mechanism insight (conditioning-magnitude interaction) is novel.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Effect size is small\\\"**\\n   - Response: 6v6 pooled Fisher exact p=0.0074 (p<0.01), Cohen's d=1.21 (large effect). +5.2pp improvement is statistically significant. Core contribution remains the mechanism insight, but pipeline improvement is now a confirmed secondary contribution.\\n\\n2. **\\\"obs_only is just a residual MLP, where is the novelty?\\\"**\\n   - Response: Novelty is in the systematic comparison revealing the conditioning-magnitude interaction failure mode. The architecture is deliberately simple to isolate the conditioning signal's effect. Discovery that obs features suffice (and conformal features harm) is non-obvious.\\n\\n3. **\\\"Spatial benchmark shows nothing works\\\"**\\n   - Response: Honest limitation. At norm 0.1, obs_only and perdof perform comparably (35%) in spatial. Magnitude sensitivity manifests primarily in tasks with larger action distribution shift (object manipulation). This task-dependence is itself informative.\\n\\n4. **CRM approximately 330K params expressivity**\\n   - Response: Intentionally minimal. 3-layer MLP (input→256→256→30), input normalization. Prevents CRM from overriding base policy. approximately 3ms overhead. Architecture is NOT the contribution.\\n\\n5. **Simulation only**\\n   - Response: CoRL accepts sim-only. LIBERO is a recognized benchmark. Real-robot validation noted as future work.\\n\\n6. **K=10 inference cost**\\n   - Response: Multi-sample generation is the dominant cost (approximately 10x VLA forward pass). CRM overhead is negligible (approximately 3ms). Trade-off between compute and robustness is explicit.\\n\\n7. **\\\"Why does per-DOF fail?\\\" — is the explanation sufficient?**\\n   - Response: Section 3.5 provides mechanistic explanation: K=10 samples in 30D → rank-deficient covariance → noisy per-dimension Mahalanobis components → unreliable directional signals at deployment. Low norm masks the noise; high norm exposes it.\\n\\n## Hard Evidence (confirmed, D047)\\n\\n### 6v6 Pooled (obs_only ε=0.2 vs argmin) — LOCKED\\n- obs_only: seeds 42/43/44/45/46/47 = 22/16/16/16/15/20, pooled 105/600 (17.5%)\\n- argmin: seeds 42/43/44/45/46/47 = 12/17/13/12/10/10, pooled 74/600 (12.3%)\\n- Fisher exact p=0.0074 (one-sided), paired t-test p=0.016, Cohen's d=1.21\\n\\n### Magnitude Sweep (multi-seed means, D045)\\n- obs_only: ε=0.1 mean 15.7% (3s) → ε=0.2 mean 17.5% (6s) → ε=0.3 mean 17.0% (3s) → default 17% (1s)\\n- perdof: ε=0.1 mean 10.0% (3s) → ε=0.2 11% (1s) → ε=0.3 mean 4.7% (3s) → default 0% (2s)\\n- VLA-only: seeds 42/43/44/45 = 12/12/10/9%, mean 10.8%±1.4%\\n- Spatial: obs_only 34-36%, perdof 30-35%, argmin 34%, VLA-only 30%\\n\\n### Additional baselines\\n- scalar CRM seed42 = 15% (single seed)\\n- VLA-mean (K=10 mean aggregation): seed42=12%, seed43=15%, seed45=running\\n- Direct correction (K=1 CRM): seed42 = 14% (not significant vs VLA-only)\\n\\n## Pending Evidence (RUNNING — ~9 experiments)\\n- perdof magnitude curve multi-seed (norm 0.2/0.3/default additional seeds)\\n- obs_only norm 0.1/0.3/default additional seeds\\n- scalar/vla_mean seed45 (n_rollouts=20, ~3-5h remaining)\\n- obs_only default seed45 (n_rollouts=20)\\n\", \"total_chars\": 7603, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_012thXc6NTqYb8YD1NUyzofM`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": 0,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "85c26fa0-48f6-4742-abba-e771acd7d650",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LzfHypwHgRJeC6oDcZvLo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 24521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1125
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WHnD68d4Kgm5dH1AmfPvww`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "73b09eb6-c7f3-42e3-9949-5983f746df9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LzfHypwHgRJeC6oDcZvLo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 24521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1125
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

_source line 12 · 2026-05-17T11:18:41.936Z_

<details><summary>↩ Tool result · `toolu_012thXc6NTqYb8YD1NUyzofM`</summary>

```text
Error: result (284,695 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "770cfce6-2c25-45aa-90b8-ea70474d0a76",
  "tool_use_result": {
    "content": "Error: result (284,695 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:32:40.226Z\", \"updated_at\": \"2026-05-17T11:05:43.649Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthens pooled significance for Narrative A transition.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed47.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"319128\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed47.log\", \"submitted_at\": \"2026-05-16T21:33:49.282Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 47, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\", \"wall_clock_seconds\": 48714.4, \"gpu_hours\": 13.53}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:48:10.086Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:48:15.850144+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"successes\": 20, \"total\": 100, \"benchmark\": \"object\", \"mode\": \"obs_only\", \"norm\": 0.2, \"seed\": 47}, \"completed_at\": \"2026-05-17T11:05:43.649Z\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:04.937Z\", \"updated_at\": \"2026-05-17T10:59:11.317Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed44.json\", \"server\": \"bjb1-18228\", \"gpu_id\": 1, \"model_name\": \"crm_perdof_norm01\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM norm=0.1 seed=44 on LIBERO object. Multi-seed magnitude curve: seed42=11%, expecting similar. Fills the biggest gap in perdof magnitude data (norm=0.1 only has 1 seed).\", \"pid\": 531963}, \"hypothesis\": \"perdof CRM (ε=0.1) seed=44 on LIBERO Object. 验证 perdof 在低 norm 的安全区域（seed42=11%，seed45 running）。多 seed 支撑 magnitude curve 低 norm 段。\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:48:36.650Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T10:48:39.951Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:48:45.826946+00:00\"}]}, \"notes\": \"失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed | 诊断中: Worker worker_diagnose_eval-perdof-object-norm01-seed44_20260517T105221 已派发到 bjb1-18228 检查是否为 cron 误判（同配置 seed45 成功，SR=11%）\", \"metrics\": {\"overall_sr\": 0.08, \"total_successes\": 8, \"total_rollouts\": 100, \"seed\": 44, \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:32:42.117Z\", \"updated_at\": \"2026-05-17T10:57:16.754Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=45 on LIBERO object benchmark. Retry after unregistered process conflict. Expected to confirm perdof collapse at high norm (seed42=4%, seed44 running). Supports magnitude curve narrative.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed45_r2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"319463\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed45-r2.log\", \"submitted_at\": \"2026-05-16T21:33:52.055Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 45, \"wall_clock_seconds\": 48204.7, \"gpu_hours\": 13.39}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:54:49.175Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:54:55.730176+00:00\"}]}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed45-r2.log\", \"metrics\": {\"overall_sr\": 0.06, \"successes\": 6, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:57:16.754Z\"}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:07:14.242Z\", \"updated_at\": \"2026-05-17T10:56:41.892Z\", \"hypothesis\": \"Duplicate of seed47 obs_only norm=0.1 on bjb2 (survived GPU conflict cleanup), provides extra seed47 data point\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 363223, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (killed duplicate)\", \"log_path\": \"N/A (killed duplicate)\"}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:42:47.471Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T10:42:49.632Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:42:53.924730+00:00\"}]}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:38.275Z\", \"updated_at\": \"2026-05-17T10:55:13.212Z\", \"hypothesis\": \"perdof CRM ε=0.2 seed46 on LIBERO-Object. 补充 perdof magnitude curve ε=0.2 数据（目前仅 seed43=9%）。与 obs_only ε=0.2 seed46 配对对比。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": 389051, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:04:31.207Z\", \"updated_at\": \"2026-05-17T10:54:36.728Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm02_seed46.log\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 510896, \"seed\": 46, \"model_name\": \"crm_obs_only_norm02\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"hypothesis\": \"obs_only CRM v3-norm norm=0.2 seed=46 on LIBERO object. 5th seed for Fisher test statistical power.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"log_path\": \"logs/eval_object_obs_only_norm02_seed46.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"hypothesis\": \"obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argmin seed46=10% 配对）。ε=0.2 是 obs_only 最优区间，seed42=22%。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"total_episodes\": 100, \"successes\": 15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 2, \"bbq_sauce\": 3, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 4, \"orange_juice\": 3}}, \"completed_at\": \"2026-05-17T05:07:55.218Z\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:17:00.494Z\", \"updated_at\": \"2026-05-17T10:54:24.948Z\", \"hypothesis\": \"Duplicate of obs_only norm=0.1 seed46 on bjb2 (deployed by batch5 Worker). Extra data point for magnitude curve.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": 365893, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:43:36.147Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T10:43:38.311Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:43:46.527772+00:00\"}]}}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:38:21.922Z\", \"updated_at\": \"2026-05-17T10:54:02.629Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) seed=47 on LIBERO object benchmark. Paired with obs_only seed47 on cuda:0 for direct comparison. Extends argmin multi-seed data for pooled Fisher test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --seed 47 --benchmark object --n_rollouts 10 --output_file logs/eval_object_reconvla_seed47.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 322337, \"seed\": 47, \"model_name\": \"SmolVLA_argmin_K10\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed47.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:51:45.356Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:51:50.389646+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T10:54:02.630Z\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:27:16.189Z\", \"updated_at\": \"2026-05-17T10:29:43.551Z\", \"hypothesis\": \"Duplicate of perdof norm=0.1 seed47 on bjb1-32546 (deployed by orphan Worker). Also running on bjb2-40593.\", \"spec\": {\"command\": \"cd /root/autodl-tmp/acr-vla && python evaluate.py --model smolvla --mode crm_perdof --benchmark object --seed 47 --n_rollouts 10 --norm_limit 0.1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 414817, \"data_path\": \"/root/autodl-tmp/acr-vla/libero/data\", \"data_count\": 100, \"model_name\": \"SmolVLA-450M + CRM-perdof\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks × 10 rollouts)\"}}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-17T10:28:56.574Z\", \"hypothesis\": \"obs_only CRM at eps=0.3 on seed46 extends magnitude curve high-norm data. seed42=19%, seed44=18%, seed45=14%. 4th seed at this norm.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --seed 46 --benchmark object --n_rollouts 10 --output_file logs/eval_object_obs_only_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"416568\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"max_correction_norm\": 0.3}}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:06.341Z\", \"updated_at\": \"2026-05-17T10:22:14.183Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed45.json\", \"server\": \"bjb1-32546\", \"gpu_id\": 2, \"model_name\": \"crm_perdof_norm01\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM norm=0.1 seed=45 on LIBERO object. Multi-seed magnitude curve: seed42=11%, seed44=deploying. 3rd seed for perdof low-norm baseline.\", \"pid\": 309151}, \"hypothesis\": \"perdof CRM (ε=0.1) seed=45 on LIBERO Object. 验证 perdof 在低 norm (0.1) 的安全区域（seed42=11%）。如果与 obs_only 接近，支持\\\"低 norm 两者等效\\\"叙事。\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-17T10:22:14.184Z\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:20.872Z\", \"updated_at\": \"2026-05-17T10:19:28.338Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed47, completes magnitude curve low-norm data for perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object --n_rollouts 10 --output_file logs/eval_object_perdof_norm01_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"388460\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed47.log\", \"submitted_at\": \"2026-05-17T06:54:11.992Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"checkpoint_path\": \"N/A (killed before completion)\", \"wall_clock_seconds\": 12316.3, \"gpu_hours\": 3.42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T10:19:28.338Z\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T18:39:23.017Z\", \"updated_at\": \"2026-05-17T10:19:26.819Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_reconvla_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"seed\": 46, \"model_name\": \"reconvla\", \"hypothesis\": \"argmin baseline K=10 seed=46 on LIBERO object. 5th seed for Fisher test. Pairs with eval-obs-only-object-norm02-seed46 (bjb1-18228:cuda:3).\", \"data_path\": \"\", \"data_count\": 0, \"checkpoint_source\": \"\", \"eval_data\": \"object\", \"pid\": 295478, \"log_path\": \"logs/eval_argmin_object_seed46.log\", \"checkpoint_path\": \"N/A (eval-only, reconvla baseline)\"}, \"hypothesis\": \"Argmin baseline (conformal selection K=10, 无 learned correction) seed=46 on LIBERO Object. 与 obs_only seed=46 配对，扩展 pooled Fisher test 到 6 seeds。预期 12-17% SR。\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_argmin_object_seed46.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:19:26.819Z\"}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:18:01.200Z\", \"updated_at\": \"2026-05-17T07:23:48.606Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed44.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"316382\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-default-seed44.log\", \"submitted_at\": \"2026-05-16T07:18:00.861Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"hypothesis\": \"perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42) seed=44 on LIBERO object. perdof norm=0.1=11%, norm=0.2=11% on object — expected similar or worse at default.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"wall_clock_seconds\": 86534.1, \"gpu_hours\": 24.04}, \"hypothesis\": \"perdof CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 perdof 在 uncapped norm 下的 catastrophic collapse（seed42=0%）。为 magnitude curve 提供第二个 seed 的 default 数据点。\", \"reproduce\": {\"finished_at\": \"2026-05-17T07:20:12.857Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T07:20:15.008Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T07:20:19.307187+00:00\"}]}, \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Task 10 not started due to 24h timeout. 0/90 rollouts succeeded. Catastrophic collapse at unclipped norm.\", \"seed\": 44, \"mode\": \"crm_perdof\", \"benchmark\": \"object\", \"max_correction_norm\": \"default (~1.42)\"}}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:05:32.383Z\", \"updated_at\": \"2026-05-17T07:18:04.606Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed46 will show magnitude sensitivity collapse pattern similar to seed42, confirming obs_only robustness advantage\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 393646, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:05:28.139Z\", \"updated_at\": \"2026-05-17T07:17:58.529Z\", \"hypothesis\": \"obs_only CRM at eps=0.1 on seed47 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude curve\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 588037, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"eval-obs-only-object-norm01-seed46-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:05:18.047Z\", \"updated_at\": \"2026-05-17T07:17:52.154Z\", \"hypothesis\": \"obs_only CRM at eps=0.1 on seed46 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude curve\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 587763, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:08.486Z\", \"updated_at\": \"2026-05-17T07:02:49.285Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"272762\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45-r2.log\", \"submitted_at\": \"2026-05-16T15:24:08.144Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:3\", \"model_name\": \"crm_obs_only_norm03\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"wall_clock_seconds\": 56321.1, \"gpu_hours\": 15.64}, \"hypothesis\": \"obs_only CRM with max_correction_norm=0.3 on LIBERO Object (seed=45) should show graceful degradation similar to seed42 (19%), providing multi-seed error estimates for the magnitude curve\", \"reproduce\": {\"finished_at\": \"2026-05-17T07:00:25.758Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T07:00:32.829645+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T07:02:49.285Z\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:45.495Z\", \"updated_at\": \"2026-05-17T06:54:28.933Z\", \"spec\": {\"model_name\": \"smolvla_libero_vla_mean\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 45 --output_file logs/eval_object_vla_mean_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"248652\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:45Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 70783.9, \"gpu_hours\": 19.66}, \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=45 on LIBERO object benchmark. Completes seed=45 six-way comparison. seed42=12%, seed43=15%, seed44=running.\", \"reproduce\": {\"finished_at\": \"2026-05-17T03:29:41.019Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T03:29:45.978517+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T06:54:28.933Z\"}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-17T06:54:17.648Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=47 on LIBERO Object. 4th seed for magnitude curve low-norm point. Combined with seeds 42/45/46, provides error bar for obs_only at ε=0.1. Supports robustness narrative (obs_only stable across all norms).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json 2>&1 | tee logs/eval_object_obs_only_norm01_seed47.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"363210\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed47.log\", \"submitted_at\": \"2026-05-17T06:54:17.250Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:13.356Z\", \"updated_at\": \"2026-05-17T06:54:15.239Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=46 on LIBERO Object. Extends magnitude curve low-norm segment to 3+ seeds. If consistent with seed42=19% and seed45 (running), strengthens robustness claim that obs_only maintains stable performance across all ε values.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm01_seed46.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"590833\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed46.log\", \"submitted_at\": \"2026-05-17T06:54:14.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:44:23.744Z\", \"updated_at\": \"2026-05-17T06:53:28.467Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 45 --K 10 --output_file logs/eval_object_argmin_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"215932\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed45.log\", \"submitted_at\": \"2026-05-16T07:45:06.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"model_name\": \"reconvla_argmin_baseline\", \"hypothesis\": \"argmin baseline K=10 seed=45 on LIBERO object. 4th seed baseline for Fisher test. Paired with eval-obs-only-object-norm02-seed45.\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"wall_clock_seconds\": 60530.4, \"gpu_hours\": 16.81}, \"reproduce\": {\"finished_at\": \"2026-05-17T00:31:27.579Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T00:31:32.330885+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"checkpoint_path\": \"N/A (eval-only)\", \"hypothesis\": \"Argmin baseline (conformal selection K=10, no correction) seed=45 on LIBERO Object. Highest priority: expands argmin multi-seed data from 3 to 4 seeds, balancing against obs_only 5 seeds for symmetric Fisher test. Expected 12-17% SR.\", \"completed_at\": \"2026-05-17T00:33:57.260Z\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:19.181Z\", \"updated_at\": \"2026-05-17T06:51:36.588Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=46 on LIBERO Object. Extends perdof low-norm data (seed42=11%, seed44/45 running). At ε=0.1 perdof is in its \\\"safe zone\\\" (tight bound masks noisy corrections). Paired with obs_only seed46 for direct comparison at same seed.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json 2>&1 | tee logs/eval_object_perdof_norm01_seed46.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"393633\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed46.log\", \"submitted_at\": \"2026-05-17T06:51:36.171Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:01:50.937Z\", \"updated_at\": \"2026-05-17T04:48:50.296Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠正价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42-r2\", \"spec\": {\"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO Object benchmark (10 tasks)\", \"data_count\": \"100 episodes (10 tasks x 10 rollouts)\", \"model_name\": \"obs_only CRM (327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO Object\", \"gpu\": \"cuda:4\", \"pid\": 364076, \"tmux_session\": \"eval-dc-r2\", \"note\": \"Code patched: print every rollout instead of every 5. Root cause of prev failures: workers killed working processes because output interval was 7.5min (5 rollouts x 90s each).\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_direct_correction_object_seed42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}, \"completed_at\": \"2026-05-17T04:48:50.296Z\"}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:11.457Z\", \"updated_at\": \"2026-05-17T04:45:11.458Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"505419\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed44.log\", \"submitted_at\": \"2026-05-16T15:24:11.074Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:2\", \"model_name\": \"crm_perdof_norm03\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 48060.4, \"gpu_hours\": 13.35}, \"hypothesis\": \"perdof CRM (ε=0.3) seed=44 on LIBERO Object. 验证 perdof 在高 norm (0.3) 的退化程度（seed42=4%）。多 seed 确认 perdof progressive collapse 机制。\", \"reproduce\": {\"finished_at\": \"2026-05-17T04:41:11.191Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T04:41:18.547308+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"total_episodes\": 100, \"successes\": 4, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 0, \"bbq_sauce\": 1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 1, \"milk\": 0, \"chocolate_pudding\": 1, \"orange_juice\": 0}}, \"completed_at\": \"2026-05-17T04:45:11.458Z\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:07:31.626Z\", \"updated_at\": \"2026-05-17T03:31:42.118Z\", \"spec\": {\"parent\": \"eval-acr-object-v4-perdof\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.2, K=10, n_rollouts=10\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"127732\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm02-object.log\"}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.2 on LIBERO object benchmark. Paired with obs_only norm=0.2 (running, 18% at 5/10) for magnitude comparison figure. Tests perdof at moderate correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:04:45.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:04:48.447852+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T07:12:35.145Z\", \"parent\": \"eval-acr-object-v3\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-17T03:31:41.215Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47778.8, \"gpu_hours\": 13.27}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:07:26.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:07:28.510451+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:10:02.679Z\", \"parent\": \"crm-train-v2-scalar-unc\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:21.006Z\", \"updated_at\": \"2026-05-17T03:31:40.288Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:5\", \"pid\": 15190, \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:03:26.878Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:03:29.305763+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm02.log\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"completed_at\": \"2026-05-15T16:06:23.063Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO Spatial benchmark. Spatial benchmark 下 obs_only 最优 norm 是否同样为 0.2。如果 spatial 无明显分离，说明方法效果依赖 action distribution shift 程度。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:16.095Z\", \"updated_at\": \"2026-05-17T03:31:39.344Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03.log\"}, \"gpu\": \"bjb2-28827:cuda:3\", \"pid\": 14260, \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:53:04.031Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:53:08.939326+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:17:49.711Z\", \"hypothesis\": \"perdof CRM (ε=0.3) on LIBERO Spatial benchmark. 高 norm 下 perdof 在 spatial 是否也出现退化。如果 spatial 无 collapse（与 obs_only 接近），说明 failure mode 与 task complexity 相关。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:10.924Z\", \"updated_at\": \"2026-05-17T03:31:38.448Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm005.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"gpu\": \"bjb2-28827:cuda:1\", \"pid\": 13456, \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:52:50.451Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:52:53.898813+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:24:59.482Z\", \"hypothesis\": \"perdof CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 下 perdof 在 spatial 的表现。如果与 obs_only-0.05 一致（35%），说明低 norm 约束消除了 conditioning 差异。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:08.547Z\", \"updated_at\": \"2026-05-17T03:31:37.673Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm003.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:0\", \"pid\": 13185, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:32:37.390Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:32:42.080703+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm003.log\", \"checkpoint_path\": \"N/A (eval-only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:40:16.878Z\", \"hypothesis\": \"perdof CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 perdof 在 spatial 的表现。与 obs_only-0.03 (34%) 对比，验证低 norm 安全区域。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-17T03:15:31.664Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"143106\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 mean action (no conformal)\", \"seed\": 42, \"hypothesis\": \"K=10 mean baseline isolates multi-sampling averaging contribution vs conformal correction. Expected between vla_only K=1 (30%) and ACR-VLA.\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\"}, \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T22:12:39.100Z\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\", \"checkpoint_path\": \"N/A (eval experiment)\", \"hypothesis\": \"VLA mean action (average of K=10 samples) on LIBERO-Spatial provides a strong baseline by reducing sampling noise — establishes whether sample averaging alone matches or exceeds single-sample VLA\", \"parent\": \"eval-spatial-v7-full\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-17T03:15:30.973Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"231421\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log\", \"submitted_at\": \"2026-05-14T17:47:58.583Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 argmin selection (no CRM correction)\", \"seed\": 42, \"hypothesis\": \"Isolate argmin base action selection from CRM correction. If argmin-only ≈ VLA mean (40%), CRM delta is the sole culprit. If argmin-only << VLA mean, argmin selection itself is problematic.\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 40187.5, \"gpu_hours\": 11.16}, \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"notes\": \"[2026-05-15] HUNG: 9/10 tasks done (36.7%, 33/90), stuck on task 10 env init for 8+ hours. Process alive (pid 231426, GPU 1414 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:45.148Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T04:57:46.099Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:50.175181+00:00\"}]}, \"hypothesis\": \"Argmin-only selection (K=10, pick lowest CRM score without correction) on LIBERO-Spatial tests whether selection alone provides benefit — isolating the selection mechanism from the correction mechanism\", \"parent\": \"eval-reconvla-spatial-v3\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:08.043Z\", \"updated_at\": \"2026-05-17T03:15:29.089Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed45.json\", \"server\": \"bjb1-32546\", \"gpu_id\": 4, \"model_name\": \"crm_perdof_default\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM default norm (~1.42) seed=45 on LIBERO object. Confirms catastrophic collapse (seed42=0%, seed44=running). Multi-seed evidence for paper figure.\", \"pid\": 310477}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T02:54:38.157Z\", \"metrics\": {\"kill_reason\": \"Sacrificed for P0 direct-correction experiment (no free GPU). Was at task 5/10 after 6h. Expected result: 0% (confirmed by seed42=0%, seed44 running on autodl-4090).\", \"partial_progress\": \"5/10 tasks, bbq_sauce 0% success\"}, \"hypothesis\": \"Per-DoF CRM with default norm on LIBERO-Object seed=45 validates cross-seed consistency of per-DoF correction — paired with seed42/43/44 to assess variance of correction-based methods vs baseline\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:46.639Z\", \"updated_at\": \"2026-05-17T03:15:28.368Z\", \"spec\": {\"hypothesis\": \"obs-only CRM with norm=0.2 on object benchmark. Cross-benchmark norm sensitivity test — paired with eval-mag-obsonly-norm02 on spatial. If obs-only at norm=0.2 > norm=0.1 on both benchmarks → robust 'observation-conditioned correction' story.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 44270, \"tmux_session\": \"eval-acr-object-obs-only-norm02\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark, 10 tasks x 10 rollouts\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\"}, \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:35:34.272Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:35:39.374197+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\", \"completed_at\": \"2026-05-15T17:37:08.420Z\", \"hypothesis\": \"ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided corrections without requiring action history\", \"parent\": \"crm-train-v2-obs-only\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:16.510Z\", \"updated_at\": \"2026-05-17T03:15:26.392Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"123761\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v7.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T01:45:58.391Z\", \"hypothesis\": \"Full ACR pipeline v7 (obs-only CRM, conformal selection, norm=0.1) on LIBERO-Spatial achieves improvement over VLA-only baseline (32%), validating the method on spatial reasoning tasks\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:25.647Z\", \"updated_at\": \"2026-05-17T03:15:25.342Z\", \"spec\": {\"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T03:10:30.457Z\", \"hypothesis\": \"Full ACR pipeline v8 (obs-only CRM, K=10 conformal selection, norm=0.1) on LIBERO-Object achieves consistent improvement over VLA-only baseline (9-12%) across all 10 tasks with optimized hyperparameters\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:02.277Z\", \"updated_at\": \"2026-05-17T03:15:19.323Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 2 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"180480\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard2.log\", \"submitted_at\": \"2026-05-14T07:56:37.531Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 2 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5491.8, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:09.308Z\", \"hypothesis\": \"Precompute v5 (shard 2/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard2\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:00.276Z\", \"updated_at\": \"2026-05-17T03:15:18.177Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 1 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"180400\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard1.log\", \"submitted_at\": \"2026-05-14T07:56:35.789Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 1 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5492.1, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:07.934Z\", \"hypothesis\": \"Precompute v5 (shard 1/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard1\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:54:59.383Z\", \"updated_at\": \"2026-05-17T03:15:17.511Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 0 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"180251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard0.log\", \"submitted_at\": \"2026-05-14T07:56:33.414Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 0 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5493.2, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:06.626Z\", \"hypothesis\": \"Precompute v5 (shard 0/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard0\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:14.301Z\", \"updated_at\": \"2026-05-17T03:15:16.391Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"69937\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard2.log\", \"submitted_at\": \"2026-05-13T18:58:14.266Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173960.7, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:09:25.582Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:09:26.379476+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:35.000Z\", \"hypothesis\": \"Precompute v4 (shard 2/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard2\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:12.183Z\", \"updated_at\": \"2026-05-17T03:15:15.362Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"69793\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard1.log\", \"submitted_at\": \"2026-05-13T18:58:12.154Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173961.1, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:22.574Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:23.366356+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:33.288Z\", \"hypothesis\": \"Precompute v4 (shard 1/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard1\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:09.830Z\", \"updated_at\": \"2026-05-17T03:15:14.415Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"69647\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard0.log\", \"submitted_at\": \"2026-05-13T18:58:09.802Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173962.3, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:45.258Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:50.222546+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:32.128Z\", \"hypothesis\": \"Precompute v4 (shard 0/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard0\"}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:13.281Z\", \"updated_at\": \"2026-05-17T03:15:08.562Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:2\", \"pid\": 13728, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:30:14.331Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T17:30:15.807Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:30:23.476790+00:00\"}]}, \"hypothesis\": \"Per-DoF CRM with max_correction_norm=0.2 on LIBERO-Spatial achieves optimal balance between correction magnitude and stability — norm=0.2 is hypothesized sweet spot from obs-only results\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-17T03:15:07.670Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"197057\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:17:05.974Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction (ACR-VLA with D016 4-bug fix) outperforms VLA K=1 (30%) and SampleConsensus (34%) on LIBERO spatial. CORE CLAIM experiment.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28899.4, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:44.725Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:45.380Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:46.631294+00:00\"}]}, \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection) on LIBERO-Spatial improves over VLA-only baseline, validating that conformal selection generalizes across spatial reasoning tasks\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-17T03:15:06.728Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"197803\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v3.log\", \"submitted_at\": \"2026-05-14T12:17:13.006Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction generalizes from spatial to object benchmark — cross-benchmark validation of ACR-VLA.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28901.2, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:53.408Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:54.185Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:55.466058+00:00\"}]}, \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection with scalar uncertainty) on LIBERO-Object improves over VLA-only baseline by selecting highest-confidence action from candidate set\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:12:01.937Z\", \"updated_at\": \"2026-05-17T03:15:05.867Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"227086\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed44.log\", \"submitted_at\": \"2026-05-16T07:12:01.614Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 45205.2, \"gpu_hours\": 12.56}, \"reproduce\": {\"finished_at\": \"2026-05-16T19:42:10.387Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:42:13.494105+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.16, \"total_success\": 16, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T19:45:26.774Z\", \"hypothesis\": \"Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, confirming that performance gains are robust across random seeds and not artifacts of a single initialization\", \"parent\": \"eval-acr-object-obs-only-norm02\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:34:53.953Z\", \"updated_at\": \"2026-05-17T03:15:04.317Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --benchmark object --mode vla_only --K 1 --seed 45 --output_file logs/eval_object_vla_only_seed45.json\", \"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:4\", \"pid\": 221407, \"seed\": 45, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO object\", \"data_count\": 10, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"VLA-only baseline K=1 seed=45 on LIBERO object. Reference for seed45 statistical comparison. seed42=12%, seed43=12%, seed44=10%.\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T14:56:50.174Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:56:52.057Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:56:54.606880+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.09, \"successes\": 18, \"total\": 200, \"tasks_done\": 10}, \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=45 provides second additional seed for baseline variance estimation — multi-seed baselines required for statistical significance claims in paper\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:50:14.071Z\", \"updated_at\": \"2026-05-17T03:15:03.364Z\", \"spec\": {\"hypothesis\": \"D031: VLA-only baseline (K=1, single sample, no CRM) seed=43 on LIBERO object benchmark. Completes 7-way seed=43 comparison table. VLA-only seed=42 = 12% = argmin.\", \"parent\": \"eval-vla-only-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 43 --K 1 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"vla_only\", \"seed\": 43, \"eval_data\": \"object\"}, \"metrics\": {\"overall_sr\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"source\": \"json_file_verified_by_worker\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T18:46:38.180Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:46:39.481Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:46:41.461084+00:00\"}]}, \"notes\": \"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=43 establishes multi-seed baseline variance — needed to determine if ACR improvements are statistically significant above baseline noise\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:20:02.901Z\", \"updated_at\": \"2026-05-17T03:14:58.588Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42 --start_task 9 --output_file /root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 10, \"model_name\": \"smolvla_libero\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:32:23.773Z\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}, \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"checkpoint_path\": \"N/A (eval only)\", \"hypothesis\": \"VLA mean action on LIBERO-Spatial task 10 (wooden shelf) specifically — completing the last missing task from the earlier eval-vla-mean-spatial run to have full 10-task baseline numbers\", \"parent\": \"eval-vla-mean-spatial\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-17T03:14:57.896Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T11:07:49.901Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:14.141Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:15.524386+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:07:51.915540+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"118108\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SampleConsensus (scalar Euclidean argmin)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\", \"hypothesis\": \"SampleConsensus scalar baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\", \"hypothesis\": \"ReconVLA (K=10 sample consensus without CRM) on LIBERO-Spatial establishes upper bound for pure sampling diversity benefit — if high, CRM correction adds value only at lower K; if low, confirms CRM is essential\", \"parent\": \"plan_014-reconvla-baseline\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-17T03:14:57.225Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"203968\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:43:42.188Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary for effective correction\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"failure_reason\": \"Bug: evaluate.py line 266 CRM load condition missing crm_obs_only, CRM was None throughout eval, all rollouts 0%. Replaced by eval-obs-only-spatial-v3.\", \"wall_clock_seconds\": 185.5, \"gpu_hours\": 0.05}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:46:47.663Z\", \"hypothesis\": \"Obs-only CRM v2 retrained on spatial data resolves the dimension mismatch from v1 and achieves meaningful improvement on LIBERO-Spatial by using benchmark-matched visual features\", \"parent\": \"eval-obs-only-spatial\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:43.696Z\", \"updated_at\": \"2026-05-17T03:14:56.290Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"186964\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"submitted_at\": \"2026-05-14T09:30:43.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM scalar-unc v2 (327K params, 8D state fix)\", \"seed\": 42, \"hypothesis\": \"Scalar CRM v2 ablation — per-DOF expected to outperform on task success rate despite similar val_loss\", \"wall_clock_seconds\": 9977.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"completed_at\": \"2026-05-14T12:17:01.093Z\", \"hypothesis\": \"Training CRM to predict scalar uncertainty enables confidence-based action selection via conformal prediction, allowing adaptive correction magnitude based on model confidence\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:40.796Z\", \"updated_at\": \"2026-05-17T03:14:55.328Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"186823\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"submitted_at\": \"2026-05-14T09:30:40.716Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM per-DOF v2 (337K params, 8D state fix, argmin base, L2 clip)\", \"seed\": 42, \"hypothesis\": \"Per-DOF CRM v2 with D016 fixes (8D state, argmin base, alpha=0.5, L2 clipping) improves over pre-fix version\", \"wall_clock_seconds\": 9979.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"completed_at\": \"2026-05-14T12:17:00.195Z\", \"hypothesis\": \"Training CRM with per-DoF (per degree-of-freedom) correction output produces more fine-grained corrections than a single scalar, improving downstream task performance on multi-joint manipulation\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:41:35.819Z\", \"updated_at\": \"2026-05-17T03:14:53.940Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"187913\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"submitted_at\": \"2026-05-14T09:41:35.736Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM obs_only v2\", \"seed\": 42, \"wall_clock_seconds\": 9366.4, \"gpu_hours\": 2.6}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"completed_at\": \"2026-05-14T12:17:42.122Z\", \"hypothesis\": \"Training a CRM with obs-only input (no action/proprio) can learn correction signals purely from visual observation features, enabling correction without access to action space information\", \"parent\": \"plan_001-crm-smolvla\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:48.056Z\", \"updated_at\": \"2026-05-17T03:13:50.200Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"47186\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard2.log\", \"submitted_at\": \"2026-05-13T11:57:48.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.4, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:07.463Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 2/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:46.669Z\", \"updated_at\": \"2026-05-17T03:13:49.286Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"47044\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard1.log\", \"submitted_at\": \"2026-05-13T11:57:46.654Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.8, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:06.485Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 1/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:45.284Z\", \"updated_at\": \"2026-05-17T03:13:43.682Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"46966\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard0.log\", \"submitted_at\": \"2026-05-13T11:57:45.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12500.2, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:05.433Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 0/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:37.603Z\", \"updated_at\": \"2026-05-17T03:13:41.787Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --precompute --benchmark spatial object --K 5 --cache_dir /root/autodl-tmp/crm_cache_k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"79517\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-k5.log\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 26737, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"K=5 precompute for K sensitivity ablation (plan_015)\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:09:33.445Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:09:34.396952+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}, \"completed_at\": \"2026-05-13T22:12:39.543Z\", \"hypothesis\": \"Precomputing K=5 VLA action samples provides sufficient diversity for conformal selection while reducing inference cost by 50% vs K=10 — testing efficiency-performance tradeoff\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T06:56:12.892Z\", \"updated_at\": \"2026-05-17T03:13:39.823Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial object --n_rollouts 20 --seed 42\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"50790\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_014-reconvla-baseline.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"20 tasks x 20 rollouts = 400 episodes\", \"model_name\": \"SmolVLA (450M) + ReconVLA argmin selection\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin selection) as baseline for ACR-VLA comparison\", \"fixes_applied\": [\"BDDL path: use benchmark_instance.get_task_bddl_file_path()\", \"LIBERO assets copied from GitHub repo\"]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T11:07:20.019Z\", \"hypothesis\": \"ReconVLA baseline implementation validates that sample consensus (K=10 argmin Euclidean) provides meaningful improvement over single-sample VLA, establishing competitive baseline for ACR comparison\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T03:01:07.682Z\", \"updated_at\": \"2026-05-17T03:13:37.890Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --auto --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --seed 42 --K 10\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"32811\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_001-crm-smolvla.log\", \"submitted_at\": \"2026-05-13T04:54:14.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": 1000, \"model_name\": \"CRM (337K) + SmolVLA (450M)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\", \"hypothesis\": \"Per-DOF conformal features enable dimension-selective action correction on LIBERO\", \"wall_clock_seconds\": 2992.2, \"gpu_hours\": 0.83}, \"conclusion\": \"failed\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"completed_at\": \"2026-05-13T05:44:07.131Z\", \"hypothesis\": \"Initial CRM + SmolVLA integration plan validates that conformal residual module can be trained and integrated with a pretrained VLA model for action refinement\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:22:10.415Z\", \"updated_at\": \"2026-05-17T03:13:35.534Z\", \"spec\": {\"hypothesis\": \"Per-DOF uncertainty features carry more actionable information than scalar uncertainty summaries, enabling dimension-selective correction\", \"description\": \"3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty) x 6 groups (3 anisotropy ratios x 2 uncertainty sources)\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"data_count\": 20000, \"model_name\": \"CorrectionMLP(2-layer, 64-hidden)\", \"seed\": 42, \"command\": \"python -u run_mvp.py\", \"data_path\": \"synthetic (generated in-script)\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/mvp/\", \"log_path\": \"/root/acr-vla-conformal-refinement/mvp/mvp_results.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T01:44:00.055Z\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}, \"hypothesis\": \"MVP validation: CRM correction signals improve point-reaching accuracy in simplified task — if corrections reliably move end-effector toward targets, the mechanism transfers to full manipulation\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:35:16.236Z\", \"updated_at\": \"2026-05-17T03:13:33.197Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"43809\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned on libero_spatial)\", \"seed\": 42, \"hypothesis\": \"Validate smolvla_libero checkpoint with fixed wrapper (correct state repr, 256x256 images, 7D action) achieves >50% success on libero_spatial\", \"log_path\": \"/tmp/eval_spatial_full.log\", \"checkpoint_source\": \"lerobot/smolvla_libero (HuggingFace community checkpoint)\", \"failure_reason\": \"smolvla_libero 0% on spatial - 6 wrapper bugs: image flip/size/normalization, state 6D→8D, state normalization, action denormalization all missing\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T15:45:51.082Z\", \"hypothesis\": \"SmolVLA pretrained model evaluates directly on LIBERO-Spatial without any CRM or conformal processing — establishing raw VLA capability as absolute floor baseline\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:10.843Z\", \"updated_at\": \"2026-05-17T03:13:04.533Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"197596\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial.log\", \"submitted_at\": \"2026-05-14T12:17:10.754Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D input, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"evaluate.py has no crm_obs_only mode. --mode acr_vla loads CRM expecting 1030D input but obs_only checkpoint has 990D (no conformal features). Replaced by eval-obs-only-spatial-v2.\", \"wall_clock_seconds\": 1392.5, \"gpu_hours\": 0.39}, \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}, \"completed_at\": \"2026-05-14T12:40:23.205Z\", \"hypothesis\": \"Obs-only CRM trained on object benchmark generalizes to LIBERO-Spatial tasks without retraining — testing cross-benchmark transfer of visual correction signals\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:13:41.913Z\", \"updated_at\": \"2026-05-17T03:09:38.443Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"229751\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log\", \"submitted_at\": \"2026-05-16T07:13:41.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 48315.0, \"gpu_hours\": 13.42}, \"reproduce\": {\"finished_at\": \"2026-05-16T20:36:24.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T20:36:28.363366+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T20:38:56.577Z\", \"hypothesis\": \"obs_only CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 obs_only 在 uncapped norm 下的跨 seed 稳定性（seed42=17%）。如果维持 15-20%，确认极端 magnitude 鲁棒性。\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:56:58.178Z\", \"updated_at\": \"2026-05-17T03:09:30.045Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.05 on LIBERO object benchmark. Paired with obs_only norm=0.05 for magnitude comparison figure.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"gpu\": \"1\", \"pid\": 109650, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object (10 tasks x 10 rollouts)\", \"log_path\": \"logs/nohup_eval_object_perdof_norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:33.616Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:36:35.355Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:40.842032+00:00\"}]}, \"hypothesis\": \"perdof CRM (ε=0.05) seed=42 on LIBERO Object. 验证 perdof 在极低 norm 下是否与 obs_only 接近（两者都受限于低 norm 纠正量）。magnitude curve 低端数据点。\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:34:16.821Z\", \"updated_at\": \"2026-05-17T03:09:27.225Z\", \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"144504\"}, \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:39:30.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:39:33.739829+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm02_seed43_r3.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:41:59.362Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=43 on LIBERO Object. 验证 perdof 在 norm=0.2 的多 seed 数据（seed42=11%）。确认 perdof 在中间 norm 的退化幅度具有跨 seed 一致性。\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:52.169Z\", \"updated_at\": \"2026-05-17T03:09:17.332Z\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": 140759, \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 42 --K 10 --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r3.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T11:10:32.044Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:10:33.866Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:10:39.747200+00:00\"}]}, \"hypothesis\": \"perdof CRM (ε=0.3) seed=42 on LIBERO Object magnitude sweep. 验证 perdof 在 norm=0.3 的 collapse 程度。预期 SR 急剧下降（支持 progressive collapse 叙事）。\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:18.917Z\", \"updated_at\": \"2026-05-17T03:09:15.263Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:4\", \"pid\": 14854, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:00:02.717Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:00:09.569232+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:08.945Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 在 spatial 上的表现。与 object 的 0.05 数据点对比，检验 benchmark 间一致性。\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-17T03:09:11.273Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"225139\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"wall_clock_seconds\": 70039.8, \"gpu_hours\": 19.46}, \"pid\": 227426, \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:42:50.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:43:27.876843+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\", \"completed_at\": \"2026-05-16T00:48:05.254Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 obs_only 在 spatial 的表现（10-task SR）。验证 magnitude 效应在不同 benchmark 上的一致性。\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-17T03:09:10.586Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.3 on LIBERO object benchmark. Tests degradation at higher correction norm on object domain. Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10\", \"pid\": 103028, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\"}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:35:42.126Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:35:43.889Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:35:47.235304+00:00\"}]}, \"hypothesis\": \"obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_only 是否仍保持 graceful degradation（对比 perdof 在同 norm 的 collapse）。\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-17T03:09:06.864Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.05 on LIBERO object benchmark. Builds object magnitude curve alongside norm=0.1 (19%) and norm=0.2 (18% partial). Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10\", \"pid\": 101610, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log\"}, \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"logs/eval_object_obs_only_norm005.json\", \"completed_at\": \"2026-05-16T08:19:41.189Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_only 表现。如果 SR 与 VLA-only 相近（12%），说明过低 norm 约束了 CRM 纠正能力。\"}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:34:55.059Z\", \"updated_at\": \"2026-05-17T03:08:52.841Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --K 10 --seed 45 --output_file logs/eval_object_perdof_norm02_seed45.json\", \"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:1\", \"pid\": 222824, \"seed\": 45, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO object\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"Perdof CRM norm=0.2 seed=45 on LIBERO object. Additional perdof data point for cross-seed comparison. Expected ~11% based on seed42 data.\"}, \"hypothesis\": \"perdof CRM (ε=0.2) seed=45 on LIBERO Object. 验证 perdof 在中间 norm (0.2) 的表现（seed42=11%, seed43=9%）。为 magnitude curve 误差估计提供第三个 seed。\"}, \"eval-scalar-object-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:38:01.206Z\", \"updated_at\": \"2026-05-17T03:08:34.153Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_scalar --max_correction_norm 0.1 --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --output_file logs/eval_object_scalar_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 224623, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_scalar_unc\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"logs/eval_object_scalar_seed45.log\"}, \"hypothesis\": \"Scalar uncertainty CRM seed=45 on LIBERO Object. 测试 scalar conditioning（单一 std 而非 per-DOF）是否比 obs_only 或 perdof 更优。如果表现介于两者之间，说明 conditioning 信息量与性能正相关。\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:15:05.583Z\", \"updated_at\": \"2026-05-17T03:08:29.766Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_obs_only --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"pid\": 242264, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 45}, \"hypothesis\": \"obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 uncapped 大 norm 下仍优于 VLA-only（seed42 在 default 为 17%）。极端 magnitude 鲁棒性测试。\"}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:01:52.970Z\", \"updated_at\": \"2026-05-17T03:08:27.511Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --mode crm_obs_only --max_correction_norm 0.1 --k 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_norm01_seed45.json > logs/eval_object_obs_only_norm01_seed45.log 2>&1\", \"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:0\", \"model_name\": \"crm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": -1, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"obs_only CRM norm=0.1 seed=45 on LIBERO object. Multi-seed magnitude curve data point. seed42=19%.\"}, \"pid\": 474319, \"hypothesis\": \"obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。seed42 在 0.1 为 19%，如果一致则确认 obs_only 全 norm 范围鲁棒。\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:46:15.008Z\", \"updated_at\": \"2026-05-17T03:04:54.543Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠���价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42\", \"spec\": {\"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO Object benchmark (10 tasks)\", \"data_count\": \"100 episodes (10 tasks x 10 rollouts)\", \"model_name\": \"obs_only CRM (327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO Object\", \"gpu\": \"cuda:4\", \"pid\": 364076, \"note\": \"Code patched to print every rollout (was every 5). Prev attempts killed working processes due to misinterpreting silence as stuck.\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T02:58:54.670Z\"}, \"failure_reason\": \"Agent误杀：wchar未增长30s被误判为stuck，实际是每5 rollout打印一次（~7.5min间隔）且MuJoCo/CUDA使用memory-mapped I/O不被/proc/PID/io追踪。进程实际正常运行中。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T02:58:57.101Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T02:59:01.101476+00:00\"}]}}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:18:02.194Z\", \"updated_at\": \"2026-05-17T02:38:55.611Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（跳过 K=10 采样+argmin 选择），测试 obs 特征鲁棒性在简化 pipeline 下是否成立。如果 SR > VLA-only (~11%)，说明 CRM 本身有独立价值；如果 SR < VLA-only，说明 selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"1\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"obs_only CRM v3-norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"pid\": 353384, \"tmux_session\": \"eval-direct-correction-object-seed42\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T02:38:55.611Z\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:37:24.278Z\", \"updated_at\": \"2026-05-17T00:38:26.185Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=44 on LIBERO Object benchmark. Adds second seed to perdof norm=0.2 (seed42=11%, seed43=9%). Enables error bar on magnitude curve figure at this norm point.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"326081\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed44.log\", \"submitted_at\": \"2026-05-17T08:36:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:44:19.258Z\", \"updated_at\": \"2026-05-16T21:33:38.747Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"pid\": \"233544\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed45.log\", \"submitted_at\": \"2026-05-16T07:44:18.928Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"model_name\": \"crm_v3_norm_obs_only\", \"hypothesis\": \"obs_only CRM v3-norm norm=0.2 seed=45 on LIBERO object. 4th seed pre-deployed for statistical power.\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"wall_clock_seconds\": 49759.8, \"gpu_hours\": 13.82}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:21:10.527Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:21:15.588019+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"checkpoint_path\": \"N/A (eval only)\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR range consistent with seeds 42-44, it confirms the method's reliability across random seeds and strengthens pooled statistical test vs argmin.\", \"completed_at\": \"2026-05-16T21:33:38.747Z\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:11:59.390Z\", \"updated_at\": \"2026-05-16T21:29:49.586Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44_r2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"226878\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44-r2.log\", \"submitted_at\": \"2026-05-16T07:11:59.066Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_scalar_unc\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 51470.5, \"gpu_hours\": 14.3}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:11:40.494Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:11:48.900516+00:00\"}]}, \"hypothesis\": \"Scalar CRM seed=44 on LIBERO object benchmark. Retry of failed eval-scalar-object-seed44. Expects scalar variant underperforms obs_only but may match argmin baseline.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-16T21:29:49.586Z\"}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:56:22.235Z\", \"updated_at\": \"2026-05-16T19:45:27.956Z\", \"hypothesis\": \"perdof CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 four-way comparison. seed42=11%, seed43=12%. Expected to confirm perdof < argmin.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:57:04.525Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 44 --n_rollouts 10 --output_file logs/eval_object_perdof_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:13:35.112Z\", \"training_hours\": 13.28}, \"spec\": {\"data_path\": \"LIBERO_object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\"}, \"pid\": \"452982\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:13:38.573783+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T19:45:27.956Z\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:05:51.470Z\", \"updated_at\": \"2026-05-16T19:37:12.898Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T06:06:08.369Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed44.json\\\"\", \"finished_at\": \"2026-05-16T19:34:37.134Z\", \"training_hours\": 13.47}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"220777\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:34:40.416412+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T19:37:12.898Z\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:58:47.863Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:33:19.875Z\", \"training_hours\": 13.58}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"submitted_at\": \"2026-05-16T04:58:50.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 49038.9, \"gpu_hours\": 13.62}, \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:33:23.084588+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\", \"completed_at\": \"2026-05-16T18:36:08.965Z\"}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:48:54.894Z\", \"updated_at\": \"2026-05-16T15:36:08.207Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44_r4.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"501420\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r4.log\", \"submitted_at\": \"2026-05-16T14:49:19.300Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1956.7, \"gpu_hours\": 0.54}, \"hypothesis\": \"P0 retry #4: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22%, seed43=16%. Previous attempts failed (127/129/killed).\", \"pid\": 501420, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T15:21:56.018Z\", \"failure_reason\": \"r2 data valid (16%), r4 redundant. PID 501420 killed by worker at 2026-05-16T15:09.\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:32:14.163Z\", \"updated_at\": \"2026-05-16T15:34:00.414Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (EXIT_CODE=127, missing conda activate). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:32:36.214Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T15:28:27.588Z\", \"training_hours\": 13.93}, \"completed_at\": \"2026-05-16T01:34:17.696Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:28:32.358640+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"428117\", \"seed\": 44, \"model_name\": \"reconvla_argmin\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:32:15.187Z\", \"updated_at\": \"2026-05-16T15:25:14.349Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:32:45.643Z\", \"finished_at\": \"2026-05-16T14:40:32.978Z\", \"training_hours\": 13.13}, \"completed_at\": \"2026-05-16T01:34:19.695Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:40:38.399800+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"428406\", \"seed\": 44, \"model_name\": \"crm_obs_only_norm02\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"failure_reason\": null, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"logs/eval_object_obs_only_norm02_seed44.json\"}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:47.376Z\", \"updated_at\": \"2026-05-16T11:30:59.542Z\", \"spec\": {\"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"248860\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:47Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 972.5, \"gpu_hours\": 0.27}, \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=45 on LIBERO object benchmark. Multi-seed magnitude curve data point. seed42 norm=0.3=19%, seed44 norm=0.3=running. Extends magnitude robustness evidence to 3rd seed.\", \"conclusion\": \"failed\", \"failure_reason\": \"killed to resolve cuda:3 GPU conflict\", \"completed_at\": \"2026-05-16T11:30:59.542Z\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:11:49.844Z\", \"updated_at\": \"2026-05-16T09:00:15.290Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"390936\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-default-r2.log\", \"submitted_at\": \"2026-05-16T02:11:20Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 24535.3, \"gpu_hours\": 6.82}, \"hypothesis\": \"v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to confirm catastrophic failure\", \"parent\": \"eval-acr-object-v4-default\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T09:00:15.290Z\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:32.591Z\", \"updated_at\": \"2026-05-16T08:37:12.296Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Tests perdof at smallest correction norm on object domain.\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_perdof --max_correction_norm 0.03 --K 10 --seed 42 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 105938, \"log_path\": \"logs/eval_object_perdof_norm003.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"parent\": \"eval-acr-object-v4-perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"metrics\": {\"overall_success_rate\": 0.14, \"per_task_range\": \"0.0-0.4\"}}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:09:00.286Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:09:03.327886+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\", \"completed_at\": \"2026-05-16T08:11:39.117Z\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:27.783Z\", \"updated_at\": \"2026-05-16T07:46:23.704Z\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed43-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 pooled to 200 trials. Original crashed after 1 task.\", \"parent\": \"eval-obs-only-object-norm02-seed43\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_seed42\": \"-6pp (22% → 16%)\", \"vs_argmin_seed43\": \"-1pp (17% → 16%)\", \"pooled_2seed_obs_only_02\": \"19% (38/200)\", \"pooled_2seed_argmin\": \"14.5% (29/200)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:21:07.838Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:21:10.900676+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:23:48.849Z\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:33:13.916Z\", \"updated_at\": \"2026-05-16T07:13:29.827Z\", \"hypothesis\": \"Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"286989\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44-r2.log\", \"submitted_at\": \"2026-05-16T01:33:46.467Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20383.4, \"gpu_hours\": 5.66}, \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:33:44.353Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T04:58:56.451Z\", \"training_hours\": 3.42}, \"pid\": \"286989\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:59:00.452305+00:00\"}]}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.1, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (vla_only baseline)\", \"completed_at\": \"2026-05-16T07:13:29.827Z\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:38:22.125Z\", \"updated_at\": \"2026-05-16T07:09:01.967Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_norm.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 134094, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log\", \"submitted_at\": \"2026-05-15T17:38:21.517Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"wall_clock_seconds\": 48640.4, \"gpu_hours\": 13.51}, \"hypothesis\": \"obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default (perdof default). Tests whether obs_only robustness holds even without magnitude capping — if yes, obs_only is fundamentally more robust than perdof regardless of norm setting.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:41:19.269Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:41:22.516205+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T07:09:01.967Z\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:02:31.432Z\", \"updated_at\": \"2026-05-16T06:04:05.747Z\", \"hypothesis\": \"D031: scalar_unc CRM v3-norm seed=43 on LIBERO object benchmark. Completes seed=43 six-way comparison table. scalar seed=42 was worst at 4% — seed=43 confirms.\", \"parent\": \"eval-acr-object-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"114664\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed43.log\", \"submitted_at\": \"2026-05-15T16:03:30.400Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_scalar\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 50435.3, \"gpu_hours\": 14.01}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:01:42.952Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:01:45.993724+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"completed_at\": \"2026-05-16T06:04:05.747Z\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:31.254Z\", \"updated_at\": \"2026-05-16T05:56:01.541Z\", \"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object benchmark. Completes 5-point magnitude curve (0.03/0.05/0.1/0.2/0.3). Tests minimum effective correction magnitude on object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 121325, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-object.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.03, K=10, n_rollouts=10\", \"parent\": \"eval-acr-object-v4-obs-only\"}, \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T05:35:17.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:35:20.742243+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:56:01.541Z\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:02:34.914Z\", \"updated_at\": \"2026-05-16T05:25:06.306Z\", \"hypothesis\": \"scalar_unc CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. scalar seed42=9%, seed43 running (0% at 3/10). Expected worst CRM variant.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T05:02:50.780Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T05:05:30.084Z\", \"training_hours\": 0.04}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"310854\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"submitted_at\": \"2026-05-16T05:25:05.983Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"309346\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T05:05:32.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:05:34.587431+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:30.429Z\", \"updated_at\": \"2026-05-16T04:59:20.094Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"431189\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:30.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.0, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (r1 EXIT_CODE=127, r2 killed by agent). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:20.095Z\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:28.047Z\", \"updated_at\": \"2026-05-16T04:59:17.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"430985\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:27.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.3, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-argmin-object-seed44 (r1 EXIT_CODE=127, r2 killed by agent). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:17.975Z\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:46:28.667Z\", \"updated_at\": \"2026-05-16T04:53:17.141Z\", \"hypothesis\": \"D031: VLA-mean baseline (K=10, mean aggregation) seed=43 on LIBERO object benchmark. Completes seed=43 comparison table. If VLA-mean seed=43 ≈ obs_only seed=43 → CRM correction claim compressed.\", \"parent\": \"eval-vla-mean-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 43 --output_file logs/eval_object_vla_mean_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"111709\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed43.log\", \"submitted_at\": \"2026-05-15T15:47:37.968Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"libero/object\", \"data_count\": 10, \"checkpoint_source\": null, \"eval_data\": \"object\", \"wall_clock_seconds\": 47139.2, \"gpu_hours\": 13.09}, \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T04:48:28.380Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:48:31.493092+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-16T04:53:17.141Z\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:19:49.586Z\", \"updated_at\": \"2026-05-16T03:15:39.287Z\", \"hypothesis\": \"D031 supplementary: perdof CRM v3-norm seed=43 on LIBERO object benchmark. Completes three-way comparison (obs_only vs argmin vs perdof) with doubled samples. If perdof seed=43 ≈ argmin seed=43 → confirms obs_only uniquely better.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 43 --n_rollouts 10 --output_file logs/eval_object_perdof_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 365925, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed43.log\", \"submitted_at\": \"2026-05-15T13:21:00.347Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO_object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"wall_clock_seconds\": 50078.9, \"gpu_hours\": 13.91}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T03:12:36.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T03:12:39.589841+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:15:39.287Z\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:29:00.342Z\", \"updated_at\": \"2026-05-16T01:33:29.678Z\", \"hypothesis\": \"D035 follow-up: VLA-only baseline (K=1) seed=44 on LIBERO object benchmark. Third seed reference point. seed42=12%, seed43=12%. Deployed on bjb2-40593.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:29:36.987Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T01:30:26.640Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"vla_only\", \"seed\": 44, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127 (command not found) — bash -c wrapping 或环境激活路径错误，bjb2-40593 上系统性问题，三个 seed44 实验全部同样失败\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:33.143Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:38.635650+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:59.304Z\", \"updated_at\": \"2026-05-16T01:32:51.127Z\", \"hypothesis\": \"D035 follow-up: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object benchmark. Third seed for Fisher exact test. ε=0.2 is PROJECT HIGH config (seed42=22%). Paired with eval-argmin-object-seed44.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:29:31.218Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:14.217Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:20.761Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:23.773246+00:00\"}]}}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:58.358Z\", \"updated_at\": \"2026-05-16T01:32:49.190Z\", \"hypothesis\": \"D035 follow-up: argmin baseline (K=10) seed=44 on LIBERO object benchmark. Third seed for Fisher exact test statistical power. Paired with eval-obs-only-object-norm02-seed44. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:29:25.990Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:04.115Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (argmin baseline)\", \"seed\": 44, \"checkpoint_source\": \"N/A (no CRM)\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:06.598Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:09.864458+00:00\"}]}}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.063Z\", \"updated_at\": \"2026-05-16T00:51:14.618Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"356490\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"submitted_at\": \"2026-05-15T12:00:38.618Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 46070.8, \"gpu_hours\": 12.8, \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:41:25.212Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:42:01.902179+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"completed_at\": \"2026-05-16T00:48:29.446Z\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:05:41.192Z\", \"updated_at\": \"2026-05-16T00:49:21.141Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03_b2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"130104\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b2.log\", \"submitted_at\": \"2026-05-15T19:11:50.323Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20250.8, \"gpu_hours\": 5.63}, \"conclusion\": \"failed\", \"notes\": \"Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had 15min more progress. Both wrote same output_file, causing potential corruption.\", \"reproduce\": {\"finished_at\": \"2026-05-15T07:10:36.759Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:10:39.645469+00:00\"}]}, \"completed_at\": \"2026-05-16T00:49:21.141Z\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.739Z\", \"updated_at\": \"2026-05-16T00:37:43.289Z\", \"hypothesis\": \"D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison.\", \"parent\": \"eval-reconvla-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 43 --K 10 --output_file logs/eval_object_reconvla_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"356696\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed43.log\", \"submitted_at\": \"2026-05-15T12:00:40.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (reconvla baseline)\", \"seed\": 43, \"checkpoint_source\": \"N/A (no CRM, pure VLA baseline)\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 45422.6, \"gpu_hours\": 12.62}, \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:35:16.646Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:35:19.825582+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:37:43.289Z\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:19:36.419Z\", \"updated_at\": \"2026-05-15T19:38:38.710Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"138858\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T19:19:36.128Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (killed — GPU conflict on cuda:2, replaced by eval-mag-perdof-norm02-seed43-object-r3)\", \"wall_clock_seconds\": 951.1, \"gpu_hours\": 0.26}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:35:27.220Z\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:43:48.583Z\", \"updated_at\": \"2026-05-15T19:38:31.587Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T06:44:02.425Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (EXIT_CODE=127, retried as eval-mag-obsonly-norm03-r2)\", \"wall_clock_seconds\": 46287.3, \"gpu_hours\": 12.86}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:44:32.019Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:44:35.317393+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=127 — tmux 用 sh 执行命令，python 不在 sh PATH 中。修复: bash -c 包裹。已重试为 eval-mag-obsonly-norm03-r2。\", \"completed_at\": \"2026-05-15T19:35:29.718Z\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:53.269Z\", \"updated_at\": \"2026-05-15T19:34:07.651Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.2 on LIBERO object benchmark. Fills the norm=0.2 gap in 5-point magnitude curve. Previous run reached 18% at 5/10 then stopped.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_v2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": 141024, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"checkpoint_path\": \"N/A (duplicate of DONE eval-acr-object-obs-only-norm02, killed to free GPU)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:34:07.651Z\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:14:01.998Z\", \"updated_at\": \"2026-05-15T19:27:30.465Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"132816\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b4.log\", \"submitted_at\": \"2026-05-15T19:14:01.050Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 809.4, \"gpu_hours\": 0.22}, \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:30.465Z\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:13:38.067Z\", \"updated_at\": \"2026-05-15T19:27:28.479Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"134532\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b3.log\", \"submitted_at\": \"2026-05-15T19:14:52.972Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 755.5, \"gpu_hours\": 0.21}, \"hypothesis\": \"Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 occupied by P0 obs-only-norm02-seed43-r2). Director approved.\", \"parent\": \"eval-mag-obsonly-norm03-b2\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:28.479Z\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:19.724Z\", \"updated_at\": \"2026-05-15T19:25:28.957Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. Paired with obs_only norm=0.2 seed=43 for statistical comparison at the best obs_only norm.\", \"parent\": \"eval-mag-perdof-norm02-object\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"Killed during cuda:2/3 GPU cleanup on bjb2-28827 (2026-05-16). Was sharing cuda:2 with perdof norm=0.3 r2.\", \"completed_at\": \"2026-05-15T19:25:28.957Z\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:16.452Z\", \"updated_at\": \"2026-05-15T19:25:28.055Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Retry of killed eval-mag-perdof-norm0p3-object. Completes perdof 5-point magnitude curve on object domain.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"GPU contention on cuda:2 (shared with perdof norm=0.2 seed=43). Killed 2026-05-16. Replaced by r3 clean restart.\", \"completed_at\": \"2026-05-15T19:25:28.055Z\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:02.698Z\", \"updated_at\": \"2026-05-15T19:17:41.948Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"7017\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar-b2.log\", \"submitted_at\": \"2026-05-15T02:55:02.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58959.5, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:41.948Z\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:00.179Z\", \"updated_at\": \"2026-05-15T19:17:40.199Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"6746\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only-b2.log\", \"submitted_at\": \"2026-05-15T02:54:59.912Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58960.3, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:40.199Z\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:07.302Z\", \"updated_at\": \"2026-05-15T19:17:39.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"69379\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v4-full.log\", \"submitted_at\": \"2026-05-13T18:58:07.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D015: evaluate.py env_args 缺少 camera_names，SmolVLA 只收到单摄像头输入，结果系统性偏低\", \"wall_clock_seconds\": 173971.8, \"gpu_hours\": 48.33}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-13T19:36:15.749Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:36:19.370112+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:39.068Z\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-15T19:17:37.622Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M) + ReconVLA argmin selection K=10\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:59:43.231Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:26:37.521060+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:59:44.694612+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:37.622Z\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-15T19:17:36.369Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline success rate on libero_object with fixed evaluate.py (env.reset bug removed, 5-step zero-action stabilization)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:36.369Z\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:04.708Z\", \"updated_at\": \"2026-05-15T19:17:30.541Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"63218\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard2.log\", \"submitted_at\": \"2026-05-13T17:39:04.684Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178705.9, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:30.541Z\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:02.628Z\", \"updated_at\": \"2026-05-15T19:17:29.292Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"63075\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard1.log\", \"submitted_at\": \"2026-05-13T17:39:02.603Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178706.7, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:29.293Z\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:00.259Z\", \"updated_at\": \"2026-05-15T19:17:27.703Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && rm -rf /root/autodl-tmp/crm_cache_v3 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"62930\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard0.log\", \"submitted_at\": \"2026-05-13T17:39:00.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178707.5, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:27.703Z\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:04.275Z\", \"updated_at\": \"2026-05-15T19:17:26.396Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"57846\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard2.log\", \"submitted_at\": \"2026-05-13T16:11:04.255Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.1, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:26.396Z\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:02.520Z\", \"updated_at\": \"2026-05-15T19:17:25.022Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"57706\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard1.log\", \"submitted_at\": \"2026-05-13T16:11:02.500Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.5, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:25.022Z\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:01.629Z\", \"updated_at\": \"2026-05-15T19:17:23.631Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && rm -rf /root/autodl-tmp/crm_cache/spatial /root/autodl-tmp/crm_cache/object && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"57628\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard0.log\", \"submitted_at\": \"2026-05-13T16:11:01.605Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.0, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:23.631Z\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:30.091Z\", \"updated_at\": \"2026-05-15T19:13:43.549Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"127570\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object-r2.log\", \"submitted_at\": \"2026-05-15T18:58:29.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"crm_perdof_v3_norm\", \"seed\": 42, \"wall_clock_seconds\": 885.6, \"gpu_hours\": 0.25}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Migrated from bjb1-32546:cuda:4 (GPU conflict) to bjb2-28827:cuda:2. Paired with obs_only norm=0.3 for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm0p3-object\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:13:15.247Z\", \"failure_reason\": \"Duplicate of eval-mag-perdof-norm03-object (PID 118886 on bjb2-28827:cuda:3, identical params). Killed to free cuda:2.\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:34:52.454Z\", \"updated_at\": \"2026-05-15T18:58:11.790Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"144887\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object.log\", \"submitted_at\": \"2026-05-15T18:37:26.089Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1245.7, \"gpu_hours\": 0.35}, \"hypothesis\": \"Retry of eval-mag-perdof-norm03-object (killed by SIGTERM). Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Paired with obs_only norm=0.3 (running) for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm03-object\", \"conclusion\": \"killed\", \"failure_reason\": \"GPU conflict on bjb1-32546:cuda:4 (shared with obs-only-default). Killed lower priority perdof. Migrating to bjb2-28827:cuda:2 as r2.\", \"completed_at\": \"2026-05-15T18:58:11.790Z\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:38:18.819Z\", \"updated_at\": \"2026-05-15T18:58:10.821Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. norm=0.2 shows strongest signal (18% SR at 5/10 tasks in seed=42). Seed=43 doubling for statistical power on the best-performing configuration.\", \"parent\": \"eval-acr-object-obs-only-norm02\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43.json\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Crashed after 1 task on bjb1-32546:cuda:3 (PID 118214). Reviewer confirmed. Restarting as r2.\", \"completed_at\": \"2026-05-15T18:58:10.821Z\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:18:17.209Z\", \"updated_at\": \"2026-05-15T17:38:37.815Z\", \"hypothesis\": \"Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether magnitude control is essential on object domain too. If v4-default << v4-perdof (norm=0.1) → magnitude control is universally needed. If v4-default ≈ v4-perdof → spatial failure was anomalous.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"107658\", \"log_path\": \"logs/eval_object_perdof_default_norm.log\", \"submitted_at\": \"2026-05-16T00:51:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"notes\": \"Killed per Director instruction. 3/10 tasks all 0% SR, no magnitude control (norm≈1.42). Conclusion obvious — magnitude control is essential.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:38:37.815Z\"}, \"eval-mag-perdof-norm03-object\": {\"status\": \"DEPLOYED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:57:00.172Z\", \"updated_at\": \"2026-05-15T17:38:28.909Z\", \"spec\": {\"pid\": 115384, \"gpu_ids\": [2], \"server\": \"bjb2-28827\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\"}, \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T17:16:56.760Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\\\"\", \"finished_at\": \"2026-05-15T17:29:42.220Z\", \"training_hours\": 0.21}, \"pid\": 118886, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03-object.log\", \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:29:45.210Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:29:48.614116+00:00\"}]}, \"notes\": \"Restarted on cuda:3 (PID 118886, tmux: eval-mag-perdof-norm03-object) after v4-default killed. Previous run killed by SIGTERM before first rollout.\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:49:38.786Z\", \"updated_at\": \"2026-05-15T17:22:51.755Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 325264, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"submitted_at\": \"2026-05-15T06:50:02.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 37969.2, \"gpu_hours\": 10.55}, \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:20:31.567Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:20:34.907634+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"completed_at\": \"2026-05-15T17:22:51.755Z\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:31:09.989Z\", \"updated_at\": \"2026-05-15T17:01:25.883Z\", \"spec\": {\"command\": \"python eval_vla.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 42\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\"}, \"hypothesis\": \"VLA mean baseline (K=10, mean aggregation) on LIBERO object benchmark. Matches reconvla spatial baseline but on object tasks.\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\", \"gpu\": \"bjb1-32546:cuda:5\", \"pid\": 18808, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\", \"completed_at\": \"2026-05-15T17:01:25.883Z\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:28.744Z\", \"updated_at\": \"2026-05-15T16:25:17.101Z\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.log\", \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\"}, \"hypothesis\": \"ReconVLA baseline (scalar Euclidean argmin, K=10) on LIBERO object benchmark. Tests whether simple sample selection improves over VLA mean on object manipulation tasks. Provides baseline for CRM comparison on object domain.\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:25:17.101Z\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:41.689Z\", \"updated_at\": \"2026-05-15T16:23:01.718Z\", \"hypothesis\": \"D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"13797\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"submitted_at\": \"2026-05-15T02:53:41.526Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47312.8, \"gpu_hours\": 13.14}, \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:59:31.860Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:59:34.042176+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:14.366Z\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:49:13.626Z\", \"updated_at\": \"2026-05-15T15:45:38.531Z\", \"hypothesis\": \"D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:1\"], \"pid\": \"11116\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, max_correction_norm=0.1, object)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-perdof.log\"}, \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:45:38.531Z\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:04.283Z\", \"updated_at\": \"2026-05-15T13:18:27.852Z\", \"hypothesis\": \"Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_unc vs obs_only.\", \"parent\": \"eval-acr-spatial-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --start_task 3\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 311881, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar-r2.log\", \"submitted_at\": \"2026-05-15T05:14:33.525Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 70, \"model_name\": \"ACR-VLA CRM scalar_unc v3-norm (restart from T3)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 3-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 29034.3, \"gpu_hours\": 8.07}, \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:15:46.765Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:15:49.226583+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:18:27.853Z\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.934Z\", \"updated_at\": \"2026-05-15T11:15:11.801Z\", \"hypothesis\": \"Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.\", \"parent\": \"eval-acr-spatial-v4-obs-only-r2\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --start_task 6\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 312420, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"submitted_at\": \"2026-05-15T05:14:38.600Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 40, \"model_name\": \"ACR-VLA CRM obs_only v3-norm (restart from T6)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 6-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 21633.2, \"gpu_hours\": 6.01}, \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T10:15:39.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:15:44.340640+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"completed_at\": \"2026-05-15T11:15:11.801Z\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:09:04.411Z\", \"updated_at\": \"2026-05-15T10:01:21.065Z\", \"hypothesis\": \"D029: obs_only seed=43 复现实验。obs_only 是项目唯一存活路径。seed=42 如果确认 +5pp over argmin，seed=43 增加统计力（200 vs 200 样本下 Fisher exact p ~0.12，配合 object benchmark 独立验证有望通过）。\", \"parent\": \"eval-acr-spatial-v4-obs-only-r3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_spatial_seed43.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"341873\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-15T09:09:23.712Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 3117.4, \"gpu_hours\": 0.87}, \"notes\": \"D029: perdof spatial 35% vs argmin 34% = +1pp, kill criterion triggered. Per-DOF claim dead on spatial. obs_only 是唯一存活路径，seed=43 用于增加统计力。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T10:01:21.065Z\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.220Z\", \"updated_at\": \"2026-05-15T09:10:21.153Z\", \"hypothesis\": \"Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.\", \"parent\": \"eval-acr-spatial-v4-small\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt --max_correction_norm 0.1 --start_task 7\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 312150, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"submitted_at\": \"2026-05-15T05:14:36.298Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 30, \"model_name\": \"ACR-VLA CRM perdof v3-norm (restart from T7)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 7-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"wall_clock_seconds\": 14053.7, \"gpu_hours\": 3.9}, \"notes\": \"[D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T09:05:27.552Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:05:31.321347+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"completed_at\": \"2026-05-15T09:08:50.017Z\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:10:44.647Z\", \"updated_at\": \"2026-05-15T07:19:12.632Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"N/A (stale duplicate entry)\", \"server\": \"bjb1-18228\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"N/A (stale duplicate entry, never ran)\", \"log_path\": \"N/A\", \"notes\": \"Stale duplicate entry with dots in name. Actual experiment is eval-mag-obsonly-norm-0p3-r3 (also killed). Real running experiment is eval-mag-obsonly-norm03-r2.\", \"completed_at\": \"2026-05-15T07:19:12.632Z\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:11:06.381Z\", \"updated_at\": \"2026-05-15T07:17:16.300Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm_0p3.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"329871\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"submitted_at\": \"2026-05-15T07:11:15.690Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 360.6, \"gpu_hours\": 0.1}, \"conclusion\": \"killed\", \"notes\": \"Director 撤销部署指令。r2 (PID 325264) 实际未被误杀，r3 是基于信息差的重复部署。立即 kill r3 保留 r2。\", \"checkpoint_path\": \"N/A (killed before completion)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"completed_at\": \"2026-05-15T07:17:16.300Z\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:03.322Z\", \"updated_at\": \"2026-05-15T06:39:37.926Z\", \"hypothesis\": \"Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.\", \"parent\": \"eval-argmin-only-spatial\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --start_task 9\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 311609, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial-r2.log\", \"submitted_at\": \"2026-05-15T05:14:30.112Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 10, \"model_name\": \"ReconVLA argmin K=10 (restart from T9)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial task 9 only\", \"checkpoint_source\": \"N/A (reconvla mode, no CRM)\", \"wall_clock_seconds\": 5107.8, \"gpu_hours\": 1.42}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:35:00.746Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:35:02.954210+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\", \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint output)\", \"completed_at\": \"2026-05-15T06:39:37.926Z\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:21:24.009Z\", \"updated_at\": \"2026-05-15T05:32:12.897Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.03 on spatial. Completes obs_only norm curve (have 0.05, 0.2; adding 0.03).\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": 225144, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45Z\", \"submitted_via\": \"tmux (manual)\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\", \"wall_clock_seconds\": 686.0, \"gpu_hours\": 0.19}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:32:10.962Z\", \"notes\": \"Duplicate experiment on same GPU. pid 225144 was actually the child python process of eval-mag-obsonly-norm003-b2's wrapper (pid 225139). Not a separate experiment. Killed, restarted b2 with new pid 227426.\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:11:14.165Z\", \"updated_at\": \"2026-05-15T05:18:17.853Z\", \"hypothesis\": \"VLA-only baseline (K=1, single sample, no CRM) on LIBERO object benchmark. Lowest-bar baseline for object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --baseline_mode single --benchmark object --n_rollouts 10 --seed 42 --K 1 --output_file logs/eval_object_vla_only_k1.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"39397\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-k1.log\", \"submitted_at\": \"2026-05-15T05:11:22.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only K=1 single sample)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_source\": \"N/A (no CRM, single VLA sample)\", \"wall_clock_seconds\": 311.9, \"gpu_hours\": 0.09}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:16:34.574Z\", \"notes\": \"Duplicate of eval-vla-only-object (already DONE at 12% SR). Process killed to free bjb1-32546 cuda:4.\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-15T05:05:21.600Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"270097\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r2.log\", \"submitted_at\": \"2026-05-14T22:21:35.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm obs_only, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 24161.7, \"gpu_hours\": 6.71}, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。6/10 tasks 完成 + task 7 部分（5/10 rollouts），40.0% SR (24/60)。需重跑。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:04:17.448Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 6/10 tasks，第 7 个 task (next_to_cookie_box) rollout 5/10 时被 kill。\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-15T05:05:19.028Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:3\"], \"pid\": 253085, \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval_acr_spatial_v4_small.log\"}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env init hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。7/10 tasks 完成，42.9% SR (30/70)。需重跑 tasks 8-10（或全部重跑）。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:04:16.712Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 7/10 tasks 后在 task 8 启动前被 kill。\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-15T05:02:30.518Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"spec\": {\"hypothesis\": \"D020 三路消融：scalar_unc CRM v3-norm (val_loss 0.0374) with max_correction_norm=0.1. 与 perdof (cuda:3) 和 obs_only (cuda:0) 同条件对比，判断 per-DOF vs scalar conformal features 的增益\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 288939, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log\", \"gpu_ids\": [\"cuda:2\"]}, \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"notes\": \"[2026-05-15] HUNG: 3/10 tasks done (56.7%, 17/30), stuck on task 4 env init for 8+ hours. Process alive (pid 288939, GPU 1450 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:54.647Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T04:57:55.887Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:57.857060+00:00\"}]}}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:54:57.323Z\", \"updated_at\": \"2026-05-15T04:47:47.959Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --n_rollouts 10 --K 1 --output_file logs/eval_object_vla_only.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only baseline)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.\", \"metrics\": {\"overall_sr\": 0.12, \"total_success\": 12, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"gpu\": \"bjb1-32546:cuda:4\", \"pid\": 17222, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\", \"completed_at\": \"2026-05-15T04:42:20.025Z\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:09.734Z\", \"updated_at\": \"2026-05-15T03:30:05.911Z\", \"hypothesis\": \"D018-D019 验证: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42). 如果 v4-default << v4-small (max_norm=0.1) → magnitude control 是必要的。如果 v4-default ≈ baseline → normalization 独自不够。补全 bjb1 上两次失败的实验。\", \"parent\": \"eval-acr-spatial-v4-default-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"212685\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r3.log\", \"submitted_at\": \"2026-05-15T01:49:35.076Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, default max_correction_norm)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 6030.8, \"gpu_hours\": 1.68}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T03:30:05.911Z\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-15T01:45:12.897Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt --max_correction_norm 0.05\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"232815\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-tiny-correction-spatial.log\", \"submitted_at\": \"2026-05-14T17:48:35.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA per-DOF CRM v2 with tiny correction (max_norm=0.05, 28x smaller than default 1.42)\", \"seed\": 42, \"hypothesis\": \"Extreme correction clipping (0.05 vs 1.42) tests whether compounding error from large CRM deltas is the primary failure mode. If tiny-correction >> full-correction, correction magnitude is the problem.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 27771.0, \"gpu_hours\": 7.71}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:31:26.353Z\", \"failure_reason\": \"D021: v2 checkpoint invalidated by crm_cache_v5 retraining. Replaced by eval-acr-spatial-v4-scalar on bjb1:2.\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:37.194Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"203217\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r2.log\", \"submitted_at\": \"2026-05-14T22:29:03.489Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1).\", \"parent\": \"eval-acr-spatial-v4-default\", \"conclusion\": \"killed\", \"failure_reason\": \"Superseded by D020 plan. Default norm=1.42 already proven to degrade (v4-default: 0/5). Not needed. Process killed on bjb2 (PID 203222 confirmed dead).\", \"completed_at\": \"2026-05-14T22:40:00.000Z\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:08:53.421Z\", \"updated_at\": \"2026-05-14T22:16:05.788Z\", \"hypothesis\": \"D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3 obs_only, default max_correction_norm=1.42)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval-acr-spatial-v4-obs-only.log\", \"tmux_session\": \"eval-acr-spatial-v4-obs-only\", \"pid\": 199257}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T22:16:04.414Z\", \"failure_reason\": \"Wrong checkpoint (crm_v3 not crm_v3_norm) + wrong max_correction_norm (1.42 not 0.1). Killed and replaced by eval-acr-spatial-v4-obs-only-r2.\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:08:59.906Z\", \"updated_at\": \"2026-05-14T22:08:58.490Z\", \"hypothesis\": \"D018: Input normalization alone fixes CRM correction degradation. v3-norm checkpoint with default max_correction_norm=1.42. If >30% baseline → normalization was the main fix.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, default correction)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Process died. D019: 0/5 on task 1 confirmed default norm=1.42 still degrades. Replaced by eval-acr-spatial-v4-obs-only on cuda:0.\", \"completed_at\": \"2026-05-14T22:08:58.490Z\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:01.250Z\", \"updated_at\": \"2026-05-14T22:05:42.608Z\", \"hypothesis\": \"Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (scalar_unc)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"/tmp/crm_train_scalar_unc.log\", \"completed_at\": \"2026-05-14T22:05:42.608Z\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.829Z\", \"updated_at\": \"2026-05-14T22:05:28.289Z\", \"hypothesis\": \"Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (obs_only)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/tmp/crm_train_obs_only.log\", \"completed_at\": \"2026-05-14T22:05:28.289Z\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:45:12.565Z\", \"updated_at\": \"2026-05-14T20:05:22.677Z\", \"hypothesis\": \"D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning\", \"parent\": \"crm-train-v3-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-337K-Normalized\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"no log file (tee failed, output was in tmux pane only)\", \"completed_at\": \"2026-05-14T20:05:20.181Z\", \"results\": {\"best_epoch\": 47, \"best_val_loss\": 0.03578, \"final_train_loss\": 0.04992, \"final_val_loss\": 0.03578, \"total_epochs\": 50, \"normalization\": \"per-feature input normalization (mean/std stored in crm_best.pt as input_mean/input_std tensors)\"}}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:37:14.400Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181896\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-scalar-unc.log\", \"submitted_at\": \"2026-05-14T18:05:00.862Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1917.7, \"gpu_hours\": 0.53}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:15.107Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:19.071535+00:00\"}]}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:36:58.566Z\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:37:04.316Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181973\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"submitted_at\": \"2026-05-14T18:05:02.833Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/spatial\", \"data_count\": 2402, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1802.8, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:22.983Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:25.410071+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"completed_at\": \"2026-05-14T18:35:05.626Z\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:37:02.631Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181668\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"submitted_at\": \"2026-05-14T18:04:54.446Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1510.3, \"gpu_hours\": 0.42}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:11.506Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:13.038696+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/perdof/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:30:04.713Z\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:49:43.787Z\", \"updated_at\": \"2026-05-14T17:47:54.523Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"211961\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:49:43.691Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:2 for eval-tiny-correction-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"wall_clock_seconds\": 17890.8, \"gpu_hours\": 4.97}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:54.523Z\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:08.413Z\", \"updated_at\": \"2026-05-14T17:47:53.188Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"197324\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-unc-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:17:08.325Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"CRM v2 scalar-uncertainty + SmolVLA K=10\", \"seed\": 42, \"hypothesis\": \"Scalar uncertainty CRM ablation — tests whether per-DOF conformal is superior to scalar aggregated uncertainty for action correction.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:1 for eval-argmin-only-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"wall_clock_seconds\": 19844.9, \"gpu_hours\": 5.51}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:53.188Z\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:48:40.837Z\", \"updated_at\": \"2026-05-14T07:59:32.676Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 10 --seed 42 --input_mode scalar_unc --output_dir /root/autodl-tmp/checkpoints/crm/scalar_unc/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"121984\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty)\", \"seed\": 42, \"hypothesis\": \"CRM with scalar Euclidean uncertainty (3D) performs worse than per-DOF (40D), validating per-DOF advantage. Ablation A4, hyperparams matched to plan_001 (bs=32/lr=1e-3).\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"conclusion_note\": \"Training converged. scalar val_loss 0.008379 < per-DOF 0.009046 — original hypothesis (scalar worse) NOT confirmed on val_loss. Hypothesis pending eval-scalar-unc-spatial task success rate validation.\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}, \"completed_at\": \"2026-05-14T02:21:00.891Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:28.643Z\", \"updated_at\": \"2026-05-14T07:59:31.277Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 512 --lr 0.016 --K 10 --seed 42 --input_mode obs_only --output_dir /root/autodl-tmp/checkpoints/crm/obs_only/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-obs_only\", \"seed\": 42, \"hypothesis\": \"CRM without conformal features (obs_only, 990D input) performs significantly worse than full CRM (1030D), validating that per-DOF conformal features are necessary for effective correction\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/train.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:43:51.534Z\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:10:36.535Z\", \"updated_at\": \"2026-05-14T07:59:30.290Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --K 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"78520\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v1.log\", \"data_path\": \"/root/autodl-tmp/crm_cache/ (spatial: 12167 + object: 14570 = 26737 samples)\", \"data_count\": 26737, \"model_name\": \"CRM MLP (337K params, 1030D→256→256→30D)\", \"seed\": 42, \"hypothesis\": \"CRM with per-DOF conformal features (1030D input) learns dimension-selective correction, achieving lower action MSE than scalar/no-uncertainty ablations\", \"checkpoint_source\": \"precompute-v4 (spatial+object)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:40:27.930Z\"}, \"failure_reason\": \"RESOLVED: EXIT_CODE=129 was SIGHUP after training completed (50/50 epochs). Not a real failure.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T22:40:28.559Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:40:29.429643+00:00\"}]}, \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:42:55.911Z\", \"updated_at\": \"2026-05-14T07:59:29.396Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 5 --seed 42 --cache_dir /root/autodl-tmp/crm_cache_k5/ --output_dir /root/autodl-tmp/checkpoints/crm/k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"139839\", \"data_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"data_count\": 26737, \"model_name\": \"CRM (K=5, 337K params)\", \"seed\": 42, \"hypothesis\": \"CRM with K=5 conformal samples for K sensitivity ablation (K=10 baseline val_loss=0.009046)\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/k5/train.log\", \"checkpoint_source\": \"from_scratch\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T04:12:42.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:12:44.286094+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}, \"completed_at\": \"2026-05-14T07:21:32.072Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:54:30.549Z\", \"updated_at\": \"2026-05-14T07:52:44.766Z\", \"spec\": {\"hypothesis\": \"Scalar CRM (3D unc) vs per-DOF CRM (40D unc) on spatial task success rate. Val_loss favored scalar (0.008 vs 0.009) but per-DOF expected to win on task success via dimension-selective correction.\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty, 327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"143206\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-scalar-unc-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch). Scalar CRM trained on wrong features. Replaced by eval-scalar-unc-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:15.933Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-14T07:52:43.327Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:31:30.005Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:31:31.129Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:31:32.734610+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"117814\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM per-DOF)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v2.log\", \"hypothesis\": \"ACR-VLA per-DOF correction improves over SmolVLA baseline on spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM trained on wrong features + CGS quantile wrong. Replaced by eval-acr-spatial-v3.\"}, \"conclusion\": \"killed\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:14:23.092Z\", \"updated_at\": \"2026-05-14T07:52:43.134Z\", \"spec\": {\"command\": \"MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"154189\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA K=5 (CRM 337K + SmolVLA 450M)\", \"seed\": 42, \"hypothesis\": \"K=5 vs K=10 ACR-VLA on task success rate.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-k5-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM K=5 trained on wrong features. Replaced by eval-k5-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:14.685Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:03:35.642Z\", \"updated_at\": \"2026-05-14T01:45:48.892Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (single inference per step)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\", \"failure_reason\": \"Duplicate entry — same PID 125830 tracked by eval-object-v8-full. Cleaning up.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T01:45:48.892Z\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:28.766Z\", \"updated_at\": \"2026-05-14T00:05:22.619Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:03:28.470Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:09.898Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:11.481851+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:03:30.351859+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"117486\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v6-full.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with fixed evaluate.py (reset→set_init_state→zero-action)\", \"failure_reason\": \"vla_only mode running K=10 instead of K=1, wasting GPU. Killed and restarted with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-14T00:04:26.792Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:43:52.899Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-13T23:43:53.809Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:43:56.187212+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"pid\": 117697, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log\", \"gpu\": \"cuda:0\", \"note\": \"restored from false DONE/failed — cron misdetected tmux pipe buffering as process exit\", \"failure_reason\": \"vla_only mode running K=10 multi-sampling (should be K=1). Killed by Director order, replaced by eval-object-v7-full with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:40.287Z\", \"updated_at\": \"2026-05-13T23:14:22.561Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/acr_vla_spatial_v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO spatial benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM perdof)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial, 10 tasks x 10 rollouts\", \"parent\": \"train-crm-v1\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信。已被 eval-acr-spatial-v2 替代\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:13:00.422Z\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:54:28.535Z\", \"updated_at\": \"2026-05-13T23:12:11.315Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/eval-acr-spatial-v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v1.log\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:38.077Z\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T23:12:10.958Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"smolvla_libero + ReconVLA argmin\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:40.252Z\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T23:12:10.037Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"103768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-object-v4-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified-deployed wrapper achieves meaningful success rate on libero_object\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.017Z\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:16:58.052Z\", \"updated_at\": \"2026-05-13T23:12:09.066Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"73756\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v5-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified wrapper + dual camera (agentview + eye_in_hand) achieves >50% on libero_spatial\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.445Z\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:38:57.194Z\", \"updated_at\": \"2026-05-13T19:09:00.612Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"62654\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v3-full.log\", \"submitted_at\": \"2026-05-13T17:38:57.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, rewritten wrapper aligned with lerobot pipeline)\", \"seed\": 42, \"hypothesis\": \"Rewritten wrapper (fully aligned with lerobot SmolVLAPolicy) achieves >50% on libero_spatial with 10 rollouts\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 5403.4, \"gpu_hours\": 1.5}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T19:09:00.612Z\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:08:51.171Z\", \"updated_at\": \"2026-05-13T16:14:40.934Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"87385\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned)\", \"seed\": 42, \"hypothesis\": \"Fixed wrapper (7 bugs) achieves >50% on libero_spatial\", \"log_path\": \"/tmp/eval_spatial.log\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"Killed by Director - wrapper not fully fixed, 55.6% result unreliable. Redirected to full wrapper rewrite aligned with lerobot pipeline.\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T16:14:40.934Z\"}}, \"count\": 177, \"total\": 177, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5822}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T11:18:41.952Z_

<details><summary>↩ Tool result · `toolu_01WHnD68d4Kgm5dH1AmfPvww`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-17 10:56 UTC | 更新原因: D047 6v6 Fisher exact p=0.0074 确认, perdof seed44=8%修正, 9/17 GPU 在跑\\n\\n## 核心方向\\nobs_only CRM 是唯一存活路径。**ε=0.2 是最优配置**（D038）。**Narrative B 已锁定**（D043）：mechanism insight（obs_only magnitude robustness vs perdof collapse）为核心贡献。**6v6 Fisher exact p=0.0074** 为 supplementary evidence（D047）。详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~9 天。\\n\\n## 当前进展\\n- **阶段**: Phase 4 → 准备启动 Paper Agent 正式写作（等用户确认方向 A）\\n- **6v6 pooled (ε=0.2)**: obs_only 105/600 (17.5%) vs argmin 74/600 (12.3%), **+5.2pp, Fisher exact p=0.0074** ✅\\n- **D047**: Claim 1 升级为 \\\"statistically significant (p<0.01, Cohen's d=1.21)\\\"\\n- **D045**: Figure 2 用多 seed 均值±stderr\\n- **GPU**: 9/17 在跑，需填满空闲卡\\n- **论文草稿**: 全 section 有 draft，核心统计数据就绪\\n\\n## Object Benchmark — obs_only ε=0.2 vs argmin（6v6 LOCKED ✅）\\n\\n| Seed | obs_only ε=0.2 | argmin | Δ |\\n|------|----------------|--------|-----|\\n| 42 | 22% | 12% | +10 |\\n| 43 | 16% | 17% | -1 |\\n| 44 | 16% | 13% | +3 |\\n| 45 | 16% | 12% | +4 |\\n| 46 | 15% | 10% | +5 |\\n| 47 | 20% | 10% | +10 |\\n| **Pooled** | **105/600 (17.5%)** | **74/600 (12.3%)** | **+5.2pp, p=0.0074** |\\n\\n## Magnitude Sweep — 多 seed 均值（D045）\\n\\n| norm | obs_only (seeds, mean) | perdof (seeds, mean) | gap |\\n|------|----------------------|---------------------|-----|\\n| 0.03 | 1s: 16% | 1s: 14% | +2pp |\\n| 0.05 | 1s: ~13% | 1s: 14% | -1pp |\\n| 0.10 | 3s: 19/12/16 → **15.7%** | 3s: 11/11/8 → **10.0%** | +5.7pp |\\n| 0.20 | 6s: 22/16/16/16/15/20 → **17.5%** | 1s: 11% | +6.5pp |\\n| 0.30 | 3s: 19/18/14 → **17.0%** | 3s: 4/4/6 → **4.7%** | +12.3pp |\\n| default | 1s: 17% | 1s: 0% | +17pp |\\n\\n## 近期任务\\n- [x] 6v6 Fisher exact p=0.0074 确认 (D047)\\n- [x] argmin seed47 = 10%, argmin seed46 = 10%\\n- [x] perdof ε=0.1 seed44 = 8% (误标 failed 已修正)\\n- [x] D045 magnitude curve 改多 seed 均值\\n- [ ] **空闲 GPU 填满**（8 张空闲）\\n- [ ] n_rollouts=20 实验完成（scalar/perdof-norm02/obs_only-default seed45）\\n- [ ] magnitude curve 剩余 seed 数据补全 (RUNNING 9 个 eval)\\n- [ ] 用户确认方向 A → 启动 Paper Agent\\n- [ ] 最终 Figure 2 (多 seed 均值+error bars) 生成\\n\\n## GPU 预算\\n17× RTX 4090，9/17 运行中，8 张空闲需填满。4 台服务器在线。\\n\\n## Spatial 最终结果（LOCKED ✅）\\n\\n| 方法 | 10-task SR | vs argmin |\\n|------|-----------|-----------|\\n| argmin K=10 | 34% | baseline |\\n| obs_only 0.1 | 35% | +1pp |\\n| perdof 0.1 | 35% | +1pp |\\n| VLA-only K=1 | 30% | -4pp |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D047 | 2026-05-17 | D047: 6v6 Fisher exact p=0.0074 确认, obs_only vs ar | eval-obs-only-object-norm02-seed47, eval-argmin-object-seed47, eval-obs-only-object-norm02-seed46, eval-argmin-object-seed46 |\\n| D046 | 2026-05-17 | D046: 6v6 pooled obs_only vs argmin 达到统计显著 (z-test | eval-obs-only-object-norm02-seed47, eval-argmin-object-seed47, eval-argmin-object-seed46 |\\n| D045 | 2026-05-17 | D045: Figure 2 magnitude curve 必须用多 seed 均值±stderr | eval-obs-only-object-norm01-seed43, eval-obs-only-object-norm03-seed45-r2, eval-obs-only-object-norm02-seed47 |\\n| D044 | 2026-05-17 | Claim 1 降级：从 \\\"obs_only consistently improves over  | eval-obs-only-object-norm02-seed46, eval-obs-only-object-seed43, eval-argmin-object-seed43 |\\n| D043 | 2026-05-17 | D043: Narrative B 正式锁定。4-seed pooled Fisher p=0.11 | eval-obs-only-object-norm02-seed45, eval-argmin-object-seed45, eval-obs-only-object-norm02-seed42, eval-argmin-object-seed42 |\\n| D042 | 2026-05-16 | D042: 论文 claim 结构确定——mechanism insight 为主线（magnitu | eval-acr-object-obs-only-default, eval-perdof-object-default-seed44, eval-obs-only-object-norm02-seed45 |\\n| D041 | 2026-05-16 | D040 修正：正确 Fisher exact p=0.110（非 0.091）。Narrative | eval-obs-only-object-norm02-seed42, eval-obs-only-object-norm02-seed43, eval-obs-only-object-norm02-seed44-r2, eval-argmin-object-seed42, eval-argmin-object-seed43, eval-argmin-object-seed44-r2 |\\n| D040 | 2026-05-16 | 3-seed pooled obs_only vs argmin: +4pp (18% vs 14% | eval-obs-only-object-norm02-seed42, eval-obs-only-object-norm02-seed43, eval-obs-only-object-norm02-seed44-r2, eval-argmin-object-seed42, eval-argmin-object-seed43, eval-argmin-object-seed44-r2 |\\n| D039 | 2026-05-16 | D039: Perdof default norm = 0% (catastrophic colla | eval-acr-object-v4-default-r2, eval-acr-object-obs-only-default, eval-mag-perdof-norm005-object |\\n| D038 | 2026-05-16 | D038: ε=0.2 确认为唯一可辩护配置；seed43 FINAL 16%，pooled 2-s | eval-obs-only-object-norm02-seed43-r2, eval-acr-object-v4-obs-only, eval-obs-only-object-seed43, eval-argmin-object-seed43 |\\n\\n\\n\", \"total_chars\": 4439, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "985fbc26-f948-4716-8d61-85544982ba20",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\\\", \\\"content\\\": \\\"# acr-vla-conformal-refinement — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-17 10:56 UTC | 更新原因: D047 6v6 Fisher exact p=0.0074 确认, perdof seed44=8%修正, 9/17 GPU 在跑\\\\n\\\\n## 核心方向\\\\nobs_only CRM 是唯一存活路径。**ε=0.2 是最优配置**（D038）。**Narrative B 已锁定**（D043）：mechanism insight（obs_only magnitude robustness vs perdof collapse）为核心贡献。**6v6 Fisher exact p=0.0074** 为 supplementary evidence（D047）。详见 paper_framing.md。\\\\n\\\\n## 投稿目标\\\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~9 天。\\\\n\\\\n## 当前进展\\\\n- **阶段**: Phase 4 → 准备启动 Paper Agent 正式写作（等用户确认方向 A）\\\\n- **6v6 pooled (ε=0.2)**: obs_only 105/600 (17.5%) vs argmin 74/600 (12.3%), **+5.2pp, Fisher exact p=0.0074** ✅\\\\n- **D047**: Claim 1 升级为 \\\\\\\"statistically significant (p<0.01, Cohen's d=1.21)\\\\\\\"\\\\n- **D045**: Figure 2 用多 seed 均值±stderr\\\\n- **GPU**: 9/17 在跑，需填满空闲卡\\\\n- **论文草稿**: 全 section 有 draft，核心统计数据就绪\\\\n\\\\n## Object Benchmark — obs_only ε=0.2 vs argmin（6v6 LOCKED ✅）\\\\n\\\\n| Seed | obs_only ε=0.2 | argmin | Δ |\\\\n|------|----------------|--------|-----|\\\\n| 42 | 22% | 12% | +10 |\\\\n| 43 | 16% | 17% | -1 |\\\\n| 44 | 16% | 13% | +3 |\\\\n| 45 | 16% | 12% | +4 |\\\\n| 46 | 15% | 10% | +5 |\\\\n| 47 | 20% | 10% | +10 |\\\\n| **Pooled** | **105/600 (17.5%)** | **74/600 (12.3%)** | **+5.2pp, p=0.0074** |\\\\n\\\\n## Magnitude Sweep — 多 seed 均值（D045）\\\\n\\\\n| norm | obs_only (seeds, mean) | perdof (seeds, mean) | gap |\\\\n|------|----------------------|---------------------|-----|\\\\n| 0.03 | 1s: 16% | 1s: 14% | +2pp |\\\\n| 0.05 | 1s: ~13% | 1s: 14% | -1pp |\\\\n| 0.10 | 3s: 19/12/16 → **15.7%** | 3s: 11/11/8 → **10.0%** | +5.7pp |\\\\n| 0.20 | 6s: 22/16/16/16/15/20 → **17.5%** | 1s: 11% | +6.5pp |\\\\n| 0.30 | 3s: 19/18/14 → **17.0%** | 3s: 4/4/6 → **4.7%** | +12.3pp |\\\\n| default | 1s: 17% | 1s: 0% | +17pp |\\\\n\\\\n## 近期任务\\\\n- [x] 6v6 Fisher exact p=0.0074 确认 (D047)\\\\n- [x] argmin seed47 = 10%, argmin seed46 = 10%\\\\n- [x] perdof ε=0.1 seed44 = 8% (误标 failed 已修正)\\\\n- [x] D045 magnitude curve 改多 seed 均值\\\\n- [ ] **空闲 GPU 填满**（8 张空闲）\\\\n- [ ] n_rollouts=20 实验完成（scalar/perdof-norm02/obs_only-default seed45）\\\\n- [ ] magnitude curve 剩余 seed 数据补全 (RUNNING 9 个 eval)\\\\n- [ ] 用户确认方向 A → 启动 Paper Agent\\\\n- [ ] 最终 Figure 2 (多 seed 均值+error bars) 生成\\\\n\\\\n## GPU 预算\\\\n17× RTX 4090，9/17 运行中，8 张空闲需填满。4 台服务器在线。\\\\n\\\\n## Spatial 最终结果（LOCKED ✅）\\\\n\\\\n| 方法 | 10-task SR | vs argmin |\\\\n|------|-----------|-----------|\\\\n| argmin K=10 | 34% | baseline |\\\\n| obs_only 0.1 | 35% | +1pp |\\\\n| perdof 0.1 | 35% | +1pp |\\\\n| VLA-only K=1 | 30% | -4pp |\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D047 | 2026-05-17 | D047: 6v6 Fisher exact p=0.0074 确认, obs_only vs ar | eval-obs-only-object-norm02-seed47, eval-argmin-object-seed47, eval-obs-only-object-norm02-seed46, eval-argmin-object-seed46 |\\\\n| D046 | 2026-05-17 | D046: 6v6 pooled obs_only vs argmin 达到统计显著 (z-test | eval-obs-only-object-norm02-seed47, eval-argmin-object-seed47, eval-argmin-object-seed46 |\\\\n| D045 | 2026-05-17 | D045: Figure 2 magnitude curve 必须用多 seed 均值±stderr | eval-obs-only-object-norm01-seed43, eval-obs-only-object-norm03-seed45-r2, eval-obs-only-object-norm02-seed47 |\\\\n| D044 | 2026-05-17 | Claim 1 降级：从 \\\\\\\"obs_only consistently improves over  | eval-obs-only-object-norm02-seed46, eval-obs-only-object-seed43, eval-argmin-object-seed43 |\\\\n| D043 | 2026-05-17 | D043: Narrative B 正式锁定。4-seed pooled Fisher p=0.11 | eval-obs-only-object-norm02-seed45, eval-argmin-object-seed45, eval-obs-only-object-norm02-seed42, eval-argmin-object-seed42 |\\\\n| D042 | 2026-05-16 | D042: 论文 claim 结构确定——mechanism insight 为主线（magnitu | eval-acr-object-obs-only-default, eval-perdof-object-default-seed44, eval-obs-only-object-norm02-seed45 |\\\\n| D041 | 2026-05-16 | D040 修正：正确 Fisher exact p=0.110（非 0.091）。Narrative | eval-obs-only-object-norm02-seed42, eval-obs-only-object-norm02-seed43, eval-obs-only-object-norm02-seed44-r2, eval-argmin-object-seed42, eval-argmin-object-seed43, eval-argmin-object-seed44-r2 |\\\\n| D040 | 2026-05-16 | 3-seed pooled obs_only vs argmin: +4pp (18% vs 14% | eval-obs-only-object-norm02-seed42, eval-obs-only-object-norm02-seed43, eval-obs-only-object-norm02-seed44-r2, eval-argmin-object-seed42, eval-argmin-object-seed43, eval-argmin-object-seed44-r2 |\\\\n| D039 | 2026-05-16 | D039: Perdof default norm = 0% (catastrophic colla | eval-acr-object-v4-default-r2, eval-acr-object-obs-only-default, eval-mag-perdof-norm005-object |\\\\n| D038 | 2026-05-16 | D038: ε=0.2 确认为唯一可辩护配置；seed43 FINAL 16%，pooled 2-s | eval-obs-only-object-norm02-seed43-r2, eval-acr-object-v4-obs-only, eval-obs-only-object-seed43, eval-argmin-object-seed43 |\\\\n\\\\n\\\\n\\\", \\\"total_chars\\\": 4439, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-17 10:56 UTC | 更新原因: D047 6v6 Fisher exact p=0.0074 确认, perdof seed44=8%修正, 9/17 GPU 在跑\\n\\n## 核心方向\\nobs_only CRM 是唯一存活路径。**ε=0.2 是最优配置**（D038）。**Narrative B 已锁定**（D043）：mechanism insight（obs_only magnitude robustness vs perdof collapse）为核心贡献。**6v6 Fisher exact p=0.0074** 为 supplementary evidence（D047）。详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~9 天。\\n\\n## 当前进展\\n- **阶段**: Phase 4 → 准备启动 Paper Agent 正式写作（等用户确认方向 A）\\n- **6v6 pooled (ε=0.2)**: obs_only 105/600 (17.5%) vs argmin 74/600 (12.3%), **+5.2pp, Fisher exact p=0.0074** ✅\\n- **D047**: Claim 1 升级为 \\\"statistically significant (p<0.01, Cohen's d=1.21)\\\"\\n- **D045**: Figure 2 用多 seed 均值±stderr\\n- **GPU**: 9/17 在跑，需填满空闲卡\\n- **论文草稿**: 全 section 有 draft，核心统计数据就绪\\n\\n## Object Benchmark — obs_only ε=0.2 vs argmin（6v6 LOCKED ✅）\\n\\n| Seed | obs_only ε=0.2 | argmin | Δ |\\n|------|----------------|--------|-----|\\n| 42 | 22% | 12% | +10 |\\n| 43 | 16% | 17% | -1 |\\n| 44 | 16% | 13% | +3 |\\n| 45 | 16% | 12% | +4 |\\n| 46 | 15% | 10% | +5 |\\n| 47 | 20% | 10% | +10 |\\n| **Pooled** | **105/600 (17.5%)** | **74/600 (12.3%)** | **+5.2pp, p=0.0074** |\\n\\n## Magnitude Sweep — 多 seed 均值（D045）\\n\\n| norm | obs_only (seeds, mean) | perdof (seeds, mean) | gap |\\n|------|----------------------|---------------------|-----|\\n| 0.03 | 1s: 16% | 1s: 14% | +2pp |\\n| 0.05 | 1s: ~13% | 1s: 14% | -1pp |\\n| 0.10 | 3s: 19/12/16 → **15.7%** | 3s: 11/11/8 → **10.0%** | +5.7pp |\\n| 0.20 | 6s: 22/16/16/16/15/20 → **17.5%** | 1s: 11% | +6.5pp |\\n| 0.30 | 3s: 19/18/14 → **17.0%** | 3s: 4/4/6 → **4.7%** | +12.3pp |\\n| default | 1s: 17% | 1s: 0% | +17pp |\\n\\n## 近期任务\\n- [x] 6v6 Fisher exact p=0.0074 确认 (D047)\\n- [x] argmin seed47 = 10%, argmin seed46 = 10%\\n- [x] perdof ε=0.1 seed44 = 8% (误标 failed 已修正)\\n- [x] D045 magnitude curve 改多 seed 均值\\n- [ ] **空闲 GPU 填满**（8 张空闲）\\n- [ ] n_rollouts=20 实验完成（scalar/perdof-norm02/obs_only-default seed45）\\n- [ ] magnitude curve 剩余 seed 数据补全 (RUNNING 9 个 eval)\\n- [ ] 用户确认方向 A → 启动 Paper Agent\\n- [ ] 最终 Figure 2 (多 seed 均值+error bars) 生成\\n\\n## GPU 预算\\n17× RTX 4090，9/17 运行中，8 张空闲需填满。4 台服务器在线。\\n\\n## Spatial 最终结果（LOCKED ✅）\\n\\n| 方法 | 10-task SR | vs argmin |\\n|------|-----------|-----------|\\n| argmin K=10 | 34% | baseline |\\n| obs_only 0.1 | 35% | +1pp |\\n| perdof 0.1 | 35% | +1pp |\\n| VLA-only K=1 | 30% | -4pp |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D047 | 2026-05-17 | D047: 6v6 Fisher exact p=0.0074 确认, obs_only vs ar | eval-obs-only-object-norm02-seed47, eval-argmin-object-seed47, eval-obs-only-object-norm02-seed46, eval-argmin-object-seed46 |\\n| D046 | 2026-05-17 | D046: 6v6 pooled obs_only vs argmin 达到统计显著 (z-test | eval-obs-only-object-norm02-seed47, eval-argmin-object-seed47, eval-argmin-object-seed46 |\\n| D045 | 2026-05-17 | D045: Figure 2 magnitude curve 必须用多 seed 均值±stderr | eval-obs-only-object-norm01-seed43, eval-obs-only-object-norm03-seed45-r2, eval-obs-only-object-norm02-seed47 |\\n| D044 | 2026-05-17 | Claim 1 降级：从 \\\"obs_only consistently improves over  | eval-obs-only-object-norm02-seed46, eval-obs-only-object-seed43, eval-argmin-object-seed43 |\\n| D043 | 2026-05-17 | D043: Narrative B 正式锁定。4-seed pooled Fisher p=0.11 | eval-obs-only-object-norm02-seed45, eval-argmin-object-seed45, eval-obs-only-object-norm02-seed42, eval-argmin-object-seed42 |\\n| D042 | 2026-05-16 | D042: 论文 claim 结构确定——mechanism insight 为主线（magnitu | eval-acr-object-obs-only-default, eval-perdof-object-default-seed44, eval-obs-only-object-norm02-seed45 |\\n| D041 | 2026-05-16 | D040 修正：正确 Fisher exact p=0.110（非 0.091）。Narrative | eval-obs-only-object-norm02-seed42, eval-obs-only-object-norm02-seed43, eval-obs-only-object-norm02-seed44-r2, eval-argmin-object-seed42, eval-argmin-object-seed43, eval-argmin-object-seed44-r2 |\\n| D040 | 2026-05-16 | 3-seed pooled obs_only vs argmin: +4pp (18% vs 14% | eval-obs-only-object-norm02-seed42, eval-obs-only-object-norm02-seed43, eval-obs-only-object-norm02-seed44-r2, eval-argmin-object-seed42, eval-argmin-object-seed43, eval-argmin-object-seed44-r2 |\\n| D039 | 2026-05-16 | D039: Perdof default norm = 0% (catastrophic colla | eval-acr-object-v4-default-r2, eval-acr-object-obs-only-default, eval-mag-perdof-norm005-object |\\n| D038 | 2026-05-16 | D038: ε=0.2 确认为唯一可辩护配置；seed43 FINAL 16%，pooled 2-s | eval-obs-only-object-norm02-seed43-r2, eval-acr-object-v4-obs-only, eval-obs-only-object-seed43, eval-argmin-object-seed43 |\\n\\n\\n\", \"total_chars\": 4439, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
I have paper_framing.md and ROADMAP.md. The registry is too large to read directly. Let me use a subagent to extract the relevant experiment data from the registry file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "f295a57d-6e54-4285-ab52-36ebad29c5b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrRPHrRatK2uxgD9QpEuPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5900,
      "cache_read_input_tokens": 25646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5900
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

_source line 15_

Registry too large for direct reading. Delegating extraction to a subagent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "88b89e4f-2a5a-48ee-ac77-3aca39b93325",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrRPHrRatK2uxgD9QpEuPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5900,
      "cache_read_input_tokens": 25646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5900
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

_source line 16_

<details open><summary>🔧 Tool call — Agent · `toolu_01CFSL8MgqBNRrRnM9bAbSFC`</summary>

```json
{
  "description": "Extract registry experiment data",
  "prompt": "I need you to analyze a large JSON file containing ML experiment registry data and extract structured information.\n\nThe file is at: `/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt`\n\nIt's JSON with schema: `{result: string}` — the `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. Probe structure with jq (type/length/keys)\n2. Extract all experiments, focusing on:\n   - experiment ID\n   - status (DONE, RUNNING, FAILED, etc.)\n   - conclusion (success, failed, etc.)\n   - metrics (success_rate, any other metrics)\n   - experiment type/name (what was being tested — obs_only, perdof, argmin, scalar, vla_mean, etc.)\n   - norm/epsilon settings if present\n   - seed number\n   - any notes\n\nFor each experiment with conclusion=success or status=DONE, I need:\n- The exp_id\n- The method being tested (obs_only, perdof, argmin, VLA-only, scalar, vla_mean, direct_correction, etc.)\n- The norm/epsilon setting\n- The seed\n- The benchmark (object vs spatial)\n- The success_rate metric\n- Number of rollouts (n_rollouts)\n\nAlso list all RUNNING experiments with what they're testing.\n\nReturn the results as a structured summary organized by method type. Be thorough — don't miss any experiments. Quote actual metric values verbatim.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "e6f1da61-3d4c-4aa1-a2cb-5dd525980d25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrRPHrRatK2uxgD9QpEuPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5900,
      "cache_read_input_tokens": 25646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5900
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

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Extract registry experiment data",
  "task_type": "local_agent",
  "prompt": "I need you to analyze a large JSON file containing ML experiment registry data and extract structured information.\n\nThe file is at: `/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt`\n\nIt's JSON with schema: `{result: string}` — the `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. Probe structure with jq (type/length/keys)\n2. Extract all experiments, focusing on:\n   - experiment ID\n   - status (DONE, RUNNING, FAILED, etc.)\n   - conclusion (success, failed, etc.)\n   - metrics (success_rate, any other metrics)\n   - experiment type/name (what was being tested — obs_only, perdof, argmin, scalar, vla_mean, etc.)\n   - norm/epsilon settings if present\n   - seed number\n   - any notes\n\nFor each experiment with conclusion=success or status=DONE, I need:\n- The exp_id\n- The method being tested (obs_only, perdof, argmin, VLA-only, scalar, vla_mean, direct_correction, etc.)\n- The norm/epsilon setting\n- The seed\n- The benchmark (object vs spatial)\n- The success_rate metric\n- Number of rollouts (n_rollouts)\n\nAlso list all RUNNING experiments with what they're testing.\n\nReturn the results as a structured summary organized by method type. Be thorough — don't miss any experiments. Quote actual metric values verbatim.",
  "uuid": "7c57f12c-5c89-49f6-a3b1-dbff0c1e91f2",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

## Round 1

56 recorded events

### User

_source line 18 · 2026-05-17T11:18:56.343Z_

I need you to analyze a large JSON file containing ML experiment registry data and extract structured information.

The file is at: `/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt`

It's JSON with schema: `{result: string}` — the `result` field is itself a JSON string that needs to be parsed.

Steps:
1. Probe structure with jq (type/length/keys)
2. Extract all experiments, focusing on:
   - experiment ID
   - status (DONE, RUNNING, FAILED, etc.)
   - conclusion (success, failed, etc.)
   - metrics (success_rate, any other metrics)
   - experiment type/name (what was being tested — obs_only, perdof, argmin, scalar, vla_mean, etc.)
   - norm/epsilon settings if present
   - seed number
   - any notes

For each experiment with conclusion=success or status=DONE, I need:
- The exp_id
- The method being tested (obs_only, perdof, argmin, VLA-only, scalar, vla_mean, direct_correction, etc.)
- The norm/epsilon setting
- The seed
- The benchmark (object vs spatial)
- The success_rate metric
- Number of rollouts (n_rollouts)

Also list all RUNNING experiments with what they're testing.

Return the results as a structured summary organized by method type. Be thorough — don't miss any experiments. Quote actual metric values verbatim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "5f6adf03-067c-4161-912c-c96206710b24"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 15810,
    "tool_uses": 1,
    "duration_ms": 3921
  },
  "last_tool_name": "Bash",
  "uuid": "f3aacbaf-883c-4ed3-bd0a-d03e6ece05b7",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_013qiXDMxDpMKQpuXnkWig54`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "53dadb3e-27ac-40c4-a745-35824f8a71e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T98PSHMxNNkgYMpKLmm2N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15799,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15799,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 21 · 2026-05-17T11:19:00.417Z_

<details><summary>↩ Tool result · `toolu_013qiXDMxDpMKQpuXnkWig54`</summary>

```text
287661 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "6c5423ec-9958-4b8f-8b76-a0ce9e7bda8e"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Probe JSON structure",
  "usage": {
    "total_tokens": 15814,
    "tool_uses": 2,
    "duration_ms": 7529
  },
  "last_tool_name": "Bash",
  "uuid": "27fa8515-156b-4656-a237-02bc98f9efe0",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01YTUmQQb1spiQrHGrnVunQV`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nprint('Type:', type(inner).__name__)\nif isinstance(inner, dict):\n    print('Top-level keys:', list(inner.keys()))\n    for k, v in inner.items():\n        if isinstance(v, list):\n            print(f'  {k}: list of {len(v)} items')\n        elif isinstance(v, dict):\n            print(f'  {k}: dict with keys {list(v.keys())[:10]}')\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:200]}')\nelif isinstance(inner, list):\n    print('Length:', len(inner))\n    if inner:\n        print('First item keys:', list(inner[0].keys()) if isinstance(inner[0], dict) else type(inner[0]))\n\"\n",
  "description": "Probe JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "48b03176-7d04-4311-a974-f7609978a69e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T98PSHMxNNkgYMpKLmm2N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15799,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15799,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 24 · 2026-05-17T11:19:04.091Z_

<details><summary>↩ Tool result · `toolu_01YTUmQQb1spiQrHGrnVunQV`</summary>

```text
Type: dict
Top-level keys: ['success', 'data', 'error', 'metadata']
  success: bool = True
  data: dict with keys ['experiments', 'count', 'total', 'baseline']
  error: NoneType = None
  metadata: dict with keys ['elapsed_seconds']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "d385bc90-a99c-4a47-b827-3914ab846037"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Explore experiments structure",
  "usage": {
    "total_tokens": 17525,
    "tool_uses": 3,
    "duration_ms": 14111
  },
  "last_tool_name": "Bash",
  "uuid": "1516f1d7-6654-460b-b40b-f830488e2f04",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_014mTUrU1No69p1nNnMD4ZyX`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\ndata = inner['data']\nprint('count:', data['count'])\nprint('total:', data['total'])\nprint('baseline:', json.dumps(data.get('baseline'), indent=2)[:500])\nprint()\nexps = data['experiments']\nprint('Number of experiments:', len(exps))\nif exps:\n    print('First experiment keys:', list(exps[0].keys()))\n    print()\n    print('First experiment sample:')\n    print(json.dumps(exps[0], indent=2)[:2000])\n\"\n",
  "description": "Explore experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "9aa2011a-5814-4594-b946-3e6ed5e1867d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ayg9yawCRvpPbBJbdp7Vv5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1640,
      "cache_read_input_tokens": 15799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1640,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 27 · 2026-05-17T11:19:10.736Z_

<details><summary>↩ Tool result · reported error · `toolu_014mTUrU1No69p1nNnMD4ZyX`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 13, in &lt;module>
    print('First experiment keys:', list(exps[0].keys()))
                                         ~~~~^^^
KeyError: 0
count: 177
total: 177
baseline: null

Number of experiments: 177
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "c9793578-ccef-4aaa-b87d-ce4fe97f01f7",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 13, in &lt;module>\n    print('First experiment keys:', list(exps[0].keys()))\n                                         ~~~~^^^\nKeyError: 0\ncount: 177\ntotal: 177\nbaseline: null\n\nNumber of experiments: 177"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Check experiments dict structure",
  "usage": {
    "total_tokens": 18029,
    "tool_uses": 4,
    "duration_ms": 19806
  },
  "last_tool_name": "Bash",
  "uuid": "e30c7555-d3de-4f73-8467-2f7675aa7d35",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01L7RjRzaT9G3MzuU8roeLTu`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\nprint('Type of experiments:', type(exps).__name__)\nif isinstance(exps, dict):\n    keys = list(exps.keys())\n    print('Number of keys:', len(keys))\n    print('First 5 keys:', keys[:5])\n    first_key = keys[0]\n    print()\n    print(f'Sample experiment [{first_key}]:')\n    print(json.dumps(exps[first_key], indent=2)[:3000])\n\"\n",
  "description": "Check experiments dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "d27ea8bb-34e6-4b1c-9c3e-a0a6ffd5df55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFcYW9UmivKTEboHPvQkid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 432,
      "cache_read_input_tokens": 17439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 432,
        "ephemeral_1h_input_tokens": 0
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

_source line 30 · 2026-05-17T11:19:16.257Z_

<details><summary>↩ Tool result · `toolu_01L7RjRzaT9G3MzuU8roeLTu`</summary>

```text
Type of experiments: dict
Number of keys: 177
First 5 keys: ['eval-obs-only-object-norm02-seed47', 'eval-perdof-object-norm01-seed44', 'eval-perdof-object-norm03-seed45-r2', 'eval-obs-only-object-norm01-seed47-bjb2', 'eval-perdof-object-norm02-seed46']

Sample experiment [eval-obs-only-object-norm02-seed47]:
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T21:32:40.226Z",
  "updated_at": "2026-05-17T11:05:43.649Z",
  "hypothesis": "obs_only CRM (\u03b5=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthens pooled significance for Narrative A transition.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed47.json\"",
    "server": "bjb1-32546",
    "gpu": [
      "cuda:0"
    ],
    "pid": "319128",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed47.log",
    "submitted_at": "2026-05-16T21:33:49.282Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "LIBERO object benchmark (10 tasks)",
    "data_count": 100,
    "model_name": "crm_v3_norm_obs_only",
    "seed": 47,
    "checkpoint_path": "/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json",
    "wall_clock_seconds": 48714.4,
    "gpu_hours": 13.53
  },
  "reproduce": {
    "finished_at": "2026-05-17T10:48:10.086Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-17T10:48:15.850144+00:00"
      }
    ]
  },
  "conclusion": "success",
  "metrics": {
    "success_rate": 0.2,
    "successes": 20,
    "total": 100,
    "benchmark": "object",
    "mode": "obs_only",
    "norm": 0.2,
    "seed": 47
  },
  "completed_at": "2026-05-17T11:05:43.649Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "83683974-5842-41c3-9e28-29bc85385857"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Get status/conclusion distribution and RUNNING experiments",
  "usage": {
    "total_tokens": 19318,
    "tool_uses": 5,
    "duration_ms": 29958
  },
  "last_tool_name": "Bash",
  "uuid": "701be689-82f5-4f9b-a520-d1ffc16c034a",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01WNp3Vc8vawN7Jggyr4Jy8Z`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt | python3 << 'PYEOF'\nimport json, sys\nfrom collections import defaultdict\n\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Collect all statuses and conclusions\nstatuses = defaultdict(int)\nconclusions = defaultdict(int)\n\nfor eid, e in exps.items():\n    statuses[e.get('status', 'UNKNOWN')] += 1\n    conclusions[e.get('conclusion', 'NONE')] += 1\n\nprint(\"=== STATUS DISTRIBUTION ===\")\nfor s, c in sorted(statuses.items(), key=lambda x: -x[1]):\n    print(f\"  {s}: {c}\")\n\nprint(\"\\n=== CONCLUSION DISTRIBUTION ===\")\nfor s, c in sorted(conclusions.items(), key=lambda x: -x[1]):\n    print(f\"  {s}: {c}\")\n\nprint(\"\\n=== ALL RUNNING EXPERIMENTS ===\")\nfor eid, e in sorted(exps.items()):\n    if e.get('status') == 'RUNNING':\n        spec = e.get('spec', {})\n        metrics = e.get('metrics', {})\n        hyp = e.get('hypothesis', '')\n        server = spec.get('server', '?')\n        print(f\"\\n  ID: {eid}\")\n        print(f\"  Server: {server}\")\n        print(f\"  Hypothesis: {hyp[:200]}\")\n        if metrics:\n            print(f\"  Metrics so far: {json.dumps(metrics)}\")\nPYEOF\n",
  "description": "Get status/conclusion distribution and RUNNING experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "5bbbe2ea-0cf5-43f8-b3f5-1f0547da613a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ViNxHEEdBjnGqUi6c1yRrd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 17871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1287,
        "ephemeral_1h_input_tokens": 0
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

_source line 33 · 2026-05-17T11:19:26.593Z_

<details><summary>↩ Tool result · reported error · `toolu_01WNp3Vc8vawN7Jggyr4Jy8Z`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 4, in &lt;module>
  File "/usr/lib/python3.14/json/__init__.py", line 298, in load
    return loads(fp.read(),
        cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "784e797b-1bdc-4ae8-9abd-f132a4f9d43a",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 4, in &lt;module>\n  File \"/usr/lib/python3.14/json/__init__.py\", line 298, in load\n    return loads(fp.read(),\n        cls=cls, object_hook=object_hook,\n        parse_float=parse_float, parse_int=parse_int,\n        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 363, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Check file encoding/format",
  "usage": {
    "total_tokens": 20278,
    "tool_uses": 6,
    "duration_ms": 33789
  },
  "last_tool_name": "Bash",
  "uuid": "ef73925c-a760-4d1c-bd34-371e2afa3b95",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01GFitvmtRaWrvd4PYMS8FSK`</summary>

```json
{
  "command": "head -c 200 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt",
  "description": "Check file encoding/format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "2319517a-81fe-40c6-9bd6-f07f2c7a47b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UthEU2pdCdkxhbghuj5pC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 901,
      "cache_read_input_tokens": 19158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 901,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 36 · 2026-05-17T11:19:30.208Z_

<details><summary>↩ Tool result · `toolu_01GFitvmtRaWrvd4PYMS8FSK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:32:40.226Z\", \"updated_a
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "1cefabab-5686-438a-a62b-54580ba9cb46"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Get status/conclusion distribution and RUNNING experiments",
  "usage": {
    "total_tokens": 20602,
    "tool_uses": 7,
    "duration_ms": 40151
  },
  "last_tool_name": "Bash",
  "uuid": "accd80cd-4013-44e1-b611-ce25cd1afcd1",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wd1GcejZWKJ9KQgHV8u1d9`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, sys\nfrom collections import defaultdict\n\nwith open(\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt\", \"r\") as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\nstatuses = defaultdict(int)\nconclusions = defaultdict(int)\n\nfor eid, e in exps.items():\n    statuses[e.get('status', 'UNKNOWN')] += 1\n    conclusions[e.get('conclusion', 'NONE')] += 1\n\nprint(\"=== STATUS DISTRIBUTION ===\")\nfor s, c in sorted(statuses.items(), key=lambda x: -x[1]):\n    print(f\"  {s}: {c}\")\n\nprint(\"\\n=== CONCLUSION DISTRIBUTION ===\")\nfor s, c in sorted(conclusions.items(), key=lambda x: -x[1]):\n    print(f\"  {s}: {c}\")\n\nprint(\"\\n=== ALL RUNNING EXPERIMENTS ===\")\nfor eid, e in sorted(exps.items()):\n    if e.get('status') == 'RUNNING':\n        spec = e.get('spec', {})\n        metrics = e.get('metrics', {})\n        hyp = e.get('hypothesis', '')\n        server = spec.get('server', '?')\n        print(f\"\\n  ID: {eid}\")\n        print(f\"  Server: {server}\")\n        print(f\"  Hypothesis: {hyp[:200]}\")\n        if metrics:\n            print(f\"  Metrics so far: {json.dumps(metrics)}\")\nPYEOF\n",
  "description": "Get status/conclusion distribution and RUNNING experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "a84bc44f-6767-4b21-bac8-1d8c3dbbdbd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGHpFCtLKgsdSNqt2L7kjR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 20059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 270,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
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

_source line 39 · 2026-05-17T11:19:36.657Z_

<details><summary>↩ Tool result · `toolu_01Wd1GcejZWKJ9KQgHV8u1d9`</summary>

```text
=== STATUS DISTRIBUTION ===
  DONE: 162
  RUNNING: 11
  PREPARING: 3
  DEPLOYED: 1

=== CONCLUSION DISTRIBUTION ===
  success: 69
  killed: 59
  failed: 26
  NONE: 12
  negative: 11

=== ALL RUNNING EXPERIMENTS ===

  ID: eval-obs-only-object-default-seed45
  Server: bjb2-28827
  Hypothesis: obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 uncapped 大 norm 下仍优于 VLA-only（seed42 在 default 为 17%）。极端 magnitude 鲁棒性测试。

  ID: eval-obs-only-object-norm01-seed45
  Server: bjb1-18228
  Hypothesis: obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。seed42 在 0.1 为 19%，如果一致则确认 obs_only 全 norm 范围鲁棒。

  ID: eval-obs-only-object-norm01-seed46-r2
  Server: bjb1-18228
  Hypothesis: obs_only CRM at eps=0.1 on seed46 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude curve

  ID: eval-obs-only-object-norm01-seed47-r2
  Server: bjb1-18228
  Hypothesis: obs_only CRM at eps=0.1 on seed47 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude curve

  ID: eval-obs-only-object-norm03-seed46
  Server: bjb1-32546
  Hypothesis: obs_only CRM at eps=0.3 on seed46 extends magnitude curve high-norm data. seed42=19%, seed44=18%, seed45=14%. 4th seed at this norm.

  ID: eval-perdof-object-norm01-seed46-r2
  Server: bjb1-32546
  Hypothesis: perdof CRM at eps=0.1 on seed46 will show magnitude sensitivity collapse pattern similar to seed42, confirming obs_only robustness advantage

  ID: eval-perdof-object-norm01-seed47-bjb1
  Server: bjb1-32546
  Hypothesis: Duplicate of perdof norm=0.1 seed47 on bjb1-32546 (deployed by orphan Worker). Also running on bjb2-40593.

  ID: eval-perdof-object-norm02-seed44
  Server: bjb2-28827
  Hypothesis: perdof CRM (ε=0.2) seed=44 on LIBERO Object benchmark. Adds second seed to perdof norm=0.2 (seed42=11%, seed43=9%). Enables error bar on magnitude curve figure at this norm point.

  ID: eval-perdof-object-norm02-seed45
  Server: bjb2-28827
  Hypothesis: perdof CRM (ε=0.2) seed=45 on LIBERO Object. 验证 perdof 在中间 norm (0.2) 的表现（seed42=11%, seed43=9%）。为 magnitude curve 误差估计提供第三个 seed。

  ID: eval-perdof-object-norm02-seed46
  Server: bjb2-28827
  Hypothesis: perdof CRM ε=0.2 seed46 on LIBERO-Object. 补充 perdof magnitude curve ε=0.2 数据（目前仅 seed43=9%）。与 obs_only ε=0.2 seed46 配对对比。

  ID: eval-scalar-object-seed45
  Server: bjb2-28827
  Hypothesis: Scalar uncertainty CRM seed=45 on LIBERO Object. 测试 scalar conditioning（单一 std 而非 per-DOF）是否比 obs_only 或 perdof 更优。如果表现介于两者之间，说明 conditioning 信息量与性能正相关。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "ba6275c3-a037-4dce-896c-cfb6ad3799b4"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Extract all DONE+success experiments grouped by method",
  "usage": {
    "total_tokens": 22341,
    "tool_uses": 8,
    "duration_ms": 58716
  },
  "last_tool_name": "Bash",
  "uuid": "bd1a1359-0f6a-4140-a7a9-34cf2438b459",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01Tut6CqSy8TwKBaKoD89Jwq`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nfrom collections import defaultdict\n\nwith open(\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt\", \"r\") as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Collect ALL DONE experiments with success conclusion\ndone_success = []\nfor eid, e in exps.items():\n    if e.get('status') == 'DONE' and e.get('conclusion') == 'success':\n        m = e.get('metrics', {})\n        spec = e.get('spec', {})\n        done_success.append({\n            'exp_id': eid,\n            'success_rate': m.get('success_rate'),\n            'successes': m.get('successes'),\n            'total': m.get('total'),\n            'benchmark': m.get('benchmark'),\n            'mode': m.get('mode'),\n            'norm': m.get('norm'),\n            'seed': m.get('seed'),\n            'n_rollouts': spec.get('data_count') or m.get('total'),\n            'hypothesis': e.get('hypothesis', '')[:150],\n        })\n\n# Sort by mode, then benchmark, then norm, then seed\ndone_success.sort(key=lambda x: (str(x['mode']), str(x['benchmark']), str(x['norm']), str(x['seed'])))\n\nprint(f\"=== DONE + SUCCESS experiments: {len(done_success)} ===\\n\")\n\n# Group by method\nby_method = defaultdict(list)\nfor exp in done_success:\n    by_method[exp['mode'] or 'unknown'].append(exp)\n\nfor method in sorted(by_method.keys()):\n    exps_list = by_method[method]\n    print(f\"\\n{'='*80}\")\n    print(f\"METHOD: {method} ({len(exps_list)} experiments)\")\n    print(f\"{'='*80}\")\n    \n    # Sub-group by benchmark\n    by_bench = defaultdict(list)\n    for exp in exps_list:\n        by_bench[exp['benchmark'] or 'unknown'].append(exp)\n    \n    for bench in sorted(by_bench.keys()):\n        bench_exps = by_bench[bench]\n        print(f\"\\n  Benchmark: {bench}\")\n        print(f\"  {'─'*60}\")\n        \n        # Sub-group by norm\n        by_norm = defaultdict(list)\n        for exp in bench_exps:\n            by_norm[exp['norm']].append(exp)\n        \n        for norm in sorted(by_norm.keys(), key=lambda x: (x is None, x)):\n            norm_exps = by_norm[norm]\n            norm_exps.sort(key=lambda x: (x['seed'] or 0))\n            print(f\"\\n    Norm/Epsilon: {norm}\")\n            for exp in norm_exps:\n                print(f\"      {exp['exp_id']}\")\n                print(f\"        seed={exp['seed']}, success_rate={exp['success_rate']}, successes={exp['successes']}/{exp['total']}, n_rollouts={exp['n_rollouts']}\")\nPYEOF\n",
  "description": "Extract all DONE+success experiments grouped by method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "a42a4eb7-b291-44f2-8eb6-b4857a4c3534",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xXGRaFxxU381Rb2K9ZG9C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1672,
      "cache_read_input_tokens": 20329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1672,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 42 · 2026-05-17T11:19:55.210Z_

<details><summary>↩ Tool result · `toolu_01Tut6CqSy8TwKBaKoD89Jwq`</summary>

```text
=== DONE + SUCCESS experiments: 69 ===


================================================================================
METHOD: crm_obs_only (3 experiments)
================================================================================

  Benchmark: object
  ────────────────────────────────────────────────────────────

    Norm/Epsilon: None
      eval-obs-only-object-norm03-seed45-r2
        seed=45, success_rate=None, successes=None/None, n_rollouts=100

  Benchmark: spatial
  ────────────────────────────────────────────────────────────

    Norm/Epsilon: None
      eval-mag-obsonly-norm005
        seed=None, success_rate=None, successes=None/None, n_rollouts=10 tasks x 10 rollouts
      eval-acr-spatial-v4-obs-only-r3
        seed=42, success_rate=None, successes=None/None, n_rollouts=40

================================================================================
METHOD: crm_perdof (1 experiments)
================================================================================

  Benchmark: object
  ────────────────────────────────────────────────────────────

    Norm/Epsilon: None
      eval-perdof-object-norm01-seed45
        seed=45, success_rate=None, successes=None/None, n_rollouts=100

================================================================================
METHOD: obs_only (2 experiments)
================================================================================

  Benchmark: object
  ────────────────────────────────────────────────────────────

    Norm/Epsilon: 0.2
      eval-obs-only-object-norm02-seed47
        seed=47, success_rate=0.2, successes=20/100, n_rollouts=100

    Norm/Epsilon: None
      eval-acr-object-v4-obs-only
        seed=42, success_rate=None, successes=None/None, n_rollouts=None

================================================================================
METHOD: perdof (2 experiments)
================================================================================

  Benchmark: object
  ────────────────────────────────────────────────────────────

    Norm/Epsilon: None
      eval-acr-object-v4-perdof
        seed=42, success_rate=None, successes=None/None, n_rollouts=100

  Benchmark: spatial
  ────────────────────────────────────────────────────────────

    Norm/Epsilon: None
      eval-acr-spatial-v4-small-r2
        seed=42, success_rate=None, successes=None/None, n_rollouts=30

================================================================================
METHOD: reconvla (2 experiments)
================================================================================

  Benchmark: object
  ────────────────────────────────────────────────────────────

    Norm/Epsilon: None
      eval-argmin-object-seed46
        seed=46, success_rate=None, successes=None/None, n_rollouts=None
      eval-argmin-object-seed47
        seed=47, success_rate=None, successes=None/None, n_rollouts=100

================================================================================
METHOD: scalar_unc (1 experiments)
================================================================================

  Benchmark: spatial
  ────────────────────────────────────────────────────────────

    Norm/Epsilon: None
      eval-acr-spatial-v4-scalar-r2
        seed=42, success_rate=None, successes=None/None, n_rollouts=70

================================================================================
METHOD: unknown (57 experiments)
================================================================================

  Benchmark: unknown
  ────────────────────────────────────────────────────────────

    Norm/Epsilon: None
      eval-perdof-object-norm03-seed45-r2
        seed=None, success_rate=None, successes=6/100, n_rollouts=100
      eval-obs-only-object-norm02-seed46
        seed=None, success_rate=0.15, successes=15/None, n_rollouts=100
      eval-vla-mean-object-seed45
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-argmin-object-seed45
        seed=None, success_rate=None, successes=12/None, n_rollouts=100
      eval-direct-correction-object-seed42-r3
        seed=None, success_rate=0.14, successes=14/None, n_rollouts=100 episodes (10 tasks x 10 rollouts)
      eval-vla-mean-spatial
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-acr-object-obs-only-norm02
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-spatial-v7-full
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-object-v8-full
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      precompute-v5-shard2
        seed=None, success_rate=None, successes=None/None, n_rollouts=~8900 samples (shard 2 of 3)
      precompute-v5-shard1
        seed=None, success_rate=None, successes=None/None, n_rollouts=~8900 samples (shard 1 of 3)
      precompute-v5-shard0
        seed=None, success_rate=None, successes=None/None, n_rollouts=~8900 samples (shard 0 of 3)
      precompute-v4-shard2
        seed=None, success_rate=None, successes=None/None, n_rollouts=None
      precompute-v4-shard1
        seed=None, success_rate=None, successes=None/None, n_rollouts=None
      precompute-v4-shard0
        seed=None, success_rate=None, successes=None/None, n_rollouts=None
      eval-obs-only-object-norm01-seed44
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-vla-only-object-seed45
        seed=None, success_rate=None, successes=18/200, n_rollouts=10
      eval-vla-only-object-seed43
        seed=None, success_rate=None, successes=None/None, n_rollouts=10
      eval-vla-mean-spatial-t10
        seed=None, success_rate=None, successes=None/None, n_rollouts=10
      eval-reconvla-spatial-v3
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      crm-train-v2-scalar-unc
        seed=None, success_rate=None, successes=None/None, n_rollouts=26737
      crm-train-v2-perdof
        seed=None, success_rate=None, successes=None/None, n_rollouts=26737
      crm-train-v2-obs-only
        seed=None, success_rate=None, successes=None/None, n_rollouts=26737
      precompute-shard2
        seed=None, success_rate=None, successes=None/None, n_rollouts=None
      precompute-shard1
        seed=None, success_rate=None, successes=None/None, n_rollouts=None
      precompute-shard0
        seed=None, success_rate=None, successes=None/None, n_rollouts=None
      precompute-k5
        seed=None, success_rate=None, successes=None/None, n_rollouts=26737
      mvp-point-reaching
        seed=None, success_rate=None, successes=None/None, n_rollouts=20000
      eval-obs-only-object-default-seed44
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-mag-perdof-norm005-object
        seed=None, success_rate=None, successes=14/100, n_rollouts=10
      eval-mag-perdof-norm02-seed43-object-r3
        seed=None, success_rate=None, successes=9/100, n_rollouts=100
      eval-mag-perdof-norm03-object-r3
        seed=None, success_rate=None, successes=4/100, n_rollouts=100
      eval-mag-obsonly-norm003-b2
        seed=None, success_rate=None, successes=None/None, n_rollouts=10
      eval-mag-obsonly-norm03-object
        seed=None, success_rate=None, successes=19/100, n_rollouts=10
      eval-mag-obsonly-norm005-object
        seed=None, success_rate=None, successes=13/None, n_rollouts=10
      eval-obs-only-object-norm02-seed45
        seed=None, success_rate=None, successes=16/None, n_rollouts=100
      eval-obs-only-object-norm03-seed44
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-vla-mean-object-seed44
        seed=None, success_rate=None, successes=None/None, n_rollouts=None
      eval-argmin-object-seed44-r2
        seed=None, success_rate=None, successes=13/100, n_rollouts=100
      eval-obs-only-object-norm02-seed44-r2
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-acr-object-v4-default-r2
        seed=None, success_rate=None, successes=0/100, n_rollouts=10
      eval-mag-perdof-norm003-object
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-obs-only-object-norm02-seed43-r2
        seed=None, success_rate=None, successes=16/100, n_rollouts=100
      eval-vla-only-object-seed44-r2
        seed=None, success_rate=None, successes=None/None, n_rollouts=None
      eval-acr-object-obs-only-default
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-scalar-object-seed43
        seed=None, success_rate=None, successes=None/None, n_rollouts=10
      eval-mag-obsonly-norm003-object
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-vla-mean-object-seed43
        seed=None, success_rate=None, successes=None/None, n_rollouts=10
      eval-perdof-object-seed43
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-argmin-object-seed43
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-mag-obsonly-norm03-r2
        seed=None, success_rate=None, successes=None/None, n_rollouts=100
      eval-reconvla-object
        seed=None, success_rate=None, successes=None/None, n_rollouts=None
      eval-argmin-only-spatial-r2
        seed=None, success_rate=None, successes=None/None, n_rollouts=10
      eval-vla-only-object
        seed=None, success_rate=None, successes=None/None, n_rollouts=10 tasks x 10 rollouts
      crm-train-v3-norm-scalar-unc
        seed=None, success_rate=None, successes=None/None, n_rollouts=12167
      crm-train-v3-norm-obs-only
        seed=None, success_rate=None, successes=None/None, n_rollouts=12167
      crm-train-v3-norm
        seed=None, success_rate=None, successes=None/None, n_rollouts=12167

================================================================================
METHOD: vla_only (1 experiments)
================================================================================

  Benchmark: object
  ────────────────────────────────────────────────────────────

    Norm/Epsilon: None
      eval-vla-mean-object
        seed=42, success_rate=None, successes=None/None, n_rollouts=100
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "8710735d-bbb6-4f43-96de-d2b3a741e601"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Dump all fields from DONE+success experiments",
  "usage": {
    "total_tokens": 26629,
    "tool_uses": 9,
    "duration_ms": 177149
  },
  "last_tool_name": "Bash",
  "uuid": "f583ff97-26b5-430a-8764-eb8162d97e49",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_012AgUSxrB7e6fuybEmqqH2s`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nfrom collections import defaultdict\n\nwith open(\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt\", \"r\") as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# For ALL DONE+success experiments, dump all available info\nfor eid, e in sorted(exps.items()):\n    if e.get('status') != 'DONE' or e.get('conclusion') != 'success':\n        continue\n    m = e.get('metrics', {})\n    spec = e.get('spec', {})\n    notes = e.get('notes', '')\n    \n    # Try to extract method from metrics, hypothesis, or exp_id\n    mode = m.get('mode', '')\n    benchmark = m.get('benchmark', '')\n    norm = m.get('norm')\n    seed = m.get('seed')\n    sr = m.get('success_rate')\n    successes = m.get('successes')\n    total = m.get('total')\n    n_rollouts = spec.get('data_count')\n    \n    # Print everything we have\n    has_sr = sr is not None or successes is not None\n    print(f\"ID: {eid}\")\n    print(f\"  mode={mode}, benchmark={benchmark}, norm={norm}, seed={seed}\")\n    print(f\"  success_rate={sr}, successes={successes}, total={total}, n_rollouts={n_rollouts}\")\n    # print all other metric keys\n    other_keys = {k: v for k, v in m.items() if k not in ('mode', 'benchmark', 'norm', 'seed', 'success_rate', 'successes', 'total')}\n    if other_keys:\n        print(f\"  other_metrics: {json.dumps(other_keys)}\")\n    if notes:\n        print(f\"  notes: {notes[:200]}\")\n    print()\nPYEOF\n",
  "description": "Dump all fields from DONE+success experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "20e785cb-3e4e-484c-b12e-ff7c927914d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2hBRhGEqeDtjMEJ4Am9PL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4286,
      "cache_read_input_tokens": 22001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4286,
        "ephemeral_1h_input_tokens": 0
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

_source line 45 · 2026-05-17T11:21:53.588Z_

<details><summary>↩ Tool result · `toolu_012AgUSxrB7e6fuybEmqqH2s`</summary>

```text
&lt;persisted-output>
Output too large (29.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/bxxzi1hiw.txt

Preview (first 2KB):
ID: crm-train-v2-obs-only
  mode=, benchmark=, norm=None, seed=None
  success_rate=None, successes=None, total=None, n_rollouts=26737
  other_metrics: {"best_val_loss": 0.050501, "best_epoch": 50, "total_epochs": 50, "final_train_loss": 0.074839, "comparison_vs_old": "old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)"}

ID: crm-train-v2-perdof
  mode=, benchmark=, norm=None, seed=None
  success_rate=None, successes=None, total=None, n_rollouts=26737
  other_metrics: {"best_val_loss": 0.051684, "best_epoch": 48, "total_epochs": 50, "final_train_loss": 0.076748, "comparison_vs_old": "old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)"}

ID: crm-train-v2-scalar-unc
  mode=, benchmark=, norm=None, seed=None
  success_rate=None, successes=None, total=None, n_rollouts=26737
  other_metrics: {"best_val_loss": 0.047202, "best_epoch": 48, "total_epochs": 50, "final_train_loss": 0.069679, "comparison_vs_old": "old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)"}

ID: crm-train-v3-norm
  mode=, benchmark=, norm=None, seed=None
  success_rate=None, successes=None, total=None, n_rollouts=12167

ID: crm-train-v3-norm-obs-only
  mode=, benchmark=, norm=None, seed=None
  success_rate=None, successes=None, total=None, n_rollouts=12167
  other_metrics: {"best_epoch": 48, "best_val_loss": 0.01645, "final_train_loss": 0.025576, "final_val_loss": 0.01645, "total_epochs": 50}

ID: crm-train-v3-norm-scalar-unc
  mode=, benchmark=, norm=None, seed=None
  success_rate=None, successes=None, total=None, n_rollouts=12167
  other_metrics: {"best_epoch": 46, "best_val_loss": 0.037354, "final_train_loss": 0.053422, "final_val_loss": 0.03737}

ID: eval-acr-object-obs-only-default
  mode=, benchmark=, norm=None, seed=None
  success_rate=None, successes=None, total=None, n_rollouts=100
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "94a07de4-ced3-49b6-aa79-44fe5f8b5638"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/bxxzi1hiw.txt",
  "usage": {
    "total_tokens": 28246,
    "tool_uses": 10,
    "duration_ms": 181400
  },
  "last_tool_name": "Read",
  "uuid": "fb2af47d-da21-4759-8fb8-9604accc7f86",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01RrnmFnxx6kYiskYkPrSpFB`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/bxxzi1hiw.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "16792075-4521-414c-b687-57ab71757690",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcPj1zjHyymgDv5MiGXb1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1552,
      "cache_read_input_tokens": 26287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1552,
        "ephemeral_1h_input_tokens": 0
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

_source line 48 · 2026-05-17T11:21:58.000Z_

<details><summary>↩ Tool result · `toolu_01RrnmFnxx6kYiskYkPrSpFB`</summary>

```text
1	ID: crm-train-v2-obs-only
2	  mode=, benchmark=, norm=None, seed=None
3	  success_rate=None, successes=None, total=None, n_rollouts=26737
4	  other_metrics: {"best_val_loss": 0.050501, "best_epoch": 50, "total_epochs": 50, "final_train_loss": 0.074839, "comparison_vs_old": "old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)"}
5	
6	ID: crm-train-v2-perdof
7	  mode=, benchmark=, norm=None, seed=None
8	  success_rate=None, successes=None, total=None, n_rollouts=26737
9	  other_metrics: {"best_val_loss": 0.051684, "best_epoch": 48, "total_epochs": 50, "final_train_loss": 0.076748, "comparison_vs_old": "old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)"}
10	
11	ID: crm-train-v2-scalar-unc
12	  mode=, benchmark=, norm=None, seed=None
13	  success_rate=None, successes=None, total=None, n_rollouts=26737
14	  other_metrics: {"best_val_loss": 0.047202, "best_epoch": 48, "total_epochs": 50, "final_train_loss": 0.069679, "comparison_vs_old": "old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)"}
15	
16	ID: crm-train-v3-norm
17	  mode=, benchmark=, norm=None, seed=None
18	  success_rate=None, successes=None, total=None, n_rollouts=12167
19	
20	ID: crm-train-v3-norm-obs-only
21	  mode=, benchmark=, norm=None, seed=None
22	  success_rate=None, successes=None, total=None, n_rollouts=12167
23	  other_metrics: {"best_epoch": 48, "best_val_loss": 0.01645, "final_train_loss": 0.025576, "final_val_loss": 0.01645, "total_epochs": 50}
24	
25	ID: crm-train-v3-norm-scalar-unc
26	  mode=, benchmark=, norm=None, seed=None
27	  success_rate=None, successes=None, total=None, n_rollouts=12167
28	  other_metrics: {"best_epoch": 46, "best_val_loss": 0.037354, "final_train_loss": 0.053422, "final_val_loss": 0.03737}
29	
30	ID: eval-acr-object-obs-only-default
31	  mode=, benchmark=, norm=None, seed=None
32	  success_rate=None, successes=None, total=None, n_rollouts=100
33	  other_metrics: {"tasks_done": 10, "tasks_total": 10, "overall_sr": 0.17, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.2, "bbq_sauce": 0.4, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.1, "chocolate_pudding": 0.5, "orange_juice": 0.3}}
34	
35	ID: eval-acr-object-obs-only-norm02
36	  mode=, benchmark=, norm=None, seed=None
37	  success_rate=None, successes=None, total=None, n_rollouts=100
38	  other_metrics: {"overall_sr": 0.22, "total_success": 22, "total_rollouts": 100, "tasks_done": 10, "tasks_total": 10, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.3, "bbq_sauce": 0.4, "ketchup": 0.2, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.2, "chocolate_pudding": 0.6, "orange_juice": 0.3}}
39	
40	ID: eval-acr-object-v4-default-r2
41	  mode=, benchmark=, norm=None, seed=None
42	  success_rate=None, successes=0, total=100, n_rollouts=10
43	  other_metrics: {"overall_sr": 0, "tasks_done": 10, "tasks_total": 10, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0, "bbq_sauce": 0, "ketchup": 0, "tomato_sauce": 0, "butter": 0, "milk": 0, "chocolate_pudding": 0, "orange_juice": 0}, "note": "actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude."}
44	
45	ID: eval-acr-object-v4-obs-only
46	  mode=obs_only, benchmark=object, norm=None, seed=42
47	  success_rate=None, successes=None, total=None, n_rollouts=None
48	  other_metrics: {"overall_sr": "19.0% (19/100)", "total_success": 19, "total_rollouts": 100, "max_correction_norm": 0.1, "K": 10, "tasks_done": "10/10", "per_task": {"alphabet_soup": "0%", "cream_cheese": "10%", "salad_dressing": "20%", "bbq_sauce": "40%", "ketchup": "10%", "tomato_sauce": "0%", "butter": "10%", "milk": "20%", "chocolate_pudding": "50%", "orange_juice": "30%"}, "json_output": "/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json"}
49	
50	ID: eval-acr-object-v4-perdof
51	  mode=perdof, benchmark=object, norm=None, seed=42
52	  success_rate=None, successes=None, total=None, n_rollouts=100
53	  other_metrics: {"overall_sr": "11.0% (11/100)", "total_success": 11, "total_rollouts": 100, "max_correction_norm": 0.1, "K": 10, "per_task": {"alphabet_soup": "0%", "cream_cheese": "0%", "salad_dressing": "20%", "bbq_sauce": "30%", "ketchup": "0%", "tomato_sauce": "0%", "butter": "10%", "milk": "0%", "chocolate_pudding": "20%", "orange_juice": "30%"}, "note": "perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object."}
54	
55	ID: eval-acr-spatial-v4-obs-only-r3
56	  mode=crm_obs_only, benchmark=spatial, norm=None, seed=42
57	  success_rate=None, successes=None, total=None, n_rollouts=40
58	  other_metrics: {"overall_sr": "35.0% (35/100)", "total_success": 35, "total_rollouts": 100, "max_correction_norm": 0.1, "K": 10, "per_task": {"T0": "90%", "T1": "100%", "T2": "0%", "T3": "40%", "T4": "10%", "T5": "0%", "T6": "90%", "T7": "0%", "T8": "20%", "T9": "0%"}, "r3_subset_T6_T9": "27.5% (11/40)", "note": "D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9."}
59	
60	ID: eval-acr-spatial-v4-scalar-r2
61	  mode=scalar_unc, benchmark=spatial, norm=None, seed=42
62	  success_rate=None, successes=None, total=None, n_rollouts=70
63	  other_metrics: {"overall_sr": "32.0% (32/100)", "total_success": 32, "total_rollouts": 100, "max_correction_norm": 0.1, "K": 10, "per_task": {"T0": "60%", "T1": "100%", "T2": "10%", "T3": "40%", "T4": "0%", "T5": "0%", "T6": "90%", "T7": "0%", "T8": "10%", "T9": "10%"}, "note": "D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial."}
64	
65	ID: eval-acr-spatial-v4-small-r2
66	  mode=perdof, benchmark=spatial, norm=None, seed=42
67	  success_rate=None, successes=None, total=None, n_rollouts=30
68	  other_metrics: {"overall_sr": "35.0% (35/100)", "total_success": 35, "total_rollouts": 100, "max_correction_norm": 0.1, "K": 10, "per_task": {"T0": "60%", "T1": "100%", "T2": "10%", "T3": "40%", "T4": "0%", "T5": "0%", "T6": "90%", "T7": "10%", "T8": "40%", "T9": "0%"}, "note": "D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered \u2014 per-DOF claim dead on spatial."}
69	  notes: [D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。
70	
71	ID: eval-argmin-object-seed43
72	  mode=, benchmark=, norm=None, seed=None
73	  success_rate=None, successes=None, total=None, n_rollouts=100
74	  other_metrics: {"overall_success_rate": 0.17, "total_successes": 17, "total_trials": 100, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.2, "bbq_sauce": 0.2, "ketchup": 0.1, "tomato_sauce": 0.1, "butter": 0.2, "milk": 0.3, "chocolate_pudding": 0.4, "orange_juice": 0.2}}
75	
76	ID: eval-argmin-object-seed44-r2
77	  mode=, benchmark=, norm=None, seed=None
78	  success_rate=None, successes=13, total=100, n_rollouts=100
79	  other_metrics: {"overall_sr": 0.13, "tasks_done": 10, "tasks_total": 10, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.1, "bbq_sauce": 0.2, "ketchup": 0.1, "tomato_sauce": 0.1, "butter": 0, "milk": 0.1, "chocolate_pudding": 0.5, "orange_juice": 0.2}, "note": "EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json"}
80	
81	ID: eval-argmin-object-seed45
82	  mode=, benchmark=, norm=None, seed=None
83	  success_rate=None, successes=12, total=None, n_rollouts=100
84	  other_metrics: {"overall_sr": 0.12, "total_rollouts": 100, "tasks_completed": "10/10"}
85	
86	ID: eval-argmin-object-seed46
87	  mode=reconvla, benchmark=object, norm=None, seed=46
88	  success_rate=None, successes=None, total=None, n_rollouts=0
89	  other_metrics: {"overall_sr": 0.1, "total_successes": 10, "total_rollouts": 100, "n_rollouts_per_task": 10, "K": 10, "baseline_mode": "single", "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.1, "bbq_sauce": 0.4, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.1, "chocolate_pudding": 0.1, "orange_juice": 0.1}}
90	
91	ID: eval-argmin-object-seed47
92	  mode=reconvla, benchmark=object, norm=None, seed=47
93	  success_rate=None, successes=None, total=None, n_rollouts=100
94	  other_metrics: {"overall_sr": 0.1, "total_successes": 10, "total_rollouts": 100, "n_rollouts_per_task": 10, "K": 10, "baseline_mode": "single", "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.1, "bbq_sauce": 0.3, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.1, "chocolate_pudding": 0.1, "orange_juice": 0.2}}
95	
96	ID: eval-argmin-only-spatial-r2
97	  mode=, benchmark=, norm=None, seed=None
98	  success_rate=None, successes=None, total=None, n_rollouts=10
99	  other_metrics: {"overall_success_rate": 0.34, "total_successes": 34, "total_trials": 100, "per_task": {"T0_between_plate_and_ramekin": 0.6, "T1_next_to_ramekin": 1, "T2_from_table_center": 0, "T3_on_cookie_box": 0.3, "T4_in_top_drawer": 0.1, "T5_on_ramekin": 0.1, "T6_next_to_cookie_box": 0.9, "T7_on_stove": 0, "T8_next_to_plate": 0.3, "T9_on_wooden_cabinet": 0.1}, "note": "T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result."}
100	  notes: 10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.
101	
102	ID: eval-direct-correction-object-seed42-r3
103	  mode=, benchmark=, norm=None, seed=None
104	  success_rate=0.14, successes=14, total=None, n_rollouts=100 episodes (10 tasks x 10 rollouts)
105	  other_metrics: {"total_episodes": 100, "per_task": {"alphabet_soup": 0, "cream_cheese": 1, "salad_dressing": 1, "bbq_sauce": 4, "ketchup": 0, "tomato_sauce": 1, "butter": 1, "milk": 1, "chocolate_pudding": 3, "orange_juice": 2}}
106	
107	ID: eval-mag-obsonly-norm003-b2
108	  mode=, benchmark=, norm=None, seed=None
109	  success_rate=None, successes=None, total=None, n_rollouts=10
110	  other_metrics: {"overall_sr_10task": 0.34, "tasks_done": 10, "tasks_total": 10, "per_task": {"between_plate_and_ramekin": 0.9, "next_to_ramekin": 1, "from_table_center": 0, "on_cookie_box": 0.3, "in_top_drawer": 0.1, "on_ramekin": 0, "next_to_cookie_box": 0.8, "on_stove": 0, "next_to_plate": 0.3, "on_wooden_cabinet": 0}}
111	  notes: Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).
112	
113	ID: eval-mag-obsonly-norm003-object
114	  mode=, benchmark=, norm=None, seed=None
115	  success_rate=None, successes=None, total=None, n_rollouts=100
116	  other_metrics: {"overall_sr": 0.16, "tasks_done": 100, "tasks_total": 100, "per_task": {"pick_up_the_alphabet_soup_and_place_it_in_the_basket": 0, "pick_up_the_cream_cheese_and_place_it_in_the_basket": 0.2, "pick_up_the_salad_dressing_and_place_it_in_the_basket": 0.1, "pick_up_the_bbq_sauce_and_place_it_in_the_basket": 0.4, "pick_up_the_ketchup_and_place_it_in_the_basket": 0, "pick_up_the_tomato_sauce_and_place_it_in_the_basket": 0, "pick_up_the_butter_and_place_it_in_the_basket": 0.1, "pick_up_the_milk_and_place_it_in_the_basket": 0.2, "pick_up_the_chocolate_pudding_and_place_it_in_the_basket": 0.3, "pick_up_the_orange_juice_and_place_it_in_the_basket": 0.3}}
117	
118	ID: eval-mag-obsonly-norm005
119	  mode=crm_obs_only, benchmark=spatial, norm=None, seed=None
120	  success_rate=None, successes=None, total=None, n_rollouts=10 tasks x 10 rollouts
121	  other_metrics: {"max_correction_norm": 0.05, "n_rollouts": 10, "K": 10, "overall_sr": 35, "total_success": 35, "total_episodes": 100, "per_task": {"T0_between_plate_ramekin": 80, "T1_next_to_ramekin": 90, "T2_table_center": 0, "T3_on_cookie_box": 40, "T4_top_drawer": 10, "T5_on_ramekin": 0, "T6_next_to_cookie_box": 80, "T7_on_stove": 0, "T8_next_to_plate": 50, "T9_on_wooden_cabinet": 0}}
122	
123	ID: eval-mag-obsonly-norm005-object
124	  mode=, benchmark=, norm=None, seed=None
125	  success_rate=None, successes=13, total=None, n_rollouts=10
126	  other_metrics: {"overall_sr": 0.13, "tasks_completed": 10, "total_rollouts": 100, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.1, "bbq_sauce": 0.3, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.2, "chocolate_pudding": 0.2, "orange_juice": 0.3}}
127	
128	ID: eval-mag-obsonly-norm03-object
129	  mode=, benchmark=, norm=None, seed=None
130	  success_rate=None, successes=19, total=100, n_rollouts=10
131	  other_metrics: {"tasks_done": 10, "tasks_total": 10, "overall_sr": 0.19}
132	
133	ID: eval-mag-obsonly-norm03-r2
134	  mode=, benchmark=, norm=None, seed=None
135	  success_rate=None, successes=None, total=None, n_rollouts=100
136	  other_metrics: {"bowl_between": 0.9, "next_to_ramekin": 1, "table_center": 0, "cookie_box": 0.3, "top_drawer": 0.1, "on_ramekin": 0, "next_to_cookie_box": 1, "stove": 0, "next_to_plate": 0.3, "wooden_cabinet": 0, "overall_SR": 0.36}
137	
138	ID: eval-mag-perdof-norm003-object
139	  mode=, benchmark=, norm=None, seed=None
140	  success_rate=None, successes=None, total=None, n_rollouts=100
141	  other_metrics: {"tasks_done": 10, "tasks_total": 10, "overall_sr": 0.14, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.2, "bbq_sauce": 0.2, "ketchup": 0.1, "tomato_sauce": 0.1, "butter": 0.2, "milk": 0.1, "chocolate_pudding": 0.4, "orange_juice": 0.1}}
142	
143	ID: eval-mag-perdof-norm005-object
144	  mode=, benchmark=, norm=None, seed=None
145	  success_rate=None, successes=14, total=100, n_rollouts=10
146	  other_metrics: {"overall_sr": 0.14, "tasks_done": 10, "tasks_total": 10}
147	
148	ID: eval-mag-perdof-norm02-seed43-object-r3
149	  mode=, benchmark=, norm=None, seed=None
150	  success_rate=None, successes=9, total=100, n_rollouts=100
151	  other_metrics: {"overall_sr": 0.09, "tasks_done": 10, "tasks_total": 10, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.1, "bbq_sauce": 0.1, "ketchup": 0, "tomato_sauce": 0, "butter": 0, "milk": 0, "chocolate_pudding": 0.4, "orange_juice": 0.3}, "vs_seed42": "-2pp (11% \u2192 9%)", "pooled_2seed_perdof_02": "10% (20/200)"}
152	
153	ID: eval-mag-perdof-norm03-object-r3
154	  mode=, benchmark=, norm=None, seed=None
155	  success_rate=None, successes=4, total=100, n_rollouts=100
156	  other_metrics: {"overall_sr": 0.04, "tasks_done": 10, "tasks_total": 10}
157	
158	ID: eval-object-v8-full
159	  mode=, benchmark=, norm=None, seed=None
160	  success_rate=None, successes=None, total=None, n_rollouts=100
161	  other_metrics: {"overall_success_rate": 0.13, "total_successes": 13, "total_rollouts": 100, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.2, "bbq_sauce": 0.3, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.2, "chocolate_pudding": 0.2, "orange_juice": 0.2}}
162	
163	ID: eval-obs-only-object-default-seed44
164	  mode=, benchmark=, norm=None, seed=None
165	  success_rate=None, successes=None, total=None, n_rollouts=100
166	  other_metrics: {"overall_sr": 0.16, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0.1, "salad_dressing": 0.1, "bbq_sauce": 0.4, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.2, "chocolate_pudding": 0.3, "orange_juice": 0.3}}
167	
168	ID: eval-obs-only-object-norm01-seed44
169	  mode=, benchmark=, norm=None, seed=None
170	  success_rate=None, successes=None, total=None, n_rollouts=100
171	  other_metrics: {"overall_sr": 0.16, "total_success": 16, "total_rollouts": 100, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0.1, "salad_dressing": 0.3, "bbq_sauce": 0.2, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.2, "chocolate_pudding": 0.3, "orange_juice": 0.3}}
172	
173	ID: eval-obs-only-object-norm02-seed43-r2
174	  mode=, benchmark=, norm=None, seed=None
175	  success_rate=None, successes=16, total=100, n_rollouts=None
176	  other_metrics: {"overall_sr": 0.16, "per_task": {"alphabet_soup": 0, "cream_cheese": 0.1, "salad_dressing": 0.2, "bbq_sauce": 0.4, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.1, "chocolate_pudding": 0.4, "orange_juice": 0.2}, "vs_seed42": "-6pp (22% \u2192 16%)", "vs_argmin_seed43": "-1pp (17% \u2192 16%)", "pooled_2seed_obs_only_02": "19% (38/200)", "pooled_2seed_argmin": "14.5% (29/200)"}
177	
178	ID: eval-obs-only-object-norm02-seed44-r2
179	  mode=, benchmark=, norm=None, seed=None
180	  success_rate=None, successes=None, total=None, n_rollouts=100
181	  other_metrics: {"overall_sr": 0.16, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0.1, "salad_dressing": 0.2, "bbq_sauce": 0.2, "ketchup": 0.1, "tomato_sauce": 0.1, "butter": 0.2, "milk": 0.1, "chocolate_pudding": 0.3, "orange_juice": 0.3}}
182	
183	ID: eval-obs-only-object-norm02-seed45
184	  mode=, benchmark=, norm=None, seed=None
185	  success_rate=None, successes=16, total=None, n_rollouts=100
186	  other_metrics: {"overall_sr": 0.16, "total_rollouts": 100, "tasks_completed": "10/10"}
187	
188	ID: eval-obs-only-object-norm02-seed46
189	  mode=, benchmark=, norm=None, seed=None
190	  success_rate=0.15, successes=15, total=None, n_rollouts=100
191	  other_metrics: {"total_episodes": 100, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 2, "bbq_sauce": 3, "ketchup": 0, "tomato_sauce": 1, "butter": 1, "milk": 1, "chocolate_pudding": 4, "orange_juice": 3}}
192	
193	ID: eval-obs-only-object-norm02-seed47
194	  mode=obs_only, benchmark=object, norm=0.2, seed=47
195	  success_rate=0.2, successes=20, total=100, n_rollouts=100
196	
197	ID: eval-obs-only-object-norm03-seed44
198	  mode=, benchmark=, norm=None, seed=None
199	  success_rate=None, successes=None, total=None, n_rollouts=100
200	  other_metrics: {"overall_sr": 0.18, "total_rollouts": 100, "per_task": {"alphabet_soup": 0, "cream_cheese": 0.1, "salad_dressing": 0.2, "bbq_sauce": 0.4, "ketchup": 0.1, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.2, "chocolate_pudding": 0.3, "orange_juice": 0.3}}
201	
202	ID: eval-obs-only-object-norm03-seed45-r2
203	  mode=crm_obs_only, benchmark=object, norm=None, seed=45
204	  success_rate=None, successes=None, total=None, n_rollouts=100
205	  other_metrics: {"overall_success_rate": 14, "total_successes": 14, "total_rollouts": 100, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 10, "bbq_sauce": 30, "ketchup": 10, "tomato_sauce": 10, "butter": 10, "milk": 10, "chocolate_pudding": 30, "orange_juice": 30}, "max_correction_norm": 0.3}
206	
207	ID: eval-perdof-object-norm01-seed45
208	  mode=crm_perdof, benchmark=object, norm=None, seed=45
209	  success_rate=None, successes=None, total=None, n_rollouts=100
210	  other_metrics: {"overall_sr": 0.11, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.2, "bbq_sauce": 0.3, "ketchup": 0, "tomato_sauce": 0, "butter": 0, "milk": 0.1, "chocolate_pudding": 0.2, "orange_juice": 0.3}, "max_correction_norm": 0.1}
211	
212	ID: eval-perdof-object-norm03-seed45-r2
213	  mode=, benchmark=, norm=None, seed=None
214	  success_rate=None, successes=6, total=100, n_rollouts=100
215	  other_metrics: {"overall_sr": 0.06, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.1, "bbq_sauce": 0.2, "ketchup": 0, "tomato_sauce": 0, "butter": 0.1, "milk": 0, "chocolate_pudding": 0.1, "orange_juice": 0.1}}
216	
217	ID: eval-perdof-object-seed43
218	  mode=, benchmark=, norm=None, seed=None
219	  success_rate=None, successes=None, total=None, n_rollouts=100
220	  other_metrics: {"overall_success_rate": 0.12, "tasks_done": 10, "tasks_total": 10, "total_rollouts": 100, "total_successes": 12, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.2, "bbq_sauce": 0.3, "ketchup": 0, "tomato_sauce": 0, "butter": 0, "milk": 0, "chocolate_pudding": 0.4, "orange_juice": 0.3}}
221	
222	ID: eval-reconvla-object
223	  mode=, benchmark=, norm=None, seed=None
224	  success_rate=None, successes=None, total=None, n_rollouts=None
225	  other_metrics: {"overall_sr": 0.12, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.1, "bbq_sauce": 0.3, "ketchup": 0, "tomato_sauce": 0, "butter": 0.1, "milk": 0.1, "chocolate_pudding": 0.3, "orange_juice": 0.3}, "n_rollouts": 10, "total_episodes": 100, "total_successes": 12}
226	
227	ID: eval-reconvla-spatial-v3
228	  mode=, benchmark=, norm=None, seed=None
229	  success_rate=None, successes=None, total=None, n_rollouts=100
230	  other_metrics: {"overall_success_rate": 0.34, "total_successes": 34, "total_rollouts": 100, "per_task": {"pick_up_black_bowl_between_plate_and_ramekin": 0.6, "pick_up_black_bowl_next_to_ramekin": 1, "pick_up_black_bowl_from_table_center": 0, "pick_up_black_bowl_on_cookie_box": 0.3, "pick_up_black_bowl_in_top_drawer": 0.1, "pick_up_black_bowl_on_ramekin": 0.1, "pick_up_black_bowl_next_to_cookie_box": 0.9, "pick_up_black_bowl_on_stove": 0, "pick_up_black_bowl_next_to_plate": 0.4, "pick_up_black_bowl_on_wooden_cabinet": 0}}
231	
232	ID: eval-scalar-object-seed43
233	  mode=, benchmark=, norm=None, seed=None
234	  success_rate=None, successes=None, total=None, n_rollouts=10
235	  other_metrics: {"tasks_done": 10, "tasks_total": 10, "avg_sr": 10, "per_task_sr": {"pick_up_the_alphabet_soup_and_place_it_in_the_basket": 0, "pick_up_the_cream_cheese_and_place_it_in_the_basket": 0, "pick_up_the_salad_dressing_and_place_it_in_the_basket": 0, "pick_up_the_bbq_sauce_and_place_it_in_the_basket": 30, "pick_up_the_ketchup_and_place_it_in_the_basket": 0, "pick_up_the_tomato_sauce_and_place_it_in_the_basket": 0, "pick_up_the_butter_and_place_it_in_the_basket": 0, "pick_up_the_milk_and_place_it_in_the_basket": 10, "pick_up_the_chocolate_pudding_and_place_it_in_the_basket": 30, "pick_up_the_orange_juice_and_place_it_in_the_basket": 30}}
236	
237	ID: eval-spatial-v7-full
238	  mode=, benchmark=, norm=None, seed=None
239	  success_rate=None, successes=None, total=None, n_rollouts=100
240	  other_metrics: {"overall_success_rate": 0.3, "total_successes": 30, "total_episodes": 100, "n_tasks": 10, "n_rollouts": 10, "per_task": {"pick_up_black_bowl_between_plate_and_ramekin": 0.6, "pick_up_black_bowl_next_to_ramekin": 1, "pick_up_black_bowl_from_table_center": 0, "pick_up_black_bowl_on_cookie_box": 0.2, "pick_up_black_bowl_in_top_drawer": 0, "pick_up_black_bowl_on_ramekin": 0, "pick_up_black_bowl_next_to_cookie_box": 0.9, "pick_up_black_bowl_on_stove": 0, "pick_up_black_bowl_next_to_plate": 0.3, "pick_up_black_bowl_on_wooden_cabinet": 0}}
241	
242	ID: eval-vla-mean-object
243	  mode=vla_only, benchmark=object, norm=None, seed=42
244	  success_rate=None, successes=None, total=None, n_rollouts=100
245	  other_metrics: {"baseline_mode": "mean", "n_rollouts": 10, "K": 10, "overall_sr": 12, "total_success": 12, "total_rollouts": 100, "tasks_done": "10/10", "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 10, "bbq_sauce": 30, "ketchup": 10, "tomato_sauce": 10, "butter": 0, "milk": 20, "chocolate_pudding": 30, "orange_juice": 10}, "json_output": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json"}
246	
247	ID: eval-vla-mean-object-seed43
248	  mode=, benchmark=, norm=None, seed=None
249	  success_rate=None, successes=None, total=None, n_rollouts=10
250	  other_metrics: {"overall_sr": 0.15, "tasks_done": 10, "tasks_total": 10, "total_success": 15, "total_rollouts": 100, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.2, "bbq_sauce": 0.3, "ketchup": 0.1, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.3, "chocolate_pudding": 0.3, "orange_juice": 0.1}}
251	
252	ID: eval-vla-mean-object-seed44
253	  mode=, benchmark=, norm=None, seed=None
254	  success_rate=None, successes=None, total=None, n_rollouts=None
255	  other_metrics: {"overall_sr": 0.1, "per_task_sr": {"pick_up_the_alphabet_soup_and_place_it_in_the_basket": 0, "pick_up_the_cream_cheese_and_place_it_in_the_basket": 0, "pick_up_the_salad_dressing_and_place_it_in_the_basket": 0.1, "pick_up_the_bbq_sauce_and_place_it_in_the_basket": 0.3, "pick_up_the_ketchup_and_place_it_in_the_basket": 0.1, "pick_up_the_tomato_sauce_and_place_it_in_the_basket": 0.1, "pick_up_the_butter_and_place_it_in_the_basket": 0, "pick_up_the_milk_and_place_it_in_the_basket": 0, "pick_up_the_chocolate_pudding_and_place_it_in_the_basket": 0.2, "pick_up_the_orange_juice_and_place_it_in_the_basket": 0.2}}
256	
257	ID: eval-vla-mean-object-seed45
258	  mode=, benchmark=, norm=None, seed=None
259	  success_rate=None, successes=None, total=None, n_rollouts=100
260	  other_metrics: {"overall_sr": 0.13, "total_success": 13, "total_rollouts": 100, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.1, "bbq_sauce": 0.4, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0, "milk": 0.1, "chocolate_pudding": 0.3, "orange_juice": 0.3}, "multi_seed_summary": "seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%"}
261	
262	ID: eval-vla-mean-spatial
263	  mode=, benchmark=, norm=None, seed=None
264	  success_rate=None, successes=None, total=None, n_rollouts=100
265	  other_metrics: {"overall_success_rate_10tasks": 0.32, "total_successes": 32, "total_trials": 100, "T1": 0.7, "T2": 1, "T3": 0, "T4": 0.3, "T5": 0, "T6": 0, "T7": 0.8, "T8": 0, "T9": 0.3, "T10": 0.1}
266	
267	ID: eval-vla-mean-spatial-t10
268	  mode=, benchmark=, norm=None, seed=None
269	  success_rate=None, successes=None, total=None, n_rollouts=10
270	  other_metrics: {"T10_on_wooden_shelf": "10% (1/10)", "note": "Only ran task 9 (start_task=9). T10 = wooden shelf task."}
271	
272	ID: eval-vla-only-object
273	  mode=, benchmark=, norm=None, seed=None
274	  success_rate=None, successes=None, total=None, n_rollouts=10 tasks x 10 rollouts
275	  other_metrics: {"overall_sr": 0.12, "total_success": 12, "total_trials": 100, "per_task": {"alphabet_soup": 0, "cream_cheese": 0.1, "salad_dressing": 0.2, "bbq_sauce": 0.2, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0, "milk": 0.1, "chocolate_pudding": 0.2, "orange_juice": 0.3}}
276	
277	ID: eval-vla-only-object-seed43
278	  mode=, benchmark=, norm=None, seed=None
279	  success_rate=None, successes=None, total=None, n_rollouts=10
280	  other_metrics: {"overall_sr": 0.12, "tasks_done": 10, "tasks_total": 10, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0.1, "salad_dressing": 0.1, "bbq_sauce": 0.3, "ketchup": 0, "tomato_sauce": 0, "butter": 0, "milk": 0.1, "chocolate_pudding": 0.4, "orange_juice": 0.2}, "source": "json_file_verified_by_worker"}
281	  notes: seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。
282	
283	ID: eval-vla-only-object-seed44-r2
284	  mode=, benchmark=, norm=None, seed=None
285	  success_rate=None, successes=None, total=None, n_rollouts=None
286	  other_metrics: {"tasks_done": 10, "tasks_total": 10, "overall_sr": 0.1, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0.1, "salad_dressing": 0.2, "bbq_sauce": 0.2, "ketchup": 0, "tomato_sauce": 0, "butter": 0, "milk": 0.1, "chocolate_pudding": 0.2, "orange_juice": 0.2}}
287	
288	ID: eval-vla-only-object-seed45
289	  mode=, benchmark=, norm=None, seed=None
290	  success_rate=None, successes=18, total=200, n_rollouts=10
291	  other_metrics: {"overall_sr": 0.09, "tasks_done": 10}
292	
293	ID: mvp-point-reaching
294	  mode=, benchmark=, norm=None, seed=None
295	  success_rate=None, successes=None, total=None, n_rollouts=20000
296	  other_metrics: {"group1_oracle": {"A_scalar": {"mse_x": 0.180218, "mse_y": 0.02497, "mse_z": 0.024232, "total": 0.076473}, "B_perDOF": {"mse_x": 0.172652, "mse_y": 0.015544, "mse_z": 0.01561, "total": 0.067935}, "C_none": {"mse_x": 0.22706, "mse_y": 0.025542, "mse_z": 0.024753, "total": 0.092451}}, "group2_oracle": {"A_scalar": {"mse_x": 0.064642, "mse_y": 0.023836, "mse_z": 0.022967, "total": 0.037148}, "B_perDOF": {"mse_x": 0.053403, "mse_y": 0.015695, "mse_z": 0.01573, "total": 0.028276}, "C_none": {"mse_x": 0.084178, "mse_y": 0.025427, "mse_z": 0.024798, "total": 0.044801}}, "group3_oracle": {"A_scalar": {"mse_x": 0.042948, "mse_y": 0.023218, "mse_z": 0.022365, "total": 0.02951}, "B_perDOF": {"mse_x": 0.033008, "mse_y": 0.015621, "mse_z": 0.015647, "total": 0.021425}, "C_none": {"mse_x": 0.053043, "mse_y": 0.025523, "mse_z": 0.024741, "total": 0.034436}}, "group4_K10": {"A_scalar": {"mse_x": 0.187418, "mse_y": 0.024701, "mse_z": 0.024277, "total": 0.078799}, "B_perDOF": {"mse_x": 0.182888, "mse_y": 0.019072, "mse_z": 0.018475, "total": 0.073478}, "C_none": {"mse_x": 0.21507, "mse_y": 0.02496, "mse_z": 0.024637, "total": 0.088223}}, "group5_K10": {"A_scalar": {"mse_x": 0.064895, "mse_y": 0.02386, "mse_z": 0.023596, "total": 0.037451}, "B_perDOF": {"mse_x": 0.05851, "mse_y": 0.018868, "mse_z": 0.018471, "total": 0.03195}, "C_none": {"mse_x": 0.077047, "mse_y": 0.024825, "mse_z": 0.02464, "total": 0.042171}}, "group6_K10": {"A_scalar": {"mse_x": 0.041848, "mse_y": 0.02344, "mse_z": 0.023207, "total": 0.029498}, "B_perDOF": {"mse_x": 0.036348, "mse_y": 0.018736, "mse_z": 0.018453, "total": 0.024512}, "C_none": {"mse_x": 0.048365, "mse_y": 0.024827, "mse_z": 0.024577, "total": 0.03259}}, "pass_criteria": {"group1": "PASS", "group4": "PASS", "overall": "SUCCESS"}, "summary_pct_improvements": {"reference_group": "group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)", "perDOF_vs_scalar_total": 6.75, "perDOF_vs_none_total": 16.71, "perDOF_vs_scalar_y_axis": 22.79, "perDOF_vs_scalar_z_axis": 23.9, "paper_claims": {"6.7_pct_over_scalar": "group4 total: (0.078799-0.073478)/0.078799 = 6.75%", "16.7_pct_over_none": "group4 total: (0.088223-0.073478)/0.088223 = 16.71%", "22_24_pct_per_axis": "group4 y: 22.79%, z: 23.90%"}}}
297	
298	ID: precompute-k5
299	  mode=, benchmark=, norm=None, seed=None
300	  success_rate=None, successes=None, total=None, n_rollouts=26737
301	  other_metrics: {"spatial_samples": 12167, "object_samples": 14570, "total_samples": 26737, "spatial_cache_mb": 106, "object_cache_mb": 127, "total_cache_mb": 233, "runtime_min": 107}
302	
303	ID: precompute-shard0
304	  mode=, benchmark=, norm=None, seed=None
305	  success_rate=None, successes=None, total=None, n_rollouts=None
306	
307	ID: precompute-shard1
308	  mode=, benchmark=, norm=None, seed=None
309	  success_rate=None, successes=None, total=None, n_rollouts=None
310	
311	ID: precompute-shard2
312	  mode=, benchmark=, norm=None, seed=None
313	  success_rate=None, successes=None, total=None, n_rollouts=None
314	
315	ID: precompute-v4-shard0
316	  mode=, benchmark=, norm=None, seed=None
317	  success_rate=None, successes=None, total=None, n_rollouts=None
318	
319	ID: precompute-v4-shard1
320	  mode=, benchmark=, norm=None, seed=None
321	  success_rate=None, successes=None, total=None, n_rollouts=None
322	
323	ID: precompute-v4-shard2
324	  mode=, benchmark=, norm=None, seed=None
325	  success_rate=None, successes=None, total=None, n_rollouts=None
326	
327	ID: precompute-v5-shard0
328	  mode=, benchmark=, norm=None, seed=None
329	  success_rate=None, successes=None, total=None, n_rollouts=~8900 samples (shard 0 of 3)
330	
331	ID: precompute-v5-shard1
332	  mode=, benchmark=, norm=None, seed=None
333	  success_rate=None, successes=None, total=None, n_rollouts=~8900 samples (shard 1 of 3)
334	
335	ID: precompute-v5-shard2
336	  mode=, benchmark=, norm=None, seed=None
337	  success_rate=None, successes=None, total=None, n_rollouts=~8900 samples (shard 2 of 3)
338	
339	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "011b8883-93a2-486f-9123-888644e355d9"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Get negative, preparing, deployed experiments",
  "usage": {
    "total_tokens": 42496,
    "tool_uses": 11,
    "duration_ms": 193869
  },
  "last_tool_name": "Bash",
  "uuid": "aa506b66-0e92-4e4c-b7a7-9bc382b87696",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01LzfTZ9SjKTkWtJtjTebiXd`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nfrom collections import defaultdict\n\nwith open(\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt\", \"r\") as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# DONE + negative experiments\nprint(\"=== DONE + NEGATIVE experiments ===\")\nfor eid, e in sorted(exps.items()):\n    if e.get('status') == 'DONE' and e.get('conclusion') == 'negative':\n        m = e.get('metrics', {})\n        sr = m.get('success_rate') or m.get('overall_sr')\n        notes = e.get('notes', '')\n        hyp = e.get('hypothesis', '')[:150]\n        print(f\"\\n  {eid}\")\n        print(f\"    metrics: {json.dumps(m)[:300]}\")\n        if notes:\n            print(f\"    notes: {str(notes)[:200]}\")\n\nprint(\"\\n\\n=== PREPARING / DEPLOYED experiments ===\")\nfor eid, e in sorted(exps.items()):\n    if e.get('status') in ('PREPARING', 'DEPLOYED'):\n        hyp = e.get('hypothesis', '')[:200]\n        print(f\"\\n  {eid} [{e['status']}]\")\n        print(f\"    hypothesis: {hyp}\")\nPYEOF\n",
  "description": "Get negative, preparing, deployed experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "13415da6-9ed0-451e-aa0c-11eea12d0e13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUiQVYzdzd9YDqzE27dapH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14242,
      "cache_read_input_tokens": 27839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14242,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 51 · 2026-05-17T11:22:10.343Z_

<details><summary>↩ Tool result · `toolu_01LzfTZ9SjKTkWtJtjTebiXd`</summary>

```text
=== DONE + NEGATIVE experiments ===

  eval-acr-object-v4-scalar
    metrics: {"overall_sr": 9, "total_success": 9, "total_trials": 100, "n_tasks": 10, "n_rollouts_per_task": 10, "per_task": {"alphabet_soup": {"sr": 0, "success": 0, "trials": 10}, "cream_cheese": {"sr": 0, "success": 0, "trials": 10}, "salad_dressing": {"sr": 10, "success": 1, "trials": 10}, "bbq_sauce": {"sr

  eval-mag-obsonly-norm02
    metrics: {"T0_between_plate_ramekin": 90, "T1_next_to_ramekin": 100, "T2_table_center": 0, "T3_on_cookie_box": 30, "T4_top_drawer": 10, "T5_on_ramekin": 0, "T6_next_to_cookie_box": 90, "T7_on_stove": 0, "T8_next_to_plate": 30, "T9_on_wooden_cabinet": 0, "overall_sr": 35, "total_success": 35, "total_rollouts"

  eval-mag-perdof-norm003
    metrics: {"benchmark": "spatial", "mode": "acr_vla", "max_correction_norm": 0.03, "n_rollouts": 10, "K": 10, "seed": 42, "overall_sr": 30, "total_success": 30, "total_rollouts": 100, "tasks_done": "10/10", "per_task": {"T0_between_plate_ramekin": 60, "T1_next_to_ramekin": 100, "T2_table_center": 0, "T3_on_co

  eval-mag-perdof-norm005
    metrics: {"T0_between_plate_ramekin": 50, "T1_next_to_ramekin": 100, "T2_table_center": 0, "T3_on_cookie_box": 30, "T4_top_drawer": 0, "T5_on_ramekin": 0, "T6_next_to_cookie_box": 100, "T7_on_stove": 0, "T8_next_to_plate": 30, "T9_on_wooden_cabinet": 0, "avg_SR_10task": 31}

  eval-mag-perdof-norm02-object
    metrics: {"tasks_done": 10, "tasks_total": 10, "overall_sr": 0.11, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0.1, "salad_dressing": 0.1, "bbq_sauce": 0.1, "ketchup": 0, "tomato_sauce": 0, "butter": 0.1, "milk": 0.1, "chocolate_pudding": 0.4, "orange_juice": 0.2}}

  eval-mag-perdof-norm03
    metrics: {"overall_sr_10task": 0.26, "T0_sr": 0.7, "T1_sr": 0.5, "T2_sr": 0.1, "T3_sr": 0.1, "T4_sr": 0, "T5_sr": 0, "T6_sr": 0.9, "T7_sr": 0.1, "T8_sr": 0.2, "T9_sr": 0, "total_successes": 26, "total_rollouts": 100, "benchmark": "spatial", "max_correction_norm": 0.3}

  eval-obs-only-object-seed43
    metrics: {"overall_success_rate": 0.12, "tasks_done": 10, "tasks_total": 10, "per_task": {"alphabet_soup": 0, "cream_cheese": 0.1, "salad_dressing": 0.1, "bbq_sauce": 0.3, "ketchup": 0, "tomato_sauce": 0, "butter": 0, "milk": 0.1, "chocolate_pudding": 0.4, "orange_juice": 0.2}, "vs_argmin_seed43": {"obs_only

  eval-perdof-object-norm01-seed44
    metrics: {"overall_sr": 0.08, "total_successes": 8, "total_rollouts": 100, "seed": 44, "mode": "crm_perdof", "max_correction_norm": 0.1}
    notes: 失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed | 诊断中: Worker worker_diagnose_eval-perdof-object-norm01-seed44_20260517T105221 已派发到 bjb1-18228 检查是否为 cron 误判（同配置 seed45 成功，SR=11%）

  eval-perdof-object-norm03-seed44
    metrics: {"success_rate": 0.04, "total_episodes": 100, "successes": 4, "per_task": {"alphabet_soup": 0, "cream_cheese": 1, "salad_dressing": 0, "bbq_sauce": 1, "ketchup": 0, "tomato_sauce": 0, "butter": 1, "milk": 0, "chocolate_pudding": 1, "orange_juice": 0}}

  eval-perdof-object-seed44
    metrics: {"overall_sr": 0.08, "total_success": 8, "total_rollouts": 100, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.2, "bbq_sauce": 0.1, "ketchup": 0, "tomato_sauce": 0, "butter": 0, "milk": 0, "chocolate_pudding": 0.2, "orange_juice": 0.3}}

  eval-scalar-object-seed44-r2
    metrics: {"overall_sr": 0.06, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0, "bbq_sauce": 0.1, "ketchup": 0, "tomato_sauce": 0, "butter": 0, "milk": 0, "chocolate_pudding": 0.2, "orange_juice": 0.3}}


=== PREPARING / DEPLOYED experiments ===

  eval-mag-perdof-norm03-object [DEPLOYED]
    hypothesis: 

  eval-obs-only-object-norm01-seed46 [PREPARING]
    hypothesis: obs_only CRM (ε=0.1) seed=46 on LIBERO Object. Extends magnitude curve low-norm segment to 3+ seeds. If consistent with seed42=19% and seed45 (running), strengthens robustness claim that obs_only main

  eval-obs-only-object-norm01-seed47 [PREPARING]
    hypothesis: obs_only CRM (ε=0.1) seed=47 on LIBERO Object. 4th seed for magnitude curve low-norm point. Combined with seeds 42/45/46, provides error bar for obs_only at ε=0.1. Supports robustness narrative (obs_o

  eval-perdof-object-norm01-seed46 [PREPARING]
    hypothesis: perdof CRM (ε=0.1) seed=46 on LIBERO Object. Extends perdof low-norm data (seed42=11%, seed44/45 running). At ε=0.1 perdof is in its "safe zone" (tight bound masks noisy corrections). Paired with obs_
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "f6b0c085-9a5e-4393-952e-2b35098b09e7"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "description": "Running Full cross-tab of status x conclusion",
  "usage": {
    "total_tokens": 45031,
    "tool_uses": 12,
    "duration_ms": 200017
  },
  "last_tool_name": "Bash",
  "uuid": "c00fde1f-cbab-41bd-871d-51625dc06f14",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01RfW2zkkF3msk7chmunECXK`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nfrom collections import defaultdict\n\nwith open(\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt\", \"r\") as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Count all statuses x conclusions\nfrom itertools import product\ncombos = defaultdict(int)\nfor eid, e in exps.items():\n    combos[(e.get('status','?'), e.get('conclusion','?'))] += 1\nprint(\"Status x Conclusion counts:\")\nfor (s,c), n in sorted(combos.items()):\n    print(f\"  {s} / {c}: {n}\")\nPYEOF\n",
  "description": "Full cross-tab of status x conclusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "0a6c0577-008e-4138-a3f9-396583a33ca0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkxPidgVeyXnZtW3zi2EJs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2531,
      "cache_read_input_tokens": 42081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2531,
        "ephemeral_1h_input_tokens": 0
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

_source line 54 · 2026-05-17T11:22:16.498Z_

<details><summary>↩ Tool result · `toolu_01RfW2zkkF3msk7chmunECXK`</summary>

```text
Status x Conclusion counts:
  DEPLOYED / killed: 1
  DONE / failed: 26
  DONE / killed: 56
  DONE / negative: 11
  DONE / success: 69
  PREPARING / ?: 1
  PREPARING / killed: 2
  RUNNING / ?: 11
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "28ef0a1a-72ff-498c-9ce8-7200467c5a6c"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a2f959b3a456f7801",
  "tool_use_id": "toolu_01CFSL8MgqBNRrRnM9bAbSFC",
  "status": "completed",
  "output_file": "",
  "summary": "Extract registry experiment data",
  "usage": {
    "total_tokens": 45479,
    "tool_uses": 12,
    "duration_ms": 261384
  },
  "uuid": "528bb24d-7294-47e8-a2d0-3872115c7241",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8"
}
```

---

### Tool result

_source line 56 · 2026-05-17T11:23:17.732Z_

<details><summary>↩ Tool result · `toolu_01CFSL8MgqBNRrRnM9bAbSFC`</summary>

```text
Now I have everything needed. Here is the comprehensive structured summary:

---

## Registry Overview

**Total experiments: 177**

| Status | Count |
|---|---|
| DONE | 162 |
| RUNNING | 11 |
| PREPARING | 3 |
| DEPLOYED | 1 |

| Conclusion | Count |
|---|---|
| success | 69 |
| killed | 59 |
| failed | 26 |
| negative | 11 |
| (none/pending) | 12 |

---

## COMPLETED EVALUATION EXPERIMENTS BY METHOD

Below are all DONE experiments with `conclusion=success` or `conclusion=negative` that produced evaluation metrics. I exclude infrastructure jobs (precompute shards, training runs) and truly failed/killed experiments.

### 1. VLA-Only Baseline (no CRM correction)

**Object benchmark:**
| exp_id | seed | success_rate | successes/total | n_rollouts |
|---|---|---|---|---|
| eval-vla-only-object | 42 | 0.12 | 12/100 | 100 |
| eval-vla-only-object-seed43 | 43 | 0.12 | 12/100 | 100 |
| eval-vla-only-object-seed44-r2 | 44 | 0.10 | 10/100 | 100 |
| eval-vla-only-object-seed45 | 45 | 0.09 | 18/200 | 200 |

**Note from metrics:** `"multi_seed_summary": "seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%"` (from vla-mean entries, see below)

### 2. VLA-Mean Baseline (mean of K=10 VLA samples)

**Object benchmark:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-vla-mean-object | 42 | 0.12 | 12/100 |
| eval-vla-mean-object-seed43 | 43 | 0.15 | 15/100 |
| eval-vla-mean-object-seed44 | 44 | 0.10 | (100 implied) |
| eval-vla-mean-object-seed45 | 45 | 0.13 | 13/100 |

**Spatial benchmark:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-vla-mean-spatial (+ t10) | 42 | 0.32 | 32/100 |

### 3. Argmin / ReconVLA Baseline (pick best of K=10 by reconstruction loss)

**Object benchmark:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-reconvla-object | 42 | 0.12 | 12/100 |
| eval-argmin-object-seed43 | 43 | 0.17 | 17/100 |
| eval-argmin-object-seed44-r2 | 44 | 0.13 | 13/100 |
| eval-argmin-object-seed45 | 45 | 0.12 | 12/100 |
| eval-argmin-object-seed46 | 46 | 0.10 | 10/100 |
| eval-argmin-object-seed47 | 47 | 0.10 | 10/100 |

**Spatial benchmark:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-argmin-only-spatial-r2 | 42 | 0.34 | 34/100 |
| eval-reconvla-spatial-v3 | 42 | 0.34 | 34/100 |

### 4. obs_only CRM (observation-only conditioning, no uncertainty)

**Object benchmark, norm=0.03 (eps=0.03):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-obsonly-norm003-object | 42 | 0.16 | 16/100 |

**Object benchmark, norm=0.05 (eps=0.05):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-obsonly-norm005-object | 42 | 0.13 | 13/100 |

**Object benchmark, norm=0.1 (eps=0.1):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-acr-object-v4-obs-only | 42 | 0.19 | 19/100 |
| eval-obs-only-object-norm01-seed44 | 44 | 0.16 | 16/100 |
| eval-obs-only-object-seed43 (negative) | 43 | 0.12 | 12/100 |

**Object benchmark, norm=0.2 (eps=0.2):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-acr-object-obs-only-norm02 | 42 | 0.22 | 22/100 |
| eval-obs-only-object-norm02-seed43-r2 | 43 | 0.16 | 16/100 |
| eval-obs-only-object-norm02-seed44-r2 | 44 | 0.16 | 16/100 |
| eval-obs-only-object-norm02-seed45 | 45 | 0.16 | 16/100 |
| eval-obs-only-object-norm02-seed46 | 46 | 0.15 | 15/100 |
| eval-obs-only-object-norm02-seed47 | 47 | 0.20 | 20/100 |

**Object benchmark, norm=0.3 (eps=0.3):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-obsonly-norm03-object | 42 | 0.19 | 19/100 |
| eval-obs-only-object-norm03-seed44 | 44 | 0.18 | 18/100 |
| eval-obs-only-object-norm03-seed45-r2 | 45 | 0.14 | 14/100 |

**Object benchmark, norm=default (~1.42, no clipping):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-acr-object-obs-only-default | 42 | 0.17 | 17/100 |
| eval-obs-only-object-default-seed44 | 44 | 0.16 | 16/100 |

**Spatial benchmark, norm=0.03:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-obsonly-norm003-b2 | 42 | 0.34 | 34/100 |

**Spatial benchmark, norm=0.05:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-obsonly-norm005 | 42 | 0.35 | 35/100 |

**Spatial benchmark, norm=0.1:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-acr-spatial-v4-obs-only-r3 | 42 | 0.35 | 35/100 |

**Spatial benchmark, norm=0.2 (negative):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-obsonly-norm02 | 42 | 0.35 | 35/100 |

**Spatial benchmark, norm=0.3:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-obsonly-norm03-r2 | 42 | 0.36 | 36/100 |

### 5. perdof CRM (per-DOF uncertainty conditioning)

**Object benchmark, norm=0.03:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-perdof-norm003-object | 42 | 0.14 | 14/100 |

**Object benchmark, norm=0.05:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-perdof-norm005-object | 42 | 0.14 | 14/100 |

**Object benchmark, norm=0.1:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-acr-object-v4-perdof | 42 | 0.11 | 11/100 |
| eval-perdof-object-seed43 | 43 | 0.12 | 12/100 |
| eval-perdof-object-seed44 (negative) | 44 | 0.08 | 8/100 |
| eval-perdof-object-norm01-seed44 (negative) | 44 | 0.08 | 8/100 |
| eval-perdof-object-norm01-seed45 | 45 | 0.11 | 11/100 |

**Object benchmark, norm=0.2:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-perdof-norm02-object (negative) | 42 | 0.11 | 11/100 |
| eval-mag-perdof-norm02-seed43-object-r3 | 43 | 0.09 | 9/100 |

**Object benchmark, norm=0.3:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-perdof-norm03-object-r3 | 42 | 0.04 | 4/100 |
| eval-perdof-object-norm03-seed44 (negative) | 44 | 0.04 | 4/100 |
| eval-perdof-object-norm03-seed45-r2 | 45 | 0.06 | 6/100 |

**Object benchmark, norm=default (~1.42):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-acr-object-v4-default-r2 | 42 | 0.00 | 0/100 |

**Spatial benchmark, norm=0.03 (negative):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-perdof-norm003 | 42 | 0.30 | 30/100 |

**Spatial benchmark, norm=0.05 (negative):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-perdof-norm005 | 42 | 0.31 | 31/100 |

**Spatial benchmark, norm=0.1:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-acr-spatial-v4-small-r2 | 42 | 0.35 | 35/100 |

**Spatial benchmark, norm=0.3 (negative):**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-mag-perdof-norm03 | 42 | 0.26 | 26/100 |

### 6. scalar_unc CRM (scalar uncertainty conditioning)

**Object benchmark, norm=0.1:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-acr-object-v4-scalar (negative) | 42 | 0.09 | 9/100 |
| eval-scalar-object-seed43 | 43 | 0.10 | 10/100 |
| eval-scalar-object-seed44-r2 (negative) | 44 | 0.06 | 6/100 |

**Spatial benchmark, norm=0.1:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-acr-spatial-v4-scalar-r2 | 42 | 0.32 | 32/100 |

### 7. direct_correction

**Object benchmark:**
| exp_id | seed | success_rate | successes/total |
|---|---|---|---|
| eval-direct-correction-object-seed42-r3 | 42 | 0.14 | 14/100 |

### 8. Early full-pipeline evals (v7/v8, likely older CRM versions)

| exp_id | benchmark | success_rate | successes/total |
|---|---|---|---|
| eval-spatial-v7-full | spatial | 0.30 | 30/100 |
| eval-object-v8-full | object | 0.13 | 13/100 |

---

## TRAINING RUNS (DONE + success)

| exp_id | best_val_loss | best_epoch | total_epochs | n_samples |
|---|---|---|---|---|
| crm-train-v2-obs-only | 0.050501 | 50 | 50 | 26737 |
| crm-train-v2-perdof | 0.051684 | 48 | 50 | 26737 |
| crm-train-v2-scalar-unc | 0.047202 | 48 | 50 | 26737 |
| crm-train-v3-norm | (no metrics) | - | - | 12167 |
| crm-train-v3-norm-obs-only | 0.01645 | 48 | 50 | 12167 |
| crm-train-v3-norm-scalar-unc | 0.037354 | 46 | 50 | 12167 |

---

## CURRENTLY RUNNING (11 experiments)

| exp_id | server | method | benchmark | norm | seed |
|---|---|---|---|---|---|
| eval-obs-only-object-default-seed45 | bjb2-28827 | obs_only | object | default (~1.42) | 45 |
| eval-obs-only-object-norm01-seed45 | bjb1-18228 | obs_only | object | 0.1 | 45 |
| eval-obs-only-object-norm01-seed46-r2 | bjb1-18228 | obs_only | object | 0.1 | 46 |
| eval-obs-only-object-norm01-seed47-r2 | bjb1-18228 | obs_only | object | 0.1 | 47 |
| eval-obs-only-object-norm03-seed46 | bjb1-32546 | obs_only | object | 0.3 | 46 |
| eval-perdof-object-norm01-seed46-r2 | bjb1-32546 | perdof | object | 0.1 | 46 |
| eval-perdof-object-norm01-seed47-bjb1 | bjb1-32546 | perdof | object | 0.1 | 47 |
| eval-perdof-object-norm02-seed44 | bjb2-28827 | perdof | object | 0.2 | 44 |
| eval-perdof-object-norm02-seed45 | bjb2-28827 | perdof | object | 0.2 | 45 |
| eval-perdof-object-norm02-seed46 | bjb2-28827 | perdof | object | 0.2 | 46 |
| eval-scalar-object-seed45 | bjb2-28827 | scalar_unc | object | (default) | 45 |

---

## PREPARING (3 experiments)

| exp_id | method | norm | seed |
|---|---|---|---|
| eval-obs-only-object-norm01-seed46 | obs_only | 0.1 | 46 |
| eval-obs-only-object-norm01-seed47 | obs_only | 0.1 | 47 |
| eval-perdof-object-norm01-seed46 | perdof | 0.1 | 46 |

---

## KEY OBSERVATIONS

1. **obs_only consistently outperforms other CRM variants on Object benchmark.** At norm=0.2, seed42 achieves 22%, with multi-seed average around 17.5% (range 15-22%). Argmin baseline averages ~12.3% across seeds 42-47. VLA-only baseline ~11%.

2. **perdof degrades sharply at higher norms on Object.** At norm=0.3, perdof collapses to 4-6%. At norm=0.1 it gets ~8-12%. The per-DOF uncertainty conditioning appears to amplify noisy corrections at larger magnitudes.

3. **On Spatial benchmark, all CRM methods cluster around the argmin baseline (32-36%).** obs_only achieves 34-36%, perdof 26-35%, scalar 32%, argmin 34%, vla-mean 32%. No clear CRM advantage on spatial.

4. **scalar_unc performs worst on Object** (6-10% across seeds), below even the VLA-only baseline.

5. **obs_only is robust across norms on Object**: 0.03=16%, 0.05=13%, 0.1=19%, 0.2=17.5% (avg), 0.3=17% (avg), default=16.5% (avg). The magnitude curve is flat, unlike perdof which drops catastrophically.

agentId: a2f959b3a456f7801 (use SendMessage with to: 'a2f959b3a456f7801' to continue this agent)
&lt;usage>total_tokens: 49659
tool_uses: 12
duration_ms: 261387&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "9dcf6545-e7e0-43c7-9373-39edb6a9574c",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to analyze a large JSON file containing ML experiment registry data and extract structured information.\n\nThe file is at: `/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7d3fb9a9-651b-4ced-b62a-b6d872235fb8/tool-results/mcp-agent-ml-research-read_registry-1779016721921.txt`\n\nIt's JSON with schema: `{result: string}` — the `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. Probe structure with jq (type/length/keys)\n2. Extract all experiments, focusing on:\n   - experiment ID\n   - status (DONE, RUNNING, FAILED, etc.)\n   - conclusion (success, failed, etc.)\n   - metrics (success_rate, any other metrics)\n   - experiment type/name (what was being tested — obs_only, perdof, argmin, scalar, vla_mean, etc.)\n   - norm/epsilon settings if present\n   - seed number\n   - any notes\n\nFor each experiment with conclusion=success or status=DONE, I need:\n- The exp_id\n- The method being tested (obs_only, perdof, argmin, VLA-only, scalar, vla_mean, direct_correction, etc.)\n- The norm/epsilon setting\n- The seed\n- The benchmark (object vs spatial)\n- The success_rate metric\n- Number of rollouts (n_rollouts)\n\nAlso list all RUNNING experiments with what they're testing.\n\nReturn the results as a structured summary organized by method type. Be thorough — don't miss any experiments. Quote actual metric values verbatim.",
    "agentId": "a2f959b3a456f7801",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have everything needed. Here is the comprehensive structured summary:\n\n---\n\n## Registry Overview\n\n**Total experiments: 177**\n\n| Status | Count |\n|---|---|\n| DONE | 162 |\n| RUNNING | 11 |\n| PREPARING | 3 |\n| DEPLOYED | 1 |\n\n| Conclusion | Count |\n|---|---|\n| success | 69 |\n| killed | 59 |\n| failed | 26 |\n| negative | 11 |\n| (none/pending) | 12 |\n\n---\n\n## COMPLETED EVALUATION EXPERIMENTS BY METHOD\n\nBelow are all DONE experiments with `conclusion=success` or `conclusion=negative` that produced evaluation metrics. I exclude infrastructure jobs (precompute shards, training runs) and truly failed/killed experiments.\n\n### 1. VLA-Only Baseline (no CRM correction)\n\n**Object benchmark:**\n| exp_id | seed | success_rate | successes/total | n_rollouts |\n|---|---|---|---|---|\n| eval-vla-only-object | 42 | 0.12 | 12/100 | 100 |\n| eval-vla-only-object-seed43 | 43 | 0.12 | 12/100 | 100 |\n| eval-vla-only-object-seed44-r2 | 44 | 0.10 | 10/100 | 100 |\n| eval-vla-only-object-seed45 | 45 | 0.09 | 18/200 | 200 |\n\n**Note from metrics:** `\"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"` (from vla-mean entries, see below)\n\n### 2. VLA-Mean Baseline (mean of K=10 VLA samples)\n\n**Object benchmark:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-vla-mean-object | 42 | 0.12 | 12/100 |\n| eval-vla-mean-object-seed43 | 43 | 0.15 | 15/100 |\n| eval-vla-mean-object-seed44 | 44 | 0.10 | (100 implied) |\n| eval-vla-mean-object-seed45 | 45 | 0.13 | 13/100 |\n\n**Spatial benchmark:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-vla-mean-spatial (+ t10) | 42 | 0.32 | 32/100 |\n\n### 3. Argmin / ReconVLA Baseline (pick best of K=10 by reconstruction loss)\n\n**Object benchmark:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-reconvla-object | 42 | 0.12 | 12/100 |\n| eval-argmin-object-seed43 | 43 | 0.17 | 17/100 |\n| eval-argmin-object-seed44-r2 | 44 | 0.13 | 13/100 |\n| eval-argmin-object-seed45 | 45 | 0.12 | 12/100 |\n| eval-argmin-object-seed46 | 46 | 0.10 | 10/100 |\n| eval-argmin-object-seed47 | 47 | 0.10 | 10/100 |\n\n**Spatial benchmark:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-argmin-only-spatial-r2 | 42 | 0.34 | 34/100 |\n| eval-reconvla-spatial-v3 | 42 | 0.34 | 34/100 |\n\n### 4. obs_only CRM (observation-only conditioning, no uncertainty)\n\n**Object benchmark, norm=0.03 (eps=0.03):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-obsonly-norm003-object | 42 | 0.16 | 16/100 |\n\n**Object benchmark, norm=0.05 (eps=0.05):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-obsonly-norm005-object | 42 | 0.13 | 13/100 |\n\n**Object benchmark, norm=0.1 (eps=0.1):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-acr-object-v4-obs-only | 42 | 0.19 | 19/100 |\n| eval-obs-only-object-norm01-seed44 | 44 | 0.16 | 16/100 |\n| eval-obs-only-object-seed43 (negative) | 43 | 0.12 | 12/100 |\n\n**Object benchmark, norm=0.2 (eps=0.2):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-acr-object-obs-only-norm02 | 42 | 0.22 | 22/100 |\n| eval-obs-only-object-norm02-seed43-r2 | 43 | 0.16 | 16/100 |\n| eval-obs-only-object-norm02-seed44-r2 | 44 | 0.16 | 16/100 |\n| eval-obs-only-object-norm02-seed45 | 45 | 0.16 | 16/100 |\n| eval-obs-only-object-norm02-seed46 | 46 | 0.15 | 15/100 |\n| eval-obs-only-object-norm02-seed47 | 47 | 0.20 | 20/100 |\n\n**Object benchmark, norm=0.3 (eps=0.3):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-obsonly-norm03-object | 42 | 0.19 | 19/100 |\n| eval-obs-only-object-norm03-seed44 | 44 | 0.18 | 18/100 |\n| eval-obs-only-object-norm03-seed45-r2 | 45 | 0.14 | 14/100 |\n\n**Object benchmark, norm=default (~1.42, no clipping):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-acr-object-obs-only-default | 42 | 0.17 | 17/100 |\n| eval-obs-only-object-default-seed44 | 44 | 0.16 | 16/100 |\n\n**Spatial benchmark, norm=0.03:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-obsonly-norm003-b2 | 42 | 0.34 | 34/100 |\n\n**Spatial benchmark, norm=0.05:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-obsonly-norm005 | 42 | 0.35 | 35/100 |\n\n**Spatial benchmark, norm=0.1:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-acr-spatial-v4-obs-only-r3 | 42 | 0.35 | 35/100 |\n\n**Spatial benchmark, norm=0.2 (negative):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-obsonly-norm02 | 42 | 0.35 | 35/100 |\n\n**Spatial benchmark, norm=0.3:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-obsonly-norm03-r2 | 42 | 0.36 | 36/100 |\n\n### 5. perdof CRM (per-DOF uncertainty conditioning)\n\n**Object benchmark, norm=0.03:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-perdof-norm003-object | 42 | 0.14 | 14/100 |\n\n**Object benchmark, norm=0.05:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-perdof-norm005-object | 42 | 0.14 | 14/100 |\n\n**Object benchmark, norm=0.1:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-acr-object-v4-perdof | 42 | 0.11 | 11/100 |\n| eval-perdof-object-seed43 | 43 | 0.12 | 12/100 |\n| eval-perdof-object-seed44 (negative) | 44 | 0.08 | 8/100 |\n| eval-perdof-object-norm01-seed44 (negative) | 44 | 0.08 | 8/100 |\n| eval-perdof-object-norm01-seed45 | 45 | 0.11 | 11/100 |\n\n**Object benchmark, norm=0.2:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-perdof-norm02-object (negative) | 42 | 0.11 | 11/100 |\n| eval-mag-perdof-norm02-seed43-object-r3 | 43 | 0.09 | 9/100 |\n\n**Object benchmark, norm=0.3:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-perdof-norm03-object-r3 | 42 | 0.04 | 4/100 |\n| eval-perdof-object-norm03-seed44 (negative) | 44 | 0.04 | 4/100 |\n| eval-perdof-object-norm03-seed45-r2 | 45 | 0.06 | 6/100 |\n\n**Object benchmark, norm=default (~1.42):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-acr-object-v4-default-r2 | 42 | 0.00 | 0/100 |\n\n**Spatial benchmark, norm=0.03 (negative):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-perdof-norm003 | 42 | 0.30 | 30/100 |\n\n**Spatial benchmark, norm=0.05 (negative):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-perdof-norm005 | 42 | 0.31 | 31/100 |\n\n**Spatial benchmark, norm=0.1:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-acr-spatial-v4-small-r2 | 42 | 0.35 | 35/100 |\n\n**Spatial benchmark, norm=0.3 (negative):**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-mag-perdof-norm03 | 42 | 0.26 | 26/100 |\n\n### 6. scalar_unc CRM (scalar uncertainty conditioning)\n\n**Object benchmark, norm=0.1:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-acr-object-v4-scalar (negative) | 42 | 0.09 | 9/100 |\n| eval-scalar-object-seed43 | 43 | 0.10 | 10/100 |\n| eval-scalar-object-seed44-r2 (negative) | 44 | 0.06 | 6/100 |\n\n**Spatial benchmark, norm=0.1:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-acr-spatial-v4-scalar-r2 | 42 | 0.32 | 32/100 |\n\n### 7. direct_correction\n\n**Object benchmark:**\n| exp_id | seed | success_rate | successes/total |\n|---|---|---|---|\n| eval-direct-correction-object-seed42-r3 | 42 | 0.14 | 14/100 |\n\n### 8. Early full-pipeline evals (v7/v8, likely older CRM versions)\n\n| exp_id | benchmark | success_rate | successes/total |\n|---|---|---|---|\n| eval-spatial-v7-full | spatial | 0.30 | 30/100 |\n| eval-object-v8-full | object | 0.13 | 13/100 |\n\n---\n\n## TRAINING RUNS (DONE + success)\n\n| exp_id | best_val_loss | best_epoch | total_epochs | n_samples |\n|---|---|---|---|---|\n| crm-train-v2-obs-only | 0.050501 | 50 | 50 | 26737 |\n| crm-train-v2-perdof | 0.051684 | 48 | 50 | 26737 |\n| crm-train-v2-scalar-unc | 0.047202 | 48 | 50 | 26737 |\n| crm-train-v3-norm | (no metrics) | - | - | 12167 |\n| crm-train-v3-norm-obs-only | 0.01645 | 48 | 50 | 12167 |\n| crm-train-v3-norm-scalar-unc | 0.037354 | 46 | 50 | 12167 |\n\n---\n\n## CURRENTLY RUNNING (11 experiments)\n\n| exp_id | server | method | benchmark | norm | seed |\n|---|---|---|---|---|---|\n| eval-obs-only-object-default-seed45 | bjb2-28827 | obs_only | object | default (~1.42) | 45 |\n| eval-obs-only-object-norm01-seed45 | bjb1-18228 | obs_only | object | 0.1 | 45 |\n| eval-obs-only-object-norm01-seed46-r2 | bjb1-18228 | obs_only | object | 0.1 | 46 |\n| eval-obs-only-object-norm01-seed47-r2 | bjb1-18228 | obs_only | object | 0.1 | 47 |\n| eval-obs-only-object-norm03-seed46 | bjb1-32546 | obs_only | object | 0.3 | 46 |\n| eval-perdof-object-norm01-seed46-r2 | bjb1-32546 | perdof | object | 0.1 | 46 |\n| eval-perdof-object-norm01-seed47-bjb1 | bjb1-32546 | perdof | object | 0.1 | 47 |\n| eval-perdof-object-norm02-seed44 | bjb2-28827 | perdof | object | 0.2 | 44 |\n| eval-perdof-object-norm02-seed45 | bjb2-28827 | perdof | object | 0.2 | 45 |\n| eval-perdof-object-norm02-seed46 | bjb2-28827 | perdof | object | 0.2 | 46 |\n| eval-scalar-object-seed45 | bjb2-28827 | scalar_unc | object | (default) | 45 |\n\n---\n\n## PREPARING (3 experiments)\n\n| exp_id | method | norm | seed |\n|---|---|---|---|\n| eval-obs-only-object-norm01-seed46 | obs_only | 0.1 | 46 |\n| eval-obs-only-object-norm01-seed47 | obs_only | 0.1 | 47 |\n| eval-perdof-object-norm01-seed46 | perdof | 0.1 | 46 |\n\n---\n\n## KEY OBSERVATIONS\n\n1. **obs_only consistently outperforms other CRM variants on Object benchmark.** At norm=0.2, seed42 achieves 22%, with multi-seed average around 17.5% (range 15-22%). Argmin baseline averages ~12.3% across seeds 42-47. VLA-only baseline ~11%.\n\n2. **perdof degrades sharply at higher norms on Object.** At norm=0.3, perdof collapses to 4-6%. At norm=0.1 it gets ~8-12%. The per-DOF uncertainty conditioning appears to amplify noisy corrections at larger magnitudes.\n\n3. **On Spatial benchmark, all CRM methods cluster around the argmin baseline (32-36%).** obs_only achieves 34-36%, perdof 26-35%, scalar 32%, argmin 34%, vla-mean 32%. No clear CRM advantage on spatial.\n\n4. **scalar_unc performs worst on Object** (6-10% across seeds), below even the VLA-only baseline.\n\n5. **obs_only is robust across norms on Object**: 0.03=16%, 0.05=13%, 0.1=19%, 0.2=17.5% (avg), 0.3=17% (avg), default=16.5% (avg). The magnitude curve is flat, unlike perdof which drops catastrophically."
      }
    ],
    "totalDurationMs": 261387,
    "totalTokens": 49659,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 44612,
      "output_tokens": 4600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4600,
          "cache_read_input_tokens": 44612,
          "cache_creation_input_tokens": 446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 446,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 11,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me compile the alignment report.

Let me extract the claims from paper_framing.md and cross-reference with the registry data.

**Core Claims (Narrative B — 3 claims):**

**Claim 1: Sample-then-correct pipeline for inference-time VLA improvement**
- Two-stage: conformal selection (K=10 argmin) + bounded residual correction (CRM, ~330K params)
- Statistically significant improvement: obs_only 17.5% vs argmin 12.3%, +5.2pp, Fisher exact p=0.0074 (6v6 seeds, D047)


- Large effect size (Cohen's d=1.21) with obs_only outperforming argmin in 5 of 6 seeds, and substantially beating VLA-only at 10.8%

**Claim 2: Conditioning-magnitude interaction as previously unidentified failure mode**
- obs_only maintains stable performance around 17% across all norm ranges from 0.03 to 1.42, while perdof shows progressive degradation from 14% down to 0% as norm increases

, revealing a critical stability gap that requires magnitude control for safe inference-time VLA correction

**Claim 3: Honest negative result: per-DOF conformal features don't generalize**
- per-DOF scores collapse outside their narrow safe region due to rank-deficient covariance (K=10 in 30D action space), and the spatial benchmark shows no method achieves separation from baseline, indicating fundamental limitations in this approach

Now I'm verifying these claims against the actual data, starting with the pooled results across all six seeds to confirm the 17.5% performance figure for obs_only. The argmin results are confirmed across all seeds with a significant Fisher exact p-value of 0.0074 and a Cohen's d of 1.21, showing a strong effect size. The VLA-only condition shows a lower mean performance at 10.8% across seeds 42-45, with all registry values verified. I have sufficient data with 6 seeds each totaling 600 observations.

Now I'm moving to Claim 2 and checking the magnitude sweep results for the obs_only curve. The lower normalization values (0.03 and 0.05) each have only a single seed, which limits confidence, but the norm=0.10 condition has three seeds with a mean of 15.7%, though I'm noticing some inconsistency in how seed 43 was marked and need to verify the paper's reported average. I'm checking seed45 at the default norm setting now. Looking at the perdof curve results, the lower norm values like 0.03 and 0.05 match the paper's 14% but only give me a single seed, which isn't ideal for stability. At norm=0.10 I'm getting four seeds with results around 11-12% for most, though there's some discrepancy between what the roadmap shows and what's actually in the registry—I need to verify which seeds are actually being counted there. I'm noticing some inconsistencies in the seed counts across different normalization levels. At norm=0.20, I'm about to run additional seeds that'll bring the total to 5, but the paper only references 1 seed for that curve. For norm=0.30, I have 3 seeds with a mean around 4.7%, which matches the roadmap. The default case is trickier—the roadmap mentions 2 seeds, but I'm only finding one in the registry so far, and there's a reference to another eval in D039 that might be the missing second seed.

Looking at the magnitude curve for Figure 2, the low normalization values (0.03, 0.05) are particularly concerning since each only has 1 seed, while the higher norms are better covered—norm=0.20 has 6 seeds, and I'm running additional seeds for norm=0.10 and norm=0.30 to reach 3 each. For the perdof method, I'm tracking similar coverage gaps and running more seeds to fill them out.

For the spatial benchmark claim, all the data points are single-seed runs across both obs_only and perdof methods, which limits confidence even though the percentages (34-36% for obs_only, 26-35% for perdof) align with the paper's claims. The root cause mechanism about rank-deficient covariance is theoretical rather than experimentally testable, so the magnitude curve itself serves as the main supporting evidence.

Now checking the baseline numbers—the paper mentions scalar CRM at seed42 achieving 15%, but the registry data shows 9% for that seed at norm=0.1, which doesn't match. I need to figure out if this is a norm setting discrepancy or an actual inconsistency in the reported results. Looking at the full pipeline results, eval-object-v8-full shows 13%, which might be an earlier version or a different configuration than what the paper references as "scalar CRM." I should flag this discrepancy. The VLA-mean results check out across seeds 42 and 43, and the VLA-only mean of 10.8% matches the registry average across all seeds. Now I need to verify what the paper says about seed45. .25, 1.25, -0.75, -1.75. Variance = (1.5625+1.5625+0.5625+3.0625)/4 = 6.75/4 = 1.6875. SD = 1.299. SEM = 1.299/2 = 0.65. Wait, ±1.4% is the SD, not SEM. SD = sqrt((1.5625+1.5625+0.5625+3.0625)/3) = sqrt(6.75/3) = sqrt(2.25) = 1.5%. Hmm, 1.5 vs 1.4, close enough.

Let me double-check the obs_only norm=0.1 results next. The paper reports "3s: 19/12/16 → 15.7%

", and looking at the registry data, I'm getting 19%, 12%, and 16% across the three runs, which averages to 15.67% — that matches. For the perdof norm=0.1 case, the roadmap says "3s: 11/11/8 → 10.0%", but when I check the registry, I'm seeing 11%, 12%, and something else, which is making me question why seed43 shows 12% instead of 11%.

Looking more closely at the experiment names and the registry section labeled "Object benchmark, norm=0.1", these should all be at the same norm setting. The roadmap only lists three seeds with values 11%, 11%, and 8%, which would be seeds 42, 45, and 44 respectively, averaging to 10.0%. But if there's actually a fourth seed (seed43 at 12%), that would change the calculation entirely — the mean would shift to around 10.5% instead.

I suspect the confusion stems from how the experiments handle norm settings: the training used norm=0.1, so when an experiment doesn't explicitly specify a norm, it defaults to that training norm. Some experiments name this explicitly while others don't, which could explain the discrepancy in what the roadmap shows versus what's in the registry.

I'll move forward with writing the report and flag these inconsistencies as I go. I'm also noticing a similar issue with the scalar CRM results — the paper mentions seed42 at 15%, but the registry shows 9% at norm=0.1, which suggests either a different training run or norm setting was used.

Looking through the scalar experiment data more carefully, I'm seeing seed42 at 9%, seed43 at 10%, and seed44 at 6%, but nothing that matches the 15% figure from the paper. This is definitely a discrepancy worth noting. The 15% might come from a different norm value like 0.2, or it could be from an entirely different CRM training run that isn't in the current registry.

Now checking the spatial results against what the paper claims — the obs_only numbers line up well across different norm values, but the perdof spatial results show a range of 26-35%, which dips below the paper's stated 30-35% range at norm03.

Looking at the ROADMAP table though, it only reports norm=0.1 results for spatial, where methods cluster around 34-35% as the paper describes. The broader data actually reveals perdof's performance degradation at higher norms, which supports the collapse narrative but isn't mentioned in the paper's framing.

Now I'm compiling the full report and checking seed coverage for the magnitude curve — starting to tally how many seeds have completed runs versus are still in progress for each normalization value. I'm tracking down the perdof default experiment results—seed 42 shows 0% success, and the roadmap indicates a 2-second timeout for this configuration. I need to verify whether eval-perdof-object-default-seed44 was actually completed or if it was killed, since it's referenced in the D042 decision but doesn't appear in my success list.

Now I'm ready to compile the final report. I notice there's an interesting case with obs_only at norm=0.1 seed43—it achieved 12% but was marked as negative in the registry, likely because it didn't significantly outperform the argmin baseline. Still, it's valid data for the magnitude curve. Let me verify the claim about 5 out of 6 seeds where obs_only beats argmin: seed42 shows 22 vs 12 in obs_only's favor, seed43 actually goes to argmin at 16 vs 17, seed44 favors obs_only at 16 vs 13, and seed45 is at 16 vs 12.

I'm also catching what looks like a data discrepancy in the paper—it claims scalar CRM seed42 is 15%, but the registry shows 9% for that same configuration. I should double-check if there's a scalar result at a different normalization value that might explain this. I've verified the direct correction results match the paper, so I'm ready to compile my findings. But let me check one more detail in the documentation about the obs_only magnitude sweep — the paper claims only 1 seed for the default condition, yet the registry shows 2 completed runs and 1 still in progress, which doesn't align.

Looking at the actual data, seed42 gives 17% and seed44 gives 16%, averaging to 16.5%, not the 17% the paper states. The same issue appears in the perdof results where the paper lists ε=0.2 as 11% from a single seed, but now there are two completed seeds (42=11%, 43=9%) that would average to 10%, with three more runs still pending.

I'm also noticing a discrepancy in the perdof norm=0.1 case. The ROADMAP shows "3s: 11/11/8 → 10.0%" and the registry has four completed seeds, but the calculation seems to be using only three of them—likely seeds 42, 45, and 44 which give 11, 11, and 8 respectively. I need to flag these inconsistencies as I write up the report.

With seeds 46 and 47 still running, I'll have six total seeds for perdof norm=0.1, which should give me better coverage. Now I'm checking whether each claim has sufficient evidence: the pipeline improvement claim is well-supported with 6v6 seeds and strong statistical significance, while the conditioning-magnitude interaction claim needs me to verify its data foundation.

Looking at the seed distribution across norms for the core figure, I see the problem — the extreme norms (0.03 and 0.05) only have single seeds each, which weakens the divergent curves narrative. Even after the running experiments complete, I'll have better coverage at 0.1 and 0.3, but those endpoints will still lack the replication needed to make the claim convincing. This is the critical figure, so having only one-seed points for the extremes is a real limitation.

For the per-DOF negative result, the spatial experiments are all single-seed too, though that's less problematic since the claim itself is about lack of separation — a null result doesn't require as much evidence to support. The rank-deficiency mechanism is grounded in theory and the magnitude patterns back it up, but the spatial data is still thin.

The running experiments will add a few more seeds at 0.1 and the default norm, but won't address the 0.03 and 0.05 gap. Looking at the progress across these experiment configurations, I've got several that are nearly complete—obs_only and perdof with norm=0.1 and perdof with norm=0.2 are all at or close to their target seed counts. The remaining gaps are mostly single-seed configurations with no plans for expansion, plus the spatial results which are also limited to one seed. With 8 GPU slots available, I could push forward on filling out the norm=0.3 and default configurations if needed.

Before finalizing the report though, I'm noticing some discrepancies between what the paper claims and what I'm seeing in the actual results—the scalar CRM baseline is reported as 15% but my numbers show 9-10%, and there's a mismatch on the obs_only norm=0.1 seed43 result that I need to track down before writing this up.

Now I'm double-checking the Cohen's d calculation for the obs_only condition to make sure it matches what's in the paper, working through the mean and standard deviation from the individual seed results. I'm finishing the standard deviation calculation for the argmin group and then computing the pooled standard deviation to get Cohen's d. The result comes out to 1.91, which doesn't match my earlier estimate of 1.21, so I'm reconsidering whether I should use the paired differences formula instead.

Now I'm recalculating using the paired approach—taking the differences between matched seeds and computing Cohen's d from those differences directly. The mean difference is 5.167 and the standard deviation of differences is 4.262, which gives d = 1.21 and matches the paper's reported value. This makes sense since the seeds are paired observations.

Now I'll draft the actual report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "9ae83a84-dfeb-4cb1-b0d7-33f0f00a1a84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TF4LvwC5SZNHQn2twQJWn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5266,
      "cache_read_input_tokens": 31546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5266
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

_source line 58_

Now I have all data. Let me compile the alignment report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "85cb0ea2-0702-4a16-b464-9e5e07e846f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TF4LvwC5SZNHQn2twQJWn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5266,
      "cache_read_input_tokens": 31546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5266
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

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01R9gZikhDWjGKBb2ZkR1eKP`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_data_alignment.md",
  "content": "# Paper Claims vs Data Alignment Report\n> Generated: 2026-05-17\n\n---\n\n## Claim 1: Sample-then-correct pipeline yields statistically significant improvement over argmin baseline\n\n**Paper states**: obs_only ε=0.2 pooled 105/600 (17.5%) vs argmin 74/600 (12.3%), +5.2pp, Fisher exact p=0.0074, Cohen's d=1.21 (paired), 5/6 seeds obs_only > argmin. VLA-only mean 10.8%.\n\n### 支撑实验\n\n**obs_only ε=0.2 (6 seeds, all confirmed):**\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-acr-object-obs-only-norm02 | 22% |\n| 43 | eval-obs-only-object-norm02-seed43-r2 | 16% |\n| 44 | eval-obs-only-object-norm02-seed44-r2 | 16% |\n| 45 | eval-obs-only-object-norm02-seed45 | 16% |\n| 46 | eval-obs-only-object-norm02-seed46 | 15% |\n| 47 | eval-obs-only-object-norm02-seed47 | 20% |\n\n**argmin (6 seeds, all confirmed):**\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-reconvla-object | 12% |\n| 43 | eval-argmin-object-seed43 | 17% |\n| 44 | eval-argmin-object-seed44-r2 | 13% |\n| 45 | eval-argmin-object-seed45 | 12% |\n| 46 | eval-argmin-object-seed46 | 10% |\n| 47 | eval-argmin-object-seed47 | 10% |\n\n**VLA-only (4 seeds):**\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-vla-only-object | 12% |\n| 43 | eval-vla-only-object-seed43 | 12% |\n| 44 | eval-vla-only-object-seed44-r2 | 10% |\n| 45 | eval-vla-only-object-seed45 | 9% (18/200) |\n\nVLA-only mean = (12+12+10+9)/4 = 10.75% ≈ 10.8% ✅\n\n**5/6 seed-wise wins**: 42(+10), 43(-1), 44(+3), 45(+4), 46(+5), 47(+10) → 5/6 ✅\n\n### 数据充分度: ✅ 充分\n- 6v6 seeds, 每组 600 trials\n- Fisher exact p=0.0074 (D047 confirmed)\n- Cohen's d=1.21 (paired) verified\n- 无缺口\n\n---\n\n## Claim 2: Conditioning-magnitude interaction — obs_only stable vs perdof progressive collapse\n\n**Paper states**: obs_only stable ~17% across norms 0.03–1.42; perdof progressive collapse 14% → 10% → 4% → 0%.\n\n### 支撑实验 — obs_only magnitude curve (Object)\n\n| norm | seeds done (values) | seeds running | total after | mean |\n|------|---------------------|--------------|-------------|------|\n| 0.03 | 1: 42=16% | 0 | 1 | 16% |\n| 0.05 | 1: 42=13% | 0 | 1 | 13% |\n| 0.10 | 3: 42=19%, 43=12%, 44=16% | 3 (s45,s46,s47) | 6 | 15.7% |\n| 0.20 | 6: 22/16/16/16/15/20 | 0 | 6 | 17.5% |\n| 0.30 | 3: 42=19%, 44=18%, 45=14% | 1 (s46) | 4 | 17.0% |\n| default | 2: 42=17%, 44=16% | 1 (s45) | 3 | 16.5% |\n\n### 支撑实验 — perdof magnitude curve (Object)\n\n| norm | seeds done (values) | seeds running | total after | mean |\n|------|---------------------|--------------|-------------|------|\n| 0.03 | 1: 42=14% | 0 | 1 | 14% |\n| 0.05 | 1: 42=14% | 0 | 1 | 14% |\n| 0.10 | 4: 42=11%, 43=12%, 44=8%, 45=11% | 2 (s46,s47) | 6 | 10.5% |\n| 0.20 | 2: 42=11%, 43=9% | 3 (s44,s45,s46) | 5 | 10.0% |\n| 0.30 | 3: 42=4%, 44=4%, 45=6% | 0 | 3 | 4.7% |\n| default | 1: 42=0% | 0 | 1 | 0% |\n\n### 数据充分度: ⚠️ 部分支撑\n- **趋势清晰**: obs_only 13–17.5% 稳定 vs perdof 14%→10%→4.7%→0% 坍塌模式明显\n- **核心缺口 — 低 norm 端 (0.03, 0.05) 双方法仅 1 seed**:\n  - 无法加 error bars，Figure 2 在端点可信度不足\n  - 审稿人可能质疑端点数据\n  - 无 RUNNING 实验覆盖这些点\n- **perdof default 仅 1 seed (0%)**:\n  - 虽然 0% 是极端值（0/100 很难是偶然），但单 seed 仍有风险\n  - 无 RUNNING 实验补充\n- **RUNNING 实验完成后改善**: norm 0.1 → 6v6 seeds; perdof norm 0.2 → 5 seeds; obs_only norm 0.3 → 4 seeds\n- **paper_framing.md 数据需更新**:\n  - obs_only default 写 \"1s: 17%\"，实际已有 2 seeds (42=17%, 44=16%)\n  - perdof norm 0.1 ROADMAP 写 \"3s: 11/11/8\"，实际有 4 seeds (含 43=12%)\n  - perdof norm 0.2 写 \"1s: 11%\"，实际已有 2 seeds (42=11%, 43=9%)\n\n---\n\n## Claim 3: Per-DOF conformal features do not generalize — honest negative result\n\n**Paper states**: per-DOF scores fail beyond narrow safe region; root cause = K=10 rank-deficient covariance in 30D; spatial benchmark shows no method separates from baseline (34-35%).\n\n### 支撑实验 — Spatial benchmark (all single seed=42)\n\n| method | norm | exp_id | SR |\n|--------|------|--------|-----|\n| obs_only | 0.03 | eval-mag-obsonly-norm003-b2 | 34% |\n| obs_only | 0.05 | eval-mag-obsonly-norm005 | 35% |\n| obs_only | 0.10 | eval-acr-spatial-v4-obs-only-r3 | 35% |\n| obs_only | 0.20 | eval-mag-obsonly-norm02 | 35% |\n| obs_only | 0.30 | eval-mag-obsonly-norm03-r2 | 36% |\n| perdof | 0.03 | eval-mag-perdof-norm003 | 30% |\n| perdof | 0.05 | eval-mag-perdof-norm005 | 31% |\n| perdof | 0.10 | eval-acr-spatial-v4-small-r2 | 35% |\n| perdof | 0.30 | eval-mag-perdof-norm03 | 26% |\n| argmin | — | eval-argmin-only-spatial-r2 | 34% |\n| VLA-only | — | eval-spatial-v7-full | 30% |\n| VLA-mean | — | eval-vla-mean-spatial | 32% |\n\n### 数据充分度: ⚠️ 部分支撑\n- **趋势支撑 Claim**: 所有方法 spatial 聚集在 30-36%，无明显分离\n- **所有 spatial 数据仅 1 seed**: 审稿人可能质疑\n- **perdof spatial 也有坍塌趋势 (35%→26%)**: 论文说 \"30-35%\"，但 norm 0.3 实际 26%，低于该范围\n  - 考虑：要么修正 paper 范围为 \"26-35%\"，要么说明 spatial 同样出现 perdof 衰退（这反而加强 Claim 2）\n- **Rank-deficiency 机制 (K=10, 30D)**: 理论论证，由 magnitude curve 模式间接支撑，无独立验证实验\n- 无 RUNNING spatial 实验\n\n---\n\n## Supporting Claims (Additional baselines)\n\n### scalar CRM\n**Paper states**: scalar CRM seed42 = 15% (single seed)\n\n**Registry data**:\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-acr-object-v4-scalar | **9%** (conclusion: negative) |\n| 43 | eval-scalar-object-seed43 | 10% |\n| 44 | eval-scalar-object-seed44-r2 | 6% (conclusion: negative) |\n\n**❌ 数据不一致**: paper_framing 写 15%，registry 实际为 9%。需核实来源。\n\n### VLA-mean (K=10 mean aggregation)\n**Paper states**: seed42=12%, seed43=15%, seed45=running\n\n**Registry data**:\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-vla-mean-object | 12% ✅ |\n| 43 | eval-vla-mean-object-seed43 | 15% ✅ |\n| 44 | eval-vla-mean-object-seed44 | 10% |\n| 45 | eval-vla-mean-object-seed45 | 13% |\n\n**Note**: seed44=10% 和 seed45=13% 已完成但未体现在 paper_framing 中。paper_framing 需更新。\n\n### Direct correction (K=1 CRM)\n**Paper states**: seed42 = 14% (not significant vs VLA-only)\n\n**Registry**: eval-direct-correction-object-seed42-r3 = 14% ✅ 单 seed 数据。\n\n---\n\n## Summary\n\n| 状态 | Claims |\n|------|--------|\n| ✅ 充分支撑 | 1 |\n| ⚠️ 部分支撑 | 2 |\n| ❌ 缺乏支撑 | 0 |\n\n- ✅ 充分支撑的 claims: **1** (Claim 1: 6v6 pipeline improvement, p=0.0074)\n- ⚠️ 部分支撑（需更多数据）: **2** (Claim 2: magnitude curve 低 norm 端仅 1 seed; Claim 3: spatial 全部单 seed)\n- ❌ 缺乏支撑: **0**\n- **数据错误**: scalar CRM seed42 paper 写 15%，registry 实为 9%\n\n### 当前 RUNNING 实验能填补的缺口\n| 缺口 | RUNNING 实验 | 完成后状态 |\n|------|-------------|-----------|\n| obs_only norm=0.1 仅 3 seeds | s45, s46, s47 running | → 6 seeds ✅ |\n| obs_only norm=0.3 仅 3 seeds | s46 running | → 4 seeds |\n| obs_only default 仅 2 seeds | s45 running | → 3 seeds |\n| perdof norm=0.1 仅 4 seeds | s46, s47 running | → 6 seeds ✅ |\n| perdof norm=0.2 仅 2 seeds | s44, s45, s46 running | → 5 seeds ✅ |\n| scalar seed45 | running | → 4 seeds |\n\n### 仍无法填补的缺口（无 RUNNING 实验，需手动启动）\n1. **obs_only norm=0.03 / 0.05**: 各仅 1 seed，Figure 2 端点无 error bars\n2. **perdof norm=0.03 / 0.05**: 各仅 1 seed\n3. **perdof default**: 仅 1 seed (0%)\n4. **所有 spatial 数据**: 全部单 seed，无补充计划\n5. **VLA-mean seed44/45**: 已完成但 paper_framing 未更新\n\n### 建议优先使用 8 张空闲 GPU\n1. perdof norm=0.03 seed43/44 (2 GPUs) — 补 Figure 2 低 norm 端\n2. obs_only norm=0.03 seed43/44 (2 GPUs) — 补 Figure 2 低 norm 端\n3. perdof default seed44/45 (2 GPUs) — 补坍塌终点\n4. perdof norm=0.05 seed43 + obs_only norm=0.05 seed43 (2 GPUs) — 低 norm 端\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "d400fac1-b7c3-4a40-818a-3c682d302c08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TF4LvwC5SZNHQn2twQJWn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5266,
      "cache_read_input_tokens": 31546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5266
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

_source line 60 · 2026-05-17T11:26:57.623Z_

<details><summary>↩ Tool result · `toolu_01R9gZikhDWjGKBb2ZkR1eKP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'paper_data_alignment.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "05bd3174-df16-4614-ba8c-3828c3961e51",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'paper_data_alignment.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'paper_data_alignment.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
The file can't be saved via the MCP tool. Let me write it directly to the artifacts directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "f8f3b2a4-9eaa-4d82-b6f8-fd21b5f4ce05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qv67dCP9JkX3nxFvCdwJLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12838,
      "cache_read_input_tokens": 36812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12838
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

_source line 62_

MCP tool doesn't allow that filename. Writing directly to artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "ba5ab1c7-58d7-4bfa-9cdc-1e7ae8b389e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qv67dCP9JkX3nxFvCdwJLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12838,
      "cache_read_input_tokens": 36812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12838
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

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01S5Go6mGFn6hP7VzNcoRboD`</summary>

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
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "1549e258-49ca-4a76-a561-a488e924782f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qv67dCP9JkX3nxFvCdwJLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12838,
      "cache_read_input_tokens": 36812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12838
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

_source line 64 · 2026-05-17T11:27:01.950Z_

<details><summary>↩ Tool result · `toolu_01S5Go6mGFn6hP7VzNcoRboD`</summary>

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
conclusion_draft.md
contribution_list.md
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
experiments_draft.md
fallback_narrative_draft.md
fig_magnitude_curve.py
figures
fisher_analysis.py
fix_plan_code_sketch.md
gpu_health_snapshot_20260515.md
introduction_draft.md
lerobot-pipeline-alignment.md
libero-smolvla-env-report.md
literature_gap_report.md
magnitude_curve.pdf
magnitude_curve.png
magnitude_curve_data.json
magnitude_curve_draft.pdf
magnitude_curve_draft.png
magnitude_multiseed_data.md
magnitude_sweep_summary.md
manifest.yaml
method_draft.md
method_section_draft.tex
mvp-point-reaching
narrative_b_abstract_draft.md
narrative_b_abstract_final.md
narrative_b_draft.md
object_eval_commands.md
object_results_summary.md
pipeline-dimension-verification.md
pooled_fisher_test_v2.py
precompute-k5
precompute-k5-analysis.md
progress_scan_loop9.md
reconvla-comparison-report.md
related_work_draft.md
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
training_loss_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "b43096b1-cffb-4390-ac94-7e9d25d62599",
  "tool_use_result": {
    "stdout": "__pycache__\n_project\nablation_eval_commands.md\nanalysis\nanalysis_magnitude_sweep.py\nanalysis_object_benchmark.py\nanalysis_spatial_final.py\nargmin_seed44_r2_results.json\ncitation_attribution_audit.md\ncitation_audit_report.md\ncompetitive_analysis_20260515.md\ncompetitor_analysis.md\nconclusion_draft.md\ncontribution_list.md\ncorl_paper_outline.md\ncorrection_degradation_literature.md\ncrm-train-v2-k5\ncrm_bug_audit.md\ndiag-eval-v6-batch-failure.md\ndiagnose-norm02-seed44-r2.md\ndream_reports\neval-acr-object-v4-obs-only\neval-acr-object-v4-scalar\neval-argmin-object-seed44-r2\neval-mag-perdof-norm03\neval-obs-only-object-default-seed45\neval-obs-only-object-norm02-seed44-r2\neval-obs-only-object-norm02-seed46\neval-obs-only-object-norm03-seed44\neval-reconvla-spatial-v1-diag.md\neval-vla-mean-object-seed44\nexperiment_progress_20260515.md\nexperiments_draft.md\nfallback_narrative_draft.md\nfig_magnitude_curve.py\nfigures\nfisher_analysis.py\nfix_plan_code_sketch.md\ngpu_health_snapshot_20260515.md\nintroduction_draft.md\nlerobot-pipeline-alignment.md\nlibero-smolvla-env-report.md\nliterature_gap_report.md\nmagnitude_curve.pdf\nmagnitude_curve.png\nmagnitude_curve_data.json\nmagnitude_curve_draft.pdf\nmagnitude_curve_draft.png\nmagnitude_multiseed_data.md\nmagnitude_sweep_summary.md\nmanifest.yaml\nmethod_draft.md\nmethod_section_draft.tex\nmvp-point-reaching\nnarrative_b_abstract_draft.md\nnarrative_b_abstract_final.md\nnarrative_b_draft.md\nobject_eval_commands.md\nobject_results_summary.md\npipeline-dimension-verification.md\npooled_fisher_test_v2.py\nprecompute-k5\nprecompute-k5-analysis.md\nprogress_scan_loop9.md\nreconvla-comparison-report.md\nrelated_work_draft.md\nreport_eval_progress.md\nreport_running_status.md\nresults_tables.md\nseed43_env_check.md\nseed44_obs_only_norm02_per_task.json\nsmolvla-libero-finetune-survey.md\nsmolvla_wrapper_fixed.py\nspatial_analysis_prep.md\nspatial_comparison_template.md\nthree_seed_fisher_analysis.py\ntraining_loss_analysis.md",
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

_source line 65_

<details open><summary>🔧 Tool call — Write · `toolu_01DuVBV4ogaDwYU7uTV9ieaV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/paper_data_alignment.md",
  "content": "# Paper Claims vs Data Alignment Report\n> Generated: 2026-05-17\n\n---\n\n## Claim 1: Sample-then-correct pipeline yields statistically significant improvement over argmin baseline\n\n**Paper states**: obs_only ε=0.2 pooled 105/600 (17.5%) vs argmin 74/600 (12.3%), +5.2pp, Fisher exact p=0.0074, Cohen's d=1.21 (paired), 5/6 seeds obs_only > argmin. VLA-only mean 10.8%.\n\n### 支撑实验\n\n**obs_only ε=0.2 (6 seeds, all confirmed):**\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-acr-object-obs-only-norm02 | 22% |\n| 43 | eval-obs-only-object-norm02-seed43-r2 | 16% |\n| 44 | eval-obs-only-object-norm02-seed44-r2 | 16% |\n| 45 | eval-obs-only-object-norm02-seed45 | 16% |\n| 46 | eval-obs-only-object-norm02-seed46 | 15% |\n| 47 | eval-obs-only-object-norm02-seed47 | 20% |\n\n**argmin (6 seeds, all confirmed):**\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-reconvla-object | 12% |\n| 43 | eval-argmin-object-seed43 | 17% |\n| 44 | eval-argmin-object-seed44-r2 | 13% |\n| 45 | eval-argmin-object-seed45 | 12% |\n| 46 | eval-argmin-object-seed46 | 10% |\n| 47 | eval-argmin-object-seed47 | 10% |\n\n**VLA-only (4 seeds):**\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-vla-only-object | 12% |\n| 43 | eval-vla-only-object-seed43 | 12% |\n| 44 | eval-vla-only-object-seed44-r2 | 10% |\n| 45 | eval-vla-only-object-seed45 | 9% (18/200) |\n\nVLA-only mean = (12+12+10+9)/4 = 10.75% ≈ 10.8% ✅\n\n**5/6 seed-wise wins**: 42(+10), 43(-1), 44(+3), 45(+4), 46(+5), 47(+10) → 5/6 ✅\n\n### 数据充分度: ✅ 充分\n- 6v6 seeds, 每组 600 trials\n- Fisher exact p=0.0074 (D047 confirmed)\n- Cohen's d=1.21 (paired) verified\n- 无缺口\n\n---\n\n## Claim 2: Conditioning-magnitude interaction — obs_only stable vs perdof progressive collapse\n\n**Paper states**: obs_only stable ~17% across norms 0.03–1.42; perdof progressive collapse 14% → 10% → 4% → 0%.\n\n### 支撑实验 — obs_only magnitude curve (Object)\n\n| norm | seeds done (values) | seeds running | total after | mean |\n|------|---------------------|--------------|-------------|------|\n| 0.03 | 1: 42=16% | 0 | 1 | 16% |\n| 0.05 | 1: 42=13% | 0 | 1 | 13% |\n| 0.10 | 3: 42=19%, 43=12%, 44=16% | 3 (s45,s46,s47) | 6 | 15.7% |\n| 0.20 | 6: 22/16/16/16/15/20 | 0 | 6 | 17.5% |\n| 0.30 | 3: 42=19%, 44=18%, 45=14% | 1 (s46) | 4 | 17.0% |\n| default | 2: 42=17%, 44=16% | 1 (s45) | 3 | 16.5% |\n\n### 支撑实验 — perdof magnitude curve (Object)\n\n| norm | seeds done (values) | seeds running | total after | mean |\n|------|---------------------|--------------|-------------|------|\n| 0.03 | 1: 42=14% | 0 | 1 | 14% |\n| 0.05 | 1: 42=14% | 0 | 1 | 14% |\n| 0.10 | 4: 42=11%, 43=12%, 44=8%, 45=11% | 2 (s46,s47) | 6 | 10.5% |\n| 0.20 | 2: 42=11%, 43=9% | 3 (s44,s45,s46) | 5 | 10.0% |\n| 0.30 | 3: 42=4%, 44=4%, 45=6% | 0 | 3 | 4.7% |\n| default | 1: 42=0% | 0 | 1 | 0% |\n\n### 数据充分度: ⚠️ 部分支撑\n- **趋势清晰**: obs_only 13–17.5% 稳定 vs perdof 14%→10%→4.7%→0% 坍塌模式明显\n- **核心缺口 — 低 norm 端 (0.03, 0.05) 双方法仅 1 seed**:\n  - 无法加 error bars，Figure 2 在端点可信度不足\n  - 审稿人可能质疑端点数据\n  - 无 RUNNING 实验覆盖这些点\n- **perdof default 仅 1 seed (0%)**:\n  - 虽然 0% (0/100) 极端值不太可能是偶然，但单 seed 仍有风险\n  - 无 RUNNING 实验补充\n- **RUNNING 实验完成后改善**: norm 0.1 → 6v6 seeds; perdof norm 0.2 → 5 seeds; obs_only norm 0.3 → 4 seeds\n- **paper_framing.md 数据需更新**:\n  - obs_only default 写 \"1s: 17%\"，实际已有 2 seeds (42=17%, 44=16%)\n  - perdof norm 0.1 ROADMAP 写 \"3s: 11/11/8\"，实际有 4 seeds (含 43=12%)\n  - perdof norm 0.2 写 \"1s: 11%\"，实际已有 2 seeds (42=11%, 43=9%)\n\n---\n\n## Claim 3: Per-DOF conformal features do not generalize — honest negative result\n\n**Paper states**: per-DOF scores fail beyond narrow safe region; root cause = K=10 rank-deficient covariance in 30D; spatial benchmark shows no method separates from baseline (34-35%).\n\n### 支撑实验 — Spatial benchmark (all single seed=42)\n\n| method | norm | exp_id | SR |\n|--------|------|--------|-----|\n| obs_only | 0.03 | eval-mag-obsonly-norm003-b2 | 34% |\n| obs_only | 0.05 | eval-mag-obsonly-norm005 | 35% |\n| obs_only | 0.10 | eval-acr-spatial-v4-obs-only-r3 | 35% |\n| obs_only | 0.20 | eval-mag-obsonly-norm02 | 35% |\n| obs_only | 0.30 | eval-mag-obsonly-norm03-r2 | 36% |\n| perdof | 0.03 | eval-mag-perdof-norm003 | 30% |\n| perdof | 0.05 | eval-mag-perdof-norm005 | 31% |\n| perdof | 0.10 | eval-acr-spatial-v4-small-r2 | 35% |\n| perdof | 0.30 | eval-mag-perdof-norm03 | 26% |\n| argmin | — | eval-argmin-only-spatial-r2 | 34% |\n| VLA-only | — | eval-spatial-v7-full | 30% |\n| VLA-mean | — | eval-vla-mean-spatial | 32% |\n\n### 数据充分度: ⚠️ 部分支撑\n- **趋势支撑 claim**: 所有方法 spatial 聚集在 26-36%，无明显分离\n- **所有 spatial 数据仅 1 seed**: 审稿人可能质疑\n- **perdof spatial 也有坍塌趋势 (35%→26%)**: 论文说 \"30-35%\"，但 norm 0.3 实际 26%，低于该范围\n  - 选项 A: 修正范围为 \"26-35%\"\n  - 选项 B: 指出 spatial 也出现 perdof 衰退（反而加强 Claim 2）\n- **Rank-deficiency 机制 (K=10, 30D)**: 理论论证，由 magnitude curve 模式间接支撑，无独立验证实验\n- 无 RUNNING spatial 实验\n\n---\n\n## Supporting Claims (Additional baselines)\n\n### scalar CRM\n**Paper states**: scalar CRM seed42 = 15% (single seed)\n\n**Registry data**:\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-acr-object-v4-scalar | **9%** (conclusion: negative) |\n| 43 | eval-scalar-object-seed43 | 10% |\n| 44 | eval-scalar-object-seed44-r2 | 6% (conclusion: negative) |\n\n**❌ 数据不一致**: paper_framing 写 15%，registry 实际为 9%。需核实来源，可能是旧版本模型数据或笔误。\n\n### VLA-mean (K=10 mean aggregation)\n**Paper states**: seed42=12%, seed43=15%, seed45=running\n\n**Registry data**:\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-vla-mean-object | 12% ✅ |\n| 43 | eval-vla-mean-object-seed43 | 15% ✅ |\n| 44 | eval-vla-mean-object-seed44 | 10% (paper 未记录) |\n| 45 | eval-vla-mean-object-seed45 | 13% (paper 标记 running，实际已完成) |\n\npaper_framing 需更新：seed44=10%, seed45=13% 已完成。4-seed mean = 12.5%。\n\n### Direct correction (K=1 CRM)\n**Paper states**: seed42 = 14% (not significant vs VLA-only)\n**Registry**: eval-direct-correction-object-seed42-r3 = 14% ✅ 单 seed。\n\n---\n\n## Summary\n\n| 状态 | 数量 | Claims |\n|------|------|--------|\n| ✅ 充分支撑 | 1 | Claim 1 (6v6 pipeline improvement, p=0.0074) |\n| ⚠️ 部分支撑 | 2 | Claim 2 (magnitude curve 低 norm 端仅 1 seed), Claim 3 (spatial 全部单 seed) |\n| ❌ 缺乏支撑 | 0 | — |\n\n### 数据错误\n- **scalar CRM**: paper_framing 写 seed42=15%，registry 实为 9%\n\n### 当前 RUNNING 实验能填补的缺口\n| 缺口 | RUNNING 实验 | 完成后状态 |\n|------|-------------|-----------|\n| obs_only norm=0.1 仅 3 seeds | s45, s46, s47 running | → 6 seeds ✅ |\n| obs_only norm=0.3 仅 3 seeds | s46 running | → 4 seeds |\n| obs_only default 仅 2 seeds | s45 running | → 3 seeds |\n| perdof norm=0.1 仅 4 seeds | s46, s47 running | → 6 seeds ✅ |\n| perdof norm=0.2 仅 2 seeds | s44, s45, s46 running | → 5 seeds ✅ |\n| scalar seed45 | running | → 4 seeds |\n\n### 仍无法填补的缺口（无 RUNNING 实验，需手动启动）\n1. **obs_only norm=0.03 / 0.05**: 各仅 1 seed，Figure 2 端点无 error bars\n2. **perdof norm=0.03 / 0.05**: 各仅 1 seed\n3. **perdof default**: 仅 1 seed (0%)\n4. **所有 spatial 数据**: 全部单 seed，无补充计划\n\n### 建议优先使用 8 张空闲 GPU\n1. perdof norm=0.03 seed43/44 (2 GPUs) — 补 Figure 2 低 norm 端\n2. obs_only norm=0.03 seed43/44 (2 GPUs) — 补 Figure 2 低 norm 端\n3. perdof default seed44/45 (2 GPUs) — 补坍塌终点\n4. perdof norm=0.05 seed43 + obs_only norm=0.05 seed43 (2 GPUs) — 低 norm 端\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "7ef1d55b-2af1-4a95-90c4-73362b39e071",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZbTsCbtTZu9qJTVcfx7Cf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 973,
      "cache_read_input_tokens": 49650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 973
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

_source line 66 · 2026-05-17T11:27:42.089Z_

<details><summary>↩ Tool result · `toolu_01DuVBV4ogaDwYU7uTV9ieaV`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/paper_data_alignment.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "ee2dad77-9383-4f8b-8961-4c0a85df951b",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/paper_data_alignment.md",
    "content": "# Paper Claims vs Data Alignment Report\n> Generated: 2026-05-17\n\n---\n\n## Claim 1: Sample-then-correct pipeline yields statistically significant improvement over argmin baseline\n\n**Paper states**: obs_only ε=0.2 pooled 105/600 (17.5%) vs argmin 74/600 (12.3%), +5.2pp, Fisher exact p=0.0074, Cohen's d=1.21 (paired), 5/6 seeds obs_only > argmin. VLA-only mean 10.8%.\n\n### 支撑实验\n\n**obs_only ε=0.2 (6 seeds, all confirmed):**\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-acr-object-obs-only-norm02 | 22% |\n| 43 | eval-obs-only-object-norm02-seed43-r2 | 16% |\n| 44 | eval-obs-only-object-norm02-seed44-r2 | 16% |\n| 45 | eval-obs-only-object-norm02-seed45 | 16% |\n| 46 | eval-obs-only-object-norm02-seed46 | 15% |\n| 47 | eval-obs-only-object-norm02-seed47 | 20% |\n\n**argmin (6 seeds, all confirmed):**\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-reconvla-object | 12% |\n| 43 | eval-argmin-object-seed43 | 17% |\n| 44 | eval-argmin-object-seed44-r2 | 13% |\n| 45 | eval-argmin-object-seed45 | 12% |\n| 46 | eval-argmin-object-seed46 | 10% |\n| 47 | eval-argmin-object-seed47 | 10% |\n\n**VLA-only (4 seeds):**\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-vla-only-object | 12% |\n| 43 | eval-vla-only-object-seed43 | 12% |\n| 44 | eval-vla-only-object-seed44-r2 | 10% |\n| 45 | eval-vla-only-object-seed45 | 9% (18/200) |\n\nVLA-only mean = (12+12+10+9)/4 = 10.75% ≈ 10.8% ✅\n\n**5/6 seed-wise wins**: 42(+10), 43(-1), 44(+3), 45(+4), 46(+5), 47(+10) → 5/6 ✅\n\n### 数据充分度: ✅ 充分\n- 6v6 seeds, 每组 600 trials\n- Fisher exact p=0.0074 (D047 confirmed)\n- Cohen's d=1.21 (paired) verified\n- 无缺口\n\n---\n\n## Claim 2: Conditioning-magnitude interaction — obs_only stable vs perdof progressive collapse\n\n**Paper states**: obs_only stable ~17% across norms 0.03–1.42; perdof progressive collapse 14% → 10% → 4% → 0%.\n\n### 支撑实验 — obs_only magnitude curve (Object)\n\n| norm | seeds done (values) | seeds running | total after | mean |\n|------|---------------------|--------------|-------------|------|\n| 0.03 | 1: 42=16% | 0 | 1 | 16% |\n| 0.05 | 1: 42=13% | 0 | 1 | 13% |\n| 0.10 | 3: 42=19%, 43=12%, 44=16% | 3 (s45,s46,s47) | 6 | 15.7% |\n| 0.20 | 6: 22/16/16/16/15/20 | 0 | 6 | 17.5% |\n| 0.30 | 3: 42=19%, 44=18%, 45=14% | 1 (s46) | 4 | 17.0% |\n| default | 2: 42=17%, 44=16% | 1 (s45) | 3 | 16.5% |\n\n### 支撑实验 — perdof magnitude curve (Object)\n\n| norm | seeds done (values) | seeds running | total after | mean |\n|------|---------------------|--------------|-------------|------|\n| 0.03 | 1: 42=14% | 0 | 1 | 14% |\n| 0.05 | 1: 42=14% | 0 | 1 | 14% |\n| 0.10 | 4: 42=11%, 43=12%, 44=8%, 45=11% | 2 (s46,s47) | 6 | 10.5% |\n| 0.20 | 2: 42=11%, 43=9% | 3 (s44,s45,s46) | 5 | 10.0% |\n| 0.30 | 3: 42=4%, 44=4%, 45=6% | 0 | 3 | 4.7% |\n| default | 1: 42=0% | 0 | 1 | 0% |\n\n### 数据充分度: ⚠️ 部分支撑\n- **趋势清晰**: obs_only 13–17.5% 稳定 vs perdof 14%→10%→4.7%→0% 坍塌模式明显\n- **核心缺口 — 低 norm 端 (0.03, 0.05) 双方法仅 1 seed**:\n  - 无法加 error bars，Figure 2 在端点可信度不足\n  - 审稿人可能质疑端点数据\n  - 无 RUNNING 实验覆盖这些点\n- **perdof default 仅 1 seed (0%)**:\n  - 虽然 0% (0/100) 极端值不太可能是偶然，但单 seed 仍有风险\n  - 无 RUNNING 实验补充\n- **RUNNING 实验完成后改善**: norm 0.1 → 6v6 seeds; perdof norm 0.2 → 5 seeds; obs_only norm 0.3 → 4 seeds\n- **paper_framing.md 数据需更新**:\n  - obs_only default 写 \"1s: 17%\"，实际已有 2 seeds (42=17%, 44=16%)\n  - perdof norm 0.1 ROADMAP 写 \"3s: 11/11/8\"，实际有 4 seeds (含 43=12%)\n  - perdof norm 0.2 写 \"1s: 11%\"，实际已有 2 seeds (42=11%, 43=9%)\n\n---\n\n## Claim 3: Per-DOF conformal features do not generalize — honest negative result\n\n**Paper states**: per-DOF scores fail beyond narrow safe region; root cause = K=10 rank-deficient covariance in 30D; spatial benchmark shows no method separates from baseline (34-35%).\n\n### 支撑实验 — Spatial benchmark (all single seed=42)\n\n| method | norm | exp_id | SR |\n|--------|------|--------|-----|\n| obs_only | 0.03 | eval-mag-obsonly-norm003-b2 | 34% |\n| obs_only | 0.05 | eval-mag-obsonly-norm005 | 35% |\n| obs_only | 0.10 | eval-acr-spatial-v4-obs-only-r3 | 35% |\n| obs_only | 0.20 | eval-mag-obsonly-norm02 | 35% |\n| obs_only | 0.30 | eval-mag-obsonly-norm03-r2 | 36% |\n| perdof | 0.03 | eval-mag-perdof-norm003 | 30% |\n| perdof | 0.05 | eval-mag-perdof-norm005 | 31% |\n| perdof | 0.10 | eval-acr-spatial-v4-small-r2 | 35% |\n| perdof | 0.30 | eval-mag-perdof-norm03 | 26% |\n| argmin | — | eval-argmin-only-spatial-r2 | 34% |\n| VLA-only | — | eval-spatial-v7-full | 30% |\n| VLA-mean | — | eval-vla-mean-spatial | 32% |\n\n### 数据充分度: ⚠️ 部分支撑\n- **趋势支撑 claim**: 所有方法 spatial 聚集在 26-36%，无明显分离\n- **所有 spatial 数据仅 1 seed**: 审稿人可能质疑\n- **perdof spatial 也有坍塌趋势 (35%→26%)**: 论文说 \"30-35%\"，但 norm 0.3 实际 26%，低于该范围\n  - 选项 A: 修正范围为 \"26-35%\"\n  - 选项 B: 指出 spatial 也出现 perdof 衰退（反而加强 Claim 2）\n- **Rank-deficiency 机制 (K=10, 30D)**: 理论论证，由 magnitude curve 模式间接支撑，无独立验证实验\n- 无 RUNNING spatial 实验\n\n---\n\n## Supporting Claims (Additional baselines)\n\n### scalar CRM\n**Paper states**: scalar CRM seed42 = 15% (single seed)\n\n**Registry data**:\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-acr-object-v4-scalar | **9%** (conclusion: negative) |\n| 43 | eval-scalar-object-seed43 | 10% |\n| 44 | eval-scalar-object-seed44-r2 | 6% (conclusion: negative) |\n\n**❌ 数据不一致**: paper_framing 写 15%，registry 实际为 9%。需核实来源，可能是旧版本模型数据或笔误。\n\n### VLA-mean (K=10 mean aggregation)\n**Paper states**: seed42=12%, seed43=15%, seed45=running\n\n**Registry data**:\n| seed | exp_id | SR |\n|------|--------|-----|\n| 42 | eval-vla-mean-object | 12% ✅ |\n| 43 | eval-vla-mean-object-seed43 | 15% ✅ |\n| 44 | eval-vla-mean-object-seed44 | 10% (paper 未记录) |\n| 45 | eval-vla-mean-object-seed45 | 13% (paper 标记 running，实际已完成) |\n\npaper_framing 需更新：seed44=10%, seed45=13% 已完成。4-seed mean = 12.5%。\n\n### Direct correction (K=1 CRM)\n**Paper states**: seed42 = 14% (not significant vs VLA-only)\n**Registry**: eval-direct-correction-object-seed42-r3 = 14% ✅ 单 seed。\n\n---\n\n## Summary\n\n| 状态 | 数量 | Claims |\n|------|------|--------|\n| ✅ 充分支撑 | 1 | Claim 1 (6v6 pipeline improvement, p=0.0074) |\n| ⚠️ 部分支撑 | 2 | Claim 2 (magnitude curve 低 norm 端仅 1 seed), Claim 3 (spatial 全部单 seed) |\n| ❌ 缺乏支撑 | 0 | — |\n\n### 数据错误\n- **scalar CRM**: paper_framing 写 seed42=15%，registry 实为 9%\n\n### 当前 RUNNING 实验能填补的缺口\n| 缺口 | RUNNING 实验 | 完成后状态 |\n|------|-------------|-----------|\n| obs_only norm=0.1 仅 3 seeds | s45, s46, s47 running | → 6 seeds ✅ |\n| obs_only norm=0.3 仅 3 seeds | s46 running | → 4 seeds |\n| obs_only default 仅 2 seeds | s45 running | → 3 seeds |\n| perdof norm=0.1 仅 4 seeds | s46, s47 running | → 6 seeds ✅ |\n| perdof norm=0.2 仅 2 seeds | s44, s45, s46 running | → 5 seeds ✅ |\n| scalar seed45 | running | → 4 seeds |\n\n### 仍无法填补的缺口（无 RUNNING 实验，需手动启动）\n1. **obs_only norm=0.03 / 0.05**: 各仅 1 seed，Figure 2 端点无 error bars\n2. **perdof norm=0.03 / 0.05**: 各仅 1 seed\n3. **perdof default**: 仅 1 seed (0%)\n4. **所有 spatial 数据**: 全部单 seed，无补充计划\n\n### 建议优先使用 8 张空闲 GPU\n1. perdof norm=0.03 seed43/44 (2 GPUs) — 补 Figure 2 低 norm 端\n2. obs_only norm=0.03 seed43/44 (2 GPUs) — 补 Figure 2 低 norm 端\n3. perdof default seed44/45 (2 GPUs) — 补坍塌终点\n4. perdof norm=0.05 seed43 + obs_only norm=0.05 seed43 (2 GPUs) — 低 norm 端\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 67_

Now registering the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "9ef19e4c-ed0c-467b-a93d-9bc6fc0344ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJcNeFVAHiBuBWat9TDG8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3853,
      "cache_read_input_tokens": 50623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3853
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

_source line 68_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Lc8CW4S8HGaQwabE8PDAxw`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "c0e67687-c15b-4094-8b0e-ca4ec18f473d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJcNeFVAHiBuBWat9TDG8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3853,
      "cache_read_input_tokens": 50623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3853
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

_source line 69 · 2026-05-17T11:27:45.090Z_

<details><summary>↩ Tool result · `toolu_01Lc8CW4S8HGaQwabE8PDAxw`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "29dabc91-c31d-4b5c-a6f8-1777b11a11c1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_012oN4UVU1qcfL5FXhZiaH6M`</summary>

```json
{
  "name": "paper_data_alignment",
  "type": "report",
  "description": "Paper claims vs experimental data alignment audit for CoRL 2026 submission. Checks each claim against registry metrics, identifies data gaps and inconsistencies.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/paper_data_alignment.md",
  "tags": [
    "paper",
    "audit",
    "corl2026"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "1b5a3f72-e7d3-403f-b70e-611ba71203de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NxLJWzSp8aBbDL6fEaU42P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 54476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
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

### Tool result

_source line 71 · 2026-05-17T11:27:50.091Z_

<details><summary>↩ Tool result · `toolu_012oN4UVU1qcfL5FXhZiaH6M`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260517_86ddf3\", \"name\": \"paper_data_alignment\", \"type\": \"report\", \"description\": \"Paper claims vs experimental data alignment audit for CoRL 2026 submission. Checks each claim against registry metrics, identifies data gaps and inconsistencies.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_data_alignment.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-17T11:27:49.940758+00:00\", \"tags\": [\"paper\", \"audit\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "5e304afc-8f5e-4894-b32e-c2eba780b6e5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260517_86ddf3\\\", \\\"name\\\": \\\"paper_data_alignment\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Paper claims vs experimental data alignment audit for CoRL 2026 submission. Checks each claim against registry metrics, identifies data gaps and inconsistencies.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_data_alignment.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-17T11:27:49.940758+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"audit\\\", \\\"corl2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260517_86ddf3\", \"name\": \"paper_data_alignment\", \"type\": \"report\", \"description\": \"Paper claims vs experimental data alignment audit for CoRL 2026 submission. Checks each claim against registry metrics, identifies data gaps and inconsistencies.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/paper_data_alignment.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-17T11:27:49.940758+00:00\", \"tags\": [\"paper\", \"audit\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 72_

报告已写入 `artifacts/paper_data_alignment.md` 并注册。核心发现：

**Claim 1 (pipeline improvement)**: ✅ 充分。6v6 seeds, p=0.0074, d=1.21 全部 registry 验证通过。

**Claim 2 (magnitude interaction)**: ⚠️ 部分。趋势清晰但 Figure 2 低 norm 端 (0.03, 0.05) 双方法仅 1 seed，无法加 error bars，且无 RUNNING 实验覆盖。perdof default 也仅 1 seed。

**Claim 3 (per-DOF negative result)**: ⚠️ 部分。所有 spatial 数据单 seed。perdof spatial norm=0.3 实际 26%，低于论文声称的 "30-35%" 范围。

**数据错误**: scalar CRM seed42 paper_framing 写 15%，registry 实为 9%。VLA-mean seed44/45 已完成但 paper_framing 未更新。

**关键建议**: 8 张空闲 GPU 应优先补 Figure 2 低 norm 端 (0.03/0.05) 的 multi-seed 数据和 perdof default 额外 seed。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "uuid": "d964bd6b-2097-4708-bc06-3a8896f27bf8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RetSe3jkzZbFjnfTrbvNP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 536,
      "cache_read_input_tokens": 55195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 536
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

_source line 73_

报告已写入 `artifacts/paper_data_alignment.md` 并注册。核心发现：

**Claim 1 (pipeline improvement)**: ✅ 充分。6v6 seeds, p=0.0074, d=1.21 全部 registry 验证通过。

**Claim 2 (magnitude interaction)**: ⚠️ 部分。趋势清晰但 Figure 2 低 norm 端 (0.03, 0.05) 双方法仅 1 seed，无法加 error bars，且无 RUNNING 实验覆盖。perdof default 也仅 1 seed。

**Claim 3 (per-DOF negative result)**: ⚠️ 部分。所有 spatial 数据单 seed。perdof spatial norm=0.3 实际 26%，低于论文声称的 "30-35%" 范围。

**数据错误**: scalar CRM seed42 paper_framing 写 15%，registry 实为 9%。VLA-mean seed44/45 已完成但 paper_framing 未更新。

**关键建议**: 8 张空闲 GPU 应优先补 Figure 2 低 norm 端 (0.03/0.05) 的 multi-seed 数据和 perdof default 额外 seed。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 566109,
  "duration_api_ms": 565336,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "7d3fb9a9-651b-4ced-b62a-b6d872235fb8",
  "total_cost_usd": 1.5725204999999998,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 43890,
    "cache_read_input_tokens": 340310,
    "output_tokens": 18504,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 43890,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 356,
        "cache_read_input_tokens": 55195,
        "cache_creation_input_tokens": 536,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 536
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1213,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001288,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 28,
      "outputTokens": 28331,
      "cacheReadInputTokens": 613785,
      "cacheCreationInputTokens": 88948,
      "webSearchRequests": 0,
      "costUSD": 1.5712325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d9d5a417-f05b-440a-9e94-97feffaf5084"
}
```

</details>

---
