# paper provenance update — Part 1 of 2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

[Transcript overview](../paper-provenance-update.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/2a/2ae1fea01b67d6182838.json)

## Before a recorded user message

## Before a recorded user message

58 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
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
  "uuid": "5e191ea9-83f2-4140-b467-9bd54338e2ba",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779725400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1fa1e22b-5fb1-4f8c-87bb-0cd0c15692b5",
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3"
}
```

---


### Assistant

_source line 4_

I'll start by reading the provenance file to find all NVE-related entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "2b318ad4-1450-43ef-b2ad-b5b1201b6464",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nHqCjAKPdDcEgyrAqK6pC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12009,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12009
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Li7UdnVhmLbsYF7YMJe6eB`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "b069c703-b43b-4745-8495-564dd30b4890",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nHqCjAKPdDcEgyrAqK6pC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12009,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12009
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

_source line 6 · 2026-05-25T14:11:15.600Z_

<details><summary>↩ Tool result · `toolu_01Li7UdnVhmLbsYF7YMJe6eB`</summary>

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "23bc16c8-5ac7-4ac3-8574-1d87c69c8c4e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---


### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the provenance file first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "e03dedbc-fde2-4514-b544-d30721ddd46b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nSVVHTiHGV7PecujJRbCk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 23456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
      },
      "output_tokens": 50,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01T3PAz31nHWiWqSf9FHJnS9`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_provenance.yaml",
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
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "e1233f63-38a9-491a-be3b-c5c02ec6c0a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nSVVHTiHGV7PecujJRbCk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 23456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
      },
      "output_tokens": 50,
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

_source line 9 · 2026-05-25T14:11:18.115Z_

<details><summary>↩ Tool result · `toolu_01T3PAz31nHWiWqSf9FHJnS9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\\n    of Variable-Rate DreamerV3'\\n  version: 38\\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\\nclaims:\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: every variable-rate configuration of DreamerV3 degrades performance\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions:\\n  - D009\\n  - D015\\n  deprecated: false\\n- id: C002\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 2\\n  text: trained temporal embedding as the causal factor\\n  type: methodological\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: control\\n  decisions:\\n  - D021\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 3\\n  text: 2.78x prediction gap between dt=1 and dt=2\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C004\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 4\\n  text: 7/8 classification (n=8)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_006_fixed_dt2\\n    metric: model_loss_at_55k\\n    value: 4.853\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C005\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 5\\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\\n    degradation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: full_collapse\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_eval_return\\n    value: 267.93\\n    role: transient_civo\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_eval_return\\n    value: 131.08\\n    role: oscillatory\\n  decisions: []\\n  deprecated: false\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 6\\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\\n    fails'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s1\\n    metric: final_eval_return\\n    value: 869.9\\n    role: healthy\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: collapsed\\n  - exp_id: exp_009a_baseline_walker_s2\\n    metric: final_eval_return\\n    value: 836.51\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C007\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: fixed dt=2 collapses to 14% of baseline\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C008\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: fixed dt=4 never exceeds 19% of baseline\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C009\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: learned Gumbel-Softmax gate collapses to 11%\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C010\\n  location:\\n    section: methodology\\n    paragraph: 8\\n    sentence: 0\\n  text: baseline runs for 500K steps, peak return 970.4\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_001_baseline\\n    metric: eval_return_peak\\n    value: 970.41\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C011\\n  location:\\n    section: methodology\\n    paragraph: 6\\n    sentence: 3\\n  text: 7/8 accuracy (AUROC=0.933)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions:\\n  - D053\\n  - D054\\n  deprecated: false\\n- id: C012\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 1\\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_001_baseline\\n    metric: eval_return_peak\\n    value: 970.41\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 2\\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: peak_return\\n    value: 485.3\\n    role: primary_evidence\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C014\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 3\\n  text: fixed dt=4 peaks at 176.9 at 25K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C015\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 4\\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_005_event_gated_v4\\n    metric: peak_return\\n    value: 541.18\\n    role: primary_evidence\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: results\\n    paragraph: 3\\n    sentence: 0\\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_25K\\n    value: 167.22\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: results\\n    paragraph: 3\\n    sentence: 1\\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C018\\n  location:\\n    section: results\\n    paragraph: 4\\n    sentence: 0\\n  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D054\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: results\\n    paragraph: 4\\n    sentence: 1\\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions: []\\n  deprecated: false\\n- id: C020\\n  location:\\n    section: results\\n    paragraph: 6\\n    sentence: 0\\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C021\\n  location:\\n    section: results\\n    paragraph: 7\\n    sentence: 0\\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\\n    267.9'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_eval_return\\n    value: 267.93\\n    role: primary_evidence\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_nve\\n    value: 0.38\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C022\\n  location:\\n    section: results\\n    paragraph: 8\\n    sentence: 0\\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\\n    final 1.57x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_eval_return\\n    value: 131.08\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_nve\\n    value: 1.57\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C023\\n  location:\\n    section: results\\n    paragraph: 10\\n    sentence: 0\\n  text: 008a reaches 777.7 (NVE=0.59x)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008a_no_subsample_dt2\\n    metric: eval_return_105K\\n    value: 777.66\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: results\\n    paragraph: 10\\n    sentence: 0\\n  text: 008c reaches 240.9 (NVE=0.58x)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008c_no_subsample_dt2_h8\\n    metric: eval_return_65K\\n    value: 240.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: results\\n    paragraph: 12\\n    sentence: 0\\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: peak_return\\n    value: 485.3\\n    role: primary_evidence\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: results\\n    paragraph: 14\\n    sentence: 0\\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: results\\n    paragraph: 14\\n    sentence: 1\\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: primary_evidence\\n  - exp_id: exp_009c_008f_walker_s2\\n    metric: final_eval_return\\n    value: 148.34\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: results\\n    paragraph: 16\\n    sentence: 0\\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s1\\n    metric: final_eval_return\\n    value: 869.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: results\\n    paragraph: 16\\n    sentence: 1\\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: primary_evidence\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: peak_eval_return\\n    value: 715.21\\n    role: primary_evidence\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: results\\n    paragraph: 17\\n    sentence: 0\\n  text: baseline seed 2 (009a) stable at 836.5\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009a_baseline_walker_s2\\n    metric: final_eval_return\\n    value: 836.51\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: results\\n    paragraph: 18\\n    sentence: 1\\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: results\\n    paragraph: 19\\n    sentence: 0\\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 0\\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 1\\n  text: 008f reward gap 1.01x (MAE 0.7469)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.reward_gap\\n    value: 1.01\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 1\\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\n    value: 0.7469\\n    role: primary_evidence\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\n    value: 0.0568\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 0\\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\\n    2.90x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: random_policy_reward_ratio\\n    value: 1.68\\n    role: stage1\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: trained_actor_reward_ratio\\n    value: 2.9\\n    role: stage2\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 1\\n  text: ~36% dynamics bias, ~64% actor exploitation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: dynamics_bias_fraction\\n    value: 0.36\\n    role: primary_evidence\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 2\\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: random_policy_reward_ratio\\n    value: 1.11\\n    role: control\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: trained_actor_reward_ratio\\n    value: 0.98\\n    role: control\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: analysis\\n    paragraph: 4\\n    sentence: 0\\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: analysis\\n    paragraph: 7\\n    sentence: 0\\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\n    value: 0.7469\\n    role: primary_evidence\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\n    value: 0.0568\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C041\\n  location:\\n    section: analysis\\n    paragraph: 8\\n    sentence: 1\\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 2\\n  text: 7/8 CIVO classification (n=8, 87.5%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C043\\n  location:\\n    section: conclusion\\n    paragraph: 2\\n    sentence: 1\\n  text: NVE margin 0.62 excluding outlier\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: lowest_true_positive\\n  decisions: []\\n  deprecated: false\\n- id: C044\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C046\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\\n    healthy, return collapses ~35K steps before entropy rises'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C047\\n  location:\\n    section: sections/methodology\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  - exp_id: plan_034_nve_threshold\\n    metric: f1_at_1.5x\\n    value: 0.88\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C048\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: sections/abstract_body\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C050\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 classification in introduction\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C051\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Contribution 1 AUROC updated to 0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C052\\n  location:\\n    section: sections/conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C053\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C055\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_064_value_distribution\\n    metric: civo_median_v_mc_ratio\\n    value: 3.4\\n    role: primary_evidence\\n  - exp_id: exp_064_value_distribution\\n    metric: control_median_v_mc_ratio\\n    value: 1.05\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C056\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\\n    vs +0.07-0.22 healthy'\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_031_actor_entropy\\n    metric: collapsed_entropy_rate\\n    value: 2.1\\n    role: primary_evidence\\n  - exp_id: plan_031_actor_entropy\\n    metric: healthy_entropy_rate_range\\n    value: 0.07-0.22\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C057\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C058\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\\n    Cheetah'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_026_obs_sgs_cheetah\\n    metric: nve_amplification\\n    value: 21.9-30.2\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C059\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\\n    baseline'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_030c_tcn_cheetah\\n    metric: nve_suppressed\\n    value: 0.3\\n    role: primary_evidence\\n  - exp_id: exp_030c_tcn_cheetah\\n    metric: eval_pct_baseline\\n    value: 15\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\\n    to -0.86 at 75K'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: trained_cos_25k_range\\n    value: -0.87 to -0.94\\n    role: primary_evidence\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: trained_cos_75k_range\\n    value: -0.70 to -0.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: frozen_cos_constant\\n    value: -0.15 to +0.07\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C062\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\\n    conditioning\\n  type: quantitative\\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\\n  decisions: []\\n  deprecated: false\\n- id: C064\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\\n    vs baseline 1.46x)\\n  type: quantitative\\n  evidence: exp_063 obs_mse data\\n  decisions: []\\n  deprecated: false\\n- id: C065\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\\n    median 1.05x (52.5% overestimated)\\n  type: quantitative\\n  evidence: exp_064 value_distribution results_summary\\n  decisions: []\\n  deprecated: false\\n- id: C066\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\\n    pathology\\n  type: quantitative\\n  evidence: exp_063 rssm_fidelity_analysis\\n  decisions: []\\n  deprecated: false\\n- id: C067\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\\n  type: quantitative\\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\\n  decisions: []\\n  deprecated: false\\n- id: C068\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\\n    improvement\\n  type: quantitative\\n  evidence: exp_066 timeseries analysis\\n  decisions: []\\n  deprecated: false\\n- id: C069\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\\n    → entropy destabilization (~35K later), n=1'\\n  type: quantitative\\n  evidence: exp_066 timeseries + actor entropy analysis\\n  decisions: []\\n  deprecated: false\\n- id: C070\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\\n    VE ratio near zero until 40K spike (1.59x)'\\n  type: quantitative\\n  evidence: exp_066 12-checkpoint timeseries analysis\\n  decisions: []\\n  deprecated: false\\n- id: C071\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\\n    selective improvement not worsening\\n  type: quantitative\\n  evidence: exp_066 timeseries MAE data\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: T001\\n  location:\\n    section: methodology\\n    table_number: 1\\n  caption: Factorial design — 9 configurations\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: '001'\\n    source:\\n      exp_id: exp_001_baseline\\n      metric: exp_id\\n  - row: 1\\n    col: 0\\n    value: '006'\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: exp_id\\n  - row: 2\\n    col: 0\\n    value: '007'\\n    source:\\n      exp_id: exp_007_fixed_dt4\\n      metric: exp_id\\n  - row: 3\\n    col: 0\\n    value: '005'\\n    source:\\n      exp_id: exp_005_event_gated_v4\\n      metric: exp_id\\n  - row: 4\\n    col: 0\\n    value: 008d\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: exp_id\\n  - row: 5\\n    col: 0\\n    value: 008f\\n    source:\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n      metric: exp_id\\n  - row: 6\\n    col: 0\\n    value: 008a\\n    source:\\n      exp_id: exp_008a_no_subsample_dt2\\n      metric: exp_id\\n  - row: 7\\n    col: 0\\n    value: 008c\\n    source:\\n      exp_id: exp_008c_no_subsample_dt2_h8\\n      metric: exp_id\\n  - row: 8\\n    col: 0\\n    value: 008e_v3\\n    source:\\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\\n      metric: exp_id\\n  deprecated: false\\n- id: T002\\n  location:\\n    section: results\\n    table_number: 1\\n  caption: All configurations and outcomes\\n  cells:\\n  - row: 0\\n    col: 5\\n    value: 915.7\\n    source:\\n      exp_id: exp_001_baseline\\n      metric: eval_return_105K\\n  - row: 1\\n    col: 5\\n    value: 132.9\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: eval_return_65K\\n  - row: 1\\n    col: 6\\n    value: 4.83\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: peak_nve\\n  - row: 2\\n    col: 5\\n    value: 152.5\\n    source:\\n      exp_id: exp_007_fixed_dt4\\n      metric: eval_return_55K\\n  - row: 3\\n    col: 5\\n    value: 98.8\\n    source:\\n      exp_id: exp_005_event_gated_v4\\n      metric: eval_return_145K\\n  - row: 4\\n    col: 5\\n    value: 82.8\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: eval_return_55K\\n  - row: 4\\n    col: 6\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 5\\n    col: 5\\n    value: 267.9\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_eval_return\\n  - row: 5\\n    col: 6\\n    value: 1.62\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: peak_nve\\n  - row: 6\\n    col: 5\\n    value: 131.1\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_eval_return\\n  - row: 6\\n    col: 6\\n    value: 4.12\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: peak_nve\\n  - row: 7\\n    col: 5\\n    value: 503.0\\n    source:\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n      metric: eval_return_105K\\n  - row: 8\\n    col: 5\\n    value: 148.3\\n    source:\\n      exp_id: exp_009c_008f_walker_s2\\n      metric: final_eval_return\\n  - row: 9\\n    col: 5\\n    value: 777.7\\n    source:\\n      exp_id: exp_008a_no_subsample_dt2\\n      metric: eval_return_105K\\n  - row: 10\\n    col: 5\\n    value: 240.9\\n    source:\\n      exp_id: exp_008c_no_subsample_dt2_h8\\n      metric: eval_return_65K\\n  - row: 11\\n    col: 5\\n    value: 869.9\\n    source:\\n      exp_id: exp_008e_v3_walker_s1\\n      metric: final_eval_return\\n  - row: 12\\n    col: 5\\n    value: 137.0\\n    source:\\n      exp_id: exp_008e_v3_walker_s2\\n      metric: final_eval_return\\n  - row: 12\\n    col: 6\\n    value: 3.78\\n    source:\\n      exp_id: exp_008e_v3_walker_s2\\n      metric: final_nve\\n  - row: 13\\n    col: 5\\n    value: 836.5\\n    source:\\n      exp_id: exp_009a_baseline_walker_s2\\n      metric: final_eval_return\\n  deprecated: false\\n- id: T003\\n  location:\\n    section: results\\n    table_number: 2\\n  caption: RSSM fidelity at dt=1 vs dt=2\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: 13.49\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt1_obs_mse\\n  - row: 0\\n    col: 1\\n    value: 27.5\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt2_obs_mse\\n  - row: 0\\n    col: 2\\n    value: 2.04\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.obs_gap\\n  - row: 0\\n    col: 3\\n    value: 0.0102\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt1_reward_mae\\n  - row: 0\\n    col: 4\\n    value: 0.0159\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt2_reward_mae\\n  - row: 0\\n    col: 5\\n    value: 1.56\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.reward_gap\\n  - row: 1\\n    col: 0\\n    value: 41.31\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt1_obs_mse\\n  - row: 1\\n    col: 1\\n    value: 53.67\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt2_obs_mse\\n  - row: 1\\n    col: 2\\n    value: 1.3\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.obs_gap\\n  - row: 1\\n    col: 3\\n    value: 0.0568\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt1_reward_mae\\n  - row: 1\\n    col: 4\\n    value: 0.1579\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt2_reward_mae\\n  - row: 1\\n    col: 5\\n    value: 2.78\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.reward_gap\\n  - row: 2\\n    col: 0\\n    value: 8.01\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt1_obs_mse\\n  - row: 2\\n    col: 1\\n    value: 22.04\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt2_obs_mse\\n  - row: 2\\n    col: 2\\n    value: 2.75\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.obs_gap\\n  - row: 2\\n    col: 3\\n    value: 0.7469\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt1_reward_mae\\n  - row: 2\\n    col: 4\\n    value: 0.7526\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt2_reward_mae\\n  - row: 2\\n    col: 5\\n    value: 1.01\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.reward_gap\\n  deprecated: false\\n- id: T004\\n  location:\\n    section: results\\n    table_number: 3\\n  caption: Post-CIVO outcomes for 008d configuration\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 0\\n    col: 1\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 0\\n    col: 2\\n    value: 82.8\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: eval_return_55K\\n  - row: 1\\n    col: 0\\n    value: 1.62\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: peak_nve\\n  - row: 1\\n    col: 1\\n    value: 0.38\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_nve\\n  - row: 1\\n    col: 2\\n    value: 267.9\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_eval_return\\n  - row: 2\\n    col: 0\\n    value: 4.12\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: peak_nve\\n  - row: 2\\n    col: 1\\n    value: 1.57\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_nve\\n  - row: 2\\n    col: 2\\n    value: 131.1\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_eval_return\\n  deprecated: false\\nfigures:\\n- id: F001\\n  location:\\n    section: results\\n    figure_number: 1\\n  caption: Learning curves for all configurations\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_001_baseline\\n    - exp_id: exp_006_fixed_dt2\\n    - exp_id: exp_007_fixed_dt4\\n    - exp_id: exp_005_event_gated_v4\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008e_v3_walker_s1\\n  output_path: figures/paper/fig1_learning_curves.pdf\\n  deprecated: false\\n- id: F002\\n  location:\\n    section: results\\n    figure_number: 2\\n  caption: Normalized value-to-eval ratio trajectories\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008e_v3_walker_s1\\n    - exp_id: exp_009b_008d_walker_s2\\n  output_path: figures/paper/fig2_nve_trajectory.pdf\\n  deprecated: false\\n- id: F003\\n  location:\\n    section: results\\n    figure_number: 3\\n  caption: Factorial experiment summary grid\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008c_no_subsample_dt2_h8\\n  output_path: figures/paper/fig3_factorial_grid.pdf\\n  deprecated: false\\n- id: F004\\n  location:\\n    section: results\\n    figure_number: 4\\n  caption: Peak evaluation return as function of imagination dt\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_001_baseline\\n    - exp_id: exp_006_fixed_dt2\\n    - exp_id: exp_007_fixed_dt4\\n  output_path: figures/paper/fig5_dt_amplification.pdf\\n  deprecated: false\\n- id: F005\\n  location:\\n    section: results\\n    figure_number: 5\\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008e_v3_walker_s2\\n    - exp_id: exp_009a_baseline_walker_s2\\n  output_path: figures/paper/fig6_multiple_pathways.pdf\\n  deprecated: false\\n- id: F006\\n  location:\\n    section: sections/appendix\\n    figure_number: 0\\n  caption: ''\\n  type: other\\n  source: {}\\n  output_path: ''\\n  deprecated: false\\n_completeness:\\n  coverage: 73/77\\n  claims: 71\\n  tables: 4\\n  figures: 6\\n  tier_counts:\\n    tier1: 0\\n    tier2: 73\\n    tier3: 4\\n    tierX: 0\\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\\n\", \"total_chars\": 36692, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "5c2b5cd3-b654-4e32-8efd-24f1804177ae",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml\\\", \\\"content\\\": \\\"paper:\\\\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\\\\n    of Variable-Rate DreamerV3'\\\\n  version: 38\\\\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\\\\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\\\\nclaims:\\\\n- id: C001\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: every variable-rate configuration of DreamerV3 degrades performance\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: eval_return_65K\\\\n    value: 132.86\\\\n    role: primary_evidence\\\\n  - exp_id: exp_007_fixed_dt4\\\\n    metric: peak_return\\\\n    value: 176.9\\\\n    role: primary_evidence\\\\n  - exp_id: exp_005_event_gated_v4\\\\n    metric: eval_return_145K\\\\n    value: 98.84\\\\n    role: primary_evidence\\\\n  decisions:\\\\n  - D009\\\\n  - D015\\\\n  deprecated: false\\\\n- id: C002\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 2\\\\n  text: trained temporal embedding as the causal factor\\\\n  type: methodological\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_55K\\\\n    value: 82.75\\\\n    role: primary_evidence\\\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    metric: eval_return_105K\\\\n    value: 503.0\\\\n    role: control\\\\n  decisions:\\\\n  - D021\\\\n  deprecated: false\\\\n- id: C003\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 3\\\\n  text: 2.78x prediction gap between dt=1 and dt=2\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.reward_gap\\\\n    value: 2.78\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C004\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 4\\\\n  text: 7/8 classification (n=8)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: true_positive\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: model_loss_at_55k\\\\n    value: 4.853\\\\n    role: true_positive\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: true_positive\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_nve\\\\n    value: 3.78\\\\n    role: false_positive\\\\n  decisions:\\\\n  - D053\\\\n  deprecated: false\\\\n- id: C005\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 5\\\\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\\\\n    degradation\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_55K\\\\n    value: 82.75\\\\n    role: full_collapse\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 267.93\\\\n    role: transient_civo\\\\n  - exp_id: exp_009e_008d_walker_s1\\\\n    metric: final_eval_return\\\\n    value: 131.08\\\\n    role: oscillatory\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C006\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 6\\\\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\\\\n    fails'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s1\\\\n    metric: final_eval_return\\\\n    value: 869.9\\\\n    role: healthy\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 136.96\\\\n    role: collapsed\\\\n  - exp_id: exp_009a_baseline_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 836.51\\\\n    role: control\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C007\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 1\\\\n    sentence: 1\\\\n  text: fixed dt=2 collapses to 14% of baseline\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: eval_return_65K\\\\n    value: 132.86\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C008\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 1\\\\n    sentence: 1\\\\n  text: fixed dt=4 never exceeds 19% of baseline\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_007_fixed_dt4\\\\n    metric: peak_return\\\\n    value: 176.9\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C009\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 1\\\\n    sentence: 1\\\\n  text: learned Gumbel-Softmax gate collapses to 11%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_005_event_gated_v4\\\\n    metric: eval_return_145K\\\\n    value: 98.84\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C010\\\\n  location:\\\\n    section: methodology\\\\n    paragraph: 8\\\\n    sentence: 0\\\\n  text: baseline runs for 500K steps, peak return 970.4\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_001_baseline\\\\n    metric: eval_return_peak\\\\n    value: 970.41\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C011\\\\n  location:\\\\n    section: methodology\\\\n    paragraph: 6\\\\n    sentence: 3\\\\n  text: 7/8 accuracy (AUROC=0.933)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: true_positive\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: true_positive\\\\n  decisions:\\\\n  - D053\\\\n  - D054\\\\n  deprecated: false\\\\n- id: C012\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 1\\\\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_001_baseline\\\\n    metric: eval_return_peak\\\\n    value: 970.41\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C013\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 2\\\\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: peak_return\\\\n    value: 485.3\\\\n    role: primary_evidence\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: eval_return_65K\\\\n    value: 132.86\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C014\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 3\\\\n  text: fixed dt=4 peaks at 176.9 at 25K\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_007_fixed_dt4\\\\n    metric: peak_return\\\\n    value: 176.9\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C015\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 4\\\\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_005_event_gated_v4\\\\n    metric: peak_return\\\\n    value: 541.18\\\\n    role: primary_evidence\\\\n  - exp_id: exp_005_event_gated_v4\\\\n    metric: eval_return_145K\\\\n    value: 98.84\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C016\\\\n  location:\\\\n    section: results\\\\n    paragraph: 3\\\\n    sentence: 0\\\\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_55K\\\\n    value: 82.75\\\\n    role: primary_evidence\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_25K\\\\n    value: 167.22\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C017\\\\n  location:\\\\n    section: results\\\\n    paragraph: 3\\\\n    sentence: 1\\\\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    metric: eval_return_105K\\\\n    value: 503.0\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C018\\\\n  location:\\\\n    section: results\\\\n    paragraph: 4\\\\n    sentence: 0\\\\n  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: true_positive\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: true_positive\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_nve\\\\n    value: 3.78\\\\n    role: false_positive\\\\n  decisions:\\\\n  - D054\\\\n  deprecated: false\\\\n- id: C019\\\\n  location:\\\\n    section: results\\\\n    paragraph: 4\\\\n    sentence: 1\\\\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: true_positive\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C020\\\\n  location:\\\\n    section: results\\\\n    paragraph: 6\\\\n    sentence: 0\\\\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_55K\\\\n    value: 82.75\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C021\\\\n  location:\\\\n    section: results\\\\n    paragraph: 7\\\\n    sentence: 0\\\\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\\\\n    267.9'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 267.93\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: final_nve\\\\n    value: 0.38\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C022\\\\n  location:\\\\n    section: results\\\\n    paragraph: 8\\\\n    sentence: 0\\\\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\\\\n    final 1.57x'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_009e_008d_walker_s1\\\\n    metric: final_eval_return\\\\n    value: 131.08\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009e_008d_walker_s1\\\\n    metric: final_nve\\\\n    value: 1.57\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009e_008d_walker_s1\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C023\\\\n  location:\\\\n    section: results\\\\n    paragraph: 10\\\\n    sentence: 0\\\\n  text: 008a reaches 777.7 (NVE=0.59x)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008a_no_subsample_dt2\\\\n    metric: eval_return_105K\\\\n    value: 777.66\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C024\\\\n  location:\\\\n    section: results\\\\n    paragraph: 10\\\\n    sentence: 0\\\\n  text: 008c reaches 240.9 (NVE=0.58x)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008c_no_subsample_dt2_h8\\\\n    metric: eval_return_65K\\\\n    value: 240.86\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C025\\\\n  location:\\\\n    section: results\\\\n    paragraph: 12\\\\n    sentence: 0\\\\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: peak_return\\\\n    value: 485.3\\\\n    role: primary_evidence\\\\n  - exp_id: exp_007_fixed_dt4\\\\n    metric: peak_return\\\\n    value: 176.9\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C026\\\\n  location:\\\\n    section: results\\\\n    paragraph: 14\\\\n    sentence: 0\\\\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_55K\\\\n    value: 82.75\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C027\\\\n  location:\\\\n    section: results\\\\n    paragraph: 14\\\\n    sentence: 1\\\\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    metric: eval_return_105K\\\\n    value: 503.0\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009c_008f_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 148.34\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C028\\\\n  location:\\\\n    section: results\\\\n    paragraph: 16\\\\n    sentence: 0\\\\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s1\\\\n    metric: final_eval_return\\\\n    value: 869.9\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C029\\\\n  location:\\\\n    section: results\\\\n    paragraph: 16\\\\n    sentence: 1\\\\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 136.96\\\\n    role: primary_evidence\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: peak_eval_return\\\\n    value: 715.21\\\\n    role: primary_evidence\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_nve\\\\n    value: 3.78\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C030\\\\n  location:\\\\n    section: results\\\\n    paragraph: 17\\\\n    sentence: 0\\\\n  text: baseline seed 2 (009a) stable at 836.5\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_009a_baseline_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 836.51\\\\n    role: control\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C031\\\\n  location:\\\\n    section: results\\\\n    paragraph: 18\\\\n    sentence: 1\\\\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 136.96\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C032\\\\n  location:\\\\n    section: results\\\\n    paragraph: 19\\\\n    sentence: 0\\\\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_nve\\\\n    value: 3.78\\\\n    role: false_positive\\\\n  decisions:\\\\n  - D053\\\\n  deprecated: false\\\\n- id: C033\\\\n  location:\\\\n    section: results\\\\n    paragraph: 21\\\\n    sentence: 0\\\\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.reward_gap\\\\n    value: 2.78\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C034\\\\n  location:\\\\n    section: results\\\\n    paragraph: 21\\\\n    sentence: 1\\\\n  text: 008f reward gap 1.01x (MAE 0.7469)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008f_no_dtEmb.reward_gap\\\\n    value: 1.01\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C035\\\\n  location:\\\\n    section: results\\\\n    paragraph: 21\\\\n    sentence: 1\\\\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\\\n    value: 0.7469\\\\n    role: primary_evidence\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\\\n    value: 0.0568\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C036\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 2\\\\n    sentence: 0\\\\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\\\\n    2.90x'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: random_policy_reward_ratio\\\\n    value: 1.68\\\\n    role: stage1\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: trained_actor_reward_ratio\\\\n    value: 2.9\\\\n    role: stage2\\\\n  decisions:\\\\n  - D042\\\\n  deprecated: false\\\\n- id: C037\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 2\\\\n    sentence: 1\\\\n  text: ~36% dynamics bias, ~64% actor exploitation\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: dynamics_bias_fraction\\\\n    value: 0.36\\\\n    role: primary_evidence\\\\n  decisions:\\\\n  - D042\\\\n  deprecated: false\\\\n- id: C038\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 2\\\\n    sentence: 2\\\\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    metric: random_policy_reward_ratio\\\\n    value: 1.11\\\\n    role: control\\\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    metric: trained_actor_reward_ratio\\\\n    value: 0.98\\\\n    role: control\\\\n  decisions:\\\\n  - D042\\\\n  deprecated: false\\\\n- id: C039\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 4\\\\n    sentence: 0\\\\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009e_008d_walker_s1\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C040\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 7\\\\n    sentence: 0\\\\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\\\n    value: 0.7469\\\\n    role: primary_evidence\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\\\n    value: 0.0568\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C041\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 8\\\\n    sentence: 1\\\\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_nve\\\\n    value: 3.78\\\\n    role: false_positive\\\\n  decisions:\\\\n  - D053\\\\n  deprecated: false\\\\n- id: C042\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 2\\\\n  text: 7/8 CIVO classification (n=8, 87.5%)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: true_positive\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: true_positive\\\\n  decisions:\\\\n  - D053\\\\n  deprecated: false\\\\n- id: C043\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 2\\\\n    sentence: 1\\\\n  text: NVE margin 0.62 excluding outlier\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: lowest_true_positive\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C044\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C045\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C046\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\\\\n    healthy, return collapses ~35K steps before entropy rises'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C047\\\\n  location:\\\\n    section: sections/methodology\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: f1_at_1.5x\\\\n    value: 0.88\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C048\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C049\\\\n  location:\\\\n    section: sections/abstract_body\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C050\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: NVE threshold 29/32 classification in introduction\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C051\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Contribution 1 AUROC updated to 0.961\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C052\\\\n  location:\\\\n    section: sections/conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C053\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C054\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.reward_gap\\\\n    value: 2.78\\\\n    role: primary_evidence\\\\n  - exp_id: exp_063_rssm_fidelity\\\\n    metric: collapsed_reward_gap\\\\n    value: 3.11\\\\n    role: corroboration\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C055\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_064_value_distribution\\\\n    metric: civo_median_v_mc_ratio\\\\n    value: 3.4\\\\n    role: primary_evidence\\\\n  - exp_id: exp_064_value_distribution\\\\n    metric: control_median_v_mc_ratio\\\\n    value: 1.05\\\\n    role: control\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C056\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\\\\n    vs +0.07-0.22 healthy'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_031_actor_entropy\\\\n    metric: collapsed_entropy_rate\\\\n    value: 2.1\\\\n    role: primary_evidence\\\\n  - exp_id: plan_031_actor_entropy\\\\n    metric: healthy_entropy_rate_range\\\\n    value: 0.07-0.22\\\\n    role: control\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C057\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.reward_gap\\\\n    value: 2.78\\\\n    role: primary_evidence\\\\n  - exp_id: exp_063_rssm_fidelity\\\\n    metric: collapsed_reward_gap\\\\n    value: 3.11\\\\n    role: corroboration\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C058\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\\\\n    Cheetah'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_026_obs_sgs_cheetah\\\\n    metric: nve_amplification\\\\n    value: 21.9-30.2\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C059\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\\\\n    baseline'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_030c_tcn_cheetah\\\\n    metric: nve_suppressed\\\\n    value: 0.3\\\\n    role: primary_evidence\\\\n  - exp_id: exp_030c_tcn_cheetah\\\\n    metric: eval_pct_baseline\\\\n    value: 15\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C060\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\\\\n    to -0.86 at 75K'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_065_dt_emb_cosine\\\\n    metric: trained_cos_25k_range\\\\n    value: -0.87 to -0.94\\\\n    role: primary_evidence\\\\n  - exp_id: exp_065_dt_emb_cosine\\\\n    metric: trained_cos_75k_range\\\\n    value: -0.70 to -0.86\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C061\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_065_dt_emb_cosine\\\\n    metric: frozen_cos_constant\\\\n    value: -0.15 to +0.07\\\\n    role: control\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C062\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.reward_gap\\\\n    value: 2.78\\\\n    role: primary_evidence\\\\n  - exp_id: exp_063_rssm_fidelity\\\\n    metric: collapsed_reward_gap\\\\n    value: 3.11\\\\n    role: corroboration\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C063\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\\\\n    conditioning\\\\n  type: quantitative\\\\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C064\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\\\\n    vs baseline 1.46x)\\\\n  type: quantitative\\\\n  evidence: exp_063 obs_mse data\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C065\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\\\\n    median 1.05x (52.5% overestimated)\\\\n  type: quantitative\\\\n  evidence: exp_064 value_distribution results_summary\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C066\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\\\\n    pathology\\\\n  type: quantitative\\\\n  evidence: exp_063 rssm_fidelity_analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C067\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\\\\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\\\\n  type: quantitative\\\\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C068\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\\\\n    improvement\\\\n  type: quantitative\\\\n  evidence: exp_066 timeseries analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C069\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\\\\n    → entropy destabilization (~35K later), n=1'\\\\n  type: quantitative\\\\n  evidence: exp_066 timeseries + actor entropy analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C070\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\\\\n    VE ratio near zero until 40K spike (1.59x)'\\\\n  type: quantitative\\\\n  evidence: exp_066 12-checkpoint timeseries analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C071\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\\\\n    selective improvement not worsening\\\\n  type: quantitative\\\\n  evidence: exp_066 timeseries MAE data\\\\n  decisions: []\\\\n  deprecated: false\\\\ntables:\\\\n- id: T001\\\\n  location:\\\\n    section: methodology\\\\n    table_number: 1\\\\n  caption: Factorial design — 9 configurations\\\\n  cells:\\\\n  - row: 0\\\\n    col: 0\\\\n    value: '001'\\\\n    source:\\\\n      exp_id: exp_001_baseline\\\\n      metric: exp_id\\\\n  - row: 1\\\\n    col: 0\\\\n    value: '006'\\\\n    source:\\\\n      exp_id: exp_006_fixed_dt2\\\\n      metric: exp_id\\\\n  - row: 2\\\\n    col: 0\\\\n    value: '007'\\\\n    source:\\\\n      exp_id: exp_007_fixed_dt4\\\\n      metric: exp_id\\\\n  - row: 3\\\\n    col: 0\\\\n    value: '005'\\\\n    source:\\\\n      exp_id: exp_005_event_gated_v4\\\\n      metric: exp_id\\\\n  - row: 4\\\\n    col: 0\\\\n    value: 008d\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: exp_id\\\\n  - row: 5\\\\n    col: 0\\\\n    value: 008f\\\\n    source:\\\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n      metric: exp_id\\\\n  - row: 6\\\\n    col: 0\\\\n    value: 008a\\\\n    source:\\\\n      exp_id: exp_008a_no_subsample_dt2\\\\n      metric: exp_id\\\\n  - row: 7\\\\n    col: 0\\\\n    value: 008c\\\\n    source:\\\\n      exp_id: exp_008c_no_subsample_dt2_h8\\\\n      metric: exp_id\\\\n  - row: 8\\\\n    col: 0\\\\n    value: 008e_v3\\\\n    source:\\\\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\\\\n      metric: exp_id\\\\n  deprecated: false\\\\n- id: T002\\\\n  location:\\\\n    section: results\\\\n    table_number: 1\\\\n  caption: All configurations and outcomes\\\\n  cells:\\\\n  - row: 0\\\\n    col: 5\\\\n    value: 915.7\\\\n    source:\\\\n      exp_id: exp_001_baseline\\\\n      metric: eval_return_105K\\\\n  - row: 1\\\\n    col: 5\\\\n    value: 132.9\\\\n    source:\\\\n      exp_id: exp_006_fixed_dt2\\\\n      metric: eval_return_65K\\\\n  - row: 1\\\\n    col: 6\\\\n    value: 4.83\\\\n    source:\\\\n      exp_id: exp_006_fixed_dt2\\\\n      metric: peak_nve\\\\n  - row: 2\\\\n    col: 5\\\\n    value: 152.5\\\\n    source:\\\\n      exp_id: exp_007_fixed_dt4\\\\n      metric: eval_return_55K\\\\n  - row: 3\\\\n    col: 5\\\\n    value: 98.8\\\\n    source:\\\\n      exp_id: exp_005_event_gated_v4\\\\n      metric: eval_return_145K\\\\n  - row: 4\\\\n    col: 5\\\\n    value: 82.8\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: eval_return_55K\\\\n  - row: 4\\\\n    col: 6\\\\n    value: 4.12\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: peak_nve\\\\n  - row: 5\\\\n    col: 5\\\\n    value: 267.9\\\\n    source:\\\\n      exp_id: exp_009b_008d_walker_s2\\\\n      metric: final_eval_return\\\\n  - row: 5\\\\n    col: 6\\\\n    value: 1.62\\\\n    source:\\\\n      exp_id: exp_009b_008d_walker_s2\\\\n      metric: peak_nve\\\\n  - row: 6\\\\n    col: 5\\\\n    value: 131.1\\\\n    source:\\\\n      exp_id: exp_009e_008d_walker_s1\\\\n      metric: final_eval_return\\\\n  - row: 6\\\\n    col: 6\\\\n    value: 4.12\\\\n    source:\\\\n      exp_id: exp_009e_008d_walker_s1\\\\n      metric: peak_nve\\\\n  - row: 7\\\\n    col: 5\\\\n    value: 503.0\\\\n    source:\\\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n      metric: eval_return_105K\\\\n  - row: 8\\\\n    col: 5\\\\n    value: 148.3\\\\n    source:\\\\n      exp_id: exp_009c_008f_walker_s2\\\\n      metric: final_eval_return\\\\n  - row: 9\\\\n    col: 5\\\\n    value: 777.7\\\\n    source:\\\\n      exp_id: exp_008a_no_subsample_dt2\\\\n      metric: eval_return_105K\\\\n  - row: 10\\\\n    col: 5\\\\n    value: 240.9\\\\n    source:\\\\n      exp_id: exp_008c_no_subsample_dt2_h8\\\\n      metric: eval_return_65K\\\\n  - row: 11\\\\n    col: 5\\\\n    value: 869.9\\\\n    source:\\\\n      exp_id: exp_008e_v3_walker_s1\\\\n      metric: final_eval_return\\\\n  - row: 12\\\\n    col: 5\\\\n    value: 137.0\\\\n    source:\\\\n      exp_id: exp_008e_v3_walker_s2\\\\n      metric: final_eval_return\\\\n  - row: 12\\\\n    col: 6\\\\n    value: 3.78\\\\n    source:\\\\n      exp_id: exp_008e_v3_walker_s2\\\\n      metric: final_nve\\\\n  - row: 13\\\\n    col: 5\\\\n    value: 836.5\\\\n    source:\\\\n      exp_id: exp_009a_baseline_walker_s2\\\\n      metric: final_eval_return\\\\n  deprecated: false\\\\n- id: T003\\\\n  location:\\\\n    section: results\\\\n    table_number: 2\\\\n  caption: RSSM fidelity at dt=1 vs dt=2\\\\n  cells:\\\\n  - row: 0\\\\n    col: 0\\\\n    value: 13.49\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.dt1_obs_mse\\\\n  - row: 0\\\\n    col: 1\\\\n    value: 27.5\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.dt2_obs_mse\\\\n  - row: 0\\\\n    col: 2\\\\n    value: 2.04\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.obs_gap\\\\n  - row: 0\\\\n    col: 3\\\\n    value: 0.0102\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.dt1_reward_mae\\\\n  - row: 0\\\\n    col: 4\\\\n    value: 0.0159\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.dt2_reward_mae\\\\n  - row: 0\\\\n    col: 5\\\\n    value: 1.56\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.reward_gap\\\\n  - row: 1\\\\n    col: 0\\\\n    value: 41.31\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.dt1_obs_mse\\\\n  - row: 1\\\\n    col: 1\\\\n    value: 53.67\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.dt2_obs_mse\\\\n  - row: 1\\\\n    col: 2\\\\n    value: 1.3\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.obs_gap\\\\n  - row: 1\\\\n    col: 3\\\\n    value: 0.0568\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.dt1_reward_mae\\\\n  - row: 1\\\\n    col: 4\\\\n    value: 0.1579\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.dt2_reward_mae\\\\n  - row: 1\\\\n    col: 5\\\\n    value: 2.78\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.reward_gap\\\\n  - row: 2\\\\n    col: 0\\\\n    value: 8.01\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.dt1_obs_mse\\\\n  - row: 2\\\\n    col: 1\\\\n    value: 22.04\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.dt2_obs_mse\\\\n  - row: 2\\\\n    col: 2\\\\n    value: 2.75\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.obs_gap\\\\n  - row: 2\\\\n    col: 3\\\\n    value: 0.7469\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.dt1_reward_mae\\\\n  - row: 2\\\\n    col: 4\\\\n    value: 0.7526\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.dt2_reward_mae\\\\n  - row: 2\\\\n    col: 5\\\\n    value: 1.01\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.reward_gap\\\\n  deprecated: false\\\\n- id: T004\\\\n  location:\\\\n    section: results\\\\n    table_number: 3\\\\n  caption: Post-CIVO outcomes for 008d configuration\\\\n  cells:\\\\n  - row: 0\\\\n    col: 0\\\\n    value: 4.12\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: peak_nve\\\\n  - row: 0\\\\n    col: 1\\\\n    value: 4.12\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: peak_nve\\\\n  - row: 0\\\\n    col: 2\\\\n    value: 82.8\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: eval_return_55K\\\\n  - row: 1\\\\n    col: 0\\\\n    value: 1.62\\\\n    source:\\\\n      exp_id: exp_009b_008d_walker_s2\\\\n      metric: peak_nve\\\\n  - row: 1\\\\n    col: 1\\\\n    value: 0.38\\\\n    source:\\\\n      exp_id: exp_009b_008d_walker_s2\\\\n      metric: final_nve\\\\n  - row: 1\\\\n    col: 2\\\\n    value: 267.9\\\\n    source:\\\\n      exp_id: exp_009b_008d_walker_s2\\\\n      metric: final_eval_return\\\\n  - row: 2\\\\n    col: 0\\\\n    value: 4.12\\\\n    source:\\\\n      exp_id: exp_009e_008d_walker_s1\\\\n      metric: peak_nve\\\\n  - row: 2\\\\n    col: 1\\\\n    value: 1.57\\\\n    source:\\\\n      exp_id: exp_009e_008d_walker_s1\\\\n      metric: final_nve\\\\n  - row: 2\\\\n    col: 2\\\\n    value: 131.1\\\\n    source:\\\\n      exp_id: exp_009e_008d_walker_s1\\\\n      metric: final_eval_return\\\\n  deprecated: false\\\\nfigures:\\\\n- id: F001\\\\n  location:\\\\n    section: results\\\\n    figure_number: 1\\\\n  caption: Learning curves for all configurations\\\\n  type: result\\\\n  source:\\\\n    experiments:\\\\n    - exp_id: exp_001_baseline\\\\n    - exp_id: exp_006_fixed_dt2\\\\n    - exp_id: exp_007_fixed_dt4\\\\n    - exp_id: exp_005_event_gated_v4\\\\n    - exp_id: exp_008d_subsample_on_h8\\\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    - exp_id: exp_008a_no_subsample_dt2\\\\n    - exp_id: exp_008e_v3_walker_s1\\\\n  output_path: figures/paper/fig1_learning_curves.pdf\\\\n  deprecated: false\\\\n- id: F002\\\\n  location:\\\\n    section: results\\\\n    figure_number: 2\\\\n  caption: Normalized value-to-eval ratio trajectories\\\\n  type: result\\\\n  source:\\\\n    experiments:\\\\n    - exp_id: exp_008d_subsample_on_h8\\\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    - exp_id: exp_008a_no_subsample_dt2\\\\n    - exp_id: exp_008e_v3_walker_s1\\\\n    - exp_id: exp_009b_008d_walker_s2\\\\n  output_path: figures/paper/fig2_nve_trajectory.pdf\\\\n  deprecated: false\\\\n- id: F003\\\\n  location:\\\\n    section: results\\\\n    figure_number: 3\\\\n  caption: Factorial experiment summary grid\\\\n  type: result\\\\n  source:\\\\n    experiments:\\\\n    - exp_id: exp_008d_subsample_on_h8\\\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    - exp_id: exp_008a_no_subsample_dt2\\\\n    - exp_id: exp_008c_no_subsample_dt2_h8\\\\n  output_path: figures/paper/fig3_factorial_grid.pdf\\\\n  deprecated: false\\\\n- id: F004\\\\n  location:\\\\n    section: results\\\\n    figure_number: 4\\\\n  caption: Peak evaluation return as function of imagination dt\\\\n  type: result\\\\n  source:\\\\n    experiments:\\\\n    - exp_id: exp_001_baseline\\\\n    - exp_id: exp_006_fixed_dt2\\\\n    - exp_id: exp_007_fixed_dt4\\\\n  output_path: figures/paper/fig5_dt_amplification.pdf\\\\n  deprecated: false\\\\n- id: F005\\\\n  location:\\\\n    section: results\\\\n    figure_number: 5\\\\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\\\\n  type: result\\\\n  source:\\\\n    experiments:\\\\n    - exp_id: exp_008d_subsample_on_h8\\\\n    - exp_id: exp_008e_v3_walker_s2\\\\n    - exp_id: exp_009a_baseline_walker_s2\\\\n  output_path: figures/paper/fig6_multiple_pathways.pdf\\\\n  deprecated: false\\\\n- id: F006\\\\n  location:\\\\n    section: sections/appendix\\\\n    figure_number: 0\\\\n  caption: ''\\\\n  type: other\\\\n  source: {}\\\\n  output_path: ''\\\\n  deprecated: false\\\\n_completeness:\\\\n  coverage: 73/77\\\\n  claims: 71\\\\n  tables: 4\\\\n  figures: 6\\\\n  tier_counts:\\\\n    tier1: 0\\\\n    tier2: 73\\\\n    tier3: 4\\\\n    tierX: 0\\\\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\\\\n\\\", \\\"total_chars\\\": 36692, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\\n    of Variable-Rate DreamerV3'\\n  version: 38\\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\\nclaims:\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: every variable-rate configuration of DreamerV3 degrades performance\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions:\\n  - D009\\n  - D015\\n  deprecated: false\\n- id: C002\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 2\\n  text: trained temporal embedding as the causal factor\\n  type: methodological\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: control\\n  decisions:\\n  - D021\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 3\\n  text: 2.78x prediction gap between dt=1 and dt=2\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C004\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 4\\n  text: 7/8 classification (n=8)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_006_fixed_dt2\\n    metric: model_loss_at_55k\\n    value: 4.853\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C005\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 5\\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\\n    degradation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: full_collapse\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_eval_return\\n    value: 267.93\\n    role: transient_civo\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_eval_return\\n    value: 131.08\\n    role: oscillatory\\n  decisions: []\\n  deprecated: false\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 6\\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\\n    fails'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s1\\n    metric: final_eval_return\\n    value: 869.9\\n    role: healthy\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: collapsed\\n  - exp_id: exp_009a_baseline_walker_s2\\n    metric: final_eval_return\\n    value: 836.51\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C007\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: fixed dt=2 collapses to 14% of baseline\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C008\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: fixed dt=4 never exceeds 19% of baseline\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C009\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: learned Gumbel-Softmax gate collapses to 11%\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C010\\n  location:\\n    section: methodology\\n    paragraph: 8\\n    sentence: 0\\n  text: baseline runs for 500K steps, peak return 970.4\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_001_baseline\\n    metric: eval_return_peak\\n    value: 970.41\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C011\\n  location:\\n    section: methodology\\n    paragraph: 6\\n    sentence: 3\\n  text: 7/8 accuracy (AUROC=0.933)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions:\\n  - D053\\n  - D054\\n  deprecated: false\\n- id: C012\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 1\\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_001_baseline\\n    metric: eval_return_peak\\n    value: 970.41\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 2\\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: peak_return\\n    value: 485.3\\n    role: primary_evidence\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C014\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 3\\n  text: fixed dt=4 peaks at 176.9 at 25K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C015\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 4\\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_005_event_gated_v4\\n    metric: peak_return\\n    value: 541.18\\n    role: primary_evidence\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: results\\n    paragraph: 3\\n    sentence: 0\\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_25K\\n    value: 167.22\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: results\\n    paragraph: 3\\n    sentence: 1\\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C018\\n  location:\\n    section: results\\n    paragraph: 4\\n    sentence: 0\\n  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D054\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: results\\n    paragraph: 4\\n    sentence: 1\\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions: []\\n  deprecated: false\\n- id: C020\\n  location:\\n    section: results\\n    paragraph: 6\\n    sentence: 0\\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C021\\n  location:\\n    section: results\\n    paragraph: 7\\n    sentence: 0\\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\\n    267.9'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_eval_return\\n    value: 267.93\\n    role: primary_evidence\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_nve\\n    value: 0.38\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C022\\n  location:\\n    section: results\\n    paragraph: 8\\n    sentence: 0\\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\\n    final 1.57x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_eval_return\\n    value: 131.08\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_nve\\n    value: 1.57\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C023\\n  location:\\n    section: results\\n    paragraph: 10\\n    sentence: 0\\n  text: 008a reaches 777.7 (NVE=0.59x)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008a_no_subsample_dt2\\n    metric: eval_return_105K\\n    value: 777.66\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: results\\n    paragraph: 10\\n    sentence: 0\\n  text: 008c reaches 240.9 (NVE=0.58x)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008c_no_subsample_dt2_h8\\n    metric: eval_return_65K\\n    value: 240.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: results\\n    paragraph: 12\\n    sentence: 0\\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: peak_return\\n    value: 485.3\\n    role: primary_evidence\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: results\\n    paragraph: 14\\n    sentence: 0\\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: results\\n    paragraph: 14\\n    sentence: 1\\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: primary_evidence\\n  - exp_id: exp_009c_008f_walker_s2\\n    metric: final_eval_return\\n    value: 148.34\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: results\\n    paragraph: 16\\n    sentence: 0\\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s1\\n    metric: final_eval_return\\n    value: 869.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: results\\n    paragraph: 16\\n    sentence: 1\\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: primary_evidence\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: peak_eval_return\\n    value: 715.21\\n    role: primary_evidence\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: results\\n    paragraph: 17\\n    sentence: 0\\n  text: baseline seed 2 (009a) stable at 836.5\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009a_baseline_walker_s2\\n    metric: final_eval_return\\n    value: 836.51\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: results\\n    paragraph: 18\\n    sentence: 1\\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: results\\n    paragraph: 19\\n    sentence: 0\\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 0\\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 1\\n  text: 008f reward gap 1.01x (MAE 0.7469)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.reward_gap\\n    value: 1.01\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 1\\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\n    value: 0.7469\\n    role: primary_evidence\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\n    value: 0.0568\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 0\\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\\n    2.90x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: random_policy_reward_ratio\\n    value: 1.68\\n    role: stage1\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: trained_actor_reward_ratio\\n    value: 2.9\\n    role: stage2\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 1\\n  text: ~36% dynamics bias, ~64% actor exploitation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: dynamics_bias_fraction\\n    value: 0.36\\n    role: primary_evidence\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 2\\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: random_policy_reward_ratio\\n    value: 1.11\\n    role: control\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: trained_actor_reward_ratio\\n    value: 0.98\\n    role: control\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: analysis\\n    paragraph: 4\\n    sentence: 0\\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: analysis\\n    paragraph: 7\\n    sentence: 0\\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\n    value: 0.7469\\n    role: primary_evidence\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\n    value: 0.0568\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C041\\n  location:\\n    section: analysis\\n    paragraph: 8\\n    sentence: 1\\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 2\\n  text: 7/8 CIVO classification (n=8, 87.5%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C043\\n  location:\\n    section: conclusion\\n    paragraph: 2\\n    sentence: 1\\n  text: NVE margin 0.62 excluding outlier\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: lowest_true_positive\\n  decisions: []\\n  deprecated: false\\n- id: C044\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C046\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\\n    healthy, return collapses ~35K steps before entropy rises'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C047\\n  location:\\n    section: sections/methodology\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  - exp_id: plan_034_nve_threshold\\n    metric: f1_at_1.5x\\n    value: 0.88\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C048\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: sections/abstract_body\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C050\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 classification in introduction\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C051\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Contribution 1 AUROC updated to 0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C052\\n  location:\\n    section: sections/conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C053\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C055\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_064_value_distribution\\n    metric: civo_median_v_mc_ratio\\n    value: 3.4\\n    role: primary_evidence\\n  - exp_id: exp_064_value_distribution\\n    metric: control_median_v_mc_ratio\\n    value: 1.05\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C056\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\\n    vs +0.07-0.22 healthy'\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_031_actor_entropy\\n    metric: collapsed_entropy_rate\\n    value: 2.1\\n    role: primary_evidence\\n  - exp_id: plan_031_actor_entropy\\n    metric: healthy_entropy_rate_range\\n    value: 0.07-0.22\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C057\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C058\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\\n    Cheetah'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_026_obs_sgs_cheetah\\n    metric: nve_amplification\\n    value: 21.9-30.2\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C059\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\\n    baseline'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_030c_tcn_cheetah\\n    metric: nve_suppressed\\n    value: 0.3\\n    role: primary_evidence\\n  - exp_id: exp_030c_tcn_cheetah\\n    metric: eval_pct_baseline\\n    value: 15\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\\n    to -0.86 at 75K'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: trained_cos_25k_range\\n    value: -0.87 to -0.94\\n    role: primary_evidence\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: trained_cos_75k_range\\n    value: -0.70 to -0.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: frozen_cos_constant\\n    value: -0.15 to +0.07\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C062\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\\n    conditioning\\n  type: quantitative\\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\\n  decisions: []\\n  deprecated: false\\n- id: C064\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\\n    vs baseline 1.46x)\\n  type: quantitative\\n  evidence: exp_063 obs_mse data\\n  decisions: []\\n  deprecated: false\\n- id: C065\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\\n    median 1.05x (52.5% overestimated)\\n  type: quantitative\\n  evidence: exp_064 value_distribution results_summary\\n  decisions: []\\n  deprecated: false\\n- id: C066\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\\n    pathology\\n  type: quantitative\\n  evidence: exp_063 rssm_fidelity_analysis\\n  decisions: []\\n  deprecated: false\\n- id: C067\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\\n  type: quantitative\\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\\n  decisions: []\\n  deprecated: false\\n- id: C068\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\\n    improvement\\n  type: quantitative\\n  evidence: exp_066 timeseries analysis\\n  decisions: []\\n  deprecated: false\\n- id: C069\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\\n    → entropy destabilization (~35K later), n=1'\\n  type: quantitative\\n  evidence: exp_066 timeseries + actor entropy analysis\\n  decisions: []\\n  deprecated: false\\n- id: C070\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\\n    VE ratio near zero until 40K spike (1.59x)'\\n  type: quantitative\\n  evidence: exp_066 12-checkpoint timeseries analysis\\n  decisions: []\\n  deprecated: false\\n- id: C071\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\\n    selective improvement not worsening\\n  type: quantitative\\n  evidence: exp_066 timeseries MAE data\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: T001\\n  location:\\n    section: methodology\\n    table_number: 1\\n  caption: Factorial design — 9 configurations\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: '001'\\n    source:\\n      exp_id: exp_001_baseline\\n      metric: exp_id\\n  - row: 1\\n    col: 0\\n    value: '006'\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: exp_id\\n  - row: 2\\n    col: 0\\n    value: '007'\\n    source:\\n      exp_id: exp_007_fixed_dt4\\n      metric: exp_id\\n  - row: 3\\n    col: 0\\n    value: '005'\\n    source:\\n      exp_id: exp_005_event_gated_v4\\n      metric: exp_id\\n  - row: 4\\n    col: 0\\n    value: 008d\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: exp_id\\n  - row: 5\\n    col: 0\\n    value: 008f\\n    source:\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n      metric: exp_id\\n  - row: 6\\n    col: 0\\n    value: 008a\\n    source:\\n      exp_id: exp_008a_no_subsample_dt2\\n      metric: exp_id\\n  - row: 7\\n    col: 0\\n    value: 008c\\n    source:\\n      exp_id: exp_008c_no_subsample_dt2_h8\\n      metric: exp_id\\n  - row: 8\\n    col: 0\\n    value: 008e_v3\\n    source:\\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\\n      metric: exp_id\\n  deprecated: false\\n- id: T002\\n  location:\\n    section: results\\n    table_number: 1\\n  caption: All configurations and outcomes\\n  cells:\\n  - row: 0\\n    col: 5\\n    value: 915.7\\n    source:\\n      exp_id: exp_001_baseline\\n      metric: eval_return_105K\\n  - row: 1\\n    col: 5\\n    value: 132.9\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: eval_return_65K\\n  - row: 1\\n    col: 6\\n    value: 4.83\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: peak_nve\\n  - row: 2\\n    col: 5\\n    value: 152.5\\n    source:\\n      exp_id: exp_007_fixed_dt4\\n      metric: eval_return_55K\\n  - row: 3\\n    col: 5\\n    value: 98.8\\n    source:\\n      exp_id: exp_005_event_gated_v4\\n      metric: eval_return_145K\\n  - row: 4\\n    col: 5\\n    value: 82.8\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: eval_return_55K\\n  - row: 4\\n    col: 6\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 5\\n    col: 5\\n    value: 267.9\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_eval_return\\n  - row: 5\\n    col: 6\\n    value: 1.62\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: peak_nve\\n  - row: 6\\n    col: 5\\n    value: 131.1\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_eval_return\\n  - row: 6\\n    col: 6\\n    value: 4.12\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: peak_nve\\n  - row: 7\\n    col: 5\\n    value: 503.0\\n    source:\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n      metric: eval_return_105K\\n  - row: 8\\n    col: 5\\n    value: 148.3\\n    source:\\n      exp_id: exp_009c_008f_walker_s2\\n      metric: final_eval_return\\n  - row: 9\\n    col: 5\\n    value: 777.7\\n    source:\\n      exp_id: exp_008a_no_subsample_dt2\\n      metric: eval_return_105K\\n  - row: 10\\n    col: 5\\n    value: 240.9\\n    source:\\n      exp_id: exp_008c_no_subsample_dt2_h8\\n      metric: eval_return_65K\\n  - row: 11\\n    col: 5\\n    value: 869.9\\n    source:\\n      exp_id: exp_008e_v3_walker_s1\\n      metric: final_eval_return\\n  - row: 12\\n    col: 5\\n    value: 137.0\\n    source:\\n      exp_id: exp_008e_v3_walker_s2\\n      metric: final_eval_return\\n  - row: 12\\n    col: 6\\n    value: 3.78\\n    source:\\n      exp_id: exp_008e_v3_walker_s2\\n      metric: final_nve\\n  - row: 13\\n    col: 5\\n    value: 836.5\\n    source:\\n      exp_id: exp_009a_baseline_walker_s2\\n      metric: final_eval_return\\n  deprecated: false\\n- id: T003\\n  location:\\n    section: results\\n    table_number: 2\\n  caption: RSSM fidelity at dt=1 vs dt=2\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: 13.49\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt1_obs_mse\\n  - row: 0\\n    col: 1\\n    value: 27.5\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt2_obs_mse\\n  - row: 0\\n    col: 2\\n    value: 2.04\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.obs_gap\\n  - row: 0\\n    col: 3\\n    value: 0.0102\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt1_reward_mae\\n  - row: 0\\n    col: 4\\n    value: 0.0159\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt2_reward_mae\\n  - row: 0\\n    col: 5\\n    value: 1.56\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.reward_gap\\n  - row: 1\\n    col: 0\\n    value: 41.31\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt1_obs_mse\\n  - row: 1\\n    col: 1\\n    value: 53.67\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt2_obs_mse\\n  - row: 1\\n    col: 2\\n    value: 1.3\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.obs_gap\\n  - row: 1\\n    col: 3\\n    value: 0.0568\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt1_reward_mae\\n  - row: 1\\n    col: 4\\n    value: 0.1579\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt2_reward_mae\\n  - row: 1\\n    col: 5\\n    value: 2.78\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.reward_gap\\n  - row: 2\\n    col: 0\\n    value: 8.01\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt1_obs_mse\\n  - row: 2\\n    col: 1\\n    value: 22.04\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt2_obs_mse\\n  - row: 2\\n    col: 2\\n    value: 2.75\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.obs_gap\\n  - row: 2\\n    col: 3\\n    value: 0.7469\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt1_reward_mae\\n  - row: 2\\n    col: 4\\n    value: 0.7526\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt2_reward_mae\\n  - row: 2\\n    col: 5\\n    value: 1.01\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.reward_gap\\n  deprecated: false\\n- id: T004\\n  location:\\n    section: results\\n    table_number: 3\\n  caption: Post-CIVO outcomes for 008d configuration\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 0\\n    col: 1\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 0\\n    col: 2\\n    value: 82.8\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: eval_return_55K\\n  - row: 1\\n    col: 0\\n    value: 1.62\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: peak_nve\\n  - row: 1\\n    col: 1\\n    value: 0.38\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_nve\\n  - row: 1\\n    col: 2\\n    value: 267.9\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_eval_return\\n  - row: 2\\n    col: 0\\n    value: 4.12\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: peak_nve\\n  - row: 2\\n    col: 1\\n    value: 1.57\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_nve\\n  - row: 2\\n    col: 2\\n    value: 131.1\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_eval_return\\n  deprecated: false\\nfigures:\\n- id: F001\\n  location:\\n    section: results\\n    figure_number: 1\\n  caption: Learning curves for all configurations\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_001_baseline\\n    - exp_id: exp_006_fixed_dt2\\n    - exp_id: exp_007_fixed_dt4\\n    - exp_id: exp_005_event_gated_v4\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008e_v3_walker_s1\\n  output_path: figures/paper/fig1_learning_curves.pdf\\n  deprecated: false\\n- id: F002\\n  location:\\n    section: results\\n    figure_number: 2\\n  caption: Normalized value-to-eval ratio trajectories\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008e_v3_walker_s1\\n    - exp_id: exp_009b_008d_walker_s2\\n  output_path: figures/paper/fig2_nve_trajectory.pdf\\n  deprecated: false\\n- id: F003\\n  location:\\n    section: results\\n    figure_number: 3\\n  caption: Factorial experiment summary grid\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008c_no_subsample_dt2_h8\\n  output_path: figures/paper/fig3_factorial_grid.pdf\\n  deprecated: false\\n- id: F004\\n  location:\\n    section: results\\n    figure_number: 4\\n  caption: Peak evaluation return as function of imagination dt\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_001_baseline\\n    - exp_id: exp_006_fixed_dt2\\n    - exp_id: exp_007_fixed_dt4\\n  output_path: figures/paper/fig5_dt_amplification.pdf\\n  deprecated: false\\n- id: F005\\n  location:\\n    section: results\\n    figure_number: 5\\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008e_v3_walker_s2\\n    - exp_id: exp_009a_baseline_walker_s2\\n  output_path: figures/paper/fig6_multiple_pathways.pdf\\n  deprecated: false\\n- id: F006\\n  location:\\n    section: sections/appendix\\n    figure_number: 0\\n  caption: ''\\n  type: other\\n  source: {}\\n  output_path: ''\\n  deprecated: false\\n_completeness:\\n  coverage: 73/77\\n  claims: 71\\n  tables: 4\\n  figures: 6\\n  tier_counts:\\n    tier1: 0\\n    tier2: 73\\n    tier3: 4\\n    tierX: 0\\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\\n\", \"total_chars\": 36692, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
I've read the full provenance file. Now I need to identify all entries that need updating. Let me analyze:

