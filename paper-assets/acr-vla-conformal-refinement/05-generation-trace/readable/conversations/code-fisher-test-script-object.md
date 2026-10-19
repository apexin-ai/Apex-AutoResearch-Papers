# code fisher test script object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_code_fisher-test-script-object_20260515T204705.jsonl`
- **Structured JSON:** [`523ae24f6d761557b992.json`](../../sessions/52/523ae24f6d761557b992.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-15T20:48:44.266431+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fisher-test-script-object_20260515T204705",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T20:48:44.266748+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fisher-test-script-object_20260515T204705",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T20:48:44.266931+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_fisher-test-script-object_20260515T204705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "mkdir -p /root/acr-vla-conformal-refinement/analysis",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T20:48:44.267082+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fisher-test-script-object_20260515T204705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T20:48:44.267316+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_fisher-test-script-object_20260515T204705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-18228",
    "account": "root",
    "command": "cat > /root/acr-vla-conformal-refinement/analysis/fisher_object_sixway.py << 'SCRIPTEOF'\n#!/usr/bin/env python3\n\"\"\"Fisher exact test + bootstrap CI for LIBERO-Object 6-method comparison.\n\nCompares obs_only (ACR) vs 5 baselines across 10 OBJECT tasks.\nEach task has 10 trials per seed. Supports seed=42 alone or pooled seed=42+43.\n\nUsage:\n    python fisher_object_sixway.py                  # use all available seeds\n    python fisher_object_sixway.py --seed42-only    # dry-run with seed=42 only\n    python fisher_object_sixway.py --output-json results.json\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport sys\nfrom collections import OrderedDict\n\nimport numpy as np\nfrom scipy.stats import fisher_exact\n\nTASKS = [\n    \"alphabet_soup\", \"cream_cheese\", \"salad_dressing\", \"bbq_sauce\", \"ketchup\",\n    \"tomato_sauce\", \"butter\", \"milk\", \"chocolate_pudding\", \"orange_juice\",\n]\n\nMETHODS = [\"obs_only\", \"argmin\", \"perdof\", \"vla_only\", \"vla_mean\", \"scalar\"]\nTRIALS_PER_TASK = 10\n\nSEED42 = {\n    \"obs_only\":  {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3},\n    \"argmin\":    {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0.0, \"tomato_sauce\": 0.0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3},\n    \"perdof\":    {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.0, \"tomato_sauce\": 0.0, \"butter\": 0.1, \"milk\": 0.0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3},\n    \"vla_only\":  {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.0, \"tomato_sauce\": 0.1, \"butter\": 0.0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3},\n    \"vla_mean\":  {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.0, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1},\n    \"scalar\":    {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.0, \"tomato_sauce\": 0.0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2},\n}\n\nSEED43 = {\n    \"obs_only\":  None,\n    \"argmin\":    None,\n    \"perdof\":    None,\n    \"vla_only\":  {\"alphabet_soup\": 0.0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0.0, \"tomato_sauce\": 0.0, \"butter\": 0.0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2},\n    \"vla_mean\":  None,\n    \"scalar\":    None,\n}\n\n\ndef sr_to_counts(sr_dict):\n    \"\"\"Convert per-task SR dict to (total_success, total_trials).\"\"\"\n    s = sum(round(sr_dict[t] * TRIALS_PER_TASK) for t in TASKS)\n    n = len(TASKS) * TRIALS_PER_TASK\n    return s, n\n\n\ndef per_task_successes(sr_dict):\n    \"\"\"Return list of per-task success counts.\"\"\"\n    return [round(sr_dict[t] * TRIALS_PER_TASK) for t in TASKS]\n\n\ndef cohens_h(p1, p2):\n    return 2 * math.asin(math.sqrt(p1)) - 2 * math.asin(math.sqrt(p2))\n\n\ndef get_pooled_counts(method, seed42_only=False):\n    \"\"\"Get pooled (success, trials) across available seeds.\"\"\"\n    s42, n42 = sr_to_counts(SEED42[method])\n    total_s, total_n = s42, n42\n    if not seed42_only and SEED43[method] is not None:\n        s43, n43 = sr_to_counts(SEED43[method])\n        total_s += s43\n        total_n += n43\n    return total_s, total_n\n\n\ndef fisher_2x2(s1, n1, s2, n2):\n    \"\"\"Run Fisher exact test on 2x2 table. Returns (odds_ratio, p_value, table).\"\"\"\n    table = np.array([[s1, n1 - s1], [s2, n2 - s2]])\n    odds, p = fisher_exact(table, alternative='two-sided')\n    return odds, p, table\n\n\ndef bootstrap_sr_diff(method_a, method_b, seed42_only=False, n_boot=10000, rng_seed=0):\n    \"\"\"Bootstrap CI for SR difference (method_a - method_b) via task-level resampling.\"\"\"\n    rng = np.random.RandomState(rng_seed)\n\n    succ_a, succ_b = [], []\n    # seed42\n    succ_a.append(per_task_successes(SEED42[method_a]))\n    succ_b.append(per_task_successes(SEED42[method_b]))\n    # seed43\n    if not seed42_only:\n        if SEED43[method_a] is not None and SEED43[method_b] is not None:\n            succ_a.append(per_task_successes(SEED43[method_a]))\n            succ_b.append(per_task_successes(SEED43[method_b]))\n\n    succ_a = np.concatenate(succ_a)  # shape: (n_tasks_total,)\n    succ_b = np.concatenate(succ_b)\n    n_tasks = len(succ_a)\n\n    diffs = np.empty(n_boot)\n    for i in range(n_boot):\n        idx = rng.randint(0, n_tasks, size=n_tasks)\n        sr_a = succ_a[idx].sum() / (n_tasks * TRIALS_PER_TASK)\n        sr_b = succ_b[idx].sum() / (n_tasks * TRIALS_PER_TASK)\n        diffs[i] = sr_a - sr_b\n\n    ci_lo, ci_hi = np.percentile(diffs, [2.5, 97.5])\n    mean_diff = diffs.mean()\n    return mean_diff, ci_lo, ci_hi, n_tasks\n\n\ndef print_header(title):\n    print(f\"\\n{'='*60}\")\n    print(f\"  {title}\")\n    print(f\"{'='*60}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Fisher exact test + bootstrap CI for LIBERO-Object\")\n    parser.add_argument(\"--seed42-only\", action=\"store_true\", help=\"Only use seed=42 data\")\n    parser.add_argument(\"--output-json\", type=str, default=None, help=\"Output JSON file path\")\n    args = parser.parse_args()\n\n    results = {}\n\n    # Count available seeds per method\n    seeds_used = {}\n    for m in METHODS:\n        n_seeds = 1\n        if not args.seed42_only and SEED43[m] is not None:\n            n_seeds = 2\n        seeds_used[m] = n_seeds\n\n    print_header(\"LIBERO-Object 6-Method Statistical Analysis\")\n    mode = \"seed=42 only\" if args.seed42_only else \"all available seeds\"\n    print(f\"Mode: {mode}\")\n    print(f\"Seeds available per method:\")\n    for m in METHODS:\n        print(f\"  {m:12s}: {seeds_used[m]} seed(s)\")\n\n    # ── Section 1: Pooled Fisher exact test (obs_only vs argmin) ──\n    print_header(\"1. Pooled Fisher Exact Test: obs_only vs argmin\")\n\n    s_obs, n_obs = get_pooled_counts(\"obs_only\", args.seed42_only)\n    s_arg, n_arg = get_pooled_counts(\"argmin\", args.seed42_only)\n    odds, p, table = fisher_2x2(s_obs, n_obs, s_arg, n_arg)\n    h = cohens_h(s_obs / n_obs, s_arg / n_arg)\n\n    print(f\"\\n  obs_only: {s_obs}/{n_obs} = {s_obs/n_obs:.1%}\")\n    print(f\"  argmin:   {s_arg}/{n_arg} = {s_arg/n_arg:.1%}\")\n    print(f\"\\n  2x2 contingency table:\")\n    print(f\"              success  failure\")\n    print(f\"  obs_only    {table[0,0]:>7.0f}  {table[0,1]:>7.0f}\")\n    print(f\"  argmin      {table[1,0]:>7.0f}  {table[1,1]:>7.0f}\")\n    print(f\"\\n  Fisher exact p-value (two-sided): {p:.4f}\")\n    print(f\"  Odds ratio: {odds:.3f}\")\n    print(f\"  Cohen's h: {h:.3f}\")\n    print(f\"  Interpretation: {'Significant (p<0.05)' if p < 0.05 else 'Not significant (p>=0.05)'}\")\n\n    results[\"pooled_fisher\"] = {\n        \"obs_only\": {\"success\": int(s_obs), \"trials\": int(n_obs), \"sr\": round(s_obs/n_obs, 4)},\n        \"argmin\": {\"success\": int(s_arg), \"trials\": int(n_arg), \"sr\": round(s_arg/n_arg, 4)},\n        \"p_value\": round(p, 6), \"odds_ratio\": round(odds, 4), \"cohens_h\": round(h, 4),\n    }\n\n    # ── Section 2: Per-seed Fisher exact test ──\n    print_header(\"2. Per-Seed Fisher Exact Test: obs_only vs argmin\")\n    results[\"per_seed_fisher\"] = {}\n\n    for seed_name, seed_data in [(\"seed42\", SEED42), (\"seed43\", SEED43)]:\n        if args.seed42_only and seed_name == \"seed43\":\n            continue\n        if seed_data[\"obs_only\"] is None or seed_data[\"argmin\"] is None:\n            print(f\"\\n  {seed_name}: SKIPPED (data not available)\")\n            results[\"per_seed_fisher\"][seed_name] = \"not_available\"\n            continue\n\n        s1, n1 = sr_to_counts(seed_data[\"obs_only\"])\n        s2, n2 = sr_to_counts(seed_data[\"argmin\"])\n        odds_s, p_s, table_s = fisher_2x2(s1, n1, s2, n2)\n        h_s = cohens_h(s1/n1, s2/n2)\n\n        print(f\"\\n  {seed_name}:\")\n        print(f\"    obs_only: {s1}/{n1} = {s1/n1:.1%}\")\n        print(f\"    argmin:   {s2}/{n2} = {s2/n2:.1%}\")\n        print(f\"    Fisher p = {p_s:.4f}, OR = {odds_s:.3f}, h = {h_s:.3f}\")\n\n        results[\"per_seed_fisher\"][seed_name] = {\n            \"obs_only_sr\": round(s1/n1, 4), \"argmin_sr\": round(s2/n2, 4),\n            \"p_value\": round(p_s, 6), \"odds_ratio\": round(odds_s, 4), \"cohens_h\": round(h_s, 4),\n        }\n\n    # ── Section 3: Bootstrap CI ──\n    print_header(\"3. Bootstrap CI for SR Difference (obs_only - argmin)\")\n\n    mean_d, ci_lo, ci_hi, n_tasks_boot = bootstrap_sr_diff(\n        \"obs_only\", \"argmin\", seed42_only=args.seed42_only\n    )\n    print(f\"\\n  Task-level resampling, {n_tasks_boot} tasks, 10000 bootstrap iterations\")\n    print(f\"  Mean difference: {mean_d:+.4f} ({mean_d:+.1%})\")\n    print(f\"  95% CI: [{ci_lo:+.4f}, {ci_hi:+.4f}] ([{ci_lo:+.1%}, {ci_hi:+.1%}])\")\n    ci_includes_zero = ci_lo <= 0 <= ci_hi\n    print(f\"  CI includes 0: {'Yes → not significant' if ci_includes_zero else 'No → significant'}\")\n\n    results[\"bootstrap_ci\"] = {\n        \"mean_diff\": round(float(mean_d), 6), \"ci_lo\": round(float(ci_lo), 6),\n        \"ci_hi\": round(float(ci_hi), 6), \"n_tasks\": n_tasks_boot,\n        \"ci_includes_zero\": bool(ci_includes_zero),\n    }\n\n    # ── Section 4: Six-way comparison table ──\n    print_header(\"4. Six-Way Comparison Table\")\n    print(f\"\\n  {'Method':12s} | {'Pooled SR':>10s} | {'seed42 SR':>10s} | {'seed43 SR':>10s} | {'Seeds':>5s}\")\n    print(f\"  {'-'*12}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*5}\")\n\n    results[\"sixway_table\"] = {}\n    for m in METHODS:\n        s42, n42 = sr_to_counts(SEED42[m])\n        sr42 = s42 / n42\n\n        sp, np_ = get_pooled_counts(m, args.seed42_only)\n        sr_pooled = sp / np_\n\n        if not args.seed42_only and SEED43[m] is not None:\n            s43, n43 = sr_to_counts(SEED43[m])\n            sr43_str = f\"{s43/n43:.1%}\"\n            sr43_val = round(s43/n43, 4)\n        else:\n            sr43_str = \"N/A\"\n            sr43_val = None\n\n        print(f\"  {m:12s} | {sr_pooled:>9.1%} | {sr42:>9.1%} | {sr43_str:>10s} | {seeds_used[m]:>5d}\")\n\n        results[\"sixway_table\"][m] = {\n            \"pooled_sr\": round(sr_pooled, 4), \"seed42_sr\": round(sr42, 4),\n            \"seed43_sr\": sr43_val, \"n_seeds\": seeds_used[m],\n        }\n\n    # ── Section 5: All pairwise Fisher tests ──\n    print_header(\"5. Pairwise Fisher Tests: obs_only vs Each Baseline\")\n    n_comparisons = len(METHODS) - 1\n    print(f\"\\n  Bonferroni correction: {n_comparisons} comparisons, α_adj = {0.05/n_comparisons:.4f}\")\n    print(f\"\\n  {'Comparison':30s} | {'p-value':>8s} | {'p_adj':>8s} | {'OR':>6s} | {'h':>6s} | {'Sig?':>6s}\")\n    print(f\"  {'-'*30}-+-{'-'*8}-+-{'-'*8}-+-{'-'*6}-+-{'-'*6}-+-{'-'*6}\")\n\n    results[\"pairwise\"] = {}\n    for m in METHODS:\n        if m == \"obs_only\":\n            continue\n        s_m, n_m = get_pooled_counts(m, args.seed42_only)\n        odds_m, p_m, _ = fisher_2x2(s_obs, n_obs, s_m, n_m)\n        h_m = cohens_h(s_obs / n_obs, s_m / n_m)\n        p_adj = min(p_m * n_comparisons, 1.0)\n        sig = \"Yes\" if p_adj < 0.05 else \"No\"\n\n        label = f\"obs_only vs {m}\"\n        print(f\"  {label:30s} | {p_m:>8.4f} | {p_adj:>8.4f} | {odds_m:>6.3f} | {h_m:>+6.3f} | {sig:>6s}\")\n\n        results[\"pairwise\"][m] = {\n            \"p_value\": round(p_m, 6), \"p_adjusted\": round(p_adj, 6),\n            \"odds_ratio\": round(odds_m, 4), \"cohens_h\": round(h_m, 4),\n            \"significant_bonferroni\": p_adj < 0.05,\n        }\n\n    print()\n\n    # JSON output\n    if args.output_json:\n        with open(args.output_json, 'w') as f:\n            json.dump(results, f, indent=2)\n        print(f\"Results saved to {args.output_json}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPTEOF"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T20:48:44.267611+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fisher-test-script-object_20260515T204705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T20:48:44.267761+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_fisher-test-script-object_20260515T204705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-18228",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/analysis && python fisher_object_sixway.py --seed42-only"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T20:48:44.267944+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  LIBERO-Object 6-Method Statistical Analysis\\n============================================================\\nMode: seed=42 only\\nSeeds available per method:\\n  obs_only    : 1 seed(s)\\n  argmin      : 1 seed(s)\\n  perdof      : 1 seed(s)\\n  vla_only    : 1 seed(s)\\n  vla_mean    : 1 seed(s)\\n  scalar      : 1 seed(s)\\n\\n============================================================\\n  1. Pooled Fisher Exact Test: obs_only vs argmin\\n============================================================\\n\\n  obs_only: 19/100 = 19.0%\\n  argmin:   12/100 = 12.0%\\n\\n  2x2 contingency table:\\n              success  failure\\n  obs_only         19       81\\n  argmin           12       88\\n\\n  Fisher exact p-value (two-sided): 0.2408\\n  Odds ratio: 1.720\\n  Cohen's h: 0.195\\n  Interpretation: Not significant (p>=0.05)\\n\\n============================================================\\n  2. Per-Seed Fisher Exact Test: obs_only vs argmin\\n============================================================\\n\\n  seed42:\\n    obs_only: 19/100 = 19.0%\\n    argmin:   12/100 = 12.0%\\n    Fisher p = 0.2408, OR = 1.720, h = 0.195\\n\\n============================================================\\n  3. Bootstrap CI for SR Difference (obs_only - argmin)\\n============================================================\\n\\n  Task-level resampling, 10 tasks, 10000 bootstrap iterations\\n  Mean difference: +0.0702 (+7.0%)\\n  95% CI: [+0.0300, +0.1100] ([+3.0%, +11.0%])\\n  CI includes 0: No → significant\\n\\n============================================================\\n  4. Six-Way Comparison Table\\n============================================================\\n\\n  Method       |  Pooled SR |  seed42 SR |  seed43 SR | Seeds\\n  -------------+------------+------------+------------+------\\n  obs_only     |     19.0% |     19.0% |        N/A |     1\\n  a
…[truncated 1250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fisher-test-script-object_20260515T204705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-15T20:48:44.268158+00:00_

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
  "session": "worker_code_fisher-test-script-object_20260515T204705"
}
```

</details>

---
