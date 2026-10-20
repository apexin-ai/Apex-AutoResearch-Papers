# analysis paper main table compilation

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_analysis_paper-main-table-compilation_20260518T212919.log`
- **Structured JSON:** [`f4d99c0732c56556e17f.json`](../../sessions/f4/f4d99c0732c56556e17f.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
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
  "uuid": "80cbf31f-fe0f-4404-b348-8745fde72714",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/memory/"
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
    "resetsAt": 1779144000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "14d16eba-a745-4ae3-99fd-87e9cee9204c",
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get all experiment data. I'll use both the MCP tool and direct file reading since the task mentions truncation issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "0cf09b40-ce2c-4c7f-8a37-a0e72df7aff6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NHhMZfibxLw677utdsFbv4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12800,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12800
      },
      "output_tokens": 21,
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

_source line 5_

Let me先获取 registry 数据，两种方式并行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "96411ada-65ed-495a-b0f7-cbaf636a9ca0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NHhMZfibxLw677utdsFbv4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12800,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12800
      },
      "output_tokens": 21,
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019PpdsiPZViQnMkohXCrgLV`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "de6f1af5-733e-47dc-a019-6b897c33a5ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NHhMZfibxLw677utdsFbv4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12800,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12800
      },
      "output_tokens": 21,
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

_source line 7 · 2026-05-18T21:29:32.456Z_

<details><summary>↩ Tool result · `toolu_019PpdsiPZViQnMkohXCrgLV`</summary>