**C047-C053 (explicitly NVE threshold entries):**
- C047: "NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32" → needs update to 53/56, AUROC=0.990, F1=0.941, n=56
- C048: "NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)" → same update


- C049: "CIVO classification 29/32 AUROC=0.961 F1=0.880" → same update
- C050: "NVE threshold 29/32 classification in introduction" → same update
- C051: "Contribution 1 AUROC updated to 0.961" → update to 0.990
- C052: "Conclusion NVE updated to 29/32 AUROC=0.961" → update to 53/56 AUROC=0.990
- C053: "Discussion NVE diagnostic consolidated to n=32 AUROC=0.961" → update to n=56 AUROC=0.990

Now I'm working through the NVE validation entries that also need updating from the smaller dataset to the expanded one. C044 and C045 both reference the old n=32 metrics with F1=0.880 and AUROC=0.961, which should shift to n=56 with F1=0.941 and AUROC=0.990. I also need to track down the older entries using n=8 data—C004, C011, C018, and C042 all cite the 7/8 classification or AUROC=0.933 figures that need to be replaced with the 53/56 classification and AUROC=0.990.

Let me pull up the paper_provenance.yaml file to make these corrections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "59793f82-6448-4806-a843-27d4a365be5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLWqmwa8c5G97AeBGgHiL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15742,
      "cache_read_input_tokens": 23910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15742
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


