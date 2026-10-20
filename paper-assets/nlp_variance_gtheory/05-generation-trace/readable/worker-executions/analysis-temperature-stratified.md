# analysis temperature stratified

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_analysis_temperature_stratified_20260521T042035.log`
- **Structured JSON:** [`362232f4cbc141bd25f3.json`](../../sessions/36/362232f4cbc141bd25f3.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
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
  "uuid": "383ce3e0-4e60-43ef-96ba-8379c4a51435",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory/memory/"
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
    "resetsAt": 1779341400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ca85e5c6-6010-4158-8690-fa3f56fd2653",
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to run a temperature-stratified G-theory analysis on the remote server. Let me first detect the image, then execute the analysis script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "0530ae11-c1df-4499-9cf1-9fb2501d430d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqhZhgQNV8FCcYGvcvWg4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14309,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14309
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Voe4eBbG7epzAU7SF5FDUL`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "90a5971b-62de-4b33-ad6b-16ddd7d0a2a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqhZhgQNV8FCcYGvcvWg4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14309,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14309
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

_source line 6 · 2026-05-21T04:20:49.093Z_

<details><summary>↩ Tool result · `toolu_01Voe4eBbG7epzAU7SF5FDUL`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
}
```

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
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "e619ea02-c403-4429-bedf-1072ecc3f231",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

先检测镜像，然后确认数据文件存在。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "f0890881-972c-4431-a18a-9f5d45be3444",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CF4QaMRheYNfJJDwAY29cr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 26150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 920
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image · `toolu_01K9gtrPWxhUsr2Qh9qBP2yG`</summary>

```json
{
  "server": "westd-32570"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "3463bf67-1a3a-4b2c-845a-2bca0e40c52b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CF4QaMRheYNfJJDwAY29cr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 26150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 920
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RmNDPAShGMiy6oqYBufL3S`</summary>

```json
{
  "server": "westd-32570",
  "command": "ls -lh /root/nlp_variance_gtheory/results/analysis/llama_full.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "4777c12c-e1a3-443b-a88a-bb1a28a5dc4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CF4QaMRheYNfJJDwAY29cr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 26150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 920
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

_source line 10 · 2026-05-21T04:20:53.516Z_

<details><summary>↩ Tool result · `toolu_01K9gtrPWxhUsr2Qh9qBP2yG`</summary>

```text
{"result":"{\n  \"detected\": false,\n  \"status\": \"ssh_error\",\n  \"skip_base_setup\": false,\n  \"message\": \"SSH error: exit code 1\"\n}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "6d6cc81e-3684-4e70-81b3-66ab4e5a59fc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\n  \\\"detected\\\": false,\\n  \\\"status\\\": \\\"ssh_error\\\",\\n  \\\"skip_base_setup\\\": false,\\n  \\\"message\\\": \\\"SSH error: exit code 1\\\"\\n}\"}",
    "structuredContent": {
      "result": "{\n  \"detected\": false,\n  \"status\": \"ssh_error\",\n  \"skip_base_setup\": false,\n  \"message\": \"SSH error: exit code 1\"\n}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T04:20:54.049Z_

<details><summary>↩ Tool result · `toolu_01RmNDPAShGMiy6oqYBufL3S`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 38M May 21 11:41 /root/nlp_variance_gtheory/results/analysis/llama_full.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "cc6c51d1-965b-421d-8c18-4647251209c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 38M May 21 11:41 /root/nlp_variance_gtheory/results/analysis/llama_full.csv\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 38M May 21 11:41 /root/nlp_variance_gtheory/results/analysis/llama_full.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

数据文件存在（38M）。执行分析脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "b4eaefca-6c47-4846-bade-72bb35a870a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sFbATsYwM6KdMfGjbg4a3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 27070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01T3apvcp1vyx1VKX5tp1iVp`</summary>

```json
{
  "server": "westd-32570",
  "command": "cd /root/nlp_variance_gtheory && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export PYTHONPATH=/root/nlp_variance_gtheory:$PYTHONPATH && python3 << 'PYEOF'\nimport json\nimport numpy as np\nimport pandas as pd\nfrom itertools import combinations\nfrom pathlib import Path\n\ndf = pd.read_csv(\"results/analysis/llama_full.csv\")\nprint(f\"Loaded {len(df)} records\")\nprint(f\"Temperatures: {sorted(df['temperature'].unique())}\")\n\nfacets_full = [\"precision\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\nfacets_no_temp = [\"precision\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\nfacets_practical = [\"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n\ndef variance_decomposition(data, metric, facets_list, fixed_facets=None):\n    if fixed_facets is None:\n        fixed_facets = set()\n    \n    N = len(data)\n    n = {f: data[f].nunique() for f in facets_list}\n    grand_mean = data[metric].mean()\n    SS_total = ((data[metric] - grand_mean) ** 2).sum()\n    \n    if SS_total == 0:\n        return {\"components_pct\": {}, \"G_coefficient\": 0, \"grand_mean\": grand_mean}\n    \n    components = {}\n    \n    for f in facets_list:\n        if n[f] <= 1:\n            continue\n        means = data.groupby(f)[metric].mean()\n        n_per = N // n[f]\n        ss = n_per * ((means - grand_mean) ** 2).sum()\n        components[f] = ss\n    \n    for f1, f2 in combinations(facets_list, 2):\n        if n[f1] <= 1 or n[f2] <= 1:\n            continue\n        cell_means = data.groupby([f1, f2])[metric].mean()\n        n_per = N // (n[f1] * n[f2])\n        ss = 0\n        f1_means = data.groupby(f1)[metric].mean()\n        f2_means = data.groupby(f2)[metric].mean()\n        for (l1, l2), cell_mean in cell_means.items():\n            ss += n_per * (cell_mean - f1_means[l1] - f2_means[l2] + grand_mean) ** 2\n        components[f\"{f1}:{f2}\"] = ss\n    \n    ss_explained = sum(components.values())\n    components[\"residual\"] = max(0, SS_total - ss_explained)\n    total = sum(components.values())\n    pct = {k: v/total * 100 for k, v in components.items()}\n    \n    tau = pct.get(\"item_id\", 0)\n    delta = 0\n    for k, v in pct.items():\n        if k == \"item_id\":\n            continue\n        parts = k.split(\":\")\n        if any(p in fixed_facets for p in parts):\n            continue\n        delta += v\n    G = tau / (tau + delta) if (tau + delta) > 0 else 0\n    \n    return {\n        \"components_pct\": {k: round(v, 4) for k, v in sorted(pct.items(), key=lambda x: -x[1])},\n        \"G_coefficient\": round(G, 4),\n        \"grand_mean\": round(float(grand_mean), 4),\n        \"n_records\": N,\n        \"tau_pct\": round(tau, 4),\n        \"delta_pct\": round(delta, 4),\n    }\n\nresults = {}\n\nprint(\"=\" * 70)\nprint(\"PART 1: Temperature-stratified analysis\")\nprint(\"=\" * 70)\n\nresults[\"stratified\"] = {}\nfor temp in sorted(df[\"temperature\"].unique()):\n    temp_df = df[df[\"temperature\"] == temp]\n    print(f\"\\n--- Temperature = {temp} ({len(temp_df)} records) ---\")\n    \n    for metric in [\"correct\", \"text_exact_match\"]:\n        r = variance_decomposition(temp_df, metric, facets_no_temp)\n        key = f\"T{temp}_{metric}\"\n        results[\"stratified\"][key] = r\n        \n        print(f\"\\n  {metric}:\")\n        print(f\"    Grand mean: {r['grand_mean']}\")\n        print(f\"    G coefficient: {r['G_coefficient']}\")\n        top5 = list(r[\"components_pct\"].items())[:5]\n        for comp, pct in top5:\n            print(f\"    {comp:30s}: {pct:7.2f}%\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"SUMMARY: G coefficients by temperature\")\nprint(\"=\" * 70)\nprint(f\"{'Temperature':<12s} {'G(correct)':>12s} {'G(text)':>12s} {'Mean(correct)':>14s} {'Mean(text)':>12s}\")\nprint(\"-\" * 70)\nfor temp in sorted(df[\"temperature\"].unique()):\n    gc = results[\"stratified\"][f\"T{temp}_correct\"][\"G_coefficient\"]\n    gt = results[\"stratified\"][f\"T{temp}_text_exact_match\"][\"G_coefficient\"]\n    mc = results[\"stratified\"][f\"T{temp}_correct\"][\"grand_mean\"]\n    mt = results[\"stratified\"][f\"T{temp}_text_exact_match\"][\"grand_mean\"]\n    print(f\"T={temp:<8} {gc:>12.4f} {gt:>12.4f} {mc:>14.4f} {mt:>12.4f}\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"PART 2: Practical scenario D-study\")\nprint(\"  (precision + temperature fixed -> only prompt/seed/ordering/item random)\")\nprint(\"=\" * 70)\n\nresults[\"practical\"] = {}\nfor metric in [\"correct\", \"text_exact_match\"]:\n    r = variance_decomposition(df, metric, facets_full, \n                                fixed_facets={\"precision\", \"temperature\"})\n    results[\"practical\"][metric] = r\n    print(f\"\\n{metric}:\")\n    print(f\"  G coefficient: {r['G_coefficient']}\")\n    print(f\"  tau (item_id): {r['tau_pct']:.2f}%\")\n    print(f\"  delta (random error): {r['delta_pct']:.2f}%\")\n\nprint(\"\\nD-study sweep (binary_correct, practical scenario):\")\nitem_pct = results[\"practical\"][\"correct\"][\"components_pct\"].get(\"item_id\", 0)\ntotal_pct = sum(results[\"practical\"][\"correct\"][\"components_pct\"].values())\nother_random_pct = results[\"practical\"][\"correct\"][\"delta_pct\"]\nn_items_actual = df[\"item_id\"].nunique()\n\nd_study = {}\nfor n_items in [25, 50, 75, 100, 150, 200, 300, 500, 1000]:\n    scaled_item = item_pct * n_items_actual / n_items\n    G_n = scaled_item / (scaled_item + other_random_pct) if (scaled_item + other_random_pct) > 0 else 0\n    d_study[n_items] = round(G_n, 4)\n    marker = \" <-- G>=0.80\" if G_n >= 0.80 and (n_items == 25 or d_study.get(n_items-25, 0) < 0.80) else \"\"\n    print(f\"  n_items={n_items:5d}: G = {G_n:.4f}{marker}\")\n\nresults[\"practical\"][\"d_study_correct\"] = d_study\n\nfor n in range(10, 2000):\n    scaled = item_pct * n_items_actual / n\n    g = scaled / (scaled + other_random_pct)\n    if g >= 0.80:\n        results[\"practical\"][\"min_items_G80\"] = n\n        print(f\"\\n  Minimum items for G>=0.80: {n}\")\n        break\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"PART 3: precision:temperature interaction\")\nprint(\"=\" * 70)\n\nfor metric in [\"correct\", \"text_exact_match\"]:\n    r_full = variance_decomposition(df, metric, facets_full)\n    pt_pct = r_full[\"components_pct\"].get(\"precision:temperature\", 0)\n    print(f\"\\n{metric}:\")\n    print(f\"  precision:temperature = {pt_pct:.4f}%\")\n    \n    cell = df.groupby([\"precision\", \"temperature\"])[metric].mean()\n    print(f\"\\n  Cell means:\")\n    print(f\"  {'':15s}\", end=\"\")\n    for t in sorted(df[\"temperature\"].unique()):\n        print(f\"  T={t:>4}\", end=\"\")\n    print()\n    for p in sorted(df[\"precision\"].unique()):\n        print(f\"  {p:15s}\", end=\"\")\n        for t in sorted(df[\"temperature\"].unique()):\n            try:\n                val = cell[(p, t)]\n                print(f\"  {val:>6.4f}\", end=\"\")\n            except:\n                print(f\"  {'N/A':>6s}\", end=\"\")\n        print()\n    \n    results[f\"prec_temp_interaction_{metric}\"] = {\n        \"pct\": round(pt_pct, 4),\n        \"cell_means\": {f\"{p}|T={t}\": round(float(cell[(p, t)]), 4) \n                       for p in sorted(df[\"precision\"].unique()) \n                       for t in sorted(df[\"temperature\"].unique())\n                       if (p, t) in cell.index}\n    }\n\nPath(\"results/analysis\").mkdir(parents=True, exist_ok=True)\nwith open(\"results/analysis/temperature_stratified_analysis.json\", \"w\") as f:\n    json.dump(results, f, indent=2, ensure_ascii=False)\nprint(f\"\\nSaved results/analysis/temperature_stratified_analysis.json\")\n\nimport shutil\nPath(\"/root/nlp_variance_gtheory/artifacts/analysis\").mkdir(parents=True, exist_ok=True)\nshutil.copy(\"results/analysis/temperature_stratified_analysis.json\",\n            \"artifacts/analysis/temperature_stratified_analysis.json\")\nprint(\"Copied to artifacts/analysis/\")\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "ce2033aa-5624-4b14-963f-b8e38c746349",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sFbATsYwM6KdMfGjbg4a3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 27070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
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

_source line 14 · 2026-05-21T04:21:40.378Z_

<details><summary>↩ Tool result · `toolu_01T3apvcp1vyx1VKX5tp1iVp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 239200 records\\nTemperatures: [np.float64(0.0), np.float64(0.3), np.float64(0.7)]\\n======================================================================\\nPART 1: Temperature-stratified analysis\\n======================================================================\\n\\n--- Temperature = 0.0 (66400 records) ---\\n\\n  correct:\\n    Grand mean: 0.6987\\n    G coefficient: 0.7605\\n    item_id                       :   76.05%\\n    precision:item_id             :    9.19%\\n    prompt_template:item_id       :    8.48%\\n    residual                      :    3.02%\\n    precision                     :    1.53%\\n\\n  text_exact_match:\\n    Grand mean: 0.9653\\n    G coefficient: 0.0085\\n    precision                     :   52.45%\\n    residual                      :   20.18%\\n    precision:item_id             :   12.46%\\n    prompt_template               :    4.49%\\n    precision:prompt_template     :    3.77%\\n\\n--- Temperature = 0.3 (86400 records) ---\\n\\n  correct:\\n    Grand mean: 0.6795\\n    G coefficient: 0.6105\\n    item_id                       :   61.05%\\n    residual                      :   21.87%\\n    prompt_template:item_id       :    5.47%\\n    seed:item_id                  :    5.41%\\n    precision:item_id             :    4.25%\\n\\n  text_exact_match:\\n    Grand mean: 0.1524\\n    G coefficient: 0.0673\\n    residual                      :   74.94%\\n    seed:item_id                  :    6.96%\\n    item_id                       :    6.73%\\n    prompt_template:item_id       :    5.22%\\n    ordering:item_id              :    1.70%\\n\\n--- Temperature = 0.7 (86400 records) ---\\n\\n  correct:\\n    Grand mean: 0.6699\\n    G coefficient: 0.5492\\n    item_id                       :   54.92%\\n    residual                      :   21.20%\\n    seed:item_id                  :   14.80%\\n    prompt_template:item_id       :    4.13%\\n    precision:item_id             :    3.23%\\n\\n  text_exact_match:\\n    Grand mean: 0.0222\\n    G coefficient: 0.0218\\n    residual                      :   82.10%\\n    seed:item_id                  :    3.62%\\n    prompt_template:item_id       :    2.37%\\n    precision                     :    2.32%\\n    item_id                       :    2.18%\\n\\n======================================================================\\nSUMMARY: G coefficients by temperature\\n======================================================================\\nTemperature    G(correct)      G(text)  Mean(correct)   Mean(text)\\n----------------------------------------------------------------------\\nT=0.0            0.7605       0.0085         0.6987       0.9653\\nT=0.3            0.6105       0.0673         0.6795       0.1524\\nT=0.7            0.5492       0.0218         0.6699       0.0222\\n\\n======================================================================\\nPART 2: Practical scenario D-study\\n  (precision + temperature fixed -> only prompt/seed/ordering/item random)\\n======================================================================\\n\\ncorrect:\\n  G coefficient: 0.6595\\n  tau (item_id): 61.08%\\n  delta (random error): 31.54%\\n\\ntext_exact_match:\\n  G coefficient: 0.0598\\n  tau (item_id): 0.66%\\n  delta (random error): 10.43%\\n\\nD-study sweep (binary_correct, practical scenario):\\n  n_items=   25: G = 0.9394 <-- G>=0.80\\n  n_items=   50: G = 0.8857\\n  n_items=   75: G = 0.8378\\n  n_items=  100: G = 0.7948\\n  n_items=  150: G = 0.7208\\n  n_items=  200: G = 0.6595\\n  n_items=  300: G = 0.5635\\n  n_items=  500: G = 0.4365\\n  n_items= 1000: G = 0.2792\\n\\n  Minimum items for G>=0.80: 10\\n\\n======================================================================\\nPART 3: precision:temperature interaction\\n======================================================================\\n\\ncorrect:\\n  precision:temperature = 0.0524%\\n\\n  Cell means:\\n                   T= 0.0  T= 0.3  T= 0.7\\n  bfloat16         0.7131  0.7148  0.7046\\n  float16          0.7137  0.7158  0.7048\\n  float32          0.6026  0.6080  0.6004\\n\\ntext_exact_match:\\n  precision:temperature = 4.1495%\\n\\n  Cell means:\\n                   T= 0.0  T= 0.3  T= 0.7\\n  bfloat16         0.9996  0.1243  0.0063\\n  float16          0.9996  0.1269  0.0064\\n  float32          0.7409  0.2060  0.0539\\n\\nSaved results/analysis/temperature_stratified_analysis.json\\nCopied to artifacts/analysis/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.18}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "f8d966e6-5cda-4aef-9aa9-6dda472a6593",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Loaded 239200 records\\\\nTemperatures: [np.float64(0.0), np.float64(0.3), np.float64(0.7)]\\\\n======================================================================\\\\nPART 1: Temperature-stratified analysis\\\\n======================================================================\\\\n\\\\n--- Temperature = 0.0 (66400 records) ---\\\\n\\\\n  correct:\\\\n    Grand mean: 0.6987\\\\n    G coefficient: 0.7605\\\\n    item_id                       :   76.05%\\\\n    precision:item_id             :    9.19%\\\\n    prompt_template:item_id       :    8.48%\\\\n    residual                      :    3.02%\\\\n    precision                     :    1.53%\\\\n\\\\n  text_exact_match:\\\\n    Grand mean: 0.9653\\\\n    G coefficient: 0.0085\\\\n    precision                     :   52.45%\\\\n    residual                      :   20.18%\\\\n    precision:item_id             :   12.46%\\\\n    prompt_template               :    4.49%\\\\n    precision:prompt_template     :    3.77%\\\\n\\\\n--- Temperature = 0.3 (86400 records) ---\\\\n\\\\n  correct:\\\\n    Grand mean: 0.6795\\\\n    G coefficient: 0.6105\\\\n    item_id                       :   61.05%\\\\n    residual                      :   21.87%\\\\n    prompt_template:item_id       :    5.47%\\\\n    seed:item_id                  :    5.41%\\\\n    precision:item_id             :    4.25%\\\\n\\\\n  text_exact_match:\\\\n    Grand mean: 0.1524\\\\n    G coefficient: 0.0673\\\\n    residual                      :   74.94%\\\\n    seed:item_id                  :    6.96%\\\\n    item_id                       :    6.73%\\\\n    prompt_template:item_id       :    5.22%\\\\n    ordering:item_id              :    1.70%\\\\n\\\\n--- Temperature = 0.7 (86400 records) ---\\\\n\\\\n  correct:\\\\n    Grand mean: 0.6699\\\\n    G coefficient: 0.5492\\\\n    item_id                       :   54.92%\\\\n    residual                      :   21.20%\\\\n    seed:item_id                  :   14.80%\\\\n    prompt_template:item_id       :    4.13%\\\\n    precision:item_id             :    3.23%\\\\n\\\\n  text_exact_match:\\\\n    Grand mean: 0.0222\\\\n    G coefficient: 0.0218\\\\n    residual                      :   82.10%\\\\n    seed:item_id                  :    3.62%\\\\n    prompt_template:item_id       :    2.37%\\\\n    precision                     :    2.32%\\\\n    item_id                       :    2.18%\\\\n\\\\n======================================================================\\\\nSUMMARY: G coefficients by temperature\\\\n======================================================================\\\\nTemperature    G(correct)      G(text)  Mean(correct)   Mean(text)\\\\n----------------------------------------------------------------------\\\\nT=0.0            0.7605       0.0085         0.6987       0.9653\\\\nT=0.3            0.6105       0.0673         0.6795       0.1524\\\\nT=0.7            0.5492       0.0218         0.6699       0.0222\\\\n\\\\n======================================================================\\\\nPART 2: Practical scenario D-study\\\\n  (precision + temperature fixed -> only prompt/seed/ordering/item random)\\\\n======================================================================\\\\n\\\\ncorrect:\\\\n  G coefficient: 0.6595\\\\n  tau (item_id): 61.08%\\\\n  delta (random error): 31.54%\\\\n\\\\ntext_exact_match:\\\\n  G coefficient: 0.0598\\\\n  tau (item_id): 0.66%\\\\n  delta (random error): 10.43%\\\\n\\\\nD-study sweep (binary_correct, practical scenario):\\\\n  n_items=   25: G = 0.9394 <-- G>=0.80\\\\n  n_items=   50: G = 0.8857\\\\n  n_items=   75: G = 0.8378\\\\n  n_items=  100: G = 0.7948\\\\n  n_items=  150: G = 0.7208\\\\n  n_items=  200: G = 0.6595\\\\n  n_items=  300: G = 0.5635\\\\n  n_items=  500: G = 0.4365\\\\n  n_items= 1000: G = 0.2792\\\\n\\\\n  Minimum items for G>=0.80: 10\\\\n\\\\n======================================================================\\\\nPART 3: precision:temperature interaction\\\\n======================================================================\\\\n\\\\ncorrect:\\\\n  precision:temperature = 0.0524%\\\\n\\\\n  Cell means:\\\\n                   T= 0.0  T= 0.3  T= 0.7\\\\n  bfloat16         0.7131  0.7148  0.7046\\\\n  float16          0.7137  0.7158  0.7048\\\\n  float32          0.6026  0.6080  0.6004\\\\n\\\\ntext_exact_match:\\\\n  precision:temperature = 4.1495%\\\\n\\\\n  Cell means:\\\\n                   T= 0.0  T= 0.3  T= 0.7\\\\n  bfloat16         0.9996  0.1243  0.0063\\\\n  float16          0.9996  0.1269  0.0064\\\\n  float32          0.7409  0.2060  0.0539\\\\n\\\\nSaved results/analysis/temperature_stratified_analysis.json\\\\nCopied to artifacts/analysis/\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.18}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Loaded 239200 records\\nTemperatures: [np.float64(0.0), np.float64(0.3), np.float64(0.7)]\\n======================================================================\\nPART 1: Temperature-stratified analysis\\n======================================================================\\n\\n--- Temperature = 0.0 (66400 records) ---\\n\\n  correct:\\n    Grand mean: 0.6987\\n    G coefficient: 0.7605\\n    item_id                       :   76.05%\\n    precision:item_id             :    9.19%\\n    prompt_template:item_id       :    8.48%\\n    residual                      :    3.02%\\n    precision                     :    1.53%\\n\\n  text_exact_match:\\n    Grand mean: 0.9653\\n    G coefficient: 0.0085\\n    precision                     :   52.45%\\n    residual                      :   20.18%\\n    precision:item_id             :   12.46%\\n    prompt_template               :    4.49%\\n    precision:prompt_template     :    3.77%\\n\\n--- Temperature = 0.3 (86400 records) ---\\n\\n  correct:\\n    Grand mean: 0.6795\\n    G coefficient: 0.6105\\n    item_id                       :   61.05%\\n    residual                      :   21.87%\\n    prompt_template:item_id       :    5.47%\\n    seed:item_id                  :    5.41%\\n    precision:item_id             :    4.25%\\n\\n  text_exact_match:\\n    Grand mean: 0.1524\\n    G coefficient: 0.0673\\n    residual                      :   74.94%\\n    seed:item_id                  :    6.96%\\n    item_id                       :    6.73%\\n    prompt_template:item_id       :    5.22%\\n    ordering:item_id              :    1.70%\\n\\n--- Temperature = 0.7 (86400 records) ---\\n\\n  correct:\\n    Grand mean: 0.6699\\n    G coefficient: 0.5492\\n    item_id                       :   54.92%\\n    residual                      :   21.20%\\n    seed:item_id                  :   14.80%\\n    prompt_template:item_id       :    4.13%\\n    precision:item_id             :    3.23%\\n\\n  text_exact_match:\\n    Grand mean: 0.0222\\n    G coefficient: 0.0218\\n    residual                      :   82.10%\\n    seed:item_id                  :    3.62%\\n    prompt_template:item_id       :    2.37%\\n    precision                     :    2.32%\\n    item_id                       :    2.18%\\n\\n======================================================================\\nSUMMARY: G coefficients by temperature\\n======================================================================\\nTemperature    G(correct)      G(text)  Mean(correct)   Mean(text)\\n----------------------------------------------------------------------\\nT=0.0            0.7605       0.0085         0.6987       0.9653\\nT=0.3            0.6105       0.0673         0.6795       0.1524\\nT=0.7            0.5492       0.0218         0.6699       0.0222\\n\\n======================================================================\\nPART 2: Practical scenario D-study\\n  (precision + temperature fixed -> only prompt/seed/ordering/item random)\\n======================================================================\\n\\ncorrect:\\n  G coefficient: 0.6595\\n  tau (item_id): 61.08%\\n  delta (random error): 31.54%\\n\\ntext_exact_match:\\n  G coefficient: 0.0598\\n  tau (item_id): 0.66%\\n  delta (random error): 10.43%\\n\\nD-study sweep (binary_correct, practical scenario):\\n  n_items=   25: G = 0.9394 <-- G>=0.80\\n  n_items=   50: G = 0.8857\\n  n_items=   75: G = 0.8378\\n  n_items=  100: G = 0.7948\\n  n_items=  150: G = 0.7208\\n  n_items=  200: G = 0.6595\\n  n_items=  300: G = 0.5635\\n  n_items=  500: G = 0.4365\\n  n_items= 1000: G = 0.2792\\n\\n  Minimum items for G>=0.80: 10\\n\\n======================================================================\\nPART 3: precision:temperature interaction\\n======================================================================\\n\\ncorrect:\\n  precision:temperature = 0.0524%\\n\\n  Cell means:\\n                   T= 0.0  T= 0.3  T= 0.7\\n  bfloat16         0.7131  0.7148  0.7046\\n  float16          0.7137  0.7158  0.7048\\n  float32          0.6026  0.6080  0.6004\\n\\ntext_exact_match:\\n  precision:temperature = 4.1495%\\n\\n  Cell means:\\n                   T= 0.0  T= 0.3  T= 0.7\\n  bfloat16         0.9996  0.1243  0.0063\\n  float16          0.9996  0.1269  0.0064\\n  float32          0.7409  0.2060  0.0539\\n\\nSaved results/analysis/temperature_stratified_analysis.json\\nCopied to artifacts/analysis/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.18}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