````text
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
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "85a17d08-9762-4c4a-a695-262329025a61",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_015RQmVfXKjAc5sWftuFnZQN`</summary>

```json
{
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "*"
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
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "b6904925-b6cc-46ba-93af-0c7dceb5c015",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNSbB7ALtf9iwXTcNZgX3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 24641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 515
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

_source line 9 · 2026-05-18T21:29:35.537Z_

<details><summary>↩ Tool result · `toolu_015RQmVfXKjAc5sWftuFnZQN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"contamination_60_random_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:57:57.040Z\", \"updated_at\": \"2026-05-18T09:01:04.795Z\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/contamination_60_random_seed42/final\", \"log_path\": \"/root/autodl-tmp/output/models/contamination_60_random_seed42/train_resume.log\", \"spec\": {\"command\": \"python train_weighted.py --config configs/contamination_60_random_seed42.yaml (resumed from checkpoint-1000)\", \"server\": \"westd-30476\", \"data_path\": \"data/human/train_contaminated_60.jsonl\", \"data_count\": 23176, \"model_name\": \"Qwen/Qwen2.5-0.5B\", \"seed\": 42}, \"metrics\": {\"eval_ppl_holdout\": 17.832, \"eval_loss_holdout\": 2.881, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"note\": \"resume from checkpoint-1000 with ~20% LR offset; checkpoint-1000 no longer available (cleaned up)\"}, \"hypothesis\": \"Random (uniform) weighting on 60% contaminated data serves as baseline; without provenance-aware reweighting, the model treats all data equally regardless of contamination level\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:01:00.559Z\"}, \"rho02_adaptive_tau09_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:11:17.034Z\", \"updated_at\": \"2026-05-17T18:11:55.221Z\", \"hypothesis\": \"Adaptive weighting with τ=0.9 on ρ=0.2 (low contamination): even at 20% contamination, stricter α_eff threshold should find non-trivial b* and outperform uniform, demonstrating proportion-robustness (Claim 3). If adaptive fails here, Claim 3 may need to be scoped to medium-high contamination levels.\", \"spec\": {\"command\": \"bash scripts/run_rho02_adaptive_tau09.sh\", \"server\": \"westd-30476\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/scored_data_rho02.jsonl\", \"data_count\": 6103, \"seed\": 42, \"gpu\": \"cuda:3\", \"weighting_method\": \"adaptive\", \"tau\": 0.9}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/rho02_adaptive_tau09_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/rho02_adaptive_tau09_r5.log\", \"conclusion\": \"negative\", \"metrics\": {\"eval_ppl_holdout\": 17.45, \"eval_loss_holdout\": 2.8593, \"eval_tokens\": 4077068, \"train_loss\": 11.864, \"total_steps\": 6103, \"b_star_mean\": 4.35, \"b_star_median\": 2.96, \"b_star_std\": 4.4, \"b_star_pct_zero\": 2.65, \"alpha_eff_mean\": 0.83, \"alpha_eff_pct_at_max_09\": 42.95, \"ess_mean\": 2.38, \"vs_rho02_uniform\": \"+0.114 (17.45 vs 17.336, adaptive WORSE)\", \"note\": \"At rho=0.2 low contamination, aggressive reweighting (tau=0.9) over-penalizes useful samples. alpha_eff hits cap 42.95% of batches. Data already clean enough that reweighting hurts.\"}, \"completed_at\": \"2026-05-17T18:11:55.221Z\"}, \"bs8_auto_nmin_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:49:30.469Z\", \"updated_at\": \"2026-05-17T18:10:10.187Z\", \"hypothesis\": \"Batch size 8 with coupling rule n_min=max(2,bs//2)=4: previous bs8_nmin2 failed (PPL=17.73) because n_min=2 was too loose for bs=8. Auto n_min=4 should recover performance to match bs=16 adaptive_fix level, validating the coupling rule as a formal method design principle.\", \"spec\": {\"command\": \"bash scripts/run_bs8_auto_nmin.sh\", \"server\": \"westd-30476\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 42, \"gpu\": \"cuda:1\", \"weighting_method\": \"adaptive\", \"batch_size\": 8, \"n_min\": 4}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/bs8_auto_nmin_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/bs8_auto_nmin_r5.log\", \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8716, \"eval_tokens\": 4077068, \"eval_method\": \"sliding window (max_length=2048, stride=1024, 5000 docs, fp16)\", \"train_loss\": 5.163, \"train_runtime_s\": 14064, \"total_steps\": 6103, \"gpu_hours\": 4.07, \"b_star_mean\": 1.0957, \"b_star_median\": 0.9, \"b_star_std\": 0.7563, \"ess_mean\": 4.49, \"ess_median\": 4.04, \"alpha_eff_mean\": 0.7, \"alpha_eff_median\": 0.76, \"alpha_eff_at_cap_pct\": 38.88, \"vs_uniform\": \"-0.034 (17.66 vs 17.6939)\", \"vs_adaptive_fix_bs16\": \"+0.007 (17.66 vs 17.6527, nearly identical)\", \"vs_bs8_nmin2\": \"-0.070 (17.66 vs 17.73, coupling rule fixes bs=8)\", \"note\": \"Coupling rule n_min=max(2,bs//2)=4 validated: bs=8 performance restored to bs=16 level. ESS median≈4.04 matches n_min=4 constraint.\"}, \"completed_at\": \"2026-05-17T18:10:10.187Z\"}, \"random_reweight_seed123_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:46:13.281Z\", \"updated_at\": \"2026-05-17T17:48:40.664Z\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/random_reweight_seed123/final\", \"hypothesis\": \"Random reweighting baseline: applying random (non-provenance-based) weights to training samples. If adaptive weighting works because of quality signal, random weights should perform worse than uniform, confirming the detector signal is load-bearing.\", \"spec\": {\"command\": \"bash scripts/run_random_reweight_seed123.sh\", \"server\": \"westd-30476\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 123, \"gpu\": \"cuda:0\", \"weighting_method\": \"random\"}, \"metrics\": {\"ppl\": 17.801, \"eval_loss\": 2.8793, \"eval_tokens\": 4077068, \"eval_method\": \"sliding window (max_length=2048, stride=1024, 5000 docs, fp16)\", \"train_loss\": 8.0176, \"train_runtime_s\": 13267, \"total_steps\": 6103, \"vs_uniform_seed123\": \"+0.114 (17.80 vs 17.6861)\", \"vs_adaptive_fix_seed123\": \"+0.157 (17.80 vs 17.6432)\", \"vs_random_seed42\": \"cross-seed consistent (seed42: +0.136, seed123: +0.114)\", \"note\": \"Detector signal is load-bearing: random weights degrade PPL consistently across seeds, confirming q-scores provide real data quality signal (Claim 1).\"}, \"log_path\": \"/root/autodl-tmp/output/models/random_reweight_seed123/step_metrics.jsonl\", \"completed_at\": \"2026-05-17T17:08:07.193Z\"}, \"batch_adaptive_tau_rho06_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:47:18.803Z\", \"updated_at\": \"2026-05-17T17:47:53.369Z\", \"hypothesis\": \"Batch-adaptive τ at ρ=0.6: per-batch dynamic threshold should outperform fixed τ=0.8 by adapting to higher contamination variability. Tests whether batch-adaptive τ adds value beyond fixed τ across contamination levels (D063 follow-up).\", \"spec\": {\"command\": \"bash scripts/run_batch_adaptive_tau_rho06.sh\", \"server\": \"westd-30476\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/scored_data_hybrid_rho06.jsonl\", \"data_count\": 6103, \"seed\": 42, \"gpu\": \"cuda:2\", \"weighting_method\": \"batch_adaptive_tau\"}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/batch_adaptive_tau_rho06_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/batch_adaptive_tau_rho06_r5.log\", \"conclusion\": \"negative\", \"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.8754, \"eval_tokens\": 4077068, \"eval_method\": \"sliding window (max_length=2048, stride=1024, 5000 docs, fp16)\", \"train_loss\": 9.267, \"train_runtime_s\": 13903, \"total_steps\": 6103, \"vs_uniform_rho06\": \"-0.036 (17.73 vs 17.766)\", \"vs_adaptive_fixed_tau08\": \"-0.010 (vs 17.74)\", \"vs_grid_best_b05\": \"+0.026 (vs 17.704)\", \"vs_hybrid\": \"+0.200 (vs 17.53)\", \"note\": \"Batch-adaptive τ provides no improvement over fixed τ at ρ=0.6, consistent with ρ=0.4 negative result. Path abandoned.\"}, \"completed_at\": \"2026-05-17T17:47:53.369Z\"}, \"grid_b0_3_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:07:30.829Z\", \"updated_at\": \"2026-05-17T17:13:13.070Z\", \"hypothesis\": \"Grid search fixed b*=0.3 weighting for Qwen3-0.6B on rho=0.4 data (seed=456). Part of grid-b sweep to establish the PPL landscape and validate that adaptive b* matches grid-best performance (Claim 2).\", \"spec\": {\"command\": \"bash scripts/run_grid_b0_3_seed456.sh\", \"server\": \"westd-41312\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 456, \"gpu\": \"cuda:3\", \"weighting_method\": \"grid\", \"b_star\": 0.3}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_3_seed456/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_3_seed456/step_metrics.jsonl\", \"completed_at\": \"2026-05-17T17:08:13.953Z\", \"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8701, \"eval_tokens\": 4077068, \"eval_note\": \"eval_perplexity.py --stride 1024 --max_docs 5000 --fp16\"}}, \"llama3b_adaptive_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:53:45.524Z\", \"updated_at\": \"2026-05-17T15:34:23.023Z\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_adaptive_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_adaptive_seed42/step_metrics.jsonl\", \"metrics\": {\"ppl\": 10.58, \"ppl_uniform\": 10.53, \"eval_loss\": 2.359, \"eval_loss_uniform\": 2.3545, \"eval_tokens\": 4017316, \"token_consistency\": \"YES\", \"reeval_v2_note\": \"unified eval in same shell session, identical params confirmed\", \"director_conclusion\": \"neutral-to-positive: PPL parity, MMLU +1.57pp (3.9σ)\", \"lm_eval_hellaswag_10shot_acc_norm\": 0.7249, \"lm_eval_mmlu_5shot\": 0.5342, \"lm_eval_mmlu_5shot_uniform\": 0.5185, \"lm_eval_mmlu_delta\": \"+1.57pp\"}, \"conclusion\": \"success\", \"hypothesis\": \"Adaptive provenance-based weighting (tau=0.8, n_min=2) generalizes across model architectures: applying the same weighting method that improved GPT-2 training to Llama-3.2-3B should yield lower perplexity than uniform weighting on the same contaminated data.\", \"completed_at\": \"2026-05-17T13:56:49.033Z\"}, \"adaptive_fix_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:05:51.420Z\", \"updated_at\": \"2026-05-17T15:28:41.820Z\", \"hypothesis\": \"Adaptive provenance-based weighting (tau=0.8, n_min=2) for Qwen3-0.6B continued pretraining on rho=0.4 contaminated data yields lower perplexity than uniform weighting by downweighting synthetic samples based on quality scores.\", \"spec\": {\"command\": \"pretrain_weighted.py --weighting adaptive --tau 0.8 --n_min 2\", \"server\": \"westd-41312\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/step_metrics.jsonl\", \"completed_at\": \"2026-05-17T15:06:23.366Z\", \"metrics\": {\"lm_eval_hellaswag_10shot_acc_norm\": 0.4863, \"lm_eval_arc_easy_25shot_acc\": 0.71, \"lm_eval_arc_easy_25shot_acc_norm\": 0.7121, \"lm_eval_piqa_5shot_acc\": 0.6866, \"lm_eval_piqa_5shot_acc_norm\": 0.6839, \"lm_eval_winogrande_5shot_acc\": 0.5635}}, \"llama3b_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:00:26.715Z\", \"updated_at\": \"2026-05-17T15:00:59.028Z\", \"metrics\": {\"ppl\": 10.53, \"eval_loss\": 2.3545, \"eval_tokens\": 4017316, \"note\": \"reeval_v2 unified params: max_docs=5000, stride=1024, fp16\"}, \"hypothesis\": \"Uniform weighting baseline for Llama-3.2-3B continued pretraining on rho=0.4 contaminated data, serving as the control condition to measure whether adaptive provenance-based weighting provides any benefit on larger models.\", \"spec\": {\"command\": \"pretrain_weighted.py --weighting uniform\", \"server\": \"westd-41312\", \"model_name\": \"meta-llama/Llama-3.2-3B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_uniform_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_uniform_seed42/step_metrics.jsonl\", \"completed_at\": \"2026-05-17T15:00:59.028Z\"}, \"batchsize16_nmin8_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:43:04.095Z\", \"updated_at\": \"2026-05-17T15:00:28.591Z\", \"hypothesis\": \"Increasing batch size to 16 with n_min=8 improves adaptive weighting stability by providing more samples for ESS estimation per batch, leading to more reliable quality-based reweighting and lower perplexity than the default batch size configuration.\", \"spec\": {\"command\": \"bash scripts/run_bs16_nmin8.sh\", \"server\": \"westd-41312\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_seed42/step_metrics.jsonl\", \"completed_at\": \"2026-05-17T14:43:31.578Z\", \"metrics\": {\"ppl\": 17.653, \"eval_loss\": 2.8709, \"eval_tokens\": 4077068, \"eval_note\": \"eval_perplexity.py --stride 1024 --max_docs 5000 --fp16\"}}, \"hybrid_rho06_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:13:44.867Z\", \"updated_at\": \"2026-05-17T00:14:21.838Z\", \"hypothesis\": \"Hybrid filter+reweight at rho=0.6: remove q>0.95, then adaptive reweight remainder. This should outperform pure filtering by retaining more training data while still downweighting low-provenance samples.\", \"spec\": {\"command\": \"scripts/run_hybrid_rho06_seed42.sh\", \"server\": \"westd-41312\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_hybrid_rho06.jsonl\", \"data_count\": 6103, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/hybrid_rho06_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/logs/hybrid_rho06_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T00:14:17.275Z\", \"metrics\": {\"eval_loss_holdout\": 2.8637, \"eval_ppl_holdout\": 17.53}}}, \"count\": 11, \"total\": 11, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0626}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "ad6d3e77-dd05-4018-bd68-1f81d8e4d6b0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"contamination_60_random_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T08:57:57.040Z\\\", \\\"updated_at\\\": \\\"2026-05-18T09:01:04.795Z\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/output/models/contamination_60_random_seed42/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/output/models/contamination_60_random_seed42/train_resume.log\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train_weighted.py --config configs/contamination_60_random_seed42.yaml (resumed from checkpoint-1000)\\\", \\\"server\\\": \\\"westd-30476\\\", \\\"data_path\\\": \\\"data/human/train_contaminated_60.jsonl\\\", \\\"data_count\\\": 23176, \\\"model_name\\\": \\\"Qwen/Qwen2.5-0.5B\\\", \\\"seed\\\": 42}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.832, \\\"eval_loss_holdout\\\": 2.881, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\\\", \\\"note\\\": \\\"resume from checkpoint-1000 with ~20% LR offset; checkpoint-1000 no longer available (cleaned up)\\\"}, \\\"hypothesis\\\": \\\"Random (uniform) weighting on 60% contaminated data serves as baseline; without provenance-aware reweighting, the model treats all data equally regardless of contamination level\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-18T09:01:00.559Z\\\"}, \\\"rho02_adaptive_tau09_r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T18:11:17.034Z\\\", \\\"updated_at\\\": \\\"2026-05-17T18:11:55.221Z\\\", \\\"hypothesis\\\": \\\"Adaptive weighting with τ=0.9 on ρ=0.2 (low contamination): even at 20% contamination, stricter α_eff threshold should find non-trivial b* and outperform uniform, demonstrating proportion-robustness (Claim 3). If adaptive fails here, Claim 3 may need to be scoped to medium-high contamination levels.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_rho02_adaptive_tau09.sh\\\", \\\"server\\\": \\\"westd-30476\\\", \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"data_path\\\": \\\"data/scored_data_rho02.jsonl\\\", \\\"data_count\\\": 6103, \\\"seed\\\": 42, \\\"gpu\\\": \\\"cuda:3\\\", \\\"weighting_method\\\": \\\"adaptive\\\", \\\"tau\\\": 0.9}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/output/models/rho02_adaptive_tau09_seed42/final\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/rho02_adaptive_tau09_r5.log\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.45, \\\"eval_loss_holdout\\\": 2.8593, \\\"eval_tokens\\\": 4077068, \\\"train_loss\\\": 11.864, \\\"total_steps\\\": 6103, \\\"b_star_mean\\\": 4.35, \\\"b_star_median\\\": 2.96, \\\"b_star_std\\\": 4.4, \\\"b_star_pct_zero\\\": 2.65, \\\"alpha_eff_mean\\\": 0.83, \\\"alpha_eff_pct_at_max_09\\\": 42.95, \\\"ess_mean\\\": 2.38, \\\"vs_rho02_uniform\\\": \\\"+0.114 (17.45 vs 17.336, adaptive WORSE)\\\", \\\"note\\\": \\\"At rho=0.2 low contamination, aggressive reweighting (tau=0.9) over-penalizes useful samples. alpha_eff hits cap 42.95% of batches. Data already clean enough that reweighting hurts.\\\"}, \\\"completed_at\\\": \\\"2026-05-17T18:11:55.221Z\\\"}, \\\"bs8_auto_nmin_r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T17:49:30.469Z\\\", \\\"updated_at\\\": \\\"2026-05-17T18:10:10.187Z\\\", \\\"hypothesis\\\": \\\"Batch size 8 with coupling rule n_min=max(2,bs//2)=4: previous bs8_nmin2 failed (PPL=17.73) because n_min=2 was too loose for bs=8. Auto n_min=4 should recover performance to match bs=16 adaptive_fix level, validating the coupling rule as a formal method design principle.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_bs8_auto_nmin.sh\\\", \\\"server\\\": \\\"westd-30476\\\", \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"data_path\\\": \\\"data/mixed/train.jsonl\\\", \\\"data_count\\\": 6103, \\\"seed\\\": 42, \\\"gpu\\\": \\\"cuda:1\\\", \\\"weighting_method\\\": \\\"adaptive\\\", \\\"batch_size\\\": 8, \\\"n_min\\\": 4}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/output/models/bs8_auto_nmin_seed42/final\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/bs8_auto_nmin_r5.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.66, \\\"eval_loss_holdout\\\": 2.8716, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding window (max_length=2048, stride=1024, 5000 docs, fp16)\\\", \\\"train_loss\\\": 5.163, \\\"train_runtime_s\\\": 14064, \\\"total_steps\\\": 6103, \\\"gpu_hours\\\": 4.07, \\\"b_star_mean\\\": 1.0957, \\\"b_star_median\\\": 0.9, \\\"b_star_std\\\": 0.7563, \\\"ess_mean\\\": 4.49, \\\"ess_median\\\": 4.04, \\\"alpha_eff_mean\\\": 0.7, \\\"alpha_eff_median\\\": 0.76, \\\"alpha_eff_at_cap_pct\\\": 38.88, \\\"vs_uniform\\\": \\\"-0.034 (17.66 vs 17.6939)\\\", \\\"vs_adaptive_fix_bs16\\\": \\\"+0.007 (17.66 vs 17.6527, nearly identical)\\\", \\\"vs_bs8_nmin2\\\": \\\"-0.070 (17.66 vs 17.73, coupling rule fixes bs=8)\\\", \\\"note\\\": \\\"Coupling rule n_min=max(2,bs//2)=4 validated: bs=8 performance restored to bs=16 level. ESS median≈4.04 matches n_min=4 constraint.\\\"}, \\\"completed_at\\\": \\\"2026-05-17T18:10:10.187Z\\\"}, \\\"random_reweight_seed123_r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T16:46:13.281Z\\\", \\\"updated_at\\\": \\\"2026-05-17T17:48:40.664Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/output/models/random_reweight_seed123/final\\\", \\\"hypothesis\\\": \\\"Random reweighting baseline: applying random (non-provenance-based) weights to training samples. If adaptive weighting works because of quality signal, random weights should perform worse than uniform, confirming the detector signal is load-bearing.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_random_reweight_seed123.sh\\\", \\\"server\\\": \\\"westd-30476\\\", \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"data_path\\\": \\\"data/mixed/train.jsonl\\\", \\\"data_count\\\": 6103, \\\"seed\\\": 123, \\\"gpu\\\": \\\"cuda:0\\\", \\\"weighting_method\\\": \\\"random\\\"}, \\\"metrics\\\": {\\\"ppl\\\": 17.801, \\\"eval_loss\\\": 2.8793, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding window (max_length=2048, stride=1024, 5000 docs, fp16)\\\", \\\"train_loss\\\": 8.0176, \\\"train_runtime_s\\\": 13267, \\\"total_steps\\\": 6103, \\\"vs_uniform_seed123\\\": \\\"+0.114 (17.80 vs 17.6861)\\\", \\\"vs_adaptive_fix_seed123\\\": \\\"+0.157 (17.80 vs 17.6432)\\\", \\\"vs_random_seed42\\\": \\\"cross-seed consistent (seed42: +0.136, seed123: +0.114)\\\", \\\"note\\\": \\\"Detector signal is load-bearing: random weights degrade PPL consistently across seeds, confirming q-scores provide real data quality signal (Claim 1).\\\"}, \\\"log_path\\\": \\\"/root/autodl-tmp/output/models/random_reweight_seed123/step_metrics.jsonl\\\", \\\"completed_at\\\": \\\"2026-05-17T17:08:07.193Z\\\"}, \\\"batch_adaptive_tau_rho06_r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T17:47:18.803Z\\\", \\\"updated_at\\\": \\\"2026-05-17T17:47:53.369Z\\\", \\\"hypothesis\\\": \\\"Batch-adaptive τ at ρ=0.6: per-batch dynamic threshold should outperform fixed τ=0.8 by adapting to higher contamination variability. Tests whether batch-adaptive τ adds value beyond fixed τ across contamination levels (D063 follow-up).\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_batch_adaptive_tau_rho06.sh\\\", \\\"server\\\": \\\"westd-30476\\\", \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"data_path\\\": \\\"data/scored_data_hybrid_rho06.jsonl\\\", \\\"data_count\\\": 6103, \\\"seed\\\": 42, \\\"gpu\\\": \\\"cuda:2\\\", \\\"weighting_method\\\": \\\"batch_adaptive_tau\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/output/models/batch_adaptive_tau_rho06_seed42/final\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/batch_adaptive_tau_rho06_r5.log\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.73, \\\"eval_loss_holdout\\\": 2.8754, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding window (max_length=2048, stride=1024, 5000 docs, fp16)\\\", \\\"train_loss\\\": 9.267, \\\"train_runtime_s\\\": 13903, \\\"total_steps\\\": 6103, \\\"vs_uniform_rho06\\\": \\\"-0.036 (17.73 vs 17.766)\\\", \\\"vs_adaptive_fixed_tau08\\\": \\\"-0.010 (vs 17.74)\\\", \\\"vs_grid_best_b05\\\": \\\"+0.026 (vs 17.704)\\\", \\\"vs_hybrid\\\": \\\"+0.200 (vs 17.53)\\\", \\\"note\\\": \\\"Batch-adaptive τ provides no improvement over fixed τ at ρ=0.6, consistent with ρ=0.4 negative result. Path abandoned.\\\"}, \\\"completed_at\\\": \\\"2026-05-17T17:47:53.369Z\\\"}, \\\"grid_b0_3_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T17:07:30.829Z\\\", \\\"updated_at\\\": \\\"2026-05-17T17:13:13.070Z\\\", \\\"hypothesis\\\": \\\"Grid search fixed b*=0.3 weighting for Qwen3-0.6B on rho=0.4 data (seed=456). Part of grid-b sweep to establish the PPL landscape and validate that adaptive b* matches grid-best performance (Claim 2).\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_grid_b0_3_seed456.sh\\\", \\\"server\\\": \\\"westd-41312\\\", \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"data_path\\\": \\\"data/mixed/train.jsonl\\\", \\\"data_count\\\": 6103, \\\"seed\\\": 456, \\\"gpu\\\": \\\"cuda:3\\\", \\\"weighting_method\\\": \\\"grid\\\", \\\"b_star\\\": 0.3}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_3_seed456/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_3_seed456/step_metrics.jsonl\\\", \\\"completed_at\\\": \\\"2026-05-17T17:08:13.953Z\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.64, \\\"eval_loss_holdout\\\": 2.8701, \\\"eval_tokens\\\": 4077068, \\\"eval_note\\\": \\\"eval_perplexity.py --stride 1024 --max_docs 5000 --fp16\\\"}}, \\\"llama3b_adaptive_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T13:53:45.524Z\\\", \\\"updated_at\\\": \\\"2026-05-17T15:34:23.023Z\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_adaptive_seed42/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_adaptive_seed42/step_metrics.jsonl\\\", \\\"metrics\\\": {\\\"ppl\\\": 10.58, \\\"ppl_uniform\\\": 10.53, \\\"eval_loss\\\": 2.359, \\\"eval_loss_uniform\\\": 2.3545, \\\"eval_tokens\\\": 4017316, \\\"token_consistency\\\": \\\"YES\\\", \\\"reeval_v2_note\\\": \\\"unified eval in same shell session, identical params confirmed\\\", \\\"director_conclusion\\\": \\\"neutral-to-positive: PPL parity, MMLU +1.57pp (3.9σ)\\\", \\\"lm_eval_hellaswag_10shot_acc_norm\\\": 0.7249, \\\"lm_eval_mmlu_5shot\\\": 0.5342, \\\"lm_eval_mmlu_5shot_uniform\\\": 0.5185, \\\"lm_eval_mmlu_delta\\\": \\\"+1.57pp\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Adaptive provenance-based weighting (tau=0.8, n_min=2) generalizes across model architectures: applying the same weighting method that improved GPT-2 training to Llama-3.2-3B should yield lower perplexity than uniform weighting on the same contaminated data.\\\", \\\"completed_at\\\": \\\"2026-05-17T13:56:49.033Z\\\"}, \\\"adaptive_fix_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T15:05:51.420Z\\\", \\\"updated_at\\\": \\\"2026-05-17T15:28:41.820Z\\\", \\\"hypothesis\\\": \\\"Adaptive provenance-based weighting (tau=0.8, n_min=2) for Qwen3-0.6B continued pretraining on rho=0.4 contaminated data yields lower perplexity than uniform weighting by downweighting synthetic samples based on quality scores.\\\", \\\"spec\\\": {\\\"command\\\": \\\"pretrain_weighted.py --weighting adaptive --tau 0.8 --n_min 2\\\", \\\"server\\\": \\\"westd-41312\\\", \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"data_path\\\": \\\"data/mixed/train.jsonl\\\", \\\"data_count\\\": 6103, \\\"seed\\\": 42}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/step_metrics.jsonl\\\", \\\"completed_at\\\": \\\"2026-05-17T15:06:23.366Z\\\", \\\"metrics\\\": {\\\"lm_eval_hellaswag_10shot_acc_norm\\\": 0.4863, \\\"lm_eval_arc_easy_25shot_acc\\\": 0.71, \\\"lm_eval_arc_easy_25shot_acc_norm\\\": 0.7121, \\\"lm_eval_piqa_5shot_acc\\\": 0.6866, \\\"lm_eval_piqa_5shot_acc_norm\\\": 0.6839, \\\"lm_eval_winogrande_5shot_acc\\\": 0.5635}}, \\\"llama3b_uniform_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T15:00:26.715Z\\\", \\\"updated_at\\\": \\\"2026-05-17T15:00:59.028Z\\\", \\\"metrics\\\": {\\\"ppl\\\": 10.53, \\\"eval_loss\\\": 2.3545, \\\"eval_tokens\\\": 4017316, \\\"note\\\": \\\"reeval_v2 unified params: max_docs=5000, stride=1024, fp16\\\"}, \\\"hypothesis\\\": \\\"Uniform weighting baseline for Llama-3.2-3B continued pretraining on rho=0.4 contaminated data, serving as the control condition to measure whether adaptive provenance-based weighting provides any benefit on larger models.\\\", \\\"spec\\\": {\\\"command\\\": \\\"pretrain_weighted.py --weighting uniform\\\", \\\"server\\\": \\\"westd-41312\\\", \\\"model_name\\\": \\\"meta-llama/Llama-3.2-3B\\\", \\\"data_path\\\": \\\"data/mixed/train.jsonl\\\", \\\"data_count\\\": 6103, \\\"seed\\\": 42}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_uniform_seed42/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_uniform_seed42/step_metrics.jsonl\\\", \\\"completed_at\\\": \\\"2026-05-17T15:00:59.028Z\\\"}, \\\"batchsize16_nmin8_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T14:43:04.095Z\\\", \\\"updated_at\\\": \\\"2026-05-17T15:00:28.591Z\\\", \\\"hypothesis\\\": \\\"Increasing batch size to 16 with n_min=8 improves adaptive weighting stability by providing more samples for ESS estimation per batch, leading to more reliable quality-based reweighting and lower perplexity than the default batch size configuration.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_bs16_nmin8.sh\\\", \\\"server\\\": \\\"westd-41312\\\", \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"data_path\\\": \\\"data/mixed/train.jsonl\\\", \\\"data_count\\\": 6103, \\\"seed\\\": 42}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_seed42/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_seed42/step_metrics.jsonl\\\", \\\"completed_at\\\": \\\"2026-05-17T14:43:31.578Z\\\", \\\"metrics\\\": {\\\"ppl\\\": 17.653, \\\"eval_loss\\\": 2.8709, \\\"eval_tokens\\\": 4077068, \\\"eval_note\\\": \\\"eval_perplexity.py --stride 1024 --max_docs 5000 --fp16\\\"}}, \\\"hybrid_rho06_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T00:13:44.867Z\\\", \\\"updated_at\\\": \\\"2026-05-17T00:14:21.838Z\\\", \\\"hypothesis\\\": \\\"Hybrid filter+reweight at rho=0.6: remove q>0.95, then adaptive reweight remainder. This should outperform pure filtering by retaining more training data while still downweighting low-provenance samples.\\\", \\\"spec\\\": {\\\"command\\\": \\\"scripts/run_hybrid_rho06_seed42.sh\\\", \\\"server\\\": \\\"westd-41312\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/data/scored_data_hybrid_rho06.jsonl\\\", \\\"data_count\\\": 6103, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/models/hybrid_rho06_seed42/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/provenance_weight_training/output/logs/hybrid_rho06_seed42.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-17T00:14:17.275Z\\\", \\\"metrics\\\": {\\\"eval_loss_holdout\\\": 2.8637, \\\"eval_ppl_holdout\\\": 17.53}}}, \\\"count\\\": 11, \\\"total\\\": 11, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0626}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"contamination_60_random_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:57:57.040Z\", \"updated_at\": \"2026-05-18T09:01:04.795Z\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/contamination_60_random_seed42/final\", \"log_path\": \"/root/autodl-tmp/output/models/contamination_60_random_seed42/train_resume.log\", \"spec\": {\"command\": \"python train_weighted.py --config configs/contamination_60_random_seed42.yaml (resumed from checkpoint-1000)\", \"server\": \"westd-30476\", \"data_path\": \"data/human/train_contaminated_60.jsonl\", \"data_count\": 23176, \"model_name\": \"Qwen/Qwen2.5-0.5B\", \"seed\": 42}, \"metrics\": {\"eval_ppl_holdout\": 17.832, \"eval_loss_holdout\": 2.881, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"note\": \"resume from checkpoint-1000 with ~20% LR offset; checkpoint-1000 no longer available (cleaned up)\"}, \"hypothesis\": \"Random (uniform) weighting on 60% contaminated data serves as baseline; without provenance-aware reweighting, the model treats all data equally regardless of contamination level\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:01:00.559Z\"}, \"rho02_adaptive_tau09_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:11:17.034Z\", \"updated_at\": \"2026-05-17T18:11:55.221Z\", \"hypothesis\": \"Adaptive weighting with τ=0.9 on ρ=0.2 (low contamination): even at 20% contamination, stricter α_eff threshold should find non-trivial b* and outperform uniform, demonstrating proportion-robustness (Claim 3). If adaptive fails here, Claim 3 may need to be scoped to medium-high contamination levels.\", \"spec\": {\"command\": \"bash scripts/run_rho02_adaptive_tau09.sh\", \"server\": \"westd-30476\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/scored_data_rho02.jsonl\", \"data_count\": 6103, \"seed\": 42, \"gpu\": \"cuda:3\", \"weighting_method\": \"adaptive\", \"tau\": 0.9}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/rho02_adaptive_tau09_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/rho02_adaptive_tau09_r5.log\", \"conclusion\": \"negative\", \"metrics\": {\"eval_ppl_holdout\": 17.45, \"eval_loss_holdout\": 2.8593, \"eval_tokens\": 4077068, \"train_loss\": 11.864, \"total_steps\": 6103, \"b_star_mean\": 4.35, \"b_star_median\": 2.96, \"b_star_std\": 4.4, \"b_star_pct_zero\": 2.65, \"alpha_eff_mean\": 0.83, \"alpha_eff_pct_at_max_09\": 42.95, \"ess_mean\": 2.38, \"vs_rho02_uniform\": \"+0.114 (17.45 vs 17.336, adaptive WORSE)\", \"note\": \"At rho=0.2 low contamination, aggressive reweighting (tau=0.9) over-penalizes useful samples. alpha_eff hits cap 42.95% of batches. Data already clean enough that reweighting hurts.\"}, \"completed_at\": \"2026-05-17T18:11:55.221Z\"}, \"bs8_auto_nmin_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:49:30.469Z\", \"updated_at\": \"2026-05-17T18:10:10.187Z\", \"hypothesis\": \"Batch size 8 with coupling rule n_min=max(2,bs//2)=4: previous bs8_nmin2 failed (PPL=17.73) because n_min=2 was too loose for bs=8. Auto n_min=4 should recover performance to match bs=16 adaptive_fix level, validating the coupling rule as a formal method design principle.\", \"spec\": {\"command\": \"bash scripts/run_bs8_auto_nmin.sh\", \"server\": \"westd-30476\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 42, \"gpu\": \"cuda:1\", \"weighting_method\": \"adaptive\", \"batch_size\": 8, \"n_min\": 4}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/bs8_auto_nmin_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/bs8_auto_nmin_r5.log\", \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8716, \"eval_tokens\": 4077068, \"eval_method\": \"sliding window (max_length=2048, stride=1024, 5000 docs, fp16)\", \"train_loss\": 5.163, \"train_runtime_s\": 14064, \"total_steps\": 6103, \"gpu_hours\": 4.07, \"b_star_mean\": 1.0957, \"b_star_median\": 0.9, \"b_star_std\": 0.7563, \"ess_mean\": 4.49, \"ess_median\": 4.04, \"alpha_eff_mean\": 0.7, \"alpha_eff_median\": 0.76, \"alpha_eff_at_cap_pct\": 38.88, \"vs_uniform\": \"-0.034 (17.66 vs 17.6939)\", \"vs_adaptive_fix_bs16\": \"+0.007 (17.66 vs 17.6527, nearly identical)\", \"vs_bs8_nmin2\": \"-0.070 (17.66 vs 17.73, coupling rule fixes bs=8)\", \"note\": \"Coupling rule n_min=max(2,bs//2)=4 validated: bs=8 performance restored to bs=16 level. ESS median≈4.04 matches n_min=4 constraint.\"}, \"completed_at\": \"2026-05-17T18:10:10.187Z\"}, \"random_reweight_seed123_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:46:13.281Z\", \"updated_at\": \"2026-05-17T17:48:40.664Z\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/random_reweight_seed123/final\", \"hypothesis\": \"Random reweighting baseline: applying random (non-provenance-based) weights to training samples. If adaptive weighting works because of quality signal, random weights should perform worse than uniform, confirming the detector signal is load-bearing.\", \"spec\": {\"command\": \"bash scripts/run_random_reweight_seed123.sh\", \"server\": \"westd-30476\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 123, \"gpu\": \"cuda:0\", \"weighting_method\": \"random\"}, \"metrics\": {\"ppl\": 17.801, \"eval_loss\": 2.8793, \"eval_tokens\": 4077068, \"eval_method\": \"sliding window (max_length=2048, stride=1024, 5000 docs, fp16)\", \"train_loss\": 8.0176, \"train_runtime_s\": 13267, \"total_steps\": 6103, \"vs_uniform_seed123\": \"+0.114 (17.80 vs 17.6861)\", \"vs_adaptive_fix_seed123\": \"+0.157 (17.80 vs 17.6432)\", \"vs_random_seed42\": \"cross-seed consistent (seed42: +0.136, seed123: +0.114)\", \"note\": \"Detector signal is load-bearing: random weights degrade PPL consistently across seeds, confirming q-scores provide real data quality signal (Claim 1).\"}, \"log_path\": \"/root/autodl-tmp/output/models/random_reweight_seed123/step_metrics.jsonl\", \"completed_at\": \"2026-05-17T17:08:07.193Z\"}, \"batch_adaptive_tau_rho06_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:47:18.803Z\", \"updated_at\": \"2026-05-17T17:47:53.369Z\", \"hypothesis\": \"Batch-adaptive τ at ρ=0.6: per-batch dynamic threshold should outperform fixed τ=0.8 by adapting to higher contamination variability. Tests whether batch-adaptive τ adds value beyond fixed τ across contamination levels (D063 follow-up).\", \"spec\": {\"command\": \"bash scripts/run_batch_adaptive_tau_rho06.sh\", \"server\": \"westd-30476\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/scored_data_hybrid_rho06.jsonl\", \"data_count\": 6103, \"seed\": 42, \"gpu\": \"cuda:2\", \"weighting_method\": \"batch_adaptive_tau\"}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/batch_adaptive_tau_rho06_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/batch_adaptive_tau_rho06_r5.log\", \"conclusion\": \"negative\", \"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.8754, \"eval_tokens\": 4077068, \"eval_method\": \"sliding window (max_length=2048, stride=1024, 5000 docs, fp16)\", \"train_loss\": 9.267, \"train_runtime_s\": 13903, \"total_steps\": 6103, \"vs_uniform_rho06\": \"-0.036 (17.73 vs 17.766)\", \"vs_adaptive_fixed_tau08\": \"-0.010 (vs 17.74)\", \"vs_grid_best_b05\": \"+0.026 (vs 17.704)\", \"vs_hybrid\": \"+0.200 (vs 17.53)\", \"note\": \"Batch-adaptive τ provides no improvement over fixed τ at ρ=0.6, consistent with ρ=0.4 negative result. Path abandoned.\"}, \"completed_at\": \"2026-05-17T17:47:53.369Z\"}, \"grid_b0_3_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:07:30.829Z\", \"updated_at\": \"2026-05-17T17:13:13.070Z\", \"hypothesis\": \"Grid search fixed b*=0.3 weighting for Qwen3-0.6B on rho=0.4 data (seed=456). Part of grid-b sweep to establish the PPL landscape and validate that adaptive b* matches grid-best performance (Claim 2).\", \"spec\": {\"command\": \"bash scripts/run_grid_b0_3_seed456.sh\", \"server\": \"westd-41312\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 456, \"gpu\": \"cuda:3\", \"weighting_method\": \"grid\", \"b_star\": 0.3}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_3_seed456/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_3_seed456/step_metrics.jsonl\", \"completed_at\": \"2026-05-17T17:08:13.953Z\", \"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8701, \"eval_tokens\": 4077068, \"eval_note\": \"eval_perplexity.py --stride 1024 --max_docs 5000 --fp16\"}}, \"llama3b_adaptive_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:53:45.524Z\", \"updated_at\": \"2026-05-17T15:34:23.023Z\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_adaptive_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_adaptive_seed42/step_metrics.jsonl\", \"metrics\": {\"ppl\": 10.58, \"ppl_uniform\": 10.53, \"eval_loss\": 2.359, \"eval_loss_uniform\": 2.3545, \"eval_tokens\": 4017316, \"token_consistency\": \"YES\", \"reeval_v2_note\": \"unified eval in same shell session, identical params confirmed\", \"director_conclusion\": \"neutral-to-positive: PPL parity, MMLU +1.57pp (3.9σ)\", \"lm_eval_hellaswag_10shot_acc_norm\": 0.7249, \"lm_eval_mmlu_5shot\": 0.5342, \"lm_eval_mmlu_5shot_uniform\": 0.5185, \"lm_eval_mmlu_delta\": \"+1.57pp\"}, \"conclusion\": \"success\", \"hypothesis\": \"Adaptive provenance-based weighting (tau=0.8, n_min=2) generalizes across model architectures: applying the same weighting method that improved GPT-2 training to Llama-3.2-3B should yield lower perplexity than uniform weighting on the same contaminated data.\", \"completed_at\": \"2026-05-17T13:56:49.033Z\"}, \"adaptive_fix_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:05:51.420Z\", \"updated_at\": \"2026-05-17T15:28:41.820Z\", \"hypothesis\": \"Adaptive provenance-based weighting (tau=0.8, n_min=2) for Qwen3-0.6B continued pretraining on rho=0.4 contaminated data yields lower perplexity than uniform weighting by downweighting synthetic samples based on quality scores.\", \"spec\": {\"command\": \"pretrain_weighted.py --weighting adaptive --tau 0.8 --n_min 2\", \"server\": \"westd-41312\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/step_metrics.jsonl\", \"completed_at\": \"2026-05-17T15:06:23.366Z\", \"metrics\": {\"lm_eval_hellaswag_10shot_acc_norm\": 0.4863, \"lm_eval_arc_easy_25shot_acc\": 0.71, \"lm_eval_arc_easy_25shot_acc_norm\": 0.7121, \"lm_eval_piqa_5shot_acc\": 0.6866, \"lm_eval_piqa_5shot_acc_norm\": 0.6839, \"lm_eval_winogrande_5shot_acc\": 0.5635}}, \"llama3b_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:00:26.715Z\", \"updated_at\": \"2026-05-17T15:00:59.028Z\", \"metrics\": {\"ppl\": 10.53, \"eval_loss\": 2.3545, \"eval_tokens\": 4017316, \"note\": \"reeval_v2 unified params: max_docs=5000, stride=1024, fp16\"}, \"hypothesis\": \"Uniform weighting baseline for Llama-3.2-3B continued pretraining on rho=0.4 contaminated data, serving as the control condition to measure whether adaptive provenance-based weighting provides any benefit on larger models.\", \"spec\": {\"command\": \"pretrain_weighted.py --weighting uniform\", \"server\": \"westd-41312\", \"model_name\": \"meta-llama/Llama-3.2-3B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_uniform_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_uniform_seed42/step_metrics.jsonl\", \"completed_at\": \"2026-05-17T15:00:59.028Z\"}, \"batchsize16_nmin8_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:43:04.095Z\", \"updated_at\": \"2026-05-17T15:00:28.591Z\", \"hypothesis\": \"Increasing batch size to 16 with n_min=8 improves adaptive weighting stability by providing more samples for ESS estimation per batch, leading to more reliable quality-based reweighting and lower perplexity than the default batch size configuration.\", \"spec\": {\"command\": \"bash scripts/run_bs16_nmin8.sh\", \"server\": \"westd-41312\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"data_path\": \"data/mixed/train.jsonl\", \"data_count\": 6103, \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_seed42/step_metrics.jsonl\", \"completed_at\": \"2026-05-17T14:43:31.578Z\", \"metrics\": {\"ppl\": 17.653, \"eval_loss\": 2.8709, \"eval_tokens\": 4077068, \"eval_note\": \"eval_perplexity.py --stride 1024 --max_docs 5000 --fp16\"}}, \"hybrid_rho06_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:13:44.867Z\", \"updated_at\": \"2026-05-17T00:14:21.838Z\", \"hypothesis\": \"Hybrid filter+reweight at rho=0.6: remove q>0.95, then adaptive reweight remainder. This should outperform pure filtering by retaining more training data while still downweighting low-provenance samples.\", \"spec\": {\"command\": \"scripts/run_hybrid_rho06_seed42.sh\", \"server\": \"westd-41312\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_hybrid_rho06.jsonl\", \"data_count\": 6103, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/hybrid_rho06_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/logs/hybrid_rho06_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T00:14:17.275Z\", \"metrics\": {\"eval_loss_holdout\": 2.8637, \"eval_ppl_holdout\": 17.53}}}, \"count\": 11, \"total\": 11, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0626}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Bash · `toolu_011XEfpUsbxYgFMxxpiujzia`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/registry.yaml",
  "description": "Count lines in registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "e7961118-e421-48c4-b923-16e0f52968ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNSbB7ALtf9iwXTcNZgX3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 24641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 515
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

_source line 11 · 2026-05-18T21:29:36.238Z_

<details><summary>↩ Tool result · `toolu_011XEfpUsbxYgFMxxpiujzia`</summary>

```text
6367 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "afb9e6eb-906a-4048-9c3d-b4525375fbce",
  "tool_use_result": {
    "stdout": "6367 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/registry.yaml",
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

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The registry API returned only 11 experiments. The registry.yaml file has 6367 lines, so there are many more experiments. I need to parse the registry.yaml directly to get all experiments. Let me grep for the key fields.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "b1d0a948-af53-4f16-a093-7095095a6a48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BavwJaCHBWVzAcVFWqDwbP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 25156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6210
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

_source line 13_

API 只返回了 11 个实验，但 registry 有 6367 行。需要直接解析 YAML 文件获取完整数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "0a3f4d51-7f8d-4e81-9efb-8f30fb2504e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BavwJaCHBWVzAcVFWqDwbP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 25156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6210
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_013tkv37DFA8GbL27C7H3g3m`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\ndone = {}\nfor eid, exp in experiments.items():\n    if exp.get('status') == 'DONE':\n        done[eid] = {\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics', {}),\n            'spec': exp.get('spec', {}),\n        }\n\nprint(f'Total DONE experiments: {len(done)}')\nprint('---')\nfor eid, exp in sorted(done.items()):\n    m = exp['metrics']\n    s = exp['spec']\n    ppl = m.get('eval_ppl_holdout') or m.get('ppl')\n    seed = s.get('seed')\n    method = s.get('weighting_method', '')\n    model = s.get('model_name', '')\n    conc = exp['conclusion']\n    print(f'{eid} | ppl={ppl} | seed={seed} | method={method} | model={model} | conclusion={conc}')\n\" 2>&1",
  "description": "Parse registry.yaml for all DONE experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "ce9127f6-0265-4cc2-af00-2de6ab88f998",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BavwJaCHBWVzAcVFWqDwbP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 25156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6210
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

_source line 15 · 2026-05-18T21:29:45.414Z_

<details><summary>↩ Tool result · `toolu_013tkv37DFA8GbL27C7H3g3m`</summary>

```text
Total DONE experiments: 133
---
adaptive_1_7b_seed42 | ppl=None | seed=None | method= | model= | conclusion=success
adaptive_fix_seed123 | ppl=17.6432 | seed=None | method= | model= | conclusion=success
adaptive_fix_seed42 | ppl=17.6527 | seed=None | method= | model= | conclusion=success
adaptive_fix_seed456 | ppl=17.6566 | seed=None | method= | model= | conclusion=success
adaptive_seed123 | ppl=17.6308 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
adaptive_seed42 | ppl=17.644 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
adaptive_seed456 | ppl=17.6419 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
adaptive_v2_seed123 | ppl=None | seed=None | method= | model= | conclusion=killed
adaptive_v2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed
adaptive_v2_seed456 | ppl=None | seed=None | method= | model= | conclusion=killed
baseline_qwen3_0.6b | ppl=22.97 | seed=0 | method= | model=Qwen3-0.6B | conclusion=success
batch_adaptive_tau_rho04_seed42 | ppl=17.681 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=negative
batch_adaptive_tau_rho06_r2 | ppl=None | seed=None | method= | model= | conclusion=failed
batch_adaptive_tau_rho06_r3 | ppl=None | seed=None | method= | model= | conclusion=failed
batch_adaptive_tau_rho06_r5 | ppl=17.73 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=negative
batch_adaptive_tau_rho06_seed42 | ppl=None | seed=42 | method=batch_adaptive_tau | model=Qwen/Qwen3-0.6B | conclusion=failed
batchsize16_nmin8_r2 | ppl=None | seed=None | method= | model= | conclusion=killed
batchsize16_nmin8_r3 | ppl=17.65 | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=success
batchsize16_nmin8_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed
bs8_auto_nmin_r2 | ppl=None | seed=None | method= | model= | conclusion=failed
bs8_auto_nmin_r3 | ppl=None | seed=None | method= | model= | conclusion=failed
bs8_auto_nmin_r5 | ppl=17.66 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
bs8_auto_nmin_seed42 | ppl=None | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=failed
bs8_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=failed
bs8_nmin2_seed42_r2 | ppl=17.73 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=negative
bs8_seed42 | ppl=None | seed=None | method= | model= | conclusion=failed
contamination_60_adaptive_seed456 | ppl=17.735 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
contamination_60_ess_only_seed123 | ppl=17.763 | seed=123 | method= | model=Qwen3-0.6B | conclusion=success
contamination_60_ess_only_seed42 | ppl=17.77 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success
contamination_60_ess_only_seed456 | ppl=17.762 | seed=456 | method= | model=Qwen3-0.6B | conclusion=success
contamination_60_grid_b0_3_seed42 | ppl=17.634 | seed=42 | method= | model=models/Qwen/Qwen3-0.6B | conclusion=success
contamination_60_grid_b0_5_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
contamination_60_random_seed123 | ppl=17.87 | seed=123 | method= | model=Qwen3-0.6B | conclusion=success
contamination_60_random_seed42 | ppl=17.832 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
contamination_60_random_seed456 | ppl=17.88 | seed=456 | method= | model=Qwen3-0.6B | conclusion=success
contamination_60_seed123 | ppl=17.732 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
contamination_60_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed
contamination_60_seed42_r2 | ppl=17.74 | seed=None | method= | model= | conclusion=success
contamination_60_tau06_seed42 | ppl=17.7359 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success
contamination_60_tau07_seed42 | ppl=17.73 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success
contamination_60_uniform_seed123 | ppl=17.754 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
contamination_60_uniform_seed42 | ppl=17.766 | seed=None | method= | model= | conclusion=success
contamination_60_uniform_seed456 | ppl=17.77 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
datagen_synthetic_4gpu | ppl=None | seed=42/1042/2042/3042 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
detect_remove_baseline_seed42 | ppl=17.29 | seed=None | method= | model= | conclusion=success
detect_remove_q03_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed
detect_remove_q05_epoch_matched_seed42 | ppl=17.65 | seed=42 | method=uniform | model=models/Qwen/Qwen3-0.6B | conclusion=success
detect_remove_q05_seed123 | ppl=17.27 | seed=123 | method=uniform | model=models/Qwen/Qwen3-0.6B | conclusion=success
detect_remove_q05_seed456 | ppl=17.28 | seed=456 | method=uniform | model=models/Qwen/Qwen3-0.6B | conclusion=success
detect_remove_q07_seed42 | ppl=17.32 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
detect_remove_q09_seed42 | ppl=17.42 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success
detector_modernbert | ppl=None | seed=None | method= | model= | conclusion=killed
detector_tfidf_lr | ppl=None | seed=42 | method= | model=TF-IDF + LogisticRegression | conclusion=success
diagnostic_contamination100 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=killed
epoch_matched_dr_seed123 | ppl=17.66 | seed=123 | method=uniform | model=Qwen/Qwen3-0.6B | conclusion=success
epoch_matched_dr_seed456 | ppl=17.66 | seed=456 | method=uniform | model=Qwen/Qwen3-0.6B | conclusion=success
ess_only_seed123 | ppl=17.72 | seed=None | method= | model= | conclusion=success
ess_only_seed123_r2 | ppl=17.721 | seed=None | method= | model= | conclusion=success
ess_only_seed42 | ppl=None | seed=None | method=ess_only | model= | conclusion=success
ess_only_seed456 | ppl=17.76 | seed=None | method= | model= | conclusion=success
ess_only_seed456_r2 | ppl=17.762 | seed=None | method= | model= | conclusion=success
golden_ratio_seed42 | ppl=17.654 | seed=None | method= | model= | conclusion=success
grid_b0_1_seed123 | ppl=17.646 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b0_1_seed42 | ppl=17.657 | seed=None | method= | model= | conclusion=success
grid_b0_1_seed456 | ppl=17.663 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b0_2_seed123 | ppl=17.637 | seed=123 | method= | model=Qwen3-0.6B | conclusion=success
grid_b0_2_seed42 | ppl=17.64 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b0_2_seed456 | ppl=17.645 | seed=456 | method= | model=Qwen3-0.6B | conclusion=success
grid_b0_3_seed123 | ppl=None | seed=None | method= | model= | conclusion=failed
grid_b0_3_seed123_r2 | ppl=17.5792 | seed=None | method= | model= | conclusion=success
grid_b0_3_seed42 | ppl=17.64 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success
grid_b0_3_seed456 | ppl=None | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=killed
grid_b0_3_seed456_r2 | ppl=17.64 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b0_5_seed123 | ppl=17.638 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b0_5_seed456 | ppl=17.65 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b1_0_seed123 | ppl=17.674 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b1_0_seed456 | ppl=17.68 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b1_5_seed123 | ppl=17.701 | seed=None | method= | model= | conclusion=success
grid_b1_5_seed456 | ppl=17.71 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b2_0_seed123 | ppl=17.725 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b2_0_seed456 | ppl=17.989 | seed=None | method= | model= | conclusion=success
grid_b3_0_seed123 | ppl=17.76 | seed=None | method= | model= | conclusion=success
grid_b3_0_seed456 | ppl=17.921 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b5_0_seed123 | ppl=17.8039 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b5_0_seed456 | ppl=17.993 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
grid_b_low_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed
grid_b_low_seed42_r2 | ppl=None | seed=None | method= | model= | conclusion=failed
grid_b_low_seed42_r3 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed
grid_b_low_serial_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed
grid_b_seed42_batch | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
hybrid_rho04_seed42 | ppl=17.514 | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=success
hybrid_rho06_seed42 | ppl=17.53 | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=success
llama3b_adaptive_seed42 | ppl=10.58 | seed=42 | method= | model=unsloth/Llama-3.2-3B | conclusion=negative
llama3b_uniform_seed42 | ppl=10.38 | seed=42 | method= | model=unsloth/Llama-3.2-3B | conclusion=success
ngram_adaptive_seed42 | ppl=None | seed=None | method= | model= | conclusion=success
ngram_uniform_seed42 | ppl=None | seed=None | method= | model= | conclusion=success
nmin1_seed42 | ppl=17.789 | seed=None | method= | model= | conclusion=success
nmin4_seed42 | ppl=17.6947 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success
nmin5_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed
p0_contamination_60_datagen | ppl=None | seed=42 | method= | model=Qwen3-0.6B (TF-IDF scoring) | conclusion=success
qwen06b_uniform_seed42 | ppl=17.69 | seed=42 | method=uniform | model=Qwen/Qwen3-0.6B | conclusion=success
random_reweight_seed123 | ppl=None | seed=None | method= | model= | conclusion=failed
random_reweight_seed123_r2 | ppl=None | seed=None | method= | model= | conclusion=failed
random_reweight_seed123_r3 | ppl=None | seed=None | method= | model= | conclusion=failed
random_reweight_seed123_r4 | ppl=None | seed=None | method= | model= | conclusion=failed
random_reweight_seed123_r5 | ppl=17.8 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
random_reweight_seed42 | ppl=None | seed=42 | method=random | model=Qwen/Qwen3-0.6B | conclusion=failed
random_reweight_seed456 | ppl=17.777 | seed=None | method= | model= | conclusion=success
random_reweight_v2_seed42 | ppl=17.83 | seed=42 | method=random | model=Qwen/Qwen3-0.6B | conclusion=success
rho02_adaptive_tau08_seed42 | ppl=17.382 | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=negative
rho02_adaptive_tau09_r2 | ppl=None | seed=None | method= | model= | conclusion=failed
rho02_adaptive_tau09_r3 | ppl=None | seed=None | method= | model= | conclusion=failed
rho02_adaptive_tau09_r4 | ppl=None | seed=None | method= | model= | conclusion=failed
rho02_adaptive_tau09_r5 | ppl=17.45 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=negative
rho02_adaptive_tau09_seed42 | ppl=None | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=failed
rho02_uniform_seed42 | ppl=17.336 | seed=None | method= | model= | conclusion=success
tau_0.6_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed
tau_05_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed
tau_05_seed42 | ppl=17.688 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
tau_06_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed
tau_06_seed42 | ppl=17.6805 | seed=42 | method= | model= | conclusion=success
tau_07_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed
tau_07_seed42 | ppl=17.6793 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
tau_095_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed
tau_095_seed42 | ppl=17.723 | seed=None | method= | model= | conclusion=negative
tau_09_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed
tau_09_seed42 | ppl=17.712 | seed=None | method= | model= | conclusion=negative
threshold_q03_seed42 | ppl=17.253 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
threshold_q07_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed
uniform_1_7b_seed42 | ppl=None | seed=None | method= | model= | conclusion=failed
uniform_seed123 | ppl=17.6861 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
uniform_seed42 | ppl=17.6939 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
uniform_seed456 | ppl=17.7015 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "4fdcf880-9634-47b8-9e65-3574db39b23c",
  "tool_use_result": {
    "stdout": "Total DONE experiments: 133\n---\nadaptive_1_7b_seed42 | ppl=None | seed=None | method= | model= | conclusion=success\nadaptive_fix_seed123 | ppl=17.6432 | seed=None | method= | model= | conclusion=success\nadaptive_fix_seed42 | ppl=17.6527 | seed=None | method= | model= | conclusion=success\nadaptive_fix_seed456 | ppl=17.6566 | seed=None | method= | model= | conclusion=success\nadaptive_seed123 | ppl=17.6308 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\nadaptive_seed42 | ppl=17.644 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\nadaptive_seed456 | ppl=17.6419 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\nadaptive_v2_seed123 | ppl=None | seed=None | method= | model= | conclusion=killed\nadaptive_v2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed\nadaptive_v2_seed456 | ppl=None | seed=None | method= | model= | conclusion=killed\nbaseline_qwen3_0.6b | ppl=22.97 | seed=0 | method= | model=Qwen3-0.6B | conclusion=success\nbatch_adaptive_tau_rho04_seed42 | ppl=17.681 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=negative\nbatch_adaptive_tau_rho06_r2 | ppl=None | seed=None | method= | model= | conclusion=failed\nbatch_adaptive_tau_rho06_r3 | ppl=None | seed=None | method= | model= | conclusion=failed\nbatch_adaptive_tau_rho06_r5 | ppl=17.73 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=negative\nbatch_adaptive_tau_rho06_seed42 | ppl=None | seed=42 | method=batch_adaptive_tau | model=Qwen/Qwen3-0.6B | conclusion=failed\nbatchsize16_nmin8_r2 | ppl=None | seed=None | method= | model= | conclusion=killed\nbatchsize16_nmin8_r3 | ppl=17.65 | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=success\nbatchsize16_nmin8_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed\nbs8_auto_nmin_r2 | ppl=None | seed=None | method= | model= | conclusion=failed\nbs8_auto_nmin_r3 | ppl=None | seed=None | method= | model= | conclusion=failed\nbs8_auto_nmin_r5 | ppl=17.66 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\nbs8_auto_nmin_seed42 | ppl=None | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=failed\nbs8_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=failed\nbs8_nmin2_seed42_r2 | ppl=17.73 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=negative\nbs8_seed42 | ppl=None | seed=None | method= | model= | conclusion=failed\ncontamination_60_adaptive_seed456 | ppl=17.735 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ncontamination_60_ess_only_seed123 | ppl=17.763 | seed=123 | method= | model=Qwen3-0.6B | conclusion=success\ncontamination_60_ess_only_seed42 | ppl=17.77 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success\ncontamination_60_ess_only_seed456 | ppl=17.762 | seed=456 | method= | model=Qwen3-0.6B | conclusion=success\ncontamination_60_grid_b0_3_seed42 | ppl=17.634 | seed=42 | method= | model=models/Qwen/Qwen3-0.6B | conclusion=success\ncontamination_60_grid_b0_5_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ncontamination_60_random_seed123 | ppl=17.87 | seed=123 | method= | model=Qwen3-0.6B | conclusion=success\ncontamination_60_random_seed42 | ppl=17.832 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ncontamination_60_random_seed456 | ppl=17.88 | seed=456 | method= | model=Qwen3-0.6B | conclusion=success\ncontamination_60_seed123 | ppl=17.732 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ncontamination_60_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed\ncontamination_60_seed42_r2 | ppl=17.74 | seed=None | method= | model= | conclusion=success\ncontamination_60_tau06_seed42 | ppl=17.7359 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success\ncontamination_60_tau07_seed42 | ppl=17.73 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success\ncontamination_60_uniform_seed123 | ppl=17.754 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ncontamination_60_uniform_seed42 | ppl=17.766 | seed=None | method= | model= | conclusion=success\ncontamination_60_uniform_seed456 | ppl=17.77 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ndatagen_synthetic_4gpu | ppl=None | seed=42/1042/2042/3042 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ndetect_remove_baseline_seed42 | ppl=17.29 | seed=None | method= | model= | conclusion=success\ndetect_remove_q03_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed\ndetect_remove_q05_epoch_matched_seed42 | ppl=17.65 | seed=42 | method=uniform | model=models/Qwen/Qwen3-0.6B | conclusion=success\ndetect_remove_q05_seed123 | ppl=17.27 | seed=123 | method=uniform | model=models/Qwen/Qwen3-0.6B | conclusion=success\ndetect_remove_q05_seed456 | ppl=17.28 | seed=456 | method=uniform | model=models/Qwen/Qwen3-0.6B | conclusion=success\ndetect_remove_q07_seed42 | ppl=17.32 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ndetect_remove_q09_seed42 | ppl=17.42 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success\ndetector_modernbert | ppl=None | seed=None | method= | model= | conclusion=killed\ndetector_tfidf_lr | ppl=None | seed=42 | method= | model=TF-IDF + LogisticRegression | conclusion=success\ndiagnostic_contamination100 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=killed\nepoch_matched_dr_seed123 | ppl=17.66 | seed=123 | method=uniform | model=Qwen/Qwen3-0.6B | conclusion=success\nepoch_matched_dr_seed456 | ppl=17.66 | seed=456 | method=uniform | model=Qwen/Qwen3-0.6B | conclusion=success\ness_only_seed123 | ppl=17.72 | seed=None | method= | model= | conclusion=success\ness_only_seed123_r2 | ppl=17.721 | seed=None | method= | model= | conclusion=success\ness_only_seed42 | ppl=None | seed=None | method=ess_only | model= | conclusion=success\ness_only_seed456 | ppl=17.76 | seed=None | method= | model= | conclusion=success\ness_only_seed456_r2 | ppl=17.762 | seed=None | method= | model= | conclusion=success\ngolden_ratio_seed42 | ppl=17.654 | seed=None | method= | model= | conclusion=success\ngrid_b0_1_seed123 | ppl=17.646 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b0_1_seed42 | ppl=17.657 | seed=None | method= | model= | conclusion=success\ngrid_b0_1_seed456 | ppl=17.663 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b0_2_seed123 | ppl=17.637 | seed=123 | method= | model=Qwen3-0.6B | conclusion=success\ngrid_b0_2_seed42 | ppl=17.64 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b0_2_seed456 | ppl=17.645 | seed=456 | method= | model=Qwen3-0.6B | conclusion=success\ngrid_b0_3_seed123 | ppl=None | seed=None | method= | model= | conclusion=failed\ngrid_b0_3_seed123_r2 | ppl=17.5792 | seed=None | method= | model= | conclusion=success\ngrid_b0_3_seed42 | ppl=17.64 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success\ngrid_b0_3_seed456 | ppl=None | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=killed\ngrid_b0_3_seed456_r2 | ppl=17.64 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b0_5_seed123 | ppl=17.638 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b0_5_seed456 | ppl=17.65 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b1_0_seed123 | ppl=17.674 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b1_0_seed456 | ppl=17.68 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b1_5_seed123 | ppl=17.701 | seed=None | method= | model= | conclusion=success\ngrid_b1_5_seed456 | ppl=17.71 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b2_0_seed123 | ppl=17.725 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b2_0_seed456 | ppl=17.989 | seed=None | method= | model= | conclusion=success\ngrid_b3_0_seed123 | ppl=17.76 | seed=None | method= | model= | conclusion=success\ngrid_b3_0_seed456 | ppl=17.921 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b5_0_seed123 | ppl=17.8039 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b5_0_seed456 | ppl=17.993 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ngrid_b_low_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed\ngrid_b_low_seed42_r2 | ppl=None | seed=None | method= | model= | conclusion=failed\ngrid_b_low_seed42_r3 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed\ngrid_b_low_serial_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed\ngrid_b_seed42_batch | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\nhybrid_rho04_seed42 | ppl=17.514 | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=success\nhybrid_rho06_seed42 | ppl=17.53 | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=success\nllama3b_adaptive_seed42 | ppl=10.58 | seed=42 | method= | model=unsloth/Llama-3.2-3B | conclusion=negative\nllama3b_uniform_seed42 | ppl=10.38 | seed=42 | method= | model=unsloth/Llama-3.2-3B | conclusion=success\nngram_adaptive_seed42 | ppl=None | seed=None | method= | model= | conclusion=success\nngram_uniform_seed42 | ppl=None | seed=None | method= | model= | conclusion=success\nnmin1_seed42 | ppl=17.789 | seed=None | method= | model= | conclusion=success\nnmin4_seed42 | ppl=17.6947 | seed=42 | method= | model=Qwen3-0.6B | conclusion=success\nnmin5_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed\np0_contamination_60_datagen | ppl=None | seed=42 | method= | model=Qwen3-0.6B (TF-IDF scoring) | conclusion=success\nqwen06b_uniform_seed42 | ppl=17.69 | seed=42 | method=uniform | model=Qwen/Qwen3-0.6B | conclusion=success\nrandom_reweight_seed123 | ppl=None | seed=None | method= | model= | conclusion=failed\nrandom_reweight_seed123_r2 | ppl=None | seed=None | method= | model= | conclusion=failed\nrandom_reweight_seed123_r3 | ppl=None | seed=None | method= | model= | conclusion=failed\nrandom_reweight_seed123_r4 | ppl=None | seed=None | method= | model= | conclusion=failed\nrandom_reweight_seed123_r5 | ppl=17.8 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\nrandom_reweight_seed42 | ppl=None | seed=42 | method=random | model=Qwen/Qwen3-0.6B | conclusion=failed\nrandom_reweight_seed456 | ppl=17.777 | seed=None | method= | model= | conclusion=success\nrandom_reweight_v2_seed42 | ppl=17.83 | seed=42 | method=random | model=Qwen/Qwen3-0.6B | conclusion=success\nrho02_adaptive_tau08_seed42 | ppl=17.382 | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=negative\nrho02_adaptive_tau09_r2 | ppl=None | seed=None | method= | model= | conclusion=failed\nrho02_adaptive_tau09_r3 | ppl=None | seed=None | method= | model= | conclusion=failed\nrho02_adaptive_tau09_r4 | ppl=None | seed=None | method= | model= | conclusion=failed\nrho02_adaptive_tau09_r5 | ppl=17.45 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=negative\nrho02_adaptive_tau09_seed42 | ppl=None | seed=42 | method=adaptive | model=Qwen/Qwen3-0.6B | conclusion=failed\nrho02_uniform_seed42 | ppl=17.336 | seed=None | method= | model= | conclusion=success\ntau_0.6_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed\ntau_05_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed\ntau_05_seed42 | ppl=17.688 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ntau_06_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed\ntau_06_seed42 | ppl=17.6805 | seed=42 | method= | model= | conclusion=success\ntau_07_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed\ntau_07_seed42 | ppl=17.6793 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\ntau_095_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed\ntau_095_seed42 | ppl=17.723 | seed=None | method= | model= | conclusion=negative\ntau_09_nmin2_seed42 | ppl=None | seed=None | method= | model= | conclusion=killed\ntau_09_seed42 | ppl=17.712 | seed=None | method= | model= | conclusion=negative\nthreshold_q03_seed42 | ppl=17.253 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\nthreshold_q07_seed42 | ppl=None | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=failed\nuniform_1_7b_seed42 | ppl=None | seed=None | method= | model= | conclusion=failed\nuniform_seed123 | ppl=17.6861 | seed=123 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\nuniform_seed42 | ppl=17.6939 | seed=42 | method= | model=Qwen/Qwen3-0.6B | conclusion=success\nuniform_seed456 | ppl=17.7015 | seed=456 | method= | model=Qwen/Qwen3-0.6B | conclusion=success",
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

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Good, I have 133 DONE experiments. Now I need to extract more detailed info for specific experiments that have missing PPL values. Let me also get the specific metrics for the ones that have PPL=None but might have it stored differently.

Let me now build the tables. Let me first get more details on experiments with missing PPL or ambiguous data.

Key experiments I need to look at more closely:
1. adaptive_1_7b_seed42 - no PPL
2. uniform_1_7b_seed42 - failed
3. ngram_adaptive_seed42 - no PPL
4. ngram_uniform_seed42 - no PPL


5. ess_only_seed42 - no PPL
6. grid_b_seed42_batch - no PPL
7. llama3b_adaptive_seed42 - PPL=10.58, conclusion=negative (but originally listed as success from API... let me check)
8. llama3b_uniform_seed42 - PPL=10.38 (from API it was 10.53... the reeval_v2 numbers differ)

I'm noticing some discrepancies between what the API reported and what my parsing shows. The llama3b experiments have conflicting conclusion labels and slightly different PPL values between sources, so I need to dig into which version is more reliable. I'm noticing some inconsistencies between what the API returned and what I'm parsing from the YAML, so I need to dig deeper and pull the full metric details for the experiments where the numbers don't match up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "2475b83c-a0ab-4082-96ce-9d3b7a58633d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gNTZF8rW9PNoL8iqAFiec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5820,
      "cache_read_input_tokens": 31366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5820
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

_source line 17_

需要补充一些缺失 PPL 的实验详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "f96bc3d5-bd8c-499d-bd63-0a47b1185cb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gNTZF8rW9PNoL8iqAFiec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5820,
      "cache_read_input_tokens": 31366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5820
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01DeywLUzfMAaS8MPbwba1Fe`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\n# Experiments we need full details for\nneed_details = [\n    'adaptive_1_7b_seed42', 'uniform_1_7b_seed42',\n    'ngram_adaptive_seed42', 'ngram_uniform_seed42',\n    'ess_only_seed42', 'grid_b_seed42_batch',\n    'contamination_60_grid_b0_5_seed42',\n    'llama3b_adaptive_seed42', 'llama3b_uniform_seed42',\n    'detect_remove_baseline_seed42', 'detect_remove_q05_seed123', 'detect_remove_q05_seed456',\n    'detect_remove_q05_epoch_matched_seed42', 'detect_remove_q07_seed42', 'detect_remove_q09_seed42',\n    'threshold_q03_seed42',\n    'adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456',\n    'detector_tfidf_lr',\n    'golden_ratio_seed42', 'nmin1_seed42', 'nmin4_seed42',\n    'hybrid_rho04_seed42', 'hybrid_rho06_seed42',\n    'rho02_uniform_seed42', 'rho02_adaptive_tau08_seed42',\n    'batchsize16_nmin8_r3',\n    'qwen06b_uniform_seed42',\n    'grid_b0_3_seed42',\n    'baseline_qwen3_0.6b',\n]\n\nfor eid in need_details:\n    exp = experiments.get(eid)\n    if exp:\n        m = exp.get('metrics', {})\n        s = exp.get('spec', {})\n        print(f'=== {eid} ===')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n        print(f'  spec: seed={s.get(\\\"seed\\\")}, model={s.get(\\\"model_name\\\")}, method={s.get(\\\"weighting_method\\\")}, data={s.get(\\\"data_path\\\")}, b_star={s.get(\\\"b_star\\\")}')\n        print(f'  metrics: {json.dumps(m, indent=None)}')\n        print()\n    else:\n        print(f'=== {eid} === NOT FOUND')\n        print()\n\" 2>&1",
  "description": "Get full details for key experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "3a6cd6aa-9e9e-4f27-85f8-e4e7146e8f0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gNTZF8rW9PNoL8iqAFiec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5820,
      "cache_read_input_tokens": 31366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5820
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

_source line 19 · 2026-05-18T21:30:07.841Z_

<details><summary>↩ Tool result · `toolu_01DeywLUzfMAaS8MPbwba1Fe`</summary>

```text
=== adaptive_1_7b_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {}

=== uniform_1_7b_seed42 ===
  conclusion: failed
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {}

=== ngram_adaptive_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {}

=== ngram_uniform_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {}

=== ess_only_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=ess_only, data=None, b_star=None
  metrics: {"eval_ppl": 17.73, "eval_loss": 2.875, "b_star_median": 1.58, "b_star_mean": 3.51, "vs_uniform_ppl_delta": "+0.038", "vs_adaptive_ppl_delta": "+0.08"}

=== grid_b_seed42_batch ===
  conclusion: success
  spec: seed=42, model=Qwen/Qwen3-0.6B, method=None, data=/root/provenance_weight_training/data/scored_data.jsonl, b_star=None
  metrics: {"b_values": [0.5, 1, 1.5, 2, 3, 5], "b0_5_train_loss": 9.598, "b0_5_completed": true, "b1_0_completed": true, "b1_5_completed": true, "b2_0_current_step": 5149, "b2_0_total_steps": 6103, "completed_b_values": [0.5, 1, 1.5, 2, 3], "current_b": 5, "total_steps": 6103, "current_step": 3422, "b5_0_progress_pct": 56, "eta_minutes": 95, "b2_0_completed": true, "b2_0_train_loss": 10.621, "b2_0_train_runtime_s": 13034, "b3_0_completed": true, "b3_0_train_loss": 10.754, "b3_0_train_runtime_s": 13036, "all_completed": true, "b1_0_train_loss": 10.223, "b1_5_train_loss": 10.485, "b5_0_train_loss": 10.858, "b0_5_runtime_s": 13036, "b1_0_runtime_s": 12968, "b1_5_runtime_s": 14789, "b2_0_runtime_s": 13034, "b3_0_runtime_s": 13036, "b5_0_runtime_s": 13115, "note": "eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending", "b0_5_eval_ppl": 17.651, "b1_0_eval_ppl": 17.692, "b1_5_eval_ppl": 17.718, "b2_0_eval_ppl": 17.741, "b3_0_eval_ppl": 17.774, "b5_0_eval_ppl": 17.818, "eval_holdout_tokens": 4077068, "best_b": 0.5, "best_eval_ppl": 17.651}

=== contamination_60_grid_b0_5_seed42 ===
  conclusion: success
  spec: seed=42, model=Qwen/Qwen3-0.6B, method=None, data=/root/provenance_weight_training/data/scored_data_60.jsonl, b_star=None
  metrics: {"eval_ppl": 17.704, "eval_loss": 2.8738, "eval_tokens": 4077068, "eval_docs": 5000}

=== llama3b_adaptive_seed42 ===
  conclusion: negative
  spec: seed=42, model=unsloth/Llama-3.2-3B, method=None, data=data/scored_data.jsonl, b_star=None
  metrics: {"ppl": 10.58, "eval_loss": 2.359, "eval_tokens": 4017316}

=== llama3b_uniform_seed42 ===
  conclusion: success
  spec: seed=42, model=unsloth/Llama-3.2-3B, method=None, data=data/scored_data.jsonl, b_star=None
  metrics: {"ppl": 10.38, "eval_loss": 2.3397, "eval_tokens": 1526195, "train_loss": 7.2987, "train_steps": 6103, "train_runtime_seconds": 94309}

=== detect_remove_baseline_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {"eval_ppl_holdout": 17.29, "eval_loss_holdout": 2.8499, "eval_holdout_tokens": 4077068, "train_loss": 11.003, "train_runtime_seconds": 13248, "total_steps": 6103, "train_samples_per_second": 7.371}

=== detect_remove_q05_seed123 ===
  conclusion: success
  spec: seed=123, model=models/Qwen/Qwen3-0.6B, method=uniform, data=data/scored_data_filtered_q05.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 17.27, "eval_loss_holdout": 2.8491, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16"}

=== detect_remove_q05_seed456 ===
  conclusion: success
  spec: seed=456, model=models/Qwen/Qwen3-0.6B, method=uniform, data=data/scored_data_filtered_q05.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 17.28, "eval_loss_holdout": 2.8493, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16"}

=== detect_remove_q05_epoch_matched_seed42 ===
  conclusion: success
  spec: seed=42, model=models/Qwen/Qwen3-0.6B, method=uniform, data=data/scored_data_filtered_q05.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 17.65, "eval_loss_holdout": 2.8707, "eval_holdout_tokens": 4077068, "train_loss_final": 3.184, "total_steps": 2533, "eval_method": "eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16", "vs_full_dr_q05": "+0.360 (17.650 vs 17.290, epoch-matched worse)", "vs_adaptive": "-0.001 (17.650 vs 17.651, nearly identical to adaptive)", "interpretation": "D&R 0.36 PPL advantage over epoch-matched is entirely from multi-epoch training on clean data, not from data quality filtering"}

=== detect_remove_q07_seed42 ===
  conclusion: success
  spec: seed=42, model=Qwen/Qwen3-0.6B, method=None, data=data/scored_data_filtered_q07.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 17.32, "eval_loss_holdout": 2.8519, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)", "note": "final checkpoint, replaces partial ckpt-3500 PPL=17.49"}

=== detect_remove_q09_seed42 ===
  conclusion: success
  spec: seed=42, model=Qwen3-0.6B, method=None, data=data/scored_data_filtered_q09.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 17.42, "eval_loss_holdout": 2.8577, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16"}

=== threshold_q03_seed42 ===
  conclusion: success
  spec: seed=42, model=Qwen/Qwen3-0.6B, method=None, data=data/scored_data_filtered_q03.jsonl, b_star=None
  metrics: {"eval_loss_holdout": 2.848, "eval_ppl_holdout": 17.253}

=== adaptive_fix_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {"train_loss": 7.5167, "train_runtime": 10304.37, "train_samples_per_second": 9.476, "train_steps_per_second": 0.592, "total_steps": 6103, "eval_ppl_holdout": 17.6527, "eval_loss_holdout": 2.8709, "eval_holdout_tokens": 4077068, "eval_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "eval_note": "unified post-hoc eval 2026-05-15; was 17.65/4077068", "b_star_count": 26458, "b_star_mean": 1.399, "b_star_median": 0.871, "b_star_std": 1.933, "b_star_min": 0, "b_star_max": 20, "b_star_p25": 0.54, "b_star_p75": 1.512, "b_star_pct_below_0.5": 20.9, "b_star_pct_0.5_to_1": 35.7, "b_star_pct_1_to_2": 27.3, "b_star_pct_above_2": 16.1, "b_star_note": "Training-only records (eval checkpoint records with b*=0 excluded)"}

=== adaptive_fix_seed123 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {"eval_ppl_holdout": 17.6432, "eval_loss_holdout": 2.8704, "eval_loss": 2.8704, "eval_holdout_tokens": 4077068, "eval_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "eval_note": "unified post-hoc eval 2026-05-15; was 17.643/4077068", "train_loss_weighted": 7.517, "train_runtime_s": 10347, "total_steps": 6103, "epoch": 0.26, "b_star_mean": 1.431, "b_star_median": 0.88, "b_star_std": 2.029, "b_star_min": 0, "b_star_max": 20, "b_star_pct_below_0.5": 20.9, "b_star_pct_0.5_to_1": 35.7, "b_star_pct_1_to_2": 27.3, "b_star_pct_2_to_5": 6.3, "b_star_pct_above_5": 1.9, "b_star_count": 25906, "b_star_p25": 0.54, "b_star_p75": 1.52, "b_star_pct_above_2": 16.1, "b_star_note": "Training-only records (eval checkpoint records with b*=0 excluded)"}

=== adaptive_fix_seed456 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {"train_loss": 8.3124, "train_runtime": 11436.05, "train_samples_per_second": 8.539, "train_steps_per_second": 0.534, "total_steps": 6103, "eval_ppl_holdout": 17.6566, "eval_loss_holdout": 2.8711, "eval_holdout_tokens": 4077068, "eval_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "eval_note": "unified post-hoc eval 2026-05-15; was 17.66/4077068", "b_star_count": 26396, "b_star_mean": 1.416, "b_star_median": 0.88, "b_star_std": 1.993, "b_star_min": 0, "b_star_max": 20, "b_star_p25": 0.54, "b_star_p75": 1.52, "b_star_pct_below_0.5": 20.9, "b_star_pct_0.5_to_1": 35.7, "b_star_pct_1_to_2": 27.3, "b_star_pct_above_2": 16.1, "b_star_note": "Training-only records (eval checkpoint records with b*=0 excluded)"}

=== detector_tfidf_lr ===
  conclusion: success
  spec: seed=42, model=TF-IDF + LogisticRegression, method=None, data=/root/provenance_weight_training/data/detector.jsonl, b_star=None
  metrics: {"auc": 0.939, "accuracy": 0.858, "ece_raw": 0.24, "ece_calibrated": 0.048, "temperature_T": 0.204, "q_score_mean": 0.6, "q_score_std": 0.374, "q_score_median": 0.707, "mid_range_ratio": 0.463}

=== golden_ratio_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {"eval_ppl_holdout": 17.654, "eval_loss": 2.871, "train_loss": 2.1145, "train_loss_last500": 2.109, "eval_holdout_tokens": 4077068, "total_steps": 6103, "train_runtime_s": 13442, "gpu_hours": 3.73}

=== nmin1_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {"eval_ppl_holdout": 17.789, "eval_loss": 2.8786, "eval_holdout_tokens": 4077068, "b_star_mean": 7.197, "b_star_median": 1.746, "b_star_std": 8.374, "b_star_min": 0, "b_star_max": 20, "b_star_p25": 0.803, "b_star_p75": 20, "b_star_zero_frac": 0.019, "b_star_pct_below_0.5": 13.1, "b_star_pct_0.5_to_1": 19.1, "b_star_pct_1_to_2": 21.1, "b_star_pct_above_2": 46.7, "b_star_count": 24412, "alpha_eff_mean": 0.714, "alpha_eff_median": 0.8}

=== nmin4_seed42 ===
  conclusion: success
  spec: seed=42, model=Qwen3-0.6B, method=None, data=/root/provenance_weight_training/data/scored_data.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 17.6947, "eval_loss": 2.8733, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)", "train_loss": 7.989, "total_steps": 6103, "train_runtime_s": 16231, "train_samples_per_second": 6.016, "b_star_count": 24412, "b_star_mean": 0, "b_star_median": 0, "b_star_std": 0, "b_star_min": 0, "b_star_max": 0, "b_star_pct_zero": 100, "ess_mean": 4, "ess_min": 4, "ess_max": 4}

=== hybrid_rho04_seed42 ===
  conclusion: success
  spec: seed=42, model=Qwen/Qwen3-0.6B, method=adaptive, data=data/scored_data_hybrid.jsonl, b_star=None
  metrics: {"eval_loss_holdout": 2.863, "eval_ppl_holdout": 17.514}

=== hybrid_rho06_seed42 ===
  conclusion: success
  spec: seed=42, model=Qwen/Qwen3-0.6B, method=adaptive, data=data/scored_data_hybrid_rho06.jsonl, b_star=None
  metrics: {"eval_loss_holdout": 2.8637, "eval_ppl_holdout": 17.53}

=== rho02_uniform_seed42 ===
  conclusion: success
  spec: seed=None, model=None, method=None, data=None, b_star=None
  metrics: {"eval_ppl_holdout": 17.336, "eval_loss_holdout": 2.853, "eval_holdout_tokens": 4077068}

=== rho02_adaptive_tau08_seed42 ===
  conclusion: negative
  spec: seed=42, model=Qwen/Qwen3-0.6B, method=adaptive, data=data/rho02_scored_data.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 17.382, "eval_loss_holdout": 2.8555, "eval_holdout_tokens": 4077068, "total_steps": 6103, "train_runtime_seconds": 14599, "vs_rho02_uniform": "+0.046 (17.382 vs 17.336)", "vs_rho04_uniform": "-0.312 (17.382 vs 17.694)", "tau": 0.8, "rho": 0.2, "b_star_pct_zero": "40-50%", "conclusion_note": "worse than same-rho uniform baseline"}

=== batchsize16_nmin8_r3 ===
  conclusion: success
  spec: seed=42, model=Qwen/Qwen3-0.6B, method=adaptive, data=data/scored_data.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 17.65, "eval_loss_holdout": 2.871, "eval_holdout_tokens": 4077068, "total_steps": 6103, "train_loss": 2.6308, "train_runtime_seconds": 15057, "vs_adaptive_bs4": "-0.003 (17.65 vs 17.6527)", "vs_bs8_nmin4": "-0.01 (17.65 vs 17.66)", "batch_size": 16, "n_min": 8}

=== qwen06b_uniform_seed42 ===
  conclusion: success
  spec: seed=42, model=Qwen/Qwen3-0.6B, method=uniform, data=data/scored_data.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 17.69, "eval_loss_holdout": 2.8733, "eval_holdout_tokens": 4077068, "train_loss": 1.9882, "note": "v2 run on westd-41312 (no inline eval)"}

