# code fisher test script object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_code_fisher-test-script-object_20260515T204705.log`
- **Structured JSON:** [`a697fdce97a1adab0040.json`](../../sessions/a6/a697fdce97a1adab0040.json)

## Before a recorded user message

16 recorded events

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
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
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
  "uuid": "1d6e6fbe-50f3-440e-8c01-c1d38a4b5099",
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
    "resetsAt": 1778886600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f435da0c-e5de-4bc6-b36a-04378374b670",
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to create a Python script on server bjb1-18228 for Fisher exact test + bootstrap CI analysis. Let me break this down:

1. Create the script `fisher_object_sixway.py` in `/root/acr-vla-conformal-refinement/analysis/`
2. Write it to the server
3. Run dry-run with `--seed42-only`
4. Report the output

First, let me write the script locally, then transfer it to the server. Actually, I should use ssh_execute to create the file and run it.

Let me first load the MCP tools I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "df5ebd2f-0796-43b2-bac1-b55be6db701b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhVsWta99acweLHLFW4PiZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12772,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12772
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RuC5cos1Mt1kuvpecGxocD`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "60b4e350-63ea-4808-ba4f-44d69c728ca7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhVsWta99acweLHLFW4PiZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12772,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12772
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

_source line 6 · 2026-05-15T20:47:19.869Z_

<details><summary>↩ Tool result · `toolu_01RuC5cos1Mt1kuvpecGxocD`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "2e0f835e-dab4-498c-92ec-3666af215350",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

先写脚本，然后部署到服务器运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "8655b550-7862-430b-affe-61dd161df1ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016N2edVcXnGHLZ2wUftS9KS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 24613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 826
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01MnHRgck8U5VFWxYqsU5gkb`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "mkdir -p /root/acr-vla-conformal-refinement/analysis",
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
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "107508d6-418b-44a2-8236-82bf4e13d99d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016N2edVcXnGHLZ2wUftS9KS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 24613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 826
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

_source line 9 · 2026-05-15T20:47:24.349Z_

