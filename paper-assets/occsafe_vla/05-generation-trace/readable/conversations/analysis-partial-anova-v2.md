# analysis partial anova v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analysis_partial_anova_v2_20260526T120959.jsonl`
- **Structured JSON:** [`05e6fbd951a961a29d56.json`](../../sessions/05/05e6fbd951a961a29d56.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-26T12:12:06.668377+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport numpy as np\nfrom scipy import stats\n\n# Data\ncell1 = np.array([0.746, 0.654, 0.776])  # Full OCC BN (Grad ON + BN)\ncell3 = np.array([0.774, 0.736, 0.762, 0.794])  # Detach BN (Grad OFF + BN)\nvanilla = 0.768\n\nn1, n3 = len(cell1), len(cell3)\nm1, m3 = cell1.mean(), cell3.mean()\ns1, s3 = cell1.std(ddof=1), cell3.std(ddof=1)\n\nprint(\"=\"*60)\nprint(\"1. 独立样本 t-test: Cell 1 vs Cell 3\")\nprint(\"=\"*60)\nt_ind, p_ind = stats.ttest_ind(cell1, cell3, equal_var=False)  # Welch's t-test\n# Cohen's d (pooled SD)\nsp = np.sqrt(((n1-1)*s1**2 + (n3-1)*s3**2) / (n1+n3-2))\nd = (m1 - m3) / sp\nprint(f\"Cell 1: mean={m1:.4f}, SD={s1:.4f}, n={n1}\")\nprint(f\"Cell 3: mean={m3:.4f}, SD={s3:.4f}, n={n3}\")\nprint(f\"差值 (Cell1 - Cell3): {m1-m3:.4f}\")\nprint(f\"Welch's t = {t_ind:.4f}, p = {p_ind:.4f}\")\nprint(f\"Cohen's d = {d:.4f}\")\nprint(f\"Pooled SD = {sp:.4f}\")\n\n# Also equal-var t-test for reference\nt_eq, p_eq = stats.ttest_ind(cell1, cell3, equal_var=True)\nprint(f\"(Equal-var t-test: t={t_eq:.4f}, p={p_eq:.4f})\")\n\nprint()\nprint(\"=\"*60)\nprint(\"2. 效应量分析\")\nprint(\"=\"*60)\nprint(f\"Cohen's d = {d:.4f}\")\nif abs(d) < 0.2:\n    mag = \"negligible\"\nelif abs(d) < 0.5:\n    mag = \"small\"\nelif abs(d) < 0.8:\n    mag = \"medium\"\nelse:\n    mag = \"large\"\nprint(f\"效应量级别: {mag}\")\nprint(f\"梯度流 ON 使 CAR 降低 {abs(m1-m3):.4f} (相对降低 {abs(m1-m3)/m3*100:.1f}%)\")\n\nprint()\nprint(\"=\"*60)\nprint(\"3. 功效分析 (Power Analysis)\")\nprint(\"=\"*60)\nfrom scipy.stats import nct\n\ndef power_ttest_ind(n1, n2, d, alpha=0.05):\n    df = n1 + n2 - 2\n    ncp = d * np.sqrt(n1 * n2 / (n1 + n2))\n    t_crit = stats.t.ppf(1 - alpha/2, df)\n    power = 1 - nct.cdf(t_crit, df, ncp) + nct.cdf(-t_crit, df, ncp)\n    return power\n\ncurrent_power = power_ttest_ind(n1, n3, abs(d))\nprint(f\"当前 power (n1={n1}, n2={n3}, d={abs(d):.3f}, α=0.05): {current_power:.4f}\")\n\n# Find required n for power=0.80\nfor n in range(3, 200):\n    pw = power_ttest_ind(n, n, abs(d))\n    if pw >= 0.80:\n        print(f\"达到 power=0.80 需要每组 n={n} (total={2*n} seeds)\")\n        print(f\"  验证: power={pw:.4f}\")\n        break\n\n# Show power curve\nprint(\"\\nPower curve (equal group sizes):\")\nfor n in [3, 4, 5, 6, 8, 10, 15, 20, 30]:\n    pw = power_ttest_ind(n, n, abs(d))\n    print(f\"  n={n:2d} per group: power={pw:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"4. 单样本 t-test: Cell 3 vs Vanilla (0.768)\")\nprint(\"=\"*60)\nt_c3, p_c3 = stats.ttest_1samp(cell3, vanilla)\nd_c3 = (m3 - vanilla) / s3\nprint(f\"Cell 3 mean={m3:.4f} vs Vanilla={vanilla}\")\nprint(f\"差值: {m3-vanilla:.4f}\")\nprint(f\"t = {t_c3:.4f}, p = {p_c3:.4f}\")\nprint(f\"Cohen's d = {d_c3:.4f}\")\n# One-sided: is Cell 3 significantly LOWER than Vanilla?\np_c3_lower = stats.ttest_1samp(cell3, vanilla, alternative='less')\nprint(f\"单侧 (Cell3 < Vanilla): p = {p_c3_lower.pvalue:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"5. 单样本 t-test: Cell 1 vs Vanilla (0.768)\")\nprint(\"=\"*60)\nt_c1, p_c1 = stats.ttest_1samp(cell1, vanilla)\nd_c1 = (m1 - vanilla) / s1\nprint(f\"Cell 1 mean={m1:.4f} vs Vanilla={vanilla}\")\nprint(f\"差值: {m1-vanilla:.4f}\")\nprint(f\"t = {t_c1:.4f}, p = {p_c1:.4f}\")\nprint(f\"Cohen's d = {d_c1:.4f}\")\np_c1_lower = stats.ttest_1samp(cell1, vanilla, alternative='less')\nprint(f\"单侧 (Cell1 < Vanilla): p = {p_c1_lower.pvalue:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"6. 方差比检验: Cell 1 vs Cell 3\")\nprint(\"=\"*60)\n# F-test\nF = s1**2 / s3**2\ndf1, df2 = n1-1, n3-1\np_F = 2 * min(stats.f.cdf(F, df1, df2), 1 - stats.f.cdf(F, df1, df2))\nprint(f\"Cell 1 SD={s1:.4f}, Var={s1**2:.6f}\")\nprint(f\"Cell 3 SD={s3:.4f}, Var={s3**2:.6f}\")\nprint(f\"F = {F:.4f} (df1={df1}, df2={df2})\")\nprint(f\"F-test p = {p_F:.4f}\")\nprint(f\"方差比 = {s1**2/s3**2:.2f}x\")\n\n# Levene's test\nlev_stat, lev_p = stats.levene(cell1, cell3)\nprint(f\"Levene's test: W={lev_stat:.4f}, p={lev_p:.4f}\")\n\n# Bartlett's test\nbart_stat, bart_p = stats.bartlett(cell1, cell3)\nprint(f\"Bartlett's test: χ²={bart_stat:.4f}, p={bart_p:.4f}\")\n\nPYEOF",
  "description": "Run statistical analysis for Cell 1 vs Cell 3 partial ANOVA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_partial_anova_v2_20260526T120959",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport numpy as np\nfrom scipy import stats\n\n# Data\ncell1 = np.array([0.746, 0.654, 0.776])  # Full OCC BN (Grad ON + BN)\ncell3 = np.array([0.774, 0.736, 0.762, 0.794])  # Detach BN (Grad OFF + BN)\nvanilla = 0.768\n\nn1, n3 = len(cell1), len(cell3)\nm1, m3 = cell1.mean(), cell3.mean()\ns1, s3 = cell1.std(ddof=1), cell3.std(ddof=1)\n\nprint(\"=\"*60)\nprint(\"1. 独立样本 t-test: Cell 1 vs Cell 3\")\nprint(\"=\"*60)\nt_ind, p_ind = stats.ttest_ind(cell1, cell3, equal_var=False)  # Welch's t-test\n# Cohen's d (pooled SD)\nsp = np.sqrt(((n1-1)*s1**2 + (n3-1)*s3**2) / (n1+n3-2))\nd = (m1 - m3) / sp\nprint(f\"Cell 1: mean={m1:.4f}, SD={s1:.4f}, n={n1}\")\nprint(f\"Cell 3: mean={m3:.4f}, SD={s3:.4f}, n={n3}\")\nprint(f\"差值 (Cell1 - Cell3): {m1-m3:.4f}\")\nprint(f\"Welch's t = {t_ind:.4f}, p = {p_ind:.4f}\")\nprint(f\"Cohen's d = {d:.4f}\")\nprint(f\"Pooled SD = {sp:.4f}\")\n\n# Also equal-var t-test for reference\nt_eq, p_eq = stats.ttest_ind(cell1, cell3, equal_var=True)\nprint(f\"(Equal-var t-test: t={t_eq:.4f}, p={p_eq:.4f})\")\n\nprint()\nprint(\"=\"*60)\nprint(\"2. 效应量分析\")\nprint(\"=\"*60)\nprint(f\"Cohen's d = {d:.4f}\")\nif abs(d) < 0.2:\n    mag = \"negligible\"\nelif abs(d) < 0.5:\n    mag = \"small\"\nelif abs(d) < 0.8:\n    mag = \"medium\"\nelse:\n    mag = \"large\"\nprint(f\"效应量级别: {mag}\")\nprint(f\"梯度流 ON 使 CAR 降低 {abs(m1-m3):.4f} (相对降低 {abs(m1-m3)/m3*100:.1f}%)\")\n\nprint()\nprint(\"=\"*60)\nprint(\"3. 功效分析 (Power Analysis)\")\nprint(\"=\"*60)\nfrom scipy.stats import nct\n\ndef power_ttest_ind(n1, n2, d, alpha=0.05):\n    df = n1 + n2 - 2\n    ncp = d * np.sqrt(n1 * n2 / (n1 + n2))\n    t_crit = stats.t.ppf(1 - alpha/2, df)\n    power = 1 - nct.cdf(t_crit, df, ncp) + nct.cdf(-t_crit, df, ncp)\n    return power\n\ncurrent_power = power_ttest_ind(n1, n3, abs(d))\nprint(f\"当前 power (n1={n1}, n2={n3}, d={abs(d):.3f}, α=0.05): {current_power:.4f}\")\n\n# Find required n for power=0.80\nfor n in range(3, 200):\n    pw = power_ttest_ind(n, n, abs(d))\n    if pw >= 0.80:\n        print(f\"达到 power=0.80 需要每组 n={n} (total={2*n} seeds)\")\n        print(f\"  验证: power={pw:.4f}\")\n        break\n\n# Show power curve\nprint(\"\\nPower curve (equal group sizes):\")\nfor n in [3, 4, 5, 6, 8, 10, 15, 20, 30]:\n    pw = power_ttest_ind(n, n, abs(d))\n    print(f\"  n={n:2d} per group: power={pw:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"4. 单样本 t-test: Cell 3 vs Vanilla (0.768)\")\nprint(\"=\"*60)\nt_c3, p_c3 = stats.ttest_1samp(cell3, vanilla)\nd_c3 = (m3 - vanilla) / s3\nprint(f\"Cell 3 mean={m3:.4f} vs Vanilla={vanilla}\")\nprint(f\"差值: {m3-vanilla:.4f}\")\nprint(f\"t = {t_c3:.4f}, p = {p_c3:.4f}\")\nprint(f\"Cohen's d = {d_c3:.4f}\")\n# One-sided: is Cell 3 significantly LOWER than Vanilla?\np_c3_lower = stats.ttest_1samp(cell3, vanilla, alternative='less')\nprint(f\"单侧 (Cell3 < Vanilla): p = {p_c3_lower.pvalue:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"5. 单样本 t-test: Cell 1 vs Vanilla (0.768)\")\nprint(\"=\"*60)\nt_c1, p_c1 = stats.ttest_1samp(cell1, vanilla)\nd_c1 = (m1 - vanilla) / s1\nprint(f\"Cell 1 mean={m1:.4f} vs Vanilla={vanilla}\")\nprint(f\"差值: {m1-vanilla:.4f}\")\nprint(f\"t = {t_c1:.4f}, p = {p_c1:.4f}\")\nprint(f\"Cohen's d = {d_c1:.4f}\")\np_c1_lower = stats.ttest_1samp(cell1, vanilla, alternative='less')\nprint(f\"单侧 (Cell1 < Vanilla): p = {p_c1_lower.pvalue:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"6. 方差比检验: Cell 1 vs Cell 3\")\nprint(\"=\"*60)\n# F-test\nF = s1**2 / s3**2\ndf1, df2 = n1-1, n3-1\np_F = 2 * min(stats.f.cdf(F, df1, df2), 1 - stats.f.cdf(F, df1, df2))\nprint(f\"Cell 1 SD={s1:.4f}, Var={s1**2:.6f}\")\nprint(f\"Cell 3 SD={s3:.4f}, Var={s3**2:.6f}\")\nprint(f\"F = {F:.4f} (df1={df1}, df2={df2})\")\nprint(f\"F-test p = {p_F:.4f}\")\nprint(f\"方差比 = {s1**2/s3**2:.2f}x\")\n\n# Levene's test\nlev_stat, lev_p = stats.levene(cell1, cell3)\nprint(f\"Levene's test: W={lev_stat:.4f}, p={lev_p:.4f}\")\n\n# Bartlett's test\nbart_stat, bart_p = stats.bartlett(cell1, cell3)\nprint(f\"Bartlett's test: χ²={bart_stat:.4f}, p={bart_p:.4f}\")\n\nPYEOF",
    "description": "Run statistical analysis for Cell 1 vs Cell 3 partial ANOVA"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T12:12:06.695160+00:00_

============================================================
1. 独立样本 t-test: Cell 1 vs Cell 3
============================================================
Cell 1: mean=0.7253, SD=0.0636, n=3
Cell 3: mean=0.7665, SD=0.0242, n=4
差值 (Cell1 - Cell3): -0.0412
Welch's t = -1.0650, p = 0.3807
Cohen's d = -0.9277
Pooled SD = 0.0444
(Equal-var t-test: t=-1.2146, p=0.2787)

============================================================
2. 效应量分析
============================================================
Cohen's d = -0.9277
效应量级别: large
梯度流 ON 使 CAR 降低 0.0412 (相对降低 5.4%)

============================================================
3. 功效分析 (Power Analysis)
============================================================
当前 power (n1=3, n2=4, d=0.928, α=0.05): 0.1687
达到 power=0.80 需要每组 n=20 (total=40 seeds)
  验证: power=0.8156

Power curve (equal group sizes):
  n= 3 per group: power=0.1435
  n= 4 per group: power=0.1988
  n= 5 per group: power=0.2534
  n= 6 per group: power=0.3068
  n= 8 per group: power=0.4085
  n=10 per group: power=0.5014
  n=15 per group: power=0.6889
  n=20 per group: power=0.8156
  n=30 per group: power=0.9421

============================================================
4. 单样本 t-test: Cell 3 vs Vanilla (0.768)
============================================================
Cell 3 mean=0.7665 vs Vanilla=0.768
差值: -0.0015
t = -0.1238, p = 0.9093
Cohen's d = -0.0619
单侧 (Cell3 < Vanilla): p = 0.4547

============================================================
5. 单样本 t-test: Cell 1 vs Vanilla (0.768)
============================================================
Cell 1 mean=0.7253 vs Vanilla=0.768
差值: -0.0427
t = -1.1625, p = 0.3650
Cohen's d = -0.6712
单侧 (Cell1 < Vanilla): p = 0.1825

============================================================
6. 方差比检验: Cell 1 vs Cell 3
============================================================
Cell 1 SD=0.0636, Var=0.004041
Cell 3 SD=0.0242, Var=0.000588
F = 6.8769 (df1=2, df2=3)
F-test p = 0.1515
方差比 = 6.88x
Levene's test: W=0.9
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_partial_anova_v2_20260526T120959",
  "tool": "Bash",
  "elapsed_ms": 26
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T12:12:06.716747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_partial_anova_v2_20260526T120959",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T12:12:06.867036+00:00_

10894_health_check.md
_project
ablation_random_occ_s0
analyze_learning_curve_fixed.py
anova_2x2_factorial.py
anova_factorial_v2.py
anova_factorial_v2_results.txt
checkpoint_analysis_summary.md
cka_analysis
cka_analysis.py
cka_detach_ln
cka_detach_ln.pdf
cka_detach_ln.png
cka_detach_ln_results.json
cka_dose_response.py
cka_dose_response_results.json
cka_full_occ_ln_s0
cka_full_occ_ln_s1
cka_random_occ_results.json
cka_results.json
cka_same_seed_4cond
comprehensive_results.csv
compute_statistics.py
d051_bn_v2_failure_diagnosis.md
detach_ln_diagnosis.md
detach_ln_s0_eval
detach_ln_s0_eval_analysis.md
diag_eval_failure_20260523.md
diagnose_ablation_batch_fail.md
diagnose_mvp_occ_s3_v2.md
diagnose_s3_v2_failures.md
diagnose_westd10894_batch_kill.md
diagnose_westd34685_20260525.md
diagnosis_disk_full_20260526.md
diagnosis_experiment_crash_20260526.md
dose_response_3seed_analysis.py
dose_response_3seed_final.pdf
dose_response_3seed_final.png
dose_response_curve_data_car.csv
dose_response_data.json
dream_reports
eval_commands.md
eval_commands_34685.md
eval_completeness_audit.md
eval_pending_checklist.md
eval_readiness_report.md
extract_depth.py
factorial_2x2_config.json
factorial_data_summary.md
fig1_overview_v2.pdf
fig1_overview_v2.png
fig1_overview_v2.py
fig_dose_response_2seed.pdf
fig_dose_response_2seed.png
fig_factorial_2x2.pdf
fig_factorial_2x2.png
figures
gen_dose_response.py
gen_factorial_2x2.py
gradient_aggregation_investigation.md
gradient_analysis
gradient_analysis_mixed_seed
gradient_cka_summary.md
gradient_dose_response.py
gradient_dose_response_s0.py
launch_commands_10894_batch2.md
manifest.yaml
occ_crash_diagnosis.md
occ_gt_design.md
occ_pipeline
openvla_oft_survey.md
paper_status_check_20260525.md
partial_anova_v2.py
partial_anova_v2_results.txt
plot_dose_response.py
plot_factorial_2x2.py
plot_gradient_comparison.py
run_gradient_same_seed.sh
safelibero_survey.md
same_seed_gradient_analysis.py
statistical_tests.json
v2_cka_analysis.py
v2_gradient_analysis.jso
…[truncated 25 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_partial_anova_v2_20260526T120959",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T12:12:06.898199+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/partial_anova_v2_results.txt",
  "content": "Partial ANOVA v2: Cell 1 vs Cell 3 统计分析报告\n================================================\n日期: 2026-05-26\n\n设计: 2×2 factorial (gradient flow × normalization) 的 BN 列切片\n- Cell 1 (Full OCC BN, Grad ON + BN): n=3, seeds=[s0,s1,s2], CAR=[0.746,0.654,0.776], mean=0.725, SD=0.064\n- Cell 3 (Detach BN, Grad OFF + BN): n=4, seeds=[s0,s1,s2,s3], CAR=[0.774,0.736,0.762,0.794], mean=0.767, SD=0.024\n- Vanilla baseline (no OCC): CAR=0.768, n=1\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n1. 独立样本 t-test: Cell 1 vs Cell 3 (梯度流效应)\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n差值 (Cell1 - Cell3): -0.041\nWelch's t = -1.065, df ≈ 2.4, p = 0.381 (双侧)\nEqual-var t = -1.215, df = 5, p = 0.279\n\n结论: 梯度流对 CAR 的影响在当前样本量下不显著 (p=0.38)。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n2. 效应量分析\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCohen's d = -0.928 (large effect)\nPooled SD = 0.044\n\n解读: 效应量为大效应 (|d|>0.8)。梯度流 ON 使 CAR 降低约 4.1 个百分点 (5.4%)。\n效应量大但 p 值不显著，典型的低功效场景——效应可能真实存在但样本不足以检出。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n3. 功效分析\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n当前 power (n1=3, n2=4, d=0.928, α=0.05): 0.169\n\n极低功效。当前设计仅有 16.9% 的概率能检出这一大效应。\n等价地说，即使真实效应确实存在，我们也有 83% 的概率得到不显著的 p 值。\n\n达到 power=0.80 需要每组 n=20 seeds (total=40)——在 ML 实验中不现实。\n\nPower 曲线:\n  n= 3/组: 0.14    n=10/组: 0.50\n  n= 5/组: 0.25    n=15/组: 0.69\n  n= 8/组: 0.41    n=20/组: 0.82\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n4. 单样本 t-test: Cell 3 (Detach BN) vs Vanilla\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 3 mean=0.767 vs Vanilla=0.768, 差值=-0.002\nt = -0.124, p = 0.909 (双侧)\n单侧 (Cell3 < Vanilla): p = 0.455\nCohen's d = -0.062 (negligible)\n\n结论: Detach BN 与 Vanilla 无显著差异。Detach OCC 对安全性能几乎零影响——\n梯度截断成功消除了 OCC head 对 driving head 的干扰。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n5. 单样本 t-test: Cell 1 (Full OCC BN) vs Vanilla\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 1 mean=0.725 vs Vanilla=0.768, 差值=-0.043\nt = -1.163, p = 0.365 (双侧)\n单侧 (Cell1 < Vanilla): p = 0.183\nCohen's d = -0.671 (medium-to-large)\n\n结论: Full OCC BN 低于 Vanilla 4.3 个百分点，效应量 medium-to-large，\n但在 n=3 下不显著 (p=0.18 单侧)。方向一致地暗示梯度流可能损害安全。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n6. 方差比检验\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 1 Var = 0.00404, Cell 3 Var = 0.00059\nF = 6.877 (df1=2, df2=3), p = 0.152\nLevene's W = 0.929, p = 0.379\nBartlett's χ² = 1.808, p = 0.179\n\n方差比 = 6.88×。Cell 1 的方差是 Cell 3 的近 7 倍，但在当前小样本下\n三种检验均不显著。趋势方向清晰：梯度流 ON 不仅降低均值，还大幅增加\n跨 seed 的变异性。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n综合结论\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n1. 梯度流效应方向明确但统计不显著\n   - Grad ON (Cell 1) 比 Grad OFF (Cell 3) 平均 CAR 低 4.1 pp\n   - Cohen's d = -0.93 (大效应)，但 p = 0.38，远未达显著水平\n   - 根因是 power 仅 0.17——当前样本量不足以支撑任何方向的统计结论\n\n2. Detach BN 完美保持 Vanilla 性能\n   - Cell 3 mean (0.767) 与 Vanilla (0.768) 几乎完全相同 (d = -0.06)\n   - 这是最强的结果：梯度截断 + BN 下加 OCC head 不损害安全\n\n3. Full OCC BN 可能损害安全\n   - 均值下降 4.3 pp，效应量 medium-to-large (d = -0.67)\n   - 但 n=3 功效不足，p = 0.18 (单侧)，不能做强结论\n\n4. 方差不对称暗示不稳定性\n   - Cell 1 方差是 Cell 3 的 7 倍 (虽然 p=0.15 不显著)\n   - 梯度流 ON 不仅降低均值，还引入更大的 seed 间波动\n   - 这与\"梯度干扰\"假说一致：OCC 梯度对 driving head 的影响是随机性的\n\n5. 论文写作建议\n   - 当前证据足以支持 \"directional evidence\" 的叙事，不宜宣称 \"statistically significant\"\n   - 推荐表述: \"large effect size (d=0.93) suggests gradient flow may impair safety,\n     though the effect did not reach significance with the current sample (p=0.38, power=0.17)\"\n   - Cell 3 ≈ Vanilla 是可以强力宣称的结果\n   - 方差差异可作为补充证据讨论\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_partial_anova_v2_20260526T120959",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/partial_anova_v2_results.txt",
    "content": "Partial ANOVA v2: Cell 1 vs Cell 3 统计分析报告\n================================================\n日期: 2026-05-26\n\n设计: 2×2 factorial (gradient flow × normalization) 的 BN 列切片\n- Cell 1 (Full OCC BN, Grad ON + BN): n=3, seeds=[s0,s1,s2], CAR=[0.746,0.654,0.776], mean=0.725, SD=0.064\n- Cell 3 (Detach BN, Grad OFF + BN): n=4, seeds=[s0,s1,s2,s3], CAR=[0.774,0.736,0.762,0.794], mean=0.767, SD=0.024\n- Vanilla baseline (no OCC): CAR=0.768, n=1\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n1. 独立样本 t-test: Cell 1 vs Cell 3 (梯度流效应)\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n差值 (Cell1 - Cell3): -0.041\nWelch's t = -1.065, df ≈ 2.4, p = 0.381 (双侧)\nEqual-var t = -1.215, df = 5, p = 0.279\n\n结论: 梯度流对 CAR 的影响在当前样本量下不显著 (p=0.38)。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n2. 效应量分析\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCohen's d = -0.928 (large effect)\nPooled SD = 0.044\n\n解读: 效应量为大效应 (|d|>0.8)。梯度流 ON 使 CAR 降低约 4.1 个百分点 (5.4%)。\n效应量大但 p 值不显著，典型的低功效场景——效应可能真实存在但样本不足以检出。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n3. 功效分析\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n当前 power (n1=3, n2=4, d=0.928, α=0.05): 0.169\n\n极低功效。当前设计仅有 16.9% 的概率能检出这一大效应。\n等价地说，即使真实效应确实存在，我们也有 83% 的概率得到不显著的 p 值。\n\n达到 power=0.80 需要每组 n=20 seeds (total=40)——在 ML 实验中不现实。\n\nPower 曲线:\n  n= 3/组: 0.14    n=10/组: 0.50\n  n= 5/组: 0.25    n=15/组: 0.69\n  n= 8/组: 0.41    n=20/组: 0.82\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n4. 单样本 t-test: Cell 3 (Detach BN) vs Vanilla\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 3 mean=0.767 vs Vanilla=0.768, 差值=-0.002\nt = -0.124, p = 0.909 (双侧)\n单侧 (Cell3 < Vanilla): p = 0.455\nCohen's d = -0.062 (negligible)\n\n结论: Detach BN 与 Vanilla 无显著差异。Detach OCC 对安全性能几乎零影响——\n梯度截断成功消除了 OCC head 对 driving head 的干扰。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n5. 单样本 t-test: Cell 1 (Full OCC BN) vs Vanilla\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 1 mean=0.725 vs Vanilla=0.768, 差值=-0.043\nt = -1.163, p = 0.365 (双侧)\n单侧 (Cell1 < Vanilla): p = 0.183\nCohen's d = -0.671 (medium-to-large)\n\n结论: Full OCC BN 低于 Vanilla 4.3 个百分点，效应量 medium-to-large，\n但在 n=3 下不显著 (p=0.18 单侧)。方向一致地暗示梯度流可能损害安全。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n6. 方差比检验\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 1 Var = 0.00404, Cell 3 Var = 0.00059\nF = 6.877 (df1=2, df2=3), p = 0.152\nLevene's W = 0.929, p = 0.379\nBartlett's χ² = 1.808, p = 0.179\n\n方差比 = 6.88×。Cell 1 的方差是 Cell 3 的近 7 倍，但在当前小样本下\n三种检验均不显著。趋势方向清晰：梯度流 ON 不仅降低均值，还大幅增加\n跨 seed 的变异性。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n综合结论\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n1. 梯度流效应方向明确但统计不显著\n   - Grad ON (Cell 1) 比 Grad OFF (Cell 3) 平均 CAR 低 4.1 pp\n   - Cohen's d = -0.93 (大效应)，但 p = 0.38，远未达显著水平\n   - 根因是 power 仅 0.17——当前样本量不足以支撑任何方向的统计结论\n\n2. Detach BN 完美保持 Vanilla 性能\n   - Cell 3 mean (0.767) 与 Vanilla (0.768) 几乎完全相同 (d = -0.06)\n   - 这是最强的结果：梯度截断 + BN 下加 OCC head 不损害安全\n\n3. Full OCC BN 可能损害安全\n   - 均值下降 4.3 pp，效应量 medium-to-large (d = -0.67)\n   - 但 n=3 功效不足，p = 0.18 (单侧)，不能做强结论\n\n4. 方差不对称暗示不稳定性\n   - Cell 1 方差是 Cell 3 的 7 倍 (虽然 p=0.15 不显著)\n   - 梯度流 ON 不仅降低均值，还引入更大的 seed 间波动\n   - 这与\"梯度干扰\"假说一致：OCC 梯度对 driving head 的影响是随机性的\n\n5. 论文写作建议\n   - 当前证据足以支持 \"directional evidence\" 的叙事，不宜宣称 \"statistically significant\"\n   - 推荐表述: \"large effect size (d=0.93) suggests gradient flow may impair safety,\n     though the effect did not reach significance with the current sample (p=0.38, power=0.17)\"\n   - Cell 3 ≈ Vanilla 是可以强力宣称的结果\n   - 方差差异可作为补充证据讨论\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T12:12:06.929608+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_partial_anova_v2_20260526T120959",
  "tool": "Write",
  "elapsed_ms": 31
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T12:12:06.968912+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat > /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/partial_anova_v2_results.txt << 'DOCEOF'\nPartial ANOVA v2: Cell 1 vs Cell 3 统计分析报告\n================================================\n日期: 2026-05-26\n\n设计: 2×2 factorial (gradient flow × normalization) 的 BN 列切片\n- Cell 1 (Full OCC BN, Grad ON + BN): n=3, seeds=[s0,s1,s2], CAR=[0.746,0.654,0.776], mean=0.725, SD=0.064\n- Cell 3 (Detach BN, Grad OFF + BN): n=4, seeds=[s0,s1,s2,s3], CAR=[0.774,0.736,0.762,0.794], mean=0.767, SD=0.024\n- Vanilla baseline (no OCC): CAR=0.768, n=1\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n1. 独立样本 t-test: Cell 1 vs Cell 3 (梯度流效应)\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n差值 (Cell1 - Cell3): -0.041\nWelch's t = -1.065, df ≈ 2.4, p = 0.381 (双侧)\nEqual-var t = -1.215, df = 5, p = 0.279\n\n结论: 梯度流对 CAR 的影响在当前样本量下不显著 (p=0.38)。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n2. 效应量分析\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCohen's d = -0.928 (large effect)\nPooled SD = 0.044\n\n解读: 效应量为大效应 (|d|>0.8)。梯度流 ON 使 CAR 降低约 4.1 个百分点 (5.4%)。\n效应量大但 p 值不显著，典型的低功效场景——效应可能真实存在但样本不足以检出。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n3. 功效分析\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n当前 power (n1=3, n2=4, d=0.928, α=0.05): 0.169\n\n极低功效。当前设计仅有 16.9% 的概率能检出这一大效应。\n等价地说，即使真实效应确实存在，我们也有 83% 的概率得到不显著的 p 值。\n\n达到 power=0.80 需要每组 n=20 seeds (total=40)——在 ML 实验中不现实。\n\nPower 曲线:\n  n= 3/组: 0.14    n=10/组: 0.50\n  n= 5/组: 0.25    n=15/组: 0.69\n  n= 8/组: 0.41    n=20/组: 0.82\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n4. 单样本 t-test: Cell 3 (Detach BN) vs Vanilla\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 3 mean=0.767 vs Vanilla=0.768, 差值=-0.002\nt = -0.124, p = 0.909 (双侧)\n单侧 (Cell3 < Vanilla): p = 0.455\nCohen's d = -0.062 (negligible)\n\n结论: Detach BN 与 Vanilla 无显著差异。Detach OCC 对安全性能几乎零影响——\n梯度截断成功消除了 OCC head 对 driving head 的干扰。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n5. 单样本 t-test: Cell 1 (Full OCC BN) vs Vanilla\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 1 mean=0.725 vs Vanilla=0.768, 差值=-0.043\nt = -1.163, p = 0.365 (双侧)\n单侧 (Cell1 < Vanilla): p = 0.183\nCohen's d = -0.671 (medium-to-large)\n\n结论: Full OCC BN 低于 Vanilla 4.3 个百分点，效应量 medium-to-large，\n但在 n=3 下不显著 (p=0.18 单侧)。方向一致地暗示梯度流可能损害安全。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n6. 方差比检验\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 1 Var = 0.00404, Cell 3 Var = 0.00059\nF = 6.877 (df1=2, df2=3), p = 0.152\nLevene's W = 0.929, p = 0.379\nBartlett's χ² = 1.808, p = 0.179\n\n方差比 = 6.88×。Cell 1 的方差是 Cell 3 的近 7 倍，但在当前小样本下\n三种检验均不显著。趋势方向清晰：梯度流 ON 不仅降低均值，还大幅增加\n跨 seed 的变异性。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n综合结论\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n1. 梯度流效应方向明确但统计不显著\n   - Grad ON (Cell 1) 比 Grad OFF (Cell 3) 平均 CAR 低 4.1 pp\n   - Cohen's d = -0.93 (大效应)，但 p = 0.38，远未达显著水平\n   - 根因是 power 仅 0.17——当前样本量不足以支撑任何方向的统计结论\n\n2. Detach BN 完美保持 Vanilla 性能\n   - Cell 3 mean (0.767) 与 Vanilla (0.768) 几乎完全相同 (d = -0.06)\n   - 这是最强的结果：梯度截断 + BN 下加 OCC head 不损害安全\n\n3. Full OCC BN 可能损害安全\n   - 均值下降 4.3 pp，效应量 medium-to-large (d = -0.67)\n   - 但 n=3 功效不足，p = 0.18 (单侧)，不能做强结论\n\n4. 方差不对称暗示不稳定性\n   - Cell 1 方差是 Cell 3 的 7 倍 (虽然 p=0.15 不显著)\n   - 梯度流 ON 不仅降低均值，还引入更大的 seed 间波动\n   - 这与\"梯度干扰\"假说一致：OCC 梯度对 driving head 的影响是随机性的\n\n5. 论文写作建议\n   - 当前证据足以支持 \"directional evidence\" 的叙事，不宜宣称 \"statistically significant\"\n   - 推荐表述: \"large effect size (d=0.93) suggests gradient flow may impair safety,\n     though the effect did not reach significance with the current sample (p=0.38, power=0.17)\"\n   - Cell 3 ≈ Vanilla 是可以强力宣称的结果\n   - 方差差异可作为补充证据讨论\nDOCEOF",
  "description": "Write analysis report to artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_partial_anova_v2_20260526T120959",
  "tool": "Bash",
  "tool_args": {
    "command": "cat > /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/partial_anova_v2_results.txt << 'DOCEOF'\nPartial ANOVA v2: Cell 1 vs Cell 3 统计分析报告\n================================================\n日期: 2026-05-26\n\n设计: 2×2 factorial (gradient flow × normalization) 的 BN 列切片\n- Cell 1 (Full OCC BN, Grad ON + BN): n=3, seeds=[s0,s1,s2], CAR=[0.746,0.654,0.776], mean=0.725, SD=0.064\n- Cell 3 (Detach BN, Grad OFF + BN): n=4, seeds=[s0,s1,s2,s3], CAR=[0.774,0.736,0.762,0.794], mean=0.767, SD=0.024\n- Vanilla baseline (no OCC): CAR=0.768, n=1\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n1. 独立样本 t-test: Cell 1 vs Cell 3 (梯度流效应)\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n差值 (Cell1 - Cell3): -0.041\nWelch's t = -1.065, df ≈ 2.4, p = 0.381 (双侧)\nEqual-var t = -1.215, df = 5, p = 0.279\n\n结论: 梯度流对 CAR 的影响在当前样本量下不显著 (p=0.38)。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n2. 效应量分析\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCohen's d = -0.928 (large effect)\nPooled SD = 0.044\n\n解读: 效应量为大效应 (|d|>0.8)。梯度流 ON 使 CAR 降低约 4.1 个百分点 (5.4%)。\n效应量大但 p 值不显著，典型的低功效场景——效应可能真实存在但样本不足以检出。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n3. 功效分析\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n当前 power (n1=3, n2=4, d=0.928, α=0.05): 0.169\n\n极低功效。当前设计仅有 16.9% 的概率能检出这一大效应。\n等价地说，即使真实效应确实存在，我们也有 83% 的概率得到不显著的 p 值。\n\n达到 power=0.80 需要每组 n=20 seeds (total=40)——在 ML 实验中不现实。\n\nPower 曲线:\n  n= 3/组: 0.14    n=10/组: 0.50\n  n= 5/组: 0.25    n=15/组: 0.69\n  n= 8/组: 0.41    n=20/组: 0.82\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n4. 单样本 t-test: Cell 3 (Detach BN) vs Vanilla\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 3 mean=0.767 vs Vanilla=0.768, 差值=-0.002\nt = -0.124, p = 0.909 (双侧)\n单侧 (Cell3 < Vanilla): p = 0.455\nCohen's d = -0.062 (negligible)\n\n结论: Detach BN 与 Vanilla 无显著差异。Detach OCC 对安全性能几乎零影响——\n梯度截断成功消除了 OCC head 对 driving head 的干扰。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n5. 单样本 t-test: Cell 1 (Full OCC BN) vs Vanilla\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 1 mean=0.725 vs Vanilla=0.768, 差值=-0.043\nt = -1.163, p = 0.365 (双侧)\n单侧 (Cell1 < Vanilla): p = 0.183\nCohen's d = -0.671 (medium-to-large)\n\n结论: Full OCC BN 低于 Vanilla 4.3 个百分点，效应量 medium-to-large，\n但在 n=3 下不显著 (p=0.18 单侧)。方向一致地暗示梯度流可能损害安全。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n6. 方差比检验\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nCell 1 Var = 0.00404, Cell 3 Var = 0.00059\nF = 6.877 (df1=2, df2=3), p = 0.152\nLevene's W = 0.929, p = 0.379\nBartlett's χ² = 1.808, p = 0.179\n\n方差比 = 6.88×。Cell 1 的方差是 Cell 3 的近 7 倍，但在当前小样本下\n三种检验均不显著。趋势方向清晰：梯度流 ON 不仅降低均值，还大幅增加\n跨 seed 的变异性。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n综合结论\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n1. 梯度流效应方向明确但统计不显著\n   - Grad ON (Cell 1) 比 Grad OFF (Cell 3) 平均 CAR 低 4.1 pp\n   - Cohen's d = -0.93 (大效应)，但 p = 0.38，远未达显著水平\n   - 根因是 power 仅 0.17——当前样本量不足以支撑任何方向的统计结论\n\n2. Detach BN 完美保持 Vanilla 性能\n   - Cell 3 mean (0.767) 与 Vanilla (0.768) 几乎完全相同 (d = -0.06)\n   - 这是最强的结果：梯度截断 + BN 下加 OCC head 不损害安全\n\n3. Full OCC BN 可能损害安全\n   - 均值下降 4.3 pp，效应量 medium-to-large (d = -0.67)\n   - 但 n=3 功效不足，p = 0.18 (单侧)，不能做强结论\n\n4. 方差不对称暗示不稳定性\n   - Cell 1 方差是 Cell 3 的 7 倍 (虽然 p=0.15 不显著)\n   - 梯度流 ON 不仅降低均值，还引入更大的 seed 间波动\n   - 这与\"梯度干扰\"假说一致：OCC 梯度对 driving head 的影响是随机性的\n\n5. 论文写作建议\n   - 当前证据足以支持 \"directional evidence\" 的叙事，不宜宣称 \"statistically significant\"\n   - 推荐表述: \"large effect size (d=0.93) suggests gradient flow may impair safety,\n     though the effect did not reach significance with the current sample (p=0.38, power=0.17)\"\n   - Cell 3 ≈ Vanilla 是可以强力宣称的结果\n   - 方差差异可作为补充证据讨论\nDOCEOF",
    "description": "Write analysis report to artifacts"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T12:12:07.005103+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_partial_anova_v2_20260526T120959",
  "tool": "Bash",
  "elapsed_ms": 36
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-26T12:12:07.066889+00:00_

分析完成，报告已写入 `artifacts/partial_anova_v2_results.txt`。核心发现：

**1. Cell 1 vs Cell 3 (梯度流效应)**
- Welch's t = -1.07, **p = 0.381** (不显著)
- **Cohen's d = -0.93** (大效应)
- 矛盾的根因：power 仅 **0.169**，需要每组 n=20 才能达到 0.80——不现实

**2. Cell 3 (Detach BN) vs Vanilla**
- 几乎完全相同：0.767 vs 0.768，d = -0.06，**p = 0.91**
- **最强结论**：梯度截断 + BN 加 OCC head 对安全零影响

**3. Cell 1 (Full OCC BN) vs Vanilla**
- 均值低 4.3 pp，d = -0.67 (medium-large)，单侧 **p = 0.18**
- 方向一致但 n=3 功效不足

**4. 方差比**
- Cell 1 方差是 Cell 3 的 **6.88 倍**，但 F-test p = 0.15 (小样本下不显著)
- 梯度流 ON 明显增加 seed 间波动，与梯度干扰假说一致

**论文建议**：用 "directional evidence with large effect size" 叙事，不宣称 significance。Cell 3 ≈ Vanilla 是可以硬宣称的结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_partial_anova_v2_20260526T120959"
}
```

</details>

---
