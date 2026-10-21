# paper p0 2 5 statistics phase2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_p0-2-5-statistics-phase2_20260528T053501.jsonl`
- **Structured JSON:** [`822a60d2c18691a9c1c3.json`](../../sessions/82/822a60d2c18691a9c1c3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-28T05:40:12.318403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T05:40:12.318986+00:00_

1	#!/usr/bin/env python3
2	"""Auto-switch paper text based on λ=0.1 s2 30K eval result.
3	
4	Usage:
5	  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0 --dry-run
6	  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0
7	"""
8	import argparse
9	import subprocess
10	import sys
11	from itertools import combinations
12	from math import comb, sqrt
13	from pathlib import Path
14	
15	NULL_VALUES = [56.5, 52.5, 55, 57, 54, 52.5]
16	NULL_MEAN = sum(NULL_VALUES) / len(NULL_VALUES)
17	NULL_STD = (sum((x - NULL_MEAN) ** 2 for x in NULL_VALUES) / 5) ** 0.5
18	
19	S0_CAR, S1_CAR = 58.0, 58.5
20	S0_TSR, S1_TSR = 47.0, 49.0
21	
22	PAPER_DIR = Path(__file__).resolve().parent.parent / "docs" / "paper"
23	
24	
25	def mean(v):
26	    return sum(v) / len(v)
27	
28	
29	def std_b(v):
30	    m = mean(v)
31	    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5
32	
33	
34	def perm_test(null_vals, treat_vals):
35	    pool = null_vals + treat_vals
36	    k = len(treat_vals)
37	    obs = mean(treat_vals)
38	    mu = mean(pool)
39	    dev = abs(obs - mu)
40	    n = comb(len(pool), k)
41	    ge = tw = 0
42	    for c in combinations(pool, k):
43	        m = mean(c)
44	        if m >= obs:
45	            ge += 1
46	        if abs(m - mu) >= dev - 1e-12:
47	            tw += 1
48	    return ge / n, tw / n, n
49	
50	
51	def fill(tpl, vals):
52	    for k, v in vals.items():
53	        tpl = tpl.replace("{" + k + "}", str(v))
54	    return tpl
55	
56	
57	def safe_replace(content, old, new, label):
58	    n = content.count(old)
59	    if n == 0:
60	        print(f"  !! [{label}] NOT FOUND")
61	        return content, False
62	    if n > 1:
63	        print(f"  !! [{label}] found {n}x")
64	        return content, False
65	    return content.replace(old, new), True
66	
67	
68	def get_replacements(scenario, v):
69	    R = []
70	    is_c = scenario == "C"
71	
72	    # 1. abstract.tex L5 (training results)
73	    old = (
74	        r"collision-free demonstrations alone account for all measured av
…[truncated 24040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T05:40:12.319197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T05:40:12.319380+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 3 & 51.5\,$\pm$\,0.0 & 54.67\,$\pm$\,2.02 & 0.391 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{Single seed (s2); 
…[truncated 2334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T05:40:12.319593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T05:40:12.319882+00:00_

1	\section{Displacement Distribution}
2	\label{sec:appendix_displacement}
3	
4	\begin{figure}[h]
5	\centering
6	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
7	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
8	\label{fig:displacement}
9	\end{figure}
10	
11	\section{Displacement Threshold Sensitivity Analysis}
12	\label{sec:appendix_threshold}
13	
14	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% frozen rate even at the most conservative setting.
15	
16	\begin{table}[h]
17	\centering
18	\caption{Frozen rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
19	\label{tab:threshold_sensitivity}
20	\begin{tabular}{lccc}
21	\toprule
22	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
23	\midrule
24	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
25	0.1 mm  & 99.6 & 0.0 & 0.0 \\
26	1.0 mm  & 100.0 & 0.0 & 0.0 \\
27	10 mm   & 100.0 & 0.0 & 0.0 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.
33	
34	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\
…[truncated 22842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T05:40:12.320108+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nfrom itertools import combinations\nfrom math import comb, sqrt\nfrom scipy import stats\n\n# === Null A: LoRA-only (3 seeds) vs λ=0.1 (3 seeds) ===\nnull_a = [56.5, 52.5, 55.0]\ntreat = [58.0, 58.5, 54.5]\npool_a = null_a + treat\nk = 3\nobs = sum(treat)/k\nmu_a = sum(pool_a)/len(pool_a)\ndev_a = abs(obs - mu_a)\nge_a = tw_a = 0\nfor c in combinations(pool_a, k):\n    m = sum(c)/k\n    if m >= obs: ge_a += 1\n    if abs(m - mu_a) >= dev_a - 1e-12: tw_a += 1\nn_a = comb(len(pool_a), k)\nprint(f\"Null A: p_one={ge_a/n_a:.3f}, p_two={tw_a/n_a:.3f}, n_combos={n_a}\")\nprint(f\"  obs_mean={obs:.2f}, pool_mean={mu_a:.4f}, dev={dev_a:.4f}\")\nprint(f\"  ge={ge_a}, tw={tw_a}\")\n\n# === Null B: LoRA + λ=0.005 (6 seeds) vs λ=0.1 (3 seeds) ===\nnull_b = [56.5, 52.5, 55.0, 57.0, 54.0, 52.5]\npool_b = null_b + treat\nobs_b = sum(treat)/k\nmu_b = sum(pool_b)/len(pool_b)\ndev_b = abs(obs_b - mu_b)\nge_b = tw_b = 0\nfor c in combinations(pool_b, k):\n    m = sum(c)/k\n    if m >= obs_b: ge_b += 1\n    if abs(m - mu_b) >= dev_b - 1e-12: tw_b += 1\nn_b = comb(len(pool_b), k)\nprint(f\"\\nNull B: p_one={ge_b/n_b:.3f}, p_two={tw_b/n_b:.3f}, n_combos={n_b}\")\n\n# === λ=0.01 exact permutation p-value ===\nlora_only = [56.5, 52.5, 55.0]\nlam001 = [57.0, 57.5, 54.5]\npool_01 = lora_only + lam001\nobs_01 = sum(lam001)/k\nmu_01 = sum(pool_01)/len(pool_01)\ndev_01 = abs(obs_01 - mu_01)\nge_01 = tw_01 = 0\nfor c in combinations(pool_01, k):\n    m = sum(c)/k\n    if m >= obs_01: ge_01 += 1\n    if abs(m - mu_01) >= dev_01 - 1e-12: tw_01 += 1\nn_01 = comb(len(pool_01), k)\nprint(f\"\\nλ=0.01 vs LoRA-only (Null A): p_one={ge_01/n_01:.3f}, p_two={tw_01/n_01:.3f}, n_combos={n_01}\")\nprint(f\"  obs_mean={obs_01:.4f}, pool_mean={mu_01:.4f}\")\n\n# === Power Analysis ===\n# n=3 per group, σ≈2.0pp, α=0.05 one-tailed\n# MDE at 80% power using t-test approximation\nn_per = 3\nsigma = 2.0\nalpha = 0.05\ndf = 2 * n_per - 2  # df=4\nt_crit = stats.t.ppf(1 - alpha, df)\nt_power = stats.t.ppf(0.80, df)  # for 80% power\n# MDE = (t_crit + t_power) * sigma * sqrt(2/n)\nMDE = (t_crit + t_power) * sigma * sqrt(2/n_per)\nprint(f\"\\nPower Analysis:\")\nprint(f\"  df={df}, t_crit(0.05,{df})={t_crit:.3f}, t_80%({df})={t_power:.3f}\")\nprint(f\"  MDE at 80% power = ({t_crit:.3f} + {t_power:.3f}) * {sigma} * sqrt(2/{n_per})\")\nprint(f\"  MDE = {MDE:.1f} pp\")\nprint(f\"  Observed effect = {obs - sum(null_a)/k:.1f} pp\")\n\n# Also compute with two-tailed alpha\nt_crit_2 = stats.t.ppf(1 - alpha/2, df)\nMDE_2 = (t_crit_2 + t_power) * sigma * sqrt(2/n_per)\nprint(f\"  MDE (two-tailed α=0.05) = {MDE_2:.1f} pp\")\n\n# Also: permutation-based power is harder to compute exactly, \n# so t-test approx is standard\nprint(f\"\\n  Observed effect (λ=0.1 - LoRA mean): {sum(treat)/k - sum(null_a)/k:.2f} pp\")\n\nPYEOF\n",
  "description": "Compute exact permutation p-values and power analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nfrom itertools import combinations\nfrom math import comb, sqrt\nfrom scipy import stats\n\n# === Null A: LoRA-only (3 seeds) vs λ=0.1 (3 seeds) ===\nnull_a = [56.5, 52.5, 55.0]\ntreat = [58.0, 58.5, 54.5]\npool_a = null_a + treat\nk = 3\nobs = sum(treat)/k\nmu_a = sum(pool_a)/len(pool_a)\ndev_a = abs(obs - mu_a)\nge_a = tw_a = 0\nfor c in combinations(pool_a, k):\n    m = sum(c)/k\n    if m >= obs: ge_a += 1\n    if abs(m - mu_a) >= dev_a - 1e-12: tw_a += 1\nn_a = comb(len(pool_a), k)\nprint(f\"Null A: p_one={ge_a/n_a:.3f}, p_two={tw_a/n_a:.3f}, n_combos={n_a}\")\nprint(f\"  obs_mean={obs:.2f}, pool_mean={mu_a:.4f}, dev={dev_a:.4f}\")\nprint(f\"  ge={ge_a}, tw={tw_a}\")\n\n# === Null B: LoRA + λ=0.005 (6 seeds) vs λ=0.1 (3 seeds) ===\nnull_b = [56.5, 52.5, 55.0, 57.0, 54.0, 52.5]\npool_b = null_b + treat\nobs_b = sum(treat)/k\nmu_b = sum(pool_b)/len(pool_b)\ndev_b = abs(obs_b - mu_b)\nge_b = tw_b = 0\nfor c in combinations(pool_b, k):\n    m = sum(c)/k\n    if m >= obs_b: ge_b += 1\n    if abs(m - mu_b) >= dev_b - 1e-12: tw_b += 1\nn_b = comb(len(pool_b), k)\nprint(f\"\\nNull B: p_one={ge_b/n_b:.3f}, p_two={tw_b/n_b:.3f}, n_combos={n_b}\")\n\n# === λ=0.01 exact permutation p-value ===\nlora_only = [56.5, 52.5, 55.0]\nlam001 = [57.0, 57.5, 54.5]\npool_01 = lora_only + lam001\nobs_01 = sum(lam001)/k\nmu_01 = sum(pool_01)/len(pool_01)\ndev_01 = abs(obs_01 - mu_01)\nge_01 = tw_01 = 0\nfor c in combinations(pool_01, k):\n    m = sum(c)/k\n    if m >= obs_01: ge_01 += 1\n    if abs(m - mu_01) >= dev_01 - 1e-12: tw_01 += 1\nn_01 = comb(len(pool_01), k)\nprint(f\"\\nλ=0.01 vs LoRA-only (Null A): p_one={ge_01/n_01:.3f}, p_two={tw_01/n_01:.3f}, n_combos={n_01}\")\nprint(f\"  obs_mean={obs_01:.4f}, pool_mean={mu_01:.4f}\")\n\n# === Power Analysis ===\n# n=3 per group, σ≈2.0pp, α=0.05 one-tailed\n# MDE at 80% power using t-test approximation\nn_per = 3\nsigma = 2.0\nalpha = 0.05\ndf = 2 * n_per - 2  # df=4\nt_crit = stats.t.ppf(1 - alpha, df)\nt_power = stats.t.ppf(0.80, df)  # for 80% power\n# MDE = (t_crit + t_power) * sigma * sqrt(2/n)\nMDE = (t_crit + t_power) * sigma * sqrt(2/n_per)\nprint(f\"\\nPower Analysis:\")\nprint(f\"  df={df}, t_crit(0.05,{df})={t_crit:.3f}, t_80%({df})={t_power:.3f}\")\nprint(f\"  MDE at 80% power = ({t_crit:.3f} + {t_power:.3f}) * {sigma} * sqrt(2/{n_per})\")\nprint(f\"  MDE = {MDE:.1f} pp\")\nprint(f\"  Observed effect = {obs - sum(null_a)/k:.1f} pp\")\n\n# Also compute with two-tailed alpha\nt_crit_2 = stats.t.ppf(1 - alpha/2, df)\nMDE_2 = (t_crit_2 + t_power) * sigma * sqrt(2/n_per)\nprint(f\"  MDE (two-tailed α=0.05) = {MDE_2:.1f} pp\")\n\n# Also: permutation-based power is harder to compute exactly, \n# so t-test approx is standard\nprint(f\"\\n  Observed effect (λ=0.1 - LoRA mean): {sum(treat)/k - sum(null_a)/k:.2f} pp\")\n\nPYEOF\n",
    "description": "Compute exact permutation p-values and power analysis"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T05:40:12.320287+00:00_

Null A: p_one=0.150, p_two=0.300, n_combos=20
  obs_mean=57.00, pool_mean=55.8333, dev=1.1667
  ge=3, tw=6

Null B: p_one=0.071, p_two=0.131, n_combos=84

λ=0.01 vs LoRA-only (Null A): p_one=0.200, p_two=0.400, n_combos=20
  obs_mean=56.3333, pool_mean=55.5000

Power Analysis:
  df=4, t_crit(0.05,4)=2.132, t_80%(4)=0.941
  MDE at 80% power = (2.132 + 0.941) * 2.0 * sqrt(2/3)
  MDE = 5.0 pp
  Observed effect = 2.3 pp
  MDE (two-tailed α=0.05) = 6.1 pp

  Observed effect (λ=0.1 - LoRA mean): 2.33 pp

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T05:40:12.320536+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nfrom itertools import combinations\nfrom math import comb\n\n# λ=0.01 vs Null B (LoRA + λ=0.005, 6 values)\nnull_b = [56.5, 52.5, 55.0, 57.0, 54.0, 52.5]\nlam001 = [57.0, 57.5, 54.5]\npool = null_b + lam001\nk = 3\nobs = sum(lam001)/k\nmu = sum(pool)/len(pool)\ndev = abs(obs - mu)\nge = tw = 0\nfor c in combinations(pool, k):\n    m = sum(c)/k\n    if m >= obs: ge += 1\n    if abs(m - mu) >= dev - 1e-12: tw += 1\nn = comb(len(pool), k)\nprint(f\"λ=0.01 vs Null B: p_one={ge/n:.3f}, p_two={tw/n:.3f}, n_combos={n}\")\nprint(f\"  obs_mean={obs:.4f}, pool_mean={mu:.4f}\")\nprint(f\"  ge={ge}, tw={tw}\")\n\n# Also enumerate for Null A to confirm\nnull_a = [56.5, 52.5, 55.0]\npool_a = null_a + lam001\nobs_a = sum(lam001)/k\nmu_a = sum(pool_a)/len(pool_a)\ndev_a = abs(obs_a - mu_a)\nge_a = tw_a = 0\nfor c in combinations(pool_a, k):\n    m = sum(c)/k\n    if m >= obs_a: ge_a += 1\n    if abs(m - mu_a) >= dev_a - 1e-12: tw_a += 1\nn_a = comb(len(pool_a), k)\nprint(f\"\\nλ=0.01 vs Null A: p_one={ge_a/n_a:.3f}, p_two={tw_a/n_a:.3f}, n_combos={n_a}\")\n\n# Enumerate all combos for Null A to double-check\nprint(\"\\nAll C(6,3) combos for λ=0.01 Null A test:\")\nfor c in combinations(pool_a, k):\n    m = sum(c)/k\n    flag_ge = \" >= obs\" if m >= obs_a else \"\"\n    flag_tw = \" |dev|>=\" if abs(m - mu_a) >= dev_a - 1e-12 else \"\"\n    print(f\"  {c} -> mean={m:.4f}{flag_ge}{flag_tw}\")\n\nPYEOF\n",
  "description": "Compute λ=0.01 permutation test against both null pools"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nfrom itertools import combinations\nfrom math import comb\n\n# λ=0.01 vs Null B (LoRA + λ=0.005, 6 values)\nnull_b = [56.5, 52.5, 55.0, 57.0, 54.0, 52.5]\nlam001 = [57.0, 57.5, 54.5]\npool = null_b + lam001\nk = 3\nobs = sum(lam001)/k\nmu = sum(pool)/len(pool)\ndev = abs(obs - mu)\nge = tw = 0\nfor c in combinations(pool, k):\n    m = sum(c)/k\n    if m >= obs: ge += 1\n    if abs(m - mu) >= dev - 1e-12: tw += 1\nn = comb(len(pool), k)\nprint(f\"λ=0.01 vs Null B: p_one={ge/n:.3f}, p_two={tw/n:.3f}, n_combos={n}\")\nprint(f\"  obs_mean={obs:.4f}, pool_mean={mu:.4f}\")\nprint(f\"  ge={ge}, tw={tw}\")\n\n# Also enumerate for Null A to confirm\nnull_a = [56.5, 52.5, 55.0]\npool_a = null_a + lam001\nobs_a = sum(lam001)/k\nmu_a = sum(pool_a)/len(pool_a)\ndev_a = abs(obs_a - mu_a)\nge_a = tw_a = 0\nfor c in combinations(pool_a, k):\n    m = sum(c)/k\n    if m >= obs_a: ge_a += 1\n    if abs(m - mu_a) >= dev_a - 1e-12: tw_a += 1\nn_a = comb(len(pool_a), k)\nprint(f\"\\nλ=0.01 vs Null A: p_one={ge_a/n_a:.3f}, p_two={tw_a/n_a:.3f}, n_combos={n_a}\")\n\n# Enumerate all combos for Null A to double-check\nprint(\"\\nAll C(6,3) combos for λ=0.01 Null A test:\")\nfor c in combinations(pool_a, k):\n    m = sum(c)/k\n    flag_ge = \" >= obs\" if m >= obs_a else \"\"\n    flag_tw = \" |dev|>=\" if abs(m - mu_a) >= dev_a - 1e-12 else \"\"\n    print(f\"  {c} -> mean={m:.4f}{flag_ge}{flag_tw}\")\n\nPYEOF\n",
    "description": "Compute λ=0.01 permutation test against both null pools"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T05:40:12.320715+00:00_

λ=0.01 vs Null B: p_one=0.119, p_two=0.262, n_combos=84
  obs_mean=56.3333, pool_mean=55.1667
  ge=10, tw=22

λ=0.01 vs Null A: p_one=0.200, p_two=0.400, n_combos=20

All C(6,3) combos for λ=0.01 Null A test:
  (56.5, 52.5, 55.0) -> mean=54.6667 |dev|>=
  (56.5, 52.5, 57.0) -> mean=55.3333
  (56.5, 52.5, 57.5) -> mean=55.5000
  (56.5, 52.5, 54.5) -> mean=54.5000 |dev|>=
  (56.5, 55.0, 57.0) -> mean=56.1667
  (56.5, 55.0, 57.5) -> mean=56.3333 >= obs |dev|>=
  (56.5, 55.0, 54.5) -> mean=55.3333
  (56.5, 57.0, 57.5) -> mean=57.0000 >= obs |dev|>=
  (56.5, 57.0, 54.5) -> mean=56.0000
  (56.5, 57.5, 54.5) -> mean=56.1667
  (52.5, 55.0, 57.0) -> mean=54.8333
  (52.5, 55.0, 57.5) -> mean=55.0000
  (52.5, 55.0, 54.5) -> mean=54.0000 |dev|>=
  (52.5, 57.0, 57.5) -> mean=55.6667
  (52.5, 57.0, 54.5) -> mean=54.6667 |dev|>=
  (52.5, 57.5, 54.5) -> mean=54.8333
  (55.0, 57.0, 57.5) -> mean=56.5000 >= obs |dev|>=
  (55.0, 57.0, 54.5) -> mean=55.5000
  (55.0, 57.5, 54.5) -> mean=55.6667
  (57.0, 57.5, 54.5) -> mean=56.3333 >= obs |dev|>=

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T05:40:12.320942+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}",
  "new_string": "\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}",
    "new_string": "\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T05:40:12.321140+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T05:40:12.321279+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\nA Phase~2 ablation reinforces this conclusion.",
  "new_string": "the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "old_string": "the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\nA Phase~2 ablation reinforces this conclusion.",
    "new_string": "the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T05:40:12.321543+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T05:40:12.321702+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.",
  "new_string": "A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "old_string": "A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.",
    "new_string": "A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T05:40:12.321922+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T05:40:12.322074+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/paper_switch.py --verify",
  "description": "Verify paper_switch.py templates still match"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/paper_switch.py --verify",
    "description": "Verify paper_switch.py templates still match"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T05:40:12.322212+00:00_

--- Scenario B (10 items) ---
  [OK]      abstract L5 training                abstract.tex
  [OK]      abstract L6 conclusion              abstract.tex
  [OK]      claim3 L3 scope                     claim3.tex
  [OK]      claim3 L7 caption                   claim3.tex
  [OK]      claim3 L20 table row                claim3.tex
  [OK]      claim3 L27 body                     claim3.tex
  [OK]      claim3 L32-33 dose-response         claim3.tex
  [OK]      claim3 L38 fig caption              claim3.tex
  [OK]      discussion L6                       discussion.tex
  [OK]      discussion L12 limitation           discussion.tex
--- Scenario C (11 items) ---
  [OK]      abstract L5 training                abstract.tex
  [OK]      abstract L6 conclusion              abstract.tex
  [OK]      claim3 L3 scope                     claim3.tex
  [OK]      claim3 L7 caption                   claim3.tex
  [OK]      claim3 L20 table row                claim3.tex
  [OK]      claim3 L27 body                     claim3.tex
  [OK]      claim3 L32-33 dose-response         claim3.tex
  [OK]      claim3 L38 fig caption              claim3.tex
  [OK]      discussion L3 scope                 discussion.tex
  [OK]      discussion L6                       discussion.tex
  [OK]      discussion L12 limitation           discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T05:40:12.322370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T05:40:12.322614+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 3 & 51.5\,$\pm$\,0.0 & 54.67\,$\pm$\,2.02 & 0.391 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{Single seed (s2); 
…[truncated 3917 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T05:40:12.322797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "offset": "173",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "offset": "173",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T05:40:12.322959+00:00_

173	\section{Null Distribution for SDF Loss Weight Analysis}
174	\label{sec:appendix_null}
175	
176	We construct a null distribution by pooling the three LoRA-only seeds and three $\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\% (LoRA s0, re-evaluated), 52.5\% (LoRA s1), 55.0\% (LoRA s2), 57.0\% ($\lambda{=}0.005$ s0), 54.0\% ($\lambda{=}0.005$ s1), 52.5\% ($\lambda{=}0.005$ s2), yielding mean 54.58\% and standard deviation 1.93\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\lambda = 0.005$ produces no separation from LoRA-only. The $\lambda = 0.01$ mean of 56.33\% falls within $0.8\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\lambda = 0.1$ 30K mean of 57.00\% (3 seeds: 58.0\%, 58.5\%, 54.5\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\alpha = 0.05$).
177	
178	The permutation test makes no distributional assumptions. Pooling the six null values $\{56.5, 52.5, 55, 57, 54, 52.5\}$ and three $\lambda = 0.1$ values $\{58, 58.5, 54.5\}$ into nine measurements, we enumerate all $\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \approx 0.131$. With the third seed ($s_2 = 54.5\%$) pulling the $\lambda = 0.1$ mean from 58.25\% (2 seeds) down to 57.00\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.
179	
180	\paragraph{Alternative null construction (Null~A).}
181	If only the three LoRA-only seeds are used as the null pool ($\{56.5, 52.5, 55.0\}$), we obtain $\binom{6}{3} = 20$ permutations for each comparison. For $\lambda = 0.1$ (treatment mean
…[truncated 1919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-28T05:40:12.323157+00:00_

All edits applied, all paper_switch.py templates verified. Here's the summary:

---

## Changes Made

### claim3.tex (lines 34–41 added)

| Line | Change |
|------|--------|
| 34–35 | **NEW** `\paragraph{Robustness to null construction.}` — Reports Null A (LoRA-only, p_two=0.300) and Null B (p_two=0.131), both non-significant |
| 37–38 | **NEW** `\paragraph{Statistical power.}` — MDE ≈ 5.0 pp at 80% power; observed effect ~2.3 pp is underpowered |
| 40–41 | **NEW** `\paragraph{Evaluation-seed consistency.}` — References Appendix J (+1.5/+2.5/+5.5 pp, σ=0.9 vs 2.0), concludes with cautious "cannot be resolved at current sample size" |

### appendix.tex

| Line | Change |
|------|--------|
| 180–181 | **NEW** `\paragraph{Alternative null construction (Null~A).}` — Exact p-values for λ=0.1 (p_two=0.300) and λ=0.01 (p_two=0.400) under Null A; also λ=0.01 under Null B (p_two=0.262) |
| 183 | **MODIFIED** Phase 2 ablation: 57.5% → 58.0%, "steps 5K–30K" → "steps 5K–18K", added "at the 18K checkpoint (13K steps of Phase~2 training)" + footnote about disk constraints |

---

## Managed Blocks Requiring Your Attention (flagged, not modified)

These contain absolute wording ("redundant", "no measurable benefit", etc.) or the 57.5% value, but are managed by paper_switch.py:

1. **claim3.tex L7** (caption): "SDF adds no measurable CAR beyond LoRA-only across the full tested range"
2. **claim3.tex L26** (body): "Adding SDF supervision produces no measurable benefit across the full tested range" + "confirming that SDF gradients produce no lasting behavioral effect" + **"CAR\,=\,57.5\%"** (Phase 2, needs → 58.0%)
3. **claim3.tex L32** (dose-response): "SDF supervision is redundant with the demonstration signal across the full tested range"
4. **claim3.tex L46** (fig caption): "confirming full redundancy of EE-only SDF supervision"

All four need updating in `paper_switch.py`'s `old` and `new` templates (both Scenario B and C) to:
- Replace absolute wording with cautious phrasing
- Change `57.5\%` → `58.0\%` with the 18K checkpoint note

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_p0-2-5-statistics-phase2_20260528T053501"
}
```

</details>

---