<details><summary>↩ Tool result · `toolu_01MnHRgck8U5VFWxYqsU5gkb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "98c92ea3-860e-4f4d-a2f2-82d9cd6be6d3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.93}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_011QJ43CHmgCTm9ddRY5sAVt`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "cat > /root/acr-vla-conformal-refinement/analysis/fisher_object_sixway.py << 'SCRIPTEOF'\n#!/usr/bin/env python3\n\"\"\"Fisher exact test + bootstrap CI for LIBERO-Object 6-method comparison.\n\nCompares obs_only (ACR) vs 5 baselines across 10 OBJECT tasks.\nEach task has 10 trials per seed. Supports seed=42 alone or pooled seed=42+43.\n\nUsage:\n    python fisher_object_sixway.py                  # use all available seeds\n    python fisher_object_sixway.py --seed42-only    # dry-run with seed=42 only\n    python fisher_object_sixway.py --output-json results.json\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport sys\nfrom collections import OrderedDict\n\nimport numpy as np\nfrom scipy.stats import fisher_exact\n\nTASKS = [\n    \"alphabet_soup\", \"cream_cheese\", \"salad_dressing\", \"bbq_sauce\", \"ketchup\",\n    \"tomato_sauce\", \"butter\", \"milk\", \"chocolate_pudding\", \"orange_juice\",\n]\n\nMETHODS = [\"obs_only\", \"argmin\", \"perdof\", \"vla_only\", \"vla_mean\", \"scalar\"]\nTRIALS_PER_TASK = 10\n\nSEED42 = {\n    \"obs_only\":  {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3},\n    \"argmin\":    {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0.0, \"tomato_sauce\": 0.0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3},\n    \"perdof\":    {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.0, \"tomato_sauce\": 0.0, \"butter\": 0.1, \"milk\": 0.0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3},\n    \"vla_only\":  {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.0, \"tomato_sauce\": 0.1, \"butter\": 0.0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3},\n    \"vla_mean\":  {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.0, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1},\n    \"scalar\":    {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.0, \"tomato_sauce\": 0.0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2},\n}\n\nSEED43 = {\n    \"obs_only\":  None,\n    \"argmin\":    None,\n    \"perdof\":    None,\n    \"vla_only\":  {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0.0, \"tomato_sauce\": 0.0, \"butter\": 0.0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2},\n    \"vla_mean\":  None,\n    \"scalar\":    None,\n}\n\n\ndef sr_to_counts(sr_dict):\n    \"\"\"Convert per-task SR dict to (total_success, total_trials).\"\"\"\n    s = sum(round(sr_dict[t] * TRIALS_PER_TASK) for t in TASKS)\n    n = len(TASKS) * TRIALS_PER_TASK\n    return s, n\n\n\ndef per_task_successes(sr_dict):\n    \"\"\"Return list of per-task success counts.\"\"\"\n    return [round(sr_dict[t] * TRIALS_PER_TASK) for t in TASKS]\n\n\ndef cohens_h(p1, p2):\n    return 2 * math.asin(math.sqrt(p1)) - 2 * math.asin(math.sqrt(p2))\n\n\ndef get_pooled_counts(method, seed42_only=False):\n    \"\"\"Get pooled (success, trials) across available seeds.\"\"\"\n    s42, n42 = sr_to_counts(SEED42[method])\n    total_s, total_n = s42, n42\n    if not seed42_only and SEED43[method] is not None:\n        s43, n43 = sr_to_counts(SEED43[method])\n        total_s += s43\n        total_n += n43\n    return total_s, total_n\n\n\ndef fisher_2x2(s1, n1, s2, n2):\n    \"\"\"Run Fisher exact test on 2x2 table. Returns (odds_ratio, p_value, table).\"\"\"\n    table = np.array([[s1, n1 - s1], [s2, n2 - s2]])\n    odds, p = fisher_exact(table, alternative='two-sided')\n    return odds, p, table\n\n\ndef bootstrap_sr_diff(method_a, method_b, seed42_only=False, n_boot=10000, rng_seed=0):\n    \"\"\"Bootstrap CI for SR difference (method_a - method_b) via task-level resampling.\"\"\"\n    rng = np.random.RandomState(rng_seed)\n\n    succ_a, succ_b = [], []\n    # seed42\n    succ_a.append(per_task_successes(SEED42[method_a]))\n    succ_b.append(per_task_successes(SEED42[method_b]))\n    # seed43\n    if not seed42_only:\n        if SEED43[method_a] is not None and SEED43[method_b] is not None:\n            succ_a.append(per_task_successes(SEED43[method_a]))\n            succ_b.append(per_task_successes(SEED43[method_b]))\n\n    succ_a = np.concatenate(succ_a)  # shape: (n_tasks_total,)\n    succ_b = np.concatenate(succ_b)\n    n_tasks = len(succ_a)\n\n    diffs = np.empty(n_boot)\n    for i in range(n_boot):\n        idx = rng.randint(0, n_tasks, size=n_tasks)\n        sr_a = succ_a[idx].sum() / (n_tasks * TRIALS_PER_TASK)\n        sr_b = succ_b[idx].sum() / (n_tasks * TRIALS_PER_TASK)\n        diffs[i] = sr_a - sr_b\n\n    ci_lo, ci_hi = np.percentile(diffs, [2.5, 97.5])\n    mean_diff = diffs.mean()\n    return mean_diff, ci_lo, ci_hi, n_tasks\n\n\ndef print_header(title):\n    print(f\"\\n{'='*60}\")\n    print(f\"  {title}\")\n    print(f\"{'='*60}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Fisher exact test + bootstrap CI for LIBERO-Object\")\n    parser.add_argument(\"--seed42-only\", action=\"store_true\", help=\"Only use seed=42 data\")\n    parser.add_argument(\"--output-json\", type=str, default=None, help=\"Output JSON file path\")\n    args = parser.parse_args()\n\n    results = {}\n\n    # Count available seeds per method\n    seeds_used = {}\n    for m in METHODS:\n        n_seeds = 1\n        if not args.seed42_only and SEED43[m] is not None:\n            n_seeds = 2\n        seeds_used[m] = n_seeds\n\n    print_header(\"LIBERO-Object 6-Method Statistical Analysis\")\n    mode = \"seed=42 only\" if args.seed42_only else \"all available seeds\"\n    print(f\"Mode: {mode}\")\n    print(f\"Seeds available per method:\")\n    for m in METHODS:\n        print(f\"  {m:12s}: {seeds_used[m]} seed(s)\")\n\n    # ── Section 1: Pooled Fisher exact test (obs_only vs argmin) ──\n    print_header(\"1. Pooled Fisher Exact Test: obs_only vs argmin\")\n\n    s_obs, n_obs = get_pooled_counts(\"obs_only\", args.seed42_only)\n    s_arg, n_arg = get_pooled_counts(\"argmin\", args.seed42_only)\n    odds, p, table = fisher_2x2(s_obs, n_obs, s_arg, n_arg)\n    h = cohens_h(s_obs / n_obs, s_arg / n_arg)\n\n    print(f\"\\n  obs_only: {s_obs}/{n_obs} = {s_obs/n_obs:.1%}\")\n    print(f\"  argmin:   {s_arg}/{n_arg} = {s_arg/n_arg:.1%}\")\n    print(f\"\\n  2x2 contingency table:\")\n    print(f\"              success  failure\")\n    print(f\"  obs_only    {table[0,0]:>7.0f}  {table[0,1]:>7.0f}\")\n    print(f\"  argmin      {table[1,0]:>7.0f}  {table[1,1]:>7.0f}\")\n    print(f\"\\n  Fisher exact p-value (two-sided): {p:.4f}\")\n    print(f\"  Odds ratio: {odds:.3f}\")\n    print(f\"  Cohen's h: {h:.3f}\")\n    print(f\"  Interpretation: {'Significant (p<0.05)' if p < 0.05 else 'Not significant (p>=0.05)'}\")\n\n    results[\"pooled_fisher\"] = {\n        \"obs_only\": {\"success\": int(s_obs), \"trials\": int(n_obs), \"sr\": round(s_obs/n_obs, 4)},\n        \"argmin\": {\"success\": int(s_arg), \"trials\": int(n_arg), \"sr\": round(s_arg/n_arg, 4)},\n        \"p_value\": round(p, 6), \"odds_ratio\": round(odds, 4), \"cohens_h\": round(h, 4),\n    }\n\n    # ── Section 2: Per-seed Fisher exact test ──\n    print_header(\"2. Per-Seed Fisher Exact Test: obs_only vs argmin\")\n    results[\"per_seed_fisher\"] = {}\n\n    for seed_name, seed_data in [(\"seed42\", SEED42), (\"seed43\", SEED43)]:\n        if args.seed42_only and seed_name == \"seed43\":\n            continue\n        if seed_data[\"obs_only\"] is None or seed_data[\"argmin\"] is None:\n            print(f\"\\n  {seed_name}: SKIPPED (data not available)\")\n            results[\"per_seed_fisher\"][seed_name] = \"not_available\"\n            continue\n\n        s1, n1 = sr_to_counts(seed_data[\"obs_only\"])\n        s2, n2 = sr_to_counts(seed_data[\"argmin\"])\n        odds_s, p_s, table_s = fisher_2x2(s1, n1, s2, n2)\n        h_s = cohens_h(s1/n1, s2/n2)\n\n        print(f\"\\n  {seed_name}:\")\n        print(f\"    obs_only: {s1}/{n1} = {s1/n1:.1%}\")\n        print(f\"    argmin:   {s2}/{n2} = {s2/n2:.1%}\")\n        print(f\"    Fisher p = {p_s:.4f}, OR = {odds_s:.3f}, h = {h_s:.3f}\")\n\n        results[\"per_seed_fisher\"][seed_name] = {\n            \"obs_only_sr\": round(s1/n1, 4), \"argmin_sr\": round(s2/n2, 4),\n            \"p_value\": round(p_s, 6), \"odds_ratio\": round(odds_s, 4), \"cohens_h\": round(h_s, 4),\n        }\n\n    # ── Section 3: Bootstrap CI ──\n    print_header(\"3. Bootstrap CI for SR Difference (obs_only - argmin)\")\n\n    mean_d, ci_lo, ci_hi, n_tasks_boot = bootstrap_sr_diff(\n        \"obs_only\", \"argmin\", seed42_only=args.seed42_only\n    )\n    print(f\"\\n  Task-level resampling, {n_tasks_boot} tasks, 10000 bootstrap iterations\")\n    print(f\"  Mean difference: {mean_d:+.4f} ({mean_d:+.1%})\")\n    print(f\"  95% CI: [{ci_lo:+.4f}, {ci_hi:+.4f}] ([{ci_lo:+.1%}, {ci_hi:+.1%}])\")\n    ci_includes_zero = ci_lo <= 0 <= ci_hi\n    print(f\"  CI includes 0: {'Yes → not significant' if ci_includes_zero else 'No → significant'}\")\n\n    results[\"bootstrap_ci\"] = {\n        \"mean_diff\": round(float(mean_d), 6), \"ci_lo\": round(float(ci_lo), 6),\n        \"ci_hi\": round(float(ci_hi), 6), \"n_tasks\": n_tasks_boot,\n        \"ci_includes_zero\": bool(ci_includes_zero),\n    }\n\n    # ── Section 4: Six-way comparison table ──\n    print_header(\"4. Six-Way Comparison Table\")\n    print(f\"\\n  {'Method':12s} | {'Pooled SR':>10s} | {'seed42 SR':>10s} | {'seed43 SR':>10s} | {'Seeds':>5s}\")\n    print(f\"  {'-'*12}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*5}\")\n\n    results[\"sixway_table\"] = {}\n    for m in METHODS:\n        s42, n42 = sr_to_counts(SEED42[m])\n        sr42 = s42 / n42\n\n        sp, np_ = get_pooled_counts(m, args.seed42_only)\n        sr_pooled = sp / np_\n\n        if not args.seed42_only and SEED43[m] is not None:\n            s43, n43 = sr_to_counts(SEED43[m])\n            sr43_str = f\"{s43/n43:.1%}\"\n            sr43_val = round(s43/n43, 4)\n        else:\n            sr43_str = \"N/A\"\n            sr43_val = None\n\n        print(f\"  {m:12s} | {sr_pooled:>9.1%} | {sr42:>9.1%} | {sr43_str:>10s} | {seeds_used[m]:>5d}\")\n\n        results[\"sixway_table\"][m] = {\n            \"pooled_sr\": round(sr_pooled, 4), \"seed42_sr\": round(sr42, 4),\n            \"seed43_sr\": sr43_val, \"n_seeds\": seeds_used[m],\n        }\n\n    # ── Section 5: All pairwise Fisher tests ──\n    print_header(\"5. Pairwise Fisher Tests: obs_only vs Each Baseline\")\n    n_comparisons = len(METHODS) - 1\n    print(f\"\\n  Bonferroni correction: {n_comparisons} comparisons, α_adj = {0.05/n_comparisons:.4f}\")\n    print(f\"\\n  {'Comparison':30s} | {'p-value':>8s} | {'p_adj':>8s} | {'OR':>6s} | {'h':>6s} | {'Sig?':>6s}\")\n    print(f\"  {'-'*30}-+-{'-'*8}-+-{'-'*8}-+-{'-'*6}-+-{'-'*6}-+-{'-'*6}\")\n\n    results[\"pairwise\"] = {}\n    for m in METHODS:\n        if m == \"obs_only\":\n            continue\n        s_m, n_m = get_pooled_counts(m, args.seed42_only)\n        odds_m, p_m, _ = fisher_2x2(s_obs, n_obs, s_m, n_m)\n        h_m = cohens_h(s_obs / n_obs, s_m / n_m)\n        p_adj = min(p_m * n_comparisons, 1.0)\n        sig = \"Yes\" if p_adj < 0.05 else \"No\"\n\n        label = f\"obs_only vs {m}\"\n        print(f\"  {label:30s} | {p_m:>8.4f} | {p_adj:>8.4f} | {odds_m:>6.3f} | {h_m:>+6.3f} | {sig:>6s}\")\n\n        results[\"pairwise\"][m] = {\n            \"p_value\": round(p_m, 6), \"p_adjusted\": round(p_adj, 6),\n            \"odds_ratio\": round(odds_m, 4), \"cohens_h\": round(h_m, 4),\n            \"significant_bonferroni\": p_adj < 0.05,\n        }\n\n    print()\n\n    # JSON output\n    if args.output_json:\n        with open(args.output_json, 'w') as f:\n            json.dump(results, f, indent=2)\n        print(f\"Results saved to {args.output_json}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPTEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "0faf947f-8866-45c0-864c-29808764a1c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTDMMoZ4YWqBYMprKqCVxa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 213,
      "cache_read_input_tokens": 25439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 213
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 11 · 2026-05-15T20:48:22.853Z_

