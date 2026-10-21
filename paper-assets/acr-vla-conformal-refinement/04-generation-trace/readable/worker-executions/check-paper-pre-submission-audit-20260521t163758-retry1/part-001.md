# check paper pre submission audit 20260521T163758 retry1 — Part 1 of 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[Transcript overview](../check-paper-pre-submission-audit-20260521t163758-retry1.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/f5/f538ad13bf5adf5f72d4.json)

## Before a recorded user message

## Before a recorded user message

124 recorded events


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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
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
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "2cbc0585-062d-4dff-8596-f655186f494e",
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
    "resetsAt": 1779397800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "14bca2a8-9513-4ceb-9142-2457ad274a22",
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "c6752624-770c-472b-8082-6953a2582701",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XD4fXzfZe6iQRLAR8Q7J17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14596,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14596
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016YqJCN4QAKbe3W8NEZnJAY`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "30bde591-87f8-42f2-9c41-fba12508e582",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XD4fXzfZe6iQRLAR8Q7J17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14596,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14596
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


### Tool result

_source line 6 · 2026-05-21T16:38:16.192Z_

<details><summary>↩ Tool result · `toolu_016YqJCN4QAKbe3W8NEZnJAY`</summary>

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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "83c8b9ab-1796-4ee8-bab8-108c9a65f60d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "e10855ab-de3f-491f-807a-c91a71fcf659",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0115V2T4xDvHxkiDvmEWeA2d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16473,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16473
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28649
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Bash · `toolu_01KTPeqZD8dhp5omPXFP1STm`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/",
  "description": "List project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "981ec51c-2fe2-444d-b3da-30772dc050c4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0115V2T4xDvHxkiDvmEWeA2d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16473,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16473
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28649
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-21T16:38:21.046Z_

<details><summary>↩ Tool result · `toolu_01KTPeqZD8dhp5omPXFP1STm`</summary>

```text
AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "d3240f24-16c8-4470-9fce-7bed7e7ab48c",
  "tool_use_result": {
    "stdout": "AGENTS.md\nROADMAP.lock\nROADMAP.md\n_last_visual_review.json\nartifacts\ncheckpoints\ndecisions.lock\ndecisions.yaml\ndocs\ndream_registry.lock\ndream_registry.yaml\ndream_registry.yaml.bak\nexperiment_plan.lock\nexperiment_plan.yaml\nliterature_map.yaml\nlogs\nmemory.md\nmistakes.lock\nmistakes.yaml\npaper\npaper_framing.md\npaper_provenance.lock\npaper_provenance.yaml\nregistry.lock\nregistry.yaml\nreport.md\nscripts\nsrc\nstudy_status.lock\ntask_context\nwriting_plan.yaml",
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ry4VfvEw5hJCdbbCxXSifa`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "e9ac9d34-bc85-4018-ba68-001d9d6f4acc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0115V2T4xDvHxkiDvmEWeA2d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16473,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16473
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28649
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-21T16:38:21.379Z_

<details><summary>↩ Tool result · `toolu_01Ry4VfvEw5hJCdbbCxXSifa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\n\\n## Target Venue\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\n- Title: \\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\"\\n\\n## Core Insight (D065 revised)\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\n\\n## Headline Metrics\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\n\\n## Core Claims (3 claims, D061)\\n\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\n\\n### C2: Conditioning-magnitude interaction — first systematic study\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\n\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\"recognizes\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\n\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\n\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\n\\n**信号验证结果 (D076)**:\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\n\\n**确定的架构**:\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\"困难步\\\"）\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\"简单步\\\"）\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\n\\n**Phase 2 结果 (Object)**:\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\n- Spatial 跨 benchmark 验证完成\\n\\n**对论文 framing 的影响**:\\n- 从纯 analysis paper 升级为 analysis + method paper\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\n- K=10 固定推理保留为 oracle upper bound\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\n\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\n\\n**D088 Learned Uncertainty Head — NO-GO**:\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\n\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\n\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\n\\n**对论文影响 (D091)**:\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\n\\n## Story Spine\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVL\\n\\n... [截断: 省略 14168 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 26168, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "ee169e09-9470-4c6a-8f2a-ac97ed269460",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — acr-vla-conformal-refinement\\\\n\\\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\\\n\\\\n## Target Venue\\\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\\\n- Title: \\\\\\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\\\\\"\\\\n\\\\n## Core Insight (D065 revised)\\\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\\\n\\\\n## Headline Metrics\\\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\\\n\\\\n## Core Claims (3 claims, D061)\\\\n\\\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\\\n\\\\n### C2: Conditioning-magnitude interaction — first systematic study\\\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\\\n\\\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\\\\\"recognizes\\\\\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\\\n\\\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\\\n\\\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\\\n\\\\n**信号验证结果 (D076)**:\\\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\\\n\\\\n**确定的架构**:\\\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\\\\\"困难步\\\\\\\"）\\\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\\\\\"简单步\\\\\\\"）\\\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\\\n\\\\n**Phase 2 结果 (Object)**:\\\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\\\n- Spatial 跨 benchmark 验证完成\\\\n\\\\n**对论文 framing 的影响**:\\\\n- 从纯 analysis paper 升级为 analysis + method paper\\\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\\\n- K=10 固定推理保留为 oracle upper bound\\\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\\\n\\\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\\\n\\\\n**D088 Learned Uncertainty Head — NO-GO**:\\\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\\\n\\\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\\\n\\\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\\\n\\\\n**对论文影响 (D091)**:\\\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\\\n\\\\n## Story Spine\\\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVL\\\\n\\\\n... [截断: 省略 14168 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 26168, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\n\\n## Target Venue\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\n- Title: \\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\"\\n\\n## Core Insight (D065 revised)\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\n\\n## Headline Metrics\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\n\\n## Core Claims (3 claims, D061)\\n\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\n\\n### C2: Conditioning-magnitude interaction — first systematic study\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\n\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\"recognizes\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\n\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\n\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\n\\n**信号验证结果 (D076)**:\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\n\\n**确定的架构**:\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\"困难步\\\"）\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\"简单步\\\"）\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\n\\n**Phase 2 结果 (Object)**:\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\n- Spatial 跨 benchmark 验证完成\\n\\n**对论文 framing 的影响**:\\n- 从纯 analysis paper 升级为 analysis + method paper\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\n- K=10 固定推理保留为 oracle upper bound\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\n\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\n\\n**D088 Learned Uncertainty Head — NO-GO**:\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\n\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\n\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\n\\n**对论文影响 (D091)**:\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\n\\n## Story Spine\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVL\\n\\n... [截断: 省略 14168 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 26168, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01AgLwA12PwJneE1Bo19Ersq`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "4ce43c84-bd5e-4a62-bdb7-994e57efc92f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01G2wkjheZQJeowtxu1tVJ51",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6963,
      "cache_read_input_tokens": 32807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6963
      },
      "output_tokens": 48,
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

_source line 13 · 2026-05-21T16:38:26.548Z_

<details><summary>↩ Tool result · `toolu_01AgLwA12PwJneE1Bo19Ersq`</summary>

```text
figure_plan.md
outline.md
sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "9df5c854-a807-42cd-adc5-7ddcea7d7059",
  "tool_use_result": {
    "stdout": "figure_plan.md\noutline.md\nsections",
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KPgUAm8rf6yhLSQACsvyzG`</summary>

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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "d7f7b1f1-1717-46fa-a520-1fe871b8b11a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01G2wkjheZQJeowtxu1tVJ51",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6963,
      "cache_read_input_tokens": 32807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6963
      },
      "output_tokens": 48,
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

_source line 15 · 2026-05-21T16:38:26.838Z_

<details><summary>↩ Tool result · `toolu_01KPgUAm8rf6yhLSQACsvyzG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\n\\n## Target Venue\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\n- Title: \\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\"\\n\\n## Core Insight (D065 revised)\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\n\\n## Headline Metrics\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\n\\n## Core Claims (3 claims, D061)\\n\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\n\\n### C2: Conditioning-magnitude interaction — first systematic study\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\n\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\"recognizes\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\n\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\n\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\n\\n**信号验证结果 (D076)**:\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\n\\n**确定的架构**:\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\"困难步\\\"）\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\"简单步\\\"）\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\n\\n**Phase 2 结果 (Object)**:\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\n- Spatial 跨 benchmark 验证完成\\n\\n**对论文 framing 的影响**:\\n- 从纯 analysis paper 升级为 analysis + method paper\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\n- K=10 固定推理保留为 oracle upper bound\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\n\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\n\\n**D088 Learned Uncertainty Head — NO-GO**:\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\n\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\n\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\n\\n**对论文影响 (D091)**:\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\n\\n## Story Spine\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVLA: UQ; SC-VLA: residual RL) address adjacent problems.\\n- **Our angle**: We first dissect inference-time multi-sample correction, finding that learned correction is the active mechanism while multi-sampling is an enabling condition. These findings inform the design of an **adaptive K mechanism** that dynamically allocates compute — sampling more only when the VLA is uncertain. The conditioning-magnitude interaction and applicability boundaries further constrain safe deployment.\\n- **Headline**: \\\"Adaptive inference-time correction improves frozen VLA with avg_K << K_max. Analysis: correction is the active mechanism, not selection. Conditioning-magnitude interaction determines success vs catastrophic failure. Adaptive K achieves ~91% of fixed K=10 performance at 38% average compute (avg_K=3.8 vs K=10).\\\"\\n\\n## Competitive Landscape\\n\\n### A2C2 (D060) — Complementary, not competing\\nFrozen VLA + per-step correction within action chunks. Solves **temporal staleness** (chunk actions become outdated during execution). Our method solves **initial action quality** (improve the action before execution). Orthogonal and combinable. A2C2 trains SmolVLA from scratch (67-72% baseline) — different setting from our frozen pretrained VLA (10.8%).\\n\\n### ReconVLA — Same domain, different route\\nConformal quantile regression for UQ + OOD detection on frozen VLA. Does not perform learned correction.\\n\\n### SC-VLA / PLD — RL-based refinement\\nResidual RL per-task. Requires online training, not plug-and-play. PLD achieves 99% on LIBERO but with full fine-tuning.\\n\\n### Our positioning (D058/D061, updated D072)\\nFirst to (1) decompose inference-time VLA correction into selection vs correction contributions, (2) systematically study conditioning-magnitude interaction revealing catastrophic failure mode, (3) establish applicability boundaries across VLA architectures (stochastic vs deterministic), **(4) propose adaptive inference-time compute allocation based on per-step uncertainty — dynamically deciding K rather than fixed brute-force sampling**. The adaptive K mechanism connects to LLM inference-time compute scaling trends in embodied AI.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Absolute performance is low (16.8% on an 11% baseline)\\\"**\\n   - Response: This is frozen fine-tuned VLA with inference-time correction (VLA weights fixed during CRM training and deployment). ~53% relative improvement (+5.8pp) is significant given the frozen constraint. The contribution is the systematic analysis of when/why/how inference-time correction works, not SOTA absolute numbers. Community benchmark: A2C2 trains SmolVLA from scratch on LIBERO reaching 67-72%, a different training regime.\\n\\n2. **\\\"Method only works for weak/small VLAs\\\"**\\n   - Response: Honest analysis (C3). Correction value correlates inversely with base model quality/determinism. This is a genuine insight with practical implications: small stochastic VLAs are relevant for edge deployment, latency-constrained scenarios, and new task generalization without fine-tuning.\\n\\n3. **\\\"K=1 doesn't work, K=10 needs 10× compute\\\"**\\n   - Response: **Adaptive K (D076) directly addresses this.** Default K=2 (same latency as K=1 with batching ~170ms). K=2 pairwise L2 distance as uncertainty signal (ρ=0.9979 vs K=10 variance). High uncertainty → extend to K=10 + CRM; low uncertainty → use K=2 directly. avg_K=3.8, achieving ~91% of fixed K=10 performance (15.3% vs 16.8%). K=1 CRM failure (10.3%) is a finding: correction needs multi-sample centering. FMVD failure (ρ=0.08) is ablation evidence for why action-space signals work while ODE-space signals don't.\\n\\n4. **\\\"obs_only is just a residual MLP, where is the novelty?\\\"**\\n   - Response: Novelty is the systematic analysis, not the architecture. Architecture simplicity isolates the conditioning signal's effect. The conditioning-magnitude interaction and component decomposition are new.\\n\\n5. **\\\"Single benchmark (LIBERO-Object)\\\"**\\n   - Response: **Fully addressed with LIBERO-Spatial data.** CRM K=10 Spatial: 35.0%±1.0% (n=3) vs VLA-only 29.3%±1.7% (n=4). Paired Δ=+5.7pp (n=3), matching Object's +6pp. K=5 Spatial: 33.5% (n=2). Both Object and Spatial are in-distribution (CRM trained on all 20 tasks). LTO (D069) shows OOD limitation — honest boundary. OpenVLA v2=69% baseline (D087), CRM eval pending.\\n\\n6. **\\\"Why does per-DOF fail?\\\"**\\n   - Response: K samples in 7D action space → rank-deficient covariance → noisy directional signals. Low ε masks noise; high ε amplifies it. 3 seeds × 0% at uncapped confirms catastrophic failure.\\n\\n7. **\\\"A2C2 does K=1 correction and it works, yours doesn't\\\"**\\n   - Response (D060): A2C2 solves temporal staleness (within-chunk correction with new observations), not initial action quality. Different problem, different mechanism. Our K=1 failure is about single-sample residual correction without temporal context — complementary finding.\\n\\n8. **\\\"Why not just fine-tune the VLA?\\\"**\\n   - Response: VLA is already fine-tuned (LoRA SFT on LIBERO), but inference-time correction provides additional gains without modifying VLA weights. CRM does not modify VLA weights but requires VLA rollout cache on deployment tasks for CRM training. LTO (D069) confirms: CRM correction is task-specific — deployment tasks must be covered in CRM training data.\\n\\n## Hard Evidence (D058 corrected, M013 fixed)\\n\\n### K=10 obs_only vs argmin — LOCKED, PRIMARY (D084: excl. seed42)\\n- obs_only: seeds 43/44/45/46/47/48/51 = 16/16/16/15/20/18/17, mean=**16.8%±1.8%** (n=7). [seed42=22% excluded per D084]\\n- argmin: seeds 42/43/44/45/46/47 = 12/17/13/12/10/10, pooled 74/600 (12.3%)\\n- Statistical tests need recalculation with updated VLA-only n=8 baseline\\n\\n### Component Decomposition — LOCKED (K=10) + PRELIMINARY (K=5)\\n\\n**K=10 decomposition (LOCKED):**\\n- VLA-only (K=1): 10.8%±1.3% (n=9, seeds 42-50)\\n- Random selection (K=10): 11.67%±2.3% (n=3, seed42=13%, seed43=9%, seed44=13%). Random ≈ VLA-only (10.8%)\\n- Argmin (K=10): 12.3%±2.6% (6 seeds, 42/43/44/45/46/47)\\n- Random selection (K=10): 9.7%±1.5% (n=6). Random fails to exceed VLA-only.\\n- CRM obs_only (K=10): 16.8%±1.8% (n=7, excl. seed42 per D084)\\n- Selection effect (D064): argmin vs random = +2.6pp. \\n- Correction effect: CRM vs argmin = +4.5pp, CRM vs random = +7.1pp (sole driver)\\n- Per-seed correction margin: -1pp to +10pp (seed43: obs_only 16% < argmin 17%)\\n\\n**K=5 decomposition (n=3 argmin, n=4 random — Random K=5 DONE ✅):**\\n- Random (K=5): **10.5%±2.9%** (n=4, seed42=14%, seed43=11%, seed44=10%, seed45=7%). ⚠️ **Random K=5 < VLA-only (10.8%)** — 随机多采样有害！\\n- Argmin (K=5): 13.7%±1.2% (n=3, seed42=15%, seed43=13%, seed45=13%). seed44 running → n=4.\\n- CRM obs_only (K=5): 16.0%±2.2% (n=7)\\n- Multi-sampling effect (K=5): random - VLA-only = **-1.1pp** (HARMFUL)\\n- Selection effect (K=5): argmin - random = **+3.2pp** (rescues from random damage + adds value)\\n- Correction effect (K=5): CRM - argmin = **+2.3pp**\\n- **K-dependent decomposition insight (updated)**:\\n  - K=5: multi-sampling hurts (-1.1pp), argmin selection essential (+3.2pp), correction additive (+2.3pp)\\n  - K=10: multi-sampling neutral (random≈VLA-only), argmin marginal (+0.6pp), correction dominant (+5.3pp)\\n  - As K↑: random pick quality improves (converges to marginal) → argmin selection becomes unnecessary → correction becomes sole differentiator\\n  - **Implication for adaptive K (D072)**: naive multi-sampling is wasteful or harmful. Smart allocation (argmin centering + CRM correction, only when needed) is essential.\\n\\n**Spatial Random Selection K=10 (cross-benchmark validation ✅):**\\n- Random Selection (K=10): **29.3%** (n=3, seed42=34%, seed43=26%, seed44=28%). exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44\\n- VLA-only Spatial: 29.3%±1.7% (n=4, seed42=30%, seed43=29%, seed44=31%, seed45=27%)\\n- CRM obs_only Spatial (K=10): 34.5%±1.5%\\n- Multi-sampling effect: Random - VLA-only = **0.0pp** (neutral, same as Object pattern)\\n- Correction effect: CRM - Random = **+5.2pp** (sole driver, consistent with Object +5.8pp)\\n- **双 benchmark 一致结论**: multi-sampling alone 不产生价值（Object: random 11.67% ≈ VLA 10.8%; Spatial: random 29.3% ≈ VLA 29.3%），CRM correction 是唯一改善来源（Object +5.8pp, Spatial +5.2pp）\\n\\n### K-value Curve (D063 updated, K=5 n=7, JSON-verified)\\n- VLA-only (K=1, no CRM): 10.8%±1.3% (n=9) — the baseline reference\\n- CRM K=1 (ACCG): 10.3±1.5% (3 seeds: 42=12%, 43=9%, 44=10%) — NEGATIVE, below VLA-only\\n- CRM K=5 (obs_only): 16.0±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18])\\n- CRM K=10 (obs_only): 16.8±1.8% (n=7, excl. seed42 per D084)\\n- CRM K=20 (obs_only): 18.7%\\n- K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp.\\n\\n### Magnitude Curve (M013 corrected, updated D069) — LOCKED\\n- obs_only: ε=0.03(**15.75%±0.96%,n=4**: seed42=16%,seed44=17%,seed47=15%,seed48=15%), ε=0.05(~14%,n=5), ε=0.1(~17%,n=8), ε=0.2(17.6%,n=7), ε=0.3(~17%,n=7), default(~17%,n=5)\\n- perdof: ε=0.03(~10%,n=3), ε=0.05(~11%,n=4: seed42=14%,seed44=9%,seed45=10%,seed43=?), ε=0.1(~11%,n=7), ε=0.2(9.9%,n=7), ε=0.3(~5%,n=5), default(0%,n=6)\\n- ✅ obs_only ε=0.03 n=4 完整 (15.75%±0.96%)，error bars 可报告\\n\\n### Cross-VLA (D054, updated D087) — IN PROGRESS\\n- OpenVLA T=0.5: 8/10 actions identical, per-DOF variance <1e-30 for DOFs 0/1/3/5/6 → near-deterministic\\n- SmolVLA (0.4B, flow-matching): naturally stochastic, K=10 produces diverse candidates\\n- **OpenVLA VLA-only (D087)**: v1=0% (plan_801, 0/100 rollouts) → **v2=69%** (10 trials/task, original eval setting). v1 failure was setup/evaluation issue, not model limitation.\\n- **OpenVLA CRM (plan_802)**: CRM obs_only training complete (val_loss=0.077260, 50 epochs, obs_dim=4096). CRM eval awaiting GPU allocation on bjb2-28827 (needs 2 GPUs for 7B model).\\n- **Key question**: Does CRM correction work for near-deterministic OpenVLA? Multi-sampling may not produce diverse candidates → C3 prerequisite 1 test.\\n\\n### Latency — plan_602 Formal Profiling (RTX 4090, bjb1-18228)\\n**Sequential**:\\n- K=1: 177ms, K=5: 892ms, K=10: 1639ms, K=20: 3246ms (~165ms/K linear)\\n\\n**Batched (model inference only)**:\\n- K=1: 180ms, K=5: 182ms, K=10: 162ms, K=20: 167ms\\n- **Batched latency ~170ms independent of K** (~5.5 Hz model inference)\\n- Full pipeline (inference + scoring): ~200ms (~5 Hz)\\n\\n**CRM overhead**: 0.246ms (negligible). CRM model size: 1.8MB vs VLA 884MB.\\n**Key insight**: Batched inference eliminates K as a latency factor. K=20 batched ≈ K=1.\\n\\n⚠️ D067 earlier reported ~314ms — likely included sim step + data loading. Paper should report model inference (~170ms) or full pipeline (~200ms), clearly labeled. Both support the narrative.\\n\\n### LTO Generalization Boundary (D069) — LOCKED, NEGATIVE\\n- CRM trained on Split A (5 tasks), evaluated on 5 held-out tasks\\n- CRM+K=5: 2% (1/50) vs VLA-only: 14% (7/50)\\n- Per-task: salad_dressing 0 vs 30%, milk 0 vs 20%, orange_juice 0 vs 10%, ketchup 0 vs 0%, tomato_sauce 10 vs 10%\\n- CRM zeroes out tasks where VLA has capability → correction is task-specific, actively harmful OOD\\n- **LTO VLA-only double reproduction**: r2=14%, r3=14%, per-task identical. Baseline stable, D069 conclusion high confidence.\\n- Mechanism: CRM learns task-specific action distribution shifts (correction biases), not general quality assessment\\n- K=1 failure + LTO failure together: CRM correction = task-specific residual, needs (1) multi-sample centering AND (2) in-distribution tasks\\n- Table 1 cross-benchmark (Object+Spatial) is in-distribution: CRM training covers all 20 tasks\\n- Paper: Discussion/Limitations section, honest analysis framing\\n\\n### Spatial (cross-benchmark, in-distribution)\\n**K=10**: seed42=35%, seed44=36%, seed45=34%, seed47=32%, mean=**34.25%±1.7%** (n=4). seed43 running on bjb2-40593, seed46 被杀待重跑.\\n**K=5**: seed42=35%, seed43=32%, seed44=37%, seed45=34%, mean=**34.5%±2.1%** (n=4). K=5→K=10 仅 +0.5pp（边际递减更极端）。\\n**VLA-only baseline**: seed42=30%, seed43=29%, seed44=**31%**, seed45=**27%**. Mean=**29.3%±1.7%** (n=4). ✅ DONE.\\n**Paired K=10 improvements**: seed42 +5pp (35-30), seed44 +5pp (36-31), seed45 +7pp (34-27). Mean Δ=**+5.7pp** (n=3 paired). seed43 K=10 still running.\\n**Paired K=5 improvements**: seed42 +5pp (35-30), seed43 +3pp (32-29). Mean Δ=+4pp (n=2 paired).\\n**CRM 方差更低**: CRM K=10 std=1.0% vs VLA-only std=1.7%。CRM 在稳定性上也优于 baseline。\\n**Framing**: \\\"consistent cross-benchmark absolute improvement (+5-6pp)\\\" — 不强调 Spatial 相对改进率（19% vs Object 52%），因为 Spatial baseline 更高。\\n**Per-task pattern**: VLA-only 和 CRM 共享同一组 zero-success tasks (4/10)。CRM 改善中等难度 tasks，不修复 impossible tasks。\\n\\n## INVALIDATED Claims (do not use)\\n- ~~K=1 improves frozen VLA~~ — D050/D051: K=1 ACCG fallback 10.0%, multi-scale 10.3%, both ≈ baseline\\n- ~~CRM ranks/selects among K candidates~~ — D058: CRM is correction module, not ranking. Same argmin selection for all modes.\\n- ~~obs_only uses conformal features~~ — D058: uf_input=None for obs_only mode\\n- ~~Cross-VLA positive transfer~~ — D054: OpenVLA near-deterministic at T=0.5. D087: v2 baseline=69%, CRM training done, eval pending\\n- ~~perdof default 0% × 3 seeds~~ — M013: was 2 seeds + 1 misclassified. Corrected to 3 data points (2 full + 1 partial) all 0%.\\n\\n## Pending Evidence (cleaned D069)\\n- ~~K=5 seeds~~ → ✅ DONE, n=7\\n- K=5 argmin decomposition: seed42/43/45 ✅ DONE (13.7%±1.2%, n=3), seed44 running (~1h) → n=4. 结果：selection +2.1pp / correction +2.3pp (与 K=10 不同的分解模式)\\n- Spatial K=10: seed43/44/45 running → cross-benchmark K scaling\\n- ~~Spatial VLA-only baseline~~ → ✅ DONE n=4 (29.3%±1.7%, seed42=30%/43=29%/44=31%/45=27%). Paired Δ=+5.7pp (n=3).\\n- ~~obs_only ε=0.03~~ → ✅ DONE, n=4 (15.75%±0.96%, seed42/44/47/48)\\n- ~~LTO~~ → ✅ DONE (D069 negative)\\n- ~~K=1 CRM eval (plan_702)~~ → ✅ DONE: 10.3%±1.5% (n=3, seed42=12%/43=9%/44=10%, NEGATIVE). Below VLA-only 10.8%. Already in K-value curve.\\n- ~~Random K=5~~ → ✅ DONE n=4 (10.5%±2.9%). Random < VLA-only — multi-sampling harmful at K=5!\\n- OpenVLA CRM eval (plan_802): CRM training done (val_loss=0.077260), eval 待 bjb2-28827 GPU 释放 (standing order P2)\\n- ~~Adaptive K~~ → ✅ P50=15.3% at avg_K=3.8 LOCKED. D090 Plan A eval in progress.\\n- Cross-server reproducibility: argmin K=5 seed42 = 15%(bjb1) vs 13%(bjb2), ±2pp noise floor noted\\n\", \"total_chars\": 26168, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "f95e3496-ded8-4b41-a061-a39f93074543",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — acr-vla-conformal-refinement\\\\n\\\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\\\n\\\\n## Target Venue\\\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\\\n- Title: \\\\\\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\\\\\"\\\\n\\\\n## Core Insight (D065 revised)\\\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\\\n\\\\n## Headline Metrics\\\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\\\n\\\\n## Core Claims (3 claims, D061)\\\\n\\\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\\\n\\\\n### C2: Conditioning-magnitude interaction — first systematic study\\\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\\\n\\\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\\\\\"recognizes\\\\\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\\\n\\\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\\\n\\\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\\\n\\\\n**信号验证结果 (D076)**:\\\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\\\n\\\\n**确定的架构**:\\\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\\\\\"困难步\\\\\\\"）\\\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\\\\\"简单步\\\\\\\"）\\\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\\\n\\\\n**Phase 2 结果 (Object)**:\\\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\\\n- Spatial 跨 benchmark 验证完成\\\\n\\\\n**对论文 framing 的影响**:\\\\n- 从纯 analysis paper 升级为 analysis + method paper\\\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\\\n- K=10 固定推理保留为 oracle upper bound\\\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\\\n\\\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\\\n\\\\n**D088 Learned Uncertainty Head — NO-GO**:\\\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\\\n\\\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\\\n\\\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\\\n\\\\n**对论文影响 (D091)**:\\\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\\\n\\\\n## Story Spine\\\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVLA: UQ; SC-VLA: residual RL) address adjacent problems.\\\\n- **Our angle**: We first dissect inference-time multi-sample correction, finding that learned correction is the active mechanism while multi-sampling is an enabling condition. These findings inform the design of an **adaptive K mechanism** that dynamically allocates compute — sampling more only when the VLA is uncertain. The conditioning-magnitude interaction and applicability boundaries further constrain safe deployment.\\\\n- **Headline**: \\\\\\\"Adaptive inference-time correction improves frozen VLA with avg_K << K_max. Analysis: correction is the active mechanism, not selection. Conditioning-magnitude interaction determines success vs catastrophic failure. Adaptive K achieves ~91% of fixed K=10 performance at 38% average compute (avg_K=3.8 vs K=10).\\\\\\\"\\\\n\\\\n## Competitive Landscape\\\\n\\\\n### A2C2 (D060) — Complementary, not competing\\\\nFrozen VLA + per-step correction within action chunks. Solves **temporal staleness** (chunk actions become outdated during execution). Our method solves **initial action quality** (improve the action before execution). Orthogonal and combinable. A2C2 trains SmolVLA from scratch (67-72% baseline) — different setting from our frozen pretrained VLA (10.8%).\\\\n\\\\n### ReconVLA — Same domain, different route\\\\nConformal quantile regression for UQ + OOD detection on frozen VLA. Does not perform learned correction.\\\\n\\\\n### SC-VLA / PLD — RL-based refinement\\\\nResidual RL per-task. Requires online training, not plug-and-play. PLD achieves 99% on LIBERO but with full fine-tuning.\\\\n\\\\n### Our positioning (D058/D061, updated D072)\\\\nFirst to (1) decompose inference-time VLA correction into selection vs correction contributions, (2) systematically study conditioning-magnitude interaction revealing catastrophic failure mode, (3) establish applicability boundaries across VLA architectures (stochastic vs deterministic), **(4) propose adaptive inference-time compute allocation based on per-step uncertainty — dynamically deciding K rather than fixed brute-force sampling**. The adaptive K mechanism connects to LLM inference-time compute scaling trends in embodied AI.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"Absolute performance is low (16.8% on an 11% baseline)\\\\\\\"**\\\\n   - Response: This is frozen fine-tuned VLA with inference-time correction (VLA weights fixed during CRM training and deployment). ~53% relative improvement (+5.8pp) is significant given the frozen constraint. The contribution is the systematic analysis of when/why/how inference-time correction works, not SOTA absolute numbers. Community benchmark: A2C2 trains SmolVLA from scratch on LIBERO reaching 67-72%, a different training regime.\\\\n\\\\n2. **\\\\\\\"Method only works for weak/small VLAs\\\\\\\"**\\\\n   - Response: Honest analysis (C3). Correction value correlates inversely with base model quality/determinism. This is a genuine insight with practical implications: small stochastic VLAs are relevant for edge deployment, latency-constrained scenarios, and new task generalization without fine-tuning.\\\\n\\\\n3. **\\\\\\\"K=1 doesn't work, K=10 needs 10× compute\\\\\\\"**\\\\n   - Response: **Adaptive K (D076) directly addresses this.** Default K=2 (same latency as K=1 with batching ~170ms). K=2 pairwise L2 distance as uncertainty signal (ρ=0.9979 vs K=10 variance). High uncertainty → extend to K=10 + CRM; low uncertainty → use K=2 directly. avg_K=3.8, achieving ~91% of fixed K=10 performance (15.3% vs 16.8%). K=1 CRM failure (10.3%) is a finding: correction needs multi-sample centering. FMVD failure (ρ=0.08) is ablation evidence for why action-space signals work while ODE-space signals don't.\\\\n\\\\n4. **\\\\\\\"obs_only is just a residual MLP, where is the novelty?\\\\\\\"**\\\\n   - Response: Novelty is the systematic analysis, not the architecture. Architecture simplicity isolates the conditioning signal's effect. The conditioning-magnitude interaction and component decomposition are new.\\\\n\\\\n5. **\\\\\\\"Single benchmark (LIBERO-Object)\\\\\\\"**\\\\n   - Response: **Fully addressed with LIBERO-Spatial data.** CRM K=10 Spatial: 35.0%±1.0% (n=3) vs VLA-only 29.3%±1.7% (n=4). Paired Δ=+5.7pp (n=3), matching Object's +6pp. K=5 Spatial: 33.5% (n=2). Both Object and Spatial are in-distribution (CRM trained on all 20 tasks). LTO (D069) shows OOD limitation — honest boundary. OpenVLA v2=69% baseline (D087), CRM eval pending.\\\\n\\\\n6. **\\\\\\\"Why does per-DOF fail?\\\\\\\"**\\\\n   - Response: K samples in 7D action space → rank-deficient covariance → noisy directional signals. Low ε masks noise; high ε amplifies it. 3 seeds × 0% at uncapped confirms catastrophic failure.\\\\n\\\\n7. **\\\\\\\"A2C2 does K=1 correction and it works, yours doesn't\\\\\\\"**\\\\n   - Response (D060): A2C2 solves temporal staleness (within-chunk correction with new observations), not initial action quality. Different problem, different mechanism. Our K=1 failure is about single-sample residual correction without temporal context — complementary finding.\\\\n\\\\n8. **\\\\\\\"Why not just fine-tune the VLA?\\\\\\\"**\\\\n   - Response: VLA is already fine-tuned (LoRA SFT on LIBERO), but inference-time correction provides additional gains without modifying VLA weights. CRM does not modify VLA weights but requires VLA rollout cache on deployment tasks for CRM training. LTO (D069) confirms: CRM correction is task-specific — deployment tasks must be covered in CRM training data.\\\\n\\\\n## Hard Evidence (D058 corrected, M013 fixed)\\\\n\\\\n### K=10 obs_only vs argmin — LOCKED, PRIMARY (D084: excl. seed42)\\\\n- obs_only: seeds 43/44/45/46/47/48/51 = 16/16/16/15/20/18/17, mean=**16.8%±1.8%** (n=7). [seed42=22% excluded per D084]\\\\n- argmin: seeds 42/43/44/45/46/47 = 12/17/13/12/10/10, pooled 74/600 (12.3%)\\\\n- Statistical tests need recalculation with updated VLA-only n=8 baseline\\\\n\\\\n### Component Decomposition — LOCKED (K=10) + PRELIMINARY (K=5)\\\\n\\\\n**K=10 decomposition (LOCKED):**\\\\n- VLA-only (K=1): 10.8%±1.3% (n=9, seeds 42-50)\\\\n- Random selection (K=10): 11.67%±2.3% (n=3, seed42=13%, seed43=9%, seed44=13%). Random ≈ VLA-only (10.8%)\\\\n- Argmin (K=10): 12.3%±2.6% (6 seeds, 42/43/44/45/46/47)\\\\n- Random selection (K=10): 9.7%±1.5% (n=6). Random fails to exceed VLA-only.\\\\n- CRM obs_only (K=10): 16.8%±1.8% (n=7, excl. seed42 per D084)\\\\n- Selection effect (D064): argmin vs random = +2.6pp. \\\\n- Correction effect: CRM vs argmin = +4.5pp, CRM vs random = +7.1pp (sole driver)\\\\n- Per-seed correction margin: -1pp to +10pp (seed43: obs_only 16% < argmin 17%)\\\\n\\\\n**K=5 decomposition (n=3 argmin, n=4 random — Random K=5 DONE ✅):**\\\\n- Random (K=5): **10.5%±2.9%** (n=4, seed42=14%, seed43=11%, seed44=10%, seed45=7%). ⚠️ **Random K=5 < VLA-only (10.8%)** — 随机多采样有害！\\\\n- Argmin (K=5): 13.7%±1.2% (n=3, seed42=15%, seed43=13%, seed45=13%). seed44 running → n=4.\\\\n- CRM obs_only (K=5): 16.0%±2.2% (n=7)\\\\n- Multi-sampling effect (K=5): random - VLA-only = **-1.1pp** (HARMFUL)\\\\n- Selection effect (K=5): argmin - random = **+3.2pp** (rescues from random damage + adds value)\\\\n- Correction effect (K=5): CRM - argmin = **+2.3pp**\\\\n- **K-dependent decomposition insight (updated)**:\\\\n  - K=5: multi-sampling hurts (-1.1pp), argmin selection essential (+3.2pp), correction additive (+2.3pp)\\\\n  - K=10: multi-sampling neutral (random≈VLA-only), argmin marginal (+0.6pp), correction dominant (+5.3pp)\\\\n  - As K↑: random pick quality improves (converges to marginal) → argmin selection becomes unnecessary → correction becomes sole differentiator\\\\n  - **Implication for adaptive K (D072)**: naive multi-sampling is wasteful or harmful. Smart allocation (argmin centering + CRM correction, only when needed) is essential.\\\\n\\\\n**Spatial Random Selection K=10 (cross-benchmark validation ✅):**\\\\n- Random Selection (K=10): **29.3%** (n=3, seed42=34%, seed43=26%, seed44=28%). exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44\\\\n- VLA-only Spatial: 29.3%±1.7% (n=4, seed42=30%, seed43=29%, seed44=31%, seed45=27%)\\\\n- CRM obs_only Spatial (K=10): 34.5%±1.5%\\\\n- Multi-sampling effect: Random - VLA-only = **0.0pp** (neutral, same as Object pattern)\\\\n- Correction effect: CRM - Random = **+5.2pp** (sole driver, consistent with Object +5.8pp)\\\\n- **双 benchmark 一致结论**: multi-sampling alone 不产生价值（Object: random 11.67% ≈ VLA 10.8%; Spatial: random 29.3% ≈ VLA 29.3%），CRM correction 是唯一改善来源（Object +5.8pp, Spatial +5.2pp）\\\\n\\\\n### K-value Curve (D063 updated, K=5 n=7, JSON-verified)\\\\n- VLA-only (K=1, no CRM): 10.8%±1.3% (n=9) — the baseline reference\\\\n- CRM K=1 (ACCG): 10.3±1.5% (3 seeds: 42=12%, 43=9%, 44=10%) — NEGATIVE, below VLA-only\\\\n- CRM K=5 (obs_only): 16.0±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18])\\\\n- CRM K=10 (obs_only): 16.8±1.8% (n=7, excl. seed42 per D084)\\\\n- CRM K=20 (obs_only): 18.7%\\\\n- K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp.\\\\n\\\\n### Magnitude Curve (M013 corrected, updated D069) — LOCKED\\\\n- obs_only: ε=0.03(**15.75%±0.96%,n=4**: seed42=16%,seed44=17%,seed47=15%,seed48=15%), ε=0.05(~14%,n=5), ε=0.1(~17%,n=8), ε=0.2(17.6%,n=7), ε=0.3(~17%,n=7), default(~17%,n=5)\\\\n- perdof: ε=0.03(~10%,n=3), ε=0.05(~11%,n=4: seed42=14%,seed44=9%,seed45=10%,seed43=?), ε=0.1(~11%,n=7), ε=0.2(9.9%,n=7), ε=0.3(~5%,n=5), default(0%,n=6)\\\\n- ✅ obs_only ε=0.03 n=4 完整 (15.75%±0.96%)，error bars 可报告\\\\n\\\\n### Cross-VLA (D054, updated D087) — IN PROGRESS\\\\n- OpenVLA T=0.5: 8/10 actions identical, per-DOF variance <1e-30 for DOFs 0/1/3/5/6 → near-deterministic\\\\n- SmolVLA (0.4B, flow-matching): naturally stochastic, K=10 produces diverse candidates\\\\n- **OpenVLA VLA-only (D087)**: v1=0% (plan_801, 0/100 rollouts) → **v2=69%** (10 trials/task, original eval setting). v1 failure was setup/evaluation issue, not model limitation.\\\\n- **OpenVLA CRM (plan_802)**: CRM obs_only training complete (val_loss=0.077260, 50 epochs, obs_dim=4096). CRM eval awaiting GPU allocation on bjb2-28827 (needs 2 GPUs for 7B model).\\\\n- **Key question**: Does CRM correction work for near-deterministic OpenVLA? Multi-sampling may not produce diverse candidates → C3 prerequisite 1 test.\\\\n\\\\n### Latency — plan_602 Formal Profiling (RTX 4090, bjb1-18228)\\\\n**Sequential**:\\\\n- K=1: 177ms, K=5: 892ms, K=10: 1639ms, K=20: 3246ms (~165ms/K linear)\\\\n\\\\n**Batched (model inference only)**:\\\\n- K=1: 180ms, K=5: 182ms, K=10: 162ms, K=20: 167ms\\\\n- **Batched latency ~170ms independent of K** (~5.5 Hz model inference)\\\\n- Full pipeline (inference + scoring): ~200ms (~5 Hz)\\\\n\\\\n**CRM overhead**: 0.246ms (negligible). CRM model size: 1.8MB vs VLA 884MB.\\\\n**Key insight**: Batched inference eliminates K as a latency factor. K=20 batched ≈ K=1.\\\\n\\\\n⚠️ D067 earlier reported ~314ms — likely included sim step + data loading. Paper should report model inference (~170ms) or full pipeline (~200ms), clearly labeled. Both support the narrative.\\\\n\\\\n### LTO Generalization Boundary (D069) — LOCKED, NEGATIVE\\\\n- CRM trained on Split A (5 tasks), evaluated on 5 held-out tasks\\\\n- CRM+K=5: 2% (1/50) vs VLA-only: 14% (7/50)\\\\n- Per-task: salad_dressing 0 vs 30%, milk 0 vs 20%, orange_juice 0 vs 10%, ketchup 0 vs 0%, tomato_sauce 10 vs 10%\\\\n- CRM zeroes out tasks where VLA has capability → correction is task-specific, actively harmful OOD\\\\n- **LTO VLA-only double reproduction**: r2=14%, r3=14%, per-task identical. Baseline stable, D069 conclusion high confidence.\\\\n- Mechanism: CRM learns task-specific action distribution shifts (correction biases), not general quality assessment\\\\n- K=1 failure + LTO failure together: CRM correction = task-specific residual, needs (1) multi-sample centering AND (2) in-distribution tasks\\\\n- Table 1 cross-benchmark (Object+Spatial) is in-distribution: CRM training covers all 20 tasks\\\\n- Paper: Discussion/Limitations section, honest analysis framing\\\\n\\\\n### Spatial (cross-benchmark, in-distribution)\\\\n**K=10**: seed42=35%, seed44=36%, seed45=34%, seed47=32%, mean=**34.25%±1.7%** (n=4). seed43 running on bjb2-40593, seed46 被杀待重跑.\\\\n**K=5**: seed42=35%, seed43=32%, seed44=37%, seed45=34%, mean=**34.5%±2.1%** (n=4). K=5→K=10 仅 +0.5pp（边际递减更极端）。\\\\n**VLA-only baseline**: seed42=30%, seed43=29%, seed44=**31%**, seed45=**27%**. Mean=**29.3%±1.7%** (n=4). ✅ DONE.\\\\n**Paired K=10 improvements**: seed42 +5pp (35-30), seed44 +5pp (36-31), seed45 +7pp (34-27). Mean Δ=**+5.7pp** (n=3 paired). seed43 K=10 still running.\\\\n**Paired K=5 improvements**: seed42 +5pp (35-30), seed43 +3pp (32-29). Mean Δ=+4pp (n=2 paired).\\\\n**CRM 方差更低**: CRM K=10 std=1.0% vs VLA-only std=1.7%。CRM 在稳定性上也优于 baseline。\\\\n**Framing**: \\\\\\\"consistent cross-benchmark absolute improvement (+5-6pp)\\\\\\\" — 不强调 Spatial 相对改进率（19% vs Object 52%），因为 Spatial baseline 更高。\\\\n**Per-task pattern**: VLA-only 和 CRM 共享同一组 zero-success tasks (4/10)。CRM 改善中等难度 tasks，不修复 impossible tasks。\\\\n\\\\n## INVALIDATED Claims (do not use)\\\\n- ~~K=1 improves frozen VLA~~ — D050/D051: K=1 ACCG fallback 10.0%, multi-scale 10.3%, both ≈ baseline\\\\n- ~~CRM ranks/selects among K candidates~~ — D058: CRM is correction module, not ranking. Same argmin selection for all modes.\\\\n- ~~obs_only uses conformal features~~ — D058: uf_input=None for obs_only mode\\\\n- ~~Cross-VLA positive transfer~~ — D054: OpenVLA near-deterministic at T=0.5. D087: v2 baseline=69%, CRM training done, eval pending\\\\n- ~~perdof default 0% × 3 seeds~~ — M013: was 2 seeds + 1 misclassified. Corrected to 3 data points (2 full + 1 partial) all 0%.\\\\n\\\\n## Pending Evidence (cleaned D069)\\\\n- ~~K=5 seeds~~ → ✅ DONE, n=7\\\\n- K=5 argmin decomposition: seed42/43/45 ✅ DONE (13.7%±1.2%, n=3), seed44 running (~1h) → n=4. 结果：selection +2.1pp / correction +2.3pp (与 K=10 不同的分解模式)\\\\n- Spatial K=10: seed43/44/45 running → cross-benchmark K scaling\\\\n- ~~Spatial VLA-only baseline~~ → ✅ DONE n=4 (29.3%±1.7%, seed42=30%/43=29%/44=31%/45=27%). Paired Δ=+5.7pp (n=3).\\\\n- ~~obs_only ε=0.03~~ → ✅ DONE, n=4 (15.75%±0.96%, seed42/44/47/48)\\\\n- ~~LTO~~ → ✅ DONE (D069 negative)\\\\n- ~~K=1 CRM eval (plan_702)~~ → ✅ DONE: 10.3%±1.5% (n=3, seed42=12%/43=9%/44=10%, NEGATIVE). Below VLA-only 10.8%. Already in K-value curve.\\\\n- ~~Random K=5~~ → ✅ DONE n=4 (10.5%±2.9%). Random < VLA-only — multi-sampling harmful at K=5!\\\\n- OpenVLA CRM eval (plan_802): CRM training done (val_loss=0.077260), eval 待 bjb2-28827 GPU 释放 (standing order P2)\\\\n- ~~Adaptive K~~ → ✅ P50=15.3% at avg_K=3.8 LOCKED. D090 Plan A eval in progress.\\\\n- Cross-server reproducibility: argmin K=5 seed42 = 15%(bjb1) vs 13%(bjb2), ±2pp noise floor noted\\\\n\\\", \\\"total_chars\\\": 26168, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度\\n\\n## Target Venue\\n- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)\\n- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)\\n- Title: \\\"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\\\"\\n\\n## Core Insight (D065 revised)\\nLearned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).\\n\\n## Headline Metrics\\n- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; JSON-verified) vs VLA-only 10.8%±1.3% (n=9). +4.4pp / ~38% relative. Mann-Whitney U=34.5, rank-biserial r=0.97 (near-perfect separation, seed47=13 ties VLA seed46=13). K=5 vs K=10 primary 待用户确认（K=10 推荐）。\\n- **K=10 CRM obs_only (scaling upper bound)**: 16.8%±1.8% (n=7, excl. seed42 per D084) vs VLA-only 10.8%. +5.8pp / ~53% relative. K=5→K=10 +1.3pp（边际递减）。Statistical tests need recalculation.\\n- **Component decomposition (D064/D070, n=4 update)**: K=10: selection ≈ 0 (argmin 12.3% vs random 11.67%), correction +5.3pp (sole driver). K=5 (n=4): **random 10.5% < VLA-only 11.3%** — 多采样有害！argmin 13.0%±1.6%, selection +1.4pp (32%, borderline), **correction +3.0pp (68%, dominant)**. Correction dominates at ALL K: 68% at K=5, ~100% at K=10. **Cross-benchmark**: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3% — multi-sampling无益 pattern consistent across both benchmarks (exp_ids: eval-random-selection-spatial-seed42-r2/seed43/seed44).\\n- **K-value scaling (D063)**: VLA-only 10.8% → CRM K=1(10.3%±1.5%,n=3,NEGATIVE) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%±1.8%,n=7) → CRM K=20(18.7%). K=5 captures ~78% of K=10 benefit over VLA-only. 收益集中在 K=1→K=5 (+5.2pp)，K=5→K=10 +1.3pp（边际递减）\\n- **Magnitude robustness**: obs_only stable 13.4-16.8% all ε (range corrected per Paper Agent audit); perdof collapse 14%→11%→9.9%→4.7%→0%\\n- **Latency (RTX 4090, plan_602 formal)**: ~170ms model inference for all K (~5.5 Hz), full pipeline ~200ms (~5 Hz). CRM overhead 0.246ms, CRM size 1.8MB vs VLA 884MB. Batched inference eliminates K as latency factor.\\n- **Spatial (cross-benchmark, in-distribution)**: K=10 34.5%±1.5% (n=9) vs VLA-only 29.3%±1.7% (n=4). Δ=+5.2pp. Cross-benchmark improvement consistent with Object +5.8pp。Random Selection Spatial K=10: 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%) ≈ VLA-only — correction is sole driver on Spatial too.\\n- **OOD cross-suite (CRM trained on Object+Spatial only)**:\\n  - Goal (OOD, n=4): 67.0% vs VLA-only 69.25%, Δ=-2.25pp, **p=0.42 不显著** — 统计中性。seed44=-9pp 是 outlier，其余 [-2,0,+2]。\\n  - Long (OOD, n=4): 17.5% vs VLA-only 13.25%(paired), Δ=+4.25pp — 正面但改善集中于 microwave task\\n  - LTO (within-suite OOD, D069): 2% vs 14%, Δ=-12pp — **灾难性**\\n  - **OOD 图景**: cross-suite OOD 中性(Goal)到正面(Long)，within-suite held-out 灾难性(LTO)。CRM 校正模式可跨 suite 迁移但不能迁移到同 suite 未见 task。\\n- **Cross-VLA boundary**: OpenVLA v1=0% → **v2=69%** (D087, 10 trials/task). CRM obs_only training complete (plan_802, val_loss=0.077260). CRM eval pending GPU. SmolVLA naturally stochastic; OpenVLA near-deterministic at T=0.5 (8/10 identical actions).\\n- **Adaptive K (D076→D090)**: K=2 L2 pairwise distance ρ=0.9979 vs K=10 variance. **P50 threshold: 15.3% SR at avg_K=3.8 (~91% of fixed K=10, 38% compute)**. D088 Learned Uncertainty Head NO-GO (mean 12.0% < VLA-only). D090 Plan A (K=2 conformal + selective CRM) in progress.\\n\\n## Core Claims (3 claims, D061)\\n\\n### C1: Dissecting inference-time correction — correction is active mechanism, multi-sampling is enabling condition\\n- K VLA samples → argmin(L2 to mean) → learned MLP residual correction with observation features\\n- 16.8%±1.8% vs 10.8%±1.3% VLA-only (n=7 vs n=9, excl. seed42 per D084; statistical tests need recalculation with updated data); vs argmin 12.3%\\n- Component decomposition (D064): argmin selection ≈ random (12.3% vs 11.67%, n=3, not significant). CRM correction +5.2pp over argmin, +5.8pp over random. Multi-sampling alone (random K=10) ≈ VLA-only — correction is the active mechanism\\n- **Spatial cross-benchmark validation**: Random Selection Spatial K=10 = 29.3% (n=3, seed42=34%, seed43=26%, seed44=28%; exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44) ≈ VLA-only Spatial 29.3% (n=4). CRM K=10 Spatial: 34.5% → correction Δ=+5.2pp. Pattern consistent with Object: multi-sampling alone ≈ VLA-only on both benchmarks, correction is the sole driver (+5.8pp Object, +5.2pp Spatial)\\n- K-value scaling (D063): CRM K=1(10.3%,n=3) → CRM K=5(15.5%,n=7) → CRM K=10(16.8%,n=7). VLA-only baseline = 10.8% (K=1, no CRM). K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp\\n- CRM K=1 does NOT work (10.3% < VLA-only 10.8%) — correction without multi-sample centering is harmful. Same CRM trained on K=10 data; K=1 failure = input distribution shift outside bounded correction radius\\n- CRM is a correction module (not selection/ranking): obs_only CRM does NOT use conformal features (D058)\\n- Evidence: Table 1 (component decomposition), Figure 3 (K-value curve)\\n\\n### C2: Conditioning-magnitude interaction — first systematic study\\n- Same CRM architecture, same training, only conditioning features differ → stable vs catastrophic failure\\n- obs_only (observation features only): 13.4-16.8% stable across all ε (n=1-7 per point, range corrected)\\n- perdof (per-DOF conformal features): 14%→11%→9.9%→4.7%→0% dose-response collapse\\n- perdof default (uncapped): 0% × 5 data points (catastrophic collapse, all seeds consistent)\\n- Root cause: rank-deficient covariance in high-D action space → noisy directional signals amplified by magnitude\\n- Practical takeaway: bounded magnitude + observation features = necessary conditions for safe correction\\n- Evidence: Figure 2 (magnitude curves), Section analysis\\n\\n### C3: Applicability boundaries — two prerequisites + unified failure framework (updated with OOD cross-suite)\\n- **Prerequisite 1: VLA diversity** — stochastic multi-sampling → action diversity across K samples. OpenVLA (7B, tokenized): T=0.5 produces 8/10 identical actions, near-deterministic (D087: v2 baseline=69%, CRM eval pending to test if correction works despite low diversity). SmolVLA (0.4B, flow-matching): naturally stochastic.\\n- **Prerequisite 2: Task proximity in CRM training data** — CRM learns task-specific correction biases. OOD behavior is **proximity-dependent**:\\n  - Near-OOD (within-suite held-out, LTO): same manipulation structure, different objects/goals → CRM \\\"recognizes\\\" context but correction direction is wrong → **adversarial** (-12pp, 2% vs 14%)\\n  - Far-OOD (cross-suite, Goal/Long): different observation distribution → correction signal naturally decays → **neutral** (Goal -1.6pp p=0.46) or **primitive-level transfer** (Long +3.3pp p=0.046, driven by microwave task sharing pick-and-place primitives with training data)\\n- **Unified failure framework** — CRM correction = bounded task-specific residual, sensitive to three distribution shifts:\\n  - Input shift (K=1): single sample ≠ multi-sample mean → correction points wrong direction (10.3% < baseline)\\n  - Task shift (proximity-dependent): near-OOD → adversarial perturbation (LTO -12pp); far-OOD → null operation (Goal ±2pp) or primitive transfer (Long +3.3pp)\\n  - Feature shift (perdof, C2): noisy conformal signals amplified by magnitude → catastrophic collapse (→0%)\\n- This is the central boundary analysis — three failure modes with mechanistic explanations. Near-OOD more dangerous than far-OOD parallels ML adversarial robustness literature.\\n- Evidence: Figure 4 (action diversity), LTO data, Goal/Long cross-suite data, magnitude curves (C2)\\n- **Long per-task breakdown required**: microwave task contributes majority of improvement. Report overall SR (honest) + per-task table. Discuss primitive-level transfer mechanism.\\n\\n## D072/D076: Adaptive K — K=2 L2 Probe 机制（用户硬要求，已验证）\\n\\n⚠️ **固定 K=10 暴力多推理不可接受**。Adaptive K 信号已验证：K=2 L2 pairwise distance。\\n\\n**信号验证结果 (D076)**:\\n- **K=2 L2 vs K=10 variance: ρ=0.9979** — 近乎完美替代，2 次推理预测 10 次推理的不确定性\\n- FMVD (flow turbulence): ρ=0.0825 → NO-GO (D075). 测量不同维度的不确定性，与 action variance 无关\\n- K=2 L2 vs FMVD: ρ=0.09 — 两个信号完全独立\\n\\n**确定的架构**:\\n- 默认 K=2（batched推理，延迟=K=1 ~170ms）\\n- 计算 K=2 pairwise L2 distance 作为 per-step 不确定性信号\\n- L2 > τ → 扩展到 K=10 + argmin + CRM obs_only 校正（\\\"困难步\\\"）\\n- L2 ≤ τ → K=2 均值，不过 CRM（\\\"简单步\\\"）\\n- 阈值 τ 从校准数据 percentile 选取：P25=0.055, P50=0.075, P75=0.099, P90=0.127\\n\\n**Phase 2 结果 (Object)**:\\n- **P50 (τ=0.075): 15.3% SR at avg_K=3.8 — ~91% of K=10 (16.8%) at 38% compute** ← 推荐默认\\n- P25/P75/P90 阈值 sweep 完成，Pareto 曲线可用\\n- Spatial 跨 benchmark 验证完成\\n\\n**对论文 framing 的影响**:\\n- 从纯 analysis paper 升级为 analysis + method paper\\n- 分析 (correction > selection, magnitude interaction, boundaries) 作为 FOUNDATION → 指导 adaptive 机制设计\\n- K=10 固定推理保留为 oracle upper bound\\n- FMVD NO-GO 作为 negative result / ablation（ODE-space 信号 vs action-space 信号）\\n- 新增贡献 C4：adaptive inference-time compute allocation for VLA\\n\\n## D088→D090: Adaptive K 方法路径（2026-05-20）\\n\\n**D088 Learned Uncertainty Head — NO-GO**:\\n- 方案 B: 3-layer MLP (960→16→16→1, 15,665 params) 在 VLA-expert deviation 上训练，AUC=0.8131, F1=0.7674, τ=0.42\\n- 3 seed eval: mean SR=12.0% < VLA-only baseline (10.8%→14%) — 方法有害\\n- 根因: avg_k≈1.0, uncertainty head 几乎从不触发 CRM correction\\n- 结论: offline uncertainty classification 不如 online multi-sample divergence\\n\\n**D090 Plan A: K=2 Conformal + Selective CRM — IN PROGRESS**:\\n- K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-centroid + CRM correction; else: argmin-to-centroid only\\n- 与 D076 adaptive K 的区别: Plan A 在 K=2 就做 CRM correction（不扩展到 K=10），更实用但可能牺牲性能\\n- 代码已实现 (`adaptive_conformal_crm` mode in evaluate.py)，3 seed eval 待 GPU 释放部署\\n- Safety net: Adaptive K P50 已有 15.3% 结果可用\\n\\n**方案 C (Action Distribution Geometry)**: 备选，如 Plan A 也失败则启用\\n\\n**对论文影响 (D091)**:\\n- 核心 claims (C1-C3) 不受影响 — D088 作为 rejected alternative 写入 Discussion\\n- D090 成功: 替代 D076 adaptive K 作为 method contribution\\n- D090 失败: D076 adaptive K P50=15.3% 结果作为 safety net\\n\\n## Story Spine\\n- **Problem**: Frozen VLA deployment with a lightweight learned correction module can improve success rates — but fixed multi-sampling (K=10) is computationally wasteful. When does correction actually help, and can we allocate inference-time compute adaptively?\\n- **Gap**: No systematic study of (1) what drives effective learned corrections for VLA, (2) how to adaptively allocate inference-time compute based on per-step uncertainty, (3) when multi-sample correction helps vs fails across VLA architectures. Existing methods (A2C2: temporal correction; ReconVLA: UQ; SC-VLA: residual RL) address adjacent problems.\\n- **Our angle**: We first dissect inference-time multi-sample correction, finding that learned correction is the active mechanism while multi-sampling is an enabling condition. These findings inform the design of an **adaptive K mechanism** that dynamically allocates compute — sampling more only when the VLA is uncertain. The conditioning-magnitude interaction and applicability boundaries further constrain safe deployment.\\n- **Headline**: \\\"Adaptive inference-time correction improves frozen VLA with avg_K << K_max. Analysis: correction is the active mechanism, not selection. Conditioning-magnitude interaction determines success vs catastrophic failure. Adaptive K achieves ~91% of fixed K=10 performance at 38% average compute (avg_K=3.8 vs K=10).\\\"\\n\\n## Competitive Landscape\\n\\n### A2C2 (D060) — Complementary, not competing\\nFrozen VLA + per-step correction within action chunks. Solves **temporal staleness** (chunk actions become outdated during execution). Our method solves **initial action quality** (improve the action before execution). Orthogonal and combinable. A2C2 trains SmolVLA from scratch (67-72% baseline) — different setting from our frozen pretrained VLA (10.8%).\\n\\n### ReconVLA — Same domain, different route\\nConformal quantile regression for UQ + OOD detection on frozen VLA. Does not perform learned correction.\\n\\n### SC-VLA / PLD — RL-based refinement\\nResidual RL per-task. Requires online training, not plug-and-play. PLD achieves 99% on LIBERO but with full fine-tuning.\\n\\n### Our positioning (D058/D061, updated D072)\\nFirst to (1) decompose inference-time VLA correction into selection vs correction contributions, (2) systematically study conditioning-magnitude interaction revealing catastrophic failure mode, (3) establish applicability boundaries across VLA architectures (stochastic vs deterministic), **(4) propose adaptive inference-time compute allocation based on per-step uncertainty — dynamically deciding K rather than fixed brute-force sampling**. The adaptive K mechanism connects to LLM inference-time compute scaling trends in embodied AI.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Absolute performance is low (16.8% on an 11% baseline)\\\"**\\n   - Response: This is frozen fine-tuned VLA with inference-time correction (VLA weights fixed during CRM training and deployment). ~53% relative improvement (+5.8pp) is significant given the frozen constraint. The contribution is the systematic analysis of when/why/how inference-time correction works, not SOTA absolute numbers. Community benchmark: A2C2 trains SmolVLA from scratch on LIBERO reaching 67-72%, a different training regime.\\n\\n2. **\\\"Method only works for weak/small VLAs\\\"**\\n   - Response: Honest analysis (C3). Correction value correlates inversely with base model quality/determinism. This is a genuine insight with practical implications: small stochastic VLAs are relevant for edge deployment, latency-constrained scenarios, and new task generalization without fine-tuning.\\n\\n3. **\\\"K=1 doesn't work, K=10 needs 10× compute\\\"**\\n   - Response: **Adaptive K (D076) directly addresses this.** Default K=2 (same latency as K=1 with batching ~170ms). K=2 pairwise L2 distance as uncertainty signal (ρ=0.9979 vs K=10 variance). High uncertainty → extend to K=10 + CRM; low uncertainty → use K=2 directly. avg_K=3.8, achieving ~91% of fixed K=10 performance (15.3% vs 16.8%). K=1 CRM failure (10.3%) is a finding: correction needs multi-sample centering. FMVD failure (ρ=0.08) is ablation evidence for why action-space signals work while ODE-space signals don't.\\n\\n4. **\\\"obs_only is just a residual MLP, where is the novelty?\\\"**\\n   - Response: Novelty is the systematic analysis, not the architecture. Architecture simplicity isolates the conditioning signal's effect. The conditioning-magnitude interaction and component decomposition are new.\\n\\n5. **\\\"Single benchmark (LIBERO-Object)\\\"**\\n   - Response: **Fully addressed with LIBERO-Spatial data.** CRM K=10 Spatial: 35.0%±1.0% (n=3) vs VLA-only 29.3%±1.7% (n=4). Paired Δ=+5.7pp (n=3), matching Object's +6pp. K=5 Spatial: 33.5% (n=2). Both Object and Spatial are in-distribution (CRM trained on all 20 tasks). LTO (D069) shows OOD limitation — honest boundary. OpenVLA v2=69% baseline (D087), CRM eval pending.\\n\\n6. **\\\"Why does per-DOF fail?\\\"**\\n   - Response: K samples in 7D action space → rank-deficient covariance → noisy directional signals. Low ε masks noise; high ε amplifies it. 3 seeds × 0% at uncapped confirms catastrophic failure.\\n\\n7. **\\\"A2C2 does K=1 correction and it works, yours doesn't\\\"**\\n   - Response (D060): A2C2 solves temporal staleness (within-chunk correction with new observations), not initial action quality. Different problem, different mechanism. Our K=1 failure is about single-sample residual correction without temporal context — complementary finding.\\n\\n8. **\\\"Why not just fine-tune the VLA?\\\"**\\n   - Response: VLA is already fine-tuned (LoRA SFT on LIBERO), but inference-time correction provides additional gains without modifying VLA weights. CRM does not modify VLA weights but requires VLA rollout cache on deployment tasks for CRM training. LTO (D069) confirms: CRM correction is task-specific — deployment tasks must be covered in CRM training data.\\n\\n## Hard Evidence (D058 corrected, M013 fixed)\\n\\n### K=10 obs_only vs argmin — LOCKED, PRIMARY (D084: excl. seed42)\\n- obs_only: seeds 43/44/45/46/47/48/51 = 16/16/16/15/20/18/17, mean=**16.8%±1.8%** (n=7). [seed42=22% excluded per D084]\\n- argmin: seeds 42/43/44/45/46/47 = 12/17/13/12/10/10, pooled 74/600 (12.3%)\\n- Statistical tests need recalculation with updated VLA-only n=8 baseline\\n\\n### Component Decomposition — LOCKED (K=10) + PRELIMINARY (K=5)\\n\\n**K=10 decomposition (LOCKED):**\\n- VLA-only (K=1): 10.8%±1.3% (n=9, seeds 42-50)\\n- Random selection (K=10): 11.67%±2.3% (n=3, seed42=13%, seed43=9%, seed44=13%). Random ≈ VLA-only (10.8%)\\n- Argmin (K=10): 12.3%±2.6% (6 seeds, 42/43/44/45/46/47)\\n- Random selection (K=10): 9.7%±1.5% (n=6). Random fails to exceed VLA-only.\\n- CRM obs_only (K=10): 16.8%±1.8% (n=7, excl. seed42 per D084)\\n- Selection effect (D064): argmin vs random = +2.6pp. \\n- Correction effect: CRM vs argmin = +4.5pp, CRM vs random = +7.1pp (sole driver)\\n- Per-seed correction margin: -1pp to +10pp (seed43: obs_only 16% < argmin 17%)\\n\\n**K=5 decomposition (n=3 argmin, n=4 random — Random K=5 DONE ✅):**\\n- Random (K=5): **10.5%±2.9%** (n=4, seed42=14%, seed43=11%, seed44=10%, seed45=7%). ⚠️ **Random K=5 < VLA-only (10.8%)** — 随机多采样有害！\\n- Argmin (K=5): 13.7%±1.2% (n=3, seed42=15%, seed43=13%, seed45=13%). seed44 running → n=4.\\n- CRM obs_only (K=5): 16.0%±2.2% (n=7)\\n- Multi-sampling effect (K=5): random - VLA-only = **-1.1pp** (HARMFUL)\\n- Selection effect (K=5): argmin - random = **+3.2pp** (rescues from random damage + adds value)\\n- Correction effect (K=5): CRM - argmin = **+2.3pp**\\n- **K-dependent decomposition insight (updated)**:\\n  - K=5: multi-sampling hurts (-1.1pp), argmin selection essential (+3.2pp), correction additive (+2.3pp)\\n  - K=10: multi-sampling neutral (random≈VLA-only), argmin marginal (+0.6pp), correction dominant (+5.3pp)\\n  - As K↑: random pick quality improves (converges to marginal) → argmin selection becomes unnecessary → correction becomes sole differentiator\\n  - **Implication for adaptive K (D072)**: naive multi-sampling is wasteful or harmful. Smart allocation (argmin centering + CRM correction, only when needed) is essential.\\n\\n**Spatial Random Selection K=10 (cross-benchmark validation ✅):**\\n- Random Selection (K=10): **29.3%** (n=3, seed42=34%, seed43=26%, seed44=28%). exp_ids: eval-random-selection-spatial-seed42-r2, eval-random-selection-spatial-seed43, eval-random-selection-spatial-seed44\\n- VLA-only Spatial: 29.3%±1.7% (n=4, seed42=30%, seed43=29%, seed44=31%, seed45=27%)\\n- CRM obs_only Spatial (K=10): 34.5%±1.5%\\n- Multi-sampling effect: Random - VLA-only = **0.0pp** (neutral, same as Object pattern)\\n- Correction effect: CRM - Random = **+5.2pp** (sole driver, consistent with Object +5.8pp)\\n- **双 benchmark 一致结论**: multi-sampling alone 不产生价值（Object: random 11.67% ≈ VLA 10.8%; Spatial: random 29.3% ≈ VLA 29.3%），CRM correction 是唯一改善来源（Object +5.8pp, Spatial +5.2pp）\\n\\n### K-value Curve (D063 updated, K=5 n=7, JSON-verified)\\n- VLA-only (K=1, no CRM): 10.8%±1.3% (n=9) — the baseline reference\\n- CRM K=1 (ACCG): 10.3±1.5% (3 seeds: 42=12%, 43=9%, 44=10%) — NEGATIVE, below VLA-only\\n- CRM K=5 (obs_only): 16.0±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18])\\n- CRM K=10 (obs_only): 16.8±1.8% (n=7, excl. seed42 per D084)\\n- CRM K=20 (obs_only): 18.7%\\n- K=5 captures ~78% of K=10 benefit over VLA-only. CRM K=1→K=5 +5.2pp, K=5→K=10 +1.3pp.\\n\\n### Magnitude Curve (M013 corrected, updated D069) — LOCKED\\n- obs_only: ε=0.03(**15.75%±0.96%,n=4**: seed42=16%,seed44=17%,seed47=15%,seed48=15%), ε=0.05(~14%,n=5), ε=0.1(~17%,n=8), ε=0.2(17.6%,n=7), ε=0.3(~17%,n=7), default(~17%,n=5)\\n- perdof: ε=0.03(~10%,n=3), ε=0.05(~11%,n=4: seed42=14%,seed44=9%,seed45=10%,seed43=?), ε=0.1(~11%,n=7), ε=0.2(9.9%,n=7), ε=0.3(~5%,n=5), default(0%,n=6)\\n- ✅ obs_only ε=0.03 n=4 完整 (15.75%±0.96%)，error bars 可报告\\n\\n### Cross-VLA (D054, updated D087) — IN PROGRESS\\n- OpenVLA T=0.5: 8/10 actions identical, per-DOF variance <1e-30 for DOFs 0/1/3/5/6 → near-deterministic\\n- SmolVLA (0.4B, flow-matching): naturally stochastic, K=10 produces diverse candidates\\n- **OpenVLA VLA-only (D087)**: v1=0% (plan_801, 0/100 rollouts) → **v2=69%** (10 trials/task, original eval setting). v1 failure was setup/evaluation issue, not model limitation.\\n- **OpenVLA CRM (plan_802)**: CRM obs_only training complete (val_loss=0.077260, 50 epochs, obs_dim=4096). CRM eval awaiting GPU allocation on bjb2-28827 (needs 2 GPUs for 7B model).\\n- **Key question**: Does CRM correction work for near-deterministic OpenVLA? Multi-sampling may not produce diverse candidates → C3 prerequisite 1 test.\\n\\n### Latency — plan_602 Formal Profiling (RTX 4090, bjb1-18228)\\n**Sequential**:\\n- K=1: 177ms, K=5: 892ms, K=10: 1639ms, K=20: 3246ms (~165ms/K linear)\\n\\n**Batched (model inference only)**:\\n- K=1: 180ms, K=5: 182ms, K=10: 162ms, K=20: 167ms\\n- **Batched latency ~170ms independent of K** (~5.5 Hz model inference)\\n- Full pipeline (inference + scoring): ~200ms (~5 Hz)\\n\\n**CRM overhead**: 0.246ms (negligible). CRM model size: 1.8MB vs VLA 884MB.\\n**Key insight**: Batched inference eliminates K as a latency factor. K=20 batched ≈ K=1.\\n\\n⚠️ D067 earlier reported ~314ms — likely included sim step + data loading. Paper should report model inference (~170ms) or full pipeline (~200ms), clearly labeled. Both support the narrative.\\n\\n### LTO Generalization Boundary (D069) — LOCKED, NEGATIVE\\n- CRM trained on Split A (5 tasks), evaluated on 5 held-out tasks\\n- CRM+K=5: 2% (1/50) vs VLA-only: 14% (7/50)\\n- Per-task: salad_dressing 0 vs 30%, milk 0 vs 20%, orange_juice 0 vs 10%, ketchup 0 vs 0%, tomato_sauce 10 vs 10%\\n- CRM zeroes out tasks where VLA has capability → correction is task-specific, actively harmful OOD\\n- **LTO VLA-only double reproduction**: r2=14%, r3=14%, per-task identical. Baseline stable, D069 conclusion high confidence.\\n- Mechanism: CRM learns task-specific action distribution shifts (correction biases), not general quality assessment\\n- K=1 failure + LTO failure together: CRM correction = task-specific residual, needs (1) multi-sample centering AND (2) in-distribution tasks\\n- Table 1 cross-benchmark (Object+Spatial) is in-distribution: CRM training covers all 20 tasks\\n- Paper: Discussion/Limitations section, honest analysis framing\\n\\n### Spatial (cross-benchmark, in-distribution)\\n**K=10**: seed42=35%, seed44=36%, seed45=34%, seed47=32%, mean=**34.25%±1.7%** (n=4). seed43 running on bjb2-40593, seed46 被杀待重跑.\\n**K=5**: seed42=35%, seed43=32%, seed44=37%, seed45=34%, mean=**34.5%±2.1%** (n=4). K=5→K=10 仅 +0.5pp（边际递减更极端）。\\n**VLA-only baseline**: seed42=30%, seed43=29%, seed44=**31%**, seed45=**27%**. Mean=**29.3%±1.7%** (n=4). ✅ DONE.\\n**Paired K=10 improvements**: seed42 +5pp (35-30), seed44 +5pp (36-31), seed45 +7pp (34-27). Mean Δ=**+5.7pp** (n=3 paired). seed43 K=10 still running.\\n**Paired K=5 improvements**: seed42 +5pp (35-30), seed43 +3pp (32-29). Mean Δ=+4pp (n=2 paired).\\n**CRM 方差更低**: CRM K=10 std=1.0% vs VLA-only std=1.7%。CRM 在稳定性上也优于 baseline。\\n**Framing**: \\\"consistent cross-benchmark absolute improvement (+5-6pp)\\\" — 不强调 Spatial 相对改进率（19% vs Object 52%），因为 Spatial baseline 更高。\\n**Per-task pattern**: VLA-only 和 CRM 共享同一组 zero-success tasks (4/10)。CRM 改善中等难度 tasks，不修复 impossible tasks。\\n\\n## INVALIDATED Claims (do not use)\\n- ~~K=1 improves frozen VLA~~ — D050/D051: K=1 ACCG fallback 10.0%, multi-scale 10.3%, both ≈ baseline\\n- ~~CRM ranks/selects among K candidates~~ — D058: CRM is correction module, not ranking. Same argmin selection for all modes.\\n- ~~obs_only uses conformal features~~ — D058: uf_input=None for obs_only mode\\n- ~~Cross-VLA positive transfer~~ — D054: OpenVLA near-deterministic at T=0.5. D087: v2 baseline=69%, CRM training done, eval pending\\n- ~~perdof default 0% × 3 seeds~~ — M013: was 2 seeds + 1 misclassified. Corrected to 3 data points (2 full + 1 partial) all 0%.\\n\\n## Pending Evidence (cleaned D069)\\n- ~~K=5 seeds~~ → ✅ DONE, n=7\\n- K=5 argmin decomposition: seed42/43/45 ✅ DONE (13.7%±1.2%, n=3), seed44 running (~1h) → n=4. 结果：selection +2.1pp / correction +2.3pp (与 K=10 不同的分解模式)\\n- Spatial K=10: seed43/44/45 running → cross-benchmark K scaling\\n- ~~Spatial VLA-only baseline~~ → ✅ DONE n=4 (29.3%±1.7%, seed42=30%/43=29%/44=31%/45=27%). Paired Δ=+5.7pp (n=3).\\n- ~~obs_only ε=0.03~~ → ✅ DONE, n=4 (15.75%±0.96%, seed42/44/47/48)\\n- ~~LTO~~ → ✅ DONE (D069 negative)\\n- ~~K=1 CRM eval (plan_702)~~ → ✅ DONE: 10.3%±1.5% (n=3, seed42=12%/43=9%/44=10%, NEGATIVE). Below VLA-only 10.8%. Already in K-value curve.\\n- ~~Random K=5~~ → ✅ DONE n=4 (10.5%±2.9%). Random < VLA-only — multi-sampling harmful at K=5!\\n- OpenVLA CRM eval (plan_802): CRM training done (val_loss=0.077260), eval 待 bjb2-28827 GPU 释放 (standing order P2)\\n- ~~Adaptive K~~ → ✅ P50=15.3% at avg_K=3.8 LOCKED. D090 Plan A eval in progress.\\n- Cross-server reproducibility: argmin K=5 seed42 = 15%(bjb1) vs 13%(bjb2), ±2pp noise floor noted\\n\", \"total_chars\": 26168, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_013NWAmZFgHxtZAjrgYK8v8J`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "7e38c908-586c-40dc-9157-888624c9b743",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Q7xj7QaBUR4s31Y4MswaAA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14019,
      "cache_read_input_tokens": 39770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14019
      },
      "output_tokens": 47,
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

_source line 17 · 2026-05-21T16:38:31.186Z_

<details><summary>↩ Tool result · `toolu_013NWAmZFgHxtZAjrgYK8v8J`</summary>

```text
ablation_k_sweep.md
related_work.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "4070a6a1-3417-48d1-82e0-8b87890751af",
  "tool_use_result": {
    "stdout": "ablation_k_sweep.md\nrelated_work.md",
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

_source line 18_

<details open><summary>🔧 Tool call — Glob · `toolu_0124Efdgad9CnTvq4ks3rbXL`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "2617ef1f-3680-4a19-91d4-12b51cf144fc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Q7xj7QaBUR4s31Y4MswaAA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14019,
      "cache_read_input_tokens": 39770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14019
      },
      "output_tokens": 47,
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

_source line 19 · 2026-05-21T16:38:32.181Z_

<details><summary>↩ Tool result · `toolu_0124Efdgad9CnTvq4ks3rbXL`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "53686e34-087e-472f-9bda-2da65eb0fda9",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 43,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_013uKZ9JLJoVAUVbrBvtUVrU`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "0843f194-dc0f-45c5-a778-36953e969631",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Q7xj7QaBUR4s31Y4MswaAA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14019,
      "cache_read_input_tokens": 39770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14019
      },
      "output_tokens": 47,
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

_source line 21 · 2026-05-21T16:38:33.287Z_

<details><summary>↩ Tool result · `toolu_013uKZ9JLJoVAUVbrBvtUVrU`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "d645bdec-bd49-47cd-a5af-f00e9f379bb8",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 31,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Glob · `toolu_01Xsa9m1TmkjGV9c91tm6hwV`</summary>

```json
{
  "pattern": "**/Makefile",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "bec7bf15-13d1-4ebc-b6d7-54980864274a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Q7xj7QaBUR4s31Y4MswaAA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14019,
      "cache_read_input_tokens": 39770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14019
      },
      "output_tokens": 47,
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

_source line 23 · 2026-05-21T16:38:33.822Z_

<details><summary>↩ Tool result · `toolu_01Xsa9m1TmkjGV9c91tm6hwV`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "fc8d8119-6a39-47ac-8d37-0f328e52fc1e",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 41,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "50533e9d-facc-4186-9f57-44112a075199",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0192JLWKHdZiCCLQj6oZTgrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 53789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Glob · `toolu_01N3tWpZpCRJfcp6u47k2npp`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "b19f7b89-d204-4d95-976d-85cbdbd11411",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0192JLWKHdZiCCLQj6oZTgrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 53789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 26 · 2026-05-21T16:38:37.254Z_

<details><summary>↩ Tool result · `toolu_01N3tWpZpCRJfcp6u47k2npp`</summary>

```text
docs/paper/camera_ready_template/corl_2026_template_cameraready/example.tex
docs/paper/review_template/corl_2026_template_submission/example.tex
artifacts/dream_reports/dream_20260513T015051/best/paper.tex
artifacts/dream_reports/dream_20260513T015051/median/paper.tex
artifacts/dream_reports/dream_20260513T015051/worst/paper.tex
artifacts/dream_reports/dream_20260513T023849/best/paper.tex
artifacts/dream_reports/dream_20260513T023849/median/paper.tex
artifacts/dream_reports/dream_20260513T023849/worst/paper.tex
artifacts/method_section_draft.tex
artifacts/_project/paper/method_section_draft.tex
artifacts/figures/object_benchmark_table.tex
artifacts/figures/spatial_final_table.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/related_work_80791f.tex
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/abstract_a1674b.tex
artifacts/_project/paper/sections/discussion.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_ac6246.tex
artifacts/_project/paper/introduction_scenarioC_607d8d.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/introduction_scenarioC.tex
artifacts/_project/paper/sections/introduction.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/abstract.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "6b1f428d-4622-41b2-aec0-26b9f85aca42",
  "tool_use_result": {
    "filenames": [
      "docs/paper/camera_ready_template/corl_2026_template_cameraready/example.tex",
      "docs/paper/review_template/corl_2026_template_submission/example.tex",
      "artifacts/dream_reports/dream_20260513T015051/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T015051/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T015051/worst/paper.tex",
      "artifacts/dream_reports/dream_20260513T023849/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T023849/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T023849/worst/paper.tex",
      "artifacts/method_section_draft.tex",
      "artifacts/_project/paper/method_section_draft.tex",
      "artifacts/figures/object_benchmark_table.tex",
      "artifacts/figures/spatial_final_table.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/introduction_c83872.tex",
      "artifacts/_project/paper/related_work_9c2927.tex",
      "artifacts/_project/paper/related_work_80791f.tex",
      "artifacts/_project/paper/method_fb526b.tex",
      "artifacts/_project/paper/experiments_c64a8c.tex",
      "artifacts/_project/paper/abstract_a1674b.tex",
      "artifacts/_project/paper/sections/discussion.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/experiments_ac6246.tex",
      "artifacts/_project/paper/introduction_scenarioC_607d8d.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/introduction_scenarioC.tex",
      "artifacts/_project/paper/sections/introduction.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/abstract.tex",
      "docs/paper/related_work.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/main.tex",
      "docs/paper/experiments.tex",
      "docs/paper/appendix.tex",
      "docs/paper/method.tex",
      "docs/paper/discussion.tex"
    ],
    "durationMs": 55,
    "numFiles": 36,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Glob · `toolu_01BGUktVehVBLm7oeAQZzzNB`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "19d1c0fe-2271-44ca-a382-36937fc00e54",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0192JLWKHdZiCCLQj6oZTgrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 53789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 28 · 2026-05-21T16:38:38.303Z_

<details><summary>↩ Tool result · `toolu_01BGUktVehVBLm7oeAQZzzNB`</summary>

```text
docs/paper/camera_ready_template/corl_2026_template_cameraready/example.bib
docs/paper/review_template/corl_2026_template_submission/example.bib
artifacts/_project/paper/references_e9d4d2.bib
artifacts/_project/paper/references.bib
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "31670f6c-431f-4bd9-9e60-16585c9ca289",
  "tool_use_result": {
    "filenames": [
      "docs/paper/camera_ready_template/corl_2026_template_cameraready/example.bib",
      "docs/paper/review_template/corl_2026_template_submission/example.bib",
      "artifacts/_project/paper/references_e9d4d2.bib",
      "artifacts/_project/paper/references.bib",
      "docs/paper/references.bib"
    ],
    "durationMs": 63,
    "numFiles": 5,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01CLwSG3nTSqq9kMFzsuez8B`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/ /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/",
  "description": "List paper recursively"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "3900db9b-530b-4f73-b667-2e0353a631a3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0192JLWKHdZiCCLQj6oZTgrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 53789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 30 · 2026-05-21T16:38:39.777Z_

<details><summary>↩ Tool result · `toolu_01CLwSG3nTSqq9kMFzsuez8B`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/:
total 32
drwxr-xr-x  3 ubuntu ubuntu 4096 May 21 11:28 .
drwxr-xr-x 11 ubuntu ubuntu 4096 May 21 16:37 ..
-rw-r--r--  1 ubuntu ubuntu 5934 May 15 19:11 figure_plan.md
-rw-r--r--  1 ubuntu ubuntu 9728 May 21 11:28 outline.md
drwxr-xr-x  2 ubuntu ubuntu 4096 May 21 11:28 sections

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/:
total 20
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 11:28 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 21 11:28 ..
-rw-r--r-- 1 ubuntu ubuntu 2811 May 21 11:28 ablation_k_sweep.md
-rw-r--r-- 1 ubuntu ubuntu 8090 May 15 19:11 related_work.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "7ea441bd-7519-40e9-a71e-9839485d4669",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/:\ntotal 32\ndrwxr-xr-x  3 ubuntu ubuntu 4096 May 21 11:28 .\ndrwxr-xr-x 11 ubuntu ubuntu 4096 May 21 16:37 ..\n-rw-r--r--  1 ubuntu ubuntu 5934 May 15 19:11 figure_plan.md\n-rw-r--r--  1 ubuntu ubuntu 9728 May 21 11:28 outline.md\ndrwxr-xr-x  2 ubuntu ubuntu 4096 May 21 11:28 sections\n\n/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/:\ntotal 20\ndrwxr-xr-x 2 ubuntu ubuntu 4096 May 21 11:28 .\ndrwxr-xr-x 3 ubuntu ubuntu 4096 May 21 11:28 ..\n-rw-r--r-- 1 ubuntu ubuntu 2811 May 21 11:28 ablation_k_sweep.md\n-rw-r--r-- 1 ubuntu ubuntu 8090 May 15 19:11 related_work.md",
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

_source line 31_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "36f90162-f402-4777-a458-c11ae37cace7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016fKdtMx6LGxhU3P9U3mLPX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2031,
      "cache_read_input_tokens": 54426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2031
      },
      "output_tokens": 47,
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

_source line 32_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Wz3S3eYrgx72jiWEU3ABFy`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "642c9818-fd98-4173-a3dd-55926b91e801",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016fKdtMx6LGxhU3P9U3mLPX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2031,
      "cache_read_input_tokens": 54426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2031
      },
      "output_tokens": 47,
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

_source line 33 · 2026-05-21T16:38:43.097Z_

<details><summary>↩ Tool result · `toolu_01Wz3S3eYrgx72jiWEU3ABFy`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "baaec57c-67d5-4544-9a53-012ba1585734",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01RPB6aHJspJMMQNSGLCwaJ4`</summary>

```json
{
  "todos": [
    {
      "content": "Explore paper LaTeX source structure",
      "activeForm": "Exploring paper LaTeX source structure",
      "status": "in_progress"
    },
    {
      "content": "Attempt compilation and capture warnings/errors",
      "activeForm": "Attempting compilation and capturing warnings/errors",
      "status": "pending"
    },
    {
      "content": "Cross-check numerical claims against registry",
      "activeForm": "Cross-checking numerical claims against registry",
      "status": "pending"
    },
    {
      "content": "Audit pi0.5 / OpenVLA section coverage gaps",
      "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps",
      "status": "pending"
    },
    {
      "content": "Verify .bib entries and \\cite{} resolution",
      "activeForm": "Verifying .bib entries and \\cite{} resolution",
      "status": "pending"
    },
    {
      "content": "Write audit report to artifacts and register",
      "activeForm": "Writing audit report to artifacts and registering",
      "status": "pending"
    }
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "5dcff5e1-2fd6-4ac3-bff2-1114afe350ca",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013guZeckQugWuJmQsJXgTGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3580,
      "cache_read_input_tokens": 56457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3580
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

_source line 35 · 2026-05-21T16:38:48.566Z_

<details><summary>↩ Tool result · `toolu_01RPB6aHJspJMMQNSGLCwaJ4`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "6dd0b975-cad0-4591-9915-085684871c23",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Explore paper LaTeX source structure",
        "status": "in_progress",
        "activeForm": "Exploring paper LaTeX source structure"
      },
      {
        "content": "Attempt compilation and capture warnings/errors",
        "status": "pending",
        "activeForm": "Attempting compilation and capturing warnings/errors"
      },
      {
        "content": "Cross-check numerical claims against registry",
        "status": "pending",
        "activeForm": "Cross-checking numerical claims against registry"
      },
      {
        "content": "Audit pi0.5 / OpenVLA section coverage gaps",
        "status": "pending",
        "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps"
      },
      {
        "content": "Verify .bib entries and \\cite{} resolution",
        "status": "pending",
        "activeForm": "Verifying .bib entries and \\cite{} resolution"
      },
      {
        "content": "Write audit report to artifacts and register",
        "status": "pending",
        "activeForm": "Writing audit report to artifacts and registering"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_016siLqXPRdhaNJPxNv6afzc`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/",
  "description": "List docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "6d2ad3be-452c-4573-a502-e3a38a49019a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013qwveYsxnvgarPpgR1GoMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 60037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 468
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

_source line 37 · 2026-05-21T16:38:53.132Z_

<details><summary>↩ Tool result · `toolu_016siLqXPRdhaNJPxNv6afzc`</summary>

```text
total 824
drwxr-xr-x 5 ubuntu ubuntu   4096 May 21 15:46 .
drwxr-xr-x 4 ubuntu ubuntu   4096 May 16 00:47 ..
-rw-r--r-- 1 ubuntu ubuntu   1651 May 21 04:21 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu  12063 May 21 14:57 appendix.tex
drwxr-xr-x 3 ubuntu ubuntu   4096 May 18 10:45 camera_ready_template
-rw------- 1 ubuntu ubuntu  17150 Jan 13 19:11 corl2026_camera_ready_template.zip
-rw------- 1 ubuntu ubuntu  17423 Apr 30 16:21 corl2026_review_template.zip
-rw-r--r-- 1 ubuntu ubuntu  14861 May 18 10:51 corl_2026.sty
-rw-r--r-- 1 ubuntu ubuntu  26694 May 18 10:51 corlabbrvnat.bst
-rw-r--r-- 1 ubuntu ubuntu    906 May 21 15:44 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu   8621 May 21 14:57 experiments.tex
drwxr-xr-x 2 ubuntu ubuntu   4096 May 20 02:34 figures
-rw-r--r-- 1 ubuntu ubuntu   5041 May 21 04:22 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  20630 May 21 15:44 main.aux
-rw-r--r-- 1 ubuntu ubuntu  11101 May 21 15:44 main.bbl
-rw-r--r-- 1 ubuntu ubuntu    922 May 21 15:44 main.blg
-rw-r--r-- 1 ubuntu ubuntu  18977 May 21 15:44 main.fdb_latexmk
-rw-r--r-- 1 ubuntu ubuntu  19030 May 21 15:44 main.fls
-rw-r--r-- 1 ubuntu ubuntu  23993 May 21 15:44 main.log
-rw-r--r-- 1 ubuntu ubuntu   4308 May 21 15:44 main.out
-rw-r--r-- 1 ubuntu ubuntu 544260 May 21 15:44 main.pdf
-rw-r--r-- 1 ubuntu ubuntu    822 May 21 14:53 main.tex
-rw-r--r-- 1 ubuntu ubuntu   8942 May 21 15:44 method.tex
-rw-r--r-- 1 ubuntu ubuntu  12075 May 21 03:33 references.bib
-rw-r--r-- 1 ubuntu ubuntu   5466 May 21 03:45 related_work.tex
drwxr-xr-x 3 ubuntu ubuntu   4096 May 18 10:45 review_template
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "6886852f-a51f-47ce-b03d-050eb0d1a22d",
  "tool_use_result": {
    "stdout": "total 824\ndrwxr-xr-x 5 ubuntu ubuntu   4096 May 21 15:46 .\ndrwxr-xr-x 4 ubuntu ubuntu   4096 May 16 00:47 ..\n-rw-r--r-- 1 ubuntu ubuntu   1651 May 21 04:21 abstract.tex\n-rw-r--r-- 1 ubuntu ubuntu  12063 May 21 14:57 appendix.tex\ndrwxr-xr-x 3 ubuntu ubuntu   4096 May 18 10:45 camera_ready_template\n-rw------- 1 ubuntu ubuntu  17150 Jan 13 19:11 corl2026_camera_ready_template.zip\n-rw------- 1 ubuntu ubuntu  17423 Apr 30 16:21 corl2026_review_template.zip\n-rw-r--r-- 1 ubuntu ubuntu  14861 May 18 10:51 corl_2026.sty\n-rw-r--r-- 1 ubuntu ubuntu  26694 May 18 10:51 corlabbrvnat.bst\n-rw-r--r-- 1 ubuntu ubuntu    906 May 21 15:44 discussion.tex\n-rw-r--r-- 1 ubuntu ubuntu   8621 May 21 14:57 experiments.tex\ndrwxr-xr-x 2 ubuntu ubuntu   4096 May 20 02:34 figures\n-rw-r--r-- 1 ubuntu ubuntu   5041 May 21 04:22 introduction.tex\n-rw-r--r-- 1 ubuntu ubuntu  20630 May 21 15:44 main.aux\n-rw-r--r-- 1 ubuntu ubuntu  11101 May 21 15:44 main.bbl\n-rw-r--r-- 1 ubuntu ubuntu    922 May 21 15:44 main.blg\n-rw-r--r-- 1 ubuntu ubuntu  18977 May 21 15:44 main.fdb_latexmk\n-rw-r--r-- 1 ubuntu ubuntu  19030 May 21 15:44 main.fls\n-rw-r--r-- 1 ubuntu ubuntu  23993 May 21 15:44 main.log\n-rw-r--r-- 1 ubuntu ubuntu   4308 May 21 15:44 main.out\n-rw-r--r-- 1 ubuntu ubuntu 544260 May 21 15:44 main.pdf\n-rw-r--r-- 1 ubuntu ubuntu    822 May 21 14:53 main.tex\n-rw-r--r-- 1 ubuntu ubuntu   8942 May 21 15:44 method.tex\n-rw-r--r-- 1 ubuntu ubuntu  12075 May 21 03:33 references.bib\n-rw-r--r-- 1 ubuntu ubuntu   5466 May 21 03:45 related_work.tex\ndrwxr-xr-x 3 ubuntu ubuntu   4096 May 18 10:45 review_template",
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

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01Wi1VRic8KjS85bCbEtvoVm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "4bb4f172-731e-4498-a08d-4d5addfbaa68",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01G7bkQhctRLRv1tsFYiS7UH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 60505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
      },
      "output_tokens": 47,
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

_source line 39 · 2026-05-21T16:38:57.074Z_

<details><summary>↩ Tool result · `toolu_01Wi1VRic8KjS85bCbEtvoVm`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{amsmath,amssymb,amsfonts}
8	\DeclareMathOperator*{\argmin}{arg\,min}
9	\DeclareMathOperator*{\argmax}{arg\,max}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{enumitem}
13	\usepackage{multirow}
14	
15	\newcommand{\placeholder}[1]{---}
16	
17	\graphicspath{{figures/}}
18	
19	\title{When to Correct: Adaptive Inference-Time Compute\\Allocation for Frozen VLAs}
20	
21	\author{
22	  Anonymous
23	}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\keywords{Vision-Language-Action Models, Inference-Time Refinement, Robotic Manipulation}
34	
35	\input{introduction}
36	\input{related_work}
37	\input{method}
38	\input{experiments}
39	\input{discussion}
40	
41	\bibliography{references}
42	
43	\clearpage
44	\input{appendix}
45	
46	\end{document}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "5ee7395b-faaa-498a-a0d4-d20b270e3705",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex",
      "content": "\\documentclass{article}\n\n\\usepackage{corl_2026}\n\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\DeclareMathOperator*{\\argmin}{arg\\,min}\n\\DeclareMathOperator*{\\argmax}{arg\\,max}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{multirow}\n\n\\newcommand{\\placeholder}[1]{---}\n\n\\graphicspath{{figures/}}\n\n\\title{When to Correct: Adaptive Inference-Time Compute\\\\Allocation for Frozen VLAs}\n\n\\author{\n  Anonymous\n}\n\n\\begin{document}\n\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\keywords{Vision-Language-Action Models, Inference-Time Refinement, Robotic Manipulation}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{discussion}\n\n\\bibliography{references}\n\n\\clearpage\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  }
}
```

</details>

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_0168yyzgP1d6DJmtXLEm1Knh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "0e811b13-b245-4e80-bb8f-05d9c3a52b2e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01G7bkQhctRLRv1tsFYiS7UH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 60505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
      },
      "output_tokens": 47,
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

_source line 41 · 2026-05-21T16:38:58.115Z_

<details><summary>↩ Tool result · `toolu_0168yyzgP1d6DJmtXLEm1Knh`</summary>

```text
1	Vision-Language-Action (VLA) models for robotic manipulation degrade under distribution shift, yet improving their outputs at inference time remains underexplored, particularly the question of \emph{when} additional compute is warranted.
2	We propose an adaptive inference-time compute pipeline for frozen flow-matching VLAs. The core mechanism is a $K{=}2$ pairwise $L_2$ distance that correlates near-perfectly with full $K{=}10$ sample variance ($\rho{=}0.9979$), providing a per-step uncertainty estimate at zero additional cost. Three alternative signals (FMVD, CRM correction magnitude) all fail ($\rho \leq 0.15$).
3	When uncertainty is low, the pipeline outputs the $K{=}2$ argmin sample directly; when high, it applies learned residual correction via a ${\sim}$327K-parameter Correction Residual Module (CRM) trained on task-specific VLA rollout data. The pipeline uses at most two forward passes---gains come from learned correction, not additional sampling.
4	The $K{=}2$ adaptive pipeline matches or exceeds fixed-$K{=}10$ unconditional correction with 80\% fewer VLA forward passes: $18.3 \pm 2.1$\% on LIBERO-Object ($+$7.3\,pp vs.\ VLA-only) and $35.0 \pm 1.0$\% on LIBERO-Spatial ($+$5.6\,pp), with selective CRM application (Object 83.7\%, Spatial 97.6\% trigger rate).
5	Component decomposition on fixed-$K$ analysis baselines reveals that learned correction contributes 55\% of the gain at $K{=}5$ and 78\% at $K{=}10$, while multi-sampling is an enabling condition ($K{=}1$ correction degrades below baseline). Three distribution shifts define operating boundaries: near-OOD task shift is adversarial ($-$12\,pp) while far-OOD is neutral.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "060b5157-936d-42f2-b10e-9be3c9a18f0c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex",
      "content": "Vision-Language-Action (VLA) models for robotic manipulation degrade under distribution shift, yet improving their outputs at inference time remains underexplored, particularly the question of \\emph{when} additional compute is warranted.\nWe propose an adaptive inference-time compute pipeline for frozen flow-matching VLAs. The core mechanism is a $K{=}2$ pairwise $L_2$ distance that correlates near-perfectly with full $K{=}10$ sample variance ($\\rho{=}0.9979$), providing a per-step uncertainty estimate at zero additional cost. Three alternative signals (FMVD, CRM correction magnitude) all fail ($\\rho \\leq 0.15$).\nWhen uncertainty is low, the pipeline outputs the $K{=}2$ argmin sample directly; when high, it applies learned residual correction via a ${\\sim}$327K-parameter Correction Residual Module (CRM) trained on task-specific VLA rollout data. The pipeline uses at most two forward passes---gains come from learned correction, not additional sampling.\nThe $K{=}2$ adaptive pipeline matches or exceeds fixed-$K{=}10$ unconditional correction with 80\\% fewer VLA forward passes: $18.3 \\pm 2.1$\\% on LIBERO-Object ($+$7.3\\,pp vs.\\ VLA-only) and $35.0 \\pm 1.0$\\% on LIBERO-Spatial ($+$5.6\\,pp), with selective CRM application (Object 83.7\\%, Spatial 97.6\\% trigger rate).\nComponent decomposition on fixed-$K$ analysis baselines reveals that learned correction contributes 55\\% of the gain at $K{=}5$ and 78\\% at $K{=}10$, while multi-sampling is an enabling condition ($K{=}1$ correction degrades below baseline). Three distribution shifts define operating boundaries: near-OOD task shift is adversarial ($-$12\\,pp) while far-OOD is neutral.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  }
}
```

</details>

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01KytWWtYP2qYnC7pAiV4B3a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "b99a8b40-5f02-4b80-b964-d56cbd1b9bd5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01G7bkQhctRLRv1tsFYiS7UH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 60505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1208
      },
      "output_tokens": 47,
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

_source line 43 · 2026-05-21T16:38:58.517Z_

<details><summary>↩ Tool result · `toolu_01KytWWtYP2qYnC7pAiV4B3a`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	\looseness=-1 Deploying a pretrained Vision-Language-Action model (VLA) on a new task typically requires fine-tuning on task-specific demonstrations, yet collecting such data is expensive and the resulting checkpoint may not generalize further.
5	An alternative is to keep the VLA frozen and attach a lightweight post-hoc correction module trained on task-specific VLA rollout data, improving action quality at inference time without modifying the base model.
6	Flow-matching VLAs~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} are natural candidates: each forward pass produces a stochastic action sample, so drawing multiple samples opens the door to selection and correction without changing model weights.
7	The question is not only how to use these samples but \emph{when} to invest the additional compute: most control steps are easy and do not benefit from multi-sample correction, while a minority of hard steps account for the majority of task failures.
8	
9	\looseness=-1 Recent robustness evaluations~\cite{fei2025liberoplus} show that state-of-the-art VLAs lose over 65 percentage points under common deployment perturbations, making inference-time correction practically relevant.
10	Training-time methods~\cite{srpo2025,robustvla2025,digflow2025,liu2026ttvla} improve the base policy through robustness-aware objectives or test-time RL, but require retraining and remain bounded by the training distribution.
11	Inference-time methods leave the policy frozen: ReconVLA~\cite{chen2026reconvla} provides uncertainty quantification but does not learn corrective residuals; A2C2~\cite{a2c2_2025} trains a per-step correction head on action chunks but applies correction unconditionally without adaptive compute allocation; VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization at 2.41\,s per control step.
12	Despite growing interest, no prior work addresses a core efficiency question: how to determine per-step whether the VLA is uncertain enough to warrant additional sampling and correction.
13	
14	\looseness=-1 We introduce an adaptive inference-time compute pipeline for frozen flow-matching VLAs. The core insight is that the pairwise $L_2$ distance between just $K{=}2$ action samples from the frozen VLA correlates near-perfectly with the full $K{=}10$ sample variance ($\rho{=}0.9979$), providing a per-step uncertainty estimate at negligible additional cost (${\sim}$250\,ms with batched inference, comparable to single-sample latency). Three alternative uncertainty signals (FMVD, CRM correction magnitude at $K{=}1$ and $K{=}2$) all yield $\rho \leq 0.15$.
15	When the probe indicates low uncertainty, the pipeline outputs the $K{=}2$ argmin sample directly; when uncertainty is high, it applies a learned residual correction to the same sample through a lightweight Correction Residual Module (CRM, ${\sim}$327K parameters). The pipeline uses at most $K{=}2$ forward passes---performance gains come from learned correction, not additional sampling.
16	
17	\looseness=-1 The $K{=}2$ adaptive pipeline achieves $18.3 \pm 2.1$\% on LIBERO-Object ($+$7.3\,pp vs.\ $11.0 \pm 1.3$\% VLA-only, 8 seeds) and $35.0 \pm 1.0$\% on Spatial ($+$5.6\,pp), matching or exceeding fixed-$K{=}10$ unconditional correction ($16.8$\%, $34.4$\%) with 80\% fewer VLA forward passes. CRM triggers on 83.7\% of Object steps but 97.6\% of Spatial steps, reflecting that selectivity is task-difficulty-dependent.
18	Component decomposition on fixed-$K$ analysis baselines reveals that learned correction contributes 55\% of the gain at $K{=}5$ and 78\% at $K{=}10$, while multi-sampling is an enabling condition: $K{=}1$ correction alone falls below baseline (10.3\%).
19	Unlike LLM test-time compute scaling~\cite{snell2024scaling} where selection is primary, here the $K{=}2$ probe provides a centered starting point and uncertainty gate for learned correction.
20	
21	Our contributions are:
22	\begin{enumerate}[leftmargin=*,nosep]
23	  \item \textbf{$K{=}2$ adaptive pipeline} (Section~\ref{sec:adaptive_k_method}): selective CRM correction gated by a pairwise $L_2$ uncertainty probe ($\rho{=}0.9979$ vs.\ $K{=}10$ variance; three alternatives fail, $\rho \leq 0.15$). Achieves $18.3$\% Object / $35.0$\% Spatial ($+$7.3 / $+$5.6\,pp vs.\ VLA-only), matching fixed-$K{=}10$ with 80\% fewer VLA forward passes.
24	  \item \textbf{Selective $>$ unconditional correction} (Section~\ref{sec:main_results}): Plan~A exceeds $K{=}10$ unconditional CRM ($18.3$\% vs.\ $16.8$\% Object); trigger rate is task-dependent (Object 83.7\%, Spatial 97.6\%).
25	  \item \textbf{Correction mechanism decomposition} (Section~\ref{sec:main_results}): on fixed-$K$ analysis baselines, learned correction contributes 55--78\% of the gain; random selection fails to exceed VLA-only on either benchmark, confirming correction as the active ingredient.
26	  \item \textbf{Distribution shift boundaries} (Section~\ref{sec:failure_modes}): three shifts define operating boundaries; near-OOD is adversarial ($-$12\,pp), far-OOD neutral ($p{=}0.46$).
27	\end{enumerate}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "04c33e83-c794-41d2-bd77-7a3726b9d613",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n\\looseness=-1 Deploying a pretrained Vision-Language-Action model (VLA) on a new task typically requires fine-tuning on task-specific demonstrations, yet collecting such data is expensive and the resulting checkpoint may not generalize further.\nAn alternative is to keep the VLA frozen and attach a lightweight post-hoc correction module trained on task-specific VLA rollout data, improving action quality at inference time without modifying the base model.\nFlow-matching VLAs~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} are natural candidates: each forward pass produces a stochastic action sample, so drawing multiple samples opens the door to selection and correction without changing model weights.\nThe question is not only how to use these samples but \\emph{when} to invest the additional compute: most control steps are easy and do not benefit from multi-sample correction, while a minority of hard steps account for the majority of task failures.\n\n\\looseness=-1 Recent robustness evaluations~\\cite{fei2025liberoplus} show that state-of-the-art VLAs lose over 65 percentage points under common deployment perturbations, making inference-time correction practically relevant.\nTraining-time methods~\\cite{srpo2025,robustvla2025,digflow2025,liu2026ttvla} improve the base policy through robustness-aware objectives or test-time RL, but require retraining and remain bounded by the training distribution.\nInference-time methods leave the policy frozen: ReconVLA~\\cite{chen2026reconvla} provides uncertainty quantification but does not learn corrective residuals; A2C2~\\cite{a2c2_2025} trains a per-step correction head on action chunks but applies correction unconditionally without adaptive compute allocation; VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization at 2.41\\,s per control step.\nDespite growing interest, no prior work addresses a core efficiency question: how to determine per-step whether the VLA is uncertain enough to warrant additional sampling and correction.\n\n\\looseness=-1 We introduce an adaptive inference-time compute pipeline for frozen flow-matching VLAs. The core insight is that the pairwise $L_2$ distance between just $K{=}2$ action samples from the frozen VLA correlates near-perfectly with the full $K{=}10$ sample variance ($\\rho{=}0.9979$), providing a per-step uncertainty estimate at negligible additional cost (${\\sim}$250\\,ms with batched inference, comparable to single-sample latency). Three alternative uncertainty signals (FMVD, CRM correction magnitude at $K{=}1$ and $K{=}2$) all yield $\\rho \\leq 0.15$.\nWhen the probe indicates low uncertainty, the pipeline outputs the $K{=}2$ argmin sample directly; when uncertainty is high, it applies a learned residual correction to the same sample through a lightweight Correction Residual Module (CRM, ${\\sim}$327K parameters). The pipeline uses at most $K{=}2$ forward passes---performance gains come from learned correction, not additional sampling.\n\n\\looseness=-1 The $K{=}2$ adaptive pipeline achieves $18.3 \\pm 2.1$\\% on LIBERO-Object ($+$7.3\\,pp vs.\\ $11.0 \\pm 1.3$\\% VLA-only, 8 seeds) and $35.0 \\pm 1.0$\\% on Spatial ($+$5.6\\,pp), matching or exceeding fixed-$K{=}10$ unconditional correction ($16.8$\\%, $34.4$\\%) with 80\\% fewer VLA forward passes. CRM triggers on 83.7\\% of Object steps but 97.6\\% of Spatial steps, reflecting that selectivity is task-difficulty-dependent.\nComponent decomposition on fixed-$K$ analysis baselines reveals that learned correction contributes 55\\% of the gain at $K{=}5$ and 78\\% at $K{=}10$, while multi-sampling is an enabling condition: $K{=}1$ correction alone falls below baseline (10.3\\%).\nUnlike LLM test-time compute scaling~\\cite{snell2024scaling} where selection is primary, here the $K{=}2$ probe provides a centered starting point and uncertainty gate for learned correction.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{$K{=}2$ adaptive pipeline} (Section~\\ref{sec:adaptive_k_method}): selective CRM correction gated by a pairwise $L_2$ uncertainty probe ($\\rho{=}0.9979$ vs.\\ $K{=}10$ variance; three alternatives fail, $\\rho \\leq 0.15$). Achieves $18.3$\\% Object / $35.0$\\% Spatial ($+$7.3 / $+$5.6\\,pp vs.\\ VLA-only), matching fixed-$K{=}10$ with 80\\% fewer VLA forward passes.\n  \\item \\textbf{Selective $>$ unconditional correction} (Section~\\ref{sec:main_results}): Plan~A exceeds $K{=}10$ unconditional CRM ($18.3$\\% vs.\\ $16.8$\\% Object); trigger rate is task-dependent (Object 83.7\\%, Spatial 97.6\\%).\n  \\item \\textbf{Correction mechanism decomposition} (Section~\\ref{sec:main_results}): on fixed-$K$ analysis baselines, learned correction contributes 55--78\\% of the gain; random selection fails to exceed VLA-only on either benchmark, confirming correction as the active ingredient.\n  \\item \\textbf{Distribution shift boundaries} (Section~\\ref{sec:failure_modes}): three shifts define operating boundaries; near-OOD is adversarial ($-$12\\,pp), far-OOD neutral ($p{=}0.46$).\n\\end{enumerate}\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_0191ojqDycXDC5WKph8koe6q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "e093b554-4d04-47b2-83df-bde86227685f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JazqT8cHDEEnMbPcNrzs5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3722,
      "cache_read_input_tokens": 61713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3722
      },
      "output_tokens": 41,
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

_source line 45 · 2026-05-21T16:39:02.525Z_

<details><summary>↩ Tool result · `toolu_0191ojqDycXDC5WKph8koe6q`</summary>

```text
1	
2	\section{Method}
3	\label{sec:method}
4	
5	\begin{figure}[t]
6	  \centering
7	  \includegraphics[width=\linewidth]{fig1_pipeline.pdf}
8	  \caption{Adaptive sample-select-correct pipeline. $K{=}2$ action samples are drawn from the frozen VLA; the argmin-to-centroid sample is selected, and a lightweight CRM applies bounded correction ($\|\boldsymbol{\delta}\|_2 \leq \varepsilon$) only when the pairwise $L_2$ distance exceeds the uncertainty threshold $\tau$.}
9	  \label{fig:pipeline}
10	\end{figure}
11	
12	\looseness=-1 Our method adaptively allocates inference-time compute for a frozen flow-matching VLA (Figure~\ref{fig:pipeline}). At each control step, a $K{=}2$ uncertainty probe determines whether the VLA is confident or uncertain; confident steps output the argmin-to-centroid sample directly, while uncertain steps apply a learned residual correction to the same sample via a lightweight module. The base VLA is never retrained.
13	
14	\subsection{Problem Setup}
15	\label{sec:problem_setup}
16	
17	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.
18	
19	\looseness=-1 Each forward pass of $\pi_\theta$ produces a stochastic action sample; querying independently $K$ times yields $K$ candidate chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to $\pi_\theta$. The method applies to any flow-matching VLA that produces diverse samples (Appendix~\ref{sec:applicability}).
20	
21	\subsection{Multi-Sample Selection}
22	\label{sec:selection}
23	
24	We draw $K$ action chunks from $\pi_\theta$ via independent flow-matching rollouts and truncate each to $H{=}5$ steps, yielding samples $\{a_h^{(k)}\}_{k=1}^K$ with $a_h^{(k)} \in \mathbb{R}^d$ for horizon step $h = 1, \dots, H$. For each step, we compute the sample mean $\boldsymbol{\mu}_h = \frac{1}{K}\sum_{k=1}^K a_h^{(k)}$ and select the sample with the smallest total $L_2$ distance to the mean across all horizon steps:
25	\begin{equation}
26	  a_{\mathrm{base}} = \argmin_{k \in \{1,\dots,K\}} \sum_{h=1}^{H} \bigl\|a_h^{(k)} - \boldsymbol{\mu}_h\bigr\|_2^2.
27	  \label{eq:argmin}
28	\end{equation}
29	Unlike the element-wise mean, which can blend incompatible modes, the argmin returns an actual sample and preserves within-sample temporal coherence.
30	
31	\subsection{Correction Module (CRM)}
32	\label{sec:crm}
33	
34	The CRM is a lightweight MLP that refines the selected action $a_{\mathrm{base}}$ by predicting a bounded residual correction conditioned on the current observation and the selected action itself.
35	
36	\paragraph{Architecture.}
37	\looseness=-1 The CRM consists of three fully connected layers with ReLU activations: $\mathrm{Linear}(n_{\mathrm{in}}, 256) \to \mathrm{ReLU} \to \mathrm{Linear}(256, 256) \to \mathrm{ReLU} \to \mathrm{Linear}(256, 30)$, preceded by input normalization. For the primary obs\_only variant ($n_{\mathrm{in}}{=}990$), the input is the concatenation of the frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{960}$ from SmolVLA's vision-language encoder and the selected action $a_{\mathrm{base}} \in \mathbb{R}^{30}$ ($H{=}5$ steps $\times$ $d{=}6$ DOFs), for a total of 327,198 parameters (${\sim}$327K). The output is a residual $\boldsymbol{\delta} \in \mathbb{R}^{30}$, and the corrected action is:
38	\begin{equation}
39	  \mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}\bigl(\boldsymbol{\delta},\; \|\boldsymbol{\delta}\|_2 \leq \varepsilon\bigr),
40	  \label{eq:crm}
41	\end{equation}
42	where $\varepsilon$ is a norm bound that limits the correction magnitude (Section~\ref{sec:magnitude}). The CRM never sees individual action candidates: it receives only the already-selected $a_{\mathrm{base}}$ and predicts a correction toward the expert action.
43	
44	\paragraph{Conditioning variants.}
45	We compare three CRM variants that share the same MLP architecture but differ in their input:
46	\begin{itemize}[nosep]
47	  \item \textbf{obs\_only} (primary): $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}}] \in \mathbb{R}^{990}$, 327K parameters. No conformal or uncertainty features.
48	  \item \textbf{perdof}: $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}};\, \mathbf{u}_{\mathrm{dof}}] \in \mathbb{R}^{1030}$, 337K parameters. $\mathbf{u}_{\mathrm{dof}}$ concatenates per-DOF standard deviations, conformal prediction radii~\cite{angelopoulos2023gentle}, and covariance log-volumes~\cite{ledoit2004well} ($40$D total).
49	  \item \textbf{scalar}: $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}};\, u_s] \in \mathbb{R}^{991}$, 327K parameters, where $u_s$ is a single scalar uncertainty summary.
50	\end{itemize}
51	Section~\ref{sec:magnitude_results} shows that conformal features fail to improve closed-loop performance; obs\_only is our primary method.
52	
53	\paragraph{Training.}
54	\looseness=-1 The CRM is trained offline on demonstration trajectories from LIBERO~\cite{liu2023libero} with $L_2$ loss:
55	\begin{equation}
56	  \mathcal{L} = \bigl\|\mathbf{a}^* - \mathbf{a}_{\mathrm{expert}}\bigr\|_2^2,
57	  \label{eq:loss}
58	\end{equation}
59	where $\mathbf{a}_{\mathrm{expert}}$ is the demonstration action. The training set comprises 26{,}737 precomputed samples from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, apply argmin selection~(\ref{eq:argmin}) to obtain $a_{\mathrm{base}}$, and train the CRM to predict the residual toward $\mathbf{a}_{\mathrm{expert}}$. Data augmentation (Gaussian noise on $a_{\mathrm{base}}$ and uncertainty features) improves generalization to the closed-loop state distribution~\cite{ross2011dagger}.
60	
61	\subsection{Magnitude Control}
62	\label{sec:magnitude}
63	
64	The norm bound $\varepsilon$ in~(\ref{eq:crm}) is critical for stable closed-loop performance. Without clipping, the CRM's natural output norm (${\approx}$1.42) causes compounding errors that destroy task performance (0\% success for the perdof variant). Constraining $\varepsilon$ to $[0.05, 0.2]$ yields stable corrections; we use $\varepsilon{=}0.2$ as the primary setting. Section~\ref{sec:magnitude_results} presents the full sensitivity analysis across conditioning variants and magnitude bounds.
65	
66	\subsection{Adaptive Inference-Time Compute}
67	\label{sec:adaptive_k_method}
68	
69	Two findings from our component analysis motivate an adaptive mechanism: (i)~learned correction is the dominant contributor to task improvement (Section~\ref{sec:main_results}), but (ii)~correction on uncentered inputs ($K{=}1$) degrades below baseline (Section~\ref{sec:failure_modes}). Fixed $K{=}10$ sampling is wasteful---most steps are easy---yet $K{=}1$ correction fails. The solution is a per-step uncertainty probe that decides \emph{when} to invest additional compute.
70	
71	\paragraph{Why $K{=}2$.}
72	\looseness=-1 $K{=}2$ is the minimum sample size that admits a pairwise disagreement measure. This probe is computationally free: under batched inference with shared prefix encoding, $K{=}2$ latency (${\sim}$255\,ms) matches $K{=}1$ (Appendix~\ref{sec:latency}). Empirically, the $K{=}2$ $L_2$ distance achieves $\rho{=}0.9979$ with $K{=}10$ sample variance (Section~\ref{sec:adaptive_k}); three alternative signals all fail ($\rho \leq 0.15$).
73	
74	\paragraph{Three-step adaptive pipeline.}
75	At each control step, the pipeline executes:
76	\begin{enumerate}[nosep,leftmargin=*]
77	  \item \textbf{Uncertainty probe.} Draw $K{=}2$ samples $a^{(1)}, a^{(2)}$ from $\pi_\theta$ in a single batched forward pass. Compute the centroid $\mathbf{c} = (a^{(1)} + a^{(2)})/2$ and the pairwise uncertainty $d_2 = \|a^{(1)} - a^{(2)}\|_2$. Select $\hat{a} = \argmin_{a \in \{a^{(1)}, a^{(2)}\}} \|a - \mathbf{c}\|_2$.
78	  \item \textbf{Adaptive decision.} If $d_2 \leq \tau$ (low uncertainty), output $\hat{a}$ directly---no further computation. If $d_2 > \tau$ (high uncertainty), pass $\hat{a}$ to the CRM for correction.
79	  \item \textbf{Learned correction.} For high-uncertainty steps only, the CRM predicts a bounded residual: $\hat{a}_{\mathrm{out}} = \hat{a} + \boldsymbol{\delta}$, where $\boldsymbol{\delta} = \mathrm{CRM}(o_t, \hat{a})$ and $\|\boldsymbol{\delta}\|_2 \leq \varepsilon$~(\ref{eq:crm}). The pipeline uses at most $K{=}2$ forward passes; performance gains come from learned correction, not brute-force sampling.
80	\end{enumerate}
81	\looseness=-1 The threshold $\tau$ is a percentile of the empirical $d_2$ distribution from CRM training data. Higher $\tau$ triggers correction on fewer steps; the optimal percentile is task-difficulty-dependent (Section~\ref{sec:adaptive_k}). CRM inference adds ${\sim}$0.3\,ms; the VLA forward pass (${\sim}$255\,ms) dominates latency.
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "82c840d6-69ec-412c-8c55-b5ef3d9bb544",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\linewidth]{fig1_pipeline.pdf}\n  \\caption{Adaptive sample-select-correct pipeline. $K{=}2$ action samples are drawn from the frozen VLA; the argmin-to-centroid sample is selected, and a lightweight CRM applies bounded correction ($\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$) only when the pairwise $L_2$ distance exceeds the uncertainty threshold $\\tau$.}\n  \\label{fig:pipeline}\n\\end{figure}\n\n\\looseness=-1 Our method adaptively allocates inference-time compute for a frozen flow-matching VLA (Figure~\\ref{fig:pipeline}). At each control step, a $K{=}2$ uncertainty probe determines whether the VLA is confident or uncertain; confident steps output the argmin-to-centroid sample directly, while uncertain steps apply a learned residual correction to the same sample via a lightweight module. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.\n\n\\looseness=-1 Each forward pass of $\\pi_\\theta$ produces a stochastic action sample; querying independently $K$ times yields $K$ candidate chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to $\\pi_\\theta$. The method applies to any flow-matching VLA that produces diverse samples (Appendix~\\ref{sec:applicability}).\n\n\\subsection{Multi-Sample Selection}\n\\label{sec:selection}\n\nWe draw $K$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts and truncate each to $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for horizon step $h = 1, \\dots, H$. For each step, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and select the sample with the smallest total $L_2$ distance to the mean across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} \\bigl\\|a_h^{(k)} - \\boldsymbol{\\mu}_h\\bigr\\|_2^2.\n  \\label{eq:argmin}\n\\end{equation}\nUnlike the element-wise mean, which can blend incompatible modes, the argmin returns an actual sample and preserves within-sample temporal coherence.\n\n\\subsection{Correction Module (CRM)}\n\\label{sec:crm}\n\nThe CRM is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a bounded residual correction conditioned on the current observation and the selected action itself.\n\n\\paragraph{Architecture.}\n\\looseness=-1 The CRM consists of three fully connected layers with ReLU activations: $\\mathrm{Linear}(n_{\\mathrm{in}}, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 30)$, preceded by input normalization. For the primary obs\\_only variant ($n_{\\mathrm{in}}{=}990$), the input is the concatenation of the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$ from SmolVLA's vision-language encoder and the selected action $a_{\\mathrm{base}} \\in \\mathbb{R}^{30}$ ($H{=}5$ steps $\\times$ $d{=}6$ DOFs), for a total of 327,198 parameters (${\\sim}$327K). The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound that limits the correction magnitude (Section~\\ref{sec:magnitude}). The CRM never sees individual action candidates: it receives only the already-selected $a_{\\mathrm{base}}$ and predicts a correction toward the expert action.\n\n\\paragraph{Conditioning variants.}\nWe compare three CRM variants that share the same MLP architecture but differ in their input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only} (primary): $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}] \\in \\mathbb{R}^{990}$, 327K parameters. No conformal or uncertainty features.\n  \\item \\textbf{perdof}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, \\mathbf{u}_{\\mathrm{dof}}] \\in \\mathbb{R}^{1030}$, 337K parameters. $\\mathbf{u}_{\\mathrm{dof}}$ concatenates per-DOF standard deviations, conformal prediction radii~\\cite{angelopoulos2023gentle}, and covariance log-volumes~\\cite{ledoit2004well} ($40$D total).\n  \\item \\textbf{scalar}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, u_s] \\in \\mathbb{R}^{991}$, 327K parameters, where $u_s$ is a single scalar uncertainty summary.\n\\end{itemize}\nSection~\\ref{sec:magnitude_results} shows that conformal features fail to improve closed-loop performance; obs\\_only is our primary method.\n\n\\paragraph{Training.}\n\\looseness=-1 The CRM is trained offline on demonstration trajectories from LIBERO~\\cite{liu2023libero} with $L_2$ loss:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2,\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\mathbf{a}_{\\mathrm{expert}}$ is the demonstration action. The training set comprises 26{,}737 precomputed samples from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, apply argmin selection~(\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$, and train the CRM to predict the residual toward $\\mathbf{a}_{\\mathrm{expert}}$. Data augmentation (Gaussian noise on $a_{\\mathrm{base}}$ and uncertainty features) improves generalization to the closed-loop state distribution~\\cite{ross2011dagger}.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical for stable closed-loop performance. Without clipping, the CRM's natural output norm (${\\approx}$1.42) causes compounding errors that destroy task performance (0\\% success for the perdof variant). Constraining $\\varepsilon$ to $[0.05, 0.2]$ yields stable corrections; we use $\\varepsilon{=}0.2$ as the primary setting. Section~\\ref{sec:magnitude_results} presents the full sensitivity analysis across conditioning variants and magnitude bounds.\n\n\\subsection{Adaptive Inference-Time Compute}\n\\label{sec:adaptive_k_method}\n\nTwo findings from our component analysis motivate an adaptive mechanism: (i)~learned correction is the dominant contributor to task improvement (Section~\\ref{sec:main_results}), but (ii)~correction on uncentered inputs ($K{=}1$) degrades below baseline (Section~\\ref{sec:failure_modes}). Fixed $K{=}10$ sampling is wasteful---most steps are easy---yet $K{=}1$ correction fails. The solution is a per-step uncertainty probe that decides \\emph{when} to invest additional compute.\n\n\\paragraph{Why $K{=}2$.}\n\\looseness=-1 $K{=}2$ is the minimum sample size that admits a pairwise disagreement measure. This probe is computationally free: under batched inference with shared prefix encoding, $K{=}2$ latency (${\\sim}$255\\,ms) matches $K{=}1$ (Appendix~\\ref{sec:latency}). Empirically, the $K{=}2$ $L_2$ distance achieves $\\rho{=}0.9979$ with $K{=}10$ sample variance (Section~\\ref{sec:adaptive_k}); three alternative signals all fail ($\\rho \\leq 0.15$).\n\n\\paragraph{Three-step adaptive pipeline.}\nAt each control step, the pipeline executes:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Uncertainty probe.} Draw $K{=}2$ samples $a^{(1)}, a^{(2)}$ from $\\pi_\\theta$ in a single batched forward pass. Compute the centroid $\\mathbf{c} = (a^{(1)} + a^{(2)})/2$ and the pairwise uncertainty $d_2 = \\|a^{(1)} - a^{(2)}\\|_2$. Select $\\hat{a} = \\argmin_{a \\in \\{a^{(1)}, a^{(2)}\\}} \\|a - \\mathbf{c}\\|_2$.\n  \\item \\textbf{Adaptive decision.} If $d_2 \\leq \\tau$ (low uncertainty), output $\\hat{a}$ directly---no further computation. If $d_2 > \\tau$ (high uncertainty), pass $\\hat{a}$ to the CRM for correction.\n  \\item \\textbf{Learned correction.} For high-uncertainty steps only, the CRM predicts a bounded residual: $\\hat{a}_{\\mathrm{out}} = \\hat{a} + \\boldsymbol{\\delta}$, where $\\boldsymbol{\\delta} = \\mathrm{CRM}(o_t, \\hat{a})$ and $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$~(\\ref{eq:crm}). The pipeline uses at most $K{=}2$ forward passes; performance gains come from learned correction, not brute-force sampling.\n\\end{enumerate}\n\\looseness=-1 The threshold $\\tau$ is a percentile of the empirical $d_2$ distribution from CRM training data. Higher $\\tau$ triggers correction on fewer steps; the optimal percentile is task-difficulty-dependent (Section~\\ref{sec:adaptive_k}). CRM inference adds ${\\sim}$0.3\\,ms; the VLA forward pass (${\\sim}$255\\,ms) dominates latency.\n",
      "numLines": 82,
      "startLine": 1,
      "totalLines": 82
    }
  }
}
```

</details>

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01YLanRRVL2tEXneX5wcVADM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "604bfe84-ea63-412b-9d52-7acf30d0acb1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JazqT8cHDEEnMbPcNrzs5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3722,
      "cache_read_input_tokens": 61713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3722
      },
      "output_tokens": 41,
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

_source line 47 · 2026-05-21T16:39:03.427Z_

<details><summary>↩ Tool result · `toolu_01YLanRRVL2tEXneX5wcVADM`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\looseness=-1 We evaluate the pipeline on two LIBERO task suites~\cite{liu2023libero}, asking: (i)~can a cheap uncertainty probe enable adaptive compute allocation? (ii)~what is the relative contribution of selection vs.\ correction? (iii)~how does conditioning interact with magnitude? (iv)~where does the pipeline fail?
6	
7	\subsection{Setup}
8	\label{sec:exp_setup}
9	
10	\paragraph{Benchmarks and base VLA.}
11	We use LIBERO-Object (10 tasks, novel object instances) and LIBERO-Spatial (10 tasks, spatial reasoning). Each task is evaluated over 10 rollouts (max 300 steps); success is binary.
12	We build on SmolVLA~\cite{shukor2025smolvla} (450M parameters, flow matching), using dual-camera RGB ($256{\times}256$) and 8D proprioceptive state. Actions are 7D (6D pose + 1D gripper); the gripper is thresholded outside the pipeline.
13	
14	\paragraph{Baselines.}
15	All use the same frozen SmolVLA: \textbf{VLA-only} ($K{=}1$, no correction), \textbf{Random} ($K{=}5{/}10$, uniform sample, no CRM), and \textbf{Argmin} ($K{=}5{/}10$, $L_2$ selection, no CRM).
16	
17	\paragraph{Training and statistics.}
18	CRM is trained on 26{,}737 samples (10 demos $\times$ 20 tasks, $K{=}10$ forward passes each), Adam $\mathrm{lr}{=}10^{-3}$, batch 32, 50 epochs, $\varepsilon{=}0.2$. All evaluation tasks are covered by CRM training data (in-distribution).
19	We report seed-level Mann-Whitney U tests (two-sided); 3--7 seeds per condition, none discarded.
20	
21	\subsection{Adaptive Inference-Time Compute}
22	\label{sec:adaptive_k}
23	
24	The key question is whether compute can be allocated adaptively per step rather than using a fixed $K$ for all steps. We validate the $K{=}2$ $L_2$ probe (Section~\ref{sec:adaptive_k_method}) and evaluate threshold-based adaptive allocation.
25	
26	\paragraph{Uncertainty signal validation.}
27	The pairwise $L_2$ distance from $K{=}2$ samples correlates near-perfectly with the full $K{=}10$ sample variance ($\rho{=}0.9979$, Spearman; Figure~\ref{fig:k2_correlation}). Three alternative signals fail: flow-matching velocity divergence (FMVD, $\rho{=}0.08$), CRM correction magnitude at $K{=}1$ ($\rho{=}0.15$), and CRM correction magnitude at $K{=}2$ ($\rho{=}0.13$). The $K{=}2$ $L_2$ distance is the only viable per-step uncertainty proxy among the four candidates tested.
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\linewidth]{figures/fig5_k2_correlation.pdf}
32	\caption{Per-step uncertainty signals vs.\ $K{=}10$ sample variance. (a)~$K{=}2$ $L_2$ pairwise distance achieves $\rho{=}0.9979$, validating it as a near-perfect proxy. (b)~FMVD ($\rho{=}0.08$) shows no correlation, confirming that ODE-space signals do not predict action-space variance.}
33	\label{fig:k2_correlation}
34	\end{figure}
35	
36	\paragraph{Threshold sweep (variable-$K$ protocol).}
37	To validate the $K{=}2$ probe as an uncertainty signal independently of Plan~A, we test a variable-$K$ protocol that expands to $K{=}10$ on high-uncertainty steps (details in Appendix~\ref{sec:spatial_adaptive}).
38	\looseness=-1 Table~\ref{tab:adaptive} reports performance on LIBERO-Object. Among variable-$K$ thresholds, P50 achieves the best trade-off (91\% of $K{=}10$ SR at 38\% compute). However, Plan~A ($K{=}2$ selective CRM) Pareto-dominates all thresholds: $18.3$\% at avg\_$K{=}2$, exceeding fixed $K{=}10$ ($16.8$\%) with 80\% fewer VLA forward passes. The sweep confirms the $K{=}2$ signal is effective, but selective CRM is its optimal utilization.
39	\looseness=-1 The optimal threshold shifts with task difficulty: on Spatial (easier), P90 reaches 33.0\% at avg\_$K{=}3.55$ while P25 drops to 31.7\%; on Object (harder) P50 is the sweet spot (Appendix~\ref{sec:spatial_adaptive}).
40	
41	\begin{table}[t]
42	\centering
43	\caption{Adaptive $K$ threshold sweep and Plan~A on LIBERO-Object ($n{=}3$ seeds unless noted). Thresholds $\tau$ on training-set $L_2$ distance: P90${=}$0.127, P75${=}$0.099, P50${=}$0.075, P25${=}$0.055. Plan~A Pareto-dominates all variable-$K$ thresholds. $^\ddagger$\,Seed set differs from Table~\ref{tab:main} ($11.0$\%, $n{=}8$). $^\S$\,$n{=}6$. $^\|$\,$n{=}8$.}
44	\label{tab:adaptive}
45	\small
46	\begin{tabular}{lcccc}
47	\toprule
48	$\tau$ & SR (\%) & avg\_$K$ & fast path (\%) & SR/SR$_{K{=}10}$ \\
49	\midrule
50	\textbf{Plan~A (ours)} & $\mathbf{18.3 \pm 2.1}$ & \textbf{2.0} & \textbf{16.3} & \textbf{109\%} \\
51	\midrule
52	P90 & $13.3 \pm 1.2$ & 2.62 & 92.2 & 79\% \\
53	P75 & $13.7 \pm 2.1$ & 3.08 & 86.5 & 82\% \\
54	P50 & $15.3 \pm 1.2$ & 3.81 & 77.3 & 91\% \\
55	P25 & $14.3 \pm 1.2$ & 4.79 & 65.1 & 85\% \\
56	\midrule
57	Fixed $K{=}10^\S$ & $16.8 \pm 1.8$ & 10.0 & 0 & 100\% \\
58	VLA-only$^{\ddagger\|}$ & $10.9 \pm 1.4$ & 1.0 & --- & 65\% \\
59	\bottomrule
60	\end{tabular}
61	\end{table}
62	
63	\subsection{Main Results and Component Decomposition}
64	\label{sec:main_results}
65	
66	Table~\ref{tab:main} compares Plan~A (Section~\ref{sec:adaptive_k_method}) with analysis baselines that isolate the contribution of selection and correction at fixed $K$.
67	
68	\paragraph{Plan~A: selective correction at $K{=}2$.}
69	\looseness=-1 The proposed pipeline achieves $18.3 \pm 2.1$\% on Object (3 seeds) and $35.0 \pm 1.0$\% on Spatial, exceeding CRM $K{=}10$ ($16.8$\%, $34.4$\%) with 80\% fewer VLA forward passes and matching CRM $K{=}20$ ($18.8$\%, $34.3$\%) at 90\% fewer (Appendix~\ref{sec:k_scaling}). The CRM trigger rate is task-dependent: 83.7\% on Object (16.3\% fast-path steps) and 97.6\% on Spatial, where correction is almost universally beneficial. Selective application outperforms unconditional correction at $K{=}10$, consistent with over-triggering degrading performance (P25 $<$ P50, Table~\ref{tab:adaptive}). With $K{=}2$, the centroid has lower variance than at $K{=}10$, providing a cleaner starting point for bounded correction.
70	
71	\begin{table}[t]
72	\centering
73	\caption{Task success rate (\%\,$\uparrow$) on LIBERO-Object and LIBERO-Spatial. Mean $\pm$ std; $n$: Object seeds. Spatial $n$: 5 (VLA-only), 4 ($K{=}5$), 3 (Random $K{=}10$, CRM $K{=}10$, Plan~A). $\Delta$: vs.\ VLA-only. Top: proposed method (Section~\ref{sec:adaptive_k_method}); middle/bottom: analysis baselines.}
74	\label{tab:main}
75	\small
76	\begin{tabular}{lccccc}
77	\toprule
78	Method & $K$ & Object (\%) & $n$ & Spatial (\%) & $\Delta$ Obj \\
79	\midrule
80	\textbf{Plan~A (ours)} & \textbf{2} & $\mathbf{18.3 \pm 2.1}$ & \textbf{3} & $\mathbf{35.0 \pm 1.0}$ & $\mathbf{+7.3}$ \\
81	\midrule
82	VLA-only & 1 & $11.0 \pm 1.3$ & 8 & $29.4 \pm 1.5$ & --- \\
83	Random & 5 & $10.5 \pm 2.9$ & 4 & --- & $-0.5$ \\
84	Argmin & 5 & $13.0 \pm 1.6$ & 4 & --- & $+2.0$ \\
85	CRM obs\_only & 5 & $16.0 \pm 2.2$ & 7 & $34.5 \pm 2.1$ & $+5.0$ \\
86	\midrule
87	Random & 10 & $9.7 \pm 1.5$ & 6 & $29.3 \pm 4.2$ & $-1.3$ \\
88	Argmin & 10 & $12.3 \pm 2.6$ & 6 & --- & $+1.3$ \\
89	CRM obs\_only & 10 & $16.8 \pm 1.8$ & 6 & $34.4 \pm 1.5$ & $+5.8$ \\
90	\midrule
91	CRM perdof & 10 & $11.0 \pm 1.8$ & 6 & --- & $\phantom{+}0.0$ \\
92	CRM scalar & 10 & $\phantom{0}8.5 \pm 1.5$ & 4 & --- & $-2.5$ \\
93	\bottomrule
94	\end{tabular}
95	\end{table}
96	
97	\paragraph{Component decomposition (fixed-$K$ analysis).}
98	\looseness=-2 The remaining rows of Table~\ref{tab:main} are analysis baselines at fixed $K$, not proposed methods. CRM obs\_only at $K{=}10$ reaches $16.8 \pm 1.8$\% on Object ($p{=}0.003$) and $34.4 \pm 1.5$\% on Spatial. Random selection fails to exceed VLA-only on either benchmark (Object $9.7$\% vs.\ $11.0$\%; Spatial $29.3$\% vs.\ $29.4$\%), confirming that sampling more actions without ranking is insufficient; argmin adds $+$1.3\,pp, and CRM correction contributes $+$4.5\,pp (78\% of the gain). At $K{=}5$, correction contributes 55\%. At $K{=}1$, correction without centering falls below baseline ($10.3$\%), validating the $K{\geq}2$ requirement.
99	
100	\vspace{-2pt}
101	\subsection{Conditioning, Magnitude, and Distribution Shift}
102	\label{sec:magnitude_results}
103	\label{sec:failure_modes}
104	
105	\looseness=-2 The CRM conditioning interacts with $\varepsilon$ (Appendix~\ref{sec:magnitude_appendix}): obs\_only is stable (12.5--16.8\%); perdof collapses (${\sim}$14\% $\to$ 0\%) because $K{=}10$ in $d{=}7$ yields effectively low-rank covariance and large $\varepsilon$ amplifies noisy per-DOF estimates; scalar (8.5\%) falls below VLA-only. Three distribution shifts define further boundaries: (1)~input ($K{=}1$, 10.3\%); (2)~task (near-OOD $-$12\,pp, far-OOD neutral $p{=}0.46$); (3)~feature (perdof $\to$ 0\%). All share a mechanism: CRM degrades when inputs depart from training distribution (Appendix~\ref{sec:per_task}). Plan~A runs 1.82$\times$ faster than $K{=}10$ with 0.28\,ms CRM overhead (Appendix~\ref{sec:latency}).
106	
107	We further validate cross-VLA generalization on $\pi_{0.5}$ (3.6B)~\cite{black2024pi0}; see Appendix~\ref{sec:cross_vla}.
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "c6c752f2-74bb-4447-9913-dc96713dbd6a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\looseness=-1 We evaluate the pipeline on two LIBERO task suites~\\cite{liu2023libero}, asking: (i)~can a cheap uncertainty probe enable adaptive compute allocation? (ii)~what is the relative contribution of selection vs.\\ correction? (iii)~how does conditioning interact with magnitude? (iv)~where does the pipeline fail?\n\n\\subsection{Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks and base VLA.}\nWe use LIBERO-Object (10 tasks, novel object instances) and LIBERO-Spatial (10 tasks, spatial reasoning). Each task is evaluated over 10 rollouts (max 300 steps); success is binary.\nWe build on SmolVLA~\\cite{shukor2025smolvla} (450M parameters, flow matching), using dual-camera RGB ($256{\\times}256$) and 8D proprioceptive state. Actions are 7D (6D pose + 1D gripper); the gripper is thresholded outside the pipeline.\n\n\\paragraph{Baselines.}\nAll use the same frozen SmolVLA: \\textbf{VLA-only} ($K{=}1$, no correction), \\textbf{Random} ($K{=}5{/}10$, uniform sample, no CRM), and \\textbf{Argmin} ($K{=}5{/}10$, $L_2$ selection, no CRM).\n\n\\paragraph{Training and statistics.}\nCRM is trained on 26{,}737 samples (10 demos $\\times$ 20 tasks, $K{=}10$ forward passes each), Adam $\\mathrm{lr}{=}10^{-3}$, batch 32, 50 epochs, $\\varepsilon{=}0.2$. All evaluation tasks are covered by CRM training data (in-distribution).\nWe report seed-level Mann-Whitney U tests (two-sided); 3--7 seeds per condition, none discarded.\n\n\\subsection{Adaptive Inference-Time Compute}\n\\label{sec:adaptive_k}\n\nThe key question is whether compute can be allocated adaptively per step rather than using a fixed $K$ for all steps. We validate the $K{=}2$ $L_2$ probe (Section~\\ref{sec:adaptive_k_method}) and evaluate threshold-based adaptive allocation.\n\n\\paragraph{Uncertainty signal validation.}\nThe pairwise $L_2$ distance from $K{=}2$ samples correlates near-perfectly with the full $K{=}10$ sample variance ($\\rho{=}0.9979$, Spearman; Figure~\\ref{fig:k2_correlation}). Three alternative signals fail: flow-matching velocity divergence (FMVD, $\\rho{=}0.08$), CRM correction magnitude at $K{=}1$ ($\\rho{=}0.15$), and CRM correction magnitude at $K{=}2$ ($\\rho{=}0.13$). The $K{=}2$ $L_2$ distance is the only viable per-step uncertainty proxy among the four candidates tested.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig5_k2_correlation.pdf}\n\\caption{Per-step uncertainty signals vs.\\ $K{=}10$ sample variance. (a)~$K{=}2$ $L_2$ pairwise distance achieves $\\rho{=}0.9979$, validating it as a near-perfect proxy. (b)~FMVD ($\\rho{=}0.08$) shows no correlation, confirming that ODE-space signals do not predict action-space variance.}\n\\label{fig:k2_correlation}\n\\end{figure}\n\n\\paragraph{Threshold sweep (variable-$K$ protocol).}\nTo validate the $K{=}2$ probe as an uncertainty signal independently of Plan~A, we test a variable-$K$ protocol that expands to $K{=}10$ on high-uncertainty steps (details in Appendix~\\ref{sec:spatial_adaptive}).\n\\looseness=-1 Table~\\ref{tab:adaptive} reports performance on LIBERO-Object. Among variable-$K$ thresholds, P50 achieves the best trade-off (91\\% of $K{=}10$ SR at 38\\% compute). However, Plan~A ($K{=}2$ selective CRM) Pareto-dominates all thresholds: $18.3$\\% at avg\\_$K{=}2$, exceeding fixed $K{=}10$ ($16.8$\\%) with 80\\% fewer VLA forward passes. The sweep confirms the $K{=}2$ signal is effective, but selective CRM is its optimal utilization.\n\\looseness=-1 The optimal threshold shifts with task difficulty: on Spatial (easier), P90 reaches 33.0\\% at avg\\_$K{=}3.55$ while P25 drops to 31.7\\%; on Object (harder) P50 is the sweet spot (Appendix~\\ref{sec:spatial_adaptive}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Adaptive $K$ threshold sweep and Plan~A on LIBERO-Object ($n{=}3$ seeds unless noted). Thresholds $\\tau$ on training-set $L_2$ distance: P90${=}$0.127, P75${=}$0.099, P50${=}$0.075, P25${=}$0.055. Plan~A Pareto-dominates all variable-$K$ thresholds. $^\\ddagger$\\,Seed set differs from Table~\\ref{tab:main} ($11.0$\\%, $n{=}8$). $^\\S$\\,$n{=}6$. $^\\|$\\,$n{=}8$.}\n\\label{tab:adaptive}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\tau$ & SR (\\%) & avg\\_$K$ & fast path (\\%) & SR/SR$_{K{=}10}$ \\\\\n\\midrule\n\\textbf{Plan~A (ours)} & $\\mathbf{18.3 \\pm 2.1}$ & \\textbf{2.0} & \\textbf{16.3} & \\textbf{109\\%} \\\\\n\\midrule\nP90 & $13.3 \\pm 1.2$ & 2.62 & 92.2 & 79\\% \\\\\nP75 & $13.7 \\pm 2.1$ & 3.08 & 86.5 & 82\\% \\\\\nP50 & $15.3 \\pm 1.2$ & 3.81 & 77.3 & 91\\% \\\\\nP25 & $14.3 \\pm 1.2$ & 4.79 & 65.1 & 85\\% \\\\\n\\midrule\nFixed $K{=}10^\\S$ & $16.8 \\pm 1.8$ & 10.0 & 0 & 100\\% \\\\\nVLA-only$^{\\ddagger\\|}$ & $10.9 \\pm 1.4$ & 1.0 & --- & 65\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Main Results and Component Decomposition}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares Plan~A (Section~\\ref{sec:adaptive_k_method}) with analysis baselines that isolate the contribution of selection and correction at fixed $K$.\n\n\\paragraph{Plan~A: selective correction at $K{=}2$.}\n\\looseness=-1 The proposed pipeline achieves $18.3 \\pm 2.1$\\% on Object (3 seeds) and $35.0 \\pm 1.0$\\% on Spatial, exceeding CRM $K{=}10$ ($16.8$\\%, $34.4$\\%) with 80\\% fewer VLA forward passes and matching CRM $K{=}20$ ($18.8$\\%, $34.3$\\%) at 90\\% fewer (Appendix~\\ref{sec:k_scaling}). The CRM trigger rate is task-dependent: 83.7\\% on Object (16.3\\% fast-path steps) and 97.6\\% on Spatial, where correction is almost universally beneficial. Selective application outperforms unconditional correction at $K{=}10$, consistent with over-triggering degrading performance (P25 $<$ P50, Table~\\ref{tab:adaptive}). With $K{=}2$, the centroid has lower variance than at $K{=}10$, providing a cleaner starting point for bounded correction.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%\\,$\\uparrow$) on LIBERO-Object and LIBERO-Spatial. Mean $\\pm$ std; $n$: Object seeds. Spatial $n$: 5 (VLA-only), 4 ($K{=}5$), 3 (Random $K{=}10$, CRM $K{=}10$, Plan~A). $\\Delta$: vs.\\ VLA-only. Top: proposed method (Section~\\ref{sec:adaptive_k_method}); middle/bottom: analysis baselines.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & $K$ & Object (\\%) & $n$ & Spatial (\\%) & $\\Delta$ Obj \\\\\n\\midrule\n\\textbf{Plan~A (ours)} & \\textbf{2} & $\\mathbf{18.3 \\pm 2.1}$ & \\textbf{3} & $\\mathbf{35.0 \\pm 1.0}$ & $\\mathbf{+7.3}$ \\\\\n\\midrule\nVLA-only & 1 & $11.0 \\pm 1.3$ & 8 & $29.4 \\pm 1.5$ & --- \\\\\nRandom & 5 & $10.5 \\pm 2.9$ & 4 & --- & $-0.5$ \\\\\nArgmin & 5 & $13.0 \\pm 1.6$ & 4 & --- & $+2.0$ \\\\\nCRM obs\\_only & 5 & $16.0 \\pm 2.2$ & 7 & $34.5 \\pm 2.1$ & $+5.0$ \\\\\n\\midrule\nRandom & 10 & $9.7 \\pm 1.5$ & 6 & $29.3 \\pm 4.2$ & $-1.3$ \\\\\nArgmin & 10 & $12.3 \\pm 2.6$ & 6 & --- & $+1.3$ \\\\\nCRM obs\\_only & 10 & $16.8 \\pm 1.8$ & 6 & $34.4 \\pm 1.5$ & $+5.8$ \\\\\n\\midrule\nCRM perdof & 10 & $11.0 \\pm 1.8$ & 6 & --- & $\\phantom{+}0.0$ \\\\\nCRM scalar & 10 & $\\phantom{0}8.5 \\pm 1.5$ & 4 & --- & $-2.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Component decomposition (fixed-$K$ analysis).}\n\\looseness=-2 The remaining rows of Table~\\ref{tab:main} are analysis baselines at fixed $K$, not proposed methods. CRM obs\\_only at $K{=}10$ reaches $16.8 \\pm 1.8$\\% on Object ($p{=}0.003$) and $34.4 \\pm 1.5$\\% on Spatial. Random selection fails to exceed VLA-only on either benchmark (Object $9.7$\\% vs.\\ $11.0$\\%; Spatial $29.3$\\% vs.\\ $29.4$\\%), confirming that sampling more actions without ranking is insufficient; argmin adds $+$1.3\\,pp, and CRM correction contributes $+$4.5\\,pp (78\\% of the gain). At $K{=}5$, correction contributes 55\\%. At $K{=}1$, correction without centering falls below baseline ($10.3$\\%), validating the $K{\\geq}2$ requirement.\n\n\\vspace{-2pt}\n\\subsection{Conditioning, Magnitude, and Distribution Shift}\n\\label{sec:magnitude_results}\n\\label{sec:failure_modes}\n\n\\looseness=-2 The CRM conditioning interacts with $\\varepsilon$ (Appendix~\\ref{sec:magnitude_appendix}): obs\\_only is stable (12.5--16.8\\%); perdof collapses (${\\sim}$14\\% $\\to$ 0\\%) because $K{=}10$ in $d{=}7$ yields effectively low-rank covariance and large $\\varepsilon$ amplifies noisy per-DOF estimates; scalar (8.5\\%) falls below VLA-only. Three distribution shifts define further boundaries: (1)~input ($K{=}1$, 10.3\\%); (2)~task (near-OOD $-$12\\,pp, far-OOD neutral $p{=}0.46$); (3)~feature (perdof $\\to$ 0\\%). All share a mechanism: CRM degrades when inputs depart from training distribution (Appendix~\\ref{sec:per_task}). Plan~A runs 1.82$\\times$ faster than $K{=}10$ with 0.28\\,ms CRM overhead (Appendix~\\ref{sec:latency}).\n\nWe further validate cross-VLA generalization on $\\pi_{0.5}$ (3.6B)~\\cite{black2024pi0}; see Appendix~\\ref{sec:cross_vla}.\n",
      "numLines": 108,
      "startLine": 1,
      "totalLines": 108
    }
  }
}
```

</details>

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01RmCsbsBEnW63odVsXyejmo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "eec27ca5-270c-4497-a26d-d1238e007fe9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Npa58XwtGSNwbJ3F4szDrj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9385,
      "cache_read_input_tokens": 65435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9385
      },
      "output_tokens": 41,
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

_source line 49 · 2026-05-21T16:39:07.722Z_

<details><summary>↩ Tool result · `toolu_01RmCsbsBEnW63odVsXyejmo`</summary>

```text
1	
2	\enlargethispage{1\baselineskip}
3	\vspace{-6pt}
4	\section{Conclusion}
5	\label{sec:conclusion}
6	\vspace{-2pt}
7	
8	\looseness=-2 We presented an adaptive inference-time compute pipeline for frozen flow-matching VLAs. The $K{=}2$ $L_2$ probe ($\rho{=}0.9979$) gates selective CRM correction, achieving $18.3$\% Object / $35.0$\% Spatial ($+$7.3 / $+$5.6\,pp vs.\ VLA-only) while matching fixed-$K{=}10$ with 80\% fewer VLA forward passes. On fixed-$K$ baselines, learned correction contributes 55--78\% of the gain.
9	\textbf{Limitations.}\enspace All experiments use LIBERO in simulation with SmolVLA (450M); real-robot transfer and larger VLAs are untested. The CRM requires task-specific calibration ($-$12\,pp on unseen tasks) and stochastic sample diversity, excluding tokenized VLAs (Appendix~\ref{sec:applicability}); generalization to diffusion-based VLAs is open. AI tools assisted with code and manuscript.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "5d250e20-5688-4a2f-b3b5-0aad034e426f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex",
      "content": "\n\\enlargethispage{1\\baselineskip}\n\\vspace{-6pt}\n\\section{Conclusion}\n\\label{sec:conclusion}\n\\vspace{-2pt}\n\n\\looseness=-2 We presented an adaptive inference-time compute pipeline for frozen flow-matching VLAs. The $K{=}2$ $L_2$ probe ($\\rho{=}0.9979$) gates selective CRM correction, achieving $18.3$\\% Object / $35.0$\\% Spatial ($+$7.3 / $+$5.6\\,pp vs.\\ VLA-only) while matching fixed-$K{=}10$ with 80\\% fewer VLA forward passes. On fixed-$K$ baselines, learned correction contributes 55--78\\% of the gain.\n\\textbf{Limitations.}\\enspace All experiments use LIBERO in simulation with SmolVLA (450M); real-robot transfer and larger VLAs are untested. The CRM requires task-specific calibration ($-$12\\,pp on unseen tasks) and stochastic sample diversity, excluding tokenized VLAs (Appendix~\\ref{sec:applicability}); generalization to diffusion-based VLAs is open. AI tools assisted with code and manuscript.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_0147KuLu5RBYqU6xEyfHV4QC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "1901f297-c834-460d-975e-0ae22c964f9a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Npa58XwtGSNwbJ3F4szDrj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9385,
      "cache_read_input_tokens": 65435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9385
      },
      "output_tokens": 41,
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

_source line 51 · 2026-05-21T16:39:08.762Z_

<details><summary>↩ Tool result · `toolu_0147KuLu5RBYqU6xEyfHV4QC`</summary>

```text
1	
2	\appendix
3	
4	\section{Component Decomposition Figure}
5	\label{sec:decomposition_appendix}
6	
7	\begin{figure}[h]
8	\centering
9	\includegraphics[width=\linewidth]{figures/fig3_decomposition.pdf}
10	\caption{Component decomposition at $K{=}5$ and $K{=}10$ on LIBERO-Object. At both operating points, correction (CRM bar height above argmin) accounts for the majority of the gain. Random selection at $K{=}5$ is harmful (below VLA-only dashed line).}
11	\label{fig:decomposition}
12	\end{figure}
13	
14	\section{Conditioning-Magnitude Dose-Response}
15	\label{sec:magnitude_appendix}
16	
17	\begin{figure}[h]
18	\centering
19	\includegraphics[width=\linewidth]{figures/fig2_magnitude.pdf}
20	\caption{Success rate vs.\ magnitude bound $\varepsilon$ on LIBERO-Object. obs\_only (blue) remains above VLA-only (dashed) across all $\varepsilon$ including uncapped (${\approx}$1.42). perdof (orange) collapses progressively to 0\%. Error bars: $\pm$1 std.}
21	\label{fig:magnitude}
22	\end{figure}
23	
24	\section{Inference-Time Scaling with $K$}
25	\label{sec:k_scaling}
26	
27	Figure~\ref{fig:kvalue} plots task success rate against the number of VLA samples $K$.
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\linewidth]{figures/fig3_kvalue.pdf}
32	\caption{Success rate (\%) vs.\ number of VLA samples $K$ on LIBERO-Object (obs\_only, $\varepsilon{=}0.2$). Reference lines: VLA-only ($11.0$\%, 8 seeds) and Argmin-only ($12.3$\%, 6 seeds). Error bars: $\pm$1 std. Note: figure reference lines reflect seed sets used at generation time; Table~\ref{tab:main} reports final aggregated statistics.}
33	\label{fig:kvalue}
34	\end{figure}
35	
36	Table~\ref{tab:k_ablation} reports the full $K$-ablation on both benchmarks.
37	
38	\begin{table}[h]
39	\centering
40	\caption{Success rate (\%) vs.\ number of VLA samples $K$ on LIBERO-Object and LIBERO-Spatial. Plan~A uses $K{=}2$ with selective CRM; all other CRM rows use unconditional correction at fixed $K$. Plan~A matches CRM $K{=}20$ with 90\% fewer VLA forward passes.}
41	\label{tab:k_ablation}
42	\small
43	\begin{tabular}{llcc}
44	\toprule
45	Method & $K$ & Object (\%) & Spatial (\%) \\
46	\midrule
47	VLA-only & 1 & $11.0 \pm 1.3$ & $29.4 \pm 1.5$ \\
48	\textbf{Plan~A (ours)} & \textbf{2} & $\mathbf{18.3 \pm 2.1}$ & $\mathbf{35.0 \pm 1.0}$ \\
49	CRM obs\_only & 5 & $16.0 \pm 2.2$ & $34.5 \pm 2.1$ \\
50	CRM obs\_only & 10 & $16.8 \pm 1.8$ & $34.4 \pm 1.5$ \\
51	CRM obs\_only & 20 & $18.8 \pm 1.0$ & $34.3 \pm 0.6$ \\
52	\bottomrule
53	\end{tabular}
54	\end{table}
55	
56	Performance improves with $K$ but saturates: Object rises from $11.0$\% ($K{=}1$) to $16.0$\% ($K{=}5$, $+$5.0\,pp) to $16.8$\% ($K{=}10$, $+$0.8\,pp) to $18.8$\% ($K{=}20$, $+$2.0\,pp, 4 seeds). On Spatial, CRM at $K{=}5{/}10{/}20$ clusters within 0.2\,pp ($34.3$--$34.5$\%), indicating complete saturation.
57	Plan~A ($K{=}2$) matches CRM $K{=}20$ on Object ($18.3$\% vs.\ $18.8$\%) and exceeds it on Spatial ($35.0$\% vs.\ $34.3$\%), using 90\% fewer VLA forward passes. This confirms that the gains derive from learned correction, not brute-force sampling.
58	At $K{=}1$, CRM correction alone falls below the VLA-only baseline (10.3\% vs.\ $11.0$\%), because the single sample lacks argmin centering and shifts outside the CRM's training distribution. Multi-sample selection is an enabling condition for effective correction.
59	The diminishing-returns pattern is loosely analogous to inference-time compute scaling in LLMs~\cite{snell2024scaling}, though the mechanism differs: in our setting, additional samples improve the starting point for correction rather than enabling better selection.
60	With batched inference (shared KV cache), $K{=}10$ sampling takes ${\sim}$255\,ms, plus $<$\,1\,ms for CRM inference and argmin selection. See Appendix~\ref{sec:latency} for the full timing breakdown.
61	
62	
63	\section{Spatial Adaptive $K$ Threshold Sweep}
64	\label{sec:spatial_adaptive}
65	
66	Table~\ref{tab:adaptive_spatial} reports the adaptive $K$ threshold sweep on LIBERO-Spatial, complementing the Object sweep in Table~\ref{tab:adaptive}.
67	
68	\begin{table}[h]
69	\centering
70	\caption{Adaptive $K$ threshold sweep and Plan~A on LIBERO-Spatial ($n{=}3$ seeds unless noted). Same thresholds $\tau$ as Table~\ref{tab:adaptive}. Plan~A Pareto-dominates all variable-$K$ thresholds: highest SR at lowest avg\_$K$. $^\dagger$\,$n{=}2$ (seed 44 pending).}
71	\label{tab:adaptive_spatial}
72	\small
73	\begin{tabular}{lcccc}
74	\toprule
75	$\tau$ & SR (\%) & avg\_$K$ & fast path (\%) & SR/SR$_{K{=}10}$ \\
76	\midrule
77	\textbf{Plan~A (ours)} & $\mathbf{35.0 \pm 1.0}$ & \textbf{2.0} & \textbf{84} & \textbf{102\%} \\
78	\midrule
79	P90$^\dagger$ & $31.5$ & 3.55 & 80.6 & 92\% \\
80	P75 & $32.7 \pm 1.5$ & 5.02 & 62.1 & 95\% \\
81	P50 & $32.0 \pm 1.7$ & 6.35 & 45.6 & 93\% \\
82	P25 & $31.7 \pm 1.5$ & 7.65 & 29.4 & 92\% \\
83	\midrule
84	Fixed $K{=}10$ & $34.4 \pm 1.5$ & 10.0 & 0 & 100\% \\
85	\bottomrule
86	\end{tabular}
87	\end{table}
88	
89	Plan~A ($K{=}2$ selective CRM) Pareto-dominates all variable-$K$ thresholds on Spatial: $35.0 \pm 1.0$\% at avg\_$K{=}2$ versus the best variable-$K$ threshold P75 at $32.7$\% with avg\_$K{=}5.02$. The variable-$K$ thresholds show a monotonic SR decrease from P90 to P25, contrasting with the non-monotonic Object pattern (P50 $>$ P25 $>$ P75). This confirms that the optimal correction frequency is task-difficulty-dependent and that the uncertainty signal is effective---but its optimal utilization is $K{=}2$ selective CRM rather than variable-$K$ expansion.
90	
91	
92	\section{Applicability Boundary: Stochastic VLA Diversity}
93	\label{sec:applicability}
94	
95	The multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\cite{kim2024openvla} (autoregressive tokenization, 7B).
96	
97	\begin{figure}[h]
98	\centering
99	\includegraphics[width=\linewidth]{figures/fig4_diversity.pdf}
100	\caption{Per-DOF action variance (log scale) across $K{=}10$ samples for SmolVLA (flow-matching) and OpenVLA (tokenized). OpenVLA produces 8/10 identical samples at temperature $T{=}0.5$, with per-DOF variance below $10^{-30}$ for most dimensions.}
101	\label{fig:diversity}
102	\end{figure}
103	
104	Figure~\ref{fig:diversity} shows the contrast: SmolVLA produces meaningfully diverse samples across all action dimensions, while OpenVLA at temperature $T{=}0.5$ generates 8 out of 10 identical action sequences, with per-DOF variance below $10^{-30}$ for most dimensions.
105	This near-determinism arises from autoregressive token selection: the argmax decoding at each token position collapses the distribution to a single mode, and moderate temperature fails to overcome the peaked distribution.
106	
107	This result establishes an applicability boundary: multi-sample inference-time correction is specific to stochastic generative VLAs (flow-matching, diffusion). Tokenized VLAs lack the action diversity that selection and correction rely on.
108	The boundary is architectural, not a limitation of our method: any inference-time approach that draws multiple action candidates requires the base policy to produce diverse samples.
109	
110	
111	\section{Per-Task Analysis}
112	\label{sec:per_task}
113	
114	Table~\ref{tab:pertask} reports per-task success rates on LIBERO-Object (seed 42) for the VLA-only baseline, Argmin selection, and obs\_only at two magnitude bounds.
115	
116	\begin{table}[h]
117	\centering
118	\caption{Per-task success rate (\%) on LIBERO-Object (seed 42, 10 rollouts per task). Tasks ordered by obs\_only $\varepsilon{=}0.2$ improvement over VLA-only.}
119	\label{tab:pertask}
120	\small
121	\begin{tabular}{lcccc}
122	\toprule
123	Task & VLA-only & Argmin & obs\_only 0.1 & obs\_only 0.2 \\
124	\midrule
125	chocolate\_pudding & 20 & 30 & 50 & \textbf{60} \\
126	ketchup            &  0 &  0 & 10 & \textbf{20} \\
127	bbq\_sauce         & 20 & 30 & \textbf{40} & \textbf{40} \\
128	salad\_dressing    & 20 & 10 & 20 & \textbf{30} \\
129	butter             &  0 & \textbf{10} & \textbf{10} & \textbf{10} \\
130	milk               & 10 & 10 & \textbf{20} & \textbf{20} \\
131	orange\_juice      & \textbf{30} & \textbf{30} & \textbf{30} & \textbf{30} \\
132	tomato\_sauce      & \textbf{10} &  0 &  0 & \textbf{10} \\
133	alphabet\_soup     &  0 &  0 &  0 &  0 \\
134	cream\_cheese      & \textbf{10} &  0 & \textbf{10} &  0 \\
135	\bottomrule
136	\end{tabular}
137	\end{table}
138	
139	Improvement concentrates on medium-difficulty tasks.
140	The largest improvements appear on tasks where the frozen VLA partially succeeds but makes correctable errors: chocolate\_pudding (+40\,pp, from 20\% to 60\%), bbq\_sauce and ketchup (+20\,pp each), and salad\_dressing (+10\,pp).
141	These four tasks account for 9 of the 10 additional successes.
142	Conversely, four tasks (alphabet\_soup, cream\_cheese, tomato\_sauce, butter) remain at 0--10\% across all methods.
143	For these tasks, the base policy fails so completely that local action-level correction cannot recover a viable trajectory.
144	
145	Correction benefits tasks where the frozen VLA partially succeeds but makes correctable errors, rather than tasks where the base policy fails catastrophically or already succeeds reliably.
146	This pattern is expected for a residual correction approach bounded by $\varepsilon$: the CRM can fix small deviations in grasp pose or approach angle, but cannot recover from fundamental planning failures.
147	The concentrated improvement profile also addresses the question of effect size: the aggregate +10\,pp is not a uniform +1\,pp across 10 tasks, but a substantial +20--40\,pp on specific tasks diluted by tasks outside the correctable regime.
148	
149	
150	\section{Latency Breakdown}
151	\label{sec:latency}
152	
153	Table~\ref{tab:latency} reports per-component wall-clock timing under batched inference on a single NVIDIA RTX 4090 (CUDA 12.8, $N{=}1{,}000$ runs).
154	
155	\begin{table}[h]
156	\centering
157	\caption{Per-step latency breakdown (ms, batched inference). CRM inference adds 0.28\,ms ($<$\,0.1\% overhead). Plan~A fast path runs at ${\sim}$4.0\,Hz; full path at ${\sim}$2.2\,Hz.}
158	\label{tab:latency}
159	\small
160	\begin{tabular}{lc}
161	\toprule
162	Component & Mean (ms) \\
163	\midrule
164	VLA E2E $K{=}1$ (batched) & 256.5 \\
165	VLA E2E $K{=}10$ (batched) & 253.2 \\
166	CRM forward & 0.28 \\
167	\midrule
168	Plan~A fast path ($K{=}2$, no CRM) & 252.9 \\
169	Plan~A full path ($K{=}2$ + CRM) & 459.6 \\
170	\midrule
171	Adaptive speedup vs.\ $K{=}10$ & $1.82{\times}$ \\
172	\bottomrule
173	\end{tabular}
174	\end{table}
175	
176	Under batched inference with shared KV cache, $K{=}2$ latency (${\sim}$253\,ms) is comparable to $K{=}1$ (${\sim}$257\,ms) because the flow-matching denoising of both samples runs in parallel. CRM inference adds only 0.28\,ms, making the correction overhead negligible. Plan~A's $K{=}2$ pipeline is 1.82$\times$ faster than the $K{=}10$ analysis baseline while achieving equal or higher success rate, because the 80\% reduction in VLA forward passes far outweighs the CRM overhead ($-$1.66\% net latency vs.\ $K{=}10$).
177	
178	
179	\section{Cross-VLA Generalization}
180	\label{sec:cross_vla}
181	
182	To test whether the pipeline generalizes beyond SmolVLA, we evaluate on $\pi_{0.5}$~\cite{black2024pi0}, a 3.6B-parameter flow-matching VLA built on PaliGemma2 (vision) and Gemma2 (language) with 50-step action chunking. We use the same LIBERO-Object and LIBERO-Spatial benchmarks with identical evaluation protocol (10 rollouts per task, 3 seeds). The CRM architecture is unchanged; only the input projection differs, mapping $\pi_{0.5}$'s 2048-dimensional observation features to the CRM input via a learned linear layer (vs.\ SmolVLA's 960D direct concatenation).
183	
184	\begin{table}[h]
185	\centering
186	\caption{Cross-VLA generalization: $\pi_{0.5}$ (3.6B) on LIBERO. The $\pi_{0.5}$ baseline operates at $81$--$85$\% SR, substantially above SmolVLA's $11$--$29$\%, constraining the headroom for correction. $n{=}3$ seeds.}
187	\label{tab:cross_vla}
188	\small
189	\begin{tabular}{lccc}
190	\toprule
191	Method & $K$ & Object (\%) & Spatial (\%) \\
192	\midrule
193	$\pi_{0.5}$ VLA-only & 1 & $81.5 \pm 0.5$ & $84.2 \pm 1.0$ \\
194	$\pi_{0.5}$ Plan~A & 2 & \placeholder{} & \placeholder{} \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	Table~\ref{tab:cross_vla} reports results. The $\pi_{0.5}$ baseline already achieves $81.5 \pm 0.5$\% on Object and $84.2 \pm 1.0$\% on Spatial---substantially above SmolVLA's $11.0$\% / $29.4$\%---leaving limited headroom for post-hoc correction. Plan~A results are pending (\placeholder{}).
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "07a7fb1e-c34f-48cb-9f87-946fb7192db7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex",
      "content": "\n\\appendix\n\n\\section{Component Decomposition Figure}\n\\label{sec:decomposition_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig3_decomposition.pdf}\n\\caption{Component decomposition at $K{=}5$ and $K{=}10$ on LIBERO-Object. At both operating points, correction (CRM bar height above argmin) accounts for the majority of the gain. Random selection at $K{=}5$ is harmful (below VLA-only dashed line).}\n\\label{fig:decomposition}\n\\end{figure}\n\n\\section{Conditioning-Magnitude Dose-Response}\n\\label{sec:magnitude_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig2_magnitude.pdf}\n\\caption{Success rate vs.\\ magnitude bound $\\varepsilon$ on LIBERO-Object. obs\\_only (blue) remains above VLA-only (dashed) across all $\\varepsilon$ including uncapped (${\\approx}$1.42). perdof (orange) collapses progressively to 0\\%. Error bars: $\\pm$1 std.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\section{Inference-Time Scaling with $K$}\n\\label{sec:k_scaling}\n\nFigure~\\ref{fig:kvalue} plots task success rate against the number of VLA samples $K$.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig3_kvalue.pdf}\n\\caption{Success rate (\\%) vs.\\ number of VLA samples $K$ on LIBERO-Object (obs\\_only, $\\varepsilon{=}0.2$). Reference lines: VLA-only ($11.0$\\%, 8 seeds) and Argmin-only ($12.3$\\%, 6 seeds). Error bars: $\\pm$1 std. Note: figure reference lines reflect seed sets used at generation time; Table~\\ref{tab:main} reports final aggregated statistics.}\n\\label{fig:kvalue}\n\\end{figure}\n\nTable~\\ref{tab:k_ablation} reports the full $K$-ablation on both benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Success rate (\\%) vs.\\ number of VLA samples $K$ on LIBERO-Object and LIBERO-Spatial. Plan~A uses $K{=}2$ with selective CRM; all other CRM rows use unconditional correction at fixed $K$. Plan~A matches CRM $K{=}20$ with 90\\% fewer VLA forward passes.}\n\\label{tab:k_ablation}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nMethod & $K$ & Object (\\%) & Spatial (\\%) \\\\\n\\midrule\nVLA-only & 1 & $11.0 \\pm 1.3$ & $29.4 \\pm 1.5$ \\\\\n\\textbf{Plan~A (ours)} & \\textbf{2} & $\\mathbf{18.3 \\pm 2.1}$ & $\\mathbf{35.0 \\pm 1.0}$ \\\\\nCRM obs\\_only & 5 & $16.0 \\pm 2.2$ & $34.5 \\pm 2.1$ \\\\\nCRM obs\\_only & 10 & $16.8 \\pm 1.8$ & $34.4 \\pm 1.5$ \\\\\nCRM obs\\_only & 20 & $18.8 \\pm 1.0$ & $34.3 \\pm 0.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPerformance improves with $K$ but saturates: Object rises from $11.0$\\% ($K{=}1$) to $16.0$\\% ($K{=}5$, $+$5.0\\,pp) to $16.8$\\% ($K{=}10$, $+$0.8\\,pp) to $18.8$\\% ($K{=}20$, $+$2.0\\,pp, 4 seeds). On Spatial, CRM at $K{=}5{/}10{/}20$ clusters within 0.2\\,pp ($34.3$--$34.5$\\%), indicating complete saturation.\nPlan~A ($K{=}2$) matches CRM $K{=}20$ on Object ($18.3$\\% vs.\\ $18.8$\\%) and exceeds it on Spatial ($35.0$\\% vs.\\ $34.3$\\%), using 90\\% fewer VLA forward passes. This confirms that the gains derive from learned correction, not brute-force sampling.\nAt $K{=}1$, CRM correction alone falls below the VLA-only baseline (10.3\\% vs.\\ $11.0$\\%), because the single sample lacks argmin centering and shifts outside the CRM's training distribution. Multi-sample selection is an enabling condition for effective correction.\nThe diminishing-returns pattern is loosely analogous to inference-time compute scaling in LLMs~\\cite{snell2024scaling}, though the mechanism differs: in our setting, additional samples improve the starting point for correction rather than enabling better selection.\nWith batched inference (shared KV cache), $K{=}10$ sampling takes ${\\sim}$255\\,ms, plus $<$\\,1\\,ms for CRM inference and argmin selection. See Appendix~\\ref{sec:latency} for the full timing breakdown.\n\n\n\\section{Spatial Adaptive $K$ Threshold Sweep}\n\\label{sec:spatial_adaptive}\n\nTable~\\ref{tab:adaptive_spatial} reports the adaptive $K$ threshold sweep on LIBERO-Spatial, complementing the Object sweep in Table~\\ref{tab:adaptive}.\n\n\\begin{table}[h]\n\\centering\n\\caption{Adaptive $K$ threshold sweep and Plan~A on LIBERO-Spatial ($n{=}3$ seeds unless noted). Same thresholds $\\tau$ as Table~\\ref{tab:adaptive}. Plan~A Pareto-dominates all variable-$K$ thresholds: highest SR at lowest avg\\_$K$. $^\\dagger$\\,$n{=}2$ (seed 44 pending).}\n\\label{tab:adaptive_spatial}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\tau$ & SR (\\%) & avg\\_$K$ & fast path (\\%) & SR/SR$_{K{=}10}$ \\\\\n\\midrule\n\\textbf{Plan~A (ours)} & $\\mathbf{35.0 \\pm 1.0}$ & \\textbf{2.0} & \\textbf{84} & \\textbf{102\\%} \\\\\n\\midrule\nP90$^\\dagger$ & $31.5$ & 3.55 & 80.6 & 92\\% \\\\\nP75 & $32.7 \\pm 1.5$ & 5.02 & 62.1 & 95\\% \\\\\nP50 & $32.0 \\pm 1.7$ & 6.35 & 45.6 & 93\\% \\\\\nP25 & $31.7 \\pm 1.5$ & 7.65 & 29.4 & 92\\% \\\\\n\\midrule\nFixed $K{=}10$ & $34.4 \\pm 1.5$ & 10.0 & 0 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPlan~A ($K{=}2$ selective CRM) Pareto-dominates all variable-$K$ thresholds on Spatial: $35.0 \\pm 1.0$\\% at avg\\_$K{=}2$ versus the best variable-$K$ threshold P75 at $32.7$\\% with avg\\_$K{=}5.02$. The variable-$K$ thresholds show a monotonic SR decrease from P90 to P25, contrasting with the non-monotonic Object pattern (P50 $>$ P25 $>$ P75). This confirms that the optimal correction frequency is task-difficulty-dependent and that the uncertainty signal is effective---but its optimal utilization is $K{=}2$ selective CRM rather than variable-$K$ expansion.\n\n\n\\section{Applicability Boundary: Stochastic VLA Diversity}\n\\label{sec:applicability}\n\nThe multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\\cite{kim2024openvla} (autoregressive tokenization, 7B).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig4_diversity.pdf}\n\\caption{Per-DOF action variance (log scale) across $K{=}10$ samples for SmolVLA (flow-matching) and OpenVLA (tokenized). OpenVLA produces 8/10 identical samples at temperature $T{=}0.5$, with per-DOF variance below $10^{-30}$ for most dimensions.}\n\\label{fig:diversity}\n\\end{figure}\n\nFigure~\\ref{fig:diversity} shows the contrast: SmolVLA produces meaningfully diverse samples across all action dimensions, while OpenVLA at temperature $T{=}0.5$ generates 8 out of 10 identical action sequences, with per-DOF variance below $10^{-30}$ for most dimensions.\nThis near-determinism arises from autoregressive token selection: the argmax decoding at each token position collapses the distribution to a single mode, and moderate temperature fails to overcome the peaked distribution.\n\nThis result establishes an applicability boundary: multi-sample inference-time correction is specific to stochastic generative VLAs (flow-matching, diffusion). Tokenized VLAs lack the action diversity that selection and correction rely on.\nThe boundary is architectural, not a limitation of our method: any inference-time approach that draws multiple action candidates requires the base policy to produce diverse samples.\n\n\n\\section{Per-Task Analysis}\n\\label{sec:per_task}\n\nTable~\\ref{tab:pertask} reports per-task success rates on LIBERO-Object (seed 42) for the VLA-only baseline, Argmin selection, and obs\\_only at two magnitude bounds.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task success rate (\\%) on LIBERO-Object (seed 42, 10 rollouts per task). Tasks ordered by obs\\_only $\\varepsilon{=}0.2$ improvement over VLA-only.}\n\\label{tab:pertask}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & VLA-only & Argmin & obs\\_only 0.1 & obs\\_only 0.2 \\\\\n\\midrule\nchocolate\\_pudding & 20 & 30 & 50 & \\textbf{60} \\\\\nketchup            &  0 &  0 & 10 & \\textbf{20} \\\\\nbbq\\_sauce         & 20 & 30 & \\textbf{40} & \\textbf{40} \\\\\nsalad\\_dressing    & 20 & 10 & 20 & \\textbf{30} \\\\\nbutter             &  0 & \\textbf{10} & \\textbf{10} & \\textbf{10} \\\\\nmilk               & 10 & 10 & \\textbf{20} & \\textbf{20} \\\\\norange\\_juice      & \\textbf{30} & \\textbf{30} & \\textbf{30} & \\textbf{30} \\\\\ntomato\\_sauce      & \\textbf{10} &  0 &  0 & \\textbf{10} \\\\\nalphabet\\_soup     &  0 &  0 &  0 &  0 \\\\\ncream\\_cheese      & \\textbf{10} &  0 & \\textbf{10} &  0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nImprovement concentrates on medium-difficulty tasks.\nThe largest improvements appear on tasks where the frozen VLA partially succeeds but makes correctable errors: chocolate\\_pudding (+40\\,pp, from 20\\% to 60\\%), bbq\\_sauce and ketchup (+20\\,pp each), and salad\\_dressing (+10\\,pp).\nThese four tasks account for 9 of the 10 additional successes.\nConversely, four tasks (alphabet\\_soup, cream\\_cheese, tomato\\_sauce, butter) remain at 0--10\\% across all methods.\nFor these tasks, the base policy fails so completely that local action-level correction cannot recover a viable trajectory.\n\nCorrection benefits tasks where the frozen VLA partially succeeds but makes correctable errors, rather than tasks where the base policy fails catastrophically or already succeeds reliably.\nThis pattern is expected for a residual correction approach bounded by $\\varepsilon$: the CRM can fix small deviations in grasp pose or approach angle, but cannot recover from fundamental planning failures.\nThe concentrated improvement profile also addresses the question of effect size: the aggregate +10\\,pp is not a uniform +1\\,pp across 10 tasks, but a substantial +20--40\\,pp on specific tasks diluted by tasks outside the correctable regime.\n\n\n\\section{Latency Breakdown}\n\\label{sec:latency}\n\nTable~\\ref{tab:latency} reports per-component wall-clock timing under batched inference on a single NVIDIA RTX 4090 (CUDA 12.8, $N{=}1{,}000$ runs).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-step latency breakdown (ms, batched inference). CRM inference adds 0.28\\,ms ($<$\\,0.1\\% overhead). Plan~A fast path runs at ${\\sim}$4.0\\,Hz; full path at ${\\sim}$2.2\\,Hz.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComponent & Mean (ms) \\\\\n\\midrule\nVLA E2E $K{=}1$ (batched) & 256.5 \\\\\nVLA E2E $K{=}10$ (batched) & 253.2 \\\\\nCRM forward & 0.28 \\\\\n\\midrule\nPlan~A fast path ($K{=}2$, no CRM) & 252.9 \\\\\nPlan~A full path ($K{=}2$ + CRM) & 459.6 \\\\\n\\midrule\nAdaptive speedup vs.\\ $K{=}10$ & $1.82{\\times}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder batched inference with shared KV cache, $K{=}2$ latency (${\\sim}$253\\,ms) is comparable to $K{=}1$ (${\\sim}$257\\,ms) because the flow-matching denoising of both samples runs in parallel. CRM inference adds only 0.28\\,ms, making the correction overhead negligible. Plan~A's $K{=}2$ pipeline is 1.82$\\times$ faster than the $K{=}10$ analysis baseline while achieving equal or higher success rate, because the 80\\% reduction in VLA forward passes far outweighs the CRM overhead ($-$1.66\\% net latency vs.\\ $K{=}10$).\n\n\n\\section{Cross-VLA Generalization}\n\\label{sec:cross_vla}\n\nTo test whether the pipeline generalizes beyond SmolVLA, we evaluate on $\\pi_{0.5}$~\\cite{black2024pi0}, a 3.6B-parameter flow-matching VLA built on PaliGemma2 (vision) and Gemma2 (language) with 50-step action chunking. We use the same LIBERO-Object and LIBERO-Spatial benchmarks with identical evaluation protocol (10 rollouts per task, 3 seeds). The CRM architecture is unchanged; only the input projection differs, mapping $\\pi_{0.5}$'s 2048-dimensional observation features to the CRM input via a learned linear layer (vs.\\ SmolVLA's 960D direct concatenation).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-VLA generalization: $\\pi_{0.5}$ (3.6B) on LIBERO. The $\\pi_{0.5}$ baseline operates at $81$--$85$\\% SR, substantially above SmolVLA's $11$--$29$\\%, constraining the headroom for correction. $n{=}3$ seeds.}\n\\label{tab:cross_vla}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $K$ & Object (\\%) & Spatial (\\%) \\\\\n\\midrule\n$\\pi_{0.5}$ VLA-only & 1 & $81.5 \\pm 0.5$ & $84.2 \\pm 1.0$ \\\\\n$\\pi_{0.5}$ Plan~A & 2 & \\placeholder{} & \\placeholder{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_vla} reports results. The $\\pi_{0.5}$ baseline already achieves $81.5 \\pm 0.5$\\% on Object and $84.2 \\pm 1.0$\\% on Spatial---substantially above SmolVLA's $11.0$\\% / $29.4$\\%---leaving limited headroom for post-hoc correction. Plan~A results are pending (\\placeholder{}).\n",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 200
    }
  }
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01Pn6fg3GBU28nuNGQGEFXzb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "d3a3bfea-1269-4ae1-9189-55313bfbca53",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Npa58XwtGSNwbJ3F4szDrj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9385,
      "cache_read_input_tokens": 65435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9385
      },
      "output_tokens": 41,
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

_source line 53 · 2026-05-21T16:39:09.299Z_

<details><summary>↩ Tool result · `toolu_01Pn6fg3GBU28nuNGQGEFXzb`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\subsection{VLA Robustness}
4	
5	\looseness=-1 Vision-language-action models have progressed from tokenized action prediction~\cite{brohan2023rt2,kim2024openvla,ghosh2024octo} to generative approaches based on diffusion~\cite{chi2023diffusion_policy} and flow matching~\cite{black2024pi0,shukor2025smolvla}. Generative VLAs produce stochastic action samples that enable multi-sample inference; tokenized VLAs, by contrast, yield near-identical outputs across draws and cannot support sample-based refinement. Robustness evaluations~\cite{fei2025liberoplus} show that current VLAs lose over 65 percentage points under common deployment perturbations, motivating both training-time and inference-time defenses.
6	
7	\paragraph{Training-time methods.}
8	\looseness=-1 Recent approaches improve robustness through modified training. SRPO~\cite{srpo2025} and RobustVLA~\cite{robustvla2025} apply reinforcement learning post-training: the former uses the policy's own rollouts as reward references, while the latter adds Jacobian and smoothness regularization for stability under observation noise. DiG-Flow~\cite{digflow2025} operates at the representation level, gating control signals via distributional discrepancy between observation and action embeddings. TT-VLA~\cite{liu2026ttvla} adapts parameters at test time through progress-reward RL but requires per-task reward design. All four methods require retraining, reward engineering, or environment interaction and cannot serve as drop-in improvements to a frozen VLA.
9	
10	\paragraph{Inference-time methods.}
11	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds but does not learn corrective residuals. SC-VLA~\cite{liu2026scvla} performs online refinement through sparse world imagination combined with residual RL, but still requires task-level RL training. VLA-Pilot~\cite{li2025vlapilot} uses evolutionary diffusion optimization guided by an MLLM verifier at 2.41\,s per control step.
12	
13	\looseness=-1 A2C2~\cite{a2c2_2025} is the closest concurrent work. It learns a lightweight correction head that adjusts each action within a pre-generated chunk at every control step, addressing \emph{temporal staleness}: as new observations arrive mid-chunk, A2C2 corrects actions planned under stale context. Our pipeline targets a complementary problem, \emph{initial action quality}, by improving the action before execution. The two approaches could in principle be composed. Our pipeline differs in three ways: (1)~multi-sample selection precedes correction and centers the initial candidate; (2)~explicit $L_2$ norm clipping controls correction magnitude (Section~\ref{sec:magnitude_results}); and (3)~the correction module conditions on the frozen VLA's observation embedding rather than temporal action features.
14	
15	\subsection{Residual Policy Learning}
16	
17	\looseness=-1 Residual policy learning augments a base controller with a learned additive correction~\cite{silver2018residual,johannink2019residual}. The central challenge is magnitude control: unconstrained residuals can dominate the base policy and effectively learn from scratch. TRANSIC~\cite{jiang2024transic} mitigates this with a learned binary gate that disables correction when the base policy suffices; without the gate, performance collapses. PLD~\cite{xiao2026pld} bounds corrections within $[-\xi, \xi]$ via off-policy RL, and DRC~\cite{pan2025drc} applies exponential decay to correction magnitude over training. All three rely on RL and environment interaction. Our correction module uses fixed $L_2$ norm clipping with supervised $L_2$ loss on demonstration data. It requires no RL, no reward design, and no online rollouts.
18	
19	\subsection{Inference-Time Compute Scaling}
20	
21	Test-time compute scaling in language models improves output quality by generating multiple candidates and selecting among them~\cite{snell2024scaling}. RoVer~\cite{dai2025rover} transfers this principle to VLAs with a reward model that scores candidates in a best-of-N scheme. DA-SIP~\cite{chun2025dasip} adapts the number of denoising steps based on per-step difficulty rather than using a fixed budget.
22	
23	\looseness=-1 In the language domain, selection among candidates is the primary mechanism for quality improvement. Our decomposition reveals a different pattern in low-dimensional continuous action spaces: learned correction accounts for 78\% of the gain at $K{=}10$ and 55\% at $K{=}5$ (Section~\ref{sec:main_results}), while multi-sample selection provides centering but not the dominant contribution. This asymmetry motivates per-step adaptive allocation: a cheap $K{=}2$ uncertainty probe ($\rho{=}0.9979$ vs.\ $K{=}10$ variance) determines whether to extend sampling and apply correction, achieving 91\% of fixed-$K{=}10$ performance at 38\% of the compute (Section~\ref{sec:adaptive_k}). Unlike DA-SIP, which adapts denoising steps within a diffusion policy, our probe operates in action space and triggers a qualitatively different computation path (selection + learned correction) rather than adjusting iteration count.
24	Conformal prediction~\cite{angelopoulos2023gentle} has been applied to robotics for safety constraints~\cite{zhou2025acp_cbf,wang2025cploop} and teleoperation calibration~\cite{zhao2024conformalized}; we test CP scores as correction features and find they do not improve over observation-only conditioning (Section~\ref{sec:magnitude_results}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "9a189367-cc24-4d16-b653-d3e9b93f0270",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\n\\looseness=-1 Vision-language-action models have progressed from tokenized action prediction~\\cite{brohan2023rt2,kim2024openvla,ghosh2024octo} to generative approaches based on diffusion~\\cite{chi2023diffusion_policy} and flow matching~\\cite{black2024pi0,shukor2025smolvla}. Generative VLAs produce stochastic action samples that enable multi-sample inference; tokenized VLAs, by contrast, yield near-identical outputs across draws and cannot support sample-based refinement. Robustness evaluations~\\cite{fei2025liberoplus} show that current VLAs lose over 65 percentage points under common deployment perturbations, motivating both training-time and inference-time defenses.\n\n\\paragraph{Training-time methods.}\n\\looseness=-1 Recent approaches improve robustness through modified training. SRPO~\\cite{srpo2025} and RobustVLA~\\cite{robustvla2025} apply reinforcement learning post-training: the former uses the policy's own rollouts as reward references, while the latter adds Jacobian and smoothness regularization for stability under observation noise. DiG-Flow~\\cite{digflow2025} operates at the representation level, gating control signals via distributional discrepancy between observation and action embeddings. TT-VLA~\\cite{liu2026ttvla} adapts parameters at test time through progress-reward RL but requires per-task reward design. All four methods require retraining, reward engineering, or environment interaction and cannot serve as drop-in improvements to a frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds but does not learn corrective residuals. SC-VLA~\\cite{liu2026scvla} performs online refinement through sparse world imagination combined with residual RL, but still requires task-level RL training. VLA-Pilot~\\cite{li2025vlapilot} uses evolutionary diffusion optimization guided by an MLLM verifier at 2.41\\,s per control step.\n\n\\looseness=-1 A2C2~\\cite{a2c2_2025} is the closest concurrent work. It learns a lightweight correction head that adjusts each action within a pre-generated chunk at every control step, addressing \\emph{temporal staleness}: as new observations arrive mid-chunk, A2C2 corrects actions planned under stale context. Our pipeline targets a complementary problem, \\emph{initial action quality}, by improving the action before execution. The two approaches could in principle be composed. Our pipeline differs in three ways: (1)~multi-sample selection precedes correction and centers the initial candidate; (2)~explicit $L_2$ norm clipping controls correction magnitude (Section~\\ref{sec:magnitude_results}); and (3)~the correction module conditions on the frozen VLA's observation embedding rather than temporal action features.\n\n\\subsection{Residual Policy Learning}\n\n\\looseness=-1 Residual policy learning augments a base controller with a learned additive correction~\\cite{silver2018residual,johannink2019residual}. The central challenge is magnitude control: unconstrained residuals can dominate the base policy and effectively learn from scratch. TRANSIC~\\cite{jiang2024transic} mitigates this with a learned binary gate that disables correction when the base policy suffices; without the gate, performance collapses. PLD~\\cite{xiao2026pld} bounds corrections within $[-\\xi, \\xi]$ via off-policy RL, and DRC~\\cite{pan2025drc} applies exponential decay to correction magnitude over training. All three rely on RL and environment interaction. Our correction module uses fixed $L_2$ norm clipping with supervised $L_2$ loss on demonstration data. It requires no RL, no reward design, and no online rollouts.\n\n\\subsection{Inference-Time Compute Scaling}\n\nTest-time compute scaling in language models improves output quality by generating multiple candidates and selecting among them~\\cite{snell2024scaling}. RoVer~\\cite{dai2025rover} transfers this principle to VLAs with a reward model that scores candidates in a best-of-N scheme. DA-SIP~\\cite{chun2025dasip} adapts the number of denoising steps based on per-step difficulty rather than using a fixed budget.\n\n\\looseness=-1 In the language domain, selection among candidates is the primary mechanism for quality improvement. Our decomposition reveals a different pattern in low-dimensional continuous action spaces: learned correction accounts for 78\\% of the gain at $K{=}10$ and 55\\% at $K{=}5$ (Section~\\ref{sec:main_results}), while multi-sample selection provides centering but not the dominant contribution. This asymmetry motivates per-step adaptive allocation: a cheap $K{=}2$ uncertainty probe ($\\rho{=}0.9979$ vs.\\ $K{=}10$ variance) determines whether to extend sampling and apply correction, achieving 91\\% of fixed-$K{=}10$ performance at 38\\% of the compute (Section~\\ref{sec:adaptive_k}). Unlike DA-SIP, which adapts denoising steps within a diffusion policy, our probe operates in action space and triggers a qualitatively different computation path (selection + learned correction) rather than adjusting iteration count.\nConformal prediction~\\cite{angelopoulos2023gentle} has been applied to robotics for safety constraints~\\cite{zhou2025acp_cbf,wang2025cploop} and teleoperation calibration~\\cite{zhao2024conformalized}; we test CP scores as correction features and find they do not improve over observation-only conditioning (Section~\\ref{sec:magnitude_results}).",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---


### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "df369ed6-63c2-4f66-b086-c547e03b2357",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0171S4D7utRfxesnJVrfy6n2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9192,
      "cache_read_input_tokens": 74820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9192
      },
      "output_tokens": 39,
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

<details open><summary>🔧 Tool call — Read · `toolu_0174TvrQpzKwAVfh1Hh5GQ4h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "ff95a46b-83d9-43d5-a03c-f0c711d5da4c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0171S4D7utRfxesnJVrfy6n2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9192,
      "cache_read_input_tokens": 74820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9192
      },
      "output_tokens": 39,
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

_source line 56 · 2026-05-21T16:39:14.825Z_

<details><summary>↩ Tool result · `toolu_0174TvrQpzKwAVfh1Hh5GQ4h`</summary>

```text
1	@misc{a2c2_2025,
2	    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3	    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4	    year={2025},
5	    eprint={2509.23224},
6	    archivePrefix={arXiv},
7	    primaryClass={cs.RO}
8	}
9	
10	@article{angelopoulos2023gentle,
11	    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
12	    author={Anastasios N. Angelopoulos and Stephen Bates},
13	    journal={Foundations and Trends in Machine Learning},
14	    year={2023},
15	    eprint={2107.07511},
16	    archivePrefix={arXiv},
17	    primaryClass={cs.LG}
18	}
19	
20	
21	@misc{black2024pi0,
22	    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
23	    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
24	    year={2024},
25	    eprint={2410.24164},
26	    archivePrefix={arXiv},
27	    primaryClass={cs.RO}
28	}
29	
30	@misc{brohan2023rt2,
31	    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
32	    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},
33	    year={2023},
34	    eprint={2307.15818},
35	    archivePrefix={arXiv},
36	    primaryClass={cs.RO}
37	}
38	
39	@misc{chen2026reconvla,
40	    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},
41	    author={Lingling Chen and Zongyao Lyu and William J. Beksi},
42	    year={2026},
43	    eprint={2604.16677},
44	    archivePrefix={arXiv},
45	    primaryClass={cs.RO}
46	}
47	
48	
49	@misc{digflow2025,
50	    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},
51	    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},
52	    year={2025},
53	    eprint={2512.01715},
54	    archivePrefix={arXiv},
55	    primaryClass={cs.RO}
56	}
57	
58	@misc{fei2025liberoplus,
59	    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},
60	    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},
61	    year={2025},
62	    eprint={2510.13626},
63	    archivePrefix={arXiv},
64	    primaryClass={cs.RO}
65	}
66	
67	
68	@misc{ghosh2024octo,
69	    title={Octo: An Open-Source Generalist Robot Policy},
70	    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},
71	    year={2024},
72	    eprint={2405.12213},
73	    archivePrefix={arXiv},
74	    primaryClass={cs.RO}
75	}
76	
77	
78	
79	@misc{kim2024openvla,
80	    title={OpenVLA: An Open-Source Vision-Language-Action Model},
81	    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},
82	    year={2024},
83	    eprint={2406.09246},
84	    archivePrefix={arXiv},
85	    primaryClass={cs.RO}
86	}
87	
88	
89	@article{ledoit2004well,
90	    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},
91	    author={Olivier Ledoit and Michael Wolf},
92	    journal={Journal of Multivariate Analysis},
93	    volume={88},
94	    number={2},
95	    pages={365--411},
96	    year={2004}
97	}
98	
99	@inproceedings{lipman2023flow,
100	    title={Flow Matching for Generative Modeling},
101	    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},
102	    booktitle={International Conference on Learning Representations (ICLR)},
103	    year={2023}
104	}
105	
106	@inproceedings{liu2023libero,
107	    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
108	    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},
109	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
110	    year={2023}
111	}
112	
113	@misc{liu2026ttvla,
114	    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},
115	    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},
116	    year={2026},
117	    eprint={2601.06748},
118	    archivePrefix={arXiv},
119	    primaryClass={cs.RO}
120	}
121	
122	
123	@misc{robustvla2025,
124	    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},
125	    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},
126	    year={2025},
127	    eprint={2511.01331},
128	    archivePrefix={arXiv},
129	    primaryClass={cs.RO}
130	}
131	
132	
133	
134	@misc{shukor2025smolvla,
135	    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},
136	    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},
137	    year={2025},
138	    eprint={2506.01844},
139	    archivePrefix={arXiv},
140	    primaryClass={cs.RO}
141	}
142	
143	@misc{srpo2025,
144	    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},
145	    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},
146	    year={2025},
147	    eprint={2511.15605},
148	    archivePrefix={arXiv},
149	    primaryClass={cs.RO}
150	}
151	
152	
153	@misc{wang2025cploop,
154	    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},
155	    author={Han Wang and Chao Ning},
156	    year={2025},
157	    eprint={2510.16376},
158	    archivePrefix={arXiv},
159	    primaryClass={cs.RO}
160	}
161	
162	
163	
164	@inproceedings{chi2023diffusion_policy,
165	    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
166	    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},
167	    booktitle={Robotics: Science and Systems (RSS)},
168	    year={2023},
169	    note={Also published in IJRR 2024. arXiv:2303.04137}
170	}
171	
172	@inproceedings{zhao2024conformalized,
173	    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},
174	    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},
175	    booktitle={Robotics: Science and Systems (RSS)},
176	    year={2024}
177	}
178	
179	@inproceedings{silver2018residual,
180	    title={Residual Policy Learning},
181	    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},
182	    booktitle={Robotics: Science and Systems (RSS)},
183	    year={2018},
184	    note={arXiv:1812.06298}
185	}
186	
187	@inproceedings{jiang2024transic,
188	    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},
189	    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},
190	    booktitle={Conference on Robot Learning (CoRL)},
191	    year={2024},
192	    note={arXiv:2405.10315}
193	}
194	
195	@inproceedings{johannink2019residual,
196	    title={Residual Reinforcement Learning for Robot Control},
197	    author={Tobias Johannink and Shikhar Bahl and Ashvin Nair and Jianlan Luo and Avinash Kumar and Matthias Loskyll and Juan Aparicio Ojea and Eugen Solowjow and Sergey Levine},
198	    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
199	    year={2019},
200	    pages={6023--6029}
201	}
202	
203	@inproceedings{xiao2026pld,
204	    title={Self-Improving Vision-Language-Action Models with Data Generation via Residual RL},
205	    author={Wenli Xiao and Haotian Lin and Andy Peng and Haoru Xue and Tairan He and Yuqi Xie and Fengyuan Hu and Jimmy Wu and Zhengyi Luo and Linxi Fan and Guanya Shi and Yuke Zhu},
206	    booktitle={International Conference on Learning Representations (ICLR)},
207	    year={2026},
208	    note={arXiv:2511.00091}
209	}
210	
211	@misc{pan2025drc,
212	    title={Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation},
213	    author={Cheng Pan and Hung Hon Cheng and Josie Hughes},
214	    year={2025},
215	    eprint={2503.15368},
216	    archivePrefix={arXiv},
217	    primaryClass={cs.RO}
218	}
219	
220	@inproceedings{zhou2025acp_cbf,
221	    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},
222	    author={Hao Zhou and Yanze Zhang and Wenhao Luo},
223	    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
224	    year={2025},
225	    note={arXiv:2503.17678}
226	}
227	
228	
229	@inproceedings{ross2011dagger,
230	    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},
231	    author={St{\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},
232	    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},
233	    year={2011}
234	}
235	
236	
237	@misc{liu2026scvla,
238	    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},
239	    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},
240	    year={2026},
241	    eprint={2602.21633},
242	    archivePrefix={arXiv},
243	    primaryClass={cs.RO}
244	}
245	
246	@misc{li2025vlapilot,
247	    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},
248	    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},
249	    year={2025},
250	    eprint={2511.14178},
251	    archivePrefix={arXiv},
252	    primaryClass={cs.RO}
253	}
254	
255	
256	@inproceedings{snell2024scaling,
257	    title={Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning},
258	    author={Charlie Snell and Jaehoon Lee and Kelvin Xu and Aviral Kumar},
259	    year={2025},
260	    eprint={2408.03314},
261	    archivePrefix={arXiv},
262	    primaryClass={cs.LG},
263	    booktitle={International Conference on Learning Representations (ICLR)}
264	}
265	
266	@misc{dai2025rover,
267	    title={RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model},
268	    author={Yufeng Dai and Haolun Liu and Zhihao Bai and Yuxin Liu and Jiaming Wang and Hongyuan Su and Chenyv Chen and Jiaying Lin and Liangjun Wu},
269	    year={2025},
270	    eprint={2510.10975},
271	    archivePrefix={arXiv},
272	    primaryClass={cs.RO}
273	}
274	
275	@inproceedings{chun2025dasip,
276	    title={Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy},
277	    author={Seonghyeon Chun and Jaehyun Lee and Michael S. Albergo and Lisa Xie and Eric Vanden-Eijnden},
278	    year={2025},
279	    eprint={2511.20906},
280	    archivePrefix={arXiv},
281	    primaryClass={cs.LG},
282	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)}
283	}
284	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "5a70fc2c-1ed1-4387-a9ea-0a6e94395fa4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
      "content": "@misc{a2c2_2025,\n    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},\n    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},\n    year={2025},\n    eprint={2509.23224},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@article{angelopoulos2023gentle,\n    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},\n    author={Anastasios N. Angelopoulos and Stephen Bates},\n    journal={Foundations and Trends in Machine Learning},\n    year={2023},\n    eprint={2107.07511},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n\n@misc{black2024pi0,\n    title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},\n    year={2024},\n    eprint={2410.24164},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{brohan2023rt2,\n    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},\n    year={2023},\n    eprint={2307.15818},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{chen2026reconvla,\n    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},\n    author={Lingling Chen and Zongyao Lyu and William J. Beksi},\n    year={2026},\n    eprint={2604.16677},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n\n@misc{digflow2025,\n    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},\n    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},\n    year={2025},\n    eprint={2512.01715},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{fei2025liberoplus,\n    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},\n    year={2025},\n    eprint={2510.13626},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n\n@misc{ghosh2024octo,\n    title={Octo: An Open-Source Generalist Robot Policy},\n    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},\n    year={2024},\n    eprint={2405.12213},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n\n\n@misc{kim2024openvla,\n    title={OpenVLA: An Open-Source Vision-Language-Action Model},\n    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},\n    year={2024},\n    eprint={2406.09246},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n\n@article{ledoit2004well,\n    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},\n    author={Olivier Ledoit and Michael Wolf},\n    journal={Journal of Multivariate Analysis},\n    volume={88},\n    number={2},\n    pages={365--411},\n    year={2004}\n}\n\n@inproceedings{lipman2023flow,\n    title={Flow Matching for Generative Modeling},\n    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2023}\n}\n\n@inproceedings{liu2023libero,\n    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2023}\n}\n\n@misc{liu2026ttvla,\n    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},\n    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},\n    year={2026},\n    eprint={2601.06748},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n\n@misc{robustvla2025,\n    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},\n    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},\n    year={2025},\n    eprint={2511.01331},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n\n\n@misc{shukor2025smolvla,\n    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},\n    year={2025},\n    eprint={2506.01844},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{srpo2025,\n    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},\n    year={2025},\n    eprint={2511.15605},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n\n@misc{wang2025cploop,\n    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},\n    author={Han Wang and Chao Ning},\n    year={2025},\n    eprint={2510.16376},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n\n\n@inproceedings{chi2023diffusion_policy,\n    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2023},\n    note={Also published in IJRR 2024. arXiv:2303.04137}\n}\n\n@inproceedings{zhao2024conformalized,\n    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},\n    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2024}\n}\n\n@inproceedings{silver2018residual,\n    title={Residual Policy Learning},\n    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2018},\n    note={arXiv:1812.06298}\n}\n\n@inproceedings{jiang2024transic,\n    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},\n    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},\n    booktitle={Conference on Robot Learning (CoRL)},\n    year={2024},\n    note={arXiv:2405.10315}\n}\n\n@inproceedings{johannink2019residual,\n    title={Residual Reinforcement Learning for Robot Control},\n    author={Tobias Johannink and Shikhar Bahl and Ashvin Nair and Jianlan Luo and Avinash Kumar and Matthias Loskyll and Juan Aparicio Ojea and Eugen Solowjow and Sergey Levine},\n    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n    year={2019},\n    pages={6023--6029}\n}\n\n@inproceedings{xiao2026pld,\n    title={Self-Improving Vision-Language-Action Models with Data Generation via Residual RL},\n    author={Wenli Xiao and Haotian Lin and Andy Peng and Haoru Xue and Tairan He and Yuqi Xie and Fengyuan Hu and Jimmy Wu and Zhengyi Luo and Linxi Fan and Guanya Shi and Yuke Zhu},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2026},\n    note={arXiv:2511.00091}\n}\n\n@misc{pan2025drc,\n    title={Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation},\n    author={Cheng Pan and Hung Hon Cheng and Josie Hughes},\n    year={2025},\n    eprint={2503.15368},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhou2025acp_cbf,\n    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},\n    author={Hao Zhou and Yanze Zhang and Wenhao Luo},\n    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n    year={2025},\n    note={arXiv:2503.17678}\n}\n\n\n@inproceedings{ross2011dagger,\n    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},\n    author={St{\\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},\n    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},\n    year={2011}\n}\n\n\n@misc{liu2026scvla,\n    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},\n    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},\n    year={2026},\n    eprint={2602.21633},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{li2025vlapilot,\n    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},\n    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},\n    year={2025},\n    eprint={2511.14178},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n\n@inproceedings{snell2024scaling,\n    title={Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning},\n    author={Charlie Snell and Jaehoon Lee and Kelvin Xu and Aviral Kumar},\n    year={2025},\n    eprint={2408.03314},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG},\n    booktitle={International Conference on Learning Representations (ICLR)}\n}\n\n@misc{dai2025rover,\n    title={RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model},\n    author={Yufeng Dai and Haolun Liu and Zhihao Bai and Yuxin Liu and Jiaming Wang and Hongyuan Su and Chenyv Chen and Jiaying Lin and Liangjun Wu},\n    year={2025},\n    eprint={2510.10975},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{chun2025dasip,\n    title={Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy},\n    author={Seonghyeon Chun and Jaehyun Lee and Michael S. Albergo and Lisa Xie and Eric Vanden-Eijnden},\n    year={2025},\n    eprint={2511.20906},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)}\n}\n",
      "numLines": 284,
      "startLine": 1,
      "totalLines": 284
    }
  }
}
```

</details>

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_017pZJ9TZCxhvMGkSd7pYVoz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "9992718c-83e0-463c-be20-303893e2426b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0171S4D7utRfxesnJVrfy6n2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9192,
      "cache_read_input_tokens": 74820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9192
      },
      "output_tokens": 39,
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

_source line 58 · 2026-05-21T16:39:15.675Z_

<details><summary>↩ Tool result · `toolu_017pZJ9TZCxhvMGkSd7pYVoz`</summary>

```text
1	This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex 2026.5.2)  21 MAY 2026 15:44
2	entering extended mode
3	 restricted \write18 enabled.
4	 %&-line parsing enabled.
5	**main.tex
6	(./main.tex
7	LaTeX2e <2025-11-01>
8	L3 programming layer <2026-01-19>
9	(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
10	Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
11	(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo
12	File: size10.clo 2025/01/22 v1.4n Standard LaTeX file (size option)
13	)
14	\c@part=\count275
15	\c@section=\count276
16	\c@subsection=\count277
17	\c@subsubsection=\count278
18	\c@paragraph=\count279
19	\c@subparagraph=\count280
20	\c@figure=\count281
21	\c@table=\count282
22	\abovecaptionskip=\skip49
23	\belowcaptionskip=\skip50
24	\bibindent=\dimen148
25	) (./corl_2026.sty
26	Package: corl_2026 2026/08/15 CORL2026 submission/preprint/camera-ready style f
27	ile
28	
29	(/usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty
30	Package: lineno 2025/05/13 line numbers on paragraphs v5.5
31	
32	(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty
33	Package: etoolbox 2025/10/02 v2.5m e-TeX tools for LaTeX (JAW)
34	\etb@tempcnta=\count283
35	)
36	(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty
37	Package: kvoptions 2022-06-15 v3.15 Key value format for package options (HO)
38	
39	(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty
40	Package: keyval 2022/05/29 v1.15 key=value parser (DPC)
41	\KV@toks@=\toks17
42	)
43	(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty
44	Package: ltxcmds 2023-12-04 v1.26 LaTeX kernel commands for general use (HO)
45	)
46	(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty
47	Package: kvsetkeys 2022-10-05 v1.19 Key value parser (HO)
48	))
49	\linenopenalty=\count284
50	\output=\toks18
51	\linenoprevgraf=\count285
52	\linenumbersep=\dimen149
53	\linenumberwidth=\dimen150
54	\c@linenumber=\count286
55	\c@pagewiselinenumber=\count287
56	\c@LN@truepage=\count288
57	\c@internallinenumber=\count289
58	\c@internallinenumbers=\count290
59	\quotelinenumbersep=\dimen151
60	\bframerule=\dimen152
61	\bframesep=\dimen153
62	\bframebox=\box53
63	)
64	(/usr/share/texlive/texmf-dist/tex/latex/graphics/color.sty
65	Package: color 2025/01/14 v1.3e Standard LaTeX Color (DPC)
66	
67	(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg
68	File: color.cfg 2016/01/02 v1.6 sample color configuration
69	)
70	Package color Info: Driver file: pdftex.def on input line 149.
71	
72	(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def
73	File: pdftex.def 2025/09/29 v1.2d Graphics/color driver for pdftex
74	)
75	(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
76	(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty
77	Package: natbib 2010/09/13 8.31b (PWD, AO)
78	\bibhang=\skip51
79	\bibsep=\skip52
80	LaTeX Info: Redefining \cite on input line 694.
81	\c@NAT@ctr=\count291
82	)
83	(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
84	Package: hyperref 2025-07-12 v7.01o Hypertext links for LaTeX
85	
86	(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty
87	Package: iftex 2024/12/12 v1.0g TeX engine tests
88	)
89	(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty
90	Package: kvdefinekeys 2019-12-19 v1.6 Define keys (HO)
91	)
92	(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
93	Package: pdfescape 2019/12/09 v1.15 Implements pdfTeX's escape features (HO)
94	
95	(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
96	Package: pdftexcmds 2020-06-27 v0.33 Utility functions of pdfTeX for LuaTeX (HO
97	)
98	
99	(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty
100	Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
101	)
102	Package pdftexcmds Info: \pdf@primitive is available.
103	Package pdftexcmds Info: \pdf@ifprimitive is available.
104	Package pdftexcmds Info: \pdfdraftmode found.
105	))
106	(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty
107	Package: hycolor 2020-01-27 v1.10 Color options for hyperref/bookmark (HO)
108	)
109	(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
110	Package: nameref 2025-06-21 v2.57 Cross-referencing by name of section
111	
112	(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty
113	Package: refcount 2019/12/15 v3.6 Data extraction from label references (HO)
114	)
115	(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
116	Package: gettitlestring 2019/12/15 v1.6 Cleanup title references (HO)
117	)
118	\c@section@level=\count292
119	)
120	(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty
121	Package: stringenc 2019/11/29 v1.12 Convert strings between diff. encodings (HO
122	)
123	)
124	\@linkdim=\dimen154
125	\Hy@linkcounter=\count293
126	\Hy@pagecounter=\count294
127	
128	(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def
129	File: pd1enc.def 2025-07-12 v7.01o Hyperref: PDFDocEncoding definition (HO)
130	Now handling font encoding PD1 ...
131	... no UTF-8 mapping file for font encoding PD1
132	)
133	(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty
134	Package: intcalc 2019/12/15 v1.3 Expandable calculations with integers (HO)
135	)
136	\Hy@SavedSpaceFactor=\count295
137	
138	(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def
139	File: puenc.def 2025-07-12 v7.01o Hyperref: PDF Unicode definition (HO)
140	Now handling font encoding PU ...
141	... no UTF-8 mapping file for font encoding PU
142	)
143	Package hyperref Info: Hyper figures OFF on input line 4195.
144	Package hyperref Info: Link nesting OFF on input line 4200.
145	Package hyperref Info: Hyper index ON on input line 4203.
146	Package hyperref Info: Plain pages OFF on input line 4210.
147	Package hyperref Info: Backreferencing OFF on input line 4215.
148	Package hyperref Info: Implicit mode ON; LaTeX internals redefined.
149	Package hyperref Info: Bookmarks ON on input line 4462.
150	\c@Hy@tempcnt=\count296
151	
152	(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty
153	\Urlmuskip=\muskip17
154	Package: url 2013/09/16  ver 3.4  Verb mode for urls, etc.
155	)
156	LaTeX Info: Redefining \url on input line 4801.
157	\XeTeXLinkMargin=\dimen155
158	
159	(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
160	Package: bitset 2019/12/09 v1.3 Handle bit-vector datatype (HO)
161	
162	(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty
163	Package: bigintcalc 2019/12/15 v1.5 Expandable calculations on big integers (HO
164	)
165	))
166	\Fld@menulength=\count297
167	\Field@Width=\dimen156
168	\Fld@charsize=\dimen157
169	Package hyperref Info: Hyper figures OFF on input line 6078.
170	Package hyperref Info: Link nesting OFF on input line 6083.
171	Package hyperref Info: Hyper index ON on input line 6086.
172	Package hyperref Info: backreferencing OFF on input line 6093.
173	Package hyperref Info: Link coloring OFF on input line 6098.
174	Package hyperref Info: Link coloring with OCG OFF on input line 6103.
175	Package hyperref Info: PDF/A mode OFF on input line 6108.
176	\Hy@abspage=\count298
177	\c@Item=\count299
178	\c@Hfootnote=\count300
179	)
180	Package hyperref Info: Driver (autodetected): hpdftex.
181	
182	(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
183	File: hpdftex.def 2025-07-12 v7.01o Hyperref driver for pdfTeX
184	\Fld@listcount=\count301
185	\c@bookmark@seq@number=\count302
186	
187	(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
188	Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)
189	
190	(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty
191	Package: uniquecounter 2019/12/15 v1.4 Provide unlimited unique counter (HO)
192	)
193	Package uniquecounter Info: New unique counter `rerunfilecheck' on input line 2
194	84.
195	)
196	\Hy@SectionHShift=\skip53
197	)
198	(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
199	Package: geometry 2020/01/02 v5.9 Page Geometry
200	
201	(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
202	Package: ifvtex 2019/10/25 v1.7 ifvtex legacy package. Use iftex instead.
203	)
204	\Gm@cnth=\count303
205	\Gm@cntv=\count304
206	\c@Gm@tempcnt=\count305
207	\Gm@bindingoffset=\dimen158
208	\Gm@wd@mp=\dimen159
209	\Gm@odd@mp=\dimen160
210	\Gm@even@mp=\dimen161
211	\Gm@layoutwidth=\dimen162
212	\Gm@layoutheight=\dimen163
213	\Gm@layouthoffset=\dimen164
214	\Gm@layoutvoffset=\dimen165
215	\Gm@dimlist=\toks19
216	)
217	Package hyperref Info: Option `colorlinks' set `true' on input line 114.
218	\@nipsabovecaptionskip=\skip54
219	\@nipsbelowcaptionskip=\skip55
220	)
221	(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty
222	Package: inputenc 2024/02/08 v1.3d Input encoding file
223	\inpenc@prehook=\toks20
224	\inpenc@posthook=\toks21
225	)
226	(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty
227	Package: fontenc 2025/07/18 v2.1d Standard LaTeX package
228	LaTeX Font Info:    Trying to load font information for T1+ptm on input line 11
229	6.
230	
231	(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd
232	File: t1ptm.fd 2001/06/04 font definitions for T1/ptm.
233	))
234	(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
235	Package: amsmath 2025/07/09 v2.17z AMS math features
236	\@mathmargin=\skip56
237	
238	For additional information on amsmath, use the `?' option.
239	(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
240	Package: amstext 2024/11/17 v2.01 AMS text
241	
242	(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty
243	File: amsgen.sty 1999/11/30 v2.0 generic functions
244	\@emptytoks=\toks22
245	\ex@=\dimen166
246	))
247	(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty
248	Package: amsbsy 1999/11/29 v1.2d Bold Symbols
249	\pmbraise@=\dimen167
250	)
251	(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty
252	Package: amsopn 2022/04/08 v2.04 operator names
253	)
254	\inf@bad=\count306
255	LaTeX Info: Redefining \frac on input line 233.
256	\uproot@=\count307
257	\leftroot@=\count308
258	LaTeX Info: Redefining \overline on input line 398.
259	LaTeX Info: Redefining \colon on input line 409.
260	\classnum@=\count309
261	\DOTSCASE@=\count310
262	LaTeX Info: Redefining \ldots on input line 495.
263	LaTeX Info: Redefining \dots on input line 498.
264	LaTeX Info: Redefining \cdots on input line 619.
265	\Mathstrutbox@=\box54
266	\strutbox@=\box55
267	LaTeX Info: Redefining \big on input line 721.
268	LaTeX Info: Redefining \Big on input line 722.
269	LaTeX Info: Redefining \bigg on input line 723.
270	LaTeX Info: Redefining \Bigg on input line 724.
271	\big@size=\dimen168
272	LaTeX Font Info:    Redeclaring font encoding OML on input line 742.
273	LaTeX Font Info:    Redeclaring font encoding OMS on input line 743.
274	\macc@depth=\count311
275	LaTeX Info: Redefining \bmod on input line 904.
276	LaTeX Info: Redefining \pmod on input line 909.
277	LaTeX Info: Redefining \smash on input line 939.
278	LaTeX Info: Redefining \relbar on input line 969.
279	LaTeX Info: Redefining \Relbar on input line 970.
280	\c@MaxMatrixCols=\count312
281	\dotsspace@=\muskip18
282	\c@parentequation=\count313
283	\dspbrk@lvl=\count314
284	\tag@help=\toks23
285	\row@=\count315
286	\column@=\count316
287	\maxfields@=\count317
288	\andhelp@=\toks24
289	\eqnshift@=\dimen169
290	\alignsep@=\dimen170
291	\tagshift@=\dimen171
292	\tagwidth@=\dimen172
293	\totwidth@=\dimen173
294	\lineht@=\dimen174
295	\@envbody=\toks25
296	\multlinegap=\skip57
297	\multlinetaggap=\skip58
298	\mathdisplay@stack=\toks26
299	LaTeX Info: Redefining \[ on input line 2950.
300	LaTeX Info: Redefining \] on input line 2951.
301	)
302	\@LN@amsmath@ams@eqpen=\count318
303	
304	(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
305	Package: amssymb 2013/01/14 v3.01 AMS font symbols
306	
307	(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty
308	Package: amsfonts 2013/01/14 v3.01 Basic AMSFonts support
309	\symAMSa=\mathgroup4
310	\symAMSb=\mathgroup5
311	LaTeX Font Info:    Redeclaring math symbol \hbar on input line 98.
312	LaTeX Font Info:    Overwriting math alphabet `\mathfrak' in version `bold'
313	(Font)                  U/euf/m/n --> U/euf/b/n on input line 106.
314	))
315	(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
316	Package: graphicx 2024/12/31 v1.2e Enhanced LaTeX Graphics (DPC,SPQR)
317	
318	(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
319	Package: graphics 2024/08/06 v1.4g Standard LaTeX Graphics (DPC,SPQR)
320	
321	(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty
322	Package: trig 2023/12/02 v1.11 sin cos tan (DPC)
323	)
324	(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg
325	File: graphics.cfg 2016/06/04 v1.11 sample graphics configuration
326	)
327	Package graphics Info: Driver file: pdftex.def on input line 106.
328	)
329	\Gin@req@height=\dimen175
330	\Gin@req@width=\dimen176
331	)
332	(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty
333	Package: booktabs 2020/01/12 v1.61803398 Publication quality tables
334	\heavyrulewidth=\dimen177
335	\lightrulewidth=\dimen178
336	\cmidrulewidth=\dimen179
337	\belowrulesep=\dimen180
338	\belowbottomsep=\dimen181
339	\aboverulesep=\dimen182
340	\abovetopsep=\dimen183
341	\cmidrulesep=\dimen184
342	\cmidrulekern=\dimen185
343	\defaultaddspace=\dimen186
344	\@cmidla=\count319
345	\@cmidlb=\count320
346	\@aboverulesep=\dimen187
347	\@belowrulesep=\dimen188
348	\@thisruleclass=\count321
349	\@lastruleclass=\count322
350	\@thisrulewidth=\dimen189
351	)
352	(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty
353	Package: enumitem 2025/02/06 v3.11 Customized lists
354	\labelindent=\skip59
355	\enit@outerparindent=\dimen190
356	\enit@toks=\toks27
357	\enit@inbox=\box56
358	\enit@count@id=\count323
359	\enitdp@description=\count324
360	)
361	(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty
362	Package: multirow 2024/11/12 v2.9 Span multiple rows of a table
363	\multirow@colwidth=\skip60
364	\multirow@cntb=\count325
365	\multirow@dima=\skip61
366	\bigstrutjot=\dimen191
367	)
368	(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def
369	File: l3backend-pdftex.def 2025-10-09 L3 backend support: PDF output (pdfTeX)
370	\l__color_backend_stack_int=\count326
371	)
372	(./main.aux)
373	\openout1 = `main.aux'.
374	
375	LaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 25.
376	LaTeX Font Info:    ... okay on input line 25.
377	LaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 25.
378	LaTeX Font Info:    ... okay on input line 25.
379	LaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 25.
380	LaTeX Font Info:    ... okay on input line 25.
381	LaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 25.
382	LaTeX Font Info:    ... okay on input line 25.
383	LaTeX Font Info:    Checking defaults for TS1/cmr/m/n on input line 25.
384	LaTeX Font Info:    ... okay on input line 25.
385	LaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 25.
386	LaTeX Font Info:    ... okay on input line 25.
387	LaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 25.
388	LaTeX Font Info:    ... okay on input line 25.
389	LaTeX Font Info:    Checking defaults for PD1/pdf/m/n on input line 25.
390	LaTeX Font Info:    ... okay on input line 25.
391	LaTeX Font Info:    Checking defaults for PU/pdf/m/n on input line 25.
392	LaTeX Font Info:    ... okay on input line 25.
393	 (/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
394	[Loading MPS to PDF converter (version 2006.09.02).]
395	\scratchcounter=\count327
396	\scratchdimen=\dimen192
397	\scratchbox=\box57
398	\nofMPsegments=\count328
399	\nofMParguments=\count329
400	\everyMPshowfont=\toks28
401	\MPscratchCnt=\count330
402	\MPscratchDim=\dimen193
403	\MPnumerator=\count331
404	\makeMPintoPDFobject=\count332
405	\everyMPtoPDFconversion=\toks29
406	) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
407	Package: epstopdf-base 2020-01-24 v2.11 Base part for package epstopdf
408	Package epstopdf-base Info: Redefining graphics rule for `.eps' on input line 4
409	85.
410	
411	(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg
412	File: epstopdf-sys.cfg 2010/07/13 v1.3 Configuration of (r)epstopdf for TeX Liv
413	e
414	))
415	*geometry* verbose mode - [ newgeometry ] result:
416	* driver: 
417	* paper: letterpaper
418	* layout: &lt;same size as paper>
419	* layoutoffset:(h,v)=(0.0pt,0.0pt)
420	* modes: 
421	* h-part:(L,W,R)=(108.405pt, 397.48499pt, 108.40501pt)
422	* v-part:(T,H,B)=(72.26999pt, 650.43pt, 72.27pt)
423	* \paperwidth=614.295pt
424	* \paperheight=794.96999pt
425	* \textwidth=397.48499pt
426	* \textheight=650.43pt
427	* \oddsidemargin=36.13501pt
428	* \evensidemargin=36.13501pt
429	* \topmargin=-37.0pt
430	* \headheight=12.0pt
431	* \headsep=25.0pt
432	* \topskip=10.0pt
433	* \footskip=30.0pt
434	* \marginparwidth=65.0pt
435	* \marginparsep=11.0pt
436	* \columnsep=10.0pt
437	* \skip\footins=9.0pt plus 4.0pt minus 2.0pt
438	* \hoffset=0.0pt
439	* \voffset=0.0pt
440	* \mag=1000
441	* \@twocolumnfalse
442	* \@twosidefalse
443	* \@mparswitchfalse
444	* \@reversemarginfalse
445	* (1in=72.27pt=25.4mm, 1cm=28.453pt)
446	
447	Package hyperref Info: Link coloring ON on input line 25.
448	(./main.out) (./main.out)
449	\@outlinefile=\write3
450	\openout3 = `main.out'.
451	
452	
453	*geometry* driver: auto-detecting
454	*geometry* detected driver: pdftex
455	*geometry* verbose mode - [ preamble ] result:
456	* driver: pdftex
457	* paper: letterpaper
458	* layout: &lt;same size as paper>
459	* layoutoffset:(h,v)=(0.0pt,0.0pt)
460	* modes: 
461	* h-part:(L,W,R)=(108.405pt, 397.48499pt, 108.40501pt)
462	* v-part:(T,H,B)=(72.26999pt, 650.43pt, 72.27pt)
463	* \paperwidth=614.295pt
464	* \paperheight=794.96999pt
465	* \textwidth=397.48499pt
466	* \textheight=650.43pt
467	* \oddsidemargin=36.13501pt
468	* \evensidemargin=36.13501pt
469	* \topmargin=-37.0pt
470	* \headheight=12.0pt
471	* \headsep=25.0pt
472	* \topskip=10.0pt
473	* \footskip=30.0pt
474	* \marginparwidth=65.0pt
475	* \marginparsep=11.0pt
476	* \columnsep=10.0pt
477	* \skip\footins=9.0pt plus 4.0pt minus 2.0pt
478	* \hoffset=0.0pt
479	* \voffset=0.0pt
480	* \mag=1000
481	* \@twocolumnfalse
482	* \@twosidefalse
483	* \@mparswitchfalse
484	* \@reversemarginfalse
485	* (1in=72.27pt=25.4mm, 1cm=28.453pt)
486	
487	LaTeX Font Info:    Trying to load font information for U+msa on input line 27.
488	
489	(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd
490	File: umsa.fd 2013/01/14 v3.01 AMS symbols A
491	)
492	LaTeX Font Info:    Trying to load font information for U+msb on input line 27.
493	
494	
495	(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd
496	File: umsb.fd 2013/01/14 v3.01 AMS symbols B
497	) (./abstract.tex)
498	LaTeX Font Info:    Trying to load font information for T1+phv on input line 31
499	.
500	
501	(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1phv.fd
502	File: t1phv.fd 2020/03/25 scalable font definitions for T1/phv.
503	)
504	Underfull \hbox (badness 3690) in paragraph at lines 33--33
505	[]\T1/ptm/b/n/10 Keywords: \T1/ptm/m/n/10 Vision-Language-Action Mod-els, Infer
506	ence-Time Re-fine-ment,
507	 []
508	
509	(./introduction.tex [1
510	
511	
512	{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-di
513	st/fonts/enc/dvips/base/8r.enc}]) (./related_work.tex
514	Underfull \hbox (badness 1194) in paragraph at lines 8--9
515	 []\T1/ptm/b/n/10 Training-time meth-ods.[] \T1/ptm/m/n/10 Re-cent ap-proaches 
516	im-prove ro-bust-ness through mod-i-fied train-ing.
517	 []
518	
519	[2]) (./method.tex
520	&lt;figures/fig1_pipeline.pdf, id=190, 537.00134pt x 209.31084pt>
521	File: figures/fig1_pipeline.pdf Graphic file (type pdf)
522	&lt;use figures/fig1_pipeline.pdf>
523	Package pdftex.def Info: figures/fig1_pipeline.pdf  used on input line 7.
524	(pdftex.def)             Requested size: 397.48499pt x 154.9291pt.
525	
526	Underfull \vbox (badness 10000) has occurred while \output is active []
527	
528	 [3]
529	Underfull \hbox (badness 1502) in paragraph at lines 37--38
530	 []\T1/ptm/b/n/10 Architecture.[] \T1/ptm/m/n/10 The CRM con-sists of three ful
531	ly con-nected lay-ers with ReLU ac-ti-va-tions:
532	 []
533	
534	[4 <./figures/fig1_pipeline.pdf>]
535	LaTeX Font Info:    Trying to load font information for TS1+ptm on input line 4
536	7.
537	
538	(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd
539	File: ts1ptm.fd 2001/06/04 font definitions for TS1/ptm.
540	) [5])
541	(./experiments.tex
542	&lt;figures/fig5_k2_correlation.pdf, id=361, 706.15883pt x 330.00478pt>
543	File: figures/fig5_k2_correlation.pdf Graphic file (type pdf)
544	&lt;use figures/fig5_k2_correlation.pdf>
545	Package pdftex.def Info: figures/fig5_k2_correlation.pdf  used on input line 31
546	.
547	(pdftex.def)             Requested size: 397.48499pt x 185.7531pt.
548	 [6] [7 <./figures/fig5_k2_correlation.pdf>])
549	(./discussion.tex) (./main.bbl [8] [9]) [10] (./appendix.tex
550	&lt;figures/fig3_decomposition.pdf, id=488, 414.79512pt x 235.77295pt>
551	File: figures/fig3_decomposition.pdf Graphic file (type pdf)
552	&lt;use figures/fig3_decomposition.pdf>
553	Package pdftex.def Info: figures/fig3_decomposition.pdf  used on input line 9.
554	(pdftex.def)             Requested size: 397.48499pt x 225.94011pt.
555	&lt;figures/fig2_magnitude.pdf, id=489, 492.92154pt x 174.60608pt>
556	File: figures/fig2_magnitude.pdf Graphic file (type pdf)
557	&lt;use figures/fig2_magnitude.pdf>
558	Package pdftex.def Info: figures/fig2_magnitude.pdf  used on input line 19.
559	(pdftex.def)             Requested size: 397.48499pt x 140.80136pt.
560	
561	
562	Package hyperref Warning: Token not allowed in a PDF string (Unicode):
563	(hyperref)                removing `math shift' on input line 24.
564	
565	
566	Package hyperref Warning: Token not allowed in a PDF string (Unicode):
567	(hyperref)                removing `math shift' on input line 24.
568	
569	&lt;figures/fig3_kvalue.pdf, id=491, 380.93694pt x 281.18738pt>
570	File: figures/fig3_kvalue.pdf Graphic file (type pdf)
571	&lt;use figures/fig3_kvalue.pdf>
572	Package pdftex.def Info: figures/fig3_kvalue.pdf  used on input line 31.
573	(pdftex.def)             Requested size: 397.48499pt x 293.42339pt.
574	
575	LaTeX Warning: `h' float specifier changed to `ht'.
576	
577	
578	LaTeX Warning: `h' float specifier changed to `ht'.
579	
580	[11
581	
582	 <./figures/fig3_decomposition.pdf> <./figures/fig2_magnitude.pdf>]
583	
584	Package hyperref Warning: Token not allowed in a PDF string (Unicode):
585	(hyperref)                removing `math shift' on input line 63.
586	
587	
588	Package hyperref Warning: Token not allowed in a PDF string (Unicode):
589	(hyperref)                removing `math shift' on input line 63.
590	
591	
592	Underfull \vbox (badness 10000) has occurred while \output is active []
593	
594	 [12 <./figures/fig3_kvalue.pdf>]
595	&lt;figures/fig4_diversity.pdf, id=666, 526.01315pt x 308.20406pt>
596	File: figures/fig4_diversity.pdf Graphic file (type pdf)
597	&lt;use figures/fig4_diversity.pdf>
598	Package pdftex.def Info: figures/fig4_diversity.pdf  used on input line 99.
599	(pdftex.def)             Requested size: 397.48499pt x 232.89722pt.
600	 [13 <./figures/fig4_diversity.pdf>]
601	
602	LaTeX Warning: `h' float specifier changed to `ht'.
603	
604	[14]) [15] (./main.aux)
605	 ***********
606	LaTeX2e <2025-11-01>
607	L3 programming layer <2026-01-19>
608	 ***********
609	Package rerunfilecheck Info: File `main.out' has not changed.
610	(rerunfilecheck)             Checksum: 4A81ACE1487BA9F88D59006070EEDD30;4308.
611	 ) 
612	Here is how much of TeX's memory you used:
613	 12112 strings out of 469438
614	 183339 string characters out of 5468411
615	 618887 words of memory out of 5000000
616	 40462 multiletter control sequences out of 15000+600000
617	 667556 words of font info for 106 fonts, out of 8000000 for 9000
618	 59 hyphenation exceptions out of 8191
619	 84i,13n,93p,978b,607s stack positions out of 10000i,1000n,20000p,200000b,200000s
620	 &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.60
621	0pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/
622	usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/sha
623	re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/tex
624	live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t
625	exmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-d
626	ist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fon
627	ts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
628	1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
629	c/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
630	fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
631	m/cmr5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p
632	fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr
633	/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t
634	exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive
635	/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-
636	dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo
637	nts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
638	e1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
639	1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
640	utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/us
641	r/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
642	Output written on main.pdf (15 pages, 544260 bytes).
643	PDF statistics:
644	 914 PDF objects out of 1000 (max. 8388607)
645	 497 compressed objects within 5 object streams
646	 110 named destinations out of 1000 (max. 500000)
647	 231 words of extra memory for PDF output out of 10000 (max. 10000000)
648	
649	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "0b4c0bd8-89da-4f1b-a12b-e45f05a8456b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.log",
      "content": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex 2026.5.2)  21 MAY 2026 15:44\nentering extended mode\n restricted \\write18 enabled.\n %&-line parsing enabled.\n**main.tex\n(./main.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo\nFile: size10.clo 2025/01/22 v1.4n Standard LaTeX file (size option)\n)\n\\c@part=\\count275\n\\c@section=\\count276\n\\c@subsection=\\count277\n\\c@subsubsection=\\count278\n\\c@paragraph=\\count279\n\\c@subparagraph=\\count280\n\\c@figure=\\count281\n\\c@table=\\count282\n\\abovecaptionskip=\\skip49\n\\belowcaptionskip=\\skip50\n\\bibindent=\\dimen148\n) (./corl_2026.sty\nPackage: corl_2026 2026/08/15 CORL2026 submission/preprint/camera-ready style f\nile\n\n(/usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty\nPackage: lineno 2025/05/13 line numbers on paragraphs v5.5\n\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty\nPackage: etoolbox 2025/10/02 v2.5m e-TeX tools for LaTeX (JAW)\n\\etb@tempcnta=\\count283\n)\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty\nPackage: kvoptions 2022-06-15 v3.15 Key value format for package options (HO)\n\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty\nPackage: keyval 2022/05/29 v1.15 key=value parser (DPC)\n\\KV@toks@=\\toks17\n)\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty\nPackage: ltxcmds 2023-12-04 v1.26 LaTeX kernel commands for general use (HO)\n)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty\nPackage: kvsetkeys 2022-10-05 v1.19 Key value parser (HO)\n))\n\\linenopenalty=\\count284\n\\output=\\toks18\n\\linenoprevgraf=\\count285\n\\linenumbersep=\\dimen149\n\\linenumberwidth=\\dimen150\n\\c@linenumber=\\count286\n\\c@pagewiselinenumber=\\count287\n\\c@LN@truepage=\\count288\n\\c@internallinenumber=\\count289\n\\c@internallinenumbers=\\count290\n\\quotelinenumbersep=\\dimen151\n\\bframerule=\\dimen152\n\\bframesep=\\dimen153\n\\bframebox=\\box53\n)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/color.sty\nPackage: color 2025/01/14 v1.3e Standard LaTeX Color (DPC)\n\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg\nFile: color.cfg 2016/01/02 v1.6 sample color configuration\n)\nPackage color Info: Driver file: pdftex.def on input line 149.\n\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def\nFile: pdftex.def 2025/09/29 v1.2d Graphics/color driver for pdftex\n)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty\nPackage: natbib 2010/09/13 8.31b (PWD, AO)\n\\bibhang=\\skip51\n\\bibsep=\\skip52\nLaTeX Info: Redefining \\cite on input line 694.\n\\c@NAT@ctr=\\count291\n)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\nPackage: hyperref 2025-07-12 v7.01o Hypertext links for LaTeX\n\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty\nPackage: iftex 2024/12/12 v1.0g TeX engine tests\n)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty\nPackage: kvdefinekeys 2019-12-19 v1.6 Define keys (HO)\n)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\nPackage: pdfescape 2019/12/09 v1.15 Implements pdfTeX's escape features (HO)\n\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\nPackage: pdftexcmds 2020-06-27 v0.33 Utility functions of pdfTeX for LuaTeX (HO\n)\n\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty\nPackage: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)\n)\nPackage pdftexcmds Info: \\pdf@primitive is available.\nPackage pdftexcmds Info: \\pdf@ifprimitive is available.\nPackage pdftexcmds Info: \\pdfdraftmode found.\n))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty\nPackage: hycolor 2020-01-27 v1.10 Color options for hyperref/bookmark (HO)\n)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\nPackage: nameref 2025-06-21 v2.57 Cross-referencing by name of section\n\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty\nPackage: refcount 2019/12/15 v3.6 Data extraction from label references (HO)\n)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\nPackage: gettitlestring 2019/12/15 v1.6 Cleanup title references (HO)\n)\n\\c@section@level=\\count292\n)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty\nPackage: stringenc 2019/11/29 v1.12 Convert strings between diff. encodings (HO\n)\n)\n\\@linkdim=\\dimen154\n\\Hy@linkcounter=\\count293\n\\Hy@pagecounter=\\count294\n\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def\nFile: pd1enc.def 2025-07-12 v7.01o Hyperref: PDFDocEncoding definition (HO)\nNow handling font encoding PD1 ...\n... no UTF-8 mapping file for font encoding PD1\n)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty\nPackage: intcalc 2019/12/15 v1.3 Expandable calculations with integers (HO)\n)\n\\Hy@SavedSpaceFactor=\\count295\n\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def\nFile: puenc.def 2025-07-12 v7.01o Hyperref: PDF Unicode definition (HO)\nNow handling font encoding PU ...\n... no UTF-8 mapping file for font encoding PU\n)\nPackage hyperref Info: Hyper figures OFF on input line 4195.\nPackage hyperref Info: Link nesting OFF on input line 4200.\nPackage hyperref Info: Hyper index ON on input line 4203.\nPackage hyperref Info: Plain pages OFF on input line 4210.\nPackage hyperref Info: Backreferencing OFF on input line 4215.\nPackage hyperref Info: Implicit mode ON; LaTeX internals redefined.\nPackage hyperref Info: Bookmarks ON on input line 4462.\n\\c@Hy@tempcnt=\\count296\n\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty\n\\Urlmuskip=\\muskip17\nPackage: url 2013/09/16  ver 3.4  Verb mode for urls, etc.\n)\nLaTeX Info: Redefining \\url on input line 4801.\n\\XeTeXLinkMargin=\\dimen155\n\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\nPackage: bitset 2019/12/09 v1.3 Handle bit-vector datatype (HO)\n\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty\nPackage: bigintcalc 2019/12/15 v1.5 Expandable calculations on big integers (HO\n)\n))\n\\Fld@menulength=\\count297\n\\Field@Width=\\dimen156\n\\Fld@charsize=\\dimen157\nPackage hyperref Info: Hyper figures OFF on input line 6078.\nPackage hyperref Info: Link nesting OFF on input line 6083.\nPackage hyperref Info: Hyper index ON on input line 6086.\nPackage hyperref Info: backreferencing OFF on input line 6093.\nPackage hyperref Info: Link coloring OFF on input line 6098.\nPackage hyperref Info: Link coloring with OCG OFF on input line 6103.\nPackage hyperref Info: PDF/A mode OFF on input line 6108.\n\\Hy@abspage=\\count298\n\\c@Item=\\count299\n\\c@Hfootnote=\\count300\n)\nPackage hyperref Info: Driver (autodetected): hpdftex.\n\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\nFile: hpdftex.def 2025-07-12 v7.01o Hyperref driver for pdfTeX\n\\Fld@listcount=\\count301\n\\c@bookmark@seq@number=\\count302\n\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\nPackage: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)\n\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty\nPackage: uniquecounter 2019/12/15 v1.4 Provide unlimited unique counter (HO)\n)\nPackage uniquecounter Info: New unique counter `rerunfilecheck' on input line 2\n84.\n)\n\\Hy@SectionHShift=\\skip53\n)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\nPackage: geometry 2020/01/02 v5.9 Page Geometry\n\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\nPackage: ifvtex 2019/10/25 v1.7 ifvtex legacy package. Use iftex instead.\n)\n\\Gm@cnth=\\count303\n\\Gm@cntv=\\count304\n\\c@Gm@tempcnt=\\count305\n\\Gm@bindingoffset=\\dimen158\n\\Gm@wd@mp=\\dimen159\n\\Gm@odd@mp=\\dimen160\n\\Gm@even@mp=\\dimen161\n\\Gm@layoutwidth=\\dimen162\n\\Gm@layoutheight=\\dimen163\n\\Gm@layouthoffset=\\dimen164\n\\Gm@layoutvoffset=\\dimen165\n\\Gm@dimlist=\\toks19\n)\nPackage hyperref Info: Option `colorlinks' set `true' on input line 114.\n\\@nipsabovecaptionskip=\\skip54\n\\@nipsbelowcaptionskip=\\skip55\n)\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty\nPackage: inputenc 2024/02/08 v1.3d Input encoding file\n\\inpenc@prehook=\\toks20\n\\inpenc@posthook=\\toks21\n)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty\nPackage: fontenc 2025/07/18 v2.1d Standard LaTeX package\nLaTeX Font Info:    Trying to load font information for T1+ptm on input line 11\n6.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd\nFile: t1ptm.fd 2001/06/04 font definitions for T1/ptm.\n))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nPackage: amsmath 2025/07/09 v2.17z AMS math features\n\\@mathmargin=\\skip56\n\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\nPackage: amstext 2024/11/17 v2.01 AMS text\n\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty\nFile: amsgen.sty 1999/11/30 v2.0 generic functions\n\\@emptytoks=\\toks22\n\\ex@=\\dimen166\n))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty\nPackage: amsbsy 1999/11/29 v1.2d Bold Symbols\n\\pmbraise@=\\dimen167\n)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty\nPackage: amsopn 2022/04/08 v2.04 operator names\n)\n\\inf@bad=\\count306\nLaTeX Info: Redefining \\frac on input line 233.\n\\uproot@=\\count307\n\\leftroot@=\\count308\nLaTeX Info: Redefining \\overline on input line 398.\nLaTeX Info: Redefining \\colon on input line 409.\n\\classnum@=\\count309\n\\DOTSCASE@=\\count310\nLaTeX Info: Redefining \\ldots on input line 495.\nLaTeX Info: Redefining \\dots on input line 498.\nLaTeX Info: Redefining \\cdots on input line 619.\n\\Mathstrutbox@=\\box54\n\\strutbox@=\\box55\nLaTeX Info: Redefining \\big on input line 721.\nLaTeX Info: Redefining \\Big on input line 722.\nLaTeX Info: Redefining \\bigg on input line 723.\nLaTeX Info: Redefining \\Bigg on input line 724.\n\\big@size=\\dimen168\nLaTeX Font Info:    Redeclaring font encoding OML on input line 742.\nLaTeX Font Info:    Redeclaring font encoding OMS on input line 743.\n\\macc@depth=\\count311\nLaTeX Info: Redefining \\bmod on input line 904.\nLaTeX Info: Redefining \\pmod on input line 909.\nLaTeX Info: Redefining \\smash on input line 939.\nLaTeX Info: Redefining \\relbar on input line 969.\nLaTeX Info: Redefining \\Relbar on input line 970.\n\\c@MaxMatrixCols=\\count312\n\\dotsspace@=\\muskip18\n\\c@parentequation=\\count313\n\\dspbrk@lvl=\\count314\n\\tag@help=\\toks23\n\\row@=\\count315\n\\column@=\\count316\n\\maxfields@=\\count317\n\\andhelp@=\\toks24\n\\eqnshift@=\\dimen169\n\\alignsep@=\\dimen170\n\\tagshift@=\\dimen171\n\\tagwidth@=\\dimen172\n\\totwidth@=\\dimen173\n\\lineht@=\\dimen174\n\\@envbody=\\toks25\n\\multlinegap=\\skip57\n\\multlinetaggap=\\skip58\n\\mathdisplay@stack=\\toks26\nLaTeX Info: Redefining \\[ on input line 2950.\nLaTeX Info: Redefining \\] on input line 2951.\n)\n\\@LN@amsmath@ams@eqpen=\\count318\n\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\nPackage: amssymb 2013/01/14 v3.01 AMS font symbols\n\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty\nPackage: amsfonts 2013/01/14 v3.01 Basic AMSFonts support\n\\symAMSa=\\mathgroup4\n\\symAMSb=\\mathgroup5\nLaTeX Font Info:    Redeclaring math symbol \\hbar on input line 98.\nLaTeX Font Info:    Overwriting math alphabet `\\mathfrak' in version `bold'\n(Font)                  U/euf/m/n --> U/euf/b/n on input line 106.\n))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\nPackage: graphicx 2024/12/31 v1.2e Enhanced LaTeX Graphics (DPC,SPQR)\n\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\nPackage: graphics 2024/08/06 v1.4g Standard LaTeX Graphics (DPC,SPQR)\n\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty\nPackage: trig 2023/12/02 v1.11 sin cos tan (DPC)\n)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg\nFile: graphics.cfg 2016/06/04 v1.11 sample graphics configuration\n)\nPackage graphics Info: Driver file: pdftex.def on input line 106.\n)\n\\Gin@req@height=\\dimen175\n\\Gin@req@width=\\dimen176\n)\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty\nPackage: booktabs 2020/01/12 v1.61803398 Publication quality tables\n\\heavyrulewidth=\\dimen177\n\\lightrulewidth=\\dimen178\n\\cmidrulewidth=\\dimen179\n\\belowrulesep=\\dimen180\n\\belowbottomsep=\\dimen181\n\\aboverulesep=\\dimen182\n\\abovetopsep=\\dimen183\n\\cmidrulesep=\\dimen184\n\\cmidrulekern=\\dimen185\n\\defaultaddspace=\\dimen186\n\\@cmidla=\\count319\n\\@cmidlb=\\count320\n\\@aboverulesep=\\dimen187\n\\@belowrulesep=\\dimen188\n\\@thisruleclass=\\count321\n\\@lastruleclass=\\count322\n\\@thisrulewidth=\\dimen189\n)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty\nPackage: enumitem 2025/02/06 v3.11 Customized lists\n\\labelindent=\\skip59\n\\enit@outerparindent=\\dimen190\n\\enit@toks=\\toks27\n\\enit@inbox=\\box56\n\\enit@count@id=\\count323\n\\enitdp@description=\\count324\n)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty\nPackage: multirow 2024/11/12 v2.9 Span multiple rows of a table\n\\multirow@colwidth=\\skip60\n\\multirow@cntb=\\count325\n\\multirow@dima=\\skip61\n\\bigstrutjot=\\dimen191\n)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def\nFile: l3backend-pdftex.def 2025-10-09 L3 backend support: PDF output (pdfTeX)\n\\l__color_backend_stack_int=\\count326\n)\n(./main.aux)\n\\openout1 = `main.aux'.\n\nLaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 25.\nLaTeX Font Info:    ... okay on input line 25.\nLaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 25.\nLaTeX Font Info:    ... okay on input line 25.\nLaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 25.\nLaTeX Font Info:    ... okay on input line 25.\nLaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 25.\nLaTeX Font Info:    ... okay on input line 25.\nLaTeX Font Info:    Checking defaults for TS1/cmr/m/n on input line 25.\nLaTeX Font Info:    ... okay on input line 25.\nLaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 25.\nLaTeX Font Info:    ... okay on input line 25.\nLaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 25.\nLaTeX Font Info:    ... okay on input line 25.\nLaTeX Font Info:    Checking defaults for PD1/pdf/m/n on input line 25.\nLaTeX Font Info:    ... okay on input line 25.\nLaTeX Font Info:    Checking defaults for PU/pdf/m/n on input line 25.\nLaTeX Font Info:    ... okay on input line 25.\n (/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n\\scratchcounter=\\count327\n\\scratchdimen=\\dimen192\n\\scratchbox=\\box57\n\\nofMPsegments=\\count328\n\\nofMParguments=\\count329\n\\everyMPshowfont=\\toks28\n\\MPscratchCnt=\\count330\n\\MPscratchDim=\\dimen193\n\\MPnumerator=\\count331\n\\makeMPintoPDFobject=\\count332\n\\everyMPtoPDFconversion=\\toks29\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\nPackage: epstopdf-base 2020-01-24 v2.11 Base part for package epstopdf\nPackage epstopdf-base Info: Redefining graphics rule for `.eps' on input line 4\n85.\n\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg\nFile: epstopdf-sys.cfg 2010/07/13 v1.3 Configuration of (r)epstopdf for TeX Liv\ne\n))\n*geometry* verbose mode - [ newgeometry ] result:\n* driver: \n* paper: letterpaper\n* layout: &lt;same size as paper>\n* layoutoffset:(h,v)=(0.0pt,0.0pt)\n* modes: \n* h-part:(L,W,R)=(108.405pt, 397.48499pt, 108.40501pt)\n* v-part:(T,H,B)=(72.26999pt, 650.43pt, 72.27pt)\n* \\paperwidth=614.295pt\n* \\paperheight=794.96999pt\n* \\textwidth=397.48499pt\n* \\textheight=650.43pt\n* \\oddsidemargin=36.13501pt\n* \\evensidemargin=36.13501pt\n* \\topmargin=-37.0pt\n* \\headheight=12.0pt\n* \\headsep=25.0pt\n* \\topskip=10.0pt\n* \\footskip=30.0pt\n* \\marginparwidth=65.0pt\n* \\marginparsep=11.0pt\n* \\columnsep=10.0pt\n* \\skip\\footins=9.0pt plus 4.0pt minus 2.0pt\n* \\hoffset=0.0pt\n* \\voffset=0.0pt\n* \\mag=1000\n* \\@twocolumnfalse\n* \\@twosidefalse\n* \\@mparswitchfalse\n* \\@reversemarginfalse\n* (1in=72.27pt=25.4mm, 1cm=28.453pt)\n\nPackage hyperref Info: Link coloring ON on input line 25.\n(./main.out) (./main.out)\n\\@outlinefile=\\write3\n\\openout3 = `main.out'.\n\n\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n*geometry* verbose mode - [ preamble ] result:\n* driver: pdftex\n* paper: letterpaper\n* layout: &lt;same size as paper>\n* layoutoffset:(h,v)=(0.0pt,0.0pt)\n* modes: \n* h-part:(L,W,R)=(108.405pt, 397.48499pt, 108.40501pt)\n* v-part:(T,H,B)=(72.26999pt, 650.43pt, 72.27pt)\n* \\paperwidth=614.295pt\n* \\paperheight=794.96999pt\n* \\textwidth=397.48499pt\n* \\textheight=650.43pt\n* \\oddsidemargin=36.13501pt\n* \\evensidemargin=36.13501pt\n* \\topmargin=-37.0pt\n* \\headheight=12.0pt\n* \\headsep=25.0pt\n* \\topskip=10.0pt\n* \\footskip=30.0pt\n* \\marginparwidth=65.0pt\n* \\marginparsep=11.0pt\n* \\columnsep=10.0pt\n* \\skip\\footins=9.0pt plus 4.0pt minus 2.0pt\n* \\hoffset=0.0pt\n* \\voffset=0.0pt\n* \\mag=1000\n* \\@twocolumnfalse\n* \\@twosidefalse\n* \\@mparswitchfalse\n* \\@reversemarginfalse\n* (1in=72.27pt=25.4mm, 1cm=28.453pt)\n\nLaTeX Font Info:    Trying to load font information for U+msa on input line 27.\n\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd\nFile: umsa.fd 2013/01/14 v3.01 AMS symbols A\n)\nLaTeX Font Info:    Trying to load font information for U+msb on input line 27.\n\n\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd\nFile: umsb.fd 2013/01/14 v3.01 AMS symbols B\n) (./abstract.tex)\nLaTeX Font Info:    Trying to load font information for T1+phv on input line 31\n.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1phv.fd\nFile: t1phv.fd 2020/03/25 scalable font definitions for T1/phv.\n)\nUnderfull \\hbox (badness 3690) in paragraph at lines 33--33\n[]\\T1/ptm/b/n/10 Keywords: \\T1/ptm/m/n/10 Vision-Language-Action Mod-els, Infer\nence-Time Re-fine-ment,\n []\n\n(./introduction.tex [1\n\n\n{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-di\nst/fonts/enc/dvips/base/8r.enc}]) (./related_work.tex\nUnderfull \\hbox (badness 1194) in paragraph at lines 8--9\n []\\T1/ptm/b/n/10 Training-time meth-ods.[] \\T1/ptm/m/n/10 Re-cent ap-proaches \nim-prove ro-bust-ness through mod-i-fied train-ing.\n []\n\n[2]) (./method.tex\n&lt;figures/fig1_pipeline.pdf, id=190, 537.00134pt x 209.31084pt>\nFile: figures/fig1_pipeline.pdf Graphic file (type pdf)\n&lt;use figures/fig1_pipeline.pdf>\nPackage pdftex.def Info: figures/fig1_pipeline.pdf  used on input line 7.\n(pdftex.def)             Requested size: 397.48499pt x 154.9291pt.\n\nUnderfull \\vbox (badness 10000) has occurred while \\output is active []\n\n [3]\nUnderfull \\hbox (badness 1502) in paragraph at lines 37--38\n []\\T1/ptm/b/n/10 Architecture.[] \\T1/ptm/m/n/10 The CRM con-sists of three ful\nly con-nected lay-ers with ReLU ac-ti-va-tions:\n []\n\n[4 <./figures/fig1_pipeline.pdf>]\nLaTeX Font Info:    Trying to load font information for TS1+ptm on input line 4\n7.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd\nFile: ts1ptm.fd 2001/06/04 font definitions for TS1/ptm.\n) [5])\n(./experiments.tex\n&lt;figures/fig5_k2_correlation.pdf, id=361, 706.15883pt x 330.00478pt>\nFile: figures/fig5_k2_correlation.pdf Graphic file (type pdf)\n&lt;use figures/fig5_k2_correlation.pdf>\nPackage pdftex.def Info: figures/fig5_k2_correlation.pdf  used on input line 31\n.\n(pdftex.def)             Requested size: 397.48499pt x 185.7531pt.\n [6] [7 <./figures/fig5_k2_correlation.pdf>])\n(./discussion.tex) (./main.bbl [8] [9]) [10] (./appendix.tex\n&lt;figures/fig3_decomposition.pdf, id=488, 414.79512pt x 235.77295pt>\nFile: figures/fig3_decomposition.pdf Graphic file (type pdf)\n&lt;use figures/fig3_decomposition.pdf>\nPackage pdftex.def Info: figures/fig3_decomposition.pdf  used on input line 9.\n(pdftex.def)             Requested size: 397.48499pt x 225.94011pt.\n&lt;figures/fig2_magnitude.pdf, id=489, 492.92154pt x 174.60608pt>\nFile: figures/fig2_magnitude.pdf Graphic file (type pdf)\n&lt;use figures/fig2_magnitude.pdf>\nPackage pdftex.def Info: figures/fig2_magnitude.pdf  used on input line 19.\n(pdftex.def)             Requested size: 397.48499pt x 140.80136pt.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 24.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 24.\n\n&lt;figures/fig3_kvalue.pdf, id=491, 380.93694pt x 281.18738pt>\nFile: figures/fig3_kvalue.pdf Graphic file (type pdf)\n&lt;use figures/fig3_kvalue.pdf>\nPackage pdftex.def Info: figures/fig3_kvalue.pdf  used on input line 31.\n(pdftex.def)             Requested size: 397.48499pt x 293.42339pt.\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[11\n\n <./figures/fig3_decomposition.pdf> <./figures/fig2_magnitude.pdf>]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 63.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 63.\n\n\nUnderfull \\vbox (badness 10000) has occurred while \\output is active []\n\n [12 <./figures/fig3_kvalue.pdf>]\n&lt;figures/fig4_diversity.pdf, id=666, 526.01315pt x 308.20406pt>\nFile: figures/fig4_diversity.pdf Graphic file (type pdf)\n&lt;use figures/fig4_diversity.pdf>\nPackage pdftex.def Info: figures/fig4_diversity.pdf  used on input line 99.\n(pdftex.def)             Requested size: 397.48499pt x 232.89722pt.\n [13 <./figures/fig4_diversity.pdf>]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[14]) [15] (./main.aux)\n ***********\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n ***********\nPackage rerunfilecheck Info: File `main.out' has not changed.\n(rerunfilecheck)             Checksum: 4A81ACE1487BA9F88D59006070EEDD30;4308.\n ) \nHere is how much of TeX's memory you used:\n 12112 strings out of 469438\n 183339 string characters out of 5468411\n 618887 words of memory out of 5000000\n 40462 multiletter control sequences out of 15000+600000\n 667556 words of font info for 106 fonts, out of 8000000 for 9000\n 59 hyphenation exceptions out of 8191\n 84i,13n,93p,978b,607s stack positions out of 10000i,1000n,20000p,200000b,200000s\n &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.60\n0pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (15 pages, 544260 bytes).\nPDF statistics:\n 914 PDF objects out of 1000 (max. 8388607)\n 497 compressed objects within 5 object streams\n 110 named destinations out of 1000 (max. 500000)\n 231 words of extra memory for PDF output out of 10000 (max. 10000000)\n\n",
      "numLines": 649,
      "startLine": 1,
      "totalLines": 649
    }
  }
}
```

</details>

---


### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "0d405463-f644-4994-a485-38b0c7179f9a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UAxVgckoqyVXPeSGsJ1H6L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21323,
      "cache_read_input_tokens": 84012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21323
      },
      "output_tokens": 74,
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

_source line 60_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01GSwqWJ7p9eQX2nCU6fNbVA`</summary>

```json
{
  "todos": [
    {
      "content": "Explore paper LaTeX source structure",
      "activeForm": "Exploring paper LaTeX source structure",
      "status": "completed"
    },
    {
      "content": "Attempt compilation and capture warnings/errors",
      "activeForm": "Attempting compilation and capturing warnings/errors",
      "status": "in_progress"
    },
    {
      "content": "Cross-check numerical claims against registry",
      "activeForm": "Cross-checking numerical claims against registry",
      "status": "pending"
    },
    {
      "content": "Audit pi0.5 / OpenVLA section coverage gaps",
      "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps",
      "status": "pending"
    },
    {
      "content": "Verify .bib entries and \\cite{} resolution",
      "activeForm": "Verifying .bib entries and \\cite{} resolution",
      "status": "pending"
    },
    {
      "content": "Write audit report to artifacts and register",
      "activeForm": "Writing audit report to artifacts and registering",
      "status": "pending"
    }
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "daca31e0-5aa4-4fc3-a8dc-f8f00825febe",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UAxVgckoqyVXPeSGsJ1H6L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21323,
      "cache_read_input_tokens": 84012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21323
      },
      "output_tokens": 74,
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

_source line 61 · 2026-05-21T16:39:23.393Z_

<details><summary>↩ Tool result · `toolu_01GSwqWJ7p9eQX2nCU6fNbVA`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "7b8c32bc-c2be-4f61-b93f-733100617e5e",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Explore paper LaTeX source structure",
        "status": "in_progress",
        "activeForm": "Exploring paper LaTeX source structure"
      },
      {
        "content": "Attempt compilation and capture warnings/errors",
        "status": "pending",
        "activeForm": "Attempting compilation and capturing warnings/errors"
      },
      {
        "content": "Cross-check numerical claims against registry",
        "status": "pending",
        "activeForm": "Cross-checking numerical claims against registry"
      },
      {
        "content": "Audit pi0.5 / OpenVLA section coverage gaps",
        "status": "pending",
        "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps"
      },
      {
        "content": "Verify .bib entries and \\cite{} resolution",
        "status": "pending",
        "activeForm": "Verifying .bib entries and \\cite{} resolution"
      },
      {
        "content": "Write audit report to artifacts and register",
        "status": "pending",
        "activeForm": "Writing audit report to artifacts and registering"
      }
    ],
    "newTodos": [
      {
        "content": "Explore paper LaTeX source structure",
        "status": "completed",
        "activeForm": "Exploring paper LaTeX source structure"
      },
      {
        "content": "Attempt compilation and capture warnings/errors",
        "status": "in_progress",
        "activeForm": "Attempting compilation and capturing warnings/errors"
      },
      {
        "content": "Cross-check numerical claims against registry",
        "status": "pending",
        "activeForm": "Cross-checking numerical claims against registry"
      },
      {
        "content": "Audit pi0.5 / OpenVLA section coverage gaps",
        "status": "pending",
        "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps"
      },
      {
        "content": "Verify .bib entries and \\cite{} resolution",
        "status": "pending",
        "activeForm": "Verifying .bib entries and \\cite{} resolution"
      },
      {
        "content": "Write audit report to artifacts and register",
        "status": "pending",
        "activeForm": "Writing audit report to artifacts and registering"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_018metr4rnATrN4Ke2H4UF58`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.blg"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "42737cbb-8214-4061-b637-45e919de0121",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012uJSn8DH83qQ41zGPBYVvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 105335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 579
      },
      "output_tokens": 46,
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

_source line 63 · 2026-05-21T16:39:26.901Z_

<details><summary>↩ Tool result · `toolu_018metr4rnATrN4Ke2H4UF58`</summary>

```text
1	This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
2	Capacity: max_strings=200000, hash_size=200000, hash_prime=170003
3	The top-level auxiliary file: main.aux
4	The style file: corlabbrvnat.bst
5	Database file #1: references.bib
6	You've used 31 entries,
7	            2773 wiz_defined-function locations,
8	            709 strings with 12551 characters,
9	and the built_in function-call counts, 22754 in all, are:
10	= -- 1624
11	> -- 2631
12	< -- 4
13	+ -- 879
14	- -- 846
15	* -- 2188
16	:= -- 3708
17	add.period$ -- 81
18	call.type$ -- 31
19	change.case$ -- 375
20	chr.to.int$ -- 29
21	cite$ -- 62
22	duplicate$ -- 609
23	empty$ -- 1139
24	format.name$ -- 883
25	if$ -- 4499
26	int.to.chr$ -- 3
27	int.to.str$ -- 1
28	missing$ -- 14
29	newline$ -- 151
30	num.names$ -- 124
31	pop$ -- 858
32	preamble$ -- 1
33	purify$ -- 344
34	quote$ -- 0
35	skip$ -- 688
36	stack$ -- 0
37	substring$ -- 127
38	swap$ -- 58
39	text.length$ -- 1
40	text.prefix$ -- 0
41	top$ -- 0
42	type$ -- 341
43	warning$ -- 0
44	while$ -- 98
45	width$ -- 0
46	write$ -- 357
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "a9f068a9-da08-47f8-aa95-2fb836fc49b2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.blg",
      "content": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nCapacity: max_strings=200000, hash_size=200000, hash_prime=170003\nThe top-level auxiliary file: main.aux\nThe style file: corlabbrvnat.bst\nDatabase file #1: references.bib\nYou've used 31 entries,\n            2773 wiz_defined-function locations,\n            709 strings with 12551 characters,\nand the built_in function-call counts, 22754 in all, are:\n= -- 1624\n> -- 2631\n< -- 4\n+ -- 879\n- -- 846\n* -- 2188\n:= -- 3708\nadd.period$ -- 81\ncall.type$ -- 31\nchange.case$ -- 375\nchr.to.int$ -- 29\ncite$ -- 62\nduplicate$ -- 609\nempty$ -- 1139\nformat.name$ -- 883\nif$ -- 4499\nint.to.chr$ -- 3\nint.to.str$ -- 1\nmissing$ -- 14\nnewline$ -- 151\nnum.names$ -- 124\npop$ -- 858\npreamble$ -- 1\npurify$ -- 344\nquote$ -- 0\nskip$ -- 688\nstack$ -- 0\nsubstring$ -- 127\nswap$ -- 58\ntext.length$ -- 1\ntext.prefix$ -- 0\ntop$ -- 0\ntype$ -- 341\nwarning$ -- 0\nwhile$ -- 98\nwidth$ -- 0\nwrite$ -- 357\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  }
}
```

</details>

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_014RvbHeYcHabTe4fbnvDj7A`</summary>

```json
{
  "command": "which pdflatex bibtex latexmk 2>&1; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/figures/",
  "description": "Check tools and figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "ddc40382-3af1-4f5f-b5bc-b8566d2e6442",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012uJSn8DH83qQ41zGPBYVvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 105335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 579
      },
      "output_tokens": 46,
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

_source line 65 · 2026-05-21T16:39:28.504Z_

<details><summary>↩ Tool result · `toolu_014RvbHeYcHabTe4fbnvDj7A`</summary>

```text
/usr/bin/pdflatex
/usr/bin/bibtex
/usr/bin/latexmk
fig1_pipeline.pdf
fig1_pipeline.png
fig2_magnitude.pdf
fig3_decomposition.pdf
fig3_kvalue.pdf
fig4_diversity.pdf
fig5_k2_correlation.pdf
fig5_k2_correlation.png
fig_magnitude_curve.py
magnitude_curve.pdf
magnitude_curve.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "910594df-6135-4aca-899a-062036a79381",
  "tool_use_result": {
    "stdout": "/usr/bin/pdflatex\n/usr/bin/bibtex\n/usr/bin/latexmk\nfig1_pipeline.pdf\nfig1_pipeline.png\nfig2_magnitude.pdf\nfig3_decomposition.pdf\nfig3_kvalue.pdf\nfig4_diversity.pdf\nfig5_k2_correlation.pdf\nfig5_k2_correlation.png\nfig_magnitude_curve.py\nmagnitude_curve.pdf\nmagnitude_curve.png",
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

_source line 66_

<details open><summary>🔧 Tool call — Bash · `toolu_01NgekpbUUVQpMg6CZAAJFyP`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -80",
  "description": "Run latexmk to verify build",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "440e6746-2250-48fb-9c42-f1b8ce76ec09",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019yWnBc1T2fyd4Eu3bUWHoi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 105914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 67 · 2026-05-21T16:39:32.084Z_

<details><summary>↩ Tool result · `toolu_01NgekpbUUVQpMg6CZAAJFyP`</summary>

```text
Rc files read:
  /etc/LatexMk
Latexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.
Latexmk: Nothing to do for 'main.tex'.
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "5ff67b27-9749-4fe8-8def-004e4f595a4e",
  "tool_use_result": {
    "stdout": "Rc files read:\n  /etc/LatexMk\nLatexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.\nLatexmk: Nothing to do for 'main.tex'.\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_01QGgLYV1g8U3fzxCXmFxpFk`</summary>

```json
{
  "command": "latexmk -C >/dev/null 2>&1; latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tail -40",
  "description": "Clean build to refresh",
  "timeout": 180000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "c4a3eadb-c4a7-454f-ad23-d82de0b666a2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01J4ix62aJjQvQTGLgWE58Us",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 107011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 69 · 2026-05-21T16:39:37.390Z_

<details><summary>↩ Tool result · `toolu_01QGgLYV1g8U3fzxCXmFxpFk`</summary>

```text
LaTeX Warning: `h' float specifier changed to `ht'.

[14]) [15] (./main.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/ms
bm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (15 pages, 544260 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "25280162-d066-408d-9608-87f94a838c67",
  "tool_use_result": {
    "stdout": "LaTeX Warning: `h' float specifier changed to `ht'.\n\n[14]) [15] (./main.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/ms\nbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (15 pages, 544260 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 70_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "f5251e77-4a93-47b6-b03b-a9298337276f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DtJQbq39Kmc91HTVB3XM6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1540,
      "cache_read_input_tokens": 107324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1540
      },
      "output_tokens": 56,
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

_source line 71_

<details open><summary>🔧 Tool call — Grep · `toolu_01PCPaTgsexoPGTL8GEqH9y1`</summary>

```json
{
  "pattern": "^(LaTeX Warning|LaTeX Error|! |Underfull|Overfull|Package .* Warning|Citation|Reference)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.log",
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "548d9701-159d-427e-8e5f-11b81a1176b4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DtJQbq39Kmc91HTVB3XM6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1540,
      "cache_read_input_tokens": 107324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1540
      },
      "output_tokens": 56,
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

_source line 72 · 2026-05-21T16:39:45.652Z_

<details><summary>↩ Tool result · `toolu_01PCPaTgsexoPGTL8GEqH9y1`</summary>

```text
504:Underfull \hbox (badness 3690) in paragraph at lines 33--33
514:Underfull \hbox (badness 1194) in paragraph at lines 8--9
526:Underfull \vbox (badness 10000) has occurred while \output is active []
529:Underfull \hbox (badness 1502) in paragraph at lines 37--38
562:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
566:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
575:LaTeX Warning: `h' float specifier changed to `ht'.
578:LaTeX Warning: `h' float specifier changed to `ht'.
584:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
588:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
592:Underfull \vbox (badness 10000) has occurred while \output is active []
602:LaTeX Warning: `h' float specifier changed to `ht'.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "f8f37618-0ca6-4320-83f1-0639fc0898b6",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "504:Underfull \\hbox (badness 3690) in paragraph at lines 33--33\n514:Underfull \\hbox (badness 1194) in paragraph at lines 8--9\n526:Underfull \\vbox (badness 10000) has occurred while \\output is active []\n529:Underfull \\hbox (badness 1502) in paragraph at lines 37--38\n562:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n566:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n575:LaTeX Warning: `h' float specifier changed to `ht'.\n578:LaTeX Warning: `h' float specifier changed to `ht'.\n584:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n588:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n592:Underfull \\vbox (badness 10000) has occurred while \\output is active []\n602:LaTeX Warning: `h' float specifier changed to `ht'.",
    "numLines": 12
  }
}
```

</details>

---


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Grep · `toolu_0189NumjACQRqZX1zozxnS7s`</summary>

```json
{
  "pattern": "undefined|multiply.defined|missing",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.log",
  "output_mode": "content",
  "-i": true,
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "4724e4ee-8d76-4af7-b5a9-2883727d6db5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DtJQbq39Kmc91HTVB3XM6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1540,
      "cache_read_input_tokens": 107324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1540
      },
      "output_tokens": 56,
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

_source line 74 · 2026-05-21T16:39:47.233Z_

<details><summary>↩ Tool result · `toolu_0189NumjACQRqZX1zozxnS7s`</summary>

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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "53457f8a-f4ae-490c-93a3-8cb7697794ea",
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


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Grep · `toolu_01MB4Hs9upvXCz4UBJYETx2n`</summary>

```json
{
  "pattern": "\\\\cite\\{([^}]+)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "9394cd3a-e985-48f6-ad06-b38a8a664f4c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DtJQbq39Kmc91HTVB3XM6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1540,
      "cache_read_input_tokens": 107324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1540
      },
      "output_tokens": 56,
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

_source line 76 · 2026-05-21T16:39:48.613Z_

<details><summary>↩ Tool result · `toolu_01MB4Hs9upvXCz4UBJYETx2n`</summary>

```text
related_work.tex:5:[Omitted long matching line]
related_work.tex:8:[Omitted long matching line]
related_work.tex:11:ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds but does not learn corrective residuals. SC-VLA~\cite{liu2026scvla} performs online refinement through sparse world imagination combined with residual RL, but still requires task-level RL training. VLA-Pilot~\cite{li2025vlapilot} uses evolutionary diffusion optimization guided by an MLLM verifier at 2.41\,s per control step.
related_work.tex:13:[Omitted long matching line]
related_work.tex:17:[Omitted long matching line]
related_work.tex:21:Test-time compute scaling in language models improves output quality by generating multiple candidates and selecting among them~\cite{snell2024scaling}. RoVer~\cite{dai2025rover} transfers this principle to VLAs with a reward model that scores candidates in a best-of-N scheme. DA-SIP~\cite{chun2025dasip} adapts the number of denoising steps based on per-step difficulty rather than using a fixed budget.
related_work.tex:24:Conformal prediction~\cite{angelopoulos2023gentle} has been applied to robotics for safety constraints~\cite{zhou2025acp_cbf,wang2025cploop} and teleoperation calibration~\cite{zhao2024conformalized}; we test CP scores as correction features and find they do not improve over observation-only conditioning (Section~\ref{sec:magnitude_results}).
experiments.tex:5:\looseness=-1 We evaluate the pipeline on two LIBERO task suites~\cite{liu2023libero}, asking: (i)~can a cheap uncertainty probe enable adaptive compute allocation? (ii)~what is the relative contribution of selection vs.\ correction? (iii)~how does conditioning interact with magnitude? (iv)~where does the pipeline fail?
experiments.tex:12:We build on SmolVLA~\cite{shukor2025smolvla} (450M parameters, flow matching), using dual-camera RGB ($256{\times}256$) and 8D proprioceptive state. Actions are 7D (6D pose + 1D gripper); the gripper is thresholded outside the pipeline.
experiments.tex:107:We further validate cross-VLA generalization on $\pi_{0.5}$ (3.6B)~\cite{black2024pi0}; see Appendix~\ref{sec:cross_vla}.
method.tex:48:  \item \textbf{perdof}: $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}};\, \mathbf{u}_{\mathrm{dof}}] \in \mathbb{R}^{1030}$, 337K parameters. $\mathbf{u}_{\mathrm{dof}}$ concatenates per-DOF standard deviations, conformal prediction radii~\cite{angelopoulos2023gentle}, and covariance log-volumes~\cite{ledoit2004well} ($40$D total).
method.tex:54:\looseness=-1 The CRM is trained offline on demonstration trajectories from LIBERO~\cite{liu2023libero} with $L_2$ loss:
method.tex:59:[Omitted long matching line]
appendix.tex:59:The diminishing-returns pattern is loosely analogous to inference-time compute scaling in LLMs~\cite{snell2024scaling}, though the mechanism differs: in our setting, additional samples improve the starting point for correction rather than enabling better selection.
appendix.tex:95:The multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\cite{kim2024openvla} (autoregressive tokenization, 7B).
appendix.tex:182:[Omitted long matching line]
introduction.tex:6:Flow-matching VLAs~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} are natural candidates: each forward pass produces a stochastic action sample, so drawing multiple samples opens the door to selection and correction without changing model weights.
introduction.tex:9:\looseness=-1 Recent robustness evaluations~\cite{fei2025liberoplus} show that state-of-the-art VLAs lose over 65 percentage points under common deployment perturbations, making inference-time correction practically relevant.
introduction.tex:10:Training-time methods~\cite{srpo2025,robustvla2025,digflow2025,liu2026ttvla} improve the base policy through robustness-aware objectives or test-time RL, but require retraining and remain bounded by the training distribution.
introduction.tex:11:Inference-time methods leave the policy frozen: ReconVLA~\cite{chen2026reconvla} provides uncertainty quantification but does not learn corrective residuals; A2C2~\cite{a2c2_2025} trains a per-step correction head on action chunks but applies correction unconditionally without adaptive compute allocation; VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization at 2.41\,s per control step.
introduction.tex:19:Unlike LLM test-time compute scaling~\cite{snell2024scaling} where selection is primary, here the $K{=}2$ probe provides a centered starting point and uncertainty gate for learned correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "5356da87-dab6-4a69-9636-2ff25cf7bc8a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "related_work.tex:5:[Omitted long matching line]\nrelated_work.tex:8:[Omitted long matching line]\nrelated_work.tex:11:ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds but does not learn corrective residuals. SC-VLA~\\cite{liu2026scvla} performs online refinement through sparse world imagination combined with residual RL, but still requires task-level RL training. VLA-Pilot~\\cite{li2025vlapilot} uses evolutionary diffusion optimization guided by an MLLM verifier at 2.41\\,s per control step.\nrelated_work.tex:13:[Omitted long matching line]\nrelated_work.tex:17:[Omitted long matching line]\nrelated_work.tex:21:Test-time compute scaling in language models improves output quality by generating multiple candidates and selecting among them~\\cite{snell2024scaling}. RoVer~\\cite{dai2025rover} transfers this principle to VLAs with a reward model that scores candidates in a best-of-N scheme. DA-SIP~\\cite{chun2025dasip} adapts the number of denoising steps based on per-step difficulty rather than using a fixed budget.\nrelated_work.tex:24:Conformal prediction~\\cite{angelopoulos2023gentle} has been applied to robotics for safety constraints~\\cite{zhou2025acp_cbf,wang2025cploop} and teleoperation calibration~\\cite{zhao2024conformalized}; we test CP scores as correction features and find they do not improve over observation-only conditioning (Section~\\ref{sec:magnitude_results}).\nexperiments.tex:5:\\looseness=-1 We evaluate the pipeline on two LIBERO task suites~\\cite{liu2023libero}, asking: (i)~can a cheap uncertainty probe enable adaptive compute allocation? (ii)~what is the relative contribution of selection vs.\\ correction? (iii)~how does conditioning interact with magnitude? (iv)~where does the pipeline fail?\nexperiments.tex:12:We build on SmolVLA~\\cite{shukor2025smolvla} (450M parameters, flow matching), using dual-camera RGB ($256{\\times}256$) and 8D proprioceptive state. Actions are 7D (6D pose + 1D gripper); the gripper is thresholded outside the pipeline.\nexperiments.tex:107:We further validate cross-VLA generalization on $\\pi_{0.5}$ (3.6B)~\\cite{black2024pi0}; see Appendix~\\ref{sec:cross_vla}.\nmethod.tex:48:  \\item \\textbf{perdof}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, \\mathbf{u}_{\\mathrm{dof}}] \\in \\mathbb{R}^{1030}$, 337K parameters. $\\mathbf{u}_{\\mathrm{dof}}$ concatenates per-DOF standard deviations, conformal prediction radii~\\cite{angelopoulos2023gentle}, and covariance log-volumes~\\cite{ledoit2004well} ($40$D total).\nmethod.tex:54:\\looseness=-1 The CRM is trained offline on demonstration trajectories from LIBERO~\\cite{liu2023libero} with $L_2$ loss:\nmethod.tex:59:[Omitted long matching line]\nappendix.tex:59:The diminishing-returns pattern is loosely analogous to inference-time compute scaling in LLMs~\\cite{snell2024scaling}, though the mechanism differs: in our setting, additional samples improve the starting point for correction rather than enabling better selection.\nappendix.tex:95:The multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\\cite{kim2024openvla} (autoregressive tokenization, 7B).\nappendix.tex:182:[Omitted long matching line]\nintroduction.tex:6:Flow-matching VLAs~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} are natural candidates: each forward pass produces a stochastic action sample, so drawing multiple samples opens the door to selection and correction without changing model weights.\nintroduction.tex:9:\\looseness=-1 Recent robustness evaluations~\\cite{fei2025liberoplus} show that state-of-the-art VLAs lose over 65 percentage points under common deployment perturbations, making inference-time correction practically relevant.\nintroduction.tex:10:Training-time methods~\\cite{srpo2025,robustvla2025,digflow2025,liu2026ttvla} improve the base policy through robustness-aware objectives or test-time RL, but require retraining and remain bounded by the training distribution.\nintroduction.tex:11:Inference-time methods leave the policy frozen: ReconVLA~\\cite{chen2026reconvla} provides uncertainty quantification but does not learn corrective residuals; A2C2~\\cite{a2c2_2025} trains a per-step correction head on action chunks but applies correction unconditionally without adaptive compute allocation; VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization at 2.41\\,s per control step.\nintroduction.tex:19:Unlike LLM test-time compute scaling~\\cite{snell2024scaling} where selection is primary, here the $K{=}2$ probe provides a centered starting point and uncertainty gate for learned correction.",
    "numLines": 21
  }
}
```

</details>

---


### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Bash · `toolu_01Avo9C2kXyPGQduoGyEYmoZ`</summary>

```json
{
  "command": "python3 -c \"\nimport re, os\ntexs = ['main.tex','abstract.tex','introduction.tex','related_work.tex','method.tex','experiments.tex','discussion.tex','appendix.tex']\ncited = set()\nfor f in texs:\n    txt = open(f).read()\n    for m in re.findall(r'\\\\\\\\cite\\{([^}]+)\\}', txt):\n        for k in m.split(','):\n            cited.add(k.strip())\nprint('Cited keys:', len(cited))\nbib = open('references.bib').read()\ndefs = set(re.findall(r'@[a-zA-Z]+\\{([^,]+),', bib))\nprint('Bib keys:', len(defs))\nmissing = cited - defs\nunused = defs - cited\nprint('Missing in bib:', missing)\nprint('Unused in bib:', unused)\n\"",
  "description": "Verify cite vs bib coverage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "5c72ff75-abd6-4e86-a886-ecb51fa40f23",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016UEEFQpgGiAXNVc8V9e77d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2994,
      "cache_read_input_tokens": 108864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2994
      },
      "output_tokens": 47,
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

_source line 78 · 2026-05-21T16:39:56.133Z_

<details><summary>↩ Tool result · `toolu_01Avo9C2kXyPGQduoGyEYmoZ`</summary>

```text
Cited keys: 31
Bib keys: 31
Missing in bib: set()
Unused in bib: set()
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "2483a327-76c8-495b-bc2e-feb556dac352",
  "tool_use_result": {
    "stdout": "Cited keys: 31\nBib keys: 31\nMissing in bib: set()\nUnused in bib: set()",
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

_source line 79_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "d3adb0d6-66f6-460e-872d-2168e485a873",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TKjAvUjaFZ8CfmFHp8p2NV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 111858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 418
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


### Tool call

_source line 80_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01GrrD8ZbKz68A1gUw3xm2kw`</summary>

```json
{
  "todos": [
    {
      "content": "Explore paper LaTeX source structure",
      "activeForm": "Exploring paper LaTeX source structure",
      "status": "completed"
    },
    {
      "content": "Attempt compilation and capture warnings/errors",
      "activeForm": "Attempting compilation and capturing warnings/errors",
      "status": "completed"
    },
    {
      "content": "Cross-check numerical claims against registry",
      "activeForm": "Cross-checking numerical claims against registry",
      "status": "in_progress"
    },
    {
      "content": "Audit pi0.5 / OpenVLA section coverage gaps",
      "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps",
      "status": "pending"
    },
    {
      "content": "Verify .bib entries and \\cite{} resolution",
      "activeForm": "Verifying .bib entries and \\cite{} resolution",
      "status": "completed"
    },
    {
      "content": "Write audit report to artifacts and register",
      "activeForm": "Writing audit report to artifacts and registering",
      "status": "pending"
    }
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "42885eb4-41ab-43f2-9d72-43b90d50d212",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TKjAvUjaFZ8CfmFHp8p2NV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 111858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 418
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

_source line 81 · 2026-05-21T16:40:12.774Z_

<details><summary>↩ Tool result · `toolu_01GrrD8ZbKz68A1gUw3xm2kw`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "194e4a3c-55d6-44ba-b89c-afdfad4af52a",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Explore paper LaTeX source structure",
        "status": "completed",
        "activeForm": "Exploring paper LaTeX source structure"
      },
      {
        "content": "Attempt compilation and capture warnings/errors",
        "status": "in_progress",
        "activeForm": "Attempting compilation and capturing warnings/errors"
      },
      {
        "content": "Cross-check numerical claims against registry",
        "status": "pending",
        "activeForm": "Cross-checking numerical claims against registry"
      },
      {
        "content": "Audit pi0.5 / OpenVLA section coverage gaps",
        "status": "pending",
        "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps"
      },
      {
        "content": "Verify .bib entries and \\cite{} resolution",
        "status": "pending",
        "activeForm": "Verifying .bib entries and \\cite{} resolution"
      },
      {
        "content": "Write audit report to artifacts and register",
        "status": "pending",
        "activeForm": "Writing audit report to artifacts and registering"
      }
    ],
    "newTodos": [
      {
        "content": "Explore paper LaTeX source structure",
        "status": "completed",
        "activeForm": "Exploring paper LaTeX source structure"
      },
      {
        "content": "Attempt compilation and capture warnings/errors",
        "status": "completed",
        "activeForm": "Attempting compilation and capturing warnings/errors"
      },
      {
        "content": "Cross-check numerical claims against registry",
        "status": "in_progress",
        "activeForm": "Cross-checking numerical claims against registry"
      },
      {
        "content": "Audit pi0.5 / OpenVLA section coverage gaps",
        "status": "pending",
        "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps"
      },
      {
        "content": "Verify .bib entries and \\cite{} resolution",
        "status": "completed",
        "activeForm": "Verifying .bib entries and \\cite{} resolution"
      },
      {
        "content": "Write audit report to artifacts and register",
        "status": "pending",
        "activeForm": "Writing audit report to artifacts and registering"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014HbCduHAL5GaiewQ6xiwue`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "DONE"
  },
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "b090d719-2bc1-43aa-93d3-2f0cd9fff511",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VjvQw3BqTp8F9gXZNtLMAb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 112276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1227
      },
      "output_tokens": 45,
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

_source line 83 · 2026-05-21T16:40:18.125Z_

<details><summary>↩ Tool result · `toolu_014HbCduHAL5GaiewQ6xiwue`</summary>

```text
Error: result (286,038 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "16eda5c3-dae2-44fa-94e5-d53ffc87629a",
  "tool_use_result": {
    "content": "Error: result (286,038 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:51:32.435Z\", \"updated_at\": \"2026-05-21T12:22:59.643Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed45 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.85, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:52:36.820Z\", \"updated_at\": \"2026-05-21T12:22:49.675Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed43 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.83, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:52:32.595Z\", \"updated_at\": \"2026-05-21T12:22:43.339Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed42 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.845, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:52:27.418Z\", \"updated_at\": \"2026-05-21T12:22:38.751Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.81, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:52:22.502Z\", \"updated_at\": \"2026-05-21T12:22:31.438Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.815, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:52:16.887Z\", \"updated_at\": \"2026-05-21T12:22:24.249Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.82, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-spatial-obs-only-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T07:09:30.589Z\", \"updated_at\": \"2026-05-21T11:50:52.186Z\", \"hypothesis\": \"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\", \"notes\": \"Cron false-positive: marked failed but actually completed successfully. Overall SR 34.0% (34/100) on LIBERO-Spatial with crm_obs_only mode (K=10, max_correction_norm=0.2). Output: /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json. Per-task: between_plate_ramekin=90%, next_to_ramekin=90%, table_center=0%, on_cookie_box=40%, in_top_drawer=10%, on_ramekin=0%, next_to_cookie_box=80%, on_stove=0%, next_to_plate=30%, on_wooden_cabinet=0%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.34, \"per_task_sr\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10}}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:19.985Z\", \"updated_at\": \"2026-05-21T11:50:10.568Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:17.435Z\", \"updated_at\": \"2026-05-21T11:49:59.821Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:14.823Z\", \"updated_at\": \"2026-05-21T11:49:55.157Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"failed\", \"notes\": \"ANOMALY: 0% SR (0/200) across all 10 tasks. Prior quick verify on bjb2-40593 showed 72% (50 rollouts) with identical code/model/deps. Code, model weights (7.47GB), normalizer files, torch 2.10.0+cu128, lerobot 0.5.2, transformers 5.8.0 all verified identical between servers. SmolVLA works fine on bjb1-32546 (12% vla_only). Root cause unknown — possible GPU arch bfloat16 difference or hidden env issue. NEEDS RE-RUN ON bjb2-40593.\"}, \"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:27.768Z\", \"updated_at\": \"2026-05-21T11:46:53.337Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM\", \"conclusion\": \"failed\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:25.180Z\", \"updated_at\": \"2026-05-21T11:46:50.878Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed43, cross-VLA validation of CRM\", \"conclusion\": \"failed\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:22.540Z\", \"updated_at\": \"2026-05-21T11:46:42.183Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed42, cross-VLA validation of CRM\", \"conclusion\": \"failed\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Stdout buffering may hide further progress. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T07:30:47.255Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T07:30:42.676Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T07:30:37.114Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\", \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T07:30:32.202Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\", \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:50:21.016Z\", \"updated_at\": \"2026-05-21T05:22:58.984Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:31.173Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}, \"notes\": \"[2026-05-21] 成功完成全部 10 task × 20 rollouts = 200。SR=11.5% (23/200)。Log: /root/autodl-tmp/logs/norm003_seed66.log (bjb1-18228, PID 642428, cuda:0)\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:00.886Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:13:12.047Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"notes\": \"[2026-05-21 修正] 之前的\\\"task 9/10 异常退出\\\"判断错误。实际进程跑完了全部 10 个 task (20 rollouts each, 共 200)，JSON 已生成: logs/eval_object_crm_obs_only_norm0.05_seed66.json。SR=11.0% (22/200)。原 conclusion=failed 已修正为 success。Log: /root/autodl-tmp/logs/norm005_seed66.log (bjb1-18228)。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T05:10:29.526Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-21T05:07:12.893Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:31:55.966Z\", \"updated_at\": \"2026-05-21T05:07:10.342Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether more candidates improve CRM selection quality.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:33:50.688Z\", \"updated_at\": \"2026-05-21T05:07:08.046Z\", \"hypothesis\": \"K=20 sweep for obs_only CRM on LIBERO-Object seed42 (plan_601). Testing whether doubling K from 10 to 20 further improves correction quality.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:47:49.745Z\", \"updated_at\": \"2026-05-21T05:07:05.713Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed44. K-value sweep third seed (plan_601): tests K=20 vs K=10 compute tradeoff.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:02:49.893Z\", \"updated_at\": \"2026-05-21T05:07:03.314Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed42. K-value sweep (plan_601): tests whether increasing from K=10 to K=20 further improves SR, justifying K=10 as compute-efficient choice.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:45:08.378Z\", \"updated_at\": \"2026-05-21T04:55:07.524Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed53. Multi-seed robustness for magnitude curve plan_500.\"}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:16.022Z\", \"updated_at\": \"2026-05-21T04:55:05.083Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed52. Multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:31:57.442Z\", \"updated_at\": \"2026-05-21T04:55:02.734Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed51. Expanding Object CRM seed coverage.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.17}, \"notes\": \"Cron false positive: 实验正常完成但无 W&B/sentinel 被误判 failed。实际 SR=17% (17/100)，与 obs_only norm02 均值 (16.8%±1.8%) 一致。新增第 7 个 seed 数据点。\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:07:41.505Z\", \"updated_at\": \"2026-05-21T04:55:00.434Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50. Expanding Object CRM norm02 from n=7 to n=8 for seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:33:11.557Z\", \"updated_at\": \"2026-05-21T04:54:57.990Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attempt. Supplements primary result (seed42-47 done, this extends to seed48).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:32:40.226Z\", \"updated_at\": \"2026-05-21T04:54:54.506Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthens pooled significance for Narrative A transition.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T16:04:31.207Z\", \"updated_at\": \"2026-05-21T04:54:51.647Z\", \"hypothesis\": \"obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argmin seed46=10% 配对）。ε=0.2 是 obs_only 最优区间，seed42=22%。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:44:19.258Z\", \"updated_at\": \"2026-05-21T04:54:44.901Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"hypothesis\": \"obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR range consistent with seeds 42-44, it confirms the method's reliability across random seeds and strengthens pooled statistical test vs argmin.\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:32:15.187Z\", \"updated_at\": \"2026-05-21T04:54:42.439Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:48:21.840Z\", \"updated_at\": \"2026-05-21T04:54:39.963Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Object seed43, retry 3. Prior attempts failed. Filling seed gap for Object CRM to balance seed count with other configs.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"notes\": \"Partial result: killed at task 8/10 but SR=16% consistent with norm02 mean (16.8%). Reclassified from failed to success per Director instruction.\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:58:27.783Z\", \"updated_at\": \"2026-05-21T04:54:37.451Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 pooled to 200 trials. Original crashed after 1 task.\", \"parent\": \"eval-obs-only-object-norm02-seed43\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:50:15.572Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}, \"notes\": \"监控误报为 failed。实际正常完成 SR=10.0% (10/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.05_seed67.json (bjb1-32546，注意保存在 /root/logs/ 而非项目 logs/)。日志: /root/autodl-tmp/logs/norm005_seed67.log。\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:49:55.438Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed67, norm sweep statistical robustness\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\", \"notes\": \"监控误报进程消失。实际正常完成 SR=14.0% (14/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.1_seed67.json (bjb1-18228，注意保存在 /root/logs/ 而非项目 logs/)。进程在完成后自然退出，非异常终止。\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-21T04:48:32.810Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Expanding VLA-only seed coverage for seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-21T04:48:27.282Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\", \"notes\": \"Experiment completed successfully but stuck in ANALYZING >24h. Manual resolution on 2026-05-21: JSON output confirmed complete (10 tasks × 10 rollouts = 100 total). Overall SR=10%. Per-task SR range: 0.0-0.2.\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:31.390Z\", \"updated_at\": \"2026-05-21T04:48:15.442Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48. Expanding VLA-only baseline seed count for balanced comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:31:32.794Z\", \"updated_at\": \"2026-05-21T04:48:05.210Z\", \"hypothesis\": \"VLA-only baseline seed46 on LIBERO-Object. 第 5 个 VLA-only seed 补全 baseline。\", \"metrics\": {\"overall_success_rate\": 0.13}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:34:53.953Z\", \"updated_at\": \"2026-05-21T04:47:51.213Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}, \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=45 provides second additional seed for baseline variance estimation — multi-seed baselines required for statistical significance claims in paper\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:33:13.916Z\", \"updated_at\": \"2026-05-21T04:47:46.335Z\", \"hypothesis\": \"Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:32:49.074Z\", \"updated_at\": \"2026-05-21T04:47:42.399Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:50:14.071Z\", \"updated_at\": \"2026-05-21T04:47:36.667Z\", \"metrics\": {\"overall_success_rate\": 0.12}, \"conclusion\": \"success\", \"notes\": \"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=43 establishes multi-seed baseline variance — needed to determine if ACR improvements are statistically significant above baseline noise\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:54:57.323Z\", \"updated_at\": \"2026-05-21T04:47:19.616Z\", \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:15.856Z\", \"updated_at\": \"2026-05-21T04:46:30.740Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"total_rollouts\": 100, \"total_successes\": 35, \"mean_uncertainty\": 0.2619, \"trigger_rate\": 0.98}, \"notes\": \"Cron false positive — 实际正常完成 SR=35.0% (35/100), trigger_rate=98.0%, mean_unc=0.2619。日志在 bjb1-32546。已手动修正。\"}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:37:28.279Z\", \"updated_at\": \"2026-05-21T04:45:27.640Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:13.764Z\", \"updated_at\": \"2026-05-21T04:44:12.088Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"total_rollouts\": 100, \"total_successes\": 34, \"mean_uncertainty\": 0.2679, \"trigger_rate\": 0.976}, \"notes\": \"Cron false positive — 实际正常完成 SR=34.0% (34/100), trigger_rate=97.6%, mean_unc=0.2679。日志在 bjb1-32546。已手动修正。\"}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:17.907Z\", \"updated_at\": \"2026-05-21T04:42:43.669Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"sr_pct\": \"36.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.2661, \"trigger_rate\": 0.978}}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:32:51.140Z\", \"updated_at\": \"2026-05-21T04:42:32.790Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:25:56.030Z\", \"updated_at\": \"2026-05-21T04:34:43.303Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed44. Third seed for Random Selection Object baseline.\", \"notes\": \"Random selection baseline seed44 完成。SR=0.11, 10 tasks × 10 rollouts = 100 total。三个 seed 汇总: seed43=0.09, seed44=0.11, seed45=0.10, 均值≈0.10。与 VLA-only baseline 相当，确认 random selection 无法有效利用 K=10 candidates。\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:10:52.130Z\", \"updated_at\": \"2026-05-21T04:34:38.177Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed43. Second seed for Random Selection Object baseline.\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T04:01:22.020Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed60. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"source\": \"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\"}}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:50:00.000Z\", \"updated_at\": \"2026-05-21T03:59:27.286Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\", \"notes\": \"PID 802634(旧)→802639(旧,killed)→811006(r2,MEAN_STD fix). Dual process conflict resolved. Monitoring until task 5.\", \"conclusion\": \"failed\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:33.689Z\", \"updated_at\": \"2026-05-21T03:30:13.218Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed54. Norm sweep: filling ε=0.1 gap, bringing n to 7+.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:31.269Z\", \"updated_at\": \"2026-05-21T03:30:10.368Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed53. Norm sweep: filling ε=0.1 gap, bringing n to 6+.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:23.747Z\", \"updated_at\": \"2026-05-21T03:30:07.112Z\", \"conclusion\": \"success\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed52. Norm sweep: filling ε=0.1 gap (ROADMAP TBD), bringing n from 3 to 5+.\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判。已手动修正。\"}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:45:04.127Z\", \"updated_at\": \"2026-05-21T03:30:04.361Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:20.171Z\", \"updated_at\": \"2026-05-21T03:29:59.855Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed49. Low-norm data point for plan_500.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:02:39.518Z\", \"updated_at\": \"2026-05-21T03:29:57.231Z\", \"hypothesis\": \"CRM obs_only with ε=0.1 and K=10 on LIBERO-Object seed48. Low-norm data point for plan_500 magnitude curve, strengthening Figure 2 error bars at small ε.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-21T03:29:54.309Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"overall_success_rate\": 0.17}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:51.040Z\", \"updated_at\": \"2026-05-21T03:29:47.720Z\", \"hypothesis\": \"obs_only CRM ε=0.1 seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=14%)，需标准化到 n_rollouts=10 与其他 seed 一致。当前 obs_only ε=0.1 有 5 seeds。\", \"parent\": \"eval-obs-only-object-norm01-seed45\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:12:01.937Z\", \"updated_at\": \"2026-05-21T03:29:43.639Z\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\", \"hypothesis\": \"Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, confirming that performance gains are robust across random seeds and not artifacts of a single initialization\", \"parent\": \"eval-acr-object-obs-only-norm02\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:23:01.005Z\", \"updated_at\": \"2026-05-21T03:29:41.343Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed55. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。\"}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:35.665Z\", \"updated_at\": \"2026-05-21T03:29:39.045Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed50. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:27.458Z\", \"updated_at\": \"2026-05-21T03:29:36.190Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed49. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。日志在 bjb1-32546。\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:19.347Z\", \"updated_at\": \"2026-05-21T03:29:30.312Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed48. Low-norm data point for plan_500.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:14:06.226Z\", \"updated_at\": \"2026-05-21T03:29:23.229Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\", \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-21T03:29:16.871Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:27.742Z\", \"updated_at\": \"2026-05-21T03:29:14.257Z\", \"hypothesis\": \"obs_only CRM with ε=0.05 on LIBERO-Object seed43. Retry (r2) for magnitude curve low-norm data point.\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:15.980Z\", \"updated_at\": \"2026-05-21T03:29:10.509Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"notes\": \"Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and r3 (bjb1-18228)\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:56:04.999Z\", \"updated_at\": \"2026-05-21T03:29:06.231Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed48 on LIBERO-Object. 新 seed, 16h timeout。C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM 确认 — PID 67825 在 bjb1-18228 GPU 1 正常运行中。已完成 5/10 tasks + T6 进行中 (T1=0%, T2=0%, T3=20%, T4=40%, T5=0%, T6 doing 5/10=1/5)。conclusion=failed 为误标(cron 误报)，无法设 null。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:56:02.708Z\", \"updated_at\": \"2026-05-21T03:29:02.399Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. Retry with 16h timeout (r1 killed on bjb1-18228). C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM — cron 检测到旧进程 EXIT_CODE=129(被 kill 的重复进程 PID 892663)，误标为 failed。实际进程 PID 894900 仍在 bjb1-32546 GPU 3 正常运行，5/10 tasks 完成 (T1=0%, T2=0%, T3=20%, T4=30%, T5=0%)。已恢复 RUNNING。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:50:34.507Z\", \"updated_at\": \"2026-05-21T03:28:57.483Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed46. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive: 实验正常完成 SR=15.0%, JSON 已写入。进程退出后 cron 无 sentinel/W&B 标记 → 误判 failed。已修正 conclusion=success。\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:16:07.852Z\", \"updated_at\": \"2026-05-21T03:28:51.768Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1，seed43/44 已在跑。第 4 个 seed 确保极低 norm 端有可靠 error bars。\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:09:01.117Z\", \"updated_at\": \"2026-05-21T03:28:48.787Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed44 on LIBERO-Object (bjb2-28827). 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)。另一份 seed44 在 bjb1-32546 同时运行。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 21:00 UTC: 实验实际成功完成。JSON 输出在 /root/logs/eval_object_obs_only_norm003_seed44.json (注意：路径是 /root/logs/ 而非 /root/acr-vla-conformal-refinement/logs/)。10/10 tasks 全部完成，overall SR=17% (17/100)。误标 failed 原因：startup recovery 发现 RUNNING 状态无 cron 监控和 PID 信息，自动标记为 failed。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:15:11.377Z\", \"updated_at\": \"2026-05-21T03:28:46.427Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:45:20.860Z\", \"updated_at\": \"2026-05-21T03:28:43.998Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"parent\": \"eval-obs-only-object-norm003-seed43\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-21T03:28:41.514Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"Cron false positive (日志路径不匹配)。实际正常完成 SR=14% (14/100)。norm003 magnitude curve 数据点，在 VLA-only (10.9%) 和 norm02 (16.8%) 之间。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:14:50.423Z\", \"updated_at\": \"2026-05-21T03:19:50.462Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed57. Norm sweep: additional ε=0.1 data point.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=19.0%。\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:19:48.034Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive confirmed. Output JSON 已存在 (1490 bytes)，日志显示正常完成。Overall SR=14.0% (14/100)。进程已退出，无异常。\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:00:59.021Z\", \"updated_at\": \"2026-05-21T03:19:45.881Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive（第N次）：eval 脚本正常完成但不写 sentinel/W&B，被 cron 误判 failed。实际 SR=15.0% (15/100)。手动修正 conclusion=success。\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.05 (ε=0.05) on LIBERO-Object seed61 provides consistent improvement over VLA-only baseline, contributing to norm sweep statistical robustness for the ε=0.05 condition.\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:18:18.450Z\", \"updated_at\": \"2026-05-21T03:19:43.346Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed58. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=16.0%。\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:25:26.898Z\", \"updated_at\": \"2026-05-21T03:19:41.023Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed59. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=13.0%。\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:28:30.000Z\", \"updated_at\": \"2026-05-21T03:19:38.737Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed56. Norm sweep seed balance for ε=0.03.\"}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T03:13:18.900Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed75. Norm sweep seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T03:13:14.621Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed74. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T03:13:06.825Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed72. Norm sweep seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:41:28.765Z\", \"updated_at\": \"2026-05-21T03:13:03.208Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63 r2. Redo after python PATH failure on bjb1-32546. Norm sweep seed balance for ε=0.03.\", \"parent\": \"eval-obs-only-object-norm003-seed63\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T03:12:59.417Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed71. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:41:26.296Z\", \"updated_at\": \"2026-05-21T03:12:55.649Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62 r2. Redo after python PATH failure on bjb1-32546. Norm sweep seed balance for ε=0.03.\", \"parent\": \"eval-obs-only-object-norm003-seed62\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T03:12:20.827Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed73. Norm sweep seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:41:19.545Z\", \"updated_at\": \"2026-05-21T03:11:43.996Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed51 r3. Redo after python PATH failure on bjb1-32546. Norm sweep: filling ε=0.1 gap.\", \"parent\": \"eval-obs-only-object-norm01-seed51-r2\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11}}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:41:23.364Z\", \"updated_at\": \"2026-05-21T03:10:52.558Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed52 r3. Redo after python PATH failure on bjb1-32546. Norm sweep: filling ε=0.1 gap.\", \"parent\": \"eval-obs-only-object-norm01-seed52-r2\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:10:27.996Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed65. Norm sweep filling ε=0.1 gap.\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:10:08.688Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed64. Norm sweep filling ε=0.1 gap (ROADMAP TBD).\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:09:32.235Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed64. Norm sweep seed balance for ε=0.05.\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:08:52.713Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.03.\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:05:28.591Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed64. Norm sweep seed balance for ε=0.03 (expanding from 3 to 5 seeds).\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T01:15:11.709Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed62. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 同 seed61/seed63,进程在 task1 rollout 5/10 时静默退出。bjb2-28827 SIGHUP 批量故障。已被 seed71-75 替代。\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T01:14:56.556Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed63. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 同 seed61/seed62,进程在 task1 rollout 5/10 时静默退出。bjb2-28827 SIGHUP 批量故障。已被 seed71-75 替代。\"}, \"eval-obs-only-object-norm01-seed61\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T01:14:51.727Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed61. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 进程在 task1 rollout 5/10 时静默退出,无 Traceback/OOM/CUDA error。日志仅 14 行。与 bjb2-28827 历史 SIGHUP 模式一致(tmux/SSH 断连导致信号杀死进程)。同时失败: seed62, seed63。已被 seed71-75 替代,无需重跑。\"}, \"eval-obs-only-object-norm003-seed64-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T00:54:21.580Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed64. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed63\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:36:29.353Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"failed\", \"notes\": \"Real failure: nohup: failed to run command 'python': No such file or directory. bjb1-32546 没有 python 在 PATH 中，需用 /root/miniconda3/bin/python。需重跑。\"}, \"eval-obs-only-object-norm003-seed62\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:36:21.900Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62. Norm sweep seed balance for ε=0.03 (only 3 seeds, need more for reliable mean±std).\", \"conclusion\": \"failed\", \"notes\": \"Real failure: nohup: failed to run command 'python': No such file or directory. bjb1-32546 没有 python 在 PATH 中，需用 /root/miniconda3/bin/python。需重跑。\"}, \"eval-obs-only-object-norm01-seed51-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:36:16.959Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed51 r2. Redo of crashed seed51 (process dead, no JSON). Norm sweep: filling ε=0.1 gap.\", \"parent\": \"eval-obs-only-object-norm01-seed51\", \"conclusion\": \"failed\", \"notes\": \"Real failure: nohup: failed to run command 'python': No such file or directory. bjb1-32546 没有 python 在 PATH 中，需用 /root/miniconda3/bin/python。需重跑。\"}, \"eval-obs-only-object-norm01-seed52-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:36:12.707Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed52 r2. Redo of crashed seed52 (process dead, no JSON). Norm sweep: filling ε=0.1 gap.\", \"parent\": \"eval-obs-only-object-norm01-seed52\", \"conclusion\": \"failed\", \"notes\": \"Real failure: nohup: failed to run command 'python': No such file or directory. bjb1-32546 没有 python 在 PATH 中，需用 /root/miniconda3/bin/python。需重跑。\"}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:19.933Z\", \"updated_at\": \"2026-05-21T00:18:47.313Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed51. Norm sweep: filling ε=0.1 gap (ROADMAP TBD), bringing n from 3 to 4+.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"total_successes\": 11}, \"notes\": \"Cron false positive — 实际正常完成 SR=11.0% (11/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。\"}, \"eval-obs-only-object-norm005-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:13:00.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed49 r2. Redo of crashed seed49 (process dead, no JSON). Norm sweep seed balance.\", \"parent\": \"eval-obs-only-object-norm005-seed49\"}, \"eval-obs-only-object-norm005-seed55-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:13:00.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed55 r2. Redo of crashed seed55 (process dead, no JSON). Norm sweep seed balance.\", \"parent\": \"eval-obs-only-object-norm005-seed55\"}, \"eval-openvla-crm-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:32:47.109Z\", \"updated_at\": \"2026-05-20T23:28:23.498Z\", \"hypothesis\": \"OpenVLA CRM obs_only eval: 测试 CRM correction 在 OpenVLA (7B, near-deterministic T=0.5) 上的效果。OpenVLA v2 baseline=69%，但 T=0.5 产生近乎相同的 actions (8/10 identical)。关键问题：CRM correction 在低 action diversity 条件下是否仍有效？解决 3 个 review criticals: M1 narrow scope, R2-W1-new low absolute perf, R1-W3-new single VLA。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0, \"sr_pct\": \"0.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:27:35.885Z\", \"updated_at\": \"2026-05-20T22:28:30.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed44 retry2. Norm sweep ε=0.03 data point.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": \"15.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:13.937Z\", \"updated_at\": \"2026-05-20T22:21:32.888Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Object seed49. Seed balance for plan_600.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:36:46.646Z\", \"updated_at\": \"2026-05-20T22:20:24.412Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Object seed48. Expanding random selection seed coverage for seed balance (plan_600, target n≥5).\", \"metrics\": {\"success_rate\": 0.1, \"sr_pct\": \"10.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:19:08.706Z\", \"updated_at\": \"2026-05-20T22:04:37.390Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:18.108Z\", \"updated_at\": \"2026-05-20T21:59:15.550Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Spatial seed52. Multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-seed54\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:45:26.024Z\", \"updated_at\": \"2026-05-20T21:32:35.788Z\", \"conclusion\": \"killed\", \"notes\": \"Killed to free GPU for P0 OpenVLA CRM eval. norm=0.2 已有 7+ seeds，边际价值低。\"}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:00:46.028Z\", \"updated_at\": \"2026-05-20T21:16:27.264Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:00:42.469Z\", \"updated_at\": \"2026-05-20T21:16:23.354Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:00:39.505Z\", \"updated_at\": \"2026-05-20T21:16:19.344Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"conclusion\": \"killed\"}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:18:59.700Z\", \"updated_at\": \"2026-05-20T19:42:34.465Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed42. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.14, \"mean_l2\": 0, \"avg_k\": 1, \"fast_path_pct\": 0.12, \"n_rollouts\": 10}, \"notes\": \"Cron false positive (日志路径不匹配)。实际正常完成 SR=14%。avg_k=1.0 说明 head 几乎不触发 full-K escalation。低于 GO 阈值 15%。\"}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:19:04.464Z\", \"updated_at\": \"2026-05-20T19:38:46.967Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed43. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.11, \"n_rollouts\": 100, \"fast_path_pct\": 12.5, \"avg_k\": 1}, \"notes\": \"Cron false positive (日志路径不匹配)。实际正常完成 SR=11%。avg_k=1.0，head 不触发 full-K。低于 GO 阈值 15%，支持 D090 NO-GO 结论。\"}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:31:51.325Z\", \"updated_at\": \"2026-05-20T19:34:40.308Z\", \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed50. Additional perdof seed for multi-seed robustness.\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.1, \"n_rollouts\": 100, \"per_task\": [0, 0, 1, 1, 0, 1, 1, 0, 4, 2]}, \"notes\": \"Cron false positive: 实验正常完成但无 W&B/sentinel 被误判 failed。实际 SR=10% (10/100)，与 VLA-only baseline (10.9%) 持平，perdof CRM 无改进。\"}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T16:52:03.117Z\", \"updated_at\": \"2026-05-20T19:21:50.874Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed44. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"avg_K\": 1, \"adaptive_trigger_rate\": 0, \"crm_trigger_rate\": 0.8795, \"unc_threshold\": 0.42}, \"conclusion\": \"negative\"}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:30:38.520Z\", \"updated_at\": \"2026-05-20T19:18:36.706Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Spatial seed42. Third attempt after prior kills.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total_rollouts\": 100}, \"notes\": \"Cron false positive — eval 实际完成，SR=34% (34/100)。与之前 seed42=34% 一致。Random Selection Spatial 三 seeds: 34%, 26%, 28%。\"}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:31:49.315Z\", \"updated_at\": \"2026-05-20T19:18:34.577Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Spatial seed50. Additional spatial seed for multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"successes\": 35, \"total_rollouts\": 100}, \"notes\": \"Cron false positive — eval 实际完成，SR=35% (35/100)。日志在项目目录下而非 ~/runs/，导致 cron 找不到 sentinel。\"}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:47:46.067Z\", \"updated_at\": \"2026-05-20T19:18:14.214Z\", \"hypothesis\": \"Training CRM obs_only model on OpenVLA features (obs_dim=4096) to enable backbone-agnostic conformal refinement. If successful, CRM can improve any VLA backbone, resolving review critical C3 (single VLA limitation).\", \"parent\": \"openvla-precompute-k1\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.07726, \"final_train_loss\": 0.234989, \"epochs_completed\": 50}, \"notes\": \"Cron false positive — 训练实际完成 50/50 epochs, best val_loss=0.077260. Checkpoint at /root/autodl-tmp/checkpoints/crm_openvla_obs_only/. 无 W&B/sentinel 导致 cron 误判。\"}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:49:30.105Z\", \"updated_at\": \"2026-05-20T18:37:09.326Z\", \"hypothesis\": \"Precomputing OpenVLA hidden features at quartile layers [7,15,23,31] will produce multi-scale representations (4×4096) compatible with the CRM K=1 training pipeline, enabling backbone-agnostic conformal refinement.\", \"conclusion\": \"success\", \"metrics\": {\"total_files\": 74507, \"obs_dim\": 4096, \"cache_size_gb\": 6, \"multi_scale_layers\": [7, 15, 23, 31]}}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:36:03.819Z\", \"updated_at\": \"2026-05-20T17:36:15.098Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Third attempt on bjb1-18228 with updated code.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"tasks_evaluated\": 10, \"rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 10}}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:56:54.460Z\", \"updated_at\": \"2026-05-20T17:31:38.771Z\", \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed49. Testing per-DOF correction architecture for multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"seed\": 49, \"K\": 10, \"max_correction_norm\": 0.2}}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:34:01.591Z\", \"updated_at\": \"2026-05-20T17:30:04.397Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed47 (plan_600). Additional seed for random baseline multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 7}}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:31:34.419Z\", \"updated_at\": \"2026-05-20T17:28:06.990Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Spatial seed42, retry 2. Prior run killed mid-evaluation. Re-run to fill missing seed42 Spatial CRM data point.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33}}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:31:47.920Z\", \"updated_at\": \"2026-05-20T17:22:56.685Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether fewer candidates degrade performance.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 17}}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:35:38.150Z\", \"updated_at\": \"2026-05-20T17:21:49.990Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Spatial seed43 re-run (plan_600). Fresh run on bjb1-18228 for additional baseline data point.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 26}}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:47:57.755Z\", \"updated_at\": \"2026-05-20T17:20:57.101Z\", \"hypothesis\": \"Random selection baseline (K=10, uniform random) on LIBERO-Spatial seed44. Tests whether random action selection ≈ VLA-only, confirming CRM guidance is the source of improvement.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.28, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:50:02.848Z\", \"updated_at\": \"2026-05-20T16:58:33.591Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed43 for plan_702. Third attempt (M032).\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:50:00.848Z\", \"updated_at\": \"2026-05-20T16:58:27.648Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed42 for plan_702. Third attempt after unc_dim bugfix + exit file cleanup (M032).\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:50:04.763Z\", \"updated_at\": \"2026-05-20T16:50:59.250Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed44 for plan_702. Third attempt (M032).\", \"metrics\": {\"sr\": 10, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:42:56.456Z\", \"updated_at\": \"2026-05-20T15:35:34.584Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Retry after code fix - additional seed for random baseline comparison.\", \"conclusion\": \"failed\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:47:52.915Z\", \"updated_at\": \"2026-05-20T15:34:05.777Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Spatial seed43 (plan_600). Additional spatial seed for random baseline to compare against CRM selection on ID suite.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.26, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"stove\": 0, \"next_to_plate\": 0.2, \"wooden_cabinet\": 0}}}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:50:36.635Z\", \"updated_at\": \"2026-05-20T15:33:54.594Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Additional seed for random baseline to establish statistical comparison against CRM selection.\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:32:05.973Z\", \"updated_at\": \"2026-05-20T15:33:15.181Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed48. Additional seed for Spatial CRM multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.35, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:48.207Z\", \"updated_at\": \"2026-05-20T15:32:12.693Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed48. Additional seed for VLA-only multi-seed baseline comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:49:20.087Z\", \"updated_at\": \"2026-05-20T15:19:37.689Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Spatial seed42. Filling missing seed42 for Spatial CRM to balance seed coverage across configs.\", \"metrics\": {\"status_note\": \"INCOMPLETE - only 2/10 tasks evaluated before process terminated\", \"partial_per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 1}, \"tasks_completed\": 2, \"tasks_total\": 10}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:27:10.816Z\", \"updated_at\": \"2026-05-20T15:19:01.383Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed49. Additional Spatial CRM seed for multi-seed robustness.\", \"metrics\": {\"sr\": 0.32, \"sr_pct\": \"32%\", \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"on_cookie_box\": 0.3, \"top_drawer_cabinet\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:06:33.103Z\", \"updated_at\": \"2026-05-20T15:17:24.944Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"metrics\": {\"success_rate\": 0.36, \"avg_K\": 3.56, \"fast_path_ratio\": 0.805, \"adaptive_trigger_rate\": 0.195, \"total_rollouts\": 100, \"successes\": 36, \"total_steps\": 23123, \"fast_steps\": 18615, \"full_steps\": 4508, \"threshold\": 0.12587, \"mean_l2_distance\": 0.09, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 0.8, \"successes\": 8, \"total\": 10}, \"next_to_ramekin\": {\"sr\": 1, \"successes\": 10, \"total\": 10}, \"from_table_center\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"on_cookie_box\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"in_top_drawer\": {\"sr\": 0.1, \"successes\": 1, \"total\": 10}, \"on_ramekin\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_cookie_box\": {\"sr\": 0.9, \"successes\": 9, \"total\": 10}, \"on_stove\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_plate\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"on_wooden_cabinet\": {\"sr\": 0, \"successes\": 0, \"total\": 10}}}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:07:43.376Z\", \"updated_at\": \"2026-05-20T15:05:10.161Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) on LIBERO-Object seed50. Additional seed for balanced Argmin vs CRM comparison.\", \"metrics\": {\"overall_sr\": 0.13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}, \"total_rollouts\": 100, \"total_successes\": 13, \"seed\": 50, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:08:11.387Z\", \"updated_at\": \"2026-05-20T14:59:00.735Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48 re-run. Prior run (sr=0.1) had process death issues. Redeploy for reliable VLA-only baseline data.\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"successes\": 11, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T05:16:21.107Z\", \"updated_at\": \"2026-05-20T14:58:56.897Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed51. Paired baseline for CRM obs_only Goal seed51 (SR=66%) comparison.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 69, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:06:37.026Z\", \"updated_at\": \"2026-05-20T14:48:09.495Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on Spatial seed42. Redeploy after M030 SIGTERM kill. Completes plan_600 Spatial baseline.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:32.629Z\", \"updated_at\": \"2026-05-20T14:37:22.190Z\", \"hypothesis\": \"Random selection baseline (K=10, uniform random pick) on LIBERO-Object seed45. Controls for sampling diversity vs CRM-guided selection. Plan_600.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-crm-k1-object-seed44-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T14:33:04.339Z\", \"updated_at\": \"2026-05-20T14:34:18.084Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed44 for plan_702. Single VLA forward + CRM correction. Compare to K=1 VLA-only baseline (10.8%). Retry after unc_dim bugfix.\", \"parent\": \"eval-crm-k1-object-seed44-plan702\"}, \"eval-crm-k1-object-seed43-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T14:33:01.973Z\", \"updated_at\": \"2026-05-20T14:34:14.100Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed43 for plan_702. Single VLA forward + CRM correction. Compare to K=1 VLA-only baseline (10.8%). Retry after unc_dim bugfix.\", \"parent\": \"eval-crm-k1-object-seed43-plan702\"}, \"eval-crm-k1-object-seed42-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T14:32:58.117Z\", \"updated_at\": \"2026-05-20T14:34:10.003Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed42 for plan_702. Single VLA forward + CRM correction. Compare to K=1 VLA-only baseline (10.8%). Retry after unc_dim bugfix.\", \"parent\": \"eval-crm-k1-object-seed42-plan702\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:05:24.390Z\", \"updated_at\": \"2026-05-20T14:26:11.524Z\", \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed48. Additional seed for per-DoF CRM magnitude curve at ε=0.2.\", \"metrics\": {\"sr\": 0.07, \"total\": 100, \"successes\": 7, \"benchmark\": \"object\", \"mode\": \"crm_perdof\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:04:51.797Z\", \"updated_at\": \"2026-05-20T14:26:08.978Z\", \"hypothesis\": \"Argmin (reconvla) baseline K=5 on LIBERO-Object seed44, retry 2. Re-run after prior failure for argmin K=5 ablation data.\", \"parent\": \"eval-argmin-object-k5-seed44\", \"metrics\": {\"sr\": 0.11, \"total\": 100, \"successes\": 11, \"benchmark\": \"object\", \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:04:56.660Z\", \"updated_at\": \"2026-05-20T14:26:03.273Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed44, retry 2. Re-run for reliable VLA-only Goal baseline data after prior process death.\", \"parent\": \"eval-vla-only-goal-seed44\", \"metrics\": {\"sr\": 0.73, \"total\": 100, \"successes\": 73, \"benchmark\": \"goal\", \"mode\": \"vla_only\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:04:55.082Z\", \"updated_at\": \"2026-05-20T14:25:59.677Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed46, retry 2. Re-run after prior process death. Tests CRM spatial generalization.\", \"parent\": \"eval-obs-only-spatial-norm02-seed46\", \"metrics\": {\"sr\": 0.33, \"total\": 100, \"successes\": 33, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\"}, \"conclusion\": \"success\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pipeline_latency_ms\": 247, \"crm_latency_ms\": 0.27}, \"created_at\": \"2026-05-20T13:50:06.703Z\", \"updated_at\": \"2026-05-20T13:50:45.112Z\", \"hypothesis\": \"Latency profiling for VLA+CRM pipeline. Measures wall-clock time for K=1/5/10/20 VLA sampling + CRM inference + conformal scoring.\"}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:41.144Z\", \"updated_at\": \"2026-05-20T13:33:48.420Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735, Object-calibrated) on LIBERO-Spatial seed44. Third seed for cross-benchmark P75 threshold sweep. Existing: seed42=31%, seed43=34%. Validates P75 consistency on Spatial.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33, \"avg_k\": 5.054, \"fast_path_pct\": 61.8, \"mean_l2\": 0.092, \"total_rollouts\": 100, \"threshold\": 0.098735}, \"notes\": \"SIGHUP false failure (同 P25-seed44 模式)。全部 100 rollouts 完成, SR=33%。已从 memory.md 恢复 metrics 并修正 conclusion=success。\"}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:48:04.411Z\", \"updated_at\": \"2026-05-20T13:32:36.837Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Goal seed51. Multi-seed supplement to address R2 seed imbalance concern. CRM should outperform VLA-only baseline on Goal OOD.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 66, \"total_rollouts\": 100, \"per_task_sr\": {\"open_middle_drawer\": 40, \"put_bowl_on_stove\": 90, \"put_wine_bottle_on_cabinet\": 50, \"open_top_drawer_put_bowl\": 40, \"put_bowl_on_cabinet\": 80, \"push_plate_to_stove\": 90, \"put_cream_cheese_in_bowl\": 20, \"turn_on_stove\": 100, \"put_bowl_on_plate\": 100, \"put_wine_bottle_on_rack\": 50}}, \"notes\": \"Cron false positive — 日志在 /root/acr-vla-conformal-refinement/logs/ 而非 ~/runs/，cron 找不到日志文件误判为 dead。全部 100 rollouts 完成, SR=66%。手动修正 conclusion=success。Goal OOD 持续 neutral (新 n=7: ~67.7% vs VLA 68.7%)。\"}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:42.913Z\", \"updated_at\": \"2026-05-20T13:31:25.501Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959, Object-calibrated) on LIBERO-Spatial seed44. Third seed for cross-benchmark P25 threshold sweep. Completes Spatial sweep table (P25/P50/P75/P90 × 3 seeds).\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 32, \"avg_k\": 7.693, \"fast_path_pct\": 28.8, \"mean_l2\": 0.0896, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 70, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 40, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}, \"notes\": \"SIGHUP false failure — 全部 100 rollouts 完成, SR=32%, JSON 已保存。EXIT_CODE=129 发生在结果保存之后 (同 P75-seed44 模式)。手动修正 conclusion=success。\"}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:53:24.027Z\", \"updated_at\": \"2026-05-20T13:26:22.725Z\", \"hypothesis\": \"OpenVLA baseline on LIBERO-Object seed42. Tests original OpenVLA performance as reference for SmolVLA-based CRM comparison.\", \"conclusion\": \"killed\", \"notes\": \"失败原因: EXIT_CODE=124 timeout。完成 400/500 episodes (8/10 tasks)，SR=68.0% (272/400)。第9个task (pick_up_milk) 4/50时被kill。每episode ~60s，500 episodes需~8.3h但timeout仅~6h。已有成果: 前8个task数据完整。建议: 加大timeout_hours至12h重跑。\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:49:04.530Z\", \"updated_at\": \"2026-05-20T13:17:52.468Z\", \"hypothesis\": \"Argmin (reconvla) baseline on LIBERO-Object seed49 K=10. Multi-seed supplement to ensure Argmin vs CRM comparison has balanced seed counts.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"total_successes\": 16, \"total_rollouts\": 100, \"seed\": 49, \"benchmark\": \"LIBERO-Object\", \"K\": 10, \"mode\": \"reconvla (argmin baseline)\", \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:48:49.157Z\", \"updated_at\": \"2026-05-20T13:07:28.620Z\", \"hypothesis\": \"Argmin (reconvla) baseline on LIBERO-Object seed48 K=10. Multi-seed supplement to ensure Argmin vs CRM comparison has balanced seed counts.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:14:26.858Z\", \"updated_at\": \"2026-05-20T13:07:16.116Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}, \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed48. Additional seed for Spatial CRM multi-seed robustness.\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:48:11.751Z\", \"updated_at\": \"2026-05-20T13:06:48.437Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Goal seed52. Multi-seed supplement to address R2 seed imbalance concern. CRM should outperform VLA-only baseline on Goal OOD.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.68, \"per_task\": {\"open_middle_drawer\": 0.7, \"bowl_on_stove\": 0.9, \"wine_on_cabinet\": 0.4, \"bowl_in_drawer\": 0.3, \"bowl_on_cabinet\": 0.8, \"plate_to_stove\": 0.8, \"cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"bowl_on_plate\": 1, \"wine_on_rack\": 0.5}}}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:47.376Z\", \"updated_at\": \"2026-05-20T13:06:03.701Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870, Object-calibrated) on LIBERO-Spatial seed43. Second seed for Spatial P90 threshold. Cross-benchmark validation of aggressive compute saving regime.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32, \"avg_K\": 3.586, \"fast_path_pct\": 80.17, \"mean_l2\": 0.0905, \"adaptive_trigger_rate\": 0.198, \"threshold\": 0.12587, \"total_steps\": 23797, \"fast_steps\": 19079, \"full_steps\": 4718}}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:09:08.601Z\", \"updated_at\": \"2026-05-20T13:05:55.751Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。\", \"metrics\": {\"overall_success_rate\": 0.12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:45.262Z\", \"updated_at\": \"2026-05-20T12:54:12.191Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870, Object-calibrated) on LIBERO-Spatial seed42. Most aggressive threshold — on Object P90 gives 93% fast_path but SR drops to 13.3%. Tests whether Spatial follows same pattern: high fast_path with SR penalty.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.31, \"avg_K\": 3.5, \"fast_path_pct\": 80.6, \"mean_l2\": 0.0907, \"threshold\": 0.12587, \"total_rollouts\": 100, \"total_successes\": 31, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"notes\": \"Cron false positive: EXIT_CODE=129 (SIGHUP after completion). 日志确认 10/10 tasks × 10 rollouts 全部完成，JSON 已写出。手动修正 conclusion=success。\"}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:50:37.777Z\", \"updated_at\": \"2026-05-20T12:48:49.975Z\", \"hypothesis\": \"CRM obs_only norm02 (ε=0.2) K=10 on Object seed49. Expanding Object CRM norm02 from n=6 to n=7 for seed balance (R2 concern).\", \"metrics\": {\"overall_success_rate\": 0.14, \"total_rollouts\": 100, \"total_successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"updated_aggregate\": {\"mean_sr\": 16.4, \"std_sr\": 2, \"n_seeds\": 7, \"prior\": \"16.8±1.8% (n=6)\", \"delta_vs_vla_baseline\": \"+5.5pp\"}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:32:24.476Z\", \"updated_at\": \"2026-05-20T12:41:49.447Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed47. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"failed\", \"metrics\": {\"incomplete\": true, \"tasks_completed\": 2, \"tasks_total\": 10, \"partial_results\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9}, \"failure_reason\": \"Process exited after 2/10 tasks; no JSON output generated; likely OOM or early termination\"}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:50.876Z\", \"updated_at\": \"2026-05-20T11:48:28.747Z\", \"hypothesis\": \"Random selection baseline (K=10, pick uniformly at random) on LIBERO-Spatial seed42. On Object, Random K=10 (11.3%) ≈ VLA-only (10.9%), proving CRM guidance is the value. Tests whether same pattern holds on Spatial: if Random ≈ VLA-only (~29.6%), CRM's +5pp is from guidance not sampling diversity.\", \"conclusion\": \"failed\"}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:34:55.742Z\", \"updated_at\": \"2026-05-20T11:30:00.787Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"conclusion\": \"success\", \"notes\": \"审计修正：JSON 完整（10 tasks × 10 rollouts），实验已成功完成。EXIT_CODE=2 为提交命令路径错误（evaluate.py vs src/evaluate.py），但实际运行的进程已正常完成并写出结果。\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:34:52.011Z\", \"updated_at\": \"2026-05-20T11:29:58.029Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"conclusion\": \"success\", \"notes\": \"审计修正：JSON 完整（10 tasks × 10 rollouts），实验已成功完成。EXIT_CODE=2 为提交命令路径错误（evaluate.py vs src/evaluate.py），但实际运行的进程已正常完成并写出结果。\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:01:50.026Z\", \"updated_at\": \"2026-05-20T11:13:15.994Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无 per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark 通用。\", \"notes\": \"Reviewer 三次独立验证确认成功：JSON 完整，SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead + 无 sentinel）。\", \"metrics\": {\"sr\": 30, \"avg_K\": 6.324, \"fast_path_pct\": 45.95, \"mean_l2\": 0.0903, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:02:47.126Z\", \"updated_at\": \"2026-05-20T10:52:54.947Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959, Object-calibrated) on LIBERO-Spatial seed42. Cross-benchmark threshold sweep: P25 keeps ~65% fast-path on Object, testing transfer to Spatial.\", \"metrics\": {\"overall_success_rate\": 0.33, \"avg_K\": 7.65, \"fast_path_pct\": 29.4, \"mean_l2_distance\": 0.0892, \"threshold\": 0.054959, \"total_steps\": 23410, \"fast_steps\": 6873, \"full_steps\": 16537, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:19:55.884Z\", \"updated_at\": \"2026-05-20T10:51:17.226Z\", \"hypothesis\": \"Adaptive K with P25 threshold (τ=0.054959) on LIBERO-Spatial will maintain competitive SR compared to K=10 baseline while reducing average inference cost by using fewer refinement steps when the model is confident.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 30, \"avg_k\": 7.6, \"fast_path_pct\": 29.5, \"mean_l2\": 0.089, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 60, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 30, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:19:53.159Z\", \"updated_at\": \"2026-05-20T10:38:12.906Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735, Object-calibrated) on LIBERO-Spatial seed43. Second seed for cross-benchmark P75 threshold sweep.\", \"metrics\": {\"success_rate\": 34, \"total_rollouts\": 100, \"adaptive_stats\": {\"fast_path_pct\": 62.2, \"avg_k\": 5, \"mean_l2\": 0.0911}, \"per_task\": {\"bowl_between_plate_ramekin\": 80, \"bowl_next_to_ramekin\": 100, \"bowl_from_table_center\": 0, \"bowl_on_cookie_box\": 40, \"bowl_in_top_drawer\": 0, \"bowl_on_ramekin\": 0, \"bowl_next_to_cookie_box\": 90, \"bowl_on_stove\": 0, \"bowl_next_to_plate\": 30, \"bowl_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:19:57.817Z\", \"updated_at\": \"2026-05-20T10:36:14.773Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed43. K-value sweep second seed (plan_601): tests K=20 vs K=10 compute tradeoff.\", \"metrics\": {\"overall_success_rate\": 0.18, \"total_successes\": 18, \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}, \"comparison\": {\"k10_reference\": \"16.8±1.8%\", \"k20_this\": \"18.0%\", \"delta\": \"+1.2pp\", \"note\": \"within K=10 error bars, marginal improvement\"}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:02:40.709Z\", \"updated_at\": \"2026-05-20T10:34:46.457Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed49 (re-run). Original seed49 data (SR=0.16) removed from analysis due to unverifiable provenance. Clean re-run for data integrity.\", \"parent\": \"eval-vla-only-long-seed49\", \"metrics\": {\"sr\": 0.16, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.9, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.2, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:02:44.429Z\", \"updated_at\": \"2026-05-20T10:34:34.589Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735, Object-calibrated) on LIBERO-Spatial seed42. Cross-benchmark threshold sweep: P75 keeps ~87% fast-path on Object, testing transfer to Spatial.\", \"metrics\": {\"sr\": 0.31, \"avg_k\": 5.02, \"fast_path_ratio\": 0.622, \"mean_l2\": 0.0909, \"adaptive_trigger_rate\": 0.378, \"total_steps\": 23914, \"fast_steps\": 14875, \"full_steps\": 9039}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:42:09.659Z\", \"updated_at\": \"2026-05-20T09:52:50.961Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"parent\": \"eval-adaptive-k-spatial-p50-seed44\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"mean_l2_distance\": 0.0923, \"total_steps\": 23661, \"fast_steps\": 10649, \"full_steps\": 13012, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:49.558Z\", \"updated_at\": \"2026-05-20T09:46:30.063Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed42. ~25% steps trigger K=10+CRM, rest use K=2 fast path. 测试 SR vs avg_K 的 Pareto 最优阈值。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 3.07, \"fast_path_ratio\": 0.866}}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:51.298Z\", \"updated_at\": \"2026-05-20T09:46:26.443Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed43. ~25% steps trigger K=10+CRM, rest use K=2 fast path. P75 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 3.15, \"fast_path_ratio\": 0.856}}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:54.375Z\", \"updated_at\": \"2026-05-20T09:46:22.801Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed42. ~50% steps trigger K=10+CRM, rest use K=2 fast path. 测试 SR vs avg_K 的 Pareto 最优阈值。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.72, \"fast_path_ratio\": 0.785}}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:55.910Z\", \"updated_at\": \"2026-05-20T09:46:19.108Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed43. ~50% steps trigger K=10+CRM, rest use K=2 fast path. P50 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.81, \"fast_path_ratio\": 0.7737, \"total_steps\": 27813, \"fast_steps\": 21520, \"full_steps\": 6293}}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:30.506Z\", \"updated_at\": \"2026-05-20T09:26:47.119Z\", \"hypothesis\": \"Random selection baseline (K=10 随机选一个 action) on LIBERO-Object seed42. Ablation 验证 CRM uncertainty-guided selection 的价值。\", \"notes\": \"2026-05-20 15:06 确认进程活跃: PID 235076, cuda:0, tmux session active, 进度 task 2/10 (~15%). 启动时间 14:40 UTC. 旧 seed44 JSON (SR=0.13) 在磁盘上但会被新运行覆盖.\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:42:06.832Z\", \"updated_at\": \"2026-05-20T09:26:09.877Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"parent\": \"eval-adaptive-k-spatial-p50-seed43\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.4, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"mean_l2_distance\": 0.0903, \"total_steps\": 23414, \"fast_steps\": 10728, \"full_steps\": 12686, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:35:07.755Z\", \"updated_at\": \"2026-05-20T08:44:33.011Z\", \"hypothesis\": \"CRM obs_only norm02 (ε=0.2) K=10 on Object seed42 achieves SR comparable to other norm02 seeds (15-20%), complementing Table 1 from n=6 to n=7 for stronger statistical backing.\", \"notes\": \"2026-05-20 15:06 确认进程活跃: PID 235678, cuda:3, tmux session active, 进度 task 2/10 (~15%). 启动时间 14:40 UTC.\", \"metrics\": {\"overall_success_rate\": 0.2, \"total_episodes\": 100, \"total_successes\": 20, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.4, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T07:21:06.879Z\", \"updated_at\": \"2026-05-20T08:42:01.299Z\", \"hypothesis\": \"Formal latency profiling (N=1000) for all inference modes. Measure per-step wall-clock time to populate Table 3 latency column.\", \"conclusion\": \"success\", \"notes\": \"N=1000 profiling 成功完成。Cron 误判 failed（脚本无 sentinel 文件）。JSON: logs/latency_profile_n1000.json (5589 bytes, 17 components × 1000 iterations)。Artifact: art_20260520_de306f。\", \"metrics\": {\"vla_e2e_K1_ms\": 256.5, \"vla_e2e_K10_ms\": 253.2, \"crm_forward_ms\": 0.28, \"cgs_features_ms\": 5.75, \"full_pipeline_K10_ms\": 249, \"adaptive_fast_path_ms\": 252.9, \"adaptive_full_path_ms\": 459.6, \"crm_overhead_vs_vla_K10_ms\": -4.2, \"crm_overhead_pct\": -1.66, \"adaptive_speedup_ratio\": 1.82, \"argmin_l2_K10_ms\": 0.06, \"gpu_mem_mb\": 903, \"n_measure\": 1000, \"gpu_model\": \"RTX 4090\"}}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:13.788Z\", \"updated_at\": \"2026-05-20T06:53:17.867Z\", \"hypothesis\": \"Adaptive K with P90 threshold (τ=0.127) on Object seed44. Part of the 4-threshold sweep validating P50 as Pareto optimal.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.58, \"fast_path_ratio\": 0.928}}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:06.901Z\", \"updated_at\": \"2026-05-20T05:56:34.512Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed43. ~75% steps trigger K=10+CRM. P25 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 4.788, \"fast_path_ratio\": 0.6515, \"total_steps\": 28207, \"fast_steps\": 18377, \"full_steps\": 9830}}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:12:15.310Z\", \"updated_at\": \"2026-05-20T05:56:30.173Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed51. 补齐 Spatial CRM 样本量，增强 ID suite correction 效果的统计可靠性。\", \"metrics\": {\"success_rate\": 0.36, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:51:05.182Z\", \"updated_at\": \"2026-05-20T05:56:26.105Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed49. 补齐 Goal baseline 样本量，与 CRM-Goal (64-72% SR) 配对对比。\", \"metrics\": {\"success_rate\": 0.65, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:12:18.551Z\", \"updated_at\": \"2026-05-20T05:56:21.658Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed52. 补齐 Long VLA-only 样本量，增强 OOD baseline 统计可靠性。\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:12:11.506Z\", \"updated_at\": \"2026-05-20T05:56:16.817Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed51. 补齐 Long VLA-only 样本量，增强 OOD baseline 统计可靠性。\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T02:42:54.485Z\", \"updated_at\": \"2026-05-20T05:56:11.186Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed50. 补齐 Long VLA-only 样本量 (n→9)，增强 OOD baseline 统计可靠性。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:16:23.286Z\", \"updated_at\": \"2026-05-20T05:56:05.404Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed50. Long OOD 补样本量，验证 CRM 在 cross-suite OOD 上的效果。\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:16:19.625Z\", \"updated_at\": \"2026-05-20T05:56:00.045Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed44. 重新部署在干净 GPU 上（原 bjb2-40593 与 calibration 共享 GPU 拖慢）。Sweep 最后一个数据点。\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.736, \"fast_path_ratio\": 0.658, \"adaptive_trigger_rate\": 0.342, \"total_steps\": 27889, \"fast_steps\": 18351, \"full_steps\": 9538}, \"conclusion\": \"success\"}, \"calibrate-crm-correction-signal\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T02:47:03.770Z\", \"updated_at\": \"2026-05-20T05:39:46.462Z\", \"hypothesis\": \"CRM correction magnitude as zero-overhead gating signal. Three correlation pairs: (1) ρ(K1_correction_mag, K10_var) — primary GO/NO-GO (threshold ρ>0.3); (2) ρ(K2_argmin_correction_mag, K10_var) — fallback if K1 fails; (3) ρ(K1_correction_mag, K2_L2_distance) — cross-validate with proven K=2 signal. If GO: zero-cost adaptive K (CRM 0.25ms, no extra VLA inference).\", \"conclusion\": \"negative\", \"metrics\": {\"go_nogo\": \"NO-GO\", \"rho_k1_corr_vs_k10_var\": 0.1523, \"p_k1_corr_vs_k10_var\": \"6.37e-143\", \"rho_k2_corr_vs_k10_var\": 0.134, \"p_k2_corr_vs_k10_var\": \"8.66e-111\", \"total_steps\": 27626, \"total_episodes\": 100}}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:05.392Z\", \"updated_at\": \"2026-05-20T03:05:13.741Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed42. ~75% steps trigger K=10+CRM. 低阈值极端——接近 fixed K=10，验证 SR 上限。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.8, \"fast_path_ratio\": 0.65}}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:08:24.943Z\", \"updated_at\": \"2026-05-20T03:02:41.906Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed48. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。重跑（前次 killed for CRM priority）。\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:08:22.088Z\", \"updated_at\": \"2026-05-20T03:02:34.679Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed47. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。重跑（前次 killed for CRM priority）。\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:43:05.230Z\", \"updated_at\": \"2026-05-20T02:54:29.366Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Goal seed46. Goal OOD 补样本量 (n→5)，验证 CRM 在 cross-suite OOD 上的效果（当前 n=2 结果中性 ~69.5%≈VLA-only）。\", \"parent\": \"eval-crm-goal-seed42\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.3}}}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:57.407Z\", \"updated_at\": \"2026-05-20T02:40:24.520Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed44. ~50% steps trigger K=10+CRM, rest use K=2 fast path. P50 sweep 第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 3.909, \"fast_path_ratio\": 0.761, \"total_steps\": 28067, \"fast_steps\": 21368, \"full_steps\": 6699}}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:52.859Z\", \"updated_at\": \"2026-05-20T02:40:21.205Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed44. ~25% steps trigger K=10+CRM, rest use K=2 fast path. P75 sweep 第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.022, \"fast_path_ratio\": 0.872, \"total_steps\": 27724, \"fast_steps\": 24181, \"full_steps\": 3543}}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:12.128Z\", \"updated_at\": \"2026-05-20T02:40:15.747Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed43. ~10% steps trigger K=10+CRM. P90 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.612, \"fast_path_ratio\": 0.923, \"total_steps\": 27935, \"fast_steps\": 25797, \"full_steps\": 2138}}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:10.641Z\", \"updated_at\": \"2026-05-20T02:40:12.273Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed42. ~10% steps trigger K=10+CRM. 高阈值极端——接近 K=2 only，验证 SR 下限。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 2.672, \"fast_path_ratio\": 0.916, \"total_steps\": 28258, \"fast_steps\": 25886, \"full_steps\": 2372}}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:51:39.170Z\", \"updated_at\": \"2026-05-20T01:39:25.709Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed47. 额外 seed 增加统计稳健性，与 CRM Spatial seed47 配对。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:49:36.050Z\", \"updated_at\": \"2026-05-20T00:21:06.698Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Long seed47. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Long 是 OOD long-horizon 任务。补充 seed42-46 增加统计样本量。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.2, \"STUDY_SCENE1_book_in_caddy\": 0.2, \"LIVING_ROOM_SCENE2_soup_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cheese_butter_basket\": 0, \"KITCHEN_SCENE4_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_soup_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:15.951Z\", \"updated_at\": \"2026-05-20T00:16:50.121Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed48. 补齐 Long VLA-only 样本量 (n→7)，增强 baseline 统计可靠性。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.3, \"STUDY_SCENE1_book_in_back_compartment\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0.1, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:13.996Z\", \"updated_at\": \"2026-05-20T00:13:08.430Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Long seed46. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Long 是未见过的 suite。补齐 CRM-Long 第 5 个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.9, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.2, \"STUDY_SCENE1_book_in_back_compartment\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:49:33.318Z\", \"updated_at\": \"2026-05-20T00:11:46.069Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed45. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。重跑（前次 crash）。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.65, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_bowl_on_top_of_the_cabinet\": 0.8, \"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"put_the_wine_bottle_on_the_rack\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_cream_cheese_in_the_bowl\": 0.2}}}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:49:31.838Z\", \"updated_at\": \"2026-05-20T00:11:07.345Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed44. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。重跑（前次 crash）。\", \"parent\": \"eval-crm-goal-seed44\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.64, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_bowl_on_the_stove\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"put_the_wine_bottle_on_the_rack\": 0.4, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:06:58.021Z\", \"updated_at\": \"2026-05-19T23:20:20.286Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed43. 重跑：bjb2-40593 上 7/10 tasks 后进程终止无 JSON。补齐 Spatial K=10 n=5。\", \"parent\": \"eval-obs-only-spatial-norm02-seed43\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:52.408Z\", \"updated_at\": \"2026-05-19T22:38:04.117Z\", \"hypothesis\": \"K=2 L2 divergence (mean pairwise L2 from K=10 samples) as uncertainty proxy for Adaptive K. Measures action-space disagreement directly. Go/no-go: Spearman ρ(mean_pair_l2, k10_variance) > 0.3.\", \"conclusion\": \"success\", \"metrics\": {\"k2l2_vs_k10var_rho\": 0.9979, \"k2l2_vs_k10var_pvalue\": 0, \"k2l2_vs_fmvd_rho\": 0.0925, \"k2l2_vs_fmvd_pvalue\": 6.03e-29, \"k10var_vs_fmvd_rho\": 0.0825, \"k10var_vs_fmvd_pvalue\": 2.33e-23, \"n_samples\": 14512, \"k2l2_mean\": 0.0807, \"k2l2_std\": 0.0361, \"go_nogo_k2_proxy\": \"GO (rho=0.9979)\", \"go_nogo_fmvd_signal\": \"NO-GO (rho=0.09)\"}}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:29.495Z\", \"updated_at\": \"2026-05-19T22:15:17.800Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed45. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD long-horizon 任务。补充 seed42/43/44 增加 n。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 18}}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:15:11.071Z\", \"updated_at\": \"2026-05-19T22:12:05.406Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed49. 补齐 Spatial VLA-only 样本量 (n→7)，增强 baseline 统计可靠性。\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:32:25.931Z\", \"updated_at\": \"2026-05-19T22:08:08.414Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed48. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:40:01.140Z\", \"updated_at\": \"2026-05-19T21:32:22.969Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed43. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.5, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.6}}}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:58.936Z\", \"updated_at\": \"2026-05-19T21:32:21.219Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed42. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:43.834Z\", \"updated_at\": \"2026-05-19T21:32:10.689Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed47. 补齐 Object VLA-only n=5，与 CRM K=10 配对统计检验。\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2, \"alphabet_soup\": 0, \"cream_cheese\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:50.501Z\", \"updated_at\": \"2026-05-19T21:32:07.617Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed44. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%，若 CRM 显著提升则证明泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.2, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.6, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:49.078Z\", \"updated_at\": \"2026-05-19T21:32:03.390Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed43. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%，若 CRM 显著提升则证明泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.3, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:47.244Z\", \"updated_at\": \"2026-05-19T21:31:58.213Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed42. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%，若 CRM 显著提升则证明泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.4, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:24.873Z\", \"updated_at\": \"2026-05-19T21:22:37.560Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed42. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。若 CRM 提升 Goal SR，证明跨 suite 泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.67, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:26.786Z\", \"updated_at\": \"2026-05-19T21:19:08.468Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed43. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。与 seed42 配对增加统计稳健性。\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:51:37.036Z\", \"updated_at\": \"2026-05-19T21:15:20.345Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed46. 补齐 Spatial VLA-only n=5，与 seed42/43/44/45 配套。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:51:41.106Z\", \"updated_at\": \"2026-05-19T21:14:38.930Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 (Long) with seed47 establishes additional statistical sample (n→6) for baseline success rate estimation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 100, \"successful_rollouts\": 14, \"per_task\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0, \"put_both_cream_cheese_box_and_butter_in_basket\": 0, \"turn_on_stove_put_moka_pot\": 0.8, \"put_black_bowl_in_bottom_drawer\": 0, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.4, \"pick_up_book_place_in_caddy\": 0.1, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.1, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0, \"put_both_moka_pots_on_stove\": 0, \"put_yellow_white_mug_in_microwave\": 0}}, \"notes\": \"Cron false positive: eval 脚本无 W&B/sentinel，进程正常退出被误判 failed。实际已完成全部 10 tasks。SR=14.0%，与已有 seeds 一致 (mean~14.2%)。手动修正 conclusion=success。\"}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:44.897Z\", \"updated_at\": \"2026-05-19T20:53:05.054Z\", \"hypothesis\": \"CRM obs_only (trained on Object+Spatial) generalizes to LIBERO-Goal OOD benchmark with ε=0.2 norm constraint, providing meaningful action refinement despite distribution shift.\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:43.382Z\", \"updated_at\": \"2026-05-19T20:52:09.464Z\", \"hypothesis\": \"CRM obs_only (trained on Object+Spatial) generalizes to LIBERO-Goal OOD benchmark with ε=0.2 norm constraint, providing meaningful action refinement despite distribution shift.\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:31:14.902Z\", \"updated_at\": \"2026-05-19T20:10:50.847Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed45. 补齐 Goal suite 第 4 个 seed (n=4)，与 seed42/43/44-r2 配套。LIBERO-Goal 目标条件泛化 baseline。\", \"metrics\": {\"overall_success_rate\": 0.63, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.3, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.1, \"turn_on_the_stove\": 0.8, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:05:08.765Z\", \"updated_at\": \"2026-05-19T20:08:19.990Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed46. 补齐 Goal suite n=5 数据，与 seed42/43/44/45 配套。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.6, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}, \"notes\": \"Cron false positive: eval completed normally (71.0%), but no W&B/sentinel → auto-resolved as failed. Manually corrected to success.\"}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:05:07.011Z\", \"updated_at\": \"2026-05-19T20:08:18.540Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed46. 补齐 Long suite n=5 数据，与 seed42/43/44/45 配套。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 0.9, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.5, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.1, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"notes\": \"Cron false positive: eval completed normally (18.0%), but no W&B/sentinel → auto-resolved as failed. Manually corrected to success.\"}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:57:05.859Z\", \"updated_at\": \"2026-05-19T20:07:21.125Z\", \"hypothesis\": \"FMVD (Flow Velocity Dispersion) signal validation: verify correlation between ODE velocity dispersion during K=1 denoising and K=10 action variance. Go/no-go gate for Adaptive K mechanism (Spearman ρ > 0.3).\", \"metrics\": {\"spearman_rho\": 0.082528, \"spearman_pvalue\": 2.33e-23, \"n_samples\": 14512, \"go_nogo\": \"NO-GO\", \"threshold\": 0.3, \"fmvd_mean\": 0.054867, \"fmvd_std\": 0.040291, \"fmvd_P25\": 0.027738, \"fmvd_P50\": 0.046693, \"fmvd_P75\": 0.070899, \"fmvd_P90\": 0.093805, \"k10_variance_mean\": 0.004888, \"k10_variance_std\": 0.005635, \"task_success_rate\": 0.06, \"n_tasks\": 10, \"n_episodes\": 50, \"n_successes\": 3}, \"conclusion\": \"negative\"}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:31:11.716Z\", \"updated_at\": \"2026-05-19T19:21:47.544Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed45. 补齐 Long suite 第 4 个 seed (n=4)，与 seed42/43/44 配套。LIBERO-10 长 horizon 任务 baseline。\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 1, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.2, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.2, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:24.175Z\", \"updated_at\": \"2026-05-19T19:05:12.052Z\", \"hypothesis\": \"perdof CRM with ε=0.03 (max_correction_norm) on LIBERO-Object seed47 tests whether a smaller correction magnitude improves or degrades task success rate compared to ε=0.05\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:21.800Z\", \"updated_at\": \"2026-05-19T19:05:09.001Z\", \"hypothesis\": \"perdof CRM with ε=0.05 (max_correction_norm) on LIBERO-Object seed47 provides per-DOF conformal refinement; this run supplements the magnitude curve at ε=0.05 (currently n=4)\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:55.593Z\", \"updated_at\": \"2026-05-19T18:38:52.937Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed44. 扩展到新 benchmark suite 验证 CRM 泛化性的前提——先建立 baseline。\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:49.327Z\", \"updated_at\": \"2026-05-19T18:38:48.009Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed42. 扩展到新 benchmark suite 验证 CRM 泛化性的前提——先建立 baseline。\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.1, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:52.159Z\", \"updated_at\": \"2026-05-19T18:33:56.305Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed43. 扩展到新 benchmark suite 验证 CRM 泛化性的前提——先建立 baseline。\", \"metrics\": {\"overall_success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.7, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.3, \"STUDY_SCENE1_book_caddy\": 0, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0.1, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:49:53.389Z\", \"updated_at\": \"2026-05-19T18:07:05.998Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:27:35.615Z\", \"updated_at\": \"2026-05-19T18:04:19.943Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed47. 补充 Spatial cross-seed 一致性数据。\", \"metrics\": {\"overall_success_rate\": 0.32, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:27:33.151Z\", \"updated_at\": \"2026-05-19T17:24:14.391Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed46. 补充 Spatial K=10 cross-benchmark 数据，当前 n=3 (seed42=35%, seed44=36%, seed45=34%)，扩展到 n=5 增强统计稳健性。\", \"conclusion\": \"failed\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:21:11.529Z\", \"updated_at\": \"2026-05-19T17:24:12.993Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed44 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:40:03.921Z\", \"updated_at\": \"2026-05-19T17:08:52.675Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed44. LIBERO-Goal 使用相同初始状态不同目标，测试 VLA 对 goal-conditioned 任务的 baseline 表现。\", \"conclusion\": \"killed\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:30.944Z\", \"updated_at\": \"2026-05-19T16:31:13.969Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed45. K=5 decomposition 对照第四个 seed，与 argmin K=5 seed45 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-random-selection-object-k5-seed45\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.07, \"successes\": 7, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:29.373Z\", \"updated_at\": \"2026-05-19T16:31:10.982Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed44. K=5 decomposition 对照第三个 seed，与 argmin K=5 seed44 配对验证 selection effect 统计显著性。\", \"parent\": \"eval-random-selection-object-k5-seed44\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:27.994Z\", \"updated_at\": \"2026-05-19T16:31:08.997Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed43. 第二个 seed 的 K=5 random selection，与 argmin K=5 seed43 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-random-selection-object-k5-seed43\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"successes\": 11, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:26.607Z\", \"updated_at\": \"2026-05-19T16:31:06.453Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed42. 从 K=5 VLA samples 中随机选 1 个执行（不用 argmin/CRM）。验证 K=5 decomposition 中 selection effect 是否真实：如果 random ≈ argmin (13.7%)，则 selection effect 不显著；如果 random < argmin，则 argmin 的选择能力在小候选池中有真实价值。\", \"parent\": \"eval-random-selection-object-k5-seed42\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:32.306Z\", \"updated_at\": \"2026-05-19T16:30:37.908Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"parent\": \"eval-obs-only-spatial-norm02-k5-seed44\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:33.621Z\", \"updated_at\": \"2026-05-19T16:30:18.549Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"parent\": \"eval-obs-only-spatial-norm02-k5-seed45\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:13:57.251Z\", \"updated_at\": \"2026-05-19T16:17:38.007Z\", \"hypothesis\": \"Latency profiling: 正式测量 VLA+CRM pipeline 各组件 wall-clock time，覆盖 K=1/5/10/20 batched vs sequential，生成论文 Table 级结果。预期 CRM overhead < 1ms，pipeline 主要 bottleneck 在 VLA flow-matching sampling。\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:24:47.682Z\", \"updated_at\": \"2026-05-19T16:06:09.222Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed45. Spatial benchmark 第四个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:50:49.193Z\", \"updated_at\": \"2026-05-19T16:06:07.907Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve perdof ε=0.05 (当前 n=2)。timeout=16h。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:24:44.727Z\", \"updated_at\": \"2026-05-19T15:30:01.540Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed44. Spatial benchmark 第三个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:50:51.880Z\", \"updated_at\": \"2026-05-19T14:58:17.531Z\", \"hypothesis\": \"obs_only CRM (ε=default/unlimited) seed48 on LIBERO-Object. 补 obs_only default (当前 n=3)。timeout=16h。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"notes\": \"误判 failed: cron 检测到 tmux session 死亡，但实验已正常完成并写入完整 JSON。手动验证 output JSON 完整（59 行，10 tasks × 10 rollouts）。success_rate=0.17，与原 seed48 (bjb2-28827) 一致。\"}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:01:28.636Z\", \"updated_at\": \"2026-05-19T14:43:19.646Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed43. P1 缺口：与 Spatial K=5 CRM seed43=32% 配对，计算 per-seed improvement。没有此 baseline 无法报告 Spatial 改进幅度。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T12:55:51.909Z\", \"updated_at\": \"2026-05-19T14:38:29.599Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed42. P1 缺口：Spatial benchmark 需要 VLA-only baseline 才能报告 CRM 的改进幅度。对标 obs_only spatial K=10 seed42=35%。\", \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:40.507Z\", \"updated_at\": \"2026-05-19T14:32:21.490Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:39.233Z\", \"updated_at\": \"2026-05-19T14:32:16.468Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:37.093Z\", \"updated_at\": \"2026-05-19T14:32:11.343Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed45. K=5 decomposition 对照第四个 seed，与 argmin K=5 seed45 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-argmin-object-k5-seed45\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:34.934Z\", \"updated_at\": \"2026-05-19T14:32:06.313Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed44. K=5 decomposition 对照第三个 seed，与 argmin K=5 seed44 配对验证 selection effect 统计显著性。\", \"parent\": \"eval-argmin-object-k5-seed44\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:57:11.028Z\", \"updated_at\": \"2026-05-19T14:32:01.561Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed43. 第二个 seed 的 K=5 random selection，与 argmin K=5 seed43 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-argmin-object-k5-seed43\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:43:11.414Z\", \"updated_at\": \"2026-05-19T14:31:56.882Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed42. 从 K=5 VLA samples 中随机选 1 个执行（不用 argmin/CRM）。验证 K=5 decomposition 中 selection effect 是否真实：如果 random ≈ argmin (13.7%)，则 selection effect 不显著；如果 random < argmin，则 argmin 的选择能力在小候选池中有真实价值。\", \"parent\": \"eval-argmin-object-k5-seed42\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:49:54.536Z\", \"updated_at\": \"2026-05-19T14:26:11.536Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T01:29:55.249Z\", \"updated_at\": \"2026-05-19T13:39:15.552Z\", \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"hypothesis\": \"per-DoF CRM with max_correction_norm=0.1 on LIBERO-Object (seed43, K=10, n_rollouts=10) should achieve comparable SR to obs_only default, as tighter norm constraint limits correction magnitude per joint.\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:53.834Z\", \"updated_at\": \"2026-05-19T13:35:23.895Z\", \"hypothesis\": \"obs_only CRM uncapped (default norm ~1.42) seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=12%)，需标准化。obs_only default 当前 n=3 (seed42/43/44)。\", \"parent\": \"eval-obs-only-object-default-seed45\", \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:30.602Z\", \"updated_at\": \"2026-05-19T13:30:16.050Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed42 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:36:13.145Z\", \"updated_at\": \"2026-05-19T13:26:50.930Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed45 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:15.812Z\", \"updated_at\": \"2026-05-19T13:26:46.918Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed43 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:18:03.763Z\", \"updated_at\": \"2026-05-19T13:24:40.192Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed43 on LIBERO-Object. 补 magnitude curve：perdof ε=0.3 当前 n=3 (seed42:4%, seed44:4%, seed45:6%)，mean=4.67%。增加第 4 个 seed 强化 error bars。\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:49:55.654Z\", \"updated_at\": \"2026-05-19T13:12:13.645Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed45. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:40:51.279Z\", \"updated_at\": \"2026-05-19T12:48:29.290Z\", \"conclusion\": \"success\", \"hypothesis\": \"K=1 CRM full training with multi-stage VLA feature fusion + composite loss (L2 + contrastive + uncertainty-weighted) on full object benchmark dataset. Scaled-up version of train-crm-k1-accg-object-seed42-v2 with complete training data.\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:11:43.484Z\", \"updated_at\": \"2026-05-19T12:48:27.021Z\", \"conclusion\": \"success\", \"hypothesis\": \"K=1 spatial benchmark precomputation: generate single-sample VLA action predictions and features for CRM K=1 training. Required preprocessing step before K=1 CRM can be trained on spatial tasks.\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:04:14.203Z\", \"updated_at\": \"2026-05-19T12:48:10.176Z\", \"hypothesis\": \"K=1 CRM 训练：使用多阶段 VLA 特征融合 + 组合损失函数（L2 + contrastive + uncertainty-weighted），训练专门用于 K=1 单采样纠正的 CRM 模型。目标是超越 K=1 VLA-only baseline (10.8%)。\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:59:53.216Z\", \"updated_at\": \"2026-05-19T12:48:06.312Z\", \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.3 至 n=7。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:59:51.090Z\", \"updated_at\": \"2026-05-19T12:48:03.869Z\", \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.1 至 n=7。\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:16.472Z\", \"updated_at\": \"2026-05-19T12:48:01.446Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks r3 rerun. Second reproduction of LTO baseline SR=14%. Confirms v2 result consistency.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:55:29.003Z\", \"updated_at\": \"2026-05-19T12:47:58.882Z\", \"hypothesis\": \"VLA-only baseline on 5 held-out tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Bugfix r2: removed .replace(\\\"_\\\",\\\" \\\") that caused 3/5 task matching failures.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:55:26.507Z\", \"updated_at\": \"2026-05-19T12:47:56.312Z\", \"hypothesis\": \"LTO split-A CRM (K=5, ε=0.2, obs_only) on 5 held-out tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Bugfix r2: removed .replace(\\\"_\\\",\\\" \\\") that caused 3/5 task matching failures.\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:13:30.382Z\", \"updated_at\": \"2026-05-19T12:47:52.436Z\", \"conclusion\": \"success\", \"hypothesis\": \"LTO Split A CRM training (obs_only, 5 tasks, task_indices 0-4). Predecessor to eval-lto-splitA-heldout experiments. Superseded by crm-lto-splitA-train-fixed (task_names matching).\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:31:15.780Z\", \"updated_at\": \"2026-05-19T12:23:18.801Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.03) seed48 on LIBERO-Object. 补 magnitude curve 最薄点 perdof ε=0.03 (当前 n=1)。timeout=16h。\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T12:22:25.439Z\", \"updated_at\": \"2026-05-19T11:45:28.182Z\", \"hypothesis\": \"Scalar CRM seed45 rerun with n_rollouts=10 for consistency. Original seed45 used n_rollouts=20. Current scalar: [9,10,6,9] mean=8.5%\", \"parent\": \"eval-scalar-object-seed45\", \"metrics\": {\"overall_success_rate\": 0.07, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:33.036Z\", \"updated_at\": \"2026-05-19T11:34:16.077Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark generalization claim.\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:04:44.384Z\", \"updated_at\": \"2026-05-19T11:34:12.397Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed48 on LIBERO-Object. D066 K=5 primary configuration 补种到 n=7 统计力度增强。\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:18.656Z\", \"updated_at\": \"2026-05-19T11:31:39.191Z\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark generalization claim.\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:29:24.718Z\", \"updated_at\": \"2026-05-19T11:30:55.300Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed46 on LIBERO-Object. 补 K=5 primary configuration 到 n≥5。D066 统计力度增强。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:19:21.005Z\", \"updated_at\": \"2026-05-19T11:30:43.198Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval. Retry after .replace task matching bug fix.\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:19:18.968Z\", \"updated_at\": \"2026-05-19T11:30:33.951Z\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. Retry after .replace task matching bug fix.\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}, \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:44.467Z\", \"updated_at\": \"2026-05-19T11:30:18.282Z\", \"hypothesis\": \"Per-DoF CRM (ε=default/unlimited) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束, success_rate=0%\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:47.310Z\", \"updated_at\": \"2026-05-19T11:30:17.012Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:41.596Z\", \"updated_at\": \"2026-05-19T11:30:15.785Z\", \"hypothesis\": \"Obs-only CRM (ε=default/unlimited) seed48 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:35.770Z\", \"updated_at\": \"2026-05-19T11:30:14.493Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.03) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-19T11:29:18.036Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:15:14.634Z\", \"updated_at\": \"2026-05-19T11:28:09.358Z\", \"hypothesis\": \"perdof CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 薄数据点：perdof ε=0.03 当前 n=1 (seed42=14%)，seed43/44 已在跑。验证 per-DOF correction 在极低 norm 下表现。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:29:27.251Z\", \"updated_at\": \"2026-05-19T11:27:53.132Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed47 on LIBERO-Object. 补 K=5 primary configuration 到 n≥6。D066 统计力度增强。\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:57:04.076Z\", \"updated_at\": \"2026-05-19T11:25:28.189Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.1) seed48 on LIBERO-Object. 补 perdof ε=0.1 至 n=7，替代被 kill 的 obs_only_norm03_seed46 重复实验的 GPU slot。\", \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-19T11:25:18.480Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-19T11:25:13.541Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-19T11:25:11.008Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-19T11:25:07.860Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:44:44.161Z\", \"updated_at\": \"2026-05-19T05:16:02.877Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. Retry with timeout=16h after r1 timed out. 补 magnitude curve 最薄点 ε=0.03。\", \"conclusion\": \"killed\", \"metrics\": {\"partial\": true, \"tasks_completed\": \"5/10\", \"task6_partial\": \"5/10 rollouts\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0}, \"partial_avg_sr\": 0.1, \"failure_mode\": \"process killed silently mid-eval, no error in log, no JSON output\"}}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:35:02.089Z\", \"updated_at\": \"2026-05-19T05:13:20.212Z\", \"conclusion\": \"killed\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval.\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:34:59.607Z\", \"updated_at\": \"2026-05-19T05:13:18.481Z\", \"conclusion\": \"killed\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. If SR > VLA-only on held-out tasks, CRM generalizes beyond training distribution.\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:53:33.612Z\", \"updated_at\": \"2026-05-19T04:58:44.483Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 obs_only ε=0.05 seed (n=4→5)。\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:15:14.835Z\", \"updated_at\": \"2026-05-19T04:58:40.993Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed48 on LIBERO-Object. 补 perdof ε=0.3 至 n=7。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:09:03.172Z\", \"updated_at\": \"2026-05-19T04:58:36.864Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed49 on LIBERO-Object. 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)，第 6 个 seed 确保极低 norm 端统计可靠。\", \"conclusion\": \"killed\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:27:23.594Z\", \"updated_at\": \"2026-05-19T04:32:49.103Z\", \"conclusion\": \"success\", \"hypothesis\": \"Leave-Task-Out Split A: CRM (obs_only) trained on 5 tasks (alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, 7499 samples) can generalize to held-out 5 tasks. Uses task_names string matching.\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:15:10.585Z\", \"updated_at\": \"2026-05-19T04:32:33.294Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. 补 magnitude curve ε=0.03 至 n=6。\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:55.304Z\", \"updated_at\": \"2026-05-19T03:28:52.476Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed43 on LIBERO-Object。magnitude curve 低 ε 端当前只有 seed42 (14%, n=1)，第二个 seed 增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:27:51.549Z\", \"updated_at\": \"2026-05-19T02:56:00.676Z\", \"hypothesis\": \"perdof CRM ε=0.05 seed43 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.05 当前只有 seed42 (14%, n=1)，第二个 seed 增强统计可靠性。\", \"parent\": \"eval-mag-perdof-norm005-object\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T06:17:50.362Z\", \"updated_at\": \"2026-05-19T01:44:05.704Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed43 confirms cross-seed consistency of collapse.\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:21:08.043Z\", \"updated_at\": \"2026-05-19T01:38:34.712Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed45 confirms cross-seed consistency of collapse.\", \"parent\": \"crm-train-v2-perdof\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:38.704Z\", \"updated_at\": \"2026-05-19T01:33:59.345Z\", \"hypothesis\": \"Obs-only CRM (ε=0.2, K=5) seed45 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:50:46.149Z\", \"updated_at\": \"2026-05-18T21:55:07.741Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve：perdof ε=0.05 当前 n=2 (seed42=14%, seed44=9%), seed43 在跑。第 4 个 seed 强化低 ε 端 error bars。\", \"conclusion\": \"failed\", \"notes\": \"失败原因: EXIT_CODE=124 timeout (wall_clock=6.03h, timeout_hours 过低) | 已知失败模式: LIBERO-Object 全量 eval 需 12-14h，6h timeout 不够 | 建议: 重提交 timeout_hours=16\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:27:12.596Z\", \"updated_at\": \"2026-05-18T21:05:50.448Z\", \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed44. Third seed for K-value curve (seed42=14%, seed43=19%, mean=16.5%). Variance 大 (5pp gap), 第三个 seed 对 K-value scaling narrative 至关重要。\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:31:41.748Z\", \"updated_at\": \"2026-05-18T19:14:55.968Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。重试 r2 修正 python 路径。\", \"parent\": \"eval-perdof-object-norm003-seed44\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:33:39.698Z\", \"updated_at\": \"2026-05-18T16:48:10.654Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed46 on LIBERO-Object. Retry r3. Supplements magnitude curve ε=0.1 data. seed42=19%, seed43=12%, seed44=16%, seed45=14%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:31:56.813Z\", \"updated_at\": \"2026-05-18T15:18:13.193Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段 perdof 数据。与 obs_only norm005 seed44 配对对比。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T11:44:42.438Z\", \"updated_at\": \"2026-05-18T14:17:30.462Z\", \"hypothesis\": \"VLA-only baseline seed45 rerun with n_rollouts=10 for consistency. Original seed45 used n_rollouts=20. Current VLA-only: [12,12,10,9,13] mean=11.2%\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:27:53.154Z\", \"updated_at\": \"2026-05-18T13:31:57.990Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。第三个 seed 进一步增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"conclusion\": \"failed\", \"notes\": \"EXIT_CODE=127, python not found. bjb1-18228 需用 /root/miniconda3/bin/python 而非 bare python.\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:02:40.444Z\", \"updated_at\": \"2026-05-18T13:27:03.418Z\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补充 magnitude curve high-norm 段 seed48 数据。扩展 error bars。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T04:37:18.401Z\", \"updated_at\": \"2026-05-18T12:39:30.555Z\", \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed43. Second seed for K-value curve (seed42=14%). Director highest priority.\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:32:26.297Z\", \"updated_at\": \"2026-05-18T12:33:45.335Z\", \"hypothesis\": \"perdof CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-perdof-object-norm01-seed42. PID 497642 on cuda:3, started 07:52 UTC.\", \"parent\": \"eval-perdof-object-norm01-seed42\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:32:25.342Z\", \"updated_at\": \"2026-05-18T12:33:41.666Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-obs-only-object-norm01-seed42. PID 497445 on cuda:1, started 07:52 UTC.\", \"parent\": \"eval-obs-only-object-norm01-seed42\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:36:46.839Z\", \"updated_at\": \"2026-05-18T10:56:45.558Z\", \"hypothesis\": \"Perdof CRM with norm clipping ε=0.2 provides controlled corrections that preserve baseline policy behavior on LIBERO-Object. Expected SR ~10% (similar to other seeds 42/44/45/46/47 at 9-12%).\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:19.181Z\", \"updated_at\": \"2026-05-18T07:05:38.605Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=46 on LIBERO Object. Extends perdof low-norm data (seed42=11%, seed44/45 running). At ε=0.1 perdof is in its \\\"safe zone\\\" (tight bound masks noisy corrections). Paired with obs_only seed46 for direct comparison at same seed.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T09:01:52.970Z\", \"updated_at\": \"2026-05-18T07:05:03.603Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。seed42 在 0.1 为 19%，如果一致则确认 obs_only 全 norm 范围鲁棒。\", \"conclusion\": \"success\", \"notes\": \"PID 474319 died, GPU idle 28h+. Ghost experiment — process dead but registry not updated.\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:34:40.971Z\", \"updated_at\": \"2026-05-18T07:05:02.646Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) 比较，验证 sample count 对 selection quality 的影响。若 K=5 显著低于 K=10，说明足够的 candidate 多样性对 CRM selection 关键。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:54.338Z\", \"updated_at\": \"2026-05-18T07:05:01.672Z\", \"hypothesis\": \"perdof CRM (default norm, 无裁剪) seed46 on LIBERO-Object. 验证 perdof 在 uncapped norm 下的灾难性崩溃（seed42=0%）是否跨 seed 一致。支撑 obs_only > perdof claim。\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:18:01.200Z\", \"updated_at\": \"2026-05-18T06:19:59.229Z\", \"hypothesis\": \"perdof CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 perdof 在 uncapped norm 下的 catastrophic collapse（seed42=0%）。为 magnitude curve 提供第二个 seed 的 default 数据点。\", \"notes\": \"Timeout (EXIT_CODE=124, 24h) but partial results conclusive: 0/90 rollouts = 0% SR across 9/10 tasks. Task 10 not started. Confirms catastrophic collapse at unclipped norm, consistent with seed42=0%. Every rollout hit max_steps=300 (agent unable to complete any task), causing the timeout.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Partial 9/10 tasks, 0/90 rollouts. Accepted as collapse evidence per Director decision 2026-05-18.\"}}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:13.281Z\", \"updated_at\": \"2026-05-18T05:54:22.364Z\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"conclusion\": \"killed\", \"hypothesis\": \"Per-DoF CRM with max_correction_norm=0.2 on LIBERO-Spatial achieves optimal balance between correction magnitude and stability — norm=0.2 is hypothesized sweet spot from obs-only results\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-18T05:54:21.341Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"notes\": \"[2026-05-15] HUNG: 3/10 tasks done (56.7%, 17/30), stuck on task 4 env init for 8+ hours. Process alive (pid 288939, GPU 1450 MiB) but zero log progress. Needs kill+restart.\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-18T05:54:20.300Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization.\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env init hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。7/10 tasks 完成，42.9% SR (30/70)。需重跑 tasks 8-10（或全部重跑）。\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-18T05:54:19.300Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。6/10 tasks 完成 + task 7 部分（5/10 rollouts），40.0% SR (24/60)。需重跑。\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-18T05:54:18.227Z\", \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"notes\": \"[2026-05-15] HUNG: 9/10 tasks done (36.7%, 33/90), stuck on task 10 env init for 8+ hours. Process alive (pid 231426, GPU 1414 MiB) but zero log progress. Needs kill+restart.\", \"conclusion\": \"killed\", \"hypothesis\": \"Argmin-only selection (K=10, pick lowest CRM score without correction) on LIBERO-Spatial tests whether selection alone provides benefit — isolating the selection mechanism from the correction mechanism\", \"parent\": \"eval-reconvla-spatial-v3\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-18T05:54:17.209Z\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"success\", \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection) on LIBERO-Spatial improves over VLA-only baseline, validating that conformal selection generalizes across spatial reasoning tasks\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-18T05:54:16.171Z\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"negative\", \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection with scalar uncertainty) on LIBERO-Object improves over VLA-only baseline by selecting highest-confidence action from candidate set\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:56:51.046Z\", \"updated_at\": \"2026-05-18T05:54:15.084Z\", \"hypothesis\": \"OpenVLA 7B VLA-only baseline on LIBERO-Object. 0% SR due to transformers 5.8 DynamicCache bug. Fix: use official repo eval code with transformers 4.40.1 in isolated conda env. Dry-run verified 80% SR on libero_spatial. Awaiting GPU for full LIBERO-Object eval.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 100, \"avg_inference_time_ms\": 178, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}, \"notes\": \"NEEDS INVESTIGATION: 0% success rate vs OpenVLA paper 88.4% (LIBERO-Object). 100% confirmed code bug. Suspected action tokenization/detokenization or unnormalize issue. Do NOT treat as valid baseline.\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:28.585Z\", \"updated_at\": \"2026-05-18T04:37:10.886Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed47. Magnitude curve data point for perdof at primary comparison norm.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:05:21.870Z\", \"updated_at\": \"2026-05-18T03:04:35.124Z\", \"hypothesis\": \"obs_only CRM ε=0.2 seed48. Key data point at primary comparison norm.\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:52.326Z\", \"updated_at\": \"2026-05-18T03:03:50.286Z\", \"hypothesis\": \"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T10:54:38.275Z\", \"updated_at\": \"2026-05-18T02:24:22.787Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed46. Magnitude curve data point for perdof variant at primary comparison norm.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:13.356Z\", \"updated_at\": \"2026-05-18T01:01:03.202Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=46 on LIBERO Object. Extends magnitude curve low-norm segment to 3+ seeds. If consistent with seed42=19% and seed45 (running), strengthens robustness claim that obs_only maintains stable performance across all ε values.\", \"conclusion\": \"failed\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:04:31.864Z\", \"updated_at\": \"2026-05-17T23:47:05.521Z\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:04:34.999Z\", \"updated_at\": \"2026-05-17T23:47:03.765Z\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T12:04:16.681Z\", \"updated_at\": \"2026-05-17T23:17:06.378Z\", \"hypothesis\": \"perdof CRM ε=0.2 seed43 on LIBERO-Object. 第 3 次尝试。补充 perdof magnitude curve ε=0.2 数据（seed42=11%）。\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:04:37.024Z\", \"updated_at\": \"2026-05-17T23:10:07.386Z\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T10:27:16.189Z\", \"updated_at\": \"2026-05-17T23:00:33.671Z\", \"hypothesis\": \"Duplicate of perdof norm=0.1 seed47 on bjb1-32546 (deployed by orphan Worker). Also running on bjb2-40593.\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T20:06:55.243Z\", \"updated_at\": \"2026-05-17T22:39:25.302Z\", \"hypothesis\": \"OpenVLA 7B finetuned VLA-only baseline on LIBERO-Object using official eval code (transformers 4.40.1, isolated conda env). v1 failed due to transformers 5.8 DynamicCache bug. Dry-run on libero_spatial confirmed 80% SR. This run uses openvla-libero-object finetuned model with 10 trials/task.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:40:32.365Z\", \"updated_at\": \"2026-05-17T21:14:35.625Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed44. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:14.132Z\", \"updated_at\": \"2026-05-17T21:02:09.738Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed44. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:11.800Z\", \"updated_at\": \"2026-05-17T21:02:08.069Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed43. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:09.846Z\", \"updated_at\": \"2026-05-17T21:02:06.052Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed42. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:05:32.383Z\", \"updated_at\": \"2026-05-17T21:01:12.153Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed46 will show magnitude sensitivity collapse pattern similar to seed42, confirming obs_only robustness advantage\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:40:31.417Z\", \"updated_at\": \"2026-05-17T20:55:55.430Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed43. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:18.289Z\", \"updated_at\": \"2026-05-17T18:37:21.561Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:34:38.488Z\", \"updated_at\": \"2026-05-17T18:37:20.319Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救重跑。seed42 ε=0.05=13%。\", \"conclusion\": \"killed\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:20.097Z\", \"updated_at\": \"2026-05-17T18:35:42.842Z\", \"hypothesis\": \"Measure wall-clock latency of ACR-VLA pipeline components: VLA encode, VLA K-sampling (K=1/5/10/20), CGS scoring, CRM forward pass, and full pipeline. Quantify overhead of conformal refinement relative to VLA sampling cost.\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:51:14.367Z\", \"updated_at\": \"2026-05-17T18:31:23.291Z\", \"hypothesis\": \"K=1 CRM with ACCG using full multi-scale features (4×960D from SmolVLA layers [3,7,11,15]). Multi-scale should capture richer correction signals than single-stage 960D fallback (val_loss=0.006505). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"notes\": \"Retry after W&B API key crash. Added --no_wandb. Precompute cache reused (65,223 samples). Training restarted from scratch (epoch 1/50). PID 447923 on cuda:0, tmux session: train-crm-k1-v2.\", \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}, \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:28:01.165Z\", \"updated_at\": \"2026-05-17T18:22:02.272Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed44. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.07, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:27:59.825Z\", \"updated_at\": \"2026-05-17T18:22:01.354Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed43. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:27:58.213Z\", \"updated_at\": \"2026-05-17T18:22:00.464Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed42. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:15:05.583Z\", \"updated_at\": \"2026-05-17T17:32:15.936Z\", \"hypothesis\": \"obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 uncapped 大 norm 下仍优于 VLA-only（seed42 在 default 为 17%）。极端 magnitude 鲁棒性测试。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:38:01.206Z\", \"updated_at\": \"2026-05-17T17:29:34.723Z\", \"hypothesis\": \"Scalar uncertainty CRM seed=45 on LIBERO Object. 测试 scalar conditioning（单一 std 而非 per-DOF）是否比 obs_only 或 perdof 更优。如果表现介于两者之间，说明 conditioning 信息量与性能正相关。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:34:55.059Z\", \"updated_at\": \"2026-05-17T17:03:14.729Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=45 on LIBERO Object. 验证 perdof 在中间 norm (0.2) 的表现（seed42=11%, seed43=9%）。为 magnitude curve 误差估计提供第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"notes\": \"perdof ε=0.2 seed45: 9% (18/200). Cross-seed: seed42=11%, seed43=9%, seed44=10%, seed45=9%. Mean ~9.75%.\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T00:37:24.278Z\", \"updated_at\": \"2026-05-17T16:52:17.419Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=44 on LIBERO Object benchmark. Adds second seed to perdof norm=0.2 (seed42=11%, seed43=9%). Enables error bar on magnitude curve figure at this norm point.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:02:35.790Z\", \"updated_at\": \"2026-05-17T15:19:16.626Z\", \"hypothesis\": \"CRM K=1 with ACCG architecture trained on K=10 single-stage cache (960D fallback) can learn effective corrections for object benchmark, achieving low val_loss comparable to multi-scale approach\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:48:22.459Z\", \"updated_at\": \"2026-05-17T14:53:10.162Z\", \"hypothesis\": \"K=1 CRM 训练（ACCG 架构）：使用 Action-Conditioned Correction Gating 替代 FiLM，多阶段 VLA 特征融合 + 组合损失函数（L2 + directional + triplet + magnitude），训练专用于 K=1 单采样纠正的 CRM。目标超越 K=1 VLA-only baseline (10.8%)。ACCG 用 action 本身计算动态 gate 选择 correction 维度。\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:34:09.564Z\", \"updated_at\": \"2026-05-17T13:52:58.983Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:05:28.139Z\", \"updated_at\": \"2026-05-17T13:31:57.433Z\", \"hypothesis\": \"obs_only CRM at eps=0.1 on seed47 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude curve\", \"conclusion\": \"killed\", \"notes\": \"Worker batch7 误杀, 4/10 tasks 完成\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:32:42.117Z\", \"updated_at\": \"2026-05-17T12:04:17.540Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=45 on LIBERO object benchmark. Retry after unregistered process conflict. Expected to confirm perdof collapse at high norm (seed42=4%, seed44 running). Supports magnitude curve narrative.\", \"metrics\": {\"overall_sr\": 0.06, \"successes\": 6, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:22:10.412Z\", \"updated_at\": \"2026-05-17T12:00:58.173Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed44 re-run on LIBERO-Object. 原 seed44 已完成(conclusion=negative, SR=4%). 重跑验证跨 seed 一致性。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"n_rollouts\": 10, \"total_rollouts\": 100, \"note\": \"JSON result found by diagnostic worker. Matches original seed44=4%. False positive failure due to no sentinel/W&B in evaluate.py.\"}}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:56.645Z\", \"updated_at\": \"2026-05-17T11:50:09.879Z\", \"hypothesis\": \"obs_only CRM ε=0.3 seed47 on LIBERO-Object. 5th seed at high norm (seed42=19%, seed44=18%, seed45=14%, seed46 running). 补全 magnitude curve 高 norm 段 error bar。\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:28:13.840Z\", \"updated_at\": \"2026-05-17T11:36:55.536Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed46 retry on LIBERO-Object. 原 PID 394433 退出，PID 392856 在 bjb2-28827 cuda:2 继续运行。seed42=4%, seed44=4%, seed45=6%。\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:21:04.937Z\", \"updated_at\": \"2026-05-17T10:59:11.317Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=44 on LIBERO Object. 验证 perdof 在低 norm 的安全区域（seed42=11%，seed45 running）。多 seed 支撑 magnitude curve 低 norm 段。\", \"conclusion\": \"negative\", \"notes\": \"失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed | 诊断中: Worker worker_diagnose_eval-perdof-object-norm01-seed44_20260517T105221 已派发到 bjb1-18228 检查是否为 cron 误判（同配置 seed45 成功，SR=11%）\", \"metrics\": {\"overall_sr\": 0.08, \"total_successes\": 8, \"total_rollouts\": 100, \"seed\": 44, \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:07:14.242Z\", \"updated_at\": \"2026-05-17T10:56:41.892Z\", \"hypothesis\": \"Duplicate of seed47 obs_only norm=0.1 on bjb2 (survived GPU conflict cleanup), provides extra seed47 data point\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:17:00.494Z\", \"updated_at\": \"2026-05-17T10:54:24.948Z\", \"hypothesis\": \"Duplicate of obs_only norm=0.1 seed46 on bjb2 (deployed by batch5 Worker). Extra data point for magnitude curve.\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:38:21.922Z\", \"updated_at\": \"2026-05-17T10:54:02.629Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) seed=47 on LIBERO object benchmark. Paired with obs_only seed47 on cuda:0 for direct comparison. Extends argmin multi-seed data for pooled Fisher test.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:21:06.341Z\", \"updated_at\": \"2026-05-17T10:22:14.183Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=45 on LIBERO Object. 验证 perdof 在低 norm (0.1) 的安全区域（seed42=11%）。如果与 obs_only 接近，支持\\\"低 norm 两者等效\\\"叙事。\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:20.872Z\", \"updated_at\": \"2026-05-17T10:19:28.338Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed47, completes magnitude curve low-norm data for perdof\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T18:39:23.017Z\", \"updated_at\": \"2026-05-17T10:19:26.819Z\", \"hypothesis\": \"Argmin baseline (conformal selection K=10, 无 learned correction) seed=46 on LIBERO Object. 与 obs_only seed=46 配对，扩展 pooled Fisher test 到 6 seeds。预期 12-17% SR。\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T15:24:08.486Z\", \"updated_at\": \"2026-05-17T07:02:49.285Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.3 on LIBERO Object (seed=45) should show graceful degradation similar to seed42 (19%), providing multi-seed error estimates for the magnitude curve\", \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:14:45.495Z\", \"updated_at\": \"2026-05-17T06:54:28.933Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=45 on LIBERO object benchmark. Completes seed=45 six-way comparison. seed42=12%, seed43=15%, seed44=running.\", \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:44:23.744Z\", \"updated_at\": \"2026-05-17T06:53:28.467Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"hypothesis\": \"Argmin baseline (conformal selection K=10, no correction) seed=45 on LIBERO Object. Highest priority: expands argmin multi-seed data from 3 to 4 seeds, balancing against obs_only 5 seeds for symmetric Fisher test. Expected 12-17% SR.\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:01:50.937Z\", \"updated_at\": \"2026-05-17T04:48:50.296Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠正价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42-r2\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T15:24:11.457Z\", \"updated_at\": \"2026-05-17T04:45:11.458Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=44 on LIBERO Object. 验证 perdof 在高 norm (0.3) 的退化程度（seed42=4%）。多 seed 确认 perdof progressive collapse 机制。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"total_episodes\": 100, \"successes\": 4, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 0, \"bbq_sauce\": 1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 1, \"milk\": 0, \"chocolate_pudding\": 1, \"orange_juice\": 0}}}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:07:31.626Z\", \"updated_at\": \"2026-05-17T03:31:42.118Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.2 on LIBERO object benchmark. Paired with obs_only norm=0.2 (running, 18% at 5/10) for magnitude comparison figure. Tests perdof at moderate correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"negative\", \"parent\": \"eval-acr-object-v3\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-17T03:31:41.215Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"conclusion\": \"negative\", \"parent\": \"crm-train-v2-scalar-unc\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:21.006Z\", \"updated_at\": \"2026-05-17T03:31:40.288Z\", \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"conclusion\": \"negative\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO Spatial benchmark. Spatial benchmark 下 obs_only 最优 norm 是否同样为 0.2。如果 spatial 无明显分离，说明方法效果依赖 action distribution shift 程度。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:16.095Z\", \"updated_at\": \"2026-05-17T03:31:39.344Z\", \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM (ε=0.3) on LIBERO Spatial benchmark. 高 norm 下 perdof 在 spatial 是否也出现退化。如果 spatial 无 collapse（与 obs_only 接近），说明 failure mode 与 task complexity 相关。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:10.924Z\", \"updated_at\": \"2026-05-17T03:31:38.448Z\", \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 下 perdof 在 spatial 的表现。如果与 obs_only-0.05 一致（35%），说明低 norm 约束消除了 conditioning 差异。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:08.547Z\", \"updated_at\": \"2026-05-17T03:31:37.673Z\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 perdof 在 spatial 的表现。与 obs_only-0.03 (34%) 对比，验证低 norm 安全区域。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-17T03:15:31.664Z\", \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\", \"hypothesis\": \"VLA mean action (average of K=10 samples) on LIBERO-Spatial provides a strong baseline by reducing sampling noise — establishes whether sample averaging alone matches or exceeds single-sample VLA\", \"parent\": \"eval-spatial-v7-full\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:20:46.639Z\", \"updated_at\": \"2026-05-17T03:15:28.368Z\", \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"hypothesis\": \"ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided corrections without requiring action history\", \"parent\": \"crm-train-v2-obs-only\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:05:16.510Z\", \"updated_at\": \"2026-05-17T03:15:26.392Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"hypothesis\": \"Full ACR pipeline v7 (obs-only CRM, conformal selection, norm=0.1) on LIBERO-Spatial achieves improvement over VLA-only baseline (32%), validating the method on spatial reasoning tasks\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:05:25.647Z\", \"updated_at\": \"2026-05-17T03:15:25.342Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"hypothesis\": \"Full ACR pipeline v8 (obs-only CRM, K=10 conformal selection, norm=0.1) on LIBERO-Object achieves consistent improvement over VLA-only baseline (9-12%) across all 10 tasks with optimized hyperparameters\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:55:02.277Z\", \"updated_at\": \"2026-05-17T03:15:19.323Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v5 (shard 2/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard2\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:55:00.276Z\", \"updated_at\": \"2026-05-17T03:15:18.177Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v5 (shard 1/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard1\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:54:59.383Z\", \"updated_at\": \"2026-05-17T03:15:17.511Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v5 (shard 0/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard0\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:14.301Z\", \"updated_at\": \"2026-05-17T03:15:16.391Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v4 (shard 2/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard2\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:12.183Z\", \"updated_at\": \"2026-05-17T03:15:15.362Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v4 (shard 1/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard1\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:09.830Z\", \"updated_at\": \"2026-05-17T03:15:14.415Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v4 (shard 0/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard0\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:20:02.901Z\", \"updated_at\": \"2026-05-17T03:14:58.588Z\", \"conclusion\": \"success\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}, \"hypothesis\": \"VLA mean action on LIBERO-Spatial task 10 (wooden shelf) specifically — completing the last missing task from the earlier eval-vla-mean-spatial run to have full 10-task baseline numbers\", \"parent\": \"eval-vla-mean-spatial\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-17T03:14:57.896Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"hypothesis\": \"ReconVLA (K=10 sample consensus without CRM) on LIBERO-Spatial establishes upper bound for pure sampling diversity benefit — if high, CRM correction adds value only at lower K; if low, confirms CRM is essential\", \"parent\": \"plan_014-reconvla-baseline\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-17T03:14:57.225Z\", \"conclusion\": \"failed\", \"hypothesis\": \"Obs-only CRM v2 retrained on spatial data resolves the dimension mismatch from v1 and achieves meaningful improvement on LIBERO-Spatial by using benchmark-matched visual features\", \"parent\": \"eval-obs-only-spatial\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:30:43.696Z\", \"updated_at\": \"2026-05-17T03:14:56.290Z\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}, \"hypothesis\": \"Training CRM to predict scalar uncertainty enables confidence-based action selection via conformal prediction, allowing adaptive correction magnitude based on model confidence\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:30:40.796Z\", \"updated_at\": \"2026-05-17T03:14:55.328Z\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}, \"hypothesis\": \"Training CRM with per-DoF (per degree-of-freedom) correction output produces more fine-grained corrections than a single scalar, improving downstream task performance on multi-joint manipulation\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:41:35.819Z\", \"updated_at\": \"2026-05-17T03:14:53.940Z\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}, \"hypothesis\": \"Training a CRM with obs-only input (no action/proprio) can learn correction signals purely from visual observation features, enabling correction without access to action space information\", \"parent\": \"plan_001-crm-smolvla\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:57:48.056Z\", \"updated_at\": \"2026-05-17T03:13:50.200Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing VLA action caches (shard 2/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:57:46.669Z\", \"updated_at\": \"2026-05-17T03:13:49.286Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing VLA action caches (shard 1/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:57:45.284Z\", \"updated_at\": \"2026-05-17T03:13:43.682Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing VLA action caches (shard 0/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-k5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:15:37.603Z\", \"updated_at\": \"2026-05-17T03:13:41.787Z\", \"conclusion\": \"success\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}, \"hypothesis\": \"Precomputing K=5 VLA action samples provides sufficient diversity for conformal selection while reducing inference cost by 50% vs K=10 — testing efficiency-performance tradeoff\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T06:56:12.892Z\", \"updated_at\": \"2026-05-17T03:13:39.823Z\", \"conclusion\": \"failed\", \"hypothesis\": \"ReconVLA baseline implementation validates that sample consensus (K=10 argmin Euclidean) provides meaningful improvement over single-sample VLA, establishing competitive baseline for ACR comparison\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T03:01:07.682Z\", \"updated_at\": \"2026-05-17T03:13:37.890Z\", \"conclusion\": \"failed\", \"hypothesis\": \"Initial CRM + SmolVLA integration plan validates that conformal residual module can be trained and integrated with a pretrained VLA model for action refinement\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T01:22:10.415Z\", \"updated_at\": \"2026-05-17T03:13:35.534Z\", \"conclusion\": \"success\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}, \"hypothesis\": \"MVP validation: CRM correction signals improve point-reaching accuracy in simplified task — if corrections reliably move end-effector toward targets, the mechanism transfers to full manipulation\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:35:16.236Z\", \"updated_at\": \"2026-05-17T03:13:33.197Z\", \"conclusion\": \"failed\", \"hypothesis\": \"SmolVLA pretrained model evaluates directly on LIBERO-Spatial without any CRM or conformal processing — establishing raw VLA capability as absolute floor baseline\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:10.843Z\", \"updated_at\": \"2026-05-17T03:13:04.533Z\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}, \"hypothesis\": \"Obs-only CRM trained on object benchmark generalizes to LIBERO-Spatial tasks without retraining — testing cross-benchmark transfer of visual correction signals\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:13:41.913Z\", \"updated_at\": \"2026-05-17T03:09:38.443Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"hypothesis\": \"obs_only CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 obs_only 在 uncapped norm 下的跨 seed 稳定性（seed42=17%）。如果维持 15-20%，确认极端 magnitude 鲁棒性。\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:56:58.178Z\", \"updated_at\": \"2026-05-17T03:09:30.045Z\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\", \"hypothesis\": \"perdof CRM (ε=0.05) seed=42 on LIBERO Object. 验证 perdof 在极低 norm 下是否与 obs_only 接近（两者都受限于低 norm 纠正量）。magnitude curve 低端数据点。\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:34:16.821Z\", \"updated_at\": \"2026-05-17T03:09:27.225Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"conclusion\": \"success\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=43 on LIBERO Object. 验证 perdof 在 norm=0.2 的多 seed 数据（seed42=11%）。确认 perdof 在中间 norm 的退化幅度具有跨 seed 一致性。\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:26:52.169Z\", \"updated_at\": \"2026-05-17T03:09:17.332Z\", \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=42 on LIBERO Object magnitude sweep. 验证 perdof 在 norm=0.3 的 collapse 程度。预期 SR 急剧下降（支持 progressive collapse 叙事）。\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:18.917Z\", \"updated_at\": \"2026-05-17T03:09:15.263Z\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 在 spatial 上的表现。与 object 的 0.05 数据点对比，检验 benchmark 间一致性。\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-17T03:09:11.273Z\", \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 obs_only 在 spatial 的表现（10-task SR）。验证 magnitude 效应在不同 benchmark 上的一致性。\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-17T03:09:10.586Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_only 是否仍保持 graceful degradation（对比 perdof 在同 norm 的 collapse）。\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-17T03:09:06.864Z\", \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_only 表现。如果 SR 与 VLA-only 相近（12%），说明过低 norm 约束了 CRM 纠正能力。\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T02:46:15.008Z\", \"updated_at\": \"2026-05-17T03:04:54.543Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠���价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42\", \"conclusion\": \"failed\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T02:18:02.194Z\", \"updated_at\": \"2026-05-17T02:38:55.611Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（跳过 K=10 采样+argmin 选择），测试 obs 特征鲁棒性在简化 pipeline 下是否成立。如果 SR > VLA-only (~11%)，说明 CRM 本身有独立价值；如果 SR < VLA-only，说明 selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"conclusion\": \"failed\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:11:59.390Z\", \"updated_at\": \"2026-05-16T21:29:49.586Z\", \"hypothesis\": \"Scalar CRM seed=44 on LIBERO object benchmark. Retry of failed eval-scalar-object-seed44. Expects scalar variant underperforms obs_only but may match argmin baseline.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:56:22.235Z\", \"updated_at\": \"2026-05-16T19:45:27.956Z\", \"hypothesis\": \"perdof CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 four-way comparison. seed42=11%, seed43=12%. Expected to confirm perdof < argmin.\", \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T06:05:51.470Z\", \"updated_at\": \"2026-05-16T19:37:12.898Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T14:48:54.894Z\", \"updated_at\": \"2026-05-16T15:36:08.207Z\", \"hypothesis\": \"P0 retry #4: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22%, seed43=16%. Previous attempts failed (127/129/killed).\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:32:14.163Z\", \"updated_at\": \"2026-05-16T15:34:00.414Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (EXIT_CODE=127, missing conda activate). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:14:47.376Z\", \"updated_at\": \"2026-05-16T11:30:59.542Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=45 on LIBERO object benchmark. Multi-seed magnitude curve data point. seed42 norm=0.3=19%, seed44 norm=0.3=running. Extends magnitude robustness evidence to 3rd seed.\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:11:49.844Z\", \"updated_at\": \"2026-05-16T09:00:15.290Z\", \"hypothesis\": \"v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to confirm catastrophic failure\", \"parent\": \"eval-acr-object-v4-default\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:47:32.591Z\", \"updated_at\": \"2026-05-16T08:37:12.296Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Tests perdof at smallest correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:38:22.125Z\", \"updated_at\": \"2026-05-16T07:09:01.967Z\", \"hypothesis\": \"obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default (perdof default). Tests whether obs_only robustness holds even without magnitude capping — if yes, obs_only is fundamentally more robust than perdof regardless of norm setting.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:02:31.432Z\", \"updated_at\": \"2026-05-16T06:04:05.747Z\", \"hypothesis\": \"D031: scalar_unc CRM v3-norm seed=43 on LIBERO object benchmark. Completes seed=43 six-way comparison table. scalar seed=42 was worst at 4% — seed=43 confirms.\", \"parent\": \"eval-acr-object-v4-scalar\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:47:31.254Z\", \"updated_at\": \"2026-05-16T05:56:01.541Z\", \"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object benchmark. Completes 5-point magnitude curve (0.03/0.05/0.1/0.2/0.3). Tests minimum effective correction magnitude on object domain.\", \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:02:34.914Z\", \"updated_at\": \"2026-05-16T05:25:06.306Z\", \"hypothesis\": \"scalar_unc CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. scalar seed42=9%, seed43 running (0% at 3/10). Expected worst CRM variant.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:34:30.429Z\", \"updated_at\": \"2026-05-16T04:59:20.094Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (r1 EXIT_CODE=127, r2 killed by agent). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:34:28.047Z\", \"updated_at\": \"2026-05-16T04:59:17.975Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (r1 EXIT_CODE=127, r2 killed by agent). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:46:28.667Z\", \"updated_at\": \"2026-05-16T04:53:17.141Z\", \"hypothesis\": \"D031: VLA-mean baseline (K=10, mean aggregation) seed=43 on LIBERO object benchmark. Completes seed=43 comparison table. If VLA-mean seed=43 ≈ obs_only seed=43 → CRM correction claim compressed.\", \"parent\": \"eval-vla-mean-object\", \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:19:49.586Z\", \"updated_at\": \"2026-05-16T03:15:39.287Z\", \"hypothesis\": \"D031 supplementary: perdof CRM v3-norm seed=43 on LIBERO object benchmark. Completes three-way comparison (obs_only vs argmin vs perdof) with doubled samples. If perdof seed=43 ≈ argmin seed=43 → confirms obs_only uniquely better.\", \"parent\": \"eval-acr-object-v4-perdof\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:29:00.342Z\", \"updated_at\": \"2026-05-16T01:33:29.678Z\", \"hypothesis\": \"D035 follow-up: VLA-only baseline (K=1) seed=44 on LIBERO object benchmark. Third seed reference point. seed42=12%, seed43=12%. Deployed on bjb2-40593.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:28:59.304Z\", \"updated_at\": \"2026-05-16T01:32:51.127Z\", \"hypothesis\": \"D035 follow-up: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object benchmark. Third seed for Fisher exact test. ε=0.2 is PROJECT HIGH config (seed42=22%). Paired with eval-argmin-object-seed44.\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:28:58.358Z\", \"updated_at\": \"2026-05-16T01:32:49.190Z\", \"hypothesis\": \"D035 follow-up: argmin baseline (K=10) seed=44 on LIBERO object benchmark. Third seed for Fisher exact test statistical power. Paired with eval-obs-only-object-norm02-seed44. seed42=12%, seed43=17%.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:58:46.063Z\", \"updated_at\": \"2026-05-16T00:51:14.618Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:05:41.192Z\", \"updated_at\": \"2026-05-16T00:49:21.141Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"conclusion\": \"failed\", \"notes\": \"Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had 15min more progress. Both wrote same output_file, causing potential corruption.\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:58:46.739Z\", \"updated_at\": \"2026-05-16T00:37:43.289Z\", \"hypothesis\": \"D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison.\", \"parent\": \"eval-reconvla-object\", \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:19:36.419Z\", \"updated_at\": \"2026-05-15T19:38:38.710Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:43:48.583Z\", \"updated_at\": \"2026-05-15T19:38:31.587Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm02\", \"conclusion\": \"killed\", \"notes\": \"失败原因: EXIT_CODE=127 — tmux 用 sh 执行命令，python 不在 sh PATH 中。修复: bash -c 包裹。已重试为 eval-mag-obsonly-norm03-r2。\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:26:53.269Z\", \"updated_at\": \"2026-05-15T19:34:07.651Z\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:14:01.998Z\", \"updated_at\": \"2026-05-15T19:27:30.465Z\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:13:38.067Z\", \"updated_at\": \"2026-05-15T19:27:28.479Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 occupied by P0 obs-only-norm02-seed43-r2). Director approved.\", \"parent\": \"eval-mag-obsonly-norm03-b2\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:15:19.724Z\", \"updated_at\": \"2026-05-15T19:25:28.957Z\", \"conclusion\": \"killed\", \"notes\": \"Killed during cuda:2/3 GPU cleanup on bjb2-28827 (2026-05-16). Was sharing cuda:2 with perdof norm=0.3 r2.\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:15:16.452Z\", \"updated_at\": \"2026-05-15T19:25:28.055Z\", \"conclusion\": \"killed\", \"notes\": \"GPU contention on cuda:2 (shared with perdof norm=0.2 seed=43). Killed 2026-05-16. Replaced by r3 clean restart.\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:55:02.698Z\", \"updated_at\": \"2026-05-15T19:17:41.948Z\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:55:00.179Z\", \"updated_at\": \"2026-05-15T19:17:40.199Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:07.302Z\", \"updated_at\": \"2026-05-15T19:17:39.068Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-15T19:17:37.622Z\", \"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-15T19:17:36.369Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:39:04.708Z\", \"updated_at\": \"2026-05-15T19:17:30.541Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:39:02.628Z\", \"updated_at\": \"2026-05-15T19:17:29.292Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:39:00.259Z\", \"updated_at\": \"2026-05-15T19:17:27.703Z\", \"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:11:04.275Z\", \"updated_at\": \"2026-05-15T19:17:26.396Z\", \"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:11:02.520Z\", \"updated_at\": \"2026-05-15T19:17:25.022Z\", \"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:11:01.629Z\", \"updated_at\": \"2026-05-15T19:17:23.631Z\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:58:30.091Z\", \"updated_at\": \"2026-05-15T19:13:43.549Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Migrated from bjb1-32546:cuda:4 (GPU conflict) to bjb2-28827:cuda:2. Paired with obs_only norm=0.3 for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm0p3-object\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:34:52.454Z\", \"updated_at\": \"2026-05-15T18:58:11.790Z\", \"hypothesis\": \"Retry of eval-mag-perdof-norm03-object (killed by SIGTERM). Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Paired with obs_only norm=0.3 (running) for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm03-object\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:38:18.819Z\", \"updated_at\": \"2026-05-15T18:58:10.821Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. norm=0.2 shows strongest signal (18% SR at 5/10 tasks in seed=42). Seed=43 doubling for statistical power on the best-performing configuration.\", \"parent\": \"eval-acr-object-obs-only-norm02\", \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:18:17.209Z\", \"updated_at\": \"2026-05-15T17:38:37.815Z\", \"hypothesis\": \"Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether magnitude control is essential on object domain too. If v4-default << v4-perdof (norm=0.1) → magnitude control is universally needed. If v4-default ≈ v4-perdof → spatial failure was anomalous.\", \"parent\": \"eval-acr-object-v4-perdof\", \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"notes\": \"Killed per Director instruction. 3/10 tasks all 0% SR, no magnitude control (norm≈1.42). Conclusion obvious — magnitude control is essential.\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:49:38.786Z\", \"updated_at\": \"2026-05-15T17:22:51.755Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:31:09.989Z\", \"updated_at\": \"2026-05-15T17:01:25.883Z\", \"hypothesis\": \"VLA mean baseline (K=10, mean aggregation) on LIBERO object benchmark. Matches reconvla spatial baseline but on object tasks.\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T01:48:28.744Z\", \"updated_at\": \"2026-05-15T16:25:17.101Z\", \"hypothesis\": \"ReconVLA baseline (scalar Euclidean argmin, K=10) on LIBERO object benchmark. Tests whether simple sample selection improves over VLA mean on object manipulation tasks. Provides baseline for CRM comparison on object domain.\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:53:41.689Z\", \"updated_at\": \"2026-05-15T16:23:01.718Z\", \"hypothesis\": \"D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\", \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:49:13.626Z\", \"updated_at\": \"2026-05-15T15:45:38.531Z\", \"hypothesis\": \"D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.\", \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:04.283Z\", \"updated_at\": \"2026-05-15T13:18:27.852Z\", \"hypothesis\": \"Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_unc vs obs_only.\", \"parent\": \"eval-acr-spatial-v4-scalar\", \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:05.934Z\", \"updated_at\": \"2026-05-15T11:15:11.801Z\", \"hypothesis\": \"Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.\", \"parent\": \"eval-acr-spatial-v4-obs-only-r2\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T09:09:04.411Z\", \"updated_at\": \"2026-05-15T10:01:21.065Z\", \"hypothesis\": \"D029: obs_only seed=43 复现实验。obs_only 是项目唯一存活路径。seed=42 如果确认 +5pp over argmin，seed=43 增加统计力（200 vs 200 样本下 Fisher exact p ~0.12，配合 object benchmark 独立验证有望通过）。\", \"parent\": \"eval-acr-spatial-v4-obs-only-r3\", \"notes\": \"D029: perdof spatial 35% vs argmin 34% = +1pp, kill criterion triggered. Per-DOF claim dead on spatial. obs_only 是唯一存活路径，seed=43 用于增加统计力。\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:05.220Z\", \"updated_at\": \"2026-05-15T09:10:21.153Z\", \"hypothesis\": \"Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.\", \"parent\": \"eval-acr-spatial-v4-small\", \"notes\": \"[D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:10:44.647Z\", \"updated_at\": \"2026-05-15T07:19:12.632Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"conclusion\": \"killed\", \"notes\": \"Stale duplicate entry with dots in name. Actual experiment is eval-mag-obsonly-norm-0p3-r3 (also killed). Real running experiment is eval-mag-obsonly-norm03-r2.\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:11:06.381Z\", \"updated_at\": \"2026-05-15T07:17:16.300Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"conclusion\": \"killed\", \"notes\": \"Director 撤销部署指令。r2 (PID 325264) 实际未被误杀，r3 是基于信息差的重复部署。立即 kill r3 保留 r2。\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:03.322Z\", \"updated_at\": \"2026-05-15T06:39:37.926Z\", \"hypothesis\": \"Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.\", \"parent\": \"eval-argmin-only-spatial\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\", \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:21:24.009Z\", \"updated_at\": \"2026-05-15T05:32:12.897Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.03 on spatial. Completes obs_only norm curve (have 0.05, 0.2; adding 0.03).\", \"conclusion\": \"killed\", \"notes\": \"Duplicate experiment on same GPU. pid 225144 was actually the child python process of eval-mag-obsonly-norm003-b2's wrapper (pid 225139). Not a separate experiment. Killed, restarted b2 with new pid 227426.\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:11:14.165Z\", \"updated_at\": \"2026-05-15T05:18:17.853Z\", \"hypothesis\": \"VLA-only baseline (K=1, single sample, no CRM) on LIBERO object benchmark. Lowest-bar baseline for object domain.\", \"conclusion\": \"failed\", \"notes\": \"Duplicate of eval-vla-only-object (already DONE at 12% SR). Process killed to free bjb1-32546 cuda:4.\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T01:48:09.734Z\", \"updated_at\": \"2026-05-15T03:30:05.911Z\", \"hypothesis\": \"D018-D019 验证: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42). 如果 v4-default << v4-small (max_norm=0.1) → magnitude control 是必要的。如果 v4-default ≈ baseline → normalization 独自不够。补全 bjb1 上两次失败的实验。\", \"parent\": \"eval-acr-spatial-v4-default-r2\", \"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-15T01:45:12.897Z\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:17:37.194Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"hypothesis\": \"D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1).\", \"parent\": \"eval-acr-spatial-v4-default\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:08:53.421Z\", \"updated_at\": \"2026-05-14T22:16:05.788Z\", \"hypothesis\": \"D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:08:59.906Z\", \"updated_at\": \"2026-05-14T22:08:58.490Z\", \"hypothesis\": \"D018: Input normalization alone fixes CRM correction degradation. v3-norm checkpoint with default max_correction_norm=1.42. If >30% baseline → normalization was the main fix.\", \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:01.250Z\", \"updated_at\": \"2026-05-14T22:05:42.608Z\", \"hypothesis\": \"Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization.\", \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:00.829Z\", \"updated_at\": \"2026-05-14T22:05:28.289Z\", \"hypothesis\": \"Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features.\", \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:45:12.565Z\", \"updated_at\": \"2026-05-14T20:05:22.677Z\", \"hypothesis\": \"D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning\", \"parent\": \"crm-train-v3-perdof\", \"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:37:14.400Z\", \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:37:04.316Z\", \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:37:02.631Z\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:49:43.787Z\", \"updated_at\": \"2026-05-14T17:47:54.523Z\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:08.413Z\", \"updated_at\": \"2026-05-14T17:47:53.188Z\", \"conclusion\": \"killed\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:48:40.837Z\", \"updated_at\": \"2026-05-14T07:59:32.676Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:56:28.643Z\", \"updated_at\": \"2026-05-14T07:59:31.277Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}}, \"crm-train-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:10:36.535Z\", \"updated_at\": \"2026-05-14T07:59:30.290Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}}, \"crm-train-k5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:42:55.911Z\", \"updated_at\": \"2026-05-14T07:59:29.396Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:54:30.549Z\", \"updated_at\": \"2026-05-14T07:52:44.766Z\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-14T07:52:43.327Z\", \"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:14:23.092Z\", \"updated_at\": \"2026-05-14T07:52:43.134Z\", \"conclusion\": \"killed\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:03:35.642Z\", \"updated_at\": \"2026-05-14T01:45:48.892Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:04:28.766Z\", \"updated_at\": \"2026-05-14T00:05:22.619Z\", \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-14T00:04:26.792Z\", \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:56:40.287Z\", \"updated_at\": \"2026-05-13T23:14:22.561Z\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:54:28.535Z\", \"updated_at\": \"2026-05-13T23:12:11.315Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T23:12:10.958Z\", \"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T23:12:10.037Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:16:58.052Z\", \"updated_at\": \"2026-05-13T23:12:09.066Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:38:57.194Z\", \"updated_at\": \"2026-05-13T19:09:00.612Z\", \"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:08:51.171Z\", \"updated_at\": \"2026-05-13T16:14:40.934Z\", \"conclusion\": \"killed\"}}, \"count\": 523, \"total\": 523, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5905}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_01UVKCJ2j85AiUTabcvgpgrp`</summary>

```json
{
  "command": "FILE=/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt\npython3 <<'EOF'\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt') as f:\n    obj = json.load(f)\ninner = json.loads(obj['result'])\ndata = inner['data']\nprint('top:', type(data), 'len:', len(data) if hasattr(data,'__len__') else '-')\nif isinstance(data, list):\n    print('first item keys:', list(data[0].keys())[:30])\n    print('total experiments:', len(data))\nEOF",
  "description": "Probe registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "079ab8da-52f4-4b1f-91c7-6c0ddbdcb307",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0165smiRw2ipfJp23QrUf9Hc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 113503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 804
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

_source line 85 · 2026-05-21T16:40:24.279Z_

<details><summary>↩ Tool result · `toolu_01UVKCJ2j85AiUTabcvgpgrp`</summary>

```text
top: &lt;class 'dict'> len: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "9dbb82d2-d520-4c6a-9a94-c66c2d6795c2",
  "tool_use_result": {
    "stdout": "top: &lt;class 'dict'> len: 4",
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

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_01NAbX1CdYZQK96TZSFjjzJk`</summary>

```json
{
  "command": "python3 <<'EOF'\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt') as f:\n    obj = json.load(f)\ninner = json.loads(obj['result'])\ndata = inner['data']\nprint('keys:', list(data.keys()))\nfor k,v in data.items():\n    print(k, type(v), len(v) if hasattr(v,'__len__') else v)\nEOF",
  "description": "Inspect dict keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "eec158ef-d721-4178-9fb4-f26aa38d5a87",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MuwufCEhmjmFUSeDKB1Tgx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 114307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 505
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

_source line 87 · 2026-05-21T16:40:28.855Z_

<details><summary>↩ Tool result · `toolu_01NAbX1CdYZQK96TZSFjjzJk`</summary>

```text
keys: ['experiments', 'count', 'total', 'baseline']
experiments &lt;class 'dict'> 523
count &lt;class 'int'> 523
total &lt;class 'int'> 523
baseline &lt;class 'NoneType'> None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "48c44539-04d2-4578-8e12-c74ea0fc9cd2",
  "tool_use_result": {
    "stdout": "keys: ['experiments', 'count', 'total', 'baseline']\nexperiments &lt;class 'dict'> 523\ncount &lt;class 'int'> 523\ntotal &lt;class 'int'> 523\nbaseline &lt;class 'NoneType'> None",
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

_source line 88_

<details open><summary>🔧 Tool call — Bash · `toolu_015do9pANArt9S19MpLvLWZN`</summary>

```json
{
  "command": "python3 <<'EOF'\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt') as f:\n    obj = json.load(f)\nexps = json.loads(obj['result'])['data']['experiments']\n# Show example experiment\nfirst_key = next(iter(exps))\nprint('Example key:', first_key)\nprint('Example fields:', list(exps[first_key].keys()))\nprint(json.dumps(exps[first_key], indent=2)[:1500])\nEOF",
  "description": "Inspect experiment fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "3da20578-929d-4459-b445-58778e513856",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DbV96KXm816vF4ZkjPqCgU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 114812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 89 · 2026-05-21T16:40:34.018Z_

<details><summary>↩ Tool result · `toolu_015do9pANArt9S19MpLvLWZN`</summary>

```text
Example key: eval-pi05-vla-only-spatial-seed45
Example fields: ['status', 'created_at', 'updated_at', 'hypothesis', 'metrics', 'conclusion']
{
  "status": "DONE",
  "created_at": "2026-05-21T11:51:32.435Z",
  "updated_at": "2026-05-21T12:22:59.643Z",
  "hypothesis": "\u03c00.5 VLA-only baseline on LIBERO-Spatial seed45 with patched lerobot (VT key remap), cross-VLA validation of CRM",
  "metrics": {
    "success_rate": 0.85,
    "n_tasks": 10,
    "total_rollouts": 200
  },
  "conclusion": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "8cf473c0-5f84-4ee9-937e-5cfe21494392",
  "tool_use_result": {
    "stdout": "Example key: eval-pi05-vla-only-spatial-seed45\nExample fields: ['status', 'created_at', 'updated_at', 'hypothesis', 'metrics', 'conclusion']\n{\n  \"status\": \"DONE\",\n  \"created_at\": \"2026-05-21T11:51:32.435Z\",\n  \"updated_at\": \"2026-05-21T12:22:59.643Z\",\n  \"hypothesis\": \"\\u03c00.5 VLA-only baseline on LIBERO-Spatial seed45 with patched lerobot (VT key remap), cross-VLA validation of CRM\",\n  \"metrics\": {\n    \"success_rate\": 0.85,\n    \"n_tasks\": 10,\n    \"total_rollouts\": 200\n  },\n  \"conclusion\": \"success\"\n}",
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

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_01RxKGRGFbNK1LsscTAbgoKC`</summary>

```json
{
  "command": "python3 <<'EOF'\nimport json, re\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt') as f:\n    obj = json.load(f)\nexps = json.loads(obj['result'])['data']['experiments']\n\ndef find(pat):\n    out = []\n    for k,v in exps.items():\n        if re.search(pat, k):\n            sr = v.get('metrics',{}).get('success_rate', '-')\n            out.append((k, sr, v.get('status'), v.get('conclusion')))\n    return out\n\n# Look at key categories\npatterns = [\n    'plan-a.*object|adaptive-conformal.*object|adaptive_conformal_crm.*object|plana.*object',\n    'plan-a.*spatial|adaptive.*spatial|adaptive_conformal_crm.*spatial|plana.*spatial',\n    'eval-vla-only.*object',\n    'eval-vla-only.*spatial',\n    'eval-crm-obs.*object.*k10|eval-crm-obs.*k10.*object|eval-obs.*k10',\n    'eval-crm-obs.*spatial',\n    'pi05',\n    'random.*object',\n    'random.*spatial',\n    'argmin.*k5|argmin.*k10',\n    'adaptive.*p25|adaptive.*p50|adaptive.*p75|adaptive.*p90',\n]\nfor p in patterns:\n    print('\\n==', p)\n    rs = find(p)\n    for r in rs[:40]:\n        print(' ', r)\n    if len(rs) > 40: print('  ...', len(rs)-40, 'more')\nEOF",
  "description": "Survey registry by pattern"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "122a72f3-148e-46c1-a9bc-b71c7d1d1cd5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FY4YmyjP8qafGnxiuEQpqE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 115223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 623
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

_source line 91 · 2026-05-21T16:40:44.182Z_

<details><summary>↩ Tool result · `toolu_01RxKGRGFbNK1LsscTAbgoKC`</summary>

```text
== plan-a.*object|adaptive-conformal.*object|adaptive_conformal_crm.*object|plana.*object
  ('eval-plan-a-object-seed42', 0.19, 'DONE', 'success')
  ('eval-plan-a-object-seed44', 0.2, 'DONE', 'success')
  ('eval-plan-a-object-seed43', 0.16, 'DONE', 'success')

== plan-a.*spatial|adaptive.*spatial|adaptive_conformal_crm.*spatial|plana.*spatial
  ('eval-adaptive-k-spatial-p90-seed44-bjb2', '-', 'DONE', 'failed')
  ('eval-plan-a-spatial-seed43', 0.35, 'DONE', 'success')
  ('eval-plan-a-spatial-seed42', 0.34, 'DONE', 'success')
  ('eval-plan-a-spatial-seed44', 0.36, 'DONE', 'success')
  ('eval-adaptive-k-spatial-p90-seed44', 0.36, 'DONE', 'success')
  ('eval-adaptive-k-spatial-p75-seed44', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p25-seed44', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p90-seed43', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p90-seed42', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p50-seed44', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p50-seed43', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p50-seed42', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p25-seed42', '-', 'DONE', 'negative')
  ('eval-adaptive-k-spatial-p25-seed43', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p75-seed43', 34, 'DONE', 'success')
  ('eval-adaptive-k-spatial-p75-seed42', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p50-seed44-r2', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p50-seed43-r2', '-', 'DONE', 'success')

== eval-vla-only.*object
  ('eval-vla-only-object-seed50', '-', 'DONE', 'success')
  ('eval-vla-only-object-seed49', '-', 'DONE', 'success')
  ('eval-vla-only-object-seed48', '-', 'DONE', 'success')
  ('eval-vla-only-object-seed46', '-', 'DONE', 'success')
  ('eval-vla-only-object-seed45', '-', 'DONE', 'success')
  ('eval-vla-only-object-seed44-r2', '-', 'DONE', 'success')
  ('eval-vla-only-object-seed43', '-', 'DONE', 'success')
  ('eval-vla-only-object', '-', 'DONE', 'success')
  ('eval-vla-only-object-seed48-r2', 0.11, 'DONE', 'success')
  ('eval-vla-only-object-seed47', '-', 'DONE', 'success')
  ('eval-vla-only-object-seed45-r2', '-', 'DONE', 'success')
  ('eval-vla-only-object-seed44', '-', 'DONE', 'failed')
  ('eval-vla-only-object-k1', '-', 'DONE', 'failed')

== eval-vla-only.*spatial
  ('eval-vla-only-spatial-seed48', '-', 'DONE', 'success')
  ('eval-vla-only-spatial-seed47', '-', 'DONE', 'success')
  ('eval-vla-only-spatial-seed49', '-', 'DONE', 'failed')
  ('eval-vla-only-spatial-seed46', '-', 'DONE', 'success')
  ('eval-vla-only-spatial-seed45', 0.27, 'DONE', 'success')
  ('eval-vla-only-spatial-seed44', 0.31, 'DONE', 'success')
  ('eval-vla-only-spatial-seed43', 0.29, 'DONE', 'success')
  ('eval-vla-only-spatial-seed42', 0.3, 'DONE', 'success')

== eval-crm-obs.*object.*k10|eval-crm-obs.*k10.*object|eval-obs.*k10

== eval-crm-obs.*spatial

== pi05
  ('eval-pi05-vla-only-spatial-seed45', 0.85, 'DONE', 'success')
  ('eval-pi05-vla-only-spatial-seed43-r3', 0.83, 'DONE', 'success')
  ('eval-pi05-vla-only-spatial-seed42-r3', 0.845, 'DONE', 'success')
  ('eval-pi05-vla-only-object-seed44-r3', 0.81, 'DONE', 'success')
  ('eval-pi05-vla-only-object-seed43-r3', 0.815, 'DONE', 'success')
  ('eval-pi05-vla-only-object-seed42-r3', 0.82, 'DONE', 'success')
  ('eval-pi05-vla-only-object-seed44', '-', 'DONE', 'failed')
  ('eval-pi05-vla-only-object-seed43', '-', 'DONE', 'failed')
  ('eval-pi05-vla-only-object-seed42', '-', 'DONE', 'failed')
  ('eval-pi05-vla-only-spatial-seed44', '-', 'DONE', 'failed')
  ('eval-pi05-vla-only-spatial-seed43', '-', 'DONE', 'failed')
  ('eval-pi05-vla-only-spatial-seed42', '-', 'DONE', 'failed')
  ('eval-pi05-baseline-object-seed42', '-', 'DONE', 'failed')

== random.*object
  ('eval-random-selection-object-seed44', '-', 'DONE', 'success')
  ('eval-random-selection-object-seed43', 0.09, 'DONE', 'success')
  ('eval-random-selection-object-seed49', 0.12, 'DONE', 'success')
  ('eval-random-selection-object-seed48', 0.1, 'DONE', 'success')
  ('eval-random-selection-object-seed46-r3', '-', 'DONE', 'success')
  ('eval-random-selection-object-seed47', '-', 'DONE', 'success')
  ('eval-random-selection-object-seed46-r2', '-', 'DONE', 'failed')
  ('eval-random-selection-object-seed46', '-', 'DONE', 'failed')
  ('eval-random-selection-object-seed45', 0.1, 'DONE', 'success')
  ('eval-random-selection-object-seed42', 0.11, 'DONE', 'success')
  ('eval-random-selection-object-k5-seed45-r2', 0.07, 'DONE', 'success')
  ('eval-random-selection-object-k5-seed44-r2', 0.1, 'DONE', 'success')
  ('eval-random-selection-object-k5-seed43-r2', 0.11, 'DONE', 'success')
  ('eval-random-selection-object-k5-seed42-r2', 0.14, 'DONE', 'success')
  ('eval-random-selection-object-k5-seed45', '-', 'DONE', 'failed')
  ('eval-random-selection-object-k5-seed44', '-', 'DONE', 'failed')
  ('eval-random-selection-object-k5-seed43', '-', 'DONE', 'failed')
  ('eval-random-selection-object-k5-seed42', '-', 'DONE', 'failed')

== random.*spatial
  ('eval-random-selection-spatial-seed42-r3', 0.34, 'DONE', 'success')
  ('eval-random-selection-spatial-seed43-r2', '-', 'DONE', 'success')
  ('eval-random-selection-spatial-seed44', '-', 'DONE', 'success')
  ('eval-random-selection-spatial-seed43', '-', 'DONE', 'success')
  ('eval-random-selection-spatial-seed42-r2', '-', 'DONE', 'success')
  ('eval-random-selection-spatial-seed42', '-', 'DONE', 'failed')

== argmin.*k5|argmin.*k10
  ('eval-argmin-object-k5-seed44-r2', '-', 'DONE', 'success')
  ('eval-argmin-object-k5-seed44', '-', 'DONE', 'failed')
  ('eval-argmin-object-k5-seed42', '-', 'DONE', 'success')
  ('eval-argmin-object-k5-seed45', '-', 'DONE', 'success')
  ('eval-argmin-object-k5-seed43', '-', 'DONE', 'success')

== adaptive.*p25|adaptive.*p50|adaptive.*p75|adaptive.*p90
  ('eval-adaptive-k-spatial-p90-seed44-bjb2', '-', 'DONE', 'failed')
  ('eval-adaptive-k-spatial-p90-seed44', 0.36, 'DONE', 'success')
  ('eval-adaptive-k-spatial-p75-seed44', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p25-seed44', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p90-seed43', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p90-seed42', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p50-seed44', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p50-seed43', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p50-seed42', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p25-seed42', '-', 'DONE', 'negative')
  ('eval-adaptive-k-spatial-p25-seed43', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p75-seed43', 34, 'DONE', 'success')
  ('eval-adaptive-k-spatial-p75-seed42', '-', 'DONE', 'success')
  ('eval-adaptive-k-spatial-p50-seed44-r2', '-', 'DONE', 'success')
  ('eval-adaptive-k-p75-seed42', 0.12, 'DONE', 'success')
  ('eval-adaptive-k-p75-seed43', 0.13, 'DONE', 'success')
  ('eval-adaptive-k-p50-seed42', 0.16, 'DONE', 'success')
  ('eval-adaptive-k-p50-seed43', 0.16, 'DONE', 'success')
  ('eval-adaptive-k-spatial-p50-seed43-r2', '-', 'DONE', 'success')
  ('eval-adaptive-k-p90-seed44', 0.14, 'DONE', 'success')
  ('eval-adaptive-k-p25-seed43', 0.13, 'DONE', 'success')
  ('eval-adaptive-k-p25-seed44-r2', 0.15, 'DONE', 'success')
  ('eval-adaptive-k-p25-seed42', 0.15, 'DONE', 'success')
  ('eval-adaptive-k-p50-seed44', 0.14, 'DONE', 'success')
  ('eval-adaptive-k-p75-seed44', 0.16, 'DONE', 'success')
  ('eval-adaptive-k-p90-seed43', 0.14, 'DONE', 'success')
  ('eval-adaptive-k-p90-seed42', 0.12, 'DONE', 'success')
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "a15d708d-542c-43c4-98d3-7804d0cb678e",
  "tool_use_result": {
    "stdout": "== plan-a.*object|adaptive-conformal.*object|adaptive_conformal_crm.*object|plana.*object\n  ('eval-plan-a-object-seed42', 0.19, 'DONE', 'success')\n  ('eval-plan-a-object-seed44', 0.2, 'DONE', 'success')\n  ('eval-plan-a-object-seed43', 0.16, 'DONE', 'success')\n\n== plan-a.*spatial|adaptive.*spatial|adaptive_conformal_crm.*spatial|plana.*spatial\n  ('eval-adaptive-k-spatial-p90-seed44-bjb2', '-', 'DONE', 'failed')\n  ('eval-plan-a-spatial-seed43', 0.35, 'DONE', 'success')\n  ('eval-plan-a-spatial-seed42', 0.34, 'DONE', 'success')\n  ('eval-plan-a-spatial-seed44', 0.36, 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p90-seed44', 0.36, 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p75-seed44', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p25-seed44', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p90-seed43', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p90-seed42', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p50-seed44', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p50-seed43', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p50-seed42', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p25-seed42', '-', 'DONE', 'negative')\n  ('eval-adaptive-k-spatial-p25-seed43', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p75-seed43', 34, 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p75-seed42', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p50-seed44-r2', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p50-seed43-r2', '-', 'DONE', 'success')\n\n== eval-vla-only.*object\n  ('eval-vla-only-object-seed50', '-', 'DONE', 'success')\n  ('eval-vla-only-object-seed49', '-', 'DONE', 'success')\n  ('eval-vla-only-object-seed48', '-', 'DONE', 'success')\n  ('eval-vla-only-object-seed46', '-', 'DONE', 'success')\n  ('eval-vla-only-object-seed45', '-', 'DONE', 'success')\n  ('eval-vla-only-object-seed44-r2', '-', 'DONE', 'success')\n  ('eval-vla-only-object-seed43', '-', 'DONE', 'success')\n  ('eval-vla-only-object', '-', 'DONE', 'success')\n  ('eval-vla-only-object-seed48-r2', 0.11, 'DONE', 'success')\n  ('eval-vla-only-object-seed47', '-', 'DONE', 'success')\n  ('eval-vla-only-object-seed45-r2', '-', 'DONE', 'success')\n  ('eval-vla-only-object-seed44', '-', 'DONE', 'failed')\n  ('eval-vla-only-object-k1', '-', 'DONE', 'failed')\n\n== eval-vla-only.*spatial\n  ('eval-vla-only-spatial-seed48', '-', 'DONE', 'success')\n  ('eval-vla-only-spatial-seed47', '-', 'DONE', 'success')\n  ('eval-vla-only-spatial-seed49', '-', 'DONE', 'failed')\n  ('eval-vla-only-spatial-seed46', '-', 'DONE', 'success')\n  ('eval-vla-only-spatial-seed45', 0.27, 'DONE', 'success')\n  ('eval-vla-only-spatial-seed44', 0.31, 'DONE', 'success')\n  ('eval-vla-only-spatial-seed43', 0.29, 'DONE', 'success')\n  ('eval-vla-only-spatial-seed42', 0.3, 'DONE', 'success')\n\n== eval-crm-obs.*object.*k10|eval-crm-obs.*k10.*object|eval-obs.*k10\n\n== eval-crm-obs.*spatial\n\n== pi05\n  ('eval-pi05-vla-only-spatial-seed45', 0.85, 'DONE', 'success')\n  ('eval-pi05-vla-only-spatial-seed43-r3', 0.83, 'DONE', 'success')\n  ('eval-pi05-vla-only-spatial-seed42-r3', 0.845, 'DONE', 'success')\n  ('eval-pi05-vla-only-object-seed44-r3', 0.81, 'DONE', 'success')\n  ('eval-pi05-vla-only-object-seed43-r3', 0.815, 'DONE', 'success')\n  ('eval-pi05-vla-only-object-seed42-r3', 0.82, 'DONE', 'success')\n  ('eval-pi05-vla-only-object-seed44', '-', 'DONE', 'failed')\n  ('eval-pi05-vla-only-object-seed43', '-', 'DONE', 'failed')\n  ('eval-pi05-vla-only-object-seed42', '-', 'DONE', 'failed')\n  ('eval-pi05-vla-only-spatial-seed44', '-', 'DONE', 'failed')\n  ('eval-pi05-vla-only-spatial-seed43', '-', 'DONE', 'failed')\n  ('eval-pi05-vla-only-spatial-seed42', '-', 'DONE', 'failed')\n  ('eval-pi05-baseline-object-seed42', '-', 'DONE', 'failed')\n\n== random.*object\n  ('eval-random-selection-object-seed44', '-', 'DONE', 'success')\n  ('eval-random-selection-object-seed43', 0.09, 'DONE', 'success')\n  ('eval-random-selection-object-seed49', 0.12, 'DONE', 'success')\n  ('eval-random-selection-object-seed48', 0.1, 'DONE', 'success')\n  ('eval-random-selection-object-seed46-r3', '-', 'DONE', 'success')\n  ('eval-random-selection-object-seed47', '-', 'DONE', 'success')\n  ('eval-random-selection-object-seed46-r2', '-', 'DONE', 'failed')\n  ('eval-random-selection-object-seed46', '-', 'DONE', 'failed')\n  ('eval-random-selection-object-seed45', 0.1, 'DONE', 'success')\n  ('eval-random-selection-object-seed42', 0.11, 'DONE', 'success')\n  ('eval-random-selection-object-k5-seed45-r2', 0.07, 'DONE', 'success')\n  ('eval-random-selection-object-k5-seed44-r2', 0.1, 'DONE', 'success')\n  ('eval-random-selection-object-k5-seed43-r2', 0.11, 'DONE', 'success')\n  ('eval-random-selection-object-k5-seed42-r2', 0.14, 'DONE', 'success')\n  ('eval-random-selection-object-k5-seed45', '-', 'DONE', 'failed')\n  ('eval-random-selection-object-k5-seed44', '-', 'DONE', 'failed')\n  ('eval-random-selection-object-k5-seed43', '-', 'DONE', 'failed')\n  ('eval-random-selection-object-k5-seed42', '-', 'DONE', 'failed')\n\n== random.*spatial\n  ('eval-random-selection-spatial-seed42-r3', 0.34, 'DONE', 'success')\n  ('eval-random-selection-spatial-seed43-r2', '-', 'DONE', 'success')\n  ('eval-random-selection-spatial-seed44', '-', 'DONE', 'success')\n  ('eval-random-selection-spatial-seed43', '-', 'DONE', 'success')\n  ('eval-random-selection-spatial-seed42-r2', '-', 'DONE', 'success')\n  ('eval-random-selection-spatial-seed42', '-', 'DONE', 'failed')\n\n== argmin.*k5|argmin.*k10\n  ('eval-argmin-object-k5-seed44-r2', '-', 'DONE', 'success')\n  ('eval-argmin-object-k5-seed44', '-', 'DONE', 'failed')\n  ('eval-argmin-object-k5-seed42', '-', 'DONE', 'success')\n  ('eval-argmin-object-k5-seed45', '-', 'DONE', 'success')\n  ('eval-argmin-object-k5-seed43', '-', 'DONE', 'success')\n\n== adaptive.*p25|adaptive.*p50|adaptive.*p75|adaptive.*p90\n  ('eval-adaptive-k-spatial-p90-seed44-bjb2', '-', 'DONE', 'failed')\n  ('eval-adaptive-k-spatial-p90-seed44', 0.36, 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p75-seed44', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p25-seed44', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p90-seed43', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p90-seed42', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p50-seed44', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p50-seed43', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p50-seed42', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p25-seed42', '-', 'DONE', 'negative')\n  ('eval-adaptive-k-spatial-p25-seed43', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p75-seed43', 34, 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p75-seed42', '-', 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p50-seed44-r2', '-', 'DONE', 'success')\n  ('eval-adaptive-k-p75-seed42', 0.12, 'DONE', 'success')\n  ('eval-adaptive-k-p75-seed43', 0.13, 'DONE', 'success')\n  ('eval-adaptive-k-p50-seed42', 0.16, 'DONE', 'success')\n  ('eval-adaptive-k-p50-seed43', 0.16, 'DONE', 'success')\n  ('eval-adaptive-k-spatial-p50-seed43-r2', '-', 'DONE', 'success')\n  ('eval-adaptive-k-p90-seed44', 0.14, 'DONE', 'success')\n  ('eval-adaptive-k-p25-seed43', 0.13, 'DONE', 'success')\n  ('eval-adaptive-k-p25-seed44-r2', 0.15, 'DONE', 'success')\n  ('eval-adaptive-k-p25-seed42', 0.15, 'DONE', 'success')\n  ('eval-adaptive-k-p50-seed44', 0.14, 'DONE', 'success')\n  ('eval-adaptive-k-p75-seed44', 0.16, 'DONE', 'success')\n  ('eval-adaptive-k-p90-seed43', 0.14, 'DONE', 'success')\n  ('eval-adaptive-k-p90-seed42', 0.12, 'DONE', 'success')",
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

_source line 92_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "e3934f8d-bce9-4c7a-bca9-4f96a22b5406",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UPisQ3i2ygsuDUfVrcgihV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4980,
      "cache_read_input_tokens": 115846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4980
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


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01Su3dReBfDy6pL23kQY3Zfp`</summary>

```json
{
  "command": "python3 <<'EOF'\nimport json, re, statistics\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt') as f:\n    obj = json.load(f)\nexps = json.loads(obj['result'])['data']['experiments']\n\n# Surface all keys with detailed metric structure where available\ndef metric(e, key='success_rate'):\n    m = e.get('metrics') or {}\n    return m.get(key)\n\n# Look for specific groups, both 'success' and 'failed' to see all numeric values\ndef grab(rx, expand=False):\n    rows = []\n    for k,v in exps.items():\n        if re.search(rx,k):\n            sr = metric(v)\n            rows.append((k, sr, v.get('conclusion'), v.get('status'), v.get('metrics') if expand else None))\n    return rows\n\nprint('=== OpenVLA ===')\nfor r in grab('openvla'):\n    print(r[:4])\n\nprint('\\n=== K=20 obs_only Object ===')\nfor r in grab('k20|k=20'):\n    print(r[:4])\n\nprint('\\n=== K=1 CRM ACCG ===')\nfor r in grab('crm.*k1[^0]|accg|k1-eval|eval-k1'):\n    print(r[:4])\n\nprint('\\n=== Plan A pi05 ===')\nfor r in grab('pi05.*plan|plan.*pi05|adaptive.*pi05'):\n    print(r[:4])\n\nprint('\\n=== Argmin K10 Object ===')\nfor r in grab('argmin.*object'):\n    print(r[:4])\n\nprint('\\n=== CRM perdof / scalar ===')\nfor r in grab('perdof|scalar'):\n    print(r[:4])\n\nprint('\\n=== Magnitude / epsilon ===')\nfor r in grab('eps0|epsilon|magnitude'):\n    print(r[:4])\n\nprint('\\n=== LTO ===')\nfor r in grab('lto'):\n    print(r[:4])\nEOF",
  "description": "Probe more registry categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "eed4729d-9ad1-4505-b017-76f0bcb87e33",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UPisQ3i2ygsuDUfVrcgihV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4980,
      "cache_read_input_tokens": 115846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4980
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

_source line 94 · 2026-05-21T16:41:21.386Z_

<details><summary>↩ Tool result · `toolu_01Su3dReBfDy6pL23kQY3Zfp`</summary>

```text
=== OpenVLA ===
('eval-openvla-crm-object-seed42', 0, 'negative', 'DONE')
('train-crm-openvla-obs-only', None, 'success', 'DONE')
('openvla-precompute-k1', None, 'success', 'DONE')
('eval-openvla-object-baseline-seed42', None, 'killed', 'DONE')
('eval-openvla-object-vla-only-seed42', None, 'negative', 'DONE')
('eval-openvla-object-vla-only-seed42-v2', None, 'success', 'DONE')

=== K=20 obs_only Object ===
('eval-k20-obs-only-spatial-seed44', None, 'success', 'DONE')
('eval-k20-obs-only-spatial-seed43', None, 'success', 'DONE')
('eval-k20-obs-only-spatial-seed42', None, 'success', 'DONE')
('eval-k20-obs-only-object-seed45', None, 'success', 'DONE')
('eval-k20-obs-only-object-seed44', None, 'success', 'DONE')
('eval-k20-obs-only-object-seed43', None, 'success', 'DONE')
('eval-k20-obs-only-object-seed42', None, 'success', 'DONE')
('eval-crm-object-k20-seed44', None, 'success', 'DONE')
('eval-crm-object-k20-seed42', None, 'success', 'DONE')
('eval-crm-object-k20-seed43', None, 'success', 'DONE')

=== K=1 CRM ACCG ===
('eval-crm-k1-object-seed43-plan702', None, 'success', 'DONE')
('eval-crm-k1-object-seed42-plan702', None, 'success', 'DONE')
('eval-crm-k1-object-seed44-plan702', None, 'success', 'DONE')
('eval-crm-k1-object-seed44-plan702-r2', None, 'killed', 'DONE')
('eval-crm-k1-object-seed43-plan702-r2', None, 'killed', 'DONE')
('eval-crm-k1-object-seed42-plan702-r2', None, 'killed', 'DONE')
('train-crm-k1-accg-object-seed42-full', None, 'success', 'DONE')
('plan_701-crm-k1-train', None, 'success', 'DONE')
('eval-k1-crm-multiscale-object-seed44-r2', None, 'negative', 'DONE')
('eval-k1-crm-multiscale-object-seed44', None, 'negative', 'DONE')
('eval-k1-crm-multiscale-object-seed43', None, 'negative', 'DONE')
('eval-k1-crm-multiscale-object-seed42', None, 'negative', 'DONE')
('eval-k1-crm-multiscale-object-seed43-r2', None, 'negative', 'DONE')
('train-crm-k1-accg-object-seed42-v2', None, 'success', 'DONE')
('eval-k1-crm-accg-object-seed44', None, 'negative', 'DONE')
('eval-k1-crm-accg-object-seed43', None, 'negative', 'DONE')
('eval-k1-crm-accg-object-seed42', None, 'negative', 'DONE')
('train-crm-k1-accg-object-seed42-fallback', None, 'success', 'DONE')
('train-crm-k1-accg-object-seed42', None, 'failed', 'DONE')

=== Plan A pi05 ===

=== Argmin K10 Object ===
('eval-argmin-object-seed50', None, 'success', 'DONE')
('eval-argmin-object-k5-seed44-r2', None, 'success', 'DONE')
('eval-argmin-object-seed49', None, 'success', 'DONE')
('eval-argmin-object-seed48', 0.15, 'success', 'DONE')
('eval-argmin-object-k5-seed44', None, 'failed', 'DONE')
('eval-argmin-object-k5-seed42', None, 'success', 'DONE')
('eval-argmin-object-k5-seed45', None, 'success', 'DONE')
('eval-argmin-object-k5-seed43', None, 'success', 'DONE')
('eval-argmin-object-seed47', None, 'success', 'DONE')
('eval-argmin-object-seed46', None, 'success', 'DONE')
('eval-argmin-object-seed45', None, 'success', 'DONE')
('eval-argmin-object-seed44-r2', None, 'success', 'DONE')
('eval-argmin-object-seed44-r3', None, 'killed', 'DONE')
('eval-argmin-object-seed44', None, 'failed', 'DONE')
('eval-argmin-object-seed43', None, 'success', 'DONE')

=== CRM perdof / scalar ===
('eval-perdof-object-norm02-seed50', 0.1, 'negative', 'DONE')
('eval-perdof-object-norm02-seed49', None, 'success', 'DONE')
('eval-perdof-object-norm02-seed48', None, 'success', 'DONE')
('eval-perdof-object-norm02-seed45-r3', None, 'success', 'DONE')
('eval-perdof-object-norm003-seed47', None, 'success', 'DONE')
('eval-perdof-object-norm005-seed47', None, 'success', 'DONE')
('eval-perdof-object-norm005-seed45-r2', 0.1, 'success', 'DONE')
('eval-perdof-object-norm01-seed43', None, 'success', 'DONE')
('eval-perdof-object-norm03-seed43', None, 'success', 'DONE')
('eval-perdof-object-norm003-seed48', 0.13, 'success', 'DONE')
('eval-scalar-object-seed45-r2', None, 'negative', 'DONE')
('eval-perdof-object-default-seed47', 0, 'negative', 'DONE')
('eval-perdof-object-norm03-seed47', 0.05, 'success', 'DONE')
('eval-perdof-object-norm003-seed46', 0.09, 'success', 'DONE')
('eval-perdof-object-norm005-seed46', 0.11, 'success', 'DONE')
('eval-perdof-object-norm003-seed45', None, 'killed', 'DONE')
('eval-perdof-object-norm01-seed48', 0.12, 'success', 'DONE')
('eval-perdof-object-norm03-seed46', 0.04, 'success', 'DONE')
('eval-scalar-object-seed46', 0.09, 'success', 'DONE')
('eval-perdof-object-norm03-seed48', None, 'killed', 'DONE')
('eval-perdof-object-norm003-seed43', None, 'success', 'DONE')
('eval-perdof-object-norm005-seed43', 0.13, 'success', 'DONE')
('eval-perdof-object-default-seed43', 0, 'success', 'DONE')
('eval-perdof-object-default-seed45', 0, 'success', 'DONE')
('eval-perdof-object-norm005-seed45', None, 'failed', 'DONE')
('eval-perdof-object-norm003-seed44-r2', None, 'failed', 'DONE')
('eval-perdof-object-norm005-seed44', 0.09, 'success', 'DONE')
('eval-perdof-object-norm003-seed44', None, 'failed', 'DONE')
('eval-perdof-object-norm01-seed42-r2', None, 'failed', 'DONE')
('eval-perdof-object-norm02-seed43', 0.09, 'success', 'DONE')
('eval-perdof-object-norm01-seed46', None, 'negative', 'DONE')
('eval-perdof-object-default-seed46', None, 'negative', 'DONE')
('eval-perdof-object-default-seed44', None, 'negative', 'DONE')
('eval-mag-perdof-norm02', None, 'killed', 'DONE')
('eval-acr-spatial-v4-scalar', None, 'killed', 'DONE')
('eval-perdof-object-norm02-seed47', None, 'success', 'DONE')
('eval-perdof-object-norm02-seed46', None, 'success', 'DONE')
('eval-perdof-object-norm02-seed43-r3', None, 'success', 'DONE')
('mag_perdof_norm02_seed43_r3', None, 'killed', 'DONE')
('eval-perdof-object-norm01-seed47-bjb1', None, 'success', 'DONE')
('eval-perdof-object-norm01-seed46-r2', None, 'success', 'DONE')
('eval-perdof-object-norm02-seed45-r2', None, 'killed', 'DONE')
('eval-scalar-object-seed45', None, 'success', 'DONE')
('eval-perdof-object-norm02-seed45', None, 'success', 'DONE')
('eval-perdof-object-norm02-seed44', None, 'success', 'DONE')
('eval-perdof-object-norm02-seed45-deploy', None, 'killed', 'DONE')
('eval-perdof-object-norm03-seed45-r2', None, 'negative', 'DONE')
('eval-perdof-object-norm03-seed44-r2', 0.04, 'negative', 'DONE')
('eval-perdof-object-norm03-seed46-r2', None, 'killed', 'DONE')
('eval-perdof-object-norm01-seed44', None, 'negative', 'DONE')
('eval-perdof-object-norm01-seed45', None, 'success', 'DONE')
('eval-perdof-object-norm01-seed47', None, 'killed', 'DONE')
('eval-perdof-object-norm03-seed44', 0.04, 'negative', 'DONE')
('eval-mag-perdof-norm02-object', None, 'negative', 'DONE')
('eval-acr-object-v4-scalar', None, 'negative', 'DONE')
('eval-mag-perdof-norm03', None, 'negative', 'DONE')
('eval-mag-perdof-norm005', None, 'negative', 'DONE')
('eval-mag-perdof-norm003', None, 'negative', 'DONE')
('crm-train-v2-scalar-unc', None, 'success', 'DONE')
('crm-train-v2-perdof', None, 'success', 'DONE')
('eval-mag-perdof-norm005-object', None, 'success', 'DONE')
('eval-mag-perdof-norm02-seed43-object-r3', None, 'success', 'DONE')
('eval-mag-perdof-norm03-object-r3', None, 'success', 'DONE')
('eval-scalar-object-seed44-r2', None, 'negative', 'DONE')
('eval-perdof-object-seed44', None, 'negative', 'DONE')
('eval-mag-perdof-norm003-object', None, 'success', 'DONE')
('eval-scalar-object-seed43', None, 'success', 'DONE')
('eval-scalar-object-seed44', None, 'failed', 'DONE')
('eval-perdof-object-seed43', None, 'success', 'DONE')
('eval-mag-perdof-norm02-seed43-object-r2', None, 'killed', 'DONE')
('eval-mag-perdof-norm02-seed43-object', None, 'killed', 'DONE')
('eval-mag-perdof-norm03-object-r2', None, 'killed', 'DONE')
('eval-acr-object-v4-scalar-b2', None, 'killed', 'DONE')
('eval-mag-perdof-norm0p3-object-r2', None, 'killed', 'DONE')
('eval-mag-perdof-norm0p3-object', None, 'killed', 'DONE')
('eval-acr-object-v4-perdof', None, 'success', 'DONE')
('eval-acr-spatial-v4-scalar-r2', None, 'success', 'DONE')
('crm-train-v3-norm-scalar-unc', None, 'success', 'DONE')
('crm-train-v3-scalar-unc', None, 'killed', 'DONE')
('crm-train-v3-perdof', None, 'killed', 'DONE')
('eval-scalar-unc-spatial-v2', None, 'killed', 'DONE')
('crm-train-a4-scalar-unc', None, 'killed', 'DONE')
('eval-scalar-unc-spatial', None, 'killed', 'DONE')

=== Magnitude / epsilon ===

=== LTO ===
('eval-lto-splitA-vla-only-r3', 0.14, 'success', 'DONE')
('eval-lto-splitA-vla-only-r2', 0.14, 'success', 'DONE')
('eval-lto-splitA-heldout-r2', 0.02, 'negative', 'DONE')
('crm-lto-splitA-train', None, 'success', 'DONE')
('eval-lto-splitA-vla-only-v2', 0.14, 'success', 'DONE')
('eval-lto-splitA-heldout-v2', 0.02, 'negative', 'DONE')
('eval-lto-splitA-vla-only', None, 'killed', 'DONE')
('eval-lto-splitA-heldout', None, 'killed', 'DONE')
('crm-lto-splitA-train-fixed', None, 'success', 'DONE')
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "42a7d1e6-7e63-4198-8ee3-661cdf89f1ff",
  "tool_use_result": {
    "stdout": "=== OpenVLA ===\n('eval-openvla-crm-object-seed42', 0, 'negative', 'DONE')\n('train-crm-openvla-obs-only', None, 'success', 'DONE')\n('openvla-precompute-k1', None, 'success', 'DONE')\n('eval-openvla-object-baseline-seed42', None, 'killed', 'DONE')\n('eval-openvla-object-vla-only-seed42', None, 'negative', 'DONE')\n('eval-openvla-object-vla-only-seed42-v2', None, 'success', 'DONE')\n\n=== K=20 obs_only Object ===\n('eval-k20-obs-only-spatial-seed44', None, 'success', 'DONE')\n('eval-k20-obs-only-spatial-seed43', None, 'success', 'DONE')\n('eval-k20-obs-only-spatial-seed42', None, 'success', 'DONE')\n('eval-k20-obs-only-object-seed45', None, 'success', 'DONE')\n('eval-k20-obs-only-object-seed44', None, 'success', 'DONE')\n('eval-k20-obs-only-object-seed43', None, 'success', 'DONE')\n('eval-k20-obs-only-object-seed42', None, 'success', 'DONE')\n('eval-crm-object-k20-seed44', None, 'success', 'DONE')\n('eval-crm-object-k20-seed42', None, 'success', 'DONE')\n('eval-crm-object-k20-seed43', None, 'success', 'DONE')\n\n=== K=1 CRM ACCG ===\n('eval-crm-k1-object-seed43-plan702', None, 'success', 'DONE')\n('eval-crm-k1-object-seed42-plan702', None, 'success', 'DONE')\n('eval-crm-k1-object-seed44-plan702', None, 'success', 'DONE')\n('eval-crm-k1-object-seed44-plan702-r2', None, 'killed', 'DONE')\n('eval-crm-k1-object-seed43-plan702-r2', None, 'killed', 'DONE')\n('eval-crm-k1-object-seed42-plan702-r2', None, 'killed', 'DONE')\n('train-crm-k1-accg-object-seed42-full', None, 'success', 'DONE')\n('plan_701-crm-k1-train', None, 'success', 'DONE')\n('eval-k1-crm-multiscale-object-seed44-r2', None, 'negative', 'DONE')\n('eval-k1-crm-multiscale-object-seed44', None, 'negative', 'DONE')\n('eval-k1-crm-multiscale-object-seed43', None, 'negative', 'DONE')\n('eval-k1-crm-multiscale-object-seed42', None, 'negative', 'DONE')\n('eval-k1-crm-multiscale-object-seed43-r2', None, 'negative', 'DONE')\n('train-crm-k1-accg-object-seed42-v2', None, 'success', 'DONE')\n('eval-k1-crm-accg-object-seed44', None, 'negative', 'DONE')\n('eval-k1-crm-accg-object-seed43', None, 'negative', 'DONE')\n('eval-k1-crm-accg-object-seed42', None, 'negative', 'DONE')\n('train-crm-k1-accg-object-seed42-fallback', None, 'success', 'DONE')\n('train-crm-k1-accg-object-seed42', None, 'failed', 'DONE')\n\n=== Plan A pi05 ===\n\n=== Argmin K10 Object ===\n('eval-argmin-object-seed50', None, 'success', 'DONE')\n('eval-argmin-object-k5-seed44-r2', None, 'success', 'DONE')\n('eval-argmin-object-seed49', None, 'success', 'DONE')\n('eval-argmin-object-seed48', 0.15, 'success', 'DONE')\n('eval-argmin-object-k5-seed44', None, 'failed', 'DONE')\n('eval-argmin-object-k5-seed42', None, 'success', 'DONE')\n('eval-argmin-object-k5-seed45', None, 'success', 'DONE')\n('eval-argmin-object-k5-seed43', None, 'success', 'DONE')\n('eval-argmin-object-seed47', None, 'success', 'DONE')\n('eval-argmin-object-seed46', None, 'success', 'DONE')\n('eval-argmin-object-seed45', None, 'success', 'DONE')\n('eval-argmin-object-seed44-r2', None, 'success', 'DONE')\n('eval-argmin-object-seed44-r3', None, 'killed', 'DONE')\n('eval-argmin-object-seed44', None, 'failed', 'DONE')\n('eval-argmin-object-seed43', None, 'success', 'DONE')\n\n=== CRM perdof / scalar ===\n('eval-perdof-object-norm02-seed50', 0.1, 'negative', 'DONE')\n('eval-perdof-object-norm02-seed49', None, 'success', 'DONE')\n('eval-perdof-object-norm02-seed48', None, 'success', 'DONE')\n('eval-perdof-object-norm02-seed45-r3', None, 'success', 'DONE')\n('eval-perdof-object-norm003-seed47', None, 'success', 'DONE')\n('eval-perdof-object-norm005-seed47', None, 'success', 'DONE')\n('eval-perdof-object-norm005-seed45-r2', 0.1, 'success', 'DONE')\n('eval-perdof-object-norm01-seed43', None, 'success', 'DONE')\n('eval-perdof-object-norm03-seed43', None, 'success', 'DONE')\n('eval-perdof-object-norm003-seed48', 0.13, 'success', 'DONE')\n('eval-scalar-object-seed45-r2', None, 'negative', 'DONE')\n('eval-perdof-object-default-seed47', 0, 'negative', 'DONE')\n('eval-perdof-object-norm03-seed47', 0.05, 'success', 'DONE')\n('eval-perdof-object-norm003-seed46', 0.09, 'success', 'DONE')\n('eval-perdof-object-norm005-seed46', 0.11, 'success', 'DONE')\n('eval-perdof-object-norm003-seed45', None, 'killed', 'DONE')\n('eval-perdof-object-norm01-seed48', 0.12, 'success', 'DONE')\n('eval-perdof-object-norm03-seed46', 0.04, 'success', 'DONE')\n('eval-scalar-object-seed46', 0.09, 'success', 'DONE')\n('eval-perdof-object-norm03-seed48', None, 'killed', 'DONE')\n('eval-perdof-object-norm003-seed43', None, 'success', 'DONE')\n('eval-perdof-object-norm005-seed43', 0.13, 'success', 'DONE')\n('eval-perdof-object-default-seed43', 0, 'success', 'DONE')\n('eval-perdof-object-default-seed45', 0, 'success', 'DONE')\n('eval-perdof-object-norm005-seed45', None, 'failed', 'DONE')\n('eval-perdof-object-norm003-seed44-r2', None, 'failed', 'DONE')\n('eval-perdof-object-norm005-seed44', 0.09, 'success', 'DONE')\n('eval-perdof-object-norm003-seed44', None, 'failed', 'DONE')\n('eval-perdof-object-norm01-seed42-r2', None, 'failed', 'DONE')\n('eval-perdof-object-norm02-seed43', 0.09, 'success', 'DONE')\n('eval-perdof-object-norm01-seed46', None, 'negative', 'DONE')\n('eval-perdof-object-default-seed46', None, 'negative', 'DONE')\n('eval-perdof-object-default-seed44', None, 'negative', 'DONE')\n('eval-mag-perdof-norm02', None, 'killed', 'DONE')\n('eval-acr-spatial-v4-scalar', None, 'killed', 'DONE')\n('eval-perdof-object-norm02-seed47', None, 'success', 'DONE')\n('eval-perdof-object-norm02-seed46', None, 'success', 'DONE')\n('eval-perdof-object-norm02-seed43-r3', None, 'success', 'DONE')\n('mag_perdof_norm02_seed43_r3', None, 'killed', 'DONE')\n('eval-perdof-object-norm01-seed47-bjb1', None, 'success', 'DONE')\n('eval-perdof-object-norm01-seed46-r2', None, 'success', 'DONE')\n('eval-perdof-object-norm02-seed45-r2', None, 'killed', 'DONE')\n('eval-scalar-object-seed45', None, 'success', 'DONE')\n('eval-perdof-object-norm02-seed45', None, 'success', 'DONE')\n('eval-perdof-object-norm02-seed44', None, 'success', 'DONE')\n('eval-perdof-object-norm02-seed45-deploy', None, 'killed', 'DONE')\n('eval-perdof-object-norm03-seed45-r2', None, 'negative', 'DONE')\n('eval-perdof-object-norm03-seed44-r2', 0.04, 'negative', 'DONE')\n('eval-perdof-object-norm03-seed46-r2', None, 'killed', 'DONE')\n('eval-perdof-object-norm01-seed44', None, 'negative', 'DONE')\n('eval-perdof-object-norm01-seed45', None, 'success', 'DONE')\n('eval-perdof-object-norm01-seed47', None, 'killed', 'DONE')\n('eval-perdof-object-norm03-seed44', 0.04, 'negative', 'DONE')\n('eval-mag-perdof-norm02-object', None, 'negative', 'DONE')\n('eval-acr-object-v4-scalar', None, 'negative', 'DONE')\n('eval-mag-perdof-norm03', None, 'negative', 'DONE')\n('eval-mag-perdof-norm005', None, 'negative', 'DONE')\n('eval-mag-perdof-norm003', None, 'negative', 'DONE')\n('crm-train-v2-scalar-unc', None, 'success', 'DONE')\n('crm-train-v2-perdof', None, 'success', 'DONE')\n('eval-mag-perdof-norm005-object', None, 'success', 'DONE')\n('eval-mag-perdof-norm02-seed43-object-r3', None, 'success', 'DONE')\n('eval-mag-perdof-norm03-object-r3', None, 'success', 'DONE')\n('eval-scalar-object-seed44-r2', None, 'negative', 'DONE')\n('eval-perdof-object-seed44', None, 'negative', 'DONE')\n('eval-mag-perdof-norm003-object', None, 'success', 'DONE')\n('eval-scalar-object-seed43', None, 'success', 'DONE')\n('eval-scalar-object-seed44', None, 'failed', 'DONE')\n('eval-perdof-object-seed43', None, 'success', 'DONE')\n('eval-mag-perdof-norm02-seed43-object-r2', None, 'killed', 'DONE')\n('eval-mag-perdof-norm02-seed43-object', None, 'killed', 'DONE')\n('eval-mag-perdof-norm03-object-r2', None, 'killed', 'DONE')\n('eval-acr-object-v4-scalar-b2', None, 'killed', 'DONE')\n('eval-mag-perdof-norm0p3-object-r2', None, 'killed', 'DONE')\n('eval-mag-perdof-norm0p3-object', None, 'killed', 'DONE')\n('eval-acr-object-v4-perdof', None, 'success', 'DONE')\n('eval-acr-spatial-v4-scalar-r2', None, 'success', 'DONE')\n('crm-train-v3-norm-scalar-unc', None, 'success', 'DONE')\n('crm-train-v3-scalar-unc', None, 'killed', 'DONE')\n('crm-train-v3-perdof', None, 'killed', 'DONE')\n('eval-scalar-unc-spatial-v2', None, 'killed', 'DONE')\n('crm-train-a4-scalar-unc', None, 'killed', 'DONE')\n('eval-scalar-unc-spatial', None, 'killed', 'DONE')\n\n=== Magnitude / epsilon ===\n\n=== LTO ===\n('eval-lto-splitA-vla-only-r3', 0.14, 'success', 'DONE')\n('eval-lto-splitA-vla-only-r2', 0.14, 'success', 'DONE')\n('eval-lto-splitA-heldout-r2', 0.02, 'negative', 'DONE')\n('crm-lto-splitA-train', None, 'success', 'DONE')\n('eval-lto-splitA-vla-only-v2', 0.14, 'success', 'DONE')\n('eval-lto-splitA-heldout-v2', 0.02, 'negative', 'DONE')\n('eval-lto-splitA-vla-only', None, 'killed', 'DONE')\n('eval-lto-splitA-heldout', None, 'killed', 'DONE')\n('crm-lto-splitA-train-fixed', None, 'success', 'DONE')",
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

_source line 95_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "4cebaf00-47ad-4362-abab-cb8c67aba18a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01G1wY9Q8oofqdWiGfn2nN74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7300,
      "cache_read_input_tokens": 120826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7300
      },
      "output_tokens": 70,
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

_source line 96_

<details open><summary>🔧 Tool call — Bash · `toolu_01E5r536CMDjnhhC21JYTHx8`</summary>

```json
{
  "command": "python3 <<'EOF'\nimport json, re\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt') as f:\n    obj = json.load(f)\nexps = json.loads(obj['result'])['data']['experiments']\n\ndef grab(rx):\n    return [(k, (e.get('metrics') or {}).get('success_rate'), e.get('conclusion'), e.get('status')) for k,e in exps.items() if re.search(rx, k)]\n\n# CRM obs_only Spatial — try alternative names\nprint('=== CRM/obs spatial ===')\nfor r in grab('obs.*spatial|spatial.*obs|crm.*spatial|spatial.*crm'):\n    print(r)\n\nprint('\\n=== Goal / Long ===')\nfor r in grab('goal|long'):\n    print(r)\nEOF",
  "description": "Spatial CRM enum"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "dce90798-9c75-436d-9d9c-cbec64cce965",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01G1wY9Q8oofqdWiGfn2nN74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7300,
      "cache_read_input_tokens": 120826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7300
      },
      "output_tokens": 70,
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

_source line 97 · 2026-05-21T16:41:48.497Z_

<details><summary>↩ Tool result · `toolu_01E5r536CMDjnhhC21JYTHx8`</summary>

```text
=== CRM/obs spatial ===
('eval-spatial-obs-only-seed45', None, 'success', 'DONE')
('eval-k20-obs-only-spatial-seed44', None, 'success', 'DONE')
('eval-k20-obs-only-spatial-seed43', None, 'success', 'DONE')
('eval-k20-obs-only-spatial-seed42', None, 'success', 'DONE')
('eval-obs-only-spatial-norm02-seed52', 0.33, 'success', 'DONE')
('eval-obs-only-spatial-norm02-seed50', 0.35, 'success', 'DONE')
('eval-obs-only-spatial-norm02-seed42-r2', None, 'success', 'DONE')
('eval-obs-only-spatial-seed48', None, 'success', 'DONE')
('eval-obs-only-spatial-norm02-seed42', None, 'killed', 'DONE')
('eval-obs-only-spatial-norm02-seed49', None, 'success', 'DONE')
('eval-obs-only-spatial-norm02-seed46-r2', None, 'success', 'DONE')
('eval-obs-only-spatial-norm02-seed48', 0.35, 'success', 'DONE')
('eval-crm-spatial-k10-seed51', 0.36, 'success', 'DONE')
('eval-obs-only-spatial-norm02-seed43-r2', None, 'success', 'DONE')
('eval-obs-only-spatial-norm02-seed43', None, 'failed', 'DONE')
('eval-obs-only-spatial-norm02-seed47', None, 'success', 'DONE')
('eval-obs-only-spatial-norm02-seed46', None, 'failed', 'DONE')
('eval-obs-only-spatial-norm02-k5-seed44-r2', 0.37, 'success', 'DONE')
('eval-obs-only-spatial-norm02-k5-seed45-r2', 0.34, 'success', 'DONE')
('eval-obs-only-spatial-norm02-k5-seed45', None, 'failed', 'DONE')
('eval-obs-only-spatial-norm02-k5-seed44', None, 'failed', 'DONE')
('eval-obs-only-spatial-norm02-seed44', 0.36, 'success', 'DONE')
('eval-obs-only-spatial-norm02-seed45', 0.34, 'success', 'DONE')
('eval-obs-only-spatial-norm02-k5-seed43', 0.32, 'success', 'DONE')
('eval-obs-only-spatial-norm02-k5-seed42', 0.35, 'success', 'DONE')
('eval-acr-spatial-v4-obs-only-r2', None, 'killed', 'DONE')
('eval-obs-only-spatial-v2', None, 'failed', 'DONE')
('eval-obs-only-spatial', None, 'failed', 'DONE')
('eval-acr-spatial-v4-obs-only-r3', None, 'success', 'DONE')
('eval-obs-only-spatial-seed43', None, 'failed', 'DONE')
('eval-acr-spatial-v4-obs-only', None, 'failed', 'DONE')
('eval-obs-only-spatial-v3', None, 'killed', 'DONE')

=== Goal / Long ===
('eval-vla-only-goal-seed51', None, 'success', 'DONE')
('eval-vla-only-goal-seed44-r2', None, 'success', 'DONE')
('eval-obs-only-goal-norm02-seed51', None, 'success', 'DONE')
('eval-obs-only-goal-norm02-seed52', 0.68, 'success', 'DONE')
('eval-vla-only-goal-seed47', None, 'failed', 'DONE')
('eval-vla-only-long-seed49-r2', None, 'success', 'DONE')
('eval-vla-only-goal-seed49', 0.65, 'success', 'DONE')
('eval-vla-only-long-seed52', 0.17, 'success', 'DONE')
('eval-vla-only-long-seed51', 0.15, 'success', 'DONE')
('eval-vla-only-long-seed50', 0.16, 'success', 'DONE')
('eval-crm-long-seed50', 0.14, 'success', 'DONE')
('eval-vla-only-goal-seed48-r2', None, 'failed', 'DONE')
('eval-vla-only-goal-seed47-r2', None, 'failed', 'DONE')
('eval-crm-goal-seed46', None, 'success', 'DONE')
('eval-crm-long-seed47', 0.17, 'success', 'DONE')
('eval-vla-only-long-seed48', 0.14, 'success', 'DONE')
('eval-crm-long-seed46', 0.18, 'success', 'DONE')
('eval-crm-goal-seed45-r2', 0.65, 'success', 'DONE')
('eval-crm-goal-seed44-r2', 0.64, 'success', 'DONE')
('eval-crm-long-seed45', None, 'success', 'DONE')
('eval-vla-only-goal-seed48', None, 'killed', 'DONE')
('eval-vla-only-goal-seed43', None, 'success', 'DONE')
('eval-vla-only-goal-seed42', None, 'success', 'DONE')
('eval-crm-long-seed44', None, 'success', 'DONE')
('eval-crm-long-seed43', None, 'success', 'DONE')
('eval-crm-long-seed42', None, 'success', 'DONE')
('eval-crm-goal-seed42', None, 'success', 'DONE')
('eval-crm-goal-seed43', None, 'success', 'DONE')
('eval-vla-only-long-seed47', None, 'success', 'DONE')
('eval-crm-goal-seed45', None, 'failed', 'DONE')
('eval-crm-goal-seed44', None, 'failed', 'DONE')
('eval-vla-only-goal-seed45', None, 'success', 'DONE')
('eval-vla-only-goal-seed46', None, 'success', 'DONE')
('eval-vla-only-long-seed46', None, 'success', 'DONE')
('eval-vla-only-long-seed45', None, 'success', 'DONE')
('eval-vla-only-long-seed44', None, 'success', 'DONE')
('eval-vla-only-long-seed42', None, 'success', 'DONE')
('eval-vla-only-long-seed43', None, 'success', 'DONE')
('eval-vla-only-goal-seed44', None, 'killed', 'DONE')
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "54420ac7-1fbb-497d-a071-8461f0347120",
  "tool_use_result": {
    "stdout": "=== CRM/obs spatial ===\n('eval-spatial-obs-only-seed45', None, 'success', 'DONE')\n('eval-k20-obs-only-spatial-seed44', None, 'success', 'DONE')\n('eval-k20-obs-only-spatial-seed43', None, 'success', 'DONE')\n('eval-k20-obs-only-spatial-seed42', None, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-seed52', 0.33, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-seed50', 0.35, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-seed42-r2', None, 'success', 'DONE')\n('eval-obs-only-spatial-seed48', None, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-seed42', None, 'killed', 'DONE')\n('eval-obs-only-spatial-norm02-seed49', None, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-seed46-r2', None, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-seed48', 0.35, 'success', 'DONE')\n('eval-crm-spatial-k10-seed51', 0.36, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-seed43-r2', None, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-seed43', None, 'failed', 'DONE')\n('eval-obs-only-spatial-norm02-seed47', None, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-seed46', None, 'failed', 'DONE')\n('eval-obs-only-spatial-norm02-k5-seed44-r2', 0.37, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-k5-seed45-r2', 0.34, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-k5-seed45', None, 'failed', 'DONE')\n('eval-obs-only-spatial-norm02-k5-seed44', None, 'failed', 'DONE')\n('eval-obs-only-spatial-norm02-seed44', 0.36, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-seed45', 0.34, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-k5-seed43', 0.32, 'success', 'DONE')\n('eval-obs-only-spatial-norm02-k5-seed42', 0.35, 'success', 'DONE')\n('eval-acr-spatial-v4-obs-only-r2', None, 'killed', 'DONE')\n('eval-obs-only-spatial-v2', None, 'failed', 'DONE')\n('eval-obs-only-spatial', None, 'failed', 'DONE')\n('eval-acr-spatial-v4-obs-only-r3', None, 'success', 'DONE')\n('eval-obs-only-spatial-seed43', None, 'failed', 'DONE')\n('eval-acr-spatial-v4-obs-only', None, 'failed', 'DONE')\n('eval-obs-only-spatial-v3', None, 'killed', 'DONE')\n\n=== Goal / Long ===\n('eval-vla-only-goal-seed51', None, 'success', 'DONE')\n('eval-vla-only-goal-seed44-r2', None, 'success', 'DONE')\n('eval-obs-only-goal-norm02-seed51', None, 'success', 'DONE')\n('eval-obs-only-goal-norm02-seed52', 0.68, 'success', 'DONE')\n('eval-vla-only-goal-seed47', None, 'failed', 'DONE')\n('eval-vla-only-long-seed49-r2', None, 'success', 'DONE')\n('eval-vla-only-goal-seed49', 0.65, 'success', 'DONE')\n('eval-vla-only-long-seed52', 0.17, 'success', 'DONE')\n('eval-vla-only-long-seed51', 0.15, 'success', 'DONE')\n('eval-vla-only-long-seed50', 0.16, 'success', 'DONE')\n('eval-crm-long-seed50', 0.14, 'success', 'DONE')\n('eval-vla-only-goal-seed48-r2', None, 'failed', 'DONE')\n('eval-vla-only-goal-seed47-r2', None, 'failed', 'DONE')\n('eval-crm-goal-seed46', None, 'success', 'DONE')\n('eval-crm-long-seed47', 0.17, 'success', 'DONE')\n('eval-vla-only-long-seed48', 0.14, 'success', 'DONE')\n('eval-crm-long-seed46', 0.18, 'success', 'DONE')\n('eval-crm-goal-seed45-r2', 0.65, 'success', 'DONE')\n('eval-crm-goal-seed44-r2', 0.64, 'success', 'DONE')\n('eval-crm-long-seed45', None, 'success', 'DONE')\n('eval-vla-only-goal-seed48', None, 'killed', 'DONE')\n('eval-vla-only-goal-seed43', None, 'success', 'DONE')\n('eval-vla-only-goal-seed42', None, 'success', 'DONE')\n('eval-crm-long-seed44', None, 'success', 'DONE')\n('eval-crm-long-seed43', None, 'success', 'DONE')\n('eval-crm-long-seed42', None, 'success', 'DONE')\n('eval-crm-goal-seed42', None, 'success', 'DONE')\n('eval-crm-goal-seed43', None, 'success', 'DONE')\n('eval-vla-only-long-seed47', None, 'success', 'DONE')\n('eval-crm-goal-seed45', None, 'failed', 'DONE')\n('eval-crm-goal-seed44', None, 'failed', 'DONE')\n('eval-vla-only-goal-seed45', None, 'success', 'DONE')\n('eval-vla-only-goal-seed46', None, 'success', 'DONE')\n('eval-vla-only-long-seed46', None, 'success', 'DONE')\n('eval-vla-only-long-seed45', None, 'success', 'DONE')\n('eval-vla-only-long-seed44', None, 'success', 'DONE')\n('eval-vla-only-long-seed42', None, 'success', 'DONE')\n('eval-vla-only-long-seed43', None, 'success', 'DONE')\n('eval-vla-only-goal-seed44', None, 'killed', 'DONE')",
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

_source line 98_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "f76b435a-617b-4633-9117-11ae2b3eac2b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PrEFizXWAEQbtf1KHttnie",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3877,
      "cache_read_input_tokens": 128126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3877
      },
      "output_tokens": 46,
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

_source line 99_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01TBMYdMeeF7mfvHJ6eB33Xe`</summary>

```json
{
  "todos": [
    {
      "content": "Explore paper LaTeX source structure",
      "activeForm": "Exploring paper LaTeX source structure",
      "status": "completed"
    },
    {
      "content": "Attempt compilation and capture warnings/errors",
      "activeForm": "Attempting compilation and capturing warnings/errors",
      "status": "completed"
    },
    {
      "content": "Cross-check numerical claims against registry",
      "activeForm": "Cross-checking numerical claims against registry",
      "status": "completed"
    },
    {
      "content": "Audit pi0.5 / OpenVLA section coverage gaps",
      "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps",
      "status": "in_progress"
    },
    {
      "content": "Verify .bib entries and \\cite{} resolution",
      "activeForm": "Verifying .bib entries and \\cite{} resolution",
      "status": "completed"
    },
    {
      "content": "Write audit report to artifacts and register",
      "activeForm": "Writing audit report to artifacts and registering",
      "status": "pending"
    }
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "99bd8d88-f21b-4afd-9ea4-27b42c48d420",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PrEFizXWAEQbtf1KHttnie",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3877,
      "cache_read_input_tokens": 128126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3877
      },
      "output_tokens": 46,
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

_source line 100 · 2026-05-21T16:42:43.577Z_

<details><summary>↩ Tool result · `toolu_01TBMYdMeeF7mfvHJ6eB33Xe`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "6d88fbdf-5807-4331-93bf-59db791e191c",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Explore paper LaTeX source structure",
        "status": "completed",
        "activeForm": "Exploring paper LaTeX source structure"
      },
      {
        "content": "Attempt compilation and capture warnings/errors",
        "status": "completed",
        "activeForm": "Attempting compilation and capturing warnings/errors"
      },
      {
        "content": "Cross-check numerical claims against registry",
        "status": "in_progress",
        "activeForm": "Cross-checking numerical claims against registry"
      },
      {
        "content": "Audit pi0.5 / OpenVLA section coverage gaps",
        "status": "pending",
        "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps"
      },
      {
        "content": "Verify .bib entries and \\cite{} resolution",
        "status": "completed",
        "activeForm": "Verifying .bib entries and \\cite{} resolution"
      },
      {
        "content": "Write audit report to artifacts and register",
        "status": "pending",
        "activeForm": "Writing audit report to artifacts and registering"
      }
    ],
    "newTodos": [
      {
        "content": "Explore paper LaTeX source structure",
        "status": "completed",
        "activeForm": "Exploring paper LaTeX source structure"
      },
      {
        "content": "Attempt compilation and capture warnings/errors",
        "status": "completed",
        "activeForm": "Attempting compilation and capturing warnings/errors"
      },
      {
        "content": "Cross-check numerical claims against registry",
        "status": "completed",
        "activeForm": "Cross-checking numerical claims against registry"
      },
      {
        "content": "Audit pi0.5 / OpenVLA section coverage gaps",
        "status": "in_progress",
        "activeForm": "Auditing pi0.5 / OpenVLA section coverage gaps"
      },
      {
        "content": "Verify .bib entries and \\cite{} resolution",
        "status": "completed",
        "activeForm": "Verifying .bib entries and \\cite{} resolution"
      },
      {
        "content": "Write audit report to artifacts and register",
        "status": "pending",
        "activeForm": "Writing audit report to artifacts and registering"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 101_

<details open><summary>🔧 Tool call — Grep · `toolu_012Zn4cJga9ooCZum32qe3z9`</summary>

```json
{
  "pattern": "pi_?\\{?0\\.5\\}?|pi05|pi0\\.5|\\\\pi_\\{0\\.5\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "950f858c-6782-4c0e-adea-9834968a058c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01882s599Abozi3LrJjx3XFu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4081,
      "cache_read_input_tokens": 132003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4081
      },
      "output_tokens": 44,
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

_source line 102 · 2026-05-21T16:42:49.894Z_

<details><summary>↩ Tool result · `toolu_012Zn4cJga9ooCZum32qe3z9`</summary>

```text
experiments.tex:107:We further validate cross-VLA generalization on $\pi_{0.5}$ (3.6B)~\cite{black2024pi0}; see Appendix~\ref{sec:cross_vla}.
appendix.tex:182:[Omitted long matching line]
appendix.tex:186:\caption{Cross-VLA generalization: $\pi_{0.5}$ (3.6B) on LIBERO. The $\pi_{0.5}$ baseline operates at $81$--$85$\% SR, substantially above SmolVLA's $11$--$29$\%, constraining the headroom for correction. $n{=}3$ seeds.}
appendix.tex:193:$\pi_{0.5}$ VLA-only & 1 & $81.5 \pm 0.5$ & $84.2 \pm 1.0$ \\
appendix.tex:194:$\pi_{0.5}$ Plan~A & 2 & \placeholder{} & \placeholder{} \\
appendix.tex:199:Table~\ref{tab:cross_vla} reports results. The $\pi_{0.5}$ baseline already achieves $81.5 \pm 0.5$\% on Object and $84.2 \pm 1.0$\% on Spatial---substantially above SmolVLA's $11.0$\% / $29.4$\%---leaving limited headroom for post-hoc correction. Plan~A results are pending (\placeholder{}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "4ccdb2c1-b82b-4910-a3ed-cdf04fd67728",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "experiments.tex:107:We further validate cross-VLA generalization on $\\pi_{0.5}$ (3.6B)~\\cite{black2024pi0}; see Appendix~\\ref{sec:cross_vla}.\nappendix.tex:182:[Omitted long matching line]\nappendix.tex:186:\\caption{Cross-VLA generalization: $\\pi_{0.5}$ (3.6B) on LIBERO. The $\\pi_{0.5}$ baseline operates at $81$--$85$\\% SR, substantially above SmolVLA's $11$--$29$\\%, constraining the headroom for correction. $n{=}3$ seeds.}\nappendix.tex:193:$\\pi_{0.5}$ VLA-only & 1 & $81.5 \\pm 0.5$ & $84.2 \\pm 1.0$ \\\\\nappendix.tex:194:$\\pi_{0.5}$ Plan~A & 2 & \\placeholder{} & \\placeholder{} \\\\\nappendix.tex:199:Table~\\ref{tab:cross_vla} reports results. The $\\pi_{0.5}$ baseline already achieves $81.5 \\pm 0.5$\\% on Object and $84.2 \\pm 1.0$\\% on Spatial---substantially above SmolVLA's $11.0$\\% / $29.4$\\%---leaving limited headroom for post-hoc correction. Plan~A results are pending (\\placeholder{}).",
    "numLines": 6
  }
}
```

</details>

---


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Grep · `toolu_01ErBAmeivJwb2mc4LP1xiAT`</summary>

```json
{
  "pattern": "openvla|OpenVLA",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "3ef82219-e3fa-4001-914a-25974fddd4b9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01882s599Abozi3LrJjx3XFu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4081,
      "cache_read_input_tokens": 132003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4081
      },
      "output_tokens": 44,
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

_source line 104 · 2026-05-21T16:42:51.407Z_

<details><summary>↩ Tool result · `toolu_01ErBAmeivJwb2mc4LP1xiAT`</summary>

```text
related_work.tex:5:[Omitted long matching line]
main.bbl:111:  Levine, Liang, and Finn]{kim2024openvla}
appendix.tex:95:The multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\cite{kim2024openvla} (autoregressive tokenization, 7B).
appendix.tex:100:\caption{Per-DOF action variance (log scale) across $K{=}10$ samples for SmolVLA (flow-matching) and OpenVLA (tokenized). OpenVLA produces 8/10 identical samples at temperature $T{=}0.5$, with per-DOF variance below $10^{-30}$ for most dimensions.}
appendix.tex:104:Figure~\ref{fig:diversity} shows the contrast: SmolVLA produces meaningfully diverse samples across all action dimensions, while OpenVLA at temperature $T{=}0.5$ generates 8 out of 10 identical action sequences, with per-DOF variance below $10^{-30}$ for most dimensions.
references.bib:79:@misc{kim2024openvla,
references.bib:80:    title={OpenVLA: An Open-Source Vision-Language-Action Model},
main.aux:15:\citation{brohan2023rt2,kim2024openvla,ghosh2024octo}
main.aux:113:\bibcite{kim2024openvla}{{14}{2024}{{Kim et~al.}}{{Kim, Pertsch, Karamcheti, Xiao, Balakrishna, Nair, Rafailov, Foster, Lam, Sanketi, Vuong, Kollar, Burchfiel, Tedrake, Sadigh, Levine, Liang, and Finn}}}
main.aux:146:\citation{kim2024openvla}
main.aux:153:\@writefile{lof}{\contentsline {figure}{\numberline {6}{\ignorespaces Per-DOF action variance (log scale) across $K{=}10$ samples for SmolVLA (flow-matching) and OpenVLA (tokenized). OpenVLA produces 8/10 identical samples at temperature $T{=}0.5$, with per-DOF variance below $10^{-30}$ for most dimensions.}}{13}{figure.6}\protected@file@percent }
main.aux:154:\newlabel{fig:diversity}{{6}{13}{Per-DOF action variance (log scale) across $K{=}10$ samples for SmolVLA (flow-matching) and OpenVLA (tokenized). OpenVLA produces 8/10 identical samples at temperature $T{=}0.5$, with per-DOF variance below $10^{-30}$ for most dimensions}{figure.6}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "124e0c70-70a5-459d-a2e1-176b80a89486",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "related_work.tex:5:[Omitted long matching line]\nmain.bbl:111:  Levine, Liang, and Finn]{kim2024openvla}\nappendix.tex:95:The multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\\cite{kim2024openvla} (autoregressive tokenization, 7B).\nappendix.tex:100:\\caption{Per-DOF action variance (log scale) across $K{=}10$ samples for SmolVLA (flow-matching) and OpenVLA (tokenized). OpenVLA produces 8/10 identical samples at temperature $T{=}0.5$, with per-DOF variance below $10^{-30}$ for most dimensions.}\nappendix.tex:104:Figure~\\ref{fig:diversity} shows the contrast: SmolVLA produces meaningfully diverse samples across all action dimensions, while OpenVLA at temperature $T{=}0.5$ generates 8 out of 10 identical action sequences, with per-DOF variance below $10^{-30}$ for most dimensions.\nreferences.bib:79:@misc{kim2024openvla,\nreferences.bib:80:    title={OpenVLA: An Open-Source Vision-Language-Action Model},\nmain.aux:15:\\citation{brohan2023rt2,kim2024openvla,ghosh2024octo}\nmain.aux:113:\\bibcite{kim2024openvla}{{14}{2024}{{Kim et~al.}}{{Kim, Pertsch, Karamcheti, Xiao, Balakrishna, Nair, Rafailov, Foster, Lam, Sanketi, Vuong, Kollar, Burchfiel, Tedrake, Sadigh, Levine, Liang, and Finn}}}\nmain.aux:146:\\citation{kim2024openvla}\nmain.aux:153:\\@writefile{lof}{\\contentsline {figure}{\\numberline {6}{\\ignorespaces Per-DOF action variance (log scale) across $K{=}10$ samples for SmolVLA (flow-matching) and OpenVLA (tokenized). OpenVLA produces 8/10 identical samples at temperature $T{=}0.5$, with per-DOF variance below $10^{-30}$ for most dimensions.}}{13}{figure.6}\\protected@file@percent }\nmain.aux:154:\\newlabel{fig:diversity}{{6}{13}{Per-DOF action variance (log scale) across $K{=}10$ samples for SmolVLA (flow-matching) and OpenVLA (tokenized). OpenVLA produces 8/10 identical samples at temperature $T{=}0.5$, with per-DOF variance below $10^{-30}$ for most dimensions}{figure.6}{}}",
    "numLines": 12
  }
}
```

</details>

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Grep · `toolu_01DBdX4gQmNcrVSd7jdUDsoQ`</summary>

```json
{
  "pattern": "placeholder|\\\\placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "6ae0d5e6-bf0d-4d5a-970f-526a8a7a4776",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01882s599Abozi3LrJjx3XFu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4081,
      "cache_read_input_tokens": 132003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4081
      },
      "output_tokens": 44,
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

_source line 106 · 2026-05-21T16:42:52.612Z_

<details><summary>↩ Tool result · `toolu_01DBdX4gQmNcrVSd7jdUDsoQ`</summary>

```text
main.tex:15:\newcommand{\placeholder}[1]{---}
appendix.tex:194:$\pi_{0.5}$ Plan~A & 2 & \placeholder{} & \placeholder{} \\
appendix.tex:199:Table~\ref{tab:cross_vla} reports results. The $\pi_{0.5}$ baseline already achieves $81.5 \pm 0.5$\% on Object and $84.2 \pm 1.0$\% on Spatial---substantially above SmolVLA's $11.0$\% / $29.4$\%---leaving limited headroom for post-hoc correction. Plan~A results are pending (\placeholder{}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "868e4fdb-7ec0-4079-8e65-f1943f61c0ce",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "main.tex:15:\\newcommand{\\placeholder}[1]{---}\nappendix.tex:194:$\\pi_{0.5}$ Plan~A & 2 & \\placeholder{} & \\placeholder{} \\\\\nappendix.tex:199:Table~\\ref{tab:cross_vla} reports results. The $\\pi_{0.5}$ baseline already achieves $81.5 \\pm 0.5$\\% on Object and $84.2 \\pm 1.0$\\% on Spatial---substantially above SmolVLA's $11.0$\\% / $29.4$\\%---leaving limited headroom for post-hoc correction. Plan~A results are pending (\\placeholder{}).",
    "numLines": 3
  }
}
```

</details>

---


### Tool call

_source line 107_

<details open><summary>🔧 Tool call — Bash · `toolu_01CRkqSUidoi9xPsiheo9e1U`</summary>

```json
{
  "command": "python3 <<'EOF'\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2a1e02b6-c6f9-46bc-8517-4220435946da/tool-results/mcp-agent-ml-research-read_registry-1779381618109.txt') as f:\n    obj = json.load(f)\nexps = json.loads(obj['result'])['data']['experiments']\nfor k,v in exps.items():\n    if 'pi05' in k.lower() and v.get('status')=='DONE':\n        print(k, v.get('metrics'), v.get('conclusion'))\nEOF",
  "description": "Verify pi05 metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "e67e0c45-6298-49a9-85be-d7724dcda197",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01A5xhVVWTPnRo2P2mWRTJVd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2327,
      "cache_read_input_tokens": 136084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2327
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

_source line 108 · 2026-05-21T16:43:02.675Z_

<details><summary>↩ Tool result · `toolu_01CRkqSUidoi9xPsiheo9e1U`</summary>

```text
eval-pi05-vla-only-spatial-seed45 {'success_rate': 0.85, 'n_tasks': 10, 'total_rollouts': 200} success
eval-pi05-vla-only-spatial-seed43-r3 {'success_rate': 0.83, 'n_tasks': 10, 'total_rollouts': 200} success
eval-pi05-vla-only-spatial-seed42-r3 {'success_rate': 0.845, 'n_tasks': 10, 'total_rollouts': 200} success
eval-pi05-vla-only-object-seed44-r3 {'success_rate': 0.81, 'n_tasks': 10, 'total_rollouts': 200} success
eval-pi05-vla-only-object-seed43-r3 {'success_rate': 0.815, 'n_tasks': 10, 'total_rollouts': 200} success
eval-pi05-vla-only-object-seed42-r3 {'success_rate': 0.82, 'n_tasks': 10, 'total_rollouts': 200} success
eval-pi05-vla-only-object-seed44 {'overall_sr': 0, 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20} failed
eval-pi05-vla-only-object-seed43 {'overall_sr': 0, 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20} failed
eval-pi05-vla-only-object-seed42 {'overall_sr': 0, 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20} failed
eval-pi05-vla-only-spatial-seed44 None failed
eval-pi05-vla-only-spatial-seed43 None failed
eval-pi05-vla-only-spatial-seed42 None failed
eval-pi05-baseline-object-seed42 {'overall_success_rate': 0} failed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "8c210ec4-9c98-41a0-ba06-d5c715c70d61",
  "tool_use_result": {
    "stdout": "eval-pi05-vla-only-spatial-seed45 {'success_rate': 0.85, 'n_tasks': 10, 'total_rollouts': 200} success\neval-pi05-vla-only-spatial-seed43-r3 {'success_rate': 0.83, 'n_tasks': 10, 'total_rollouts': 200} success\neval-pi05-vla-only-spatial-seed42-r3 {'success_rate': 0.845, 'n_tasks': 10, 'total_rollouts': 200} success\neval-pi05-vla-only-object-seed44-r3 {'success_rate': 0.81, 'n_tasks': 10, 'total_rollouts': 200} success\neval-pi05-vla-only-object-seed43-r3 {'success_rate': 0.815, 'n_tasks': 10, 'total_rollouts': 200} success\neval-pi05-vla-only-object-seed42-r3 {'success_rate': 0.82, 'n_tasks': 10, 'total_rollouts': 200} success\neval-pi05-vla-only-object-seed44 {'overall_sr': 0, 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20} failed\neval-pi05-vla-only-object-seed43 {'overall_sr': 0, 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20} failed\neval-pi05-vla-only-object-seed42 {'overall_sr': 0, 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_rollouts': 200, 'n_tasks': 10, 'n_rollouts_per_task': 20} failed\neval-pi05-vla-only-spatial-seed44 None failed\neval-pi05-vla-only-spatial-seed43 None failed\neval-pi05-vla-only-spatial-seed42 None failed\neval-pi05-baseline-object-seed42 {'overall_success_rate': 0} failed",
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

_source line 109_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "c1cb13ce-96a0-48dc-98bc-2991aad65b59",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MYbYrzChMqVD7PGJWyx7sc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 138411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1133
      },
      "output_tokens": 95,
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

_source line 110_

<details open><summary>🔧 Tool call — Read · `toolu_017ZaQZSvJ9oVqtJHsgfg7iA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.bbl",
  "offset": 1,
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
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "890359e8-9f65-4d5c-8fac-8c36036ee5d4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MYbYrzChMqVD7PGJWyx7sc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 138411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1133
      },
      "output_tokens": 95,
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

_source line 111 · 2026-05-21T16:43:12.706Z_

<details><summary>↩ Tool result · `toolu_017ZaQZSvJ9oVqtJHsgfg7iA`</summary>

```text
1	\begin{thebibliography}{31}
2	\providecommand{\natexlab}[1]{#1}
3	\providecommand{\url}[1]{\texttt{#1}}
4	\expandafter\ifx\csname urlstyle\endcsname\relax
5	  \providecommand{\doi}[1]{doi: #1}\else
6	  \providecommand{\doi}{doi: \begingroup \urlstyle{rm}\Url}\fi
7	
8	\bibitem[Black et~al.(2024)Black, Brown, Driess, Esmail, Equi, Finn, Fusai,
9	  Groom, Hausman, Ichter, Jakubczak, Jones, Ke, Levine, Li-Bell, Mothukuri,
10	  Nair, Pertsch, Shi, Tanner, Vuong, Walling, Wang, and
11	  Zhilinsky]{black2024pi0}
12	K.~Black, N.~Brown, D.~Driess, A.~Esmail, M.~Equi, C.~Finn, N.~Fusai, L.~Groom,
13	  K.~Hausman, B.~Ichter, S.~Jakubczak, T.~Jones, L.~Ke, S.~Levine, A.~Li-Bell,
14	  M.~Mothukuri, S.~Nair, K.~Pertsch, L.~X. Shi, J.~Tanner, Q.~Vuong,
15	  A.~Walling, H.~Wang, and U.~Zhilinsky.
16	\newblock $\pi_0$: A vision-language-action flow model for general robot
17	  control, 2024.
18	
19	\bibitem[Shukor et~al.(2025)Shukor, Aubakirova, Capuano, Kooijmans, Palma,
20	  Zouitine, Aractingi, Pascal, Russi, Marafioti, Alibert, Cord, Wolf, and
21	  Cadene]{shukor2025smolvla}
22	M.~Shukor, D.~Aubakirova, F.~Capuano, P.~Kooijmans, S.~Palma, A.~Zouitine,
23	  M.~Aractingi, C.~Pascal, M.~Russi, A.~Marafioti, S.~Alibert, M.~Cord,
24	  T.~Wolf, and R.~Cadene.
25	\newblock Smolvla: A vision-language-action model for affordable and efficient
26	  robotics, 2025.
27	
28	\bibitem[Lipman et~al.(2023)Lipman, Chen, Ben-Hamu, Nickel, and
29	  Le]{lipman2023flow}
30	Y.~Lipman, R.~T.~Q. Chen, H.~Ben-Hamu, M.~Nickel, and M.~Le.
31	\newblock Flow matching for generative modeling.
32	\newblock In \emph{International Conference on Learning Representations
33	  (ICLR)}, 2023.
34	
35	\bibitem[Fei et~al.(2025{\natexlab{a}})Fei, Wang, Shi, Dai, Cai, Qian, Ji, He,
36	  Zhang, Fei, Fu, Gong, and Qiu]{fei2025liberoplus}
37	S.~Fei, S.~Wang, J.~Shi, Z.~Dai, J.~Cai, P.~Qian, L.~Ji, X.~He, S.~Zhang,
38	  Z.~Fei, J.~Fu, J.~Gong, and X.~Qiu.
39	\newblock Libero-plus: In-depth robustness analysis of vision-language-action
40	  models, 2025{\natexlab{a}}.
41	
42	\bibitem[Fei et~al.(2025{\natexlab{b}})Fei, Wang, Ji, Li, Zhang, Liu, Hou,
43	  Gong, Zhao, and Qiu]{srpo2025}
44	S.~Fei, S.~Wang, L.~Ji, A.~Li, S.~Zhang, L.~Liu, J.~Hou, J.~Gong, X.~Zhao, and
45	  X.~Qiu.
46	\newblock Srpo: Self-referential policy optimization for vision-language-action
47	  models, 2025{\natexlab{b}}.
48	
49	\bibitem[Zhang et~al.(2025{\natexlab{a}})Zhang, Zhang, Jin, Zeng, Li, and
50	  Wang]{robustvla2025}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "28798699-bdb9-4054-b1b3-e380e74bf6c9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.bbl",
      "content": "\\begin{thebibliography}{31}\n\\providecommand{\\natexlab}[1]{#1}\n\\providecommand{\\url}[1]{\\texttt{#1}}\n\\expandafter\\ifx\\csname urlstyle\\endcsname\\relax\n  \\providecommand{\\doi}[1]{doi: #1}\\else\n  \\providecommand{\\doi}{doi: \\begingroup \\urlstyle{rm}\\Url}\\fi\n\n\\bibitem[Black et~al.(2024)Black, Brown, Driess, Esmail, Equi, Finn, Fusai,\n  Groom, Hausman, Ichter, Jakubczak, Jones, Ke, Levine, Li-Bell, Mothukuri,\n  Nair, Pertsch, Shi, Tanner, Vuong, Walling, Wang, and\n  Zhilinsky]{black2024pi0}\nK.~Black, N.~Brown, D.~Driess, A.~Esmail, M.~Equi, C.~Finn, N.~Fusai, L.~Groom,\n  K.~Hausman, B.~Ichter, S.~Jakubczak, T.~Jones, L.~Ke, S.~Levine, A.~Li-Bell,\n  M.~Mothukuri, S.~Nair, K.~Pertsch, L.~X. Shi, J.~Tanner, Q.~Vuong,\n  A.~Walling, H.~Wang, and U.~Zhilinsky.\n\\newblock $\\pi_0$: A vision-language-action flow model for general robot\n  control, 2024.\n\n\\bibitem[Shukor et~al.(2025)Shukor, Aubakirova, Capuano, Kooijmans, Palma,\n  Zouitine, Aractingi, Pascal, Russi, Marafioti, Alibert, Cord, Wolf, and\n  Cadene]{shukor2025smolvla}\nM.~Shukor, D.~Aubakirova, F.~Capuano, P.~Kooijmans, S.~Palma, A.~Zouitine,\n  M.~Aractingi, C.~Pascal, M.~Russi, A.~Marafioti, S.~Alibert, M.~Cord,\n  T.~Wolf, and R.~Cadene.\n\\newblock Smolvla: A vision-language-action model for affordable and efficient\n  robotics, 2025.\n\n\\bibitem[Lipman et~al.(2023)Lipman, Chen, Ben-Hamu, Nickel, and\n  Le]{lipman2023flow}\nY.~Lipman, R.~T.~Q. Chen, H.~Ben-Hamu, M.~Nickel, and M.~Le.\n\\newblock Flow matching for generative modeling.\n\\newblock In \\emph{International Conference on Learning Representations\n  (ICLR)}, 2023.\n\n\\bibitem[Fei et~al.(2025{\\natexlab{a}})Fei, Wang, Shi, Dai, Cai, Qian, Ji, He,\n  Zhang, Fei, Fu, Gong, and Qiu]{fei2025liberoplus}\nS.~Fei, S.~Wang, J.~Shi, Z.~Dai, J.~Cai, P.~Qian, L.~Ji, X.~He, S.~Zhang,\n  Z.~Fei, J.~Fu, J.~Gong, and X.~Qiu.\n\\newblock Libero-plus: In-depth robustness analysis of vision-language-action\n  models, 2025{\\natexlab{a}}.\n\n\\bibitem[Fei et~al.(2025{\\natexlab{b}})Fei, Wang, Ji, Li, Zhang, Liu, Hou,\n  Gong, Zhao, and Qiu]{srpo2025}\nS.~Fei, S.~Wang, L.~Ji, A.~Li, S.~Zhang, L.~Liu, J.~Hou, J.~Gong, X.~Zhao, and\n  X.~Qiu.\n\\newblock Srpo: Self-referential policy optimization for vision-language-action\n  models, 2025{\\natexlab{b}}.\n\n\\bibitem[Zhang et~al.(2025{\\natexlab{a}})Zhang, Zhang, Jin, Zeng, Li, and\n  Wang]{robustvla2025}",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 237
    }
  }
}
```

</details>

---


### Assistant

_source line 112_

Now writing the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a1e02b6-c6f9-46bc-8517-4220435946da",
  "uuid": "6de27e76-7ad4-4412-835d-0b37ec89cc11",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015YCJEmZgvwDMymKJeR85pi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 139544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2012
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