### Assistant

_source line 11_

I've identified all NVE-related entries needing updates. Let me read the actual file and make edits.

Entries to update:
- **Old n=8 data**: C004, C011, C018, C042
- **Old n=32 data**: C044, C045, C047, C048, C049, C050, C051, C052, C053

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "b3254db6-8aa4-49ef-bf03-059c7ac3b316",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLWqmwa8c5G97AeBGgHiL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15742,
      "cache_read_input_tokens": 23910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15742
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01HUqz3NfsbwTkUWVQ5TbBSh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "bee5004a-fbee-4127-a18f-8535b8b7abac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLWqmwa8c5G97AeBGgHiL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15742,
      "cache_read_input_tokens": 23910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15742
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

_source line 13 · 2026-05-25T14:11:37.510Z_

<details><summary>↩ Tool result · `toolu_01HUqz3NfsbwTkUWVQ5TbBSh`</summary>

```text
1	paper:
2	  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis
3	    of Variable-Rate DreamerV3'
4	  version: 38
5	  generated_at: '2026-05-25T03:36:26.589946+00:00'
6	  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness
7	claims:
8	- id: C001
9	  location:
10	    section: abstract
11	    paragraph: 0
12	    sentence: 0
13	  text: every variable-rate configuration of DreamerV3 degrades performance
14	  type: quantitative
15	  evidence:
16	  - exp_id: exp_006_fixed_dt2
17	    metric: eval_return_65K
18	    value: 132.86
19	    role: primary_evidence
20	  - exp_id: exp_007_fixed_dt4
21	    metric: peak_return
22	    value: 176.9
23	    role: primary_evidence
24	  - exp_id: exp_005_event_gated_v4
25	    metric: eval_return_145K
26	    value: 98.84
27	    role: primary_evidence
28	  decisions:
29	  - D009
30	  - D015
31	  deprecated: false
32	- id: C002
33	  location:
34	    section: abstract
35	    paragraph: 0
36	    sentence: 2
37	  text: trained temporal embedding as the causal factor
38	  type: methodological
39	  evidence:
40	  - exp_id: exp_008d_subsample_on_h8
41	    metric: eval_return_55K
42	    value: 82.75
43	    role: primary_evidence
44	  - exp_id: exp_008f_no_dt_embed_subsample_on_h8
45	    metric: eval_return_105K
46	    value: 503.0
47	    role: control
48	  decisions:
49	  - D021
50	  deprecated: false
51	- id: C003
52	  location:
53	    section: abstract
54	    paragraph: 0
55	    sentence: 3
56	  text: 2.78x prediction gap between dt=1 and dt=2
57	  type: quantitative
58	  evidence:
59	  - exp_id: exp_rssm_fidelity_analysis
60	    metric: 008d_trained_dtEmb.reward_gap
61	    value: 2.78
62	    role: primary_evidence
63	  decisions: []
64	  deprecated: false
65	- id: C004
66	  location:
67	    section: abstract
68	    paragraph: 0
69	    sentence: 4
70	  text: 7/8 classification (n=8)
71	  type: quantitative
72	  evidence:
73	  - exp_id: exp_008d_subsample_on_h8
74	    metric: peak_nve
75	    value: 4.12
76	    role: true_positive
77	  - exp_id: exp_006_fixed_dt2
78	    metric: model_loss_at_55k
79	    value: 4.853
80	    role: true_positive
81	  - exp_id: exp_009b_008d_walker_s2
82	    metric: peak_nve
83	    value: 1.62
84	    role: true_positive
85	  - exp_id: exp_008e_v3_walker_s2
86	    metric: final_nve
87	    value: 3.78
88	    role: false_positive
89	  decisions:
90	  - D053
91	  deprecated: false
92	- id: C005
93	  location:
94	    section: abstract
95	    paragraph: 0
96	    sentence: 5
97	  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory
98	    degradation
99	  type: quantitative
100	  evidence:
101	  - exp_id: exp_008d_subsample_on_h8
102	    metric: eval_return_55K
103	    value: 82.75
104	    role: full_collapse
105	  - exp_id: exp_009b_008d_walker_s2
106	    metric: final_eval_return
107	    value: 267.93
108	    role: transient_civo
109	  - exp_id: exp_009e_008d_walker_s1
110	    metric: final_eval_return
111	    value: 131.08
112	    role: oscillatory
113	  decisions: []
114	  deprecated: false
115	- id: C006
116	  location:
117	    section: abstract
118	    paragraph: 0
119	    sentence: 6
120	  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds
121	    fails'
122	  type: quantitative
123	  evidence:
124	  - exp_id: exp_008e_v3_walker_s1
125	    metric: final_eval_return
126	    value: 869.9
127	    role: healthy
128	  - exp_id: exp_008e_v3_walker_s2
129	    metric: final_eval_return
130	    value: 136.96
131	    role: collapsed
132	  - exp_id: exp_009a_baseline_walker_s2
133	    metric: final_eval_return
134	    value: 836.51
135	    role: control
136	  decisions: []
137	  deprecated: false
138	- id: C007
139	  location:
140	    section: introduction
141	    paragraph: 1
142	    sentence: 1
143	  text: fixed dt=2 collapses to 14% of baseline
144	  type: quantitative
145	  evidence:
146	  - exp_id: exp_006_fixed_dt2
147	    metric: eval_return_65K
148	    value: 132.86
149	    role: primary_evidence
150	  decisions: []
151	  deprecated: false
152	- id: C008
153	  location:
154	    section: introduction
155	    paragraph: 1
156	    sentence: 1
157	  text: fixed dt=4 never exceeds 19% of baseline
158	  type: quantitative
159	  evidence:
160	  - exp_id: exp_007_fixed_dt4
161	    metric: peak_return
162	    value: 176.9
163	    role: primary_evidence
164	  decisions: []
165	  deprecated: false
166	- id: C009
167	  location:
168	    section: introduction
169	    paragraph: 1
170	    sentence: 1
171	  text: learned Gumbel-Softmax gate collapses to 11%
172	  type: quantitative
173	  evidence:
174	  - exp_id: exp_005_event_gated_v4
175	    metric: eval_return_145K
176	    value: 98.84
177	    role: primary_evidence
178	  decisions: []
179	  deprecated: false
180	- id: C010
181	  location:
182	    section: methodology
183	    paragraph: 8
184	    sentence: 0
185	  text: baseline runs for 500K steps, peak return 970.4
186	  type: quantitative
187	  evidence:
188	  - exp_id: exp_001_baseline
189	    metric: eval_return_peak
190	    value: 970.41
191	    role: primary_evidence
192	  decisions: []
193	  deprecated: false
194	- id: C011
195	  location:
196	    section: methodology
197	    paragraph: 6
198	    sentence: 3
199	  text: 7/8 accuracy (AUROC=0.933)
200	  type: quantitative
201	  evidence:
202	  - exp_id: exp_008d_subsample_on_h8
203	    metric: peak_nve
204	    value: 4.12
205	    role: true_positive
206	  - exp_id: exp_009b_008d_walker_s2
207	    metric: peak_nve
208	    value: 1.62
209	    role: true_positive
210	  decisions:
211	  - D053
212	  - D054
213	  deprecated: false
214	- id: C012
215	  location:
216	    section: results
217	    paragraph: 0
218	    sentence: 1
219	  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K
220	  type: quantitative
221	  evidence:
222	  - exp_id: exp_001_baseline
223	    metric: eval_return_peak
224	    value: 970.41
225	    role: primary_evidence
226	  decisions: []
227	  deprecated: false
228	- id: C013
229	  location:
230	    section: results
231	    paragraph: 0
232	    sentence: 2
233	  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K
234	  type: quantitative
235	  evidence:
236	  - exp_id: exp_006_fixed_dt2
237	    metric: peak_return
238	    value: 485.3
239	    role: primary_evidence
240	  - exp_id: exp_006_fixed_dt2
241	    metric: eval_return_65K
242	    value: 132.86
243	    role: primary_evidence
244	  decisions: []
245	  deprecated: false
246	- id: C014
247	  location:
248	    section: results
249	    paragraph: 0
250	    sentence: 3
251	  text: fixed dt=4 peaks at 176.9 at 25K
252	  type: quantitative
253	  evidence:
254	  - exp_id: exp_007_fixed_dt4
255	    metric: peak_return
256	    value: 176.9
257	    role: primary_evidence
258	  decisions: []
259	  deprecated: false
260	- id: C015
261	  location:
262	    section: results
263	    paragraph: 0
264	    sentence: 4
265	  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K
266	  type: quantitative
267	  evidence:
268	  - exp_id: exp_005_event_gated_v4
269	    metric: peak_return
270	    value: 541.18
271	    role: primary_evidence
272	  - exp_id: exp_005_event_gated_v4
273	    metric: eval_return_145K
274	    value: 98.84
275	    role: primary_evidence
276	  decisions: []
277	  deprecated: false
278	- id: C016
279	  location:
280	    section: results
281	    paragraph: 3
282	    sentence: 0
283	  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8
284	  type: quantitative
285	  evidence:
286	  - exp_id: exp_008d_subsample_on_h8
287	    metric: eval_return_55K
288	    value: 82.75
289	    role: primary_evidence
290	  - exp_id: exp_008d_subsample_on_h8
291	    metric: eval_return_25K
292	    value: 167.22
293	    role: primary_evidence
294	  decisions: []
295	  deprecated: false
296	- id: C017
297	  location:
298	    section: results
299	    paragraph: 3
300	    sentence: 1
301	  text: 008f NVE=0.30x at 105K, no collapse eval 503.0
302	  type: quantitative
303	  evidence:
304	  - exp_id: exp_008f_no_dt_embed_subsample_on_h8
305	    metric: eval_return_105K
306	    value: 503.0
307	    role: primary_evidence
308	  decisions: []
309	  deprecated: false
310	- id: C018
311	  location:
312	    section: results
313	    paragraph: 4
314	    sentence: 0
315	  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]
316	  type: quantitative
317	  evidence:
318	  - exp_id: exp_008d_subsample_on_h8
319	    metric: peak_nve
320	    value: 4.12
321	    role: true_positive
322	  - exp_id: exp_009b_008d_walker_s2
323	    metric: peak_nve
324	    value: 1.62
325	    role: true_positive
326	  - exp_id: exp_008e_v3_walker_s2
327	    metric: final_nve
328	    value: 3.78
329	    role: false_positive
330	  decisions:
331	  - D054
332	  deprecated: false
333	- id: C019
334	  location:
335	    section: results
336	    paragraph: 4
337	    sentence: 1
338	  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62
339	  type: quantitative
340	  evidence:
341	  - exp_id: exp_009b_008d_walker_s2
342	    metric: peak_nve
343	    value: 1.62
344	    role: true_positive
345	  decisions: []
346	  deprecated: false
347	- id: C020
348	  location:
349	    section: results
350	    paragraph: 6
351	    sentence: 0
352	  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'
353	  type: quantitative
354	  evidence:
355	  - exp_id: exp_008d_subsample_on_h8
356	    metric: eval_return_55K
357	    value: 82.75
358	    role: primary_evidence
359	  decisions: []
360	  deprecated: false
361	- id: C021
362	  location:
363	    section: results
364	    paragraph: 7
365	    sentence: 0
366	  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval
367	    267.9'
368	  type: quantitative
369	  evidence:
370	  - exp_id: exp_009b_008d_walker_s2
371	    metric: final_eval_return
372	    value: 267.93
373	    role: primary_evidence
374	  - exp_id: exp_009b_008d_walker_s2
375	    metric: final_nve
376	    value: 0.38
377	    role: primary_evidence
378	  decisions: []
379	  deprecated: false
380	- id: C022
381	  location:
382	    section: results
383	    paragraph: 8
384	    sentence: 0
385	  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,
386	    final 1.57x'
387	  type: quantitative
388	  evidence:
389	  - exp_id: exp_009e_008d_walker_s1
390	    metric: final_eval_return
391	    value: 131.08
392	    role: primary_evidence
393	  - exp_id: exp_009e_008d_walker_s1
394	    metric: final_nve
395	    value: 1.57
396	    role: primary_evidence
397	  - exp_id: exp_009e_008d_walker_s1
398	    metric: peak_nve
399	    value: 4.12
400	    role: primary_evidence
401	  decisions: []
402	  deprecated: false
403	- id: C023
404	  location:
405	    section: results
406	    paragraph: 10
407	    sentence: 0
408	  text: 008a reaches 777.7 (NVE=0.59x)
409	  type: quantitative
410	  evidence:
411	  - exp_id: exp_008a_no_subsample_dt2
412	    metric: eval_return_105K
413	    value: 777.66
414	    role: primary_evidence
415	  decisions: []
416	  deprecated: false
417	- id: C024
418	  location:
419	    section: results
420	    paragraph: 10
421	    sentence: 0
422	  text: 008c reaches 240.9 (NVE=0.58x)
423	  type: quantitative
424	  evidence:
425	  - exp_id: exp_008c_no_subsample_dt2_h8
426	    metric: eval_return_65K
427	    value: 240.86
428	    role: primary_evidence
429	  decisions: []
430	  deprecated: false
431	- id: C025
432	  location:
433	    section: results
434	    paragraph: 12
435	    sentence: 0
436	  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)
437	  type: quantitative
438	  evidence:
439	  - exp_id: exp_006_fixed_dt2
440	    metric: peak_return
441	    value: 485.3
442	    role: primary_evidence
443	  - exp_id: exp_007_fixed_dt4
444	    metric: peak_return
445	    value: 176.9
446	    role: primary_evidence
447	  decisions: []
448	  deprecated: false
449	- id: C026
450	  location:
451	    section: results
452	    paragraph: 14
453	    sentence: 0
454	  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x
455	  type: quantitative
456	  evidence:
457	  - exp_id: exp_008d_subsample_on_h8
458	    metric: eval_return_55K
459	    value: 82.75
460	    role: primary_evidence
461	  decisions: []
462	  deprecated: false
463	- id: C027
464	  location:
465	    section: results
466	    paragraph: 14
467	    sentence: 1
468	  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'
469	  type: quantitative
470	  evidence:
471	  - exp_id: exp_008f_no_dt_embed_subsample_on_h8
472	    metric: eval_return_105K
473	    value: 503.0
474	    role: primary_evidence
475	  - exp_id: exp_009c_008f_walker_s2
476	    metric: final_eval_return
477	    value: 148.34
478	    role: primary_evidence
479	  decisions: []
480	  deprecated: false
481	- id: C028
482	  location:
483	    section: results
484	    paragraph: 16
485	    sentence: 0
486	  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'
487	  type: quantitative
488	  evidence:
489	  - exp_id: exp_008e_v3_walker_s1
490	    metric: final_eval_return
491	    value: 869.9
492	    role: primary_evidence
493	  decisions: []
494	  deprecated: false
495	- id: C029
496	  location:
497	    section: results
498	    paragraph: 16
499	    sentence: 1
500	  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'
501	  type: quantitative
502	  evidence:
503	  - exp_id: exp_008e_v3_walker_s2
504	    metric: final_eval_return
505	    value: 136.96
506	    role: primary_evidence
507	  - exp_id: exp_008e_v3_walker_s2
508	    metric: peak_eval_return
509	    value: 715.21
510	    role: primary_evidence
511	  - exp_id: exp_008e_v3_walker_s2
512	    metric: final_nve
513	    value: 3.78
514	    role: primary_evidence
515	  decisions: []
516	  deprecated: false
517	- id: C030
518	  location:
519	    section: results
520	    paragraph: 17
521	    sentence: 0
522	  text: baseline seed 2 (009a) stable at 836.5
523	  type: quantitative
524	  evidence:
525	  - exp_id: exp_009a_baseline_walker_s2
526	    metric: final_eval_return
527	    value: 836.51
528	    role: control
529	  decisions: []
530	  deprecated: false
531	- id: C031
532	  location:
533	    section: results
534	    paragraph: 18
535	    sentence: 1
536	  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'
537	  type: quantitative
538	  evidence:
539	  - exp_id: exp_008e_v3_walker_s2
540	    metric: final_eval_return
541	    value: 136.96
542	    role: primary_evidence
543	  decisions: []
544	  deprecated: false
545	- id: C032
546	  location:
547	    section: results
548	    paragraph: 19
549	    sentence: 0
550	  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)
551	  type: quantitative
552	  evidence:
553	  - exp_id: exp_008e_v3_walker_s2
554	    metric: final_nve
555	    value: 3.78
556	    role: false_positive
557	  decisions:
558	  - D053
559	  deprecated: false
560	- id: C033
561	  location:
562	    section: results
563	    paragraph: 21
564	    sentence: 0
565	  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)
566	  type: quantitative
567	  evidence:
568	  - exp_id: exp_rssm_fidelity_analysis
569	    metric: 008d_trained_dtEmb.reward_gap
570	    value: 2.78
571	    role: primary_evidence
572	  decisions: []
573	  deprecated: false
574	- id: C034
575	  location:
576	    section: results
577	    paragraph: 21
578	    sentence: 1
579	  text: 008f reward gap 1.01x (MAE 0.7469)
580	  type: quantitative
581	  evidence:
582	  - exp_id: exp_rssm_fidelity_analysis
583	    metric: 008f_no_dtEmb.reward_gap
584	    value: 1.01
585	    role: primary_evidence
586	  decisions: []
587	  deprecated: false
588	- id: C035
589	  location:
590	    section: results
591	    paragraph: 21
592	    sentence: 1
593	  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1
594	  type: quantitative
595	  evidence:
596	  - exp_id: exp_rssm_fidelity_analysis
597	    metric: 008f_no_dtEmb.dt1_reward_mae
598	    value: 0.7469
599	    role: primary_evidence
600	  - exp_id: exp_rssm_fidelity_analysis
601	    metric: 008d_trained_dtEmb.dt1_reward_mae
602	    value: 0.0568
603	    role: primary_evidence
604	  decisions: []
605	  deprecated: false
606	- id: C036
607	  location:
608	    section: analysis
609	    paragraph: 2
610	    sentence: 0
611	  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation
612	    2.90x'
613	  type: quantitative
614	  evidence:
615	  - exp_id: exp_008d_subsample_on_h8
616	    metric: random_policy_reward_ratio
617	    value: 1.68
618	    role: stage1
619	  - exp_id: exp_008d_subsample_on_h8
620	    metric: trained_actor_reward_ratio
621	    value: 2.9
622	    role: stage2
623	  decisions:
624	  - D042
625	  deprecated: false
626	- id: C037
627	  location:
628	    section: analysis
629	    paragraph: 2
630	    sentence: 1
631	  text: ~36% dynamics bias, ~64% actor exploitation
632	  type: quantitative
633	  evidence:
634	  - exp_id: exp_008d_subsample_on_h8
635	    metric: dynamics_bias_fraction
636	    value: 0.36
637	    role: primary_evidence
638	  decisions:
639	  - D042
640	  deprecated: false
641	- id: C038
642	  location:
643	    section: analysis
644	    paragraph: 2
645	    sentence: 2
646	  text: '008f control: random 1.11x, trained 0.98x — no effect'
647	  type: quantitative
648	  evidence:
649	  - exp_id: exp_008f_no_dt_embed_subsample_on_h8
650	    metric: random_policy_reward_ratio
651	    value: 1.11
652	    role: control
653	  - exp_id: exp_008f_no_dt_embed_subsample_on_h8
654	    metric: trained_actor_reward_ratio
655	    value: 0.98
656	    role: control
657	  decisions:
658	  - D042
659	  deprecated: false
660	- id: C039
661	  location:
662	    section: analysis
663	    paragraph: 4
664	    sentence: 0
665	  text: all runs cross NVE>1.5x — CIVO triggers deterministically
666	  type: quantitative
667	  evidence:
668	  - exp_id: exp_008d_subsample_on_h8
669	    metric: peak_nve
670	    value: 4.12
671	    role: primary_evidence
672	  - exp_id: exp_009b_008d_walker_s2
673	    metric: peak_nve
674	    value: 1.62
675	    role: primary_evidence
676	  - exp_id: exp_009e_008d_walker_s1
677	    metric: peak_nve
678	    value: 4.12
679	    role: primary_evidence
680	  decisions: []
681	  deprecated: false
682	- id: C040
683	  location:
684	    section: analysis
685	    paragraph: 7
686	    sentence: 0
687	  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'
688	  type: quantitative
689	  evidence:
690	  - exp_id: exp_rssm_fidelity_analysis
691	    metric: 008f_no_dtEmb.dt1_reward_mae
692	    value: 0.7469
693	    role: primary_evidence
694	  - exp_id: exp_rssm_fidelity_analysis
695	    metric: 008d_trained_dtEmb.dt1_reward_mae
696	    value: 0.0568
697	    role: primary_evidence
698	  decisions: []
699	  deprecated: false
700	- id: C041
701	  location:
702	    section: analysis
703	    paragraph: 8
704	    sentence: 1
705	  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'
706	  type: quantitative
707	  evidence:
708	  - exp_id: exp_008e_v3_walker_s2
709	    metric: final_nve
710	    value: 3.78
711	    role: false_positive
712	  decisions:
713	  - D053
714	  deprecated: false
715	- id: C042
716	  location:
717	    section: conclusion
718	    paragraph: 0
719	    sentence: 2
720	  text: 7/8 CIVO classification (n=8, 87.5%)
721	  type: quantitative
722	  evidence:
723	  - exp_id: exp_008d_subsample_on_h8
724	    metric: peak_nve
725	    value: 4.12
726	    role: true_positive
727	  - exp_id: exp_009b_008d_walker_s2
728	    metric: peak_nve
729	    value: 1.62
730	    role: true_positive
731	  decisions:
732	  - D053
733	  deprecated: false
734	- id: C043
735	  location:
736	    section: conclusion
737	    paragraph: 2
738	    sentence: 1
739	  text: NVE margin 0.62 excluding outlier
740	  type: quantitative
741	  evidence:
742	  - exp_id: exp_009b_008d_walker_s2
743	    metric: peak_nve
744	    value: 1.62
745	    role: lowest_true_positive
746	  decisions: []
747	  deprecated: false
748	- id: C044
749	  location:
750	    section: sections/appendix
751	    paragraph: 0
752	    sentence: 0
753	  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold
754	  type: quantitative
755	  evidence: []
756	  decisions: []
757	  deprecated: false
758	- id: C045
759	  location:
760	    section: sections/analysis
761	    paragraph: 0
762	    sentence: 0
763	  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880
764	  type: quantitative
765	  evidence: []
766	  decisions: []
767	  deprecated: false
768	- id: C046
769	  location:
770	    section: sections/analysis
771	    paragraph: 0
772	    sentence: 0
773	  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22
774	    healthy, return collapses ~35K steps before entropy rises'
775	  type: quantitative
776	  evidence: []
777	  decisions: []
778	  deprecated: false
779	- id: C047
780	  location:
781	    section: sections/methodology
782	    paragraph: 0
783	    sentence: 0
784	  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32
785	  type: quantitative
786	  evidence:
787	  - exp_id: plan_034_nve_threshold
788	    metric: auroc_n32
789	    value: 0.961
790	    role: primary_evidence
791	  - exp_id: plan_034_nve_threshold
792	    metric: f1_at_1.5x
793	    value: 0.88
794	    role: primary_evidence
795	  decisions: []
796	  deprecated: false
797	- id: C048
798	  location:
799	    section: sections/results
800	    paragraph: 0
801	    sentence: 0
802	  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)
803	  type: quantitative
804	  evidence:
805	  - exp_id: plan_034_nve_threshold
806	    metric: auroc_n32
807	    value: 0.961
808	    role: primary_evidence
809	  decisions: []
810	  deprecated: false
811	- id: C049
812	  location:
813	    section: sections/abstract_body
814	    paragraph: 0
815	    sentence: 0
816	  text: CIVO classification 29/32 AUROC=0.961 F1=0.880
817	  type: quantitative
818	  evidence:
819	  - exp_id: plan_034_nve_threshold
820	    metric: auroc_n32
821	    value: 0.961
822	    role: primary_evidence
823	  decisions: []
824	  deprecated: false
825	- id: C050
826	  location:
827	    section: sections/introduction
828	    paragraph: 0
829	    sentence: 0
830	  text: NVE threshold 29/32 classification in introduction
831	  type: quantitative
832	  evidence:
833	  - exp_id: plan_034_nve_threshold
834	    metric: auroc_n32
835	    value: 0.961
836	    role: primary_evidence
837	  decisions: []
838	  deprecated: false
839	- id: C051
840	  location:
841	    section: sections/introduction
842	    paragraph: 0
843	    sentence: 0
844	  text: Contribution 1 AUROC updated to 0.961
845	  type: quantitative
846	  evidence:
847	  - exp_id: plan_034_nve_threshold
848	    metric: auroc_n32
849	    value: 0.961
850	    role: primary_evidence
851	  decisions: []
852	  deprecated: false
853	- id: C052
854	  location:
855	    section: sections/conclusion
856	    paragraph: 0
857	    sentence: 0
858	  text: Conclusion NVE updated to 29/32 AUROC=0.961
859	  type: quantitative
860	  evidence:
861	  - exp_id: plan_034_nve_threshold
862	    metric: auroc_n32
863	    value: 0.961
864	    role: primary_evidence
865	  decisions: []
866	  deprecated: false
867	- id: C053
868	  location:
869	    section: sections/analysis
870	    paragraph: 0
871	    sentence: 0
872	  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961
873	  type: quantitative
874	  evidence:
875	  - exp_id: plan_034_nve_threshold
876	    metric: auroc_n32
877	    value: 0.961
878	    role: primary_evidence
879	  decisions: []
880	  deprecated: false
881	- id: C054
882	  location:
883	    section: sections/results
884	    paragraph: 0
885	    sentence: 0
886	  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation
887	  type: quantitative
888	  evidence:
889	  - exp_id: exp_rssm_fidelity_analysis
890	    metric: 008d_trained_dtEmb.reward_gap
891	    value: 2.78
892	    role: primary_evidence
893	  - exp_id: exp_063_rssm_fidelity
894	    metric: collapsed_reward_gap
895	    value: 3.11
896	    role: corroboration
897	  decisions: []
898	  deprecated: false
899	- id: C055
900	  location:
901	    section: sections/results
902	    paragraph: 0
903	    sentence: 0
904	  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05
905	  type: quantitative
906	  evidence:
907	  - exp_id: exp_064_value_distribution
908	    metric: civo_median_v_mc_ratio
909	    value: 3.4
910	    role: primary_evidence
911	  - exp_id: exp_064_value_distribution
912	    metric: control_median_v_mc_ratio
913	    value: 1.05
914	    role: control
915	  decisions: []
916	  deprecated: false
917	- id: C056
918	  location:
919	    section: sections/results
920	    paragraph: 0
921	    sentence: 0
922	  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed
923	    vs +0.07-0.22 healthy'
924	  type: quantitative
925	  evidence:
926	  - exp_id: plan_031_actor_entropy
927	    metric: collapsed_entropy_rate
928	    value: 2.1
929	    role: primary_evidence
930	  - exp_id: plan_031_actor_entropy
931	    metric: healthy_entropy_rate_range
932	    value: 0.07-0.22
933	    role: control
934	  decisions: []
935	  deprecated: false
936	- id: C057
937	  location:
938	    section: sections/analysis
939	    paragraph: 0
940	    sentence: 0
941	  text: RSSM reward gap 2.78-3.11x range across two independent analyses
942	  type: quantitative
943	  evidence:
944	  - exp_id: exp_rssm_fidelity_analysis
945	    metric: 008d_trained_dtEmb.reward_gap
946	    value: 2.78
947	    role: primary_evidence
948	  - exp_id: exp_063_rssm_fidelity
949	    metric: collapsed_reward_gap
950	    value: 3.11
951	    role: corroboration
952	  decisions: []
953	  deprecated: false
954	- id: C058
955	  location:
956	    section: sections/analysis
957	    paragraph: 0
958	    sentence: 0
959	  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on
960	    Cheetah'
961	  type: quantitative
962	  evidence:
963	  - exp_id: exp_026_obs_sgs_cheetah
964	    metric: nve_amplification
965	    value: 21.9-30.2
966	    role: primary_evidence
967	  decisions: []
968	  deprecated: false
969	- id: C059
970	  location:
971	    section: sections/analysis
972	    paragraph: 0
973	    sentence: 0
974	  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%
975	    baseline'
976	  type: quantitative
977	  evidence:
978	  - exp_id: exp_030c_tcn_cheetah
979	    metric: nve_suppressed
980	    value: 0.3
981	    role: primary_evidence
982	  - exp_id: exp_030c_tcn_cheetah
983	    metric: eval_pct_baseline
984	    value: 15
985	    role: primary_evidence
986	  decisions: []
987	  deprecated: false
988	- id: C060
989	  location:
990	    section: sections/appendix
991	    paragraph: 0
992	    sentence: 0
993	  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70
994	    to -0.86 at 75K'
995	  type: quantitative
996	  evidence:
997	  - exp_id: exp_065_dt_emb_cosine
998	    metric: trained_cos_25k_range
999	    value: -0.87 to -0.94
1000	    role: primary_evidence
1001	  - exp_id: exp_065_dt_emb_cosine
1002	    metric: trained_cos_75k_range
1003	    value: -0.70 to -0.86
1004	    role: primary_evidence
1005	  decisions: []
1006	  deprecated: false
1007	- id: C061
1008	  location:
1009	    section: sections/appendix
1010	    paragraph: 0
1011	    sentence: 0
1012	  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'
1013	  type: quantitative
1014	  evidence:
1015	  - exp_id: exp_065_dt_emb_cosine
1016	    metric: frozen_cos_constant
1017	    value: -0.15 to +0.07
1018	    role: control
1019	  decisions: []
1020	  deprecated: false
1021	- id: C062
1022	  location:
1023	    section: sections/introduction
1024	    paragraph: 0
1025	    sentence: 0
1026	  text: RSSM reward prediction gap 2.78-3.11x in introduction
1027	  type: quantitative
1028	  evidence:
1029	  - exp_id: exp_rssm_fidelity_analysis
1030	    metric: 008d_trained_dtEmb.reward_gap
1031	    value: 2.78
1032	    role: primary_evidence
1033	  - exp_id: exp_063_rssm_fidelity
1034	    metric: collapsed_reward_gap
1035	    value: 3.11
1036	    role: corroboration
1037	  decisions: []
1038	  deprecated: false
1039	- id: C063
1040	  location:
1041	    section: sections/results
1042	    paragraph: 0
1043	    sentence: 0
1044	  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained
1045	    conditioning
1046	  type: quantitative
1047	  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation
1048	  decisions: []
1049	  deprecated: false
1050	- id: C064
1051	  location:
1052	    section: sections/results
1053	    paragraph: 0
1054	    sentence: 0
1055	  text: Observation reconstruction gap improves with temporal conditioning (1.33x
1056	    vs baseline 1.46x)
1057	  type: quantitative
1058	  evidence: exp_063 obs_mse data
1059	  decisions: []
1060	  deprecated: false
1061	- id: C065
1062	  location:
1063	    section: sections/results
1064	    paragraph: 0
1065	    sentence: 0
1066	  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control
1067	    median 1.05x (52.5% overestimated)
1068	  type: quantitative
1069	  evidence: exp_064 value_distribution results_summary
1070	  decisions: []
1071	  deprecated: false
1072	- id: C066
1073	  location:
1074	    section: sections/analysis
1075	    paragraph: 0
1076	    sentence: 0
1077	  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific
1078	    pathology
1079	  type: quantitative
1080	  evidence: exp_063 rssm_fidelity_analysis
1081	  decisions: []
1082	  deprecated: false
1083	- id: C067
1084	  location:
1085	    section: sections/results
1086	    paragraph: 0
1087	    sentence: 0
1088	  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at
1089	    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)
1090	  type: quantitative
1091	  evidence: exp_066 timeseries analysis, 12 dense checkpoints
1092	  decisions: []
1093	  deprecated: false
1094	- id: C068
1095	  location:
1096	    section: sections/results
1097	    paragraph: 0
1098	    sentence: 0
1099	  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential
1100	    improvement
1101	  type: quantitative
1102	  evidence: exp_066 timeseries analysis
1103	  decisions: []
1104	  deprecated: false
1105	- id: C069
1106	  location:
1107	    section: sections/analysis
1108	    paragraph: 0
1109	    sentence: 0
1110	  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)
1111	    → entropy destabilization (~35K later), n=1'
1112	  type: quantitative
1113	  evidence: exp_066 timeseries + actor entropy analysis
1114	  decisions: []
1115	  deprecated: false
1116	- id: C070
1117	  location:
1118	    section: sections/appendix
1119	    paragraph: 0
1120	    sentence: 0
1121	  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;
1122	    VE ratio near zero until 40K spike (1.59x)'
1123	  type: quantitative
1124	  evidence: exp_066 12-checkpoint timeseries analysis
1125	  decisions: []
1126	  deprecated: false
1127	- id: C071
1128	  location:
1129	    section: sections/appendix
1130	    paragraph: 0
1131	    sentence: 0
1132	  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from
1133	    selective improvement not worsening
1134	  type: quantitative
1135	  evidence: exp_066 timeseries MAE data
1136	  decisions: []
1137	  deprecated: false
1138	tables:
1139	- id: T001
1140	  location:
1141	    section: methodology
1142	    table_number: 1
1143	  caption: Factorial design — 9 configurations
1144	  cells:
1145	  - row: 0
1146	    col: 0
1147	    value: '001'
1148	    source:
1149	      exp_id: exp_001_baseline
1150	      metric: exp_id
1151	  - row: 1
1152	    col: 0
1153	    value: '006'
1154	    source:
1155	      exp_id: exp_006_fixed_dt2
1156	      metric: exp_id
1157	  - row: 2
1158	    col: 0
1159	    value: '007'
1160	    source:
1161	      exp_id: exp_007_fixed_dt4
1162	      metric: exp_id
1163	  - row: 3
1164	    col: 0
1165	    value: '005'
1166	    source:
1167	      exp_id: exp_005_event_gated_v4
1168	      metric: exp_id
1169	  - row: 4
1170	    col: 0
1171	    value: 008d
1172	    source:
1173	      exp_id: exp_008d_subsample_on_h8
1174	      metric: exp_id
1175	  - row: 5
1176	    col: 0
1177	    value: 008f
1178	    source:
1179	      exp_id: exp_008f_no_dt_embed_subsample_on_h8
1180	      metric: exp_id
1181	  - row: 6
1182	    col: 0
1183	    value: 008a
1184	    source:
1185	      exp_id: exp_008a_no_subsample_dt2
1186	      metric: exp_id
1187	  - row: 7
1188	    col: 0
1189	    value: 008c
1190	    source:
1191	      exp_id: exp_008c_no_subsample_dt2_h8
1192	      metric: exp_id
1193	  - row: 8
1194	    col: 0
1195	    value: 008e_v3
1196	    source:
1197	      exp_id: exp_008e_v3_subsample_on_dt1_h15
1198	      metric: exp_id
1199	  deprecated: false
1200	- id: T002
1201	  location:
1202	    section: results
1203	    table_number: 1
1204	  caption: All configurations and outcomes
1205	  cells:
1206	  - row: 0
1207	    col: 5
1208	    value: 915.7
1209	    source:
1210	      exp_id: exp_001_baseline
1211	      metric: eval_return_105K
1212	  - row: 1
1213	    col: 5
1214	    value: 132.9
1215	    source:
1216	      exp_id: exp_006_fixed_dt2
1217	      metric: eval_return_65K
1218	  - row: 1
1219	    col: 6
1220	    value: 4.83
1221	    source:
1222	      exp_id: exp_006_fixed_dt2
1223	      metric: peak_nve
1224	  - row: 2
1225	    col: 5
1226	    value: 152.5
1227	    source:
1228	      exp_id: exp_007_fixed_dt4
1229	      metric: eval_return_55K
1230	  - row: 3
1231	    col: 5
1232	    value: 98.8
1233	    source:
1234	      exp_id: exp_005_event_gated_v4
1235	      metric: eval_return_145K
1236	  - row: 4
1237	    col: 5
1238	    value: 82.8
1239	    source:
1240	      exp_id: exp_008d_subsample_on_h8
1241	      metric: eval_return_55K
1242	  - row: 4
1243	    col: 6
1244	    value: 4.12
1245	    source:
1246	      exp_id: exp_008d_subsample_on_h8
1247	      metric: peak_nve
1248	  - row: 5
1249	    col: 5
1250	    value: 267.9
1251	    source:
1252	      exp_id: exp_009b_008d_walker_s2
1253	      metric: final_eval_return
1254	  - row: 5
1255	    col: 6
1256	    value: 1.62
1257	    source:
1258	      exp_id: exp_009b_008d_walker_s2
1259	      metric: peak_nve
1260	  - row: 6
1261	    col: 5
1262	    value: 131.1
1263	    source:
1264	      exp_id: exp_009e_008d_walker_s1
1265	      metric: final_eval_return
1266	  - row: 6
1267	    col: 6
1268	    value: 4.12
1269	    source:
1270	      exp_id: exp_009e_008d_walker_s1
1271	      metric: peak_nve
1272	  - row: 7
1273	    col: 5
1274	    value: 503.0
1275	    source:
1276	      exp_id: exp_008f_no_dt_embed_subsample_on_h8
1277	      metric: eval_return_105K
1278	  - row: 8
1279	    col: 5
1280	    value: 148.3
1281	    source:
1282	      exp_id: exp_009c_008f_walker_s2
1283	      metric: final_eval_return
1284	  - row: 9
1285	    col: 5
1286	    value: 777.7
1287	    source:
1288	      exp_id: exp_008a_no_subsample_dt2
1289	      metric: eval_return_105K
1290	  - row: 10
1291	    col: 5
1292	    value: 240.9
1293	    source:
1294	      exp_id: exp_008c_no_subsample_dt2_h8
1295	      metric: eval_return_65K
1296	  - row: 11
1297	    col: 5
1298	    value: 869.9
1299	    source:
1300	      exp_id: exp_008e_v3_walker_s1
1301	      metric: final_eval_return
1302	  - row: 12
1303	    col: 5
1304	    value: 137.0
1305	    source:
1306	      exp_id: exp_008e_v3_walker_s2
1307	      metric: final_eval_return
1308	  - row: 12
1309	    col: 6
1310	    value: 3.78
1311	    source:
1312	      exp_id: exp_008e_v3_walker_s2
1313	      metric: final_nve
1314	  - row: 13
1315	    col: 5
1316	    value: 836.5
1317	    source:
1318	      exp_id: exp_009a_baseline_walker_s2
1319	      metric: final_eval_return
1320	  deprecated: false
1321	- id: T003
1322	  location:
1323	    section: results
1324	    table_number: 2
1325	  caption: RSSM fidelity at dt=1 vs dt=2
1326	  cells:
1327	  - row: 0
1328	    col: 0
1329	    value: 13.49
1330	    source:
1331	      exp_id: exp_rssm_fidelity_analysis
1332	      metric: baseline.dt1_obs_mse
1333	  - row: 0
1334	    col: 1
1335	    value: 27.5
1336	    source:
1337	      exp_id: exp_rssm_fidelity_analysis
1338	      metric: baseline.dt2_obs_mse
1339	  - row: 0
1340	    col: 2
1341	    value: 2.04
1342	    source:
1343	      exp_id: exp_rssm_fidelity_analysis
1344	      metric: baseline.obs_gap
1345	  - row: 0
1346	    col: 3
1347	    value: 0.0102
1348	    source:
1349	      exp_id: exp_rssm_fidelity_analysis
1350	      metric: baseline.dt1_reward_mae
1351	  - row: 0
1352	    col: 4
1353	    value: 0.0159
1354	    source:
1355	      exp_id: exp_rssm_fidelity_analysis
1356	      metric: baseline.dt2_reward_mae
1357	  - row: 0
1358	    col: 5
1359	    value: 1.56
1360	    source:
1361	      exp_id: exp_rssm_fidelity_analysis
1362	      metric: baseline.reward_gap
1363	  - row: 1
1364	    col: 0
1365	    value: 41.31
1366	    source:
1367	      exp_id: exp_rssm_fidelity_analysis
1368	      metric: 008d_trained_dtEmb.dt1_obs_mse
1369	  - row: 1
1370	    col: 1
1371	    value: 53.67
1372	    source:
1373	      exp_id: exp_rssm_fidelity_analysis
1374	      metric: 008d_trained_dtEmb.dt2_obs_mse
1375	  - row: 1
1376	    col: 2
1377	    value: 1.3
1378	    source:
1379	      exp_id: exp_rssm_fidelity_analysis
1380	      metric: 008d_trained_dtEmb.obs_gap
1381	  - row: 1
1382	    col: 3
1383	    value: 0.0568
1384	    source:
1385	      exp_id: exp_rssm_fidelity_analysis
1386	      metric: 008d_trained_dtEmb.dt1_reward_mae
1387	  - row: 1
1388	    col: 4
1389	    value: 0.1579
1390	    source:
1391	      exp_id: exp_rssm_fidelity_analysis
1392	      metric: 008d_trained_dtEmb.dt2_reward_mae
1393	  - row: 1
1394	    col: 5
1395	    value: 2.78
1396	    source:
1397	      exp_id: exp_rssm_fidelity_analysis
1398	      metric: 008d_trained_dtEmb.reward_gap
1399	  - row: 2
1400	    col: 0
1401	    value: 8.01
1402	    source:
1403	      exp_id: exp_rssm_fidelity_analysis
1404	      metric: 008f_no_dtEmb.dt1_obs_mse
1405	  - row: 2
1406	    col: 1
1407	    value: 22.04
1408	    source:
1409	      exp_id: exp_rssm_fidelity_analysis
1410	      metric: 008f_no_dtEmb.dt2_obs_mse
1411	  - row: 2
1412	    col: 2
1413	    value: 2.75
1414	    source:
1415	      exp_id: exp_rssm_fidelity_analysis
1416	      metric: 008f_no_dtEmb.obs_gap
1417	  - row: 2
1418	    col: 3
1419	    value: 0.7469
1420	    source:
1421	      exp_id: exp_rssm_fidelity_analysis
1422	      metric: 008f_no_dtEmb.dt1_reward_mae
1423	  - row: 2
1424	    col: 4
1425	    value: 0.7526
1426	    source:
1427	      exp_id: exp_rssm_fidelity_analysis
1428	      metric: 008f_no_dtEmb.dt2_reward_mae
1429	  - row: 2
1430	    col: 5
1431	    value: 1.01
1432	    source:
1433	      exp_id: exp_rssm_fidelity_analysis
1434	      metric: 008f_no_dtEmb.reward_gap
1435	  deprecated: false
1436	- id: T004
1437	  location:
1438	    section: results
1439	    table_number: 3
1440	  caption: Post-CIVO outcomes for 008d configuration
1441	  cells:
1442	  - row: 0
1443	    col: 0
1444	    value: 4.12
1445	    source:
1446	      exp_id: exp_008d_subsample_on_h8
1447	      metric: peak_nve
1448	  - row: 0
1449	    col: 1
1450	    value: 4.12
1451	    source:
1452	      exp_id: exp_008d_subsample_on_h8
1453	      metric: peak_nve
1454	  - row: 0
1455	    col: 2
1456	    value: 82.8
1457	    source:
1458	      exp_id: exp_008d_subsample_on_h8
1459	      metric: eval_return_55K
1460	  - row: 1
1461	    col: 0
1462	    value: 1.62
1463	    source:
1464	      exp_id: exp_009b_008d_walker_s2
1465	      metric: peak_nve
1466	  - row: 1
1467	    col: 1
1468	    value: 0.38
1469	    source:
1470	      exp_id: exp_009b_008d_walker_s2
1471	      metric: final_nve
1472	  - row: 1
1473	    col: 2
1474	    value: 267.9
1475	    source:
1476	      exp_id: exp_009b_008d_walker_s2
1477	      metric: final_eval_return
1478	  - row: 2
1479	    col: 0
1480	    value: 4.12
1481	    source:
1482	      exp_id: exp_009e_008d_walker_s1
1483	      metric: peak_nve
1484	  - row: 2
1485	    col: 1
1486	    value: 1.57
1487	    source:
1488	      exp_id: exp_009e_008d_walker_s1
1489	      metric: final_nve
1490	  - row: 2
1491	    col: 2
1492	    value: 131.1
1493	    source:
1494	      exp_id: exp_009e_008d_walker_s1
1495	      metric: final_eval_return
1496	  deprecated: false
1497	figures:
1498	- id: F001
1499	  location:
1500	    section: results
1501	    figure_number: 1
1502	  caption: Learning curves for all configurations
1503	  type: result
1504	  source:
1505	    experiments:
1506	    - exp_id: exp_001_baseline
1507	    - exp_id: exp_006_fixed_dt2
1508	    - exp_id: exp_007_fixed_dt4
1509	    - exp_id: exp_005_event_gated_v4
1510	    - exp_id: exp_008d_subsample_on_h8
1511	    - exp_id: exp_008f_no_dt_embed_subsample_on_h8
1512	    - exp_id: exp_008a_no_subsample_dt2
1513	    - exp_id: exp_008e_v3_walker_s1
1514	  output_path: figures/paper/fig1_learning_curves.pdf
1515	  deprecated: false
1516	- id: F002
1517	  location:
1518	    section: results
1519	    figure_number: 2
1520	  caption: Normalized value-to-eval ratio trajectories
1521	  type: result
1522	  source:
1523	    experiments:
1524	    - exp_id: exp_008d_subsample_on_h8
1525	    - exp_id: exp_008f_no_dt_embed_subsample_on_h8
1526	    - exp_id: exp_008a_no_subsample_dt2
1527	    - exp_id: exp_008e_v3_walker_s1
1528	    - exp_id: exp_009b_008d_walker_s2
1529	  output_path: figures/paper/fig2_nve_trajectory.pdf
1530	  deprecated: false
1531	- id: F003
1532	  location:
1533	    section: results
1534	    figure_number: 3
1535	  caption: Factorial experiment summary grid
1536	  type: result
1537	  source:
1538	    experiments:
1539	    - exp_id: exp_008d_subsample_on_h8
1540	    - exp_id: exp_008f_no_dt_embed_subsample_on_h8
1541	    - exp_id: exp_008a_no_subsample_dt2
1542	    - exp_id: exp_008c_no_subsample_dt2_h8
1543	  output_path: figures/paper/fig3_factorial_grid.pdf
1544	  deprecated: false
1545	- id: F004
1546	  location:
1547	    section: results
1548	    figure_number: 4
1549	  caption: Peak evaluation return as function of imagination dt
1550	  type: result
1551	  source:
1552	    experiments:
1553	    - exp_id: exp_001_baseline
1554	    - exp_id: exp_006_fixed_dt2
1555	    - exp_id: exp_007_fixed_dt4
1556	  output_path: figures/paper/fig5_dt_amplification.pdf
1557	  deprecated: false
1558	- id: F005
1559	  location:
1560	    section: results
1561	    figure_number: 5
1562	  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'
1563	  type: result
1564	  source:
1565	    experiments:
1566	    - exp_id: exp_008d_subsample_on_h8
1567	    - exp_id: exp_008e_v3_walker_s2
1568	    - exp_id: exp_009a_baseline_walker_s2
1569	  output_path: figures/paper/fig6_multiple_pathways.pdf
1570	  deprecated: false
1571	- id: F006
1572	  location:
1573	    section: sections/appendix
1574	    figure_number: 0
1575	  caption: ''
1576	  type: other
1577	  source: {}
1578	  output_path: ''
1579	  deprecated: false
1580	_completeness:
1581	  coverage: 73/77
1582	  claims: 71
1583	  tables: 4
1584	  figures: 6
1585	  tier_counts:
1586	    tier1: 0
1587	    tier2: 73
1588	    tier3: 4
1589	    tierX: 0
1590	  last_checked: '2026-05-25T03:36:26.590002+00:00'
1591	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "bb772324-b131-4251-a591-6bfbb4c6bb38",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
      "content": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 7/8 classification (n=8)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_006_fixed_dt2\n    metric: model_loss_at_55k\n    value: 4.853\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 7/8 accuracy (AUROC=0.933)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 7/8 CIVO classification (n=8, 87.5%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_at_1.5x\n    value: 0.88\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
      "numLines": 1591,
      "startLine": 1,
      "totalLines": 1591
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
Now I have the full file. Let me make all the edits. I need to update:

1. **C004** (line 70): `7/8 classification (n=8)` → `53/56 classification (n=56)`
2. **C011** (line 199): `7/8 accuracy (AUROC=0.933)` → `53/56 accuracy (AUROC=0.990)`
3. **C018** (line 315): `AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]` → `AUROC=0.990, 53/56 accuracy (n=56)`


4. **C042** (line 720): `7/8 CIVO classification (n=8, 87.5%)` → `53/56 CIVO classification (n=56, 94.6%)`
5. **C044** (line 753): `Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold` → `Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold`
6. **C045** (line 763): Updating the NVE diagnostic extended validation sample size and metrics from n=32 with AUROC=0.961 and F1=0.880 to n=56 with AUROC=0.990 and F1=0.941
7-13. **C047-C053** (lines 784-880): Need to update text and evidence values across these sections, including converting metric names from `auroc_n32` to `auroc_n56` format

Now I'll apply these changes in batch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "5d6f73dd-9d12-4acb-8467-2b5cfec7ec7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GnxiEH81vcswFezu26bow",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18789,
      "cache_read_input_tokens": 39652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18789
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

Now applying all updates. Starting with C004, C011, C018, C042 (old n=8 entries), then C044-C045, then C047-C053.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "695937dd-41d6-443a-adbe-6e14899df057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GnxiEH81vcswFezu26bow",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18789,
      "cache_read_input_tokens": 39652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18789
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

<details open><summary>🔧 Tool call — Edit · `toolu_012EZz133L26t11XCE7Niqe9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: 7/8 classification (n=8)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_006_fixed_dt2\n    metric: model_loss_at_55k\n    value: 4.853\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053",
  "new_string": "  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "ee9a8a16-16e6-49fe-876b-82ca749e9373",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GnxiEH81vcswFezu26bow",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18789,
      "cache_read_input_tokens": 39652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18789
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