<details><summary>↩ Tool result · `toolu_011QJ43CHmgCTm9ddRY5sAVt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "5aec0d4e-6af6-4bff-8f19-d5cddca2e6b3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

脚本已写入，运行 dry-run。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "5af556b2-8d06-47db-839c-70cf8c69be67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHL2HTXM5rJi62UHk2tQKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4999,
      "cache_read_input_tokens": 25652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4999
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_013oLWDeS4P5WFcJszLELFhc`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/analysis && python fisher_object_sixway.py --seed42-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "e8deb5cf-f0a8-4ed9-a151-1643a34150df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHL2HTXM5rJi62UHk2tQKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4999,
      "cache_read_input_tokens": 25652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4999
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

_source line 14 · 2026-05-15T20:48:29.330Z_

<details><summary>↩ Tool result · `toolu_013oLWDeS4P5WFcJszLELFhc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  LIBERO-Object 6-Method Statistical Analysis\\n============================================================\\nMode: seed=42 only\\nSeeds available per method:\\n  obs_only    : 1 seed(s)\\n  argmin      : 1 seed(s)\\n  perdof      : 1 seed(s)\\n  vla_only    : 1 seed(s)\\n  vla_mean    : 1 seed(s)\\n  scalar      : 1 seed(s)\\n\\n============================================================\\n  1. Pooled Fisher Exact Test: obs_only vs argmin\\n============================================================\\n\\n  obs_only: 19/100 = 19.0%\\n  argmin:   12/100 = 12.0%\\n\\n  2x2 contingency table:\\n              success  failure\\n  obs_only         19       81\\n  argmin           12       88\\n\\n  Fisher exact p-value (two-sided): 0.2408\\n  Odds ratio: 1.720\\n  Cohen's h: 0.195\\n  Interpretation: Not significant (p>=0.05)\\n\\n============================================================\\n  2. Per-Seed Fisher Exact Test: obs_only vs argmin\\n============================================================\\n\\n  seed42:\\n    obs_only: 19/100 = 19.0%\\n    argmin:   12/100 = 12.0%\\n    Fisher p = 0.2408, OR = 1.720, h = 0.195\\n\\n============================================================\\n  3. Bootstrap CI for SR Difference (obs_only - argmin)\\n============================================================\\n\\n  Task-level resampling, 10 tasks, 10000 bootstrap iterations\\n  Mean difference: +0.0702 (+7.0%)\\n  95% CI: [+0.0300, +0.1100] ([+3.0%, +11.0%])\\n  CI includes 0: No → significant\\n\\n============================================================\\n  4. Six-Way Comparison Table\\n============================================================\\n\\n  Method       |  Pooled SR |  seed42 SR |  seed43 SR | Seeds\\n  -------------+------------+------------+------------+------\\n  obs_only     |     19.0% |     19.0% |        N/A |     1\\n  argmin       |     12.0% |     12.0% |        N/A |     1\\n  perdof       |     11.0% |     11.0% |        N/A |     1\\n  vla_only     |     12.0% |     12.0% |        N/A |     1\\n  vla_mean     |     12.0% |     12.0% |        N/A |     1\\n  scalar       |      9.0% |      9.0% |        N/A |     1\\n\\n============================================================\\n  5. Pairwise Fisher Tests: obs_only vs Each Baseline\\n============================================================\\n\\n  Bonferroni correction: 5 comparisons, α_adj = 0.0100\\n\\n  Comparison                     |  p-value |    p_adj |     OR |      h |   Sig?\\n  -------------------------------+----------+----------+--------+--------+-------\\n  obs_only vs argmin             |   0.2408 |   1.0000 |  1.720 | +0.195 |     No\\n  obs_only vs perdof             |   0.1649 |   0.8247 |  1.898 | +0.226 |     No\\n  obs_only vs vla_only           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No\\n  obs_only vs vla_mean           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No\\n  obs_only vs scalar             |   0.0652 |   0.3261 |  2.372 | +0.293 |     No\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.57}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "f0a6a910-75d7-4c73-be44-273b4a75c29c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\n============================================================\\\\n  LIBERO-Object 6-Method Statistical Analysis\\\\n============================================================\\\\nMode: seed=42 only\\\\nSeeds available per method:\\\\n  obs_only    : 1 seed(s)\\\\n  argmin      : 1 seed(s)\\\\n  perdof      : 1 seed(s)\\\\n  vla_only    : 1 seed(s)\\\\n  vla_mean    : 1 seed(s)\\\\n  scalar      : 1 seed(s)\\\\n\\\\n============================================================\\\\n  1. Pooled Fisher Exact Test: obs_only vs argmin\\\\n============================================================\\\\n\\\\n  obs_only: 19/100 = 19.0%\\\\n  argmin:   12/100 = 12.0%\\\\n\\\\n  2x2 contingency table:\\\\n              success  failure\\\\n  obs_only         19       81\\\\n  argmin           12       88\\\\n\\\\n  Fisher exact p-value (two-sided): 0.2408\\\\n  Odds ratio: 1.720\\\\n  Cohen's h: 0.195\\\\n  Interpretation: Not significant (p>=0.05)\\\\n\\\\n============================================================\\\\n  2. Per-Seed Fisher Exact Test: obs_only vs argmin\\\\n============================================================\\\\n\\\\n  seed42:\\\\n    obs_only: 19/100 = 19.0%\\\\n    argmin:   12/100 = 12.0%\\\\n    Fisher p = 0.2408, OR = 1.720, h = 0.195\\\\n\\\\n============================================================\\\\n  3. Bootstrap CI for SR Difference (obs_only - argmin)\\\\n============================================================\\\\n\\\\n  Task-level resampling, 10 tasks, 10000 bootstrap iterations\\\\n  Mean difference: +0.0702 (+7.0%)\\\\n  95% CI: [+0.0300, +0.1100] ([+3.0%, +11.0%])\\\\n  CI includes 0: No → significant\\\\n\\\\n============================================================\\\\n  4. Six-Way Comparison Table\\\\n============================================================\\\\n\\\\n  Method       |  Pooled SR |  seed42 SR |  seed43 SR | Seeds\\\\n  -------------+------------+------------+------------+------\\\\n  obs_only     |     19.0% |     19.0% |        N/A |     1\\\\n  argmin       |     12.0% |     12.0% |        N/A |     1\\\\n  perdof       |     11.0% |     11.0% |        N/A |     1\\\\n  vla_only     |     12.0% |     12.0% |        N/A |     1\\\\n  vla_mean     |     12.0% |     12.0% |        N/A |     1\\\\n  scalar       |      9.0% |      9.0% |        N/A |     1\\\\n\\\\n============================================================\\\\n  5. Pairwise Fisher Tests: obs_only vs Each Baseline\\\\n============================================================\\\\n\\\\n  Bonferroni correction: 5 comparisons, α_adj = 0.0100\\\\n\\\\n  Comparison                     |  p-value |    p_adj |     OR |      h |   Sig?\\\\n  -------------------------------+----------+----------+--------+--------+-------\\\\n  obs_only vs argmin             |   0.2408 |   1.0000 |  1.720 | +0.195 |     No\\\\n  obs_only vs perdof             |   0.1649 |   0.8247 |  1.898 | +0.226 |     No\\\\n  obs_only vs vla_only           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No\\\\n  obs_only vs vla_mean           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No\\\\n  obs_only vs scalar             |   0.0652 |   0.3261 |  2.372 | +0.293 |     No\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.57}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  LIBERO-Object 6-Method Statistical Analysis\\n============================================================\\nMode: seed=42 only\\nSeeds available per method:\\n  obs_only    : 1 seed(s)\\n  argmin      : 1 seed(s)\\n  perdof      : 1 seed(s)\\n  vla_only    : 1 seed(s)\\n  vla_mean    : 1 seed(s)\\n  scalar      : 1 seed(s)\\n\\n============================================================\\n  1. Pooled Fisher Exact Test: obs_only vs argmin\\n============================================================\\n\\n  obs_only: 19/100 = 19.0%\\n  argmin:   12/100 = 12.0%\\n\\n  2x2 contingency table:\\n              success  failure\\n  obs_only         19       81\\n  argmin           12       88\\n\\n  Fisher exact p-value (two-sided): 0.2408\\n  Odds ratio: 1.720\\n  Cohen's h: 0.195\\n  Interpretation: Not significant (p>=0.05)\\n\\n============================================================\\n  2. Per-Seed Fisher Exact Test: obs_only vs argmin\\n============================================================\\n\\n  seed42:\\n    obs_only: 19/100 = 19.0%\\n    argmin:   12/100 = 12.0%\\n    Fisher p = 0.2408, OR = 1.720, h = 0.195\\n\\n============================================================\\n  3. Bootstrap CI for SR Difference (obs_only - argmin)\\n============================================================\\n\\n  Task-level resampling, 10 tasks, 10000 bootstrap iterations\\n  Mean difference: +0.0702 (+7.0%)\\n  95% CI: [+0.0300, +0.1100] ([+3.0%, +11.0%])\\n  CI includes 0: No → significant\\n\\n============================================================\\n  4. Six-Way Comparison Table\\n============================================================\\n\\n  Method       |  Pooled SR |  seed42 SR |  seed43 SR | Seeds\\n  -------------+------------+------------+------------+------\\n  obs_only     |     19.0% |     19.0% |        N/A |     1\\n  argmin       |     12.0% |     12.0% |        N/A |     1\\n  perdof       |     11.0% |     11.0% |        N/A |     1\\n  vla_only     |     12.0% |     12.0% |        N/A |     1\\n  vla_mean     |     12.0% |     12.0% |        N/A |     1\\n  scalar       |      9.0% |      9.0% |        N/A |     1\\n\\n============================================================\\n  5. Pairwise Fisher Tests: obs_only vs Each Baseline\\n============================================================\\n\\n  Bonferroni correction: 5 comparisons, α_adj = 0.0100\\n\\n  Comparison                     |  p-value |    p_adj |     OR |      h |   Sig?\\n  -------------------------------+----------+----------+--------+--------+-------\\n  obs_only vs argmin             |   0.2408 |   1.0000 |  1.720 | +0.195 |     No\\n  obs_only vs perdof             |   0.1649 |   0.8247 |  1.898 | +0.226 |     No\\n  obs_only vs vla_only           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No\\n  obs_only vs vla_mean           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No\\n  obs_only vs scalar             |   0.0652 |   0.3261 |  2.372 | +0.293 |     No\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.57}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

dry-run 完成，输出如下：

```
============================================================
  LIBERO-Object 6-Method Statistical Analysis