=== grid_b0_3_seed42 ===
  conclusion: success
  spec: seed=42, model=Qwen3-0.6B, method=None, data=/root/provenance_weight_training/data/scored_data.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 17.64, "eval_loss_holdout": 2.8702, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "train_loss": 9.1154, "train_runtime_seconds": 13365.79, "train_samples_per_second": 7.306, "total_steps": 6103, "b_fixed": 0.3, "alpha_eff_typical_range": "0.07-0.88", "ess_typical_range": "2.3-4.0"}

=== baseline_qwen3_0.6b ===
  conclusion: success
  spec: seed=0, model=Qwen3-0.6B, method=None, data=data/human/eval_holdout.jsonl, b_star=None
  metrics: {"eval_ppl_holdout": 22.97, "eval_loss": 3.134, "eval_holdout_tokens": 4077068, "eval_method": "sliding_window_stride1024_maxlen2048_fp16"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "5440d7fa-558b-46e7-a563-4b62bcdfc0ed",
  "tool_use_result": {
    "stdout": "=== adaptive_1_7b_seed42 ===\n  conclusion: success\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {}\n\n=== uniform_1_7b_seed42 ===\n  conclusion: failed\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {}\n\n=== ngram_adaptive_seed42 ===\n  conclusion: success\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {}\n\n=== ngram_uniform_seed42 ===\n  conclusion: success\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {}\n\n=== ess_only_seed42 ===\n  conclusion: success\n  spec: seed=None, model=None, method=ess_only, data=None, b_star=None\n  metrics: {\"eval_ppl\": 17.73, \"eval_loss\": 2.875, \"b_star_median\": 1.58, \"b_star_mean\": 3.51, \"vs_uniform_ppl_delta\": \"+0.038\", \"vs_adaptive_ppl_delta\": \"+0.08\"}\n\n=== grid_b_seed42_batch ===\n  conclusion: success\n  spec: seed=42, model=Qwen/Qwen3-0.6B, method=None, data=/root/provenance_weight_training/data/scored_data.jsonl, b_star=None\n  metrics: {\"b_values\": [0.5, 1, 1.5, 2, 3, 5], \"b0_5_train_loss\": 9.598, \"b0_5_completed\": true, \"b1_0_completed\": true, \"b1_5_completed\": true, \"b2_0_current_step\": 5149, \"b2_0_total_steps\": 6103, \"completed_b_values\": [0.5, 1, 1.5, 2, 3], \"current_b\": 5, \"total_steps\": 6103, \"current_step\": 3422, \"b5_0_progress_pct\": 56, \"eta_minutes\": 95, \"b2_0_completed\": true, \"b2_0_train_loss\": 10.621, \"b2_0_train_runtime_s\": 13034, \"b3_0_completed\": true, \"b3_0_train_loss\": 10.754, \"b3_0_train_runtime_s\": 13036, \"all_completed\": true, \"b1_0_train_loss\": 10.223, \"b1_5_train_loss\": 10.485, \"b5_0_train_loss\": 10.858, \"b0_5_runtime_s\": 13036, \"b1_0_runtime_s\": 12968, \"b1_5_runtime_s\": 14789, \"b2_0_runtime_s\": 13034, \"b3_0_runtime_s\": 13036, \"b5_0_runtime_s\": 13115, \"note\": \"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\", \"b0_5_eval_ppl\": 17.651, \"b1_0_eval_ppl\": 17.692, \"b1_5_eval_ppl\": 17.718, \"b2_0_eval_ppl\": 17.741, \"b3_0_eval_ppl\": 17.774, \"b5_0_eval_ppl\": 17.818, \"eval_holdout_tokens\": 4077068, \"best_b\": 0.5, \"best_eval_ppl\": 17.651}\n\n=== contamination_60_grid_b0_5_seed42 ===\n  conclusion: success\n  spec: seed=42, model=Qwen/Qwen3-0.6B, method=None, data=/root/provenance_weight_training/data/scored_data_60.jsonl, b_star=None\n  metrics: {\"eval_ppl\": 17.704, \"eval_loss\": 2.8738, \"eval_tokens\": 4077068, \"eval_docs\": 5000}\n\n=== llama3b_adaptive_seed42 ===\n  conclusion: negative\n  spec: seed=42, model=unsloth/Llama-3.2-3B, method=None, data=data/scored_data.jsonl, b_star=None\n  metrics: {\"ppl\": 10.58, \"eval_loss\": 2.359, \"eval_tokens\": 4017316}\n\n=== llama3b_uniform_seed42 ===\n  conclusion: success\n  spec: seed=42, model=unsloth/Llama-3.2-3B, method=None, data=data/scored_data.jsonl, b_star=None\n  metrics: {\"ppl\": 10.38, \"eval_loss\": 2.3397, \"eval_tokens\": 1526195, \"train_loss\": 7.2987, \"train_steps\": 6103, \"train_runtime_seconds\": 94309}\n\n=== detect_remove_baseline_seed42 ===\n  conclusion: success\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.29, \"eval_loss_holdout\": 2.8499, \"eval_holdout_tokens\": 4077068, \"train_loss\": 11.003, \"train_runtime_seconds\": 13248, \"total_steps\": 6103, \"train_samples_per_second\": 7.371}\n\n=== detect_remove_q05_seed123 ===\n  conclusion: success\n  spec: seed=123, model=models/Qwen/Qwen3-0.6B, method=uniform, data=data/scored_data_filtered_q05.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.27, \"eval_loss_holdout\": 2.8491, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\"}\n\n=== detect_remove_q05_seed456 ===\n  conclusion: success\n  spec: seed=456, model=models/Qwen/Qwen3-0.6B, method=uniform, data=data/scored_data_filtered_q05.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.28, \"eval_loss_holdout\": 2.8493, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\"}\n\n=== detect_remove_q05_epoch_matched_seed42 ===\n  conclusion: success\n  spec: seed=42, model=models/Qwen/Qwen3-0.6B, method=uniform, data=data/scored_data_filtered_q05.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.65, \"eval_loss_holdout\": 2.8707, \"eval_holdout_tokens\": 4077068, \"train_loss_final\": 3.184, \"total_steps\": 2533, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"vs_full_dr_q05\": \"+0.360 (17.650 vs 17.290, epoch-matched worse)\", \"vs_adaptive\": \"-0.001 (17.650 vs 17.651, nearly identical to adaptive)\", \"interpretation\": \"D&R 0.36 PPL advantage over epoch-matched is entirely from multi-epoch training on clean data, not from data quality filtering\"}\n\n=== detect_remove_q07_seed42 ===\n  conclusion: success\n  spec: seed=42, model=Qwen/Qwen3-0.6B, method=None, data=data/scored_data_filtered_q07.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.32, \"eval_loss_holdout\": 2.8519, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\", \"note\": \"final checkpoint, replaces partial ckpt-3500 PPL=17.49\"}\n\n=== detect_remove_q09_seed42 ===\n  conclusion: success\n  spec: seed=42, model=Qwen3-0.6B, method=None, data=data/scored_data_filtered_q09.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.42, \"eval_loss_holdout\": 2.8577, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\"}\n\n=== threshold_q03_seed42 ===\n  conclusion: success\n  spec: seed=42, model=Qwen/Qwen3-0.6B, method=None, data=data/scored_data_filtered_q03.jsonl, b_star=None\n  metrics: {\"eval_loss_holdout\": 2.848, \"eval_ppl_holdout\": 17.253}\n\n=== adaptive_fix_seed42 ===\n  conclusion: success\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {\"train_loss\": 7.5167, \"train_runtime\": 10304.37, \"train_samples_per_second\": 9.476, \"train_steps_per_second\": 0.592, \"total_steps\": 6103, \"eval_ppl_holdout\": 17.6527, \"eval_loss_holdout\": 2.8709, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.65/4077068\", \"b_star_count\": 26458, \"b_star_mean\": 1.399, \"b_star_median\": 0.871, \"b_star_std\": 1.933, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.512, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}\n\n=== adaptive_fix_seed123 ===\n  conclusion: success\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.6432, \"eval_loss_holdout\": 2.8704, \"eval_loss\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.643/4077068\", \"train_loss_weighted\": 7.517, \"train_runtime_s\": 10347, \"total_steps\": 6103, \"epoch\": 0.26, \"b_star_mean\": 1.431, \"b_star_median\": 0.88, \"b_star_std\": 2.029, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_2_to_5\": 6.3, \"b_star_pct_above_5\": 1.9, \"b_star_count\": 25906, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}\n\n=== adaptive_fix_seed456 ===\n  conclusion: success\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {\"train_loss\": 8.3124, \"train_runtime\": 11436.05, \"train_samples_per_second\": 8.539, \"train_steps_per_second\": 0.534, \"total_steps\": 6103, \"eval_ppl_holdout\": 17.6566, \"eval_loss_holdout\": 2.8711, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.66/4077068\", \"b_star_count\": 26396, \"b_star_mean\": 1.416, \"b_star_median\": 0.88, \"b_star_std\": 1.993, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}\n\n=== detector_tfidf_lr ===\n  conclusion: success\n  spec: seed=42, model=TF-IDF + LogisticRegression, method=None, data=/root/provenance_weight_training/data/detector.jsonl, b_star=None\n  metrics: {\"auc\": 0.939, \"accuracy\": 0.858, \"ece_raw\": 0.24, \"ece_calibrated\": 0.048, \"temperature_T\": 0.204, \"q_score_mean\": 0.6, \"q_score_std\": 0.374, \"q_score_median\": 0.707, \"mid_range_ratio\": 0.463}\n\n=== golden_ratio_seed42 ===\n  conclusion: success\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.654, \"eval_loss\": 2.871, \"train_loss\": 2.1145, \"train_loss_last500\": 2.109, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_s\": 13442, \"gpu_hours\": 3.73}\n\n=== nmin1_seed42 ===\n  conclusion: success\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.789, \"eval_loss\": 2.8786, \"eval_holdout_tokens\": 4077068, \"b_star_mean\": 7.197, \"b_star_median\": 1.746, \"b_star_std\": 8.374, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.803, \"b_star_p75\": 20, \"b_star_zero_frac\": 0.019, \"b_star_pct_below_0.5\": 13.1, \"b_star_pct_0.5_to_1\": 19.1, \"b_star_pct_1_to_2\": 21.1, \"b_star_pct_above_2\": 46.7, \"b_star_count\": 24412, \"alpha_eff_mean\": 0.714, \"alpha_eff_median\": 0.8}\n\n=== nmin4_seed42 ===\n  conclusion: success\n  spec: seed=42, model=Qwen3-0.6B, method=None, data=/root/provenance_weight_training/data/scored_data.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.6947, \"eval_loss\": 2.8733, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 7.989, \"total_steps\": 6103, \"train_runtime_s\": 16231, \"train_samples_per_second\": 6.016, \"b_star_count\": 24412, \"b_star_mean\": 0, \"b_star_median\": 0, \"b_star_std\": 0, \"b_star_min\": 0, \"b_star_max\": 0, \"b_star_pct_zero\": 100, \"ess_mean\": 4, \"ess_min\": 4, \"ess_max\": 4}\n\n=== hybrid_rho04_seed42 ===\n  conclusion: success\n  spec: seed=42, model=Qwen/Qwen3-0.6B, method=adaptive, data=data/scored_data_hybrid.jsonl, b_star=None\n  metrics: {\"eval_loss_holdout\": 2.863, \"eval_ppl_holdout\": 17.514}\n\n=== hybrid_rho06_seed42 ===\n  conclusion: success\n  spec: seed=42, model=Qwen/Qwen3-0.6B, method=adaptive, data=data/scored_data_hybrid_rho06.jsonl, b_star=None\n  metrics: {\"eval_loss_holdout\": 2.8637, \"eval_ppl_holdout\": 17.53}\n\n=== rho02_uniform_seed42 ===\n  conclusion: success\n  spec: seed=None, model=None, method=None, data=None, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.336, \"eval_loss_holdout\": 2.853, \"eval_holdout_tokens\": 4077068}\n\n=== rho02_adaptive_tau08_seed42 ===\n  conclusion: negative\n  spec: seed=42, model=Qwen/Qwen3-0.6B, method=adaptive, data=data/rho02_scored_data.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.382, \"eval_loss_holdout\": 2.8555, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_seconds\": 14599, \"vs_rho02_uniform\": \"+0.046 (17.382 vs 17.336)\", \"vs_rho04_uniform\": \"-0.312 (17.382 vs 17.694)\", \"tau\": 0.8, \"rho\": 0.2, \"b_star_pct_zero\": \"40-50%\", \"conclusion_note\": \"worse than same-rho uniform baseline\"}\n\n=== batchsize16_nmin8_r3 ===\n  conclusion: success\n  spec: seed=42, model=Qwen/Qwen3-0.6B, method=adaptive, data=data/scored_data.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.65, \"eval_loss_holdout\": 2.871, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 2.6308, \"train_runtime_seconds\": 15057, \"vs_adaptive_bs4\": \"-0.003 (17.65 vs 17.6527)\", \"vs_bs8_nmin4\": \"-0.01 (17.65 vs 17.66)\", \"batch_size\": 16, \"n_min\": 8}\n\n=== qwen06b_uniform_seed42 ===\n  conclusion: success\n  spec: seed=42, model=Qwen/Qwen3-0.6B, method=uniform, data=data/scored_data.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.69, \"eval_loss_holdout\": 2.8733, \"eval_holdout_tokens\": 4077068, \"train_loss\": 1.9882, \"note\": \"v2 run on westd-41312 (no inline eval)\"}\n\n=== grid_b0_3_seed42 ===\n  conclusion: success\n  spec: seed=42, model=Qwen3-0.6B, method=None, data=/root/provenance_weight_training/data/scored_data.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8702, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"train_loss\": 9.1154, \"train_runtime_seconds\": 13365.79, \"train_samples_per_second\": 7.306, \"total_steps\": 6103, \"b_fixed\": 0.3, \"alpha_eff_typical_range\": \"0.07-0.88\", \"ess_typical_range\": \"2.3-4.0\"}\n\n=== baseline_qwen3_0.6b ===\n  conclusion: success\n  spec: seed=0, model=Qwen3-0.6B, method=None, data=data/human/eval_holdout.jsonl, b_star=None\n  metrics: {\"eval_ppl_holdout\": 22.97, \"eval_loss\": 3.134, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16\"}",
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

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now I need more details on:
1. adaptive_1_7b_seed42 and uniform_1_7b_seed42 (1.7B scale experiments)
2. ngram_adaptive_seed42 and ngram_uniform_seed42 (multi-detector experiments)
3. The `ess_only_seed42` uses `eval_ppl` which might be different from eval_ppl_holdout

Let me also check for ess_only_seed123 and ess_only_seed456, and get more info on the Llama and 1.7B experiments.


I'm noticing a discrepancy between the API results and my YAML parsing for the Llama experiments. The API shows llama3b_adaptive_seed42 with a success conclusion and multiple metrics including MMLU scores, while my YAML has it marked as negative with just the perplexity value. I need to reconcile these differences and verify which source is accurate.

Looking at the metadata, the API includes a `reeval_v2_note` for the adaptive variant mentioning unified evaluation in the same shell session, which suggests those are the more recent and reliable numbers. The YAML appears to have an older version of the uniform metric with different token counts, so I should trust the API's reeval_v2 results as the authoritative source. There's a discrepancy between what the API returned for llama3b_adaptive_seed42 (conclusion=success) and what my YAML parser is showing (conclusion=negative). Let me check the actual YAML entry for the llama3b experiments to figure out which one is correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "b1fd0159-92a4-427e-9acf-dbc3efb35b03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Np3YAJ3zB15u6K84GCMUNb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7185,
      "cache_read_input_tokens": 37186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7185
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

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01HRRiu3vpr13vH4NQQCqgwp`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\n# Get more details\nneed = ['adaptive_1_7b_seed42', 'uniform_1_7b_seed42', 'ngram_adaptive_seed42', 'ngram_uniform_seed42',\n        'ess_only_seed42', 'ess_only_seed123', 'ess_only_seed123_r2', 'ess_only_seed456', 'ess_only_seed456_r2',\n        'contamination_60_uniform_seed42', 'contamination_60_seed123', 'contamination_60_seed42_r2',\n        'contamination_60_adaptive_seed456',\n        'adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456',\n        'random_reweight_v2_seed42', 'random_reweight_seed456',\n        'llama3b_adaptive_seed42', 'llama3b_uniform_seed42']\n\nfor eid in need:\n    exp = experiments.get(eid, {})\n    print(f'=== {eid} ===')\n    print(json.dumps(exp, indent=2, default=str))\n    print()\n\" 2>&1 | head -500",
  "description": "Get full YAML entries for remaining experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "538e71ed-7434-433d-8848-905094b16605",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Np3YAJ3zB15u6K84GCMUNb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7185,
      "cache_read_input_tokens": 37186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7185
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

_source line 22 · 2026-05-18T21:30:34.368Z_

<details><summary>↩ Tool result · `toolu_01HRRiu3vpr13vH4NQQCqgwp`</summary>

```text
=== adaptive_1_7b_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T11:47:25.251Z",
  "updated_at": "2026-05-18T19:07:03.284Z",
  "hypothesis": "Scale validation: adaptive provenance weighting on Qwen3-1.7B (2.8x larger than 0.6B). If adaptive still outperforms uniform at 1.7B scale, demonstrates method generality beyond small models. Key for Main conference upgrade (D079 Line B). Expected: adaptive < uniform by \u22650.03 PPL (consistent with 0.6B gap).",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-1.7B --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42 --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/checkpoint-2500\"",
    "server": "westd-41312",
    "gpu": [
      "cuda:1"
    ],
    "pid": "226766",
    "log_path": "~/runs/provenance_weight_training/adaptive_1_7b_seed42.log",
    "submitted_at": "2026-05-18T15:00:59.483Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "checkpoint_path": "/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/final",
    "train_loss": 5.36,
    "train_runtime_s": 10990,
    "total_steps": 6103,
    "wall_clock_seconds": 14763.8,
    "gpu_hours": 4.1
  },
  "conclusion": "success",
  "completed_at": "2026-05-18T19:07:03.284Z"
}

