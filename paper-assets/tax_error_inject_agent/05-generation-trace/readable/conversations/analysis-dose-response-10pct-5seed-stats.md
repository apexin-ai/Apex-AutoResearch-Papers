# analysis dose response 10pct 5seed stats

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analysis_dose-response-10pct-5seed-stats_20260515T221749.jsonl`
- **Structured JSON:** [`82757949b4d4c8049d05.json`](../../sessions/82/82757949b4d4c8049d05.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-15T22:19:13.557800+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport numpy as np\nfrom scipy import stats\nimport json\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# Data\nvanilla = np.array([61.7, 68.1, 66.0, 72.3, 68.1])\ntaxei_10 = np.array([61.7, 70.2, 55.3, 51.1, 68.1])\nrandom_10 = np.array([68.1, 66.0, 55.3, 68.1, 61.7])\n\ntaxei_full = np.array([61.7, 46.8, 61.7, 63.8, 57.4])\nrandom_full = np.array([66.0, 55.3, 68.1, 46.8, 55.3])\n\nseeds = [42, 0, 123, 1, 7]\n\ndef cohen_d_paired(x, y):\n    diff = x - y\n    return np.mean(diff) / np.std(diff, ddof=1)\n\ndef cohen_d_independent(x, y):\n    nx, ny = len(x), len(y)\n    pooled_std = np.sqrt(((nx-1)*np.std(x,ddof=1)**2 + (ny-1)*np.std(y,ddof=1)**2) / (nx+ny-2))\n    return (np.mean(x) - np.mean(y)) / pooled_std\n\ndef bootstrap_ci(x, y, n_boot=10000, ci=0.95, seed=42):\n    rng = np.random.RandomState(seed)\n    diffs = x - y\n    n = len(diffs)\n    boot_means = np.array([np.mean(rng.choice(diffs, size=n, replace=True)) for _ in range(n_boot)])\n    alpha = (1 - ci) / 2\n    return float(np.percentile(boot_means, alpha*100)), float(np.percentile(boot_means, (1-alpha)*100))\n\ndef pairwise(name_a, a, name_b, b):\n    diff = a - b\n    mean_diff = float(np.mean(diff))\n    se_diff = float(np.std(diff, ddof=1) / np.sqrt(len(diff)))\n    \n    t_paired, p_paired = stats.ttest_rel(a, b)\n    t_welch, p_welch = stats.ttest_ind(a, b, equal_var=False)\n    ci_lo, ci_hi = bootstrap_ci(a, b)\n    d = float(cohen_d_paired(a, b))\n    \n    return {\n        \"comparison\": f\"{name_a} vs {name_b}\",\n        \"mean_A\": float(np.mean(a)),\n        \"mean_B\": float(np.mean(b)),\n        \"mean_diff\": round(mean_diff, 3),\n        \"SE_diff\": round(se_diff, 3),\n        \"paired_ttest\": {\"t\": round(float(t_paired), 4), \"p\": round(float(p_paired), 4), \"df\": 4},\n        \"welch_ttest\": {\"t\": round(float(t_welch), 4), \"p\": round(float(p_welch), 4)},\n        \"bootstrap_95CI\": [round(ci_lo, 3), round(ci_hi, 3)],\n        \"cohens_d_paired\": round(d, 4),\n        \"significant_005\": bool(p_paired < 0.05)\n    }\n\n# 1. Pairwise comparisons\npw1 = pairwise(\"Vanilla\", vanilla, \"TaxEI_10pct\", taxei_10)\npw2 = pairwise(\"Vanilla\", vanilla, \"Random_10pct\", random_10)\npw3 = pairwise(\"TaxEI_10pct\", taxei_10, \"Random_10pct\", random_10)\n\n# 2. Variance tests\nlev_stat, lev_p = stats.levene(vanilla, taxei_10, random_10)\n# F-test: ratio of variances (TaxEI 10% vs Random 10%)\nvar_taxei = float(np.var(taxei_10, ddof=1))\nvar_random = float(np.var(random_10, ddof=1))\nf_ratio = var_taxei / var_random\ndf1, df2 = 4, 4\nf_p = float(2 * min(stats.f.cdf(f_ratio, df1, df2), 1 - stats.f.cdf(f_ratio, df1, df2)))\n\nvariance_tests = {\n    \"levene_3group\": {\n        \"statistic\": round(float(lev_stat), 4),\n        \"p_value\": round(float(lev_p), 4),\n        \"groups\": [\"Vanilla\", \"TaxEI_10pct\", \"Random_10pct\"],\n        \"group_SDs\": [round(float(np.std(vanilla, ddof=1)), 2),\n                      round(float(np.std(taxei_10, ddof=1)), 2),\n                      round(float(np.std(random_10, ddof=1)), 2)]\n    },\n    \"f_test_taxei10_vs_random10\": {\n        \"var_taxei10\": round(var_taxei, 2),\n        \"var_random10\": round(var_random, 2),\n        \"SD_taxei10\": round(float(np.std(taxei_10, ddof=1)), 2),\n        \"SD_random10\": round(float(np.std(random_10, ddof=1)), 2),\n        \"F_ratio\": round(f_ratio, 4),\n        \"p_value\": round(f_p, 4)\n    }\n}\n\n# 3. Dose-response trend & cross-dose comparison\ndef dose_trend(name, baseline, dose10, dose_full):\n    m0 = float(np.mean(baseline))\n    m10 = float(np.mean(dose10))\n    m100 = float(np.mean(dose_full))\n    \n    # paired t-test: 10% vs full\n    t_10vfull, p_10vfull = stats.ttest_rel(dose10, dose_full)\n    d_10vfull = float(cohen_d_paired(dose10, dose_full))\n    \n    # effect sizes relative to vanilla\n    d_10 = float(cohen_d_paired(baseline, dose10))\n    d_full = float(cohen_d_paired(baseline, dose_full))\n    \n    return {\n        \"condition\": name,\n        \"mean_0pct\": round(m0, 2),\n        \"mean_10pct\": round(m10, 2),\n        \"mean_100pct\": round(m100, 2),\n        \"drop_0_to_10\": round(m0 - m10, 2),\n        \"drop_0_to_100\": round(m0 - m100, 2),\n        \"drop_10_to_100\": round(m10 - m100, 2),\n        \"effect_size_0v10_d\": round(d_10, 4),\n        \"effect_size_0v100_d\": round(d_full, 4),\n        \"dose_10_vs_full_paired_t\": {\n            \"t\": round(float(t_10vfull), 4),\n            \"p\": round(float(p_10vfull), 4),\n            \"cohens_d\": round(d_10vfull, 4)\n        },\n        \"linearity\": \"monotonic\" if (m0 >= m10 >= m100) or (m0 <= m10 <= m100) else \"non-monotonic\"\n    }\n\ndose_taxei = dose_trend(\"TaxEI\", vanilla, taxei_10, taxei_full)\ndose_random = dose_trend(\"Random\", vanilla, random_10, random_full)\n\n# 4. Power analysis\ndef power_analysis(a, b, alpha=0.05):\n    diff = a - b\n    d = abs(np.mean(diff)) / np.std(diff, ddof=1)\n    n = len(diff)\n    \n    # Non-central t distribution for observed power\n    t_crit = stats.t.ppf(1 - alpha/2, df=n-1)\n    nc = d * np.sqrt(n)  # non-centrality parameter\n    power = 1 - stats.nct.cdf(t_crit, df=n-1, nc=nc) + stats.nct.cdf(-t_crit, df=n-1, nc=nc)\n    \n    # Required n for 80% power\n    target_power = 0.80\n    for req_n in range(5, 500):\n        nc_test = d * np.sqrt(req_n)\n        t_crit_test = stats.t.ppf(1 - alpha/2, df=req_n-1)\n        p_test = 1 - stats.nct.cdf(t_crit_test, df=req_n-1, nc=nc_test) + stats.nct.cdf(-t_crit_test, df=req_n-1, nc=nc_test)\n        if p_test >= target_power:\n            break\n    else:\n        req_n = \">500\"\n    \n    return {\n        \"observed_d\": round(float(d), 4),\n        \"observed_power\": round(float(power), 4),\n        \"n_current\": n,\n        \"n_for_80pct_power\": req_n\n    }\n\npower = {\n    \"Vanilla_vs_TaxEI10\": power_analysis(vanilla, taxei_10),\n    \"Vanilla_vs_Random10\": power_analysis(vanilla, random_10),\n    \"TaxEI10_vs_Random10\": power_analysis(taxei_10, random_10),\n    \"TaxEI10_vs_TaxEI_full\": power_analysis(taxei_10, taxei_full),\n    \"Random10_vs_Random_full\": power_analysis(random_10, random_full),\n}\n\n# Summary\nv_mean = np.mean(vanilla)\nt10_mean = np.mean(taxei_10)\nr10_mean = np.mean(random_10)\nt_full_mean = np.mean(taxei_full)\nr_full_mean = np.mean(random_full)\n\nsummary = (\n    f\"10% dose 5-seed analysis (n=5 per condition): \"\n    f\"Vanilla {v_mean:.1f}±{np.std(vanilla,ddof=1):.1f}%, \"\n    f\"TaxEI-10% {t10_mean:.1f}±{np.std(taxei_10,ddof=1):.1f}%, \"\n    f\"Random-10% {r10_mean:.1f}±{np.std(random_10,ddof=1):.1f}%. \"\n    f\"No pairwise comparison reaches significance (all p>0.05). \"\n    f\"Vanilla vs TaxEI-10%: Δ={v_mean-t10_mean:.1f}pp, p={pw1['paired_ttest']['p']:.3f}, d={pw1['cohens_d_paired']:.2f}. \"\n    f\"Vanilla vs Random-10%: Δ={v_mean-r10_mean:.1f}pp, p={pw2['paired_ttest']['p']:.3f}, d={pw2['cohens_d_paired']:.2f}. \"\n    f\"TaxEI-10% vs Random-10%: Δ={t10_mean-r10_mean:.1f}pp, p={pw3['paired_ttest']['p']:.3f}, d={pw3['cohens_d_paired']:.2f}. \"\n    f\"Levene's test: p={variance_tests['levene_3group']['p_value']:.3f} (no sig variance difference). \"\n    f\"Dose-response: TaxEI 0%→10%→100% = {v_mean:.1f}→{t10_mean:.1f}→{t_full_mean:.1f}% ({dose_taxei['linearity']}); \"\n    f\"Random 0%→10%→100% = {v_mean:.1f}→{r10_mean:.1f}→{r_full_mean:.1f}% ({dose_random['linearity']}). \"\n    f\"10% vs full-dose: TaxEI p={dose_taxei['dose_10_vs_full_paired_t']['p']:.3f}, Random p={dose_random['dose_10_vs_full_paired_t']['p']:.3f}. \"\n    f\"Power at n=5 is low across all comparisons (max {max(v['observed_power'] for v in power.values()):.1%}). \"\n    f\"Largest comparison (Vanilla vs TaxEI-10%) needs ~{power['Vanilla_vs_TaxEI10']['n_for_80pct_power']} seeds for 80% power.\"\n)\n\nresults = {\n    \"pairwise_comparisons\": {\n        \"Vanilla_vs_TaxEI10\": pw1,\n        \"Vanilla_vs_Random10\": pw2,\n        \"TaxEI10_vs_Random10\": pw3\n    },\n    \"variance_tests\": variance_tests,\n    \"dose_response_trend\": {\n        \"TaxEI\": dose_taxei,\n        \"Random\": dose_random\n    },\n    \"power_analysis\": power,\n    \"descriptive_stats\": {\n        \"Vanilla\": {\"mean\": round(v_mean, 2), \"SD\": round(float(np.std(vanilla,ddof=1)), 2), \"values\": vanilla.tolist()},\n        \"TaxEI_10pct\": {\"mean\": round(t10_mean, 2), \"SD\": round(float(np.std(taxei_10,ddof=1)), 2), \"values\": taxei_10.tolist()},\n        \"Random_10pct\": {\"mean\": round(r10_mean, 2), \"SD\": round(float(np.std(random_10,ddof=1)), 2), \"values\": random_10.tolist()},\n        \"TaxEI_full\": {\"mean\": round(t_full_mean, 2), \"SD\": round(float(np.std(taxei_full,ddof=1)), 2), \"values\": taxei_full.tolist()},\n        \"Random_full\": {\"mean\": round(r_full_mean, 2), \"SD\": round(float(np.std(random_full,ddof=1)), 2), \"values\": random_full.tolist()},\n    },\n    \"summary\": summary\n}\n\nout_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dose_response_10pct_stats.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(results, f, indent=2, ensure_ascii=False)\n\nprint(json.dumps(results, indent=2, ensure_ascii=False))\nPYEOF\n",
  "description": "Run dose-response statistical analysis",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-10pct-5seed-stats_20260515T221749",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport numpy as np\nfrom scipy import stats\nimport json\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# Data\nvanilla = np.array([61.7, 68.1, 66.0, 72.3, 68.1])\ntaxei_10 = np.array([61.7, 70.2, 55.3, 51.1, 68.1])\nrandom_10 = np.array([68.1, 66.0, 55.3, 68.1, 61.7])\n\ntaxei_full = np.array([61.7, 46.8, 61.7, 63.8, 57.4])\nrandom_full = np.array([66.0, 55.3, 68.1, 46.8, 55.3])\n\nseeds = [42, 0, 123, 1, 7]\n\ndef cohen_d_paired(x, y):\n    diff = x - y\n    return np.mean(diff) / np.std(diff, ddof=1)\n\ndef cohen_d_independent(x, y):\n    nx, ny = len(x), len(y)\n    pooled_std = np.sqrt(((nx-1)*np.std(x,ddof=1)**2 + (ny-1)*np.std(y,ddof=1)**2) / (nx+ny-2))\n    return (np.mean(x) - np.mean(y)) / pooled_std\n\ndef bootstrap_ci(x, y, n_boot=10000, ci=0.95, seed=42):\n    rng = np.random.RandomState(seed)\n    diffs = x - y\n    n = len(diffs)\n    boot_means = np.array([np.mean(rng.choice(diffs, size=n, replace=True)) for _ in range(n_boot)])\n    alpha = (1 - ci) / 2\n    return float(np.percentile(boot_means, alpha*100)), float(np.percentile(boot_means, (1-alpha)*100))\n\ndef pairwise(name_a, a, name_b, b):\n    diff = a - b\n    mean_diff = float(np.mean(diff))\n    se_diff = float(np.std(diff, ddof=1) / np.sqrt(len(diff)))\n    \n    t_paired, p_paired = stats.ttest_rel(a, b)\n    t_welch, p_welch = stats.ttest_ind(a, b, equal_var=False)\n    ci_lo, ci_hi = bootstrap_ci(a, b)\n    d = float(cohen_d_paired(a, b))\n    \n    return {\n        \"comparison\": f\"{name_a} vs {name_b}\",\n        \"mean_A\": float(np.mean(a)),\n        \"mean_B\": float(np.mean(b)),\n        \"mean_diff\": round(mean_diff, 3),\n        \"SE_diff\": round(se_diff, 3),\n        \"paired_ttest\": {\"t\": round(float(t_paired), 4), \"p\": round(float(p_paired), 4), \"df\": 4},\n        \"welch_ttest\": {\"t\": round(float(t_welch), 4), \"p\": round(float(p_welch), 4)},\n        \"bootstrap_95CI\": [round(ci_lo, 3), round(ci_hi, 3)],\n        \"cohens_d_paired\": round(d, 4),\n        \"significant_005\": bool(p_paired < 0.05)\n    }\n\n# 1. Pairwise comparisons\npw1 = pairwise(\"Vanilla\", vanilla, \"TaxEI_10pct\", taxei_10)\npw2 = pairwise(\"Vanilla\", vanilla, \"Random_10pct\", random_10)\npw3 = pairwise(\"TaxEI_10pct\", taxei_10, \"Random_10pct\", random_10)\n\n# 2. Variance tests\nlev_stat, lev_p = stats.levene(vanilla, taxei_10, random_10)\n# F-test: ratio of variances (TaxEI 10% vs Random 10%)\nvar_taxei = float(np.var(taxei_10, ddof=1))\nvar_random = float(np.var(random_10, ddof=1))\nf_ratio = var_taxei / var_random\ndf1, df2 = 4, 4\nf_p = float(2 * min(stats.f.cdf(f_ratio, df1, df2), 1 - stats.f.cdf(f_ratio, df1, df2)))\n\nvariance_tests = {\n    \"levene_3group\": {\n        \"statistic\": round(float(lev_stat), 4),\n        \"p_value\": round(float(lev_p), 4),\n        \"groups\": [\"Vanilla\", \"TaxEI_10pct\", \"Random_10pct\"],\n        \"group_SDs\": [round(float(np.std(vanilla, ddof=1)), 2),\n                      round(float(np.std(taxei_10, ddof=1)), 2),\n                      round(float(np.std(random_10, ddof=1)), 2)]\n    },\n    \"f_test_taxei10_vs_random10\": {\n        \"var_taxei10\": round(var_taxei, 2),\n        \"var_random10\": round(var_random, 2),\n        \"SD_taxei10\": round(float(np.std(taxei_10, ddof=1)), 2),\n        \"SD_random10\": round(float(np.std(random_10, ddof=1)), 2),\n        \"F_ratio\": round(f_ratio, 4),\n        \"p_value\": round(f_p, 4)\n    }\n}\n\n# 3. Dose-response trend & cross-dose comparison\ndef dose_trend(name, baseline, dose10, dose_full):\n    m0 = float(np.mean(baseline))\n    m10 = float(np.mean(dose10))\n    m100 = float(np.mean(dose_full))\n    \n    # paired t-test: 10% vs full\n    t_10vfull, p_10vfull = stats.ttest_rel(dose10, dose_full)\n    d_10vfull = float(cohen_d_paired(dose10, dose_full))\n    \n    # effect sizes relative to vanilla\n    d_10 = float(cohen_d_paired(baseline, dose10))\n    d_full = float(cohen_d_paired(baseline, dose_full))\n    \n    return {\n        \"condition\": name,\n        \"mean_0pct\": round(m0, 2),\n        \"mean_10pct\": round(m10, 2),\n        \"mean_100pct\": round(m100, 2),\n        \"drop_0_to_10\": round(m0 - m10, 2),\n        \"drop_0_to_100\": round(m0 - m100, 2),\n        \"drop_10_to_100\": round(m10 - m100, 2),\n        \"effect_size_0v10_d\": round(d_10, 4),\n        \"effect_size_0v100_d\": round(d_full, 4),\n        \"dose_10_vs_full_paired_t\": {\n            \"t\": round(float(t_10vfull), 4),\n            \"p\": round(float(p_10vfull), 4),\n            \"cohens_d\": round(d_10vfull, 4)\n        },\n        \"linearity\": \"monotonic\" if (m0 >= m10 >= m100) or (m0 <= m10 <= m100) else \"non-monotonic\"\n    }\n\ndose_taxei = dose_trend(\"TaxEI\", vanilla, taxei_10, taxei_full)\ndose_random = dose_trend(\"Random\", vanilla, random_10, random_full)\n\n# 4. Power analysis\ndef power_analysis(a, b, alpha=0.05):\n    diff = a - b\n    d = abs(np.mean(diff)) / np.std(diff, ddof=1)\n    n = len(diff)\n    \n    # Non-central t distribution for observed power\n    t_crit = stats.t.ppf(1 - alpha/2, df=n-1)\n    nc = d * np.sqrt(n)  # non-centrality parameter\n    power = 1 - stats.nct.cdf(t_crit, df=n-1, nc=nc) + stats.nct.cdf(-t_crit, df=n-1, nc=nc)\n    \n    # Required n for 80% power\n    target_power = 0.80\n    for req_n in range(5, 500):\n        nc_test = d * np.sqrt(req_n)\n        t_crit_test = stats.t.ppf(1 - alpha/2, df=req_n-1)\n        p_test = 1 - stats.nct.cdf(t_crit_test, df=req_n-1, nc=nc_test) + stats.nct.cdf(-t_crit_test, df=req_n-1, nc=nc_test)\n        if p_test >= target_power:\n            break\n    else:\n        req_n = \">500\"\n    \n    return {\n        \"observed_d\": round(float(d), 4),\n        \"observed_power\": round(float(power), 4),\n        \"n_current\": n,\n        \"n_for_80pct_power\": req_n\n    }\n\npower = {\n    \"Vanilla_vs_TaxEI10\": power_analysis(vanilla, taxei_10),\n    \"Vanilla_vs_Random10\": power_analysis(vanilla, random_10),\n    \"TaxEI10_vs_Random10\": power_analysis(taxei_10, random_10),\n    \"TaxEI10_vs_TaxEI_full\": power_analysis(taxei_10, taxei_full),\n    \"Random10_vs_Random_full\": power_analysis(random_10, random_full),\n}\n\n# Summary\nv_mean = np.mean(vanilla)\nt10_mean = np.mean(taxei_10)\nr10_mean = np.mean(random_10)\nt_full_mean = np.mean(taxei_full)\nr_full_mean = np.mean(random_full)\n\nsummary = (\n    f\"10% dose 5-seed analysis (n=5 per condition): \"\n    f\"Vanilla {v_mean:.1f}±{np.std(vanilla,ddof=1):.1f}%, \"\n    f\"TaxEI-10% {t10_mean:.1f}±{np.std(taxei_10,ddof=1):.1f}%, \"\n    f\"Random-10% {r10_mean:.1f}±{np.std(random_10,ddof=1):.1f}%. \"\n    f\"No pairwise comparison reaches significance (all p>0.05). \"\n    f\"Vanilla vs TaxEI-10%: Δ={v_mean-t10_mean:.1f}pp, p={pw1['paired_ttest']['p']:.3f}, d={pw1['cohens_d_paired']:.2f}. \"\n    f\"Vanilla vs Random-10%: Δ={v_mean-r10_mean:.1f}pp, p={pw2['paired_ttest']['p']:.3f}, d={pw2['cohens_d_paired']:.2f}. \"\n    f\"TaxEI-10% vs Random-10%: Δ={t10_mean-r10_mean:.1f}pp, p={pw3['paired_ttest']['p']:.3f}, d={pw3['cohens_d_paired']:.2f}. \"\n    f\"Levene's test: p={variance_tests['levene_3group']['p_value']:.3f} (no sig variance difference). \"\n    f\"Dose-response: TaxEI 0%→10%→100% = {v_mean:.1f}→{t10_mean:.1f}→{t_full_mean:.1f}% ({dose_taxei['linearity']}); \"\n    f\"Random 0%→10%→100% = {v_mean:.1f}→{r10_mean:.1f}→{r_full_mean:.1f}% ({dose_random['linearity']}). \"\n    f\"10% vs full-dose: TaxEI p={dose_taxei['dose_10_vs_full_paired_t']['p']:.3f}, Random p={dose_random['dose_10_vs_full_paired_t']['p']:.3f}. \"\n    f\"Power at n=5 is low across all comparisons (max {max(v['observed_power'] for v in power.values()):.1%}). \"\n    f\"Largest comparison (Vanilla vs TaxEI-10%) needs ~{power['Vanilla_vs_TaxEI10']['n_for_80pct_power']} seeds for 80% power.\"\n)\n\nresults = {\n    \"pairwise_comparisons\": {\n        \"Vanilla_vs_TaxEI10\": pw1,\n        \"Vanilla_vs_Random10\": pw2,\n        \"TaxEI10_vs_Random10\": pw3\n    },\n    \"variance_tests\": variance_tests,\n    \"dose_response_trend\": {\n        \"TaxEI\": dose_taxei,\n        \"Random\": dose_random\n    },\n    \"power_analysis\": power,\n    \"descriptive_stats\": {\n        \"Vanilla\": {\"mean\": round(v_mean, 2), \"SD\": round(float(np.std(vanilla,ddof=1)), 2), \"values\": vanilla.tolist()},\n        \"TaxEI_10pct\": {\"mean\": round(t10_mean, 2), \"SD\": round(float(np.std(taxei_10,ddof=1)), 2), \"values\": taxei_10.tolist()},\n        \"Random_10pct\": {\"mean\": round(r10_mean, 2), \"SD\": round(float(np.std(random_10,ddof=1)), 2), \"values\": random_10.tolist()},\n        \"TaxEI_full\": {\"mean\": round(t_full_mean, 2), \"SD\": round(float(np.std(taxei_full,ddof=1)), 2), \"values\": taxei_full.tolist()},\n        \"Random_full\": {\"mean\": round(r_full_mean, 2), \"SD\": round(float(np.std(random_full,ddof=1)), 2), \"values\": random_full.tolist()},\n    },\n    \"summary\": summary\n}\n\nout_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dose_response_10pct_stats.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(results, f, indent=2, ensure_ascii=False)\n\nprint(json.dumps(results, indent=2, ensure_ascii=False))\nPYEOF\n",
    "description": "Run dose-response statistical analysis",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T22:19:13.558320+00:00_

{
  "pairwise_comparisons": {
    "Vanilla_vs_TaxEI10": {
      "comparison": "Vanilla vs TaxEI_10pct",
      "mean_A": 67.24000000000001,
      "mean_B": 61.279999999999994,
      "mean_diff": 5.96,
      "SE_diff": 4.42,
      "paired_ttest": {
        "t": 1.3484,
        "p": 0.2488,
        "df": 4
      },
      "welch_ttest": {
        "t": 1.4786,
        "p": 0.1923
      },
      "bootstrap_95CI": [
        -0.84,
        14.44
      ],
      "cohens_d_paired": 0.603,
      "significant_005": false
    },
    "Vanilla_vs_Random10": {
      "comparison": "Vanilla vs Random_10pct",
      "mean_A": 67.24000000000001,
      "mean_B": 63.839999999999996,
      "mean_diff": 3.4,
      "SE_diff": 2.834,
      "paired_ttest": {
        "t": 1.1996,
        "p": 0.2965,
        "df": 4
      },
      "welch_ttest": {
        "t": 1.1404,
        "p": 0.2906
      },
      "bootstrap_95CI": [
        -1.72,
        7.68
      ],
      "cohens_d_paired": 0.5365,
      "significant_005": false
    },
    "TaxEI10_vs_Random10": {
      "comparison": "TaxEI_10pct vs Random_10pct",
      "mean_A": 61.279999999999994,
      "mean_B": 63.839999999999996,
      "mean_diff": -2.56,
      "SE_diff": 4.218,
      "paired_ttest": {
        "t": -0.607,
        "p": 0.5766,
        "df": 4
      },
      "welch_ttest": {
        "t": -0.5841,
        "p": 0.5775
      },
      "bootstrap_95CI": [
        -10.2,
        4.24
      ],
      "cohens_d_paired": -0.2714,
      "significant_005": false
    }
  },
  "variance_tests": {
    "levene_3group": {
      "statistic": 1.4143,
      "p_value": 0.2809,
      "groups": [
        "Vanilla",
        "TaxEI_10pct",
        "Random_10pct"
      ],
      "group_SDs": [
        3.85,
        8.15,
        5.44
      ]
    },
    "f_test_taxei10_vs_random10": {
      "var_taxei10": 66.41,
      "var_random10": 29.62,
      "SD_taxei10": 8.15,
      "SD_random10": 5.44,
      "F_ratio": 2.2423,
      "p_value": 0.4534
    }
  },
  "dose_
…[truncated 3175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-10pct-5seed-stats_20260515T221749",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T22:19:13.558559+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-10pct-5seed-stats_20260515T221749",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T22:19:13.558720+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-10pct-5seed-stats_20260515T221749",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T22:19:13.558853+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "dose_response_10pct_stats",
  "type": "data",
  "description": "10% dose-response 5-seed 正式统计分析：pairwise t-tests, bootstrap CI, Cohen's d, Levene's test, dose-response trend, power analysis",
  "project": "tax_error_inject_agent",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dose_response_10pct_stats.json",
  "tags": "['statistics', 'dose-response', '10pct', '5-seed']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-10pct-5seed-stats_20260515T221749",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "dose_response_10pct_stats",
    "type": "data",
    "description": "10% dose-response 5-seed 正式统计分析：pairwise t-tests, bootstrap CI, Cohen's d, Levene's test, dose-response trend, power analysis",
    "project": "tax_error_inject_agent",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dose_response_10pct_stats.json",
    "tags": "['statistics', 'dose-response', '10pct', '5-seed']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T22:19:13.559041+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_405e49\", \"name\": \"dose_response_10pct_stats\", \"type\": \"data\", \"description\": \"10% dose-response 5-seed 正式统计分析：pairwise t-tests, bootstrap CI, Cohen's d, Levene's test, dose-response trend, power analysis\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/data/dose_response_10pct_stats.json\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T22:18:53.685827+00:00\", \"tags\": [\"statistics\", \"dose-response\", \"10pct\", \"5-seed\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-10pct-5seed-stats_20260515T221749",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-15T22:19:13.559220+00:00_

## 10% Dose-Response 统计结果

### 描述统计
| 条件 | Mean | SD |
|------|------|----|
| Vanilla | 67.2% | 3.9 |
| TaxEI 10% | 61.3% | 8.1 |
| Random 10% | 63.8% | 5.4 |

### 两两对比 — 全部不显著

| 对比 | Δ | paired-t p | Welch p | Bootstrap 95% CI | Cohen's d |
|------|---|-----------|---------|-------------------|-----------|
| Vanilla vs TaxEI-10% | +6.0pp | **0.249** | 0.192 | [−0.8, 14.4] | 0.60 (medium) |
| Vanilla vs Random-10% | +3.4pp | **0.296** | 0.291 | [−1.7, 7.7] | 0.54 (medium) |
| TaxEI-10% vs Random-10% | −2.6pp | **0.577** | 0.578 | [−10.2, 4.2] | −0.27 (small) |

CI 均跨零，无显著差异。

### 方差检验
- **Levene's test** (三组): F=1.41, p=0.281 — 方差无显著差异
- **F-test** (TaxEI-10% SD=8.15 vs Random-10% SD=5.44): F=2.24, p=0.453 — 不显著

TaxEI 10% 的 SD（8.15）是 Vanilla（3.85）的 2 倍，但样本量不足以达到统计显著。

### Dose-Response 趋势
两种注入方式均呈**单调递减**：

| 条件 | 0% → 10% → 100% | d(0→10) | d(0→100) |
|------|------------------|---------|----------|
| TaxEI | 67.2 → 61.3 → 58.3 | 0.60 | **1.12** |
| Random | 67.2 → 63.8 → 58.3 | 0.54 | 0.73 |

- **10% vs full-dose 无显著差异**: TaxEI p=0.664, Random p=0.377
- 10% 剂量的效果约为 full-dose 的 2/3（TaxEI: 6.0pp vs 9.0pp），但 n=5 下无法区分

### Power Analysis
| 对比 | observed d | Power (n=5) | n for 80% power |
|------|-----------|-------------|-----------------|
| Vanilla vs TaxEI-10% | 0.60 | **18.2%** | **24 seeds** |
| Vanilla vs Random-10% | 0.54 | 15.4% | 30 seeds |
| TaxEI-10% vs Random-10% | 0.27 | 7.6% | 109 seeds |
| 10% vs full (TaxEI) | 0.21 | 6.6% | 181 seeds |
| 10% vs full (Random) | 0.44 | 12.1% | 42 seeds |

### 关键结论

1. **10% 剂量下无统计显著差异**，但 effect size 为 medium（d≈0.5–0.6），方向与 full-dose 一致
2. **Dose-response 单调**：两种注入方式的性能均随剂量递增而单调下降（0% > 10% > 100%）
3. **10% 与 100% 之间无法区分**（p>0.37），说明 10% 剂量已产生可观效果，额外 90% 的注入边际收益有限
4. **n=5 严重 underpowered**：最大 power 仅 18.2%，检测 medium effect 需要约 24–30 seeds

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_dose-response-10pct-5seed-stats_20260515T221749"
}
```

</details>

---