============================================================
Mode: seed=42 only
Seeds available per method:
  obs_only    : 1 seed(s)
  argmin      : 1 seed(s)
  perdof      : 1 seed(s)
  vla_only    : 1 seed(s)
  vla_mean    : 1 seed(s)
  scalar      : 1 seed(s)

============================================================
  1. Pooled Fisher Exact Test: obs_only vs argmin
============================================================

  obs_only: 19/100 = 19.0%
  argmin:   12/100 = 12.0%

  2x2 contingency table:
              success  failure
  obs_only         19       81
  argmin           12       88

  Fisher exact p-value (two-sided): 0.2408
  Odds ratio: 1.720
  Cohen's h: 0.195

  Interpretation: Not significant (p>=0.05)

============================================================
  2. Per-Seed Fisher Exact Test: obs_only vs argmin
============================================================

  seed42:
    obs_only: 19/100 = 19.0%
    argmin:   12/100 = 12.0%
    Fisher p = 0.2408, OR = 1.720, h = 0.195

============================================================
  3. Bootstrap CI for SR Difference (obs_only - argmin)
============================================================

  Task-level resampling, 10 tasks, 10000 bootstrap iterations
  Mean difference: +0.0702 (+7.0%)
  95% CI: [+0.0300, +0.1100] ([+3.0%, +11.0%])
  CI includes 0: No → significant