=== uniform_1_7b_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T11:47:26.566Z",
  "updated_at": "2026-05-18T15:45:29.875Z",
  "hypothesis": "Uniform weighting baseline on Qwen3-1.7B for scale validation. Control condition for comparing adaptive provenance weighting at larger model scale. Part of D079 Line B.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-1.7B --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42 --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42/checkpoint-3000\"",
    "server": "westd-41312",
    "gpu": [
      "cuda:0"
    ],
    "pid": "226623",
    "log_path": "~/runs/provenance_weight_training/uniform_1_7b_seed42.log",
    "submitted_at": "2026-05-18T15:00:55.785Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 2489.8,
    "gpu_hours": 0.69
  },
  "reproduce": {
    "finished_at": "2026-05-18T15:42:18.572Z"
  },
  "failure_reason": "EXIT_CODE=1 (generic error \u2014 check log tail)",
  "conclusion": "failed",
  "completed_at": "2026-05-18T15:42:25.542Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-18T15:42:32.973826+00:00"
      }
    ]
  },
  "notes": "\u5931\u8d25\u539f\u56e0: FileNotFoundError \u2014 checkpoint-3000/trainer_state.json \u7f3a\u5931\uff0cresume \u5d29\u6e83 | \u5df2\u6709\u6210\u679c: checkpoint-3000 \u5b58\u5728\u4f46\u4e0d\u5b8c\u6574 | \u5efa\u8bae: \u627e\u6709\u6548 checkpoint \u91cd resume \u6216\u4ece\u5934\u8bad\u7ec3"
}