分析完成，结果已保存。

---

**PART 1 — Stratified G coefficients:**

| Temperature | G(correct) | G(text) | Mean(correct) | Mean(text) |
|---|---|---|---|---|
| T=0.0 | 0.7605 | 0.0085 | 0.6987 | 0.9653 |
| T=0.3 | 0.6105 | 0.0673 | 0.6795 | 0.1524 |
| T=0.7 | 0.5492 | 0.0218 | 0.6699 | 0.0222 |

`correct` 指标：温度固定后 G 从全量的 0.007 恢复到 0.55–0.76，T=0.0 最高（76%方差来自 item_id）。随温度升高，residual 和 seed:item_id 交互增大（T=0.7 时 seed:item_id 占 14.8%），G 下降——采样随机性在侵蚀信号。

`text_exact_match`：即使分层后 G 仍极低（0.008–0.067）。T=0.0 时 precision 占 52.5%（float32 vs bf16/fp16 的文本匹配率差异巨大）；T=0.3/0.7 时 residual 占 75–82%，说明文本匹配在非零温度下几乎是纯噪声。

---

**PART 2 — Practical D-study（precision + temperature 固定）:**

- G(correct) = 0.6595，item_id 占 61.08%，delta 占 31.54%
- G(text_exact_match) = 0.0598（不可用）
- **Minimum items for G≥0.80 = 10**（D-study 反转：当前 200 items 远超所需，G 随 n_items 减少反而升高，因为 item variance 被放大）