============================================================
  4. Six-Way Comparison Table
============================================================

  Method       |  Pooled SR |  seed42 SR |  seed43 SR | Seeds
  -------------+------------+------------+------------+------
  obs_only     |     19.0% |     19.0% |        N/A |     1
  argmin       |     12.0% |     12.0% |        N/A |     1
  perdof       |     11.0% |     11.0% |        N/A |     1
  vla_only     |     12.0% |     12.0% |        N/A |     1
  vla_mean     |     12.0% |     12.0% |        N/A |     1
  scalar       |      9.0% |      9.0% |        N/A |     1

============================================================
  5. Pairwise Fisher Tests: obs_only vs Each Baseline
============================================================

  Bonferroni correction: 5 comparisons, α_adj = 0.0100

  Comparison                     |  p-value |    p_adj |     OR |      h |   Sig?
  -------------------------------+----------+----------+--------+--------+-------
  obs_only vs argmin             |   0.2408 |   1.0000 |  1.720 | +0.195 |     No
  obs_only vs perdof             |   0.1649 |   0.8247 |  1.898 | +0.226 |     No
  obs_only vs vla_only           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No
  obs_only vs vla_mean           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No
  obs_only vs scalar             |   0.0652 |   0.3261 |  2.372 | +0.293 |     No