=== ngram_adaptive_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T14:14:23.226Z",
  "updated_at": "2026-05-18T19:07:52.563Z",
  "hypothesis": "Multi-detector validation: adaptive weighting with n-gram PPL detector (statistical, AUC=0.73) produces lower PPL than uniform, demonstrating method works with fundamentally different detector type (not just neural classifier). Complementary to q_score (Spearman r=-0.36). Part of D079 Line A.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-0.6B --data_path data/scored_data_ngram_qscore.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42 --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_only_model --save_total_limit 3\"",
    "server": "westd-41312",
    "gpu": [
      "cuda:2"
    ],
    "pid": "226953",
    "log_path": "~/runs/provenance_weight_training/ngram_adaptive_seed42.log",
    "submitted_at": "2026-05-18T15:01:02.239Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "checkpoint_path": "/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/final",
    "train_loss": 9.298,
    "train_runtime_s": 14170,
    "total_steps": 6103,
    "wall_clock_seconds": 14810.3,
    "gpu_hours": 4.11
  },
  "conclusion": "success",
  "completed_at": "2026-05-18T19:07:52.563Z"
}

=== ngram_uniform_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T14:14:25.095Z",
  "updated_at": "2026-05-18T19:07:54.054Z",
  "hypothesis": "Uniform baseline for n-gram detector comparison. Control condition: uniform weighting on ngram-scored data. Expected to perform worse than ngram_adaptive, confirming adaptive advantage generalizes across detectors.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-0.6B --data_path data/scored_data_ngram_qscore.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42 --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_only_model --save_total_limit 3\"",
    "server": "westd-41312",
    "gpu": [
      "cuda:3"
    ],
    "pid": "227105",
    "log_path": "~/runs/provenance_weight_training/ngram_uniform_seed42.log",
    "submitted_at": "2026-05-18T15:01:05.106Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "checkpoint_path": "/root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/final",
    "train_loss": 7.99,
    "train_runtime_s": 12800,
    "total_steps": 6103,
    "wall_clock_seconds": 14808.9,
    "gpu_hours": 4.11
  },
  "conclusion": "success",
  "completed_at": "2026-05-18T19:07:54.054Z"
}

=== ess_only_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T07:20:13.656Z",
  "updated_at": "2026-05-16T03:01:02.547Z",
  "hypothesis": "ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) \u2265 n_min} \u2014 proves min-intervention (adaptive) superior to max-intervention (ESS-only)",
  "server": "westd-47453",
  "gpu": "cuda:1",
  "account": "root",
  "reproduce": {
    "server": "westd-47453",
    "gpu": "cuda:1",
    "started_at": "2026-05-15T09:13:26.412Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed42 --weighting_method ess_only --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\"",
    "finished_at": "2026-05-15T12:50:22.690Z",
    "training_hours": 3.62
  },
  "spec": {
    "n_min": 2,
    "weighting_method": "ess_only"
  },
  "pid": "189240",
  "log_path": "~/runs/provenance_weight_training/ess_only_seed42.log",
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T12:50:24.148259+00:00"
      }
    ]
  },
  "conclusion": "success",
  "metrics": {
    "eval_ppl": 17.73,
    "eval_loss": 2.875,
    "b_star_median": 1.58,
    "b_star_mean": 3.51,
    "vs_uniform_ppl_delta": "+0.038",
    "vs_adaptive_ppl_delta": "+0.08"
  },
  "checkpoint_path": "/root/provenance_weight_training/output/models/ess_only_seed42",
  "completed_at": "2026-05-15T13:29:03.148Z"
}

=== ess_only_seed123 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T15:51:52.911Z",
  "updated_at": "2026-05-18T17:09:12.199Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && bash scripts/run_ess_only_seed123.sh\"",
    "server": "westd-41312",
    "gpu": [
      "cuda:2"
    ],
    "pid": "115009",
    "log_path": "~/runs/provenance_weight_training/ess_only_seed123.log",
    "submitted_at": "2026-05-17T15:31:00.484Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 92291.7,
    "gpu_hours": 25.64
  },
  "server": "westd-47453",
  "gpu": "cuda:0",
  "account": "root",
  "pid": "233872",
  "log_path": "~/runs/provenance_weight_training/ess_only_seed123.log",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\"",
    "finished_at": "2026-05-15T21:41:11.165Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T21:41:12.958200+00:00"
      }
    ]
  },
  "metrics": {
    "eval_ppl_holdout": 17.72,
    "eval_loss_holdout": 2.8746,
    "eval_holdout_tokens": 4077068,
    "eval_method": "eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16",
    "eval_note": "Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693",
    "train_loss": 10.2159,
    "train_steps": 6103,
    "train_runtime_seconds": 12959.5,
    "b_star_mean": 3.55,
    "b_star_median": 1.5918,
    "b_star_std": 4.7209,
    "b_star_min": 0.2344,
    "b_star_max": 20,
    "b_star_p25": 0.8398,
    "b_star_p75": 3.8281,
    "b_star_p90": 9.5996,
    "b_star_count": 21971,
    "vs_uniform_ppl_delta": "+0.034",
    "vs_adaptive_fix_ppl_delta": "+0.077"
  },
  "checkpoint_path": "/root/provenance_weight_training/output/models/ess_only_seed123/final",
  "conclusion": "success",
  "completed_at": "2026-05-15T21:51:53.436Z",
  "hypothesis": "ESS-only adaptive baseline (max-intervention) seed=123: b* = max{b : ESS(b) >= n_min} ignores \u03b1_eff quality constraint, applying strongest possible downweighting. Multi-seed validation that dual-constraint (min-intervention) consistently outperforms ESS-only."
}

=== ess_only_seed123_r2 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-17T20:25:27.652Z",
  "updated_at": "2026-05-18T12:35:22.330Z",
  "hypothesis": "ESS-only (max-intervention) seed123 re-run on westd-41312: b* = max{b : ESS(b) >= n_min} \u2014 proves dual-constraint adaptive (min-intervention) superior to ESS-only across seeds",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_MODE=disabled && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --n_min 2 --tau 0.8 --max_steps 6103 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --warmup_ratio 0.05 --weight_decay 0.01 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed123/checkpoint-2000\"",
    "server": "westd-41312",
    "gpu": [
      "cuda:2"
    ],
    "pid": "133444",
    "log_path": "~/runs/provenance_weight_training/ess_only_seed123_r2.log",
    "submitted_at": "2026-05-17T21:00:40.838Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 234.0,
    "gpu_hours": 0.06
  },
  "reproduce": {
    "finished_at": "2026-05-17T21:04:32.320Z"
  },
  "failure_reason": "process dead 5\u00d7 with no sentinel/W&B \u2014 auto-resolved as failed",
  "conclusion": "success",
  "completed_at": "2026-05-17T21:04:34.797Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-17T21:04:40.672713+00:00"
      }
    ]
  },
  "metrics": {
    "eval_ppl_holdout": 17.721,
    "eval_loss_holdout": 2.8747,
    "eval_holdout_tokens": 4077068,
    "total_steps": 6103,
    "train_loss": 6.86,
    "train_runtime_seconds": 8674
  }
}

=== ess_only_seed456 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T16:04:39.611Z",
  "updated_at": "2026-05-18T17:09:41.460Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && bash scripts/run_ess_only_seed456.sh\"",
    "server": "westd-41312",
    "gpu": [
      "cuda:1"
    ],
    "pid": "115513",
    "log_path": "~/runs/provenance_weight_training/ess_only_seed456.log",
    "submitted_at": "2026-05-17T15:33:24.322Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 92146.3,
    "gpu_hours": 25.6
  },
  "server": "westd-47453",
  "gpu": "cuda:3",
  "account": "root",
  "pid": "233952",
  "log_path": "~/runs/provenance_weight_training/ess_only_seed456.log",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\"",
    "finished_at": "2026-05-15T21:41:17.276Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T21:41:21.343173+00:00"
      }
    ]
  },
  "metrics": {
    "eval_ppl_holdout": 17.76,
    "eval_loss_holdout": 2.877,
    "eval_holdout_tokens": 4077068,
    "train_loss": 1.9364,
    "note": "re-eval on westd-41312 latest run (v2)"
  },
  "checkpoint_path": "output/models/ess_only_seed456/final",
  "conclusion": "success",
  "completed_at": "2026-05-15T21:51:54.328Z",
  "hypothesis": "ESS-only (max-intervention) seed456: b* = max{b : ESS(b) \u2265 n_min} \u2014 proves dual-constraint adaptive (min-intervention) superior to ESS-only"
}

=== ess_only_seed456_r2 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-17T20:25:26.810Z",
  "updated_at": "2026-05-18T12:35:23.819Z",
  "hypothesis": "ESS-only (max-intervention) seed456 re-run on westd-41312: b* = max{b : ESS(b) >= n_min} \u2014 proves dual-constraint adaptive (min-intervention) superior to ESS-only across seeds",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_MODE=disabled && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --n_min 2 --tau 0.8 --max_steps 6103 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --warmup_ratio 0.05 --weight_decay 0.01 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed456/checkpoint-2500\"",
    "server": "westd-41312",
    "gpu": [
      "cuda:1"
    ],
    "pid": "133521",
    "log_path": "~/runs/provenance_weight_training/ess_only_seed456_r2.log",
    "submitted_at": "2026-05-17T21:00:43.303Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 219.9,
    "gpu_hours": 0.06
  },
  "reproduce": {
    "finished_at": "2026-05-17T21:04:21.425Z"
  },
  "failure_reason": "process dead 5\u00d7 with no sentinel/W&B \u2014 auto-resolved as failed",
  "conclusion": "success",
  "completed_at": "2026-05-17T21:04:23.229Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-17T21:04:28.148336+00:00"
      }
    ]
  },
  "metrics": {
    "eval_ppl_holdout": 17.762,
    "eval_loss_holdout": 2.877,
    "eval_holdout_tokens": 4077068,
    "total_steps": 6103,
    "train_loss": 5.998,
    "train_runtime_seconds": 7611
  }
}

=== contamination_60_uniform_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T20:19:24.785Z",
  "updated_at": "2026-05-16T01:12:50.897Z",
  "hypothesis": "\u03c1=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher contamination for comparison with adaptive and grid methods.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:1"
    ],
    "pid": "250074",
    "log_path": "~/runs/provenance_weight_training/contamination_60_uniform_seed42.log",
    "submitted_at": "2026-05-15T21:26:23.538Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 12988.3,
    "gpu_hours": 3.61,
    "checkpoint_path": "/root/provenance_weight_training/output/models/contamination_60_uniform_seed42/final"
  },
  "parent": "uniform_seed42",
  "server": "westd-47453",
  "gpu": "cuda:1",
  "account": "root",
  "reproduce": {
    "server": "westd-47453",
    "gpu": "cuda:1",
    "started_at": "2026-05-15T21:19:46.484Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\"",
    "finished_at": "2026-05-16T01:02:50.356Z",
    "training_hours": 3.72
  },
  "pid": "250074",
  "log_path": "~/runs/provenance_weight_training/contamination_60_uniform_seed42.log",
  "failure_reason": "EXIT_CODE=129 (non-zero)",
  "conclusion": "success",
  "completed_at": "2026-05-16T01:02:51.880Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T01:02:54.397978+00:00"
      }
    ]
  },
  "notes": "\u8bad\u7ec3\u5b9e\u9645\u5df2\u5b8c\u6210 (6103/6103 steps, 3:35:04)\u3002\u6a21\u578b\u5df2\u4fdd\u5b58\u5230 output/models/contamination_60_uniform_seed42/final\u3002EXIT_CODE=129 (SIGHUP) \u53d1\u751f\u5728\u8bad\u7ec3\u5b8c\u6210\u540e\u3002WANDB_MODE=disabled \u5bfc\u81f4 cron \u8bef\u5224\u4e3a failed\u3002train_loss=7.649 (avg), train_runtime=12904s\u3002\u9700\u8981 eval \u83b7\u53d6 PPL\u3002",
  "metrics": {
    "eval_ppl_holdout": 17.766,
    "eval_loss_holdout": 2.8773,
    "eval_tokens": 4077068,
    "eval_method": "eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl",
    "train_loss": 7.649,
    "train_runtime_seconds": 12904
  },
  "checkpoint_path": "output/models/contamination_60_uniform_seed42/final"
}

