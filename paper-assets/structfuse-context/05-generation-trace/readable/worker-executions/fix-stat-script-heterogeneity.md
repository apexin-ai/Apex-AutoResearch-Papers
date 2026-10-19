# fix stat script heterogeneity

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_fix_stat-script-heterogeneity_20260515T011849.log`
- **Structured JSON:** [`8d90447806b34bd318e3.json`](../../sessions/8d/8d90447806b34bd318e3.json)

## Before a recorded user message

18 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "9f8c7e65-1c7b-40c2-b2b4-05d152d53ddd",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
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
    "resetsAt": 1778825400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "041bade4-facb-42a9-859d-1ef0efc48ccb",
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current HETEROGENEITY_NOTES section from the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "ccf7d9a1-e63e-4290-a64b-2f4390ee13b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtQsonC15L8dBctDPneHq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11630,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11630
      },
      "output_tokens": 36,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FaRPkq8936dg4n2fk4ZU3H`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "30ddd3f7-5647-4754-aba0-62d6f7433672",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtQsonC15L8dBctDPneHq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11630,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11630
      },
      "output_tokens": 36,
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

_source line 6 · 2026-05-15T01:19:02.221Z_

<details><summary>↩ Tool result · `toolu_01FaRPkq8936dg4n2fk4ZU3H`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "30cdc19f-22d2-4e4a-b474-a0a1048d2c71",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CFtkfcSfUuCFAm6ZTuQonn`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n -A 20 \"HETEROGENEITY_NOTES\" /root/structfuse/scripts/m2_statistical_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "2f274c0b-dcd6-4cb7-a5cc-d2ea2f7c1119",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4y7z8YDsisp8uaNzMjURz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 23077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 705
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

_source line 8 · 2026-05-15T01:19:06.424Z_

<details><summary>↩ Tool result · `toolu_01CFtkfcSfUuCFAm6ZTuQonn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"31:HETEROGENEITY_NOTES = {\\n32-    (\\\"starcoder\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n33-    (\\\"starcoder\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n34-    (\\\"starcoder\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n35-}\\n36-\\n37-\\n38-def _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\\n39-    \\\"\\\"\\\"Return candidate directories to search for a run's output.\\\"\\\"\\\"\\n40-    enc_short = {\\\"qwen\\\": \\\"qwen\\\", \\\"starcoder\\\": \\\"starcoder\\\"}[encoder]\\n41-    enc_full = {\\\"qwen\\\": \\\"m2_full_qwen\\\", \\\"starcoder\\\": \\\"m2_full_starcoder\\\"}[encoder]\\n42-    tag = f\\\"{strategy}_s{seed}\\\"\\n43-    tag_enc = f\\\"{strategy}_{enc_short}_s{seed}\\\"\\n44-    return [\\n45-        f\\\"{OUTPUT_BASE}/{tag}\\\",\\n46-        f\\\"{OUTPUT_BASE}/{tag_enc}\\\",\\n47-        f\\\"{CHECKPOINT_BASE}/{enc_full}/{tag}\\\",\\n48-    ]\\n49-\\n50-\\n51-def _parse_best_r1_from_log(log_path: str) -> Optional[float]:\\n--\\n115:                    note = HETEROGENEITY_NOTES.get((encoder, strategy, seed), \\\"\\\")\\n116-                    results[(encoder, strategy, seed)] = {\\n117-                        \\\"best_r1\\\": r1,\\n118-                        \\\"source\\\": \\\"mock\\\",\\n119-                        \\\"note\\\": f\\\"[DRY-RUN mock] {note}\\\" if note else \\\"[DRY-RUN mock]\\\",\\n120-                        \\\"all_evals\\\": [],\\n121-                    }\\n122-        return results\\n123-\\n124-    for encoder in ENCODERS:\\n125-        for strategy in STRATEGIES:\\n126-            for seed in SEEDS:\\n127-                key = (encoder, strategy, seed)\\n128:                note = HETEROGENEITY_NOTES.get(key, \\\"\\\")\\n129-                candidates = _candidate_dirs(encoder, strategy, seed)\\n130-                found = False\\n131-\\n132-                for cdir in candidates:\\n133-                    log_path = os.path.join(cdir, \\\"train.log\\\")\\n134-                    best_ckpt = os.path.join(cdir, \\\"best_by_recall_at_1\\\")\\n135-\\n136-                    if os.path.isfile(log_path):\\n137-                        best_r1 = _parse_best_r1_from_log(log_path)\\n138-                        all_evals = _parse_eval_metrics_from_log(log_path)\\n139-                        final = _parse_final_eval(log_path)\\n140-\\n141-                        if best_r1 is None and all_evals:\\n142-                            best_r1 = max(e.get(\\\"recall@1\\\", 0) for e in all_evals)\\n143-                        if best_r1 is None and final:\\n144-                            best_r1 = final.get(\\\"recall@1\\\")\\n145-\\n146-                        results[key] = {\\n147-                            \\\"best_r1\\\": best_r1,\\n148-                            \\\"source\\\": log_path,\\n--\\n253:                    n = HETEROGENEITY_NOTES.get((encoder, s, seed))\\n254-                    if n:\\n255-                        het_notes.append(f\\\"{encoder}/{s}/s{seed}: {n}\\\")\\n256-\\n257-            comparisons[label] = {\\n258-                \\\"status\\\": \\\"OK\\\",\\n259-                \\\"encoder\\\": encoder,\\n260-                \\\"treatment\\\": treat_strategy,\\n261-                \\\"control\\\": \\\"random\\\",\\n262-                \\\"n_pairs\\\": n_pairs,\\n263-                \\\"valid_seeds\\\": valid_seeds,\\n264-                \\\"treatment_values\\\": treat_vals,\\n265-                \\\"control_values\\\": ctrl_vals,\\n266-                \\\"treatment_mean\\\": float(treat_arr.mean()),\\n267-                \\\"treatment_std\\\": float(treat_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\n268-                \\\"control_mean\\\": float(ctrl_arr.mean()),\\n269-                \\\"control_std\\\": float(ctrl_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\n270-                \\\"mean_diff\\\": mean_diff,\\n271-                \\\"paired_ttest\\\": {\\\"t_statistic\\\": float(t_stat), \\\"p_value\\\": float(t_pval)},\\n272-                \\\"wilcoxon\\\": {\\\"w_statistic\\\": float(w_stat), \\\"p_value\\\": float(w_pval)},\\n273-                \\\"bootstrap_95ci\\\": {\\\"lower\\\": ci_lo, \\\"upper\\\": ci_hi},\\n--\\n435:        flag = \\\" *\\\" if (enc, strat, seed) in HETEROGENEITY_NOTES else \\\"\\\"\\n436-        print(f\\\"  {enc:12s} {strat:22s} s{seed}: R@1={r1_str}{flag}\\\")\\n437-\\n438-    # 2. Per-condition summary\\n439-    print()\\n440-    print(\\\"=\\\" * 60)\\n441-    print(\\\"Phase 2: Per-condition summary\\\")\\n442-    print(\\\"=\\\" * 60)\\n443-    summary = per_condition_summary(metrics)\\n444-    for s in summary:\\n445-        if s[\\\"mean\\\"] is not None:\\n446-            print(f\\\"  {s['encoder']:12s} {s['strategy']:22s}: {s['mean']:.4f} +/- {s['std']:.4f} (n={s['n']})\\\")\\n447-        else:\\n448-            print(f\\\"  {s['encoder']:12s} {s['strategy']:22s}: NO DATA\\\")\\n449-\\n450-    # 3. Statistical comparisons\\n451-    print()\\n452-    print(\\\"=\\\" * 60)\\n453-    print(\\\"Phase 3: Statistical comparisons\\\")\\n454-    print(\\\"=\\\" * 60)\\n455-    comparisons = run_comparisons(metrics)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.02}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "48797201-3fc0-493e-8ac4-f18e5fc935f1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"31:HETEROGENEITY_NOTES = {\\\\n32-    (\\\\\\\"starcoder\\\\\\\", \\\\\\\"random\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n33-    (\\\\\\\"starcoder\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n34-    (\\\\\\\"starcoder\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n35-}\\\\n36-\\\\n37-\\\\n38-def _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\\\\n39-    \\\\\\\"\\\\\\\"\\\\\\\"Return candidate directories to search for a run's output.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n40-    enc_short = {\\\\\\\"qwen\\\\\\\": \\\\\\\"qwen\\\\\\\", \\\\\\\"starcoder\\\\\\\": \\\\\\\"starcoder\\\\\\\"}[encoder]\\\\n41-    enc_full = {\\\\\\\"qwen\\\\\\\": \\\\\\\"m2_full_qwen\\\\\\\", \\\\\\\"starcoder\\\\\\\": \\\\\\\"m2_full_starcoder\\\\\\\"}[encoder]\\\\n42-    tag = f\\\\\\\"{strategy}_s{seed}\\\\\\\"\\\\n43-    tag_enc = f\\\\\\\"{strategy}_{enc_short}_s{seed}\\\\\\\"\\\\n44-    return [\\\\n45-        f\\\\\\\"{OUTPUT_BASE}/{tag}\\\\\\\",\\\\n46-        f\\\\\\\"{OUTPUT_BASE}/{tag_enc}\\\\\\\",\\\\n47-        f\\\\\\\"{CHECKPOINT_BASE}/{enc_full}/{tag}\\\\\\\",\\\\n48-    ]\\\\n49-\\\\n50-\\\\n51-def _parse_best_r1_from_log(log_path: str) -> Optional[float]:\\\\n--\\\\n115:                    note = HETEROGENEITY_NOTES.get((encoder, strategy, seed), \\\\\\\"\\\\\\\")\\\\n116-                    results[(encoder, strategy, seed)] = {\\\\n117-                        \\\\\\\"best_r1\\\\\\\": r1,\\\\n118-                        \\\\\\\"source\\\\\\\": \\\\\\\"mock\\\\\\\",\\\\n119-                        \\\\\\\"note\\\\\\\": f\\\\\\\"[DRY-RUN mock] {note}\\\\\\\" if note else \\\\\\\"[DRY-RUN mock]\\\\\\\",\\\\n120-                        \\\\\\\"all_evals\\\\\\\": [],\\\\n121-                    }\\\\n122-        return results\\\\n123-\\\\n124-    for encoder in ENCODERS:\\\\n125-        for strategy in STRATEGIES:\\\\n126-            for seed in SEEDS:\\\\n127-                key = (encoder, strategy, seed)\\\\n128:                note = HETEROGENEITY_NOTES.get(key, \\\\\\\"\\\\\\\")\\\\n129-                candidates = _candidate_dirs(encoder, strategy, seed)\\\\n130-                found = False\\\\n131-\\\\n132-                for cdir in candidates:\\\\n133-                    log_path = os.path.join(cdir, \\\\\\\"train.log\\\\\\\")\\\\n134-                    best_ckpt = os.path.join(cdir, \\\\\\\"best_by_recall_at_1\\\\\\\")\\\\n135-\\\\n136-                    if os.path.isfile(log_path):\\\\n137-                        best_r1 = _parse_best_r1_from_log(log_path)\\\\n138-                        all_evals = _parse_eval_metrics_from_log(log_path)\\\\n139-                        final = _parse_final_eval(log_path)\\\\n140-\\\\n141-                        if best_r1 is None and all_evals:\\\\n142-                            best_r1 = max(e.get(\\\\\\\"recall@1\\\\\\\", 0) for e in all_evals)\\\\n143-                        if best_r1 is None and final:\\\\n144-                            best_r1 = final.get(\\\\\\\"recall@1\\\\\\\")\\\\n145-\\\\n146-                        results[key] = {\\\\n147-                            \\\\\\\"best_r1\\\\\\\": best_r1,\\\\n148-                            \\\\\\\"source\\\\\\\": log_path,\\\\n--\\\\n253:                    n = HETEROGENEITY_NOTES.get((encoder, s, seed))\\\\n254-                    if n:\\\\n255-                        het_notes.append(f\\\\\\\"{encoder}/{s}/s{seed}: {n}\\\\\\\")\\\\n256-\\\\n257-            comparisons[label] = {\\\\n258-                \\\\\\\"status\\\\\\\": \\\\\\\"OK\\\\\\\",\\\\n259-                \\\\\\\"encoder\\\\\\\": encoder,\\\\n260-                \\\\\\\"treatment\\\\\\\": treat_strategy,\\\\n261-                \\\\\\\"control\\\\\\\": \\\\\\\"random\\\\\\\",\\\\n262-                \\\\\\\"n_pairs\\\\\\\": n_pairs,\\\\n263-                \\\\\\\"valid_seeds\\\\\\\": valid_seeds,\\\\n264-                \\\\\\\"treatment_values\\\\\\\": treat_vals,\\\\n265-                \\\\\\\"control_values\\\\\\\": ctrl_vals,\\\\n266-                \\\\\\\"treatment_mean\\\\\\\": float(treat_arr.mean()),\\\\n267-                \\\\\\\"treatment_std\\\\\\\": float(treat_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\\\n268-                \\\\\\\"control_mean\\\\\\\": float(ctrl_arr.mean()),\\\\n269-                \\\\\\\"control_std\\\\\\\": float(ctrl_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\\\n270-                \\\\\\\"mean_diff\\\\\\\": mean_diff,\\\\n271-                \\\\\\\"paired_ttest\\\\\\\": {\\\\\\\"t_statistic\\\\\\\": float(t_stat), \\\\\\\"p_value\\\\\\\": float(t_pval)},\\\\n272-                \\\\\\\"wilcoxon\\\\\\\": {\\\\\\\"w_statistic\\\\\\\": float(w_stat), \\\\\\\"p_value\\\\\\\": float(w_pval)},\\\\n273-                \\\\\\\"bootstrap_95ci\\\\\\\": {\\\\\\\"lower\\\\\\\": ci_lo, \\\\\\\"upper\\\\\\\": ci_hi},\\\\n--\\\\n435:        flag = \\\\\\\" *\\\\\\\" if (enc, strat, seed) in HETEROGENEITY_NOTES else \\\\\\\"\\\\\\\"\\\\n436-        print(f\\\\\\\"  {enc:12s} {strat:22s} s{seed}: R@1={r1_str}{flag}\\\\\\\")\\\\n437-\\\\n438-    # 2. Per-condition summary\\\\n439-    print()\\\\n440-    print(\\\\\\\"=\\\\\\\" * 60)\\\\n441-    print(\\\\\\\"Phase 2: Per-condition summary\\\\\\\")\\\\n442-    print(\\\\\\\"=\\\\\\\" * 60)\\\\n443-    summary = per_condition_summary(metrics)\\\\n444-    for s in summary:\\\\n445-        if s[\\\\\\\"mean\\\\\\\"] is not None:\\\\n446-            print(f\\\\\\\"  {s['encoder']:12s} {s['strategy']:22s}: {s['mean']:.4f} +/- {s['std']:.4f} (n={s['n']})\\\\\\\")\\\\n447-        else:\\\\n448-            print(f\\\\\\\"  {s['encoder']:12s} {s['strategy']:22s}: NO DATA\\\\\\\")\\\\n449-\\\\n450-    # 3. Statistical comparisons\\\\n451-    print()\\\\n452-    print(\\\\\\\"=\\\\\\\" * 60)\\\\n453-    print(\\\\\\\"Phase 3: Statistical comparisons\\\\\\\")\\\\n454-    print(\\\\\\\"=\\\\\\\" * 60)\\\\n455-    comparisons = run_comparisons(metrics)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.02}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"31:HETEROGENEITY_NOTES = {\\n32-    (\\\"starcoder\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n33-    (\\\"starcoder\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n34-    (\\\"starcoder\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n35-}\\n36-\\n37-\\n38-def _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\\n39-    \\\"\\\"\\\"Return candidate directories to search for a run's output.\\\"\\\"\\\"\\n40-    enc_short = {\\\"qwen\\\": \\\"qwen\\\", \\\"starcoder\\\": \\\"starcoder\\\"}[encoder]\\n41-    enc_full = {\\\"qwen\\\": \\\"m2_full_qwen\\\", \\\"starcoder\\\": \\\"m2_full_starcoder\\\"}[encoder]\\n42-    tag = f\\\"{strategy}_s{seed}\\\"\\n43-    tag_enc = f\\\"{strategy}_{enc_short}_s{seed}\\\"\\n44-    return [\\n45-        f\\\"{OUTPUT_BASE}/{tag}\\\",\\n46-        f\\\"{OUTPUT_BASE}/{tag_enc}\\\",\\n47-        f\\\"{CHECKPOINT_BASE}/{enc_full}/{tag}\\\",\\n48-    ]\\n49-\\n50-\\n51-def _parse_best_r1_from_log(log_path: str) -> Optional[float]:\\n--\\n115:                    note = HETEROGENEITY_NOTES.get((encoder, strategy, seed), \\\"\\\")\\n116-                    results[(encoder, strategy, seed)] = {\\n117-                        \\\"best_r1\\\": r1,\\n118-                        \\\"source\\\": \\\"mock\\\",\\n119-                        \\\"note\\\": f\\\"[DRY-RUN mock] {note}\\\" if note else \\\"[DRY-RUN mock]\\\",\\n120-                        \\\"all_evals\\\": [],\\n121-                    }\\n122-        return results\\n123-\\n124-    for encoder in ENCODERS:\\n125-        for strategy in STRATEGIES:\\n126-            for seed in SEEDS:\\n127-                key = (encoder, strategy, seed)\\n128:                note = HETEROGENEITY_NOTES.get(key, \\\"\\\")\\n129-                candidates = _candidate_dirs(encoder, strategy, seed)\\n130-                found = False\\n131-\\n132-                for cdir in candidates:\\n133-                    log_path = os.path.join(cdir, \\\"train.log\\\")\\n134-                    best_ckpt = os.path.join(cdir, \\\"best_by_recall_at_1\\\")\\n135-\\n136-                    if os.path.isfile(log_path):\\n137-                        best_r1 = _parse_best_r1_from_log(log_path)\\n138-                        all_evals = _parse_eval_metrics_from_log(log_path)\\n139-                        final = _parse_final_eval(log_path)\\n140-\\n141-                        if best_r1 is None and all_evals:\\n142-                            best_r1 = max(e.get(\\\"recall@1\\\", 0) for e in all_evals)\\n143-                        if best_r1 is None and final:\\n144-                            best_r1 = final.get(\\\"recall@1\\\")\\n145-\\n146-                        results[key] = {\\n147-                            \\\"best_r1\\\": best_r1,\\n148-                            \\\"source\\\": log_path,\\n--\\n253:                    n = HETEROGENEITY_NOTES.get((encoder, s, seed))\\n254-                    if n:\\n255-                        het_notes.append(f\\\"{encoder}/{s}/s{seed}: {n}\\\")\\n256-\\n257-            comparisons[label] = {\\n258-                \\\"status\\\": \\\"OK\\\",\\n259-                \\\"encoder\\\": encoder,\\n260-                \\\"treatment\\\": treat_strategy,\\n261-                \\\"control\\\": \\\"random\\\",\\n262-                \\\"n_pairs\\\": n_pairs,\\n263-                \\\"valid_seeds\\\": valid_seeds,\\n264-                \\\"treatment_values\\\": treat_vals,\\n265-                \\\"control_values\\\": ctrl_vals,\\n266-                \\\"treatment_mean\\\": float(treat_arr.mean()),\\n267-                \\\"treatment_std\\\": float(treat_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\n268-                \\\"control_mean\\\": float(ctrl_arr.mean()),\\n269-                \\\"control_std\\\": float(ctrl_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\n270-                \\\"mean_diff\\\": mean_diff,\\n271-                \\\"paired_ttest\\\": {\\\"t_statistic\\\": float(t_stat), \\\"p_value\\\": float(t_pval)},\\n272-                \\\"wilcoxon\\\": {\\\"w_statistic\\\": float(w_stat), \\\"p_value\\\": float(w_pval)},\\n273-                \\\"bootstrap_95ci\\\": {\\\"lower\\\": ci_lo, \\\"upper\\\": ci_hi},\\n--\\n435:        flag = \\\" *\\\" if (enc, strat, seed) in HETEROGENEITY_NOTES else \\\"\\\"\\n436-        print(f\\\"  {enc:12s} {strat:22s} s{seed}: R@1={r1_str}{flag}\\\")\\n437-\\n438-    # 2. Per-condition summary\\n439-    print()\\n440-    print(\\\"=\\\" * 60)\\n441-    print(\\\"Phase 2: Per-condition summary\\\")\\n442-    print(\\\"=\\\" * 60)\\n443-    summary = per_condition_summary(metrics)\\n444-    for s in summary:\\n445-        if s[\\\"mean\\\"] is not None:\\n446-            print(f\\\"  {s['encoder']:12s} {s['strategy']:22s}: {s['mean']:.4f} +/- {s['std']:.4f} (n={s['n']})\\\")\\n447-        else:\\n448-            print(f\\\"  {s['encoder']:12s} {s['strategy']:22s}: NO DATA\\\")\\n449-\\n450-    # 3. Statistical comparisons\\n451-    print()\\n452-    print(\\\"=\\\" * 60)\\n453-    print(\\\"Phase 3: Statistical comparisons\\\")\\n454-    print(\\\"=\\\" * 60)\\n455-    comparisons = run_comparisons(metrics)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.02}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

现有条目在第32-34行。用 `sed` 插入 Qwen 条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "ee46c676-25ca-4621-ad4a-df2618970fff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018twqa3T6woLtunnVW5E1Lo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 23782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2144
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01KdqB134iVLwH3QbneB7e76`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "sed -i '34a\\    (\"qwen\", \"random\", 42): \"3 epochs (others: 2)\",\\n    (\"qwen\", \"embedding_distance\", 42): \"3 epochs (others: 2)\",\\n    (\"qwen\", \"dataflow_aware\", 42): \"3 epochs (others: 2)\",' /root/structfuse/scripts/m2_statistical_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "3d8039f6-e823-47a8-a468-5cc799a20c98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018twqa3T6woLtunnVW5E1Lo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 23782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2144
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

_source line 11 · 2026-05-15T01:19:13.663Z_

<details><summary>↩ Tool result · `toolu_01KdqB134iVLwH3QbneB7e76`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "f9834c41-f4a4-4a2a-8ae3-2794566dbf1f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TL8FHfyc249NRxLZcufAa4`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n -A 25 \"HETEROGENEITY_NOTES\" /root/structfuse/scripts/m2_statistical_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "c396a93d-af8c-4e9c-aaa4-425cdb1cd12e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrGyCBvXPe3dVs7dpj879L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 298,
      "cache_read_input_tokens": 25926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 298
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

_source line 13 · 2026-05-15T01:19:16.751Z_

<details><summary>↩ Tool result · `toolu_01TL8FHfyc249NRxLZcufAa4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"31:HETEROGENEITY_NOTES = {\\n32-    (\\\"starcoder\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n33-    (\\\"starcoder\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n34-    (\\\"starcoder\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n35-    (\\\"qwen\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n36-    (\\\"qwen\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n37-    (\\\"qwen\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n38-}\\n39-\\n40-\\n41-def _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\\n42-    \\\"\\\"\\\"Return candidate directories to search for a run's output.\\\"\\\"\\\"\\n43-    enc_short = {\\\"qwen\\\": \\\"qwen\\\", \\\"starcoder\\\": \\\"starcoder\\\"}[encoder]\\n44-    enc_full = {\\\"qwen\\\": \\\"m2_full_qwen\\\", \\\"starcoder\\\": \\\"m2_full_starcoder\\\"}[encoder]\\n45-    tag = f\\\"{strategy}_s{seed}\\\"\\n46-    tag_enc = f\\\"{strategy}_{enc_short}_s{seed}\\\"\\n47-    return [\\n48-        f\\\"{OUTPUT_BASE}/{tag}\\\",\\n49-        f\\\"{OUTPUT_BASE}/{tag_enc}\\\",\\n50-        f\\\"{CHECKPOINT_BASE}/{enc_full}/{tag}\\\",\\n51-    ]\\n52-\\n53-\\n54-def _parse_best_r1_from_log(log_path: str) -> Optional[float]:\\n55-    \\\"\\\"\\\"Extract the last 'New best R@1=X.XXXX' value from a train.log.\\\"\\\"\\\"\\n56-    best = None\\n--\\n118:                    note = HETEROGENEITY_NOTES.get((encoder, strategy, seed), \\\"\\\")\\n119-                    results[(encoder, strategy, seed)] = {\\n120-                        \\\"best_r1\\\": r1,\\n121-                        \\\"source\\\": \\\"mock\\\",\\n122-                        \\\"note\\\": f\\\"[DRY-RUN mock] {note}\\\" if note else \\\"[DRY-RUN mock]\\\",\\n123-                        \\\"all_evals\\\": [],\\n124-                    }\\n125-        return results\\n126-\\n127-    for encoder in ENCODERS:\\n128-        for strategy in STRATEGIES:\\n129-            for seed in SEEDS:\\n130-                key = (encoder, strategy, seed)\\n131:                note = HETEROGENEITY_NOTES.get(key, \\\"\\\")\\n132-                candidates = _candidate_dirs(encoder, strategy, seed)\\n133-                found = False\\n134-\\n135-                for cdir in candidates:\\n136-                    log_path = os.path.join(cdir, \\\"train.log\\\")\\n137-                    best_ckpt = os.path.join(cdir, \\\"best_by_recall_at_1\\\")\\n138-\\n139-                    if os.path.isfile(log_path):\\n140-                        best_r1 = _parse_best_r1_from_log(log_path)\\n141-                        all_evals = _parse_eval_metrics_from_log(log_path)\\n142-                        final = _parse_final_eval(log_path)\\n143-\\n144-                        if best_r1 is None and all_evals:\\n145-                            best_r1 = max(e.get(\\\"recall@1\\\", 0) for e in all_evals)\\n146-                        if best_r1 is None and final:\\n147-                            best_r1 = final.get(\\\"recall@1\\\")\\n148-\\n149-                        results[key] = {\\n150-                            \\\"best_r1\\\": best_r1,\\n151-                            \\\"source\\\": log_path,\\n152-                            \\\"note\\\": note,\\n153-                            \\\"all_evals\\\": all_evals,\\n154-                            \\\"final_metrics\\\": final,\\n155-                        }\\n156-                        found = True\\n--\\n256:                    n = HETEROGENEITY_NOTES.get((encoder, s, seed))\\n257-                    if n:\\n258-                        het_notes.append(f\\\"{encoder}/{s}/s{seed}: {n}\\\")\\n259-\\n260-            comparisons[label] = {\\n261-                \\\"status\\\": \\\"OK\\\",\\n262-                \\\"encoder\\\": encoder,\\n263-                \\\"treatment\\\": treat_strategy,\\n264-                \\\"control\\\": \\\"random\\\",\\n265-                \\\"n_pairs\\\": n_pairs,\\n266-                \\\"valid_seeds\\\": valid_seeds,\\n267-                \\\"treatment_values\\\": treat_vals,\\n268-                \\\"control_values\\\": ctrl_vals,\\n269-                \\\"treatment_mean\\\": float(treat_arr.mean()),\\n270-                \\\"treatment_std\\\": float(treat_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\n271-                \\\"control_mean\\\": float(ctrl_arr.mean()),\\n272-                \\\"control_std\\\": float(ctrl_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\n273-                \\\"mean_diff\\\": mean_diff,\\n274-                \\\"paired_ttest\\\": {\\\"t_statistic\\\": float(t_stat), \\\"p_value\\\": float(t_pval)},\\n275-                \\\"wilcoxon\\\": {\\\"w_statistic\\\": float(w_stat), \\\"p_value\\\": float(w_pval)},\\n276-                \\\"bootstrap_95ci\\\": {\\\"lower\\\": ci_lo, \\\"upper\\\": ci_hi},\\n277-                \\\"cohens_d\\\": d,\\n278-                \\\"heterogeneity_notes\\\": het_notes,\\n279-            }\\n280-\\n281-    return comparisons\\n--\\n438:        flag = \\\" *\\\" if (enc, strat, seed) in HETEROGENEITY_NOTES else \\\"\\\"\\n439-        print(f\\\"  {enc:12s} {strat:22s} s{seed}: R@1={r1_str}{flag}\\\")\\n440-\\n441-    # 2. Per-condition summary\\n442-    print()\\n443-    print(\\\"=\\\" * 60)\\n444-    print(\\\"Phase 2: Per-condition summary\\\")\\n445-    print(\\\"=\\\" * 60)\\n446-    summary = per_condition_summary(metrics)\\n447-    for s in summary:\\n448-        if s[\\\"mean\\\"] is not None:\\n449-            print(f\\\"  {s['encoder']:12s} {s['strategy']:22s}: {s['mean']:.4f} +/- {s['std']:.4f} (n={s['n']})\\\")\\n450-        else:\\n451-            print(f\\\"  {s['encoder']:12s} {s['strategy']:22s}: NO DATA\\\")\\n452-\\n453-    # 3. Statistical comparisons\\n454-    print()\\n455-    print(\\\"=\\\" * 60)\\n456-    print(\\\"Phase 3: Statistical comparisons\\\")\\n457-    print(\\\"=\\\" * 60)\\n458-    comparisons = run_comparisons(metrics)\\n459-\\n460-    for label, c in comparisons.items():\\n461-        print(f\\\"\\\\n  [{label}]\\\")\\n462-        if c[\\\"status\\\"] != \\\"OK\\\":\\n463-            print(f\\\"    WARN: {c['status']}: only {c['n_pairs']} valid pairs\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "9e442c59-18e9-4112-a176-d5abde7e92fe",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"31:HETEROGENEITY_NOTES = {\\\\n32-    (\\\\\\\"starcoder\\\\\\\", \\\\\\\"random\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n33-    (\\\\\\\"starcoder\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n34-    (\\\\\\\"starcoder\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n35-    (\\\\\\\"qwen\\\\\\\", \\\\\\\"random\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n36-    (\\\\\\\"qwen\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n37-    (\\\\\\\"qwen\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n38-}\\\\n39-\\\\n40-\\\\n41-def _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\\\\n42-    \\\\\\\"\\\\\\\"\\\\\\\"Return candidate directories to search for a run's output.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n43-    enc_short = {\\\\\\\"qwen\\\\\\\": \\\\\\\"qwen\\\\\\\", \\\\\\\"starcoder\\\\\\\": \\\\\\\"starcoder\\\\\\\"}[encoder]\\\\n44-    enc_full = {\\\\\\\"qwen\\\\\\\": \\\\\\\"m2_full_qwen\\\\\\\", \\\\\\\"starcoder\\\\\\\": \\\\\\\"m2_full_starcoder\\\\\\\"}[encoder]\\\\n45-    tag = f\\\\\\\"{strategy}_s{seed}\\\\\\\"\\\\n46-    tag_enc = f\\\\\\\"{strategy}_{enc_short}_s{seed}\\\\\\\"\\\\n47-    return [\\\\n48-        f\\\\\\\"{OUTPUT_BASE}/{tag}\\\\\\\",\\\\n49-        f\\\\\\\"{OUTPUT_BASE}/{tag_enc}\\\\\\\",\\\\n50-        f\\\\\\\"{CHECKPOINT_BASE}/{enc_full}/{tag}\\\\\\\",\\\\n51-    ]\\\\n52-\\\\n53-\\\\n54-def _parse_best_r1_from_log(log_path: str) -> Optional[float]:\\\\n55-    \\\\\\\"\\\\\\\"\\\\\\\"Extract the last 'New best R@1=X.XXXX' value from a train.log.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n56-    best = None\\\\n--\\\\n118:                    note = HETEROGENEITY_NOTES.get((encoder, strategy, seed), \\\\\\\"\\\\\\\")\\\\n119-                    results[(encoder, strategy, seed)] = {\\\\n120-                        \\\\\\\"best_r1\\\\\\\": r1,\\\\n121-                        \\\\\\\"source\\\\\\\": \\\\\\\"mock\\\\\\\",\\\\n122-                        \\\\\\\"note\\\\\\\": f\\\\\\\"[DRY-RUN mock] {note}\\\\\\\" if note else \\\\\\\"[DRY-RUN mock]\\\\\\\",\\\\n123-                        \\\\\\\"all_evals\\\\\\\": [],\\\\n124-                    }\\\\n125-        return results\\\\n126-\\\\n127-    for encoder in ENCODERS:\\\\n128-        for strategy in STRATEGIES:\\\\n129-            for seed in SEEDS:\\\\n130-                key = (encoder, strategy, seed)\\\\n131:                note = HETEROGENEITY_NOTES.get(key, \\\\\\\"\\\\\\\")\\\\n132-                candidates = _candidate_dirs(encoder, strategy, seed)\\\\n133-                found = False\\\\n134-\\\\n135-                for cdir in candidates:\\\\n136-                    log_path = os.path.join(cdir, \\\\\\\"train.log\\\\\\\")\\\\n137-                    best_ckpt = os.path.join(cdir, \\\\\\\"best_by_recall_at_1\\\\\\\")\\\\n138-\\\\n139-                    if os.path.isfile(log_path):\\\\n140-                        best_r1 = _parse_best_r1_from_log(log_path)\\\\n141-                        all_evals = _parse_eval_metrics_from_log(log_path)\\\\n142-                        final = _parse_final_eval(log_path)\\\\n143-\\\\n144-                        if best_r1 is None and all_evals:\\\\n145-                            best_r1 = max(e.get(\\\\\\\"recall@1\\\\\\\", 0) for e in all_evals)\\\\n146-                        if best_r1 is None and final:\\\\n147-                            best_r1 = final.get(\\\\\\\"recall@1\\\\\\\")\\\\n148-\\\\n149-                        results[key] = {\\\\n150-                            \\\\\\\"best_r1\\\\\\\": best_r1,\\\\n151-                            \\\\\\\"source\\\\\\\": log_path,\\\\n152-                            \\\\\\\"note\\\\\\\": note,\\\\n153-                            \\\\\\\"all_evals\\\\\\\": all_evals,\\\\n154-                            \\\\\\\"final_metrics\\\\\\\": final,\\\\n155-                        }\\\\n156-                        found = True\\\\n--\\\\n256:                    n = HETEROGENEITY_NOTES.get((encoder, s, seed))\\\\n257-                    if n:\\\\n258-                        het_notes.append(f\\\\\\\"{encoder}/{s}/s{seed}: {n}\\\\\\\")\\\\n259-\\\\n260-            comparisons[label] = {\\\\n261-                \\\\\\\"status\\\\\\\": \\\\\\\"OK\\\\\\\",\\\\n262-                \\\\\\\"encoder\\\\\\\": encoder,\\\\n263-                \\\\\\\"treatment\\\\\\\": treat_strategy,\\\\n264-                \\\\\\\"control\\\\\\\": \\\\\\\"random\\\\\\\",\\\\n265-                \\\\\\\"n_pairs\\\\\\\": n_pairs,\\\\n266-                \\\\\\\"valid_seeds\\\\\\\": valid_seeds,\\\\n267-                \\\\\\\"treatment_values\\\\\\\": treat_vals,\\\\n268-                \\\\\\\"control_values\\\\\\\": ctrl_vals,\\\\n269-                \\\\\\\"treatment_mean\\\\\\\": float(treat_arr.mean()),\\\\n270-                \\\\\\\"treatment_std\\\\\\\": float(treat_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\\\n271-                \\\\\\\"control_mean\\\\\\\": float(ctrl_arr.mean()),\\\\n272-                \\\\\\\"control_std\\\\\\\": float(ctrl_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\\\n273-                \\\\\\\"mean_diff\\\\\\\": mean_diff,\\\\n274-                \\\\\\\"paired_ttest\\\\\\\": {\\\\\\\"t_statistic\\\\\\\": float(t_stat), \\\\\\\"p_value\\\\\\\": float(t_pval)},\\\\n275-                \\\\\\\"wilcoxon\\\\\\\": {\\\\\\\"w_statistic\\\\\\\": float(w_stat), \\\\\\\"p_value\\\\\\\": float(w_pval)},\\\\n276-                \\\\\\\"bootstrap_95ci\\\\\\\": {\\\\\\\"lower\\\\\\\": ci_lo, \\\\\\\"upper\\\\\\\": ci_hi},\\\\n277-                \\\\\\\"cohens_d\\\\\\\": d,\\\\n278-                \\\\\\\"heterogeneity_notes\\\\\\\": het_notes,\\\\n279-            }\\\\n280-\\\\n281-    return comparisons\\\\n--\\\\n438:        flag = \\\\\\\" *\\\\\\\" if (enc, strat, seed) in HETEROGENEITY_NOTES else \\\\\\\"\\\\\\\"\\\\n439-        print(f\\\\\\\"  {enc:12s} {strat:22s} s{seed}: R@1={r1_str}{flag}\\\\\\\")\\\\n440-\\\\n441-    # 2. Per-condition summary\\\\n442-    print()\\\\n443-    print(\\\\\\\"=\\\\\\\" * 60)\\\\n444-    print(\\\\\\\"Phase 2: Per-condition summary\\\\\\\")\\\\n445-    print(\\\\\\\"=\\\\\\\" * 60)\\\\n446-    summary = per_condition_summary(metrics)\\\\n447-    for s in summary:\\\\n448-        if s[\\\\\\\"mean\\\\\\\"] is not None:\\\\n449-            print(f\\\\\\\"  {s['encoder']:12s} {s['strategy']:22s}: {s['mean']:.4f} +/- {s['std']:.4f} (n={s['n']})\\\\\\\")\\\\n450-        else:\\\\n451-            print(f\\\\\\\"  {s['encoder']:12s} {s['strategy']:22s}: NO DATA\\\\\\\")\\\\n452-\\\\n453-    # 3. Statistical comparisons\\\\n454-    print()\\\\n455-    print(\\\\\\\"=\\\\\\\" * 60)\\\\n456-    print(\\\\\\\"Phase 3: Statistical comparisons\\\\\\\")\\\\n457-    print(\\\\\\\"=\\\\\\\" * 60)\\\\n458-    comparisons = run_comparisons(metrics)\\\\n459-\\\\n460-    for label, c in comparisons.items():\\\\n461-        print(f\\\\\\\"\\\\\\\\n  [{label}]\\\\\\\")\\\\n462-        if c[\\\\\\\"status\\\\\\\"] != \\\\\\\"OK\\\\\\\":\\\\n463-            print(f\\\\\\\"    WARN: {c['status']}: only {c['n_pairs']} valid pairs\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"31:HETEROGENEITY_NOTES = {\\n32-    (\\\"starcoder\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n33-    (\\\"starcoder\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n34-    (\\\"starcoder\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n35-    (\\\"qwen\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n36-    (\\\"qwen\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n37-    (\\\"qwen\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n38-}\\n39-\\n40-\\n41-def _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\\n42-    \\\"\\\"\\\"Return candidate directories to search for a run's output.\\\"\\\"\\\"\\n43-    enc_short = {\\\"qwen\\\": \\\"qwen\\\", \\\"starcoder\\\": \\\"starcoder\\\"}[encoder]\\n44-    enc_full = {\\\"qwen\\\": \\\"m2_full_qwen\\\", \\\"starcoder\\\": \\\"m2_full_starcoder\\\"}[encoder]\\n45-    tag = f\\\"{strategy}_s{seed}\\\"\\n46-    tag_enc = f\\\"{strategy}_{enc_short}_s{seed}\\\"\\n47-    return [\\n48-        f\\\"{OUTPUT_BASE}/{tag}\\\",\\n49-        f\\\"{OUTPUT_BASE}/{tag_enc}\\\",\\n50-        f\\\"{CHECKPOINT_BASE}/{enc_full}/{tag}\\\",\\n51-    ]\\n52-\\n53-\\n54-def _parse_best_r1_from_log(log_path: str) -> Optional[float]:\\n55-    \\\"\\\"\\\"Extract the last 'New best R@1=X.XXXX' value from a train.log.\\\"\\\"\\\"\\n56-    best = None\\n--\\n118:                    note = HETEROGENEITY_NOTES.get((encoder, strategy, seed), \\\"\\\")\\n119-                    results[(encoder, strategy, seed)] = {\\n120-                        \\\"best_r1\\\": r1,\\n121-                        \\\"source\\\": \\\"mock\\\",\\n122-                        \\\"note\\\": f\\\"[DRY-RUN mock] {note}\\\" if note else \\\"[DRY-RUN mock]\\\",\\n123-                        \\\"all_evals\\\": [],\\n124-                    }\\n125-        return results\\n126-\\n127-    for encoder in ENCODERS:\\n128-        for strategy in STRATEGIES:\\n129-            for seed in SEEDS:\\n130-                key = (encoder, strategy, seed)\\n131:                note = HETEROGENEITY_NOTES.get(key, \\\"\\\")\\n132-                candidates = _candidate_dirs(encoder, strategy, seed)\\n133-                found = False\\n134-\\n135-                for cdir in candidates:\\n136-                    log_path = os.path.join(cdir, \\\"train.log\\\")\\n137-                    best_ckpt = os.path.join(cdir, \\\"best_by_recall_at_1\\\")\\n138-\\n139-                    if os.path.isfile(log_path):\\n140-                        best_r1 = _parse_best_r1_from_log(log_path)\\n141-                        all_evals = _parse_eval_metrics_from_log(log_path)\\n142-                        final = _parse_final_eval(log_path)\\n143-\\n144-                        if best_r1 is None and all_evals:\\n145-                            best_r1 = max(e.get(\\\"recall@1\\\", 0) for e in all_evals)\\n146-                        if best_r1 is None and final:\\n147-                            best_r1 = final.get(\\\"recall@1\\\")\\n148-\\n149-                        results[key] = {\\n150-                            \\\"best_r1\\\": best_r1,\\n151-                            \\\"source\\\": log_path,\\n152-                            \\\"note\\\": note,\\n153-                            \\\"all_evals\\\": all_evals,\\n154-                            \\\"final_metrics\\\": final,\\n155-                        }\\n156-                        found = True\\n--\\n256:                    n = HETEROGENEITY_NOTES.get((encoder, s, seed))\\n257-                    if n:\\n258-                        het_notes.append(f\\\"{encoder}/{s}/s{seed}: {n}\\\")\\n259-\\n260-            comparisons[label] = {\\n261-                \\\"status\\\": \\\"OK\\\",\\n262-                \\\"encoder\\\": encoder,\\n263-                \\\"treatment\\\": treat_strategy,\\n264-                \\\"control\\\": \\\"random\\\",\\n265-                \\\"n_pairs\\\": n_pairs,\\n266-                \\\"valid_seeds\\\": valid_seeds,\\n267-                \\\"treatment_values\\\": treat_vals,\\n268-                \\\"control_values\\\": ctrl_vals,\\n269-                \\\"treatment_mean\\\": float(treat_arr.mean()),\\n270-                \\\"treatment_std\\\": float(treat_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\n271-                \\\"control_mean\\\": float(ctrl_arr.mean()),\\n272-                \\\"control_std\\\": float(ctrl_arr.std(ddof=1)) if n_pairs > 1 else 0.0,\\n273-                \\\"mean_diff\\\": mean_diff,\\n274-                \\\"paired_ttest\\\": {\\\"t_statistic\\\": float(t_stat), \\\"p_value\\\": float(t_pval)},\\n275-                \\\"wilcoxon\\\": {\\\"w_statistic\\\": float(w_stat), \\\"p_value\\\": float(w_pval)},\\n276-                \\\"bootstrap_95ci\\\": {\\\"lower\\\": ci_lo, \\\"upper\\\": ci_hi},\\n277-                \\\"cohens_d\\\": d,\\n278-                \\\"heterogeneity_notes\\\": het_notes,\\n279-            }\\n280-\\n281-    return comparisons\\n--\\n438:        flag = \\\" *\\\" if (enc, strat, seed) in HETEROGENEITY_NOTES else \\\"\\\"\\n439-        print(f\\\"  {enc:12s} {strat:22s} s{seed}: R@1={r1_str}{flag}\\\")\\n440-\\n441-    # 2. Per-condition summary\\n442-    print()\\n443-    print(\\\"=\\\" * 60)\\n444-    print(\\\"Phase 2: Per-condition summary\\\")\\n445-    print(\\\"=\\\" * 60)\\n446-    summary = per_condition_summary(metrics)\\n447-    for s in summary:\\n448-        if s[\\\"mean\\\"] is not None:\\n449-            print(f\\\"  {s['encoder']:12s} {s['strategy']:22s}: {s['mean']:.4f} +/- {s['std']:.4f} (n={s['n']})\\\")\\n450-        else:\\n451-            print(f\\\"  {s['encoder']:12s} {s['strategy']:22s}: NO DATA\\\")\\n452-\\n453-    # 3. Statistical comparisons\\n454-    print()\\n455-    print(\\\"=\\\" * 60)\\n456-    print(\\\"Phase 3: Statistical comparisons\\\")\\n457-    print(\\\"=\\\" * 60)\\n458-    comparisons = run_comparisons(metrics)\\n459-\\n460-    for label, c in comparisons.items():\\n461-        print(f\\\"\\\\n  [{label}]\\\")\\n462-        if c[\\\"status\\\"] != \\\"OK\\\":\\n463-            print(f\\\"    WARN: {c['status']}: only {c['n_pairs']} valid pairs\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

条目已正确插入（第35-37行）。运行 dry-run 验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "916eac08-62e7-4de6-9411-3275b03e105a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QagR4cC7gVcGiWCMKPreuZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 26224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2526
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

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01AQ4LcZX5fqdjR1VdWNH2RX`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cd /root/structfuse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/m2_statistical_analysis.py --dry-run 2>&1 | tail -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "bd29419a-92ba-4f5c-9e18-95a124558bd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QagR4cC7gVcGiWCMKPreuZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 26224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2526
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

_source line 16 · 2026-05-15T01:19:24.821Z_

<details><summary>↩ Tool result · `toolu_01AQ4LcZX5fqdjR1VdWNH2RX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    Boot 95CI: [0.0348, 0.0763]\\n    Cohen's d: 2.6341\\n    Note: starcoder/embedding_distance/s42: 3 epochs (others: 2)\\n    Note: starcoder/random/s42: 3 epochs (others: 2)\\n\\n  [starcoder__dataflow_aware_vs_random]\\n    Treatment: 0.5082 +/- 0.0150\\n    Control:   0.4150 +/- 0.0040\\n    D Mean:    0.0932\\n    Paired t:  t=14.4310, p=0.0048\\n    Wilcoxon:  W=0.0000, p=0.2500\\n    Boot 95CI: [0.0804, 0.1011]\\n    Cohen's d: 8.3317\\n    Note: starcoder/dataflow_aware/s42: 3 epochs (others: 2)\\n    Note: starcoder/random/s42: 3 epochs (others: 2)\\n\\nJSON saved: /root/structfuse/results/m2_stats_dryrun.json\\nMarkdown saved: /root/structfuse/results/m2_stats_dryrun.md\\n\\nDone.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "913c09b0-29ec-4653-a6bd-6109b78417d7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    Boot 95CI: [0.0348, 0.0763]\\\\n    Cohen's d: 2.6341\\\\n    Note: starcoder/embedding_distance/s42: 3 epochs (others: 2)\\\\n    Note: starcoder/random/s42: 3 epochs (others: 2)\\\\n\\\\n  [starcoder__dataflow_aware_vs_random]\\\\n    Treatment: 0.5082 +/- 0.0150\\\\n    Control:   0.4150 +/- 0.0040\\\\n    D Mean:    0.0932\\\\n    Paired t:  t=14.4310, p=0.0048\\\\n    Wilcoxon:  W=0.0000, p=0.2500\\\\n    Boot 95CI: [0.0804, 0.1011]\\\\n    Cohen's d: 8.3317\\\\n    Note: starcoder/dataflow_aware/s42: 3 epochs (others: 2)\\\\n    Note: starcoder/random/s42: 3 epochs (others: 2)\\\\n\\\\nJSON saved: /root/structfuse/results/m2_stats_dryrun.json\\\\nMarkdown saved: /root/structfuse/results/m2_stats_dryrun.md\\\\n\\\\nDone.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    Boot 95CI: [0.0348, 0.0763]\\n    Cohen's d: 2.6341\\n    Note: starcoder/embedding_distance/s42: 3 epochs (others: 2)\\n    Note: starcoder/random/s42: 3 epochs (others: 2)\\n\\n  [starcoder__dataflow_aware_vs_random]\\n    Treatment: 0.5082 +/- 0.0150\\n    Control:   0.4150 +/- 0.0040\\n    D Mean:    0.0932\\n    Paired t:  t=14.4310, p=0.0048\\n    Wilcoxon:  W=0.0000, p=0.2500\\n    Boot 95CI: [0.0804, 0.1011]\\n    Cohen's d: 8.3317\\n    Note: starcoder/dataflow_aware/s42: 3 epochs (others: 2)\\n    Note: starcoder/random/s42: 3 epochs (others: 2)\\n\\nJSON saved: /root/structfuse/results/m2_stats_dryrun.json\\nMarkdown saved: /root/structfuse/results/m2_stats_dryrun.md\\n\\nDone.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.35}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

完成。Qwen s42 的 3 条 heterogeneity 标注已添加到 `HETEROGENEITY_NOTES`（第35-37行），dry-run 正常通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "uuid": "6bada89c-9866-4ad2-a8b3-0ed3ad30f426",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJKM6fMTfR21ubNK53Defu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 28750,
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

_source line 18_

完成。Qwen s42 的 3 条 heterogeneity 标注已添加到 `HETEROGENEITY_NOTES`（第35-37行），dry-run 正常通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 29941,
  "duration_api_ms": 27897,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "2232eb28-fb02-4ca5-8df5-034b9605609a",
  "total_cost_usd": 0.20449600000000004,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 17892,
    "cache_read_input_tokens": 139206,
    "output_tokens": 873,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17892,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 56,
        "cache_read_input_tokens": 28750,
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
      "inputTokens": 1088,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001198,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 873,
      "cacheReadInputTokens": 139206,
      "cacheCreationInputTokens": 17892,
      "webSearchRequests": 0,
      "costUSD": 0.20329800000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "4cd6b225-5659-48d8-b8ca-f58a24683451"
}
```

</details>

---