```

**验证结果**:
- 5 个 section 全部正常输出
- Pooled Fisher p=0.2408，符合预期范围（19% vs 12%, n=100, 预期 p≈0.17-0.25）
- Bootstrap CI [+3.0%, +11.0%] 不含 0 — task-level resampling 比 Fisher 更敏感，因为它保留了 task 间方差结构
- Six-way table 数值正确（obs_only 19%, scalar 最低 9%）
- Bonferroni 校正后所有比较均不显著（单 seed 100 trials power 不够）

seed=43 数据到齐后填入 `SEED43` dict 即可，不需改代码逻辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "uuid": "c1a28a71-11ef-49c8-b81b-f356ecd808c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUhPYWAFXM2NjcKuTh2VsN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1261,
      "cache_read_input_tokens": 30651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1261
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

_source line 16_

dry-run 完成，输出如下：

```
============================================================
  LIBERO-Object 6-Method Statistical Analysis
============================================================
Mode: seed=42 only
Seeds available per method:
  obs_only    : 1 seed(s)
  argmin      : 1 seed(s)
  perdof      : 1 seed(s)
  vla_only    : 1 seed(s)
  vla_mean    : 1 seed(s)
  scalar      : 1 seed(s)

============================================================
  1. Pooled Fisher Exact Test: obs_only vs argmin
