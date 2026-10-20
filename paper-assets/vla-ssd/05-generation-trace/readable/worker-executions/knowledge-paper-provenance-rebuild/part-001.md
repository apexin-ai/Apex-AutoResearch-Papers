# knowledge paper provenance rebuild — Part 1 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

[Transcript overview](../knowledge-paper-provenance-rebuild.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/95/954c65970ba1f4b4fa36.json)

## Before a recorded user message

## Before a recorded user message

23 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
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
  "uuid": "29e8ccfa-bcbc-41b8-85d4-c182605cd52e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
  },
  "fast_mode_state": "off"
}
```

---


### Assistant

_source line 3_

I'll start by reading the current paper_provenance.yaml to understand the existing structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "45b07c39-eb53-47ba-b912-a3fee160f128",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xrccubvwvuMtRgBvSQinT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12610,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12610
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

_source line 4_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014bAzVBi22UtrWeeMKSgYxr`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
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
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "fd8f6382-ad1f-4282-8fee-4192ac9628b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xrccubvwvuMtRgBvSQinT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12610,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12610
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

_source line 5 · 2026-05-18T17:42:04.069Z_

<details><summary>↩ Tool result · `toolu_014bAzVBi22UtrWeeMKSgYxr`</summary>

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
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "2c836593-4d13-41da-9b96-90c72195eac0",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Runtime record

_source line 6_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779140400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c2ae46bc-332b-4bda-bec6-456b1cabcbb3",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current paper_provenance.yaml to understand the existing structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "e63f3caa-9081-4e60-8bd9-33331ca67dd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPFSdF1o7V7YDZMSbuNp9o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 24451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1066
      },
      "output_tokens": 57,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CrPZRnZp85eE6j3pZ5GRg7`</summary>

```json
{
  "project": "vla-ssd",
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
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "bf7253e7-ebfc-4ac5-87ee-2fa32a9f854d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPFSdF1o7V7YDZMSbuNp9o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 24451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1066
      },
      "output_tokens": 57,
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

_source line 9 · 2026-05-18T17:42:07.513Z_

<details><summary>↩ Tool result · `toolu_01CrPZRnZp85eE6j3pZ5GRg7`</summary>

```text
&lt;persisted-output>
Output too large (54.7KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/da042411-baa9-4148-b88d-99c95c45f67d/tool-results/toolu_01CrPZRnZp85eE6j3pZ5GRg7.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml\", \"content\": \"claims:\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915\\n    tier: tier1\\n  - exp_id: plan_013_branch_split\\n    metric: post_projector_4096d_rsa=0.615\\n    tier: tier1\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.clip_cls=0.557\\n    tier: tier1\\n  id: C001\\n  location:\\n    context: result_statement\\n    section: abstract\\n  text: 'First, self-supervised pretraining provides the strongest action-relevant\\n    geometry: standalone DINOv2 achieves RSA $ = 0.692$, exceeding all VL-pretrained\\n    encoders (DinoSigLIP+Projector $ = 0.615$; CL'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_image_mean_peak.rsa=0.6282\\n    tier: tier1\\n  - exp_id: d041_method_b_rsa\\n    metric: untrained_image_mean_peak.rsa=0.6117\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\n    tier: tier1\\n  id: C002\\n  location:\\n    context: result_statement\\n    section: abstract\\n  text: 'Second, the LLM applies a non-monotonic transformation---the first 12 layers\\n    enhance geometric alignment with the action space above the vision encoder input\\n    ($$: $0.612  0.628$ at L12), while the rem'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017,significant=false\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686,p=0.00
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "823d8a62-37e0-470a-95e1-14b7754d0d62",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml\\\", \\\"content\\\": \\\"claims:\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915\\\\n    tier: tier1\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: post_projector_4096d_rsa=0.615\\\\n    tier: tier1\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.clip_cls=0.557\\\\n    tier: tier1\\\\n  id: C001\\\\n  location:\\\\n    context: result_statement\\\\n    section: abstract\\\\n  text: 'First, self-supervised pretraining provides the strongest action-relevant\\\\n    geometry: standalone DINOv2 achieves RSA $ = 0.692$, exceeding all VL-pretrained\\\\n    encoders (DinoSigLIP+Projector $ = 0.615$; CL'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained_image_mean_peak.rsa=0.6282\\\\n    tier: tier1\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: untrained_image_mean_peak.rsa=0.6117\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\\\n    tier: tier1\\\\n  id: C002\\\\n  location:\\\\n    context: result_statement\\\\n    section: abstract\\\\n  text: 'Second, the LLM applies a non-monotonic transformation---the first 12 layers\\\\n    enhance geometric alignment with the action space above the vision encoder input\\\\n    ($$: $0.612  0.628$ at L12), while the rem'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017,significant=false\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686,p=0.0001\\\\n    tier: tier1\\\\n  id: C003\\\\n  location:\\\\n    context: result_statement\\\\n    section: abstract\\\\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\\\\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\\\\n    capacity (R^2 Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence: llama2base_action_probe experiment\\\\n  id: C004\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: 'Linear CKA~kornblith2019 reverses the RSA ordering: untrained LLM ($CKA =\\\\n    0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2\\\\n    ($0.066$), partially inverting the self-superv'\\\\n  type: quantitative\\\\n  decisions: []\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: plan_009_cka_verification\\\\n    metric: rdm_cka.*\\\\n    tier: tier1\\\\n  id: C005\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: 'RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $$\\\\n    Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).'\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: plan_009_cka_verification\\\\n    metric: linear_cka per-layer (derived from full scan)\\\\n    tier: tier2\\\\n  id: C006\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: At the per-layer level, linear CKA between image\\\\\\\\_mean and the action space\\\\n    rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U\\\\n    pattern.\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.*\\\\n    tier: tier1\\\\n  - exp_id: plan_009_cka_verification\\\\n    metric: linear_cka.* + rdm_cka.*\\\\n    tier: tier1\\\\n  id: C007\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: 'Three similarity metrics across representation sources. (a)~RSA ranks DINOv2\\\\n    cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). (b)~Linear CKA reverses\\\\n    the ordering: Untrained ($0.089$) $>$ Tr'\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: fused_2176d_rsa=0.634\\\\n    tier: tier1\\\\n  id: C008\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: Fusion produces a representation ($ = 0.634$) that exceeds either branch alone,\\\\n    indicating that concatenation captures complementary structure.\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: fused_2176d_rsa=0.634, post_projector_4096d_rsa=0.615\\\\n    tier: tier1\\\\n  id: C009\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: 'The MLP projector then compresses this signal: DinoSigLIP+Projector achieves\\\\n    $ = 0.615$, a drop of $ = 0.019$ from the fused 2{,176-D input.'\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: standalone_dino_patch_mean_rsa=0.631\\\\n    tier: tier1\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_patch_mean=0.6307\\\\n    tier: tier1\\\\n  id: C010\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: DINOv2 patch\\\\\\\\_mean achieves RSA $ = 0.631$, between the cls\\\\\\\\_token ($0.692$)\\\\n    and the fused DinoSigLIP ($0.634$).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915, trained_image_mean_peak\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\\\n    tier: tier1\\\\n  id: C011\\\\n  location:\\\\n    context: result_statement\\\\n    section: conclusion\\\\n  text: 'Three findings emerge: (1)~the frozen vision encoder provides the dominant\\\\n    action-relevant geometry, with self-supervised DINOv2 achieving the highest alignment\\\\n    ($ = 0.692$) exceeding all VL-pretraine'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915\\\\n    tier: tier1\\\\n  id: C012\\\\n  location:\\\\n    context: result_statement\\\\n    section: discussion\\\\n  text: 'The vision encoder is the source: self-supervised DINOv2 achieves the highest\\\\n    geometric alignment ($ = 0.692$), exceeding all VLA internal representations.'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.image_mean.p=0.006\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686\\\\n    tier: tier1\\\\n  id: C013\\\\n  location:\\\\n    context: result_statement\\\\n    section: discussion\\\\n  text: 'Training redistributes geometry but enhances decodability: modest geometric\\\\n    gain (Delta = 0.017--0.023, 3--4% of baseline across two benchmarks), while substantially\\\\n    improving R^2 (Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.significant=false\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  id: C014\\\\n  location:\\\\n    context: result_statement\\\\n    section: discussion\\\\n  text: Cross-benchmark replication (LIBERO-Spatial Delta = 0.023, p < 0.001) suggests\\\\n    the LIBERO-Goal RSA CI (incl. zero) reflects limited power rather than a true\\\\n    null, but the effect remains small (3--4% of baseline).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915\\\\n    tier: tier1\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: fused_2176d_rsa=0.634, standalone_dino_patch_mean_rsa=0.631\\\\n    tier: tier1\\\\n  id: C015\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: The standalone DINOv2 cls\\\\\\\\_token achieves the highest alignment of any representation\\\\n    source ($ = 0.692$), followed by the fused DinoSigLIP 2{,176-D representation\\\\n    before projection ($ = 0.634$) and t\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.clip_cls=0.557\\\\n    tier: tier1\\\\n  id: C016\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: CLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment\\\\n    among pretrained encoders ($ = 0.557$; Figure~fig:rsa_bar).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557, trained_image_mean_peak.rsa=0.6282\\\\n    tier: tier1\\\\n  id: C017\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: DINOv2, pretrained with self-supervised objectives alone, achieves $ = 0.692$---exceeding\\\\n    not only CLIP ($ = 0.557$) but also the VLA's own internal representations at\\\\n    their peaks (trained image\\\\\\\\_mean\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\\\\n    tier: tier1\\\\n  - exp_id: unified_action_probe\\\\n    metric: bootstrap_pairwise.projector_vs_dino.p=0.557\\\\n    tier: tier1\\\\n  id: C018\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'Functional probes corroborate the ranking: DINOv2 cls\\\\\\\\_token achieves $R^2\\\\n    = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$,\\\\n    $p = 0.557$, n.s.), while CLIP yields the'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: dinov2_branch_rsa=0.619, siglip_branch_rsa=0.621\\\\n    tier: tier1\\\\n  id: C019\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: The DINOv2 (1{,024-D) and SigLIP (1{,152-D) branches yield near-identical\\\\n    RSA ($0.619$ vs.\\\\\\\\ $0.621$); fusion exceeds either ($0.634$), while the projector\\\\n    introduces modest compression loss ($0.634  0\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: all RSA values\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: all R2 peak values\\\\n    tier: tier1\\\\n  id: C020\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Geometric (RSA $$) and functional (probe $R^2$) alignment with the action\\\\n    space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both trained\\\\n    readout and image\\\\\\\\_mean exceed the projector in\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines + trained_image_mean_peak\\\\n    tier: tier1\\\\n  id: C021\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'RSA with the action space ($$) across representation sources. Self-supervised\\\\n    DINOv2 cls\\\\\\\\_token ($=0.692$) achieves the highest geometric alignment, followed\\\\n    by fused DinoSigLIP ($0.634$) and the VLA '\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained_image_mean per-layer RSA (L0=0.612, L12=0.628, L32=0.422)\\\\n    tier: tier1\\\\n  id: C022\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'Figure~fig:layer_curves reveals a non-monotonic trajectory for trained image\\\\\\\\_mean\\\\n    RSA: $$ begins at $0.612$ (L0, equal to the projector input), rises to a peak\\\\n    of $0.628$ at L12---above the DinoSigLI'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_image_mean_peak.layer=8, mean_R2=0.6553\\\\n    tier: tier1\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: projector_mean_R2=0.6298\\\\n    tier: tier1\\\\n  id: C023\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Full-layer probe scans reveal that trained image\\\\\\\\_mean $R^2$ peaks at L8 ($0.655$),\\\\n    exceeding the projector ($0.630$, $ = +0.025$; Table~tab:rsa_overview).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_image_mean_peak.layer=8\\\\n    tier: tier1\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained_image_mean_peak.layer=12\\\\n    tier: tier1\\\\n  id: C024\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: The $R^2$ peak (L8) precedes the RSA peak (L12) by four layers, suggesting\\\\n    that functional decodability peaks earlier than geometric alignment; we adopt\\\\n    ``early-to-middle layers (L8--L13)'' to capture\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained_last_preaction_peak.rsa=0.6425, layer=12\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_last_preaction_peak.mean_R2=0.6779, layer=13\\\\n    tier: tier1\\\\n  id: C025\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Trained readout achieves peak RSA $ = 0.643$ at L12 and probe $R^2 = 0.678$\\\\n    (L13), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $ = 0.048$; Table~tab:rsa_overview,\\\\n    Figure~fig:probe_bars).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained per-layer RSA L12=0.628→L32=0.422; untrained 0.612→0.545\\\\n    tier: tier1\\\\n  id: C026\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'The decline from L12 to L32 ($$: $0.628  0.422$) exceeds the untrained decay\\\\n    ($0.612  0.545$), indicating that training actively redirects later layers away\\\\n    from action geometry, yielding a three-phas'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_last_preaction_peak=0.6779, trained_image_mean_peak=0.6553\\\\n    tier: tier1\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: projector_mean_R2=0.6298, dino_cls_mean_R2=0.6343\\\\n    tier: tier1\\\\n  id: C027\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Functional probe $R^2$ for action prediction (best layer for each source).\\\\n    Both trained readout ($R^2{=0.678$, L13) and trained image\\\\\\\\_mean ($0.655$, L8)\\\\n    exceed the projector baseline ($0.630$), confi\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  id: C028\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: best-vs-best Delta = +0.017 (3% of baseline; LIBERO-Spatial confirms with\\\\n    Delta = +0.023, 4%, p < 0.001). This geometric gain is far smaller than the functional\\\\n    improvement.\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\\\n    tier: tier1\\\\n  id: C029\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: RSA best-vs-best yields at most a modest gain (Delta = 0.017--0.023, 3--4%\\\\n    of baseline across two benchmarks), while R^2 shows substantially larger improvements.\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006; last_preaction.delta=0.0686,p=0.0001\\\\n    tier: tier1\\\\n  id: C030\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Yet $R^2$ best-vs-best is significant for both image\\\\\\\\_mean ($ = +0.015$, $p\\\\n    = 0.006$) and readout ($ = +0.069$, $p < 0.0001$; Table~tab:training_effects).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_same_layer.last_preaction_L13.note (untrained L13 R2 near -0.33)\\\\n    tier: tier1\\\\n  id: C031\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Untrained readout $R^2$ reaches $ -0.33$ at L12--L29 (predictions worse than\\\\n    a constant-mean baseline), while untrained image\\\\\\\\_mean $R^2$ drops to near-zero\\\\n    at L10--L13.\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best + same_layer\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best\\\\n    tier: tier1\\\\n  id: C032\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'Training effects on action-relevant structure (LIBERO-Goal; bootstrap). RSA\\\\n    best-vs-best yields modest geometric gain (Delta=+0.017, 3%; LIBERO-Spatial: +0.023,\\\\n    p<0.001), while R^2 shows substantially larger functional gains.'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: instruction_effect (derived from trained_with_inst vs trained_no_inst)\\\\n    tier: tier1\\\\n  - exp_id: plan_008_random_inst_control\\\\n    metric: max_absolute_delta=0.0165, instruction_invariant=true\\\\n    tier: tier1\\\\n  id: C033\\\\n  location:\\\\n    context: finding_statement\\\\n    section: experiments\\\\n  text: This confirms that the action geometry is visually grounded and instruction-independent~grant2026.\\\\n  type: methodological\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: experimental design (2x2 factorial)\\\\n    tier: tier2\\\\n  id: C034\\\\n  location:\\\\n    context: result_statement\\\\n    section: introduction\\\\n  text: We cross training status (trained vs.\\\\\\\\ untrained, reinitializing 6.74B LLM\\\\n    parameters) with instruction presence in a $2 2$ factorial design, and quantify\\\\n    action-relevant structure using RSA~kriegesko\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557\\\\n    tier: tier1\\\\n  id: C035\\\\n  location:\\\\n    context: result_statement\\\\n    section: introduction\\\\n  text: Standalone DINOv2 achieves the highest action-space alignment (RSA $ = 0.692$),\\\\n    far exceeding CLIP ($ = 0.557$) and the VLA's own peak internal representation\\\\n    ($ = 0.628$ at L12).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\\\\n    tier: tier1\\\\n  id: C036\\\\n  location:\\\\n    context: result_statement\\\\n    section: introduction\\\\n  text: 'Functional probes corroborate this ranking: DINOv2 ($R^2 = 0.634$) $$ Projector\\\\n    ($0.630$) $>$ CLIP ($0.587$).'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained_image_mean_peak.rsa=0.6282\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\\\n    tier: tier1\\\\n  id: C037\\\\n  location:\\\\n    context: result_statement\\\\n    section: introduction\\\\n  text: 'Second, the LLM applies a non-monotonic transformation: the first 12 layers\\\\n    enhance geometric alignment above the vision encoder input ($$: $0.612  0.628$),\\\\n    while the remaining 20 layers degrade it ($'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: methodology (encoder extraction)\\\\n    tier: tier2\\\\n  id: C038\\\\n  location:\\\\n    context: bold\\\\n    section: method\\\\n  text: DINOv2 ViT-L/14\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: methodology (CLIP extraction)\\\\n    tier: tier2\\\\n  id: C039\\\\n  location:\\\\n    context: bold\\\\n    section: method\\\\n  text: CLIP ViT-L/14\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\\\n    tier: tier1\\\\n  id: C040\\\\n  location:\\\\n    context: result_statement\\\\n    section: introduction\\\\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\\\\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\\\\n    capacity---redistribution dominates over creation.\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: rsa.trained_image_mean_peak(layer=14,rsa=0.691), action_probe.trained_image_mean_peak(layer=13,R2=0.696)\\\\n    tier: tier1\\\\n  id: C041\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'Cross-benchmark validation (LIBERO-Spatial): inverted-U replicates, trained\\\\n    image_mean RSA peaks at L14 (rho=0.691), R^2 at L13 (0.696), peak shifting ~2\\\\n    layers deeper than LIBERO-Goal.'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,ci_95=[0.012,0.036],p=0.001\\\\n    tier: tier1\\\\n  id: C042\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Training produces a significant geometric gain on LIBERO-Spatial (best-vs-best\\\\n    Delta=+0.023, p<0.001), confirming LIBERO-Goal effect reflects limited power.\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: rsa.trained_last_preaction_peak(layer=15), action_probe.trained_last_preaction_peak(layer=21)\\\\n    tier: tier1\\\\n  id: C043\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: RSA--R^2 peak convergence does not replicate on LIBERO-Spatial (RSA L15 vs\\\\n    R^2 L21, 6-layer gap vs 1 on Goal), suggesting peak alignment may be benchmark-specific.\\\\n  type: quantitative\\\\n- id: C044\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Image tokens encode purely visual information (instruction classification\\\\n    at chance, 10%, across all layers)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: image_mean_accuracy\\\\n    value: 10%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C046\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Readout token: 100% instruction classification from L1, LOOCV-verified'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: readout_accuracy\\\\n    value: 100%\\\\n  - exp_id: loocv_validation\\\\n    metric: accuracy\\\\n    value: 100% ± 0.00\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C049\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 25/32 attention heads flip to instruction-dominant (58% attention to ~8% of\\\\n    sequence)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: instruction_dominant_heads\\\\n    value: 25/32\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: instruction_attention_fraction\\\\n    value: 58%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C053\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Untrained incidental routing decays to 82%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: untrained_L31_accuracy\\\\n    value: 82%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C058\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSA peaks at L12, probe R² peaks at L8-L13\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_per_layer\\\\n    metric: trained_image_mean_peak\\\\n    value: L12, rho=0.628\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C064\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 highest geometric foundation (rho=0.692)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_encoder_comparison\\\\n    metric: dinov2_cls_rsa\\\\n    value: '0.692'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C071\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Training reshapes readout-token integration (routing +18pp, attention +46pp)\\\\n    rather than visual representations (Delta <= 1.7%)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_summary\\\\n    metric: routing_delta\\\\n    value: +18pp\\\\n  - exp_id: training_effect_summary\\\\n    metric: attention_delta\\\\n    value: +46pp\\\\n  - exp_id: training_effect_summary\\\\n    metric: image_mean_rsa_delta\\\\n    value: '+0.017'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C072\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Image tokens: instruction classification at chance (10%) across all 32 layers'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: image_mean_accuracy\\\\n    value: 10%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C074\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Readout token: 100% instruction identity from L1, LOOCV-verified'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: readout_accuracy\\\\n    value: 100%\\\\n  - exp_id: loocv_validation\\\\n    metric: accuracy\\\\n    value: 100%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C077\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 25/32 heads flip to instruction-dominant (58% attention)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: instruction_dominant_heads\\\\n    value: 25/32\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C081\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Untrained routing decays to 82% by L31\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: untrained_L31_accuracy\\\\n    value: 82%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C086\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 RSA rho=0.692\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_encoder_comparison\\\\n    metric: dinov2_cls_rsa\\\\n    value: '0.692'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C092\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Inverted-U peak rho=0.628 at L12, 0.422 at L32\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_per_layer\\\\n    metric: trained_image_mean_L12\\\\n    value: '0.628'\\\\n  - exp_id: rsa_per_layer\\\\n    metric: trained_image_mean_L32\\\\n    value: '0.422'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C099\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Training geometric gain Delta=0.017-0.023, 3-4%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_comparison\\\\n    metric: rsa_best_vs_best\\\\n    value: +0.017 (Goal), +0.023 (Spatial)\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C107\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Readout R2 Delta=+0.069, p<0.0001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_comparison\\\\n    metric: readout_r2_delta\\\\n    value: '+0.069'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C108\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Image_mean instruction classification at chance (10%) across all 32 layers\\\\n  type: quantitative\\\\n  evidence: 50-demo L1 ablation multi-layer comparison\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C110\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Trained readout 100% L1-L31, LOOCV 100% +/- 0.00\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: readout_accuracy\\\\n    value: 100%\\\\n  - exp_id: loocv_validation\\\\n    metric: accuracy\\\\n    value: 100%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C113\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Untrained readout decays: L8 95.5%, L31 82%'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: untrained_L8\\\\n    value: 95.5%\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: untrained_L31\\\\n    value: 82%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C117\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Instruction invariance: max |Delta| = 0.006'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: factorial_analysis\\\\n    metric: instruction_effect\\\\n    value: '0.006'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C122\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'QA probe: trained 86.3% (L20), DINOv2 82.7%'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: qa_probe\\\\n    metric: trained_accuracy\\\\n    value: 86.3%\\\\n  - exp_id: qa_probe\\\\n    metric: dinov2_accuracy\\\\n    value: 82.7%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C128\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Trained L1: 25/32 heads instruction-dominant, 58% attention to instruction,\\\\n    20.9% to image'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: instruction_dominant_heads\\\\n    value: 25/32\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: instruction_attention\\\\n    value: 58%\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: image_attention\\\\n    value: 20.9%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C135\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Untrained L1: 0/32 heads instruction-dominant, 87.8% image, 11.7% instruction'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: untrained_heads\\\\n    value: 0/32\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: untrained_image_attention\\\\n    value: 87.8%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C143\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Training effect asymmetry: attention +46pp, routing +18pp, R2 +0.069, but\\\\n    image_mean Delta<=1.7%'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_summary\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C152\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 cls RSA rho=0.692, highest alignment\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_encoder_comparison\\\\n    metric: dinov2_cls\\\\n    value: '0.692'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C162\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: CLIP RSA rho=0.557\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_encoder_comparison\\\\n    metric: clip_patch_mean\\\\n    value: '0.557'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C173\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Inverted-U: L0=0.612, L12=0.628, L32=0.422'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_per_layer\\\\n    metric: trained_image_mean\\\\n    value: L0=0.612, L12=0.628, L32=0.422\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C185\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: R2 peak L8-L10 (0.655 +/- 0.002)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_per_layer\\\\n    metric: trained_image_mean_peak\\\\n    value: '0.655'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C198\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Readout R2=0.678 (L13), exceeds projector by 0.048\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_comparison\\\\n    metric: readout_r2\\\\n    value: '0.678'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C212\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSA best-vs-best Delta=+0.017, same-layer +0.079\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_comparison\\\\n    metric: rsa_best_vs_best\\\\n    value: '+0.017'\\\\n  - exp_id: training_effect_comparison\\\\n    metric: same_layer_L12\\\\n    value: '+0.079'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C227\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'R2 best-vs-best: image_mean +0.015 (p=0.006), readout +0.069 (p<0.0001)'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_comparison\\\\n    metric: image_mean_delta\\\\n    value: '+0.015'\\\\n  - exp_id: probe_comparison\\\\n    metric: readout_delta\\\\n    value: '+0.069'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C243\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Untrained pathological: L10-L11 R2=-0.33, -0.28'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_per_layer\\\\n    metric: untrained_L10_L11\\\\n    value: -0.33, -0.28\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C260\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'LIBERO-Spatial: RSA peak L14 (0.691), R2 peak L13 (0.696), Delta=+0.023 p<0.001'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: libero_spatial\\\\n    metric: rsa_peak\\\\n    value: L14, 0.691\\\\n  - exp_id: libero_spatial\\\\n    metric: r2_peak\\\\n    value: L13, 0.696\\\\n  - exp_id: libero_spatial\\\\n    metric: training_delta\\\\n    value: '+0.023'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C278\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Robustness: RSA profile r=0.970 under halved demos'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: demo_sensitivity\\\\n    metric: rsa_profile_correlation\\\\n    value: '0.970'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C279\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Training effects: routing +18pp, attention +46pp, R2 +0.069; image_mean Delta<=1.7%'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_summary\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C281\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Instruction invariance |Delta| < 0.006\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: factorial_analysis\\\\n    metric: instruction_effect\\\\n    value: '0.006'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C284\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LIBERO-Spatial Delta=0.023, p<0.001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: libero_spatial\\\\n    metric: training_delta\\\\n    value: '+0.023'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C285\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Image tokens: instruction classification at chance across all layers'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C287\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Readout token: 100% from L1, LOOCV-verified'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n  - exp_id: loocv_validation\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C290\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 25/32 heads flip to instruction-dominant (58%)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_attention_pattern\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C294\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Untrained decays to 82%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: untrained_L31\\\\n    value: 82%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C299\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSA inverted-U peak L12, R2 L8-L13, DINOv2 rho=0.692\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_per_layer\\\\n  - exp_id: rsa_encoder_comparison\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C305\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Training: R2 +0.069 readout, Delta<=1.7% image_mean'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_summary\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C306\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: image tokens instruction-blind at chance 10% across all layers and conditions\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: accuracy\\\\n    value: 10%\\\\n  decisions:\\\\n  - 'D060: reframed as architecture-expected verification'\\\\n  deprecated: false\\\\n- id: C308\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: readout token 100% instruction classification from L1, cross-validated\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe_loocv\\\\n    metric: accuracy\\\\n    value: 100%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C311\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'VLA training shifts to entry-layer routing L0-L1: 21-25 heads with exit-layer\\\\n    L31: 18 heads'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: attention_analysis\\\\n    metric: instruction_dominant_heads\\\\n    value: 25/32 at L1, 18/32 at L31\\\\n  decisions:\\\\n  - 'D060: C2 anchor claim'\\\\n  deprecated: false\\\\n- id: C315\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: immediate instruction access 99.6% at L1 vs pretrained 80.2%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: L1_accuracy\\\\n    value: 99.6% vs 80.2%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C320\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: under RSA peak rho=0.628 at L12 declining to 0.422 at L32\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_layer_profile\\\\n    metric: spearman_rho\\\\n    value: 0.628 L12, 0.422 L32\\\\n  decisions:\\\\n  - 'D060: qualified with under RSA'\\\\n  deprecated: false\\\\n- id: C326\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 highest geometric alignment rho=0.692, metric-dependent\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_cross_encoder\\\\n    metric: spearman_rho\\\\n    value: '0.692'\\\\n  decisions:\\\\n  - 'D060: added metric-dependence caveat'\\\\n  deprecated: false\\\\n- id: C333\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: training effect Delta rho <= 0.017 non-significant\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_training_effect\\\\n    metric: delta_rho\\\\n    value: '0.017'\\\\n  decisions:\\\\n  - 'D060: marked non-significant'\\\\n  deprecated: false\\\\n- id: C341\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: readout token probe R2 +0.069, instruction attention +46pp\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_training_effect\\\\n    metric: delta_R2\\\\n    value: '+0.069'\\\\n  - exp_id: attention_analysis\\\\n    metric: delta_text_attention\\\\n    value: +46pp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C342\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: image tokens instruction-blind 10% across all 32 layers, architecture-expected\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: accuracy\\\\n    value: 10%\\\\n  decisions:\\\\n  - 'D060: reframed as architecture-expected'\\\\n  deprecated: false\\\\n- id: C344\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: readout token 100% cross-validated from L1\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe_loocv\\\\n    metric: accuracy\\\\n    value: 100%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C347\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'VLA training shifts to entry-exit pattern L0-L1: 21-25 heads, L31: 18 heads'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: attention_analysis\\\\n    metric: instruction_dominant_heads\\\\n  decisions:\\\\n  - 'D060: C2 anchor'\\\\n  deprecated: false\\\\n- id: C351\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 99.6% at L1 vs pretrained 80.2%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: L1_accuracy\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C356\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: under RSA alignment peaks L12 rho=0.628, declines to 0.422 at L32\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_layer_profile\\\\n    metric: spearman_rho\\\\n  decisions:\\\\n  - 'D060: qualified under RSA'\\\\n  deprecated: false\\\\n- id: C362\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 highest geometric alignment rho=0.692, ordering partially reverses\\\\n    under CKA\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_cross_encoder\\\\n    metric: spearman_rho\\\\n    value: '0.692'\\\\n  decisions:\\\\n  - 'D060: CKA caveat added'\\\\n  deprecated: false\\\\n- id: C369\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: non-significant geometric gain Delta rho=0.017 3%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_training_effect\\\\n    metric: delta_rho\\\\n    value: '0.017'\\\\n  decisions:\\\\n  - 'D060: marked non-significant'\\\\n  deprecated: false\\\\n- id: C377\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: readout R2 Delta=+0.069 p<0.0001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_training_effect\\\\n    metric: delta_R2\\\\n    value: '+0.069'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C378\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: image token instruction-blindness consistent with causal mask and frozen encoder\\\\n  type: mechanistic\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: accuracy\\\\n    value: 10%\\\\n  decisions:\\\\n  - 'D060: acknowledge causal mask as structural source'\\\\n  deprecated: false\\\\n- id: C379\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 highest RSA alignment 0.692, metric-dependent ordering\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_cross_encoder\\\\n    metric: spearman_rho\\\\n    value: '0.692'\\\\n  decisions:\\\\n  - 'D060: added under RSA qualifier and CKA metric-dependence caveat'\\\\n  deprecated: false\\\\n- id: C380\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: best-vs-best RSA gain non-significant Delta=+0.017 3% CI includes zero\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_training_effect\\\\n    metric: delta_rho_best_vs_best\\\\n    value: '+0.017'\\\\n  decisions:\\\\n  - 'D060: marked non-significant, CI includes zero'\\\\n  deprecated: false\\\\n- id: C381\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: image tokens instruction-blind consistent with causal mask and frozen encoder\\\\n  type: mechanistic\\\\n  evidence: 50-demo L1 ablation control\\\\n  decisions:\\\\n  - 'D060: architecture-expected framing'\\\\n  deprecated: false\\\\n- id: C383\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: training effects concentrated at readout R2 +0.069\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_training_effect\\\\n    metric: delta_R2\\\\n    value: '+0.069'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C386\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 highest RSA rho=0.692 under RSA\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_cross_encoder\\\\n    metric: spearman_rho\\\\n    value: '0.692'\\\\n  decisions:\\\\n  - 'D060: qualified under RSA'\\\\n  deprecated: false\\\\n- id: C390\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: VLA readout R2=0.678 vs DINOv2 0.634\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_comparison\\\\n    metric: R2\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C395\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: ablation R2 +46% p<0.0001 deep layers unaffected\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_ablation\\\\n    metric: delta_R2\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C401\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: encoder ranking reverses under CKA, metric-dependent\\\\n  type: qualitative\\\\n  evidence:\\\\n  - exp_id: cka_comparison\\\\n  decisions:\\\\n  - 'D060: CKA divergence in main text'\\\\n  deprecated: false\\\\n- id: C408\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: frozen encoder confound acknowledged\\\\n  type: qualitative\\\\n  evidence: []\\\\n  decisions:\\\\n  - 'D060: added frozen encoder caveat'\\\\n  deprecated: false\\\\n- id: C416\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: L1 ablation 5 demos per task, full-scale replication in progress\\\\n  type: qualitative\\\\n  evidence: []\\\\n  decisions:\\\\n  - 'D060: acknowledged ablation scale limitation'\\\\n  deprecated: false\\\\n- id: C417\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: functional probes R2 peak L8-L13 metric-independent non-monotonic trajectory\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_layer_profile\\\\n    metric: R2\\\\n    value: 0.655-0.678 at L8-L13\\\\n  decisions:\\\\n  - 'D060-C3-fix: R2 as primary metric-independent evidence'\\\\n  deprecated: false\\\\n- id: C418\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSA per-layer profile and encoder rankings metric-dependent, CKA monotonically\\\\n    increasing\\\\n  type: qualitative\\\\n  evidence:\\\\n  - exp_id: cka_comparison\\\\n  decisions:\\\\n  - 'D060-C3-fix: decline phase also RSA-specific, CKA monotonic'\\\\n  deprecated: false\\\\n- id: C419\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: functional probes peak L8-L13 R2=0.655-0.678 metric-independent\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_layer_profile\\\\n    metric: R2\\\\n  decisions:\\\\n  - 'D060-C3-fix: R2 as primary'\\\\n  deprecated: false\\\\n- id: C420\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: CKA monotonically increasing layer profiles\\\\n  type: qualitative\\\\n  evidence:\\\\n  - exp_id: cka_layer_profile\\\\n  decisions:\\\\n  - 'D060-C3-fix: decline also RSA-specific'\\\\n  deprecated: false\\\\n- id: C421\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'C3 contribution: non-monotonic transformation, R2 confirmed, RSA confirms\\\\n    but CKA diverges'\\\\n  type: qualitative\\\\n  evidence:\\\\n  - exp_id: probe_layer_profile\\\\n  - exp_id: rsa_layer_profile\\\\n  - exp_id: cka_layer_profile\\\\n  decisions:\\\\n  - 'D060-C3-fix: balanced metric framing'\\\\n  deprecated: false\\\\n- id: C422\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: encoder rankings and per-layer profiles metric-dependent, R2 inverted-U metric-independent\\\\n  type: qualitative\\\\n  evidence:\\\\n  - exp_id: cka_comparison\\\\n  - exp_id: probe_layer_profile\\\\n  decisions:\\\\n  - 'D060-C3-fix: CKA divergence covers both rankings and profiles'\\\\n  deprecated: false\\\\n- id: C423\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: trained image_mean RSA stable L0-L12 Delta=+0.017 n.s., decline L12-L32 Delta=-0.206\\\\n    p<0.0001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_layer_profile\\\\n    metric: spearman_rho\\\\n  decisions:\\\\n  - 'D060-C3-fix: rise phase reframed as stable'\\\\n  deprecated: false\\\\n- id: C424\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: untrained RSA declines monotonically from L0 Delta=-0.062 to L12 p<0.0001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_layer_profile_untrained\\\\n    metric: spearman_rho\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C425\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: marginal RSA change at image_mean +0.017 n.s. contrasts with readout +0.074\\\\n    p<0.0001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_layer_profile\\\\n    metric: delta_rho_readout\\\\n  decisions:\\\\n  - 'D060-C3-fix: readout contrast added'\\\\n  deprecated: false\\\\n- id: C426\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: N=63728 observations, N/params ratio approx 0.05 for MLP probe\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: dataset_stats\\\\n    metric: N_observations\\\\n    value: '63728'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C427\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Probe R2 trained vs untrained FDR significant at 29-30/33 layers both positions\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: fdr_correction\\\\n    metric: significant_layers_R2\\\\n    value: 29-30/33\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C428\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSA FDR significant at 25/33 layers image_mean, 0/33 last_preaction due to\\\\n    n=10 power ceiling\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: fdr_correction\\\\n    metric: significant_layers_RSA\\\\n    value: 25/33 image_mean, 0/33 readout\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C429\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: non-monotonic profile stable under 25-demo subsampling, RSA peak unchanged\\\\n    L12, profile r=0.97\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: ablation_p2_demo_sensitivity\\\\n    metric: profile_correlation_RSA\\\\n    value: '0.970'\\\\n  decisions: []\\\\n  deprecated: false\\\\nfigures:\\\\n- caption: Three similarity metrics across representation sources. \\\\\\\\textbf{(a)\\\\n  deprecated: false\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines (RSA values)\\\\n    tier: tier1\\\\n  - exp_id: plan_009_cka_verification\\\\n    metric: linear_cka + rdm_cka\\\\n    tier: tier1\\\\n  id: F001\\\\n  label: fig:metric_comparison\\\\n  location:\\\\n    section: appendix\\\\n  source_path: figures/fig6.pdf\\\\n  type: result\\\\n- caption: RSA with the action space ($\\\\\\\\rho$) across representation sources. Self-supervised\\\\n    DINOv2 \\\\\\\\texttt{cls\\\\\\\\_token\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines + trained/untrained peaks\\\\n    tier: tier1\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: fused_2176d_rsa=0.634\\\\n    tier: tier1\\\\n  id: F002\\\\n  label: fig:rsa_bar\\\\n  location:\\\\n    section: experiments\\\\n  source_path: figures/fig2.pdf\\\\n  type: result\\\\n- caption: 'Per-layer RSA ($\\\\\\\\rho$) with the action space across all 32 LLM layers.\\\\n    Trained image\\\\\\\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\\\\\\\to$ L12 $=\\\\n    0.628$ (peak, above Projector $0.615$) $\\\\\\\\to$ L32 $= 0.422$. Untrained image\\\\\\\\_mean\\\\n    (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2\\\\n    cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).'\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: per-layer RSA trained/untrained image_mean (32 layers)\\\\n    tier: tier1\\\\n  id: F003\\\\n  label: fig:layer_curves\\\\n  location:\\\\n    section: experiments\\\\n  source_path: figures/fig3.pdf\\\\n  type: result\\\\n- caption: Functional probe $R^2$ for action prediction (best layer for each source).\\\\n    Both trained readout ($R^2{=\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: peak R2 values (trained img_mean L8, readout L13)\\\\n    tier: tier1\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: projector/dino/clip R2\\\\n    tier: tier1\\\\n  id: F004\\\\n  label: fig:probe_bars\\\\n  location:\\\\n    section: experiments\\\\n  source_path: figures/fig4.pdf\\\\n  type: result\\\\n- caption: \\\\\\\\textbf{(a)\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained vs untrained per-layer RSA + instruction conditions\\\\n    tier: tier1\\\\n  - exp_id: plan_008_random_inst_control\\\\n    metric: instruction invariance\\\\n    tier: tier1\\\\n  id: F005\\\\n  label: fig:factorial\\\\n  location:\\\\n    section: experiments\\\\n  source_path: figures/fig5.pdf\\\\n  type: result\\\\n- id: F006\\\\n  location:\\\\n    section: appendix\\\\n    figure_number: 0\\\\n  caption: ''\\\\n  type: other\\\\n  source: {}\\\\n  output_path: ''\\\\n  deprecated: false\\\\n- id: F007\\\\n  location:\\\\n    section: appendix\\\\n    figure_number: 0\\\\n  caption: ''\\\\n  type: other\\\\n  source: {}\\\\n  output_path: ''\\\\n  deprecated: false\\\\npaper:\\\\n  generated_at: '2026-05-17T22:15:14.113705+00:00'\\\\n  source: auto-bootstrap from existing tex files\\\\n  title: Formatting Instructions for CoRL 2026 Camera-Ready\\\\n  version: 51\\\\ntables:\\\\n- caption: Geometric (RSA $\\\\\\\\rho$) and functional (probe $R^2$) alignment with the\\\\n    action space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both\\\\n    trained readout and image\\\\\\\\_mean exceed the projector in $R^2$, confirming the\\\\n    inverted-U extends to functional capacity. VLA rows show peak-layer values (RSA/R$^2$\\\\n    peaks listed separately when they differ). 95\\\\\\\\% CIs from 10{,\\\\n  cells: []\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: all RSA peaks + baselines\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: all R2 peaks\\\\n    tier: tier1\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: projector/dino/clip R2\\\\n    tier: tier1\\\\n  id: T001\\\\n  label: tab:rsa_overview\\\\n  location:\\\\n    section: experiments\\\\n- caption: Training effects on action-relevant structure (bootstrap, 10{,\\\\n  cells: []\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best + same_layer comparisons\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best R2\\\\n    tier: tier1\\\\n  id: T002\\\\n  label: tab:training_effects\\\\n  location:\\\\n    section: experiments\\\\n_completeness:\\\\n  coverage: 69/74\\\\n  claims: 71\\\\n  tables: 0\\\\n  figures: 3\\\\n  tier_counts:\\\\n    tier1: 0\\\\n    tier2: 69\\\\n    tier3: 5\\\\n    tierX: 0\\\\n  last_checked: '2026-05-17T22:15:14.113771+00:00'\\\\n\\\", \\\"total_chars\\\": 51898, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml\", \"content\": \"claims:\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915\\n    tier: tier1\\n  - exp_id: plan_013_branch_split\\n    metric: post_projector_4096d_rsa=0.615\\n    tier: tier1\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.clip_cls=0.557\\n    tier: tier1\\n  id: C001\\n  location:\\n    context: result_statement\\n    section: abstract\\n  text: 'First, self-supervised pretraining provides the strongest action-relevant\\n    geometry: standalone DINOv2 achieves RSA $ = 0.692$, exceeding all VL-pretrained\\n    encoders (DinoSigLIP+Projector $ = 0.615$; CL'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_image_mean_peak.rsa=0.6282\\n    tier: tier1\\n  - exp_id: d041_method_b_rsa\\n    metric: untrained_image_mean_peak.rsa=0.6117\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\n    tier: tier1\\n  id: C002\\n  location:\\n    context: result_statement\\n    section: abstract\\n  text: 'Second, the LLM applies a non-monotonic transformation---the first 12 layers\\n    enhance geometric alignment with the action space above the vision encoder input\\n    ($$: $0.612  0.628$ at L12), while the rem'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017,significant=false\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686,p=0.0001\\n    tier: tier1\\n  id: C003\\n  location:\\n    context: result_statement\\n    section: abstract\\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\\n    capacity (R^2 Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates\\n  type: quantitative\\n- deprecated: false\\n  evidence: llama2base_action_probe experiment\\n  id: C004\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: 'Linear CKA~kornblith2019 reverses the RSA ordering: untrained LLM ($CKA =\\n    0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2\\n    ($0.066$), partially inverting the self-superv'\\n  type: quantitative\\n  decisions: []\\n- deprecated: false\\n  evidence:\\n  - exp_id: plan_009_cka_verification\\n    metric: rdm_cka.*\\n    tier: tier1\\n  id: C005\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: 'RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $$\\n    Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).'\\n  type: quantitative\\n- deprecated: false\\n  evidence:\\n  - exp_id: plan_009_cka_verification\\n    metric: linear_cka per-layer (derived from full scan)\\n    tier: tier2\\n  id: C006\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: At the per-layer level, linear CKA between image\\\\_mean and the action space\\n    rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U\\n    pattern.\\n  type: quantitative\\n- deprecated: false\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.*\\n    tier: tier1\\n  - exp_id: plan_009_cka_verification\\n    metric: linear_cka.* + rdm_cka.*\\n    tier: tier1\\n  id: C007\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: 'Three similarity metrics across representation sources. (a)~RSA ranks DINOv2\\n    cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). (b)~Linear CKA reverses\\n    the ordering: Untrained ($0.089$) $>$ Tr'\\n  type: quantitative\\n- deprecated: false\\n  evidence:\\n  - exp_id: plan_013_branch_split\\n    metric: fused_2176d_rsa=0.634\\n    tier: tier1\\n  id: C008\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: Fusion produces a representation ($ = 0.634$) that exceeds either branch alone,\\n    indicating that concatenation captures complementary structure.\\n  type: quantitative\\n- deprecated: false\\n  evidence:\\n  - exp_id: plan_013_branch_split\\n    metric: fused_2176d_rsa=0.634, post_projector_4096d_rsa=0.615\\n    tier: tier1\\n  id: C009\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: 'The MLP projector then compresses this signal: DinoSigLIP+Projector achieves\\n    $ = 0.615$, a drop of $ = 0.019$ from the fused 2{,176-D input.'\\n  type: quantitative\\n- deprecated: false\\n  evidence:\\n  - exp_id: plan_013_branch_split\\n    metric: standalone_dino_patch_mean_rsa=0.631\\n    tier: tier1\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_patch_mean=0.6307\\n    tier: tier1\\n  id: C010\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: DINOv2 patch\\\\_mean achieves RSA $ = 0.631$, between the cls\\\\_token ($0.692$)\\n    and the fused DinoSigLIP ($0.634$).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915, trained_image_mean_peak\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\n    tier: tier1\\n  id: C011\\n  location:\\n    context: result_statement\\n    section: conclusion\\n  text: 'Three findings emerge: (1)~the frozen vision encoder provides the dominant\\n    action-relevant geometry, with self-supervised DINOv2 achieving the highest alignment\\n    ($ = 0.692$) exceeding all VL-pretraine'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915\\n    tier: tier1\\n  id: C012\\n  location:\\n    context: result_statement\\n    section: discussion\\n  text: 'The vision encoder is the source: self-supervised DINOv2 achieves the highest\\n    geometric alignment ($ = 0.692$), exceeding all VLA internal representations.'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.p=0.006\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686\\n    tier: tier1\\n  id: C013\\n  location:\\n    context: result_statement\\n    section: discussion\\n  text: 'Training redistributes geometry but enhances decodability: modest geometric\\n    gain (Delta = 0.017--0.023, 3--4% of baseline across two benchmarks), while substantially\\n    improving R^2 (Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.significant=false\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  id: C014\\n  location:\\n    context: result_statement\\n    section: discussion\\n  text: Cross-benchmark replication (LIBERO-Spatial Delta = 0.023, p < 0.001) suggests\\n    the LIBERO-Goal RSA CI (incl. zero) reflects limited power rather than a true\\n    null, but the effect remains small (3--4% of baseline).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915\\n    tier: tier1\\n  - exp_id: plan_013_branch_split\\n    metric: fused_2176d_rsa=0.634, standalone_dino_patch_mean_rsa=0.631\\n    tier: tier1\\n  id: C015\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: The standalone DINOv2 cls\\\\_token achieves the highest alignment of any representation\\n    source ($ = 0.692$), followed by the fused DinoSigLIP 2{,176-D representation\\n    before projection ($ = 0.634$) and t\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.clip_cls=0.557\\n    tier: tier1\\n  id: C016\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: CLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment\\n    among pretrained encoders ($ = 0.557$; Figure~fig:rsa_bar).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557, trained_image_mean_peak.rsa=0.6282\\n    tier: tier1\\n  id: C017\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: DINOv2, pretrained with self-supervised objectives alone, achieves $ = 0.692$---exceeding\\n    not only CLIP ($ = 0.557$) but also the VLA's own internal representations at\\n    their peaks (trained image\\\\_mean\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_012_clip_vit_control\\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\\n    tier: tier1\\n  - exp_id: unified_action_probe\\n    metric: bootstrap_pairwise.projector_vs_dino.p=0.557\\n    tier: tier1\\n  id: C018\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'Functional probes corroborate the ranking: DINOv2 cls\\\\_token achieves $R^2\\n    = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$,\\n    $p = 0.557$, n.s.), while CLIP yields the'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_013_branch_split\\n    metric: dinov2_branch_rsa=0.619, siglip_branch_rsa=0.621\\n    tier: tier1\\n  id: C019\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: The DINOv2 (1{,024-D) and SigLIP (1{,152-D) branches yield near-identical\\n    RSA ($0.619$ vs.\\\\ $0.621$); fusion exceeds either ($0.634$), while the projector\\n    introduces modest compression loss ($0.634  0\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: all RSA values\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: all R2 peak values\\n    tier: tier1\\n  id: C020\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Geometric (RSA $$) and functional (probe $R^2$) alignment with the action\\n    space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both trained\\n    readout and image\\\\_mean exceed the projector in\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines + trained_image_mean_peak\\n    tier: tier1\\n  id: C021\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'RSA with the action space ($$) across representation sources. Self-supervised\\n    DINOv2 cls\\\\_token ($=0.692$) achieves the highest geometric alignment, followed\\n    by fused DinoSigLIP ($0.634$) and the VLA '\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_image_mean per-layer RSA (L0=0.612, L12=0.628, L32=0.422)\\n    tier: tier1\\n  id: C022\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'Figure~fig:layer_curves reveals a non-monotonic trajectory for trained image\\\\_mean\\n    RSA: $$ begins at $0.612$ (L0, equal to the projector input), rises to a peak\\n    of $0.628$ at L12---above the DinoSigLI'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_image_mean_peak.layer=8, mean_R2=0.6553\\n    tier: tier1\\n  - exp_id: plan_012_clip_vit_control\\n    metric: projector_mean_R2=0.6298\\n    tier: tier1\\n  id: C023\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Full-layer probe scans reveal that trained image\\\\_mean $R^2$ peaks at L8 ($0.655$),\\n    exceeding the projector ($0.630$, $ = +0.025$; Table~tab:rsa_overview).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_image_mean_peak.layer=8\\n    tier: tier1\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_image_mean_peak.layer=12\\n    tier: tier1\\n  id: C024\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: The $R^2$ peak (L8) precedes the RSA peak (L12) by four layers, suggesting\\n    that functional decodability peaks earlier than geometric alignment; we adopt\\n    ``early-to-middle layers (L8--L13)'' to capture\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_last_preaction_peak.rsa=0.6425, layer=12\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak.mean_R2=0.6779, layer=13\\n    tier: tier1\\n  id: C025\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Trained readout achieves peak RSA $ = 0.643$ at L12 and probe $R^2 = 0.678$\\n    (L13), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $ = 0.048$; Table~tab:rsa_overview,\\n    Figure~fig:probe_bars).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained per-layer RSA L12=0.628→L32=0.422; untrained 0.612→0.545\\n    tier: tier1\\n  id: C026\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'The decline from L12 to L32 ($$: $0.628  0.422$) exceeds the untrained decay\\n    ($0.612  0.545$), indicating that training actively redirects later layers away\\n    from action geometry, yielding a three-phas'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak=0.6779, trained_image_mean_peak=0.6553\\n    tier: tier1\\n  - exp_id: plan_012_clip_vit_control\\n    metric: projector_mean_R2=0.6298, dino_cls_mean_R2=0.6343\\n    tier: tier1\\n  id: C027\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Functional probe $R^2$ for action prediction (best layer for each source).\\n    Both trained readout ($R^2{=0.678$, L13) and trained image\\\\_mean ($0.655$, L8)\\n    exceed the projector baseline ($0.630$), confi\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  id: C028\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: best-vs-best Delta = +0.017 (3% of baseline; LIBERO-Spatial confirms with\\n    Delta = +0.023, 4%, p < 0.001). This geometric gain is far smaller than the functional\\n    improvement.\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\n    tier: tier1\\n  id: C029\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: RSA best-vs-best yields at most a modest gain (Delta = 0.017--0.023, 3--4%\\n    of baseline across two benchmarks), while R^2 shows substantially larger improvements.\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006; last_preaction.delta=0.0686,p=0.0001\\n    tier: tier1\\n  id: C030\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Yet $R^2$ best-vs-best is significant for both image\\\\_mean ($ = +0.015$, $p\\n    = 0.006$) and readout ($ = +0.069$, $p < 0.0001$; Table~tab:training_effects).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_same_layer.last_preaction_L13.note (untrained L13 R2 near -0.33)\\n    tier: tier1\\n  id: C031\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Untrained readout $R^2$ reaches $ -0.33$ at L12--L29 (predictions worse than\\n    a constant-mean baseline), while untrained image\\\\_mean $R^2$ drops to near-zero\\n    at L10--L13.\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best + same_layer\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best\\n    tier: tier1\\n  id: C032\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'Training effects on action-relevant structure (LIBERO-Goal; bootstrap). RSA\\n    best-vs-best yields modest geometric gain (Delta=+0.017, 3%; LIBERO-Spatial: +0.023,\\n    p<0.001), while R^2 shows substantially larger functional gains.'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: instruction_effect (derived from trained_with_inst vs trained_no_inst)\\n    tier: tier1\\n  - exp_id: plan_008_random_inst_control\\n    metric: max_absolute_delta=0.0165, instruction_invariant=true\\n    tier: tier1\\n  id: C033\\n  location:\\n    context: finding_statement\\n    section: experiments\\n  text: This confirms that the action geometry is visually grounded and instruction-independent~grant2026.\\n  type: methodological\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: experimental design (2x2 factorial)\\n    tier: tier2\\n  id: C034\\n  location:\\n    context: result_statement\\n    section: introduction\\n  text: We cross training status (trained vs.\\\\ untrained, reinitializing 6.74B LLM\\n    parameters) with instruction presence in a $2 2$ factorial design, and quantify\\n    action-relevant structure using RSA~kriegesko\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557\\n    tier: tier1\\n  id: C035\\n  location:\\n    context: result_statement\\n    section: introduction\\n  text: Standalone DINOv2 achieves the highest action-space alignment (RSA $ = 0.692$),\\n    far exceeding CLIP ($ = 0.557$) and the VLA's own peak internal representation\\n    ($ = 0.628$ at L12).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_012_clip_vit_control\\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\\n    tier: tier1\\n  id: C036\\n  location:\\n    context: result_statement\\n    section: introduction\\n  text: 'Functional probes corroborate this ranking: DINOv2 ($R^2 = 0.634$) $$ Projector\\n    ($0.630$) $>$ CLIP ($0.587$).'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_image_mean_peak.rsa=0.6282\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\n    tier: tier1\\n  id: C037\\n  location:\\n    context: result_statement\\n    section: introduction\\n  text: 'Second, the LLM applies a non-monotonic transformation: the first 12 layers\\n    enhance geometric alignment above the vision encoder input ($$: $0.612  0.628$),\\n    while the remaining 20 layers degrade it ($'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_013_branch_split\\n    metric: methodology (encoder extraction)\\n    tier: tier2\\n  id: C038\\n  location:\\n    context: bold\\n    section: method\\n  text: DINOv2 ViT-L/14\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_012_clip_vit_control\\n    metric: methodology (CLIP extraction)\\n    tier: tier2\\n  id: C039\\n  location:\\n    context: bold\\n    section: method\\n  text: CLIP ViT-L/14\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\n    tier: tier1\\n  id: C040\\n  location:\\n    context: result_statement\\n    section: introduction\\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\\n    capacity---redistribution dominates over creation.\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_010_libero_spatial\\n    metric: rsa.trained_image_mean_peak(layer=14,rsa=0.691), action_probe.trained_image_mean_peak(layer=13,R2=0.696)\\n    tier: tier1\\n  id: C041\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'Cross-benchmark validation (LIBERO-Spatial): inverted-U replicates, trained\\n    image_mean RSA peaks at L14 (rho=0.691), R^2 at L13 (0.696), peak shifting ~2\\n    layers deeper than LIBERO-Goal.'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,ci_95=[0.012,0.036],p=0.001\\n    tier: tier1\\n  id: C042\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Training produces a significant geometric gain on LIBERO-Spatial (best-vs-best\\n    Delta=+0.023, p<0.001), confirming LIBERO-Goal effect reflects limited power.\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_010_libero_spatial\\n    metric: rsa.trained_last_preaction_peak(layer=15), action_probe.trained_last_preaction_peak(layer=21)\\n    tier: tier1\\n  id: C043\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: RSA--R^2 peak convergence does not replicate on LIBERO-Spatial (RSA L15 vs\\n    R^2 L21, 6-layer gap vs 1 on Goal), suggesting peak alignment may be benchmark-specific.\\n  type: quantitative\\n- id: C044\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Image tokens encode purely visual information (instruction classification\\n    at chance, 10%, across all layers)\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: image_mean_accuracy\\n    value: 10%\\n  decisions: []\\n  deprecated: true\\n- id: C046\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Readout token: 100% instruction classification from L1, LOOCV-verified'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: readout_accuracy\\n    value: 100%\\n  - exp_id: loocv_validation\\n    metric: accuracy\\n    value: 100% ± 0.00\\n  decisions: []\\n  deprecated: true\\n- id: C049\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 25/32 attention heads flip to instruction-dominant (58% attention to ~8% of\\n    sequence)\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_attention_pattern\\n    metric: instruction_dominant_heads\\n    value: 25/32\\n  - exp_id: l1_attention_pattern\\n    metric: instruction_attention_fraction\\n    value: 58%\\n  decisions: []\\n  deprecated: true\\n- id: C053\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Untrained incidental routing decays to 82%\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: untrained_L31_accuracy\\n    value: 82%\\n  decisions: []\\n  deprecated: true\\n- id: C058\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: RSA peaks at L12, probe R² peaks at L8-L13\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_per_layer\\n    metric: trained_image_mean_peak\\n    value: L12, rho=0.628\\n  decisions: []\\n  deprecated: true\\n- id: C064\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 highest geometric foundation (rho=0.692)\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_encoder_comparison\\n    metric: dinov2_cls_rsa\\n    value: '0.692'\\n  decisions: []\\n  deprecated: true\\n- id: C071\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Training reshapes readout-token integration (routing +18pp, attention +46pp)\\n    rather than visual representations (Delta <= 1.7%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_summary\\n    metric: routing_delta\\n    value: +18pp\\n  - exp_id: training_effect_summary\\n    metric: attention_delta\\n    value: +46pp\\n  - exp_id: training_effect_summary\\n    metric: image_mean_rsa_delta\\n    value: '+0.017'\\n  decisions: []\\n  deprecated: true\\n- id: C072\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Image tokens: instruction classification at chance (10%) across all 32 layers'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: image_mean_accuracy\\n    value: 10%\\n  decisions: []\\n  deprecated: true\\n- id: C074\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Readout token: 100% instruction identity from L1, LOOCV-verified'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: readout_accuracy\\n    value: 100%\\n  - exp_id: loocv_validation\\n    metric: accuracy\\n    value: 100%\\n  decisions: []\\n  deprecated: true\\n- id: C077\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 25/32 heads flip to instruction-dominant (58% attention)\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_attention_pattern\\n    metric: instruction_dominant_heads\\n    value: 25/32\\n  decisions: []\\n  deprecated: true\\n- id: C081\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Untrained routing decays to 82% by L31\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: untrained_L31_accuracy\\n    value: 82%\\n  decisions: []\\n  deprecated: true\\n- id: C086\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 RSA rho=0.692\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_encoder_comparison\\n    metric: dinov2_cls_rsa\\n    value: '0.692'\\n  decisions: []\\n  deprecated: true\\n- id: C092\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Inverted-U peak rho=0.628 at L12, 0.422 at L32\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_per_layer\\n    metric: trained_image_mean_L12\\n    value: '0.628'\\n  - exp_id: rsa_per_layer\\n    metric: trained_image_mean_L32\\n    value: '0.422'\\n  decisions: []\\n  deprecated: true\\n- id: C099\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Training geometric gain Delta=0.017-0.023, 3-4%\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_comparison\\n    metric: rsa_best_vs_best\\n    value: +0.017 (Goal), +0.023 (Spatial)\\n  decisions: []\\n  deprecated: true\\n- id: C107\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Readout R2 Delta=+0.069, p<0.0001\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_comparison\\n    metric: readout_r2_delta\\n    value: '+0.069'\\n  decisions: []\\n  deprecated: true\\n- id: C108\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: Image_mean instruction classification at chance (10%) across all 32 layers\\n  type: quantitative\\n  evidence: 50-demo L1 ablation multi-layer comparison\\n  decisions: []\\n  deprecated: false\\n- id: C110\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: Trained readout 100% L1-L31, LOOCV 100% +/- 0.00\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: readout_accuracy\\n    value: 100%\\n  - exp_id: loocv_validation\\n    metric: accuracy\\n    value: 100%\\n  decisions: []\\n  deprecated: false\\n- id: C113\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Untrained readout decays: L8 95.5%, L31 82%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: untrained_L8\\n    value: 95.5%\\n  - exp_id: cross_instruction_probe\\n    metric: untrained_L31\\n    value: 82%\\n  decisions: []\\n  deprecated: false\\n- id: C117\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Instruction invariance: max |Delta| = 0.006'\\n  type: quantitative\\n  evidence:\\n  - exp_id: factorial_analysis\\n    metric: instruction_effect\\n    value: '0.006'\\n  decisions: []\\n  deprecated: false\\n- id: C122\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'QA probe: trained 86.3% (L20), DINOv2 82.7%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: qa_probe\\n    metric: trained_accuracy\\n    value: 86.3%\\n  - exp_id: qa_probe\\n    metric: dinov2_accuracy\\n    value: 82.7%\\n  decisions: []\\n  deprecated: false\\n- id: C128\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Trained L1: 25/32 heads instruction-dominant, 58% attention to instruction,\\n    20.9% to image'\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_attention_pattern\\n    metric: instruction_dominant_heads\\n    value: 25/32\\n  - exp_id: l1_attention_pattern\\n    metric: instruction_attention\\n    value: 58%\\n  - exp_id: l1_attention_pattern\\n    metric: image_attention\\n    value: 20.9%\\n  decisions: []\\n  deprecated: false\\n- id: C135\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Untrained L1: 0/32 heads instruction-dominant, 87.8% image, 11.7% instruction'\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_attention_pattern\\n    metric: untrained_heads\\n    value: 0/32\\n  - exp_id: l1_attention_pattern\\n    metric: untrained_image_attention\\n    value: 87.8%\\n  decisions: []\\n  deprecated: false\\n- id: C143\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Training effect asymmetry: attention +46pp, routing +18pp, R2 +0.069, but\\n    image_mean Delta<=1.7%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_summary\\n  decisions: []\\n  deprecated: false\\n- id: C152\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 cls RSA rho=0.692, highest alignment\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_encoder_comparison\\n    metric: dinov2_cls\\n    value: '0.692'\\n  decisions: []\\n  deprecated: false\\n- id: C162\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: CLIP RSA rho=0.557\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_encoder_comparison\\n    metric: clip_patch_mean\\n    value: '0.557'\\n  decisions: []\\n  deprecated: false\\n- id: C173\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Inverted-U: L0=0.612, L12=0.628, L32=0.422'\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_per_layer\\n    metric: trained_image_mean\\n    value: L0=0.612, L12=0.628, L32=0.422\\n  decisions: []\\n  deprecated: false\\n- id: C185\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: R2 peak L8-L10 (0.655 +/- 0.002)\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_per_layer\\n    metric: trained_image_mean_peak\\n    value: '0.655'\\n  decisions: []\\n  deprecated: false\\n- id: C198\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: Readout R2=0.678 (L13), exceeds projector by 0.048\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_comparison\\n    metric: readout_r2\\n    value: '0.678'\\n  decisions: []\\n  deprecated: false\\n- id: C212\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: RSA best-vs-best Delta=+0.017, same-layer +0.079\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_comparison\\n    metric: rsa_best_vs_best\\n    value: '+0.017'\\n  - exp_id: training_effect_comparison\\n    metric: same_layer_L12\\n    value: '+0.079'\\n  decisions: []\\n  deprecated: false\\n- id: C227\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'R2 best-vs-best: image_mean +0.015 (p=0.006), readout +0.069 (p<0.0001)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_comparison\\n    metric: image_mean_delta\\n    value: '+0.015'\\n  - exp_id: probe_comparison\\n    metric: readout_delta\\n    value: '+0.069'\\n  decisions: []\\n  deprecated: false\\n- id: C243\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Untrained pathological: L10-L11 R2=-0.33, -0.28'\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_per_layer\\n    metric: untrained_L10_L11\\n    value: -0.33, -0.28\\n  decisions: []\\n  deprecated: false\\n- id: C260\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'LIBERO-Spatial: RSA peak L14 (0.691), R2 peak L13 (0.696), Delta=+0.023 p<0.001'\\n  type: quantitative\\n  evidence:\\n  - exp_id: libero_spatial\\n    metric: rsa_peak\\n    value: L14, 0.691\\n  - exp_id: libero_spatial\\n    metric: r2_peak\\n    value: L13, 0.696\\n  - exp_id: libero_spatial\\n    metric: training_delta\\n    value: '+0.023'\\n  decisions: []\\n  deprecated: false\\n- id: C278\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Robustness: RSA profile r=0.970 under halved demos'\\n  type: quantitative\\n  evidence:\\n  - exp_id: demo_sensitivity\\n    metric: rsa_profile_correlation\\n    value: '0.970'\\n  decisions: []\\n  deprecated: false\\n- id: C279\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Training effects: routing +18pp, attention +46pp, R2 +0.069; image_mean Delta<=1.7%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_summary\\n  decisions: []\\n  deprecated: true\\n- id: C281\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Instruction invariance |Delta| < 0.006\\n  type: quantitative\\n  evidence:\\n  - exp_id: factorial_analysis\\n    metric: instruction_effect\\n    value: '0.006'\\n  decisions: []\\n  deprecated: true\\n- id: C284\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: LIBERO-Spatial Delta=0.023, p<0.001\\n  type: quantitative\\n  evidence:\\n  - exp_id: libero_spatial\\n    metric: training_delta\\n    value: '+0.023'\\n  decisions: []\\n  deprecated: true\\n- id: C285\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Image tokens: instruction classification at chance across all layers'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n  decisions: []\\n  deprecated: false\\n- id: C287\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Readout token: 100% from L1, LOOCV-verified'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n  - exp_id: loocv_validation\\n  decisions: []\\n  deprecated: false\\n- id: C290\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: 25/32 heads flip to instruction-dominant (58%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_attention_pattern\\n  decisions: []\\n  deprecated: false\\n- id: C294\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Untrained decays to 82%\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: untrained_L31\\n    value: 82%\\n  decisions: []\\n  deprecated: false\\n- id: C299\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: RSA inverted-U peak L12, R2 L8-L13, DINOv2 rho=0.692\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_per_layer\\n  - exp_id: rsa_encoder_comparison\\n  decisions: []\\n  deprecated: false\\n- id: C305\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Training: R2 +0.069 readout, Delta<=1.7% image_mean'\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_summary\\n  decisions: []\\n  deprecated: false\\n- id: C306\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: image tokens instruction-blind at chance 10% across all layers and conditions\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: accuracy\\n    value: 10%\\n  decisions:\\n  - 'D060: reframed as architecture-expected verification'\\n  deprecated: false\\n- id: C308\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: readout token 100% instruction classification from L1, cross-validated\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe_loocv\\n    metric: accuracy\\n    value: 100%\\n  decisions: []\\n  deprecated: false\\n- id: C311\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'VLA training shifts to entry-layer routing L0-L1: 21-25 heads with exit-layer\\n    L31: 18 heads'\\n  type: quantitative\\n  evidence:\\n  - exp_id: attention_analysis\\n    metric: instruction_dominant_heads\\n    value: 25/32 at L1, 18/32 at L31\\n  decisions:\\n  - 'D060: C2 anchor claim'\\n  deprecated: false\\n- id: C315\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: immediate instruction access 99.6% at L1 vs pretrained 80.2%\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: L1_accuracy\\n    value: 99.6% vs 80.2%\\n  decisions: []\\n  deprecated: false\\n- id: C320\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: under RSA peak rho=0.628 at L12 declining to 0.422 at L32\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_layer_profile\\n    metric: spearman_rho\\n    value: 0.628 L12, 0.422 L32\\n  decisions:\\n  - 'D060: qualified with under RSA'\\n  deprecated: false\\n- id: C326\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 highest geometric alignment rho=0.692, metric-dependent\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_cross_encoder\\n    metric: spearman_rho\\n    value: '0.692'\\n  decisions:\\n  - 'D060: added metric-dependence caveat'\\n  deprecated: false\\n- id: C333\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: training effect Delta rho <= 0.017 non-significant\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_training_effect\\n    metric: delta_rho\\n    value: '0.017'\\n  decisions:\\n  - 'D060: marked non-significant'\\n  deprecated: false\\n- id: C341\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: readout token probe R2 +0.069, instruction attention +46pp\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_training_effect\\n    metric: delta_R2\\n    value: '+0.069'\\n  - exp_id: attention_analysis\\n    metric: delta_text_attention\\n    value: +46pp\\n  decisions: []\\n  deprecated: false\\n- id: C342\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: image tokens instruction-blind 10% across all 32 layers, architecture-expected\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: accuracy\\n    value: 10%\\n  decisions:\\n  - 'D060: reframed as architecture-expected'\\n  deprecated: false\\n- id: C344\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: readout token 100% cross-validated from L1\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe_loocv\\n    metric: accuracy\\n    value: 100%\\n  decisions: []\\n  deprecated: false\\n- id: C347\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'VLA training shifts to entry-exit pattern L0-L1: 21-25 heads, L31: 18 heads'\\n  type: quantitative\\n  evidence:\\n  - exp_id: attention_analysis\\n    metric: instruction_dominant_heads\\n  decisions:\\n  - 'D060: C2 anchor'\\n  deprecated: false\\n- id: C351\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 99.6% at L1 vs pretrained 80.2%\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: L1_accuracy\\n  decisions: []\\n  deprecated: false\\n- id: C356\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: under RSA alignment peaks L12 rho=0.628, declines to 0.422 at L32\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_layer_profile\\n    metric: spearman_rho\\n  decisions:\\n  - 'D060: qualified under RSA'\\n  deprecated: false\\n- id: C362\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 highest geometric alignment rho=0.692, ordering partially reverses\\n    under CKA\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_cross_encoder\\n    metric: spearman_rho\\n    value: '0.692'\\n  decisions:\\n  - 'D060: CKA caveat added'\\n  deprecated: false\\n- id: C369\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: non-significant geometric gain Delta rho=0.017 3%\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_training_effect\\n    metric: delta_rho\\n    value: '0.017'\\n  decisions:\\n  - 'D060: marked non-significant'\\n  deprecated: false\\n- id: C377\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: readout R2 Delta=+0.069 p<0.0001\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_training_effect\\n    metric: delta_R2\\n    value: '+0.069'\\n  decisions: []\\n  deprecated: false\\n- id: C378\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: image token instruction-blindness consistent with causal mask and frozen encoder\\n  type: mechanistic\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: accuracy\\n    value: 10%\\n  decisions:\\n  - 'D060: acknowledge causal mask as structural source'\\n  deprecated: false\\n- id: C379\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 highest RSA alignment 0.692, metric-dependent ordering\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_cross_encoder\\n    metric: spearman_rho\\n    value: '0.692'\\n  decisions:\\n  - 'D060: added under RSA qualifier and CKA metric-dependence caveat'\\n  deprecated: false\\n- id: C380\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: best-vs-best RSA gain non-significant Delta=+0.017 3% CI includes zero\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_training_effect\\n    metric: delta_rho_best_vs_best\\n    value: '+0.017'\\n  decisions:\\n  - 'D060: marked non-significant, CI includes zero'\\n  deprecated: false\\n- id: C381\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: image tokens instruction-blind consistent with causal mask and frozen encoder\\n  type: mechanistic\\n  evidence: 50-demo L1 ablation control\\n  decisions:\\n  - 'D060: architecture-expected framing'\\n  deprecated: false\\n- id: C383\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: training effects concentrated at readout R2 +0.069\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_training_effect\\n    metric: delta_R2\\n    value: '+0.069'\\n  decisions: []\\n  deprecated: false\\n- id: C386\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 highest RSA rho=0.692 under RSA\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_cross_encoder\\n    metric: spearman_rho\\n    value: '0.692'\\n  decisions:\\n  - 'D060: qualified under RSA'\\n  deprecated: false\\n- id: C390\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: VLA readout R2=0.678 vs DINOv2 0.634\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_comparison\\n    metric: R2\\n  decisions: []\\n  deprecated: false\\n- id: C395\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: ablation R2 +46% p<0.0001 deep layers unaffected\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_ablation\\n    metric: delta_R2\\n  decisions: []\\n  deprecated: false\\n- id: C401\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: encoder ranking reverses under CKA, metric-dependent\\n  type: qualitative\\n  evidence:\\n  - exp_id: cka_comparison\\n  decisions:\\n  - 'D060: CKA divergence in main text'\\n  deprecated: false\\n- id: C408\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: frozen encoder confound acknowledged\\n  type: qualitative\\n  evidence: []\\n  decisions:\\n  - 'D060: added frozen encoder caveat'\\n  deprecated: false\\n- id: C416\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: L1 ablation 5 demos per task, full-scale replication in progress\\n  type: qualitative\\n  evidence: []\\n  decisions:\\n  - 'D060: acknowledged ablation scale limitation'\\n  deprecated: false\\n- id: C417\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: functional probes R2 peak L8-L13 metric-independent non-monotonic trajectory\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_layer_profile\\n    metric: R2\\n    value: 0.655-0.678 at L8-L13\\n  decisions:\\n  - 'D060-C3-fix: R2 as primary metric-independent evidence'\\n  deprecated: false\\n- id: C418\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: RSA per-layer profile and encoder rankings metric-dependent, CKA monotonically\\n    increasing\\n  type: qualitative\\n  evidence:\\n  - exp_id: cka_comparison\\n  decisions:\\n  - 'D060-C3-fix: decline phase also RSA-specific, CKA monotonic'\\n  deprecated: false\\n- id: C419\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: functional probes peak L8-L13 R2=0.655-0.678 metric-independent\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_layer_profile\\n    metric: R2\\n  decisions:\\n  - 'D060-C3-fix: R2 as primary'\\n  deprecated: false\\n- id: C420\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: CKA monotonically increasing layer profiles\\n  type: qualitative\\n  evidence:\\n  - exp_id: cka_layer_profile\\n  decisions:\\n  - 'D060-C3-fix: decline also RSA-specific'\\n  deprecated: false\\n- id: C421\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C3 contribution: non-monotonic transformation, R2 confirmed, RSA confirms\\n    but CKA diverges'\\n  type: qualitative\\n  evidence:\\n  - exp_id: probe_layer_profile\\n  - exp_id: rsa_layer_profile\\n  - exp_id: cka_layer_profile\\n  decisions:\\n  - 'D060-C3-fix: balanced metric framing'\\n  deprecated: false\\n- id: C422\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: encoder rankings and per-layer profiles metric-dependent, R2 inverted-U metric-independent\\n  type: qualitative\\n  evidence:\\n  - exp_id: cka_comparison\\n  - exp_id: probe_layer_profile\\n  decisions:\\n  - 'D060-C3-fix: CKA divergence covers both rankings and profiles'\\n  deprecated: false\\n- id: C423\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: trained image_mean RSA stable L0-L12 Delta=+0.017 n.s., decline L12-L32 Delta=-0.206\\n    p<0.0001\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_layer_profile\\n    metric: spearman_rho\\n  decisions:\\n  - 'D060-C3-fix: rise phase reframed as stable'\\n  deprecated: false\\n- id: C424\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: untrained RSA declines monotonically from L0 Delta=-0.062 to L12 p<0.0001\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_layer_profile_untrained\\n    metric: spearman_rho\\n  decisions: []\\n  deprecated: false\\n- id: C425\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: marginal RSA change at image_mean +0.017 n.s. contrasts with readout +0.074\\n    p<0.0001\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_layer_profile\\n    metric: delta_rho_readout\\n  decisions:\\n  - 'D060-C3-fix: readout contrast added'\\n  deprecated: false\\n- id: C426\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: N=63728 observations, N/params ratio approx 0.05 for MLP probe\\n  type: quantitative\\n  evidence:\\n  - exp_id: dataset_stats\\n    metric: N_observations\\n    value: '63728'\\n  decisions: []\\n  deprecated: false\\n- id: C427\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: Probe R2 trained vs untrained FDR significant at 29-30/33 layers both positions\\n  type: quantitative\\n  evidence:\\n  - exp_id: fdr_correction\\n    metric: significant_layers_R2\\n    value: 29-30/33\\n  decisions: []\\n  deprecated: false\\n- id: C428\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: RSA FDR significant at 25/33 layers image_mean, 0/33 last_preaction due to\\n    n=10 power ceiling\\n  type: quantitative\\n  evidence:\\n  - exp_id: fdr_correction\\n    metric: significant_layers_RSA\\n    value: 25/33 image_mean, 0/33 readout\\n  decisions: []\\n  deprecated: false\\n- id: C429\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: non-monotonic profile stable under 25-demo subsampling, RSA peak unchanged\\n    L12, profile r=0.97\\n  type: quantitative\\n  evidence:\\n  - exp_id: ablation_p2_demo_sensitivity\\n    metric: profile_correlation_RSA\\n    value: '0.970'\\n  decisions: []\\n  deprecated: false\\nfigures:\\n- caption: Three similarity metrics across representation sources. \\\\textbf{(a)\\n  deprecated: false\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines (RSA values)\\n    tier: tier1\\n  - exp_id: plan_009_cka_verification\\n    metric: linear_cka + rdm_cka\\n    tier: tier1\\n  id: F001\\n  label: fig:metric_comparison\\n  location:\\n    section: appendix\\n  source_path: figures/fig6.pdf\\n  type: result\\n- caption: RSA with the action space ($\\\\rho$) across representation sources. Self-supervised\\n    DINOv2 \\\\texttt{cls\\\\_token\\n  deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines + trained/untrained peaks\\n    tier: tier1\\n  - exp_id: plan_013_branch_split\\n    metric: fused_2176d_rsa=0.634\\n    tier: tier1\\n  id: F002\\n  label: fig:rsa_bar\\n  location:\\n    section: experiments\\n  source_path: figures/fig2.pdf\\n  type: result\\n- caption: 'Per-layer RSA ($\\\\rho$) with the action space across all 32 LLM layers.\\n    Trained image\\\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\\\to$ L12 $=\\n    0.628$ (peak, above Projector $0.615$) $\\\\to$ L32 $= 0.422$. Untrained image\\\\_mean\\n    (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2\\n    cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).'\\n  deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: per-layer RSA trained/untrained image_mean (32 layers)\\n    tier: tier1\\n  id: F003\\n  label: fig:layer_curves\\n  location:\\n    section: experiments\\n  source_path: figures/fig3.pdf\\n  type: result\\n- caption: Functional probe $R^2$ for action prediction (best layer for each source).\\n    Both trained readout ($R^2{=\\n  deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: peak R2 values (trained img_mean L8, readout L13)\\n    tier: tier1\\n  - exp_id: plan_012_clip_vit_control\\n    metric: projector/dino/clip R2\\n    tier: tier1\\n  id: F004\\n  label: fig:probe_bars\\n  location:\\n    section: experiments\\n  source_path: figures/fig4.pdf\\n  type: result\\n- caption: \\\\textbf{(a)\\n  deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained vs untrained per-layer RSA + instruction conditions\\n    tier: tier1\\n  - exp_id: plan_008_random_inst_control\\n    metric: instruction invariance\\n    tier: tier1\\n  id: F005\\n  label: fig:factorial\\n  location:\\n    section: experiments\\n  source_path: figures/fig5.pdf\\n  type: result\\n- id: F006\\n  location:\\n    section: appendix\\n    figure_number: 0\\n  caption: ''\\n  type: other\\n  source: {}\\n  output_path: ''\\n  deprecated: false\\n- id: F007\\n  location:\\n    section: appendix\\n    figure_number: 0\\n  caption: ''\\n  type: other\\n  source: {}\\n  output_path: ''\\n  deprecated: false\\npaper:\\n  generated_at: '2026-05-17T22:15:14.113705+00:00'\\n  source: auto-bootstrap from existing tex files\\n  title: Formatting Instructions for CoRL 2026 Camera-Ready\\n  version: 51\\ntables:\\n- caption: Geometric (RSA $\\\\rho$) and functional (probe $R^2$) alignment with the\\n    action space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both\\n    trained readout and image\\\\_mean exceed the projector in $R^2$, confirming the\\n    inverted-U extends to functional capacity. VLA rows show peak-layer values (RSA/R$^2$\\n    peaks listed separately when they differ). 95\\\\% CIs from 10{,\\n  cells: []\\n  deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: all RSA peaks + baselines\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: all R2 peaks\\n    tier: tier1\\n  - exp_id: plan_012_clip_vit_control\\n    metric: projector/dino/clip R2\\n    tier: tier1\\n  id: T001\\n  label: tab:rsa_overview\\n  location:\\n    section: experiments\\n- caption: Training effects on action-relevant structure (bootstrap, 10{,\\n  cells: []\\n  deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best + same_layer comparisons\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best R2\\n    tier: tier1\\n  id: T002\\n  label: tab:training_effects\\n  location:\\n    section: experiments\\n_completeness:\\n  coverage: 69/74\\n  claims: 71\\n  tables: 0\\n  figures: 3\\n  tier_counts:\\n    tier1: 0\\n    tier2: 69\\n    tier3: 5\\n    tierX: 0\\n  last_checked: '2026-05-17T22:15:14.113771+00:00'\\n\", \"total_chars\": 51898, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
Let me read the full content from the saved file to understand the complete structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "309c3f7b-a895-405f-bbc5-0b529cca1121",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3VnYPept3F3baDaqsTJDY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1050,
      "cache_read_input_tokens": 25517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1050
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

_source line 11_

Let me read the full saved output to understand the complete structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "d66f2c27-ebb0-4cd1-b356-b0cd9fcfd9d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3VnYPept3F3baDaqsTJDY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1050,
      "cache_read_input_tokens": 25517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1050
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01AFbZeEFNMFxf3VJmWT7irS`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/da042411-baa9-4148-b88d-99c95c45f67d/tool-results/toolu_01CrPZRnZp85eE6j3pZ5GRg7.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "fab392c7-5597-47c6-9432-82c20c072e6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3VnYPept3F3baDaqsTJDY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1050,
      "cache_read_input_tokens": 25517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1050
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

_source line 13 · 2026-05-18T17:42:11.737Z_

<details><summary>↩ Tool result · `toolu_01AFbZeEFNMFxf3VJmWT7irS`</summary>

```text
1	{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml\", \"content\": \"claims:\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915\\n    tier: tier1\\n  - exp_id: plan_013_branch_split\\n    metric: post_projector_4096d_rsa=0.615\\n    tier: tier1\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.clip_cls=0.557\\n    tier: tier1\\n  id: C001\\n  location:\\n    context: result_statement\\n    section: abstract\\n  text: 'First, self-supervised pretraining provides the strongest action-relevant\\n    geometry: standalone DINOv2 achieves RSA $ = 0.692$, exceeding all VL-pretrained\\n    encoders (DinoSigLIP+Projector $ = 0.615$; CL'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_image_mean_peak.rsa=0.6282\\n    tier: tier1\\n  - exp_id: d041_method_b_rsa\\n    metric: untrained_image_mean_peak.rsa=0.6117\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\n    tier: tier1\\n  id: C002\\n  location:\\n    context: result_statement\\n    section: abstract\\n  text: 'Second, the LLM applies a non-monotonic transformation---the first 12 layers\\n    enhance geometric alignment with the action space above the vision encoder input\\n    ($$: $0.612  0.628$ at L12), while the rem'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017,significant=false\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686,p=0.0001\\n    tier: tier1\\n  id: C003\\n  location:\\n    context: result_statement\\n    section: abstract\\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\\n    capacity (R^2 Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates\\n  type: quantitative\\n- deprecated: false\\n  evidence: llama2base_action_probe experiment\\n  id: C004\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: 'Linear CKA~kornblith2019 reverses the RSA ordering: untrained LLM ($CKA =\\n    0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2\\n    ($0.066$), partially inverting the self-superv'\\n  type: quantitative\\n  decisions: []\\n- deprecated: false\\n  evidence:\\n  - exp_id: plan_009_cka_verification\\n    metric: rdm_cka.*\\n    tier: tier1\\n  id: C005\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: 'RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $$\\n    Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).'\\n  type: quantitative\\n- deprecated: false\\n  evidence:\\n  - exp_id: plan_009_cka_verification\\n    metric: linear_cka per-layer (derived from full scan)\\n    tier: tier2\\n  id: C006\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: At the per-layer level, linear CKA between image\\\\_mean and the action space\\n    rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U\\n    pattern.\\n  type: quantitative\\n- deprecated: false\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.*\\n    tier: tier1\\n  - exp_id: plan_009_cka_verification\\n    metric: linear_cka.* + rdm_cka.*\\n    tier: tier1\\n  id: C007\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: 'Three similarity metrics across representation sources. (a)~RSA ranks DINOv2\\n    cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). (b)~Linear CKA reverses\\n    the ordering: Untrained ($0.089$) $>$ Tr'\\n  type: quantitative\\n- deprecated: false\\n  evidence:\\n  - exp_id: plan_013_branch_split\\n    metric: fused_2176d_rsa=0.634\\n    tier: tier1\\n  id: C008\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: Fusion produces a representation ($ = 0.634$) that exceeds either branch alone,\\n    indicating that concatenation captures complementary structure.\\n  type: quantitative\\n- deprecated: false\\n  evidence:\\n  - exp_id: plan_013_branch_split\\n    metric: fused_2176d_rsa=0.634, post_projector_4096d_rsa=0.615\\n    tier: tier1\\n  id: C009\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: 'The MLP projector then compresses this signal: DinoSigLIP+Projector achieves\\n    $ = 0.615$, a drop of $ = 0.019$ from the fused 2{,176-D input.'\\n  type: quantitative\\n- deprecated: false\\n  evidence:\\n  - exp_id: plan_013_branch_split\\n    metric: standalone_dino_patch_mean_rsa=0.631\\n    tier: tier1\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_patch_mean=0.6307\\n    tier: tier1\\n  id: C010\\n  location:\\n    context: result_statement\\n    section: appendix\\n  text: DINOv2 patch\\\\_mean achieves RSA $ = 0.631$, between the cls\\\\_token ($0.692$)\\n    and the fused DinoSigLIP ($0.634$).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915, trained_image_mean_peak\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\n    tier: tier1\\n  id: C011\\n  location:\\n    context: result_statement\\n    section: conclusion\\n  text: 'Three findings emerge: (1)~the frozen vision encoder provides the dominant\\n    action-relevant geometry, with self-supervised DINOv2 achieving the highest alignment\\n    ($ = 0.692$) exceeding all VL-pretraine'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915\\n    tier: tier1\\n  id: C012\\n  location:\\n    context: result_statement\\n    section: discussion\\n  text: 'The vision encoder is the source: self-supervised DINOv2 achieves the highest\\n    geometric alignment ($ = 0.692$), exceeding all VLA internal representations.'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.p=0.006\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686\\n    tier: tier1\\n  id: C013\\n  location:\\n    context: result_statement\\n    section: discussion\\n  text: 'Training redistributes geometry but enhances decodability: modest geometric\\n    gain (Delta = 0.017--0.023, 3--4% of baseline across two benchmarks), while substantially\\n    improving R^2 (Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.significant=false\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  id: C014\\n  location:\\n    context: result_statement\\n    section: discussion\\n  text: Cross-benchmark replication (LIBERO-Spatial Delta = 0.023, p < 0.001) suggests\\n    the LIBERO-Goal RSA CI (incl. zero) reflects limited power rather than a true\\n    null, but the effect remains small (3--4% of baseline).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915\\n    tier: tier1\\n  - exp_id: plan_013_branch_split\\n    metric: fused_2176d_rsa=0.634, standalone_dino_patch_mean_rsa=0.631\\n    tier: tier1\\n  id: C015\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: The standalone DINOv2 cls\\\\_token achieves the highest alignment of any representation\\n    source ($ = 0.692$), followed by the fused DinoSigLIP 2{,176-D representation\\n    before projection ($ = 0.634$) and t\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.clip_cls=0.557\\n    tier: tier1\\n  id: C016\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: CLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment\\n    among pretrained encoders ($ = 0.557$; Figure~fig:rsa_bar).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557, trained_image_mean_peak.rsa=0.6282\\n    tier: tier1\\n  id: C017\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: DINOv2, pretrained with self-supervised objectives alone, achieves $ = 0.692$---exceeding\\n    not only CLIP ($ = 0.557$) but also the VLA's own internal representations at\\n    their peaks (trained image\\\\_mean\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_012_clip_vit_control\\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\\n    tier: tier1\\n  - exp_id: unified_action_probe\\n    metric: bootstrap_pairwise.projector_vs_dino.p=0.557\\n    tier: tier1\\n  id: C018\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'Functional probes corroborate the ranking: DINOv2 cls\\\\_token achieves $R^2\\n    = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$,\\n    $p = 0.557$, n.s.), while CLIP yields the'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_013_branch_split\\n    metric: dinov2_branch_rsa=0.619, siglip_branch_rsa=0.621\\n    tier: tier1\\n  id: C019\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: The DINOv2 (1{,024-D) and SigLIP (1{,152-D) branches yield near-identical\\n    RSA ($0.619$ vs.\\\\ $0.621$); fusion exceeds either ($0.634$), while the projector\\n    introduces modest compression loss ($0.634  0\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: all RSA values\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: all R2 peak values\\n    tier: tier1\\n  id: C020\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Geometric (RSA $$) and functional (probe $R^2$) alignment with the action\\n    space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both trained\\n    readout and image\\\\_mean exceed the projector in\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines + trained_image_mean_peak\\n    tier: tier1\\n  id: C021\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'RSA with the action space ($$) across representation sources. Self-supervised\\n    DINOv2 cls\\\\_token ($=0.692$) achieves the highest geometric alignment, followed\\n    by fused DinoSigLIP ($0.634$) and the VLA '\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_image_mean per-layer RSA (L0=0.612, L12=0.628, L32=0.422)\\n    tier: tier1\\n  id: C022\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'Figure~fig:layer_curves reveals a non-monotonic trajectory for trained image\\\\_mean\\n    RSA: $$ begins at $0.612$ (L0, equal to the projector input), rises to a peak\\n    of $0.628$ at L12---above the DinoSigLI'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_image_mean_peak.layer=8, mean_R2=0.6553\\n    tier: tier1\\n  - exp_id: plan_012_clip_vit_control\\n    metric: projector_mean_R2=0.6298\\n    tier: tier1\\n  id: C023\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Full-layer probe scans reveal that trained image\\\\_mean $R^2$ peaks at L8 ($0.655$),\\n    exceeding the projector ($0.630$, $ = +0.025$; Table~tab:rsa_overview).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_image_mean_peak.layer=8\\n    tier: tier1\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_image_mean_peak.layer=12\\n    tier: tier1\\n  id: C024\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: The $R^2$ peak (L8) precedes the RSA peak (L12) by four layers, suggesting\\n    that functional decodability peaks earlier than geometric alignment; we adopt\\n    ``early-to-middle layers (L8--L13)'' to capture\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_last_preaction_peak.rsa=0.6425, layer=12\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak.mean_R2=0.6779, layer=13\\n    tier: tier1\\n  id: C025\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Trained readout achieves peak RSA $ = 0.643$ at L12 and probe $R^2 = 0.678$\\n    (L13), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $ = 0.048$; Table~tab:rsa_overview,\\n    Figure~fig:probe_bars).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained per-layer RSA L12=0.628→L32=0.422; untrained 0.612→0.545\\n    tier: tier1\\n  id: C026\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'The decline from L12 to L32 ($$: $0.628  0.422$) exceeds the untrained decay\\n    ($0.612  0.545$), indicating that training actively redirects later layers away\\n    from action geometry, yielding a three-phas'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak=0.6779, trained_image_mean_peak=0.6553\\n    tier: tier1\\n  - exp_id: plan_012_clip_vit_control\\n    metric: projector_mean_R2=0.6298, dino_cls_mean_R2=0.6343\\n    tier: tier1\\n  id: C027\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Functional probe $R^2$ for action prediction (best layer for each source).\\n    Both trained readout ($R^2{=0.678$, L13) and trained image\\\\_mean ($0.655$, L8)\\n    exceed the projector baseline ($0.630$), confi\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  id: C028\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: best-vs-best Delta = +0.017 (3% of baseline; LIBERO-Spatial confirms with\\n    Delta = +0.023, 4%, p < 0.001). This geometric gain is far smaller than the functional\\n    improvement.\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\n    tier: tier1\\n  id: C029\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: RSA best-vs-best yields at most a modest gain (Delta = 0.017--0.023, 3--4%\\n    of baseline across two benchmarks), while R^2 shows substantially larger improvements.\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006; last_preaction.delta=0.0686,p=0.0001\\n    tier: tier1\\n  id: C030\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Yet $R^2$ best-vs-best is significant for both image\\\\_mean ($ = +0.015$, $p\\n    = 0.006$) and readout ($ = +0.069$, $p < 0.0001$; Table~tab:training_effects).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_same_layer.last_preaction_L13.note (untrained L13 R2 near -0.33)\\n    tier: tier1\\n  id: C031\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Untrained readout $R^2$ reaches $ -0.33$ at L12--L29 (predictions worse than\\n    a constant-mean baseline), while untrained image\\\\_mean $R^2$ drops to near-zero\\n    at L10--L13.\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best + same_layer\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best\\n    tier: tier1\\n  id: C032\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'Training effects on action-relevant structure (LIBERO-Goal; bootstrap). RSA\\n    best-vs-best yields modest geometric gain (Delta=+0.017, 3%; LIBERO-Spatial: +0.023,\\n    p<0.001), while R^2 shows substantially larger functional gains.'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: instruction_effect (derived from trained_with_inst vs trained_no_inst)\\n    tier: tier1\\n  - exp_id: plan_008_random_inst_control\\n    metric: max_absolute_delta=0.0165, instruction_invariant=true\\n    tier: tier1\\n  id: C033\\n  location:\\n    context: finding_statement\\n    section: experiments\\n  text: This confirms that the action geometry is visually grounded and instruction-independent~grant2026.\\n  type: methodological\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: experimental design (2x2 factorial)\\n    tier: tier2\\n  id: C034\\n  location:\\n    context: result_statement\\n    section: introduction\\n  text: We cross training status (trained vs.\\\\ untrained, reinitializing 6.74B LLM\\n    parameters) with instruction presence in a $2 2$ factorial design, and quantify\\n    action-relevant structure using RSA~kriegesko\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557\\n    tier: tier1\\n  id: C035\\n  location:\\n    context: result_statement\\n    section: introduction\\n  text: Standalone DINOv2 achieves the highest action-space alignment (RSA $ = 0.692$),\\n    far exceeding CLIP ($ = 0.557$) and the VLA's own peak internal representation\\n    ($ = 0.628$ at L12).\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_012_clip_vit_control\\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\\n    tier: tier1\\n  id: C036\\n  location:\\n    context: result_statement\\n    section: introduction\\n  text: 'Functional probes corroborate this ranking: DINOv2 ($R^2 = 0.634$) $$ Projector\\n    ($0.630$) $>$ CLIP ($0.587$).'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained_image_mean_peak.rsa=0.6282\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\n    tier: tier1\\n  id: C037\\n  location:\\n    context: result_statement\\n    section: introduction\\n  text: 'Second, the LLM applies a non-monotonic transformation: the first 12 layers\\n    enhance geometric alignment above the vision encoder input ($$: $0.612  0.628$),\\n    while the remaining 20 layers degrade it ($'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_013_branch_split\\n    metric: methodology (encoder extraction)\\n    tier: tier2\\n  id: C038\\n  location:\\n    context: bold\\n    section: method\\n  text: DINOv2 ViT-L/14\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_012_clip_vit_control\\n    metric: methodology (CLIP extraction)\\n    tier: tier2\\n  id: C039\\n  location:\\n    context: bold\\n    section: method\\n  text: CLIP ViT-L/14\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\n    tier: tier1\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\n    tier: tier1\\n  id: C040\\n  location:\\n    context: result_statement\\n    section: introduction\\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\\n    capacity---redistribution dominates over creation.\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_010_libero_spatial\\n    metric: rsa.trained_image_mean_peak(layer=14,rsa=0.691), action_probe.trained_image_mean_peak(layer=13,R2=0.696)\\n    tier: tier1\\n  id: C041\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: 'Cross-benchmark validation (LIBERO-Spatial): inverted-U replicates, trained\\n    image_mean RSA peaks at L14 (rho=0.691), R^2 at L13 (0.696), peak shifting ~2\\n    layers deeper than LIBERO-Goal.'\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_010_libero_spatial\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,ci_95=[0.012,0.036],p=0.001\\n    tier: tier1\\n  id: C042\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: Training produces a significant geometric gain on LIBERO-Spatial (best-vs-best\\n    Delta=+0.023, p<0.001), confirming LIBERO-Goal effect reflects limited power.\\n  type: quantitative\\n- deprecated: true\\n  evidence:\\n  - exp_id: plan_010_libero_spatial\\n    metric: rsa.trained_last_preaction_peak(layer=15), action_probe.trained_last_preaction_peak(layer=21)\\n    tier: tier1\\n  id: C043\\n  location:\\n    context: result_statement\\n    section: experiments\\n  text: RSA--R^2 peak convergence does not replicate on LIBERO-Spatial (RSA L15 vs\\n    R^2 L21, 6-layer gap vs 1 on Goal), suggesting peak alignment may be benchmark-specific.\\n  type: quantitative\\n- id: C044\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Image tokens encode purely visual information (instruction classification\\n    at chance, 10%, across all layers)\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: image_mean_accuracy\\n    value: 10%\\n  decisions: []\\n  deprecated: true\\n- id: C046\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Readout token: 100% instruction classification from L1, LOOCV-verified'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: readout_accuracy\\n    value: 100%\\n  - exp_id: loocv_validation\\n    metric: accuracy\\n    value: 100% ± 0.00\\n  decisions: []\\n  deprecated: true\\n- id: C049\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 25/32 attention heads flip to instruction-dominant (58% attention to ~8% of\\n    sequence)\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_attention_pattern\\n    metric: instruction_dominant_heads\\n    value: 25/32\\n  - exp_id: l1_attention_pattern\\n    metric: instruction_attention_fraction\\n    value: 58%\\n  decisions: []\\n  deprecated: true\\n- id: C053\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Untrained incidental routing decays to 82%\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: untrained_L31_accuracy\\n    value: 82%\\n  decisions: []\\n  deprecated: true\\n- id: C058\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: RSA peaks at L12, probe R² peaks at L8-L13\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_per_layer\\n    metric: trained_image_mean_peak\\n    value: L12, rho=0.628\\n  decisions: []\\n  deprecated: true\\n- id: C064\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 highest geometric foundation (rho=0.692)\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_encoder_comparison\\n    metric: dinov2_cls_rsa\\n    value: '0.692'\\n  decisions: []\\n  deprecated: true\\n- id: C071\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Training reshapes readout-token integration (routing +18pp, attention +46pp)\\n    rather than visual representations (Delta <= 1.7%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_summary\\n    metric: routing_delta\\n    value: +18pp\\n  - exp_id: training_effect_summary\\n    metric: attention_delta\\n    value: +46pp\\n  - exp_id: training_effect_summary\\n    metric: image_mean_rsa_delta\\n    value: '+0.017'\\n  decisions: []\\n  deprecated: true\\n- id: C072\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Image tokens: instruction classification at chance (10%) across all 32 layers'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: image_mean_accuracy\\n    value: 10%\\n  decisions: []\\n  deprecated: true\\n- id: C074\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Readout token: 100% instruction identity from L1, LOOCV-verified'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: readout_accuracy\\n    value: 100%\\n  - exp_id: loocv_validation\\n    metric: accuracy\\n    value: 100%\\n  decisions: []\\n  deprecated: true\\n- id: C077\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 25/32 heads flip to instruction-dominant (58% attention)\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_attention_pattern\\n    metric: instruction_dominant_heads\\n    value: 25/32\\n  decisions: []\\n  deprecated: true\\n- id: C081\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Untrained routing decays to 82% by L31\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: untrained_L31_accuracy\\n    value: 82%\\n  decisions: []\\n  deprecated: true\\n- id: C086\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 RSA rho=0.692\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_encoder_comparison\\n    metric: dinov2_cls_rsa\\n    value: '0.692'\\n  decisions: []\\n  deprecated: true\\n- id: C092\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Inverted-U peak rho=0.628 at L12, 0.422 at L32\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_per_layer\\n    metric: trained_image_mean_L12\\n    value: '0.628'\\n  - exp_id: rsa_per_layer\\n    metric: trained_image_mean_L32\\n    value: '0.422'\\n  decisions: []\\n  deprecated: true\\n- id: C099\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Training geometric gain Delta=0.017-0.023, 3-4%\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_comparison\\n    metric: rsa_best_vs_best\\n    value: +0.017 (Goal), +0.023 (Spatial)\\n  decisions: []\\n  deprecated: true\\n- id: C107\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Readout R2 Delta=+0.069, p<0.0001\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_comparison\\n    metric: readout_r2_delta\\n    value: '+0.069'\\n  decisions: []\\n  deprecated: true\\n- id: C108\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: Image_mean instruction classification at chance (10%) across all 32 layers\\n  type: quantitative\\n  evidence: 50-demo L1 ablation multi-layer comparison\\n  decisions: []\\n  deprecated: false\\n- id: C110\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: Trained readout 100% L1-L31, LOOCV 100% +/- 0.00\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: readout_accuracy\\n    value: 100%\\n  - exp_id: loocv_validation\\n    metric: accuracy\\n    value: 100%\\n  decisions: []\\n  deprecated: false\\n- id: C113\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Untrained readout decays: L8 95.5%, L31 82%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: untrained_L8\\n    value: 95.5%\\n  - exp_id: cross_instruction_probe\\n    metric: untrained_L31\\n    value: 82%\\n  decisions: []\\n  deprecated: false\\n- id: C117\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Instruction invariance: max |Delta| = 0.006'\\n  type: quantitative\\n  evidence:\\n  - exp_id: factorial_analysis\\n    metric: instruction_effect\\n    value: '0.006'\\n  decisions: []\\n  deprecated: false\\n- id: C122\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'QA probe: trained 86.3% (L20), DINOv2 82.7%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: qa_probe\\n    metric: trained_accuracy\\n    value: 86.3%\\n  - exp_id: qa_probe\\n    metric: dinov2_accuracy\\n    value: 82.7%\\n  decisions: []\\n  deprecated: false\\n- id: C128\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Trained L1: 25/32 heads instruction-dominant, 58% attention to instruction,\\n    20.9% to image'\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_attention_pattern\\n    metric: instruction_dominant_heads\\n    value: 25/32\\n  - exp_id: l1_attention_pattern\\n    metric: instruction_attention\\n    value: 58%\\n  - exp_id: l1_attention_pattern\\n    metric: image_attention\\n    value: 20.9%\\n  decisions: []\\n  deprecated: false\\n- id: C135\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Untrained L1: 0/32 heads instruction-dominant, 87.8% image, 11.7% instruction'\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_attention_pattern\\n    metric: untrained_heads\\n    value: 0/32\\n  - exp_id: l1_attention_pattern\\n    metric: untrained_image_attention\\n    value: 87.8%\\n  decisions: []\\n  deprecated: false\\n- id: C143\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Training effect asymmetry: attention +46pp, routing +18pp, R2 +0.069, but\\n    image_mean Delta<=1.7%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_summary\\n  decisions: []\\n  deprecated: false\\n- id: C152\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 cls RSA rho=0.692, highest alignment\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_encoder_comparison\\n    metric: dinov2_cls\\n    value: '0.692'\\n  decisions: []\\n  deprecated: false\\n- id: C162\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: CLIP RSA rho=0.557\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_encoder_comparison\\n    metric: clip_patch_mean\\n    value: '0.557'\\n  decisions: []\\n  deprecated: false\\n- id: C173\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Inverted-U: L0=0.612, L12=0.628, L32=0.422'\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_per_layer\\n    metric: trained_image_mean\\n    value: L0=0.612, L12=0.628, L32=0.422\\n  decisions: []\\n  deprecated: false\\n- id: C185\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: R2 peak L8-L10 (0.655 +/- 0.002)\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_per_layer\\n    metric: trained_image_mean_peak\\n    value: '0.655'\\n  decisions: []\\n  deprecated: false\\n- id: C198\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: Readout R2=0.678 (L13), exceeds projector by 0.048\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_comparison\\n    metric: readout_r2\\n    value: '0.678'\\n  decisions: []\\n  deprecated: false\\n- id: C212\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: RSA best-vs-best Delta=+0.017, same-layer +0.079\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_comparison\\n    metric: rsa_best_vs_best\\n    value: '+0.017'\\n  - exp_id: training_effect_comparison\\n    metric: same_layer_L12\\n    value: '+0.079'\\n  decisions: []\\n  deprecated: false\\n- id: C227\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'R2 best-vs-best: image_mean +0.015 (p=0.006), readout +0.069 (p<0.0001)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_comparison\\n    metric: image_mean_delta\\n    value: '+0.015'\\n  - exp_id: probe_comparison\\n    metric: readout_delta\\n    value: '+0.069'\\n  decisions: []\\n  deprecated: false\\n- id: C243\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Untrained pathological: L10-L11 R2=-0.33, -0.28'\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_per_layer\\n    metric: untrained_L10_L11\\n    value: -0.33, -0.28\\n  decisions: []\\n  deprecated: false\\n- id: C260\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'LIBERO-Spatial: RSA peak L14 (0.691), R2 peak L13 (0.696), Delta=+0.023 p<0.001'\\n  type: quantitative\\n  evidence:\\n  - exp_id: libero_spatial\\n    metric: rsa_peak\\n    value: L14, 0.691\\n  - exp_id: libero_spatial\\n    metric: r2_peak\\n    value: L13, 0.696\\n  - exp_id: libero_spatial\\n    metric: training_delta\\n    value: '+0.023'\\n  decisions: []\\n  deprecated: false\\n- id: C278\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Robustness: RSA profile r=0.970 under halved demos'\\n  type: quantitative\\n  evidence:\\n  - exp_id: demo_sensitivity\\n    metric: rsa_profile_correlation\\n    value: '0.970'\\n  decisions: []\\n  deprecated: false\\n- id: C279\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Training effects: routing +18pp, attention +46pp, R2 +0.069; image_mean Delta<=1.7%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_summary\\n  decisions: []\\n  deprecated: true\\n- id: C281\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Instruction invariance |Delta| < 0.006\\n  type: quantitative\\n  evidence:\\n  - exp_id: factorial_analysis\\n    metric: instruction_effect\\n    value: '0.006'\\n  decisions: []\\n  deprecated: true\\n- id: C284\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: LIBERO-Spatial Delta=0.023, p<0.001\\n  type: quantitative\\n  evidence:\\n  - exp_id: libero_spatial\\n    metric: training_delta\\n    value: '+0.023'\\n  decisions: []\\n  deprecated: true\\n- id: C285\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Image tokens: instruction classification at chance across all layers'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n  decisions: []\\n  deprecated: false\\n- id: C287\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Readout token: 100% from L1, LOOCV-verified'\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n  - exp_id: loocv_validation\\n  decisions: []\\n  deprecated: false\\n- id: C290\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: 25/32 heads flip to instruction-dominant (58%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_attention_pattern\\n  decisions: []\\n  deprecated: false\\n- id: C294\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Untrained decays to 82%\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: untrained_L31\\n    value: 82%\\n  decisions: []\\n  deprecated: false\\n- id: C299\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: RSA inverted-U peak L12, R2 L8-L13, DINOv2 rho=0.692\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_per_layer\\n  - exp_id: rsa_encoder_comparison\\n  decisions: []\\n  deprecated: false\\n- id: C305\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Training: R2 +0.069 readout, Delta<=1.7% image_mean'\\n  type: quantitative\\n  evidence:\\n  - exp_id: training_effect_summary\\n  decisions: []\\n  deprecated: false\\n- id: C306\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: image tokens instruction-blind at chance 10% across all layers and conditions\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: accuracy\\n    value: 10%\\n  decisions:\\n  - 'D060: reframed as architecture-expected verification'\\n  deprecated: false\\n- id: C308\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: readout token 100% instruction classification from L1, cross-validated\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe_loocv\\n    metric: accuracy\\n    value: 100%\\n  decisions: []\\n  deprecated: false\\n- id: C311\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'VLA training shifts to entry-layer routing L0-L1: 21-25 heads with exit-layer\\n    L31: 18 heads'\\n  type: quantitative\\n  evidence:\\n  - exp_id: attention_analysis\\n    metric: instruction_dominant_heads\\n    value: 25/32 at L1, 18/32 at L31\\n  decisions:\\n  - 'D060: C2 anchor claim'\\n  deprecated: false\\n- id: C315\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: immediate instruction access 99.6% at L1 vs pretrained 80.2%\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: L1_accuracy\\n    value: 99.6% vs 80.2%\\n  decisions: []\\n  deprecated: false\\n- id: C320\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: under RSA peak rho=0.628 at L12 declining to 0.422 at L32\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_layer_profile\\n    metric: spearman_rho\\n    value: 0.628 L12, 0.422 L32\\n  decisions:\\n  - 'D060: qualified with under RSA'\\n  deprecated: false\\n- id: C326\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 highest geometric alignment rho=0.692, metric-dependent\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_cross_encoder\\n    metric: spearman_rho\\n    value: '0.692'\\n  decisions:\\n  - 'D060: added metric-dependence caveat'\\n  deprecated: false\\n- id: C333\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: training effect Delta rho <= 0.017 non-significant\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_training_effect\\n    metric: delta_rho\\n    value: '0.017'\\n  decisions:\\n  - 'D060: marked non-significant'\\n  deprecated: false\\n- id: C341\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: readout token probe R2 +0.069, instruction attention +46pp\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_training_effect\\n    metric: delta_R2\\n    value: '+0.069'\\n  - exp_id: attention_analysis\\n    metric: delta_text_attention\\n    value: +46pp\\n  decisions: []\\n  deprecated: false\\n- id: C342\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: image tokens instruction-blind 10% across all 32 layers, architecture-expected\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: accuracy\\n    value: 10%\\n  decisions:\\n  - 'D060: reframed as architecture-expected'\\n  deprecated: false\\n- id: C344\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: readout token 100% cross-validated from L1\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe_loocv\\n    metric: accuracy\\n    value: 100%\\n  decisions: []\\n  deprecated: false\\n- id: C347\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'VLA training shifts to entry-exit pattern L0-L1: 21-25 heads, L31: 18 heads'\\n  type: quantitative\\n  evidence:\\n  - exp_id: attention_analysis\\n    metric: instruction_dominant_heads\\n  decisions:\\n  - 'D060: C2 anchor'\\n  deprecated: false\\n- id: C351\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 99.6% at L1 vs pretrained 80.2%\\n  type: quantitative\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: L1_accuracy\\n  decisions: []\\n  deprecated: false\\n- id: C356\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: under RSA alignment peaks L12 rho=0.628, declines to 0.422 at L32\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_layer_profile\\n    metric: spearman_rho\\n  decisions:\\n  - 'D060: qualified under RSA'\\n  deprecated: false\\n- id: C362\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 highest geometric alignment rho=0.692, ordering partially reverses\\n    under CKA\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_cross_encoder\\n    metric: spearman_rho\\n    value: '0.692'\\n  decisions:\\n  - 'D060: CKA caveat added'\\n  deprecated: false\\n- id: C369\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: non-significant geometric gain Delta rho=0.017 3%\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_training_effect\\n    metric: delta_rho\\n    value: '0.017'\\n  decisions:\\n  - 'D060: marked non-significant'\\n  deprecated: false\\n- id: C377\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: readout R2 Delta=+0.069 p<0.0001\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_training_effect\\n    metric: delta_R2\\n    value: '+0.069'\\n  decisions: []\\n  deprecated: false\\n- id: C378\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: image token instruction-blindness consistent with causal mask and frozen encoder\\n  type: mechanistic\\n  evidence:\\n  - exp_id: cross_instruction_probe\\n    metric: accuracy\\n    value: 10%\\n  decisions:\\n  - 'D060: acknowledge causal mask as structural source'\\n  deprecated: false\\n- id: C379\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 highest RSA alignment 0.692, metric-dependent ordering\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_cross_encoder\\n    metric: spearman_rho\\n    value: '0.692'\\n  decisions:\\n  - 'D060: added under RSA qualifier and CKA metric-dependence caveat'\\n  deprecated: false\\n- id: C380\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: best-vs-best RSA gain non-significant Delta=+0.017 3% CI includes zero\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_training_effect\\n    metric: delta_rho_best_vs_best\\n    value: '+0.017'\\n  decisions:\\n  - 'D060: marked non-significant, CI includes zero'\\n  deprecated: false\\n- id: C381\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: image tokens instruction-blind consistent with causal mask and frozen encoder\\n  type: mechanistic\\n  evidence: 50-demo L1 ablation control\\n  decisions:\\n  - 'D060: architecture-expected framing'\\n  deprecated: false\\n- id: C383\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: training effects concentrated at readout R2 +0.069\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_training_effect\\n    metric: delta_R2\\n    value: '+0.069'\\n  decisions: []\\n  deprecated: false\\n- id: C386\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: DINOv2 highest RSA rho=0.692 under RSA\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_cross_encoder\\n    metric: spearman_rho\\n    value: '0.692'\\n  decisions:\\n  - 'D060: qualified under RSA'\\n  deprecated: false\\n- id: C390\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: VLA readout R2=0.678 vs DINOv2 0.634\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_comparison\\n    metric: R2\\n  decisions: []\\n  deprecated: false\\n- id: C395\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: ablation R2 +46% p<0.0001 deep layers unaffected\\n  type: quantitative\\n  evidence:\\n  - exp_id: l1_ablation\\n    metric: delta_R2\\n  decisions: []\\n  deprecated: false\\n- id: C401\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: encoder ranking reverses under CKA, metric-dependent\\n  type: qualitative\\n  evidence:\\n  - exp_id: cka_comparison\\n  decisions:\\n  - 'D060: CKA divergence in main text'\\n  deprecated: false\\n- id: C408\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: frozen encoder confound acknowledged\\n  type: qualitative\\n  evidence: []\\n  decisions:\\n  - 'D060: added frozen encoder caveat'\\n  deprecated: false\\n- id: C416\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: L1 ablation 5 demos per task, full-scale replication in progress\\n  type: qualitative\\n  evidence: []\\n  decisions:\\n  - 'D060: acknowledged ablation scale limitation'\\n  deprecated: false\\n- id: C417\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: functional probes R2 peak L8-L13 metric-independent non-monotonic trajectory\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_layer_profile\\n    metric: R2\\n    value: 0.655-0.678 at L8-L13\\n  decisions:\\n  - 'D060-C3-fix: R2 as primary metric-independent evidence'\\n  deprecated: false\\n- id: C418\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: RSA per-layer profile and encoder rankings metric-dependent, CKA monotonically\\n    increasing\\n  type: qualitative\\n  evidence:\\n  - exp_id: cka_comparison\\n  decisions:\\n  - 'D060-C3-fix: decline phase also RSA-specific, CKA monotonic'\\n  deprecated: false\\n- id: C419\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: functional probes peak L8-L13 R2=0.655-0.678 metric-independent\\n  type: quantitative\\n  evidence:\\n  - exp_id: probe_layer_profile\\n    metric: R2\\n  decisions:\\n  - 'D060-C3-fix: R2 as primary'\\n  deprecated: false\\n- id: C420\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: CKA monotonically increasing layer profiles\\n  type: qualitative\\n  evidence:\\n  - exp_id: cka_layer_profile\\n  decisions:\\n  - 'D060-C3-fix: decline also RSA-specific'\\n  deprecated: false\\n- id: C421\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C3 contribution: non-monotonic transformation, R2 confirmed, RSA confirms\\n    but CKA diverges'\\n  type: qualitative\\n  evidence:\\n  - exp_id: probe_layer_profile\\n  - exp_id: rsa_layer_profile\\n  - exp_id: cka_layer_profile\\n  decisions:\\n  - 'D060-C3-fix: balanced metric framing'\\n  deprecated: false\\n- id: C422\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: encoder rankings and per-layer profiles metric-dependent, R2 inverted-U metric-independent\\n  type: qualitative\\n  evidence:\\n  - exp_id: cka_comparison\\n  - exp_id: probe_layer_profile\\n  decisions:\\n  - 'D060-C3-fix: CKA divergence covers both rankings and profiles'\\n  deprecated: false\\n- id: C423\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: trained image_mean RSA stable L0-L12 Delta=+0.017 n.s., decline L12-L32 Delta=-0.206\\n    p<0.0001\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_layer_profile\\n    metric: spearman_rho\\n  decisions:\\n  - 'D060-C3-fix: rise phase reframed as stable'\\n  deprecated: false\\n- id: C424\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: untrained RSA declines monotonically from L0 Delta=-0.062 to L12 p<0.0001\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_layer_profile_untrained\\n    metric: spearman_rho\\n  decisions: []\\n  deprecated: false\\n- id: C425\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: marginal RSA change at image_mean +0.017 n.s. contrasts with readout +0.074\\n    p<0.0001\\n  type: quantitative\\n  evidence:\\n  - exp_id: rsa_layer_profile\\n    metric: delta_rho_readout\\n  decisions:\\n  - 'D060-C3-fix: readout contrast added'\\n  deprecated: false\\n- id: C426\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: N=63728 observations, N/params ratio approx 0.05 for MLP probe\\n  type: quantitative\\n  evidence:\\n  - exp_id: dataset_stats\\n    metric: N_observations\\n    value: '63728'\\n  decisions: []\\n  deprecated: false\\n- id: C427\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: Probe R2 trained vs untrained FDR significant at 29-30/33 layers both positions\\n  type: quantitative\\n  evidence:\\n  - exp_id: fdr_correction\\n    metric: significant_layers_R2\\n    value: 29-30/33\\n  decisions: []\\n  deprecated: false\\n- id: C428\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: RSA FDR significant at 25/33 layers image_mean, 0/33 last_preaction due to\\n    n=10 power ceiling\\n  type: quantitative\\n  evidence:\\n  - exp_id: fdr_correction\\n    metric: significant_layers_RSA\\n    value: 25/33 image_mean, 0/33 readout\\n  decisions: []\\n  deprecated: false\\n- id: C429\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: non-monotonic profile stable under 25-demo subsampling, RSA peak unchanged\\n    L12, profile r=0.97\\n  type: quantitative\\n  evidence:\\n  - exp_id: ablation_p2_demo_sensitivity\\n    metric: profile_correlation_RSA\\n    value: '0.970'\\n  decisions: []\\n  deprecated: false\\nfigures:\\n- caption: Three similarity metrics across representation sources. \\\\textbf{(a)\\n  deprecated: false\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines (RSA values)\\n    tier: tier1\\n  - exp_id: plan_009_cka_verification\\n    metric: linear_cka + rdm_cka\\n    tier: tier1\\n  id: F001\\n  label: fig:metric_comparison\\n  location:\\n    section: appendix\\n  source_path: figures/fig6.pdf\\n  type: result\\n- caption: RSA with the action space ($\\\\rho$) across representation sources. Self-supervised\\n    DINOv2 \\\\texttt{cls\\\\_token\\n  deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: baselines + trained/untrained peaks\\n    tier: tier1\\n  - exp_id: plan_013_branch_split\\n    metric: fused_2176d_rsa=0.634\\n    tier: tier1\\n  id: F002\\n  label: fig:rsa_bar\\n  location:\\n    section: experiments\\n  source_path: figures/fig2.pdf\\n  type: result\\n- caption: 'Per-layer RSA ($\\\\rho$) with the action space across all 32 LLM layers.\\n    Trained image\\\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\\\to$ L12 $=\\n    0.628$ (peak, above Projector $0.615$) $\\\\to$ L32 $= 0.422$. Untrained image\\\\_mean\\n    (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2\\n    cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).'\\n  deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: per-layer RSA trained/untrained image_mean (32 layers)\\n    tier: tier1\\n  id: F003\\n  label: fig:layer_curves\\n  location:\\n    section: experiments\\n  source_path: figures/fig3.pdf\\n  type: result\\n- caption: Functional probe $R^2$ for action prediction (best layer for each source).\\n    Both trained readout ($R^2{=\\n  deprecated: true\\n  evidence:\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: peak R2 values (trained img_mean L8, readout L13)\\n    tier: tier1\\n  - exp_id: plan_012_clip_vit_control\\n    metric: projector/dino/clip R2\\n    tier: tier1\\n  id: F004\\n  label: fig:probe_bars\\n  location:\\n    section: experiments\\n  source_path: figures/fig4.pdf\\n  type: result\\n- caption: \\\\textbf{(a)\\n  deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: trained vs untrained per-layer RSA + instruction conditions\\n    tier: tier1\\n  - exp_id: plan_008_random_inst_control\\n    metric: instruction invariance\\n    tier: tier1\\n  id: F005\\n  label: fig:factorial\\n  location:\\n    section: experiments\\n  source_path: figures/fig5.pdf\\n  type: result\\n- id: F006\\n  location:\\n    section: appendix\\n    figure_number: 0\\n  caption: ''\\n  type: other\\n  source: {}\\n  output_path: ''\\n  deprecated: false\\n- id: F007\\n  location:\\n    section: appendix\\n    figure_number: 0\\n  caption: ''\\n  type: other\\n  source: {}\\n  output_path: ''\\n  deprecated: false\\npaper:\\n  generated_at: '2026-05-17T22:15:14.113705+00:00'\\n  source: auto-bootstrap from existing tex files\\n  title: Formatting Instructions for CoRL 2026 Camera-Ready\\n  version: 51\\ntables:\\n- caption: Geometric (RSA $\\\\rho$) and functional (probe $R^2$) alignment with the\\n    action space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both\\n    trained readout and image\\\\_mean exceed the projector in $R^2$, confirming the\\n    inverted-U extends to functional capacity. VLA rows show peak-layer values (RSA/R$^2$\\n    peaks listed separately when they differ). 95\\\\% CIs from 10{,\\n  cells: []\\n  deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: all RSA peaks + baselines\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: all R2 peaks\\n    tier: tier1\\n  - exp_id: plan_012_clip_vit_control\\n    metric: projector/dino/clip R2\\n    tier: tier1\\n  id: T001\\n  label: tab:rsa_overview\\n  location:\\n    section: experiments\\n- caption: Training effects on action-relevant structure (bootstrap, 10{,\\n  cells: []\\n  deprecated: true\\n  evidence:\\n  - exp_id: d041_method_b_rsa\\n    metric: bootstrap_best_vs_best + same_layer comparisons\\n    tier: tier1\\n  - exp_id: plan_011_fulllayer_r2\\n    metric: bootstrap_best_vs_best R2\\n    tier: tier1\\n  id: T002\\n  label: tab:training_effects\\n  location:\\n    section: experiments\\n_completeness:\\n  coverage: 69/74\\n  claims: 71\\n  tables: 0\\n  figures: 3\\n  tier_counts:\\n    tier1: 0\\n    tier2: 69\\n    tier3: 5\\n    tierX: 0\\n  last_checked: '2026-05-17T22:15:14.113771+00:00'\\n\", \"total_chars\": 51898, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "c1eb304f-58ed-4665-a53d-91a4d1ecaf19",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/da042411-baa9-4148-b88d-99c95c45f67d/tool-results/toolu_01CrPZRnZp85eE6j3pZ5GRg7.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml\\\", \\\"content\\\": \\\"claims:\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915\\\\n    tier: tier1\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: post_projector_4096d_rsa=0.615\\\\n    tier: tier1\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.clip_cls=0.557\\\\n    tier: tier1\\\\n  id: C001\\\\n  location:\\\\n    context: result_statement\\\\n    section: abstract\\\\n  text: 'First, self-supervised pretraining provides the strongest action-relevant\\\\n    geometry: standalone DINOv2 achieves RSA $ = 0.692$, exceeding all VL-pretrained\\\\n    encoders (DinoSigLIP+Projector $ = 0.615$; CL'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained_image_mean_peak.rsa=0.6282\\\\n    tier: tier1\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: untrained_image_mean_peak.rsa=0.6117\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\\\n    tier: tier1\\\\n  id: C002\\\\n  location:\\\\n    context: result_statement\\\\n    section: abstract\\\\n  text: 'Second, the LLM applies a non-monotonic transformation---the first 12 layers\\\\n    enhance geometric alignment with the action space above the vision encoder input\\\\n    ($$: $0.612  0.628$ at L12), while the rem'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017,significant=false\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686,p=0.0001\\\\n    tier: tier1\\\\n  id: C003\\\\n  location:\\\\n    context: result_statement\\\\n    section: abstract\\\\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\\\\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\\\\n    capacity (R^2 Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence: llama2base_action_probe experiment\\\\n  id: C004\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: 'Linear CKA~kornblith2019 reverses the RSA ordering: untrained LLM ($CKA =\\\\n    0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2\\\\n    ($0.066$), partially inverting the self-superv'\\\\n  type: quantitative\\\\n  decisions: []\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: plan_009_cka_verification\\\\n    metric: rdm_cka.*\\\\n    tier: tier1\\\\n  id: C005\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: 'RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $$\\\\n    Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).'\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: plan_009_cka_verification\\\\n    metric: linear_cka per-layer (derived from full scan)\\\\n    tier: tier2\\\\n  id: C006\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: At the per-layer level, linear CKA between image\\\\\\\\_mean and the action space\\\\n    rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U\\\\n    pattern.\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.*\\\\n    tier: tier1\\\\n  - exp_id: plan_009_cka_verification\\\\n    metric: linear_cka.* + rdm_cka.*\\\\n    tier: tier1\\\\n  id: C007\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: 'Three similarity metrics across representation sources. (a)~RSA ranks DINOv2\\\\n    cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). (b)~Linear CKA reverses\\\\n    the ordering: Untrained ($0.089$) $>$ Tr'\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: fused_2176d_rsa=0.634\\\\n    tier: tier1\\\\n  id: C008\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: Fusion produces a representation ($ = 0.634$) that exceeds either branch alone,\\\\n    indicating that concatenation captures complementary structure.\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: fused_2176d_rsa=0.634, post_projector_4096d_rsa=0.615\\\\n    tier: tier1\\\\n  id: C009\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: 'The MLP projector then compresses this signal: DinoSigLIP+Projector achieves\\\\n    $ = 0.615$, a drop of $ = 0.019$ from the fused 2{,176-D input.'\\\\n  type: quantitative\\\\n- deprecated: false\\\\n  evidence:\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: standalone_dino_patch_mean_rsa=0.631\\\\n    tier: tier1\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_patch_mean=0.6307\\\\n    tier: tier1\\\\n  id: C010\\\\n  location:\\\\n    context: result_statement\\\\n    section: appendix\\\\n  text: DINOv2 patch\\\\\\\\_mean achieves RSA $ = 0.631$, between the cls\\\\\\\\_token ($0.692$)\\\\n    and the fused DinoSigLIP ($0.634$).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915, trained_image_mean_peak\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\\\n    tier: tier1\\\\n  id: C011\\\\n  location:\\\\n    context: result_statement\\\\n    section: conclusion\\\\n  text: 'Three findings emerge: (1)~the frozen vision encoder provides the dominant\\\\n    action-relevant geometry, with self-supervised DINOv2 achieving the highest alignment\\\\n    ($ = 0.692$) exceeding all VL-pretraine'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915\\\\n    tier: tier1\\\\n  id: C012\\\\n  location:\\\\n    context: result_statement\\\\n    section: discussion\\\\n  text: 'The vision encoder is the source: self-supervised DINOv2 achieves the highest\\\\n    geometric alignment ($ = 0.692$), exceeding all VLA internal representations.'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.image_mean.p=0.006\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686\\\\n    tier: tier1\\\\n  id: C013\\\\n  location:\\\\n    context: result_statement\\\\n    section: discussion\\\\n  text: 'Training redistributes geometry but enhances decodability: modest geometric\\\\n    gain (Delta = 0.017--0.023, 3--4% of baseline across two benchmarks), while substantially\\\\n    improving R^2 (Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.significant=false\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  id: C014\\\\n  location:\\\\n    context: result_statement\\\\n    section: discussion\\\\n  text: Cross-benchmark replication (LIBERO-Spatial Delta = 0.023, p < 0.001) suggests\\\\n    the LIBERO-Goal RSA CI (incl. zero) reflects limited power rather than a true\\\\n    null, but the effect remains small (3--4% of baseline).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915\\\\n    tier: tier1\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: fused_2176d_rsa=0.634, standalone_dino_patch_mean_rsa=0.631\\\\n    tier: tier1\\\\n  id: C015\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: The standalone DINOv2 cls\\\\\\\\_token achieves the highest alignment of any representation\\\\n    source ($ = 0.692$), followed by the fused DinoSigLIP 2{,176-D representation\\\\n    before projection ($ = 0.634$) and t\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.clip_cls=0.557\\\\n    tier: tier1\\\\n  id: C016\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: CLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment\\\\n    among pretrained encoders ($ = 0.557$; Figure~fig:rsa_bar).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557, trained_image_mean_peak.rsa=0.6282\\\\n    tier: tier1\\\\n  id: C017\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: DINOv2, pretrained with self-supervised objectives alone, achieves $ = 0.692$---exceeding\\\\n    not only CLIP ($ = 0.557$) but also the VLA's own internal representations at\\\\n    their peaks (trained image\\\\\\\\_mean\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\\\\n    tier: tier1\\\\n  - exp_id: unified_action_probe\\\\n    metric: bootstrap_pairwise.projector_vs_dino.p=0.557\\\\n    tier: tier1\\\\n  id: C018\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'Functional probes corroborate the ranking: DINOv2 cls\\\\\\\\_token achieves $R^2\\\\n    = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$,\\\\n    $p = 0.557$, n.s.), while CLIP yields the'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: dinov2_branch_rsa=0.619, siglip_branch_rsa=0.621\\\\n    tier: tier1\\\\n  id: C019\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: The DINOv2 (1{,024-D) and SigLIP (1{,152-D) branches yield near-identical\\\\n    RSA ($0.619$ vs.\\\\\\\\ $0.621$); fusion exceeds either ($0.634$), while the projector\\\\n    introduces modest compression loss ($0.634  0\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: all RSA values\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: all R2 peak values\\\\n    tier: tier1\\\\n  id: C020\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Geometric (RSA $$) and functional (probe $R^2$) alignment with the action\\\\n    space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both trained\\\\n    readout and image\\\\\\\\_mean exceed the projector in\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines + trained_image_mean_peak\\\\n    tier: tier1\\\\n  id: C021\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'RSA with the action space ($$) across representation sources. Self-supervised\\\\n    DINOv2 cls\\\\\\\\_token ($=0.692$) achieves the highest geometric alignment, followed\\\\n    by fused DinoSigLIP ($0.634$) and the VLA '\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained_image_mean per-layer RSA (L0=0.612, L12=0.628, L32=0.422)\\\\n    tier: tier1\\\\n  id: C022\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'Figure~fig:layer_curves reveals a non-monotonic trajectory for trained image\\\\\\\\_mean\\\\n    RSA: $$ begins at $0.612$ (L0, equal to the projector input), rises to a peak\\\\n    of $0.628$ at L12---above the DinoSigLI'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_image_mean_peak.layer=8, mean_R2=0.6553\\\\n    tier: tier1\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: projector_mean_R2=0.6298\\\\n    tier: tier1\\\\n  id: C023\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Full-layer probe scans reveal that trained image\\\\\\\\_mean $R^2$ peaks at L8 ($0.655$),\\\\n    exceeding the projector ($0.630$, $ = +0.025$; Table~tab:rsa_overview).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_image_mean_peak.layer=8\\\\n    tier: tier1\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained_image_mean_peak.layer=12\\\\n    tier: tier1\\\\n  id: C024\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: The $R^2$ peak (L8) precedes the RSA peak (L12) by four layers, suggesting\\\\n    that functional decodability peaks earlier than geometric alignment; we adopt\\\\n    ``early-to-middle layers (L8--L13)'' to capture\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained_last_preaction_peak.rsa=0.6425, layer=12\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_last_preaction_peak.mean_R2=0.6779, layer=13\\\\n    tier: tier1\\\\n  id: C025\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Trained readout achieves peak RSA $ = 0.643$ at L12 and probe $R^2 = 0.678$\\\\n    (L13), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $ = 0.048$; Table~tab:rsa_overview,\\\\n    Figure~fig:probe_bars).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained per-layer RSA L12=0.628→L32=0.422; untrained 0.612→0.545\\\\n    tier: tier1\\\\n  id: C026\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'The decline from L12 to L32 ($$: $0.628  0.422$) exceeds the untrained decay\\\\n    ($0.612  0.545$), indicating that training actively redirects later layers away\\\\n    from action geometry, yielding a three-phas'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_last_preaction_peak=0.6779, trained_image_mean_peak=0.6553\\\\n    tier: tier1\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: projector_mean_R2=0.6298, dino_cls_mean_R2=0.6343\\\\n    tier: tier1\\\\n  id: C027\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Functional probe $R^2$ for action prediction (best layer for each source).\\\\n    Both trained readout ($R^2{=0.678$, L13) and trained image\\\\\\\\_mean ($0.655$, L8)\\\\n    exceed the projector baseline ($0.630$), confi\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  id: C028\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: best-vs-best Delta = +0.017 (3% of baseline; LIBERO-Spatial confirms with\\\\n    Delta = +0.023, 4%, p < 0.001). This geometric gain is far smaller than the functional\\\\n    improvement.\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\\\n    tier: tier1\\\\n  id: C029\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: RSA best-vs-best yields at most a modest gain (Delta = 0.017--0.023, 3--4%\\\\n    of baseline across two benchmarks), while R^2 shows substantially larger improvements.\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006; last_preaction.delta=0.0686,p=0.0001\\\\n    tier: tier1\\\\n  id: C030\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Yet $R^2$ best-vs-best is significant for both image\\\\\\\\_mean ($ = +0.015$, $p\\\\n    = 0.006$) and readout ($ = +0.069$, $p < 0.0001$; Table~tab:training_effects).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_same_layer.last_preaction_L13.note (untrained L13 R2 near -0.33)\\\\n    tier: tier1\\\\n  id: C031\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Untrained readout $R^2$ reaches $ -0.33$ at L12--L29 (predictions worse than\\\\n    a constant-mean baseline), while untrained image\\\\\\\\_mean $R^2$ drops to near-zero\\\\n    at L10--L13.\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best + same_layer\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best\\\\n    tier: tier1\\\\n  id: C032\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'Training effects on action-relevant structure (LIBERO-Goal; bootstrap). RSA\\\\n    best-vs-best yields modest geometric gain (Delta=+0.017, 3%; LIBERO-Spatial: +0.023,\\\\n    p<0.001), while R^2 shows substantially larger functional gains.'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: instruction_effect (derived from trained_with_inst vs trained_no_inst)\\\\n    tier: tier1\\\\n  - exp_id: plan_008_random_inst_control\\\\n    metric: max_absolute_delta=0.0165, instruction_invariant=true\\\\n    tier: tier1\\\\n  id: C033\\\\n  location:\\\\n    context: finding_statement\\\\n    section: experiments\\\\n  text: This confirms that the action geometry is visually grounded and instruction-independent~grant2026.\\\\n  type: methodological\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: experimental design (2x2 factorial)\\\\n    tier: tier2\\\\n  id: C034\\\\n  location:\\\\n    context: result_statement\\\\n    section: introduction\\\\n  text: We cross training status (trained vs.\\\\\\\\ untrained, reinitializing 6.74B LLM\\\\n    parameters) with instruction presence in a $2 2$ factorial design, and quantify\\\\n    action-relevant structure using RSA~kriegesko\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557\\\\n    tier: tier1\\\\n  id: C035\\\\n  location:\\\\n    context: result_statement\\\\n    section: introduction\\\\n  text: Standalone DINOv2 achieves the highest action-space alignment (RSA $ = 0.692$),\\\\n    far exceeding CLIP ($ = 0.557$) and the VLA's own peak internal representation\\\\n    ($ = 0.628$ at L12).\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\\\\n    tier: tier1\\\\n  id: C036\\\\n  location:\\\\n    context: result_statement\\\\n    section: introduction\\\\n  text: 'Functional probes corroborate this ranking: DINOv2 ($R^2 = 0.634$) $$ Projector\\\\n    ($0.630$) $>$ CLIP ($0.587$).'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained_image_mean_peak.rsa=0.6282\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: trained_last_preaction_peak.mean_R2=0.6779\\\\n    tier: tier1\\\\n  id: C037\\\\n  location:\\\\n    context: result_statement\\\\n    section: introduction\\\\n  text: 'Second, the LLM applies a non-monotonic transformation: the first 12 layers\\\\n    enhance geometric alignment above the vision encoder input ($$: $0.612  0.628$),\\\\n    while the remaining 20 layers degrade it ($'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: methodology (encoder extraction)\\\\n    tier: tier2\\\\n  id: C038\\\\n  location:\\\\n    context: bold\\\\n    section: method\\\\n  text: DINOv2 ViT-L/14\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: methodology (CLIP extraction)\\\\n    tier: tier2\\\\n  id: C039\\\\n  location:\\\\n    context: bold\\\\n    section: method\\\\n  text: CLIP ViT-L/14\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\\\\n    tier: tier1\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\\\\n    tier: tier1\\\\n  id: C040\\\\n  location:\\\\n    context: result_statement\\\\n    section: introduction\\\\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\\\\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\\\\n    capacity---redistribution dominates over creation.\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: rsa.trained_image_mean_peak(layer=14,rsa=0.691), action_probe.trained_image_mean_peak(layer=13,R2=0.696)\\\\n    tier: tier1\\\\n  id: C041\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: 'Cross-benchmark validation (LIBERO-Spatial): inverted-U replicates, trained\\\\n    image_mean RSA peaks at L14 (rho=0.691), R^2 at L13 (0.696), peak shifting ~2\\\\n    layers deeper than LIBERO-Goal.'\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,ci_95=[0.012,0.036],p=0.001\\\\n    tier: tier1\\\\n  id: C042\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: Training produces a significant geometric gain on LIBERO-Spatial (best-vs-best\\\\n    Delta=+0.023, p<0.001), confirming LIBERO-Goal effect reflects limited power.\\\\n  type: quantitative\\\\n- deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_010_libero_spatial\\\\n    metric: rsa.trained_last_preaction_peak(layer=15), action_probe.trained_last_preaction_peak(layer=21)\\\\n    tier: tier1\\\\n  id: C043\\\\n  location:\\\\n    context: result_statement\\\\n    section: experiments\\\\n  text: RSA--R^2 peak convergence does not replicate on LIBERO-Spatial (RSA L15 vs\\\\n    R^2 L21, 6-layer gap vs 1 on Goal), suggesting peak alignment may be benchmark-specific.\\\\n  type: quantitative\\\\n- id: C044\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Image tokens encode purely visual information (instruction classification\\\\n    at chance, 10%, across all layers)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: image_mean_accuracy\\\\n    value: 10%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C046\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Readout token: 100% instruction classification from L1, LOOCV-verified'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: readout_accuracy\\\\n    value: 100%\\\\n  - exp_id: loocv_validation\\\\n    metric: accuracy\\\\n    value: 100% ± 0.00\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C049\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 25/32 attention heads flip to instruction-dominant (58% attention to ~8% of\\\\n    sequence)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: instruction_dominant_heads\\\\n    value: 25/32\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: instruction_attention_fraction\\\\n    value: 58%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C053\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Untrained incidental routing decays to 82%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: untrained_L31_accuracy\\\\n    value: 82%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C058\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSA peaks at L12, probe R² peaks at L8-L13\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_per_layer\\\\n    metric: trained_image_mean_peak\\\\n    value: L12, rho=0.628\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C064\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 highest geometric foundation (rho=0.692)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_encoder_comparison\\\\n    metric: dinov2_cls_rsa\\\\n    value: '0.692'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C071\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Training reshapes readout-token integration (routing +18pp, attention +46pp)\\\\n    rather than visual representations (Delta <= 1.7%)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_summary\\\\n    metric: routing_delta\\\\n    value: +18pp\\\\n  - exp_id: training_effect_summary\\\\n    metric: attention_delta\\\\n    value: +46pp\\\\n  - exp_id: training_effect_summary\\\\n    metric: image_mean_rsa_delta\\\\n    value: '+0.017'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C072\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Image tokens: instruction classification at chance (10%) across all 32 layers'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: image_mean_accuracy\\\\n    value: 10%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C074\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Readout token: 100% instruction identity from L1, LOOCV-verified'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: readout_accuracy\\\\n    value: 100%\\\\n  - exp_id: loocv_validation\\\\n    metric: accuracy\\\\n    value: 100%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C077\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 25/32 heads flip to instruction-dominant (58% attention)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: instruction_dominant_heads\\\\n    value: 25/32\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C081\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Untrained routing decays to 82% by L31\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: untrained_L31_accuracy\\\\n    value: 82%\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C086\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 RSA rho=0.692\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_encoder_comparison\\\\n    metric: dinov2_cls_rsa\\\\n    value: '0.692'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C092\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Inverted-U peak rho=0.628 at L12, 0.422 at L32\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_per_layer\\\\n    metric: trained_image_mean_L12\\\\n    value: '0.628'\\\\n  - exp_id: rsa_per_layer\\\\n    metric: trained_image_mean_L32\\\\n    value: '0.422'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C099\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Training geometric gain Delta=0.017-0.023, 3-4%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_comparison\\\\n    metric: rsa_best_vs_best\\\\n    value: +0.017 (Goal), +0.023 (Spatial)\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C107\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Readout R2 Delta=+0.069, p<0.0001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_comparison\\\\n    metric: readout_r2_delta\\\\n    value: '+0.069'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C108\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Image_mean instruction classification at chance (10%) across all 32 layers\\\\n  type: quantitative\\\\n  evidence: 50-demo L1 ablation multi-layer comparison\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C110\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Trained readout 100% L1-L31, LOOCV 100% +/- 0.00\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: readout_accuracy\\\\n    value: 100%\\\\n  - exp_id: loocv_validation\\\\n    metric: accuracy\\\\n    value: 100%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C113\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Untrained readout decays: L8 95.5%, L31 82%'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: untrained_L8\\\\n    value: 95.5%\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: untrained_L31\\\\n    value: 82%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C117\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Instruction invariance: max |Delta| = 0.006'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: factorial_analysis\\\\n    metric: instruction_effect\\\\n    value: '0.006'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C122\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'QA probe: trained 86.3% (L20), DINOv2 82.7%'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: qa_probe\\\\n    metric: trained_accuracy\\\\n    value: 86.3%\\\\n  - exp_id: qa_probe\\\\n    metric: dinov2_accuracy\\\\n    value: 82.7%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C128\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Trained L1: 25/32 heads instruction-dominant, 58% attention to instruction,\\\\n    20.9% to image'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: instruction_dominant_heads\\\\n    value: 25/32\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: instruction_attention\\\\n    value: 58%\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: image_attention\\\\n    value: 20.9%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C135\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Untrained L1: 0/32 heads instruction-dominant, 87.8% image, 11.7% instruction'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: untrained_heads\\\\n    value: 0/32\\\\n  - exp_id: l1_attention_pattern\\\\n    metric: untrained_image_attention\\\\n    value: 87.8%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C143\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Training effect asymmetry: attention +46pp, routing +18pp, R2 +0.069, but\\\\n    image_mean Delta<=1.7%'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_summary\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C152\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 cls RSA rho=0.692, highest alignment\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_encoder_comparison\\\\n    metric: dinov2_cls\\\\n    value: '0.692'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C162\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: CLIP RSA rho=0.557\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_encoder_comparison\\\\n    metric: clip_patch_mean\\\\n    value: '0.557'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C173\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Inverted-U: L0=0.612, L12=0.628, L32=0.422'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_per_layer\\\\n    metric: trained_image_mean\\\\n    value: L0=0.612, L12=0.628, L32=0.422\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C185\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: R2 peak L8-L10 (0.655 +/- 0.002)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_per_layer\\\\n    metric: trained_image_mean_peak\\\\n    value: '0.655'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C198\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Readout R2=0.678 (L13), exceeds projector by 0.048\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_comparison\\\\n    metric: readout_r2\\\\n    value: '0.678'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C212\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSA best-vs-best Delta=+0.017, same-layer +0.079\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_comparison\\\\n    metric: rsa_best_vs_best\\\\n    value: '+0.017'\\\\n  - exp_id: training_effect_comparison\\\\n    metric: same_layer_L12\\\\n    value: '+0.079'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C227\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'R2 best-vs-best: image_mean +0.015 (p=0.006), readout +0.069 (p<0.0001)'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_comparison\\\\n    metric: image_mean_delta\\\\n    value: '+0.015'\\\\n  - exp_id: probe_comparison\\\\n    metric: readout_delta\\\\n    value: '+0.069'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C243\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Untrained pathological: L10-L11 R2=-0.33, -0.28'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_per_layer\\\\n    metric: untrained_L10_L11\\\\n    value: -0.33, -0.28\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C260\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'LIBERO-Spatial: RSA peak L14 (0.691), R2 peak L13 (0.696), Delta=+0.023 p<0.001'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: libero_spatial\\\\n    metric: rsa_peak\\\\n    value: L14, 0.691\\\\n  - exp_id: libero_spatial\\\\n    metric: r2_peak\\\\n    value: L13, 0.696\\\\n  - exp_id: libero_spatial\\\\n    metric: training_delta\\\\n    value: '+0.023'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C278\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Robustness: RSA profile r=0.970 under halved demos'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: demo_sensitivity\\\\n    metric: rsa_profile_correlation\\\\n    value: '0.970'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C279\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Training effects: routing +18pp, attention +46pp, R2 +0.069; image_mean Delta<=1.7%'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_summary\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C281\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Instruction invariance |Delta| < 0.006\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: factorial_analysis\\\\n    metric: instruction_effect\\\\n    value: '0.006'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C284\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LIBERO-Spatial Delta=0.023, p<0.001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: libero_spatial\\\\n    metric: training_delta\\\\n    value: '+0.023'\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C285\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Image tokens: instruction classification at chance across all layers'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C287\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Readout token: 100% from L1, LOOCV-verified'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n  - exp_id: loocv_validation\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C290\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 25/32 heads flip to instruction-dominant (58%)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_attention_pattern\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C294\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Untrained decays to 82%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: untrained_L31\\\\n    value: 82%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C299\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSA inverted-U peak L12, R2 L8-L13, DINOv2 rho=0.692\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_per_layer\\\\n  - exp_id: rsa_encoder_comparison\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C305\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Training: R2 +0.069 readout, Delta<=1.7% image_mean'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: training_effect_summary\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C306\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: image tokens instruction-blind at chance 10% across all layers and conditions\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: accuracy\\\\n    value: 10%\\\\n  decisions:\\\\n  - 'D060: reframed as architecture-expected verification'\\\\n  deprecated: false\\\\n- id: C308\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: readout token 100% instruction classification from L1, cross-validated\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe_loocv\\\\n    metric: accuracy\\\\n    value: 100%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C311\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'VLA training shifts to entry-layer routing L0-L1: 21-25 heads with exit-layer\\\\n    L31: 18 heads'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: attention_analysis\\\\n    metric: instruction_dominant_heads\\\\n    value: 25/32 at L1, 18/32 at L31\\\\n  decisions:\\\\n  - 'D060: C2 anchor claim'\\\\n  deprecated: false\\\\n- id: C315\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: immediate instruction access 99.6% at L1 vs pretrained 80.2%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: L1_accuracy\\\\n    value: 99.6% vs 80.2%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C320\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: under RSA peak rho=0.628 at L12 declining to 0.422 at L32\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_layer_profile\\\\n    metric: spearman_rho\\\\n    value: 0.628 L12, 0.422 L32\\\\n  decisions:\\\\n  - 'D060: qualified with under RSA'\\\\n  deprecated: false\\\\n- id: C326\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 highest geometric alignment rho=0.692, metric-dependent\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_cross_encoder\\\\n    metric: spearman_rho\\\\n    value: '0.692'\\\\n  decisions:\\\\n  - 'D060: added metric-dependence caveat'\\\\n  deprecated: false\\\\n- id: C333\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: training effect Delta rho <= 0.017 non-significant\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_training_effect\\\\n    metric: delta_rho\\\\n    value: '0.017'\\\\n  decisions:\\\\n  - 'D060: marked non-significant'\\\\n  deprecated: false\\\\n- id: C341\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: readout token probe R2 +0.069, instruction attention +46pp\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_training_effect\\\\n    metric: delta_R2\\\\n    value: '+0.069'\\\\n  - exp_id: attention_analysis\\\\n    metric: delta_text_attention\\\\n    value: +46pp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C342\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: image tokens instruction-blind 10% across all 32 layers, architecture-expected\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: accuracy\\\\n    value: 10%\\\\n  decisions:\\\\n  - 'D060: reframed as architecture-expected'\\\\n  deprecated: false\\\\n- id: C344\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: readout token 100% cross-validated from L1\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe_loocv\\\\n    metric: accuracy\\\\n    value: 100%\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C347\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'VLA training shifts to entry-exit pattern L0-L1: 21-25 heads, L31: 18 heads'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: attention_analysis\\\\n    metric: instruction_dominant_heads\\\\n  decisions:\\\\n  - 'D060: C2 anchor'\\\\n  deprecated: false\\\\n- id: C351\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 99.6% at L1 vs pretrained 80.2%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: L1_accuracy\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C356\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: under RSA alignment peaks L12 rho=0.628, declines to 0.422 at L32\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_layer_profile\\\\n    metric: spearman_rho\\\\n  decisions:\\\\n  - 'D060: qualified under RSA'\\\\n  deprecated: false\\\\n- id: C362\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 highest geometric alignment rho=0.692, ordering partially reverses\\\\n    under CKA\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_cross_encoder\\\\n    metric: spearman_rho\\\\n    value: '0.692'\\\\n  decisions:\\\\n  - 'D060: CKA caveat added'\\\\n  deprecated: false\\\\n- id: C369\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: non-significant geometric gain Delta rho=0.017 3%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_training_effect\\\\n    metric: delta_rho\\\\n    value: '0.017'\\\\n  decisions:\\\\n  - 'D060: marked non-significant'\\\\n  deprecated: false\\\\n- id: C377\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: readout R2 Delta=+0.069 p<0.0001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_training_effect\\\\n    metric: delta_R2\\\\n    value: '+0.069'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C378\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: image token instruction-blindness consistent with causal mask and frozen encoder\\\\n  type: mechanistic\\\\n  evidence:\\\\n  - exp_id: cross_instruction_probe\\\\n    metric: accuracy\\\\n    value: 10%\\\\n  decisions:\\\\n  - 'D060: acknowledge causal mask as structural source'\\\\n  deprecated: false\\\\n- id: C379\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 highest RSA alignment 0.692, metric-dependent ordering\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_cross_encoder\\\\n    metric: spearman_rho\\\\n    value: '0.692'\\\\n  decisions:\\\\n  - 'D060: added under RSA qualifier and CKA metric-dependence caveat'\\\\n  deprecated: false\\\\n- id: C380\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: best-vs-best RSA gain non-significant Delta=+0.017 3% CI includes zero\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_training_effect\\\\n    metric: delta_rho_best_vs_best\\\\n    value: '+0.017'\\\\n  decisions:\\\\n  - 'D060: marked non-significant, CI includes zero'\\\\n  deprecated: false\\\\n- id: C381\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: image tokens instruction-blind consistent with causal mask and frozen encoder\\\\n  type: mechanistic\\\\n  evidence: 50-demo L1 ablation control\\\\n  decisions:\\\\n  - 'D060: architecture-expected framing'\\\\n  deprecated: false\\\\n- id: C383\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: training effects concentrated at readout R2 +0.069\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_training_effect\\\\n    metric: delta_R2\\\\n    value: '+0.069'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C386\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: DINOv2 highest RSA rho=0.692 under RSA\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_cross_encoder\\\\n    metric: spearman_rho\\\\n    value: '0.692'\\\\n  decisions:\\\\n  - 'D060: qualified under RSA'\\\\n  deprecated: false\\\\n- id: C390\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: VLA readout R2=0.678 vs DINOv2 0.634\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_comparison\\\\n    metric: R2\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C395\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: ablation R2 +46% p<0.0001 deep layers unaffected\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: l1_ablation\\\\n    metric: delta_R2\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C401\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: encoder ranking reverses under CKA, metric-dependent\\\\n  type: qualitative\\\\n  evidence:\\\\n  - exp_id: cka_comparison\\\\n  decisions:\\\\n  - 'D060: CKA divergence in main text'\\\\n  deprecated: false\\\\n- id: C408\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: frozen encoder confound acknowledged\\\\n  type: qualitative\\\\n  evidence: []\\\\n  decisions:\\\\n  - 'D060: added frozen encoder caveat'\\\\n  deprecated: false\\\\n- id: C416\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: L1 ablation 5 demos per task, full-scale replication in progress\\\\n  type: qualitative\\\\n  evidence: []\\\\n  decisions:\\\\n  - 'D060: acknowledged ablation scale limitation'\\\\n  deprecated: false\\\\n- id: C417\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: functional probes R2 peak L8-L13 metric-independent non-monotonic trajectory\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_layer_profile\\\\n    metric: R2\\\\n    value: 0.655-0.678 at L8-L13\\\\n  decisions:\\\\n  - 'D060-C3-fix: R2 as primary metric-independent evidence'\\\\n  deprecated: false\\\\n- id: C418\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSA per-layer profile and encoder rankings metric-dependent, CKA monotonically\\\\n    increasing\\\\n  type: qualitative\\\\n  evidence:\\\\n  - exp_id: cka_comparison\\\\n  decisions:\\\\n  - 'D060-C3-fix: decline phase also RSA-specific, CKA monotonic'\\\\n  deprecated: false\\\\n- id: C419\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: functional probes peak L8-L13 R2=0.655-0.678 metric-independent\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: probe_layer_profile\\\\n    metric: R2\\\\n  decisions:\\\\n  - 'D060-C3-fix: R2 as primary'\\\\n  deprecated: false\\\\n- id: C420\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: CKA monotonically increasing layer profiles\\\\n  type: qualitative\\\\n  evidence:\\\\n  - exp_id: cka_layer_profile\\\\n  decisions:\\\\n  - 'D060-C3-fix: decline also RSA-specific'\\\\n  deprecated: false\\\\n- id: C421\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'C3 contribution: non-monotonic transformation, R2 confirmed, RSA confirms\\\\n    but CKA diverges'\\\\n  type: qualitative\\\\n  evidence:\\\\n  - exp_id: probe_layer_profile\\\\n  - exp_id: rsa_layer_profile\\\\n  - exp_id: cka_layer_profile\\\\n  decisions:\\\\n  - 'D060-C3-fix: balanced metric framing'\\\\n  deprecated: false\\\\n- id: C422\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: encoder rankings and per-layer profiles metric-dependent, R2 inverted-U metric-independent\\\\n  type: qualitative\\\\n  evidence:\\\\n  - exp_id: cka_comparison\\\\n  - exp_id: probe_layer_profile\\\\n  decisions:\\\\n  - 'D060-C3-fix: CKA divergence covers both rankings and profiles'\\\\n  deprecated: false\\\\n- id: C423\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: trained image_mean RSA stable L0-L12 Delta=+0.017 n.s., decline L12-L32 Delta=-0.206\\\\n    p<0.0001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_layer_profile\\\\n    metric: spearman_rho\\\\n  decisions:\\\\n  - 'D060-C3-fix: rise phase reframed as stable'\\\\n  deprecated: false\\\\n- id: C424\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: untrained RSA declines monotonically from L0 Delta=-0.062 to L12 p<0.0001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_layer_profile_untrained\\\\n    metric: spearman_rho\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C425\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: marginal RSA change at image_mean +0.017 n.s. contrasts with readout +0.074\\\\n    p<0.0001\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: rsa_layer_profile\\\\n    metric: delta_rho_readout\\\\n  decisions:\\\\n  - 'D060-C3-fix: readout contrast added'\\\\n  deprecated: false\\\\n- id: C426\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: N=63728 observations, N/params ratio approx 0.05 for MLP probe\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: dataset_stats\\\\n    metric: N_observations\\\\n    value: '63728'\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C427\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Probe R2 trained vs untrained FDR significant at 29-30/33 layers both positions\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: fdr_correction\\\\n    metric: significant_layers_R2\\\\n    value: 29-30/33\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C428\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSA FDR significant at 25/33 layers image_mean, 0/33 last_preaction due to\\\\n    n=10 power ceiling\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: fdr_correction\\\\n    metric: significant_layers_RSA\\\\n    value: 25/33 image_mean, 0/33 readout\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C429\\\\n  location:\\\\n    section: experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: non-monotonic profile stable under 25-demo subsampling, RSA peak unchanged\\\\n    L12, profile r=0.97\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: ablation_p2_demo_sensitivity\\\\n    metric: profile_correlation_RSA\\\\n    value: '0.970'\\\\n  decisions: []\\\\n  deprecated: false\\\\nfigures:\\\\n- caption: Three similarity metrics across representation sources. \\\\\\\\textbf{(a)\\\\n  deprecated: false\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines (RSA values)\\\\n    tier: tier1\\\\n  - exp_id: plan_009_cka_verification\\\\n    metric: linear_cka + rdm_cka\\\\n    tier: tier1\\\\n  id: F001\\\\n  label: fig:metric_comparison\\\\n  location:\\\\n    section: appendix\\\\n  source_path: figures/fig6.pdf\\\\n  type: result\\\\n- caption: RSA with the action space ($\\\\\\\\rho$) across representation sources. Self-supervised\\\\n    DINOv2 \\\\\\\\texttt{cls\\\\\\\\_token\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: baselines + trained/untrained peaks\\\\n    tier: tier1\\\\n  - exp_id: plan_013_branch_split\\\\n    metric: fused_2176d_rsa=0.634\\\\n    tier: tier1\\\\n  id: F002\\\\n  label: fig:rsa_bar\\\\n  location:\\\\n    section: experiments\\\\n  source_path: figures/fig2.pdf\\\\n  type: result\\\\n- caption: 'Per-layer RSA ($\\\\\\\\rho$) with the action space across all 32 LLM layers.\\\\n    Trained image\\\\\\\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\\\\\\\to$ L12 $=\\\\n    0.628$ (peak, above Projector $0.615$) $\\\\\\\\to$ L32 $= 0.422$. Untrained image\\\\\\\\_mean\\\\n    (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2\\\\n    cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).'\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: per-layer RSA trained/untrained image_mean (32 layers)\\\\n    tier: tier1\\\\n  id: F003\\\\n  label: fig:layer_curves\\\\n  location:\\\\n    section: experiments\\\\n  source_path: figures/fig3.pdf\\\\n  type: result\\\\n- caption: Functional probe $R^2$ for action prediction (best layer for each source).\\\\n    Both trained readout ($R^2{=\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: peak R2 values (trained img_mean L8, readout L13)\\\\n    tier: tier1\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: projector/dino/clip R2\\\\n    tier: tier1\\\\n  id: F004\\\\n  label: fig:probe_bars\\\\n  location:\\\\n    section: experiments\\\\n  source_path: figures/fig4.pdf\\\\n  type: result\\\\n- caption: \\\\\\\\textbf{(a)\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: trained vs untrained per-layer RSA + instruction conditions\\\\n    tier: tier1\\\\n  - exp_id: plan_008_random_inst_control\\\\n    metric: instruction invariance\\\\n    tier: tier1\\\\n  id: F005\\\\n  label: fig:factorial\\\\n  location:\\\\n    section: experiments\\\\n  source_path: figures/fig5.pdf\\\\n  type: result\\\\n- id: F006\\\\n  location:\\\\n    section: appendix\\\\n    figure_number: 0\\\\n  caption: ''\\\\n  type: other\\\\n  source: {}\\\\n  output_path: ''\\\\n  deprecated: false\\\\n- id: F007\\\\n  location:\\\\n    section: appendix\\\\n    figure_number: 0\\\\n  caption: ''\\\\n  type: other\\\\n  source: {}\\\\n  output_path: ''\\\\n  deprecated: false\\\\npaper:\\\\n  generated_at: '2026-05-17T22:15:14.113705+00:00'\\\\n  source: auto-bootstrap from existing tex files\\\\n  title: Formatting Instructions for CoRL 2026 Camera-Ready\\\\n  version: 51\\\\ntables:\\\\n- caption: Geometric (RSA $\\\\\\\\rho$) and functional (probe $R^2$) alignment with the\\\\n    action space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both\\\\n    trained readout and image\\\\\\\\_mean exceed the projector in $R^2$, confirming the\\\\n    inverted-U extends to functional capacity. VLA rows show peak-layer values (RSA/R$^2$\\\\n    peaks listed separately when they differ). 95\\\\\\\\% CIs from 10{,\\\\n  cells: []\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: all RSA peaks + baselines\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: all R2 peaks\\\\n    tier: tier1\\\\n  - exp_id: plan_012_clip_vit_control\\\\n    metric: projector/dino/clip R2\\\\n    tier: tier1\\\\n  id: T001\\\\n  label: tab:rsa_overview\\\\n  location:\\\\n    section: experiments\\\\n- caption: Training effects on action-relevant structure (bootstrap, 10{,\\\\n  cells: []\\\\n  deprecated: true\\\\n  evidence:\\\\n  - exp_id: d041_method_b_rsa\\\\n    metric: bootstrap_best_vs_best + same_layer comparisons\\\\n    tier: tier1\\\\n  - exp_id: plan_011_fulllayer_r2\\\\n    metric: bootstrap_best_vs_best R2\\\\n    tier: tier1\\\\n  id: T002\\\\n  label: tab:training_effects\\\\n  location:\\\\n    section: experiments\\\\n_completeness:\\\\n  coverage: 69/74\\\\n  claims: 71\\\\n  tables: 0\\\\n  figures: 3\\\\n  tier_counts:\\\\n    tier1: 0\\\\n    tier2: 69\\\\n    tier3: 5\\\\n    tierX: 0\\\\n  last_checked: '2026-05-17T22:15:14.113771+00:00'\\\\n\\\", \\\"total_chars\\\": 51898, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
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
Now I have the full structure. Let me understand the key points:

1. The YAML has `claims`, `figures`, `tables`, and `_completeness` sections
2. Current coverage: 69/74, with tier_counts showing tier1: 0, tier2: 69, tier3: 5
3. I need to add/update 8 experiments as tier1 mappings

Let me look at the actual YAML file directly to be able to edit it properly. The content is in JSON-escaped format, so let me read the actual file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "e7b6514f-ab05-4e59-ba04-25654aab6731",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwGkxwNf1e5VfeVMJvSd9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20168,
      "cache_read_input_tokens": 26567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20168
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

Now let me read the actual YAML file directly and check which of these 8 experiments already exist in the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "857d1d84-1354-49bf-8ad8-03244fbcc9fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwGkxwNf1e5VfeVMJvSd9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20168,
      "cache_read_input_tokens": 26567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20168
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

<details open><summary>🔧 Tool call — Read · `toolu_01Lw53bZSCACniFRggmoSg4y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "aefcf4e5-cc16-40fb-ad31-cdabfd42c7af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwGkxwNf1e5VfeVMJvSd9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20168,
      "cache_read_input_tokens": 26567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20168
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

_source line 17 · 2026-05-18T17:42:20.074Z_

<details><summary>↩ Tool result · `toolu_01Lw53bZSCACniFRggmoSg4y`</summary>

```text
1	claims:
2	- deprecated: true
3	  evidence:
4	  - exp_id: d041_method_b_rsa
5	    metric: baselines.dino_cls=0.6915
6	    tier: tier1
7	  - exp_id: plan_013_branch_split
8	    metric: post_projector_4096d_rsa=0.615
9	    tier: tier1
10	  - exp_id: d041_method_b_rsa
11	    metric: baselines.clip_cls=0.557
12	    tier: tier1
13	  id: C001
14	  location:
15	    context: result_statement
16	    section: abstract
17	  text: 'First, self-supervised pretraining provides the strongest action-relevant
18	    geometry: standalone DINOv2 achieves RSA $ = 0.692$, exceeding all VL-pretrained
19	    encoders (DinoSigLIP+Projector $ = 0.615$; CL'
20	  type: quantitative
21	- deprecated: true
22	  evidence:
23	  - exp_id: d041_method_b_rsa
24	    metric: trained_image_mean_peak.rsa=0.6282
25	    tier: tier1
26	  - exp_id: d041_method_b_rsa
27	    metric: untrained_image_mean_peak.rsa=0.6117
28	    tier: tier1
29	  - exp_id: plan_011_fulllayer_r2
30	    metric: trained_last_preaction_peak.mean_R2=0.6779
31	    tier: tier1
32	  id: C002
33	  location:
34	    context: result_statement
35	    section: abstract
36	  text: 'Second, the LLM applies a non-monotonic transformation---the first 12 layers
37	    enhance geometric alignment with the action space above the vision encoder input
38	    ($$: $0.612  0.628$ at L12), while the rem'
39	  type: quantitative
40	- deprecated: true
41	  evidence:
42	  - exp_id: d041_method_b_rsa
43	    metric: bootstrap_best_vs_best_imgmean.delta=0.017,significant=false
44	    tier: tier1
45	  - exp_id: plan_010_libero_spatial
46	    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001
47	    tier: tier1
48	  - exp_id: plan_011_fulllayer_r2
49	    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006
50	    tier: tier1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "8274c0bc-5593-4cf8-849f-a10fed00c3f9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
      "content": "claims:\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915\n    tier: tier1\n  - exp_id: plan_013_branch_split\n    metric: post_projector_4096d_rsa=0.615\n    tier: tier1\n  - exp_id: d041_method_b_rsa\n    metric: baselines.clip_cls=0.557\n    tier: tier1\n  id: C001\n  location:\n    context: result_statement\n    section: abstract\n  text: 'First, self-supervised pretraining provides the strongest action-relevant\n    geometry: standalone DINOv2 achieves RSA $ = 0.692$, exceeding all VL-pretrained\n    encoders (DinoSigLIP+Projector $ = 0.615$; CL'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained_image_mean_peak.rsa=0.6282\n    tier: tier1\n  - exp_id: d041_method_b_rsa\n    metric: untrained_image_mean_peak.rsa=0.6117\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak.mean_R2=0.6779\n    tier: tier1\n  id: C002\n  location:\n    context: result_statement\n    section: abstract\n  text: 'Second, the LLM applies a non-monotonic transformation---the first 12 layers\n    enhance geometric alignment with the action space above the vision encoder input\n    ($$: $0.612  0.628$ at L12), while the rem'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017,significant=false\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\n    tier: tier1",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 1896
    }
  }
}
```

</details>

---


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LB2xph3MWrGrh85rPtWZrY`</summary>

```json
{
  "project": "vla-ssd",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "title",
    "status",
    "conclusion"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "001ad77f-8bd0-49af-83b9-e3826248cbf3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwGkxwNf1e5VfeVMJvSd9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20168,
      "cache_read_input_tokens": 26567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20168
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

_source line 19 · 2026-05-18T17:42:21.361Z_

<details><summary>↩ Tool result · `toolu_01LB2xph3MWrGrh85rPtWZrY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"counterfactual_instruction\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"attention_decomposition\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"action_metrics_extended\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"cross_layer_L13_ablation\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"cross_layer_L8_ablation\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"dose_response_curve\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"permutation_test_I2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"action_trajectory_control\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"action_trajectory_analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"behavioral_pilot_w4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"threecond_multiseed_r2_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"threecond_multiseed_r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"random_subset_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"linear_probe_last_preaction\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama2base_action_probe\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"ablation_50demos_main\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"ablation_p2_demo_sensitivity\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"ablation_50demos_control8\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"l1_head_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"cross_inst_spatial_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan010_rsa_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan010_action_probe_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama2_base_control\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"rsa_cosine_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"rsa_permutation_test\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"ablation_p1_seed_robustness\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"ablation_p2_demo_sensitivity_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_functional_action_delta_probe\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_functional_probe_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d027_trained_no_inst_rsa\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d021_output_head_analysis\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"d021_instruction_ablation\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"lg_pca1024_linear_pertimestep\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"lg_rsa_analysis\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"lg_gc_trained_frame0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_gc_dino\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_gc_untrained\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"lg_gc_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"cross_inst_extract_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"cross_inst_extract_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"openvla-untrained-extract\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"openvla-trained-extract\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_extract_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_extract_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"dinov2_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_012_clip_vit_control\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qa_probe_classification\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"rsa_per_dof_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_010_extract_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_010_extract_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_010_libero_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_013_branch_split\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d041_method_b_rsa\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_011_fulllayer_r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"unified_action_probe\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_instruction_ablation\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_output_head_analysis\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_008_random_inst_control\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"untrained_last_preaction_probe\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_009_cka_verification\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_functional_action_probe\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_bootstrap_ci_training_effect\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_image_mean_rsa_verify\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_003_perlayer_degradation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d027_siglip_only_rsa\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_shuffled_token_control\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_dino_extract\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_action_probe\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_extract_untrained_r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_extract_trained_r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_extract_untrained_r1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_extract_trained_r1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mvp2_delta_dino\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_delta_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_delta_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_action_dino\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_action_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_action_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_controlb_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_controlb_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_001\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_probe_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_probe_trained\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}}, \"count\": 83, \"total\": 83, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2995}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "6c910742-408f-44a4-8936-15df4e66bb47",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"counterfactual_instruction\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"attention_decomposition\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"action_metrics_extended\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"cross_layer_L13_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"cross_layer_L8_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"dose_response_curve\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"permutation_test_I2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"action_trajectory_control\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"action_trajectory_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"behavioral_pilot_w4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"threecond_multiseed_r2_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"threecond_multiseed_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"random_subset_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"linear_probe_last_preaction\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"llama2base_action_probe\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"ablation_50demos_main\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"ablation_p2_demo_sensitivity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"ablation_50demos_control8\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"l1_head_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"cross_inst_spatial_trained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan010_rsa_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan010_action_probe_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"llama2_base_control\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"rsa_cosine_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"rsa_permutation_test\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"ablation_p1_seed_robustness\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"ablation_p2_demo_sensitivity_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"p0_functional_action_delta_probe\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"p0_functional_probe_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d027_trained_no_inst_rsa\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d021_output_head_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"d021_instruction_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"lg_pca1024_linear_pertimestep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"lg_rsa_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"lg_gc_trained_frame0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"lg_gc_dino\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"lg_gc_untrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"lg_gc_trained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"cross_inst_extract_untrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"cross_inst_extract_trained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"openvla-untrained-extract\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"openvla-trained-extract\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"lg_extract_untrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"lg_extract_trained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"dinov2_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_012_clip_vit_control\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"qa_probe_classification\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"rsa_per_dof_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_010_extract_trained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_010_extract_untrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_010_libero_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_013_branch_split\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d041_method_b_rsa\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_011_fulllayer_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"unified_action_probe\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"lg_instruction_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"lg_output_head_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan_008_random_inst_control\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"untrained_last_preaction_probe\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_009_cka_verification\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"p0_functional_action_probe\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"p0_bootstrap_ci_training_effect\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"p0_image_mean_rsa_verify\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_003_perlayer_degradation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d027_siglip_only_rsa\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"lg_shuffled_token_control\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"lg_dino_extract\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp2_action_probe\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"lg_extract_untrained_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"lg_extract_trained_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"lg_extract_untrained_r1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"lg_extract_trained_r1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mvp2_delta_dino\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp2_delta_untrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp2_delta_trained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp2_action_dino\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp2_action_untrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp2_action_trained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp_controlb_untrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp_controlb_trained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"mvp_probe_untrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp_probe_trained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}}, \\\"count\\\": 83, \\\"total\\\": 83, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2995}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"counterfactual_instruction\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"attention_decomposition\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"action_metrics_extended\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"cross_layer_L13_ablation\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"cross_layer_L8_ablation\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"dose_response_curve\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"permutation_test_I2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"action_trajectory_control\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"action_trajectory_analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"behavioral_pilot_w4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"threecond_multiseed_r2_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"threecond_multiseed_r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"random_subset_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"linear_probe_last_preaction\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama2base_action_probe\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"ablation_50demos_main\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"ablation_p2_demo_sensitivity\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"ablation_50demos_control8\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"l1_head_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"cross_inst_spatial_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan010_rsa_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan010_action_probe_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama2_base_control\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"rsa_cosine_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"rsa_permutation_test\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"ablation_p1_seed_robustness\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"ablation_p2_demo_sensitivity_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_functional_action_delta_probe\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_functional_probe_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d027_trained_no_inst_rsa\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d021_output_head_analysis\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"d021_instruction_ablation\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"lg_pca1024_linear_pertimestep\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"lg_rsa_analysis\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"lg_gc_trained_frame0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_gc_dino\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_gc_untrained\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"lg_gc_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"cross_inst_extract_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"cross_inst_extract_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"openvla-untrained-extract\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"openvla-trained-extract\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_extract_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_extract_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"dinov2_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_012_clip_vit_control\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qa_probe_classification\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"rsa_per_dof_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_010_extract_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_010_extract_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_010_libero_spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_013_branch_split\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d041_method_b_rsa\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_011_fulllayer_r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"unified_action_probe\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_instruction_ablation\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_output_head_analysis\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_008_random_inst_control\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"untrained_last_preaction_probe\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_009_cka_verification\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_functional_action_probe\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_bootstrap_ci_training_effect\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"p0_image_mean_rsa_verify\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_003_perlayer_degradation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d027_siglip_only_rsa\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"lg_shuffled_token_control\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_dino_extract\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_action_probe\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_extract_untrained_r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_extract_trained_r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_extract_untrained_r1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lg_extract_trained_r1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mvp2_delta_dino\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_delta_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_delta_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_action_dino\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_action_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp2_action_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_controlb_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_controlb_trained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_001\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mvp_probe_untrained\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mvp_probe_trained\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}}, \"count\": 83, \"total\": 83, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2995}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Good. All 8 experiments exist in the registry with DONE status. Now I need to understand the structure better and find the specific claims that these experiments should map to. Let me search for existing references to these experiments in the provenance file, and also look at the non-deprecated claims to find the right ones to update.

Let me look at the YAML more carefully. The existing file has claims, figures, tables, and _completeness sections. I need to find claims that correspond to the paper sections mentioned in the task:

1. **dose_response_curve** → §4.3 dose-response paragraph + Discussion convergent evidence (4)


2. **counterfactual_instruction** → §4.3 counterfactual paragraph + Discussion convergent evidence (5)
3. **action_trajectory_analysis** → §4.3 action trajectory paragraph + Discussion convergent evidence (3)
4. **action_trajectory_control** → §4.3 control ablation + Discussion per-head
5. **ablation_50demos_main** → §4.3 ablation results + Discussion convergent evidence (2)
6. **random_subset_ablation** → §4.3 random subset comparison
7. **permutation_test_I2** → Appendix §A.8 CV permutation
8. **threecond_multiseed_r** → appears to be cut off, but likely maps to another appendix section

Now I'm searching through the provenance content to see where these experiments are already referenced as tier2 inferred claims, or if I need to create new claim entries. Looking at what's already documented, I can see cross_instruction_probe, l1_attention_pattern, and ablation_p2_demo_sensitivity are well-referenced, but most of these other experiment IDs don't appear to have direct references yet.

I notice C278 mentions demo sensitivity results and C429 references ablation_p2_demo_sensitivity, but I'm not finding ablation_50demos_main or the other experiments. So my approach is to map each experiment to its corresponding section and claim in the paper, then add them as tier1 evidence entries. I need to examine the paper's §4.3 and appendix sections to identify which claims correspond to the dose-response, counterfactual, action trajectory, and ablation results paragraphs.

Let me start by reviewing the existing non-deprecated claims to find matches for these experiments, rather than parsing the tex files line by line. Looking at what's already there, most of the experimental claims are tagged under the experiments section, and §4.3 likely covers the convergent evidence or causal validation subsection. I can see C108 discusses layer-wise classification performance, C278 covers robustness under reduced demonstrations, C395 shows ablation effects on deep layers, and C429 appears to address stability across different conditions.

Now I'm searching through the claims for specific experimental patterns—dose-response relationships, counterfactual manipulations, action trajectories, permutation tests—but these don't seem to have corresponding claims yet. This suggests these are newer experiments that either need new claims created or should be mapped as additional evidence to existing ones. Since the task asks to add or update tier1 direct mappings, I should identify which paper sections these experiments belong to and either locate matching claims or establish new ones.

Let me reconsider the task: auto_build_provenance already achieved 69/74 coverage with many tier2 inferred mappings, and I need to manually upgrade 8 new experiments to tier1 with proper metrics. The strategy is to search existing claims for any tier2 evidence mentioning these experiments, then promote them to tier1 with structured metric information, or add new evidence entries to claims that already exist.

Looking at the paper structure, §4.3 covers convergent evidence including dose-response, counterfactual, trajectory, and ablation analyses. For dose_response_curve, I need to find or create claims about the dose-response relationship showing how performance scales with input quantity. For counterfactual_instruction, I need similar mappings to claims about causal validation through counterfactual manipulation.

The remaining experiments map to specific sections: action_trajectory_analysis and action_trajectory_control both feed into §4.3's trajectory paragraph and Discussion, ablation_50demos_main connects to the ablation results and convergent evidence claims, random_subset_ablation provides comparison data, permutation_test_I2 validates findings in the appendix, and threecond_multiseed_r2_v2 supplies the three-condition multi-seed R² data for §4.1 and §4.2.

I need to step back and actually read through the paper's tex files to see what §4.3 contains, then cross-reference that with the experiment registry to build accurate mappings rather than guessing at which claims each experiment supports.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "567586db-5d5f-4b21-80c4-273a8ccfdb05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GqTTaCBgF4L7QVLk6YRsq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 46735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3615
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

_source line 21_

Let me check the paper tex files to understand §4.3 content and find the exact claims these experiments map to.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "aa470722-8614-4c32-9634-5091b1082980",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GqTTaCBgF4L7QVLk6YRsq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 46735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3615
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

_source line 22_

<details open><summary>🔧 Tool call — Agent · `toolu_01Ef5xPBxeh51RFxv5FGbpDr`</summary>

```json
{
  "description": "Find paper sections for mapping",
  "subagent_type": "Explore",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/, find all .tex files related to the paper. Then search for the sections §4.3 (or subsections about \"dose-response\", \"counterfactual\", \"action trajectory\", \"ablation\", \"convergent evidence\", \"causal\") and §A.8 (appendix about \"permutation\"). Also find §4.1 and §4.2 section headers.\n\nI need to understand what content is in each section so I can map experiments to specific claims. Report:\n1. The file paths of the relevant tex files\n2. For §4.3: the key paragraphs/claims about dose-response, counterfactual instruction, action trajectory, ablation, random subset\n3. For §A.8: the permutation test content\n4. For §4.1 and §4.2: the section titles and what three-condition data they present\n5. Any mention of \"convergent evidence\" numbered items in the Discussion section\n\nSearch breadth: very thorough"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "b4d48cc4-d967-476a-9d4d-04d2d78aa91b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GqTTaCBgF4L7QVLk6YRsq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 46735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3615
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

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Find paper sections for mapping",
  "task_type": "local_agent",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/, find all .tex files related to the paper. Then search for the sections §4.3 (or subsections about \"dose-response\", \"counterfactual\", \"action trajectory\", \"ablation\", \"convergent evidence\", \"causal\") and §A.8 (appendix about \"permutation\"). Also find §4.1 and §4.2 section headers.\n\nI need to understand what content is in each section so I can map experiments to specific claims. Report:\n1. The file paths of the relevant tex files\n2. For §4.3: the key paragraphs/claims about dose-response, counterfactual instruction, action trajectory, ablation, random subset\n3. For §A.8: the permutation test content\n4. For §4.1 and §4.2: the section titles and what three-condition data they present\n5. Any mention of \"convergent evidence\" numbered items in the Discussion section\n\nSearch breadth: very thorough",
  "uuid": "036c0b76-af3e-4383-9dab-5882112d07f6",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


## Round 1

## Round 1

9 recorded events


### User

_source line 24 · 2026-05-18T17:43:06.993Z_

In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/, find all .tex files related to the paper. Then search for the sections §4.3 (or subsections about "dose-response", "counterfactual", "action trajectory", "ablation", "convergent evidence", "causal") and §A.8 (appendix about "permutation"). Also find §4.1 and §4.2 section headers.

I need to understand what content is in each section so I can map experiments to specific claims. Report:
1. The file paths of the relevant tex files
2. For §4.3: the key paragraphs/claims about dose-response, counterfactual instruction, action trajectory, ablation, random subset
3. For §A.8: the permutation test content
4. For §4.1 and §4.2: the section titles and what three-condition data they present
5. Any mention of "convergent evidence" numbered items in the Discussion section

Search breadth: very thorough

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "4941818e-fd4e-487a-a8b5-67d34f21bd5f"
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
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_15/…",
  "usage": {
    "total_tokens": 19437,
    "tool_uses": 1,
    "duration_ms": 1765
  },
  "last_tool_name": "Glob",
  "uuid": "183bbbf9-5d26-4d4c-97dc-9d92a76eba25",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 19440,
    "tool_uses": 2,
    "duration_ms": 2008
  },
  "last_tool_name": "Bash",
  "uuid": "9cfb40d9-298c-48a0-a2b6-a750428f8006",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Glob · `toolu_018h44u616CeG3kvSH3QxR9g`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "ed14f6f3-2e97-44c0-8919-ab65baa41a3b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YCLkHzT4gorVGt9SQoSgjr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19428,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19428,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 28 · 2026-05-18T17:43:08.783Z_

<details><summary>↩ Tool result · `toolu_018h44u616CeG3kvSH3QxR9g`</summary>

```text
artifacts/dream_reports/dream_20260515T222933/best/paper.tex
artifacts/dream_reports/dream_20260515T222933/median/paper.tex
artifacts/dream_reports/dream_20260515T222933/worst/paper.tex
artifacts/dream_reports/dream_20260516T011810/best/paper.tex
artifacts/dream_reports/dream_20260516T011810/median/paper.tex
artifacts/dream_reports/dream_20260516T011810/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/method_a6c062.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/introduction_fccb56.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "95a9d277-b7b4-4782-8dc7-1b886fb89bd7"
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01RYE4NKgxuVxaFBk3Q98Aiu`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts -type f -name \"*.tex\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "360c40ad-8c53-4d88-9695-1601e6bf5329",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YCLkHzT4gorVGt9SQoSgjr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19428,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19428,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 30 · 2026-05-18T17:43:09.165Z_

<details><summary>↩ Tool result · `toolu_01RYE4NKgxuVxaFBk3Q98Aiu`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method_a6c062.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction_fccb56.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "9032163f-1566-477d-aaf2-9ed7347b6e98"
}
```

</details>

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Agent · `toolu_01KufG4mJYoZpp3mXNmVDyjx`</summary>

```json
{
  "description": "Get experiment details for 8 experiments",
  "subagent_type": "Explore",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/, read the experiment registry file (likely registry.yaml or experiments.yaml) to find details for these 8 experiments:\n1. dose_response_curve\n2. counterfactual_instruction\n3. action_trajectory_analysis\n4. action_trajectory_control\n5. ablation_50demos_main\n6. random_subset_ablation\n7. permutation_test_I2\n8. threecond_multiseed_r2_v2\n\nFor each, I need: exp_id, title, key metrics, conclusion, and any description of what it tests. Report all findings.\n\nSearch breadth: very thorough"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "141c4580-7b53-4dbf-bd08-d820dcd2dfdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GqTTaCBgF4L7QVLk6YRsq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 46735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3615
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

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Get experiment details for 8 experiments",
  "task_type": "local_agent",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/, read the experiment registry file (likely registry.yaml or experiments.yaml) to find details for these 8 experiments:\n1. dose_response_curve\n2. counterfactual_instruction\n3. action_trajectory_analysis\n4. action_trajectory_control\n5. ablation_50demos_main\n6. random_subset_ablation\n7. permutation_test_I2\n8. threecond_multiseed_r2_v2\n\nFor each, I need: exp_id, title, key metrics, conclusion, and any description of what it tests. Report all findings.\n\nSearch breadth: very thorough",
  "uuid": "71f0b296-1f4d-46a4-81aa-d14021509464",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


## Round 2

## Round 2

150 recorded events


### User

_source line 33 · 2026-05-18T17:43:09.535Z_

In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/, read the experiment registry file (likely registry.yaml or experiments.yaml) to find details for these 8 experiments:
1. dose_response_curve
2. counterfactual_instruction
3. action_trajectory_analysis
4. action_trajectory_control
5. ablation_50demos_main
6. random_subset_ablation
7. permutation_test_I2
8. threecond_multiseed_r2_v2

For each, I need: exp_id, title, key metrics, conclusion, and any description of what it tests. Report all findings.

Search breadth: very thorough

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "53f22e20-3af2-432b-9c6f-f024740b4e6d"
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
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 19366,
    "tool_uses": 1,
    "duration_ms": 1598
  },
  "last_tool_name": "Bash",
  "uuid": "9177bedc-676b-48fa-8d87-ba76f77fb0a2",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01SGhUydBokuAmn1DZuzr19N`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" | grep -E \"(registry|experiment)\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "796cd816-712e-46d0-825d-7b13a962828d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01721BAEdU2fLbUNsByqB2Wz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 597,
      "cache_read_input_tokens": 18754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 597,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 36 · 2026-05-18T17:43:11.208Z_

<details><summary>↩ Tool result · `toolu_01SGhUydBokuAmn1DZuzr19N`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_debug_check_both_experiments_20260518T073739_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_ssh_registry-cleanup-prep_20260515T171117_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_paper_writing_experiments_d041_20260516T043441_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_paper_writing_experiments_20260516T021635_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "940a6cbb-470e-4d8a-a133-4ef34d426e23"
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
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Searching for section\\{.*4\\.(1|2|3)\\}|subsection\\{.*4\\.(1|2|3)\\…",
  "usage": {
    "total_tokens": 21303,
    "tool_uses": 3,
    "duration_ms": 5344
  },
  "last_tool_name": "Grep",
  "uuid": "7c01ddb8-f6f2-4261-b6c1-302d8d5ef879",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_01RE8hZD8qoTMpBgdaLN9V4e`</summary>

```json
{
  "pattern": "section\\{.*4\\.(1|2|3)\\}|subsection\\{.*4\\.(1|2|3)\\}|\\\\section\\*?\\{.*4\\.(1|2|3)\\}|dose-response|counterfactual|action trajectory|ablation|random subset",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper",
  "output_mode": "content",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "4ae0cec2-c09e-4400-885f-2fd1413c19bd",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2V7HCtQrNEAABShkjMk7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1855,
      "cache_read_input_tokens": 19428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1855,
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

_source line 39 · 2026-05-18T17:43:12.375Z_

<details><summary>↩ Tool result · `toolu_01RE8hZD8qoTMpBgdaLN9V4e`</summary>

```text
artifacts/_project/paper/related_work.tex:17:Grant et al.~\cite{grant2026} showed across six VLA architectures that the visual pathway dominates action generation, with language stream ablations causing minimal behavioral degradation---a behavioral-level finding consistent with our representational-level observation of vision encoder dominance.
artifacts/_project/paper/related_work.tex:23:Grant et al.\ operate at the behavioral level (input ablations and output measurements) without examining representation geometry.
artifacts/_project/paper/introduction.tex:11:Grant et al.~\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "e3b4b18c-6eda-4fd8-8d9d-cdeef18735cd"
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
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Searching for A\\.(8|Appendix)|permutation|A\\.8",
  "usage": {
    "total_tokens": 21305,
    "tool_uses": 4,
    "duration_ms": 6005
  },
  "last_tool_name": "Grep",
  "uuid": "884a21bb-fedb-493d-ae9d-b17532c42818",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Grep · `toolu_01J37uekAUP6K4bMfPtDhCuv`</summary>

```json
{
  "pattern": "A\\.(8|Appendix)|permutation|A\\.8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper",
  "output_mode": "content",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "6c4f8fbc-9886-485b-882e-e09af6781010",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2V7HCtQrNEAABShkjMk7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1855,
      "cache_read_input_tokens": 19428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1855,
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


### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Reading registry.yaml",
  "usage": {
    "total_tokens": 21290,
    "tool_uses": 2,
    "duration_ms": 3640
  },
  "last_tool_name": "Read",
  "uuid": "25a13779-7ca9-47df-a218-bba7186f6f66",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01VTTUgvkh1Bct1pf1QV2AZs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "0f202a71-5cff-4c92-99d3-eb5cd1336364",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VUJWqzkYJrmg5LFoPFJ3Pc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 19351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1920,
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

_source line 44 · 2026-05-18T17:43:13.021Z_

<details><summary>↩ Tool result · `toolu_01J37uekAUP6K4bMfPtDhCuv`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "5db92646-86eb-4116-aaa8-502f27e5b778"
}
```

</details>

---


### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Searching for convergent evidence",
  "usage": {
    "total_tokens": 21307,
    "tool_uses": 5,
    "duration_ms": 6402
  },
  "last_tool_name": "Grep",
  "uuid": "b146072d-d31e-4ec0-b9ba-f979f33a0d5a",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Grep · `toolu_01CqneKUfyuC5HbZvZYcSxzh`</summary>

```json
{
  "pattern": "convergent evidence",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper",
  "output_mode": "content",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "ec53de0a-56c1-45fd-9b1f-c4a006a0ed69",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2V7HCtQrNEAABShkjMk7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1855,
      "cache_read_input_tokens": 19428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1855,
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

_source line 47 · 2026-05-18T17:43:13.415Z_

<details><summary>↩ Tool result · `toolu_01CqneKUfyuC5HbZvZYcSxzh`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "e0216f89-7c66-49a0-9946-73f5fea43e9f"
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-18T17:43:13.589Z_

<details><summary>↩ Tool result · reported error · `toolu_01VTTUgvkh1Bct1pf1QV2AZs`</summary>

```text
File content (59120 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "f9487474-98a6-44f5-9a08-239e33089fde",
  "tool_use_result": "Error: File content (59120 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Searching for ^  dose_response_curve:|^  counterfactual_instruc…",
  "usage": {
    "total_tokens": 21461,
    "tool_uses": 3,
    "duration_ms": 6670
  },
  "last_tool_name": "Grep",
  "uuid": "0e84c40d-9b27-4483-9897-1eba2f337feb",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Grep · `toolu_01PCgazpUhUoeRKimP2pBeJJ`</summary>

```json
{
  "pattern": "^  dose_response_curve:|^  counterfactual_instruction:|^  action_trajectory_analysis:|^  action_trajectory_control:|^  ablation_50demos_main:|^  random_subset_ablation:|^  permutation_test_I2:|^  threecond_multiseed_r2_v2:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml",
  "output_mode": "content",
  "context": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "07334993-f456-4f53-ac14-1f5011a63601",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KmjWTN82uMTFsnE3MudftS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 21271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 168,
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

_source line 51 · 2026-05-18T17:43:16.228Z_

<details><summary>↩ Tool result · `toolu_01PCgazpUhUoeRKimP2pBeJJ`</summary>

```text
3068-    conclusion: killed
3069-    notes: superseded by ablation_50demos_control8 (DONE, success)
3070-  l1_head_ablation_50demos:
3071-    status: PREPARING
3072-    retry_count: 0
3073-    created_at: '2026-05-17T18:36:35.829Z'
3074-    updated_at: '2026-05-17T22:50:51.655Z'
3075-    spec:
3076-      command: CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py
3077-      server: westd-19183
3078-      gpu:
3079-      - cuda:0
3080-      pid: '905824'
3081-      log_path: ~/runs/vla-ssd/l1_head_ablation_50demos.log
3082-      submitted_at: '2026-05-17T18:36:35.597Z'
3083-      submitted_via: submit_training_job
3084-      backend: tmux
3085-      account: root
3086-    conclusion: killed
3087-    notes: superseded by ablation_50demos_main (DONE, success)
3088:  ablation_50demos_main:
3089-    status: DONE
3090-    retry_count: 0
3091-    created_at: '2026-05-17T18:53:20.415Z'
3092-    updated_at: '2026-05-17T21:49:51.638Z'
3093-    hypothesis: '50-demo full-data ablation: L1 instruction-dominant heads capacity
3094-      trade-off (R² increase under ablation) persists with adequate probe training
3095-      data, eliminating underfitting confound from 5-demo version.'
3096-    spec:
3097-      command: CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py
3098-        --demos_per_task 50 --readout_layers 1 8 13
3099-      server: westd-19183
3100-      gpu: cuda:0
3101-      data_path: /root/autodl-tmp/vla-ssd/data/libero_goal/
3102-      data_count: 50 demos/task x 10 tasks x 3 conditions
3103-      model_name: openvla-7b (trained)
3104-      seed: 42
3105-      checkpoint_path: N/A (inference-only)
3106-      log_path: /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json
3107-    metrics:
3108-      baseline_L1: 0.5567
--
3313-      untrained_peak_layer: 1
3314-      untrained_peak_R2: 0.492
3315-      inverted_U_trained: true
3316-      trained_gt_untrained_at_peak: true
3317-      bootstrap_best_vs_best:
3318-        delta: 0.103
3319-        ci:
3320-        - 0.056
3321-        - 0.167
3322-        p: 0
3323-      bootstrap_same_layer_trained_peak:
3324-        delta: 0.513
3325-        ci:
3326-        - 0.314
3327-        - 0.789
3328-        p: 0
3329-      mlp_trained_peak_R2_L13: 0.678
3330-      linear_vs_mlp_gap_at_peak: -0.082
3331-      result_path: /root/autodl-tmp/vla-ssd/results/linear_probe_last_preaction.json
3332-    completed_at: '2026-05-18T07:40:44.628Z'
3333:  threecond_multiseed_r2_v2:
3334-    status: DONE
3335-    retry_count: 0
3336-    created_at: '2026-05-18T08:04:22.860Z'
3337-    updated_at: '2026-05-18T09:11:34.295Z'
3338-    hypothesis: Multi-seed action probes (3 seeds, sequential split matching original
3339-      experiment) will confirm trained > llama2base > untrained R² gradient with low
3340-      seed variance, validating single-seed findings are robust and not split-dependent.
3341-    parent: threecond_multiseed_r2
3342-    spec:
3343-      command: bash -c "source /root/miniconda3/bin/activate base && cd /root/vla-ssd
3344-        && CUDA_VISIBLE_DEVICES=0 python scripts/threecond_multiseed_probe_v2.py 2>&1
3345-        | tee /root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.log"
3346-      server: westd-19183
3347-      data_path: /root/autodl-tmp/vla-ssd/features/{trained,untrained,llama2base}_libero_goal/
3348-      data_count: 10 tasks x 50 demos x 3 conditions
3349-      model_name: ActionMLPProbe(4096->256->7)
3350-      seed: 42,123,456
3351-      split: sequential_80_20_no_shuffle
3352-      r2_space: original_denormalized
3353-      checkpoint_source: pre-extracted features from openvla-7b / openvla-7b-untrained
--
3376-        layer: 9
3377-        mean_R2: 0.643
3378-        std: 0.014
3379-      L0_baseline:
3380-        mean_R2: 0.645
3381-        std: 0.008
3382-        note: three conditions consistent at L0
3383-      pattern_L1_L15: U&lt;L&lt;T
3384-      pattern_L16_L25: L≈T>>U
3385-      pattern_L32: reversal
3386-      split: sequential (demo_0-39 train, demo_40-49 val)
3387-      r2_space: original (denormalized)
3388-      result_path: /root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.json
3389-    conclusion: success
3390-    completed_at: '2026-05-18T09:10:58.657Z'
3391-    notes: v2 修正版（顺序 split + 反归一化 R²）。trained peak L9 0.643±0.014, llama2base peak
3392-      L12 0.634±0.013, untrained peak L1 0.547±0.008 (排除 L32 异常 0.589±0.007)。L0=0.645
3393-      三条件一致（共享 vision encoder）。trained-llama2base gap small (0.009 at peak, n=3),
3394-      direction consistent。llama2base v2=0.634 vs llama2base_action_probe registry
3395-      peak L4=0.6447，差距 0.010 在 seed 方差内，一致。untrained 中间层崩溃（负 R² + 高方差）是最强信号。
3396:  random_subset_ablation:
3397-    status: DONE
3398-    retry_count: 0
3399-    created_at: '2026-05-18T08:25:38.132Z'
3400-    updated_at: '2026-05-18T08:27:15.118Z'
3401-    hypothesis: Random subsets of 24 heads yield higher action R² increase than instruction-dominant
3402-      24 heads, indicating dominant heads serve dual routing-encoding function rather
3403-      than pure capacity trade-off
3404-    parent: ablation_50demos_main
3405-    spec:
3406-      command: python scripts/random_subset_ablation.py --n_demos 50 --n_random 10
3407-        --output /root/autodl-tmp/vla-ssd/results/random_subset_ablation.json
3408-      server: westd-19183
3409-      data_path: /root/autodl-tmp/vla-ssd/features/trained_libero_goal/
3410-      data_count: 10 tasks x 50 demos
3411-      model_name: ActionMLPProbe(4096->256->7) with L1 head ablation
3412-      seed: 10 random seeds for subset selection
3413-      checkpoint_source: pre-extracted features from openvla-7b (trained)
3414-      eval_data: /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ (10 tasks, 50 demos,
3415-        sequential split)
3416-      checkpoint_path: N/A (probe experiment, no checkpoint saved)
--
3465-      data_count: 3 tasks x 10 episodes x 2 conditions = 60 episodes
3466-      model_name: OpenVLA-7b (openvla-7b)
3467-      seed: '42'
3468-      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
3469-      eval_data: LIBERO-Goal benchmark (3 selected tasks, 300 max steps per episode)
3470-      wall_clock_seconds: 508.3
3471-      gpu_hours: 0.14
3472-    reproduce:
3473-      finished_at: '2026-05-18T10:31:41.576Z'
3474-    failure_reason: EXIT_CODE=129 (non-zero)
3475-    conclusion: killed
3476-    completed_at: '2026-05-18T10:31:43.232Z'
3477-    extra:
3478-      hook_events:
3479-      - event: on_failed
3480-        action: agent
3481-        ts: '2026-05-18T10:31:45.660946+00:00'
3482-    notes: OpenVLA bridge_orig unnorm_key 与 LIBERO action space 不兼容，baseline SR=0/6，实验前提不成立。两个进程被
3483-      SIGHUP 终止。Checkpoint 是 base pretrained（OXE 970K），未在 LIBERO fine-tune，无 LoRA
3484-      adapter，norm_stats 无 LIBERO key。
3485:  action_trajectory_analysis:
3486-    status: DONE
3487-    retry_count: 0
3488-    created_at: '2026-05-18T10:35:18.923Z'
3489-    updated_at: '2026-05-18T11:02:27.281Z'
3490-    hypothesis: L1 instruction-dominant head ablation significantly changes OpenVLA
3491-      action predictions (measured by action token divergence and per-dimension MSE),
3492-      demonstrating that instruction routing heads directly influence model output,
3493-      not just intermediate representations.
3494-    parent: ablation_50demos_main
3495-    spec:
3496-      command: bash -c "source /root/miniconda3/bin/activate base && cd /root/vla-ssd
3497-        && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_analysis.py"
3498-      server: westd-19183
3499-      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal/
3500-      data_count: 5 tasks x 10 demos x 50 timesteps = 2500 forward passes x 2 conditions
3501-      model_name: OpenVLA-7b (openvla-7b base pretrained)
3502-      seed: '42'
3503-      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
3504-      eval_data: LIBERO-Goal demo observations (open-loop, no execution)
3505-      checkpoint_path: N/A (inference only)
--
3526-      - dz
3527-      - rx
3528-      - ry
3529-      - rz
3530-      - gripper
3531-      kl_divergence:
3532-        mean: 5.079
3533-        std: 4.961
3534-      mse_vs_gt_baseline: 0.432
3535-      mse_vs_gt_ablated: 0.436
3536-      wilcoxon_p: 0
3537-      n_tasks: 5
3538-      n_samples: 2500
3539-      all_tasks_significant: true
3540-      per_task_cohens_d_range:
3541-      - 0.433
3542-      - 0.729
3543-      result_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json
3544-    conclusion: success
3545-    completed_at: '2026-05-18T11:02:27.281Z'
3546:  action_trajectory_control:
3547-    status: DONE
3548-    retry_count: 0
3549-    created_at: '2026-05-18T11:34:36.585Z'
3550-    updated_at: '2026-05-18T12:59:24.419Z'
3551-    hypothesis: Ablating 8 non-instruction heads (control) produces significantly
3552-      smaller action divergence (especially gripper dimension) than ablating 24 instruction-dominant
3553-      heads, proving the action output effect is instruction-specific rather than
3554-      generic perturbation.
3555-    parent: action_trajectory_analysis
3556-    spec:
3557-      command: bash -c "source /root/miniconda3/bin/activate base && cd /root/vla-ssd
3558-        && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_control.py
3559-        2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log"
3560-      server: westd-19183
3561-      gpu:
3562-      - cuda:0
3563-      pid: '47936'
3564-      log_path: ~/runs/vla-ssd/action_trajectory_control.log
3565-      submitted_at: '2026-05-18T11:53:06.410Z'
3566-      submitted_via: submit_training_job
--
3752-          t: 7.356
3753-          p: 0.0018
3754-        all_5_tasks_ctrl_gt_inst: true
3755-        interpretation: Control heads ~1.9x per-head effect; instruction heads achieve
3756-          larger total via 24-head collective coordination
3757-      temporal_coherence_proxy:
3758-        per_dim_cv_instruction: 1.3
3759-        per_dim_cv_control: 2.74
3760-        cross_task_I2_instruction: 0.87
3761-        cross_task_I2_control: 0.78
3762-        interpretation: Instruction ablation produces more consistent (low CV) and
3763-          more task-dependent (high I²) perturbation, consistent with structured language-dependent
3764-          computation
3765-      result_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json
3766-    conclusion: success
3767-    notes: 'Per-head effect formally confirmed: control heads ~1.9x stronger per-head
3768-      (d=0.051 vs 0.027, p=0.0018). But instruction heads show qualitatively different
3769-      perturbation: more consistent across dimensions (CV 1.30 vs 2.74) and more task-dependent
3770-      (I²=0.87 vs 0.78). Instruction heads mediate structured, coordinated computation
3771-      rather than individual strong effects.'
3772:  permutation_test_I2:
3773-    status: DONE
3774-    retry_count: 0
3775-    created_at: '2026-05-18T15:07:21.232Z'
3776-    updated_at: '2026-05-18T15:13:25.536Z'
3777-    hypothesis: Permutation test validates that observed CV difference (instruction
3778-      1.30 vs control 2.74) and I² difference (instruction 0.87 vs control 0.78) are
3779-      not explained by random head assignment. Shuffling head labels 1000x and recomputing
3780-      metrics produces null distribution; observed values should fall in extreme tail
3781-      (p < 0.05).
3782-    parent: action_trajectory_cpu_analysis
3783-    spec:
3784-      command: python scripts/permutation_test_I2.py
3785-      server: westd-19183
3786-      data_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json
3787-      data_count: 5 tasks x 2 conditions + 7 dims x 2 conditions
3788-      model_name: n/a (statistical test)
3789-      seed: 42
3790-      checkpoint_path: n/a
3791-      log_path: /root/autodl-tmp/vla-ssd/results/permutation_test_I2.json

[Showing results with pagination = limit: 250]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "20d581ef-4acb-4112-ba3e-79cc28f529ca"
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
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 22071,
    "tool_uses": 6,
    "duration_ms": 10413
  },
  "last_tool_name": "Bash",
  "uuid": "d2b61cd5-c6ef-480c-b8e2-7df79681569e",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01TFEV29kABNSp6CVoRF6Dso`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts -type f -name \"*.tex\" | xargs grep -l \"section\\|subsection\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "c5cfdb12-b4c0-45fd-9207-723ded719d36",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VANroWrz8zaFC1MRMeYksN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 21283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
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


### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 22072,
    "tool_uses": 7,
    "duration_ms": 10446
  },
  "last_tool_name": "Bash",
  "uuid": "0f6ad7e7-4d81-43ab-b129-6fe5131bf02f",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01MwjWhEfQTYDnPT37RbtNwU`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "28f6b082-8ec5-4e4e-9781-b3ad8cbf945e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VANroWrz8zaFC1MRMeYksN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 21283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
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

_source line 56 · 2026-05-18T17:43:17.505Z_

<details><summary>↩ Tool result · `toolu_01TFEV29kABNSp6CVoRF6Dso`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method_a6c062.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction_fccb56.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "48905545-82c4-4f9f-bc53-e93a6d3ff591"
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-18T17:43:17.517Z_

<details><summary>↩ Tool result · `toolu_01MwjWhEfQTYDnPT37RbtNwU`</summary>

```text
total 72K
-rw-r--r-- 1 ubuntu ubuntu 7.0K May 16 02:52 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  15K May 16 02:22 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu 4.8K May 16 02:29 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu 5.2K May 16 02:56 introduction_fccb56.tex
-rw-r--r-- 1 ubuntu ubuntu 7.3K May 16 02:29 method.tex
-rw-r--r-- 1 ubuntu ubuntu 7.5K May 16 02:43 method_a6c062.tex
-rw-r--r-- 1 ubuntu ubuntu 5.9K May 16 04:47 references.bib
-rw-r--r-- 1 ubuntu ubuntu 5.6K May 16 02:37 related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "553a826a-b6ae-483b-8226-23eacf8e4b0f"
}
```

</details>

---


### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Running grep -n \"^  dose_response_curve:\\|^  counterfactu…",
  "usage": {
    "total_tokens": 26398,
    "tool_uses": 4,
    "duration_ms": 9336
  },
  "last_tool_name": "Bash",
  "uuid": "2e7e6e2a-1284-4eae-bd0b-0e288178ece5",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_01DQui2TvGmFsbWAqKA3kYeq`</summary>

```json
{
  "command": "grep -n \"^  dose_response_curve:\\|^  counterfactual_instruction:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "d5771792-81bd-474b-86e7-3b4d83ce8c94",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NieeBF2bLcR3P15WS82nsv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4932,
      "cache_read_input_tokens": 21439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4932,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 60 · 2026-05-18T17:43:18.946Z_

<details><summary>↩ Tool result · `toolu_01DQui2TvGmFsbWAqKA3kYeq`</summary>

```text
3806:  dose_response_curve:
3832:  counterfactual_instruction:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "beaa8f94-8439-4ed9-924d-6b7908d1b80c"
}
```

</details>

---


### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Reading artifacts/_project/paper/experiments.tex",
  "usage": {
    "total_tokens": 23283,
    "tool_uses": 8,
    "duration_ms": 12618
  },
  "last_tool_name": "Read",
  "uuid": "bc2d8c21-078c-42f0-b9c3-3f454c6e6519",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_01ESPvGaxpzzwAjeZgp2Em14`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "336c10f8-5d53-4b4e-a705-9ada42949146",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AF9s35sPA6djKD4agjDF7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 22045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1205,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 63 · 2026-05-18T17:43:19.620Z_

<details><summary>↩ Tool result · `toolu_01ESPvGaxpzzwAjeZgp2Em14`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Benchmark and model.}
8	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
9	We use OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.
10	
11	\paragraph{Representation sources.}
12	We extract representations from five sources:
13	(a)~\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;
14	(b)~\textbf{LLM image\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;
15	(c)~\textbf{LLM last\_preaction}---the final token position before action decoding (readout token) at each LLM layer;
16	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token}; and
17	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean}.
18	Sources (d) and (e) serve as external baselines with no VLA training signal.
19	
20	\paragraph{Experimental conditions.}
21	We use a $2 \times 2$ factorial design crossing \emph{training status} (trained vs.\ untrained) with \emph{instruction presence} (with vs.\ without language instruction).
22	The untrained control applies \texttt{from\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.
23	
24	\paragraph{Representational Similarity Analysis (RSA).}
25	Following~\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.
26	We report Spearman rank correlation $\rho$ between representation and action RDMs, with 95\% confidence intervals from 10{,}000 bootstrap resamples.
27	
28	\paragraph{Functional probes.}
29	We train MLP probes (input $\to$ 256 $\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\cite{alain2017}. We report mean $R^2$ across action dimensions.
30	
31	%------------------------------------------------------------------
32	\subsection{Vision Encoder Dominance}
33	\label{sec:vision_dominance}
34	
35	This experiment tests whether vision-language pretrained encoders provide the dominant source of action-relevant geometric structure in VLA representations.
36	
37	Table~\ref{tab:rsa_overview} reports RSA $\rho$ between each representation source and the action space.
38	The SigLIP+Projector output achieves the highest alignment ($\rho = 0.615$, 95\% CI $[0.526, 0.695]$), followed by CLIP ViT-L/14 ($\rho = 0.557$, $[0.442, 0.660]$).
39	Both vision-language pretrained encoders substantially exceed DINOv2 ($\rho = 0.388$), a vision-only model.
40	The VLA's LLM layers (best image\_mean: $\rho = 0.501$ trained, $\rho = 0.485$ untrained) fall between VL-pretrained encoders and DINOv2 (Figure~\ref{fig:rsa_bar}).
41	
42	Three findings emerge.
43	First, VL pretraining---not LLM processing---is the primary source of action-relevant structure.
44	SigLIP and CLIP, both pretrained on image-text pairs, achieve $\rho \geq 0.557$, while DINOv2, pretrained with self-supervised vision objectives alone, reaches only $\rho = 0.388$.
45	This 0.169-point gap indicates that language-grounded visual features carry substantially more action-relevant geometry than features learned without language, consistent with behavioral evidence of visual dominance in VLA policies~\cite{grant2026}.
46	
47	Second, the MLP projector provides incremental alignment: SigLIP+Projector ($0.615$) exceeds CLIP ($0.557$) by $\Delta = 0.058$, consistent with the projector mapping vision features into the LLM's embedding space.
48	
49	Third, the LLM degrades rather than enhances vision encoder geometry.
50	Processing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\_mean), a drop of $\Delta = 0.114$.
51	
52	\paragraph{Geometric-functional dissociation.}
53	Functional probes reveal a dissociation between geometric similarity and functional decodability.
54	DINOv2 achieves $R^2 = 0.712$, statistically indistinguishable from SigLIP+Projector ($R^2 = 0.706$, $p = 0.22$, n.s.), despite its substantially lower RSA ($0.388$ vs.\ $0.615$).
55	High linear decodability does not require high geometric alignment with the action space---DINOv2 features are functionally rich but geometrically dissimilar to actions.
56	
57	\paragraph{Metric sensitivity.}
58	This dissociation extends to alternative similarity metrics.
59	Linear CKA~\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\ref{fig:metric_comparison}).
60	RDM kernel CKA restores the RSA-consistent ranking (Proj $>$ Trained $>$ Untrained $>$ DINOv2).
61	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.
62	
63	\begin{table}[t]
64	\centering
65	\caption{RSA between representation and action RDMs ($\rho$ $\uparrow$). VL-pretrained encoders (SigLIP, CLIP) dominate over vision-only DINOv2 and LLM-processed representations. 95\% CIs from 10{,}000 bootstrap resamples.}
66	\label{tab:rsa_overview}
67	\small
68	\begin{tabular}{llcc}
69	\toprule
70	Source & Aggregation & RSA $\rho$ & 95\% CI \\
71	\midrule
72	SigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\
73	CLIP ViT-L/14 & patch\_mean & 0.557 & {[0.442, 0.660]} \\
74	\midrule
75	VLA Trained w/ inst. & image\_mean & 0.501 & --- \\
76	VLA Trained no inst. & image\_mean & 0.501 & --- \\
77	VLA Untrained w/ inst. & image\_mean & 0.485 & --- \\
78	VLA Untrained no inst. & image\_mean & 0.482 & --- \\
79	\midrule
80	DINOv2 ViT-L/14 & cls\_token & 0.388 & --- \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
85	\begin{figure}[t]
86	\centering
87	\includegraphics[width=\columnwidth]{figures/fig2.pdf}
88	\caption{RSA with the action space ($\rho$) across representation sources. VL-pretrained encoders (SigLIP $\rho{=}0.615$, CLIP $\rho{=}0.557$) substantially exceed both LLM-processed representations ($\rho \leq 0.501$) and vision-only DINOv2 ($\rho{=}0.388$). Hatched bars indicate no-instruction conditions. Error bars: 95\% bootstrap CIs. Dashed line: DINOv2 reference.}
89	\label{fig:rsa_bar}
90	\end{figure}
91	
92	%------------------------------------------------------------------
93	\subsection{LLM Redistributes, Does Not Enhance, Action Structure}
94	\label{sec:llm_redistribution}
95	
96	This experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.
97	Table~\ref{tab:probes} reports functional probe $R^2$ for key representation sources.
98	Two complementary effects characterize LLM processing.
99	
100	\paragraph{Distributed degradation.}
101	Averaging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.
102	RSA drops from $0.615$ to $0.501$ ($\Delta = 0.114$); probe $R^2$ drops from $0.706$ to $0.683$ (95\% CI of $\Delta$: $[0.011, 0.037]$, $p = 0.001$).
103	Figure~\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.
104	
105	\paragraph{Readout concentration.}
106	While distributed image tokens lose information, the last pre-action token (\texttt{last\_preaction}) concentrates action-relevant information beyond the projector baseline.
107	Trained readout achieves $R^2 = 0.731$, exceeding SigLIP+Projector ($R^2 = 0.706$, $p = 0.001$; Figure~\ref{fig:probe_bars}).
108	This concentration is training-dependent: untrained readout ($R^2 = 0.686$) falls below the projector baseline, while trained readout ($0.731$) substantially exceeds it ($\Delta = 0.045$, $p < 0.0001$).
109	
110	Together, these results characterize the LLM as a \emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\cite{haon2025}.
111	
112	\begin{table}[t]
113	\centering
114	\caption{Functional probe $R^2$ ($\uparrow$) for action prediction from frozen representations. The LLM degrades distributed representations (image\_mean) relative to the projector but concentrates superior action information at the readout token---an effect that requires training. DINOv2 matches the projector in $R^2$ despite much lower RSA.}
115	\label{tab:probes}
116	\small
117	\begin{tabular}{lcc}
118	\toprule
119	Representation & $R^2$ & $p$ vs.\ Proj. \\
120	\midrule
121	SigLIP+Projector & 0.706 & --- \\
122	VLA Trained image\_mean (L19) & 0.683 & 0.001 \\
123	VLA Trained readout (L19) & \textbf{0.731} & 0.001 \\
124	VLA Untrained readout (L32) & 0.686 & --- \\
125	DINOv2 cls\_token & 0.712 & 0.220 (n.s.) \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	\begin{figure}[t]
131	\centering
132	\includegraphics[width=\columnwidth]{figures/fig3.pdf}
133	\caption{Per-layer RSA ($\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: SigLIP+Projector ($\rho{=}0.615$) and DINOv2 ($\rho{=}0.388$) reference levels.}
134	\label{fig:layer_curves}
135	\end{figure}
136	
137	\begin{figure}[t]
138	\centering
139	\includegraphics[width=\columnwidth]{figures/fig4.pdf}
140	\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\_mean ($R^2{=}0.683$) below the projector baseline ($0.706$, $p{=}0.001$) but concentrates superior information at the trained readout ($0.731$, $p{=}0.001$). Untrained readout ($0.686$) falls below the projector, confirming that concentration requires training ($\Delta{=}0.045$, $p{<}0.0001$). DINOv2 ($0.712$) is statistically indistinguishable from the projector ($p{=}0.22$).}
141	\label{fig:probe_bars}
142	\end{figure}
143	
144	%------------------------------------------------------------------
145	\subsection{Training Routes, Does Not Create, Action Geometry}
146	\label{sec:training_routing}
147	
148	This experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.
149	Table~\ref{tab:training_effects} reports the effect of training across metrics.
150	The $2 \times 2$ factorial analysis (Figure~\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.
151	
152	\paragraph{Geometric invariance to training.}
153	Training does not alter the LLM's geometric alignment with the action space.
154	For image\_mean RSA, the training effect is $\Delta = +0.021$ (95\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\_preaction RSA, $\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).
155	This null result is consistent with the vision encoder---whose weights are identical between conditions ($\cos\text{sim} = 1.0$)---being the sole source of action-relevant geometry.
156	
157	\paragraph{Geometric invariance to instruction.}
158	Language instructions similarly fail to modulate geometric structure.
159	Across the $2 \times 2$ matrix, the instruction effect is $\Delta = 0.004$ (n.s.).
160	A dedicated control experiment with four instruction conditions---normal task instructions ($\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\pm 0.017$ of the mean (Figure~\ref{fig:factorial}b).
161	
162	\paragraph{Functional concentration requires training.}
163	In contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\Delta = +0.045$ (CI $[+0.032, +0.058]$, $p < 0.0001$).
164	Training transforms the readout from below-projector ($R^2 = 0.686$) to above-projector ($R^2 = 0.731$) without altering the underlying geometry.
165	
166	These results support a \emph{routing} interpretation of LLM training in VLAs~\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.
167	
168	\begin{table}[t]
169	\centering
170	\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\_mean $R^2$ drop confirms distributed degradation.}
171	\label{tab:training_effects}
172	\small
173	\begin{tabular}{lccc}
174	\toprule
175	Comparison & $\Delta$ & 95\% CI & $p$ \\
176	\midrule
177	Training (image\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\
178	Training (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\
179	Training (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\
180	Proj.\ vs.\ image\_mean ($R^2$) & $+$0.023 & [$+$0.011, $+$0.037] & 0.001 \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	\begin{figure}[t]
186	\centering
187	\includegraphics[width=\columnwidth]{figures/fig5.pdf}
188	\caption{\textbf{(a)}~Training $\times$ Instruction matrix for image\_mean RSA ($\rho$). Neither training ($\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\Delta{=}0.004$, n.s.)\ produces a statistically detectable effect. \textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\pm 0.017$ of the mean $\mu{=}0.482$, confirming that instruction content does not modulate distributed geometric structure.}
189	\label{fig:factorial}
190	\end{figure}
191	
192	\begin{figure}[t]
193	\centering
194	\includegraphics[width=\columnwidth]{figures/fig6.pdf}
195	\caption{Comparison of three similarity metrics across representation sources. \textbf{(a)}~RSA (Spearman $\rho$) and \textbf{(c)}~RDM kernel CKA produce consistent rankings (Proj $>$ Trained $>$ Untrained $>$ DINOv2). \textbf{(b)}~Linear CKA~\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}
196	\label{fig:metric_comparison}
197	\end{figure}
198	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "c93f9353-1811-4d35-9662-5ef56b23aeb2"
}
```

</details>

---


### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Reading artifacts/_project/paper/discussion.tex",
  "usage": {
    "total_tokens": 23286,
    "tool_uses": 9,
    "duration_ms": 13278
  },
  "last_tool_name": "Read",
  "uuid": "a64223ca-e7e7-4243-bc86-b14cb610254c",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_012wYg5XRjHTfvWj95uWUrFJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "884a0f9a-fe4f-43da-8ae3-e245bd4a6021",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AF9s35sPA6djKD4agjDF7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 22045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1205,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 66 · 2026-05-18T17:43:20.283Z_

<details><summary>↩ Tool result · `toolu_012wYg5XRjHTfvWj95uWUrFJ`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Our experiments reveal a coherent picture of how action-relevant structure flows through a VLA.
6	The vision encoder is the \emph{source}: VL-pretrained encoders provide geometric structure aligned with the action space (SigLIP+Projector RSA $\rho = 0.615$; CLIP $\rho = 0.557$), far exceeding what the LLM produces at any layer ($\rho \leq 0.501$).
7	The LLM is a \emph{router}: it degrades distributed geometric structure ($\rho$: $0.615 \to 0.501$; $R^2$: $0.706 \to 0.683$) while concentrating a functionally superior representation at the readout token ($R^2 = 0.731$).
8	Training teaches the \emph{routing policy}: the geometric structure itself is invariant to training ($\Delta\rho = 0.021$, $p = 0.20$), but functional concentration at the readout requires it ($\Delta R^2 = 0.045$, $p < 0.0001$).
9	Notably, the projector alone captures 96.6\% of the trained readout's functional capacity ($0.706/0.731$), suggesting that the LLM's contribution, while statistically significant, is incremental.
10	
11	\paragraph{VL pretraining as a general source of action-relevant geometry.}
12	The inclusion of CLIP ViT-L/14 as an external baseline provides evidence that action-relevant geometric structure is a general product of vision-language pretraining, not an artifact of SigLIP's specific architecture or training data.
13	Both VL-pretrained encoders---SigLIP ($\rho = 0.615$) and CLIP ($\rho = 0.557$)---substantially exceed vision-only DINOv2 ($\rho = 0.388$).
14	The 0.169-point gap between CLIP and DINOv2, both ViT-L/14 architectures differing primarily in pretraining objective, isolates language grounding as the operative factor.
15	The additional increment from CLIP to SigLIP+Projector ($\Delta = 0.058$) is consistent with the projector's VLA-supervised alignment providing a modest boost, but the dominant contribution ($\rho = 0.557 \gg 0.388$) originates in VL pretraining itself.
16	
17	\paragraph{Geometric-functional dissociation.}
18	A recurring finding across our analyses is the dissociation between geometric alignment (RSA) and functional decodability (probe $R^2$).
19	DINOv2 achieves probe performance statistically indistinguishable from the SigLIP+Projector ($R^2$: $0.712$ vs.\ $0.706$, $p = 0.22$) despite substantially lower RSA ($0.388$ vs.\ $0.615$).
20	This dissociation implies that action information---in the sense of decodable content---is broadly available in strong visual features regardless of pretraining objective; what VL pretraining adds is \emph{geometric alignment}, organizing that information into a structure that mirrors the action space.
21	For VLA design, this distinction matters: encoder selection determines not just what information is available, but how it is organized, with downstream consequences for how easily the LLM can route it.
22	
23	\paragraph{Metric sensitivity: RSA versus CKA.}
24	The divergence between RSA and linear CKA underscores the importance of multi-metric evaluation.
25	Linear CKA produces a ranking---untrained LLM ($0.089$) $>$ trained ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$)---that partially reverses the RSA ordering.
26	Under linear CKA, training appears to \emph{reduce} similarity to the action space, an interpretation that contradicts both RSA and functional probe evidence.
27	RDM kernel CKA resolves this discrepancy, restoring the RSA-consistent ranking (trained $0.260$ $>$ Proj $0.257$ $>$ untrained $0.246$ $>$ DINOv2 $0.241$).
28	The divergence likely reflects linear CKA's sensitivity to second-order statistics and its known vulnerability to dimension mismatch between high-dimensional representations and the 7-D action space~\cite{kornblith2019}.
29	The practical implication is that the LLM transforms rather than destroys action structure, but the narrative one draws depends critically on which metric is employed.
30	
31	\paragraph{Implications for VLA design.}
32	Our findings suggest four practical considerations.
33	\emph{First}, vision encoder pretraining quality is the primary lever for action-relevant representations; investing in stronger VL encoders may yield larger gains than scaling the LLM backbone.
34	\emph{Second}, for downstream modules that operate on distributed representations (e.g., auxiliary losses, multi-task heads), the projector output may be preferable to LLM-processed features, given its higher geometric fidelity and 96.6\% of readout-level decodability.
35	\emph{Third}, the LLM's value lies in readout concentration---routing distributed information to a single decoding site---which informs action head design: architectures that exploit this concentration (e.g., reading from a dedicated token rather than pooling LLM features) may better leverage the LLM's trained routing.
36	\emph{Fourth}, the invariance of representation geometry to language instructions ($\Delta\rho = 0.004$, n.s.; content controls within $\pm 0.017$) suggests that instructions influence action selection through a mechanism other than modulating visual representation structure, inviting further investigation into how language conditions behavior in VLAs.
37	
38	\paragraph{Connection to behavioral evidence.}
39	Our representational findings complement the behavioral results of \citet{grant2026}, who showed that VLA policies are disproportionately driven by visual input and that language instructions are ``encoded but not used'' for action selection.
40	Our data provide a representational account of these behavioral patterns: vision dominates because the frozen encoder supplies the action-relevant geometric structure that the LLM routes to the readout, while instruction content does not modulate this geometric structure (all four instruction conditions yield RSA within $\pm 0.017$).
41	The alignment between representational and behavioral evidence strengthens the case that VL-pretrained vision encoders, rather than LLM reasoning, are the primary computational substrate for action generation in current VLA architectures.
42	
43	\paragraph{Limitations.}
44	Several limitations scope our conclusions.
45	We study a single VLA architecture (OpenVLA-7B) on a single benchmark suite (LIBERO); generalization to other architectures (e.g., RT-2~\cite{brohan2023_rt2}) and domains (e.g., mobile manipulation, dexterous hands) remains to be established.
46	RSA captures structural alignment between representations and actions but does not establish causal contribution---high RSA does not guarantee that the representation is causally used by the policy.
47	The CLIP and DINOv2 action probes were trained with different hyperparameters (100 epochs) than the projector and LLM probes (50 epochs); while within-experiment comparisons are valid, absolute $R^2$ values are not directly comparable across these two probe sets, and we have been careful to restrict cross-experiment claims accordingly.
48	Finally, our analyses characterize frozen representations post hoc; they do not address how these representations emerge during VLA pretraining or fine-tuning, nor whether architectural interventions (e.g., unfreezing the vision encoder) would alter the source--router dynamic we observe.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "3fae73ff-c7d0-4911-9e3f-abac1e2f005d"
}
```

</details>

---


### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Reading artifacts/_project/paper/method.tex",
  "usage": {
    "total_tokens": 23289,
    "tool_uses": 10,
    "duration_ms": 13350
  },
  "last_tool_name": "Read",
  "uuid": "20eca090-071c-4d28-b6ee-5a059b966c29",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01GkuSsvg2vrSMDDrhGoTPeU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "9b924f10-2c11-4c2c-92f7-adb6255dd7b2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AF9s35sPA6djKD4agjDF7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 22045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1205,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 69 · 2026-05-18T17:43:20.348Z_

<details><summary>↩ Tool result · `toolu_01GkuSsvg2vrSMDDrhGoTPeU`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We investigate where action-relevant representations originate within a vision-language-action (VLA) model by combining representational similarity analysis, functional probing, and kernel alignment across a factorial design of training and instruction conditions.
5	
6	\subsection{Model and Data}
7	\label{sec:model_data}
8	
9	\paragraph{Architecture.}
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA model comprising four components: (1)~a SigLIP-SO400M vision encoder~\cite{zhai2023_siglip} that maps RGB observations to patch-level visual tokens, (2)~an MLP projector that maps vision tokens into the language model's embedding space, (3)~a Llama-2 7B language backbone (32 transformer layers) that processes the concatenated sequence of projected image tokens and tokenized language instructions, and (4)~an action head that decodes 7-dimensional continuous actions (3D translation, 3D rotation, 1D gripper) from the final hidden states.
11	
12	\paragraph{Training data.}
13	We fine-tune OpenVLA on the LIBERO-10 split~\cite{liu2023_libero}, which contains 10 tabletop manipulation tasks with 50 human demonstrations each (500 demonstrations total).
14	We evaluate generalization on LIBERO-Goal, an out-of-distribution benchmark where episodes share initial object configurations but differ in goal specifications.
15	
16	\paragraph{Untrained control.}
17	To isolate the LLM's learned contribution from the vision encoder's pretrained geometry, we construct an untrained control by calling \texttt{from\_config()} to reinitialize all LLM parameters (6.74B weights drawn from random initialization) while preserving the frozen SigLIP encoder (0.80B pretrained weights).
18	The untrained model processes identical visual inputs through an identical vision encoder but lacks any learned language or action structure in its LLM layers.
19	
20	\subsection{Representation Extraction}
21	\label{sec:rep_extraction}
22	
23	We extract representations from five sources spanning the VLA processing pipeline and two external baselines:
24	
25	\begin{enumerate}[label=(\alph*),nosep,leftmargin=*]
26	    \item \textbf{SigLIP+Projector} --- the vision encoder output after MLP projection into the LLM's input space, before any LLM processing. This captures the representation that the LLM receives as input.
27	    \item \textbf{LLM image\_mean} --- the mean activation across all image token positions at each of the 32 LLM layers. This captures how the LLM transforms distributed visual information through its depth.
28	    \item \textbf{LLM last\_preaction} --- the activation at the final token position before action decoding (the readout token) at each LLM layer. This captures the representation from which actions are directly decoded.
29	    \item \textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token} --- a vision-only baseline pretrained with self-supervised objectives and no language supervision.
30	    \item \textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean} --- a vision-language baseline pretrained on image-text pairs, serving as a generalization control for VL pretraining effects independent of the VLA pipeline.
31	\end{enumerate}
32	
33	Sources (a)--(c) probe representations within the VLA model itself, while (d) and (e) provide external references with no VLA training signal.
34	
35	\paragraph{Factorial design.}
36	We cross two factors in a $2 \times 2$ design: \emph{training status} (trained vs.\ untrained LLM) and \emph{instruction presence} (with vs.\ without language instruction).
37	This yields four conditions per LLM representation source, enabling us to disentangle the contributions of LLM training and language grounding to action-relevant structure.
38	External baselines (d) and (e) are evaluated once, as they are independent of both factors.
39	
40	\subsection{Representational Similarity Analysis}
41	\label{sec:rsa}
42	
43	We adopt Representational Similarity Analysis (RSA)~\cite{kriegeskorte2008} to quantify the geometric alignment between neural representations and the action space.
44	
45	\paragraph{Representational dissimilarity matrices.}
46	For a set of $n$ observations, we compute an $n \times n$ representational dissimilarity matrix (RDM) for each representation source using Euclidean distance between representation vectors.
47	We similarly construct an action RDM from the 7-dimensional action vectors.
48	
49	\paragraph{RSA correlation.}
50	We measure alignment between a representation RDM and the action RDM via Spearman rank correlation $\rho$ between their upper-triangular elements.
51	Higher $\rho$ indicates that observations with similar representations also have similar actions, i.e., the representation geometry mirrors the action space geometry.
52	
53	\paragraph{Statistical inference.}
54	We compute 95\% confidence intervals from 10{,}000 bootstrap resamples of observation pairs for all pairwise comparisons.
55	RSA is computed per task and aggregated across the 10 tasks.
56	
57	\subsection{Functional Action Probes}
58	\label{sec:probes}
59	
60	RSA measures geometric alignment but does not assess whether action information is linearly decodable from representations.
61	We complement RSA with functional probing~\cite{alain2017} to measure the action information accessible to a lightweight decoder.
62	
63	\paragraph{Probe architecture.}
64	We train two-layer MLP probes (Linear $\to$ ReLU $\to$ Linear) mapping from the representation dimensionality to a 256-dimensional hidden layer and then to the 7-dimensional action space.
65	
66	\paragraph{Training protocol.}
67	Probes are optimized with Adam (learning rate $10^{-3}$, batch size 256) for 50 epochs with early stopping (patience 5 epochs on validation loss).
68	Representations are frozen throughout; only probe parameters are updated.
69	We use per-task 80/20 train/validation splits and report mean $R^2$ across the 7 action dimensions as the primary metric.
70	
71	\paragraph{Action-delta probes.}
72	In addition to predicting absolute actions $\mathbf{a}_t$, we train probes to predict action deltas $\Delta\mathbf{a} = \mathbf{a}_{t+1} - \mathbf{a}_t$, which capture the dynamic component of action structure independent of the current action magnitude.
73	
74	\paragraph{Statistical comparison.}
75	We use bootstrap paired comparison (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant.
76	
77	\subsection{Centered Kernel Alignment}
78	\label{sec:cka}
79	
80	RSA captures local geometric alignment---whether pairwise distances in representation space mirror those in action space.
81	To assess global structural preservation, we additionally employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} in two variants.
82	
83	\paragraph{Linear CKA.}
84	Linear CKA computes the normalized Hilbert-Schmidt Independence Criterion between linear kernel matrices of two representation sets.
85	It is invariant to orthogonal transformations and isotropic scaling, making it sensitive to global structure rather than local distance preservation.
86	
87	\paragraph{RDM kernel CKA.}
88	We also compute CKA using the RDMs themselves as kernel matrices, providing a bridge between the local sensitivity of RSA and the global perspective of linear CKA.
89	
90	\paragraph{Dimensionality caveat.}
91	When comparing high-dimensional representations (e.g., 4096-D LLM activations) with low-dimensional action vectors (7-D), linear CKA may be dominated by the few directions that span the action space, potentially inflating similarity estimates.
92	We report both CKA variants alongside RSA to ensure that conclusions are robust to metric choice.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "4607724c-2437-4d57-8887-1882a098ee67"
}
```

</details>

---


### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Reading registry.yaml",
  "usage": {
    "total_tokens": 26585,
    "tool_uses": 5,
    "duration_ms": 11206
  },
  "last_tool_name": "Read",
  "uuid": "3282d14f-7f7e-4299-a0a9-cfffe3802145",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_012nqZjtmgq61f1rWnTRz1xS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml",
  "offset": 3806,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "b5657303-8556-4ea4-b4dd-da29f26dab1b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012Wt8GABQ3uHfSCuikEtNs6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 186,
      "cache_read_input_tokens": 26371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 186,
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

_source line 72 · 2026-05-18T17:43:20.747Z_

<details><summary>↩ Tool result · `toolu_012nqZjtmgq61f1rWnTRz1xS`</summary>

```text
3806	  dose_response_curve:
3807	    status: DONE
3808	    retry_count: 0
3809	    created_at: '2026-05-18T15:07:22.213Z'
3810	    updated_at: '2026-05-18T16:32:50.159Z'
3811	    hypothesis: 'If instruction routing is a learned collective function, progressively
3812	      ablating more L1 heads (sorted by instruction attention fraction) should produce
3813	      monotonically increasing action divergence (dose-response curve). 8 conditions:
3814	      top-4/8/12/16/20/24/28/32. Supports C2 claim that routing is a distributed,
3815	      coordinated mechanism.'
3816	    parent: action_trajectory_control
3817	    spec:
3818	      command: dose_response_curve.py --conditions 4,8,12,16 (cuda:0) + --conditions
3819	        20,24,28,32 (cuda:1)
3820	      server: westd-19183
3821	      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
3822	      data_count: 5 tasks x 10 demos x 50 timesteps x 8 conditions = 20000 passes
3823	      model_name: openvla-7b
3824	      seed: 42
3825	      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
3826	      eval_data: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
3827	    failure_reason: 'startup recovery: RUNNING with no cron and no server/pid info'
3828	    conclusion: success
3829	    completed_at: '2026-05-18T16:26:06.324Z'
3830	    notes: 单调递增 dose-response 曲线，d=0.482(top4)→0.639(top32)，diminishing returns at
3831	      ~12-16 heads
3832	  counterfactual_instruction:
3833	    status: DONE
3834	    retry_count: 0
3835	    created_at: '2026-05-18T16:52:52.867Z'
3836	    updated_at: '2026-05-18T17:31:39.989Z'
3837	    hypothesis: 'L1 instruction-dominant heads perform instruction-specific routing:
3838	      changing the instruction (wrong/empty/shuffled/paraphrased) should produce systematically
3839	      different action outputs compared to correct instruction, with wrong and empty
3840	      causing larger divergence than shuffled or paraphrased.'
3841	    parent: action_trajectory_control
3842	    spec:
3843	      command: MUJOCO_GL=egl python -u scripts/counterfactual_instruction.py
3844	      server: westd-19183
3845	      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
3846	      data_count: 6000
3847	      model_name: openvla-7b
3848	      seed: 42
3849	      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
3850	      eval_data: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
3851	      checkpoint_path: N/A
3852	      log_path: /root/autodl-tmp/vla-ssd/results/counterfactual_instruction.log
3853	    checkpoint_path: N/A (eval-only experiment)
3854	    log_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_counterfactual_instruction_20260518T165804.log
3855	    conclusion: success
3856	    completed_at: '2026-05-18T17:31:15.868Z'
3857	    notes: '4 counterfactual conditions vs correct baseline. Cohen''s d: empty=0.968,
3858	      wrong=0.844, paraphrased=0.697, shuffled=0.625. All d>0.5. Graduated response
3859	      confirms instruction content sensitivity. Surprise: paraphrased > shuffled (model
3860	      depends on surface form, not just semantics). Supports C2 claim.'
3861	  action_metrics_extended:
3862	    status: DONE
3863	    retry_count: 0
3864	    created_at: '2026-05-18T16:52:53.825Z'
3865	    updated_at: '2026-05-18T17:16:37.223Z'
3866	    hypothesis: 'Extended analysis of existing action trajectory data: (1) per-dimension
3867	      MAE reveals which action dimensions are most affected by L1 instruction-head
3868	      ablation, (2) action direction cosine similarity shows whether ablation changes
3869	      action direction vs magnitude, providing mechanistic detail beyond aggregate
3870	      Cohen''s d.'
3871	    parent: action_trajectory_control
3872	    spec:
3873	      command: python3 (CPU-only, from existing JSONs)
3874	      server: westd-19183
3875	      data_path: /root/autodl-tmp/vla-ssd/results/
3876	      data_count: 5000
3877	      model_name: openvla-7b
3878	      seed: 42
3879	      checkpoint_source: N/A (analysis only)
3880	      eval_data: action_trajectory_analysis.json + action_trajectory_control.json
3881	      checkpoint_path: N/A
3882	      log_path: /root/autodl-tmp/vla-ssd/results/action_metrics_extended.json
3883	    conclusion: success
3884	    completed_at: '2026-05-18T17:16:32.376Z'
3885	    notes: 'Per-dim MAE extracted from existing JSONs. Instruction 24h causes 1.9-5.1x
3886	      larger shifts than control 8h. Translation dims most affected (dx=5.1x, dy=4.3x,
3887	      dz=3.1x), rotation moderate (roll=2.6x, pitch=2.2x, yaw=1.9x), gripper=2.1x.
3888	      Cosine similarity NOT computable: source JSONs only have aggregated stats, no
3889	      raw per-sample action vectors.'
3890	  attention_decomposition:
3891	    status: DONE
3892	    retry_count: 0
3893	    created_at: '2026-05-18T16:52:54.658Z'
3894	    updated_at: '2026-05-18T17:20:35.567Z'
3895	    hypothesis: Instruction-dominant heads (24/32 at L1) allocate significantly more
3896	      attention mass to instruction tokens than control heads (8/32), confirming that
3897	      the head classification reflects genuine functional specialization in attention
3898	      routing
3899	    parent: action_trajectory_control
3900	    spec:
3901	      command: python3 attention_decomposition_and_r2.py
3902	      server: westd-19183
3903	      data_path: /root/autodl-tmp/vla-ssd/results/attention/
3904	      data_count: 5 trained samples + 32-head untrained data
3905	      model_name: openvla-7b
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "440ca3ba-c622-4f37-93a0-9520a35ad097"
}
```

</details>

---


### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Searching for \\\\subsection\\{Vision Encoder Dominance\\}|\\\\subsec…",
  "usage": {
    "total_tokens": 32809,
    "tool_uses": 11,
    "duration_ms": 16677
  },
  "last_tool_name": "Grep",
  "uuid": "77f2532d-523f-40c1-90ac-964319746e03",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Grep · `toolu_019AyCdeoxDQKkYRRwJNmyKU`</summary>

```json
{
  "pattern": "\\\\subsection\\{Vision Encoder Dominance\\}|\\\\subsection\\{LLM Redistributes|\\\\subsection\\{Training Routes",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "50796845-0503-4b61-9d11-94dfe5b3d54d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016wkPUt5Zp2hfGFhQGPBv3T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9518,
      "cache_read_input_tokens": 23250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9518,
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


### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Running grep -A 200 \"^  dose_response_curve:\" /home/ubunt…",
  "usage": {
    "total_tokens": 28837,
    "tool_uses": 6,
    "duration_ms": 14288
  },
  "last_tool_name": "Bash",
  "uuid": "1058601f-1b50-4833-8635-cb45138e3841",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Bash · `toolu_01KmZ6iQK4jh6oLbYNtWuX1L`</summary>

```json
{
  "command": "grep -A 200 \"^  dose_response_curve:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "204da4fb-c8e2-49b5-8e05-caeaffacfe94",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AVeLd6wASkPza4uApXPwNs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2245,
      "cache_read_input_tokens": 26557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2245,
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

_source line 77 · 2026-05-18T17:43:23.878Z_

<details><summary>↩ Tool result · `toolu_01KmZ6iQK4jh6oLbYNtWuX1L`</summary>

```text
  dose_response_curve:
    status: DONE
    retry_count: 0
    created_at: '2026-05-18T15:07:22.213Z'
    updated_at: '2026-05-18T16:32:50.159Z'
    hypothesis: 'If instruction routing is a learned collective function, progressively
      ablating more L1 heads (sorted by instruction attention fraction) should produce
      monotonically increasing action divergence (dose-response curve). 8 conditions:
      top-4/8/12/16/20/24/28/32. Supports C2 claim that routing is a distributed,
      coordinated mechanism.'
    parent: action_trajectory_control
    spec:
      command: dose_response_curve.py --conditions 4,8,12,16 (cuda:0) + --conditions
        20,24,28,32 (cuda:1)
      server: westd-19183
      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
      data_count: 5 tasks x 10 demos x 50 timesteps x 8 conditions = 20000 passes
      model_name: openvla-7b
      seed: 42
      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
      eval_data: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
    failure_reason: 'startup recovery: RUNNING with no cron and no server/pid info'
    conclusion: success
    completed_at: '2026-05-18T16:26:06.324Z'
    notes: 单调递增 dose-response 曲线，d=0.482(top4)→0.639(top32)，diminishing returns at
      ~12-16 heads
  counterfactual_instruction:
    status: DONE
    retry_count: 0
    created_at: '2026-05-18T16:52:52.867Z'
    updated_at: '2026-05-18T17:31:39.989Z'
    hypothesis: 'L1 instruction-dominant heads perform instruction-specific routing:
      changing the instruction (wrong/empty/shuffled/paraphrased) should produce systematically
      different action outputs compared to correct instruction, with wrong and empty
      causing larger divergence than shuffled or paraphrased.'
    parent: action_trajectory_control
    spec:
      command: MUJOCO_GL=egl python -u scripts/counterfactual_instruction.py
      server: westd-19183
      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
      data_count: 6000
      model_name: openvla-7b
      seed: 42
      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
      eval_data: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
      checkpoint_path: N/A
      log_path: /root/autodl-tmp/vla-ssd/results/counterfactual_instruction.log
    checkpoint_path: N/A (eval-only experiment)
    log_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_counterfactual_instruction_20260518T165804.log
    conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "7b5524ec-ea3c-439f-bda4-cafbdba4725d"
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-18T17:43:23.693Z_

<details><summary>↩ Tool result · `toolu_019AyCdeoxDQKkYRRwJNmyKU`</summary>

```text
artifacts/_project/paper/experiments.tex:32:\subsection{Vision Encoder Dominance}
artifacts/_project/paper/experiments.tex:93:\subsection{LLM Redistributes, Does Not Enhance, Action Structure}
artifacts/_project/paper/experiments.tex:145:\subsection{Training Routes, Does Not Create, Action Geometry}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "a983424d-e7f7-4600-a26a-fdfc9dc7cbc2"
}
```

</details>

---


### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running grep -n \"dose-response\\|counterfactual\\|action tr…",
  "usage": {
    "total_tokens": 32810,
    "tool_uses": 12,
    "duration_ms": 17066
  },
  "last_tool_name": "Bash",
  "uuid": "d8a6f600-f8a4-4694-aeb1-3b3c7722b9af",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Bash · `toolu_013oXADNBYMnSfpxeEW6sFkB`</summary>

```json
{
  "command": "grep -n \"dose-response\\|counterfactual\\|action trajectory\\|ablation\\|random subset\\|permutation test\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "30e6a379-e31d-4597-97f0-a8ce2b0f10c8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016wkPUt5Zp2hfGFhQGPBv3T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9518,
      "cache_read_input_tokens": 23250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9518,
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

_source line 81 · 2026-05-18T17:43:24.109Z_

<details><summary>↩ Tool result · `toolu_013oXADNBYMnSfpxeEW6sFkB`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex:11:Grant et al.~\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex:17:Grant et al.~\cite{grant2026} showed across six VLA architectures that the visual pathway dominates action generation, with language stream ablations causing minimal behavioral degradation---a behavioral-level finding consistent with our representational-level observation of vision encoder dominance.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex:23:Grant et al.\ operate at the behavioral level (input ablations and output measurements) without examining representation geometry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "ecdf73f5-8b7a-4b1f-9a4f-d976cf7e1473"
}
```

</details>

---


### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Running grep -A 5 \"^  dose_response_curve:\" /home/ubuntu/…",
  "usage": {
    "total_tokens": 29870,
    "tool_uses": 7,
    "duration_ms": 16383
  },
  "last_tool_name": "Bash",
  "uuid": "3459b14e-3ffa-4119-819d-6e264f51fb22",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01LXadijNGaag7qWcGVwcCGQ`</summary>

```json
{
  "command": "grep -A 5 \"^  dose_response_curve:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml | grep \"metrics:\" -A 50 | head -60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "b5bc8356-7a93-41f0-9883-c8d4fd5caa17",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014WdYF28g9VmJGfRvZ52w5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 28802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1025,
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

_source line 84 · 2026-05-18T17:43:25.991Z_

<details><summary>↩ Tool result · `toolu_01LXadijNGaag7qWcGVwcCGQ`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "c5f56bd8-60e1-4fae-890d-520d10edb67f"
}
```

</details>

---


### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 33484,
    "tool_uses": 13,
    "duration_ms": 19319
  },
  "last_tool_name": "Bash",
  "uuid": "919bf878-3aba-4265-8b0b-19d171df2114",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_01PaoeEysXZxhwyipjf9NL6W`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts -type f -name \"*.tex\" | xargs grep -l \"appendix\\|Appendix\\|\\\\\\\\appendix\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "5fb1fa29-0f8c-42cc-af86-c02e991c1eba",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BA5rQ66W3FMVzebd9wXtGi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 32768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 672,
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


### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 33485,
    "tool_uses": 14,
    "duration_ms": 19339
  },
  "last_tool_name": "Bash",
  "uuid": "943fd4b5-b656-424d-a274-b0bb61c96355",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Bash · `toolu_017S2rZD7DgT2mfhPq7JMyZz`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/ | grep -E \"appendix|supp\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "a2321e77-22fa-499e-8221-b862138ab7f8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BA5rQ66W3FMVzebd9wXtGi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 32768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 672,
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

_source line 89 · 2026-05-18T17:43:26.403Z_

<details><summary>↩ Tool result · `toolu_01PaoeEysXZxhwyipjf9NL6W`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "a0bca3cc-9c08-47ff-898d-62ef5c5568ab"
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-18T17:43:26.421Z_

<details><summary>↩ Tool result · `toolu_017S2rZD7DgT2mfhPq7JMyZz`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "a4e8ada1-9b53-4c34-a22c-26d61600d1b2"
}
```

</details>

---


### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Reading registry.yaml",
  "usage": {
    "total_tokens": 30027,
    "tool_uses": 8,
    "duration_ms": 18981
  },
  "last_tool_name": "Read",
  "uuid": "b6c252fc-ab95-4636-b36d-b5f89cbbde32",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 92_

<details open><summary>🔧 Tool call — Read · `toolu_01SETCd7TQjfhfsz6GM73uRg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml",
  "offset": 3088,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "00b24a78-3f45-4e45-87db-cc3a008d7732",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QJ2TGAB6P73bHtjcQEZtaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 148,
      "cache_read_input_tokens": 29827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 148,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Reading artifacts/dream_reports/dream_20260515T222933/median/paper.tex",
  "usage": {
    "total_tokens": 33932,
    "tool_uses": 15,
    "duration_ms": 21553
  },
  "last_tool_name": "Read",
  "uuid": "19931f61-774f-43e2-93f7-297ffa0c104a",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Read · `toolu_01QhjXoW7kTYJngbTeQQeLtw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "9904c2c8-1caf-4a4b-9e9e-aefe7fb5dd67",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019c9GzYRU2VYS4cAkjscoJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 33440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 437,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 95 · 2026-05-18T17:43:28.525Z_

<details><summary>↩ Tool result · `toolu_01SETCd7TQjfhfsz6GM73uRg`</summary>

```text
3088	  ablation_50demos_main:
3089	    status: DONE
3090	    retry_count: 0
3091	    created_at: '2026-05-17T18:53:20.415Z'
3092	    updated_at: '2026-05-17T21:49:51.638Z'
3093	    hypothesis: '50-demo full-data ablation: L1 instruction-dominant heads capacity
3094	      trade-off (R² increase under ablation) persists with adequate probe training
3095	      data, eliminating underfitting confound from 5-demo version.'
3096	    spec:
3097	      command: CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py
3098	        --demos_per_task 50 --readout_layers 1 8 13
3099	      server: westd-19183
3100	      gpu: cuda:0
3101	      data_path: /root/autodl-tmp/vla-ssd/data/libero_goal/
3102	      data_count: 50 demos/task x 10 tasks x 3 conditions
3103	      model_name: openvla-7b (trained)
3104	      seed: 42
3105	      checkpoint_path: N/A (inference-only)
3106	      log_path: /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json
3107	    metrics:
3108	      baseline_L1: 0.5567
3109	      baseline_L8: 0.6199
3110	      baseline_L13: 0.6763
3111	      all24_L1: 0.6153
3112	      all24_L8: 0.6377
3113	      all24_L13: 0.6762
3114	      all32_L1: 0.5823
3115	      all32_L8: 0.6311
3116	      all32_L13: 0.6636
3117	      all24_vs_baseline_L1_delta: 0.0585
3118	      all24_vs_baseline_L1_p: 0
3119	      all24_vs_baseline_L1_CI:
3120	      - 0.042
3121	      - 0.0752
3122	      all24_vs_control8_L1_delta: 0.0421
3123	      all24_vs_control8_L1_p: 0
3124	      all24_vs_control8_L1_CI:
3125	      - 0.0286
3126	      - 0.0563
3127	    conclusion: success
3128	    completed_at: '2026-05-17T21:49:51.638Z'
3129	  ablation_50demos_control8:
3130	    status: DONE
3131	    retry_count: 0
3132	    created_at: '2026-05-17T18:53:21.900Z'
3133	    updated_at: '2026-05-17T19:57:09.980Z'
3134	    hypothesis: Ablating 8 non-dominant L1 heads (control) should NOT increase action
3135	      R², proving the capacity trade-off is specific to instruction-dominant heads.
3136	    spec:
3137	      command: CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_control8.py
3138	        --demos_per_task 50 --readout_layers 1 8 13
3139	      server: westd-19183
3140	      gpu: cuda:1
3141	      data_path: /root/autodl-tmp/vla-ssd/data/libero_goal/
3142	      data_count: 50 demos/task x 10 tasks x 1 condition
3143	      model_name: openvla-7b (trained)
3144	      seed: 42
3145	      checkpoint_path: N/A (inference-only)
3146	      log_path: /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos_control8.json
3147	    metrics:
3148	      ablate_control8_L1_R2: 0.5732
3149	      ablate_control8_L1_CI:
3150	      - 0.5149
3151	      - 0.6321
3152	      ablate_control8_L8_R2: 0.6311
3153	      ablate_control8_L8_CI:
3154	      - 0.5773
3155	      - 0.6834
3156	      ablate_control8_L13_R2: 0.6787
3157	      ablate_control8_L13_CI:
3158	      - 0.6322
3159	      - 0.7255
3160	    conclusion: success
3161	    completed_at: '2026-05-17T19:57:09.980Z'
3162	  llama2base_action_probe:
3163	    status: DONE
3164	    retry_count: 0
3165	    created_at: '2026-05-17T20:54:26.047Z'
3166	    updated_at: '2026-05-17T22:02:32.172Z'
3167	    spec:
3168	      command: bash -c "source /root/miniconda3/bin/activate base && cd /root/vla-ssd
3169	        && CUDA_VISIBLE_DEVICES=1 python scripts/llama2base_action_probe.py"
3170	      server: westd-19183
3171	      gpu: cuda:1
3172	      pid: '913312'
3173	      log_path: /root/autodl-tmp/vla-ssd/results/llama2base_action_probe/three_condition_comparison.json
3174	      submitted_at: '2026-05-17T20:55:56.743Z'
3175	      submitted_via: submit_training_job
3176	      backend: tmux
3177	      account: root
3178	      data_path: /root/autodl-tmp/vla-ssd/data/libero_goal/
3179	      data_count: 50 demos/task x 10 tasks
3180	      model_name: meta-llama/Llama-2-7b-hf (via OpenVLA architecture)
3181	      seed: 42
3182	      checkpoint_path: N/A (probe experiment, no checkpoint)
3183	      wall_clock_seconds: 3995.4
3184	      gpu_hours: 1.11
3185	    hypothesis: 'Llama-2 base (pretrained LLM, no VLA training) action R² follows
3186	      the three-condition gradient: untrained < llama2base < trained, completing the
3187	      C2 evidence chain for action encoding specialization.'
3188	    reproduce:
3189	      finished_at: '2026-05-17T21:57:33.185Z'
3190	    extra:
3191	      hook_events:
3192	      - event: on_complete
3193	        action: agent
3194	        ts: '2026-05-17T21:57:38.637406+00:00'
3195	    conclusion: success
3196	    metrics:
3197	      L1_untrained_R2: 0.5546
3198	      L1_llama2base_R2: 0.6366
3199	      L1_trained_R2: 0.6331
3200	      peak_untrained:
3201	        layer: L0
3202	        R2: 0.6403
3203	      peak_llama2base:
3204	        layer: L4
3205	        R2: 0.6447
3206	      peak_trained:
3207	        layer: L8
3208	        R2: 0.6553
3209	      mean_all_untrained: 0.4491
3210	      mean_all_llama2base: 0.6014
3211	      mean_all_trained: 0.5849
3212	      mean_L2_L9_untrained: 0.5294
3213	      mean_L2_L9_llama2base: 0.6347
3214	      mean_L2_L9_trained: 0.6463
3215	      pattern_L2_L9: U&lt;L&lt;T (19/21 layers)
3216	      pattern_L1: U&lt;L≈T (pretraining near ceiling)
3217	      pattern_late: L>T (VLA repurposes late layers)
3218	      result_path: /root/autodl-tmp/vla-ssd/results/llama2base_action_probe/three_condition_comparison.json
3219	    completed_at: '2026-05-17T22:02:32.172Z'
3220	  threecond_multiseed_r2:
3221	    status: DONE
3222	    retry_count: 0
3223	    created_at: '2026-05-18T06:09:57.814Z'
3224	    updated_at: '2026-05-18T08:50:31.406Z'
3225	    hypothesis: Multi-seed action probes will confirm that trained models yield higher
3226	      per-layer R² than untrained/llama2base with low variance across seeds, validating
3227	      that the single-seed result is robust.
3228	    parent: llama2base_action_probe
3229	    server: westd-19183
3230	    gpu: cuda:0
3231	    reproduce:
3232	      server: westd-19183
3233	      gpu: cuda:0
3234	      started_at: '2026-05-18T06:44:28.859Z'
3235	    spec:
3236	      command: source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=0
3237	        python scripts/threecond_multiseed_probe.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "0439ab8b-dcde-4b0a-9ae3-b8e950377079"
}
```

</details>

---


### Tool result

_source line 96 · 2026-05-18T17:43:28.814Z_

<details><summary>↩ Tool result · `toolu_01QhjXoW7kTYJngbTeQQeLtw`</summary>

```text
1	\documentclass[letterpaper]{article}
2	
3	\usepackage[margin=1in]{geometry}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{natbib}
8	\usepackage{hyperref}
9	\usepackage{xcolor}
10	\usepackage{multirow}
11	\usepackage{caption}
12	\usepackage{subcaption}
13	
14	\title{Where Do Action-Relevant Representations Come From in Vision-Language-Action Models?\\A Representational Analysis of OpenVLA}
15	
16	\author{
17	Anonymous Authors\\
18	CoRL 2026 Submission
19	}
20	
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	%==============================================================================
27	\begin{abstract}
28	%==============================================================================
29	Vision-Language-Action models (VLAs) fine-tune large language models on robot demonstration data to produce action tokens, yet the origin of action-relevant representational structure within VLAs remains poorly understood.
30	We present a systematic representational analysis of OpenVLA, decomposing the contributions of the frozen vision encoder (SigLIP), the learned projector, and the language model backbone.
31	Using Representational Similarity Analysis (RSA) across two LIBERO benchmarks and four experimental conditions (trained/untrained $\times$ with/without instruction), we find that:
32	(1)~the vision encoder plus projector already achieves high alignment with action structure (RSA $\rho=0.615$), far exceeding the full VLA ($\rho\approx0.488$) and a standalone vision model (DINOv2, $\rho=0.388$);
33	(2)~LLM processing does not enhance and partially disrupts action-relevant geometry, with a consistent drop of $\Delta\rho\approx0.13$ from projector output to the final hidden layer;
34	(3)~neither task-specific fine-tuning ($\Delta<0.01$) nor language instruction content ($\Delta<0.005$) meaningfully alters action-relevant structure in the LLM hidden states.
35	These findings are robust across two representational similarity metrics (RSA and CKA, Kendall $\tau=0.87$) and two task families (LIBERO-Goal and LIBERO-Spatial).
36	Our results suggest that action-relevant representations in OpenVLA-class architectures are predominantly inherited from the pretrained vision encoder, not learned through fine-tuning.
37	\end{abstract}
38	
39	%==============================================================================
40	\section{Introduction}
41	\label{sec:intro}
42	%==============================================================================
43	
44	Vision-Language-Action models (VLAs) have emerged as a promising paradigm for generalist robot policies~\citep{brohan2023rt2,kim2024openvla}.
45	By fine-tuning a pretrained vision-language model (VLM) on robot demonstration data, VLAs convert visual observations and language instructions into discretized action tokens.
46	The prevailing assumption is that task-specific fine-tuning teaches the LLM backbone to transform visual representations into action-relevant features---in effect, that fine-tuning injects new representational knowledge about how to act.
47	
48	However, this assumption has never been systematically verified at the representational level.
49	Recent work by \citet{grant2026visual} demonstrated at the \emph{behavioral} level that the visual pathway dominates VLA performance, but did not decompose which \emph{component} carries action-relevant representational structure or how that structure transforms through the processing pipeline.
50	Concurrently, findings that VLAs largely ignore language instruction content~\citep{hou2026langgap,fei2025liberoplus} and that fine-tuning erodes VLM reasoning capabilities~\citep{fang2025finetuning} raise questions about what fine-tuning actually changes inside these models.
51	
52	We address these questions through a systematic representational analysis of OpenVLA~\citep{kim2024openvla}, measuring how action-relevant structure is distributed across the vision encoder (SigLIP), projector, and LLM backbone.
53	Our methodology uses Representational Similarity Analysis (RSA)~\citep{kriegeskorte2008rsa} to quantify the alignment between internal representations and ground-truth action structure across 2 benchmarks and $2 \times 2$ experimental conditions (trained/untrained model $\times$ with/without instruction).
54	
55	Our three main findings challenge the implicit fine-tuning narrative:
56	
57	\begin{enumerate}
58	    \item \textbf{Vision encoder dominance.}
59	    SigLIP + projector representations achieve RSA $\rho=0.615$ with action structure---substantially higher than the full VLA ($\rho\approx0.488$) and DINOv2 ($\rho=0.388$).
60	    The vision encoder, not the LLM, is the primary source of action-relevant geometry.
61	
62	    \item \textbf{LLM does not enhance action-relevant structure.}
63	    Passing through the LLM reduces action alignment by $\Delta\rho\approx0.13$.
64	    Per-layer analysis reveals a net negative trend (Spearman $\rho=-0.62$ between layer index and RSA) with a partial recovery at intermediate layers (12--16) attributable to cross-modal integration, but the final layer remains well below the projector output.
65	
66	    \item \textbf{Training and instruction invariance.}
67	    The $2 \times 2$ matrix of conditions (trained/untrained $\times$ instruction/no-instruction) collapses into a narrow band ($\rho\in[0.480, 0.489]$; bootstrap CI for all pairwise differences includes zero).
68	    Instruction content provides weak contextual modulation ($\Delta\approx0.02$) that is an order of magnitude smaller than the architecture effect ($\Delta\approx0.13$).
69	\end{enumerate}
70	
71	These results are verified with CKA~\citep{kornblith2019cka} (Kendall $\tau=0.87$ agreement with RSA ordering) and replicated on LIBERO-Spatial (qualitatively identical conclusions).
72	Together, they suggest that for OpenVLA-class architectures, investment in vision encoder quality may yield larger returns than LLM fine-tuning for action-relevant representation.
73	
74	%==============================================================================
75	\section{Related Work}
76	\label{sec:related}
77	%==============================================================================
78	
79	\paragraph{Vision-Language-Action Models.}
80	VLAs adapt pretrained VLMs for robot control by fine-tuning on demonstration data~\citep{brohan2023rt2,kim2024openvla}.
81	OpenVLA~\citep{kim2024openvla} pairs a SigLIP vision encoder with a Llama-2 language model, connected via a learned MLP projector.
82	While VLAs achieve strong behavioral performance, the representational mechanisms underlying this success remain underexplored.
83	
84	\paragraph{Behavioral Analysis of VLAs.}
85	\citet{grant2026visual} showed that the visual pathway dominates VLA behavior using orthogonal fine-tuning ablations.
86	\citet{hou2026langgap} and \citet{fei2025liberoplus} demonstrated that VLAs often ignore language instruction content.
87	Our work complements these behavioral findings with a representational decomposition, revealing \emph{why} the visual pathway dominates and \emph{why} instructions have little effect.
88	
89	\paragraph{Representational Analysis.}
90	RSA~\citep{kriegeskorte2008rsa} and CKA~\citep{kornblith2019cka} are standard tools for comparing representational geometries across neural systems.
91	\citet{fang2025finetuning} used probing to show fine-tuning erodes VLM reasoning.
92	We apply similar methodology but focus on the action domain, systematically comparing representations before and after LLM processing.
93	
94	%==============================================================================
95	\section{Method}
96	\label{sec:method}
97	%==============================================================================
98	
99	\subsection{Architecture Decomposition}
100	
101	We decompose OpenVLA into three stages and extract representations at each:
102	\begin{itemize}
103	    \item \textbf{SigLIP + Projector output}: Visual features after the frozen SigLIP encoder and learned MLP projector, before entering the LLM. This is the ``input'' to the language model and represents the vision encoder's contribution.
104	    \item \textbf{LLM per-layer hidden states}: Representations at each of the 32 transformer layers of the Llama-2 backbone, capturing the progressive transformation applied by the LLM.
105	    \item \textbf{LLM final hidden state}: The last-layer representation used to predict action tokens.
106	\end{itemize}
107	We also extract representations from a standalone DINOv2~\citep{oquab2023dinov2} encoder (same input images, no projector or LLM) as a reference baseline.
108	
109	\subsection{Experimental Conditions}
110	
111	We use a $2 \times 2$ factorial design crossing two binary factors:
112	\begin{itemize}
113	    \item \textbf{Training}: Trained (fine-tuned on LIBERO demonstrations) vs.\ Untrained (pretrained VLM weights, no robot fine-tuning).
114	    \item \textbf{Instruction}: Real task instruction provided vs.\ no instruction input.
115	\end{itemize}
116	This yields four conditions that isolate the effects of training and instruction on internal representations.
117	We additionally run instruction ablations with three control conditions: random English words, wrong-task instructions, and a fixed nonsense string.
118	
119	\subsection{Representational Similarity Analysis}
120	
121	For each condition, we compute pairwise representational dissimilarity matrices (RDMs) over a set of observations from the LIBERO benchmark suite.
122	Action structure RDMs are computed from ground-truth action labels.
123	We measure alignment between representation RDMs and action RDMs using Spearman rank correlation ($\rho$).
124	Higher $\rho$ indicates that the representational geometry preserves more action-relevant structure.
125	
126	\subsection{Verification with CKA}
127	
128	To ensure findings are not metric-dependent, we replicate core analyses using Centered Kernel Alignment (CKA)~\citep{kornblith2019cka}, which compares kernel matrices rather than rank-based dissimilarity matrices.
129	CKA is invariant to isotropic scaling but sensitive to rotation, providing a complementary perspective to RSA.
130	
131	\subsection{Cross-Benchmark Validation}
132	
133	We conduct the full analysis on two LIBERO task families:
134	\textbf{LIBERO-Goal} (functional objectives, e.g., ``open the drawer'') and \textbf{LIBERO-Spatial} (spatial relation tasks, e.g., ``place the cup next to the plate'').
135	These task families stress different aspects of visual representation, enabling us to assess generalization within the LIBERO suite.
136	
137	%==============================================================================
138	\section{Experiments}
139	\label{sec:experiments}
140	%==============================================================================
141	
142	\subsection{Component-Level RSA Comparison}
143	\label{sec:exp_component}
144	
145	Table~\ref{tab:main_rsa} presents the core finding.
146	SigLIP + projector output achieves the highest alignment with action structure ($\rho=0.615$), substantially exceeding all four VLA conditions ($\rho\in[0.480, 0.489]$) and the DINOv2 baseline ($\rho=0.388$).
147	The gap between projector output and the best VLA condition is $\Delta\rho=0.126$, indicating that the LLM processing step \emph{reduces} action-relevant structure.
148	
149	\begin{table}[t]
150	\centering
151	\caption{RSA alignment ($\rho$) with action structure on LIBERO-Goal. SigLIP+projector output retains the highest action alignment; all four VLA conditions converge to a narrow band, well below the projector output.}
152	\label{tab:main_rsa}
153	\begin{tabular}{lcc}
154	\toprule
155	\textbf{Condition} & \textbf{RSA $\rho$} & \textbf{$\Delta$ vs.\ Projector} \\
156	\midrule
157	SigLIP + Projector & 0.615 & --- \\
158	\midrule
159	VLA Trained + Instruction & 0.488 & $-0.127$ \\
160	VLA Trained $-$ Instruction & 0.489 & $-0.126$ \\
161	VLA Untrained + Instruction & 0.485 & $-0.130$ \\
162	VLA Untrained $-$ Instruction & 0.480 & $-0.135$ \\
163	\midrule
164	DINOv2 (reference) & 0.388 & $-0.227$ \\
165	\bottomrule
166	\end{tabular}
167	\end{table}
168	
169	The $2 \times 2$ factorial analysis reveals:
170	\begin{itemize}
171	    \item \textbf{Training effect}: $\Delta\rho < 0.01$ between trained and untrained conditions. Bootstrap 95\% CI for the difference includes zero.
172	    \item \textbf{Instruction effect}: $\Delta\rho < 0.005$ between instruction and no-instruction conditions. CI includes zero.
173	\end{itemize}
174	The four VLA conditions span only a 0.009-wide band ($0.480$--$0.489$), confirming that neither training nor instruction meaningfully alters action-relevant structure in the final LLM hidden state.
175	
176	\subsection{Instruction Ablation with Random Controls}
177	\label{sec:exp_random_inst}
178	
179	To test whether instruction effects are driven by semantic content or merely by the presence of additional input tokens, we compare real instructions against three control conditions (Table~\ref{tab:random_inst}).
180	
181	\begin{table}[t]
182	\centering
183	\caption{Instruction ablation: RSA ($\rho$) under different instruction conditions. Real instructions provide a small advantage over random controls ($\Delta\approx0.02$), but this effect is an order of magnitude smaller than the architecture effect ($\Delta\approx0.13$).}
184	\label{tab:random_inst}
185	\begin{tabular}{lccc}
186	\toprule
187	\textbf{Condition} & \textbf{Trained} & \textbf{Untrained} & \textbf{Mean} \\
188	\midrule
189	Real instruction & 0.488 & 0.485 & 0.486 \\
190	No instruction & 0.489 & 0.480 & 0.485 \\
191	Random words & 0.468 & 0.460 & 0.464 \\
192	Wrong-task instruction & 0.472 & 0.465 & 0.469 \\
193	Fixed string (``aaaa bbbb'') & 0.462 & 0.455 & 0.459 \\
194	\midrule
195	DINOv2 (reference) & --- & --- & 0.388 \\
196	\bottomrule
197	\end{tabular}
198	\end{table}
199	
200	Real instructions yield a small advantage over the mean of random controls ($\Delta=0.021$ for trained, $\Delta=0.025$ for untrained), confirming that instruction semantic content provides measurable but weak contextual modulation.
201	Critically, this instruction effect ($\Delta\approx0.02$) is less than one-fifth of the architecture effect ($\Delta\approx0.127$; ratio $= 0.17$).
202	
203	Among the random controls, wrong-task instructions produce the highest RSA (they are syntactically valid robot instructions and activate similar attention patterns), while the fixed nonsense string produces the lowest (minimal token diversity yields minimal attention modulation).
204	Notably, all random instruction conditions yield \emph{lower} RSA than the no-instruction baseline, suggesting that semantically incoherent input tokens actively disrupt rather than modulate the representation.
205	
206	\subsection{Metric Robustness: CKA Verification}
207	\label{sec:exp_cka}
208	
209	Table~\ref{tab:cka} compares RSA and CKA across conditions.
210	The two metrics agree on the qualitative ordering of conditions (Kendall $\tau=0.87$) and on all core conclusions: SigLIP $\gg$ VLA $\gg$ DINOv2, and trained $\approx$ untrained.
211	However, the absolute gap between SigLIP and VLA is smaller under CKA ($0.06$) than under RSA ($0.127$).
212	
213	\begin{table}[t]
214	\centering
215	\caption{RSA vs.\ CKA comparison. Condition ordering is largely preserved (Kendall $\tau=0.87$). The SigLIP--VLA gap is attenuated under CKA, consistent with CKA's insensitivity to rotation-like transformations in the LLM.}
216	\label{tab:cka}
217	\begin{tabular}{lcccc}
218	\toprule
219	\textbf{Condition} & \textbf{RSA $\rho$} & \textbf{CKA} & \textbf{RSA rank} & \textbf{CKA rank} \\
220	\midrule
221	SigLIP + Projector & 0.615 & 0.53 & 1 & 1 \\
222	Trained + Inst & 0.488 & 0.47 & 2 & 3 \\
223	Trained $-$ Inst & 0.489 & 0.48 & 3 & 2 \\
224	Untrained + Inst & 0.485 & 0.46 & 4 & 4 \\
225	Untrained $-$ Inst & 0.480 & 0.45 & 5 & 5 \\
226	DINOv2 & 0.388 & 0.38 & 6 & 6 \\
227	\bottomrule
228	\end{tabular}
229	\end{table}
230	
231	\paragraph{Interpreting the gap discrepancy.}
232	CKA operates on kernel matrices and is insensitive to orthogonal transformations.
233	If the LLM primarily applies rotation-like transformations to visual representations---reorienting features toward the next-token prediction objective without destroying kernel structure---CKA would partially absorb this transformation while RSA (rank-based) would register the full change.
234	The gap attenuation is thus consistent with LLM processing being partly rotation-like, which disrupts \emph{rank-order} similarity (captured by RSA) more than \emph{kernel alignment} (captured by CKA).
235	
236	\paragraph{Per-layer reversals.}
237	At the per-layer level, CKA and RSA disagree on condition ordering at 4 of 33 layers (layers 7, 15, 22, and 29), with a maximum reversal magnitude of 0.03.
238	These reversals occur at layers where trained and untrained representations are nearly indistinguishable, and the reversal magnitudes are within bootstrap confidence intervals.
239	Both metrics agree on the critical comparisons: SigLIP $>$ VLA at every layer, and the training effect CKA CI of $[-0.04, 0.07]$ includes zero.
240	
241	\begin{table}[t]
242	\centering
243	\caption{Metric agreement statistics between RSA and CKA.}
244	\label{tab:metric_agreement}
245	\begin{tabular}{lc}
246	\toprule
247	\textbf{Metric} & \textbf{Value} \\
248	\midrule
249	Kendall $\tau$ (condition ordering) & 0.87 \\
250	Per-layer ordering reversals & 4 / 33 \\
251	Max reversal magnitude & 0.03 \\
252	Both metrics: SigLIP $>$ VLA? & Yes \\
253	Both metrics: trained $\approx$ untrained? & Yes (CI incl.\ 0) \\
254	\bottomrule
255	\end{tabular}
256	\end{table}
257	
258	\subsection{Cross-Benchmark Validation: LIBERO-Spatial}
259	\label{sec:exp_spatial}
260	
261	To rule out benchmark-specific artifacts, we replicate the full analysis on LIBERO-Spatial, which emphasizes spatial relationships (``place X next to Y'') rather than functional goals (Table~\ref{tab:spatial}).
262	
263	\begin{table}[t]
264	\centering
265	\caption{Cross-benchmark comparison: LIBERO-Goal vs.\ LIBERO-Spatial. All qualitative conclusions replicate. Absolute RSA values are uniformly lower on Spatial tasks, consistent with reduced alignment between contrastive pretraining features and spatial-relation action structure.}
266	\label{tab:spatial}
267	\begin{tabular}{lccc}
268	\toprule
269	\textbf{Condition} & \textbf{LIBERO-Goal} & \textbf{LIBERO-Spatial} & $\boldsymbol{\Delta}$ \\
270	\midrule
271	SigLIP + Projector & 0.615 & 0.580 & $-0.035$ \\
272	Trained + Inst & 0.488 & 0.460 & $-0.028$ \\
273	Untrained + Inst & 0.485 & 0.450 & $-0.035$ \\
274	DINOv2 & 0.388 & 0.350 & $-0.038$ \\
275	\midrule
276	SigLIP--VLA gap & 0.127 & 0.120 & $-0.007$ \\
277	Training effect & $<0.01$ & 0.01 & --- \\
278	Instruction effect & $<0.005$ & 0.01 & --- \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	All qualitative conclusions replicate: the ordering SigLIP $\gg$ VLA $\gg$ DINOv2 is preserved, the SigLIP--VLA gap is comparable ($0.12$ vs.\ $0.127$), training and instruction effects remain negligible (bootstrap CIs include zero), and the per-layer degradation trend is present (Spearman $\rho=-0.55$) with a mid-layer bump at layers 10--14.
284	
285	Absolute RSA values are uniformly lower by approximately $0.03$ on LIBERO-Spatial.
286	This is expected: spatial-relation tasks demand fine-grained positional features that are less strongly encoded by SigLIP's image-text contrastive pretraining compared to object-identity features relevant to LIBERO-Goal.
287	The consistent downward shift across all conditions suggests it reflects a task--encoder interaction rather than a change in the relative contributions of VLA components.
288	
289	%==============================================================================
290	\section{Discussion}
291	\label{sec:discussion}
292	%==============================================================================
293	
294	\paragraph{The vision encoder as the primary source.}
295	Our results converge on a clear picture: action-relevant representational structure in OpenVLA is predominantly determined by the frozen SigLIP vision encoder and projector, not learned through task-specific fine-tuning or shaped by instruction input.
296	The LLM backbone, rather than enhancing this structure, partially disrupts it---consistent with the LLM optimizing representations for next-token prediction, an objective that does not prioritize preservation of action-relevant geometry.
297	
298	\paragraph{Information routing in intermediate layers.}
299	The per-layer analysis reveals that action alignment does not degrade monotonically (Spearman $\rho=-0.62$ between layer index and RSA, with 8 monotonicity violations).
300	Layers 12--16 show a partial recovery of action structure ($\Delta\approx0.06$ above the surrounding trend), which we attribute to cross-modal integration: at these intermediate layers, attention between vision tokens and instruction tokens creates transient binding patterns that partially restore action-relevant geometric alignment.
301	However, this recovery is not sustained---subsequent layers continue the overall degradation, and the final-layer RSA ($0.47$) remains well below the projector output ($0.615$).
302	
303	\paragraph{Instruction content provides weak contextual modulation.}
304	The random instruction experiment reveals that instruction semantic content does have a small, measurable effect ($\Delta\approx0.02$ over random controls).
305	We acknowledge that instructions provide weak contextual modulation of action-relevant structure.
306	However, this effect is less than one-fifth of the architecture-level determination of action structure ($\Delta\approx0.13$), confirming that instruction content is not a primary driver of action-relevant representations.
307	The finding that even random instructions produce non-zero effects suggests that attention routing itself---not semantic content---is the primary mechanism of instruction modulation.
308	
309	\paragraph{Metric robustness.}
310	The CKA verification confirms that our conclusions are not an artifact of RSA's specific sensitivity profile.
311	The gap attenuation under CKA (SigLIP--VLA gap of $0.06$ vs.\ $0.127$) is interpretable: CKA absorbs rotation-like transformations that the LLM applies, while RSA registers the full representational reorientation.
312	The consistent \emph{direction} across two independent metrics (Kendall $\tau=0.87$) is more informative than the absolute magnitude under either metric alone.
313	
314	\paragraph{Practical implications.}
315	These findings suggest three actionable directions for VLA design:
316	(1)~Investing in vision encoder pretraining quality (e.g., better contrastive objectives, spatial-aware pretraining) may yield larger returns than LLM fine-tuning strategies for action-relevant representation.
317	(2)~Downstream tasks that require action-relevant features should consider using projector output directly rather than final LLM hidden states.
318	(3)~VLA architectures should explore mechanisms to reduce representational disruption during LLM processing, such as residual connections from the projector to the action head or representation-preserving fine-tuning objectives.
319	
320	\paragraph{Limitations.}
321	Our analysis is limited to the OpenVLA architecture (SigLIP + Llama-2).
322	While OpenVLA is among the most widely used open-source VLAs, generalization to architecturally different VLAs (e.g., those using different vision encoders, cross-attention instead of prefix tuning, or diffusion action heads) requires further investigation.
323	Both benchmarks are within the LIBERO simulation suite with a single robot morphology; extension to real-robot settings and diverse embodiments is an important direction.
324	RSA and CKA measure representational geometry but do not directly assess whether preserved structure is \emph{used} by the downstream action head---the functional relevance of geometric alignment remains an open question.
325	
326	%==============================================================================
327	\section{Conclusion}
328	\label{sec:conclusion}
329	%==============================================================================
330	
331	We presented a systematic representational analysis of OpenVLA, revealing that action-relevant structure is primarily inherited from the pretrained vision encoder rather than learned through LLM fine-tuning.
332	The LLM backbone does not enhance---and partially disrupts---this structure, while task-specific training and instruction content have negligible effects on action-relevant geometry.
333	These findings, validated across two metrics and two benchmarks, suggest that the representational locus of action competence in VLAs may lie upstream of the components most commonly optimized.
334	
335	%==============================================================================
336	\appendix
337	\section{Per-Layer RSA Degradation Curve}
338	\label{app:perlayer}
339	%==============================================================================
340	
341	Table~\ref{tab:perlayer} reports the full per-layer RSA profile from the SigLIP+projector output through all 32 LLM layers (trained model with instruction, LIBERO-Goal).
342	
343	\begin{table}[h]
344	\centering
345	\caption{Per-layer RSA ($\rho$) with action structure. The overall trend is negative (Spearman $\rho=-0.62$), but layers 12--16 show a partial recovery attributable to cross-modal integration.}
346	\label{tab:perlayer}
347	\begin{tabular}{lccc}
348	\toprule
349	\textbf{Layer} & \textbf{RSA $\rho$} & $\boldsymbol{\Delta}$ \textbf{vs.\ prev} & $\boldsymbol{\Delta}$ \textbf{vs.\ Projector} \\
350	\midrule
351	Projector & 0.615 & --- & 0.000 \\
352	L0 & 0.580 & $-0.035$ & $-0.035$ \\
353	L4 & 0.510 & $-0.013$ & $-0.105$ \\
354	L8 & 0.470 & $-0.008$ & $-0.145$ \\
355	L12 & 0.520 & $+0.015$ & $-0.095$ \\
356	L14 & 0.530 & $+0.005$ & $-0.085$ \\
357	L16 & 0.510 & --- & $-0.105$ \\
358	L20 & 0.490 & $-0.008$ & $-0.125$ \\
359	L24 & 0.480 & --- & $-0.135$ \\
360	L28 & 0.470 & $-0.005$ & $-0.145$ \\
361	L30 & 0.490 & --- & $-0.125$ \\
362	L32 & 0.470 & $-0.005$ & $-0.145$ \\
363	\bottomrule
364	\end{tabular}
365	\end{table}
366	
367	The curve exhibits three phases:
368	(1)~\emph{Early rapid decline} (L0--L8): RSA drops from $0.58$ to $0.47$ as initial transformer layers perform token mixing and positional encoding integration, substantially disrupting action-relevant geometry.
369	(2)~\emph{Mid-layer recovery} (L12--L16): RSA rebounds to $\sim$0.52--0.53. We interpret this as an information routing phenomenon---cross-modal attention at these layers creates transient binding between vision and instruction tokens that partially restores action-relevant spatial structure.
370	(3)~\emph{Late-stage plateau} (L20--L32): RSA oscillates in the $0.47$--$0.49$ range. A small uptick at L30 may reflect output preparation compressing representations in a way that incidentally preserves low-rank action structure.
371	
372	Overall Spearman correlation between layer index and RSA is $\rho=-0.62$, confirming a net downward trend but far from perfect monotonicity (8 monotonicity violations across 33 measurement points).
373	The endpoint comparison---projector output ($0.615$) vs.\ final layer ($0.47$), a drop of $0.145$---is the most robust summary statistic.
374	
375	%==============================================================================
376	\section{LIBERO-Spatial Detailed Results}
377	\label{app:spatial}
378	%==============================================================================
379	
380	On LIBERO-Spatial, the per-layer degradation trend is qualitatively similar (Spearman $\rho=-0.55$) with the mid-layer bump shifted to layers 10--14, consistent with spatial tasks engaging cross-modal integration slightly earlier.
381	The $2\times2$ matrix spans $[0.44, 0.46]$ with bootstrap CIs including zero for all pairwise differences.
382	
383	\bibliographystyle{plainnat}
384	\begin{thebibliography}{10}
385	
386	\bibitem[Brohan et~al.(2023)]{brohan2023rt2}
387	Anthony Brohan, Noah Brown, Justice Carbajal, et~al.
388	\newblock RT-2: Vision-language-action models transfer web knowledge to robotic control.
389	\newblock \emph{arXiv preprint arXiv:2307.15818}, 2023.
390	
391	\bibitem[Fang et~al.(2025)]{fang2025finetuning}
392	Yuxin Fang, Shusheng Yang, Shijie Wang, et~al.
393	\newblock Fine-tuning erodes pretrained reasoning in vision-language models.
394	\newblock In \emph{Proceedings of ICML}, 2025.
395	
396	\bibitem[Fei et~al.(2025)]{fei2025liberoplus}
397	Hongjie Fei, Rui Liu, Jinxin Liu, et~al.
398	\newblock Do VLAs really understand language? Evaluating instruction following in LIBERO-Plus.
399	\newblock \emph{arXiv preprint arXiv:2501.xxxx}, 2025.
400	
401	\bibitem[Grant et~al.(2026)]{grant2026visual}
402	Edward Grant, Simone Parisi, et~al.
403	\newblock The visual pathway dominates action prediction in vision-language-action models.
404	\newblock In \emph{Proceedings of ICRA}, 2026.
405	
406	\bibitem[Hou et~al.(2026)]{hou2026langgap}
407	Wenlong Hou, et~al.
408	\newblock LangGap: Measuring and closing the language grounding gap in VLAs.
409	\newblock In \emph{Proceedings of RSS}, 2026.
410	
411	\bibitem[Kim et~al.(2024)]{kim2024openvla}
412	Moo~Jin Kim, Karl Pertsch, Siddharth Karamcheti, et~al.
413	\newblock OpenVLA: An open-source vision-language-action model.
414	\newblock In \emph{Proceedings of CoRL}, 2024.
415	
416	\bibitem[Kornblith et~al.(2019)]{kornblith2019cka}
417	Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton.
418	\newblock Similarity of neural network representations revisited.
419	\newblock In \emph{Proceedings of ICML}, 2019.
420	
421	\bibitem[Kriegeskorte et~al.(2008)]{kriegeskorte2008rsa}
422	Nikolaus Kriegeskorte, Marieke Mur, and Peter Bandettini.
423	\newblock Representational similarity analysis---connecting the branches of systems neuroscience.
424	\newblock \emph{Frontiers in Systems Neuroscience}, 2:4, 2008.
425	
426	\bibitem[Oquab et~al.(2023)]{oquab2023dinov2}
427	Maxime Oquab, Timoth{\'e}e Darcet, Th{\'e}o Moutakanni, et~al.
428	\newblock DINOv2: Learning robust visual features without supervision.
429	\newblock \emph{arXiv preprint arXiv:2304.07193}, 2023.
430	
431	\end{thebibliography}
432	
433	\end{document}
434	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "c3db133e-774a-4028-9a9c-28c4625ff28a"
}
```

</details>

---


### System

_source line 97_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Reading registry.yaml",
  "usage": {
    "total_tokens": 32858,
    "tool_uses": 9,
    "duration_ms": 21306
  },
  "last_tool_name": "Read",
  "uuid": "f2c20643-21d9-47c9-8bbc-2672de2a91a5",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 98_

<details open><summary>🔧 Tool call — Read · `toolu_01N1uAHG8PNWaugwaey2Czqr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml",
  "offset": 3333,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "0bb4c40b-c6d7-4875-a98a-5359d5e7e7de",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HCdK1RGSoBCZ2Y6wVWnzB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2829,
      "cache_read_input_tokens": 29975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2829,
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

_source line 99 · 2026-05-18T17:43:30.849Z_

<details><summary>↩ Tool result · `toolu_01N1uAHG8PNWaugwaey2Czqr`</summary>

```text
3333	  threecond_multiseed_r2_v2:
3334	    status: DONE
3335	    retry_count: 0
3336	    created_at: '2026-05-18T08:04:22.860Z'
3337	    updated_at: '2026-05-18T09:11:34.295Z'
3338	    hypothesis: Multi-seed action probes (3 seeds, sequential split matching original
3339	      experiment) will confirm trained > llama2base > untrained R² gradient with low
3340	      seed variance, validating single-seed findings are robust and not split-dependent.
3341	    parent: threecond_multiseed_r2
3342	    spec:
3343	      command: bash -c "source /root/miniconda3/bin/activate base && cd /root/vla-ssd
3344	        && CUDA_VISIBLE_DEVICES=0 python scripts/threecond_multiseed_probe_v2.py 2>&1
3345	        | tee /root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.log"
3346	      server: westd-19183
3347	      data_path: /root/autodl-tmp/vla-ssd/features/{trained,untrained,llama2base}_libero_goal/
3348	      data_count: 10 tasks x 50 demos x 3 conditions
3349	      model_name: ActionMLPProbe(4096->256->7)
3350	      seed: 42,123,456
3351	      split: sequential_80_20_no_shuffle
3352	      r2_space: original_denormalized
3353	      checkpoint_source: pre-extracted features from openvla-7b / openvla-7b-untrained
3354	        / openvla-7b-llama2base
3355	      eval_data: /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ (10 tasks, 50 demos,
3356	        sequential split demo_0-39 train / demo_40-49 val)
3357	      checkpoint_path: N/A (probe experiment)
3358	      log_path: /root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.log
3359	    reproduce:
3360	      finished_at: '2026-05-18T08:47:23.230Z'
3361	    extra:
3362	      hook_events:
3363	      - event: on_complete
3364	        action: agent
3365	        ts: '2026-05-18T08:47:26.372903+00:00'
3366	    metrics:
3367	      conditions:
3368	      - untrained
3369	      - llama2base
3370	      - trained
3371	      seeds:
3372	      - 42
3373	      - 123
3374	      - 456
3375	      trained_peak:
3376	        layer: 9
3377	        mean_R2: 0.643
3378	        std: 0.014
3379	      L0_baseline:
3380	        mean_R2: 0.645
3381	        std: 0.008
3382	        note: three conditions consistent at L0
3383	      pattern_L1_L15: U&lt;L&lt;T
3384	      pattern_L16_L25: L≈T>>U
3385	      pattern_L32: reversal
3386	      split: sequential (demo_0-39 train, demo_40-49 val)
3387	      r2_space: original (denormalized)
3388	      result_path: /root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.json
3389	    conclusion: success
3390	    completed_at: '2026-05-18T09:10:58.657Z'
3391	    notes: v2 修正版（顺序 split + 反归一化 R²）。trained peak L9 0.643±0.014, llama2base peak
3392	      L12 0.634±0.013, untrained peak L1 0.547±0.008 (排除 L32 异常 0.589±0.007)。L0=0.645
3393	      三条件一致（共享 vision encoder）。trained-llama2base gap small (0.009 at peak, n=3),
3394	      direction consistent。llama2base v2=0.634 vs llama2base_action_probe registry
3395	      peak L4=0.6447，差距 0.010 在 seed 方差内，一致。untrained 中间层崩溃（负 R² + 高方差）是最强信号。
3396	  random_subset_ablation:
3397	    status: DONE
3398	    retry_count: 0
3399	    created_at: '2026-05-18T08:25:38.132Z'
3400	    updated_at: '2026-05-18T08:27:15.118Z'
3401	    hypothesis: Random subsets of 24 heads yield higher action R² increase than instruction-dominant
3402	      24 heads, indicating dominant heads serve dual routing-encoding function rather
3403	      than pure capacity trade-off
3404	    parent: ablation_50demos_main
3405	    spec:
3406	      command: python scripts/random_subset_ablation.py --n_demos 50 --n_random 10
3407	        --output /root/autodl-tmp/vla-ssd/results/random_subset_ablation.json
3408	      server: westd-19183
3409	      data_path: /root/autodl-tmp/vla-ssd/features/trained_libero_goal/
3410	      data_count: 10 tasks x 50 demos
3411	      model_name: ActionMLPProbe(4096->256->7) with L1 head ablation
3412	      seed: 10 random seeds for subset selection
3413	      checkpoint_source: pre-extracted features from openvla-7b (trained)
3414	      eval_data: /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ (10 tasks, 50 demos,
3415	        sequential split)
3416	      checkpoint_path: N/A (probe experiment, no checkpoint saved)
3417	      log_path: /root/autodl-tmp/vla-ssd/results/random_subset_ablation.json
3418	    metrics:
3419	      baseline_r2: 0.517
3420	      dominant_24_delta: 0.042
3421	      random_24_mean_delta: 0.077
3422	      random_24_std_delta: 0.013
3423	      z_score: -2.73
3424	      p_value: 0.003
3425	      n_random_seeds: 10
3426	      interpretation: dominant-24 heads NOT special - any 24/32 heads ablation produces
3427	        similar or larger R² increase
3428	      result_path: /root/autodl-tmp/vla-ssd/results/random_subset_ablation.json
3429	      figure_path: /root/autodl-tmp/vla-ssd/results/figures/fig_random_subset_ablation.pdf
3430	    conclusion: success
3431	    notes: Plan C (D061) 核心证据。Dominant-24 heads 不具有特异性——10 组随机 24-head 子集的 R² 增量均高于
3432	      dominant-24（z=-2.73, p=0.003）。支持 dual routing-encoding function 解释。
3433	    completed_at: '2026-05-18T08:27:15.118Z'
3434	  behavioral_pilot:
3435	    status: PREPARING
3436	    retry_count: 0
3437	    created_at: '2026-05-18T09:25:24.217Z'
3438	    updated_at: '2026-05-18T09:25:31.366Z'
3439	    hypothesis: Ablating L1 instruction-dominant heads during VLA inference will measurably
3440	      change task success rate, providing behavioral evidence that these heads serve
3441	      a functional role beyond representational reorganization measured by probes.
3442	    parent: ablation_50demos_main
3443	  behavioral_pilot_w4:
3444	    status: DONE
3445	    retry_count: 0
3446	    created_at: '2026-05-18T09:34:21.677Z'
3447	    updated_at: '2026-05-18T10:34:21.649Z'
3448	    hypothesis: Ablating L1 instruction-dominant heads (24/32) during VLA inference
3449	      changes task success rate, providing behavioral evidence that attention head
3450	      specialization has functional consequences beyond representation-level metrics.
3451	    parent: ablation_50demos_main
3452	    spec:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "a4f8fa9f-1cd8-43b3-819d-b4858757824c"
}
```

</details>

---


### System

_source line 100_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running grep -n \"^\\\\\\\\section\\|^\\\\\\\\subsection\" /home/ubu…",
  "usage": {
    "total_tokens": 43357,
    "tool_uses": 16,
    "duration_ms": 24859
  },
  "last_tool_name": "Bash",
  "uuid": "2d881923-7728-450a-b55d-7faa6b5c4de4",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 101_

<details open><summary>🔧 Tool call — Bash · `toolu_01QA5N1jhPv7YmWU7T2dWjrG`</summary>

```json
{
  "command": "grep -n \"^\\\\\\\\section\\|^\\\\\\\\subsection\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "f8db8d98-cf2a-417d-bfb0-dc16e76d01b9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sxh8udBt4YbSJ4nSR89dKE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9424,
      "cache_read_input_tokens": 33877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9424,
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

_source line 102 · 2026-05-18T17:43:31.903Z_

<details><summary>↩ Tool result · `toolu_01QA5N1jhPv7YmWU7T2dWjrG`</summary>

```text
1:\section{Experiments}
4:\subsection{Experimental Setup}
32:\subsection{Vision Encoder Dominance}
93:\subsection{LLM Redistributes, Does Not Enhance, Action Structure}
145:\subsection{Training Routes, Does Not Create, Action Geometry}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "c65b041a-114a-42d6-8b4e-05fe81610e5a"
}
```

</details>

---


### System

_source line 103_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running grep -rn \"convergent evidence\\|convergent\\|1\\.\\|2…",
  "usage": {
    "total_tokens": 43358,
    "tool_uses": 17,
    "duration_ms": 25240
  },
  "last_tool_name": "Bash",
  "uuid": "b14abcea-3908-4798-a328-7f4d0ffb4b5f",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 104_

<details open><summary>🔧 Tool call — Bash · `toolu_01FsjxGkZoXz8EW9L9263MUw`</summary>

```json
{
  "command": "grep -rn \"convergent evidence\\|convergent\\|1\\.\\|2\\.\\|3\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/discussion.tex | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "953c534c-3e05-4d25-814d-ce7b73618853",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sxh8udBt4YbSJ4nSR89dKE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9424,
      "cache_read_input_tokens": 33877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9424,
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

_source line 105 · 2026-05-18T17:43:32.308Z_

<details><summary>↩ Tool result · `toolu_01FsjxGkZoXz8EW9L9263MUw`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "dfbde276-8b99-41bd-8ec2-be062b9c7927"
}
```

</details>

---


### System

_source line 106_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Reading registry.yaml",
  "usage": {
    "total_tokens": 35360,
    "tool_uses": 10,
    "duration_ms": 23695
  },
  "last_tool_name": "Read",
  "uuid": "fc43f824-6cf3-4432-b6de-c33093c60771",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 107_

<details open><summary>🔧 Tool call — Read · `toolu_01WZ43EMpEX8j3PvtfiQgFDr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml",
  "offset": 3485,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "f354b8f3-9855-4dce-92eb-c192cea08dc3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C58HLsHGswQTvYMsc8JfRa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2501,
      "cache_read_input_tokens": 32804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2501,
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

_source line 108 · 2026-05-18T17:43:33.236Z_

<details><summary>↩ Tool result · `toolu_01WZ43EMpEX8j3PvtfiQgFDr`</summary>

```text
3485	  action_trajectory_analysis:
3486	    status: DONE
3487	    retry_count: 0
3488	    created_at: '2026-05-18T10:35:18.923Z'
3489	    updated_at: '2026-05-18T11:02:27.281Z'
3490	    hypothesis: L1 instruction-dominant head ablation significantly changes OpenVLA
3491	      action predictions (measured by action token divergence and per-dimension MSE),
3492	      demonstrating that instruction routing heads directly influence model output,
3493	      not just intermediate representations.
3494	    parent: ablation_50demos_main
3495	    spec:
3496	      command: bash -c "source /root/miniconda3/bin/activate base && cd /root/vla-ssd
3497	        && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_analysis.py"
3498	      server: westd-19183
3499	      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal/
3500	      data_count: 5 tasks x 10 demos x 50 timesteps = 2500 forward passes x 2 conditions
3501	      model_name: OpenVLA-7b (openvla-7b base pretrained)
3502	      seed: '42'
3503	      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
3504	      eval_data: LIBERO-Goal demo observations (open-loop, no execution)
3505	      checkpoint_path: N/A (inference only)
3506	      log_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.log
3507	    metrics:
3508	      paired_action_mse:
3509	        mean: 0.0416
3510	        std: 0.0639
3511	        t_stat: 32.56
3512	        p_value: 3.99e-194
3513	        cohens_d: 0.651
3514	      token_divergence_rate: 0.723
3515	      per_dim_action_shift_means:
3516	      - 0.0019
3517	      - 0.0053
3518	      - 0.0076
3519	      - 0.0206
3520	      - 0.0307
3521	      - 0.0339
3522	      - 0.2907
3523	      per_dim_names:
3524	      - dx
3525	      - dy
3526	      - dz
3527	      - rx
3528	      - ry
3529	      - rz
3530	      - gripper
3531	      kl_divergence:
3532	        mean: 5.079
3533	        std: 4.961
3534	      mse_vs_gt_baseline: 0.432
3535	      mse_vs_gt_ablated: 0.436
3536	      wilcoxon_p: 0
3537	      n_tasks: 5
3538	      n_samples: 2500
3539	      all_tasks_significant: true
3540	      per_task_cohens_d_range:
3541	      - 0.433
3542	      - 0.729
3543	      result_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json
3544	    conclusion: success
3545	    completed_at: '2026-05-18T11:02:27.281Z'
3546	  action_trajectory_control:
3547	    status: DONE
3548	    retry_count: 0
3549	    created_at: '2026-05-18T11:34:36.585Z'
3550	    updated_at: '2026-05-18T12:59:24.419Z'
3551	    hypothesis: Ablating 8 non-instruction heads (control) produces significantly
3552	      smaller action divergence (especially gripper dimension) than ablating 24 instruction-dominant
3553	      heads, proving the action output effect is instruction-specific rather than
3554	      generic perturbation.
3555	    parent: action_trajectory_analysis
3556	    spec:
3557	      command: bash -c "source /root/miniconda3/bin/activate base && cd /root/vla-ssd
3558	        && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_control.py
3559	        2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log"
3560	      server: westd-19183
3561	      gpu:
3562	      - cuda:0
3563	      pid: '47936'
3564	      log_path: ~/runs/vla-ssd/action_trajectory_control.log
3565	      submitted_at: '2026-05-18T11:53:06.410Z'
3566	      submitted_via: submit_training_job
3567	      backend: tmux
3568	      account: root
3569	    reproduce:
3570	      finished_at: '2026-05-18T11:42:54.772Z'
3571	    extra:
3572	      hook_events:
3573	      - event: on_complete
3574	        action: agent
3575	        ts: '2026-05-18T11:42:57.559215+00:00'
3576	    metrics:
3577	      paired_action_mse:
3578	        mean: 0.0201
3579	        std: 0.0489
3580	        t_stat: 20.54
3581	        p_value: 9.0e-87
3582	        cohens_d: 0.41
3583	      token_divergence_rate: 0.293
3584	      per_dim_action_shift:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "6c9c3b38-ea58-433c-bc23-11c89dab004e"
}
```

</details>

---


### System

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 43743,
    "tool_uses": 18,
    "duration_ms": 27201
  },
  "last_tool_name": "Bash",
  "uuid": "3d714322-37a1-4a00-afa1-ff306b972626",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 110_

<details open><summary>🔧 Tool call — Bash · `toolu_01P1QDzPvT42KMiKtUY3fvpY`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts -type f -name \"*.tex\" -exec grep -l \"4\\.1\\|4\\.2\\|4\\.3\\|§4\" {} \\;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "6beeb37d-ae47-43fd-99f5-3a734d3b45e2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FEa7SUmQCs6oXyGPAKgaZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 376,
      "cache_read_input_tokens": 43301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 376,
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

_source line 111 · 2026-05-18T17:43:34.266Z_

<details><summary>↩ Tool result · `toolu_01P1QDzPvT42KMiKtUY3fvpY`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "e012d35d-2faf-4467-9b28-65ea6d606091"
}
```

</details>

---


### System

_source line 112_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 43747,
    "tool_uses": 19,
    "duration_ms": 27464
  },
  "last_tool_name": "Bash",
  "uuid": "2f872123-fc25-4165-ab9d-55e597fd13d0",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 113_

<details open><summary>🔧 Tool call — Bash · `toolu_011WtMwYdFvqgkvT4ZUYVMut`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts -type f -name \"*.tex\" -exec grep -l \"A\\.8\\|appendix.*8\" {} \\;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "e510d13b-d526-45aa-a5ea-2d6efefb43ae",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FEa7SUmQCs6oXyGPAKgaZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 376,
      "cache_read_input_tokens": 43301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 376,
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

_source line 114 · 2026-05-18T17:43:34.534Z_

<details><summary>↩ Tool result · `toolu_011WtMwYdFvqgkvT4ZUYVMut`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "e06b53c5-4c34-4970-a00c-82b1536b73c4"
}
```

</details>

---


### System

_source line 115_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Reading registry.yaml",
  "usage": {
    "total_tokens": 37177,
    "tool_uses": 11,
    "duration_ms": 25745
  },
  "last_tool_name": "Read",
  "uuid": "9e5974d8-b84e-4b1a-af02-8829dab20fa1",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 116_

<details open><summary>🔧 Tool call — Read · `toolu_017RQfV8e7r9AUB8HfU3iMFQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml",
  "offset": 3576,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "90b967b9-4ef5-46e4-86bf-06ef97901de7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UCu2aRxBJ7X5TKmrejx7Tm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 1812,
      "cache_read_input_tokens": 35305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1812,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 117 · 2026-05-18T17:43:35.286Z_

<details><summary>↩ Tool result · `toolu_017RQfV8e7r9AUB8HfU3iMFQ`</summary>

```text
3576	    metrics:
3577	      paired_action_mse:
3578	        mean: 0.0201
3579	        std: 0.0489
3580	        t_stat: 20.54
3581	        p_value: 9.0e-87
3582	        cohens_d: 0.41
3583	      token_divergence_rate: 0.293
3584	      per_dim_action_shift:
3585	        dx: 0.00037
3586	        dy: 0.00125
3587	        dz: 0.00243
3588	        rx: 0.00785
3589	        ry: 0.01387
3590	        rz: 0.01783
3591	        gripper: 0.1407
3592	      kl_divergence:
3593	        mean: 1.69
3594	        std: 3.7
3595	      wilcoxon_p: 8.0e-235
3596	      config:
3597	        n_tasks: 5
3598	        n_demos_per_task: 10
3599	        n_timesteps_per_demo: 50
3600	        total_forward_passes: 5000
3601	        ablated_heads:
3602	        - 3
3603	        - 5
3604	        - 6
3605	        - 9
3606	        - 13
3607	        - 21
3608	        - 24
3609	        - 28
3610	      per_task:
3611	        open_middle_drawer:
3612	          mse: 0.0071
3613	          cohens_d: 0.24
3614	          token_div: 0.24
3615	        open_top_drawer_put_bowl:
3616	          mse: 0.0258
3617	          cohens_d: 0.48
3618	          token_div: 0.304
3619	        push_plate_to_stove:
3620	          mse: 0.0213
3621	          cohens_d: 0.42
3622	          token_div: 0.306
3623	        put_bowl_on_plate:
3624	          mse: 0.0227
3625	          cohens_d: 0.44
3626	          token_div: 0.299
3627	        put_bowl_on_stove:
3628	          mse: 0.0236
3629	          cohens_d: 0.45
3630	          token_div: 0.313
3631	      comparison_vs_instruction_ablation:
3632	        instruction_24heads_mse: 0.0416
3633	        control_8heads_mse: 0.0201
3634	        mse_ratio: 2.07
3635	        instruction_token_div: 0.723
3636	        control_token_div: 0.293
3637	        div_ratio: 2.47
3638	        instruction_kl: 5.079
3639	        control_kl: 1.69
3640	        kl_ratio: 3
3641	        instruction_gripper: 0.291
3642	        control_gripper: 0.141
3643	        gripper_ratio: 2.07
3644	        head_count_ratio: 3
3645	        note: Ratios (2.0-3.0x) are at or below head count ratio (3:1), meaning per-head
3646	          effect of control heads is comparable to instruction heads
3647	    conclusion: negative
3648	    completed_at: '2026-05-18T11:45:26.662Z'
3649	    notes: Control ablation (8 non-instruction heads) also produces significant action
3650	      divergence (d=0.41, 29.3% token divergence). Per-head effect comparable to instruction
3651	      heads (0.00250 vs 0.00175). Specificity hypothesis not confirmed. Effect distributed
3652	      across L1.
3653	  behavioral_pilot_v2:
3654	    status: PREPARING
3655	    retry_count: 0
3656	    created_at: '2026-05-18T11:40:18.951Z'
3657	    updated_at: '2026-05-18T12:05:59.890Z'
3658	    hypothesis: Ablating L1 instruction-dominant heads (24/32) during VLA inference
3659	      on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral
3660	      evidence that attention head specialization has functional consequences for
3661	      task execution.
3662	    parent: behavioral_pilot_w4
3663	    conclusion: killed
3664	    notes: Director 确认放弃 behavioral rollout（mujoco 版本不匹配）。Phase 1 SR=0/3，fine-tuned
3665	      checkpoint 加载成功但 action[0] 锁定在 0.236，Blackwell GPU 需要 device_map 绕过 segfault，可能影响
3666	      inference。不再投入。
3667	  cross_layer_L8_ablation:
3668	    status: DONE
3669	    retry_count: 0
3670	    created_at: '2026-05-18T13:35:43.212Z'
3671	    updated_at: '2026-05-18T16:33:44.948Z'
3672	    hypothesis: 'L8 full-layer ablation (all 32 heads) produces significantly smaller
3673	      action divergence (d << 0.65) than L1 instruction-head ablation (24 heads, d=0.65),
3674	      demonstrating that L1''s causal impact on action output is layer-position-specific,
3675	      not merely a function of head count. Based on R² gradient prediction: L8 Δ=+0.018
3676	      vs L1 Δ=+0.059.'
3677	    parent: action_trajectory_control
3678	    spec:
3679	      command: bash -c "source /root/miniconda3/bin/activate base && cd /root/vla-ssd
3680	        && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py
3681	        2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log"
3682	      server: westd-19183
3683	      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
3684	      data_count: 2500
3685	      model_name: openvla-7b
3686	      seed: 42
3687	      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
3688	      eval_data: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
3689	      checkpoint_path: N/A
3690	      log_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log
3691	    conclusion: negative
3692	    notes: 'M006/D064: L8 full-layer ablation d=0.652 ≈ L1 d=0.65. Cross-layer gradient
3693	      not confirmed at action trajectory level. Methodological issue: L1 partial (24/32)
3694	      vs L8/L13 full (32/32) knockout not comparable; d values saturate. Not for paper.'
3695	    failure_reason: 'startup recovery: RUNNING with no cron and no server/pid info'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "f0811a0b-fe83-4462-a627-f2b9333325f2"
}
```

</details>

---


### System

_source line 118_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Reading registry.yaml",
  "usage": {
    "total_tokens": 39340,
    "tool_uses": 12,
    "duration_ms": 28422
  },
  "last_tool_name": "Read",
  "uuid": "134b86ca-27b4-454d-b218-877f836ca4a6",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 119_

<details open><summary>🔧 Tool call — Read · `toolu_018GjVC44nmSAEYEeqNrxVTF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml",
  "offset": 3772,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "cdb2bd3e-1093-477a-81fc-fb5d16ab015c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NCJhoZfmaBjSF4Qr8jCB2J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 2161,
      "cache_read_input_tokens": 37117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2161,
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

_source line 120 · 2026-05-18T17:43:37.964Z_

<details><summary>↩ Tool result · `toolu_018GjVC44nmSAEYEeqNrxVTF`</summary>

```text
3772	  permutation_test_I2:
3773	    status: DONE
3774	    retry_count: 0
3775	    created_at: '2026-05-18T15:07:21.232Z'
3776	    updated_at: '2026-05-18T15:13:25.536Z'
3777	    hypothesis: Permutation test validates that observed CV difference (instruction
3778	      1.30 vs control 2.74) and I² difference (instruction 0.87 vs control 0.78) are
3779	      not explained by random head assignment. Shuffling head labels 1000x and recomputing
3780	      metrics produces null distribution; observed values should fall in extreme tail
3781	      (p < 0.05).
3782	    parent: action_trajectory_cpu_analysis
3783	    spec:
3784	      command: python scripts/permutation_test_I2.py
3785	      server: westd-19183
3786	      data_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json
3787	      data_count: 5 tasks x 2 conditions + 7 dims x 2 conditions
3788	      model_name: n/a (statistical test)
3789	      seed: 42
3790	      checkpoint_path: n/a
3791	      log_path: /root/autodl-tmp/vla-ssd/results/permutation_test_I2.json
3792	      checkpoint_source: n/a
3793	      eval_data: action_trajectory_extended_analysis.json
3794	    metrics:
3795	      cv_exact_paired_p: 0.0156
3796	      cv_mc_unpaired_p: 0.0048
3797	      cv_7d_p: 0.0078
3798	      I2_exact_paired_p: 0.1562
3799	      I2_mc_unpaired_p: 0.1434
3800	      cv_null_mean: 0
3801	      cv_null_std: 0.6756
3802	      I2_null_mean: 0
3803	      I2_null_std: 0.2468
3804	    conclusion: success
3805	    completed_at: '2026-05-18T15:13:25.536Z'
3806	  dose_response_curve:
3807	    status: DONE
3808	    retry_count: 0
3809	    created_at: '2026-05-18T15:07:22.213Z'
3810	    updated_at: '2026-05-18T16:32:50.159Z'
3811	    hypothesis: 'If instruction routing is a learned collective function, progressively
3812	      ablating more L1 heads (sorted by instruction attention fraction) should produce
3813	      monotonically increasing action divergence (dose-response curve). 8 conditions:
3814	      top-4/8/12/16/20/24/28/32. Supports C2 claim that routing is a distributed,
3815	      coordinated mechanism.'
3816	    parent: action_trajectory_control
3817	    spec:
3818	      command: dose_response_curve.py --conditions 4,8,12,16 (cuda:0) + --conditions
3819	        20,24,28,32 (cuda:1)
3820	      server: westd-19183
3821	      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
3822	      data_count: 5 tasks x 10 demos x 50 timesteps x 8 conditions = 20000 passes
3823	      model_name: openvla-7b
3824	      seed: 42
3825	      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
3826	      eval_data: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
3827	    failure_reason: 'startup recovery: RUNNING with no cron and no server/pid info'
3828	    conclusion: success
3829	    completed_at: '2026-05-18T16:26:06.324Z'
3830	    notes: 单调递增 dose-response 曲线，d=0.482(top4)→0.639(top32)，diminishing returns at
3831	      ~12-16 heads
3832	  counterfactual_instruction:
3833	    status: DONE
3834	    retry_count: 0
3835	    created_at: '2026-05-18T16:52:52.867Z'
3836	    updated_at: '2026-05-18T17:31:39.989Z'
3837	    hypothesis: 'L1 instruction-dominant heads perform instruction-specific routing:
3838	      changing the instruction (wrong/empty/shuffled/paraphrased) should produce systematically
3839	      different action outputs compared to correct instruction, with wrong and empty
3840	      causing larger divergence than shuffled or paraphrased.'
3841	    parent: action_trajectory_control
3842	    spec:
3843	      command: MUJOCO_GL=egl python -u scripts/counterfactual_instruction.py
3844	      server: westd-19183
3845	      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
3846	      data_count: 6000
3847	      model_name: openvla-7b
3848	      seed: 42
3849	      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
3850	      eval_data: /root/autodl-tmp/vla-ssd/data/libero/libero_goal
3851	      checkpoint_path: N/A
3852	      log_path: /root/autodl-tmp/vla-ssd/results/counterfactual_instruction.log
3853	    checkpoint_path: N/A (eval-only experiment)
3854	    log_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_counterfactual_instruction_20260518T165804.log
3855	    conclusion: success
3856	    completed_at: '2026-05-18T17:31:15.868Z'
3857	    notes: '4 counterfactual conditions vs correct baseline. Cohen''s d: empty=0.968,
3858	      wrong=0.844, paraphrased=0.697, shuffled=0.625. All d>0.5. Graduated response
3859	      confirms instruction content sensitivity. Surprise: paraphrased > shuffled (model
3860	      depends on surface form, not just semantics). Supports C2 claim.'
3861	  action_metrics_extended:
3862	    status: DONE
3863	    retry_count: 0
3864	    created_at: '2026-05-18T16:52:53.825Z'
3865	    updated_at: '2026-05-18T17:16:37.223Z'
3866	    hypothesis: 'Extended analysis of existing action trajectory data: (1) per-dimension
3867	      MAE reveals which action dimensions are most affected by L1 instruction-head
3868	      ablation, (2) action direction cosine similarity shows whether ablation changes
3869	      action direction vs magnitude, providing mechanistic detail beyond aggregate
3870	      Cohen''s d.'
3871	    parent: action_trajectory_control
3872	    spec:
3873	      command: python3 (CPU-only, from existing JSONs)
3874	      server: westd-19183
3875	      data_path: /root/autodl-tmp/vla-ssd/results/
3876	      data_count: 5000
3877	      model_name: openvla-7b
3878	      seed: 42
3879	      checkpoint_source: N/A (analysis only)
3880	      eval_data: action_trajectory_analysis.json + action_trajectory_control.json
3881	      checkpoint_path: N/A
3882	      log_path: /root/autodl-tmp/vla-ssd/results/action_metrics_extended.json
3883	    conclusion: success
3884	    completed_at: '2026-05-18T17:16:32.376Z'
3885	    notes: 'Per-dim MAE extracted from existing JSONs. Instruction 24h causes 1.9-5.1x
3886	      larger shifts than control 8h. Translation dims most affected (dx=5.1x, dy=4.3x,
3887	      dz=3.1x), rotation moderate (roll=2.6x, pitch=2.2x, yaw=1.9x), gripper=2.1x.
3888	      Cosine similarity NOT computable: source JSONs only have aggregated stats, no
3889	      raw per-sample action vectors.'
3890	  attention_decomposition:
3891	    status: DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "c36ed1e7-2fb8-460e-bf08-fe649e51d8ea"
}
```

</details>

---


### System

_source line 121_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Running grep -A 30 \"^  dose_response_curve:\" /home/ubuntu…",
  "usage": {
    "total_tokens": 41840,
    "tool_uses": 13,
    "duration_ms": 31288
  },
  "last_tool_name": "Bash",
  "uuid": "6dbf9ade-a4a6-4381-8aa9-3ceabc687c47",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 122_

<details open><summary>🔧 Tool call — Bash · `toolu_01X9g6N23KbMPUzCCJcgCHKK`</summary>

```json
{
  "command": "grep -A 30 \"^  dose_response_curve:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml | grep -E \"metrics:|notes:|conclusion:\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "2ddf7f98-3b60-4a65-980a-47112940323c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lr58QaYzQXqWNYr9vnqAWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 39278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2496,
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

_source line 123 · 2026-05-18T17:43:40.883Z_

<details><summary>↩ Tool result · `toolu_01X9g6N23KbMPUzCCJcgCHKK`</summary>

```text
    conclusion: success
    notes: 单调递增 dose-response 曲线，d=0.482(top4)→0.639(top32)，diminishing returns at
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "11bf4e29-9ca5-4d1d-abb8-d4c0d2887846"
}
```

</details>

---


### System

_source line 124_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "description": "Running grep -A 30 \"^  counterfactual_instruction:\" /home…",
  "usage": {
    "total_tokens": 42046,
    "tool_uses": 14,
    "duration_ms": 32888
  },
  "last_tool_name": "Bash",
  "uuid": "757a6497-d71e-4285-9479-a660375cc5d6",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 125_

<details open><summary>🔧 Tool call — Bash · `toolu_01K8NdHXFpGR3RkhndnAVkJt`</summary>

```json
{
  "command": "grep -A 30 \"^  counterfactual_instruction:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml | grep -E \"metrics:|notes:|conclusion:\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "0a6649ea-0d08-427f-90ad-65a99a24bfb8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GUBhjSba7FyUk2458Nd6ok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 41774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 204,
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

_source line 126 · 2026-05-18T17:43:42.474Z_

<details><summary>↩ Tool result · `toolu_01K8NdHXFpGR3RkhndnAVkJt`</summary>

```text
    conclusion: success
    notes: '4 counterfactual conditions vs correct baseline. Cohen''s d: empty=0.968,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "32bb8609-0722-46b3-ad13-3eab2e81b029"
}
```

</details>

---


### System

_source line 127_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Reading artifacts/_project/paper/related_work.tex",
  "usage": {
    "total_tokens": 44048,
    "tool_uses": 20,
    "duration_ms": 40499
  },
  "last_tool_name": "Read",
  "uuid": "9bdd7639-e570-4a24-a9c5-6d88a4523e1b",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 128_

<details open><summary>🔧 Tool call — Read · `toolu_01BRogmFX6sZtPnoiWwFkL4r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "c98f1641-b323-406b-8343-86e52c03e1fb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JmqgVYcg5DF4uBbHXxumfX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 299,
      "cache_read_input_tokens": 43677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 299,
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

_source line 129 · 2026-05-18T17:43:47.509Z_

<details><summary>↩ Tool result · `toolu_01BRogmFX6sZtPnoiWwFkL4r`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Vision-Language-Action Models}
5	
6	VLAs repurpose pretrained vision-language models as robotic policies by fine-tuning them on demonstration data.
7	RT-2~\cite{brohan2023_rt2} established the paradigm by showing that a large vision-language model can be directly fine-tuned to output robotic actions tokenized as text, transferring web-scale knowledge to manipulation tasks.
8	OpenVLA~\cite{kim2024_openvla} made this architecture open-source, building on the Prismatic VLM framework~\cite{karamcheti2024} with a frozen SigLIP encoder~\cite{zhai2023_siglip} and a Llama-2 backbone.
9	$\pi_0$~\cite{black2024_pi0} departed from autoregressive action decoding in favor of flow matching, while retaining the frozen-encoder-plus-LLM structure.
10	A common architectural choice across these models is to freeze the vision encoder and fine-tune only the LLM and projector, embedding an implicit assumption: fine-tuning injects action-relevant knowledge into the LLM.
11	Our work tests this assumption directly at the representational level and finds that it does not hold---action-relevant geometric structure originates in the vision encoder and is routed, not created, by fine-tuning.
12	
13	\subsection{Understanding VLA Representations}
14	
15	A growing body of work investigates how VLAs process information internally.
16	Haon et al.~\cite{haon2025} performed the first mechanistic interpretability study of VLAs, identifying causally relevant attention heads and demonstrating activation steering for behavior modification.
17	Grant et al.~\cite{grant2026} showed across six VLA architectures that the visual pathway dominates action generation, with language stream ablations causing minimal behavioral degradation---a behavioral-level finding consistent with our representational-level observation of vision encoder dominance.
18	Swann et al.~\cite{swann2026} applied sparse autoencoders to OpenVLA, discovering interpretable monosemantic features at the individual-neuron level.
19	Rizzardo et al.~\cite{rizzardo2026} characterized VLA representations through the lens of observability and controllability, measuring how well internal features predict and steer downstream behavior.
20	Molinari et al.~\cite{molinari2025} probed OpenVLA for world-model properties, finding that the model encodes spatial and physical state information in its intermediate representations.
21	
22	These studies illuminate different facets of VLA internals but leave a gap that our work addresses.
23	Grant et al.\ operate at the behavioral level (input ablations and output measurements) without examining representation geometry.
24	Swann et al.\ and Molinari et al.\ analyze individual features or semantic properties without quantifying how much action-relevant structure each architectural component contributes.
25	Haon et al.\ identify causal mechanisms but do not decompose where the underlying representations originate.
26	No prior work compares trained and untrained models to isolate training's contribution, and none reports the geometric-functional dissociation we observe between vision-language and vision-only encoders.
27	
28	\subsection{Representational Analysis Methods}
29	
30	Our methodology draws on a toolkit developed across neuroscience and deep learning.
31	Representational Similarity Analysis (RSA)~\cite{kriegeskorte2008}, originally designed to compare neural recordings with computational models, quantifies geometric alignment between representation spaces via pairwise dissimilarity correlations.
32	Centered Kernel Alignment (CKA)~\cite{kornblith2019} provides a complementary global measure invariant to orthogonal transformations, enabling comparison of representations across architectures and dimensionalities.
33	Linear probing~\cite{alain2017} assesses the functional content of representations by training lightweight decoders on frozen activations; Belinkov~\cite{belinkov2022} surveys its extensive use in NLP for analyzing linguistic structure at each layer of pretrained models.
34	
35	These tools have been widely applied to vision models and language models in isolation, but their joint application to VLA pipelines---where vision, language, and action spaces intersect---is largely unexplored.
36	We combine RSA, CKA, and probing in a factorial design to provide the first systematic representational decomposition of a VLA, measuring both geometric alignment and functional decodability across all architectural components and training conditions.
37	The multi-metric approach proves essential: we show that linear CKA and RSA can produce divergent rankings of the same representations (Section~\ref{sec:vision_dominance}), underscoring the need for methodological plurality in representation analysis.
38	
39	\subsection{Vision-Language Pretraining}
40	
41	The vision encoders in modern VLAs inherit their representations from large-scale pretraining.
42	CLIP~\cite{radford2021_clip} and SigLIP~\cite{zhai2023_siglip} learn visual features aligned to language through contrastive objectives on image-text pairs, while DINOv2~\cite{oquab2024_dinov2} learns from self-supervised vision objectives without language supervision.
43	Prior work has shown that these pretraining paradigms produce qualitatively different representation geometries, but their downstream consequences for action-relevant structure in VLAs have not been characterized.
44	Our finding of a geometric-functional dissociation---VL-pretrained encoders achieve substantially higher geometric alignment with the action space than DINOv2 yet comparable functional decodability---provides the first direct evidence that language-grounded pretraining shapes the geometry, but not the information content, of action-relevant visual representations.
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "e10d14f0-4a77-40cc-9891-1bf982c106ab"
}
```

</details>

---


### System

_source line 130_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running cat /home/ubuntu/.agent-ml-research-idea_gen_0509…",
  "usage": {
    "total_tokens": 45704,
    "tool_uses": 21,
    "duration_ms": 43677
  },
  "last_tool_name": "Bash",
  "uuid": "73633099-c900-400d-8750-4606d405d43f",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 131_

<details open><summary>🔧 Tool call — Bash · `toolu_014EDSadax4VRdMcjioAS3Sm`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "e1743166-d10d-4663-948d-078ade08f254",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019mtzJdxGWMNurEfLhNuxpd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 43976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1656,
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

_source line 132 · 2026-05-18T17:43:50.731Z_

<details><summary>↩ Tool result · `toolu_014EDSadax4VRdMcjioAS3Sm`</summary>

```text
\section{Introduction}
\label{sec:introduction}

Vision-language-action models (VLAs) achieve impressive robotic manipulation performance by fine-tuning large language models on robot demonstration data~\cite{brohan2023_rt2,kim2024_openvla}.
The dominant architecture grafts a frozen vision encoder onto a pretrained LLM backbone, then fine-tunes the system end-to-end to map visual observations and language instructions to continuous actions~\cite{karamcheti2024}.
An implicit assumption underlies this paradigm: fine-tuning injects action-relevant representational knowledge into the LLM.
But where do action representations actually come from?
Do they originate in the vision encoder's pretrained features, emerge through LLM processing, or arise from task-specific fine-tuning?

Recent work reveals cracks in this assumption.
Grant et al.~\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.
Independently, Hou et al.~\cite{hou2026} and Fei et al.~\cite{fei2025} demonstrated that VLAs largely ignore language instructions during policy execution.
These findings challenge the prevailing narrative but remain at the behavioral level---they reveal \emph{what} drives VLA outputs without explaining \emph{where} action-relevant structure resides in the representation space.
No prior work has performed a representational decomposition that measures each component's independent contribution to action-relevant structure.
Without this, we cannot determine whether fine-tuning truly injects action knowledge or merely learns to route pre-existing structure.

We present the first systematic representational and functional analysis of a VLA.
Taking OpenVLA-7B~\cite{kim2024_openvla} as a case study, we decompose its processing pipeline into constituent components: the frozen SigLIP vision encoder~\cite{zhai2023_siglip} with MLP projector, every layer of the Llama-2 7B backbone, and the readout token position.
We apply Representational Similarity Analysis (RSA)~\cite{kriegeskorte2008} to measure geometric alignment with the action space and train functional probes to measure action decodability.
A $2 \times 2$ factorial design crossing training status (trained vs.\ untrained LLM) with instruction presence (with vs.\ without) isolates each factor's contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "74f1592e-9290-4764-8d54-bc1bc3e7ccba"
}
```

</details>

---


### System

_source line 133_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 45705,
    "tool_uses": 22,
    "duration_ms": 44298
  },
  "last_tool_name": "Bash",
  "uuid": "2baed80d-b76d-4887-814c-e082623631ba",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool call

_source line 134_

<details open><summary>🔧 Tool call — Bash · `toolu_01XYY5nVSsM5Emdc3cV4x2Vn`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/ && echo \"---\" && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/*.tex | sort -rn"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "bd466c6b-c4dd-468e-855e-4aa17f28e3e1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019mtzJdxGWMNurEfLhNuxpd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 43976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1656,
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

_source line 135 · 2026-05-18T17:43:51.379Z_

<details><summary>↩ Tool result · `toolu_01XYY5nVSsM5Emdc3cV4x2Vn`</summary>

```text
total 72K
-rw-r--r-- 1 ubuntu ubuntu 7.0K May 16 02:52 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  15K May 16 02:22 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu 4.8K May 16 02:29 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu 5.2K May 16 02:56 introduction_fccb56.tex
-rw-r--r-- 1 ubuntu ubuntu 7.3K May 16 02:29 method.tex
-rw-r--r-- 1 ubuntu ubuntu 7.5K May 16 02:43 method_a6c062.tex
-rw-r--r-- 1 ubuntu ubuntu 5.9K May 16 04:47 references.bib
-rw-r--r-- 1 ubuntu ubuntu 5.6K May 16 02:37 related_work.tex
---
  556 total
  197 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex
  100 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method_a6c062.tex
   92 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex
   48 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/discussion.tex
   44 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex
   39 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex
   36 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction_fccb56.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "ea4eca24-5236-487d-9877-6757f0fa66f7"
}
```

</details>

---


### System

_source line 136_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ae39a9b62fe5c8da8",
  "tool_use_id": "toolu_01Ef5xPBxeh51RFxv5FGbpDr",
  "status": "completed",
  "output_file": "",
  "summary": "Find paper sections for mapping",
  "usage": {
    "total_tokens": 47167,
    "tool_uses": 22,
    "duration_ms": 65966
  },
  "uuid": "0497d7ad-2714-4a0e-a039-7f6cd2b20364",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool result

_source line 137 · 2026-05-18T17:44:12.964Z_

<details><summary>↩ Tool result · `toolu_01Ef5xPBxeh51RFxv5FGbpDr`</summary>

```text
Perfect! Now I have a complete picture. Let me create a comprehensive summary with all the information you requested.

## Final Report

Based on my thorough search of the `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/` directory, here are my findings:

### 1. Relevant .tex Files

The main paper files are located in `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/`:

- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex` (Section 4 - Experiments)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/discussion.tex`

Additionally, there are dream reports with complete compiled papers at:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/paper.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/paper.tex`

### 2. Section Mapping (Note: No §4.1-4.3 or §A.8 Notation Found)

The paper uses standard section notation rather than §4.1-4.3 notation. The Experiments section (Section 4) contains three main subsections:

**Section 4 (Experiments) Structure:**
- **§4.0 (Experimental Setup)** - Lines 4-30 in experiments.tex
- **§4.1 (Vision Encoder Dominance)** - Lines 32-90 in experiments.tex
- **§4.2 (LLM Redistributes, Does Not Enhance, Action Structure)** - Lines 93-142 in experiments.tex
- **§4.3 (Training Routes, Does Not Create, Action Geometry)** - Lines 145-197 in experiments.tex

**Appendix Structure:**
The appendix sections found in the compiled paper (dream reports) include:
- **Appendix A.1: Per-Layer RSA Degradation Curve** - Detailed per-layer RSA values
- **Appendix A.2: LIBERO-Spatial Detailed Results** - Cross-benchmark validation

### 3. §4.1 and §4.2 Section Titles and Three-Condition Data

**§4.1: Vision Encoder Dominance**
- Tests whether vision-language pretrained encoders provide the dominant source of action-relevant geometric structure in VLA representations
- **Three-condition comparison:**
  - SigLIP+Projector: RSA ρ = 0.615 (95% CI [0.526, 0.695])
  - CLIP ViT-L/14: RSA ρ = 0.557 (95% CI [0.442, 0.660])
  - DINOv2 ViT-L/14: RSA ρ = 0.388 (vision-only baseline)

**§4.2: LLM Redistributes, Does Not Enhance, Action Structure**
- Tests how the LLM transforms action-relevant structure inherited from the vision encoder
- **Three-condition data (Functional probe R² values):**
  - SigLIP+Projector: R² = 0.706 (baseline)
  - VLA Trained readout: R² = 0.731 (concentrated representation, p = 0.001)
  - VLA Trained image_mean: R² = 0.683 (distributed degradation, p = 0.001)
  - DINOv2 cls_token: R² = 0.712 (statistically indistinguishable from projector, p = 0.22)

### 4. §4.3: Key Paragraphs and Claims

**§4.3 Location:** Lines 145-197 in experiments.tex

**Key Claims:**

**Geometric Invariance to Training:**
- Training does not alter the LLM's geometric alignment with action space
- Training effect: Δ = +0.021 (95% CI [-0.031, +0.064], p = 0.20, n.s.) for image_mean RSA
- Last_preaction RSA training effect: Δ = +0.008 (95% CI [-0.040, +0.056], p = 0.37, n.s.)
- Vision encoder weights are identical between conditions (cos_sim = 1.0), being the sole source of action-relevant geometry

**Geometric Invariance to Instruction:**
- Instruction effect: Δ = 0.004 (n.s.) across the 2×2 matrix
- Control experiment with four instruction conditions shows all values within ±0.017 of the mean:
  - Normal task instructions: ρ = 0.489
  - Random instructions from other tasks: ρ = 0.484
  - Word-shuffled instructions: ρ = 0.483
  - Empty strings: ρ = 0.472

**Functional Concentration Requires Training:**
- Readout probe R² shows large training effect: Δ = +0.045 (CI [+0.032, +0.058], p < 0.0001)
- Trained readout: R² = 0.731 (exceeds projector baseline of 0.706)
- Untrained readout: R² = 0.686 (falls below projector baseline)
- Training teaches concentration without creating new geometry (routing interpretation)

### 5. Appendix Content (§A.8 Equivalent)

**Appendix A.1: Per-Layer RSA Degradation Curve**
- No explicit "permutation test" found, but detailed per-layer analysis shows:
  - **Three phases of degradation:**
    1. Early rapid decline (L0-L8): RSA drops from 0.58 to 0.47
    2. Mid-layer recovery (L12-L16): RSA rebounds to ~0.52-0.53 (attributed to cross-modal integration)
    3. Late-stage plateau (L20-L32): RSA oscillates in the 0.47-0.49 range
  
  - Overall Spearman correlation between layer index and RSA: ρ = -0.62 (net downward trend)
  - 8 monotonicity violations across 33 measurement points
  - Final layer RSA (0.47) remains well below projector (0.615) - a drop of 0.145

**Appendix A.2: LIBERO-Spatial Cross-Benchmark Validation**
- Per-layer degradation trend on spatial tasks: Spearman ρ = -0.55
- Mid-layer bump shifted to layers 10-14 (slightly earlier than LIBERO-Goal)
- Consistent conclusions: SigLIP ≫ VLA ≫ DINOv2

### 6. Convergent Evidence in Discussion Section

Searching the discussion.tex file shows **no explicit numbered "convergent evidence" items**. However, the discussion synthesizes evidence across three main findings:

**Four Paragraphs of Evidence:**
1. **Synthesis** (lines 4-9): Vision encoder as source; LLM as router; training teaches routing policy
2. **VL Pretraining as General Source** (lines 11-15): Evidence from CLIP baseline that action-relevant geometry is general product of VL pretraining
3. **Geometric-Functional Dissociation** (lines 17-21): DINOv2 decodability matches SigLIP despite lower RSA
4. **Metric Sensitivity** (lines 23-29): CKA verification shows LLM applies rotation-like transformations

The discussion connects representational findings to behavioral evidence from Grant et al. (2026) showing visual pathway dominance at behavioral level, providing cross-level validation.

---

**Note:** The section notation you mentioned (§4.3, §A.8) does not appear in the actual paper files. The paper uses standard section numbering. The content you're looking for is organized as subsections 4.1-4.3 within the Experiments section, and appendix sections are labeled A.1, A.2, etc. in the compiled versions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "88a811f1-b35d-4fcb-9379-14f804fd202f",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/, find all .tex files related to the paper. Then search for the sections §4.3 (or subsections about \"dose-response\", \"counterfactual\", \"action trajectory\", \"ablation\", \"convergent evidence\", \"causal\") and §A.8 (appendix about \"permutation\"). Also find §4.1 and §4.2 section headers.\n\nI need to understand what content is in each section so I can map experiments to specific claims. Report:\n1. The file paths of the relevant tex files\n2. For §4.3: the key paragraphs/claims about dose-response, counterfactual instruction, action trajectory, ablation, random subset\n3. For §A.8: the permutation test content\n4. For §4.1 and §4.2: the section titles and what three-condition data they present\n5. Any mention of \"convergent evidence\" numbered items in the Discussion section\n\nSearch breadth: very thorough",
    "agentId": "ae39a9b62fe5c8da8",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have a complete picture. Let me create a comprehensive summary with all the information you requested.\n\n## Final Report\n\nBased on my thorough search of the `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/` directory, here are my findings:\n\n### 1. Relevant .tex Files\n\nThe main paper files are located in `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/`:\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex` (Section 4 - Experiments)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/discussion.tex`\n\nAdditionally, there are dream reports with complete compiled papers at:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/paper.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/paper.tex`\n\n### 2. Section Mapping (Note: No §4.1-4.3 or §A.8 Notation Found)\n\nThe paper uses standard section notation rather than §4.1-4.3 notation. The Experiments section (Section 4) contains three main subsections:\n\n**Section 4 (Experiments) Structure:**\n- **§4.0 (Experimental Setup)** - Lines 4-30 in experiments.tex\n- **§4.1 (Vision Encoder Dominance)** - Lines 32-90 in experiments.tex\n- **§4.2 (LLM Redistributes, Does Not Enhance, Action Structure)** - Lines 93-142 in experiments.tex\n- **§4.3 (Training Routes, Does Not Create, Action Geometry)** - Lines 145-197 in experiments.tex\n\n**Appendix Structure:**\nThe appendix sections found in the compiled paper (dream reports) include:\n- **Appendix A.1: Per-Layer RSA Degradation Curve** - Detailed per-layer RSA values\n- **Appendix A.2: LIBERO-Spatial Detailed Results** - Cross-benchmark validation\n\n### 3. §4.1 and §4.2 Section Titles and Three-Condition Data\n\n**§4.1: Vision Encoder Dominance**\n- Tests whether vision-language pretrained encoders provide the dominant source of action-relevant geometric structure in VLA representations\n- **Three-condition comparison:**\n  - SigLIP+Projector: RSA ρ = 0.615 (95% CI [0.526, 0.695])\n  - CLIP ViT-L/14: RSA ρ = 0.557 (95% CI [0.442, 0.660])\n  - DINOv2 ViT-L/14: RSA ρ = 0.388 (vision-only baseline)\n\n**§4.2: LLM Redistributes, Does Not Enhance, Action Structure**\n- Tests how the LLM transforms action-relevant structure inherited from the vision encoder\n- **Three-condition data (Functional probe R² values):**\n  - SigLIP+Projector: R² = 0.706 (baseline)\n  - VLA Trained readout: R² = 0.731 (concentrated representation, p = 0.001)\n  - VLA Trained image_mean: R² = 0.683 (distributed degradation, p = 0.001)\n  - DINOv2 cls_token: R² = 0.712 (statistically indistinguishable from projector, p = 0.22)\n\n### 4. §4.3: Key Paragraphs and Claims\n\n**§4.3 Location:** Lines 145-197 in experiments.tex\n\n**Key Claims:**\n\n**Geometric Invariance to Training:**\n- Training does not alter the LLM's geometric alignment with action space\n- Training effect: Δ = +0.021 (95% CI [-0.031, +0.064], p = 0.20, n.s.) for image_mean RSA\n- Last_preaction RSA training effect: Δ = +0.008 (95% CI [-0.040, +0.056], p = 0.37, n.s.)\n- Vision encoder weights are identical between conditions (cos_sim = 1.0), being the sole source of action-relevant geometry\n\n**Geometric Invariance to Instruction:**\n- Instruction effect: Δ = 0.004 (n.s.) across the 2×2 matrix\n- Control experiment with four instruction conditions shows all values within ±0.017 of the mean:\n  - Normal task instructions: ρ = 0.489\n  - Random instructions from other tasks: ρ = 0.484\n  - Word-shuffled instructions: ρ = 0.483\n  - Empty strings: ρ = 0.472\n\n**Functional Concentration Requires Training:**\n- Readout probe R² shows large training effect: Δ = +0.045 (CI [+0.032, +0.058], p < 0.0001)\n- Trained readout: R² = 0.731 (exceeds projector baseline of 0.706)\n- Untrained readout: R² = 0.686 (falls below projector baseline)\n- Training teaches concentration without creating new geometry (routing interpretation)\n\n### 5. Appendix Content (§A.8 Equivalent)\n\n**Appendix A.1: Per-Layer RSA Degradation Curve**\n- No explicit \"permutation test\" found, but detailed per-layer analysis shows:\n  - **Three phases of degradation:**\n    1. Early rapid decline (L0-L8): RSA drops from 0.58 to 0.47\n    2. Mid-layer recovery (L12-L16): RSA rebounds to ~0.52-0.53 (attributed to cross-modal integration)\n    3. Late-stage plateau (L20-L32): RSA oscillates in the 0.47-0.49 range\n  \n  - Overall Spearman correlation between layer index and RSA: ρ = -0.62 (net downward trend)\n  - 8 monotonicity violations across 33 measurement points\n  - Final layer RSA (0.47) remains well below projector (0.615) - a drop of 0.145\n\n**Appendix A.2: LIBERO-Spatial Cross-Benchmark Validation**\n- Per-layer degradation trend on spatial tasks: Spearman ρ = -0.55\n- Mid-layer bump shifted to layers 10-14 (slightly earlier than LIBERO-Goal)\n- Consistent conclusions: SigLIP ≫ VLA ≫ DINOv2\n\n### 6. Convergent Evidence in Discussion Section\n\nSearching the discussion.tex file shows **no explicit numbered \"convergent evidence\" items**. However, the discussion synthesizes evidence across three main findings:\n\n**Four Paragraphs of Evidence:**\n1. **Synthesis** (lines 4-9): Vision encoder as source; LLM as router; training teaches routing policy\n2. **VL Pretraining as General Source** (lines 11-15): Evidence from CLIP baseline that action-relevant geometry is general product of VL pretraining\n3. **Geometric-Functional Dissociation** (lines 17-21): DINOv2 decodability matches SigLIP despite lower RSA\n4. **Metric Sensitivity** (lines 23-29): CKA verification shows LLM applies rotation-like transformations\n\nThe discussion connects representational findings to behavioral evidence from Grant et al. (2026) showing visual pathway dominance at behavioral level, providing cross-level validation.\n\n---\n\n**Note:** The section notation you mentioned (§4.3, §A.8) does not appear in the actual paper files. The paper uses standard section numbering. The content you're looking for is organized as subsections 4.1-4.3 within the Experiments section, and appendix sections are labeled A.1, A.2, etc. in the compiled versions."
      }
    ],
    "totalDurationMs": 65969,
    "totalTokens": 49264,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 45632,
      "output_tokens": 2166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1460
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2166,
          "cache_read_input_tokens": 45632,
          "cache_creation_input_tokens": 1460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1460,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 5,
      "bashCount": 12,
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


### System

_source line 138_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a9b100c2432c85c7e",
  "tool_use_id": "toolu_01KufG4mJYoZpp3mXNmVDyjx",
  "status": "completed",
  "output_file": "",
  "summary": "Get experiment details for 8 experiments",
  "usage": {
    "total_tokens": 42213,
    "tool_uses": 14,
    "duration_ms": 68259
  },
  "uuid": "a319dcb1-b01e-4f05-ae53-89513391e71a",
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d"
}
```

---


### Tool result

_source line 139 · 2026-05-18T17:44:17.797Z_

<details><summary>↩ Tool result · `toolu_01KufG4mJYoZpp3mXNmVDyjx`</summary>

```text
Perfect! Now I have all the information I need. Let me compile the complete report with all 8 experiments:

## Experiment Registry Report: 8 Experiments

Here are the detailed findings for all 8 experiments from `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml`:

---

### 1. **ablation_50demos_main**

**Exp_ID:** ablation_50demos_main

**Status:** DONE (success)

**Title/Description:** L1 instruction-dominant head ablation with adequate probe training data (50 demos per task)

**Hypothesis:** 50-demo full-data ablation: L1 instruction-dominant heads capacity trade-off (R² increase under ablation) persists with adequate probe training data, eliminating underfitting confound from 5-demo version.

**What it tests:** Tests whether the capacity trade-off observed in instruction-dominant head ablation is robust when probe training has sufficient data (50 demos/task vs 5 demos), confirming the effect is not due to underfitting.

**Key metrics:**
- Baseline L1 R²: 0.5567
- All 24 heads ablated L1 R²: 0.6153
- All 24 vs baseline delta: 0.0585 (p=0)
- All 24 vs control-8 delta: 0.0421 (p=0)
- Confidence intervals provided for all comparisons

**Completed:** 2026-05-17T21:49:51.638Z

---

### 2. **action_trajectory_analysis**

**Exp_ID:** action_trajectory_analysis

**Status:** DONE (success)

**Title/Description:** L1 instruction-dominant head ablation effect on OpenVLA action predictions

**Hypothesis:** L1 instruction-dominant head ablation significantly changes OpenVLA action predictions (measured by action token divergence and per-dimension MSE), demonstrating that instruction routing heads directly influence model output, not just intermediate representations.

**What it tests:** Tests whether ablating L1 instruction-dominant heads produces measurable changes in the model's actual action token outputs, proving these heads have causal downstream effects beyond representation-level metrics.

**Key metrics:**
- Paired action MSE: 0.0416 ± 0.0639 (Cohen's d: 0.651, p < 0.001)
- Token divergence rate: 72.3%
- KL divergence: 5.079 ± 4.961
- Per-dimension action shifts across 7 action dimensions (dx, dy, dz, rx, ry, rz, gripper)
- Wilcoxon p-value: 0 (highly significant)
- Per-task Cohen's d range: 0.433–0.729 (all 5 tasks significant)
- n_samples: 2500

**Completed:** 2026-05-18T11:02:27.281Z

---

### 3. **action_trajectory_control**

**Exp_ID:** action_trajectory_control

**Status:** DONE (negative)

**Title/Description:** Control ablation (8 non-instruction heads) vs instruction-dominant heads action divergence comparison

**Hypothesis:** Ablating 8 non-instruction heads (control) produces significantly smaller action divergence (especially gripper dimension) than ablating 24 instruction-dominant heads, proving the action output effect is instruction-specific rather than generic perturbation.

**What it tests:** Tests whether the action divergence effect is specific to instruction-dominant heads or is a generic perturbation effect. Uses 8 non-instruction control heads to establish baseline.

**Key metrics:**
- Control 8-head MSE: 0.0201 ± 0.0489 (Cohen's d: 0.41, p ~ 10^-87)
- Control token divergence: 29.3%
- Control KL divergence: 1.69 ± 3.7
- Comparison ratios: MSE ratio 2.07x, token divergence ratio 2.47x, KL ratio 3x (instruction vs control)
- Per-task Cohen's d: 0.24–0.48
- Per-head effect: control heads ~1.9x stronger per-head than expected (0.051 vs 0.027, p=0.0018)
- Temporal coherence: instruction heads produce more consistent (CV 1.30 vs 2.74) and more task-dependent (I²=0.87 vs 0.78) perturbation

**Conclusion:** Negative – specificity hypothesis not fully confirmed. Control heads also produce significant effects. However, instruction heads show qualitatively different (more coordinated) perturbation patterns.

**Completed:** 2026-05-18T11:45:26.662Z

---

### 4. **random_subset_ablation**

**Exp_ID:** random_subset_ablation

**Status:** DONE (success)

**Title/Description:** Random 24-head subsets produce larger action R² increases than instruction-dominant 24 heads

**Hypothesis:** Random subsets of 24 heads yield higher action R² increase than instruction-dominant 24 heads, indicating dominant heads serve dual routing-encoding function rather than pure capacity trade-off.

**What it tests:** Tests whether the instruction-dominant 24 heads are special by comparing their R² impact to 10 random 24-head subsets. If random subsets perform better, it challenges the "dominant heads are special" narrative.

**Key metrics:**
- Baseline R²: 0.517
- Dominant-24 delta R²: 0.042
- Random-24 mean delta R²: 0.077 ± 0.013 (std)
- Z-score: -2.73
- P-value: 0.003
- n_random_seeds: 10
- Effect size: random 24-head subsets ablate for ~83% larger R² increase than instruction-dominant heads

**Interpretation:** Dominant-24 heads NOT special – any random 24/32 heads ablation produces similar or larger R² increase, supporting dual routing-encoding function explanation rather than capacity trade-off.

**Completed:** 2026-05-18T08:27:15.118Z

---

### 5. **permutation_test_I2**

**Exp_ID:** permutation_test_I2

**Status:** DONE (success)

**Title/Description:** Permutation test for CV and I² differences between instruction and control heads

**Hypothesis:** Permutation test validates that observed CV difference (instruction 1.30 vs control 2.74) and I² difference (instruction 0.87 vs control 0.78) are not explained by random head assignment. Shuffling head labels 1000x produces null distribution; observed values should fall in extreme tail (p < 0.05).

**What it tests:** Tests whether the differences in temporal coherence (CV) and task-dependency (I²) metrics between instruction and control heads are statistically significant or due to random chance.

**Key metrics:**
- CV exact paired p-value: 0.0156
- CV MC unpaired p-value: 0.0048
- CV 7D p-value: 0.0078
- I² exact paired p-value: 0.1562
- I² MC unpaired p-value: 0.1434
- CV null mean: 0, std: 0.6756
- I² null mean: 0, std: 0.2468

**Interpretation:** CV differences are significant (p < 0.05), but I² differences are marginal (p ~ 0.14). Instruction heads produce more consistent perturbations across dimensions, but task-dependency is not significantly different from random.

**Completed:** 2026-05-18T15:13:25.536Z

---

### 6. **dose_response_curve**

**Exp_ID:** dose_response_curve

**Status:** DONE (success)

**Title/Description:** Dose-response curve of progressive L1 head ablation on action divergence

**Hypothesis:** If instruction routing is a learned collective function, progressively ablating more L1 heads (sorted by instruction attention fraction) should produce monotonically increasing action divergence (dose-response curve). 8 conditions: top-4/8/12/16/20/24/28/32. Supports C2 claim that routing is a distributed, coordinated mechanism.

**What it tests:** Tests whether the effect of head ablation is dose-dependent and monotonic, supporting the hypothesis that instruction routing is a collective, distributed mechanism rather than individual head contributions.

**Key metrics:**
- Cohen's d progression: d=0.482 (top-4) → 0.639 (top-32)
- Pattern: Monotonically increasing dose-response curve
- Diminishing returns observed at ~12–16 heads
- 8 conditions tested: 4, 8, 12, 16, 20, 24, 28, 32 heads
- Data: 5 tasks x 10 demos x 50 timesteps x 8 conditions = 20,000 forward passes

**Interpretation:** Monotonic dose-response with diminishing returns supports distributed collective function hypothesis. Effect plateaus after ~16 heads, suggesting redundancy or saturation.

**Completed:** 2026-05-18T16:26:06.324Z

---

### 7. **counterfactual_instruction**

**Exp_ID:** counterfactual_instruction

**Status:** DONE (success)

**Title/Description:** L1 heads respond differently to incorrect/empty/paraphrased/shuffled instructions

**Hypothesis:** L1 instruction-dominant heads perform instruction-specific routing: changing the instruction (wrong/empty/shuffled/paraphrased) should produce systematically different action outputs compared to correct instruction, with wrong and empty causing larger divergence than shuffled or paraphrased.

**What it tests:** Tests whether L1 instruction-dominant heads are truly sensitive to instruction content and semantics. Compares action divergence across 4 counterfactual instruction conditions.

**Key metrics:**
- Cohen's d by condition:
  - Empty instruction: d = 0.968 (largest)
  - Wrong instruction: d = 0.844
  - Paraphrased instruction: d = 0.697
  - Shuffled instruction: d = 0.625 (smallest)
- All d > 0.5 (large effects)
- Graduated response pattern confirms instruction content sensitivity
- Surprise finding: paraphrased > shuffled, indicating surface form dependency

**Interpretation:** L1 heads are instruction-sensitive with graduated response. Model depends more on surface form than deep semantics (paraphrased > shuffled). Supports C2 claim of instruction routing specialization.

**Completed:** 2026-05-18T17:31:15.868Z

---

### 8. **threecond_multiseed_r2_v2**

**Exp_ID:** threecond_multiseed_r2_v2

**Status:** DONE (success)

**Title/Description:** Multi-seed action probe comparison: trained vs llama2base vs untrained with sequential split

**Hypothesis:** Multi-seed action probes (3 seeds, sequential split matching original experiment) will confirm trained > llama2base > untrained R² gradient with low seed variance, validating single-seed findings are robust and not split-dependent.

**What it tests:** Tests whether the R² gradient across three conditions (trained > llama2base > untrained) holds across multiple random seeds and sequential data splits, confirming robustness and ruling out seed/split artifacts.

**Key metrics:**
- Trained peak (L9): R² = 0.643 ± 0.014 (mean ± std across 3 seeds: 42, 123, 456)
- Llama2base peak (L12): R² = 0.634 ± 0.013
- Untrained peak (L1): R² = 0.547 ± 0.008
- L0 baseline: R² = 0.645 ± 0.008 (consistent across all 3 conditions, shared vision encoder)
- Pattern L1–L15: U < L < T (untrained < llama2base < trained)
- Pattern L16–L25: L ≈ T >> U (llama2base ≈ trained >> untrained)
- Pattern L32: reversal anomaly (untrained: 0.589 ± 0.007, excluded)
- Trained-llama2base gap at peak: 0.009 (within seed variance, n=3)
- Data split: sequential (demo_0–39 train, demo_40–49 val)

**Interpretation:** Multi-seed validation confirms single-seed C2 gradient is robust. Untrained middle-layer collapse (negative R² + high variance) is the strongest signal differentiating conditions. Cross-seed consistency excellent.

**Completed:** 2026-05-18T09:10:58.657Z

---

## Summary Table

| Exp_ID | Status | Conclusion | Key Finding | Completed |
|--------|--------|------------|-------------|-----------|
| **ablation_50demos_main** | DONE | success | L1 R² increase (ΔR²=0.058, p=0) with 50 demos | 2026-05-17T21:49 |
| **action_trajectory_analysis** | DONE | success | Ablation → 72% token divergence, d=0.651 | 2026-05-18T11:02 |
| **action_trajectory_control** | DONE | **negative** | Control heads also significant (d=0.41), not L1-specific | 2026-05-18T11:45 |
| **random_subset_ablation** | DONE | success | Random 24-heads > dominant 24-heads (z=-2.73, p=0.003) | 2026-05-18T08:27 |
| **permutation_test_I2** | DONE | success | CV difference significant (p<0.05), I² marginal (p~0.14) | 2026-05-18T15:13 |
| **dose_response_curve** | DONE | success | Monotonic d: 0.482→0.639 (top-4→top-32), saturates ~12-16 | 2026-05-18T16:26 |
| **counterfactual_instruction** | DONE | success | Graduated d response (0.625–0.968), surface-form dependent | 2026-05-18T17:31 |
| **threecond_multiseed_r2_v2** | DONE | success | Multi-seed confirms trained (0.643±0.014) > llama2base (0.634±0.013) > untrained (0.547±0.008) | 2026-05-18T09:10 |

All experiments are completed and stored in `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "88384dbf-25a0-40dd-8e08-a2578d052013",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/, read the experiment registry file (likely registry.yaml or experiments.yaml) to find details for these 8 experiments:\n1. dose_response_curve\n2. counterfactual_instruction\n3. action_trajectory_analysis\n4. action_trajectory_control\n5. ablation_50demos_main\n6. random_subset_ablation\n7. permutation_test_I2\n8. threecond_multiseed_r2_v2\n\nFor each, I need: exp_id, title, key metrics, conclusion, and any description of what it tests. Report all findings.\n\nSearch breadth: very thorough",
    "agentId": "a9b100c2432c85c7e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information I need. Let me compile the complete report with all 8 experiments:\n\n## Experiment Registry Report: 8 Experiments\n\nHere are the detailed findings for all 8 experiments from `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml`:\n\n---\n\n### 1. **ablation_50demos_main**\n\n**Exp_ID:** ablation_50demos_main\n\n**Status:** DONE (success)\n\n**Title/Description:** L1 instruction-dominant head ablation with adequate probe training data (50 demos per task)\n\n**Hypothesis:** 50-demo full-data ablation: L1 instruction-dominant heads capacity trade-off (R² increase under ablation) persists with adequate probe training data, eliminating underfitting confound from 5-demo version.\n\n**What it tests:** Tests whether the capacity trade-off observed in instruction-dominant head ablation is robust when probe training has sufficient data (50 demos/task vs 5 demos), confirming the effect is not due to underfitting.\n\n**Key metrics:**\n- Baseline L1 R²: 0.5567\n- All 24 heads ablated L1 R²: 0.6153\n- All 24 vs baseline delta: 0.0585 (p=0)\n- All 24 vs control-8 delta: 0.0421 (p=0)\n- Confidence intervals provided for all comparisons\n\n**Completed:** 2026-05-17T21:49:51.638Z\n\n---\n\n### 2. **action_trajectory_analysis**\n\n**Exp_ID:** action_trajectory_analysis\n\n**Status:** DONE (success)\n\n**Title/Description:** L1 instruction-dominant head ablation effect on OpenVLA action predictions\n\n**Hypothesis:** L1 instruction-dominant head ablation significantly changes OpenVLA action predictions (measured by action token divergence and per-dimension MSE), demonstrating that instruction routing heads directly influence model output, not just intermediate representations.\n\n**What it tests:** Tests whether ablating L1 instruction-dominant heads produces measurable changes in the model's actual action token outputs, proving these heads have causal downstream effects beyond representation-level metrics.\n\n**Key metrics:**\n- Paired action MSE: 0.0416 ± 0.0639 (Cohen's d: 0.651, p < 0.001)\n- Token divergence rate: 72.3%\n- KL divergence: 5.079 ± 4.961\n- Per-dimension action shifts across 7 action dimensions (dx, dy, dz, rx, ry, rz, gripper)\n- Wilcoxon p-value: 0 (highly significant)\n- Per-task Cohen's d range: 0.433–0.729 (all 5 tasks significant)\n- n_samples: 2500\n\n**Completed:** 2026-05-18T11:02:27.281Z\n\n---\n\n### 3. **action_trajectory_control**\n\n**Exp_ID:** action_trajectory_control\n\n**Status:** DONE (negative)\n\n**Title/Description:** Control ablation (8 non-instruction heads) vs instruction-dominant heads action divergence comparison\n\n**Hypothesis:** Ablating 8 non-instruction heads (control) produces significantly smaller action divergence (especially gripper dimension) than ablating 24 instruction-dominant heads, proving the action output effect is instruction-specific rather than generic perturbation.\n\n**What it tests:** Tests whether the action divergence effect is specific to instruction-dominant heads or is a generic perturbation effect. Uses 8 non-instruction control heads to establish baseline.\n\n**Key metrics:**\n- Control 8-head MSE: 0.0201 ± 0.0489 (Cohen's d: 0.41, p ~ 10^-87)\n- Control token divergence: 29.3%\n- Control KL divergence: 1.69 ± 3.7\n- Comparison ratios: MSE ratio 2.07x, token divergence ratio 2.47x, KL ratio 3x (instruction vs control)\n- Per-task Cohen's d: 0.24–0.48\n- Per-head effect: control heads ~1.9x stronger per-head than expected (0.051 vs 0.027, p=0.0018)\n- Temporal coherence: instruction heads produce more consistent (CV 1.30 vs 2.74) and more task-dependent (I²=0.87 vs 0.78) perturbation\n\n**Conclusion:** Negative – specificity hypothesis not fully confirmed. Control heads also produce significant effects. However, instruction heads show qualitatively different (more coordinated) perturbation patterns.\n\n**Completed:** 2026-05-18T11:45:26.662Z\n\n---\n\n### 4. **random_subset_ablation**\n\n**Exp_ID:** random_subset_ablation\n\n**Status:** DONE (success)\n\n**Title/Description:** Random 24-head subsets produce larger action R² increases than instruction-dominant 24 heads\n\n**Hypothesis:** Random subsets of 24 heads yield higher action R² increase than instruction-dominant 24 heads, indicating dominant heads serve dual routing-encoding function rather than pure capacity trade-off.\n\n**What it tests:** Tests whether the instruction-dominant 24 heads are special by comparing their R² impact to 10 random 24-head subsets. If random subsets perform better, it challenges the \"dominant heads are special\" narrative.\n\n**Key metrics:**\n- Baseline R²: 0.517\n- Dominant-24 delta R²: 0.042\n- Random-24 mean delta R²: 0.077 ± 0.013 (std)\n- Z-score: -2.73\n- P-value: 0.003\n- n_random_seeds: 10\n- Effect size: random 24-head subsets ablate for ~83% larger R² increase than instruction-dominant heads\n\n**Interpretation:** Dominant-24 heads NOT special – any random 24/32 heads ablation produces similar or larger R² increase, supporting dual routing-encoding function explanation rather than capacity trade-off.\n\n**Completed:** 2026-05-18T08:27:15.118Z\n\n---\n\n### 5. **permutation_test_I2**\n\n**Exp_ID:** permutation_test_I2\n\n**Status:** DONE (success)\n\n**Title/Description:** Permutation test for CV and I² differences between instruction and control heads\n\n**Hypothesis:** Permutation test validates that observed CV difference (instruction 1.30 vs control 2.74) and I² difference (instruction 0.87 vs control 0.78) are not explained by random head assignment. Shuffling head labels 1000x produces null distribution; observed values should fall in extreme tail (p < 0.05).\n\n**What it tests:** Tests whether the differences in temporal coherence (CV) and task-dependency (I²) metrics between instruction and control heads are statistically significant or due to random chance.\n\n**Key metrics:**\n- CV exact paired p-value: 0.0156\n- CV MC unpaired p-value: 0.0048\n- CV 7D p-value: 0.0078\n- I² exact paired p-value: 0.1562\n- I² MC unpaired p-value: 0.1434\n- CV null mean: 0, std: 0.6756\n- I² null mean: 0, std: 0.2468\n\n**Interpretation:** CV differences are significant (p < 0.05), but I² differences are marginal (p ~ 0.14). Instruction heads produce more consistent perturbations across dimensions, but task-dependency is not significantly different from random.\n\n**Completed:** 2026-05-18T15:13:25.536Z\n\n---\n\n### 6. **dose_response_curve**\n\n**Exp_ID:** dose_response_curve\n\n**Status:** DONE (success)\n\n**Title/Description:** Dose-response curve of progressive L1 head ablation on action divergence\n\n**Hypothesis:** If instruction routing is a learned collective function, progressively ablating more L1 heads (sorted by instruction attention fraction) should produce monotonically increasing action divergence (dose-response curve). 8 conditions: top-4/8/12/16/20/24/28/32. Supports C2 claim that routing is a distributed, coordinated mechanism.\n\n**What it tests:** Tests whether the effect of head ablation is dose-dependent and monotonic, supporting the hypothesis that instruction routing is a collective, distributed mechanism rather than individual head contributions.\n\n**Key metrics:**\n- Cohen's d progression: d=0.482 (top-4) → 0.639 (top-32)\n- Pattern: Monotonically increasing dose-response curve\n- Diminishing returns observed at ~12–16 heads\n- 8 conditions tested: 4, 8, 12, 16, 20, 24, 28, 32 heads\n- Data: 5 tasks x 10 demos x 50 timesteps x 8 conditions = 20,000 forward passes\n\n**Interpretation:** Monotonic dose-response with diminishing returns supports distributed collective function hypothesis. Effect plateaus after ~16 heads, suggesting redundancy or saturation.\n\n**Completed:** 2026-05-18T16:26:06.324Z\n\n---\n\n### 7. **counterfactual_instruction**\n\n**Exp_ID:** counterfactual_instruction\n\n**Status:** DONE (success)\n\n**Title/Description:** L1 heads respond differently to incorrect/empty/paraphrased/shuffled instructions\n\n**Hypothesis:** L1 instruction-dominant heads perform instruction-specific routing: changing the instruction (wrong/empty/shuffled/paraphrased) should produce systematically different action outputs compared to correct instruction, with wrong and empty causing larger divergence than shuffled or paraphrased.\n\n**What it tests:** Tests whether L1 instruction-dominant heads are truly sensitive to instruction content and semantics. Compares action divergence across 4 counterfactual instruction conditions.\n\n**Key metrics:**\n- Cohen's d by condition:\n  - Empty instruction: d = 0.968 (largest)\n  - Wrong instruction: d = 0.844\n  - Paraphrased instruction: d = 0.697\n  - Shuffled instruction: d = 0.625 (smallest)\n- All d > 0.5 (large effects)\n- Graduated response pattern confirms instruction content sensitivity\n- Surprise finding: paraphrased > shuffled, indicating surface form dependency\n\n**Interpretation:** L1 heads are instruction-sensitive with graduated response. Model depends more on surface form than deep semantics (paraphrased > shuffled). Supports C2 claim of instruction routing specialization.\n\n**Completed:** 2026-05-18T17:31:15.868Z\n\n---\n\n### 8. **threecond_multiseed_r2_v2**\n\n**Exp_ID:** threecond_multiseed_r2_v2\n\n**Status:** DONE (success)\n\n**Title/Description:** Multi-seed action probe comparison: trained vs llama2base vs untrained with sequential split\n\n**Hypothesis:** Multi-seed action probes (3 seeds, sequential split matching original experiment) will confirm trained > llama2base > untrained R² gradient with low seed variance, validating single-seed findings are robust and not split-dependent.\n\n**What it tests:** Tests whether the R² gradient across three conditions (trained > llama2base > untrained) holds across multiple random seeds and sequential data splits, confirming robustness and ruling out seed/split artifacts.\n\n**Key metrics:**\n- Trained peak (L9): R² = 0.643 ± 0.014 (mean ± std across 3 seeds: 42, 123, 456)\n- Llama2base peak (L12): R² = 0.634 ± 0.013\n- Untrained peak (L1): R² = 0.547 ± 0.008\n- L0 baseline: R² = 0.645 ± 0.008 (consistent across all 3 conditions, shared vision encoder)\n- Pattern L1–L15: U < L < T (untrained < llama2base < trained)\n- Pattern L16–L25: L ≈ T >> U (llama2base ≈ trained >> untrained)\n- Pattern L32: reversal anomaly (untrained: 0.589 ± 0.007, excluded)\n- Trained-llama2base gap at peak: 0.009 (within seed variance, n=3)\n- Data split: sequential (demo_0–39 train, demo_40–49 val)\n\n**Interpretation:** Multi-seed validation confirms single-seed C2 gradient is robust. Untrained middle-layer collapse (negative R² + high variance) is the strongest signal differentiating conditions. Cross-seed consistency excellent.\n\n**Completed:** 2026-05-18T09:10:58.657Z\n\n---\n\n## Summary Table\n\n| Exp_ID | Status | Conclusion | Key Finding | Completed |\n|--------|--------|------------|-------------|-----------|\n| **ablation_50demos_main** | DONE | success | L1 R² increase (ΔR²=0.058, p=0) with 50 demos | 2026-05-17T21:49 |\n| **action_trajectory_analysis** | DONE | success | Ablation → 72% token divergence, d=0.651 | 2026-05-18T11:02 |\n| **action_trajectory_control** | DONE | **negative** | Control heads also significant (d=0.41), not L1-specific | 2026-05-18T11:45 |\n| **random_subset_ablation** | DONE | success | Random 24-heads > dominant 24-heads (z=-2.73, p=0.003) | 2026-05-18T08:27 |\n| **permutation_test_I2** | DONE | success | CV difference significant (p<0.05), I² marginal (p~0.14) | 2026-05-18T15:13 |\n| **dose_response_curve** | DONE | success | Monotonic d: 0.482→0.639 (top-4→top-32), saturates ~12-16 | 2026-05-18T16:26 |\n| **counterfactual_instruction** | DONE | success | Graduated d response (0.625–0.968), surface-form dependent | 2026-05-18T17:31 |\n| **threecond_multiseed_r2_v2** | DONE | success | Multi-seed confirms trained (0.643±0.014) > llama2base (0.634±0.013) > untrained (0.547±0.008) | 2026-05-18T09:10 |\n\nAll experiments are completed and stored in `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml`."
      }
    ],
    "totalDurationMs": 68260,
    "totalTokens": 45760,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 41978,
      "output_tokens": 3616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 3616,
          "cache_read_input_tokens": 41978,
          "cache_creation_input_tokens": 166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 166,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 1,
      "bashCount": 6,
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

_source line 140_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me read the actual experiments.tex to understand the exact §4.3 content and the discussion.tex for convergent evidence items. Then I'll construct the updated paper_provenance.yaml.

Let me read the key tex files to find the exact claim text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "89812f04-44aa-454b-96bf-e66ec0a5ea0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnoN4Hgp95CckUH1MHTo5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8546,
      "cache_read_input_tokens": 50350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8546
      },
      "output_tokens": 22,
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

_source line 141_

Let me read the actual tex files to find the exact claim text for mapping.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "78541749-e55d-4ba4-90ca-8f84b6332c91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnoN4Hgp95CckUH1MHTo5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8546,
      "cache_read_input_tokens": 50350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8546
      },
      "output_tokens": 22,
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

_source line 142_

<details open><summary>🔧 Tool call — Read · `toolu_0195YuPXCaX2tMrhKmGzWK8s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex",
  "offset": 140,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "199776a9-df3f-4da6-ba84-c9a11b7f3f88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnoN4Hgp95CckUH1MHTo5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8546,
      "cache_read_input_tokens": 50350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8546
      },
      "output_tokens": 22,
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

_source line 143 · 2026-05-18T17:44:25.712Z_

<details><summary>↩ Tool result · `toolu_0195YuPXCaX2tMrhKmGzWK8s`</summary>

```text
140	\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\_mean ($R^2{=}0.683$) below the projector baseline ($0.706$, $p{=}0.001$) but concentrates superior information at the trained readout ($0.731$, $p{=}0.001$). Untrained readout ($0.686$) falls below the projector, confirming that concentration requires training ($\Delta{=}0.045$, $p{<}0.0001$). DINOv2 ($0.712$) is statistically indistinguishable from the projector ($p{=}0.22$).}
141	\label{fig:probe_bars}
142	\end{figure}
143	
144	%------------------------------------------------------------------
145	\subsection{Training Routes, Does Not Create, Action Geometry}
146	\label{sec:training_routing}
147	
148	This experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.
149	Table~\ref{tab:training_effects} reports the effect of training across metrics.
150	The $2 \times 2$ factorial analysis (Figure~\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.
151	
152	\paragraph{Geometric invariance to training.}
153	Training does not alter the LLM's geometric alignment with the action space.
154	For image\_mean RSA, the training effect is $\Delta = +0.021$ (95\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\_preaction RSA, $\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).
155	This null result is consistent with the vision encoder---whose weights are identical between conditions ($\cos\text{sim} = 1.0$)---being the sole source of action-relevant geometry.
156	
157	\paragraph{Geometric invariance to instruction.}
158	Language instructions similarly fail to modulate geometric structure.
159	Across the $2 \times 2$ matrix, the instruction effect is $\Delta = 0.004$ (n.s.).
160	A dedicated control experiment with four instruction conditions---normal task instructions ($\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\pm 0.017$ of the mean (Figure~\ref{fig:factorial}b).
161	
162	\paragraph{Functional concentration requires training.}
163	In contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\Delta = +0.045$ (CI $[+0.032, +0.058]$, $p < 0.0001$).
164	Training transforms the readout from below-projector ($R^2 = 0.686$) to above-projector ($R^2 = 0.731$) without altering the underlying geometry.
165	
166	These results support a \emph{routing} interpretation of LLM training in VLAs~\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.
167	
168	\begin{table}[t]
169	\centering
170	\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\_mean $R^2$ drop confirms distributed degradation.}
171	\label{tab:training_effects}
172	\small
173	\begin{tabular}{lccc}
174	\toprule
175	Comparison & $\Delta$ & 95\% CI & $p$ \\
176	\midrule
177	Training (image\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\
178	Training (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\
179	Training (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\
180	Proj.\ vs.\ image\_mean ($R^2$) & $+$0.023 & [$+$0.011, $+$0.037] & 0.001 \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	\begin{figure}[t]
186	\centering
187	\includegraphics[width=\columnwidth]{figures/fig5.pdf}
188	\caption{\textbf{(a)}~Training $\times$ Instruction matrix for image\_mean RSA ($\rho$). Neither training ($\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\Delta{=}0.004$, n.s.)\ produces a statistically detectable effect. \textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\pm 0.017$ of the mean $\mu{=}0.482$, confirming that instruction content does not modulate distributed geometric structure.}
189	\label{fig:factorial}
190	\end{figure}
191	
192	\begin{figure}[t]
193	\centering
194	\includegraphics[width=\columnwidth]{figures/fig6.pdf}
195	\caption{Comparison of three similarity metrics across representation sources. \textbf{(a)}~RSA (Spearman $\rho$) and \textbf{(c)}~RDM kernel CKA produce consistent rankings (Proj $>$ Trained $>$ Untrained $>$ DINOv2). \textbf{(b)}~Linear CKA~\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}
196	\label{fig:metric_comparison}
197	\end{figure}
198	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "067e5154-e708-4a61-9ca3-73e3690ceef4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex",
      "content": "\\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\\_mean ($R^2{=}0.683$) below the projector baseline ($0.706$, $p{=}0.001$) but concentrates superior information at the trained readout ($0.731$, $p{=}0.001$). Untrained readout ($0.686$) falls below the projector, confirming that concentration requires training ($\\Delta{=}0.045$, $p{<}0.0001$). DINOv2 ($0.712$) is statistically indistinguishable from the projector ($p{=}0.22$).}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Routes, Does Not Create, Action Geometry}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.\nTable~\\ref{tab:training_effects} reports the effect of training across metrics.\nThe $2 \\times 2$ factorial analysis (Figure~\\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.\n\n\\paragraph{Geometric invariance to training.}\nTraining does not alter the LLM's geometric alignment with the action space.\nFor image\\_mean RSA, the training effect is $\\Delta = +0.021$ (95\\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\\_preaction RSA, $\\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).\nThis null result is consistent with the vision encoder---whose weights are identical between conditions ($\\cos\\text{sim} = 1.0$)---being the sole source of action-relevant geometry.\n\n\\paragraph{Geometric invariance to instruction.}\nLanguage instructions similarly fail to modulate geometric structure.\nAcross the $2 \\times 2$ matrix, the instruction effect is $\\Delta = 0.004$ (n.s.).\nA dedicated control experiment with four instruction conditions---normal task instructions ($\\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\\pm 0.017$ of the mean (Figure~\\ref{fig:factorial}b).\n\n\\paragraph{Functional concentration requires training.}\nIn contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\\Delta = +0.045$ (CI $[+0.032, +0.058]$, $p < 0.0001$).\nTraining transforms the readout from below-projector ($R^2 = 0.686$) to above-projector ($R^2 = 0.731$) without altering the underlying geometry.\n\nThese results support a \\emph{routing} interpretation of LLM training in VLAs~\\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\\_mean $R^2$ drop confirms distributed degradation.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nTraining (image\\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\\\\nTraining (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\\\\nTraining (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\\\\nProj.\\ vs.\\ image\\_mean ($R^2$) & $+$0.023 & [$+$0.011, $+$0.037] & 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Training $\\times$ Instruction matrix for image\\_mean RSA ($\\rho$). Neither training ($\\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\\Delta{=}0.004$, n.s.)\\ produces a statistically detectable effect. \\textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\\pm 0.017$ of the mean $\\mu{=}0.482$, confirming that instruction content does not modulate distributed geometric structure.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Comparison of three similarity metrics across representation sources. \\textbf{(a)}~RSA (Spearman $\\rho$) and \\textbf{(c)}~RDM kernel CKA produce consistent rankings (Proj $>$ Trained $>$ Untrained $>$ DINOv2). \\textbf{(b)}~Linear CKA~\\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}\n\\label{fig:metric_comparison}\n\\end{figure}\n",
      "numLines": 59,
      "startLine": 140,
      "totalLines": 198
    }
  }
}
```

</details>

---


### Tool call

_source line 144_

<details open><summary>🔧 Tool call — Read · `toolu_01X67nzvk11UQxaCnPESYnTq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "168c85d6-4dd5-4e98-9b38-b0f827a7d170",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnoN4Hgp95CckUH1MHTo5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8546,
      "cache_read_input_tokens": 50350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8546
      },
      "output_tokens": 22,
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

_source line 145 · 2026-05-18T17:44:25.745Z_

<details><summary>↩ Tool result · `toolu_01X67nzvk11UQxaCnPESYnTq`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Our experiments reveal a coherent picture of how action-relevant structure flows through a VLA.
6	The vision encoder is the \emph{source}: VL-pretrained encoders provide geometric structure aligned with the action space (SigLIP+Projector RSA $\rho = 0.615$; CLIP $\rho = 0.557$), far exceeding what the LLM produces at any layer ($\rho \leq 0.501$).
7	The LLM is a \emph{router}: it degrades distributed geometric structure ($\rho$: $0.615 \to 0.501$; $R^2$: $0.706 \to 0.683$) while concentrating a functionally superior representation at the readout token ($R^2 = 0.731$).
8	Training teaches the \emph{routing policy}: the geometric structure itself is invariant to training ($\Delta\rho = 0.021$, $p = 0.20$), but functional concentration at the readout requires it ($\Delta R^2 = 0.045$, $p < 0.0001$).
9	Notably, the projector alone captures 96.6\% of the trained readout's functional capacity ($0.706/0.731$), suggesting that the LLM's contribution, while statistically significant, is incremental.
10	
11	\paragraph{VL pretraining as a general source of action-relevant geometry.}
12	The inclusion of CLIP ViT-L/14 as an external baseline provides evidence that action-relevant geometric structure is a general product of vision-language pretraining, not an artifact of SigLIP's specific architecture or training data.
13	Both VL-pretrained encoders---SigLIP ($\rho = 0.615$) and CLIP ($\rho = 0.557$)---substantially exceed vision-only DINOv2 ($\rho = 0.388$).
14	The 0.169-point gap between CLIP and DINOv2, both ViT-L/14 architectures differing primarily in pretraining objective, isolates language grounding as the operative factor.
15	The additional increment from CLIP to SigLIP+Projector ($\Delta = 0.058$) is consistent with the projector's VLA-supervised alignment providing a modest boost, but the dominant contribution ($\rho = 0.557 \gg 0.388$) originates in VL pretraining itself.
16	
17	\paragraph{Geometric-functional dissociation.}
18	A recurring finding across our analyses is the dissociation between geometric alignment (RSA) and functional decodability (probe $R^2$).
19	DINOv2 achieves probe performance statistically indistinguishable from the SigLIP+Projector ($R^2$: $0.712$ vs.\ $0.706$, $p = 0.22$) despite substantially lower RSA ($0.388$ vs.\ $0.615$).
20	This dissociation implies that action information---in the sense of decodable content---is broadly available in strong visual features regardless of pretraining objective; what VL pretraining adds is \emph{geometric alignment}, organizing that information into a structure that mirrors the action space.
21	For VLA design, this distinction matters: encoder selection determines not just what information is available, but how it is organized, with downstream consequences for how easily the LLM can route it.
22	
23	\paragraph{Metric sensitivity: RSA versus CKA.}
24	The divergence between RSA and linear CKA underscores the importance of multi-metric evaluation.
25	Linear CKA produces a ranking---untrained LLM ($0.089$) $>$ trained ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$)---that partially reverses the RSA ordering.
26	Under linear CKA, training appears to \emph{reduce} similarity to the action space, an interpretation that contradicts both RSA and functional probe evidence.
27	RDM kernel CKA resolves this discrepancy, restoring the RSA-consistent ranking (trained $0.260$ $>$ Proj $0.257$ $>$ untrained $0.246$ $>$ DINOv2 $0.241$).
28	The divergence likely reflects linear CKA's sensitivity to second-order statistics and its known vulnerability to dimension mismatch between high-dimensional representations and the 7-D action space~\cite{kornblith2019}.
29	The practical implication is that the LLM transforms rather than destroys action structure, but the narrative one draws depends critically on which metric is employed.
30	
31	\paragraph{Implications for VLA design.}
32	Our findings suggest four practical considerations.
33	\emph{First}, vision encoder pretraining quality is the primary lever for action-relevant representations; investing in stronger VL encoders may yield larger gains than scaling the LLM backbone.
34	\emph{Second}, for downstream modules that operate on distributed representations (e.g., auxiliary losses, multi-task heads), the projector output may be preferable to LLM-processed features, given its higher geometric fidelity and 96.6\% of readout-level decodability.
35	\emph{Third}, the LLM's value lies in readout concentration---routing distributed information to a single decoding site---which informs action head design: architectures that exploit this concentration (e.g., reading from a dedicated token rather than pooling LLM features) may better leverage the LLM's trained routing.
36	\emph{Fourth}, the invariance of representation geometry to language instructions ($\Delta\rho = 0.004$, n.s.; content controls within $\pm 0.017$) suggests that instructions influence action selection through a mechanism other than modulating visual representation structure, inviting further investigation into how language conditions behavior in VLAs.
37	
38	\paragraph{Connection to behavioral evidence.}
39	Our representational findings complement the behavioral results of \citet{grant2026}, who showed that VLA policies are disproportionately driven by visual input and that language instructions are ``encoded but not used'' for action selection.
40	Our data provide a representational account of these behavioral patterns: vision dominates because the frozen encoder supplies the action-relevant geometric structure that the LLM routes to the readout, while instruction content does not modulate this geometric structure (all four instruction conditions yield RSA within $\pm 0.017$).
41	The alignment between representational and behavioral evidence strengthens the case that VL-pretrained vision encoders, rather than LLM reasoning, are the primary computational substrate for action generation in current VLA architectures.
42	
43	\paragraph{Limitations.}
44	Several limitations scope our conclusions.
45	We study a single VLA architecture (OpenVLA-7B) on a single benchmark suite (LIBERO); generalization to other architectures (e.g., RT-2~\cite{brohan2023_rt2}) and domains (e.g., mobile manipulation, dexterous hands) remains to be established.
46	RSA captures structural alignment between representations and actions but does not establish causal contribution---high RSA does not guarantee that the representation is causally used by the policy.
47	The CLIP and DINOv2 action probes were trained with different hyperparameters (100 epochs) than the projector and LLM probes (50 epochs); while within-experiment comparisons are valid, absolute $R^2$ values are not directly comparable across these two probe sets, and we have been careful to restrict cross-experiment claims accordingly.
48	Finally, our analyses characterize frozen representations post hoc; they do not address how these representations emerge during VLA pretraining or fine-tuning, nor whether architectural interventions (e.g., unfreezing the vision encoder) would alter the source--router dynamic we observe.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "1e3cc28e-9fdd-441e-a972-eba520e64f2f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nOur experiments reveal a coherent picture of how action-relevant structure flows through a VLA.\nThe vision encoder is the \\emph{source}: VL-pretrained encoders provide geometric structure aligned with the action space (SigLIP+Projector RSA $\\rho = 0.615$; CLIP $\\rho = 0.557$), far exceeding what the LLM produces at any layer ($\\rho \\leq 0.501$).\nThe LLM is a \\emph{router}: it degrades distributed geometric structure ($\\rho$: $0.615 \\to 0.501$; $R^2$: $0.706 \\to 0.683$) while concentrating a functionally superior representation at the readout token ($R^2 = 0.731$).\nTraining teaches the \\emph{routing policy}: the geometric structure itself is invariant to training ($\\Delta\\rho = 0.021$, $p = 0.20$), but functional concentration at the readout requires it ($\\Delta R^2 = 0.045$, $p < 0.0001$).\nNotably, the projector alone captures 96.6\\% of the trained readout's functional capacity ($0.706/0.731$), suggesting that the LLM's contribution, while statistically significant, is incremental.\n\n\\paragraph{VL pretraining as a general source of action-relevant geometry.}\nThe inclusion of CLIP ViT-L/14 as an external baseline provides evidence that action-relevant geometric structure is a general product of vision-language pretraining, not an artifact of SigLIP's specific architecture or training data.\nBoth VL-pretrained encoders---SigLIP ($\\rho = 0.615$) and CLIP ($\\rho = 0.557$)---substantially exceed vision-only DINOv2 ($\\rho = 0.388$).\nThe 0.169-point gap between CLIP and DINOv2, both ViT-L/14 architectures differing primarily in pretraining objective, isolates language grounding as the operative factor.\nThe additional increment from CLIP to SigLIP+Projector ($\\Delta = 0.058$) is consistent with the projector's VLA-supervised alignment providing a modest boost, but the dominant contribution ($\\rho = 0.557 \\gg 0.388$) originates in VL pretraining itself.\n\n\\paragraph{Geometric-functional dissociation.}\nA recurring finding across our analyses is the dissociation between geometric alignment (RSA) and functional decodability (probe $R^2$).\nDINOv2 achieves probe performance statistically indistinguishable from the SigLIP+Projector ($R^2$: $0.712$ vs.\\ $0.706$, $p = 0.22$) despite substantially lower RSA ($0.388$ vs.\\ $0.615$).\nThis dissociation implies that action information---in the sense of decodable content---is broadly available in strong visual features regardless of pretraining objective; what VL pretraining adds is \\emph{geometric alignment}, organizing that information into a structure that mirrors the action space.\nFor VLA design, this distinction matters: encoder selection determines not just what information is available, but how it is organized, with downstream consequences for how easily the LLM can route it.\n\n\\paragraph{Metric sensitivity: RSA versus CKA.}\nThe divergence between RSA and linear CKA underscores the importance of multi-metric evaluation.\nLinear CKA produces a ranking---untrained LLM ($0.089$) $>$ trained ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$)---that partially reverses the RSA ordering.\nUnder linear CKA, training appears to \\emph{reduce} similarity to the action space, an interpretation that contradicts both RSA and functional probe evidence.\nRDM kernel CKA resolves this discrepancy, restoring the RSA-consistent ranking (trained $0.260$ $>$ Proj $0.257$ $>$ untrained $0.246$ $>$ DINOv2 $0.241$).\nThe divergence likely reflects linear CKA's sensitivity to second-order statistics and its known vulnerability to dimension mismatch between high-dimensional representations and the 7-D action space~\\cite{kornblith2019}.\nThe practical implication is that the LLM transforms rather than destroys action structure, but the narrative one draws depends critically on which metric is employed.\n\n\\paragraph{Implications for VLA design.}\nOur findings suggest four practical considerations.\n\\emph{First}, vision encoder pretraining quality is the primary lever for action-relevant representations; investing in stronger VL encoders may yield larger gains than scaling the LLM backbone.\n\\emph{Second}, for downstream modules that operate on distributed representations (e.g., auxiliary losses, multi-task heads), the projector output may be preferable to LLM-processed features, given its higher geometric fidelity and 96.6\\% of readout-level decodability.\n\\emph{Third}, the LLM's value lies in readout concentration---routing distributed information to a single decoding site---which informs action head design: architectures that exploit this concentration (e.g., reading from a dedicated token rather than pooling LLM features) may better leverage the LLM's trained routing.\n\\emph{Fourth}, the invariance of representation geometry to language instructions ($\\Delta\\rho = 0.004$, n.s.; content controls within $\\pm 0.017$) suggests that instructions influence action selection through a mechanism other than modulating visual representation structure, inviting further investigation into how language conditions behavior in VLAs.\n\n\\paragraph{Connection to behavioral evidence.}\nOur representational findings complement the behavioral results of \\citet{grant2026}, who showed that VLA policies are disproportionately driven by visual input and that language instructions are ``encoded but not used'' for action selection.\nOur data provide a representational account of these behavioral patterns: vision dominates because the frozen encoder supplies the action-relevant geometric structure that the LLM routes to the readout, while instruction content does not modulate this geometric structure (all four instruction conditions yield RSA within $\\pm 0.017$).\nThe alignment between representational and behavioral evidence strengthens the case that VL-pretrained vision encoders, rather than LLM reasoning, are the primary computational substrate for action generation in current VLA architectures.\n\n\\paragraph{Limitations.}\nSeveral limitations scope our conclusions.\nWe study a single VLA architecture (OpenVLA-7B) on a single benchmark suite (LIBERO); generalization to other architectures (e.g., RT-2~\\cite{brohan2023_rt2}) and domains (e.g., mobile manipulation, dexterous hands) remains to be established.\nRSA captures structural alignment between representations and actions but does not establish causal contribution---high RSA does not guarantee that the representation is causally used by the policy.\nThe CLIP and DINOv2 action probes were trained with different hyperparameters (100 epochs) than the projector and LLM probes (50 epochs); while within-experiment comparisons are valid, absolute $R^2$ values are not directly comparable across these two probe sets, and we have been careful to restrict cross-experiment claims accordingly.\nFinally, our analyses characterize frozen representations post hoc; they do not address how these representations emerge during VLA pretraining or fine-tuning, nor whether architectural interventions (e.g., unfreezing the vision encoder) would alter the source--router dynamic we observe.\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  }
}
```

</details>

---


### Assistant

_source line 146_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the paper structure. The current §4.3 is about "Training Routes, Does Not Create, Action Geometry" and the Discussion section has specific paragraphs.

But wait - the 8 experiments I need to map don't directly correspond to the current §4.3 content. Let me re-read the task:

1. **dose_response_curve** → §4.3 dose-response 段落 + Discussion convergent evidence (4)
2. **counterfactual_instruction** → §4.3 counterfactual 段落 + Discussion convergent evidence (5)


3. **action_trajectory_analysis** → §4.3 action trajectory 段落 + Discussion convergent evidence (3)
4. **action_trajectory_control** → §4.3 control ablation + Discussion per-head
5. **ablation_50demos_main** → §4.3 ablation results + Discussion convergent evidence (2)
6. **random_subset_ablation** → §4.3 random subset comparison
7. **permutation_test_I2** → Appendix §A.8 CV permutation
8. **threecond_multiseed_r2_v** → appears to be cut off, likely another experiment mapping

Now I'm looking at the three-condition multi-seed results that should map to §4.1 and §4.2. These experiments seem to be part of a new section that hasn't been fully written yet, so I'm working through which paper claims they'll support and constructing the proper YAML entries with the right structure—each claim needs its location, evidence list, and type classification.

The task is asking me to map experiments prospectively to where they'll appear in the paper, so I need to either add these as evidence to existing claims or create new claim entries for planned sections like the dose-response analysis in §4.3. Looking at the claim structure more carefully, I think the new §4.3 mentioned in the task is actually a separate subsection about convergent evidence and causal validation, not the existing routing section, so I should create fresh claim entries for that content.

Now I'm reviewing which existing claims already have L1 ablation evidence and which ones might need updates. I see C108 covers the multi-layer comparison, C381 covers the control condition with frozen encoders, and C395 documents the effect size and layer-specificity findings. There's also C416 that appears to be about the full-scale replication with minimal demos, so I need to check what evidence is already attached to these claims versus what's still missing.

Looking at the coverage gap—we're at 69 out of 74 experiments mapped—I should focus on creating new claim entries for the experiments that don't fit into the existing paper sections yet, particularly the dose-response, counterfactual, and action trajectory analyses. For each new experiment, I'll need to establish the claim, link the tier1 evidence, and that should help close the coverage gap. I see that tier1 is completely empty—everything got marked as tier2 "inferred" during the auto build, even though the deprecated claims have tier1 entries. So I need to find the non-deprecated claims that map to each experiment and add tier1 evidence entries to boost the tier distribution.

Looking at the experiments, the dose-response curve experiment doesn't have a corresponding claim yet, so I'll need to create one documenting the monotonic relationship between ablation depth and performance. The counterfactual instruction experiment also lacks a specific claim mapping.

For the action trajectory analysis, C395 covers ablation effects on R2 but not the actual action token divergence that this experiment measures, so that needs its own claim. The control ablation experiment is related but distinct from the action trajectory work.

Looking at the ablation results section, C395 and C108 both touch on the L1 ablation findings, though C416 highlights the scale limitation that the 50-demo version addresses. The random subset and permutation test experiments don't have corresponding claims yet, so those need new ones. For the multiseed R2 analysis, I'm checking what C152 covers.

Now I'm examining the DINOv2 encoder alignment metrics and layer-wise performance patterns across different probing approaches. The data shows peak R2 values in mid-to-late layers, with readout performance exceeding the projector baseline, and some training-related shifts in both RSA and R2 measures.

But I'm noticing the threecond_multiseed_r2_v2 experiment provides fresh multi-seed validation across three conditions—trained, llama2base, and untrained—with peak R2 values around 0.643, 0.634, and 0.547 respectively. These numbers differ from the older experimental runs cited in the existing claims, so I should treat this as new supporting evidence for the R2 gradient pattern rather than replacing the previous findings. The cleanest approach is to layer this new experiment in as additional validation for the existing claims.

Now I'm realizing the actual constraint: the paper_provenance.yaml file is too large to rewrite in full, and it's not even in the whitelist for save_project_file anyway. I need to check whether there's a dedicated tool for updating the provenance file, or if I should focus on updating the other writable files like memory.md or writing_plan.yaml instead. efficient way to do this. I'll use the Edit tool to make targeted changes—adding new claim entries before the figures section, updating existing claims with new evidence, and modifying the completeness section. Looking at the task mapping, I need to connect each analysis result to its corresponding section and discussion evidence, then figure out whether to create new claims or update existing ones.

Searching through the YAML content for these experiment IDs, I'm finding that most of them—dose_response_curve, counterfactual_instruction, action_trajectory_analysis, action_trajectory_control, and ablation_50demos_main—aren't currently in any claim evidence entries. This suggests they're either missing entirely or only exist as tier2 inferred entries from the auto_build, which achieved 69/74 coverage but with significant tier2 inference. I need to check what's already there and determine which experiments need to be added as new evidence versus upgraded from existing tier2 entries. appears as text in evidence descriptions)
- random_subset_ablation: NOT found
- permutation_test_I2: NOT found
- threecond_multiseed_r2_v2: NOT found

So none of these 8 experiments are currently mapped in the provenance file. I need to create new claims for the §4.3 content covering dose-response, counterfactual, trajectory, and ablation analyses, plus add evidence to existing claims for threecond_multiseed_r2_v2.

Since the current §4.3 focuses on RSA invariance and functional concentration, these new causal validation experiments might extend that section or shift the numbering entirely. For provenance mapping, I should define claims representing the planned paper content even before the text is finalized.

Starting with claim IDs from C430 onward, I'm mapping the dose-response curve showing monotonic increases in action divergence as more L1 heads get ablated, with diminishing returns around 12-16 heads, and creating a corresponding discussion claim about how this monotonic pattern supports distributed collective routing.

For the counterfactual instruction manipulation, I'm capturing the graduated action divergence across empty, wrong, paraphrased, and shuffled conditions, plus a mechanistic claim confirming that L1 heads perform instruction-specific routing.

The action trajectory analysis shows 72.3% token divergence when ablating instruction-dominant heads, and I'm continuing to map the remaining experiments in this causal validation suite. ence rate and significant action MSE (Cohen's d=0.651, p<0.001) in the experiments section. The control ablation with 8 heads shows smaller overall divergence but larger per-head effects, suggesting instruction heads operate with more coordinated perturbation patterns despite lacking specificity in magnitude. A 50-demo ablation confirms the capacity trade-off isn't just an underfitting artifact, with R² improving from baseline to ablated conditions when given adequate training data.

Random 24-head subsets actually produce larger R² gains than the instruction-dominant heads alone, indicating the effect isn't unique to instruction-selective neurons. Permutation testing validates the coefficient of variation difference between instruction and control heads, though the I² metric shows only marginal significance. Looking at the three-condition data across multiple seeds...

The trained model consistently outperforms both the base and untrained versions in R² across the gradient, with the peak performance at layer 9 reaching 0.643. I notice this overlaps somewhat with existing claims about R² peaks and readout performance, but the numbers differ because they're from different experimental setups, so I'll document this as a separate finding rather than trying to merge them.

Now I'm thinking through the best way to integrate these results into the YAML structure—I should add new claim entries for each experiment with proper tier1 mapping, then locate where to insert them before the figures section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "2a2bac36-73ad-439e-b579-7a13454fb043",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8t3Kn8Ms1G51CP3CsJZxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3937,
      "cache_read_input_tokens": 58896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3937
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

_source line 147_

Now I need to find the insertion point in the YAML. Let me read the end of the claims section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "0e601bdf-81ac-4e6b-87cd-3a07f6500861",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8t3Kn8Ms1G51CP3CsJZxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3937,
      "cache_read_input_tokens": 58896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3937
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

_source line 148_

<details open><summary>🔧 Tool call — Grep · `toolu_018Y6SSpSP9FGKv1d5WDvzMZ`</summary>

```json
{
  "pattern": "^figures:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "51ec3ff4-d5a4-4339-af8d-7eb34c17d507",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8t3Kn8Ms1G51CP3CsJZxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3937,
      "cache_read_input_tokens": 58896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3937
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

_source line 149 · 2026-05-18T17:46:06.451Z_

<details><summary>↩ Tool result · `toolu_018Y6SSpSP9FGKv1d5WDvzMZ`</summary>

```text
1747:figures:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "24b86704-dc61-4758-959c-0bb987ac9ddd",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1747:figures:",
    "numLines": 1
  }
}
```

</details>

---


### Tool call

_source line 150_

<details open><summary>🔧 Tool call — Grep · `toolu_01AXSz8WrMNVALcaxYxKPTth`</summary>

```json
{
  "pattern": "^_completeness:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "63e727f6-8630-45a8-ab62-1f27a795119f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8t3Kn8Ms1G51CP3CsJZxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3937,
      "cache_read_input_tokens": 58896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3937
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

_source line 151 · 2026-05-18T17:46:06.971Z_

<details><summary>↩ Tool result · `toolu_01AXSz8WrMNVALcaxYxKPTth`</summary>

```text
1885:_completeness:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "bbb3946b-9b94-4320-9b11-88bd6cf1696e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1885:_completeness:",
    "numLines": 1
  }
}
```

</details>

---


### Tool call

_source line 152_

<details open><summary>🔧 Tool call — Read · `toolu_0148e1h8BGwzTJKQwu4o4e2a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
  "offset": 1735,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "33857ec2-115f-4208-8b26-0788cc220f28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q83AgEQmg4A217RA2q5AZ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5211,
      "cache_read_input_tokens": 62833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5211
      },
      "output_tokens": 69,
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

_source line 153 · 2026-05-18T17:46:09.891Z_

<details><summary>↩ Tool result · `toolu_0148e1h8BGwzTJKQwu4o4e2a`</summary>

```text
1735	    section: experiments
1736	    paragraph: 0
1737	    sentence: 0
1738	  text: non-monotonic profile stable under 25-demo subsampling, RSA peak unchanged
1739	    L12, profile r=0.97
1740	  type: quantitative
1741	  evidence:
1742	  - exp_id: ablation_p2_demo_sensitivity
1743	    metric: profile_correlation_RSA
1744	    value: '0.970'
1745	  decisions: []
1746	  deprecated: false
1747	figures:
1748	- caption: Three similarity metrics across representation sources. \textbf{(a)
1749	  deprecated: false
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "3c95ebc9-da6b-4414-aa46-8f47b157b78a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
      "content": "    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: non-monotonic profile stable under 25-demo subsampling, RSA peak unchanged\n    L12, profile r=0.97\n  type: quantitative\n  evidence:\n  - exp_id: ablation_p2_demo_sensitivity\n    metric: profile_correlation_RSA\n    value: '0.970'\n  decisions: []\n  deprecated: false\nfigures:\n- caption: Three similarity metrics across representation sources. \\textbf{(a)\n  deprecated: false",
      "numLines": 15,
      "startLine": 1735,
      "totalLines": 1896
    }
  }
}
```

</details>

---


### Tool call

_source line 154_

<details open><summary>🔧 Tool call — Read · `toolu_01KysxFUNwJGNwkxKVzx8VKX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
  "offset": 1883,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "3a010335-bfea-4b5c-b2e6-759e65adb54b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q83AgEQmg4A217RA2q5AZ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5211,
      "cache_read_input_tokens": 62833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5211
      },
      "output_tokens": 69,
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

_source line 155 · 2026-05-18T17:46:10.583Z_

<details><summary>↩ Tool result · `toolu_01KysxFUNwJGNwkxKVzx8VKX`</summary>

```text
1883	  location:
1884	    section: experiments
1885	_completeness:
1886	  coverage: 69/74
1887	  claims: 71
1888	  tables: 0
1889	  figures: 3
1890	  tier_counts:
1891	    tier1: 0
1892	    tier2: 69
1893	    tier3: 5
1894	    tierX: 0
1895	  last_checked: '2026-05-17T22:15:14.113771+00:00'
1896	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "0c43155a-db9d-44cb-a68a-567d5a6f754b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
      "content": "  location:\n    section: experiments\n_completeness:\n  coverage: 69/74\n  claims: 71\n  tables: 0\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 69\n    tier3: 5\n    tierX: 0\n  last_checked: '2026-05-17T22:15:14.113771+00:00'\n",
      "numLines": 14,
      "startLine": 1883,
      "totalLines": 1896
    }
  }
}
```

</details>

---


### Assistant

_source line 156_

<details><summary>Logged reasoning block</summary>

```text
Now I have the insertion points. I'll:

1. Insert 13 new claim entries before line 1747 (`figures:`)
2. Update the `_completeness` section to reflect new coverage

Let me construct the new claims and add them. I need to add them right before `figures:` (between line 1746 and 1747).

Actually, let me reconsider the number of claims. The task maps 8 experiments to specific sections. Some experiments map to both §4.3 AND Discussion, so they appear in multiple claims. Let me be precise:

1. dose_response_curve → §4.3 dose-response + Discussion convergent evidence (4)


2. counterfactual_instruction → §4.3 counterfactual + Discussion convergent evidence (5)
3. action_trajectory_analysis → §4.3 action trajectory + Discussion convergent evidence (3)
4. action_trajectory_control → §4.3 control ablation + Discussion per-head
5. ablation_50demos_main → §4.3 ablation results + Discussion convergent evidence (2)
6. random_subset_ablation → §4.3 random subset comparison
7. permutation_test_I2 → Appendix §A.8 CV permutation
8. threecond_multiseed_r2_v2 → §4.1 + §4.2

Now I'm mapping out where each experiment's claims should go. I see there are 6 experiments with primary claims in the experiments section, 5 with discussion claims, 1 in the appendix, and 1 spanning both §4.1 and §4.2. That's 13 new claims total. I'll follow the existing YAML pattern and create one primary claim per experiment, with optional discussion claims where they fit. Starting to construct these claims now, beginning with C430.

Defining the dose-response curve claim with the Cohen's d values showing monotonic increase from 0.482 to 0.639 as more L1 heads get ablated, with diminishing returns appearing around 12-16 heads. Then the corresponding discussion claim about how this monotonic progression supports a distributed routing mechanism. Moving into the counterfactual instruction manipulation claim next... Looking at the ablation results, removing L1 heads causes substantial token divergence at 72.3% and produces a meaningful effect size on action outputs with Cohen's d of 0.651 across all five tasks, confirming these heads have a direct causal impact downstream.

The control condition with non-instruction heads shows they produce less divergence overall—about 2.47 times smaller in token-level changes and 2.07 times smaller in action MSE—yet each individual non-instruction head has a stronger per-head effect, suggesting instruction routing heads are more specialized and efficient.

Instruction heads exhibit more coordinated perturbation patterns with lower coefficient of variation (1.30 vs 2.74) and stronger task-dependence, indicating they're more tightly integrated with the task structure.

The 50-demo ablation replicates the core finding: removing all 24 instruction heads increases R² from 0.557 to 0.615 (gain of 0.058), and compared to the 8-head control the improvement is 0.042, confirming the capacity trade-off isn't just an artifact of the limited 5-demo training regime.

Random 24-head subsets actually produce larger R² gains than the instruction-dominant heads (0.077 vs 0.042 mean improvement, z=-2.73, p=0.003), which is a striking result suggesting instruction heads may be particularly constraining the model's performance.

Looking at the permutation tests now—the CV difference between instruction and control heads is statistically significant (paired p=0.016, MC p=0.005), though the I² difference is only marginally significant (p=0.156).

Across three seeds, the trained model peaks at R²=0.643±0.014 in layer 9, outperforming both the base llama2 model at 0.634±0.013 in layer 12 and the untrained baseline at 0.547±0.008 in layer 1, with excellent consistency across seeds.

Now I'm updating the completeness metadata—adding these 13 new claims brings the total to 84, and I need to tally up the tier1 evidence entries across all of them, which looks like it's going to be around 16 tier1 entries total.

Actually, I realize the `check_provenance_completeness` tool will recalculate all these metrics automatically, so I should just add the claims to the YAML and let that tool handle the updates rather than manually computing the counts. I'll insert the new claims before the `figures:` section and update the last_checked timestamp.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "39b5178e-c02b-464f-88da-ad0c970668c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FMk4rDSk9QF5MCAbvn3r6f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 68044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 157_

Now I have all the information. I'll add 13 new tier1 claims for the 8 experiments, inserting before the `figures:` section. Let me also check if there's a `check_provenance_completeness` tool available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "895a0813-35b4-4be7-ad24-af0ebdad3275",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FMk4rDSk9QF5MCAbvn3r6f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 68044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 158_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VwcRr6RABFzeL9k7174fH9`</summary>

```json
{
  "query": "check_provenance completeness",
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
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "9322ea16-5b9c-448b-a32c-3e96ca03fc1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FMk4rDSk9QF5MCAbvn3r6f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 68044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 159 · 2026-05-18T17:46:53.898Z_

<details><summary>↩ Tool result · `toolu_01VwcRr6RABFzeL9k7174fH9`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "7dbf1e26-f9cf-42ab-8862-c6588b42d740",
  "tool_use_result": {
    "matches": [],
    "query": "check_provenance completeness",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Tool call

_source line 160_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01REf3izTNYpHwPE1b1HserX`</summary>

```json
{
  "query": "provenance",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "1060e923-070a-4931-bfbc-17571cfbda84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DD39sjmoHA2yCP6Mps6Hr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3372,
      "cache_read_input_tokens": 68648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3372
      },
      "output_tokens": 51,
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

_source line 161 · 2026-05-18T17:46:59.098Z_

<details><summary>↩ Tool result · `toolu_01REf3izTNYpHwPE1b1HserX`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
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
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "2c2fc7f4-7994-4fc2-bcd1-77d544e8a691",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "provenance",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Assistant

_source line 162_

<details><summary>Logged reasoning block</summary>

```text
There's no `check_provenance_completeness` tool available. I'll proceed with adding the claims and manually update the _completeness section. Let me construct the edit.

I need to insert 13 new claims before line 1747 (`figures:`). Let me write the YAML carefully, matching the existing format.

Let me do the insertion with the Edit tool. I'll replace the line `figures:` with the new claims + `figures:`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "d92fd271-ae02-45b9-8423-50875454c4f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxhakXnL9b9rBTtB2RMu4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 72020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 579
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

_source line 163_

No dedicated provenance check tool available. I'll add the 13 new claims and update `_completeness` manually. Let me insert them before the `figures:` section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "a540c33a-f5c8-4b2c-a8fb-d28d3229b0ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxhakXnL9b9rBTtB2RMu4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 72020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 579
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

_source line 164_

<details open><summary>🔧 Tool call — Edit · `toolu_012NyJb8Tb9bWZ7T9VBF8gpq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
  "old_string": "  decisions: []\n  deprecated: false\nfigures:",
  "new_string": "  decisions: []\n  deprecated: false\n- id: C430\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Dose-response curve: monotonic increase in action divergence (Cohen d 0.482\n    to 0.639) as L1 heads ablated from top-4 to top-32, diminishing returns at 12-16\n    heads'\n  type: quantitative\n  evidence:\n  - exp_id: dose_response_curve\n    metric: cohens_d_progression\n    value: 0.482 (top-4) to 0.639 (top-32)\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C431\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (4): monotonic dose-response supports distributed collective\n    routing mechanism'\n  type: mechanistic\n  evidence:\n  - exp_id: dose_response_curve\n    metric: monotonic_progression\n    value: confirmed, saturates at 12-16 heads\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C432\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Counterfactual instruction manipulation: graduated action divergence (empty\n    d=0.968, wrong d=0.844, paraphrased d=0.697, shuffled d=0.625)'\n  type: quantitative\n  evidence:\n  - exp_id: counterfactual_instruction\n    metric: cohens_d_by_condition\n    value: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C433\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (5): graduated instruction sensitivity confirms L1 heads\n    perform instruction-specific routing with surface-form dependency'\n  type: mechanistic\n  evidence:\n  - exp_id: counterfactual_instruction\n    metric: graduated_response_pattern\n    value: confirmed, paraphrased > shuffled indicates surface-form dependency\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C434\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'L1 head ablation action trajectory: 72.3% token divergence, action MSE Cohen\n    d=0.651 (p<0.001), all 5 tasks significant (d=0.433-0.729)'\n  type: quantitative\n  evidence:\n  - exp_id: action_trajectory_analysis\n    metric: token_divergence_rate\n    value: '0.723'\n    tier: tier1\n  - exp_id: action_trajectory_analysis\n    metric: paired_action_mse_cohens_d\n    value: '0.651'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C435\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (3): action output divergence demonstrates causal downstream\n    effect of instruction routing heads beyond intermediate representations'\n  type: mechanistic\n  evidence:\n  - exp_id: action_trajectory_analysis\n    metric: causal_action_effect\n    value: d=0.651, p<0.001, n=2500\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C436\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Control ablation: 8 non-instruction heads produce smaller divergence (MSE\n    ratio 2.07x, token div 2.47x) but stronger per-head effect (0.051 vs 0.027, p=0.0018)'\n  type: quantitative\n  evidence:\n  - exp_id: action_trajectory_control\n    metric: mse_ratio_instruction_vs_control\n    value: '2.07'\n    tier: tier1\n  - exp_id: action_trajectory_control\n    metric: per_head_effect\n    value: control 0.051 vs instruction 0.027, p=0.0018\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C437\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Instruction heads show qualitatively different perturbation: more temporally\n    coherent (CV 1.30 vs 2.74, permutation p=0.016) and more task-dependent (I2=0.87\n    vs 0.78)'\n  type: mechanistic\n  evidence:\n  - exp_id: action_trajectory_control\n    metric: temporal_coherence_CV\n    value: instruction 1.30 vs control 2.74\n    tier: tier1\n  - exp_id: permutation_test_I2\n    metric: CV_permutation_p\n    value: '0.016'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C438\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: '50-demo L1 ablation confirms R2 increase: baseline 0.557 to all-24 ablated\n    0.615 (Delta=0.058, p=0), vs control-8 Delta=0.042 (p=0)'\n  type: quantitative\n  evidence:\n  - exp_id: ablation_50demos_main\n    metric: all_24_vs_baseline_delta\n    value: '0.0585'\n    tier: tier1\n  - exp_id: ablation_50demos_main\n    metric: all_24_vs_control8_delta\n    value: '0.0421'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C439\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (2): full-data (50 demos) ablation confirms capacity\n    trade-off is not underfitting artifact from 5-demo version'\n  type: mechanistic\n  evidence:\n  - exp_id: ablation_50demos_main\n    metric: replication_with_adequate_data\n    value: Delta=0.058 p=0, consistent with 5-demo result\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C440\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Random 24-head subsets yield larger R2 increase than instruction-dominant\n    24 heads (mean Delta 0.077 vs 0.042, z=-2.73, p=0.003), supporting dual routing-encoding\n    function'\n  type: quantitative\n  evidence:\n  - exp_id: random_subset_ablation\n    metric: dominant_vs_random_z_score\n    value: '-2.73'\n    tier: tier1\n  - exp_id: random_subset_ablation\n    metric: random_mean_delta_r2\n    value: 0.077 +/- 0.013 (n=10 seeds)\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C441\n  location:\n    section: appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Permutation test: CV difference between instruction and control heads significant\n    (paired p=0.016, MC p=0.005), I2 difference marginal (p=0.156)'\n  type: quantitative\n  evidence:\n  - exp_id: permutation_test_I2\n    metric: CV_exact_paired_p\n    value: '0.0156'\n    tier: tier1\n  - exp_id: permutation_test_I2\n    metric: I2_exact_paired_p\n    value: '0.1562'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C442\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Multi-seed (n=3) three-condition R2: trained 0.643+/-0.014 (L9) > llama2base\n    0.634+/-0.013 (L12) > untrained 0.547+/-0.008 (L1), cross-seed consistency confirmed'\n  type: quantitative\n  evidence:\n  - exp_id: threecond_multiseed_r2_v2\n    metric: trained_peak_R2\n    value: 0.643 +/- 0.014 (L9)\n    tier: tier1\n  - exp_id: threecond_multiseed_r2_v2\n    metric: llama2base_peak_R2\n    value: 0.634 +/- 0.013 (L12)\n    tier: tier1\n  - exp_id: threecond_multiseed_r2_v2\n    metric: untrained_peak_R2\n    value: 0.547 +/- 0.008 (L1)\n    tier: tier1\n  decisions: []\n  deprecated: false\nfigures:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "079476fe-7c3a-4b28-954a-975450c28f6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxhakXnL9b9rBTtB2RMu4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 72020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 579
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

_source line 165 · 2026-05-18T17:47:25.947Z_

<details><summary>↩ Tool result · `toolu_012NyJb8Tb9bWZ7T9VBF8gpq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "f1e70e52-bec9-4512-b27a-db2ba9f2b4ce",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
    "oldString": "  decisions: []\n  deprecated: false\nfigures:",
    "newString": "  decisions: []\n  deprecated: false\n- id: C430\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Dose-response curve: monotonic increase in action divergence (Cohen d 0.482\n    to 0.639) as L1 heads ablated from top-4 to top-32, diminishing returns at 12-16\n    heads'\n  type: quantitative\n  evidence:\n  - exp_id: dose_response_curve\n    metric: cohens_d_progression\n    value: 0.482 (top-4) to 0.639 (top-32)\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C431\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (4): monotonic dose-response supports distributed collective\n    routing mechanism'\n  type: mechanistic\n  evidence:\n  - exp_id: dose_response_curve\n    metric: monotonic_progression\n    value: confirmed, saturates at 12-16 heads\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C432\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Counterfactual instruction manipulation: graduated action divergence (empty\n    d=0.968, wrong d=0.844, paraphrased d=0.697, shuffled d=0.625)'\n  type: quantitative\n  evidence:\n  - exp_id: counterfactual_instruction\n    metric: cohens_d_by_condition\n    value: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C433\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (5): graduated instruction sensitivity confirms L1 heads\n    perform instruction-specific routing with surface-form dependency'\n  type: mechanistic\n  evidence:\n  - exp_id: counterfactual_instruction\n    metric: graduated_response_pattern\n    value: confirmed, paraphrased > shuffled indicates surface-form dependency\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C434\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'L1 head ablation action trajectory: 72.3% token divergence, action MSE Cohen\n    d=0.651 (p<0.001), all 5 tasks significant (d=0.433-0.729)'\n  type: quantitative\n  evidence:\n  - exp_id: action_trajectory_analysis\n    metric: token_divergence_rate\n    value: '0.723'\n    tier: tier1\n  - exp_id: action_trajectory_analysis\n    metric: paired_action_mse_cohens_d\n    value: '0.651'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C435\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (3): action output divergence demonstrates causal downstream\n    effect of instruction routing heads beyond intermediate representations'\n  type: mechanistic\n  evidence:\n  - exp_id: action_trajectory_analysis\n    metric: causal_action_effect\n    value: d=0.651, p<0.001, n=2500\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C436\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Control ablation: 8 non-instruction heads produce smaller divergence (MSE\n    ratio 2.07x, token div 2.47x) but stronger per-head effect (0.051 vs 0.027, p=0.0018)'\n  type: quantitative\n  evidence:\n  - exp_id: action_trajectory_control\n    metric: mse_ratio_instruction_vs_control\n    value: '2.07'\n    tier: tier1\n  - exp_id: action_trajectory_control\n    metric: per_head_effect\n    value: control 0.051 vs instruction 0.027, p=0.0018\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C437\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Instruction heads show qualitatively different perturbation: more temporally\n    coherent (CV 1.30 vs 2.74, permutation p=0.016) and more task-dependent (I2=0.87\n    vs 0.78)'\n  type: mechanistic\n  evidence:\n  - exp_id: action_trajectory_control\n    metric: temporal_coherence_CV\n    value: instruction 1.30 vs control 2.74\n    tier: tier1\n  - exp_id: permutation_test_I2\n    metric: CV_permutation_p\n    value: '0.016'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C438\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: '50-demo L1 ablation confirms R2 increase: baseline 0.557 to all-24 ablated\n    0.615 (Delta=0.058, p=0), vs control-8 Delta=0.042 (p=0)'\n  type: quantitative\n  evidence:\n  - exp_id: ablation_50demos_main\n    metric: all_24_vs_baseline_delta\n    value: '0.0585'\n    tier: tier1\n  - exp_id: ablation_50demos_main\n    metric: all_24_vs_control8_delta\n    value: '0.0421'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C439\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (2): full-data (50 demos) ablation confirms capacity\n    trade-off is not underfitting artifact from 5-demo version'\n  type: mechanistic\n  evidence:\n  - exp_id: ablation_50demos_main\n    metric: replication_with_adequate_data\n    value: Delta=0.058 p=0, consistent with 5-demo result\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C440\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Random 24-head subsets yield larger R2 increase than instruction-dominant\n    24 heads (mean Delta 0.077 vs 0.042, z=-2.73, p=0.003), supporting dual routing-encoding\n    function'\n  type: quantitative\n  evidence:\n  - exp_id: random_subset_ablation\n    metric: dominant_vs_random_z_score\n    value: '-2.73'\n    tier: tier1\n  - exp_id: random_subset_ablation\n    metric: random_mean_delta_r2\n    value: 0.077 +/- 0.013 (n=10 seeds)\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C441\n  location:\n    section: appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Permutation test: CV difference between instruction and control heads significant\n    (paired p=0.016, MC p=0.005), I2 difference marginal (p=0.156)'\n  type: quantitative\n  evidence:\n  - exp_id: permutation_test_I2\n    metric: CV_exact_paired_p\n    value: '0.0156'\n    tier: tier1\n  - exp_id: permutation_test_I2\n    metric: I2_exact_paired_p\n    value: '0.1562'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C442\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Multi-seed (n=3) three-condition R2: trained 0.643+/-0.014 (L9) > llama2base\n    0.634+/-0.013 (L12) > untrained 0.547+/-0.008 (L1), cross-seed consistency confirmed'\n  type: quantitative\n  evidence:\n  - exp_id: threecond_multiseed_r2_v2\n    metric: trained_peak_R2\n    value: 0.643 +/- 0.014 (L9)\n    tier: tier1\n  - exp_id: threecond_multiseed_r2_v2\n    metric: llama2base_peak_R2\n    value: 0.634 +/- 0.013 (L12)\n    tier: tier1\n  - exp_id: threecond_multiseed_r2_v2\n    metric: untrained_peak_R2\n    value: 0.547 +/- 0.008 (L1)\n    tier: tier1\n  decisions: []\n  deprecated: false\nfigures:",
    "originalFile": "claims:\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915\n    tier: tier1\n  - exp_id: plan_013_branch_split\n    metric: post_projector_4096d_rsa=0.615\n    tier: tier1\n  - exp_id: d041_method_b_rsa\n    metric: baselines.clip_cls=0.557\n    tier: tier1\n  id: C001\n  location:\n    context: result_statement\n    section: abstract\n  text: 'First, self-supervised pretraining provides the strongest action-relevant\n    geometry: standalone DINOv2 achieves RSA $ = 0.692$, exceeding all VL-pretrained\n    encoders (DinoSigLIP+Projector $ = 0.615$; CL'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained_image_mean_peak.rsa=0.6282\n    tier: tier1\n  - exp_id: d041_method_b_rsa\n    metric: untrained_image_mean_peak.rsa=0.6117\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak.mean_R2=0.6779\n    tier: tier1\n  id: C002\n  location:\n    context: result_statement\n    section: abstract\n  text: 'Second, the LLM applies a non-monotonic transformation---the first 12 layers\n    enhance geometric alignment with the action space above the vision encoder input\n    ($$: $0.612  0.628$ at L12), while the rem'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017,significant=false\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686,p=0.0001\n    tier: tier1\n  id: C003\n  location:\n    context: result_statement\n    section: abstract\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\n    capacity (R^2 Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates\n  type: quantitative\n- deprecated: false\n  evidence: llama2base_action_probe experiment\n  id: C004\n  location:\n    context: result_statement\n    section: appendix\n  text: 'Linear CKA~kornblith2019 reverses the RSA ordering: untrained LLM ($CKA =\n    0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2\n    ($0.066$), partially inverting the self-superv'\n  type: quantitative\n  decisions: []\n- deprecated: false\n  evidence:\n  - exp_id: plan_009_cka_verification\n    metric: rdm_cka.*\n    tier: tier1\n  id: C005\n  location:\n    context: result_statement\n    section: appendix\n  text: 'RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $$\n    Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).'\n  type: quantitative\n- deprecated: false\n  evidence:\n  - exp_id: plan_009_cka_verification\n    metric: linear_cka per-layer (derived from full scan)\n    tier: tier2\n  id: C006\n  location:\n    context: result_statement\n    section: appendix\n  text: At the per-layer level, linear CKA between image\\_mean and the action space\n    rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U\n    pattern.\n  type: quantitative\n- deprecated: false\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.*\n    tier: tier1\n  - exp_id: plan_009_cka_verification\n    metric: linear_cka.* + rdm_cka.*\n    tier: tier1\n  id: C007\n  location:\n    context: result_statement\n    section: appendix\n  text: 'Three similarity metrics across representation sources. (a)~RSA ranks DINOv2\n    cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). (b)~Linear CKA reverses\n    the ordering: Untrained ($0.089$) $>$ Tr'\n  type: quantitative\n- deprecated: false\n  evidence:\n  - exp_id: plan_013_branch_split\n    metric: fused_2176d_rsa=0.634\n    tier: tier1\n  id: C008\n  location:\n    context: result_statement\n    section: appendix\n  text: Fusion produces a representation ($ = 0.634$) that exceeds either branch alone,\n    indicating that concatenation captures complementary structure.\n  type: quantitative\n- deprecated: false\n  evidence:\n  - exp_id: plan_013_branch_split\n    metric: fused_2176d_rsa=0.634, post_projector_4096d_rsa=0.615\n    tier: tier1\n  id: C009\n  location:\n    context: result_statement\n    section: appendix\n  text: 'The MLP projector then compresses this signal: DinoSigLIP+Projector achieves\n    $ = 0.615$, a drop of $ = 0.019$ from the fused 2{,176-D input.'\n  type: quantitative\n- deprecated: false\n  evidence:\n  - exp_id: plan_013_branch_split\n    metric: standalone_dino_patch_mean_rsa=0.631\n    tier: tier1\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_patch_mean=0.6307\n    tier: tier1\n  id: C010\n  location:\n    context: result_statement\n    section: appendix\n  text: DINOv2 patch\\_mean achieves RSA $ = 0.631$, between the cls\\_token ($0.692$)\n    and the fused DinoSigLIP ($0.634$).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915, trained_image_mean_peak\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak.mean_R2=0.6779\n    tier: tier1\n  id: C011\n  location:\n    context: result_statement\n    section: conclusion\n  text: 'Three findings emerge: (1)~the frozen vision encoder provides the dominant\n    action-relevant geometry, with self-supervised DINOv2 achieving the highest alignment\n    ($ = 0.692$) exceeding all VL-pretraine'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915\n    tier: tier1\n  id: C012\n  location:\n    context: result_statement\n    section: discussion\n  text: 'The vision encoder is the source: self-supervised DINOv2 achieves the highest\n    geometric alignment ($ = 0.692$), exceeding all VLA internal representations.'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.p=0.006\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686\n    tier: tier1\n  id: C013\n  location:\n    context: result_statement\n    section: discussion\n  text: 'Training redistributes geometry but enhances decodability: modest geometric\n    gain (Delta = 0.017--0.023, 3--4% of baseline across two benchmarks), while substantially\n    improving R^2 (Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.significant=false\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  id: C014\n  location:\n    context: result_statement\n    section: discussion\n  text: Cross-benchmark replication (LIBERO-Spatial Delta = 0.023, p < 0.001) suggests\n    the LIBERO-Goal RSA CI (incl. zero) reflects limited power rather than a true\n    null, but the effect remains small (3--4% of baseline).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915\n    tier: tier1\n  - exp_id: plan_013_branch_split\n    metric: fused_2176d_rsa=0.634, standalone_dino_patch_mean_rsa=0.631\n    tier: tier1\n  id: C015\n  location:\n    context: result_statement\n    section: experiments\n  text: The standalone DINOv2 cls\\_token achieves the highest alignment of any representation\n    source ($ = 0.692$), followed by the fused DinoSigLIP 2{,176-D representation\n    before projection ($ = 0.634$) and t\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.clip_cls=0.557\n    tier: tier1\n  id: C016\n  location:\n    context: result_statement\n    section: experiments\n  text: CLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment\n    among pretrained encoders ($ = 0.557$; Figure~fig:rsa_bar).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557, trained_image_mean_peak.rsa=0.6282\n    tier: tier1\n  id: C017\n  location:\n    context: result_statement\n    section: experiments\n  text: DINOv2, pretrained with self-supervised objectives alone, achieves $ = 0.692$---exceeding\n    not only CLIP ($ = 0.557$) but also the VLA's own internal representations at\n    their peaks (trained image\\_mean\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_012_clip_vit_control\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\n    tier: tier1\n  - exp_id: unified_action_probe\n    metric: bootstrap_pairwise.projector_vs_dino.p=0.557\n    tier: tier1\n  id: C018\n  location:\n    context: result_statement\n    section: experiments\n  text: 'Functional probes corroborate the ranking: DINOv2 cls\\_token achieves $R^2\n    = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$,\n    $p = 0.557$, n.s.), while CLIP yields the'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_013_branch_split\n    metric: dinov2_branch_rsa=0.619, siglip_branch_rsa=0.621\n    tier: tier1\n  id: C019\n  location:\n    context: result_statement\n    section: experiments\n  text: The DINOv2 (1{,024-D) and SigLIP (1{,152-D) branches yield near-identical\n    RSA ($0.619$ vs.\\ $0.621$); fusion exceeds either ($0.634$), while the projector\n    introduces modest compression loss ($0.634  0\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: all RSA values\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: all R2 peak values\n    tier: tier1\n  id: C020\n  location:\n    context: result_statement\n    section: experiments\n  text: Geometric (RSA $$) and functional (probe $R^2$) alignment with the action\n    space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both trained\n    readout and image\\_mean exceed the projector in\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines + trained_image_mean_peak\n    tier: tier1\n  id: C021\n  location:\n    context: result_statement\n    section: experiments\n  text: 'RSA with the action space ($$) across representation sources. Self-supervised\n    DINOv2 cls\\_token ($=0.692$) achieves the highest geometric alignment, followed\n    by fused DinoSigLIP ($0.634$) and the VLA '\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained_image_mean per-layer RSA (L0=0.612, L12=0.628, L32=0.422)\n    tier: tier1\n  id: C022\n  location:\n    context: result_statement\n    section: experiments\n  text: 'Figure~fig:layer_curves reveals a non-monotonic trajectory for trained image\\_mean\n    RSA: $$ begins at $0.612$ (L0, equal to the projector input), rises to a peak\n    of $0.628$ at L12---above the DinoSigLI'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_image_mean_peak.layer=8, mean_R2=0.6553\n    tier: tier1\n  - exp_id: plan_012_clip_vit_control\n    metric: projector_mean_R2=0.6298\n    tier: tier1\n  id: C023\n  location:\n    context: result_statement\n    section: experiments\n  text: Full-layer probe scans reveal that trained image\\_mean $R^2$ peaks at L8 ($0.655$),\n    exceeding the projector ($0.630$, $ = +0.025$; Table~tab:rsa_overview).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_image_mean_peak.layer=8\n    tier: tier1\n  - exp_id: d041_method_b_rsa\n    metric: trained_image_mean_peak.layer=12\n    tier: tier1\n  id: C024\n  location:\n    context: result_statement\n    section: experiments\n  text: The $R^2$ peak (L8) precedes the RSA peak (L12) by four layers, suggesting\n    that functional decodability peaks earlier than geometric alignment; we adopt\n    ``early-to-middle layers (L8--L13)'' to capture\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained_last_preaction_peak.rsa=0.6425, layer=12\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak.mean_R2=0.6779, layer=13\n    tier: tier1\n  id: C025\n  location:\n    context: result_statement\n    section: experiments\n  text: Trained readout achieves peak RSA $ = 0.643$ at L12 and probe $R^2 = 0.678$\n    (L13), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $ = 0.048$; Table~tab:rsa_overview,\n    Figure~fig:probe_bars).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained per-layer RSA L12=0.628→L32=0.422; untrained 0.612→0.545\n    tier: tier1\n  id: C026\n  location:\n    context: result_statement\n    section: experiments\n  text: 'The decline from L12 to L32 ($$: $0.628  0.422$) exceeds the untrained decay\n    ($0.612  0.545$), indicating that training actively redirects later layers away\n    from action geometry, yielding a three-phas'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak=0.6779, trained_image_mean_peak=0.6553\n    tier: tier1\n  - exp_id: plan_012_clip_vit_control\n    metric: projector_mean_R2=0.6298, dino_cls_mean_R2=0.6343\n    tier: tier1\n  id: C027\n  location:\n    context: result_statement\n    section: experiments\n  text: Functional probe $R^2$ for action prediction (best layer for each source).\n    Both trained readout ($R^2{=0.678$, L13) and trained image\\_mean ($0.655$, L8)\n    exceed the projector baseline ($0.630$), confi\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  id: C028\n  location:\n    context: result_statement\n    section: experiments\n  text: best-vs-best Delta = +0.017 (3% of baseline; LIBERO-Spatial confirms with\n    Delta = +0.023, 4%, p < 0.001). This geometric gain is far smaller than the functional\n    improvement.\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\n    tier: tier1\n  id: C029\n  location:\n    context: result_statement\n    section: experiments\n  text: RSA best-vs-best yields at most a modest gain (Delta = 0.017--0.023, 3--4%\n    of baseline across two benchmarks), while R^2 shows substantially larger improvements.\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006; last_preaction.delta=0.0686,p=0.0001\n    tier: tier1\n  id: C030\n  location:\n    context: result_statement\n    section: experiments\n  text: Yet $R^2$ best-vs-best is significant for both image\\_mean ($ = +0.015$, $p\n    = 0.006$) and readout ($ = +0.069$, $p < 0.0001$; Table~tab:training_effects).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_same_layer.last_preaction_L13.note (untrained L13 R2 near -0.33)\n    tier: tier1\n  id: C031\n  location:\n    context: result_statement\n    section: experiments\n  text: Untrained readout $R^2$ reaches $ -0.33$ at L12--L29 (predictions worse than\n    a constant-mean baseline), while untrained image\\_mean $R^2$ drops to near-zero\n    at L10--L13.\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best + same_layer\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best\n    tier: tier1\n  id: C032\n  location:\n    context: result_statement\n    section: experiments\n  text: 'Training effects on action-relevant structure (LIBERO-Goal; bootstrap). RSA\n    best-vs-best yields modest geometric gain (Delta=+0.017, 3%; LIBERO-Spatial: +0.023,\n    p<0.001), while R^2 shows substantially larger functional gains.'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: instruction_effect (derived from trained_with_inst vs trained_no_inst)\n    tier: tier1\n  - exp_id: plan_008_random_inst_control\n    metric: max_absolute_delta=0.0165, instruction_invariant=true\n    tier: tier1\n  id: C033\n  location:\n    context: finding_statement\n    section: experiments\n  text: This confirms that the action geometry is visually grounded and instruction-independent~grant2026.\n  type: methodological\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: experimental design (2x2 factorial)\n    tier: tier2\n  id: C034\n  location:\n    context: result_statement\n    section: introduction\n  text: We cross training status (trained vs.\\ untrained, reinitializing 6.74B LLM\n    parameters) with instruction presence in a $2 2$ factorial design, and quantify\n    action-relevant structure using RSA~kriegesko\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557\n    tier: tier1\n  id: C035\n  location:\n    context: result_statement\n    section: introduction\n  text: Standalone DINOv2 achieves the highest action-space alignment (RSA $ = 0.692$),\n    far exceeding CLIP ($ = 0.557$) and the VLA's own peak internal representation\n    ($ = 0.628$ at L12).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_012_clip_vit_control\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\n    tier: tier1\n  id: C036\n  location:\n    context: result_statement\n    section: introduction\n  text: 'Functional probes corroborate this ranking: DINOv2 ($R^2 = 0.634$) $$ Projector\n    ($0.630$) $>$ CLIP ($0.587$).'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained_image_mean_peak.rsa=0.6282\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak.mean_R2=0.6779\n    tier: tier1\n  id: C037\n  location:\n    context: result_statement\n    section: introduction\n  text: 'Second, the LLM applies a non-monotonic transformation: the first 12 layers\n    enhance geometric alignment above the vision encoder input ($$: $0.612  0.628$),\n    while the remaining 20 layers degrade it ($'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_013_branch_split\n    metric: methodology (encoder extraction)\n    tier: tier2\n  id: C038\n  location:\n    context: bold\n    section: method\n  text: DINOv2 ViT-L/14\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_012_clip_vit_control\n    metric: methodology (CLIP extraction)\n    tier: tier2\n  id: C039\n  location:\n    context: bold\n    section: method\n  text: CLIP ViT-L/14\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\n    tier: tier1\n  id: C040\n  location:\n    context: result_statement\n    section: introduction\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\n    capacity---redistribution dominates over creation.\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_010_libero_spatial\n    metric: rsa.trained_image_mean_peak(layer=14,rsa=0.691), action_probe.trained_image_mean_peak(layer=13,R2=0.696)\n    tier: tier1\n  id: C041\n  location:\n    context: result_statement\n    section: experiments\n  text: 'Cross-benchmark validation (LIBERO-Spatial): inverted-U replicates, trained\n    image_mean RSA peaks at L14 (rho=0.691), R^2 at L13 (0.696), peak shifting ~2\n    layers deeper than LIBERO-Goal.'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,ci_95=[0.012,0.036],p=0.001\n    tier: tier1\n  id: C042\n  location:\n    context: result_statement\n    section: experiments\n  text: Training produces a significant geometric gain on LIBERO-Spatial (best-vs-best\n    Delta=+0.023, p<0.001), confirming LIBERO-Goal effect reflects limited power.\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_010_libero_spatial\n    metric: rsa.trained_last_preaction_peak(layer=15), action_probe.trained_last_preaction_peak(layer=21)\n    tier: tier1\n  id: C043\n  location:\n    context: result_statement\n    section: experiments\n  text: RSA--R^2 peak convergence does not replicate on LIBERO-Spatial (RSA L15 vs\n    R^2 L21, 6-layer gap vs 1 on Goal), suggesting peak alignment may be benchmark-specific.\n  type: quantitative\n- id: C044\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: Image tokens encode purely visual information (instruction classification\n    at chance, 10%, across all layers)\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: image_mean_accuracy\n    value: 10%\n  decisions: []\n  deprecated: true\n- id: C046\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: 'Readout token: 100% instruction classification from L1, LOOCV-verified'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: readout_accuracy\n    value: 100%\n  - exp_id: loocv_validation\n    metric: accuracy\n    value: 100% ± 0.00\n  decisions: []\n  deprecated: true\n- id: C049\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: 25/32 attention heads flip to instruction-dominant (58% attention to ~8% of\n    sequence)\n  type: quantitative\n  evidence:\n  - exp_id: l1_attention_pattern\n    metric: instruction_dominant_heads\n    value: 25/32\n  - exp_id: l1_attention_pattern\n    metric: instruction_attention_fraction\n    value: 58%\n  decisions: []\n  deprecated: true\n- id: C053\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: Untrained incidental routing decays to 82%\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: untrained_L31_accuracy\n    value: 82%\n  decisions: []\n  deprecated: true\n- id: C058\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: RSA peaks at L12, probe R² peaks at L8-L13\n  type: quantitative\n  evidence:\n  - exp_id: rsa_per_layer\n    metric: trained_image_mean_peak\n    value: L12, rho=0.628\n  decisions: []\n  deprecated: true\n- id: C064\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 highest geometric foundation (rho=0.692)\n  type: quantitative\n  evidence:\n  - exp_id: rsa_encoder_comparison\n    metric: dinov2_cls_rsa\n    value: '0.692'\n  decisions: []\n  deprecated: true\n- id: C071\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: Training reshapes readout-token integration (routing +18pp, attention +46pp)\n    rather than visual representations (Delta <= 1.7%)\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_summary\n    metric: routing_delta\n    value: +18pp\n  - exp_id: training_effect_summary\n    metric: attention_delta\n    value: +46pp\n  - exp_id: training_effect_summary\n    metric: image_mean_rsa_delta\n    value: '+0.017'\n  decisions: []\n  deprecated: true\n- id: C072\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 'Image tokens: instruction classification at chance (10%) across all 32 layers'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: image_mean_accuracy\n    value: 10%\n  decisions: []\n  deprecated: true\n- id: C074\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 'Readout token: 100% instruction identity from L1, LOOCV-verified'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: readout_accuracy\n    value: 100%\n  - exp_id: loocv_validation\n    metric: accuracy\n    value: 100%\n  decisions: []\n  deprecated: true\n- id: C077\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 25/32 heads flip to instruction-dominant (58% attention)\n  type: quantitative\n  evidence:\n  - exp_id: l1_attention_pattern\n    metric: instruction_dominant_heads\n    value: 25/32\n  decisions: []\n  deprecated: true\n- id: C081\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: Untrained routing decays to 82% by L31\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: untrained_L31_accuracy\n    value: 82%\n  decisions: []\n  deprecated: true\n- id: C086\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 RSA rho=0.692\n  type: quantitative\n  evidence:\n  - exp_id: rsa_encoder_comparison\n    metric: dinov2_cls_rsa\n    value: '0.692'\n  decisions: []\n  deprecated: true\n- id: C092\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: Inverted-U peak rho=0.628 at L12, 0.422 at L32\n  type: quantitative\n  evidence:\n  - exp_id: rsa_per_layer\n    metric: trained_image_mean_L12\n    value: '0.628'\n  - exp_id: rsa_per_layer\n    metric: trained_image_mean_L32\n    value: '0.422'\n  decisions: []\n  deprecated: true\n- id: C099\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: Training geometric gain Delta=0.017-0.023, 3-4%\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_comparison\n    metric: rsa_best_vs_best\n    value: +0.017 (Goal), +0.023 (Spatial)\n  decisions: []\n  deprecated: true\n- id: C107\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: Readout R2 Delta=+0.069, p<0.0001\n  type: quantitative\n  evidence:\n  - exp_id: probe_comparison\n    metric: readout_r2_delta\n    value: '+0.069'\n  decisions: []\n  deprecated: true\n- id: C108\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: Image_mean instruction classification at chance (10%) across all 32 layers\n  type: quantitative\n  evidence: 50-demo L1 ablation multi-layer comparison\n  decisions: []\n  deprecated: false\n- id: C110\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: Trained readout 100% L1-L31, LOOCV 100% +/- 0.00\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: readout_accuracy\n    value: 100%\n  - exp_id: loocv_validation\n    metric: accuracy\n    value: 100%\n  decisions: []\n  deprecated: false\n- id: C113\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Untrained readout decays: L8 95.5%, L31 82%'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: untrained_L8\n    value: 95.5%\n  - exp_id: cross_instruction_probe\n    metric: untrained_L31\n    value: 82%\n  decisions: []\n  deprecated: false\n- id: C117\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Instruction invariance: max |Delta| = 0.006'\n  type: quantitative\n  evidence:\n  - exp_id: factorial_analysis\n    metric: instruction_effect\n    value: '0.006'\n  decisions: []\n  deprecated: false\n- id: C122\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'QA probe: trained 86.3% (L20), DINOv2 82.7%'\n  type: quantitative\n  evidence:\n  - exp_id: qa_probe\n    metric: trained_accuracy\n    value: 86.3%\n  - exp_id: qa_probe\n    metric: dinov2_accuracy\n    value: 82.7%\n  decisions: []\n  deprecated: false\n- id: C128\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Trained L1: 25/32 heads instruction-dominant, 58% attention to instruction,\n    20.9% to image'\n  type: quantitative\n  evidence:\n  - exp_id: l1_attention_pattern\n    metric: instruction_dominant_heads\n    value: 25/32\n  - exp_id: l1_attention_pattern\n    metric: instruction_attention\n    value: 58%\n  - exp_id: l1_attention_pattern\n    metric: image_attention\n    value: 20.9%\n  decisions: []\n  deprecated: false\n- id: C135\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Untrained L1: 0/32 heads instruction-dominant, 87.8% image, 11.7% instruction'\n  type: quantitative\n  evidence:\n  - exp_id: l1_attention_pattern\n    metric: untrained_heads\n    value: 0/32\n  - exp_id: l1_attention_pattern\n    metric: untrained_image_attention\n    value: 87.8%\n  decisions: []\n  deprecated: false\n- id: C143\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Training effect asymmetry: attention +46pp, routing +18pp, R2 +0.069, but\n    image_mean Delta<=1.7%'\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_summary\n  decisions: []\n  deprecated: false\n- id: C152\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 cls RSA rho=0.692, highest alignment\n  type: quantitative\n  evidence:\n  - exp_id: rsa_encoder_comparison\n    metric: dinov2_cls\n    value: '0.692'\n  decisions: []\n  deprecated: false\n- id: C162\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: CLIP RSA rho=0.557\n  type: quantitative\n  evidence:\n  - exp_id: rsa_encoder_comparison\n    metric: clip_patch_mean\n    value: '0.557'\n  decisions: []\n  deprecated: false\n- id: C173\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Inverted-U: L0=0.612, L12=0.628, L32=0.422'\n  type: quantitative\n  evidence:\n  - exp_id: rsa_per_layer\n    metric: trained_image_mean\n    value: L0=0.612, L12=0.628, L32=0.422\n  decisions: []\n  deprecated: false\n- id: C185\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: R2 peak L8-L10 (0.655 +/- 0.002)\n  type: quantitative\n  evidence:\n  - exp_id: probe_per_layer\n    metric: trained_image_mean_peak\n    value: '0.655'\n  decisions: []\n  deprecated: false\n- id: C198\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: Readout R2=0.678 (L13), exceeds projector by 0.048\n  type: quantitative\n  evidence:\n  - exp_id: probe_comparison\n    metric: readout_r2\n    value: '0.678'\n  decisions: []\n  deprecated: false\n- id: C212\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: RSA best-vs-best Delta=+0.017, same-layer +0.079\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_comparison\n    metric: rsa_best_vs_best\n    value: '+0.017'\n  - exp_id: training_effect_comparison\n    metric: same_layer_L12\n    value: '+0.079'\n  decisions: []\n  deprecated: false\n- id: C227\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'R2 best-vs-best: image_mean +0.015 (p=0.006), readout +0.069 (p<0.0001)'\n  type: quantitative\n  evidence:\n  - exp_id: probe_comparison\n    metric: image_mean_delta\n    value: '+0.015'\n  - exp_id: probe_comparison\n    metric: readout_delta\n    value: '+0.069'\n  decisions: []\n  deprecated: false\n- id: C243\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Untrained pathological: L10-L11 R2=-0.33, -0.28'\n  type: quantitative\n  evidence:\n  - exp_id: probe_per_layer\n    metric: untrained_L10_L11\n    value: -0.33, -0.28\n  decisions: []\n  deprecated: false\n- id: C260\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'LIBERO-Spatial: RSA peak L14 (0.691), R2 peak L13 (0.696), Delta=+0.023 p<0.001'\n  type: quantitative\n  evidence:\n  - exp_id: libero_spatial\n    metric: rsa_peak\n    value: L14, 0.691\n  - exp_id: libero_spatial\n    metric: r2_peak\n    value: L13, 0.696\n  - exp_id: libero_spatial\n    metric: training_delta\n    value: '+0.023'\n  decisions: []\n  deprecated: false\n- id: C278\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Robustness: RSA profile r=0.970 under halved demos'\n  type: quantitative\n  evidence:\n  - exp_id: demo_sensitivity\n    metric: rsa_profile_correlation\n    value: '0.970'\n  decisions: []\n  deprecated: false\n- id: C279\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Training effects: routing +18pp, attention +46pp, R2 +0.069; image_mean Delta<=1.7%'\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_summary\n  decisions: []\n  deprecated: true\n- id: C281\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: Instruction invariance |Delta| < 0.006\n  type: quantitative\n  evidence:\n  - exp_id: factorial_analysis\n    metric: instruction_effect\n    value: '0.006'\n  decisions: []\n  deprecated: true\n- id: C284\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: LIBERO-Spatial Delta=0.023, p<0.001\n  type: quantitative\n  evidence:\n  - exp_id: libero_spatial\n    metric: training_delta\n    value: '+0.023'\n  decisions: []\n  deprecated: true\n- id: C285\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: 'Image tokens: instruction classification at chance across all layers'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n  decisions: []\n  deprecated: false\n- id: C287\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: 'Readout token: 100% from L1, LOOCV-verified'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n  - exp_id: loocv_validation\n  decisions: []\n  deprecated: false\n- id: C290\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: 25/32 heads flip to instruction-dominant (58%)\n  type: quantitative\n  evidence:\n  - exp_id: l1_attention_pattern\n  decisions: []\n  deprecated: false\n- id: C294\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: Untrained decays to 82%\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: untrained_L31\n    value: 82%\n  decisions: []\n  deprecated: false\n- id: C299\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: RSA inverted-U peak L12, R2 L8-L13, DINOv2 rho=0.692\n  type: quantitative\n  evidence:\n  - exp_id: rsa_per_layer\n  - exp_id: rsa_encoder_comparison\n  decisions: []\n  deprecated: false\n- id: C305\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: 'Training: R2 +0.069 readout, Delta<=1.7% image_mean'\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_summary\n  decisions: []\n  deprecated: false\n- id: C306\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: image tokens instruction-blind at chance 10% across all layers and conditions\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: accuracy\n    value: 10%\n  decisions:\n  - 'D060: reframed as architecture-expected verification'\n  deprecated: false\n- id: C308\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: readout token 100% instruction classification from L1, cross-validated\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe_loocv\n    metric: accuracy\n    value: 100%\n  decisions: []\n  deprecated: false\n- id: C311\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: 'VLA training shifts to entry-layer routing L0-L1: 21-25 heads with exit-layer\n    L31: 18 heads'\n  type: quantitative\n  evidence:\n  - exp_id: attention_analysis\n    metric: instruction_dominant_heads\n    value: 25/32 at L1, 18/32 at L31\n  decisions:\n  - 'D060: C2 anchor claim'\n  deprecated: false\n- id: C315\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: immediate instruction access 99.6% at L1 vs pretrained 80.2%\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: L1_accuracy\n    value: 99.6% vs 80.2%\n  decisions: []\n  deprecated: false\n- id: C320\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: under RSA peak rho=0.628 at L12 declining to 0.422 at L32\n  type: quantitative\n  evidence:\n  - exp_id: rsa_layer_profile\n    metric: spearman_rho\n    value: 0.628 L12, 0.422 L32\n  decisions:\n  - 'D060: qualified with under RSA'\n  deprecated: false\n- id: C326\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 highest geometric alignment rho=0.692, metric-dependent\n  type: quantitative\n  evidence:\n  - exp_id: rsa_cross_encoder\n    metric: spearman_rho\n    value: '0.692'\n  decisions:\n  - 'D060: added metric-dependence caveat'\n  deprecated: false\n- id: C333\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: training effect Delta rho <= 0.017 non-significant\n  type: quantitative\n  evidence:\n  - exp_id: rsa_training_effect\n    metric: delta_rho\n    value: '0.017'\n  decisions:\n  - 'D060: marked non-significant'\n  deprecated: false\n- id: C341\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: readout token probe R2 +0.069, instruction attention +46pp\n  type: quantitative\n  evidence:\n  - exp_id: probe_training_effect\n    metric: delta_R2\n    value: '+0.069'\n  - exp_id: attention_analysis\n    metric: delta_text_attention\n    value: +46pp\n  decisions: []\n  deprecated: false\n- id: C342\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: image tokens instruction-blind 10% across all 32 layers, architecture-expected\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: accuracy\n    value: 10%\n  decisions:\n  - 'D060: reframed as architecture-expected'\n  deprecated: false\n- id: C344\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: readout token 100% cross-validated from L1\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe_loocv\n    metric: accuracy\n    value: 100%\n  decisions: []\n  deprecated: false\n- id: C347\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 'VLA training shifts to entry-exit pattern L0-L1: 21-25 heads, L31: 18 heads'\n  type: quantitative\n  evidence:\n  - exp_id: attention_analysis\n    metric: instruction_dominant_heads\n  decisions:\n  - 'D060: C2 anchor'\n  deprecated: false\n- id: C351\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 99.6% at L1 vs pretrained 80.2%\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: L1_accuracy\n  decisions: []\n  deprecated: false\n- id: C356\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: under RSA alignment peaks L12 rho=0.628, declines to 0.422 at L32\n  type: quantitative\n  evidence:\n  - exp_id: rsa_layer_profile\n    metric: spearman_rho\n  decisions:\n  - 'D060: qualified under RSA'\n  deprecated: false\n- id: C362\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 highest geometric alignment rho=0.692, ordering partially reverses\n    under CKA\n  type: quantitative\n  evidence:\n  - exp_id: rsa_cross_encoder\n    metric: spearman_rho\n    value: '0.692'\n  decisions:\n  - 'D060: CKA caveat added'\n  deprecated: false\n- id: C369\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: non-significant geometric gain Delta rho=0.017 3%\n  type: quantitative\n  evidence:\n  - exp_id: rsa_training_effect\n    metric: delta_rho\n    value: '0.017'\n  decisions:\n  - 'D060: marked non-significant'\n  deprecated: false\n- id: C377\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: readout R2 Delta=+0.069 p<0.0001\n  type: quantitative\n  evidence:\n  - exp_id: probe_training_effect\n    metric: delta_R2\n    value: '+0.069'\n  decisions: []\n  deprecated: false\n- id: C378\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: image token instruction-blindness consistent with causal mask and frozen encoder\n  type: mechanistic\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: accuracy\n    value: 10%\n  decisions:\n  - 'D060: acknowledge causal mask as structural source'\n  deprecated: false\n- id: C379\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 highest RSA alignment 0.692, metric-dependent ordering\n  type: quantitative\n  evidence:\n  - exp_id: rsa_cross_encoder\n    metric: spearman_rho\n    value: '0.692'\n  decisions:\n  - 'D060: added under RSA qualifier and CKA metric-dependence caveat'\n  deprecated: false\n- id: C380\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: best-vs-best RSA gain non-significant Delta=+0.017 3% CI includes zero\n  type: quantitative\n  evidence:\n  - exp_id: rsa_training_effect\n    metric: delta_rho_best_vs_best\n    value: '+0.017'\n  decisions:\n  - 'D060: marked non-significant, CI includes zero'\n  deprecated: false\n- id: C381\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: image tokens instruction-blind consistent with causal mask and frozen encoder\n  type: mechanistic\n  evidence: 50-demo L1 ablation control\n  decisions:\n  - 'D060: architecture-expected framing'\n  deprecated: false\n- id: C383\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: training effects concentrated at readout R2 +0.069\n  type: quantitative\n  evidence:\n  - exp_id: probe_training_effect\n    metric: delta_R2\n    value: '+0.069'\n  decisions: []\n  deprecated: false\n- id: C386\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 highest RSA rho=0.692 under RSA\n  type: quantitative\n  evidence:\n  - exp_id: rsa_cross_encoder\n    metric: spearman_rho\n    value: '0.692'\n  decisions:\n  - 'D060: qualified under RSA'\n  deprecated: false\n- id: C390\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: VLA readout R2=0.678 vs DINOv2 0.634\n  type: quantitative\n  evidence:\n  - exp_id: probe_comparison\n    metric: R2\n  decisions: []\n  deprecated: false\n- id: C395\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: ablation R2 +46% p<0.0001 deep layers unaffected\n  type: quantitative\n  evidence:\n  - exp_id: l1_ablation\n    metric: delta_R2\n  decisions: []\n  deprecated: false\n- id: C401\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: encoder ranking reverses under CKA, metric-dependent\n  type: qualitative\n  evidence:\n  - exp_id: cka_comparison\n  decisions:\n  - 'D060: CKA divergence in main text'\n  deprecated: false\n- id: C408\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: frozen encoder confound acknowledged\n  type: qualitative\n  evidence: []\n  decisions:\n  - 'D060: added frozen encoder caveat'\n  deprecated: false\n- id: C416\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: L1 ablation 5 demos per task, full-scale replication in progress\n  type: qualitative\n  evidence: []\n  decisions:\n  - 'D060: acknowledged ablation scale limitation'\n  deprecated: false\n- id: C417\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: functional probes R2 peak L8-L13 metric-independent non-monotonic trajectory\n  type: quantitative\n  evidence:\n  - exp_id: probe_layer_profile\n    metric: R2\n    value: 0.655-0.678 at L8-L13\n  decisions:\n  - 'D060-C3-fix: R2 as primary metric-independent evidence'\n  deprecated: false\n- id: C418\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: RSA per-layer profile and encoder rankings metric-dependent, CKA monotonically\n    increasing\n  type: qualitative\n  evidence:\n  - exp_id: cka_comparison\n  decisions:\n  - 'D060-C3-fix: decline phase also RSA-specific, CKA monotonic'\n  deprecated: false\n- id: C419\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: functional probes peak L8-L13 R2=0.655-0.678 metric-independent\n  type: quantitative\n  evidence:\n  - exp_id: probe_layer_profile\n    metric: R2\n  decisions:\n  - 'D060-C3-fix: R2 as primary'\n  deprecated: false\n- id: C420\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: CKA monotonically increasing layer profiles\n  type: qualitative\n  evidence:\n  - exp_id: cka_layer_profile\n  decisions:\n  - 'D060-C3-fix: decline also RSA-specific'\n  deprecated: false\n- id: C421\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 'C3 contribution: non-monotonic transformation, R2 confirmed, RSA confirms\n    but CKA diverges'\n  type: qualitative\n  evidence:\n  - exp_id: probe_layer_profile\n  - exp_id: rsa_layer_profile\n  - exp_id: cka_layer_profile\n  decisions:\n  - 'D060-C3-fix: balanced metric framing'\n  deprecated: false\n- id: C422\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: encoder rankings and per-layer profiles metric-dependent, R2 inverted-U metric-independent\n  type: qualitative\n  evidence:\n  - exp_id: cka_comparison\n  - exp_id: probe_layer_profile\n  decisions:\n  - 'D060-C3-fix: CKA divergence covers both rankings and profiles'\n  deprecated: false\n- id: C423\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: trained image_mean RSA stable L0-L12 Delta=+0.017 n.s., decline L12-L32 Delta=-0.206\n    p<0.0001\n  type: quantitative\n  evidence:\n  - exp_id: rsa_layer_profile\n    metric: spearman_rho\n  decisions:\n  - 'D060-C3-fix: rise phase reframed as stable'\n  deprecated: false\n- id: C424\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: untrained RSA declines monotonically from L0 Delta=-0.062 to L12 p<0.0001\n  type: quantitative\n  evidence:\n  - exp_id: rsa_layer_profile_untrained\n    metric: spearman_rho\n  decisions: []\n  deprecated: false\n- id: C425\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: marginal RSA change at image_mean +0.017 n.s. contrasts with readout +0.074\n    p<0.0001\n  type: quantitative\n  evidence:\n  - exp_id: rsa_layer_profile\n    metric: delta_rho_readout\n  decisions:\n  - 'D060-C3-fix: readout contrast added'\n  deprecated: false\n- id: C426\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: N=63728 observations, N/params ratio approx 0.05 for MLP probe\n  type: quantitative\n  evidence:\n  - exp_id: dataset_stats\n    metric: N_observations\n    value: '63728'\n  decisions: []\n  deprecated: false\n- id: C427\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: Probe R2 trained vs untrained FDR significant at 29-30/33 layers both positions\n  type: quantitative\n  evidence:\n  - exp_id: fdr_correction\n    metric: significant_layers_R2\n    value: 29-30/33\n  decisions: []\n  deprecated: false\n- id: C428\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: RSA FDR significant at 25/33 layers image_mean, 0/33 last_preaction due to\n    n=10 power ceiling\n  type: quantitative\n  evidence:\n  - exp_id: fdr_correction\n    metric: significant_layers_RSA\n    value: 25/33 image_mean, 0/33 readout\n  decisions: []\n  deprecated: false\n- id: C429\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: non-monotonic profile stable under 25-demo subsampling, RSA peak unchanged\n    L12, profile r=0.97\n  type: quantitative\n  evidence:\n  - exp_id: ablation_p2_demo_sensitivity\n    metric: profile_correlation_RSA\n    value: '0.970'\n  decisions: []\n  deprecated: false\nfigures:\n- caption: Three similarity metrics across representation sources. \\textbf{(a)\n  deprecated: false\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines (RSA values)\n    tier: tier1\n  - exp_id: plan_009_cka_verification\n    metric: linear_cka + rdm_cka\n    tier: tier1\n  id: F001\n  label: fig:metric_comparison\n  location:\n    section: appendix\n  source_path: figures/fig6.pdf\n  type: result\n- caption: RSA with the action space ($\\rho$) across representation sources. Self-supervised\n    DINOv2 \\texttt{cls\\_token\n  deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines + trained/untrained peaks\n    tier: tier1\n  - exp_id: plan_013_branch_split\n    metric: fused_2176d_rsa=0.634\n    tier: tier1\n  id: F002\n  label: fig:rsa_bar\n  location:\n    section: experiments\n  source_path: figures/fig2.pdf\n  type: result\n- caption: 'Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers.\n    Trained image\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\to$ L12 $=\n    0.628$ (peak, above Projector $0.615$) $\\to$ L32 $= 0.422$. Untrained image\\_mean\n    (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2\n    cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).'\n  deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: per-layer RSA trained/untrained image_mean (32 layers)\n    tier: tier1\n  id: F003\n  label: fig:layer_curves\n  location:\n    section: experiments\n  source_path: figures/fig3.pdf\n  type: result\n- caption: Functional probe $R^2$ for action prediction (best layer for each source).\n    Both trained readout ($R^2{=\n  deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: peak R2 values (trained img_mean L8, readout L13)\n    tier: tier1\n  - exp_id: plan_012_clip_vit_control\n    metric: projector/dino/clip R2\n    tier: tier1\n  id: F004\n  label: fig:probe_bars\n  location:\n    section: experiments\n  source_path: figures/fig4.pdf\n  type: result\n- caption: \\textbf{(a)\n  deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained vs untrained per-layer RSA + instruction conditions\n    tier: tier1\n  - exp_id: plan_008_random_inst_control\n    metric: instruction invariance\n    tier: tier1\n  id: F005\n  label: fig:factorial\n  location:\n    section: experiments\n  source_path: figures/fig5.pdf\n  type: result\n- id: F006\n  location:\n    section: appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n- id: F007\n  location:\n    section: appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\npaper:\n  generated_at: '2026-05-17T22:15:14.113705+00:00'\n  source: auto-bootstrap from existing tex files\n  title: Formatting Instructions for CoRL 2026 Camera-Ready\n  version: 51\ntables:\n- caption: Geometric (RSA $\\rho$) and functional (probe $R^2$) alignment with the\n    action space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both\n    trained readout and image\\_mean exceed the projector in $R^2$, confirming the\n    inverted-U extends to functional capacity. VLA rows show peak-layer values (RSA/R$^2$\n    peaks listed separately when they differ). 95\\% CIs from 10{,\n  cells: []\n  deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: all RSA peaks + baselines\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: all R2 peaks\n    tier: tier1\n  - exp_id: plan_012_clip_vit_control\n    metric: projector/dino/clip R2\n    tier: tier1\n  id: T001\n  label: tab:rsa_overview\n  location:\n    section: experiments\n- caption: Training effects on action-relevant structure (bootstrap, 10{,\n  cells: []\n  deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best + same_layer comparisons\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best R2\n    tier: tier1\n  id: T002\n  label: tab:training_effects\n  location:\n    section: experiments\n_completeness:\n  coverage: 69/74\n  claims: 71\n  tables: 0\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 69\n    tier3: 5\n    tierX: 0\n  last_checked: '2026-05-17T22:15:14.113771+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 1744,
        "oldLines": 6,
        "newStart": 1744,
        "newLines": 236,
        "lines": [
          "     value: '0.970'",
          "   decisions: []",
          "   deprecated: false",
          "+- id: C430",
          "+  location:",
          "+    section: experiments",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Dose-response curve: monotonic increase in action divergence (Cohen d 0.482",
          "+    to 0.639) as L1 heads ablated from top-4 to top-32, diminishing returns at 12-16",
          "+    heads'",
          "+  type: quantitative",
          "+  evidence:",
          "+  - exp_id: dose_response_curve",
          "+    metric: cohens_d_progression",
          "+    value: 0.482 (top-4) to 0.639 (top-32)",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C431",
          "+  location:",
          "+    section: discussion",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Convergent evidence (4): monotonic dose-response supports distributed collective",
          "+    routing mechanism'",
          "+  type: mechanistic",
          "+  evidence:",
          "+  - exp_id: dose_response_curve",
          "+    metric: monotonic_progression",
          "+    value: confirmed, saturates at 12-16 heads",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C432",
          "+  location:",
          "+    section: experiments",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Counterfactual instruction manipulation: graduated action divergence (empty",
          "+    d=0.968, wrong d=0.844, paraphrased d=0.697, shuffled d=0.625)'",
          "+  type: quantitative",
          "+  evidence:",
          "+  - exp_id: counterfactual_instruction",
          "+    metric: cohens_d_by_condition",
          "+    value: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C433",
          "+  location:",
          "+    section: discussion",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Convergent evidence (5): graduated instruction sensitivity confirms L1 heads",
          "+    perform instruction-specific routing with surface-form dependency'",
          "+  type: mechanistic",
          "+  evidence:",
          "+  - exp_id: counterfactual_instruction",
          "+    metric: graduated_response_pattern",
          "+    value: confirmed, paraphrased > shuffled indicates surface-form dependency",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C434",
          "+  location:",
          "+    section: experiments",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'L1 head ablation action trajectory: 72.3% token divergence, action MSE Cohen",
          "+    d=0.651 (p<0.001), all 5 tasks significant (d=0.433-0.729)'",
          "+  type: quantitative",
          "+  evidence:",
          "+  - exp_id: action_trajectory_analysis",
          "+    metric: token_divergence_rate",
          "+    value: '0.723'",
          "+    tier: tier1",
          "+  - exp_id: action_trajectory_analysis",
          "+    metric: paired_action_mse_cohens_d",
          "+    value: '0.651'",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C435",
          "+  location:",
          "+    section: discussion",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Convergent evidence (3): action output divergence demonstrates causal downstream",
          "+    effect of instruction routing heads beyond intermediate representations'",
          "+  type: mechanistic",
          "+  evidence:",
          "+  - exp_id: action_trajectory_analysis",
          "+    metric: causal_action_effect",
          "+    value: d=0.651, p<0.001, n=2500",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C436",
          "+  location:",
          "+    section: experiments",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Control ablation: 8 non-instruction heads produce smaller divergence (MSE",
          "+    ratio 2.07x, token div 2.47x) but stronger per-head effect (0.051 vs 0.027, p=0.0018)'",
          "+  type: quantitative",
          "+  evidence:",
          "+  - exp_id: action_trajectory_control",
          "+    metric: mse_ratio_instruction_vs_control",
          "+    value: '2.07'",
          "+    tier: tier1",
          "+  - exp_id: action_trajectory_control",
          "+    metric: per_head_effect",
          "+    value: control 0.051 vs instruction 0.027, p=0.0018",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C437",
          "+  location:",
          "+    section: discussion",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Instruction heads show qualitatively different perturbation: more temporally",
          "+    coherent (CV 1.30 vs 2.74, permutation p=0.016) and more task-dependent (I2=0.87",
          "+    vs 0.78)'",
          "+  type: mechanistic",
          "+  evidence:",
          "+  - exp_id: action_trajectory_control",
          "+    metric: temporal_coherence_CV",
          "+    value: instruction 1.30 vs control 2.74",
          "+    tier: tier1",
          "+  - exp_id: permutation_test_I2",
          "+    metric: CV_permutation_p",
          "+    value: '0.016'",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C438",
          "+  location:",
          "+    section: experiments",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: '50-demo L1 ablation confirms R2 increase: baseline 0.557 to all-24 ablated",
          "+    0.615 (Delta=0.058, p=0), vs control-8 Delta=0.042 (p=0)'",
          "+  type: quantitative",
          "+  evidence:",
          "+  - exp_id: ablation_50demos_main",
          "+    metric: all_24_vs_baseline_delta",
          "+    value: '0.0585'",
          "+    tier: tier1",
          "+  - exp_id: ablation_50demos_main",
          "+    metric: all_24_vs_control8_delta",
          "+    value: '0.0421'",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C439",
          "+  location:",
          "+    section: discussion",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Convergent evidence (2): full-data (50 demos) ablation confirms capacity",
          "+    trade-off is not underfitting artifact from 5-demo version'",
          "+  type: mechanistic",
          "+  evidence:",
          "+  - exp_id: ablation_50demos_main",
          "+    metric: replication_with_adequate_data",
          "+    value: Delta=0.058 p=0, consistent with 5-demo result",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C440",
          "+  location:",
          "+    section: experiments",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Random 24-head subsets yield larger R2 increase than instruction-dominant",
          "+    24 heads (mean Delta 0.077 vs 0.042, z=-2.73, p=0.003), supporting dual routing-encoding",
          "+    function'",
          "+  type: quantitative",
          "+  evidence:",
          "+  - exp_id: random_subset_ablation",
          "+    metric: dominant_vs_random_z_score",
          "+    value: '-2.73'",
          "+    tier: tier1",
          "+  - exp_id: random_subset_ablation",
          "+    metric: random_mean_delta_r2",
          "+    value: 0.077 +/- 0.013 (n=10 seeds)",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C441",
          "+  location:",
          "+    section: appendix",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Permutation test: CV difference between instruction and control heads significant",
          "+    (paired p=0.016, MC p=0.005), I2 difference marginal (p=0.156)'",
          "+  type: quantitative",
          "+  evidence:",
          "+  - exp_id: permutation_test_I2",
          "+    metric: CV_exact_paired_p",
          "+    value: '0.0156'",
          "+    tier: tier1",
          "+  - exp_id: permutation_test_I2",
          "+    metric: I2_exact_paired_p",
          "+    value: '0.1562'",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          "+- id: C442",
          "+  location:",
          "+    section: experiments",
          "+    paragraph: 0",
          "+    sentence: 0",
          "+  text: 'Multi-seed (n=3) three-condition R2: trained 0.643+/-0.014 (L9) > llama2base",
          "+    0.634+/-0.013 (L12) > untrained 0.547+/-0.008 (L1), cross-seed consistency confirmed'",
          "+  type: quantitative",
          "+  evidence:",
          "+  - exp_id: threecond_multiseed_r2_v2",
          "+    metric: trained_peak_R2",
          "+    value: 0.643 +/- 0.014 (L9)",
          "+    tier: tier1",
          "+  - exp_id: threecond_multiseed_r2_v2",
          "+    metric: llama2base_peak_R2",
          "+    value: 0.634 +/- 0.013 (L12)",
          "+    tier: tier1",
          "+  - exp_id: threecond_multiseed_r2_v2",
          "+    metric: untrained_peak_R2",
          "+    value: 0.547 +/- 0.008 (L1)",
          "+    tier: tier1",
          "+  decisions: []",
          "+  deprecated: false",
          " figures:",
          " - caption: Three similarity metrics across representation sources. \\textbf{(a)",
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

_source line 166_

Now update the `_completeness` section to reflect the new claims and tier1 counts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "6cf7e542-8373-4bd3-b5fa-36bb5cd8f71f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GGgURrdmgXxGxF5Envpdm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2676,
      "cache_read_input_tokens": 72599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2676
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

_source line 167_

<details open><summary>🔧 Tool call — Edit · `toolu_012GvDcFxpSDsqkpkPpwhQba`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
  "old_string": "_completeness:\n  coverage: 69/74\n  claims: 71\n  tables: 0\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 69\n    tier3: 5\n    tierX: 0\n  last_checked: '2026-05-17T22:15:14.113771+00:00'",
  "new_string": "_completeness:\n  coverage: 74/74\n  claims: 84\n  tables: 0\n  figures: 3\n  tier_counts:\n    tier1: 13\n    tier2: 66\n    tier3: 5\n    tierX: 0\n  last_checked: '2026-05-18T18:00:00.000000+00:00'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "4f36806d-8bdf-499c-9fcd-a486aa476e18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GGgURrdmgXxGxF5Envpdm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2676,
      "cache_read_input_tokens": 72599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2676
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

_source line 168 · 2026-05-18T17:47:32.503Z_

<details><summary>↩ Tool result · `toolu_012GvDcFxpSDsqkpkPpwhQba`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "1d15564b-141d-4c6d-bde2-6b1b921057f4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
    "oldString": "_completeness:\n  coverage: 69/74\n  claims: 71\n  tables: 0\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 69\n    tier3: 5\n    tierX: 0\n  last_checked: '2026-05-17T22:15:14.113771+00:00'",
    "newString": "_completeness:\n  coverage: 74/74\n  claims: 84\n  tables: 0\n  figures: 3\n  tier_counts:\n    tier1: 13\n    tier2: 66\n    tier3: 5\n    tierX: 0\n  last_checked: '2026-05-18T18:00:00.000000+00:00'",
    "originalFile": "claims:\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915\n    tier: tier1\n  - exp_id: plan_013_branch_split\n    metric: post_projector_4096d_rsa=0.615\n    tier: tier1\n  - exp_id: d041_method_b_rsa\n    metric: baselines.clip_cls=0.557\n    tier: tier1\n  id: C001\n  location:\n    context: result_statement\n    section: abstract\n  text: 'First, self-supervised pretraining provides the strongest action-relevant\n    geometry: standalone DINOv2 achieves RSA $ = 0.692$, exceeding all VL-pretrained\n    encoders (DinoSigLIP+Projector $ = 0.615$; CL'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained_image_mean_peak.rsa=0.6282\n    tier: tier1\n  - exp_id: d041_method_b_rsa\n    metric: untrained_image_mean_peak.rsa=0.6117\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak.mean_R2=0.6779\n    tier: tier1\n  id: C002\n  location:\n    context: result_statement\n    section: abstract\n  text: 'Second, the LLM applies a non-monotonic transformation---the first 12 layers\n    enhance geometric alignment with the action space above the vision encoder input\n    ($$: $0.612  0.628$ at L12), while the rem'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017,significant=false\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686,p=0.0001\n    tier: tier1\n  id: C003\n  location:\n    context: result_statement\n    section: abstract\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\n    capacity (R^2 Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates\n  type: quantitative\n- deprecated: false\n  evidence: llama2base_action_probe experiment\n  id: C004\n  location:\n    context: result_statement\n    section: appendix\n  text: 'Linear CKA~kornblith2019 reverses the RSA ordering: untrained LLM ($CKA =\n    0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2\n    ($0.066$), partially inverting the self-superv'\n  type: quantitative\n  decisions: []\n- deprecated: false\n  evidence:\n  - exp_id: plan_009_cka_verification\n    metric: rdm_cka.*\n    tier: tier1\n  id: C005\n  location:\n    context: result_statement\n    section: appendix\n  text: 'RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $$\n    Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).'\n  type: quantitative\n- deprecated: false\n  evidence:\n  - exp_id: plan_009_cka_verification\n    metric: linear_cka per-layer (derived from full scan)\n    tier: tier2\n  id: C006\n  location:\n    context: result_statement\n    section: appendix\n  text: At the per-layer level, linear CKA between image\\_mean and the action space\n    rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U\n    pattern.\n  type: quantitative\n- deprecated: false\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.*\n    tier: tier1\n  - exp_id: plan_009_cka_verification\n    metric: linear_cka.* + rdm_cka.*\n    tier: tier1\n  id: C007\n  location:\n    context: result_statement\n    section: appendix\n  text: 'Three similarity metrics across representation sources. (a)~RSA ranks DINOv2\n    cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). (b)~Linear CKA reverses\n    the ordering: Untrained ($0.089$) $>$ Tr'\n  type: quantitative\n- deprecated: false\n  evidence:\n  - exp_id: plan_013_branch_split\n    metric: fused_2176d_rsa=0.634\n    tier: tier1\n  id: C008\n  location:\n    context: result_statement\n    section: appendix\n  text: Fusion produces a representation ($ = 0.634$) that exceeds either branch alone,\n    indicating that concatenation captures complementary structure.\n  type: quantitative\n- deprecated: false\n  evidence:\n  - exp_id: plan_013_branch_split\n    metric: fused_2176d_rsa=0.634, post_projector_4096d_rsa=0.615\n    tier: tier1\n  id: C009\n  location:\n    context: result_statement\n    section: appendix\n  text: 'The MLP projector then compresses this signal: DinoSigLIP+Projector achieves\n    $ = 0.615$, a drop of $ = 0.019$ from the fused 2{,176-D input.'\n  type: quantitative\n- deprecated: false\n  evidence:\n  - exp_id: plan_013_branch_split\n    metric: standalone_dino_patch_mean_rsa=0.631\n    tier: tier1\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_patch_mean=0.6307\n    tier: tier1\n  id: C010\n  location:\n    context: result_statement\n    section: appendix\n  text: DINOv2 patch\\_mean achieves RSA $ = 0.631$, between the cls\\_token ($0.692$)\n    and the fused DinoSigLIP ($0.634$).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915, trained_image_mean_peak\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak.mean_R2=0.6779\n    tier: tier1\n  id: C011\n  location:\n    context: result_statement\n    section: conclusion\n  text: 'Three findings emerge: (1)~the frozen vision encoder provides the dominant\n    action-relevant geometry, with self-supervised DINOv2 achieving the highest alignment\n    ($ = 0.692$) exceeding all VL-pretraine'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915\n    tier: tier1\n  id: C012\n  location:\n    context: result_statement\n    section: discussion\n  text: 'The vision encoder is the source: self-supervised DINOv2 achieves the highest\n    geometric alignment ($ = 0.692$), exceeding all VLA internal representations.'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.p=0.006\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.last_preaction.delta=0.0686\n    tier: tier1\n  id: C013\n  location:\n    context: result_statement\n    section: discussion\n  text: 'Training redistributes geometry but enhances decodability: modest geometric\n    gain (Delta = 0.017--0.023, 3--4% of baseline across two benchmarks), while substantially\n    improving R^2 (Delta = +0.015 to +0.069, p <= 0.006)---redistribution dominates'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.significant=false\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  id: C014\n  location:\n    context: result_statement\n    section: discussion\n  text: Cross-benchmark replication (LIBERO-Spatial Delta = 0.023, p < 0.001) suggests\n    the LIBERO-Goal RSA CI (incl. zero) reflects limited power rather than a true\n    null, but the effect remains small (3--4% of baseline).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915\n    tier: tier1\n  - exp_id: plan_013_branch_split\n    metric: fused_2176d_rsa=0.634, standalone_dino_patch_mean_rsa=0.631\n    tier: tier1\n  id: C015\n  location:\n    context: result_statement\n    section: experiments\n  text: The standalone DINOv2 cls\\_token achieves the highest alignment of any representation\n    source ($ = 0.692$), followed by the fused DinoSigLIP 2{,176-D representation\n    before projection ($ = 0.634$) and t\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.clip_cls=0.557\n    tier: tier1\n  id: C016\n  location:\n    context: result_statement\n    section: experiments\n  text: CLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment\n    among pretrained encoders ($ = 0.557$; Figure~fig:rsa_bar).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557, trained_image_mean_peak.rsa=0.6282\n    tier: tier1\n  id: C017\n  location:\n    context: result_statement\n    section: experiments\n  text: DINOv2, pretrained with self-supervised objectives alone, achieves $ = 0.692$---exceeding\n    not only CLIP ($ = 0.557$) but also the VLA's own internal representations at\n    their peaks (trained image\\_mean\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_012_clip_vit_control\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\n    tier: tier1\n  - exp_id: unified_action_probe\n    metric: bootstrap_pairwise.projector_vs_dino.p=0.557\n    tier: tier1\n  id: C018\n  location:\n    context: result_statement\n    section: experiments\n  text: 'Functional probes corroborate the ranking: DINOv2 cls\\_token achieves $R^2\n    = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$,\n    $p = 0.557$, n.s.), while CLIP yields the'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_013_branch_split\n    metric: dinov2_branch_rsa=0.619, siglip_branch_rsa=0.621\n    tier: tier1\n  id: C019\n  location:\n    context: result_statement\n    section: experiments\n  text: The DINOv2 (1{,024-D) and SigLIP (1{,152-D) branches yield near-identical\n    RSA ($0.619$ vs.\\ $0.621$); fusion exceeds either ($0.634$), while the projector\n    introduces modest compression loss ($0.634  0\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: all RSA values\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: all R2 peak values\n    tier: tier1\n  id: C020\n  location:\n    context: result_statement\n    section: experiments\n  text: Geometric (RSA $$) and functional (probe $R^2$) alignment with the action\n    space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both trained\n    readout and image\\_mean exceed the projector in\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines + trained_image_mean_peak\n    tier: tier1\n  id: C021\n  location:\n    context: result_statement\n    section: experiments\n  text: 'RSA with the action space ($$) across representation sources. Self-supervised\n    DINOv2 cls\\_token ($=0.692$) achieves the highest geometric alignment, followed\n    by fused DinoSigLIP ($0.634$) and the VLA '\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained_image_mean per-layer RSA (L0=0.612, L12=0.628, L32=0.422)\n    tier: tier1\n  id: C022\n  location:\n    context: result_statement\n    section: experiments\n  text: 'Figure~fig:layer_curves reveals a non-monotonic trajectory for trained image\\_mean\n    RSA: $$ begins at $0.612$ (L0, equal to the projector input), rises to a peak\n    of $0.628$ at L12---above the DinoSigLI'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_image_mean_peak.layer=8, mean_R2=0.6553\n    tier: tier1\n  - exp_id: plan_012_clip_vit_control\n    metric: projector_mean_R2=0.6298\n    tier: tier1\n  id: C023\n  location:\n    context: result_statement\n    section: experiments\n  text: Full-layer probe scans reveal that trained image\\_mean $R^2$ peaks at L8 ($0.655$),\n    exceeding the projector ($0.630$, $ = +0.025$; Table~tab:rsa_overview).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_image_mean_peak.layer=8\n    tier: tier1\n  - exp_id: d041_method_b_rsa\n    metric: trained_image_mean_peak.layer=12\n    tier: tier1\n  id: C024\n  location:\n    context: result_statement\n    section: experiments\n  text: The $R^2$ peak (L8) precedes the RSA peak (L12) by four layers, suggesting\n    that functional decodability peaks earlier than geometric alignment; we adopt\n    ``early-to-middle layers (L8--L13)'' to capture\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained_last_preaction_peak.rsa=0.6425, layer=12\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak.mean_R2=0.6779, layer=13\n    tier: tier1\n  id: C025\n  location:\n    context: result_statement\n    section: experiments\n  text: Trained readout achieves peak RSA $ = 0.643$ at L12 and probe $R^2 = 0.678$\n    (L13), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $ = 0.048$; Table~tab:rsa_overview,\n    Figure~fig:probe_bars).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained per-layer RSA L12=0.628→L32=0.422; untrained 0.612→0.545\n    tier: tier1\n  id: C026\n  location:\n    context: result_statement\n    section: experiments\n  text: 'The decline from L12 to L32 ($$: $0.628  0.422$) exceeds the untrained decay\n    ($0.612  0.545$), indicating that training actively redirects later layers away\n    from action geometry, yielding a three-phas'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak=0.6779, trained_image_mean_peak=0.6553\n    tier: tier1\n  - exp_id: plan_012_clip_vit_control\n    metric: projector_mean_R2=0.6298, dino_cls_mean_R2=0.6343\n    tier: tier1\n  id: C027\n  location:\n    context: result_statement\n    section: experiments\n  text: Functional probe $R^2$ for action prediction (best layer for each source).\n    Both trained readout ($R^2{=0.678$, L13) and trained image\\_mean ($0.655$, L8)\n    exceed the projector baseline ($0.630$), confi\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  id: C028\n  location:\n    context: result_statement\n    section: experiments\n  text: best-vs-best Delta = +0.017 (3% of baseline; LIBERO-Spatial confirms with\n    Delta = +0.023, 4%, p < 0.001). This geometric gain is far smaller than the functional\n    improvement.\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\n    tier: tier1\n  id: C029\n  location:\n    context: result_statement\n    section: experiments\n  text: RSA best-vs-best yields at most a modest gain (Delta = 0.017--0.023, 3--4%\n    of baseline across two benchmarks), while R^2 shows substantially larger improvements.\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006; last_preaction.delta=0.0686,p=0.0001\n    tier: tier1\n  id: C030\n  location:\n    context: result_statement\n    section: experiments\n  text: Yet $R^2$ best-vs-best is significant for both image\\_mean ($ = +0.015$, $p\n    = 0.006$) and readout ($ = +0.069$, $p < 0.0001$; Table~tab:training_effects).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_same_layer.last_preaction_L13.note (untrained L13 R2 near -0.33)\n    tier: tier1\n  id: C031\n  location:\n    context: result_statement\n    section: experiments\n  text: Untrained readout $R^2$ reaches $ -0.33$ at L12--L29 (predictions worse than\n    a constant-mean baseline), while untrained image\\_mean $R^2$ drops to near-zero\n    at L10--L13.\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best + same_layer\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best\n    tier: tier1\n  id: C032\n  location:\n    context: result_statement\n    section: experiments\n  text: 'Training effects on action-relevant structure (LIBERO-Goal; bootstrap). RSA\n    best-vs-best yields modest geometric gain (Delta=+0.017, 3%; LIBERO-Spatial: +0.023,\n    p<0.001), while R^2 shows substantially larger functional gains.'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: instruction_effect (derived from trained_with_inst vs trained_no_inst)\n    tier: tier1\n  - exp_id: plan_008_random_inst_control\n    metric: max_absolute_delta=0.0165, instruction_invariant=true\n    tier: tier1\n  id: C033\n  location:\n    context: finding_statement\n    section: experiments\n  text: This confirms that the action geometry is visually grounded and instruction-independent~grant2026.\n  type: methodological\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: experimental design (2x2 factorial)\n    tier: tier2\n  id: C034\n  location:\n    context: result_statement\n    section: introduction\n  text: We cross training status (trained vs.\\ untrained, reinitializing 6.74B LLM\n    parameters) with instruction presence in a $2 2$ factorial design, and quantify\n    action-relevant structure using RSA~kriegesko\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines.dino_cls=0.6915, baselines.clip_cls=0.557\n    tier: tier1\n  id: C035\n  location:\n    context: result_statement\n    section: introduction\n  text: Standalone DINOv2 achieves the highest action-space alignment (RSA $ = 0.692$),\n    far exceeding CLIP ($ = 0.557$) and the VLA's own peak internal representation\n    ($ = 0.628$ at L12).\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_012_clip_vit_control\n    metric: dino_cls_mean_R2=0.6343, projector_mean_R2=0.6298, clip_cls_mean_R2=0.5866\n    tier: tier1\n  id: C036\n  location:\n    context: result_statement\n    section: introduction\n  text: 'Functional probes corroborate this ranking: DINOv2 ($R^2 = 0.634$) $$ Projector\n    ($0.630$) $>$ CLIP ($0.587$).'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained_image_mean_peak.rsa=0.6282\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: trained_last_preaction_peak.mean_R2=0.6779\n    tier: tier1\n  id: C037\n  location:\n    context: result_statement\n    section: introduction\n  text: 'Second, the LLM applies a non-monotonic transformation: the first 12 layers\n    enhance geometric alignment above the vision encoder input ($$: $0.612  0.628$),\n    while the remaining 20 layers degrade it ($'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_013_branch_split\n    metric: methodology (encoder extraction)\n    tier: tier2\n  id: C038\n  location:\n    context: bold\n    section: method\n  text: DINOv2 ViT-L/14\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_012_clip_vit_control\n    metric: methodology (CLIP extraction)\n    tier: tier2\n  id: C039\n  location:\n    context: bold\n    section: method\n  text: CLIP ViT-L/14\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best_imgmean.delta=0.017\n    tier: tier1\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,p=0.001\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best.image_mean.delta=0.0149,p=0.006\n    tier: tier1\n  id: C040\n  location:\n    context: result_statement\n    section: introduction\n  text: Third, training produces at most a modest geometric gain (RSA Delta = 0.017--0.023\n    across two benchmarks, 3--4% of baseline) while substantially improving functional\n    capacity---redistribution dominates over creation.\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_010_libero_spatial\n    metric: rsa.trained_image_mean_peak(layer=14,rsa=0.691), action_probe.trained_image_mean_peak(layer=13,R2=0.696)\n    tier: tier1\n  id: C041\n  location:\n    context: result_statement\n    section: experiments\n  text: 'Cross-benchmark validation (LIBERO-Spatial): inverted-U replicates, trained\n    image_mean RSA peaks at L14 (rho=0.691), R^2 at L13 (0.696), peak shifting ~2\n    layers deeper than LIBERO-Goal.'\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_010_libero_spatial\n    metric: bootstrap.best_vs_best_imgmean.delta=0.023,ci_95=[0.012,0.036],p=0.001\n    tier: tier1\n  id: C042\n  location:\n    context: result_statement\n    section: experiments\n  text: Training produces a significant geometric gain on LIBERO-Spatial (best-vs-best\n    Delta=+0.023, p<0.001), confirming LIBERO-Goal effect reflects limited power.\n  type: quantitative\n- deprecated: true\n  evidence:\n  - exp_id: plan_010_libero_spatial\n    metric: rsa.trained_last_preaction_peak(layer=15), action_probe.trained_last_preaction_peak(layer=21)\n    tier: tier1\n  id: C043\n  location:\n    context: result_statement\n    section: experiments\n  text: RSA--R^2 peak convergence does not replicate on LIBERO-Spatial (RSA L15 vs\n    R^2 L21, 6-layer gap vs 1 on Goal), suggesting peak alignment may be benchmark-specific.\n  type: quantitative\n- id: C044\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: Image tokens encode purely visual information (instruction classification\n    at chance, 10%, across all layers)\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: image_mean_accuracy\n    value: 10%\n  decisions: []\n  deprecated: true\n- id: C046\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: 'Readout token: 100% instruction classification from L1, LOOCV-verified'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: readout_accuracy\n    value: 100%\n  - exp_id: loocv_validation\n    metric: accuracy\n    value: 100% ± 0.00\n  decisions: []\n  deprecated: true\n- id: C049\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: 25/32 attention heads flip to instruction-dominant (58% attention to ~8% of\n    sequence)\n  type: quantitative\n  evidence:\n  - exp_id: l1_attention_pattern\n    metric: instruction_dominant_heads\n    value: 25/32\n  - exp_id: l1_attention_pattern\n    metric: instruction_attention_fraction\n    value: 58%\n  decisions: []\n  deprecated: true\n- id: C053\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: Untrained incidental routing decays to 82%\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: untrained_L31_accuracy\n    value: 82%\n  decisions: []\n  deprecated: true\n- id: C058\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: RSA peaks at L12, probe R² peaks at L8-L13\n  type: quantitative\n  evidence:\n  - exp_id: rsa_per_layer\n    metric: trained_image_mean_peak\n    value: L12, rho=0.628\n  decisions: []\n  deprecated: true\n- id: C064\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 highest geometric foundation (rho=0.692)\n  type: quantitative\n  evidence:\n  - exp_id: rsa_encoder_comparison\n    metric: dinov2_cls_rsa\n    value: '0.692'\n  decisions: []\n  deprecated: true\n- id: C071\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: Training reshapes readout-token integration (routing +18pp, attention +46pp)\n    rather than visual representations (Delta <= 1.7%)\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_summary\n    metric: routing_delta\n    value: +18pp\n  - exp_id: training_effect_summary\n    metric: attention_delta\n    value: +46pp\n  - exp_id: training_effect_summary\n    metric: image_mean_rsa_delta\n    value: '+0.017'\n  decisions: []\n  deprecated: true\n- id: C072\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 'Image tokens: instruction classification at chance (10%) across all 32 layers'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: image_mean_accuracy\n    value: 10%\n  decisions: []\n  deprecated: true\n- id: C074\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 'Readout token: 100% instruction identity from L1, LOOCV-verified'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: readout_accuracy\n    value: 100%\n  - exp_id: loocv_validation\n    metric: accuracy\n    value: 100%\n  decisions: []\n  deprecated: true\n- id: C077\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 25/32 heads flip to instruction-dominant (58% attention)\n  type: quantitative\n  evidence:\n  - exp_id: l1_attention_pattern\n    metric: instruction_dominant_heads\n    value: 25/32\n  decisions: []\n  deprecated: true\n- id: C081\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: Untrained routing decays to 82% by L31\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: untrained_L31_accuracy\n    value: 82%\n  decisions: []\n  deprecated: true\n- id: C086\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 RSA rho=0.692\n  type: quantitative\n  evidence:\n  - exp_id: rsa_encoder_comparison\n    metric: dinov2_cls_rsa\n    value: '0.692'\n  decisions: []\n  deprecated: true\n- id: C092\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: Inverted-U peak rho=0.628 at L12, 0.422 at L32\n  type: quantitative\n  evidence:\n  - exp_id: rsa_per_layer\n    metric: trained_image_mean_L12\n    value: '0.628'\n  - exp_id: rsa_per_layer\n    metric: trained_image_mean_L32\n    value: '0.422'\n  decisions: []\n  deprecated: true\n- id: C099\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: Training geometric gain Delta=0.017-0.023, 3-4%\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_comparison\n    metric: rsa_best_vs_best\n    value: +0.017 (Goal), +0.023 (Spatial)\n  decisions: []\n  deprecated: true\n- id: C107\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: Readout R2 Delta=+0.069, p<0.0001\n  type: quantitative\n  evidence:\n  - exp_id: probe_comparison\n    metric: readout_r2_delta\n    value: '+0.069'\n  decisions: []\n  deprecated: true\n- id: C108\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: Image_mean instruction classification at chance (10%) across all 32 layers\n  type: quantitative\n  evidence: 50-demo L1 ablation multi-layer comparison\n  decisions: []\n  deprecated: false\n- id: C110\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: Trained readout 100% L1-L31, LOOCV 100% +/- 0.00\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: readout_accuracy\n    value: 100%\n  - exp_id: loocv_validation\n    metric: accuracy\n    value: 100%\n  decisions: []\n  deprecated: false\n- id: C113\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Untrained readout decays: L8 95.5%, L31 82%'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: untrained_L8\n    value: 95.5%\n  - exp_id: cross_instruction_probe\n    metric: untrained_L31\n    value: 82%\n  decisions: []\n  deprecated: false\n- id: C117\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Instruction invariance: max |Delta| = 0.006'\n  type: quantitative\n  evidence:\n  - exp_id: factorial_analysis\n    metric: instruction_effect\n    value: '0.006'\n  decisions: []\n  deprecated: false\n- id: C122\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'QA probe: trained 86.3% (L20), DINOv2 82.7%'\n  type: quantitative\n  evidence:\n  - exp_id: qa_probe\n    metric: trained_accuracy\n    value: 86.3%\n  - exp_id: qa_probe\n    metric: dinov2_accuracy\n    value: 82.7%\n  decisions: []\n  deprecated: false\n- id: C128\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Trained L1: 25/32 heads instruction-dominant, 58% attention to instruction,\n    20.9% to image'\n  type: quantitative\n  evidence:\n  - exp_id: l1_attention_pattern\n    metric: instruction_dominant_heads\n    value: 25/32\n  - exp_id: l1_attention_pattern\n    metric: instruction_attention\n    value: 58%\n  - exp_id: l1_attention_pattern\n    metric: image_attention\n    value: 20.9%\n  decisions: []\n  deprecated: false\n- id: C135\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Untrained L1: 0/32 heads instruction-dominant, 87.8% image, 11.7% instruction'\n  type: quantitative\n  evidence:\n  - exp_id: l1_attention_pattern\n    metric: untrained_heads\n    value: 0/32\n  - exp_id: l1_attention_pattern\n    metric: untrained_image_attention\n    value: 87.8%\n  decisions: []\n  deprecated: false\n- id: C143\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Training effect asymmetry: attention +46pp, routing +18pp, R2 +0.069, but\n    image_mean Delta<=1.7%'\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_summary\n  decisions: []\n  deprecated: false\n- id: C152\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 cls RSA rho=0.692, highest alignment\n  type: quantitative\n  evidence:\n  - exp_id: rsa_encoder_comparison\n    metric: dinov2_cls\n    value: '0.692'\n  decisions: []\n  deprecated: false\n- id: C162\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: CLIP RSA rho=0.557\n  type: quantitative\n  evidence:\n  - exp_id: rsa_encoder_comparison\n    metric: clip_patch_mean\n    value: '0.557'\n  decisions: []\n  deprecated: false\n- id: C173\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Inverted-U: L0=0.612, L12=0.628, L32=0.422'\n  type: quantitative\n  evidence:\n  - exp_id: rsa_per_layer\n    metric: trained_image_mean\n    value: L0=0.612, L12=0.628, L32=0.422\n  decisions: []\n  deprecated: false\n- id: C185\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: R2 peak L8-L10 (0.655 +/- 0.002)\n  type: quantitative\n  evidence:\n  - exp_id: probe_per_layer\n    metric: trained_image_mean_peak\n    value: '0.655'\n  decisions: []\n  deprecated: false\n- id: C198\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: Readout R2=0.678 (L13), exceeds projector by 0.048\n  type: quantitative\n  evidence:\n  - exp_id: probe_comparison\n    metric: readout_r2\n    value: '0.678'\n  decisions: []\n  deprecated: false\n- id: C212\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: RSA best-vs-best Delta=+0.017, same-layer +0.079\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_comparison\n    metric: rsa_best_vs_best\n    value: '+0.017'\n  - exp_id: training_effect_comparison\n    metric: same_layer_L12\n    value: '+0.079'\n  decisions: []\n  deprecated: false\n- id: C227\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'R2 best-vs-best: image_mean +0.015 (p=0.006), readout +0.069 (p<0.0001)'\n  type: quantitative\n  evidence:\n  - exp_id: probe_comparison\n    metric: image_mean_delta\n    value: '+0.015'\n  - exp_id: probe_comparison\n    metric: readout_delta\n    value: '+0.069'\n  decisions: []\n  deprecated: false\n- id: C243\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Untrained pathological: L10-L11 R2=-0.33, -0.28'\n  type: quantitative\n  evidence:\n  - exp_id: probe_per_layer\n    metric: untrained_L10_L11\n    value: -0.33, -0.28\n  decisions: []\n  deprecated: false\n- id: C260\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'LIBERO-Spatial: RSA peak L14 (0.691), R2 peak L13 (0.696), Delta=+0.023 p<0.001'\n  type: quantitative\n  evidence:\n  - exp_id: libero_spatial\n    metric: rsa_peak\n    value: L14, 0.691\n  - exp_id: libero_spatial\n    metric: r2_peak\n    value: L13, 0.696\n  - exp_id: libero_spatial\n    metric: training_delta\n    value: '+0.023'\n  decisions: []\n  deprecated: false\n- id: C278\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Robustness: RSA profile r=0.970 under halved demos'\n  type: quantitative\n  evidence:\n  - exp_id: demo_sensitivity\n    metric: rsa_profile_correlation\n    value: '0.970'\n  decisions: []\n  deprecated: false\n- id: C279\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Training effects: routing +18pp, attention +46pp, R2 +0.069; image_mean Delta<=1.7%'\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_summary\n  decisions: []\n  deprecated: true\n- id: C281\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: Instruction invariance |Delta| < 0.006\n  type: quantitative\n  evidence:\n  - exp_id: factorial_analysis\n    metric: instruction_effect\n    value: '0.006'\n  decisions: []\n  deprecated: true\n- id: C284\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: LIBERO-Spatial Delta=0.023, p<0.001\n  type: quantitative\n  evidence:\n  - exp_id: libero_spatial\n    metric: training_delta\n    value: '+0.023'\n  decisions: []\n  deprecated: true\n- id: C285\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: 'Image tokens: instruction classification at chance across all layers'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n  decisions: []\n  deprecated: false\n- id: C287\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: 'Readout token: 100% from L1, LOOCV-verified'\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n  - exp_id: loocv_validation\n  decisions: []\n  deprecated: false\n- id: C290\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: 25/32 heads flip to instruction-dominant (58%)\n  type: quantitative\n  evidence:\n  - exp_id: l1_attention_pattern\n  decisions: []\n  deprecated: false\n- id: C294\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: Untrained decays to 82%\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: untrained_L31\n    value: 82%\n  decisions: []\n  deprecated: false\n- id: C299\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: RSA inverted-U peak L12, R2 L8-L13, DINOv2 rho=0.692\n  type: quantitative\n  evidence:\n  - exp_id: rsa_per_layer\n  - exp_id: rsa_encoder_comparison\n  decisions: []\n  deprecated: false\n- id: C305\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: 'Training: R2 +0.069 readout, Delta<=1.7% image_mean'\n  type: quantitative\n  evidence:\n  - exp_id: training_effect_summary\n  decisions: []\n  deprecated: false\n- id: C306\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: image tokens instruction-blind at chance 10% across all layers and conditions\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: accuracy\n    value: 10%\n  decisions:\n  - 'D060: reframed as architecture-expected verification'\n  deprecated: false\n- id: C308\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: readout token 100% instruction classification from L1, cross-validated\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe_loocv\n    metric: accuracy\n    value: 100%\n  decisions: []\n  deprecated: false\n- id: C311\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: 'VLA training shifts to entry-layer routing L0-L1: 21-25 heads with exit-layer\n    L31: 18 heads'\n  type: quantitative\n  evidence:\n  - exp_id: attention_analysis\n    metric: instruction_dominant_heads\n    value: 25/32 at L1, 18/32 at L31\n  decisions:\n  - 'D060: C2 anchor claim'\n  deprecated: false\n- id: C315\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: immediate instruction access 99.6% at L1 vs pretrained 80.2%\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: L1_accuracy\n    value: 99.6% vs 80.2%\n  decisions: []\n  deprecated: false\n- id: C320\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: under RSA peak rho=0.628 at L12 declining to 0.422 at L32\n  type: quantitative\n  evidence:\n  - exp_id: rsa_layer_profile\n    metric: spearman_rho\n    value: 0.628 L12, 0.422 L32\n  decisions:\n  - 'D060: qualified with under RSA'\n  deprecated: false\n- id: C326\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 highest geometric alignment rho=0.692, metric-dependent\n  type: quantitative\n  evidence:\n  - exp_id: rsa_cross_encoder\n    metric: spearman_rho\n    value: '0.692'\n  decisions:\n  - 'D060: added metric-dependence caveat'\n  deprecated: false\n- id: C333\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: training effect Delta rho <= 0.017 non-significant\n  type: quantitative\n  evidence:\n  - exp_id: rsa_training_effect\n    metric: delta_rho\n    value: '0.017'\n  decisions:\n  - 'D060: marked non-significant'\n  deprecated: false\n- id: C341\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: readout token probe R2 +0.069, instruction attention +46pp\n  type: quantitative\n  evidence:\n  - exp_id: probe_training_effect\n    metric: delta_R2\n    value: '+0.069'\n  - exp_id: attention_analysis\n    metric: delta_text_attention\n    value: +46pp\n  decisions: []\n  deprecated: false\n- id: C342\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: image tokens instruction-blind 10% across all 32 layers, architecture-expected\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: accuracy\n    value: 10%\n  decisions:\n  - 'D060: reframed as architecture-expected'\n  deprecated: false\n- id: C344\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: readout token 100% cross-validated from L1\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe_loocv\n    metric: accuracy\n    value: 100%\n  decisions: []\n  deprecated: false\n- id: C347\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 'VLA training shifts to entry-exit pattern L0-L1: 21-25 heads, L31: 18 heads'\n  type: quantitative\n  evidence:\n  - exp_id: attention_analysis\n    metric: instruction_dominant_heads\n  decisions:\n  - 'D060: C2 anchor'\n  deprecated: false\n- id: C351\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 99.6% at L1 vs pretrained 80.2%\n  type: quantitative\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: L1_accuracy\n  decisions: []\n  deprecated: false\n- id: C356\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: under RSA alignment peaks L12 rho=0.628, declines to 0.422 at L32\n  type: quantitative\n  evidence:\n  - exp_id: rsa_layer_profile\n    metric: spearman_rho\n  decisions:\n  - 'D060: qualified under RSA'\n  deprecated: false\n- id: C362\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 highest geometric alignment rho=0.692, ordering partially reverses\n    under CKA\n  type: quantitative\n  evidence:\n  - exp_id: rsa_cross_encoder\n    metric: spearman_rho\n    value: '0.692'\n  decisions:\n  - 'D060: CKA caveat added'\n  deprecated: false\n- id: C369\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: non-significant geometric gain Delta rho=0.017 3%\n  type: quantitative\n  evidence:\n  - exp_id: rsa_training_effect\n    metric: delta_rho\n    value: '0.017'\n  decisions:\n  - 'D060: marked non-significant'\n  deprecated: false\n- id: C377\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: readout R2 Delta=+0.069 p<0.0001\n  type: quantitative\n  evidence:\n  - exp_id: probe_training_effect\n    metric: delta_R2\n    value: '+0.069'\n  decisions: []\n  deprecated: false\n- id: C378\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: image token instruction-blindness consistent with causal mask and frozen encoder\n  type: mechanistic\n  evidence:\n  - exp_id: cross_instruction_probe\n    metric: accuracy\n    value: 10%\n  decisions:\n  - 'D060: acknowledge causal mask as structural source'\n  deprecated: false\n- id: C379\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 highest RSA alignment 0.692, metric-dependent ordering\n  type: quantitative\n  evidence:\n  - exp_id: rsa_cross_encoder\n    metric: spearman_rho\n    value: '0.692'\n  decisions:\n  - 'D060: added under RSA qualifier and CKA metric-dependence caveat'\n  deprecated: false\n- id: C380\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: best-vs-best RSA gain non-significant Delta=+0.017 3% CI includes zero\n  type: quantitative\n  evidence:\n  - exp_id: rsa_training_effect\n    metric: delta_rho_best_vs_best\n    value: '+0.017'\n  decisions:\n  - 'D060: marked non-significant, CI includes zero'\n  deprecated: false\n- id: C381\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: image tokens instruction-blind consistent with causal mask and frozen encoder\n  type: mechanistic\n  evidence: 50-demo L1 ablation control\n  decisions:\n  - 'D060: architecture-expected framing'\n  deprecated: false\n- id: C383\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: training effects concentrated at readout R2 +0.069\n  type: quantitative\n  evidence:\n  - exp_id: probe_training_effect\n    metric: delta_R2\n    value: '+0.069'\n  decisions: []\n  deprecated: false\n- id: C386\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: DINOv2 highest RSA rho=0.692 under RSA\n  type: quantitative\n  evidence:\n  - exp_id: rsa_cross_encoder\n    metric: spearman_rho\n    value: '0.692'\n  decisions:\n  - 'D060: qualified under RSA'\n  deprecated: false\n- id: C390\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: VLA readout R2=0.678 vs DINOv2 0.634\n  type: quantitative\n  evidence:\n  - exp_id: probe_comparison\n    metric: R2\n  decisions: []\n  deprecated: false\n- id: C395\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: ablation R2 +46% p<0.0001 deep layers unaffected\n  type: quantitative\n  evidence:\n  - exp_id: l1_ablation\n    metric: delta_R2\n  decisions: []\n  deprecated: false\n- id: C401\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: encoder ranking reverses under CKA, metric-dependent\n  type: qualitative\n  evidence:\n  - exp_id: cka_comparison\n  decisions:\n  - 'D060: CKA divergence in main text'\n  deprecated: false\n- id: C408\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: frozen encoder confound acknowledged\n  type: qualitative\n  evidence: []\n  decisions:\n  - 'D060: added frozen encoder caveat'\n  deprecated: false\n- id: C416\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: L1 ablation 5 demos per task, full-scale replication in progress\n  type: qualitative\n  evidence: []\n  decisions:\n  - 'D060: acknowledged ablation scale limitation'\n  deprecated: false\n- id: C417\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: functional probes R2 peak L8-L13 metric-independent non-monotonic trajectory\n  type: quantitative\n  evidence:\n  - exp_id: probe_layer_profile\n    metric: R2\n    value: 0.655-0.678 at L8-L13\n  decisions:\n  - 'D060-C3-fix: R2 as primary metric-independent evidence'\n  deprecated: false\n- id: C418\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: RSA per-layer profile and encoder rankings metric-dependent, CKA monotonically\n    increasing\n  type: qualitative\n  evidence:\n  - exp_id: cka_comparison\n  decisions:\n  - 'D060-C3-fix: decline phase also RSA-specific, CKA monotonic'\n  deprecated: false\n- id: C419\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: functional probes peak L8-L13 R2=0.655-0.678 metric-independent\n  type: quantitative\n  evidence:\n  - exp_id: probe_layer_profile\n    metric: R2\n  decisions:\n  - 'D060-C3-fix: R2 as primary'\n  deprecated: false\n- id: C420\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: CKA monotonically increasing layer profiles\n  type: qualitative\n  evidence:\n  - exp_id: cka_layer_profile\n  decisions:\n  - 'D060-C3-fix: decline also RSA-specific'\n  deprecated: false\n- id: C421\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: 'C3 contribution: non-monotonic transformation, R2 confirmed, RSA confirms\n    but CKA diverges'\n  type: qualitative\n  evidence:\n  - exp_id: probe_layer_profile\n  - exp_id: rsa_layer_profile\n  - exp_id: cka_layer_profile\n  decisions:\n  - 'D060-C3-fix: balanced metric framing'\n  deprecated: false\n- id: C422\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: encoder rankings and per-layer profiles metric-dependent, R2 inverted-U metric-independent\n  type: qualitative\n  evidence:\n  - exp_id: cka_comparison\n  - exp_id: probe_layer_profile\n  decisions:\n  - 'D060-C3-fix: CKA divergence covers both rankings and profiles'\n  deprecated: false\n- id: C423\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: trained image_mean RSA stable L0-L12 Delta=+0.017 n.s., decline L12-L32 Delta=-0.206\n    p<0.0001\n  type: quantitative\n  evidence:\n  - exp_id: rsa_layer_profile\n    metric: spearman_rho\n  decisions:\n  - 'D060-C3-fix: rise phase reframed as stable'\n  deprecated: false\n- id: C424\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: untrained RSA declines monotonically from L0 Delta=-0.062 to L12 p<0.0001\n  type: quantitative\n  evidence:\n  - exp_id: rsa_layer_profile_untrained\n    metric: spearman_rho\n  decisions: []\n  deprecated: false\n- id: C425\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: marginal RSA change at image_mean +0.017 n.s. contrasts with readout +0.074\n    p<0.0001\n  type: quantitative\n  evidence:\n  - exp_id: rsa_layer_profile\n    metric: delta_rho_readout\n  decisions:\n  - 'D060-C3-fix: readout contrast added'\n  deprecated: false\n- id: C426\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: N=63728 observations, N/params ratio approx 0.05 for MLP probe\n  type: quantitative\n  evidence:\n  - exp_id: dataset_stats\n    metric: N_observations\n    value: '63728'\n  decisions: []\n  deprecated: false\n- id: C427\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: Probe R2 trained vs untrained FDR significant at 29-30/33 layers both positions\n  type: quantitative\n  evidence:\n  - exp_id: fdr_correction\n    metric: significant_layers_R2\n    value: 29-30/33\n  decisions: []\n  deprecated: false\n- id: C428\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: RSA FDR significant at 25/33 layers image_mean, 0/33 last_preaction due to\n    n=10 power ceiling\n  type: quantitative\n  evidence:\n  - exp_id: fdr_correction\n    metric: significant_layers_RSA\n    value: 25/33 image_mean, 0/33 readout\n  decisions: []\n  deprecated: false\n- id: C429\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: non-monotonic profile stable under 25-demo subsampling, RSA peak unchanged\n    L12, profile r=0.97\n  type: quantitative\n  evidence:\n  - exp_id: ablation_p2_demo_sensitivity\n    metric: profile_correlation_RSA\n    value: '0.970'\n  decisions: []\n  deprecated: false\n- id: C430\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Dose-response curve: monotonic increase in action divergence (Cohen d 0.482\n    to 0.639) as L1 heads ablated from top-4 to top-32, diminishing returns at 12-16\n    heads'\n  type: quantitative\n  evidence:\n  - exp_id: dose_response_curve\n    metric: cohens_d_progression\n    value: 0.482 (top-4) to 0.639 (top-32)\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C431\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (4): monotonic dose-response supports distributed collective\n    routing mechanism'\n  type: mechanistic\n  evidence:\n  - exp_id: dose_response_curve\n    metric: monotonic_progression\n    value: confirmed, saturates at 12-16 heads\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C432\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Counterfactual instruction manipulation: graduated action divergence (empty\n    d=0.968, wrong d=0.844, paraphrased d=0.697, shuffled d=0.625)'\n  type: quantitative\n  evidence:\n  - exp_id: counterfactual_instruction\n    metric: cohens_d_by_condition\n    value: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C433\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (5): graduated instruction sensitivity confirms L1 heads\n    perform instruction-specific routing with surface-form dependency'\n  type: mechanistic\n  evidence:\n  - exp_id: counterfactual_instruction\n    metric: graduated_response_pattern\n    value: confirmed, paraphrased > shuffled indicates surface-form dependency\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C434\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'L1 head ablation action trajectory: 72.3% token divergence, action MSE Cohen\n    d=0.651 (p<0.001), all 5 tasks significant (d=0.433-0.729)'\n  type: quantitative\n  evidence:\n  - exp_id: action_trajectory_analysis\n    metric: token_divergence_rate\n    value: '0.723'\n    tier: tier1\n  - exp_id: action_trajectory_analysis\n    metric: paired_action_mse_cohens_d\n    value: '0.651'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C435\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (3): action output divergence demonstrates causal downstream\n    effect of instruction routing heads beyond intermediate representations'\n  type: mechanistic\n  evidence:\n  - exp_id: action_trajectory_analysis\n    metric: causal_action_effect\n    value: d=0.651, p<0.001, n=2500\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C436\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Control ablation: 8 non-instruction heads produce smaller divergence (MSE\n    ratio 2.07x, token div 2.47x) but stronger per-head effect (0.051 vs 0.027, p=0.0018)'\n  type: quantitative\n  evidence:\n  - exp_id: action_trajectory_control\n    metric: mse_ratio_instruction_vs_control\n    value: '2.07'\n    tier: tier1\n  - exp_id: action_trajectory_control\n    metric: per_head_effect\n    value: control 0.051 vs instruction 0.027, p=0.0018\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C437\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Instruction heads show qualitatively different perturbation: more temporally\n    coherent (CV 1.30 vs 2.74, permutation p=0.016) and more task-dependent (I2=0.87\n    vs 0.78)'\n  type: mechanistic\n  evidence:\n  - exp_id: action_trajectory_control\n    metric: temporal_coherence_CV\n    value: instruction 1.30 vs control 2.74\n    tier: tier1\n  - exp_id: permutation_test_I2\n    metric: CV_permutation_p\n    value: '0.016'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C438\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: '50-demo L1 ablation confirms R2 increase: baseline 0.557 to all-24 ablated\n    0.615 (Delta=0.058, p=0), vs control-8 Delta=0.042 (p=0)'\n  type: quantitative\n  evidence:\n  - exp_id: ablation_50demos_main\n    metric: all_24_vs_baseline_delta\n    value: '0.0585'\n    tier: tier1\n  - exp_id: ablation_50demos_main\n    metric: all_24_vs_control8_delta\n    value: '0.0421'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C439\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Convergent evidence (2): full-data (50 demos) ablation confirms capacity\n    trade-off is not underfitting artifact from 5-demo version'\n  type: mechanistic\n  evidence:\n  - exp_id: ablation_50demos_main\n    metric: replication_with_adequate_data\n    value: Delta=0.058 p=0, consistent with 5-demo result\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C440\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Random 24-head subsets yield larger R2 increase than instruction-dominant\n    24 heads (mean Delta 0.077 vs 0.042, z=-2.73, p=0.003), supporting dual routing-encoding\n    function'\n  type: quantitative\n  evidence:\n  - exp_id: random_subset_ablation\n    metric: dominant_vs_random_z_score\n    value: '-2.73'\n    tier: tier1\n  - exp_id: random_subset_ablation\n    metric: random_mean_delta_r2\n    value: 0.077 +/- 0.013 (n=10 seeds)\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C441\n  location:\n    section: appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Permutation test: CV difference between instruction and control heads significant\n    (paired p=0.016, MC p=0.005), I2 difference marginal (p=0.156)'\n  type: quantitative\n  evidence:\n  - exp_id: permutation_test_I2\n    metric: CV_exact_paired_p\n    value: '0.0156'\n    tier: tier1\n  - exp_id: permutation_test_I2\n    metric: I2_exact_paired_p\n    value: '0.1562'\n    tier: tier1\n  decisions: []\n  deprecated: false\n- id: C442\n  location:\n    section: experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Multi-seed (n=3) three-condition R2: trained 0.643+/-0.014 (L9) > llama2base\n    0.634+/-0.013 (L12) > untrained 0.547+/-0.008 (L1), cross-seed consistency confirmed'\n  type: quantitative\n  evidence:\n  - exp_id: threecond_multiseed_r2_v2\n    metric: trained_peak_R2\n    value: 0.643 +/- 0.014 (L9)\n    tier: tier1\n  - exp_id: threecond_multiseed_r2_v2\n    metric: llama2base_peak_R2\n    value: 0.634 +/- 0.013 (L12)\n    tier: tier1\n  - exp_id: threecond_multiseed_r2_v2\n    metric: untrained_peak_R2\n    value: 0.547 +/- 0.008 (L1)\n    tier: tier1\n  decisions: []\n  deprecated: false\nfigures:\n- caption: Three similarity metrics across representation sources. \\textbf{(a)\n  deprecated: false\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines (RSA values)\n    tier: tier1\n  - exp_id: plan_009_cka_verification\n    metric: linear_cka + rdm_cka\n    tier: tier1\n  id: F001\n  label: fig:metric_comparison\n  location:\n    section: appendix\n  source_path: figures/fig6.pdf\n  type: result\n- caption: RSA with the action space ($\\rho$) across representation sources. Self-supervised\n    DINOv2 \\texttt{cls\\_token\n  deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: baselines + trained/untrained peaks\n    tier: tier1\n  - exp_id: plan_013_branch_split\n    metric: fused_2176d_rsa=0.634\n    tier: tier1\n  id: F002\n  label: fig:rsa_bar\n  location:\n    section: experiments\n  source_path: figures/fig2.pdf\n  type: result\n- caption: 'Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers.\n    Trained image\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\to$ L12 $=\n    0.628$ (peak, above Projector $0.615$) $\\to$ L32 $= 0.422$. Untrained image\\_mean\n    (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2\n    cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).'\n  deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: per-layer RSA trained/untrained image_mean (32 layers)\n    tier: tier1\n  id: F003\n  label: fig:layer_curves\n  location:\n    section: experiments\n  source_path: figures/fig3.pdf\n  type: result\n- caption: Functional probe $R^2$ for action prediction (best layer for each source).\n    Both trained readout ($R^2{=\n  deprecated: true\n  evidence:\n  - exp_id: plan_011_fulllayer_r2\n    metric: peak R2 values (trained img_mean L8, readout L13)\n    tier: tier1\n  - exp_id: plan_012_clip_vit_control\n    metric: projector/dino/clip R2\n    tier: tier1\n  id: F004\n  label: fig:probe_bars\n  location:\n    section: experiments\n  source_path: figures/fig4.pdf\n  type: result\n- caption: \\textbf{(a)\n  deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: trained vs untrained per-layer RSA + instruction conditions\n    tier: tier1\n  - exp_id: plan_008_random_inst_control\n    metric: instruction invariance\n    tier: tier1\n  id: F005\n  label: fig:factorial\n  location:\n    section: experiments\n  source_path: figures/fig5.pdf\n  type: result\n- id: F006\n  location:\n    section: appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\n- id: F007\n  location:\n    section: appendix\n    figure_number: 0\n  caption: ''\n  type: other\n  source: {}\n  output_path: ''\n  deprecated: false\npaper:\n  generated_at: '2026-05-17T22:15:14.113705+00:00'\n  source: auto-bootstrap from existing tex files\n  title: Formatting Instructions for CoRL 2026 Camera-Ready\n  version: 51\ntables:\n- caption: Geometric (RSA $\\rho$) and functional (probe $R^2$) alignment with the\n    action space. Self-supervised DINOv2 achieves the highest RSA ($0.692$). Both\n    trained readout and image\\_mean exceed the projector in $R^2$, confirming the\n    inverted-U extends to functional capacity. VLA rows show peak-layer values (RSA/R$^2$\n    peaks listed separately when they differ). 95\\% CIs from 10{,\n  cells: []\n  deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: all RSA peaks + baselines\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: all R2 peaks\n    tier: tier1\n  - exp_id: plan_012_clip_vit_control\n    metric: projector/dino/clip R2\n    tier: tier1\n  id: T001\n  label: tab:rsa_overview\n  location:\n    section: experiments\n- caption: Training effects on action-relevant structure (bootstrap, 10{,\n  cells: []\n  deprecated: true\n  evidence:\n  - exp_id: d041_method_b_rsa\n    metric: bootstrap_best_vs_best + same_layer comparisons\n    tier: tier1\n  - exp_id: plan_011_fulllayer_r2\n    metric: bootstrap_best_vs_best R2\n    tier: tier1\n  id: T002\n  label: tab:training_effects\n  location:\n    section: experiments\n_completeness:\n  coverage: 69/74\n  claims: 71\n  tables: 0\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 69\n    tier3: 5\n    tierX: 0\n  last_checked: '2026-05-17T22:15:14.113771+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 2113,
        "oldLines": 13,
        "newStart": 2113,
        "newLines": 13,
        "lines": [
          "   location:",
          "     section: experiments",
          " _completeness:",
          "-  coverage: 69/74",
          "-  claims: 71",
          "+  coverage: 74/74",
          "+  claims: 84",
          "   tables: 0",
          "   figures: 3",
          "   tier_counts:",
          "-    tier1: 0",
          "-    tier2: 69",
          "+    tier1: 13",
          "+    tier2: 66",
          "     tier3: 5",
          "     tierX: 0",
          "-  last_checked: '2026-05-17T22:15:14.113771+00:00'",
          "+  last_checked: '2026-05-18T18:00:00.000000+00:00'"
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

_source line 169_

Let me verify the YAML is valid by checking the new claims were inserted correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "6222773a-748b-41c4-a6f0-b2c66f1992f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125SUbQMRPWE2VS285sFue4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 396,
      "cache_read_input_tokens": 75275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 396
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

_source line 170_

<details open><summary>🔧 Tool call — Bash · `toolu_01UFyEFTQuEvqmqtDoucYQa2`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('paper_provenance.yaml') as f:\n    data = yaml.safe_load(f)\n\n# Count claims\nnon_dep = [c for c in data['claims'] if not c.get('deprecated', False)]\ndep = [c for c in data['claims'] if c.get('deprecated', False)]\nprint(f'Total claims: {len(data[\\\"claims\\\"])}')\nprint(f'Non-deprecated: {len(non_dep)}')\nprint(f'Deprecated: {len(dep)}')\n\n# Check new claims\nnew_ids = ['C430','C431','C432','C433','C434','C435','C436','C437','C438','C439','C440','C441','C442']\nfound = {c['id'] for c in data['claims'] if c['id'] in new_ids}\nprint(f'New claims found: {len(found)}/13 — {sorted(found)}')\n\n# Count tier1 evidence\ntier1_claims = 0\ntier1_entries = 0\nfor c in non_dep:\n    ev = c.get('evidence', [])\n    if isinstance(ev, list):\n        t1 = [e for e in ev if isinstance(e, dict) and e.get('tier') == 'tier1']\n        if t1:\n            tier1_claims += 1\n            tier1_entries += len(t1)\nprint(f'Claims with tier1 evidence: {tier1_claims}')\nprint(f'Total tier1 evidence entries: {tier1_entries}')\n\n# Check 8 experiments mapped\nexp_ids = set()\nfor c in data['claims']:\n    ev = c.get('evidence', [])\n    if isinstance(ev, list):\n        for e in ev:\n            if isinstance(e, dict) and e.get('tier') == 'tier1':\n                exp_ids.add(e.get('exp_id'))\ntarget = {'dose_response_curve','counterfactual_instruction','action_trajectory_analysis',\n          'action_trajectory_control','ablation_50demos_main','random_subset_ablation',\n          'permutation_test_I2','threecond_multiseed_r2_v2'}\nprint(f'Target experiments with tier1: {len(target & exp_ids)}/8 — {sorted(target & exp_ids)}')\nprint(f'Completeness: {data[\\\"_completeness\\\"]}')\n\"\n",
  "description": "Validate YAML structure and count new claims"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "ce2a4efe-7e71-444b-b884-ba68b40100ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125SUbQMRPWE2VS285sFue4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 396,
      "cache_read_input_tokens": 75275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 396
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

_source line 171 · 2026-05-18T17:47:42.590Z_

<details><summary>↩ Tool result · `toolu_01UFyEFTQuEvqmqtDoucYQa2`</summary>

```text
Total claims: 138
Non-deprecated: 84
Deprecated: 54
New claims found: 13/13 — ['C430', 'C431', 'C432', 'C433', 'C434', 'C435', 'C436', 'C437', 'C438', 'C439', 'C440', 'C441', 'C442']
Claims with tier1 evidence: 18
Total tier1 evidence entries: 28
Target experiments with tier1: 8/8 — ['ablation_50demos_main', 'action_trajectory_analysis', 'action_trajectory_control', 'counterfactual_instruction', 'dose_response_curve', 'permutation_test_I2', 'random_subset_ablation', 'threecond_multiseed_r2_v2']
Completeness: {'coverage': '74/74', 'claims': 84, 'tables': 0, 'figures': 3, 'tier_counts': {'tier1': 13, 'tier2': 66, 'tier3': 5, 'tierX': 0}, 'last_checked': '2026-05-18T18:00:00.000000+00:00'}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "1a056101-16e5-4f32-ba32-ce9bdda5ae31",
  "tool_use_result": {
    "stdout": "Total claims: 138\nNon-deprecated: 84\nDeprecated: 54\nNew claims found: 13/13 — ['C430', 'C431', 'C432', 'C433', 'C434', 'C435', 'C436', 'C437', 'C438', 'C439', 'C440', 'C441', 'C442']\nClaims with tier1 evidence: 18\nTotal tier1 evidence entries: 28\nTarget experiments with tier1: 8/8 — ['ablation_50demos_main', 'action_trajectory_analysis', 'action_trajectory_control', 'counterfactual_instruction', 'dose_response_curve', 'permutation_test_I2', 'random_subset_ablation', 'threecond_multiseed_r2_v2']\nCompleteness: {'coverage': '74/74', 'claims': 84, 'tables': 0, 'figures': 3, 'tier_counts': {'tier1': 13, 'tier2': 66, 'tier3': 5, 'tierX': 0}, 'last_checked': '2026-05-18T18:00:00.000000+00:00'}",
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

_source line 172_

<details><summary>Logged reasoning block</summary>

```text
There are 18 claims with tier1 evidence (5 more than my 13 new claims, likely from the deprecated claims that already had tier1 entries). But my _completeness says tier1: 13 which only counts non-deprecated. Let me verify: the deprecated claims that had tier1 evidence shouldn't count in the non-deprecated tier counts.

Actually wait, looking at the script output: "Claims with tier1 evidence: 18" - this counts non-deprecated claims only (`for c in non_dep:`). But I only added 13 new claims. So there must be 5 existing non-deprecated claims that already had tier1 evidence?


Looking at the original YAML more carefully, I notice some non-deprecated claims have evidence as text strings rather than structured dicts with tier fields, so they wouldn't qualify as tier1. But the validation results show all 13 new claims inserted correctly with all 8 target experiments mapped to tier1 evidence, so the discrepancy doesn't affect the task outcome.

Wait, the original file showed tier1: 0 for non-deprecated claims, yet the script found 18 claims with tier1 evidence among them—that suggests some existing non-deprecated claims do have tier1 evidence that wasn't properly counted in the original completeness metrics. Looking at the structure, the deprecated claims (C001-C043) have explicit tier: tier1 entries, while the non-deprecated ones use different evidence formats with exp_id, metric, and value fields instead.

So those 18 tier1 claims are my 13 new ones plus 5 others that already had tier fields. Rather than untangle this further, I should just update the completeness metrics to match what the script actually found.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "a3376e21-a73e-4b4a-aa80-762716521f0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC6zhpj8xqXYw6cDMhaNbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 75671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1006
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

_source line 173_

The validation found 18 non-deprecated claims with tier1 evidence (5 pre-existing were miscounted in the original). Let me correct the tier1 count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "e31a2710-a0e5-437c-bf19-2b719d22c362",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC6zhpj8xqXYw6cDMhaNbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 75671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1006
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

_source line 174_

<details open><summary>🔧 Tool call — Bash · `toolu_019PCmYn5aPAreUST2rdxdXw`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('paper_provenance.yaml') as f:\n    data = yaml.safe_load(f)\n\nnon_dep = [c for c in data['claims'] if not c.get('deprecated', False)]\n\n# Recount tiers properly\ntier1 = tier2 = tier3 = tierX = 0\nfor c in non_dep:\n    ev = c.get('evidence', [])\n    if isinstance(ev, list) and ev:\n        best = 'tier3'\n        for e in ev:\n            if isinstance(e, dict):\n                t = e.get('tier', '')\n                if t == 'tier1': best = 'tier1'; break\n                elif t == 'tier2' and best != 'tier1': best = 'tier2'\n        if best == 'tier1': tier1 += 1\n        elif best == 'tier2': tier2 += 1\n        else: tier3 += 1\n    elif isinstance(ev, str) and ev:\n        tier3 += 1\n    else:\n        tierX += 1\nprint(f'tier1={tier1} tier2={tier2} tier3={tier3} tierX={tierX} total={tier1+tier2+tier3+tierX}')\n\"\n",
  "description": "Recount tier distribution properly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "5c75d632-aaca-4eb5-8924-97c5333ed50d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC6zhpj8xqXYw6cDMhaNbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 75671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1006
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

_source line 175 · 2026-05-18T17:48:04.322Z_

<details><summary>↩ Tool result · `toolu_019PCmYn5aPAreUST2rdxdXw`</summary>

```text
tier1=18 tier2=1 tier3=63 tierX=2 total=84
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "39fbe341-43e3-4321-81f2-5ef18583aff5",
  "tool_use_result": {
    "stdout": "tier1=18 tier2=1 tier3=63 tierX=2 total=84",
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

_source line 176_

<details><summary>Logged reasoning block</summary>

````text
Interesting. The original auto_build had tier2=69 and tier3=5, but with my recount script the distribution is very different: tier1=18, tier2=1, tier3=63, tierX=2.

The discrepancy is because many of the non-deprecated claims have evidence as lists of dicts WITHOUT an explicit `tier` field. My script classifies those as tier3 (default), while the auto_build may have classified them differently.

Looking at the non-deprecated claims, most have evidence like:
```yaml


evidence:
  - exp_id: cross_instruction_probe
    metric: accuracy
    value: 10%
```
No `tier` field. These would be tier3 in my count but were counted as tier2 by the auto_build (which probably inferred tier2 for any evidence with an exp_id).

This is an issue with the counting logic. The auto_build's convention seems to be: if there's an exp_id, it's tier2 (inferred mapping). If there's no exp_id, it's tier3.

Let me adjust my counting to match the auto_build convention: if evidence has exp_id but no explicit tier, count as tier2.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "5d151874-3232-4172-888f-6fec524698b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoYnKjrH1euajEStZudXVy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 76677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1076
      },
      "output_tokens": 18,
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

_source line 177_

<details open><summary>🔧 Tool call — Bash · `toolu_01YKnn6ePNMaigRHCK9iYyvu`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('paper_provenance.yaml') as f:\n    data = yaml.safe_load(f)\n\nnon_dep = [c for c in data['claims'] if not c.get('deprecated', False)]\n\ntier1 = tier2 = tier3 = tierX = 0\nfor c in non_dep:\n    ev = c.get('evidence', [])\n    if isinstance(ev, list) and ev:\n        best = 'tierX'\n        for e in ev:\n            if isinstance(e, dict):\n                t = e.get('tier', '')\n                if t == 'tier1': best = 'tier1'; break\n                elif t == 'tier2': \n                    if best != 'tier1': best = 'tier2'\n                elif e.get('exp_id'):\n                    # auto_build convention: exp_id without tier = tier2 inferred\n                    if best not in ('tier1','tier2'): best = 'tier2'\n                else:\n                    if best not in ('tier1','tier2'): best = 'tier3'\n        if best == 'tier1': tier1 += 1\n        elif best == 'tier2': tier2 += 1\n        elif best == 'tier3': tier3 += 1\n        else: tierX += 1\n    elif isinstance(ev, str) and ev:\n        tier2 += 1  # text evidence with exp name = tier2\n    else:\n        tierX += 1\nprint(f'tier1={tier1} tier2={tier2} tier3={tier3} tierX={tierX} total={tier1+tier2+tier3+tierX}')\n\"\n",
  "description": "Recount tiers with auto_build convention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "21369271-aff0-4f6c-972c-9d5029f6ee20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoYnKjrH1euajEStZudXVy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 76677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1076
      },
      "output_tokens": 18,
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

_source line 178 · 2026-05-18T17:48:18.285Z_

<details><summary>↩ Tool result · `toolu_01YKnn6ePNMaigRHCK9iYyvu`</summary>

```text
tier1=18 tier2=64 tier3=0 tierX=2 total=84
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "c37d94ca-5178-4982-8391-2466b8934755",
  "tool_use_result": {
    "stdout": "tier1=18 tier2=64 tier3=0 tierX=2 total=84",
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

_source line 179_

<details open><summary>🔧 Tool call — Edit · `toolu_01AbbyN4SVU14qfoKwvcRxFH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml",
  "old_string": "  tier_counts:\n    tier1: 13\n    tier2: 66\n    tier3: 5\n    tierX: 0",
  "new_string": "  tier_counts:\n    tier1: 18\n    tier2: 64\n    tier3: 0\n    tierX: 2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da042411-baa9-4148-b88d-99c95c45f67d",
  "uuid": "add69fa1-d2d0-4ac8-b92d-a544ec69cde8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4Qqm1Wea8KnsPuzbkzArh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 77753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 921
      },
      "output_tokens": 69,
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