---

**PART 3 — precision:temperature 交互:**

- `correct`: **0.05%** — 几乎不存在交互，precision 对准确率的影响不随温度变化
- `text_exact_match`: **4.15%** — 存在实质性交互

Cell means 揭示了交互本质：
- bf16/fp16 在 T=0.0 时文本匹配率 99.96%，到 T=0.7 骤降至 0.6%
- float32 在 T=0.0 时只有 74.09%，但 T=0.7 时仍有 5.39%（下降更平缓）

float32 的 KV cache 精度更高，在有采样随机性时反而保留了更多文本一致性。这就是 precision:temperature 交互的来源。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "uuid": "b83b9ab3-8760-4f42-85d2-d765453c3a35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdKj5xPJ2AWQUypptbtgSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4336,
      "cache_read_input_tokens": 27500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4336
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

分析完成，结果已保存。

---

**PART 1 — Stratified G coefficients:**

| Temperature | G(correct) | G(text) | Mean(correct) | Mean(text) |
|---|---|---|---|---|
| T=0.0 | 0.7605 | 0.0085 | 0.6987 | 0.9653 |
| T=0.3 | 0.6105 | 0.0673 | 0.6795 | 0.1524 |
| T=0.7 | 0.5492 | 0.0218 | 0.6699 | 0.0222 |