============================================================

  obs_only: 19/100 = 19.0%
  argmin:   12/100 = 12.0%

  2x2 contingency table:
              success  failure
  obs_only         19       81
  argmin           12       88

  Fisher exact p-value (two-sided): 0.2408
  Odds ratio: 1.720
  Cohen's h: 0.195

  Interpretation: Not significant (p>=0.05)

============================================================
  2. Per-Seed Fisher Exact Test: obs_only vs argmin
============================================================

  seed42:
    obs_only: 19/100 = 19.0%
    argmin:   12/100 = 12.0%
    Fisher p = 0.2408, OR = 1.720, h = 0.195

============================================================
  3. Bootstrap CI for SR Difference (obs_only - argmin)
============================================================

  Task-level resampling, 10 tasks, 10000 bootstrap iterations
  Mean difference: +0.0702 (+7.0%)
  95% CI: [+0.0300, +0.1100] ([+3.0%, +11.0%])
  CI includes 0: No → significant

============================================================
  4. Six-Way Comparison Table
============================================================

  Method       |  Pooled SR |  seed42 SR |  seed43 SR | Seeds
  -------------+------------+------------+------------+------
  obs_only     |     19.0% |     19.0% |        N/A |     1
  argmin       |     12.0% |     12.0% |        N/A |     1
  perdof       |     11.0% |     11.0% |        N/A |     1
  vla_only     |     12.0% |     12.0% |        N/A |     1
  vla_mean     |     12.0% |     12.0% |        N/A |     1
  scalar       |      9.0% |      9.0% |        N/A |     1

