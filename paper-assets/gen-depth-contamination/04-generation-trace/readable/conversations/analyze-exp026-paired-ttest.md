# analyze exp026 paired ttest

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analyze_exp026-paired-ttest_20260518T114213.jsonl`
- **Structured JSON:** [`7d38a35574e295b66ccd.json`](../../sessions/7d/7d38a35574e295b66ccd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-18T11:43:47.456997+00:00_

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
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
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

_source line 2 · 2026-05-18T11:43:47.457320+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T11:43:47.457505+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/ -name eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/ -name eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T11:43:47.457672+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/no_filter_seed42/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/binary_seed42/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/graduated_a09_seed42/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/binary_seed123/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/graduated_a09_seed123/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/no_filter_seed123/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/binary_seed456/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/binary_seed789/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/no_filter_seed456/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/graduated_a09_seed456/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/binary_seed1024/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/graduated_a09_seed789/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/no_filter_seed789/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/graduated_a09_seed1024/eval_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/no_filter_seed1024/eval_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T11:43:47.457856+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/no_filter_seed42/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/no_filter_seed42/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T11:43:47.458209+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scores\\\": {\\n    \\\"mmlu\\\": 0.5887337986041874,\\n    \\\"hellaswag\\\": 0.6602270464050985\\n  },\\n  \\\"full\\\": {\\n    \\\"mmlu_abstract_algebra\\\": {\\n      \\\"name\\\": \\\"mmlu_abstract_algebra\\\",\\n      \\\"alias\\\": \\\"abstract_algebra\\\",\\n      \\\"sample_len\\\": 100,\\n      \\\"acc,none\\\": 0.35,\\n      \\\"acc_stderr,none\\\": 0.04793724854411023\\n    },\\n    \\\"mmlu_anatomy\\\": {\\n      \\\"name\\\": \\\"mmlu_anatomy\\\",\\n      \\\"alias\\\": \\\"anatomy\\\",\\n      \\\"sample_len\\\": 135,\\n      \\\"acc,none\\\": 0.4740740740740741,\\n      \\\"acc_stderr,none\\\": 0.043135316967505756\\n    },\\n    \\\"mmlu_astronomy\\\": {\\n      \\\"name\\\": \\\"mmlu_astronomy\\\",\\n      \\\"alias\\\": \\\"astronomy\\\",\\n      \\\"sample_len\\\": 152,\\n      \\\"acc,none\\\": 0.6973684210526315,\\n      \\\"acc_stderr,none\\\": 0.03738520676119667\\n    },\\n    \\\"mmlu_college_biology\\\": {\\n      \\\"name\\\": \\\"mmlu_college_biology\\\",\\n      \\\"alias\\\": \\\"college_biology\\\",\\n      \\\"sample_len\\\": 144,\\n      \\\"acc,none\\\": 0.6666666666666666,\\n      \\\"acc_stderr,none\\\": 0.03942082639927217\\n    },\\n    \\\"mmlu_college_chemistry\\\": {\\n      \\\"name\\\": \\\"mmlu_college_chemistry\\\",\\n      \\\"alias\\\": \\\"college_chemistry\\\",\\n      \\\"sample_len\\\": 100,\\n      \\\"acc,none\\\": 0.4,\\n      \\\"acc_stderr,none\\\": 0.0492365963917331\\n    },\\n    \\\"mmlu_college_computer_science\\\": {\\n      \\\"name\\\": \\\"mmlu_college_computer_science\\\",\\n      \\\"alias\\\": \\\"college_computer_science\\\",\\n      \\\"sample_len\\\": 100,\\n      \\\"acc,none\\\": 0.42,\\n      \\\"acc_stderr,none\\\": 0.04960449637488583\\n    },\\n    \\\"mmlu_college_mathematics\\\": {\\n      \\\"name\\\": \\\"mmlu_college_mathematics\\\",\\n      \\\"alias\\\": \\\"college_mathematics\\\",\\n      \\\"sample_len\\\": 100,\\
…[truncated 8491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T11:43:47.458438+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat << 'PYEOF' | python3 -\nimport json, os, itertools\nimport numpy as np\nfrom scipy import stats\n\nbase = \"/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering\"\nstrategies = [\"graduated_a09\", \"binary\", \"no_filter\"]\nseeds = [42, 123, 456, 789, 1024]\nmetrics = [\"mmlu\", \"hellaswag\"]\n\n# Load all data\ndata = {}\nfor strat in strategies:\n    data[strat] = {}\n    for seed in seeds:\n        path = os.path.join(base, f\"{strat}_seed{seed}\", \"eval_results.json\")\n        with open(path) as f:\n            d = json.load(f)\n        data[strat][seed] = {m: d[\"scores\"][m] for m in metrics}\n\n# Print raw data\nprint(\"=\" * 80)\nprint(\"RAW SCORES\")\nprint(\"=\" * 80)\nfor strat in strategies:\n    for m in metrics:\n        vals = [data[strat][s][m] for s in seeds]\n        print(f\"{strat:>15} | {m:>10} | seeds: {['%.6f' % v for v in vals]} | mean={np.mean(vals):.6f} std={np.std(vals, ddof=1):.6f}\")\n\n# Paired t-tests for all pairs\npairs = list(itertools.combinations(strategies, 2))\nn_comparisons = len(pairs) * len(metrics)  # 6\nbonferroni_alpha = 0.05 / n_comparisons\n\nprint(f\"\\n{'=' * 80}\")\nprint(f\"PAIRED T-TESTS (df=4, two-tailed, Bonferroni alpha = 0.05/{n_comparisons} = {bonferroni_alpha:.4f})\")\nprint(f\"{'=' * 80}\")\n\nresults = []\nfor (s1, s2) in pairs:\n    for m in metrics:\n        a = np.array([data[s1][seed][m] for seed in seeds])\n        b = np.array([data[s2][seed][m] for seed in seeds])\n        diff = a - b\n        mean_diff = np.mean(diff)\n        std_diff = np.std(diff, ddof=1)\n        se_diff = std_diff / np.sqrt(len(diff))\n        \n        t_stat, p_val = stats.ttest_rel(a, b)\n        df = len(diff) - 1\n        \n        # 95% CI\n        t_crit = stats.t.ppf(0.975, df)\n        ci_low = mean_diff - t_crit * se_diff\n        ci_high = mean_diff + t_crit * se_diff\n        \n        # Cohen's d (for paired: mean_diff / std_diff)\n        cohens_d = mean_diff / std_diff if std_diff > 0 else 0.0\n        \n        sig = \"YES\" if p_val < 0.05 else \"NO\"\n        sig_bonf = \"YES\" if p_val < bonferroni_alpha else \"NO\"\n        \n        results.append({\n            \"pair\": f\"{s1} vs {s2}\",\n            \"metric\": m,\n            \"mean_diff\": mean_diff,\n            \"std_diff\": std_diff,\n            \"t_stat\": t_stat,\n            \"df\": df,\n            \"p_val\": p_val,\n            \"ci_low\": ci_low,\n            \"ci_high\": ci_high,\n            \"cohens_d\": cohens_d,\n            \"sig_005\": sig,\n            \"sig_bonf\": sig_bonf,\n        })\n        \n        print(f\"\\n--- {s1} vs {s2} | {m} ---\")\n        print(f\"  Mean diff:  {mean_diff:+.6f} (±{std_diff:.6f})\")\n        print(f\"  t({df}) = {t_stat:.4f}, p = {p_val:.6f}\")\n        print(f\"  95% CI:     [{ci_low:+.6f}, {ci_high:+.6f}]\")\n        print(f\"  Cohen's d:  {cohens_d:.4f}\")\n        print(f\"  Sig (p<.05): {sig}  |  Sig (Bonferroni p<{bonferroni_alpha:.4f}): {sig_bonf}\")\n\n# Summary table\nprint(f\"\\n{'=' * 80}\")\nprint(\"SUMMARY TABLE\")\nprint(f\"{'=' * 80}\")\nheader = f\"{'Comparison':<30} {'Metric':<12} {'Mean Diff':>12} {'Std':>10} {'t(4)':>8} {'p-value':>10} {'95% CI':>28} {'d':>8} {'Sig':>5} {'Bonf':>5}\"\nprint(header)\nprint(\"-\" * len(header))\nfor r in results:\n    ci_str = f\"[{r['ci_low']:+.6f}, {r['ci_high']:+.6f}]\"\n    print(f\"{r['pair']:<30} {r['metric']:<12} {r['mean_diff']:>+12.6f} {r['std_diff']:>10.6f} {r['t_stat']:>8.4f} {r['p_val']:>10.6f} {ci_str:>28} {r['cohens_d']:>8.4f} {r['sig_005']:>5} {r['sig_bonf']:>5}\")\n\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat << 'PYEOF' | python3 -\nimport json, os, itertools\nimport numpy as np\nfrom scipy import stats\n\nbase = \"/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering\"\nstrategies = [\"graduated_a09\", \"binary\", \"no_filter\"]\nseeds = [42, 123, 456, 789, 1024]\nmetrics = [\"mmlu\", \"hellaswag\"]\n\n# Load all data\ndata = {}\nfor strat in strategies:\n    data[strat] = {}\n    for seed in seeds:\n        path = os.path.join(base, f\"{strat}_seed{seed}\", \"eval_results.json\")\n        with open(path) as f:\n            d = json.load(f)\n        data[strat][seed] = {m: d[\"scores\"][m] for m in metrics}\n\n# Print raw data\nprint(\"=\" * 80)\nprint(\"RAW SCORES\")\nprint(\"=\" * 80)\nfor strat in strategies:\n    for m in metrics:\n        vals = [data[strat][s][m] for s in seeds]\n        print(f\"{strat:>15} | {m:>10} | seeds: {['%.6f' % v for v in vals]} | mean={np.mean(vals):.6f} std={np.std(vals, ddof=1):.6f}\")\n\n# Paired t-tests for all pairs\npairs = list(itertools.combinations(strategies, 2))\nn_comparisons = len(pairs) * len(metrics)  # 6\nbonferroni_alpha = 0.05 / n_comparisons\n\nprint(f\"\\n{'=' * 80}\")\nprint(f\"PAIRED T-TESTS (df=4, two-tailed, Bonferroni alpha = 0.05/{n_comparisons} = {bonferroni_alpha:.4f})\")\nprint(f\"{'=' * 80}\")\n\nresults = []\nfor (s1, s2) in pairs:\n    for m in metrics:\n        a = np.array([data[s1][seed][m] for seed in seeds])\n        b = np.array([data[s2][seed][m] for seed in seeds])\n        diff = a - b\n        mean_diff = np.mean(diff)\n        std_diff = np.std(diff, ddof=1)\n        se_diff = std_diff / np.sqrt(len(diff))\n        \n        t_stat, p_val = stats.ttest_rel(a, b)\n        df = len(diff) - 1\n        \n        # 95% CI\n        t_crit = stats.t.ppf(0.975, df)\n        ci_low = mean_diff - t_crit * se_diff\n        ci_high = mean_diff + t_crit * se_diff\n        \n        # Cohen's d (for paired: mean_diff / std_diff)\n        cohens_d = mean_diff / std_diff if std_diff > 0 else 0.0\n        \n        sig = \"YES\" if p_val < 0.05 else \"NO\"\n        sig_bonf = \"YES\" if p_val < bonferroni_alpha else \"NO\"\n        \n        results.append({\n            \"pair\": f\"{s1} vs {s2}\",\n            \"metric\": m,\n            \"mean_diff\": mean_diff,\n            \"std_diff\": std_diff,\n            \"t_stat\": t_stat,\n            \"df\": df,\n            \"p_val\": p_val,\n            \"ci_low\": ci_low,\n            \"ci_high\": ci_high,\n            \"cohens_d\": cohens_d,\n            \"sig_005\": sig,\n            \"sig_bonf\": sig_bonf,\n        })\n        \n        print(f\"\\n--- {s1} vs {s2} | {m} ---\")\n        print(f\"  Mean diff:  {mean_diff:+.6f} (±{std_diff:.6f})\")\n        print(f\"  t({df}) = {t_stat:.4f}, p = {p_val:.6f}\")\n        print(f\"  95% CI:     [{ci_low:+.6f}, {ci_high:+.6f}]\")\n        print(f\"  Cohen's d:  {cohens_d:.4f}\")\n        print(f\"  Sig (p<.05): {sig}  |  Sig (Bonferroni p<{bonferroni_alpha:.4f}): {sig_bonf}\")\n\n# Summary table\nprint(f\"\\n{'=' * 80}\")\nprint(\"SUMMARY TABLE\")\nprint(f\"{'=' * 80}\")\nheader = f\"{'Comparison':<30} {'Metric':<12} {'Mean Diff':>12} {'Std':>10} {'t(4)':>8} {'p-value':>10} {'95% CI':>28} {'d':>8} {'Sig':>5} {'Bonf':>5}\"\nprint(header)\nprint(\"-\" * len(header))\nfor r in results:\n    ci_str = f\"[{r['ci_low']:+.6f}, {r['ci_high']:+.6f}]\"\n    print(f\"{r['pair']:<30} {r['metric']:<12} {r['mean_diff']:>+12.6f} {r['std_diff']:>10.6f} {r['t_stat']:>8.4f} {r['p_val']:>10.6f} {ci_str:>28} {r['cohens_d']:>8.4f} {r['sig_005']:>5} {r['sig_bonf']:>5}\")\n\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T11:43:47.458654+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"================================================================================\\nRAW SCORES\\n================================================================================\\n  graduated_a09 |       mmlu | seeds: ['0.588876', '0.588663', '0.590087', '0.591654', '0.590728'] | mean=0.590001 std=0.001257\\n  graduated_a09 |  hellaswag | seeds: ['0.660426', '0.659630', '0.659928', '0.659829', '0.659530'] | mean=0.659869 std=0.000349\\n         binary |       mmlu | seeds: ['0.587096', '0.588093', '0.587167', '0.587594', '0.588022'] | mean=0.587594 std=0.000464\\n         binary |  hellaswag | seeds: ['0.664111', '0.663712', '0.664907', '0.663912', '0.664111'] | mean=0.664151 std=0.000454\\n      no_filter |       mmlu | seeds: ['0.588734', '0.589304', '0.590016', '0.591084', '0.590443'] | mean=0.589916 std=0.000925\\n      no_filter |  hellaswag | seeds: ['0.660227', '0.659729', '0.660327', '0.659928', '0.659829'] | mean=0.660008 std=0.000258\\n\\n================================================================================\\nPAIRED T-TESTS (df=4, two-tailed, Bonferroni alpha = 0.05/6 = 0.0083)\\n================================================================================\\n\\n--- graduated_a09 vs binary | mmlu ---\\n  Mean diff:  +0.002407 (±0.001309)\\n  t(4) = 4.1128, p = 0.014699\\n  95% CI:     [+0.000782, +0.004032]\\n  Cohen's d:  1.8393\\n  Sig (p<.05): YES  |  Sig (Bonferroni p<0.0083): NO\\n\\n--- graduated_a09 vs binary | hellaswag ---\\n  Mean diff:  -0.004282 (±0.000503)\\n  t(4) = -19.0407, p = 0.000045\\n  95% CI:     [-0.004906, -0.003658]\\n  Cohen's d:  -8.5153\\n  Sig (p<.05): YES  |  Sig (Bonferroni p<0.0083): YES\\n\\n--- graduated_a09 vs no_filter | mmlu ---\\n  Mean diff:  +0.000085 (±0.000449)\\n  t(4) = 0.4259, p = 0.692122\\n  95% CI:     [-0.000472, +0.000643]\\n  Cohen's d:  0.1905\\n  Sig (p<.05): NO  |  Sig (Bonferroni p<0.0083): NO\\n\\n--- graduated_a09 vs no_filter | hell
…[truncated 2074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T11:43:47.458864+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_026_ttest",
  "description": "Create artifact directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_026_ttest",
    "description": "Create artifact directory"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T11:43:47.459003+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T11:43:47.459140+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_026_ttest/results_summary.md",
  "content": "# exp_026 Paired t-test Results: arXiv Filtering Strategies\n\n**Date:** 2026-05-18\n**Design:** 3 strategies (graduated_a09, binary, no_filter) × 5 seeds (42, 123, 456, 789, 1024), paired by seed\n**Metrics:** MMLU, HellaSwag\n**Correction:** Bonferroni (6 comparisons, adjusted alpha = 0.0083)\n\n## Raw Scores\n\n| Strategy | Metric | Seed 42 | Seed 123 | Seed 456 | Seed 789 | Seed 1024 | Mean | Std |\n|---|---|---|---|---|---|---|---|---|\n| graduated | MMLU | 0.5889 | 0.5887 | 0.5901 | 0.5917 | 0.5907 | 0.5900 | 0.0013 |\n| graduated | HellaSwag | 0.6604 | 0.6596 | 0.6599 | 0.6598 | 0.6595 | 0.6599 | 0.0003 |\n| binary | MMLU | 0.5871 | 0.5881 | 0.5872 | 0.5876 | 0.5880 | 0.5876 | 0.0005 |\n| binary | HellaSwag | 0.6641 | 0.6637 | 0.6649 | 0.6639 | 0.6641 | 0.6642 | 0.0005 |\n| no_filter | MMLU | 0.5887 | 0.5893 | 0.5900 | 0.5911 | 0.5904 | 0.5899 | 0.0009 |\n| no_filter | HellaSwag | 0.6602 | 0.6597 | 0.6603 | 0.6599 | 0.6598 | 0.6600 | 0.0003 |\n\n## Paired t-test Results\n\n| Comparison | Metric | Mean Diff | Std Diff | t(4) | p-value | 95% CI | Cohen's d | Sig (p<.05) | Sig (Bonferroni) |\n|---|---|---|---|---|---|---|---|---|---|\n| graduated vs binary | MMLU | +0.0024 | 0.0013 | 4.11 | 0.0147 | [+0.0008, +0.0040] | 1.84 | Yes | No |\n| graduated vs binary | HellaSwag | -0.0043 | 0.0005 | -19.04 | 0.000045 | [-0.0049, -0.0037] | -8.52 | Yes | Yes |\n| graduated vs no_filter | MMLU | +0.0001 | 0.0004 | 0.43 | 0.6921 | [-0.0005, +0.0006] | 0.19 | No | No |\n| graduated vs no_filter | HellaSwag | -0.0001 | 0.0002 | -1.36 | 0.2455 | [-0.0004, +0.0001] | -0.61 | No | No |\n| binary vs no_filter | MMLU | -0.0023 | 0.0009 | -5.67 | 0.0048 | [-0.0035, -0.0012] | -2.54 | Yes | Yes |\n| binary vs no_filter | HellaSwag | +0.0041 | 0.0003 | 32.29 | 0.000005 | [+0.0038, +0.0045] | 14.44 | Yes | Yes |\n\n## Key Findings\n\n### 1. graduated vs no_filter: No significant difference (confirmed null result)\n\n- **MMLU:** mean diff = +0.01pp, p = 0.692, d = 0.19 (negligible effect)\n- **HellaSwag:** mean diff = -0.01pp, p = 0.245, d = -0.61 (small effect, not significant)\n- Both CIs include zero. Graduated filtering is statistically indistinguishable from no filtering.\n\n### 2. binary vs no_filter: Significant difference (trade-off)\n\n- **MMLU:** binary is 0.23pp worse (p = 0.005, survives Bonferroni)\n- **HellaSwag:** binary is 0.41pp better (p < 0.00001, survives Bonferroni)\n- Binary filtering shows a statistically significant metric trade-off: it hurts MMLU but helps HellaSwag.\n\n### 3. graduated vs binary: Significant difference\n\n- **MMLU:** graduated is 0.24pp better (p = 0.015, does not survive Bonferroni)\n- **HellaSwag:** graduated is 0.43pp worse (p < 0.0001, survives Bonferroni)\n- Same trade-off pattern as binary vs no_filter, since graduated ≈ no_filter.\n\n## Interpretation\n\nGraduated arXiv filtering (alpha=0.9) has no measurable effect on either MMLU or HellaSwag compared to no filtering at all. The differences are well within noise (0.01pp on both metrics, p > 0.24). This confirms the graduated strategy is effectively a no-op at alpha=0.9.\n\nBinary filtering produces a real but small trade-off: ~0.2pp MMLU degradation for ~0.4pp HellaSwag improvement, both statistically significant after Bonferroni correction.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_026_ttest/results_summary.md",
    "content": "# exp_026 Paired t-test Results: arXiv Filtering Strategies\n\n**Date:** 2026-05-18\n**Design:** 3 strategies (graduated_a09, binary, no_filter) × 5 seeds (42, 123, 456, 789, 1024), paired by seed\n**Metrics:** MMLU, HellaSwag\n**Correction:** Bonferroni (6 comparisons, adjusted alpha = 0.0083)\n\n## Raw Scores\n\n| Strategy | Metric | Seed 42 | Seed 123 | Seed 456 | Seed 789 | Seed 1024 | Mean | Std |\n|---|---|---|---|---|---|---|---|---|\n| graduated | MMLU | 0.5889 | 0.5887 | 0.5901 | 0.5917 | 0.5907 | 0.5900 | 0.0013 |\n| graduated | HellaSwag | 0.6604 | 0.6596 | 0.6599 | 0.6598 | 0.6595 | 0.6599 | 0.0003 |\n| binary | MMLU | 0.5871 | 0.5881 | 0.5872 | 0.5876 | 0.5880 | 0.5876 | 0.0005 |\n| binary | HellaSwag | 0.6641 | 0.6637 | 0.6649 | 0.6639 | 0.6641 | 0.6642 | 0.0005 |\n| no_filter | MMLU | 0.5887 | 0.5893 | 0.5900 | 0.5911 | 0.5904 | 0.5899 | 0.0009 |\n| no_filter | HellaSwag | 0.6602 | 0.6597 | 0.6603 | 0.6599 | 0.6598 | 0.6600 | 0.0003 |\n\n## Paired t-test Results\n\n| Comparison | Metric | Mean Diff | Std Diff | t(4) | p-value | 95% CI | Cohen's d | Sig (p<.05) | Sig (Bonferroni) |\n|---|---|---|---|---|---|---|---|---|---|\n| graduated vs binary | MMLU | +0.0024 | 0.0013 | 4.11 | 0.0147 | [+0.0008, +0.0040] | 1.84 | Yes | No |\n| graduated vs binary | HellaSwag | -0.0043 | 0.0005 | -19.04 | 0.000045 | [-0.0049, -0.0037] | -8.52 | Yes | Yes |\n| graduated vs no_filter | MMLU | +0.0001 | 0.0004 | 0.43 | 0.6921 | [-0.0005, +0.0006] | 0.19 | No | No |\n| graduated vs no_filter | HellaSwag | -0.0001 | 0.0002 | -1.36 | 0.2455 | [-0.0004, +0.0001] | -0.61 | No | No |\n| binary vs no_filter | MMLU | -0.0023 | 0.0009 | -5.67 | 0.0048 | [-0.0035, -0.0012] | -2.54 | Yes | Yes |\n| binary vs no_filter | HellaSwag | +0.0041 | 0.0003 | 32.29 | 0.000005 | [+0.0038, +0.0045] | 14.44 | Yes | Yes |\n\n## Key Findings\n\n### 1. graduated vs no_filter: No significant difference (confirmed null result)\n\n- **MMLU:** mean diff = +0.01pp, p = 0.692, d = 0.19 (negligible effect)\n- **HellaSwag:** mean diff = -0.01pp, p = 0.245, d = -0.61 (small effect, not significant)\n- Both CIs include zero. Graduated filtering is statistically indistinguishable from no filtering.\n\n### 2. binary vs no_filter: Significant difference (trade-off)\n\n- **MMLU:** binary is 0.23pp worse (p = 0.005, survives Bonferroni)\n- **HellaSwag:** binary is 0.41pp better (p < 0.00001, survives Bonferroni)\n- Binary filtering shows a statistically significant metric trade-off: it hurts MMLU but helps HellaSwag.\n\n### 3. graduated vs binary: Significant difference\n\n- **MMLU:** graduated is 0.24pp better (p = 0.015, does not survive Bonferroni)\n- **HellaSwag:** graduated is 0.43pp worse (p < 0.0001, survives Bonferroni)\n- Same trade-off pattern as binary vs no_filter, since graduated ≈ no_filter.\n\n## Interpretation\n\nGraduated arXiv filtering (alpha=0.9) has no measurable effect on either MMLU or HellaSwag compared to no filtering at all. The differences are well within noise (0.01pp on both metrics, p > 0.24). This confirms the graduated strategy is effectively a no-op at alpha=0.9.\n\nBinary filtering produces a real but small trade-off: ~0.2pp MMLU degradation for ~0.4pp HellaSwag improvement, both statistically significant after Bonferroni correction.\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T11:43:47.459348+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_026_ttest/results_summary.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T11:43:47.459505+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T11:43:47.459631+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T11:43:47.459803+00:00_

完成。结果已保存到 `artifacts/exp_026_ttest/results_summary.md`。

核心结论：

**graduated vs no_filter：差异不显著（null result confirmed）**
- MMLU: +0.01pp, p=0.692, d=0.19
- HellaSwag: -0.01pp, p=0.245, d=-0.61
- 两个指标的 95% CI 都包含零

**binary vs no_filter：存在显著 trade-off**
- MMLU: -0.23pp (p=0.005, survives Bonferroni)
- HellaSwag: +0.41pp (p<0.00001, survives Bonferroni)

**graduated vs binary：显著差异（与上面同一 trade-off pattern）**
- MMLU: +0.24pp (p=0.015, 不过 Bonferroni)
- HellaSwag: -0.43pp (p<0.0001, 过 Bonferroni)

graduated (alpha=0.9) 在统计上等同于 no_filter，是个 no-op。binary filtering 有真实但很小的 MMLU/HellaSwag trade-off。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_exp026-paired-ttest_20260518T114213"
}
```

</details>

---