`correct` 指标：温度固定后 G 从全量的 0.007 恢复到 0.55–0.76，T=0.0 最高（76%方差来自 item_id）。随温度升高，residual 和 seed:item_id 交互增大（T=0.7 时 seed:item_id 占 14.8%），G 下降——采样随机性在侵蚀信号。

`text_exact_match`：即使分层后 G 仍极低（0.008–0.067）。T=0.0 时 precision 占 52.5%（float32 vs bf16/fp16 的文本匹配率差异巨大）；T=0.3/0.7 时 residual 占 75–82%，说明文本匹配在非零温度下几乎是纯噪声。

---

**PART 2 — Practical D-study（precision + temperature 固定）:**

- G(correct) = 0.6595，item_id 占 61.08%，delta 占 31.54%
- G(text_exact_match) = 0.0598（不可用）
- **Minimum items for G≥0.80 = 10**（D-study 反转：当前 200 items 远超所需，G 随 n_items 减少反而升高，因为 item variance 被放大）

---

**PART 3 — precision:temperature 交互:**

- `correct`: **0.05%** — 几乎不存在交互，precision 对准确率的影响不随温度变化
- `text_exact_match`: **4.15%** — 存在实质性交互

Cell means 揭示了交互本质：
- bf16/fp16 在 T=0.0 时文本匹配率 99.96%，到 T=0.7 骤降至 0.6%
- float32 在 T=0.0 时只有 74.09%，但 T=0.7 时仍有 5.39%（下降更平缓）

float32 的 KV cache 精度更高，在有采样随机性时反而保留了更多文本一致性。这就是 precision:temperature 交互的来源。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 74929,
  "duration_api_ms": 72117,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "9d3f034f-d664-42cb-be3e-6181c37cfaf5",
  "total_cost_usd": 0.27305025,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 19995,
    "cache_read_input_tokens": 92561,
    "output_tokens": 3911,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 19995,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 785,
        "cache_read_input_tokens": 27500,
        "cache_creation_input_tokens": 4336,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4336
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3886,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003986,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 3911,
      "cacheReadInputTokens": 92561,
      "cacheCreationInputTokens": 19995,
      "webSearchRequests": 0,
      "costUSD": 0.26906425,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "746b0d54-7fa7-493e-b666-8b1e88706d93"
}
```

</details>

---