============================================================
  5. Pairwise Fisher Tests: obs_only vs Each Baseline
============================================================

  Bonferroni correction: 5 comparisons, α_adj = 0.0100

  Comparison                     |  p-value |    p_adj |     OR |      h |   Sig?
  -------------------------------+----------+----------+--------+--------+-------
  obs_only vs argmin             |   0.2408 |   1.0000 |  1.720 | +0.195 |     No
  obs_only vs perdof             |   0.1649 |   0.8247 |  1.898 | +0.226 |     No
  obs_only vs vla_only           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No
  obs_only vs vla_mean           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No
  obs_only vs scalar             |   0.0652 |   0.3261 |  2.372 | +0.293 |     No
```

**验证结果**:
- 5 个 section 全部正常输出
- Pooled Fisher p=0.2408，符合预期范围（19% vs 12%, n=100, 预期 p≈0.17-0.25）
- Bootstrap CI [+3.0%, +11.0%] 不含 0 — task-level resampling 比 Fisher 更敏感，因为它保留了 task 间方差结构
- Six-way table 数值正确（obs_only 19%, scalar 最低 9%）
- Bonferroni 校正后所有比较均不显著（单 seed 100 trials power 不够）

seed=43 数据到齐后填入 `SEED43` dict 即可，不需改代码逻辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 89042,
  "duration_api_ms": 87255,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "dc3540fd-16bb-41d5-9523-a93017ebed7d",
  "total_cost_usd": 0.3536027500000001,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 20071,
    "cache_read_input_tokens": 118196,
    "output_tokens": 6654,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 20071,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1162,
        "cache_read_input_tokens": 30651,
        "cache_creation_input_tokens": 1261,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1261
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2596,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0026709999999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 6654,
      "cacheReadInputTokens": 118196,
      "cacheCreationInputTokens": 20071,
      "webSearchRequests": 0,
      "costUSD": 0.35093175,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fc3c7fc0-ab57-46fb-a3d4-5590086e131a"
}
```

</details>

---