_source line 17 · 2026-05-25T14:11:58.312Z_

<details><summary>↩ Tool result · `toolu_012EZz133L26t11XCE7Niqe9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "1ebfc342-fcea-40c4-8544-3d968b4dae30",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: 7/8 classification (n=8)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_006_fixed_dt2\n    metric: model_loss_at_55k\n    value: 4.853\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053",
    "newString": "  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 7/8 classification (n=8)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_006_fixed_dt2\n    metric: model_loss_at_55k\n    value: 4.853\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 7/8 accuracy (AUROC=0.933)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 7/8 CIVO classification (n=8, 87.5%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_at_1.5x\n    value: 0.88\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 67,
        "oldLines": 25,
        "newStart": 67,
        "newLines": 17,
        "lines": [
          "     section: abstract",
          "     paragraph: 0",
          "     sentence: 4",
          "-  text: 7/8 classification (n=8)",
          "+  text: 53/56 classification (n=56, AUROC=0.990)",
          "   type: quantitative",
          "   evidence:",
          "-  - exp_id: exp_008d_subsample_on_h8",
          "-    metric: peak_nve",
          "-    value: 4.12",
          "-    role: true_positive",
          "-  - exp_id: exp_006_fixed_dt2",
          "-    metric: model_loss_at_55k",
          "-    value: 4.853",
          "-    role: true_positive",
          "-  - exp_id: exp_009b_008d_walker_s2",
          "-    metric: peak_nve",
          "-    value: 1.62",
          "-    role: true_positive",
          "-  - exp_id: exp_008e_v3_walker_s2",
          "-    metric: final_nve",
          "-    value: 3.78",
          "-    role: false_positive",
          "+  - exp_id: plan_034_nve_threshold",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "+    role: primary_evidence",
          "+  - exp_id: plan_034_nve_threshold",
          "+    metric: accuracy_n56",
          "+    value: 0.946",
          "+    role: primary_evidence",
          "   decisions:",
          "   - D053",
          "   deprecated: false"
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


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_013erz6iyLzQkZ7u4UkQiWDC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: 7/8 accuracy (AUROC=0.933)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053\n  - D054",
  "new_string": "  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "54a93715-9b56-4052-8d84-eca9a33c6be2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CBcH7vr5rBgeF2USVYFo7J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 58441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1126
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

_source line 19 · 2026-05-25T14:12:02.537Z_

<details><summary>↩ Tool result · `toolu_013erz6iyLzQkZ7u4UkQiWDC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "8cfcc824-cbe7-4950-909c-5c1b30bf07f4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: 7/8 accuracy (AUROC=0.933)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053\n  - D054",
    "newString": "  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 7/8 accuracy (AUROC=0.933)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 7/8 CIVO classification (n=8, 87.5%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_at_1.5x\n    value: 0.88\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 188,
        "oldLines": 17,
        "newStart": 188,
        "newLines": 17,
        "lines": [
          "     section: methodology",
          "     paragraph: 6",
          "     sentence: 3",
          "-  text: 7/8 accuracy (AUROC=0.933)",
          "+  text: 53/56 accuracy (AUROC=0.990, n=56)",
          "   type: quantitative",
          "   evidence:",
          "-  - exp_id: exp_008d_subsample_on_h8",
          "-    metric: peak_nve",
          "-    value: 4.12",
          "-    role: true_positive",
          "-  - exp_id: exp_009b_008d_walker_s2",
          "-    metric: peak_nve",
          "-    value: 1.62",
          "-    role: true_positive",
          "+  - exp_id: plan_034_nve_threshold",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "+    role: primary_evidence",
          "+  - exp_id: plan_034_nve_threshold",
          "+    metric: accuracy_n56",
          "+    value: 0.946",
          "+    role: primary_evidence",
          "   decisions:",
          "   - D053",
          "   - D054"
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


### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01AJoXrudiKjosFSmJPUTqEL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D054",
  "new_string": "  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "4ae29650-ad6b-4eeb-ba3e-80b80452fee5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxranFFCASmgVixuEpckrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 448,
      "cache_read_input_tokens": 59567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 448
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

_source line 21 · 2026-05-25T14:12:08.338Z_

<details><summary>↩ Tool result · `toolu_01AJoXrudiKjosFSmJPUTqEL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "476b951d-1f46-4141-b035-3989fe0f7d7c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D054",
    "newString": "  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 7/8 CIVO classification (n=8, 87.5%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_at_1.5x\n    value: 0.88\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 304,
        "oldLines": 21,
        "newStart": 304,
        "newLines": 17,
        "lines": [
          "     section: results",
          "     paragraph: 4",
          "     sentence: 0",
          "-  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]",
          "+  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)",
          "   type: quantitative",
          "   evidence:",
          "-  - exp_id: exp_008d_subsample_on_h8",
          "-    metric: peak_nve",
          "-    value: 4.12",
          "-    role: true_positive",
          "-  - exp_id: exp_009b_008d_walker_s2",
          "-    metric: peak_nve",
          "-    value: 1.62",
          "-    role: true_positive",
          "-  - exp_id: exp_008e_v3_walker_s2",
          "-    metric: final_nve",
          "-    value: 3.78",
          "-    role: false_positive",
          "+  - exp_id: plan_034_nve_threshold",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "+    role: primary_evidence",
          "+  - exp_id: plan_034_nve_threshold",
          "+    metric: f1_n56",
          "+    value: 0.941",
          "+    role: primary_evidence",
          "   decisions:",
          "   - D054",
          "   deprecated: false"
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


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_014ifeH263eKdd3bLFcJNCso`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: 7/8 CIVO classification (n=8, 87.5%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053",
  "new_string": "  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "eff49043-2c26-4a38-8a22-55157a3b20a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DeNMVQZ8KZGLbA6HuhFQjv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 60015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 513
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

_source line 23 · 2026-05-25T14:12:13.183Z_

<details><summary>↩ Tool result · `toolu_014ifeH263eKdd3bLFcJNCso`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "eeead57a-7118-4150-b02f-15ad07518d71",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: 7/8 CIVO classification (n=8, 87.5%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053",
    "newString": "  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 7/8 CIVO classification (n=8, 87.5%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: true_positive\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_at_1.5x\n    value: 0.88\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 705,
        "oldLines": 17,
        "newStart": 705,
        "newLines": 17,
        "lines": [
          "     section: conclusion",
          "     paragraph: 0",
          "     sentence: 2",
          "-  text: 7/8 CIVO classification (n=8, 87.5%)",
          "+  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)",
          "   type: quantitative",
          "   evidence:",
          "-  - exp_id: exp_008d_subsample_on_h8",
          "-    metric: peak_nve",
          "-    value: 4.12",
          "-    role: true_positive",
          "-  - exp_id: exp_009b_008d_walker_s2",
          "-    metric: peak_nve",
          "-    value: 1.62",
          "-    role: true_positive",
          "+  - exp_id: plan_034_nve_threshold",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "+    role: primary_evidence",
          "+  - exp_id: plan_034_nve_threshold",
          "+    metric: accuracy_n56",
          "+    value: 0.946",
          "+    role: primary_evidence",
          "   decisions:",
          "   - D053",
          "   deprecated: false"
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

_source line 24_

Now updating C044 and C045.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "1b8fffa3-9456-48f4-8e2e-a9dd59996920",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7W5MC1QRRtznpCknkEWLt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 554,
      "cache_read_input_tokens": 60528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 554
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01MzkGeiStG645HcuyawqGKL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\n  type: quantitative\n  evidence: []",
  "new_string": "  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "a4763783-8d3f-4f61-8f08-d3511fbb0c14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7W5MC1QRRtznpCknkEWLt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 554,
      "cache_read_input_tokens": 60528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 554
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

_source line 26 · 2026-05-25T14:12:17.500Z_

<details><summary>↩ Tool result · `toolu_01MzkGeiStG645HcuyawqGKL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "408f5e59-eefb-4e3f-98d7-5c6984352a68",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\n  type: quantitative\n  evidence: []",
    "newString": "  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_at_1.5x\n    value: 0.88\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 738,
        "oldLines": 9,
        "newStart": 738,
        "newLines": 13,
        "lines": [
          "     section: sections/appendix",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold",
          "+  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold",
          "   type: quantitative",
          "-  evidence: []",
          "+  evidence:",
          "+  - exp_id: plan_034_nve_threshold",
          "+    metric: f1_n56",
          "+    value: 0.941",
          "+    role: primary_evidence",
          "   decisions: []",
          "   deprecated: false",
          " - id: C045"
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


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01Gf6M2QjWe6zKhggBU2M4gf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence: []",
  "new_string": "  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "3d9a763d-ea34-4414-b7bd-641f1d421cb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JtVYdFM5DqzBm3yobHhTG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 61082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 331
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

_source line 28 · 2026-05-25T14:12:20.941Z_

<details><summary>↩ Tool result · `toolu_01Gf6M2QjWe6zKhggBU2M4gf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "81fbb633-c218-447a-99c7-78e5aba1c1ef",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence: []",
    "newString": "  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_at_1.5x\n    value: 0.88\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 752,
        "oldLines": 9,
        "newStart": 752,
        "newLines": 13,
        "lines": [
          "     section: sections/analysis",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880",
          "+  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941",
          "   type: quantitative",
          "-  evidence: []",
          "+  evidence:",
          "+  - exp_id: plan_034_nve_threshold",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "+    role: primary_evidence",
          "   decisions: []",
          "   deprecated: false",
          " - id: C046"
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

_source line 29_

Now updating C047-C053.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "19c95679-e0bc-4ea3-94a0-a9bd73c326d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FUwuy8EoikieY8dJHzf9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 61413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01MPyB1En2sWFn6aH9kDHmKp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_at_1.5x\n    value: 0.88\n    role: primary_evidence",
  "new_string": "  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "efbc63a6-702d-4c9a-9d95-443463ec04b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FUwuy8EoikieY8dJHzf9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 61413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 31 · 2026-05-25T14:12:27.790Z_

<details><summary>↩ Tool result · `toolu_01MPyB1En2sWFn6aH9kDHmKp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "b6287b5d-e3ae-4d0d-9994-97ad7db7262a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_at_1.5x\n    value: 0.88\n    role: primary_evidence",
    "newString": "  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_at_1.5x\n    value: 0.88\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 777,
        "oldLines": 16,
        "newStart": 777,
        "newLines": 16,
        "lines": [
          "     section: sections/methodology",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32",
          "+  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56",
          "   type: quantitative",
          "   evidence:",
          "   - exp_id: plan_034_nve_threshold",
          "-    metric: auroc_n32",
          "-    value: 0.961",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "     role: primary_evidence",
          "   - exp_id: plan_034_nve_threshold",
          "-    metric: f1_at_1.5x",
          "-    value: 0.88",
          "+    metric: f1_n56",
          "+    value: 0.941",
          "     role: primary_evidence",
          "   decisions: []",
          "   deprecated: false"
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


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01RuFZ2k7bngjhtjEbTHr7Sc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
  "new_string": "  text: NVE threshold 53/56 classification (n=56, AUROC=0.990, F1=0.941)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "6d8c6f5b-4860-4b99-aa75-ff24da4ff67e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRguveRfLcuGZik1LUxGo2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 61726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 33 · 2026-05-25T14:12:32.322Z_

<details><summary>↩ Tool result · `toolu_01RuFZ2k7bngjhtjEbTHr7Sc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "a7bf4ea1-8f9b-4307-8ff9-f19847210da8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
    "newString": "  text: NVE threshold 53/56 classification (n=56, AUROC=0.990, F1=0.941)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 795,
        "oldLines": 12,
        "newStart": 795,
        "newLines": 12,
        "lines": [
          "     section: sections/results",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)",
          "+  text: NVE threshold 53/56 classification (n=56, AUROC=0.990, F1=0.941)",
          "   type: quantitative",
          "   evidence:",
          "   - exp_id: plan_034_nve_threshold",
          "-    metric: auroc_n32",
          "-    value: 0.961",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "     role: primary_evidence",
          "   decisions: []",
          "   deprecated: false"
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


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01HggTTHBeaKXgAiDXMUhQDd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
  "new_string": "  text: CIVO classification 53/56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "fd4f3aa1-622c-4cc6-80d0-917e343daece",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NL1psQHFXsKtfkokEMTrC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 62180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
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

_source line 35 · 2026-05-25T14:12:36.211Z_

<details><summary>↩ Tool result · `toolu_01HggTTHBeaKXgAiDXMUhQDd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "f74295d2-96af-491e-9475-d2c0b7dd8d9e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
    "newString": "  text: CIVO classification 53/56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 classification (n=56, AUROC=0.990, F1=0.941)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 809,
        "oldLines": 12,
        "newStart": 809,
        "newLines": 12,
        "lines": [
          "     section: sections/abstract_body",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: CIVO classification 29/32 AUROC=0.961 F1=0.880",
          "+  text: CIVO classification 53/56 AUROC=0.990 F1=0.941",
          "   type: quantitative",
          "   evidence:",
          "   - exp_id: plan_034_nve_threshold",
          "-    metric: auroc_n32",
          "-    value: 0.961",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "     role: primary_evidence",
          "   decisions: []",
          "   deprecated: false"
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


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01FV5fvKXVwwYeM2yCZWo4Zj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
  "new_string": "  text: NVE threshold 53/56 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "c296fbf0-573d-442a-b710-68c062cf53bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPDBtyqiG9j7tcntfKVS39",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 349,
      "cache_read_input_tokens": 62543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 349
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

_source line 37 · 2026-05-25T14:12:40.311Z_

<details><summary>↩ Tool result · `toolu_01FV5fvKXVwwYeM2yCZWo4Zj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "880218fa-2c9d-4d7c-80c3-9be653169613",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
    "newString": "  text: NVE threshold 53/56 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 classification (n=56, AUROC=0.990, F1=0.941)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 53/56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 29/32 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 823,
        "oldLines": 12,
        "newStart": 823,
        "newLines": 12,
        "lines": [
          "     section: sections/introduction",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: NVE threshold 29/32 classification in introduction",
          "+  text: NVE threshold 53/56 classification in introduction",
          "   type: quantitative",
          "   evidence:",
          "   - exp_id: plan_034_nve_threshold",
          "-    metric: auroc_n32",
          "-    value: 0.961",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "     role: primary_evidence",
          "   decisions: []",
          "   deprecated: false"
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


### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01VX35aQSVybor6EeYzw5FxW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
  "new_string": "  text: Contribution 1 AUROC updated to 0.990\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "c89dcfcd-c62b-4aa0-ac69-919ca24c899c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcKebGMscNxeSyg2iyt6Z8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 327,
      "cache_read_input_tokens": 62892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 327
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

_source line 39 · 2026-05-25T14:12:44.153Z_

<details><summary>↩ Tool result · `toolu_01VX35aQSVybor6EeYzw5FxW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "c4faa886-96a2-41f5-bc23-2596e48029e8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
    "newString": "  text: Contribution 1 AUROC updated to 0.990\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 classification (n=56, AUROC=0.990, F1=0.941)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 53/56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 837,
        "oldLines": 12,
        "newStart": 837,
        "newLines": 12,
        "lines": [
          "     section: sections/introduction",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: Contribution 1 AUROC updated to 0.961",
          "+  text: Contribution 1 AUROC updated to 0.990",
          "   type: quantitative",
          "   evidence:",
          "   - exp_id: plan_034_nve_threshold",
          "-    metric: auroc_n32",
          "-    value: 0.961",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "     role: primary_evidence",
          "   decisions: []",
          "   deprecated: false"
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


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_01SVQ8XqtWmEFKHH5kd7PQzZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
  "new_string": "  text: Conclusion NVE updated to 53/56 AUROC=0.990\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "886a5fe6-6364-4279-bba1-da6ec2bb94b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178GxSTarJQ61pZrSXmYwu1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 63219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 331
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

_source line 41 · 2026-05-25T14:12:54.273Z_

<details><summary>↩ Tool result · `toolu_01SVQ8XqtWmEFKHH5kd7PQzZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "abfb7f32-40a9-44d8-bfa4-b124a36d92bc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
    "newString": "  text: Conclusion NVE updated to 53/56 AUROC=0.990\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 classification (n=56, AUROC=0.990, F1=0.941)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 53/56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.990\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 851,
        "oldLines": 12,
        "newStart": 851,
        "newLines": 12,
        "lines": [
          "     section: sections/conclusion",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: Conclusion NVE updated to 29/32 AUROC=0.961",
          "+  text: Conclusion NVE updated to 53/56 AUROC=0.990",
          "   type: quantitative",
          "   evidence:",
          "   - exp_id: plan_034_nve_threshold",
          "-    metric: auroc_n32",
          "-    value: 0.961",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "     role: primary_evidence",
          "   decisions: []",
          "   deprecated: false"
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


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01B8eTZkhKBxi8o3c8HrrxAR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "old_string": "  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
  "new_string": "  text: Discussion NVE diagnostic consolidated to n=56 AUROC=0.990\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "0be5e45a-826c-4c99-b58c-b91a29db44db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgxCxurvyUDb6PM9QZy8ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 63550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 445
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

_source line 43 · 2026-05-25T14:12:58.571Z_

<details><summary>↩ Tool result · `toolu_01B8eTZkhKBxi8o3c8HrrxAR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "4e3c605d-7a83-4b8a-9b9c-eef932ed304f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
    "oldString": "  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence",
    "newString": "  text: Discussion NVE diagnostic consolidated to n=56 AUROC=0.990\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence",
    "originalFile": "paper:\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\n    of Variable-Rate DreamerV3'\n  version: 38\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\nclaims:\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: every variable-rate configuration of DreamerV3 degrades performance\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions:\n  - D009\n  - D015\n  deprecated: false\n- id: C002\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 2\n  text: trained temporal embedding as the causal factor\n  type: methodological\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: control\n  decisions:\n  - D021\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 3\n  text: 2.78x prediction gap between dt=1 and dt=2\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 4\n  text: 53/56 classification (n=56, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C005\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 5\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\n    degradation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: full_collapse\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: transient_civo\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: oscillatory\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 6\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\n    fails'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: healthy\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: collapsed\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C007\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=2 collapses to 14% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C008\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: fixed dt=4 never exceeds 19% of baseline\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C009\n  location:\n    section: introduction\n    paragraph: 1\n    sentence: 1\n  text: learned Gumbel-Softmax gate collapses to 11%\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: methodology\n    paragraph: 8\n    sentence: 0\n  text: baseline runs for 500K steps, peak return 970.4\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: methodology\n    paragraph: 6\n    sentence: 3\n  text: 53/56 accuracy (AUROC=0.990, n=56)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  - D054\n  deprecated: false\n- id: C012\n  location:\n    section: results\n    paragraph: 0\n    sentence: 1\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\n  type: quantitative\n  evidence:\n  - exp_id: exp_001_baseline\n    metric: eval_return_peak\n    value: 970.41\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C013\n  location:\n    section: results\n    paragraph: 0\n    sentence: 2\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_006_fixed_dt2\n    metric: eval_return_65K\n    value: 132.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C014\n  location:\n    section: results\n    paragraph: 0\n    sentence: 3\n  text: fixed dt=4 peaks at 176.9 at 25K\n  type: quantitative\n  evidence:\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C015\n  location:\n    section: results\n    paragraph: 0\n    sentence: 4\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\n  type: quantitative\n  evidence:\n  - exp_id: exp_005_event_gated_v4\n    metric: peak_return\n    value: 541.18\n    role: primary_evidence\n  - exp_id: exp_005_event_gated_v4\n    metric: eval_return_145K\n    value: 98.84\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: results\n    paragraph: 3\n    sentence: 0\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_25K\n    value: 167.22\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C017\n  location:\n    section: results\n    paragraph: 3\n    sentence: 1\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: results\n    paragraph: 4\n    sentence: 0\n  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions:\n  - D054\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 4\n    sentence: 1\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: true_positive\n  decisions: []\n  deprecated: false\n- id: C020\n  location:\n    section: results\n    paragraph: 6\n    sentence: 0\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 7\n    sentence: 0\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\n    267.9'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_eval_return\n    value: 267.93\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: final_nve\n    value: 0.38\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: results\n    paragraph: 8\n    sentence: 0\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\n    final 1.57x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_eval_return\n    value: 131.08\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: final_nve\n    value: 1.57\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008a reaches 777.7 (NVE=0.59x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008a_no_subsample_dt2\n    metric: eval_return_105K\n    value: 777.66\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 10\n    sentence: 0\n  text: 008c reaches 240.9 (NVE=0.58x)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008c_no_subsample_dt2_h8\n    metric: eval_return_65K\n    value: 240.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: results\n    paragraph: 12\n    sentence: 0\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\n  type: quantitative\n  evidence:\n  - exp_id: exp_006_fixed_dt2\n    metric: peak_return\n    value: 485.3\n    role: primary_evidence\n  - exp_id: exp_007_fixed_dt4\n    metric: peak_return\n    value: 176.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: results\n    paragraph: 14\n    sentence: 0\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: eval_return_55K\n    value: 82.75\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: results\n    paragraph: 14\n    sentence: 1\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: eval_return_105K\n    value: 503.0\n    role: primary_evidence\n  - exp_id: exp_009c_008f_walker_s2\n    metric: final_eval_return\n    value: 148.34\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 16\n    sentence: 0\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s1\n    metric: final_eval_return\n    value: 869.9\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: results\n    paragraph: 16\n    sentence: 1\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: peak_eval_return\n    value: 715.21\n    role: primary_evidence\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: results\n    paragraph: 17\n    sentence: 0\n  text: baseline seed 2 (009a) stable at 836.5\n  type: quantitative\n  evidence:\n  - exp_id: exp_009a_baseline_walker_s2\n    metric: final_eval_return\n    value: 836.51\n    role: control\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: results\n    paragraph: 18\n    sentence: 1\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_eval_return\n    value: 136.96\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: results\n    paragraph: 19\n    sentence: 0\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 21\n    sentence: 0\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f reward gap 1.01x (MAE 0.7469)\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.reward_gap\n    value: 1.01\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 21\n    sentence: 1\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 0\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\n    2.90x'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.68\n    role: stage1\n  - exp_id: exp_008d_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 2.9\n    role: stage2\n  decisions:\n  - D042\n  deprecated: false\n- id: C037\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 1\n  text: ~36% dynamics bias, ~64% actor exploitation\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: dynamics_bias_fraction\n    value: 0.36\n    role: primary_evidence\n  decisions:\n  - D042\n  deprecated: false\n- id: C038\n  location:\n    section: analysis\n    paragraph: 2\n    sentence: 2\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: random_policy_reward_ratio\n    value: 1.11\n    role: control\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    metric: trained_actor_reward_ratio\n    value: 0.98\n    role: control\n  decisions:\n  - D042\n  deprecated: false\n- id: C039\n  location:\n    section: analysis\n    paragraph: 4\n    sentence: 0\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\n  type: quantitative\n  evidence:\n  - exp_id: exp_008d_subsample_on_h8\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: primary_evidence\n  - exp_id: exp_009e_008d_walker_s1\n    metric: peak_nve\n    value: 4.12\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: analysis\n    paragraph: 7\n    sentence: 0\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008f_no_dtEmb.dt1_reward_mae\n    value: 0.7469\n    role: primary_evidence\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.dt1_reward_mae\n    value: 0.0568\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: analysis\n    paragraph: 8\n    sentence: 1\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\n  type: quantitative\n  evidence:\n  - exp_id: exp_008e_v3_walker_s2\n    metric: final_nve\n    value: 3.78\n    role: false_positive\n  decisions:\n  - D053\n  deprecated: false\n- id: C042\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 2\n  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: accuracy_n56\n    value: 0.946\n    role: primary_evidence\n  decisions:\n  - D053\n  deprecated: false\n- id: C043\n  location:\n    section: conclusion\n    paragraph: 2\n    sentence: 1\n  text: NVE margin 0.62 excluding outlier\n  type: quantitative\n  evidence:\n  - exp_id: exp_009b_008d_walker_s2\n    metric: peak_nve\n    value: 1.62\n    role: lowest_true_positive\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\n    healthy, return collapses ~35K steps before entropy rises'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/methodology\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  - exp_id: plan_034_nve_threshold\n    metric: f1_n56\n    value: 0.941\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 classification (n=56, AUROC=0.990, F1=0.941)\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/abstract_body\n    paragraph: 0\n    sentence: 0\n  text: CIVO classification 53/56 AUROC=0.990 F1=0.941\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: NVE threshold 53/56 classification in introduction\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: Contribution 1 AUROC updated to 0.990\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/conclusion\n    paragraph: 0\n    sentence: 0\n  text: Conclusion NVE updated to 53/56 AUROC=0.990\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n56\n    value: 0.990\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\n  type: quantitative\n  evidence:\n  - exp_id: plan_034_nve_threshold\n    metric: auroc_n32\n    value: 0.961\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\n  type: quantitative\n  evidence:\n  - exp_id: exp_064_value_distribution\n    metric: civo_median_v_mc_ratio\n    value: 3.4\n    role: primary_evidence\n  - exp_id: exp_064_value_distribution\n    metric: control_median_v_mc_ratio\n    value: 1.05\n    role: control\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\n    vs +0.07-0.22 healthy'\n  type: quantitative\n  evidence:\n  - exp_id: plan_031_actor_entropy\n    metric: collapsed_entropy_rate\n    value: 2.1\n    role: primary_evidence\n  - exp_id: plan_031_actor_entropy\n    metric: healthy_entropy_rate_range\n    value: 0.07-0.22\n    role: control\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\n    Cheetah'\n  type: quantitative\n  evidence:\n  - exp_id: exp_026_obs_sgs_cheetah\n    metric: nve_amplification\n    value: 21.9-30.2\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\n    baseline'\n  type: quantitative\n  evidence:\n  - exp_id: exp_030c_tcn_cheetah\n    metric: nve_suppressed\n    value: 0.3\n    role: primary_evidence\n  - exp_id: exp_030c_tcn_cheetah\n    metric: eval_pct_baseline\n    value: 15\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\n    to -0.86 at 75K'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_25k_range\n    value: -0.87 to -0.94\n    role: primary_evidence\n  - exp_id: exp_065_dt_emb_cosine\n    metric: trained_cos_75k_range\n    value: -0.70 to -0.86\n    role: primary_evidence\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\n  type: quantitative\n  evidence:\n  - exp_id: exp_065_dt_emb_cosine\n    metric: frozen_cos_constant\n    value: -0.15 to +0.07\n    role: control\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\n  type: quantitative\n  evidence:\n  - exp_id: exp_rssm_fidelity_analysis\n    metric: 008d_trained_dtEmb.reward_gap\n    value: 2.78\n    role: primary_evidence\n  - exp_id: exp_063_rssm_fidelity\n    metric: collapsed_reward_gap\n    value: 3.11\n    role: corroboration\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\n    conditioning\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\n  decisions: []\n  deprecated: false\n- id: C064\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\n    vs baseline 1.46x)\n  type: quantitative\n  evidence: exp_063 obs_mse data\n  decisions: []\n  deprecated: false\n- id: C065\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\n    median 1.05x (52.5% overestimated)\n  type: quantitative\n  evidence: exp_064 value_distribution results_summary\n  decisions: []\n  deprecated: false\n- id: C066\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\n    pathology\n  type: quantitative\n  evidence: exp_063 rssm_fidelity_analysis\n  decisions: []\n  deprecated: false\n- id: C067\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\n  type: quantitative\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\n  decisions: []\n  deprecated: false\n- id: C068\n  location:\n    section: sections/results\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\n    improvement\n  type: quantitative\n  evidence: exp_066 timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C069\n  location:\n    section: sections/analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\n    → entropy destabilization (~35K later), n=1'\n  type: quantitative\n  evidence: exp_066 timeseries + actor entropy analysis\n  decisions: []\n  deprecated: false\n- id: C070\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\n    VE ratio near zero until 40K spike (1.59x)'\n  type: quantitative\n  evidence: exp_066 12-checkpoint timeseries analysis\n  decisions: []\n  deprecated: false\n- id: C071\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\n    selective improvement not worsening\n  type: quantitative\n  evidence: exp_066 timeseries MAE data\n  decisions: []\n  deprecated: false\ntables:\n- id: T001\n  location:\n    section: methodology\n    table_number: 1\n  caption: Factorial design — 9 configurations\n  cells:\n  - row: 0\n    col: 0\n    value: '001'\n    source:\n      exp_id: exp_001_baseline\n      metric: exp_id\n  - row: 1\n    col: 0\n    value: '006'\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: exp_id\n  - row: 2\n    col: 0\n    value: '007'\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: exp_id\n  - row: 3\n    col: 0\n    value: '005'\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: exp_id\n  - row: 4\n    col: 0\n    value: 008d\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: exp_id\n  - row: 5\n    col: 0\n    value: 008f\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: exp_id\n  - row: 6\n    col: 0\n    value: 008a\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: exp_id\n  - row: 7\n    col: 0\n    value: 008c\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: exp_id\n  - row: 8\n    col: 0\n    value: 008e_v3\n    source:\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\n      metric: exp_id\n  deprecated: false\n- id: T002\n  location:\n    section: results\n    table_number: 1\n  caption: All configurations and outcomes\n  cells:\n  - row: 0\n    col: 5\n    value: 915.7\n    source:\n      exp_id: exp_001_baseline\n      metric: eval_return_105K\n  - row: 1\n    col: 5\n    value: 132.9\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: eval_return_65K\n  - row: 1\n    col: 6\n    value: 4.83\n    source:\n      exp_id: exp_006_fixed_dt2\n      metric: peak_nve\n  - row: 2\n    col: 5\n    value: 152.5\n    source:\n      exp_id: exp_007_fixed_dt4\n      metric: eval_return_55K\n  - row: 3\n    col: 5\n    value: 98.8\n    source:\n      exp_id: exp_005_event_gated_v4\n      metric: eval_return_145K\n  - row: 4\n    col: 5\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 4\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 5\n    col: 5\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 5\n    col: 6\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 6\n    col: 5\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  - row: 6\n    col: 6\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 7\n    col: 5\n    value: 503.0\n    source:\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\n      metric: eval_return_105K\n  - row: 8\n    col: 5\n    value: 148.3\n    source:\n      exp_id: exp_009c_008f_walker_s2\n      metric: final_eval_return\n  - row: 9\n    col: 5\n    value: 777.7\n    source:\n      exp_id: exp_008a_no_subsample_dt2\n      metric: eval_return_105K\n  - row: 10\n    col: 5\n    value: 240.9\n    source:\n      exp_id: exp_008c_no_subsample_dt2_h8\n      metric: eval_return_65K\n  - row: 11\n    col: 5\n    value: 869.9\n    source:\n      exp_id: exp_008e_v3_walker_s1\n      metric: final_eval_return\n  - row: 12\n    col: 5\n    value: 137.0\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_eval_return\n  - row: 12\n    col: 6\n    value: 3.78\n    source:\n      exp_id: exp_008e_v3_walker_s2\n      metric: final_nve\n  - row: 13\n    col: 5\n    value: 836.5\n    source:\n      exp_id: exp_009a_baseline_walker_s2\n      metric: final_eval_return\n  deprecated: false\n- id: T003\n  location:\n    section: results\n    table_number: 2\n  caption: RSSM fidelity at dt=1 vs dt=2\n  cells:\n  - row: 0\n    col: 0\n    value: 13.49\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_obs_mse\n  - row: 0\n    col: 1\n    value: 27.5\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_obs_mse\n  - row: 0\n    col: 2\n    value: 2.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.obs_gap\n  - row: 0\n    col: 3\n    value: 0.0102\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt1_reward_mae\n  - row: 0\n    col: 4\n    value: 0.0159\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.dt2_reward_mae\n  - row: 0\n    col: 5\n    value: 1.56\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: baseline.reward_gap\n  - row: 1\n    col: 0\n    value: 41.31\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_obs_mse\n  - row: 1\n    col: 1\n    value: 53.67\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_obs_mse\n  - row: 1\n    col: 2\n    value: 1.3\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.obs_gap\n  - row: 1\n    col: 3\n    value: 0.0568\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt1_reward_mae\n  - row: 1\n    col: 4\n    value: 0.1579\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.dt2_reward_mae\n  - row: 1\n    col: 5\n    value: 2.78\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008d_trained_dtEmb.reward_gap\n  - row: 2\n    col: 0\n    value: 8.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_obs_mse\n  - row: 2\n    col: 1\n    value: 22.04\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_obs_mse\n  - row: 2\n    col: 2\n    value: 2.75\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.obs_gap\n  - row: 2\n    col: 3\n    value: 0.7469\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt1_reward_mae\n  - row: 2\n    col: 4\n    value: 0.7526\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.dt2_reward_mae\n  - row: 2\n    col: 5\n    value: 1.01\n    source:\n      exp_id: exp_rssm_fidelity_analysis\n      metric: 008f_no_dtEmb.reward_gap\n  deprecated: false\n- id: T004\n  location:\n    section: results\n    table_number: 3\n  caption: Post-CIVO outcomes for 008d configuration\n  cells:\n  - row: 0\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 1\n    value: 4.12\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: peak_nve\n  - row: 0\n    col: 2\n    value: 82.8\n    source:\n      exp_id: exp_008d_subsample_on_h8\n      metric: eval_return_55K\n  - row: 1\n    col: 0\n    value: 1.62\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: peak_nve\n  - row: 1\n    col: 1\n    value: 0.38\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_nve\n  - row: 1\n    col: 2\n    value: 267.9\n    source:\n      exp_id: exp_009b_008d_walker_s2\n      metric: final_eval_return\n  - row: 2\n    col: 0\n    value: 4.12\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: peak_nve\n  - row: 2\n    col: 1\n    value: 1.57\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_nve\n  - row: 2\n    col: 2\n    value: 131.1\n    source:\n      exp_id: exp_009e_008d_walker_s1\n      metric: final_eval_return\n  deprecated: false\nfigures:\n- id: F001\n  location:\n    section: results\n    figure_number: 1\n  caption: Learning curves for all configurations\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n    - exp_id: exp_005_event_gated_v4\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n  output_path: figures/paper/fig1_learning_curves.pdf\n  deprecated: false\n- id: F002\n  location:\n    section: results\n    figure_number: 2\n  caption: Normalized value-to-eval ratio trajectories\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008e_v3_walker_s1\n    - exp_id: exp_009b_008d_walker_s2\n  output_path: figures/paper/fig2_nve_trajectory.pdf\n  deprecated: false\n- id: F003\n  location:\n    section: results\n    figure_number: 3\n  caption: Factorial experiment summary grid\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\n    - exp_id: exp_008a_no_subsample_dt2\n    - exp_id: exp_008c_no_subsample_dt2_h8\n  output_path: figures/paper/fig3_factorial_grid.pdf\n  deprecated: false\n- id: F004\n  location:\n    section: results\n    figure_number: 4\n  caption: Peak evaluation return as function of imagination dt\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_001_baseline\n    - exp_id: exp_006_fixed_dt2\n    - exp_id: exp_007_fixed_dt4\n  output_path: figures/paper/fig5_dt_amplification.pdf\n  deprecated: false\n- id: F005\n  location:\n    section: results\n    figure_number: 5\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\n  type: result\n  source:\n    experiments:\n    - exp_id: exp_008d_subsample_on_h8\n    - exp_id: exp_008e_v3_walker_s2\n    - exp_id: exp_009a_baseline_walker_s2\n  output_path: figures/paper/fig6_multiple_pathways.pdf\n  deprecated: false\n- id: F006\n  location:\n    section: sections/appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n_completeness:\n  coverage: 73/77\n  claims: 71\n  tables: 4\n  figures: 6\n  tier_counts:\n    tier1: 0\n    tier2: 73\n    tier3: 4\n    tierX: 0\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 865,
        "oldLines": 12,
        "newStart": 865,
        "newLines": 12,
        "lines": [
          "     section: sections/analysis",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961",
          "+  text: Discussion NVE diagnostic consolidated to n=56 AUROC=0.990",
          "   type: quantitative",
          "   evidence:",
          "   - exp_id: plan_034_nve_threshold",
          "-    metric: auroc_n32",
          "-    value: 0.961",
          "+    metric: auroc_n56",
          "+    value: 0.990",
          "     role: primary_evidence",
          "   decisions: []",
          "   deprecated: false"
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

_source line 44_

Now verifying — scanning the file for any remaining old NVE values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "c338099b-b165-47d1-813f-d87abce10874",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YajPCC9QbRzwTvosoUHw85",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 339,
      "cache_read_input_tokens": 63995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 339
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

_source line 45_

<details open><summary>🔧 Tool call — Grep · `toolu_01Djqd8usbPuMJ3nGr2uzcYh`</summary>

```json
{
  "pattern": "0\\.961|0\\.933|0\\.880|n=32|n=8[^0-9]|7/8|29/32|27/30",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "9ef2c80f-6a4c-43fa-8377-1ae7f873c579",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YajPCC9QbRzwTvosoUHw85",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 339,
      "cache_read_input_tokens": 63995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 339
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

_source line 46 · 2026-05-25T14:13:02.567Z_

<details><summary>↩ Tool result · `toolu_01Djqd8usbPuMJ3nGr2uzcYh`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "21e9863d-0d73-4c9d-a5c4-cc112f28c9e9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---


### Assistant

_source line 47_

No stale values remain. Now let me do a quick sanity check that the new values are present and consistent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "65442cef-8342-4e0c-b9f8-277564cc7cad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BUakUTRzWy6XxTCtBuxLT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 64334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 192
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

_source line 48_

<details open><summary>🔧 Tool call — Grep · `toolu_01JJfKt7NrsfXrRZPnnGwhZb`</summary>

```json
{
  "pattern": "0\\.990|n=56|53/56|0\\.941",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "d095df65-9b8a-4111-a435-5e0832f09c4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BUakUTRzWy6XxTCtBuxLT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 64334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 192
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

_source line 49 · 2026-05-25T14:13:06.078Z_

<details><summary>↩ Tool result · `toolu_01JJfKt7NrsfXrRZPnnGwhZb`</summary>

```text
70:  text: 53/56 classification (n=56, AUROC=0.990)
75:    value: 0.990
191:  text: 53/56 accuracy (AUROC=0.990, n=56)
196:    value: 0.990
307:  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)
312:    value: 0.990
316:    value: 0.941
708:  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)
713:    value: 0.990
741:  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold
746:    value: 0.941
755:  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941
760:    value: 0.990
780:  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56
785:    value: 0.990
789:    value: 0.941
798:  text: NVE threshold 53/56 classification (n=56, AUROC=0.990, F1=0.941)
803:    value: 0.990
812:  text: CIVO classification 53/56 AUROC=0.990 F1=0.941
817:    value: 0.990
826:  text: NVE threshold 53/56 classification in introduction
831:    value: 0.990
840:  text: Contribution 1 AUROC updated to 0.990
845:    value: 0.990
854:  text: Conclusion NVE updated to 53/56 AUROC=0.990
859:    value: 0.990
868:  text: Discussion NVE diagnostic consolidated to n=56 AUROC=0.990
873:    value: 0.990
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "4f816a8a-cded-447e-bd7f-122afdd8326a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "70:  text: 53/56 classification (n=56, AUROC=0.990)\n75:    value: 0.990\n191:  text: 53/56 accuracy (AUROC=0.990, n=56)\n196:    value: 0.990\n307:  text: AUROC=0.990, 53/56 accuracy (n=56, F1=0.941, threshold NVE≥1.5)\n312:    value: 0.990\n316:    value: 0.941\n708:  text: 53/56 CIVO classification (n=56, 94.6%, AUROC=0.990)\n713:    value: 0.990\n741:  text: Extended NVE validation (n=56) achieves F1=0.941 at NVE≥1.5 threshold\n746:    value: 0.941\n755:  text: NVE diagnostic extended validation n=56 AUROC=0.990 F1=0.941\n760:    value: 0.990\n780:  text: NVE threshold 53/56 accuracy (AUROC=0.990, F1=0.941) at n=56\n785:    value: 0.990\n789:    value: 0.941\n798:  text: NVE threshold 53/56 classification (n=56, AUROC=0.990, F1=0.941)\n803:    value: 0.990\n812:  text: CIVO classification 53/56 AUROC=0.990 F1=0.941\n817:    value: 0.990\n826:  text: NVE threshold 53/56 classification in introduction\n831:    value: 0.990\n840:  text: Contribution 1 AUROC updated to 0.990\n845:    value: 0.990\n854:  text: Conclusion NVE updated to 53/56 AUROC=0.990\n859:    value: 0.990\n868:  text: Discussion NVE diagnostic consolidated to n=56 AUROC=0.990\n873:    value: 0.990",
    "numLines": 28
  }
}
```

</details>

---


### Assistant

_source line 50_

Now saving the file via the MCP tool to persist the changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "e55ba642-0015-4c58-b1f4-68b0d562eadc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HyfU7WA2Wa64MFcguHHrpe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 64526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 703
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

_source line 51_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014CFbyPEc8eNetKqNKyfmKk`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "d5a784b6-8cd8-498c-874a-4d6c836dbaf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HyfU7WA2Wa64MFcguHHrpe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 64526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 703
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

_source line 52 · 2026-05-25T14:13:11.409Z_

<details><summary>↩ Tool result · `toolu_014CFbyPEc8eNetKqNKyfmKk`</summary>

````text
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
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "8ddb8fc0-e6f4-449e-995a-f4104e6f4c85",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---


### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
The `save_project_file` tool only allows writing to `memory.md`, `writing_plan.yaml`, and `paper_framing.md`. The `paper_provenance.yaml` file is not in the whitelist. But I already edited the file directly using the Edit tool, so the changes are already saved to disk. Let me verify the file was properly modified by reading back the key sections.

Actually, the Edit tool already modified the file on disk. The MCP save tool has a restricted whitelist that doesn't include paper_provenance.yaml. The edits are already persisted via the Edit tool. Let me just verify the final state is correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "c16a5c93-c11a-4d68-9c08-d2a9e2714fec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ms33mGGTDv9xLyHRJa6GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 65229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 378
      },
      "output_tokens": 0,
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

_source line 54_

The file was already modified directly on disk via the Edit tool. Let me do a final verification by reading the updated entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "370c1e6a-179b-4335-aaf2-1b6f8d441a22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ms33mGGTDv9xLyHRJa6GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 65229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 378
      },
      "output_tokens": 0,
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

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DqkKfEJXcQZf2GQWEnvtbZ`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_provenance.yaml",
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
  "session_id": "2dbaa264-008d-4d5c-9efc-081f6f40d0c3",
  "uuid": "e992d4ed-d54b-49b8-b3bb-64af9ae59708",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ms33mGGTDv9xLyHRJa6GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 65229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 378
      },
      "output_tokens": 0,
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