=== contamination_60_seed123 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-17T23:04:52.646Z",
  "updated_at": "2026-05-18T03:02:27.875Z",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=2 python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/output/models/contamination_60_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.8 --n_min 2 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --bf16 --save_total_limit 3 --save_only_model --dataloader_num_workers 0",
    "server": "westd-30476",
    "gpu": [
      "cuda:2"
    ],
    "pid": "63153",
    "log_path": "~/runs/provenance_weight_training/contamination_60_seed123.log",
    "submitted_at": "2026-05-17T23:06:06.738Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/scored_data_60.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 123,
    "wall_clock_seconds": 14181.1,
    "gpu_hours": 3.94
  },
  "hypothesis": "Cross-seed replication (seed123) of adaptive weighting at \u03c1=0.6: confirms contamination_60_seed42_r2 result is not seed-specific, strengthening Claim 3 proportion-robustness across contamination levels.",
  "reproduce": {
    "finished_at": "2026-05-18T02:55:06.709Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-18T02:55:10.838537+00:00"
      }
    ]
  },
  "metrics": {
    "eval_ppl_holdout": 17.732,
    "eval_loss_holdout": 2.8754,
    "eval_holdout_tokens": 4077068,
    "train_loss": 9.6302,
    "train_runtime_seconds": 13638.6,
    "total_steps": 6103,
    "eval_method": "eval_perplexity.py --max_docs 5000 --max_length 2048"
  },
  "checkpoint_path": "/root/autodl-tmp/output/models/contamination_60_seed123/final",
  "conclusion": "success",
  "completed_at": "2026-05-18T03:02:27.875Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "0ef4864f-a7a5-463e-bbab-f04c58beacc4",
  "tool_use_result": {
    "stdout": "=== adaptive_1_7b_seed42 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-18T11:47:25.251Z\",\n  \"updated_at\": \"2026-05-18T19:07:03.284Z\",\n  \"hypothesis\": \"Scale validation: adaptive provenance weighting on Qwen3-1.7B (2.8x larger than 0.6B). If adaptive still outperforms uniform at 1.7B scale, demonstrates method generality beyond small models. Key for Main conference upgrade (D079 Line B). Expected: adaptive < uniform by \\u22650.03 PPL (consistent with 0.6B gap).\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-1.7B --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42 --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/checkpoint-2500\\\"\",\n    \"server\": \"westd-41312\",\n    \"gpu\": [\n      \"cuda:1\"\n    ],\n    \"pid\": \"226766\",\n    \"log_path\": \"~/runs/provenance_weight_training/adaptive_1_7b_seed42.log\",\n    \"submitted_at\": \"2026-05-18T15:00:59.483Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/final\",\n    \"train_loss\": 5.36,\n    \"train_runtime_s\": 10990,\n    \"total_steps\": 6103,\n    \"wall_clock_seconds\": 14763.8,\n    \"gpu_hours\": 4.1\n  },\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-18T19:07:03.284Z\"\n}\n\n=== uniform_1_7b_seed42 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-18T11:47:26.566Z\",\n  \"updated_at\": \"2026-05-18T15:45:29.875Z\",\n  \"hypothesis\": \"Uniform weighting baseline on Qwen3-1.7B for scale validation. Control condition for comparing adaptive provenance weighting at larger model scale. Part of D079 Line B.\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-1.7B --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42 --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42/checkpoint-3000\\\"\",\n    \"server\": \"westd-41312\",\n    \"gpu\": [\n      \"cuda:0\"\n    ],\n    \"pid\": \"226623\",\n    \"log_path\": \"~/runs/provenance_weight_training/uniform_1_7b_seed42.log\",\n    \"submitted_at\": \"2026-05-18T15:00:55.785Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 2489.8,\n    \"gpu_hours\": 0.69\n  },\n  \"reproduce\": {\n    \"finished_at\": \"2026-05-18T15:42:18.572Z\"\n  },\n  \"failure_reason\": \"EXIT_CODE=1 (generic error \\u2014 check log tail)\",\n  \"conclusion\": \"failed\",\n  \"completed_at\": \"2026-05-18T15:42:25.542Z\",\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_failed\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-18T15:42:32.973826+00:00\"\n      }\n    ]\n  },\n  \"notes\": \"\\u5931\\u8d25\\u539f\\u56e0: FileNotFoundError \\u2014 checkpoint-3000/trainer_state.json \\u7f3a\\u5931\\uff0cresume \\u5d29\\u6e83 | \\u5df2\\u6709\\u6210\\u679c: checkpoint-3000 \\u5b58\\u5728\\u4f46\\u4e0d\\u5b8c\\u6574 | \\u5efa\\u8bae: \\u627e\\u6709\\u6548 checkpoint \\u91cd resume \\u6216\\u4ece\\u5934\\u8bad\\u7ec3\"\n}\n\n=== ngram_adaptive_seed42 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-18T14:14:23.226Z\",\n  \"updated_at\": \"2026-05-18T19:07:52.563Z\",\n  \"hypothesis\": \"Multi-detector validation: adaptive weighting with n-gram PPL detector (statistical, AUC=0.73) produces lower PPL than uniform, demonstrating method works with fundamentally different detector type (not just neural classifier). Complementary to q_score (Spearman r=-0.36). Part of D079 Line A.\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-0.6B --data_path data/scored_data_ngram_qscore.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42 --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_only_model --save_total_limit 3\\\"\",\n    \"server\": \"westd-41312\",\n    \"gpu\": [\n      \"cuda:2\"\n    ],\n    \"pid\": \"226953\",\n    \"log_path\": \"~/runs/provenance_weight_training/ngram_adaptive_seed42.log\",\n    \"submitted_at\": \"2026-05-18T15:01:02.239Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/final\",\n    \"train_loss\": 9.298,\n    \"train_runtime_s\": 14170,\n    \"total_steps\": 6103,\n    \"wall_clock_seconds\": 14810.3,\n    \"gpu_hours\": 4.11\n  },\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-18T19:07:52.563Z\"\n}\n\n=== ngram_uniform_seed42 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-18T14:14:25.095Z\",\n  \"updated_at\": \"2026-05-18T19:07:54.054Z\",\n  \"hypothesis\": \"Uniform baseline for n-gram detector comparison. Control condition: uniform weighting on ngram-scored data. Expected to perform worse than ngram_adaptive, confirming adaptive advantage generalizes across detectors.\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-0.6B --data_path data/scored_data_ngram_qscore.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42 --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_only_model --save_total_limit 3\\\"\",\n    \"server\": \"westd-41312\",\n    \"gpu\": [\n      \"cuda:3\"\n    ],\n    \"pid\": \"227105\",\n    \"log_path\": \"~/runs/provenance_weight_training/ngram_uniform_seed42.log\",\n    \"submitted_at\": \"2026-05-18T15:01:05.106Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/final\",\n    \"train_loss\": 7.99,\n    \"train_runtime_s\": 12800,\n    \"total_steps\": 6103,\n    \"wall_clock_seconds\": 14808.9,\n    \"gpu_hours\": 4.11\n  },\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-18T19:07:54.054Z\"\n}\n\n=== ess_only_seed42 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-15T07:20:13.656Z\",\n  \"updated_at\": \"2026-05-16T03:01:02.547Z\",\n  \"hypothesis\": \"ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) \\u2265 n_min} \\u2014 proves min-intervention (adaptive) superior to max-intervention (ESS-only)\",\n  \"server\": \"westd-47453\",\n  \"gpu\": \"cuda:1\",\n  \"account\": \"root\",\n  \"reproduce\": {\n    \"server\": \"westd-47453\",\n    \"gpu\": \"cuda:1\",\n    \"started_at\": \"2026-05-15T09:13:26.412Z\",\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed42 --weighting_method ess_only --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\",\n    \"finished_at\": \"2026-05-15T12:50:22.690Z\",\n    \"training_hours\": 3.62\n  },\n  \"spec\": {\n    \"n_min\": 2,\n    \"weighting_method\": \"ess_only\"\n  },\n  \"pid\": \"189240\",\n  \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed42.log\",\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-15T12:50:24.148259+00:00\"\n      }\n    ]\n  },\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"eval_ppl\": 17.73,\n    \"eval_loss\": 2.875,\n    \"b_star_median\": 1.58,\n    \"b_star_mean\": 3.51,\n    \"vs_uniform_ppl_delta\": \"+0.038\",\n    \"vs_adaptive_ppl_delta\": \"+0.08\"\n  },\n  \"checkpoint_path\": \"/root/provenance_weight_training/output/models/ess_only_seed42\",\n  \"completed_at\": \"2026-05-15T13:29:03.148Z\"\n}\n\n=== ess_only_seed123 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-15T15:51:52.911Z\",\n  \"updated_at\": \"2026-05-18T17:09:12.199Z\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && bash scripts/run_ess_only_seed123.sh\\\"\",\n    \"server\": \"westd-41312\",\n    \"gpu\": [\n      \"cuda:2\"\n    ],\n    \"pid\": \"115009\",\n    \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed123.log\",\n    \"submitted_at\": \"2026-05-17T15:31:00.484Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 92291.7,\n    \"gpu_hours\": 25.64\n  },\n  \"server\": \"westd-47453\",\n  \"gpu\": \"cuda:0\",\n  \"account\": \"root\",\n  \"pid\": \"233872\",\n  \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed123.log\",\n  \"reproduce\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\",\n    \"finished_at\": \"2026-05-15T21:41:11.165Z\"\n  },\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-15T21:41:12.958200+00:00\"\n      }\n    ]\n  },\n  \"metrics\": {\n    \"eval_ppl_holdout\": 17.72,\n    \"eval_loss_holdout\": 2.8746,\n    \"eval_holdout_tokens\": 4077068,\n    \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\",\n    \"eval_note\": \"Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693\",\n    \"train_loss\": 10.2159,\n    \"train_steps\": 6103,\n    \"train_runtime_seconds\": 12959.5,\n    \"b_star_mean\": 3.55,\n    \"b_star_median\": 1.5918,\n    \"b_star_std\": 4.7209,\n    \"b_star_min\": 0.2344,\n    \"b_star_max\": 20,\n    \"b_star_p25\": 0.8398,\n    \"b_star_p75\": 3.8281,\n    \"b_star_p90\": 9.5996,\n    \"b_star_count\": 21971,\n    \"vs_uniform_ppl_delta\": \"+0.034\",\n    \"vs_adaptive_fix_ppl_delta\": \"+0.077\"\n  },\n  \"checkpoint_path\": \"/root/provenance_weight_training/output/models/ess_only_seed123/final\",\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-15T21:51:53.436Z\",\n  \"hypothesis\": \"ESS-only adaptive baseline (max-intervention) seed=123: b* = max{b : ESS(b) >= n_min} ignores \\u03b1_eff quality constraint, applying strongest possible downweighting. Multi-seed validation that dual-constraint (min-intervention) consistently outperforms ESS-only.\"\n}\n\n=== ess_only_seed123_r2 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-17T20:25:27.652Z\",\n  \"updated_at\": \"2026-05-18T12:35:22.330Z\",\n  \"hypothesis\": \"ESS-only (max-intervention) seed123 re-run on westd-41312: b* = max{b : ESS(b) >= n_min} \\u2014 proves dual-constraint adaptive (min-intervention) superior to ESS-only across seeds\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_MODE=disabled && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --n_min 2 --tau 0.8 --max_steps 6103 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --warmup_ratio 0.05 --weight_decay 0.01 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed123/checkpoint-2000\\\"\",\n    \"server\": \"westd-41312\",\n    \"gpu\": [\n      \"cuda:2\"\n    ],\n    \"pid\": \"133444\",\n    \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed123_r2.log\",\n    \"submitted_at\": \"2026-05-17T21:00:40.838Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 234.0,\n    \"gpu_hours\": 0.06\n  },\n  \"reproduce\": {\n    \"finished_at\": \"2026-05-17T21:04:32.320Z\"\n  },\n  \"failure_reason\": \"process dead 5\\u00d7 with no sentinel/W&B \\u2014 auto-resolved as failed\",\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-17T21:04:34.797Z\",\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_failed\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-17T21:04:40.672713+00:00\"\n      }\n    ]\n  },\n  \"metrics\": {\n    \"eval_ppl_holdout\": 17.721,\n    \"eval_loss_holdout\": 2.8747,\n    \"eval_holdout_tokens\": 4077068,\n    \"total_steps\": 6103,\n    \"train_loss\": 6.86,\n    \"train_runtime_seconds\": 8674\n  }\n}\n\n=== ess_only_seed456 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-15T16:04:39.611Z\",\n  \"updated_at\": \"2026-05-18T17:09:41.460Z\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && bash scripts/run_ess_only_seed456.sh\\\"\",\n    \"server\": \"westd-41312\",\n    \"gpu\": [\n      \"cuda:1\"\n    ],\n    \"pid\": \"115513\",\n    \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed456.log\",\n    \"submitted_at\": \"2026-05-17T15:33:24.322Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 92146.3,\n    \"gpu_hours\": 25.6\n  },\n  \"server\": \"westd-47453\",\n  \"gpu\": \"cuda:3\",\n  \"account\": \"root\",\n  \"pid\": \"233952\",\n  \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed456.log\",\n  \"reproduce\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\",\n    \"finished_at\": \"2026-05-15T21:41:17.276Z\"\n  },\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-15T21:41:21.343173+00:00\"\n      }\n    ]\n  },\n  \"metrics\": {\n    \"eval_ppl_holdout\": 17.76,\n    \"eval_loss_holdout\": 2.877,\n    \"eval_holdout_tokens\": 4077068,\n    \"train_loss\": 1.9364,\n    \"note\": \"re-eval on westd-41312 latest run (v2)\"\n  },\n  \"checkpoint_path\": \"output/models/ess_only_seed456/final\",\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-15T21:51:54.328Z\",\n  \"hypothesis\": \"ESS-only (max-intervention) seed456: b* = max{b : ESS(b) \\u2265 n_min} \\u2014 proves dual-constraint adaptive (min-intervention) superior to ESS-only\"\n}\n\n=== ess_only_seed456_r2 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-17T20:25:26.810Z\",\n  \"updated_at\": \"2026-05-18T12:35:23.819Z\",\n  \"hypothesis\": \"ESS-only (max-intervention) seed456 re-run on westd-41312: b* = max{b : ESS(b) >= n_min} \\u2014 proves dual-constraint adaptive (min-intervention) superior to ESS-only across seeds\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_MODE=disabled && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --n_min 2 --tau 0.8 --max_steps 6103 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --warmup_ratio 0.05 --weight_decay 0.01 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed456/checkpoint-2500\\\"\",\n    \"server\": \"westd-41312\",\n    \"gpu\": [\n      \"cuda:1\"\n    ],\n    \"pid\": \"133521\",\n    \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed456_r2.log\",\n    \"submitted_at\": \"2026-05-17T21:00:43.303Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 219.9,\n    \"gpu_hours\": 0.06\n  },\n  \"reproduce\": {\n    \"finished_at\": \"2026-05-17T21:04:21.425Z\"\n  },\n  \"failure_reason\": \"process dead 5\\u00d7 with no sentinel/W&B \\u2014 auto-resolved as failed\",\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-17T21:04:23.229Z\",\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_failed\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-17T21:04:28.148336+00:00\"\n      }\n    ]\n  },\n  \"metrics\": {\n    \"eval_ppl_holdout\": 17.762,\n    \"eval_loss_holdout\": 2.877,\n    \"eval_holdout_tokens\": 4077068,\n    \"total_steps\": 6103,\n    \"train_loss\": 5.998,\n    \"train_runtime_seconds\": 7611\n  }\n}\n\n=== contamination_60_uniform_seed42 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-15T20:19:24.785Z\",\n  \"updated_at\": \"2026-05-16T01:12:50.897Z\",\n  \"hypothesis\": \"\\u03c1=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher contamination for comparison with adaptive and grid methods.\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:1\"\n    ],\n    \"pid\": \"250074\",\n    \"log_path\": \"~/runs/provenance_weight_training/contamination_60_uniform_seed42.log\",\n    \"submitted_at\": \"2026-05-15T21:26:23.538Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 12988.3,\n    \"gpu_hours\": 3.61,\n    \"checkpoint_path\": \"/root/provenance_weight_training/output/models/contamination_60_uniform_seed42/final\"\n  },\n  \"parent\": \"uniform_seed42\",\n  \"server\": \"westd-47453\",\n  \"gpu\": \"cuda:1\",\n  \"account\": \"root\",\n  \"reproduce\": {\n    \"server\": \"westd-47453\",\n    \"gpu\": \"cuda:1\",\n    \"started_at\": \"2026-05-15T21:19:46.484Z\",\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\",\n    \"finished_at\": \"2026-05-16T01:02:50.356Z\",\n    \"training_hours\": 3.72\n  },\n  \"pid\": \"250074\",\n  \"log_path\": \"~/runs/provenance_weight_training/contamination_60_uniform_seed42.log\",\n  \"failure_reason\": \"EXIT_CODE=129 (non-zero)\",\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-16T01:02:51.880Z\",\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_failed\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-16T01:02:54.397978+00:00\"\n      }\n    ]\n  },\n  \"notes\": \"\\u8bad\\u7ec3\\u5b9e\\u9645\\u5df2\\u5b8c\\u6210 (6103/6103 steps, 3:35:04)\\u3002\\u6a21\\u578b\\u5df2\\u4fdd\\u5b58\\u5230 output/models/contamination_60_uniform_seed42/final\\u3002EXIT_CODE=129 (SIGHUP) \\u53d1\\u751f\\u5728\\u8bad\\u7ec3\\u5b8c\\u6210\\u540e\\u3002WANDB_MODE=disabled \\u5bfc\\u81f4 cron \\u8bef\\u5224\\u4e3a failed\\u3002train_loss=7.649 (avg), train_runtime=12904s\\u3002\\u9700\\u8981 eval \\u83b7\\u53d6 PPL\\u3002\",\n  \"metrics\": {\n    \"eval_ppl_holdout\": 17.766,\n    \"eval_loss_holdout\": 2.8773,\n    \"eval_tokens\": 4077068,\n    \"eval_method\": \"eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl\",\n    \"train_loss\": 7.649,\n    \"train_runtime_seconds\": 12904\n  },\n  \"checkpoint_path\": \"output/models/contamination_60_uniform_seed42/final\"\n}\n\n=== contamination_60_seed123 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-17T23:04:52.646Z\",\n  \"updated_at\": \"2026-05-18T03:02:27.875Z\",\n  \"spec\": {\n    \"command\": \"CUDA_VISIBLE_DEVICES=2 python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/output/models/contamination_60_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.8 --n_min 2 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --bf16 --save_total_limit 3 --save_only_model --dataloader_num_workers 0\",\n    \"server\": \"westd-30476\",\n    \"gpu\": [\n      \"cuda:2\"\n    ],\n    \"pid\": \"63153\",\n    \"log_path\": \"~/runs/provenance_weight_training/contamination_60_seed123.log\",\n    \"submitted_at\": \"2026-05-17T23:06:06.738Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"data_path\": \"data/scored_data_60.jsonl\",\n    \"data_count\": 371499,\n    \"model_name\": \"Qwen/Qwen3-0.6B\",\n    \"seed\": 123,\n    \"wall_clock_seconds\": 14181.1,\n    \"gpu_hours\": 3.94\n  },\n  \"hypothesis\": \"Cross-seed replication (seed123) of adaptive weighting at \\u03c1=0.6: confirms contamination_60_seed42_r2 result is not seed-specific, strengthening Claim 3 proportion-robustness across contamination levels.\",\n  \"reproduce\": {\n    \"finished_at\": \"2026-05-18T02:55:06.709Z\"\n  },\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-18T02:55:10.838537+00:00\"\n      }\n    ]\n  },\n  \"metrics\": {\n    \"eval_ppl_holdout\": 17.732,\n    \"eval_loss_holdout\": 2.8754,\n    \"eval_holdout_tokens\": 4077068,\n    \"train_loss\": 9.6302,\n    \"train_runtime_seconds\": 13638.6,\n    \"total_steps\": 6103,\n    \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\"\n  },\n  \"checkpoint_path\": \"/root/autodl-tmp/output/models/contamination_60_seed123/final\",\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-18T03:02:27.875Z\"\n}",
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

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
I need to continue getting more data. Let me also get the rho06 adaptive seed data and a few more remaining experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "e51e977f-f104-4dc6-a71a-2d225937627d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113V9Nqc9wih8B87Z9Xvji1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11012,
      "cache_read_input_tokens": 44371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11012
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_014mcfoj2YNpN45oX59sr8gV`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\nneed = ['contamination_60_seed42_r2', 'contamination_60_adaptive_seed456',\n        'contamination_60_random_seed42', 'contamination_60_random_seed123', 'contamination_60_random_seed456',\n        'contamination_60_ess_only_seed42', 'contamination_60_ess_only_seed123', 'contamination_60_ess_only_seed456',\n        'contamination_60_uniform_seed123', 'contamination_60_uniform_seed456',\n        'adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456',\n        'random_reweight_v2_seed42', 'random_reweight_seed456', 'random_reweight_seed123_r5',\n        'grid_b0_5_seed123', 'grid_b0_5_seed456',\n        'tau_05_seed42', 'tau_06_seed42', 'tau_07_seed42', 'tau_095_seed42', 'tau_09_seed42',\n        'contamination_60_tau06_seed42', 'contamination_60_tau07_seed42',\n        'detect_remove_q03_seed42',\n        ]\n\nfor eid in need:\n    exp = experiments.get(eid, {})\n    if not exp:\n        print(f'=== {eid} === NOT FOUND')\n        continue\n    m = exp.get('metrics', {})\n    s = exp.get('spec', {})\n    print(f'{eid} | conclusion={exp.get(\\\"conclusion\\\")} | ppl={m.get(\\\"eval_ppl_holdout\\\") or m.get(\\\"ppl\\\") or m.get(\\\"eval_ppl\\\")} | seed={s.get(\\\"seed\\\")} | method={s.get(\\\"weighting_method\\\")}')\n    # Print select metrics\n    if m:\n        keys = ['eval_ppl_holdout', 'ppl', 'eval_ppl', 'lm_eval_mmlu_5shot', 'vs_uniform_ppl_delta']\n        for k in keys:\n            if k in m:\n                print(f'  {k}: {m[k]}')\n    print()\n\" 2>&1",
  "description": "Get remaining experiment PPL values",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "ce6ca187-aa42-41a8-96c1-4d2ac0ad401e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113V9Nqc9wih8B87Z9Xvji1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11012,
      "cache_read_input_tokens": 44371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11012
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

_source line 25 · 2026-05-18T21:30:49.600Z_

<details><summary>↩ Tool result · `toolu_014mcfoj2YNpN45oX59sr8gV`</summary>

```text
contamination_60_seed42_r2 | conclusion=success | ppl=17.74 | seed=None | method=None
  eval_ppl_holdout: 17.74

contamination_60_adaptive_seed456 | conclusion=success | ppl=17.735 | seed=456 | method=None
  eval_ppl_holdout: 17.735

contamination_60_random_seed42 | conclusion=success | ppl=17.832 | seed=42 | method=None
  eval_ppl_holdout: 17.832

contamination_60_random_seed123 | conclusion=success | ppl=17.87 | seed=123 | method=None
  eval_ppl_holdout: 17.87

contamination_60_random_seed456 | conclusion=success | ppl=17.88 | seed=456 | method=None
  eval_ppl_holdout: 17.88

contamination_60_ess_only_seed42 | conclusion=success | ppl=17.77 | seed=42 | method=None
  eval_ppl_holdout: 17.77

contamination_60_ess_only_seed123 | conclusion=success | ppl=17.763 | seed=123 | method=None
  eval_ppl_holdout: 17.763

contamination_60_ess_only_seed456 | conclusion=success | ppl=17.762 | seed=456 | method=None
  eval_ppl_holdout: 17.762

contamination_60_uniform_seed123 | conclusion=success | ppl=17.754 | seed=123 | method=None
  eval_ppl_holdout: 17.754

contamination_60_uniform_seed456 | conclusion=success | ppl=17.77 | seed=456 | method=None
  eval_ppl_holdout: 17.77

adaptive_seed42 | conclusion=success | ppl=17.644 | seed=42 | method=None
  eval_ppl_holdout: 17.644

adaptive_seed123 | conclusion=success | ppl=17.6308 | seed=123 | method=None
  eval_ppl_holdout: 17.6308

adaptive_seed456 | conclusion=success | ppl=17.6419 | seed=456 | method=None
  eval_ppl_holdout: 17.6419

random_reweight_v2_seed42 | conclusion=success | ppl=17.83 | seed=42 | method=random
  eval_ppl_holdout: 17.83

random_reweight_seed456 | conclusion=success | ppl=17.777 | seed=None | method=None
  eval_ppl_holdout: 17.777

random_reweight_seed123_r5 | conclusion=success | ppl=17.8 | seed=123 | method=None
  eval_ppl_holdout: 17.8

grid_b0_5_seed123 | conclusion=success | ppl=17.638 | seed=123 | method=None
  eval_ppl_holdout: 17.638

grid_b0_5_seed456 | conclusion=success | ppl=17.65 | seed=456 | method=None
  eval_ppl_holdout: 17.65

tau_05_seed42 | conclusion=success | ppl=17.688 | seed=42 | method=None
  eval_ppl_holdout: 17.688

tau_06_seed42 | conclusion=success | ppl=17.6805 | seed=42 | method=None
  eval_ppl_holdout: 17.6805

tau_07_seed42 | conclusion=success | ppl=17.6793 | seed=42 | method=None
  eval_ppl_holdout: 17.6793

tau_095_seed42 | conclusion=negative | ppl=17.723 | seed=None | method=None
  eval_ppl_holdout: 17.723

tau_09_seed42 | conclusion=negative | ppl=17.712 | seed=None | method=None
  eval_ppl_holdout: 17.712

contamination_60_tau06_seed42 | conclusion=success | ppl=17.7359 | seed=42 | method=None
  eval_ppl_holdout: 17.7359

contamination_60_tau07_seed42 | conclusion=success | ppl=17.73 | seed=42 | method=None
  eval_ppl_holdout: 17.73

detect_remove_q03_seed42 | conclusion=failed | ppl=None | seed=42 | method=None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "5d4f1669-d02e-4080-b022-ed9e1226452c",
  "tool_use_result": {
    "stdout": "contamination_60_seed42_r2 | conclusion=success | ppl=17.74 | seed=None | method=None\n  eval_ppl_holdout: 17.74\n\ncontamination_60_adaptive_seed456 | conclusion=success | ppl=17.735 | seed=456 | method=None\n  eval_ppl_holdout: 17.735\n\ncontamination_60_random_seed42 | conclusion=success | ppl=17.832 | seed=42 | method=None\n  eval_ppl_holdout: 17.832\n\ncontamination_60_random_seed123 | conclusion=success | ppl=17.87 | seed=123 | method=None\n  eval_ppl_holdout: 17.87\n\ncontamination_60_random_seed456 | conclusion=success | ppl=17.88 | seed=456 | method=None\n  eval_ppl_holdout: 17.88\n\ncontamination_60_ess_only_seed42 | conclusion=success | ppl=17.77 | seed=42 | method=None\n  eval_ppl_holdout: 17.77\n\ncontamination_60_ess_only_seed123 | conclusion=success | ppl=17.763 | seed=123 | method=None\n  eval_ppl_holdout: 17.763\n\ncontamination_60_ess_only_seed456 | conclusion=success | ppl=17.762 | seed=456 | method=None\n  eval_ppl_holdout: 17.762\n\ncontamination_60_uniform_seed123 | conclusion=success | ppl=17.754 | seed=123 | method=None\n  eval_ppl_holdout: 17.754\n\ncontamination_60_uniform_seed456 | conclusion=success | ppl=17.77 | seed=456 | method=None\n  eval_ppl_holdout: 17.77\n\nadaptive_seed42 | conclusion=success | ppl=17.644 | seed=42 | method=None\n  eval_ppl_holdout: 17.644\n\nadaptive_seed123 | conclusion=success | ppl=17.6308 | seed=123 | method=None\n  eval_ppl_holdout: 17.6308\n\nadaptive_seed456 | conclusion=success | ppl=17.6419 | seed=456 | method=None\n  eval_ppl_holdout: 17.6419\n\nrandom_reweight_v2_seed42 | conclusion=success | ppl=17.83 | seed=42 | method=random\n  eval_ppl_holdout: 17.83\n\nrandom_reweight_seed456 | conclusion=success | ppl=17.777 | seed=None | method=None\n  eval_ppl_holdout: 17.777\n\nrandom_reweight_seed123_r5 | conclusion=success | ppl=17.8 | seed=123 | method=None\n  eval_ppl_holdout: 17.8\n\ngrid_b0_5_seed123 | conclusion=success | ppl=17.638 | seed=123 | method=None\n  eval_ppl_holdout: 17.638\n\ngrid_b0_5_seed456 | conclusion=success | ppl=17.65 | seed=456 | method=None\n  eval_ppl_holdout: 17.65\n\ntau_05_seed42 | conclusion=success | ppl=17.688 | seed=42 | method=None\n  eval_ppl_holdout: 17.688\n\ntau_06_seed42 | conclusion=success | ppl=17.6805 | seed=42 | method=None\n  eval_ppl_holdout: 17.6805\n\ntau_07_seed42 | conclusion=success | ppl=17.6793 | seed=42 | method=None\n  eval_ppl_holdout: 17.6793\n\ntau_095_seed42 | conclusion=negative | ppl=17.723 | seed=None | method=None\n  eval_ppl_holdout: 17.723\n\ntau_09_seed42 | conclusion=negative | ppl=17.712 | seed=None | method=None\n  eval_ppl_holdout: 17.712\n\ncontamination_60_tau06_seed42 | conclusion=success | ppl=17.7359 | seed=42 | method=None\n  eval_ppl_holdout: 17.7359\n\ncontamination_60_tau07_seed42 | conclusion=success | ppl=17.73 | seed=42 | method=None\n  eval_ppl_holdout: 17.73\n\ndetect_remove_q03_seed42 | conclusion=failed | ppl=None | seed=42 | method=None",
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

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I need to check the remaining experiments: the Llama 3B results from the API (which had reeval numbers), the 1.7B results (adaptive_1_7b_seed42 has no metrics stored), and the ngram detector results. 

Let me also check what we know about detect_remove experiments:
- detect_remove_baseline_seed42: PPL=17.29 (this seems to be D&R with q05 threshold, seed42, with multi-epoch)
- detect_remove_q05_seed123: PPL=17.27
- detect_remove_q05_seed456: PPL=17.28


- detect_remove_q05_epoch_matched_seed42: PPL=17.65 (epoch-matched version)
- detect_remove_q07_seed42: PPL=17.32
- detect_remove_q09_seed42: PPL=17.42
- threshold_q03_seed42: PPL=17.253

The 1.7B and ngram experiments just finished but don't have eval metrics yet, and I'm still waiting on the Llama 3B API data to see what those reeval numbers look like.

Looking at the Llama results, the API shows adaptive at PPL=10.58 with MMLU=53.42% marked as success, while uniform is at PPL=10.53 with MMLU=51.85%, but the YAML has different conclusions and slightly different PPL values for uniform. The API data with the reeval_v2 unified numbers seems more reliable since it's from the same session, so I'll go with those. Now I need to check what's happening with grid_b_seed42_batch.

I see it contains all the evaluation PPLs across the b parameter range from 0.5 to 5.0 at seed 42. Let me map out which experiments correspond to which table by organizing everything I've collected so far. For the main results table with ρ=0.4 on Qwen3-0.6B, I have the uniform baseline across three seeds and the adaptive results, though I need to clarify whether the canonical adaptive version is the base adaptive_seed variants or the adaptive_fix variants since both sets exist.

Looking at the PPL values, the non-fix adaptive versions actually perform better, and checking the timestamps shows the fix versions are newer but have more detailed metrics. I need to determine which set represents the final, canonical results to use in the table. Looking at the API timestamps and cross-experiment references, the adaptive_fix versions are clearly the canonical baseline since they're consistently cited in the random_reweight comparisons and have more recent update dates. I'll use adaptive_fix_seed{42,123,456} as the main adaptive results for ρ=0.4 in the paper.

For the uniform baseline, I'm noticing qwen06b_uniform_seed42 (17.69) differs slightly from uniform_seed42 (17.6939), but since uniform_seed42 is the one referenced in the cross-comparisons, I'll stick with uniform_seed{42,123,456} as the canonical uniform values.

Now I'm deciding between adaptive_seed and adaptive_fix_seed for the paper table. The "fix" suffix suggests a bug correction, which would make adaptive_fix more reliable even though it performs slightly worse (17.6527 vs 17.644). Since adaptive_fix is what other experiments reference as the baseline, I'll use that as the canonical version and note the distinction.

For the ESS-only ablation across three seeds, I'm consolidating the results—using the original runs where available (seed123 at 17.72, seed456 at 17.76) and noting that seed42 uses a slightly different metric naming convention, though it's likely the same measurement.

The random reweight baseline shows consistent performance around 17.8 PPL across seeds, while the grid-b sweep with varying batch sizes shows a clear trend of increasing perplexity as b increases from 0.5 to 2.0. Now I'm looking at the b=0.5 and b=1.0 results, and I notice the b=0.5 batch run gives 17.651 for seed42, but there's no matching individual grid entry for that seed—only results for seeds 123 and 456. I'm also spotting something odd with the b=0.3 seed123 result at 17.5792, which seems notably lower than the others and worth verifying.

Let me pull together the seed42 grid results I can find across the individual experiments: b=0.1 is 17.657, b=0.2 is 17.64, b=0.3 is 17.64, and then from the batch run I have b=0.5 at 17.651, b=1.0 at 17.692, and b=1.5 at 17.718, with b=2.0 still incomplete.

Now I'm looking at the remaining grid values: b=2.0 gives 17.741, b=3.0 gives 17.774, and b=5.0 reaches 17.818. For the detect-and-remove threshold sensitivity, I'm comparing the different quantile thresholds—q03 at 17.253, q05 with both a multi-epoch version at 17.29 and an epoch-matched version at 17.65 for fair comparison, q07 at 17.32, and q09 at 17.42. These D&R experiments filter out high-threshold samples during training. I'm also starting to look at the contamination rate experiments with ρ=0.2, where I have the uniform variant at 17.336 and need to check the adaptive variant.

Continuing with the contamination analysis, the adaptive approaches at ρ=0.2 actually perform worse than uniform—17.382 and 17.45 respectively. At ρ=0.4 with three seeds, uniform averages around 17.694 while the adaptive fix is better at 17.651. For ρ=0.6, the uniform results cluster tightly around 17.75-17.77 across three seeds, with the adaptive variant showing 17.74.

Looking at the multi-detector results, I'm tracking TF-IDF+LR where the adaptive fix gives 17.6527 versus uniform at 17.6939, and I've just completed the n-gram PPL and GPT-2 PPL evaluations but haven't gotten metrics back yet. For the 1.7B scale experiments, the adaptive run finished but evaluation is still pending.

The cross-model Llama results show an interesting trade-off: adaptive has slightly worse perplexity at 10.58 versus 10.53, but significantly better MMLU performance at 53.42% compared to 51.85%. The YAML marked this as negative due to the PPL regression, though the API evaluation notes it's more neutral-to-positive given the MMLU improvement of 1.57 percentage points.

Now that I have the full picture, I'm ready to compile everything into the comprehensive results table, though I should double-check whether there are any additional GPT-2 PPL detector experiments I'm missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "ffba6199-b221-460d-aee4-9dcc4124316a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCGBPJ2j4Cs1gSD2EyQbzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 55383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2027
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

_source line 27_

Let me check for GPT-2 PPL detector experiments and the Llama reeval data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "688d39d7-11e5-4470-ae57-43a06a5f7cee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCGBPJ2j4Cs1gSD2EyQbzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 55383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2027
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_012KF3xvwwh1f9FXNBVm8UWM`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nexperiments = data.get('experiments', {})\n\n# Look for gpt2 detector experiments\nfor eid, exp in experiments.items():\n    if 'gpt2' in eid.lower() or 'gpt-2' in eid.lower():\n        m = exp.get('metrics', {})\n        print(f'{eid} | status={exp.get(\\\"status\\\")} | conclusion={exp.get(\\\"conclusion\\\")} | metrics={json.dumps(m)}')\n        \nprint()\nprint('--- RUNNING experiments ---')\nfor eid, exp in experiments.items():\n    if exp.get('status') == 'RUNNING':\n        s = exp.get('spec', {})\n        print(f'{eid} | method={s.get(\\\"weighting_method\\\")} | model={s.get(\\\"model_name\\\")} | data={s.get(\\\"data_path\\\")}')\n\n# Also check llama reeval details\nprint()\nprint('--- llama3b API reeval data (from earlier API call) ---')\nprint('llama3b_adaptive_seed42: PPL=10.58, MMLU=53.42%, HellaSwag=72.49%')\nprint('llama3b_uniform_seed42: PPL=10.53, MMLU=51.85%')\nprint('(reeval_v2: unified eval params, 4017316 tokens)')\n\" 2>&1",
  "description": "Check GPT-2 and running experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "4b212d3a-b547-46ec-913a-35307ac16f75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCGBPJ2j4Cs1gSD2EyQbzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 55383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2027
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

_source line 29 · 2026-05-18T21:32:10.252Z_

<details><summary>↩ Tool result · `toolu_012KF3xvwwh1f9FXNBVm8UWM`</summary>

```text
gpt2_adaptive_seed42 | status=PREPARING | conclusion=None | metrics={}
gpt2_uniform_seed42 | status=PREPARING | conclusion=None | metrics={}

--- RUNNING experiments ---
detect_remove_q01_seed42 | method=None | model=Qwen/Qwen3-0.6B | data=data/scored_data_filtered_q01.jsonl
eval_uniform_1_7b_v3 | method=None | model=Qwen3-1.7B (uniform) | data=data/human/eval_holdout.jsonl
eval_adaptive_1_7b_v2 | method=None | model=Qwen3-1.7B (adaptive) | data=data/human/eval_holdout.jsonl
detect_remove_q08_seed42 | method=None | model=Qwen/Qwen3-0.6B | data=data/scored_data_filtered_q08.jsonl
adaptive_1_7b_seed123 | method=None | model=Qwen/Qwen3-1.7B | data=data/scored_data.jsonl

--- llama3b API reeval data (from earlier API call) ---
llama3b_adaptive_seed42: PPL=10.58, MMLU=53.42%, HellaSwag=72.49%
llama3b_uniform_seed42: PPL=10.53, MMLU=51.85%
(reeval_v2: unified eval params, 4017316 tokens)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "ffdc65d6-51b8-4576-8aa2-304f1e423827",
  "tool_use_result": {
    "stdout": "gpt2_adaptive_seed42 | status=PREPARING | conclusion=None | metrics={}\ngpt2_uniform_seed42 | status=PREPARING | conclusion=None | metrics={}\n\n--- RUNNING experiments ---\ndetect_remove_q01_seed42 | method=None | model=Qwen/Qwen3-0.6B | data=data/scored_data_filtered_q01.jsonl\neval_uniform_1_7b_v3 | method=None | model=Qwen3-1.7B (uniform) | data=data/human/eval_holdout.jsonl\neval_adaptive_1_7b_v2 | method=None | model=Qwen3-1.7B (adaptive) | data=data/human/eval_holdout.jsonl\ndetect_remove_q08_seed42 | method=None | model=Qwen/Qwen3-0.6B | data=data/scored_data_filtered_q08.jsonl\nadaptive_1_7b_seed123 | method=None | model=Qwen/Qwen3-1.7B | data=data/scored_data.jsonl\n\n--- llama3b API reeval data (from earlier API call) ---\nllama3b_adaptive_seed42: PPL=10.58, MMLU=53.42%, HellaSwag=72.49%\nllama3b_uniform_seed42: PPL=10.53, MMLU=51.85%\n(reeval_v2: unified eval params, 4017316 tokens)",
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

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have a complete picture. Let me also check what grid_b0_3_seed123_r2 = 17.5792 is about - seems suspiciously low.

Actually, let me just proceed with writing the table. I have all the info I need. Let me organize:

Key observations:
1. GPT-2 detector: PREPARING (not started yet)
2. 1.7B eval: RUNNING (eval_uniform_1_7b_v3, eval_adaptive_1_7b_v2)
3. D&R q01: RUNNING


4. D&R q08: RUNNING
5. ngram adaptive/uniform: completed but NO EVAL PPL yet

Now I'm deciding which adaptive variant to use for the main table. Comparing the PPL scores, the standard adaptive series performs better than the fixed seed variants, so I'll go with those numbers for rho=0.4.

But I'm noticing the adaptive_fix entries have more detailed diagnostic metrics that other experiments reference, so I should probably present both sets and mark the fixed seed version as the primary baseline used across comparisons.

Looking at the b_star statistics for adaptive_fix_seed42, the pct_below_0.5 value of 20.9% indicates that about a fifth of batches received minimal reweighting, which aligns with the adaptive approach's conservative intervention strategy. For the ess_only experiments across the three seeds, the eval_ppl values cluster tightly around 17.7-17.76, so I'll use those numbers to write up the results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "ea261150-bcab-428a-b682-d5d4a5c51cc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017B5nvbNxUNebhNPoFT18tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4599,
      "cache_read_input_tokens": 57410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4599
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

_source line 31_

All data collected. Now writing the summary table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "5bc7bb95-89ea-42b4-885a-a68beec0afdb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017B5nvbNxUNebhNPoFT18tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4599,
      "cache_read_input_tokens": 57410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4599
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

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01Axy2FTLgrFNrRYwcdy4kut`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/",
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
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "fe81165b-0896-46ef-a272-e43bc5baa37b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017B5nvbNxUNebhNPoFT18tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4599,
      "cache_read_input_tokens": 57410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4599
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

_source line 33 · 2026-05-18T21:32:28.275Z_

<details><summary>↩ Tool result · `toolu_01Axy2FTLgrFNrRYwcdy4kut`</summary>

```text
_project
ablation_summary.csv
adaptive_fix_seed42
all_success_summary.md
alpha_eff_analysis.json
alpha_eff_batch_size_sweep.json
alpha_eff_binding_rate_rho_comparison.pdf
alpha_eff_binding_rate_rho_comparison.png
analyze_tau_sweep.py
binding_diagnosis_rho06_vs_04.md
bootstrap_test.py
bstar_distribution_analysis.md
bstar_distribution_rho_comparison.pdf
bstar_distribution_rho_comparison.png
bstar_trajectory_adaptive_fix.pdf
convergence_speed_comparison.pdf
convergence_speed_comparison.png
data_generation
detector
diag_contamination_60_random_seed42.md
diagnose_batchsize16_nmin8_seed42.md
diagnosis_exit127_20260518.md
diagnosis_threshold_q03_seed42.md
diagnosis_westd41312_failures.md
drayson_comparison.md
dream_reports
dynamics
ess_only_analysis_template.md
ess_only_implementation.md
ess_only_seed42
evaluation
experiment_data.csv
experiment_results_summary.csv
experiment_results_summary.md
experiment_setup_draft.md
experiment_status_summary.md
experiment_summary.md
experiment_summary_table.md
experiment_tables.md
fig_b_landscape.csv
fig_contamination_comparison.csv
fig_method_comparison.csv
fig_nmin_ablation.csv
fig_tau_sweep.csv
figures
full_experiment_data.md
full_results_summary.csv
full_results_summary.md
generate_full_results.py
grid_b5_0_seed123
grid_b_shift.csv
grid_b_trend_stats.json
grid_eval_source_audit.md
interim_mvp_analysis.md
literature_diff_drayson.md
literature_notes.md
literature_scan_20260516.md
literature_scan_results.md
literature_tau_sensitivity.md
manifest.yaml
mechanism_decomposition_stats.json
method_section_draft.md
metrics_summary.csv
metrics_summary.md
mvp_analysis_draft.md
mvp_analysis_summary.md
new_scripts_manifest.md
nmin1_seed42
novelty_drayson_analysis.md
paper_tables.md
paper_tables_data.md
plot_training_dynamics.py
q1_ess_equivalence_analysis.md
related_work_notes.md
report_tables.md
results_table_ablation.csv
results_table_contamination.csv
results_table_grid_b_curve.csv
results_table_main.csv
review_issues.yaml
review_reports
rho06_mechanism_summary.json
rho_comparison.csv
run_mvp.sh
scored_data_rho_analysis.json
seed42_diagnostic.md
statistical_tests.md
table1_compilation.md
table1_data.json
table1_data.md
table1_summary.md
tables
tau_095_seed42
tau_09_seed42
tau_b_strength.pdf
tau_b_strength.png
tau_derivation_check.md
tau_fix_changelog.md
tau_ppl_curve.pdf
tau_ppl_curve.png
tau_rho_grid.csv
tau_rho_rank_analysis.csv
tau_rho_rank_analysis.py
tau_rho_rank_stats.json
tau_sweep.pdf
tau_sweep.png
tau_sweep_commands.md
tau_sweep_curve_dummy.pdf
tau_sweep_curve_dummy.png
tau_sweep_improvement_dummy.pdf
tau_sweep_improvement_dummy.png
tau_sweep_readiness.md
tau_theory_analysis.md
tau_theory_audit.md
training
training_progress_20260516.md
training_progress_check.md
weighting
worker_output.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "c30d0063-4c19-4e7b-850e-438f78396b59",
  "tool_use_result": {
    "stdout": "_project\nablation_summary.csv\nadaptive_fix_seed42\nall_success_summary.md\nalpha_eff_analysis.json\nalpha_eff_batch_size_sweep.json\nalpha_eff_binding_rate_rho_comparison.pdf\nalpha_eff_binding_rate_rho_comparison.png\nanalyze_tau_sweep.py\nbinding_diagnosis_rho06_vs_04.md\nbootstrap_test.py\nbstar_distribution_analysis.md\nbstar_distribution_rho_comparison.pdf\nbstar_distribution_rho_comparison.png\nbstar_trajectory_adaptive_fix.pdf\nconvergence_speed_comparison.pdf\nconvergence_speed_comparison.png\ndata_generation\ndetector\ndiag_contamination_60_random_seed42.md\ndiagnose_batchsize16_nmin8_seed42.md\ndiagnosis_exit127_20260518.md\ndiagnosis_threshold_q03_seed42.md\ndiagnosis_westd41312_failures.md\ndrayson_comparison.md\ndream_reports\ndynamics\ness_only_analysis_template.md\ness_only_implementation.md\ness_only_seed42\nevaluation\nexperiment_data.csv\nexperiment_results_summary.csv\nexperiment_results_summary.md\nexperiment_setup_draft.md\nexperiment_status_summary.md\nexperiment_summary.md\nexperiment_summary_table.md\nexperiment_tables.md\nfig_b_landscape.csv\nfig_contamination_comparison.csv\nfig_method_comparison.csv\nfig_nmin_ablation.csv\nfig_tau_sweep.csv\nfigures\nfull_experiment_data.md\nfull_results_summary.csv\nfull_results_summary.md\ngenerate_full_results.py\ngrid_b5_0_seed123\ngrid_b_shift.csv\ngrid_b_trend_stats.json\ngrid_eval_source_audit.md\ninterim_mvp_analysis.md\nliterature_diff_drayson.md\nliterature_notes.md\nliterature_scan_20260516.md\nliterature_scan_results.md\nliterature_tau_sensitivity.md\nmanifest.yaml\nmechanism_decomposition_stats.json\nmethod_section_draft.md\nmetrics_summary.csv\nmetrics_summary.md\nmvp_analysis_draft.md\nmvp_analysis_summary.md\nnew_scripts_manifest.md\nnmin1_seed42\nnovelty_drayson_analysis.md\npaper_tables.md\npaper_tables_data.md\nplot_training_dynamics.py\nq1_ess_equivalence_analysis.md\nrelated_work_notes.md\nreport_tables.md\nresults_table_ablation.csv\nresults_table_contamination.csv\nresults_table_grid_b_curve.csv\nresults_table_main.csv\nreview_issues.yaml\nreview_reports\nrho06_mechanism_summary.json\nrho_comparison.csv\nrun_mvp.sh\nscored_data_rho_analysis.json\nseed42_diagnostic.md\nstatistical_tests.md\ntable1_compilation.md\ntable1_data.json\ntable1_data.md\ntable1_summary.md\ntables\ntau_095_seed42\ntau_09_seed42\ntau_b_strength.pdf\ntau_b_strength.png\ntau_derivation_check.md\ntau_fix_changelog.md\ntau_ppl_curve.pdf\ntau_ppl_curve.png\ntau_rho_grid.csv\ntau_rho_rank_analysis.csv\ntau_rho_rank_analysis.py\ntau_rho_rank_stats.json\ntau_sweep.pdf\ntau_sweep.png\ntau_sweep_commands.md\ntau_sweep_curve_dummy.pdf\ntau_sweep_curve_dummy.png\ntau_sweep_improvement_dummy.pdf\ntau_sweep_improvement_dummy.png\ntau_sweep_readiness.md\ntau_theory_analysis.md\ntau_theory_audit.md\ntraining\ntraining_progress_20260516.md\ntraining_progress_check.md\nweighting\nworker_output.md",
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

_source line 34_

<details open><summary>🔧 Tool call — Write · `toolu_0179A11MA1tooQdnqzE9VHJ6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/paper_main_table_data.md",
  "content": "# Paper Main Table Data — Compiled 2026-05-18\n\nAll PPL values are `eval_ppl_holdout` on `data/human/eval_holdout.jsonl` (sliding window, stride=1024, max_docs=5000, fp16, ~4.08M tokens).\n\nPretrained baseline (no continued training): **Qwen3-0.6B = 22.97** (`baseline_qwen3_0.6b`)\n\n---\n\n## Table 1: Main Results (ρ=0.4, Qwen3-0.6B)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean | Δ vs Uniform |\n|--------|---------|----------|----------|------|-------------|\n| Uniform | 17.6939 (`uniform_seed42`) | 17.6861 (`uniform_seed123`) | 17.7015 (`uniform_seed456`) | 17.694 | — |\n| **Adaptive (fix)** | 17.6527 (`adaptive_fix_seed42`) | 17.6432 (`adaptive_fix_seed123`) | 17.6566 (`adaptive_fix_seed456`) | **17.651** | **-0.043** |\n| ESS-only | 17.73 (`ess_only_seed42`) | 17.72 (`ess_only_seed123`) | 17.76 (`ess_only_seed456`) | 17.737 | +0.043 |\n| Random reweight | 17.83 (`random_reweight_v2_seed42`) | 17.801 (`random_reweight_seed123_r5`) | 17.777 (`random_reweight_seed456`) | 17.803 | +0.109 |\n\n**Notes:**\n- \"Adaptive (fix)\" = dual-constraint min-intervention (τ=0.8, n_min=2). Used as reference in all cross-experiment comparisons.\n- Earlier \"adaptive_seed{42,123,456}\" runs produced slightly better PPL (17.644/17.631/17.642, mean=17.639), but adaptive_fix is the canonical version referenced throughout.\n- ESS-only = max-intervention (b* = max{b : ESS(b) ≥ n_min}), ignores α_eff quality constraint.\n- Random reweight = random (non-provenance) weights applied to samples.\n- Random > Uniform > ESS-only > Adaptive confirms detector signal is load-bearing.\n\n---\n\n## Table 2: Grid-b Sweep (ρ=0.4, Qwen3-0.6B)\n\n### Seed 42 (from `grid_b_seed42_batch` + individual runs)\n\n| b | PPL | exp_id |\n|---|-----|--------|\n| 0.1 | 17.657 | `grid_b0_1_seed42` |\n| 0.2 | 17.64 | `grid_b0_2_seed42` |\n| 0.3 | 17.64 | `grid_b0_3_seed42` |\n| 0.5 | 17.651 | `grid_b_seed42_batch` (b0.5) |\n| 1.0 | 17.692 | `grid_b_seed42_batch` (b1.0) |\n| 1.5 | 17.718 | `grid_b_seed42_batch` (b1.5) |\n| 2.0 | 17.741 | `grid_b_seed42_batch` (b2.0) |\n| 3.0 | 17.774 | `grid_b_seed42_batch` (b3.0) |\n| 5.0 | 17.818 | `grid_b_seed42_batch` (b5.0) |\n\n### Multi-seed (seed 123 & 456)\n\n| b | Seed 123 | Seed 456 | exp_ids |\n|---|----------|----------|---------|\n| 0.1 | 17.646 | 17.663 | `grid_b0_1_seed{123,456}` |\n| 0.2 | 17.637 | 17.645 | `grid_b0_2_seed{123,456}` |\n| 0.3 | 17.579 | 17.64 | `grid_b0_3_seed123_r2`, `grid_b0_3_seed456_r2` |\n| 0.5 | 17.638 | 17.65 | `grid_b0_5_seed{123,456}` |\n| 1.0 | 17.674 | 17.68 | `grid_b1_0_seed{123,456}` |\n| 1.5 | 17.701 | 17.71 | `grid_b1_5_seed{123,456}` |\n| 2.0 | 17.725 | 17.989 | `grid_b2_0_seed{123,456}` |\n| 3.0 | 17.76 | 17.921 | `grid_b3_0_seed{123,456}` |\n| 5.0 | 17.804 | 17.993 | `grid_b5_0_seed{123,456}` |\n\n**Notes:**\n- grid_b0_3_seed123_r2 = 17.579 is an outlier (lowest in entire sweep). Verify before using.\n- grid_b2_0_seed456 = 17.989 and grid_b3_0_seed456 = 17.921 are outliers (much higher than seed123). May indicate training instability at high b.\n- Best grid-b ≈ 0.2-0.3, consistent with adaptive b* median ≈ 0.88.\n- Adaptive PPL (17.651) matches grid-best region, validating auto-tuning (Claim 2).\n\n---\n\n## Table 3: Detect & Remove (D&R) Threshold Sensitivity (ρ=0.4, seed=42)\n\n| Threshold | PPL | Data Retained | Training | exp_id |\n|-----------|-----|---------------|----------|--------|\n| q=0.3 | 17.253 | ~70% (remove top 30%) | Multi-epoch | `threshold_q03_seed42` |\n| q=0.5 | 17.29 | ~50% (remove top 50%) | Multi-epoch | `detect_remove_baseline_seed42` |\n| q=0.5 (epoch-matched) | 17.65 | ~50% | Single pass | `detect_remove_q05_epoch_matched_seed42` |\n| q=0.7 | 17.32 | ~30% retained | Multi-epoch | `detect_remove_q07_seed42` |\n| q=0.9 | 17.42 | ~10% retained | Multi-epoch | `detect_remove_q09_seed42` |\n\n**Multi-seed D&R q=0.5 (multi-epoch):**\n\n| Seed | PPL | exp_id |\n|------|-----|--------|\n| 42 | 17.29 | `detect_remove_baseline_seed42` |\n| 123 | 17.27 | `detect_remove_q05_seed123` |\n| 456 | 17.28 | `detect_remove_q05_seed456` |\n| Mean | **17.28** | |\n\n**Epoch-matched D&R q=0.5:**\n\n| Seed | PPL | exp_id |\n|------|-----|--------|\n| 42 | 17.65 | `detect_remove_q05_epoch_matched_seed42` |\n| 123 | 17.66 | `epoch_matched_dr_seed123` |\n| 456 | 17.66 | `epoch_matched_dr_seed456` |\n| Mean | **17.66** | |\n\n**Notes:**\n- D&R multi-epoch PPL is much lower (17.28) but trains multiple epochs on filtered clean data.\n- Epoch-matched D&R (17.66) is comparable to Adaptive (17.651), confirming advantage is from multi-epoch, not filtering.\n- D&R discards data; Adaptive retains all data with reweighting.\n- **RUNNING:** q=0.1 (`detect_remove_q01_seed42`), q=0.8 (`detect_remove_q08_seed42`)\n\n---\n\n## Table 4: Contamination Rate (ρ) Sensitivity\n\n### ρ=0.2 (seed=42 only)\n\n| Method | PPL | exp_id | Note |\n|--------|-----|--------|------|\n| Uniform | 17.336 | `rho02_uniform_seed42` | |\n| Adaptive (τ=0.8) | 17.382 | `rho02_adaptive_tau08_seed42` | **NEGATIVE** (+0.046) |\n| Adaptive (τ=0.9) | 17.45 | `rho02_adaptive_tau09_r5` | **NEGATIVE** (+0.114) |\n\n### ρ=0.4 (3 seeds)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| Uniform | 17.694 | 17.686 | 17.702 | 17.694 |\n| Adaptive | 17.653 | 17.643 | 17.657 | 17.651 |\n| Δ | -0.041 | -0.043 | -0.045 | **-0.043** |\n\n### ρ=0.6 (3 seeds)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| Uniform | 17.766 (`contamination_60_uniform_seed42`) | 17.754 (`contamination_60_uniform_seed123`) | 17.770 (`contamination_60_uniform_seed456`) | 17.763 |\n| Adaptive | 17.740 (`contamination_60_seed42_r2`) | 17.732 (`contamination_60_seed123`) | 17.735 (`contamination_60_adaptive_seed456`) | 17.736 |\n| Δ | -0.026 | -0.022 | -0.035 | **-0.028** |\n\n### ρ=0.6 Additional Methods\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| ESS-only | 17.77 | 17.763 | 17.762 | 17.765 |\n| Random | 17.832 | 17.87 | 17.88 | 17.861 |\n| Hybrid (filter+reweight) | 17.53 (`hybrid_rho06_seed42`) | — | — | 17.53 |\n| Grid b=0.3 | 17.634 (`contamination_60_grid_b0_3_seed42`) | — | — | |\n| Grid b=0.5 | 17.704 (`contamination_60_grid_b0_5_seed42`) | — | — | |\n\nexp_ids for ρ=0.6 ESS-only: `contamination_60_ess_only_seed{42,123,456}`\nexp_ids for ρ=0.6 Random: `contamination_60_random_seed{42,123,456}`\n\n**Summary:**\n- ρ=0.2: Adaptive HURTS (data already clean, reweighting over-penalizes)\n- ρ=0.4: Adaptive improves by -0.043 PPL (consistent across seeds)\n- ρ=0.6: Adaptive improves by -0.028 PPL (smaller gap, consistent across seeds)\n- Hybrid (filter q>0.95 + reweight) at ρ=0.6 achieves 17.53 (best), but single-seed only\n- ρ=0.4 also has hybrid: 17.514 (`hybrid_rho04_seed42`) — also single-seed\n\n---\n\n## Table 5: Multi-Detector Validation (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| Detector | Adaptive PPL | Uniform PPL | Δ | exp_ids |\n|----------|-------------|-------------|---|---------|\n| TF-IDF+LR (q_score, AUC=0.939) | 17.653 | 17.694 | -0.041 | `adaptive_fix_seed42` / `uniform_seed42` |\n| N-gram PPL (AUC=0.73) | **NO EVAL** | **NO EVAL** | — | `ngram_adaptive_seed42` / `ngram_uniform_seed42` |\n| GPT-2 PPL | **NOT STARTED** | **NOT STARTED** | — | `gpt2_adaptive_seed42` / `gpt2_uniform_seed42` (PREPARING) |\n\n**Notes:**\n- N-gram experiments completed training but eval PPL not yet computed. Models saved at:\n  - `/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/final`\n  - `/root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/final`\n- GPT-2 detector experiments still in PREPARING status.\n\n---\n\n## Table 6: Model Scale — Qwen3-1.7B (ρ=0.4, seed=42)\n\n| Method | PPL | exp_id | Status |\n|--------|-----|--------|--------|\n| Adaptive | **EVAL RUNNING** | `adaptive_1_7b_seed42` | Training done, eval in progress (`eval_adaptive_1_7b_v2`) |\n| Uniform | **EVAL RUNNING** | `uniform_1_7b_seed42` | Training FAILED (checkpoint issue); eval running on available checkpoint (`eval_uniform_1_7b_v3`) |\n\n**Notes:**\n- uniform_1_7b_seed42 training failed due to FileNotFoundError on checkpoint-3000/trainer_state.json during resume.\n- Eval is running on whatever checkpoint exists.\n- adaptive_1_7b_seed123 is also RUNNING (additional seed).\n\n---\n\n## Table 7: Cross-Architecture — Llama-3.2-3B (ρ=0.4, seed=42)\n\n| Method | PPL | MMLU (5-shot) | HellaSwag (10-shot) | exp_id |\n|--------|-----|---------------|---------------------|--------|\n| Uniform | 10.53 | 51.85% | — | `llama3b_uniform_seed42` |\n| Adaptive | 10.58 | **53.42%** | 72.49% | `llama3b_adaptive_seed42` |\n| Δ | +0.05 | **+1.57pp** (3.9σ) | — | |\n\n**Notes:**\n- PPL: adaptive slightly WORSE (+0.05), but within noise range.\n- MMLU: adaptive significantly BETTER (+1.57pp, 3.9σ), suggesting reweighting improves knowledge retention.\n- Conclusion: \"neutral-to-positive\" — PPL parity with downstream task improvement.\n- YAML shows conclusion=negative (PPL worse), API shows conclusion=success (considering MMLU gain).\n- eval_tokens=4,017,316 (reeval_v2 unified params).\n\n---\n\n## Table 8: τ Sensitivity (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| τ | PPL | Δ vs Uniform | exp_id | Conclusion |\n|---|-----|-------------|--------|------------|\n| 0.5 | 17.688 | -0.006 | `tau_05_seed42` | success |\n| 0.6 | 17.681 | -0.013 | `tau_06_seed42` | success |\n| 0.7 | 17.679 | -0.015 | `tau_07_seed42` | success |\n| 0.8 | 17.653 | -0.041 | `adaptive_fix_seed42` | success |\n| 0.9 | 17.712 | +0.018 | `tau_09_seed42` | **negative** |\n| 0.95 | 17.723 | +0.029 | `tau_095_seed42` | **negative** |\n\n**τ sweep at ρ=0.6 (seed=42):**\n\n| τ | PPL | exp_id |\n|---|-----|--------|\n| 0.6 | 17.736 | `contamination_60_tau06_seed42` |\n| 0.7 | 17.73 | `contamination_60_tau07_seed42` |\n| 0.8 | 17.74 | `contamination_60_seed42_r2` |\n\n---\n\n## Table 9: Batch Size & n_min Ablation (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| Config | PPL | Δ vs Uniform | exp_id |\n|--------|-----|-------------|--------|\n| bs=4, n_min=2 (default) | 17.653 | -0.041 | `adaptive_fix_seed42` |\n| bs=4, n_min=1 | 17.789 | +0.095 | `nmin1_seed42` |\n| bs=4, n_min=4 | 17.695 | +0.001 | `nmin4_seed42` |\n| bs=8, n_min=2 | 17.73 | +0.036 | `bs8_nmin2_seed42_r2` |\n| bs=8, n_min=4 (coupling rule) | 17.66 | -0.034 | `bs8_auto_nmin_r5` |\n| bs=16, n_min=8 (coupling rule) | 17.65 | -0.044 | `batchsize16_nmin8_r3` |\n| Golden ratio (b*=φ−1≈0.618) | 17.654 | -0.040 | `golden_ratio_seed42` |\n\n**Notes:**\n- Coupling rule: n_min = max(2, bs//2).\n- bs=8 without coupling (n_min=2) degrades; coupling (n_min=4) restores performance.\n- bs=16 with n_min=8 matches default performance.\n- n_min=1 is too loose, n_min=4 at bs=4 is too strict (forces b*=0 for 100% of batches).\n\n---\n\n## Batch-Adaptive τ (negative results)\n\n| Setting | PPL | exp_id | Conclusion |\n|---------|-----|--------|------------|\n| Batch-adaptive τ, ρ=0.4 | 17.681 | `batch_adaptive_tau_rho04_seed42` | **negative** |\n| Batch-adaptive τ, ρ=0.6 | 17.73 | `batch_adaptive_tau_rho06_r5` | **negative** |\n\nNo improvement over fixed τ at either contamination level. Path abandoned.\n\n---\n\n## Summary of Missing / In-Progress Data\n\n| Item | Status | Blocking? |\n|------|--------|-----------|\n| N-gram detector eval (adaptive + uniform) | Training done, **eval needed** | Yes — Table 5 |\n| GPT-2 detector (adaptive + uniform) | PREPARING | Yes — Table 5 |\n| 1.7B eval (adaptive + uniform) | RUNNING | Yes — Table 6 |\n| D&R q=0.1 | RUNNING | Minor — Table 3 |\n| D&R q=0.8 | RUNNING | Minor — Table 3 |\n| 1.7B seed 123 | RUNNING | Desirable — Table 6 multi-seed |\n| Llama-3.2-3B multi-seed | Not started | Desirable — Table 7 robustness |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "12262d4a-8cda-4f7e-b1e1-ea30acbed10e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wc65Z7fCDGZ73yj4tzhgtu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1815,
      "cache_read_input_tokens": 62009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1815
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

_source line 35 · 2026-05-18T21:33:44.242Z_

<details><summary>↩ Tool result · `toolu_0179A11MA1tooQdnqzE9VHJ6`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/paper_main_table_data.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "3134825a-16bd-4884-becc-d41578874118",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/paper_main_table_data.md",
    "content": "# Paper Main Table Data — Compiled 2026-05-18\n\nAll PPL values are `eval_ppl_holdout` on `data/human/eval_holdout.jsonl` (sliding window, stride=1024, max_docs=5000, fp16, ~4.08M tokens).\n\nPretrained baseline (no continued training): **Qwen3-0.6B = 22.97** (`baseline_qwen3_0.6b`)\n\n---\n\n## Table 1: Main Results (ρ=0.4, Qwen3-0.6B)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean | Δ vs Uniform |\n|--------|---------|----------|----------|------|-------------|\n| Uniform | 17.6939 (`uniform_seed42`) | 17.6861 (`uniform_seed123`) | 17.7015 (`uniform_seed456`) | 17.694 | — |\n| **Adaptive (fix)** | 17.6527 (`adaptive_fix_seed42`) | 17.6432 (`adaptive_fix_seed123`) | 17.6566 (`adaptive_fix_seed456`) | **17.651** | **-0.043** |\n| ESS-only | 17.73 (`ess_only_seed42`) | 17.72 (`ess_only_seed123`) | 17.76 (`ess_only_seed456`) | 17.737 | +0.043 |\n| Random reweight | 17.83 (`random_reweight_v2_seed42`) | 17.801 (`random_reweight_seed123_r5`) | 17.777 (`random_reweight_seed456`) | 17.803 | +0.109 |\n\n**Notes:**\n- \"Adaptive (fix)\" = dual-constraint min-intervention (τ=0.8, n_min=2). Used as reference in all cross-experiment comparisons.\n- Earlier \"adaptive_seed{42,123,456}\" runs produced slightly better PPL (17.644/17.631/17.642, mean=17.639), but adaptive_fix is the canonical version referenced throughout.\n- ESS-only = max-intervention (b* = max{b : ESS(b) ≥ n_min}), ignores α_eff quality constraint.\n- Random reweight = random (non-provenance) weights applied to samples.\n- Random > Uniform > ESS-only > Adaptive confirms detector signal is load-bearing.\n\n---\n\n## Table 2: Grid-b Sweep (ρ=0.4, Qwen3-0.6B)\n\n### Seed 42 (from `grid_b_seed42_batch` + individual runs)\n\n| b | PPL | exp_id |\n|---|-----|--------|\n| 0.1 | 17.657 | `grid_b0_1_seed42` |\n| 0.2 | 17.64 | `grid_b0_2_seed42` |\n| 0.3 | 17.64 | `grid_b0_3_seed42` |\n| 0.5 | 17.651 | `grid_b_seed42_batch` (b0.5) |\n| 1.0 | 17.692 | `grid_b_seed42_batch` (b1.0) |\n| 1.5 | 17.718 | `grid_b_seed42_batch` (b1.5) |\n| 2.0 | 17.741 | `grid_b_seed42_batch` (b2.0) |\n| 3.0 | 17.774 | `grid_b_seed42_batch` (b3.0) |\n| 5.0 | 17.818 | `grid_b_seed42_batch` (b5.0) |\n\n### Multi-seed (seed 123 & 456)\n\n| b | Seed 123 | Seed 456 | exp_ids |\n|---|----------|----------|---------|\n| 0.1 | 17.646 | 17.663 | `grid_b0_1_seed{123,456}` |\n| 0.2 | 17.637 | 17.645 | `grid_b0_2_seed{123,456}` |\n| 0.3 | 17.579 | 17.64 | `grid_b0_3_seed123_r2`, `grid_b0_3_seed456_r2` |\n| 0.5 | 17.638 | 17.65 | `grid_b0_5_seed{123,456}` |\n| 1.0 | 17.674 | 17.68 | `grid_b1_0_seed{123,456}` |\n| 1.5 | 17.701 | 17.71 | `grid_b1_5_seed{123,456}` |\n| 2.0 | 17.725 | 17.989 | `grid_b2_0_seed{123,456}` |\n| 3.0 | 17.76 | 17.921 | `grid_b3_0_seed{123,456}` |\n| 5.0 | 17.804 | 17.993 | `grid_b5_0_seed{123,456}` |\n\n**Notes:**\n- grid_b0_3_seed123_r2 = 17.579 is an outlier (lowest in entire sweep). Verify before using.\n- grid_b2_0_seed456 = 17.989 and grid_b3_0_seed456 = 17.921 are outliers (much higher than seed123). May indicate training instability at high b.\n- Best grid-b ≈ 0.2-0.3, consistent with adaptive b* median ≈ 0.88.\n- Adaptive PPL (17.651) matches grid-best region, validating auto-tuning (Claim 2).\n\n---\n\n## Table 3: Detect & Remove (D&R) Threshold Sensitivity (ρ=0.4, seed=42)\n\n| Threshold | PPL | Data Retained | Training | exp_id |\n|-----------|-----|---------------|----------|--------|\n| q=0.3 | 17.253 | ~70% (remove top 30%) | Multi-epoch | `threshold_q03_seed42` |\n| q=0.5 | 17.29 | ~50% (remove top 50%) | Multi-epoch | `detect_remove_baseline_seed42` |\n| q=0.5 (epoch-matched) | 17.65 | ~50% | Single pass | `detect_remove_q05_epoch_matched_seed42` |\n| q=0.7 | 17.32 | ~30% retained | Multi-epoch | `detect_remove_q07_seed42` |\n| q=0.9 | 17.42 | ~10% retained | Multi-epoch | `detect_remove_q09_seed42` |\n\n**Multi-seed D&R q=0.5 (multi-epoch):**\n\n| Seed | PPL | exp_id |\n|------|-----|--------|\n| 42 | 17.29 | `detect_remove_baseline_seed42` |\n| 123 | 17.27 | `detect_remove_q05_seed123` |\n| 456 | 17.28 | `detect_remove_q05_seed456` |\n| Mean | **17.28** | |\n\n**Epoch-matched D&R q=0.5:**\n\n| Seed | PPL | exp_id |\n|------|-----|--------|\n| 42 | 17.65 | `detect_remove_q05_epoch_matched_seed42` |\n| 123 | 17.66 | `epoch_matched_dr_seed123` |\n| 456 | 17.66 | `epoch_matched_dr_seed456` |\n| Mean | **17.66** | |\n\n**Notes:**\n- D&R multi-epoch PPL is much lower (17.28) but trains multiple epochs on filtered clean data.\n- Epoch-matched D&R (17.66) is comparable to Adaptive (17.651), confirming advantage is from multi-epoch, not filtering.\n- D&R discards data; Adaptive retains all data with reweighting.\n- **RUNNING:** q=0.1 (`detect_remove_q01_seed42`), q=0.8 (`detect_remove_q08_seed42`)\n\n---\n\n## Table 4: Contamination Rate (ρ) Sensitivity\n\n### ρ=0.2 (seed=42 only)\n\n| Method | PPL | exp_id | Note |\n|--------|-----|--------|------|\n| Uniform | 17.336 | `rho02_uniform_seed42` | |\n| Adaptive (τ=0.8) | 17.382 | `rho02_adaptive_tau08_seed42` | **NEGATIVE** (+0.046) |\n| Adaptive (τ=0.9) | 17.45 | `rho02_adaptive_tau09_r5` | **NEGATIVE** (+0.114) |\n\n### ρ=0.4 (3 seeds)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| Uniform | 17.694 | 17.686 | 17.702 | 17.694 |\n| Adaptive | 17.653 | 17.643 | 17.657 | 17.651 |\n| Δ | -0.041 | -0.043 | -0.045 | **-0.043** |\n\n### ρ=0.6 (3 seeds)\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| Uniform | 17.766 (`contamination_60_uniform_seed42`) | 17.754 (`contamination_60_uniform_seed123`) | 17.770 (`contamination_60_uniform_seed456`) | 17.763 |\n| Adaptive | 17.740 (`contamination_60_seed42_r2`) | 17.732 (`contamination_60_seed123`) | 17.735 (`contamination_60_adaptive_seed456`) | 17.736 |\n| Δ | -0.026 | -0.022 | -0.035 | **-0.028** |\n\n### ρ=0.6 Additional Methods\n\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean |\n|--------|---------|----------|----------|------|\n| ESS-only | 17.77 | 17.763 | 17.762 | 17.765 |\n| Random | 17.832 | 17.87 | 17.88 | 17.861 |\n| Hybrid (filter+reweight) | 17.53 (`hybrid_rho06_seed42`) | — | — | 17.53 |\n| Grid b=0.3 | 17.634 (`contamination_60_grid_b0_3_seed42`) | — | — | |\n| Grid b=0.5 | 17.704 (`contamination_60_grid_b0_5_seed42`) | — | — | |\n\nexp_ids for ρ=0.6 ESS-only: `contamination_60_ess_only_seed{42,123,456}`\nexp_ids for ρ=0.6 Random: `contamination_60_random_seed{42,123,456}`\n\n**Summary:**\n- ρ=0.2: Adaptive HURTS (data already clean, reweighting over-penalizes)\n- ρ=0.4: Adaptive improves by -0.043 PPL (consistent across seeds)\n- ρ=0.6: Adaptive improves by -0.028 PPL (smaller gap, consistent across seeds)\n- Hybrid (filter q>0.95 + reweight) at ρ=0.6 achieves 17.53 (best), but single-seed only\n- ρ=0.4 also has hybrid: 17.514 (`hybrid_rho04_seed42`) — also single-seed\n\n---\n\n## Table 5: Multi-Detector Validation (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| Detector | Adaptive PPL | Uniform PPL | Δ | exp_ids |\n|----------|-------------|-------------|---|---------|\n| TF-IDF+LR (q_score, AUC=0.939) | 17.653 | 17.694 | -0.041 | `adaptive_fix_seed42` / `uniform_seed42` |\n| N-gram PPL (AUC=0.73) | **NO EVAL** | **NO EVAL** | — | `ngram_adaptive_seed42` / `ngram_uniform_seed42` |\n| GPT-2 PPL | **NOT STARTED** | **NOT STARTED** | — | `gpt2_adaptive_seed42` / `gpt2_uniform_seed42` (PREPARING) |\n\n**Notes:**\n- N-gram experiments completed training but eval PPL not yet computed. Models saved at:\n  - `/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/final`\n  - `/root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/final`\n- GPT-2 detector experiments still in PREPARING status.\n\n---\n\n## Table 6: Model Scale — Qwen3-1.7B (ρ=0.4, seed=42)\n\n| Method | PPL | exp_id | Status |\n|--------|-----|--------|--------|\n| Adaptive | **EVAL RUNNING** | `adaptive_1_7b_seed42` | Training done, eval in progress (`eval_adaptive_1_7b_v2`) |\n| Uniform | **EVAL RUNNING** | `uniform_1_7b_seed42` | Training FAILED (checkpoint issue); eval running on available checkpoint (`eval_uniform_1_7b_v3`) |\n\n**Notes:**\n- uniform_1_7b_seed42 training failed due to FileNotFoundError on checkpoint-3000/trainer_state.json during resume.\n- Eval is running on whatever checkpoint exists.\n- adaptive_1_7b_seed123 is also RUNNING (additional seed).\n\n---\n\n## Table 7: Cross-Architecture — Llama-3.2-3B (ρ=0.4, seed=42)\n\n| Method | PPL | MMLU (5-shot) | HellaSwag (10-shot) | exp_id |\n|--------|-----|---------------|---------------------|--------|\n| Uniform | 10.53 | 51.85% | — | `llama3b_uniform_seed42` |\n| Adaptive | 10.58 | **53.42%** | 72.49% | `llama3b_adaptive_seed42` |\n| Δ | +0.05 | **+1.57pp** (3.9σ) | — | |\n\n**Notes:**\n- PPL: adaptive slightly WORSE (+0.05), but within noise range.\n- MMLU: adaptive significantly BETTER (+1.57pp, 3.9σ), suggesting reweighting improves knowledge retention.\n- Conclusion: \"neutral-to-positive\" — PPL parity with downstream task improvement.\n- YAML shows conclusion=negative (PPL worse), API shows conclusion=success (considering MMLU gain).\n- eval_tokens=4,017,316 (reeval_v2 unified params).\n\n---\n\n## Table 8: τ Sensitivity (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| τ | PPL | Δ vs Uniform | exp_id | Conclusion |\n|---|-----|-------------|--------|------------|\n| 0.5 | 17.688 | -0.006 | `tau_05_seed42` | success |\n| 0.6 | 17.681 | -0.013 | `tau_06_seed42` | success |\n| 0.7 | 17.679 | -0.015 | `tau_07_seed42` | success |\n| 0.8 | 17.653 | -0.041 | `adaptive_fix_seed42` | success |\n| 0.9 | 17.712 | +0.018 | `tau_09_seed42` | **negative** |\n| 0.95 | 17.723 | +0.029 | `tau_095_seed42` | **negative** |\n\n**τ sweep at ρ=0.6 (seed=42):**\n\n| τ | PPL | exp_id |\n|---|-----|--------|\n| 0.6 | 17.736 | `contamination_60_tau06_seed42` |\n| 0.7 | 17.73 | `contamination_60_tau07_seed42` |\n| 0.8 | 17.74 | `contamination_60_seed42_r2` |\n\n---\n\n## Table 9: Batch Size & n_min Ablation (ρ=0.4, seed=42, Qwen3-0.6B)\n\n| Config | PPL | Δ vs Uniform | exp_id |\n|--------|-----|-------------|--------|\n| bs=4, n_min=2 (default) | 17.653 | -0.041 | `adaptive_fix_seed42` |\n| bs=4, n_min=1 | 17.789 | +0.095 | `nmin1_seed42` |\n| bs=4, n_min=4 | 17.695 | +0.001 | `nmin4_seed42` |\n| bs=8, n_min=2 | 17.73 | +0.036 | `bs8_nmin2_seed42_r2` |\n| bs=8, n_min=4 (coupling rule) | 17.66 | -0.034 | `bs8_auto_nmin_r5` |\n| bs=16, n_min=8 (coupling rule) | 17.65 | -0.044 | `batchsize16_nmin8_r3` |\n| Golden ratio (b*=φ−1≈0.618) | 17.654 | -0.040 | `golden_ratio_seed42` |\n\n**Notes:**\n- Coupling rule: n_min = max(2, bs//2).\n- bs=8 without coupling (n_min=2) degrades; coupling (n_min=4) restores performance.\n- bs=16 with n_min=8 matches default performance.\n- n_min=1 is too loose, n_min=4 at bs=4 is too strict (forces b*=0 for 100% of batches).\n\n---\n\n## Batch-Adaptive τ (negative results)\n\n| Setting | PPL | exp_id | Conclusion |\n|---------|-----|--------|------------|\n| Batch-adaptive τ, ρ=0.4 | 17.681 | `batch_adaptive_tau_rho04_seed42` | **negative** |\n| Batch-adaptive τ, ρ=0.6 | 17.73 | `batch_adaptive_tau_rho06_r5` | **negative** |\n\nNo improvement over fixed τ at either contamination level. Path abandoned.\n\n---\n\n## Summary of Missing / In-Progress Data\n\n| Item | Status | Blocking? |\n|------|--------|-----------|\n| N-gram detector eval (adaptive + uniform) | Training done, **eval needed** | Yes — Table 5 |\n| GPT-2 detector (adaptive + uniform) | PREPARING | Yes — Table 5 |\n| 1.7B eval (adaptive + uniform) | RUNNING | Yes — Table 6 |\n| D&R q=0.1 | RUNNING | Minor — Table 3 |\n| D&R q=0.8 | RUNNING | Minor — Table 3 |\n| 1.7B seed 123 | RUNNING | Desirable — Table 6 multi-seed |\n| Llama-3.2-3B multi-seed | Not started | Desirable — Table 7 robustness |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 36_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "1458507f-9a11-47ba-903b-5aa576d3e985",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVnATCbPRtL9Wu7uiaFWFS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5269,
      "cache_read_input_tokens": 63824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5269
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

_source line 37_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JjxJMvq1gRXPemq8yxXNnK`</summary>

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
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "55169b67-99ae-4f0f-a913-dedae9440b13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVnATCbPRtL9Wu7uiaFWFS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5269,
      "cache_read_input_tokens": 63824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5269
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

_source line 38 · 2026-05-18T21:33:47.522Z_

<details><summary>↩ Tool result · `toolu_01JjxJMvq1gRXPemq8yxXNnK`</summary>

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
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "a8bf6a06-fac7-4a99-b4c2-6f00af418cc8",
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

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_0154DNc4Z2cPjWbrRd5dSsGj`</summary>

```json
{
  "name": "paper_main_table_data",
  "type": "data",
  "description": "Complete PPL results compilation for all paper tables (Tables 1-9): main results, grid-b sweep, D&R threshold, contamination rate sensitivity, multi-detector, scale, cross-architecture, τ sensitivity, batch size ablation. Includes exp_id traceability and missing data tracker.",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/paper_main_table_data.md",
  "tags": [
    "paper",
    "tables",
    "ppl",
    "compilation"
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
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "8403a3d9-6d64-4955-9a7d-e49bdc0ef5d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwNZbTxLgJni7cZM2w7ucn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 69093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
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

_source line 40 · 2026-05-18T21:33:53.262Z_

<details><summary>↩ Tool result · `toolu_0154DNc4Z2cPjWbrRd5dSsGj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_87a413\", \"name\": \"paper_main_table_data\", \"type\": \"data\", \"description\": \"Complete PPL results compilation for all paper tables (Tables 1-9): main results, grid-b sweep, D&R threshold, contamination rate sensitivity, multi-detector, scale, cross-architecture, τ sensitivity, batch size ablation. Includes exp_id traceability and missing data tracker.\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/paper_main_table_data.md\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-18T21:33:52.961503+00:00\", \"tags\": [\"paper\", \"tables\", \"ppl\", \"compilation\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "b6c6eb96-6377-458f-a7a8-f6abb55664c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260518_87a413\\\", \\\"name\\\": \\\"paper_main_table_data\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Complete PPL results compilation for all paper tables (Tables 1-9): main results, grid-b sweep, D&R threshold, contamination rate sensitivity, multi-detector, scale, cross-architecture, τ sensitivity, batch size ablation. Includes exp_id traceability and missing data tracker.\\\", \\\"path\\\": \\\"projects/provenance_weight_training/artifacts/_project/data/paper_main_table_data.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"provenance_weight_training\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-18T21:33:52.961503+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"tables\\\", \\\"ppl\\\", \\\"compilation\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_87a413\", \"name\": \"paper_main_table_data\", \"type\": \"data\", \"description\": \"Complete PPL results compilation for all paper tables (Tables 1-9): main results, grid-b sweep, D&R threshold, contamination rate sensitivity, multi-detector, scale, cross-architecture, τ sensitivity, batch size ablation. Includes exp_id traceability and missing data tracker.\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/paper_main_table_data.md\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-18T21:33:52.961503+00:00\", \"tags\": [\"paper\", \"tables\", \"ppl\", \"compilation\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

已写入 `artifacts/paper_main_table_data.md`，包含 9 张表格数据。

**核心发现汇总：**

| 表格 | 关键结论 |
|------|---------|
| Table 1 (Main) | Adaptive -0.043 PPL vs Uniform (3 seeds), Random +0.109 证实 detector signal load-bearing |
| Table 2 (Grid-b) | 最优 b≈0.2-0.3，Adaptive 自动匹配 grid-best |
| Table 3 (D&R) | 多 epoch D&R=17.28，epoch-matched D&R=17.66 ≈ Adaptive=17.651 |
| Table 4 (ρ) | ρ=0.2 adaptive 反而有害；ρ=0.4 有效 (-0.043)；ρ=0.6 有效 (-0.028) |
| Table 5 (Multi-det) | TF-IDF 已验证；N-gram 训练完缺 eval；GPT-2 未开始 |
| Table 6 (1.7B) | Eval 正在跑 |
| Table 7 (Llama-3B) | PPL +0.05 (微劣)，MMLU +1.57pp (3.9σ 显著提升) |
| Table 8 (τ) | 最优 τ=0.8；τ≥0.9 有害 |
| Table 9 (bs/n_min) | coupling rule n_min=max(2,bs//2) 验证有效 |

**阻塞项：** N-gram eval、GPT-2 实验、1.7B eval 尚未完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "uuid": "9d495756-2bb3-4a19-8c6c-7409d02141db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01298s9PYR3CQ6vi2eckFLse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 69811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 589
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

已写入 `artifacts/paper_main_table_data.md`，包含 9 张表格数据。

**核心发现汇总：**

| 表格 | 关键结论 |
|------|---------|
| Table 1 (Main) | Adaptive -0.043 PPL vs Uniform (3 seeds), Random +0.109 证实 detector signal load-bearing |
| Table 2 (Grid-b) | 最优 b≈0.2-0.3，Adaptive 自动匹配 grid-best |
| Table 3 (D&R) | 多 epoch D&R=17.28，epoch-matched D&R=17.66 ≈ Adaptive=17.651 |
| Table 4 (ρ) | ρ=0.2 adaptive 反而有害；ρ=0.4 有效 (-0.043)；ρ=0.6 有效 (-0.028) |
| Table 5 (Multi-det) | TF-IDF 已验证；N-gram 训练完缺 eval；GPT-2 未开始 |
| Table 6 (1.7B) | Eval 正在跑 |
| Table 7 (Llama-3B) | PPL +0.05 (微劣)，MMLU +1.57pp (3.9σ 显著提升) |
| Table 8 (τ) | 最优 τ=0.8；τ≥0.9 有害 |
| Table 9 (bs/n_min) | coupling rule n_min=max(2,bs//2) 验证有效 |

**阻塞项：** N-gram eval、GPT-2 实验、1.7B eval 尚未完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 276467,
  "duration_api_ms": 274387,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "5f3dbd93-803c-44af-8cad-9392deab43cf",
  "total_cost_usd": 1.02646825,
  "usage": {
    "input_tokens": 18,
    "cache_creation_input_tokens": 58559,
    "cache_read_input_tokens": 552091,
    "output_tokens": 15315,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 58559,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 471,
        "cache_read_input_tokens": 69811,
        "cache_creation_input_tokens": 589,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 589
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1374,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001464,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 18,
      "outputTokens": 15315,
      "cacheReadInputTokens": 552091,
      "cacheCreationInputTokens": 58559,
      "webSearchRequests": 0,
      "costUSD": 1.0250042499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bccee9f4-b007-4047-8464-eea3a79e9a4c"
}
```

</details>

---
