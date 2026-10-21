# analysis bootstrap ci update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_bootstrap-ci-update_20260516T174322.jsonl`
- **Structured JSON:** [`61e125af8d906c8cbcd1.json`](../../sessions/61/61e125af8d906c8cbcd1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-16T17:44:57.809337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T17:44:57.809748+00:00_

1	# Bootstrap 95% Confidence Intervals — Event-Gated Adaptive Horizon
2	
3	N_BOOTSTRAP = 10,000 resamples. Date: 2026-05-16.
4	
5	## Per-Condition Metrics
6	
7	| Condition | Metric | n | Mean | 95% CI Lower | 95% CI Upper | Adequate? |
8	|-----------|--------|---|------|--------------|--------------|-----------|
9	| trained_dt_emb | nve_peak | 3 | 3.430 | 2.050 | 4.120 | ✓ |
10	| trained_dt_emb | nve_sustained_avg | 3 | 1.775 | 1.030 | 2.425 | ✓ |
11	| trained_dt_emb | eval_return_peak | 3 | 231.920 | 167.220 | 278.540 | ✓ |
12	| trained_dt_emb | eval_return_final | 3 | 160.587 | 82.750 | 267.930 | ✓ |
13	| trained_dt_emb | collapse_rate | 3 | 0.667 | 0.000 | 1.000 | ✓ |
14	| no_dt_emb | nve_peak | 2 | 1.140 | 1.020 | 1.260 | ⚠️ n<3 |
15	| no_dt_emb | nve_sustained_avg | 2 | 0.710 | 0.650 | 0.770 | ⚠️ n<3 |
16	| no_dt_emb | eval_return_peak | 2 | 431.070 | 359.140 | 503.000 | ⚠️ n<3 |
17	| no_dt_emb | eval_return_final | 2 | 325.670 | 148.340 | 503.000 | ⚠️ n<3 |
18	| no_dt_emb | collapse_rate | 2 | 0.000 | 0.000 | 0.000 | ⚠️ n<3 |
19	| SGS_partial | nve_peak | 1 | 10.420 | 10.420 | 10.420 | ⚠️ n<3 |
20	| SGS_partial | nve_sustained_avg | 1 | 2.460 | 2.460 | 2.460 | ⚠️ n<3 |
21	| SGS_partial | eval_return_peak | 1 | 326.670 | 326.670 | 326.670 | ⚠️ n<3 |
22	| SGS_partial | eval_return_final | 1 | 31.730 | 31.730 | 31.730 | ⚠️ n<3 |
23	| SGS_partial | collapse_rate | 1 | 1.000 | 0.000 | 1.000 | ⚠️ n<3 |
24	| SGS_full | nve_peak | 1 | 0.720 | 0.720 | 0.720 | ⚠️ n<3 |
25	| SGS_full | nve_sustained_avg | 1 | 0.550 | 0.550 | 0.550 | ⚠️ n<3 |
26	| SGS_full | eval_return_peak | 1 | 915.700 | 915.700 | 915.700 | ⚠️ n<3 |
27	| SGS_full | eval_return_final | 1 | 915.700 | 915.700 | 915.700 | ⚠️ n<3 |
28	| SGS_full | collapse_rate | 1 | 0.000 | 0.000 | 1.000 | ⚠️ n<3 |
29	| frozen_dt_emb | nve_peak | 1 | 0.467 | 0.467 | 0.467 | ⚠️ n<3 |
30	| frozen_dt_emb | nve_sustained_avg | 1 | 0.427 | 0.427 | 0.427 | ⚠️ n<3 |
31	| frozen_dt_emb | eval_return_peak | 1 | 238.400 | 238.400 | 
…[truncated 3135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T17:44:57.810101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/compute_bootstrap_cis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/compute_bootstrap_cis.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T17:44:57.810436+00:00_

1	"""
2	Bootstrap Confidence Intervals for Event-Gated Adaptive Horizon (CoRL 2026).
3	Action item D8: NVE peaks, collapse rates, cross-env classification CIs.
4	"""
5	import numpy as np
6	from collections import OrderedDict
7	
8	np.random.seed(42)
9	N_BOOTSTRAP = 10000
10	
11	# =============================================================================
12	# Raw data from registry (DONE experiments only)
13	# =============================================================================
14	
15	# --- Condition: trained_dt_emb (subsample ON, trained dt_emb, dt=2 imag, H=8) ---
16	# 008d (seed 0, 55K steps) -> continuation is 009e (seed 1, 105K steps, shares 008d's first 55K)
17	# 009b (seed 2, 105K steps, self-corrected)
18	# NOTE: 008d and 009e share first 55K identically. For independence, we use:
19	#   - 009e as the full 105K run for seed 1
20	#   - 009b as seed 2
21	#   - 008d's 55K-only data as seed 0 (shorter run, distinct seed)
22	trained_dt_emb = {
23	    "nve_peak": [4.12, 4.12, 2.05],        # 008d(s0), 009e(s1), 009b(s2)
24	    "nve_sustained_max": [4.12, 4.12, 2.05],
25	    "nve_sustained_avg": [2.425, 1.87, 1.03],
26	    "eval_return_peak": [167.22, 250.0, 278.54],
27	    "eval_return_final": [82.75, 131.08, 267.93],
28	    "collapse": [1, 1, 0],  # 008d collapsed, 009e collapsed, 009b self-corrected
29	}
30	
31	# --- Condition: no_dt_emb (subsample ON, dt_embed_dim=0, dt=2 imag, H=8) ---
32	# 008f (seed 1), 009c (seed 2)
33	no_dt_emb = {
34	    "nve_peak": [1.02, 1.26],
35	    "nve_sustained_max": [1.02, 1.26],
36	    "nve_sustained_avg": [0.65, 0.77],
37	    "eval_return_peak": [503.0, 359.14],
38	    "eval_return_final": [503.0, 148.34],
39	    "collapse": [0, 0],
40	}
41	
42	# --- Condition: SGS_partial (reward_dt_emb_detach only, trained dt_emb) ---
43	# 016e (seed 1)
44	sgs_partial = {
45	    "nve_peak": [10.42],
46	    "nve_sustained_max": [10.42],
47	    "nve_sustained_avg": [2.46],
48	    "eval_return_peak": [326.67],
49	    "eval_return_final"
…[truncated 13925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T17:44:57.810673+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/compute_bootstrap_cis.py",
  "old_string": "# --- Condition: SGS_full (detach ALL non-KL grads from dt_emb) ---\n# 018 (seed 1)\nsgs_full = {\n    \"nve_peak\": [0.72],\n    \"nve_sustained_max\": [0.72],\n    \"nve_sustained_avg\": [0.55],\n    \"eval_return_peak\": [915.7],\n    \"eval_return_final\": [915.7],\n    \"collapse\": [0],\n}",
  "new_string": "# --- Condition: SGS_full (detach ALL non-KL grads from dt_emb) ---\n# 018v2 (seed 1) — replaces invalid 018 (gate_enabled=false config error)\n# Need seed 2 for replication\nsgs_full = {\n    \"nve_peak\": [4.01],           # 018v2: peak at 25K\n    \"nve_sustained_max\": [4.01],\n    \"nve_sustained_avg\": [1.34],  # 018v2: NVE final\n    \"eval_return_peak\": [448.34], # 018v2: eval@105K\n    \"eval_return_final\": [448.34],\n    \"collapse\": [0],\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/compute_bootstrap_cis.py",
    "old_string": "# --- Condition: SGS_full (detach ALL non-KL grads from dt_emb) ---\n# 018 (seed 1)\nsgs_full = {\n    \"nve_peak\": [0.72],\n    \"nve_sustained_max\": [0.72],\n    \"nve_sustained_avg\": [0.55],\n    \"eval_return_peak\": [915.7],\n    \"eval_return_final\": [915.7],\n    \"collapse\": [0],\n}",
    "new_string": "# --- Condition: SGS_full (detach ALL non-KL grads from dt_emb) ---\n# 018v2 (seed 1) — replaces invalid 018 (gate_enabled=false config error)\n# Need seed 2 for replication\nsgs_full = {\n    \"nve_peak\": [4.01],           # 018v2: peak at 25K\n    \"nve_sustained_max\": [4.01],\n    \"nve_sustained_avg\": [1.34],  # 018v2: NVE final\n    \"eval_return_peak\": [448.34], # 018v2: eval@105K\n    \"eval_return_final\": [448.34],\n    \"collapse\": [0],\n}"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T17:44:57.810975+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/compute_bootstrap_cis.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T17:44:57.811164+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis && python3 compute_bootstrap_cis.py 2>&1 | tail -40",
  "description": "Run bootstrap CI script to regenerate summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis && python3 compute_bootstrap_cis.py 2>&1 | tail -40",
    "description": "Run bootstrap CI script to regenerate summary"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T17:44:57.811338+00:00_

EFFECT SIZE: trained_dt_emb vs no_dt_emb (difference of means ± 95% CI)
==========================================================================================
  Δ nve_peak                 :    +2.29  [   +0.91,    +3.10]
  Δ nve_sustained_avg        :    +1.07  [   +0.32,    +1.71]
  Δ eval_return_peak         :  -199.15  [ -308.19,   -90.11]
  Δ collapse_rate            :   +0.667  [  +0.000,   +1.000]

==========================================================================================
NVE > 1.5x THRESHOLD EXCEEDANCE RATE (collapse indicator)
==========================================================================================
  trained_dt_emb           : 1.000  [1.000, 1.000]  (n=3)
  no_dt_emb                : 0.000  [0.000, 0.000]  (n=2) ⚠️  n<3
  SGS_partial              : 1.000  [0.000, 1.000]  (n=1) ⚠️  n<3
  SGS_full                 : 1.000  [0.000, 1.000]  (n=1) ⚠️  n<3
  frozen_dt_emb            : 0.000  [0.000, 1.000]  (n=1) ⚠️  n<3
  no_subsample             : 0.000  [0.000, 1.000]  (n=1) ⚠️  n<3
  dt1_imag                 : 1.000  [0.000, 1.000]  (n=1) ⚠️  n<3

==========================================================================================
CROSS-ENVIRONMENT CLASSIFICATION (CIVO)
==========================================================================================
  NOTE: Only 1 Cheetah Run experiment (010a, baseline only).
  Cross-env classification CIs cannot be meaningfully computed
  with current data. All treatment conditions are Walker Walk only.
  Recommend: run at least 2-3 Cheetah seeds with trained_dt_emb and no_dt_emb.

==========================================================================================
SAMPLE SIZE ADEQUACY
==========================================================================================
  trained_dt_emb           : n=3  ✓ adequate
  no_dt_emb                : n=2  ⚠️  INSUFFICIENT (n=2, need ≥3)
  SGS_partial              : n=1  ⚠️  INSUFFICIENT (n=1, need ≥3)
  SGS_full         
…[truncated 445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T17:44:57.811512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T17:44:57.811676+00:00_

1	# Bootstrap 95% Confidence Intervals — Event-Gated Adaptive Horizon
2	
3	N_BOOTSTRAP = 10,000 resamples. Date: 2026-05-16.
4	
5	## Per-Condition Metrics
6	
7	| Condition | Metric | n | Mean | 95% CI Lower | 95% CI Upper | Adequate? |
8	|-----------|--------|---|------|--------------|--------------|-----------|
9	| trained_dt_emb | nve_peak | 3 | 3.430 | 2.050 | 4.120 | ✓ |
10	| trained_dt_emb | nve_sustained_avg | 3 | 1.775 | 1.030 | 2.425 | ✓ |
11	| trained_dt_emb | eval_return_peak | 3 | 231.920 | 167.220 | 278.540 | ✓ |
12	| trained_dt_emb | eval_return_final | 3 | 160.587 | 82.750 | 267.930 | ✓ |
13	| trained_dt_emb | collapse_rate | 3 | 0.667 | 0.000 | 1.000 | ✓ |
14	| no_dt_emb | nve_peak | 2 | 1.140 | 1.020 | 1.260 | ⚠️ n<3 |
15	| no_dt_emb | nve_sustained_avg | 2 | 0.710 | 0.650 | 0.770 | ⚠️ n<3 |
16	| no_dt_emb | eval_return_peak | 2 | 431.070 | 359.140 | 503.000 | ⚠️ n<3 |
17	| no_dt_emb | eval_return_final | 2 | 325.670 | 148.340 | 503.000 | ⚠️ n<3 |
18	| no_dt_emb | collapse_rate | 2 | 0.000 | 0.000 | 0.000 | ⚠️ n<3 |
19	| SGS_partial | nve_peak | 1 | 10.420 | 10.420 | 10.420 | ⚠️ n<3 |
20	| SGS_partial | nve_sustained_avg | 1 | 2.460 | 2.460 | 2.460 | ⚠️ n<3 |
21	| SGS_partial | eval_return_peak | 1 | 326.670 | 326.670 | 326.670 | ⚠️ n<3 |
22	| SGS_partial | eval_return_final | 1 | 31.730 | 31.730 | 31.730 | ⚠️ n<3 |
23	| SGS_partial | collapse_rate | 1 | 1.000 | 0.000 | 1.000 | ⚠️ n<3 |
24	| SGS_full | nve_peak | 1 | 4.010 | 4.010 | 4.010 | ⚠️ n<3 |
25	| SGS_full | nve_sustained_avg | 1 | 1.340 | 1.340 | 1.340 | ⚠️ n<3 |
26	| SGS_full | eval_return_peak | 1 | 448.340 | 448.340 | 448.340 | ⚠️ n<3 |
27	| SGS_full | eval_return_final | 1 | 448.340 | 448.340 | 448.340 | ⚠️ n<3 |
28	| SGS_full | collapse_rate | 1 | 0.000 | 0.000 | 1.000 | ⚠️ n<3 |
29	| frozen_dt_emb | nve_peak | 1 | 0.467 | 0.467 | 0.467 | ⚠️ n<3 |
30	| frozen_dt_emb | nve_sustained_avg | 1 | 0.427 | 0.427 | 0.427 | ⚠️ n<3 |
31	| frozen_dt_emb | eval_return_peak | 1 | 238.400 | 238.400 | 
…[truncated 3135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T17:44:57.811905+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md",
  "old_string": "## Effect Sizes: trained_dt_emb − no_dt_emb",
  "new_string": "## Effect Sizes: trained_dt_emb − no_dt_emb (bootstrap)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md",
    "old_string": "## Effect Sizes: trained_dt_emb − no_dt_emb",
    "new_string": "## Effect Sizes: trained_dt_emb − no_dt_emb (bootstrap)"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T17:44:57.812107+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T17:44:57.812253+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md",
  "old_string": "## Cross-Environment Classification\n\n**Cannot compute.** Only 1 Cheetah Run experiment exists (baseline 010a).\nAll treatment conditions are Walker Walk only.\n\n**Recommendation:** Run 2-3 Cheetah seeds each for trained_dt_emb and no_dt_emb conditions.\n\n## Sample Size Notes",
  "new_string": "## Effect Sizes: SGS_full − trained_dt_emb (point estimates, n=1 vs n=3)\n\n| Metric | SGS_full | trained_dt_emb (mean) | Δ | Note |\n|--------|----------|----------------------|---|------|\n| nve_peak | 4.010 | 3.430 | +0.580 | Both show NVE amplification |\n| nve_sustained_avg | 1.340 | 1.775 | −0.435 | SGS_full sustains less |\n| eval_return_peak | 448.340 | 231.920 | +216.420 | SGS_full much higher return |\n| eval_return_final | 448.340 | 160.587 | +287.753 | No collapse in SGS_full |\n| collapse_rate | 0.000 | 0.667 | −0.667 | SGS_full avoids collapse |\n\n> **Caveat:** SGS_full has n=1 (018v2 only). No CI can be computed. Need seed 2 to confirm.\n\n## Cross-Environment Classification\n\n**Cannot compute.** Only 1 Cheetah Run experiment exists (baseline 010a).\nAll treatment conditions are Walker Walk only.\n\n**Recommendation:** Run 2-3 Cheetah seeds each for trained_dt_emb and no_dt_emb conditions.\n\n## Sample Size Notes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md",
    "old_string": "## Cross-Environment Classification\n\n**Cannot compute.** Only 1 Cheetah Run experiment exists (baseline 010a).\nAll treatment conditions are Walker Walk only.\n\n**Recommendation:** Run 2-3 Cheetah seeds each for trained_dt_emb and no_dt_emb conditions.\n\n## Sample Size Notes",
    "new_string": "## Effect Sizes: SGS_full − trained_dt_emb (point estimates, n=1 vs n=3)\n\n| Metric | SGS_full | trained_dt_emb (mean) | Δ | Note |\n|--------|----------|----------------------|---|------|\n| nve_peak | 4.010 | 3.430 | +0.580 | Both show NVE amplification |\n| nve_sustained_avg | 1.340 | 1.775 | −0.435 | SGS_full sustains less |\n| eval_return_peak | 448.340 | 231.920 | +216.420 | SGS_full much higher return |\n| eval_return_final | 448.340 | 160.587 | +287.753 | No collapse in SGS_full |\n| collapse_rate | 0.000 | 0.667 | −0.667 | SGS_full avoids collapse |\n\n> **Caveat:** SGS_full has n=1 (018v2 only). No CI can be computed. Need seed 2 to confirm.\n\n## Cross-Environment Classification\n\n**Cannot compute.** Only 1 Cheetah Run experiment exists (baseline 010a).\nAll treatment conditions are Walker Walk only.\n\n**Recommendation:** Run 2-3 Cheetah seeds each for trained_dt_emb and no_dt_emb conditions.\n\n## Sample Size Notes"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T17:44:57.812424+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T17:44:57.812558+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md",
  "old_string": "- **trained_dt_emb**: 008d (seed 0, 55K) and 009e (seed 1, 105K) share first 55K steps.\n  For NVE peak at 55K they are effectively the same observation.\n  Conservative effective n=2 for this condition.\n- **no_dt_emb**: 2 fully independent seeds (008f s1, 009c s2).\n- **All other conditions**: single seed only — CIs are degenerate (point estimates).",
  "new_string": "- **trained_dt_emb**: 008d (seed 0, 55K) and 009e (seed 1, 105K) share first 55K steps.\n  For NVE peak at 55K they are effectively the same observation.\n  Conservative effective n=2 for this condition.\n- **no_dt_emb**: 2 fully independent seeds (008f s1, 009c s2).\n- **SGS_full**: 018v2 (seed 1) only. Exp 018 excluded — invalid config (gate_enabled=false, not actually SGS). Need seed 2.\n- **All other conditions**: single seed only — CIs are degenerate (point estimates)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md",
    "old_string": "- **trained_dt_emb**: 008d (seed 0, 55K) and 009e (seed 1, 105K) share first 55K steps.\n  For NVE peak at 55K they are effectively the same observation.\n  Conservative effective n=2 for this condition.\n- **no_dt_emb**: 2 fully independent seeds (008f s1, 009c s2).\n- **All other conditions**: single seed only — CIs are degenerate (point estimates).",
    "new_string": "- **trained_dt_emb**: 008d (seed 0, 55K) and 009e (seed 1, 105K) share first 55K steps.\n  For NVE peak at 55K they are effectively the same observation.\n  Conservative effective n=2 for this condition.\n- **no_dt_emb**: 2 fully independent seeds (008f s1, 009c s2).\n- **SGS_full**: 018v2 (seed 1) only. Exp 018 excluded — invalid config (gate_enabled=false, not actually SGS). Need seed 2.\n- **All other conditions**: single seed only — CIs are degenerate (point estimates)."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T17:44:57.812717+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T17:44:57.812888+00:00_

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
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
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

_source line 18 · 2026-05-16T17:44:57.813023+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T17:44:57.813142+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "bootstrap_ci_summary_v2",
  "type": "report",
  "description": "Bootstrap 95% CI summary updated with 018v2 real data for SGS_full (replacing invalid 018). Includes SGS_full vs trained_dt_emb effect sizes.",
  "project": "event-gated-adaptive-horizon",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md",
  "tags": "['bootstrap', 'CI', '018v2', 'SGS_full', 'statistics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "bootstrap_ci_summary_v2",
    "type": "report",
    "description": "Bootstrap 95% CI summary updated with 018v2 real data for SGS_full (replacing invalid 018). Includes SGS_full vs trained_dt_emb effect sizes.",
    "project": "event-gated-adaptive-horizon",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md",
    "tags": "['bootstrap', 'CI', '018v2', 'SGS_full', 'statistics']"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T17:44:57.813290+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_57cb8e\", \"name\": \"bootstrap_ci_summary_v2\", \"type\": \"report\", \"description\": \"Bootstrap 95% CI summary updated with 018v2 real data for SGS_full (replacing invalid 018). Includes SGS_full vs trained_dt_emb effect sizes.\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/bootstrap_ci_summary.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T17:44:49.069297+00:00\", \"tags\": [\"bootstrap\", \"CI\", \"018v2\", \"SGS_full\", \"statistics\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T17:44:57.813460+00:00_

完成。更新内容：

1. **脚本** (`compute_bootstrap_cis.py`): SGS_full 数据替换为 018v2（NVE peak=4.01, eval=448.34, collapse=0），注释标注 018 无效原因
2. **汇总** (`bootstrap_ci_summary.md`):
   - SGS_full 行已更新为 018v2 point estimates
   - NVE >1.5× exceedance: SGS_full 从 0.000 → 1.000（4.01 > 1.5）
   - 新增 "SGS_full − trained_dt_emb" effect size 表（eval +216, collapse −0.667）
   - Independence Notes 中标注 018 排除原因和 seed 2 需求

关键发现：SGS_full (018v2) 比 trained_dt_emb 的 eval return 高 +216（448 vs 232），且无 collapse，但 n=1 无法计算 CI。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_bootstrap-ci-update_20260516T174322"
}
```

</details>

---
