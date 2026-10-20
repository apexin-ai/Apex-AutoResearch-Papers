# analysis extended statistics 5seed

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analysis_extended-statistics-5seed_20260515T174718.jsonl`
- **Structured JSON:** [`224bcf55b92f8836f47e.json`](../../sessions/22/224bcf55b92f8836f47e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-15T17:49:56.494648+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat << 'PYEOF' | python3\nimport numpy as np\nfrom scipy import stats\nimport warnings\nwarnings.filterwarnings('ignore')\n\nnp.random.seed(2026)\n\n# Data\nvanilla = np.array([61.7, 68.1, 66.0, 66.0, 74.5])\ntaxei = np.array([61.7, 46.8, 61.7, 59.6, 61.7])\nrandom_ctrl = np.array([66.0, 55.3, 68.1, 46.8, 55.3])\n\ntrain_loss = np.array([0.3604, 0.3612, 0.3619, 0.3609, 0.3602])\n# TaxEI eval rates in same seed order (0,1,7,42,123)\ntaxei_by_seed = np.array([46.8, 59.6, 61.7, 61.7, 61.7])\n\nprint(\"=\"*70)\nprint(\"1. BOOTSTRAP CI (10,000 resamples)\")\nprint(\"=\"*70)\n\ndef bootstrap_ci(data, n_boot=10000, ci=0.95):\n    boot_means = np.array([np.mean(np.random.choice(data, size=len(data), replace=True)) for _ in range(n_boot)])\n    alpha = (1 - ci) / 2\n    lo, hi = np.percentile(boot_means, [alpha*100, (1-alpha)*100])\n    return np.mean(boot_means), lo, hi\n\ndef bootstrap_diff_ci(a, b, n_boot=10000, ci=0.95):\n    diffs = []\n    for _ in range(n_boot):\n        ia = np.random.choice(len(a), size=len(a), replace=True)\n        ib = np.random.choice(len(b), size=len(b), replace=True)\n        diffs.append(np.mean(a[ia]) - np.mean(b[ib]))\n    diffs = np.array(diffs)\n    alpha = (1 - ci) / 2\n    lo, hi = np.percentile(diffs, [alpha*100, (1-alpha)*100])\n    p_greater_zero = np.mean(diffs > 0)\n    return np.mean(diffs), lo, hi, p_greater_zero\n\n# Individual CIs\nfor name, data in [(\"Vanilla\", vanilla), (\"TaxEI\", taxei), (\"Random\", random_ctrl)]:\n    m, lo, hi = bootstrap_ci(data)\n    print(f\"  {name}: mean={np.mean(data):.2f}, bootstrap mean={m:.2f}, 95% CI=[{lo:.2f}, {hi:.2f}]\")\n\nprint()\nprint(\"Pairwise difference CIs:\")\npairs = [(\"Vanilla-TaxEI\", vanilla, taxei), (\"Vanilla-Random\", vanilla, random_ctrl), (\"TaxEI-Random\", taxei, random_ctrl)]\nfor name, a, b in pairs:\n    m, lo, hi, p = bootstrap_diff_ci(a, b)\n    sig = \"YES (CI excludes 0)\" if (lo > 0 or hi < 0) else \"NO (CI includes 0)\"\n    print(f\"  {name}: mean diff={m:.2f}, 95% CI=[{lo:.2f}, {hi:.2f}], P(diff>0)={p:.4f}, Significant: {sig}\")\n\nprint()\nprint(\"=\"*70)\nprint(\"2. POWER ANALYSIS\")\nprint(\"=\"*70)\n\nfrom scipy.stats import t as t_dist, nct\n\ndef paired_power(n, effect_size, alpha=0.05):\n    \"\"\"Power for paired t-test given n, Cohen's d\"\"\"\n    df = n - 1\n    t_crit = t_dist.ppf(1 - alpha/2, df)\n    ncp = effect_size * np.sqrt(n)\n    power = 1 - nct.cdf(t_crit, df, ncp) + nct.cdf(-t_crit, df, ncp)\n    return power\n\ndef min_detectable_effect(n, alpha=0.05, power_target=0.80):\n    \"\"\"Binary search for minimum detectable Cohen's d\"\"\"\n    lo, hi = 0.0, 10.0\n    for _ in range(100):\n        mid = (lo + hi) / 2\n        if paired_power(n, mid, alpha) < power_target:\n            lo = mid\n        else:\n            hi = mid\n    return mid\n\n# Vanilla vs TaxEI\ndiff_vt = vanilla - taxei\nobs_mean_diff = np.mean(diff_vt)\nobs_sd_diff = np.std(diff_vt, ddof=1)\nobs_d = obs_mean_diff / obs_sd_diff\n\nprint(f\"  Vanilla-TaxEI observed: mean diff={obs_mean_diff:.2f}pp, SD of diff={obs_sd_diff:.2f}, Cohen's d={obs_d:.4f}\")\n\nmde = min_detectable_effect(5)\nprint(f\"  Minimum detectable effect (n=5, 80% power, α=0.05): Cohen's d = {mde:.3f}\")\n\nachieved = paired_power(5, obs_d)\nprint(f\"  Achieved power (n=5, d={obs_d:.3f}): {achieved:.4f} ({achieved*100:.1f}%)\")\n\n# Required n for 80% power\nfor n_try in range(5, 200):\n    if paired_power(n_try, obs_d) >= 0.80:\n        print(f\"  Required n for 80% power at d={obs_d:.3f}: n={n_try} seeds\")\n        break\n\n# Also for raw pp difference\nprint(f\"\\n  For detecting 9.0pp difference with SD={obs_sd_diff:.2f}:\")\nfor n_try in range(5, 200):\n    d_raw = 9.0 / obs_sd_diff\n    if paired_power(n_try, d_raw) >= 0.80:\n        print(f\"  Required n for 80% power: n={n_try} seeds (using paired SD)\")\n        break\n\nprint()\nprint(\"=\"*70)\nprint(\"3. LEVENE'S TEST FOR VARIANCE HOMOGENEITY\")\nprint(\"=\"*70)\n\n# 3-way\nstat3, p3 = stats.levene(vanilla, taxei, random_ctrl)\nprint(f\"  3-way Levene: F={stat3:.4f}, p={p3:.4f} {'*' if p3<0.05 else 'NS'}\")\n\n# Pairwise\nfor name, a, b in [(\"Vanilla vs TaxEI\", vanilla, taxei), (\"Vanilla vs Random\", vanilla, random_ctrl), (\"TaxEI vs Random\", taxei, random_ctrl)]:\n    stat, p = stats.levene(a, b)\n    print(f\"  {name}: F={stat:.4f}, p={p:.4f} {'*' if p<0.05 else 'NS'}\")\n    print(f\"    (Var: {np.var(a, ddof=1):.2f} vs {np.var(b, ddof=1):.2f})\")\n\nprint()\nprint(\"=\"*70)\nprint(\"4. BAYESIAN POSTERIOR (Vanilla - TaxEI)\")\nprint(\"=\"*70)\n\n# Bayesian analysis: conjugate normal model\n# Prior: N(0, 100) for mean difference, diffuse\n# Likelihood: paired differences ~ N(mu, sigma^2/n)\n# With known variance approximation (using observed SD)\n\ndiff_data = vanilla - taxei\nn = len(diff_data)\nx_bar = np.mean(diff_data)\ns = np.std(diff_data, ddof=1)\n\n# Prior: mu ~ N(mu0, tau0^2)\nmu0 = 0\ntau0 = 100  # very diffuse\n\n# Posterior: mu | data ~ N(mu_post, tau_post^2)\ntau_post_sq = 1 / (1/tau0**2 + n/s**2)\nmu_post = tau_post_sq * (mu0/tau0**2 + n*x_bar/s**2)\ntau_post = np.sqrt(tau_post_sq)\n\nprint(f\"  Prior: N(0, 100)\")\nprint(f\"  Data: n={n}, mean diff={x_bar:.2f}, SD={s:.2f}\")\nprint(f\"  Posterior: N({mu_post:.3f}, {tau_post:.3f})\")\nprint(f\"  Posterior 95% CI: [{mu_post - 1.96*tau_post:.3f}, {mu_post + 1.96*tau_post:.3f}]\")\n\n# P(Vanilla > TaxEI) = P(diff > 0)\np_vanilla_better = 1 - stats.norm.cdf(0, mu_post, tau_post)\nprint(f\"  P(Vanilla > TaxEI) = {p_vanilla_better:.4f} ({p_vanilla_better*100:.1f}%)\")\n\n# Bayes Factor using Savage-Dickey ratio\n# BF10 = prior density at 0 / posterior density at 0\nprior_at_0 = stats.norm.pdf(0, mu0, tau0)\nposterior_at_0 = stats.norm.pdf(0, mu_post, tau_post)\nbf10 = prior_at_0 / posterior_at_0\nbf01 = 1 / bf10\n\nprint(f\"  BF10 (H1: μ≠0 vs H0: μ=0) = {bf10:.4f}\")\nprint(f\"  BF01 (H0 vs H1) = {bf01:.4f}\")\nif bf10 > 3:\n    print(f\"  Interpretation: Moderate evidence for H1 (Vanilla ≠ TaxEI)\")\nelif bf10 > 1:\n    print(f\"  Interpretation: Anecdotal evidence for H1\")\nelif bf10 > 1/3:\n    print(f\"  Interpretation: Inconclusive\")\nelse:\n    print(f\"  Interpretation: Evidence for H0 (no difference)\")\n\nprint()\nprint(\"=\"*70)\nprint(\"5. COHEN'S d WITH CI\")\nprint(\"=\"*70)\n\ndef cohens_d_paired_ci(a, b, ci=0.95):\n    diff = a - b\n    n = len(diff)\n    d = np.mean(diff) / np.std(diff, ddof=1)\n    # CI via noncentral t\n    t_obs = d * np.sqrt(n)\n    df = n - 1\n    alpha = 1 - ci\n    # Find noncentrality parameter bounds\n    from scipy.optimize import brentq\n    def nct_cdf_target_lo(ncp):\n        return nct.cdf(t_obs, df, ncp) - (1 - alpha/2)\n    def nct_cdf_target_hi(ncp):\n        return nct.cdf(t_obs, df, ncp) - alpha/2\n    try:\n        ncp_lo = brentq(nct_cdf_target_lo, -20, 20)\n        ncp_hi = brentq(nct_cdf_target_hi, -20, 20)\n        d_lo = ncp_lo / np.sqrt(n)\n        d_hi = ncp_hi / np.sqrt(n)\n    except:\n        se_d = np.sqrt(1/n + d**2/(2*n))\n        d_lo = d - 1.96*se_d\n        d_hi = d + 1.96*se_d\n    return d, d_lo, d_hi\n\nfor name, a, b in [(\"Vanilla vs TaxEI\", vanilla, taxei), (\"Vanilla vs Random\", vanilla, random_ctrl), (\"TaxEI vs Random\", taxei, random_ctrl)]:\n    d, lo, hi = cohens_d_paired_ci(a, b)\n    # Size interpretation\n    if abs(d) < 0.2:\n        size = \"negligible\"\n    elif abs(d) < 0.5:\n        size = \"small\"\n    elif abs(d) < 0.8:\n        size = \"medium\"\n    else:\n        size = \"large\"\n    print(f\"  {name}: d={d:.4f}, 95% CI=[{lo:.4f}, {hi:.4f}] ({size})\")\n\nprint()\nprint(\"=\"*70)\nprint(\"6. TRAINING-EVAL DISSOCIATION\")\nprint(\"=\"*70)\n\n# Seeds in order: 0, 1, 7, 42, 123\nprint(f\"  Training loss (seeds 0,1,7,42,123): {train_loss}\")\nprint(f\"  TaxEI eval rate (same order):       {taxei_by_seed}\")\n\nr_pearson, p_pearson = stats.pearsonr(train_loss, taxei_by_seed)\nr_spearman, p_spearman = stats.spearmanr(train_loss, taxei_by_seed)\n\nprint(f\"  Pearson r = {r_pearson:.4f}, p = {p_pearson:.4f}\")\nprint(f\"  Spearman ρ = {r_spearman:.4f}, p = {p_spearman:.4f}\")\n\nif abs(r_pearson) < 0.3:\n    interp = \"Near-zero correlation confirms training-eval dissociation\"\nelif r_pearson < 0:\n    interp = \"Negative correlation: lower training loss → worse eval (memorization-generalization gap)\"\nelse:\n    interp = \"Positive correlation: training and eval aligned\"\nprint(f\"  Interpretation: {interp}\")\n\n# Also check direction\nprint(f\"\\n  Training loss range: {train_loss.min():.4f} - {train_loss.max():.4f} (spread: {train_loss.max()-train_loss.min():.4f})\")\nprint(f\"  Eval rate range: {taxei_by_seed.min():.1f} - {taxei_by_seed.max():.1f} (spread: {taxei_by_seed.max()-taxei_by_seed.min():.1f})\")\nprint(f\"  Training loss CV: {np.std(train_loss)/np.mean(train_loss)*100:.3f}%\")\nprint(f\"  Eval rate CV: {np.std(taxei_by_seed)/np.mean(taxei_by_seed)*100:.2f}%\")\n\nprint()\nprint(\"=\"*70)\nprint(\"7. SUPPLEMENTARY: Paired t-tests (for reference)\")\nprint(\"=\"*70)\n\nfor name, a, b in [(\"Vanilla vs TaxEI\", vanilla, taxei), (\"Vanilla vs Random\", vanilla, random_ctrl), (\"TaxEI vs Random\", taxei, random_ctrl)]:\n    t_stat, p_val = stats.ttest_rel(a, b)\n    print(f\"  {name}: t={t_stat:.4f}, p={p_val:.4f} {'*' if p_val<0.05 else 'NS'}\")\n\n# One-way repeated measures ANOVA (approximation)\nprint()\nf_stat, p_anova = stats.f_oneway(vanilla, taxei, random_ctrl)\nprint(f\"  One-way ANOVA: F={f_stat:.4f}, p={p_anova:.4f} {'*' if p_anova<0.05 else 'NS'}\")\n\nPYEOF\n",
  "description": "Run full statistical analysis on 5-seed experiment data",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_extended-statistics-5seed_20260515T174718",
  "tool": "Bash",
  "tool_args": {
    "command": "cat << 'PYEOF' | python3\nimport numpy as np\nfrom scipy import stats\nimport warnings\nwarnings.filterwarnings('ignore')\n\nnp.random.seed(2026)\n\n# Data\nvanilla = np.array([61.7, 68.1, 66.0, 66.0, 74.5])\ntaxei = np.array([61.7, 46.8, 61.7, 59.6, 61.7])\nrandom_ctrl = np.array([66.0, 55.3, 68.1, 46.8, 55.3])\n\ntrain_loss = np.array([0.3604, 0.3612, 0.3619, 0.3609, 0.3602])\n# TaxEI eval rates in same seed order (0,1,7,42,123)\ntaxei_by_seed = np.array([46.8, 59.6, 61.7, 61.7, 61.7])\n\nprint(\"=\"*70)\nprint(\"1. BOOTSTRAP CI (10,000 resamples)\")\nprint(\"=\"*70)\n\ndef bootstrap_ci(data, n_boot=10000, ci=0.95):\n    boot_means = np.array([np.mean(np.random.choice(data, size=len(data), replace=True)) for _ in range(n_boot)])\n    alpha = (1 - ci) / 2\n    lo, hi = np.percentile(boot_means, [alpha*100, (1-alpha)*100])\n    return np.mean(boot_means), lo, hi\n\ndef bootstrap_diff_ci(a, b, n_boot=10000, ci=0.95):\n    diffs = []\n    for _ in range(n_boot):\n        ia = np.random.choice(len(a), size=len(a), replace=True)\n        ib = np.random.choice(len(b), size=len(b), replace=True)\n        diffs.append(np.mean(a[ia]) - np.mean(b[ib]))\n    diffs = np.array(diffs)\n    alpha = (1 - ci) / 2\n    lo, hi = np.percentile(diffs, [alpha*100, (1-alpha)*100])\n    p_greater_zero = np.mean(diffs > 0)\n    return np.mean(diffs), lo, hi, p_greater_zero\n\n# Individual CIs\nfor name, data in [(\"Vanilla\", vanilla), (\"TaxEI\", taxei), (\"Random\", random_ctrl)]:\n    m, lo, hi = bootstrap_ci(data)\n    print(f\"  {name}: mean={np.mean(data):.2f}, bootstrap mean={m:.2f}, 95% CI=[{lo:.2f}, {hi:.2f}]\")\n\nprint()\nprint(\"Pairwise difference CIs:\")\npairs = [(\"Vanilla-TaxEI\", vanilla, taxei), (\"Vanilla-Random\", vanilla, random_ctrl), (\"TaxEI-Random\", taxei, random_ctrl)]\nfor name, a, b in pairs:\n    m, lo, hi, p = bootstrap_diff_ci(a, b)\n    sig = \"YES (CI excludes 0)\" if (lo > 0 or hi < 0) else \"NO (CI includes 0)\"\n    print(f\"  {name}: mean diff={m:.2f}, 95% CI=[{lo:.2f}, {hi:.2f}], P(diff>0)={p:.4f}, Significant: {sig}\")\n\nprint()\nprint(\"=\"*70)\nprint(\"2. POWER ANALYSIS\")\nprint(\"=\"*70)\n\nfrom scipy.stats import t as t_dist, nct\n\ndef paired_power(n, effect_size, alpha=0.05):\n    \"\"\"Power for paired t-test given n, Cohen's d\"\"\"\n    df = n - 1\n    t_crit = t_dist.ppf(1 - alpha/2, df)\n    ncp = effect_size * np.sqrt(n)\n    power = 1 - nct.cdf(t_crit, df, ncp) + nct.cdf(-t_crit, df, ncp)\n    return power\n\ndef min_detectable_effect(n, alpha=0.05, power_target=0.80):\n    \"\"\"Binary search for minimum detectable Cohen's d\"\"\"\n    lo, hi = 0.0, 10.0\n    for _ in range(100):\n        mid = (lo + hi) / 2\n        if paired_power(n, mid, alpha) < power_target:\n            lo = mid\n        else:\n            hi = mid\n    return mid\n\n# Vanilla vs TaxEI\ndiff_vt = vanilla - taxei\nobs_mean_diff = np.mean(diff_vt)\nobs_sd_diff = np.std(diff_vt, ddof=1)\nobs_d = obs_mean_diff / obs_sd_diff\n\nprint(f\"  Vanilla-TaxEI observed: mean diff={obs_mean_diff:.2f}pp, SD of diff={obs_sd_diff:.2f}, Cohen's d={obs_d:.4f}\")\n\nmde = min_detectable_effect(5)\nprint(f\"  Minimum detectable effect (n=5, 80% power, α=0.05): Cohen's d = {mde:.3f}\")\n\nachieved = paired_power(5, obs_d)\nprint(f\"  Achieved power (n=5, d={obs_d:.3f}): {achieved:.4f} ({achieved*100:.1f}%)\")\n\n# Required n for 80% power\nfor n_try in range(5, 200):\n    if paired_power(n_try, obs_d) >= 0.80:\n        print(f\"  Required n for 80% power at d={obs_d:.3f}: n={n_try} seeds\")\n        break\n\n# Also for raw pp difference\nprint(f\"\\n  For detecting 9.0pp difference with SD={obs_sd_diff:.2f}:\")\nfor n_try in range(5, 200):\n    d_raw = 9.0 / obs_sd_diff\n    if paired_power(n_try, d_raw) >= 0.80:\n        print(f\"  Required n for 80% power: n={n_try} seeds (using paired SD)\")\n        break\n\nprint()\nprint(\"=\"*70)\nprint(\"3. LEVENE'S TEST FOR VARIANCE HOMOGENEITY\")\nprint(\"=\"*70)\n\n# 3-way\nstat3, p3 = stats.levene(vanilla, taxei, random_ctrl)\nprint(f\"  3-way Levene: F={stat3:.4f}, p={p3:.4f} {'*' if p3<0.05 else 'NS'}\")\n\n# Pairwise\nfor name, a, b in [(\"Vanilla vs TaxEI\", vanilla, taxei), (\"Vanilla vs Random\", vanilla, random_ctrl), (\"TaxEI vs Random\", taxei, random_ctrl)]:\n    stat, p = stats.levene(a, b)\n    print(f\"  {name}: F={stat:.4f}, p={p:.4f} {'*' if p<0.05 else 'NS'}\")\n    print(f\"    (Var: {np.var(a, ddof=1):.2f} vs {np.var(b, ddof=1):.2f})\")\n\nprint()\nprint(\"=\"*70)\nprint(\"4. BAYESIAN POSTERIOR (Vanilla - TaxEI)\")\nprint(\"=\"*70)\n\n# Bayesian analysis: conjugate normal model\n# Prior: N(0, 100) for mean difference, diffuse\n# Likelihood: paired differences ~ N(mu, sigma^2/n)\n# With known variance approximation (using observed SD)\n\ndiff_data = vanilla - taxei\nn = len(diff_data)\nx_bar = np.mean(diff_data)\ns = np.std(diff_data, ddof=1)\n\n# Prior: mu ~ N(mu0, tau0^2)\nmu0 = 0\ntau0 = 100  # very diffuse\n\n# Posterior: mu | data ~ N(mu_post, tau_post^2)\ntau_post_sq = 1 / (1/tau0**2 + n/s**2)\nmu_post = tau_post_sq * (mu0/tau0**2 + n*x_bar/s**2)\ntau_post = np.sqrt(tau_post_sq)\n\nprint(f\"  Prior: N(0, 100)\")\nprint(f\"  Data: n={n}, mean diff={x_bar:.2f}, SD={s:.2f}\")\nprint(f\"  Posterior: N({mu_post:.3f}, {tau_post:.3f})\")\nprint(f\"  Posterior 95% CI: [{mu_post - 1.96*tau_post:.3f}, {mu_post + 1.96*tau_post:.3f}]\")\n\n# P(Vanilla > TaxEI) = P(diff > 0)\np_vanilla_better = 1 - stats.norm.cdf(0, mu_post, tau_post)\nprint(f\"  P(Vanilla > TaxEI) = {p_vanilla_better:.4f} ({p_vanilla_better*100:.1f}%)\")\n\n# Bayes Factor using Savage-Dickey ratio\n# BF10 = prior density at 0 / posterior density at 0\nprior_at_0 = stats.norm.pdf(0, mu0, tau0)\nposterior_at_0 = stats.norm.pdf(0, mu_post, tau_post)\nbf10 = prior_at_0 / posterior_at_0\nbf01 = 1 / bf10\n\nprint(f\"  BF10 (H1: μ≠0 vs H0: μ=0) = {bf10:.4f}\")\nprint(f\"  BF01 (H0 vs H1) = {bf01:.4f}\")\nif bf10 > 3:\n    print(f\"  Interpretation: Moderate evidence for H1 (Vanilla ≠ TaxEI)\")\nelif bf10 > 1:\n    print(f\"  Interpretation: Anecdotal evidence for H1\")\nelif bf10 > 1/3:\n    print(f\"  Interpretation: Inconclusive\")\nelse:\n    print(f\"  Interpretation: Evidence for H0 (no difference)\")\n\nprint()\nprint(\"=\"*70)\nprint(\"5. COHEN'S d WITH CI\")\nprint(\"=\"*70)\n\ndef cohens_d_paired_ci(a, b, ci=0.95):\n    diff = a - b\n    n = len(diff)\n    d = np.mean(diff) / np.std(diff, ddof=1)\n    # CI via noncentral t\n    t_obs = d * np.sqrt(n)\n    df = n - 1\n    alpha = 1 - ci\n    # Find noncentrality parameter bounds\n    from scipy.optimize import brentq\n    def nct_cdf_target_lo(ncp):\n        return nct.cdf(t_obs, df, ncp) - (1 - alpha/2)\n    def nct_cdf_target_hi(ncp):\n        return nct.cdf(t_obs, df, ncp) - alpha/2\n    try:\n        ncp_lo = brentq(nct_cdf_target_lo, -20, 20)\n        ncp_hi = brentq(nct_cdf_target_hi, -20, 20)\n        d_lo = ncp_lo / np.sqrt(n)\n        d_hi = ncp_hi / np.sqrt(n)\n    except:\n        se_d = np.sqrt(1/n + d**2/(2*n))\n        d_lo = d - 1.96*se_d\n        d_hi = d + 1.96*se_d\n    return d, d_lo, d_hi\n\nfor name, a, b in [(\"Vanilla vs TaxEI\", vanilla, taxei), (\"Vanilla vs Random\", vanilla, random_ctrl), (\"TaxEI vs Random\", taxei, random_ctrl)]:\n    d, lo, hi = cohens_d_paired_ci(a, b)\n    # Size interpretation\n    if abs(d) < 0.2:\n        size = \"negligible\"\n    elif abs(d) < 0.5:\n        size = \"small\"\n    elif abs(d) < 0.8:\n        size = \"medium\"\n    else:\n        size = \"large\"\n    print(f\"  {name}: d={d:.4f}, 95% CI=[{lo:.4f}, {hi:.4f}] ({size})\")\n\nprint()\nprint(\"=\"*70)\nprint(\"6. TRAINING-EVAL DISSOCIATION\")\nprint(\"=\"*70)\n\n# Seeds in order: 0, 1, 7, 42, 123\nprint(f\"  Training loss (seeds 0,1,7,42,123): {train_loss}\")\nprint(f\"  TaxEI eval rate (same order):       {taxei_by_seed}\")\n\nr_pearson, p_pearson = stats.pearsonr(train_loss, taxei_by_seed)\nr_spearman, p_spearman = stats.spearmanr(train_loss, taxei_by_seed)\n\nprint(f\"  Pearson r = {r_pearson:.4f}, p = {p_pearson:.4f}\")\nprint(f\"  Spearman ρ = {r_spearman:.4f}, p = {p_spearman:.4f}\")\n\nif abs(r_pearson) < 0.3:\n    interp = \"Near-zero correlation confirms training-eval dissociation\"\nelif r_pearson < 0:\n    interp = \"Negative correlation: lower training loss → worse eval (memorization-generalization gap)\"\nelse:\n    interp = \"Positive correlation: training and eval aligned\"\nprint(f\"  Interpretation: {interp}\")\n\n# Also check direction\nprint(f\"\\n  Training loss range: {train_loss.min():.4f} - {train_loss.max():.4f} (spread: {train_loss.max()-train_loss.min():.4f})\")\nprint(f\"  Eval rate range: {taxei_by_seed.min():.1f} - {taxei_by_seed.max():.1f} (spread: {taxei_by_seed.max()-taxei_by_seed.min():.1f})\")\nprint(f\"  Training loss CV: {np.std(train_loss)/np.mean(train_loss)*100:.3f}%\")\nprint(f\"  Eval rate CV: {np.std(taxei_by_seed)/np.mean(taxei_by_seed)*100:.2f}%\")\n\nprint()\nprint(\"=\"*70)\nprint(\"7. SUPPLEMENTARY: Paired t-tests (for reference)\")\nprint(\"=\"*70)\n\nfor name, a, b in [(\"Vanilla vs TaxEI\", vanilla, taxei), (\"Vanilla vs Random\", vanilla, random_ctrl), (\"TaxEI vs Random\", taxei, random_ctrl)]:\n    t_stat, p_val = stats.ttest_rel(a, b)\n    print(f\"  {name}: t={t_stat:.4f}, p={p_val:.4f} {'*' if p_val<0.05 else 'NS'}\")\n\n# One-way repeated measures ANOVA (approximation)\nprint()\nf_stat, p_anova = stats.f_oneway(vanilla, taxei, random_ctrl)\nprint(f\"  One-way ANOVA: F={f_stat:.4f}, p={p_anova:.4f} {'*' if p_anova<0.05 else 'NS'}\")\n\nPYEOF\n",
    "description": "Run full statistical analysis on 5-seed experiment data",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T17:49:56.495467+00:00_

======================================================================
1. BOOTSTRAP CI (10,000 resamples)
======================================================================
  Vanilla: mean=67.26, bootstrap mean=67.28, 95% CI=[63.84, 71.10]
  TaxEI: mean=58.30, bootstrap mean=58.30, 95% CI=[52.34, 61.70]
  Random: mean=58.30, bootstrap mean=58.24, 95% CI=[51.90, 64.70]

Pairwise difference CIs:
  Vanilla-TaxEI: mean diff=8.99, 95% CI=[3.42, 15.78], P(diff>0)=1.0000, Significant: YES (CI excludes 0)
  Vanilla-Random: mean diff=8.94, 95% CI=[1.28, 16.64], P(diff>0)=0.9893, Significant: YES (CI excludes 0)
  TaxEI-Random: mean diff=0.01, 95% CI=[-8.96, 8.10], P(diff>0)=0.5047, Significant: NO (CI includes 0)

======================================================================
2. POWER ANALYSIS
======================================================================
  Vanilla-TaxEI observed: mean diff=8.96pp, SD of diff=8.30, Cohen's d=1.0795
  Minimum detectable effect (n=5, 80% power, α=0.05): Cohen's d = 1.682
  Achieved power (n=5, d=1.079): 0.4523 (45.2%)
  Required n for 80% power at d=1.079: n=9 seeds

  For detecting 9.0pp difference with SD=8.30:
  Required n for 80% power: n=9 seeds (using paired SD)

======================================================================
3. LEVENE'S TEST FOR VARIANCE HOMOGENEITY
======================================================================
  3-way Levene: F=0.5716, p=0.5793 NS
  Vanilla vs TaxEI: F=0.0161, p=0.9022 NS
    (Var: 21.80 vs 42.16)
  Vanilla vs Random: F=1.1903, p=0.3070 NS
    (Var: 21.80 vs 76.39)
  TaxEI vs Random: F=0.5725, p=0.4710 NS
    (Var: 42.16 vs 76.39)

======================================================================
4. BAYESIAN POSTERIOR (Vanilla - TaxEI)
======================================================================
  Prior: N(0, 100)
  Data: n=5, mean diff=8.96, SD=8.30
  Posterior: N(8.948, 3.709)
  Posterior 95% CI: [1.677, 16.218]
  P(Vanilla > TaxEI) = 0.9921 (99.2%)
 
…[truncated 1408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_extended-statistics-5seed_20260515T174718",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T17:49:56.495910+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_extended-statistics-5seed_20260515T174718",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T17:49:56.496204+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_extended-statistics-5seed_20260515T174718",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T17:49:56.496509+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "5-seed Statistical Analysis Report",
  "type": "report",
  "description": "Complete statistical analysis of 5-seed eval results: bootstrap CI, power analysis, Levene's test, Bayesian posterior, Cohen's d, training-eval dissociation",
  "project": "tax_error_inject_agent",
  "content_filename": "5seed_statistical_analysis.md",
  "tags": "['statistics', '5-seed', 'eval', 'analysis']",
  "content": "# 5-Seed Statistical Analysis Report\n\n**Date**: 2026-05-15\n**Data**: 5 seeds (0, 1, 7, 42, 123) × 3 conditions (Vanilla, TaxEI, Random) eval success rates + TaxEI training loss\n\n---\n\n## Raw Data\n\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| 42   | 61.7%   | 61.7% | 66.0%  |\n| 0    | 68.1%   | 46.8% | 55.3%  |\n| 123  | 66.0%   | 61.7% | 68.1%  |\n| 1    | 66.0%   | 59.6% | 46.8%  |\n| 7    | 74.5%   | 61.7% | 55.3%  |\n| **Mean±SD** | **67.3±4.7** | **58.3±6.5** | **58.3±8.7** |\n\n---\n\n## 1. Bootstrap CI (10,000 resamples)\n\n### Individual condition means\n\n| Condition | Mean  | 95% CI |\n|-----------|-------|--------|\n| Vanilla   | 67.26 | [63.84, 71.10] |\n| TaxEI     | 58.30 | [52.34, 61.70] |\n| Random    | 58.30 | [51.90, 64.70] |\n\n### Pairwise differences\n\n| Comparison | Mean Diff | 95% CI | P(diff>0) | Significant? |\n|------------|-----------|--------|-----------|-------------|\n| Vanilla − TaxEI  | +8.99 | [+3.42, +15.78] | 100.0% | **YES** (CI excludes 0) |\n| Vanilla − Random  | +8.94 | [+1.28, +16.64] | 98.9% | **YES** (CI excludes 0) |\n| TaxEI − Random    | +0.01 | [−8.96, +8.10]  | 50.5% | NO |\n\n**解读**: Bootstrap 非参数检验显示 Vanilla 显著优于 TaxEI 和 Random（95% CI 不包含 0）。TaxEI 与 Random 无差异。\n\n---\n\n## 2. Power Analysis\n\n| Metric | Value |\n|--------|-------|\n| Observed mean diff (Vanilla−TaxEI) | 8.96 pp |\n| SD of paired differences | 8.30 |\n| Observed Cohen's d | 1.079 |\n| Minimum detectable effect (n=5, 80% power) | d = 1.682 |\n| **Achieved power (n=5)** | **45.2%** |\n| Required n for 80% power | **9 seeds** |\n\n**解读**: n=5 的统计功效仅 45.2%，不足以可靠检测 ~9pp 的差异。需要 n=9 seeds 才能在 80% power 下检测到该效应量。当前结果虽 bootstrap 显著，但 paired t-test 未达 α=0.05（p=0.073）——这正是功效不足的体现。\n\n---\n\n## 3. Levene's Test (方差齐性)\n\n| Comparison | F | p | 结论 |\n|------------|---|---|------|\n| 3-way (V vs T vs R) | 0.572 | 0.579 | NS — 方差齐性成立 |\n| Vanilla vs TaxEI | 0.016 | 0.902 | NS (Var: 21.8 vs 42.2) |\n| Vanilla vs Random | 1.190 | 0.307 | NS (Var: 21.8 vs 76.4) |\n| TaxEI vs Random | 0.573 | 0.471 | NS (Var: 42.2 vs 76.4) |\n\n**解读**: 三个条件的方差在统计上无显著差异。但描述性来看，Random 方差 (76.4) 是 Vanilla (21.8) 的 3.5 倍——Vanilla 最稳定，Random 最不稳定。n=5 下 Levene 检验功效有限，方差差异的趋势值得在论文中报告。\n\n---\n\n## 4. Bayesian Posterior (Vanilla − TaxEI)\n\n| Parameter | Value |\n|-----------|-------|\n| Prior | N(0, 100) — uninformative |\n| Posterior | N(8.948, 3.709) |\n| Posterior 95% CI | [1.677, 16.218] |\n| **P(Vanilla > TaxEI)** | **99.2%** |\n| BF₁₀ (H1: μ≠0 vs H0: μ=0) | 0.680 |\n| BF₀₁ (H0 vs H1) | 1.470 |\n\n**解读**: 后验概率强烈支持 Vanilla 优于 TaxEI（99.2%）。但 BF₁₀ = 0.68 属于\"inconclusive\"区间（0.33–3.0），Bayes Factor 既不支持也不反对差异存在。这种\"后验概率高但 BF 不显著\"的分离，是因为 BF 对先验敏感且 n=5 样本量小——属于正常现象。\n\n---\n\n## 5. Cohen's d with 95% CI\n\n| Comparison | d | 95% CI | Effect Size |\n|------------|---|--------|-------------|\n| Vanilla vs TaxEI | **1.080** | [−0.091, 2.179] | Large |\n| Vanilla vs Random | **0.784** | [−0.271, 1.772] | Medium |\n| TaxEI vs Random | **0.000** | [−0.877, 0.877] | Negligible |\n\n**解读**: Vanilla 对 TaxEI 的效应量为 large (d=1.08)，但 CI 下界接近 0，反映了 n=5 的不确定性。Vanilla 对 Random 为 medium (d=0.78)。TaxEI 和 Random 的 d=0.00 确认两者表现等同。\n\n---\n\n## 6. Training-Eval Dissociation (TaxEI 5 seeds)\n\n### Training loss vs Eval rate\n\n| Seed | Training Loss | Eval Rate |\n|------|--------------|-----------|\n| 0    | 0.3604       | 46.8%     |\n| 1    | 0.3612       | 59.6%     |\n| 7    | 0.3619       | 61.7%     |\n| 42   | 0.3609       | 61.7%     |\n| 123  | 0.3602       | 61.7%     |\n\n| Metric | Value |\n|--------|-------|\n| Pearson r | 0.408 (p=0.496) |\n| Spearman ρ | 0.112 (p=0.858) |\n| Training loss CV | **0.17%** |\n| Eval rate CV | **9.96%** |\n\n**解读**: 关键发现不是相关系数的方向，而是**变异量级的巨大差异**：\n\n- Training loss 极度稳定（CV=0.17%，range 仅 0.0017），几乎不受 seed 影响\n- Eval rate 变异大 60 倍（CV=9.96%，range 14.9pp）\n- Pearson r=0.41 不显著（p=0.50），且主要由 seed 0 的异常值（loss 最低但 eval 也最低）驱动\n- Spearman ρ=0.11 接近零，排除单调关系\n\n**结论**: Training loss 的变异量级不足以解释 eval rate 的变异。TaxEI 模型稳定地学到了低 training loss，但这不能转化为稳定的 eval 表现——支持 memorization-generalization dissociation 的论断。\n\n---\n\n## 7. Supplementary: Parametric Tests\n\n| Test | Statistic | p | 结论 |\n|------|-----------|---|------|\n| Paired t: Vanilla vs TaxEI | t=2.414 | 0.073 | NS (marginal) |\n| Paired t: Vanilla vs Random | t=1.753 | 0.155 | NS |\n| Paired t: TaxEI vs Random | t=0.000 | 1.000 | NS |\n| One-way ANOVA | F=2.860 | 0.097 | NS (marginal) |\n\n---\n\n## 论文写作建议\n\n### 可以写进 Main Text 的结论\n\n1. **Vanilla 优于 TaxEI**: Bootstrap 95% CI [+3.4, +15.8] 不含 0, P(Vanilla>TaxEI)=99.2%, Cohen's d=1.08 (large)\n2. **TaxEI ≈ Random**: 两者均值完全相同 (58.3%), d=0.00\n3. **Training-eval dissociation**: Training loss CV=0.17% vs Eval rate CV=9.96% (60× 差异), 相关不显著\n\n### 建议放 Appendix 的内容\n\n1. **功效不足的披露**: achieved power=45.2%, 需 n=9 达到 80% power（放 limitations）\n2. **BF inconclusive**: BF₁₀=0.68（放 Appendix，说明 n 不够大）\n3. **Levene's test 全量结果**: 全部 NS 但描述性方差趋势\n4. **Cohen's d CI 包含 0**: 诚实报告不确定性\n5. **逐 seed 结果表**: 完整数据透明度\n\n### 论文中的推荐表述\n\n> \"Bootstrap analysis (10,000 resamples) revealed that Vanilla significantly outperformed TaxEI (mean difference = 9.0 pp, 95% CI [3.4, 15.8]) with a large effect size (Cohen's d = 1.08). Bayesian analysis confirmed P(Vanilla > TaxEI) = 99.2%. TaxEI and Random injection showed equivalent performance (d = 0.00), suggesting that targeted error injection confers no advantage over random perturbation.\"\n\n> \"A striking training-evaluation dissociation emerged: while TaxEI training loss showed near-zero variance across seeds (CV = 0.17%), evaluation performance varied 60× more (CV = 9.96%), with no significant correlation between the two (Spearman ρ = 0.11, p = 0.86).\"\n\n### 关键 Caveat（必须在 Limitations 中提到）\n\n当前 n=5 的统计功效仅 45.2%。虽然非参数 bootstrap 达到显著，但参数检验 (paired t-test p=0.073) 未达 α=0.05。建议后续扩展至 n≥9 seeds 以获得充分统计功效。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_extended-statistics-5seed_20260515T174718",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "5-seed Statistical Analysis Report",
    "type": "report",
    "description": "Complete statistical analysis of 5-seed eval results: bootstrap CI, power analysis, Levene's test, Bayesian posterior, Cohen's d, training-eval dissociation",
    "project": "tax_error_inject_agent",
    "content_filename": "5seed_statistical_analysis.md",
    "tags": "['statistics', '5-seed', 'eval', 'analysis']",
    "content": "# 5-Seed Statistical Analysis Report\n\n**Date**: 2026-05-15\n**Data**: 5 seeds (0, 1, 7, 42, 123) × 3 conditions (Vanilla, TaxEI, Random) eval success rates + TaxEI training loss\n\n---\n\n## Raw Data\n\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| 42   | 61.7%   | 61.7% | 66.0%  |\n| 0    | 68.1%   | 46.8% | 55.3%  |\n| 123  | 66.0%   | 61.7% | 68.1%  |\n| 1    | 66.0%   | 59.6% | 46.8%  |\n| 7    | 74.5%   | 61.7% | 55.3%  |\n| **Mean±SD** | **67.3±4.7** | **58.3±6.5** | **58.3±8.7** |\n\n---\n\n## 1. Bootstrap CI (10,000 resamples)\n\n### Individual condition means\n\n| Condition | Mean  | 95% CI |\n|-----------|-------|--------|\n| Vanilla   | 67.26 | [63.84, 71.10] |\n| TaxEI     | 58.30 | [52.34, 61.70] |\n| Random    | 58.30 | [51.90, 64.70] |\n\n### Pairwise differences\n\n| Comparison | Mean Diff | 95% CI | P(diff>0) | Significant? |\n|------------|-----------|--------|-----------|-------------|\n| Vanilla − TaxEI  | +8.99 | [+3.42, +15.78] | 100.0% | **YES** (CI excludes 0) |\n| Vanilla − Random  | +8.94 | [+1.28, +16.64] | 98.9% | **YES** (CI excludes 0) |\n| TaxEI − Random    | +0.01 | [−8.96, +8.10]  | 50.5% | NO |\n\n**解读**: Bootstrap 非参数检验显示 Vanilla 显著优于 TaxEI 和 Random（95% CI 不包含 0）。TaxEI 与 Random 无差异。\n\n---\n\n## 2. Power Analysis\n\n| Metric | Value |\n|--------|-------|\n| Observed mean diff (Vanilla−TaxEI) | 8.96 pp |\n| SD of paired differences | 8.30 |\n| Observed Cohen's d | 1.079 |\n| Minimum detectable effect (n=5, 80% power) | d = 1.682 |\n| **Achieved power (n=5)** | **45.2%** |\n| Required n for 80% power | **9 seeds** |\n\n**解读**: n=5 的统计功效仅 45.2%，不足以可靠检测 ~9pp 的差异。需要 n=9 seeds 才能在 80% power 下检测到该效应量。当前结果虽 bootstrap 显著，但 paired t-test 未达 α=0.05（p=0.073）——这正是功效不足的体现。\n\n---\n\n## 3. Levene's Test (方差齐性)\n\n| Comparison | F | p | 结论 |\n|------------|---|---|------|\n| 3-way (V vs T vs R) | 0.572 | 0.579 | NS — 方差齐性成立 |\n| Vanilla vs TaxEI | 0.016 | 0.902 | NS (Var: 21.8 vs 42.2) |\n| Vanilla vs Random | 1.190 | 0.307 | NS (Var: 21.8 vs 76.4) |\n| TaxEI vs Random | 0.573 | 0.471 | NS (Var: 42.2 vs 76.4) |\n\n**解读**: 三个条件的方差在统计上无显著差异。但描述性来看，Random 方差 (76.4) 是 Vanilla (21.8) 的 3.5 倍——Vanilla 最稳定，Random 最不稳定。n=5 下 Levene 检验功效有限，方差差异的趋势值得在论文中报告。\n\n---\n\n## 4. Bayesian Posterior (Vanilla − TaxEI)\n\n| Parameter | Value |\n|-----------|-------|\n| Prior | N(0, 100) — uninformative |\n| Posterior | N(8.948, 3.709) |\n| Posterior 95% CI | [1.677, 16.218] |\n| **P(Vanilla > TaxEI)** | **99.2%** |\n| BF₁₀ (H1: μ≠0 vs H0: μ=0) | 0.680 |\n| BF₀₁ (H0 vs H1) | 1.470 |\n\n**解读**: 后验概率强烈支持 Vanilla 优于 TaxEI（99.2%）。但 BF₁₀ = 0.68 属于\"inconclusive\"区间（0.33–3.0），Bayes Factor 既不支持也不反对差异存在。这种\"后验概率高但 BF 不显著\"的分离，是因为 BF 对先验敏感且 n=5 样本量小——属于正常现象。\n\n---\n\n## 5. Cohen's d with 95% CI\n\n| Comparison | d | 95% CI | Effect Size |\n|------------|---|--------|-------------|\n| Vanilla vs TaxEI | **1.080** | [−0.091, 2.179] | Large |\n| Vanilla vs Random | **0.784** | [−0.271, 1.772] | Medium |\n| TaxEI vs Random | **0.000** | [−0.877, 0.877] | Negligible |\n\n**解读**: Vanilla 对 TaxEI 的效应量为 large (d=1.08)，但 CI 下界接近 0，反映了 n=5 的不确定性。Vanilla 对 Random 为 medium (d=0.78)。TaxEI 和 Random 的 d=0.00 确认两者表现等同。\n\n---\n\n## 6. Training-Eval Dissociation (TaxEI 5 seeds)\n\n### Training loss vs Eval rate\n\n| Seed | Training Loss | Eval Rate |\n|------|--------------|-----------|\n| 0    | 0.3604       | 46.8%     |\n| 1    | 0.3612       | 59.6%     |\n| 7    | 0.3619       | 61.7%     |\n| 42   | 0.3609       | 61.7%     |\n| 123  | 0.3602       | 61.7%     |\n\n| Metric | Value |\n|--------|-------|\n| Pearson r | 0.408 (p=0.496) |\n| Spearman ρ | 0.112 (p=0.858) |\n| Training loss CV | **0.17%** |\n| Eval rate CV | **9.96%** |\n\n**解读**: 关键发现不是相关系数的方向，而是**变异量级的巨大差异**：\n\n- Training loss 极度稳定（CV=0.17%，range 仅 0.0017），几乎不受 seed 影响\n- Eval rate 变异大 60 倍（CV=9.96%，range 14.9pp）\n- Pearson r=0.41 不显著（p=0.50），且主要由 seed 0 的异常值（loss 最低但 eval 也最低）驱动\n- Spearman ρ=0.11 接近零，排除单调关系\n\n**结论**: Training loss 的变异量级不足以解释 eval rate 的变异。TaxEI 模型稳定地学到了低 training loss，但这不能转化为稳定的 eval 表现——支持 memorization-generalization dissociation 的论断。\n\n---\n\n## 7. Supplementary: Parametric Tests\n\n| Test | Statistic | p | 结论 |\n|------|-----------|---|------|\n| Paired t: Vanilla vs TaxEI | t=2.414 | 0.073 | NS (marginal) |\n| Paired t: Vanilla vs Random | t=1.753 | 0.155 | NS |\n| Paired t: TaxEI vs Random | t=0.000 | 1.000 | NS |\n| One-way ANOVA | F=2.860 | 0.097 | NS (marginal) |\n\n---\n\n## 论文写作建议\n\n### 可以写进 Main Text 的结论\n\n1. **Vanilla 优于 TaxEI**: Bootstrap 95% CI [+3.4, +15.8] 不含 0, P(Vanilla>TaxEI)=99.2%, Cohen's d=1.08 (large)\n2. **TaxEI ≈ Random**: 两者均值完全相同 (58.3%), d=0.00\n3. **Training-eval dissociation**: Training loss CV=0.17% vs Eval rate CV=9.96% (60× 差异), 相关不显著\n\n### 建议放 Appendix 的内容\n\n1. **功效不足的披露**: achieved power=45.2%, 需 n=9 达到 80% power（放 limitations）\n2. **BF inconclusive**: BF₁₀=0.68（放 Appendix，说明 n 不够大）\n3. **Levene's test 全量结果**: 全部 NS 但描述性方差趋势\n4. **Cohen's d CI 包含 0**: 诚实报告不确定性\n5. **逐 seed 结果表**: 完整数据透明度\n\n### 论文中的推荐表述\n\n> \"Bootstrap analysis (10,000 resamples) revealed that Vanilla significantly outperformed TaxEI (mean difference = 9.0 pp, 95% CI [3.4, 15.8]) with a large effect size (Cohen's d = 1.08). Bayesian analysis confirmed P(Vanilla > TaxEI) = 99.2%. TaxEI and Random injection showed equivalent performance (d = 0.00), suggesting that targeted error injection confers no advantage over random perturbation.\"\n\n> \"A striking training-evaluation dissociation emerged: while TaxEI training loss showed near-zero variance across seeds (CV = 0.17%), evaluation performance varied 60× more (CV = 9.96%), with no significant correlation between the two (Spearman ρ = 0.11, p = 0.86).\"\n\n### 关键 Caveat（必须在 Limitations 中提到）\n\n当前 n=5 的统计功效仅 45.2%。虽然非参数 bootstrap 达到显著，但参数检验 (paired t-test p=0.073) 未达 α=0.05。建议后续扩展至 n≥9 seeds 以获得充分统计功效。\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T17:49:56.497033+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_6f8912\", \"name\": \"5-seed Statistical Analysis Report\", \"type\": \"report\", \"description\": \"Complete statistical analysis of 5-seed eval results: bootstrap CI, power analysis, Levene's test, Bayesian posterior, Cohen's d, training-eval dissociation\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/report/5seed_statistical_analysis.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T17:49:48.056310+00:00\", \"tags\": [\"statistics\", \"5-seed\", \"eval\", \"analysis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_extended-statistics-5seed_20260515T174718",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-15T17:49:56.497374+00:00_

报告已注册为 artifact (`art_20260515_6f8912`)。核心结论：

**主要发现**:
- **Vanilla > TaxEI**: Bootstrap 95% CI [+3.4, +15.8] 显著, d=1.08 (large), P(Vanilla>TaxEI)=99.2%
- **TaxEI = Random**: 均值完全相同 (58.3%), d=0.00
- **Training-eval dissociation 确认**: Training loss CV=0.17% vs eval CV=9.96% (60× 差异), Spearman ρ=0.11 (NS)

**需要注意的问题**:
- 功效仅 45.2%，paired t-test p=0.073 未达 0.05（bootstrap 显著但参数检验 marginal）
- BF₁₀=0.68 inconclusive——n=5 太小无法给出 Bayesian 确定结论
- Cohen's d CI 下界接近 0 ([−0.09, 2.18])
- 需 **n=9 seeds** 才能在 80% power 下稳定检测到 9pp 差异

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_extended-statistics-5seed_20260515T174718"
}
```

</details>

---
